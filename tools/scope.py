"""The two lists handed out since 2026-10-12 (Edgar's decision).

  gestamp   G01-G22, the points of Gestamp's review: what the customer audits
            for the buy-off. R10_Gestamp_Puntos_*.xlsx, R10_Gestamp_reporte_*.pdf.
  mejoras   the Fnn/Cnn items of Ethos' review: process improvements, not a
            condition of the buy-off. R10_Mejoras_Puntos_*.xlsx,
            R10_Mejoras_reporte_*.pdf.

Every item is in exactly one list (by its ID), so the programmer fills it in
one workbook only. A Gestamp point whose closing criterion is "se cumplen los
criterios de F43" carries F43's criteria inline in the Gestamp list; F43 says
in the improvement list which open Gestamp points it counts for.
"""
import re

SCOPES = {
    'gestamp': {'xlsx': 'R10_Gestamp_Puntos', 'pdf': 'R10_Gestamp_reporte',
                'title': 'Puntos de Gestamp para el buy off'},
    'mejoras': {'xlsx': 'R10_Mejoras_Puntos', 'pdf': 'R10_Mejoras_reporte',
                'title': 'Mejoras de proceso (puntos de Ethos)'},
}
# Names used before the split; the generators remove these copies from dist/.
OLD = {'xlsx': 'R10_Puntos_Abiertos', 'pdf': 'R10_reporte'}

CLOSED = ('Cerrado', 'No aplica', 'Aceptado sin cambio', 'Sin acción', 'Se cierra con otro punto')
REF = re.compile(r'criterios de ((?:[FC]\d\d)(?:(?:\s*,\s*|\s+y\s+)[FC]\d\d)*)')


def is_gestamp(item):
    return item['id'].startswith('G')


def is_closed(item):
    return item.get('estado', '').startswith(CLOSED)


def select(items, scope):
    return [i for i in items if is_gestamp(i) == (scope == 'gestamp')]


def criteria_refs(item):
    """IDs whose closing criteria are part of this item's ('se cumplen los criterios de F38 y F14')."""
    out = []
    for c in item.get('criterio_cierre', []):
        for m in REF.finditer(c):
            out += [r for r in re.findall(r'[FC]\d\d', m.group(1)) if r not in out]
    return out


def expanded_criteria(item, by_id):
    """[(False, criterion)] of the item, each 'se cumplen los criterios de X' followed by
    [(True, 'X: criterion of X')]."""
    out = []
    for c in item.get('criterio_cierre', []):
        out.append((False, c))
        for m in REF.finditer(c):
            for ref in re.findall(r'[FC]\d\d', m.group(1)):
                if ref in by_id:
                    out += [(True, f'{ref}: {sub}') for sub in by_id[ref].get('criterio_cierre', [])]
    return out


def related(item, by_id):
    """The Ethos items an open Gestamp point depends on or takes its criteria from, in order."""
    ids = list(item.get('depende_de', []))
    ids += [r for r in criteria_refs(item) if r not in ids]
    return [r for r in ids if r in by_id and not r.startswith('G')]


def gestamp_links(items):
    """{Ethos item ID: [open Gestamp points that depend on it]}."""
    by_id = {i['id']: i for i in items}
    out = {}
    for g in items:
        if is_gestamp(g) and not is_closed(g):
            for r in related(g, by_id):
                out.setdefault(r, []).append(g['id'])
    return out


def with_state(ids, by_id):
    return ', '.join(f"{r} ({by_id[r].get('estado', '')})" for r in ids if r in by_id)
