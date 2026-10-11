# Backup audit - ed7a88c5-V431_03_WINDOWS-2CPT70E_BMW_03_10_R1_658424.zip

- Backup: `/root/.claude/uploads/50f56c92-2919-5ae3-94c9-0de4476bbe87/ed7a88c5-V431_03_WINDOWS-2CPT70E_BMW_03_10_R1_658424.zip` (sha256 `5bbd1a59c40285b9...`)
- am.ini: archive `C:\windows\TEMP\tmpB87B.tmp\`, date `2026-10-10_21-20-39`, config `All`, robot `BMW_03_10_R1`, serial `658424`, KSS `V8.3.29`
- Compared with: `1b28a7e` = `1b28a7ee87` "Delivery of 2026-10-05 evening: program package on the 14:46 backup; Excel and PDF"; first commit (archive as received) `22a98cc8ef`
- Generated 2026-10-11T13:46:57 by tools/audit_backup.py

## Summary

| | |
|---|---|
| Entries audited (Log Files/ skipped: 8) | 322 |
| Unchanged | 231 |
| Changed | 76 |
| Added | 5 |
| Missing from the backup | 7 |
| **Deleted modules still on the controller** | 8 |
| **Pre-cleanup files** | 1 |
| Edited on top of the pre-cleanup file | 0 |
| KRL files with code changes | 43 |
| Code lines removed / added | 192 / 768 |
| KRL files with comment-only changes | 17 |
| KRL files with runtime values only (written by the program, not edits) | 2 |
| Checks FAIL / WARN / INFO | 10 / 52 / 19 |

**Needs attention:**

- **8 module(s) deleted in the cleanup still on the controller** (listed below)
- **1 PRE-CLEANUP file(s)**: the cleaned program was not loaded or was overwritten: `KRC/R1/Mada/$robcor.dat`
- WARN 2 entries outside the KUKA archive layout ignored (e.g. Archive.log)
- WARN 7 file(s) of the base missing from the backup - deleted on the robot, or an incomplete archive (e.g. C/KRC/User/ProjectRoot/@BaseProject/BaseProject.wvs; all in Files, "Missing from the backup")
- WARN KRC/R1/System/ir_stopm.src: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- **10 FAIL** in the mechanical checks
- 52 WARN in the mechanical checks

## The backup itself

- FAIL: KRC/R1/Program/Utilities/capchange.dat: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/Utilities/capchange.src: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/Utilities/ElectrodeChange.dat: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/Utilities/electrodechange.src: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/Utilities/RedRabbit.dat: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/Utilities/redrabbit.src: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/POUNCE.dat: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Program/POUNCE.src: module deleted in the cleanup is still on the controller - delete it there
- FAIL: KRC/R1/Mada/$robcor.dat: this is the pre-cleanup file: the cleaned program was not loaded or was overwritten
- WARN: 2 entries outside the KUKA archive layout ignored (e.g. Archive.log)
- WARN: 7 file(s) of the base missing from the backup - deleted on the robot, or an incomplete archive (e.g. C/KRC/User/ProjectRoot/@BaseProject/BaseProject.wvs; all in Files, "Missing from the backup")
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
- INFO: KRC/R1/Program/StylePicks/Options/style1pick1opt1autorr.src: spelled KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src in the base (the controller ignores case)
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
- INFO: KRC/R1/TP/AutomationCore/automationglobalpos.dat: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)
- INFO: KRC/R1/TP/GripperSpotTech/grp_data.dat: KUKA system / vendor package file changed - if intended, list the edit in the hand-over so a package update does not drop it (C28)

## Deleted modules still present

The cleanup deleted these modules. A restore does not delete files, so they are still on the controller: delete them there (navigator, expert mode).

- `KRC/R1/Program/Utilities/capchange.dat` - identical to the archive as received
- `KRC/R1/Program/Utilities/capchange.src` - identical to the archive as received
- `KRC/R1/Program/Utilities/ElectrodeChange.dat` - identical to the archive as received
- `KRC/R1/Program/Utilities/electrodechange.src` - identical to the archive as received
- `KRC/R1/Program/Utilities/RedRabbit.dat` - identical to the archive as received
- `KRC/R1/Program/Utilities/redrabbit.src` - identical to the archive as received
- `KRC/R1/Program/POUNCE.dat` - identical to the archive as received
- `KRC/R1/Program/POUNCE.src` - identical to the archive as received

## Pre-cleanup files

**These files are byte-for-byte the archive as received: the cleaned program was not loaded or was overwritten. Every comment correction, header and junk removal of the cleanup is lost in them.**

- `KRC/R1/Mada/$robcor.dat`

## Files

### Changed (76)

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
- `KRC/R1/Mada/$robcor.dat` - machine data - PRE-CLEANUP FILE (mechanical checks skipped)
- `KRC/R1/Program/Centerline/centerline_weld.src` - integrator program
- `KRC/R1/Program/Centerline/gun_open_check.dat` - integrator program
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src` - integrator program
- `KRC/R1/Program/Centerline/PRELOAD.dat` - integrator program
- `KRC/R1/Program/Centerline/PRELOAD.src` - integrator program
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
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.dat` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt2.dat` - integrator program
- `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src` - integrator program
- `KRC/R1/Program/Styles/style_1.dat` - integrator program
- `KRC/R1/Program/Utilities/closeandcheckallclamps.dat` - integrator program
- `KRC/R1/Program/Utilities/closeandcheckallclamps.src` - integrator program
- `KRC/R1/Program/Utilities/hometorepair.dat` - integrator program
- `KRC/R1/Program/Utilities/hometorepair.src` - integrator program
- `KRC/R1/Program/Utilities/openandcheckallclamps.dat` - integrator program
- `KRC/R1/Program/Utilities/openandcheckallclamps.src` - integrator program
- `KRC/R1/Program/Utilities/RejectGE4.dat` - integrator program
- `KRC/R1/Program/Utilities/RejectGE4.src` - integrator program
- `KRC/R1/Program/Utilities/repairtohome.dat` - integrator program
- `KRC/R1/Program/Utilities/repairtohome.src` - integrator program
- `KRC/R1/Program/home.dat` - integrator program
- `KRC/R1/Program/masref_user.dat` - integrator program
- `KRC/R1/Program/masref_user.src` - integrator program
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
- `KRC/R1/cell.src` - integrator program
- `KRC/STEU/Mada/$machine.dat` - machine data
- `Registry/LMSOFTWAREKUKA ROBOTER GMBHKUKA BOFOCX Control'sFileHandler.amr` - controller configuration - 1391 line(s) removed, 1078 added - diffs/Registry/LMSOFTWAREKUKA ROBOTER GMBHKUKA BOFOCX Control'sFileHandler.amr.diff
- `Registry/LMSOFTWAREKUKA ROBOTER GMBHWorkVisual.amr` - controller configuration - 3 line(s) removed, 2 added - diffs/Registry/LMSOFTWAREKUKA ROBOTER GMBHWorkVisual.amr.diff
- `am.ini` - archive metadata - 3 line(s) removed, 3 added - diffs/am.ini.diff

### Added (5)

- `C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8.asz` - controller configuration - binary, 4329196 bytes
- `C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8.useDeployedProject` - controller configuration - 0 line(s) removed, 1 added - diffs/C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8.useDeployedProject.diff
- `KRC/R1/Program/Styles/optiones/style1opt1.src` - integrator program
- `KRC/R1/Program/Styles/optiones/style1opt10autorr.src` - integrator program
- `Registry/LMSOFTWAREKUKA Roboter GmbHPerformance.amr` - controller configuration - 0 line(s) removed, 385 added - diffs/Registry/LMSOFTWAREKUKA Roboter GmbHPerformance.amr.diff

### Missing from the backup (7)

- `C/KRC/User/ProjectRoot/@BaseProject/BaseProject.wvs`
- `C/KRC/User/ProjectRoot/BMW-03-10R1_v8/BMW-03-10R1_v8.wvs`
- `C/KRC/User/ProjectRoot/V431-03-10R1_v6Active_Centerline_18/V431-03-10R1_v6Active_Centerline_18.log`
- `C/KRC/User/ProjectRoot/V431-03-10R1_v6Active_Centerline_18/V431-03-10R1_v6Active_Centerline_18.wvs`
- `C/KRC/User/ProjectRoot/V431-03-10R1_v6Active_Centerline_18/V431-03-10R1_v6Active_Centerline_18_old.log`
- `KRC/R1/Program/Styles/Options/Style1Opt10AutoRR.src`
- `KRC/R1/Program/Styles/Options/style1opt1.src`

### Outside the archive layout (ignored) (2)

- `Archive.log`
- `ArchiveInfo.xml`

## Code changes

### `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src`

changed, integrator program: 3 code line(s) removed, 243 added; 132 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src.diff](diffs/KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src.diff)

Attributes: &ACCESS RVO1 -> &ACCESS RVO5; &REL 2 -> &REL 25; +&PARAM DISKPATH = KRC:\R1\Program\Centerline

```diff
@@ base line 130, backup line 133 @@
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
@@ base line 142, backup line 157 @@
    157  WAIT SEC 0.1
    158  ENDWHILE
-   146  IF ($PRO_STATE0<>#P_ACTIVE) OR (CL_GunStrokePositionLPT<nGunOpenMin) OR (CL_GunStrokePositionLPT>nGunOpenMax) THEN
+   161  IF ($PRO_STATE0<>#P_ACTIVE) OR (CL_GunStrokePositionLPT<nGunOpenMin) OR (CL_GunStrokePositionLPT>nGunOpenMax) OR (NOT CL_ClampOpen) OR (NOT CL_PinRetracted) THEN
    162  Msg.Nr=7
-   148  Msg.Msg_txt[]="Robot in welder waiting for gun open and Submit running"
+   163  Msg.Msg_txt[]="Robot in welder waiting: Submit, gun open, clamp open, pin retracted"
    164  Par[1].Par_Type=#EMPTY
    165  nHandle=Set_KrlMsg(#STATE, Msg, Par[], Opt)
-   151  WHILE ($PRO_STATE0<>#P_ACTIVE) OR (CL_GunStrokePositionLPT<nGunOpenMin) OR (CL_GunStrokePositionLPT>nGunOpenMax)
+   166  WHILE ($PRO_STATE0<>#P_ACTIVE) OR (CL_GunStrokePositionLPT<nGunOpenMin) OR (CL_GunStrokePositionLPT>nGunOpenMax) OR (NOT CL_ClampOpen) OR (NOT CL_PinRetracted)
    167  WAIT SEC 0.1
    168  ENDWHILE
@@ base line 155, backup line 170 @@
    170  ENDIF
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
+   211  WHILE (NOT di466PartClampOpen) AND (nWaitMs<nPedestalWaitMs)
+   212  WAIT SEC 0.05
+   213  nWaitMs=nWaitMs+50
+   214  ENDWHILE
```
_206 more lines: see diffs/KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src.diff_

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

changed, integrator program: 13 code line(s) removed, 52 added; 62 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/PRELOAD.src.diff](diffs/KRC/R1/Program/Centerline/PRELOAD.src.diff)

