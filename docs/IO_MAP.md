# R10 I/O map — the labels used in program comments

Station **03-10-R1** (BMW-03-10-R1: line BMW G65, cell 03, operation 10,
robot R1), KUKA KRC4, KSS 8.3.29, robot serial 658424, WorkVisual project
`V431-03-10R1_v6Active_Centerline_18`.

Every program comment that describes an I/O action names the signal with
its address and the label in this table, for example

```
;GUN OPEN - SIGNALS $OUT[472] dopw1_GunWork OFF, $OUT[471] dopw1_GunHome ON
```

`tools/check_cleanup.py` refuses a comment that writes `$OUT[n] name` with a
signal name that is not declared at that address, so a comment cannot
silently name the wrong signal. The checker does not read this table; the
table is kept in step with the declarations by hand.

**Which name is the label.** The KRC4 often has two or three names on one
bit (AutomationCore `do471GunHome`, NutWeld `dopw1_GunHome`, a CenterLine
`CL_` alias). The label is chosen in this order:

1. the name the code itself uses for that bit, when it uses one;
2. for the pedestal (CenterLine projection nut welder = NutWeld "PW1"), the
   NutWeld `dipw1_`/`dopw1_` name, because the CenterLine programs use that
   family (`dopw1_WeldInit`, `dopw1_StartFeed`, ...);
3. otherwise the AutomationCore `diNNN`/`doNNN` name;
4. when the only declared names are `Spare`/`Reserved`, a description in
   parentheses. Since the office code changes (Gestamp review, G12) the
   pedestal bits that had only those names carry an AutomationCore name
   declared in `automationcoreroutines.dat` (`do503QFPAdvance`, ...); only
   `$OUT[500]` keeps `do500Reserved` (function unknown, F17).

**QFP** = the CenterLine nut feed slide (shuttle) that carries the nut from
the feeder to the lower pin. **LPT** = the Balluff BTL6 linear transducer on
the pedestal gun stroke.

The device names come from `EIPIODriver.xml` (same devices as R20); which bit
sits on which device follows from `KRC_IO.xml`. Confirm byte numbers in
WorkVisual before rewiring anything.

## PLC interface (EtherNet/IP adapter, cell PLC ⇄ robot, `$IN/$OUT[1..160]`)

| Address | Label | Meaning in this program |
|---|---|---|
| `$IN[4]` | `di004UseDryCycle` | PLC dry cycle: skips weld, nut-sensor checks, part-present waits, PRELOAD steps (not the camera request) |
| `$IN[5]` | `di005InitiateCycle` | PLC cycle start (cell.src) |
| `$IN[6]` | `di006RequestToEnter` | PLC request to enter; AutomationCore halts at the next taught point (bas.src TRIGGER `AC_PointArrival`) |
| `$IN[8]` | `di008ReturnFromRepair` | PLC permission to return from repair |
| `$IN[9]` | `di009GoToRepair` | PLC request: go to repair position |
| `$IN[21]` | `di021BrakeTestRequest` | PLC request: brake test |
| `$IN[22]` | `di022MstrRefRequest` | PLC request: mastering reference test |
| `$IN[33..37]` | `gdiStyle` | style number (only style 1 exists) |
| `$IN[38..45]` | `gdiOption` | option number: 1/2/7/8 production, 12 red rabbit (F02, F19) |
| `$IN[65]` | `di065PickupMachine1` | pick from station 1 |
| `$IN[66]` | `di066PickupMachine2` | pick from station 2 |
| `$IN[80]` | `di080ToolRepositioned1` | camera nut inspection done (acknowledge of `do080`) |
| `$IN[100]` | `di100CameraJudgmentOK` | camera result OK (renamed from the misspelt `di100CameraJudmentOK`, G15) |
| `$IN[101]` | `di101CameraJudgmentNG` | camera result NG (renamed from `di101CameraJudmentNG`) |
| `$OUT[5]` | `do005RobotInCycle` | robot in cycle (set by cell.src; reset by MaintainSystem, not by EndOfCycle, F46) |
| `$OUT[15]` | `do015WorkComplete` | work complete — **never set** on R10: EndOfCycle was edited (F46) |
| `$OUT[18]` | `do018Part1InGripper` | part in gripper, latched (the inline forms show the undeclared text `do018PartInGripper1`) |
| `$OUT[33..37]` | `gdoStyleAckn` | style acknowledge |
| `$OUT[38..45]` | `gdoOptionAckn` | option acknowledge |
| `$OUT[80]` | `do080RepositionTooling1` | camera nut inspection request (never reset by the program, only by MaintainSystem) |
| `$OUT[106]` | `do106PartRejected` | part rejected (renamed from `do106PartRejeted`, G15; the inline forms still show `do106PartRejeted` / `do106RemoveScrapParts`) |
| `$OUT[141]` | `do141RedRabbitFailed` | red rabbit test failed (F19) |
| `$OUT[142]` | `do142RedRabbitPassed` | red rabbit test passed (F19) |
| `$OUT[930]` | `do930MasterRefInProcess` | mastering reference running — left ON for good (F35); mirrors the adapter bit of `$OUT[111]` (F18) |

