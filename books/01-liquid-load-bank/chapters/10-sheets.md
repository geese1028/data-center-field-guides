# 10. The two sheets, line by line

The early chapters told you to produce a requirements list and an acceptance sheet. This chapter sits with you while you do it. It does not fill the numbers. It fills the prompts, and it says what a weak answer looks like so you can reject your own first draft before a vendor does it for you.

Copy the headings into your own file. Leave the citation cells blank until you have a title and a revision. Do not paste this chapter into a purchase order. It is a tutor, not a specification. A purchase order that quotes a tutor is how a book accidentally becomes a contract.

## Header

Unit identity, or “unassigned” if the metal does not exist yet. File revision. Date. Sheet owner. Scope signer. Interface owner, who may be a role rather than a person in the room. Claim sentence, two clauses: represents, does not represent. Interface specification title and revision, or “unknown, due on” and a date. Coolant citation, same pattern. Electrical supply citation, same pattern.

A header without a due date on the unknowns is a header that plans to stay ignorant. Put the date. If the date slips, revise the header. Do not let the old date stand as decoration.

Weak header: “NVL72 load bank, various sites, standard coolant.” There is no standard coolant in this book. There is a citation you have not fetched.

## Row: adjustable flow

Statement: the operator named on the acceptance sheet can move flow across the band on the duty sheet and hold each declared flow point for the dwell, without rebuilding hose and without a private trick. Observed where: the path named in the authority sentence as the stand-in flow. Evidence: indicated flow and a check method, both recorded, at not fewer than two declared points. Do-not-ship if: command or handle moves and indicated flow does not, or indicated flow moves and will not hold, or only the person who built the unit can recover the point. Owner: sheet owner. Status: written, unknown, deferred, or cited.

Write the authority sentence under the row if it is short. If flow adjustment is outside the unit, this row must say so, and the limitations must forbid a claim of on-unit adjustment. Do not leave the row saying adjustable while the authority sentence says the CDU does it. That contradiction is a failed sheet, not a nuance.

Weak row: “flow control included.” Included where. Shown how. Failed how. If you cannot answer, the row is a brochure line. Delete the adjective and start again.

## Row: temperatures

Statement: supply and return temperature, as named on the diagram, are readable by a person in the room and by the export. Observed where: the taps on the diagram, not “in the system.” Evidence: both values in the export at the declared interval, with units and quality, and a check comparison that does not change the heat story or that is explained. Do-not-ship if: only one temperature exists, or the export can repeat a stale temperature with a fresh time, or the tap is in a stub that leaves the stream. Owner. Status.

Add a sub-line for which sensor, if either, is allowed to remove heat. If neither is allowed to remove heat, say which other sensor is. A temperature row with no path to a stop is a display row. Display rows do not satisfy the protection function. They can still exist. They must not be the only temperature story.

Weak row: “high-accuracy temperature.” Accuracy unnamed, location unnamed, stale-data behavior unnamed. High is not a specification. It is a mood.

## Row: flow readable

Statement: flow on the stand-in path is in the export at the same times as the temperatures. Observed where: meter location on the diagram, with installation assumptions written, including whether straight lengths are satisfied. Evidence: reading present, quality flagged, check method named at the duty point and at one reduced point. Do-not-ship if: the meter is on a bypass and labeled as heater flow, or the only “flow” is a pump curve inference you did not declare as a limitation. Owner. Status.

If you have more than one branch and you will command them independently, repeat the row per branch. A single row for a multi-branch claim is how one meter launders three paths.

Weak row: “flow meter, good brand.” Brand is not evidence. A good brand in a bad elbow is a bad reading.

## Row: pressure

Statement: pressures sufficient to form the differential pressure in the duty set are readable at the locations on the diagram. Observed where: high side and low side named. Evidence: both in the export with flow, or a differential device whose ports are drawn. Do-not-ship if: a single undirected gauge is the only pressure, or taps are valved off and still reporting. Owner. Status.

Add the absolute-pressure survival question as a sub-line, not as a performance target: weakest wetted component versus the highest source you will connect, including the bench. That sub-line connects this row to the overpressure stop. If it is blank, Gate 1 is not ready.

Weak row: “pressure monitoring.” Monitoring without a side is a word.

## Row: stepped heat

Statement: the unit can sit at the named plateaus, defined as measured electrical power unless you have explicitly defined them otherwise, for the named dwells, and can perform the sudden increase between the two plateaus you named. Observed where: power in the export, heat command in the export, liquid set in the export. Evidence: Gate 3 record. Do-not-ship if: the unit is only off or full, or percent does not correspond to measured power and you still script in percent, or the sudden increase is an undocumented stagger. Owner. Status.