```diff
@@ base line 40, backup line 51 @@
     51  STEP10DONE=FALSE
     52  STEP20DONE=FALSE
+    53  STEP10_ADV_STARTED=FALSE
     54  NUT_PRELOAD_FAULT=FALSE
     55  $TIMER_STOP[10]=TRUE
@@ base line 63, backup line 75 @@
     75  do503QFPAdvance=FALSE
     76  do504QFPReturn=TRUE
-    68  IF (dipw1_SpearHome==TRUE) AND (di470QFPAdvanced==FALSE) THEN
+    79  IF QFP_NUT_LOADED AND (dipw1_SpearHome==TRUE) AND (di470QFPAdvanced==FALSE) THEN
+    80  STEP0DONE=TRUE
+    81  ENDIF
+    85  IF (dipw1_SpearHome==TRUE) AND (di470QFPAdvanced==FALSE) AND (NOT QFP_NUT_LOADED) THEN
     88  dopw1_StartFeed=TRUE
     89  dopw1_BlowOff=FALSE
@@ base line 77, backup line 94 @@
     94  $TIMER_STOP[10]=FALSE
     95  ENDIF
-    81  IF $TIMER[10]>=2000 THEN
+    99  IF $TIMER[10]>=(2000+nFeedSettleMs) THEN
    100  $TIMER_STOP[10]=TRUE
    102  STEP0DONE=TRUE
@@ base line 112, backup line 130 @@
    130  IF NOT STEP10_ADV_STARTED THEN
    132  dopw1_BlowOff=TRUE
+   135  dopw1_AdvancePin=FALSE
+   136  dopw1_ReturnPin=TRUE
+   138  IF $TIMER_STOP[11] THEN
+   139  $TIMER[11]=0
+   140  $TIMER_STOP[11]=FALSE
+   141  ENDIF
    143  do503QFPAdvance=FALSE
    144  do504QFPReturn=TRUE
-   121  IF (dipw1_SpearHome==TRUE) AND (di470QFPAdvanced==FALSE) THEN
+   149  IF (dipw1_SpearHome==TRUE) AND (di470QFPAdvanced==FALSE) AND (((NOT bPinDownSensor) AND ($TIMER[11]>=nPinDownMs)) OR (bPinDownSensor AND ((dipw1_PinReturn==TRUE) OR ($TIMER[11]>=nPinDownMaxMs)))) THEN
    150  STEP10_ADV_STARTED=TRUE
+   151  $TIMER_STOP[11]=TRUE
+   152  $TIMER[11]=0
    154  ENDIF
    155  ELSE
@@ base line 137, backup line 167 @@
    167  do505QFPNutBlowOff=TRUE
    168  dopw1_BlowOff=FALSE
+   170  QFP_NUT_LOADED=FALSE
    172  IF $TIMER_STOP[13] THEN
    173  $TIMER[13]=0
    174  $TIMER_STOP[13]=FALSE
    175  ENDIF
+   181  dopw1_Nut1Intensify_Home=FALSE
    182  dopw1_ReturnPin=FALSE
    183  dopw1_AdvancePin=TRUE
@@ base line 152, backup line 188 @@
    188  $TIMER_STOP[11]=FALSE
    189  ENDIF
-   156  IF $TIMER[11]>=500 THEN
+   193  IF $TIMER[11]>=nPinUpMs THEN
    194  $TIMER_STOP[11]=TRUE
    196  STEP10DONE=TRUE
@@ base line 171, backup line 208 @@
```
_66 more lines: see diffs/KRC/R1/Program/Centerline/PRELOAD.src.diff_

### `KRC/R1/Program/Centerline/centerline_weld.src`

changed, integrator program: 16 code line(s) removed, 37 added; 105 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/centerline_weld.src.diff](diffs/KRC/R1/Program/Centerline/centerline_weld.src.diff)

```diff
@@ base line 5, backup line 5 @@
      5  DEF CENTERLINE_WELD()
+    64  CT_WELD_START()
+    67  NUT_WELD_RETRY=FALSE
     72  dopw1_GunWork=FALSE
     73  dopw1_GunHome=TRUE
@@ base line 68, backup line 82 @@
     82  do502PartClampOpen=TRUE
     84  WAIT FOR di466PartClampOpen
+    88  IF NUT_READY THEN
+    90  dopw1_BlowOff=FALSE
     91  dopw1_ReturnPin=FALSE
     92  dopw1_AdvancePin=TRUE
+    93  ELSE
+    95  dopw1_AdvancePin=FALSE
+    96  dopw1_ReturnPin=TRUE
+    97  dopw1_BlowOff=TRUE
+    98  ENDIF
    101  do503QFPAdvance=FALSE
    102  do504QFPReturn=TRUE
    104  WAIT FOR dipw1_SpearHome
    108  IF NOT NUT_READY THEN
-    87  dopw1_ReturnPin=FALSE
-    88  dopw1_AdvancePin=TRUE
-    89  dopw1_BlowOff=TRUE
+   111  WAIT SEC 1.0
    112  do504QFPReturn=FALSE
    113  do503QFPAdvance=TRUE
    115  WAIT FOR di470QFPAdvanced
+   117  QFP_NUT_LOADED=FALSE
+   122  dopw1_Nut1Intensify_Home=FALSE
+   123  dopw1_BlowOff=FALSE
+   124  dopw1_ReturnPin=FALSE
+   125  dopw1_AdvancePin=TRUE
    130  dopw1_StartFeed=TRUE
    131  dopw1_StartFeed=FALSE
@@ base line 108, backup line 138 @@
    138  do504QFPReturn=TRUE
    140  WAIT FOR dipw1_SpearHome
+   141  dopw1_Nut1Intensify_Home=TRUE
    142  ENDIF
    145  do499UpperPinRetract=FALSE
@@ base line 118, backup line 149 @@
    149  CL_GunPressureCmd=CL_GUN_PRESS_BASE
    155  dopw1_WeldInit=FALSE
-   123  dopw1_WeldContactEnable=FALSE
-   124  dopw1_WeldOnExternal=FALSE
    156  gdopw1_SpotNumber=0
+   160  IF NOT NUTCYCLE_ACTIVE THEN
    161  dopw1_StartFeed=FALSE
+   162  ENDIF
    163  dopw1_Nut1Intensify=FALSE
    164  dopw1_Nut1Intensify_Home=TRUE
    165  dopw1_BlowOff=FALSE
    167  CL_GunPressureCmd=CL_GUN_PRESS_BASE
-   136  dopw1_WeldContactEnable=TRUE
-   137  dopw1_WeldOnExternal=TRUE
-   140  WAIT FOR dipw1_Ready
+   172  PIN_SETTLE_WAIT()
    175  do502PartClampOpen=FALSE
```
_66 more lines: see diffs/KRC/R1/Program/Centerline/centerline_weld.src.diff_

### `KRC/R1/Program/Centerline/gun_open_check.dat`

changed, integrator program: 4 code line(s) removed, 26 added; 17 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Centerline/gun_open_check.dat.diff](diffs/KRC/R1/Program/Centerline/gun_open_check.dat.diff)

Attributes: -&ACCESS  RV; +&ACCESS RVO5; +&REL 25; &REL 2 -> &PARAM DISKPATH = KRC:\R1\Program\Centerline

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
-    15  DECL INT nGunOpenWaitMs=2000
-    18  DECL BOOL bGunAirCheck=FALSE
+    16  DECL GLOBAL INT nGunOpenWaitMs=2000
+    19  DECL GLOBAL BOOL bGunAirCheck=TRUE
     24  DECL GLOBAL INT nWaterFlowMin=150
     25  DECL GLOBAL INT nWaterFlowHyst=10
-    26  DECL BOOL bGunWaterCheck=TRUE
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

changed, integrator program: 4 code line(s) removed, 5 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1A.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1A.dat.diff)

Attributes: &REL 339 -> &REL 343; &COMMENT NUT1 -> &COMMENT 03-10-R1 PNW1 NUT 1 ST2

Data changes:

- XP8 (E6POS) re-taught: moved 71.4 mm, rotated up to 0.9 deg
- XP19 (E6POS) re-taught: moved 1.9 mm
- XP20 (E6POS) re-taught: moved 0.2 mm
- added 1 DEFDAT: style1app1opt1a
- added 1 PDAT: PPDAT1
- removed 1 DEFDAT: style1app1opt1A

Runtime values (left out of the code diff): LAST_BASIS: {POINT1[] "P0                      ",POI... -> {POINT1[] "P0                      ",POI...

```diff
@@ base line 7, backup line 7 @@
-     7  DEFDAT style1app1opt1A
+     7  DEFDAT style1app1opt1a
     10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
-    17  DECL E6POS XP20={X -3850.82104,Y -108.397034,Z -435.544800,A -178.432037,B 0.654220462,C -179.967712,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    17  DECL E6POS XP20={X -3850.82104,Y -108.397034,Z -435.788452,A -178.432037,B 0.654220343,C -179.967712,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     18  DECL FDAT FP20={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     28  DECL FDAT FPNW1={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
@@ base line 34, backup line 34 @@
     34  DECL FDAT FP0={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     35  DECL MODULEPARAM_T LAST_TP_PARAMS={PARAMS[] "NutWeld_CmdPos=Weld; NutWeld_Move=LIN; NutWeld_NutWeldDat=NutData1_7; NutWeld_NWGunNr=1; NutWeld_NWSpotNr=7; NutWeld_NWOffset=45; Kuka.MoveDataName=gAboveWeld; Kuka.VelocityPath=2; Kuka. [...]
-    36  DECL E6POS XP8={X -3704.29346,Y 1.10223198,Z -449.805786,A -178.368118,B 0.266879767,C 179.968445,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    36  DECL E6POS XP8={X -3747.39,Y 5.76858711,Z -393.029510,A -178.432297,B -0.654858768,C -179.985626,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     37  DECL FDAT FP8={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     38  DECL LDAT LCPDAT8={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
@@ base line 41, backup line 41 @@
     41  DECL LDAT LCPDAT17={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     42  DECL PDAT PPDAT18={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    43  DECL E6POS XP19={X -3851.81445,Y -107.010963,Z -442.857483,A -178.432037,B 0.654220223,C -179.967712,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    43  DECL E6POS XP19={X -3849.93530,Y -106.544395,Z -442.889893,A -178.432037,B 0.654220402,C -179.967712,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     44  DECL FDAT FP19={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     45  DECL LDAT LCPDAT18={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    46  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     47  ENDDAT
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt1A.src`

changed, integrator program: 11 code line(s) removed, 22 added; 24 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1A.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1A.src.diff)

Attributes: &REL 339 -> &REL 343; &COMMENT 03-10-R1 PNW1 NUT 1 ST1 -> &COMMENT 03-10-R1 PNW1 NUT 1 ST2

```diff
@@ base line 56, backup line 56 @@
     56  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
     57  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
-    62  WAIT FOR NUT_READY== TRUE
+    60  INTERRUPT DECL 23 WHEN CL_ClampOpen==FALSE DO GUN_OPEN_LOST()
+    61  INTERRUPT DECL 24 WHEN CL_PinRetracted==FALSE DO GUN_OPEN_LOST()
+    66  CT_NUT_WAIT(1)
     69  INTERRUPT ON 20
     70  INTERRUPT ON 21
     71  INTERRUPT ON 22
-    68  GUN_OPEN_CHECK()
+    72  INTERRUPT ON 23
+    73  INTERRUPT ON 24
+    75  PEDESTAL_CLEAR_CHECK()
     79  $BWDSTART=FALSE
     80  LDAT_ACT=LCPDAT8
@@ base line 94, backup line 101 @@
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
-   103  GUN_OPEN_CHECK()
+   125  INTERRUPT ON 23
+   126  INTERRUPT ON 24
+   128  PEDESTAL_CLEAR_CHECK()
    129  ENDIF
    133  $BWDSTART=FALSE
@@ base line 118, backup line 143 @@
    143  INTERRUPT OFF 21
    144  INTERRUPT OFF 22
+   145  INTERRUPT OFF 23
+   146  INTERRUPT OFF 24
    149  $BWDSTART=FALSE
-   123  LDAT_ACT=LCPDAT17
+   150  PDAT_ACT=PPDAT1
    151  FDAT_ACT=FP8
-   125  BAS(#CP_PARAMS,2)
-   126  LIN XP8 C_DIS C_DIS
-   133  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO Request_next_nut() PRIO= -1
-   135  $BWDSTART=FALSE
-   136  PDAT_ACT=PPDAT18
-   137  FDAT_ACT=FP0
    152  BAS(#PTP_PARAMS,100)
-   139  PTP XP0
+   153  PTP XP8 C_DIS
    161  END
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt1B.dat`

changed, integrator program: 3 code line(s) removed, 4 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1B.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1B.dat.diff)

