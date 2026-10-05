# R10 — behaviour findings and Gestamp compliance

Station 03-10-R1 (BMW-03-10-R1), KUKA KRC4 KSS 8.3.29, robot serial 658424,
archive `v431_03_10_r1.zip` of 2026-10-02 22:15.

R10 runs the same operation as R20 (EOAT 1 picks the GE4 part from station 1
or 2, the part is presented to a CenterLine pedestal projection nut welder,
the nuts are checked with a sensor and a camera, the part goes to the
conveyor or to reject). The differences that matter: **three nuts** instead of
five (M6/M8 nut size is the only process difference), a different option
table (1/2/7/8 production, 12 red rabbit), GripperTech forms in the picks and
drops, nuts 2 and 3 wait for `NEXT_NUT_READY`, and several items that exist
only on this robot (F44, F46, F47 and others marked *R10*).

The findings keep the **numbers of the R20 list** where the problem is the
same, so the two robots can be compared line by line; a finding that does not
apply to R10 says so. F44-F47 are new on R10.

The comment cleanup in this repository changes no robot behaviour, and so it
fixes none of the items below. Each one needs an owner decision, and most
need a test on the cell. The `;CHECK:`, `;NOTE:` and `;WARNING:` comments in
the programs point here by number.

Gestamp's own program review of 2026-10-02 is answered in the section
[Gestamp program review](#gestamp-program-review-2026-10-02--bmw-03-10r1);
Calvin's open-issues list (2026-10-03) is verified point by point in
[Calvin's list](#calvins-open-issues-list-2026-10-03--verification-for-10r1).

Line numbers refer to the archive **as received** (first commit of this
repository, `22a98cc`), because the cleanup moved lines. Module names are
given so the place can be found in the cleaned files too.

**Severity.** *Critical*: a single plausible fault or operator action
leads to a collision or can injure a person. *High*: wrong part
disposition, equipment wear or damage over time, or the cell stops or
hangs. *Medium*: robustness or diagnosis. *Low*: hygiene.

## Summary

| ID | Sev. | Finding | Fix type |
|---|---|---|---|
| F01 | Critical | Robot drives the part into the pedestal before gun open, clamp open and QFP returned are confirmed | code |
| F02 | High | Options 2, 7 and 8 ignore the nut sensor: only the camera decides good or scrap | code + PLC info |
| F03 | High | `PARTPRESENT1..3` / `bscrapGE4` are not reset at cycle start and a missing nut never writes FALSE | code |
| F04 | High | Dry cycle hangs at the first weld: PRELOAD clears `NUT_READY` and never sets it | code |
| F05 | High | Dry cycle input re-read at every step: switching it mid-cycle drops a part-welded, uninspected part | code |
| F06 | High | Both or neither pick inputs: empty cycle; unknown style/option is silent or hangs | code |
| F07 | High | Gun-closed check: HALT as fault handling, timers not restarted after resume, no message | code |
| F08 | High | Bosch weld result not evaluated: weld complete is taken as success; fault input never read | code + Bosch I/O list |
| F09 | High | Water flow result is thrown away (`dipw1_WaterOk` TRUE in both branches); water output forced ON | code |
| F10 | High | No safe pedestal state on program cancel/reset | code |
| F11 | Critical | PRELOAD runs in the submit interpreter in every mode and drives pedestal valves on its own | code + safety review |
| F12 | High | AutomationCore and NutWeld background tasks are commented out: PLC status bits never update | Gestamp decision |
| F13 | Medium | PRELOAD has no step timeouts, never raises its fault flag, declares a nut ready on timers | code |
| F14 | Medium | `NUT_READY` never consumed after a weld; the preload depends on motion TRIGGERs | code |
| F15 | Medium | About 35 `WAIT FOR` on process inputs without timeout or message | code |
| F16 | Medium | Pedestal pin positions never verified; declared windows unused, other numbers in the code | code |
| F17 | Medium | Overlapping I/O declarations; pedestal bits named only Spare/Reserved | declarations |
| F18 | Medium | `KRC_IO.xml` maps `$OUT[820..979]` and `$IN[820..930]` onto the same PLC adapter bytes as `[1..160]` | WorkVisual |
| F19 | High | *R10:* the red rabbit cycle cannot produce a result and cannot release the part | code + decision |
| F20 | Medium | Reject path: no interlock for the reject location; Application 1 not released | code + PLC |
| F21 | Medium | Hidden AutomationCore inline-form parameters disagree with the calls | inline forms |
| F22 | Medium | Pedestal moves mix base and external-TCP modes; no weld presentation uses external TCP | re-teach |
| F23 | Low | *R10:* LPT position built from 3 bytes in another order than R20 | site check |
| F24 | Low | Nut weld retry path is dead | cleanup decision |
| F25 | Low | Fallback nut feed in CENTERLINE_WELD has a zero-length feed pulse | code |
| F26 | Low | Timer allocation `$TIMER[10..15]` undocumented in code | documentation |
| F27 | Low | Comments that contradicted the code — corrected; valve meanings to confirm | site check |
| F28 | Low | Nut sensor sampled on arrival, dwell placed after the sample | code |
| F29 | Low | KL50L2 beacon logic dead; one beacon bit not mapped | code |
| F30 | Low | GOTO structure in Style1Opt1 is load-bearing | keep |
| F31 | Medium | *R10:* GripperTech form parameters disagree with the calls; red-rabbit drop releases with gripper 3 (same I/O as gripper 1) | inline forms |
| F32 | Medium | TRIGGERs and statements hand-inserted inside inline-form folds are lost on Touch Up | procedure |
| F33 | Medium | HMI `GripperConfig.xml` out of sync with `grp_data.dat` | procedure |
| F34 | Low | CENTERLINE_HOME: `$OUT[473]` polarity and missing Bosch reset | code |
| F35 | Medium | *R10:* mastering reference leaves `$OUT[930]` ON for ever | code |
| F36 | Low | `$IN[227]` declared twice under different names | declarations |
| F37 | — | Intensify pressure not confirmed — **not applicable on R10** (the wait is active) | — |
| F38 | High | Nut-preload state not re-initialised at program start, reset or controller boot | code + cell test |
| F39 | Medium | Torque monitoring values at 0; load-data check only warns; tool 1 load hand-entered | machine data |
| F40 | Medium | Drops and reject open the gripper without confirming the part; red-rabbit drop moves before gripper-empty | code |
| F41 | Low | PRELOAD times, water-flow limit and fixed waits are literal numbers | code |
| F42 | Low | Software work envelopes off | decision |
| F43 | Medium | Electrode change: stepper reset by a 0.1 s pulse, PLC handshake does not close | code |
| F44 | High | *R10:* pressure set-point written in two byte orders (405/1820 vs 39425) | site check + code |
| F45 | Low | *R10:* clamp routines: grippers 2-4 disabled, only gripper 1 exists | — (cleanup) |
| F46 | Medium | *R10:* vendor EndOfCycle edited: Work Complete is never sent to the PLC | Gestamp decision |
| F47 | Medium | *R10:* brake-test path taught with tool 3 / base 1 named for 03-30-R1 | re-teach |
| F48 | High | *Audit 2026-10-05:* drop-off interlock moved after the approach to the conveyor (undone in the integrated version); AtDrop3 re-taught (kept) | code |
| F49 | High | *Audit 2026-10-05:* AutomationCore_BKG switched on and the vendor routine edited, no recorded decision | Gestamp decision |
| F50 | High | *Audit 2026-10-05 14:46:* application-1 permission (nut check / camera) checked after the robot reaches P22 | code |
| F51 | Low | *Audit 2026-10-05 14:46:* weld apps duplicated per pick station (A/B): every change must go into both | documentation |

Gestamp compliance items are at the end (C01–C28).

## Behaviour findings

### F01 — Critical — pedestal entry not confirmed

Before the approach LIN to each weld pose the three weld apps wait only for
the preload flag: `NUT_READY` in style1app1opt1 (line 37), `NEXT_NUT_READY` in
style1app1opt2 (line 36) and opt3 (line 30). PRELOAD sets those flags
(PRELOAD:153-157) after commanding gun open, upper pin retract and clamp open
with no feedback, and after a timer on the QFP return without reading
`$IN[482]`. CENTERLINE_WELD checks clamp open (`$IN[466]`) and QFP returned
(`$IN[482]`) only once the robot is already at the weld pose, and checks the
gun open (`CL_GunStrokePositionLPT > 120000`) only at the end. Approach speed
is 2 m/s.

*Scenario:* the gun valve sticks or loses air, or a stopped run of
CENTERLINE_LOOP left the gun or clamp closed. PRELOAD times out "open", the
flag goes TRUE and the robot drives the part and EOAT into a closed
electrode, clamp or advanced slide.

*Fix:* before each approach, wait with timeout and message for gun open
(LPT > 120000), clamp open (`$IN[466]`) and QFP returned
(`$IN[482] AND NOT $IN[470]`); make PRELOAD step 20 require `$IN[482]`.

*Programmer's gun interlock (2026-10-05, integrated), independent review:*
GUN_OPEN_CHECK and interrupts 20-22 are valid KRL and the integration is
faithful, but interrupts fire only on a FALSE→TRUE change: (1) after the weld
the gun is confirmed open inside CENTERLINE_WELD and the interrupts come back
on only after the clamp/QFP waits and the rest pressure — a gun that left the
range meanwhile is never caught; (2) on entry GUN_OPEN_CHECK checks the submit
only at its start, before the interrupts are on. *Fix:* INTERRUPT ON 20-22
before each GUN_OPEN_CHECK call. Also: after the operator acknowledges
GUN_OPEN_LOST the robot can wait with no message; monitoring goes off one point
before the robot is out (P20/P06/P17); a block selection past the INTERRUPT ON
skips the interlock; the open range is written twice (interrupts and .dat;
global variables are allowed in interrupt conditions, e.g. tm_bib.src). Clamp
open and QFP returned are still not checked.
*Integrated version (2026-10-05, from the 14:46 backup):* the interrupts go on
before each GUN_OPEN_CHECK, on entry and again after the weld, and GUN_OPEN_LOST
shows a state message after the acknowledgement. Still open: clamp and QFP,
monitoring off one point early, block selection, the range written twice.

### F02 — High — options 2, 7, 8 ignore the nut sensor

Style_1 sends options 1, 2, 7 and 8 to Style1Opt1 (style_1.src:18-25). The
nut sensor check (style1app2opt1:135-151) decides only `CASE 1` (sets
`bscrapGE4`) and `CASE 10` (red rabbit outputs); there is no `CASE 2/7/8` and
no `DEFAULT`, so for options 2, 7 and 8 the sensor result is never used and
`bscrapGE4` keeps its last value. The camera check (style1app2opt2:42-48) has
no option switch: it sets `bscrapGE4` FALSE on OK/not-NG and TRUE on not-OK/NG;
any other combination leaves it unchanged. `nOption` is a bit mask (GetOptions);
2, 7 and 8 are other bit combinations.

*Scenario:* PLC sends option 2, nut 3 is missing, the sensor sees it, nothing
evaluates it; if the camera misses it or answers neither OK nor NG, the part
goes to the good conveyor.

*Fix:* evaluate on the option bit or add the cases; set `bscrapGE4 = TRUE` at
the start of each inspection and clear it only on an explicit pass; fault on
an unknown option. *Ask the PLC programmer which options production sends.*

### F03 — High — inspection flags not reset

`PARTPRESENT1..3` are persistent `$config.dat` globals that the nut check
only ever sets TRUE (style1app2opt1:50-52, 81-83, 112-114). They are cleared at
the end of Style1Opt1 (lines 59-61), of RejectGE4 and of the red-rabbit drop —
never at cycle start. `bscrapGE4` is written only by the option-1 sensor
result, the camera result and RejectGE4 (FALSE).

*Scenario:* a cycle passes the nut check, stops at the camera handshake, is
cancelled and restarted with a new part missing nut 2: `PARTPRESENT2` is
still TRUE and the sensor gate passes.

*Fix:* clear `PARTPRESENT1..3` and set `bscrapGE4 = TRUE` at cycle start;
assign each flag from the sensor (`PARTPRESENTn = NUT_PRESENT1`).
*Office (G13):* each check now writes the sensor value (TRUE or FALSE); the
start-of-cycle reset is still to do.

### F04 — High — dry cycle deadlock

The picks set `NUT_STAR` by TRIGGER at P12 / P10 whether or not dry cycle is
on. PRELOAD (lines 5-24) then sets `NUT_READY = FALSE`, but its step machine
is gated by `NOT di004UseDryCycle` (line 26), so it never sets `NUT_READY`
again. Nut 1 waits for `NUT_READY` (style1app1opt1:37) before its own
dry-cycle branch; nuts 2 and 3 wait for `NEXT_NUT_READY`, which no preload
sets either.

*Scenario:* PLC selects dry cycle and starts: the robot waits forever at the
first weld app, with no message, "in cycle". *Verify on the robot.*

*Fix:* in dry cycle, do not start a preload and set the flags, or move the
waits inside the non-dry branch.

### F05 — High — dry cycle sampled at every step

`di004UseDryCycle` is read separately in the picks, in each weld app, in the
three nut-check blocks and the decision, in PRELOAD and in sps.sub. The
camera check has no dry-cycle test at all. In dry cycle the sensor decision
leaves `bscrapGE4` untouched.

*Scenario:* nuts 1 and 2 are welded; dry cycle is switched on before the
robot reaches the nut-3 weld pose (after the nut-3 preload finished); nut 3
is skipped and, if the camera answers OK, a 2-nut part is dropped as good.

*Fix:* latch the dry-cycle state once at cycle start; in dry cycle require an
empty gripper or force the part to reject.

### F06 — High — empty or silent cycles

Style1Opt1 picks station 1 only on `di065 AND NOT di066`, station 2 only on
the inverse. Both or neither TRUE: nothing runs, the flags are cleared and
the cycle ends. cell.src has an empty `DEFAULT` for styles other than 1.
Style_1 answers an unknown option with `WAIT FOR FALSE` — an endless wait
with no message.

*Fix:* fault (AutomationCore message + `do004ProcessFault`) instead of the
silent defaults; wait with a message for exactly one pick permission.

### F07 — High — gun-closed check

CENTERLINE_WELD starts `$TIMER[14]` (1000 ms timeout) and `$TIMER[15]`
(300 ms settle) at lines 126-132 and checks the LPT window 69000..73000. On
timeout it stops and zeroes both timers, executes `HALT` (line 162) and jumps
back to the check — without restarting either timer. After resume the
timeout can never fire again, and if the LPT is already in the window the
settle timer is stopped at 0, so the busy loop spins forever. No message
names the fault.

*Fix:* restart the timers, or rewrite as a `WAIT FOR` with timeout; replace
the `HALT` by a dialog (no nut / double nut / gun not closed) with Retry and
an Abort that opens gun and clamp.
*Office (G11):* the check is a LOOP/EXIT and both timers restart after the
HALT, so a second timeout is possible. The dialog is still to do.

### F08 — High — weld result not evaluated

The weld sets `dopw1_WeldInit` (line 197), waits only for
`dipw1_WeldComplete` (line 199) and continues. `$IN[485]` is never read by
active code; its two names disagree (`dipw1_Fault` in NutWeld, `di485NoFaults`
in AutomationCore). The feed-complete wait (line 70) is commented out. The old
CENTERLINE_WELD1 (deleted by the cleanup: unmapped AutomationCore Bosch
signals and the R20 LPT window) waited for complete-or-fault. The later checks
test nut presence, not weld quality.

*Fix:* wait for complete OR fault with a timeout; on fault release pressure,
open the gun, scrap the part, raise a message. Confirm the polarity of
`$IN[485]` on the Bosch I/O list.

### F09 — High — water flow and water output

sps.sub computes `SV0500_FLOW` and `CL_WaterOK = (SV0500_FLOW > 1230)` but
sets the BOOL `dipw1_WaterOk` (the integrator turned that NutWeld signal into
a variable) to **TRUE in both branches** (sps.sub:84 and 87): the water flow
result is thrown away. Nothing in the weld path reads either one, nor the
transformer temperature `$IN[475]`. The threshold is `> 1230` while the old
comment said "1230 = water OK". sps.sub (line 110) sets `$OUT[475]`
`dopw1_StartWater` TRUE every cycle outside dry cycle, never clears it,
ignores `di013WaterEnable`, and overrides the water-off in CENTERLINE_HOME
and GunElectrodeChange.

*Fix:* require water flow (and transformer temperature) OK before
`dopw1_WeldInit`; gate the water output on `di013WaterEnable`; review the
threshold; write `dipw1_WaterOk` FALSE in the low-flow branch.

### F10 — High — no safe state on cancel

The only program-reset hook (sps.sub interrupt 91, `RESET_OUT`) clears PGNO
bits. Nothing resets clamp, gun, pressure word, intensify, blow-off, weld
start or contactor enable when a program is cancelled. On restart, the
AutomationCore HomeCheck dialog can move PTP HOME in T1.

*Scenario:* the weld hangs, the operator cancels and restarts: the part
stays clamped in the closed gun, and HOME pulls the gripper against it. If
the Bosch timer is reset while `WeldInit` is still high, a weld can start
while people handle the part.

*Fix:* a reset routine that drives the pedestal safe (weld start and
contactor off, general pressure, gun and clamp open); block HOME while the
clamp or gun is closed.

### F11 — Critical (pending safety review) — PRELOAD in the submit interpreter

sps.sub calls PRELOAD every SPS cycle in every mode (line 113). Once
`NUT_STAR` is set (by a motion TRIGGER, which also fires when stepping in
T1), PRELOAD writes feed, QFP, gun, pins, clamp and blow-off valves on its
own. The robot programs write the same outputs. Neither side checks the
other; in normal automatic flow only the `NUT_READY` / `NEXT_NUT_READY`
handshake keeps them apart. `NUT_STAR` is consumed only when no preload is
active, so a request during a preload is queued and starts a second preload
right after the first.

*Scenario:* in T1 an operator steps a pick past P12 and walks to the
pedestal: PRELOAD feeds, opens gun and clamp, moves the slide and pins over
about 4 s with no enabling switch held. Or CENTERLINE_HOME tries to return
the QFP while a stuck PRELOAD keeps advancing it.

*Fix:* one owner for the pedestal; gate PRELOAD on automatic external,
`$MOVE_ENABLE` and a robot-side release; let the manual programs abort or
wait for PRELOAD. *Needs the safety review: is pedestal air cut when the
gate is open?*

### F12 — High — background tasks disabled

`NutWeld_BKG ( )` and `AutomationCore_BKG ( )` are commented out in sps.sub
(lines 59, 62). Never written therefore: brake test due (`do021`), mastering
due (`do022`), battery alarm (`do006`), robot at pounce (`do007`, needed by
HomeCheck), electrode change due (`do111..113`, which cell.src tests — so
GunElectrodeChange never runs, F43), weld mode, bus-node OK bits, speed not
100 %, `doCriticalWZ` for request to enter, hopper level. The AutomationCore
edit inside `bas.src` still halts every PTP/LIN at the next point when the PLC
raises `di006RequestToEnter`, but `doCriticalWZ` stays FALSE, so the PLC sees
"entry allowed" while PRELOAD or a running CENTERLINE_WELD keep driving the
pedestal.

*Fix:* decide with Gestamp whether the background task is mandatory. If it
is re-enabled, first remove its weld-enable writes that fight
CENTERLINE_WELD and its water-on write (`$OUT[475]`); fix F35 first
(`$OUT[930]` stuck ON would block every request to enter). Otherwise
reproduce the required status bits in sps.sub.

### F13 — Medium — PRELOAD robustness

Steps 0 and 10 wait silently on the QFP switches with no time limit (step 20
runs on timers only). `NUT_PRELOAD_FAULT` is never set TRUE. `NUT_READY` is set
after fixed times (2000 ms feed at line 47, 500 ms after advance, 800 ms
blow-off, 800 ms after the return command); `$IN[481] dipw1_FeedComplt` (on the
bus) and `dipw1_HopperLowLevel` are not read. *Fix:* step timeouts that raise
the fault and a message; require feed complete and hopper level before
`NUT_READY`; weld apps wait for ready OR fault.
Calvin rates this High (#6). We keep Medium: a missing nut lets the gun close
past the 69000..73000 window, so the gun-closed check stops the cycle (F07)
instead of welding an empty pin — the cell stops, the part is not wrong.

### F14 — Medium — nut state

`NUT_READY` means "nut loaded" but is cleared only when PRELOAD accepts a new
request or on the gun timeout, never when a weld consumes the nut. The next
nut is requested only by motion TRIGGERs (pick P12/P10, end of apps 1 and 2).
A cancelled cycle can leave a nut on the pin and the next pick feeds a second
one (double nut); a skipped pick TRIGGER lets nut 1 pass on a stale TRUE with
no nut fed — only the LPT window (F07) then stands between that and a weld
without a nut. The red-rabbit pick also starts a preload although no weld
follows. *Fix:* clear `NUT_READY` after the weld; check the pin is empty
before feeding; request the next nut in line, not only by TRIGGER.

### F15 — Medium — unsupervised waits

Bosch ready/complete, intensify pressure, LPT windows, gun open, clamp
open/closed, QFP advanced/returned, `NUT_READY`/`NEXT_NUT_READY`, the camera
handshake and the gripper-empty / part-present waits are all bare
`WAIT FOR`. The AutomationCore idiom (`SetWaitingMessage`) is not used.
*Fix:* a wait helper with timeout, `do004ProcessFault` and a message naming
the signal; in the pedestal the abort path opens gun and clamp.

### F16 — Medium — pin positions

sps.sub assembles `CL_WeldPinPosition` and nothing reads it.
`CL_PIN_WELD_MIN/MAX` (10000..13500) and `CL_GUN_WELD_MIN/MAX`
(65000..76000) are declared and unused; CENTERLINE_WELD hard-codes the
narrower 69000..73000 and `> 120000`. At the end of the weld the upper pin is
commanded back (0.2 s after the gun is seen open) without confirmation.
*Fix:* check the pin at weld position before weld start and retracted
before withdrawing; use the declared constants.
*Office (G16):* the gun windows are named constants: `CL_GUN_WELD_MIN/MAX`
now hold 69000..73000, the window the code always checked (they were declared
65000..76000 and unused). The open limit `> 120000` was replaced by the
programmer's GUN_OPEN_CHECK range 137000..142000 (F01, audit 2026-10-05); the
pin checks are still to do.

### F17 — Medium — overlapping declarations

`CL_GunPressureCmd $OUT[506..521]` covers AutomationCore `do512..do521` and
NutWeld `dopw2_*` names; `CL_LPT_BYTE0..3 $IN[559..590]` covers `dipw3_*`
and `di561..di590`; `CL_PIN_BYTE0/1 $IN[591..606]` covers `aiNutSensorPW3`.
Guns 2 and 3 do not exist on this robot. `$IN[466..470]` carry two
AutomationCore names each (`Spare` and `Reserved`); the pedestal valves
`$OUT[498..505]` have only `Reserved` names, so the programs write them as
literal `$OUT[n]`. `$OUT[477]`/`$OUT[478]` are named the other way round by
NutWeld (`LevelOk`/`LowLevel`) and AutomationCore (`LowLevel`/`LevelOk`).
*Fix:* declare AutomationCore-style names for the pedestal bits, mark the
gun-2/3 names retired, then replace the literal addresses.
*Office (G12):* `$IN[466]`, `$IN[467]`, `$IN[470]`, `$OUT[498]`, `$OUT[499]`
and `$OUT[501..505]` have AutomationCore names and the pedestal code uses
names only. Still open: retire the overlapping gun 2/3 names, identify
`$OUT[500]` (`do500Reserved`).

### F18 — Medium — adapter mapped twice

Same as R20: `KRC_IO.xml` maps `$OUT[820..979]` onto the same 20 adapter
bytes as `$OUT[1..160]`, and `$IN[820..930]` onto `$IN[1..111]` (plus
`$IN[973..979]`). So `do930MasterRefInProcess` lands on the PLC bit of
`$OUT[111]` (`do111Gun1ElectrodeChange`) and `di823ToolIDBit0` is physically
`$IN[4]` `di004UseDryCycle`. *Fix:* check the intended adapter assembly in
WorkVisual and agree the PLC tag map with Gestamp.

### F19 — High — red rabbit cannot work (R10)

Style_1 runs the red rabbit as **option 12** (Style1Opt10AutoRR). That cycle
calls the *production* nut check and camera check (the AutoRR copies existed
but nothing called them; the cleanup deleted them). The nut check sets the
red-rabbit outputs only for `CASE 10`, so with option 12 neither
`do141RedRabbitFailed` nor `do142RedRabbitPassed` is ever set; the camera
check only writes `bscrapGE4`. The red-rabbit drop (style1drop1opt2AutoRR)
first drives gripper 1 to CLOSE with hand-written outputs (`$OUT[249]` OFF,
`$OUT[250]` ON, lines 25-32), then "opens" with
`GRPg_SetStateAndCheck(3, 1, ...)` (line 105). Gripper 3 is inactive in
`grp_data.dat`, but it is configured on the same I/O as gripper 1
(`$OUT[249]/[250]`, `$IN[257]/[258]`, same states) and `GRPg_SetState` does not
look at the active flag (only the PLC path `GRPg_ChkSetStatePLC` does): gripper
1 really opens and the check of gripper 1 OPEN (line 111) passes. The release
works only because of that duplicate mapping. The robot then moves away (LIN
P23) before the gripper-empty wait, and the outputs are cleared at the drop,
before the PLC can read them; MaintainSystem clears them again at the top of
the next cycle. Gestamp review points 8 and 21 describe the same.

*Fix:* decide the red-rabbit procedure with Gestamp (option number, what a
pass is: all nuts missing seen by sensor AND camera), evaluate it in one place
with one exclusive verdict held until the PLC acknowledges, release with
gripper 1 and wait for gripper empty before moving.

### F20 — Medium — reject path

RejectGE4 opens the gripper over the reject location with no
`AC_DropOffCheck` or zone request. A scrap decision in the nut check jumps to
RejectGE4 and skips the `AC_Application(1, TRUE)` release in the camera
program, so Application 1 stays occupied until MaintainSystem. The second
`OUT 106 ... State=FALSE` inline form carried hidden data `5:TRUE` and
enclosed the flag resets — **fixed by the cleanup** (form data now FALSE,
resets moved out of the fold; see the allowlist). *Fix:* interlock the reject
location, release Application 1 on the reject path.

### F21 — Medium — hidden AutomationCore form parameters

style1pick1opt2 has `AC_CmdParam=1` in both pick folds but calls
`AC_pickUPCheck(2)` / `AC_pickUP(2,True)`; style1app2opt2 has
`AC_CmdParam=2` but calls `AC_Application(1,True)`; style1drop1opt1 has
`AC_CmdParam=2` and calls `AC_DropOffCheck(1)` / `AC_DropOff(1,True)`, while
the red-rabbit drop has `AC_CmdParam=2` and calls `(2)` — no consistent offset.
Opening and confirming such a form regenerates the call from the hidden
parameter. The cleanup left these lines untouched and put a `;WARNING:` above
each fold. *Fix:* establish the index convention of the AutomationCore form,
then correct the parameters.

### F22 — Medium — frame modes at the pedestal

Of the 22 moves taught in base 3 "NUT WELDER", 11 run in base mode and 11 in
external-TCP mode; the three weld presentations (P19 in app 1, P16 in apps 2
and 3) are all in base mode. Gestamp asks for pedestal moves interpolated
about the fixed die (C04). No production move uses tool 2 on R10 (the only
user was the deleted redrabbit.src). *Fix:* decide one frame convention for
the pedestal and re-teach consistently.

### F23 — Low — LPT position assembly (R10)

R10 builds `CL_GunStrokePositionLPT = BYTE1*65536 + BYTE2*256 + BYTE3`
(sps.sub:69): 24 bits, `CL_LPT_BYTE0` ignored, so the R20 32-bit overflow does
not exist here. R20 builds the value from all four bytes in the order
BYTE1, BYTE0, BYTE3, BYTE2 with the same bus mapping. One of the two is not
the BTL6 format. *Check:* the BTL6 output format of this pedestal; with the
gun open the value must read about 139800 (comment table), with the gun on
the nut about 70900.

### F24 — Low — dead retry path

`NUT_WELD_RETRY` is never set TRUE, so the three `GOTO RETRY_NUT1` branches
never run (style1app1opt1:73-77, opt2:70-74, opt3:62-66). *Decide:* delete
the branches or design the retry (request and await a fresh preload).
Gestamp point 17. **Fixed in the office (G17); to be tested on the cell.**
Decision: delete, as on R20. Branches, labels and the variable are gone; no
path changed.

### F25 — Low — fallback feed

When `NUT_READY` is FALSE at entry, CENTERLINE_WELD feeds its own nut:
`dopw1_StartFeed = TRUE` then immediately `FALSE` (lines 69-71), with the
feed-complete wait commented out (line 70) and a fixed `WAIT SEC 1.5`. The
jump label `NUT_READY:` has the name of the global BOOL. *Fix:* remove the
path or make it request a PRELOAD and wait for it; rename the label.
Calvin (#19) proposes to restore the feed-complete wait with a timeout; on
R20 Ethos (Edgar, 2026-10-04) kept the criterion of this item (remove the
local path or turn it into a preload request) — the same is proposed here.

### F26 — Low — timers

PRELOAD uses `$TIMER[10..13]`, CENTERLINE_WELD `$TIMER[14..15]`. No active
collision with vendor code. `$TIMER[13]` is never stopped at the end of a
preload. *Fix:* named constants with an ownership comment.

### F27 — Low — contradicting comments (corrected)

Corrected in the cleanup: "UPPER PIN EXTEND" over the retract command,
"LOWER PIN RETURN" and "CL_LowerPinRetreated" over the advance command,
"SCHEDULE 7" over weld program 2, "QFP ADV" over the QFP-returned check, the
Spanish comments of the pedestal programs. *Confirm on the cell:* what
`$OUT[494]` `dopw1_BlowOff` physically drives (it is switched during the feed
and during intensify), the upper and lower pin valve assignment, and that
weld program 2 is the intended Bosch schedule.

### F28 — Low — nut sensor timing

Each nut check is `LIN` (exact stop), sample the sensor, then `WAIT SEC 0.2`
(style1app2opt1:50-53, 81-84, 112-115). The settle time follows the sample.
*Fix:* dwell (or wait with a short timeout) before sampling.
**Fixed in the office (G13); to be tested on the cell.** Each check is now
`WAIT SEC 0.2` then `PARTPRESENTn = NUT_PRESENT1` (renamed `di227NutPresent1`):
the read happens with the robot standing at the point and a missing nut
writes FALSE (part of F03).

### F29 — Low — beacon (R10 variant)

sps.sub (lines 93-101) drives the KL50L2 beacon from `$OUT[478]`/`$OUT[477]`,
which only the disabled NutWeld background writes: red sets `$OUT[3008]` and
`$OUT[3024]`, green sets `$OUT[3001]` and clears `$OUT[3024]`. None of the
three bits is declared, `$OUT[3001]` is **not mapped** (KRC_IO.xml maps
`$OUT[3000]`, `[3008]`, `[3016]`, `[3024]`), and R20 uses `$OUT[3000]` and
`$OUT[3016]` for the same beacon. *Fix:* confirm the KL50L2 bit layout, drive
the beacon from `$IN[480]` hopper low with explicit on/off, or remove the
block.
*Office (G12):* the three bits are declared (`CL_BeaconBit3001`,
`CL_BeaconBit3008`, `CL_BeaconBit3024`); the logic is unchanged.

### F30 — Low — GOTO structure

After RejectGE4 the GOTO skips the rest of the block and, in the station-1
block, the station-2 test; after a station-1 drop `GOTO LABEL12` skips the
station-2 test. The three labels are one exit.
**Fixed in the office (G11); to be tested on the cell.** Rewritten as IF/ELSE:
the pick station is read once into `nPickStation`; after any RejectGE4 nothing
else runs, a station-1 cycle never runs station 2, and every path ends at the
clear of `PARTPRESENT1..3`.

### F31 — Medium — GripperTech forms (R10)

R10 uses GripperTech forms in the production picks, drops and reject (R20
replaced them by hand-written outputs). Only gripper 1 is active in
`grp_data.dat` (`$OUT[249]/[250]`, `$IN[257]/[258]`). In the three picks and in
the conveyor drop the gripper SET forms carry the hidden parameters
`setgripper=4;setstate=2` while the code calls `GRPg_SetStateAndCheck(1, 1 or
2, ...)`: opening and confirming such a form regenerates the call for
gripper 4 — `$OUT[251]/[252]` and `$IN[259]/[260]`, which are on the bus:
gripper 1 would no longer move and the check would time out (3 s) into the
error strategy. The red-rabbit drop writes `$OUT[249]/[250]` by hand and
releases with gripper 3, which shares gripper 1's I/O (F19).
**Office version (G10):** the hidden parameters of the pick and conveyor-drop
SET forms now read `setgripper=1` with the state of the call, and the redundant
`GRPg_Check` after each SET-with-check is gone; to be tested on the cell (open
and confirm one form of each on the smartPAD and compare the call). Each SET with check is followed by a redundant `GRPg_Check` of the same
state. *Fix:* correct the hidden parameters (open each form with the right
gripper and state, or edit the `;Params` line), use one SET-with-check per
command, replace the hand-written outputs of the red-rabbit drop.

### F32 — Medium — code inside inline-form folds

`TRIGGER WHEN DISTANCE=0 DELAY=0 DO NUT_STAR=TRUE` (picks, P12 / P10) and
`TRIGGER ... DO Request_next_nut()` (end of weld apps 1 and 2, in the P0
fold) were typed by hand inside motion inline-form folds; the red-rabbit drop
has the flag resets inside the `DropOff[2] Reset` form. Touch Up or re-opening
the form regenerates the fold body and deletes them — then nut 1 gets no
preload (`NUT_READY` keeps a stale TRUE, F14) or nut 2/3 waits forever for
`NEXT_NUT_READY`. Gestamp point 20 describes exactly this for xP0.
**Fixed in the office (G20); to be tested on the cell.** Each TRIGGER stands
right before its motion fold (the place KUKA's own SYN OUT form uses: same
motion, same trigger point); the red-rabbit resets follow the `DropOff[2]
Reset` fold.

### F33 — Medium — GripperTech configuration out of sync

`C/KRC/User/TP/Gripper_SpotTech/GripperConfig.xml` (HMI plug-in, identical to
R20's) has all grippers inactive with dummy I/O, while `grp_data.dat` has
gripper 1 active on `$OUT[249..250]`/`$IN[257..258]`. Saving the GripperTech
configuration on the smartHMI would regenerate `grp_data.dat` with gripper 1
inactive and its dummy I/O. GripperTech's set routine ignores the active
flag; it is the dummy I/O that would break production: every
`GRPg_SetStateAndCheck(1, ...)` would drive and check the wrong bits. *Procedure:* do not save the gripper configuration until the XML is
re-synchronised.

### F34 — Low — CENTERLINE_HOME

CENTERLINE_HOME writes `$OUT[473]` `dopw1_Nut1Intensify_Home` OFF, while
CENTERLINE_WELD keeps it ON at rest; it never resets weld start, contactor
enable, weld-on or the spot number; its water-off is overwritten by sps.sub
(F09) and PRELOAD may rewrite its outputs (F11). *Fix:* confirm the polarity
of `$OUT[473]`; add the Bosch reset.

### F35 — Medium — mastering reference leaves `$OUT[930]` ON (R10)

MASREFSTARTG1 sets `do930MasterRefInProcess` TRUE (masref_user:12) and
MASREFBACKG1 sets it **TRUE again** at the end (line 120) where the old
commented line set `do828` FALSE. Nothing else writes `$OUT[930]`. After the
first mastering-reference test the flag stays ON for good; the AutomationCore
request-to-enter routine (vendor edit) refuses entry while it is ON, so if the
background task is ever re-enabled (F12), request to enter is blocked for
ever. `$OUT[930]` also lands on the PLC bit of `$OUT[111]` (F18). The path
closes gripper 1 before moving to the reference switch. *Fix:* set it FALSE at
the end of MASREFBACKG1.

### F36 — Low — `$IN[227]` names

`$IN[227]` is declared as `NUT_PRESENT1` in `$config.dat` and as
`di227SensorCamera` in automationcoreroutines.dat — it is the nut sensor, not
the camera. *Fix:* keep one AutomationCore-style name (`di227NutPresent1`).
*Office (G15):* `di227SensorCamera` renamed `di227NutPresent1`, the
`NUT_PRESENT1` declaration removed.

### F37 — not applicable on R10

On R20 the intensify-pressure wait is disabled (Calvin #1). R10 keeps
`WAIT FOR dipw1_IntensfPresOk` (centerline_weld:191) — confirmed, as Calvin
notes. It has no timeout (F15), and what pressure the regulator really
receives is F44.

### F38 — High — nut-preload state not re-initialised

*Source: Calvin #11 (10R1), Gestamp point 19.* The nut handshake lives in
persistent `$config.dat` globals (`NUT_READY` declared TRUE, `NUT_STAR`,
`NUTCYCLE_ACTIVE`, `NUT_PRELOAD_STEP`, `STEP*DONE`, `STEP10_ADV_STARTED`,
`NEXT_NUT_*`). Nothing initialises them at program start, cancel/reset or
controller boot; after a reboot in the middle of a preload, PRELOAD resumes at
the stored step; after a block selection the TRIGGERs that drive the
handshake are skipped. *Fix:* one initialisation routine called from the
sps.sub USER INIT, from cell.src before the first cycle and from the F10
safe-state routine, deriving `NUT_READY` from real I/O.

### F39 — Medium — torque monitoring values and load data

*Source: Calvin #16.* `$TORQMON_DEF[1..12]` and `$TORQMON_COM_DEF[1..12]` are 0
in `KRC/STEU/Mada/$custom.dat` (lines 80-104). `$LDC_CONFIG[1]` =
`{UNDERLOAD #WARNONLY, OVERLOAD #WARNONLY}`: the load-data check only warns.
`LOAD_DATA[1]` is `M 210, CM {270, 0, 240}, J {105, 105, 105}` — round values,
typed in, not determined (Gestamp point 3). All production moves run with
`TQ_STATE FALSE`. Calvin describes R10 as a "gun robot"; it is a material
handling robot (EOAT 1 + part) — the facts stand. *Fix:* after G03/C08, set the
values per the KUKA manual (or record why they stay) and decide the reaction of
the load-data check.

### F40 — Medium — gripper opened without confirming the part

*Source: Calvin #25.* The conveyor drop and RejectGE4 open the gripper without
first confirming `$IN[253]/$IN[254]` ON: a part lost on the way is "dropped" and
`$OUT[18]` cleared as if delivered. The red-rabbit drop moves away (LIN P23)
before waiting for gripper-empty. G14 fixes the order at the start of the
picks. *Fix:* supervised part-present wait before opening; gripper-empty wait
before the move away.

### F41 — Low — literal numbers left

*Source: Calvin standards #5.* After G16: PRELOAD timer limits (2000, 500, 800,
800 ms), the water-flow limit `SV0500_FLOW > 1230` and the fixed `WAIT SEC`
values of CENTERLINE_HOME and CENTERLINE_WELD are literals. *Fix:* named
constants in `$config.dat`, same values.

### F42 — Low — software work envelopes

*Source: Calvin #30.* `$AXWORKSPACE[1..8]` and `$CYLWORKSPACE[1..8]` are
`#OFF` ($machine.dat:378-385, 403-410). Two Cartesian workspaces are set in
`$custom.dat` (`$WORKSPACE[1..2]`, `MODE #OUTSIDE`): they only signal, they
do not stop the robot.
SafeOperation has a monitoring space "Nest Workspace" (edited last on
2026-09-13). *Decide* with Gestamp whether software envelopes with stop are
wanted on top of SafeOperation, and document what the safety spaces cover.

### F43 — Medium — electrode change handshake

*Source: Calvin #29, Gestamp point 6.* In gunelectrodechange.src the stepper
reset is `PULSE(dopw1_StepperReset,TRUE,0.1)` (line 68) with no check of
`$IN[487] dipw1_EndOfStepper`; `$OUT[92] do092RobotCapChg1Cmplt` is switched
off only if `$OUT[111]` is already off, and `$OUT[91]` is switched off without
waiting for the PLC to drop `$IN[92]`. Calvin cites electrodechange.src, an
older copy nothing called (deleted by the cleanup); the live routine has the
same pattern. cell.src calls GunElectrodeChange when `$OUT[111..113]` are ON,
but those outputs are written only by the disabled background task (F12): as
it stands the electrode change never runs. *Fix:* decide how the change is
requested (PLC bit or counter), confirm the reset, close the handshake by
levels, supervise the waits.

### F44 — High — pressure set-point byte order (R10)

`CL_GunPressureCmd` (`$OUT[506..521]`) is mapped in KRC_IO.xml exactly as on
R20: `$OUT[506..513]` to byte 653 and `$OUT[514..521]` to byte 652 — the
regulator receives the word **byte-swapped**. On R20 every value is written
swapped (0.30 MPa = 1365 = 0555 hex is written 21765 = 5505 hex). R10 writes
**405** (general) and **1820** (intensify, "0.40 MPa" in the comment table)
not swapped, and **39425** (= 019A hex swapped = 410 = 0.09 MPa) at the end of
every weld (centerline_weld:256). Unless the R10 regulator is configured
differently, the general command reaches the ITV as 38145 and the intensify
command as 7175 — both outside 0..4095; if it is not swapped, the rest value
39425 is outside the range instead. Either way one set of values is wrong, and
the gun rests at the 39425 value between welds. The intensify-pressure switch
`$IN[479]` is satisfied in production, so the weld pressure is at least above
the switch setting.

*Check on the cell:* read the ITV display (or its monitor output) at rest,
with the gun closed before intensify and during intensify; compare with the
regulator configuration (byte order, 12-bit range). *Fix:* write all values
in the byte order the regulator expects, as named constants (G16).

### F45 — Low — clamp routines (R10, closed by the cleanup)

*Source: Calvin #23.* CloseAndCheckAllClamps / OpenAndCheckAllClamps (called
only by the mastering reference) had the set and check of grippers 2-4
commented out (`;===SL===`). Grippers 2-4 are inactive in `grp_data.dat`:
gripper 3 is a duplicate of gripper 1's I/O, gripper 4 points at
`$OUT[251]/[252]`, `$IN[259]/[260]` (no EOAT function on R10) and gripper 2's
inputs `$IN[269..272]` are not on the bus. Re-enabling them would add nothing
on EOAT 1; the cleanup removed the disabled folds and documented that the
routines handle gripper 1 only.

### F46 — Medium — Work Complete never sent (R10)

The vendor routine `EndOfCycle` (automationcoreroutines.src:396-415) was
edited on this robot (`;======SL====`): `do015WorkComplete=TRUE`, the wait for
`di015WorkCompleteAckn` and `do005RobotInCycle = FALSE` are commented out.
Work Complete therefore never goes to the PLC; Robot In Cycle drops only at the
top of the next loop (MaintainSystem). R20 still has the standard routine. The
cell runs, so the PLC evidently does not wait for Work Complete from 10R1 —
but it is a Gestamp standard handshake (C18, C20). *Decide* with Gestamp and
the PLC programmer; restore the vendor routine or document the deviation.

### F47 — Medium — brake-test path (R10)

`TP/BrakeTest/braketeststart.src` moves PTP to `m` and `h` (the same pose, 2.6 m
high) with `Tool[3]` and `Base[1]` — the fold text names them "Tool 3" and
"3-30-R1 03-20B", copied from another robot; on R10 base 1 is "10A" and tool 3
is "TOOL 3". The points are Cartesian, so the path depends on whatever tool 3
and base 1 hold. `braketestback.src` returns with tool 1. The vendor files also
carry the `do931BrakeTestInProcess` edit. *Check:* run the brake test slowly
in T1; re-teach the path with tool 1 / base 0 (joint points preferred).


### F48 — High — drop-off interlock after the approach (audit 2026-10-05)

In the programmer's backup of 2026-10-05, `AC_DropOffCheck(1)` (wait for
`$IN[75]` di075DropOffMachine1) moved from before the first motion to after
`PTP P5` and `PTP P1` in style1drop1opt1: the robot approaches the conveyor
before the PLC grants the drop-off. AtDrop3 was re-taught 26° in B and 34° in
C. *Fix:* check the drop-off before the first motion, or prove with the
layout that P5/P1 are outside the conveyor zone; explain the new AtDrop3.
*Integrated version (2026-10-05):* `AC_DropOffCheck(1)` stays before the first
motion. The new AtDrop3 is kept: the part falls better on the conveyor
(validated by Edgar Montiel with the programmer). To test on the cell.
*Backup 14:46:* the programmer also removed PTP P1: one 330 mm LIN from P5 to
AtDrop3, dropping 166 mm at about 30°, with the drop-off check at P5. In the
integrated version the robot waits for the drop-off at the camera point P3
with application 1 already reported clear (`AC_Application(1,TRUE)` at the
end of style1app2opt2): release application 1 after the robot leaves the
camera area. *Integrated version (from the 14:46 backup):* P1 kept (the
programmer is asked why he removed it); `$OUT[70]` do070ApplicationClear1 is
set by a TRIGGER on the first motion away from the camera (P5 of the conveyor
drop, P23 of RejectGE4, P28 of the red-rabbit drop), which also releases
application 1 after a sensor scrap (F20).

### F49 — High — AutomationCore background switched on (audit 2026-10-05)

The same backup calls `AutomationCore_BKG()` in sps.sub (F12) and edits the
vendor routine: the outputs of nut welders 2-3 are removed and
`AC_Request_to_enter` no longer waits inside the submit (it latches
`bACEntryGranted`; `$OUT[145]` doCriticalWZ = NOT granted). With the
background on, the status bits to the PLC update every cycle, CELL is
selected automatically in EXT, every program reset sets `do004ProcessFault`,
and `do111Gun1ElectrodeChange` follows the stepper end, so cell.src now runs
GunElectrodeChange (F43). *Decide* with Gestamp, test every signal with the
PLC and the electrode change, list the vendor edits (C28).

Independent review of 2026-10-05 (confirmed in the code):
* **Request to enter.** `AC_PointArrival` (bas.src motion triggers) halts the
  robot on `$IN[6]` di006RequestToEnter only while `$OUT[145]` doCriticalWZ is
  FALSE. With the background on, doCriticalWZ = NOT granted, and entry is
  never granted while `$OUT[930]` do930MasterRefInProcess is ON — which it
  stays for ever after a mastering reference test (F35). The robot then no
  longer stops on a request to enter. Before, nothing wrote `$OUT[145]` and
  the robot always stopped.
* **Two writers on the Bosch enables.** The task writes `$OUT[481]`
  dopw1_WeldContactEnable and `$OUT[482]` dopw1_WeldOnExternal = NOT dry cycle
  every submit cycle, overriding CENTERLINE_WELD's reset and disable; in dry
  cycle it overrides the enable and `WAIT FOR dipw1_Ready` can hang.
* **Electrode change** runs at the stepper end and waits for the PLC's
  `$IN[92]` in a dialog; `$OUT[111]` shares its adapter bit with the stuck
  `$OUT[930]` (F18).
* **AC_MODE** (CWRITE of the mainline auto select) is declared without a
  value; KUKA's template sets MODE=#SYNC first.
* Every program reset sets `$OUT[4]` do004ProcessFault until MaintainSystem.
* `bACEntryGranted` is persistent: a grant survives a submit restart.

*Integrated version (from the 14:46 backup):* the background task is off again,
as received, until Gestamp decides and these points are fixed; the submit
clears `$OUT[145]` and `$OUT[111]` at start. The programmer's edits inside the
vendor routine stay, inactive (C28).

### F50 — High — application permission after the motion (audit 2026-10-05 14:46)

In the programmer's backup of 14:46, style1app2opt1 runs `PTP P22` before
`AC_ApplicationCheck(1)` (wait for `$IN[70]`). P22 is the approach point of the
inspection station (about 170 mm from the camera approach P6, 480 mm below the
nut-check points), so the robot enters it without the PLC's permission while
`$OUT[70]`/`$OUT[24]` still report it clear. *Fix:* check before the motion,
as in the integrated version.

### F51 — Low — weld apps per pick station (audit 2026-10-05 14:46)

The programmer split the three weld apps per pick station: style1app1opt1A..3A
for parts from pickup 1 (positions unchanged) and 1B..3B for pickup 2 (weld
positions re-taught 1-5 mm: the part sits differently in the gripper).
Style1Opt1 calls A or B by the pick station. The code of A and B is the same:
any later change to a weld app has to be made in both. Integrated as it is.
## Gestamp compliance

Reference: GESTAMP FANUC Reference Guide V23 and NA-ST-002 rev 11, as
recorded for the sister station 03-30-R1, and the AutomationCore package in
this archive.

| ID | Requirement | State on R10 | Fix type |
|---|---|---|---|
| C01 | AutomationCore background task maintains PLC status | Off (F12) | Gestamp decision |
| C02 | Designation `<prog>-03-10-R1-<device>`, devices PNW1 / MH1 | `BMW-03-10-R1-...` in every header (Gestamp's review names the station BMW-03-10R1, header assumed); exact format to confirm with Gestamp. The old HOME header said "Line - Volvo" | info |
| C03 | Header block in every integrator module | Done by the cleanup | — |
| C04 | Pedestal (remote TCP) moves interpolated about the fixed die | 11 of 22 base-3 moves in external TCP, none of the 3 weld presentations (F22) | re-teach |
| C05 | Remote TCP 6.35 mm off the stationary electrode, axes square to the die | `BASE_DATA[3]` "NUT WELDER" = {X 21.84, Y 1866.09, Z 658.47, A 90, B 0, C 180} | measure on site |
| C06 | Tool/base named; no unnamed tools in production | Tools named "TOOL 1".."TOOL 3"; bases "10A", "20B", "PED SEALER" come from another project; stale tool names in fold text refreshed by the cleanup | rename |
| C07 | One user frame per fixture | Pick stations, nut check, camera, reject and drop mostly taught in WORLD (camera approach P6 and reject exit P24 in Base[3]) | Gestamp decision |
| C08 | Payload per loading scenario, determined | `LOAD_DATA[1]` 210 kg, round values typed in (F39) | LoadDataDetermination |
| C09 | Collision detection on at all times | Off (`$TORQMON` 0, `TQ_STATE FALSE` on every production move); reaction is a bare HALT | tune on cell or written waiver |
| C10 | `ZERO_G1` mastering program | Missing (only the KUKA mastering-reference test exists) | new module |
| C11 | Zones commented with this robot, the zone and the partner robot; NA-FM-71-138.1 | No zone is requested anywhere (production, repair, pounce) | Gestamp form |
| C12 | One common pounce | None in the cycle; `do007RobotAtPounce` never computed | Gestamp decision |
| C13 | Zone handling consistent | No zones used | — |
| C14 | Brake test due reported, executed at home | Runs on PLC request; "due" never reported (F12); path taught with another robot's tool/base (F47) | code |
| C15 | Dry cycle selectable, must not hang | Hangs (F04) | code |
| C16 | Part present / part in gripper | Checked at pick and drop; `$OUT[18]` latched, not live (Gestamp 9) | code |
| C17 | Nut verification and red rabbit | F02, F03, F19 | code |
| C18 | AutomationCore pick/application/drop handshakes | Paired, except reject (F20), hidden parameters (F21) and Work Complete (F46) | code |
| C19 | Request to enter honoured | Robot halts at the next point, `doCriticalWZ` never set (F12) | code |
| C20 | Weld count checked at end of cycle | `#CHECK` commented out in the vendor EndOfCycle, Work Complete removed (F46) | code |
| C21 | Faults through AutomationCore messages, no bare HALT | HALT, WAIT FOR FALSE, unsupervised waits (F06, F07, F15) | code |
| C22 | Grippers through GripperTech forms | Used in picks, drops and reject; stale hidden parameters (F31); hand-written in the red-rabbit drop | inline forms |
| C23 | AutomationCore I/O names, no literal addresses | Done in the office (G12) outside KUKA inline forms; overlapping gun 2/3 names still to retire (F17) | declarations |
| C24 | Comments name the signal | Done by the cleanup | — |
| C25 | Inline forms consistent with code | Fixed where safe (RejectGE4); warnings elsewhere (F21, F31, F32) | inline forms |
| C26 | English only | Done by the cleanup; identifiers renamed in the office (G15) | — |
| C27 | Robot-controlled process not shared; two-process rule | Compliant (material handling + one process) | — |
| C28 | Vendor packages unmodified | Integrator edits found in automationcoreroutines.src (EndOfCycle, F46), grp_func.src, grp_user.src, bas.src, BrakeTest; GlueTech installed but unused | documentation |

## Integrator edits found inside vendor files (not touched)

* `KRC/R1/System/bas.src`: AutomationCore installer folds adding
  `TRIGGER ... AC_PointArrival()` to every PTP/LIN parameter set.
* `TP/AutomationCore/automationcoreroutines.src`: **EndOfCycle without Work
  Complete** (F46); water start and beacon logic, speed-not-100 output,
  `Stop_at_End_of_Cycle` in MaintainSystem, request-to-enter extended with
  `do930..932`.
* `TP/GripperSpotTech/grp_func.src`: `do121GripperFault` set and reset in the
  check and error-strategy routines; `grp_user.src`: `do932GripperInProcess`.
* `TP/BrakeTest/braketeststart.src`, `braketestback.src`: `do931` in-process
  flag (old `do829` commented); start path taught with tool 3 / base 1 (F47).
* `TP/GLUETECH/*` and `Program/MoveToPurge.src`: GlueTech package (template
  purge routine) installed on a nut-weld robot; not called by the cycle.

## Gestamp program review (2026-10-02) — BMW-03-10R1

Gestamp's "Robot Program Review – Findings" lists 22 points for this station
(the header of the page is not visible in the photo; the document assumes
BMW-03-10R1, and the content matches this archive). Each one is open item Gnn
in `docs/open_items.json` (Spanish, with closure criteria). Verification against
the archive, and status after the office changes:

| # | Gestamp | Verified in the archive | Status | Related |
|---|---|---|---|---|
| 1 | Robot name needs to change | Yes: robot name `V431_03_10_R1` (am.ini, RobotData.xml) | Open — rename on the controller; format to confirm with Gestamp | C02 |
| 2 | Safety Tool is not equal to Default TCP | Not verifiable from the archive (safety tool geometry is in the safety controller); the safety log shows tool 1 changed three times on 2026-08-30 | Open — SafeOperation, checksum, acceptance | C05 |
| 3 | Tool 1 is used without Load data determination | Yes: `LOAD_DATA[1]` round values, load check warn-only | Open — Load Data Determination with and without part | F39, C08 |
| 4 | Program Red Rabbit() is blocked, might be an unnecessary copy | Yes: redrabbit.src starts with `WAIT FOR FALSE`, from a stud cell, blocked by `WAIT FOR FALSE` right after INI, not called, cannot link | **Fixed by the cleanup** — deleted | F19 |
| 5 | Unused programs | Yes: 11 modules nothing calls | **Fixed by the cleanup and the office** — 11 deleted + CENTERLINE_LOOP; safetest kept (decision), GlueTech to uninstall | C28 |
| 6 | Electrode change confirmation only 0.1 s, no handshake | Yes (gunelectrodechange:68) | Open | F43 |
| 7 | Multiple options in Style_1 call the same sub-program | Yes: 1, 2, 7, 8 → Style1Opt1 | Decision — what options 2/7/8 are | F02 |
| 8 | Separate Auto-Red Rabbit program that doesn't match production | Yes, and worse: it cannot give a result | Decision — red rabbit procedure | F19 |
| 9 | Part control to PLC is set/reset instead of reflecting the real part controls | Yes: `$OUT[18]` set at pick, reset at drop/reject | Decision — `$OUT[18]` from the part-present switches | F12, C01, C16 |
| 10 | Gripper commands not used at all times | Yes: red-rabbit drop hand-written; stale hidden form parameters | Open | F31, F33 |
| 11 | Use of Goto labels | Yes: 9 modules | **Fixed in the office** | F30, F07 |
| 12 | Use of I/O numbers instead of signal names | Yes: pedestal programs, sps.sub | **Fixed in the office** | F17, C23, F29 |
| 13 | Poor programming (10 lines for nut present) | Yes: style1app2opt1 | **Fixed in the office** | F28, F03 |
| 14 | Gripper opened before the part control check | Yes: the 3 picks open the gripper, then wait for gripper empty | **Fixed in the office** | — |
| 15 | Names, variables and comments not in English | Yes: comments, `NUT_STAR`, `Judment`, `Rejeted`, folder `optiones` | **Fixed by the cleanup and the office** | C26, F36 |
| 16 | NO variables for e.g. stroke limits | Yes | **Fixed in the office** — constants in `$config.dat` | F16 |
| 17 | Nut_weld_Retry logic useless | Yes: never set TRUE | **Fixed in the office** — removed | F24 |
| 18 | NO check for Weld OK, just weld finished | Yes (centerline_weld:199) | Open — Bosch OK/fault signal and polarity to confirm on the cell | F08 |
| 19 | Next_Nut_Ready logic can fail at block selection, reset, reboot | Yes | Open | F38, F14 |
| 20 | Change of xP0 deletes Request_next_nut inside inline forms | Yes: TRIGGER in the P0 folds of apps 1 and 2 (and NUT_STAR in the picks) | **Fixed in the office** — TRIGGERs before the folds | F32 |
| 21 | Style1app2Opt1 will not work for RedRabbit | Yes: option 12 has no case | Decision | F19 |
| 22 | Use of AutomationCore is wrong in multiple places | Partly verifiable; known: F12, F20, F21, F46, C11, C18, C19 | Decision — ask Gestamp for the list | F12, F21, F46 |

Office changes are proved with `tools/check_equivalence.py` (logic diff
against the cleanup commit, signals compared by address, constants by
value) and every change is declared in `tools/code_changes.json`. None
replaces the cell test each G item asks for.

## Calvin's open-issues list (2026-10-03) — verification for 10R1

`Gstamp_Robot_Open_Issues_2026-10-03.xlsx` (Calvin Kimura, Ethos) covers the
three robots. Every row for 10R1 or "All" was checked against this archive.
*Confirmed* = the code shows exactly what the row says. The row's item in our
list is given; no row is left without one.

| Calvin # | Robot | Row (short) | Verdict on R10 | Our item |
|---|---|---|---|---|
| 1 | 20R1 | Intensify pressure wait commented out; "10R1 still has it active" | Confirmed for 10R1: the wait is active (centerline_weld:191), no timeout | F37 (n/a), F15, F44 |
| 2 | 10R1 | Live weld waits only on WeldComplete (line 199), no fault/OK, no timeout | Confirmed. The "CENTERLINE_WELD1 pattern" used AutomationCore Bosch signals that are not on this robot's bus; use the NutWeld `$IN[485]` instead | G18, F08 |
| 6 | 10R1 | PRELOAD CASE 0 completes on `$TIMER[10]>=2000` (line 47) | Confirmed. Severity: we keep Medium (missing nut stops at the LPT window, F07) | F13 |
| 8 | 10R1 | Part present to PLC latched: PARTPRESENT1/2/3 and do018 set/reset | Partly: `$OUT[18]` is latched (confirmed); `PARTPRESENT1..3` are the internal nut-check flags, not PLC signals (their problem is F03) | G09, F03 |
| 11 | 10R1 | NUT_READY / NUT_STAR / NEXT_NUT_READY globals, no reset/power-fail handling | Confirmed | G19, F38, F14 |
| 13 | 10R1 | Safety tool ≠ default TCP | Not verifiable from the archive (safety log only) — check on the controller | G02 |
| 16 | 10R1 | `$TORQMON` all zero ($custom.dat 80-104); LOAD_DATA[1] hand-entered | Confirmed (lines 80-104; 210 kg round values). R10 is a handling robot, not a gun robot | F39, G03 |
| 19 | 10R1 | Fallback feed: feed-complete wait commented, WAIT SEC 1.5 (70-72) | Confirmed (lines 68-73). Proposed fix differs: remove the path or make it a preload request (as decided on R20) | F25 |
| 23 | 10R1 | Clamps 2-4 set/check commented out | Confirmed, but grippers 2-4 do not exist on this EOAT: rescoped and cleaned | F45 |
| 25 | All | Gripper opened before part control; gripper commands inconsistent | Confirmed (picks: fixed in the office, G14; drops/reject: F40; forms: F31) | G14, G10, F40, F31 |
| 26 | All | Auto-Red Rabbit path does not match production; Style1app2Opt1 not under RedRabbit | Confirmed and worse on R10 | G08, G21, F19 |
| 27 | All | Nut_weld_Retry does not retry | Confirmed: never set TRUE | G17, F24 |
| 28 | All | Editing xP0 deletes Request_next_nut in the inline form | Confirmed | G20, F32 |
| 29 | 10R1 | Electrode change 0.1 s pulse, no handshake (electrodechange.src) | Confirmed in substance: the file cited was not called (deleted); the live gunelectrodechange.src has the same pattern | G06, F43 |
| 30 | All | `$AXWORKSPACE` all off | Confirmed | F42 |
| 31 | 10R1 | Dead code CENTERLINE_WELD1, trigger1-3 | Confirmed; deleted by the cleanup | G05 |
| Std 1-8 | All | Robot name, GOTO, I/O numbers, English, magic numbers, nut-present code, options, AutomationCore | Same as Gestamp points 1, 11, 12, 15, 16, 13, 7, 22 | G01, G11, G12, G15, G16, G13, G07, G22 |
| Std 9 | 10R1 | Red Rabbit() blocked / unnecessary copy | Confirmed; deleted by the cleanup | G04 |

Not in Calvin's list and found in this review: F44 (pressure byte order),
F46 (Work Complete removed from EndOfCycle), F19's gripper-3 release (works only through a duplicate I/O mapping), F09
(water OK forced TRUE), F35 (`$OUT[930]` stuck ON), F29 (unmapped beacon bit),
F47 (brake-test path), F01, F11 (pedestal entry and PRELOAD ownership — the two
critical items).
