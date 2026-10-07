#!/usr/bin/env python3
"""Audit a robot backup sent by the integrator against the last audited state.

    python3 tools/audit_backup.py NEW_BACKUP.zip [--base REF] [--items ITEMS.xlsx]
                                  [--out DIR] [--import]

Working mode: the integrator's robot programmer changes the program to close
the items of docs/FINDINGS.md, marks them in the open-items workbook (an
Excel copy) and sends a full KUKA archive (zip) at the end of each day. The
owner puts it next to this repository and the auditor runs this tool. It
answers three questions: what changed in the program, is each item the
programmer marked as fixed really touched by the backup, and did anything
else break.

What it does

  * Reads every entry of the zip except 'Log Files/' (KUKA archive layout:
    KRC/..., C/..., Registry/..., am.ini) and compares it with the files of
    --base (a git ref, default HEAD: the last audited state; the first
    commit of the repository is the archive as received). Each entry is
    unchanged, changed, added (not in the base) or missing (in the base, not
    in the backup). Names are compared without case, as on the controller;
    a new file is placed in the folder of the base whatever the case of its
    folder in the zip. A zip whose entries all sit in one folder holding
    am.ini (the archive extracted and zipped again) is read from that
    folder, with a WARN. Reports the archive name, date, robot name and
    serial number from am.ini; a serial other than 658424 is another robot.
    A missing KRL file whose routines or data the backup still uses is a
    FAIL (the program does not compile or a call fails).
  * A module the cleanup deleted (tools/cleanup_allowlist.json,
    'deleted_files') that is in the backup is still on the controller: a
    restore never deletes files, so it must be deleted there.
  * A changed KRL file whose bytes equal its version in the first commit is
    the pre-cleanup file: the cleaned program was not loaded or was
    overwritten. A changed file whose comments are closer to that version
    than to the base was edited on top of the pre-cleanup file.
  * For each changed or added KRL file (.src/.dat/.sub): the change of the
    executable code (comments, blank lines and indentation removed, the
    '&' attribute lines apart) with line numbers, the number of comment-only
    line changes, the taught points and data that changed (.dat), and the
    full diff in DIR/diffs/<path>.diff.
  * Runtime values: a .dat keeps the last value the program wrote to each
    of its variables, and the inline-form editor keeps its suggestions
    (LAST_BASIS, LAST_TP_PARAMS). A value-only change of a variable the
    program assigns somewhere, or of the editor's suggestion data, is listed
    apart and is not a code change, not a vendor edit (C28) and does not
    count as a change of the modules of an item claimed fixed.
  * Mechanical checks on the new content, each a FAIL, WARN or INFO line
    with file:line. Only what is new relative to the base is reported; what
    the base already had is known (docs/FINDINGS.md). Checks 2 (non-ASCII),
    6, 7, 8, 9 and 10 are style rules of the integrator's program and are
    not applied to KUKA or tech-package files (an edit there is C28).
      1  ;FOLD balance or DEF/IF/LOOP... nesting worse than in the base
      2  line-ending convention changed, non-ASCII bytes introduced
      3  a comment names '$IN/$OUT[n] name' with a name not declared at that
         index (declarations read from the backup)
      4  inline form whose fold text, form data (%P) and generated code
         disagree: PTP/LIN point, FDAT/PDAT/LDAT, velocity, CONT; OUT index
         and state; WAIT time; WAIT FOR inputs. The Tool[n] / Base[n] /
         extTCP of a PTP/LIN fold text against its FDAT in the .dat (also
         when only the .dat changed: a hand-edited FDAT moves the robot with
         another tool, F22). AutomationCore forms whose AC_CmdParam differs
         from the call are INFO (index convention, F21)
      5  hand-typed executable line inside an inline form: lost on Touch Up
         (F32)
      6  new commented-out code
      7  new comment with Spanish words
      8  new or changed I/O access with no comment naming the signal in the
         four lines above (C24)
      9  new module without the '; Gestamp Standards' header or &COMMENT
     10  new HALT, WAIT FOR FALSE, WAIT FOR with no timeout nearby (INFO;
         C21, F07, F15)
     11  a new motion form whose point or data is not declared, a
         declaration removed from a .dat that is still used: the module
         would not compile
  * --items ITEMS.xlsx: the programmer's open-items workbook (sheet 'Puntos
    abiertos'; columns found by their header: 'ID', 'Estado', 'Qué cambió
    el programador', 'Módulos'). Every item marked 'Corregido - por
    auditar' is listed with the programmer's note and which of its modules
    changed in this backup. A fix claimed with no change in its modules is
    a red flag. openpyxl is used when installed; otherwise the workbook is
    read with zipfile and xml.

Output: DIR (default audits/<am.ini date>/) with AUDIT.md (the report for
the auditor), summary.json (counts and lists for scripts) and diffs/.

--import, after the report, copies every changed and added entry (never
'Log Files/', never a deleted module still present, never an entry outside
the archive layout, never a pre-cleanup file - it is the first commit byte
for byte and would undo the cleanup for whoever commits) into the working
tree byte-for-byte, so the auditor can review it with git diff and commit
it as the new audited state. Nothing is deleted: files missing from the
backup are listed, not removed.

Exit status is 0 whatever the backup contains - the report is for a human
auditor - and 2 when the zip or the base ref cannot be read.
"""
import argparse
import configparser
import datetime
import difflib
import fnmatch
import hashlib
import json
import math
import os
import posixpath
import re
import subprocess
import sys
import unicodedata
import zipfile
import xml.etree.ElementTree as ET
from collections import Counter

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, 'tools'))

from check_cleanup import (KRL_EXT, SIG_REF, SIGNALISH, declared_names,  # noqa: E402
                           declared_signals, eol_style, fold_issues, form_bodies,
                           header_key, live, load_allowlist, nesting_issues, normalise,
                           split_code, word_in)

ARCHIVE_DIRS = ('krc/', 'c/', 'registry/')
ARCHIVE_FILES = ('am.ini',)
LOG_DIR = 'log files/'
SERIAL = '658424'
INLINE_DIFF_LINES = 60      # code-diff lines shown per file in AUDIT.md
MAX_PER_FILE = 25           # findings of one check shown per file before a summary line

LEVELS = ('FAIL', 'WARN', 'INFO')
CHECKS = {0: 'audit error', 1: 'fold/block structure', 2: 'format', 3: 'signal named in comment',
          4: 'inline form consistency', 5: 'hand-typed line in inline form',
          6: 'commented-out code', 7: 'Spanish comment', 8: 'I/O without signal comment',
          9: 'module header', 10: 'fault handling', 11: 'data declarations'}

SPANISH = set('''
QUITAR PONER CONFIRMAR CONFIRMA PIEZA PIEZAS TUERCA TUERCAS SOLDADURA SOLDAR SOLDADO
PRESION ABRIR ABRE CERRAR CIERRA ESPERA ESPERAR ESPERANDO INICIAR INICIO ALIMENTAR
ALIMENTADOR ALIMENTACION CERRADA CERRADO ABIERTA ABIERTO HABILITAR DESHABILITAR
HABILITADO DESHABILITADO PINZA PERNO SALIDA SALIDAS ENTRADA ENTRADAS SENAL SENALES
AVANZAR AVANCE REGRESAR REGRESO RETORNO BAJAR SUBIR ARRIBA ABAJO ADELANTE ATRAS
POSICION CAMBIO CAMBIAR AGUA PUERTA RECHAZO RECHAZAR RECHAZADA BUENA BUENO MALA MALO
LISTO LISTA TERMINADO TERMINAR TERMINA ACTIVAR DESACTIVAR ACTIVADO DESACTIVADO APAGAR
ENCENDER REVISAR VERIFICAR FALLA ALARMA CICLO TIEMPO PISTOLA ELECTRODO CAMARA
HERRAMIENTA PUNTO PUNTOS RUTINA PROGRAMA LLAMAR PRUEBA NUEVO NUEVA VIEJO VIEJA
TOMAR COLOCAR SOLTAR AGARRAR DEJAR MOVER SALIR ENTRAR VALVULA CILINDRO SUJETADOR
MORDAZA PRESENCIA CUANDO DESPUES ANTES HASTA PARA AQUI ESTA ESTE CORREGIR
'''.split())

KRL_OPERATORS = {'AND', 'OR', 'NOT', 'EXOR', 'B_AND', 'B_OR', 'B_NOT', 'B_EXOR', 'TRUE', 'FALSE'}
TIMEOUT_HINT = re.compile(r'\$TIMER|TIMEOUT|TIME_OUT|\bTMO', re.I)
IO_LITERAL = re.compile(r'\$(IN|OUT)(?:_C)?\[(\d+)\]', re.I)
CITED_IO = re.compile(r'\$(IN|OUT)\[(\d+)', re.I)


# --------------------------------------------------------------------- git

def git(*args, data=None):
    return subprocess.run(('git',) + args, input=data, check=True,
                          capture_output=True, cwd=REPO).stdout


def blob_id(data):
    """The git blob id of `data`: equal ids, equal bytes."""
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


def tree_blobs(ref):
    """{path: blob id} of every file in commit `ref`."""
    blobs = {}
    for rec in git('ls-tree', '-r', '-z', ref).split(b'\0'):
        if rec:
            meta, path = rec.split(b'\t', 1)
            blobs[path.decode('utf-8', 'surrogateescape')] = meta.split()[2].decode()
    return blobs


def read_blobs(ids):
    """{blob id: bytes}, read with a single 'git cat-file --batch'."""
    ids = sorted(set(ids))
    if not ids:
        return {}
    out = git('cat-file', '--batch', data=''.join(i + '\n' for i in ids).encode())
    blobs, pos = {}, 0
    for i in ids:
        nl = out.index(b'\n', pos)
        head = out[pos:nl].split()
        if len(head) < 3:
            raise RuntimeError(f'git object {i} not found')
        size = int(head[2])
        blobs[i] = out[nl + 1:nl + 1 + size]
        pos = nl + 1 + size + 1
    return blobs


def first_commit():
    return git('rev-list', '--max-parents=0', 'HEAD').decode().split()[0]


# ----------------------------------------------------------------- archive

def is_archive_path(path):
    low = path.lower()
    return low in ARCHIVE_FILES or low.startswith(ARCHIVE_DIRS)


def is_krl(path):
    return path.lower().endswith(KRL_EXT)


def archive_prefix(names):
    """'658424/' when the archive was extracted and zipped again inside a
    folder (am.ini not at the root, but in exactly one top folder holding
    every entry); '' otherwise."""
    if any(n.lower() == 'am.ini' for n in names):
        return ''
    tops = {n.split('/', 1)[0] + '/' for n in names if n.count('/') == 1 and n.lower().endswith('/am.ini')}
    if len(tops) != 1:
        return ''
    top = tops.pop()
    return top if all(n.startswith(top) for n in names) else ''


def read_backup(zip_path):
    """The entries of a KUKA archive zip: ({name: bytes}, log entries skipped,
    notes). Directory entries and 'Log Files/' are skipped, '\\' becomes '/'.
    A zip whose entries all sit in one top folder holding am.ini (the archive
    extracted and zipped again) is read as if that folder were the root."""
    entries, notes, logs = {}, [], 0
    with zipfile.ZipFile(zip_path) as z:
        infos = [(i, i.filename.replace('\\', '/').lstrip('/')) for i in z.infolist()]
        prefix = archive_prefix([n for i, n in infos if not i.is_dir() and n and not n.endswith('/')])
        if prefix:
            notes.append(('WARN', f'every entry of the zip is inside the folder {prefix}: the archive was '
                                  f'extracted and zipped again, read as if {prefix} were the root - ask '
                                  f'for the zip exactly as the controller wrote it'))
        for info, name in infos:
            if info.is_dir() or not name or name.endswith('/'):
                continue
            name = name[len(prefix):]
            if name.lower().startswith(LOG_DIR):
                logs += 1
                continue
            try:
                data = z.read(info)
            except (zipfile.BadZipFile, OSError, EOFError, RuntimeError) as exc:
                notes.append(('WARN', f'{name}: entry cannot be read ({exc}) - left out of the audit'))
                continue
            if name in entries:
                notes.append(('WARN', f'{name}: entry appears twice in the zip; the last copy is audited'))
            entries[name] = data
    return entries, logs, notes


def read_am_ini(data):
    """Archive name, date, configuration, robot name, serial and KSS version."""
    cp = configparser.RawConfigParser(strict=False)
    try:
        cp.read_string(data.decode('latin-1'))
    except configparser.Error:
        return {}

    def get(section, key):
        return cp.get(section, key, fallback='').strip()
    return {'name': get('Archive', 'Name'), 'date': get('Archive', 'Date'),
            'config': get('Archive', 'Config'), 'rob_name': get('Roboter', 'RobName'),
            'serial': get('Roboter', 'IRSerialNr'), 'version': get('Version', 'Version')}


def area(path):
    """Who owns a file: decides how loud a change to it is."""
    low = path.lower()
    if low == 'am.ini':
        return 'archive metadata'
    if low.startswith(('c/', 'registry/')):
        return 'controller configuration'
    if low.startswith('krc/r1/program/') or (low.startswith('krc/r1/') and low.count('/') == 2) or low in (
            'krc/r1/system/$config.dat', 'krc/r1/system/sps.sub'):
        return 'integrator program'
    if '/mada/' in low:
        return 'machine data'
    return 'KUKA system / vendor package'


def canonical_dirs(name, base_dirs):
    """`name` with each of its folders spelled as in the base, matched without
    case: 'KRC/R1/program/x.src' -> 'KRC/R1/Program/x.src'. A new file must
    not open a second folder that differs only in case (one folder on the
    controller, two in git)."""
    parts = name.split('/')
    for k in range(len(parts) - 1):
        known = base_dirs.get('/'.join(parts[:k + 1]).lower())
        if known:
            parts[:k + 1] = known.split('/')
    return '/'.join(parts)


