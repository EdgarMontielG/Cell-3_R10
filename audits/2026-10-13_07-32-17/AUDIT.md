# Backup audit - fc022d57-BMW_03_WINDOWS-2CPT70E_BMW_03_10_R1_658424.zip

- Backup: `/root/.claude/uploads/50f56c92-2919-5ae3-94c9-0de4476bbe87/fc022d57-BMW_03_WINDOWS-2CPT70E_BMW_03_10_R1_658424.zip` (sha256 `6819763dc1b260dd...`)
- am.ini: archive `C:\windows\TEMP\tmp5821.tmp\`, date `2026-10-13_07-32-17`, config `All`, robot `BMW_03_10_R1`, serial `658424`, KSS `V8.3.29`
- Compared with: `HEAD` = `cd7409d305` "R10 program audit for the Gestamp buy-off workbook NA-FM-71-070"; first commit (archive as received) `22a98cc8ef`
- Generated 2026-10-13T12:04:17 by tools/audit_backup.py

## Summary

| | |
|---|---|
| Entries audited (Log Files/ skipped: 8) | 323 |
| Unchanged | 267 |
| Changed | 54 |
| Added | 0 |
| Missing from the backup | 0 |
| **Deleted modules still on the controller** | 0 |
| **Pre-cleanup files** | 0 |
| Edited on top of the pre-cleanup file | 0 |
| KRL files with code changes | 3 |
| Code lines removed / added | 6 / 28 |
| KRL files with comment-only changes | 43 |
| KRL files with runtime values only (written by the program, not edits) | 4 |
| Checks FAIL / WARN / INFO | 0 / 1 / 0 |

**Needs attention:**

- WARN 2 entries outside the KUKA archive layout ignored (e.g. Archive.log)
- WARN KRC/R1/System/ir_stopm.src: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- 1 WARN in the mechanical checks

## The backup itself

- WARN: 2 entries outside the KUKA archive layout ignored (e.g. Archive.log)
- WARN: KRC/R1/System/ir_stopm.src: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- INFO: KRC/R1/System/tm_bib.dat: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- INFO: KRC/R1/TP/AutomationCore/automationglobalpos.dat: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)

## Deleted modules still present

_none_

## Pre-cleanup files

_none_

## Files

### Changed (54)

- `C/KRC/Roboter/Config/User/Common/PersistPC/KrcRrtLog.xml` - controller configuration - 1 line(s) removed, 1 added - diffs/C/KRC/Roboter/Config/User/Common/PersistPC/KrcRrtLog.xml.diff
- `C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8.asz` - controller configuration - binary, 4301487 bytes
- `KRC/R1/Program/Centerline/centerline_home.src` - integrator program
- `KRC/R1/Program/Centerline/centerline_weld.src` - integrator program
- `KRC/R1/Program/Centerline/gun_open_check.dat` - integrator program
- `KRC/R1/Program/Centerline/gun_open_check.src` - integrator program
- `KRC/R1/Program/Centerline/preload.dat` - integrator program
- `KRC/R1/Program/Centerline/preload.src` - integrator program
- `KRC/R1/Program/Centerline/request_next_nut.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt1a.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt1b.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt2a.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt2b.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt3a.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app1opt3b.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app2opt1.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app2opt2.src` - integrator program
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src` - integrator program
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt2autorr.src` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.src` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src` - integrator program
- `KRC/R1/Program/Styles/optiones/style1opt1.src` - integrator program
- `KRC/R1/Program/Styles/optiones/style1opt10autorr.src` - integrator program
- `KRC/R1/Program/Styles/style_1.src` - integrator program
- `KRC/R1/Program/Utilities/closeandcheckallclamps.src` - integrator program
- `KRC/R1/Program/Utilities/gunelectrodechange.src` - integrator program
- `KRC/R1/Program/Utilities/hometopounce.src` - integrator program
- `KRC/R1/Program/Utilities/hometorepair.src` - integrator program
- `KRC/R1/Program/Utilities/openandcheckallclamps.src` - integrator program
- `KRC/R1/Program/Utilities/pouncetohome.src` - integrator program
- `KRC/R1/Program/Utilities/rejectge4.src` - integrator program
- `KRC/R1/Program/Utilities/repairtohome.src` - integrator program
- `KRC/R1/Program/home.src` - integrator program
- `KRC/R1/Program/masref_user.src` - integrator program
- `KRC/R1/Program/tm_useraction.src` - integrator program
- `KRC/R1/System/$config.dat` - integrator program
- `KRC/R1/System/ir_stopm.src` - KUKA system / vendor package
- `KRC/R1/System/sps.sub` - integrator program
- `KRC/R1/System/tm_bib.dat` - KUKA system / vendor package
- `KRC/R1/TP/AutomationCore/automationcoredata.dat` - KUKA system / vendor package
- `KRC/R1/TP/AutomationCore/automationglobalpos.dat` - KUKA system / vendor package
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
- `Registry/LMSOFTWAREKUKA Roboter GmbHPerformance.amr` - controller configuration - 25 line(s) removed, 25 added - diffs/Registry/LMSOFTWAREKUKA Roboter GmbHPerformance.amr.diff
- `am.ini` - archive metadata - 3 line(s) removed, 3 added - diffs/am.ini.diff

### Added (0)

_none_

### Missing from the backup (0)

_none_

### Outside the archive layout (ignored) (2)

- `Archive.log`
- `ArchiveInfo.xml`

## Code changes

### `KRC/R1/Program/Centerline/gun_open_check.src`

changed, integrator program: 4 code line(s) removed, 26 added; 108 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/gun_open_check.src.diff](diffs/KRC/R1/Program/Centerline/gun_open_check.src.diff)

```diff
@@ base line 115, backup line 112 @@
    112  DECL INT nHandle
    113  DECL BOOL bRes
