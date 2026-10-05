# Backup audit - 658424_R10_2026-10-05_1351.zip

- Backup: `/tmp/claude-0/-home-user/50f56c92-2919-5ae3-94c9-0de4476bbe87/scratchpad/dist4/658424_R10_2026-10-05_1351.zip` (sha256 `c31f9b6031af81ce...`)
- am.ini: archive `e:\bmw_03_10_r1.zip\`, date `2026-10-05_14-46-44`, config `All`, robot `BMW_03_10_R1`, serial `658424`, KSS `V8.3.29`
- Compared with: `fb8a4c8` = `fb8a4c8b96` "Add findings, I/O label map and cleanup conventions for R10"; first commit (archive as received) `22a98cc8ef`
- Generated 2026-10-05T19:51:47 by tools/audit_backup.py

## Summary

| | |
|---|---|
| Entries audited (Log Files/ skipped: 8) | 314 |
| Unchanged | 252 |
| Changed | 43 |
| Added | 19 |
| Missing from the backup | 10 |
| **Deleted modules still on the controller** | 0 |
| **Pre-cleanup files** | 0 |
| Edited on top of the pre-cleanup file | 0 |
| KRL files with code changes | 38 |
| Code lines removed / added | 271 / 937 |
| KRL files with comment-only changes | 12 |
| KRL files with runtime values only (written by the program, not edits) | 0 |
| Checks FAIL / WARN / INFO | 0 / 0 / 22 |

**Needs attention:**

- WARN 10 file(s) of the base missing from the backup - deleted on the robot, or an incomplete archive (e.g. C/KRC/User/ProjectRoot/V431-03-10R1_v6Active_Centerline_18/V431-03-10R1_v6Active_Centerline_18.asz; all in Files, "Missing from the backup")
- WARN KRC/R1/Mada/$machine.dat: machine data file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- WARN KRC/R1/TP/AutomationCore/automationcoreroutines.src: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)

## The backup itself

- WARN: 10 file(s) of the base missing from the backup - deleted on the robot, or an incomplete archive (e.g. C/KRC/User/ProjectRoot/V431-03-10R1_v6Active_Centerline_18/V431-03-10R1_v6Active_Centerline_18.asz; all in Files, "Missing from the backup")
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

### Changed (43)

- `C/KRC/Roboter/Config/User/Common/KRC_IO.xml` - controller configuration - 51 line(s) removed, 56 added - diffs/C/KRC/Roboter/Config/User/Common/KRC_IO.xml.diff
- `C/KRC/Roboter/Config/User/Common/KrcIoSignals.xml` - controller configuration - 0 line(s) removed, 16 added - diffs/C/KRC/Roboter/Config/User/Common/KrcIoSignals.xml.diff
- `C/KRC/Roboter/Rdc/RdcDirectoryContents.txt` - controller configuration - 3 line(s) removed, 3 added - diffs/C/KRC/Roboter/Rdc/RdcDirectoryContents.txt.diff
- `C/KRC/Roboter/Rdc/RobotData.xml` - controller configuration - 1 line(s) removed, 1 added - diffs/C/KRC/Roboter/Rdc/RobotData.xml.diff
- `C/KRC/User/ConfigMon.ini` - controller configuration - binary, 2606 bytes
- `C/KRC/User/ProjectRoot/V431-03-10R1_v6Active_Centerline_18/V431-03-10R1_v6Active_Centerline_18.wvs` - controller configuration - binary, 8982528 bytes
- `C/KRC/User/Settings.xml` - controller configuration - 1 line(s) removed, 1 added - diffs/C/KRC/User/Settings.xml.diff
- `KRC/R1/Mada/$machine.dat` - machine data
- `KRC/R1/Mada/$robcor.dat` - machine data
- `KRC/R1/Program/Centerline/CENTERLINE_HOME.src` - integrator program
- `KRC/R1/Program/Centerline/PRELOAD.src` - integrator program
- `KRC/R1/Program/Centerline/Request_next_nut.src` - integrator program
- `KRC/R1/Program/Centerline/centerline_weld.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app2opt1.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app2opt2.dat` - integrator program
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
- `KRC/R1/System/tm_bib.src` - KUKA system / vendor package
- `KRC/R1/TP/AutomationCore/automationcoreroutines.dat` - KUKA system / vendor package
- `KRC/R1/TP/AutomationCore/automationcoreroutines.src` - KUKA system / vendor package
- `KRC/R1/TP/BrakeTest/braketestback.dat` - KUKA system / vendor package
- `KRC/R1/TP/BrakeTest/braketestback.src` - KUKA system / vendor package
- `KRC/R1/TP/BrakeTest/braketestreq.dat` - KUKA system / vendor package
- `KRC/R1/TP/BrakeTest/braketestreq.src` - KUKA system / vendor package
- `KRC/R1/TP/BrakeTest/braketeststart.dat` - KUKA system / vendor package
- `KRC/R1/TP/BrakeTest/braketeststart.src` - KUKA system / vendor package
- `KRC/R1/TP/GripperSpotTech/grp_data.dat` - KUKA system / vendor package
- `KRC/R1/TP/NutWeld/nutweldroutines.dat` - KUKA system / vendor package
- `KRC/R1/cell.src` - integrator program
- `KRC/STEU/Mada/$custom.dat` - machine data
- `Registry/LMSOFTWAREKUKA ROBOTER GMBHWorkVisual.amr` - controller configuration - 5 line(s) removed, 7 added - diffs/Registry/LMSOFTWAREKUKA ROBOTER GMBHWorkVisual.amr.diff
- `am.ini` - archive metadata - 4 line(s) removed, 4 added - diffs/am.ini.diff

### Added (19)

- `C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8.log` - controller configuration - 0 line(s) removed, 342 added - diffs/C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8.log.diff
- `C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8.wvs` - controller configuration - binary, 5566464 bytes
- `C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8_old.log` - controller configuration - 0 line(s) removed, 372 added - diffs/C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8_old.log.diff
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src` - integrator program
- `KRC/R1/Program/Centerline/gun_open_check.dat` - integrator program
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
- `KRC/R1/Program/Styles/Options/Style1Opt10AutoRR.src` - integrator program
- `KRC/R1/Program/Styles/Options/style1opt1.src` - integrator program

### Missing from the backup (10)

- `C/KRC/User/ProjectRoot/V431-03-10R1_v6Active_Centerline_18/V431-03-10R1_v6Active_Centerline_18.asz`
- `KRC/R1/Program/Centerline/centerline_loop.src`
- `KRC/R1/Program/StyleApps/Options/style1app1opt1.dat`
- `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`
- `KRC/R1/Program/StyleApps/Options/style1app1opt2.dat`
- `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`
- `KRC/R1/Program/StyleApps/Options/style1app1opt3.dat`
- `KRC/R1/Program/StyleApps/Options/style1app1opt3.src`
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

added, integrator program: 0 code line(s) removed, 102 added; 51 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src.diff](diffs/KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src.diff)

Attributes: +&ACCESS RVO1; +&REL 2; +&COMMENT 03-10-R1 PNW1 GUN OPEN CHECK; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\Roboter\Template\vorgabe