List the plateaus here by name and by what kind of number they are: fraction of cited duty, or project choice. Do not list a dozen. If the list has an item no gate will sit on, delete it now. Unused plateaus become unofficial setpoints later, which is worse than not having them.

Weak row: “0–100% adjustable.” That row has never failed a unit and never will. It cannot fail a unit. Replace it.

## Row: overtemperature protection and alarm

Statement: overtemperature removes heat and latches an alarm that says overtemperature, locally, with the network dead. Observed where: the sensor you named, at the place you drew. Evidence: non-destructive test method named, to be run at Gate 2 and confirmed in spirit at a low plateau. Do-not-ship if: the only trip is silent, or the only alarm is a code with no words, or a failed sensor continues the last setpoint. Owner. Status.

Name the failed-sensor behavior in the row, not in a philosophy section. Philosophy sections are skipped on the day. Rows are not.

Weak row: “has protection.” All unsafe units have a slide that says this.

## Interface line: liquid

Statement: mating family per the cited specification, hose owner named, spare defined as plumbed or not claimed, isolation on supply, return, and spare. Observed where: the boundary on the diagram. Evidence: Gate 1 reaches and a mate-demate or joint inspection as appropriate to the family. Do-not-ship if: family does not match the citation, spare is a plug while claimed as a connection, or a hose kink is required to reach the manifold position. Owner: interface owner for the family, sheet owner for the routing. Status.

Leave the family blank rather than guessing from the last project. A blank is a question. A guess is a false part.

Weak line: “compatible with NVL72.” Compatible is the word vendors use when the family is unresolved. Make them name the family against the citation, or make yourself name it and own the risk in limitations.

## Interface line: power

Statement: delivered unit requires the supply you cited; acceptance feed is that supply or a written difference. Observed where: nameplate and the plug or hardwire point. Evidence: earth and insulation results per the rules you cited, local disconnect test, breaker-open test. Do-not-ship if: an adapter defeats earth, or acceptance ran on a feed you will not ship to and the difference is unwritten. Owner. Status.

Weak line: “standard power.” Name the citation. If the hall and the bench differ, the line is two lines. Do not average them.

## Interface line: air-cooled companion

Statement: either “not in scope” or a separate mini-sheet with steps, alarm, and power, explicitly not part of the liquid gates. Evidence: none, if not in scope. Do-not-ship if: the companion’s faults are used to waive a liquid gate, or liquid faults are waived because the air unit looked fine. Owner. Status.

Weak line: a blank that might mean out of scope or might mean forgotten. Write “not in scope” if that is the decision. Blanks on scope are how scope returns during acceptance as a surprise crate.

## Duty block

One nominal set. Columns: quantity, side of boundary, value or “cited, not copied here,” source title and revision, false story if missing, why the acceptance place exists. Rows: heat into the liquid, flow, differential pressure, supply temperature, return temperature, electrical power. Then a short list of other places: reduced, middle, full if full is not nominal, zero, overload visit. Each place has a dwell and a why.

Add a row for minimum flow for heat permitted. That row is a protection input, not a performance boast. If it is missing, the low-flow interlock has nothing to compare against.

Weak duty block: a single kilowatt number in bold, and five liquid cells marked TBD for six months. The kilowatt number will be remembered. The TBD will be forgotten. If the liquid cells are unknown, the kilowatt number is not a duty. Mark the whole set unknown rather than letting one cell look finished.

## Limitations block, started early

Open this block on the day you open the sheet, not after failure. Seed it with the refusals you already know: no universal fitting invented by this project, no overload-as-rating, no claim on CDU behavior, no claim on IT performance, no unattended heat if leak detection is absent. Add hardware limitations as you earn them. A limitations block that appears the night before the truck is a negotiation, not a record.

Each limitation: does not, therefore you must not, owner, review date. If you cannot write “therefore you must not,” the sentence is a worry, not a limitation. Worries go in a notebook. Limitations go in the file.

## Acceptance sheet header

Unit identity matching the requirements header. Requirements revision being used. Loop description and whether it meets the minimums. Feed description. Roles: sheet owner, operator, recorder, stranger. Waiver authority, written as a name or as “none on the day.” Export location. Date.

If the requirements revision on this header does not match the file you think you are using, stop. You are about to accept the wrong document. This happens when two people edited two copies. One copy wins, by the revision rule, before any valve is touched.

## Gate 1 lines

Write these as lines you can initial, not as a paragraph you can admire.

