# Backup audit - 5eba76d2-BMW_03_WINDOWS-2CPT70E_BMW_03_10_R1_658424.zip

- Backup: `/root/.claude/uploads/50f56c92-2919-5ae3-94c9-0de4476bbe87/5eba76d2-BMW_03_WINDOWS-2CPT70E_BMW_03_10_R1_658424.zip` (sha256 `0f71260b2b08429d...`)
- am.ini: archive `C:\windows\TEMP\tmpB604.tmp\`, date `2026-10-11_22-32-16`, config `All`, robot `BMW_03_10_R1`, serial `658424`, KSS `V8.3.29`
- Compared with: `HEAD` = `0425c96373` "Cycle time target of R10: 38 s part to part (Edgar, 2026-10-11)"; first commit (archive as received) `22a98cc8ef`
- Generated 2026-10-12T11:34:53 by tools/audit_backup.py

## Summary

| | |
|---|---|
| Entries audited (Log Files/ skipped: 8) | 323 |
| Unchanged | 281 |
| Changed | 39 |
| Added | 1 |
| Missing from the backup | 0 |
| **Deleted modules still on the controller** | 0 |
| **Pre-cleanup files** | 0 |
| Edited on top of the pre-cleanup file | 0 |
| KRL files with code changes | 10 |
| Code lines removed / added | 38 / 70 |
| KRL files with comment-only changes | 15 |
| KRL files with runtime values only (written by the program, not edits) | 6 |
| Checks FAIL / WARN / INFO | 0 / 19 / 0 |

**Needs attention:**

- WARN 2 entries outside the KUKA archive layout ignored (e.g. Archive.log)
- WARN KRC/R1/TP/NutWeld/nutweldroutines.src: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- 19 WARN in the mechanical checks

## The backup itself

- WARN: 2 entries outside the KUKA archive layout ignored (e.g. Archive.log)
- WARN: KRC/R1/TP/NutWeld/nutweldroutines.src: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- INFO: KRC/R1/TP/GripperSpotTech/grp_data.dat: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- INFO: KRC/R1/TP/NutWeld/nutweldroutines.dat: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)

## Deleted modules still present

_none_

## Pre-cleanup files

_none_

## Files

### Changed (39)

- `C/KRC/User/ConfigMon.ini` - controller configuration - binary, 13354 bytes
- `C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8.asz` - controller configuration - binary, 4334403 bytes
- `C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8.log` - controller configuration - 333 line(s) removed, 329 added - diffs/C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8.log.diff
- `C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8_old.log` - controller configuration - 329 line(s) removed, 333 added - diffs/C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8_old.log.diff
- `C/KRC/User/Settings.xml` - controller configuration - 1 line(s) removed, 1 added - diffs/C/KRC/User/Settings.xml.diff
- `KRC/R1/Mada/$machine.dat` - machine data
- `KRC/R1/Mada/$robcor.dat` - machine data
- `KRC/R1/Program/Centerline/centerline_weld.src` - integrator program
- `KRC/R1/Program/Centerline/gun_open_check.dat` - integrator program
- `KRC/R1/Program/Centerline/gun_open_check.src` - integrator program
- `KRC/R1/Program/Centerline/preload.dat` - integrator program
- `KRC/R1/Program/Centerline/preload.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app2opt1.dat` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app2opt1.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app2opt2.src` - integrator program
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt2autorr.dat` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.dat` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.dat` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.src` - integrator program
- `KRC/R1/Program/Styles/optiones/style1opt1.src` - integrator program
- `KRC/R1/Program/Styles/optiones/style1opt10autorr.src` - integrator program
- `KRC/R1/Program/home.dat` - integrator program
- `KRC/R1/Program/home.src` - integrator program
- `KRC/R1/System/$config.dat` - integrator program
- `KRC/R1/System/sps.sub` - integrator program
- `KRC/R1/System/tm_bib.dat` - KUKA system / vendor package
- `KRC/R1/System/tm_bib.src` - KUKA system / vendor package
- `KRC/R1/TP/AutomationCore/automationcoredata.dat` - KUKA system / vendor package
- `KRC/R1/TP/AutomationCore/automationcoreroutines.dat` - KUKA system / vendor package
- `KRC/R1/TP/GripperSpotTech/grp_data.dat` - KUKA system / vendor package
- `KRC/R1/TP/GripperSpotTech/grp_func.dat` - KUKA system / vendor package
- `KRC/R1/TP/NutWeld/nutwelddata.dat` - KUKA system / vendor package
- `KRC/R1/TP/NutWeld/nutweldroutines.dat` - KUKA system / vendor package
- `KRC/R1/TP/NutWeld/nutweldroutines.src` - KUKA system / vendor package
- `KRC/STEU/Mada/$custom.dat` - machine data
- `Registry/LMSOFTWAREKUKA ROBOTER GMBHWorkVisual.amr` - controller configuration - 2 line(s) removed, 2 added - diffs/Registry/LMSOFTWAREKUKA ROBOTER GMBHWorkVisual.amr.diff
- `Registry/LMSOFTWAREKUKA Roboter GmbHPerformance.amr` - controller configuration - 25 line(s) removed, 25 added - diffs/Registry/LMSOFTWAREKUKA Roboter GmbHPerformance.amr.diff
- `am.ini` - archive metadata - 3 line(s) removed, 3 added - diffs/am.ini.diff

