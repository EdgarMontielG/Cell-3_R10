#!/usr/bin/env python3
"""Write the programmer's instruction PDF of a delivery folder (entregas/<date>_<items>/).

    python3 tools/make_delivery_pdf.py entregas/2026-10-11_F52_medicion

The text lives in <folder>/instrucciones.json, so each delivery only writes its
content; the look is the one of make_report.py. Inline markup in any text:
`code` (mono) and **bold**. Blocks: {"p": text}, {"lista": [..]},
{"pasos": [..], "desde": n}, {"codigo": text}, {"tabla": {"anchos_mm": [..], "filas": [[..]]}}.
A table cell "[ ]" prints an empty check box.
"""
import json
import os
import re
import sys

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.platypus import KeepTogether, Paragraph, Preformatted, SimpleDocTemplate, Spacer, Table, TableStyle

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_report as mr  # noqa: E402  (fonts, styles, table, colors)

BOX = '☐'


def markup(text):
    text = mr.esc(text)
    text = re.sub(r'`([^`]+)`', r'<font name="Mono">\1</font>', text)
    return re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', text)


def block(b, st):
    if 'p' in b:
        return [Paragraph(markup(b['p']), st['body'])]
    if 'lista' in b:
        return [Paragraph(markup(i), st['bullet'], bulletText='•') for i in b['lista']]
    if 'pasos' in b:
        first = b.get('desde', 1)   # numbering continues after a code block
        return [Paragraph(markup(i), st['bullet'], bulletText=f'{n}.') for n, i in enumerate(b['pasos'], first)]
    if 'codigo' in b:
        t = Table([[Preformatted(b['codigo'], st['code'])]], colWidths=[180 * mm])
        t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), mr.HEAD_BG),
                               ('LEFTPADDING', (0, 0), (-1, -1), 5), ('TOPPADDING', (0, 0), (-1, -1), 4),
                               ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]))
        return [Spacer(1, 2), t, Spacer(1, 4)]
    if 'tabla' in b:
        rows = []
        for r, row in enumerate(b['tabla']['filas']):
            style = st['cellb'] if r == 0 else st['cell']
            rows.append([Paragraph(BOX if c == '[ ]' else markup(c), style) for c in row])
        return [mr.table(rows, [w * mm for w in b['tabla']['anchos_mm']], st), Spacer(1, 4)]
    raise ValueError(f'unknown block {b}')


def main():
    folder = sys.argv[1]
    spec = json.load(open(os.path.join(folder, 'instrucciones.json'), encoding='utf-8'))
    mr.fonts()
    st = mr.styles()
    out = os.path.join(folder, spec['archivo'])
    footer = spec['pie']

    def decor(canvas, doc):
        canvas.saveState()
        canvas.setFont('Sans', 7)
        canvas.setFillColor(mr.MUTED)
        canvas.drawString(18 * mm, 10 * mm, footer)
        canvas.drawRightString(letter[0] - 18 * mm, 10 * mm, f'Página {doc.page}')
        canvas.restoreState()

    story = [Paragraph(markup(spec['titulo']), st['title']), Spacer(1, 2),
             Paragraph(markup(spec['subtitulo']), st['subtitle']), Spacer(1, 8)]
    for b in spec.get('intro', []):
        story += block(b, st)
    for sec in spec['secciones']:
        body = [f for b in sec['bloques'] for f in block(b, st)]
        # The heading never stays alone at the bottom of a page
        story.append(KeepTogether([Paragraph(markup(sec['titulo']), st['h1'])] + body[:1]))
        story += body[1:]
    doc = SimpleDocTemplate(out, pagesize=letter, leftMargin=16 * mm, rightMargin=16 * mm,
                            topMargin=15 * mm, bottomMargin=16 * mm, title=spec['titulo'],
                            author='Ethos Automation México')
    doc.build(story, onFirstPage=decor, onLaterPages=decor)
    print(out)


if __name__ == '__main__':
    main()
