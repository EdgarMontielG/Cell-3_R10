#!/usr/bin/env python3
"""Build a KRC4 archive zip of the cleaned program from the original archive.

    python3 tools/build_archive.py ARCHIVE.zip [OUT]

OUT is a directory (default dist/) or a file name. In a directory the archive
is named 658424_R10_<YYYY-MM-DD_HHMM>.zip, with the date and time of central
Mexico (tools/naming.py), so every archive handed to the programmer says when
it was built.

Every entry of the source archive is copied through byte-for-byte with its
original timestamp, except:
  - files this repository changed are replaced by the repository version;
  - files listed as deleted in the cleanup allowlist or in
    tools/code_changes.json are left out;
  - files listed in "moved_files" of tools/code_changes.json are written
    under their new path (with the repository version);
  - files listed in "added_files" that the archive does not hold are added.
Names are matched without case, as on the controller. The script prints the
lists, so the operator knows exactly what differs from the archive that is
running on the robot.

The source archive is either the one this repository was made from (archive
v431_03_10_r1.zip of robot 658424, the first commit) or a later backup that
was audited (its sha256 is recorded in audits/*/summary.json) and whose
changes were merged into the repository. For any other archive, an entry that
differs from the first commit means the robot was changed after that backup:
the script refuses to build rather than overwrite that change. Audit and
merge first.

Run the two checkers first; this script refuses to build when either fails:
tools/check_cleanup.py --head <base of tools/code_changes.json> (the cleanup
changed only comments) and tools/check_equivalence.py (every later code
change is listed with its items).
"""
import hashlib
import os
import subprocess
import sys
import time
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
    added = changes.get('added_files', {})
    base = git('rev-list', '--max-parents=0', 'HEAD').decode().split()[0]
    baseline = tree_blobs(base)
    tracked = set(git('ls-files', '-z').decode('utf-8', 'surrogateescape').split('\0'))
    # The controller ignores case: match archive entries to repository paths
    # without it (a WorkVisual deploy may write style1app2opt1autorr.src).
    tracked_l = {t.lower(): t for t in tracked if os.path.isfile(t)}
    deleted_l = {d.lower() for d in deleted}
    moved_l = {k.lower(): v for k, v in moved.items()}
    added_l = {k.lower(): k for k in added}
    audited = audited_backup(src)
    if audited:
        print(f'{os.path.basename(src)} is the backup audited in {audited}: its changes were merged.')

    # Only files the repository tracks can be "changed by the repository";
    # anything else in the archive (Log Files/) is copied as it is.
    replaced, dropped, conflicts, local, newname = [], [], [], {}, {}
    seen = set()
    with zipfile.ZipFile(src) as zin:
        for info in zin.infolist():
            name = info.filename
            low = name.lower()
            data = zin.read(name)
            if low in moved_l:
                newname[name] = moved_l[low]
                with open(moved_l[low], 'rb') as f:
                    local[name] = f.read()
                seen.add(moved_l[low].lower())
            elif low in tracked_l:
                with open(tracked_l[low], 'rb') as f:
                    local[name] = f.read()
                seen.add(low)
            gone = low in deleted_l
            changed = gone or name in newname or local.get(name, data) != data
            if changed and not audited and baseline.get(name) != blob_id(data):
                conflicts.append(name)
            elif gone:
                dropped.append(name)
            elif changed:
                replaced.append(name)
    if conflicts:
        print('These files of the archive differ from the first commit of this repository')
        print('and would be overwritten or left out: the robot was changed after archive')
        print('658424 (2026-10-02) and the backup was not audited. Audit it and merge those')
        print('changes into the repository first. Nothing was written.')
        for n in conflicts:
            print('  differs  ', n)
        sys.exit(1)
    extra = sorted(path for low, path in added_l.items() if low not in seen)

    os.makedirs(os.path.dirname(dst), exist_ok=True)
    replace, drop = set(replaced), set(dropped)
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as zout:
        for info in zin.infolist():
            name = info.filename
            if name in drop:
                continue
            data = local[name] if name in replace else zin.read(name)
            if name in newname:
                info = zipfile.ZipInfo(newname[name], date_time=info.date_time)
                info.compress_type = zipfile.ZIP_DEFLATED
            zout.writestr(info, data)
        for path in extra:
            with open(path, 'rb') as f:
                zout.writestr(zipfile.ZipInfo(path, date_time=time.localtime()[:6]), f.read(),
                              zipfile.ZIP_DEFLATED)
    missing = deleted_l - {d.lower() for d in drop}
    print(f'{dst}: {len(replaced)} files replaced, {len(extra)} added, {len(dropped)} left out')
    for n in replaced:
        print('  replaced ', n if n not in newname else f'{n} -> {newname[n]} (moved: delete the old file on the robot)')
    for n in extra:
        print('  added    ', n)
    for n in dropped:
        print('  left out ', n)
    if missing:
        print('NOTE: deletions not in this archive (already deleted on the robot):', sorted(missing))


def audited_backup(path):
    """The audits/ folder whose summary.json records this zip (by sha256), or None."""
    import glob
    import json
    with open(path, 'rb') as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    for summary in sorted(glob.glob(os.path.join(REPO, 'audits', '*', 'summary.json'))):
        with open(summary) as f:
            if json.load(f).get('backup', {}).get('sha256') == sha:
                return os.path.relpath(os.path.dirname(summary), REPO)
    return None

if __name__ == '__main__':
    main()
