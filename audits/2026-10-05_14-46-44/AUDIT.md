# Backup audit - bmw_03_10_r1_1450.zip

- Backup: `/tmp/claude-0/-home-user/50f56c92-2919-5ae3-94c9-0de4476bbe87/scratchpad/bmw_03_10_r1_1450.zip` (sha256 `5449a841ac107d88...`)
- am.ini: archive `e:\bmw_03_10_r1.zip\`, date `2026-10-05_14-46-44`, config `All`, robot `BMW_03_10_R1`, serial `658424`, KSS `V8.3.29`
- Compared with: `HEAD` = `b62cd9c8dc` "Process: how a daily audit is reviewed, when to integrate instead of import"; first commit (archive as received) `22a98cc8ef`
- Generated 2026-10-05T18:51:36 by tools/audit_backup.py

## Summary

| | |
|---|---|
| Entries audited (Log Files/ skipped: 8) | 336 |
| Unchanged | 242 |
| Changed | 58 |
| Added | 14 |
| Missing from the backup | 8 |
| **Deleted modules still on the controller** | 22 |
| **Pre-cleanup files** | 19 |
| Edited on top of the pre-cleanup file | 17 |
| KRL files with code changes | 38 |
| Code lines removed / added | 169 / 1941 |
| KRL files with comment-only changes | 28 |
| KRL files with runtime values only (written by the program, not edits) | 2 |
| Checks FAIL / WARN / INFO | 2 / 32 / 6 |

**Needs attention:**

- **22 module(s) deleted in the cleanup still on the controller** (listed below)
- **19 PRE-CLEANUP file(s)**: the cleaned program was not loaded or was overwritten (listed below)
- **17 file(s) edited on top of the pre-cleanup version** (listed below)
- WARN 8 file(s) of the base missing from the backup - deleted on the robot, or an incomplete archive (e.g. KRC/R1/Program/StyleApps/Options/style1app1opt1.dat; all in Files, "Missing from the backup")
- **2 FAIL** in the mechanical checks
- 32 WARN in the mechanical checks

## The backup itself

- FAIL: KRC/R1/Program/CK1STXXX.dat: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/CK1STXXX.src: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/Centerline/CENTERLINE_WELD1.src: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/Centerline/centerline_loop.src: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/Centerline/trigger1.dat: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/Centerline/trigger1.src: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/Centerline/trigger2.dat: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/Centerline/trigger2.src: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/Centerline/trigger3.dat: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/Centerline/trigger3.src: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/POUNCE.dat: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/POUNCE.src: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/StyleApps/Options/style1app2opt1AutoRR.dat: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/StyleApps/Options/style1app2opt1AutoRR.src: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/StyleApps/Options/style1app2opt2AutoRR.dat: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/StyleApps/Options/style1app2opt2AutoRR.src: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/Utilities/ElectrodeChange.dat: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/Utilities/RedRabbit.dat: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/Utilities/capchange.dat: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/Utilities/capchange.src: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/Utilities/electrodechange.src: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/Utilities/redrabbit.src: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/Centerline/CENTERLINE_HOME.src: this is the pre-cleanup file: the cleaned program was not loaded or was overwritten
- FAIL: KRC/R1/Program/Centerline/PRELOAD.src: this is the pre-cleanup file: the cleaned program was not loaded or was overwritten
- FAIL: KRC/R1/Program/Centerline/Request_next_nut.src: this is the pre-cleanup file: the cleaned program was not loaded or was overwritten
- FAIL: KRC/R1/Program/Centerline/centerline_weld.src: edited on top of the pre-cleanup file (comments match the archive as received 21%, the base 10%)
- FAIL: KRC/R1/Program/HOME.src: edited on top of the pre-cleanup file (comments match the archive as received 100%, the base 57%)
- FAIL: KRC/R1/Program/StyleApps/Options/style1app2opt1.src: edited on top of the pre-cleanup file (comments match the archive as received 7%, the base 3%)
- FAIL: KRC/R1/Program/StyleApps/Options/style1app2opt2.src: edited on top of the pre-cleanup file (comments match the archive as received 9%, the base 4%)
- FAIL: KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src: edited on top of the pre-cleanup file (comments match the archive as received 100%, the base 8%)
- FAIL: KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.dat: this is the pre-cleanup file: the cleaned program was not loaded or was overwritten
- FAIL: KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src: this is the pre-cleanup file: the cleaned program was not loaded or was overwritten
- FAIL: KRC/R1/Program/StylePicks/Options/style1pick1opt1.dat: this is the pre-cleanup file: the cleaned program was not loaded or was overwritten
- FAIL: KRC/R1/Program/StylePicks/Options/style1pick1opt1.src: edited on top of the pre-cleanup file (comments match the archive as received 11%, the base 4%)
- FAIL: KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.dat: this is the pre-cleanup file: the cleaned program was not loaded or was overwritten
- FAIL: KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src: edited on top of the pre-cleanup file (comments match the archive as received 11%, the base 4%)
- FAIL: KRC/R1/Program/StylePicks/Options/style1pick1opt2.src: edited on top of the pre-cleanup file (comments match the archive as received 11%, the base 4%)
- FAIL: KRC/R1/Program/Styles/style_1.dat: this is the pre-cleanup file: the cleaned program was not loaded or was overwritten
- FAIL: KRC/R1/Program/Styles/style_1.src: edited on top of the pre-cleanup file (comments match the archive as received 15%, the base 6%)
- FAIL: KRC/R1/Program/Utilities/RejectGE4.dat: this is the pre-cleanup file: the cleaned program was not loaded or was overwritten
- FAIL: KRC/R1/Program/Utilities/RejectGE4.src: this is the pre-cleanup file: the cleaned program was not loaded or was overwritten
- FAIL: KRC/R1/Program/Utilities/closeandcheckallclamps.src: edited on top of the pre-cleanup file (comments match the archive as received 100%, the base 10%)
- FAIL: KRC/R1/Program/Utilities/gunelectrodechange.src: this is the pre-cleanup file: the cleaned program was not loaded or was overwritten
- FAIL: KRC/R1/Program/Utilities/hometopounce.src: this is the pre-cleanup file: the cleaned program was not loaded or was overwritten
- FAIL: KRC/R1/Program/Utilities/hometorepair.src: this is the pre-cleanup file: the cleaned program was not loaded or was overwritten
- FAIL: KRC/R1/Program/Utilities/openandcheckallclamps.src: edited on top of the pre-cleanup file (comments match the archive as received 100%, the base 11%)
- FAIL: KRC/R1/Program/Utilities/pouncetohome.src: this is the pre-cleanup file: the cleaned program was not loaded or was overwritten
- FAIL: KRC/R1/Program/Utilities/repairtohome.src: this is the pre-cleanup file: the cleaned program was not loaded or was overwritten
- FAIL: KRC/R1/Program/masref_user.src: edited on top of the pre-cleanup file (comments match the archive as received 100%, the base 0%)
- FAIL: KRC/R1/Program/tm_useraction.src: this is the pre-cleanup file: the cleaned program was not loaded or was overwritten
- FAIL: KRC/R1/System/$config.dat: edited on top of the pre-cleanup file (comments match the archive as received 100%, the base 85%)
- FAIL: KRC/R1/System/sps.sub: edited on top of the pre-cleanup file (comments match the archive as received 64%, the base 10%)
- FAIL: KRC/R1/TP/AutomationCore/automationcoredata.dat: edited on top of the pre-cleanup file (comments match the archive as received 100%, the base 90%)
- FAIL: KRC/R1/TP/AutomationCore/automationcoreroutines.dat: edited on top of the pre-cleanup file (comments match the archive as received 97%, the base 65%)
- FAIL: KRC/R1/TP/GripperSpotTech/grp_func.dat: this is the pre-cleanup file: the cleaned program was not loaded or was overwritten
- FAIL: KRC/R1/TP/NutWeld/nutweldroutines.dat: edited on top of the pre-cleanup file (comments match the archive as received 99%, the base 94%)
- FAIL: KRC/R1/cell.src: this is the pre-cleanup file: the cleaned program was not loaded or was overwritten
- FAIL: KRC/R1/safetest.src: this is the pre-cleanup file: the cleaned program was not loaded or was overwritten
- WARN: 8 file(s) of the base missing from the backup - deleted on the robot, or an incomplete archive (e.g. KRC/R1/Program/StyleApps/Options/style1app1opt1.dat; all in Files, "Missing from the backup")
- INFO: KRC/R1/Program/StyleApps/Options/style1app2opt1autorr.src: spelled KRC/R1/Program/StyleApps/Options/style1app2opt1AutoRR.src in the base (the controller ignores case)
- INFO: KRC/R1/Program/StyleApps/Options/style1app2opt2autorr.src: spelled KRC/R1/Program/StyleApps/Options/style1app2opt2AutoRR.src in the base (the controller ignores case)
- INFO: KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.src: spelled KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src in the base (the controller ignores case)
- INFO: KRC/R1/TP/AutomationCore/automationcoredata.dat: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- INFO: KRC/R1/TP/AutomationCore/automationcoreroutines.dat: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- INFO: KRC/R1/TP/NutWeld/nutweldroutines.dat: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)

## Deleted modules still present

The cleanup deleted these modules. A restore does not delete files, so they are still on the controller: delete them there (navigator, expert mode).

- `KRC/R1/Program/CK1STXXX.dat` - identical to the archive as received
- `KRC/R1/Program/CK1STXXX.src` - identical to the archive as received
- `KRC/R1/Program/Centerline/CENTERLINE_WELD1.src` - identical to the archive as received
- `KRC/R1/Program/Centerline/centerline_loop.src` - identical to the archive as received
- `KRC/R1/Program/Centerline/trigger1.dat` - identical to the archive as received
- `KRC/R1/Program/Centerline/trigger1.src` - identical to the archive as received
- `KRC/R1/Program/Centerline/trigger2.dat` - identical to the archive as received
- `KRC/R1/Program/Centerline/trigger2.src` - identical to the archive as received
- `KRC/R1/Program/Centerline/trigger3.dat` - identical to the archive as received
- `KRC/R1/Program/Centerline/trigger3.src` - identical to the archive as received
- `KRC/R1/Program/POUNCE.dat` - identical to the archive as received
- `KRC/R1/Program/POUNCE.src` - identical to the archive as received
- `KRC/R1/Program/StyleApps/Options/style1app2opt1AutoRR.dat` - identical to the archive as received
- `KRC/R1/Program/StyleApps/Options/style1app2opt1AutoRR.src` - MODIFIED since the archive as received
- `KRC/R1/Program/StyleApps/Options/style1app2opt2AutoRR.dat` - identical to the archive as received
- `KRC/R1/Program/StyleApps/Options/style1app2opt2AutoRR.src` - MODIFIED since the archive as received
- `KRC/R1/Program/Utilities/ElectrodeChange.dat` - identical to the archive as received
- `KRC/R1/Program/Utilities/RedRabbit.dat` - identical to the archive as received
- `KRC/R1/Program/Utilities/capchange.dat` - identical to the archive as received
- `KRC/R1/Program/Utilities/capchange.src` - identical to the archive as received
- `KRC/R1/Program/Utilities/electrodechange.src` - identical to the archive as received
- `KRC/R1/Program/Utilities/redrabbit.src` - identical to the archive as received

## Pre-cleanup files

**These files are byte-for-byte the archive as received: the cleaned program was not loaded or was overwritten. Every comment correction, header and junk removal of the cleanup is lost in them.**

- `KRC/R1/Program/Centerline/CENTERLINE_HOME.src`
- `KRC/R1/Program/Centerline/PRELOAD.src`
- `KRC/R1/Program/Centerline/Request_next_nut.src`
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.dat`
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src`
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.dat`
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.dat`
- `KRC/R1/Program/Styles/style_1.dat`
- `KRC/R1/Program/Utilities/RejectGE4.dat`
- `KRC/R1/Program/Utilities/RejectGE4.src`
- `KRC/R1/Program/Utilities/gunelectrodechange.src`
- `KRC/R1/Program/Utilities/hometopounce.src`
- `KRC/R1/Program/Utilities/hometorepair.src`
- `KRC/R1/Program/Utilities/pouncetohome.src`
- `KRC/R1/Program/Utilities/repairtohome.src`
- `KRC/R1/Program/tm_useraction.src`
- `KRC/R1/TP/GripperSpotTech/grp_func.dat`
- `KRC/R1/cell.src`
- `KRC/R1/safetest.src`

Edited on top of the pre-cleanup file (its comments are closer to the archive as received than to the base):

- `KRC/R1/Program/Centerline/centerline_weld.src`
- `KRC/R1/Program/HOME.src`
- `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`
- `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src`
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`
- `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`
- `KRC/R1/Program/Styles/style_1.src`
- `KRC/R1/Program/Utilities/closeandcheckallclamps.src`
- `KRC/R1/Program/Utilities/openandcheckallclamps.src`
- `KRC/R1/Program/masref_user.src`
- `KRC/R1/System/$config.dat`
- `KRC/R1/System/sps.sub`
- `KRC/R1/TP/AutomationCore/automationcoredata.dat`
- `KRC/R1/TP/AutomationCore/automationcoreroutines.dat`
- `KRC/R1/TP/NutWeld/nutweldroutines.dat`

## Files

### Changed (58)

- `C/KRC/User/ConfigMon.ini` - controller configuration - binary, 2606 bytes
- `C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8.wvs` - controller configuration - binary, 5566464 bytes
- `KRC/R1/Program/Centerline/CENTERLINE_HOME.src` - integrator program - PRE-CLEANUP FILE (mechanical checks skipped)
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src` - integrator program
- `KRC/R1/Program/Centerline/PRELOAD.src` - integrator program - PRE-CLEANUP FILE (mechanical checks skipped)
- `KRC/R1/Program/Centerline/Request_next_nut.src` - integrator program - PRE-CLEANUP FILE (mechanical checks skipped)
- `KRC/R1/Program/Centerline/centerline_weld.src` - integrator program
- `KRC/R1/Program/Centerline/gun_open_check.dat` - integrator program
- `KRC/R1/Program/HOME.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app2opt1.dat` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app2opt1.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app2opt2.dat` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app2opt2.src` - integrator program
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.dat` - integrator program
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src` - integrator program
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.dat` - integrator program - PRE-CLEANUP FILE (mechanical checks skipped)
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src` - integrator program - PRE-CLEANUP FILE (mechanical checks skipped)
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.dat` - integrator program - PRE-CLEANUP FILE (mechanical checks skipped)
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.dat` - integrator program - PRE-CLEANUP FILE (mechanical checks skipped)
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt2.dat` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src` - integrator program
- `KRC/R1/Program/Styles/style_1.dat` - integrator program - PRE-CLEANUP FILE (mechanical checks skipped)
- `KRC/R1/Program/Styles/style_1.src` - integrator program
- `KRC/R1/Program/Utilities/RejectGE4.dat` - integrator program - PRE-CLEANUP FILE (mechanical checks skipped)
- `KRC/R1/Program/Utilities/RejectGE4.src` - integrator program - PRE-CLEANUP FILE (mechanical checks skipped)
- `KRC/R1/Program/Utilities/closeandcheckallclamps.dat` - integrator program
- `KRC/R1/Program/Utilities/closeandcheckallclamps.src` - integrator program
- `KRC/R1/Program/Utilities/gunelectrodechange.src` - integrator program - PRE-CLEANUP FILE (mechanical checks skipped)
- `KRC/R1/Program/Utilities/hometopounce.src` - integrator program - PRE-CLEANUP FILE (mechanical checks skipped)
- `KRC/R1/Program/Utilities/hometorepair.src` - integrator program - PRE-CLEANUP FILE (mechanical checks skipped)
- `KRC/R1/Program/Utilities/openandcheckallclamps.dat` - integrator program
- `KRC/R1/Program/Utilities/openandcheckallclamps.src` - integrator program
- `KRC/R1/Program/Utilities/pouncetohome.src` - integrator program - PRE-CLEANUP FILE (mechanical checks skipped)
- `KRC/R1/Program/Utilities/repairtohome.src` - integrator program - PRE-CLEANUP FILE (mechanical checks skipped)
- `KRC/R1/Program/home.dat` - integrator program
- `KRC/R1/Program/masref_user.dat` - integrator program
- `KRC/R1/Program/masref_user.src` - integrator program
- `KRC/R1/Program/tm_useraction.src` - integrator program - PRE-CLEANUP FILE (mechanical checks skipped)
- `KRC/R1/System/$config.dat` - integrator program
- `KRC/R1/System/sps.sub` - integrator program
- `KRC/R1/System/tm_bib.dat` - KUKA system / vendor package
- `KRC/R1/System/tm_bib.src` - KUKA system / vendor package
- `KRC/R1/TP/AutomationCore/automationcoredata.dat` - KUKA system / vendor package
- `KRC/R1/TP/AutomationCore/automationcoreroutines.dat` - KUKA system / vendor package
- `KRC/R1/TP/BrakeTest/braketestback.dat` - KUKA system / vendor package
- `KRC/R1/TP/BrakeTest/braketestback.src` - KUKA system / vendor package
- `KRC/R1/TP/BrakeTest/braketestreq.dat` - KUKA system / vendor package
- `KRC/R1/TP/BrakeTest/braketestreq.src` - KUKA system / vendor package
- `KRC/R1/TP/BrakeTest/braketeststart.dat` - KUKA system / vendor package
- `KRC/R1/TP/BrakeTest/braketeststart.src` - KUKA system / vendor package
- `KRC/R1/TP/GripperSpotTech/grp_func.dat` - KUKA system / vendor package - PRE-CLEANUP FILE (mechanical checks skipped)
- `KRC/R1/TP/NutWeld/nutweldroutines.dat` - KUKA system / vendor package
- `KRC/R1/cell.src` - integrator program - PRE-CLEANUP FILE (mechanical checks skipped)
- `KRC/R1/safetest.src` - integrator program - PRE-CLEANUP FILE (mechanical checks skipped)
- `Registry/LMSOFTWAREKUKA ROBOTER GMBHKUKA BOFOCX Control'sFileHandler.amr` - controller configuration - 1 line(s) removed, 1 added - diffs/Registry/LMSOFTWAREKUKA ROBOTER GMBHKUKA BOFOCX Control'sFileHandler.amr.diff
- `am.ini` - archive metadata - 2 line(s) removed, 2 added - diffs/am.ini.diff

### Added (14)

- `KRC/R1/Program/StyleApps/Options/style1app1opt1A.dat` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt1A.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt1B.dat` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt1B.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt2A.dat` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt2A.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt2B.dat` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt2B.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt3A.dat` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt3A.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt3B.dat` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt3B.src` - integrator program
- `KRC/R1/Program/Styles/optiones/style1opt1.src` - integrator program
- `KRC/R1/Program/Styles/optiones/style1opt10autorr.src` - integrator program

### Missing from the backup (8)

- `KRC/R1/Program/StyleApps/Options/style1app1opt1.dat`
- `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`
- `KRC/R1/Program/StyleApps/Options/style1app1opt2.dat`
- `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`
- `KRC/R1/Program/StyleApps/Options/style1app1opt3.dat`
- `KRC/R1/Program/StyleApps/Options/style1app1opt3.src`
- `KRC/R1/Program/Styles/Options/Style1Opt10AutoRR.src`
- `KRC/R1/Program/Styles/Options/style1opt1.src`

### Outside the archive layout (ignored) (0)

_none_

## Code changes

### `KRC/R1/Program/Centerline/CENTERLINE_HOME.src`

changed, integrator program: 18 code line(s) removed, 18 added; 66 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/CENTERLINE_HOME.src.diff](diffs/KRC/R1/Program/Centerline/CENTERLINE_HOME.src.diff)

Attributes: &COMMENT 03-10-R1 PNW1 MANUAL HOME -> &COMMENT CENTERLINE HOME

```diff
@@ base line 6, backup line 6 @@
      6  DEF CENTERLINE_HOME()
-    28  CL_GunPressureCmd=CL_GUN_PRESS_BASE
-    33  dopw1_Nut1Intensify_Home=FALSE
-    34  dopw1_StartWater=FALSE
-    35  dopw1_StartFeed=FALSE
-    38  dopw1_BlowOff=FALSE
-    39  do500Reserved=FALSE
-    40  do505QFPNutBlowOff=FALSE
-    44  dopw1_AdvancePin=FALSE
+    31  CL_GunPressureCmd=405
+    35  $OUT[473]=FALSE
+    36  $OUT[475]=FALSE
+    37  $OUT[476]=FALSE
+    38  $OUT[494]=FALSE
+    39  $OUT[500]=FALSE
+    40  $OUT[505]=FALSE
+    43  $OUT[495]=FALSE
     44  WAIT SEC 0.2
-    46  dopw1_ReturnPin=TRUE
+    45  $OUT[496]=TRUE
     46  WAIT SEC 1.0
-    51  do503QFPAdvance=FALSE
+    49  $OUT[503]=FALSE
     50  WAIT SEC 0.2
-    53  do504QFPReturn=TRUE
-    55  WAIT FOR dipw1_SpearHome
+    51  $OUT[504]=TRUE
+    52  WAIT FOR $IN[482]
     53  WAIT SEC 0.5
-    60  do498UpperPinExtend=FALSE
+    56  $OUT[498]=FALSE
     57  WAIT SEC 0.2
-    62  do499UpperPinRetract=TRUE
+    58  $OUT[499]=TRUE
     59  WAIT SEC 1.0
-    67  dopw1_GunWork=FALSE
+    62  $OUT[472]=FALSE
     63  WAIT SEC 0.2
-    69  dopw1_GunHome=TRUE
+    64  $OUT[471]=TRUE
     65  WAIT SEC 1.5
-    74  do501PartClampClose=FALSE
+    68  $OUT[501]=FALSE
     69  WAIT SEC 0.2
-    76  do502PartClampOpen=TRUE
+    70  $OUT[502]=TRUE
     71  WAIT SEC 1.0
     73  END
```

### `KRC/R1/Program/Centerline/PRELOAD.src`

changed, integrator program: 30 code line(s) removed, 30 added; 279 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/PRELOAD.src.diff](diffs/KRC/R1/Program/Centerline/PRELOAD.src.diff)

Attributes: -&COMMENT 03-10-R1 PNW1 NUT PRELOAD