```diff
@@ base line end, backup line 6 @@
+     6  DEF GUN_OPEN_CHECK( )
+    23  DECL KrlMsg_T Msg
+    24  DECL KrlMsg_T MsgW
+    25  DECL KrlMsgPar_T Par[3]
+    26  DECL KrlMsgOpt_T Opt
+    27  DECL INT nHandle, nWaitMs
+    28  DECL BOOL bRes
+    31  WAIT SEC 0
+    34  Msg.Modul[]="GunOpenCheck"
+    35  MsgW.Modul[]="GunOpenCheck"
+    36  Par[1].Par_Type=#EMPTY
+    37  Par[2].Par_Type=#EMPTY
+    38  Par[3].Par_Type=#EMPTY
+    39  Opt.VL_Stop=TRUE
+    40  Opt.Clear_P_Reset=TRUE
+    41  Opt.Clear_P_SAW=FALSE
+    42  Opt.Log_To_DB=TRUE
+    46  IF $PRO_STATE0<>#P_ACTIVE THEN
+    47  Msg.Nr=1
+    48  Msg.Msg_txt[]="Submit (SPS) not running - gun position not valid - robot waiting"
+    49  Par[1].Par_Type=#EMPTY
+    50  nHandle=Set_KrlMsg(#STATE, Msg, Par[], Opt)
+    51  WAIT FOR $PRO_STATE0==#P_ACTIVE
+    52  bRes=Clear_KrlMsg(nHandle)
+    54  WAIT SEC 0.5
+    55  ENDIF
+    58  IF bGunAirCheck THEN
+    60  IF NOT dipw1_AirOK THEN
+    61  Msg.Nr=3
+    62  Msg.Msg_txt[]="Nut welder air pressure not OK (dipw1_AirOK) - robot waiting"
+    63  Par[1].Par_Type=#EMPTY
+    64  nHandle=Set_KrlMsg(#STATE, Msg, Par[], Opt)
+    66  WAIT FOR dipw1_AirOK
+    67  bRes=Clear_KrlMsg(nHandle)
+    68  ENDIF
+    69  ENDIF
+    72  IF bGunWaterCheck THEN
+    73  IF NOT dipw1_WaterOk THEN
+    74  MsgW.Nr=6
+    75  MsgW.Msg_txt[]="Nut welder cooling water flow too low (%1 x0.1 l/min) - robot waiting"
+    76  Par[1].Par_Type=#VALUE
+    77  Par[1].Par_Int=nWaterFlow
+    78  nHandle=Set_KrlMsg(#STATE, MsgW, Par[], Opt)
+    79  WAIT FOR dipw1_WaterOk
+    80  bRes=Clear_KrlMsg(nHandle)
+    81  Par[1].Par_Type=#EMPTY
+    82  ENDIF
+    83  ENDIF
+    86  nWaitMs=0
+    87  WHILE ((CL_GunStrokePositionLPT<nGunOpenMin) OR (CL_GunStrokePositionLPT>nGunOpenMax)) AND (nWaitMs<nGunOpenWaitMs)
+    88  WAIT SEC 0.05
+    89  nWaitMs=nWaitMs+50
+    90  ENDWHILE
+    93  IF (CL_GunStrokePositionLPT<nGunOpenMin) OR (CL_GunStrokePositionLPT>nGunOpenMax) THEN
+    94  Msg.Nr=2
+    95  Msg.Msg_txt[]="Nut welder gun not open (position %1) - robot waiting"
+    96  Par[1].Par_Type=#VALUE
+    97  Par[1].Par_Int=CL_GunStrokePositionLPT
+    98  nHandle=Set_KrlMsg(#STATE, Msg, Par[], Opt)
```
_43 more lines: see diffs/KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src.diff_

### `KRC/R1/Program/Centerline/PRELOAD.src`

changed, integrator program: 30 code line(s) removed, 30 added; 230 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/PRELOAD.src.diff](diffs/KRC/R1/Program/Centerline/PRELOAD.src.diff)

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

changed, integrator program: 2 code line(s) removed, 2 added; 8 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/Request_next_nut.src.diff](diffs/KRC/R1/Program/Centerline/Request_next_nut.src.diff)

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

changed, integrator program: 73 code line(s) removed, 65 added; 193 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/centerline_weld.src.diff](diffs/KRC/R1/Program/Centerline/centerline_weld.src.diff)

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

### `KRC/R1/Program/StyleApps/Options/style1app1opt1A.dat`

added, integrator program: 0 code line(s) removed, 23 added; 18 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1A.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1A.dat.diff)

Attributes: +&ACCESS RVO1; +&REL 339; +&COMMENT NUT1; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\TP\Nutweld\Template\NutWeld_Vorgabe; +&PARAM DISKPATH = KRC:\R1\Program\StyleApps\Options

Data changes:

- added 1 BASIS_SUGG_T: LAST_BASIS
- added 1 DEFDAT: style1app1opt1A
- added 5 E6POS: XP0, XP8, XP19, XP20, XPNW1
- added 1 EXT: BAS
- added 5 FDAT: FP0, FP8, FP19, FP20, FPNW1
- added 5 LDAT: LCPDAT8, LCPDAT12, LCPDAT16, LCPDAT17, LCPDAT18
- added 1 MODULEPARAM_T: LAST_TP_PARAMS
- added 1 NUTWELD_SUGG_T: LAST_NutWeld
- added 2 PDAT: PPDAT0, PPDAT18

```diff
@@ base line end, backup line 7 @@
+     7  DEFDAT style1app1opt1A
+    10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
+    17  DECL E6POS XP20={X -3850.82104,Y -108.397034,Z -435.544800,A -178.432037,B 0.654220462,C -179.967712,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    18  DECL FDAT FP20={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    28  DECL FDAT FPNW1={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    29  DECL E6POS XPNW1={X 123.774101,Y 312.995331,Z -88.6478,A 8.71582699,B 8.82717705,C 1.11576855,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    30  DECL NutWeld_SUGG_T LAST_NutWeld={POINT1[] "PNW1_SPOT7              ",POINT2[] "PNW0                    ",CP_PARAMS[] "CPDATNutWeld0           ",PTP_PARAMS[] "PDATNutWeld0            ",CONT[] "C_PTP                   ",CP_VEL[] "2  [...]
+    31  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P0                      ",POINT2[] "P0                      ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT0                   ",CONT[] "                        ",CP_VEL[] "2      [...]
+    32  DECL PDAT PPDAT0={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    33  DECL E6POS XP0={X -3704.29346,Y 1.10223198,Z -449.805786,A -178.368118,B 0.266879767,C 179.968445,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    34  DECL FDAT FP0={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    35  DECL MODULEPARAM_T LAST_TP_PARAMS={PARAMS[] "NutWeld_CmdPos=Weld; NutWeld_Move=LIN; NutWeld_NutWeldDat=NutData1_7; NutWeld_NWGunNr=1; NutWeld_NWSpotNr=7; NutWeld_NWOffset=45; Kuka.MoveDataName=gAboveWeld; Kuka.VelocityPath=2; Kuka. [...]
+    36  DECL E6POS XP8={X -3704.29346,Y 1.10223198,Z -449.805786,A -178.368118,B 0.266879767,C 179.968445,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    37  DECL FDAT FP8={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    38  DECL LDAT LCPDAT8={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    39  DECL LDAT LCPDAT12={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    40  DECL LDAT LCPDAT16={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    41  DECL LDAT LCPDAT17={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    42  DECL PDAT PPDAT18={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    43  DECL E6POS XP19={X -3851.81445,Y -107.010963,Z -442.857483,A -178.432037,B 0.654220223,C -179.967712,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    44  DECL FDAT FP19={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    45  DECL LDAT LCPDAT18={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    46  ENDDAT
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt1A.src`

added, integrator program: 0 code line(s) removed, 64 added; 71 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1A.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1A.src.diff)

Attributes: +&ACCESS RVO1; +&REL 339; +&COMMENT 03-10-R1 PNW1 NUT 1 ST1; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\TP\Nutweld\Template\NutWeld_Vorgabe; +&PARAM DISKPATH = KRC:\R1\Program\StyleApps\Options

