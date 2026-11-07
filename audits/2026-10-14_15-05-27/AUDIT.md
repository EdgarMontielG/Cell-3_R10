# Backup audit - c19d21f8-BMW_03_WINDOWS-2CPT70E_BMW_03_10_R1_658424.zip

- Backup: `/root/.claude/uploads/50f56c92-2919-5ae3-94c9-0de4476bbe87/c19d21f8-BMW_03_WINDOWS-2CPT70E_BMW_03_10_R1_658424.zip` (sha256 `a6ac5a6e30df2f15...`)
- am.ini: archive `C:\windows\TEMP\tmpC8BA.tmp\`, date `2026-10-14_15-05-27`, config `All`, robot `BMW_03_10_R1`, serial `658424`, KSS `V8.3.29`
- Compared with: `HEAD` = `118e8cf5ad` "Audit of the programmer's backup of 2026-10-13 07:32; G01 and G02 closed"; first commit (archive as received) `22a98cc8ef`
- Generated 2026-11-07T14:07:46 by tools/audit_backup.py

## Summary

| | |
|---|---|
| Entries audited (Log Files/ skipped: 8) | 316 |
| Unchanged | 238 |
| Changed | 75 |
| Added | 0 |
| Missing from the backup | 8 |
| **Deleted modules still on the controller** | 0 |
| **Pre-cleanup files** | 0 |
| Edited on top of the pre-cleanup file | 0 |
| KRL files with code changes | 26 |
| Code lines removed / added | 84 / 112 |
| KRL files with comment-only changes | 31 |
| KRL files with runtime values only (written by the program, not edits) | 6 |
| Checks FAIL / WARN / INFO | 0 / 9 / 0 |

**Needs attention:**

- WARN 3 entries outside the KUKA archive layout ignored (e.g. Archive.log)
- WARN 8 file(s) of the base missing from the backup - deleted on the robot, or an incomplete archive (e.g. KRC/R1/Program/Utilities/capchange.dat; all in Files, "Missing from the backup")
- 9 WARN in the mechanical checks

## The backup itself

- WARN: 3 entries outside the KUKA archive layout ignored (e.g. Archive.log)
- WARN: 8 file(s) of the base missing from the backup - deleted on the robot, or an incomplete archive (e.g. KRC/R1/Program/Utilities/capchange.dat; all in Files, "Missing from the backup")
- INFO: KRC/R1/System/tm_bib.dat: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)

## Deleted modules still present

_none_

## Pre-cleanup files

_none_

## Files

### Changed (75)

- `C/KRC/Roboter/Config/User/Common/HNFINFO.SAF` - controller configuration - binary, 32 bytes
- `C/KRC/Roboter/Config/User/Common/PNIOIM4Data.dat` - controller configuration
- `C/KRC/Roboter/Config/User/Common/PersistPC/KrcRrtLog.xml` - controller configuration - 5 line(s) removed, 5 added - diffs/C/KRC/Roboter/Config/User/Common/PersistPC/KrcRrtLog.xml.diff
- `C/KRC/Roboter/Config/User/Common/SCTLCRC.IMG` - controller configuration - binary, 99 bytes
- `C/KRC/Roboter/Config/User/Common/SCTLCRC.XML` - controller configuration - 1 line(s) removed, 1 added - diffs/C/KRC/Roboter/Config/User/Common/SCTLCRC.XML.diff
- `C/KRC/Roboter/Config/User/Common/SCTLPARA.SAF` - controller configuration - binary, 14269 bytes
- `C/KRC/Roboter/Config/User/Common/SCtlPara.sg` - controller configuration - binary, 26574 bytes
- `C/KRC/Roboter/Config/User/Common/SafetyConfigData.xml` - controller configuration - 3 line(s) removed, 13 added - diffs/C/KRC/Roboter/Config/User/Common/SafetyConfigData.xml.diff
- `C/KRC/Roboter/Config/User/KrlModSize.bin` - controller configuration - 27 line(s) removed, 59 added - diffs/C/KRC/Roboter/Config/User/KrlModSize.bin.diff
- `C/KRC/Roboter/Rdc/RdcDirectoryContents.txt` - controller configuration - 5 line(s) removed, 5 added - diffs/C/KRC/Roboter/Rdc/RdcDirectoryContents.txt.diff
- `C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8.asz` - controller configuration - binary, 4290355 bytes
- `KRC/R1/Mada/$machine.dat` - machine data
- `KRC/R1/Mada/$robcor.dat` - machine data
- `KRC/R1/Program/Centerline/centerline_weld.src` - integrator program
- `KRC/R1/Program/Centerline/gun_open_check.dat` - integrator program
- `KRC/R1/Program/Centerline/gun_open_check.src` - integrator program
- `KRC/R1/Program/Centerline/preload.dat` - integrator program
- `KRC/R1/Program/Centerline/preload.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt1a.dat` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt1a.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt1b.dat` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt1b.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt2a.dat` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt2a.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt2b.dat` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt2b.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt3a.dat` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt3a.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt3b.dat` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt3b.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app2opt1.dat` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app2opt1.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app2opt2.dat` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app2opt2.src` - integrator program
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.dat` - integrator program
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src` - integrator program
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt2autorr.dat` - integrator program
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt2autorr.src` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.dat` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.dat` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.src` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt2.dat` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src` - integrator program
- `KRC/R1/Program/Utilities/closeandcheckallclamps.dat` - integrator program
- `KRC/R1/Program/Utilities/closeandcheckallclamps.src` - integrator program
- `KRC/R1/Program/Utilities/openandcheckallclamps.dat` - integrator program
- `KRC/R1/Program/Utilities/openandcheckallclamps.src` - integrator program
- `KRC/R1/Program/Utilities/rejectge4.dat` - integrator program
- `KRC/R1/Program/Utilities/rejectge4.src` - integrator program
- `KRC/R1/Program/home.dat` - integrator program
- `KRC/R1/Program/home.src` - integrator program
- `KRC/R1/Program/masref_user.dat` - integrator program
- `KRC/R1/Program/masref_user.src` - integrator program
- `KRC/R1/System/$config.dat` - integrator program
- `KRC/R1/System/masref_main.dat` - KUKA system / vendor package
- `KRC/R1/System/masref_main.src` - KUKA system / vendor package
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
- `KRC/R1/TP/GripperSpotTech/grp_func.dat` - KUKA system / vendor package
- `KRC/R1/TP/NutWeld/nutwelddata.dat` - KUKA system / vendor package
- `KRC/R1/TP/NutWeld/nutweldroutines.dat` - KUKA system / vendor package
- `KRC/R1/cell.src` - integrator program
- `KRC/STEU/Mada/$custom.dat` - machine data
- `Registry/LMSOFTWAREKUKA Roboter GmbHPerformance.amr` - controller configuration - 372 line(s) removed, 345 added - diffs/Registry/LMSOFTWAREKUKA Roboter GmbHPerformance.amr.diff
- `am.ini` - archive metadata - 3 line(s) removed, 3 added - diffs/am.ini.diff

### Added (0)

_none_

### Missing from the backup (8)