def classify(entries, base, deleted):
    """Sort the backup entries against the base tree. Paths are matched
    case-insensitively (the controller file system is), and reported under
    the spelling of the base."""
    base_lower = {p.lower(): p for p in base}
    deleted_lower = {p.lower(): p for p in deleted}
    base_dirs = {}
    for p in list(base) + list(deleted):
        parts = p.split('/')
        for k in range(1, len(parts)):
            base_dirs.setdefault('/'.join(parts[:k]).lower(), '/'.join(parts[:k]))
    files, source = {}, {}
    res = {k: [] for k in ('unchanged', 'changed', 'added', 'missing',
                           'deleted_present', 'unexpected', 'case', 'duplicates')}
    for name in sorted(entries):
        if not is_archive_path(name) or '..' in name.split('/'):
            res['unexpected'].append(name)
            continue
        path = name if name in base else base_lower.get(
            name.lower(), deleted_lower.get(name.lower(), canonical_dirs(name, base_dirs)))
        if path in files:
            # Two entries that differ only in case are one file on the controller.
            res['duplicates'].append((source[path], name))
            for k in ('unchanged', 'changed', 'added', 'deleted_present'):
                if path in res[k]:
                    res[k].remove(path)
        if path != name:
            res['case'].append((name, path))
        files[path], source[path] = entries[name], name
        if path.lower() in deleted_lower:
            res['deleted_present'].append(path)
        elif path not in base:
            res['added'].append(path)
        elif blob_id(entries[name]) == base[path]:
            res['unchanged'].append(path)
        else:
            res['changed'].append(path)
    res['missing'] = sorted(p for p in base if is_archive_path(p) and p not in files)
    return files, res


# ------------------------------------------------------------ KRL helpers

def lines_of(text):
    return [l.rstrip('\r') for l in text.split('\n')]


def numbered_code(text):
    """[(line number, normalised code)] of the executable lines: what
    check_cleanup.code_lines() keeps, minus the '&' attribute lines (&ACCESS,
    &REL, &PARAM), which the controller rewrites when it saves a file."""
    out = []
    for n, raw in enumerate(lines_of(text), 1):
        if raw.startswith('&'):
            continue
        code = normalise(split_code(raw))
        if code:
            out.append((n, code))
    return out


def attributes(text):
    return [l for l in lines_of(text) if l.startswith('&')]


def attribute_changes(old, new):
    """(['&REL 39 -> &REL 41', '+&COMMENT ...'], number of lines changed)."""
    out, count = [], 0
    for tag, a1, a2, b1, b2 in difflib.SequenceMatcher(None, old, new).get_opcodes():
        if tag == 'equal':
            continue
        count += (a2 - a1) + (b2 - b1)
        if tag == 'replace' and a2 - a1 == b2 - b1:
            out += [f'{a} -> {b}' for a, b in zip(old[a1:a2], new[b1:b2])]
        else:
            out += [f'-{a}' for a in old[a1:a2]] + [f'+{b}' for b in new[b1:b2]]
    return out, count


def comment_text(raw):
    """The comment of a line without its ';', or '' (inline-form data and
    fold markers are the editor's, not comments)."""
    code = split_code(raw)
    comment = raw[len(code):].strip()
    if not comment.startswith(';') or ';%{' in comment:
        return ''
    text = comment[1:].strip()
    if text.upper().startswith(('FOLD', 'ENDFOLD', 'PARAMS ', 'START AUTOGENERATED',
                                'END AUTOGENERATED', '%{')):
        return ''
    return text


def fold_case(s):
    """Upper case, accents removed: 'presión' -> 'PRESION'."""
    return ''.join(c for c in unicodedata.normalize('NFKD', s)
                   if not unicodedata.combining(c)).upper()


def looks_like_code(expr):
    """True if `expr` reads as a KRL expression rather than English: no two
    operands (words, numbers, addresses) side by side unless one is an
    operator ('GUN OPEN' and 'SIGNAL $IN[15]' are English, '$IN[5] AND NOT X'
    is code)."""
    expr = re.sub(r'\{[^}]*\}|"[^"]*"', 'V', expr.strip())
    if not expr or not re.fullmatch(r'[\w$.\[\]()+\-*/#,=<>:\s\'"]+', expr):
        return False
    operand = re.compile(r'[\w$][\w$\[\].]*[,.:;]?')
    chunks = expr.split()
    for a, b in zip(chunks, chunks[1:]):
        if operand.fullmatch(a) and operand.fullmatch(b) and not a.endswith(',') and \
                a.upper().strip(',.:;') not in KRL_OPERATORS and b.upper().strip(',.:;') not in KRL_OPERATORS:
            return False
    return True


def commented_code_kind(text):
    """What KRL statement a comment parses as ('assignment', 'WAIT', ...),
    or None for prose."""
    s = split_code(text).strip()
    if not s:
        return None
    u = s.upper()
    m = re.match(r'^\$?[A-Za-z_][\w$]*(\[[^\]]*\])?(\.[A-Za-z_]\w*)*\s*=(?!=)\s*(.+)$', s)
    if m and looks_like_code(m.group(3)):
        return 'assignment'
    if re.match(r'^WAIT\s+SEC\s+[\w.$\[\]]+$', u):
        return 'WAIT SEC'
    m = re.match(r'^WAIT\s+FOR\s+(.+)$', u)
    # ';WAIT FOR NUT_READY' heads a block in plain English as often as it is
    # a statement taken out: only an expression with an operator, an address
    # or a constant reads as code.
    if m and looks_like_code(m.group(1)) and re.search(
            r'[$\[\]()=<>]|\b(AND|OR|NOT|EXOR|TRUE|FALSE)\b', m.group(1)):
        return 'WAIT FOR'
    m = re.match(r'^(ELSE\s*)?IF\s+(.+)\s+THEN$', u)
    if m and looks_like_code(m.group(2)):
        return 'IF'
    if re.match(r'^(ENDIF|ELSE|LOOP|ENDLOOP|ENDWHILE|ENDFOR|ENDSWITCH|HALT|CONTINUE|RETURN|EXIT)$', u):
        return u
    if re.match(r'^GOTO\s+\w+$', u):
        return 'GOTO'
    m = re.match(r'^[A-Za-z_]\w*\s*\((.*)\)$', s)
    if m and (not m.group(1).strip() or looks_like_code(m.group(1))):
        return 'call'
    if re.match(r'^(PTP|LIN|CIRC|SPTP|SLIN|SCIRC)(_REL)?\s+(\{.*\}|\$?\w+)(\s*,\s*\w+)?(\s+C_\w+)*$', u):
        return 'motion'
    if re.match(r'^(GLOBAL\s+)?SIGNAL\s+\w+\s+\$(IN|OUT)\[', u):
        return 'SIGNAL'
    if re.match(r'^(GLOBAL\s+)?DECL\s+\w+\s+\w+', u) or re.match(
            r'^(GLOBAL\s+)?(INT|BOOL|REAL|CHAR|E6POS|E6AXIS|POS|AXIS|FRAME|FDAT|PDAT|LDAT)'
            r'\s+[A-Z_]\w*\s*(=|,|\[|$)', u):
        return 'declaration'
    if re.match(r'^TRIGGER\s+WHEN\b', u):
        return 'TRIGGER'
    return None


def spanish_words(text):
    words = set(re.findall(r'[A-Z]+', fold_case(text)))
    hits = sorted(words & SPANISH)
    if re.search('[ñÑ¿¡]', text):
        hits.append('ñ/¿/¡')
    return hits


def structure_issues(path, text):
    found = fold_issues(path, text)
    if path.lower().endswith(('.src', '.sub')):
        found += nesting_issues(path, text)
    return found


def def_names(text):
    # [ \t], not \s: '^\s*' would run across blank lines and make the scan quadratic
    return re.findall(r'^[ \t]*(?:GLOBAL[ \t]+)?DEF(?:FCT[ \t]+\S+)?[ \t]+([A-Za-z_]\w*)',
                      '\n'.join(split_code(l) for l in lines_of(text)), re.M | re.I)


# ------------------------------------------------------------ inline forms

def is_form_header(line):
    """The headers check_cleanup.form_bodies() returns a body for."""
    s = line.rstrip('\r').lstrip()
    return s.upper().startswith(';FOLD') and ';%{' in s and '%P' in s and '%CEXT' not in s


def forms_with_lines(text):
    """[(header line number, header, [(line number, stripped body line)])]:
    check_cleanup.form_bodies() with line numbers."""
    heads = [n for n, l in enumerate(text.split('\n'), 1) if is_form_header(l)]
    forms = form_bodies(text)
    assert len(heads) == len(forms), 'inline-form header scan out of step with form_bodies'
    return [(n, h, [(n + 1 + k, b) for k, b in enumerate(body)])
            for n, (h, body) in zip(heads, forms)]


def form_data(header):
    return header[header.index(';%{'):]


def form_kind(header):
    """('KUKATPBASIS', 'MOVE') ... from the form data."""
    data = form_data(header)
    mod = re.search(r'%M(\w+)', data)
    cmd = re.search(r'%C(\w+)', data)
    return (mod.group(1).upper() if mod else ''), (cmd.group(1).upper() if cmd else '')


def form_params(header):
    """'%P 1:PTP, 2:P9, 3:, 5:100' -> {1: 'PTP', 2: 'P9', 3: '', 5: '100'}"""
    m = re.search(r'%P\s*(.*)$', form_data(header))
    return {int(k): v.strip() for k, v in re.findall(r'(\d+):([^,]*)', m.group(1))} if m else {}


def same_number(a, b):
    try:
        return math.isclose(float(a), float(b), rel_tol=1e-9, abs_tol=1e-9)
    except (TypeError, ValueError):
        return str(a).strip().upper() == str(b).strip().upper()


def compact(code):
    return re.sub(r'\s+', '', code).upper()


GENERATED = {
    # SET_CD_PARAMS: written by KSS 8 motion forms when collision detection is configured.
    'MOVE': lambda n, c: re.match(r'^(\$BWDSTART|PDAT_ACT|LDAT_ACT|FDAT_ACT|\$H_POS)=|^BAS\(|^SET_CD_PARAMS\(', c)
    or re.match(r'^(PTP|LIN|CIRC)\s', n),
    'OUT': lambda n, c: re.match(r'^\$OUT(_C)?\[\d+\]=', c) or c == 'CONTINUE',
    'WAIT': lambda n, c: n.startswith('WAIT SEC'),
    'EXT_WAIT_FOR': lambda n, c: n.startswith('WAIT FOR') or c == 'CONTINUE',
}


def check_motion_form(header, p, body):
    """Problems of a PTP/LIN/CIRC form: fold text, %P data and body must agree."""
    probs = []
    kind, pt, approx, vel, dat = (p.get(1, '').upper(), p.get(2, ''), p.get(3, ''),
                                  p.get(5, ''), p.get(7, ''))
    if kind not in ('PTP', 'LIN', 'CIRC'):
        return []           # a motion form this check does not know: no opinion
    norm = [normalise(c).upper() for c in body]
    comp = [compact(c) for c in body]
    moves = [n for n in norm if re.match(r'^(PTP|LIN|CIRC)\s', n)]
    if len(moves) != 1:
        probs.append(f'{len(moves)} motion statements in the body, the form generates one')
    else:
        tok = moves[0].split()
        if tok[0] != kind:
            probs.append(f'form data 1:{kind} but the body moves {tok[0]}')
        elif kind == 'CIRC':
            if pt and 'X' + pt.upper() not in moves[0].replace(',', ' ').split():
                probs.append(f'form data 2:{pt} is not a point of the body: {moves[0]}')
        elif len(tok) < 2 or tok[1] != 'X' + pt.upper():
            probs.append(f'form data 2:{pt} but the body moves to {tok[1] if len(tok) > 1 else "nothing"}')
        cs = [t for t in tok[2:] if t.startswith('C_')]
        if kind != 'CIRC' and cs != approx.upper().split():
            probs.append(f'form data 3:{approx or "(exact stop)"} but the body has '
                         f'{" ".join(cs) or "no approximation"}')
    if kind == 'CIRC':
        # The CIRC form numbers its fields differently (auxiliary and end
        # point, then approximation, velocity and data further on): only
        # what does not depend on that numbering is compared.
        return probs
    f = [c for c in comp if c.startswith('FDAT_ACT=')]
    if f != ['FDAT_ACT=F' + pt.upper()]:
        probs.append(f'form data 2:{pt} expects FDAT_ACT=F{pt}, body has {", ".join(f) or "none"}')
    key, pre = ('PDAT_ACT=', 'P') if kind == 'PTP' else ('LDAT_ACT=', 'L')
    d = [c for c in comp if c.startswith(key)]
    if dat and d != [key + pre + dat.upper()]:
        probs.append(f'form data 7:{dat} expects {key}{pre}{dat}, body has {", ".join(d) or "none"}')
    # KSS 8 forms set the velocity with BAS(#PTP_PARAMS,v) / BAS(#CP_PARAMS,v),
    # older ones with BAS(#VEL_PTP,v) / BAS(#VEL_CP,v).
    params = ('PTP_PARAMS', 'VEL_PTP') if kind == 'PTP' else ('CP_PARAMS', 'VEL_CP')
    bas = [re.match(r'^BAS\(#(\w+),([^)]*)\)$', c) for c in comp if c.startswith('BAS(')]
    bas = [m for m in bas if m and m.group(1) in ('PTP_PARAMS', 'VEL_PTP', 'CP_PARAMS', 'VEL_CP')]
    if vel and bas and not any(m.group(1) in params and same_number(m.group(2), vel) for m in bas):
        probs.append(f'form data 5:{vel} expects BAS(#{params[0]},{vel}), body has '
                     + ', '.join(f'BAS(#{m.group(1)},{m.group(2)})' for m in bas))
    shown = header[:header.index(';%{')]
    m = re.match(r'\s*;FOLD\s+(PTP|LIN|CIRC)\s+(\S+)(.*?)\bVel\s*=\s*([\d.]+)\s*(?:%|m/s)\s+(\w+)',
                 shown, re.I)
    if m:
        if m.group(1).upper() != kind:
            probs.append(f'fold text shows {m.group(1)}, form data 1:{kind}')
        if m.group(2).upper() != pt.upper():
            probs.append(f'fold text shows point {m.group(2)}, form data 2:{pt}')
        if ('CONT' in m.group(3).upper().split()) != bool(approx):
            probs.append(f'fold text {"shows" if "CONT" in m.group(3).upper() else "lacks"} CONT, '
                         f'form data 3:{approx or "(exact stop)"}')
        if not same_number(m.group(4), vel):
            probs.append(f'fold text shows Vel={m.group(4)}, form data 5:{vel}')
        if dat and m.group(5).upper() != dat.upper():
            probs.append(f'fold text shows {m.group(5)}, form data 7:{dat}')
    return probs


