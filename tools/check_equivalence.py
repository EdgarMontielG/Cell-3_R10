#!/usr/bin/env python3
"""Separate real logic changes from renames in the code-change phase of R10.

    python3 tools/check_equivalence.py             # base from tools/code_changes.json
    python3 tools/check_equivalence.py --base REF  # compare against another commit
    python3 tools/check_equivalence.py --diff      # also print the normalised diffs

After the comment-only cleanup (proved by tools/check_cleanup.py) the program
gets real code changes: the fixes of the Gestamp review and of the open
items. Most of the edited lines are renames - a literal $OUT[498] becomes
its new name do498UpperPinExtend, a constant replaces a number, NUT_STAR
becomes NUT_START. This tool hides those so what is left to review by eye
is only what changes behaviour.

Every KRL file of the working tree is compared with the base after:
  * removing comments, blank lines, indentation and the &COMMENT line;
  * writing every single-bit SIGNAL name as its address ($IN[n] / $OUT[n]),
    each side with its own declarations (a renamed signal is invisible);
  * applying the "identifiers" map of tools/renames.json to the base
    ({"OLD": "NEW"} for any other identifier) and its "constants" map to
    both sides (a named constant is read as its value);
  * dropping parentheses around one operand, '==TRUE', the case and the
    spaces around operators.

A file is then 'equivalent' or 'changed' (with the normalised diff), or it
was added or deleted. A file moved to another folder is listed in
"moved_files" ({old path: new path}) and compared with its old version. tools/code_changes.json must list every changed,
added and deleted KRL file with the items it closes; anything not listed is
a FAIL, so no edit slips through unexplained. A deleted module whose
routines are still called, or a removed or renamed name still used, is a
FAIL too.
"""
import argparse
import difflib
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_cleanup import code_lines, live, split_code, word_in  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KRL_EXT = ('.src', '.dat', '.sub')
CHANGES = 'tools/code_changes.json'
RENAMES = 'tools/renames.json'
SIGNAL = re.compile(r'^\s*(?:GLOBAL\s+)?SIGNAL\s+([A-Za-z_$][A-Za-z0-9_]*)\s+'
                    r'\$(IN|OUT)\[(\d+)\](?:\s+TO\s+\$(?:IN|OUT)\[(\d+)\])?', re.I)
IDENT = re.compile(r'\$?[A-Za-z_][A-Za-z0-9_]*')
WORD = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_$')

problems = []


def fail(msg):
    problems.append(msg)
    print('FAIL  ' + msg)


def git(*args):
    return subprocess.run(('git',) + args, check=True, capture_output=True,
                          cwd=REPO).stdout


def krl_files_at(ref):
    return {p: git('show', f'{ref}:{p}').decode('latin-1')
            for p in git('ls-tree', '-r', '--name-only', ref).decode().splitlines()
            if p.lower().endswith(KRL_EXT)}


def krl_files_worktree():
    paths = git('ls-files', '--cached', '--others', '--exclude-standard').decode().splitlines()
    return {p: open(os.path.join(REPO, p), 'rb').read().decode('latin-1')
            for p in paths if p.lower().endswith(KRL_EXT) and os.path.exists(os.path.join(REPO, p))}


def signal_map(texts):
    """{NAME: '$IN[n]'} for single-bit signals, {NAME: '$IN[a..b]'} for groups."""
    table = {}
    for path, text in texts.items():
        if not path.lower().endswith('.dat'):
            continue
        for raw in text.split('\n'):
            m = SIGNAL.match(split_code(raw))
            if m:
                name, io, a, b = m.groups()
                table[name.upper()] = f'${io.upper()}[{a}]' if not b else f'${io.upper()}[{a}..{b}]'
    return table


def substitute(code, mapping):
    """Replace identifiers outside strings by mapping[IDENT], in one pass."""
    out, i = [], 0
    for m in re.finditer(r'"[^"]*"|' + IDENT.pattern, code):
        out.append(code[i:m.start()])
        tok = m.group(0)
        out.append(tok if tok.startswith('"') else mapping.get(tok, tok))
        i = m.end()
    out.append(code[i:])
    return ''.join(out)


def squeeze(code):
    """Drop spaces that do not separate two words, outside strings."""
    out, in_str = [], False
    for i, ch in enumerate(code):
        if ch == '"':
            in_str = not in_str
        if ch == ' ' and not in_str:
            prev = out[-1] if out else ''
            nxt = code[i + 1] if i + 1 < len(code) else ''
            if not (prev in WORD and nxt in WORD):
                continue
        out.append(ch)
    return ''.join(out)


ATOM_PARENS = re.compile(r'\((NOT )?(\$(?:IN|OUT)\[[^\]]+\]|[A-Z_$][A-Z0-9_]*)\)')


def normalise(line, signals, maps):
    code = line.upper()
    for mapping in maps:
        code = substitute(code, mapping)
    code = substitute(code, signals)
    code = squeeze(code)
    code = re.sub(r'==TRUE(?![A-Z0-9_])', '', code)
    prev = None
    while prev != code:
        prev = code
        code = squeeze(ATOM_PARENS.sub(lambda m: ' ' + (m.group(1) or '') + m.group(2) + ' ', code))
    return code


def comparable(text, signals, maps):
    return [normalise(l, signals, maps) for l in code_lines(text)
            if not l.startswith('&')]