- `KRC/R1/Program/Utilities/capchange.dat`
- `KRC/R1/Program/Utilities/capchange.src`
- `KRC/R1/Program/Utilities/electrodechange.dat`
- `KRC/R1/Program/Utilities/electrodechange.src`
- `KRC/R1/Program/Utilities/redrabbit.dat`
- `KRC/R1/Program/Utilities/redrabbit.src`
- `KRC/R1/safetest.dat`
- `KRC/R1/safetest.src`

### Outside the archive layout (ignored) (3)

- `Archive.log`
- `ArchiveInfo.xml`
- `Ethos -  Purchase Order 263178.pdf`

## Code changes

### `KRC/R1/Program/Centerline/centerline_weld.src`

changed, integrator program: 0 code line(s) removed, 1 added; 1 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/centerline_weld.src.diff](diffs/KRC/R1/Program/Centerline/centerline_weld.src.diff)

```diff
@@ base line 231, backup line 231 @@
    231  dopw1_WeldInit=FALSE
    232  WAIT FOR NOT dipw1_WeldComplete
+   234  NUT_READY=FALSE
    237  dopw1_Nut1Intensify=FALSE
    238  dopw1_Nut1Intensify_Home=TRUE
```

### `KRC/R1/Program/Centerline/gun_open_check.src`

changed, integrator program: 0 code line(s) removed, 3 added; 1 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/gun_open_check.src.diff](diffs/KRC/R1/Program/Centerline/gun_open_check.src.diff)

Attributes: &ACCESS RVO5 -> &ACCESS RVO2; &REL 29 -> &REL 49

```diff
@@ base line 418, backup line 418 @@
    418  $TIMER[21]=0
    419  $TIMER_STOP[21]=FALSE
+   422  IF NOT NUT_READY AND NOT NUTCYCLE_ACTIVE AND NOT NUT_START THEN
+   423  Request_next_nut()
+   424  ENDIF
    425  WAIT FOR NUT_READY==TRUE
    426  IF (nNut>=1) AND (nNut<=3) THEN
```

### `KRC/R1/Program/Centerline/preload.src`

changed, integrator program: 0 code line(s) removed, 26 added; 8 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/preload.src.diff](diffs/KRC/R1/Program/Centerline/preload.src.diff)

```diff
@@ base line 3, backup line 3 @@
      3  DEF PRELOAD ( )
+    20  IF NUT_START AND NUT_READY AND NOT NUTCYCLE_ACTIVE THEN
+    21  NUT_START=FALSE
+    22  ENDIF
     25  IF NUT_START AND NOT NUTCYCLE_ACTIVE THEN
     27  NUT_START=FALSE
@@ base line 251, backup line 257 @@
    257  ENDIF
    258  END
+   260  GLOBAL DEF NUT_STATE_INIT( )
+   263  NUT_START=FALSE
+   264  NEXT_NUT_REQUEST=FALSE
+   265  NEXT_NUT_READY=FALSE
+   266  NUT_READY=FALSE
+   267  NUTCYCLE_ACTIVE=FALSE
+   268  NUT_PRELOAD_STEP=0
+   269  STEP0DONE=FALSE
+   270  STEP10DONE=FALSE
+   271  STEP20DONE=FALSE
+   272  STEP10_ADV_STARTED=FALSE
+   273  NUT_PRELOAD_FAULT=FALSE
+   274  $TIMER_STOP[10]=TRUE
+   275  $TIMER[10]=0
+   276  $TIMER_STOP[11]=TRUE
+   277  $TIMER[11]=0
+   278  $TIMER_STOP[12]=TRUE
+   279  $TIMER[12]=0
+   280  $TIMER_STOP[13]=TRUE
+   281  $TIMER[13]=0
+   283  dopw1_StartFeed=FALSE
+   284  do505QFPNutBlowOff=FALSE
+   285  END
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt1a.dat`

changed, integrator program: 4 code line(s) removed, 4 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1a.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1a.dat.diff)

Data changes:

- FP0 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
- FP8 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
- FP19 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP20 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}

```diff
@@ base line 10, backup line 10 @@
     10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
     17  DECL E6POS XP20={X -3850.82104,Y -108.397034,Z -435.788452,A -178.432037,B 0.654220343,C -179.967712,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    18  DECL FDAT FP20={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    18  DECL FDAT FP20={TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     28  DECL FDAT FPNW1={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     29  DECL E6POS XPNW1={X 123.774101,Y 312.995331,Z -88.6478,A 8.71582699,B 8.82717705,C 1.11576855,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
@@ base line 32, backup line 32 @@
     32  DECL PDAT PPDAT0={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     33  DECL E6POS XP0={X -3704.29346,Y 1.10223198,Z -449.805786,A -178.368118,B 0.266879767,C 179.968445,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    34  DECL FDAT FP0={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    34  DECL FDAT FP0={TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     35  DECL MODULEPARAM_T LAST_TP_PARAMS={PARAMS[] "NutWeld_CmdPos=Weld; NutWeld_Move=LIN; NutWeld_NutWeldDat=NutData1_7; NutWeld_NWGunNr=1; NutWeld_NWSpotNr=7; NutWeld_NWOffset=45; Kuka.MoveDataName=gAboveWeld; Kuka.VelocityPath=2; Kuka. [...]
     36  DECL E6POS XP8={X -3747.39,Y 5.76858711,Z -393.029510,A -178.432297,B -0.654858768,C -179.985626,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    37  DECL FDAT FP8={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    37  DECL FDAT FP8={TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     38  DECL LDAT LCPDAT8={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     39  DECL LDAT LCPDAT12={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
@@ base line 42, backup line 42 @@
     42  DECL PDAT PPDAT18={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     43  DECL E6POS XP19={X -3849.93530,Y -106.544395,Z -442.889893,A -178.432037,B 0.654220402,C -179.967712,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    44  DECL FDAT FP19={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    44  DECL FDAT FP19={TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     45  DECL LDAT LCPDAT18={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     46  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt1b.dat`

changed, integrator program: 4 code line(s) removed, 4 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1b.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1b.dat.diff)

Data changes:

- FP0 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
- FP8 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
- FP19 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP20 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}

```diff
@@ base line 10, backup line 10 @@
     10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
     17  DECL E6POS XP20={X -3850.82104,Y -108.397034,Z -435.788452,A -178.432037,B 0.654220343,C -179.967712,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    18  DECL FDAT FP20={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    18  DECL FDAT FP20={TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     28  DECL FDAT FPNW1={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     29  DECL E6POS XPNW1={X 123.774101,Y 312.995331,Z -88.6478,A 8.71582699,B 8.82717705,C 1.11576855,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
@@ base line 32, backup line 32 @@
     32  DECL PDAT PPDAT0={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     33  DECL E6POS XP0={X -3704.29346,Y 1.10223198,Z -449.805786,A -178.368118,B 0.266879767,C 179.968445,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    34  DECL FDAT FP0={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    34  DECL FDAT FP0={TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     35  DECL MODULEPARAM_T LAST_TP_PARAMS={PARAMS[] "NutWeld_CmdPos=Weld; NutWeld_Move=LIN; NutWeld_NutWeldDat=NutData1_7; NutWeld_NWGunNr=1; NutWeld_NWSpotNr=7; NutWeld_NWOffset=45; Kuka.MoveDataName=gAboveWeld; Kuka.VelocityPath=2; Kuka. [...]
     36  DECL E6POS XP8={X -3747.39,Y 5.76858711,Z -393.029510,A -178.432297,B -0.654858768,C -179.985626,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    37  DECL FDAT FP8={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    37  DECL FDAT FP8={TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     38  DECL LDAT LCPDAT8={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     39  DECL LDAT LCPDAT12={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
@@ base line 42, backup line 42 @@
     42  DECL PDAT PPDAT18={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     43  DECL E6POS XP19={X -3849.93530,Y -106.544395,Z -442.889893,A -178.432037,B 0.654220402,C -179.967712,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    44  DECL FDAT FP19={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    44  DECL FDAT FP19={TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     45  DECL LDAT LCPDAT18={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     46  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt2a.dat`