def check_out_form(header, p, body):
    probs = []
    idx, state = p.get(2, ''), p.get(5, '').upper()
    outs = [re.match(r'^\$OUT(?:_C)?\[(\d+)\]=(TRUE|FALSE)$', compact(c)) for c in body]
    outs = [m for m in outs if m]
    if len(outs) != 1:
        probs.append(f'{len(outs)} output assignments in the body, the form generates one')
    else:
        if outs[0].group(1) != idx:
            probs.append(f'form data 2:{idx} but the body writes $OUT[{outs[0].group(1)}]')
        if outs[0].group(2) != state:
            probs.append(f'form data 5:{state} but the body sets '
                         f'$OUT[{outs[0].group(1)}]={outs[0].group(2)}')
    shown = header[:header.index(';%{')]
    m = re.match(r"\s*;FOLD\s+OUT\s+(\d+)\s+'[^']*'\s+State\s*=\s*(TRUE|FALSE)", shown, re.I)
    if m:
        if m.group(1) != idx:
            probs.append(f'fold text shows OUT {m.group(1)}, form data 2:{idx}')
        if m.group(2).upper() != state:
            probs.append(f'fold text shows State={m.group(2).upper()}, form data 5:{state}')
    return probs


def check_wait_form(header, p, body):
    probs = []
    t = p.get(3, '')
    waits = [re.match(r'^WAIT SEC (\S+)$', normalise(c), re.I) for c in body]
    waits = [m for m in waits if m]
    if len(waits) != 1:
        probs.append(f'{len(waits)} WAIT SEC statements in the body, the form generates one')
    elif not same_number(waits[0].group(1), t):
        probs.append(f'form data 3:{t} but the body waits WAIT SEC {waits[0].group(1)}')
    m = re.match(r'\s*;FOLD\s+WAIT\s+Time\s*=\s*([\d.]+)\s*sec', header[:header.index(';%{')], re.I)
    if m and not same_number(m.group(1), t):
        probs.append(f'fold text shows Time={m.group(1)} sec, form data 3:{t}')
    return probs


def fmt_conds(conds):
    return ' AND '.join(f'{"NOT " if neg else ""}{io}[{idx}]' for neg, io, idx in conds) or 'nothing'


def check_wait_for_form(header, p, body):
    """WAIT FOR form: each condition group k holds 4+8k:NOT, 5+8k:$IN, 6+8k:index."""
    probs, want, k = [], [], 0
    while 5 + 8 * k in p and 6 + 8 * k in p:
        io, idx = p[5 + 8 * k].upper(), p[6 + 8 * k]
        if io or idx:
            want.append((p.get(4 + 8 * k, '').upper() == 'NOT', io, idx))
        k += 1
    waits = [normalise(c).upper() for c in body if normalise(c).upper().startswith('WAIT FOR')]
    if len(waits) != 1:
        return [f'{len(waits)} WAIT FOR statements in the body, the form generates one']
    got = [(bool(m.group(1)), m.group(2).upper(), m.group(3))
           for m in re.finditer(r'(NOT\s*)?(\$\w+)\[(\d+)\]', waits[0], re.I)]
    if want != got:
        probs.append(f'form data waits for {fmt_conds(want)} but the body waits for {fmt_conds(got)}')
    shown = [(bool(m.group(1)), '$' + m.group(2).upper(), m.group(3)) for m in re.finditer(
        r'(NOT\s+)?\b(IN|OUT|FLAG|CYCFLAG|TIMER_FLAG)\s+(\d+)', header[:header.index(';%{')], re.I)]
    if shown and shown != want:
        probs.append(f'fold text shows {fmt_conds(shown)}, form data {fmt_conds(want)}')
    return probs


FORM_CHECKS = {'MOVE': check_motion_form, 'OUT': check_out_form, 'WAIT': check_wait_form,
               'EXT_WAIT_FOR': check_wait_for_form}


def form_problems(header, body_lines):
    """check 4 for one KUKATPBASIS form; [] for forms of other packages."""
    mod, cmd = form_kind(header)
    if mod != 'KUKATPBASIS' or cmd not in FORM_CHECKS:
        return []
    code = [split_code(b).strip() for b in body_lines]
    return FORM_CHECKS[cmd](header, form_params(header), [c for c in code if c])


def hand_lines(header, body):
    """[(line number, normalised code)] of executable body lines the form
    does not generate (check 5)."""
    mod, cmd = form_kind(header)
    gen = GENERATED.get(cmd) if mod == 'KUKATPBASIS' else None
    if gen is None:
        return []
    out = []
    for n, line in body:
        code = normalise(split_code(line))
        if code and not gen(code.upper(), compact(code)):
            out.append((n, code))
    return out


def ac_forms(text):
    """AutomationCore inline forms: ';FOLD title' / ';FOLD ;%{h}' / ';Params
    IlfProvider=...' / ';ENDFOLD' / call / ';ENDFOLD'. Returns [(params line
    number, params text, (call line number, call) or None, [(n, code)] of
    other executable lines inside the outer fold)]."""
    lines = lines_of(text)
    out = []
    for i, line in enumerate(lines):
        if not line.strip().startswith(';Params IlfProvider='):
            continue
        j, depth = i + 1, 1
        while j < len(lines) and depth:          # end of the ;%{h} fold
            s = lines[j].strip().upper()
            depth += s.startswith(';FOLD') - s.startswith(';ENDFOLD')
            j += 1
        execs, depth = [], 1
        while j < len(lines) and depth:          # rest of the outer fold
            s = lines[j].strip().upper()
            if s.startswith(';FOLD'):
                depth += 1
            elif s.startswith(';ENDFOLD'):
                depth -= 1
            else:
                code = normalise(split_code(lines[j]))
                if code:
                    execs.append((j + 1, code))
            j += 1
        out.append((i + 1, line.strip(), execs[0] if execs else None, execs[1:]))
    return out


def ac_problem(params, call):
    m = re.search(r'AC_CmdParam\s*=\s*(\d+)', params)
    c = re.match(r'^\w+\s*\(\s*(\d+)', call[1]) if call else None
    if m and c and m.group(1) != c.group(1):
        return (f'AutomationCore form AC_CmdParam={m.group(1)} but the call passes {c.group(1)}: '
                f'confirming the form regenerates the call from the form value (F21)')
    return None


# ----------------------------------------------------------------- diffs

def code_diff(old, new, context=2):
    """Diff of two numbered_code() lists. Returns (rendered lines, removed,
    added, new line numbers inserted or replaced)."""
    sm = difflib.SequenceMatcher(None, [c for _, c in old], [c for _, c in new], autojunk=False)
    out, removed, added, touched = [], 0, 0, set()
    for group in sm.get_grouped_opcodes(context):
        a, b = group[0][1], group[0][3]
        out.append(f'@@ base line {old[a][0] if a < len(old) else "end"}, '
                   f'backup line {new[b][0] if b < len(new) else "end"} @@')
        for tag, a1, a2, b1, b2 in group:
            if tag == 'equal':
                out += [f'  {new[k][0]:>5}  {new[k][1]}' for k in range(b1, b2)]
                continue
            out += [f'- {old[k][0]:>5}  {old[k][1]}' for k in range(a1, a2)]
            out += [f'+ {new[k][0]:>5}  {new[k][1]}' for k in range(b1, b2)]
            removed += a2 - a1
            added += b2 - b1
            touched.update(new[k][0] for k in range(b1, b2))
    return out, removed, added, touched


def line_diff(old_lines, new_lines):
    """(removed, added, new line numbers inserted or replaced) of a plain line diff."""
    sm = difflib.SequenceMatcher(None, old_lines, new_lines, autojunk=False)
    removed = added = 0
    touched = set()
    for tag, a1, a2, b1, b2 in sm.get_opcodes():
        if tag != 'equal':
            removed += a2 - a1
            added += b2 - b1
            touched.update(range(b1 + 1, b2 + 1))
    return removed, added, touched


def write_diff(out_dir, path, old_text, new_text, base_label):
    old = lines_of(old_text) if old_text is not None else []
    new = lines_of(new_text)
    diff = difflib.unified_diff(old, new, f'{base_label}:{path}' if old_text is not None
                                else '/dev/null', f'backup:{path}', lineterm='', n=3)
    rel = posixpath.join('diffs', path + '.diff')
    dest = os.path.join(out_dir, *rel.split('/'))
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(diff) + '\n')
    return rel


def is_text(data):
    return b'\0' not in data[:8192]


# ------------------------------------------------------------ data (.dat)

COORD = re.compile(r'\b(A[1-6]|E[1-6]|[XYZABCST])\s+(-?\d+(?:\.\d*)?(?:E[+-]?\d+)?)', re.I)


DECL_VALUE = re.compile(r'^(?:GLOBAL\s+)?(?:DECL\s+)?(?:GLOBAL\s+)?([A-Za-z_]\w*)\s+'
                        r'([A-Za-z_$][\w$]*)\s*=\s*(.+)$', re.I)
ELEM_VALUE = re.compile(r'^([A-Za-z_$][\w$]*)\s*\[([^\]]*)\]\s*=\s*(.+)$')
# Data the inline-form editor rewrites whenever a form is opened (LAST_BASIS,
# LAST_TP_PARAMS, LAST_NutWeld): its suggestions for the next form, not program.
EDITOR_TYPE = re.compile(r'_SUGG_T$|^MODULEPARAM_T$', re.I)


def decl_values(text):
    """{name: (type, value)} of the initialised declarations of a .dat file."""
    out = {}
    for raw in lines_of(text):
        code = normalise(split_code(raw))
        m = DECL_VALUE.match(code)
        if m and m.group(1).upper() not in ('SIGNAL', 'DECL', 'GLOBAL'):
            out[m.group(2)] = (m.group(1).upper(), m.group(3))
    return out


def value_key(code):
    """(key, display name, variable name, type or None, value) of a .dat line
    that gives a variable its value ('DECL INT nX=5', 'nArr[3]=7'), else None."""
    m = DECL_VALUE.match(code)
    if m and m.group(1).upper() not in ('SIGNAL', 'DECL', 'GLOBAL', 'CONST'):
        return ('decl', m.group(1).upper(), m.group(2).lower()), m.group(2), m.group(2), m.group(1), m.group(3)
    m = ELEM_VALUE.match(code)
    if m:
        name = f'{m.group(1)}[{m.group(2).strip()}]'
        return ('elem', m.group(1).lower(), compact(m.group(2))), name, m.group(1), None, m.group(3)
    return None


def written_names(texts):
    """Lower-case names the program assigns somewhere ('nX=...', 'nArr[i]=...',
    'rec.field=...', 'FOR i=...'). A .dat keeps the last value the program
    wrote to its variables (persistent data), so a backup taken after the
    robot ran shows new values for them without any program change."""
    found = set()
    # the index may hold one nested index: CL_T_LOG[n,CL_T_ROW[n],s]=...
    pat = re.compile(r'(?<![\w$.])([A-Za-z_$][\w$]*)[ \t]*(?:\[(?:[^\[\]\n]|\[[^\[\]\n]*\])*\])?'
                     r'(?:\.[A-Za-z_]\w*)*[ \t]*=(?!=)')
    for p, t in texts.items():
        if p.lower().endswith(('.src', '.sub')):
            for line in live(t).split('\n'):
                if '=' in line:
                    found |= {m.group(1).lower() for m in pat.finditer(line)}
    return found


def split_runtime_values(old_code, new_code, written):
    """Take out of two numbered_code() lists of a .dat the value-only changes
    of variables the program writes at run time (and the first value of an
    element of an array it writes), and of the editor's suggestion data.
    Returns (old, new, [(name, old value, new value)])."""
    def keyed(code):
        out, dup = {}, set()
        for i, (_, c) in enumerate(code):
            k = value_key(c)
            if k:
                if k[0] in out:
                    dup.add(k[0])
                out[k[0]] = (i, k)
        return {k: v for k, v in out.items() if k not in dup}
    old_k, new_k = keyed(old_code), keyed(new_code)
    drop_old, drop_new, changes = set(), set(), []
    for key, (j, (_, shown, var, typ, value)) in new_k.items():
        if key not in old_k:
            # an element of an array the program writes appears in the .dat the
            # first time the program writes it (CL_CYCLE_TIME.dat, CL_T_LOG)
            if key[0] == 'elem' and var.lower() in written:
                drop_new.add(j)
                changes.append((shown, '-', value))
            continue
        if old_k[key][1][4] == value:
            continue
        if var.lower() in written or (typ and EDITOR_TYPE.search(typ)):
            drop_old.add(old_k[key][0])
            drop_new.add(j)
            changes.append((shown, old_k[key][1][4], value))
    changes.sort(key=lambda c: natural(c[0]))
    return ([c for i, c in enumerate(old_code) if i not in drop_old],
            [c for j, c in enumerate(new_code) if j not in drop_new], changes)


def short(value, width=70):
    return value if len(value) <= width else value[:width] + '...'


def point_change(old, new):
    """How a taught point moved, or None if it is not a point."""
    a = {k.upper(): float(v) for k, v in COORD.findall(old)}
    b = {k.upper(): float(v) for k, v in COORD.findall(new)}
    parts = []
    if all(k in a and k in b for k in 'XYZ'):
        parts.append(f'moved {math.dist([a[k] for k in "XYZ"], [b[k] for k in "XYZ"]):.1f} mm')
        rot = [abs((b[k] - a[k] + 180) % 360 - 180) for k in 'ABC' if k in a and k in b]
        if rot and max(rot) >= 0.05:
            parts.append(f'rotated up to {max(rot):.1f} deg')
        if (a.get('S'), a.get('T')) != (b.get('S'), b.get('T')):
            def st(p):
                return '/'.join('?' if p.get(k) is None else f'{p[k]:.0f}' for k in 'ST')
            parts.append(f'S/T {st(a)} -> {st(b)} (ARM CONFIGURATION CHANGED)')
    elif all(f'A{i}' in a and f'A{i}' in b for i in range(1, 7)):
        parts.append(f'axes moved up to {max(abs(b[f"A{i}"] - a[f"A{i}"]) for i in range(1, 7)):.1f} deg')
    return ', '.join(parts) or None


def natural(name):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r'(\d+)', name)]


