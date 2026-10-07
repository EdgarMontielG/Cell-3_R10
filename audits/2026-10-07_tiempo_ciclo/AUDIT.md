# Backup audit - 658424_R10_2026-10-07_1340.zip

- Backup: `/tmp/claude-0/-home-user/50f56c92-2919-5ae3-94c9-0de4476bbe87/scratchpad/s1/build/658424_R10_2026-10-07_1340.zip` (sha256 `d3ecd66309722a80...`)
- am.ini: archive `e:\bmw_03_10_r1.zip\`, date `2026-10-05_14-46-44`, config `All`, robot `BMW_03_10_R1`, serial `658424`, KSS `V8.3.29`
- Compared with: `1b28a7e` = `1b28a7ee87` "Delivery of 2026-10-05 evening: program package on the 14:46 backup; Excel and PDF"; first commit (archive as received) `22a98cc8ef`
- Generated 2026-10-07T19:41:01 by tools/audit_backup.py

## Summary

| | |
|---|---|
| Entries audited (Log Files/ skipped: 8) | 316 |
| Unchanged | 304 |
| Changed | 10 |
| Added | 2 |
| Missing from the backup | 0 |
| **Deleted modules still on the controller** | 0 |
| **Pre-cleanup files** | 0 |
| Edited on top of the pre-cleanup file | 0 |
| KRL files with code changes | 11 |
| Code lines removed / added | 21 / 112 |
| KRL files with comment-only changes | 1 |
| KRL files with runtime values only (written by the program, not edits) | 0 |
| Checks FAIL / WARN / INFO | 0 / 0 / 0 |

**Needs attention:**

_nothing beyond the changes listed below_

## The backup itself

- INFO: KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.src: spelled KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src in the base (the controller ignores case)

## Deleted modules still present

_none_

## Pre-cleanup files

_none_

## Files

### Changed (10)

- `KRC/R1/Program/Centerline/PRELOAD.src` - integrator program
- `KRC/R1/Program/Centerline/Request_next_nut.src` - integrator program
- `KRC/R1/Program/Centerline/centerline_weld.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt1A.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt1B.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt2A.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt2B.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt3A.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt3B.src` - integrator program
- `KRC/R1/System/$config.dat` - integrator program

### Added (2)

- `KRC/R1/Program/Centerline/CL_CYCLE_TIME.dat` - integrator program
- `KRC/R1/Program/Centerline/CL_CYCLE_TIME.src` - integrator program

### Missing from the backup (0)

_none_

### Outside the archive layout (ignored) (0)

_none_

## Code changes

### `KRC/R1/Program/Centerline/CL_CYCLE_TIME.dat`

added, integrator program: 0 code line(s) removed, 8 added; 15 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/CL_CYCLE_TIME.dat.diff](diffs/KRC/R1/Program/Centerline/CL_CYCLE_TIME.dat.diff)

Attributes: +&ACCESS  RV; +&COMMENT 03-10-R1 PNW1 CYCLE TIME MEASUREMENT; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\Roboter\Template\vorgabe; +&REL 1

Data changes:

- added 1 DEFDAT: CL_CYCLE_TIME
- added 3 INT: CL_T_LOG, CL_T_NUT, CL_T_ROW

```diff
@@ base line end, backup line 6 @@
+     6  DEFDAT CL_CYCLE_TIME PUBLIC
+    20  DECL INT CL_T_NUT=0
+    21  DECL INT CL_T_ROW[3]
+    22  CL_T_ROW[1]=0
+    23  CL_T_ROW[2]=0
+    24  CL_T_ROW[3]=0
+    25  DECL INT CL_T_LOG[3,10,13]
+    27  ENDDAT
```

### `KRC/R1/Program/Centerline/CL_CYCLE_TIME.src`

added, integrator program: 0 code line(s) removed, 29 added; 25 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/CL_CYCLE_TIME.src.diff](diffs/KRC/R1/Program/Centerline/CL_CYCLE_TIME.src.diff)

Attributes: +&ACCESS RVO1; +&REL 1; +&COMMENT 03-10-R1 PNW1 CYCLE TIME MEASUREMENT; +&PARAM EDITMASK = *; +&PARAM TEMPLATE = C:\KRC\Roboter\Template\vorgabe

```diff
@@ base line end, backup line 6 @@
+     6  DEF CL_CYCLE_TIME(nStep:IN)
+    21  INT nStep
+    24  IF (CL_T_NUT>=1) AND (CL_T_NUT<=3) AND (nStep>=1) AND (nStep<=13) THEN
+    25  IF (CL_T_ROW[CL_T_NUT]>=1) AND (CL_T_ROW[CL_T_NUT]<=10) THEN
+    26  CL_T_LOG[CL_T_NUT,CL_T_ROW[CL_T_NUT],nStep]=$TIMER[20]
+    27  ENDIF
+    29  IF nStep==13 THEN
+    30  CL_T_NUT=0
+    31  ENDIF
+    32  ENDIF
+    33  END
+    35  GLOBAL DEF CL_CYCLE_START(nNut:IN)
+    38  INT nNut, nStep
+    40  CL_T_NUT=0
+    41  IF (nNut>=1) AND (nNut<=3) THEN
+    43  IF (CL_T_ROW[nNut]>=1) AND (CL_T_ROW[nNut]<10) THEN
+    44  CL_T_ROW[nNut]=CL_T_ROW[nNut]+1
+    45  ELSE
+    46  CL_T_ROW[nNut]=1
+    47  ENDIF
+    49  FOR nStep=1 TO 13
+    50  CL_T_LOG[nNut,CL_T_ROW[nNut],nStep]=-1
+    51  ENDFOR
+    52  CL_T_NUT=nNut
+    54  $TIMER_STOP[20]=TRUE
+    55  $TIMER[20]=0
+    56  $TIMER_STOP[20]=FALSE
+    57  ENDIF
+    58  END
```

### `KRC/R1/Program/Centerline/PRELOAD.src`

changed, integrator program: 16 code line(s) removed, 22 added; 95 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/PRELOAD.src.diff](diffs/KRC/R1/Program/Centerline/PRELOAD.src.diff)

```diff
@@ base line 3, backup line 3 @@
      3  DEF PRELOAD ( )
