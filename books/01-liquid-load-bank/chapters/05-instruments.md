# 5. Instruments, control, and the data exit

A load bank that cannot be read is a heater. A load bank that can be read only on its own door is a demonstration. The test you are building toward needs the same facts in a file as the person on the floor sees in the room. This chapter is about what is measured, where, how the readings share a clock, and what must be true of the exit path. It is not a register map. It is not a brand of monitoring software. Maps and brands rot. The duties do not.

## Two sets, or you cannot compare

On the unit, the minimum set is supply temperature, return temperature, supply pressure, return pressure, and flow. Those words match the duty set. If your diagram used different names, this is the moment to stop and make them match. Synonyms are how columns get swapped in the export.

On the rack side of the boundary, the same quantities need to exist as a comparison set, at least during acceptance and during any test where you will claim the stand-in behaved like the interface. People skip the second set because the unit already has sensors. Then every argument about a mismatch is unresolvable. The unit can be telling the truth about itself and lying about the manifold, because a hose, an adapter, or a mixing point sits between them.

The second set can be temporary instrumentation. Temporary is allowed. Impossible is not. The chassis, the hose routing, and the insulation must leave a place for a check probe and a check pressure tap, or you must have permanent rack-side points. Decide which. “We will figure out taps on the day” means you will not have them, and Gate 3 will be a local demonstration you over-interpret.

Write a column: unit point, comparison point, what difference is expected. Some difference is normal. A hose has loss. A sensor has bias. The column is not a demand that the numbers match to the last digit. It is a demand that you know which differences would change the story. A difference that changes the story is a stop until explained. An explained difference becomes a limitation or a correction you apply in public.

## Placement: Core immersion metrology versus dead-leg fraud

A sensor measures the thermodynamic microclimate of the exact spot where its sensing element sits, not the abstract stream in its software label. Supply temperature placed in a stagnant pipe stub measures the stub. Return temperature downstream of a bypass mix measures a mixture. (See Figure 03 for the detailed cutaway comparison of compliant core immersion versus dead-leg fraud).

To achieve valid metrology that survives mathematical scrutiny, four installation rules are non-negotiable:
1. **Core Stream Immersion ($1/3 \sim 1/2 D$)**: The thermowell tip must penetrate past the boundary layer and sit directly inside the high-velocity central core of the stream (between 35% and 50% of the pipe inner diameter). A shallow probe sitting flush with the pipe wall measures cold laminar boundary liquid and ambient metal conduction.
2. **Angle of Attack**: Angle the thermowell 45° upstream into the oncoming fluid flow. This maximizes convective heat transfer across the sheath, eliminates stagnant vortex wakes, and ensures rapid thermal response.
3. **Thermal Conductive Compound**: The annular gap between the RTD element and the inner thermowell sleeve must be packed with high-temperature thermal compound (zinc oxide/silicone grease). A dry thermowell creates an air-gap insulation barrier with a 30-second thermal lag, masking rapid transient spikes.
4. **Flush Deburred Static Pressure Taps**: Pressure taps for differential measurement (DPT) must be drilled perfectly perpendicular to the pipe axis, with inner edges completely deburred and polished flush. A tap drilled immediately downstream of a throttled butterfly valve or elbow sits in turbulent swirling eddies, converting dynamic velocity pressure into massive, fluctuating false static heads.

Protection sensors are not the same as recording sensors, even when they measure the same physical quantity. A protection sensor (such as a mechanical bimetal snap switch) must be fast, crude, fail-safe, and mounted directly on the heater element sheath. A recording sensor (such as a calibrated 4-wire Pt100 RTD) sits in the bulk stream to tell the true thermodynamic heat story.

## Industrial telemetry: Modbus-TCP, polling intervals, and quality flags

While the final acceptance package requires a flat CSV export for the stranger audit, modern data hall commissioning relies on automated supervisory platforms (such as Zabbix, DCIM, or PLC schedulers).

The load bank controller must expose a standardized, isolated telemetry interface (such as Modbus-TCP or Modbus-RTU over RS-485):
- **Discrete Coils**: Solenoid positions, heater contactor feedback, leak rope trip, E-stop circuit continuity.
- **Holding Registers**: Commanded kW, actual kW, supply temperature (0.01°C resolution), return temperature, flow rate (0.1 LPM resolution), supply pressure, return pressure.
- **Quality Bitmask**: A dedicated status register indicating sensor health. If a sensor wire breaks or a reading freezes, the controller must set the corresponding fault bit rather than echoing a stale value.

## Calibration tolerance classes and dual-sensor cross-checks