Attributes: &REL 339 -> &REL 343; &COMMENT NUT1 -> &COMMENT 03-10-R1 PNW1 NUT 1 ST2

Data changes:

- XP8 (E6POS) re-taught: moved 71.4 mm, rotated up to 0.9 deg
- XP20 (E6POS) re-taught: moved 5.5 mm
- added 1 DEFDAT: style1app1opt1b
- added 1 PDAT: PPDAT1
- removed 1 DEFDAT: style1app1opt1B

Runtime values (left out of the code diff): LAST_BASIS: {POINT1[] "P0                      ",POI... -> {POINT1[] "P0                      ",POI...

```diff
@@ base line 7, backup line 7 @@
-     7  DEFDAT style1app1opt1B
+     7  DEFDAT style1app1opt1b
     10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
-    17  DECL E6POS XP20={X -3850.82104,Y -108.397034,Z -430.314789,A -178.432037,B 0.654220343,C -179.967712,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    17  DECL E6POS XP20={X -3850.82104,Y -108.397034,Z -435.788452,A -178.432037,B 0.654220343,C -179.967712,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     18  DECL FDAT FP20={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     28  DECL FDAT FPNW1={TOOL_NO 2,BASE_NO 1,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
@@ base line 34, backup line 34 @@
     34  DECL FDAT FP0={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     35  DECL MODULEPARAM_T LAST_TP_PARAMS={PARAMS[] "NutWeld_CmdPos=Weld; NutWeld_Move=LIN; NutWeld_NutWeldDat=NutData1_7; NutWeld_NWGunNr=1; NutWeld_NWSpotNr=7; NutWeld_NWOffset=45; Kuka.MoveDataName=gAboveWeld; Kuka.VelocityPath=2; Kuka. [...]
-    36  DECL E6POS XP8={X -3704.29346,Y 1.10223198,Z -449.805786,A -178.368118,B 0.266879767,C 179.968445,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    36  DECL E6POS XP8={X -3747.39,Y 5.76858711,Z -393.029510,A -178.432297,B -0.654858768,C -179.985626,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     37  DECL FDAT FP8={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     38  DECL LDAT LCPDAT8={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
@@ base line 44, backup line 44 @@
     44  DECL FDAT FP19={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     45  DECL LDAT LCPDAT18={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    46  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     47  ENDDAT
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt1B.src`

changed, integrator program: 11 code line(s) removed, 22 added; 22 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1B.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt1B.src.diff)

Attributes: &REL 339 -> &REL 343

```diff
@@ base line 56, backup line 56 @@
     56  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
     57  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
-    62  WAIT FOR NUT_READY== TRUE
+    60  INTERRUPT DECL 23 WHEN CL_ClampOpen==FALSE DO GUN_OPEN_LOST()
+    61  INTERRUPT DECL 24 WHEN CL_PinRetracted==FALSE DO GUN_OPEN_LOST()
+    66  CT_NUT_WAIT(1)
     69  INTERRUPT ON 20
     70  INTERRUPT ON 21
     71  INTERRUPT ON 22
-    68  GUN_OPEN_CHECK()
+    72  INTERRUPT ON 23
+    73  INTERRUPT ON 24
+    75  PEDESTAL_CLEAR_CHECK()
     79  $BWDSTART=FALSE
     80  LDAT_ACT=LCPDAT8
@@ base line 94, backup line 101 @@
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
-   103  GUN_OPEN_CHECK()
+   125  INTERRUPT ON 23
+   126  INTERRUPT ON 24
+   128  PEDESTAL_CLEAR_CHECK()
    129  ENDIF
    133  $BWDSTART=FALSE
@@ base line 118, backup line 143 @@
    143  INTERRUPT OFF 21
    144  INTERRUPT OFF 22
+   145  INTERRUPT OFF 23
+   146  INTERRUPT OFF 24
    149  $BWDSTART=FALSE
-   123  LDAT_ACT=LCPDAT17
+   150  PDAT_ACT=PPDAT1
    151  FDAT_ACT=FP8
-   125  BAS(#CP_PARAMS,2)
-   126  LIN XP8 C_DIS C_DIS
-   133  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO Request_next_nut() PRIO= -1
-   135  $BWDSTART=FALSE
-   136  PDAT_ACT=PPDAT18
-   137  FDAT_ACT=FP0
    152  BAS(#PTP_PARAMS,100)
-   139  PTP XP0
+   153  PTP XP8 C_DIS
    161  END
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt2A.dat`

changed, integrator program: 5 code line(s) removed, 6 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2A.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2A.dat.diff)

Attributes: &REL 246 -> &REL 252; &COMMENT GE4_002_GUN1 -> &COMMENT 03-10-R1 PNW1 NUT 2 ST2

Data changes:

- XP0 (E6POS) re-taught: moved 126.7 mm, rotated up to 1.7 deg
- XP05 (E6POS) re-taught: moved 60.9 mm, rotated up to 1.7 deg
- XP06 (E6POS) re-taught: moved 3.3 mm
- XP6 (E6POS) re-taught: moved 3.3 mm
- XP16 (E6POS) re-taught: moved 2.0 mm
- added 1 PDAT: PPDAT1