changed, integrator program: 5 code line(s) removed, 5 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2a.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2a.dat.diff)

Data changes:

- FP0 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
- Fp05 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP06 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
- FP6 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP16 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}

```diff
@@ base line 24, backup line 24 @@
     24  DECL PDAT PPDAT0={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     25  DECL E6POS XP0={X -3747.39,Y 5.76903486,Z -387.973175,A -178.432297,B -0.654858828,C -179.985626,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    26  DECL FDAT FP0={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    26  DECL FDAT FP0={TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     27  DECL E6POS XP5={X -3700.01831,Y -153.317429,Z -426.154480,A -178.336502,B -1.01672721,C 179.960312,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     28  DECL FDAT FP5={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     29  DECL LDAT LCPDAT0={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     30  DECL E6POS XP6={X -3882.34546,Y -153.988113,Z -434.603973,A -178.336502,B -1.01672721,C 179.960312,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    31  DECL FDAT FP6={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    31  DECL FDAT FP6={TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     32  DECL E6POS XP06={X -3876.85596,Y 41.5696564,Z -503.446716,A -178.336945,B 1.01745081,C 179.989838,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    33  DECL FDAT FP06={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    33  DECL FDAT FP06={TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     34  DECL E6POS XP05={X -3741.15063,Y -108.396217,Z -430.732452,A -178.432037,B 0.654220343,C -179.967712,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    35  DECL FDAT Fp05={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    35  DECL FDAT Fp05={TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     36  DECL LDAT LCPDAT6={VEL 2.00000,ACC 100.000,APO_DIST 2.00000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     37  DECL PDAT PPDAT26={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
@@ base line 39, backup line 39 @@
     39  DECL LDAT LCPDAT14={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     40  DECL E6POS XP16={X -3882.34546,Y -153.988113,Z -439.433533,A -178.336502,B -1.01672721,C 179.960312,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    41  DECL FDAT FP16={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    41  DECL FDAT FP16={TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     42  DECL LDAT LCPDAT15={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     43  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt2b.dat`

changed, integrator program: 5 code line(s) removed, 5 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2b.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2b.dat.diff)

Data changes:

- FP0 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
- Fp05 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP06 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
- FP6 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP16 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}

```diff
@@ base line 24, backup line 24 @@
     24  DECL PDAT PPDAT0={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     25  DECL E6POS XP0={X -3747.39,Y 5.76903486,Z -387.973175,A -178.432297,B -0.654858828,C -179.985626,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    26  DECL FDAT FP0={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    26  DECL FDAT FP0={TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     27  DECL E6POS XP5={X -3700.01831,Y -153.317429,Z -426.154480,A -178.336502,B -1.01672721,C 179.960312,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     28  DECL FDAT FP5={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     29  DECL LDAT LCPDAT0={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     30  DECL E6POS XP6={X -3882.34546,Y -153.988113,Z -434.603973,A -178.336502,B -1.01672721,C 179.960312,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    31  DECL FDAT FP6={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    31  DECL FDAT FP6={TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     32  DECL E6POS XP06={X -3876.85596,Y 41.5696564,Z -503.446716,A -178.336945,B 1.01745081,C 179.989838,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    33  DECL FDAT FP06={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    33  DECL FDAT FP06={TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     34  DECL E6POS XP05={X -3741.15063,Y -108.396217,Z -430.732452,A -178.432037,B 0.654220343,C -179.967712,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    35  DECL FDAT Fp05={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    35  DECL FDAT Fp05={TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     36  DECL LDAT LCPDAT6={VEL 2.00000,ACC 100.000,APO_DIST 2.00000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     37  DECL PDAT PPDAT26={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
@@ base line 39, backup line 39 @@
     39  DECL LDAT LCPDAT14={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     40  DECL E6POS XP16={X -3882.34546,Y -153.988113,Z -439.433533,A -178.336502,B -1.01672721,C 179.960312,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    41  DECL FDAT FP16={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    41  DECL FDAT FP16={TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     42  DECL LDAT LCPDAT15={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     43  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt3a.dat`

changed, integrator program: 5 code line(s) removed, 5 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3a.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3a.dat.diff)

Data changes:

- FP7 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
- FP13 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
- FP16 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP17 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP20 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}

```diff
@@ base line 10, backup line 10 @@
     10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
     17  DECL E6POS XP20={X -3747.39,Y 5.76903486,Z -387.973175,A -178.432297,B -0.654858828,C -179.985626,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    18  DECL FDAT FP20={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    18  DECL FDAT FP20={TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     20  DECL FDAT FPNW1={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     21  DECL E6POS XPNW1={X -684.340210,Y -936.680359,Z 6.96372366,A -85.0124512,B -3.00309157,C -5.37728167,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
@@ base line 25, backup line 25 @@
     25  DECL LDAT Lpnw1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     26  DECL E6POS XP7={X -3596.62695,Y -2.77881479,Z -444.531586,A -178.368134,B 0.266892016,C 179.968369,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    27  DECL FDAT FP7={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    27  DECL FDAT FP7={TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     28  DECL E6POS XP13={X -3882.44,Y -49.6154175,Z -451.879456,A -178.367340,B 0.267035931,C 179.968063,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    29  DECL FDAT FP13={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    29  DECL FDAT FP13={TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     30  DECL LDAT LCPDAT4={VEL 2.00000,ACC 100.000,APO_DIST 2.00000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     31  DECL PDAT PPDAT25={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
@@ base line 33, backup line 33 @@
     33  DECL LDAT LCPDAT10={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     34  DECL E6POS XP16={X -3884.36157,Y -60.7767830,Z -438.167816,A -178.367172,B -0.266017556,C 179.960464,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    35  DECL FDAT FP16={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    35  DECL FDAT FP16={TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     36  DECL LDAT LCPDAT11={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     37  DECL E6POS XP17={X -3884.34131,Y -60.7792091,Z -433.814606,A -178.367172,B -0.266017556,C 179.960464,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    38  DECL FDAT FP17={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    38  DECL FDAT FP17={TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     39  DECL LDAT LCPDAT12={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     40  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt3b.dat`

changed, integrator program: 5 code line(s) removed, 5 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3b.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3b.dat.diff)

Data changes:

- FP7 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
- FP13 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
- FP16 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP17 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP20 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}

