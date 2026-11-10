# Backup audit - a500448e-BMW_03_WINDOWS-2CPT70E_BMW_03_10_R1_658424_1.zip

- Backup: `/root/.claude/uploads/50f56c92-2919-5ae3-94c9-0de4476bbe87/a500448e-BMW_03_WINDOWS-2CPT70E_BMW_03_10_R1_658424_1.zip` (sha256 `1567fd5c63c86e01...`)
- am.ini: archive `C:\windows\TEMP\tmp55DC.tmp\`, date `2026-11-10_08-31-30`, config `All`, robot `BMW_03_10_R1`, serial `658424`, KSS `V8.3.29`
- Compared with: `HEAD` = `2037b79263` "Cycle time closed by Gestamp: out of the deliverables"; first commit (archive as received) `22a98cc8ef`
- Generated 2026-11-10T16:34:07 by tools/audit_backup.py

## Summary

| | |
|---|---|
| Entries audited (Log Files/ skipped: 8) | 313 |
| Unchanged | 267 |
| Changed | 44 |
| Added | 0 |
| Missing from the backup | 2 |
| **Deleted modules still on the controller** | 0 |
| **Pre-cleanup files** | 0 |
| Edited on top of the pre-cleanup file | 0 |
| KRL files with code changes | 18 |
| Code lines removed / added | 45 / 54 |
| KRL files with comment-only changes | 6 |
| KRL files with runtime values only (written by the program, not edits) | 6 |
| Checks FAIL / WARN / INFO | 0 / 5 / 1 |

**Needs attention:**

- WARN 2 entries outside the KUKA archive layout ignored (e.g. Archive.log)
- WARN 2 file(s) of the base missing from the backup - deleted on the robot, or an incomplete archive (e.g. KRC/R1/Program/movetopurge.dat; all in Files, "Missing from the backup")
- WARN KRC/R1/Mada/$machine.dat: machine data file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- WARN KRC/R1/TP/GLUETECH/glue.src: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- 5 WARN in the mechanical checks

## The backup itself

- WARN: 2 entries outside the KUKA archive layout ignored (e.g. Archive.log)
- WARN: 2 file(s) of the base missing from the backup - deleted on the robot, or an incomplete archive (e.g. KRC/R1/Program/movetopurge.dat; all in Files, "Missing from the backup")
- WARN: KRC/R1/Mada/$machine.dat: machine data file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- WARN: KRC/R1/TP/GLUETECH/glue.src: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- INFO: KRC/R1/System/tm_bib.dat: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)

## Deleted modules still present

_none_

## Pre-cleanup files

_none_

## Files

### Changed (44)

- `C/KRC/Roboter/Config/User/Common/HNFINFO.SAF` - controller configuration - binary, 32 bytes
- `C/KRC/Roboter/Config/User/Common/PNIOIM4Data.dat` - controller configuration
- `C/KRC/Roboter/Config/User/Common/PersistPC/KrcRrtLog.xml` - controller configuration - 10 line(s) removed, 10 added - diffs/C/KRC/Roboter/Config/User/Common/PersistPC/KrcRrtLog.xml.diff
- `C/KRC/Roboter/Config/User/Common/SCTLCRC.IMG` - controller configuration - binary, 99 bytes
- `C/KRC/Roboter/Config/User/Common/SCTLCRC.XML` - controller configuration - 1 line(s) removed, 1 added - diffs/C/KRC/Roboter/Config/User/Common/SCTLCRC.XML.diff
- `C/KRC/Roboter/Config/User/Common/SCTLPARA.SAF` - controller configuration - binary, 14269 bytes
- `C/KRC/Roboter/Config/User/Common/SCtlPara.sg` - controller configuration - binary, 26574 bytes
- `C/KRC/Roboter/Config/User/Common/SafetyConfigData.xml` - controller configuration - 3 line(s) removed, 13 added - diffs/C/KRC/Roboter/Config/User/Common/SafetyConfigData.xml.diff
- `C/KRC/Roboter/Rdc/RdcDirectoryContents.txt` - controller configuration - 2 line(s) removed, 2 added - diffs/C/KRC/Roboter/Rdc/RdcDirectoryContents.txt.diff
- `C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8.asz` - controller configuration - binary, 4289308 bytes
- `C/KRC/User/Settings.xml` - controller configuration - 1 line(s) removed, 1 added - diffs/C/KRC/User/Settings.xml.diff
- `C/KRC/User/TP/SafetyDiagnostics/SpaceVisualization.xml` - controller configuration - 8 line(s) removed, 14 added - diffs/C/KRC/User/TP/SafetyDiagnostics/SpaceVisualization.xml.diff
- `KRC/R1/Mada/$machine.dat` - machine data
- `KRC/R1/Program/Centerline/centerline_home.src` - integrator program
- `KRC/R1/Program/Centerline/gun_open_check.dat` - integrator program
- `KRC/R1/Program/Centerline/gun_open_check.src` - integrator program
- `KRC/R1/Program/Centerline/preload.dat` - integrator program
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
- `KRC/R1/Program/Styles/style_1.src` - integrator program
- `KRC/R1/Program/Utilities/rejectge4.dat` - integrator program
- `KRC/R1/Program/Utilities/rejectge4.src` - integrator program
- `KRC/R1/System/$config.dat` - integrator program
- `KRC/R1/System/sps.sub` - integrator program
- `KRC/R1/System/tm_bib.dat` - KUKA system / vendor package
- `KRC/R1/System/tm_bib.src` - KUKA system / vendor package
- `KRC/R1/TP/AutomationCore/automationcoredata.dat` - KUKA system / vendor package
- `KRC/R1/TP/AutomationCore/automationcoreroutines.dat` - KUKA system / vendor package
- `KRC/R1/TP/GLUETECH/glue.src` - KUKA system / vendor package
- `KRC/R1/TP/GripperSpotTech/grp_func.dat` - KUKA system / vendor package
- `KRC/R1/TP/NutWeld/nutwelddata.dat` - KUKA system / vendor package
- `KRC/R1/TP/NutWeld/nutweldroutines.dat` - KUKA system / vendor package
- `KRC/R1/TP/NutWeld/nutweldroutines.src` - KUKA system / vendor package
- `Registry/LMSOFTWAREKUKA ROBOTER GMBHKUKA BOFOCX Control'sFileHandler.amr` - controller configuration - 1 line(s) removed, 1 added - diffs/Registry/LMSOFTWAREKUKA ROBOTER GMBHKUKA BOFOCX Control'sFileHandler.amr.diff
- `Registry/LMSOFTWAREKUKA Roboter GmbHPerformance.amr` - controller configuration - 14 line(s) removed, 14 added - diffs/Registry/LMSOFTWAREKUKA Roboter GmbHPerformance.amr.diff
- `am.ini` - archive metadata - 3 line(s) removed, 3 added - diffs/am.ini.diff

