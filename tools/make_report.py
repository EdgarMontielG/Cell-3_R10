#!/usr/bin/env python3
"""Build the PDF reports of the R10 audit and of the open items.

    python3 tools/make_report.py [--scope gestamp|mejoras|both] [--out FILE.pdf]

Two reports since 2026-10-12 (tools/scope.py): the Gestamp points G01-G22 for
the buy-off (R10_Gestamp_reporte_<YYYY-MM-DD_HHMM>.pdf) and the Ethos items as
process improvements (R10_Mejoras_reporte_<...>.pdf). By default it writes
both to dist/ (date and time of central Mexico, tools/naming.py) and removes
the older copies there (and the single report of before).

Content, in Spanish for the owner, with code quoted as it is (English):
  Gestamp: 1. summary and what is left for the buy off, 1.1 what the last
  audit changed in those points, 2. the 22 points, 3. detail (a criterion
  "se cumplen los criterios de F43" carries F43's), 4. the daily process.
  Mejoras: 1. summary, 1.1 last audit (audits/*/resumen.json), 2. the office
  version as reference, 3. the daily process and the audits, 4. items summary
  (column Gestamp: the open point each counts for) and 5. detail, annex A:
  every ;CHECK: and ;WARNING: comment in the programs.
The sections of the office-version stage (what the cleanup did, annex B
with the shaded listing) are kept below but no longer built.

Re-run it after each audit: the open-item status comes from
docs/open_items.json, the rest from the repository itself.
Needs reportlab (pip install reportlab).
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (KeepTogether, PageBreak, Paragraph, SimpleDocTemplate,
                                Spacer, Table, TableStyle)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, 'tools'))
import scope as scopes  # noqa: E402

BASE = '22a98cc'
OFFICE = 'Corregido en oficina - probar en celda'
DELETED_ES = {
    'centerline_weld1.src': 'Primera versión de la soldadura; usaba el bloque Bosch Unit 1 de AutomationCore, que no está mapeado.',
    'trigger1.src': 'Primer paso de la precarga de tuerca antigua (hoy PRELOAD); nada lo llama (Calvin #31, Gestamp 5).',
    'trigger1.dat': 'Datos de trigger1, sin datos globales.',
    'trigger2.src': 'Segundo paso de la precarga antigua (hoy PRELOAD); nada lo llama (Calvin #31, Gestamp 5).',
    'trigger2.dat': 'Datos de trigger2, sin datos globales.',
    'trigger3.src': 'Tercer paso de la precarga antigua (hoy PRELOAD); nada lo llama (Calvin #31, Gestamp 5).',
    'trigger3.dat': 'Datos de trigger3, sin datos globales.',
    'ck1stxxx.src': 'Plantilla de revisión de tuerca de otra línea ("Line - Volvo", "Robot XXXXX"); nada la llama (Gestamp 5).',
    'ck1stxxx.dat': 'Datos de CK1STXXX, sin datos globales.',
    'pounce.src': 'Plantilla de otra línea ("Robot XXXXX"); el pounce de AutomationCore es XPOUNCE global.',
    'pounce.dat': 'Datos de POUNCE, sin datos globales.',
    'capchange.src': 'Cambiador de caps de la pistola servo de una aplicación anterior; nada lo llama y no enlazaba.',
    'capchange.dat': 'Datos de capchange, solo locales.',
    'electrodechange.src': 'Cambio de electrodo viejo, reemplazado por GunElectrodeChange (el que llama cell.src); no enlazaba.',
    'electrodechange.dat': 'Datos de electrodechange, sin datos globales.',
    'redrabbit.src': 'Red rabbit de una celda de birlos (TOOL 2, grippers 2-4, sensores di777..782); bloqueado con WAIT FOR FALSE '
                     'después del INI; nada lo llama; no enlazaba (Gestamp 4).',
    'redrabbit.dat': 'Datos de redrabbit, sin datos globales.',
    'style1app2opt1autorr.src': 'Copia red rabbit de la revisión de tuerca; nada la llama: Style1Opt10AutoRR llama la de producción (Gestamp 5, 8).',
    'style1app2opt1autorr.dat': 'Datos de style1app2opt1AutoRR, solo puntos locales.',
    'style1app2opt2autorr.src': 'Copia red rabbit de la revisión de cámara; nada la llama (Gestamp 5, 8).',
    'style1app2opt2autorr.dat': 'Datos de style1app2opt2AutoRR, solo puntos locales.',
    'centerline_loop.src': 'Lazo de prueba manual de las válvulas del pedestal, sin salida ni interlocks; nada lo llama (G05).',
}
FONT_DIR = '/usr/share/fonts/truetype/dejavu'

INK = colors.HexColor('#1f2933')
MUTED = colors.HexColor('#616e7c')
ACCENT = colors.HexColor('#1d4e89')
RULE = colors.HexColor('#cbd2d9')
HEAD_BG = colors.HexColor('#e4e7eb')
NEW_BG = colors.HexColor('#fff4c2')
CODE_BG = colors.HexColor('#dcebfa')
CRIT_BG = colors.HexColor('#f8c9c5')
DONE_BG = colors.HexColor('#c6efce')
CRIT = colors.HexColor('#b42318')
SEV = {'Crítico': colors.HexColor('#b42318'), 'Alto': colors.HexColor('#c4561d'),
       'Medio': colors.HexColor('#a16207'), 'Bajo': colors.HexColor('#52606d'),
       '-': colors.HexColor('#9aa5b1')}


def git(*args):
    return subprocess.run(('git',) + args, cwd=REPO, check=True,
                          capture_output=True).stdout


def fonts():
    pdfmetrics.registerFont(TTFont('Sans', f'{FONT_DIR}/DejaVuSans.ttf'))
    pdfmetrics.registerFont(TTFont('Sans-Bold', f'{FONT_DIR}/DejaVuSans-Bold.ttf'))
    pdfmetrics.registerFont(TTFont('Mono', f'{FONT_DIR}/DejaVuSansMono.ttf'))
    from reportlab.lib.fonts import addMapping
    addMapping('Sans', 0, 0, 'Sans')
    addMapping('Sans', 1, 0, 'Sans-Bold')


def styles():
    base = dict(fontName='Sans', textColor=INK, leading=13, fontSize=9.5, alignment=TA_LEFT)
    return {
        'title': ParagraphStyle('title', **{**base, 'fontName': 'Sans-Bold', 'fontSize': 20,
                                            'leading': 24, 'textColor': ACCENT}),
        'subtitle': ParagraphStyle('subtitle', **{**base, 'fontSize': 11, 'leading': 15,
                                                  'textColor': MUTED}),
        'h1': ParagraphStyle('h1', **{**base, 'fontName': 'Sans-Bold', 'fontSize': 14,
                                      'leading': 18, 'textColor': ACCENT, 'spaceBefore': 6,
                                      'spaceAfter': 6}),
        'h2': ParagraphStyle('h2', **{**base, 'fontName': 'Sans-Bold', 'fontSize': 11,
                                      'leading': 14, 'spaceBefore': 8, 'spaceAfter': 3}),
        'body': ParagraphStyle('body', **{**base, 'spaceAfter': 4}),
        'small': ParagraphStyle('small', **{**base, 'fontSize': 8, 'leading': 10}),
        'cell': ParagraphStyle('cell', **{**base, 'fontSize': 8, 'leading': 10}),
        'cellb': ParagraphStyle('cellb', **{**base, 'fontName': 'Sans-Bold', 'fontSize': 8,
                                            'leading': 10}),
        'bullet': ParagraphStyle('bullet', **{**base, 'leftIndent': 12, 'bulletIndent': 2,
                                              'spaceAfter': 2}),
        'sub': ParagraphStyle('sub', **{**base, 'fontSize': 8.5, 'leading': 11, 'leftIndent': 26,
                                        'bulletIndent': 16, 'spaceAfter': 1, 'textColor': MUTED}),
        'code': ParagraphStyle('code', **{**base, 'fontName': 'Mono', 'fontSize': 7.5,
                                          'leading': 9.5}),
        'mono': ParagraphStyle('mono', **{**base, 'fontName': 'Mono', 'fontSize': 6.3,
                                          'leading': 7.6}),
    }


def esc(text):
    return (str(text).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))


def is_critical(item):
    return item.get('severidad') == 'Crítico'


def is_closed(item):
    return item.get('estado', '').startswith(('Cerrado', 'No aplica', 'Aceptado sin cambio', 'Sin acción',
                                              'Se cierra con otro punto'))


def critical_rows(items, first_row=1):
    """Table style commands that paint the whole row of a closed item green and of an open critical item red."""
    return [('BACKGROUND', (0, n), (-1, n), DONE_BG if is_closed(i) else CRIT_BG)
            for n, i in enumerate(items, first_row) if is_closed(i) or is_critical(i)]


def origin_note(item):
    return f" ({item['origen_ref']})" if item.get('origen_ref') else ''


def table(rows, widths, st, header=True, extra=()):
    data = [[c if not isinstance(c, str) else Paragraph(esc(c), st['cellb' if header and i == 0
                                                                     else 'cell'])
             for c in row] for i, row in enumerate(rows)]
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0)
    style = [('VALIGN', (0, 0), (-1, -1), 'TOP'),
             ('LINEBELOW', (0, 0), (-1, -1), 0.25, RULE),
             ('TOPPADDING', (0, 0), (-1, -1), 2), ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
             ('LEFTPADDING', (0, 0), (-1, -1), 3), ('RIGHTPADDING', (0, 0), (-1, -1), 3)]
    if header:
        style.append(('BACKGROUND', (0, 0), (-1, 0), HEAD_BG))
    t.setStyle(TableStyle(style + list(extra)))
    return t


def bullets(items, st):
    return [Paragraph(esc(i) if not i.startswith('<') else i, st['bullet'], bulletText='•')
            for i in items]


# ---------------------------------------------------------------- repository facts

def allowlist():
    sys.path.insert(0, os.path.join(REPO, 'tools'))
    from check_cleanup import load_allowlist
    cwd = os.getcwd()
    os.chdir(REPO)
    try:
        allow, _ = load_allowlist()
    finally:
        os.chdir(cwd)
    return allow


def changed_programs():
    names = git('diff', '--name-only', BASE, 'HEAD', '--', 'KRC').decode().split('\n')
    return [n for n in names if n.lower().endswith(('.src', '.sub'))
            and os.path.exists(os.path.join(REPO, n))]


def code_changes():
    return json.load(open(os.path.join(REPO, 'tools', 'code_changes.json')))


def audit_base():
    """tools/audit_base.json when the programmer's program is the audited base, else None."""
    path = os.path.join(REPO, 'tools', 'audit_base.json')
    if not os.path.exists(path):
        return None
    data = json.load(open(path))
    return data if data.get('programmer_base_commit') else None