```diff
@@ base line 10, backup line 10 @@
     10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
     17  DECL E6POS XP20={X -3747.39,Y 5.76903486,Z -387.973175,A -178.432297,B -0.654858828,C -179.985626,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    18  DECL FDAT FP20={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    18  DECL FDAT FP20={TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     20  DECL FDAT FPNW1={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     21  DECL E6POS XPNW1={X -684.340210,Y -936.680359,Z 6.96372366,A -85.0124512,B -3.00309157,C -5.37728167,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
@@ base line 25, backup line 25 @@
     25  DECL LDAT Lpnw1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     26  DECL E6POS XP7={X -3596.62695,Y -2.77881479,Z -444.531586,A -178.368134,B 0.266892016,C 179.968369,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    27  DECL FDAT FP7={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    27  DECL FDAT FP7={TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     28  DECL E6POS XP13={X -3882.44,Y -49.6154175,Z -451.879456,A -178.367340,B 0.267035931,C 179.968063,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    29  DECL FDAT FP13={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    29  DECL FDAT FP13={TOOL_NO 2,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     30  DECL LDAT LCPDAT4={VEL 2.00000,ACC 100.000,APO_DIST 2.00000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     31  DECL PDAT PPDAT25={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
@@ base line 33, backup line 33 @@
     33  DECL LDAT LCPDAT10={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     34  DECL E6POS XP16={X -3884.36157,Y -60.7767830,Z -438.167816,A -178.367172,B -0.266017556,C 179.960464,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    35  DECL FDAT FP16={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    35  DECL FDAT FP16={TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     36  DECL LDAT LCPDAT11={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     37  DECL E6POS XP17={X -3884.34131,Y -60.7792091,Z -433.814606,A -178.367172,B -0.266017556,C 179.960464,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    38  DECL FDAT FP17={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    38  DECL FDAT FP17={TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     39  DECL LDAT LCPDAT12={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     40  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
```

### `KRC/R1/Program/StyleApps/Options/style1app2opt1.dat`

changed, integrator program: 7 code line(s) removed, 7 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.dat.diff)

Attributes: &ACCESS RVO2 -> &ACCESS RVO1

Data changes:

- FP22 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP28 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP31 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP32 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP36 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP37 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP38 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}

```diff
@@ base line 24, backup line 24 @@
     24  DECL PDAT PPDAT16={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     25  DECL E6POS XP22={X -724.403137,Y -1811.34314,Z 1367.20557,A -104.758530,B 0.614156485,C 179.947769,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    26  DECL FDAT FP22={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    26  DECL FDAT FP22={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     27  DECL E6POS XP28={X -802.319214,Y -1890.74048,Z 1835.80981,A -104.760674,B 0.614438713,C 179.948120,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    28  DECL FDAT FP28={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    28  DECL FDAT FP28={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     29  DECL LDAT LCPDAT15={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     30  DECL E6POS XP31={X -792.590820,Y -1863.87073,Z 1820.80676,A -104.762810,B 0.614705622,C 179.948196,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    31  DECL FDAT FP31={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    31  DECL FDAT FP31={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     32  DECL LDAT LCPDAT16={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     33  DECL E6POS XP32={X -744.894226,Y -1870.63672,Z 1831.00122,A -104.765282,B 0.613685668,C 179.947861,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    34  DECL FDAT FP32={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    34  DECL FDAT FP32={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     35  DECL LDAT LCPDAT17={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     36  DECL E6POS XP36={X -709.667664,Y -1914.80627,Z 1836.26062,A -104.766647,B 0.614143848,C 179.947922,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    37  DECL FDAT FP36={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    37  DECL FDAT FP36={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     38  DECL E6POS XP37={X -709.665833,Y -1914.80737,Z 1695.13147,A -104.766281,B 0.614050865,C 179.947906,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    39  DECL FDAT FP37={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    39  DECL FDAT FP37={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     40  DECL E6POS XP38={X -698.678955,Y -1881.92224,Z 1822.50745,A -104.765289,B 0.613687098,C 179.947861,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    41  DECL FDAT FP38={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    41  DECL FDAT FP38={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     42  DECL PDAT PPDAT35={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     43  DECL PDAT PPDAT36={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
```

### `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`

changed, integrator program: 6 code line(s) removed, 2 added; 19 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.src.diff)

Attributes: &ACCESS RVO2 -> &ACCESS RVO1

```diff
@@ base line 141, backup line 141 @@
    141  ENDIF
    142  CASE 12
-   143  IF (PARTPRESENT1==TRUE ) AND (PARTPRESENT2==TRUE) AND (PARTPRESENT3==TRUE) THEN
-   144  do141RedRabbitFailed=TRUE
-   145  ENDIF
-   147  IF (PARTPRESENT1==FALSE ) AND (PARTPRESENT2==FALSE) AND (PARTPRESENT3==FALSE) THEN
-   149  do142RedRabbitPassed=TRUE
-   150  ENDIF
+   144  do141RedRabbitFailed = PARTPRESENT1 OR PARTPRESENT2 OR PARTPRESENT3
+   145  do142RedRabbitPassed = NOT (PARTPRESENT1 OR PARTPRESENT2 OR PARTPRESENT3)
    146  ENDSWITCH
    148  ENDIF
```

### `KRC/R1/Program/StyleApps/Options/style1app2opt2.dat`

changed, integrator program: 2 code line(s) removed, 2 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.dat.diff)

Data changes:

- FP3 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP6 (FDAT): {TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}

```diff
@@ base line 17, backup line 17 @@
     17  DECL LDAT LCPDAT0={VEL 2.00000,ACC 80.0000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     18  DECL E6POS XP3={X -709.833740,Y -2035.40430,Z 1423.71777,A -98.4577484,B -5.84655905,C -164.806564,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    19  DECL FDAT FP3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    19  DECL FDAT FP3={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     20  DECL E6POS XP6={X -3780.88599,Y -731.523132,Z -847.811157,A -165.231735,B -0.613393545,C -0.0522668548,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    21  DECL FDAT FP6={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    21  DECL FDAT FP6={TOOL_NO 2,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     22  DECL PDAT PPDAT10={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     23  ENDDAT
```

### `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`

changed, integrator program: 3 code line(s) removed, 1 added; 7 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.src.diff)

```diff
@@ base line 63, backup line 63 @@
     63  CASE 12
     65  IF (di100CameraJudgmentOK==TRUE) AND (di101CameraJudgmentNG==FALSE) THEN
+    66  do142RedRabbitPassed=FALSE
     67  do141RedRabbitFailed=TRUE
-    67  ENDIF
-    69  IF (di100CameraJudgmentOK==FALSE) AND (di101CameraJudgmentNG==TRUE) THEN
-    70  do142RedRabbitPassed=TRUE
     68  ENDIF
     69  ENDSWITCH
```

### `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.dat`

changed, integrator program: 3 code line(s) removed, 3 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt1.dat.diff](diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt1.dat.diff)

Attributes: &REL 234 -> &REL 235

Data changes:

- XATDROP3 (E6POS) re-taught: moved 66.7 mm
- FAtDrop3 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP5 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}

