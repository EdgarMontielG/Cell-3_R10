#!/usr/bin/env python3
"""Tests of tools/audit_backup.py on synthetic robot backups.

    python3 tools/test_audit_backup.py        (from the repository root)

Each test builds a KUKA archive zip in a temporary directory - the cleaned
archive (the archive files of HEAD) with one deliberate change - runs the
audit on it and checks the report. The entries keep the order and the
timestamps of the original archive 658424 when that zip is available
(AUDIT_ORIGINAL_ZIP, default the path it was uploaded to); otherwise the
backup is built from git alone, which gives the same contents.

The cleaned archive and the audit base are AUDIT_TEST_REF (default HEAD).
The edits anchor on lines of the cleaned program (e.g. the first 'WAIT SEC
0.2' of centerline_weld.src); once audited fixes are committed and an
anchor is gone, run with AUDIT_TEST_REF=<the cleanup commit>.
"""
import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
import warnings
import zipfile
from xml.sax.saxutils import escape

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, 'tools'))
import audit_backup as ab  # noqa: E402

REF = os.environ.get('AUDIT_TEST_REF', 'HEAD')
ORIGINAL = os.environ.get(
    'AUDIT_ORIGINAL_ZIP',
    '/root/.claude/uploads/50f56c92-2919-5ae3-94c9-0de4476bbe87/667d8b38-v431_03_10_r1.zip')

WELD = 'KRC/R1/Program/Centerline/centerline_weld.src'
DROP = 'KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src'
PICK2 = 'KRC/R1/Program/StylePicks/Options/style1pick1opt2.src'
CELL = 'KRC/R1/cell.src'
PRELOAD = 'KRC/R1/Program/Centerline/PRELOAD.src'
MAYBEHOME = 'KRC/R1/Program/POUNCE.src'
APP1 = 'KRC/R1/Program/StyleApps/Options/style1app1opt1A.src'
APP1_DAT = 'KRC/R1/Program/StyleApps/Options/style1app1opt1A.dat'
CONFIG = 'KRC/R1/System/$config.dat'
ACDATA = 'KRC/R1/TP/AutomationCore/automationcoredata.dat'
CYCLE_DAT = 'KRC/R1/Program/Centerline/CL_CYCLE_TIME.dat'


def archive_files(ref):
    """{path: bytes} of the archive files (KRC/, C/, Registry/, am.ini) of a commit."""
    tree = {p: b for p, b in ab.tree_blobs(ref).items() if ab.is_archive_path(p)}
    blobs = ab.read_blobs(tree.values())
    return {p: blobs[b] for p, b in tree.items()}


class BackupTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.clean = archive_files(REF)
        cls.first = archive_files(ab.first_commit())
        cls.order = sorted(cls.clean)
        cls.stamps = {}
        if os.path.exists(ORIGINAL):
            with zipfile.ZipFile(ORIGINAL) as z:
                listed = [i.filename for i in z.infolist()]
                cls.stamps = {i.filename: i.date_time for i in z.infolist()}
            cls.order = [n for n in listed if n in cls.clean] + \
                sorted(set(cls.clean) - set(listed))

    def setUp(self):
        # check_cleanup.load_allowlist() leaves its json files to the garbage collector
        warnings.filterwarnings('ignore', category=ResourceWarning,
                                message=r'unclosed file .*cleanup_allowlist')
        self._tmp = tempfile.TemporaryDirectory(prefix='audit_test_')
        self.tmp = self._tmp.name

    def tearDown(self):
        self._tmp.cleanup()

    # -- helpers ------------------------------------------------------

    def text(self, path):
        return self.clean[path].decode('latin-1')

    def backup(self, changes=None, name='backup.zip'):
        """Write the cleaned archive with `changes` ({path: bytes | str | None})
        applied - None removes the entry - plus one 'Log Files/' entry."""
        changes = changes or {}
        files = dict(self.clean)
        for path, data in changes.items():
            if data is None:
                files.pop(path, None)
            else:
                files[path] = data.encode('latin-1') if isinstance(data, str) else data
        order = [p for p in self.order if p in files] + sorted(set(files) - set(self.order))
        dest = os.path.join(self.tmp, name)
        with zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED) as z:
            for p in order:
                info = zipfile.ZipInfo(p, self.stamps.get(p, (2026, 10, 3, 20, 21, 48)))
                info.compress_type = zipfile.ZIP_DEFLATED
                z.writestr(info, files[p])
            z.writestr('Log Files/KrcLog.log', b'not audited')
        return dest

    def audit(self, zip_path, *extra):
        out = os.path.join(self.tmp, 'report')
        with contextlib.redirect_stdout(io.StringIO()) as buf:
            summary = ab.main([zip_path, '--base', REF, '--out', out] + list(extra))
        self.stdout = buf.getvalue()
        with open(os.path.join(out, 'AUDIT.md'), encoding='utf-8') as f:
            self.report = f.read()
        with open(os.path.join(out, 'summary.json'), encoding='utf-8') as f:
            self.assertEqual(json.load(f)['counts'], summary['counts'])
        self.out = out
        return summary

    def findings(self, summary, check, level=None, path=None):
        return [f for f in summary['findings'] if f['check'] == check
                and (level is None or f['level'] == level) and (path is None or f['file'] == path)]

    def edit(self, path, old, new, count=1):
        text = self.text(path)
        self.assertIn(old, text, f'test anchor missing in {path}')
        return text.replace(old, new, count)

    # -- (a) ----------------------------------------------------------

    def test_a_clean_archive_unchanged(self):
        s = self.audit(self.backup())
        c = s['counts']
        self.assertEqual((c['changed'], c['added'], c['missing'], c['unexpected']), (0, 0, 0, 0))
        self.assertEqual(c['unchanged'], len(self.clean))
        self.assertEqual((c['code_changed_files'], c['FAIL'], c['WARN'], c['INFO']), (0, 0, 0, 0))
        self.assertEqual((c['deleted_still_present'], c['pre_cleanup']), (0, 0))
        self.assertEqual(s['backup']['log_entries_skipped'], 1)
        self.assertTrue(s['backup']['serial_ok'])
        self.assertEqual(s['backup']['am_ini']['serial'], '658424')
        self.assertFalse([a for a in s['alerts'] if a[0] == 'FAIL'])
        self.assertIn('identical to the base', self.report)

    # -- (b) ----------------------------------------------------------

    def test_b_code_change_reported(self):
        s = self.audit(self.backup({WELD: self.edit(WELD, 'WAIT SEC 0.2', 'WAIT SEC 0.3')}))
        self.assertEqual(s['changed'], [WELD])
        f = s['files'][WELD]
        self.assertEqual((f['code_removed'], f['code_added'], f['comment_only_changes']), (1, 1, 0))
        self.assertEqual(s['counts']['code_changed_files'], 1)
        self.assertEqual(s['counts']['FAIL'], 0)
        self.assertRegex(self.report, r'-\s+\d+\s+WAIT SEC 0\.2')
        self.assertRegex(self.report, r'\+\s+\d+\s+WAIT SEC 0\.3')
        diff = os.path.join(self.out, *f['diff'].split('/'))
        with open(diff, encoding='utf-8') as fh:
            self.assertIn('+WAIT SEC 0.3', fh.read())

    # -- (c) ----------------------------------------------------------

    def test_c_out_form_data_disagrees_with_body(self):
        # Only the hidden form data changes: a comment for the compiler, a set
        # instead of a reset the next time someone confirms the form (F20).
        s = self.audit(self.backup({DROP: self.edit(DROP, '%P 2:18, 3:do018PartInGripper1, 5:FALSE, 6:',
                                                    '%P 2:18, 3:do018PartInGripper1, 5:TRUE, 6:')}))
        self.assertEqual(s['counts']['code_changed_files'], 0)
        fails = self.findings(s, 4, 'FAIL', DROP)
        self.assertTrue(any('form data 5:TRUE but the body sets $OUT[18]=FALSE' in f['message']
                            for f in fails), fails)
        self.assertTrue(any('fold text shows State=FALSE, form data 5:TRUE' in f['message'] for f in fails))

    # -- (d) ----------------------------------------------------------

    def test_d_hand_typed_trigger_in_ptp_fold(self):
        drop = self.edit(DROP, 'FDAT_ACT=FP2\r\n',
                         'FDAT_ACT=FP2\r\nTRIGGER WHEN DISTANCE=0 DELAY=0 DO $OUT[5]=TRUE\r\n')
        # A comment-only edit in a file that already holds two known hand-typed
        # TRIGGERs (F32) must not report them again.
        pick = self.edit(PICK2, ';APPROACH PICKUP - P10', ';APPROACH PICKUP - P10 (EDITED)')
        s = self.audit(self.backup({DROP: drop, PICK2: pick}))
        warns = self.findings(s, 5, 'WARN')
        self.assertEqual(len(warns), 1, warns)
        self.assertEqual(warns[0]['file'], DROP)
        self.assertIn('TRIGGER WHEN DISTANCE=0 DELAY=0 DO $OUT[5]=TRUE', warns[0]['message'])
        self.assertIn('lost on Touch Up (F32)', warns[0]['message'])
        self.assertFalse(self.findings(s, 4, 'FAIL'))   # the generated lines still agree

    # -- (e) ----------------------------------------------------------

    def test_e_deleted_module_still_present(self):
        s = self.audit(self.backup({MAYBEHOME: self.first[MAYBEHOME]}))
        self.assertEqual([d['path'] for d in s['deleted_still_present']], [MAYBEHOME])
        self.assertEqual(s['deleted_still_present'][0]['state'], 'identical to the archive as received')
        self.assertNotIn(MAYBEHOME, s['added'])
        self.assertEqual(s['counts']['code_changed_files'], 0)
        self.assertTrue(any('still on the controller - delete it there' in a[1] for a in s['alerts']))
        self.assertIn('Deleted modules still present', self.report)

    # -- (f) ----------------------------------------------------------

    def test_f_pre_cleanup_file(self):
        # cell.src: the cleanup changed only its comments, so the pre-cleanup
        # file differs from HEAD in comments only (CENTERLINE_WELD also has
        # code changes since the Gestamp review)
        s = self.audit(self.backup({CELL: self.first[CELL]}))
        self.assertEqual(s['pre_cleanup'], [CELL])
        self.assertEqual(s['counts']['pre_cleanup'], 1)
        self.assertEqual(s['files'][CELL]['code_removed'] + s['files'][CELL]['code_added'], 0)
        self.assertTrue(any('this is the pre-cleanup file' in a[1] for a in s['alerts'] if a[0] == 'FAIL'))
        self.assertIn('FAIL  ' + CELL + ': this is the pre-cleanup file', self.stdout)

    def test_f2_edited_on_top_of_pre_cleanup_file(self):
        old = self.first[WELD].decode('latin-1').replace('WAIT SEC 0.2', 'WAIT SEC 0.3', 1)
        old = old.replace('WAIT SEC 0.3', 'WAIT SEC 0.3\r\n;ESPERAR TUERCA NUEVA', 1)
        s = self.audit(self.backup({WELD: old}))
        self.assertEqual(s['pre_cleanup'], [])
        self.assertEqual(s['pre_cleanup_based'], [WELD])
        # the checks see what the programmer added to the version he started
        # from, not every old comment that version brings back
        spanish = self.findings(s, 7, path=WELD)
        self.assertEqual([f['message'].split(': ;')[1] for f in spanish], ['ESPERAR TUERCA NUEVA'])
        self.assertTrue(any(a[0] == 'FAIL' and 'edited on top of the pre-cleanup file' in a[1]
                            for a in s['alerts']))

    # -- (g) ----------------------------------------------------------

    def test_g_spanish_comment_and_commented_out_code(self):
        weld = self.edit(WELD, 'WAIT SEC 0.2\r\n',
                         'WAIT SEC 0.2\r\n;ESPERAR TUERCA EN POSICION\r\n;$OUT[5]=TRUE\r\n'
                         ';GUN CLOSED - WAIT FOR THE GUN TO SETTLE\r\n')
        s = self.audit(self.backup({WELD: weld}))
        spanish = self.findings(s, 7, 'WARN', WELD)
        commented = self.findings(s, 6, 'WARN', WELD)
        self.assertEqual(len(spanish), 1, spanish)
        self.assertIn('ESPERAR', spanish[0]['message'])
        self.assertIn('TUERCA', spanish[0]['message'])
        self.assertEqual(len(commented), 1, commented)
        self.assertIn('$OUT[5]=TRUE', commented[0]['message'])
        self.assertEqual(commented[0]['line'], spanish[0]['line'] + 1)
        self.assertEqual(s['counts']['code_changed_files'], 0)

    # -- (h) ----------------------------------------------------------

    def test_h_items_claimed_fixed_without_change_is_red_flag(self):
        zip_path = self.backup({WELD: self.edit(WELD, 'WAIT SEC 0.2', 'WAIT SEC 0.3')})
        xlsx = os.path.join(self.tmp, 'puntos.xlsx')
        write_xlsx(xlsx, [
            ['Lista de puntos abiertos R10'],
            [],
            ['Módulos', 'ID', 'Qué cambió el programador', 'Estado', 'Evidencia'],
            ['centerline_weld', 'F25', 'Pulso de alimentación alargado', 'Corregido - por auditar', 'video'],
            ['PRELOAD.src, Request_next_nut', 'F4', 'NUT_READY se activa en dry cycle',
             'Corregido – Por Auditar', ''],
            ['style1app1opt1..5', 'F01', '', 'Abierto', ''],
            ['', 'C21', 'mensajes', 'corregido por auditar', ''],
        ])
        s = self.audit(zip_path, '--items', xlsx)
        items = s['items']
        self.assertEqual(items['sheet'], 'Puntos abiertos')
        self.assertEqual([it['id'] for it in items['claimed']], ['F25', 'F4', 'C21'])
        f25, f04, c21 = items['claimed']
        self.assertIsNone(f25['red_flag'])
        self.assertEqual(f25['code_changed_files'], [WELD])
        self.assertEqual(f04['red_flag'], 'none of its modules changed in this backup')
        self.assertEqual({f['state'] for m in f04['modules'] for f in m['files']}, {'unchanged'})
        self.assertTrue(f04['title'].startswith('Dry cycle hangs'))
        self.assertTrue(f04['cited_base'])
        self.assertEqual(c21['red_flag'], 'no modules listed - the fix cannot be traced to the backup')
        self.assertEqual((s['counts']['items_claimed'], s['counts']['items_red_flags']), (3, 2))
        self.assertIn('RED FLAG: none of its modules changed', self.report)

    def test_o_items_workbook_of_make_items_xlsx(self):
        """The layout tools/make_items_xlsx.py writes: header in row 1, the item's
        'Módulos' and the programmer's 'Módulos modificados', multi-line criteria."""
        opt = 'KRC/R1/Program/StyleApps/Options/style1app1opt%dA.src'
        changes = {opt % k: self.edit(opt % k, '; Gestamp Standards', '; Gestamp Standards - rev 2')
                   for k in (1, 2)}
        zip_path = self.backup(changes)
        heads = ['ID', 'Sev.', 'Punto', 'Tipo', 'Responsable', 'Módulos', 'Criterio de cierre',
                 'Depende de', 'Estado', 'Qué cambió el programador', 'Módulos modificados',
                 'Evidencia / prueba en celda', 'Fecha programador', 'Resultado auditoría',
                 'Fecha auditoría', 'Nota auditoría']
        f01 = ['F01', 'Crítico', 'Entrada al pedestal', 'código', 'Ethos', 'style1app1opt1..5, PRELOAD',
               '• espera supervisada antes del LIN\n• prueba en celda con clamp cerrado', '',
               'Corregido - por auditar', 'espera antes del LIN', 'style1app1opt1A.src, style1app1opt2A.src, style1app1opt3A.src',
               'T1 50 %: se detuvo antes de P22', '2026-10-06', '', '', '']
        f26 = ['F26', 'Bajo', 'Timers', 'documentación', 'Ethos', 'centerline_weld', '', '', 'En proceso',
               '', '', '', '', '', '', '']
        xlsx = os.path.join(self.tmp, 'R10_Puntos_Abiertos.xlsx')
        write_xlsx(xlsx, [heads, f01, f26])
        s = self.audit(zip_path, '--items', xlsx)
        (item,) = s['items']['claimed']
        self.assertEqual(item['id'], 'F01')
        self.assertEqual([m['module'] for m in item['modified']],
                         ['style1app1opt1A.src', 'style1app1opt2A.src', 'style1app1opt3A.src'])
        self.assertEqual(item['red_flag'],
                         'listed as modified by the programmer but unchanged: style1app1opt3A.src')
        self.assertEqual(item['code_changed_files'], [])        # a comment only
        self.assertIn('  - prueba en celda con clamp cerrado', self.report)
        self.assertIn('Only comments changed in its modules', self.report)
        self.assertEqual(s['items']['statuses'], {'Corregido - por auditar': 1, 'En proceso': 1})

    # -- further checks -----------------------------------------------

    def test_i_mechanical_checks(self):
        cell = self.edit(CELL, 'WAIT SEC 5\r\n', 'WAIT SEC 4\r\n')                 # WAIT form, check 4
        drop = self.edit(DROP, 'FDAT_ACT=FP2\r\nBAS(#PTP_PARAMS,100)',
                         'FDAT_ACT=FP2\r\nBAS(#PTP_PARAMS,50)')                     # velocity, check 4
        drop = drop.replace(';LEAVE DROPOFF 1', 'WAIT FOR $IN[467]\r\n;LEAVE DROPOFF 1', 1)  # check 10
        weld = self.edit(WELD, 'WAIT SEC 0.2\r\n',
                         'WAIT SEC 0.2\r\n;GUN HOME - SIGNAL $OUT[18] dopw1_GunHome ON\r\n'  # check 3
                         '$OUT[499]=TRUE\r\n'                                              # check 8
                         'HALT\r\n'                                                        # check 10
                         ';FOLD LEFT OPEN\r\n')                                            # check 1
        new_src = ('&ACCESS RVO1\r\n&REL 1\r\nDEF NEWMOD( )\r\n$OUT[5]=TRUE\r\nEND\r\n')
        s = self.audit(self.backup({CELL: cell, DROP: drop, WELD: weld,
                                    'KRC/R1/Program/newmod.src': new_src}))
        msgs = {(f['check'], f['level'], f['file']): f['message'] for f in s['findings']}
        self.assertIn('form data 3:5 but the body waits WAIT SEC 4', msgs[(4, 'FAIL', CELL)])
        self.assertTrue(any('form data 5:100 expects BAS(#PTP_PARAMS,100)' in f['message']
                            for f in self.findings(s, 4, 'FAIL', DROP)))
        self.assertIn('dopw1_GunHome at $OUT[18]', msgs[(3, 'FAIL', WELD)])
        self.assertIn('$OUT[499]', ' '.join(f['message'] for f in self.findings(s, 8, 'WARN', WELD)))
        self.assertIn('new HALT', ' '.join(f['message'] for f in self.findings(s, 10, 'INFO', WELD)))
        self.assertIn('WAIT FOR with no timeout',
                      ' '.join(f['message'] for f in self.findings(s, 10, 'INFO', DROP)))
        self.assertTrue(self.findings(s, 1, 'FAIL', WELD))
        header = [f['message'] for f in self.findings(s, 9, 'WARN', 'KRC/R1/Program/newmod.src')]
        self.assertEqual(len(header), 2, header)
        self.assertEqual(s['added'], ['KRC/R1/Program/newmod.src'])

    def test_n_data_declarations(self):
        dat_path = DROP[:-4] + '.dat'
        dat = self.text(dat_path)
        start = dat.index('DECL FDAT FP2=')
        dat = dat[:start] + dat[dat.index('\n', start) + 1:]          # FP2 still used by the P2 form
        form = ('\r\n;FOLD PTP P99 Vel=100 % PDAT7 Tool[1]:EOAT 1 Base[0];%{PE}%R 8.3.43,%MKUKATPBASIS,'
                '%CMOVE,%VPTP,%P 1:PTP, 2:P99, 3:, 5:100, 7:PDAT7\r\n$BWDSTART=FALSE\r\nPDAT_ACT=PPDAT7\r\n'
                'FDAT_ACT=FP99\r\nBAS(#PTP_PARAMS,100)\r\nPTP XP99\r\n;ENDFOLD\r\n')
        drop = self.edit(DROP, ';LEAVE DROPOFF 1', form.lstrip() + ';LEAVE DROPOFF 1')
        s = self.audit(self.backup({dat_path: dat, DROP: drop}))
        msgs = [f['message'] for f in self.findings(s, 11, 'FAIL')]
        self.assertTrue(any(m.startswith('FP2 was removed from this file but is still used in ' + DROP)
                            for m in msgs), msgs)
        self.assertEqual(sorted(m.split()[0] for m in msgs if 'new PTP P99 form' in m), ['FP99', 'XP99'])
        self.assertTrue(any('FP2 (FDAT)' in d or 'removed 1 FDAT: FP2' in d
                            for d in s['files'][dat_path]['data_changes']))

    def test_j_serial_missing_and_line_endings(self):
        am = self.text('am.ini').replace('IRSerialNr=658424', 'IRSerialNr=123456')
        preload = self.clean[PRELOAD]
        self.assertNotIn(b'\r\n', preload)          # PRELOAD.src is one of the LF files
        self.assertIn(b'\r\n', self.clean[WELD])
        s = self.audit(self.backup({'am.ini': am, 'KRC/R1/Program/Utilities/RejectGE4.dat': None,
                                    PRELOAD: preload.replace(b'\n', b'\r\n'),
                                    WELD: self.clean[WELD].replace(b'\r\n', b'\n')}))
        self.assertFalse(s['backup']['serial_ok'])
        self.assertTrue(any('ANOTHER ROBOT' in a[1] for a in s['alerts'] if a[0] == 'FAIL'))
        self.assertEqual(s['missing'], ['KRC/R1/Program/Utilities/RejectGE4.dat'])
        self.assertIn('am.ini', s['changed'])
        # LF -> CRLF is what saving on the smartPAD does: INFO; CRLF -> LF: WARN
        self.assertTrue(any('line endings changed from LF to CRLF' in f['message']
                            for f in self.findings(s, 2, 'INFO', PRELOAD)))
        self.assertTrue(any('line endings changed from CRLF to LF' in f['message']
                            for f in self.findings(s, 2, 'WARN', WELD)))
        for p in (PRELOAD, WELD):
            self.assertEqual(s['files'][p]['code_removed'] + s['files'][p]['code_added'], 0)
        # RejectGE4.dat holds the local data of RejectGE4.src: the module no longer compiles
        self.assertTrue(any(a[0] == 'FAIL' and a[1].startswith('KRC/R1/Program/Utilities/RejectGE4.dat is '
                                                               'missing from the backup but its data')
                            for a in s['alerts']), s['alerts'])

    def test_k_import_and_layout(self):
        weld = self.edit(WELD, 'WAIT SEC 0.2', 'WAIT SEC 0.3').encode('latin-1')
        zip_path = self.backup({WELD: weld, MAYBEHOME: self.first[MAYBEHOME],
                                'tools/check_cleanup.py': b'print("replaced")\n'})
        entries, logs, _ = ab.read_backup(zip_path)
        base = {p: b for p, b in ab.tree_blobs(REF).items() if ab.is_archive_path(p)}
        files, cls = ab.classify(entries, base, ab.deleted_modules(base))
        self.assertEqual(logs, 1)
        self.assertEqual(cls['unexpected'], ['tools/check_cleanup.py'])
        self.assertEqual(cls['deleted_present'], [MAYBEHOME])
        self.assertEqual(cls['changed'] + cls['added'], [WELD])
        root = os.path.join(self.tmp, 'tree')
        os.makedirs(os.path.join(root, 'KRC'))
        keep = os.path.join(root, 'KRC', 'keep.txt')
        with open(keep, 'w') as f:
            f.write('untouched')
        with contextlib.redirect_stdout(io.StringIO()):
            written = ab.import_entries(root, files, cls['changed'] + cls['added'], base)
        self.assertEqual(written, [WELD])
        with open(os.path.join(root, *WELD.split('/')), 'rb') as f:
            self.assertEqual(f.read(), weld)
        self.assertTrue(os.path.exists(keep))

    def test_l_xlsx_reader_and_status_variants(self):
        for status in ('Corregido - por auditar', 'Corregido – por auditar', 'CORREGIDO-POR AUDITAR',
                       'corregido por auditar', 'Corregido — Por Auditar'):
            self.assertTrue(ab.is_claimed_fixed(status), status)
        for status in ('Abierto', 'Cerrado', 'Corregido', 'Por auditar', ''):
            self.assertFalse(ab.is_claimed_fixed(status), status)
        self.assertEqual(ab.item_tokens('style1app1opt1..3, PRELOAD.src;sps.sub'),
                         ['style1app1opt1', 'style1app1opt2', 'style1app1opt3', 'PRELOAD.src', 'sps.sub'])
        xlsx = os.path.join(self.tmp, 'm.xlsx')
        write_minimal_xlsx(xlsx, [['ID', 'Estado'], ['F07', 'Corregido - por auditar'], [3, True]])
        sheets = ab.read_xlsx_minimal(xlsx)
        self.assertEqual(sheets['Puntos abiertos'][1], ['F07', 'Corregido - por auditar'])
        self.assertEqual(sheets['Puntos abiertos'][2], ['3', 'TRUE'])
        # A date typed in Excel is a number without openpyxl; '-' or 'N/A' in a
        # modules cell means none, not a module the programmer left unchanged.
        self.assertEqual(ab.item_tokens('-'), [])
        self.assertEqual(ab.item_tokens('N/A; ninguno'), [])
        write_minimal_xlsx(xlsx, [['ID', 'Estado', 'Módulos', 'Módulos modificados', 'Fecha programador'],
                                  ['F07', 'Corregido - por auditar', 'cell', '-', 46301]])
        items = ab.audit_items(xlsx, lambda p: 'code changed', [CELL], {}, {}, {})
        (f07,) = items['claimed']
        self.assertEqual(f07['date'], '2026-10-06')
        self.assertEqual(f07['modified'], [])
        self.assertIsNone(f07['red_flag'])

    def test_m_head_forms_and_code_lines(self):
        """No false alarms on the audited program itself: every inline form of
        HEAD passes check 4 except the known template forms of the global
        points (7:DEFAULT while the body loads PPOUNCE/PREPAIR), and the
        numbered code matches check_cleanup.code_lines()."""
        from check_cleanup import code_lines
        problems = []
        for path, data in self.clean.items():
            if not ab.is_krl(path) or ab.area(path) != 'integrator program':
                continue
            text = data.decode('latin-1')
            self.assertEqual([c for _, c in ab.numbered_code(text)],
                             [c for c in code_lines(text) if not c.startswith('&')], path)
            for n, header, body in ab.forms_with_lines(text):
                problems += [(os.path.basename(path), p)
                             for p in ab.form_problems(header, [b for _, b in body])]
        # R10 also has the three picks whose fold text says AtPick1 while the
        # form data and the code move to AtPick3 (documented in the code)
        self.assertTrue(all('form data 7:DEFAULT expects PDAT_ACT=PDEFAULT' in p
                            or p == 'fold text shows point AtPick1, form data 2:AtPick3' for _, p in problems),
                        problems)
        self.assertEqual(sorted(f for f, _ in problems),
                         ['hometopounce.src', 'hometorepair.src', 'pouncetohome.src', 'repairtohome.src',
                          'style1pick1opt1.src', 'style1pick1opt1AutoRR.src', 'style1pick1opt2.src'])

    # -- added in the review: realistic changes, no noise ---------------

    def test_p_realistic_supervised_wait(self):
        """A programmer closes F15 the way CONVENTIONS.md asks: a $TIMER-supervised
        wait with a Set_KrlMsg, commented, new data in the .dat, &REL bumped by the
        controller. It must read as a code change and raise nothing."""
        src = self.edit(APP1, ';NOTE: NO TIMEOUT, NO MESSAGE (F15). IN DRY CYCLE',
                        ';NOTE: AT MOST 10 S, THEN QUIT MESSAGE "NUT NOT READY" (F15). IN DRY CYCLE')
        src = src.replace('WAIT FOR NUT_READY== TRUE\r\n', (
            '$TIMER_STOP[20]=TRUE\r\n$TIMER[20]=0\r\n$TIMER_STOP[20]=FALSE\r\n'
            'WAIT FOR NUT_READY OR ($TIMER[20]>10000)\r\n$TIMER_STOP[20]=TRUE\r\n'
            'IF NOT NUT_READY THEN\r\n'
            '   ;MESSAGE R10 2001 NUT NOT READY AT THE PEDESTAL - THE OPERATOR ACKNOWLEDGES\r\n'
            '   nNutMsgHandle=Set_KrlMsg(#QUIT, NutMsg, NutMsgPar[], AutoCore_MsgOpt_Stop)\r\n'
            '   WAIT FOR NUT_READY\r\nENDIF\r\n'), 1).replace('&REL 339', '&REL 342')
        dat = self.text(APP1_DAT).replace('ENDDAT', (
            'DECL KRLMSG_T NutMsg={MODUL[] "R10",NR 2001,MSG_TXT[] "NUT NOT READY AT THE PEDESTAL"}\r\n'
            'DECL KRLMSGPAR_T NutMsgPar[3]\r\nDECL INT nNutMsgHandle=0\r\nENDDAT'))
        s = self.audit(self.backup({APP1: src, APP1_DAT: dat}))
        c = s['counts']
        self.assertEqual((c['FAIL'], c['WARN'], c['INFO']), (0, 0, 0), s['findings'])
        self.assertFalse([a for a in s['alerts'] if a[0] != 'INFO'], s['alerts'])
        self.assertEqual(sorted(s['changed']), [APP1_DAT, APP1])
        f = s['files'][APP1]
        self.assertEqual((f['code_removed'], f['code_added']), (1, 9))
        self.assertEqual(f['attributes'], ['&REL 339 -> &REL 342'])
        self.assertIn('added 1 KRLMSGPAR_T: NutMsgPar', s['files'][APP1_DAT]['data_changes'])
        self.assertNotIn('identical', self.report)
        self.assertIn('nothing beyond the changes listed below', self.report)

    def test_q_touch_up_and_runtime_values(self):
        """Touch Up changes only the E6POS in the .dat. A backup taken after the
        robot ran also carries new values the program wrote into persistent
        .dat data (message handles, NUT_READY, the editor's LAST_BASIS): they
        are not code changes, not vendor edits (C28), and they must not hide a
        red flag of an item whose modules really did not change."""
        dat = self.edit(APP1_DAT, 'XP19={X -3851.81445,Y -107.010963,', 'XP19={X -3851.81445,Y -94.510963,')
        dat = dat.replace('POINT1[] "P0                      "', 'POINT1[] "P19                     "', 1)
        cfg = self.edit(CONFIG, 'DECL BOOL NUT_READY=TRUE', 'DECL BOOL NUT_READY=FALSE')
        cfg = cfg.replace('DECL INT NUT_PRELOAD_STEP=0', 'DECL INT NUT_PRELOAD_STEP=20')
        acd = self.edit(ACDATA, 'nCycleStart_Handle=11564', 'nCycleStart_Handle=11877')
        # the measurement writes array elements the .dat did not list before (F52)
        cyc = self.edit(CYCLE_DAT, 'CL_T_ROW[2]=0', 'CL_T_ROW[2]=1')
        cyc = cyc.replace('DECL INT CL_T_LOG[3,10,13]',
                          'DECL INT CL_T_LOG[3,10,13]\r\nCL_T_LOG[2,1,1]=1530\r\nCL_T_LOG[2,1,2]=2210', 1)
        xlsx = os.path.join(self.tmp, 'items.xlsx')
        write_minimal_xlsx(xlsx, [['ID', 'Estado', 'Módulos', 'Qué cambió el programador'],
                                  ['F04', 'Corregido - por auditar', 'PRELOAD, $config.dat', 'dry cycle']])
        s = self.audit(self.backup({APP1_DAT: dat, CONFIG: cfg, ACDATA: acd, CYCLE_DAT: cyc}), '--items', xlsx)
        f = s['files'][APP1_DAT]
        self.assertEqual(f['data_changes'], ['XP19 (E6POS) re-taught: moved 12.5 mm'])
        self.assertEqual((f['code_removed'], f['code_added']), (1, 1))
        self.assertTrue(any(r.startswith('LAST_BASIS:') for r in f['runtime_values']))
        self.assertEqual(sorted(s['runtime_value_files']), sorted([ACDATA, CONFIG, CYCLE_DAT]))
        self.assertEqual(s['files'][CYCLE_DAT]['runtime_values'],
                         ['CL_T_LOG[2,1,1]: - -> 1530', 'CL_T_LOG[2,1,2]: - -> 2210', 'CL_T_ROW[2]: 0 -> 1'])
        self.assertEqual(s['files'][CONFIG]['runtime_values'],
                         ['NUT_PRELOAD_STEP: 0 -> 20', 'NUT_READY: TRUE -> FALSE'])
        self.assertEqual(s['counts']['code_changed_files'], 1)
        self.assertFalse([a for a in s['alerts'] if 'C28' in a[1]], s['alerts'])
        (f04,) = s['items']['claimed']
        self.assertEqual(f04['red_flag'], 'none of its modules changed in this backup')
        self.assertIn(f'{CONFIG}: runtime values only', self.report)
        self.assertIn('### Runtime values only', self.report)

    def test_r_case_and_layout(self):
        """Names that differ only in case, a whole folder spelled differently,
        AM.INI in capitals, the archive zipped again inside a folder, and two
        entries that are one file on the controller."""
        util = 'KRC/R1/Program/Utilities/'
        renamed = {p: p.replace(util, 'KRC/R1/program/UTILITIES/') for p in self.clean if p.startswith(util)}
        files = {renamed.get(p, p): d for p, d in self.clean.items()}
        files['AM.INI'] = files.pop('am.ini')
        files['KRC/R1/program/UTILITIES/newhelper.src'] = (
            b'&ACCESS RVO1\r\n&COMMENT 03-10-R1 HELPER\r\nDEF newhelper( )\r\n;********************************\r\n'
            b'; Gestamp Standards\r\n; Robot 03-10-R1 (BMW-03-10-R1)\r\n;********************************\r\n'
            b'END\r\n')
        files['KRC/R1/cell.SRC'] = self.clean[CELL]
        zip_path = os.path.join(self.tmp, 'layout.zip')
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
            for p in sorted(files):
                z.writestr('658424/' + p, files[p])
            z.writestr('658424/Log Files/KrcLog.log', b'x')
        s = self.audit(zip_path)
        self.assertEqual(s['backup']['am_ini']['serial'], '658424')
        self.assertTrue(s['backup']['serial_ok'])
        self.assertEqual(s['backup']['log_entries_skipped'], 1)
        self.assertEqual((s['counts']['missing'], s['counts']['unexpected'], s['counts']['changed']), (0, 0, 0))
        self.assertEqual(s['added'], [util + 'newhelper.src'])       # in the folder of the base
        infos = [a[1] for a in s['alerts'] if a[0] == 'INFO']
        self.assertTrue(any(m.startswith('KRC/R1/program/UTILITIES/: spelled KRC/R1/Program/Utilities/')
                            for m in infos), infos)
        self.assertFalse([m for m in infos if m.startswith('KRC/R1/program/UTILITIES/Home')])
        warns = [a[1] for a in s['alerts'] if a[0] == 'WARN']
        self.assertTrue(any('inside the folder 658424/' in m for m in warns), warns)
        self.assertTrue(any('KRC/R1/cell.SRC' in m and 'same file on the controller' in m for m in warns))
        self.assertEqual(s['counts']['FAIL'], 0, s['findings'])

    def test_s_missing_folder(self):
        """A backup without the StyleDrops folder is not 'identical to the base':
        the drop modules are still called, the program cannot run."""
        gone = {p: None for p in self.clean if p.startswith('KRC/R1/Program/StyleDrops/')}
        s = self.audit(self.backup(gone))
        self.assertEqual(len(s['missing']), len(gone))
        fails = [a[1] for a in s['alerts'] if a[0] == 'FAIL']
        self.assertTrue(any(m.startswith(DROP + ' is missing from the backup but Style1Drop1Opt1 is still '
                                                'called') for m in fails), fails)
        self.assertNotIn('identical to the base', self.report)
        attention = self.report[self.report.index('**Needs attention:**'):self.report.index('## The backup')]
        self.assertIn('missing from the backup', attention)

    def test_t_no_false_alarms(self):
        """Things a normal backup holds that must not raise a FAIL or WARN:
        English words after an address, a ';WAIT FOR NUT_READY' heading, a CIRC
        form, a new AutomationCore zone request (two generated calls), a vendor
        file with German comments, a point without T; and a
        structure defect that replaces a fixed one must still be found."""
        src = self.edit(APP1, 'WAIT FOR NUT_READY== TRUE\r\n',
                        ';NOTE: $OUT[476] DONE BY PRELOAD, $IN[467] DIRECTLY READ, $OUT[18] DOWN\r\n'
                        ';WAIT FOR NUT_READY\r\nWAIT FOR NUT_READY== TRUE\r\n')
        circ = ('\r\n;MOVE AROUND THE PEDESTAL - CIRC P40 P41\r\n;FOLD CIRC P40 P41 CONT Vel=2 m/s CPDAT40 '
                'Tool[1]:EOAT 1 Base[3]:NUT WELDER;%{PE}%R 8.3.43,%MKUKATPBASIS,%CMOVE,%VCIRC,%P 1:CIRC, '
                '2:P40, 3:P41, 4:C_DIS C_DIS, 6:2, 8:CPDAT40\r\n$BWDSTART=FALSE\r\nLDAT_ACT=LCPDAT40\r\n'
                'FDAT_ACT=FP41\r\nBAS(#CP_PARAMS,2)\r\nCIRC XP40, XP41 C_DIS C_DIS\r\n;ENDFOLD\r\n')
        zone = (';REQUEST ZONE 3 - AUTOMATIONCORE ZONE REQUEST (C13)\r\n;FOLD Zone[3] Request\r\n;FOLD ;%{h}\r\n'
                ';Params IlfProvider=ac_zoneilf; AC_CmdZones=Zone; AC_CmdParam=3; AC_ZoneRepo=False; '
                'AC_Blending=False\r\n;ENDFOLD\r\nAC_ZoneLogic (3,False)\r\nAC_ZoneCheck (3)\r\n;ENDFOLD\r\n')
        src = src.replace(';LEAVE THE PEDESTAL - P20', circ.lstrip() + zone + ';LEAVE THE PEDESTAL - P20', 1)
        pt = ('DECL E6POS XP{0}={{X 1.0,Y 2.0,Z 3.0,A 0.0,B 0.0,C 0.0,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,'
              'E5 0.0,E6 0.0}}\r\nDECL FDAT FP{0}={{TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",'
              'TQ_STATE FALSE}}\r\n')
        dat = self.edit(APP1_DAT, 'S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}\r\nDECL FDAT FP19=',
                        'S 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}\r\nDECL FDAT FP19=')
        dat = dat.replace('ENDDAT', pt.format(40) + pt.format(41) + 'DECL LDAT LCPDAT40={VEL 2.00000,ACC 100.000,'
                          'APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,'
                          'CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}\r\nENDDAT')
        vendor = 'KRC/R1/TP/NewPackage/neu.src'
        vendor_src = ('&ACCESS RVO\r\nDEF neu( )\r\n;Greifer \xf6ffnen\r\n;$OUT[5]=TRUE\r\n;ESPERA\r\n'
                      '$OUT[7]=TRUE\r\nHALT\r\nEND\r\n')
        s = self.audit(self.backup({APP1: src, APP1_DAT: dat, vendor: vendor_src}))
        bad = [f for f in s['findings'] if f['level'] in ('FAIL', 'WARN')]
        self.assertEqual(bad, [])
        self.assertTrue(any('ARM CONFIGURATION' in d for d in s['files'][APP1_DAT]['data_changes']))
        self.assertTrue(any(vendor in a[1] and 'C28' in a[1] for a in s['alerts']))
        # structure: fix nothing, add an IF never closed -> FAIL even though the count of
        # defects of a vendor file with one known defect is compared
        td = 'KRC/R1/TP/GLUETECH/glue.src'
        self.assertEqual(len(ab.structure_issues(td, self.text(td))), 1)
        broken = self.text(td).replace('DEFFCT', 'DEFFCT', 1) + '\r\nIF X THEN\r\n'
        audit = ab.Audit()
        ab.check_structure(audit, ab.Change(td, self.clean[td], broken.encode('latin-1')), {})
        self.assertTrue(any(f['level'] == 'FAIL' and 'IF is never closed' in f['message']
                            for f in audit.findings), audit.findings)

    def test_u_dat_removal_global_and_local(self):
        """A local point removed from a .dat is looked for in its own .src only,
        a GLOBAL one everywhere; $config.dat names are global."""
        dat_path = APP1_DAT
        old = self.text(dat_path).replace('ENDDAT', 'DECL GLOBAL INT nNutTimeout=10000\r\nENDDAT')
        new = self.text(dat_path)
        start = new.index('DECL E6POS XP20=')
        new = new[:start] + new[new.index('\n', start) + 1:]          # XP20: local, also in other modules
        texts = {p: d.decode('latin-1') for p, d in self.clean.items() if ab.is_krl(p)}
        texts[dat_path] = new
        texts[CELL] = texts[CELL].replace('HOME()\r\n', 'HOME()\r\n  nNutTimeout=5000\r\n', 1)
        ctx = {'texts': texts}
        audit = ab.Audit()
        ab.check_data(audit, ab.Change(dat_path, old.encode('latin-1'), new.encode('latin-1')), ctx)
        msgs = sorted(f['message'] for f in audit.findings)
        self.assertEqual(len(msgs), 2, msgs)
        self.assertTrue(msgs[0].startswith('XP20 was removed from this file but is still used in ' + APP1))
        self.assertTrue(msgs[1].startswith('nNutTimeout was removed from this file but is still used in ' + CELL))
        cfg_old = self.text(CONFIG)
        cfg_new = cfg_old.replace('DECL BOOL NUT_READY=TRUE\r\n', '', 1)
        self.assertNotEqual(cfg_old, cfg_new)
        audit = ab.Audit()
        ab.check_data(audit, ab.Change(CONFIG, cfg_old.encode('latin-1'), cfg_new.encode('latin-1')), ctx)
        self.assertTrue(any(f['message'].startswith('NUT_READY was removed from this file but is still used')
                            for f in audit.findings), audit.findings)

    def test_w_tool_base_against_fdat(self):
        """TOOL_NO edited in the .dat only: the LIN P19 form still shows
        Tool[1] - the robot moves with another tool than the program says.
        The same fix made through the smartPAD (fold text and FDAT) is clean; a
        GLOBAL FDAT edited by hand is found in every module that uses it."""
        dat = self.edit(APP1_DAT, 'DECL FDAT FP19={TOOL_NO 1,', 'DECL FDAT FP19={TOOL_NO 2,')
        s = self.audit(self.backup({APP1_DAT: dat}))
        fails = self.findings(s, 4, 'FAIL')
        self.assertEqual([(f['file'], f['message'].split(': ', 1)[1]) for f in fails],
                         [(APP1, 'fold text shows Tool[1], its FDAT has TOOL_NO 2')])
        src = self.edit(APP1, 'CPDAT18 Tool[1]:TOOL 1 Base[3]:NUT WELDER;%{PE}', 'CPDAT18 Tool[2] Base[3]:NUT WELDER;%{PE}')
        s = self.audit(self.backup({APP1_DAT: dat, APP1: src}))
        self.assertEqual(self.findings(s, 4), [])
        agp = 'KRC/R1/TP/AutomationCore/automationglobalpos.dat'
        # on R10 the pounce forms show no Tool/Base (old form); the reference switch does
        g = self.edit(agp, 'FRefSwitch={TOOL_NO 1,BASE_NO 0', 'FRefSwitch={TOOL_NO 1,BASE_NO 2')
        s = self.audit(self.backup({agp: g}))
        self.assertTrue(any(f['file'].endswith('masref_user.src') and 'its FDAT has BASE_NO 2' in f['message']
                            for f in self.findings(s, 4, 'FAIL')), s['findings'])

    def test_v_import_skips_pre_cleanup_files(self):
        """--import writes changed and added entries byte for byte into the
        working tree, never a deleted module, a Log Files entry, an entry
        outside the layout, nor a pre-cleanup file (it would undo the cleanup
        for whoever commits)."""
        weld = self.edit(WELD, 'WAIT SEC 0.2', 'WAIT SEC 0.3').encode('latin-1')
        zip_path = self.backup({WELD: weld, PRELOAD: self.first[PRELOAD], MAYBEHOME: self.first[MAYBEHOME],
                                'KRC/R1/program/Centerline/new one.src': b'DEF x( )\r\nEND\r\n',
                                'tools/x.py': b'print(1)\n'})
        root = os.path.join(self.tmp, 'tree')
        os.makedirs(root)
        with contextlib.redirect_stdout(io.StringIO()) as buf:
            s = ab.main([zip_path, '--base', REF, '--out', os.path.join(self.tmp, 'r'), '--import'],
                        import_root=root)
        self.assertEqual(s['pre_cleanup'], [PRELOAD])
        self.assertEqual([d['path'] for d in s['deleted_still_present']], [MAYBEHOME])
        written = sorted(os.path.relpath(os.path.join(d, n), root).replace(os.sep, '/')
                         for d, _, ns in os.walk(root) for n in ns)
        self.assertEqual(written, ['KRC/R1/Program/Centerline/centerline_weld.src',
                                   'KRC/R1/Program/Centerline/new one.src'])
        with open(os.path.join(root, *WELD.split('/')), 'rb') as f:
            self.assertEqual(f.read(), weld)
        self.assertIn('not imported (PRE-CLEANUP files', buf.getvalue())


