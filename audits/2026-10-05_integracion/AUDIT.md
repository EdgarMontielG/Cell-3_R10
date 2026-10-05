# Backup audit - 658424_R10_2026-10-05_0819.zip

- Backup: `/tmp/claude-0/-home-user/50f56c92-2919-5ae3-94c9-0de4476bbe87/scratchpad/dist3/658424_R10_2026-10-05_0819.zip` (sha256 `97599631f56c22f4...`)
- am.ini: archive `e:\bmw_03_10_r1.zip\`, date `2026-10-05_09-43-37`, config `All`, robot `BMW_03_10_R1`, serial `658424`, KSS `V8.3.29`
- Compared with: `fb8a4c8` = `fb8a4c8b96` "Add findings, I/O label map and cleanup conventions for R10"; first commit (archive as received) `22a98cc8ef`
- Generated 2026-10-05T14:19:12 by tools/audit_backup.py

## Summary

| | |
|---|---|
| Entries audited (Log Files/ skipped: 8) | 308 |
| Unchanged | 262 |
| Changed | 39 |
| Added | 7 |
| Missing from the backup | 4 |
| **Deleted modules still on the controller** | 0 |
| **Pre-cleanup files** | 0 |
| Edited on top of the pre-cleanup file | 0 |
| KRL files with code changes | 27 |
| Code lines removed / added | 298 / 423 |
| KRL files with comment-only changes | 6 |
| KRL files with runtime values only (written by the program, not edits) | 1 |
| Checks FAIL / WARN / INFO | 0 / 0 / 16 |

**Needs attention:**

- WARN 4 file(s) of the base missing from the backup - deleted on the robot, or an incomplete archive (e.g. C/KRC/User/ProjectRoot/V431-03-10R1_v6Active_Centerline_18/V431-03-10R1_v6Active_Centerline_18.asz; all in Files, "Missing from the backup")
- WARN KRC/R1/Mada/$machine.dat: machine data file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- WARN KRC/R1/TP/AutomationCore/automationcoreroutines.src: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)

## The backup itself

- WARN: 4 file(s) of the base missing from the backup - deleted on the robot, or an incomplete archive (e.g. C/KRC/User/ProjectRoot/V431-03-10R1_v6Active_Centerline_18/V431-03-10R1_v6Active_Centerline_18.asz; all in Files, "Missing from the backup")
- WARN: KRC/R1/Mada/$machine.dat: machine data file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- WARN: KRC/R1/TP/AutomationCore/automationcoreroutines.src: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- INFO: KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.src: spelled KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src in the base (the controller ignores case)
- INFO: KRC/R1/System/tm_bib.dat: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- INFO: KRC/R1/TP/AutomationCore/automationcoreroutines.dat: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- INFO: KRC/R1/TP/GripperSpotTech/grp_data.dat: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- INFO: KRC/R1/TP/NutWeld/nutweldroutines.dat: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)

## Deleted modules still present

_none_

## Pre-cleanup files

_none_

## Files

### Changed (39)

- `C/KRC/Roboter/Config/User/Common/KRC_IO.xml` - controller configuration - 51 line(s) removed, 56 added - diffs/C/KRC/Roboter/Config/User/Common/KRC_IO.xml.diff
- `C/KRC/Roboter/Config/User/Common/KrcIoSignals.xml` - controller configuration - 0 line(s) removed, 16 added - diffs/C/KRC/Roboter/Config/User/Common/KrcIoSignals.xml.diff
- `C/KRC/Roboter/Rdc/RdcDirectoryContents.txt` - controller configuration - 3 line(s) removed, 3 added - diffs/C/KRC/Roboter/Rdc/RdcDirectoryContents.txt.diff
- `C/KRC/Roboter/Rdc/RobotData.xml` - controller configuration - 1 line(s) removed, 1 added - diffs/C/KRC/Roboter/Rdc/RobotData.xml.diff
- `C/KRC/User/ProjectRoot/V431-03-10R1_v6Active_Centerline_18/V431-03-10R1_v6Active_Centerline_18.wvs` - controller configuration - binary, 8982528 bytes
- `C/KRC/User/Settings.xml` - controller configuration - 1 line(s) removed, 1 added - diffs/C/KRC/User/Settings.xml.diff
- `KRC/R1/Mada/$machine.dat` - machine data
- `KRC/R1/Mada/$robcor.dat` - machine data
- `KRC/R1/Program/Centerline/CENTERLINE_HOME.src` - integrator program
- `KRC/R1/Program/Centerline/PRELOAD.src` - integrator program
- `KRC/R1/Program/Centerline/Request_next_nut.src` - integrator program
- `KRC/R1/Program/Centerline/centerline_weld.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt1.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt2.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt3.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app2opt1.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app2opt2.src` - integrator program
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.dat` - integrator program
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src` - integrator program
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src` - integrator program
- `KRC/R1/Program/Styles/style_1.src` - integrator program
- `KRC/R1/Program/Utilities/RejectGE4.src` - integrator program
- `KRC/R1/Program/Utilities/gunelectrodechange.src` - integrator program
- `KRC/R1/System/$config.dat` - integrator program
- `KRC/R1/System/sps.sub` - integrator program
- `KRC/R1/System/tm_bib.dat` - KUKA system / vendor package
- `KRC/R1/TP/AutomationCore/automationcoreroutines.dat` - KUKA system / vendor package
- `KRC/R1/TP/AutomationCore/automationcoreroutines.src` - KUKA system / vendor package
- `KRC/R1/TP/GripperSpotTech/grp_data.dat` - KUKA system / vendor package
- `KRC/R1/TP/GripperSpotTech/grp_func.dat` - KUKA system / vendor package
- `KRC/R1/TP/NutWeld/nutweldroutines.dat` - KUKA system / vendor package
- `KRC/R1/cell.src` - integrator program
- `KRC/STEU/Mada/$custom.dat` - machine data
- `Registry/LMSOFTWAREKUKA ROBOTER GMBHKUKA BOFOCX Control'sFileHandler.amr` - controller configuration - 1 line(s) removed, 1 added - diffs/Registry/LMSOFTWAREKUKA ROBOTER GMBHKUKA BOFOCX Control'sFileHandler.amr.diff
- `Registry/LMSOFTWAREKUKA ROBOTER GMBHWorkVisual.amr` - controller configuration - 5 line(s) removed, 7 added - diffs/Registry/LMSOFTWAREKUKA ROBOTER GMBHWorkVisual.amr.diff
- `am.ini` - archive metadata - 4 line(s) removed, 4 added - diffs/am.ini.diff

### Added (7)

- `C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8.log` - controller configuration - 0 line(s) removed, 342 added - diffs/C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8.log.diff
- `C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8.wvs` - controller configuration - binary, 5529600 bytes
- `C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8_old.log` - controller configuration - 0 line(s) removed, 372 added - diffs/C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8_old.log.diff
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src` - integrator program
- `KRC/R1/Program/Centerline/gun_open_check.dat` - integrator program
- `KRC/R1/Program/Styles/Options/Style1Opt10AutoRR.src` - integrator program
- `KRC/R1/Program/Styles/Options/style1opt1.src` - integrator program

### Missing from the backup (4)

- `C/KRC/User/ProjectRoot/V431-03-10R1_v6Active_Centerline_18/V431-03-10R1_v6Active_Centerline_18.asz`
- `KRC/R1/Program/Centerline/centerline_loop.src`
- `KRC/R1/Program/Styles/optiones/Style1Opt10AutoRR.src`
- `KRC/R1/Program/Styles/optiones/style1opt1.src`

### Outside the archive layout (ignored) (0)

_none_

## Code changes

### `KRC/R1/Program/Centerline/CENTERLINE_HOME.src`

changed, integrator program: 18 code line(s) removed, 18 added; 19 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/CENTERLINE_HOME.src.diff](diffs/KRC/R1/Program/Centerline/CENTERLINE_HOME.src.diff)

```diff
@@ base line 6, backup line 6 @@
      6  DEF CENTERLINE_HOME()
-    28  CL_GunPressureCmd=405
-    34  $OUT[473]=FALSE
-    35  $OUT[475]=FALSE
-    36  $OUT[476]=FALSE
-    37  $OUT[494]=FALSE
-    38  $OUT[500]=FALSE
-    39  $OUT[505]=FALSE
-    43  $OUT[495]=FALSE
+    28  CL_GunPressureCmd=CL_GUN_PRESS_BASE
+    33  dopw1_Nut1Intensify_Home=FALSE
+    34  dopw1_StartWater=FALSE
+    35  dopw1_StartFeed=FALSE
+    38  dopw1_BlowOff=FALSE
+    39  do500Reserved=FALSE
+    40  do505QFPNutBlowOff=FALSE
+    44  dopw1_AdvancePin=FALSE
     45  WAIT SEC 0.2
-    45  $OUT[496]=TRUE
+    46  dopw1_ReturnPin=TRUE
     47  WAIT SEC 1.0
-    50  $OUT[503]=FALSE
+    51  do503QFPAdvance=FALSE
     52  WAIT SEC 0.2
-    52  $OUT[504]=TRUE
-    54  WAIT FOR $IN[482]
+    53  do504QFPReturn=TRUE
+    55  WAIT FOR dipw1_SpearHome
     56  WAIT SEC 0.5
-    59  $OUT[498]=FALSE
+    60  do498UpperPinExtend=FALSE
     61  WAIT SEC 0.2
-    61  $OUT[499]=TRUE
+    62  do499UpperPinRetract=TRUE
     63  WAIT SEC 1.0
-    66  $OUT[472]=FALSE
+    67  dopw1_GunWork=FALSE
     68  WAIT SEC 0.2
-    68  $OUT[471]=TRUE
+    69  dopw1_GunHome=TRUE
     70  WAIT SEC 1.5
-    73  $OUT[501]=FALSE
+    74  do501PartClampClose=FALSE
     75  WAIT SEC 0.2
-    75  $OUT[502]=TRUE
+    76  do502PartClampOpen=TRUE
     77  WAIT SEC 1.0
     79  END