```diff
@@ base line end, backup line 7 @@
+     7  DEF style1app1opt1A( )
+    10  GLOBAL INTERRUPT DECL 3 WHEN $STOPMESS==TRUE DO IR_STOPM ( )
+    11  INTERRUPT ON 3
+    12  BAS (#INITMOV,0 )
+    37  $BWDSTART=FALSE
+    38  PDAT_ACT=PPDAT0
+    39  FDAT_ACT=FP0
+    40  BAS(#PTP_PARAMS,100)
+    41  PTP XP0 C_DIS
+    44  $BWDSTART=FALSE
+    45  LDAT_ACT=LCPDAT12
+    46  FDAT_ACT=FP8
+    47  BAS(#CP_PARAMS,2)
+    48  LIN XP8 C_DIS C_DIS
+    55  INTERRUPT DECL 20 WHEN CL_GunStrokePositionLPT<137000 DO GUN_OPEN_LOST()
+    56  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
+    57  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
+    62  WAIT FOR NUT_READY== TRUE
+    65  INTERRUPT ON 20
+    66  INTERRUPT ON 21
+    67  INTERRUPT ON 22
+    68  GUN_OPEN_CHECK()
+    72  $BWDSTART=FALSE
+    73  LDAT_ACT=LCPDAT8
+    74  FDAT_ACT=FP20
+    75  BAS(#CP_PARAMS,2)
+    76  LIN XP20 C_DIS C_DIS
+    82  IF NOT di004UseDryCycle THEN
+    84  $BWDSTART=FALSE
+    85  LDAT_ACT=LCPDAT18
+    86  FDAT_ACT=FP19
+    87  BAS(#CP_PARAMS,2)
+    88  LIN XP19
+    92  WAIT SEC 0
+    93  INTERRUPT OFF 20
+    94  INTERRUPT OFF 21
+    95  INTERRUPT OFF 22
+    97  CENTERLINE_WELD()
+   100  INTERRUPT ON 20
+   101  INTERRUPT ON 21
+   102  INTERRUPT ON 22
+   103  GUN_OPEN_CHECK()
+   104  ENDIF
+   108  $BWDSTART=FALSE
+   109  LDAT_ACT=LCPDAT16
+   110  FDAT_ACT=FP20
+   111  BAS(#CP_PARAMS,2)
+   112  LIN XP20 C_DIS C_DIS
+   116  WAIT SEC 0
+   117  INTERRUPT OFF 20
+   118  INTERRUPT OFF 21
+   119  INTERRUPT OFF 22
+   122  $BWDSTART=FALSE
+   123  LDAT_ACT=LCPDAT17
+   124  FDAT_ACT=FP8
+   125  BAS(#CP_PARAMS,2)
+   126  LIN XP8 C_DIS C_DIS
+   133  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO Request_next_nut() PRIO= -1
+   135  $BWDSTART=FALSE
```
_5 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1A.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt1B.dat`

added, integrator program: 0 code line(s) removed, 23 added; 18 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1B.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1B.dat.diff)

Attributes: +&ACCESS RVO1; +&REL 339; +&COMMENT NUT1; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\TP\Nutweld\Template\NutWeld_Vorgabe; +&PARAM DISKPATH = KRC:\R1\Program\StyleApps\Options

Data changes:

- added 1 BASIS_SUGG_T: LAST_BASIS
- added 1 DEFDAT: style1app1opt1B
- added 5 E6POS: XP0, XP8, XP19, XP20, XPNW1
- added 1 EXT: BAS
- added 5 FDAT: FP0, FP8, FP19, FP20, FPNW1
- added 5 LDAT: LCPDAT8, LCPDAT12, LCPDAT16, LCPDAT17, LCPDAT18
- added 1 MODULEPARAM_T: LAST_TP_PARAMS
- added 1 NUTWELD_SUGG_T: LAST_NutWeld
- added 2 PDAT: PPDAT0, PPDAT18

```diff
@@ base line end, backup line 7 @@
+     7  DEFDAT style1app1opt1B
+    10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
+    17  DECL E6POS XP20={X -3850.82104,Y -108.397034,Z -430.314789,A -178.432037,B 0.654220343,C -179.967712,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    18  DECL FDAT FP20={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    28  DECL FDAT FPNW1={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    29  DECL E6POS XPNW1={X 123.774101,Y 312.995331,Z -88.6478,A 8.71582699,B 8.82717705,C 1.11576855,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    30  DECL NutWeld_SUGG_T LAST_NutWeld={POINT1[] "PNW1_SPOT7              ",POINT2[] "PNW0                    ",CP_PARAMS[] "CPDATNutWeld0           ",PTP_PARAMS[] "PDATNutWeld0            ",CONT[] "C_PTP                   ",CP_VEL[] "2  [...]
+    31  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P0                      ",POINT2[] "P0                      ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT0                   ",CONT[] "                        ",CP_VEL[] "2      [...]
+    32  DECL PDAT PPDAT0={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    33  DECL E6POS XP0={X -3704.29346,Y 1.10223198,Z -449.805786,A -178.368118,B 0.266879767,C 179.968445,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    34  DECL FDAT FP0={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    35  DECL MODULEPARAM_T LAST_TP_PARAMS={PARAMS[] "NutWeld_CmdPos=Weld; NutWeld_Move=LIN; NutWeld_NutWeldDat=NutData1_7; NutWeld_NWGunNr=1; NutWeld_NWSpotNr=7; NutWeld_NWOffset=45; Kuka.MoveDataName=gAboveWeld; Kuka.VelocityPath=2; Kuka. [...]
+    36  DECL E6POS XP8={X -3704.29346,Y 1.10223198,Z -449.805786,A -178.368118,B 0.266879767,C 179.968445,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    37  DECL FDAT FP8={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    38  DECL LDAT LCPDAT8={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    39  DECL LDAT LCPDAT12={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    40  DECL LDAT LCPDAT16={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    41  DECL LDAT LCPDAT17={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    42  DECL PDAT PPDAT18={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    43  DECL E6POS XP19={X -3849.93530,Y -106.544395,Z -442.889893,A -178.432037,B 0.654220402,C -179.967712,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    44  DECL FDAT FP19={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    45  DECL LDAT LCPDAT18={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    46  ENDDAT
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt1B.src`

added, integrator program: 0 code line(s) removed, 64 added; 71 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1B.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1B.src.diff)

Attributes: +&ACCESS RVO1; +&REL 339; +&COMMENT 03-10-R1 PNW1 NUT 1 ST2; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\TP\Nutweld\Template\NutWeld_Vorgabe; +&PARAM DISKPATH = KRC:\R1\Program\StyleApps\Options

```diff
@@ base line end, backup line 7 @@
+     7  DEF style1app1opt1B( )
+    10  GLOBAL INTERRUPT DECL 3 WHEN $STOPMESS==TRUE DO IR_STOPM ( )
+    11  INTERRUPT ON 3
+    12  BAS (#INITMOV,0 )
+    37  $BWDSTART=FALSE
+    38  PDAT_ACT=PPDAT0
+    39  FDAT_ACT=FP0
+    40  BAS(#PTP_PARAMS,100)
+    41  PTP XP0 C_DIS
+    44  $BWDSTART=FALSE
+    45  LDAT_ACT=LCPDAT12
+    46  FDAT_ACT=FP8
+    47  BAS(#CP_PARAMS,2)
+    48  LIN XP8 C_DIS C_DIS
+    55  INTERRUPT DECL 20 WHEN CL_GunStrokePositionLPT<137000 DO GUN_OPEN_LOST()
+    56  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
+    57  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
+    62  WAIT FOR NUT_READY== TRUE
+    65  INTERRUPT ON 20
+    66  INTERRUPT ON 21
+    67  INTERRUPT ON 22
+    68  GUN_OPEN_CHECK()
+    72  $BWDSTART=FALSE
+    73  LDAT_ACT=LCPDAT8
+    74  FDAT_ACT=FP20
+    75  BAS(#CP_PARAMS,2)
+    76  LIN XP20 C_DIS C_DIS
+    82  IF NOT di004UseDryCycle THEN
+    84  $BWDSTART=FALSE
+    85  LDAT_ACT=LCPDAT18
+    86  FDAT_ACT=FP19
+    87  BAS(#CP_PARAMS,2)
+    88  LIN XP19
+    92  WAIT SEC 0
+    93  INTERRUPT OFF 20
+    94  INTERRUPT OFF 21
+    95  INTERRUPT OFF 22
+    97  CENTERLINE_WELD()
+   100  INTERRUPT ON 20
+   101  INTERRUPT ON 21
+   102  INTERRUPT ON 22
+   103  GUN_OPEN_CHECK()
+   104  ENDIF
+   108  $BWDSTART=FALSE
+   109  LDAT_ACT=LCPDAT16
+   110  FDAT_ACT=FP20
+   111  BAS(#CP_PARAMS,2)
+   112  LIN XP20 C_DIS C_DIS
+   116  WAIT SEC 0
+   117  INTERRUPT OFF 20
+   118  INTERRUPT OFF 21
+   119  INTERRUPT OFF 22
+   122  $BWDSTART=FALSE
+   123  LDAT_ACT=LCPDAT17
+   124  FDAT_ACT=FP8
+   125  BAS(#CP_PARAMS,2)
+   126  LIN XP8 C_DIS C_DIS
+   133  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO Request_next_nut() PRIO= -1
+   135  $BWDSTART=FALSE
```
_5 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1B.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt2A.dat`

added, integrator program: 0 code line(s) removed, 27 added; 11 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2A.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2A.dat.diff)

Attributes: +&ACCESS RVO1; +&REL 246; +&COMMENT GE4_002_GUN1; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\TP\Nutweld\Template\NutWeld_Vorgabe; +&PARAM DISKPATH = KRC:\R1\Program\StyleApps\Options

Data changes:

- added 1 BASIS_SUGG_T: LAST_BASIS
- added 1 DEFDAT: style1app1opt2A
- added 7 E6POS: XP0, XP05, XP5, XP6, XP06, XP16, XPnw1
- added 1 EXT: BAS
- added 7 FDAT: FP0, Fp05, FP5, FP06, FP6, FP16, FPnw1
- added 6 LDAT: LCPDAT0, LCPDAT6, LCPDAT11, LCPDAT14, LCPDAT15, Lpnw1
- added 1 NUTWELD_SUGG_T: LAST_NutWeld
- added 2 PDAT: PPDAT0, PPDAT26

```diff
@@ base line end, backup line 7 @@
+     7  DEFDAT style1app1opt2A
+    10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
+    18  DECL NutWeld_SUGG_T LAST_NutWeld={POINT1[] "PNW2_SPOT3              ",POINT2[] "PNW0                    ",CP_PARAMS[] "CPDATNutWeld0           ",PTP_PARAMS[] "PDATNutWeld0            ",CONT[] "C_PTP                   ",CP_VEL[] "2  [...]
+    19  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P0                      ",POINT2[] "P0                      ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT0                   ",CONT[] "                        ",CP_VEL[] "2      [...]
+    20  DECL LDAT Lpnw1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    21  DECL E6POS XPnw1={X -681.099854,Y -933.961731,Z 7.00223589,A -84.9330902,B -1.72864902,C -2.54664612,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    22  DECL FDAT FPnw1={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    24  DECL PDAT PPDAT0={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    25  DECL E6POS XP0={X -3694.69214,Y 46.1868858,Z -495.861603,A -178.336945,B 1.01745069,C 179.989838,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    26  DECL FDAT FP0={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    27  DECL E6POS XP5={X -3700.01831,Y -153.317429,Z -426.154480,A -178.336502,B -1.01672721,C 179.960312,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    28  DECL FDAT FP5={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    29  DECL LDAT LCPDAT0={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    30  DECL E6POS XP6={X -3883.74512,Y -155.081940,Z -431.860352,A -178.336502,B -1.01672721,C 179.960312,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    31  DECL FDAT FP6={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    32  DECL E6POS XP06={X -3878.33521,Y 42.6205063,Z -500.728149,A -178.336945,B 1.01745081,C 179.989838,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    33  DECL FDAT FP06={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    34  DECL E6POS XP05={X -3700.01831,Y -153.317429,Z -430.255676,A -178.336502,B -1.01672721,C 179.960312,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    35  DECL FDAT Fp05={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    36  DECL LDAT LCPDAT6={VEL 2.00000,ACC 100.000,APO_DIST 2.00000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    37  DECL PDAT PPDAT26={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    38  DECL LDAT LCPDAT11={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    39  DECL LDAT LCPDAT14={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    40  DECL E6POS XP16={X -3884.30103,Y -154.162430,Z -439.919525,A -178.336502,B -1.01672733,C 179.960312,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    41  DECL FDAT FP16={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    42  DECL LDAT LCPDAT15={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    43  ENDDAT
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt2A.src`

added, integrator program: 0 code line(s) removed, 64 added; 67 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2A.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2A.src.diff)

Attributes: +&ACCESS RVO1; +&REL 246; +&COMMENT 03-10-R1 PNW1 NUT 2 ST1; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\TP\Nutweld\Template\NutWeld_Vorgabe; +&PARAM DISKPATH = KRC:\R1\Program\StyleApps\Options

```diff
@@ base line end, backup line 7 @@
+     7  DEF style1app1opt2A( )
+    10  GLOBAL INTERRUPT DECL 3 WHEN $STOPMESS==TRUE DO IR_STOPM ( )
+    11  INTERRUPT ON 3
+    12  BAS (#INITMOV,0 )
+    36  $BWDSTART=FALSE
+    37  PDAT_ACT=PPDAT0
+    38  FDAT_ACT=FP0
+    39  BAS(#PTP_PARAMS,100)
+    40  PTP XP0 C_DIS
+    43  $BWDSTART=FALSE
+    44  LDAT_ACT=LCPDAT11
+    45  FDAT_ACT=FP5
+    46  BAS(#CP_PARAMS,2)
+    47  LIN XP5
+    54  INTERRUPT DECL 20 WHEN CL_GunStrokePositionLPT<137000 DO GUN_OPEN_LOST()
+    55  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
+    56  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
+    59  WAIT FOR NEXT_NUT_READY==TRUE
+    62  INTERRUPT ON 20
+    63  INTERRUPT ON 21
+    64  INTERRUPT ON 22
+    65  GUN_OPEN_CHECK()
+    68  $BWDSTART=FALSE
+    69  LDAT_ACT=LCPDAT0
+    70  FDAT_ACT=FP6
+    71  BAS(#CP_PARAMS,2)
+    72  LIN XP6
+    78  IF NOT di004UseDryCycle THEN
+    80  $BWDSTART=FALSE
+    81  LDAT_ACT=LCPDAT15
+    82  FDAT_ACT=FP16
+    83  BAS(#CP_PARAMS,2)
+    84  LIN XP16
+    88  WAIT SEC 0
+    89  INTERRUPT OFF 20
+    90  INTERRUPT OFF 21
+    91  INTERRUPT OFF 22
+    93  CENTERLINE_WELD()
+    96  INTERRUPT ON 20
+    97  INTERRUPT ON 21
+    98  INTERRUPT ON 22
+    99  GUN_OPEN_CHECK()
+   100  ENDIF
+   103  $BWDSTART=FALSE
+   104  LDAT_ACT=LCPDAT6
+   105  FDAT_ACT=FP06
+   106  BAS(#CP_PARAMS,2)
+   107  LIN XP06 C_DIS C_DIS
+   111  WAIT SEC 0
+   112  INTERRUPT OFF 20
+   113  INTERRUPT OFF 21
+   114  INTERRUPT OFF 22
+   116  $BWDSTART=FALSE
+   117  LDAT_ACT=LCPDAT14
+   118  FDAT_ACT=FP05
+   119  BAS(#CP_PARAMS,2)
+   120  LIN XP05
+   127  TRIGGER WHEN DISTANCE = 1 DELAY = 0 DO Request_next_nut() PRIO= -1
+   129  $BWDSTART=FALSE
```
_5 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2A.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt2B.dat`

added, integrator program: 0 code line(s) removed, 27 added; 11 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2B.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2B.dat.diff)

Attributes: +&ACCESS RVO1; +&REL 246; +&COMMENT GE4_002_GUN1; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\TP\Nutweld\Template\NutWeld_Vorgabe; +&PARAM DISKPATH = KRC:\R1\Program\StyleApps\Options

Data changes:

- added 1 BASIS_SUGG_T: LAST_BASIS
- added 1 DEFDAT: style1app1opt2B
- added 7 E6POS: XP0, XP05, XP5, XP6, XP06, XP16, XPnw1
- added 1 EXT: BAS
- added 7 FDAT: FP0, Fp05, FP5, FP06, FP6, FP16, FPnw1
- added 6 LDAT: LCPDAT0, LCPDAT6, LCPDAT11, LCPDAT14, LCPDAT15, Lpnw1
- added 1 NUTWELD_SUGG_T: LAST_NutWeld
- added 2 PDAT: PPDAT0, PPDAT26

```diff
@@ base line end, backup line 7 @@
+     7  DEFDAT style1app1opt2B
+    10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
+    18  DECL NutWeld_SUGG_T LAST_NutWeld={POINT1[] "PNW2_SPOT3              ",POINT2[] "PNW0                    ",CP_PARAMS[] "CPDATNutWeld0           ",PTP_PARAMS[] "PDATNutWeld0            ",CONT[] "C_PTP                   ",CP_VEL[] "2  [...]
+    19  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P0                      ",POINT2[] "P0                      ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT0                   ",CONT[] "                        ",CP_VEL[] "2      [...]
+    20  DECL LDAT Lpnw1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    21  DECL E6POS XPnw1={X -681.099854,Y -933.961731,Z 7.00223589,A -84.9330902,B -1.72864902,C -2.54664612,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    22  DECL FDAT FPnw1={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    24  DECL PDAT PPDAT0={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    25  DECL E6POS XP0={X -3694.69214,Y 46.1868858,Z -495.861603,A -178.336945,B 1.01745069,C 179.989838,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    26  DECL FDAT FP0={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    27  DECL E6POS XP5={X -3700.01831,Y -153.317429,Z -426.154480,A -178.336502,B -1.01672721,C 179.960312,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    28  DECL FDAT FP5={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    29  DECL LDAT LCPDAT0={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    30  DECL E6POS XP6={X -3883.74512,Y -155.081940,Z -431.860352,A -178.336502,B -1.01672721,C 179.960312,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    31  DECL FDAT FP6={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    32  DECL E6POS XP06={X -3878.33521,Y 42.6205063,Z -500.728149,A -178.336945,B 1.01745081,C 179.989838,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    33  DECL FDAT FP06={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    34  DECL E6POS XP05={X -3700.01831,Y -153.317429,Z -430.255676,A -178.336502,B -1.01672721,C 179.960312,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    35  DECL FDAT Fp05={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    36  DECL LDAT LCPDAT6={VEL 2.00000,ACC 100.000,APO_DIST 2.00000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    37  DECL PDAT PPDAT26={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    38  DECL LDAT LCPDAT11={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    39  DECL LDAT LCPDAT14={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    40  DECL E6POS XP16={X -3882.34546,Y -153.988113,Z -439.433533,A -178.336502,B -1.01672721,C 179.960312,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    41  DECL FDAT FP16={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    42  DECL LDAT LCPDAT15={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    43  ENDDAT
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt2B.src`

added, integrator program: 0 code line(s) removed, 64 added; 67 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2B.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2B.src.diff)

Attributes: +&ACCESS RVO1; +&REL 246; +&COMMENT 03-10-R1 PNW1 NUT 2 ST2; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\TP\Nutweld\Template\NutWeld_Vorgabe; +&PARAM DISKPATH = KRC:\R1\Program\StyleApps\Options

```diff
@@ base line end, backup line 7 @@
+     7  DEF style1app1opt2B( )
+    10  GLOBAL INTERRUPT DECL 3 WHEN $STOPMESS==TRUE DO IR_STOPM ( )
+    11  INTERRUPT ON 3
+    12  BAS (#INITMOV,0 )
+    36  $BWDSTART=FALSE
+    37  PDAT_ACT=PPDAT0
+    38  FDAT_ACT=FP0
+    39  BAS(#PTP_PARAMS,100)
+    40  PTP XP0 C_DIS
+    43  $BWDSTART=FALSE
+    44  LDAT_ACT=LCPDAT11
+    45  FDAT_ACT=FP5
+    46  BAS(#CP_PARAMS,2)
+    47  LIN XP5
+    54  INTERRUPT DECL 20 WHEN CL_GunStrokePositionLPT<137000 DO GUN_OPEN_LOST()
+    55  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
+    56  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
+    59  WAIT FOR NEXT_NUT_READY==TRUE
+    62  INTERRUPT ON 20
+    63  INTERRUPT ON 21
+    64  INTERRUPT ON 22
+    65  GUN_OPEN_CHECK()
+    68  $BWDSTART=FALSE
+    69  LDAT_ACT=LCPDAT0
+    70  FDAT_ACT=FP6
+    71  BAS(#CP_PARAMS,2)
+    72  LIN XP6
+    78  IF NOT di004UseDryCycle THEN
+    80  $BWDSTART=FALSE
+    81  LDAT_ACT=LCPDAT15
+    82  FDAT_ACT=FP16
+    83  BAS(#CP_PARAMS,2)
+    84  LIN XP16
+    88  WAIT SEC 0
+    89  INTERRUPT OFF 20
+    90  INTERRUPT OFF 21
+    91  INTERRUPT OFF 22
+    93  CENTERLINE_WELD()
+    96  INTERRUPT ON 20
+    97  INTERRUPT ON 21
+    98  INTERRUPT ON 22
+    99  GUN_OPEN_CHECK()
+   100  ENDIF
+   103  $BWDSTART=FALSE
+   104  LDAT_ACT=LCPDAT6
+   105  FDAT_ACT=FP06
+   106  BAS(#CP_PARAMS,2)
+   107  LIN XP06 C_DIS C_DIS
+   111  WAIT SEC 0
+   112  INTERRUPT OFF 20
+   113  INTERRUPT OFF 21
+   114  INTERRUPT OFF 22
+   116  $BWDSTART=FALSE
+   117  LDAT_ACT=LCPDAT14
+   118  FDAT_ACT=FP05
+   119  BAS(#CP_PARAMS,2)
+   120  LIN XP05
+   127  TRIGGER WHEN DISTANCE = 1 DELAY = 0 DO Request_next_nut() PRIO= -1
+   129  $BWDSTART=FALSE
```
_5 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2B.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt3A.dat`

added, integrator program: 0 code line(s) removed, 25 added; 10 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3A.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3A.dat.diff)

Attributes: +&ACCESS RVO1; +&REL 227; +&COMMENT GE4_003_GUN1; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\TP\Nutweld\Template\NutWeld_Vorgabe; +&PARAM DISKPATH = KRC:\R1\Program\StyleApps\Options

Data changes:

- added 1 BASIS_SUGG_T: LAST_BASIS
- added 1 DEFDAT: style1app1opt3A
- added 6 E6POS: XP7, XP13, XP16, XP17, XP20, XPNW1
- added 1 EXT: BAS
- added 6 FDAT: FP7, FP13, FP16, FP17, FP20, FPNW1
- added 6 LDAT: LCPDAT4, LCPDAT6, LCPDAT10, LCPDAT11, LCPDAT12, Lpnw1
- added 1 MODULEPARAM_T: LAST_TP_PARAMS
- added 1 NUTWELD_SUGG_T: LAST_NutWeld
- added 1 PDAT: PPDAT25

```diff
@@ base line end, backup line 7 @@
+     7  DEFDAT style1app1opt3A
+    10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
+    17  DECL E6POS XP20={X -3678.25781,Y -44.2650108,Z -442.362579,A -178.367340,B 0.267035842,C 179.968063,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    18  DECL FDAT FP20={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    20  DECL FDAT FPNW1={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    21  DECL E6POS XPNW1={X -684.340210,Y -936.680359,Z 6.96372366,A -85.0124512,B -3.00309157,C -5.37728167,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    22  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P18                     ",POINT2[] "P18                     ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT26                  ",CONT[] "                        ",CP_VEL[] "2      [...]
+    23  DECL NutWeld_SUGG_T LAST_NutWeld={POINT1[] "PNW3_SPOT03             ",POINT2[] "PNW0                    ",CP_PARAMS[] "CPDATNutWeld0           ",PTP_PARAMS[] "PDATNutWeld0            ",CONT[] "C_PTP                   ",CP_VEL[] "2  [...]
+    24  DECL MODULEPARAM_T LAST_TP_PARAMS={PARAMS[] "NutWeld_CmdPos=Weld; NutWeld_Move=LIN; NutWeld_NutWeldDat=NutWeldDAT1; NutWeld_NWGunNr=3; NutWeld_NWSpotNr=3; NutWeld_NWOffset=0; Kuka.MoveDataName=CPDAT2; Kuka.VelocityPath=2; Kuka.Poin [...]
+    25  DECL LDAT Lpnw1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    26  DECL E6POS XP7={X -3596.62695,Y -2.77881479,Z -444.531586,A -178.368134,B 0.266892016,C 179.968369,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    27  DECL FDAT FP7={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    28  DECL E6POS XP13={X -3882.93384,Y -48.4484138,Z -446.836792,A -178.367340,B 0.267035872,C 179.968063,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    29  DECL FDAT FP13={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    30  DECL LDAT LCPDAT4={VEL 2.00000,ACC 100.000,APO_DIST 2.00000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    31  DECL PDAT PPDAT25={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    32  DECL LDAT LCPDAT6={VEL 2.00000,ACC 100.000,APO_DIST 2.00000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    33  DECL LDAT LCPDAT10={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    34  DECL E6POS XP16={X -3885.41455,Y -60.8571358,Z -438.795197,A -178.367233,B -0.684153676,C 179.983429,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    35  DECL FDAT FP16={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    36  DECL LDAT LCPDAT11={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    37  DECL E6POS XP17={X -3884.77832,Y -61.9626274,Z -428.770508,A -178.367172,B -0.266017497,C 179.960464,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    38  DECL FDAT FP17={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    39  DECL LDAT LCPDAT12={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    40  ENDDAT
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt3A.src`

added, integrator program: 0 code line(s) removed, 58 added; 62 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3A.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3A.src.diff)

Attributes: +&ACCESS RVO1; +&REL 227; +&COMMENT 03-10-R1 PNW1 NUT 3 ST1; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\TP\Nutweld\Template\NutWeld_Vorgabe; +&PARAM DISKPATH = KRC:\R1\Program\StyleApps\Options

```diff
@@ base line end, backup line 7 @@
+     7  DEF style1app1opt3A( )
+    10  GLOBAL INTERRUPT DECL 3 WHEN $STOPMESS==TRUE DO IR_STOPM ( )
+    11  INTERRUPT ON 3
+    12  BAS (#INITMOV,0 )
+    37  $BWDSTART=FALSE
+    38  LDAT_ACT=LCPDAT6
+    39  FDAT_ACT=FP20
+    40  BAS(#CP_PARAMS,2)
+    41  LIN XP20 C_DIS C_DIS
+    48  INTERRUPT DECL 20 WHEN CL_GunStrokePositionLPT<137000 DO GUN_OPEN_LOST()
+    49  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
+    50  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
+    53  WAIT FOR NEXT_NUT_READY==TRUE
+    56  INTERRUPT ON 20
+    57  INTERRUPT ON 21
+    58  INTERRUPT ON 22
+    59  GUN_OPEN_CHECK()
+    62  $BWDSTART=FALSE
+    63  LDAT_ACT=LCPDAT4
+    64  FDAT_ACT=FP13
+    65  BAS(#CP_PARAMS,2)
+    66  LIN XP13 C_DIS C_DIS
+    72  IF NOT di004UseDryCycle THEN
+    74  $BWDSTART=FALSE
+    75  LDAT_ACT=LCPDAT11
+    76  FDAT_ACT=FP16
+    77  BAS(#CP_PARAMS,2)
+    78  LIN XP16
+    82  WAIT SEC 0
+    83  INTERRUPT OFF 20
+    84  INTERRUPT OFF 21
+    85  INTERRUPT OFF 22
+    87  CENTERLINE_WELD()
+    90  INTERRUPT ON 20
+    91  INTERRUPT ON 21
+    92  INTERRUPT ON 22
+    93  GUN_OPEN_CHECK()
+    94  ENDIF
+    97  $BWDSTART=FALSE
+    98  LDAT_ACT=LCPDAT12
+    99  FDAT_ACT=FP17
+   100  BAS(#CP_PARAMS,2)
+   101  LIN XP17
+   105  WAIT SEC 0
+   106  INTERRUPT OFF 20
+   107  INTERRUPT OFF 21
+   108  INTERRUPT OFF 22
+   110  $BWDSTART=FALSE
+   111  LDAT_ACT=LCPDAT10
+   112  FDAT_ACT=FP20
+   113  BAS(#CP_PARAMS,2)
+   114  LIN XP20
+   118  $BWDSTART=FALSE
+   119  PDAT_ACT=PPDAT25
+   120  FDAT_ACT=FP7
+   121  BAS(#PTP_PARAMS,60)
+   122  PTP XP7
+   126  END
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt3B.dat`

added, integrator program: 0 code line(s) removed, 25 added; 10 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3B.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3B.dat.diff)

Attributes: +&ACCESS RVO1; +&REL 227; +&COMMENT GE4_003_GUN1; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\TP\Nutweld\Template\NutWeld_Vorgabe; +&PARAM DISKPATH = KRC:\R1\Program\StyleApps\Options

Data changes:

- added 1 BASIS_SUGG_T: LAST_BASIS
- added 1 DEFDAT: style1app1opt3B
- added 6 E6POS: XP7, XP13, XP16, XP17, XP20, XPNW1
- added 1 EXT: BAS
- added 6 FDAT: FP7, FP13, FP16, FP17, FP20, FPNW1
- added 6 LDAT: LCPDAT4, LCPDAT6, LCPDAT10, LCPDAT11, LCPDAT12, Lpnw1
- added 1 MODULEPARAM_T: LAST_TP_PARAMS
- added 1 NUTWELD_SUGG_T: LAST_NutWeld
- added 1 PDAT: PPDAT25

```diff
@@ base line end, backup line 7 @@
+     7  DEFDAT style1app1opt3B
+    10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
+    17  DECL E6POS XP20={X -3678.25781,Y -44.2650108,Z -442.362579,A -178.367340,B 0.267035842,C 179.968063,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    18  DECL FDAT FP20={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    20  DECL FDAT FPNW1={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    21  DECL E6POS XPNW1={X -684.340210,Y -936.680359,Z 6.96372366,A -85.0124512,B -3.00309157,C -5.37728167,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    22  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P18                     ",POINT2[] "P18                     ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT26                  ",CONT[] "                        ",CP_VEL[] "2      [...]
+    23  DECL NutWeld_SUGG_T LAST_NutWeld={POINT1[] "PNW3_SPOT03             ",POINT2[] "PNW0                    ",CP_PARAMS[] "CPDATNutWeld0           ",PTP_PARAMS[] "PDATNutWeld0            ",CONT[] "C_PTP                   ",CP_VEL[] "2  [...]
+    24  DECL MODULEPARAM_T LAST_TP_PARAMS={PARAMS[] "NutWeld_CmdPos=Weld; NutWeld_Move=LIN; NutWeld_NutWeldDat=NutWeldDAT1; NutWeld_NWGunNr=3; NutWeld_NWSpotNr=3; NutWeld_NWOffset=0; Kuka.MoveDataName=CPDAT2; Kuka.VelocityPath=2; Kuka.Poin [...]
+    25  DECL LDAT Lpnw1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    26  DECL E6POS XP7={X -3596.62695,Y -2.77881479,Z -444.531586,A -178.368134,B 0.266892016,C 179.968369,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    27  DECL FDAT FP7={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    28  DECL E6POS XP13={X -3882.93384,Y -48.4484138,Z -446.836792,A -178.367340,B 0.267035872,C 179.968063,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    29  DECL FDAT FP13={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
+    30  DECL LDAT LCPDAT4={VEL 2.00000,ACC 100.000,APO_DIST 2.00000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    31  DECL PDAT PPDAT25={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    32  DECL LDAT LCPDAT6={VEL 2.00000,ACC 100.000,APO_DIST 2.00000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    33  DECL LDAT LCPDAT10={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    34  DECL E6POS XP16={X -3884.36157,Y -60.7767830,Z -438.167816,A -178.367172,B -0.266017556,C 179.960464,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    35  DECL FDAT FP16={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    36  DECL LDAT LCPDAT11={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    37  DECL E6POS XP17={X -3884.77832,Y -61.9626274,Z -428.770508,A -178.367172,B -0.266017497,C 179.960464,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    38  DECL FDAT FP17={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    39  DECL LDAT LCPDAT12={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    40  ENDDAT
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt3B.src`

added, integrator program: 0 code line(s) removed, 58 added; 62 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3B.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3B.src.diff)

Attributes: +&ACCESS RVO1; +&REL 227; +&COMMENT 03-10-R1 PNW1 NUT 3 ST2; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\TP\Nutweld\Template\NutWeld_Vorgabe; +&PARAM DISKPATH = KRC:\R1\Program\StyleApps\Options

```diff
@@ base line end, backup line 7 @@
+     7  DEF style1app1opt3B( )
+    10  GLOBAL INTERRUPT DECL 3 WHEN $STOPMESS==TRUE DO IR_STOPM ( )
+    11  INTERRUPT ON 3
+    12  BAS (#INITMOV,0 )
+    37  $BWDSTART=FALSE
+    38  LDAT_ACT=LCPDAT6
+    39  FDAT_ACT=FP20
+    40  BAS(#CP_PARAMS,2)
+    41  LIN XP20 C_DIS C_DIS
+    48  INTERRUPT DECL 20 WHEN CL_GunStrokePositionLPT<137000 DO GUN_OPEN_LOST()
+    49  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
+    50  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
+    53  WAIT FOR NEXT_NUT_READY==TRUE
+    56  INTERRUPT ON 20
+    57  INTERRUPT ON 21
+    58  INTERRUPT ON 22
+    59  GUN_OPEN_CHECK()
+    62  $BWDSTART=FALSE
+    63  LDAT_ACT=LCPDAT4
+    64  FDAT_ACT=FP13
+    65  BAS(#CP_PARAMS,2)
+    66  LIN XP13 C_DIS C_DIS
+    72  IF NOT di004UseDryCycle THEN
+    74  $BWDSTART=FALSE
+    75  LDAT_ACT=LCPDAT11
+    76  FDAT_ACT=FP16
+    77  BAS(#CP_PARAMS,2)
+    78  LIN XP16
+    82  WAIT SEC 0
+    83  INTERRUPT OFF 20
+    84  INTERRUPT OFF 21
+    85  INTERRUPT OFF 22
+    87  CENTERLINE_WELD()
+    90  INTERRUPT ON 20
+    91  INTERRUPT ON 21
+    92  INTERRUPT ON 22
+    93  GUN_OPEN_CHECK()
+    94  ENDIF
+    97  $BWDSTART=FALSE
+    98  LDAT_ACT=LCPDAT12
+    99  FDAT_ACT=FP17
+   100  BAS(#CP_PARAMS,2)
+   101  LIN XP17
+   105  WAIT SEC 0
+   106  INTERRUPT OFF 20
+   107  INTERRUPT OFF 21
+   108  INTERRUPT OFF 22
+   110  $BWDSTART=FALSE
+   111  LDAT_ACT=LCPDAT10
+   112  FDAT_ACT=FP20
+   113  BAS(#CP_PARAMS,2)
+   114  LIN XP20
+   118  $BWDSTART=FALSE
+   119  PDAT_ACT=PPDAT25
+   120  FDAT_ACT=FP7
+   121  BAS(#PTP_PARAMS,60)
+   122  PTP XP7
+   126  END
```

### `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`

changed, integrator program: 30 code line(s) removed, 12 added; 68 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.src.diff)

```diff
@@ base line 58, backup line 58 @@
     58  BAS(#CP_PARAMS,2)
     59  LIN XP28
-    67  IF di004UseDryCycle==TRUE THEN
-    69  GOTO DRY1
-    70  ELSE
-    71  IF ($IN[227]==TRUE) THEN
-    72  PARTPRESENT1=TRUE
+    65  IF NOT di004UseDryCycle THEN
+    66  WAIT SEC 0.2
+    68  PARTPRESENT1=di227NutPresent1
     69  ENDIF
-    74  WAIT SEC 0.2
-    76  ENDIF
-    78  DRY1:
     72  $BWDSTART=FALSE
     73  PDAT_ACT=PPDAT35
@@ base line 93, backup line 84 @@
     84  BAS(#CP_PARAMS,2)
     85  LIN XP32
-   102  IF di004UseDryCycle==TRUE THEN
-   104  GOTO DRY2
-   105  ELSE
-   106  IF ($IN[227]==TRUE) THEN
-   107  PARTPRESENT2=TRUE
+    91  IF NOT di004UseDryCycle THEN
+    92  WAIT SEC 0.2
+    94  PARTPRESENT2=di227NutPresent1
     95  ENDIF
-   109  WAIT SEC 0.2
-   111  ENDIF
-   113  DRY2:
     98  $BWDSTART=FALSE
     99  PDAT_ACT=PPDAT36
@@ base line 128, backup line 110 @@
    110  BAS(#CP_PARAMS,2)
    111  LIN XP36
-   137  IF di004UseDryCycle==TRUE THEN
-   139  GOTO DRY3
-   140  ELSE
-   141  IF ($IN[227]==TRUE) THEN
-   142  PARTPRESENT3=TRUE
+   117  IF NOT di004UseDryCycle THEN
+   118  WAIT SEC 0.2
+   120  PARTPRESENT3=di227NutPresent1
    121  ENDIF
-   144  WAIT SEC 0.2
-   146  ENDIF
-   148  DRY3:
    124  $BWDSTART=FALSE
    125  PDAT_ACT=PPDAT37
@@ base line 154, backup line 127 @@
    127  BAS(#PTP_PARAMS,100)
    128  PTP XP37
-   163  IF di004UseDryCycle==TRUE THEN
-   165  GOTO DRY6
-   166  ELSE
+   138  IF NOT di004UseDryCycle THEN
    139  WAIT SEC 0.2
    140  SWITCH nOption
```
_16 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app2opt2.dat`

changed, integrator program: 1 code line(s) removed, 1 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.dat.diff)

Data changes:

- XP3 (E6POS) re-taught: moved 84.6 mm, rotated up to 16.2 deg

```diff
@@ base line 15, backup line 15 @@
     15  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P0                      ",POINT2[] "P0                      ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT0                   ",CONT[] "                        ",CP_VEL[] "2.0    [...]
     17  DECL LDAT LCPDAT0={VEL 2.00000,ACC 80.0000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    18  DECL E6POS XP3={X -709.692566,Y -2053.68652,Z 1506.28467,A -104.821503,B 4.90587568,C 179.018478,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    18  DECL E6POS XP3={X -709.833740,Y -2035.40430,Z 1423.71777,A -98.4577484,B -5.84655905,C -164.806564,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     19  DECL FDAT FP3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     20  DECL E6POS XP6={X -3780.88599,Y -731.523132,Z -847.811157,A -165.231735,B -0.613393545,C -0.0522668548,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
```

### `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`

changed, integrator program: 4 code line(s) removed, 12 added; 33 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.src.diff)

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
-    77  AC_Application (1,True)
+    69  CASE 12
+    72  IF (di100CameraJudgmentOK==TRUE) AND (di101CameraJudgmentNG==FALSE) THEN
+    73  do141RedRabbitFailed=TRUE
+    74  ENDIF
+    77  IF (di100CameraJudgmentOK==FALSE) AND (di101CameraJudgmentNG==TRUE) THEN
+    78  do142RedRabbitPassed=TRUE
+    79  ENDIF
+    80  ENDSWITCH
     86  END
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

changed, integrator program: 1 code line(s) removed, 1 added; 14 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src.diff](diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src.diff)

```diff
@@ base line 11, backup line 11 @@
     11  BAS (#INITMOV,0 )
     35  AC_DropOffCheck (1)
+    42  TRIGGER WHEN DISTANCE=1 DELAY=0 DO do070ApplicationClear1=TRUE
     44  $BWDSTART=FALSE
     45  PDAT_ACT=PPDAT10
@@ base line 58, backup line 62 @@
     62  LIN XAtDrop3
     72  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
-    76  GRPg_Check(1, 1, FALSE, 1)
     76  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254] )
     80  $OUT[18]=FALSE
```

### `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src`

changed, integrator program: 0 code line(s) removed, 1 added; 29 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src.diff](diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src.diff)

```diff
@@ base line 56, backup line 56 @@
     56  BAS(#PTP_PARAMS,100)
     57  PTP XP27
+    62  TRIGGER WHEN DISTANCE=1 DELAY=0 DO do070ApplicationClear1=TRUE
     64  $BWDSTART=FALSE
     65  PDAT_ACT=PPDAT26
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

added, integrator program: 0 code line(s) removed, 6 added; 19 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Styles/Options/Style1Opt10AutoRR.src.diff](diffs/KRC/R1/Program/Styles/Options/Style1Opt10AutoRR.src.diff)

Attributes: +&ACCESS RVO1; +&REL 3; +&COMMENT 03-10-R1 RED RABBIT CYCLE

```diff
@@ base line end, backup line 4 @@
+     4  DEF Style1Opt10AutoRR( )
+    17  Style1Pick1Opt1AutoRR()
+    19  style1app2opt1()
+    23  style1app2opt2()
+    26  style1drop1opt2AutoRR()
+    28  END
```

### `KRC/R1/Program/Styles/Options/style1opt1.src`

added, integrator program: 0 code line(s) removed, 41 added; 31 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Styles/Options/style1opt1.src.diff](diffs/KRC/R1/Program/Styles/Options/style1opt1.src.diff)

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
+    40  IF nPickStation==1 THEN
+    41  style1app1opt1A()
+    42  Style1App1Opt2A()
+    43  Style1App1Opt3A()
+    44  ELSE
+    45  style1app1opt1B()
+    46  Style1App1Opt2B()
+    47  Style1App1Opt3B()
+    48  ENDIF
+    51  style1app2opt1()
+    52  IF bScrapGE4==TRUE THEN
+    55  RejectGE4()
+    56  ELSE
+    59  style1app2opt2()
+    60  IF bScrapGE4==TRUE THEN
+    62  RejectGE4()
+    63  ELSE
+    65  Style1Drop1Opt1()
+    66  ENDIF
+    67  ENDIF
+    68  ENDIF
+    71  PARTPRESENT1=FALSE
+    72  PARTPRESENT2=FALSE
+    73  PARTPRESENT3=FALSE
+    75  END
```

### `KRC/R1/Program/Utilities/RejectGE4.src`

changed, integrator program: 1 code line(s) removed, 1 added; 15 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Utilities/RejectGE4.src.diff](diffs/KRC/R1/Program/Utilities/RejectGE4.src.diff)

```diff
@@ base line 37, backup line 37 @@
     37  BAS(#PTP_PARAMS,100)
     38  PTP XP10
+    44  TRIGGER WHEN DISTANCE=1 DELAY=0 DO do070ApplicationClear1=TRUE
     46  $BWDSTART=FALSE
     47  LDAT_ACT=LCPDAT0
@@ base line 46, backup line 50 @@
     50  LIN XP23
     60  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
-    63  GRPg_Check(1, 1, FALSE, 1)
     64  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254] )
     69  $BWDSTART=FALSE
```

### `KRC/R1/System/$config.dat`

changed, integrator program: 5 code line(s) removed, 12 added; 34 comment/blank line change(s). Full diff: [diffs/KRC/R1/System/$config.dat.diff](diffs/KRC/R1/System/$config.dat.diff)

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

changed, integrator program: 12 code line(s) removed, 43 added; 53 comment/blank line change(s). Full diff: [diffs/KRC/R1/System/sps.sub.diff](diffs/KRC/R1/System/sps.sub.diff)

```diff
@@ base line 31, backup line 31 @@
     31  BM_OUTPUTVALUE = 0
     34  TorqueDefinitions()
+    44  doCriticalWZ=FALSE
+    45  do111Gun1ElectrodeChange=FALSE
+    48  do006RobotBatteryAlarm=FALSE
+    49  do007RobotAtPounce=FALSE
+    50  do009RobotAtRepair=FALSE
+    51  do010RobotAtTipDress=FALSE
+    52  do013WaterIsOn=FALSE
+    53  do021BrakeTestReqd=FALSE
+    54  do022MstrRefRequired=FALSE
+    55  do046WeldMode=FALSE
+    56  do048RPWCtrlrEnetOK=FALSE
+    57  do050TDVlvManifold=FALSE
+    58  do051RbtAtMstrRefSwitch=FALSE
+    59  do052EOATVlvMnfldEnetOK=FALSE
+    60  do053MigReamerEnetOK=FALSE
+    61  do054SRWTipDressIOEnetOK=FALSE
+    62  do055EndEffectorIOEnetOK=FALSE
+    63  do056WeldCntl1EnetOK=FALSE
+    64  do057RPWSlrDArc1EnetOK=FALSE
+    65  do058PinScribeCntlrIOOK=FALSE
+    66  do059RPWSlrDArc2EnetOK=FALSE
+    67  do060VlvManifoldEnetOK=FALSE
+    68  do094AirOK=FALSE
+    69  gdoAxis1Posn=0
+    70  do107Hopper1LowLevel=FALSE
+    71  do118Nut1Ready=FALSE
+    72  do123ToolIDBit0=FALSE
+    73  do124ToolIDBit1=FALSE
+    74  do134Nut1Fault=FALSE
+    75  do146SpeedNot100=FALSE
+    76  do464WaterBeacon=FALSE
     87  LOOP
     88  WAIT FOR NOT($POWER_FAIL)
@@ base line 85, backup line 126 @@
    126  CL_WeldPinPosition=(CL_PIN_BYTE0*256)+CL_PIN_BYTE1
    129  SV0500_FLOW =( SV0500_BYTE0*256)+SV0500_BYTE1
-    94  IF SV0500_FLOW > 1230 THEN
-    95  CL_WaterOk = TRUE
+   136  nWaterFlow = SV0500_FLOW / 4
+   137  IF nWaterFlow >= nWaterFlowMin THEN
    138  dipw1_WaterOk = TRUE
    139  ELSE
-    98  CL_WaterOk = FALSE
-    99  dipw1_WaterOk = TRUE
+   140  IF nWaterFlow < (nWaterFlowMin - nWaterFlowHyst) THEN
+   141  dipw1_WaterOk = FALSE
    142  ENDIF
-   108  IF $OUT[478] THEN
-   109  $OUT[3008] = TRUE
-   110  $OUT[3024] = TRUE
    143  ENDIF
-   114  IF $OUT[477] THEN
-   115  $OUT[3001] = TRUE
-   116  $OUT[3024] = FALSE
+   145  CL_WaterOk = dipw1_WaterOk
+   153  IF dopw1_LowLevel THEN
+   154  CL_BeaconBit3008 = TRUE
```
_11 more lines: see diffs/KRC/R1/System/sps.sub.diff_

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

### Comment-only changes

| File | Comment/blank line changes | Attributes | Diff |
|---|---|---|---|
| `KRC/R1/Mada/$robcor.dat` | 0 | +&PARAM VERSION = 1.0.0; -&PARAM VERSION = 1.0.0 | diffs/KRC/R1/Mada/$robcor.dat.diff |
| `KRC/R1/Program/Styles/style_1.src` | 9 | - | diffs/KRC/R1/Program/Styles/style_1.src.diff |
| `KRC/R1/Program/Utilities/gunelectrodechange.src` | 6 | - | diffs/KRC/R1/Program/Utilities/gunelectrodechange.src.diff |
| `KRC/R1/System/tm_bib.src` | 0 | &ACCESS R2 -> &ACCESS R7; &REL 951 -> &REL 953 | diffs/KRC/R1/System/tm_bib.src.diff |
| `KRC/R1/TP/BrakeTest/braketestback.dat` | 0 | &ACCESS RVO1 -> &ACCESS RVO7 | diffs/KRC/R1/TP/BrakeTest/braketestback.dat.diff |
| `KRC/R1/TP/BrakeTest/braketestback.src` | 0 | &ACCESS RVO1 -> &ACCESS RVO7 | diffs/KRC/R1/TP/BrakeTest/braketestback.src.diff |
| `KRC/R1/TP/BrakeTest/braketestreq.dat` | 0 | &ACCESS RVO1 -> &ACCESS RVO7 | diffs/KRC/R1/TP/BrakeTest/braketestreq.dat.diff |
| `KRC/R1/TP/BrakeTest/braketestreq.src` | 0 | &ACCESS RVO1 -> &ACCESS RVO7 | diffs/KRC/R1/TP/BrakeTest/braketestreq.src.diff |
| `KRC/R1/TP/BrakeTest/braketeststart.dat` | 0 | &ACCESS RVO1 -> &ACCESS RVO7 | diffs/KRC/R1/TP/BrakeTest/braketeststart.dat.diff |
| `KRC/R1/TP/BrakeTest/braketeststart.src` | 0 | &ACCESS RVO1 -> &ACCESS RVO7 | diffs/KRC/R1/TP/BrakeTest/braketeststart.src.diff |
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

### INFO (22)

- `KRC/R1/Program/Centerline/CENTERLINE_HOME.src:55` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR dipw1_SpearHome
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:51` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR $PRO_STATE0==#P_ACTIVE
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:66` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR dipw1_AirOK
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:79` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR dipw1_WaterOk
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:99` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR (CL_GunStrokePositionLPT>=nGunOpenMin) AND (CL_GunStrokePosit
- `KRC/R1/Program/Centerline/centerline_weld.src:70` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR di466PartClampOpen
- `KRC/R1/Program/Centerline/centerline_weld.src:80` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR dipw1_SpearHome
- `KRC/R1/Program/Centerline/centerline_weld.src:95` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR di470QFPAdvanced
- `KRC/R1/Program/Centerline/centerline_weld.src:110` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR dipw1_SpearHome
- `KRC/R1/Program/Centerline/centerline_weld.src:146` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR di467PartClampClosed
- `KRC/R1/Program/Centerline/centerline_weld.src:227` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR (CL_GunStrokePositionLPT>=CL_GUN_WELD_MIN) AND (CL_GunStrokeP
- `KRC/R1/Program/Centerline/centerline_weld.src:275` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR di466PartClampOpen
- `KRC/R1/Program/Centerline/centerline_weld.src:286` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR dipw1_SpearHome
- `KRC/R1/Program/StyleApps/Options/style1app1opt1A.src:62` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR NUT_READY== TRUE
- `KRC/R1/Program/StyleApps/Options/style1app1opt1B.src:62` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR NUT_READY== TRUE
- `KRC/R1/Program/StyleApps/Options/style1app1opt2A.src:59` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR NEXT_NUT_READY==TRUE
- `KRC/R1/Program/StyleApps/Options/style1app1opt2B.src:59` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR NEXT_NUT_READY==TRUE
- `KRC/R1/Program/StyleApps/Options/style1app1opt3A.src:53` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR NEXT_NUT_READY==TRUE
- `KRC/R1/Program/StyleApps/Options/style1app1opt3B.src:53` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR NEXT_NUT_READY==TRUE
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src:37` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254])
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src:38` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254])
- `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src:39` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254])