-    33  IF NUT_START AND NOT NUTCYCLE_ACTIVE THEN
+    44  IF (NUT_START OR NUT_FEED_START) AND NOT NUTCYCLE_ACTIVE THEN
+    46  NUT_FEED_START=FALSE
+    47  IF NUT_START THEN
     48  NUT_START=FALSE
+    49  NUT_LOAD_OK=TRUE
+    50  NUT_READY=FALSE
+    51  ELSE
+    52  NUT_LOAD_OK=FALSE
+    53  ENDIF
     54  NUTCYCLE_ACTIVE=TRUE
-    37  NUT_READY=FALSE
     55  NUT_PRELOAD_STEP=0
     56  STEP0DONE=FALSE
@@ base line 45, backup line 62 @@
     62  $TIMER_STOP[11]=TRUE
     63  $TIMER[11]=0
-    47  $TIMER_STOP[12]=TRUE
-    48  $TIMER[12]=0
     64  $TIMER_STOP[13]=TRUE
     65  $TIMER[13]=0
+    67  ENDIF
+    72  IF NUT_START AND NUTCYCLE_ACTIVE AND NOT NUT_LOAD_OK THEN
+    73  NUT_START=FALSE
+    74  NUT_READY=FALSE
+    75  NUT_LOAD_OK=TRUE
     76  ENDIF
     79  IF NUTCYCLE_ACTIVE AND NOT di004UseDryCycle THEN
     81  SWITCH NUT_PRELOAD_STEP
     83  CASE 0
+    86  IF NOT STEP0DONE THEN
     89  do503QFPAdvance=FALSE
     90  do504QFPReturn=TRUE
     94  IF (dipw1_SpearHome==TRUE) AND (di470QFPAdvanced==FALSE) THEN
     96  dopw1_StartFeed=TRUE
+    99  IF NUT_LOAD_OK THEN
    100  dopw1_BlowOff=FALSE
+   101  ENDIF
    104  IF $TIMER_STOP[10] THEN
    105  $TIMER[10]=0
@@ base line 81, backup line 110 @@
    110  IF $TIMER[10]>=2000 THEN
    111  $TIMER_STOP[10]=TRUE
+   112  dopw1_StartFeed=FALSE
    113  STEP0DONE=TRUE
    114  ENDIF
    116  ENDIF
-    89  IF STEP0DONE THEN
+   118  ENDIF
+   121  IF STEP0DONE AND NUT_LOAD_OK THEN
    122  NUT_PRELOAD_STEP = 10
    123  ENDIF
@@ base line 166, backup line 198 @@
    198  IF STEP0DONE AND STEP10DONE THEN
    199  NUT_PRELOAD_STEP = 20
-   168  $TIMER_STOP[12]=TRUE
-   169  $TIMER[12]=0
    201  ENDIF
