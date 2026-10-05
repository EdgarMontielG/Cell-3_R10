#!/usr/bin/env python3
"""Build the programmer's open-items workbook from docs/open_items.json.

    python3 tools/make_items_xlsx.py [--out FILE.xlsx]

By default it writes dist/R10_Puntos_Abiertos_<YYYY-MM-DD_HHMM>.xlsx (date and
time of central Mexico, tools/naming.py) and removes the older copies in
dist/.

docs/open_items.json is the master list (kept in the repository and updated
after every audit). The workbook is the working copy the robot programmer
fills in during the day and sends back with the robot backup:

  Puntos abiertos   one row per item. Yellow columns are the programmer's;
                    grey columns are written by the audit.
  Resumen           counts by status and severity (formulas).
  Instrucciones     how to fill it in, with one example row.
  Historial         one row per audit.

tools/audit_backup.py --items reads the 'Puntos abiertos' sheet by header
text, so the header names below are part of the interface.
"""
import argparse
import json
import os
import sys

from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATES = ['Abierto', 'Requiere decisión', 'Corregido en oficina - probar en celda', 'En proceso',
          'Corregido - por auditar', 'Cerrado - auditado', 'Reabierto', 'Aceptado sin cambio',
          'Cerrado - depuración', 'No aplica', 'Sin acción - documentado', 'Se cierra con otro punto']
PENDING = ['Abierto', 'Requiere decisión', 'Corregido en oficina - probar en celda', 'En proceso',
           'Corregido - por auditar', 'Reabierto']
PROGRAMMER_STATES = ['En proceso', 'Corregido - por auditar']
# Closed: nothing is left to do. These rows are green, critical or not.
CLOSED = ['Cerrado - auditado', 'Cerrado - depuración', 'Aceptado sin cambio', 'No aplica',
          'Sin acción - documentado']
SEVERITIES = ['Crítico', 'Alto', 'Medio', 'Bajo', '-']

# (header, width, owner) - owner: 'item' fixed text, 'prog' programmer input, 'audit' auditor.
COLUMNS = [
    ('ID', 6, 'item'), ('Origen', 11, 'item'), ('Sev.', 8, 'item'), ('Punto', 46, 'item'),
    ('Tipo', 18, 'item'),
    ('Responsable', 18, 'item'), ('Módulos', 28, 'item'), ('Criterio de cierre', 70, 'item'),
    ('Depende de', 12, 'item'),
    ('Estado', 22, 'prog'), ('Qué cambió el programador', 50, 'prog'),
    ('Módulos modificados', 28, 'prog'), ('Evidencia / prueba en celda', 40, 'prog'),
    ('Fecha programador', 13, 'prog'),
    ('Resultado auditoría', 20, 'audit'), ('Fecha auditoría', 13, 'audit'),
    ('Nota auditoría', 50, 'audit'),
]

FONT = 'Arial'
THIN = Side(style='thin', color='CBD2D9')
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
HEAD = PatternFill('solid', fgColor='1D4E89')
PROG = PatternFill('solid', fgColor='FFF4C2')
AUDIT = PatternFill('solid', fgColor='E4E7EB')
SEV_COLOR = {'Crítico': 'B42318', 'Alto': 'C4561D', 'Medio': 'A16207', 'Bajo': '52606D', '-': '9AA5B1'}
GESTAMP = PatternFill('solid', fgColor='DCEBFA')
DONE = PatternFill('solid', fgColor='C6EFCE')


def is_gestamp(item):
    return item['id'].startswith('G')


def origin_text(item):
    if is_gestamp(item):
        return f"Gestamp #{int(item['id'][1:])}"
    return item.get('origen_ref') or 'Ethos'


def title_text(item):
    if item.get('texto_gestamp'):
        return f"{item['titulo']}\nGestamp: \"{item['texto_gestamp']}\""
    return item['titulo']


def criteria_text(item):
    return '\n'.join('• ' + c for c in item.get('criterio_cierre', []))