### Added (0)

_none_

### Missing from the backup (2)

- `KRC/R1/Program/movetopurge.dat`
- `KRC/R1/Program/movetopurge.src`

### Outside the archive layout (ignored) (2)

- `Archive.log`
- `ArchiveInfo.xml`

## Code changes

### `KRC/R1/Program/Centerline/gun_open_check.dat`

changed, integrator program: 1 code line(s) removed, 1 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/gun_open_check.dat.diff](diffs/KRC/R1/Program/Centerline/gun_open_check.dat.diff)

Attributes: -&ACCESS RVO2; -&REL 49; +&ACCESS  RV; +&REL 164

Data changes:

- nWaterFlowMin (INT): 150 -> 130

Runtime values (left out of the code diff): CL_ClampOpen: FALSE -> TRUE; nCtCycle: 102432 -> 1400196; nCtInWelder[1]: 4104 -> 63408; nCtInWelder[2]: 4008 -> 2976; nCtInWelder[3]: 3996 -> 4056; nCtNut: 3 -> 1; ... and 11 more

```diff
@@ base line 13, backup line 13 @@
     13  DECL GLOBAL INT nGunOpenWaitMs=2000
     15  DECL GLOBAL BOOL bGunAirCheck=TRUE
-    18  DECL GLOBAL INT nWaterFlowMin=150
+    18  DECL GLOBAL INT nWaterFlowMin=130
     19  DECL GLOBAL INT nWaterFlowHyst=10
     21  DECL GLOBAL BOOL bGunWaterCheck=TRUE
```