```
_32 more lines: see diffs/KRC/R1/Program/Centerline/PRELOAD.src.diff_

### `KRC/R1/Program/Centerline/centerline_weld.src`

changed, integrator program: 3 code line(s) removed, 19 added; 27 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/centerline_weld.src.diff](diffs/KRC/R1/Program/Centerline/centerline_weld.src.diff)

```diff
@@ base line 5, backup line 5 @@
      5  DEF CENTERLINE_WELD()
+    59  CL_CYCLE_TIME(2)
     64  dopw1_GunWork=FALSE
     65  dopw1_GunHome=TRUE
@@ base line 78, backup line 84 @@
     84  do504QFPReturn=TRUE
     86  WAIT FOR dipw1_SpearHome
-    84  IF NOT NUT_READY THEN
+    93  IF NOT NUT_READY AND NOT NUTCYCLE_ACTIVE THEN
     96  dopw1_ReturnPin=FALSE
     97  dopw1_AdvancePin=TRUE
@@ base line 110, backup line 119 @@
    119  WAIT FOR dipw1_SpearHome
    120  ENDIF
+   122  CL_CYCLE_TIME(3)
    125  do499UpperPinRetract=FALSE
    126  do498UpperPinExtend=TRUE
@@ base line 124, backup line 135 @@
    135  dopw1_WeldOnExternal=FALSE
    136  gdopw1_SpotNumber=0
-   128  dopw1_StartFeed=FALSE
    139  dopw1_Nut1Intensify=FALSE
    140  dopw1_Nut1Intensify_Home=TRUE
    141  dopw1_BlowOff=FALSE
+   144  IF NOT NUTCYCLE_ACTIVE THEN
+   145  dopw1_StartFeed=FALSE
+   146  ENDIF
    148  CL_GunPressureCmd=CL_GUN_PRESS_BASE
    151  dopw1_WeldContactEnable=TRUE
    152  dopw1_WeldOnExternal=TRUE
    155  WAIT FOR dipw1_Ready
+   157  CL_CYCLE_TIME(4)
    160  do502PartClampOpen=FALSE
    161  do501PartClampClose=TRUE
    163  WAIT FOR di467PartClampClosed
+   165  CL_CYCLE_TIME(5)
    168  dopw1_GunHome=FALSE
    169  WAIT SEC 0.2
@@ base line 201, backup line 220 @@
    220  $TIMER_STOP[15]=TRUE
    221  $TIMER[15]=0
+   223  CL_CYCLE_TIME(6)
    226  dopw1_WeldOnExternal=TRUE
    230  gdopw1_SpotNumber=CL_WELD_PROGRAM
    233  WAIT FOR dipw1_Ready
+   235  CL_CYCLE_TIME(7)
    238  CL_GunPressureCmd=CL_GUN_PRESS_WELD
    242  dopw1_BlowOff=TRUE
@@ base line 221, backup line 244 @@
    244  dopw1_Nut1Intensify=TRUE
    247  WAIT FOR dipw1_IntensfPresOk
+   249  CL_CYCLE_TIME(8)
    252  WAIT FOR (CL_GunStrokePositionLPT>=CL_GUN_WELD_MIN) AND (CL_GunStrokePositionLPT<=CL_GUN_WELD_MAX)
    255  dopw1_WeldInit=TRUE
    257  WAIT FOR dipw1_WeldComplete
+   259  CL_CYCLE_TIME(9)
    262  dopw1_WeldInit=FALSE
    263  WAIT FOR NOT dipw1_WeldComplete
+   265  CL_CYCLE_TIME(10)
```
_30 more lines: see diffs/KRC/R1/Program/Centerline/centerline_weld.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt1A.src`

changed, integrator program: 0 code line(s) removed, 6 added; 15 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1A.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1A.src.diff)

```diff
@@ base line 56, backup line 56 @@
     56  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
     57  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
+    60  WAIT SEC 0
+    61  CL_CYCLE_START(1)
     66  WAIT FOR NUT_READY== TRUE
+    68  CL_CYCLE_TIME(1)
+    73  IF NUT_READY AND NOT NUTCYCLE_ACTIVE AND NOT di004UseDryCycle THEN
+    74  NUT_FEED_START=TRUE
+    75  ENDIF
     78  INTERRUPT ON 20
     79  INTERRUPT ON 21
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt1B.src`

changed, integrator program: 0 code line(s) removed, 6 added; 15 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1B.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1B.src.diff)