Runtime values (left out of the code diff): LAST_BASIS: {POINT1[] "P0                      ",POI... -> {POINT1[] "P0                      ",POI...

```diff
@@ base line 22, backup line 22 @@
     22  DECL FDAT FPnw1={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     24  DECL PDAT PPDAT0={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    25  DECL E6POS XP0={X -3694.69214,Y 46.1868858,Z -495.861603,A -178.336945,B 1.01745069,C 179.989838,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    25  DECL E6POS XP0={X -3747.39,Y 5.76903486,Z -387.973175,A -178.432297,B -0.654858828,C -179.985626,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     26  DECL FDAT FP0={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     27  DECL E6POS XP5={X -3700.01831,Y -153.317429,Z -426.154480,A -178.336502,B -1.01672721,C 179.960312,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     28  DECL FDAT FP5={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     29  DECL LDAT LCPDAT0={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    30  DECL E6POS XP6={X -3883.74512,Y -155.081940,Z -431.860352,A -178.336502,B -1.01672721,C 179.960312,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    30  DECL E6POS XP6={X -3882.34546,Y -153.988113,Z -434.603973,A -178.336502,B -1.01672721,C 179.960312,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     31  DECL FDAT FP6={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    32  DECL E6POS XP06={X -3878.33521,Y 42.6205063,Z -500.728149,A -178.336945,B 1.01745081,C 179.989838,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    32  DECL E6POS XP06={X -3876.85596,Y 41.5696564,Z -503.446716,A -178.336945,B 1.01745081,C 179.989838,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     33  DECL FDAT FP06={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    34  DECL E6POS XP05={X -3700.01831,Y -153.317429,Z -430.255676,A -178.336502,B -1.01672721,C 179.960312,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    34  DECL E6POS XP05={X -3741.15063,Y -108.396217,Z -430.732452,A -178.432037,B 0.654220343,C -179.967712,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     35  DECL FDAT Fp05={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     36  DECL LDAT LCPDAT6={VEL 2.00000,ACC 100.000,APO_DIST 2.00000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
@@ base line 38, backup line 38 @@
     38  DECL LDAT LCPDAT11={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     39  DECL LDAT LCPDAT14={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    40  DECL E6POS XP16={X -3884.30103,Y -154.162430,Z -439.919525,A -178.336502,B -1.01672733,C 179.960312,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    40  DECL E6POS XP16={X -3882.34546,Y -153.988113,Z -439.433533,A -178.336502,B -1.01672721,C 179.960312,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     41  DECL FDAT FP16={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     42  DECL LDAT LCPDAT15={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    43  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     44  ENDDAT
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt2A.src`

changed, integrator program: 16 code line(s) removed, 22 added; 26 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2A.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2A.src.diff)

Attributes: &REL 246 -> &REL 252; &COMMENT 03-10-R1 PNW1 NUT 2 ST1 -> &COMMENT 03-10-R1 PNW1 NUT 2 ST2

```diff
@@ base line 39, backup line 39 @@
     39  BAS(#PTP_PARAMS,100)
     40  PTP XP0 C_DIS
-    43  $BWDSTART=FALSE
-    44  LDAT_ACT=LCPDAT11
-    45  FDAT_ACT=FP5
-    46  BAS(#CP_PARAMS,2)
-    47  LIN XP5
     47  INTERRUPT DECL 20 WHEN CL_GunStrokePositionLPT<137000 DO GUN_OPEN_LOST()
     48  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
     49  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
-    59  WAIT FOR NEXT_NUT_READY==TRUE
+    52  INTERRUPT DECL 23 WHEN CL_ClampOpen==FALSE DO GUN_OPEN_LOST()
+    53  INTERRUPT DECL 24 WHEN CL_PinRetracted==FALSE DO GUN_OPEN_LOST()
+    56  CT_NUT_WAIT(2)
     59  INTERRUPT ON 20
     60  INTERRUPT ON 21
     61  INTERRUPT ON 22
-    65  GUN_OPEN_CHECK()
+    62  INTERRUPT ON 23
+    63  INTERRUPT ON 24
+    65  PEDESTAL_CLEAR_CHECK()
     68  $BWDSTART=FALSE
     69  LDAT_ACT=LCPDAT0
@@ base line 90, backup line 90 @@
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
-    99  GUN_OPEN_CHECK()
+   114  INTERRUPT ON 23
+   115  INTERRUPT ON 24
+   117  PEDESTAL_CLEAR_CHECK()
    118  ENDIF
    121  $BWDSTART=FALSE
@@ base line 113, backup line 131 @@
    131  INTERRUPT OFF 21
    132  INTERRUPT OFF 22
+   133  INTERRUPT OFF 23
+   134  INTERRUPT OFF 24
    136  $BWDSTART=FALSE
-   117  LDAT_ACT=LCPDAT14
+   137  PDAT_ACT=PPDAT1
    138  FDAT_ACT=FP05
-   119  BAS(#CP_PARAMS,2)
-   120  LIN XP05
-   127  TRIGGER WHEN DISTANCE = 1 DELAY = 0 DO Request_next_nut() PRIO= -1
-   129  $BWDSTART=FALSE
-   130  PDAT_ACT=PPDAT26
```
_5 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2A.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt2B.dat`

changed, integrator program: 5 code line(s) removed, 6 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2B.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2B.dat.diff)

Attributes: &REL 246 -> &REL 252; &COMMENT GE4_002_GUN1 -> &COMMENT 03-10-R1 PNW1 NUT 2 ST2

Data changes:

- XP0 (E6POS) re-taught: moved 126.7 mm, rotated up to 1.7 deg
- XP05 (E6POS) re-taught: moved 60.9 mm, rotated up to 1.7 deg
- XP06 (E6POS) re-taught: moved 3.3 mm
- XP6 (E6POS) re-taught: moved 3.3 mm
- added 1 DEFDAT: style1app1opt2b
- added 1 PDAT: PPDAT1
- removed 1 DEFDAT: style1app1opt2B

Runtime values (left out of the code diff): LAST_BASIS: {POINT1[] "P0                      ",POI... -> {POINT1[] "P0                      ",POI...

```diff
@@ base line 7, backup line 7 @@
-     7  DEFDAT style1app1opt2B
+     7  DEFDAT style1app1opt2b
     10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
     18  DECL NutWeld_SUGG_T LAST_NutWeld={POINT1[] "PNW2_SPOT3              ",POINT2[] "PNW0                    ",CP_PARAMS[] "CPDATNutWeld0           ",PTP_PARAMS[] "PDATNutWeld0            ",CONT[] "C_PTP                   ",CP_VEL[] "2  [...]
@@ base line 22, backup line 22 @@
     22  DECL FDAT FPnw1={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     24  DECL PDAT PPDAT0={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
-    25  DECL E6POS XP0={X -3694.69214,Y 46.1868858,Z -495.861603,A -178.336945,B 1.01745069,C 179.989838,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    25  DECL E6POS XP0={X -3747.39,Y 5.76903486,Z -387.973175,A -178.432297,B -0.654858828,C -179.985626,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     26  DECL FDAT FP0={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     27  DECL E6POS XP5={X -3700.01831,Y -153.317429,Z -426.154480,A -178.336502,B -1.01672721,C 179.960312,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     28  DECL FDAT FP5={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     29  DECL LDAT LCPDAT0={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    30  DECL E6POS XP6={X -3883.74512,Y -155.081940,Z -431.860352,A -178.336502,B -1.01672721,C 179.960312,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    30  DECL E6POS XP6={X -3882.34546,Y -153.988113,Z -434.603973,A -178.336502,B -1.01672721,C 179.960312,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     31  DECL FDAT FP6={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    32  DECL E6POS XP06={X -3878.33521,Y 42.6205063,Z -500.728149,A -178.336945,B 1.01745081,C 179.989838,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    32  DECL E6POS XP06={X -3876.85596,Y 41.5696564,Z -503.446716,A -178.336945,B 1.01745081,C 179.989838,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     33  DECL FDAT FP06={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    34  DECL E6POS XP05={X -3700.01831,Y -153.317429,Z -430.255676,A -178.336502,B -1.01672721,C 179.960312,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    34  DECL E6POS XP05={X -3741.15063,Y -108.396217,Z -430.732452,A -178.432037,B 0.654220343,C -179.967712,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     35  DECL FDAT Fp05={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     36  DECL LDAT LCPDAT6={VEL 2.00000,ACC 100.000,APO_DIST 2.00000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
@@ base line 41, backup line 41 @@
     41  DECL FDAT FP16={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     42  DECL LDAT LCPDAT15={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    43  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     44  ENDDAT
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt2B.src`

changed, integrator program: 16 code line(s) removed, 22 added; 24 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2B.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2B.src.diff)

Attributes: &REL 246 -> &REL 252

```diff
@@ base line 39, backup line 39 @@
     39  BAS(#PTP_PARAMS,100)
     40  PTP XP0 C_DIS
-    43  $BWDSTART=FALSE
-    44  LDAT_ACT=LCPDAT11
-    45  FDAT_ACT=FP5
-    46  BAS(#CP_PARAMS,2)
-    47  LIN XP5
     47  INTERRUPT DECL 20 WHEN CL_GunStrokePositionLPT<137000 DO GUN_OPEN_LOST()
     48  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
     49  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
-    59  WAIT FOR NEXT_NUT_READY==TRUE
+    52  INTERRUPT DECL 23 WHEN CL_ClampOpen==FALSE DO GUN_OPEN_LOST()
+    53  INTERRUPT DECL 24 WHEN CL_PinRetracted==FALSE DO GUN_OPEN_LOST()
+    56  CT_NUT_WAIT(2)
     59  INTERRUPT ON 20
     60  INTERRUPT ON 21
     61  INTERRUPT ON 22
-    65  GUN_OPEN_CHECK()
+    62  INTERRUPT ON 23
+    63  INTERRUPT ON 24
+    65  PEDESTAL_CLEAR_CHECK()
     68  $BWDSTART=FALSE
     69  LDAT_ACT=LCPDAT0
@@ base line 90, backup line 90 @@
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
-    99  GUN_OPEN_CHECK()
+   114  INTERRUPT ON 23
+   115  INTERRUPT ON 24
+   117  PEDESTAL_CLEAR_CHECK()
    118  ENDIF
    121  $BWDSTART=FALSE
@@ base line 113, backup line 131 @@
    131  INTERRUPT OFF 21
    132  INTERRUPT OFF 22
+   133  INTERRUPT OFF 23
+   134  INTERRUPT OFF 24
    136  $BWDSTART=FALSE
-   117  LDAT_ACT=LCPDAT14
+   137  PDAT_ACT=PPDAT1
    138  FDAT_ACT=FP05
-   119  BAS(#CP_PARAMS,2)
-   120  LIN XP05
-   127  TRIGGER WHEN DISTANCE = 1 DELAY = 0 DO Request_next_nut() PRIO= -1
-   129  $BWDSTART=FALSE
-   130  PDAT_ACT=PPDAT26
```
_5 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt2B.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt3A.dat`

changed, integrator program: 4 code line(s) removed, 6 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3A.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3A.dat.diff)

Attributes: &REL 227 -> &REL 234; &COMMENT GE4_003_GUN1 -> &COMMENT 03-10-R1 PNW1 NUT 3 ST2

Data changes:

- XP13 (E6POS) re-taught: moved 5.2 mm
- XP16 (E6POS) re-taught: moved 1.2 mm, rotated up to 0.4 deg
- XP17 (E6POS) re-taught: moved 5.2 mm
- XP20 (E6POS) re-taught: moved 101.2 mm, rotated up to 0.9 deg, S/T 2/2 -> 2/34 (ARM CONFIGURATION CHANGED)
- added 2 PDAT: PPDAT1, PPDAT2

Runtime values (left out of the code diff): LAST_BASIS: {POINT1[] "P18                     ",POI... -> {POINT1[] "P0                      ",POI...

```diff
@@ base line 7, backup line 7 @@
      7  DEFDAT style1app1opt3A
     10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
-    17  DECL E6POS XP20={X -3678.25781,Y -44.2650108,Z -442.362579,A -178.367340,B 0.267035842,C 179.968063,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    17  DECL E6POS XP20={X -3747.39,Y 5.76903486,Z -387.973175,A -178.432297,B -0.654858828,C -179.985626,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     18  DECL FDAT FP20={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     20  DECL FDAT FPNW1={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
@@ base line 26, backup line 26 @@
     26  DECL E6POS XP7={X -3596.62695,Y -2.77881479,Z -444.531586,A -178.368134,B 0.266892016,C 179.968369,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     27  DECL FDAT FP7={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    28  DECL E6POS XP13={X -3882.93384,Y -48.4484138,Z -446.836792,A -178.367340,B 0.267035872,C 179.968063,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    28  DECL E6POS XP13={X -3882.44,Y -49.6154175,Z -451.879456,A -178.367340,B 0.267035931,C 179.968063,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     29  DECL FDAT FP13={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     30  DECL LDAT LCPDAT4={VEL 2.00000,ACC 100.000,APO_DIST 2.00000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
@@ base line 32, backup line 32 @@
     32  DECL LDAT LCPDAT6={VEL 2.00000,ACC 100.000,APO_DIST 2.00000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
     33  DECL LDAT LCPDAT10={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    34  DECL E6POS XP16={X -3885.41455,Y -60.8571358,Z -438.795197,A -178.367233,B -0.684153676,C 179.983429,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    34  DECL E6POS XP16={X -3884.36157,Y -60.7767830,Z -438.167816,A -178.367172,B -0.266017556,C 179.960464,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     35  DECL FDAT FP16={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     36  DECL LDAT LCPDAT11={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    37  DECL E6POS XP17={X -3884.77832,Y -61.9626274,Z -428.770508,A -178.367172,B -0.266017497,C 179.960464,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    37  DECL E6POS XP17={X -3884.34131,Y -60.7792091,Z -433.814606,A -178.367172,B -0.266017556,C 179.960464,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     38  DECL FDAT FP17={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     39  DECL LDAT LCPDAT12={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    40  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    41  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     42  ENDDAT
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt3A.src`

changed, integrator program: 11 code line(s) removed, 27 added; 20 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3A.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3A.src.diff)

Attributes: &REL 227 -> &REL 234; &COMMENT 03-10-R1 PNW1 NUT 3 ST1 -> &COMMENT 03-10-R1 PNW1 NUT 3 ST2

```diff
@@ base line 12, backup line 12 @@
     12  BAS (#INITMOV,0 )
     37  $BWDSTART=FALSE
-    38  LDAT_ACT=LCPDAT6
+    38  PDAT_ACT=PPDAT1
     39  FDAT_ACT=FP20
-    40  BAS(#CP_PARAMS,2)
-    41  LIN XP20 C_DIS C_DIS
+    40  BAS(#PTP_PARAMS,100)
+    41  PTP XP20 C_DIS
     48  INTERRUPT DECL 20 WHEN CL_GunStrokePositionLPT<137000 DO GUN_OPEN_LOST()
     49  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
     50  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
-    53  WAIT FOR NEXT_NUT_READY==TRUE
+    53  INTERRUPT DECL 23 WHEN CL_ClampOpen==FALSE DO GUN_OPEN_LOST()
+    54  INTERRUPT DECL 24 WHEN CL_PinRetracted==FALSE DO GUN_OPEN_LOST()
+    57  CT_NUT_WAIT(3)
     60  INTERRUPT ON 20
     61  INTERRUPT ON 21
     62  INTERRUPT ON 22
-    59  GUN_OPEN_CHECK()
+    63  INTERRUPT ON 23
+    64  INTERRUPT ON 24
+    66  PEDESTAL_CLEAR_CHECK()
     69  $BWDSTART=FALSE
     70  LDAT_ACT=LCPDAT4
@@ base line 84, backup line 91 @@
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
-    93  GUN_OPEN_CHECK()
+   111  INTERRUPT ON 23
+   112  INTERRUPT ON 24
+   114  PEDESTAL_CLEAR_CHECK()
    115  ENDIF
    118  $BWDSTART=FALSE
@@ base line 107, backup line 128 @@
    128  INTERRUPT OFF 21
    129  INTERRUPT OFF 22
+   130  INTERRUPT OFF 23
+   131  INTERRUPT OFF 24
    133  $BWDSTART=FALSE
-   111  LDAT_ACT=LCPDAT10
+   134  PDAT_ACT=PPDAT2
    135  FDAT_ACT=FP20
-   113  BAS(#CP_PARAMS,2)
-   114  LIN XP20
+   136  BAS(#PTP_PARAMS,100)
+   137  PTP XP20 C_DIS
```
_8 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3A.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app1opt3B.dat`

changed, integrator program: 4 code line(s) removed, 6 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3B.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3B.dat.diff)

Attributes: &REL 227 -> &REL 234; &COMMENT GE4_003_GUN1 -> &COMMENT 03-10-R1 PNW1 NUT 3 ST2

Data changes:

- XP13 (E6POS) re-taught: moved 5.2 mm
- XP17 (E6POS) re-taught: moved 5.2 mm
- XP20 (E6POS) re-taught: moved 101.2 mm, rotated up to 0.9 deg, S/T 2/2 -> 2/34 (ARM CONFIGURATION CHANGED)
- added 1 DEFDAT: style1app1opt3b
- added 2 PDAT: PPDAT1, PPDAT2
- removed 1 DEFDAT: style1app1opt3B

Runtime values (left out of the code diff): LAST_BASIS: {POINT1[] "P18                     ",POI... -> {POINT1[] "P0                      ",POI...

```diff
@@ base line 7, backup line 7 @@
-     7  DEFDAT style1app1opt3B
+     7  DEFDAT style1app1opt3b
     10  EXT BAS (BAS_COMMAND :IN,REAL :IN )
-    17  DECL E6POS XP20={X -3678.25781,Y -44.2650108,Z -442.362579,A -178.367340,B 0.267035842,C 179.968063,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    17  DECL E6POS XP20={X -3747.39,Y 5.76903486,Z -387.973175,A -178.432297,B -0.654858828,C -179.985626,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     18  DECL FDAT FP20={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     20  DECL FDAT FPNW1={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
@@ base line 26, backup line 26 @@
     26  DECL E6POS XP7={X -3596.62695,Y -2.77881479,Z -444.531586,A -178.368134,B 0.266892016,C 179.968369,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     27  DECL FDAT FP7={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
-    28  DECL E6POS XP13={X -3882.93384,Y -48.4484138,Z -446.836792,A -178.367340,B 0.267035872,C 179.968063,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    28  DECL E6POS XP13={X -3882.44,Y -49.6154175,Z -451.879456,A -178.367340,B 0.267035931,C 179.968063,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     29  DECL FDAT FP13={TOOL_NO 1,BASE_NO 3,IPO_FRAME #TCP,POINT2[] " ",TQ_STATE FALSE}
     30  DECL LDAT LCPDAT4={VEL 2.00000,ACC 100.000,APO_DIST 2.00000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
@@ base line 35, backup line 35 @@
     35  DECL FDAT FP16={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     36  DECL LDAT LCPDAT11={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    37  DECL E6POS XP17={X -3884.77832,Y -61.9626274,Z -428.770508,A -178.367172,B -0.266017497,C 179.960464,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    37  DECL E6POS XP17={X -3884.34131,Y -60.7792091,Z -433.814606,A -178.367172,B -0.266017556,C 179.960464,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     38  DECL FDAT FP17={TOOL_NO 1,BASE_NO 3,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     39  DECL LDAT LCPDAT12={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
+    40  DECL PDAT PPDAT1={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
+    41  DECL PDAT PPDAT2={VEL 100.000,ACC 100.000,APO_DIST 100.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
     42  ENDDAT
```

### `KRC/R1/Program/StyleApps/Options/style1app1opt3B.src`

changed, integrator program: 11 code line(s) removed, 27 added; 18 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3B.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3B.src.diff)

Attributes: &REL 227 -> &REL 234

```diff
@@ base line 12, backup line 12 @@
     12  BAS (#INITMOV,0 )
     37  $BWDSTART=FALSE
-    38  LDAT_ACT=LCPDAT6
+    38  PDAT_ACT=PPDAT1
     39  FDAT_ACT=FP20
-    40  BAS(#CP_PARAMS,2)
-    41  LIN XP20 C_DIS C_DIS
+    40  BAS(#PTP_PARAMS,100)
+    41  PTP XP20 C_DIS
     48  INTERRUPT DECL 20 WHEN CL_GunStrokePositionLPT<137000 DO GUN_OPEN_LOST()
     49  INTERRUPT DECL 21 WHEN CL_GunStrokePositionLPT>142000 DO GUN_OPEN_LOST()
     50  INTERRUPT DECL 22 WHEN $PRO_STATE0<>#P_ACTIVE DO GUN_OPEN_LOST()
-    53  WAIT FOR NEXT_NUT_READY==TRUE
+    53  INTERRUPT DECL 23 WHEN CL_ClampOpen==FALSE DO GUN_OPEN_LOST()
+    54  INTERRUPT DECL 24 WHEN CL_PinRetracted==FALSE DO GUN_OPEN_LOST()
+    57  CT_NUT_WAIT(3)
     60  INTERRUPT ON 20
     61  INTERRUPT ON 21
     62  INTERRUPT ON 22
-    59  GUN_OPEN_CHECK()
+    63  INTERRUPT ON 23
+    64  INTERRUPT ON 24
+    66  PEDESTAL_CLEAR_CHECK()
     69  $BWDSTART=FALSE
     70  LDAT_ACT=LCPDAT4
@@ base line 84, backup line 91 @@
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
-    93  GUN_OPEN_CHECK()
+   111  INTERRUPT ON 23
+   112  INTERRUPT ON 24
+   114  PEDESTAL_CLEAR_CHECK()
    115  ENDIF
    118  $BWDSTART=FALSE
@@ base line 107, backup line 128 @@
    128  INTERRUPT OFF 21
    129  INTERRUPT OFF 22
+   130  INTERRUPT OFF 23
+   131  INTERRUPT OFF 24
    133  $BWDSTART=FALSE
-   111  LDAT_ACT=LCPDAT10
+   134  PDAT_ACT=PPDAT2
    135  FDAT_ACT=FP20
-   113  BAS(#CP_PARAMS,2)
-   114  LIN XP20
+   136  BAS(#PTP_PARAMS,100)
+   137  PTP XP20 C_DIS
```
_8 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app1opt3B.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app2opt1.dat`

changed, integrator program: 1 code line(s) removed, 1 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.dat.diff)

Attributes: -&REL 19; +&REL 29; +&COMMENT 03-10-R1 NUT CHECK SENSOR

Data changes:

- XP31 (E6POS) re-taught: moved 4.9 mm

```diff
@@ base line 27, backup line 28 @@
     28  DECL FDAT FP28={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     29  DECL LDAT LCPDAT15={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
-    29  DECL E6POS XP31={X -792.581726,Y -1863.81885,Z 1815.91077,A -104.762810,B 0.614705741,C 179.948196,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    30  DECL E6POS XP31={X -792.590820,Y -1863.87073,Z 1820.80676,A -104.762810,B 0.614705622,C 179.948196,S 2,T 34,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     31  DECL FDAT FP31={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     32  DECL LDAT LCPDAT16={VEL 2.00000,ACC 100.000,APO_DIST 100.000,APO_FAC 50.0000,AXIS_VEL 100.000,AXIS_ACC 100.000,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0000,GEAR_JERK 50.0000,EXAX_IGN 0}
```

### `KRC/R1/Program/StyleApps/Options/style1app2opt1.src`

changed, integrator program: 5 code line(s) removed, 42 added; 33 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.src.diff)

Attributes: &REL 19 -> &REL 29

```diff
@@ base line 11, backup line 11 @@
     11  INTERRUPT ON 3
     12  BAS (#INITMOV,0 )
-    41  AC_ApplicationCheck (1)
+    38  bscrapGE4=FALSE
     42  $BWDSTART=FALSE
     43  PDAT_ACT=PPDAT16
     44  FDAT_ACT=FP22
     45  BAS(#PTP_PARAMS,100)
-    50  PTP XP22
+    46  PTP XP22 C_DIS
+    56  AC_ApplicationCheck (1)
     61  $BWDSTART=FALSE
     62  LDAT_ACT=LCPDAT15
@@ base line 74, backup line 80 @@
     80  FDAT_ACT=FP31
     81  BAS(#PTP_PARAMS,100)
-    76  PTP XP31
+    82  PTP XP31 C_DIS
     87  $BWDSTART=FALSE
     88  LDAT_ACT=LCPDAT16
@@ base line 100, backup line 106 @@
    106  FDAT_ACT=FP38
    107  BAS(#PTP_PARAMS,100)
-   102  PTP XP38
+   108  PTP XP38 C_DIS
    113  $BWDSTART=FALSE
    114  LDAT_ACT=LCPDAT17
@@ base line 126, backup line 132 @@
    132  FDAT_ACT=FP37
    133  BAS(#PTP_PARAMS,100)
-   128  PTP XP37
+   134  PTP XP37 C_DIS
    144  IF NOT di004UseDryCycle THEN
    145  WAIT SEC 0.2
@@ base line 144, backup line 150 @@
    150  ELSE
    151  bscrapGE4=TRUE
+   153  IF NOT PARTPRESENT1 THEN
+   154  NUT_MISSING_MSG(1)
+   155  ENDIF
+   156  IF NOT PARTPRESENT2 THEN
+   157  NUT_MISSING_MSG(2)
+   158  ENDIF
+   159  IF NOT PARTPRESENT3 THEN
+   160  NUT_MISSING_MSG(3)
+   161  ENDIF
    162  ENDIF
    163  CASE 12
@@ base line 158, backup line 174 @@
    174  ENDIF
    180  END
+   182  DEF NUT_MISSING_MSG(nNut:IN)
+   185  DECL INT nNut
+   186  DECL KrlMsg_T Msg
+   187  DECL KrlMsgPar_T Par[3]
+   188  DECL KrlMsgOpt_T Opt
+   189  DECL INT nHandle
+   191  Msg.Modul[]="NutCheck"
+   192  Msg.Nr=30+nNut
```
_19 more lines: see diffs/KRC/R1/Program/StyleApps/Options/style1app2opt1.src.diff_

### `KRC/R1/Program/StyleApps/Options/style1app2opt2.dat`

changed, integrator program: 1 code line(s) removed, 1 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.dat.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.dat.diff)

Attributes: &REL 16 -> &REL 17; &COMMENT GE4_NutCHK -> &COMMENT 03-10-R1 NUT CHECK CAMERA

Data changes:

- added 1 DEFDAT: style1app2opt2
- removed 1 DEFDAT: Style1App2Opt2

```diff
@@ base line 6, backup line 6 @@
-     6  DEFDAT Style1App2Opt2
+     6  DEFDAT style1app2opt2
      9  EXT BAS (BAS_COMMAND :IN,REAL :IN )
     15  DECL BASIS_SUGG_T LAST_BASIS={POINT1[] "P0                      ",POINT2[] "P0                      ",CP_PARAMS[] "CPDAT0                  ",PTP_PARAMS[] "PDAT0                   ",CONT[] "                        ",CP_VEL[] "2.0    [...]
```

### `KRC/R1/Program/StyleApps/Options/style1app2opt2.src`

changed, integrator program: 2 code line(s) removed, 2 added; 2 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.src.diff](diffs/KRC/R1/Program/StyleApps/Options/style1app2opt2.src.diff)

Attributes: &REL 16 -> &REL 17

```diff
@@ base line 33, backup line 33 @@
     33  FDAT_ACT=FP6
     34  BAS(#PTP_PARAMS,100)
-    35  PTP XP6
+    35  PTP XP6 C_DIS
     40  $BWDSTART=FALSE
     41  LDAT_ACT=LCPDAT0
@@ base line 50, backup line 50 @@
     50  do080RepositionTooling1=TRUE
     53  WAIT FOR di080ToolRepositioned1
-    60  WAIT SEC 0.2
+    60  WAIT SEC 2.0
     61  SWITCH nOption
     62  CASE 1,2,7,8
```

### `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.dat`

changed, integrator program: 1 code line(s) removed, 1 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt1.dat.diff](diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt1.dat.diff)

Attributes: &REL 222 -> &REL 234; &COMMENT GE4_Conveyor -> &COMMENT 03-10-R1 DROP CONVEYOR

Data changes:

- XP2 (E6POS) re-taught: moved 200.5 mm, rotated up to 17.4 deg

Runtime values (left out of the code diff): LAST_BASIS: {POINT1[] "P10                     ",POI... -> {POINT1[] "P0                      ",POI...

```diff
@@ base line 18, backup line 18 @@
     18  DECL FDAT FAtDrop3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     19  DECL MODULEPARAM_T LAST_TP_PARAMS={PARAMS[] "AC_CmdZones=DropOff; AC_CmdParam=2; AC_ZoneRepo=True; AC_UseState=True; AC_Blending=False                               "}
-    20  DECL E6POS XP2={X -1471.65808,Y -890.400757,Z 672.790649,A 177.082932,B 4.31955290,C -0.298484206,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    20  DECL E6POS XP2={X -1279.37976,Y -897.098,Z 616.329468,A 176.629059,B 21.7134552,C -1.31570351,S 2,T 2,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     21  DECL FDAT FP2={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     22  DECL PDAT PPDAT7={VEL 100.000,ACC 100.000,APO_DIST 500.000,APO_MODE #CDIS,GEAR_JERK 50.0000,EXAX_IGN 0}
```

### `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src`

changed, integrator program: 9 code line(s) removed, 4 added; 22 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src.diff](diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src.diff)

Attributes: &REL 222 -> &REL 234

```diff
@@ base line 10, backup line 10 @@
     10  INTERRUPT ON 3
     11  BAS (#INITMOV,0 )
-    35  AC_DropOffCheck (1)
     32  TRIGGER WHEN DISTANCE=1 DELAY=0 DO do070ApplicationClear1=TRUE
     34  $BWDSTART=FALSE
@@ base line 47, backup line 37 @@
     37  BAS(#PTP_PARAMS,100)
     38  PTP XP5 C_DIS
-    51  $BWDSTART=FALSE
-    52  PDAT_ACT=PPDAT1
-    53  FDAT_ACT=FP1
-    54  BAS(#PTP_PARAMS,100)
-    55  PTP XP1
+    49  AC_DropOffCheck (1)
     53  $BWDSTART=FALSE
     54  LDAT_ACT=LCPDAT1
@@ base line 62, backup line 57 @@
     57  LIN XAtDrop3
     67  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
-    76  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254] )
-    80  $OUT[18]=FALSE
+    71  WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2 )
+    75  do018Part1InGripper=FALSE
     80  $BWDSTART=FALSE
     81  PDAT_ACT=PPDAT7
@@ base line 102, backup line 97 @@
     97  FDAT_ACT=FP3
     98  BAS(#PTP_PARAMS,100)
-   104  PTP XP3
+    99  PTP XP3 C_DIS
    108  AC_DropOff (1,True)
    113  $BWDSTART=FALSE
```

### `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src`

changed, integrator program: 4 code line(s) removed, 4 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src.diff](diffs/KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src.diff)

```diff
@@ base line 37, backup line 37 @@
     37  AC_DropOffCheck (2)
     43  CONTINUE
-    44  $OUT[249]=FALSE
+    44  do249Group1Home=FALSE
     47  CONTINUE
-    48  $OUT[250]=TRUE
+    48  do250Group1Work=TRUE
     53  $BWDSTART=FALSE
     54  PDAT_ACT=PPDAT25
@@ base line 145, backup line 145 @@
    145  BAS(#CP_PARAMS,2)
    146  LIN XP23
-   150  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254] )
+   150  WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2 )
    155  $BWDSTART=FALSE
    156  LDAT_ACT=LCPDAT4
@@ base line 158, backup line 158 @@
    158  BAS(#CP_PARAMS,2)
    159  LIN XP24
-   163  $OUT[18]=FALSE
+   163  do018Part1InGripper=FALSE
    167  $BWDSTART=FALSE
    168  LDAT_ACT=LCPDAT7
```

### `KRC/R1/Program/StylePicks/Options/style1pick1opt1.dat`

changed, integrator program: 1 code line(s) removed, 1 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1.dat.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1.dat.diff)

Attributes: &REL 52 -> &REL 53; &COMMENT St1_PICK_GE4 -> &COMMENT 03-10-R1 PICK ST1

Data changes:

- XAtPick3 (E6POS) re-taught: moved 0.5 mm

```diff
@@ base line 23, backup line 23 @@
     23  DECL E6POS XP10={X 1081.09485,Y -250.197342,Z 931.476,A -96.8303,B 37.9899406,C -15.7576666,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     24  DECL FDAT FP10={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
-    25  DECL E6POS XAtPick3={X 1206.28552,Y -208.912048,Z 214.158249,A -91.4409,B -0.232809141,C 0.168289974,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
+    25  DECL E6POS XAtPick3={X 1206.28552,Y -208.912048,Z 214.640366,A -91.4409,B -0.232809022,C 0.168290094,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
     26  DECL FDAT FAtPick3={TOOL_NO 1,BASE_NO 0,IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}
     27  DECL E6POS XP40={X 1206.28552,Y -208.912048,Z 630.625366,A -91.4409,B -0.232809082,C 0.168290034,S 2,T 3,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}
```

### `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src`

changed, integrator program: 3 code line(s) removed, 3 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1.src.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1.src.diff)

Attributes: &REL 52 -> &REL 53

```diff
@@ base line 11, backup line 11 @@
     11  BAS (#INITMOV,0 )
     32  AC_pickUPCheck (1)
-    37  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254])
+    37  WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2)
     46  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
     57  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO NUT_START=TRUE
@@ base line 102, backup line 102 @@
    102  GRPg_SetStateAndCheck(1, 2, 0.2, 1)
    108  IF NOT di004UseDryCycle THEN
-   111  WAIT FOR ( $IN[253] ) AND ( $IN[254] )
-   117  $OUT[18]=TRUE
+   111  WAIT FOR ( di253PartPresent1 ) AND ( di254PartPresent2 )
+   117  do018Part1InGripper=TRUE
    119  ENDIF
    123  $BWDSTART=FALSE
```

### `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src`

changed, integrator program: 3 code line(s) removed, 3 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src.diff)

```diff
@@ base line 11, backup line 11 @@
     11  BAS (#INITMOV,0 )
     33  AC_pickUPCheck (1)
-    38  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254])
+    38  WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2)
     47  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
     58  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO NUT_START=TRUE
@@ base line 103, backup line 103 @@
    103  GRPg_SetStateAndCheck(1, 2, 0.2, 1)
    109  IF NOT di004UseDryCycle THEN
-   112  WAIT FOR ( $IN[253] ) AND ( $IN[254] )
-   118  $OUT[18]=TRUE
+   112  WAIT FOR ( di253PartPresent1 ) AND ( di254PartPresent2 )
+   118  do018Part1InGripper=TRUE
    120  ENDIF
    124  $BWDSTART=FALSE
```

### `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src`

changed, integrator program: 5 code line(s) removed, 5 added; 14 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt2.src.diff](diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt2.src.diff)

Attributes: &REL 41 -> &REL 43

```diff
@@ base line 11, backup line 11 @@
     11  BAS (#INITMOV,0 )
     34  AC_pickUPCheck (2)
-    39  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254])
+    39  WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2)
     48  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
     59  TRIGGER WHEN DISTANCE = 0 DELAY = 0 DO NUT_START=TRUE
@@ base line 97, backup line 97 @@
     97  GRPg_SetStateAndCheck(1, 2, 0.2, 1)
    103  IF NOT di004UseDryCycle THEN
-   106  WAIT FOR ( $IN[253] ) AND ( $IN[254] )
-   112  $OUT[18]=TRUE
+   106  WAIT FOR ( di253PartPresent1 ) AND ( di254PartPresent2 )
+   112  do018Part1InGripper=TRUE
    114  ENDIF
    119  $BWDSTART=FALSE
@@ base line 121, backup line 121 @@
    121  FDAT_ACT=FP40
    122  BAS(#CP_PARAMS,2)
-   123  LIN XP40
+   123  LIN XP40 C_DIS C_DIS
    126  $BWDSTART=FALSE
    127  PDAT_ACT=PPDAT12
    128  FDAT_ACT=FP8
    129  BAS(#PTP_PARAMS,100)
-   130  PTP XP8
+   130  PTP XP8 C_DIS
    138  AC_pickUP (2,True)
    140  END
```

### `KRC/R1/Program/Styles/optiones/style1opt1.src`

added, integrator program: 0 code line(s) removed, 41 added; 31 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Styles/optiones/style1opt1.src.diff](diffs/KRC/R1/Program/Styles/optiones/style1opt1.src.diff)

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

### `KRC/R1/Program/Styles/optiones/style1opt10autorr.src`

added, integrator program: 0 code line(s) removed, 6 added; 19 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Styles/optiones/style1opt10autorr.src.diff](diffs/KRC/R1/Program/Styles/optiones/style1opt10autorr.src.diff)

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

### `KRC/R1/Program/Utilities/RejectGE4.src`

changed, integrator program: 4 code line(s) removed, 4 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Utilities/RejectGE4.src.diff](diffs/KRC/R1/Program/Utilities/RejectGE4.src.diff)

Attributes: &ACCESS RVO2 -> &ACCESS RVO1

```diff
@@ base line 9, backup line 9 @@
      9  INTERRUPT ON 3
     10  BAS (#INITMOV,0 )
-    30  $OUT[106]=TRUE
+    30  do106PartRejected=TRUE
     34  $BWDSTART=FALSE
     35  PDAT_ACT=PL
@@ base line 50, backup line 50 @@
     50  LIN XP23
     60  GRPg_SetStateAndCheck(1, 1, 0.2, 1)
-    64  WAIT FOR ( NOT $IN[253] ) AND ( NOT $IN[254] )
+    64  WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2 )
     69  $BWDSTART=FALSE
     70  PDAT_ACT=PPDAT29
@@ base line 72, backup line 72 @@
     72  BAS(#PTP_PARAMS,100)
     73  PTP XP24
-    77  $OUT[18]=FALSE
+    77  do018Part1InGripper=FALSE
     82  $BWDSTART=FALSE
     83  PDAT_ACT=PPDAT32
@@ base line 101, backup line 101 @@
    101  $H_POS=XHOME
    102  PTP XHOME
-   110  $OUT[106]=FALSE
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

changed, integrator program: 0 code line(s) removed, 15 added; 6 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Utilities/hometorepair.src.diff](diffs/KRC/R1/Program/Utilities/hometorepair.src.diff)

Attributes: &ACCESS RVP14 -> &ACCESS RVP3; &REL 3 -> &REL 12

```diff
@@ base line 34, backup line 34 @@
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

changed, integrator program: 0 code line(s) removed, 15 added; 6 comment/blank line change(s). Full diff: [diffs/KRC/R1/Program/Utilities/repairtohome.src.diff](diffs/KRC/R1/Program/Utilities/repairtohome.src.diff)

Attributes: &ACCESS RVP15 -> &ACCESS RVP4; &REL 3 -> &REL 10

```diff
@@ base line 30, backup line 30 @@
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

### `KRC/R1/System/$config.dat`

changed, integrator program: 5 code line(s) removed, 7 added; 8 comment/blank line change(s). Full diff: [diffs/KRC/R1/System/$config.dat.diff](diffs/KRC/R1/System/$config.dat.diff)

Attributes: &PARAM DISKPATH = KRC:\R1\System -> &PARAM DISKPATH = SYSTEM

Data changes:

- LOAD_A3_DATA (LOAD) re-taught: moved 0.0 mm
- CL_GUN_IN_WINDOW_TIME (INT): 300 -> 150
- CL_PIN_WELD_MAX (INT): 13500 -> 12200
- CL_PIN_WELD_MIN (INT): 10000 -> 11000
- added 1 BOOL: CL_WeldFault
- added 1 INT: CL_WELD_COMPLETE_TIMEOUT

Runtime values (left out of the code diff): CL_GunStrokePositionLPT: 139790 -> 139760; CL_WeldPinPosition: 27339 -> 27367

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
@@ base line 825, backup line 826 @@
    826  SIGNAL CL_BeaconBit3008 $OUT[3008]
    827  SIGNAL CL_BeaconBit3024 $OUT[3024]
-   833  DECL INT CL_PIN_WELD_MIN=10000
-   834  DECL INT CL_PIN_WELD_MAX=13500
+   836  DECL INT CL_PIN_WELD_MIN=11000
+   837  DECL INT CL_PIN_WELD_MAX=12200
    841  DECL INT CL_GUN_WELD_MIN=69000
    842  DECL INT CL_GUN_WELD_MAX=73000
    845  DECL INT CL_GUN_CLOSE_TIMEOUT=1000
-   843  DECL INT CL_GUN_IN_WINDOW_TIME=300
+   846  DECL INT CL_GUN_IN_WINDOW_TIME=150
    851  DECL INT CL_GUN_PRESS_BASE=405
    852  DECL INT CL_GUN_PRESS_WELD=1820
    853  DECL INT CL_GUN_PRESS_REST=39425
    855  DECL INT CL_WELD_PROGRAM=2
+   859  DECL BOOL CL_WeldFault=FALSE
+   860  DECL INT CL_WELD_COMPLETE_TIMEOUT=3000
    868  DECL BOOL NUT_START=FALSE
    873  DECL BOOL NUT_READY=TRUE
```

### `KRC/R1/System/sps.sub`

changed, integrator program: 1 code line(s) removed, 38 added; 45 comment/blank line change(s). Full diff: [diffs/KRC/R1/System/sps.sub.diff](diffs/KRC/R1/System/sps.sub.diff)

```diff
@@ base line 122, backup line 122 @@
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
@@ base line 143, backup line 152 @@
    152  ENDIF
    154  CL_WaterOk = dipw1_WaterOk
+   162  dopw1_LowLevel = CL_WeldFault OR dipw1_Fault
+   163  dopw1_LevelOk = NOT (CL_WeldFault OR dipw1_Fault)
    171  IF dopw1_LowLevel THEN
    172  CL_BeaconBit3008 = TRUE
@@ base line 160, backup line 178 @@
    178  IF dopw1_LevelOk THEN
    179  CL_BeaconBit3001 = TRUE
+   180  CL_BeaconBit3008 = TRUE
    181  CL_BeaconBit3024 = FALSE
    182  ENDIF
-   171  dopw1_StartWater=di013WaterEnable
+   192  dopw1_StartWater=di013WaterEnable AND NOT do091RobotReadyCapChange
+   198  do111Gun1ElectrodeChange=dipw1_EndOfStepper
+   200  IF ((dipw1_StepperWarning==FALSE) AND (dipw1_EndOfStepper==FALSE)) THEN
+   202  dopw1_StepperWarningPL=TRUE
+   203  dopw1_EndofStepperPL=FALSE
+   204  ELSE
+   205  IF ((dipw1_StepperWarning==TRUE) AND (dipw1_EndOfStepper==FALSE)) THEN
+   207  dopw1_StepperWarningPL=TRUE
+   208  dopw1_EndofStepperPL=TRUE
+   209  ELSE
+   210  IF (dipw1_EndOfStepper==TRUE) THEN
+   212  dopw1_StepperWarningPL=FALSE
+   213  dopw1_EndofStepperPL=TRUE
+   214  ENDIF
+   215  ENDIF
+   216  ENDIF
+   222  IF di004UseDryCycle THEN
+   223  dopw1_WeldContactEnable=FALSE
+   224  dopw1_WeldOnExternal=FALSE
+   225  ELSE
+   226  dopw1_WeldContactEnable=TRUE
+   227  dopw1_WeldOnExternal=TRUE
+   228  ENDIF
+   233  do046WeldMode=NOT di004UseDryCycle
+   237  do107Hopper1LowLevel= NOT dipw1_HopperLowLevel
+   238  do118Nut1Ready= (dipw1_Ready AND NOT dipw1_Fault)
+   239  do134Nut1Fault= (dipw1_Fault OR NOT dipw1_Ready)
+   240  do094AirOK= dipw1_AirOK
+   241  do013WaterIsOn = dipw1_WaterOk
    247  PRELOAD()
    253  ENDLOOP
```

### `KRC/R1/cell.src`

changed, integrator program: 1 code line(s) removed, 1 added; 0 comment/blank line change(s). Full diff: [diffs/KRC/R1/cell.src.diff](diffs/KRC/R1/cell.src.diff)

```diff
@@ base line 82, backup line 82 @@
     82  HomeCheck( )
     83  HomeToRepair( )
-    86  WAIT FOR ( $IN[8] )
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

### Runtime values only

A .dat keeps the last value the program wrote to each of its variables, and the inline-form editor keeps its suggestions (LAST_BASIS...): these files changed only in such values, nobody edited them.

| File | Values | Diff |
|---|---|---|
| `KRC/R1/Program/StylePicks/Options/style1pick1opt2.dat` | LAST_BASIS: {POINT1[] "P8                      ",POI... -> {POINT1[] "P0                      ",POI... | diffs/KRC/R1/Program/StylePicks/Options/style1pick1opt2.dat.diff |
| `KRC/R1/TP/AutomationCore/automationcoredata.dat` | nAutoCore_Handle: 10035 -> 10263; nCycleStart_Handle: 11564 -> 10553; nCycleTime: 50 -> 39; nCycTime_Handle: 11563 -> 10552; nLogOnlyMsg_Handle: 10032 -> 10136 | diffs/KRC/R1/TP/AutomationCore/automationcoredata.dat.diff |

### Comment-only changes

| File | Comment/blank line changes | Attributes | Diff |
|---|---|---|---|
| `KRC/R1/Mada/$machine.dat` | 0 | -&ACCESS  RV; -&PARAM VERSION = 1.0.0; -&PARAM DISKPATH = MADA; +&ACCESS RV$ | diffs/KRC/R1/Mada/$machine.dat.diff |
| `KRC/R1/Mada/$robcor.dat` | 0 | +&PARAM DISKPATH = MADA; -&PARAM DISKPATH = MADA | diffs/KRC/R1/Mada/$robcor.dat.diff |
| `KRC/R1/Program/Styles/style_1.dat` | 0 | &COMMENT GE4_002 -> &COMMENT 03-10-R1 STYLE 1 | diffs/KRC/R1/Program/Styles/style_1.dat.diff |
| `KRC/R1/Program/Utilities/closeandcheckallclamps.dat` | 0 | &ACCESS RVO1 -> &ACCESS RVO4; +&COMMENT 03-10-R1 CLOSE GRIPPER 1 | diffs/KRC/R1/Program/Utilities/closeandcheckallclamps.dat.diff |
| `KRC/R1/Program/Utilities/closeandcheckallclamps.src` | 0 | &ACCESS RVO1 -> &ACCESS RVO4 | diffs/KRC/R1/Program/Utilities/closeandcheckallclamps.src.diff |
| `KRC/R1/Program/Utilities/openandcheckallclamps.dat` | 0 | &ACCESS RVO1 -> &ACCESS RVO4; +&COMMENT 03-10-R1 OPEN GRIPPER 1 | diffs/KRC/R1/Program/Utilities/openandcheckallclamps.dat.diff |
| `KRC/R1/Program/Utilities/openandcheckallclamps.src` | 0 | &ACCESS RVO1 -> &ACCESS RVO4 | diffs/KRC/R1/Program/Utilities/openandcheckallclamps.src.diff |
| `KRC/R1/Program/Utilities/RejectGE4.dat` | 0 | &ACCESS RVO2 -> &ACCESS RVO1; +&COMMENT 03-10-R1 REJECT | diffs/KRC/R1/Program/Utilities/RejectGE4.dat.diff |
| `KRC/R1/Program/home.dat` | 0 | +&COMMENT 03-10-R1 MOVE HOME | diffs/KRC/R1/Program/home.dat.diff |
| `KRC/R1/Program/masref_user.dat` | 0 | &ACCESS RVO1 -> &ACCESS RVO4; &COMMENT Mastering Reference User Program -> &COMMENT 03-10-R1 MASTERING REF | diffs/KRC/R1/Program/masref_user.dat.diff |
| `KRC/R1/Program/masref_user.src` | 0 | &ACCESS RVO1 -> &ACCESS RVO4 | diffs/KRC/R1/Program/masref_user.src.diff |
| `KRC/R1/System/masref_main.dat` | 0 | &ACCESS RVO1 -> &ACCESS RVP1 | diffs/KRC/R1/System/masref_main.dat.diff |
| `KRC/R1/System/masref_main.src` | 0 | &ACCESS RVO1 -> &ACCESS RVP1 | diffs/KRC/R1/System/masref_main.src.diff |
| `KRC/R1/System/tm_bib.src` | 0 | &ACCESS R7 -> &ACCESS R5; &REL 953 -> &REL 962 | diffs/KRC/R1/System/tm_bib.src.diff |
| `KRC/R1/TP/AutomationCore/automationcoreroutines.dat` | 0 | -&ACCESS  R; -&PARAM DISKPATH = TP/AutomationCore; -&REL 11; +&ACCESS RO5 | diffs/KRC/R1/TP/AutomationCore/automationcoreroutines.dat.diff |
| `KRC/R1/TP/GripperSpotTech/grp_func.dat` | 0 | -&ACCESS  R; -&COMMENT GripperSpotTech package; -&PARAM DISKPATH = TP/GripperSpotTech; -&PARAM KUKATPGRP_VERSION = 4.0; -&REL 1; +&ACCESS R5 | diffs/KRC/R1/TP/GripperSpotTech/grp_func.dat.diff |
| `KRC/STEU/Mada/$machine.dat` | 0 | -&ACCESS RV$; +&ACCESS  RV; +&PARAM DISKPATH = MADA | diffs/KRC/STEU/Mada/$machine.dat.diff |

## Mechanical checks

### FAIL (10)

- `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src:74` [4 inline form consistency] ;FOLD OUT 18 'do018PartInGripper1' State=FALSE: 0 output assignments in the body, the form generates one
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src:42` [4 inline form consistency] ;FOLD OUT 249 'do249Group1Home' State=FALSE CONT: 0 output assignments in the body, the form generates one
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src:46` [4 inline form consistency] ;FOLD OUT 250 'do250Group1Work' State=TRUE CONT: 0 output assignments in the body, the form generates one
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src:162` [4 inline form consistency] ;FOLD OUT 18 'do018PartInGripper1' State=FALSE: 0 output assignments in the body, the form generates one
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src:116` [4 inline form consistency] ;FOLD OUT 18 'do018PartInGripper1' State=TRUE: 0 output assignments in the body, the form generates one
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src:117` [4 inline form consistency] ;FOLD OUT 18 'do018PartInGripper1' State=TRUE: 0 output assignments in the body, the form generates one
- `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src:111` [4 inline form consistency] ;FOLD OUT 18 'do018PartInGripper1' State=TRUE: 0 output assignments in the body, the form generates one
- `KRC/R1/Program/Utilities/RejectGE4.src:29` [4 inline form consistency] ;FOLD OUT 106 'do106PartRejeted' State=TRUE: 0 output assignments in the body, the form generates one
- `KRC/R1/Program/Utilities/RejectGE4.src:76` [4 inline form consistency] ;FOLD OUT 18 'do018PartInGripper1' State=FALSE: 0 output assignments in the body, the form generates one
- `KRC/R1/Program/Utilities/RejectGE4.src:109` [4 inline form consistency] ;FOLD OUT 106 'do106PartRejeted' State=FALSE: 0 output assignments in the body, the form generates one

### WARN (52)

- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:208` [8 I/O without signal comment] do501PartClampClose accessed with no comment naming it in the 4 lines above (C24): do501PartClampClose=FALSE
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:209` [8 I/O without signal comment] do502PartClampOpen accessed with no comment naming it in the 4 lines above (C24): do502PartClampOpen=TRUE
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:215` [8 I/O without signal comment] di466PartClampOpen accessed with no comment naming it in the 4 lines above (C24): IF NOT di466PartClampOpen THEN
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:217` [8 I/O without signal comment] $IN[466], $IN[467] accessed with no comment naming it in the 4 lines above (C24): Msg.Msg_txt[]="Part clamp not open ($IN[466] / $IN[467]) - robot waiti
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:220` [8 I/O without signal comment] di466PartClampOpen accessed with no comment naming it in the 4 lines above (C24): WAIT FOR di466PartClampOpen
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:225` [8 I/O without signal comment] do498UpperPinExtend accessed with no comment naming it in the 4 lines above (C24): do498UpperPinExtend=FALSE
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:226` [8 I/O without signal comment] do499UpperPinRetract accessed with no comment naming it in the 4 lines above (C24): do499UpperPinRetract=TRUE
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:322` [8 I/O without signal comment] dipw1_WeldComplete, dipw1_Fault accessed with no comment naming it in the 4 lines above (C24): WHILE (NOT dipw1_WeldComplete) AND (NOT dipw1_Fault) AND (nWaitMs<CL_W
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:328` [8 I/O without signal comment] dipw1_WeldComplete, dipw1_Fault accessed with no comment naming it in the 4 lines above (C24): IF dipw1_Fault OR (NOT dipw1_WeldComplete) THEN
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:331` [8 I/O without signal comment] dipw1_Fault accessed with no comment naming it in the 4 lines above (C24): IF dipw1_Fault THEN
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:333` [8 I/O without signal comment] $IN[485] accessed with no comment naming it in the 4 lines above (C24): Msg.Msg_txt[]="Bosch weld fault ($IN[485]) - nut weld NOT OK, red ligh
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:337` [8 I/O without signal comment] $IN[483] accessed with no comment naming it in the 4 lines above (C24): Msg.Msg_txt[]="Weld complete ($IN[483]) not received in %1 ms - red li
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:345` [8 I/O without signal comment] dipw1_WeldComplete accessed with no comment naming it in the 4 lines above (C24): IF NOT dipw1_WeldComplete THEN
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:347` [8 I/O without signal comment] $IN[483] accessed with no comment naming it in the 4 lines above (C24): Msg.Msg_txt[]="Robot waiting for weld complete $IN[483] from the Bosch
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:349` [8 I/O without signal comment] dipw1_WeldComplete accessed with no comment naming it in the 4 lines above (C24): WAIT FOR dipw1_WeldComplete
- `KRC/R1/Program/Centerline/PRELOAD.src:79` [8 I/O without signal comment] dipw1_SpearHome, di470QFPAdvanced accessed with no comment naming it in the 4 lines above (C24): IF QFP_NUT_LOADED AND (dipw1_SpearHome==TRUE) AND (di470QFPAdvanced==F
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
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src:163` [5 hand-typed line in inline form] hand-typed line inside inline form - lost on Touch Up (F32): do018Part1InGripper=FALSE
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src:117` [5 hand-typed line in inline form] hand-typed line inside inline form - lost on Touch Up (F32): do018Part1InGripper=TRUE
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src:118` [5 hand-typed line in inline form] hand-typed line inside inline form - lost on Touch Up (F32): do018Part1InGripper=TRUE
- `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src:112` [5 hand-typed line in inline form] hand-typed line inside inline form - lost on Touch Up (F32): do018Part1InGripper=TRUE
- `KRC/R1/Program/Utilities/RejectGE4.src:30` [5 hand-typed line in inline form] hand-typed line inside inline form - lost on Touch Up (F32): do106PartRejected=TRUE
- `KRC/R1/Program/Utilities/RejectGE4.src:77` [5 hand-typed line in inline form] hand-typed line inside inline form - lost on Touch Up (F32): do018Part1InGripper=FALSE
- `KRC/R1/Program/Utilities/RejectGE4.src:110` [5 hand-typed line in inline form] hand-typed line inside inline form - lost on Touch Up (F32): do106PartRejected=FALSE
- `KRC/R1/System/sps.sub:163` [8 I/O without signal comment] dipw1_Fault accessed with no comment naming it in the 4 lines above (C24): dopw1_LevelOk = NOT (CL_WeldFault OR dipw1_Fault)
- `KRC/R1/System/sps.sub:192` [8 I/O without signal comment] dopw1_StartWater, di013WaterEnable accessed with no comment naming it in the 4 lines above (C24): dopw1_StartWater=di013WaterEnable AND NOT do091RobotReadyCapChange
- `KRC/R1/System/sps.sub:200` [8 I/O without signal comment] dipw1_StepperWarning, dipw1_EndOfStepper accessed with no comment naming it in the 4 lines above (C24): IF ((dipw1_StepperWarning==FALSE) AND (dipw1_EndOfStepper==FALSE)) THE
- `KRC/R1/System/sps.sub:205` [8 I/O without signal comment] dipw1_StepperWarning, dipw1_EndOfStepper accessed with no comment naming it in the 4 lines above (C24): IF ((dipw1_StepperWarning==TRUE) AND (dipw1_EndOfStepper==FALSE)) THEN
- `KRC/R1/System/sps.sub:207` [8 I/O without signal comment] dopw1_StepperWarningPL accessed with no comment naming it in the 4 lines above (C24): dopw1_StepperWarningPL=TRUE
- `KRC/R1/System/sps.sub:208` [8 I/O without signal comment] dopw1_EndofStepperPL accessed with no comment naming it in the 4 lines above (C24): dopw1_EndofStepperPL=TRUE
- `KRC/R1/System/sps.sub:210` [8 I/O without signal comment] dipw1_EndOfStepper accessed with no comment naming it in the 4 lines above (C24): IF (dipw1_EndOfStepper==TRUE) THEN
- `KRC/R1/System/sps.sub:212` [8 I/O without signal comment] dopw1_StepperWarningPL accessed with no comment naming it in the 4 lines above (C24): dopw1_StepperWarningPL=FALSE
- `KRC/R1/System/sps.sub:213` [8 I/O without signal comment] dopw1_EndofStepperPL accessed with no comment naming it in the 4 lines above (C24): dopw1_EndofStepperPL=TRUE
- `KRC/R1/System/sps.sub:224` [8 I/O without signal comment] dopw1_WeldOnExternal accessed with no comment naming it in the 4 lines above (C24): dopw1_WeldOnExternal=FALSE
- `KRC/R1/System/sps.sub:226` [8 I/O without signal comment] dopw1_WeldContactEnable accessed with no comment naming it in the 4 lines above (C24): dopw1_WeldContactEnable=TRUE
- `KRC/R1/System/sps.sub:227` [8 I/O without signal comment] dopw1_WeldOnExternal accessed with no comment naming it in the 4 lines above (C24): dopw1_WeldOnExternal=TRUE
- `KRC/R1/System/sps.sub:237` [8 I/O without signal comment] dipw1_HopperLowLevel, do107Hopper1LowLevel accessed with no comment naming it in the 4 lines above (C24): do107Hopper1LowLevel= NOT dipw1_HopperLowLevel
- `KRC/R1/System/sps.sub:238` [8 I/O without signal comment] do118Nut1Ready, dipw1_Fault, dipw1_Ready accessed with no comment naming it in the 4 lines above (C24): do118Nut1Ready= (dipw1_Ready AND NOT dipw1_Fault)
- `KRC/R1/System/sps.sub:239` [8 I/O without signal comment] dipw1_Fault, do134Nut1Fault, dipw1_Ready accessed with no comment naming it in the 4 lines above (C24): do134Nut1Fault= (dipw1_Fault OR NOT dipw1_Ready)
- `KRC/R1/System/sps.sub:240` [8 I/O without signal comment] do094AirOK, dipw1_AirOK accessed with no comment naming it in the 4 lines above (C24): do094AirOK= dipw1_AirOK
- `KRC/R1/System/sps.sub:241` [8 I/O without signal comment] do013WaterIsOn accessed with no comment naming it in the 4 lines above (C24): do013WaterIsOn = dipw1_WaterOk

### INFO (19)

- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:220` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR di466PartClampOpen
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:239` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR (CL_WeldPinPosition>=nPinRetractMin) AND (CL_WeldPinPosition<
- `KRC/R1/Program/Centerline/GUN_OPEN_CHECK.src:286` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR (CL_WeldPinPosition>=CL_PIN_WELD_MIN) AND (CL_WeldPinPosition
- `KRC/R1/Program/StyleApps/Options/style1app1opt1A.src:113` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR NUT_READY==TRUE
- `KRC/R1/Program/StyleApps/Options/style1app1opt1B.src:113` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR NUT_READY==TRUE
- `KRC/R1/Program/StyleApps/Options/style1app1opt2A.src:102` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR NUT_READY==TRUE
- `KRC/R1/Program/StyleApps/Options/style1app1opt2B.src:102` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR NUT_READY==TRUE
- `KRC/R1/Program/StyleApps/Options/style1app1opt3A.src:103` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR NUT_READY==TRUE
- `KRC/R1/Program/StyleApps/Options/style1app1opt3B.src:103` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR NUT_READY==TRUE
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt1.src:71` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2 )
- `KRC/R1/Program/StyleDrops/Options/style1drop1opt2AutoRR.src:150` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2 )
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src:37` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2)
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1.src:111` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( di253PartPresent1 ) AND ( di254PartPresent2 )
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src:38` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2)
- `KRC/R1/Program/StylePicks/Options/style1pick1opt1AutoRR.src:112` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( di253PartPresent1 ) AND ( di254PartPresent2 )
- `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src:39` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2)
- `KRC/R1/Program/StylePicks/Options/style1pick1opt2.src:106` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( di253PartPresent1 ) AND ( di254PartPresent2 )
- `KRC/R1/Program/Utilities/RejectGE4.src:64` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( NOT di253PartPresent1 ) AND ( NOT di254PartPresent2 )
- `KRC/R1/cell.src:86` [10 fault handling] new WAIT FOR with no timeout ($TIMER) nearby (F15): WAIT FOR ( di008ReturnFromRepair )