Metrology on acceptance day cannot rely on uncalibrated process gauges. Instruments must adhere to defined calibration tolerance classes:
1. **Temperature Sensors**: 4-wire Pt100 RTD elements conforming to IEC 60751 Class A (± 0.15°C tolerance at 0°C, ± 0.23°C at 40°C). Dual matched pairs must be calibrated together to ensure differential temperature measurement (ΔT) error remains ≤ 0.10 K.
2. **Flow Meters**: High-accuracy electromagnetic or Coriolis mass flow meters with factory-calibrated accuracy ≤ ± 0.5% of rate across the 50–250 L/min flow envelope. Vortex or turbine meters with ± 2.0% accuracy are acceptable only if straight-run piping requirements (10D upstream, 5D downstream) are strictly satisfied.
3. **Differential Pressure Transmitters (DPT)**: High-stability piezoresistive transmitters with ≤ ± 0.10% of calibrated span (e.g., ± 0.25 kPa on a 0–250 kPa span).

During Gate 2 and Gate 3, cross-checks between the unit's onboard sensors and the facility rack-side comparison probes must satisfy strict delta limits:
- **Temperature Cross-Check**: |T_unit - T_rack| ≤ 0.20 K.
- **Differential Temperature Delta**: |ΔT_unit - ΔT_rack| ≤ 0.15 K.
- **Differential Pressure Cross-Check**: |ΔP_unit - ΔP_rack| ≤ 5.0 kPa (after subtracting calibrated hose and coupling losses).
- **Flow Cross-Check**: |Q_unit - Q_rack| ≤ 1.0 L/min (or ≤ 1.0%).

Any variance exceeding these limits stops the gate until resolved. Never adjust sensor offsets in software to force arbitrary agreement.

## Clock and interval

The two sets and the electrical power must share a timeline. A temperature at one minute and a flow at four minutes are not a pair. You do not need a laboratory time service to meet this. You need one clock the export uses, a declared sample interval, and a way to see that a sample is missing rather than quietly repeated.

Missing versus repeated is the whole game. Many systems, when a read fails, hold the last value and keep stamping new times. The file looks dense. The process left. Any heat balance you compute from that file is fiction. The requirement is: a failed read is a failed read, marked, not painted over. If your platform cannot mark quality, do not use it as the acceptance record. Use something that can, even if it is humble, and demote the pretty platform to a display.

Declare the interval in the file. Faster is not always better. Faster than you can align is a way to fill disks and still mis-pair events. Slower than the sudden increase is a way to miss the only interesting moment. The interval must show the command jump and the plateau dwell with more than one sample on the dwell. If you have one sample on a dwell, you did not dwell in the record. You flickered.

Timestamp the command as well as the measurements. A record of temperatures with no record of what was requested is a weather log. You will not remember the request. The person who reviews the file next month was not in the room. The request is data.

## Four duties of the exit

Collect. The test platform can read the points without a person typing them off a panel. Typing is allowed as a backup for one gate, once, if the export path is broken and you are deciding whether to stop. It is not the design. If collection depends on a laptop that a single engineer must remember to start, the collection does not exist when that engineer is late. Start collection with the run, or make the run refuse to start. Prefer refuse.

Store. A run survives the end of the run. Power loss to the display does not erase the hour you just paid for. If storage is on the unit, say what happens when the unit’s storage fills: stop the test, overwrite oldest, or alarm and continue. Pick one. Overwrite without alarm is how evidence disappears from the front. Continuing with a full disk and no record is the same failure in slower motion.

Show. A person on the floor can see the live point and the alarm without the export. Floors are loud and bright. A tiny screen with a fault code is a show only if the code is in the file and the alarm is also a lamp or a line of plain words. Plain words beat codes. If you use codes, the code list is part of the delivery file, and an unknown code is itself an alarm condition, not a blank.

Export. The next book needs a file, not a photograph of a screen. The file has one row per time, or an equivalent that does not require a private tool to flatten. Columns have names, units, and a quality flag. A proprietary container that only one application can open is a hostage, not an export. You may keep a proprietary live protocol. You may not make it the only way out. Define the export as something a stranger can open in a ordinary table tool. If that sentence is painful, your architecture is showing off.

Identity of each point travels with the value. Unit of measure travels with the value. Timestamp travels with the value. Quality travels with the value. A documented failure travels with a stale point. Those four companions are the design principle. Everything else is implementation, and implementation may vary, and implementation does not get to drop a companion because the protocol makes it awkward.

## Valve position, leak, and other facts that change the story

If a valve can change the hydraulic story, its position is a point, not a decoration. At minimum the isolation valves and the trim or bypass valve, if they exist, need a state in the record when they are power-operated. Manually operated valves need a recorded check at the start of a run, because they will not update themselves. A run that begins without that check is not comparable to a run that begins with the valves elsewhere. Put the check on the acceptance sheet and on the later run sheet. This book only forces the acceptance version. The project book should steal it.