def decl_types(text):
    """{name: type} of every declaration of a .dat, initialised or not
    ('DECL KRLMSGPAR_T MsgPar[3]' included)."""
    out = {}
    for raw in lines_of(text):
        code = normalise(split_code(raw))
        found = declared_names(code) if code else []
        if not found:
            continue
        toks = [t for t in re.findall(r'[A-Za-z_$][\w$]*', code)
                if t.upper() not in ('GLOBAL', 'DECL', 'PUBLIC', 'CONST')]
        kind = toks[0].upper() if toks else '?'
        for n in found:
            out[n] = kind
    return out


def data_changes(old_text, new_text, runtime=()):
    """Readable list of what changed in the declarations of a .dat:
    re-taught points first, then other values, then added and removed
    names grouped by type. `runtime`: names whose value change is a value
    written by the program (listed apart)."""
    old, new = decl_values(old_text or ''), decl_values(new_text)
    skip = {r.lower() for r in runtime}
    moved, values = [], []
    for name in sorted(set(old) & set(new), key=natural):
        if old[name] != new[name] and name.lower() not in skip:
            how = point_change(old[name][1], new[name][1]) if old[name][0] == new[name][0] else None
            if how:
                moved.append(f'{name} ({new[name][0]}) re-taught: {how}')
            else:
                values.append(f'{name} ({new[name][0]}): {short(old[name][1])} -> {short(new[name][1])}')
    old_t, new_t = decl_types(old_text or ''), decl_types(new_text)
    added, removed = {}, {}
    for name in sorted(set(old_t) | set(new_t), key=natural):
        if name not in new_t:
            removed.setdefault(old_t[name], []).append(name)
        elif name not in old_t:
            added.setdefault(new_t[name], []).append(name)

    def grouped(label, table):
        return [f'{label} {len(names)} {kind}: {", ".join(names[:12])}{" ..." if len(names) > 12 else ""}'
                for kind, names in sorted(table.items())]
    return moved + values + grouped('added', added) + grouped('removed', removed)


def declared_in(text):
    """The names declared in a KRL file ({lower case: as written}), and the
    lower-case names of those declared GLOBAL."""
    names, glob = {}, set()
    for raw in lines_of(text):
        code = split_code(raw)
        found = declared_names(code) if code.strip() else []
        names.update((n.lower(), n) for n in found)
        if re.search(r'\bGLOBAL\b', code, re.I):
            glob |= {n.lower() for n in found}
    return names, glob


def twin(path, texts):
    """The .dat of a .src (or the .src of a .dat) in `texts`, matched without case."""
    stem, ext = path.rsplit('.', 1)
    other = 'dat' if ext.lower() in ('src', 'sub') else 'src'
    return next((p for p in texts if p.lower() == f'{stem}.{other}'.lower()), None)


# ---------------------------------------------------------------- signals

def signal_changes(base_sig, new_sig):
    """Declarations that differ between base and backup, merged into index ranges."""
    rows = []
    for key in sorted(set(base_sig) | set(new_sig)):
        b, n = sorted(base_sig.get(key, ())), sorted(new_sig.get(key, ()))
        if b == n:
            continue
        last = rows[-1] if rows else None
        if last and last['io'] == key[0] and last['last'] == key[1] - 1 and \
                last['base'] == b and last['new'] == n:
            last['last'] = key[1]
        else:
            rows.append({'io': key[0], 'first': key[1], 'last': key[1], 'base': b, 'new': n})
    return rows


def describe_signal_change(r):
    rng = f'{r["first"]}' if r['first'] == r['last'] else f'{r["first"]}..{r["last"]}'
    return (f'${r["io"]}[{rng}]: {", ".join(r["base"]) or "(not declared)"} -> '
            f'{", ".join(r["new"]) or "(not declared)"}')


# ------------------------------------------------------------- the audit

class Audit:
    """The FAIL / WARN / INFO findings of the mechanical checks."""
    def __init__(self):
        self.findings = []

    def add(self, level, check, path, line, msg):
        self.findings.append({'level': level, 'check': check, 'name': CHECKS.get(check, ''),
                              'file': path, 'line': line, 'message': msg})

    def add_all(self, level, check, path, items):
        """Add [(line, message)], at most MAX_PER_FILE of them, then a count."""
        for k, (line, msg) in enumerate(items):
            if k == MAX_PER_FILE:
                self.add(level, check, path, line, f'... and {len(items) - k} more of the same')
                break
            self.add(level, check, path, line, msg)


def form_key(header, body):
    """What identifies an inline form: its header (tool name blanked) and body."""
    return header_key(header), tuple(b for _, b in body)


class Change:
    """One changed or added KRL file: both versions, their executable code,
    and which lines of the new version are new."""

    def __init__(self, path, old_raw, new_raw, written=frozenset()):
        self.path, self.old_raw, self.new_raw = path, old_raw, new_raw
        self.old = old_raw.decode('latin-1') if old_raw is not None else None
        self.new = new_raw.decode('latin-1')
        self.old_lines = lines_of(self.old) if self.old is not None else []
        self.new_lines = lines_of(self.new)
        old_code = numbered_code(self.old) if self.old is not None else []
        new_code = numbered_code(self.new)
        self.runtime = []
        runtime_lines = set()
        if path.lower().endswith('.dat') and self.old is not None:
            kept = set(new_code)
            old_code, new_code, self.runtime = split_runtime_values(old_code, new_code, written)
            runtime_lines = {n for n, _ in kept - set(new_code)}
        self.code_diff, self.code_removed, self.code_added, self.code_touched = \
            code_diff(old_code, new_code)
        self.raw_removed, self.raw_added, self.raw_touched = line_diff(self.old_lines, self.new_lines)
        self.raw_touched -= runtime_lines       # a value the program wrote is nobody's edit
        seen = Counter(l.strip() for l in self.old_lines)
        # Lines inserted or rewritten whose text the old file does not hold
        # anywhere: a comment block that only moved is not new.
        self.new_text = {n for n in self.raw_touched if not seen[self.new_lines[n - 1].strip()]}
        self.old_forms = forms_with_lines(self.old) if self.old is not None else []
        self.forms = forms_with_lines(self.new)
        known = {form_key(h, body) for _, h, body in self.old_forms}
        self.changed_forms = [f for f in self.forms if form_key(f[1], f[2]) not in known]

    def is_program(self):
        return self.path.lower().endswith(('.src', '.sub'))

    def is_integrator(self):
        """The style checks (2 non-ASCII, 6 to 10) apply to the integrator's
        program; a KUKA or tech-package file has its own comments, German
        and commented-out code included, and an edit to it is flagged C28."""
        return area(self.path) == 'integrator program'


def check_structure(audit, ch, ctx):
    """1: ;FOLD balance and block nesting no worse than in the base: every
    defect the base did not have is a FAIL, also when the backup fixed
    another one in the same file."""
    now = structure_issues(ch.path, ch.new)
    before = structure_issues(ch.path, ch.old) if ch.old is not None else []

    def key(msg):
        return re.sub(r'\d+', 'N', msg[len(ch.path):])
    left = Counter(key(m) for m in before)
    new = []
    for msg in now:
        if left[key(msg)]:
            left[key(msg)] -= 1
        else:
            new.append(msg)
    fixed = sum(left.values())
    if fixed:
        audit.add('INFO', 1, ch.path, None, f'fold/block structure improved: {fixed} of {len(before)} '
                  f'pre-existing defects fixed')
    for msg in new:
        m = re.match(re.escape(ch.path) + r':(\d+)', msg)
        audit.add('FAIL', 1, ch.path, int(m.group(1)) if m else None,
                  msg[len(ch.path):].lstrip(': ') + f' (base had {len(before)} structure defects, '
                  f'backup has {len(now)})')


def readable(line):
    """A line decoded as latin-1, shown as UTF-8 when its bytes are UTF-8
    (a comment typed on a laptop): 'PRESIÃ\\x93N' -> 'PRESIÓN'."""
    try:
        return line.encode('latin-1').decode('utf-8')
    except (UnicodeEncodeError, UnicodeDecodeError):
        return line


def check_format(audit, ch, ctx):
    """2: line-ending convention kept, no non-ASCII bytes on new lines of the
    integrator's program. CRLF is what the smartPAD editor writes, so an LF
    file saved on the controller becoming CRLF is INFO; anything else WARN."""
    if ch.old_raw is not None and eol_style(ch.new_raw) != eol_style(ch.old_raw):
        level = 'INFO' if eol_style(ch.new_raw) == 'CRLF' else 'WARN'
        audit.add(level, 2, ch.path, 1, f'line endings changed from {eol_style(ch.old_raw)} to '
                  f'{eol_style(ch.new_raw)} (the KRC reads both; git diff shows every line changed, '
                  f'the code diff of this report does not)')
    elif ch.old_raw is None and eol_style(ch.new_raw) == 'mixed':
        audit.add('WARN', 2, ch.path, 1, 'mixed CRLF and LF line endings')
    if not ch.is_integrator():
        return
    items = []
    for n in sorted(ch.raw_touched):
        line = ch.new_lines[n - 1]
        odd = sorted(set(c for c in line if ord(c) > 127))
        if odd:
            utf8 = readable(line) != line
            shown = sorted(set(c for c in readable(line) if ord(c) > 127))
            items.append((n, f'non-ASCII character(s) introduced: {"".join(shown)!r}'
                             + (' (UTF-8 bytes; the smartPAD shows them as two characters)' if utf8 else '')))
    audit.add_all('WARN', 2, ch.path, items)


def check_signal_comments(audit, ch, ctx):
    """3: a comment naming '$OUT[n] name' names the signal declared there."""
    audit.add_all('FAIL', 3, ch.path, signal_comment_problems(ch.new_lines, ctx, ch.new_text.__contains__))


def check_forms(audit, ch, ctx):
    """4 and 5 on the inline forms that are new or changed."""
    known_hand = {(form_data(h), c) for _, h, body in ch.old_forms for _, c in hand_lines(h, body)}
    for n, header, body in ch.changed_forms:
        shown = header[:header.index(';%{')].strip()
        for prob in form_problems(header, [b for _, b in body]):
            audit.add('FAIL', 4, ch.path, n, f'{shown[:70]}: {prob}')
        for ln, code in hand_lines(header, body):
            if (form_data(header), code) not in known_hand:
                audit.add('WARN', 5, ch.path, ln, f'hand-typed line inside inline form - lost on '
                          f'Touch Up (F32): {code}')
    old_ac = ac_forms(ch.old) if ch.old is not None else []
    known = {(p, c[1] if c else None) for _, p, c, _ in old_ac}
    known_hand = {(p, code) for _, p, _, rest in old_ac for _, code in rest}
    for n, params, call, rest in ac_forms(ch.new):
        prob = ac_problem(params, call)
        if prob and (params, call[1] if call else None) not in known:
            audit.add('INFO', 4, ch.path, call[0] if call else n, prob)
        for ln, code in rest:
            # AutomationCore forms generate one or two AC_ calls (a zone request:
            # AC_ZoneLogic (3,False) then AC_ZoneCheck (3)); anything else is typed
            if (params, code) not in known_hand and not re.match(r'^AC_\w+\s*\(', code, re.I):
                audit.add('WARN', 5, ch.path, ln, f'hand-typed line inside AutomationCore form - lost '
                          f'when the form is confirmed (F32): {code}')


def dat_values(path, ctx):
    """{lower-case name: (type, value)} of a .dat of the backup, cached."""
    cache = ctx.setdefault('_dat_values', {})
    if path not in cache:
        cache[path] = {n.lower(): v for n, v in decl_values(ctx['texts'][path]).items()}
    return cache[path]


def find_fdat(name, src, ctx):
    """The value of FDAT `name` as the module `src` sees it: its own .dat
    first, then any .dat of the backup that declares it GLOBAL or $config.dat."""
    dat = twin(src, ctx['texts'])
    if dat:
        v = dat_values(dat, ctx).get(name.lower())
        if v:
            return v[1]
    if name.lower() in ctx.get('global_decls', ()):
        for p in sorted(ctx['texts']):
            if p.lower().endswith('.dat'):
                v = dat_values(p, ctx).get(name.lower())
                if v and v[0] == 'FDAT':
                    return v[1]
    return None


def tool_base_problem(header, fdat):
    """The fold text of a motion form shows the tool, base and external-TCP
    mode the robot uses; they come from the point's FDAT. A hand edit of the
    FDAT in the .dat (or of the fold) makes the two disagree: the robot moves
    with another tool or base than the program says (F22)."""
    shown = header[:header.index(';%{')]
    probs = []
    for label, key in (('Tool', 'TOOL_NO'), ('Base', 'BASE_NO')):
        a = re.search(label + r'\[(\d+)\]', shown)
        b = re.search(key + r'\s+(\d+)', fdat, re.I)
        if a and b and a.group(1) != b.group(1):
            probs.append(f'fold text shows {label}[{a.group(1)}], its FDAT has {key} {b.group(1)}')
    ipo = re.search(r'IPO_FRAME\s+#(\w+)', fdat, re.I)
    if ipo and ('extTCP' in shown) != (ipo.group(1).upper() == 'TCP'):
        probs.append(f'fold text {"shows" if "extTCP" in shown else "lacks"} extTCP, its FDAT has '
                     f'IPO_FRAME #{ipo.group(1)}')
    return probs


def check_tool_base(audit, ch, ctx):
    """4 (Tool/Base): the motion forms that are new or changed, and the forms
    whose FDAT changed in a .dat, agree with their FDAT."""
    reported = ctx.setdefault('_tool_base_reported', set())
    targets = []
    if ch.is_program():
        targets = [(ch.path, n, h) for n, h, _ in ch.changed_forms]
    elif ch.path.lower().endswith('.dat'):
        old = {n.lower(): v for n, v in decl_values(ch.old or '').items()}
        changed = {n.lower() for n, (t, v) in decl_values(ch.new).items()
                   if t == 'FDAT' and old.get(n.lower()) != (t, v)}
        if not changed:
            return
        names, glob = declared_in(ch.new)
        src = twin(ch.path, ctx['texts'])
        users = sorted(p for p in ctx['texts'] if p.lower().endswith(('.src', '.sub'))) \
            if changed & glob or ch.path.lower().endswith('$config.dat') else [src] if src else []
        for user in users:
            for n, h, _ in forms_with_lines(ctx['texts'][user]):
                p = form_params(h)
                if form_kind(h) == ('KUKATPBASIS', 'MOVE') and ('f' + p.get(2, '')).lower() in changed:
                    targets.append((user, n, h))
    for path, n, header in targets:
        if (path, n) in reported or form_kind(header) != ('KUKATPBASIS', 'MOVE'):
            continue
        p = form_params(header)
        if p.get(1, '').upper() not in ('PTP', 'LIN') or not p.get(2):
            continue
        fdat = find_fdat('F' + p[2], path, ctx)
        for prob in tool_base_problem(header, fdat) if fdat else []:
            reported.add((path, n))
            audit.add('FAIL', 4, path, n, f'{header[:header.index(";%{")].strip()[:70]}: {prob}')


