#!/usr/bin/env python3
"""Cycle times of the nut weld, from the measurement of CL_CYCLE_TIME (F52).

    python3 tools/cycle_times.py ROBOT_BACKUP.zip | CL_CYCLE_TIME.dat

The controller keeps in CL_CYCLE_TIME.dat the last 10 cycles of each nut:
CL_T_LOG[nut,row,step] = ms from the robot stopped at the wait point of the
weld app to each step (step list in the .dat; -1 = not reached). A backup
taken after the robot ran carries them. This prints, per nut, the average,
minimum and maximum of each segment over the complete cycles (step 13
reached), and the time the robot stands still per part - nut wait plus
CENTERLINE_WELD, the robot motions left out - which is what Gestamp counts
(12 s per part). Output in Spanish (Markdown), for the report to the owner.
"""
import re
import sys
import zipfile

STEPS = 13
ELEM = re.compile(r'^\s*CL_T_LOG\s*\[\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\]\s*=\s*(-?\d+)', re.I | re.M)
# (label, from step, to step); step 0 = the start at the wait point
SEGMENTS = [
    ('Espera de tuerca (robot parado en el punto de espera)', 0, 1),
    ('Entrada al pedestal (robot en movimiento)', 1, 2),
    ('Pedestal listo (pistola, pines, clamp, QFP)', 2, 3),
    ('Bosch ready', 3, 4),
    ('Clamp cerrado', 4, 5),
    ('Pistola cerrada en la ventana', 5, 6),
    ('Bosch ready otra vez', 6, 7),
    ('Presion de intensify OK', 7, 8),
    ('Soldadura (hasta Weld Complete)', 8, 9),
    ('Weld Complete apagado', 9, 10),
    ('Pistola abierta confirmada', 10, 11),
    ('Clamp abierto', 11, 12),
    ('Fin de CENTERLINE_WELD (QFP, salidas)', 12, 13),
]


def read_dat(path):
    if path.lower().endswith('.zip'):
        with zipfile.ZipFile(path) as z:
            name = next((n for n in z.namelist() if n.lower().endswith('/cl_cycle_time.dat')), None)
            if not name:
                sys.exit(f'{path}: no CL_CYCLE_TIME.dat (the measurement is not loaded on this robot)')
            return z.read(name).decode('latin-1')
    with open(path, encoding='latin-1') as f:
        return f.read()


def cycles(text):
    """({nut: [{step: ms}, ...]}, rows left out) of the complete cycles: step 13
    reached and the times never going back (a cycle aborted and restarted by a
    block selection can write its steps into the row of an older one)."""
    log = {}
    for nut, row, step, ms in ELEM.findall(text):
        log.setdefault((int(nut), int(row)), {})[int(step)] = int(ms)
    out, skipped = {}, 0
    for (nut, _), steps in sorted(log.items()):
        t = [steps.get(s, -1) for s in range(1, STEPS + 1)]
        if min(t) >= 0 and all(a <= b for a, b in zip(t, t[1:])):
            out.setdefault(nut, []).append({0: 0, **steps})
        elif any(v >= 0 for v in t):
            skipped += 1
    return out, skipped


def report(text):
    data, skipped = cycles(text)
    if not data:
        return 'Sin ciclos completos registrados en CL_CYCLE_TIME.dat.\n'
    out = []
    if skipped:
        out += [f'Ciclos incompletos o interrumpidos que no se cuentan: {skipped}.', '']

    def row(label, values):
        avg = sum(values) / len(values)
        out.append(f'| {label} | {avg / 1000:.2f} | {min(values) / 1000:.2f} | {max(values) / 1000:.2f} |')

    still_part = []
    for nut in sorted(data):
        cyc = data[nut]
        out += [f'### Tuerca {nut} ({len(cyc)} ciclos completos)', '',
                '| Tramo | Promedio s | Min s | Max s |', '|---|---:|---:|---:|']
        for label, a, b in SEGMENTS:
            row(label, [c[b] - c[a] for c in cyc])
        still = [c[1] + c[13] - c[2] for c in cyc]
        row('**Robot parado (espera + CENTERLINE_WELD)**', still)
        out.append('')
        still_part.append(sum(still) / len(still))
    if len(still_part) == 3:
        out.append(f'**Robot parado por pieza (3 tuercas, promedio): {sum(still_part) / 1000:.1f} s** '
                   '- Gestamp pide 12 s.')
        out.append('')
    return '\n'.join(out)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    print(report(read_dat(sys.argv[1])))


if __name__ == '__main__':
    main()