### `KRC/R1/Program/Centerline/gun_open_check.src`

changed, integrator program: 0 code line(s) removed, 4 added; 2 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/gun_open_check.src.diff](diffs/KRC/R1/Program/Centerline/gun_open_check.src.diff)

Attributes: &ACCESS RVO2 -> &ACCESS RVO4; &REL 49 -> &REL 216

```diff
@@ base line 61, backup line 61 @@
     61  ENDIF
     62  ENDIF
+    66  IF di004UseDryCycle==true then
+    67  GOTO Jump
+    68  ENDIF
     69  IF bGunWaterCheck THEN
     70  IF NOT dipw1_WaterOk THEN
@@ base line 75, backup line 79 @@
     79  ENDIF
     80  ENDIF
+    81  Jump:
     85  nWaitMs=0
     86  WHILE ((CL_GunStrokePositionLPT<nGunOpenMin) OR (CL_GunStrokePositionLPT>nGunOpenMax)) AND (nWaitMs<nGunOpenWaitMs)
```

### `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.dat`

changed, integrator program: 2 code line(s) removed, 11 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt1.dat.diff](diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt1.dat.diff)

Attributes: &ACCESS RVO1 -> &ACCESS RVP1; &REL 235 -> &REL 271

Data changes:

- XATDROP3 (E6POS) re-taught: moved 877.4 mm, rotated up to 32.7 deg
- XP5 (E6POS) re-taught: moved 603.3 mm, rotated up to 12.9 deg
- added 3 E6POS: XP4, XP6, XP8
- added 3 FDAT: FP4, FP6, FP8
- added 3 PDAT: PPDAT3, PPDAT4, PPDAT5

