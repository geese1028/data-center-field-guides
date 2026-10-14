# 6. Safety

Safety in this book is a list of stops, not a site emergency plan. The project book can hold phone numbers, egress, and who to call in a particular hall. This book holds the stops that must be true of the unit wherever it is plugged in, including a bench, including a truck dock, including a room where the network is a rumor.

A stop has a sensor or a discrete cause, an action that removes or contains the hazard, a local indication, a record, and a behavior when the thing that was supposed to detect the hazard has itself failed. If you cannot fill those five, you do not have a stop. You have a warning label.

The five stops this chapter requires by name are overtemperature, overpressure, leak, electrical fault of the kinds that set things on fire or shock a person, and the wrong valve. You may add others. You may not drop these and replace them with a single “system healthy” bit.

## Overtemperature and the Class-1 hardwired safety loop

The unit’s product is heat. The failure of that product is heat in the liquid, on a surface, or in a terminal that was not meant to be the heat sink. Overtemperature protection must remove heat without asking a person to notice a trend. Trends are for the data book. Stops are for hardware and for circuits that still work when the trend display has crashed.

In mission-critical load bank engineering, overtemperature safety must be split into two tiers:
1. **Class-2 Supervisory Software Trip**: The PLC or monitoring microcontroller reads calibrated Pt100 RTD values and software setpoints. If liquid temperature drifts high, it commands contactors open via Modbus or firmware logic.
2. **Class-1 Hardwired Fail-Safe Interlock (Firmware-Independent)**: (See Figure 04). A series electrical circuit powered directly from the 24VDC contactor coil supply, passing through:
 - A red latching mushroom E-Stop pushbutton on the front panel;
 - A mechanical bimetal snap-disc thermostat welded directly to the immersion heater vessel shell (tripping mechanically at 85°C);
 - A hardware mechanical low-flow differential pressure switch (opening if flow collapses below minimum 30 LPM);
 - A containment drip-tray leak detection relay contact.

If any of these physical devices opens, the main contactor coil de-energizes immediately (< 20 milliseconds), and internal spring returns force the high-voltage contacts open. This safety action occurs even if the PLC processor is completely frozen, firmware is in an infinite loop, or the operating system is locked in a kernel panic. Software cannot override this hardwired loop. Acceptance includes pulling one of these wires and proving the contactors drop.

## Condensation and dew point interlock

Liquid load banks operating in humid or tropical facilities face a reverse thermal hazard: condensation. 

When chilled liquid enters the secondary loop below the data hall dew point (T_dp), bare metal manifolds, uninsulated EPDM hoses, and quick disconnects instantly condense water from the air. In a high-density AI room, droplets dripping onto live 400V busbars or 54V power shelves cause catastrophic phase-to-phase arc flashes.

The safety architecture must include a hard dew point interlock:
- The controller monitors data hall ambient air temperature and relative humidity (RH) to compute real-time dew point (T_dp).
- **Safety Rule**: Supply temperature must maintain an operating margin of T_supply ≥ T_dp + 2.0 K.
- If secondary loop temperature falls toward the dew point envelope, the controller must sound an alarm and immediately close modulating cooling valves or stage on minimal trim heat. Liquid cooling tests must never allow a sweating machine.

## Overpressure

The loop the load bank can influence needs a limit that does not depend on the CDU being polite. If the only protection is “the CDU will catch it,” write that assumption in known limitations, in ink, and do not claim the unit is safe on a bench pump that has no such politeness. Bench pumps are where prototypes die, because the bench pump is often capable of more pressure than the hall loop, into a closed valve the hall loop would not have closed.

Name the highest pressure you believe the cited loop, and the bench loop, can apply. Compare that with the weakest wetted component: hose, gasket, gauge, heater shell, meter body, valve body. The weakest one is the rating that matters. A strong shell does not rescue a weak gauge. Gauges fail sharp. Put a gauge range and a gauge isolation valve on the diagram if a failed gauge can spray.

Relief is the honest design when a trapped section can be pressurized beyond that weakest rating. A relief path needs a destination: a tank, a return, a place that is not a person’s face and not an electrical enclosure. A relief that relieves onto the floor without a record is a leak you intended. It still needs an alarm or an inspection step after any event, because a relief that has lifted may not have reseated.

If you choose not to fit relief, because every pressure source is external and controlled, write the assumption and the administrative control: this unit is not to be connected to an unregulated source. Then make that sentence impossible to miss in the file a stranger gets. Administrative controls are weaker than relief. They are sometimes all you have. They are never a reason to skip the sentence.