def check_data(audit, ch, ctx):
    """11: a new motion form needs its point and data declared; a declaration
    taken out of a .dat must not be used any more."""
    if ch.is_program():
        dat = twin(ch.path, ctx['texts'])
        local = declared_in(ctx['texts'][dat])[0] if dat else {}
        for n, header, body in ch.changed_forms:
            if form_kind(header) != ('KUKATPBASIS', 'MOVE'):
                continue
            p = form_params(header)
            kind, pt, data = p.get(1, '').upper(), p.get(2, ''), p.get(7, '')
            # What the form data names (regenerated on Touch Up; the CIRC form
            # numbers its fields differently) and what the body uses (compiled).
            wanted = ([f'X{pt}', f'F{pt}'] + ([('P' if kind == 'PTP' else 'L') + data] if data else [])
                      if kind in ('PTP', 'LIN') and pt else [])
            for _, line in body:
                code = normalise(split_code(line))
                m = re.match(r'^(?:FDAT_ACT|PDAT_ACT|LDAT_ACT)\s*=\s*([A-Za-z_]\w*)$', code, re.I)
                if m:
                    wanted.append(m.group(1))
                elif re.match(r'^(PTP|LIN|CIRC)\s', code, re.I):
                    wanted += [t for t in re.findall(r'(?<![\w$])[A-Za-z_][\w$]*',
                                                     re.sub(r'\{[^}]*\}', '', code))[1:]
                               if not t.upper().startswith('C_')]
            for name in dict.fromkeys(wanted):
                low = name.lower()
                if low not in local and low not in ctx['global_decls']:
                    where = posixpath.basename(dat) if dat else 'a .dat of this module'
                    audit.add('FAIL', 11, ch.path, n, f'{name} is used by the new {kind} {pt} form but '
                              f'declared neither in {where} nor globally: the module does not compile')
    elif ch.path.lower().endswith('.dat') and ch.old is not None:
        (was, was_global), now = declared_in(ch.old), declared_in(ch.new)[0]
        gone = [was[k] for k in set(was) - set(now)]
        src = twin(ch.path, ctx['texts'])
        for name in sorted(gone, key=natural):
            # A GLOBAL name may be used anywhere, a local one only in its .src.
            users = sorted(ctx['texts']) if name.lower() in was_global or \
                ch.path.lower().endswith('$config.dat') else [src] if src else []
            for user in users:
                if user == ch.path:
                    continue
                text = live(ctx['texts'][user])
                if word_in(name, text):
                    line = next(k for k, l in enumerate(text.split('\n'), 1) if word_in(name, l))
                    audit.add('FAIL', 11, ch.path, None, f'{name} was removed from this file but is still '
                              f'used in {user}:{line}: that module no longer compiles')
                    break


def check_comments(audit, ch, ctx):
    """6 and 7 on new comment lines: commented-out code, Spanish."""
    if not ch.is_integrator():
        return
    code_items, spanish_items = [], []
    for n in sorted(ch.new_text):
        text = readable(comment_text(ch.new_lines[n - 1]))
        if not text:
            continue
        kind = commented_code_kind(text)
        if kind:
            code_items.append((n, f'commented-out code ({kind}): ;{text[:80]}'))
        words = spanish_words(text)
        if words:
            spanish_items.append((n, f'Spanish in comment ({", ".join(words)}): ;{text[:80]}'))
    audit.add_all('WARN', 6, ch.path, code_items)
    audit.add_all('WARN', 7, ch.path, spanish_items)


def check_new_code(audit, ch, ctx):
    """8 and 10 on new or changed executable lines of a program."""
    if not ch.is_program() or not ch.is_integrator():
        return
    in_form = {ln for _, _, body in ch.forms for ln, _ in body}
    io_items, fault_items = [], []
    for n in sorted(ch.code_touched):
        code = normalise(split_code(ch.new_lines[n - 1]))
        up = code.upper()
        if n not in in_form and not re.match(r'^(GLOBAL\s+)?(SIGNAL|DECL)\b', up):
            unnamed = unnamed_io(ch.new_lines, n, code, ctx)
            if unnamed:
                io_items.append((n, f'{", ".join(unnamed)} accessed with no comment naming it in the '
                                    f'4 lines above (C24): {code[:70]}'))
        if up == 'HALT':
            fault_items.append((n, 'new HALT - faults go through an AutomationCore message, not a '
                                   'bare HALT (C21, F07)'))
        elif re.match(r'^WAIT\s+FOR\s*\(?\s*FALSE\s*\)?$', up):
            fault_items.append((n, 'new WAIT FOR FALSE - stops the program for good (C21)'))
        elif up.startswith('WAIT FOR'):
            window = ch.new_lines[max(0, n - 11):n + 10]
            if not any(TIMEOUT_HINT.search(split_code(l)) for l in window):
                fault_items.append((n, f'new WAIT FOR with no timeout ($TIMER) nearby (F15): {code[:70]}'))
    audit.add_all('WARN', 8, ch.path, io_items)
    audit.add_all('INFO', 10, ch.path, fault_items)


def check_new_module(audit, ch, ctx):
    """9: a new module carries the Gestamp header and a navigator comment."""
    if ch.old is not None or not ch.path.lower().endswith('.src') or not ch.is_integrator():
        return
    if not any(re.match(r'^\s*;\s*Gestamp Standards', l, re.I) for l in ch.new_lines):
        audit.add('WARN', 9, ch.path, None, "new module without the '; Gestamp Standards' header "
                  "block (C03, docs/CONVENTIONS.md)")
    elif 'BMW-03-10-R1' not in ch.new:
        audit.add('INFO', 9, ch.path, None, 'header does not carry the designation BMW-03-10-R1 (C02)')
    if not any(l.startswith('&COMMENT') and l[8:].strip() for l in ch.new_lines):
        audit.add('WARN', 9, ch.path, None, 'new module without &COMMENT (navigator comment)')


KRL_CHECKS = (check_structure, check_format, check_signal_comments, check_forms, check_tool_base,
              check_data, check_comments, check_new_code, check_new_module)


def analyse_krl(audit, path, old_raw, new_raw, ctx, checked_from=None):
    """Run the checks on one changed or added KRL file and describe its change.
    `checked_from`: the version the programmer started from when it is not the
    base (a file edited on top of the pre-cleanup version): the checks report
    what is new against it, so the old comments it brings back do not bury the
    edit; the description is still against the base."""
    if path.lower().endswith('.dat') and 'written' not in ctx:
        ctx['written'] = written_names(ctx['texts'])     # only needed when a .dat changed
    ch = Change(path, old_raw, new_raw, ctx.get('written', frozenset()))
    checked = ch if checked_from is None else Change(path, checked_from, new_raw, ctx.get('written', frozenset()))
    for check in KRL_CHECKS:
        check(audit, checked, ctx)
    attrs, attr_count = attribute_changes(attributes(ch.old or ''), attributes(ch.new))
    return {
        'status': 'added' if ch.old is None else 'changed',
        'code_removed': ch.code_removed, 'code_added': ch.code_added,
        'comment_only_changes': max(0, ch.raw_removed + ch.raw_added - ch.code_removed
                                    - ch.code_added - attr_count - 2 * len(ch.runtime)),
        'attributes': attrs,
        'code_diff': ch.code_diff,
        'data_changes': data_changes(ch.old, ch.new, [r[0] for r in ch.runtime])
        if path.lower().endswith('.dat') else [],
        'runtime_values': [f'{name}: {short(old, 40)} -> {short(new, 40)}' for name, old, new in ch.runtime],
        'diff': write_diff(ctx['out'], path, ch.old, ch.new, ctx['base_label']),
    }


def signal_comment_problems(lines, ctx, is_new):
    """Check 3 (check_cleanup.check_signal_comments, returning the problems):
    a comment ';$OUT[471] do471GunHome' must name a signal declared at that
    index in the backup. Reported for new comment lines, and for any line
    whose signal or index had its declaration changed by the backup (a
    comment that was right can become wrong without being touched)."""
    sigs, all_names = ctx['signals'], ctx['signal_names']
    items = []
    for n, raw in enumerate(lines, 1):
        code = split_code(raw)
        comment = raw[len(code):]
        if not comment or ';%{' in comment:
            continue
        for io, idx, name in SIG_REF.findall(comment):
            key, low = (io.upper(), int(idx)), name.lower()
            if low in sigs.get(key, set()):
                continue
            if not (is_new(n) or key in ctx['sig_changed_keys'] or low in ctx['sig_changed_names']):
                continue
            if low in all_names:
                items.append((n, f'comment names {name} at ${io}[{idx}], but {name} is declared at '
                                 f'another index'))
            elif SIGNALISH.match(name) and looks_like_signal_name(name):
                items.append((n, f'comment names {name} at ${io}[{idx}], and no signal of that name '
                                 f'is declared'))
    return items


def looks_like_signal_name(name):
    """'do005RobotInCycle', 'dopw1_GunHome', 'DI_004' are signal names; 'DONE',
    'DOWN', 'DIRECTLY' after an address are English words of the comment
    (comments are written in upper case, signal names in mixed case or with
    digits / underscores)."""
    return bool(re.search(r'\d|_|[a-z][A-Z]', name))


def unnamed_io(lines, n, code, ctx):
    """The I/O addresses or signal names accessed by line n that no comment
    in it or in the four lines above names."""
    refs = {}
    for m in IO_LITERAL.finditer(code):
        refs[f'${m.group(1).upper()}[{m.group(2)}]'] = ({(m.group(1).upper(), int(m.group(2)))}, None)
    stripped = re.sub(r'"[^"]*"', '""', code)
    for tok in set(re.findall(r'[A-Za-z_][\w$]*', stripped)):     # $ names are system signals
        keys = ctx['signal_keys'].get(tok.lower())
        if keys:
            refs[tok] = (keys, tok.lower())
    if not refs:
        return []
    comments = ' '.join(lines[k][len(split_code(lines[k])):] for k in range(max(0, n - 5), n))
    cited = {(io.upper(), int(i)) for io, i in CITED_IO.findall(comments)}
    words = {w.lower() for w in re.findall(r'[A-Za-z_$][\w$]*', comments)}
    return [ref for ref, (keys, name) in refs.items()
            if not (keys & cited) and not (name and name in words)]


# ------------------------------------------------------------------ items

def fold_text(s):
    """Header and status text compared without case, accents or punctuation."""
    s = ''.join(c for c in unicodedata.normalize('NFKD', str(s)) if not unicodedata.combining(c))
    return ' '.join(re.sub(r'[^a-z0-9]+', ' ', s.lower()).split())


def is_claimed_fixed(status):
    f = fold_text(status).replace(' ', '')
    return f.startswith('corregido') and 'auditar' in f


XL = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
XL_REL = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
PKG_REL = '{http://schemas.openxmlformats.org/package/2006/relationships}'


def xl_text(node):
    """Text of a shared or inline string: its <t> and rich-text runs (phonetic runs left out)."""
    parts = []
    for child in node:
        if child.tag == XL + 't':
            parts.append(child.text or '')
        elif child.tag == XL + 'r':
            parts += [t.text or '' for t in child.iter(XL + 't')]
    return ''.join(parts)


def xl_column(ref):
    n = 0
    for ch in re.match(r'[A-Z]*', ref.upper()).group(0):
        n = n * 26 + ord(ch) - 64
    return n - 1


def read_xlsx_minimal(path):
    """{sheet name: rows of cell texts}, read straight from the SpreadsheetML parts."""
    with zipfile.ZipFile(path) as z:
        names = set(z.namelist())
        shared = []
        if 'xl/sharedStrings.xml' in names:
            shared = [xl_text(si) for si in ET.fromstring(z.read('xl/sharedStrings.xml')).iter(XL + 'si')]
        rels = {}
        if 'xl/_rels/workbook.xml.rels' in names:
            rels = {r.get('Id'): r.get('Target') for r in
                    ET.fromstring(z.read('xl/_rels/workbook.xml.rels')).iter(PKG_REL + 'Relationship')}
        sheets = {}
        for s in ET.fromstring(z.read('xl/workbook.xml')).iter(XL + 'sheet'):
            target = rels.get(s.get(XL_REL + 'id'), '')
            part = posixpath.normpath(target.lstrip('/') if target.startswith('/') else 'xl/' + target)
            if part not in names:
                continue
            rows = {}
            for row in ET.fromstring(z.read(part)).iter(XL + 'row'):
                r = int(row.get('r')) if row.get('r') else max(rows, default=0) + 1
                cells = {}
                for c in row.findall(XL + 'c'):
                    col = xl_column(c.get('r')) if c.get('r') else max(cells, default=-1) + 1
                    t, v = c.get('t'), c.find(XL + 'v')
                    if t == 's' and v is not None:
                        cells[col] = shared[int(v.text)]
                    elif t == 'inlineStr':
                        node = c.find(XL + 'is')
                        cells[col] = xl_text(node) if node is not None else ''
                    elif t == 'b':
                        cells[col] = 'TRUE' if v is not None and v.text == '1' else 'FALSE'
                    else:
                        cells[col] = v.text if v is not None and v.text else ''
                rows[r] = [cells.get(i, '') for i in range(max(cells, default=-1) + 1)]
            sheets[s.get('name')] = [rows.get(i, []) for i in range(1, max(rows, default=0) + 1)]
    return sheets


def read_xlsx(path):
    """{sheet name: rows of cell texts}: openpyxl when installed, else read_xlsx_minimal()."""
    try:
        import openpyxl
    except ImportError:
        return read_xlsx_minimal(path)
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    return {ws.title: [['' if v is None else str(v) for v in row]
                       for row in ws.iter_rows(values_only=True)] for ws in wb.worksheets}