def declared(texts):
    """Every name declared by DEF/DEFFCT/DEFDAT, DECL, SIGNAL, ENUM, STRUC or
    EXT in live code, upper case -> first file declaring it."""
    pat = re.compile(r'^\s*(?:GLOBAL\s+)?(?:DEF|DEFFCT\s+\w+(?:\[\d*\])?|DEFDAT)\s+([A-Za-z_]\w*)'
                     r'|^\s*(?:DECL\s+)?(?:GLOBAL\s+)?(?:SIGNAL|ENUM|STRUC|EXT|EXTFCT\s+\w+)\s+'
                     r'([A-Za-z_$]\w*)', re.I | re.M)
    names = {}
    for p, t in texts.items():
        for m in pat.finditer(live(t)):
            names.setdefault((m.group(1) or m.group(2)).upper(), p)
    return names


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base')
    ap.add_argument('--diff', action='store_true')
    args = ap.parse_args()
    os.chdir(REPO)
    changes = json.load(open(CHANGES))
    renames = json.load(open(RENAMES)) if os.path.exists(RENAMES) else {}
    base = args.base or changes['base']
    rename_map = {k.upper(): v.upper() for k, v in renames.get('identifiers', {}).items()}
    constants = {k.upper(): str(v) for k, v in renames.get('constants', {}).items()}

    old_texts = krl_files_at(base)
    new_texts = krl_files_worktree()
    old_sig, new_sig = signal_map(old_texts), signal_map(new_texts)
    moved = changes.get('moved_files', {})
    for src, dst in moved.items():
        if src not in old_texts:
            fail(f'{src}: listed as moved but not in the base')
        elif src in new_texts:
            fail(f'{src}: listed as moved but still present')
        elif dst not in new_texts:
            fail(f'{dst}: target of a move but does not exist')
        else:
            old_texts[dst] = old_texts.pop(src)
            print(f'ok    moved       {src} -> {dst}')

    listed = {}
    for entry in changes.get('changes', []):
        for path in entry['files']:
            listed.setdefault(path, []).extend(entry['items'])
    deleted_ok = changes.get('deleted_files', {})
    added_ok = changes.get('added_files', {})

    counts = {'equivalent': 0, 'changed': 0, 'added': 0, 'deleted': 0, 'identical': 0}
    for path in sorted(set(old_texts) | set(new_texts)):
        old, new = old_texts.get(path), new_texts.get(path)
        if new is None:
            counts['deleted'] += 1
            if path in deleted_ok:
                print(f'ok    deleted     {path}: {deleted_ok[path]}')
            else:
                fail(f'{path}: deleted but not listed in {CHANGES} deleted_files')
            continue
        if old is None:
            counts['added'] += 1
            if path in added_ok:
                print(f'ok    added       {path}: {added_ok[path]}')
            else:
                fail(f'{path}: new KRL file not listed in {CHANGES} added_files')
            continue
        if old == new:
            counts['identical'] += 1
            continue
        a = comparable(old, old_sig, (rename_map, constants))
        b = comparable(new, new_sig, (constants,))
        if a == b:
            counts['equivalent'] += 1
            print(f'ok    equivalent  {path}')
            continue
        counts['changed'] += 1
        diff = [l for l in difflib.unified_diff(a, b, 'base', 'now', n=1, lineterm='')][2:]
        minus = sum(1 for l in diff if l.startswith('-'))
        plus = sum(1 for l in diff if l.startswith('+'))
        if path in listed:
            print(f'ok    changed     {path}: -{minus} +{plus} normalised lines '
                  f'({", ".join(sorted(set(listed[path])))})')
        else:
            fail(f'{path}: logic changed (-{minus} +{plus} normalised lines) but the file '
                 f'is not listed in {CHANGES}')
        if args.diff or path not in listed:
            for l in diff:
                print('        ' + l)

    for path in deleted_ok:
        if path in new_texts:
            fail(f'{path}: listed as deleted but still present')
        elif path not in old_texts:
            fail(f'{path}: listed as deleted but not in the base')
    for path in listed:
        if path not in new_texts:
            fail(f'{path}: listed in {CHANGES} but does not exist')

    # Nothing removed or renamed may still be used.
    old_names, new_names = declared(old_texts), declared(new_texts)
    live_new = {p: live(t) for p, t in new_texts.items()}
    for name, where in sorted(old_names.items()):
        if name in new_names:
            continue
        for p, t in live_new.items():
            if word_in(name, t):
                fail(f'{name} (declared in {where} in the base) is no longer declared '
                     f'but still used in {p}')
    for old in rename_map:
        if old in new_names:
            fail(f'renamed identifier {old} is still declared ({new_names[old]})')
    for name in constants:
        if name not in new_names and not any(
                re.search(r'^\s*(?:DECL\s+)?(?:GLOBAL\s+)?\w+\s+' + name + r'\s*=', t, re.I | re.M)
                for t in new_texts.values()):
            fail(f'constant {name} of {RENAMES} is not declared in the working tree')

    print(f'\nbase {base[:10]}: {counts["identical"]} identical, {counts["equivalent"]} '
          f'equivalent after renames, {counts["changed"]} with logic changes, '
          f'{counts["added"]} added, {counts["deleted"]} deleted')
    if problems:
        print(f'\n{len(problems)} problem(s)')
        sys.exit(1)
    print('\nall changes are listed in ' + CHANGES)


if __name__ == '__main__':
    main()