### Added (1)

- `C/KRC/User/ConfigMonold.ini` - controller configuration - binary, 3362 bytes

### Missing from the backup (0)

_none_

### Outside the archive layout (ignored) (2)

- `Archive.log`
- `ArchiveInfo.xml`

## Code changes

### `KRC/R1/Program/Centerline/centerline_weld.src`

changed, integrator program: 1 code line(s) removed, 2 added; 3 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/centerline_weld.src.diff](diffs/KRC/R1/Program/Centerline/centerline_weld.src.diff)

```diff
@@ base line 310, backup line 310 @@
    310  ENDIF
    314  dopw1_GunWork=FALSE
-   315  dopw1_GunHome=TRUE
    317  do498UpperPinExtend=FALSE
    318  do499UpperPinRetract=TRUE
+   320  WAIT SEC 0.2
+   321  dopw1_GunHome=TRUE
    326  GUN_OPEN_CHECK()
    331  do501PartClampClose=FALSE
```

### `KRC/R1/Program/Centerline/preload.dat`

changed, integrator program: 1 code line(s) removed, 0 added; 2 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/preload.dat.diff](diffs/KRC/R1/Program/Centerline/preload.dat.diff)

Attributes: -&ACCESS RVO5; +&ACCESS  RV; +&COMMENT 03-10-R1 PNW1 NUT PRELOAD; +&PARAM DISKPATH = Program/Centerline

Data changes:

- removed 1 INT: nFeedSettleMs

```diff
@@ base line 22, backup line 24 @@
     24  DECL GLOBAL BOOL bPinDownSensor=FALSE
     27  DECL GLOBAL INT nPinUpMs=300
-    28  DECL GLOBAL INT nFeedSettleMs=3000
     28  ENDDAT
```

### `KRC/R1/Program/Centerline/preload.src`

changed, integrator program: 4 code line(s) removed, 2 added; 6 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/preload.src.diff](diffs/KRC/R1/Program/Centerline/preload.src.diff)

```diff
@@ base line 94, backup line 94 @@
     94  $TIMER_STOP[10]=FALSE
     95  ENDIF
-    99  IF $TIMER[10]>=(2000+nFeedSettleMs) THEN
+    98  IF $TIMER[10]>=2000 THEN
     99  $TIMER_STOP[10]=TRUE
    101  STEP0DONE=TRUE
@@ base line 263, backup line 262 @@
    262  ENDIF
    265  IF (dipw1_SpearHome==TRUE) AND (di470QFPAdvanced==FALSE) THEN
+   267  dopw1_StartFeed=TRUE
    268  IF $TIMER_STOP[10] THEN
-   272  dopw1_StartFeed=TRUE
    269  $TIMER[10]=0
    270  $TIMER_STOP[10]=FALSE
@@ base line 276, backup line 272 @@
    272  IF $TIMER[10]>=2000 THEN
    273  dopw1_StartFeed=FALSE
-   278  ENDIF
-   279  IF $TIMER[10]>=(2000+nFeedSettleMs) THEN
    274  QFP_NUT_LOADED=TRUE
    275  NUT_PRELOAD_STEP = 40
```

### `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`

changed, integrator program: 1 code line(s) removed, 6 added; 5 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.src.diff)