+   116  IF ($PRO_STATE0==#P_ACTIVE) AND (CL_GunStrokePositionLPT>=nGunOpenMin) AND (CL_GunStrokePositionLPT<=nGunOpenMax) AND CL_ClampOpen AND CL_PinRetracted THEN
+   117  RETURN
+   118  ENDIF
    120  BRAKE F
    123  Msg.Modul[]="GunOpenCheck"
@@ base line 157, backup line 158 @@
    158  WAIT SEC 0.1
    159  ENDWHILE
-   161  IF ($PRO_STATE0<>#P_ACTIVE) OR (CL_GunStrokePositionLPT<nGunOpenMin) OR (CL_GunStrokePositionLPT>nGunOpenMax) OR (NOT CL_ClampOpen) OR (NOT CL_PinRetracted) THEN
+   162  IF NOT (($PRO_STATE0==#P_ACTIVE) AND (CL_GunStrokePositionLPT>=nGunOpenMin) AND (CL_GunStrokePositionLPT<=nGunOpenMax) AND CL_ClampOpen AND CL_PinRetracted) THEN
+   163  Par[1].Par_Type=#EMPTY
+   164  IF $PRO_STATE0<>#P_ACTIVE THEN
    165  Msg.Nr=7
-   163  Msg.Msg_txt[]="Robot in welder waiting: Submit, gun open, clamp open, pin retracted"
-   164  Par[1].Par_Type=#EMPTY
+   166  Msg.Msg_txt[]="Robot in welder waiting: Submit (SPS) not running"
+   167  ELSE
+   168  IF (CL_GunStrokePositionLPT<nGunOpenMin) OR (CL_GunStrokePositionLPT>nGunOpenMax) THEN
+   169  Msg.Nr=7
+   170  Msg.Msg_txt[]="Robot in welder waiting: gun not open (pos. %1)"
+   171  Par[1].Par_Type=#VALUE
+   172  Par[1].Par_Int=CL_GunStrokePositionLPT
+   173  ELSE
+   174  IF NOT CL_ClampOpen THEN
+   175  Msg.Nr=7
+   176  Msg.Msg_txt[]="Robot in welder waiting: part clamp not open ($IN[466])"
+   177  ELSE
+   178  Msg.Nr=7
+   179  Msg.Msg_txt[]="Robot in welder waiting: upper pin not retracted (pos. %1)"
+   180  Par[1].Par_Type=#VALUE
+   181  Par[1].Par_Int=CL_WeldPinPosition
+   182  ENDIF
+   183  ENDIF
+   184  ENDIF
    185  nHandle=Set_KrlMsg(#STATE, Msg, Par[], Opt)
-   166  WHILE ($PRO_STATE0<>#P_ACTIVE) OR (CL_GunStrokePositionLPT<nGunOpenMin) OR (CL_GunStrokePositionLPT>nGunOpenMax) OR (NOT CL_ClampOpen) OR (NOT CL_PinRetracted)
+   186  WHILE NOT (($PRO_STATE0==#P_ACTIVE) AND (CL_GunStrokePositionLPT>=nGunOpenMin) AND (CL_GunStrokePositionLPT<=nGunOpenMax) AND CL_ClampOpen AND CL_PinRetracted)
    187  WAIT SEC 0.1
    188  ENDWHILE
```

### `KRC/R1/System/tm_bib.dat`

changed, KUKA system / vendor package: 1 code line(s) removed, 1 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/System/tm_bib.dat.diff](diffs/KRC/R1/System/tm_bib.dat.diff)

Data changes:

- iSTOP_TYPE (INT): 53 -> 20

Runtime values (left out of the code diff): iTQM_LAST_OVPRO: 0 -> 100; iTQM_ZEIGER: 2 -> 1; TQM_ACT: {T11 200,T12 200,T13 200,T14 200,T15 200... -> {T11 200,T12 200,T13 200,T14 200,T15 200...

```diff
@@ base line 36, backup line 36 @@
     36  REAL ScalingImpact=250000.0
     37  REAL TooLarge=100000.0
-    47  DECL INT iSTOP_TYPE=53
+    47  DECL INT iSTOP_TYPE=20
     48  DECL REAL rPAR=0.0
     50  GLOBAL INT iTQM_DELAY=150
```

### `KRC/R1/TP/AutomationCore/automationglobalpos.dat`

changed, KUKA system / vendor package: 1 code line(s) removed, 1 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/TP/AutomationCore/automationglobalpos.dat.diff](diffs/KRC/R1/TP/AutomationCore/automationglobalpos.dat.diff)

Data changes:

- XPOUNCE (E6POS) re-taught: moved 100.7 mm, rotated up to 0.1 deg

```diff
@@ base line 5, backup line 5 @@
      5  DEFDAT automationglobalpos PUBLIC
-    13  DECL GLOBAL E6POS XPOUNCE={X 874.811523,Y -100.694267,Z 2254.22876,A -4.40716410,B 2.42973685,C 0.669219,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    13  DECL GLOBAL E6POS XPOUNCE={X 873.497559,Y -100.437592,Z 2354.87305,A -4.40757895,B 2.34435153,C 0.659262061,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     14  DECL GLOBAL FDAT FPounce={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     15  DECL GLOBAL PDAT PPounce={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000}
```

### Runtime values only

A .dat keeps the last value the program wrote to each of its variables, and the inline-form editor keeps its suggestions (LAST_BASIS...): these files changed only in such values, nobody edited them.

| File | Values | Diff |
|---|---|---|
| `KRC/R1/TP/AutomationCore/automationcoredata.dat` | nAutoCore_Handle: 10557 -> 10729; nCycleStart_Handle: 10726 -> 10938; nCycleTime: 26 -> 67; nCycTime_Handle: 10725 -> 10937 | diffs/KRC/R1/TP/AutomationCore/automationcoredata.dat.diff |
| `KRC/R1/TP/GripperSpotTech/grp_func.dat` | GRP_iPreStNo: 1 -> 2; GRP_PreState[1]: {iGrpIn 257,iStInVal 1,bStInVal TRUE,bGh... -> {iGrpIn 257,iStInVal -1,bStInVal FALSE,b...; GRP_PreState[2]: {iGrpIn 258,iStInVal -1,bStInVal FALSE,b... -> {iGrpIn 258,iStInVal 1,bStInVal TRUE,bGh...; GRPg_ProcessData: {ActGrp 1,ReqState 0,LastGrpNo 3,LastStN... -> {ActGrp 1,ReqState 0,LastGrpNo 0,LastStN... | diffs/KRC/R1/TP/GripperSpotTech/grp_func.dat.diff |
| `KRC/R1/TP/NutWeld/nutwelddata.dat` | bNutWeldProcessReset: FALSE -> TRUE; bNutWeldWOJoining: FALSE -> TRUE; rNutSensorValue[3]: 15834.0 -> 2586.00 | diffs/KRC/R1/TP/NutWeld/nutwelddata.dat.diff |
| `KRC/R1/TP/NutWeld/nutweldroutines.dat` | rLowerLVDT: 15834.0 -> 2586.00 | diffs/KRC/R1/TP/NutWeld/nutweldroutines.dat.diff |

### Comment-only changes

| File | Comment/blank line changes | Attributes | Diff |
|---|---|---|---|
| `KRC/R1/Program/Centerline/centerline_home.src` | 39 | - | diffs/KRC/R1/Program/Centerline/centerline_home.src.diff |
| `KRC/R1/Program/Centerline/centerline_weld.src` | 221 | - | diffs/KRC/R1/Program/Centerline/centerline_weld.src.diff |
| `KRC/R1/Program/Centerline/gun_open_check.dat` | 42 | - | diffs/KRC/R1/Program/Centerline/gun_open_check.dat.diff |
| `KRC/R1/Program/Centerline/preload.dat` | 11 | - | diffs/KRC/R1/Program/Centerline/preload.dat.diff |
| `KRC/R1/Program/Centerline/preload.src` | 124 | - | diffs/KRC/R1/Program/Centerline/preload.src.diff |
| `KRC/R1/Program/Centerline/request_next_nut.src` | 8 | - | diffs/KRC/R1/Program/Centerline/request_next_nut.src.diff |
| `KRC/R1/Program/StyleApps/Options/style1app1opt1a.src` | 60 | - | diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1a.src.diff |
| `KRC/R1/Program/StyleApps/Options/style1app1opt1b.src` | 60 | - | diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1b.src.diff |
| `KRC/R1/Program/StyleApps/Options/style1app1opt2a.src` | 60 | - | diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2a.src.diff |
| `KRC/R1/Program/StyleApps/Options/style1app1opt2b.src` | 60 | - | diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2b.src.diff |
| `KRC/R1/Program/StyleApps/Options/style1app1opt3a.src` | 48 | - | diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3a.src.diff |
| `KRC/R1/Program/StyleApps/Options/style1app1opt3b.src` | 48 | - | diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3b.src.diff |
| `KRC/R1/Program/StyleApps/Options/style1app2opt1.src` | 46 | - | diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.src.diff |
| `KRC/R1/Program/StyleApps/Options/style1app2opt2.src` | 33 | - | diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.src.diff |
| `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src` | 24 | - | diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src.diff |
| `KRC/R1/Program/StyleDrops/Options/style1drop1opt2autorr.src` | 37 | - | diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt2autorr.src.diff |
| `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src` | 38 | - | diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1.src.diff |
| `KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.src` | 38 | - | diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.src.diff |
| `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src` | 41 | - | diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt2.src.diff |
| `KRC/R1/Program/Styles/optiones/style1opt1.src` | 26 | - | diffs/KRC/R1/Program/Styles/optiones/style1opt1.src.diff |
| `KRC/R1/Program/Styles/optiones/style1opt10autorr.src` | 13 | - | diffs/KRC/R1/Program/Styles/optiones/style1opt10autorr.src.diff |
| `KRC/R1/Program/Styles/style_1.src` | 9 | - | diffs/KRC/R1/Program/Styles/style_1.src.diff |
| `KRC/R1/Program/Utilities/closeandcheckallclamps.src` | 4 | - | diffs/KRC/R1/Program/Utilities/closeandcheckallclamps.src.diff |
| `KRC/R1/Program/Utilities/gunelectrodechange.src` | 88 | - | diffs/KRC/R1/Program/Utilities/gunelectrodechange.src.diff |
| `KRC/R1/Program/Utilities/hometopounce.src` | 6 | - | diffs/KRC/R1/Program/Utilities/hometopounce.src.diff |
| `KRC/R1/Program/Utilities/hometorepair.src` | 5 | - | diffs/KRC/R1/Program/Utilities/hometorepair.src.diff |
| `KRC/R1/Program/Utilities/openandcheckallclamps.src` | 4 | - | diffs/KRC/R1/Program/Utilities/openandcheckallclamps.src.diff |
| `KRC/R1/Program/Utilities/pouncetohome.src` | 6 | - | diffs/KRC/R1/Program/Utilities/pouncetohome.src.diff |
| `KRC/R1/Program/Utilities/rejectge4.src` | 27 | - | diffs/KRC/R1/Program/Utilities/rejectge4.src.diff |
| `KRC/R1/Program/Utilities/repairtohome.src` | 2 | - | diffs/KRC/R1/Program/Utilities/repairtohome.src.diff |
| `KRC/R1/Program/home.src` | 5 | - | diffs/KRC/R1/Program/home.src.diff |
| `KRC/R1/Program/masref_user.src` | 14 | - | diffs/KRC/R1/Program/masref_user.src.diff |
| `KRC/R1/Program/tm_useraction.src` | 3 | - | diffs/KRC/R1/Program/tm_useraction.src.diff |
| `KRC/R1/System/$config.dat` | 76 | - | diffs/KRC/R1/System/$config.dat.diff |
| `KRC/R1/System/ir_stopm.src` | 5 | - | diffs/KRC/R1/System/ir_stopm.src.diff |
| `KRC/R1/System/sps.sub` | 180 | - | diffs/KRC/R1/System/sps.sub.diff |
| `KRC/R1/TP/BrakeTest/braketestback.dat` | 0 | &ACCESS RVO7 -> &ACCESS RVO5 | diffs/KRC/R1/TP/BrakeTest/braketestback.dat.diff |
| `KRC/R1/TP/BrakeTest/braketestback.src` | 0 | &ACCESS RVO7 -> &ACCESS RVO5 | diffs/KRC/R1/TP/BrakeTest/braketestback.src.diff |
| `KRC/R1/TP/BrakeTest/braketestreq.dat` | 0 | &ACCESS RVO7 -> &ACCESS RVO5 | diffs/KRC/R1/TP/BrakeTest/braketestreq.dat.diff |
| `KRC/R1/TP/BrakeTest/braketestreq.src` | 0 | &ACCESS RVO7 -> &ACCESS RVO5 | diffs/KRC/R1/TP/BrakeTest/braketestreq.src.diff |
| `KRC/R1/TP/BrakeTest/braketeststart.dat` | 0 | &ACCESS RVO7 -> &ACCESS RVO5 | diffs/KRC/R1/TP/BrakeTest/braketeststart.dat.diff |
| `KRC/R1/TP/BrakeTest/braketeststart.src` | 0 | &ACCESS RVO7 -> &ACCESS RVO5 | diffs/KRC/R1/TP/BrakeTest/braketeststart.src.diff |
| `KRC/R1/cell.src` | 56 | - | diffs/KRC/R1/cell.src.diff |

## Mechanical checks

### FAIL (0)

_none_

### WARN (1)

- `KRC/R1/Program/Centerline/gun_open_check.src:176` [8 I/O without signal comment] $IN[466] accessed with no comment naming it in the 4 lines above (C24): Msg.Msg_txt[]="Robot in welder waiting: part clamp not open ($IN[466])

### INFO (0)

_none_
