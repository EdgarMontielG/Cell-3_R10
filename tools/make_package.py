#!/usr/bin/env python3
"""Build the program package the cell programmer loads through WorkVisual.

    python3 tools/make_package.py ROBOT_BACKUP.zip BUILT_ARCHIVE.zip [OUT_DIR]

ROBOT_BACKUP.zip is the audited backup of what runs on the robot now;
BUILT_ARCHIVE.zip is what tools/build_archive.py made from it (the repository
version). The package holds only what differs between the two, so the
programmer replaces files instead of restoring a whole archive:

  - every file whose content differs, and every file the robot does not have
    yet, under its path on the controller (KRC/R1/...);
  - LEEME.txt: the backup it is based on, the repository version, the file
    lists, and the files to delete on the robot (deleted or moved modules -
    WorkVisual and a restore do not delete them).

Names are compared without case, as on the controller. Default OUT_DIR is
dist/; the package is named R10_paquete_<YYYY-MM-DD_HHMM>.zip (central Mexico
time, tools/naming.py).
"""
import configparser
import io
import os
import subprocess
import sys
import zipfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def am_ini(z):
    name = next((n for n in z.namelist() if n.lower() == 'am.ini'), None)
    if not name:
        return '?'
    cp = configparser.ConfigParser(strict=False)
    cp.read_string(z.read(name).decode('latin-1'))
    return f"{cp.get('Archive', 'Date', fallback='?')}, robot {cp.get('Roboter', 'RobName', fallback='?')}"


def main():
    if len(sys.argv) not in (3, 4):
        sys.exit(__doc__)
    robot, built = (os.path.abspath(p) for p in sys.argv[1:3])
    out_dir = os.path.abspath(sys.argv[3]) if len(sys.argv) == 4 else os.path.join(REPO, 'dist')
    sys.path.insert(0, os.path.join(REPO, 'tools'))
    import naming
    when = naming.now()
    out = naming.dated_path(out_dir, 'R10_paquete', '.zip', when)
    head = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], cwd=REPO, capture_output=True,
                          text=True).stdout.strip()

    with zipfile.ZipFile(robot) as a, zipfile.ZipFile(built) as b:
        on_robot = {n.lower(): n for n in a.namelist() if not n.endswith('/')}
        in_build = {n.lower(): n for n in b.namelist() if not n.endswith('/')}
        skip = ('log files/',)
        replace, add = [], []
        for low, name in sorted(in_build.items()):
            if low.startswith(skip):
                continue
            if low not in on_robot:
                add.append(name)
            elif a.read(on_robot[low]) != b.read(name):
                replace.append(name)
        delete = sorted(name for low, name in on_robot.items()
                        if low not in in_build and not low.startswith(skip))
        folders = sorted({os.path.dirname(n) for n in delete}
                         - {os.path.dirname(n) for n in in_build.values()})

        text = io.StringIO()
        text.write(f'Paquete R10 (BMW-03-10-R1) - {naming.human(when)}\n')
        text.write(f'Basado en el respaldo del robot: {os.path.basename(robot)} ({am_ini(a)})\n')
        text.write(f'Version del repositorio: {head}\n\n')
        text.write(f'REEMPLAZAR ({len(replace)})\n')
        text.writelines(f'  {n}\n' for n in replace)
        text.write(f'\nAGREGAR ({len(add)}) - modulos nuevos que llaman los demas: sin ellos no compila\n')
        text.writelines(f'  {n}\n' for n in add)
        text.write(f'\nBORRAR EN EL ROBOT ({len(delete)}) - WorkVisual no los borra. Quitarlos en el mismo\n'
                   '  deploy: si quedan, no compila (modulos con el mismo nombre, senales renombradas).\n')
        text.writelines(f'  {n}\n' for n in delete)
        if folders:
            text.write('\nCARPETAS QUE QUEDAN VACIAS (borrarlas)\n')
            text.writelines(f'  {f}/\n' for f in folders)

        os.makedirs(out_dir, exist_ok=True)
        with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
            for name in replace + add:
                info = b.getinfo(name)
                z.writestr(zipfile.ZipInfo(name, date_time=info.date_time), b.read(name),
                           zipfile.ZIP_DEFLATED)
            z.writestr('LEEME.txt', text.getvalue().replace('\n', '\r\n'))
    for old in naming.remove_older(out, 'R10_paquete', '.zip'):
        print('removed', old)
    print(f'{out}: {len(replace)} replace, {len(add)} add, {len(delete)} delete')


if __name__ == '__main__':
    main()