Leak or coolant detection belongs as an alarm if liquid leaving the path is a credible failure of this unit. It does not belong as a science project, and it does not belong as a substitute for isolation and for a person looking during Gate 1. A leak sensor that is not tested is a rumor. Test it the way the safety chapter says: a simulated input or a controlled wet test that does not soak the electrical section. Write the method. A method you cannot write is a sensor you do not have.

Level in a reservoir, if you have a reservoir, is the same kind of fact. A falling level with stable flow readings can mean a leak downstream of the meter or a deaeration event. Without level, you will misread both. If the unit has no reservoir, say so, and say where the expansion volume of the loop actually is. It is not nowhere.

Electrical power, voltage, and a current or a power reading are points, not just nameplate facts. The heat story needs power. A contactor auxiliary contact is a useful companion to power: command on and power at zero is an open element or a missed stage; command off and power above zero is the welded-contactor case. You do not need a power-quality study. You need enough electrical truth to know whether the heaters did what the heat command said.

## Alarms are sentences

An alarm must say what it is. Overtemperature, low flow, sensor fault, valve not in position, leak, storage full, export failed, control power lost: these are different events. A single red lamp is how acceptance becomes a debate about which fault was meant. Lamps may exist. They may not be the only text.

Each alarm has a source, a threshold or a discrete cause, a local indication, a record line, and an action. Action is one of: remove heat, stop flow authority, alert only, or inhibit start. Alert-only is acceptable for a storage warning and unacceptable for overtemperature. Write the action next to the name. If the action column is empty, the alarm is not specified.

Latched versus self-resetting is a choice. Protection alarms latch until a person resets them, so a trip is not erased by the condition going away. Informational alarms may reset. A protection that self-resets and then allows heat to return without a person is a heater that hunts through a fault. Do not build that unless you have a written reason and a limit on retries. Prefer latch and a local reset that does not require the network.

Alarm tests are part of acceptance, not part of the first real emergency. For each protection alarm, the sheet names the way you will cause it without destroying the unit. Simulated sensor. Controlled low flow with heat inhibited, then with a small heat, if that is safe. Open-door or jumper methods only if they do not bypass the very stop you are testing. If the only way to test overtemperature is to overheat the liquid past the limit, you have not designed a test, and you will skip it. Add a test input or accept that the protection is unproven. Unproven protection is a stop on the claim that the unit is safe to leave with heat available.

## Control duties, and no fifth duty

Control has four duties. Hold a setpoint that corresponds to a plateau. Step when asked, including the sudden increase. Remove heat on stop or on protection, including loss of control power. Leave a record of what it commanded and what it did. A control system that can do less is not finished. A control system that can also optimize a plant, forecast a price, or host a dashboard for visitors is out of scope. Extra scope that threatens the four duties is not a bonus. It is a risk. If the extra scope shares a processor with the stop path, you have coupled a toy to a protection. Separate them or delete the toy.

Remote command is allowed. Remote command is not the stop path. A local means to remove heat must work when the remote path is silent, wrong, or hostile. Hostile includes a stuck command to full load. The local stop overrides stuck remote command. Test that. A stop that politely asks the remote controller to stop is not a stop. It is a request.

Setpoint limits live in the controller and in the sheet. The controller should refuse a setpoint outside the duty you accepted, or outside a temporary override that is itself an alarmed mode. An open percentage field that can command beyond the tested plateaus will be used, in a hurry, beyond the tested plateaus. Refuse, or alarm and log, but do not be quiet.

Mode names should match the sheet. If the sheet says plateaus, the screen should not say “scenario B” unless the file defines scenario B as a plateau in watts. Undefined modes are how a unit ships with a demo mode that bypasses interlocks. Demo mode, if it exists, is heat-inhibited or it is not allowed to exist in the delivered software. Acceptance includes a hunt for heat that can be commanded with interlocks defeated. Ask the builder what modes exist. Then try to find one they did not mention. This is not hostility. It is how software ships.

## What you will not specify here

You will not specify a default network address. Addresses are commissioning facts. They go on the acceptance record as “identity as commissioned,” not into a book where they will be wrong and, worse, where they will be copied.

You will not specify a register map. The map is a project file. It must exist for your project if you use a bus, and it must match the points in this chapter, and it must be revision-controlled. It is not a design principle. The principle is the companions: identity, unit, time, quality. A map that delivers a number with none of those is a failed map even if the number is correct today.

You will not name a monitoring product. If the hall already has one, the collect duty can be satisfied by it, provided the quality and export duties are also satisfied. A product that can graph and cannot mark a stale point fails the exit, regardless of how common it is. Do not let familiarity substitute for the stale-data test.