Diagram matches object in the streams named. Supply isolation reach, label, visible state. Return isolation, same. Spare matches definition. Drain and vent, or limitation already signed. Hose routing in the position of use, pressurized look, no kink, no rub. Fitting family matches citation, adapters drawn. Materials-versus-coolant row signed. Module removal and re-fit, or sealed-section limitation signed. Reaches repeated after re-fit. Labels readable with hoses on. Relief pointing, if fitted. Drip path does not enter electrical section. Fill procedure executed from the file with the author silent. Leak test at the cited condition, claim reduced if the condition was milder than the window. Valve line-up recorded.

Each line: pass, fail, not started. A line without a box will be skipped when you are tired. Boxes are the method.

Add a line: no do-not-ship cell was edited during this gate. That line protects the revision rule when everyone is standing up.

## Gate 2 lines

Feed matches, or difference written. Earth and insulation recorded against criteria. Local disconnect prevents remote heat. Breaker-open behavior matches the drawing. Identity commissioned, written here. Minimum points present with unit, time, quality. Stale-data proof performed, result attached. Stranger mapped columns to diagram at idle. One protection alarm by simulation, action and latch confirmed. Network-loss test, resulting state is heat off. Power-cycle with remote silent, resulting state is not default full load. Local and export do not disagree without a signed limitation.

If a line cannot be performed because the unit has no network, rewrite the line to the thing that exists, and limit the claim to local use. Do not mark a network line pass because there was nothing to fail. Not started, with a limitation, is the honest mark. Pass is a claim that a test happened.

## Gate 3 lines

Export started before the first command. Self-check recorded or “no self-check” already on the sheet. Ready state with heat off. Each plateau: command, measured power, dwell, heat story told or explicitly record-only, alarms explained. Sudden increase distinguished from ramp. Comparison probes unmoved during judged plateaus. Return to zero. Stranger reconstructed a plateau from the file without coaching. No band edited during the run, or waiver identifier written.

Include a line for the authority sentence: nobody trimmed a path that was supposed to be fixed, or trims were the ones allowed and were recorded. Unrecorded trims fail the gate even if the numbers look smooth. Smoothness is easy to buy with a hand on a valve and a quiet recorder.

## Gate 4 lines

Overload level and dwell are the ones on the sheet, not an extension. Exit to the named state completed. No new leak, no new kink, no stale data during the visit. Local stop practiced at a low plateau with remote command asserting. Control-power kill practiced at a low plateau. Override cleared afterward. Claim sentence still says the visit is not a continuous rating.

A line for the person whose job was to look at the unit rather than the plot: name them. If you cannot name them, the role was not filled. Do not leave it implicit that “everyone was watching.” Everyone was watching the screen. That is how hoses change shape off-camera.

## Close-out lines

Limitations page matches the gates, same day. Export opens on a machine that did not run the test. File revision bumped if the unit or the claim changed. Handoff exercise done, or explicitly not yet delivered. Second unit, if any, not declared accepted by resemblance.

The close-out is where people skip because the interesting part is over. The close-out is the delivery. A perfect Gate 4 with a missing export next month is a story you will not be able to retell. Initial the close-out with the same seriousness as the overload.

## How to use a failed line

Write the observation in one sentence. Write the disturbed lines you must repeat. Do not write the remedy as a pass. The remedy is a new attempt. Number the attempts. Attempt 1 fail, attempt 2 pass, on the same line, is a history. A single pass with the fail erased is a brochure. Keep both.

If the same line fails twice for different reasons, the design is talking to you. Two hose failures are not bad luck. They are a routing that is not fixed. Stop and change the routing requirement, or change the hardware, before a third attempt. Three attempts at the same line without a design change are how acceptance becomes a campaign to wear the recorder down.

## A fictitious walk-through, digits labeled false

Imagine a sheet where every numeric cell says “citation withheld, value not in this book.” The team still has to practice the motions. They mark nominal flow as cited. They mark a reduced flow as a project choice at “a fraction the sheet names,” without me telling you the fraction. They sit on it. The export shows a hold. The stranger says: command was the reduced plateau, flow held, temperatures moved in the direction heat would cause, quality stayed good. That sentence is a pass line and it contains no stolen number. If your real line cannot be written without a number you do not own, write the sentence and attach the number in your project file, not in a public example.

Practice that sentence once in your own words before the day. Teams who have never said a pass line out loud will write “OK” when the time comes. The sentence is a skill. The gates only create the occasion.

## Tabular Sheet 1: Liquid Load Bank Engineering Requirements

