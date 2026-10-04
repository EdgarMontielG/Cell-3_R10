#!/usr/bin/env python3
"""Prove that the cleanup of the R10 archive changed comments, not behaviour.

Run from the repository root:

    python3 tools/check_cleanup.py            # compare against the baseline commit
    python3 tools/check_cleanup.py --base REF # compare against another commit
    python3 tools/check_cleanup.py --head REF # check commit REF, not the working tree

Once the comment-only cleanup was finished, real code changes started (see
tools/check_equivalence.py); from then on the proof is run on the cleanup
commit with --head, the one named 'base' in tools/code_changes.json.

The baseline is the first commit of the repository: the archive exactly as
it came off the controller. Every KRL file (.src / .dat / .sub) in the
working tree is compared with its baseline version after removing
everything the KRL compiler ignores (comments, blank lines, indentation).
What remains must be identical, line for line, except for the code removals
listed - each with its reason - in tools/cleanup_allowlist.json.

It also checks, per file:

  * each file keeps its line-ending convention (CRLF or LF) and stays
    plain ASCII;
  * every inline-form fold header that carries form parameters (the
    ';FOLD ... ;%{PE}...%P ...' lines the smartPAD parses to re-open a
    PTP/LIN/OUT/WAIT form) is byte-identical to the baseline, or listed as
    removed in the allowlist, and the body of every such form (the lines
    the smartPAD regenerates) is unchanged too;
  * the ';Params IlfProvider=' lines of AutomationCore inline forms are
    unchanged (stale GripperTech ones, in hand-written folds, may go);
  * ;FOLD / ;ENDFOLD balance and DEF/IF/SWITCH/LOOP... nesting are no
    worse than in the baseline (defects already there are warnings);
  * every comment that names a signal next to its index, e.g.
    ';$OUT[471] do471GunHome', names a signal really declared at that index.

Deleted modules must be listed in the allowlist too. Exit status is
non-zero on any failure.
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys

KRL_EXT = ('.src', '.dat', '.sub')
ALLOWLIST = 'tools/cleanup_allowlist.json'
ALLOWLIST_DIR = 'tools/cleanup_allowlist.d'

OPENERS = {'DEF': 'END', 'DEFFCT': 'ENDFCT', 'DEFDAT': 'ENDDAT',
           'IF': 'ENDIF', 'SWITCH': 'ENDSWITCH', 'FOR': 'ENDFOR',
           'LOOP': 'ENDLOOP', 'WHILE': 'ENDWHILE', 'REPEAT': 'UNTIL'}
CLOSERS = {v: k for k, v in OPENERS.items()}

problems = []


def fail(msg):
    problems.append(msg)
    print('FAIL  ' + msg)


def git(*args):
    return subprocess.run(('git',) + args, check=True, capture_output=True).stdout


def split_code(line):
    """Return the part of a KRL line the compiler reads: everything before
    the first ';' that is not inside a double-quoted string."""
    in_str = False
    for i, ch in enumerate(line):
        if ch == '"':
            in_str = not in_str
        elif ch == ';' and not in_str:
            return line[:i]
    return line


def normalise(code):
    """Collapse whitespace outside strings; KRL ignores it."""
    out, in_str, prev_space = [], False, False
    for ch in code.strip():
        if ch == '"':
            in_str = not in_str
        if not in_str and ch in ' \t':
            if not prev_space:
                out.append(' ')
            prev_space = True
            continue
        prev_space = False
        out.append(ch)
    return ''.join(out)


def code_lines(text):
    """The executable content of a file, as a list of normalised lines.
    '&COMMENT' is navigator text; every other '&' header line is kept."""
    result = []
    for raw in text.split('\n'):
        raw = raw.rstrip('\r')
        if raw.startswith('&COMMENT'):
            continue
        code = normalise(split_code(raw))
        if code:
            result.append(code)
    return result


def form_headers(text):
    """Fold headers the smartPAD parses back into an inline form: they carry
    the form's parameters after '%P'. Hand-edited folds that kept only the
    ';%{PE}' marker (no parameters) are display text and may be retitled."""
    return [l.rstrip('\r') for l in text.split('\n')
            if l.lstrip().upper().startswith(';FOLD') and ';%{' in l and '%P' in l]


def subtract_in_order(old, removals):
    """Remove each allowed line from `old` once, keeping order. Returns the
    reduced list and the removals that were not found."""
    result, missing = list(old), []
    for line in removals:
        target = normalise(split_code(line))
        for i, cur in enumerate(result):
            if cur == target:
                del result[i]
                break
        else:
            missing.append(line)
    return result, missing


def first_difference(a, b):
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            return i, x, y
    if len(a) != len(b):
        i = min(len(a), len(b))
        return i, a[i] if i < len(a) else '<end>', b[i] if i < len(b) else '<end>'
    return None


def eol_style(raw):
    crlf = raw.count(b'\r\n')
    lf = raw.count(b'\n') - crlf
    return 'CRLF' if lf == 0 else 'LF' if crlf == 0 else 'mixed'


def check_format(path, raw_new, raw_old):
    """The archive holds both CRLF files (written on the controller) and
    LF-only files (edited on a laptop and copied over); the KRC4 reads
    both. The cleanup keeps each file's convention so a diff shows only
    the lines that really changed."""
    if raw_old is not None and eol_style(raw_new) != eol_style(raw_old):
        fail(f'{path}: line endings changed from {eol_style(raw_old)} '
             f'to {eol_style(raw_new)}')
    try:
        raw_new.decode('ascii')
    except UnicodeDecodeError:
        try:
            if raw_old is not None:
                raw_old.decode('ascii')
            fail(f'{path}: cleanup introduced non-ASCII bytes')
        except UnicodeDecodeError:
            pass  # vendor file that was already ANSI


def fold_issues(path, text):
    issues, depth = [], 0
    for lineno, raw in enumerate(text.split('\n'), 1):
        s = raw.strip().upper()
        if s.startswith(';FOLD'):
            depth += 1
        elif s.startswith(';ENDFOLD'):
            depth -= 1
            if depth < 0:
                issues.append(f'{path}:{lineno} ;ENDFOLD with no open ;FOLD')
                depth = 0
    if depth:
        issues.append(f'{path}: {depth} ;FOLD left open at end of file')
    return issues


def nesting_issues(path, text):
    issues, stack = [], []
    for lineno, raw in enumerate(text.split('\n'), 1):
        code = split_code(raw).strip().upper()
        tokens = re.findall(r'[A-Z_$][A-Z0-9_]*', code)
        if not tokens:
            continue
        first = tokens[0]
        if first in ('GLOBAL', 'PUBLIC') and len(tokens) > 1:
            first = tokens[1]
        if first in OPENERS:
            if first == 'IF' and 'THEN' not in tokens:
                continue  # single-line forms are not KRL; let the compiler say so
            stack.append((first, lineno))
        elif first in CLOSERS:
            if not stack:
                issues.append(f'{path}:{lineno} {first} with nothing open')
                continue
            opener, opened_at = stack.pop()
            if OPENERS[opener] != first:
                issues.append(f'{path}:{lineno} {first} closes {opener} '
                              f'opened on line {opened_at}')
    for opener, opened_at in stack:
        issues.append(f'{path}:{opened_at} {opener} is never closed')
    return issues


def check_structure(path, text, old_text):
    """Folds and block nesting. A defect already present in the archive is
    reported once as a warning; the cleanup may fix it but must not add one."""
    def issues(t):
        found = fold_issues(path, t)
        if path.lower().endswith(('.src', '.sub')):
            found += nesting_issues(path, t)
        return found
    now = issues(text)
    before = issues(old_text) if old_text is not None else []
    if len(now) > len(before):
        for msg in now:
            fail(msg)
    else:
        for msg in now:
            print('WARN  pre-existing: ' + msg)


def declared_signals(files):
    """{(IO, index): set(names)} from every live SIGNAL declaration."""
    pat = re.compile(r'^\s*(?:GLOBAL\s+)?SIGNAL\s+([A-Za-z_$][A-Za-z0-9_]*)\s+'
                     r'\$(IN|OUT)\[(\d+)\](?:\s+TO\s+\$(?:IN|OUT)\[(\d+)\])?', re.I)
    table = {}
    for path, text in files.items():
        if not path.lower().endswith('.dat'):
            continue
        for raw in text.split('\n'):
            m = pat.match(split_code(raw))
            if not m:
                continue
            name, io, a, b = m.group(1), m.group(2).upper(), int(m.group(3)), m.group(4)
            for idx in range(a, (int(b) if b else a) + 1):
                table.setdefault((io, idx), set()).add(name.lower())
    return table


SIG_REF = re.compile(r'\$(IN|OUT)\[(\d+)\]\s+([A-Za-z_][A-Za-z0-9_]*)')
SIGNALISH = re.compile(r'^(g?d[io]|dipw|dopw|gdopw|gdipw|CL_)', re.I)


def check_signal_comments(path, text, signals):
    all_names = {n for names in signals.values() for n in names}
    for lineno, raw in enumerate(text.split('\n'), 1):
        code = split_code(raw)
        comment = raw[len(code):]
        if not comment or ';%{' in comment:
            continue  # inline-form parameters are the editor's, not ours
        for io, idx, name in SIG_REF.findall(comment):
            key = (io.upper(), int(idx))
            low = name.lower()
            if low in signals.get(key, set()):
                continue
            if low in all_names:
                fail(f'{path}:{lineno} comment names {name} at ${io}[{idx}], '
                     f'but {name} is declared at another index')
            elif SIGNALISH.match(name):
                fail(f'{path}:{lineno} comment names {name} at ${io}[{idx}], '
                     f'and no signal of that name is declared')


def load_allowlist():
    """tools/cleanup_allowlist.json plus every tools/cleanup_allowlist.d/*.json,
    merged. Each file may hold:
      deleted_files       {path: reason}
      removed_code        {path: {reason, lines: [...], form_headers: [...]}}
      form_header_changes {path: [{old, new, reason}]}
      form_body_changes   {path: [{header, reason}]}"""
    allow = {'deleted_files': {}, 'removed_code': {}, 'form_header_changes': {},
             'form_body_changes': {}}
    sources = ([ALLOWLIST] if os.path.exists(ALLOWLIST) else []) + \
        sorted(glob.glob(ALLOWLIST_DIR + '/*.json'))
    for src in sources:
        part = json.load(open(src))
        allow['deleted_files'].update(part.get('deleted_files', {}))
        for path, entry in part.get('removed_code', {}).items():
            cur = allow['removed_code'].setdefault(path, {'lines': [], 'form_headers': []})
            cur['lines'] += entry.get('lines', [])
            cur['form_headers'] += entry.get('form_headers', [])
        for path, changes in part.get('form_header_changes', {}).items():
            allow['form_header_changes'].setdefault(path, []).extend(changes)
        for path, changes in part.get('form_body_changes', {}).items():
            allow['form_body_changes'].setdefault(path, []).extend(changes)
    return allow, sources


DECL_TYPES = ('BOOL', 'INT', 'REAL', 'CHAR', 'FRAME', 'POS', 'E6POS', 'AXIS',
              'E6AXIS', 'FDAT', 'PDAT', 'LDAT', 'LOAD', 'BASIS_SUGG_T')


def declared_names(code):
    """Names introduced by one declaration line, or [] if it is not one."""
    toks = re.findall(r'[A-Za-z_$][A-Za-z0-9_$]*', code)
    while toks and toks[0].upper() in ('GLOBAL', 'DECL', 'PUBLIC'):
        toks = toks[1:]
    if not toks:
        return []
    head = toks[0].upper()
    if head in ('SIGNAL', 'ENUM', 'STRUC', 'EXT', 'EXTFCT') and len(toks) > 1:
        return [toks[2]] if head == 'EXTFCT' and len(toks) > 2 else [toks[1]]
    m = re.match(r'^\s*(?:GLOBAL\s+)?(?:DECL\s+)?(?:GLOBAL\s+)?([A-Za-z_][A-Za-z0-9_]*)\s+(.*)$', code)
    if not m or '=' in m.group(1):
        return []
    body = re.sub(r'\[[^\]]*\]', '', m.group(2))
    body = re.sub(r'=\s*\{.*\}', '', body)
    body = re.sub(r'"[^"]*"', '', body)
    names = [re.match(r'\s*([A-Za-z_$][A-Za-z0-9_$]*)', part) for part in body.split(',')]
    return [n.group(1) for n in names if n]


def word_in(name, text):
    return re.search(r'(?<![\w$])' + re.escape(name) + r'(?![\w$])', text, re.I)


def live(text):
    """Code the compiler reads, for reference searches: comments, '&' header
    lines and string contents removed (a name inside a string, such as the
    editor's LAST_BASIS suggestion "POUNCE", is not a reference)."""
    return '\n'.join('' if l.startswith('&') else re.sub(r'"[^"]*"', '""', split_code(l))
                     for l in text.split('\n'))


def check_removed_references(allow, texts, base):
    """Nothing the cleanup removed may still be referenced. A GLOBAL name or
    a deleted module must not appear in live code of any remaining file; a
    module-local DECL must not appear anywhere in its own .src, comments
    and inline-form parameters included ('2:P25' references XP25/FP25)."""
    live_texts = {p: live(t) for p, t in texts.items()}
    for path in allow['deleted_files']:
        try:
            old = git('show', f'{base}:{path}').decode('latin-1')
        except subprocess.CalledProcessError:
            continue
        for name in re.findall(r'^\s*(?:GLOBAL\s+)?DEF(?:FCT\s+\S+)?\s+([A-Za-z_][A-Za-z0-9_]*)',
                               live(old), re.M | re.I):
            for p, t in live_texts.items():
                if word_in(name, t):
                    fail(f'{path}: deleted module {name} is still referenced in {p}')
    for path, entry in allow['removed_code'].items():
        src_twin = None
        if path.lower().endswith('.dat'):
            stem = path[:-4]
            src_twin = next((p for p in texts if p.lower() == (stem + '.src').lower()), None)
        for line in entry['lines']:
            code = split_code(line)
            is_global = re.match(r'^\s*(?:DECL\s+)?GLOBAL\b', code, re.I) or \
                path.lower().endswith('$config.dat')
            for name in declared_names(code):
                if is_global or src_twin is None:
                    for p, t in live_texts.items():
                        if word_in(name, t):
                            fail(f'{path}: removed declaration {name} is still referenced in {p}')
                else:
                    variants = {name}
                    m = re.match(r'^(X|F|P|L)(.+)$', name, re.I)
                    if m:
                        variants.add(m.group(2))
                    for v in variants:
                        if word_in(v, texts[src_twin]):
                            fail(f'{path}: removed local data {name} is still referenced '
                                 f'in {src_twin} (as {v})')


def form_bodies(text):
    """[(header, body lines)] for every inline form carrying form data. The
    body is what the smartPAD regenerates when the form is confirmed; a line
    added there (even a comment) is lost on the next Touch Up, a line taken
    out changes what the form owns."""
    lines = [l.rstrip('\r') for l in text.split('\n')]
    out = []
    for i, line in enumerate(lines):
        s = line.lstrip()
        if not (s.upper().startswith(';FOLD') and ';%{' in s and '%P' in s):
            continue
        if '%CEXT' in s:
            continue  # template containers (EXTERNAL DECLARATIONS, USER EXT): edited by hand
        depth, body = 0, []
        for nxt in lines[i + 1:]:
            t = nxt.strip().upper()
            if t.startswith(';FOLD'):
                depth += 1
            elif t.startswith(';ENDFOLD'):
                if depth == 0:
                    break
                depth -= 1
            body.append(nxt.strip())
        out.append((line, body))
    return out


TOOL_NAME = re.compile(r'Tool\[(\d+)\]:[^;\[]*?(?=\s+Base\[|;|$)')


def header_key(header):
    """Split an inline-form header into the smartPAD form data (from ';%{'
    on, which must never change) and the display text, with the tool name
    blanked out. The display text is regenerated by the editor whenever the
    form is opened; refreshing a stale tool name is the only edit allowed."""
    i = header.index(';%{')
    return TOOL_NAME.sub(r'Tool[\1]', header[:i]), header[i:]


def check_form_headers(path, old_text, text, entry, changes, body_changes):
    old_forms = form_headers(old_text)
    old_bodies = dict()
    for header, body in form_bodies(old_text):
        old_bodies.setdefault(header, []).append(body)
    for change in changes:
        if change['old'] in old_forms:
            old_forms[old_forms.index(change['old'])] = change['new']
            old_bodies.setdefault(change['new'], []).extend(old_bodies.get(change['old'], []))
        else:
            fail(f'{path}: allowlisted form header change not found in baseline: '
                 f'{change["old"]!r}')
    for h in entry.get('form_headers', []):
        if h in old_forms:
            old_forms.remove(h)
        else:
            fail(f'{path}: allowlisted form header removal not found in baseline: {h!r}')
    def ilf_params(t):
        return sorted(l.strip() for l in t.split('\n')
                      if l.strip().startswith(';Params IlfProvider=')
                      and 'GripperTech' not in l)
    if ilf_params(old_text) != ilf_params(text):
        fail(f'{path}: an AutomationCore inline-form ";Params IlfProvider=" line '
             f'changed or disappeared (the smartPAD regenerates the call from it)')
    new_forms = form_headers(text)
    if len(old_forms) != len(new_forms):
        fail(f'{path}: {len(old_forms)} inline-form headers expected, {len(new_forms)} found')
        return 0
    refreshed = 0
    for old, new in zip(old_forms, new_forms):
        if old == new:
            continue
        if header_key(old) == header_key(new):
            refreshed += 1
            continue
        fail(f'{path}: inline-form fold header changed (smartPAD form data): '
             f'baseline {old!r}, now {new!r}')
    allowed_bodies = {c['header'] for c in body_changes}
    for header, body in form_bodies(text):
        candidates = [b for h, bs in old_bodies.items() if header_key(h) == header_key(header)
                      for b in bs]
        if body in candidates or header in allowed_bodies:
            continue
        fail(f'{path}: the body of inline form {header.strip()[:70]!r} changed - '
             f'lines inside a form fold are regenerated by the smartPAD')
    return refreshed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base', default=git('rev-list', '--max-parents=0', 'HEAD')
                    .decode().split()[0])
    ap.add_argument('--head', help='commit to check instead of the working tree')
    args = ap.parse_args()

    def read_new(path):
        if args.head:
            return git('show', f'{args.head}:{path}')
        return open(path, 'rb').read()

    allow, sources = load_allowlist()

    base_files = [p for p in git('ls-tree', '-r', '--name-only', args.base)
                  .decode().splitlines() if p.lower().endswith(KRL_EXT)]
    if args.head:
        work_files = sorted(p for p in git('ls-tree', '-r', '--name-only', args.head)
                            .decode().splitlines() if p.lower().endswith(KRL_EXT))
    else:
        work_files = sorted(p for p in git('ls-files', '--cached', '--others',
                                           '--exclude-standard').decode().splitlines()
                            if p.lower().endswith(KRL_EXT) and os.path.exists(p))

    texts = {p: read_new(p).decode('latin-1') for p in work_files}
    signals = declared_signals(texts)

    changed = refreshed = 0
    for path in base_files:
        if path not in texts:
            if path in allow['deleted_files']:
                print(f'ok    {path}: deleted ({allow["deleted_files"][path]})')
            else:
                fail(f'{path}: deleted but not listed in the allowlist')
    for path in allow['deleted_files']:
        if path in texts:
            fail(f'{path}: listed as deleted in the allowlist but still present')
        elif path not in base_files:
            fail(f'{path}: listed as deleted in the allowlist but not in the baseline')

    for path in work_files:
        raw_new = read_new(path)
        try:
            raw_old = git('show', f'{args.base}:{path}')
        except subprocess.CalledProcessError:
            raw_old = None
        check_format(path, raw_new, raw_old)
        text = texts[path]
        check_structure(path, text, raw_old.decode('latin-1') if raw_old else None)
        check_signal_comments(path, text, signals)
        if raw_old is None:
            fail(f'{path}: new KRL file - the cleanup adds no modules')
            continue
        if raw_old == raw_new:
            continue
        changed += 1
        old_text = raw_old.decode('latin-1')

        entry = allow['removed_code'].get(path, {'lines': [], 'form_headers': []})
        old_code, missing = subtract_in_order(code_lines(old_text), entry['lines'])
        for line in missing:
            fail(f'{path}: allowlisted removal not found in baseline: {line!r}')
        new_code = code_lines(text)
        diff = first_difference(old_code, new_code)
        if diff:
            i, was, now = diff
            fail(f'{path}: executable code differs at code line {i + 1}: '
                 f'baseline {was!r}, now {now!r}')
        refreshed += check_form_headers(path, old_text, text, entry,
                                        allow['form_header_changes'].get(path, []),
                                        allow['form_body_changes'].get(path, []))

    for path in list(allow['removed_code']) + list(allow['form_header_changes']):
        if path not in texts:
            fail(f'{path}: allowlist entry for a file that does not exist')
    check_removed_references(allow, texts, args.base)

    removed = sum(len(e['lines']) for e in allow['removed_code'].values())
    print(f'checked {len(work_files)} KRL files of {args.head or "the working tree"} '
          f'against {args.base[:10]} '
          f'(allowlist: {", ".join(sources) or "none"})')
    print(f'{changed} changed, {len(allow["deleted_files"])} deleted, '
          f'{removed} code lines removed by allowlist, '
          f'{refreshed} inline-form headers with a refreshed tool name')
    if problems:
        print(f'\n{len(problems)} problem(s)')
        sys.exit(1)
    print('\nall checks passed: comments changed, behaviour did not')


if __name__ == '__main__':
    main()