You will not publish a point list from a site. Your point list is the functions in this chapter, plus any branch points your grouping sentence required, plus valve states. That is enough. A hundred extra points copied from a building design will bury the ones that can stop a bad heat story. Extra points are allowed after the minimum set is in the export and has been used in a real plateau. Not before.

## The command path that already exists

The working file has one page that is the control logic, and it is only one page. It is still the most concrete logic we have. Use it. Do not wait for a ladder diagram that is not in the file.

There are two sensor groups, and they are not optional duplicates. One group is the single load: supply temperature, return temperature, supply pressure, return pressure, flow. The other group is the rack side of the same boundary: the same five quantities. If you only build the first group, you can describe the heater. You cannot describe the stand-in. The page draws both. So does this chapter.

Above the sensors is a test platform with five jobs, in this order: collect, store, run a schedule, show, export. Collect is the read. Store is the file that outlives the screen. The schedule is a script, not a person clicking. Show is the live view. Export is what leaves the room. A platform that can show and cannot export has failed the page, even if the demo looked busy.

Two facts sit beside the temperatures because they change the story. Valve position, because a valve can be the hidden throttle. Leak or coolant detection, because a wet unit that still reports healthy flow is not healthy. They are alarms and records, not a research topic.

The bus on that page is Modbus, and the monitoring path is allowed to be Modbus or SNMP. That is a protocol family, not a register map and not an address. Do not publish a default address. Do not paste a site point list into the book. Do require that the points above can be read by the platform without a person typing them, and that a failed read is marked.

The command direction is the part people skip. A test task becomes a script. The script becomes a rack-level command. The rack-level command becomes the load bank’s on, off, and step. It does not become a suggestion on a local screen that someone may ignore. If the only way to change heat is a button the script cannot reach, you do not have the logic on that page. You have a heater with a laptop nearby.

Write this as six lines on the point list. Unit sensors. Rack-side sensors. Valve state. Leak state. Command echo, meaning what the script asked and what the unit did. Export. If any line is missing, the control logic is not implemented, however finished the enclosure looks.

## The stranger test for a file

Take an export from a bench run. Hand it to someone who was not there. Ask them to answer, without you: what was commanded, what heat did the liquid appear to receive, did any sample go stale, did any alarm fire, were the valves in the recorded state. If they cannot answer, the exit failed, even if you can answer from memory. Memory is not an export.

This test is the acceptance test for the data path. Do it on Gate 2 and again on a plateau in Gate 3. Gate 2 proves the points exist. Gate 3 proves they exist while heat and flow are moving. A data path that only works at idle is a data path that will be down during the only hour that matters.

## Composite: the last good value

A platform loses the flow meter for twenty minutes and repeats the last flow with fresh timestamps. Temperatures climb. The computed heat balance shows a bizarre efficiency. An engineer “corrects” the temperatures. The correction is famous for a week. The held flow is discovered later, or not at all. The fix is quality flags and a rule that a stale flow fails the plateau. The fix is not a better correction. Corrections on top of painted data are how false precision spreads.

## Composite: the door display

Another unit has a fine local display and an export that is a different set of names, updated at a different interval, missing power. The team uses the display for the acceptance conversation and files a screenshot. The screenshot becomes the record. Two months later the screenshot cannot support a heat story, and the export cannot either, and the unit “passed.” The stranger test would have failed in ten minutes. Screenshots are allowed as illustrations. They are not the export.

## Public sources for this chapter

Public documents will tell you that liquid-cooled IT is discussed in terms of flow, temperatures, and pressure. They will not give you a register map, and you should not build one by transcribing a figure. The minimum set in this chapter is the book’s own: both temperatures, both pressures, flow, on the unit and as a comparison at the boundary, plus electrical power. If a cited ASHRAE or NVIDIA document requires an additional quantity for the interface you are standing in for, add a row and cite the edition. Do not add a hundred points because a building guide had a hundred points. ASHRAE’s titled work on real-time energy measurements and on DCIM integration is about the hall’s data problem. It is the next book’s neighborhood. Here it only supports the export duties: time, unit, quality, and a file a stranger can open. Do not paste a point list from a sample chapter.

## Decisions to record

- Unit points and comparison points, with expected-difference notes.
- Sensor places on the diagram, including which sensor is allowed to remove heat.
- The interval, the clock, and the rule that a failed read is marked, not repeated.
- Collect, store, show, export, each with a do-not-ship condition.
- Alarm list with actions, latch behavior, and a non-destructive test method for each protection.
- The local stop that overrides a stuck remote command.
- A named person for the stranger test, and the file they will be handed.