```diff
@@ base line 9, backup line 9 @@
      9  DECL INT SUCCESS
     16  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P0                      ",POINT2[] "P0                      ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT0                   ",CONT[] "                        ",CP_VEL[] "2.0    [...]
-    17  DECL E6POS XATDROP3={X -1563.67676,Y -913.306702,Z 449.989929,A 179.143311,B 30.0803795,C -34.7621422,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    18  DECL FDAT FAtDrop3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    17  DECL E6POS XATDROP3={X -1563.67676,Y -979.977295,Z 449.989929,A 179.143311,B 30.0803795,C -34.7621422,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    18  DECL FDAT FAtDrop3={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     19  DECL MODULEPARAM_T LAST_TP_PARAMS={PARAMS[] "AC_CmdZones=DropOff; AC_CmdParam=2; AC_ZoneRepo=True; AC_UseState=True; AC_Blending=False                               "}
     20  DECL E6POS XP2={X -1279.37976,Y -897.098,Z 616.329468,A 176.629059,B 21.7134552,C -1.31570351,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
@@ base line 22, backup line 22 @@
     22  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     23  DECL E6POS XP5={X -1279.37976,Y -897.098,Z 616.329468,A 176.629059,B 21.7134552,C -1.31570351,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    24  DECL FDAT FP5={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    24  DECL FDAT FP5={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     25  DECL PDAT PPDAT10={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     26  DECL PDAT PPDAT11={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
```

### `KRC/R1/Program/StyleDrops/Options/style1drop1opt2autorr.dat`

changed, integrator program: 9 code line(s) removed, 9 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt2autorr.dat.diff](diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt2autorr.dat.diff)

Data changes:

- FAtPick3 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP27 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP28 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP32 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP33 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP34 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP35 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP36 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP37 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}

```diff
@@ base line 29, backup line 29 @@
     29  DECL PDAT PPDAT23={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     30  DECL E6POS XP27={X -709.692566,Y -2053.68652,Z 1506.28467,A -104.821503,B 4.90587568,C 179.018478,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    31  DECL FDAT FP27={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    31  DECL FDAT FP27={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     32  DECL PDAT PPDAT25={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     33  DECL E6POS XP28={X -1268.63135,Y -1764.04834,Z 1506.28467,A -121.480026,B 4.90587568,C 179.018478,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    34  DECL FDAT FP28={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    34  DECL FDAT FP28={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     35  DECL PDAT PPDAT26={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     36  DECL PDAT PPDAT30={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     37  DECL E6POS XP32={X -988.705139,Y -820.766479,Z 2569.14844,A 137.545090,B -48.9822197,C 56.5858917,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    38  DECL FDAT FP32={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    38  DECL FDAT FP32={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     39  DECL PDAT PPDAT31={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     40  DECL E6POS XP33={X 370.852905,Y -298.257416,Z 2804.38916,A -147.361786,B -35.6047363,C 79.4075775,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    41  DECL FDAT FP33={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    41  DECL FDAT FP33={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     42  DECL PDAT PPDAT32={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     43  DECL E6POS XP34={X 874.811584,Y -100.693466,Z 2352.82349,A -4.40710449,B 2.42972946,C 0.669244647,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    44  DECL FDAT FP34={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    44  DECL FDAT FP34={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     45  DECL LDAT LCPDAT5={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     46  DECL E6POS XP35={X 1081.09485,Y -250.197342,Z 931.476,A -96.8303,B 37.9899406,C -15.7576666,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    47  DECL FDAT FP35={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    47  DECL FDAT FP35={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     48  DECL PDAT PPDAT33={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     49  DECL E6POS XP36={X 1070.46545,Y -208.124084,Z 714.012268,A -91.4409,B -0.232809603,C 0.168291062,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    50  DECL FDAT FP36={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    50  DECL FDAT FP36={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     51  DECL PDAT PPDAT34={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     52  DECL E6POS XP37={X 1206.28552,Y -208.912048,Z 298.869263,A -91.4409,B -0.232809111,C 0.168290,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    53  DECL FDAT FP37={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    53  DECL FDAT FP37={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     54  DECL LDAT LCPDAT6={VEL 2.00000,ACC 100.000,APO_DIST 0.0,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     55  DECL E6POS XAtPick3={X 1206.28552,Y -208.912048,Z 214.158249,A -91.4409,B -0.232809141,C 0.168289974,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    56  DECL FDAT FAtPick3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    56  DECL FDAT FAtPick3={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     57  DECL LDAT LCPDAT7={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     58  ENDDAT
```

### `KRC/R1/Program/StyleDrops/Options/style1drop1opt2autorr.src`

changed, integrator program: 8 code line(s) removed, 1 added; 38 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt2autorr.src.diff](diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt2autorr.src.diff)

```diff
@@ base line 11, backup line 11 @@
     11  BAS (#INITMOV,0 )
     29  AC_DropOffCheck (2)
-    34  CONTINUE
-    35  do249Group1Home=FALSE
-    38  CONTINUE
-    39  do250Group1Work=TRUE
     34  $BWDSTART=FALSE
     35  PDAT_ACT=PPDAT25
@@ base line 109, backup line 99 @@
     99  BAS(#CP_PARAMS,2)
    100  LIN XAtPick3
-   117  GRPg_SetStateAndCheck(3, 1, 0.2, 1)
-   124  GRPg_Check(1, 1, FALSE, 1)
+   107  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
    111  $BWDSTART=FALSE
    112  LDAT_ACT=LCPDAT2
@@ base line 164, backup line 147 @@
    147  PTP XP25
    155  AC_DropOff (2,True)
-   175  do141RedRabbitFailed=FALSE
-   176  do142RedRabbitPassed=FALSE
    158  PARTPRESENT1=FALSE
    159  PARTPRESENT2=FALSE
```

### `KRC/R1/Program/StylePicks/Options/style1pick1opt1.dat`

changed, integrator program: 3 code line(s) removed, 3 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1.dat.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1.dat.diff)

Attributes: &ACCESS RVO2 -> &ACCESS RVO1

Data changes:

- FP8 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP9 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP40 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}

```diff
@@ base line 26, backup line 26 @@
     26  DECL FDAT FAtPick3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     27  DECL E6POS XP40={X 1206.28552,Y -208.912048,Z 630.625366,A -91.4409,B -0.232809082,C 0.168290034,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    28  DECL FDAT FP40={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    28  DECL FDAT FP40={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     29  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     30  DECL E6POS XP30ABOVEPICK={X 1206.28552,Y -208.912048,Z 298.869263,A -91.4409,B -0.232809111,C 0.168290,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     31  DECL FDAT FP30AbovePick={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     32  DECL E6POS XP8={X 504.083313,Y -786.363220,Z 1705.62256,A -111.705475,B 40.2604485,C 19.4570847,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    33  DECL FDAT FP8={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    33  DECL FDAT FP8={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     34  DECL PDAT PPDAT12={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     35  DECL LDAT LCPDAT5={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     36  DECL E6POS XP9={X 913.201294,Y -527.473816,Z 1006.97571,A -91.4454117,B -0.232742429,C 0.168951720,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    37  DECL FDAT FP9={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    37  DECL FDAT FP9={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     38  DECL PDAT PPDAT13={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     39  DECL E6POS XP12={X 874.811584,Y -100.693466,Z 2352.82349,A -4.40710449,B 2.42972946,C 0.669244647,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
```

### `KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.dat`

changed, integrator program: 5 code line(s) removed, 5 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.dat.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.dat.diff)

Data changes:

- FP1 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP2 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP8 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP9 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP40 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}