def items_sheet(ws, items):
    ws.title = 'Puntos abiertos'
    for col, (head, width, owner) in enumerate(COLUMNS, 1):
        c = ws.cell(row=1, column=col, value=head)
        c.font = Font(name=FONT, bold=True, color='FFFFFF', size=9)
        c.fill = HEAD
        c.alignment = Alignment(wrap_text=True, vertical='center')
        c.border = BORDER
        ws.column_dimensions[get_column_letter(col)].width = width
    status_col = [h for h, _, _ in COLUMNS].index('Estado') + 1
    ws.cell(row=1, column=status_col).comment = Comment(
        'El programador solo pone En proceso o Corregido - por auditar. '
        'Cerrado lo pone la auditoría.', 'Ethos')
    for r, it in enumerate(items, 2):
        audit = (it.get('historial') or [{}])[-1]
        values = [it['id'], origin_text(it), it['severidad'], title_text(it), it['tipo'], it['responsable'],
                  ', '.join(it.get('modulos', [])), criteria_text(it), ', '.join(it.get('depende_de', [])),
                  it.get('estado', 'Abierto'), it.get('nota_programador', ''),
                  it.get('modulos_modificados', ''), it.get('evidencia', ''), it.get('fecha_programador', ''),
                  audit.get('resultado', ''), audit.get('fecha', ''), audit.get('nota', '')]
        for col, ((head, _, owner), v) in enumerate(zip(COLUMNS, values), 1):
            c = ws.cell(row=r, column=col, value=v)
            c.font = Font(name=FONT, size=9, bold=(head == 'ID'),
                          color=SEV_COLOR.get(v, '1F2933') if head == 'Sev.' else '1F2933')
            c.alignment = Alignment(wrap_text=True, vertical='top')
            c.border = BORDER
            if it.get('estado') in CLOSED:
                c.fill = DONE
            elif owner == 'prog':
                c.fill = PROG
            elif owner == 'audit':
                c.fill = AUDIT
            elif is_gestamp(it) and head in ('ID', 'Origen', 'Punto'):
                c.fill = GESTAMP
    last = len(items) + 1
    dv = DataValidation(type='list', formula1='"' + ','.join(STATES) + '"', allow_blank=False,
                        showErrorMessage=True, errorTitle='Estado',
                        error='Elige un estado de la lista (hoja Instrucciones).')
    ws.add_data_validation(dv)
    status = get_column_letter(status_col)
    dv.add(f'{status}2:{status}{last}')
    # The row also turns green when the auditor sets a closed state in the workbook.
    cond = ' , '.join(f'${status}2="{st}"' for st in CLOSED).replace(' , ', ',')
    ws.conditional_formatting.add(f'A2:{get_column_letter(len(COLUMNS))}{last}',
                                  FormulaRule(formula=[f'OR({cond})'], fill=DONE, stopIfTrue=True))
    ws.freeze_panes = 'D2'
    ws.auto_filter.ref = f'A1:{get_column_letter(len(COLUMNS))}{last}'
    ws.sheet_view.zoomScale = 90


def summary_sheet(ws, n, status_col, generated):
    ws.title = 'Resumen'
    ws['A1'] = 'Resumen de puntos abiertos'
    ws['A1'].font = Font(name=FONT, bold=True, size=12, color='1D4E89')
    ws['A2'] = f'Generado {generated}'
    ws['A2'].font = Font(name=FONT, size=8, italic=True, color='616E7C')
    ws['A3'], ws['B3'] = 'Estado', 'Puntos'
    for col in ('A3', 'B3'):
        ws[col].font = Font(name=FONT, bold=True, size=9)
        ws[col].fill = AUDIT
    col = get_column_letter(status_col)
    rng = f"'Puntos abiertos'!${col}$2:${col}${n + 1}"
    for r, s in enumerate(STATES, 4):
        ws.cell(row=r, column=1, value=s).font = Font(name=FONT, size=9)
        c = ws.cell(row=r, column=2, value=f'=COUNTIF({rng},A{r})')
        c.font = Font(name=FONT, size=9)
    tot = 4 + len(STATES)
    ws.cell(row=tot, column=1, value='Total').font = Font(name=FONT, bold=True, size=9)
    ws.cell(row=tot, column=2, value=f'=SUM(B4:B{tot - 1})').font = Font(name=FONT, bold=True, size=9)

    top = tot + 2
    ws.cell(row=top, column=1, value='Severidad').font = Font(name=FONT, bold=True, size=9)
    ws.cell(row=top, column=2, value='Total').font = Font(name=FONT, bold=True, size=9)
    ws.cell(row=top, column=3, value='Pendientes').font = Font(name=FONT, bold=True, size=9)
    for col in range(1, 4):
        ws.cell(row=top, column=col).fill = AUDIT
    sev_col = get_column_letter([h for h, _, _ in COLUMNS].index('Sev.') + 1)
    sev = f"'Puntos abiertos'!${sev_col}$2:${sev_col}${n + 1}"
    for r, s in enumerate(SEVERITIES[:-1], top + 1):
        ws.cell(row=r, column=1, value=s).font = Font(name=FONT, size=9)
        ws.cell(row=r, column=2, value=f'=COUNTIF({sev},A{r})').font = Font(name=FONT, size=9)
        parts = '+'.join(f'COUNTIFS({sev},A{r},{rng},"{p}")' for p in PENDING)
        ws.cell(row=r, column=3, value='=' + parts).font = Font(name=FONT, size=9)
    org_col = get_column_letter([h for h, _, _ in COLUMNS].index('Origen') + 1)
    org = f"'Puntos abiertos'!${org_col}$2:${org_col}${n + 1}"
    gtop = top + len(SEVERITIES) + 1
    ws.cell(row=gtop, column=1, value='Origen').font = Font(name=FONT, bold=True, size=9)
    ws.cell(row=gtop, column=2, value='Total').font = Font(name=FONT, bold=True, size=9)
    ws.cell(row=gtop, column=3, value='Pendientes').font = Font(name=FONT, bold=True, size=9)
    for col in range(1, 4):
        ws.cell(row=gtop, column=col).fill = AUDIT
    for r, (label, pat) in enumerate([('Gestamp', 'Gestamp*'), ('Ethos', 'Ethos'), ('Calvin (Ethos)', 'Calvin*')],
                                     gtop + 1):
        ws.cell(row=r, column=1, value=label).font = Font(name=FONT, size=9)
        ws.cell(row=r, column=2, value=f'=COUNTIF({org},"{pat}")').font = Font(name=FONT, size=9)
        parts = '+'.join(f'COUNTIFS({org},"{pat}",{rng},"{p}")' for p in PENDING)
        ws.cell(row=r, column=3, value='=' + parts).font = Font(name=FONT, size=9)
    note = gtop + 5
    ws.cell(row=note, column=1, value='Pendientes = ' + ', '.join(PENDING) + '.').font = \
        Font(name=FONT, size=8, italic=True, color='616E7C')
    ws.column_dimensions['A'].width = 34
    ws.column_dimensions['B'].width = 10
    ws.column_dimensions['C'].width = 12