# ------------------------------------------------------------ workbooks

def col(i):
    s = ''
    i += 1
    while i:
        i, r = divmod(i - 1, 26)
        s = chr(65 + r) + s
    return s


def write_minimal_xlsx(path, rows, sheet='Puntos abiertos'):
    """A workbook written by hand: a first 'Instrucciones' sheet, then `sheet`
    with `rows`; text alternates between shared and inline strings, numbers
    and booleans are typed cells."""
    shared, cells_xml = [], []
    for r, row in enumerate(rows, 1):
        cells = []
        for c, v in enumerate(row):
            ref = f'{col(c)}{r}'
            if isinstance(v, bool):
                cells.append(f'<c r="{ref}" t="b"><v>{int(v)}</v></c>')
            elif isinstance(v, (int, float)):
                cells.append(f'<c r="{ref}"><v>{v}</v></c>')
            elif (r + c) % 2:
                cells.append(f'<c r="{ref}" t="inlineStr"><is><t>{escape(v)}</t></is></c>')
            else:
                shared.append(v)
                cells.append(f'<c r="{ref}" t="s"><v>{len(shared) - 1}</v></c>')
        cells_xml.append(f'<row r="{r}">{"".join(cells)}</row>')
    ns = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'
    rel = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
    parts = {
        '[Content_Types].xml':
            '<?xml version="1.0" encoding="UTF-8"?><Types xmlns="http://schemas.openxmlformats.org/'
            'package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.'
            'openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="'
            'application/xml"/><Override PartName="/xl/workbook.xml" ContentType="application/vnd.'
            'openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/><Override PartName="/xl/'
            'worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.'
            'spreadsheetml.worksheet+xml"/><Override PartName="/xl/worksheets/sheet2.xml" ContentType'
            '="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/><Override '
            'PartName="/xl/sharedStrings.xml" ContentType="application/vnd.openxmlformats-officedocument'
            '.spreadsheetml.sharedStrings+xml"/></Types>',
        '_rels/.rels':
            '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.'
            'org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats'
            '.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>'
            '</Relationships>',
        'xl/workbook.xml':
            f'<?xml version="1.0" encoding="UTF-8"?><workbook xmlns="{ns}" xmlns:r="{rel}"><sheets>'
            f'<sheet name="Instrucciones" sheetId="1" r:id="rId1"/><sheet name="{escape(sheet)}" '
            f'sheetId="2" r:id="rId2"/></sheets></workbook>',
        'xl/_rels/workbook.xml.rels':
            '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.'
            'org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxml'
            'formats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>'
            '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/'
            'relationships/worksheet" Target="worksheets/sheet2.xml"/><Relationship Id="rId3" Type="'
            'http://schemas.openxmlformats.org/officeDocument/2006/relationships/sharedStrings" '
            'Target="sharedStrings.xml"/></Relationships>',
        'xl/worksheets/sheet1.xml':
            f'<?xml version="1.0" encoding="UTF-8"?><worksheet xmlns="{ns}"><sheetData><row r="1">'
            f'<c r="A1" t="inlineStr"><is><t>ID</t></is></c><c r="B1" t="inlineStr"><is><t>Estado</t>'
            f'</is></c></row></sheetData></worksheet>',
        'xl/worksheets/sheet2.xml':
            f'<?xml version="1.0" encoding="UTF-8"?><worksheet xmlns="{ns}"><sheetData>'
            f'{"".join(cells_xml)}</sheetData></worksheet>',
        'xl/sharedStrings.xml':
            f'<?xml version="1.0" encoding="UTF-8"?><sst xmlns="{ns}" count="{len(shared)}" '
            f'uniqueCount="{len(shared)}">' + ''.join(f'<si><t>{escape(s)}</t></si>' for s in shared)
            + '</sst>',
    }
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as z:
        for name, xml in parts.items():
            z.writestr(name, xml.encode('utf-8'))


def write_xlsx(path, rows, sheet='Puntos abiertos'):
    """The workbook of test (h): openpyxl when installed, else written by hand."""
    try:
        import openpyxl
    except ImportError:
        return write_minimal_xlsx(path, rows, sheet)
    wb = openpyxl.Workbook()
    wb.active.title = 'Instrucciones'
    wb.active.append(['ID', 'Estado'])
    ws = wb.create_sheet(sheet)
    for row in rows:
        ws.append(row)
    wb.save(path)


if __name__ == '__main__':
    os.chdir(REPO)
    unittest.main(verbosity=2)
