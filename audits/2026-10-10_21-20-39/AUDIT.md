# Backup audit - ed7a88c5-V431_03_WINDOWS-2CPT70E_BMW_03_10_R1_658424.zip

- Backup: `/root/.claude/uploads/50f56c92-2919-5ae3-94c9-0de4476bbe87/ed7a88c5-V431_03_WINDOWS-2CPT70E_BMW_03_10_R1_658424.zip` (sha256 `5bbd1a59c40285b9...`)
- am.ini: archive `C:\windows\TEMP\tmpB87B.tmp\`, date `2026-10-10_21-20-39`, config `All`, robot `BMW_03_10_R1`, serial `658424`, KSS `V8.3.29`
- Compared with: `HEAD` = `e9363d05af` "Cycle time first: measurement delivery (CT_* timers as R20) on the programmer's backup; lever analysis"; first commit (archive as received) `22a98cc8ef`
- Generated 2026-10-11T13:46:08 by tools/audit_backup.py

## Summary

| | |
|---|---|
| Entries audited (Log Files/ skipped: 8) | 322 |
| Unchanged | 227 |
| Changed | 90 |
| Added | 3 |
| Missing from the backup | 19 |
| **Deleted modules still on the controller** | 0 |
| **Pre-cleanup files** | 0 |
| Edited on top of the pre-cleanup file | 0 |
| KRL files with code changes | 51 |
| Code lines removed / added | 1562 / 931 |
| KRL files with comment-only changes | 23 |
| KRL files with runtime values only (written by the program, not edits) | 0 |
| Checks FAIL / WARN / INFO | 12 / 55 / 32 |

**Needs attention:**

- WARN 2 entries outside the KUKA archive layout ignored (e.g. Archive.log)
- WARN 19 file(s) of the base missing from the backup - deleted on the robot, or an incomplete archive (e.g. C/KRC/User/ProjectRoot/@BaseProject/BaseProject.wvs; all in Files, "Missing from the backup")
- WARN KRC/R1/System/ir_stopm.src: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- **12 FAIL** in the mechanical checks
- 55 WARN in the mechanical checks

## The backup itself

- WARN: 2 entries outside the KUKA archive layout ignored (e.g. Archive.log)
- WARN: 19 file(s) of the base missing from the backup - deleted on the robot, or an incomplete archive (e.g. C/KRC/User/ProjectRoot/@BaseProject/BaseProject.wvs; all in Files, "Missing from the backup")
- WARN: KRC/R1/System/ir_stopm.src: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- INFO: KRC/R1/Program/Centerline/centerline_home.src: spelled KRC/R1/Program/Centerline/CENTERLINE_HOME.src in the base (the controller ignores case)
- INFO: KRC/R1/Program/Centerline/gun_open_check.src: spelled KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src in the base (the controller ignores case)
- INFO: KRC/R1/Program/Centerline/preload.dat: spelled KRC/R1/Program/Centerline/PRELOAD.dat in the base (the controller ignores case)
- INFO: KRC/R1/Program/Centerline/preload.src: spelled KRC/R1/Program/Centerline/PRELOAD.src in the base (the controller ignores case)
- INFO: KRC/R1/Program/Centerline/request_next_nut.dat: spelled KRC/R1/Program/Centerline/Request_next_nut.dat in the base (the controller ignores case)
- INFO: KRC/R1/Program/Centerline/request_next_nut.src: spelled KRC/R1/Program/Centerline/Request_next_nut.src in the base (the controller ignores case)
- INFO: KRC/R1/Program/StyleApps/Options/style1app1opt1a.dat: spelled KRC/R1/Program/StyleApps/Options/style1app1opt1A.dat in the base (the controller ignores case)
- INFO: KRC/R1/Program/StyleApps/Options/style1app1opt1a.src: spelled KRC/R1/Program/StyleApps/Options/style1app1opt1A.src in the base (the controller ignores case)
- INFO: KRC/R1/Program/StyleApps/Options/style1app1opt1b.dat: spelled KRC/R1/Program/StyleApps/Options/style1app1opt1B.dat in the base (the controller ignores case)
- INFO: KRC/R1/Program/StyleApps/Options/style1app1opt1b.src: spelled KRC/R1/Program/StyleApps/Options/style1app1opt1B.src in the base (the controller ignores case)
- INFO: KRC/R1/Program/StyleApps/Options/style1app1opt2a.dat: spelled KRC/R1/Program/StyleApps/Options/style1app1opt2A.dat in the base (the controller ignores case)
- INFO: KRC/R1/Program/StyleApps/Options/style1app1opt2a.src: spelled KRC/R1/Program/StyleApps/Options/style1app1opt2A.src in the base (the controller ignores case)
- INFO: KRC/R1/Program/StyleApps/Options/style1app1opt2b.dat: spelled KRC/R1/Program/StyleApps/Options/style1app1opt2B.dat in the base (the controller ignores case)
- INFO: KRC/R1/Program/StyleApps/Options/style1app1opt2b.src: spelled KRC/R1/Program/StyleApps/Options/style1app1opt2B.src in the base (the controller ignores case)
- INFO: KRC/R1/Program/StyleApps/Options/style1app1opt3a.dat: spelled KRC/R1/Program/StyleApps/Options/style1app1opt3A.dat in the base (the controller ignores case)
- INFO: KRC/R1/Program/StyleApps/Options/style1app1opt3a.src: spelled KRC/R1/Program/StyleApps/Options/style1app1opt3A.src in the base (the controller ignores case)
- INFO: KRC/R1/Program/StyleApps/Options/style1app1opt3b.dat: spelled KRC/R1/Program/StyleApps/Options/style1app1opt3B.dat in the base (the controller ignores case)
- INFO: KRC/R1/Program/StyleApps/Options/style1app1opt3b.src: spelled KRC/R1/Program/StyleApps/Options/style1app1opt3B.src in the base (the controller ignores case)
- INFO: KRC/R1/Program/StyleDrops/Options/style1drop1opt2autorr.dat: spelled KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.dat in the base (the controller ignores case)
- INFO: KRC/R1/Program/StyleDrops/Options/style1drop1opt2autorr.src: spelled KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src in the base (the controller ignores case)
- INFO: KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.dat: spelled KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.dat in the base (the controller ignores case)
- INFO: KRC/R1/Program/Utilities/electrodechange.dat: spelled KRC/R1/Program/Utilities/ElectrodeChange.dat in the base (the controller ignores case)
- INFO: KRC/R1/Program/Utilities/redrabbit.dat: spelled KRC/R1/Program/Utilities/RedRabbit.dat in the base (the controller ignores case)
- INFO: KRC/R1/Program/Utilities/rejectge4.dat: spelled KRC/R1/Program/Utilities/RejectGE4.dat in the base (the controller ignores case)
- INFO: KRC/R1/Program/Utilities/rejectge4.src: spelled KRC/R1/Program/Utilities/RejectGE4.src in the base (the controller ignores case)
- INFO: KRC/R1/Program/home.src: spelled KRC/R1/Program/HOME.src in the base (the controller ignores case)
- INFO: KRC/R1/Program/movetopurge.dat: spelled KRC/R1/Program/MoveToPurge.dat in the base (the controller ignores case)
- INFO: KRC/R1/Program/movetopurge.src: spelled KRC/R1/Program/MoveToPurge.src in the base (the controller ignores case)
- INFO: KRC/R1/Program/pounce.dat: spelled KRC/R1/Program/POUNCE.dat in the base (the controller ignores case)
- INFO: KRC/R1/Program/pounce.src: spelled KRC/R1/Program/POUNCE.src in the base (the controller ignores case)
- INFO: KRC/R1/System/tm_bib.dat: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- INFO: KRC/R1/TP/AutomationCore/automationcoredata.dat: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- INFO: KRC/R1/TP/AutomationCore/automationcoreroutines.dat: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- INFO: KRC/R1/TP/AutomationCore/automationglobalpos.dat: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- INFO: KRC/R1/TP/GripperSpotTech/grp_data.dat: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- INFO: KRC/R1/TP/NutWeld/nutweldroutines.dat: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)

## Deleted modules still present

_none_

## Pre-cleanup files

_none_

## Files

### Changed (90)

- `C/KRC/Roboter/Config/User/Common/HNFINFO.SAF` - controller configuration - binary, 32 bytes
- `C/KRC/Roboter/Config/User/Common/PNIOIM4Data.dat` - controller configuration
- `C/KRC/Roboter/Config/User/Common/PersistPC/KrcRrtLog.xml` - controller configuration - 5 line(s) removed, 5 added - diffs/C/KRC/Roboter/Config/User/Common/PersistPC/KrcRrtLog.xml.diff
- `C/KRC/Roboter/Config/User/Common/SCTLCRC.IMG` - controller configuration - binary, 99 bytes
- `C/KRC/Roboter/Config/User/Common/SCTLCRC.XML` - controller configuration - 1 line(s) removed, 1 added - diffs/C/KRC/Roboter/Config/User/Common/SCTLCRC.XML.diff
- `C/KRC/Roboter/Config/User/Common/SCTLPARA.SAF` - controller configuration - binary, 14269 bytes
- `C/KRC/Roboter/Config/User/Common/SCtlPara.sg` - controller configuration - binary, 26574 bytes
- `C/KRC/Roboter/Config/User/Common/SafetyConfigData.xml` - controller configuration - 4 line(s) removed, 28 added - diffs/C/KRC/Roboter/Config/User/Common/SafetyConfigData.xml.diff
- `C/KRC/Roboter/Ir_Spec/L_IDENT/$__Ident.idf` - controller configuration - 12 line(s) removed, 12 added - diffs/C/KRC/Roboter/Ir_Spec/L_IDENT/$__Ident.idf.diff
- `C/KRC/Roboter/Ir_Spec/L_IDENT/KukaLoadProject.658424.xml` - controller configuration - 1 line(s) removed, 46 added - diffs/C/KRC/Roboter/Ir_Spec/L_IDENT/KukaLoadProject.658424.xml.diff
- `C/KRC/Roboter/Rdc/RdcDirectoryContents.txt` - controller configuration - 3 line(s) removed, 3 added - diffs/C/KRC/Roboter/Rdc/RdcDirectoryContents.txt.diff
- `C/KRC/User/ConfigMon.ini` - controller configuration - binary, 3362 bytes
- `C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8.log` - controller configuration - 341 line(s) removed, 333 added - diffs/C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8.log.diff
- `C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8_old.log` - controller configuration - 371 line(s) removed, 329 added - diffs/C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8_old.log.diff
- `KRC/R1/Mada/$machine.dat` - machine data
- `KRC/R1/Mada/$robcor.dat` - machine data
- `KRC/R1/Program/Centerline/CENTERLINE_HOME.src` - integrator program
- `KRC/R1/Program/Centerline/centerline_weld.src` - integrator program
- `KRC/R1/Program/Centerline/gun_open_check.dat` - integrator program
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src` - integrator program
- `KRC/R1/Program/Centerline/PRELOAD.dat` - integrator program
- `KRC/R1/Program/Centerline/PRELOAD.src` - integrator program
- `KRC/R1/Program/Centerline/Request_next_nut.src` - integrator program
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
- `KRC/R1/Program/StyleApps/Options/style1app2opt1.dat` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app2opt1.src` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app2opt2.dat` - integrator program
- `KRC/R1/Program/StyleApps/Options/style1app2opt2.src` - integrator program
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.dat` - integrator program
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src` - integrator program
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.dat` - integrator program
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.dat` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.dat` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.src` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt2.dat` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src` - integrator program
- `KRC/R1/Program/Styles/optiones/style1opt1.src` - integrator program
- `KRC/R1/Program/Styles/optiones/style1opt10autorr.src` - integrator program
- `KRC/R1/Program/Styles/style_1.dat` - integrator program
- `KRC/R1/Program/Styles/style_1.src` - integrator program
- `KRC/R1/Program/Utilities/closeandcheckallclamps.dat` - integrator program
- `KRC/R1/Program/Utilities/closeandcheckallclamps.src` - integrator program
- `KRC/R1/Program/Utilities/gunelectrodechange.src` - integrator program
- `KRC/R1/Program/Utilities/hometopounce.src` - integrator program
- `KRC/R1/Program/Utilities/hometorepair.dat` - integrator program
- `KRC/R1/Program/Utilities/hometorepair.src` - integrator program
- `KRC/R1/Program/Utilities/openandcheckallclamps.dat` - integrator program
- `KRC/R1/Program/Utilities/openandcheckallclamps.src` - integrator program
- `KRC/R1/Program/Utilities/pouncetohome.src` - integrator program
- `KRC/R1/Program/Utilities/RejectGE4.dat` - integrator program
- `KRC/R1/Program/Utilities/RejectGE4.src` - integrator program
- `KRC/R1/Program/Utilities/repairtohome.dat` - integrator program
- `KRC/R1/Program/Utilities/repairtohome.src` - integrator program
- `KRC/R1/Program/home.dat` - integrator program
- `KRC/R1/Program/HOME.src` - integrator program
- `KRC/R1/Program/masref_user.dat` - integrator program
- `KRC/R1/Program/masref_user.src` - integrator program
- `KRC/R1/Program/tm_useraction.src` - integrator program
- `KRC/R1/System/$config.dat` - integrator program
- `KRC/R1/System/ir_stopm.src` - KUKA system / vendor package
- `KRC/R1/System/masref_main.dat` - KUKA system / vendor package
- `KRC/R1/System/masref_main.src` - KUKA system / vendor package
- `KRC/R1/System/sps.sub` - integrator program
- `KRC/R1/System/tm_bib.dat` - KUKA system / vendor package
- `KRC/R1/System/tm_bib.src` - KUKA system / vendor package
- `KRC/R1/TP/AutomationCore/automationcoredata.dat` - KUKA system / vendor package
- `KRC/R1/TP/AutomationCore/automationcoreroutines.dat` - KUKA system / vendor package
- `KRC/R1/TP/AutomationCore/automationglobalpos.dat` - KUKA system / vendor package
- `KRC/R1/TP/GripperSpotTech/grp_data.dat` - KUKA system / vendor package
- `KRC/R1/TP/GripperSpotTech/grp_func.dat` - KUKA system / vendor package
- `KRC/R1/TP/NutWeld/nutweldroutines.dat` - KUKA system / vendor package
- `KRC/R1/cell.src` - integrator program
- `KRC/R1/safetest.src` - integrator program
- `KRC/STEU/Mada/$machine.dat` - machine data
- `Registry/LMSOFTWAREKUKA ROBOTER GMBHKUKA BOFOCX Control'sFileHandler.amr` - controller configuration - 1391 line(s) removed, 1078 added - diffs/Registry/LMSOFTWAREKUKA ROBOTER GMBHKUKA BOFOCX Control'sFileHandler.amr.diff
- `Registry/LMSOFTWAREKUKA ROBOTER GMBHWorkVisual.amr` - controller configuration - 3 line(s) removed, 2 added - diffs/Registry/LMSOFTWAREKUKA ROBOTER GMBHWorkVisual.amr.diff
- `am.ini` - archive metadata - 3 line(s) removed, 3 added - diffs/am.ini.diff

### Added (3)

- `C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8.asz` - controller configuration - binary, 4329196 bytes
- `C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8.useDeployedProject` - controller configuration - 0 line(s) removed, 1 added - diffs/C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8.useDeployedProject.diff
- `Registry/LMSOFTWAREKUKA Roboter GmbHPerformance.amr` - controller configuration - 0 line(s) removed, 385 added - diffs/Registry/LMSOFTWAREKUKA Roboter GmbHPerformance.amr.diff

### Missing from the backup (19)

- `C/KRC/User/ProjectRoot/@BaseProject/BaseProject.wvs`
- `C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8.wvs`
- `C/KRC/User/ProjectRoot/V431-03-10R1_v6Active_Centerline_18/V431-03-10R1_v6Active_Centerline_18.log`
- `C/KRC/User/ProjectRoot/V431-03-10R1_v6Active_Centerline_18/V431-03-10R1_v6Active_Centerline_18.wvs`
- `C/KRC/User/ProjectRoot/V431-03-10R1_v6Active_Centerline_18/V431-03-10R1_v6Active_Centerline_18_old.log`
- `KRC/R1/Program/CK1STXXX.dat`
- `KRC/R1/Program/CK1STXXX.src`
- `KRC/R1/Program/Centerline/CENTERLINE_WELD1.src`
- `KRC/R1/Program/Centerline/centerline_loop.src`
- `KRC/R1/Program/Centerline/trigger1.dat`
- `KRC/R1/Program/Centerline/trigger1.src`
- `KRC/R1/Program/Centerline/trigger2.dat`
- `KRC/R1/Program/Centerline/trigger2.src`
- `KRC/R1/Program/Centerline/trigger3.dat`
- `KRC/R1/Program/Centerline/trigger3.src`
- `KRC/R1/Program/StyleApps/Options/style1app2opt1AutoRR.dat`
- `KRC/R1/Program/StyleApps/Options/style1app2opt1autorr.src`
- `KRC/R1/Program/StyleApps/Options/style1app2opt2AutoRR.dat`
- `KRC/R1/Program/StyleApps/Options/style1app2opt2autorr.src`

### Outside the archive layout (ignored) (2)

- `Archive.log`
- `ArchiveInfo.xml`

## Code changes

### `KRC/R1/Program/Centerline/CENTERLINE_HOME.src`

changed, integrator program: 18 code line(s) removed, 18 added; 66 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/CENTERLINE_HOME.src.diff](diffs/KRC/R1/Program/Centerline/CENTERLINE_HOME.src.diff)

Attributes: &COMMENT CENTERLINE HOME -> &COMMENT 03-10-R1 PNW1 MANUAL HOME

```diff
@@ base line 6, backup line 6 @@
      6  DEF CENTERLINE_HOME()
-    31  CL_GunPressureCmd=405
-    35  $OUT[473]=FALSE
-    36  $OUT[475]=FALSE
-    37  $OUT[476]=FALSE
-    38  $OUT[494]=FALSE
-    39  $OUT[500]=FALSE
-    40  $OUT[505]=FALSE
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
-    49  $OUT[503]=FALSE
+    51  do503QFPAdvance=FALSE
     52  WAIT SEC 0.2
-    51  $OUT[504]=TRUE
-    52  WAIT FOR $IN[482]
+    53  do504QFPReturn=TRUE
+    55  WAIT FOR dipw1_SpearHome
     56  WAIT SEC 0.5
-    56  $OUT[498]=FALSE
+    60  do498UpperPinExtend=FALSE
     61  WAIT SEC 0.2
-    58  $OUT[499]=TRUE
+    62  do499UpperPinRetract=TRUE
     63  WAIT SEC 1.0
-    62  $OUT[472]=FALSE
+    67  dopw1_GunWork=FALSE
     68  WAIT SEC 0.2
-    64  $OUT[471]=TRUE
+    69  dopw1_GunHome=TRUE
     70  WAIT SEC 1.5
-    68  $OUT[501]=FALSE
+    74  do501PartClampClose=FALSE
     75  WAIT SEC 0.2
-    70  $OUT[502]=TRUE
+    76  do502PartClampOpen=TRUE
     77  WAIT SEC 1.0
     79  END
```

### `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src`

changed, integrator program: 1 code line(s) removed, 252 added; 212 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src.diff](diffs/KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src.diff)

Attributes: &ACCESS RVO7 -> &ACCESS RVO5; &REL 4 -> &REL 25; &COMMENT NUT WELDER GUN OPEN CHECK -> &COMMENT 03-10-R1 PNW1 GUN OPEN CHECK

```diff
@@ base line 134, backup line 114 @@
    114  DECL KrlMsgOpt_T Opt
    115  DECL INT nHandle
+   116  DECL BOOL bRes
    118  BRAKE F
    121  Msg.Modul[]="GunOpenCheck"
@@ base line 152, backup line 133 @@
    133  Msg.Msg_txt[]="Submit (SPS) stopped while robot in welder - robot stopped, acknowledge"
    134  ELSE
+   135  IF (CL_GunStrokePositionLPT<nGunOpenMin) OR (CL_GunStrokePositionLPT>nGunOpenMax) THEN
    136  Msg.Nr=4
    137  Msg.Msg_txt[]="Gun not open while robot in welder (pos. %1) - robot stopped, acknowledge"
    138  Par[1].Par_Type=#VALUE
    139  Par[1].Par_Int=CL_GunStrokePositionLPT
+   140  ELSE
+   141  IF NOT CL_ClampOpen THEN
+   142  Msg.Nr=10
+   143  Msg.Msg_txt[]="Part clamp not open while robot in welder - robot stopped, acknowledge"
+   144  ELSE
+   145  Msg.Nr=11
+   146  Msg.Msg_txt[]="Upper pin not retracted in welder (pos. %1) - robot stopped, acknowledge"
+   147  Par[1].Par_Type=#VALUE
+   148  Par[1].Par_Int=CL_WeldPinPosition
+   149  ENDIF
+   150  ENDIF
    151  ENDIF
    152  nHandle=Set_KrlMsg(#QUIT, Msg, Par[], Opt)
-   163  WHILE Exists_KrlMsg(nHandle) OR ($PRO_STATE0<>#P_ACTIVE) OR (CL_GunStrokePositionLPT<nGunOpenMin) OR (CL_GunStrokePositionLPT>nGunOpenMax)
+   156  WHILE Exists_KrlMsg(nHandle)
    157  WAIT SEC 0.1
    158  ENDWHILE
+   161  IF ($PRO_STATE0<>#P_ACTIVE) OR (CL_GunStrokePositionLPT<nGunOpenMin) OR (CL_GunStrokePositionLPT>nGunOpenMax) OR (NOT CL_ClampOpen) OR (NOT CL_PinRetracted) THEN
+   162  Msg.Nr=7
+   163  Msg.Msg_txt[]="Robot in welder waiting: Submit, gun open, clamp open, pin retracted"
+   164  Par[1].Par_Type=#EMPTY
+   165  nHandle=Set_KrlMsg(#STATE, Msg, Par[], Opt)
+   166  WHILE ($PRO_STATE0<>#P_ACTIVE) OR (CL_GunStrokePositionLPT<nGunOpenMin) OR (CL_GunStrokePositionLPT>nGunOpenMax) OR (NOT CL_ClampOpen) OR (NOT CL_PinRetracted)
+   167  WAIT SEC 0.1
+   168  ENDWHILE
+   169  bRes=Clear_KrlMsg(nHandle)
+   170  ENDIF
    172  END
+   174  GLOBAL DEF PEDESTAL_CLEAR_CHECK( )
+   187  DECL KrlMsg_T Msg
+   188  DECL KrlMsgPar_T Par[3]
+   189  DECL KrlMsgOpt_T Opt
+   190  DECL INT nHandle, nWaitMs
+   191  DECL BOOL bRes
+   194  GUN_OPEN_CHECK()
+   197  Msg.Modul[]="GunOpenCheck"
+   198  Par[1].Par_Type=#EMPTY
+   199  Par[2].Par_Type=#EMPTY
+   200  Par[3].Par_Type=#EMPTY
+   201  Opt.VL_Stop=TRUE
+   202  Opt.Clear_P_Reset=TRUE
+   203  Opt.Clear_P_SAW=FALSE
+   204  Opt.Log_To_DB=TRUE
+   208  do501PartClampClose=FALSE
+   209  do502PartClampOpen=TRUE
+   210  nWaitMs=0
```
_210 more lines: see diffs/KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src.diff_

### `KRC/R1/Program/Centerline/PRELOAD.dat`

changed, integrator program: 1 code line(s) removed, 7 added; 11 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/PRELOAD.dat.diff](diffs/KRC/R1/Program/Centerline/PRELOAD.dat.diff)

Attributes: &ACCESS RVP1 -> &ACCESS RVO5

Data changes:

- added 2 BOOL: bPinDownSensor, QFP_NUT_LOADED
- added 1 DEFDAT: preload
- added 4 INT: nFeedSettleMs, nPinDownMaxMs, nPinDownMs, nPinUpMs
- removed 1 DEFDAT: PRELOAD

```diff
@@ base line 2, backup line 2 @@
-     2  DEFDAT PRELOAD
+     2  DEFDAT preload PUBLIC
      5  EXT BAS (BAS_COMMAND :IN,REAL :IN )
+    15  DECL GLOBAL BOOL QFP_NUT_LOADED=TRUE
+    20  DECL GLOBAL INT nPinDownMs=200
+    21  DECL GLOBAL INT nPinDownMaxMs=1000
+    22  DECL GLOBAL BOOL bPinDownSensor=FALSE
+    25  DECL GLOBAL INT nPinUpMs=300
+    28  DECL GLOBAL INT nFeedSettleMs=3000
     29  ENDDAT
```

### `KRC/R1/Program/Centerline/PRELOAD.src`

changed, integrator program: 41 code line(s) removed, 80 added; 293 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/PRELOAD.src.diff](diffs/KRC/R1/Program/Centerline/PRELOAD.src.diff)

Attributes: +&COMMENT 03-10-R1 PNW1 NUT PRELOAD

```diff
@@ base line 2, backup line 3 @@
      3  DEF PRELOAD ( )
-     5  IF NUT_STAR AND NOT NUTCYCLE_ACTIVE THEN
-     7  NUT_STAR=FALSE
+    44  IF NUT_START AND NOT NUTCYCLE_ACTIVE THEN
+    46  NUT_START=FALSE
     47  NUTCYCLE_ACTIVE=TRUE
     48  NUT_READY=FALSE
@@ base line 12, backup line 51 @@
     51  STEP10DONE=FALSE
     52  STEP20DONE=FALSE
+    53  STEP10_ADV_STARTED=FALSE
     54  NUT_PRELOAD_FAULT=FALSE
     55  $TIMER_STOP[10]=TRUE
@@ base line 28, backup line 69 @@
     69  SWITCH NUT_PRELOAD_STEP
     71  CASE 0
-    33  $OUT[503]=FALSE
-    34  $OUT[504]=TRUE
-    37  IF ($IN[482]==TRUE) AND ($IN[470]==FALSE) THEN
-    39  $OUT[476]=TRUE
-    40  $OUT[494]=FALSE
+    75  do503QFPAdvance=FALSE
+    76  do504QFPReturn=TRUE
+    79  IF QFP_NUT_LOADED AND (dipw1_SpearHome==TRUE) AND (di470QFPAdvanced==FALSE) THEN
+    80  STEP0DONE=TRUE
+    81  ENDIF
+    85  IF (dipw1_SpearHome==TRUE) AND (di470QFPAdvanced==FALSE) AND (NOT QFP_NUT_LOADED) THEN
+    88  dopw1_StartFeed=TRUE
+    89  dopw1_BlowOff=FALSE
     92  IF $TIMER_STOP[10] THEN
     93  $TIMER[10]=0
     94  $TIMER_STOP[10]=FALSE
     95  ENDIF
-    47  IF $TIMER[10]>=2000 THEN
+    99  IF $TIMER[10]>=(2000+nFeedSettleMs) THEN
    100  $TIMER_STOP[10]=TRUE
    102  STEP0DONE=TRUE
@@ base line 59, backup line 111 @@
    111  CASE 10
    114  IF STEP0DONE THEN
-    65  $OUT[472]=FALSE
-    66  $OUT[471]=TRUE
-    68  $OUT[498]=FALSE
-    69  $OUT[499]=TRUE
-    71  $OUT[501]=FALSE
-    72  $OUT[502]=TRUE
+   118  dopw1_GunWork=FALSE
+   119  dopw1_GunHome=TRUE
+   122  do498UpperPinExtend=FALSE
+   123  do499UpperPinRetract=TRUE
+   126  do501PartClampClose=FALSE
+   127  do502PartClampOpen=TRUE
    130  IF NOT STEP10_ADV_STARTED THEN
-    75  $OUT[494]=TRUE
-    77  $OUT[503]=FALSE
-    78  $OUT[504]=TRUE
-    80  IF ($IN[482]==TRUE) AND ($IN[470]==FALSE) THEN
+   132  dopw1_BlowOff=TRUE
+   135  dopw1_AdvancePin=FALSE
```
_115 more lines: see diffs/KRC/R1/Program/Centerline/PRELOAD.src.diff_