# Columns of the open-items workbook, found by header text (tools/make_items_xlsx.py
# writes them): the item's modules, and the modules the programmer says he changed.
ITEM_COLUMNS = (('id', lambda h: h == 'id'),
                ('status', lambda h: h.startswith('estado')),
                ('note', lambda h: 'que cambio' in h or 'cambio el programador' in h),
                ('modified', lambda h: h.startswith('modulo') and 'modific' in h),
                ('modules', lambda h: h.startswith('modulo')),
                ('criterion', lambda h: h.startswith('criterio')),
                ('evidence', lambda h: h.startswith('evidencia')),
                ('date', lambda h: h.startswith('fecha programador')),
                ('title', lambda h: h.startswith(('punto', 'descripcion', 'titulo', 'hallazgo'))))


def find_items_table(sheets):
    """(sheet name, {column key: index}, data rows) of the open-items list:
    sheet 'Puntos abiertos' first, header row found by its text."""
    for name in sorted(sheets, key=lambda n: (fold_text(n) != 'puntos abiertos',
                                              not fold_text(n).startswith('puntos'))):
        for i, row in enumerate(sheets[name]):
            cols = {}
            for idx, cell in enumerate(row):
                h = fold_text(cell)
                for key, test in ITEM_COLUMNS:
                    if key not in cols and h and test(h):
                        cols[key] = idx
                        break
            if 'id' in cols and 'status' in cols:
                return name, cols, sheets[name][i + 1:]
    return None, {}, []


PLACEHOLDERS = {'n a', 'na', 'no', 'aplica', 'ninguno', 'ninguna', 'none', 'nada', 'tbd', 'pendiente'}


def item_tokens(cell):
    """Module names of a 'Módulos' cell. 'style1app1opt1..5' and
    'style1app1opt1.src ... style1app1opt5.src' expand to five names."""
    raw = [t.strip('()[]"\'`') for t in re.split(r'[,;\n\s]+', (cell or '').replace('\u2026', ' ... '))]
    out = []
    for tok in raw:
        if tok in ('..', '...'):
            out.append(tok)
            continue
        tok = tok.rstrip(',;:.')
        m = re.match(r'^(.*?)(\d+)\.\.(\d+)$', tok)
        if m and 0 <= int(m.group(3)) - int(m.group(2)) < 50:
            out += [f'{m.group(1)}{k}' for k in range(int(m.group(2)), int(m.group(3)) + 1)]
        elif tok:
            out.append(tok)
    expanded = []
    for i, tok in enumerate(out):
        if tok not in ('..', '...'):
            # '-', 'N/A', 'ninguno' in a modules cell mean "none", not a module
            if re.search(r'[A-Za-z0-9]', tok) and fold_text(tok) not in PLACEHOLDERS:
                expanded.append(tok)
            continue
        a = re.match(r'^(.*?)(\d+)(\.\w+)?$', out[i - 1]) if i else None
        b = re.match(r'^(.*?)(\d+)(\.\w+)?$', out[i + 1]) if i + 1 < len(out) else None
        if a and b and a.group(1) == b.group(1) and a.group(3) == b.group(3) and \
                0 < int(b.group(2)) - int(a.group(2)) < 50:
            expanded += [f'{a.group(1)}{k}{a.group(3) or ""}'
                         for k in range(int(a.group(2)) + 1, int(b.group(2)))]
    return expanded


def match_module(tok, paths, defs):
    t = tok.lower().replace('\\', '/')
    base = [(p, posixpath.basename(p).lower()) for p in paths]
    if '/' in t:
        found = [p for p in paths if p.lower() == t or p.lower().endswith('/' + t)]
    elif any(ch in t for ch in '*?'):
        found = [p for p, b in base if fnmatch.fnmatch(b, t) or fnmatch.fnmatch(b.rsplit('.', 1)[0], t)]
    elif re.search(r'\.[a-z0-9]{1,4}$', t):
        found = [p for p, b in base if b == t]
    else:
        found = [p for p, b in base if b.rsplit('.', 1)[0] == t and is_krl(p)]
    if not found and t in defs:
        found = [defs[t]]
    return sorted(found)


def load_titles():
    """{'F01': title, 'C01': requirement} from the summary tables of docs/FINDINGS.md."""
    titles = {}
    try:
        with open(os.path.join(REPO, 'docs', 'FINDINGS.md'), encoding='utf-8') as f:
            text = f.read()
    except OSError:
        return titles
    for line in text.split('\n'):
        m = re.match(r'^\|\s*([FC]\d\d)\s*\|(.*)\|\s*$', line)
        if m:
            cells = [c.strip() for c in m.group(2).split('|')]
            titles[m.group(1)] = cells[1] if m.group(1)[0] == 'F' and len(cells) > 1 else cells[0]
    return titles


def citations(texts, item_id):
    """['path:line'] of comment lines citing an item number (F25, C21)."""
    pat = re.compile(r'(?<![A-Za-z0-9])' + re.escape(item_id) + r'(?!\d)')
    hits = []
    for path in sorted(texts):
        for n, raw in enumerate(lines_of(texts[path]), 1):
            if pat.search(raw[len(split_code(raw)):]):
                hits.append(f'{posixpath.basename(path)}:{n}')
    return hits


CHANGED_STATES = ('code changed', 'comments only', 'changed', 'added')


def audit_items(xlsx, status_of, paths, defs, base_texts, new_texts):
    """The items claimed fixed, each with the state of its modules in this backup."""
    try:
        sheets = read_xlsx(xlsx)
    except (OSError, zipfile.BadZipFile, KeyError, ET.ParseError, ValueError) as exc:
        return {'error': f'{xlsx}: cannot read the workbook ({exc})'}
    sheet, cols, rows = find_items_table(sheets)
    if sheet is None:
        return {'error': f'{xlsx}: no sheet with a header row holding ID and Estado'}
    titles = load_titles()

    def cell(row, key):
        i = cols.get(key)
        return str(row[i]).strip() if i is not None and i < len(row) and row[i] is not None else ''
    statuses, claimed, covered = Counter(), [], set()
    for row in rows:
        item = cell(row, 'id')
        if not item:
            continue
        statuses[cell(row, 'status') or '(empty)'] += 1
        if not is_claimed_fixed(cell(row, 'status')):
            continue
        date = cell(row, 'date')
        if re.fullmatch(r'\d{5}(\.0+)?', date) and 30000 < float(date) < 80000:
            # a date typed in Excel, read without openpyxl: days since 1899-12-30
            date = (datetime.date(1899, 12, 30) + datetime.timedelta(days=int(float(date)))).isoformat()
        date = re.sub(r' 00:00:00$', '', date)
        m = re.match(r'^([FC])0*(\d+)$', item.upper())
        key = f'{m.group(1)}{int(m.group(2)):02d}' if m else item

        def resolve(column):
            out = []
            for tok in item_tokens(cell(row, column)):
                found = match_module(tok, paths, defs)
                covered.update(found)
                out.append({'module': tok, 'files': [{'path': p, 'state': status_of(p)} for p in found]})
            return out
        modules, modified = resolve('modules'), resolve('modified')
        listed = [f for mod in modules + modified for f in mod['files']]
        changed = sorted({f['path'] for f in listed if f['state'] in CHANGED_STATES})
        code = sorted({f['path'] for f in listed if f['state'] in ('code changed', 'added')})
        stale = sorted({f['path'] for f in listed if f['state'] == 'PRE-CLEANUP FILE'})
        claimed_unchanged = [mod['module'] for mod in modified
                             if not any(f['state'] in CHANGED_STATES for f in mod['files'])]
        flag = None
        if not modules and not modified:
            flag = 'no modules listed - the fix cannot be traced to the backup'
        elif stale:
            flag = (f'{", ".join(posixpath.basename(p) for p in stale)} is the pre-cleanup file: '
                    f'the fix is not in this backup')
        elif not changed:
            flag = 'none of its modules changed in this backup'
        elif claimed_unchanged:
            flag = f'listed as modified by the programmer but unchanged: {", ".join(claimed_unchanged)}'
        entry = {'id': item, 'title': titles.get(key, cell(row, 'title')), 'status': cell(row, 'status'),
                 'note': cell(row, 'note'), 'criterion': cell(row, 'criterion'),
                 'evidence': cell(row, 'evidence'), 'date': date,
                 'modules': modules, 'modified': modified,
                 'changed_files': changed, 'code_changed_files': code, 'red_flag': flag}
        if re.match(r'^[FC]\d\d$', key):
            entry['cited_base'] = citations(base_texts, key)
            entry['cited_backup'] = citations(new_texts, key)
        claimed.append(entry)
    return {'workbook': xlsx, 'sheet': sheet, 'rows': sum(statuses.values()),
            'statuses': dict(statuses), 'claimed': claimed, 'covered': sorted(covered)}


# ------------------------------------------------------------------ report

def md_list(items, empty='none'):
    return '\n'.join(f'- {i}' for i in items) if items else f'_{empty}_'


def render(s, files):
    """AUDIT.md."""
    c = s['counts']
    am = s['backup']['am_ini']
    out = [f'# Backup audit - {os.path.basename(s["backup"]["zip"])}', '']
    out += [f'- Backup: `{s["backup"]["zip"]}` (sha256 `{s["backup"]["sha256"][:16]}...`)',
            f'- am.ini: archive `{am.get("name", "?")}`, date `{am.get("date", "?")}`, '
            f'config `{am.get("config", "?")}`, robot `{am.get("rob_name", "?")}`, '
            f'serial `{am.get("serial", "?")}`, KSS `{am.get("version", "?")}`',
            f'- Compared with: `{s["base"]["ref"]}` = `{s["base"]["commit"][:10]}` '
            f'"{s["base"]["subject"]}"; first commit (archive as received) `{s["first_commit"][:10]}`',
            f'- Generated {s["generated"]} by tools/audit_backup.py', '']

    out += ['## Summary', '', '| | |', '|---|---|']
    rows = [('Entries audited (Log Files/ skipped: %d)' % s['backup']['log_entries_skipped'],
             c['entries']), ('Unchanged', c['unchanged']), ('Changed', c['changed']),
            ('Added', c['added']), ('Missing from the backup', c['missing']),
            ('**Deleted modules still on the controller**', c['deleted_still_present']),
            ('**Pre-cleanup files**', c['pre_cleanup']),
            ('Edited on top of the pre-cleanup file', c['pre_cleanup_based']),
            ('KRL files with code changes', c['code_changed_files']),
            ('Code lines removed / added', f'{c["code_lines_removed"]} / {c["code_lines_added"]}'),
            ('KRL files with comment-only changes', c['comment_only_files']),
            ('KRL files with runtime values only (written by the program, not edits)',
             c.get('runtime_value_files', 0)),
            ('Checks FAIL / WARN / INFO', f'{c["FAIL"]} / {c["WARN"]} / {c["INFO"]}')]
    if 'items_claimed' in c:
        rows.append(('Items claimed fixed / red flags', f'{c["items_claimed"]} / {c["items_red_flags"]}'))
    out += [f'| {a} | {b} |' for a, b in rows] + ['']

    def few(paths):
        return ': ' + ', '.join(f'`{p}`' for p in paths) if len(paths) <= 3 else ' (listed below)'
    grouped = {d['path'] for d in s['deleted_still_present']} | set(s['pre_cleanup']) | \
        set(s['pre_cleanup_based'])
    attention = [f'**FAIL** {msg}' for lvl, msg in s['alerts']
                 if lvl == 'FAIL' and msg.split(':')[0] not in grouped]
    if s['deleted_still_present']:
        attention.append(f'**{len(s["deleted_still_present"])} module(s) deleted in the cleanup still on the '
                         f'controller**' + few([d['path'] for d in s['deleted_still_present']]))
    if s['pre_cleanup']:
        attention.append(f'**{len(s["pre_cleanup"])} PRE-CLEANUP file(s)**: the cleaned program was not '
                         f'loaded or was overwritten' + few(s['pre_cleanup']))
    if s['pre_cleanup_based']:
        attention.append(f'**{len(s["pre_cleanup_based"])} file(s) edited on top of the pre-cleanup '
                         f'version**' + few(s['pre_cleanup_based']))
    attention += [f'WARN {msg}' for lvl, msg in s['alerts'] if lvl == 'WARN']
    if c['FAIL']:
        attention.append(f'**{c["FAIL"]} FAIL** in the mechanical checks')
    if c['WARN']:
        attention.append(f'{c["WARN"]} WARN in the mechanical checks')
    if c.get('items_red_flags'):
        attention.append(f'**{c["items_red_flags"]} item(s)** claimed fixed with a red flag (last section)')
    if attention or c['changed'] or c['added'] or c['unexpected'] or s['case_differences']:
        verdict = md_list(attention, 'nothing beyond the changes listed below')
    else:
        verdict = '_nothing: the backup is identical to the base_'
    out += ['**Needs attention:**', '', verdict, '']

    out += ['## The backup itself', '',
            md_list([f'{lvl}: {msg}' for lvl, msg in s['alerts']], 'no remarks'), '']

    out += ['## Deleted modules still present', '']
    if s['deleted_still_present']:
        out += ['The cleanup deleted these modules. A restore does not delete files, so they are still on '
                'the controller: delete them there (navigator, expert mode).', '']
    out += [md_list([f'`{d["path"]}` - {d["state"]}' for d in s['deleted_still_present']]), '']

    out += ['## Pre-cleanup files', '']
    if s['pre_cleanup']:
        out += ['**These files are byte-for-byte the archive as received: the cleaned program was not '
                'loaded or was overwritten. Every comment correction, header and junk removal of the '
                'cleanup is lost in them.**', '']
    out += [md_list([f'`{p}`' for p in s['pre_cleanup']])]
    if s['pre_cleanup_based']:
        out += ['', 'Edited on top of the pre-cleanup file (its comments are closer to the archive as '
                'received than to the base):', '', md_list([f'`{p}`' for p in s['pre_cleanup_based']])]
    out += ['']

    out += ['## Files', '']
    for label, key in (('Changed', 'changed'), ('Added', 'added'), ('Missing from the backup', 'missing'),
                       ('Outside the archive layout (ignored)', 'unexpected')):
        lst = s[key]
        out += [f'### {label} ({len(lst)})', '']
        if key in ('changed', 'added'):
            out += [md_list([f'`{p}` - {files[p]["area"]}'
                             + (f' - {files[p]["note"]}' if files[p].get('note') else '') for p in lst])]
        else:
            shown = lst[:50]
            out += [md_list([f'`{p}`' for p in shown])]
            if len(lst) > 50:
                out += [f'- ... and {len(lst) - 50} more (summary.json)']
        out += ['']

    out += ['## Code changes', '']
    code_files = [p for p in s['changed'] + s['added']
                  if files[p].get('code_removed') or files[p].get('code_added')]
    if not code_files:
        out += ['_No executable code changed._', '']
    for p in sorted(code_files, key=lambda p: (files[p]['area'] != 'integrator program', p)):
        f = files[p]
        out += [f'### `{p}`', '',
                f'{f["status"]}, {f["area"]}: {f["code_removed"]} code line(s) removed, '
                f'{f["code_added"]} added; {f["comment_only_changes"]} comment/blank line change(s). '
                f'Full diff: [{f["diff"]}]({f["diff"].replace(" ", "%20")})', '']
        if f['attributes']:
            out += [f'Attributes: {"; ".join(f["attributes"])}', '']
        if f['data_changes']:
            out += ['Data changes:', '', md_list(f['data_changes'][:40])]
            if len(f['data_changes']) > 40:
                out += [f'- ... and {len(f["data_changes"]) - 40} more']
            out += ['']
        if f.get('runtime_values'):
            out += [f'Runtime values (left out of the code diff): {runtime_summary(f["runtime_values"])}', '']
        diff = [clip(line) for line in f['code_diff']]
        out += ['```diff'] + diff[:INLINE_DIFF_LINES] + ['```']
        if len(diff) > INLINE_DIFF_LINES:
            out += [f'_{len(diff) - INLINE_DIFF_LINES} more lines: see {f["diff"]}_']
        out += ['']
    runtime = [p for p in s.get('runtime_value_files', []) if p not in code_files]
    comment_only = [p for p in s['changed'] + s['added'] if is_krl(p) and p not in code_files
                    and p not in runtime]
    if runtime:
        out += ['### Runtime values only', '',
                'A .dat keeps the last value the program wrote to each of its variables, and the inline-form '
                'editor keeps its suggestions (LAST_BASIS...): these files changed only in such values, '
                'nobody edited them.', '', '| File | Values | Diff |', '|---|---|---|']
        out += [f'| `{p}` | {runtime_summary(files[p]["runtime_values"])} | {files[p]["diff"]} |'
                for p in runtime] + ['']
    if comment_only:
        out += ['### Comment-only changes', '', '| File | Comment/blank line changes | Attributes | Diff |',
                '|---|---|---|---|']
        out += [f'| `{p}` | {files[p].get("comment_only_changes", "?")} | '
                f'{"; ".join(files[p].get("attributes", [])) or "-"} | '
                f'{files[p].get("diff") or files[p].get("note", "-")} |' for p in comment_only] + ['']

    out += ['## Mechanical checks', '']
    if s['signal_changes']:
        out += ['Signal declarations changed (names lower-cased):', '',
                md_list([describe_signal_change(r) for r in s['signal_changes']]), '']
    for lvl in LEVELS:
        found = [f for f in s['findings'] if f['level'] == lvl]
        out += [f'### {lvl} ({len(found)})', '']
        out += [md_list([f'`{f["file"]}{":" + str(f["line"]) if f["line"] else ""}` '
                         f'[{f["check"]} {f["name"]}] {f["message"]}' for f in found])]
        out += ['']

    if 'items' in s:
        out += render_items(s['items'], s)
    return '\n'.join(out).rstrip() + '\n'