## EOAT 1 — SMC EX600 valve terminal (EtherNet/IP scanner, device `EOAT_SMC_EX600`)

GripperTech (`grp_data.dat`) has only **Gripper 1** active: outputs
`$OUT[249]` (OUT1) / `$OUT[250]` (OUT2), inputs `$IN[257]` / `$IN[258]`;
*OPEN* = 249 ON, 250 OFF, 257 ON, 258 OFF; *CLOSE* = the opposite. Grippers
2-4 are inactive (F31, F45).

| Address | Label | Meaning |
|---|---|---|
| `$OUT[249]` | `do249Group1Home` | gripper 1 OPEN valve |
| `$OUT[250]` | `do250Group1Work` | gripper 1 CLOSE valve |
| `$IN[253]` | `di253PartPresent1` | part present 1 |
| `$IN[254]` | `di254PartPresent2` | part present 2 |
| `$IN[257]` | `di257Cylinder1Home` | gripper 1 open switch |
| `$IN[258]` | `di258Cylinder1Work` | gripper 1 closed switch |
| `$OUT[121]` | `do121GripperFault` | gripper fault to the PLC (written inside the vendor GripperTech routines, C28) |

## Nut check station — Balluff BNI508 (device `SRU_BALLUF_BNI508`)

| Address | Label | Meaning |
|---|---|---|
| `$IN[227]` | `di227NutPresent1` | nut-present sensor; each of the three checks writes it to `PARTPRESENT1..3` (before the office changes: `NUT_PRESENT1` in `$config.dat` and `di227SensorCamera` in AutomationCore, F36) |

## CenterLine pedestal projection nut welder (PNW1)

Gun, blow-off, pin, clamp and QFP valves (`$OUT[471..472]`, `$OUT[494..496]`,
`$OUT[498..505]`) on the SMC EX260 manifold (device `EX260-SEN1_CENTERLINE`).
Switches, LPT and pin transducers, SV0500 water flow, the pressure regulator,
the outputs `$OUT[473]`, `$OUT[475..478]` and the KL50L2 beacon on device
`PED_CENTERLINE`. Weld timer on device `BOSCH_WELD_CONTROLLER`.

### Valves and outputs