Overpressure and heat interact in a closed volume. The heat-path chapter forbade trapped heaters between closed valves, or required an interlock. This chapter repeats the consequence: a relief device is not a substitute for heat in a trapped volume, because the liquid that leaves through the relief may be hot, and the element may still be dry-firing after the liquid has left. Interlock first. Relief second. Procedure third. Do not reverse that order because a relief valve was easier to buy than a valve-position switch.

Test the overpressure story carefully. You do not need to drive the unit to destruction. You need to show that the detecting device, if you have one, alarms at a simulated pressure, and that a relief, if you have one, has a certificate or a bench test from its maker that you have filed, and that the destination of the relief is the one on the diagram. A relief pointed at a changed panel, because the panel moved after the drawing, is a failed Gate 1 item. Look at where it points, with the enclosure closed, from the position a person would occupy.

## Leak

A leak is a liquid failure and sometimes an electrical failure, in that order of time and in the reverse order of severity if the liquid is conductive and reaches a live part. Design so liquid does not have a path into the electrical enclosure. Drip lips, separation, connectors that face down, no terminal blocks in the drip plane. These are design duties. They are also Gate 1 looks. A rendering will not show the path a drip actually takes. A cup of water, used deliberately on the outside of the liquid section while the electrical section is open and powered down, will show it. Do that before you mix electricity and coolant. It is a cheap test and it embarrasses drawings, which is what you want.

Detection, if fitted, must cause an action. Minimum action: remove heat and alarm locally. Better: also close what you can close, if closing does not trap a heater that is still hot. Think that sequence through. Close valves, then heat off, is the wrong order if closing traps heat. Heat off, then isolate, is usually the right order. Write the order.

A leak alarm that only exists on a screen in another room is a report. It is not a protection for the person standing next to the unit. Local indication has to work with the network dead. A lamp, a horn, a flag. Pick one that can be heard or seen in the room you will actually use. Then test it by simulation. A wet test on a sensor probe, done so the liquid cannot reach live parts, is better than a software bit if the sensor is the thing that will fail in service. Software bits do not get wet.

No leak sensor is an allowed limitation for a prototype that is never left alone and is used only on a bench with a person whose job is to watch. It is a poor limitation for a unit that will be left at a plateau while people look at a CDU. Match the limitation to the way the unit will be used. If the use changes, the limitation must be reopened. Limitations are not permanent gifts.

## Electrical: 2N dual feeders and dielectric withstand thresholds

Insulation and protective earth are acceptance items, not a paragraph in a manual no one opens. In industrial load bank commissioning, “the electrician said OK” is not a test record.

Two electrical standards govern Gate 2 acceptance:
1. **Insulation Resistance (Megger Test)**: Apply DC 1000V for 1 minute between the main power circuit and the grounded chassis frame. The measured insulation resistance must be ≥ 10 MΩ. Any lower resistance indicates moisture ingress, compromised conductor insulation, or internal coolant leakage.
2. **Dielectric Withstand Test (Hipot)**: Subject the main circuit to power-frequency 1.5 kV AC for 1 minute with zero dielectric breakdown, flashover, or trip.

Furthermore, mission-critical AI data centers utilize a **2N dual-feeder power architecture (Feed A and Feed B)**. Racks are dual-corded, with each feeder fed from independent upstream UPS and PDU lines. A prototype liquid load bank must mirror this dual-corded reality:
- **Feeder Separation**: Feeder A powers Heating Banks 1 & 2; Feeder B powers Heating Banks 3 & 4. Each feeder features its own lockable molded case circuit breaker (CB-101A and CB-101B).
- **Control Power Survival**: The internal 24VDC control power supply must be dual-fed via a diode-OR redundancy module. 
- **Single-Feed Loss Drop Test**: During Gate 3 testing at 100% load, operator intentionally trips Feeder A. The load bank must instantly shed Banks 1 & 2 without causing Feeder B to trip on overcurrent or inrush transient. Crucially, the control bus, PLC, flow meter, and temperature sensors must not suffer even a microsecond brownout. If losing one feeder reboots the controller or freezes the export, the unit fails 2N acceptance. (See Figure 04 for the dual-feeder and control bus schematic).

Conductive coolant and a leak into a terminal is the combined failure. The drip test and the earth test are how you cheapen that combination. Do not wait to “see if the coolant is really conductive.” Assume a leak can become a shock or a trip, and keep liquid and live parts apart. If a design cannot keep them apart, it is not finished.

Lockout matters for service. Module removal and any work that opens the electrical section need a way to make heat and unexpected motion impossible. A local disconnect, lockable, visible, is the usual answer. A software “service mode” is not a lockout. Acceptance includes opening the disconnect and confirming heat cannot be commanded remotely while it is open. Remote start that ignores a local disconnect is a failed unit, not a feature.