```diff
@@ base line 26, backup line 26 @@
     26  DECL FDAT FAtPick3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     27  DECL E6POS XP40={X 1206.28552,Y -208.912048,Z 630.625366,A -91.4409,B -0.232809082,C 0.168290034,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    28  DECL FDAT FP40={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    28  DECL FDAT FP40={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     29  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     30  DECL E6POS XP30ABOVEPICK={X 1206.28552,Y -208.912048,Z 298.869263,A -91.4409,B -0.232809111,C 0.168290,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     31  DECL FDAT FP30AbovePick={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     32  DECL E6POS XP8={X 504.083313,Y -786.363220,Z 1705.62256,A -111.705475,B 40.2604485,C 19.4570847,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    33  DECL FDAT FP8={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    33  DECL FDAT FP8={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     34  DECL PDAT PPDAT12={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     35  DECL LDAT LCPDAT5={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     36  DECL E6POS XP9={X 913.201294,Y -527.473816,Z 1006.97571,A -91.4454117,B -0.232742429,C 0.168951720,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    37  DECL FDAT FP9={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    37  DECL FDAT FP9={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     38  DECL PDAT PPDAT13={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     39  DECL E6POS XP12={X 874.811584,Y -100.693466,Z 2352.82349,A -4.40710449,B 2.42972946,C 0.669244647,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
@@ base line 41, backup line 41 @@
     41  DECL PDAT PPDAT15={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     42  DECL E6POS XP1={X -724.403137,Y -1811.34314,Z 1367.20557,A -104.758530,B 0.614156485,C 179.947769,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    43  DECL FDAT FP1={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    43  DECL FDAT FP1={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     44  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     45  DECL E6POS XP2={X -391.021637,Y -1718.64941,Z 1886.74170,A -101.501625,B -31.6927509,C 144.874908,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    46  DECL FDAT FP2={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    46  DECL FDAT FP2={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     47  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     48  ENDDAT
```

### `KRC/R1/Program/StylePicks/Options/style1pick1opt2.dat`

changed, integrator program: 2 code line(s) removed, 2 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt2.dat.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt2.dat.diff)

Data changes:

- FP8 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP40 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}

```diff
@@ base line 27, backup line 27 @@
     27  DECL FDAT FAtPick3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     28  DECL E6POS XP40={X 1206.28552,Y -208.912048,Z 630.625366,A -91.4409,B -0.232809082,C 0.168290034,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    29  DECL FDAT FP40={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    29  DECL FDAT FP40={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     30  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     31  DECL E6POS XP30ABOVEPICK={X 1206.28552,Y -208.912048,Z 298.869263,A -91.4409,B -0.232809111,C 0.168290,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     32  DECL FDAT FP30AbovePick={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     33  DECL E6POS XP8={X 504.083313,Y -786.363220,Z 1705.62256,A -111.705475,B 40.2604485,C 19.4570847,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    34  DECL FDAT FP8={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    34  DECL FDAT FP8={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     35  DECL PDAT PPDAT12={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     36  ENDDAT
```

### `KRC/R1/Program/Utilities/rejectge4.dat`

changed, integrator program: 2 code line(s) removed, 2 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Utilities/rejectge4.dat.diff](diffs/KRC/R1/Program/Utilities/rejectge4.dat.diff)

Data changes:

- FP10 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
- FP23 (FDAT): {TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE} -> {TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}

```diff
@@ base line 16, backup line 16 @@
     16  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P27                     ",POINT2[] "P27                     ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT32                  ",CONT[] "C_DIS                   ",CP_VEL[] "2      [...]
     17  DECL E6POS XP10={X -724.403137,Y -1811.34314,Z 1367.20557,A -104.758530,B 0.614156485,C 179.947769,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    18  DECL FDAT FP10={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    18  DECL FDAT FP10={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     19  DECL PDAT PL={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     20  DECL LDAT LCPDAT0={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     21  DECL E6POS XP23={X -703.896545,Y -1395.42871,Z 344.753052,A -135.022919,B 21.6832848,C -1.44161212,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    22  DECL FDAT FP23={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    22  DECL FDAT FP23={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     23  DECL PDAT PPDAT29={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     24  DECL E6POS XP24={X -3261.39941,Y -725.320496,Z 42.1042595,A -135.019226,B -21.6840553,C 178.585571,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
```

### `KRC/R1/Program/masref_user.src`

changed, integrator program: 1 code line(s) removed, 1 added; 2 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/masref_user.src.diff](diffs/KRC/R1/Program/masref_user.src.diff)

Attributes: &ACCESS RVO4 -> &ACCESS RVO1

```diff
@@ base line 127, backup line 127 @@
    127  PTP XHomePos
    131  OpenAndCheckAllClamps ( )
-   133  do930MasterRefInProcess=TRUE
+   133  do930MasterRefInProcess=FALSE
    135  WAIT SEC 1
    137  END
```

### `KRC/R1/System/$config.dat`

changed, integrator program: 3 code line(s) removed, 3 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/System/$config.dat.diff](diffs/KRC/R1/System/$config.dat.diff)

Runtime values (left out of the code diff): CL_GunStrokePositionLPT: 139770 -> 139740; CL_WeldPinPosition: 27432 -> 27321; NUT_READY: TRUE -> FALSE; STOPM_FLAG: FALSE -> TRUE

```diff
@@ base line 233, backup line 233 @@
    233  DECL FRAME TOOL_DATA[16]
    234  TOOL_DATA[1]={X 0.0,Y 0.0,Z 380.790,A -90.0000,B -90.0000,C -90.0000}
-   235  TOOL_DATA[2]={X 420.390,Y 195.500,Z 259.650,A 0.0,B 0.0,C 0.0}
+   235  TOOL_DATA[2]={X 0.0,Y 0.0,Z 380.790,A -90.0000,B -90.0000,C -90.0000}
    236  TOOL_DATA[3]={X -186.740,Y 93.0000,Z 420.740,A -180.000,B 0.0,C 0.0}
    237  TOOL_DATA[4]={X 0.0,Y 0.0,Z 0.0,A 0.0,B 0.0,C 0.0}
@@ base line 251, backup line 251 @@
    251  DECL CHAR TOOL_NAME[16,24]
    252  TOOL_NAME[1,]="TOOL 1"
-   253  TOOL_NAME[2,]="TOOL 2"
+   253  TOOL_NAME[2,]="TOOL 1 WITH PART"
    254  TOOL_NAME[3,]="TOOL 3"
    255  TOOL_NAME[4,]=" "
@@ base line 269, backup line 269 @@
    269  DECL LOAD LOAD_DATA[16]
    271  LOAD_DATA[1]={M 67.2787094,CM {X -2.62049794,Y 17.9348812,Z 219.182,A -90.0034943,B -0.200046,C 0.0651830},J {X 5.25000,Y 5.25000,Z 5.25000}}
-   272  LOAD_DATA[2]={M 129.297,CM {X 38.8040,Y -94.4510,Z 136.873,A 89.7770,B -0.721000,C 0.991000},J {X 5.25000,Y 5.57200,Z 7.65800}}
+   272  LOAD_DATA[2]={M 68.2787094,CM {X -2.62049794,Y 17.9348812,Z 219.182,A -90.0034943,B -0.200046,C 0.0651830},J {X 5.25000,Y 5.25000,Z 5.25000}}
    273  LOAD_DATA[3]={M 129.297,CM {X 38.8040,Y -94.4510,Z 136.873,A 89.7770,B -0.721000,C 0.991000},J {X 5.25000,Y 5.57200,Z 7.65800}}
    274  LOAD_DATA[4]={M -1.00000,CM {X 0.0,Y 0.0,Z 0.0,A 0.0,B 0.0,C 0.0},J {X 0.0,Y 0.0,Z 0.0}}
```

