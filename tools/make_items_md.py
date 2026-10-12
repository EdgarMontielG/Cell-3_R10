#!/usr/bin/env python3
"""Write docs/OPEN_ITEMS.es.md, the readable view of docs/open_items.json.

    python3 tools/make_items_md.py

Same layout as the sister project's OPEN_QUESTIONS: a summary table, closed
items struck through, then one section per item. Regenerate it after every
audit; never edit OPEN_ITEMS.es.md by hand.
"""
import json
import os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLOSED = ('Cerrado', 'No aplica', 'Aceptado sin cambio', 'Sin acción', 'Se cierra con otro punto')


def closed(item):
    return item.get('estado', '').startswith(CLOSED)


def main():
    data = json.load(open(os.path.join(REPO, 'docs', 'open_items.json')))
    items = data['items']
    pending = [i for i in items if not closed(i)]
    gestamp = [i for i in items if i['id'].startswith('G')]
    out = ['# Puntos abiertos — robot R10 (BMW-03-10-R1)', '',
           '*Archivo generado por `tools/make_items_md.py` a partir de `docs/open_items.json` — '
           'no se edita a mano.*', '',
           f"Actualizado: {data.get('actualizado', '')}. Pendientes: **{len(pending)}** de {len(items)}. "
           'El detalle técnico de cada punto (en inglés, para Gestamp) está en '
           '[FINDINGS.md](FINDINGS.md); el proceso en [PROCESO.es.md](PROCESO.es.md).', '',
           f"**Puntos de Gestamp (G01–G{len(gestamp):02d})**: revisión de Gestamp del 2026-10-02 (BMW-03-10R1), "
           'con su texto original. Desde el 2026-10-11 la base es el programa del programador: cada punto se '
           'revisa contra su programa y la versión de oficina queda como referencia (nota de cada punto). '
           'Los Fnn/Cnn son de la revisión de Ethos (numeración del R20); los marcados "Calvin #n" también están '
           'en la lista de Calvin (2026-10-03), verificada punto por punto. Esta lista es la única que se usa.', '',
           'Desde el 2026-10-12 se entregan dos juegos de Excel y PDF: **Gestamp** (G01–G22 y los puntos de Ethos '
           'que su criterio de cierre requiere, marcados "para Gnn"; es lo que Gestamp audita para el buy-off) y '
           '**mejora de proceso** (los demás; no son condición del buy-off).', '',
           '## Resumen — puntos de Gestamp', '',
           '| ID | Gestamp | Punto | Sev. | Responsable | Estado | Ver |',
           '|---|---|---|---|---|---|---|']
    def row(i, gest):
        title = f"~~{i['titulo']}~~" if closed(i) else i['titulo']
        state = f"**{i.get('estado', '')}**" if not closed(i) else i.get('estado', '')
        if gest:
            return (f"| {i['id']} | {i.get('texto_gestamp', '')} | {title} | {i['severidad']} | "
                    f"{i['responsable']} | {state} | {', '.join(i.get('depende_de', []))} |")
        if i.get('origen_ref'):
            title += f" ({i['origen_ref']})"
        if i.get('requerido_por'):
            title += f" — **para {', '.join(i['requerido_por'])}**"
        return f"| {i['id']} | {title} | {i['severidad']} | {i['responsable']} | {state} |"
    out += [row(i, True) for i in gestamp] + ['', '## Resumen — puntos de Ethos', '',
                                               '| ID | Punto | Sev. | Responsable | Estado |',
                                               '|---|---|---|---|---|']
    out += [row(i, False) for i in items if not i['id'].startswith('G')]
    out.append('')
    for i in items:
        out += ['---', '', f"## {i['id']} — {i['titulo']}", '']
        if i.get('texto_gestamp'):
            out += [f"**Origen:** {i.get('origen', '')}. Texto de Gestamp: *\"{i['texto_gestamp']}\"*", '']
        elif i.get('origen_ref'):
            out += [f"**Origen:** {i.get('origen', '')}.", '']
        out += [f"**Severidad:** {i['severidad']} · **Tipo:** {i['tipo']} · "
                f"**Responsable:** {i['responsable']} · **Estado:** {i.get('estado', '')}", '']
        if i.get('modulos'):
            out += ['**Módulos:** ' + ', '.join(f'`{m}`' for m in i['modulos']), '']
        out += [f"**Qué está mal.** {i['que_esta_mal']}", '', f"**Qué hacer.** {i['que_hacer']}", '']
        if i.get('criterio_cierre'):
            out += ['**Criterio de cierre** (se verifica en el respaldo):', '']
            out += [f'* {c}' for c in i['criterio_cierre']] + ['']
        if i.get('evidencia_programador'):
            out += [f"**Evidencia del programador.** {i['evidencia_programador']}", '']
        if i.get('depende_de'):
            out += ['**Depende de / se cierra con:** ' + ', '.join(i['depende_de']), '']
        if i.get('nota'):
            out += [f"**Nota.** {i['nota']}", '']
        if i.get('historial'):
            out += ['**Historial:**', '']
            out += [f"* {h.get('fecha', '')} — {h.get('resultado', '')}: {h.get('nota', '')}"
                    for h in i['historial']] + ['']
    path = os.path.join(REPO, 'docs', 'OPEN_ITEMS.es.md')
    open(path, 'w').write('\n'.join(out))
    print(path)


if __name__ == '__main__':
    main()
