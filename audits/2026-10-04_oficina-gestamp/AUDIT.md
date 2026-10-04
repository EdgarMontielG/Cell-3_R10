# Backup audit - 658424_R10_oficina.zip

- Backup: `/tmp/claude-0/-home-user-Cell-3-R10/50f56c92-2919-5ae3-94c9-0de4476bbe87/scratchpad/dist/658424_R10_oficina.zip` (sha256 `ca7b547d07af8127...`)
- am.ini: archive `e:\v431_03_10_r1.zip\`, date `2026-10-02_22-15-15`, config `All`, robot `V431_03_10_R1`, serial `658424`, KSS `V8.3.29`
- Compared with: `fb8a4c8` = `fb8a4c8b96` "Add findings, I/O label map and cleanup conventions for R10"; first commit (archive as received) `22a98cc8ef`
- Generated 2026-10-04T15:24:34 by tools/audit_backup.py

## Summary

| | |
|---|---|
| Entries audited (Log Files/ skipped: 8) | 304 |
| Unchanged | 284 |
| Changed | 18 |
| Added | 2 |
| Missing from the backup | 3 |
| **Deleted modules still on the controller** | 0 |
| **Pre-cleanup files** | 0 |
| Edited on top of the pre-cleanup file | 0 |
| KRL files with code changes | 19 |
| Code lines removed / added | 235 / 217 |
| KRL files with comment-only changes | 1 |
| KRL files with runtime values only (written by the program, not edits) | 0 |
| Checks FAIL / WARN / INFO | 0 / 0 / 12 |

**Needs attention:**

- WARN 3 file(s) of the base missing from the backup - deleted on the robot, or an incomplete archive (e.g. KRC/R1/Program/Centerline/centerline_loop.src; all in Files, "Missing from the backup")

## The backup itself

- WARN: 3 file(s) of the base missing from the backup - deleted on the robot, or an incomplete archive (e.g. KRC/R1/Program/Centerline/centerline_loop.src; all in Files, "Missing from the backup")
- INFO: KRC/R1/TP/AutomationCore/automationcoreroutines.dat: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)

## Deleted modules still present

_none_

## Pre-cleanup files

_none_

## Files

### Changed (18)

- `KRC/R1/Program/Centerline/CENTERLINE_HOME.src` - integrator program
- `KRC/R1/Program/Centerline/PRELOAD.src` - integrator program
- `KRC/R1/Program/Centerline/Request_next_nut.src` - integrator program
- `KRC/R1/Program/Centerline/centerline_weld.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt1.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt2.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt3.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app2opt1.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app2opt2.src` - integrator program
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src` - integrator program
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src` - integrator program
- `KRC/R1/Program/Utilities/RejectGE4.src` - integrator program
- `KRC/R1/System/$config.dat` - integrator program
- `KRC/R1/System/sps.sub` - integrator program
- `KRC/R1/TP/AutomationCore/automationcoreroutines.dat` - KUKA system / vendor package

### Added (2)

- `KRC/R1/Program/Styles/Options/Style1Opt10AutoRR.src` - integrator program
- `KRC/R1/Program/Styles/Options/style1opt1.src` - integrator program

### Missing from the backup (3)

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

changed, integrator program: 73 code line(s) removed, 65 added; 184 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/centerline_weld.src.diff](diffs/KRC/R1/Program/Centerline/centerline_weld.src.diff)

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

### `KRC/R1/Program/StyleApps/Options/style1app1opt1.src`

changed, integrator program: 10 code line(s) removed, 2 added; 25 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1.src.diff)

```diff
@@ base line 47, backup line 47 @@
     47  BAS(#CP_PARAMS,2)
     48  LIN XP8 C_DIS C_DIS
-    51  RETRY_NUT1:
     54  WAIT FOR NUT_READY== TRUE
     58  $BWDSTART=FALSE
@@ base line 63, backup line 61 @@
     61  BAS(#CP_PARAMS,2)
     62  LIN XP20 C_DIS C_DIS
-    68  IF di004UseDryCycle==TRUE THEN
-    70  GOTO DRY1
-    71  ELSE
+    68  IF NOT di004UseDryCycle THEN
     70  $BWDSTART=FALSE
     71  LDAT_ACT=LCPDAT18
@@ base line 81, backup line 77 @@
     77  CENTERLINE_WELD()
     78  ENDIF
-    84  DRY1:
     82  $BWDSTART=FALSE
     83  LDAT_ACT=LCPDAT16
@@ base line 91, backup line 85 @@
     85  BAS(#CP_PARAMS,2)
     86  LIN XP20 C_DIS C_DIS
-    97  IF NUT_WELD_RETRY THEN
-    98  NUT_WELD_RETRY=FALSE
-   100  GOTO RETRY_NUT1
-   101  ENDIF
     92  $BWDSTART=FALSE
     93  LDAT_ACT=LCPDAT17
@@ base line 107, backup line 95 @@
     95  BAS(#CP_PARAMS,2)
     96  LIN XP8 C_DIS C_DIS
+   103  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO Request_next_nut() PRIO= -1
    105  $BWDSTART=FALSE
    106  PDAT_ACT=PPDAT18
    107  FDAT_ACT=FP0
    108  BAS(#PTP_PARAMS,100)
-   119  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO Request_next_nut() PRIO= -1
    109  PTP XP0
    111  END
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt2.src`

changed, integrator program: 10 code line(s) removed, 2 added; 25 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2.src.diff)

```diff
@@ base line 46, backup line 46 @@
     46  BAS(#CP_PARAMS,2)
     47  LIN XP5
-    50  RETRY_NUT1:
     51  WAIT FOR NEXT_NUT_READY==TRUE
     54  $BWDSTART=FALSE
@@ base line 59, backup line 57 @@
     57  BAS(#CP_PARAMS,2)
     58  LIN XP6
-    64  IF di004UseDryCycle==TRUE THEN
-    66  GOTO DRY1
-    67  ELSE
+    64  IF NOT di004UseDryCycle THEN
     66  $BWDSTART=FALSE
     67  LDAT_ACT=LCPDAT15
@@ base line 77, backup line 73 @@
     73  CENTERLINE_WELD()
     74  ENDIF
-    82  DRY1:
     77  $BWDSTART=FALSE
     78  LDAT_ACT=LCPDAT6
@@ base line 88, backup line 80 @@
     80  BAS(#CP_PARAMS,2)
     81  LIN XP06 C_DIS C_DIS
-    92  IF NUT_WELD_RETRY THEN
-    93  NUT_WELD_RETRY=FALSE
-    95  GOTO RETRY_NUT1
-    96  ENDIF
     84  $BWDSTART=FALSE
     85  LDAT_ACT=LCPDAT14
@@ base line 101, backup line 87 @@
     87  BAS(#CP_PARAMS,2)
     88  LIN XP05
+    95  TRIGGER WHEN DISTANCE = 1 DELAY = 0 DO Request_next_nut() PRIO= -1
     97  $BWDSTART=FALSE
     98  PDAT_ACT=PPDAT26
     99  FDAT_ACT=FP0
    100  BAS(#PTP_PARAMS,100)
-   113  TRIGGER WHEN DISTANCE = 1 DELAY = 0 DO Request_next_nut() PRIO= -1
    101  PTP XP0
    105  END
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt3.src`

changed, integrator program: 9 code line(s) removed, 1 added; 14 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3.src.diff)

```diff
@@ base line 40, backup line 40 @@
     40  BAS(#CP_PARAMS,2)
     41  LIN XP20 C_DIS C_DIS
-    44  RETRY_NUT1:
     45  WAIT FOR NEXT_NUT_READY==TRUE
     48  $BWDSTART=FALSE
@@ base line 53, backup line 51 @@
     51  BAS(#CP_PARAMS,2)
     52  LIN XP13 C_DIS C_DIS
-    58  IF di004UseDryCycle==TRUE THEN
-    60  GOTO DRY1
-    61  ELSE
+    58  IF NOT di004UseDryCycle THEN
     60  $BWDSTART=FALSE
     61  LDAT_ACT=LCPDAT11
@@ base line 71, backup line 67 @@
     67  CENTERLINE_WELD()
     68  ENDIF
-    74  DRY1:
     71  $BWDSTART=FALSE
     72  LDAT_ACT=LCPDAT12
@@ base line 80, backup line 74 @@
     74  BAS(#CP_PARAMS,2)
     75  LIN XP17
-    84  IF NUT_WELD_RETRY THEN
-    85  NUT_WELD_RETRY=FALSE
-    87  GOTO RETRY_NUT1
-    88  ENDIF
     78  $BWDSTART=FALSE
     79  LDAT_ACT=LCPDAT10
```

### `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`

changed, integrator program: 28 code line(s) removed, 10 added; 53 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.src.diff)

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
+   137  IF NOT di004UseDryCycle THEN
    138  WAIT SEC 0.2
    139  SWITCH nOption
```
_5 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`

changed, integrator program: 2 code line(s) removed, 2 added; 4 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.src.diff)

```diff
@@ base line 53, backup line 53 @@
     53  WAIT FOR di080ToolRepositioned1
     58  WAIT SEC 0.2
-    60  IF (di100CameraJudmentOK==TRUE) AND (di101CameraJudmentNG==FALSE)THEN
+    61  IF (di100CameraJudgmentOK==TRUE) AND (di101CameraJudgmentNG==FALSE)THEN
     62  bscrapGE4 = FALSE
     64  ENDIF
-    64  IF (di100CameraJudmentOK==FALSE) AND (di101CameraJudmentNG==TRUE)THEN
+    66  IF (di100CameraJudgmentOK==FALSE) AND (di101CameraJudgmentNG==TRUE)THEN
     67  bscrapGE4 = TRUE
     68  ENDIF
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

added, integrator program: 0 code line(s) removed, 6 added; 17 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Styles/Options/Style1Opt10AutoRR.src.diff](diffs/KRC/R1/Program/Styles/Options/Style1Opt10AutoRR.src.diff)

Attributes: +&ACCESS RVO1; +&REL 3; +&COMMENT 03-10-R1 RED RABBIT CYCLE

```diff
@@ base line end, backup line 4 @@
+     4  DEF Style1Opt10AutoRR( )
+    16  Style1Pick1Opt1AutoRR()
+    18  style1app2opt1()
+    21  style1app2opt2()
+    24  style1drop1opt2AutoRR()
+    26  END
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

changed, integrator program: 5 code line(s) removed, 13 added; 30 comment/blank line change(s). Full diff: [diffs/KRC/R1/System/$config.dat.diff](diffs/KRC/R1/System/$config.dat.diff)

Data changes:

- CL_GUN_WELD_MAX (INT): 76000 -> 73000
- CL_GUN_WELD_MIN (INT): 65000 -> 69000
- added 1 BOOL: NUT_START
- added 7 INT: CL_GUN_CLOSE_TIMEOUT, CL_GUN_IN_WINDOW_TIME, CL_GUN_OPEN_MIN, CL_GUN_PRESS_BASE, CL_GUN_PRESS_REST, CL_GUN_PRESS_WELD, CL_WELD_PROGRAM
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
+   841  DECL INT CL_GUN_OPEN_MIN=120000
+   843  DECL INT CL_GUN_CLOSE_TIMEOUT=1000
+   844  DECL INT CL_GUN_IN_WINDOW_TIME=300
+   849  DECL INT CL_GUN_PRESS_BASE=405
+   850  DECL INT CL_GUN_PRESS_WELD=1820
+   851  DECL INT CL_GUN_PRESS_REST=39425
+   853  DECL INT CL_WELD_PROGRAM=2
+   861  DECL BOOL NUT_START=FALSE
    866  DECL BOOL NUT_READY=TRUE
    869  DECL BOOL NUTCYCLE_ACTIVE=FALSE
@@ base line 856, backup line 878 @@
    878  DECL BOOL NEXT_NUT_READY=TRUE
    879  DECL BOOL NEXT_NUT_REQUEST=FALSE
-   859  DECL BOOL NUT_WELD_RETRY=FALSE
    881  DECL BOOL STEP10_ADV_STARTED=FALSE
    885  ENDDAT
```

### `KRC/R1/System/sps.sub`

changed, integrator program: 7 code line(s) removed, 7 added; 23 comment/blank line change(s). Full diff: [diffs/KRC/R1/System/sps.sub.diff](diffs/KRC/R1/System/sps.sub.diff)

```diff
@@ base line 99, backup line 101 @@
    101  dipw1_WaterOk = TRUE
    102  ENDIF
-   108  IF $OUT[478] THEN
-   109  $OUT[3008] = TRUE
-   110  $OUT[3024] = TRUE
+   110  IF dopw1_LowLevel THEN
+   111  CL_BeaconBit3008 = TRUE
+   112  CL_BeaconBit3024 = TRUE
    113  ENDIF
-   114  IF $OUT[477] THEN
-   115  $OUT[3001] = TRUE
-   116  $OUT[3024] = FALSE
+   117  IF dopw1_LevelOk THEN
+   118  CL_BeaconBit3001 = TRUE
+   119  CL_BeaconBit3024 = FALSE
    120  ENDIF
    128  IF di004UseDryCycle==FALSE THEN
-   126  $OUT[475]=TRUE
+   129  dopw1_StartWater=TRUE
    130  ENDIF
    136  PRELOAD()
```

### `KRC/R1/TP/AutomationCore/automationcoreroutines.dat`

changed, KUKA system / vendor package: 15 code line(s) removed, 15 added; 5 comment/blank line change(s). Full diff: [diffs/KRC/R1/TP/AutomationCore/automationcoreroutines.dat.diff](diffs/KRC/R1/TP/AutomationCore/automationcoreroutines.dat.diff)

Data changes:

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
```

### Comment-only changes

| File | Comment/blank line changes | Attributes | Diff |
|---|---|---|---|
| `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src` | 26 | - | diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src.diff |

## Mechanical checks

Signal declarations changed (names lower-cased):

- $IN[100]: di100camerajudmentok -> di100camerajudgmentok
- $IN[101]: di101camerajudmentng -> di101camerajudgmentng
- $IN[106]: di106partrejeted -> di106partrejected
- $IN[227]: di227sensorcamera, nut_present1 -> di227nutpresent1
- $IN[466]: di466reserved, di466spare -> di466partclampopen, di466spare
- $IN[467]: di467reserved, di467spare -> di467partclampclosed, di467spare
- $IN[470]: di470reserved, di470spare -> di470qfpadvanced, di470spare
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

### INFO (12)

- `KRC/R1/Program/Centerline/CENTERLINE_HOME.src:55` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR dipw1_SpearHome
- `KRC/R1/Program/Centerline/centerline_weld.src:70` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR di466PartClampOpen
- `KRC/R1/Program/Centerline/centerline_weld.src:80` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR dipw1_SpearHome
- `KRC/R1/Program/Centerline/centerline_weld.src:95` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR di470QFPAdvanced
- `KRC/R1/Program/Centerline/centerline_weld.src:110` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR dipw1_SpearHome
- `KRC/R1/Program/Centerline/centerline_weld.src:146` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR di467PartClampClosed
- `KRC/R1/Program/Centerline/centerline_weld.src:227` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR (CL_GunStrokePositionLPT>=CL_GUN_WELD_MIN) AND (CL_GunStrokeP
- `KRC/R1/Program/Centerline/centerline_weld.src:274` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR di466PartClampOpen
- `KRC/R1/Program/Centerline/centerline_weld.src:285` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR dipw1_SpearHome
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src:37` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254])
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src:38` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254])
- `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src:39` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254])