Runtime values (left out of the code diff): LAST_BASIS: {POINT1[] "P0                      ",POI... -> {POINT1[] "P8                      ",POI...; LAST_TP_PARAMS: {PARAMS[] "AC_CmdZones=DropOff; AC_CmdPa... -> {PARAMS[] "AC_CmdZones=DropOff; AC_CmdPa...

```diff
@@ base line 8, backup line 8 @@
      8  EXT BAS (BAS_COMMAND :IN,REAL :IN )
      9  DECL INT SUCCESS
-    17  DECL E6POS XATDROP3={X -1563.67676,Y -979.977295,Z 449.989929,A 179.143311,B 30.0803795,C -34.7621422,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    17  DECL E6POS XATDROP3={X -1657.31580,Y -120.488045,Z 300.706421,A -179.787964,B 31.6830921,C -2.07227635,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     18  DECL FDAT FAtDrop3={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     20  DECL E6POS XP2={X -1279.37976,Y -897.098,Z 616.329468,A 176.629059,B 21.7134552,C -1.31570351,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     21  DECL FDAT FP2={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     22  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    23  DECL E6POS XP5={X -1279.37976,Y -897.098,Z 616.329468,A 176.629059,B 21.7134552,C -1.31570351,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    23  DECL E6POS XP5={X -1542.15381,Y -366.608337,Z 499.976440,A -179.449371,B 34.6504440,C -2.87115669,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     24  DECL FDAT FP5={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     25  DECL PDAT PPDAT10={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
@@ base line 35, backup line 35 @@
     35  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     36  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    37  DECL E6POS XP4={X -1542.15393,Y -366.608246,Z 499.976624,A -179.449371,B 34.6504364,C -2.87115288,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    38  DECL FDAT FP4={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    39  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    40  DECL E6POS XP6={X -1634.19763,Y -42.4847107,Z 318.383850,A -179.447479,B 34.6464500,C -2.86936498,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    41  DECL FDAT FP6={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    42  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    43  DECL E6POS XP8={X -1428.15417,Y -316.098480,Z 1201.79382,A 177.977814,B -4.51434231,C -19.7672443,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    44  DECL FDAT FP8={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    45  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     46  ENDDAT
```

### `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src`

changed, integrator program: 6 code line(s) removed, 5 added; 40 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src.diff](diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src.diff)

Attributes: &ACCESS RVO1 -> &ACCESS RVP1; &REL 235 -> &REL 271

```diff
@@ base line 47, backup line 49 @@
     49  BAS(#CP_PARAMS,2)
     50  LIN XAtDrop3
-    56  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
+    61  GRPg_SetStateAndCheck(1, 1, 0, 1)
     65  WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2 )
-    64  do018Part1InGripper=FALSE
     69  $BWDSTART=FALSE
-    70  PDAT_ACT=PPDAT7
-    71  FDAT_ACT=FP2
+    70  PDAT_ACT=PPDAT5
+    71  FDAT_ACT=FP8
     72  BAS(#PTP_PARAMS,100)
-    73  PTP XP2 C_DIS
+    73  PTP XP8 C_DIS
     78  $BWDSTART=FALSE
     79  PDAT_ACT=PPDAT13
@@ base line 80, backup line 81 @@
     81  BAS(#PTP_PARAMS,100)
     82  PTP XP7 C_DIS
+    89  AC_DropOff (1,True)
     92  $BWDSTART=FALSE
     93  PDAT_ACT=PPDAT2
@@ base line 87, backup line 95 @@
     95  BAS(#PTP_PARAMS,100)
     96  PTP XP3 C_DIS
-    96  AC_DropOff (1,True)
    102  $BWDSTART=FALSE
    103  PDAT_ACT=PPDAT11
```

### `KRC/R1/Program/StyleDrops/Options/style1drop1opt2autorr.src`

changed, integrator program: 1 code line(s) removed, 0 added; 3 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt2autorr.src.diff](diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt2autorr.src.diff)

Attributes: &ACCESS RVO1 -> &ACCESS RVP1

```diff
@@ base line 127, backup line 127 @@
    127  BAS(#CP_PARAMS,2)
    128  LIN XP24
-   132  do018Part1InGripper=FALSE
    132  $BWDSTART=FALSE
    133  LDAT_ACT=LCPDAT7
```

### `KRC/R1/Program/StylePicks/Options/style1pick1opt1.dat`

changed, integrator program: 2 code line(s) removed, 5 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1.dat.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1.dat.diff)

Attributes: &ACCESS RVO1 -> &ACCESS RVP1; &REL 53 -> &REL 62

Data changes:

- XP30ABOVEPICK (E6POS) re-taught: moved 41.2 mm
- XP40 (E6POS) re-taught: moved 183.2 mm
- added 1 E6POS: XP13
- added 1 FDAT: FP13
- added 1 PDAT: PPDAT16