```diff
@@ base line 3, backup line 2 @@
      2  DEF PRELOAD ( )
-    33  IF NUT_START AND NOT NUTCYCLE_ACTIVE THEN
-    35  NUT_START=FALSE
+     5  IF NUT_STAR AND NOT NUTCYCLE_ACTIVE THEN
+     7  NUT_STAR=FALSE
      8  NUTCYCLE_ACTIVE=TRUE
      9  NUT_READY=FALSE
@@ base line 57, backup line 28 @@
     28  SWITCH NUT_PRELOAD_STEP
     30  CASE 0
-    63  do503QFPAdvance=FALSE
-    64  do504QFPReturn=TRUE
-    68  IF (dipw1_SpearHome==TRUE) AND (di470QFPAdvanced==FALSE) THEN
-    71  dopw1_StartFeed=TRUE
-    72  dopw1_BlowOff=FALSE
+    33  $OUT[503]=FALSE
+    34  $OUT[504]=TRUE
+    37  IF ($IN[482]==TRUE) AND ($IN[470]==FALSE) THEN
+    39  $OUT[476]=TRUE
+    40  $OUT[494]=FALSE
     42  IF $TIMER_STOP[10] THEN
     43  $TIMER[10]=0
@@ base line 93, backup line 59 @@
     59  CASE 10
     61  IF STEP0DONE THEN
-   100  dopw1_GunWork=FALSE
-   101  dopw1_GunHome=TRUE
-   104  do498UpperPinExtend=FALSE
-   105  do499UpperPinRetract=TRUE
-   108  do501PartClampClose=FALSE
-   109  do502PartClampOpen=TRUE
+    65  $OUT[472]=FALSE
+    66  $OUT[471]=TRUE
+    68  $OUT[498]=FALSE
+    69  $OUT[499]=TRUE
+    71  $OUT[501]=FALSE
+    72  $OUT[502]=TRUE
     74  IF NOT STEP10_ADV_STARTED THEN
-   114  dopw1_BlowOff=TRUE
-   116  do503QFPAdvance=FALSE
-   117  do504QFPReturn=TRUE
-   121  IF (dipw1_SpearHome==TRUE) AND (di470QFPAdvanced==FALSE) THEN
+    75  $OUT[494]=TRUE
+    77  $OUT[503]=FALSE
+    78  $OUT[504]=TRUE
+    80  IF ($IN[482]==TRUE) AND ($IN[470]==FALSE) THEN
     81  STEP10_ADV_STARTED=TRUE
     83  ENDIF
     84  ELSE
-   129  do504QFPReturn=FALSE
-   130  do503QFPAdvance=TRUE
-   131  dopw1_StartFeed=FALSE
-   135  IF (di470QFPAdvanced==TRUE) AND (dipw1_SpearHome==FALSE) THEN
-   137  do505QFPNutBlowOff=TRUE
-   138  dopw1_BlowOff=FALSE
+    87  $OUT[504]=FALSE
+    88  $OUT[503]=TRUE
+    89  $OUT[476]=FALSE
+    91  IF ($IN[470]==TRUE) AND ($IN[482]==FALSE) THEN
```
_27 more lines: see diffs/KRC/R1/Program/Centerline/PRELOAD.src.diff_

### `KRC/R1/Program/Centerline/Request_next_nut.src`

changed, integrator program: 2 code line(s) removed, 2 added; 19 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/Request_next_nut.src.diff](diffs/KRC/R1/Program/Centerline/Request_next_nut.src.diff)

Attributes: -&COMMENT 03-10-R1 PNW1 NEXT NUT REQUEST

```diff
@@ base line 3, backup line 2 @@
      2  DEF Request_next_nut ( )
-    20  NEXT_NUT_READY=FALSE
+     4  NEXT_NUT_READY=false
      5  NEXT_NUT_REQUEST=TRUE
-    22  NUT_START=TRUE
+     6  NUT_STAR=TRUE
      8  END
```

### `KRC/R1/Program/Centerline/centerline_weld.src`

changed, integrator program: 57 code line(s) removed, 61 added; 211 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/centerline_weld.src.diff](diffs/KRC/R1/Program/Centerline/centerline_weld.src.diff)

Attributes: &ACCESS RVO1 -> &ACCESS RVP3; -&COMMENT 03-10-R1 PNW1 NUT WELD

