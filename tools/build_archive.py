#!/usr/bin/env python3
"""Build a KRC4 archive zip of the cleaned program from the original archive.

    python3 tools/build_archive.py v431_03_10_r1.zip [OUT]

OUT is a directory (default dist/) or a file name. In a directory the archive
is named 658424_R10_<YYYY-MM-DD_HHMM>.zip, with the date and time of central
Mexico (tools/naming.py), so every archive handed to the programmer says when
it was built.

Every entry of the original archive is copied through byte-for-byte with its
original timestamp, except:
  - files this repository changed are replaced by the repository version;
  - files listed as deleted in the cleanup allowlist or in
    tools/code_changes.json are left out;
  - files listed in "moved_files" of tools/code_changes.json are written
    under their new path (with the repository version).
Nothing else is added. The script prints both lists, so the operator knows
exactly what differs from the archive that is running on the robot.

The original archive must be the one this repository was made from (archive
v431_03_10_r1.zip of robot 658424, the first commit). An entry that differs from the first commit means
the robot was changed after that backup: the script refuses to build rather
than overwrite that change with the repository version. Merge first.

Run the two checkers first; this script refuses to build when either fails:
tools/check_cleanup.py --head <base of tools/code_changes.json> (the cleanup
changed only comments) and tools/check_equivalence.py (every later code
change is listed with its items).
"""
import hashlib
import os
import subprocess
import sys
import zipfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def git(*args):
    return subprocess.run(('git',) + args, check=True, capture_output=True).stdout


def blob_id(data):
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


def tree_blobs(ref):
    """{path: blob sha} of every file in commit `ref`."""
    blobs = {}
    for rec in git('ls-tree', '-r', '-z', ref).split(b'\0'):
        if rec:
            meta, path = rec.split(b'\t', 1)
            blobs[path.decode('utf-8', 'surrogateescape')] = meta.split()[2].decode()
    return blobs


def main():
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    # Resolve both paths against the caller's directory before moving to the repo.
    src = os.path.abspath(sys.argv[1])
    dst = os.path.abspath(sys.argv[2]) if len(sys.argv) == 3 else os.path.join(REPO, 'dist')
    if os.path.isdir(dst) or not dst.lower().endswith('.zip'):
        sys.path.insert(0, os.path.join(REPO, 'tools'))
        import naming
        dst = naming.dated_path(dst, '658424_R10', '.zip')
    if os.path.exists(dst) and os.path.samefile(src, dst):
        sys.exit('the output must not overwrite the original archive')
    os.chdir(REPO)
    import json
    changes = json.load(open('tools/code_changes.json'))
    for cmd in (['tools/check_cleanup.py', '--head', changes['base']],
                ['tools/check_equivalence.py']):
        if subprocess.run([sys.executable] + cmd, capture_output=True).returncode != 0:
            sys.exit(f'{" ".join(cmd)} fails - fix that first')
    sys.path.insert(0, os.path.join(REPO, 'tools'))
    from check_cleanup import load_allowlist
    allow, _ = load_allowlist()
    deleted = set(allow['deleted_files']) | set(changes.get('deleted_files', {}))
    moved = changes.get('moved_files', {})
    base = git('rev-list', '--max-parents=0', 'HEAD').decode().split()[0]
    baseline = tree_blobs(base)
    tracked = set(git('ls-files', '-z').decode('utf-8', 'surrogateescape').split('\0'))

    # Only files the repository tracks can be "changed by the repository";
    # anything else in the archive (Log Files/) is copied as it is.
    replaced, dropped, conflicts, local = [], [], [], {}
    with zipfile.ZipFile(src) as zin:
        for info in zin.infolist():
            name = info.filename
            data = zin.read(name)
            if name in tracked and os.path.isfile(name):
                with open(name, 'rb') as f:
                    local[name] = f.read()
            if name in moved:
                with open(moved[name], 'rb') as f:
                    local[name] = f.read()
            changed = name in deleted or name in moved or local.get(name, data) != data
            if changed and baseline.get(name) != blob_id(data):
                conflicts.append(name)
            elif name in deleted:
                dropped.append(name)
            elif changed:
                replaced.append(name)
    if conflicts:
        print('These files of the archive differ from the first commit of this repository')
        print('and would be overwritten or left out: the robot was changed after archive')
        print('658424 (2026-10-02). Merge those changes into the repository first. Nothing was written.')
        for n in conflicts:
            print('  differs  ', n)
        sys.exit(1)

    os.makedirs(os.path.dirname(dst), exist_ok=True)
    replace, drop = set(replaced), set(dropped)
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as zout:
        for info in zin.infolist():
            name = info.filename
            if name in drop:
                continue
            data = local[name] if name in replace else zin.read(name)
            if name in moved:
                info = zipfile.ZipInfo(moved[name], date_time=info.date_time)
                info.compress_type = zipfile.ZIP_DEFLATED
            zout.writestr(info, data)
    missing = deleted - drop
    added = set(changes.get('added_files', {}))
    if added:
        print('WARNING: files added by tools/code_changes.json are not in the original archive '
              'and are not written; copy them to the robot by hand:', sorted(added))
    print(f'{dst}: {len(replaced)} files replaced, {len(dropped)} left out')
    for n in replaced:
        print('  replaced ', n if n not in moved else f'{n} -> {moved[n]} (moved: delete the old file on the robot)')
    for n in dropped:
        print('  left out ', n)
    if missing:
        print('WARNING: allowlisted deletions not found in the archive:', sorted(missing))


if __name__ == '__main__':
    main()