| Address | Label | Meaning |
|---|---|---|
| `$OUT[471]` | `dopw1_GunHome` | weld gun OPEN valve |
| `$OUT[472]` | `dopw1_GunWork` | weld gun CLOSE valve |
| `$OUT[473]` | `dopw1_Nut1Intensify_Home` | intensify "home" output: ON at rest in CENTERLINE_WELD, OFF while intensifying (polarity to confirm, F34) |
| `$OUT[474]` | `dopw1_Nut1Intensify` | intensify command — **not mapped to any bus bit**, has no effect |
| `$OUT[475]` | `dopw1_StartWater` | cooling water on (forced ON every SPS cycle outside dry cycle, F09) |
| `$OUT[476]` | `dopw1_StartFeed` | nut feeder feed command |
| `$OUT[477]` | `dopw1_LevelOk` | hopper level OK, green light (AutomationCore names this bit `do477LowLevel`) |
| `$OUT[478]` | `dopw1_LowLevel` | hopper level low, red light (AutomationCore names this bit `do478LevelOk`) |
| `$OUT[494]` | `dopw1_BlowOff` | blow-off air (switched during nut feed and during intensify — physical function to confirm, F27) |
| `$OUT[495]` | `dopw1_AdvancePin` | lower (locating) pin ADVANCE / up |
| `$OUT[496]` | `dopw1_ReturnPin` | lower (locating) pin RETURN / down |
| `$OUT[498]` | `do498UpperPinExtend` | upper weld pin extend / forward (was `do498Reserved`) |
| `$OUT[499]` | `do499UpperPinRetract` | upper weld pin retract / return (was `do499Reserved`) |
| `$OUT[500]` | `do500Reserved` | function unknown — only ever set FALSE, in CENTERLINE_HOME and CENTERLINE_LOOP (F17) |
| `$OUT[501]` | `do501PartClampClose` | part clamp close (was `do501Reserved`) |
| `$OUT[502]` | `do502PartClampOpen` | part clamp open (was `do502Reserved`) |
| `$OUT[503]` | `do503QFPAdvance` | nut feed slide advance (was `do503Reserved`) |
| `$OUT[504]` | `do504QFPReturn` | nut feed slide return (was `do504Reserved`) |
| `$OUT[505]` | `do505QFPNutBlowOff` | blows the nut from the slide onto the lower pin (was `do505Reserved`) |
| `$OUT[506..521]` | `CL_GunPressureCmd` | SMC ITV pressure set-point; the bus swaps the two bytes (as on R20). The code writes 405 general, 1820 intensify (not swapped) and 39425 at the end (swapped 0.09 MPa) — **byte order to confirm on the regulator, F44** |
| `$OUT[3001]` | `CL_BeaconBit3001` | KL50L2 beacon, "green" bit written by sps.sub — **not mapped** on the bus (F29) |
| `$OUT[3008]` | `CL_BeaconBit3008` | KL50L2 beacon, byte 589 bit 0 ("red") |
| `$OUT[3024]` | `CL_BeaconBit3024` | KL50L2 beacon, byte 591 bit 0 (ON with red, OFF with green) |

### Switches, transducers and weld timer

| Address | Label | Meaning |
|---|---|---|
| `$IN[466]` | `di466PartClampOpen` | part clamp open switch (was `di466Reserved`; `di466Spare` still declared too) |
| `$IN[467]` | `di467PartClampClosed` | part clamp closed switch (was `di467Reserved`; `di467Spare` still declared too) |
| `$IN[470]` | `di470QFPAdvanced` | nut feed slide advanced switch (was `di470Reserved`; `di470Spare` still declared too) |
| `$IN[479]` | `dipw1_IntensfPresOk` | intensify pressure OK (waited for in CENTERLINE_WELD, no timeout) |
| `$IN[481]` | `dipw1_FeedComplt` | nut feed complete — on the bus, not read (F13, F25) |
| `$IN[482]` | `dipw1_SpearHome` | QFP returned (spear home) |
| `$IN[559..590]` | `CL_LPT_BYTE0..3` | LPT gun stroke position; sps.sub assembles `CL_GunStrokePositionLPT` from bytes 1..3 (F23) |
| `$IN[591..606]` | `CL_PIN_BYTE0..1` | upper pin position; sps.sub assembles `CL_WeldPinPosition` (never read) |
| `$IN[3000..3015]` | `SV0500_BYTE0..1` | SV0500 water flow; sps.sub assembles `SV0500_FLOW` (result thrown away, F09) |
| `$IN[483]` | `dipw1_WeldComplete` | Bosch: weld complete |
| `$IN[484]` | `dipw1_Ready` | Bosch: ready |
| `$OUT[481]` | `dopw1_WeldContactEnable` | Bosch: weld contactor enable |
| `$OUT[482]` | `dopw1_WeldOnExternal` | Bosch: weld on (external) |
| `$OUT[483]` | `dopw1_WeldInit` | Bosch: weld start |
| `$OUT[486..493]` | `gdopw1_SpotNumber` | Bosch: weld program number (production uses program **2**) |

LPT position windows used by CENTERLINE_WELD (comment table in the program):
gun retracted ≈ 139815, open check > 120000 (`CL_GUN_OPEN_MIN`); gun on the nut
69000..73000 (`CL_GUN_CLOSED_MIN..MAX`, office names; the older declared
`CL_GUN_WELD_MIN/MAX` = 65000..76000 are not used).

## AutomationCore handshake and service signals named in comments