| Item / Function | Engineering Parameter & Target | Interface / Location | Verification Method | Do-Not-Ship Condition |
|---|---|---|---|---|
| Liquid Interface Coupling | Danfoss FD83-2051 (2" dual-interlock full-flow quick disconnect, C_v ≥ 12.5), female supply, male return | Rack manifold supply & return ports | Physical mating test & ball valve lockout inspection | Coupling lacks mechanical dual interlock, uses blade-level UQD adapter hose, or leaks during mate/demate |
| Nominal Thermal Duty | P_thermal = 120.0 kW into liquid stream (ΔT = 10.0 K, $35.0°C \to 45.0°C$) | Core electric heating bundle in fluid stream | Calibrated flow + RTD power balance: Q = ṁ C_p ΔT | Inferred thermal heat differs from electrical kW by > ± 3.0% at steady-state dwell |
| Flow Rate & Valve Authority | Q_v = 80.0–220.0 L/min (nominal 176.5 L/min for PG25); linear modulating TCV | Internal trim & bypass manifold | Electromagnetic / Coriolis flow meter | Indicated flow fails to hold setpoint within ± 2.0% or valve induces cavitation choke |
| Hydraulic Flow Resistance | ΔP_nominal = 115 kPa ± 10% (103.5–126.5 kPa) at 176.5 L/min rated flow | Inlet to outlet across FD83 couplings | Calibrated differential pressure transmitter (DPT) | Differential pressure deviates by > 10% from cited rack manifold resistance curve |
| Pre-Commissioning Flushing Bypass | 50-micron inline bypass strainer (V-105 loop) with differential pressure indicator | Full bypass loop isolating main heating vessel | 15-minute cold flush & basket particulate inspection | Bypass loop omitted, strainer > 50 μm, or strainer differential pressure unmonitored |
| Air-Cooled Companion Load | 15.0 kW sensible heat into data hall air (80:20 liquid-to-air heat split) | Top/rear chassis exhaust fan-coil elements | Thermal anemometer & air temperature sensors | Companion air heat omitted without written facility waiver, leaving CRAH unexercised |
| Dew Point Safety Margin | Supply temperature T_supply ≥ T_dp + 2.0 K (automated safety interlock) | Supply RTD cross-referenced with hall humidity/dew point | Automated modulating valve closure on dew point approach | Unit operates with coolant below dew point, causing condensation dripping onto equipment |
| Power Architecture | 2N Dual Feeder (Feed A and Feed B, 400V/480V 3-phase, lockable CB-101A/B) | Dual input power lugs and terminal block | Single-feed loss drop test during 100% full load | Tripping Feed A causes Feed B trip, or causes control PLC reboot / telemetry loss |
| Megger Insulation Resistance | DC 1000V applied for 60 seconds; insulation resistance R_iso ≥ 10 MΩ | Main 3-phase busbars to chassis PE frame | Calibrated DC Megohmmeter test | Measured insulation resistance < 10 MΩ, indicating coolant leakage or degraded dielectric |
| Dielectric Withstand (Hipot) | 1.5 kV AC power frequency applied for 60 seconds | Main circuits to chassis PE ground | Factory / bench calibrated Hipot tester | Any dielectric breakdown, sparkover, or current trip during 60-second dwell |
| Emergency Stop (E-Stop) | Hardwired trip dropping main contactors in ≤ 20 ms; 24VDC control logging remains alive | Local dual-channel mushroom pushbutton & remote loop | Contact opening oscilloscope timing test | Contactor drop exceeds 20 ms, or E-Stop kills 24VDC telemetry power |
| Industrial Telemetry & Export | Modbus-TCP / RTU holding registers & discrete coils; flat CSV export with quality bitmask | RJ45 Ethernet / RS-485 port and local storage | Stranger audit on flat CSV file with simulated sensor failure | Stale readings repeated with fresh timestamps; missing quality flags; proprietary raw files |

## Tabular Sheet 2: Liquid Load Bank Gate Acceptance Checklist

| Gate / Step | Inspection & Test Procedure | Engineering Criteria & Pass Limits | Recorded Field Measurement | Result | Witness Initial |
|---|---|---|---|---|---|
| Gate 1.1 | Danfoss FD83 coupling dual-interlock verification | Safety pin snaps into detent; ball valves locked closed when disconnected | [ Detent engaged / Valve lockout verified ] | Pass / Fail | [ ] |
| Gate 1.2 | Hose routing and minimum bend radius inspection | Minimum bend radius R ≥ 6D; zero kinks, rubs, or coupling neck strain | [ Measured radius: ___ mm (D = 32 mm) ] | Pass / Fail | [ ] |
| Gate 1.3 | Pre-commissioning flushing bypass & 50-micron strainer | 15-minute cold flush through V-105; basket clean of swarf, ΔP ≤ 10 kPa | [ Strainer clean / $ΔP = \_\_\_ kPa$ ] | Pass / Fail | [ ] |
| Gate 1.4 | Hydrostatic pressure hold & joint integrity | Cold hydrostatic hold at 1.5× rated pressure (9.0 bar) for 30 minutes | [ 30 min hold: 9.0 bar $\to$ ___ bar (0 leaks) ] | Pass / Fail | [ ] |
| Gate 1.5 | Drip path liquid-to-electrical isolation | 250 mL water poured over liquid section exterior with electrical doors open | [ Runoff to tray: 100% / Cabinet drops: 0 ] | Pass / Fail | [ ] |
| Gate 2.1 | Megger insulation resistance test | DC 1000V applied for 60 seconds between phases and chassis PE; R ≥ 10 MΩ | [ Measured $R_iso = \_\_\_ MΩ$ ] | Pass / Fail | [ ] |
| Gate 2.2 | Dielectric withstand (Hipot) test | 1.5 kV AC applied for 60 seconds between main power circuits and ground | [ Leakage current: ___ mA (0 breakdown) ] | Pass / Fail | [ ] |
| Gate 2.3 | Hardwired E-Stop contactor trip response | Assert mushroom pushbutton; main contactors drop in ≤ 20 ms; 24VDC alive | [ Trip time: ___ ms / PLC alive: Yes ] | Pass / Fail | [ ] |
| Gate 2.4 | Local disconnect lockout interlock | Open lockable CB-101; send remote Modbus start command; zero heater energization | [ Software override blocked: Verified ] | Pass / Fail | [ ] |
| Gate 2.5 | Modbus telemetry and stale-data proof | Disconnect flow sensor for 60s; controller marks quality bit bad; zero repeated stale value | [ Quality flag bad asserted: Verified ] | Pass / Fail | [ ] |
| Gate 2.6 | Stranger data audit at idle | Deliver idle CSV file to stranger; verify column headers, engineering units, clock | [ Stranger verified point list without assistance ] | Pass / Fail | [ ] |
| Gate 3.1 | Sequential load step plateaus (25%, 50%, 75%, 100%) | Hold 15-minute dwell at 30, 60, 90, 120 kW; thermal heat balance within ± 3.0% | [ 120 kW dwell: $Q_thermal = \_\_\_ kW$ ] | Pass / Fail | [ ] |
| Gate 3.2 | 2N single-feed loss drop test | At 120 kW load, trip Feeder A; Banks 1-2 shed instantly; Feed B & 24VDC hold | [ Feed B load stable / Zero PLC reboot ] | Pass / Fail | [ ] |
| Gate 3.3 | Sudden step response vs. hidden ramp | Step command 60 kW $\to$ 120 kW; instant command jump; thermal lag τ ≈ 45 s | [ Instant step verified / Zero stagger delay ] | Pass / Fail | [ ] |
| Gate 4.1 | Overload capacity stress dwell | Hold 135 kW (112.5% rated) for exactly 5 minutes; zero overtemp trip or hose bulge | [ 5-min dwell completed / Return to 0 kW ] | Pass / Fail | [ ] |
| Gate 4.2 | Final close-out and stranger data package audit | Complete CSV export delivered to stranger; thermal story reconstructed without author | [ Heat story reconstructed / All gates signed ] | Pass / Fail | [ ] |

## What the sheets are not

They are not a risk matrix with red and green icons. Color will be used to hide a fail inside a mostly green row. They are not a Gantt chart. Schedule does not pass a gate. They are not a vendor scorecard with weights. Weights are how a failed stale-data test becomes ten percent of a score and gets outvoted by paint. A do-not-ship cell is not outvoted. It stops the claim it belongs to.

If your organization requires a scorecard, attach it behind the sheets and do not let it edit them. If the scorecard and the sheet disagree, the sheet wins. Write that on the scorecard so the required process does not quietly become the real process.

## Public sources for this chapter

Citation cells on the sheet use the form in chapter 19: title, edition, date read, cell informed. A blank that says “see NVIDIA” fails the form. A blank that says “see ASHRAE” fails the form. The premises code and the equipment standard are two rows, not a single word, electrical. Do not paste a class table into the duty block to make it look finished.

## Decisions to record

- A requirements file with the rows in this chapter, blanks dated.
- An acceptance file with a box on every line, not a narrative in place of boxes.
- A rule that color, schedule, and weighted scores do not pass a failed line.
- One practiced pass sentence that contains no number you cannot cite.