### `KRC/R1/System/sps.sub`

changed, integrator program: 0 code line(s) removed, 2 added; 1 comment/blank line change(s). Full diff: [diffs/KRC/R1/System/sps.sub.diff](diffs/KRC/R1/System/sps.sub.diff)

```diff
@@ base line 31, backup line 31 @@
     31  BM_OUTPUTVALUE = 0
     34  TorqueDefinitions()
+    42  NUT_STATE_INIT()
     44  doCriticalWZ=FALSE
     45  do111Gun1ElectrodeChange=FALSE
@@ base line 93, backup line 95 @@
     95  GRPg_ChkSetStatePLC()
     99  NutWeld_BKG ( )
+   102  AutomationCore_BKG ( )
    110  CL_GunStrokePositionLPT=(CL_LPT_BYTE1*65536)+(CL_LPT_BYTE2*256)+CL_LPT_BYTE3
    113  CL_WeldPinPosition=(CL_PIN_BYTE0*256)+CL_PIN_BYTE1
```

### `KRC/R1/cell.src`

changed, integrator program: 0 code line(s) removed, 9 added; 2 comment/blank line change(s). Full diff: [diffs/KRC/R1/cell.src.diff](diffs/KRC/R1/cell.src.diff)

```diff
@@ base line 13, backup line 13 @@
     13  DMY[]="---"
     15  InitializeSystem()
+    17  NUT_STATE_INIT()
     18  HOME()
     20  LOOP
@@ base line 59, backup line 61 @@
     61  IF ((nStyle>0) AND (nOption>0)) THEN
     63  EndOfCycle( )
+    65  do015WorkComplete=TRUE
+    66  WHILE (di015WorkCompleteAckn==FALSE)
+    67  IF (Exists_KrlMsg(nWorkComplete_Handle)==FALSE) THEN
+    68  nWorkComplete_Handle=Set_Krlmsg (#STATE, AutomationCore_Msg[4], AutoCore_MsgPar[], AutoCore_MsgOpt_NoStop)
+    69  ENDIF
+    70  ENDWHILE
+    71  do005RobotInCycle = FALSE
+    72  bAutoCore_Clear=Clear_KRLMsg(nWorkComplete_Handle)
     74  StopCycTime( )
     75  ENDIF
```

### `C/KRC/Roboter/Config/User/Common/PNIOIM4Data.dat`

changed, controller configuration: 1 code line(s) removed, 1 added; 0 comment/blank line change(s). Full diff: [diffs/C/KRC/Roboter/Config/User/Common/PNIOIM4Data.dat.diff](diffs/C/KRC/Roboter/Config/User/Common/PNIOIM4Data.dat.diff)

```diff
@@ base line 1, backup line 1 @@
-     1  zUªxýkð
+     1  zUªòfíÒ
```

### `KRC/R1/System/tm_bib.dat`

changed, KUKA system / vendor package: 1 code line(s) removed, 1 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/System/tm_bib.dat.diff](diffs/KRC/R1/System/tm_bib.dat.diff)

Attributes: &REL 964 -> &REL 965

Data changes:

- iSTOP_TYPE (INT): 20 -> 53

Runtime values (left out of the code diff): iTQM_ZEIGER: 1 -> 2

```diff
@@ base line 36, backup line 36 @@
     36  REAL ScalingImpact=250000.0
     37  REAL TooLarge=100000.0
-    47  DECL INT iSTOP_TYPE=20
+    47  DECL INT iSTOP_TYPE=53
     48  DECL REAL rPAR=0.0
     50  GLOBAL INT iTQM_DELAY=150
```

### Runtime values only

A .dat keeps the last value the program wrote to each of its variables, and the inline-form editor keeps its suggestions (LAST_BASIS...): these files changed only in such values, nobody edited them.