def last_backup():
    """(date and time, short commit) of the newest programmer backup imported as received,
    from its commit subject; the switch commit of 2026-10-05 14:46 when none came after it."""
    out = git('log', '-1', '--format=%h %s', '--grep', "^Programmer's backup of").decode().strip()
    m = re.match(r"(\w+) Programmer's backup of (\d{4}-\d\d-\d\d \d\d:\d\d)", out)
    if m:
        return m.group(2), m.group(1)
    switch = audit_base()
    return '2026-10-05 14:46', switch['programmer_base_commit'][:7] if switch else ''


def added_lines(path, base=BASE):
    """Line numbers of the HEAD version added or changed since `base`."""
    diff = git('diff', '-U0', base, 'HEAD', '--', path).decode('latin-1')
    added = set()
    for m in re.finditer(r'^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@', diff, re.M):
        start, count = int(m.group(1)), int(m.group(2) or '1')
        added.update(range(start, start + count))
    return added


def head_text(path):
    return git('show', f'HEAD:{path}').decode('latin-1').replace('\r', '')


def marked_comments():
    """[(path, line, kind, text)] of every ;CHECK: / ;WARNING: comment, joined
    with its continuation lines: indented comment lines (';  ...') and, for a
    sentence split over several marked lines, the same marker again until the
    text ends with the finding number in parentheses."""
    out = []
    for path in sorted(git('ls-files', 'KRC').decode().split('\n')):
        if not path.lower().endswith(('.src', '.sub', '.dat')):
            continue
        lines = head_text(path).split('\n')
        i = 0
        while i < len(lines):
            m = re.match(r'\s*;\s*(CHECK|WARNING):\s*(.*)', lines[i])
            if not m:
                i += 1
                continue
            kind, text, j = m.group(1), m.group(2).strip(), i + 1
            while j < len(lines):
                nxt = lines[j].strip()
                same = re.match(r';\s*' + kind + r':\s*(.*)', nxt)
                if nxt.startswith(';  '):
                    text += ' ' + nxt[1:].strip()
                elif same and not text.endswith(')'):
                    text += ' ' + same.group(1).strip()
                else:
                    break
                j += 1
            out.append((path, i + 1, kind, text))
            i = j
    return out


# ---------------------------------------------------------------- sections

def cover(st, items, now, scope='all'):
    head = git('rev-parse', '--short', 'HEAD').decode().strip()
    archive = code_changes().get('archive')
    switch = audit_base()
    open_n = sum(1 for i in items if i.get('estado', '').startswith(('Abierto', 'Requiere',
                                                                       'En proceso', 'Reabierto',
                                                                       'Corregido')))
    if switch:
        title = scopes.SCOPES[scope]['title'] if scope in scopes.SCOPES else \
            'Auditoría del programa del programador y puntos abiertos'
        when, commit = last_backup()
        base = (f'Base auditada desde el 2026-10-11: el programa del programador, su último respaldo, del {when} '
                f'(commit {commit}). La versión de oficina (commit '
                f'{switch["office_last_commit"][:7]}) queda como referencia. ')
    else:
        title = 'Depuración, correcciones de la revisión Gestamp y puntos abiertos'
        base = (f'Respaldo de partida: 658424 (v431_03_10_r1) del 2026-10-02 (commit {BASE}). '
                + (f'Fusionado con el respaldo {esc(archive["zip"])} (commit {archive["commit"][:7]}). '
                   if archive else ''))
    return [
        Paragraph('Robot R10 (BMW-03-10-R1)', st['title']),
        Paragraph(title, st['h1']),
        Paragraph(f'Gestamp, línea BMW G65, celda 03, estación 03-10-R1 · KUKA KR C4, KSS 8.3.29, '
                  f'robot 658424 · Ethos Automation México', st['subtitle']),
        Spacer(1, 4),
        Paragraph(base +
                  f'Estado de este reporte: commit {head}, generado {now}. '
                  f'Puntos abiertos: {open_n} de {len(items)}.', st['small']),
        Spacer(1, 10),
    ]