```diff
@@ base line 50, backup line 50 @@
     50  do080RepositionTooling1=TRUE
     53  WAIT FOR di080ToolRepositioned1
-    60  WAIT SEC 2.0
+    63  $TIMER_STOP[17]=TRUE
+    64  $TIMER[17]=0
+    65  $TIMER_STOP[17]=FALSE
+    66  WAIT FOR (di100CameraJudgmentOK EXOR di101CameraJudgmentNG) OR ($TIMER[17]>=5000)
+    67  WAIT SEC 0.1
+    68  $TIMER_STOP[17]=TRUE
     69  SWITCH nOption
     70  CASE 1,2,7,8
```

### `KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.dat`

changed, integrator program: 4 code line(s) removed, 7 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.dat.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.dat.diff)

Attributes: &ACCESS RVO1 -> &ACCESS RVO2; &REL 61 -> &REL 58; &COMMENT St1_PICK_GE4 -> &COMMENT 03-10-R1 PICK ST1

Data changes:

- XAtPick3 (E6POS) re-taught: moved 0.5 mm
- added 2 E6POS: XP1, XP2
- added 2 FDAT: FP1, FP2
- added 2 PDAT: PPDAT1, PPDAT3
- removed 1 E6POS: XP16
- removed 1 FDAT: FP16
- removed 1 PDAT: PPDAT18

```diff
@@ base line 23, backup line 23 @@
     23  DECL E6POS XP10={X 1081.09485,Y -250.197342,Z 931.476,A -96.8303,B 37.9899406,C -15.7576666,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     24  DECL FDAT FP10={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    25  DECL E6POS XAtPick3={X 1206.28552,Y -208.912048,Z 214.158249,A -91.4409,B -0.232809141,C 0.168289974,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    25  DECL E6POS XAtPick3={X 1206.28552,Y -208.912048,Z 214.640366,A -91.4409,B -0.232809022,C 0.168290094,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     26  DECL FDAT FAtPick3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     27  DECL E6POS XP40={X 1206.28552,Y -208.912048,Z 630.625366,A -91.4409,B -0.232809082,C 0.168290034,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
@@ base line 40, backup line 40 @@
     40  DECL FDAT FP12={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     41  DECL PDAT PPDAT15={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    42  DECL PDAT PPDAT18={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    43  DECL E6POS XP16={X -77.5694046,Y -1731.18909,Z 1086.30457,A -91.6320343,B 0.265882939,C -0.0392194763,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    44  DECL FDAT FP16={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    42  DECL E6POS XP1={X -724.403137,Y -1811.34314,Z 1367.20557,A -104.758530,B 0.614156485,C 179.947769,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    43  DECL FDAT FP1={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    44  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    45  DECL E6POS XP2={X -391.021637,Y -1718.64941,Z 1886.74170,A -101.501625,B -31.6927509,C 144.874908,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    46  DECL FDAT FP2={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    47  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     48  ENDDAT
```

### `KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.src`

changed, integrator program: 6 code line(s) removed, 10 added; 17 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.src.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.src.diff)

Attributes: &ACCESS RVO1 -> &ACCESS RVO2; &REL 61 -> &REL 58; &COMMENT 03-10-R1 RED RABBIT PICK -> &COMMENT 03-10-R1 PICK ST1

```diff
@@ base line 38, backup line 37 @@
     37  WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2)
     46  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
-    58  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO NUT_START=TRUE
     58  $BWDSTART=FALSE
     59  PDAT_ACT=PPDAT15
@@ base line 140, backup line 138 @@
    138  FDAT_ACT=FP8
    139  BAS(#PTP_PARAMS,100)
-   142  PTP XP8
+   140  PTP XP8 C_DIS
    143  $BWDSTART=FALSE
-   147  PDAT_ACT=PPDAT18
-   148  FDAT_ACT=FP16
-   149  BAS(#PTP_PARAMS,60)
-   150  PTP XP16
+   144  PDAT_ACT=PPDAT3
+   145  FDAT_ACT=FP2
+   146  BAS(#PTP_PARAMS,100)
+   147  PTP XP2 C_DIS
+   150  $BWDSTART=FALSE
+   151  PDAT_ACT=PPDAT1
+   152  FDAT_ACT=FP1
+   153  BAS(#PTP_PARAMS,100)
+   154  PTP XP1 C_DIS
    162  AC_pickUP (1,True)
    164  END
```