Runtime values (left out of the code diff): LAST_BASIS: {POINT1[] "P12                     ",POI... -> {POINT1[] "P13                     ",POI...

```diff
@@ base line 25, backup line 25 @@
     25  DECL E6POS XAtPick3={X 1206.28552,Y -208.912048,Z 214.640366,A -91.4409,B -0.232809022,C 0.168290094,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     26  DECL FDAT FAtPick3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    27  DECL E6POS XP40={X 1206.28552,Y -208.912048,Z 630.625366,A -91.4409,B -0.232809082,C 0.168290034,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    27  DECL E6POS XP40={X 1206.28552,Y -208.912048,Z 447.440277,A -91.4409,B -0.232809052,C 0.168290079,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     28  DECL FDAT FP40={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     29  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    30  DECL E6POS XP30ABOVEPICK={X 1206.28552,Y -208.912048,Z 298.869263,A -91.4409,B -0.232809111,C 0.168290,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    30  DECL E6POS XP30ABOVEPICK={X 1206.28552,Y -208.912048,Z 257.659698,A -91.4409,B -0.232809067,C 0.168290034,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     31  DECL FDAT FP30AbovePick={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     32  DECL E6POS XP8={X 504.083313,Y -786.363220,Z 1705.62256,A -111.705475,B 40.2604485,C 19.4570847,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
@@ base line 40, backup line 40 @@
     40  DECL FDAT FP12={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     41  DECL PDAT PPDAT15={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    42  DECL E6POS XP13={X 1057.17285,Y -292.574677,Z 818.824951,A -91.4409,B -0.232808977,C 0.168290094,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    43  DECL FDAT FP13={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    44  DECL PDAT PPDAT16={VEL 100.000,ACC 100.000,APO_DIST 101.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     45  ENDDAT
```

### `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`

changed, integrator program: 4 code line(s) removed, 3 added; 8 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1.src.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1.src.diff)

Attributes: &ACCESS RVO1 -> &ACCESS RVP1; &REL 53 -> &REL 62

```diff
@@ base line 90, backup line 90 @@
     90  IF NOT di004UseDryCycle THEN
     93  WAIT FOR ( di253PartPresent1 ) AND ( di254PartPresent2 )
-    97  do018Part1InGripper=TRUE
     95  ENDIF
     99  $BWDSTART=FALSE
@@ base line 107, backup line 103 @@
    103  LIN XP40
    108  $BWDSTART=FALSE
-   111  PDAT_ACT=PPDAT13
-   112  FDAT_ACT=FP9
+   109  PDAT_ACT=PPDAT16
+   110  FDAT_ACT=FP13
    111  BAS(#PTP_PARAMS,100)
-   114  PTP XP9
+   112  PTP XP13 C_DIS
    116  $BWDSTART=FALSE
    117  PDAT_ACT=PPDAT12
```

### `KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.src`

changed, integrator program: 1 code line(s) removed, 0 added; 3 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.src.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.src.diff)

Attributes: &ACCESS RVO2 -> &ACCESS RVP1

```diff
@@ base line 89, backup line 89 @@
     89  IF NOT di004UseDryCycle THEN
     92  WAIT FOR ( di253PartPresent1 ) AND ( di254PartPresent2 )
-    96  do018Part1InGripper=TRUE
     94  ENDIF
     98  $BWDSTART=FALSE
```

### `KRC/R1/Program/StylePicks/Options/style1pick1opt2.dat`

changed, integrator program: 1 code line(s) removed, 1 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt2.dat.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt2.dat.diff)

Attributes: &REL 43 -> &REL 44

Data changes:

- XP30ABOVEPICK (E6POS) re-taught: moved 23.9 mm, rotated up to 0.5 deg

```diff
@@ base line 29, backup line 29 @@
     29  DECL FDAT FP40={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     30  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    31  DECL E6POS XP30ABOVEPICK={X 1206.28552,Y -208.912048,Z 298.869263,A -91.4409,B -0.232809111,C 0.168290,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    31  DECL E6POS XP30ABOVEPICK={X 1207.43152,Y -211.725739,Z 322.579956,A -91.4152374,B 0.285709113,C 0.179984540,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     32  DECL FDAT FP30AbovePick={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     33  DECL E6POS XP8={X 504.083313,Y -786.363220,Z 1705.62256,A -111.705475,B 40.2604485,C 19.4570847,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
```

### `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`

changed, integrator program: 1 code line(s) removed, 0 added; 3 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt2.src.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt2.src.diff)

Attributes: &REL 43 -> &REL 44

```diff
@@ base line 83, backup line 83 @@
     83  IF NOT di004UseDryCycle THEN
     86  WAIT FOR ( di253PartPresent1 ) AND ( di254PartPresent2 )
-    90  do018Part1InGripper=TRUE
     88  ENDIF
     93  $BWDSTART=FALSE
```

### `KRC/R1/Program/Styles/style_1.src`

changed, integrator program: 7 code line(s) removed, 1 added; 4 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Styles/style_1.src.diff](diffs/KRC/R1/Program/Styles/style_1.src.diff)

```diff
@@ base line 9, backup line 9 @@
      9  BAS (#INITMOV,0 )
     23  SWITCH nOption
-    24  CASE 1
-    26  Style1Opt1 ( )
-    27  CASE 2
-    29  Style1Opt1 ( )
-    30  CASE 7
-    32  Style1Opt1 ( )
-    33  CASE 8
+    24  CASE 1,2,7,8
     26  Style1Opt1 ( )
     28  CASE 12
```