def summary(st, items):
    crit = [i for i in items if i['severidad'] == 'Crítico']
    high = [i for i in items if i['severidad'] == 'Alto']
    switch = audit_base()
    if switch:
        return summary_programmer_base(st, items, crit, high)
    out = [Paragraph('1. Resumen', st['h1']),
           Paragraph('Se depuró el programa del R10 sin cambiar lo que hace el robot. Se tradujeron '
                     'los comentarios al inglés, cada acción de I/O y cada espera nombra su señal con '
                     'dirección y nombre, se corrigieron los comentarios que contradecían al código, '
                     'cada módulo lleva el encabezado Gestamp, y se eliminó el código basura: once '
                     'módulos que nada llama (21 archivos), código comentado y 856 declaraciones y puntos '
                     'sin uso. El R10 hace la misma operación que el R20 (pedestal CenterLine, tres tuercas '
                     'en lugar de cinco); los hallazgos conservan la numeración del R20.',
                     st['body']),
           Paragraph('La prueba de que el comportamiento no cambió es mecánica: '
                     '<font name="Mono">tools/check_cleanup.py</font> quita lo que el compilador KRL '
                     'ignora y compara línea por línea contra el respaldo original; además un revisor '
                     'independiente comparó cada comentario contra el código.',
                     st['body']),
           Paragraph('Los problemas de comportamiento encontrados en la depuración no se corrigieron en '
                     'ese paso: son los puntos abiertos de este documento '
                     f'({len(items)} en total, {len(crit)} críticos y {len(high)} altos). El programador los '
                     'cierra modificando el programa; cada respaldo diario se audita contra el criterio de '
                     'cierre de cada punto.', st['body'])]
    gest = [i for i in items if i['id'].startswith('G')]
    if gest:
        ofi = [i for i in gest if i.get('estado') == OFFICE]
        out.append(Paragraph(
            f'Gestamp revisó el programa el 2026-10-02 y entregó {len(gest)} puntos para esta estación '
            f'(BMW-03-10R1). Están en la lista como G01–G{len(gest):02d}, con su texto original. '
            f'{len(ofi)} se corrigieron en la oficina en la versión que se entrega al programador '
            f'({", ".join(i["id"] for i in ofi)}): falta cargarla y probarla en celda. El resto necesita '
            'trabajo en celda (seguridad, cargas, nombre del robot) o una decisión de Gestamp (sección 3).',
            st['body']))
    calvin = [i for i in items if i.get('origen_ref', '').startswith('Calvin')]
    if calvin:
        out.append(Paragraph(
            f'La lista de Calvin (Ethos, 2026-10-03) se verificó punto por punto para el 10R1: '
            f'{len(calvin)} puntos de esta lista citan su número (columna Origen, "Calvin #n"). '
            'Esta lista es la única que se usa.', st['body']))
    if crit:
        out.append(Paragraph('<font color="#b42318">Críticos</font>', st['h2']))
        out += [Paragraph(f'<font color="#b42318"><b>{esc(i["id"])} — {esc(i["titulo"])}</b></font>',
                          st['bullet'], bulletText='•') for i in crit]
    return out


def summary_gestamp(st, items, by_id):
    """Section 1 of the Gestamp report: where the 22 points stand and what is left for the buy off."""
    done = [i for i in items if is_closed(i)]
    work = [i for i in items if i.get('estado') == 'En proceso']
    left = [i for i in items if not is_closed(i)]
    out = [Paragraph('1. Resumen', st['h1']),
           Paragraph(f'Gestamp revisó el programa el 2026-10-02 y entregó {len(items)} puntos para esta estación '
                     f'(BMW-03-10R1), G01–G{len(items):02d}. Son los que Gestamp audita para el buy off. Sobre el '
                     f'programa del programador (su último respaldo, del {last_backup()[0]}): {len(done)} cerrados, '
                     f'{len(work)} en proceso y {len(left) - len(work)} pendientes.', st['body']),
           Paragraph('Criterio: no se le pide al programa más de lo que hace el respaldo de Gestamp NUT07_10R1; el '
                     'cierre final lo acepta Gestamp. Cuando un punto se cierra con los criterios de un punto de '
                     'Ethos, esos criterios vienen en el detalle. Los demás puntos de Ethos están en el reporte de '
                     'mejoras de proceso y no condicionan el buy off.', st['body'])]
    if left:
        out.append(Paragraph('Lo que falta para el buy off', st['h2']))
        rows = [['Punto', 'Estado', 'Qué hacer', 'Relacionados (Ethos) abiertos']]
        for i in left:
            rows.append([i['id'] + '\n' + i['titulo'], i.get('estado', ''), i['que_hacer'],
                         scopes.with_state([r for r in scopes.related(i, by_id) if not is_closed(by_id[r])],
                                           by_id)])
        out.append(table(rows, [38 * mm, 22 * mm, 88 * mm, 34 * mm], st, extra=critical_rows(left)))
    return out


def summary_mejoras(st, items, links):
    crit_open = [i for i in items if is_critical(i) and not is_closed(i)]
    pending = [i for i in items if not is_closed(i)]
    counted = [i for i in pending if links.get(i['id'])]
    out = [Paragraph('1. Resumen', st['h1']),
           Paragraph(f'Puntos de la revisión de Ethos (Fnn/Cnn): {len(items)} en total, {len(pending)} pendientes. '
                     'Son mejoras de proceso: no condicionan el buy off y se trabajan después de los puntos de '
                     'Gestamp, que van en su propio reporte.', st['body']),
           Paragraph(f'{len(counted)} de los pendientes cuentan además para un punto de Gestamp abierto (columna '
                     'Gestamp en la sección 4): cerrarlos ayuda al buy off.', st['body']),
           Paragraph(f'Base: el programa del programador, su último respaldo, del {last_backup()[0]}. Cada respaldo se '
                     'audita contra el anterior (tools/audit_backup.py); la versión de oficina queda como referencia '
                     '(sección 2).', st['body'])]
    if crit_open:
        out.append(Paragraph('<font color="#b42318">Críticos abiertos</font>', st['h2']))
        out += [Paragraph(f'<font color="#b42318"><b>{esc(i["id"])} — {esc(i["titulo"])}</b></font>',
                          st['bullet'], bulletText='•') for i in crit_open]
    return out