```diff
@@ base line 5, backup line 4 @@
      4  DEF CENTERLINE_WELD()
-    58  dopw1_GunWork=FALSE
-    59  dopw1_GunHome=TRUE
-    63  do498UpperPinExtend=FALSE
-    64  do499UpperPinRetract=TRUE
-    67  do501PartClampClose=FALSE
-    68  do502PartClampOpen=TRUE
-    70  WAIT FOR di466PartClampOpen
-    73  dopw1_ReturnPin=FALSE
-    74  dopw1_AdvancePin=TRUE
-    77  do503QFPAdvance=FALSE
-    78  do504QFPReturn=TRUE
-    80  WAIT FOR dipw1_SpearHome
+    51  $OUT[472]=FALSE
+    52  $OUT[471]=TRUE
+    55  $OUT[498]=FALSE
+    56  $OUT[499]=TRUE
+    59  $OUT[501]=FALSE
+    60  $OUT[502]=TRUE
+    61  WAIT FOR $IN[466]
+    64  $OUT[496]=FALSE
+    65  $OUT[495]=TRUE
+    68  $OUT[503]=FALSE
+    69  $OUT[504]=TRUE
+    70  WAIT FOR $IN[482]
     73  IF NOT NUT_READY THEN
-    87  dopw1_ReturnPin=FALSE
-    88  dopw1_AdvancePin=TRUE
-    89  dopw1_BlowOff=TRUE
-    92  do504QFPReturn=FALSE
-    93  do503QFPAdvance=TRUE
-    95  WAIT FOR di470QFPAdvanced
+    75  $OUT[496]=FALSE
+    76  $OUT[495]=TRUE
+    77  $OUT[494]=TRUE
+    80  $OUT[504]=FALSE
+    81  $OUT[503]=TRUE
+    82  WAIT FOR $IN[470]
     85  dopw1_StartFeed=TRUE
     87  dopw1_StartFeed=FALSE
     88  WAIT SEC 1.5
-   104  dopw1_BlowOff=FALSE
-   107  do503QFPAdvance=FALSE
-   108  do504QFPReturn=TRUE
-   110  WAIT FOR dipw1_SpearHome
+    89  $OUT[494]=FALSE
+    92  $OUT[503]=FALSE
+    93  $OUT[504]=TRUE
+    94  WAIT FOR $IN[482]
+    97  $OUT[499]=FALSE
+    98  $OUT[498]=TRUE
     99  ENDIF
-   114  do499UpperPinRetract=FALSE
-   115  do498UpperPinExtend=TRUE
-   118  CL_GunPressureCmd=CL_GUN_PRESS_BASE
+   102  $OUT[499]=FALSE
+   103  $OUT[498]=TRUE
+   107  CL_GunPressureCmd=405
    110  dopw1_WeldInit=FALSE
```
_118 more lines: see diffs/KRC/R1/Program/Centerline/centerline_weld.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt1A.dat`

added, integrator program: 0 code line(s) removed, 113 added; 18 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1A.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1A.dat.diff)

Attributes: +&ACCESS RVP1; +&REL 339; +&COMMENT NUT1; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\TP\Nutweld\Template\NutWeld_Vorgabe; +&PARAM DISKPATH = KRC:\R1\Program\StyleApps\Options

Data changes:

- added 1 BASIS_SUGG_T: LAST_BASIS
- added 1 DEFDAT: style1app1opt1A
- added 30 E6POS: XABOVENUT1, XAboveNut2, XDROP17, XDROP18, XP0, XP1, XP2, XP3, XP4, XP5, XP6, XP7 ...
- added 1 EXT: BAS
- added 30 FDAT: FAboveNut1, FAboveNut2, FDROP17, FDROP18, FP0, FP1, FP2, FP3, FP4, FP5, FP6, FP7 ...
- added 21 LDAT: LCPDAT0, LCPDAT1, LCPDAT2, LCPDAT3, LCPDAT4, LCPDAT5, LCPDAT6, LCPDAT7, LCPDAT8, LCPDAT9, LCPDAT10, LCPDAT11 ...
- added 1 MODULEPARAM_T: LAST_TP_PARAMS
- added 5 NUTWELDDAT: NutData1_11, NutData1_12, NutData1_13, NutWeldDAT1, NutWeldDAT3
- added 1 NUTWELD_SUGG_T: LAST_NutWeld
- added 19 PDAT: PPDAT0, PPDAT1, PPDAT2, PPDAT3, PPDAT4, PPDAT5, PPDAT6, PPDAT7, PPDAT8, PPDAT9, PPDAT10, PPDAT11 ...
- added 1 TM_SUGG_T: LAST_TQM
- added 1 TQM_TQDAT_T: TM1

```diff
@@ base line end, backup line 7 @@
+     7  DEFDAT style1app1opt1A
+    10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
+    17  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    18  DECL E6POS XP10={X 214.483856,Y 193.590897,Z 1005.80865,A 6.59456158,B -23.4313526,C 9.77940178,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    19  DECL FDAT FP10={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    20  DECL E6POS XP20={X -3850.82104,Y -108.397034,Z -435.544800,A -178.432037,B 0.654220462,C -179.967712,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    21  DECL FDAT FP20={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    22  DECL E6POS XP30={X 359.994781,Y 339.042908,Z -58.4685249,A 9.62195110,B 8.87501,C 1.49797690,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    23  DECL FDAT FP30={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    24  DECL E6POS XABOVENUT1={X 134.661209,Y 312.220856,Z -32.0869446,A 8.71582699,B 8.82717705,C 1.11576843,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    25  DECL FDAT FAboveNut1={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    26  DECL LDAT LCPDAT0={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    27  DECL E6POS XAboveNut2={X 38.3333626,Y 318.813446,Z -15.8014164,A 9.53667259,B 8.81424236,C 1.48279762,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    28  DECL FDAT FAboveNut2={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    29  DECL LDAT LCPDAT4={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    30  DECL E6POS XP60={X 214.522202,Y 447.905060,Z 1005.80865,A 6.59456158,B -23.4313526,C 9.77940178,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    31  DECL FDAT FP60={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    32  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    42  DECL NutWeldDAT NutWeldDAT1={GunNr 1,SpotNr 7,Offset 0}
+    43  DECL LDAT XPNW1CPDAT={VEL 0.150000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000}
+    44  DECL FDAT FPNW1={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    45  DECL LDAT LCPDAT6={ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    46  DECL E6POS XPNW1={X 123.774101,Y 312.995331,Z -88.6478,A 8.71582699,B 8.82717705,C 1.11576855,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    47  DECL NutWeldDAT NutWeldDAT3={GunNr 1,SpotNr 8,Offset 0}
+    48  DECL LDAT XPNW5CPDAT={VEL 0.150000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000}
+    49  DECL FDAT FPNW5={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    50  DECL LDAT LCPDAT13={ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    51  DECL E6POS XPNW5={X 29.6411285,Y 320.239532,Z -61.6583595,A 9.53667259,B 8.81424236,C 1.48279774,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    52  DECL PDAT PPDAT6={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    53  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    54  DECL PDAT PPDAT8={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    55  DECL NutWeld_SUGG_T LAST_NutWeld={POINT1[] "PNW1_SPOT7              ",POINT2[] "PNW0                    ",CP_PARAMS[] "CPDATNutWeld0           ",PTP_PARAMS[] "PDATNutWeld0            ",CONT[] "C_PTP                   ",CP_VEL[] "2  [...]
+    56  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P0                      ",POINT2[] "P0                      ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT0                   ",CONT[] "                        ",CP_VEL[] "2      [...]
+    57  DECL E6POS XDROP17={X 254.475,Y 260.666412,Z -295.081390,A -1.28851116,B 6.20056677,C -103.654922,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    58  DECL FDAT FDROP17={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    59  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    60  DECL E6POS XDROP18={X 640.467163,Y -739.926514,Z 98.7580948,A -2.83424330,B 2.72720981,C 59.2469177,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    61  DECL FDAT FDROP18={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    62  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    63  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    64  DECL LDAT LCPDAT2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    65  DECL PDAT PPDAT0={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    66  DECL E6POS XP0={X -3704.29346,Y 1.10223198,Z -449.805786,A -178.368118,B 0.266879767,C 179.968445,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    67  DECL FDAT FP0={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    68  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    69  DECL E6POS XP1={X -1824.18188,Y -1001.09119,Z -157.213959,A -87.6076279,B -4.42733240,C -177.429916,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    70  DECL FDAT FP1={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    71  DECL PDAT PPDAT9={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    72  DECL E6POS XP2={X 502.171722,Y 190.181396,Z -135.596970,A -6.24112272,B -3.20316982,C 176.013672,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    73  DECL FDAT FP2={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    74  DECL PDAT PPDAT10={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    75  DECL E6POS XP3={X 403.314392,Y 226.179260,Z -114.475060,A -6.33512926,B 0.0627186,C 178.051514,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    76  DECL FDAT FP3={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    77  DECL PDAT PPDAT11={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    78  DECL E6POS XP4={X -99.9718552,Y -496.474915,Z -138.682404,A -31.5940628,B -0.774911,C 178.211197,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    79  DECL FDAT FP4={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    80  DECL PDAT PPDAT12={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    81  DECL E6POS XP5={X -3674.25464,Y -4.99133062,Z -444.893219,A -178.368118,B 0.266879946,C 179.968445,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    82  DECL FDAT FP5={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
```
_54 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1A.dat.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt1A.src`

added, integrator program: 0 code line(s) removed, 69 added; 66 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1A.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1A.src.diff)

Attributes: +&ACCESS RVP1; +&REL 339; +&COMMENT NUT1; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\TP\Nutweld\Template\NutWeld_Vorgabe; +&PARAM DISKPATH = KRC:\R1\Program\StyleApps\Options

```diff
@@ base line end, backup line 7 @@
+     7  DEF style1app1opt1A( )
+    26  GLOBAL INTERRUPT DECL 3 WHEN $STOPMESS==TRUE DO IR_STOPM ( )
+    27  INTERRUPT ON 3
+    28  BAS (#INITMOV,0 )
+    40  $BWDSTART=FALSE
+    41  PDAT_ACT=PPDAT0
+    42  FDAT_ACT=FP0
+    43  BAS(#PTP_PARAMS,100)
+    44  PTP XP0 C_DIS
+    47  $BWDSTART=FALSE
+    48  LDAT_ACT=LCPDAT12
+    49  FDAT_ACT=FP8
+    50  BAS(#CP_PARAMS,2)
+    51  LIN XP8 C_DIS C_DIS
+    63  INTERRUPT DECL 20 WHEN CL_GunStrokePositionLPT<137000 DO GUN_OPEN_LOST()
+    64  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
+    65  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
+    68  LOOP
+    69  WAIT FOR NUT_READY== TRUE
+    71  GUN_OPEN_CHECK()
+    72  INTERRUPT ON 20
+    73  INTERRUPT ON 21
+    74  INTERRUPT ON 22
+    76  $BWDSTART=FALSE
+    77  LDAT_ACT=LCPDAT8
+    78  FDAT_ACT=FP20
+    79  BAS(#CP_PARAMS,2)
+    80  LIN XP20 C_DIS C_DIS
+    83  IF di004UseDryCycle==FALSE THEN
+    87  $BWDSTART=FALSE
+    88  LDAT_ACT=LCPDAT18
+    89  FDAT_ACT=FP19
+    90  BAS(#CP_PARAMS,2)
+    91  LIN XP19
+    93  WAIT SEC 0
+    94  INTERRUPT OFF 20
+    95  INTERRUPT OFF 21
+    96  INTERRUPT OFF 22
+    97  CENTERLINE_WELD()
+    98  INTERRUPT ON 20
+    99  INTERRUPT ON 21
+   100  INTERRUPT ON 22
+   102  ENDIF
+   105  $BWDSTART=FALSE
+   106  LDAT_ACT=LCPDAT16
+   107  FDAT_ACT=FP20
+   108  BAS(#CP_PARAMS,2)
+   109  LIN XP20 C_DIS C_DIS
+   113  WAIT SEC 0
+   114  INTERRUPT OFF 20
+   115  INTERRUPT OFF 21
+   116  INTERRUPT OFF 22
+   118  IF NOT NUT_WELD_RETRY THEN
+   119  EXIT
+   120  ENDIF
+   121  NUT_WELD_RETRY=FALSE
+   122  ENDLOOP
+   126  $BWDSTART=FALSE
+   127  LDAT_ACT=LCPDAT17
```
_10 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1A.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt1B.dat`

added, integrator program: 0 code line(s) removed, 113 added; 18 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1B.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1B.dat.diff)

Attributes: +&ACCESS RVO2; +&REL 1; +&COMMENT NUT1; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\TP\Nutweld\Template\NutWeld_Vorgabe; +&PARAM DISKPATH = KRC:\R1\Program\StyleApps\Options

Data changes:

- added 1 BASIS_SUGG_T: LAST_BASIS
- added 1 DEFDAT: style1app1opt1B
- added 30 E6POS: XABOVENUT1, XAboveNut2, XDROP17, XDROP18, XP0, XP1, XP2, XP3, XP4, XP5, XP6, XP7 ...
- added 1 EXT: BAS
- added 30 FDAT: FAboveNut1, FAboveNut2, FDROP17, FDROP18, FP0, FP1, FP2, FP3, FP4, FP5, FP6, FP7 ...
- added 21 LDAT: LCPDAT0, LCPDAT1, LCPDAT2, LCPDAT3, LCPDAT4, LCPDAT5, LCPDAT6, LCPDAT7, LCPDAT8, LCPDAT9, LCPDAT10, LCPDAT11 ...
- added 1 MODULEPARAM_T: LAST_TP_PARAMS
- added 5 NUTWELDDAT: NutData1_11, NutData1_12, NutData1_13, NutWeldDAT1, NutWeldDAT3
- added 1 NUTWELD_SUGG_T: LAST_NutWeld
- added 19 PDAT: PPDAT0, PPDAT1, PPDAT2, PPDAT3, PPDAT4, PPDAT5, PPDAT6, PPDAT7, PPDAT8, PPDAT9, PPDAT10, PPDAT11 ...
- added 1 TM_SUGG_T: LAST_TQM
- added 1 TQM_TQDAT_T: TM1

```diff
@@ base line end, backup line 7 @@
+     7  DEFDAT style1app1opt1B
+    10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
+    17  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    18  DECL E6POS XP10={X 214.483856,Y 193.590897,Z 1005.80865,A 6.59456158,B -23.4313526,C 9.77940178,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    19  DECL FDAT FP10={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    20  DECL E6POS XP20={X -3850.82104,Y -108.397034,Z -430.314789,A -178.432037,B 0.654220343,C -179.967712,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    21  DECL FDAT FP20={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    22  DECL E6POS XP30={X 359.994781,Y 339.042908,Z -58.4685249,A 9.62195110,B 8.87501,C 1.49797690,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    23  DECL FDAT FP30={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    24  DECL E6POS XABOVENUT1={X 134.661209,Y 312.220856,Z -32.0869446,A 8.71582699,B 8.82717705,C 1.11576843,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    25  DECL FDAT FAboveNut1={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    26  DECL LDAT LCPDAT0={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    27  DECL E6POS XAboveNut2={X 38.3333626,Y 318.813446,Z -15.8014164,A 9.53667259,B 8.81424236,C 1.48279762,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    28  DECL FDAT FAboveNut2={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    29  DECL LDAT LCPDAT4={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    30  DECL E6POS XP60={X 214.522202,Y 447.905060,Z 1005.80865,A 6.59456158,B -23.4313526,C 9.77940178,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    31  DECL FDAT FP60={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    32  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    42  DECL NutWeldDAT NutWeldDAT1={GunNr 1,SpotNr 7,Offset 0}
+    43  DECL LDAT XPNW1CPDAT={VEL 0.150000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000}
+    44  DECL FDAT FPNW1={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    45  DECL LDAT LCPDAT6={ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    46  DECL E6POS XPNW1={X 123.774101,Y 312.995331,Z -88.6478,A 8.71582699,B 8.82717705,C 1.11576855,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    47  DECL NutWeldDAT NutWeldDAT3={GunNr 1,SpotNr 8,Offset 0}
+    48  DECL LDAT XPNW5CPDAT={VEL 0.150000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000}
+    49  DECL FDAT FPNW5={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    50  DECL LDAT LCPDAT13={ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    51  DECL E6POS XPNW5={X 29.6411285,Y 320.239532,Z -61.6583595,A 9.53667259,B 8.81424236,C 1.48279774,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    52  DECL PDAT PPDAT6={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    53  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    54  DECL PDAT PPDAT8={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    55  DECL NutWeld_SUGG_T LAST_NutWeld={POINT1[] "PNW1_SPOT7              ",POINT2[] "PNW0                    ",CP_PARAMS[] "CPDATNutWeld0           ",PTP_PARAMS[] "PDATNutWeld0            ",CONT[] "C_PTP                   ",CP_VEL[] "2  [...]
+    56  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P0                      ",POINT2[] "P0                      ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT0                   ",CONT[] "                        ",CP_VEL[] "2      [...]
+    57  DECL E6POS XDROP17={X 254.475,Y 260.666412,Z -295.081390,A -1.28851116,B 6.20056677,C -103.654922,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    58  DECL FDAT FDROP17={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    59  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    60  DECL E6POS XDROP18={X 640.467163,Y -739.926514,Z 98.7580948,A -2.83424330,B 2.72720981,C 59.2469177,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    61  DECL FDAT FDROP18={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    62  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    63  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    64  DECL LDAT LCPDAT2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    65  DECL PDAT PPDAT0={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    66  DECL E6POS XP0={X -3704.29346,Y 1.10223198,Z -449.805786,A -178.368118,B 0.266879767,C 179.968445,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    67  DECL FDAT FP0={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    68  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    69  DECL E6POS XP1={X -1824.18188,Y -1001.09119,Z -157.213959,A -87.6076279,B -4.42733240,C -177.429916,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    70  DECL FDAT FP1={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    71  DECL PDAT PPDAT9={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    72  DECL E6POS XP2={X 502.171722,Y 190.181396,Z -135.596970,A -6.24112272,B -3.20316982,C 176.013672,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    73  DECL FDAT FP2={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    74  DECL PDAT PPDAT10={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    75  DECL E6POS XP3={X 403.314392,Y 226.179260,Z -114.475060,A -6.33512926,B 0.0627186,C 178.051514,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    76  DECL FDAT FP3={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    77  DECL PDAT PPDAT11={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    78  DECL E6POS XP4={X -99.9718552,Y -496.474915,Z -138.682404,A -31.5940628,B -0.774911,C 178.211197,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    79  DECL FDAT FP4={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    80  DECL PDAT PPDAT12={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    81  DECL E6POS XP5={X -3674.25464,Y -4.99133062,Z -444.893219,A -178.368118,B 0.266879946,C 179.968445,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    82  DECL FDAT FP5={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
```
_54 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1B.dat.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt1B.src`

added, integrator program: 0 code line(s) removed, 69 added; 66 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1B.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1B.src.diff)

Attributes: +&ACCESS RVO2; +&REL 1; +&COMMENT NUT1; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\TP\Nutweld\Template\NutWeld_Vorgabe; +&PARAM DISKPATH = KRC:\R1\Program\StyleApps\Options

```diff
@@ base line end, backup line 7 @@
+     7  DEF style1app1opt1B( )
+    26  GLOBAL INTERRUPT DECL 3 WHEN $STOPMESS==TRUE DO IR_STOPM ( )
+    27  INTERRUPT ON 3
+    28  BAS (#INITMOV,0 )
+    40  $BWDSTART=FALSE
+    41  PDAT_ACT=PPDAT0
+    42  FDAT_ACT=FP0
+    43  BAS(#PTP_PARAMS,100)
+    44  PTP XP0 C_DIS
+    47  $BWDSTART=FALSE
+    48  LDAT_ACT=LCPDAT12
+    49  FDAT_ACT=FP8
+    50  BAS(#CP_PARAMS,2)
+    51  LIN XP8 C_DIS C_DIS
+    63  INTERRUPT DECL 20 WHEN CL_GunStrokePositionLPT<137000 DO GUN_OPEN_LOST()
+    64  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
+    65  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
+    68  LOOP
+    69  WAIT FOR NUT_READY== TRUE
+    71  GUN_OPEN_CHECK()
+    72  INTERRUPT ON 20
+    73  INTERRUPT ON 21
+    74  INTERRUPT ON 22
+    76  $BWDSTART=FALSE
+    77  LDAT_ACT=LCPDAT8
+    78  FDAT_ACT=FP20
+    79  BAS(#CP_PARAMS,2)
+    80  LIN XP20 C_DIS C_DIS
+    83  IF di004UseDryCycle==FALSE THEN
+    87  $BWDSTART=FALSE
+    88  LDAT_ACT=LCPDAT18
+    89  FDAT_ACT=FP19
+    90  BAS(#CP_PARAMS,2)
+    91  LIN XP19
+    93  WAIT SEC 0
+    94  INTERRUPT OFF 20
+    95  INTERRUPT OFF 21
+    96  INTERRUPT OFF 22
+    97  CENTERLINE_WELD()
+    98  INTERRUPT ON 20
+    99  INTERRUPT ON 21
+   100  INTERRUPT ON 22
+   102  ENDIF
+   105  $BWDSTART=FALSE
+   106  LDAT_ACT=LCPDAT16
+   107  FDAT_ACT=FP20
+   108  BAS(#CP_PARAMS,2)
+   109  LIN XP20 C_DIS C_DIS
+   113  WAIT SEC 0
+   114  INTERRUPT OFF 20
+   115  INTERRUPT OFF 21
+   116  INTERRUPT OFF 22
+   118  IF NOT NUT_WELD_RETRY THEN
+   119  EXIT
+   120  ENDIF
+   121  NUT_WELD_RETRY=FALSE
+   122  ENDLOOP
+   126  $BWDSTART=FALSE
+   127  LDAT_ACT=LCPDAT17
```
_10 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1B.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt2A.dat`

added, integrator program: 0 code line(s) removed, 151 added; 11 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2A.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2A.dat.diff)

Attributes: +&ACCESS  RV; +&COMMENT GE4_002_GUN1; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\TP\Nutweld\Template\NutWeld_Vorgabe; +&PARAM DISKPATH = KRC:\R1\Program\StyleApps\Options; +&REL 246

Data changes:

- added 1 BASIS_SUGG_T: LAST_BASIS
- added 1 DEFDAT: style1app1opt2A
- added 42 E6POS: XAboveNut3, XAboveNut4, XAboveNut6, XDROP21, XDROP22, XDROP23, XDROP24, XDROP25, XDROP26, XDROP31, XDROP32, XP0 ...
- added 1 EXT: BAS
- added 42 FDAT: FAboveNut3, FAboveNut4, FAboveNut6, FDROP21, FDROP22, FDROP23, FDROP24, FDROP25, FDROP26, FDROP31, FDROP32, FP0 ...
- added 29 LDAT: LCPDAT0, LCPDAT1, LCPDAT2, LCPDAT3, LCPDAT4, LCPDAT5, LCPDAT6, LCPDAT7, LCPDAT8, LCPDAT9, LCPDAT10, LCPDAT11 ...
- added 3 NUTWELDDAT: NutWeldDAT4, NutWeldDAT6, NutWeldDAT8
- added 1 NUTWELD_SUGG_T: LAST_NutWeld
- added 30 PDAT: PPDAT0, PPDAT1, PPDAT2, PPDAT3, PPDAT4, PPDAT5, PPDAT6, PPDAT7, PPDAT8, PPDAT9, PPDAT10, PPDAT11 ...

```diff
@@ base line end, backup line 7 @@
+     7  DEFDAT style1app1opt2A
+    10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
+    17  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    18  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    19  DECL LDAT LCPDAT4={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    20  DECL E6POS XP10={X -1783.28369,Y -204.411,Z 1353.11560,A 22.6009655,B -85.8094482,C -23.7340908,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    21  DECL FDAT FP10={TOOL_NO 3,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    22  DECL E6POS XAboveNut3={X -303.780243,Y 813.191772,Z 166.218750,A 57.0816841,B -0.384623110,C -0.00601434475,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    23  DECL FDAT FAboveNut3={TOOL_NO 3,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    24  DECL E6POS XAboveNut4={X -347.034637,Y 785.924500,Z 174.869568,A 56.8305,B -0.0316173770,C 0.561762750,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    25  DECL FDAT FAboveNut4={TOOL_NO 3,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    26  DECL E6POS XP70={X -29.1782665,Y 976.513794,Z 395.040894,A 39.0784416,B -7.62199688,C -6.57393408,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    27  DECL FDAT FP70={TOOL_NO 3,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    28  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    29  DECL E6POS XP80={X 290.249634,Y 607.626892,Z -209.393982,A -8.90244770,B 0.239384755,C 178.080566,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    30  DECL FDAT FP80={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    31  DECL LDAT LCPDAT7={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    32  DECL LDAT LCPDAT8={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    33  DECL E6POS XAboveNut6={X -336.120819,Y 902.973755,Z 176.529984,A 58.7987671,B -0.490157604,C -0.146124393,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    34  DECL FDAT FAboveNut6={TOOL_NO 3,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    35  DECL E6POS XP100={X -194.562393,Y 1020.65479,Z 164.107071,A 56.8293304,B 0.00100069749,C 3.79618939E-07,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    36  DECL FDAT FP100={TOOL_NO 3,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    37  DECL LDAT LCPDAT9={VEL 2.00000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    38  DECL E6POS XP110={X -204.560745,Y 1246.33264,Z 194.087265,A 49.2418823,B 0.000983044622,C -0.000102232269,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    39  DECL FDAT FP110={TOOL_NO 3,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    40  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    41  DECL E6POS XP160={X 49.7469,Y 920.334961,Z 194.458664,A 58.6510048,B 0.000999865937,C -1.87045970E-07,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    42  DECL FDAT FP160={TOOL_NO 4,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    43  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    44  DECL E6POS XP170={X -91.4441605,Y 931.337219,Z 170.413101,A 58.6510048,B 0.000999745447,C -2.17383686E-07,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    45  DECL FDAT FP170={TOOL_NO 4,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    46  DECL LDAT LCPDAT13={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    47  DECL E6POS XP180={X -91.4441605,Y 931.337219,Z 170.413101,A 58.6510048,B 0.000999745447,C -2.17383686E-07,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    48  DECL FDAT FP180={TOOL_NO 4,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    50  DECL LDAT XPNW3CPDAT={VEL 0.150000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000}
+    51  DECL FDAT FPNW3={TOOL_NO 4,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    52  DECL E6POS XPNW3={X -153.696930,Y 813.359619,Z 144.277161,A 57.0816841,B -0.384623110,C -0.00601430889,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    53  DECL NutWeldDAT NutWeldDAT4={GunNr 2,SpotNr 3,Offset 0}
+    54  DECL LDAT LCPDAT16={ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    55  DECL LDAT XPNW4CPDAT={VEL 0.150000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000}
+    56  DECL FDAT FPNW4={TOOL_NO 4,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    57  DECL E6POS XPNW4={X -198.215103,Y 787.285461,Z 148.794556,A 56.8301735,B -0.0342749394,C 0.560239315,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    58  DECL NutWeldDAT NutWeldDAT6={GunNr 2,SpotNr 4,Offset 0}
+    59  DECL LDAT LCPDAT17={ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    60  DECL NutWeldDAT NutWeldDAT8={GunNr 3,SpotNr 2,Offset 0}
+    61  DECL LDAT XPNW6CPDAT={VEL 0.150000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000}
+    62  DECL FDAT FPNW6={TOOL_NO 3,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    63  DECL LDAT LCPDAT19={ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    64  DECL E6POS XPNW6={X -338.196289,Y 904.619080,Z 152.926773,A 58.7987671,B -0.490157604,C -0.146124482,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    65  DECL LDAT LCPDAT20={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    66  DECL PDAT PPDAT13={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    67  DECL PDAT PPDAT14={VEL 100.000,ACC 100.000,APO_DIST 5.00000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    68  DECL PDAT PPDAT15={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    69  DECL NutWeld_SUGG_T LAST_NutWeld={POINT1[] "PNW2_SPOT3              ",POINT2[] "PNW0                    ",CP_PARAMS[] "CPDATNutWeld0           ",PTP_PARAMS[] "PDATNutWeld0            ",CONT[] "C_PTP                   ",CP_VEL[] "2  [...]
+    70  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P0                      ",POINT2[] "P0                      ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT0                   ",CONT[] "                        ",CP_VEL[] "2      [...]
+    71  DECL LDAT LReload_XPNW1_1_1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    72  DECL LDAT LReload_XPNW1_1_2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    73  DECL PDAT PReload_XPNW1_1_3={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    74  DECL LDAT Lpnw1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
```
_92 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2A.dat.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt2A.src`

added, integrator program: 0 code line(s) removed, 69 added; 64 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2A.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2A.src.diff)

Attributes: +&ACCESS RVO1; +&REL 246; +&COMMENT GE4_002_GUN1; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\TP\Nutweld\Template\NutWeld_Vorgabe; +&PARAM DISKPATH = KRC:\R1\Program\StyleApps\Options

```diff
@@ base line end, backup line 7 @@
+     7  DEF style1app1opt2A( )
+    26  GLOBAL INTERRUPT DECL 3 WHEN $STOPMESS==TRUE DO IR_STOPM ( )
+    27  INTERRUPT ON 3
+    28  BAS (#INITMOV,0 )
+    39  $BWDSTART=FALSE
+    40  PDAT_ACT=PPDAT0
+    41  FDAT_ACT=FP0
+    42  BAS(#PTP_PARAMS,100)
+    43  PTP XP0 C_DIS
+    46  $BWDSTART=FALSE
+    47  LDAT_ACT=LCPDAT11
+    48  FDAT_ACT=FP5
+    49  BAS(#CP_PARAMS,2)
+    50  LIN XP5
+    62  INTERRUPT DECL 20 WHEN CL_GunStrokePositionLPT<137000 DO GUN_OPEN_LOST()
+    63  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
+    64  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
+    67  LOOP
+    68  WAIT FOR NEXT_NUT_READY==TRUE
+    69  GUN_OPEN_CHECK()
+    70  INTERRUPT ON 20
+    71  INTERRUPT ON 21
+    72  INTERRUPT ON 22
+    74  $BWDSTART=FALSE
+    75  LDAT_ACT=LCPDAT0
+    76  FDAT_ACT=FP6
+    77  BAS(#CP_PARAMS,2)
+    78  LIN XP6
+    81  IF di004UseDryCycle==FALSE THEN
+    85  $BWDSTART=FALSE
+    86  LDAT_ACT=LCPDAT15
+    87  FDAT_ACT=FP16
+    88  BAS(#CP_PARAMS,2)
+    89  LIN XP16
+    91  WAIT SEC 0
+    92  INTERRUPT OFF 20
+    93  INTERRUPT OFF 21
+    94  INTERRUPT OFF 22
+    95  CENTERLINE_WELD()
+    96  INTERRUPT ON 20
+    97  INTERRUPT ON 21
+    98  INTERRUPT ON 22
+   102  ENDIF
+   104  $BWDSTART=FALSE
+   105  LDAT_ACT=LCPDAT6
+   106  FDAT_ACT=FP06
+   107  BAS(#CP_PARAMS,2)
+   108  LIN XP06 C_DIS C_DIS
+   110  WAIT SEC 0
+   111  INTERRUPT OFF 20
+   112  INTERRUPT OFF 21
+   113  INTERRUPT OFF 22
+   115  IF NOT NUT_WELD_RETRY THEN
+   116  EXIT
+   117  ENDIF
+   118  NUT_WELD_RETRY=FALSE
+   119  ENDLOOP
+   122  $BWDSTART=FALSE
+   123  LDAT_ACT=LCPDAT14
```
_10 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2A.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt2B.dat`

added, integrator program: 0 code line(s) removed, 151 added; 11 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2B.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2B.dat.diff)

Attributes: +&ACCESS RVO2; +&REL 1; +&COMMENT GE4_002_GUN1; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\TP\Nutweld\Template\NutWeld_Vorgabe; +&PARAM DISKPATH = KRC:\R1\Program\StyleApps\Options

Data changes:

- added 1 BASIS_SUGG_T: LAST_BASIS
- added 1 DEFDAT: style1app1opt2B
- added 42 E6POS: XAboveNut3, XAboveNut4, XAboveNut6, XDROP21, XDROP22, XDROP23, XDROP24, XDROP25, XDROP26, XDROP31, XDROP32, XP0 ...
- added 1 EXT: BAS
- added 42 FDAT: FAboveNut3, FAboveNut4, FAboveNut6, FDROP21, FDROP22, FDROP23, FDROP24, FDROP25, FDROP26, FDROP31, FDROP32, FP0 ...
- added 29 LDAT: LCPDAT0, LCPDAT1, LCPDAT2, LCPDAT3, LCPDAT4, LCPDAT5, LCPDAT6, LCPDAT7, LCPDAT8, LCPDAT9, LCPDAT10, LCPDAT11 ...
- added 3 NUTWELDDAT: NutWeldDAT4, NutWeldDAT6, NutWeldDAT8
- added 1 NUTWELD_SUGG_T: LAST_NutWeld
- added 30 PDAT: PPDAT0, PPDAT1, PPDAT2, PPDAT3, PPDAT4, PPDAT5, PPDAT6, PPDAT7, PPDAT8, PPDAT9, PPDAT10, PPDAT11 ...

```diff
@@ base line end, backup line 7 @@
+     7  DEFDAT style1app1opt2B
+    10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
+    17  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    18  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    19  DECL LDAT LCPDAT4={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    20  DECL E6POS XP10={X -1783.28369,Y -204.411,Z 1353.11560,A 22.6009655,B -85.8094482,C -23.7340908,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    21  DECL FDAT FP10={TOOL_NO 3,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    22  DECL E6POS XAboveNut3={X -303.780243,Y 813.191772,Z 166.218750,A 57.0816841,B -0.384623110,C -0.00601434475,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    23  DECL FDAT FAboveNut3={TOOL_NO 3,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    24  DECL E6POS XAboveNut4={X -347.034637,Y 785.924500,Z 174.869568,A 56.8305,B -0.0316173770,C 0.561762750,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    25  DECL FDAT FAboveNut4={TOOL_NO 3,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    26  DECL E6POS XP70={X -29.1782665,Y 976.513794,Z 395.040894,A 39.0784416,B -7.62199688,C -6.57393408,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    27  DECL FDAT FP70={TOOL_NO 3,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    28  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    29  DECL E6POS XP80={X 290.249634,Y 607.626892,Z -209.393982,A -8.90244770,B 0.239384755,C 178.080566,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    30  DECL FDAT FP80={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    31  DECL LDAT LCPDAT7={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    32  DECL LDAT LCPDAT8={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    33  DECL E6POS XAboveNut6={X -336.120819,Y 902.973755,Z 176.529984,A 58.7987671,B -0.490157604,C -0.146124393,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    34  DECL FDAT FAboveNut6={TOOL_NO 3,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    35  DECL E6POS XP100={X -194.562393,Y 1020.65479,Z 164.107071,A 56.8293304,B 0.00100069749,C 3.79618939E-07,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    36  DECL FDAT FP100={TOOL_NO 3,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    37  DECL LDAT LCPDAT9={VEL 2.00000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    38  DECL E6POS XP110={X -204.560745,Y 1246.33264,Z 194.087265,A 49.2418823,B 0.000983044622,C -0.000102232269,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    39  DECL FDAT FP110={TOOL_NO 3,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    40  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    41  DECL E6POS XP160={X 49.7469,Y 920.334961,Z 194.458664,A 58.6510048,B 0.000999865937,C -1.87045970E-07,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    42  DECL FDAT FP160={TOOL_NO 4,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    43  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    44  DECL E6POS XP170={X -91.4441605,Y 931.337219,Z 170.413101,A 58.6510048,B 0.000999745447,C -2.17383686E-07,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    45  DECL FDAT FP170={TOOL_NO 4,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    46  DECL LDAT LCPDAT13={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    47  DECL E6POS XP180={X -91.4441605,Y 931.337219,Z 170.413101,A 58.6510048,B 0.000999745447,C -2.17383686E-07,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    48  DECL FDAT FP180={TOOL_NO 4,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    50  DECL LDAT XPNW3CPDAT={VEL 0.150000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000}
+    51  DECL FDAT FPNW3={TOOL_NO 4,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    52  DECL E6POS XPNW3={X -153.696930,Y 813.359619,Z 144.277161,A 57.0816841,B -0.384623110,C -0.00601430889,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    53  DECL NutWeldDAT NutWeldDAT4={GunNr 2,SpotNr 3,Offset 0}
+    54  DECL LDAT LCPDAT16={ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    55  DECL LDAT XPNW4CPDAT={VEL 0.150000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000}
+    56  DECL FDAT FPNW4={TOOL_NO 4,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    57  DECL E6POS XPNW4={X -198.215103,Y 787.285461,Z 148.794556,A 56.8301735,B -0.0342749394,C 0.560239315,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    58  DECL NutWeldDAT NutWeldDAT6={GunNr 2,SpotNr 4,Offset 0}
+    59  DECL LDAT LCPDAT17={ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    60  DECL NutWeldDAT NutWeldDAT8={GunNr 3,SpotNr 2,Offset 0}
+    61  DECL LDAT XPNW6CPDAT={VEL 0.150000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000}
+    62  DECL FDAT FPNW6={TOOL_NO 3,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    63  DECL LDAT LCPDAT19={ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    64  DECL E6POS XPNW6={X -338.196289,Y 904.619080,Z 152.926773,A 58.7987671,B -0.490157604,C -0.146124482,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    65  DECL LDAT LCPDAT20={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    66  DECL PDAT PPDAT13={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    67  DECL PDAT PPDAT14={VEL 100.000,ACC 100.000,APO_DIST 5.00000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    68  DECL PDAT PPDAT15={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    69  DECL NutWeld_SUGG_T LAST_NutWeld={POINT1[] "PNW2_SPOT3              ",POINT2[] "PNW0                    ",CP_PARAMS[] "CPDATNutWeld0           ",PTP_PARAMS[] "PDATNutWeld0            ",CONT[] "C_PTP                   ",CP_VEL[] "2  [...]
+    70  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P0                      ",POINT2[] "P0                      ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT0                   ",CONT[] "                        ",CP_VEL[] "2      [...]
+    71  DECL LDAT LReload_XPNW1_1_1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    72  DECL LDAT LReload_XPNW1_1_2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    73  DECL PDAT PReload_XPNW1_1_3={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    74  DECL LDAT Lpnw1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
```
_92 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2B.dat.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt2B.src`

added, integrator program: 0 code line(s) removed, 69 added; 64 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2B.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2B.src.diff)

Attributes: +&ACCESS RVO2; +&REL 1; +&COMMENT GE4_002_GUN1; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\TP\Nutweld\Template\NutWeld_Vorgabe; +&PARAM DISKPATH = KRC:\R1\Program\StyleApps\Options

```diff
@@ base line end, backup line 7 @@
+     7  DEF style1app1opt2B( )
+    26  GLOBAL INTERRUPT DECL 3 WHEN $STOPMESS==TRUE DO IR_STOPM ( )
+    27  INTERRUPT ON 3
+    28  BAS (#INITMOV,0 )
+    39  $BWDSTART=FALSE
+    40  PDAT_ACT=PPDAT0
+    41  FDAT_ACT=FP0
+    42  BAS(#PTP_PARAMS,100)
+    43  PTP XP0 C_DIS
+    46  $BWDSTART=FALSE
+    47  LDAT_ACT=LCPDAT11
+    48  FDAT_ACT=FP5
+    49  BAS(#CP_PARAMS,2)
+    50  LIN XP5
+    62  INTERRUPT DECL 20 WHEN CL_GunStrokePositionLPT<137000 DO GUN_OPEN_LOST()
+    63  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
+    64  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
+    67  LOOP
+    68  WAIT FOR NEXT_NUT_READY==TRUE
+    69  GUN_OPEN_CHECK()
+    70  INTERRUPT ON 20
+    71  INTERRUPT ON 21
+    72  INTERRUPT ON 22
+    74  $BWDSTART=FALSE
+    75  LDAT_ACT=LCPDAT0
+    76  FDAT_ACT=FP6
+    77  BAS(#CP_PARAMS,2)
+    78  LIN XP6
+    81  IF di004UseDryCycle==FALSE THEN
+    85  $BWDSTART=FALSE
+    86  LDAT_ACT=LCPDAT15
+    87  FDAT_ACT=FP16
+    88  BAS(#CP_PARAMS,2)
+    89  LIN XP16
+    91  WAIT SEC 0
+    92  INTERRUPT OFF 20
+    93  INTERRUPT OFF 21
+    94  INTERRUPT OFF 22
+    95  CENTERLINE_WELD()
+    96  INTERRUPT ON 20
+    97  INTERRUPT ON 21
+    98  INTERRUPT ON 22
+   102  ENDIF
+   104  $BWDSTART=FALSE
+   105  LDAT_ACT=LCPDAT6
+   106  FDAT_ACT=FP06
+   107  BAS(#CP_PARAMS,2)
+   108  LIN XP06 C_DIS C_DIS
+   110  WAIT SEC 0
+   111  INTERRUPT OFF 20
+   112  INTERRUPT OFF 21
+   113  INTERRUPT OFF 22
+   115  IF NOT NUT_WELD_RETRY THEN
+   116  EXIT
+   117  ENDIF
+   118  NUT_WELD_RETRY=FALSE
+   119  ENDLOOP
+   122  $BWDSTART=FALSE
+   123  LDAT_ACT=LCPDAT14
```
_10 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2B.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt3A.dat`

added, integrator program: 0 code line(s) removed, 104 added; 9 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3A.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3A.dat.diff)

Attributes: +&ACCESS  RV; +&COMMENT GE4_003_GUN1; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\TP\Nutweld\Template\NutWeld_Vorgabe; +&PARAM DISKPATH = KRC:\R1\Program\StyleApps\Options; +&REL 227

Data changes:

- added 1 BASIS_SUGG_T: LAST_BASIS
- added 1 DEFDAT: style1app1opt3A
- added 25 E6POS: XABOVENUT1, XDROP73, XNUT1, XP1, XP2, XP3, XP4, XP5, XP6, XP7, XP8, XP9 ...
- added 1 EXT: BAS
- added 25 FDAT: FAboveNut1, FDROP73, FNut1, FP1, FP2, FP3, FP4, FP5, FP6, FP7, FP8, FP9 ...
- added 19 LDAT: LCPDAT1, LCPDAT2, LCPDAT3, LCPDAT4, LCPDAT5, LCPDAT6, LCPDAT7, LCPDAT8, LCPDAT9, LCPDAT10, LCPDAT11, LCPDAT12 ...
- added 1 MODULEPARAM_T: LAST_TP_PARAMS
- added 2 NUTWELDDAT: NutWeldDAT1, NutWeldDAT2
- added 1 NUTWELD_SUGG_T: LAST_NutWeld
- added 27 PDAT: PPDAT1, PPDAT2, PPDAT3, PPDAT4, PPDAT5, PPDAT6, PPDAT7, PPDAT8, PPDAT9, PPDAT10, PPDAT11, PPDAT12 ...

```diff
@@ base line end, backup line 7 @@
+     7  DEFDAT style1app1opt3A
+    10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
+    16  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    17  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    18  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    19  DECL E6POS XP10={X -2075.68359,Y 854.949158,Z 1307.29810,A 77.6920624,B -20.6746445,C -80.6289597,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    20  DECL FDAT FP10={TOOL_NO 7,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    21  DECL E6POS XNUT1={X -12.8878489,Y 123.584129,Z -36.2668114,A 60.1760483,B -3.21555185,C -5.74943399,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    22  DECL FDAT FNut1={TOOL_NO 7,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    23  DECL E6POS XP40={X 194.480,Y 444.441528,Z 109.191170,A 59.0454025,B -2.16523719,C -3.66616058,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    24  DECL FDAT FP40={TOOL_NO 7,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    25  DECL E6POS XP20={X -3678.25781,Y -44.2650108,Z -442.362579,A -178.367340,B 0.267035842,C 179.968063,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    26  DECL FDAT FP20={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    27  DECL E6POS XABOVENUT1={X -16.2189884,Y 123.785316,Z 31.4176292,A 59.9875450,B -3.00310516,C -5.37727165,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    28  DECL FDAT FAboveNut1={TOOL_NO 7,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    29  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    31  DECL NutWeldDAT NutWeldDAT1={GunNr 3,SpotNr 3,Offset 0}
+    32  DECL LDAT XPNW1CPDAT={VEL 0.150000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000}
+    33  DECL FDAT FPNW1={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    34  DECL PDAT PPDAT6={ACC 100.000,APO_DIST 100.000,APO_MODE #CPTP,GEAR_JERK 50.0000,EXAX_IGN 0}
+    35  DECL E6POS XPNW1={X -684.340210,Y -936.680359,Z 6.96372366,A -85.0124512,B -3.00309157,C -5.37728167,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    36  DECL LDAT LCPDAT7={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    37  DECL LDAT LCPDAT8={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    38  DECL PDAT PPDAT10={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    39  DECL E6POS XP50={X -1950.08691,Y 799.801636,Z 1115.17920,A 76.5103378,B -21.3705120,C -77.1953812,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    40  DECL FDAT FP50={TOOL_NO 7,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    41  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P18                     ",POINT2[] "P18                     ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT26                  ",CONT[] "                        ",CP_VEL[] "2      [...]
+    42  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    43  DECL NutWeld_SUGG_T LAST_NutWeld={POINT1[] "PNW3_SPOT03             ",POINT2[] "PNW0                    ",CP_PARAMS[] "CPDATNutWeld0           ",PTP_PARAMS[] "PDATNutWeld0            ",CONT[] "C_PTP                   ",CP_VEL[] "2  [...]
+    44  DECL NutWeldDAT NutWeldDAT2={GunNr 3,SpotNr 3,Offset 0}
+    45  DECL LDAT LCPDAT2={ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    46  DECL MODULEPARAM_T LAST_TP_PARAMS={PARAMS[] "NutWeld_CmdPos=Weld; NutWeld_Move=LIN; NutWeld_NutWeldDat=NutWeldDAT1; NutWeld_NWGunNr=3; NutWeld_NWSpotNr=3; NutWeld_NWOffset=0; Kuka.MoveDataName=CPDAT2; Kuka.VelocityPath=2; Kuka.Poin [...]
+    47  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    48  DECL LDAT LCPDAT3={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    49  DECL LDAT LCPDAT21={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    50  DECL LDAT LReload_XPNW1_1_1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    51  DECL LDAT LReload_XPNW1_1_2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    52  DECL PDAT PReload_XPNW1_1_3={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    53  DECL LDAT Lpnw1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    54  DECL LDAT Lpnw2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    55  DECL E6POS XDROP73={X 156.140869,Y 596.295715,Z 615.623230,A 6.04692936,B -8.02280807,C -82.7209473,S 6,T 58,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    56  DECL FDAT FDROP73={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    57  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    58  DECL E6POS XP1={X -961.490173,Y 265.809387,Z 1090.12085,A 30.7095222,B 5.15975904,C -176.833344,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    59  DECL FDAT FP1={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    60  DECL PDAT PPDAT8={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    61  DECL PDAT PPDAT9={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    62  DECL E6POS XP2={X -2340.77637,Y -67.3134537,Z -2402.96,A 178.721222,B 74.3561554,C 43.7313080,S 6,T 59,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    63  DECL FDAT FP2={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    64  DECL PDAT PPDAT11={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    65  DECL E6POS XP3={X -1824.18188,Y -1001.09119,Z -157.213959,A -87.6076279,B -4.42733240,C -177.429916,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    66  DECL FDAT FP3={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    67  DECL PDAT PPDAT12={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    68  DECL E6POS XP4={X 502.171722,Y 190.181396,Z -135.596970,A -6.24112272,B -3.20316982,C 176.013672,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    69  DECL FDAT FP4={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    70  DECL PDAT PPDAT13={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    71  DECL E6POS XP5={X 403.314392,Y 226.179260,Z -114.475060,A -6.33512926,B 0.0627186,C 178.051514,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    72  DECL FDAT FP5={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    73  DECL PDAT PPDAT14={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
```
_45 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3A.dat.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt3A.src`

added, integrator program: 0 code line(s) removed, 63 added; 61 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3A.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3A.src.diff)

Attributes: +&ACCESS RVO1; +&REL 227; +&COMMENT GE4_003_GUN1; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\TP\Nutweld\Template\NutWeld_Vorgabe; +&PARAM DISKPATH = KRC:\R1\Program\StyleApps\Options

```diff
@@ base line end, backup line 7 @@
+     7  DEF style1app1opt3A( )
+    26  GLOBAL INTERRUPT DECL 3 WHEN $STOPMESS==TRUE DO IR_STOPM ( )
+    27  INTERRUPT ON 3
+    28  BAS (#INITMOV,0 )
+    40  $BWDSTART=FALSE
+    41  LDAT_ACT=LCPDAT6
+    42  FDAT_ACT=FP20
+    43  BAS(#CP_PARAMS,2)
+    44  LIN XP20 C_DIS C_DIS
+    56  INTERRUPT DECL 20 WHEN CL_GunStrokePositionLPT<137000 DO GUN_OPEN_LOST()
+    57  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
+    58  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
+    61  LOOP
+    62  WAIT FOR NEXT_NUT_READY==TRUE
+    63  GUN_OPEN_CHECK()
+    64  INTERRUPT ON 20
+    65  INTERRUPT ON 21
+    66  INTERRUPT ON 22
+    68  $BWDSTART=FALSE
+    69  LDAT_ACT=LCPDAT4
+    70  FDAT_ACT=FP13
+    71  BAS(#CP_PARAMS,2)
+    72  LIN XP13 C_DIS C_DIS
+    75  IF di004UseDryCycle==FALSE THEN
+    79  $BWDSTART=FALSE
+    80  LDAT_ACT=LCPDAT11
+    81  FDAT_ACT=FP16
+    82  BAS(#CP_PARAMS,2)
+    83  LIN XP16
+    85  WAIT SEC 0
+    86  INTERRUPT OFF 20
+    87  INTERRUPT OFF 21
+    88  INTERRUPT OFF 22
+    89  CENTERLINE_WELD()
+    90  INTERRUPT ON 20
+    91  INTERRUPT ON 21
+    92  INTERRUPT ON 22
+    94  ENDIF
+    96  $BWDSTART=FALSE
+    97  LDAT_ACT=LCPDAT12
+    98  FDAT_ACT=FP17
+    99  BAS(#CP_PARAMS,2)
+   100  LIN XP17
+   102  WAIT SEC 0
+   103  INTERRUPT OFF 20
+   104  INTERRUPT OFF 21
+   105  INTERRUPT OFF 22
+   107  IF NOT NUT_WELD_RETRY THEN
+   108  EXIT
+   109  ENDIF
+   110  NUT_WELD_RETRY=FALSE
+   111  ENDLOOP
+   114  $BWDSTART=FALSE
+   115  LDAT_ACT=LCPDAT10
+   116  FDAT_ACT=FP20
+   117  BAS(#CP_PARAMS,2)
+   118  LIN XP20
+   121  $BWDSTART=FALSE
+   122  PDAT_ACT=PPDAT25
```
_4 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3A.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt3B.dat`

added, integrator program: 0 code line(s) removed, 104 added; 9 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3B.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3B.dat.diff)

Attributes: +&ACCESS RVO2; +&REL 1; +&COMMENT GE4_003_GUN1; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\TP\Nutweld\Template\NutWeld_Vorgabe; +&PARAM DISKPATH = KRC:\R1\Program\StyleApps\Options

Data changes:

- added 1 BASIS_SUGG_T: LAST_BASIS
- added 1 DEFDAT: style1app1opt3B
- added 25 E6POS: XABOVENUT1, XDROP73, XNUT1, XP1, XP2, XP3, XP4, XP5, XP6, XP7, XP8, XP9 ...
- added 1 EXT: BAS
- added 25 FDAT: FAboveNut1, FDROP73, FNut1, FP1, FP2, FP3, FP4, FP5, FP6, FP7, FP8, FP9 ...
- added 19 LDAT: LCPDAT1, LCPDAT2, LCPDAT3, LCPDAT4, LCPDAT5, LCPDAT6, LCPDAT7, LCPDAT8, LCPDAT9, LCPDAT10, LCPDAT11, LCPDAT12 ...
- added 1 MODULEPARAM_T: LAST_TP_PARAMS
- added 2 NUTWELDDAT: NutWeldDAT1, NutWeldDAT2
- added 1 NUTWELD_SUGG_T: LAST_NutWeld
- added 27 PDAT: PPDAT1, PPDAT2, PPDAT3, PPDAT4, PPDAT5, PPDAT6, PPDAT7, PPDAT8, PPDAT9, PPDAT10, PPDAT11, PPDAT12 ...

```diff
@@ base line end, backup line 7 @@
+     7  DEFDAT style1app1opt3B
+    10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
+    16  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    17  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    18  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    19  DECL E6POS XP10={X -2075.68359,Y 854.949158,Z 1307.29810,A 77.6920624,B -20.6746445,C -80.6289597,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    20  DECL FDAT FP10={TOOL_NO 7,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    21  DECL E6POS XNUT1={X -12.8878489,Y 123.584129,Z -36.2668114,A 60.1760483,B -3.21555185,C -5.74943399,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    22  DECL FDAT FNut1={TOOL_NO 7,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    23  DECL E6POS XP40={X 194.480,Y 444.441528,Z 109.191170,A 59.0454025,B -2.16523719,C -3.66616058,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    24  DECL FDAT FP40={TOOL_NO 7,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    25  DECL E6POS XP20={X -3678.25781,Y -44.2650108,Z -442.362579,A -178.367340,B 0.267035842,C 179.968063,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    26  DECL FDAT FP20={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    27  DECL E6POS XABOVENUT1={X -16.2189884,Y 123.785316,Z 31.4176292,A 59.9875450,B -3.00310516,C -5.37727165,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    28  DECL FDAT FAboveNut1={TOOL_NO 7,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    29  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    31  DECL NutWeldDAT NutWeldDAT1={GunNr 3,SpotNr 3,Offset 0}
+    32  DECL LDAT XPNW1CPDAT={VEL 0.150000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000}
+    33  DECL FDAT FPNW1={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    34  DECL PDAT PPDAT6={ACC 100.000,APO_DIST 100.000,APO_MODE #CPTP,GEAR_JERK 50.0000,EXAX_IGN 0}
+    35  DECL E6POS XPNW1={X -684.340210,Y -936.680359,Z 6.96372366,A -85.0124512,B -3.00309157,C -5.37728167,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    36  DECL LDAT LCPDAT7={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    37  DECL LDAT LCPDAT8={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    38  DECL PDAT PPDAT10={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    39  DECL E6POS XP50={X -1950.08691,Y 799.801636,Z 1115.17920,A 76.5103378,B -21.3705120,C -77.1953812,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    40  DECL FDAT FP50={TOOL_NO 7,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    41  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P18                     ",POINT2[] "P18                     ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT26                  ",CONT[] "                        ",CP_VEL[] "2      [...]
+    42  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    43  DECL NutWeld_SUGG_T LAST_NutWeld={POINT1[] "PNW3_SPOT03             ",POINT2[] "PNW0                    ",CP_PARAMS[] "CPDATNutWeld0           ",PTP_PARAMS[] "PDATNutWeld0            ",CONT[] "C_PTP                   ",CP_VEL[] "2  [...]
+    44  DECL NutWeldDAT NutWeldDAT2={GunNr 3,SpotNr 3,Offset 0}
+    45  DECL LDAT LCPDAT2={ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    46  DECL MODULEPARAM_T LAST_TP_PARAMS={PARAMS[] "NutWeld_CmdPos=Weld; NutWeld_Move=LIN; NutWeld_NutWeldDat=NutWeldDAT1; NutWeld_NWGunNr=3; NutWeld_NWSpotNr=3; NutWeld_NWOffset=0; Kuka.MoveDataName=CPDAT2; Kuka.VelocityPath=2; Kuka.Poin [...]
+    47  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    48  DECL LDAT LCPDAT3={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    49  DECL LDAT LCPDAT21={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    50  DECL LDAT LReload_XPNW1_1_1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    51  DECL LDAT LReload_XPNW1_1_2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    52  DECL PDAT PReload_XPNW1_1_3={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    53  DECL LDAT Lpnw1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    54  DECL LDAT Lpnw2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    55  DECL E6POS XDROP73={X 156.140869,Y 596.295715,Z 615.623230,A 6.04692936,B -8.02280807,C -82.7209473,S 6,T 58,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    56  DECL FDAT FDROP73={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    57  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    58  DECL E6POS XP1={X -961.490173,Y 265.809387,Z 1090.12085,A 30.7095222,B 5.15975904,C -176.833344,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    59  DECL FDAT FP1={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    60  DECL PDAT PPDAT8={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    61  DECL PDAT PPDAT9={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    62  DECL E6POS XP2={X -2340.77637,Y -67.3134537,Z -2402.96,A 178.721222,B 74.3561554,C 43.7313080,S 6,T 59,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    63  DECL FDAT FP2={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    64  DECL PDAT PPDAT11={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    65  DECL E6POS XP3={X -1824.18188,Y -1001.09119,Z -157.213959,A -87.6076279,B -4.42733240,C -177.429916,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    66  DECL FDAT FP3={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    67  DECL PDAT PPDAT12={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    68  DECL E6POS XP4={X 502.171722,Y 190.181396,Z -135.596970,A -6.24112272,B -3.20316982,C 176.013672,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    69  DECL FDAT FP4={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    70  DECL PDAT PPDAT13={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    71  DECL E6POS XP5={X 403.314392,Y 226.179260,Z -114.475060,A -6.33512926,B 0.0627186,C 178.051514,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    72  DECL FDAT FP5={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    73  DECL PDAT PPDAT14={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
```
_45 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3B.dat.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt3B.src`

added, integrator program: 0 code line(s) removed, 63 added; 61 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3B.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3B.src.diff)

Attributes: +&ACCESS RVO2; +&REL 1; +&COMMENT GE4_003_GUN1; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\TP\Nutweld\Template\NutWeld_Vorgabe; +&PARAM DISKPATH = KRC:\R1\Program\StyleApps\Options

```diff
@@ base line end, backup line 7 @@
+     7  DEF style1app1opt3B( )
+    26  GLOBAL INTERRUPT DECL 3 WHEN $STOPMESS==TRUE DO IR_STOPM ( )
+    27  INTERRUPT ON 3
+    28  BAS (#INITMOV,0 )
+    40  $BWDSTART=FALSE
+    41  LDAT_ACT=LCPDAT6
+    42  FDAT_ACT=FP20
+    43  BAS(#CP_PARAMS,2)
+    44  LIN XP20 C_DIS C_DIS
+    56  INTERRUPT DECL 20 WHEN CL_GunStrokePositionLPT<137000 DO GUN_OPEN_LOST()
+    57  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
+    58  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
+    61  LOOP
+    62  WAIT FOR NEXT_NUT_READY==TRUE
+    63  GUN_OPEN_CHECK()
+    64  INTERRUPT ON 20
+    65  INTERRUPT ON 21
+    66  INTERRUPT ON 22
+    68  $BWDSTART=FALSE
+    69  LDAT_ACT=LCPDAT4
+    70  FDAT_ACT=FP13
+    71  BAS(#CP_PARAMS,2)
+    72  LIN XP13 C_DIS C_DIS
+    75  IF di004UseDryCycle==FALSE THEN
+    79  $BWDSTART=FALSE
+    80  LDAT_ACT=LCPDAT11
+    81  FDAT_ACT=FP16
+    82  BAS(#CP_PARAMS,2)
+    83  LIN XP16
+    85  WAIT SEC 0
+    86  INTERRUPT OFF 20
+    87  INTERRUPT OFF 21
+    88  INTERRUPT OFF 22
+    89  CENTERLINE_WELD()
+    90  INTERRUPT ON 20
+    91  INTERRUPT ON 21
+    92  INTERRUPT ON 22
+    94  ENDIF
+    96  $BWDSTART=FALSE
+    97  LDAT_ACT=LCPDAT12
+    98  FDAT_ACT=FP17
+    99  BAS(#CP_PARAMS,2)
+   100  LIN XP17
+   102  WAIT SEC 0
+   103  INTERRUPT OFF 20
+   104  INTERRUPT OFF 21
+   105  INTERRUPT OFF 22
+   107  IF NOT NUT_WELD_RETRY THEN
+   108  EXIT
+   109  ENDIF
+   110  NUT_WELD_RETRY=FALSE
+   111  ENDLOOP
+   114  $BWDSTART=FALSE
+   115  LDAT_ACT=LCPDAT10
+   116  FDAT_ACT=FP20
+   117  BAS(#CP_PARAMS,2)
+   118  LIN XP20
+   121  $BWDSTART=FALSE
+   122  PDAT_ACT=PPDAT25
```
_4 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3B.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app2opt1.dat`

changed, integrator program: 0 code line(s) removed, 143 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.dat.diff)

Attributes: &ACCESS RVO1 -> &ACCESS RVO2; &REL 19 -> &REL 21

Data changes:

- added 43 E6POS: XP1, XP2, XP3, XP4, XP5, XP6, XP7, XP8, XP9, XP10, XP11, XP12 ...
- added 43 FDAT: FP1, FP2, FP3, FP4, FP5, FP6, FP7, FP8, FP9, FP10, FP11, FP12 ...
- added 23 LDAT: LCPDAT1, LCPDAT2, LCPDAT3, LCPDAT4, LCPDAT5, LCPDAT6, LCPDAT7, LCPDAT8, LCPDAT9, LCPDAT10, LCPDAT11, LCPDAT12 ...
- added 1 NUTWELDDAT: NutWeldDAT1
- added 33 PDAT: PPDAT1, PPDAT2, PPDAT3, PPDAT4, PPDAT5, PPDAT6, PPDAT7, PPDAT8, PPDAT9, PPDAT10, PPDAT11, PPDAT12 ...

```diff
@@ base line 13, backup line 13 @@
     13  BOOL NutWeld_TEMPLATE=TRUE
     20  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P0                      ",POINT2[] "P0                      ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT0                   ",CONT[] "                        ",CP_VEL[] "2.0    [...]
+    21  DECL E6POS XP1={X 504.083038,Y -786.363281,Z 1705.62244,A -111.705475,B 40.2604523,C 19.4570885,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    22  DECL FDAT FP1={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    23  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    24  DECL E6POS XP2={X -3354.51514,Y -143.403854,Z -774.646057,A -178.361191,B -0.268041790,C 179.960083,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    25  DECL FDAT FP2={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    26  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    27  DECL E6POS XP3={X -68.0168152,Y -1722.30078,Z 1086.26270,A -91.6317673,B 0.275582,C -0.0421518087,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    28  DECL FDAT FP3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    29  DECL LDAT LCPDAT2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    30  DECL E6POS XP4={X -82.9339371,Y -1983.86072,Z 1026.44580,A -91.6317673,B 0.275582284,C -0.0421519652,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    31  DECL FDAT FP4={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    32  DECL LDAT LCPDAT3={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    33  DECL E6POS XP5={X -3596.24170,Y -96.9433,Z -420.628052,A -178.367157,B -0.266017616,C 179.960464,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    34  DECL FDAT FP5={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    35  DECL LDAT LCPDAT4={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    36  DECL E6POS XP6={X -3850.17822,Y -104.182068,Z -419.448608,A -178.367157,B -0.266017616,C 179.960464,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    37  DECL FDAT FP6={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    38  DECL LDAT LCPDAT5={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     39  DECL NutWeld_SUGG_T LAST_NutWeld={POINT1[] "PNW1                    ",POINT2[] "PNW0                    ",CP_PARAMS[] "CPDATNutWeld0           ",PTP_PARAMS[] "PDATNutWeld0            ",CONT[] "C_PTP                   ",CP_VEL[] "2  [...]
+    40  DECL NutWeldDAT NutWeldDAT1={GunNr 1,SpotNr 1,Offset 25}
+    41  DECL LDAT XPNW1CPDAT={VEL 0.150000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000}
+    42  DECL FDAT FPNW1={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    43  DECL PDAT PPDAT2={ACC 100.000,APO_DIST 100.000,APO_MODE #CPTP,GEAR_JERK 50.0000}
+    44  DECL E6POS XPNW1={X -3849.50415,Y -104.198906,Z -367.222534,A -178.367157,B -0.266017586,C 179.960464,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     45  DECL MODULEPARAM_T LAST_TP_PARAMS={PARAMS[] "NutWeld_CmdPos=Weld; NutWeld_Move=PTP; NutWeld_NutWeldDat=NutWeldDAT1; NutWeld_NWGunNr=1; NutWeld_NWSpotNr=1; NutWeld_NWOffset=25; Kuka.MoveDataPtpName=PDAT2; Kuka.VelocityPtp=100; Kuka. [...]
+    46  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    47  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    48  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    49  DECL E6POS XP7={X -3850.17822,Y -104.182068,Z -419.448608,A -178.367157,B -0.266017616,C 179.960464,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    50  DECL FDAT FP7={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    51  DECL LDAT LCPDAT6={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    52  DECL E6POS XP8={X -3596.24170,Y -96.9433670,Z -420.628,A -178.367157,B -0.266018540,C 179.960464,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    53  DECL FDAT FP8={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    54  DECL PDAT PPDAT6={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    55  DECL E6POS XP9={X -3850.17822,Y -104.182068,Z -419.448608,A -178.367172,B -0.266017824,C 179.960464,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    56  DECL FDAT FP9={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    57  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    58  DECL PDAT PPDAT8={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    59  DECL E6POS XP10={X -3881.98315,Y -151.523331,Z -362.167358,A -178.367172,B -0.266017944,C 179.960464,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    60  DECL FDAT FP10={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    61  DECL E6POS XP11={X -3881.98315,Y -151.523331,Z -391.565582,A -178.367172,B -0.266018,C 179.960464,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    62  DECL FDAT FP11={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    63  DECL LDAT LCPDAT7={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    64  DECL E6POS XP12={X -3881.98218,Y -151.525742,Z -362.166504,A -178.366943,B -0.266011864,C 179.960327,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    65  DECL FDAT FP12={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    66  DECL LDAT LCPDAT8={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    67  DECL E6POS XPNW2={X -3849.50415,Y -104.198906,Z -367.222534,A -178.367157,B -0.266017586,C 179.960464,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    68  DECL FDAT FPNW2={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    69  DECL PDAT PPDAT9={ACC 100.000,APO_DIST 100.000,APO_MODE #CPTP,GEAR_JERK 50.0000}
+    70  DECL E6POS XP13={X -3881.98315,Y -151.523331,Z -391.565582,A -178.367172,B -0.266017824,C 179.960464,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    71  DECL FDAT FP13={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    72  DECL LDAT LCPDAT9={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    73  DECL E6POS XP14={X -3850.17822,Y -104.182068,Z -419.448608,A -178.367172,B -0.266017824,C 179.960464,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    74  DECL FDAT FP14={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    75  DECL PDAT PPDAT10={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    76  DECL PDAT PPDAT11={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    77  DECL E6POS XP15={X -3596.24170,Y -96.9433670,Z -420.628,A -178.367157,B -0.266018540,C 179.960464,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
```
_108 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.dat.diff_

### `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`

changed, integrator program: 8 code line(s) removed, 14 added; 103 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.src.diff)

Attributes: -&ACCESS RVO1; -&REL 19; -&COMMENT 03-10-R1 NUT CHECK SENSOR; +&ACCESS RVO2; +&REL 21

```diff
@@ base line 11, backup line 26 @@
     26  INTERRUPT ON 3
     27  BAS (#INITMOV,0 )
-    40  AC_ApplicationCheck (1)
     39  $BWDSTART=FALSE
     40  PDAT_ACT=PPDAT16
@@ base line 48, backup line 42 @@
     42  BAS(#PTP_PARAMS,100)
     43  PTP XP22
+    50  AC_ApplicationCheck (1)
     54  $BWDSTART=FALSE
     55  LDAT_ACT=LCPDAT15
@@ base line 57, backup line 57 @@
     57  BAS(#CP_PARAMS,2)
     58  LIN XP28
-    64  IF NOT di004UseDryCycle THEN
+    62  IF di004UseDryCycle==FALSE THEN
+    64  IF ($IN[227]==TRUE) THEN
+    65  PARTPRESENT1=TRUE
+    66  ENDIF
     67  WAIT SEC 0.2
-    67  PARTPRESENT1=di227NutPresent1
     69  ENDIF
     73  $BWDSTART=FALSE
@@ base line 83, backup line 85 @@
     85  BAS(#CP_PARAMS,2)
     86  LIN XP32
-    90  IF NOT di004UseDryCycle THEN
+    90  IF di004UseDryCycle==FALSE THEN
+    92  IF ($IN[227]==TRUE) THEN
+    93  PARTPRESENT2=TRUE
+    94  ENDIF
     95  WAIT SEC 0.2
-    93  PARTPRESENT2=di227NutPresent1
     97  ENDIF
    101  $BWDSTART=FALSE
@@ base line 109, backup line 113 @@
    113  BAS(#CP_PARAMS,2)
    114  LIN XP36
-   116  IF NOT di004UseDryCycle THEN
+   118  IF di004UseDryCycle==FALSE THEN
+   120  IF ($IN[227]==TRUE) THEN
+   121  PARTPRESENT3=TRUE
+   122  ENDIF
    123  WAIT SEC 0.2
-   119  PARTPRESENT3=di227NutPresent1
    125  ENDIF
    129  $BWDSTART=FALSE
@@ base line 126, backup line 132 @@
    132  BAS(#PTP_PARAMS,100)
    133  PTP XP37
-   137  IF NOT di004UseDryCycle THEN
+   136  IF di004UseDryCycle==FALSE THEN
    139  WAIT SEC 0.2
    140  SWITCH nOption
```

### `KRC/R1/Program/StyleApps/Options/style1app2opt2.dat`

changed, integrator program: 2 code line(s) removed, 53 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.dat.diff)

Attributes: &ACCESS RVO1 -> &ACCESS RVP2; &REL 16 -> &REL 17

Data changes:

- XP3 (E6POS) re-taught: moved 84.6 mm, rotated up to 16.2 deg
- added 1 DEFDAT: style1app2opt2
- added 16 E6POS: XAtNutCheck1, XATNUTCHECK4, XP1, XP2, XP4, XP5, XP7, XP10, XP20, XP30, XP40, XP50 ...
- added 16 FDAT: FAtNutCheck1, FAtNutCheck4, FP1, FP2, FP4, FP5, FP7, FP10, FP20, FP30, FP40, FP50 ...
- added 1 INT: nCount
- added 4 LDAT: LCPDAT1, LCPDAT2, LCPDAT3, LCPDAT4
- added 14 PDAT: PL, PPDAT1, PPDAT2, PPDAT3, PPDAT4, PPDAT5, PPDAT6, PPDAT7, PPDAT8, PPDAT9, PPDAT11, PPDAT27 ...
- removed 1 DEFDAT: Style1App2Opt2

```diff
@@ base line 6, backup line 6 @@
-     6  DEFDAT Style1App2Opt2
+     6  DEFDAT style1app2opt2
      9  EXT BAS (BAS_COMMAND :IN,REAL :IN )
+    15  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    16  DECL LDAT LCPDAT2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    17  DECL LDAT LCPDAT3={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    18  DECL E6POS XP10={X 2281.82666,Y 91.3649292,Z 1193.99182,A 7.45437717,B 25.0854454,C -152.934311,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    19  DECL FDAT FP10={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    20  DECL E6POS XP20={X -754.658569,Y 975.418701,Z 816.985291,A -77.7530136,B 74.7448044,C 166.116241,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    21  DECL FDAT FP20={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    22  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    23  DECL E6POS XP30={X -901.723145,Y 967.531250,Z 193.220627,A -69.3627243,B 43.5717201,C -178.930527,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    24  DECL FDAT FP30={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    25  DECL E6POS XP40={X -805.908447,Y -1889.91296,Z 1609.52112,A -104.761292,B 0.614048064,C 179.948,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    26  DECL FDAT FP40={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    27  DECL E6POS XATNUTCHECK4={X -822.738831,Y 721.997314,Z 139.945435,A -67.9592667,B 13.8679914,C -179.228760,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    28  DECL FDAT FAtNutCheck4={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    29  DECL E6POS XP50={X -853.289612,Y 785.232605,Z 116.436310,A -67.8503265,B 26.4141159,C -179.377487,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    30  DECL FDAT FP50={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    31  DECL E6POS XP60={X -709.683105,Y -1914.79602,Z 1506.28113,A -104.768265,B 0.613393545,C 179.947739,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    32  DECL FDAT Fp60={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    33  DECL E6POS XP70={X -754.658569,Y 975.418701,Z 816.985291,A -77.7530136,B 74.7448044,C 166.116241,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    34  DECL FDAT FP70={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    35  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    36  DECL E6POS XP80={X -21.1073933,Y 977.088257,Z 1822.06055,A -57.9586,B 86.2354584,C -137.216766,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    37  DECL FDAT FP80={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    38  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    39  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    40  DECL PDAT PPDAT8={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    41  DECL E6POS XP92={X 2434.83228,Y 96.6232,Z 1122.02954,A -15.1512289,B -2.07428622,C -159.203690,S 6,T 58,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    42  DECL FDAT FP92={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    43  DECL PDAT PPDAT9={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     44  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P0                      ",POINT2[] "P0                      ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT0                   ",CONT[] "                        ",CP_VEL[] "2.0    [...]
+    45  DECL E6POS XP1={X -756.930054,Y -1663.77429,Z 1079.05762,A -104.756149,B 0.614769,C 179.948242,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    46  DECL FDAT FP1={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    47  DECL PDAT PL={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    48  DECL E6POS XAtNutCheck1={X -806.267639,Y -1892.02271,Z 1807.86584,A -104.760185,B 0.614405334,C 179.948120,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    49  DECL FDAT FAtNutCheck1={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    50  DECL INT nCount
+    52  DECL PDAT PPDAT27={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    53  DECL E6POS XP2={X -725.920410,Y -1758.69482,Z 1448.59143,A -104.766548,B 0.615574777,C 179.948090,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    54  DECL FDAT FP2={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     55  DECL LDAT LCPDAT0={VEL 2.00000,ACC 80.0000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    18  DECL E6POS XP3={X -709.692566,Y -2053.68652,Z 1506.28467,A -104.821503,B 4.90587568,C 179.018478,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    56  DECL E6POS XP3={X -709.833740,Y -2035.40430,Z 1423.71777,A -98.4577484,B -5.84655905,C -164.806564,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     57  DECL FDAT FP3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    58  DECL PDAT PPDAT28={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    59  DECL E6POS XP4={X -725.920410,Y -1758.69482,Z 1448.59143,A -104.766548,B 0.615574777,C 179.948090,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    60  DECL FDAT FP4={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    61  DECL E6POS XP5={X -724.403137,Y -1811.34314,Z 1367.20557,A -104.758530,B 0.614156485,C 179.947769,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    62  DECL FDAT FP5={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    63  DECL PDAT PPDAT29={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     64  DECL E6POS XP6={X -3780.88599,Y -731.523132,Z -847.811157,A -165.231735,B -0.613393545,C -0.0522668548,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     65  DECL FDAT FP6={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    66  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    67  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    68  DECL LDAT LCPDAT4={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    69  DECL E6POS XP7={X -728.679932,Y -2041.37085,Z 1460.12866,A -87.6372147,B 17.6803131,C 179.975311,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    70  DECL FDAT FP7={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
```
_4 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.dat.diff_

### `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`

changed, integrator program: 3 code line(s) removed, 3 added; 57 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.src.diff)

Attributes: &ACCESS RVO1 -> &ACCESS RVP2; &REL 16 -> &REL 17; &COMMENT 03-10-R1 NUT CHECK CAMERA -> &COMMENT GE4_NutCHK

```diff
@@ base line 61, backup line 55 @@
     55  SWITCH nOption
     56  CASE 1,2,7,8
-    64  IF (di100CameraJudgmentOK==TRUE) AND (di101CameraJudgmentNG==FALSE) THEN
+    57  IF (di100CameraJudmentOK==TRUE) AND (di101CameraJudmentNG==FALSE) THEN
     58  bscrapGE4 = FALSE
     59  ELSE
@@ base line 68, backup line 61 @@
     61  ENDIF
     62  CASE 12
-    72  IF (di100CameraJudgmentOK==TRUE) AND (di101CameraJudgmentNG==FALSE) THEN
+    63  IF (di100CameraJudmentOK==TRUE) AND (di101CameraJudmentNG==FALSE) THEN
     64  do141RedRabbitFailed=TRUE
     65  ENDIF
-    77  IF (di100CameraJudgmentOK==FALSE) AND (di101CameraJudgmentNG==TRUE) THEN
+    66  IF (di100CameraJudmentOK==FALSE) AND (di101CameraJudmentNG==TRUE) THEN
     67  do142RedRabbitPassed=TRUE
     68  ENDIF
```

### `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.dat`

changed, integrator program: 0 code line(s) removed, 16 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt1.dat.diff](diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt1.dat.diff)

Attributes: &ACCESS RVO1 -> &ACCESS RVO2; &REL 222 -> &REL 226

Data changes:

- added 5 E6POS: XP4, XP6, XP8, XP9, XP10
- added 5 FDAT: FP4, FP6, FP8, FP9, FP10
- added 6 PDAT: PPDAT3, PPDAT4, PPDAT5, PPDAT6, PPDAT9, PPDAT12

```diff
@@ base line 17, backup line 17 @@
     17  DECL E6POS XATDROP3={X -1563.67676,Y -913.306702,Z 449.989929,A 179.143311,B 30.0803795,C -34.7621422,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     18  DECL FDAT FAtDrop3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    19  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
     20  DECL MODULEPARAM_T LAST_TP_PARAMS={PARAMS[] "AC_CmdZones=DropOff; AC_CmdParam=2; AC_ZoneRepo=True; AC_UseState=True; AC_Blending=False                               "}
     21  DECL E6POS XP2={X -1471.65808,Y -890.400757,Z 672.790649,A 177.082932,B 4.31955290,C -0.298484206,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     22  DECL FDAT FP2={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     23  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    24  DECL PDAT PPDAT9={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    25  DECL E6POS XP4={X -703.480469,Y -1395.30945,Z 616.365723,A -134.980774,B 21.6840553,C -1.41442871,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    26  DECL FDAT FP4={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     27  DECL E6POS XP5={X -1279.37976,Y -897.098,Z 616.329468,A 176.629059,B 21.7134552,C -1.31570351,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     28  DECL FDAT FP5={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     29  DECL PDAT PPDAT10={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     30  DECL PDAT PPDAT11={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    31  DECL E6POS XP6={X -1035.24158,Y -1191.13391,Z 1034.36511,A 179.322769,B 1.56446958,C 5.43827724,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    32  DECL FDAT FP6={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    33  DECL PDAT PPDAT12={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     34  DECL PDAT PPDAT13={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     35  DECL E6POS XP7={X -988.705139,Y -820.766479,Z 2569.14844,A 137.545090,B -48.9822197,C 56.5858917,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
@@ base line 35, backup line 42 @@
     42  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     43  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    44  DECL E6POS XP8={X -709.683167,Y -1914.79602,Z 1611.27075,A -104.768265,B 0.613394141,C 179.947723,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    45  DECL FDAT FP8={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    46  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    47  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    48  DECL E6POS XP9={X -709.683105,Y -1914.79602,Z 1506.28113,A -104.768265,B 0.613393545,C 179.947739,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    49  DECL FDAT FP9={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    50  DECL PDAT PPDAT6={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    51  DECL E6POS XP10={X -709.683105,Y -1914.79602,Z 1506.28113,A -104.768265,B 0.613393545,C 179.947739,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    52  DECL FDAT FP10={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     53  ENDDAT
```

### `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src`

changed, integrator program: 6 code line(s) removed, 2 added; 46 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src.diff](diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src.diff)

Attributes: &ACCESS RVO1 -> &ACCESS RVO2; &REL 222 -> &REL 226; &COMMENT 03-10-R1 DROP CONVEYOR -> &COMMENT GE4_Conveyor

```diff
@@ base line 10, backup line 10 @@
     10  INTERRUPT ON 3
     11  BAS (#INITMOV,0 )
-    35  AC_DropOffCheck (1)
     20  $BWDSTART=FALSE
     21  PDAT_ACT=PPDAT10
@@ base line 43, backup line 23 @@
     23  BAS(#PTP_PARAMS,100)
     24  PTP XP5 C_DIS
-    47  $BWDSTART=FALSE
-    48  PDAT_ACT=PPDAT1
-    49  FDAT_ACT=FP1
-    50  BAS(#PTP_PARAMS,100)
-    51  PTP XP1
+    30  AC_DropOffCheck (1)
     33  $BWDSTART=FALSE
     34  LDAT_ACT=LCPDAT1
@@ base line 58, backup line 37 @@
     37  LIN XAtDrop3
     44  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
+    50  GRPg_Check(1, 1, FALSE, 1)
     53  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254] )
     56  $OUT[18]=FALSE
```

### `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.dat`

changed, integrator program: 0 code line(s) removed, 80 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.dat.diff](diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.dat.diff)

Data changes:

- added 26 E6POS: XATDROP3, XP1, XP2, XP3, XP4, XP5, XP6, XP7, XP8, XP9, XP10, XP11 ...
- added 26 FDAT: FAtDrop3, FP1, FP2, FP3, FP4, FP5, FP6, FP7, FP8, FP9, FP10, FP11 ...
- added 3 LDAT: LCPDAT0, LCPDAT1, LCPDAT3
- added 25 PDAT: PPDAT1, PPDAT2, PPDAT3, PPDAT4, PPDAT5, PPDAT6, PPDAT7, PPDAT8, PPDAT9, PPDAT10, PPDAT12, PPDAT13 ...

```diff
@@ base line 9, backup line 9 @@
      9  DECL INT SUCCESS
     16  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P37                     ",POINT2[] "P37                     ",CP_PARAMS[] "CPDAT6                  ",PTP_PARAMS[] "PDAT34                  ",CONT[] "                        ",CP_VEL[] "2      [...]
+    17  DECL E6POS XATDROP3={X -1471.65808,Y -890.400757,Z 408.943,A 177.082932,B 4.31955290,C -0.298484236,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    18  DECL FDAT FAtDrop3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    19  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
     20  DECL MODULEPARAM_T LAST_TP_PARAMS={PARAMS[] "AC_CmdZones=DropOff; AC_CmdParam=2; AC_ZoneRepo=True; AC_UseState=True; AC_Blending=False                               "}
+    21  DECL E6POS XP2={X -1471.65808,Y -890.400757,Z 672.790649,A 177.082932,B 4.31955290,C -0.298484206,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    22  DECL FDAT FP2={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    23  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    24  DECL PDAT PPDAT9={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    25  DECL E6POS XP4={X -703.480469,Y -1395.30945,Z 616.365723,A -134.980774,B 21.6840553,C -1.41442871,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    26  DECL FDAT FP4={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    27  DECL E6POS XP5={X -1279.37976,Y -897.098,Z 616.329468,A 176.629059,B 21.7134552,C -1.31570351,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    28  DECL FDAT FP5={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    29  DECL PDAT PPDAT10={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     30  DECL PDAT PPDAT11={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    31  DECL E6POS XP6={X -1035.24158,Y -1191.13391,Z 1034.36511,A 179.322769,B 1.56446958,C 5.43827724,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    32  DECL FDAT FP6={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    33  DECL PDAT PPDAT12={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    34  DECL PDAT PPDAT13={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    35  DECL E6POS XP7={X -611.371521,Y -693.136719,Z 1916.56042,A 157.985474,B -61.9188309,C 9.87796,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    36  DECL FDAT FP7={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    37  DECL E6POS XP1={X -1440.21106,Y -892.543274,Z 457.022766,A 177.090073,B 1.60787833,C -0.160304546,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    38  DECL FDAT FP1={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    39  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    40  DECL E6POS XP3={X 370.852905,Y -298.257416,Z 2804.38916,A -147.361786,B -35.6047363,C 79.4075775,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    41  DECL FDAT FP3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    42  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    43  DECL LDAT LCPDAT0={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    44  DECL E6POS XP8={X 1206.28552,Y -208.912048,Z 319.300903,A -91.4409,B -0.232809097,C 0.168290034,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    45  DECL FDAT FP8={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    46  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    47  DECL E6POS XP9={X 1206.28552,Y -208.912048,Z 409.521729,A -91.4413757,B -0.232714087,C 0.168696448,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    48  DECL FDAT FP9={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    49  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    50  DECL E6POS XP10={X 1206.28552,Y -208.912048,Z 573.307922,A -91.4409,B -0.232809082,C 0.168290049,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    51  DECL FDAT FP10={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    52  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    53  DECL E6POS XP11={X 1206.28552,Y -208.912048,Z 1092.82214,A -91.4409,B -0.232809037,C 0.168290079,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    54  DECL FDAT FP11={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    55  DECL PDAT PPDAT6={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    56  DECL E6POS XP12={X 671.407898,Y -378.268097,Z 2030.44653,A -89.8029327,B 7.84505653,C 24.4156590,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    57  DECL FDAT FP12={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    58  DECL PDAT PPDAT8={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    59  DECL E6POS XP13={X 12.7359648,Y -130.494156,Z 3309.79932,A -58.5948639,B -68.7112122,C 63.6888771,S 3,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    60  DECL FDAT FP13={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    61  DECL E6POS XP14={X 12.7359648,Y -130.494156,Z 3309.79932,A -58.5948639,B -68.7112122,C 63.6888771,S 3,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    62  DECL FDAT FP14={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    63  DECL PDAT PPDAT14={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    64  DECL E6POS XP15={X 671.407898,Y -378.268097,Z 2030.44653,A -89.8029327,B 7.84505653,C 24.4156590,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    65  DECL FDAT FP15={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    66  DECL PDAT PPDAT15={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    67  DECL E6POS XP16={X 1206.28552,Y -208.912048,Z 1092.82214,A -91.4409,B -0.232809037,C 0.168290079,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    68  DECL FDAT FP16={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    69  DECL PDAT PPDAT16={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    70  DECL E6POS XP17={X 1206.28552,Y -208.912048,Z 573.307922,A -91.4409,B -0.232809082,C 0.168290049,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    71  DECL FDAT FP17={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    72  DECL PDAT PPDAT17={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    73  DECL E6POS XP18={X 1206.28552,Y -208.912048,Z 573.307922,A -91.4409,B -0.232809082,C 0.168290049,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
```
_42 more lines: see diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.dat.diff_

### `KRC/R1/Program/StylePicks/Options/style1pick1opt1.dat`

changed, integrator program: 0 code line(s) removed, 47 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1.dat.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1.dat.diff)

Data changes:

- added 17 E6POS: XP0, XP1, XP2, XP3, XP4, XP5, XP6, XP7, XP11, XP30, XP50, XP60 ...
- added 17 FDAT: FP0, FP1, FP2, FP3, FP4, FP5, FP6, FP7, FP11, FP30, FP50, FP60 ...
- added 2 LDAT: LCPDAT3, LCPDAT4
- added 11 PDAT: PPDAT0, PPDAT1, PPDAT3, PPDAT5, PPDAT6, PPDAT7, PPDAT8, PPDAT9, PPDAT10, PPDAT11, PPDAT14

```diff
@@ base line 9, backup line 9 @@
      9  EXT BAS (BAS_COMMAND :IN,REAL :IN )
     10  DECL INT SUCCESS
+    17  DECL E6POS XTag4={X -612.686,Y -1589.39600,Z 2916.51807,A 84.5120,B -104.062,C 7.85700,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    18  DECL FDAT FTag4={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE}
+    19  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    20  DECL E6POS XTag3={X -570.159,Y -2455.64600,Z 462.298,A 90.7960,B -176.000,C -0.0550000,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    21  DECL FDAT FTag3={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE}
     22  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    23  DECL E6POS XTag1={X -570.159,Y -2469.59692,Z 262.786,A 90.7960,B -176.000,C -0.0560000,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    24  DECL FDAT FTag1={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE}
     25  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 0.0,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    26  DECL E6POS XTag2={X -570.159,Y -2466.10889,Z 312.664,A 90.7960,B -176.000,C -0.0560000,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    27  DECL FDAT FTag2={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE}
     28  DECL LDAT LCPDAT2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     29  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P12                     ",POINT2[] "P12                     ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT15                  ",CONT[] "                        ",CP_VEL[] "2.0    [...]
@@ base line 23, backup line 32 @@
     32  DECL E6POS XP10={X 1081.09485,Y -250.197342,Z 931.476,A -96.8303,B 37.9899406,C -15.7576666,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     33  DECL FDAT FP10={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    34  DECL E6POS XP30={X -602.469604,Y -2473.76245,Z 446.371094,A -89.4232254,B -2.67896390,C -179.996689,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    35  DECL FDAT FP30={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     36  DECL E6POS XAtPick3={X 1206.28552,Y -208.912048,Z 214.158249,A -91.4409,B -0.232809141,C 0.168289974,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     37  DECL FDAT FAtPick3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    38  DECL E6POS XP1={X -603.354553,Y -2477.18481,Z 667.120239,A -89.3294754,B 0.653617203,C -179.853607,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    39  DECL FDAT FP1={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    40  DECL LDAT LCPDAT3={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     41  DECL E6POS XP40={X 1206.28552,Y -208.912048,Z 630.625366,A -91.4409,B -0.232809082,C 0.168290034,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     42  DECL FDAT FP40={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    43  DECL E6POS XP50={X 1206.28552,Y -208.912048,Z 409.521729,A -91.4413757,B -0.232714087,C 0.168696448,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    44  DECL FDAT FP50={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    45  DECL E6POS XP60={X 671.407898,Y -378.268097,Z 2030.44653,A -89.8029327,B 7.84505653,C 24.4156590,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    46  DECL FDAT FP60={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    47  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     48  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    49  DECL E6POS XP70={X 1525.90320,Y -261.054626,Z 1246.12451,A 16.2779942,B 28.5338478,C 22.5772171,S 2,T 42,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    50  DECL FDAT FP70={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    51  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     52  DECL E6POS XP30ABOVEPICK={X 1206.28552,Y -208.912048,Z 298.869263,A -91.4409,B -0.232809111,C 0.168290,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     53  DECL FDAT FP30AbovePick={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    54  DECL E6POS XP2={X -599.756165,Y -2478.73,Z 369.150330,A -89.4027710,B -3.84103417,C 179.935089,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    55  DECL FDAT FP2={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    56  DECL PDAT PPDAT6={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    57  DECL E6POS XP3={X -599.698364,Y -2469.82422,Z 501.779144,A -89.4027710,B -3.84103417,C 179.935089,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    58  DECL FDAT FP3={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    59  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    60  DECL PDAT PPDAT0={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    61  DECL E6POS XP0={X 1206.28552,Y -208.912048,Z 573.307922,A -91.4409,B -0.232809082,C 0.168290049,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    62  DECL FDAT FP0={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    63  DECL LDAT LCPDAT4={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    64  DECL PDAT PPDAT8={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    65  DECL E6POS XP4={X 0.0,Y 0.0,Z 0.0,A 0.0,B 0.0,C 0.0,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    66  DECL FDAT FP4={TOOL_NO 0,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    67  DECL PDAT PPDAT9={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    68  DECL E6POS XP5={X 1206.28552,Y -208.912048,Z 1092.82214,A -91.4409,B -0.232809037,C 0.168290079,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    69  DECL FDAT FP5={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    70  DECL E6POS XP6={X 12.7359648,Y -130.494156,Z 3309.79932,A -58.5948639,B -68.7112122,C 63.6888771,S 3,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    71  DECL FDAT FP6={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    72  DECL PDAT PPDAT10={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    73  DECL E6POS XP7={X -1067.77161,Y -2105.70923,Z -1670.46326,A -142.262650,B 26.2927914,C -143.375824,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    74  DECL FDAT FP7={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
```
_11 more lines: see diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1.dat.diff_

### `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`

changed, integrator program: 3 code line(s) removed, 5 added; 85 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1.src.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1.src.diff)

Attributes: &COMMENT 03-10-R1 PICK ST1 -> &COMMENT St1_PICK_GE4

```diff
@@ base line 11, backup line 22 @@
     22  BAS (#INITMOV,0 )
     33  AC_pickUPCheck (1)
+    40  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
+    46  GRPg_Check(1, 1, FALSE, 1)
     50  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254])
-    46  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
-    57  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO NUT_START=TRUE
     55  $BWDSTART=FALSE
     56  PDAT_ACT=PPDAT15
     57  FDAT_ACT=FP12
     58  BAS(#PTP_PARAMS,100)
+    59  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO NUT_STAR=TRUE
     60  PTP XP12
     63  $BWDSTART=FALSE
@@ base line 92, backup line 88 @@
     88  LIN XAtPick3
     96  GRPg_SetStateAndCheck(1, 2, 0.2, 1)
-   108  IF NOT di004UseDryCycle THEN
+   102  GRPg_Check(1, 2, FALSE, 1)
+   106  IF di004UseDryCycle==FALSE THEN
    109  WAIT FOR ( $IN[253] ) AND ( $IN[254] )
    112  $OUT[18]=TRUE
```

### `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.dat`

changed, integrator program: 0 code line(s) removed, 56 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.dat.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.dat.diff)

Data changes:

- added 20 E6POS: XP0, XP1, XP2, XP3, XP4, XP5, XP6, XP7, XP11, XP13, XP14, XP15 ...
- added 20 FDAT: FP0, FP1, FP2, FP3, FP4, FP5, FP6, FP7, FP11, FP13, FP14, FP15 ...
- added 3 LDAT: LCPDAT0, LCPDAT3, LCPDAT4
- added 13 PDAT: PPDAT0, PPDAT1, PPDAT3, PPDAT5, PPDAT6, PPDAT7, PPDAT8, PPDAT9, PPDAT10, PPDAT11, PPDAT14, PPDAT16 ...

```diff
@@ base line 9, backup line 9 @@
      9  EXT BAS (BAS_COMMAND :IN,REAL :IN )
     10  DECL INT SUCCESS
+    17  DECL E6POS XTag4={X -612.686,Y -1589.39600,Z 2916.51807,A 84.5120,B -104.062,C 7.85700,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    18  DECL FDAT FTag4={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE}
+    19  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    20  DECL E6POS XTag3={X -570.159,Y -2455.64600,Z 462.298,A 90.7960,B -176.000,C -0.0550000,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    21  DECL FDAT FTag3={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE}
     22  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    23  DECL E6POS XTag1={X -570.159,Y -2469.59692,Z 262.786,A 90.7960,B -176.000,C -0.0560000,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    24  DECL FDAT FTag1={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE}
     25  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 0.0,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    26  DECL E6POS XTag2={X -570.159,Y -2466.10889,Z 312.664,A 90.7960,B -176.000,C -0.0560000,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    27  DECL FDAT FTag2={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE}
     28  DECL LDAT LCPDAT2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     29  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P0                      ",POINT2[] "P0                      ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT0                   ",CONT[] "                        ",CP_VEL[] "2.0    [...]
@@ base line 23, backup line 32 @@
     32  DECL E6POS XP10={X 1081.09485,Y -250.197342,Z 931.476,A -96.8303,B 37.9899406,C -15.7576666,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     33  DECL FDAT FP10={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    34  DECL E6POS XP30={X -602.469604,Y -2473.76245,Z 446.371094,A -89.4232254,B -2.67896390,C -179.996689,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    35  DECL FDAT FP30={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     36  DECL E6POS XAtPick3={X 1206.28552,Y -208.912048,Z 214.158249,A -91.4409,B -0.232809141,C 0.168289974,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     37  DECL FDAT FAtPick3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    38  DECL E6POS XP1={X -603.354553,Y -2477.18481,Z 667.120239,A -89.3294754,B 0.653617203,C -179.853607,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    39  DECL FDAT FP1={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    40  DECL LDAT LCPDAT3={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     41  DECL E6POS XP40={X 1206.28552,Y -208.912048,Z 630.625366,A -91.4409,B -0.232809082,C 0.168290034,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     42  DECL FDAT FP40={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    43  DECL E6POS XP50={X 1206.28552,Y -208.912048,Z 409.521729,A -91.4413757,B -0.232714087,C 0.168696448,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    44  DECL FDAT FP50={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    45  DECL E6POS XP60={X 671.407898,Y -378.268097,Z 2030.44653,A -89.8029327,B 7.84505653,C 24.4156590,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    46  DECL FDAT FP60={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    47  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     48  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    49  DECL E6POS XP70={X 1525.90320,Y -261.054626,Z 1246.12451,A 16.2779942,B 28.5338478,C 22.5772171,S 2,T 42,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    50  DECL FDAT FP70={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    51  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     52  DECL E6POS XP30ABOVEPICK={X 1206.28552,Y -208.912048,Z 298.869263,A -91.4409,B -0.232809111,C 0.168290,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     53  DECL FDAT FP30AbovePick={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    54  DECL E6POS XP2={X -599.756165,Y -2478.73,Z 369.150330,A -89.4027710,B -3.84103417,C 179.935089,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    55  DECL FDAT FP2={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    56  DECL PDAT PPDAT6={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    57  DECL E6POS XP3={X -599.698364,Y -2469.82422,Z 501.779144,A -89.4027710,B -3.84103417,C 179.935089,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    58  DECL FDAT FP3={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    59  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    60  DECL PDAT PPDAT0={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    61  DECL E6POS XP0={X 1206.28552,Y -208.912048,Z 573.307922,A -91.4409,B -0.232809082,C 0.168290049,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    62  DECL FDAT FP0={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    63  DECL LDAT LCPDAT4={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    64  DECL PDAT PPDAT8={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    65  DECL E6POS XP4={X 0.0,Y 0.0,Z 0.0,A 0.0,B 0.0,C 0.0,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    66  DECL FDAT FP4={TOOL_NO 0,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    67  DECL PDAT PPDAT9={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    68  DECL E6POS XP5={X 1206.28552,Y -208.912048,Z 1092.82214,A -91.4409,B -0.232809037,C 0.168290079,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    69  DECL FDAT FP5={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    70  DECL E6POS XP6={X 12.7359648,Y -130.494156,Z 3309.79932,A -58.5948639,B -68.7112122,C 63.6888771,S 3,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    71  DECL FDAT FP6={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    72  DECL PDAT PPDAT10={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    73  DECL E6POS XP7={X -1067.77161,Y -2105.70923,Z -1670.46326,A -142.262650,B 26.2927914,C -143.375824,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    74  DECL FDAT FP7={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
```
_23 more lines: see diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.dat.diff_

### `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`

changed, integrator program: 3 code line(s) removed, 5 added; 86 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src.diff)

Attributes: &COMMENT 03-10-R1 RED RABBIT PICK -> &COMMENT St1_PICK_GE4

```diff
@@ base line 11, backup line 22 @@
     22  BAS (#INITMOV,0 )
     33  AC_pickUPCheck (1)
+    40  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
+    46  GRPg_Check(1, 1, FALSE, 1)
     50  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254])
-    47  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
-    58  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO NUT_START=TRUE
     55  $BWDSTART=FALSE
     56  PDAT_ACT=PPDAT15
     57  FDAT_ACT=FP12
     58  BAS(#PTP_PARAMS,100)
+    59  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO NUT_STAR=TRUE
     60  PTP XP12
     63  $BWDSTART=FALSE
@@ base line 93, backup line 88 @@
     88  LIN XAtPick3
     96  GRPg_SetStateAndCheck(1, 2, 0.2, 1)
-   109  IF NOT di004UseDryCycle THEN
+   102  GRPg_Check(1, 2, FALSE, 1)
+   106  IF di004UseDryCycle==FALSE THEN
    109  WAIT FOR ( $IN[253] ) AND ( $IN[254] )
    112  $OUT[18]=TRUE
```

### `KRC/R1/Program/StylePicks/Options/style1pick1opt2.dat`

changed, integrator program: 0 code line(s) removed, 43 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt2.dat.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt2.dat.diff)

Attributes: &ACCESS RVO1 -> &ACCESS RVP2

Data changes:

- added 16 E6POS: XP0, XP1, XP2, XP3, XP4, XP5, XP6, XP7, XP30, XP50, XP60, XP70 ...
- added 16 FDAT: FP0, FP1, FP2, FP3, FP4, FP5, FP6, FP7, FP30, FP50, FP60, FP70 ...
- added 2 LDAT: LCPDAT3, LCPDAT4
- added 9 PDAT: PPDAT0, PPDAT3, PPDAT5, PPDAT6, PPDAT7, PPDAT8, PPDAT9, PPDAT10, PPDAT11

```diff
@@ base line 9, backup line 9 @@
      9  EXT BAS (BAS_COMMAND :IN,REAL :IN )
     10  DECL INT SUCCESS
+    17  DECL E6POS XTag4={X -612.686,Y -1589.39600,Z 2916.51807,A 84.5120,B -104.062,C 7.85700,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    18  DECL FDAT FTag4={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE}
     19  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    20  DECL E6POS XTag3={X -570.159,Y -2455.64600,Z 462.298,A 90.7960,B -176.000,C -0.0550000,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    21  DECL FDAT FTag3={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE}
     22  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    23  DECL E6POS XTag1={X -570.159,Y -2469.59692,Z 262.786,A 90.7960,B -176.000,C -0.0560000,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    24  DECL FDAT FTag1={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE}
     25  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 0.0,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    26  DECL E6POS XTag2={X -570.159,Y -2466.10889,Z 312.664,A 90.7960,B -176.000,C -0.0560000,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    27  DECL FDAT FTag2={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE}
     28  DECL LDAT LCPDAT2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     29  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P8                      ",POINT2[] "P8                      ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT12                  ",CONT[] "                        ",CP_VEL[] "2.0    [...]
@@ base line 24, backup line 32 @@
     32  DECL E6POS XP10={X 1164.28674,Y -250.197327,Z 931.476,A -96.8303,B 37.9899406,C -15.7576675,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     33  DECL FDAT FP10={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    34  DECL E6POS XP30={X -602.469604,Y -2473.76245,Z 446.371094,A -89.4232254,B -2.67896390,C -179.996689,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    35  DECL FDAT FP30={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     36  DECL E6POS XAtPick3={X 1206.51978,Y -207.283051,Z 215.779846,A -91.4152374,B 0.285709,C 0.179984391,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     37  DECL FDAT FAtPick3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    38  DECL E6POS XP1={X -603.354553,Y -2477.18481,Z 667.120239,A -89.3294754,B 0.653617203,C -179.853607,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    39  DECL FDAT FP1={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    40  DECL LDAT LCPDAT3={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     41  DECL E6POS XP40={X 1206.28552,Y -208.912048,Z 630.625366,A -91.4409,B -0.232809082,C 0.168290034,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     42  DECL FDAT FP40={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    43  DECL E6POS XP50={X 1206.28552,Y -208.912048,Z 409.521729,A -91.4413757,B -0.232714087,C 0.168696448,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    44  DECL FDAT FP50={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    45  DECL E6POS XP60={X 671.407898,Y -378.268097,Z 2030.44653,A -89.8029327,B 7.84505653,C 24.4156590,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    46  DECL FDAT FP60={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    47  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     48  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    49  DECL E6POS XP70={X 1525.90320,Y -261.054626,Z 1246.12451,A 16.2779942,B 28.5338478,C 22.5772171,S 2,T 42,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    50  DECL FDAT FP70={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    51  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     52  DECL E6POS XP30ABOVEPICK={X 1206.28552,Y -208.912048,Z 298.869263,A -91.4409,B -0.232809111,C 0.168290,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     53  DECL FDAT FP30AbovePick={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    54  DECL E6POS XP2={X -599.756165,Y -2478.73,Z 369.150330,A -89.4027710,B -3.84103417,C 179.935089,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    55  DECL FDAT FP2={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    56  DECL PDAT PPDAT6={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    57  DECL E6POS XP3={X -599.698364,Y -2469.82422,Z 501.779144,A -89.4027710,B -3.84103417,C 179.935089,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    58  DECL FDAT FP3={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    59  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    60  DECL PDAT PPDAT0={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    61  DECL E6POS XP0={X 1206.28552,Y -208.912048,Z 573.307922,A -91.4409,B -0.232809082,C 0.168290049,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    62  DECL FDAT FP0={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    63  DECL LDAT LCPDAT4={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    64  DECL PDAT PPDAT8={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    65  DECL E6POS XP4={X 0.0,Y 0.0,Z 0.0,A 0.0,B 0.0,C 0.0,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    66  DECL FDAT FP4={TOOL_NO 0,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    67  DECL PDAT PPDAT9={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    68  DECL E6POS XP5={X 1206.28552,Y -208.912048,Z 1092.82214,A -91.4409,B -0.232809037,C 0.168290079,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    69  DECL FDAT FP5={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    70  DECL E6POS XP6={X 12.7359648,Y -130.494156,Z 3309.79932,A -58.5948639,B -68.7112122,C 63.6888771,S 3,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    71  DECL FDAT FP6={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    72  DECL PDAT PPDAT10={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    73  DECL E6POS XP7={X -1067.77161,Y -2105.70923,Z -1670.46326,A -142.262650,B 26.2927914,C -143.375824,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    74  DECL FDAT FP7={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
```
_3 more lines: see diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt2.dat.diff_

### `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`

changed, integrator program: 3 code line(s) removed, 5 added; 90 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt2.src.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt2.src.diff)

Attributes: &ACCESS RVO1 -> &ACCESS RVP2; &COMMENT 03-10-R1 PICK ST2 -> &COMMENT St1_PICK_GE4

```diff
@@ base line 11, backup line 22 @@
     22  BAS (#INITMOV,0 )
     33  AC_pickUPCheck (2)
+    40  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
+    46  GRPg_Check(1, 1, FALSE, 1)
     50  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254])
-    48  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
-    59  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO NUT_START=TRUE
     55  $BWDSTART=FALSE
     56  PDAT_ACT=PPDAT1
     57  FDAT_ACT=FP10
     58  BAS(#PTP_PARAMS,100)
+    59  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO NUT_STAR=TRUE
     60  PTP XP10 C_DIS
     63  $BWDSTART=FALSE
@@ base line 87, backup line 81 @@
     81  LIN XAtPick3
     89  GRPg_SetStateAndCheck(1, 2, 0.2, 1)
-   103  IF NOT di004UseDryCycle THEN
+    95  GRPg_Check(1, 2, FALSE, 1)
+    99  IF di004UseDryCycle==FALSE THEN
    102  WAIT FOR ( $IN[253] ) AND ( $IN[254] )
    105  $OUT[18]=TRUE
```

### `KRC/R1/Program/Styles/optiones/style1opt1.src`

added, integrator program: 0 code line(s) removed, 40 added; 29 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Styles/optiones/style1opt1.src.diff](diffs/KRC/R1/Program/Styles/optiones/style1opt1.src.diff)

Attributes: +&ACCESS RVP1; +&REL 40; +&COMMENT GE4_002

```diff
@@ base line end, backup line 4 @@
+     4  DEF Style1Opt1 ( )
+    20  IF di065PickupMachine1 AND NOT di066PickupMachine2 THEN
+    22  style1pick1opt1()
+    24  style1app1opt1A()
+    25  Style1App1Opt2A()
+    26  Style1App1Opt3A()
+    28  style1app2opt1()
+    29  IF bScrapGE4==TRUE THEN
+    30  RejectGE4()
+    31  ELSE
+    32  style1app2opt2()
+    33  IF bScrapGE4==TRUE THEN
+    34  RejectGE4()
+    35  ELSE
+    36  Style1Drop1Opt1()
+    37  ENDIF
+    38  ENDIF
+    40  ELSE
+    42  IF di066PickupMachine2 AND NOT di065PickupMachine1 THEN
+    44  style1pick1opt2()
+    46  style1app1opt1B()
+    47  Style1App1Opt2B()
+    48  Style1App1Opt3B()
+    50  style1app2opt1()
+    51  IF bScrapGE4==TRUE THEN
+    52  RejectGE4()
+    53  ELSE
+    54  style1app2opt2()
+    55  IF bScrapGE4==TRUE THEN
+    56  RejectGE4()
+    57  ELSE
+    58  Style1Drop1Opt1()
+    59  ENDIF
+    60  ENDIF
+    61  ENDIF
+    62  ENDIF
+    66  PARTPRESENT1=FALSE
+    67  PARTPRESENT2=FALSE
+    68  PARTPRESENT3=FALSE
+    71  END
```

### `KRC/R1/Program/Styles/optiones/style1opt10autorr.src`

added, integrator program: 0 code line(s) removed, 6 added; 15 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Styles/optiones/style1opt10autorr.src.diff](diffs/KRC/R1/Program/Styles/optiones/style1opt10autorr.src.diff)

Attributes: +&ACCESS RVO1; +&REL 3; +&COMMENT GE4_002

```diff
@@ base line end, backup line 4 @@
+     4  DEF Style1Opt10AutoRR( )
+    18  Style1Pick1Opt1AutoRR()
+    19  style1app2opt1()
+    20  style1app2opt2()
+    21  style1drop1opt2AutoRR()
+    23  END
```

### `KRC/R1/Program/Styles/style_1.dat`

changed, integrator program: 0 code line(s) removed, 7 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Styles/style_1.dat.diff](diffs/KRC/R1/Program/Styles/style_1.dat.diff)

Data changes:

- added 6 PDAT: PPDAT1, PPDAT2, PPDAT3, PPDAT4, PPDAT5, PPDAT6
- added 1 SIGNAL: di141RedRabbitFail

```diff
@@ base line 7, backup line 7 @@
      7  EXT BAS (BAS_COMMAND :IN,REAL :IN )
      8  DECL INT SUCCESS
+    13  SIGNAL di141RedRabbitFail $IN[141]
     16  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "POUNCE                  ",POINT2[] "POUNCE                  ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT6                   ",CONT[] "                        ",CP_VEL[] "2.0    [...]
+    17  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    18  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    19  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    20  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    21  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    22  DECL PDAT PPDAT6={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
     23  ENDDAT
```

### `KRC/R1/Program/Utilities/RejectGE4.dat`

changed, integrator program: 0 code line(s) removed, 32 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Utilities/RejectGE4.dat.diff](diffs/KRC/R1/Program/Utilities/RejectGE4.dat.diff)

Data changes:

- added 11 E6POS: XP11, XP12, XP20, XP21, XP22, XP26, XP30, XPABOVESCRAP, XPSCRAPREORIENT, XReject_Drop, XSCRAP_POUNCE
- added 11 FDAT: FP11, FP12, FP20, FP21, FP22, FP26, FP30, FPAboveScrap, FPScrapReorient, FReject_Drop, FScrap_Pounce
- added 10 PDAT: PPDAT1, PPDAT2, PPDAT3, PPDAT4, PPDAT5, PPDAT6, PPDAT7, PPDAT8, PPDAT28, PPDAT31

```diff
@@ base line 7, backup line 7 @@
      7  EXT BAS (BAS_COMMAND :IN,REAL :IN )
      8  DECL INT SUCCESS
+    15  DECL E6POS XPSCRAPREORIENT={X 2153.09570,Y 1755.13818,Z 2068.92651,A -8.10456848,B -7.40806341,C -132.602493,S 2,T 43,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     16  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P27                     ",POINT2[] "P27                     ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT32                  ",CONT[] "C_DIS                   ",CP_VEL[] "2      [...]
+    17  DECL FDAT FPScrapReorient={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    18  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    19  DECL E6POS XPABOVESCRAP={X 2375.58740,Y 1146.28662,Z 2113.63257,A -15.2346992,B -12.9237299,C -133.089966,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    20  DECL FDAT FPAboveScrap={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    21  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    22  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    23  DECL E6POS XSCRAP_POUNCE={X 1988.17371,Y 1131.17041,Z 1238.16,A -56.3896446,B 5.16084337,C -175.312164,S 2,T 43,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    24  DECL FDAT FScrap_Pounce={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    25  DECL E6POS XReject_Drop={X 2069.87720,Y 1447.17029,Z 200.832,A -55.7535553,B 0.336941630,C -179.384842,S 2,T 43,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    26  DECL FDAT FReject_Drop={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    27  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    28  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
     29  DECL E6POS XP10={X -724.403137,Y -1811.34314,Z 1367.20557,A -104.758530,B 0.614156485,C 179.947769,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     30  DECL FDAT FP10={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    31  DECL PDAT PPDAT6={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    32  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    33  DECL E6POS XP11={X 1625.17554,Y 419.790771,Z 1424.78357,A -47.9713402,B 1.16016603,C -173.202026,S 2,T 43,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    34  DECL FDAT FP11={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    35  DECL E6POS XP12={X -21.1073933,Y 977.088257,Z 1822.06055,A -57.9586,B 86.2354584,C -137.216766,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    36  DECL FDAT FP12={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    37  DECL PDAT PPDAT8={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
     38  DECL PDAT PL={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    39  DECL E6POS XP20={X 2719.51270,Y 311.994171,Z 1611.79553,A -0.154689506,B 3.52242422,C 177.449234,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    40  DECL FDAT FP20={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    41  DECL E6POS XP30={X 3228.21240,Y 452.756042,Z 1483.90466,A 2.29265,B 2.86626720,C 177.589737,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    42  DECL FDAT FP30={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    43  DECL E6POS XP21={X 2719.51270,Y 311.994171,Z 1611.79553,A -0.154689506,B 3.52242422,C 177.449234,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    44  DECL FDAT FP21={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    45  DECL PDAT PPDAT28={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    46  DECL E6POS XP22={X -725.920410,Y -1758.69482,Z 1448.59143,A -104.766548,B 0.615574777,C 179.948090,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    47  DECL FDAT FP22={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     48  DECL LDAT LCPDAT0={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     49  DECL E6POS XP23={X -703.896545,Y -1395.42871,Z 344.753052,A -135.022919,B 21.6832848,C -1.44161212,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
@@ base line 26, backup line 55 @@
     55  DECL E6POS XP25={X -518.438721,Y -800.197693,Z 3339.05908,A -175.274445,B -73.1114883,C 13.2109089,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     56  DECL FDAT FP25={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    57  DECL PDAT PPDAT31={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    58  DECL E6POS XP26={X 370.852905,Y -298.257416,Z 2804.38916,A -147.361786,B -35.6047363,C 79.4075775,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    59  DECL FDAT FP26={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     60  DECL E6POS XP27={X -1209.28430,Y -1491.03662,Z 1129.57971,A -146.959381,B 2.43560171,C 8.39888477,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     61  DECL FDAT FP27={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
```

### `KRC/R1/Program/Utilities/RejectGE4.src`

changed, integrator program: 0 code line(s) removed, 1 added; 38 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Utilities/RejectGE4.src.diff](diffs/KRC/R1/Program/Utilities/RejectGE4.src.diff)

Attributes: -&COMMENT 03-10-R1 REJECT

```diff
@@ base line 46, backup line 33 @@
     33  LIN XP23
     40  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
+    46  GRPg_Check(1, 1, FALSE, 1)
     49  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254] )
     53  $BWDSTART=FALSE
```

### `KRC/R1/Program/masref_user.dat`

changed, integrator program: 0 code line(s) removed, 67 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/masref_user.dat.diff](diffs/KRC/R1/Program/masref_user.dat.diff)

Attributes: &ACCESS RVO1 -> &ACCESS RVO7

Data changes:

- added 22 E6POS: XP0, XP1, XP2, XP3, XP4, XP5, XP6, XP8, XP11, XP12, XP13, XP14 ...
- added 22 FDAT: FP0, FP1, FP2, FP3, FP4, FP5, FP6, FP8, FP11, FP12, FP13, FP14 ...
- added 11 LDAT: LCPDAT0, LCPDAT1, LCPDAT2, LCPDAT3, LCPDAT4, LCPDAT5, LCPDAT9, LCPDAT10, LCPDAT11, LCPDAT12, LCPDAT13
- added 12 PDAT: PPDAT1, PPDAT2, PPDAT3, PPDAT6, PPDAT7, PPDAT8, PPDAT9, PPDAT10, PPDAT11, PPDAT12, PPDAT13, PPDAT14

```diff
@@ base line 5, backup line 5 @@
      5  DEFDAT masref_user
      8  EXT BAS (BAS_COMMAND :IN,REAL :IN )
+    15  DECL E6POS XP1={X 771.684875,Y 1042.88721,Z 737.000916,A -148.484344,B -76.1350861,C -33.4368,S 2,T 43,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     16  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P0                      ",POINT2[] "P0                      ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT19                  ",CONT[] "                        ",CP_VEL[] "2.0    [...]
+    17  DECL FDAT FP1={TOOL_NO 1,BASE_NO 4,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    18  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    19  DECL E6POS XP2={X -152.238663,Y 615.762451,Z -392.502960,A 167.793732,B 0.890011191,C 1.12833,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    20  DECL FDAT FP2={TOOL_NO 1,BASE_NO 4,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    21  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    22  DECL E6POS XP3={X -80.0698090,Y 676.307739,Z -1414.60132,A 167.793716,B 0.889924049,C 1.12850881,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    23  DECL FDAT FP3={TOOL_NO 1,BASE_NO 4,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    24  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    25  DECL E6POS XPREFSWITCH={X -486.106415,Y 1092.98462,Z -486.351685,A -106.778526,B 2.95674634,C -171.498047,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    26  DECL FDAT FPRefSwitch={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    27  DECL LDAT LCPDAT2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    28  DECL E6POS XP4={X -80.0698090,Y 676.307739,Z -1414.60132,A 167.793716,B 0.889924049,C 1.12850881,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    29  DECL FDAT FP4={TOOL_NO 1,BASE_NO 4,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    30  DECL LDAT LCPDAT3={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    31  DECL E6POS XP5={X -152.238663,Y 615.762451,Z -392.502960,A 167.793732,B 0.890011191,C 1.12833,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    32  DECL FDAT FP5={TOOL_NO 1,BASE_NO 4,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    33  DECL LDAT LCPDAT4={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    34  DECL E6POS XP6={X 771.684631,Y 1042.88708,Z 737.001,A -148.484344,B -76.1350784,C -33.4367905,S 2,T 43,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    35  DECL FDAT FP6={TOOL_NO 1,BASE_NO 4,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    36  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     37  DECL E6POS XHOMEPOS={X 874.811523,Y -100.694267,Z 2352.82349,A -4.40716410,B 2.42973685,C 0.669219,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     38  DECL FDAT FHomePos={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
@@ base line 20, backup line 41 @@
     41  DECL FDAT FP7={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     42  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    43  DECL E6POS XP8={X -433.243591,Y 649.095947,Z 704.272461,A -110.291306,B 5.96638775,C -179.082123,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    44  DECL FDAT FP8={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    45  DECL LDAT LCPDAT5={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     46  DECL LDAT LCPDAT6={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     47  DECL E6POS XP9={X -754.263306,Y -752.360107,Z -58.2259216,A 93.9359894,B 87.4085,C -176.908646,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
@@ base line 27, backup line 51 @@
     51  DECL FDAT FP10={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     52  DECL LDAT LCPDAT8={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    53  DECL E6POS XP11={X -70.5918045,Y 521.023560,Z -1469.24475,A 167.536987,B 3.44113851,C 8.19418,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    54  DECL FDAT FP11={TOOL_NO 1,BASE_NO 4,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    55  DECL LDAT LCPDAT9={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    56  DECL E6POS XP12={X -70.5918,Y 521.023560,Z -873.411072,A 167.536987,B 3.44113851,C 8.19418,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    57  DECL FDAT FP12={TOOL_NO 1,BASE_NO 4,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    58  DECL LDAT LCPDAT10={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    59  DECL E6POS XP13={X -317.774414,Y 768.403870,Z -235.033524,A 167.615891,B 4.67066622,C 9.54216766,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    60  DECL FDAT FP13={TOOL_NO 1,BASE_NO 4,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    61  DECL LDAT LCPDAT11={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    62  DECL LDAT LCPDAT0={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    63  DECL E6POS XP0={X -503.651337,Y 1034.79419,Z -489.490936,A -106.778526,B 2.95674658,C -171.498047,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    64  DECL FDAT FP0={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    65  DECL LDAT LCPDAT12={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    66  DECL E6POS XP14={X -526.497131,Y 987.852051,Z 368.179169,A -102.828995,B -1.56158221,C -171.254395,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    67  DECL FDAT FP14={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    68  DECL LDAT LCPDAT13={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    69  DECL E6POS XP15={X -336.148285,Y 665.637207,Z 410.031342,A -103.188179,B -1.53990638,C -171.960983,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    70  DECL FDAT FP15={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    71  DECL E6POS XP16={X -384.212372,Y 1013.49115,Z 1497.91638,A -123.715569,B 42.0906258,C 148.746750,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    72  DECL FDAT FP16={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    73  DECL PDAT PPDAT6={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    74  DECL E6POS XPHOME={X 811.073303,Y 379.504303,Z 907.073425,A 160.176132,B -57.3357124,C -11.5811968,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
```
_23 more lines: see diffs/KRC/R1/Program/masref_user.dat.diff_

### `KRC/R1/System/$config.dat`

changed, integrator program: 12 code line(s) removed, 26 added; 56 comment/blank line change(s). Full diff: [diffs/KRC/R1/System/$config.dat.diff](diffs/KRC/R1/System/$config.dat.diff)

Data changes:

- CL_GUN_WELD_MAX (INT): 73000 -> 76000
- CL_GUN_WELD_MIN (INT): 69000 -> 65000
- added 19 BOOL: bscrapGE4_1, bscrapGE4_2, bscrapGE4_3, bscrapGE4_4, bscrapGE4_5, CL_ALL_HOME, CL_CENTERLINE_READY, CL_GUN_WORK_REQ, CL_WeldPressureOK, NUT_STAR, NUT_WELD_RETRY, PARTPRESENT4 ...
- added 3 INT: CL_STEP, NUT_RETRY, Part_Style
- added 2 SIGNAL: CL_ALL_HOME_PLC, NUT_PRESENT1
- removed 1 BOOL: NUT_START
- removed 6 INT: CL_GUN_CLOSE_TIMEOUT, CL_GUN_IN_WINDOW_TIME, CL_GUN_PRESS_BASE, CL_GUN_PRESS_REST, CL_GUN_PRESS_WELD, CL_WELD_PROGRAM
- removed 3 SIGNAL: CL_BeaconBit3001, CL_BeaconBit3008, CL_BeaconBit3024

Runtime values (left out of the code diff): CL_GunStrokePositionLPT: 139790 -> 139785; CL_WeldPinPosition: 27339 -> 27330; STOPM_FLAG: TRUE -> FALSE

```diff
@@ base line 760, backup line 757 @@
    757  BOOL PARTPRESENT2=FALSE
    758  BOOL PARTPRESENT3=FALSE
+   759  BOOL PARTPRESENT4=FALSE
+   760  BOOL PARTPRESENT5=FALSE
+   761  BOOL REDRABBIT
+   762  BOOL REDRABBIT1=FALSE
+   763  BOOL REDRABBIT2=FALSE
+   764  BOOL REDRABBIT3=FALSE
+   765  BOOL REDRABBIT4=FALSE
+   766  BOOL REDRABBIT5=FALSE
+   767  BOOL bscrapGE4_1=FALSE
+   768  BOOL bscrapGE4_2=FALSE
+   769  BOOL bscrapGE4_3=FALSE
+   770  BOOL bscrapGE4_4=FALSE
+   771  BOOL bscrapGE4_5=FALSE
+   772  SIGNAL NUT_PRESENT1 $IN[227]
+   776  INT Part_Style=1
    780  DECL CHAR LDDPLUGIN_VARNAME[19]
    781  LDDPLUGIN_VARNAME[]="LDDPLUGIN_ACTIVATED"
@@ base line 816, backup line 811 @@
    811  SIGNAL CL_PIN_BYTE0 $IN[591] TO $IN[598]
    812  SIGNAL CL_PIN_BYTE1 $IN[599] TO $IN[606]
-   824  SIGNAL CL_BeaconBit3001 $OUT[3001]
-   825  SIGNAL CL_BeaconBit3008 $OUT[3008]
-   826  SIGNAL CL_BeaconBit3024 $OUT[3024]
+   815  BOOL CL_WeldPressureOK=FALSE
+   821  DECL INT CL_STEP=0
    823  DECL INT CL_PIN_WELD_MIN=10000
    824  DECL INT CL_PIN_WELD_MAX=13500
-   838  DECL INT CL_GUN_WELD_MIN=69000
-   839  DECL INT CL_GUN_WELD_MAX=73000
-   842  DECL INT CL_GUN_CLOSE_TIMEOUT=1000
-   843  DECL INT CL_GUN_IN_WINDOW_TIME=300
-   848  DECL INT CL_GUN_PRESS_BASE=405
-   849  DECL INT CL_GUN_PRESS_WELD=1820
-   850  DECL INT CL_GUN_PRESS_REST=39425
-   852  DECL INT CL_WELD_PROGRAM=2
-   860  DECL BOOL NUT_START=FALSE
+   825  DECL INT CL_GUN_WELD_MIN=65000
+   826  DECL INT CL_GUN_WELD_MAX=76000
+   828  DECL BOOL CL_GUN_WORK_REQ=FALSE
+   829  DECL BOOL CL_CENTERLINE_READY=FALSE
+   830  DECL BOOL CL_ALL_HOME=FALSE
+   832  SIGNAL CL_ALL_HOME_PLC $OUT[4000]
+   837  DECL BOOL NUT_STAR=FALSE
    838  DECL BOOL NUT_READY=TRUE
    839  DECL BOOL NUTCYCLE_ACTIVE=FALSE
@@ base line 871, backup line 842 @@
    842  DECL BOOL STEP10DONE=TRUE
    843  DECL BOOL STEP20DONE=TRUE
+   844  DECL INT NUT_RETRY=2
    845  DECL BOOL NUT_PRELOAD_FAULT=FALSE
    846  DECL BOOL NEXT_NUT_READY=TRUE
    847  DECL BOOL NEXT_NUT_REQUEST=FALSE
+   848  DECL BOOL NUT_WELD_RETRY=FALSE
    849  DECL BOOL STEP10_ADV_STARTED=FALSE
    852  ENDDAT
```

### `KRC/R1/System/sps.sub`

changed, integrator program: 7 code line(s) removed, 7 added; 89 comment/blank line change(s). Full diff: [diffs/KRC/R1/System/sps.sub.diff](diffs/KRC/R1/System/sps.sub.diff)

Attributes: &COMMENT 03-10-R1 SUBMIT SPS -> &COMMENT PLC on control

```diff
@@ base line 107, backup line 91 @@
     91  ENDIF
     92  CL_WaterOk = dipw1_WaterOk
-   117  IF dopw1_LowLevel THEN
-   118  CL_BeaconBit3008 = TRUE
-   119  CL_BeaconBit3024 = TRUE
+    97  IF $OUT[478] THEN
+    98  $OUT[3008] = TRUE
+    99  $OUT[3024] = TRUE
    100  ENDIF
-   124  IF dopw1_LevelOk THEN
-   125  CL_BeaconBit3001 = TRUE
-   126  CL_BeaconBit3024 = FALSE
+   102  IF $OUT[477] THEN
+   103  $OUT[3001] = TRUE
+   104  $OUT[3024] = FALSE
    105  ENDIF
-   135  dopw1_StartWater=di013WaterEnable
+   117  $OUT[475]=$IN[13]
    120  PRELOAD()
    126  ENDLOOP
```

### `KRC/R1/TP/AutomationCore/automationcoreroutines.dat`

changed, KUKA system / vendor package: 15 code line(s) removed, 34 added; 11 comment/blank line change(s). Full diff: [diffs/KRC/R1/TP/AutomationCore/automationcoreroutines.dat.diff](diffs/KRC/R1/TP/AutomationCore/automationcoreroutines.dat.diff)

Data changes:

- added 4 BOOL: bScrapBackpanel, bScrapCrossMBR, bScrapSMBRlower, bScrapSMBRupper
- added 1 INT: ScrapCount
- added 29 SIGNAL: di100CameraJudmentOK, di101CameraJudmentNG, di106PartRejeted, di227SensorCamera, di466Reserved, di467Reserved, di470Reserved, di610Stud_Nut_Present1, di611Stud_Nut_Present2, di612Stud_Nut_Present3, di613Stud_Nut_Present4, di630Stud_Nut_Present1 ...
- removed 15 SIGNAL: di100CameraJudgmentOK, di101CameraJudgmentNG, di106PartRejected, di227NutPresent1, di466PartClampOpen, di467PartClampClosed, di470QFPAdvanced, do106PartRejected, do498UpperPinExtend, do499UpperPinRetract, do501PartClampClose, do502PartClampOpen ...

```diff
@@ base line 137, backup line 137 @@
    137  GLOBAL SIGNAL di098Spare $IN[98]
    138  GLOBAL SIGNAL di099Spare $IN[99]
-   139  GLOBAL SIGNAL di100CameraJudgmentOK $IN[100]
-   140  GLOBAL SIGNAL di101CameraJudgmentNG $IN[101]
+   139  GLOBAL SIGNAL di100CameraJudmentOK $IN[100]
+   140  GLOBAL SIGNAL di101CameraJudmentNG $IN[101]
    141  GLOBAL SIGNAL di102Spare $IN[102]
    142  GLOBAL SIGNAL di103Spare $IN[103]
    143  GLOBAL SIGNAL di104Spare $IN[104]
    144  GLOBAL SIGNAL di105Spare $IN[105]
-   145  GLOBAL SIGNAL di106PartRejected $IN[106]
+   145  GLOBAL SIGNAL di106PartRejeted $IN[106]
    146  GLOBAL SIGNAL di107Spare $IN[107]
    147  GLOBAL SIGNAL di108Spare $IN[108]
@@ base line 314, backup line 314 @@
    314  GLOBAL SIGNAL do104Axis1Bit128 $OUT[104]
    315  GLOBAL SIGNAL do105Axis1Bit256 $OUT[105]
-   316  GLOBAL SIGNAL do106PartRejected $OUT[106]
+   316  GLOBAL SIGNAL do106PartRejeted $OUT[106]
    317  GLOBAL SIGNAL do107Hopper1LowLevel $OUT[107]
    318  GLOBAL SIGNAL do108Hopper2LowLevel $OUT[108]
@@ base line 638, backup line 638 @@
    638  GLOBAL SIGNAL di225WaterFlowOK $IN[225]
    639  GLOBAL SIGNAL di226Spare $IN[226]
-   642  GLOBAL SIGNAL di227NutPresent1 $IN[227]
+   640  GLOBAL SIGNAL di227SensorCamera $IN[227]
    641  GLOBAL SIGNAL di228Spare $IN[228]
    642  GLOBAL SIGNAL di229Spare $IN[229]
@@ base line 1343, backup line 1341 @@
   1341  GLOBAL SIGNAL do496Reserved $OUT[496]
   1342  GLOBAL SIGNAL do497Reserved $OUT[497]
-  1347  GLOBAL SIGNAL do498UpperPinExtend $OUT[498]
-  1348  GLOBAL SIGNAL do499UpperPinRetract $OUT[499]
+  1343  GLOBAL SIGNAL do498Reserved $OUT[498]
+  1344  GLOBAL SIGNAL do499Reserved $OUT[499]
   1345  GLOBAL SIGNAL do500Reserved $OUT[500]
-  1350  GLOBAL SIGNAL do501PartClampClose $OUT[501]
-  1351  GLOBAL SIGNAL do502PartClampOpen $OUT[502]
-  1352  GLOBAL SIGNAL do503QFPAdvance $OUT[503]
-  1353  GLOBAL SIGNAL do504QFPReturn $OUT[504]
-  1354  GLOBAL SIGNAL do505QFPNutBlowOff $OUT[505]
+  1346  GLOBAL SIGNAL do501Reserved $OUT[501]
+  1347  GLOBAL SIGNAL do502Reserved $OUT[502]
+  1348  GLOBAL SIGNAL do503Reserved $OUT[503]
+  1349  GLOBAL SIGNAL do504Reserved $OUT[504]
+  1350  GLOBAL SIGNAL do505Reserved $OUT[505]
   1353  GLOBAL SIGNAL di465Reserved $IN[465]
-  1358  GLOBAL SIGNAL di466PartClampOpen $IN[466]
-  1359  GLOBAL SIGNAL di467PartClampClosed $IN[467]
+  1354  GLOBAL SIGNAL di466Reserved $IN[466]
+  1355  GLOBAL SIGNAL di467Reserved $IN[467]
   1356  GLOBAL SIGNAL di468Reserved $IN[468]
   1357  GLOBAL SIGNAL di469Reserved $IN[469]
-  1362  GLOBAL SIGNAL di470QFPAdvanced $IN[470]
+  1358  GLOBAL SIGNAL di470Reserved $IN[470]
   1359  GLOBAL SIGNAL di471Reserved $IN[471]
   1360  GLOBAL SIGNAL di472WaterTempOK $IN[472]
@@ base line 1592, backup line 1588 @@
   1588  GLOBAL SIGNAL di605ai_Nut1_B13 $IN[605]
```
_24 more lines: see diffs/KRC/R1/TP/AutomationCore/automationcoreroutines.dat.diff_

### Runtime values only

A .dat keeps the last value the program wrote to each of its variables, and the inline-form editor keeps its suggestions (LAST_BASIS...): these files changed only in such values, nobody edited them.

| File | Values | Diff |
|---|---|---|
| `KRC/R1/System/tm_bib.dat` | iTQM_ZEIGER: 1 -> 2; TQM_ACT: {T11 200,T12 200,T13 200,T14 200,T15 200... -> {T11 200,T12 200,T13 200,T14 200,T15 200... | diffs/KRC/R1/System/tm_bib.dat.diff |
| `KRC/R1/TP/GripperSpotTech/grp_func.dat` | GRP_iPreStNo: 2 -> 1; GRP_PreState[1]: {iGrpIn 257,iStInVal -1,bStInVal FALSE,b... -> {iGrpIn 257,iStInVal 1,bStInVal TRUE,bGh...; GRP_PreState[2]: {iGrpIn 258,iStInVal 1,bStInVal TRUE,bGh... -> {iGrpIn 258,iStInVal -1,bStInVal FALSE,b...; GRPg_ProcessData: {ActGrp 1,ReqState 0,LastGrpNo 1,LastStN... -> {ActGrp 1,ReqState 0,LastGrpNo 1,LastStN... | diffs/KRC/R1/TP/GripperSpotTech/grp_func.dat.diff |

### Comment-only changes

| File | Comment/blank line changes | Attributes | Diff |
|---|---|---|---|
| `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src` | 84 | &ACCESS RVO1 -> &ACCESS RVO7; &REL 2 -> &REL 4; &COMMENT 03-10-R1 PNW1 GUN OPEN CHECK -> &COMMENT NUT WELDER GUN OPEN CHECK; +&PARAM DISKPATH = KRC:\R1\Program\Centerline | diffs/KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src.diff |
| `KRC/R1/Program/Centerline/gun_open_check.dat` | 31 | &COMMENT 03-10-R1 PNW1 GUN OPEN CHECK -> &COMMENT NUT WELDER GUN OPEN CHECK | diffs/KRC/R1/Program/Centerline/gun_open_check.dat.diff |
| `KRC/R1/Program/HOME.src` | 11 | &ACCESS RVO1 -> &ACCESS RVP1; -&COMMENT 03-10-R1 MOVE HOME | diffs/KRC/R1/Program/HOME.src.diff |
| `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src` | 36 | &COMMENT 03-10-R1 RED RABBIT DROP -> &COMMENT GE4_Conveyor | diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src.diff |
| `KRC/R1/Program/Styles/style_1.src` | 46 | &COMMENT 03-10-R1 STYLE 1 -> &COMMENT GE4_002 | diffs/KRC/R1/Program/Styles/style_1.src.diff |
| `KRC/R1/Program/Utilities/closeandcheckallclamps.dat` | 0 | &ACCESS RVO1 -> &ACCESS RVO7 | diffs/KRC/R1/Program/Utilities/closeandcheckallclamps.dat.diff |
| `KRC/R1/Program/Utilities/closeandcheckallclamps.src` | 48 | &ACCESS RVO1 -> &ACCESS RVO7; -&COMMENT 03-10-R1 CLOSE GRIPPER 1 | diffs/KRC/R1/Program/Utilities/closeandcheckallclamps.src.diff |
| `KRC/R1/Program/Utilities/gunelectrodechange.src` | 103 | -&COMMENT 03-10-R1 ELECTRODE CHANGE | diffs/KRC/R1/Program/Utilities/gunelectrodechange.src.diff |
| `KRC/R1/Program/Utilities/hometopounce.src` | 11 | -&COMMENT 03-10-R1 NOT CALLED POUNCE | diffs/KRC/R1/Program/Utilities/hometopounce.src.diff |
| `KRC/R1/Program/Utilities/hometorepair.src` | 12 | -&COMMENT 03-10-R1 HOME TO REPAIR | diffs/KRC/R1/Program/Utilities/hometorepair.src.diff |
| `KRC/R1/Program/Utilities/openandcheckallclamps.dat` | 0 | &ACCESS RVO1 -> &ACCESS RVO7 | diffs/KRC/R1/Program/Utilities/openandcheckallclamps.dat.diff |
| `KRC/R1/Program/Utilities/openandcheckallclamps.src` | 42 | &ACCESS RVO1 -> &ACCESS RVO7; -&COMMENT 03-10-R1 OPEN GRIPPER 1 | diffs/KRC/R1/Program/Utilities/openandcheckallclamps.src.diff |
| `KRC/R1/Program/Utilities/pouncetohome.src` | 11 | -&COMMENT 03-10-R1 POUNCE TO HOME | diffs/KRC/R1/Program/Utilities/pouncetohome.src.diff |
| `KRC/R1/Program/Utilities/repairtohome.src` | 9 | -&COMMENT 03-10-R1 REPAIR TO HOME | diffs/KRC/R1/Program/Utilities/repairtohome.src.diff |
| `KRC/R1/Program/home.dat` | 0 | &ACCESS RVO1 -> &ACCESS RVP1 | diffs/KRC/R1/Program/home.dat.diff |
| `KRC/R1/Program/masref_user.src` | 39 | &ACCESS RVO1 -> &ACCESS RVO7; &COMMENT 03-10-R1 MASTERING REF -> &COMMENT Mastering Reference User Program | diffs/KRC/R1/Program/masref_user.src.diff |
| `KRC/R1/Program/tm_useraction.src` | 14 | -&COMMENT 03-10-R1 COLLISION STOP | diffs/KRC/R1/Program/tm_useraction.src.diff |
| `KRC/R1/System/tm_bib.src` | 0 | &ACCESS R2 -> &ACCESS R7; &REL 951 -> &REL 953 | diffs/KRC/R1/System/tm_bib.src.diff |
| `KRC/R1/TP/AutomationCore/automationcoredata.dat` | 2 | - | diffs/KRC/R1/TP/AutomationCore/automationcoredata.dat.diff |
| `KRC/R1/TP/BrakeTest/braketestback.dat` | 0 | &ACCESS RVO1 -> &ACCESS RVO7 | diffs/KRC/R1/TP/BrakeTest/braketestback.dat.diff |
| `KRC/R1/TP/BrakeTest/braketestback.src` | 0 | &ACCESS RVO1 -> &ACCESS RVO7 | diffs/KRC/R1/TP/BrakeTest/braketestback.src.diff |
| `KRC/R1/TP/BrakeTest/braketestreq.dat` | 0 | &ACCESS RVO1 -> &ACCESS RVO7 | diffs/KRC/R1/TP/BrakeTest/braketestreq.dat.diff |
| `KRC/R1/TP/BrakeTest/braketestreq.src` | 0 | &ACCESS RVO1 -> &ACCESS RVO7 | diffs/KRC/R1/TP/BrakeTest/braketestreq.src.diff |
| `KRC/R1/TP/BrakeTest/braketeststart.dat` | 0 | &ACCESS RVO1 -> &ACCESS RVO7 | diffs/KRC/R1/TP/BrakeTest/braketeststart.dat.diff |
| `KRC/R1/TP/BrakeTest/braketeststart.src` | 0 | &ACCESS RVO1 -> &ACCESS RVO7 | diffs/KRC/R1/TP/BrakeTest/braketeststart.src.diff |
| `KRC/R1/TP/NutWeld/nutweldroutines.dat` | 9 | - | diffs/KRC/R1/TP/NutWeld/nutweldroutines.dat.diff |
| `KRC/R1/cell.src` | 51 | &COMMENT 03-10-R1 AUTO EXTERNAL MAIN -> &COMMENT HANDLER on external automatic | diffs/KRC/R1/cell.src.diff |
| `KRC/R1/safetest.src` | 10 | -&COMMENT 03-10-R1 TEST LOOP | diffs/KRC/R1/safetest.src.diff |

## Mechanical checks

Signal declarations changed (names lower-cased):

- $IN[100]: di100camerajudgmentok -> di100camerajudmentok
- $IN[101]: di101camerajudgmentng -> di101camerajudmentng
- $IN[106]: di106partrejected -> di106partrejeted
- $IN[141]: di141spare -> di141redrabbitfail, di141spare
- $IN[227]: di227nutpresent1 -> di227sensorcamera, nut_present1
- $IN[466]: di466partclampopen, di466spare -> di466reserved, di466spare
- $IN[467]: di467partclampclosed, di467spare -> di467reserved, di467spare
- $IN[470]: di470qfpadvanced, di470spare -> di470reserved, di470spare
- $IN[610]: (not declared) -> di610stud_nut_present1
- $IN[611]: (not declared) -> di611stud_nut_present2
- $IN[612]: (not declared) -> di612stud_nut_present3
- $IN[613]: (not declared) -> di613stud_nut_present4
- $IN[630]: (not declared) -> di630stud_nut_present1
- $IN[631]: (not declared) -> di631stud_nut_present2
- $IN[632]: (not declared) -> di632stud_nut_present3
- $IN[633]: (not declared) -> di633stud_nut_present4
- $IN[634]: (not declared) -> di634stud_nut_present5
- $IN[635]: (not declared) -> di635stud_nut_present6
- $IN[777]: (not declared) -> di777stud_nut_present1
- $IN[778]: (not declared) -> di778stud_nut_present2
- $IN[779]: (not declared) -> di779stud_nut_present3
- $IN[780]: (not declared) -> di780stud_nut_present4
- $OUT[106]: do106partrejected -> do106partrejeted
- $OUT[498]: do498upperpinextend -> do498reserved
- $OUT[499]: do499upperpinretract -> do499reserved
- $OUT[501]: do501partclampclose -> do501reserved
- $OUT[502]: do502partclampopen -> do502reserved
- $OUT[503]: do503qfpadvance -> do503reserved
- $OUT[504]: do504qfpreturn -> do504reserved
- $OUT[505]: do505qfpnutblowoff -> do505reserved
- $OUT[3001]: cl_beaconbit3001 -> (not declared)
- $OUT[3008]: cl_beaconbit3008 -> (not declared)
- $OUT[3024]: cl_beaconbit3024 -> (not declared)
- $OUT[4000]: (not declared) -> cl_all_home_plc

### FAIL (2)

- `KRC/R1/Program/StyleApps/Options/style1app1opt3A.dat` [1 fold/block structure] 1 ;FOLD left open at end of file (base had 0 structure defects, backup has 1)
- `KRC/R1/Program/StyleApps/Options/style1app1opt3B.dat` [1 fold/block structure] 1 ;FOLD left open at end of file (base had 0 structure defects, backup has 1)

### WARN (32)

- `KRC/R1/Program/StyleApps/Options/style1app1opt1A.src` [9 module header] new module without the '; Gestamp Standards' header block (C03, docs/CONVENTIONS.md)
- `KRC/R1/Program/StyleApps/Options/style1app1opt1A.src:83` [8 I/O without signal comment] di004UseDryCycle accessed with no comment naming it in the 4 lines above (C24): IF di004UseDryCycle==FALSE THEN
- `KRC/R1/Program/StyleApps/Options/style1app1opt1A.src:137` [5 hand-typed line in inline form] hand-typed line inside inline form - lost on Touch Up (F32): TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO Request_next_nut() PRIO= -1
- `KRC/R1/Program/StyleApps/Options/style1app1opt1B.src` [9 module header] new module without the '; Gestamp Standards' header block (C03, docs/CONVENTIONS.md)
- `KRC/R1/Program/StyleApps/Options/style1app1opt1B.src:83` [8 I/O without signal comment] di004UseDryCycle accessed with no comment naming it in the 4 lines above (C24): IF di004UseDryCycle==FALSE THEN
- `KRC/R1/Program/StyleApps/Options/style1app1opt1B.src:137` [5 hand-typed line in inline form] hand-typed line inside inline form - lost on Touch Up (F32): TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO Request_next_nut() PRIO= -1
- `KRC/R1/Program/StyleApps/Options/style1app1opt2A.src` [9 module header] new module without the '; Gestamp Standards' header block (C03, docs/CONVENTIONS.md)
- `KRC/R1/Program/StyleApps/Options/style1app1opt2A.src:81` [8 I/O without signal comment] di004UseDryCycle accessed with no comment naming it in the 4 lines above (C24): IF di004UseDryCycle==FALSE THEN
- `KRC/R1/Program/StyleApps/Options/style1app1opt2A.src:133` [5 hand-typed line in inline form] hand-typed line inside inline form - lost on Touch Up (F32): TRIGGER WHEN DISTANCE = 1 DELAY = 0 DO Request_next_nut() PRIO= -1
- `KRC/R1/Program/StyleApps/Options/style1app1opt2B.src` [9 module header] new module without the '; Gestamp Standards' header block (C03, docs/CONVENTIONS.md)
- `KRC/R1/Program/StyleApps/Options/style1app1opt2B.src:81` [8 I/O without signal comment] di004UseDryCycle accessed with no comment naming it in the 4 lines above (C24): IF di004UseDryCycle==FALSE THEN
- `KRC/R1/Program/StyleApps/Options/style1app1opt2B.src:133` [5 hand-typed line in inline form] hand-typed line inside inline form - lost on Touch Up (F32): TRIGGER WHEN DISTANCE = 1 DELAY = 0 DO Request_next_nut() PRIO= -1
- `KRC/R1/Program/StyleApps/Options/style1app1opt3A.src` [9 module header] new module without the '; Gestamp Standards' header block (C03, docs/CONVENTIONS.md)
- `KRC/R1/Program/StyleApps/Options/style1app1opt3A.src:75` [8 I/O without signal comment] di004UseDryCycle accessed with no comment naming it in the 4 lines above (C24): IF di004UseDryCycle==FALSE THEN
- `KRC/R1/Program/StyleApps/Options/style1app1opt3B.src` [9 module header] new module without the '; Gestamp Standards' header block (C03, docs/CONVENTIONS.md)
- `KRC/R1/Program/StyleApps/Options/style1app1opt3B.src:75` [8 I/O without signal comment] di004UseDryCycle accessed with no comment naming it in the 4 lines above (C24): IF di004UseDryCycle==FALSE THEN
- `KRC/R1/Program/StyleApps/Options/style1app2opt1.src:62` [8 I/O without signal comment] di004UseDryCycle accessed with no comment naming it in the 4 lines above (C24): IF di004UseDryCycle==FALSE THEN
- `KRC/R1/Program/StyleApps/Options/style1app2opt1.src:90` [8 I/O without signal comment] di004UseDryCycle accessed with no comment naming it in the 4 lines above (C24): IF di004UseDryCycle==FALSE THEN
- `KRC/R1/Program/StyleApps/Options/style1app2opt1.src:118` [8 I/O without signal comment] di004UseDryCycle accessed with no comment naming it in the 4 lines above (C24): IF di004UseDryCycle==FALSE THEN
- `KRC/R1/Program/StyleApps/Options/style1app2opt1.src:136` [8 I/O without signal comment] di004UseDryCycle accessed with no comment naming it in the 4 lines above (C24): IF di004UseDryCycle==FALSE THEN
- `KRC/R1/Program/StyleApps/Options/style1app2opt2.src:57` [8 I/O without signal comment] di101CameraJudmentNG, di100CameraJudmentOK accessed with no comment naming it in the 4 lines above (C24): IF (di100CameraJudmentOK==TRUE) AND (di101CameraJudmentNG==FALSE) THEN
- `KRC/R1/Program/StyleApps/Options/style1app2opt2.src:63` [8 I/O without signal comment] di101CameraJudmentNG, di100CameraJudmentOK accessed with no comment naming it in the 4 lines above (C24): IF (di100CameraJudmentOK==TRUE) AND (di101CameraJudmentNG==FALSE) THEN
- `KRC/R1/Program/StyleApps/Options/style1app2opt2.src:64` [8 I/O without signal comment] do141RedRabbitFailed accessed with no comment naming it in the 4 lines above (C24): do141RedRabbitFailed=TRUE
- `KRC/R1/Program/StyleApps/Options/style1app2opt2.src:66` [8 I/O without signal comment] di101CameraJudmentNG, di100CameraJudmentOK accessed with no comment naming it in the 4 lines above (C24): IF (di100CameraJudmentOK==FALSE) AND (di101CameraJudmentNG==TRUE) THEN
- `KRC/R1/Program/StyleApps/Options/style1app2opt2.src:67` [8 I/O without signal comment] do142RedRabbitPassed accessed with no comment naming it in the 4 lines above (C24): do142RedRabbitPassed=TRUE
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src:106` [8 I/O without signal comment] di004UseDryCycle accessed with no comment naming it in the 4 lines above (C24): IF di004UseDryCycle==FALSE THEN
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src:106` [8 I/O without signal comment] di004UseDryCycle accessed with no comment naming it in the 4 lines above (C24): IF di004UseDryCycle==FALSE THEN
- `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src:99` [8 I/O without signal comment] di004UseDryCycle accessed with no comment naming it in the 4 lines above (C24): IF di004UseDryCycle==FALSE THEN
- `KRC/R1/Program/Styles/optiones/style1opt1.src` [9 module header] new module without the '; Gestamp Standards' header block (C03, docs/CONVENTIONS.md)
- `KRC/R1/Program/Styles/optiones/style1opt1.src:20` [8 I/O without signal comment] di066PickupMachine2, di065PickupMachine1 accessed with no comment naming it in the 4 lines above (C24): IF di065PickupMachine1 AND NOT di066PickupMachine2 THEN
- `KRC/R1/Program/Styles/optiones/style1opt1.src:42` [8 I/O without signal comment] di066PickupMachine2, di065PickupMachine1 accessed with no comment naming it in the 4 lines above (C24): IF di066PickupMachine2 AND NOT di065PickupMachine1 THEN
- `KRC/R1/Program/Styles/optiones/style1opt10autorr.src` [9 module header] new module without the '; Gestamp Standards' header block (C03, docs/CONVENTIONS.md)

### INFO (6)

- `KRC/R1/Program/StyleApps/Options/style1app1opt1A.src:69` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR NUT_READY== TRUE
- `KRC/R1/Program/StyleApps/Options/style1app1opt1B.src:69` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR NUT_READY== TRUE
- `KRC/R1/Program/StyleApps/Options/style1app1opt2A.src:68` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR NEXT_NUT_READY==TRUE
- `KRC/R1/Program/StyleApps/Options/style1app1opt2B.src:68` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR NEXT_NUT_READY==TRUE
- `KRC/R1/Program/StyleApps/Options/style1app1opt3A.src:62` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR NEXT_NUT_READY==TRUE
- `KRC/R1/Program/StyleApps/Options/style1app1opt3B.src:62` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR NEXT_NUT_READY==TRUE