## Wrong valve

The spare port, the bypass, and the isolation valves will be found in the wrong state. This is not a slur on operators. It is a count of handles. Every handle will, at some point, be left where the last task needed it.

Label handles by function, in words a stranger can match to the one-line diagram. “V3” is not a function. “Return isolation” is a function. If you need both, use both, and make the function the large text. Labels that face the wall fail Gate 1. Labels that fall off fail Gate 1. Acceptance includes a hand on each valve and a comparison to the diagram, not a glance at a list.

Wrong valve is also an interlock problem where the valve can trap heat or dead-head a path you said was protected. Position switches on those valves are how the interlock becomes real. Without switches, the interlock is a procedure. Procedures are Gate checks and run checks. They are weaker than switches. If you rely on procedure, the acceptance sheet and the run sheet must both include the valve line, and a missed line is a failed start, not a coaching moment. Write that.

The spare brought into service without a retest is a wrong-valve event of a special kind. The hydraulic path changed and the record did not. The liquid chapter already said a swap requires a named person and a retest. Here the safety consequence: a spare path that is uninstrumented can put full heat through a path with no flow reading. Forbid heat on an uninstrumented spare, by procedure or by switch, or instrument it. Do not leave the combination available and unnamed.

## What stays out of this chapter

Phone numbers, room names, egress maps, chemical-handling plans for a particular hall, and medical advice. Those are real, and they are not properties of the load bank. Putting them here would make the book look complete and make the unit look specified when it is not. Point to the project book. Then check that your unit does not assume a response time that only one hall can provide. A stop that needs someone to arrive in one minute is not a stop on the unit. It is a hope about the building. Convert it into a stop on the unit, or write the dependency as a limitation that forbids unattended heat.

Fire suppression interfaces, if a building requires them, are a project interface. The unit’s contribution is a contact that means “heat is commanded” or “fault,” if the project needs it, tested like any other discrete. Do not pretend this book designs the suppression system.

## Composite: the polite CDU

A prototype is always tested downstream of a CDU that trips at a sensible pressure. The unit has no relief and no pressure switch. The limitations page never gets the sentence about unregulated sources. On a bench, a temporary pump and a closed isolation valve meet. The weakest gauge fails. Nobody is injured because the gauge happens to point at a panel. The panel is then redesigned, and the gauge is replaced with the same range, and the sentence is still missing. The fix is the sentence, the comparison with the bench source, and a relief or a pressure switch that does not need the CDU. The fix is not a new panel.

## Composite: the software limit

Overtemperature is a number in a controller. The contactor is driven by a different board that holds last state on loss of communication. The controller reboots during a sag and comes back slowly. The contactor stays in. The software limit is not in force for the minute that matters. The safe-state test, kill control power, and the separate test, kill the link between controller and contactor, would have shown it. Those tests are acceptance tests. They are boring. They are the chapter.

## Public sources for this chapter

Electrical control is two citations, not one copied article. The feed is governed by the premises code the hall adopted: NFPA 70, the National Electrical Code, in the United States, in the adopted edition, or the local adoption of IEC 60364 or the national wiring rules. The unit is governed by an equipment standard. IEC 60204-1, electrical equipment of machines, is the usual international reference for a heater with a control circuit and a disconnect. The mark the builder claims, if any, names the product-safety standard. Write both editions on the sheet. Do not transcribe code text into the gate. Transcribing a code is a copyright problem and a maintenance problem, because the adopted edition will move.

The behaviors this book requires are its own, and they are the ones the gates test. Lockable disconnect that remote command cannot override. Overcurrent that removes heat, with the control-supply state known. Protective earth tested. Loss of control power removes heat. Stop does not ask the network. Liquid does not track into live parts. Where the cited edition specifies a test method, use that method and cite it. Where it does not, write the method. Do not invent a clause number.

ASHRAE’s bulletin titled “Data Center Power Equipment Thermal Guidelines and Best Practices” is about the thermal environment of power equipment. Cite it if the project needs that subject. It is not the wiring code, and it is not extracted here.

## Decisions to record

- For each of the five stops: sensor or cause, action, local indication, record, failed-sensor behavior.
- Thresholds cited or labeled as your choice. No invented universal numbers.
- Non-destructive test method for each protection, written before the prototype is hot.
- Control power versus heater power, and the open-breaker test.
- Valve labels and which valves are procedure-only versus switched.
- The limitations that forbid unattended heat, if detection or relief is absent.
- Confirmation that hall emergency plans were not used as a substitute for a unit stop.