def summary_programmer_base(st, items, crit, high):
    out = [Paragraph('1. Resumen', st['h1']),
           Paragraph('Desde el 2026-10-11, por decisión de Edgar (igual que en R20), la base es el programa que corre '
                     f'en el robot: su último respaldo, del {last_backup()[0]}. Ya no se le pide cargar la versión de oficina. Cada '
                     'respaldo se audita contra el anterior (tools/audit_backup.py) y cada punto contra su '
                     'criterio de cierre sobre su programa.', st['body']),
           Paragraph('La depuración y las correcciones de oficina (2026-10-02 a 2026-10-07) se entregaron como '
                     'paquetes y no se cargaron; quedan como referencia (sección 2). Los puntos que la oficina había '
                     'corregido se revisaron contra su programa; la nota de cada uno dice cómo lo resolvió la '
                     'oficina.', st['body']),
           Paragraph(f'Puntos de la lista: {len(items)} en total, {len(crit)} críticos y {len(high)} altos. El '
                     'programador los cierra modificando su programa; cada respaldo diario se audita contra el '
                     'criterio de cierre de cada punto.', st['body'])]
    gest = [i for i in items if i['id'].startswith('G')]
    if gest:
        done = [i for i in gest if i.get('estado', '').startswith(('Cerrado', 'No aplica', 'Aceptado',
                                                                   'Se cierra'))]
        work = [i for i in gest if i.get('estado') == 'En proceso']
        out.append(Paragraph(
            f'Gestamp revisó el programa el 2026-10-02 y entregó {len(gest)} puntos para esta estación '
            f'(BMW-03-10R1), en la lista como G01–G{len(gest):02d}. Sobre el programa del programador: '
            f'{len(done)} cerrados, {len(work)} en proceso y {len(gest) - len(done) - len(work)} pendientes '
            '(sección 3).', st['body']))
    crit_open = [i for i in crit if not is_closed(i)]
    if crit_open:
        out.append(Paragraph('<font color="#b42318">Críticos abiertos</font>', st['h2']))
        out += [Paragraph(f'<font color="#b42318"><b>{esc(i["id"])} — {esc(i["titulo"])}</b></font>',
                          st['bullet'], bulletText='•') for i in crit_open]
    return out


def latest_audit():
    """The newest audits/*/resumen.json (curated summary of a programmer-backup audit), or None."""
    found = []
    for path in glob.glob(os.path.join(REPO, 'audits', '*', 'resumen.json')):
        data = json.load(open(path, encoding='utf-8'))
        found.append((data.get('fecha_auditoria', ''), path, data))
    if not found:
        return None
    _, path, data = max(found)
    data['carpeta'] = os.path.relpath(os.path.dirname(path), REPO)
    return data


def last_audit_gestamp(st, items, data):
    """1.1 of the Gestamp report: what the last audit changed in the Gestamp points."""
    a = latest_audit()
    audits_ = data.get('auditorias', [])
    if not audits_:
        return []
    last = audits_[-1]
    rows = [['Punto', 'Estado', 'Resultado de la auditoría']]
    shown = []
    for i in items:
        notes = [h for h in i.get('historial', []) if h.get('fecha') == last.get('fecha')]
        if notes:
            rows.append([i['id'] + '\n' + i['titulo'], i.get('estado', ''),
                         '\n'.join(f"{h.get('resultado', '')}: {h.get('nota', '')}" for h in notes)])
            shown.append(i)
    out = [Paragraph('1.1 Última auditoría', st['h2']),
           Paragraph(f"Respaldo: {esc(last.get('respaldo', ''))}. Auditado el {esc(last.get('fecha', ''))}"
                     + (f". Detalle completo: <font name='Mono'>{esc(a['carpeta'])}/REVISION.es.md</font>."
                        if a else '.'), st['small']), Spacer(1, 3)]
    if shown:
        out.append(table(rows, [38 * mm, 26 * mm, 118 * mm], st, extra=critical_rows(shown)))
    else:
        out.append(Paragraph('Sin cambios en los puntos de Gestamp en esta auditoría.', st['body']))
    return out


def last_audit(st):
    a = latest_audit()
    if not a:
        return []
    out = [PageBreak(), Paragraph(f"1.1 {esc(a['titulo'])}", st['h1']),
           Paragraph(f"Respaldo: {esc(a['respaldo'])}. Auditado el {esc(a['fecha_auditoria'])}. Detalle "
                     f"completo: "
                     f"<font name='Mono'>{esc(a['carpeta'])}/REVISION.es.md</font>.", st['small']),
           Spacer(1, 4),
           Paragraph(esc(a['base']), st['body']),
           Paragraph(esc(a['cierre']), st['body'])]
    if a.get('bueno'):
        out.append(Paragraph('Lo que hizo bien el programador', st['h2']))
        out += bullets(a['bueno'], st)
    if a.get('riesgos'):
        out.append(Paragraph('Riesgos, de más a menos importante', st['h2']))
        rows = [['#', 'Riesgo', 'Puntos']]
        rows += [[str(n), r['texto'], ', '.join(r.get('items', []))] for n, r in enumerate(a['riesgos'], 1)]
        out.append(table(rows, [7 * mm, 145 * mm, 28 * mm], st))
    if a.get('plan'):
        out.append(Paragraph('Plan', st['h2']))
        out += [Paragraph(esc(p), st['bullet'], bulletText=f'{n}.') for n, p in enumerate(a['plan'], 1)]
    if a.get('pedir'):
        out.append(Paragraph('Qué pedir al programador', st['h2']))
        out += bullets(a['pedir'], st)
    return out


