# Cell 3 — robot R10 (BMW-03-10-R1) — program cleanup and Gestamp review fixes

KUKA KR C4, KSS 8.3.29, robot serial 658424, line BMW G65, cell 03, station
03-10-R1 (Gestamp: BMW-03-10R1). WorkVisual project
`V431-03-10R1_v6Active_Centerline_18`; the robot name on the controller is
still `V431_03_10_R1` (item G01).

The robot picks the GE4 part from station 1 or 2 with EOAT 1, presents it
three times to a CenterLine pedestal projection nut welder (Bosch timer, LPT
transducer on the gun), checks the three nuts with a sensor and a camera, and
drops the part on the conveyor or rejects it. It is the same operation as R20;
the process difference is the nut (M6/M8) and the number of nuts (three
instead of five). The findings keep R20's numbering so the two robots can be
compared.

*Versión en español: [README.es.md](README.es.md)*

## Status

The program has run in production and has **not** been accepted by Gestamp.
This repository holds the controller archive as received (commit `22a98cc`,
archive `v431_03_10_r1.zip` of 2026-10-02) plus a cleanup that changes **what
a person reads, not what the robot does**:

* comments, fold titles and `&COMMENT` lines in English, corrected where they
  contradicted the code;
* every I/O action and every wait on a signal commented with the signal's
  address and name — `;GUN OPEN - SIGNALS $OUT[472] dopw1_GunWork OFF,
  $OUT[471] dopw1_GunHome ON`;
* the Gestamp standard header in every integrator module, with the
  designation `BMW-03-10-R1` and the device code (PNW1 pedestal, MH1 material
  handling);
* junk removed: eleven modules nothing calls (21 files with their `.dat`),
  commented-out code, 856 unused declarations and points — every deleted
  module and every removed declaration is listed with its reason in
  `tools/cleanup_allowlist.json` and `tools/cleanup_allowlist.d/*.json`;
* traps disarmed or flagged: an inline form whose hidden data turned a reset
  into a set (RejectGE4), the disabled folds of grippers 2-4, and `;WARNING:`
  lines on folds that must not be re-opened.

The behaviour problems found were **not fixed** by the cleanup: they need an
owner decision and a test on the cell. They are in
**[docs/FINDINGS.md](docs/FINDINGS.md)**: F01–F47 (two critical; F37 does not
apply to R10; F44–F47 exist only on R10) and 28 Gestamp compliance items
(C01–C28). The code points to them with `;CHECK: ... (Fnn)` comments.

On 2026-10-02 Gestamp reviewed the program and issued 22 points for this
station (G01–G22, with Gestamp's text; point-by-point verification in
FINDINGS.md). Calvin's list of 2026-10-03 was also verified point by point for
10R1. Part of the Gestamp points were **fixed in the office** in a second step
that does change code (see *Office fixes*): no GOTO, signal names instead of
I/O numbers, one-line nut check, gripper-empty check before the gripper
command, GripperTech hidden parameters corrected, English names, constants
for the stroke limits and pressures, dead weld retry removed, and the
next-nut TRIGGERs taken out of the inline forms. They still have to be tested
on the cell.

## Proof that behaviour did not change

```
python3 tools/check_cleanup.py --head fb8a4c8
```

compares every KRL file of the cleanup commit with the original archive (first
commit) after removing what the compiler ignores — comments, blank lines,
indentation. What is left must be identical line by line, except the removals
listed in the allowlist. It also checks that nothing deleted is still
referenced, that inline-form headers carrying smartPAD data and the lines
inside the forms are unchanged (except a stale tool name in the display text
and the one listed RejectGE4 form-data change), that AutomationCore `;Params`
lines are untouched, that every comment naming a signal next to an address
names a signal really declared at that address, that every file keeps its
line endings (the archive mixes CRLF and LF) and stays ASCII, and that the
fold and block structure is no worse than before. It exits non-zero on any
failure.

## Office fixes (Gestamp review)

The second step changes code, so it cannot be proved equal to the archive.
Instead every change is declared and the rest is proved unchanged:

```
python3 tools/check_equivalence.py [--diff]
```

compares every KRL file with the cleanup commit after removing comments and
writing every signal name as its address and every constant as its value
(`tools/renames.json`): renames disappear and only changed logic is left.
Every changed, added, deleted or moved file must be listed in
`tools/code_changes.json` with the items it answers, or the check fails. The
changes and the cell test each one needs are in the open items (state
*Corregido en oficina - probar en celda*) and in section 3 of the PDF.

## Cycle time (stage 1, 2026-10-07)

Gestamp expects 12 s per part of welding process with the robot stopped. The
robot waited about 4 s for the nut before nuts 2 and 3 because the next nut was
fed only after the weld. Stage 1 (F52) feeds it into the shuttle while the robot
moves in and welds, and loads it onto the pin on the way out, at the same robot
positions as before; it also adds a measurement (`CL_CYCLE_TIME`, last 10
cycles per nut, 13 steps of the weld). After 10 cycles in automatic, a backup
gives the times:

```
python3 tools/cycle_times.py <backup.zip>
```

## Loading onto the robot

The office version changes code: run the cell tests of the items "Corregido en
oficina - probar en celda" before production. It is a program change on a
production cell:

1. Take a fresh backup of the robot. If it differs from the last audited
   backup (today `bmw_03_10_r1.zip` of 2026-10-05, in `audits/`), someone
   changed the robot since — audit and merge before loading.
2. Build the archive to load on top of the last audited backup:

   ```
   python3 tools/build_archive.py <bmw_03_10_r1.zip> dist/
   ```

   writes `dist/658424_R10_YYYY-MM-DD_HHMM.zip` (central Mexico time, like
   the Excel and the PDF). It copies the archive entry by entry,
   replaces the changed files, leaves out the deleted modules, writes the two
   files of `Styles/optiones` to `Styles/Options`, adds the new modules and
   prints the lists; names are matched without case, as on the controller. It
   accepts only the original archive or an audited one (its sha256 is in
   `audits/*/summary.json`); for any other, if a file it would replace or
   leave out is not the one of archive 658424, it stops without writing
   anything (see step 1). That zip is the full record of the version; the
   programmer gets the package from `tools/make_package.py <audited backup>
   <built zip> dist/`: only the programs that differ from the robot, in their
   controller folders, and `LEEME.txt` with the replace, add and delete lists.
   It is loaded through WorkVisual (project opened from the robot, deploy),
   which also proves that it compiles. **Delete on the controller the
   twenty-two files reported "left out"** (21 from the cleanup, one from the
   office fixes) **and the folder `Program/Styles/optiones`** — a restore does
   not delete files that are not in the archive.
3. On the smartPAD, open every changed module once: no navigator error, folds
   open and close normally.
4. Run a production cycle at reduced override in T1, then in automatic, and
   the cell tests of the office fixes (PDF section 3.3).
5. **WorkVisual.** The projects inside the archive
   (`C/KRC/User/ProjectRoot/...wvs`, also the new `BMW-03-10R1_v8`) hold the
   *old* files, including `$config.dat` and the deleted modules; on
   2026-10-05 such a deploy put the original program back on the robot. Activating the project copies them
   back to the controller when their checksum differs. Before anyone deploys
   from WorkVisual again, load the project from the controller (or update it
   with these files) and save it; otherwise a deploy silently restores the
   old program.

Do not open or confirm old inline forms while editing comments on the smartPAD
(Cmd OK / Touch Up): several carry hidden parameters that disagree with the
code (F21). Do not save the GripperTech configuration on the HMI until
`GripperConfig.xml` is re-synchronised (F33).

## Layout

```
KRC/, C/, Registry/, am.ini   the controller archive (cleaned)
docs/FINDINGS.md              findings and Gestamp compliance - start here
docs/IO_MAP.md                the name of every address the program uses
docs/CONVENTIONS.md           what may and may not change; comment format
tools/check_cleanup.py        proof that comments changed, not behaviour
tools/cleanup_allowlist.json  the deleted modules, each with its reason
tools/cleanup_allowlist.d/    the other executable removals, with reasons
tools/check_equivalence.py    office fixes: logic diff without renames, every change declared
tools/code_changes.json       every code change after the cleanup, with its items
tools/renames.json            renamed identifiers and constants for check_equivalence
tools/build_archive.py        builds the full archive of the version, on top of the last audited backup
tools/make_package.py         builds the programmer's package: changed programs and the delete list
tools/cycle_times.py          cycle times of the nut weld from a backup (CL_CYCLE_TIME, F52)
docs/open_items.json          master list (Gestamp G01-G22, F01-F47, C01-C28), state and history
docs/OPEN_ITEMS.es.md         readable view of the open items (generated, Spanish)
docs/PROCESO.es.md            the daily close-and-audit process (Spanish)
tools/audit_backup.py         audits a daily backup against the last audited state
tools/test_audit_backup.py    tests of the audit tool
tools/make_items_xlsx.py      builds the open-items Excel for the programmer
tools/make_items_md.py        builds docs/OPEN_ITEMS.es.md
tools/make_report.py          builds the PDF report (Spanish)
dist/                         generated Excel and PDF (dated names; tools/naming.py)
audits/                       one folder per audited backup (AUDIT.md, summary.json)
```

`Log Files/` of the original archive (KRC logs) is not under version control;
`build_archive.py` copies it from the original zip.

## Scope

KUKA system files, tech packages and Gestamp standard routines
(AutomationCore, NutWeld, GripperTech, BrakeTest, GlueTech) were not edited,
except: the integrator parts of `$config.dat` and `sps.sub` and the KUKA user
hooks `masref_user.src` and `tm_useraction.src` were cleaned like the
integrator modules; unused integrator leftovers were removed from
`$config.dat` and `automationcoreroutines.dat`; comments were edited in
`automationcoredata.dat`, `automationcoreroutines.dat` and
`nutweldroutines.dat`. The office fixes added constants and the beacon signals
to `$config.dat` and renamed the pedestal and camera signals in
`automationcoreroutines.dat` (same addresses, item C28). The vendor routines
(`TP/**/*.src`, `bas.src`) are unchanged. Integrator edits found *inside*
vendor files — notably `EndOfCycle` without Work Complete (F46) — are listed
in [docs/FINDINGS.md](docs/FINDINGS.md) so a package update does not lose
them unnoticed.