### `KRC/R1/System/sps.sub`

changed, integrator program: 16 code line(s) removed, 8 added; 30 comment/blank line change(s). Full diff: [diffs/KRC/R1/System/sps.sub.diff](diffs/KRC/R1/System/sps.sub.diff)

```diff
@@ base line 93, backup line 93 @@
     93  ENDIF
     97  GRPg_ChkSetStatePLC()
+   105  NutWeld_BKG ( )
    124  CL_GunStrokePositionLPT=(CL_LPT_BYTE1*65536)+(CL_LPT_BYTE2*256)+CL_LPT_BYTE3
    128  CL_WeldPinPosition=(CL_PIN_BYTE0*256)+CL_PIN_BYTE1
@@ base line 152, backup line 154 @@
    154  ENDIF
    156  CL_WaterOk = dipw1_WaterOk
-   162  dopw1_LowLevel = CL_WeldFault OR dipw1_Fault
-   163  dopw1_LevelOk = NOT (CL_WeldFault OR dipw1_Fault)
    175  IF dopw1_LowLevel THEN
    176  CL_BeaconBit3008 = TRUE
@@ base line 192, backup line 196 @@
    196  dopw1_StartWater=di013WaterEnable AND NOT do091RobotReadyCapChange
    202  do111Gun1ElectrodeChange=dipw1_EndOfStepper
-   200  IF ((dipw1_StepperWarning==FALSE) AND (dipw1_EndOfStepper==FALSE)) THEN
-   202  dopw1_StepperWarningPL=TRUE
-   203  dopw1_EndofStepperPL=FALSE
-   204  ELSE
-   205  IF ((dipw1_StepperWarning==TRUE) AND (dipw1_EndOfStepper==FALSE)) THEN
-   207  dopw1_StepperWarningPL=TRUE
-   208  dopw1_EndofStepperPL=TRUE
-   209  ELSE
-   210  IF (dipw1_EndOfStepper==TRUE) THEN
-   212  dopw1_StepperWarningPL=FALSE
-   213  dopw1_EndofStepperPL=TRUE
-   214  ENDIF
-   215  ENDIF
-   216  ENDIF
    227  IF di004UseDryCycle THEN
    228  dopw1_WeldContactEnable=FALSE
@@ base line 240, backup line 245 @@
    245  do094AirOK= dipw1_AirOK
    246  do013WaterIsOn = dipw1_WaterOk
+   251  IF (VARSTATE("$POS_ACT")==#INITIALIZED) THEN
+   252  ON_ERROR_PROCEED
+   253  PosCheck = $POS_ACT
+   254  IF ($ERR.NUMBER<>1419) THEN
+   255  do009RobotAtRepair=AC_CheckSphWZ(xRepair,$Repair_POS_TOL)
+   256  ENDIF
+   257  ENDIF
    263  PRELOAD()
    269  ENDLOOP
```

### `KRC/R1/TP/GripperSpotTech/grp_data.dat`

changed, KUKA system / vendor package: 1 code line(s) removed, 1 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/TP/GripperSpotTech/grp_data.dat.diff](diffs/KRC/R1/TP/GripperSpotTech/grp_data.dat.diff)

Data changes:

- GRPg_SignVal (INT): 11310649 -> 8610918

```diff
@@ base line 20, backup line 20 @@
     20  GLOBAL BOOL GRPg_GhostMode=False
     21  GLOBAL INT GRPg_GhostInput=0
-    22  GLOBAL INT GRPg_SignVal=11310649
+    22  GLOBAL INT GRPg_SignVal=8610918
     23  DECL GLOBAL GRP_ErrStrategy_T GRPg_ErrStrategy[3]
     24  GRPg_ErrStrategy[1]=#DialAtT1T2
```

### `KRC/R1/TP/NutWeld/nutweldroutines.dat`

changed, KUKA system / vendor package: 1 code line(s) removed, 1 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/TP/NutWeld/nutweldroutines.dat.diff](diffs/KRC/R1/TP/NutWeld/nutweldroutines.dat.diff)

Attributes: -&ACCESS RVO3; +&ACCESS  RV; +&PARAM DISKPATH = KRC:\R1\TP\NutWeld; -&PARAM DISKPATH = KRC:\R1\TP\NutWeld

Data changes:

- nNutWeldGunNrSTK (INT): 3 -> 1

Runtime values (left out of the code diff): rLowerLVDT: 11674.0 -> 15834.0

```diff
@@ base line 35, backup line 35 @@
     35  DECL GLOBAL BOOL bNutWeldWOJoinSTK=TRUE
     36  DECL GLOBAL BOOL bNutWeldResetSTK=FALSE
-    39  DECL GLOBAL INT nNutWeldGunNrSTK=3
+    39  DECL GLOBAL INT nNutWeldGunNrSTK=1
     40  DECL GLOBAL BOOL bNutWeldOpnGunSTK=FALSE
     41  DECL GLOBAL BOOL bNutWeldClsGunSTK=FALSE
```

### `KRC/R1/TP/NutWeld/nutweldroutines.src`

changed, KUKA system / vendor package: 3 code line(s) removed, 33 added; 119 comment/blank line change(s). Full diff: [diffs/KRC/R1/TP/NutWeld/nutweldroutines.src.diff](diffs/KRC/R1/TP/NutWeld/nutweldroutines.src.diff)

```diff
@@ base line 30, backup line 30 @@
     30  DECL BOOL bSensorRetry
     33  dopw1_Hidraulyc_Valve = ($PERI_RDY==TRUE)
+    37  IF nMaxGunNr>=2 THEN
     38  dopw2_Hidraulyc_Valve = (($PERI_RDY==TRUE) AND (nMaxGunNr>=2))
+    39  ENDIF
+    40  IF nMaxGunNr>=3 THEN
     41  dopw3_Hidraulyc_Valve = (($PERI_RDY==TRUE) AND (nMaxGunNr>=3))
+    42  ENDIF
     43  IF (($EXT==TRUE) AND (bNutWeld_InhibitWeld==TRUE)) THEN
     44  bNutWeld_InhibitWeld=FALSE
@@ base line 953, backup line 960 @@
    960  ENDIF
    961  ENDIF
-   961  IF (dipw1_HopperLowLevel==TRUE) THEN
+   971  IF (dipw1_HopperLowLevel==TRUE) AND NOT (CL_WeldFault OR dipw1_Fault) THEN
    973  dopw1_LevelOk=TRUE
    974  dopw1_LowLevel=FALSE
    975  ELSE
-   966  IF (dipw1_HopperLowLevel==FALSE) THEN
    977  dopw1_LevelOk=FALSE
    978  dopw1_LowLevel=TRUE
    979  ENDIF
-   970  ENDIF
+   982  IF nMaxGunNr>=2 THEN
    984  IF (dipw2_HopperLowLevel==TRUE) THEN
    985  dopw2_LevelOk=TRUE
@@ base line 982, backup line 992 @@
    992  ENDIF
    993  ENDIF
+   994  ENDIF
+   997  IF nMaxGunNr>=3 THEN
    999  IF (dipw3_HopperLowLevel==TRUE) THEN
   1000  dopw3_LevelOk=TRUE
@@ base line 993, backup line 1005 @@
   1005  dopw3_LevelOk=FALSE
   1006  dopw3_LowLevel=TRUE
+  1007  ENDIF
   1008  ENDIF
   1009  ENDIF
@@ base line 1016, backup line 1029 @@
   1029  ENDIF
   1030  ENDIF
+  1033  IF nMaxGunNr>=2 THEN
   1035  IF ((dipw2_StepperWarning==FALSE) AND (dipw2_EndOfStepper==FALSE)) THEN
   1036  dopw2_StepperWarningPL=TRUE
@@ base line 1035, backup line 1049 @@
   1049  ENDIF
   1050  ENDIF
+  1051  ENDIF
+  1054  IF nMaxGunNr>=3 THEN
   1056  IF ((dipw3_StepperWarning==FALSE) AND (dipw3_EndOfStepper==FALSE)) THEN
   1057  dopw3_StepperWarningPL=TRUE
@@ base line 1051, backup line 1067 @@
   1067  dopw3_StepperWarningPL=FALSE
   1068  dopw3_EndofStepperPL=TRUE
+  1069  ENDIF
   1070  ENDIF
   1071  ENDIF
@@ base line 1241, backup line 1258 @@
```
_35 more lines: see diffs/KRC/R1/TP/NutWeld/nutweldroutines.src.diff_

### Runtime values only