def instructions_sheet(ws):
    ws.title = 'Instrucciones'
    rows = [
        ('Cómo usar esta lista', True),
        ('1. Trabaja los puntos en el programa del robot. Respeta docs/CONVENTIONS.md del repositorio: '
         'comentarios en inglés con la señal nombrada ($OUT[n] nombre), sin código comentado, sin reabrir '
         'inline forms que tengan líneas escritas a mano.', False),
        ('2. En la hoja "Puntos abiertos" llena SOLO las columnas amarillas de los puntos que trabajaste: '
         'Estado, Qué cambió el programador, Módulos modificados, Evidencia / prueba en celda, Fecha '
         'programador.', False),
        ('3. Estado: pon "En proceso" si empezaste y no está listo, o "Corregido - por auditar" si el '
         'cambio está hecho y probado (también los "Corregido en oficina" después de probarlos en celda). '
         'No pongas Cerrado: lo pone la auditoría.', False),
        ('4. La evidencia es lo que pide el criterio de cierre: prueba en celda con fecha y resultado, '
         'valor leído en el smartPAD, documento de Gestamp. Sin evidencia el punto se reabre.', False),
        ('5. Al final del día saca un respaldo completo del robot (Archive → All), nómbralo '
         '658424_AAAA-MM-DD_HHMM.zip con la hora en que lo sacaste, y envíalo junto con este archivo '
         'guardado como R10_Puntos_Abiertos_AAAA-MM-DD_HHMM.xlsx. No borres filas ni cambies las columnas '
         'blancas o grises.', False),
        ('', False),
        ('Ejemplo de una fila llenada (formato esperado)', True),
        ('Estado: Corregido - por auditar', False),
        ('Qué cambió el programador: style1app1opt1..3: espera supervisada antes del LIN de aproximación '
         '(gun open LPT > 120000, $IN[466], $IN[482], NOT $IN[470]) con $TIMER[16] 3 s, mensaje y '
         'do004ProcessFault. PRELOAD paso 20 ahora espera $IN[482].', False),
        ('Módulos modificados: style1app1opt1.src ... style1app1opt3.src, PRELOAD.src', False),
        ('Evidencia / prueba en celda: 2026-10-06, T1 50 %: clamp cerrado a mano, el robot se detuvo '
         'antes de P22 con mensaje; con todo abierto el ciclo siguió normal. 3 ciclos en automático OK.', False),
        ('Fecha programador: 2026-10-06', False),
        ('', False),
        ('Puntos de Gestamp', True),
        ('Los puntos G01 a G22 vienen de la revisión de Gestamp del 2026-10-02 (BMW-03-10R1): columna Origen '
         '"Gestamp #n", fondo azul y el texto original de Gestamp en la columna Punto. Los Fnn/Cnn son de la revisión '
         'de Ethos y conservan la numeración del R20 (F37 no aplica en el R10; F44 a F49 son solo del R10; F48 y F49 salieron de la auditoría del 2026-10-05). La lista '
         'de Calvin se verificó punto por punto: los puntos que él también señaló dicen "Calvin #n" en Origen. Esta '
         'lista es la única que se usa.', False),
        ('"Corregido en oficina - probar en celda": Ethos ya cambió el programa en la versión que se entrega. Carga esa '
         'versión, haz la prueba que pide el criterio de cierre y pon "Corregido - por auditar" con la evidencia; si '
         'la prueba falla, pon "En proceso" y explica qué pasó.', False),
        ('Fila en verde: punto cerrado (Cerrado - auditado, Cerrado - depuración, Aceptado sin cambio, No aplica, '
         'Sin acción - documentado), aunque sea crítico. No hay nada que hacer en esas filas.', False),
        ('', False),
        ('Estados', True),
    ]
    meaning = {
        'Abierto': 'Pendiente de trabajar.',
        'Requiere decisión': 'Falta información o decisión (Gestamp, seguridad, Ethos) antes de programar.',
        'Corregido en oficina - probar en celda': 'Ethos lo cambió en la versión entregada; falta la prueba en celda '
                                                  'del programador.',
        'En proceso': 'Lo pone el programador: trabajo empezado.',
        'Corregido - por auditar': 'Lo pone el programador: cambio hecho y probado, pide auditoría.',
        'Cerrado - auditado': 'Lo pone la auditoría: cumple el criterio de cierre en el respaldo.',
        'Reabierto': 'Lo pone la auditoría: no se encontró el cambio o no cumple (ver Nota auditoría).',
        'Aceptado sin cambio': 'Ethos / Gestamp decidieron no corregir; queda la razón.',
        'Cerrado - depuración': 'Resuelto por la depuración del 2026-10-04.',
        'No aplica': 'El punto ya cumple.',
        'Sin acción - documentado': 'Se deja como está; la nota dice cuándo se reabriría.',
        'Se cierra con otro punto': 'Duplica otro punto (columna Depende de); se cierra con él.',
    }
    r = 1
    for text, bold in rows:
        c = ws.cell(row=r, column=1, value=text)
        c.font = Font(name=FONT, size=10 if bold else 9, bold=bold, color='1D4E89' if bold else '1F2933')
        c.alignment = Alignment(wrap_text=True, vertical='top')
        r += 1
    for s in STATES:
        ws.cell(row=r, column=1, value=f'{s}: {meaning[s]}').font = Font(name=FONT, size=9)
        r += 1
    r += 1
    ws.cell(row=r, column=1, value='Colores: amarillo = lo llena el programador; gris = lo llena la '
                                   'auditoría; blanco = no se edita.').font = Font(name=FONT, size=9,
                                                                                    italic=True)
    ws.column_dimensions['A'].width = 120