def what_was_done(st, allow):
    out = [PageBreak(), Paragraph('2. Qué se hizo', st['h1'])]
    out.append(Paragraph('2.1 Regla de trabajo', st['h2']))
    out += bullets([
        'Cambia lo que lee una persona, nunca lo que hace el robot: ninguna instrucción ejecutable '
        'cambió de texto, de orden ni de mayúsculas.',
        'Los encabezados de inline form con datos del smartPAD (%P) y las líneas dentro del form no se '
        'tocaron, salvo refrescar el nombre de herramienta en el texto visible y la corrección '
        'registrada de RejectGE4.',
        'Cada archivo conserva sus fines de línea (el respaldo mezcla CRLF y LF) y queda en ASCII.',
        'Cada eliminación ejecutable (módulo o declaración) está en el allowlist con su razón, y el '
        'verificador prueba que nada la referencia.'], st)

    out.append(Paragraph('2.2 Formato de los comentarios', st['h2']))
    out.append(Paragraph('Cada acción de I/O y cada espera nombra la señal con dirección y etiqueta '
                         '(docs/IO_MAP.md). Tres prefijos: NOTE (explicación), CHECK (confirmar en celda, '
                         'cita el punto abierto) y WARNING (trampa, p. ej. no reabrir un inline form).',
                         st['body']))
    before = (';QUITAR AIRE LOWER PIN\n$OUT[495]=FALSE\n$OUT[496]=FALSE')
    after = (';LOWER PIN BOTH VALVES OFF (OLD COMMENT: REMOVE AIR FROM THE LOWER PIN) -\n'
             ';  SIGNALS $OUT[495] dopw1_AdvancePin OFF, $OUT[496] dopw1_ReturnPin OFF\n'
             '$OUT[495]=FALSE\n$OUT[496]=FALSE')
    out.append(table([['Antes', 'Después'],
                      [Paragraph(esc(before).replace('\n', '<br/>'), st['code']),
                       Paragraph(esc(after).replace('\n', '<br/>'), st['code'])]],
                     [70 * mm, 110 * mm], st))

    out.append(Paragraph('2.3 Módulos eliminados', st['h2']))
    out.append(Paragraph('Ninguno es llamado por nada; el verificador prueba que ninguna línea viva los '
                         'referencia. La razón completa (en inglés) está en tools/cleanup_allowlist.json.',
                         st['body']))
    rows = [['Archivo', 'Razón']]
    for path in allow['deleted_files']:
        name = os.path.basename(path)
        rows.append([path.replace('KRC/R1/Program/', ''), DELETED_ES.get(name.lower(), allow['deleted_files'][path])])
    out.append(table(rows, [60 * mm, 120 * mm], st))

    out.append(Paragraph('2.4 Declaraciones y datos sin uso eliminados', st['h2']))
    out.append(Paragraph('Declaraciones que nada referencia: puntos y datos de movimientos que ya no existen, '
                         'datos de inline forms NutWeld viejos y variables globales sin uso. Cada línea está '
                         'en tools/cleanup_allowlist.d/ con su razón.', st['body']))
    rows = [['Archivo', 'Líneas', 'Qué se eliminó']]
    total = 0
    for path, entry in sorted(allow['removed_code'].items()):
        if not entry['lines']:
            continue
        total += len(entry['lines'])
        kinds = {}
        for line in entry['lines']:
            m = re.match(r'\s*(?:GLOBAL\s+)?(?:DECL\s+)?(?:GLOBAL\s+)?(\w+)', line)
            k = m.group(1).upper() if m else '?'
            kinds[k] = kinds.get(k, 0) + 1
        what = ', '.join(f'{n} {k}' for k, n in sorted(kinds.items(), key=lambda x: -x[1]))
        rows.append([path.replace('KRC/R1/', ''), str(len(entry['lines'])), what])
    rows.append(['Total', str(total), ''])
    out.append(table(rows, [78 * mm, 16 * mm, 86 * mm], st))

    out.append(Paragraph('2.5 Trampas corregidas o señaladas', st['h2']))
    out += bullets([
        'RejectGE4: el inline form del reset de $OUT[106] traía oculto 5:TRUE y encerraba los resets de '
        'banderas; confirmarlo convertía el reset en set y borraba los resets. Quedó 5:FALSE y los resets '
        'fuera del fold, sin mover código (igual que en el R20).',
        'Forms GripperTech de picks y drop a banda: parámetros ocultos setgripper=4;setstate=2. Reabrirlos '
        'habría regenerado la llamada para el gripper 4 ($OUT[251]/[252]): el gripper 1 no se mueve y el check '
        'cae en timeout. Corregido en la versión de oficina (F31, G10).',
        'Drop red rabbit: suelta con el gripper 3, que en grp_data.dat tiene el mismo I/O que el gripper 1; '
        'funciona solo por ese mapeo duplicado (F19, F31). Quedó WARNING en el código.',
        'WARNING sobre los folds que no deben reabrirse: parámetros AutomationCore ocultos que no coinciden '
        'con la llamada (F21). Los TRIGGER escritos a mano dentro de inline forms (F32) se sacaron en la '
        'versión de oficina.',
        'CloseAndCheckAllClamps / OpenAndCheckAllClamps: se quitaron los folds comentados de los grippers 2-4 '
        '(Calvin #23, F45).'], st)

    out.append(Paragraph('2.6 Comentarios que contradecían el código', st['h2']))
    out.append(Paragraph('Se reescribieron para describir lo que hace el código; cada uno lleva un CHECK '
                         'para confirmarlo en celda (punto F27).', st['body']))
    rows = [['Programa', 'Decía', 'El código hace']]
    rows += [['centerline_weld', 'UPPER PIN EXTEND', 'retrae el upper pin ($OUT[499] ON)'],
             ['centerline_weld', 'SCHEDULE 7', 'selecciona el programa Bosch 2'],
             ['centerline_weld', 'LOWER PIN RETURN (fin de soldadura)', 'avanza el lower pin ($OUT[495] ON)'],
             ['PRELOAD', 'CL_LowerPinRetreated', 'avanza el lower pin'],
             ['PRELOAD', 'QFP ADV (en la espera de QFP regresado)', 'espera $IN[482] QFP regresado'],
             ['programas del pedestal', 'comentarios en español', 'traducidos y con la señal nombrada']]
    out.append(table(rows, [42 * mm, 62 * mm, 76 * mm], st))

    out.append(Paragraph('2.7 Herramientas que quedan en el repositorio', st['h2']))
    out += bullets([
        'tools/check_cleanup.py — prueba que la depuración cambió comentarios y no comportamiento.',
        'tools/build_archive.py — arma el zip de respaldo a cargar sobre el respaldo original o sobre el '
        'último respaldo auditado (hoy bmw_03_10_r1 del 2026-10-05); con cualquier otro se niega si el '
        'robot cambió.',
        'tools/check_equivalence.py — separa los cambios reales de lógica de los renombres en los cambios '
        'de código posteriores a la depuración (sección 3).',
        'tools/audit_backup.py — audita cada respaldo diario contra el último estado auditado.',
        'tools/make_report.py — genera este PDF.'], st)
    return out


def gestamp_review(st, items):
    gest = [i for i in items if i['id'].startswith('G')]
    if not gest:
        return []
    cc = code_changes()
    out = [PageBreak(), Paragraph('3. Revisión de Gestamp y correcciones de oficina', st['h1']),
           Paragraph('Documento de Gestamp "Robot Program Review – Findings" del 2026-10-02, sección '
                     'BMW-03-10R1 (22 puntos). Cada punto quedó en la lista de puntos abiertos con el prefijo G y '
                     'su texto original; los que coinciden con un hallazgo de Ethos remiten a él (columna Ver).',
                     st['body'])]
    rows = [['ID', 'Texto de Gestamp', 'Estado', 'Ver']]
    extra = []
    for n, i in enumerate(gest, 1):
        rows.append([i['id'], i.get('texto_gestamp', ''), i.get('estado', ''), ', '.join(i.get('depende_de', []))])
        if i.get('estado') == OFFICE:
            extra.append(('BACKGROUND', (2, n), (2, n), CODE_BG))
    out.append(table(rows, [11 * mm, 96 * mm, 45 * mm, 30 * mm], st, extra=critical_rows(gest) + extra))

    out.append(Paragraph('3.1 Qué se corrigió en la oficina', st['h2']))
    out.append(Paragraph('A diferencia de la depuración, aquí sí cambia el código. Cada cambio está en '
                         'tools/code_changes.json con los puntos que atiende; resumen:', st['body']))
    rows = [['Punto', 'Cambio']]
    for i in gest:
        if i.get('estado') == OFFICE:
            what = re.sub(r'^Hecho en oficina: ', '', i['que_hacer'])
            rows.append([i['id'] + '\n' + i['titulo'], what[:1].upper() + what[1:]])
    out.append(table(rows, [42 * mm, 140 * mm], st))
    rows = [['Módulo borrado', 'Razón']]
    for path, why in cc.get('deleted_files', {}).items():
        rows.append([path.replace('KRC/R1/', ''), DELETED_ES.get(os.path.basename(path).lower(), why)])
    out.append(Spacer(1, 4))
    out.append(table(rows, [68 * mm, 114 * mm], st))

    out.append(Paragraph('3.2 Cómo se verificó', st['h2']))
    out += bullets([
        'La depuración sigue probada: tools/check_cleanup.py --head ' + cc['base'][:7] + ' (commit de la '
        'depuración) pasa.',
        'tools/check_equivalence.py compara cada programa contra la depuración traduciendo cada nombre de '
        'señal a su dirección y cada constante a su valor: los renombres desaparecen y solo queda la lógica '
        'que cambió. Ocho módulos salen equivalentes (solo renombres o sangría); en los demás, cada diferencia '
        'es una de las listadas arriba. Un cambio no listado en tools/code_changes.json lo hace fallar. La '
        'carpeta Styles/optiones pasó a Styles/Options (dos archivos movidos, mismo contenido).',
        'tools/audit_backup.py sobre el zip armado contra el commit de la depuración: 0 FAIL y 0 WARN '
        '(los INFO son esperas sin timeout que ya existían, F15). Reporte en audits/2026-10-04_oficina-gestamp.',
        'Revisión independiente de los comentarios contra el código: corrigió el texto del drop red rabbit '
        '(el gripper 3 sí abre el gripper 1), el de las tareas de fondo de sps.sub y el de las banderas de '
        'precarga.',
        'Lo que ninguna verificación de escritorio sustituye: la prueba en celda que pide cada punto '
        '"Corregido en oficina - probar en celda".'], st)

    out.append(Paragraph('3.3 Lo que debe probar el programador en celda', st['h2']))
    for i in gest:
        if i.get('estado') == OFFICE:
            tests = [c for c in i.get('criterio_cierre', [])
                     if c.startswith('Prueba') or 'ciclo' in c and not c.startswith('Respaldo completo')]
            if tests:
                out.append(Paragraph(f"<b>{i['id']}</b> {esc(i['titulo'])}", st['body']))
                out += bullets(tests, st)

    out.append(Paragraph('3.4 Lo que queda fuera de la oficina', st['h2']))
    rows = [['ID', 'Punto', 'Responsable', 'Estado']]
    rest = [i for i in gest if i.get('estado') != OFFICE]
    for i in rest:
        rows.append([i['id'], i['titulo'], i['responsable'], i.get('estado', '')])
    out.append(table(rows, [11 * mm, 85 * mm, 54 * mm, 32 * mm], st, extra=critical_rows(rest)))
    return out