### `KRC/R1/Program/Utilities/rejectge4.dat`

changed, integrator program: 2 code line(s) removed, 2 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Utilities/rejectge4.dat.diff](diffs/KRC/R1/Program/Utilities/rejectge4.dat.diff)

Attributes: &ACCESS RVO1 -> &ACCESS RVP1; &REL 41 -> &REL 43

Data changes:

- XP23 (E6POS) re-taught: moved 70.6 mm
- added 1 DEFDAT: rejectge4
- removed 1 DEFDAT: RejectGE4

```diff
@@ base line 5, backup line 5 @@
-     5  DEFDAT RejectGE4
+     5  DEFDAT rejectge4
      8  EXT BAS (BAS_COMMAND :IN,REAL :IN )
      9  DECL INT SUCCESS
@@ base line 19, backup line 19 @@
     19  DECL PDAT PL={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     20  DECL LDAT LCPDAT0={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    21  DECL E6POS XP23={X -703.896545,Y -1395.42871,Z 344.753052,A -135.022919,B 21.6832848,C -1.44161212,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    21  DECL E6POS XP23={X -703.896423,Y -1395.42859,Z 415.333649,A -135.022903,B 21.6832867,C -1.44160593,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     22  DECL FDAT FP23={TOOL_NO 2,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     23  DECL PDAT PPDAT29={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
```

### `KRC/R1/Program/Utilities/rejectge4.src`

changed, integrator program: 1 code line(s) removed, 1 added; 4 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Utilities/rejectge4.src.diff](diffs/KRC/R1/Program/Utilities/rejectge4.src.diff)

Attributes: &ACCESS RVO1 -> &ACCESS RVP1; &REL 41 -> &REL 43

```diff
@@ base line 42, backup line 42 @@
     42  BAS(#CP_PARAMS,2)
     43  LIN XP23
-    51  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
+    51  GRPg_SetStateAndCheck(1, 1, 0.4, 1)
     55  WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2 )
     60  $BWDSTART=FALSE
```

### `KRC/R1/System/sps.sub`

changed, integrator program: 1 code line(s) removed, 6 added; 430 comment/blank line change(s). Full diff: [diffs/KRC/R1/System/sps.sub.diff](diffs/KRC/R1/System/sps.sub.diff)

```diff
@@ base line 90, backup line 88 @@
     88  BM_OUTPUTSIGNAL = BM_OUTPUTVALUE
     89  ENDIF
-    95  GRPg_ChkSetStatePLC()
     96  NutWeld_BKG ( )
     99  AutomationCore_BKG ( )
@@ base line 187, backup line 182 @@
    182  ENDIF
    185  PRELOAD()
+   189  do018Part1InGripper=FALSE
+   191  IF ((di253PartPresent1) AND (di254PartPresent2)) THEN
+   193  do018Part1InGripper=TRUE
+   195  ELSE
+   197  do018Part1InGripper=FALSE
+   199  ENDIF
    202  ENDLOOP
    205  END
```

### `C/KRC/Roboter/Config/User/Common/PNIOIM4Data.dat`

changed, controller configuration: 1 code line(s) removed, 1 added; 0 comment/blank line change(s). Full diff: [diffs/C/KRC/Roboter/Config/User/Common/PNIOIM4Data.dat.diff](diffs/C/KRC/Roboter/Config/User/Common/PNIOIM4Data.dat.diff)

```diff
@@ base line 1, backup line 1 @@
-     1  zUªòfíÒ
+     1  zUªà2çä
```

### `KRC/R1/Mada/$machine.dat`

changed, machine data: 12 code line(s) removed, 12 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Mada/$machine.dat.diff](diffs/KRC/R1/Mada/$machine.dat.diff)