### `KRC/R1/Program/Centerline/Request_next_nut.src`

changed, integrator program: 2 code line(s) removed, 2 added; 19 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/Request_next_nut.src.diff](diffs/KRC/R1/Program/Centerline/Request_next_nut.src.diff)

Attributes: +&COMMENT 03-10-R1 PNW1 NEXT NUT REQUEST

```diff
@@ base line 2, backup line 3 @@
      3  DEF Request_next_nut ( )
-     4  NEXT_NUT_READY=false
+    20  NEXT_NUT_READY=FALSE
     21  NEXT_NUT_REQUEST=TRUE
-     6  NUT_STAR=TRUE
+    22  NUT_START=TRUE
     24  END
```

### `KRC/R1/Program/Centerline/centerline_weld.src`

changed, integrator program: 73 code line(s) removed, 90 added; 260 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/centerline_weld.src.diff](diffs/KRC/R1/Program/Centerline/centerline_weld.src.diff)

Attributes: &ACCESS RVP3 -> &ACCESS RVO1; +&COMMENT 03-10-R1 PNW1 NUT WELD

```diff
@@ base line 4, backup line 5 @@
      5  DEF CENTERLINE_WELD()
-    51  $OUT[472]=FALSE
-    52  $OUT[471]=TRUE
-    55  $OUT[498]=FALSE
-    56  $OUT[499]=TRUE
-    59  $OUT[501]=FALSE
-    60  $OUT[502]=TRUE
-    61  WAIT FOR $IN[466]
-    64  $OUT[496]=FALSE
-    65  $OUT[495]=TRUE
-    68  $OUT[503]=FALSE
-    69  $OUT[504]=TRUE
-    70  WAIT FOR $IN[482]
+    64  CT_WELD_START()
+    67  NUT_WELD_RETRY=FALSE
+    72  dopw1_GunWork=FALSE
+    73  dopw1_GunHome=TRUE
+    77  do498UpperPinExtend=FALSE
+    78  do499UpperPinRetract=TRUE
+    81  do501PartClampClose=FALSE
+    82  do502PartClampOpen=TRUE
+    84  WAIT FOR di466PartClampOpen
+    88  IF NUT_READY THEN
+    90  dopw1_BlowOff=FALSE
+    91  dopw1_ReturnPin=FALSE
+    92  dopw1_AdvancePin=TRUE
+    93  ELSE
+    95  dopw1_AdvancePin=FALSE
+    96  dopw1_ReturnPin=TRUE
+    97  dopw1_BlowOff=TRUE
+    98  ENDIF
+   101  do503QFPAdvance=FALSE
+   102  do504QFPReturn=TRUE
+   104  WAIT FOR dipw1_SpearHome
    108  IF NOT NUT_READY THEN
-    75  $OUT[496]=FALSE
-    76  $OUT[495]=TRUE
-    77  $OUT[494]=TRUE
-    80  $OUT[504]=FALSE
-    81  $OUT[503]=TRUE
-    82  WAIT FOR $IN[470]
+   111  WAIT SEC 1.0
+   112  do504QFPReturn=FALSE
+   113  do503QFPAdvance=TRUE
+   115  WAIT FOR di470QFPAdvanced
+   117  QFP_NUT_LOADED=FALSE
+   122  dopw1_Nut1Intensify_Home=FALSE
+   123  dopw1_BlowOff=FALSE
+   124  dopw1_ReturnPin=FALSE
+   125  dopw1_AdvancePin=TRUE
    130  dopw1_StartFeed=TRUE
    131  dopw1_StartFeed=FALSE
    132  WAIT SEC 1.5
-    89  $OUT[494]=FALSE
-    92  $OUT[503]=FALSE
-    93  $OUT[504]=TRUE
-    94  WAIT FOR $IN[482]
-    97  $OUT[499]=FALSE
-    98  $OUT[498]=TRUE
```
_159 more lines: see diffs/KRC/R1/Program/Centerline/centerline_weld.src.diff_

### `KRC/R1/Program/Centerline/gun_open_check.dat`

changed, integrator program: 4 code line(s) removed, 26 added; 48 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/gun_open_check.dat.diff](diffs/KRC/R1/Program/Centerline/gun_open_check.dat.diff)

Attributes: -&ACCESS  RV; -&COMMENT NUT WELDER GUN OPEN CHECK; +&ACCESS RVO5; +&REL 25; +&COMMENT 03-10-R1 PNW1 GUN OPEN CHECK; &REL 2 -> &PARAM DISKPATH = KRC:\R1\Program\Centerline

Data changes:

- bGunAirCheck (BOOL): FALSE -> TRUE
- added 5 BOOL: bPinCheck, bPinWeldCheck, CL_ClampOpen, CL_PinRetracted, NUT_WELD_RETRY
- added 1 DEFDAT: gun_open_check
- added 17 INT: nCtCycle, nCtInWelder, nCtNut, nCtNutToNut, nCtNutWait, nCtPart, nCtWaitSum, nNutRetryCnt, nNutRetryLast, nNutRetryMax, nNutRetryTotal, nPedestalWaitMs ...
- removed 1 DEFDAT: GUN_OPEN_CHECK

Runtime values (left out of the code diff): nCtInWelder[1]: - -> 4032; nCtInWelder[2]: - -> 3924; nCtInWelder[3]: - -> 3912; nCtNutToNut[1]: - -> 263832; nCtNutToNut[2]: - -> 6708; nCtNutToNut[3]: - -> 6612; ... and 4 more

```diff
@@ base line 6, backup line 7 @@
-     6  DEFDAT GUN_OPEN_CHECK PUBLIC
+     7  DEFDAT gun_open_check PUBLIC
     13  DECL GLOBAL INT nGunOpenMin=137000
     14  DECL GLOBAL INT nGunOpenMax=142000
-    18  DECL INT nGunOpenWaitMs=2000
-    24  DECL BOOL bGunAirCheck=FALSE
+    16  DECL GLOBAL INT nGunOpenWaitMs=2000
+    19  DECL GLOBAL BOOL bGunAirCheck=TRUE
     24  DECL GLOBAL INT nWaterFlowMin=150
     25  DECL GLOBAL INT nWaterFlowHyst=10
-    35  DECL BOOL bGunWaterCheck=TRUE
+    27  DECL GLOBAL BOOL bGunWaterCheck=TRUE
+    31  DECL GLOBAL INT nPedestalWaitMs=3000
+    35  DECL GLOBAL BOOL bPinCheck=TRUE
+    36  DECL GLOBAL INT nPinRetractMin=26000
+    37  DECL GLOBAL INT nPinRetractMax=28000
+    40  DECL GLOBAL BOOL bPinWeldCheck=TRUE
+    44  DECL GLOBAL INT nPinStableMs=60
+    45  DECL GLOBAL INT nPinStableCnt=30
+    46  DECL GLOBAL INT nPinSettleMaxMs=1000
+    50  DECL GLOBAL BOOL NUT_WELD_RETRY=FALSE
+    51  DECL GLOBAL INT nNutRetryMax=1
+    52  DECL GLOBAL INT nNutRetryCnt=0
+    53  DECL GLOBAL INT nNutRetryTotal=8
+    54  DECL GLOBAL INT nNutRetryLast=3
+    66  DECL GLOBAL INT nCtNut=3
+    67  DECL GLOBAL INT nCtNutToNut[3]
+    71  DECL GLOBAL INT nCtNutWait[3]
+    75  DECL GLOBAL INT nCtInWelder[3]
+    79  DECL GLOBAL INT nCtPart=17232
+    80  DECL GLOBAL INT nCtWaitSum=564
+    81  DECL GLOBAL INT nCtCycle=276828
+    83  DECL GLOBAL BOOL CL_ClampOpen=FALSE
+    84  DECL GLOBAL BOOL CL_PinRetracted=TRUE
     86  ENDDAT
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt1A.dat`

changed, integrator program: 94 code line(s) removed, 5 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1A.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1A.dat.diff)

Attributes: &ACCESS RVP1 -> &ACCESS RVO1; &REL 339 -> &REL 343; &COMMENT NUT1 -> &COMMENT 03-10-R1 PNW1 NUT 1 ST2

Data changes:

- XP8 (E6POS) re-taught: moved 71.4 mm, rotated up to 0.9 deg
- XP19 (E6POS) re-taught: moved 1.9 mm
- XP20 (E6POS) re-taught: moved 0.2 mm
- added 1 DEFDAT: style1app1opt1a
- removed 1 DEFDAT: style1app1opt1A
- removed 25 E6POS: XABOVENUT1, XAboveNut2, XDROP17, XDROP18, XP1, XP2, XP3, XP4, XP5, XP6, XP7, XP08 ...
- removed 25 FDAT: FAboveNut1, FAboveNut2, FDROP17, FDROP18, FP1, FP2, FP3, FP4, FP5, FP6, FP7, FP08 ...
- removed 16 LDAT: LCPDAT0, LCPDAT1, LCPDAT2, LCPDAT3, LCPDAT4, LCPDAT5, LCPDAT6, LCPDAT7, LCPDAT9, LCPDAT10, LCPDAT11, LCPDAT13 ...
- removed 5 NUTWELDDAT: NutData1_11, NutData1_12, NutData1_13, NutWeldDAT1, NutWeldDAT3
- removed 16 PDAT: PPDAT2, PPDAT3, PPDAT4, PPDAT5, PPDAT6, PPDAT7, PPDAT8, PPDAT9, PPDAT10, PPDAT11, PPDAT12, PPDAT13 ...
- removed 1 TM_SUGG_T: LAST_TQM
- removed 1 TQM_TQDAT_T: TM1