def history_sheet(ws, audits):
    ws.title = 'Historial'
    heads = ['Fecha auditoría', 'Respaldo', 'Cerrados', 'Reabiertos', 'Cambios de código', 'Notas']
    for col, h in enumerate(heads, 1):
        c = ws.cell(row=1, column=col, value=h)
        c.font = Font(name=FONT, bold=True, size=9, color='FFFFFF')
        c.fill = HEAD
    for r, a in enumerate(audits, 2):
        for col, key in enumerate(['fecha', 'respaldo', 'cerrados', 'reabiertos', 'cambios', 'notas'], 1):
            ws.cell(row=r, column=col, value=a.get(key, '')).font = Font(name=FONT, size=9)
    for col, w in enumerate([14, 30, 10, 10, 16, 80], 1):
        ws.column_dimensions[get_column_letter(col)].width = w


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--items', default=os.path.join(REPO, 'docs', 'open_items.json'))
    ap.add_argument('--out', help='output file (default: dated file in dist/)')
    args = ap.parse_args()
    sys.path.insert(0, os.path.join(REPO, 'tools'))
    import naming
    when = naming.now()
    default = args.out is None
    if default:
        args.out = naming.dated_path(os.path.join(REPO, 'dist'), 'R10_Puntos_Abiertos', '.xlsx', when)
    data = json.load(open(args.items))
    items = data['items']
    wb = Workbook()
    items_sheet(wb.active, items)
    summary_sheet(wb.create_sheet(), len(items), [h for h, _, _ in COLUMNS].index('Estado') + 1,
                  naming.human(when))
    instructions_sheet(wb.create_sheet())
    history_sheet(wb.create_sheet(), data.get('auditorias', []))
    # The summary sheet is formulas only: have Excel compute them when the file opens.
    from openpyxl.workbook.properties import CalcProperties
    wb.calculation = CalcProperties(fullCalcOnLoad=True)
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    wb.save(args.out)
    if default:
        for old in naming.remove_older(args.out, 'R10_Puntos_Abiertos', '.xlsx'):
            print('removed', old)
    print(args.out)


if __name__ == '__main__':
    main()