```diff
@@ base line 462, backup line 462 @@
    462  $AXIS_DIR[12]=0
    463  REAL $INC_AXIS[6]
-   464  $INC_AXIS[1]=1.00000
-   465  $INC_AXIS[2]=1.00000
-   466  $INC_AXIS[3]=1.00000
-   467  $INC_AXIS[4]=1.00000
-   468  $INC_AXIS[5]=1.00000
-   469  $INC_AXIS[6]=1.00000
+   464  $INC_AXIS[1]=3.00000
+   465  $INC_AXIS[2]=3.00000
+   466  $INC_AXIS[3]=3.00000
+   467  $INC_AXIS[4]=3.00000
+   468  $INC_AXIS[5]=3.00000
+   469  $INC_AXIS[6]=3.00000
    470  REAL $INC_EXTAX[6]
    471  $INC_EXTAX[1]=10.0000
@@ base line 476, backup line 476 @@
    476  $INC_EXTAX[6]=10.0000
    477  REAL $INC_CAR[6]
-   478  $INC_CAR[1]=50.0000
-   479  $INC_CAR[2]=50.0000
-   480  $INC_CAR[3]=50.0000
-   481  $INC_CAR[4]=50.0000
-   482  $INC_CAR[5]=50.0000
-   483  $INC_CAR[6]=50.0000
+   478  $INC_CAR[1]=10.0000
+   479  $INC_CAR[2]=10.0000
+   480  $INC_CAR[3]=10.0000
+   481  $INC_CAR[4]=3.00000
+   482  $INC_CAR[5]=3.00000
+   483  $INC_CAR[6]=3.00000
    484  INT $POS_SWB[3]
    485  $POS_SWB[1]=0
```

### `KRC/R1/System/tm_bib.dat`

changed, KUKA system / vendor package: 1 code line(s) removed, 1 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/System/tm_bib.dat.diff](diffs/KRC/R1/System/tm_bib.dat.diff)

Data changes:

- iSTOP_TYPE (INT): 53 -> 0