Runtime values (left out of the code diff): LAST_BASIS: {POINT1[] "P0                      ",POI... -> {POINT1[] "P0                      ",POI...

```diff
@@ base line 7, backup line 7 @@
-     7  DEFDAT style1app1opt1A
+     7  DEFDAT style1app1opt1a
     10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
-    17  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    18  DECL E6POS XP10={X 214.483856,Y 193.590897,Z 1005.80865,A 6.59456158,B -23.4313526,C 9.77940178,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    19  DECL FDAT FP10={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    20  DECL E6POS XP20={X -3850.82104,Y -108.397034,Z -435.544800,A -178.432037,B 0.654220462,C -179.967712,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    17  DECL E6POS XP20={X -3850.82104,Y -108.397034,Z -435.788452,A -178.432037,B 0.654220343,C -179.967712,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     18  DECL FDAT FP20={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    22  DECL E6POS XP30={X 359.994781,Y 339.042908,Z -58.4685249,A 9.62195110,B 8.87501,C 1.49797690,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    23  DECL FDAT FP30={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    24  DECL E6POS XABOVENUT1={X 134.661209,Y 312.220856,Z -32.0869446,A 8.71582699,B 8.82717705,C 1.11576843,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    25  DECL FDAT FAboveNut1={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    26  DECL LDAT LCPDAT0={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    27  DECL E6POS XAboveNut2={X 38.3333626,Y 318.813446,Z -15.8014164,A 9.53667259,B 8.81424236,C 1.48279762,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    28  DECL FDAT FAboveNut2={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    29  DECL LDAT LCPDAT4={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    30  DECL E6POS XP60={X 214.522202,Y 447.905060,Z 1005.80865,A 6.59456158,B -23.4313526,C 9.77940178,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    31  DECL FDAT FP60={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    32  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    42  DECL NutWeldDAT NutWeldDAT1={GunNr 1,SpotNr 7,Offset 0}
-    43  DECL LDAT XPNW1CPDAT={VEL 0.150000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000}
     28  DECL FDAT FPNW1={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    45  DECL LDAT LCPDAT6={ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     29  DECL E6POS XPNW1={X 123.774101,Y 312.995331,Z -88.6478,A 8.71582699,B 8.82717705,C 1.11576855,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    47  DECL NutWeldDAT NutWeldDAT3={GunNr 1,SpotNr 8,Offset 0}
-    48  DECL LDAT XPNW5CPDAT={VEL 0.150000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000}
-    49  DECL FDAT FPNW5={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    50  DECL LDAT LCPDAT13={ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    51  DECL E6POS XPNW5={X 29.6411285,Y 320.239532,Z -61.6583595,A 9.53667259,B 8.81424236,C 1.48279774,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    52  DECL PDAT PPDAT6={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    53  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    54  DECL PDAT PPDAT8={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     30  DECL NutWeld_SUGG_T LAST_NutWeld={POINT1[] "PNW1_SPOT7              ",POINT2[] "PNW0                    ",CP_PARAMS[] "CPDATNutWeld0           ",PTP_PARAMS[] "PDATNutWeld0            ",CONT[] "C_PTP                   ",CP_VEL[] "2  [...]
-    57  DECL E6POS XDROP17={X 254.475,Y 260.666412,Z -295.081390,A -1.28851116,B 6.20056677,C -103.654922,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    58  DECL FDAT FDROP17={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    59  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    60  DECL E6POS XDROP18={X 640.467163,Y -739.926514,Z 98.7580948,A -2.83424330,B 2.72720981,C 59.2469177,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    61  DECL FDAT FDROP18={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    62  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    63  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    64  DECL LDAT LCPDAT2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     32  DECL PDAT PPDAT0={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     33  DECL E6POS XP0={X -3704.29346,Y 1.10223198,Z -449.805786,A -178.368118,B 0.266879767,C 179.968445,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     34  DECL FDAT FP0={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    68  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    69  DECL E6POS XP1={X -1824.18188,Y -1001.09119,Z -157.213959,A -87.6076279,B -4.42733240,C -177.429916,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    70  DECL FDAT FP1={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    71  DECL PDAT PPDAT9={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    72  DECL E6POS XP2={X 502.171722,Y 190.181396,Z -135.596970,A -6.24112272,B -3.20316982,C 176.013672,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    73  DECL FDAT FP2={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    74  DECL PDAT PPDAT10={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    75  DECL E6POS XP3={X 403.314392,Y 226.179260,Z -114.475060,A -6.33512926,B 0.0627186,C 178.051514,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    76  DECL FDAT FP3={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    77  DECL PDAT PPDAT11={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    78  DECL E6POS XP4={X -99.9718552,Y -496.474915,Z -138.682404,A -31.5940628,B -0.774911,C 178.211197,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    79  DECL FDAT FP4={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    80  DECL PDAT PPDAT12={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    81  DECL E6POS XP5={X -3674.25464,Y -4.99133062,Z -444.893219,A -178.368118,B 0.266879946,C 179.968445,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
```
_58 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1A.dat.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt1A.src`

changed, integrator program: 17 code line(s) removed, 23 added; 113 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1A.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1A.src.diff)

Attributes: &ACCESS RVP1 -> &ACCESS RVO1; &REL 339 -> &REL 343; &COMMENT NUT1 -> &COMMENT 03-10-R1 PNW1 NUT 1 ST2

```diff
@@ base line 64, backup line 56 @@
     56  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
     57  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
-    68  LOOP
-    69  WAIT FOR NUT_READY== TRUE
-    71  GUN_OPEN_CHECK()
+    60  INTERRUPT DECL 23 WHEN CL_ClampOpen==FALSE DO GUN_OPEN_LOST()
+    61  INTERRUPT DECL 24 WHEN CL_PinRetracted==FALSE DO GUN_OPEN_LOST()
+    66  CT_NUT_WAIT(1)
     69  INTERRUPT ON 20
     70  INTERRUPT ON 21
     71  INTERRUPT ON 22
+    72  INTERRUPT ON 23
+    73  INTERRUPT ON 24
+    75  PEDESTAL_CLEAR_CHECK()
     79  $BWDSTART=FALSE
     80  LDAT_ACT=LCPDAT8
@@ base line 79, backup line 82 @@
     82  BAS(#CP_PARAMS,2)
     83  LIN XP20 C_DIS C_DIS
-    83  IF di004UseDryCycle==FALSE THEN
+    89  IF NOT di004UseDryCycle THEN
     91  $BWDSTART=FALSE
     92  LDAT_ACT=LCPDAT18
@@ base line 95, backup line 101 @@
    101  INTERRUPT OFF 21
    102  INTERRUPT OFF 22
+   103  INTERRUPT OFF 23
+   104  INTERRUPT OFF 24
    106  CENTERLINE_WELD()
+   110  WHILE NUT_WELD_RETRY
+   111  NUT_WELD_RETRY=FALSE
+   112  Request_next_nut()
+   113  WAIT FOR NUT_READY==TRUE
+   114  CENTERLINE_WELD()
+   115  ENDWHILE
+   119  Request_next_nut()
    122  INTERRUPT ON 20
    123  INTERRUPT ON 21
    124  INTERRUPT ON 22
+   125  INTERRUPT ON 23
+   126  INTERRUPT ON 24
+   128  PEDESTAL_CLEAR_CHECK()
    129  ENDIF
    133  $BWDSTART=FALSE
@@ base line 115, backup line 143 @@
    143  INTERRUPT OFF 21
    144  INTERRUPT OFF 22
-   118  IF NOT NUT_WELD_RETRY THEN
-   119  EXIT
-   120  ENDIF
-   121  NUT_WELD_RETRY=FALSE
-   122  ENDLOOP
+   145  INTERRUPT OFF 23
+   146  INTERRUPT OFF 24
    149  $BWDSTART=FALSE
-   127  LDAT_ACT=LCPDAT17
+   150  PDAT_ACT=PPDAT1
    151  FDAT_ACT=FP8
-   129  BAS(#CP_PARAMS,2)
```
_9 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1A.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt1B.dat`

changed, integrator program: 93 code line(s) removed, 4 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1B.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1B.dat.diff)

Attributes: &ACCESS RVO2 -> &ACCESS RVO1; &REL 1 -> &REL 343; &COMMENT NUT1 -> &COMMENT 03-10-R1 PNW1 NUT 1 ST2

Data changes:

- XP8 (E6POS) re-taught: moved 71.4 mm, rotated up to 0.9 deg
- XP20 (E6POS) re-taught: moved 5.5 mm
- added 1 DEFDAT: style1app1opt1b
- removed 1 DEFDAT: style1app1opt1B
- removed 25 E6POS: XABOVENUT1, XAboveNut2, XDROP17, XDROP18, XP1, XP2, XP3, XP4, XP5, XP6, XP7, XP08 ...
- removed 25 FDAT: FAboveNut1, FAboveNut2, FDROP17, FDROP18, FP1, FP2, FP3, FP4, FP5, FP6, FP7, FP08 ...
- removed 16 LDAT: LCPDAT0, LCPDAT1, LCPDAT2, LCPDAT3, LCPDAT4, LCPDAT5, LCPDAT6, LCPDAT7, LCPDAT9, LCPDAT10, LCPDAT11, LCPDAT13 ...
- removed 5 NUTWELDDAT: NutData1_11, NutData1_12, NutData1_13, NutWeldDAT1, NutWeldDAT3
- removed 16 PDAT: PPDAT2, PPDAT3, PPDAT4, PPDAT5, PPDAT6, PPDAT7, PPDAT8, PPDAT9, PPDAT10, PPDAT11, PPDAT12, PPDAT13 ...
- removed 1 TM_SUGG_T: LAST_TQM
- removed 1 TQM_TQDAT_T: TM1

Runtime values (left out of the code diff): LAST_BASIS: {POINT1[] "P0                      ",POI... -> {POINT1[] "P0                      ",POI...

```diff
@@ base line 7, backup line 7 @@
-     7  DEFDAT style1app1opt1B
+     7  DEFDAT style1app1opt1b
     10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
-    17  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    18  DECL E6POS XP10={X 214.483856,Y 193.590897,Z 1005.80865,A 6.59456158,B -23.4313526,C 9.77940178,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    19  DECL FDAT FP10={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    20  DECL E6POS XP20={X -3850.82104,Y -108.397034,Z -430.314789,A -178.432037,B 0.654220343,C -179.967712,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    17  DECL E6POS XP20={X -3850.82104,Y -108.397034,Z -435.788452,A -178.432037,B 0.654220343,C -179.967712,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     18  DECL FDAT FP20={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    22  DECL E6POS XP30={X 359.994781,Y 339.042908,Z -58.4685249,A 9.62195110,B 8.87501,C 1.49797690,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    23  DECL FDAT FP30={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    24  DECL E6POS XABOVENUT1={X 134.661209,Y 312.220856,Z -32.0869446,A 8.71582699,B 8.82717705,C 1.11576843,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    25  DECL FDAT FAboveNut1={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    26  DECL LDAT LCPDAT0={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    27  DECL E6POS XAboveNut2={X 38.3333626,Y 318.813446,Z -15.8014164,A 9.53667259,B 8.81424236,C 1.48279762,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    28  DECL FDAT FAboveNut2={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    29  DECL LDAT LCPDAT4={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    30  DECL E6POS XP60={X 214.522202,Y 447.905060,Z 1005.80865,A 6.59456158,B -23.4313526,C 9.77940178,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    31  DECL FDAT FP60={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    32  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    42  DECL NutWeldDAT NutWeldDAT1={GunNr 1,SpotNr 7,Offset 0}
-    43  DECL LDAT XPNW1CPDAT={VEL 0.150000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000}
     28  DECL FDAT FPNW1={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    45  DECL LDAT LCPDAT6={ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     29  DECL E6POS XPNW1={X 123.774101,Y 312.995331,Z -88.6478,A 8.71582699,B 8.82717705,C 1.11576855,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    47  DECL NutWeldDAT NutWeldDAT3={GunNr 1,SpotNr 8,Offset 0}
-    48  DECL LDAT XPNW5CPDAT={VEL 0.150000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000}
-    49  DECL FDAT FPNW5={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    50  DECL LDAT LCPDAT13={ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    51  DECL E6POS XPNW5={X 29.6411285,Y 320.239532,Z -61.6583595,A 9.53667259,B 8.81424236,C 1.48279774,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    52  DECL PDAT PPDAT6={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    53  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    54  DECL PDAT PPDAT8={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     30  DECL NutWeld_SUGG_T LAST_NutWeld={POINT1[] "PNW1_SPOT7              ",POINT2[] "PNW0                    ",CP_PARAMS[] "CPDATNutWeld0           ",PTP_PARAMS[] "PDATNutWeld0            ",CONT[] "C_PTP                   ",CP_VEL[] "2  [...]
-    57  DECL E6POS XDROP17={X 254.475,Y 260.666412,Z -295.081390,A -1.28851116,B 6.20056677,C -103.654922,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    58  DECL FDAT FDROP17={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    59  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    60  DECL E6POS XDROP18={X 640.467163,Y -739.926514,Z 98.7580948,A -2.83424330,B 2.72720981,C 59.2469177,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    61  DECL FDAT FDROP18={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    62  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    63  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    64  DECL LDAT LCPDAT2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     32  DECL PDAT PPDAT0={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     33  DECL E6POS XP0={X -3704.29346,Y 1.10223198,Z -449.805786,A -178.368118,B 0.266879767,C 179.968445,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     34  DECL FDAT FP0={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    68  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    69  DECL E6POS XP1={X -1824.18188,Y -1001.09119,Z -157.213959,A -87.6076279,B -4.42733240,C -177.429916,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    70  DECL FDAT FP1={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    71  DECL PDAT PPDAT9={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    72  DECL E6POS XP2={X 502.171722,Y 190.181396,Z -135.596970,A -6.24112272,B -3.20316982,C 176.013672,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    73  DECL FDAT FP2={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    74  DECL PDAT PPDAT10={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    75  DECL E6POS XP3={X 403.314392,Y 226.179260,Z -114.475060,A -6.33512926,B 0.0627186,C 178.051514,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    76  DECL FDAT FP3={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    77  DECL PDAT PPDAT11={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    78  DECL E6POS XP4={X -99.9718552,Y -496.474915,Z -138.682404,A -31.5940628,B -0.774911,C 178.211197,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    79  DECL FDAT FP4={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    80  DECL PDAT PPDAT12={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    81  DECL E6POS XP5={X -3674.25464,Y -4.99133062,Z -444.893219,A -178.368118,B 0.266879946,C 179.968445,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
```
_57 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1B.dat.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt1B.src`

changed, integrator program: 17 code line(s) removed, 23 added; 113 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1B.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1B.src.diff)

Attributes: &ACCESS RVO2 -> &ACCESS RVO1; &REL 1 -> &REL 343; &COMMENT NUT1 -> &COMMENT 03-10-R1 PNW1 NUT 1 ST2

```diff
@@ base line 64, backup line 56 @@
     56  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
     57  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
-    68  LOOP
-    69  WAIT FOR NUT_READY== TRUE
-    71  GUN_OPEN_CHECK()
+    60  INTERRUPT DECL 23 WHEN CL_ClampOpen==FALSE DO GUN_OPEN_LOST()
+    61  INTERRUPT DECL 24 WHEN CL_PinRetracted==FALSE DO GUN_OPEN_LOST()
+    66  CT_NUT_WAIT(1)
     69  INTERRUPT ON 20
     70  INTERRUPT ON 21
     71  INTERRUPT ON 22
+    72  INTERRUPT ON 23
+    73  INTERRUPT ON 24
+    75  PEDESTAL_CLEAR_CHECK()
     79  $BWDSTART=FALSE
     80  LDAT_ACT=LCPDAT8
@@ base line 79, backup line 82 @@
     82  BAS(#CP_PARAMS,2)
     83  LIN XP20 C_DIS C_DIS
-    83  IF di004UseDryCycle==FALSE THEN
+    89  IF NOT di004UseDryCycle THEN
     91  $BWDSTART=FALSE
     92  LDAT_ACT=LCPDAT18
@@ base line 95, backup line 101 @@
    101  INTERRUPT OFF 21
    102  INTERRUPT OFF 22
+   103  INTERRUPT OFF 23
+   104  INTERRUPT OFF 24
    106  CENTERLINE_WELD()
+   110  WHILE NUT_WELD_RETRY
+   111  NUT_WELD_RETRY=FALSE
+   112  Request_next_nut()
+   113  WAIT FOR NUT_READY==TRUE
+   114  CENTERLINE_WELD()
+   115  ENDWHILE
+   119  Request_next_nut()
    122  INTERRUPT ON 20
    123  INTERRUPT ON 21
    124  INTERRUPT ON 22
+   125  INTERRUPT ON 23
+   126  INTERRUPT ON 24
+   128  PEDESTAL_CLEAR_CHECK()
    129  ENDIF
    133  $BWDSTART=FALSE
@@ base line 115, backup line 143 @@
    143  INTERRUPT OFF 21
    144  INTERRUPT OFF 22
-   118  IF NOT NUT_WELD_RETRY THEN
-   119  EXIT
-   120  ENDIF
-   121  NUT_WELD_RETRY=FALSE
-   122  ENDLOOP
+   145  INTERRUPT OFF 23
+   146  INTERRUPT OFF 24
    149  $BWDSTART=FALSE
-   127  LDAT_ACT=LCPDAT17
+   150  PDAT_ACT=PPDAT1
    151  FDAT_ACT=FP8
-   129  BAS(#CP_PARAMS,2)
```
_9 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1B.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt2A.dat`

changed, integrator program: 129 code line(s) removed, 6 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2A.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2A.dat.diff)

Attributes: -&ACCESS  RV; -&COMMENT GE4_002_GUN1; +&ACCESS RVO1; +&REL 252; +&COMMENT 03-10-R1 PNW1 NUT 2 ST2; -&REL 246

Data changes:

- XP0 (E6POS) re-taught: moved 126.7 mm, rotated up to 1.7 deg
- XP05 (E6POS) re-taught: moved 60.9 mm, rotated up to 1.7 deg
- XP06 (E6POS) re-taught: moved 3.3 mm
- XP6 (E6POS) re-taught: moved 3.3 mm
- XP16 (E6POS) re-taught: moved 2.0 mm
- removed 35 E6POS: XAboveNut3, XAboveNut4, XAboveNut6, XDROP21, XDROP22, XDROP23, XDROP24, XDROP25, XDROP26, XDROP31, XDROP32, XP1 ...
- removed 35 FDAT: FAboveNut3, FAboveNut4, FAboveNut6, FDROP21, FDROP22, FDROP23, FDROP24, FDROP25, FDROP26, FDROP31, FDROP32, FP1 ...
- removed 23 LDAT: LCPDAT1, LCPDAT2, LCPDAT3, LCPDAT4, LCPDAT5, LCPDAT7, LCPDAT8, LCPDAT9, LCPDAT10, LCPDAT12, LCPDAT13, LCPDAT16 ...
- removed 3 NUTWELDDAT: NutWeldDAT4, NutWeldDAT6, NutWeldDAT8
- removed 27 PDAT: PPDAT2, PPDAT3, PPDAT4, PPDAT5, PPDAT6, PPDAT7, PPDAT8, PPDAT9, PPDAT10, PPDAT11, PPDAT12, PPDAT13 ...

Runtime values (left out of the code diff): LAST_BASIS: {POINT1[] "P0                      ",POI... -> {POINT1[] "P0                      ",POI...

```diff
@@ base line 7, backup line 7 @@
      7  DEFDAT style1app1opt2A
     10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
-    17  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    18  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    19  DECL LDAT LCPDAT4={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    20  DECL E6POS XP10={X -1783.28369,Y -204.411,Z 1353.11560,A 22.6009655,B -85.8094482,C -23.7340908,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    21  DECL FDAT FP10={TOOL_NO 3,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    22  DECL E6POS XAboveNut3={X -303.780243,Y 813.191772,Z 166.218750,A 57.0816841,B -0.384623110,C -0.00601434475,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    23  DECL FDAT FAboveNut3={TOOL_NO 3,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    24  DECL E6POS XAboveNut4={X -347.034637,Y 785.924500,Z 174.869568,A 56.8305,B -0.0316173770,C 0.561762750,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    25  DECL FDAT FAboveNut4={TOOL_NO 3,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    26  DECL E6POS XP70={X -29.1782665,Y 976.513794,Z 395.040894,A 39.0784416,B -7.62199688,C -6.57393408,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    27  DECL FDAT FP70={TOOL_NO 3,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    28  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    29  DECL E6POS XP80={X 290.249634,Y 607.626892,Z -209.393982,A -8.90244770,B 0.239384755,C 178.080566,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    30  DECL FDAT FP80={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    31  DECL LDAT LCPDAT7={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    32  DECL LDAT LCPDAT8={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    33  DECL E6POS XAboveNut6={X -336.120819,Y 902.973755,Z 176.529984,A 58.7987671,B -0.490157604,C -0.146124393,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    34  DECL FDAT FAboveNut6={TOOL_NO 3,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    35  DECL E6POS XP100={X -194.562393,Y 1020.65479,Z 164.107071,A 56.8293304,B 0.00100069749,C 3.79618939E-07,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    36  DECL FDAT FP100={TOOL_NO 3,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    37  DECL LDAT LCPDAT9={VEL 2.00000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    38  DECL E6POS XP110={X -204.560745,Y 1246.33264,Z 194.087265,A 49.2418823,B 0.000983044622,C -0.000102232269,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    39  DECL FDAT FP110={TOOL_NO 3,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    40  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    41  DECL E6POS XP160={X 49.7469,Y 920.334961,Z 194.458664,A 58.6510048,B 0.000999865937,C -1.87045970E-07,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    42  DECL FDAT FP160={TOOL_NO 4,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    43  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    44  DECL E6POS XP170={X -91.4441605,Y 931.337219,Z 170.413101,A 58.6510048,B 0.000999745447,C -2.17383686E-07,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    45  DECL FDAT FP170={TOOL_NO 4,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    46  DECL LDAT LCPDAT13={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    47  DECL E6POS XP180={X -91.4441605,Y 931.337219,Z 170.413101,A 58.6510048,B 0.000999745447,C -2.17383686E-07,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    48  DECL FDAT FP180={TOOL_NO 4,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    50  DECL LDAT XPNW3CPDAT={VEL 0.150000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000}
-    51  DECL FDAT FPNW3={TOOL_NO 4,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    52  DECL E6POS XPNW3={X -153.696930,Y 813.359619,Z 144.277161,A 57.0816841,B -0.384623110,C -0.00601430889,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    53  DECL NutWeldDAT NutWeldDAT4={GunNr 2,SpotNr 3,Offset 0}
-    54  DECL LDAT LCPDAT16={ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    55  DECL LDAT XPNW4CPDAT={VEL 0.150000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000}
-    56  DECL FDAT FPNW4={TOOL_NO 4,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    57  DECL E6POS XPNW4={X -198.215103,Y 787.285461,Z 148.794556,A 56.8301735,B -0.0342749394,C 0.560239315,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    58  DECL NutWeldDAT NutWeldDAT6={GunNr 2,SpotNr 4,Offset 0}
-    59  DECL LDAT LCPDAT17={ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    60  DECL NutWeldDAT NutWeldDAT8={GunNr 3,SpotNr 2,Offset 0}
-    61  DECL LDAT XPNW6CPDAT={VEL 0.150000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000}
-    62  DECL FDAT FPNW6={TOOL_NO 3,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    63  DECL LDAT LCPDAT19={ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    64  DECL E6POS XPNW6={X -338.196289,Y 904.619080,Z 152.926773,A 58.7987671,B -0.490157604,C -0.146124482,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    65  DECL LDAT LCPDAT20={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    66  DECL PDAT PPDAT13={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    67  DECL PDAT PPDAT14={VEL 100.000,ACC 100.000,APO_DIST 5.00000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    68  DECL PDAT PPDAT15={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     18  DECL NutWeld_SUGG_T LAST_NutWeld={POINT1[] "PNW2_SPOT3              ",POINT2[] "PNW0                    ",CP_PARAMS[] "CPDATNutWeld0           ",PTP_PARAMS[] "PDATNutWeld0            ",CONT[] "C_PTP                   ",CP_VEL[] "2  [...]
-    71  DECL LDAT LReload_XPNW1_1_1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    72  DECL LDAT LReload_XPNW1_1_2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    73  DECL PDAT PReload_XPNW1_1_3={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
     20  DECL LDAT Lpnw1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     21  DECL E6POS XPnw1={X -681.099854,Y -933.961731,Z 7.00223589,A -84.9330902,B -1.72864902,C -2.54664612,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
```
_97 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2A.dat.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt2A.src`

changed, integrator program: 22 code line(s) removed, 23 added; 109 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2A.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2A.src.diff)

Attributes: &REL 246 -> &REL 252; &COMMENT GE4_002_GUN1 -> &COMMENT 03-10-R1 PNW1 NUT 2 ST2

```diff
@@ base line 42, backup line 39 @@
     39  BAS(#PTP_PARAMS,100)
     40  PTP XP0 C_DIS
-    46  $BWDSTART=FALSE
-    47  LDAT_ACT=LCPDAT11
-    48  FDAT_ACT=FP5
-    49  BAS(#CP_PARAMS,2)
-    50  LIN XP5
     47  INTERRUPT DECL 20 WHEN CL_GunStrokePositionLPT<137000 DO GUN_OPEN_LOST()
     48  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
     49  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
-    67  LOOP
-    68  WAIT FOR NEXT_NUT_READY==TRUE
-    69  GUN_OPEN_CHECK()
+    52  INTERRUPT DECL 23 WHEN CL_ClampOpen==FALSE DO GUN_OPEN_LOST()
+    53  INTERRUPT DECL 24 WHEN CL_PinRetracted==FALSE DO GUN_OPEN_LOST()
+    56  CT_NUT_WAIT(2)
     59  INTERRUPT ON 20
     60  INTERRUPT ON 21
     61  INTERRUPT ON 22
+    62  INTERRUPT ON 23
+    63  INTERRUPT ON 24
+    65  PEDESTAL_CLEAR_CHECK()
     68  $BWDSTART=FALSE
     69  LDAT_ACT=LCPDAT0
@@ base line 77, backup line 71 @@
     71  BAS(#CP_PARAMS,2)
     72  LIN XP6
-    81  IF di004UseDryCycle==FALSE THEN
+    78  IF NOT di004UseDryCycle THEN
     80  $BWDSTART=FALSE
     81  LDAT_ACT=LCPDAT15
@@ base line 93, backup line 90 @@
     90  INTERRUPT OFF 21
     91  INTERRUPT OFF 22
+    92  INTERRUPT OFF 23
+    93  INTERRUPT OFF 24
     95  CENTERLINE_WELD()
+    99  WHILE NUT_WELD_RETRY
+   100  NUT_WELD_RETRY=FALSE
+   101  Request_next_nut()
+   102  WAIT FOR NUT_READY==TRUE
+   103  CENTERLINE_WELD()
+   104  ENDWHILE
+   108  Request_next_nut()
    111  INTERRUPT ON 20
    112  INTERRUPT ON 21
    113  INTERRUPT ON 22
+   114  INTERRUPT ON 23
+   115  INTERRUPT ON 24
+   117  PEDESTAL_CLEAR_CHECK()
    118  ENDIF
    121  $BWDSTART=FALSE
@@ base line 112, backup line 131 @@
    131  INTERRUPT OFF 21
    132  INTERRUPT OFF 22
-   115  IF NOT NUT_WELD_RETRY THEN
-   116  EXIT
-   117  ENDIF
-   118  NUT_WELD_RETRY=FALSE
```
_17 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2A.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt2B.dat`

changed, integrator program: 129 code line(s) removed, 6 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2B.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2B.dat.diff)

Attributes: &ACCESS RVO2 -> &ACCESS RVO1; &REL 1 -> &REL 252; &COMMENT GE4_002_GUN1 -> &COMMENT 03-10-R1 PNW1 NUT 2 ST2

Data changes:

- XP0 (E6POS) re-taught: moved 126.7 mm, rotated up to 1.7 deg
- XP05 (E6POS) re-taught: moved 60.9 mm, rotated up to 1.7 deg
- XP06 (E6POS) re-taught: moved 3.3 mm
- XP6 (E6POS) re-taught: moved 3.3 mm
- added 1 DEFDAT: style1app1opt2b
- removed 1 DEFDAT: style1app1opt2B
- removed 35 E6POS: XAboveNut3, XAboveNut4, XAboveNut6, XDROP21, XDROP22, XDROP23, XDROP24, XDROP25, XDROP26, XDROP31, XDROP32, XP1 ...
- removed 35 FDAT: FAboveNut3, FAboveNut4, FAboveNut6, FDROP21, FDROP22, FDROP23, FDROP24, FDROP25, FDROP26, FDROP31, FDROP32, FP1 ...
- removed 23 LDAT: LCPDAT1, LCPDAT2, LCPDAT3, LCPDAT4, LCPDAT5, LCPDAT7, LCPDAT8, LCPDAT9, LCPDAT10, LCPDAT12, LCPDAT13, LCPDAT16 ...
- removed 3 NUTWELDDAT: NutWeldDAT4, NutWeldDAT6, NutWeldDAT8
- removed 27 PDAT: PPDAT2, PPDAT3, PPDAT4, PPDAT5, PPDAT6, PPDAT7, PPDAT8, PPDAT9, PPDAT10, PPDAT11, PPDAT12, PPDAT13 ...

Runtime values (left out of the code diff): LAST_BASIS: {POINT1[] "P0                      ",POI... -> {POINT1[] "P0                      ",POI...

```diff
@@ base line 7, backup line 7 @@
-     7  DEFDAT style1app1opt2B
+     7  DEFDAT style1app1opt2b
     10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
-    17  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    18  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    19  DECL LDAT LCPDAT4={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    20  DECL E6POS XP10={X -1783.28369,Y -204.411,Z 1353.11560,A 22.6009655,B -85.8094482,C -23.7340908,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    21  DECL FDAT FP10={TOOL_NO 3,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    22  DECL E6POS XAboveNut3={X -303.780243,Y 813.191772,Z 166.218750,A 57.0816841,B -0.384623110,C -0.00601434475,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    23  DECL FDAT FAboveNut3={TOOL_NO 3,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    24  DECL E6POS XAboveNut4={X -347.034637,Y 785.924500,Z 174.869568,A 56.8305,B -0.0316173770,C 0.561762750,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    25  DECL FDAT FAboveNut4={TOOL_NO 3,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    26  DECL E6POS XP70={X -29.1782665,Y 976.513794,Z 395.040894,A 39.0784416,B -7.62199688,C -6.57393408,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    27  DECL FDAT FP70={TOOL_NO 3,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    28  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    29  DECL E6POS XP80={X 290.249634,Y 607.626892,Z -209.393982,A -8.90244770,B 0.239384755,C 178.080566,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    30  DECL FDAT FP80={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    31  DECL LDAT LCPDAT7={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    32  DECL LDAT LCPDAT8={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    33  DECL E6POS XAboveNut6={X -336.120819,Y 902.973755,Z 176.529984,A 58.7987671,B -0.490157604,C -0.146124393,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    34  DECL FDAT FAboveNut6={TOOL_NO 3,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    35  DECL E6POS XP100={X -194.562393,Y 1020.65479,Z 164.107071,A 56.8293304,B 0.00100069749,C 3.79618939E-07,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    36  DECL FDAT FP100={TOOL_NO 3,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    37  DECL LDAT LCPDAT9={VEL 2.00000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    38  DECL E6POS XP110={X -204.560745,Y 1246.33264,Z 194.087265,A 49.2418823,B 0.000983044622,C -0.000102232269,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    39  DECL FDAT FP110={TOOL_NO 3,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    40  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    41  DECL E6POS XP160={X 49.7469,Y 920.334961,Z 194.458664,A 58.6510048,B 0.000999865937,C -1.87045970E-07,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    42  DECL FDAT FP160={TOOL_NO 4,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    43  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    44  DECL E6POS XP170={X -91.4441605,Y 931.337219,Z 170.413101,A 58.6510048,B 0.000999745447,C -2.17383686E-07,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    45  DECL FDAT FP170={TOOL_NO 4,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    46  DECL LDAT LCPDAT13={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    47  DECL E6POS XP180={X -91.4441605,Y 931.337219,Z 170.413101,A 58.6510048,B 0.000999745447,C -2.17383686E-07,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    48  DECL FDAT FP180={TOOL_NO 4,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    50  DECL LDAT XPNW3CPDAT={VEL 0.150000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000}
-    51  DECL FDAT FPNW3={TOOL_NO 4,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    52  DECL E6POS XPNW3={X -153.696930,Y 813.359619,Z 144.277161,A 57.0816841,B -0.384623110,C -0.00601430889,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    53  DECL NutWeldDAT NutWeldDAT4={GunNr 2,SpotNr 3,Offset 0}
-    54  DECL LDAT LCPDAT16={ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    55  DECL LDAT XPNW4CPDAT={VEL 0.150000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000}
-    56  DECL FDAT FPNW4={TOOL_NO 4,BASE_NO 2,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    57  DECL E6POS XPNW4={X -198.215103,Y 787.285461,Z 148.794556,A 56.8301735,B -0.0342749394,C 0.560239315,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    58  DECL NutWeldDAT NutWeldDAT6={GunNr 2,SpotNr 4,Offset 0}
-    59  DECL LDAT LCPDAT17={ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    60  DECL NutWeldDAT NutWeldDAT8={GunNr 3,SpotNr 2,Offset 0}
-    61  DECL LDAT XPNW6CPDAT={VEL 0.150000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000}
-    62  DECL FDAT FPNW6={TOOL_NO 3,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    63  DECL LDAT LCPDAT19={ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    64  DECL E6POS XPNW6={X -338.196289,Y 904.619080,Z 152.926773,A 58.7987671,B -0.490157604,C -0.146124482,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    65  DECL LDAT LCPDAT20={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    66  DECL PDAT PPDAT13={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    67  DECL PDAT PPDAT14={VEL 100.000,ACC 100.000,APO_DIST 5.00000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    68  DECL PDAT PPDAT15={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     18  DECL NutWeld_SUGG_T LAST_NutWeld={POINT1[] "PNW2_SPOT3              ",POINT2[] "PNW0                    ",CP_PARAMS[] "CPDATNutWeld0           ",PTP_PARAMS[] "PDATNutWeld0            ",CONT[] "C_PTP                   ",CP_VEL[] "2  [...]
-    71  DECL LDAT LReload_XPNW1_1_1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    72  DECL LDAT LReload_XPNW1_1_2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    73  DECL PDAT PReload_XPNW1_1_3={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
     20  DECL LDAT Lpnw1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
```
_97 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2B.dat.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt2B.src`

changed, integrator program: 22 code line(s) removed, 23 added; 109 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2B.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2B.src.diff)

Attributes: &ACCESS RVO2 -> &ACCESS RVO1; &REL 1 -> &REL 252; &COMMENT GE4_002_GUN1 -> &COMMENT 03-10-R1 PNW1 NUT 2 ST2

```diff
@@ base line 42, backup line 39 @@
     39  BAS(#PTP_PARAMS,100)
     40  PTP XP0 C_DIS
-    46  $BWDSTART=FALSE
-    47  LDAT_ACT=LCPDAT11
-    48  FDAT_ACT=FP5
-    49  BAS(#CP_PARAMS,2)
-    50  LIN XP5
     47  INTERRUPT DECL 20 WHEN CL_GunStrokePositionLPT<137000 DO GUN_OPEN_LOST()
     48  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
     49  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
-    67  LOOP
-    68  WAIT FOR NEXT_NUT_READY==TRUE
-    69  GUN_OPEN_CHECK()
+    52  INTERRUPT DECL 23 WHEN CL_ClampOpen==FALSE DO GUN_OPEN_LOST()
+    53  INTERRUPT DECL 24 WHEN CL_PinRetracted==FALSE DO GUN_OPEN_LOST()
+    56  CT_NUT_WAIT(2)
     59  INTERRUPT ON 20
     60  INTERRUPT ON 21
     61  INTERRUPT ON 22
+    62  INTERRUPT ON 23
+    63  INTERRUPT ON 24
+    65  PEDESTAL_CLEAR_CHECK()
     68  $BWDSTART=FALSE
     69  LDAT_ACT=LCPDAT0
@@ base line 77, backup line 71 @@
     71  BAS(#CP_PARAMS,2)
     72  LIN XP6
-    81  IF di004UseDryCycle==FALSE THEN
+    78  IF NOT di004UseDryCycle THEN
     80  $BWDSTART=FALSE
     81  LDAT_ACT=LCPDAT15
@@ base line 93, backup line 90 @@
     90  INTERRUPT OFF 21
     91  INTERRUPT OFF 22
+    92  INTERRUPT OFF 23
+    93  INTERRUPT OFF 24
     95  CENTERLINE_WELD()
+    99  WHILE NUT_WELD_RETRY
+   100  NUT_WELD_RETRY=FALSE
+   101  Request_next_nut()
+   102  WAIT FOR NUT_READY==TRUE
+   103  CENTERLINE_WELD()
+   104  ENDWHILE
+   108  Request_next_nut()
    111  INTERRUPT ON 20
    112  INTERRUPT ON 21
    113  INTERRUPT ON 22
+   114  INTERRUPT ON 23
+   115  INTERRUPT ON 24
+   117  PEDESTAL_CLEAR_CHECK()
    118  ENDIF
    121  $BWDSTART=FALSE
@@ base line 112, backup line 131 @@
    131  INTERRUPT OFF 21
    132  INTERRUPT OFF 22
-   115  IF NOT NUT_WELD_RETRY THEN
-   116  EXIT
-   117  ENDIF
-   118  NUT_WELD_RETRY=FALSE
```
_17 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2B.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt3A.dat`

changed, integrator program: 83 code line(s) removed, 6 added; 1 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3A.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3A.dat.diff)

Attributes: -&ACCESS  RV; -&COMMENT GE4_003_GUN1; +&ACCESS RVO1; +&REL 234; +&COMMENT 03-10-R1 PNW1 NUT 3 ST2; -&REL 227

Data changes:

- XP13 (E6POS) re-taught: moved 5.2 mm
- XP16 (E6POS) re-taught: moved 1.2 mm, rotated up to 0.4 deg
- XP17 (E6POS) re-taught: moved 5.2 mm
- XP20 (E6POS) re-taught: moved 101.2 mm, rotated up to 0.9 deg, S/T 2/2 -> 2/34 (ARM CONFIGURATION CHANGED)
- PPDAT2 (PDAT): {VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.... -> {VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50....
- removed 19 E6POS: XABOVENUT1, XDROP73, XNUT1, XP1, XP2, XP3, XP4, XP5, XP6, XP8, XP9, XP10 ...
- removed 19 FDAT: FAboveNut1, FDROP73, FNut1, FP1, FP2, FP3, FP4, FP5, FP6, FP8, FP9, FP10 ...
- removed 13 LDAT: LCPDAT1, LCPDAT2, LCPDAT3, LCPDAT5, LCPDAT7, LCPDAT8, LCPDAT9, LCPDAT21, Lpnw2, Lpnw3, LReload_XPNW1_1_1, LReload_XPNW1_1_2 ...
- removed 2 NUTWELDDAT: NutWeldDAT1, NutWeldDAT2
- removed 24 PDAT: PPDAT3, PPDAT4, PPDAT5, PPDAT6, PPDAT7, PPDAT8, PPDAT9, PPDAT10, PPDAT11, PPDAT12, PPDAT13, PPDAT14 ...

Runtime values (left out of the code diff): LAST_BASIS: {POINT1[] "P18                     ",POI... -> {POINT1[] "P0                      ",POI...

```diff
@@ base line 7, backup line 7 @@
      7  DEFDAT style1app1opt3A
     10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
-    16  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    17  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    18  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    19  DECL E6POS XP10={X -2075.68359,Y 854.949158,Z 1307.29810,A 77.6920624,B -20.6746445,C -80.6289597,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    20  DECL FDAT FP10={TOOL_NO 7,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    21  DECL E6POS XNUT1={X -12.8878489,Y 123.584129,Z -36.2668114,A 60.1760483,B -3.21555185,C -5.74943399,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    22  DECL FDAT FNut1={TOOL_NO 7,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    23  DECL E6POS XP40={X 194.480,Y 444.441528,Z 109.191170,A 59.0454025,B -2.16523719,C -3.66616058,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    24  DECL FDAT FP40={TOOL_NO 7,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    25  DECL E6POS XP20={X -3678.25781,Y -44.2650108,Z -442.362579,A -178.367340,B 0.267035842,C 179.968063,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    17  DECL E6POS XP20={X -3747.39,Y 5.76903486,Z -387.973175,A -178.432297,B -0.654858828,C -179.985626,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     18  DECL FDAT FP20={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    27  DECL E6POS XABOVENUT1={X -16.2189884,Y 123.785316,Z 31.4176292,A 59.9875450,B -3.00310516,C -5.37727165,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    28  DECL FDAT FAboveNut1={TOOL_NO 7,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    29  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    31  DECL NutWeldDAT NutWeldDAT1={GunNr 3,SpotNr 3,Offset 0}
-    32  DECL LDAT XPNW1CPDAT={VEL 0.150000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000}
     20  DECL FDAT FPNW1={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    34  DECL PDAT PPDAT6={ACC 100.000,APO_DIST 100.000,APO_MODE #CPTP,GEAR_JERK 50.0000,EXAX_IGN 0}
     21  DECL E6POS XPNW1={X -684.340210,Y -936.680359,Z 6.96372366,A -85.0124512,B -3.00309157,C -5.37728167,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    36  DECL LDAT LCPDAT7={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    37  DECL LDAT LCPDAT8={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    38  DECL PDAT PPDAT10={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    39  DECL E6POS XP50={X -1950.08691,Y 799.801636,Z 1115.17920,A 76.5103378,B -21.3705120,C -77.1953812,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    40  DECL FDAT FP50={TOOL_NO 7,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    42  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     23  DECL NutWeld_SUGG_T LAST_NutWeld={POINT1[] "PNW3_SPOT03             ",POINT2[] "PNW0                    ",CP_PARAMS[] "CPDATNutWeld0           ",PTP_PARAMS[] "PDATNutWeld0            ",CONT[] "C_PTP                   ",CP_VEL[] "2  [...]
-    44  DECL NutWeldDAT NutWeldDAT2={GunNr 3,SpotNr 3,Offset 0}
-    45  DECL LDAT LCPDAT2={ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     24  DECL MODULEPARAM_T LAST_TP_PARAMS={PARAMS[] "NutWeld_CmdPos=Weld; NutWeld_Move=LIN; NutWeld_NutWeldDat=NutWeldDAT1; NutWeld_NWGunNr=3; NutWeld_NWSpotNr=3; NutWeld_NWOffset=0; Kuka.MoveDataName=CPDAT2; Kuka.VelocityPath=2; Kuka.Poin [...]
-    47  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    48  DECL LDAT LCPDAT3={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    49  DECL LDAT LCPDAT21={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    50  DECL LDAT LReload_XPNW1_1_1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    51  DECL LDAT LReload_XPNW1_1_2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    52  DECL PDAT PReload_XPNW1_1_3={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
     25  DECL LDAT Lpnw1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    54  DECL LDAT Lpnw2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    55  DECL E6POS XDROP73={X 156.140869,Y 596.295715,Z 615.623230,A 6.04692936,B -8.02280807,C -82.7209473,S 6,T 58,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    56  DECL FDAT FDROP73={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    57  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    58  DECL E6POS XP1={X -961.490173,Y 265.809387,Z 1090.12085,A 30.7095222,B 5.15975904,C -176.833344,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    59  DECL FDAT FP1={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    60  DECL PDAT PPDAT8={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    61  DECL PDAT PPDAT9={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    62  DECL E6POS XP2={X -2340.77637,Y -67.3134537,Z -2402.96,A 178.721222,B 74.3561554,C 43.7313080,S 6,T 59,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    63  DECL FDAT FP2={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    64  DECL PDAT PPDAT11={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    65  DECL E6POS XP3={X -1824.18188,Y -1001.09119,Z -157.213959,A -87.6076279,B -4.42733240,C -177.429916,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    66  DECL FDAT FP3={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    67  DECL PDAT PPDAT12={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    68  DECL E6POS XP4={X 502.171722,Y 190.181396,Z -135.596970,A -6.24112272,B -3.20316982,C 176.013672,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    69  DECL FDAT FP4={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    70  DECL PDAT PPDAT13={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    71  DECL E6POS XP5={X 403.314392,Y 226.179260,Z -114.475060,A -6.33512926,B 0.0627186,C 178.051514,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    72  DECL FDAT FP5={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    73  DECL PDAT PPDAT14={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
```
_50 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3A.dat.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt3A.src`

changed, integrator program: 17 code line(s) removed, 28 added; 97 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3A.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3A.src.diff)

Attributes: &REL 227 -> &REL 234; &COMMENT GE4_003_GUN1 -> &COMMENT 03-10-R1 PNW1 NUT 3 ST2

```diff
@@ base line 28, backup line 12 @@
     12  BAS (#INITMOV,0 )
     37  $BWDSTART=FALSE
-    41  LDAT_ACT=LCPDAT6
+    38  PDAT_ACT=PPDAT1
     39  FDAT_ACT=FP20
-    43  BAS(#CP_PARAMS,2)
-    44  LIN XP20 C_DIS C_DIS
+    40  BAS(#PTP_PARAMS,100)
+    41  PTP XP20 C_DIS
     48  INTERRUPT DECL 20 WHEN CL_GunStrokePositionLPT<137000 DO GUN_OPEN_LOST()
     49  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
     50  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
-    61  LOOP
-    62  WAIT FOR NEXT_NUT_READY==TRUE
-    63  GUN_OPEN_CHECK()
+    53  INTERRUPT DECL 23 WHEN CL_ClampOpen==FALSE DO GUN_OPEN_LOST()
+    54  INTERRUPT DECL 24 WHEN CL_PinRetracted==FALSE DO GUN_OPEN_LOST()
+    57  CT_NUT_WAIT(3)
     60  INTERRUPT ON 20
     61  INTERRUPT ON 21
     62  INTERRUPT ON 22
+    63  INTERRUPT ON 23
+    64  INTERRUPT ON 24
+    66  PEDESTAL_CLEAR_CHECK()
     69  $BWDSTART=FALSE
     70  LDAT_ACT=LCPDAT4
@@ base line 71, backup line 72 @@
     72  BAS(#CP_PARAMS,2)
     73  LIN XP13 C_DIS C_DIS
-    75  IF di004UseDryCycle==FALSE THEN
+    79  IF NOT di004UseDryCycle THEN
     81  $BWDSTART=FALSE
     82  LDAT_ACT=LCPDAT11
@@ base line 87, backup line 91 @@
     91  INTERRUPT OFF 21
     92  INTERRUPT OFF 22
+    93  INTERRUPT OFF 23
+    94  INTERRUPT OFF 24
     96  CENTERLINE_WELD()
+   100  WHILE NUT_WELD_RETRY
+   101  NUT_WELD_RETRY=FALSE
+   102  Request_next_nut()
+   103  WAIT FOR NUT_READY==TRUE
+   104  CENTERLINE_WELD()
+   105  ENDWHILE
    108  INTERRUPT ON 20
    109  INTERRUPT ON 21
    110  INTERRUPT ON 22
+   111  INTERRUPT ON 23
+   112  INTERRUPT ON 24
+   114  PEDESTAL_CLEAR_CHECK()
    115  ENDIF
    118  $BWDSTART=FALSE
@@ base line 104, backup line 128 @@
    128  INTERRUPT OFF 21
    129  INTERRUPT OFF 22
-   107  IF NOT NUT_WELD_RETRY THEN
-   108  EXIT
-   109  ENDIF
```
_20 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3A.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt3B.dat`

changed, integrator program: 83 code line(s) removed, 6 added; 1 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3B.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3B.dat.diff)

Attributes: &ACCESS RVO2 -> &ACCESS RVO1; &REL 1 -> &REL 234; &COMMENT GE4_003_GUN1 -> &COMMENT 03-10-R1 PNW1 NUT 3 ST2

Data changes:

- XP13 (E6POS) re-taught: moved 5.2 mm
- XP17 (E6POS) re-taught: moved 5.2 mm
- XP20 (E6POS) re-taught: moved 101.2 mm, rotated up to 0.9 deg, S/T 2/2 -> 2/34 (ARM CONFIGURATION CHANGED)
- PPDAT2 (PDAT): {VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.... -> {VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50....
- added 1 DEFDAT: style1app1opt3b
- removed 1 DEFDAT: style1app1opt3B
- removed 19 E6POS: XABOVENUT1, XDROP73, XNUT1, XP1, XP2, XP3, XP4, XP5, XP6, XP8, XP9, XP10 ...
- removed 19 FDAT: FAboveNut1, FDROP73, FNut1, FP1, FP2, FP3, FP4, FP5, FP6, FP8, FP9, FP10 ...
- removed 13 LDAT: LCPDAT1, LCPDAT2, LCPDAT3, LCPDAT5, LCPDAT7, LCPDAT8, LCPDAT9, LCPDAT21, Lpnw2, Lpnw3, LReload_XPNW1_1_1, LReload_XPNW1_1_2 ...
- removed 2 NUTWELDDAT: NutWeldDAT1, NutWeldDAT2
- removed 24 PDAT: PPDAT3, PPDAT4, PPDAT5, PPDAT6, PPDAT7, PPDAT8, PPDAT9, PPDAT10, PPDAT11, PPDAT12, PPDAT13, PPDAT14 ...

Runtime values (left out of the code diff): LAST_BASIS: {POINT1[] "P18                     ",POI... -> {POINT1[] "P0                      ",POI...

```diff
@@ base line 7, backup line 7 @@
-     7  DEFDAT style1app1opt3B
+     7  DEFDAT style1app1opt3b
     10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
-    16  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    17  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    18  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    19  DECL E6POS XP10={X -2075.68359,Y 854.949158,Z 1307.29810,A 77.6920624,B -20.6746445,C -80.6289597,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    20  DECL FDAT FP10={TOOL_NO 7,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    21  DECL E6POS XNUT1={X -12.8878489,Y 123.584129,Z -36.2668114,A 60.1760483,B -3.21555185,C -5.74943399,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    22  DECL FDAT FNut1={TOOL_NO 7,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    23  DECL E6POS XP40={X 194.480,Y 444.441528,Z 109.191170,A 59.0454025,B -2.16523719,C -3.66616058,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    24  DECL FDAT FP40={TOOL_NO 7,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    25  DECL E6POS XP20={X -3678.25781,Y -44.2650108,Z -442.362579,A -178.367340,B 0.267035842,C 179.968063,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    17  DECL E6POS XP20={X -3747.39,Y 5.76903486,Z -387.973175,A -178.432297,B -0.654858828,C -179.985626,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     18  DECL FDAT FP20={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    27  DECL E6POS XABOVENUT1={X -16.2189884,Y 123.785316,Z 31.4176292,A 59.9875450,B -3.00310516,C -5.37727165,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    28  DECL FDAT FAboveNut1={TOOL_NO 7,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    29  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    31  DECL NutWeldDAT NutWeldDAT1={GunNr 3,SpotNr 3,Offset 0}
-    32  DECL LDAT XPNW1CPDAT={VEL 0.150000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000}
     20  DECL FDAT FPNW1={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    34  DECL PDAT PPDAT6={ACC 100.000,APO_DIST 100.000,APO_MODE #CPTP,GEAR_JERK 50.0000,EXAX_IGN 0}
     21  DECL E6POS XPNW1={X -684.340210,Y -936.680359,Z 6.96372366,A -85.0124512,B -3.00309157,C -5.37728167,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    36  DECL LDAT LCPDAT7={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    37  DECL LDAT LCPDAT8={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    38  DECL PDAT PPDAT10={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    39  DECL E6POS XP50={X -1950.08691,Y 799.801636,Z 1115.17920,A 76.5103378,B -21.3705120,C -77.1953812,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    40  DECL FDAT FP50={TOOL_NO 7,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    42  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     23  DECL NutWeld_SUGG_T LAST_NutWeld={POINT1[] "PNW3_SPOT03             ",POINT2[] "PNW0                    ",CP_PARAMS[] "CPDATNutWeld0           ",PTP_PARAMS[] "PDATNutWeld0            ",CONT[] "C_PTP                   ",CP_VEL[] "2  [...]
-    44  DECL NutWeldDAT NutWeldDAT2={GunNr 3,SpotNr 3,Offset 0}
-    45  DECL LDAT LCPDAT2={ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     24  DECL MODULEPARAM_T LAST_TP_PARAMS={PARAMS[] "NutWeld_CmdPos=Weld; NutWeld_Move=LIN; NutWeld_NutWeldDat=NutWeldDAT1; NutWeld_NWGunNr=3; NutWeld_NWSpotNr=3; NutWeld_NWOffset=0; Kuka.MoveDataName=CPDAT2; Kuka.VelocityPath=2; Kuka.Poin [...]
-    47  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    48  DECL LDAT LCPDAT3={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    49  DECL LDAT LCPDAT21={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    50  DECL LDAT LReload_XPNW1_1_1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    51  DECL LDAT LReload_XPNW1_1_2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    52  DECL PDAT PReload_XPNW1_1_3={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
     25  DECL LDAT Lpnw1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    54  DECL LDAT Lpnw2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    55  DECL E6POS XDROP73={X 156.140869,Y 596.295715,Z 615.623230,A 6.04692936,B -8.02280807,C -82.7209473,S 6,T 58,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    56  DECL FDAT FDROP73={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    57  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    58  DECL E6POS XP1={X -961.490173,Y 265.809387,Z 1090.12085,A 30.7095222,B 5.15975904,C -176.833344,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    59  DECL FDAT FP1={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    60  DECL PDAT PPDAT8={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    61  DECL PDAT PPDAT9={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    62  DECL E6POS XP2={X -2340.77637,Y -67.3134537,Z -2402.96,A 178.721222,B 74.3561554,C 43.7313080,S 6,T 59,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    63  DECL FDAT FP2={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    64  DECL PDAT PPDAT11={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    65  DECL E6POS XP3={X -1824.18188,Y -1001.09119,Z -157.213959,A -87.6076279,B -4.42733240,C -177.429916,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    66  DECL FDAT FP3={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    67  DECL PDAT PPDAT12={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    68  DECL E6POS XP4={X 502.171722,Y 190.181396,Z -135.596970,A -6.24112272,B -3.20316982,C 176.013672,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    69  DECL FDAT FP4={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    70  DECL PDAT PPDAT13={VEL 100.000,ACC 100.000,APO_DIST 50.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    71  DECL E6POS XP5={X 403.314392,Y 226.179260,Z -114.475060,A -6.33512926,B 0.0627186,C 178.051514,S 6,T 50,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    72  DECL FDAT FP5={TOOL_NO 1,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
```
_50 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3B.dat.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt3B.src`

changed, integrator program: 17 code line(s) removed, 28 added; 97 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3B.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3B.src.diff)

Attributes: &ACCESS RVO2 -> &ACCESS RVO1; &REL 1 -> &REL 234; &COMMENT GE4_003_GUN1 -> &COMMENT 03-10-R1 PNW1 NUT 3 ST2

```diff
@@ base line 28, backup line 12 @@
     12  BAS (#INITMOV,0 )
     37  $BWDSTART=FALSE
-    41  LDAT_ACT=LCPDAT6
+    38  PDAT_ACT=PPDAT1
     39  FDAT_ACT=FP20
-    43  BAS(#CP_PARAMS,2)
-    44  LIN XP20 C_DIS C_DIS
+    40  BAS(#PTP_PARAMS,100)
+    41  PTP XP20 C_DIS
     48  INTERRUPT DECL 20 WHEN CL_GunStrokePositionLPT<137000 DO GUN_OPEN_LOST()
     49  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
     50  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
-    61  LOOP
-    62  WAIT FOR NEXT_NUT_READY==TRUE
-    63  GUN_OPEN_CHECK()
+    53  INTERRUPT DECL 23 WHEN CL_ClampOpen==FALSE DO GUN_OPEN_LOST()
+    54  INTERRUPT DECL 24 WHEN CL_PinRetracted==FALSE DO GUN_OPEN_LOST()
+    57  CT_NUT_WAIT(3)
     60  INTERRUPT ON 20
     61  INTERRUPT ON 21
     62  INTERRUPT ON 22
+    63  INTERRUPT ON 23
+    64  INTERRUPT ON 24
+    66  PEDESTAL_CLEAR_CHECK()
     69  $BWDSTART=FALSE
     70  LDAT_ACT=LCPDAT4
@@ base line 71, backup line 72 @@
     72  BAS(#CP_PARAMS,2)
     73  LIN XP13 C_DIS C_DIS
-    75  IF di004UseDryCycle==FALSE THEN
+    79  IF NOT di004UseDryCycle THEN
     81  $BWDSTART=FALSE
     82  LDAT_ACT=LCPDAT11
@@ base line 87, backup line 91 @@
     91  INTERRUPT OFF 21
     92  INTERRUPT OFF 22
+    93  INTERRUPT OFF 23
+    94  INTERRUPT OFF 24
     96  CENTERLINE_WELD()
+   100  WHILE NUT_WELD_RETRY
+   101  NUT_WELD_RETRY=FALSE
+   102  Request_next_nut()
+   103  WAIT FOR NUT_READY==TRUE
+   104  CENTERLINE_WELD()
+   105  ENDWHILE
    108  INTERRUPT ON 20
    109  INTERRUPT ON 21
    110  INTERRUPT ON 22
+   111  INTERRUPT ON 23
+   112  INTERRUPT ON 24
+   114  PEDESTAL_CLEAR_CHECK()
    115  ENDIF
    118  $BWDSTART=FALSE
@@ base line 104, backup line 128 @@
    128  INTERRUPT OFF 21
    129  INTERRUPT OFF 22
-   107  IF NOT NUT_WELD_RETRY THEN
-   108  EXIT
-   109  ENDIF
```
_20 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3B.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app2opt1.dat`

changed, integrator program: 144 code line(s) removed, 1 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.dat.diff)

Attributes: -&ACCESS RVO2; -&REL 21; +&ACCESS RVO1; +&REL 29; +&COMMENT 03-10-R1 NUT CHECK SENSOR

Data changes:

- XP31 (E6POS) re-taught: moved 4.9 mm
- removed 43 E6POS: XP1, XP2, XP3, XP4, XP5, XP6, XP7, XP8, XP9, XP10, XP11, XP12 ...
- removed 43 FDAT: FP1, FP2, FP3, FP4, FP5, FP6, FP7, FP8, FP9, FP10, FP11, FP12 ...
- removed 23 LDAT: LCPDAT1, LCPDAT2, LCPDAT3, LCPDAT4, LCPDAT5, LCPDAT6, LCPDAT7, LCPDAT8, LCPDAT9, LCPDAT10, LCPDAT11, LCPDAT12 ...
- removed 1 NUTWELDDAT: NutWeldDAT1
- removed 33 PDAT: PPDAT1, PPDAT2, PPDAT3, PPDAT4, PPDAT5, PPDAT6, PPDAT7, PPDAT8, PPDAT9, PPDAT10, PPDAT11, PPDAT12 ...

```diff
@@ base line 13, backup line 14 @@
     14  BOOL NutWeld_TEMPLATE=TRUE
     21  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P0                      ",POINT2[] "P0                      ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT0                   ",CONT[] "                        ",CP_VEL[] "2.0    [...]
-    21  DECL E6POS XP1={X 504.083038,Y -786.363281,Z 1705.62244,A -111.705475,B 40.2604523,C 19.4570885,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    22  DECL FDAT FP1={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    23  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    24  DECL E6POS XP2={X -3354.51514,Y -143.403854,Z -774.646057,A -178.361191,B -0.268041790,C 179.960083,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    25  DECL FDAT FP2={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    26  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    27  DECL E6POS XP3={X -68.0168152,Y -1722.30078,Z 1086.26270,A -91.6317673,B 0.275582,C -0.0421518087,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    28  DECL FDAT FP3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    29  DECL LDAT LCPDAT2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    30  DECL E6POS XP4={X -82.9339371,Y -1983.86072,Z 1026.44580,A -91.6317673,B 0.275582284,C -0.0421519652,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    31  DECL FDAT FP4={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    32  DECL LDAT LCPDAT3={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    33  DECL E6POS XP5={X -3596.24170,Y -96.9433,Z -420.628052,A -178.367157,B -0.266017616,C 179.960464,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    34  DECL FDAT FP5={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    35  DECL LDAT LCPDAT4={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    36  DECL E6POS XP6={X -3850.17822,Y -104.182068,Z -419.448608,A -178.367157,B -0.266017616,C 179.960464,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    37  DECL FDAT FP6={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    38  DECL LDAT LCPDAT5={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     22  DECL NutWeld_SUGG_T LAST_NutWeld={POINT1[] "PNW1                    ",POINT2[] "PNW0                    ",CP_PARAMS[] "CPDATNutWeld0           ",PTP_PARAMS[] "PDATNutWeld0            ",CONT[] "C_PTP                   ",CP_VEL[] "2  [...]
-    40  DECL NutWeldDAT NutWeldDAT1={GunNr 1,SpotNr 1,Offset 25}
-    41  DECL LDAT XPNW1CPDAT={VEL 0.150000,ACC 100.000,APO_DIST 10.0000,APO_FAC 50.0000}
-    42  DECL FDAT FPNW1={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    43  DECL PDAT PPDAT2={ACC 100.000,APO_DIST 100.000,APO_MODE #CPTP,GEAR_JERK 50.0000}
-    44  DECL E6POS XPNW1={X -3849.50415,Y -104.198906,Z -367.222534,A -178.367157,B -0.266017586,C 179.960464,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     23  DECL MODULEPARAM_T LAST_TP_PARAMS={PARAMS[] "NutWeld_CmdPos=Weld; NutWeld_Move=PTP; NutWeld_NutWeldDat=NutWeldDAT1; NutWeld_NWGunNr=1; NutWeld_NWSpotNr=1; NutWeld_NWOffset=25; Kuka.MoveDataPtpName=PDAT2; Kuka.VelocityPtp=100; Kuka. [...]
-    46  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    47  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    48  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    49  DECL E6POS XP7={X -3850.17822,Y -104.182068,Z -419.448608,A -178.367157,B -0.266017616,C 179.960464,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    50  DECL FDAT FP7={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    51  DECL LDAT LCPDAT6={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    52  DECL E6POS XP8={X -3596.24170,Y -96.9433670,Z -420.628,A -178.367157,B -0.266018540,C 179.960464,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    53  DECL FDAT FP8={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    54  DECL PDAT PPDAT6={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    55  DECL E6POS XP9={X -3850.17822,Y -104.182068,Z -419.448608,A -178.367172,B -0.266017824,C 179.960464,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    56  DECL FDAT FP9={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    57  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    58  DECL PDAT PPDAT8={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    59  DECL E6POS XP10={X -3881.98315,Y -151.523331,Z -362.167358,A -178.367172,B -0.266017944,C 179.960464,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    60  DECL FDAT FP10={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    61  DECL E6POS XP11={X -3881.98315,Y -151.523331,Z -391.565582,A -178.367172,B -0.266018,C 179.960464,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    62  DECL FDAT FP11={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    63  DECL LDAT LCPDAT7={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    64  DECL E6POS XP12={X -3881.98218,Y -151.525742,Z -362.166504,A -178.366943,B -0.266011864,C 179.960327,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    65  DECL FDAT FP12={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    66  DECL LDAT LCPDAT8={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    67  DECL E6POS XPNW2={X -3849.50415,Y -104.198906,Z -367.222534,A -178.367157,B -0.266017586,C 179.960464,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    68  DECL FDAT FPNW2={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    69  DECL PDAT PPDAT9={ACC 100.000,APO_DIST 100.000,APO_MODE #CPTP,GEAR_JERK 50.0000}
-    70  DECL E6POS XP13={X -3881.98315,Y -151.523331,Z -391.565582,A -178.367172,B -0.266017824,C 179.960464,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    71  DECL FDAT FP13={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    72  DECL LDAT LCPDAT9={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    73  DECL E6POS XP14={X -3850.17822,Y -104.182068,Z -419.448608,A -178.367172,B -0.266017824,C 179.960464,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    74  DECL FDAT FP14={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    75  DECL PDAT PPDAT10={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    76  DECL PDAT PPDAT11={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    77  DECL E6POS XP15={X -3596.24170,Y -96.9433670,Z -420.628,A -178.367157,B -0.266018540,C 179.960464,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
```
_109 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.dat.diff_

### `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`

changed, integrator program: 17 code line(s) removed, 48 added; 111 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.src.diff)

Attributes: -&ACCESS RVO2; -&REL 21; +&ACCESS RVO1; +&REL 29; +&COMMENT 03-10-R1 NUT CHECK SENSOR

```diff
@@ base line 26, backup line 11 @@
     11  INTERRUPT ON 3
     12  BAS (#INITMOV,0 )
+    38  bscrapGE4=FALSE
     42  $BWDSTART=FALSE
     43  PDAT_ACT=PPDAT16
     44  FDAT_ACT=FP22
     45  BAS(#PTP_PARAMS,100)
-    43  PTP XP22
+    46  PTP XP22 C_DIS
     56  AC_ApplicationCheck (1)
     61  $BWDSTART=FALSE
@@ base line 57, backup line 64 @@
     64  BAS(#CP_PARAMS,2)
     65  LIN XP28
-    62  IF di004UseDryCycle==FALSE THEN
-    64  IF ($IN[227]==TRUE) THEN
-    65  PARTPRESENT1=TRUE
-    66  ENDIF
+    71  IF NOT di004UseDryCycle THEN
     72  WAIT SEC 0.2
+    74  PARTPRESENT1=di227NutPresent1
     75  ENDIF
     78  $BWDSTART=FALSE
@@ base line 75, backup line 80 @@
     80  FDAT_ACT=FP31
     81  BAS(#PTP_PARAMS,100)
-    77  PTP XP31
+    82  PTP XP31 C_DIS
     87  $BWDSTART=FALSE
     88  LDAT_ACT=LCPDAT16
@@ base line 85, backup line 90 @@
     90  BAS(#CP_PARAMS,2)
     91  LIN XP32
-    90  IF di004UseDryCycle==FALSE THEN
-    92  IF ($IN[227]==TRUE) THEN
-    93  PARTPRESENT2=TRUE
-    94  ENDIF
+    97  IF NOT di004UseDryCycle THEN
     98  WAIT SEC 0.2
+   100  PARTPRESENT2=di227NutPresent1
    101  ENDIF
    104  $BWDSTART=FALSE
@@ base line 103, backup line 106 @@
    106  FDAT_ACT=FP38
    107  BAS(#PTP_PARAMS,100)
-   105  PTP XP38
+   108  PTP XP38 C_DIS
    113  $BWDSTART=FALSE
    114  LDAT_ACT=LCPDAT17
@@ base line 113, backup line 116 @@
    116  BAS(#CP_PARAMS,2)
    117  LIN XP36
-   118  IF di004UseDryCycle==FALSE THEN
-   120  IF ($IN[227]==TRUE) THEN
-   121  PARTPRESENT3=TRUE
-   122  ENDIF
+   123  IF NOT di004UseDryCycle THEN
    124  WAIT SEC 0.2
+   126  PARTPRESENT3=di227NutPresent1
```
_55 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app2opt2.dat`

changed, integrator program: 51 code line(s) removed, 0 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.dat.diff)

Attributes: &ACCESS RVP2 -> &ACCESS RVO1; &COMMENT GE4_NutCHK -> &COMMENT 03-10-R1 NUT CHECK CAMERA

Data changes:

- removed 16 E6POS: XAtNutCheck1, XATNUTCHECK4, XP1, XP2, XP4, XP5, XP7, XP10, XP20, XP30, XP40, XP50 ...
- removed 16 FDAT: FAtNutCheck1, FAtNutCheck4, FP1, FP2, FP4, FP5, FP7, FP10, FP20, FP30, FP40, FP50 ...
- removed 1 INT: nCount
- removed 4 LDAT: LCPDAT1, LCPDAT2, LCPDAT3, LCPDAT4
- removed 14 PDAT: PL, PPDAT1, PPDAT2, PPDAT3, PPDAT4, PPDAT5, PPDAT6, PPDAT7, PPDAT8, PPDAT9, PPDAT11, PPDAT27 ...

```diff
@@ base line 6, backup line 6 @@
      6  DEFDAT style1app2opt2
      9  EXT BAS (BAS_COMMAND :IN,REAL :IN )
-    15  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    16  DECL LDAT LCPDAT2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    17  DECL LDAT LCPDAT3={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    18  DECL E6POS XP10={X 2281.82666,Y 91.3649292,Z 1193.99182,A 7.45437717,B 25.0854454,C -152.934311,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    19  DECL FDAT FP10={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    20  DECL E6POS XP20={X -754.658569,Y 975.418701,Z 816.985291,A -77.7530136,B 74.7448044,C 166.116241,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    21  DECL FDAT FP20={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    22  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    23  DECL E6POS XP30={X -901.723145,Y 967.531250,Z 193.220627,A -69.3627243,B 43.5717201,C -178.930527,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    24  DECL FDAT FP30={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    25  DECL E6POS XP40={X -805.908447,Y -1889.91296,Z 1609.52112,A -104.761292,B 0.614048064,C 179.948,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    26  DECL FDAT FP40={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    27  DECL E6POS XATNUTCHECK4={X -822.738831,Y 721.997314,Z 139.945435,A -67.9592667,B 13.8679914,C -179.228760,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    28  DECL FDAT FAtNutCheck4={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    29  DECL E6POS XP50={X -853.289612,Y 785.232605,Z 116.436310,A -67.8503265,B 26.4141159,C -179.377487,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    30  DECL FDAT FP50={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    31  DECL E6POS XP60={X -709.683105,Y -1914.79602,Z 1506.28113,A -104.768265,B 0.613393545,C 179.947739,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    32  DECL FDAT Fp60={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    33  DECL E6POS XP70={X -754.658569,Y 975.418701,Z 816.985291,A -77.7530136,B 74.7448044,C 166.116241,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    34  DECL FDAT FP70={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    35  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    36  DECL E6POS XP80={X -21.1073933,Y 977.088257,Z 1822.06055,A -57.9586,B 86.2354584,C -137.216766,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    37  DECL FDAT FP80={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    38  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    39  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    40  DECL PDAT PPDAT8={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    41  DECL E6POS XP92={X 2434.83228,Y 96.6232,Z 1122.02954,A -15.1512289,B -2.07428622,C -159.203690,S 6,T 58,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    42  DECL FDAT FP92={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    43  DECL PDAT PPDAT9={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     15  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P0                      ",POINT2[] "P0                      ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT0                   ",CONT[] "                        ",CP_VEL[] "2.0    [...]
-    45  DECL E6POS XP1={X -756.930054,Y -1663.77429,Z 1079.05762,A -104.756149,B 0.614769,C 179.948242,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    46  DECL FDAT FP1={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    47  DECL PDAT PL={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    48  DECL E6POS XAtNutCheck1={X -806.267639,Y -1892.02271,Z 1807.86584,A -104.760185,B 0.614405334,C 179.948120,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    49  DECL FDAT FAtNutCheck1={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    50  DECL INT nCount
-    52  DECL PDAT PPDAT27={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    53  DECL E6POS XP2={X -725.920410,Y -1758.69482,Z 1448.59143,A -104.766548,B 0.615574777,C 179.948090,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    54  DECL FDAT FP2={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     17  DECL LDAT LCPDAT0={VEL 2.00000,ACC 80.0000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     18  DECL E6POS XP3={X -709.833740,Y -2035.40430,Z 1423.71777,A -98.4577484,B -5.84655905,C -164.806564,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     19  DECL FDAT FP3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    58  DECL PDAT PPDAT28={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    59  DECL E6POS XP4={X -725.920410,Y -1758.69482,Z 1448.59143,A -104.766548,B 0.615574777,C 179.948090,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    60  DECL FDAT FP4={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    61  DECL E6POS XP5={X -724.403137,Y -1811.34314,Z 1367.20557,A -104.758530,B 0.614156485,C 179.947769,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    62  DECL FDAT FP5={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    63  DECL PDAT PPDAT29={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     20  DECL E6POS XP6={X -3780.88599,Y -731.523132,Z -847.811157,A -165.231735,B -0.613393545,C -0.0522668548,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     21  DECL FDAT FP6={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    66  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    67  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    68  DECL LDAT LCPDAT4={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    69  DECL E6POS XP7={X -728.679932,Y -2041.37085,Z 1460.12866,A -87.6372147,B 17.6803131,C 179.975311,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    70  DECL FDAT FP7={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    71  DECL PDAT PPDAT6={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     22  DECL PDAT PPDAT10={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
```
_2 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.dat.diff_

### `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`

changed, integrator program: 6 code line(s) removed, 5 added; 63 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.src.diff)

Attributes: &ACCESS RVP2 -> &ACCESS RVO1; &COMMENT GE4_NutCHK -> &COMMENT 03-10-R1 NUT CHECK CAMERA

```diff
@@ base line 35, backup line 33 @@
     33  FDAT_ACT=FP6
     34  BAS(#PTP_PARAMS,100)
-    37  PTP XP6
+    35  PTP XP6 C_DIS
     40  $BWDSTART=FALSE
     41  LDAT_ACT=LCPDAT0
@@ base line 49, backup line 50 @@
     50  do080RepositionTooling1=TRUE
     53  WAIT FOR di080ToolRepositioned1
-    53  WAIT SEC 0.2
+    60  WAIT SEC 2.0
     61  SWITCH nOption
     62  CASE 1,2,7,8
-    57  IF (di100CameraJudmentOK==TRUE) AND (di101CameraJudmentNG==FALSE) THEN
+    64  IF (di100CameraJudgmentOK==TRUE) AND (di101CameraJudgmentNG==FALSE) THEN
     65  bscrapGE4 = FALSE
     66  ELSE
@@ base line 61, backup line 68 @@
     68  ENDIF
     69  CASE 12
-    63  IF (di100CameraJudmentOK==TRUE) AND (di101CameraJudmentNG==FALSE) THEN
+    72  IF (di100CameraJudgmentOK==TRUE) AND (di101CameraJudgmentNG==FALSE) THEN
     73  do141RedRabbitFailed=TRUE
     74  ENDIF
-    66  IF (di100CameraJudmentOK==FALSE) AND (di101CameraJudmentNG==TRUE) THEN
+    77  IF (di100CameraJudgmentOK==FALSE) AND (di101CameraJudgmentNG==TRUE) THEN
     78  do142RedRabbitPassed=TRUE
     79  ENDIF
     80  ENDSWITCH
-    76  AC_Application (1,True)
     86  END
```

### `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.dat`

changed, integrator program: 17 code line(s) removed, 1 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt1.dat.diff](diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt1.dat.diff)

Attributes: &ACCESS RVO2 -> &ACCESS RVO1; &REL 226 -> &REL 234; &COMMENT GE4_Conveyor -> &COMMENT 03-10-R1 DROP CONVEYOR

Data changes:

- XP2 (E6POS) re-taught: moved 200.5 mm, rotated up to 17.4 deg
- removed 5 E6POS: XP4, XP6, XP8, XP9, XP10
- removed 5 FDAT: FP4, FP6, FP8, FP9, FP10
- removed 6 PDAT: PPDAT3, PPDAT4, PPDAT5, PPDAT6, PPDAT9, PPDAT12

Runtime values (left out of the code diff): LAST_BASIS: {POINT1[] "P10                     ",POI... -> {POINT1[] "P0                      ",POI...

```diff
@@ base line 17, backup line 17 @@
     17  DECL E6POS XATDROP3={X -1563.67676,Y -913.306702,Z 449.989929,A 179.143311,B 30.0803795,C -34.7621422,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     18  DECL FDAT FAtDrop3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    19  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
     19  DECL MODULEPARAM_T LAST_TP_PARAMS={PARAMS[] "AC_CmdZones=DropOff; AC_CmdParam=2; AC_ZoneRepo=True; AC_UseState=True; AC_Blending=False                               "}
-    21  DECL E6POS XP2={X -1471.65808,Y -890.400757,Z 672.790649,A 177.082932,B 4.31955290,C -0.298484206,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    20  DECL E6POS XP2={X -1279.37976,Y -897.098,Z 616.329468,A 176.629059,B 21.7134552,C -1.31570351,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     21  DECL FDAT FP2={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     22  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    24  DECL PDAT PPDAT9={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    25  DECL E6POS XP4={X -703.480469,Y -1395.30945,Z 616.365723,A -134.980774,B 21.6840553,C -1.41442871,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    26  DECL FDAT FP4={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     23  DECL E6POS XP5={X -1279.37976,Y -897.098,Z 616.329468,A 176.629059,B 21.7134552,C -1.31570351,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     24  DECL FDAT FP5={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     25  DECL PDAT PPDAT10={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     26  DECL PDAT PPDAT11={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    31  DECL E6POS XP6={X -1035.24158,Y -1191.13391,Z 1034.36511,A 179.322769,B 1.56446958,C 5.43827724,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    32  DECL FDAT FP6={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    33  DECL PDAT PPDAT12={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     27  DECL PDAT PPDAT13={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     28  DECL E6POS XP7={X -988.705139,Y -820.766479,Z 2569.14844,A 137.545090,B -48.9822197,C 56.5858917,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
@@ base line 42, backup line 35 @@
     35  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     36  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    44  DECL E6POS XP8={X -709.683167,Y -1914.79602,Z 1611.27075,A -104.768265,B 0.613394141,C 179.947723,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    45  DECL FDAT FP8={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    46  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    47  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    48  DECL E6POS XP9={X -709.683105,Y -1914.79602,Z 1506.28113,A -104.768265,B 0.613393545,C 179.947739,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    49  DECL FDAT FP9={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    50  DECL PDAT PPDAT6={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    51  DECL E6POS XP10={X -709.683105,Y -1914.79602,Z 1506.28113,A -104.768265,B 0.613393545,C 179.947739,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    52  DECL FDAT FP10={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     37  ENDDAT
```

### `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src`

changed, integrator program: 4 code line(s) removed, 4 added; 45 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src.diff](diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src.diff)

Attributes: &ACCESS RVO2 -> &ACCESS RVO1; &REL 226 -> &REL 234; &COMMENT GE4_Conveyor -> &COMMENT 03-10-R1 DROP CONVEYOR

```diff
@@ base line 10, backup line 10 @@
     10  INTERRUPT ON 3
     11  BAS (#INITMOV,0 )
+    32  TRIGGER WHEN DISTANCE=1 DELAY=0 DO do070ApplicationClear1=TRUE
     34  $BWDSTART=FALSE
     35  PDAT_ACT=PPDAT10
@@ base line 37, backup line 57 @@
     57  LIN XAtDrop3
     67  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
-    50  GRPg_Check(1, 1, FALSE, 1)
-    53  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254] )
-    56  $OUT[18]=FALSE
+    71  WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2 )
+    75  do018Part1InGripper=FALSE
     80  $BWDSTART=FALSE
     81  PDAT_ACT=PPDAT7
@@ base line 77, backup line 97 @@
     97  FDAT_ACT=FP3
     98  BAS(#PTP_PARAMS,100)
-    79  PTP XP3
+    99  PTP XP3 C_DIS
    108  AC_DropOff (1,True)
    113  $BWDSTART=FALSE
```

### `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.dat`

changed, integrator program: 80 code line(s) removed, 0 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.dat.diff](diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.dat.diff)

Data changes:

- removed 26 E6POS: XATDROP3, XP1, XP2, XP3, XP4, XP5, XP6, XP7, XP8, XP9, XP10, XP11 ...
- removed 26 FDAT: FAtDrop3, FP1, FP2, FP3, FP4, FP5, FP6, FP7, FP8, FP9, FP10, FP11 ...
- removed 3 LDAT: LCPDAT0, LCPDAT1, LCPDAT3
- removed 25 PDAT: PPDAT1, PPDAT2, PPDAT3, PPDAT4, PPDAT5, PPDAT6, PPDAT7, PPDAT8, PPDAT9, PPDAT10, PPDAT12, PPDAT13 ...

```diff
@@ base line 9, backup line 9 @@
      9  DECL INT SUCCESS
     16  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P37                     ",POINT2[] "P37                     ",CP_PARAMS[] "CPDAT6                  ",PTP_PARAMS[] "PDAT34                  ",CONT[] "                        ",CP_VEL[] "2      [...]
-    17  DECL E6POS XATDROP3={X -1471.65808,Y -890.400757,Z 408.943,A 177.082932,B 4.31955290,C -0.298484236,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    18  DECL FDAT FAtDrop3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    19  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
     17  DECL MODULEPARAM_T LAST_TP_PARAMS={PARAMS[] "AC_CmdZones=DropOff; AC_CmdParam=2; AC_ZoneRepo=True; AC_UseState=True; AC_Blending=False                               "}
-    21  DECL E6POS XP2={X -1471.65808,Y -890.400757,Z 672.790649,A 177.082932,B 4.31955290,C -0.298484206,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    22  DECL FDAT FP2={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    23  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    24  DECL PDAT PPDAT9={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    25  DECL E6POS XP4={X -703.480469,Y -1395.30945,Z 616.365723,A -134.980774,B 21.6840553,C -1.41442871,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    26  DECL FDAT FP4={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    27  DECL E6POS XP5={X -1279.37976,Y -897.098,Z 616.329468,A 176.629059,B 21.7134552,C -1.31570351,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    28  DECL FDAT FP5={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    29  DECL PDAT PPDAT10={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     18  DECL PDAT PPDAT11={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    31  DECL E6POS XP6={X -1035.24158,Y -1191.13391,Z 1034.36511,A 179.322769,B 1.56446958,C 5.43827724,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    32  DECL FDAT FP6={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    33  DECL PDAT PPDAT12={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    34  DECL PDAT PPDAT13={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    35  DECL E6POS XP7={X -611.371521,Y -693.136719,Z 1916.56042,A 157.985474,B -61.9188309,C 9.87796,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    36  DECL FDAT FP7={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    37  DECL E6POS XP1={X -1440.21106,Y -892.543274,Z 457.022766,A 177.090073,B 1.60787833,C -0.160304546,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    38  DECL FDAT FP1={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    39  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    40  DECL E6POS XP3={X 370.852905,Y -298.257416,Z 2804.38916,A -147.361786,B -35.6047363,C 79.4075775,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    41  DECL FDAT FP3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    42  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    43  DECL LDAT LCPDAT0={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    44  DECL E6POS XP8={X 1206.28552,Y -208.912048,Z 319.300903,A -91.4409,B -0.232809097,C 0.168290034,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    45  DECL FDAT FP8={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    46  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    47  DECL E6POS XP9={X 1206.28552,Y -208.912048,Z 409.521729,A -91.4413757,B -0.232714087,C 0.168696448,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    48  DECL FDAT FP9={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    49  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    50  DECL E6POS XP10={X 1206.28552,Y -208.912048,Z 573.307922,A -91.4409,B -0.232809082,C 0.168290049,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    51  DECL FDAT FP10={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    52  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    53  DECL E6POS XP11={X 1206.28552,Y -208.912048,Z 1092.82214,A -91.4409,B -0.232809037,C 0.168290079,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    54  DECL FDAT FP11={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    55  DECL PDAT PPDAT6={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    56  DECL E6POS XP12={X 671.407898,Y -378.268097,Z 2030.44653,A -89.8029327,B 7.84505653,C 24.4156590,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    57  DECL FDAT FP12={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    58  DECL PDAT PPDAT8={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    59  DECL E6POS XP13={X 12.7359648,Y -130.494156,Z 3309.79932,A -58.5948639,B -68.7112122,C 63.6888771,S 3,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    60  DECL FDAT FP13={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    61  DECL E6POS XP14={X 12.7359648,Y -130.494156,Z 3309.79932,A -58.5948639,B -68.7112122,C 63.6888771,S 3,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    62  DECL FDAT FP14={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    63  DECL PDAT PPDAT14={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    64  DECL E6POS XP15={X 671.407898,Y -378.268097,Z 2030.44653,A -89.8029327,B 7.84505653,C 24.4156590,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    65  DECL FDAT FP15={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    66  DECL PDAT PPDAT15={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    67  DECL E6POS XP16={X 1206.28552,Y -208.912048,Z 1092.82214,A -91.4409,B -0.232809037,C 0.168290079,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    68  DECL FDAT FP16={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    69  DECL PDAT PPDAT16={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    70  DECL E6POS XP17={X 1206.28552,Y -208.912048,Z 573.307922,A -91.4409,B -0.232809082,C 0.168290049,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    71  DECL FDAT FP17={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    72  DECL PDAT PPDAT17={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    73  DECL E6POS XP18={X 1206.28552,Y -208.912048,Z 573.307922,A -91.4409,B -0.232809082,C 0.168290049,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
```
_42 more lines: see diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.dat.diff_

### `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src`

changed, integrator program: 4 code line(s) removed, 5 added; 39 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src.diff](diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src.diff)

Attributes: &COMMENT GE4_Conveyor -> &COMMENT 03-10-R1 RED RABBIT DROP

```diff
@@ base line 22, backup line 37 @@
     37  AC_DropOffCheck (2)
     43  CONTINUE
-    27  $OUT[249]=FALSE
+    44  do249Group1Home=FALSE
     47  CONTINUE
-    31  $OUT[250]=TRUE
+    48  do250Group1Work=TRUE
     53  $BWDSTART=FALSE
     54  PDAT_ACT=PPDAT25
@@ base line 38, backup line 56 @@
     56  BAS(#PTP_PARAMS,100)
     57  PTP XP27
+    62  TRIGGER WHEN DISTANCE=1 DELAY=0 DO do070ApplicationClear1=TRUE
     64  $BWDSTART=FALSE
     65  PDAT_ACT=PPDAT26
@@ base line 117, backup line 145 @@
    145  BAS(#CP_PARAMS,2)
    146  LIN XP23
-   121  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254] )
+   150  WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2 )
    155  $BWDSTART=FALSE
    156  LDAT_ACT=LCPDAT4
@@ base line 128, backup line 158 @@
    158  BAS(#CP_PARAMS,2)
    159  LIN XP24
-   132  $OUT[18]=FALSE
+   163  do018Part1InGripper=FALSE
    167  $BWDSTART=FALSE
    168  LDAT_ACT=LCPDAT7
```

### `KRC/R1/Program/StylePicks/Options/style1pick1opt1.dat`

changed, integrator program: 48 code line(s) removed, 1 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1.dat.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1.dat.diff)

Attributes: &REL 52 -> &REL 53; &COMMENT St1_PICK_GE4 -> &COMMENT 03-10-R1 PICK ST1

Data changes:

- XAtPick3 (E6POS) re-taught: moved 0.5 mm
- removed 17 E6POS: XP0, XP1, XP2, XP3, XP4, XP5, XP6, XP7, XP11, XP30, XP50, XP60 ...
- removed 17 FDAT: FP0, FP1, FP2, FP3, FP4, FP5, FP6, FP7, FP11, FP30, FP50, FP60 ...
- removed 2 LDAT: LCPDAT3, LCPDAT4
- removed 11 PDAT: PPDAT0, PPDAT1, PPDAT3, PPDAT5, PPDAT6, PPDAT7, PPDAT8, PPDAT9, PPDAT10, PPDAT11, PPDAT14

```diff
@@ base line 9, backup line 9 @@
      9  EXT BAS (BAS_COMMAND :IN,REAL :IN )
     10  DECL INT SUCCESS
-    17  DECL E6POS XTag4={X -612.686,Y -1589.39600,Z 2916.51807,A 84.5120,B -104.062,C 7.85700,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    18  DECL FDAT FTag4={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE}
-    19  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    20  DECL E6POS XTag3={X -570.159,Y -2455.64600,Z 462.298,A 90.7960,B -176.000,C -0.0550000,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    21  DECL FDAT FTag3={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE}
     17  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    23  DECL E6POS XTag1={X -570.159,Y -2469.59692,Z 262.786,A 90.7960,B -176.000,C -0.0560000,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    24  DECL FDAT FTag1={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE}
     18  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 0.0,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    26  DECL E6POS XTag2={X -570.159,Y -2466.10889,Z 312.664,A 90.7960,B -176.000,C -0.0560000,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    27  DECL FDAT FTag2={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE}
     19  DECL LDAT LCPDAT2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     20  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P12                     ",POINT2[] "P12                     ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT15                  ",CONT[] "                        ",CP_VEL[] "2.0    [...]
@@ base line 32, backup line 23 @@
     23  DECL E6POS XP10={X 1081.09485,Y -250.197342,Z 931.476,A -96.8303,B 37.9899406,C -15.7576666,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     24  DECL FDAT FP10={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    34  DECL E6POS XP30={X -602.469604,Y -2473.76245,Z 446.371094,A -89.4232254,B -2.67896390,C -179.996689,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    35  DECL FDAT FP30={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    36  DECL E6POS XAtPick3={X 1206.28552,Y -208.912048,Z 214.158249,A -91.4409,B -0.232809141,C 0.168289974,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    25  DECL E6POS XAtPick3={X 1206.28552,Y -208.912048,Z 214.640366,A -91.4409,B -0.232809022,C 0.168290094,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     26  DECL FDAT FAtPick3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    38  DECL E6POS XP1={X -603.354553,Y -2477.18481,Z 667.120239,A -89.3294754,B 0.653617203,C -179.853607,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    39  DECL FDAT FP1={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    40  DECL LDAT LCPDAT3={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     27  DECL E6POS XP40={X 1206.28552,Y -208.912048,Z 630.625366,A -91.4409,B -0.232809082,C 0.168290034,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     28  DECL FDAT FP40={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    43  DECL E6POS XP50={X 1206.28552,Y -208.912048,Z 409.521729,A -91.4413757,B -0.232714087,C 0.168696448,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    44  DECL FDAT FP50={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    45  DECL E6POS XP60={X 671.407898,Y -378.268097,Z 2030.44653,A -89.8029327,B 7.84505653,C 24.4156590,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    46  DECL FDAT FP60={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    47  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     29  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    49  DECL E6POS XP70={X 1525.90320,Y -261.054626,Z 1246.12451,A 16.2779942,B 28.5338478,C 22.5772171,S 2,T 42,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    50  DECL FDAT FP70={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    51  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     30  DECL E6POS XP30ABOVEPICK={X 1206.28552,Y -208.912048,Z 298.869263,A -91.4409,B -0.232809111,C 0.168290,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     31  DECL FDAT FP30AbovePick={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    54  DECL E6POS XP2={X -599.756165,Y -2478.73,Z 369.150330,A -89.4027710,B -3.84103417,C 179.935089,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    55  DECL FDAT FP2={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    56  DECL PDAT PPDAT6={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    57  DECL E6POS XP3={X -599.698364,Y -2469.82422,Z 501.779144,A -89.4027710,B -3.84103417,C 179.935089,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    58  DECL FDAT FP3={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    59  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    60  DECL PDAT PPDAT0={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    61  DECL E6POS XP0={X 1206.28552,Y -208.912048,Z 573.307922,A -91.4409,B -0.232809082,C 0.168290049,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    62  DECL FDAT FP0={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    63  DECL LDAT LCPDAT4={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    64  DECL PDAT PPDAT8={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    65  DECL E6POS XP4={X 0.0,Y 0.0,Z 0.0,A 0.0,B 0.0,C 0.0,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    66  DECL FDAT FP4={TOOL_NO 0,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    67  DECL PDAT PPDAT9={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    68  DECL E6POS XP5={X 1206.28552,Y -208.912048,Z 1092.82214,A -91.4409,B -0.232809037,C 0.168290079,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    69  DECL FDAT FP5={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    70  DECL E6POS XP6={X 12.7359648,Y -130.494156,Z 3309.79932,A -58.5948639,B -68.7112122,C 63.6888771,S 3,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    71  DECL FDAT FP6={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    72  DECL PDAT PPDAT10={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    73  DECL E6POS XP7={X -1067.77161,Y -2105.70923,Z -1670.46326,A -142.262650,B 26.2927914,C -143.375824,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
```
_12 more lines: see diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1.dat.diff_

### `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`

changed, integrator program: 7 code line(s) removed, 5 added; 85 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1.src.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1.src.diff)

Attributes: &REL 52 -> &REL 53; &COMMENT St1_PICK_GE4 -> &COMMENT 03-10-R1 PICK ST1

```diff
@@ base line 22, backup line 11 @@
     11  BAS (#INITMOV,0 )
     32  AC_pickUPCheck (1)
+    37  WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2)
     46  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
-    46  GRPg_Check(1, 1, FALSE, 1)
-    50  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254])
+    57  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO NUT_START=TRUE
     59  $BWDSTART=FALSE
     60  PDAT_ACT=PPDAT15
     61  FDAT_ACT=FP12
     62  BAS(#PTP_PARAMS,100)
-    59  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO NUT_STAR=TRUE
     63  PTP XP12
     66  $BWDSTART=FALSE
@@ base line 88, backup line 92 @@
     92  LIN XAtPick3
    102  GRPg_SetStateAndCheck(1, 2, 0.2, 1)
-   102  GRPg_Check(1, 2, FALSE, 1)
-   106  IF di004UseDryCycle==FALSE THEN
-   109  WAIT FOR ( $IN[253] ) AND ( $IN[254] )
-   112  $OUT[18]=TRUE
+   108  IF NOT di004UseDryCycle THEN
+   111  WAIT FOR ( di253PartPresent1 ) AND ( di254PartPresent2 )
+   117  do018Part1InGripper=TRUE
    119  ENDIF
    123  $BWDSTART=FALSE
```

### `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.dat`

changed, integrator program: 56 code line(s) removed, 0 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.dat.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.dat.diff)

Data changes:

- removed 20 E6POS: XP0, XP1, XP2, XP3, XP4, XP5, XP6, XP7, XP11, XP13, XP14, XP15 ...
- removed 20 FDAT: FP0, FP1, FP2, FP3, FP4, FP5, FP6, FP7, FP11, FP13, FP14, FP15 ...
- removed 3 LDAT: LCPDAT0, LCPDAT3, LCPDAT4
- removed 13 PDAT: PPDAT0, PPDAT1, PPDAT3, PPDAT5, PPDAT6, PPDAT7, PPDAT8, PPDAT9, PPDAT10, PPDAT11, PPDAT14, PPDAT16 ...

```diff
@@ base line 9, backup line 9 @@
      9  EXT BAS (BAS_COMMAND :IN,REAL :IN )
     10  DECL INT SUCCESS
-    17  DECL E6POS XTag4={X -612.686,Y -1589.39600,Z 2916.51807,A 84.5120,B -104.062,C 7.85700,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    18  DECL FDAT FTag4={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE}
-    19  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    20  DECL E6POS XTag3={X -570.159,Y -2455.64600,Z 462.298,A 90.7960,B -176.000,C -0.0550000,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    21  DECL FDAT FTag3={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE}
     17  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    23  DECL E6POS XTag1={X -570.159,Y -2469.59692,Z 262.786,A 90.7960,B -176.000,C -0.0560000,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    24  DECL FDAT FTag1={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE}
     18  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 0.0,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    26  DECL E6POS XTag2={X -570.159,Y -2466.10889,Z 312.664,A 90.7960,B -176.000,C -0.0560000,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    27  DECL FDAT FTag2={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE}
     19  DECL LDAT LCPDAT2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     20  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P0                      ",POINT2[] "P0                      ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT0                   ",CONT[] "                        ",CP_VEL[] "2.0    [...]
@@ base line 32, backup line 23 @@
     23  DECL E6POS XP10={X 1081.09485,Y -250.197342,Z 931.476,A -96.8303,B 37.9899406,C -15.7576666,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     24  DECL FDAT FP10={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    34  DECL E6POS XP30={X -602.469604,Y -2473.76245,Z 446.371094,A -89.4232254,B -2.67896390,C -179.996689,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    35  DECL FDAT FP30={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     25  DECL E6POS XAtPick3={X 1206.28552,Y -208.912048,Z 214.158249,A -91.4409,B -0.232809141,C 0.168289974,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     26  DECL FDAT FAtPick3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    38  DECL E6POS XP1={X -603.354553,Y -2477.18481,Z 667.120239,A -89.3294754,B 0.653617203,C -179.853607,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    39  DECL FDAT FP1={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    40  DECL LDAT LCPDAT3={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     27  DECL E6POS XP40={X 1206.28552,Y -208.912048,Z 630.625366,A -91.4409,B -0.232809082,C 0.168290034,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     28  DECL FDAT FP40={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    43  DECL E6POS XP50={X 1206.28552,Y -208.912048,Z 409.521729,A -91.4413757,B -0.232714087,C 0.168696448,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    44  DECL FDAT FP50={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    45  DECL E6POS XP60={X 671.407898,Y -378.268097,Z 2030.44653,A -89.8029327,B 7.84505653,C 24.4156590,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    46  DECL FDAT FP60={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    47  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     29  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    49  DECL E6POS XP70={X 1525.90320,Y -261.054626,Z 1246.12451,A 16.2779942,B 28.5338478,C 22.5772171,S 2,T 42,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    50  DECL FDAT FP70={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    51  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     30  DECL E6POS XP30ABOVEPICK={X 1206.28552,Y -208.912048,Z 298.869263,A -91.4409,B -0.232809111,C 0.168290,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     31  DECL FDAT FP30AbovePick={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    54  DECL E6POS XP2={X -599.756165,Y -2478.73,Z 369.150330,A -89.4027710,B -3.84103417,C 179.935089,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    55  DECL FDAT FP2={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    56  DECL PDAT PPDAT6={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    57  DECL E6POS XP3={X -599.698364,Y -2469.82422,Z 501.779144,A -89.4027710,B -3.84103417,C 179.935089,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    58  DECL FDAT FP3={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    59  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    60  DECL PDAT PPDAT0={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    61  DECL E6POS XP0={X 1206.28552,Y -208.912048,Z 573.307922,A -91.4409,B -0.232809082,C 0.168290049,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    62  DECL FDAT FP0={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    63  DECL LDAT LCPDAT4={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    64  DECL PDAT PPDAT8={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    65  DECL E6POS XP4={X 0.0,Y 0.0,Z 0.0,A 0.0,B 0.0,C 0.0,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    66  DECL FDAT FP4={TOOL_NO 0,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    67  DECL PDAT PPDAT9={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    68  DECL E6POS XP5={X 1206.28552,Y -208.912048,Z 1092.82214,A -91.4409,B -0.232809037,C 0.168290079,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    69  DECL FDAT FP5={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    70  DECL E6POS XP6={X 12.7359648,Y -130.494156,Z 3309.79932,A -58.5948639,B -68.7112122,C 63.6888771,S 3,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    71  DECL FDAT FP6={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    72  DECL PDAT PPDAT10={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    73  DECL E6POS XP7={X -1067.77161,Y -2105.70923,Z -1670.46326,A -142.262650,B 26.2927914,C -143.375824,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    74  DECL FDAT FP7={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
```
_23 more lines: see diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.dat.diff_

### `KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.src`

changed, integrator program: 7 code line(s) removed, 5 added; 86 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.src.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.src.diff)

Attributes: &COMMENT St1_PICK_GE4 -> &COMMENT 03-10-R1 RED RABBIT PICK

```diff
@@ base line 22, backup line 11 @@
     11  BAS (#INITMOV,0 )
     33  AC_pickUPCheck (1)
+    38  WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2)
     47  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
-    46  GRPg_Check(1, 1, FALSE, 1)
-    50  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254])
+    58  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO NUT_START=TRUE
     60  $BWDSTART=FALSE
     61  PDAT_ACT=PPDAT15
     62  FDAT_ACT=FP12
     63  BAS(#PTP_PARAMS,100)
-    59  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO NUT_STAR=TRUE
     64  PTP XP12
     67  $BWDSTART=FALSE
@@ base line 88, backup line 93 @@
     93  LIN XAtPick3
    103  GRPg_SetStateAndCheck(1, 2, 0.2, 1)
-   102  GRPg_Check(1, 2, FALSE, 1)
-   106  IF di004UseDryCycle==FALSE THEN
-   109  WAIT FOR ( $IN[253] ) AND ( $IN[254] )
-   112  $OUT[18]=TRUE
+   109  IF NOT di004UseDryCycle THEN
+   112  WAIT FOR ( di253PartPresent1 ) AND ( di254PartPresent2 )
+   118  do018Part1InGripper=TRUE
    120  ENDIF
    124  $BWDSTART=FALSE
```

### `KRC/R1/Program/StylePicks/Options/style1pick1opt2.dat`

changed, integrator program: 43 code line(s) removed, 0 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt2.dat.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt2.dat.diff)

Attributes: &ACCESS RVP2 -> &ACCESS RVO1; &REL 41 -> &REL 43; &COMMENT St1_PICK_GE4 -> &COMMENT 03-10-R1 PICK ST2

Data changes:

- removed 16 E6POS: XP0, XP1, XP2, XP3, XP4, XP5, XP6, XP7, XP30, XP50, XP60, XP70 ...
- removed 16 FDAT: FP0, FP1, FP2, FP3, FP4, FP5, FP6, FP7, FP30, FP50, FP60, FP70 ...
- removed 2 LDAT: LCPDAT3, LCPDAT4
- removed 9 PDAT: PPDAT0, PPDAT3, PPDAT5, PPDAT6, PPDAT7, PPDAT8, PPDAT9, PPDAT10, PPDAT11

Runtime values (left out of the code diff): LAST_BASIS: {POINT1[] "P8                      ",POI... -> {POINT1[] "P0                      ",POI...

```diff
@@ base line 9, backup line 9 @@
      9  EXT BAS (BAS_COMMAND :IN,REAL :IN )
     10  DECL INT SUCCESS
-    17  DECL E6POS XTag4={X -612.686,Y -1589.39600,Z 2916.51807,A 84.5120,B -104.062,C 7.85700,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    18  DECL FDAT FTag4={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE}
     17  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    20  DECL E6POS XTag3={X -570.159,Y -2455.64600,Z 462.298,A 90.7960,B -176.000,C -0.0550000,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    21  DECL FDAT FTag3={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE}
     18  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    23  DECL E6POS XTag1={X -570.159,Y -2469.59692,Z 262.786,A 90.7960,B -176.000,C -0.0560000,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    24  DECL FDAT FTag1={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE}
     19  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 0.0,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    26  DECL E6POS XTag2={X -570.159,Y -2466.10889,Z 312.664,A 90.7960,B -176.000,C -0.0560000,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    27  DECL FDAT FTag2={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE}
     20  DECL LDAT LCPDAT2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     22  DECL E6POS XP20={X 1206.28552,Y -208.912048,Z 714.012268,A -91.4409,B -0.232809097,C 0.168290034,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
@@ base line 32, backup line 24 @@
     24  DECL E6POS XP10={X 1164.28674,Y -250.197327,Z 931.476,A -96.8303,B 37.9899406,C -15.7576675,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     25  DECL FDAT FP10={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    34  DECL E6POS XP30={X -602.469604,Y -2473.76245,Z 446.371094,A -89.4232254,B -2.67896390,C -179.996689,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    35  DECL FDAT FP30={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     26  DECL E6POS XAtPick3={X 1206.51978,Y -207.283051,Z 215.779846,A -91.4152374,B 0.285709,C 0.179984391,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     27  DECL FDAT FAtPick3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    38  DECL E6POS XP1={X -603.354553,Y -2477.18481,Z 667.120239,A -89.3294754,B 0.653617203,C -179.853607,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    39  DECL FDAT FP1={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    40  DECL LDAT LCPDAT3={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     28  DECL E6POS XP40={X 1206.28552,Y -208.912048,Z 630.625366,A -91.4409,B -0.232809082,C 0.168290034,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     29  DECL FDAT FP40={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    43  DECL E6POS XP50={X 1206.28552,Y -208.912048,Z 409.521729,A -91.4413757,B -0.232714087,C 0.168696448,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    44  DECL FDAT FP50={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    45  DECL E6POS XP60={X 671.407898,Y -378.268097,Z 2030.44653,A -89.8029327,B 7.84505653,C 24.4156590,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    46  DECL FDAT FP60={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    47  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     30  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    49  DECL E6POS XP70={X 1525.90320,Y -261.054626,Z 1246.12451,A 16.2779942,B 28.5338478,C 22.5772171,S 2,T 42,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    50  DECL FDAT FP70={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    51  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     31  DECL E6POS XP30ABOVEPICK={X 1206.28552,Y -208.912048,Z 298.869263,A -91.4409,B -0.232809111,C 0.168290,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     32  DECL FDAT FP30AbovePick={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    54  DECL E6POS XP2={X -599.756165,Y -2478.73,Z 369.150330,A -89.4027710,B -3.84103417,C 179.935089,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    55  DECL FDAT FP2={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    56  DECL PDAT PPDAT6={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    57  DECL E6POS XP3={X -599.698364,Y -2469.82422,Z 501.779144,A -89.4027710,B -3.84103417,C 179.935089,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    58  DECL FDAT FP3={TOOL_NO 7,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    59  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    60  DECL PDAT PPDAT0={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    61  DECL E6POS XP0={X 1206.28552,Y -208.912048,Z 573.307922,A -91.4409,B -0.232809082,C 0.168290049,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    62  DECL FDAT FP0={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    63  DECL LDAT LCPDAT4={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    64  DECL PDAT PPDAT8={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    65  DECL E6POS XP4={X 0.0,Y 0.0,Z 0.0,A 0.0,B 0.0,C 0.0,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    66  DECL FDAT FP4={TOOL_NO 0,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    67  DECL PDAT PPDAT9={VEL 100.000,ACC 100.000,APO_DIST 1000.00,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    68  DECL E6POS XP5={X 1206.28552,Y -208.912048,Z 1092.82214,A -91.4409,B -0.232809037,C 0.168290079,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    69  DECL FDAT FP5={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    70  DECL E6POS XP6={X 12.7359648,Y -130.494156,Z 3309.79932,A -58.5948639,B -68.7112122,C 63.6888771,S 3,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    71  DECL FDAT FP6={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    72  DECL PDAT PPDAT10={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    73  DECL E6POS XP7={X -1067.77161,Y -2105.70923,Z -1670.46326,A -142.262650,B 26.2927914,C -143.375824,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    74  DECL FDAT FP7={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
```
_3 more lines: see diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt2.dat.diff_

### `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`

changed, integrator program: 9 code line(s) removed, 7 added; 102 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt2.src.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt2.src.diff)

Attributes: &ACCESS RVP2 -> &ACCESS RVO1; &REL 41 -> &REL 43; &COMMENT St1_PICK_GE4 -> &COMMENT 03-10-R1 PICK ST2

```diff
@@ base line 22, backup line 11 @@
     11  BAS (#INITMOV,0 )
     34  AC_pickUPCheck (2)
+    39  WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2)
     48  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
-    46  GRPg_Check(1, 1, FALSE, 1)
-    50  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254])
+    59  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO NUT_START=TRUE
     61  $BWDSTART=FALSE
     62  PDAT_ACT=PPDAT1
     63  FDAT_ACT=FP10
     64  BAS(#PTP_PARAMS,100)
-    59  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO NUT_STAR=TRUE
     65  PTP XP10 C_DIS
     68  $BWDSTART=FALSE
@@ base line 81, backup line 87 @@
     87  LIN XAtPick3
     97  GRPg_SetStateAndCheck(1, 2, 0.2, 1)
-    95  GRPg_Check(1, 2, FALSE, 1)
-    99  IF di004UseDryCycle==FALSE THEN
-   102  WAIT FOR ( $IN[253] ) AND ( $IN[254] )
-   105  $OUT[18]=TRUE
+   103  IF NOT di004UseDryCycle THEN
+   106  WAIT FOR ( di253PartPresent1 ) AND ( di254PartPresent2 )
+   112  do018Part1InGripper=TRUE
    114  ENDIF
    119  $BWDSTART=FALSE
@@ base line 114, backup line 121 @@
    121  FDAT_ACT=FP40
    122  BAS(#CP_PARAMS,2)
-   116  LIN XP40
+   123  LIN XP40 C_DIS C_DIS
    126  $BWDSTART=FALSE
    127  PDAT_ACT=PPDAT12
    128  FDAT_ACT=FP8
    129  BAS(#PTP_PARAMS,100)
-   123  PTP XP8
+   130  PTP XP8 C_DIS
    138  AC_pickUP (2,True)
    140  END
```

### `KRC/R1/Program/Styles/optiones/style1opt1.src`

changed, integrator program: 14 code line(s) removed, 15 added; 92 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Styles/optiones/style1opt1.src.diff](diffs/KRC/R1/Program/Styles/optiones/style1opt1.src.diff)

Attributes: &ACCESS RVP1 -> &ACCESS RVO1; &COMMENT GE4_002 -> &COMMENT 03-10-R1 PRODUCTION CYCLE

```diff
@@ base line 4, backup line 4 @@
      4  DEF Style1Opt1 ( )
+    11  DECL INT nPickStation
+    20  nPickStation=0
     22  IF di065PickupMachine1 AND NOT di066PickupMachine2 THEN
+    23  nPickStation=1
+    24  ELSE
+    26  IF di066PickupMachine2 AND NOT di065PickupMachine1 THEN
+    27  nPickStation=2
+    28  ENDIF
+    29  ENDIF
+    31  IF nPickStation<>0 THEN
+    33  IF nPickStation==1 THEN
     34  style1pick1opt1()
+    35  ELSE
+    36  style1pick1opt2()
+    37  ENDIF
+    40  IF nPickStation==1 THEN
     41  style1app1opt1A()
     42  Style1App1Opt2A()
     43  Style1App1Opt3A()
-    28  style1app2opt1()
-    29  IF bScrapGE4==TRUE THEN
-    30  RejectGE4()
     44  ELSE
-    32  style1app2opt2()
-    33  IF bScrapGE4==TRUE THEN
-    34  RejectGE4()
-    35  ELSE
-    36  Style1Drop1Opt1()
-    37  ENDIF
-    38  ENDIF
-    40  ELSE
-    42  IF di066PickupMachine2 AND NOT di065PickupMachine1 THEN
-    44  style1pick1opt2()
     45  style1app1opt1B()
     46  Style1App1Opt2B()
     47  Style1App1Opt3B()
+    48  ENDIF
     51  style1app2opt1()
     52  IF bScrapGE4==TRUE THEN
@@ base line 60, backup line 67 @@
     67  ENDIF
     68  ENDIF
-    62  ENDIF
     71  PARTPRESENT1=FALSE
     72  PARTPRESENT2=FALSE
```

### `KRC/R1/Program/Styles/style_1.dat`

changed, integrator program: 7 code line(s) removed, 0 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Styles/style_1.dat.diff](diffs/KRC/R1/Program/Styles/style_1.dat.diff)

Attributes: &COMMENT GE4_002 -> &COMMENT 03-10-R1 STYLE 1

Data changes:

- removed 6 PDAT: PPDAT1, PPDAT2, PPDAT3, PPDAT4, PPDAT5, PPDAT6
- removed 1 SIGNAL: di141RedRabbitFail

```diff
@@ base line 7, backup line 7 @@
      7  EXT BAS (BAS_COMMAND :IN,REAL :IN )
      8  DECL INT SUCCESS
-    13  SIGNAL di141RedRabbitFail $IN[141]
     15  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "POUNCE                  ",POINT2[] "POUNCE                  ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT6                   ",CONT[] "                        ",CP_VEL[] "2.0    [...]
-    17  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    18  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    19  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    20  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    21  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    22  DECL PDAT PPDAT6={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
     16  ENDDAT
```

### `KRC/R1/Program/Utilities/RejectGE4.dat`

changed, integrator program: 32 code line(s) removed, 0 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Utilities/RejectGE4.dat.diff](diffs/KRC/R1/Program/Utilities/RejectGE4.dat.diff)

Attributes: &ACCESS RVO2 -> &ACCESS RVO1; +&COMMENT 03-10-R1 REJECT

Data changes:

- removed 11 E6POS: XP11, XP12, XP20, XP21, XP22, XP26, XP30, XPABOVESCRAP, XPSCRAPREORIENT, XReject_Drop, XSCRAP_POUNCE
- removed 11 FDAT: FP11, FP12, FP20, FP21, FP22, FP26, FP30, FPAboveScrap, FPScrapReorient, FReject_Drop, FScrap_Pounce
- removed 10 PDAT: PPDAT1, PPDAT2, PPDAT3, PPDAT4, PPDAT5, PPDAT6, PPDAT7, PPDAT8, PPDAT28, PPDAT31

```diff
@@ base line 7, backup line 8 @@
      8  EXT BAS (BAS_COMMAND :IN,REAL :IN )
      9  DECL INT SUCCESS
-    15  DECL E6POS XPSCRAPREORIENT={X 2153.09570,Y 1755.13818,Z 2068.92651,A -8.10456848,B -7.40806341,C -132.602493,S 2,T 43,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     16  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P27                     ",POINT2[] "P27                     ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT32                  ",CONT[] "C_DIS                   ",CP_VEL[] "2      [...]
-    17  DECL FDAT FPScrapReorient={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    18  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    19  DECL E6POS XPABOVESCRAP={X 2375.58740,Y 1146.28662,Z 2113.63257,A -15.2346992,B -12.9237299,C -133.089966,S 2,T 11,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    20  DECL FDAT FPAboveScrap={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    21  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    22  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    23  DECL E6POS XSCRAP_POUNCE={X 1988.17371,Y 1131.17041,Z 1238.16,A -56.3896446,B 5.16084337,C -175.312164,S 2,T 43,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    24  DECL FDAT FScrap_Pounce={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    25  DECL E6POS XReject_Drop={X 2069.87720,Y 1447.17029,Z 200.832,A -55.7535553,B 0.336941630,C -179.384842,S 2,T 43,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    26  DECL FDAT FReject_Drop={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    27  DECL PDAT PPDAT4={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    28  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
     17  DECL E6POS XP10={X -724.403137,Y -1811.34314,Z 1367.20557,A -104.758530,B 0.614156485,C 179.947769,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     18  DECL FDAT FP10={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    31  DECL PDAT PPDAT6={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    32  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    33  DECL E6POS XP11={X 1625.17554,Y 419.790771,Z 1424.78357,A -47.9713402,B 1.16016603,C -173.202026,S 2,T 43,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    34  DECL FDAT FP11={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    35  DECL E6POS XP12={X -21.1073933,Y 977.088257,Z 1822.06055,A -57.9586,B 86.2354584,C -137.216766,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    36  DECL FDAT FP12={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    37  DECL PDAT PPDAT8={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000,EXAX_IGN 0}
     19  DECL PDAT PL={VEL 100.000,ACC 100.000,APO_DIST 10.0000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    39  DECL E6POS XP20={X 2719.51270,Y 311.994171,Z 1611.79553,A -0.154689506,B 3.52242422,C 177.449234,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    40  DECL FDAT FP20={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    41  DECL E6POS XP30={X 3228.21240,Y 452.756042,Z 1483.90466,A 2.29265,B 2.86626720,C 177.589737,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    42  DECL FDAT FP30={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    43  DECL E6POS XP21={X 2719.51270,Y 311.994171,Z 1611.79553,A -0.154689506,B 3.52242422,C 177.449234,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    44  DECL FDAT FP21={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    45  DECL PDAT PPDAT28={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    46  DECL E6POS XP22={X -725.920410,Y -1758.69482,Z 1448.59143,A -104.766548,B 0.615574777,C 179.948090,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    47  DECL FDAT FP22={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     20  DECL LDAT LCPDAT0={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     21  DECL E6POS XP23={X -703.896545,Y -1395.42871,Z 344.753052,A -135.022919,B 21.6832848,C -1.44161212,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
@@ base line 55, backup line 27 @@
     27  DECL E6POS XP25={X -518.438721,Y -800.197693,Z 3339.05908,A -175.274445,B -73.1114883,C 13.2109089,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     28  DECL FDAT FP25={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    57  DECL PDAT PPDAT31={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    58  DECL E6POS XP26={X 370.852905,Y -298.257416,Z 2804.38916,A -147.361786,B -35.6047363,C 79.4075775,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    59  DECL FDAT FP26={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     29  DECL E6POS XP27={X -1209.28430,Y -1491.03662,Z 1129.57971,A -146.959381,B 2.43560171,C 8.39888477,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     30  DECL FDAT FP27={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
```

### `KRC/R1/Program/Utilities/RejectGE4.src`

changed, integrator program: 5 code line(s) removed, 5 added; 41 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Utilities/RejectGE4.src.diff](diffs/KRC/R1/Program/Utilities/RejectGE4.src.diff)

Attributes: &ACCESS RVO2 -> &ACCESS RVO1; +&COMMENT 03-10-R1 REJECT

```diff
@@ base line 8, backup line 9 @@
      9  INTERRUPT ON 3
     10  BAS (#INITMOV,0 )
-    17  $OUT[106]=TRUE
+    30  do106PartRejected=TRUE
     34  $BWDSTART=FALSE
     35  PDAT_ACT=PL
@@ base line 23, backup line 37 @@
     37  BAS(#PTP_PARAMS,100)
     38  PTP XP10
+    44  TRIGGER WHEN DISTANCE=1 DELAY=0 DO do070ApplicationClear1=TRUE
     46  $BWDSTART=FALSE
     47  LDAT_ACT=LCPDAT0
@@ base line 33, backup line 50 @@
     50  LIN XP23
     60  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
-    46  GRPg_Check(1, 1, FALSE, 1)
-    49  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254] )
+    64  WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2 )
     69  $BWDSTART=FALSE
     70  PDAT_ACT=PPDAT29
@@ base line 56, backup line 72 @@
     72  BAS(#PTP_PARAMS,100)
     73  PTP XP24
-    60  $OUT[18]=FALSE
+    77  do018Part1InGripper=FALSE
     82  $BWDSTART=FALSE
     83  PDAT_ACT=PPDAT32
@@ base line 83, backup line 101 @@
    101  $H_POS=XHOME
    102  PTP XHOME
-    88  $OUT[106]=FALSE
+   110  do106PartRejected=FALSE
    114  bScrapCantrail=FALSE
    115  bscrapGE4=FALSE
```

### `KRC/R1/Program/Utilities/hometorepair.dat`

changed, integrator program: 0 code line(s) removed, 18 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Utilities/hometorepair.dat.diff](diffs/KRC/R1/Program/Utilities/hometorepair.dat.diff)

Attributes: -&ACCESS RVP14; -&REL 3; +&ACCESS RVP3; +&REL 12; +&COMMENT 03-10-R1 HOME TO REPAIR

Data changes:

- added 6 E6POS: XHomePos, XP0, XP1, XP2, XP3, XP4
- added 6 FDAT: FHomePos, FP0, FP1, FP2, FP3, FP4
- added 2 LDAT: LCPDAT0, LCPDAT1
- added 4 PDAT: PPDAT0, PPDAT1, PPDAT2, PPDAT3

Runtime values (left out of the code diff): LAST_BASIS: {POINT1[] "P0                      ",POI... -> {POINT1[] "P4                      ",POI...

```diff
@@ base line 6, backup line 7 @@
      7  EXT BAS (BAS_COMMAND :IN,REAL :IN )
      8  DECL INT SUCCESS
+    16  DECL PDAT PPDAT0={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    17  DECL E6POS XHomePos={X 874.811523,Y -100.694267,Z 2352.82349,A -4.40716410,B 2.42973685,C 0.669219,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    18  DECL FDAT FHomePos={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    19  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    20  DECL E6POS XP0={X 578.283081,Y -208.830032,Z 2497.68457,A -20.7746563,B 27.3249149,C -50.2284737,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    21  DECL FDAT FP0={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    22  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    23  DECL E6POS XP1={X -489.036224,Y -839.989319,Z 2474.99487,A -123.849350,B 35.8758926,C -51.4425964,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    24  DECL FDAT FP1={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    25  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    26  DECL E6POS XP2={X -551.392334,Y -958.296631,Z 832.440857,A 153.051483,B 84.2137,C -117.695351,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    27  DECL FDAT FP2={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    28  DECL LDAT LCPDAT0={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    29  DECL E6POS XP3={X -618.757446,Y -1118.39392,Z 667.271301,A 93.8276825,B 87.4137192,C -177.018982,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    30  DECL FDAT FP3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    31  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    32  DECL E6POS XP4={X -754.263306,Y -752.360107,Z -58.2259216,A 93.9359894,B 87.4085,C -176.908646,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    33  DECL FDAT FP4={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     34  ENDDAT
```

### `KRC/R1/Program/Utilities/hometorepair.src`

changed, integrator program: 0 code line(s) removed, 15 added; 18 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Utilities/hometorepair.src.diff](diffs/KRC/R1/Program/Utilities/hometorepair.src.diff)

Attributes: -&ACCESS RVP14; -&REL 3; +&ACCESS RVP3; +&REL 12; +&COMMENT 03-10-R1 HOME TO REPAIR

```diff
@@ base line 21, backup line 34 @@
     34  $H_POS=XHOME
     35  PTP XHOME
+    39  $BWDSTART=FALSE
+    40  PDAT_ACT=PPDAT1
+    41  FDAT_ACT=FP0
+    42  BAS(#PTP_PARAMS,100)
+    43  PTP XP0
+    46  $BWDSTART=FALSE
+    47  PDAT_ACT=PPDAT2
+    48  FDAT_ACT=FP1
+    49  BAS(#PTP_PARAMS,100)
+    50  PTP XP1
+    53  $BWDSTART=FALSE
+    54  PDAT_ACT=PPDAT3
+    55  FDAT_ACT=FP2
+    56  BAS(#PTP_PARAMS,80)
+    57  PTP XP2 C_DIS
     60  $BWDSTART = FALSE
     61  PDAT_ACT=PREPAIR
```

### `KRC/R1/Program/Utilities/repairtohome.dat`

changed, integrator program: 1 code line(s) removed, 11 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Utilities/repairtohome.dat.diff](diffs/KRC/R1/Program/Utilities/repairtohome.dat.diff)

Attributes: -&ACCESS RVP15; -&REL 3; +&ACCESS RVP4; +&REL 10; +&COMMENT 03-10-R1 REPAIR TO HOME

Data changes:

- added 1 BASIS_SUGG_T: LAST_BASIS
- added 1 DEFDAT: repairtohome
- added 3 E6POS: XP0, XP1, XP2
- added 3 FDAT: FP0, FP1, FP2
- added 3 PDAT: PPDAT0, PPDAT1, PPDAT2
- removed 1 DEFDAT: RepairToHome

```diff
@@ base line 3, backup line 4 @@
-     3  DEFDAT RepairToHome
+     4  DEFDAT repairtohome
      7  EXT BAS (BAS_COMMAND :IN,REAL :IN )
      8  DECL INT SUCCESS
+    15  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P2                      ",POINT2[] "P2                      ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT2                   ",CONT[] "                        ",CP_VEL[] "2.0    [...]
+    16  DECL PDAT PPDAT0={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    17  DECL E6POS XP0={X 578.283081,Y -208.830032,Z 2497.68457,A -20.7746563,B 27.3249149,C -50.2284737,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    18  DECL FDAT FP0={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    19  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    20  DECL E6POS XP1={X -489.036224,Y -839.989319,Z 2474.99487,A -123.849350,B 35.8758926,C -51.4425964,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    21  DECL FDAT FP1={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
+    22  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    23  DECL E6POS XP2={X -551.392334,Y -958.296631,Z 832.440857,A 153.051483,B 84.2137,C -117.695351,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    24  DECL FDAT FP2={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     25  ENDDAT
```

### `KRC/R1/Program/Utilities/repairtohome.src`

changed, integrator program: 0 code line(s) removed, 15 added; 15 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Utilities/repairtohome.src.diff](diffs/KRC/R1/Program/Utilities/repairtohome.src.diff)

Attributes: -&ACCESS RVP15; -&REL 3; +&ACCESS RVP4; +&REL 10; +&COMMENT 03-10-R1 REPAIR TO HOME

```diff
@@ base line 20, backup line 30 @@
     30  BAS (#PTP_PARAMS,100 )
     31  PTP XREPAIR
+    35  $BWDSTART=FALSE
+    36  PDAT_ACT=PPDAT2
+    37  FDAT_ACT=FP2
+    38  BAS(#PTP_PARAMS,80)
+    39  PTP XP2 C_DIS
+    42  $BWDSTART=FALSE
+    43  PDAT_ACT=PPDAT1
+    44  FDAT_ACT=FP1
+    45  BAS(#PTP_PARAMS,100)
+    46  PTP XP1
+    49  $BWDSTART=FALSE
+    50  PDAT_ACT=PPDAT0
+    51  FDAT_ACT=FP0
+    52  BAS(#PTP_PARAMS,100)
+    53  PTP XP0
     56  $BWDSTART = FALSE
     57  PDAT_ACT=PDEFAULT
```

### `KRC/R1/Program/masref_user.dat`

changed, integrator program: 67 code line(s) removed, 0 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/masref_user.dat.diff](diffs/KRC/R1/Program/masref_user.dat.diff)

Attributes: &ACCESS RVO7 -> &ACCESS RVO4; &COMMENT Mastering Reference User Program -> &COMMENT 03-10-R1 MASTERING REF

Data changes:

- removed 22 E6POS: XP0, XP1, XP2, XP3, XP4, XP5, XP6, XP8, XP11, XP12, XP13, XP14 ...
- removed 22 FDAT: FP0, FP1, FP2, FP3, FP4, FP5, FP6, FP8, FP11, FP12, FP13, FP14 ...
- removed 11 LDAT: LCPDAT0, LCPDAT1, LCPDAT2, LCPDAT3, LCPDAT4, LCPDAT5, LCPDAT9, LCPDAT10, LCPDAT11, LCPDAT12, LCPDAT13
- removed 12 PDAT: PPDAT1, PPDAT2, PPDAT3, PPDAT6, PPDAT7, PPDAT8, PPDAT9, PPDAT10, PPDAT11, PPDAT12, PPDAT13, PPDAT14

```diff
@@ base line 5, backup line 5 @@
      5  DEFDAT masref_user
      8  EXT BAS (BAS_COMMAND :IN,REAL :IN )
-    15  DECL E6POS XP1={X 771.684875,Y 1042.88721,Z 737.000916,A -148.484344,B -76.1350861,C -33.4368,S 2,T 43,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     15  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P0                      ",POINT2[] "P0                      ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT19                  ",CONT[] "                        ",CP_VEL[] "2.0    [...]
-    17  DECL FDAT FP1={TOOL_NO 1,BASE_NO 4,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    18  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    19  DECL E6POS XP2={X -152.238663,Y 615.762451,Z -392.502960,A 167.793732,B 0.890011191,C 1.12833,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    20  DECL FDAT FP2={TOOL_NO 1,BASE_NO 4,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    21  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    22  DECL E6POS XP3={X -80.0698090,Y 676.307739,Z -1414.60132,A 167.793716,B 0.889924049,C 1.12850881,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    23  DECL FDAT FP3={TOOL_NO 1,BASE_NO 4,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    24  DECL LDAT LCPDAT1={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    25  DECL E6POS XPREFSWITCH={X -486.106415,Y 1092.98462,Z -486.351685,A -106.778526,B 2.95674634,C -171.498047,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    26  DECL FDAT FPRefSwitch={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    27  DECL LDAT LCPDAT2={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    28  DECL E6POS XP4={X -80.0698090,Y 676.307739,Z -1414.60132,A 167.793716,B 0.889924049,C 1.12850881,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    29  DECL FDAT FP4={TOOL_NO 1,BASE_NO 4,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    30  DECL LDAT LCPDAT3={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    31  DECL E6POS XP5={X -152.238663,Y 615.762451,Z -392.502960,A 167.793732,B 0.890011191,C 1.12833,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    32  DECL FDAT FP5={TOOL_NO 1,BASE_NO 4,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    33  DECL LDAT LCPDAT4={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    34  DECL E6POS XP6={X 771.684631,Y 1042.88708,Z 737.001,A -148.484344,B -76.1350784,C -33.4367905,S 2,T 43,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    35  DECL FDAT FP6={TOOL_NO 1,BASE_NO 4,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    36  DECL PDAT PPDAT3={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     16  DECL E6POS XHOMEPOS={X 874.811523,Y -100.694267,Z 2352.82349,A -4.40716410,B 2.42973685,C 0.669219,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     17  DECL FDAT FHomePos={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
@@ base line 41, backup line 20 @@
     20  DECL FDAT FP7={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     21  DECL PDAT PPDAT5={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    43  DECL E6POS XP8={X -433.243591,Y 649.095947,Z 704.272461,A -110.291306,B 5.96638775,C -179.082123,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    44  DECL FDAT FP8={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    45  DECL LDAT LCPDAT5={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     22  DECL LDAT LCPDAT6={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     23  DECL E6POS XP9={X -754.263306,Y -752.360107,Z -58.2259216,A 93.9359894,B 87.4085,C -176.908646,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
@@ base line 51, backup line 27 @@
     27  DECL FDAT FP10={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     28  DECL LDAT LCPDAT8={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    53  DECL E6POS XP11={X -70.5918045,Y 521.023560,Z -1469.24475,A 167.536987,B 3.44113851,C 8.19418,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    54  DECL FDAT FP11={TOOL_NO 1,BASE_NO 4,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    55  DECL LDAT LCPDAT9={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    56  DECL E6POS XP12={X -70.5918,Y 521.023560,Z -873.411072,A 167.536987,B 3.44113851,C 8.19418,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    57  DECL FDAT FP12={TOOL_NO 1,BASE_NO 4,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    58  DECL LDAT LCPDAT10={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    59  DECL E6POS XP13={X -317.774414,Y 768.403870,Z -235.033524,A 167.615891,B 4.67066622,C 9.54216766,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    60  DECL FDAT FP13={TOOL_NO 1,BASE_NO 4,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    61  DECL LDAT LCPDAT11={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    62  DECL LDAT LCPDAT0={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    63  DECL E6POS XP0={X -503.651337,Y 1034.79419,Z -489.490936,A -106.778526,B 2.95674658,C -171.498047,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    64  DECL FDAT FP0={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    65  DECL LDAT LCPDAT12={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    66  DECL E6POS XP14={X -526.497131,Y 987.852051,Z 368.179169,A -102.828995,B -1.56158221,C -171.254395,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    67  DECL FDAT FP14={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    68  DECL LDAT LCPDAT13={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    69  DECL E6POS XP15={X -336.148285,Y 665.637207,Z 410.031342,A -103.188179,B -1.53990638,C -171.960983,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    70  DECL FDAT FP15={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    71  DECL E6POS XP16={X -384.212372,Y 1013.49115,Z 1497.91638,A -123.715569,B 42.0906258,C 148.746750,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
-    72  DECL FDAT FP16={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    73  DECL PDAT PPDAT6={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    74  DECL E6POS XPHOME={X 811.073303,Y 379.504303,Z 907.073425,A 160.176132,B -57.3357124,C -11.5811968,S 2,T 35,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
```
_23 more lines: see diffs/KRC/R1/Program/masref_user.dat.diff_

### `KRC/R1/System/$config.dat`

changed, integrator program: 30 code line(s) removed, 18 added; 62 comment/blank line change(s). Full diff: [diffs/KRC/R1/System/$config.dat.diff](diffs/KRC/R1/System/$config.dat.diff)

Attributes: &PARAM DISKPATH = KRC:\R1\System -> &PARAM DISKPATH = SYSTEM

Data changes:

- LOAD_A3_DATA (LOAD) re-taught: moved 0.0 mm
- CL_GUN_WELD_MAX (INT): 76000 -> 73000
- CL_GUN_WELD_MIN (INT): 65000 -> 69000
- CL_PIN_WELD_MAX (INT): 13500 -> 12200
- CL_PIN_WELD_MIN (INT): 10000 -> 11000
- added 2 BOOL: CL_WeldFault, NUT_START
- added 7 INT: CL_GUN_CLOSE_TIMEOUT, CL_GUN_IN_WINDOW_TIME, CL_GUN_PRESS_BASE, CL_GUN_PRESS_REST, CL_GUN_PRESS_WELD, CL_WELD_COMPLETE_TIMEOUT, CL_WELD_PROGRAM
- added 3 SIGNAL: CL_BeaconBit3001, CL_BeaconBit3008, CL_BeaconBit3024
- removed 19 BOOL: bscrapGE4_1, bscrapGE4_2, bscrapGE4_3, bscrapGE4_4, bscrapGE4_5, CL_ALL_HOME, CL_CENTERLINE_READY, CL_GUN_WORK_REQ, CL_WeldPressureOK, NUT_STAR, NUT_WELD_RETRY, PARTPRESENT4 ...
- removed 3 INT: CL_STEP, NUT_RETRY, Part_Style
- removed 2 SIGNAL: CL_ALL_HOME_PLC, NUT_PRESENT1

Runtime values (left out of the code diff): CL_GunStrokePositionLPT: 139785 -> 139760; CL_WeldPinPosition: 27330 -> 27367; STOPM_FLAG: FALSE -> TRUE

```diff
@@ base line 267, backup line 267 @@
    267  TOOL_NAME[16,]=" "
    269  DECL LOAD LOAD_DATA[16]
-   270  LOAD_DATA[1]={M 210.000,CM {X 270.000,Y 0.0,Z 240.000,A 0.0,B 0.0,C 0.0},J {X 105.000,Y 105.000,Z 105.000}}
+   271  LOAD_DATA[1]={M 67.2787094,CM {X -2.62049794,Y 17.9348812,Z 219.182,A -90.0034943,B -0.200046,C 0.0651830},J {X 5.25000,Y 5.25000,Z 5.25000}}
    272  LOAD_DATA[2]={M 129.297,CM {X 38.8040,Y -94.4510,Z 136.873,A 89.7770,B -0.721000,C 0.991000},J {X 5.25000,Y 5.57200,Z 7.65800}}
    273  LOAD_DATA[3]={M 129.297,CM {X 38.8040,Y -94.4510,Z 136.873,A 89.7770,B -0.721000,C 0.991000},J {X 5.25000,Y 5.57200,Z 7.65800}}
@@ base line 305, backup line 306 @@
    306  DECL LOAD LOAD_A1_DATA={M -1.00000,CM {X 0.0,Y 0.0,Z 0.0,A 0.0,B 0.0,C 0.0},J {X 0.0,Y 0.0,Z 0.0}}
    307  DECL LOAD LOAD_A2_DATA={M -1.00000,CM {X 0.0,Y 0.0,Z 0.0,A 0.0,B 0.0,C 0.0},J {X 0.0,Y 0.0,Z 0.0}}
-   307  DECL LOAD LOAD_A3_DATA={M 30.0000,CM {X -400.000,Y 0.0,Z -1315.00,A 0.0,B 0.0,C 0.0},J {X 10.0000,Y 10.0000,Z 10.0000}}
+   308  DECL LOAD LOAD_A3_DATA={M 50.0000,CM {X -400.000,Y 0.0,Z -1315.00,A 0.0,B 0.0,C 0.0},J {X 10.0000,Y 10.0000,Z 10.0000}}
    310  INT MAX_BASE=32
    311  DECL FRAME BASE_DATA[32]
@@ base line 757, backup line 761 @@
    761  BOOL PARTPRESENT2=FALSE
    762  BOOL PARTPRESENT3=FALSE
-   759  BOOL PARTPRESENT4=FALSE
-   760  BOOL PARTPRESENT5=FALSE
-   761  BOOL REDRABBIT
-   762  BOOL REDRABBIT1=FALSE
-   763  BOOL REDRABBIT2=FALSE
-   764  BOOL REDRABBIT3=FALSE
-   765  BOOL REDRABBIT4=FALSE
-   766  BOOL REDRABBIT5=FALSE
-   767  BOOL bscrapGE4_1=FALSE
-   768  BOOL bscrapGE4_2=FALSE
-   769  BOOL bscrapGE4_3=FALSE
-   770  BOOL bscrapGE4_4=FALSE
-   771  BOOL bscrapGE4_5=FALSE
-   772  SIGNAL NUT_PRESENT1 $IN[227]
-   776  INT Part_Style=1
    770  DECL CHAR LDDPLUGIN_VARNAME[19]
    771  LDDPLUGIN_VARNAME[]="LDDPLUGIN_ACTIVATED"
@@ base line 811, backup line 817 @@
    817  SIGNAL CL_PIN_BYTE0 $IN[591] TO $IN[598]
    818  SIGNAL CL_PIN_BYTE1 $IN[599] TO $IN[606]
-   815  BOOL CL_WeldPressureOK=FALSE
-   821  DECL INT CL_STEP=0
-   823  DECL INT CL_PIN_WELD_MIN=10000
-   824  DECL INT CL_PIN_WELD_MAX=13500
-   825  DECL INT CL_GUN_WELD_MIN=65000
-   826  DECL INT CL_GUN_WELD_MAX=76000
-   828  DECL BOOL CL_GUN_WORK_REQ=FALSE
-   829  DECL BOOL CL_CENTERLINE_READY=FALSE
-   830  DECL BOOL CL_ALL_HOME=FALSE
-   832  SIGNAL CL_ALL_HOME_PLC $OUT[4000]
-   837  DECL BOOL NUT_STAR=FALSE
+   825  SIGNAL CL_BeaconBit3001 $OUT[3001]
+   826  SIGNAL CL_BeaconBit3008 $OUT[3008]
+   827  SIGNAL CL_BeaconBit3024 $OUT[3024]
+   836  DECL INT CL_PIN_WELD_MIN=11000
+   837  DECL INT CL_PIN_WELD_MAX=12200
+   841  DECL INT CL_GUN_WELD_MIN=69000
+   842  DECL INT CL_GUN_WELD_MAX=73000
+   845  DECL INT CL_GUN_CLOSE_TIMEOUT=1000
+   846  DECL INT CL_GUN_IN_WINDOW_TIME=150
+   851  DECL INT CL_GUN_PRESS_BASE=405
+   852  DECL INT CL_GUN_PRESS_WELD=1820
+   853  DECL INT CL_GUN_PRESS_REST=39425
```
_16 more lines: see diffs/KRC/R1/System/$config.dat.diff_

### `KRC/R1/System/sps.sub`

changed, integrator program: 8 code line(s) removed, 75 added; 122 comment/blank line change(s). Full diff: [diffs/KRC/R1/System/sps.sub.diff](diffs/KRC/R1/System/sps.sub.diff)

Attributes: &COMMENT PLC on control -> &COMMENT 03-10-R1 SUBMIT SPS

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
@@ base line 51, backup line 93 @@
     93  ENDIF
     97  GRPg_ChkSetStatePLC()
-    62  AutomationCore_BKG ( )
    122  CL_GunStrokePositionLPT=(CL_LPT_BYTE1*65536)+(CL_LPT_BYTE2*256)+CL_LPT_BYTE3
    126  CL_WeldPinPosition=(CL_PIN_BYTE0*256)+CL_PIN_BYTE1
+   130  CL_ClampOpen=di466PartClampOpen
+   131  IF bPinCheck THEN
+   132  CL_PinRetracted=(CL_WeldPinPosition>=nPinRetractMin) AND (CL_WeldPinPosition<=nPinRetractMax)
+   133  ELSE
+   134  CL_PinRetracted=TRUE
+   135  ENDIF
    138  SV0500_FLOW =( SV0500_BYTE0*256)+SV0500_BYTE1
    145  nWaterFlow = SV0500_FLOW / 4
@@ base line 91, backup line 152 @@
    152  ENDIF
    154  CL_WaterOk = dipw1_WaterOk
-    97  IF $OUT[478] THEN
-    98  $OUT[3008] = TRUE
-    99  $OUT[3024] = TRUE
+   162  dopw1_LowLevel = CL_WeldFault OR dipw1_Fault
+   163  dopw1_LevelOk = NOT (CL_WeldFault OR dipw1_Fault)
+   171  IF dopw1_LowLevel THEN
+   172  CL_BeaconBit3008 = TRUE
```
_42 more lines: see diffs/KRC/R1/System/sps.sub.diff_

### `KRC/R1/cell.src`

changed, integrator program: 1 code line(s) removed, 1 added; 49 comment/blank line change(s). Full diff: [diffs/KRC/R1/cell.src.diff](diffs/KRC/R1/cell.src.diff)

Attributes: &COMMENT HANDLER on external automatic -> &COMMENT 03-10-R1 AUTO EXTERNAL MAIN

```diff
@@ base line 49, backup line 82 @@
     82  HomeCheck( )
     83  HomeToRepair( )
-    52  WAIT FOR ( $IN[8] )
+    86  WAIT FOR ( di008ReturnFromRepair )
     88  RepairToHome( )
     89  ENDIF
```

### `C/KRC/Roboter/Config/User/Common/PNIOIM4Data.dat`

changed, controller configuration: 1 code line(s) removed, 1 added; 0 comment/blank line change(s). Full diff: [diffs/C/KRC/Roboter/Config/User/Common/PNIOIM4Data.dat.diff](diffs/C/KRC/Roboter/Config/User/Common/PNIOIM4Data.dat.diff)

```diff
@@ base line 1, backup line 1 @@
-     1  zUªû
+     1  zUªxýkð
```

### `KRC/R1/System/ir_stopm.src`

changed, KUKA system / vendor package: 2 code line(s) removed, 0 added; 5 comment/blank line change(s). Full diff: [diffs/KRC/R1/System/ir_stopm.src.diff](diffs/KRC/R1/System/ir_stopm.src.diff)

```diff
@@ base line 23, backup line 23 @@
     23  If ($STOPMESS==TRUE) THEN
     24  BRAKE
-    28  GLUE_TechStop ()
     36  P00 (#EXT_ERR,#PGNO_GET,ID[],128 )
     37  ApplicationRunFlag=FALSE
@@ base line 54, backup line 55 @@
     55  ENDIF
     56  ENDIF
-    62  GLUE_Restart ()
     67  Endif
     68  INTERRUPT ON 3
```

### `KRC/R1/System/tm_bib.dat`

changed, KUKA system / vendor package: 1 code line(s) removed, 1 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/System/tm_bib.dat.diff](diffs/KRC/R1/System/tm_bib.dat.diff)

Attributes: &PARAM DISKPATH = System -> &PARAM DISKPATH = KRC:\R1\System; &REL 941 -> &REL 961

Data changes:

- iSTOP_TYPE (INT): 0 -> 53

Runtime values (left out of the code diff): TQM_ACT: {T11 200,T12 200,T13 200,T14 200,T15 200... -> {T11 200,T12 200,T13 200,T14 200,T15 200...

```diff
@@ base line 36, backup line 36 @@
     36  REAL ScalingImpact=250000.0
     37  REAL TooLarge=100000.0
-    47  DECL INT iSTOP_TYPE=0
+    47  DECL INT iSTOP_TYPE=53
     48  DECL REAL rPAR=0.0
     50  GLOBAL INT iTQM_DELAY=150
```

### `KRC/R1/TP/AutomationCore/automationcoreroutines.dat`

changed, KUKA system / vendor package: 34 code line(s) removed, 15 added; 11 comment/blank line change(s). Full diff: [diffs/KRC/R1/TP/AutomationCore/automationcoreroutines.dat.diff](diffs/KRC/R1/TP/AutomationCore/automationcoreroutines.dat.diff)

Attributes: -&ACCESS  R; -&PARAM DISKPATH = TP/AutomationCore; -&REL 11; +&ACCESS RO5

Data changes:

- added 15 SIGNAL: di100CameraJudgmentOK, di101CameraJudgmentNG, di106PartRejected, di227NutPresent1, di466PartClampOpen, di467PartClampClosed, di470QFPAdvanced, do106PartRejected, do498UpperPinExtend, do499UpperPinRetract, do501PartClampClose, do502PartClampOpen ...
- removed 4 BOOL: bScrapBackpanel, bScrapCrossMBR, bScrapSMBRlower, bScrapSMBRupper
- removed 1 INT: ScrapCount
- removed 29 SIGNAL: di100CameraJudmentOK, di101CameraJudmentNG, di106PartRejeted, di227SensorCamera, di466Reserved, di467Reserved, di470Reserved, di610Stud_Nut_Present1, di611Stud_Nut_Present2, di612Stud_Nut_Present3, di613Stud_Nut_Present4, di630Stud_Nut_Present1 ...

```diff
@@ base line 137, backup line 135 @@
    135  GLOBAL SIGNAL di098Spare $IN[98]
    136  GLOBAL SIGNAL di099Spare $IN[99]
-   139  GLOBAL SIGNAL di100CameraJudmentOK $IN[100]
-   140  GLOBAL SIGNAL di101CameraJudmentNG $IN[101]
+   137  GLOBAL SIGNAL di100CameraJudgmentOK $IN[100]
+   138  GLOBAL SIGNAL di101CameraJudgmentNG $IN[101]
    139  GLOBAL SIGNAL di102Spare $IN[102]
    140  GLOBAL SIGNAL di103Spare $IN[103]
    141  GLOBAL SIGNAL di104Spare $IN[104]
    142  GLOBAL SIGNAL di105Spare $IN[105]
-   145  GLOBAL SIGNAL di106PartRejeted $IN[106]
+   143  GLOBAL SIGNAL di106PartRejected $IN[106]
    144  GLOBAL SIGNAL di107Spare $IN[107]
    145  GLOBAL SIGNAL di108Spare $IN[108]
@@ base line 314, backup line 312 @@
    312  GLOBAL SIGNAL do104Axis1Bit128 $OUT[104]
    313  GLOBAL SIGNAL do105Axis1Bit256 $OUT[105]
-   316  GLOBAL SIGNAL do106PartRejeted $OUT[106]
+   314  GLOBAL SIGNAL do106PartRejected $OUT[106]
    315  GLOBAL SIGNAL do107Hopper1LowLevel $OUT[107]
    316  GLOBAL SIGNAL do108Hopper2LowLevel $OUT[108]
@@ base line 638, backup line 636 @@
    636  GLOBAL SIGNAL di225WaterFlowOK $IN[225]
    637  GLOBAL SIGNAL di226Spare $IN[226]
-   640  GLOBAL SIGNAL di227SensorCamera $IN[227]
+   640  GLOBAL SIGNAL di227NutPresent1 $IN[227]
    641  GLOBAL SIGNAL di228Spare $IN[228]
    642  GLOBAL SIGNAL di229Spare $IN[229]
@@ base line 1341, backup line 1341 @@
   1341  GLOBAL SIGNAL do496Reserved $OUT[496]
   1342  GLOBAL SIGNAL do497Reserved $OUT[497]
-  1343  GLOBAL SIGNAL do498Reserved $OUT[498]
-  1344  GLOBAL SIGNAL do499Reserved $OUT[499]
+  1345  GLOBAL SIGNAL do498UpperPinExtend $OUT[498]
+  1346  GLOBAL SIGNAL do499UpperPinRetract $OUT[499]
   1347  GLOBAL SIGNAL do500Reserved $OUT[500]
-  1346  GLOBAL SIGNAL do501Reserved $OUT[501]
-  1347  GLOBAL SIGNAL do502Reserved $OUT[502]
-  1348  GLOBAL SIGNAL do503Reserved $OUT[503]
-  1349  GLOBAL SIGNAL do504Reserved $OUT[504]
-  1350  GLOBAL SIGNAL do505Reserved $OUT[505]
+  1348  GLOBAL SIGNAL do501PartClampClose $OUT[501]
+  1349  GLOBAL SIGNAL do502PartClampOpen $OUT[502]
+  1350  GLOBAL SIGNAL do503QFPAdvance $OUT[503]
+  1351  GLOBAL SIGNAL do504QFPReturn $OUT[504]
+  1352  GLOBAL SIGNAL do505QFPNutBlowOff $OUT[505]
   1355  GLOBAL SIGNAL di465Reserved $IN[465]
-  1354  GLOBAL SIGNAL di466Reserved $IN[466]
-  1355  GLOBAL SIGNAL di467Reserved $IN[467]
+  1356  GLOBAL SIGNAL di466PartClampOpen $IN[466]
+  1357  GLOBAL SIGNAL di467PartClampClosed $IN[467]
   1358  GLOBAL SIGNAL di468Reserved $IN[468]
   1359  GLOBAL SIGNAL di469Reserved $IN[469]
-  1358  GLOBAL SIGNAL di470Reserved $IN[470]
+  1360  GLOBAL SIGNAL di470QFPAdvanced $IN[470]
   1361  GLOBAL SIGNAL di471Reserved $IN[471]
   1362  GLOBAL SIGNAL di472WaterTempOK $IN[472]
@@ base line 1588, backup line 1590 @@
   1590  GLOBAL SIGNAL di605ai_Nut1_B13 $IN[605]
```
_24 more lines: see diffs/KRC/R1/TP/AutomationCore/automationcoreroutines.dat.diff_

### `KRC/R1/TP/AutomationCore/automationglobalpos.dat`

changed, KUKA system / vendor package: 2 code line(s) removed, 2 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/TP/AutomationCore/automationglobalpos.dat.diff](diffs/KRC/R1/TP/AutomationCore/automationglobalpos.dat.diff)

Data changes:

- XREFSWITCH (E6POS) re-taught: moved 1.0 mm, rotated up to 0.4 deg
- XREPAIR (E6POS) re-taught: moved 2104.5 mm, rotated up to 146.1 deg, S/T 2/10 -> 2/2 (ARM CONFIGURATION CHANGED)

```diff
@@ base line 15, backup line 15 @@
     15  DECL GLOBAL PDAT PPounce={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000}
     16  DECL GLOBAL LDAT LCPounce={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    17  DECL GLOBAL E6POS XREPAIR={X 57.3420563,Y -1090.23523,Z 2456.71094,A -83.9461,B 4.55372906,C 0.917426229,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    17  DECL GLOBAL E6POS XREPAIR={X -626.534790,Y -1314.66345,Z 479.154968,A 129.959946,B 86.7954178,C -140.846069,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     18  DECL GLOBAL FDAT FRepair={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     19  DECL GLOBAL PDAT PRepair={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000}
@@ base line 23, backup line 23 @@
     23  DECL GLOBAL PDAT PTipDress={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000}
     24  DECL GLOBAL LDAT LCTipDress={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    25  DECL GLOBAL E6POS XREFSWITCH={X -814.158813,Y -752.360107,Z -58.2259216,A 93.9359894,B 87.4085,C -176.908646,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    25  DECL GLOBAL E6POS XREFSWITCH={X -813.172302,Y -752.430481,Z -57.9095879,A 94.3093109,B 87.4202652,C -176.541763,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     26  DECL GLOBAL FDAT FRefSwitch={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     27  DECL GLOBAL PDAT PRefSwitch={VEL 100.000,ACC 100.000,APO_DIST 100.000,GEAR_JERK 50.0000}
```

### `KRC/R1/TP/GripperSpotTech/grp_data.dat`

changed, KUKA system / vendor package: 1 code line(s) removed, 1 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/TP/GripperSpotTech/grp_data.dat.diff](diffs/KRC/R1/TP/GripperSpotTech/grp_data.dat.diff)

Data changes:

- GRPg_SignVal (INT): 7850579 -> 11310649

```diff
@@ base line 20, backup line 20 @@
     20  GLOBAL BOOL GRPg_GhostMode=False
     21  GLOBAL INT GRPg_GhostInput=0
-    22  GLOBAL INT GRPg_SignVal=7850579
+    22  GLOBAL INT GRPg_SignVal=11310649
     23  DECL GLOBAL GRP_ErrStrategy_T GRPg_ErrStrategy[3]
     24  GRPg_ErrStrategy[1]=#DialAtT1T2
```

### Comment-only changes

| File | Comment/blank line changes | Attributes | Diff |
|---|---|---|---|
| `KRC/R1/Mada/$machine.dat` | 0 | -&ACCESS  RV; -&PARAM VERSION = 1.0.0; -&PARAM DISKPATH = MADA; +&ACCESS RV$ | diffs/KRC/R1/Mada/$machine.dat.diff |
| `KRC/R1/Mada/$robcor.dat` | 0 | +&PARAM DISKPATH = MADA; -&PARAM DISKPATH = MADA | diffs/KRC/R1/Mada/$robcor.dat.diff |
| `KRC/R1/Program/Styles/optiones/style1opt10autorr.src` | 38 | &COMMENT GE4_002 -> &COMMENT 03-10-R1 RED RABBIT CYCLE | diffs/KRC/R1/Program/Styles/optiones/style1opt10autorr.src.diff |
| `KRC/R1/Program/Styles/style_1.src` | 46 | &COMMENT GE4_002 -> &COMMENT 03-10-R1 STYLE 1 | diffs/KRC/R1/Program/Styles/style_1.src.diff |
| `KRC/R1/Program/Utilities/closeandcheckallclamps.dat` | 0 | &ACCESS RVO7 -> &ACCESS RVO4; +&COMMENT 03-10-R1 CLOSE GRIPPER 1 | diffs/KRC/R1/Program/Utilities/closeandcheckallclamps.dat.diff |
| `KRC/R1/Program/Utilities/closeandcheckallclamps.src` | 48 | &ACCESS RVO7 -> &ACCESS RVO4; +&COMMENT 03-10-R1 CLOSE GRIPPER 1 | diffs/KRC/R1/Program/Utilities/closeandcheckallclamps.src.diff |
| `KRC/R1/Program/Utilities/gunelectrodechange.src` | 103 | +&COMMENT 03-10-R1 ELECTRODE CHANGE | diffs/KRC/R1/Program/Utilities/gunelectrodechange.src.diff |
| `KRC/R1/Program/Utilities/hometopounce.src` | 11 | +&COMMENT 03-10-R1 NOT CALLED POUNCE | diffs/KRC/R1/Program/Utilities/hometopounce.src.diff |
| `KRC/R1/Program/Utilities/openandcheckallclamps.dat` | 0 | &ACCESS RVO7 -> &ACCESS RVO4; +&COMMENT 03-10-R1 OPEN GRIPPER 1 | diffs/KRC/R1/Program/Utilities/openandcheckallclamps.dat.diff |
| `KRC/R1/Program/Utilities/openandcheckallclamps.src` | 42 | &ACCESS RVO7 -> &ACCESS RVO4; +&COMMENT 03-10-R1 OPEN GRIPPER 1 | diffs/KRC/R1/Program/Utilities/openandcheckallclamps.src.diff |
| `KRC/R1/Program/Utilities/pouncetohome.src` | 11 | +&COMMENT 03-10-R1 POUNCE TO HOME | diffs/KRC/R1/Program/Utilities/pouncetohome.src.diff |
| `KRC/R1/Program/home.dat` | 0 | &ACCESS RVP1 -> &ACCESS RVO1; +&COMMENT 03-10-R1 MOVE HOME | diffs/KRC/R1/Program/home.dat.diff |
| `KRC/R1/Program/HOME.src` | 11 | &ACCESS RVP1 -> &ACCESS RVO1; +&COMMENT 03-10-R1 MOVE HOME | diffs/KRC/R1/Program/HOME.src.diff |
| `KRC/R1/Program/masref_user.src` | 39 | &ACCESS RVO7 -> &ACCESS RVO4; &COMMENT Mastering Reference User Program -> &COMMENT 03-10-R1 MASTERING REF | diffs/KRC/R1/Program/masref_user.src.diff |
| `KRC/R1/Program/tm_useraction.src` | 14 | +&COMMENT 03-10-R1 COLLISION STOP | diffs/KRC/R1/Program/tm_useraction.src.diff |
| `KRC/R1/System/masref_main.dat` | 0 | &ACCESS RVO1 -> &ACCESS RVP1 | diffs/KRC/R1/System/masref_main.dat.diff |
| `KRC/R1/System/masref_main.src` | 0 | &ACCESS RVO1 -> &ACCESS RVP1 | diffs/KRC/R1/System/masref_main.src.diff |
| `KRC/R1/System/tm_bib.src` | 0 | &ACCESS R7 -> &ACCESS R5; &REL 953 -> &REL 962 | diffs/KRC/R1/System/tm_bib.src.diff |
| `KRC/R1/TP/AutomationCore/automationcoredata.dat` | 2 | -&ACCESS  R; -&PARAM DISKPATH = TP/AutomationCore; +&ACCESS R5 | diffs/KRC/R1/TP/AutomationCore/automationcoredata.dat.diff |
| `KRC/R1/TP/GripperSpotTech/grp_func.dat` | 0 | -&ACCESS  R; -&COMMENT GripperSpotTech package; -&PARAM DISKPATH = TP/GripperSpotTech; -&PARAM KUKATPGRP_VERSION = 4.0; -&REL 1; +&ACCESS R5 | diffs/KRC/R1/TP/GripperSpotTech/grp_func.dat.diff |
| `KRC/R1/TP/NutWeld/nutweldroutines.dat` | 9 | - | diffs/KRC/R1/TP/NutWeld/nutweldroutines.dat.diff |
| `KRC/R1/safetest.src` | 10 | +&COMMENT 03-10-R1 TEST LOOP | diffs/KRC/R1/safetest.src.diff |
| `KRC/STEU/Mada/$machine.dat` | 0 | -&ACCESS RV$; +&ACCESS  RV; +&PARAM DISKPATH = MADA | diffs/KRC/STEU/Mada/$machine.dat.diff |

## Mechanical checks

Signal declarations changed (names lower-cased):

- $IN[100]: di100camerajudmentok -> di100camerajudgmentok
- $IN[101]: di101camerajudmentng -> di101camerajudgmentng
- $IN[106]: di106partrejeted -> di106partrejected
- $IN[141]: di141redrabbitfail, di141spare -> di141spare
- $IN[227]: di227sensorcamera, nut_present1 -> di227nutpresent1
- $IN[466]: di466reserved, di466spare -> di466partclampopen, di466spare
- $IN[467]: di467reserved, di467spare -> di467partclampclosed, di467spare
- $IN[470]: di470reserved, di470spare -> di470qfpadvanced, di470spare
- $IN[610]: di610stud_nut_present1 -> (not declared)
- $IN[611]: di611stud_nut_present2 -> (not declared)
- $IN[612]: di612stud_nut_present3 -> (not declared)
- $IN[613]: di613stud_nut_present4 -> (not declared)
- $IN[630]: di630stud_nut_present1 -> (not declared)
- $IN[631]: di631stud_nut_present2 -> (not declared)
- $IN[632]: di632stud_nut_present3 -> (not declared)
- $IN[633]: di633stud_nut_present4 -> (not declared)
- $IN[634]: di634stud_nut_present5 -> (not declared)
- $IN[635]: di635stud_nut_present6 -> (not declared)
- $IN[777]: di777stud_nut_present1 -> (not declared)
- $IN[778]: di778stud_nut_present2 -> (not declared)
- $IN[779]: di779stud_nut_present3 -> (not declared)
- $IN[780]: di780stud_nut_present4 -> (not declared)
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
- $OUT[4000]: cl_all_home_plc -> (not declared)

### FAIL (12)

- `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src:74` [4 inline form consistency] ;FOLD OUT 18 'do018PartInGripper1' State=FALSE: 0 output assignments in the body, the form generates one
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src:42` [4 inline form consistency] ;FOLD OUT 249 'do249Group1Home' State=FALSE CONT: 0 output assignments in the body, the form generates one
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src:46` [4 inline form consistency] ;FOLD OUT 250 'do250Group1Work' State=TRUE CONT: 0 output assignments in the body, the form generates one
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src:162` [4 inline form consistency] ;FOLD OUT 18 'do018PartInGripper1' State=FALSE: 0 output assignments in the body, the form generates one
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src:116` [4 inline form consistency] ;FOLD OUT 18 'do018PartInGripper1' State=TRUE: 0 output assignments in the body, the form generates one
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.src:117` [4 inline form consistency] ;FOLD OUT 18 'do018PartInGripper1' State=TRUE: 0 output assignments in the body, the form generates one
- `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src:111` [4 inline form consistency] ;FOLD OUT 18 'do018PartInGripper1' State=TRUE: 0 output assignments in the body, the form generates one
- `KRC/R1/Program/Utilities/RejectGE4.src:29` [4 inline form consistency] ;FOLD OUT 106 'do106PartRejeted' State=TRUE: 0 output assignments in the body, the form generates one
- `KRC/R1/Program/Utilities/RejectGE4.src:76` [4 inline form consistency] ;FOLD OUT 18 'do018PartInGripper1' State=FALSE: 0 output assignments in the body, the form generates one
- `KRC/R1/Program/Utilities/RejectGE4.src:109` [4 inline form consistency] ;FOLD OUT 106 'do106PartRejeted' State=FALSE: 0 output assignments in the body, the form generates one
- `KRC/R1/System/$config.dat` [11 data declarations] NUT_WELD_RETRY was removed from this file but is still used in KRC/R1/Program/Centerline/centerline_weld.src:67: that module no longer compiles
- `KRC/R1/System/$config.dat` [11 data declarations] REDRABBIT was removed from this file but is still used in KRC/R1/Program/Utilities/RedRabbit.dat:5: that module no longer compiles

### WARN (55)

- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:208` [8 I/O without signal comment] do501PartClampClose accessed with no comment naming it in the 4 lines above (C24): do501PartClampClose=FALSE
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:209` [8 I/O without signal comment] do502PartClampOpen accessed with no comment naming it in the 4 lines above (C24): do502PartClampOpen=TRUE
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:215` [8 I/O without signal comment] di466PartClampOpen accessed with no comment naming it in the 4 lines above (C24): IF NOT di466PartClampOpen THEN
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:217` [8 I/O without signal comment] $IN[466], $IN[467] accessed with no comment naming it in the 4 lines above (C24): Msg.Msg_txt[]="Part clamp not open ($IN[466] / $IN[467]) - robot waiti
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:220` [8 I/O without signal comment] di466PartClampOpen accessed with no comment naming it in the 4 lines above (C24): WAIT FOR di466PartClampOpen
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:225` [8 I/O without signal comment] do498UpperPinExtend accessed with no comment naming it in the 4 lines above (C24): do498UpperPinExtend=FALSE
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:226` [8 I/O without signal comment] do499UpperPinRetract accessed with no comment naming it in the 4 lines above (C24): do499UpperPinRetract=TRUE
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:322` [8 I/O without signal comment] dipw1_Fault, dipw1_WeldComplete accessed with no comment naming it in the 4 lines above (C24): WHILE (NOT dipw1_WeldComplete) AND (NOT dipw1_Fault) AND (nWaitMs<CL_W
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:328` [8 I/O without signal comment] dipw1_Fault, dipw1_WeldComplete accessed with no comment naming it in the 4 lines above (C24): IF dipw1_Fault OR (NOT dipw1_WeldComplete) THEN
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:331` [8 I/O without signal comment] dipw1_Fault accessed with no comment naming it in the 4 lines above (C24): IF dipw1_Fault THEN
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:333` [8 I/O without signal comment] $IN[485] accessed with no comment naming it in the 4 lines above (C24): Msg.Msg_txt[]="Bosch weld fault ($IN[485]) - nut weld NOT OK, red ligh
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:337` [8 I/O without signal comment] $IN[483] accessed with no comment naming it in the 4 lines above (C24): Msg.Msg_txt[]="Weld complete ($IN[483]) not received in %1 ms - red li
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:345` [8 I/O without signal comment] dipw1_WeldComplete accessed with no comment naming it in the 4 lines above (C24): IF NOT dipw1_WeldComplete THEN
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:347` [8 I/O without signal comment] $IN[483] accessed with no comment naming it in the 4 lines above (C24): Msg.Msg_txt[]="Robot waiting for weld complete $IN[483] from the Bosch
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:349` [8 I/O without signal comment] dipw1_WeldComplete accessed with no comment naming it in the 4 lines above (C24): WAIT FOR dipw1_WeldComplete
- `KRC/R1/Program/Centerline/PRELOAD.src:79` [8 I/O without signal comment] di470QFPAdvanced, dipw1_SpearHome accessed with no comment naming it in the 4 lines above (C24): IF QFP_NUT_LOADED AND (dipw1_SpearHome==TRUE) AND (di470QFPAdvanced==F
- `KRC/R1/Program/Centerline/PRELOAD.src:182` [8 I/O without signal comment] dopw1_ReturnPin accessed with no comment naming it in the 4 lines above (C24): dopw1_ReturnPin=FALSE
- `KRC/R1/Program/Centerline/PRELOAD.src:183` [8 I/O without signal comment] dopw1_AdvancePin accessed with no comment naming it in the 4 lines above (C24): dopw1_AdvancePin=TRUE
- `KRC/R1/Program/Centerline/PRELOAD.src:272` [8 I/O without signal comment] dopw1_StartFeed accessed with no comment naming it in the 4 lines above (C24): dopw1_StartFeed=TRUE
- `KRC/R1/Program/Centerline/PRELOAD.src:277` [8 I/O without signal comment] dopw1_StartFeed accessed with no comment naming it in the 4 lines above (C24): dopw1_StartFeed=FALSE
- `KRC/R1/Program/Centerline/centerline_weld.src:95` [8 I/O without signal comment] dopw1_AdvancePin accessed with no comment naming it in the 4 lines above (C24): dopw1_AdvancePin=FALSE
- `KRC/R1/Program/Centerline/centerline_weld.src:125` [8 I/O without signal comment] dopw1_AdvancePin accessed with no comment naming it in the 4 lines above (C24): dopw1_AdvancePin=TRUE
- `KRC/R1/Program/StyleApps/Options/style1app1opt1A.src:160` [6 commented-out code] commented-out code (TRIGGER): ;TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO Request_next_nut() PRIO= -1   ;2026-10-10
- `KRC/R1/Program/StyleApps/Options/style1app1opt1B.src:160` [6 commented-out code] commented-out code (TRIGGER): ;TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO Request_next_nut() PRIO= -1   ;2026-10-10
- `KRC/R1/Program/StyleApps/Options/style1app1opt2A.src:147` [6 commented-out code] commented-out code (TRIGGER): ;TRIGGER WHEN DISTANCE = 1 DELAY = 0 DO Request_next_nut() PRIO= -1   ;2026-10-10
- `KRC/R1/Program/StyleApps/Options/style1app1opt2B.src:147` [6 commented-out code] commented-out code (TRIGGER): ;TRIGGER WHEN DISTANCE = 1 DELAY = 0 DO Request_next_nut() PRIO= -1   ;2026-10-10
- `KRC/R1/Program/StyleApps/Options/style1app2opt1.src:193` [8 I/O without signal comment] $IN[227] accessed with no comment naming it in the 4 lines above (C24): Msg.Msg_txt[]="Nut check: PN%1 missing (sensor $IN[227] at P%2) - part
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src:75` [5 hand-typed line in inline form] hand-typed line inside inline form - lost on Touch Up (F32): do018Part1InGripper=FALSE
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src:44` [5 hand-typed line in inline form] hand-typed line inside inline form - lost on Touch Up (F32): do249Group1Home=FALSE
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src:48` [5 hand-typed line in inline form] hand-typed line inside inline form - lost on Touch Up (F32): do250Group1Work=TRUE
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src:153` [6 commented-out code] commented-out code (motion): ;LIN P24
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src:163` [5 hand-typed line in inline form] hand-typed line inside inline form - lost on Touch Up (F32): do018Part1InGripper=FALSE
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src:117` [5 hand-typed line in inline form] hand-typed line inside inline form - lost on Touch Up (F32): do018Part1InGripper=TRUE
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.src:118` [5 hand-typed line in inline form] hand-typed line inside inline form - lost on Touch Up (F32): do018Part1InGripper=TRUE
- `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src:112` [5 hand-typed line in inline form] hand-typed line inside inline form - lost on Touch Up (F32): do018Part1InGripper=TRUE
- `KRC/R1/Program/Utilities/RejectGE4.src:30` [5 hand-typed line in inline form] hand-typed line inside inline form - lost on Touch Up (F32): do106PartRejected=TRUE
- `KRC/R1/Program/Utilities/RejectGE4.src:77` [5 hand-typed line in inline form] hand-typed line inside inline form - lost on Touch Up (F32): do018Part1InGripper=FALSE
- `KRC/R1/Program/Utilities/RejectGE4.src:110` [5 hand-typed line in inline form] hand-typed line inside inline form - lost on Touch Up (F32): do106PartRejected=FALSE
- `KRC/R1/System/sps.sub:163` [8 I/O without signal comment] dipw1_Fault accessed with no comment naming it in the 4 lines above (C24): dopw1_LevelOk = NOT (CL_WeldFault OR dipw1_Fault)
- `KRC/R1/System/sps.sub:192` [8 I/O without signal comment] dopw1_StartWater, di013WaterEnable accessed with no comment naming it in the 4 lines above (C24): dopw1_StartWater=di013WaterEnable AND NOT do091RobotReadyCapChange
- `KRC/R1/System/sps.sub:200` [8 I/O without signal comment] dipw1_EndOfStepper, dipw1_StepperWarning accessed with no comment naming it in the 4 lines above (C24): IF ((dipw1_StepperWarning==FALSE) AND (dipw1_EndOfStepper==FALSE)) THE
- `KRC/R1/System/sps.sub:205` [8 I/O without signal comment] dipw1_EndOfStepper, dipw1_StepperWarning accessed with no comment naming it in the 4 lines above (C24): IF ((dipw1_StepperWarning==TRUE) AND (dipw1_EndOfStepper==FALSE)) THEN
- `KRC/R1/System/sps.sub:207` [8 I/O without signal comment] dopw1_StepperWarningPL accessed with no comment naming it in the 4 lines above (C24): dopw1_StepperWarningPL=TRUE
- `KRC/R1/System/sps.sub:208` [8 I/O without signal comment] dopw1_EndofStepperPL accessed with no comment naming it in the 4 lines above (C24): dopw1_EndofStepperPL=TRUE
- `KRC/R1/System/sps.sub:210` [8 I/O without signal comment] dipw1_EndOfStepper accessed with no comment naming it in the 4 lines above (C24): IF (dipw1_EndOfStepper==TRUE) THEN
- `KRC/R1/System/sps.sub:212` [8 I/O without signal comment] dopw1_StepperWarningPL accessed with no comment naming it in the 4 lines above (C24): dopw1_StepperWarningPL=FALSE
- `KRC/R1/System/sps.sub:213` [8 I/O without signal comment] dopw1_EndofStepperPL accessed with no comment naming it in the 4 lines above (C24): dopw1_EndofStepperPL=TRUE
- `KRC/R1/System/sps.sub:224` [8 I/O without signal comment] dopw1_WeldOnExternal accessed with no comment naming it in the 4 lines above (C24): dopw1_WeldOnExternal=FALSE
- `KRC/R1/System/sps.sub:226` [8 I/O without signal comment] dopw1_WeldContactEnable accessed with no comment naming it in the 4 lines above (C24): dopw1_WeldContactEnable=TRUE
- `KRC/R1/System/sps.sub:227` [8 I/O without signal comment] dopw1_WeldOnExternal accessed with no comment naming it in the 4 lines above (C24): dopw1_WeldOnExternal=TRUE
- `KRC/R1/System/sps.sub:237` [8 I/O without signal comment] do107Hopper1LowLevel, dipw1_HopperLowLevel accessed with no comment naming it in the 4 lines above (C24): do107Hopper1LowLevel= NOT dipw1_HopperLowLevel
- `KRC/R1/System/sps.sub:238` [8 I/O without signal comment] dipw1_Ready, dipw1_Fault, do118Nut1Ready accessed with no comment naming it in the 4 lines above (C24): do118Nut1Ready= (dipw1_Ready AND NOT dipw1_Fault)
- `KRC/R1/System/sps.sub:239` [8 I/O without signal comment] do134Nut1Fault, dipw1_Ready, dipw1_Fault accessed with no comment naming it in the 4 lines above (C24): do134Nut1Fault= (dipw1_Fault OR NOT dipw1_Ready)
- `KRC/R1/System/sps.sub:240` [8 I/O without signal comment] dipw1_AirOK, do094AirOK accessed with no comment naming it in the 4 lines above (C24): do094AirOK= dipw1_AirOK
- `KRC/R1/System/sps.sub:241` [8 I/O without signal comment] do013WaterIsOn accessed with no comment naming it in the 4 lines above (C24): do013WaterIsOn = dipw1_WaterOk

### INFO (32)

- `KRC/R1/Program/Centerline/CENTERLINE_HOME.src:55` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR dipw1_SpearHome
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:220` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR di466PartClampOpen
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:239` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR (CL_WeldPinPosition>=nPinRetractMin) AND (CL_WeldPinPosition<
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:286` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR (CL_WeldPinPosition>=CL_PIN_WELD_MIN) AND (CL_WeldPinPosition
- `KRC/R1/Program/Centerline/centerline_weld.src:84` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR di466PartClampOpen
- `KRC/R1/Program/Centerline/centerline_weld.src:104` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR dipw1_SpearHome
- `KRC/R1/Program/Centerline/centerline_weld.src:115` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR di470QFPAdvanced
- `KRC/R1/Program/Centerline/centerline_weld.src:140` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR dipw1_SpearHome
- `KRC/R1/Program/Centerline/centerline_weld.src:178` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR di467PartClampClosed
- `KRC/R1/Program/Centerline/centerline_weld.src:274` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR (CL_GunStrokePositionLPT>=CL_GUN_WELD_MIN) AND (CL_GunStrokeP
- `KRC/R1/Program/Centerline/centerline_weld.src:332` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR di466PartClampOpen
- `KRC/R1/Program/Centerline/centerline_weld.src:344` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR dipw1_SpearHome
- `KRC/R1/Program/StyleApps/Options/style1app1opt1A.src:113` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR NUT_READY==TRUE
- `KRC/R1/Program/StyleApps/Options/style1app1opt1B.src:113` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR NUT_READY==TRUE
- `KRC/R1/Program/StyleApps/Options/style1app1opt2A.src:1` [2 format] line endings changed from LF to CRLF (the KRC reads both; git diff shows every line changed, the code diff of this report does not)
- `KRC/R1/Program/StyleApps/Options/style1app1opt2A.src:102` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR NUT_READY==TRUE
- `KRC/R1/Program/StyleApps/Options/style1app1opt2B.src:102` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR NUT_READY==TRUE
- `KRC/R1/Program/StyleApps/Options/style1app1opt3A.dat` [1 fold/block structure] fold/block structure improved: 1 of 1 pre-existing defects fixed
- `KRC/R1/Program/StyleApps/Options/style1app1opt3A.src:1` [2 format] line endings changed from LF to CRLF (the KRC reads both; git diff shows every line changed, the code diff of this report does not)
- `KRC/R1/Program/StyleApps/Options/style1app1opt3A.src:103` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR NUT_READY==TRUE
- `KRC/R1/Program/StyleApps/Options/style1app1opt3B.dat` [1 fold/block structure] fold/block structure improved: 1 of 1 pre-existing defects fixed
- `KRC/R1/Program/StyleApps/Options/style1app1opt3B.src:103` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR NUT_READY==TRUE
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src:71` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2 )
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src:150` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2 )
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src:37` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2)
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src:111` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( di253PartPresent1 ) AND ( di254PartPresent2 )
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.src:38` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2)
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.src:112` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( di253PartPresent1 ) AND ( di254PartPresent2 )
- `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src:39` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2)
- `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src:106` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( di253PartPresent1 ) AND ( di254PartPresent2 )
- `KRC/R1/Program/Utilities/RejectGE4.src:64` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2 )
- `KRC/R1/cell.src:86` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( di008ReturnFromRepair )