| File | Values | Diff |
|---|---|---|
| `KRC/R1/Program/Centerline/gun_open_check.dat` | CL_ClampOpen: TRUE -> FALSE; nCtCycle: 276828 -> 102432; nCtInWelder[1]: 4032 -> 4104; nCtInWelder[2]: 3924 -> 4008; nCtInWelder[3]: 3912 -> 3996; nCtNutToNut[1]: 263832 -> 88656; ... and 7 more | diffs/KRC/R1/Program/Centerline/gun_open_check.dat.diff |
| `KRC/R1/TP/AutomationCore/automationcoredata.dat` | bACProcessReset: TRUE -> FALSE; nAutoCore_Handle: 10729 -> 10782; nCycleStart_Handle: 10938 -> 12431; nCycleTime: 67 -> 42; nCycTime_Handle: 10937 -> 12430; nReqEnter_Handle: 10558 -> 11827; ... and 1 more | diffs/KRC/R1/TP/AutomationCore/automationcoredata.dat.diff |
| `KRC/R1/TP/AutomationCore/automationcoreroutines.dat` | bACEntryGranted: FALSE -> TRUE | diffs/KRC/R1/TP/AutomationCore/automationcoreroutines.dat.diff |
| `KRC/R1/TP/GripperSpotTech/grp_func.dat` | GRP_iPreStNo: 2 -> 1; GRP_PreState[1]: {iGrpIn 257,iStInVal -1,bStInVal FALSE,b... -> {iGrpIn 257,iStInVal 1,bStInVal TRUE,bGh...; GRP_PreState[2]: {iGrpIn 258,iStInVal 1,bStInVal TRUE,bGh... -> {iGrpIn 258,iStInVal -1,bStInVal FALSE,b...; GRPg_ProcessData: {ActGrp 1,ReqState 0,LastGrpNo 0,LastStN... -> {ActGrp 1,ReqState 0,LastGrpNo 1,LastStN... | diffs/KRC/R1/TP/GripperSpotTech/grp_func.dat.diff |
| `KRC/R1/TP/NutWeld/nutwelddata.dat` | bNutWeldProcessReset: TRUE -> FALSE; bNutWeldWOJoining: TRUE -> FALSE; rNutSensorValue[3]: 2586.00 -> 11866.0 | diffs/KRC/R1/TP/NutWeld/nutwelddata.dat.diff |
| `KRC/R1/TP/NutWeld/nutweldroutines.dat` | rLowerLVDT: 2586.00 -> 11866.0 | diffs/KRC/R1/TP/NutWeld/nutweldroutines.dat.diff |

### Comment-only changes

| File | Comment/blank line changes | Attributes | Diff |
|---|---|---|---|
| `KRC/R1/Mada/$machine.dat` | 0 | -&ACCESS  RV; -&PARAM VERSION = 1.0.0; -&PARAM DISKPATH = MADA; +&ACCESS RV$ | diffs/KRC/R1/Mada/$machine.dat.diff |
| `KRC/R1/Mada/$robcor.dat` | 0 | +&PARAM DISKPATH = MADA; -&PARAM DISKPATH = MADA | diffs/KRC/R1/Mada/$robcor.dat.diff |
| `KRC/R1/Program/Centerline/preload.dat` | 0 | -&ACCESS  RV; -&COMMENT 03-10-R1 PNW1 NUT PRELOAD; -&PARAM DISKPATH = Program/Centerline; +&ACCESS RVO2 | diffs/KRC/R1/Program/Centerline/preload.dat.diff |
| `KRC/R1/Program/StyleApps/Options/style1app1opt1a.src` | 12 | - | diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1a.src.diff |
| `KRC/R1/Program/StyleApps/Options/style1app1opt1b.src` | 12 | - | diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1b.src.diff |
| `KRC/R1/Program/StyleApps/Options/style1app1opt2a.src` | 10 | - | diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2a.src.diff |
| `KRC/R1/Program/StyleApps/Options/style1app1opt2b.src` | 10 | - | diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2b.src.diff |
| `KRC/R1/Program/StyleApps/Options/style1app1opt3a.src` | 12 | - | diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3a.src.diff |
| `KRC/R1/Program/StyleApps/Options/style1app1opt3b.src` | 12 | - | diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3b.src.diff |
| `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src` | 8 | &REL 234 -> &REL 235 | diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src.diff |
| `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src` | 6 | &ACCESS RVO2 -> &ACCESS RVO1 | diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1.src.diff |
| `KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.src` | 12 | &COMMENT 03-10-R1 PICK ST1 -> &COMMENT 03-10-R1 RED RABBIT PICK | diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.src.diff |
| `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src` | 8 | - | diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt2.src.diff |
| `KRC/R1/Program/Utilities/closeandcheckallclamps.dat` | 0 | &ACCESS RVO4 -> &ACCESS RVO1 | diffs/KRC/R1/Program/Utilities/closeandcheckallclamps.dat.diff |
| `KRC/R1/Program/Utilities/closeandcheckallclamps.src` | 0 | &ACCESS RVO4 -> &ACCESS RVO1 | diffs/KRC/R1/Program/Utilities/closeandcheckallclamps.src.diff |
| `KRC/R1/Program/Utilities/openandcheckallclamps.dat` | 0 | &ACCESS RVO4 -> &ACCESS RVO1 | diffs/KRC/R1/Program/Utilities/openandcheckallclamps.dat.diff |
| `KRC/R1/Program/Utilities/openandcheckallclamps.src` | 0 | &ACCESS RVO4 -> &ACCESS RVO1 | diffs/KRC/R1/Program/Utilities/openandcheckallclamps.src.diff |
| `KRC/R1/Program/Utilities/rejectge4.src` | 4 | - | diffs/KRC/R1/Program/Utilities/rejectge4.src.diff |
| `KRC/R1/Program/home.dat` | 0 | &ACCESS RVP1 -> &ACCESS RVO1 | diffs/KRC/R1/Program/home.dat.diff |
| `KRC/R1/Program/home.src` | 0 | &ACCESS RVP1 -> &ACCESS RVO1 | diffs/KRC/R1/Program/home.src.diff |
| `KRC/R1/Program/masref_user.dat` | 0 | &ACCESS RVO4 -> &ACCESS RVO1 | diffs/KRC/R1/Program/masref_user.dat.diff |
| `KRC/R1/System/masref_main.dat` | 0 | &ACCESS RVP1 -> &ACCESS RVO1 | diffs/KRC/R1/System/masref_main.dat.diff |
| `KRC/R1/System/masref_main.src` | 0 | &ACCESS RVP1 -> &ACCESS RVO1 | diffs/KRC/R1/System/masref_main.src.diff |
| `KRC/R1/System/tm_bib.src` | 0 | &REL 964 -> &REL 966 | diffs/KRC/R1/System/tm_bib.src.diff |
| `KRC/R1/TP/BrakeTest/braketestback.dat` | 0 | &ACCESS RVO5 -> &ACCESS RVO1 | diffs/KRC/R1/TP/BrakeTest/braketestback.dat.diff |
| `KRC/R1/TP/BrakeTest/braketestback.src` | 0 | &ACCESS RVO5 -> &ACCESS RVO1 | diffs/KRC/R1/TP/BrakeTest/braketestback.src.diff |
| `KRC/R1/TP/BrakeTest/braketestreq.dat` | 0 | &ACCESS RVO5 -> &ACCESS RVO1 | diffs/KRC/R1/TP/BrakeTest/braketestreq.dat.diff |
| `KRC/R1/TP/BrakeTest/braketestreq.src` | 0 | &ACCESS RVO5 -> &ACCESS RVO1 | diffs/KRC/R1/TP/BrakeTest/braketestreq.src.diff |
| `KRC/R1/TP/BrakeTest/braketeststart.dat` | 0 | &ACCESS RVO5 -> &ACCESS RVO1 | diffs/KRC/R1/TP/BrakeTest/braketeststart.dat.diff |
| `KRC/R1/TP/BrakeTest/braketeststart.src` | 0 | &ACCESS RVO5 -> &ACCESS RVO1 | diffs/KRC/R1/TP/BrakeTest/braketeststart.src.diff |
| `KRC/STEU/Mada/$custom.dat` | 0 | +&PARAM DISKPATH = MADA; -&PARAM DISKPATH = MADA | diffs/KRC/STEU/Mada/$custom.dat.diff |

## Mechanical checks

### FAIL (0)

_none_

### WARN (9)

- `KRC/R1/Program/Centerline/preload.src:283` [8 I/O without signal comment] dopw1_StartFeed accessed with no comment naming it in the 4 lines above (C24): dopw1_StartFeed=FALSE
- `KRC/R1/Program/Centerline/preload.src:284` [8 I/O without signal comment] do505QFPNutBlowOff accessed with no comment naming it in the 4 lines above (C24): do505QFPNutBlowOff=FALSE
- `KRC/R1/Program/StyleApps/Options/style1app2opt1.src:144` [8 I/O without signal comment] do141RedRabbitFailed accessed with no comment naming it in the 4 lines above (C24): do141RedRabbitFailed = PARTPRESENT1 OR PARTPRESENT2 OR PARTPRESENT3
- `KRC/R1/Program/StyleApps/Options/style1app2opt1.src:145` [8 I/O without signal comment] do142RedRabbitPassed accessed with no comment naming it in the 4 lines above (C24): do142RedRabbitPassed = NOT (PARTPRESENT1 OR PARTPRESENT2 OR PARTPRESEN
- `KRC/R1/Program/StyleApps/Options/style1app2opt2.src:66` [8 I/O without signal comment] do142RedRabbitPassed accessed with no comment naming it in the 4 lines above (C24): do142RedRabbitPassed=FALSE
- `KRC/R1/Program/masref_user.src:133` [8 I/O without signal comment] do930MasterRefInProcess accessed with no comment naming it in the 4 lines above (C24): do930MasterRefInProcess=FALSE
- `KRC/R1/cell.src:65` [8 I/O without signal comment] do015WorkComplete accessed with no comment naming it in the 4 lines above (C24): do015WorkComplete=TRUE
- `KRC/R1/cell.src:66` [8 I/O without signal comment] di015WorkCompleteAckn accessed with no comment naming it in the 4 lines above (C24): WHILE (di015WorkCompleteAckn==FALSE)
- `KRC/R1/cell.src:71` [8 I/O without signal comment] do005RobotInCycle accessed with no comment naming it in the 4 lines above (C24): do005RobotInCycle = FALSE

### INFO (0)

_none_