def clip(line, width=240):
    """A code-diff line for AUDIT.md: a .dat declaration can run to 1000
    characters (the full line is in the .diff file)."""
    return line if len(line) <= width else line[:width] + ' [...]'


def runtime_summary(values, limit=6):
    shown = '; '.join(values[:limit]).replace('|', '\\|')
    return shown + (f'; ... and {len(values) - limit} more' if len(values) > limit else '')


def md_field(label, text):
    """A bullet for a workbook cell; a multi-line cell becomes sub-bullets."""
    lines = [l.strip().lstrip('•-* ').strip() for l in str(text or '').splitlines() if l.strip()]
    if not lines:
        return []
    if len(lines) == 1:
        return [f'- {label}: {lines[0]}']
    return [f'- {label}:'] + [f'  - {l}' for l in lines]


def describe_modules(modules):
    out = []
    for m in modules:
        if not m['files']:
            out.append(f'{m["module"]} (not found in the backup or the base)')
        else:
            names = Counter(posixpath.basename(f['path']).lower() for f in m['files'])
            out.append(f'{m["module"]} (' + ', '.join(
                f'{f["path"] if names[posixpath.basename(f["path"]).lower()] > 1 else posixpath.basename(f["path"])}'
                f': {f["state"]}' for f in m['files']) + ')')
    return '; '.join(out) or '_none listed_'


def render_items(items, s):
    out = ['## Items claimed fixed', '']
    if 'error' in items:
        return out + [f'**{items["error"]}**', '']
    out += [f'Workbook `{items["workbook"]}`, sheet "{items["sheet"]}": {items["rows"]} items '
            f'(' + ', '.join(f'{k}: {v}' for k, v in sorted(items['statuses'].items())) + ').', '']
    if not items['claimed']:
        out += ['_No item is marked "Corregido - por auditar"._', '']
    for it in items['claimed']:
        flag = f' - **RED FLAG: {it["red_flag"]}**' if it['red_flag'] else ''
        out += [f'### {it["id"]}{" - " + it["title"] if it["title"] else ""}{flag}', '']
        out += md_field('Programmer', it['note'] or '_(no note)_')
        out += [f'- Modules of the item: {describe_modules(it["modules"])}']
        if it['modified']:
            out += [f'- Modules the programmer modified: {describe_modules(it["modified"])}']
        if it['changed_files'] and not it['code_changed_files']:
            out += ['- Only comments changed in its modules: no executable change backs the fix']
        if 'cited_base' in it:
            where = ', '.join(it['cited_backup'][:8]) + (' ...' if len(it['cited_backup']) > 8 else '')
            out += [f'- Comments citing {it["id"]}: {len(it["cited_base"])} in the base, '
                    f'{len(it["cited_backup"])} in the backup' + (f' ({where})' if where else '')]
        out += md_field('Evidence', it['evidence'] + (f' ({it["date"]})' if it.get('date') else ''))
        out += md_field('Closure criterion', it['criterion'])
        out += ['']
    unclaimed = [p for p in s['changed'] + s['added']
                 if is_krl(p) and p not in items['covered'] and s['files'][p].get('code_added', 0)
                 + s['files'][p].get('code_removed', 0)]
    out += ['Code changes that no item claimed fixed lists among its modules:', '',
            md_list([f'`{p}`' for p in unclaimed]), '']
    return out


# -------------------------------------------------------------------- run

def backup_alerts(am, cls):
    """Remarks on the backup as a whole: which robot, how complete."""
    alerts = []
    if not am:
        alerts.append(('FAIL', 'am.ini missing or unreadable: not a complete KUKA archive'))
    elif am.get('serial') != SERIAL:
        alerts.append(('FAIL', f'am.ini IRSerialNr {am.get("serial")!r} (RobName {am.get("rob_name")!r}): '
                               f'expected {SERIAL} - this backup is from ANOTHER ROBOT'))
    if am and am.get('config', '').lower() not in ('all', ''):
        alerts.append(('WARN', f'am.ini Config={am["config"]}: partial archive, missing files are expected'))
    for line in case_differences(cls['case']):
        alerts.append(('INFO', line))
    for first, second in cls['duplicates']:
        alerts.append(('WARN', f'{first} and {second} are both in the zip and are the same file on the '
                               f'controller (names differ only in case); {second} is audited'))
    if cls['unexpected']:
        alerts.append(('WARN', f'{len(cls["unexpected"])} entries outside the KUKA archive layout ignored '
                               f'(e.g. {cls["unexpected"][0]})'))
    if cls['missing']:
        alerts.append(('WARN', f'{len(cls["missing"])} file(s) of the base missing from the backup - deleted '
                               f'on the robot, or an incomplete archive (e.g. {cls["missing"][0]}; all in '
                               f'Files, "Missing from the backup")'))
    return alerts


def case_differences(pairs):
    """One line per folder spelled differently in the backup (all its files
    follow), one per file otherwise."""
    folders, lines = {}, []
    for name, path in pairs:
        zd, zb = posixpath.split(name)
        bd, bb = posixpath.split(path)
        if zb == bb and zd != bd:
            folders.setdefault((zd, bd), []).append(name)
        else:
            lines.append(f'{name}: spelled {path} in the base (the controller ignores case)')
    for (zd, bd), names in sorted(folders.items()):
        lines.append(f'{zd}/: spelled {bd}/ in the base, {len(names)} file(s) (the controller ignores case)')
    return lines


def vendor_alerts(cls, info):
    """C28: an edit to a KUKA system or tech-package file, or to machine data.
    A .dat whose only change is runtime values written by the program is not
    an edit."""
    alerts = []
    for p in cls['changed'] + cls['added']:
        a = area(p)
        if a not in ('KUKA system / vendor package', 'machine data'):
            continue
        f = info.get(p, {})
        if is_krl(p) and f.get('status') == 'changed' and not (
                f.get('code_removed') or f.get('code_added') or f.get('comment_only_changes')):
            continue        # runtime values (and controller attributes) only
        level = 'INFO' if a != 'machine data' and p.lower().endswith('.dat') else 'WARN'
        alerts.append((level, f'{p}: {a} file changed - if intended, list the edit in the hand-over '
                              f'so a package update does not drop it (C28)'))
    return alerts


def missing_alerts(cls, ctx):
    """A KRL file of the base missing from the backup whose routines or data
    the backup still uses: the program does not compile or a call fails.
    (A restore does not delete files: if the robot really lost the file, the
    controller holds the old copy until someone deletes it there.)"""
    alerts = []
    if not any(is_krl(p) for p in cls['missing']):
        return alerts
    lives = {p: live(t) for p, t in ctx['texts'].items()}
    defined = {d.lower() for t in ctx['texts'].values() for d in def_names(t)}
    for p in cls['missing']:
        if not is_krl(p) or p not in ctx['base_texts']:
            continue
        old = ctx['base_texts'][p]
        if p.lower().endswith('.dat'):
            names, glob = declared_in(old)
            src = twin(p, ctx['texts'])
            uses = []
            for low, name in sorted(names.items()):
                for user in (sorted(lives) if low in glob or p.lower().endswith('$config.dat')
                             else [src] if src else []):
                    if user != p and word_in(name, lives[user]):
                        uses.append(f'{name} in {user}')
                        break
            if uses:
                alerts.append(('FAIL', f'{p} is missing from the backup but its data is still used '
                                       f'({", ".join(uses[:5])}{" ..." if len(uses) > 5 else ""}): the '
                                       f'program does not compile without it'))
            continue
        for name in def_names(old):
            if name.lower() in defined:
                continue
            users = [u for u in sorted(lives) if word_in(name, lives[u])]
            if users:
                alerts.append(('FAIL', f'{p} is missing from the backup but {name} is still called in '
                                       f'{", ".join(users[:3])}{" ..." if len(users) > 3 else ""}'))
    return alerts


def comment_lines(raw):
    return [t for t in (comment_text(l) for l in lines_of(raw.decode('latin-1'))) if t]


def cleanup_alerts(cls, files, base, first_tree, blobs):
    """Is the cleaned program what runs on the robot? Deleted modules still
    present, files equal to (or edited from) the archive as received."""
    alerts, deleted, pre_cleanup, pre_based = [], [], [], []
    for p in cls['deleted_present']:
        same = first_tree.get(p) == blob_id(files[p])
        deleted.append({'path': p, 'state': 'identical to the archive as received' if same
                        else 'MODIFIED since the archive as received'})
        alerts.append(('FAIL', f'{p}: module deleted in the cleanup is still on the controller - '
                               f'delete it there'))
    for p in cls['changed']:
        if not is_krl(p) or p not in first_tree:
            continue
        if first_tree[p] == blob_id(files[p]):
            pre_cleanup.append(p)
            alerts.append(('FAIL', f'{p}: this is the pre-cleanup file: the cleaned program was not '
                                   f'loaded or was overwritten'))
        elif first_tree[p] != base[p]:
            new = comment_lines(files[p])
            r_first = difflib.SequenceMatcher(None, comment_lines(blobs[first_tree[p]]), new,
                                              autojunk=False).ratio()
            r_base = difflib.SequenceMatcher(None, comment_lines(blobs[base[p]]), new, autojunk=False).ratio()
            if r_first > r_base:
                pre_based.append(p)
                alerts.append(('FAIL', f'{p}: edited on top of the pre-cleanup file (comments match the '
                                       f'archive as received {r_first:.0%}, the base {r_base:.0%})'))
    return alerts, deleted, pre_cleanup, pre_based


def make_context(cls, files, base, blobs, out_dir, base_label):
    """What the checks need to know about the whole program: every KRL text
    of the backup and of the base, the signal declarations of both, the
    global data names."""
    live_paths = [p for p in files if is_krl(p) and p not in cls['deleted_present']]
    new_texts = {p: files[p].decode('latin-1') for p in live_paths}
    base_texts = {p: (blobs[base[p]] if p in cls['changed'] or p in cls['missing'] else files[p])
                  .decode('latin-1') for p in base if is_krl(p) and (p in files or p in cls['missing'])}
    new_sig = declared_signals(new_texts)
    sig_rows = signal_changes(declared_signals(base_texts), new_sig)
    signal_keys = {}
    for key, names in new_sig.items():
        for n in names:
            signal_keys.setdefault(n, set()).add(key)
    global_decls = set()
    for p, t in new_texts.items():
        if p.lower().endswith('.dat'):
            names, glob = declared_in(t)
            global_decls |= set(names) if p.lower().endswith('$config.dat') else glob
    return {'out': out_dir, 'base_label': base_label, 'texts': new_texts, 'base_texts': base_texts,
            'signals': new_sig, 'signal_names': set(signal_keys), 'signal_keys': signal_keys,
            'signal_rows': sig_rows, 'global_decls': global_decls,
            'sig_changed_keys': {(r['io'], i) for r in sig_rows for i in range(r['first'], r['last'] + 1)},
            'sig_changed_names': {n for r in sig_rows for n in set(r['base']) ^ set(r['new'])}}