Runtime values (left out of the code diff): TQM_ACT: {T11 200,T12 200,T13 200,T14 200,T15 200... -> {T11 200,T12 200,T13 200,T14 200,T15 200...

```diff
@@ base line 36, backup line 36 @@
     36  REAL ScalingImpact=250000.0
     37  REAL TooLarge=100000.0
-    47  DECL INT iSTOP_TYPE=53
+    47  DECL INT iSTOP_TYPE=0
     48  DECL REAL rPAR=0.0
     50  GLOBAL INT iTQM_DELAY=150
```

### `KRC/R1/TP/GLUETECH/glue.src`

changed, KUKA system / vendor package: 1 code line(s) removed, 0 added; 1 comment/blank line change(s). Full diff: [diffs/KRC/R1/TP/GLUETECH/glue.src.diff](diffs/KRC/R1/TP/GLUETECH/glue.src.diff)

```diff
@@ base line 125, backup line 125 @@
    125  ENDIF
    126  IF (((bCheckSystem[GlueActData.SystemNo]==TRUE) and ($TIMER_FLAG[iTimerSystem[GlueActData.SystemNo]]==TRUE)) OR (InputState(GlueSysDoserGenIn[GlueActData.SystemNo].PurgeRequest))) AND $IN_HOME THEN
-   127  MoveToPurge(GlueActData.SystemNo)
    128  $TIMER_STOP[iTimerSystem[GlueActData.SystemNo]]=TRUE
    129  bCheckSystem[GlueActData.SystemNo]=FALSE
```

### Runtime values only

A .dat keeps the last value the program wrote to each of its variables, and the inline-form editor keeps its suggestions (LAST_BASIS...): these files changed only in such values, nobody edited them.

| File | Values | Diff |
|---|---|---|
| `KRC/R1/System/$config.dat` | CL_GunStrokePositionLPT: 139740 -> 139725; CL_WeldFault: FALSE -> TRUE; CL_WeldPinPosition: 27321 -> 27225; NEXT_NUT_READY: TRUE -> FALSE; STEP0DONE: TRUE -> FALSE; STEP10DONE: TRUE -> FALSE; ... and 2 more | diffs/KRC/R1/System/$config.dat.diff |
| `KRC/R1/TP/AutomationCore/automationcoredata.dat` | bACMainLine: FALSE -> TRUE; nAutoCore_Handle: 10782 -> 13151; nCycleStart_Handle: 12431 -> 17050; nCycleTime: 42 -> 44; nCycTime_Handle: 12430 -> 17049; nLogOnlyMsg_Handle: 10688 -> 17042; ... and 2 more | diffs/KRC/R1/TP/AutomationCore/automationcoredata.dat.diff |
| `KRC/R1/TP/AutomationCore/automationcoreroutines.dat` | bACEntryGranted: TRUE -> FALSE | diffs/KRC/R1/TP/AutomationCore/automationcoreroutines.dat.diff |
| `KRC/R1/TP/GripperSpotTech/grp_func.dat` | GRPg_ProcessData: {ActGrp 1,ReqState 0,LastGrpNo 1,LastStN... -> {ActGrp 1,ReqState 2,LastGrpNo 1,LastStN... | diffs/KRC/R1/TP/GripperSpotTech/grp_func.dat.diff |
| `KRC/R1/TP/NutWeld/nutwelddata.dat` | rNutSensorValue[3]: 11866.0 -> 5722.00 | diffs/KRC/R1/TP/NutWeld/nutwelddata.dat.diff |
| `KRC/R1/TP/NutWeld/nutweldroutines.dat` | rLowerLVDT: 11866.0 -> 5722.00 | diffs/KRC/R1/TP/NutWeld/nutweldroutines.dat.diff |

### Comment-only changes

| File | Comment/blank line changes | Attributes | Diff |
|---|---|---|---|
| `KRC/R1/Program/Centerline/centerline_home.src` | 0 | &ACCESS RVO -> &ACCESS RVP | diffs/KRC/R1/Program/Centerline/centerline_home.src.diff |
| `KRC/R1/Program/Centerline/preload.dat` | 0 | -&ACCESS RVO2; +&ACCESS  RV; +&COMMENT 03-10-R1 PNW1 NUT PRELOAD; +&PARAM DISKPATH = Program/Centerline | diffs/KRC/R1/Program/Centerline/preload.dat.diff |
| `KRC/R1/Program/StyleDrops/Options/style1drop1opt2autorr.dat` | 0 | &ACCESS RVO1 -> &ACCESS RVP1 | diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt2autorr.dat.diff |
| `KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.dat` | 0 | &ACCESS RVO2 -> &ACCESS RVP1; &COMMENT 03-10-R1 PICK ST1 -> &COMMENT 03-10-R1 RED RABBIT PICK | diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.dat.diff |
| `KRC/R1/System/tm_bib.src` | 0 | &ACCESS R2 -> &ACCESS R1; &REL 966 -> &REL 972 | diffs/KRC/R1/System/tm_bib.src.diff |
| `KRC/R1/TP/NutWeld/nutweldroutines.src` | 0 | &ACCESS RVO3 -> &ACCESS RVO5; &REL 3482 -> &REL 3483 | diffs/KRC/R1/TP/NutWeld/nutweldroutines.src.diff |

## Mechanical checks

### FAIL (0)

_none_

### WARN (5)

- `KRC/R1/Program/Centerline/gun_open_check.src:66` [8 I/O without signal comment] di004UseDryCycle accessed with no comment naming it in the 4 lines above (C24): IF di004UseDryCycle==true then
- `KRC/R1/System/sps.sub:189` [8 I/O without signal comment] do018Part1InGripper accessed with no comment naming it in the 4 lines above (C24): do018Part1InGripper=FALSE
- `KRC/R1/System/sps.sub:191` [8 I/O without signal comment] di254PartPresent2, di253PartPresent1 accessed with no comment naming it in the 4 lines above (C24): IF ((di253PartPresent1) AND (di254PartPresent2)) THEN
- `KRC/R1/System/sps.sub:193` [8 I/O without signal comment] do018Part1InGripper accessed with no comment naming it in the 4 lines above (C24): do018Part1InGripper=TRUE
- `KRC/R1/System/sps.sub:197` [8 I/O without signal comment] do018Part1InGripper accessed with no comment naming it in the 4 lines above (C24): do018Part1InGripper=FALSE

### INFO (1)

- `KRC/R1/Program/Centerline/centerline_home.src:1` [2 format] line endings changed from LF to CRLF (the KRC reads both; git diff shows every line changed, the code diff of this report does not)