```diff
@@ base line 56, backup line 56 @@
     56  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
     57  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
+    60  WAIT SEC 0
+    61  CL_CYCLE_START(1)
     66  WAIT FOR NUT_READY== TRUE
+    68  CL_CYCLE_TIME(1)
+    73  IF NUT_READY AND NOT NUTCYCLE_ACTIVE AND NOT di004UseDryCycle THEN
+    74  NUT_FEED_START=TRUE
+    75  ENDIF
     78  INTERRUPT ON 20
     79  INTERRUPT ON 21
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt2A.src`

changed, integrator program: 1 code line(s) removed, 7 added; 19 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2A.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2A.src.diff)

```diff
@@ base line 55, backup line 55 @@
     55  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
     56  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
+    59  WAIT SEC 0
+    60  CL_CYCLE_START(2)
     64  WAIT FOR NEXT_NUT_READY==TRUE
+    66  CL_CYCLE_TIME(1)
+    71  IF NUT_READY AND NOT NUTCYCLE_ACTIVE AND NOT di004UseDryCycle THEN
+    72  NUT_FEED_START=TRUE
+    73  ENDIF
     76  INTERRUPT ON 20
     77  INTERRUPT ON 21
@@ base line 119, backup line 133 @@
    133  BAS(#CP_PARAMS,2)
    134  LIN XP05
-   127  TRIGGER WHEN DISTANCE = 1 DELAY = 0 DO Request_next_nut() PRIO= -1
+   144  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO Request_next_nut() PRIO= -1
    146  $BWDSTART=FALSE
    147  PDAT_ACT=PPDAT26
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt2B.src`

changed, integrator program: 1 code line(s) removed, 7 added; 19 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2B.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2B.src.diff)

```diff
@@ base line 55, backup line 55 @@
     55  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
     56  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
+    59  WAIT SEC 0
+    60  CL_CYCLE_START(2)
     64  WAIT FOR NEXT_NUT_READY==TRUE
+    66  CL_CYCLE_TIME(1)
+    71  IF NUT_READY AND NOT NUTCYCLE_ACTIVE AND NOT di004UseDryCycle THEN
+    72  NUT_FEED_START=TRUE
+    73  ENDIF
     76  INTERRUPT ON 20
     77  INTERRUPT ON 21
@@ base line 119, backup line 133 @@
    133  BAS(#CP_PARAMS,2)
    134  LIN XP05
-   127  TRIGGER WHEN DISTANCE = 1 DELAY = 0 DO Request_next_nut() PRIO= -1
+   144  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO Request_next_nut() PRIO= -1
    146  $BWDSTART=FALSE
    147  PDAT_ACT=PPDAT26
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt3A.src`

changed, integrator program: 0 code line(s) removed, 3 added; 6 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3A.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3A.src.diff)

```diff
@@ base line 49, backup line 49 @@
     49  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
     50  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
+    53  WAIT SEC 0
+    54  CL_CYCLE_START(3)
     58  WAIT FOR NEXT_NUT_READY==TRUE
+    60  CL_CYCLE_TIME(1)
     63  INTERRUPT ON 20
     64  INTERRUPT ON 21
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt3B.src`

changed, integrator program: 0 code line(s) removed, 3 added; 6 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3B.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3B.src.diff)

```diff
@@ base line 49, backup line 49 @@
     49  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
     50  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
+    53  WAIT SEC 0
+    54  CL_CYCLE_START(3)
     58  WAIT FOR NEXT_NUT_READY==TRUE
+    60  CL_CYCLE_TIME(1)
     63  INTERRUPT ON 20
     64  INTERRUPT ON 21
```

### `KRC/R1/System/$config.dat`

changed, integrator program: 0 code line(s) removed, 2 added; 19 comment/blank line change(s). Full diff: [diffs/KRC/R1/System/$config.dat.diff](diffs/KRC/R1/System/$config.dat.diff)

Data changes:

- added 2 BOOL: NUT_FEED_START, NUT_LOAD_OK

```diff
@@ base line 852, backup line 852 @@
    852  DECL INT CL_WELD_PROGRAM=2
    861  DECL BOOL NUT_START=FALSE
+   865  DECL BOOL NUT_FEED_START=FALSE
+   868  DECL BOOL NUT_LOAD_OK=FALSE
    874  DECL BOOL NUT_READY=TRUE
    877  DECL BOOL NUTCYCLE_ACTIVE=FALSE
```

### Comment-only changes

| File | Comment/blank line changes | Attributes | Diff |
|---|---|---|---|
| `KRC/R1/Program/Centerline/Request_next_nut.src` | 9 | - | diffs/KRC/R1/Program/Centerline/Request_next_nut.src.diff |

## Mechanical checks

### FAIL (0)

_none_

### WARN (0)

_none_

### INFO (0)

_none_