A .dat keeps the last value the program wrote to each of its variables, and the inline-form editor keeps its suggestions (LAST_BASIS...): these files changed only in such values, nobody edited them.

| File | Values | Diff |
|---|---|---|
| `KRC/R1/Program/Centerline/gun_open_check.dat` | nWaterFlow: 231 -> 222 | diffs/KRC/R1/Program/Centerline/gun_open_check.dat.diff |
| `KRC/R1/System/$config.dat` | CL_GunStrokePositionLPT: 139760 -> 139750; CL_WeldPinPosition: 27367 -> 27383 | diffs/KRC/R1/System/$config.dat.diff |
| `KRC/R1/System/tm_bib.dat` | iTQM_LAST_OVPRO: 100 -> 0; TQM_ACT: {T11 200,T12 200,T13 200,T14 200,T15 200... -> {T11 200,T12 200,T13 200,T14 200,T15 200... | diffs/KRC/R1/System/tm_bib.dat.diff |
| `KRC/R1/TP/AutomationCore/automationcoredata.dat` | nAutoCore_Handle: 10263 -> 10557; nCycleStart_Handle: 10553 -> 10726; nCycleTime: 39 -> 26; nCycTime_Handle: 10552 -> 10725; nLogOnlyMsg_Handle: 10136 -> 10688 | diffs/KRC/R1/TP/AutomationCore/automationcoredata.dat.diff |
| `KRC/R1/TP/GripperSpotTech/grp_func.dat` | GRPg_ProcessData: {ActGrp 1,ReqState 0,LastGrpNo 1,LastStN... -> {ActGrp 1,ReqState 0,LastGrpNo 3,LastStN... | diffs/KRC/R1/TP/GripperSpotTech/grp_func.dat.diff |
| `KRC/R1/TP/NutWeld/nutwelddata.dat` | bNutWeldWOJoining: TRUE -> FALSE; rNutSensorValue[3]: 11674.0 -> 15834.0 | diffs/KRC/R1/TP/NutWeld/nutwelddata.dat.diff |

### Comment-only changes

| File | Comment/blank line changes | Attributes | Diff |
|---|---|---|---|
| `KRC/R1/Mada/$machine.dat` | 0 | -&ACCESS RV$; +&ACCESS  RV; +&PARAM VERSION = 1.0.0; +&PARAM DISKPATH = MADA | diffs/KRC/R1/Mada/$machine.dat.diff |
| `KRC/R1/Mada/$robcor.dat` | 0 | +&PARAM VERSION = 1.0.0; -&PARAM VERSION = 1.0.0 | diffs/KRC/R1/Mada/$robcor.dat.diff |
| `KRC/R1/Program/Centerline/gun_open_check.src` | 0 | &REL 25 -> &REL 29 | diffs/KRC/R1/Program/Centerline/gun_open_check.src.diff |
| `KRC/R1/Program/StyleApps/Options/style1app2opt1.dat` | 0 | &ACCESS RVO1 -> &ACCESS RVO2 | diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.dat.diff |
| `KRC/R1/Program/StyleApps/Options/style1app2opt1.src` | 0 | &ACCESS RVO1 -> &ACCESS RVO2 | diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.src.diff |
| `KRC/R1/Program/StyleDrops/Options/style1drop1opt2autorr.dat` | 0 | &COMMENT GE4_Conveyor -> &COMMENT 03-10-R1 RED RABBIT DROP | diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt2autorr.dat.diff |
| `KRC/R1/Program/StylePicks/Options/style1pick1opt1.dat` | 0 | &ACCESS RVO1 -> &ACCESS RVO2 | diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1.dat.diff |
| `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src` | 0 | &ACCESS RVO1 -> &ACCESS RVO2 | diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1.src.diff |
| `KRC/R1/Program/Styles/optiones/style1opt1.src` | 0 | &ACCESS RVO1 -> &ACCESS RVP1 | diffs/KRC/R1/Program/Styles/optiones/style1opt1.src.diff |
| `KRC/R1/Program/Styles/optiones/style1opt10autorr.src` | 0 | &ACCESS RVO1 -> &ACCESS RVP1 | diffs/KRC/R1/Program/Styles/optiones/style1opt10autorr.src.diff |
| `KRC/R1/Program/home.dat` | 0 | &ACCESS RVO1 -> &ACCESS RVP1 | diffs/KRC/R1/Program/home.dat.diff |
| `KRC/R1/Program/home.src` | 0 | &ACCESS RVO1 -> &ACCESS RVP1 | diffs/KRC/R1/Program/home.src.diff |
| `KRC/R1/System/tm_bib.src` | 0 | &ACCESS R5 -> &ACCESS R2; &REL 962 -> &REL 964 | diffs/KRC/R1/System/tm_bib.src.diff |
| `KRC/R1/TP/AutomationCore/automationcoreroutines.dat` | 0 | -&ACCESS RO5; +&ACCESS  R; +&PARAM DISKPATH = TP/AutomationCore; +&REL 11 | diffs/KRC/R1/TP/AutomationCore/automationcoreroutines.dat.diff |
| `KRC/STEU/Mada/$custom.dat` | 0 | +&PARAM VERSION = 1.0.0; -&PARAM VERSION = 1.0.0 | diffs/KRC/STEU/Mada/$custom.dat.diff |

## Mechanical checks

### FAIL (0)

_none_

### WARN (19)

- `KRC/R1/Program/StyleApps/Options/style1app2opt2.src:66` [8 I/O without signal comment] di100CameraJudgmentOK, di101CameraJudgmentNG accessed with no comment naming it in the 4 lines above (C24): WAIT FOR (di100CameraJudgmentOK EXOR di101CameraJudgmentNG) OR ($TIMER
- `KRC/R1/System/sps.sub:166` [6 commented-out code] commented-out code (assignment): ;dopw1_LowLevel = CL_WeldFault OR dipw1_Fault
- `KRC/R1/System/sps.sub:167` [6 commented-out code] commented-out code (assignment): ;dopw1_LevelOk = NOT (CL_WeldFault OR dipw1_Fault)
- `KRC/R1/System/sps.sub:205` [6 commented-out code] commented-out code (IF): ;IF ((dipw1_StepperWarning==FALSE) AND (dipw1_EndOfStepper==FALSE)) THEN
- `KRC/R1/System/sps.sub:207` [6 commented-out code] commented-out code (assignment): ;dopw1_StepperWarningPL=TRUE
- `KRC/R1/System/sps.sub:208` [6 commented-out code] commented-out code (assignment): ;dopw1_EndofStepperPL=FALSE
- `KRC/R1/System/sps.sub:209` [6 commented-out code] commented-out code (ELSE): ;ELSE
- `KRC/R1/System/sps.sub:210` [6 commented-out code] commented-out code (IF): ;IF ((dipw1_StepperWarning==TRUE) AND (dipw1_EndOfStepper==FALSE)) THEN
- `KRC/R1/System/sps.sub:212` [6 commented-out code] commented-out code (assignment): ;dopw1_StepperWarningPL=TRUE
- `KRC/R1/System/sps.sub:213` [6 commented-out code] commented-out code (assignment): ;dopw1_EndofStepperPL=TRUE
- `KRC/R1/System/sps.sub:214` [6 commented-out code] commented-out code (ELSE): ;ELSE
- `KRC/R1/System/sps.sub:215` [6 commented-out code] commented-out code (IF): ;IF (dipw1_EndOfStepper==TRUE) THEN
- `KRC/R1/System/sps.sub:217` [6 commented-out code] commented-out code (assignment): ;dopw1_StepperWarningPL=FALSE
- `KRC/R1/System/sps.sub:218` [6 commented-out code] commented-out code (assignment): ;dopw1_EndofStepperPL=TRUE
- `KRC/R1/System/sps.sub:219` [6 commented-out code] commented-out code (ENDIF): ;ENDIF
- `KRC/R1/System/sps.sub:220` [6 commented-out code] commented-out code (ENDIF): ;ENDIF
- `KRC/R1/System/sps.sub:221` [6 commented-out code] commented-out code (ENDIF): ;ENDIF
- `KRC/R1/System/sps.sub:254` [8 I/O without signal comment] ERR accessed with no comment naming it in the 4 lines above (C24): IF ($ERR.NUMBER<>1419) THEN
- `KRC/R1/System/sps.sub:255` [8 I/O without signal comment] do009RobotAtRepair accessed with no comment naming it in the 4 lines above (C24): do009RobotAtRepair=AC_CheckSphWZ(xRepair,$Repair_POS_TOL)

### INFO (0)

_none_
