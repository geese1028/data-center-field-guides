# 2. Before heat

A liquid load-bank flash report opens with a mandatory preparation block. This block is evaluated as pass or fail long before the first kilowatt of heat is energized. A failed preparation gate does not become an acceptable, mild anomaly during the later gradient; it halts the testing campaign immediately. Claiming that a thermal test succeeded when the pre-heat preparation failed is an engineering contradiction.

In high-density liquid cooling, the pre-heat phase establishes the zero-baseline of the entire thermodynamic universe. If your baseline is contaminated with air bubbles, uncalibrated sensor offsets, or unverified electrical feeds, every subsequent energy-balance calculation will be fundamentally corrupted.

## The four preparation gates

Before any heat command is issued to the contactors, the test team must verify and initial four sequential preparation gates:

### Gate 1: All units filled, de-aerated, and vented
Liquid load banks cannot tolerate trapped air. In an immersion heating vessel, an air pocket creates a localized dead zone where liquid cannot circulate. The moment electrical power is applied, the exposed element sheaths will experience rapid dry-fire thermal runaway, blistering the Incoloy sheath, scorching the internal baffle seals, and tripping high-temperature snap switches within seconds.

The preparation block requires physical evidence that:
- The entire wetted circuit—including the internal heating vessels, the 50μm pre-commissioning bypass loop, the manifold drop hoses, and the Danfoss FD83 quick-disconnect couplings—has been fully flooded with the designated heat transfer fluid (e.g., PG25).
- All high-point manual air bleed valves and automatic air vents (AAVs) have been opened, vented until continuous bubble-free liquid discharges, and then securely seated.
- Visual sight glasses or de-aeration chambers confirm zero frothing or micro-bubble entrainment under full circulation pump pressure.

### Gate 2: Electrical power feed verified to engineering specification
The electrical feed delivering power to the load bank must match the declared design basis, not a temporary convenience connection that someone hopes to overlook.
- Verify line-to-line voltages across all phases (V_AB, V_BC, V_CA) with a calibrated digital multimeter at the load-bank main circuit breaker terminals. Phase unbalance must satisfy V_unbalance ≤ 1.0%.
- Verify correct clockwise phase rotation (A-B-C) to prevent reverse rotation of internal auxiliary ventilation blowers.
- Measure ground-loop impedance and verify that the equipment grounding conductor (EGC) is bonded to the facility ground bus in strict compliance with NFPA 70 (NEC Article 250) or IEC 60364-5-54.
- Conduct a live operational test of the lockable main disconnect switch to prove that the unit can be completely de-energized and mechanically locked out in an emergency.

### Gate 3: Comprehensive unit self-check passed
Every load-bank cabinet in the test cluster must execute its built-in self-test (BIST) sequence:
- The supervisory PLC must cycle all control relays and verify that main immersion contactors operate freely without mechanical binding, excessive contact bounce, or humming.
- The Class-1 hardwired safety loop must be verified: pressing the front-panel emergency stop (E-stop) mushroom button must drop all contactor control coils in under 20 milliseconds.
- The internal leak detection rope or optical float sensor in the bottom containment basin must be tested to ensure it triggers an immediate hardwired shutdown.
- All digital communication channels (Modbus-TCP / MQTT) must report zero active alarm flags, and the 16-bit Quality Bitmask must initialize to a healthy state (`0x0001` - `0x0007`).

### Gate 4: Stable ten-minute zero-load baseline run
Once Gates 1 through 3 are complete, the entire test cluster must circulate coolant at full rated flow with all heating elements strictly de-energized (commanded to zero watts).

This zero-load run must be sustained for a continuous duration of at least **ten minutes** (or the specific baseline duration pre-declared on your requirements sheet). The purpose of this hold is to allow the cold loop to achieve hydraulic equilibrium and to expose any sensor drift, communication drops, or dead channels before thermal noise enters the stream.

If an operator becomes impatient and applies "just a little heat" (e.g., 5kW) to warm up the room, that period cannot be used as the preparation baseline. Commanding partial heat during the baseline destroys the zero-reference. If heat is applied prematurely, stop the test, de-energize the heaters, and restart the full ten-minute clock from scratch.

## What you record during the baseline

During the final minute of the ten-minute zero-load stabilization run, record a continuous one-minute baseline block. This block must capture:
- **Electrical Channels**: Active power P_elec must read exactly 0.0 kW across all cabinets (auxiliary parasitic blower power, typically 0.8kW, must be recorded on a separate line and not conflated with heater power).
- **Hydraulic Channels**: Supply coolant temperature (T_in), return coolant temperature (T_out), volumetric flow rate (Q_v), supply static pressure (P_in), and return static pressure (P_out).
- **Companion Air Channels**: Ambient intake air temperature (T_air,in) and discharge air temperature (T_air,out).

In a healthy zero-load baseline, the temperature difference across the heating core (ΔT = T_out - T_in) will typically be slightly positive—on the order of +0.05 K to +0.15 K—due entirely to the mechanical pumping power converted into viscous friction heat within the piping and CDU pump impellers (P_friction = Q_v · ΔP). Documenting this tiny offset is critical: it prevents an auditor from later misinterpreting pump friction heat as an electrical calibration error during low-load steps.

Every sensor channel that will appear in subsequent gradient data blocks must already be present, reading, and healthy during this baseline minute. A sensor that suddenly "appears" in the export halfway through the gradient test was not verified during preparation. Its data cannot be used to prove compliance.

## Hydraulic resistance baseline: The cold impedance curve

If your requirements sheet includes the duty to stand in for the physical rack's hydraulic resistance curve (the k_v or C_v relationship between flow and pressure drop), the preparation phase is where that claim is calibrated.

Cold coolant (e.g., PG25 at 35.0°C) exhibits a higher kinematic viscosity ($\nu ≈ 2.85 cSt$) than hot coolant at 45.0°C ($\nu ≈ 2.15 cSt$). As a result, the cold baseline pressure drop across the load bank will be slightly higher than the hot steady-state drop. 

During the zero-load preparation run:
1. Measure the differential pressure across the manifold supply and return ports (ΔP = P_in - P_out) at rated flow (176.5 LPM).
2. If the load bank includes an adjustable manual balancing valve (such as a calibrated triple-duty balancing valve), adjust the trim handle until the measured ΔP matches the cited virtual rack impedance curve (e.g., 112.0 kPa ± 3.0 kPa).
3. Lock the balancing valve position with a mechanical memory stop or tamper-evident seal.
4. Record the final valve position, the cold fluid temperature, and the measured ΔP on the preparation sheet.

This adjustment is a physical setup baseline. It is not an experimental result. You do not write "PASS" for hydraulic resistance during preparation; you record the setup fact so that when the later 120kW thermal gradient runs, any change in differential pressure can be attributed honestly to temperature-dependent viscosity shifts rather than unrecorded valve tampering.

## Decisions to record

Before issuing the command to ramp to the first load step, record the following facts in the preparation section of the flash report:

- Initials of the technician confirming air venting and de-aeration for every cabinet.
- Measured line-to-line voltages and ground loop resistance for Feeder A and Feeder B.
- Confirmed tripping time (< 20ms) of the Class-1 emergency stop circuit.
- The exact start and stop timestamps of the 10-minute zero-load stabilization run.
- The arithmetic mean values of all electrical, hydraulic, and air channels during the final baseline minute.
- The locked position of the hydraulic balancing valve and the measured cold ΔP.
- The signature of the Sheet Owner certifying that all four preparation gates have achieved PASS.