```

### `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src`

added, integrator program: 0 code line(s) removed, 91 added; 47 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src.diff](diffs/KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src.diff)

Attributes: +&ACCESS RVO1; +&REL 2; +&COMMENT 03-10-R1 PNW1 GUN OPEN CHECK; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\Roboter\Template\vorgabe

```diff
@@ base line end, backup line 6 @@
+     6  DEF GUN_OPEN_CHECK( )
+    22  DECL KrlMsg_T Msg
+    23  DECL KrlMsg_T MsgW
+    24  DECL KrlMsgPar_T Par[3]
+    25  DECL KrlMsgOpt_T Opt
+    26  DECL INT nHandle, nWaitMs
+    27  DECL BOOL bRes
+    30  WAIT SEC 0
+    33  Msg.Modul[]="GunOpenCheck"
+    34  MsgW.Modul[]="GunOpenCheck"
+    35  Par[1].Par_Type=#EMPTY
+    36  Par[2].Par_Type=#EMPTY
+    37  Par[3].Par_Type=#EMPTY
+    38  Opt.VL_Stop=TRUE
+    39  Opt.Clear_P_Reset=TRUE
+    40  Opt.Clear_P_SAW=FALSE
+    41  Opt.Log_To_DB=TRUE
+    45  IF $PRO_STATE0<>#P_ACTIVE THEN
+    46  Msg.Nr=1
+    47  Msg.Msg_txt[]="Submit (SPS) not running - gun position not valid - robot waiting"
+    48  Par[1].Par_Type=#EMPTY
+    49  nHandle=Set_KrlMsg(#STATE, Msg, Par[], Opt)
+    50  WAIT FOR $PRO_STATE0==#P_ACTIVE
+    51  bRes=Clear_KrlMsg(nHandle)
+    53  WAIT SEC 0.5
+    54  ENDIF
+    57  IF bGunAirCheck THEN
+    59  IF NOT dipw1_AirOK THEN
+    60  Msg.Nr=3
+    61  Msg.Msg_txt[]="Nut welder air pressure not OK (dipw1_AirOK) - robot waiting"
+    62  Par[1].Par_Type=#EMPTY
+    63  nHandle=Set_KrlMsg(#STATE, Msg, Par[], Opt)
+    65  WAIT FOR dipw1_AirOK
+    66  bRes=Clear_KrlMsg(nHandle)
+    67  ENDIF
+    68  ENDIF
+    71  IF bGunWaterCheck THEN
+    72  IF NOT dipw1_WaterOk THEN
+    73  MsgW.Nr=6
+    74  MsgW.Msg_txt[]="Nut welder cooling water flow too low (%1 x0.1 l/min) - robot waiting"
+    75  Par[1].Par_Type=#VALUE
+    76  Par[1].Par_Int=nWaterFlow
+    77  nHandle=Set_KrlMsg(#STATE, MsgW, Par[], Opt)
+    78  WAIT FOR dipw1_WaterOk
+    79  bRes=Clear_KrlMsg(nHandle)
+    80  Par[1].Par_Type=#EMPTY
+    81  ENDIF
+    82  ENDIF
+    85  nWaitMs=0
+    86  WHILE ((CL_GunStrokePositionLPT<nGunOpenMin) OR (CL_GunStrokePositionLPT>nGunOpenMax)) AND (nWaitMs<nGunOpenWaitMs)
+    87  WAIT SEC 0.05
+    88  nWaitMs=nWaitMs+50
+    89  ENDWHILE
+    92  IF (CL_GunStrokePositionLPT<nGunOpenMin) OR (CL_GunStrokePositionLPT>nGunOpenMax) THEN
+    93  Msg.Nr=2
+    94  Msg.Msg_txt[]="Nut welder gun not open (position %1) - robot waiting"
+    95  Par[1].Par_Type=#VALUE
+    96  Par[1].Par_Int=CL_GunStrokePositionLPT
+    97  nHandle=Set_KrlMsg(#STATE, Msg, Par[], Opt)
```
_32 more lines: see diffs/KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src.diff_

### `KRC/R1/Program/Centerline/PRELOAD.src`

changed, integrator program: 30 code line(s) removed, 30 added; 228 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/PRELOAD.src.diff](diffs/KRC/R1/Program/Centerline/PRELOAD.src.diff)

```diff
@@ base line 3, backup line 3 @@
      3  DEF PRELOAD ( )
-    33  IF NUT_STAR AND NOT NUTCYCLE_ACTIVE THEN
-    35  NUT_STAR=FALSE
+    33  IF NUT_START AND NOT NUTCYCLE_ACTIVE THEN
+    35  NUT_START=FALSE
     36  NUTCYCLE_ACTIVE=TRUE
     37  NUT_READY=FALSE
@@ base line 57, backup line 57 @@
     57  SWITCH NUT_PRELOAD_STEP
     59  CASE 0
-    63  $OUT[503]=FALSE
-    64  $OUT[504]=TRUE
-    68  IF ($IN[482]==TRUE) AND ($IN[470]==FALSE) THEN
-    71  $OUT[476]=TRUE
-    72  $OUT[494]=FALSE
+    63  do503QFPAdvance=FALSE
+    64  do504QFPReturn=TRUE
+    68  IF (dipw1_SpearHome==TRUE) AND (di470QFPAdvanced==FALSE) THEN
+    71  dopw1_StartFeed=TRUE
+    72  dopw1_BlowOff=FALSE
     75  IF $TIMER_STOP[10] THEN
     76  $TIMER[10]=0
@@ base line 93, backup line 93 @@
     93  CASE 10
     96  IF STEP0DONE THEN
-   100  $OUT[472]=FALSE
-   101  $OUT[471]=TRUE
-   104  $OUT[498]=FALSE
-   105  $OUT[499]=TRUE
-   108  $OUT[501]=FALSE
-   109  $OUT[502]=TRUE
+   100  dopw1_GunWork=FALSE
+   101  dopw1_GunHome=TRUE
+   104  do498UpperPinExtend=FALSE
+   105  do499UpperPinRetract=TRUE
+   108  do501PartClampClose=FALSE
+   109  do502PartClampOpen=TRUE
    112  IF NOT STEP10_ADV_STARTED THEN
-   114  $OUT[494]=TRUE
-   116  $OUT[503]=FALSE
-   117  $OUT[504]=TRUE
-   121  IF ($IN[482]==TRUE) AND ($IN[470]==FALSE) THEN
+   114  dopw1_BlowOff=TRUE
+   116  do503QFPAdvance=FALSE
+   117  do504QFPReturn=TRUE
+   121  IF (dipw1_SpearHome==TRUE) AND (di470QFPAdvanced==FALSE) THEN
    122  STEP10_ADV_STARTED=TRUE
    124  ENDIF
    125  ELSE
-   129  $OUT[504]=FALSE
-   130  $OUT[503]=TRUE
-   131  $OUT[476]=FALSE
-   135  IF ($IN[470]==TRUE) AND ($IN[482]==FALSE) THEN
-   137  $OUT[505]=TRUE
-   138  $OUT[494]=FALSE
+   129  do504QFPReturn=FALSE
+   130  do503QFPAdvance=TRUE
+   131  dopw1_StartFeed=FALSE
+   135  IF (di470QFPAdvanced==TRUE) AND (dipw1_SpearHome==FALSE) THEN
```
_27 more lines: see diffs/KRC/R1/Program/Centerline/PRELOAD.src.diff_

### `KRC/R1/Program/Centerline/Request_next_nut.src`

changed, integrator program: 2 code line(s) removed, 2 added; 4 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/Request_next_nut.src.diff](diffs/KRC/R1/Program/Centerline/Request_next_nut.src.diff)

```diff
@@ base line 3, backup line 3 @@
      3  DEF Request_next_nut ( )
-    20  NEXT_NUT_READY=false
+    20  NEXT_NUT_READY=FALSE
     21  NEXT_NUT_REQUEST=TRUE
-    22  NUT_STAR=TRUE
+    22  NUT_START=TRUE
     24  END
```

### `KRC/R1/Program/Centerline/centerline_weld.src`

changed, integrator program: 73 code line(s) removed, 65 added; 191 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/centerline_weld.src.diff](diffs/KRC/R1/Program/Centerline/centerline_weld.src.diff)

```diff
@@ base line 5, backup line 5 @@
      5  DEF CENTERLINE_WELD()
-    56  $OUT[472]=FALSE
-    57  $OUT[471]=TRUE
-    62  $OUT[498]=FALSE
-    63  $OUT[499]=TRUE
-    67  $OUT[501]=FALSE
-    68  $OUT[502]=TRUE
-    70  WAIT FOR $IN[466]
-    73  $OUT[496]=FALSE
-    74  $OUT[495]=TRUE
-    77  $OUT[503]=FALSE
-    78  $OUT[504]=TRUE
-    80  WAIT FOR $IN[482]
-    83  IF NUT_READY THEN
-    84  GOTO NUT_READY
-    85  ENDIF
-    92  $OUT[496]=FALSE
-    93  $OUT[495]=TRUE
-    94  $OUT[494]=TRUE
-    97  $OUT[504]=FALSE
-    98  $OUT[503]=TRUE
-   100  WAIT FOR $IN[470]
+    58  dopw1_GunWork=FALSE
+    59  dopw1_GunHome=TRUE
+    63  do498UpperPinExtend=FALSE
+    64  do499UpperPinRetract=TRUE
+    67  do501PartClampClose=FALSE
+    68  do502PartClampOpen=TRUE
+    70  WAIT FOR di466PartClampOpen
+    73  dopw1_ReturnPin=FALSE
+    74  dopw1_AdvancePin=TRUE
+    77  do503QFPAdvance=FALSE
+    78  do504QFPReturn=TRUE
+    80  WAIT FOR dipw1_SpearHome
+    84  IF NOT NUT_READY THEN
+    87  dopw1_ReturnPin=FALSE
+    88  dopw1_AdvancePin=TRUE
+    89  dopw1_BlowOff=TRUE
+    92  do504QFPReturn=FALSE
+    93  do503QFPAdvance=TRUE
+    95  WAIT FOR di470QFPAdvanced
    100  dopw1_StartFeed=TRUE
    101  dopw1_StartFeed=FALSE
    102  WAIT SEC 1.5
-   109  $OUT[494]=FALSE
-   112  $OUT[503]=FALSE
-   113  $OUT[504]=TRUE
-   115  WAIT FOR $IN[482]
-   119  $OUT[499]=FALSE
-   120  $OUT[498]=TRUE
-   124  NUT_READY:
-   129  $OUT[499]=FALSE
-   130  $OUT[498]=TRUE
-   133  CL_GunPressureCmd=405
+   104  dopw1_BlowOff=FALSE
+   107  do503QFPAdvance=FALSE
+   108  do504QFPReturn=TRUE
+   110  WAIT FOR dipw1_SpearHome
+   111  ENDIF
```
_132 more lines: see diffs/KRC/R1/Program/Centerline/centerline_weld.src.diff_

### `KRC/R1/Program/Centerline/gun_open_check.dat`

added, integrator program: 0 code line(s) removed, 10 added; 14 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/gun_open_check.dat.diff](diffs/KRC/R1/Program/Centerline/gun_open_check.dat.diff)

Attributes: +&ACCESS  RV; +&COMMENT 03-10-R1 PNW1 GUN OPEN CHECK; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\Roboter\Template\vorgabe; +&REL 2

Data changes:

- added 2 BOOL: bGunAirCheck, bGunWaterCheck
- added 1 DEFDAT: GUN_OPEN_CHECK
- added 6 INT: nGunOpenMax, nGunOpenMin, nGunOpenWaitMs, nWaterFlow, nWaterFlowHyst, nWaterFlowMin

```diff
@@ base line end, backup line 6 @@
+     6  DEFDAT GUN_OPEN_CHECK PUBLIC
+    12  DECL GLOBAL INT nGunOpenMin=137000
+    13  DECL GLOBAL INT nGunOpenMax=142000
+    15  DECL INT nGunOpenWaitMs=2000
+    18  DECL BOOL bGunAirCheck=FALSE
+    22  DECL GLOBAL INT nWaterFlow=226
+    23  DECL GLOBAL INT nWaterFlowMin=150
+    24  DECL GLOBAL INT nWaterFlowHyst=10
+    26  DECL BOOL bGunWaterCheck=TRUE
+    28  ENDDAT
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`

changed, integrator program: 10 code line(s) removed, 20 added; 43 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1.src.diff)

```diff
@@ base line 47, backup line 47 @@
     47  BAS(#CP_PARAMS,2)
     48  LIN XP8 C_DIS C_DIS
-    51  RETRY_NUT1:
+    55  INTERRUPT DECL 20 WHEN CL_GunStrokePositionLPT<137000 DO GUN_OPEN_LOST()
+    56  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
+    57  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
     62  WAIT FOR NUT_READY== TRUE
+    65  GUN_OPEN_CHECK()
+    66  INTERRUPT ON 20
+    67  INTERRUPT ON 21
+    68  INTERRUPT ON 22
     72  $BWDSTART=FALSE
     73  LDAT_ACT=LCPDAT8
@@ base line 63, backup line 75 @@
     75  BAS(#CP_PARAMS,2)
     76  LIN XP20 C_DIS C_DIS
-    68  IF di004UseDryCycle==TRUE THEN
-    70  GOTO DRY1
-    71  ELSE
+    82  IF NOT di004UseDryCycle THEN
     84  $BWDSTART=FALSE
     85  LDAT_ACT=LCPDAT18
@@ base line 77, backup line 87 @@
     87  BAS(#CP_PARAMS,2)
     88  LIN XP19
+    92  WAIT SEC 0
+    93  INTERRUPT OFF 20
+    94  INTERRUPT OFF 21
+    95  INTERRUPT OFF 22
     97  CENTERLINE_WELD()
+    99  INTERRUPT ON 20
+   100  INTERRUPT ON 21
+   101  INTERRUPT ON 22
    102  ENDIF
-    84  DRY1:
    106  $BWDSTART=FALSE
    107  LDAT_ACT=LCPDAT16
@@ base line 91, backup line 109 @@
    109  BAS(#CP_PARAMS,2)
    110  LIN XP20 C_DIS C_DIS
-    97  IF NUT_WELD_RETRY THEN
-    98  NUT_WELD_RETRY=FALSE
-   100  GOTO RETRY_NUT1
-   101  ENDIF
+   114  WAIT SEC 0
+   115  INTERRUPT OFF 20
+   116  INTERRUPT OFF 21
+   117  INTERRUPT OFF 22
    120  $BWDSTART=FALSE
    121  LDAT_ACT=LCPDAT17
@@ base line 107, backup line 123 @@
    123  BAS(#CP_PARAMS,2)
    124  LIN XP8 C_DIS C_DIS
+   131  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO Request_next_nut() PRIO= -1
    133  $BWDSTART=FALSE
    134  PDAT_ACT=PPDAT18
    135  FDAT_ACT=FP0
    136  BAS(#PTP_PARAMS,100)
-   119  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO Request_next_nut() PRIO= -1
```
_2 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`

changed, integrator program: 10 code line(s) removed, 20 added; 41 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2.src.diff)

```diff
@@ base line 46, backup line 46 @@
     46  BAS(#CP_PARAMS,2)
     47  LIN XP5
-    50  RETRY_NUT1:
+    54  INTERRUPT DECL 20 WHEN CL_GunStrokePositionLPT<137000 DO GUN_OPEN_LOST()
+    55  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
+    56  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
     59  WAIT FOR NEXT_NUT_READY==TRUE
+    62  GUN_OPEN_CHECK()
+    63  INTERRUPT ON 20
+    64  INTERRUPT ON 21
+    65  INTERRUPT ON 22
     68  $BWDSTART=FALSE
     69  LDAT_ACT=LCPDAT0
@@ base line 59, backup line 71 @@
     71  BAS(#CP_PARAMS,2)
     72  LIN XP6
-    64  IF di004UseDryCycle==TRUE THEN
-    66  GOTO DRY1
-    67  ELSE
+    78  IF NOT di004UseDryCycle THEN
     80  $BWDSTART=FALSE
     81  LDAT_ACT=LCPDAT15
@@ base line 73, backup line 83 @@
     83  BAS(#CP_PARAMS,2)
     84  LIN XP16
+    88  WAIT SEC 0
+    89  INTERRUPT OFF 20
+    90  INTERRUPT OFF 21
+    91  INTERRUPT OFF 22
     93  CENTERLINE_WELD()
+    95  INTERRUPT ON 20
+    96  INTERRUPT ON 21
+    97  INTERRUPT ON 22
     98  ENDIF
-    82  DRY1:
    101  $BWDSTART=FALSE
    102  LDAT_ACT=LCPDAT6
@@ base line 88, backup line 104 @@
    104  BAS(#CP_PARAMS,2)
    105  LIN XP06 C_DIS C_DIS
-    92  IF NUT_WELD_RETRY THEN
-    93  NUT_WELD_RETRY=FALSE
-    95  GOTO RETRY_NUT1
-    96  ENDIF
+   109  WAIT SEC 0
+   110  INTERRUPT OFF 20
+   111  INTERRUPT OFF 21
+   112  INTERRUPT OFF 22
    114  $BWDSTART=FALSE
    115  LDAT_ACT=LCPDAT14
@@ base line 101, backup line 117 @@
    117  BAS(#CP_PARAMS,2)
    118  LIN XP05
+   125  TRIGGER WHEN DISTANCE = 1 DELAY = 0 DO Request_next_nut() PRIO= -1
    127  $BWDSTART=FALSE
    128  PDAT_ACT=PPDAT26
    129  FDAT_ACT=FP0
    130  BAS(#PTP_PARAMS,100)
-   113  TRIGGER WHEN DISTANCE = 1 DELAY = 0 DO Request_next_nut() PRIO= -1
```
_2 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt3.src`

changed, integrator program: 9 code line(s) removed, 19 added; 30 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3.src.diff)

```diff
@@ base line 40, backup line 40 @@
     40  BAS(#CP_PARAMS,2)
     41  LIN XP20 C_DIS C_DIS
-    44  RETRY_NUT1:
+    48  INTERRUPT DECL 20 WHEN CL_GunStrokePositionLPT<137000 DO GUN_OPEN_LOST()
+    49  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
+    50  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
     53  WAIT FOR NEXT_NUT_READY==TRUE
+    56  GUN_OPEN_CHECK()
+    57  INTERRUPT ON 20
+    58  INTERRUPT ON 21
+    59  INTERRUPT ON 22
     62  $BWDSTART=FALSE
     63  LDAT_ACT=LCPDAT4
@@ base line 53, backup line 65 @@
     65  BAS(#CP_PARAMS,2)
     66  LIN XP13 C_DIS C_DIS
-    58  IF di004UseDryCycle==TRUE THEN
-    60  GOTO DRY1
-    61  ELSE
+    72  IF NOT di004UseDryCycle THEN
     74  $BWDSTART=FALSE
     75  LDAT_ACT=LCPDAT11
@@ base line 67, backup line 77 @@
     77  BAS(#CP_PARAMS,2)
     78  LIN XP16
+    82  WAIT SEC 0
+    83  INTERRUPT OFF 20
+    84  INTERRUPT OFF 21
+    85  INTERRUPT OFF 22
     87  CENTERLINE_WELD()
+    89  INTERRUPT ON 20
+    90  INTERRUPT ON 21
+    91  INTERRUPT ON 22
     92  ENDIF
-    74  DRY1:
     95  $BWDSTART=FALSE
     96  LDAT_ACT=LCPDAT12
@@ base line 80, backup line 98 @@
     98  BAS(#CP_PARAMS,2)
     99  LIN XP17
-    84  IF NUT_WELD_RETRY THEN
-    85  NUT_WELD_RETRY=FALSE
-    87  GOTO RETRY_NUT1
-    88  ENDIF
+   103  WAIT SEC 0
+   104  INTERRUPT OFF 20
+   105  INTERRUPT OFF 21
+   106  INTERRUPT OFF 22
    108  $BWDSTART=FALSE
    109  LDAT_ACT=LCPDAT10
```

### `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`

changed, integrator program: 30 code line(s) removed, 12 added; 65 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.src.diff)

```diff
@@ base line 58, backup line 57 @@
     57  BAS(#CP_PARAMS,2)
     58  LIN XP28
-    67  IF di004UseDryCycle==TRUE THEN
-    69  GOTO DRY1
-    70  ELSE
-    71  IF ($IN[227]==TRUE) THEN
-    72  PARTPRESENT1=TRUE
+    64  IF NOT di004UseDryCycle THEN
+    65  WAIT SEC 0.2
+    67  PARTPRESENT1=di227NutPresent1
     68  ENDIF
-    74  WAIT SEC 0.2
-    76  ENDIF
-    78  DRY1:
     71  $BWDSTART=FALSE
     72  PDAT_ACT=PPDAT35
@@ base line 93, backup line 83 @@
     83  BAS(#CP_PARAMS,2)
     84  LIN XP32
-   102  IF di004UseDryCycle==TRUE THEN
-   104  GOTO DRY2
-   105  ELSE
-   106  IF ($IN[227]==TRUE) THEN
-   107  PARTPRESENT2=TRUE
+    90  IF NOT di004UseDryCycle THEN
+    91  WAIT SEC 0.2
+    93  PARTPRESENT2=di227NutPresent1
     94  ENDIF
-   109  WAIT SEC 0.2
-   111  ENDIF
-   113  DRY2:
     97  $BWDSTART=FALSE
     98  PDAT_ACT=PPDAT36
@@ base line 128, backup line 109 @@
    109  BAS(#CP_PARAMS,2)
    110  LIN XP36
-   137  IF di004UseDryCycle==TRUE THEN
-   139  GOTO DRY3
-   140  ELSE
-   141  IF ($IN[227]==TRUE) THEN
-   142  PARTPRESENT3=TRUE
+   116  IF NOT di004UseDryCycle THEN
+   117  WAIT SEC 0.2
+   119  PARTPRESENT3=di227NutPresent1
    120  ENDIF
-   144  WAIT SEC 0.2
-   146  ENDIF
-   148  DRY3:
    123  $BWDSTART=FALSE
    124  PDAT_ACT=PPDAT37
@@ base line 154, backup line 126 @@
    126  BAS(#PTP_PARAMS,100)
    127  PTP XP37
-   163  IF di004UseDryCycle==TRUE THEN
-   165  GOTO DRY6
-   166  ELSE
+   137  IF NOT di004UseDryCycle THEN
    138  WAIT SEC 0.2
    139  SWITCH nOption
```
_16 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`

changed, integrator program: 3 code line(s) removed, 12 added; 19 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.src.diff)

```diff
@@ base line 53, backup line 53 @@
     53  WAIT FOR di080ToolRepositioned1
     60  WAIT SEC 0.2
-    60  IF (di100CameraJudmentOK==TRUE) AND (di101CameraJudmentNG==FALSE)THEN
+    61  SWITCH nOption
+    62  CASE 1,2,7,8
+    64  IF (di100CameraJudgmentOK==TRUE) AND (di101CameraJudgmentNG==FALSE) THEN
     65  bscrapGE4 = FALSE
-    63  ENDIF
-    64  IF (di100CameraJudmentOK==FALSE) AND (di101CameraJudmentNG==TRUE)THEN
+    66  ELSE
     67  bscrapGE4 = TRUE
     68  ENDIF
+    69  CASE 12
+    72  IF (di100CameraJudgmentOK==TRUE) AND (di101CameraJudgmentNG==FALSE) THEN
+    73  do141RedRabbitFailed=TRUE
+    74  ENDIF
+    77  IF (di100CameraJudgmentOK==FALSE) AND (di101CameraJudgmentNG==TRUE) THEN
+    78  do142RedRabbitPassed=TRUE
+    79  ENDIF
+    80  ENDSWITCH
     91  AC_Application (1,True)
     93  END
```

### `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.dat`

changed, integrator program: 1 code line(s) removed, 1 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt1.dat.diff](diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt1.dat.diff)

Data changes:

- XATDROP3 (E6POS) re-taught: moved 34.8 mm, rotated up to 34.5 deg

```diff
@@ base line 9, backup line 9 @@
      9  DECL INT SUCCESS
     16  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P10                     ",POINT2[] "P10                     ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT6                   ",CONT[] "                        ",CP_VEL[] "2      [...]
-    17  DECL E6POS XATDROP3={X -1587.76917,Y -890.400757,Z 439.605072,A 177.082932,B 4.31955290,C -0.298484027,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    17  DECL E6POS XATDROP3={X -1563.67676,Y -913.306702,Z 449.989929,A 179.143311,B 30.0803795,C -34.7621422,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     18  DECL FDAT FAtDrop3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     19  DECL MODULEPARAM_T LAST_TP_PARAMS={PARAMS[] "AC_CmdZones=DropOff; AC_CmdParam=2; AC_ZoneRepo=True; AC_UseState=True; AC_Blending=False                               "}
```

### `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src`

changed, integrator program: 1 code line(s) removed, 0 added; 11 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src.diff](diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src.diff)

```diff
@@ base line 58, backup line 58 @@
     58  LIN XAtDrop3
     68  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
-    76  GRPg_Check(1, 1, FALSE, 1)
     72  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254] )
     76  $OUT[18]=FALSE
```

### `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`

changed, integrator program: 8 code line(s) removed, 3 added; 46 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1.src.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1.src.diff)

```diff
@@ base line 11, backup line 11 @@
     11  BAS (#INITMOV,0 )
     32  AC_pickUPCheck (1)
+    37  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254])
     46  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
-    51  GRPg_Check(1, 1, FALSE, 1)
-    55  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254])
+    57  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO NUT_START=TRUE
     59  $BWDSTART=FALSE
     60  PDAT_ACT=PPDAT15
     61  FDAT_ACT=FP12
     62  BAS(#PTP_PARAMS,100)
-    69  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO NUT_STAR=TRUE
     63  PTP XP12
     66  $BWDSTART=FALSE
@@ base line 99, backup line 92 @@
     92  LIN XAtPick3
    102  GRPg_SetStateAndCheck(1, 2, 0.2, 1)
-   118  GRPg_Check(1, 2, FALSE, 1)
-   123  IF di004UseDryCycle==TRUE THEN
-   125  GOTO DRY
-   126  ELSE
+   108  IF NOT di004UseDryCycle THEN
    111  WAIT FOR ( $IN[253] ) AND ( $IN[254] )
    117  $OUT[18]=TRUE
    119  ENDIF
-   139  DRY:
    123  $BWDSTART=FALSE
    124  LDAT_ACT=LCPDAT2
```

### `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`

changed, integrator program: 8 code line(s) removed, 3 added; 48 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src.diff)

```diff
@@ base line 11, backup line 11 @@
     11  BAS (#INITMOV,0 )
     33  AC_pickUPCheck (1)
+    38  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254])
     47  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
-    52  GRPg_Check(1, 1, FALSE, 1)
-    56  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254])
+    58  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO NUT_START=TRUE
     60  $BWDSTART=FALSE
     61  PDAT_ACT=PPDAT15
     62  FDAT_ACT=FP12
     63  BAS(#PTP_PARAMS,100)
-    70  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO NUT_STAR=TRUE
     64  PTP XP12
     67  $BWDSTART=FALSE
@@ base line 100, backup line 93 @@
     93  LIN XAtPick3
    103  GRPg_SetStateAndCheck(1, 2, 0.2, 1)
-   119  GRPg_Check(1, 2, FALSE, 1)
-   124  IF di004UseDryCycle==TRUE THEN
-   126  GOTO DRY
-   127  ELSE
+   109  IF NOT di004UseDryCycle THEN
    112  WAIT FOR ( $IN[253] ) AND ( $IN[254] )
    118  $OUT[18]=TRUE
    120  ENDIF
-   140  DRY:
    124  $BWDSTART=FALSE
    125  LDAT_ACT=LCPDAT2
```

### `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`

changed, integrator program: 8 code line(s) removed, 3 added; 46 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt2.src.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt2.src.diff)

```diff
@@ base line 11, backup line 11 @@
     11  BAS (#INITMOV,0 )
     34  AC_pickUPCheck (2)
+    39  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254])
     48  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
-    53  GRPg_Check(1, 1, FALSE, 1)
-    57  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254])
+    59  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO NUT_START=TRUE
     61  $BWDSTART=FALSE
     62  PDAT_ACT=PPDAT1
     63  FDAT_ACT=FP10
     64  BAS(#PTP_PARAMS,100)
-    71  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO NUT_STAR=TRUE
     65  PTP XP10 C_DIS
     68  $BWDSTART=FALSE
@@ base line 94, backup line 87 @@
     87  LIN XAtPick3
     97  GRPg_SetStateAndCheck(1, 2, 0.2, 1)
-   113  GRPg_Check(1, 2, FALSE, 1)
-   118  IF di004UseDryCycle==TRUE THEN
-   120  GOTO DRY
-   121  ELSE
+   103  IF NOT di004UseDryCycle THEN
    106  WAIT FOR ( $IN[253] ) AND ( $IN[254] )
    112  $OUT[18]=TRUE
    114  ENDIF
-   134  DRY:
    119  $BWDSTART=FALSE
    120  LDAT_ACT=LCPDAT2
```

### `KRC/R1/Program/Styles/Options/Style1Opt10AutoRR.src`

added, integrator program: 0 code line(s) removed, 6 added; 18 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Styles/Options/Style1Opt10AutoRR.src.diff](diffs/KRC/R1/Program/Styles/Options/Style1Opt10AutoRR.src.diff)

Attributes: +&ACCESS RVO1; +&REL 3; +&COMMENT 03-10-R1 RED RABBIT CYCLE

```diff
@@ base line end, backup line 4 @@
+     4  DEF Style1Opt10AutoRR( )
+    17  Style1Pick1Opt1AutoRR()
+    19  style1app2opt1()
+    22  style1app2opt2()
+    25  style1drop1opt2AutoRR()
+    27  END
```

### `KRC/R1/Program/Styles/Options/style1opt1.src`

added, integrator program: 0 code line(s) removed, 35 added; 32 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Styles/Options/style1opt1.src.diff](diffs/KRC/R1/Program/Styles/Options/style1opt1.src.diff)

Attributes: +&ACCESS RVO1; +&REL 40; +&COMMENT 03-10-R1 PRODUCTION CYCLE

```diff
@@ base line end, backup line 4 @@
+     4  DEF Style1Opt1 ( )
+    11  DECL INT nPickStation
+    20  nPickStation=0
+    22  IF di065PickupMachine1 AND NOT di066PickupMachine2 THEN
+    23  nPickStation=1
+    24  ELSE
+    26  IF di066PickupMachine2 AND NOT di065PickupMachine1 THEN
+    27  nPickStation=2
+    28  ENDIF
+    29  ENDIF
+    31  IF nPickStation<>0 THEN
+    33  IF nPickStation==1 THEN
+    34  style1pick1opt1()
+    35  ELSE
+    36  style1pick1opt2()
+    37  ENDIF
+    39  style1app1opt1()
+    41  Style1App1Opt2()
+    43  Style1App1Opt3()
+    46  style1app2opt1()
+    47  IF bScrapGE4==TRUE THEN
+    50  RejectGE4()
+    51  ELSE
+    54  style1app2opt2()
+    55  IF bScrapGE4==TRUE THEN
+    57  RejectGE4()
+    58  ELSE
+    60  Style1Drop1Opt1()
+    61  ENDIF
+    62  ENDIF
+    63  ENDIF
+    66  PARTPRESENT1=FALSE
+    67  PARTPRESENT2=FALSE
+    68  PARTPRESENT3=FALSE
+    70  END
```

### `KRC/R1/Program/Utilities/RejectGE4.src`

changed, integrator program: 1 code line(s) removed, 0 added; 10 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Utilities/RejectGE4.src.diff](diffs/KRC/R1/Program/Utilities/RejectGE4.src.diff)

```diff
@@ base line 46, backup line 46 @@
     46  LIN XP23
     56  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
-    63  GRPg_Check(1, 1, FALSE, 1)
     60  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254] )
     65  $BWDSTART=FALSE
```

### `KRC/R1/System/$config.dat`

changed, integrator program: 5 code line(s) removed, 12 added; 30 comment/blank line change(s). Full diff: [diffs/KRC/R1/System/$config.dat.diff](diffs/KRC/R1/System/$config.dat.diff)

Data changes:

- CL_GUN_WELD_MAX (INT): 76000 -> 73000
- CL_GUN_WELD_MIN (INT): 65000 -> 69000
- added 1 BOOL: NUT_START
- added 6 INT: CL_GUN_CLOSE_TIMEOUT, CL_GUN_IN_WINDOW_TIME, CL_GUN_PRESS_BASE, CL_GUN_PRESS_REST, CL_GUN_PRESS_WELD, CL_WELD_PROGRAM
- added 3 SIGNAL: CL_BeaconBit3001, CL_BeaconBit3008, CL_BeaconBit3024
- removed 2 BOOL: NUT_STAR, NUT_WELD_RETRY
- removed 1 SIGNAL: NUT_PRESENT1

```diff
@@ base line 760, backup line 760 @@
    760  BOOL PARTPRESENT2=FALSE
    761  BOOL PARTPRESENT3=FALSE
-   763  SIGNAL NUT_PRESENT1 $IN[227]
    769  DECL CHAR LDDPLUGIN_VARNAME[19]
    770  LDDPLUGIN_VARNAME[]="LDDPLUGIN_ACTIVATED"
@@ base line 817, backup line 817 @@
    817  SIGNAL CL_PIN_BYTE1 $IN[599] TO $IN[606]
    819  INT CL_WeldPinPosition=27339
+   824  SIGNAL CL_BeaconBit3001 $OUT[3001]
+   825  SIGNAL CL_BeaconBit3008 $OUT[3008]
+   826  SIGNAL CL_BeaconBit3024 $OUT[3024]
    833  DECL INT CL_PIN_WELD_MIN=10000
    834  DECL INT CL_PIN_WELD_MAX=13500
-   830  DECL INT CL_GUN_WELD_MIN=65000
-   831  DECL INT CL_GUN_WELD_MAX=76000
-   839  DECL BOOL NUT_STAR=FALSE
+   838  DECL INT CL_GUN_WELD_MIN=69000
+   839  DECL INT CL_GUN_WELD_MAX=73000
+   842  DECL INT CL_GUN_CLOSE_TIMEOUT=1000
+   843  DECL INT CL_GUN_IN_WINDOW_TIME=300
+   848  DECL INT CL_GUN_PRESS_BASE=405
+   849  DECL INT CL_GUN_PRESS_WELD=1820
+   850  DECL INT CL_GUN_PRESS_REST=39425
+   852  DECL INT CL_WELD_PROGRAM=2
+   860  DECL BOOL NUT_START=FALSE
    865  DECL BOOL NUT_READY=TRUE
    868  DECL BOOL NUTCYCLE_ACTIVE=FALSE
@@ base line 856, backup line 877 @@
    877  DECL BOOL NEXT_NUT_READY=TRUE
    878  DECL BOOL NEXT_NUT_REQUEST=FALSE
-   859  DECL BOOL NUT_WELD_RETRY=FALSE
    880  DECL BOOL STEP10_ADV_STARTED=FALSE
    884  ENDDAT
```

### `KRC/R1/System/sps.sub`

changed, integrator program: 12 code line(s) removed, 13 added; 45 comment/blank line change(s). Full diff: [diffs/KRC/R1/System/sps.sub.diff](diffs/KRC/R1/System/sps.sub.diff)

```diff
@@ base line 57, backup line 57 @@
     57  ENDIF
     61  GRPg_ChkSetStatePLC()
+    74  AutomationCore_BKG ( )
     86  CL_GunStrokePositionLPT=(CL_LPT_BYTE1*65536)+(CL_LPT_BYTE2*256)+CL_LPT_BYTE3
     90  CL_WeldPinPosition=(CL_PIN_BYTE0*256)+CL_PIN_BYTE1
     93  SV0500_FLOW =( SV0500_BYTE0*256)+SV0500_BYTE1
-    94  IF SV0500_FLOW > 1230 THEN
-    95  CL_WaterOk = TRUE
+   100  nWaterFlow = SV0500_FLOW / 4
+   101  IF nWaterFlow >= nWaterFlowMin THEN
    102  dipw1_WaterOk = TRUE
    103  ELSE
-    98  CL_WaterOk = FALSE
-    99  dipw1_WaterOk = TRUE
+   104  IF nWaterFlow < (nWaterFlowMin - nWaterFlowHyst) THEN
+   105  dipw1_WaterOk = FALSE
    106  ENDIF
-   108  IF $OUT[478] THEN
-   109  $OUT[3008] = TRUE
-   110  $OUT[3024] = TRUE
    107  ENDIF
-   114  IF $OUT[477] THEN
-   115  $OUT[3001] = TRUE
-   116  $OUT[3024] = FALSE
+   109  CL_WaterOk = dipw1_WaterOk
+   117  IF dopw1_LowLevel THEN
+   118  CL_BeaconBit3008 = TRUE
+   119  CL_BeaconBit3024 = TRUE
    120  ENDIF
-   125  IF di004UseDryCycle==FALSE THEN
-   126  $OUT[475]=TRUE
+   124  IF dopw1_LevelOk THEN
+   125  CL_BeaconBit3001 = TRUE
+   126  CL_BeaconBit3024 = FALSE
    127  ENDIF
+   135  dopw1_StartWater=di013WaterEnable
    141  PRELOAD()
    147  ENDLOOP
```

### `KRC/R1/Mada/$machine.dat`

changed, machine data: 1 code line(s) removed, 1 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Mada/$machine.dat.diff](diffs/KRC/R1/Mada/$machine.dat.diff)

Attributes: +&PARAM VERSION = 1.0.0; -&PARAM VERSION = 1.0.0

```diff
@@ base line 385, backup line 385 @@
    385  $AXWORKSPACE[8]={A1_N 0.0,A1_P 0.0,A2_N 0.0,A2_P 0.0,A3_N 0.0,A3_P 0.0,A4_N 0.0,A4_P 0.0,A5_N 0.0,A5_P 0.0,A6_N 0.0,A6_P 0.0,E1_N 0.0,E1_P 0.0,E2_N 0.0,E2_P 0.0,E3_N 0.0,E3_P 0.0,E4_N 0.0,E4_P 0.0,E5_N 0.0,E5_P 0.0,E6_N 0.0,E6_P 0. [...]
    386  CHAR $AXWORKSPACE_NAME1[24]
-   387  $AXWORKSPACE_NAME1[]="AXWORKSPACE_NAME 1      "
+   387  $AXWORKSPACE_NAME1[]="AXWORKSPACE_NAME 1"
    388  CHAR $AXWORKSPACE_NAME2[24]
    389  $AXWORKSPACE_NAME2[]="AXWORKSPACE_NAME 2"
```

### `KRC/R1/System/tm_bib.dat`

changed, KUKA system / vendor package: 1 code line(s) removed, 1 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/System/tm_bib.dat.diff](diffs/KRC/R1/System/tm_bib.dat.diff)

Data changes:

- iSTOP_TYPE (INT): 20 -> 0

Runtime values (left out of the code diff): iTQM_ZEIGER: 2 -> 1; TQM_ACT: {T11 200,T12 200,T13 200,T14 200,T15 200... -> {T11 200,T12 200,T13 200,T14 200,T15 200...

```diff
@@ base line 36, backup line 36 @@
     36  REAL ScalingImpact=250000.0
     37  REAL TooLarge=100000.0
-    47  DECL INT iSTOP_TYPE=20
+    47  DECL INT iSTOP_TYPE=0
     48  DECL REAL rPAR=0.0
     50  GLOBAL INT iTQM_DELAY=150
```

### `KRC/R1/TP/AutomationCore/automationcoreroutines.dat`

changed, KUKA system / vendor package: 15 code line(s) removed, 16 added; 6 comment/blank line change(s). Full diff: [diffs/KRC/R1/TP/AutomationCore/automationcoreroutines.dat.diff](diffs/KRC/R1/TP/AutomationCore/automationcoreroutines.dat.diff)

Data changes:

- added 1 BOOL: bACEntryGranted
- added 15 SIGNAL: di100CameraJudgmentOK, di101CameraJudgmentNG, di106PartRejected, di227NutPresent1, di466PartClampOpen, di467PartClampClosed, di470QFPAdvanced, do106PartRejected, do498UpperPinExtend, do499UpperPinRetract, do501PartClampClose, do502PartClampOpen ...
- removed 15 SIGNAL: di100CameraJudmentOK, di101CameraJudmentNG, di106PartRejeted, di227SensorCamera, di466Reserved, di467Reserved, di470Reserved, do106PartRejeted, do498Reserved, do499Reserved, do501Reserved, do502Reserved ...

```diff
@@ base line 137, backup line 137 @@
    137  GLOBAL SIGNAL di098Spare $IN[98]
    138  GLOBAL SIGNAL di099Spare $IN[99]
-   139  GLOBAL SIGNAL di100CameraJudmentOK $IN[100]
-   140  GLOBAL SIGNAL di101CameraJudmentNG $IN[101]
+   139  GLOBAL SIGNAL di100CameraJudgmentOK $IN[100]
+   140  GLOBAL SIGNAL di101CameraJudgmentNG $IN[101]
    141  GLOBAL SIGNAL di102Spare $IN[102]
    142  GLOBAL SIGNAL di103Spare $IN[103]
    143  GLOBAL SIGNAL di104Spare $IN[104]
    144  GLOBAL SIGNAL di105Spare $IN[105]
-   145  GLOBAL SIGNAL di106PartRejeted $IN[106]
+   145  GLOBAL SIGNAL di106PartRejected $IN[106]
    146  GLOBAL SIGNAL di107Spare $IN[107]
    147  GLOBAL SIGNAL di108Spare $IN[108]
@@ base line 314, backup line 314 @@
    314  GLOBAL SIGNAL do104Axis1Bit128 $OUT[104]
    315  GLOBAL SIGNAL do105Axis1Bit256 $OUT[105]
-   316  GLOBAL SIGNAL do106PartRejeted $OUT[106]
+   316  GLOBAL SIGNAL do106PartRejected $OUT[106]
    317  GLOBAL SIGNAL do107Hopper1LowLevel $OUT[107]
    318  GLOBAL SIGNAL do108Hopper2LowLevel $OUT[108]
@@ base line 638, backup line 638 @@
    638  GLOBAL SIGNAL di225WaterFlowOK $IN[225]
    639  GLOBAL SIGNAL di226Spare $IN[226]
-   641  GLOBAL SIGNAL di227SensorCamera $IN[227]
+   642  GLOBAL SIGNAL di227NutPresent1 $IN[227]
    643  GLOBAL SIGNAL di228Spare $IN[228]
    644  GLOBAL SIGNAL di229Spare $IN[229]
@@ base line 1342, backup line 1343 @@
   1343  GLOBAL SIGNAL do496Reserved $OUT[496]
   1344  GLOBAL SIGNAL do497Reserved $OUT[497]
-  1344  GLOBAL SIGNAL do498Reserved $OUT[498]
-  1345  GLOBAL SIGNAL do499Reserved $OUT[499]
+  1347  GLOBAL SIGNAL do498UpperPinExtend $OUT[498]
+  1348  GLOBAL SIGNAL do499UpperPinRetract $OUT[499]
   1349  GLOBAL SIGNAL do500Reserved $OUT[500]
-  1347  GLOBAL SIGNAL do501Reserved $OUT[501]
-  1348  GLOBAL SIGNAL do502Reserved $OUT[502]
-  1349  GLOBAL SIGNAL do503Reserved $OUT[503]
-  1350  GLOBAL SIGNAL do504Reserved $OUT[504]
-  1351  GLOBAL SIGNAL do505Reserved $OUT[505]
+  1350  GLOBAL SIGNAL do501PartClampClose $OUT[501]
+  1351  GLOBAL SIGNAL do502PartClampOpen $OUT[502]
+  1352  GLOBAL SIGNAL do503QFPAdvance $OUT[503]
+  1353  GLOBAL SIGNAL do504QFPReturn $OUT[504]
+  1354  GLOBAL SIGNAL do505QFPNutBlowOff $OUT[505]
   1357  GLOBAL SIGNAL di465Reserved $IN[465]
-  1355  GLOBAL SIGNAL di466Reserved $IN[466]
-  1356  GLOBAL SIGNAL di467Reserved $IN[467]
+  1358  GLOBAL SIGNAL di466PartClampOpen $IN[466]
+  1359  GLOBAL SIGNAL di467PartClampClosed $IN[467]
   1360  GLOBAL SIGNAL di468Reserved $IN[468]
   1361  GLOBAL SIGNAL di469Reserved $IN[469]
-  1359  GLOBAL SIGNAL di470Reserved $IN[470]
+  1362  GLOBAL SIGNAL di470QFPAdvanced $IN[470]
   1363  GLOBAL SIGNAL di471Reserved $IN[471]
   1364  GLOBAL SIGNAL di472WaterTempOK $IN[472]
@@ base line 1608, backup line 1611 @@
   1611  GLOBAL SIGNAL do932GripperInProcess $OUT[932]
```
_3 more lines: see diffs/KRC/R1/TP/AutomationCore/automationcoreroutines.dat.diff_

### `KRC/R1/TP/AutomationCore/automationcoreroutines.src`

changed, KUKA system / vendor package: 30 code line(s) removed, 8 added; 5 comment/blank line change(s). Full diff: [diffs/KRC/R1/TP/AutomationCore/automationcoreroutines.src.diff](diffs/KRC/R1/TP/AutomationCore/automationcoreroutines.src.diff)

```diff
@@ base line 29, backup line 30 @@
     30  dopw1_WeldContactEnable=FALSE
     31  dopw1_WeldOnExternal=FALSE
-    31  dopw2_WeldContactEnable=FALSE
-    32  dopw2_WeldOnExternal=FALSE
-    33  dopw3_WeldContactEnable=FALSE
-    34  dopw3_WeldOnExternal=FALSE
     32  ELSE
     33  dopw1_WeldContactEnable=TRUE
     34  dopw1_WeldOnExternal=TRUE
-    38  dopw2_WeldContactEnable=TRUE
-    39  dopw2_WeldOnExternal=TRUE
-    40  dopw3_WeldContactEnable=TRUE
-    41  dopw3_WeldOnExternal=TRUE
     35  ENDIF
     38  do123ToolIDBit0 = di823ToolIDBit0
@@ base line 96, backup line 89 @@
     89  do022MstrRefRequired = ($MasteringTest_Req_Int==TRUE)
     90  gdoAxis1Posn=$AXIS_ACT.A1 + nA1Offset
-    98  do094AirOK= (dipw1_AirOK AND dipw2_AirOK AND dipw3_AirOK)
-    99  do013WaterIsOn = ((di472WaterTempOK AND di474WaterOk) AND (di520WaterTempOK AND di522WaterOk) AND (di568WaterTempOK AND di570WaterOk))
+    91  do094AirOK= dipw1_AirOK
+    92  do013WaterIsOn = dipw1_WaterOk
     93  do107Hopper1LowLevel= NOT dipw1_HopperLowLevel
-   101  do108Hopper2LowLevel= NOT dipw2_HopperLowLevel
-   102  do110Hopper3LowLevel= NOT dipw3_HopperLowLevel
     94  do111Gun1ElectrodeChange= dipw1_EndofStepper
-   104  do112Gun2ElectrodeChange= dipw2_EndofStepper
-   105  do113Gun3ElectrodeChange= dipw3_EndofStepper
     95  do118Nut1Ready= (dipw1_Ready AND NOT dipw1_Fault)
-   107  do119Nut2Ready= (dipw2_Ready AND NOT dipw2_Fault)
-   108  do120Nut3Ready= (dipw3_Ready AND NOT dipw3_Fault)
     96  do134Nut1Fault= (dipw1_Fault OR NOT dipw1_Ready)
-   110  do135Nut2Fault= (dipw2_Fault OR NOT dipw2_Ready)
-   111  do136Nut3Fault= (dipw3_Fault OR NOT dipw3_Ready)
-   113  IF di013WaterEnable==TRUE THEN
-   114  do475StartWater=TRUE
-   115  do523StartWater=TRUE
-   116  do571StartWater=TRUE
-   117  ELSE
-   118  ENDIF
    100  do464WaterBeacon = (di472WaterTempOK AND di474WaterOk)
-   121  do512WaterBeacon = (di520WaterTempOK AND di522WaterOk)
-   122  do560WaterBeacon = (di568WaterTempOK AND di570WaterOk)
    103  IF (($MODE_OP==#EX) AND NOT ($OV_PRO==100)) THEN
    104  do146SpeedNot100=TRUE
@@ base line 1429, backup line 1407 @@
   1407  ENDFCT
   1411  GLOBAL DEF AC_Request_to_enter( )
-  1439  IF di006RequestToEnter AND NOT (dipw1_GunAtWork OR dipw2_GunAtWork OR dipw3_GunAtWork OR do932GripperInProcess OR do931BrakeTestInProcess OR do930MasterRefInProcess) THEN
-  1440  doCriticalWZ = FALSE
-  1441  WAIT FOR (di006RequestToEnter)==FALSE
+  1420  IF di006RequestToEnter THEN
+  1421  IF NOT bACEntryGranted AND NOT (dipw1_GunAtWork OR do932GripperInProcess OR do931BrakeTestInProcess OR do930MasterRefInProcess) THEN
+  1422  bACEntryGranted = TRUE
+  1423  ENDIF
   1424  ELSE
-  1443  doCriticalWZ = TRUE
+  1425  bACEntryGranted = FALSE
   1426  ENDIF
```
_3 more lines: see diffs/KRC/R1/TP/AutomationCore/automationcoreroutines.src.diff_

### `KRC/R1/TP/GripperSpotTech/grp_data.dat`

changed, KUKA system / vendor package: 20 code line(s) removed, 20 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/TP/GripperSpotTech/grp_data.dat.diff](diffs/KRC/R1/TP/GripperSpotTech/grp_data.dat.diff)

Attributes: -&ACCESS  RV; -&PARAM DISKPATH = TP/GripperSpotTech

Data changes:

- GRPg_GhostMode (BOOL): FALSE -> False
- GRPg_SignVal (INT): 5861033 -> 7850579
- added 1 DEFDAT: Grp_Data
- removed 1 DEFDAT: grp_data

```diff
@@ base line 3, backup line 1 @@
-     3  DEFDAT grp_data PUBLIC
+     1  DEFDAT Grp_Data PUBLIC
     10  GLOBAL STRUC GRP_T CHAR Name[24],BOOL Act,INT NumState,NumOut,NumIn,OUT1,OUT2,OUT3,OUT4,OUT5,OUT6,IN1,IN2,IN3,IN4,IN5,IN6
-    13  GLOBAL STRUC GRP_GrpPar_T REAL PulsLen,INT TimeOut,BOOL GhOut1,GhOut2,GhOut3,GhOut4,GhOut5,GhOut6,GhIn1,GhIn2,GhIn3,GhIn4,GhIn5,GhIn6
+    11  GLOBAL STRUC GRP_GrpPar_T REAL PulsLen, INT TimeOut,BOOL GhOut1,GhOut2,GhOut3,GhOut4,GhOut5,GhOut6,GhIn1,GhIn2,GhIn3,GhIn4,GhIn5,GhIn6
     12  GLOBAL STRUC GRP_State_T CHAR Name[12],INT OUT1,OUT2,OUT3,OUT4,OUT5,OUT6,IN1,IN2,IN3,IN4,IN5,IN6,StateNo,FuncNo,InputNo,BOOL Value
     13  GLOBAL ENUM GRP_ErrStrategy_T StopAtErr,DialAtT1T2,DialAtT1T2Aut,DialAllMode,UserErrStrategy
@@ base line 20, backup line 18 @@
     18  GLOBAL INT GRPg_MaxGrp=16
     19  GLOBAL INT GRPg_Err2PLC=0
-    22  GLOBAL BOOL GRPg_GhostMode=FALSE
+    20  GLOBAL BOOL GRPg_GhostMode=False
     21  GLOBAL INT GRPg_GhostInput=0
-    24  GLOBAL INT GRPg_SignVal=5861033
+    22  GLOBAL INT GRPg_SignVal=7850579
     23  DECL GLOBAL GRP_ErrStrategy_T GRPg_ErrStrategy[3]
     24  GRPg_ErrStrategy[1]=#DialAtT1T2
@@ base line 48, backup line 46 @@
     46  GRPg_Grp[16]={Name[] "Gripper16",Act FALSE,NumState 2,NumOut 2,NumIn 2,OUT1 0,OUT2 0,OUT3 0,OUT4 0,OUT5 0,OUT6 0,IN1 1026,IN2 1026,IN3 0,IN4 0,IN5 0,IN6 0}
     50  DECL GLOBAL GRP_GrpPar_T GRPg_GrpPar[16]
-    53  GRPg_GrpPar[1]={PulsLen 0.500000,TimeOut 3000,GhOut1 TRUE,GhOut2 TRUE,GhOut3 FALSE,GhOut4 FALSE,GhOut5 FALSE,GhOut6 FALSE,GhIn1 FALSE,GhIn2 FALSE,GhIn3 FALSE,GhIn4 FALSE,GhIn5 FALSE,GhIn6 FALSE}
-    54  GRPg_GrpPar[2]={PulsLen 0.500000,TimeOut 3000,GhOut1 FALSE,GhOut2 FALSE,GhOut3 FALSE,GhOut4 FALSE,GhOut5 FALSE,GhOut6 FALSE,GhIn1 FALSE,GhIn2 FALSE,GhIn3 FALSE,GhIn4 FALSE,GhIn5 FALSE,GhIn6 FALSE}
-    55  GRPg_GrpPar[3]={PulsLen 0.500000,TimeOut 3000,GhOut1 FALSE,GhOut2 FALSE,GhOut3 FALSE,GhOut4 FALSE,GhOut5 FALSE,GhOut6 FALSE,GhIn1 FALSE,GhIn2 FALSE,GhIn3 FALSE,GhIn4 FALSE,GhIn5 FALSE,GhIn6 FALSE}
-    56  GRPg_GrpPar[4]={PulsLen 0.500000,TimeOut 3000,GhOut1 FALSE,GhOut2 FALSE,GhOut3 FALSE,GhOut4 FALSE,GhOut5 FALSE,GhOut6 FALSE,GhIn1 FALSE,GhIn2 FALSE,GhIn3 FALSE,GhIn4 FALSE,GhIn5 FALSE,GhIn6 FALSE}
-    57  GRPg_GrpPar[5]={PulsLen 0.500000,TimeOut 3000,GhOut1 FALSE,GhOut2 FALSE,GhOut3 FALSE,GhOut4 FALSE,GhOut5 FALSE,GhOut6 FALSE,GhIn1 TRUE,GhIn2 TRUE,GhIn3 FALSE,GhIn4 FALSE,GhIn5 FALSE,GhIn6 FALSE}
-    58  GRPg_GrpPar[6]={PulsLen 0.500000,TimeOut 3000,GhOut1 FALSE,GhOut2 FALSE,GhOut3 FALSE,GhOut4 FALSE,GhOut5 FALSE,GhOut6 FALSE,GhIn1 TRUE,GhIn2 TRUE,GhIn3 FALSE,GhIn4 FALSE,GhIn5 FALSE,GhIn6 FALSE}
-    59  GRPg_GrpPar[7]={PulsLen 0.500000,TimeOut 3000,GhOut1 FALSE,GhOut2 FALSE,GhOut3 FALSE,GhOut4 FALSE,GhOut5 FALSE,GhOut6 FALSE,GhIn1 TRUE,GhIn2 TRUE,GhIn3 FALSE,GhIn4 FALSE,GhIn5 FALSE,GhIn6 FALSE}
-    60  GRPg_GrpPar[8]={PulsLen 0.500000,TimeOut 3000,GhOut1 FALSE,GhOut2 FALSE,GhOut3 FALSE,GhOut4 FALSE,GhOut5 FALSE,GhOut6 FALSE,GhIn1 TRUE,GhIn2 TRUE,GhIn3 FALSE,GhIn4 FALSE,GhIn5 FALSE,GhIn6 FALSE}
-    61  GRPg_GrpPar[9]={PulsLen 0.500000,TimeOut 3000,GhOut1 FALSE,GhOut2 FALSE,GhOut3 FALSE,GhOut4 FALSE,GhOut5 FALSE,GhOut6 FALSE,GhIn1 TRUE,GhIn2 TRUE,GhIn3 FALSE,GhIn4 FALSE,GhIn5 FALSE,GhIn6 FALSE}
-    62  GRPg_GrpPar[10]={PulsLen 0.500000,TimeOut 3000,GhOut1 FALSE,GhOut2 FALSE,GhOut3 FALSE,GhOut4 FALSE,GhOut5 FALSE,GhOut6 FALSE,GhIn1 TRUE,GhIn2 TRUE,GhIn3 FALSE,GhIn4 FALSE,GhIn5 FALSE,GhIn6 FALSE}
-    63  GRPg_GrpPar[11]={PulsLen 0.500000,TimeOut 3000,GhOut1 FALSE,GhOut2 FALSE,GhOut3 FALSE,GhOut4 FALSE,GhOut5 FALSE,GhOut6 FALSE,GhIn1 TRUE,GhIn2 TRUE,GhIn3 FALSE,GhIn4 FALSE,GhIn5 FALSE,GhIn6 FALSE}
-    64  GRPg_GrpPar[12]={PulsLen 0.500000,TimeOut 3000,GhOut1 FALSE,GhOut2 FALSE,GhOut3 FALSE,GhOut4 FALSE,GhOut5 FALSE,GhOut6 FALSE,GhIn1 TRUE,GhIn2 TRUE,GhIn3 FALSE,GhIn4 FALSE,GhIn5 FALSE,GhIn6 FALSE}
-    65  GRPg_GrpPar[13]={PulsLen 0.500000,TimeOut 3000,GhOut1 FALSE,GhOut2 FALSE,GhOut3 FALSE,GhOut4 FALSE,GhOut5 FALSE,GhOut6 FALSE,GhIn1 TRUE,GhIn2 TRUE,GhIn3 FALSE,GhIn4 FALSE,GhIn5 FALSE,GhIn6 FALSE}
-    66  GRPg_GrpPar[14]={PulsLen 0.500000,TimeOut 3000,GhOut1 FALSE,GhOut2 FALSE,GhOut3 FALSE,GhOut4 FALSE,GhOut5 FALSE,GhOut6 FALSE,GhIn1 TRUE,GhIn2 TRUE,GhIn3 FALSE,GhIn4 FALSE,GhIn5 FALSE,GhIn6 FALSE}
-    67  GRPg_GrpPar[15]={PulsLen 0.500000,TimeOut 3000,GhOut1 FALSE,GhOut2 FALSE,GhOut3 FALSE,GhOut4 FALSE,GhOut5 FALSE,GhOut6 FALSE,GhIn1 TRUE,GhIn2 TRUE,GhIn3 FALSE,GhIn4 FALSE,GhIn5 FALSE,GhIn6 FALSE}
-    68  GRPg_GrpPar[16]={PulsLen 0.500000,TimeOut 3000,GhOut1 FALSE,GhOut2 FALSE,GhOut3 FALSE,GhOut4 FALSE,GhOut5 FALSE,GhOut6 FALSE,GhIn1 TRUE,GhIn2 TRUE,GhIn3 FALSE,GhIn4 FALSE,GhIn5 FALSE,GhIn6 FALSE}
+    51  GRPg_GrpPar[1]={PulsLen 0.5,TimeOut 3000,GhOut1 True,GhOut2 True,GhOut3 False,GhOut4 False,GhOut5 False,GhOut6 False,GhIn1 False,GhIn2 False,GhIn3 False,GhIn4 False,GhIn5 False,GhIn6 False}
+    52  GRPg_GrpPar[2]={PulsLen 0.5,TimeOut 3000,GhOut1 False,GhOut2 False,GhOut3 False,GhOut4 False,GhOut5 False,GhOut6 False,GhIn1 False,GhIn2 False,GhIn3 False,GhIn4 False,GhIn5 False,GhIn6 False}
+    53  GRPg_GrpPar[3]={PulsLen 0.5,TimeOut 3000,GhOut1 False,GhOut2 False,GhOut3 False,GhOut4 False,GhOut5 False,GhOut6 False,GhIn1 False,GhIn2 False,GhIn3 False,GhIn4 False,GhIn5 False,GhIn6 False}
+    54  GRPg_GrpPar[4]={PulsLen 0.5,TimeOut 3000,GhOut1 False,GhOut2 False,GhOut3 False,GhOut4 False,GhOut5 False,GhOut6 False,GhIn1 False,GhIn2 False,GhIn3 False,GhIn4 False,GhIn5 False,GhIn6 False}
+    55  GRPg_GrpPar[5]={PulsLen 0.5,TimeOut 3000,GhOut1 False,GhOut2 False,GhOut3 False,GhOut4 False,GhOut5 False,GhOut6 False,GhIn1 True,GhIn2 True,GhIn3 False,GhIn4 False,GhIn5 False,GhIn6 False}
+    56  GRPg_GrpPar[6]={PulsLen 0.5,TimeOut 3000,GhOut1 False,GhOut2 False,GhOut3 False,GhOut4 False,GhOut5 False,GhOut6 False,GhIn1 True,GhIn2 True,GhIn3 False,GhIn4 False,GhIn5 False,GhIn6 False}
+    57  GRPg_GrpPar[7]={PulsLen 0.5,TimeOut 3000,GhOut1 False,GhOut2 False,GhOut3 False,GhOut4 False,GhOut5 False,GhOut6 False,GhIn1 True,GhIn2 True,GhIn3 False,GhIn4 False,GhIn5 False,GhIn6 False}
+    58  GRPg_GrpPar[8]={PulsLen 0.5,TimeOut 3000,GhOut1 False,GhOut2 False,GhOut3 False,GhOut4 False,GhOut5 False,GhOut6 False,GhIn1 True,GhIn2 True,GhIn3 False,GhIn4 False,GhIn5 False,GhIn6 False}
+    59  GRPg_GrpPar[9]={PulsLen 0.5,TimeOut 3000,GhOut1 False,GhOut2 False,GhOut3 False,GhOut4 False,GhOut5 False,GhOut6 False,GhIn1 True,GhIn2 True,GhIn3 False,GhIn4 False,GhIn5 False,GhIn6 False}
+    60  GRPg_GrpPar[10]={PulsLen 0.5,TimeOut 3000,GhOut1 False,GhOut2 False,GhOut3 False,GhOut4 False,GhOut5 False,GhOut6 False,GhIn1 True,GhIn2 True,GhIn3 False,GhIn4 False,GhIn5 False,GhIn6 False}
+    61  GRPg_GrpPar[11]={PulsLen 0.5,TimeOut 3000,GhOut1 False,GhOut2 False,GhOut3 False,GhOut4 False,GhOut5 False,GhOut6 False,GhIn1 True,GhIn2 True,GhIn3 False,GhIn4 False,GhIn5 False,GhIn6 False}
+    62  GRPg_GrpPar[12]={PulsLen 0.5,TimeOut 3000,GhOut1 False,GhOut2 False,GhOut3 False,GhOut4 False,GhOut5 False,GhOut6 False,GhIn1 True,GhIn2 True,GhIn3 False,GhIn4 False,GhIn5 False,GhIn6 False}
+    63  GRPg_GrpPar[13]={PulsLen 0.5,TimeOut 3000,GhOut1 False,GhOut2 False,GhOut3 False,GhOut4 False,GhOut5 False,GhOut6 False,GhIn1 True,GhIn2 True,GhIn3 False,GhIn4 False,GhIn5 False,GhIn6 False}
+    64  GRPg_GrpPar[14]={PulsLen 0.5,TimeOut 3000,GhOut1 False,GhOut2 False,GhOut3 False,GhOut4 False,GhOut5 False,GhOut6 False,GhIn1 True,GhIn2 True,GhIn3 False,GhIn4 False,GhIn5 False,GhIn6 False}
+    65  GRPg_GrpPar[15]={PulsLen 0.5,TimeOut 3000,GhOut1 False,GhOut2 False,GhOut3 False,GhOut4 False,GhOut5 False,GhOut6 False,GhIn1 True,GhIn2 True,GhIn3 False,GhIn4 False,GhIn5 False,GhIn6 False}
+    66  GRPg_GrpPar[16]={PulsLen 0.5,TimeOut 3000,GhOut1 False,GhOut2 False,GhOut3 False,GhOut4 False,GhOut5 False,GhOut6 False,GhIn1 True,GhIn2 True,GhIn3 False,GhIn4 False,GhIn5 False,GhIn6 False}
     70  DECL GLOBAL GRP_State_T GRPg_State[16,6]
     71  GRPg_State[1,1]={Name[] "OPEN",OUT1 1,OUT2 -1,OUT3 0,OUT4 0,OUT5 0,OUT6 0,IN1 1,IN2 -1,IN3 0,IN4 0,IN5 0,IN6 0,StateNo 0,FuncNo 0,InputNo 0,Value FALSE}
```

### `KRC/R1/TP/NutWeld/nutweldroutines.dat`

changed, KUKA system / vendor package: 2 code line(s) removed, 2 added; 4 comment/blank line change(s). Full diff: [diffs/KRC/R1/TP/NutWeld/nutweldroutines.dat.diff](diffs/KRC/R1/TP/NutWeld/nutweldroutines.dat.diff)

Data changes:

- nMaxGunNr (INT): 3 -> 1

```diff
@@ base line 12, backup line 12 @@
     12  GLOBAL ENUM Nut_Dump_Move Reload_PTP,Reload_LIN
     13  DECL GLOBAL BOOL bDump_Nut
-    14  DECL GLOBAL INT nMaxGunNr=3
+    14  DECL GLOBAL INT nMaxGunNr=1
     15  DECL GLOBAL INT nMaxWeldRetries=0
     16  DECL GLOBAL INT nMaxFeedRetries=0
@@ base line 63, backup line 63 @@
     63  DECL GLOBAL REAL rActualValue
     64  DECL GLOBAL BOOL WeldTouchUp=FALSE
-    75  GLOBAL SIGNAL dipw1_AirOK $IN[473]
+    75  GLOBAL SIGNAL dipw1_AirOK $IN[3132]
     78  GLOBAL BOOL dipw1_WaterOk=TRUE
     80  GLOBAL SIGNAL dipw1_XtfmrTempOk $IN[475]
```

### Runtime values only

A .dat keeps the last value the program wrote to each of its variables, and the inline-form editor keeps its suggestions (LAST_BASIS...): these files changed only in such values, nobody edited them.

| File | Values | Diff |
|---|---|---|
| `KRC/R1/TP/GripperSpotTech/grp_func.dat` | GRP_iPreStNo: 1 -> 2; GRP_PreState[1]: {iGrpIn 257,iStInVal 1,bStInVal TRUE,bGh... -> {iGrpIn 257,iStInVal -1,bStInVal FALSE,b...; GRP_PreState[2]: {iGrpIn 258,iStInVal -1,bStInVal FALSE,b... -> {iGrpIn 258,iStInVal 1,bStInVal TRUE,bGh...; GRPg_ProcessData: {ActGrp 1,ReqState 0,LastGrpNo 1,LastStN... -> {ActGrp 1,ReqState 0,LastGrpNo 1,LastStN... | diffs/KRC/R1/TP/GripperSpotTech/grp_func.dat.diff |

### Comment-only changes

| File | Comment/blank line changes | Attributes | Diff |
|---|---|---|---|
| `KRC/R1/Mada/$robcor.dat` | 0 | +&PARAM VERSION = 1.0.0; -&PARAM VERSION = 1.0.0 | diffs/KRC/R1/Mada/$robcor.dat.diff |
| `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src` | 26 | - | diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src.diff |
| `KRC/R1/Program/Styles/style_1.src` | 9 | - | diffs/KRC/R1/Program/Styles/style_1.src.diff |
| `KRC/R1/Program/Utilities/gunelectrodechange.src` | 6 | - | diffs/KRC/R1/Program/Utilities/gunelectrodechange.src.diff |
| `KRC/R1/cell.src` | 5 | - | diffs/KRC/R1/cell.src.diff |
| `KRC/STEU/Mada/$custom.dat` | 0 | -&ACCESS RV$; +&ACCESS  RV; +&PARAM DISKPATH = MADA; +&PARAM VERSION = 1.0.0 | diffs/KRC/STEU/Mada/$custom.dat.diff |

## Mechanical checks

Signal declarations changed (names lower-cased):

- $IN[100]: di100camerajudmentok -> di100camerajudgmentok
- $IN[101]: di101camerajudmentng -> di101camerajudgmentng
- $IN[106]: di106partrejeted -> di106partrejected
- $IN[227]: di227sensorcamera, nut_present1 -> di227nutpresent1
- $IN[466]: di466reserved, di466spare -> di466partclampopen, di466spare
- $IN[467]: di467reserved, di467spare -> di467partclampclosed, di467spare
- $IN[470]: di470reserved, di470spare -> di470qfpadvanced, di470spare
- $IN[473]: di473airok, dipw1_airok -> di473airok
- $IN[3132]: (not declared) -> dipw1_airok
- $OUT[106]: do106partrejeted -> do106partrejected
- $OUT[498]: do498reserved -> do498upperpinextend
- $OUT[499]: do499reserved -> do499upperpinretract
- $OUT[501]: do501reserved -> do501partclampclose
- $OUT[502]: do502reserved -> do502partclampopen
- $OUT[503]: do503reserved -> do503qfpadvance
- $OUT[504]: do504reserved -> do504qfpreturn
- $OUT[505]: do505reserved -> do505qfpnutblowoff
- $OUT[3001]: (not declared) -> cl_beaconbit3001
- $OUT[3008]: (not declared) -> cl_beaconbit3008
- $OUT[3024]: (not declared) -> cl_beaconbit3024

### FAIL (0)

_none_

### WARN (0)

_none_

### INFO (16)

- `KRC/R1/Program/Centerline/CENTERLINE_HOME.src:55` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR dipw1_SpearHome
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:50` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR $PRO_STATE0==#P_ACTIVE
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:65` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR dipw1_AirOK
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:78` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR dipw1_WaterOk
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:98` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR (CL_GunStrokePositionLPT>=nGunOpenMin) AND (CL_GunStrokePosit
- `KRC/R1/Program/Centerline/centerline_weld.src:70` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR di466PartClampOpen
- `KRC/R1/Program/Centerline/centerline_weld.src:80` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR dipw1_SpearHome
- `KRC/R1/Program/Centerline/centerline_weld.src:95` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR di470QFPAdvanced
- `KRC/R1/Program/Centerline/centerline_weld.src:110` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR dipw1_SpearHome
- `KRC/R1/Program/Centerline/centerline_weld.src:146` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR di467PartClampClosed
- `KRC/R1/Program/Centerline/centerline_weld.src:227` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR (CL_GunStrokePositionLPT>=CL_GUN_WELD_MIN) AND (CL_GunStrokeP
- `KRC/R1/Program/Centerline/centerline_weld.src:275` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR di466PartClampOpen
- `KRC/R1/Program/Centerline/centerline_weld.src:286` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR dipw1_SpearHome
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src:37` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254])
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src:38` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254])
- `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src:39` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254])