def office_reference(st):
    switch = audit_base()
    out = [PageBreak(), Paragraph('2. Versión de oficina (referencia, no cargada)', st['h1'])]
    out += bullets([
        'Del 2026-10-02 al 2026-10-07 Ethos preparó una versión de oficina: depuración de comentarios y código '
        'basura sin cambiar el comportamiento (03/10), correcciones de la revisión de Gestamp (04/10), integración '
        'de los respaldos del programador (05/10) y la etapa 1 de tiempo ciclo, F52 (07/10).',
        'Se entregó como paquetes de WorkVisual. Hasta el 05/10 el programador siguió sobre su propio programa; '
        'antes del respaldo del 10/10 cargó la versión de oficina del 05/10 y trabajó encima.',
        f'El 2026-10-11 Edgar decidió tomar su programa como base (commit '
        f'{switch["programmer_base_commit"][:7]}). La versión de oficina queda en el commit '
        f'{switch["office_last_commit"][:7]}; build_archive.py, check_cleanup.py y check_equivalence.py son '
        'herramientas de esa etapa.',
        'En cada punto que la oficina había corregido, la nota dice cómo lo resolvió (referencia para el '
        'programador). El detalle técnico sigue en docs/FINDINGS.md.'], st)
    return out


def gestamp_status(st, items):
    gest = [i for i in items if i['id'].startswith('G')]
    if not gest:
        return []
    out = [PageBreak(), Paragraph('2. Los 22 puntos de Gestamp', st['h1']),
           Paragraph('Documento de Gestamp "Robot Program Review – Findings" del 2026-10-02, sección '
                     'BMW-03-10R1 (22 puntos), revisado contra el programa del programador. Fondo verde: cerrado. '
                     'Columna Cómo quedó: el último resultado de la auditoría.', st['body'])]
    rows = [['ID', 'Texto de Gestamp', 'Estado', 'Cómo quedó']]
    for i in gest:
        last = (i.get('historial') or [{}])[-1]
        rows.append([i['id'], i.get('texto_gestamp', ''), i.get('estado', ''),
                     f"{last.get('fecha', '')}: {last.get('nota', '')}"])
    out.append(table(rows, [11 * mm, 62 * mm, 27 * mm, 82 * mm], st, extra=critical_rows(gest)))
    return out


def process(st, num='4'):
    out = [PageBreak(), Paragraph(f'{num}. Cómo vamos a trabajar', st['h1'])]
    switch = audit_base()
    if switch:
        out.append(Paragraph('Base', st['h2']))
        out += bullets([
            f'La base es el programa del programador (su último respaldo, del {last_backup()[0]}, commit '
            f'{last_backup()[1]}). No se carga ninguna versión de oficina.',
            'Los módulos sobrantes (G05: capchange, electrodechange, redrabbit y POUNCE) se borran cuando la celda esté probada al 100 %; antes no se evalúan. '
            'Guardar el proyecto WorkVisual desde el controlador antes de cualquier deploy.',
            'Ethos cambia código solo cuando Edgar lo pide, siempre sobre el último respaldo del programador, y '
            'entrega solo los archivos que cambian en entregas/<fecha>_<puntos>/ (cambios.diff, LEEME.txt y PDF de '
            'instrucciones); $config.dat nunca va completo.',
            'Dos listas desde el 2026-10-12: los puntos de Gestamp (G01–G22), que Gestamp audita para el buy off y '
            'van primero, y las mejoras de proceso (puntos de Ethos), que no lo condicionan. Cada una con su Excel y '
            'su reporte; cada punto está en una sola.'], st)
    else:
        out.append(Paragraph('Día 0', st['h2']))
    out += [] if switch else bullets([
        'Cargar en el robot la versión de oficina (zip de build_archive.py: depuración más correcciones de '
        'Gestamp) y borrar en el controlador los 17 archivos de módulos eliminados (12 de la depuración, 5 de '
        'las correcciones; un restore no borra archivos). Actualizar el proyecto WorkVisual desde el '
        'controlador antes de cualquier deploy.',
        'Hacer las pruebas en celda de los puntos "Corregido en oficina - probar en celda" (sección 3.3).',
        'Correr un ciclo en T1 con override reducido y uno en automático.',
        'Sacar un respaldo completo (Archive → All): es el punto de partida de las auditorías.'], st)
    out.append(Paragraph('Cada día', st['h2']))
    out += bullets([
        'El programador modifica el programa para cerrar puntos. Respeta docs/CONVENTIONS.md: comentarios '
        'en inglés con la señal nombrada, sin código comentado, sin reabrir inline forms con líneas '
        'escritas a mano.',
        'En el Excel de su lista (Gestamp o mejoras), por cada punto trabajado: Estado = "Corregido - por auditar", qué '
        'cambió, en qué módulos, y la evidencia que pide el criterio de cierre (prueba en celda con fecha '
        'y resultado). No marca nada como Cerrado: eso lo hace la auditoría.',
        'Al final del día saca un respaldo completo y lo envía junto con los Excel que trabajó.',
        'Edgar sube ambos aquí. La auditoría compara el respaldo contra el último auditado, revisa cada '
        'cambio de código, verifica cada punto marcado contra su criterio de cierre, corre las '
        'verificaciones mecánicas y regresa el Excel actualizado con el resultado y un reporte de '
        'auditoría.'], st)
    out.append(Paragraph('Estados', st['h2']))
    rows = [['Estado', 'Quién lo pone', 'Significa'],
            ['Abierto', 'Auditoría', 'Pendiente de trabajar.'],
            ['Requiere decisión', 'Auditoría', 'Falta información o decisión (Gestamp, seguridad, Ethos) '
                                               'antes de programar.'],
            ['En proceso', 'Programador', 'Trabajo empezado, aún no listo para auditar.'],
            ['Corregido - por auditar', 'Programador', 'Cambio hecho y probado; pide auditoría.'],
            ['Cerrado - auditado', 'Auditoría', 'Cumple todos los criterios de cierre en el respaldo.'],
            ['Reabierto', 'Auditoría', 'La auditoría no encontró el cambio o no cumple; ver nota.'],
            ['Aceptado sin cambio', 'Ethos / Gestamp', 'Se decidió no corregir; queda la razón y quién '
                                                       'lo aceptó.'],
            ['Cerrado - depuración / No aplica / Se cierra con otro punto', 'Auditoría',
             'Resuelto por la depuración, cumple, o duplica otro punto.']]
    if not switch:
        rows.insert(3, [OFFICE, 'Auditoría', 'Ethos lo corrigió en la versión entregada; el programador lo '
                                             'prueba en celda y lo pasa a "Corregido - por auditar" con la '
                                             'evidencia.'])
    out.append(table(rows, [52 * mm, 30 * mm, 98 * mm], st))
    return out