These bits are driven or read by AutomationCore routines that the programs
call (`AC_PickUpCheck`, `AC_ApplicationCheck`, `AC_DropOffCheck`,
`MaintainSystem`, `EndOfCycle`), or only by modules that are not called. They
are labelled with their AutomationCore names.

| Address | Label | Meaning |
|---|---|---|
| `$IN[13]` | `di013WaterEnable` | PLC water enable — not used by sps.sub, which forces the water on (F09) |
| `$IN[15]` | `di015WorkCompleteAckn` | PLC acknowledges work complete — no longer waited for (F46) |
| `$IN[70]` | `di070ApplicationMachine1` | permission to enter application 1 (nut check / camera) |
| `$IN[75]` | `di075DropOffMachine1` | permission to enter drop-off 1 (conveyor) |
| `$IN[76]` | `di076DropOffMachine2` | permission to enter drop-off 2 (red rabbit) |
| `$IN[92..94]` | `di092Caps1areChanged` .. `di094Caps3areChanged` | PLC: electrodes of gun 1/2/3 changed (GunElectrodeChange) |
| `$IN[147]` | `di147SEOC` | PLC stop at end of cycle (MaintainSystem waits while it is ON) |
| `$OUT[4]` | `do004ProcessFault` | process fault to the PLC |
| `$OUT[7]` | `do007RobotAtPounce` | robot at pounce — written only by the disabled AutomationCore background (F12) |
| `$OUT[23]` | `do023PickClearTooling` | robot clear of the pick tooling (OFF while in a pick) |
| `$OUT[24]` | `do024ApplClrTooling` | robot clear of the application tooling |
| `$OUT[25]` | `do025DropClearTooling` | robot clear of the drop tooling |
| `$OUT[65]` | `do065PickupClear1` | robot clear of pick-up 1 (station 1) |
| `$OUT[66]` | `do066PickupClear2` | robot clear of pick-up 2 (station 2) |
| `$OUT[70]` | `do070ApplicationClear1` | robot clear of application 1 |
| `$OUT[75]` | `do075DropOffClear1` | robot clear of drop-off 1 |
| `$OUT[76]` | `do076DropOffClear2` | robot clear of drop-off 2 |
| `$OUT[91]` | `do091RobotReadyCapChange` | robot ready for electrode change (GunElectrodeChange) |
| `$OUT[92]`, `$OUT[93]`, `$OUT[95]` | `do092RobotCapChg1Cmplt`, `do093RobotCapChg2Cmplt`, `do095RobotCapChg3Cmplt` | electrode change of gun 1/2/3 complete |
| `$OUT[111..113]` | `do111Gun1ElectrodeChange` .. `do113Gun3ElectrodeChange` | electrode change due — written only by the disabled AutomationCore background (F12, F43); `$OUT[111]` shares its adapter bit with `do930` (F18) |
| `$OUT[485]` | `dopw1_StepperReset` | Bosch stepper reset after an electrode change (0.1 s pulse, F43) |
| `$OUT[523]`, `$OUT[571]` | `dopw2_StartWater`, `dopw3_StartWater` | water of NutWeld guns 2/3 — guns that do not exist; not mapped |
| `$OUT[533]`, `$OUT[581]` | `dopw2_StepperReset`, `dopw3_StepperReset` | stepper reset of guns 2/3 — not mapped |

## Mapped on the bus but never read by production code

`$IN[468]`, `$IN[469]` (CenterLine, unknown switches), `$IN[475]`
`dipw1_XtfmrTempOk`, `$IN[480]` `dipw1_HopperLowLevel`, `$IN[481]`
`dipw1_FeedComplt`, `$IN[485]` `dipw1_Fault` (AutomationCore calls it
`di485NoFaults` — opposite polarity names), `$IN[486..488]` Bosch stepper;
`$OUT[484]` `dopw1_FaultReset` is never pulsed. See F08, F09, F13, F34.

## Timers

| Timer | Owner | Use |
|---|---|---|
| `$TIMER[10..13]` | PRELOAD (submit interpreter) | step timers: feed 2000 ms, advance 500 ms, return 800 ms, blow-off 800 ms |
| `$TIMER[14..15]` | CENTERLINE_WELD (robot interpreter) | gun-closed check: 1000 ms timeout, 300 ms settle |