def analyse_files(cls, files, base, blobs, pre_cleanup, ctx, started_from=None):
    """Describe and check every changed or added file: (Audit, {path: info}).
    `started_from`: {path: bytes} of the files edited on top of the pre-cleanup
    version, that version."""
    audit, info = Audit(), {}
    for p in cls['changed'] + cls['added']:
        info[p] = {'area': area(p), 'status': 'changed' if p in cls['changed'] else 'added'}
        old = blobs[base[p]] if p in cls['changed'] else None
        if is_krl(p):
            # A pre-cleanup file brings back every old comment: its checks would
            # only bury the one finding that matters, raised by cleanup_alerts().
            try:
                info[p].update(analyse_krl(Audit() if p in pre_cleanup else audit, p, old, files[p], ctx,
                                           (started_from or {}).get(p)))
            except Exception as exc:     # one odd file must not cost the auditor the whole report
                info[p]['diff'] = write_diff(ctx['out'], p, old.decode('latin-1') if old is not None else None,
                                             files[p].decode('latin-1'), ctx['base_label'])
                info[p]['note'] = 'NOT ANALYSED'
                audit.add('FAIL', 0, p, None, f'the audit could not analyse this file ({exc!r}): '
                          f'review {info[p]["diff"]} by hand')
                continue
            if p in pre_cleanup:
                info[p]['note'] = 'PRE-CLEANUP FILE (mechanical checks skipped)'
        elif is_text(files[p]):
            old_text = old.decode('latin-1') if old is not None else None
            new_text = files[p].decode('latin-1')
            info[p]['diff'] = write_diff(ctx['out'], p, old_text, new_text, ctx['base_label'])
            r, a, _ = line_diff(lines_of(old_text) if old_text is not None else [], lines_of(new_text))
            info[p]['note'] = f'{r} line(s) removed, {a} added - {info[p]["diff"]}'
        else:
            info[p]['note'] = f'binary, {len(files[p])} bytes'
    if ctx['signal_rows']:       # check 3 on unchanged files whose declarations changed
        for p in sorted(set(ctx['texts']) - set(info)):
            for n, msg in signal_comment_problems(lines_of(ctx['texts'][p]), ctx, lambda n: False):
                audit.add('FAIL', 3, p, n, msg + ' (its declaration changed in this backup)')
    audit.findings.sort(key=lambda f: (LEVELS.index(f['level']), f['file'], f['line'] or 0))
    return audit, info


def file_state(p, cls, pre_cleanup, code_files, runtime_files=()):
    """How a file fared in this backup, in words, for the items section."""
    if p in cls['deleted_present']:
        return 'deleted module still present'
    if p in cls['missing']:
        return 'missing from the backup'
    if p in cls['added']:
        return 'added'
    if p in pre_cleanup:
        return 'PRE-CLEANUP FILE'
    if p in cls['changed']:
        if not is_krl(p):
            return 'changed'
        if p in code_files:
            return 'code changed'
        return 'runtime values only' if p in runtime_files else 'comments only'
    return 'unchanged'


def count(entries, cls, cleanup, info, audit):
    _, deleted, pre_cleanup, pre_based = cleanup
    code_files = [p for p in info if info[p].get('code_removed') or info[p].get('code_added')]
    runtime_files = runtime_only(info, code_files)
    counts = {'entries': len(entries), 'unchanged': len(cls['unchanged']), 'changed': len(cls['changed']),
              'added': len(cls['added']), 'missing': len(cls['missing']),
              'unexpected': len(cls['unexpected']), 'deleted_still_present': len(deleted),
              'pre_cleanup': len(pre_cleanup), 'pre_cleanup_based': len(pre_based),
              'code_changed_files': len(code_files),
              'code_lines_removed': sum(info[p].get('code_removed', 0) for p in info),
              'code_lines_added': sum(info[p].get('code_added', 0) for p in info),
              'comment_only_files': sum(1 for p in info if is_krl(p) and p not in code_files
                                        and p not in runtime_files),
              'runtime_value_files': len(runtime_files)}
    counts.update({lvl: sum(f['level'] == lvl for f in audit.findings) for lvl in LEVELS})
    return counts, code_files, runtime_files


def runtime_only(info, code_files):
    """KRL files whose only change is values the program wrote at run time
    (or the editor's suggestion data): no code, no comment, edited by nobody."""
    return [p for p in info if p not in code_files and info[p].get('runtime_values')
            and not info[p].get('comment_only_changes')]


def print_summary(s, out_dir):
    c, am = s['counts'], s['backup']['am_ini']
    print(f'{s["backup"]["zip"]}: {c["entries"]} entries vs {s["base"]["ref"]} ({s["base"]["commit"][:10]}): '
          f'{c["unchanged"]} unchanged, {c["changed"]} changed, {c["added"]} added, {c["missing"]} missing')
    print(f'serial {am.get("serial", "?")}, archive date {am.get("date", "?")}; '
          f'{c["code_changed_files"]} KRL files with code changes '
          f'(-{c["code_lines_removed"]}/+{c["code_lines_added"]} lines); '
          f'checks: {c["FAIL"]} FAIL, {c["WARN"]} WARN, {c["INFO"]} INFO')
    fails = [msg for lvl, msg in s['alerts'] if lvl == 'FAIL']
    for msg in fails[:10]:
        print(f'FAIL  {msg}')
    if len(fails) > 10:
        print(f'FAIL  ... and {len(fails) - 10} more (AUDIT.md, "The backup itself")')
    if 'items_claimed' in c:
        print(f'items claimed fixed: {c["items_claimed"]}, red flags: {c["items_red_flags"]}')
    print(f'report: {os.path.join(out_dir, "AUDIT.md")}')


def write_outputs(out_dir, summary, info):
    with open(os.path.join(out_dir, 'AUDIT.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(render(summary, info))
    with open(os.path.join(out_dir, 'summary.json'), 'w', encoding='utf-8', newline='\n') as f:
        json.dump(summary, f, indent=1, ensure_ascii=False)
        f.write('\n')


def import_entries(root, files, names, base_blobs):
    """Write `names` from `files` under `root`, byte-for-byte. Never deletes."""
    written = []
    root = os.path.abspath(root)
    for name in names:
        dest = os.path.abspath(os.path.join(root, *name.split('/')))
        if not dest.startswith(root + os.sep):
            print(f'  refused   {name} (outside the working tree)')
            continue
        note = ''
        if os.path.isfile(dest):
            with open(dest, 'rb') as f:
                cur = blob_id(f.read())
            if name in base_blobs and cur != base_blobs[name] and cur != blob_id(files[name]):
                note = '  (OVERWROTE an uncommitted local change)'
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, 'wb') as f:
            f.write(files[name])
        written.append(name)
        print(f'  wrote     {name}{note}')
    return written


def run_import(cls, files, base, pre_cleanup, pre_based=(), root=None):
    """--import: the changed and added entries into the working tree. The
    deleted modules still present and the entries outside the archive
    layout are not among them (classify() keeps them apart). A pre-cleanup
    file is not imported either: its bytes are the first commit, so it adds
    nothing, and importing it would undo the cleanup for whoever commits."""
    names = [p for p in cls['changed'] + cls['added'] if p not in pre_cleanup]
    root = root or REPO
    print(f'\nimporting {len(names)} changed/added entries into {root}:')
    written = import_entries(root, files, names, base)
    if pre_cleanup:
        print('not imported (PRE-CLEANUP files, byte-for-byte the archive as received - the cleaned '
              'version must be loaded on the robot again):')
        for p in pre_cleanup:
            print(f'  {p}')
    if pre_based:
        print('WARNING: imported files edited on top of the pre-cleanup version - their diff undoes the '
              'cleanup comments; merge the code change into the cleaned file by hand before committing:')
        for p in pre_based:
            print(f'  {p}')
    if cls['missing']:
        more = ' ...' if len(cls['missing']) > 10 else ''
        print(f'not deleted ({len(cls["missing"])} files missing from the backup - delete by hand if '
              f'that is intended): {", ".join(cls["missing"][:10])}{more}')
    if cls['deleted_present']:
        print('not imported (deleted in the cleanup, still on the controller): '
              + ', '.join(cls['deleted_present']))
    print('review with git status / git diff before committing')
    return written


def deleted_modules(base=None):
    """The 'deleted_files' of the cleanup allowlist and of the code-change
    phase (tools/code_changes.json). A code-change deletion counts only when
    the audit base no longer holds the file: auditing against an older base
    (e.g. the cleanup commit) treats it as an ordinary file. check_cleanup
    reads its allowlist relative to the current directory: read it from the
    repository and give the caller its directory back."""
    cwd = os.getcwd()
    try:
        os.chdir(REPO)
        deleted = dict(load_allowlist()[0]['deleted_files'])
        if os.path.exists('tools/code_changes.json'):
            with open('tools/code_changes.json') as f:
                later = json.load(f).get('deleted_files', {})
            deleted.update({p: why for p, why in later.items() if base is None or p not in base})
        return deleted
    finally:
        os.chdir(cwd)


def parse_args(argv):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('backup', help='the KUKA archive zip sent by the programmer')
    ap.add_argument('--base', default='HEAD', help='git ref of the last audited state (default HEAD)')
    ap.add_argument('--items', help="the programmer's open-items workbook (.xlsx)")
    ap.add_argument('--out', help='output directory (default audits/<am.ini date>/)')
    ap.add_argument('--import', dest='do_import', action='store_true',
                    help='copy the changed and added entries into the working tree')
    return ap.parse_args(argv)


def prepare_out_dir(out_dir, am):
    stamp = re.sub(r'[^\w.-]+', '_', am.get('date') or datetime.date.today().isoformat())
    out_dir = out_dir or os.path.join(REPO, 'audits', stamp)
    os.makedirs(out_dir, exist_ok=True)
    for dirpath, _, names in os.walk(os.path.join(out_dir, 'diffs')):    # stale diffs of an earlier run
        for n in names:
            if n.endswith('.diff'):
                os.remove(os.path.join(dirpath, n))
    return out_dir


def main(argv=None, import_root=None):
    """Audit one backup; returns the summary (also written to summary.json).
    `import_root`: where --import writes (default the repository; tests)."""
    args = parse_args(argv)
    zip_path = os.path.abspath(args.backup)
    out_dir = os.path.abspath(args.out) if args.out else None
    items_path = os.path.abspath(args.items) if args.items else None

    try:
        entries, log_count, read_notes = read_backup(zip_path)
        with open(zip_path, 'rb') as f:
            zip_sha = hashlib.sha256(f.read()).hexdigest()
    except (OSError, zipfile.BadZipFile) as exc:
        print(f'cannot read {zip_path}: {exc}', file=sys.stderr)
        sys.exit(2)
    try:
        base_commit = git('rev-parse', '--verify', args.base + '^{commit}').decode().strip()
    except subprocess.CalledProcessError:
        print(f'unknown git ref: {args.base}', file=sys.stderr)
        sys.exit(2)
    first = first_commit()
    base = {p: b for p, b in tree_blobs(base_commit).items() if is_archive_path(p)}
    first_tree = tree_blobs(first)
    files, cls = classify(entries, base, deleted_modules(base))
    am_path = next((p for p in files if p.lower() == 'am.ini'), None)
    am = read_am_ini(files[am_path]) if am_path else {}
    out_dir = prepare_out_dir(out_dir, am)

    # From git: the base version of every changed file and missing KRL file,
    # the first-commit version of changed KRL files and deleted modules present.
    blobs = read_blobs([base[p] for p in cls['changed']] +
                       [base[p] for p in cls['missing'] if is_krl(p)] +
                       [first_tree[p] for p in cls['changed'] + cls['deleted_present'] if p in first_tree])
    cleanup = cleanup_alerts(cls, files, base, first_tree, blobs)
    ctx = make_context(cls, files, base, blobs, out_dir, args.base)
    audit, info = analyse_files(cls, files, base, blobs, cleanup[2], ctx,
                                {p: blobs[first_tree[p]] for p in cleanup[3]})
    alerts = list(read_notes) + backup_alerts(am, cls) + cleanup[0] + missing_alerts(cls, ctx) + \
        vendor_alerts(cls, info)
    alerts.sort(key=lambda a: LEVELS.index(a[0]))
    counts, code_files, runtime_files = count(entries, cls, cleanup, info, audit)

    summary = {
        'tool': 'tools/audit_backup.py',
        'generated': datetime.datetime.now().isoformat(timespec='seconds'),
        'backup': {'zip': zip_path, 'sha256': zip_sha, 'log_entries_skipped': log_count,
                   'am_ini': am, 'serial_ok': am.get('serial') == SERIAL},
        'base': {'ref': args.base, 'commit': base_commit,
                 'subject': git('log', '-1', '--format=%s', base_commit).decode().strip()},
        'first_commit': first, 'counts': counts, 'alerts': alerts,
        'changed': cls['changed'], 'added': cls['added'], 'missing': cls['missing'],
        'unexpected': cls['unexpected'], 'case_differences': cls['case'],
        'duplicate_entries': cls['duplicates'], 'runtime_value_files': runtime_files,
        'deleted_still_present': cleanup[1], 'pre_cleanup': cleanup[2], 'pre_cleanup_based': cleanup[3],
        'files': {p: {k: v for k, v in d.items() if k != 'code_diff'} for p, d in info.items()},
        'signal_changes': ctx['signal_rows'], 'findings': audit.findings,
    }
    if items_path:
        defs = {}
        for texts in (ctx['base_texts'], ctx['texts']):
            for p, t in texts.items():
                for d in def_names(t):
                    defs.setdefault(d.lower(), p)
        summary['items'] = audit_items(items_path,
                                       lambda p: file_state(p, cls, cleanup[2], code_files, runtime_files),
                                       sorted(set(files) | set(base)), defs, ctx['base_texts'], ctx['texts'])
        claimed = summary['items'].get('claimed', [])
        counts['items_claimed'] = len(claimed)
        counts['items_red_flags'] = sum(1 for it in claimed if it['red_flag'])

    write_outputs(out_dir, summary, info)
    print_summary(summary, out_dir)
    if args.do_import:
        summary['imported'] = run_import(cls, files, base, cleanup[2], cleanup[3], import_root)
        write_outputs(out_dir, summary, info)
    return summary


if __name__ == '__main__':
    main()
    sys.exit(0)