def audits(st, data, num='4.1'):
    rows = [['Fecha', 'Respaldo', 'Resultado']]
    for a in data.get('auditorias', []):
        rows.append([a.get('fecha', ''), a.get('respaldo', ''),
                     f"{a.get('cambios', '')}\n{a.get('notas', '')}"])
    if len(rows) == 1:
        return []
    return [Paragraph(f'{num} Auditorías', st['h2']),
            Paragraph('Cada respaldo auditado y cada versión entregada, del más viejo al más nuevo. El detalle '
                      'técnico (en inglés) está en audits/&lt;fecha&gt;/AUDIT.md.', st['body']),
            table(rows, [20 * mm, 46 * mm, 116 * mm], st)]


def items_summary(st, items, num='5', links=None):
    if links is not None:
        out = [PageBreak(), Paragraph(f'{num}. Puntos — resumen', st['h1']),
               Paragraph('Fondo verde: puntos cerrados. Fondo rojo: puntos críticos abiertos. Columna Gestamp: punto '
                         'de Gestamp abierto para el que también cuenta (fondo azul en el ID). Los que vienen de la '
                         'lista de Calvin dicen "Calvin #n".', st['small'])]
        rows = [['ID', 'Sev.', 'Punto', 'Responsable', 'Estado', 'Gestamp']]
        extra = critical_rows(items)
        for n, i in enumerate(items, 1):
            g = links.get(i['id'], [])
            rows.append([i['id'], i['severidad'], i['titulo'] + origin_note(i), i['responsable'],
                         i.get('estado', ''), ', '.join(g)])
            extra.append(('TEXTCOLOR', (1, n), (1, n), SEV.get(i['severidad'], INK)))
            if g and not is_closed(i):
                extra.append(('BACKGROUND', (0, n), (0, n), CODE_BG))
        out.append(table(rows, [11 * mm, 14 * mm, 80 * mm, 30 * mm, 31 * mm, 16 * mm], st, extra=extra))
        return out
    out = [PageBreak(), Paragraph(f'{num}. Puntos abiertos — resumen', st['h1']),
           Paragraph('Fondo verde: puntos cerrados. Fondo rojo: puntos críticos abiertos. G01–G22: puntos de la revisión de Gestamp (fondo azul en el '
                     'ID). Fnn/Cnn: revisión de Ethos; los que vienen de la lista de Calvin dicen "Calvin #n".',
                     st['small'])]
    rows = [['ID', 'Sev.', 'Punto', 'Responsable', 'Estado']]
    extra = critical_rows(items)
    for n, i in enumerate(items, 1):
        rows.append([i['id'], i['severidad'], i['titulo'] + origin_note(i), i['responsable'], i.get('estado', '')])
        extra.append(('TEXTCOLOR', (1, n), (1, n), SEV.get(i['severidad'], INK)))
        if i['id'].startswith('G') and not is_closed(i):
            extra.append(('BACKGROUND', (0, n), (0, n), CODE_BG))
    out.append(table(rows, [11 * mm, 14 * mm, 88 * mm, 33 * mm, 34 * mm], st, extra=extra))
    return out


def items_detail(st, items, num='6', by_id=None, links=None, title='Puntos abiertos — detalle'):
    """by_id (Gestamp report): criteria 'se cumplen los criterios de F43' carry F43's, and the related
    Ethos items are listed with their state. links (improvement report): the Gestamp points an item counts for."""
    out = [PageBreak(), Paragraph(f'{num}. {title}', st['h1'])]
    for i in items:
        if is_critical(i):
            head = Table([[Paragraph(f"<font color='#b42318'>CRÍTICO — {i['id']} — {esc(i['titulo'])}</font>",
                                     st['h2'])]], colWidths=[182 * mm])
            head.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), CRIT_BG),
                                      ('LINEBEFORE', (0, 0), (0, -1), 3, CRIT),
                                      ('TOPPADDING', (0, 0), (-1, -1), 1), ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]))
            block = [Spacer(1, 4), head]
        else:
            block = [Paragraph(f"{i['id']} — {esc(i['titulo'])}", st['h2'])]
        if i.get('texto_gestamp'):
            block.append(Paragraph(f"<b>Gestamp:</b> \"{esc(i['texto_gestamp'])}\" — {esc(i.get('origen', ''))}",
                                   st['small']))
        elif i.get('origen_ref'):
            block.append(Paragraph(f"<b>Origen:</b> {esc(i.get('origen', ''))}", st['small']))
        block += [
                 Paragraph(f"<b>Severidad:</b> <font color='{SEV.get(i['severidad'], INK).hexval()}'>"
                           f"{i['severidad']}</font> · <b>Tipo:</b> {esc(i['tipo'])} · "
                           f"<b>Responsable:</b> {esc(i['responsable'])} · <b>Estado:</b> "
                           f"{esc(i.get('estado', ''))}", st['small'])]
        if i.get('modulos'):
            block.append(Paragraph('<b>Módulos:</b> ' + esc(', '.join(i['modulos'])), st['small']))
        block.append(Spacer(1, 3))
        out.append(KeepTogether(block))
        out.append(Paragraph('<b>Qué está mal.</b> ' + esc(i['que_esta_mal']), st['body']))
        out.append(Paragraph('<b>Qué hacer.</b> ' + esc(i['que_hacer']), st['body']))
        if i.get('criterio_cierre'):
            out.append(Paragraph('<b>Criterio de cierre</b> (se verifica en el respaldo):', st['body']))
            for sub, c in (scopes.expanded_criteria(i, by_id) if by_id else
                           [(False, c) for c in i['criterio_cierre']]):
                out.append(Paragraph(esc(c), st['sub'] if sub else st['bullet'], bulletText='–' if sub else '•'))
        if i.get('evidencia_programador'):
            out.append(Paragraph('<b>Evidencia del programador.</b> ' + esc(i['evidencia_programador']),
                                 st['body']))
        if by_id and scopes.related(i, by_id):
            out.append(Paragraph('<b>Relacionados (Ethos):</b> ' + esc(scopes.with_state(scopes.related(i, by_id),
                                                                                        by_id)), st['body']))
        elif i.get('depende_de'):
            out.append(Paragraph('<b>Depende de / se cierra con:</b> ' + esc(', '.join(i['depende_de'])),
                                 st['body']))
        if links and links.get(i['id']):
            out.append(Paragraph('<b>Cuenta para Gestamp:</b> ' + esc(', '.join(links[i['id']])), st['body']))
        if i.get('nota'):
            out.append(Paragraph('<b>Nota.</b> ' + esc(i['nota']), st['body']))
        hist = i.get('historial') or []
        if hist:
            out.append(Paragraph('<b>Historial de auditoría:</b>', st['body']))
            out += bullets([f"{h.get('fecha', '')} — {h.get('resultado', '')}: {h.get('nota', '')}"
                            for h in hist], st)
        out.append(Spacer(1, 6))
    return out


