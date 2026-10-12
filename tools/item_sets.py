"""Which open items go to which deliverable (Edgar, 2026-10-12).

Two Excel workbooks and two PDF reports are handed out:

  gestamp  The Gestamp review items G01-G22, plus the Ethos items that a
           Gestamp item's closure criterion requires (field "requerido_por"
           in docs/open_items.json). This is what the customer audits for the
           buy-off: the priority.
  mejora   Every other item: process improvement found by Ethos. Not a
           condition for the buy-off.

Every item in docs/open_items.json carries "conjunto": "gestamp" | "mejora";
an item without it is classified by its ID (Gnn -> gestamp).
"""
SETS = {
    'gestamp': {
        'label': 'Puntos de Gestamp para el buy-off',
        'short': 'Puntos de Gestamp (buy-off)',
        'xlsx': 'R10_Gestamp_Puntos',
        'pdf': 'R10_Gestamp_reporte',
    },
    'mejora': {
        'label': 'Puntos de mejora de proceso (no son condición del buy-off)',
        'short': 'Mejora de proceso',
        'xlsx': 'R10_Mejora_Puntos',
        'pdf': 'R10_Mejora_reporte',
    },
}
# The single files written before 2026-10-12, removed when the split ones are written
OLD_PREFIXES = {'xlsx': 'R10_Puntos_Abiertos', 'pdf': 'R10_reporte'}


def set_of(item):
    return item.get('conjunto') or ('gestamp' if item['id'].startswith('G') else 'mejora')


def select(items, name):
    return [i for i in items if set_of(i) == name]