def annex_marked(st):
    out = [PageBreak(), Paragraph('Anexo A. Comentarios CHECK y WARNING en el programa', st['h1']),
           Paragraph('Cada línea que pide confirmar algo en celda (CHECK) o advierte de una trampa '
                     '(WARNING), con archivo y línea en el estado actual. El número entre paréntesis es '
                     'el punto abierto.', st['body'])]
    rows = [['Archivo:línea', 'Tipo', 'Comentario']]
    for path, line, kind, text in marked_comments():
        rows.append([f"{path.replace('KRC/R1/Program/', '').replace('KRC/R1/', '')}:{line}", kind, text])
    out.append(table(rows, [60 * mm, 19 * mm, 103 * mm], st))
    return out


def annex_listing(st):
    out = [PageBreak(), Paragraph('Anexo B. Programas modificados, con los comentarios de la depuración',
                                  st['h1']),
           Paragraph('Listado completo de cada programa modificado en su estado actual. Sombreado amarillo: '
                     'líneas que agregó o cambió la depuración (comentarios; el código no cambió). Sombreado '
                     'azul: líneas de las correcciones de oficina (cambios de código y sus comentarios). Los '
                     'encabezados de inline form se recortan después de ";%{" porque el resto son datos del '
                     'smartPAD.', st['body'])]
    office_base = code_changes()['base']
    width = 132
    for path in changed_programs():
        text = head_text(path).split('\n')
        added = added_lines(path)
        office = added_lines(path, office_base)
        out.append(Paragraph(esc(path), st['h2']))
        rows, shade = [], []
        for n, line in enumerate(text, 1):
            shown = line.split(';%{')[0] + (' ;%{...}' if ';%{' in line else '')
            shown = shown.expandtabs(3).rstrip()
            parts = [shown[k:k + width] for k in range(0, max(len(shown), 1), width)] or ['']
            for k, part in enumerate(parts):
                rows.append([str(n) if k == 0 else '', Paragraph(esc(part).replace(' ', '&nbsp;')
                                                                 or '&nbsp;', st['mono'])])
                if n in office:
                    shade.append(('BACKGROUND', (0, len(rows) - 1), (-1, len(rows) - 1), CODE_BG))
                elif n in added:
                    shade.append(('BACKGROUND', (0, len(rows) - 1), (-1, len(rows) - 1), NEW_BG))
        t = Table(rows, colWidths=[10 * mm, 172 * mm])
        t.setStyle(TableStyle([('FONTNAME', (0, 0), (0, -1), 'Mono'),
                               ('FONTSIZE', (0, 0), (0, -1), 6), ('TEXTCOLOR', (0, 0), (0, -1), MUTED),
                               ('ALIGN', (0, 0), (0, -1), 'RIGHT'), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                               ('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
                               ('LEFTPADDING', (0, 0), (-1, -1), 2), ('RIGHTPADDING', (0, 0), (-1, -1), 2)]
                              + shade))
        out.append(t)
    return out


CURRENT = {'scope': None}


def page_decor(canvas, doc):
    canvas.saveState()
    canvas.setFont('Sans', 7)
    canvas.setFillColor(MUTED)
    what = (scopes.SCOPES[CURRENT['scope']]['title'] if CURRENT['scope'] in scopes.SCOPES
            else 'Auditoría del programa del programador y puntos abiertos' if audit_base()
            else 'Depuración, correcciones Gestamp y puntos abiertos')
    canvas.drawString(18 * mm, 10 * mm, f'R10 (BMW-03-10-R1) · {what} · Ethos Automation México')
    canvas.drawRightString(letter[0] - 18 * mm, 10 * mm, f'Página {doc.page}')
    canvas.restoreState()


def build(scope, out, data, now):
    """One report: scope 'gestamp' or 'mejoras' (tools/scope.py)."""
    st = styles()
    all_items = data.get('items', [])
    items = scopes.select(all_items, scope)
    by_id = {i['id']: i for i in all_items}
    links = scopes.gestamp_links(all_items)
    CURRENT['scope'] = scope
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    doc = SimpleDocTemplate(out, pagesize=letter, leftMargin=16 * mm, rightMargin=16 * mm,
                            topMargin=15 * mm, bottomMargin=16 * mm,
                            title='R10 (BMW-03-10-R1) - ' + scopes.SCOPES[scope]['title'],
                            author='Ethos Automation México')
    story = cover(st, items, now, scope)
    if scope == 'gestamp':
        story += summary_gestamp(st, items, by_id) + last_audit_gestamp(st, items, data)
        story += gestamp_status(st, items)
        story += items_detail(st, items, '3', by_id=by_id, title='Detalle de los puntos de Gestamp')
        story += process(st, '4')
    else:
        story += summary_mejoras(st, items, links) + last_audit(st) + office_reference(st)
        story += process(st, '3') + audits(st, data, '3.1')
        story += items_summary(st, items, '4', links) + items_detail(st, items, '5', links=links,
                                                                     title='Puntos — detalle')
        story += annex_marked(st)
    doc.build(story, onFirstPage=page_decor, onLaterPages=page_decor)
    print(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--scope', choices=['gestamp', 'mejoras', 'both'], default='both',
                    help='gestamp, mejoras or both (default: the two reports)')
    ap.add_argument('--out', help='output file (default: dated file in dist/); needs a single --scope')
    ap.add_argument('--items', default=os.path.join(REPO, 'docs', 'open_items.json'))
    args = ap.parse_args()
    if args.out and args.scope == 'both':
        ap.error('--out needs --scope gestamp or mejoras')
    import naming
    when = naming.now()
    fonts()
    data = json.load(open(args.items)) if os.path.exists(args.items) else {}
    now = naming.human(when)
    if args.out:
        build(args.scope, args.out, data, now)
        return
    dist = os.path.join(REPO, 'dist')
    for scope in (['gestamp', 'mejoras'] if args.scope == 'both' else [args.scope]):
        prefix = scopes.SCOPES[scope]['pdf']
        out = naming.dated_path(dist, prefix, '.pdf', when)
        build(scope, out, data, now)
        for old in naming.remove_older(out, prefix, '.pdf'):
            print('removed', old)
    if args.scope == 'both':
        # the single report of before 2026-10-12
        for old in naming.remove_older(os.path.join(dist, 'x.pdf'), scopes.OLD['pdf'], '.pdf'):
            print('removed', old)


if __name__ == '__main__':
    main()
