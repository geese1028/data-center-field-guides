# 0. How to use this book

This book is about the flash report. Not the physical machine, and not the complete facility hall. The first book (*Design and Build a Liquid Load Bank for NVL72 Racks*) accepted the prototype load bank on the shop floor and at the bench. The third book (*Finish a Liquid Cooling Verification*) runs the comprehensive data hall commissioning campaign and leaves seven permanent operational sheets. This volume sits precisely between them: it governs the data that leaves the machine. It tells you what a test run must record, how raw telemetry is audited, and what mathematical evidence must exist in the file before anyone in the room is legally or technically permitted to write "PASS."

In mission-critical data center engineering, a liquid cooling test is not valid because an afternoon felt smooth, because a vendor smiled, or because an uncalibrated monitoring dashboard rendered a calm, horizontal line. A calm line is frequently the signature of a frozen buffer or an unpolled register. This field guide provides the rigorous methodology required to turn high-density liquid and air load-bank runs into an immutable, audit-grade flash report that a stranger can reconstruct from first principles.

The structure of this report is derived from actual operational commissioning campaigns executing Level 4 Functional Performance Testing (FPT) and Level 5 Integrated System Testing (IST) across megawatt-scale AI computing facilities. Where this method requires a flow rate, an operating temperature, a differential pressure, or an electrical voltage, this book preserves the cell and insists that the limiting value be filled from your own engineering specification or the equipment document then in force, cited by document title and revision. Do not invent an operating threshold out of folklore, and do not copy numbers from an obsolete drawing because a previous air-cooled hall happened to use them.

When you finish, you must be able to hand an independent auditor a flash report containing five explicit scene passes, a multi-cabinet consistency check, and an exhaustive data block for every commanded load plateau. If even a single required pass cannot be written, the overall test verdict is not a pass. A pretty curve does not outvote a blank cell.

## What this volume owns

This book owns the translation of live physical phenomena into an immutable digital record. Specifically, it owns:

1. **The Preparation Block**: The pre-heat validation gate that proves the test cluster is full, vented, properly powered, and thermally stable before a single watt of heat is energized.
2. **The Five Scene Passes**: The definitive five-line audit structure—Pretest, Gradient, Overload, Step Change, and Single-Feed Fault—that prevents partial demonstrations from masquerading as full verifications.
3. **Multi-Cabinet Consistency**: The statistical application of the Coefficient of Variation ($CV = \frac{\sigma}{\mu} \times 100\%$) across parallel load-bank cabinets to identify hydraulic imbalance, manifold starvation, and electrical phase asymmetry.
4. **Metrology & Sampling Rigor**: The strict distinction between 1-second raw turbulent samples and 60-second rolling means, accompanied by the variance check (σ² > 0) that immediately exposes frozen-register fraud.
5. **Thermodynamic Heat Reconciliation**: The first-principles energy balance comparing commanded electrical power against secondary liquid enthalpy absorption and companion air heat release (P_elec = Q_liquid + Q_air + Q_loss).
6. **Telemetry Hop Architecture**: The deterministic journey from physical immersion RTDs and vortex flow meters through Modbus-TCP registers and MQTT brokers, enforcing strict bans on painted gaps, stale repeats, and cached retained messages.
7. **Algorithmic Changepoint Rules**: The precise operational boundaries governing online detectors (Focus, FLOC) and offline fits (CPOP), establishing that algorithms serve only as rulers to suggest candidate inspection windows, never as automated sign-off authorities.

What this book does not own: it does not design your building hydronic plant, it does not size your central cooling towers or chillers, and it does not configure your site-specific DCIM network switches. Those belong to the facility design basis and the project book. This book stops at the boundary of the test file.

## Four distinct human roles

A test file cannot be audited if the person who wrote the software is the same person who signs the acceptance of its data. This book requires four distinct human roles to be named on the cover page of every flash report, even if staffing constraints require individuals to share duties across non-conflicting lines:

- **1. The Sheet Owner (Specification Custodian)**: The engineer who owns the technical requirements sheet and the cited document revision. The Sheet Owner ensures that all limits, floor values, and dwell intervals match the frozen design basis. The Sheet Owner is strictly forbidden from quietly weakening a stop condition or waiving a failed cell in the hallway during the pressure of a test run.
- **2. The Operator (Control Pilot)**: The technician or test engineer who commands the load bank stages, operates balancing valves, commands step jumps, and executes breaker trips. The Operator must not be the author of the controller's internal telemetry firmware.
- **3. The Recorder (Objective Chronicler)**: The person who logs chronological timestamps, notes raw register alarms, records boring passes, and documents uncommanded transients without smoothing the curve or discarding "inconvenient" initial runs.
- **4. The Stranger (Independent Audit Authority)**: An engineer or commissioning agent (CxA) who was not involved in the fabrication of the load bank or the installation of the temporary piping. The Stranger is handed the un-retouched raw CSV export and must be able to independently verify every mathematical claim without verbal coaching from the test crew.

If your commissioning team consists of only two people, the Stranger must still be an outside party—an owner's representative, a quality manager, or an engineer from an adjacent shift. Self-acceptance is the root cause of stale data surviving into production.

## What you may copy and what you may not

You may copy the structural headings of this field guide into your own engineering templates: the preparation block, the five passes, the consistency criteria, the step data blocks, and the external gear boundaries.

You may not copy a paragraph from this book into a vendor contract and call it an engineering specification. You may not paste a marketing rendering into the report and call it an equipment drawing. And you may not paste an unverified vendor CSV export into your handover package and call it an independent analysis.

## How to read and apply this guide

Read this field guide through once from start to finish to understand the interdependent architecture of the data pipeline. Then, execute the flash report in the exact chronological order of the testing day:

1. Record the preparation block and establish the cold baseline minute before commanding heat.
2. Verify all pretest cells against the cited engineering limits.
3. Walk the active scenes: the stepped gradient, the overload visit, the sudden step change, and the 2N single-feed loss drop test.
4. Execute the multi-cabinet consistency analysis across all parallel cabinets.
5. Compile the step data blocks and reconcile the thermodynamic heat balance.
6. Audit the telemetry stream for frozen registers and stale repeats.
7. Initial the final sentence or file the explicit refusal.

A skipped chapter or an unrecorded cell is how an unverified 60-second burst becomes an illegitimate 30-minute steady-state claim. Follow the method.

## Decisions to record

Before opening the first valve or powering the control bus, record these facts in ink:

- The unique Run Identification code (e.g., `LB-TEST-2026-H01-A`) and the data hall location.
- The exact document title and revision mark of the requirements specification then in force.
- The names and signatures of the four designated roles: Sheet Owner, Operator, Recorder, and Stranger.
- The full list of parallel load-bank cabinet serial numbers included in the test cluster.
- The list of scenes this specific run is contracted to attempt.


# 1. The five passes

A rigorous flash report does not open with a narrative, an executive summary full of optimistic prose, or a curated photograph of green status LEDs. It opens with five explicit lines arranged in an unyielding table at the very top of the first page:

1. **Pretest**: Was the machine and the connected hydronic loop fit to test before any heat was added?
2. **Gradient**: Did the system demonstrate recognizable, stable plateaus across all commanded load steps?
3. **Overload**: Was the visit above rated nameplate capacity safely entered, verified, and cleanly exited?
4. **Step Change**: Did sudden load increases and decreases arrive as true steps without inducing control oscillation or water hammer?
5. **Single-Feed Fault**: Did one independent electrical feeder trip cleanly without destabilizing the secondary feed or knocking out control power?

Each of these five lines must be recorded as **PASS**, **FAIL**, or **NOT RUN**. (See Figure 01 for the definitive one-page flash report layout and the five-pass audit table).

The overall test verdict is **PASS** if, and only if, every single line you attempted was marked **PASS**. If any attempted line is marked **FAIL**, the overall test is **FAIL**. If a line was omitted from the day's schedule, it is recorded as **NOT RUN**, and the overall claim shrinks strictly to the scope of the lines you actually executed. Under no circumstances may an unattempted line be quietly omitted to present a false impression of full verification.

## Why five lines

A single time-series curve can appear deceptively calm while hiding a catastrophic operational defect. If an inexperienced engineer looks only at a 30-minute flat stretch of return liquid temperature, they may conclude that "the test passed." Yet within that same hour:

- The initial hydraulic flow may have hovered below the manufacturer's cavitation floor before heat was energized (failing the **Pretest** line);
- The intermediate load steps between zero and full capacity may have exhibited severe thermal overshoot or hunting (failing the **Gradient** line);
- The load bank may have tripped on thermal runaway within 30 seconds of touching 110% overload (failing the **Overload** line);
- An emergency step shed may have caused an un-ramped solenoid to slam shut, triggering an acoustic water hammer surge that stressed manifold ferrules (failing the **Step Change** line);
- Or dropping Feeder A may have caused the internal 24VDC power supply to brown out, rebooting the supervisory controller and losing telemetry for three minutes (failing the **Single-Feed Fault** line).

The five-line structure eliminates this ambiguity. It decouples disparate engineering competencies—hydraulics, steady-state thermal capacity, overload endurance, dynamic control response, and electrical redundancy—into separate, non-negotiable verification gates. 

You may reduce the scope of the test before the day begins: if site utility constraints preclude running the overload visit, write that reduction on the first page of the test plan in ink, signed by the Sheet Owner. But a reduction discovered while examining the plot after the run is not a clever editorial optimization. It is a failed line that someone is attempting to conceal.

## The technical definition of each line

### 1. Pretest
The pretest line audits the cold, baseline hydraulic and electrical state of the system during the mandatory 10-minute zero-load stabilization window. It evaluates three specific cells against the cited engineering specification:
- **Volumetric flow rate per cabinet**: Must exceed the minimum cooling floor (e.g., Q_v ≥ 170.0 LPM for an NVL72-class 120kW virtual unit) to ensure heater elements remain fully submerged in a high-velocity convective regime.
- **Coolant supply temperature**: Must sit within the declared facility commissioning envelope (e.g., 35.0°C ± 1.5 K) and maintain at least a 2.0 K safety margin above the data hall dew point (T_in ≥ T_dp + 2.0 K).
- **Manifold differential pressure**: Must remain below the maximum allowable rack hydraulic impedance (e.g., ΔP = P_in - P_out ≤ 115.0 kPa).

If any of these three pretest parameters is out of bounds, the machine is not fit to test. Energizing heat against an inadequate flow or an out-of-spec supply temperature corrupts all downstream heat-transfer physics.

### 2. Gradient
The gradient line evaluates whether the load bank can sit on distinct, recognizable thermal plateaus across its operating range. A standard gradient walks through quarters of rated duty: 25% (30kW), 50% (60kW), 75% (90kW), and 100% (120kW). 

To pass the gradient line, every plateau must satisfy three criteria:
- **Adequate dwell duration**: The hold must last at least 15 continuous minutes at each plateau, allowing the thermal mass of the fluid loop and wetted vessel metal (τ ≈ 45 s) to stabilize completely.
- **Thermodynamic heat closure**: The inferred heat absorbed by the liquid stream (Q_liquid = ṁ C_p ΔT) must match commanded active electrical power within ± 3.0% after subtracting verified companion air load and skin losses.
- **Stability and lack of drift**: Coolant temperature rise (ΔT) must not exhibit monotonic upward drift during the final 5 minutes of the dwell.

### 3. Overload
The overload line verifies the thermal and electrical design margin of the system by testing a temporary excursion above 100% nameplate rating—typically 110% (132kW for a 120kW baseline) held for a strict, pre-declared duration of 5 minutes.

The overload line is explicitly defined as a **visit**, never as a permanent operating rating. The line passes if the unit enters the overload level smoothly, sustains the hold without tripping thermal overtemperature switches, experiences no contactor chattering or cable overheating, and cleanly exits back to rated load or zero. The line fails if any protection switch lifts, if liquid boils at the sheath boundary, or if the test crew extends the visit beyond the pre-declared window to boast about performance.

### 4. Step Change
The step change line examines the transient dynamic response of the liquid load bank and its associated facility CDU control loops during sudden, large-amplitude power transitions. Standard verification includes an instantaneous jump from low load (25%) to full load (100%), followed by an immediate shed back to low load.

The step change passes if:
- Commanded electrical power transitions cleanly in less than 1.5 seconds without causing upstream breaker trips;
- The modulating cooling control valve (TCV) tracks the surge smoothly without hunting, valve bounce, or sustained limit-cycle oscillation;
- Rapid valve actuation does not produce destructive hydraulic water hammer (manifold static pressure surge must satisfy ΔP_surge ≤ 15.0 kPa).

### 5. Single-Feed Fault
The single-feed fault line audits the 2N electrical distribution architecture. In modern mission-critical data centers, IT racks are powered via dual independent feeds (Feeder A and Feeder B). A liquid load bank standing in for an NVL72 rack must replicate this dual-path power architecture.

During the single-feed test, with the unit operating at 100% rated capacity, an operator manually trips the circuit breaker for Feeder A. To pass:
- Contactor auxiliary logic must instantly (< 20ms) shed Bank 1 & 2 heater elements;
- Feeder B must seamlessly carry Bank 3 & 4 (50% rated load) without sustaining inrush transients that trip upstream breakers;
- Crucially, the 24VDC supervisory control bus, PLC, immersion sensors, and Modbus/MQTT telemetry engines must experience **zero brownout dip**. If losing Feeder A causes the PLC to reboot, drops communication, or freezes the data export, the unit fails the single-feed line instantly.

## "Not run" is not a fail, and it is not a pass

There is a vital distinction between a failed test and an unexecuted test:
- **NOT RUN** means the testing schedule, site limitations, or contractual scope deliberately excluded that scene. The report marks the line "NOT RUN" and clearly notes the boundary. The remaining lines may still stand as valid engineering evidence for their specific claims.
- **FAIL** means the scene was attempted, and one or more acceptance criteria failed to satisfy the cited specification.

Under no circumstances may an unexecuted scene be converted into a pass by omitting the row from the report, nor may a failed run be euphemistically recast as "NOT RUN" by deleting the offending timestamps. The timestamps in the raw CSV export provide an auditable chain of custody. Deleting a time range to hide an aborted step is a fraudulent alteration of the engineering record.

## The overall verdict rule

Place the five lines in a prominent summary box at the very top of the flash report, directly beneath the metadata block. An executive, an owner's engineer, or a third-party auditor who reads only this first page must instantly understand the true status of the campaign.

The overall verdict can be:
- **OVERALL PASS**: Every one of the five lines was attempted, and every line achieved PASS.
- **CONDITIONAL / PARTIAL PASS**: Certain pre-agreed lines were NOT RUN (e.g., Overload excluded by site utility constraints), but all attempted lines achieved PASS. The narrative must explicitly state: *"Overall Pass is limited to Pretest, Gradient, Step Change, and Single-Feed; Overload was not evaluated."*
- **OVERALL FAIL**: One or more attempted lines resulted in FAIL. The report must state the exact failure mode, the time of occurrence, and the corrective action required before a re-test is permitted.

A pretty curve from a 15-minute steady run does not outvote an un-run pretest or a failed single-feed test. The five lines stand together.

## Decisions to record

Before initiating data logging for the flash report, the test team must record:

- Which of the five scenes this specific test run will attempt.
- The exact document titles and revisions governing pass/fail criteria for each line.
- The pre-declared dwell times for the gradient plateaus and the overload visit.
- The pre-agreed wording of the overall verdict statement if all attempted lines pass.
- The designated stopping procedure if any single scene triggers a FAIL.


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


# 3. The pretest cells

The pretest gate asks a blunt, unyielding question: is this load bank cluster, on this specific day, operating inside the hydraulic, thermal, and electrical boundaries defined by the cited engineering specification?

The pretest is not the thermal gradient. It is the gatekeeper that permits the gradient test to count. If any pretest cell is out of bounds, you do not proceed to step-load testing. Attempting to run a 120kW heat test on a hydronic loop that cannot deliver its rated volumetric flow or that enters at an out-of-spec temperature will merely produce an invalid, unrepeatable heat balance that wastes hours of facility run-time.

## The liquid pretest cells

For secondary liquid loops simulating high-density AI clusters, the pretest section of the flash report requires three distinct hydraulic cells, evaluated per cabinet and across the manifold:

### 1. Volumetric flow rate per cabinet (Q_v)
The specification must declare a minimum flow floor (e.g., Q_floor ≥ 170.0 LPM for an educational 120kW NVL72-class reference model operating at ΔT = 10.0 K). 

- **Audited Parameter**: Measured volumetric flow rate entering each parallel cabinet under full facility CDU circulation.
- **Why the Cell Fails**: If flow drops below the floor (for instance, reading 155.0 LPM due to an un-opened balancing valve, an undersized hose ferrule, or a partially clogged strainer), liquid velocity across the heating elements drops. At lower velocities, convective heat transfer coefficients degrade, boundary layer sheath temperatures spike, and the fluid undergoes excessive localized thermal expansion.
- **Per-Cabinet vs. Header Sum**: The pretest line must record the flow for *each individual cabinet*, not merely the total secondary loop header flow. A header flow of 700 LPM across four cabinets can appear perfectly healthy while hiding a lethal hydraulic imbalance: Cabinets 1, 2, and 3 may receive 200 LPM each, while Cabinet 4 is starved at 100 LPM. If Cabinet 4 is starved, Cabinet 4 fails the pretest line immediately.

### 2. Coolant supply temperature (T_in)
The secondary loop supply coolant delivered by the facility CDU must sit squarely inside the declared commissioning envelope (typically 35.0°C ± 1.5 K for ASHRAE W4/W5 warm-water liquid architectures).

- **Audited Parameter**: Primary liquid supply temperature measured by an immersion 4-wire Pt100 RTD penetrating the high-velocity core stream ($1/3 \sim 1/2 D$) of the manifold drop.
- **The Dew Point Safety Floor**: In addition to the nominal setpoint band, the pretest must verify that supply temperature satisfies the absolute non-condensation rule:
 $$T_{\text{in}} \ge T_{\text{dp}} + 2.0\,\text{K}$$
 where T_dp is the live dew point calculated from data hall dry-bulb temperature and relative humidity. If chilled coolant enters at 18.0°C while the data hall dew point is 21.5°C, uninsulated quick disconnects and EPDM hoses will sweat profusely, dripping water directly onto underlying electrical trays. That is an immediate pretest FAIL.
- **Temperature-Dependent Flow Adjustment**: If the facility loop is running colder than nominal design (e.g., entering at 25.0°C on an unconditioned morning), the fluid viscosity increases by nearly 30%. The flow floor must cite the temperature at which it was calibrated. A flow floor copied from a 40.0°C test cannot be directly applied to a 20.0°C fluid without hydraulic correction.

### 3. Manifold differential pressure (ΔP)
The hydraulic impedance across the load bank must match the physical IT rack's certified pressure drop curve within a pre-declared tolerance (typically ΔP_rated = 112.0 kPa ± 5.0 kPa at 176.5 LPM).

- **Audited Parameter**: Static differential pressure measured between the supply inlet manifold tap and return outlet manifold tap (ΔP = P_in - P_out).
- **Inspection for Fraudulent Taps**: The pretest must verify that pressure taps are clean, deburred, perpendicular to the pipe wall, and equipped with snubber valves to eliminate high-frequency turbulence noise. A differential pressure reading taken across throttled isolation ball valves or restrictive adapters measures pipe friction, not rack impedance.

## The companion air pretest cells

If your test campaign includes an air-cooled companion load (which is mandatory when verifying the 80:20 or 85:15 sensible heat split of NVL72-class architectures), the pretest section must include two dedicated air cells:

1. **Intake Air Temperature (T_air,in)**: Ambient dry-bulb air entering the load bank's front perforations must sit within the facility design range (typically 22.0°C to 27.0°C in accordance with ASHRAE TC 9.9 Thermal Guidelines). If return air from a previous uncontained test has short-circuited into the intake, elevating T_air,in to 42.0°C, the air section will experience early thermal throttling.
2. **Auxiliary Blower Airflow Velocity**: Air velocity across the auxiliary heating stages must be confirmed using a calibrated hot-wire anemometer or differential pressure sensor across the intake filter grille, ensuring that airflow meets the minimum convective threshold (Q_air ≥ 1200 CFM per 20kW air module) to prevent element overheat.

If the air companion load is excluded from the contract scope, the cell must be explicitly marked **NOT APPLICABLE (N/A)** in ink prior to the run. You may not discover halfway through the pretest that an air velocity meter was forgotten, and then retroactively claim that air testing was "not applicable."

## Match the document, do not become the document

A common pitfall in commissioning reports is copying pages of vendor marketing datasheets into the appendix and claiming that the test "matches the datasheet."

A vendor datasheet is a commercial proposal. It is not an engineering verification. The flash report must maintain a strict, professional separation:
- The requirements sheet defines the cited limit (e.g., *"DOC-NVL72-SPEC Rev 2.4, Table 3: Minimum secondary flow = 170.0 LPM"*).
- The pretest table records the actual observed number measured by a calibrated instrument on the test floor (e.g., *"Cabinet #01 = 176.4 LPM at 14:02:15 UTC"*).
- The verdict column records the mathematical comparison: **PASS** (within tolerance) or **FAIL** (outside tolerance).

A reader must be able to see the cited limit, the measured value, the timestamp, and the verdict side-by-side on a single page. If an audit team cannot trace the measured number to a real instrument tag, or cannot trace the limit to a frozen document revision, the cell is open. An open cell means the pretest line is **FAIL**.

## Decisions to record

Before signing the pretest section of the flash report, verify that the following items are fully documented:

- The cited specification document title, revision mark, and issue date for all hydraulic limits.
- The measured volumetric flow rate for each individual cabinet in the parallel cluster.
- The verified coolant supply temperature and the calculated data hall dew point margin.
- The measured manifold differential pressure ΔP across clean, deburred taps.
- The companion air intake temperature and velocity (or the signed N/A scope reduction).
- The final pass/fail determination for the pretest gate, initialed by the Sheet Owner and the Operator.


# 4. Scene functions

Once the pretest gate achieves PASS, the flash report executes the active operational scenes. A scene is not an informal walk-through, an un-timed equipment demonstration, or a casual turning of a control knob until a crowd is satisfied.

A scene is a formal, time-bounded functional performance test with an explicit start time, a mandatory dwell hold, a defined physical disturbance, and a quantitative pass/fail criterion. Each scene tests a distinct operational capability of the liquid load bank and its associated facility CDU cooling plant.

Standard liquid load-bank verification consists of five core scenes:
1. **Stepped Gradients** (Steady-state capacity and thermal linearity);
2. **The Overload Visit** (Design margin and emergency endurance);
3. **The Sudden Step Change** (Dynamic control response and hydraulic stability);
4. **The 2N Single-Feed Loss Drop Test** (Electrical redundancy and telemetry immunity);
5. **Modulating Valve Authority & Stroke Verification** (Hydraulic trim control).

(See Figure 07 for the detailed electromechanical and control oscillogram of the 2N Single-Feed Loss Drop Test).

## Scene 1: Gradients (The Stepped Capacity Run)

The gradient scene verifies that the load bank can sit stably on distinct load plateaus across its entire operating envelope without hunting, element degradation, or excessive fluid bypass.

Standard testing follows four distinct load fractions:
- **Step 1 (25% Rated Duty)**: 30.0 kW active electrical load (24.6 kW liquid, 4.8 kW air companion).
- **Step 2 (50% Rated Duty)**: 60.0 kW active electrical load (49.3 kW liquid, 9.6 kW air companion).
- **Step 3 (75% Rated Duty)**: 90.0 kW active electrical load (74.0 kW liquid, 14.4 kW air companion).
- **Step 4 (100% Full Rated Duty)**: 120.0 kW active electrical load (98.6 kW liquid, 19.2 kW air companion).

### The rules of the dwell clock
At each plateau, the load command must be held constant for a continuous dwell of **at least 15 minutes** (or the specific hold interval declared in the testing contract). 

The 15-minute clock is non-negotiable because physical liquid loops have mass. An industrial immersion load bank containing 150 kg of 316 stainless steel vessel metal, 20 liters of fluid, heavy internal copper busbars, and thick insulated headers has a thermal time constant of τ ≈ 45 seconds. 
- The first 3 to 5 minutes of any load step represent the **thermal transient window**, during which heat is actively absorbed by the cold metal shell before fluid temperature rise stabilizes.
- A heat-balance calculation attempted during this transient window will falsely report that the heaters are deficient.
- The steady-state evaluation window begins only after four time constants (t ≥ 4τ ≈ 3 minutes) have elapsed. The final 10 minutes of the 15-minute dwell represent the true steady-state plateau.

To pass the gradient scene, all four steps must be successfully held, and the observed fluid temperature rise (ΔT = T_out - T_in) must scale linearly with commanded electrical power within ± 2.0% of theoretical values.

## Scene 2: Overload (The Bounded Visit)

The overload scene verifies that the heating elements, internal solid-state relays (SSRs), contactors, wiring harnesses, and pipe gaskets possess adequate safety margin above 100% nameplate capacity.

For a 120kW baseline unit, the overload step commands **110% rated power (132.0 kW)**.
- **The Visit Rule**: The overload scene is strictly defined as an intentional **visit**, typically lasting exactly **5 minutes**. It is not a permanent rating.
- **Why It Stops at Five Minutes**: Immersion heating elements operating at 110% load experience sheath watt densities approaching 15 W/cm². While safe for short commissioning checks under high-velocity coolant flow, prolonged operation at this elevated flux degrades fluid corrosion inhibitors (such as tolyltriazole) and accelerates EPDM gasket thermal hardening.
- **Pass/Fail Criteria**: The overload scene passes if the unit enters 132kW cleanly, sustains the 5-minute hold without tripping overtemperature snap-switches, shows no contactor chatter or terminal block smoke, and cleanly sheds back to rated load or zero on command.
- **The Fraud of Promotion**: If the test crew notices that the unit ran smoothly at 132kW and attempts to market or re-label the machine as a "132kW continuous load bank," reject the claim immediately. A visit that survived is not a continuous rating.

## Scene 3: Step Change (Dynamic Control & Surge Immunity)

The step change scene tests the dynamic agility of the system during violent power swings—simulating a synchronized AI inference batch launch or an emergency GPU cluster throttle.

The scene executes an instantaneous step jump:
1. The load bank is held steady at 25% load (30 kW).
2. An automated supervisory script or manual operator commands an instantaneous step to 100% load (120 kW).
3. The unit is held at 100% for 10 minutes.
4. An instantaneous shed from 100% back to 25% is commanded.

### What is evaluated
- **Electrical Tracking**: Contactors or thyristor power controllers must switch and stabilize the power step in less than 1.5 seconds.
- **Control Loop Settling Time**: The facility CDU's modulating cooling valve (TCV) must adjust coolant flow or secondary supply temperature to stabilize the new heat flux within 120 seconds, exhibiting less than 5.0% overshoot.
- **Hydraulic Water Hammer Suppression**: When large heater stages drop or modulating valves throttle, rapid flow shifts can induce acoustic pressure pulses. Manifold differential pressure sensors must verify that the peak pressure spike does not exceed ΔP_surge ≤ 15.0 kPa. If rapid valve movement causes violent pipe shudder, pipe support banging, or pressure spikes exceeding 50 kPa, the step change scene is an immediate FAIL.

## Scene 4: Single Feed (2N Power Loss Drop Test)

In high-density AI data halls, power distribution to the rack level is configured as 2N (dual-feeder A and B path) or distributed redundant. A liquid load bank standing in for an NVL72 rack must replicate this split-path electrical topology.

### Test Execution
With the load bank cluster operating at 100% rated capacity (120.0 kW per cabinet, with 60.0 kW drawn from Feeder A and 60.0 kW drawn from Feeder B):
1. An operator manually trips the main feeder breaker feeding Feeder A.
2. Contactor control logic for Bank 1 and Bank 2 (powered by Feeder A) must de-energize immediately.
3. Auxiliary contacts must clear within **< 20 milliseconds**, cleanly shedding exactly 50% of the active load (60.0 kW).
4. Feeder B must seamlessly sustain Bank 3 and Bank 4 without tripping its own upstream circuit breakers or suffering inrush transients exceeding 115% of nominal current.
5. **The Control Bus Zero-Dip Requirement**: The 24VDC supervisory power supply bus (feeding the PLC, sensors, and Modbus/MQTT communication gateways) must be diode-OR coupled across both feeds (see Figure 07). Dropping Feeder A must produce **zero voltage brownout dip** (ripple < 50 mV). If losing Feeder A causes the PLC to reboot, drops the network link, or causes sensor readings to freeze, the load bank fails the single-feed test unconditionally.
6. Once Feeder A drop is validated, Feeder A is restored, the unit returns to 100% steady state, and the identical test is repeated by tripping Feeder B. Both feeders must be tested as the failed path.

## Scene 5: Modulating Valve Authority & Stroke Verification

If the load bank includes an integrated modulating trim valve (TCV) used to regulate rack-side differential pressure or flow impedance, the valve's mechanical authority must be verified.

The test compares a 5-minute steady window prior to valve movement against a 5-minute steady window after valve repositioning:
- **Stroke Verification**: The valve actuator must move from 100% open to 50% throttled upon command without mechanical binding, hunting, or motor stalling.
- **Hydraulic Authority**: Throttling the valve to 50% stroke must produce a measurable, repeatable shift in branch differential pressure (ΔP) without choking into a severe cavitation noise regime.
- A report that simply notes "the valve moved" is un-auditable. The report must state the commanded stroke percentage, the measured change in flow (Δ Q_v), and the resulting shift in manifold differential pressure.

## Decisions to record

For every active scene executed during the test campaign, record the following in the flash report:

- The exact chronological start time, stabilization time, and end time for each gradient plateau.
- The pre-declared duration and power level of the overload visit.
- The measured settling time and peak hydraulic pressure spike (ΔP_surge) during the step change jump.
- The contactor clearing time (< 20ms) and confirmed zero-dip continuity of the 24VDC control bus during the Feeder A and Feeder B drop tests.
- The pre/post flow and pressure measurements for the modulating trim valve stroke test.
- The signature of the Recorder and the Operator confirming that all scene transitions were executed in strict accordance with the testing schedule.


# 5. Consistency and multi-cabinet uniformity

A single sensor can report a plausible, attractive number and still be fundamentally disconnected from physical reality. In high-density data halls where multiple parallel load banks simulate an entire AI cluster row, evaluating units in isolation is inadequate.

The flash report requires a rigorous mathematical test of multi-cabinet consistency: do the instruments and machines that claim to be identical twins on the same secondary manifold behave like identical twins under full load?

In this field guide, consistency is not an informal impression or a visual appraisal of parallel graphs. It is defined by a strict mathematical metric: the **Coefficient of Variation (CV)**.

$$\text{CV} = \left( \frac{\sigma}{\mu} \right) \times 100\% = \left[ \frac{\sqrt{\frac{1}{N} \sum_{i=1}^N (x_i - \mu)^2}}{\mu} \right] \times 100\%$$

where N is the number of parallel load-bank cabinets in the cluster, μ is the arithmetic group mean, and σ is the sample standard deviation. 

(See Figure 03 for the multi-cabinet hydraulic distribution schematic, manifold pressure gradients, and the comparative case studies of balanced vs. starved clusters).

## Where the CV metric applies

The flash report calculates CV across four physical dimensions during the steady-state dwell of every load step:

### 1. Electrical active power uniformity (CV ≤ 1.0%)
Across all parallel load-bank cabinets, active electrical power draw must be balanced within a 1.0% envelope. Resistors manufactured from high-grade Nickel-Chromium (NiCr 80/20) alloys have a strict resistance tolerance (± 2.0% cold, expanding to ± 1.0% across balanced 3-phase delta configurations). 
- If four parallel cabinets are commanded to 120kW, and three draw 120.2kW while Cabinet 4 draws only 108.5kW, the electrical CV spikes to 4.8%.
- An electrical CV exceeding 1.0% indicates a loose terminal lug, a blown branch fuse, a burnt SSR, or an uncalibrated current transducer (CT). It fails the electrical consistency line immediately.

### 2. Coolant volumetric flow uniformity (CV ≤ 5.0%)
In a properly balanced secondary cooling distribution network, every parallel IT rack must receive an identical share of the total liquid stream.
- For four 120kW units operating on a common manifold with a total delivery of 706 LPM, the ideal branch flow is 176.5 LPM per unit.
- Liquid flow rates across all active cabinets must satisfy **CV ≤ 5.0%**.
- A flow CV exceeding 5.0% reveals hydraulic maldistribution—typically caused by unequal branch hose lengths, sharp 90° elbow kinks, improperly seated quick-disconnect internal check valves, or unadjusted branch balancing valves.

### 3. Return coolant temperature rise uniformity (CV ≤ 3.0%)
If electrical power is uniform (CV ≤ 1.0%) and liquid flow is uniform (CV ≤ 5.0%), thermodynamics dictates that the return coolant temperature rise (ΔT = T_out - T_in) must also be uniform.
- Across all cabinets, temperature rise must satisfy **CV ≤ 3.0%**.
- If Cabinet 1 through 3 exhibit ΔT = 10.0 K while Cabinet 4 exhibits ΔT = 14.5 K, Cabinet 4 is experiencing localized heat concentration (frequently driven by low flow). Conversely, if Cabinet 4 exhibits ΔT = 2.1 K, it is suffering from internal fluid short-circuiting around its heating core.

### 4. Manifold differential pressure uniformity (CV ≤ 5.0%)
Differential pressure measured across the supply and return ports of each individual cabinet must satisfy **CV ≤ 5.0%**. This verifies that all chassis present identical hydraulic impedance to the facility CDU pumps.

## The hydraulic danger: Direct-return vs. reverse-return manifolds

The consistency chapter exposes the single most common piping defect in temporary liquid load-bank installations: **direct-return manifold starvation**.

As illustrated in Figure 03:
- In a **Direct-Return (First-In, First-Out)** manifold, the first load bank (Rack 1) is closest to both the primary supply feed and the primary return collector. Rack 1 experiences the shortest hydraulic circuit and the highest available differential pressure (ΔP). The farthest unit (Rack 4) sits at the hydraulic dead-end, where supply pressure has decayed due to pipe friction and return back-pressure has accumulated.
- Without individual branch balancing valves, Rack 4 receives significantly degraded flow (e.g., 124.0 LPM vs 192.0 LPM at Rack 1). This results in a disastrous flow CV of **18.25%**!
- In an attempt to mask this failure, inexperienced teams will calculate an "average cluster flow" (168.25 LPM) and declare the test passed. Meanwhile, in Rack 4, fluid velocity has collapsed, sheath temperatures are soaring toward 85°C trip limits, and the CDU pumps are operating in an unstable region.
- In a **Reverse-Return (Tichelmann)** piping loop, the first unit fed is the last unit returned, ensuring that total equivalent pipe length is identical across all four branches. The resulting flow CV easily drops to **0.33%**, guaranteeing true hydraulic fidelity.

The flash report requires the CV of flow to be calculated and printed on the first page. A high CV immediately exposes direct-return starvation before real compute hardware is deployed.

## The evaluation window rules

The consistency analysis must be performed over a continuous **five-minute evaluation window** taken during the final, steady portion of a 15-minute load dwell.
- The window must be sampled at **1 Hz** (one live reading per second per channel).
- The window must be strictly confined to steady state. It must never span across a load step transition or an operator valve adjustment. Including a power step within the window artificially inflates variance, causing an honest set of cabinets to fail the calculation.
- If a load step was held for only 3 minutes, you do not have sufficient steady-state data to compute CV. In that case, you must mark the consistency line **NOT RUN** or repeat the step with a proper dwell. You may not stretch the window backward into the transient warm-up to collect enough points.

## What CV cannot say: The zero-variance fraud

A low CV proves that the cluster agrees with itself. It does not prove that the cluster is correct.

Consider two dangerous failure modes that produce deceptively low CVs:
1. **Uniformly Out of Spec**: All four cabinets receive an identical flow of 130.0 LPM against a specified floor of 170.0 LPM. The standard deviation is zero, and the calculated flow CV is a spotless 0.00%. Yet the cluster is uniformly starved! This passes the consistency line, but it fails the Pretest line unconditionally. Uniform failure is still failure.
2. **The Stale / Frozen Data Fraud**: If an edge gateway communication thread crashes, or if a Modbus poller repeatedly logs cached values without reading live registers, the recorded values across all four cabinets will remain mathematically frozen. A dead group will report a standard deviation of σ = 0.000 and a calculated CV of **0.00%**!

A CV of exactly 0.00% is not a mark of engineering perfection; in a turbulent fluid loop, it is physical proof of telemetry fraud. Real turbulent convection always generates microscopic thermal and pressure fluctuations. 

Therefore, before any calculated CV can be accepted in the flash report:
- The supervisory system must verify that **sample variance σ² > 0** across all channels.
- The 16-bit Quality Bitmask must confirm that no channel has its "STALE / FROZEN" bit asserted.

If the variance is zero or the quality bit is faulted, the calculated CV is paint. Fail the line.

## Decisions to record

In the consistency section of the flash report, record the following facts:

- The pre-declared CV threshold limits for electrical power (≤ 1.0%), liquid flow (≤ 5.0%), temperature rise (≤ 3.0%), and differential pressure (≤ 5.0%).
- The exact 5-minute time window (start and end timestamps to the second) used for the steady-state calculation.
- The arithmetic mean (μ), sample standard deviation (σ), and calculated CV for each parameter across all parallel cabinets.
- The certified non-zero variance check (σ² > 0) confirming that live turbulent jitter was present on every channel.
- The signed pass/fail verdict for multi-cabinet consistency, initialed by the Stranger.


# 6. How a point is made

A plotted point on a flash-report chart is not a raw measurement, and a raw measurement is not an optional disposable scratch file.

In mission-critical commissioning, an engineering chart that cannot produce its underlying raw time-series data is not an analysis; it is a graphic illustration. If you discard the raw data and keep only minute-averages, you lose the ability to detect contactor arcing, flow meter cavitation slugs, and communication timeouts. Conversely, if you present an auditor with an un-aggregated scatter of sixty thousand points per hour, the eye will drown in visual noise and miss long-term thermodynamic drift.

A professional flash report retains both: it acquires high-frequency raw samples, archives them in an immutable time-series store, and constructs each plotted point through strict, auditable statistical aggregation.

(See Figure 04 for the metrological comparison between live physical turbulent jitter and buffer-freeze flatline fraud).

## Raw acquisition at 1 Hz, then the sixty-second mean

The standard acquisition rate for all primary channels in this field guide is **1 Hz (one sample per second per channel)**.
- **Why 1 Hz Is Required**: A sampling rate of 1 Hz captures critical sub-minute physical phenomena: the rapid inrush current of heater staging, the 14-millisecond contactor clearing time during a single-feed drop test, and the dynamic pressure spikes of rapid valve movement. Sampling once every 10 or 30 seconds acts as a severe low-pass filter that blinds the observer to dangerous transients.
- **The Sixty-Second Mean**: Each formal point plotted on a flash-report time-series chart represents the **arithmetic mean of sixty consecutive raw 1-second samples**:
 $$\mu_t = \frac{1}{60} \sum_{i=1}^{60} x_i$$
 where each point is timestamped with the exact start-time of that sixty-second interval (e.g., `14:22:00.000Z`).
- **The Missing Sample Rule**: If an edge gateway or Modbus poller drops communication during that minute, resulting in only 52 valid samples instead of 60, the minute is marked **PARTIAL** in the data block. Under no circumstances may the reporting script copy the neighboring minute's average or fabricate linear interpolation to "keep the curve looking smooth." A smooth curve that covers a communication dropout is an audit falsehood.

## The variance gate: Catching stale data fraud

Sixty raw samples that are identical copies of a single cached float value are not a 60-sample average. They are one value wearing sixty timestamps.

In a turbulent fluid stream carrying 176.5 LPM of fluid through pipe diameters of 1.5 inches (DN39), the Reynolds number easily exceeds Re ≈ 28,000. Fluid flow in this regime is intensely turbulent. Convective micro-eddies, boundary-layer vortex shedding, and pump impeller blade-pass frequencies constantly produce microscopic thermal and pressure fluctuations.
- A genuine physical immersion RTD in live fluid will always exhibit a non-zero sample variance:
 $$\sigma_t^2 = \frac{1}{60} \sum_{i=1}^{60} (x_i - \mu_t)^2 > 0$$
 Typically, a healthy 1-second temperature stream exhibits a standard deviation of σ ≈ 0.05 K to 0.20 K (σ² ≈ 0.0025 to 0.0400 K²).
- **The Flatline Signature of Fraud**: If an edge gateway communication thread locks up, or if an ADC driver hangs and continuously echoes the last known register from RAM, the recorded values become mathematically flat. Every sample over a five-minute stretch reads exactly 45.000000°C down to the least significant bit. The calculated sample variance collapses to:
 $$\sigma_t^2 \equiv 0.000000\,\text{K}^2$$

In a live liquid cooling loop, a variance of exactly zero is physically impossible. It is the definitive smoking gun of **stale data fraud**.

The flash report's automated data ingestion engine must run a continuous variance check:
$$\text{If } \sigma_t^2 \le 1.0 \times 10^{-4}\,\text{K}^2 \text{ for more than 3 consecutive minutes, flag CHANNEL\_FROZEN\_STALE.}$$
When this flag is asserted, the reporting engine must reject the minute block, sound an audible alert, and refuse to calculate a compliant mean. Stale repeats fail the step plateau automatically.

## The four-summary requirement on every step

Whenever a step data block is compiled for the flash report, reporting a simple arithmetic mean is strictly prohibited. A mean alone can conceal a dangerous localized spike.

Every step data block must report **four mandatory statistical quantities** for each active channel across the steady-state dwell:
1. **Minimum Value ($\min$)**: The lowest raw 1-second reading recorded during the dwell.
2. **Maximum Value ($\max$)**: The highest raw 1-second reading recorded during the dwell.
3. **Arithmetic Mean (μ)**: The central baseline value across all valid samples.
4. **Sample Standard Deviation (σ)**: The measure of physical turbulence and control stability.

### Why the Maximum is Essential
Consider a 120kW load step with a mean coolant temperature of 45.0°C. If a pump briefly cavitated or an air bubble passed through the heater vessel for 10 seconds, the localized fluid temperature may have spiked to 68.5°C before recovering. 
- In a 15-minute average of 900 points, that 10-second spike of 68.5°C will raise the mean by a negligible 0.26 K—an offset that any auditor would dismiss as rounding error.
- But reporting the maximum instantly exposes the peak: $\max = 68.5°C$. This immediately alerts the engineering team that EPDM hose temperature limits were breached and that cavitation occurred.

A report that omits the maximum is an attempt to bury operational extremes inside a comfortable average. Require all four numbers on every line.

## Mathematical rules for branch and total sums

When aggregating flow and power across multiple parallel cabinets, arithmetic rules must respect the physical piping and electrical topology:

- **Total Volumetric Flow**: Must be computed strictly from the sum of the individual branch vortex flow meters:
 $$Q_{\text{total}} = \sum_{k=1}^N Q_{\text{branch},k}$$
 Do not sum a main header ultrasonic flow meter and the individual branch meters together and claim that the loop moved twice the fluid! 
- **Missing Meter Rule**: If Cabinet 3's flow meter fails or drops communication, Q_total is incomplete. The flash report must report: *"Total flow: INCOMPLETE (Cabinet 3 meter offline)."* Under no circumstances may an automated script estimate Cabinet 3's flow by averaging Cabinets 1, 2, and 4! An estimated number in a sum is an engineered fabrication.
- **Total Electrical Power**: Must be computed from the discrete phase powers of each branch feeder:
 $$P_{\text{total}} = \sum_{k=1}^N \left( P_{A,k} + P_{B,k} \right)$$
 Do not report an upstream substation transformer power reading and call it the load-bank load. Upstream transformers include cable losses, lighting, and auxiliary chiller pump power that do not touch the liquid load bank.

## Annotating dynamic step transitions

For the Sudden Step Change and Overload scenes, the time-series chart must explicitly annotate the exact second when the command was issued:
- A vertical red dashed marker must indicate t_command.
- A second vertical blue marker must indicate t_settled, when fluid temperature and power achieved their new steady plateau.
- The chart label must state the observed rise time (Δt_rise) and the peak transient pressure pulse (ΔP_surge).

An un-annotated spike on a chart will be interpreted as a catastrophic fault by a skeptic and as a brilliant operational feature by an optimist. Only precise, labeled timestamps prevent subjective debate.

## Decisions to record

In the metrology section of the flash report, record the following facts:

- The verified 1 Hz sampling frequency of the edge data logger and the location of the immutable raw CSV archive.
- The calculated sample variance (σ²) for every channel across the steady dwell, certifying that σ² > 0.
- The Four-Summary table (Min, Max, Mean, StdDev) for every monitored parameter on each load step.
- The certified list of branch flow meters included in the total flow summation.
- The exact annotated timestamps for all step command transitions and breaker trips.


# 7. The data block and heat balance reconciliation

Every load plateau that the flash report claims as evidence must possess an identical, standardized data block. 

A data block is not an unstructured collection of numbers thrown onto a page. It is a systematic thermodynamic balance sheet containing five mandatory sections:
1. **Setpoints & Commands** (The pre-declared intention);
2. **Initial State Baseline** (The reference condition immediately prior to the step);
3. **Electrical Distribution Data** (The verified energy delivered to the elements);
4. **Hydraulic Enthalpy Data** (The heat absorbed into the liquid stream);
5. **Companion Air & Thermal Closure** (The total first-principles energy balance reconciliation).

Missing any one of these five headings is not an economical formatting choice; it is an omission of a fundamental engineering claim. (See Figure 06 for the complete energy decomposition Sankey, the four-step reconciliation table, and the four diagnostic failure modes).

## Heading 1: Setpoints and commands

The first section of the data block records the commands issued to the machine *before* the dwell began:
- Commanded electrical load: e.g., 120.0 kW (or the specific percentage of rated duty: 25%, 50%, 75%, 100%, 110%).
- Commanded power split across dual feeders: e.g., Feeder A = 60.0 kW, Feeder B = 60.0 kW.
- Commanded modulating valve position: e.g., TCV = 100% full open (or locked balancing valve position = 4.2 turns).
- Commanded companion air blower speed: e.g., 100% (or fixed 1200 CFM).

A command value must be recorded from the supervisory control log before the clock starts. Reconstructing the "command" by averaging the observed power during the dwell is a circular calculation: it turns a measured result into an artificial setpoint.

## Heading 2: Initial state baseline

The second section documents the condition of the system during the minute immediately preceding the step transition:
- Starting coolant supply temperature (T_in,init) and return temperature (T_out,init).
- Starting volumetric flow rate (Q_v,init) and manifold differential pressure (ΔP_init).
- Timestamp of the baseline minute (start and end to the second).

This baseline is essential for separating the steady-state thermal gain from any background temperature drift occurring within the facility primary cooling loop.

## Heading 3: Electrical distribution data

The third section details the active electrical power drawn by the heating elements. In an industrial 415V 3-phase dual-feeder configuration, reporting a single aggregated "kilowatts" figure is inadequate. The report must provide:
- **Feeder A Metrics**: Line-to-line voltages (V_AB, V_BC, V_CA), line currents (I_A, I_B, I_C), total Feeder A active power (P_A), and power factor (PF_A).
- **Feeder B Metrics**: Line-to-line voltages, line currents, total Feeder B active power (P_B), and power factor (PF_B).
- **Total Active Power**: 
 $$P_{\text{elec}} = P_A + P_B$$
- **Phase Balance Verification**: Current unbalance across phases must satisfy I_unbalance ≤ 2.0%. A severely unbalanced current indicates that one resistor bank has failed open or that an internal contactor pole is pitted and failing to seat.

## Heading 4: Hydraulic enthalpy data

The fourth section captures the cooling fluid's thermodynamic absorption of heat. This requires high-accuracy metrology across six physical parameters:
1. **Supply Coolant Temperature (T_in)**: Measured via 4-wire Pt100 RTD immersed in the core flow ($1/3 \sim 1/2 D$).
2. **Return Coolant Temperature (T_out)**: Measured downstream of the heating vessel after full fluid mixing.
3. **Net Temperature Rise (ΔT)**: 
 $$\Delta T = T_{\text{out}} - T_{\text{in}}$$
4. **Volumetric Flow Rate (Q_v)**: Measured via calibrated vortex shedding flow meter (reported in liters per minute, LPM).
5. **Fluid Thermophysical Properties**: Density (ρ) and specific heat capacity (C_p) must be evaluated at the mean bulk fluid temperature:
 $$\bar{T} = \frac{T_{\text{in}} + T_{\text{out}}}{2}$$
 For a standard 25% Propylene Glycol / 75% Water solution (PG25) at $\bar{T} = 40.0°C$, the standard values are:
 $$\rho = 1025.0\,\text{kg/m}^3, \quad C_p = 3.980\,\text{kJ/(kg}\cdot\text{K)}$$
6. **Inferred Liquid Thermal Heat (Q_liquid)**: 
 Derived directly from first-principles thermodynamics:
 $$Q_{\text{liquid}} = \dot{m} \cdot C_p \cdot \Delta T = \left( Q_v \times \frac{\rho}{60{,}000} \right) \cdot C_p \cdot (T_{\text{out}} - T_{\text{in}})$$

For the baseline educational reference model operating at rated full duty (Q_v = 176.5 LPM, ΔT = 10.04 K):
$$\dot{m} = 176.5 \times \frac{1025.0}{60{,}000} = 3.015\,\text{kg/s}$$
$$Q_{\text{liquid}} = 3.015\,\text{kg/s} \times 3.980\,\text{kJ/(kg}\cdot\text{K)} \times 10.04\,\text{K} = 120.48\,\text{kW} \times \text{split ratio} \approx 98.6\,\text{kW}$$

## Heading 5: Companion air & first-principles thermal closure

In NVL72-class AI architectures, approximately 16% to 20% of total rack heat is rejected directly into the data hall air by optical transceivers, motherboard power conversion stages, and memory modules. The companion air section must capture this sensible heat:
- Intake dry-bulb air temperature (T_air,in) and discharge air temperature (T_air,out).
- Air mass flow rate (ṁ_air) derived from blower RPM and calibrated nozzle differential pressure.
- Inferred air sensible heat:
 $$Q_{\text{air}} = \dot{m}_{\text{air}} \cdot C_{p,\text{air}} \cdot (T_{\text{air,out}} - T_{\text{air,in}})$$

### The First-Principles Energy Balance Equation
By the first law of thermodynamics, the active electrical energy delivered to the load bank must equal the total heat leaving the cabinet boundaries plus any uninsulated parasitic losses:
$$P_{\text{elec}} = Q_{\text{liquid}} + Q_{\text{air}} + Q_{\text{chassis\_loss}}$$

Where uninsulated chassis skin loss ($Q_chassis\_loss$) through natural convection and radiation is typically bounded at ≤ 2.0% of total power when proper internal ceramic blanket insulation is installed.

### The Enthalpy Closure Ratio Gate
The flash report evaluates the **Enthalpy Closure Ratio**:
$$\text{Closure Ratio} = \left[ 1.0 - \frac{|P_{\text{elec}} - (Q_{\text{liquid}} + Q_{\text{air}})|}{P_{\text{elec}}} \right] \times 100\%$$

To achieve a **PASS** on the step data block, the energy closure must satisfy:
$$\text{Closure Ratio} \ge 97.0\% \quad \left( \text{or an energy discrepancy } \le 3.0\% \right)$$

If P_elec = 120.0 kW, but the sum of liquid enthalpy (Q_liquid = 75.0 kW) and air heat (Q_air = 19.0 kW) is only 94.0 kW, the closure ratio is only 78.3%! There is 26.0 kW of missing energy!
- This discrepancy cannot be glossed over by adding an undocumented "efficiency factor" or "loss correction."
- An enthalpy closure failure of 26 kW indicates a severe physical defect: fluid is short-circuiting around the heating vessel via an open bypass valve, the flow meter calibration factor (K-factor) is incorrect, or the RTDs are seated in stagnant dead-leg stubs.
- An energy closure failure fails the step plateau unconditionally.

## Reporting hierarchy: One cabinet, then the cluster summary

When reporting multi-cabinet test clusters:
1. Each individual cabinet must have its own discrete data block printed first, with all five headings and four-summary statistics ($\min, \max, μ, σ$).
2. Beneath the individual cabinet blocks, the **Cluster Summary Block** is compiled, reporting total electrical power, total liquid enthalpy absorption, total air heat, and the cluster-wide Enthalpy Closure Ratio.

A cluster summary that looks calm and balanced cannot outvote an individual cabinet that failed its energy closure. If Cabinet 4 has 20kW of missing heat while Cabinets 1, 2, and 3 are balanced, Cabinet 4 is a failure. You do not average Cabinet 4 into the cluster to manufacture a synthetic pass.

## Decisions to record

For every step data block compiled in the flash report, record:

- The commanded setpoints for active power, dual-feeder split, and trim valve position.
- The pre-step initial baseline fluid and air temperatures.
- The 3-phase electrical voltages, currents, power factors, and total active power P_elec.
- The measured fluid temperatures, volumetric flow, fluid density, specific heat, and inferred liquid enthalpy Q_liquid.
- The measured air temperatures, airflow rate, and inferred companion air heat Q_air.
- The calculated First-Principles Enthalpy Closure Ratio, certifying that closure ≥ 97.0%.
- The initials of the Recorder and the Stranger confirming the energy balance.


# 8. External gear and facility boundaries

A liquid load bank is not an island, and a commissioning test does not occur in an abstract vacuum. The load bank connects directly to live facility infrastructure: to a Coolant Distribution Unit (CDU), to an uninterruptible power supply (UPS) or automatic transfer switch (ATS), and to computer room air handlers (CRAH).

A frequent failure mode in commissioning reporting is the confusion of boundaries:
- When a facility CDU circulating pump trips on an internal inverter fault, an inexperienced team may blame the load bank for "failing to maintain flow."
- Conversely, when a load bank's high-temperature safety switch trips due to poorly submerged heating elements, a vendor may attempt to blame the facility CDU for "running too warm."

The flash report must draw an uncompromising physical and operational boundary between the load bank (the machine under test) and the external facility gear (the host environment). A failure of external facility gear is an operational event; it is not automatically a failure of the load bank. But it must be documented with absolute precision so that the true cause of an interrupted dwell is transparent to any future auditor.

## The four external gear lines

The flash report includes an External Gear section with four explicit lines, evaluated before, during, and after every test run:

### Line 1: Coolant Distribution Unit (CDU)
The CDU is responsible for circulating secondary coolant through the load bank and transferring heat to the primary facility chilled water loop via its internal brazed plate or shell-and-tube heat exchanger.

The flash report monitors four CDU interface metrics:
- **Secondary Loop Supply Temperature (T_CDU,sup)**: The temperature of fluid exiting the CDU heat exchanger before entering the load-bank supply manifold. The report verifies that the CDU maintains its declared supply setpoint (e.g., 35.0°C ± 1.0 K). If the primary facility water warms up, causing T_CDU,sup to drift upward to 42.0°C, that drift is recorded as a **CDU boundary condition excursion**, not as a load-bank heating error.
- **Secondary Delivery Pressure & Pump Curve**: The available static pressure delivered by the CDU pumps at rated cluster flow. If the CDU pump speed hunts or cavitates due to poor suction pressure, the resulting flow fluctuations are logged against the CDU line.
- **CDU Approach Temperature**: The temperature difference between the secondary return fluid and the primary facility water (Approach = T_sec,ret - T_pri,sup). An increasing approach temperature over time indicates fouling in the CDU heat exchanger plates, not element degradation in the load bank.

### Line 2: Uninterruptible Power Supply (UPS) & Automatic Transfer Switch (ATS)
The electrical power feeding the load bank originates from facility distribution switchboards, often backed by static UPS modules or diesel generator ATS gear.

The flash report monitors:
- **Voltage Stability & Harmonic Distortion**: Line voltage sag during full-load staging. If the facility transformer sags from 415V down to 380V under full 480kW load, the active power of resistive elements will drop by nearly 16% ($P \propto V²$). The report must document that the load drop was driven by facility utility sag, not by early contactor shedding.
- **ATS Transfer Immunity**: If an integrated system test (IST) initiates an upstream power transfer, the duration of the open-transition interruption must be timed. If the interruption exceeds the load bank's 24VDC control buffer hold-up time (typically 40ms), the unit will de-energize safely, which must be attributed to the facility transfer transient.

### Line 3: Power Distribution Units (PDUs) and Busways
The physical power path from the electrical panelboard through busway tap-off boxes and drop cables to the load-bank terminals:
- **Terminal Temperature Rise (ΔT_terminal)**: Infrared thermography or calibrated thermocouple monitoring of cable lugs and contactor terminals. Terminal temperature must not exceed 70°C (or the specific rating of the 90°C RHW-2 conductor).
- **Busway Voltage Drop**: Voltage drop across the temporary feeder cables must be bounded at ≤ 2.0%.

### Line 4: Computer Room Air Handlers (CRAH / CRAC / Fan Wall)
The facility air-handling units responsible for absorbing the 16% to 20% companion air sensible heat dissipated by the load-bank blowers:
- **Intake/Discharge Air Differential**: Verifying that the data hall's hot-aisle containment (HAC) maintains proper negative pressure relative to the cold aisle, preventing thermal recirculation into adjacent server rows.
- **CRAH Chilled Water Valve Response**: Confirming that CRAH cooling coils modulate open smoothly in response to the companion air load without overflowing condensate drain pans.

## How to write an honest boundary sentence

When an anomaly or interruption occurs during a test run, the Recorder must write an honest boundary sentence. 

An honest boundary sentence adheres to three strict grammatical rules:
1. **It names the exact physical parameter that breached a threshold.**
2. **It names the specific side of the boundary where the breach occurred.**
3. **It states the consequence on the test scene without assigning speculative blame.**

### Example of an Honest Boundary Sentence
> *"At 15:42:18 UTC, during Step 4 (120kW dwell), secondary coolant supply temperature from the facility CDU rose to 39.8°C (exceeding the cited pretest boundary of 36.5°C). The load bank maintained rated electrical load (120.1kW) and normal flow (176.4 LPM), but return temperature reached 49.9°C, triggering an automated overtemperature supervisory alarm. The dwell was halted at Minute 11 by operator command. Verdict for Step 4: INVALID due to facility CDU supply temperature excursion; load bank electrical and hydraulic tracking remained fully compliant."*

### Example of a Dishonest Sentence
> *"The test had some issues with the building water, but the load bank basically passed."*

The dishonest sentence provides zero data, cites no timestamp, names no temperature, and attempts to claim an illegitimate pass. An auditor will reject it instantly. The honest sentence provides exact numbers, identifies the CDU boundary excursion, records the aborted dwell, and preserves the technical integrity of the load-bank hardware for the re-test.

## External gear pass/fail status

On the flash report summary sheet, each of the four external gear lines is given an independent status:
- **NORMAL**: Operated within the cited design envelope for the entire run.
- **EXCURSION**: Breached an operating envelope, with exact timestamps and affected parameters documented.
- **NOT APPLICABLE (N/A)**: Gear was excluded from the testing boundary by pre-declared agreement.

A facility CDU excursion does not ruin the reputation of a well-engineered load bank, nor does a clean load bank excuse a failing facility plant. The report records both, in daylight, separated by the physical manifold boundary.

## Decisions to record

In the external gear section of the flash report, record:

- The serial number, model, and firmware version of the facility CDU and its primary loop chilled water temperature.
- The upstream transformer / UPS bus voltage and phase balance during the maximum load step.
- The maximum observed cable lug terminal temperature during the full-load dwell.
- The operational status of the facility CRAH units and hot-aisle containment integrity.
- Any honest boundary sentences explaining test pauses or aborted dwells, signed by both the Operator and the Stranger.


# 9. Automated fields and human judgment

Modern commissioning platforms use automated data ingestion scripts, Python pipelines, and cloud dashboards to ingest thousands of Modbus and MQTT telemetry points per second. Automation is efficient, consistent, and immune to manual calculation fatigue.

However, an automated script that calculates numbers must never be confused with an automated script that grants technical acceptance.

The flash report establishes an unyielding boundary between two distinct categories of cells:
1. **Script-Filled Cells**: Arithmetic and statistical quantities computed deterministically from raw telemetry.
2. **Human-Filled Cells**: Qualitative verdicts, contractual compliance determinations, and legal signatures of technical acceptance.

An algorithm does not hold a professional engineering license, cannot appear in court, and cannot take financial or operational responsibility for a data hall fire. An algorithm calculates numbers; a human writes the verdict.

## What a script is allowed to fill

Automated scripts, ingestion pipelines, and database aggregation queries are ideally suited for deterministic mathematics. A script may—and should—fill the following fields without human intervention:

- **Timestamps and Sample Counts**: Exact start and end times to the millisecond, duration of dwells in seconds, and the total count of valid raw 1-second samples received per channel.
- **Statistical Summaries**: Arithmetic mean (μ), minimum ($\min$), maximum ($\max$), sample standard deviation (σ), and variance (σ²) across defined time windows.
- **Derived Physical Calculations**: Mass flow rate (ṁ), bulk fluid density (ρ), specific heat capacity (C_p), liquid enthalpy absorption (Q_liquid), and companion air sensible heat (Q_air).
- **Multi-Cabinet Metrics**: Group means, group standard deviations, and the Coefficient of Variation (CV) across parallel cabinets.
- **Enthalpy Closure Ratios**: The exact percentage closure between active electrical power and total thermodynamic heat dissipation (P_elec vs Q_liquid + Q_air).
- **Algorithmic Anomaly Flags**: Automated alerts indicating zero-variance flatlines (σ² ≤ 1.0 × 10^{-4}), missing communication gaps, out-of-range sensor readings, and changepoint candidate trigger times from Focus, FLOC, or CPOP.

A computer executes arithmetic faster and with far greater precision than a human with a pocket calculator. Let the script do the arithmetic.

## What a script is strictly forbidden from writing

Under no circumstances may an automated script, a dashboard macro, or an AI model generate the words:
- **PASS**
- **FAIL**
- **NOT RUN**
- **WAIVED**

An automated script that evaluates a row, observes that the calculated temperature is 45.1°C against an upper limit of 46.0°C, and automatically stamps the word "PASS" onto the PDF has exceeded its authority.

### Why Automated "Pass" is Dangerous
Consider what an algorithm cannot know:
- The algorithm does not know that the RTD reporting 45.1°C was accidentally installed in a cold dead-leg stub rather than the active stream.
- The algorithm does not know that a temporary bypass hose was kinked behind the cabinet, or that an unrecorded manual valve adjustment was performed during the hold.
- The algorithm does not know that the client issued an emergency verbal bulletin that morning shifting the test envelope from 46.0°C down to 44.0°C.

An automated script that writes "PASS" lulls the engineering team into a false sense of security. Operators stop looking at physical pipes, stop listening for pump cavitation, and stop verifying instrument calibration tags, assuming that "the software is handling compliance."

In this field guide, the verdict cells on the flash report template are born blank. They can only be filled by a human hand using an ink pen or an authenticated digital cryptographic signature.

## The crime of the human override

The inverse failure mode is equally toxic: a human being who observes a failed mathematical cell calculated by the script and overwrites the verdict with an unauthorized "PASS."

If the script correctly calculates that flow CV is **7.2%** against a maximum threshold of **5.0%**, an engineer may not write "PASS" beside that cell and add a verbal excuse: *"Flow was a little uneven, but overall cooling looked fine."*

That action is not an engineering interpretation. It is an unrecorded, illegitimate waiver. 

If a calculated cell fails:
- The human verdict for that line must be **FAIL**.
- If the project team genuinely believes that the failure does not compromise the broader commissioning objective, the Sheet Owner must invoke the formal **Waiver Protocol**:
 1. Revise the design basis specification to explicitly widen the tolerance from 5.0% to 7.5%;
 2. Assign a new document revision mark (e.g., Rev 2.5);
 3. Formally re-classify the claim as a known limitation;
 4. Obtain written, signed authorization from the facility owner.

A waiver executed in broad daylight with an updated document revision is an auditable engineering decision. A human "PASS" written over a failed cell in the dark of a spreadsheet is a falsification of the test record.

## Designing the two-column interface

To enforce this discipline in software and print, every flash report template must implement a strict **Two-Column Interface**:

| Left Column: Automated Data Block (Script Owned) | Right Column: Evaluation & Verdict (Human Owned) |
| :--- | :--- |
| • Commanded Power: 120.0 kW | • Cited Limit Citation: DOC-SPEC Rev 2.4, Table 2 |
| • Measured Power: 120.2 kW | • Verified Feeder Balance: Phase unbalance < 1.0% |
| • Inferred Liquid Heat: 98.6 kW | • Thermodynamic Plausibility: Confirmed |
| • Enthalpy Closure: 98.0% | • Hardware Physical Inspection: No leaks / Normal sound |
| • Calculated Flow CV: 2.95% (σ = 5.21 LPM) | • Consistency Verification: Passed within 5.0% threshold |
| • Quality Mask: 0x0007 (Valid, σ² > 0) | • **Human Verdict**: **PASS** [Initials: E.V., Lead CxA] |

The left column contains un-retouched numbers generated by code. The right column contains human scrutiny, manual verification checks, and the final responsible signature.

## Decisions to record

In the governance section of the flash report, record:

- The software version, script checksum (SHA-256 hash), and repository branch of the automated data aggregation pipeline.
- The certified statement that all verdict cells (Pass/Fail/Not Run) were manually reviewed and entered by the designated human authorities.
- Any formal waivers invoked during the campaign, referencing the authorized document revision and the owner's signature.


# 10. The formal report package

A flash report is designed for rapid, on-site technical triage. It delivers the immediate five-line verdict within two hours of a load-bank test shutdown so that facility managers, commissioning directors, and contractor leads can determine whether to advance to the next commissioning phase or hold the site for corrective repairs.

However, the flash report does not vanish when the shift ends. It forms the permanent core of the **Formal Commissioning Verification Handover Package**—the legal and technical dossier that survives into the operational life of the data center and is archived for insurance underwriters, hyperscale tenant audits, and annual facility recertifications.

A formal package that is eighty pages of marketing brochures and un-indexed raw data dumps will be discarded by an auditor. Conversely, a package that is too brief to defend its numbers will be rejected. 

This chapter defines exactly what to keep in the formal handover package, what to ruthlessly discard, and how to structure the archive so that a stranger can verify its integrity ten years after the test crew has demobilized.

## What must be kept: The seven essential artifacts

The formal handover package must contain seven discrete, numbered artifacts. If any one of these seven is missing, the package is incomplete:

### Artifact 1: The One-Page Executive Flash Report
The definitive summary sheet defined in Chapter 1 and illustrated in Figure 01:
- The run metadata (Run ID, facility location, date, cited specification revision).
- The five scene passes table (Pretest, Gradient, Overload, Step Change, Single-Feed Fault) with measured values, dwell durations, and explicit PASS/FAIL/NOT RUN verdicts.
- The overall test verdict clause.
- The wet ink or cryptographic signatures of all four designated roles (Sheet Owner, Operator, Recorder, Stranger).

### Artifact 2: The Preparation and Baseline Certificate
Documentation proving that the test cluster was fit to test before heat was commanded:
- The four preparation gates verified and signed.
- The cold 10-minute stabilization log, including the one-minute baseline averages.
- The cold hydraulic impedance calibration record, noting locked balancing valve positions and baseline differential pressure (ΔP).

### Artifact 3: The Multi-Cabinet Consistency Sheet
The statistical evaluation of cluster balance across all parallel load banks:
- The calculated Coefficient of Variation (CV) for electrical active power (CV ≤ 1.0%), coolant flow (CV ≤ 5.0%), temperature rise (CV ≤ 3.0%), and manifold pressure (CV ≤ 5.0%).
- The certified non-zero variance check (σ² > 0) proving that live turbulent flow was present and that no channel was echoing cached/frozen data.

### Artifact 4: The Step Data Blocks and Enthalpy Closure Tables
The complete thermodynamic balance sheet for every load step (25%, 50%, 75%, 100%, 110%):
- The Four-Summary statistics (Minimum, Maximum, Arithmetic Mean, Standard Deviation) for all electrical, liquid, and air channels.
- The first-principles thermodynamic energy balance: active electrical power (P_elec) compared against liquid enthalpy (Q_liquid = ṁ C_p ΔT) and companion air sensible heat (Q_air).
- The certified Enthalpy Closure Ratio (≥ 97.0%).

### Artifact 5: The Time-Series Oscillograms and Charts
High-resolution, vector-quality charts generated from the immutable raw data:
- Overlaid power and temperature waveforms for all parallel units, plotted on scales that honestly reveal individual cabinet divergence.
- Annotated dynamic step-change response plots, detailing settling times and peak hydraulic pressure pulses.
- The 2N single-feed loss transient oscillogram, capturing contactor clearing (< 20ms) and zero-dip control bus stability.

### Artifact 6: The Algorithmic Changepoint and Anomaly Audit Log
The complete log of automated algorithmic scrutiny:
- Online Focus and FLOC candidate trigger times compared chronologically against the Operator's command log.
- Offline CPOP piecewise-linear slope segments across steady dwell boxes.
- Human classification tags initialed for every candidate: *Expected Step*, *Inspect / Split Hold*, or *No Impact*.

### Artifact 7: The Cryptographically Signed Raw CSV Data Archive
The full, un-retouched 1-second raw telemetry file exported directly from the edge gateway:
- Every active sensor channel recorded once per second with ISO-8601 UTC timestamps.
- Accompanied by a formal SHA-256 cryptographic checksum file (e.g., `LB_TEST_2026_H01_RAW.csv.sha256`) generated immediately upon file closing, guaranteeing that raw numbers have not been modified, filtered, or retroactively edited.

## What must be ruthlessly discarded

A formal handover package is an engineering audit record, not an advertising portfolio. The following items must be strictly excluded:

- **Uncalibrated Smartphone Photographs**: Do not include dozens of blurry smartphone photos of illuminated panel lamps, operator faces, or cable bundles. A photograph of a green LED is a souvenir; it is not evidence of electrical continuity or fluid enthalpy. (High-resolution thermal imaging captures with calibrated temperature scales are permitted only as supporting documentation for terminal lug checks).
- **Vendor Marketing Brochures & 3D Renderings**: Do not pad the document with glossy sales brochures, computer-generated concept art, or corporate profile slides. The audit package belongs to the physical machine on the floor, not the sales brochure.
- **Unredacted Confidential Client Data**: Do not include customer tenant identities, proprietary AI model names, unredacted security access codes, or internal corporate IP addresses. The report verifies thermodynamic and electrical performance; it does not map private data networks.
- **Un-Indexed Multi-Gigabyte Raw Log Dumps**: Do not paste millions of unformatted raw JSON log lines or raw terminal outputs into the PDF appendix. Store the raw CSV archive in a separate secure digital repository, cite its SHA-256 hash, and keep the formal report PDF clean, readable, and focused.

## The structure of the archive folder

Organize the final digital handover package into a clean, standardized folder directory structure:

```
├── 01_Executive_Flash_Report.pdf # The signed 1-page summary
├── 02_Preparation_and_Baseline.pdf # Cold gates & hydraulic calibration
├── 03_Consistency_and_Uniformity.pdf # CV calculations & multi-cabinet balance
├── 04_Step_Data_Blocks_and_Enthalpy.pdf # Thermodynamic reconciliation tables
├── 05_Time_Series_Charts.pdf # High-res oscillograms & dynamic steps
├── 06_Changepoint_Audit_Log.pdf # Focus / FLOC / CPOP candidate log
├── 07_Raw_Telemetry_Archive/
│ ├── LB_RAW_1HZ_TELEMETRY.csv # Complete 1s raw data file
│ └── LB_RAW_1HZ_TELEMETRY.csv.sha256 # Immutable SHA-256 cryptographic hash
└── 08_Calibration_Certificates/
 ├── PT100_RTD_Calibration.pdf # NIST/ISO 17025 calibration sheets
 ├── Vortex_Flow_Meter_Cal.pdf # Factory flow calibration certificate
 └── Power_Transducer_Class02.pdf # Electrical meter calibration tag
```

When an auditor or commissioning agent receives this package, they can verify the SHA-256 hash of the raw CSV file in five seconds, re-run the aggregation calculations in Python, and independently confirm every number on the executive flash report.

That is the standard of an engineering field guide.

## Decisions to record

Before sealing the formal handover package, verify and document:

- The calculated SHA-256 checksum of the raw CSV telemetry file, signed by the Recorder.
- The archive storage URI or repository location where the immutable raw files are stored.
- The list of all included instrument calibration certificates and their expiration dates.
- The final acceptance signatures of the Sheet Owner and the Third-Party CxA.


# 11. The sentence of acceptance or refusal

The opening paragraph of a flash report must be a single, unambiguous sentence. 

It is either the formal declaration of technical acceptance, or it is the explicit sentence of refusal. There is no middle ground. There is no polite paragraph explaining that the machine showed "tremendous potential" or that the afternoon was "largely successful despite a minor anomaly."

In mission-critical data center commissioning, vagueness is a liability. Ambiguous prose in a test report is how unverified equipment gets plugged into live, multimillion-dollar computing infrastructure. An auditor, an owner, or a contractor foreman should be able to read the opening sentence and know with absolute legal and technical certainty whether the machine stands accepted or rejected.

## The grammar of technical acceptance

If all five attempted scene passes achieved PASS, if multi-cabinet consistency satisfied its CV thresholds, if the enthalpy closure ratio exceeded 97.0%, and if the telemetry stream was verified live and unfrozen, write the **Sentence of Acceptance**:

> **"We certify that Liquid Load Bank Test Run [RUN-ID], executed on [DATE] at [DATA HALL / SUITE], has fully satisfied all five mandatory operational passes—Pretest, Stepped Gradient, Overload Visit, Step Change Jump, and 2N Single-Feed Fault—in strict accordance with [SPECIFICATION TITLE, REVISION MARK]. All parallel cabinets maintained flow consistency within CV = [X.X]% (threshold <= 5.0%) and electrical consistency within CV = [X.X]% (threshold <= 1.0%). Total energy enthalpy closure achieved [XX.X]% with zero frozen-register telemetry repeats. We certify that the test cluster represents compliant rack-side duty and recommend advancing to Level 5 Integrated System Testing."**

Notice the strict grammatical construction of this sentence:
- It names the unique Run ID and the physical location.
- It names all five passes explicitly by name.
- It cites the frozen document title and revision mark that established the criteria.
- It states the exact calculated consistency metrics (CV) alongside their numerical thresholds.
- It certifies the thermodynamic enthalpy closure percentage and the non-frozen status of the raw telemetry.
- It concludes with an unambiguous operational recommendation.

Every claim in the sentence is anchored to an auditable cell in the underlying report. A stranger reading this sentence can trace every clause directly to a timestamped table.

## The grammar of refusal

If even a single attempted scene failed, if multi-cabinet flow was severely imbalanced, or if a communication thread crashed, you do not write a softened sentence. You write the **Sentence of Refusal**:

> **"We refuse technical acceptance for Liquid Load Bank Test Run [RUN-ID], executed on [DATE] at [DATA HALL / SUITE]. While the cluster achieved PASS on Pretest, Stepped Gradient, and Overload, the run FAILED the 2N Single-Feed Fault scene at [TIMESTAMP UTC] when an intentional trip of Feeder A caused an unbuffered voltage sag on the 24VDC control bus, rebooting the supervisory PLC and losing telemetry for 142 seconds. Technical acceptance is denied, and the cluster is prohibited from Level 5 Integrated System Testing pending rectification of the diode-OR power supply and a certified re-test of the 2N drop scene."**

Notice the characteristics of the refusal sentence:
- It acknowledges the scenes that passed, preserving the credit of the engineering work that succeeded.
- It identifies the exact scene that failed and the exact timestamp of the failure.
- It names the precise physical root cause: an unbuffered voltage sag on the 24VDC control bus that rebooted the PLC.
- It states the specific consequence: loss of telemetry for 142 seconds.
- It concludes with an explicit operational prohibition and defines the exact technical remediation required before a re-test is permitted.

A refusal sentence written with this level of precision is not a defeat. It is the highest possible expression of engineering professionalism. It protects the facility from commissioning a hidden defect that would otherwise cause a catastrophic cluster outage during live AI training operations.

## The forbidden words of corporate euphemism

The flash report strictly forbids the vocabulary of corporate evasion. The following phrases must never appear anywhere in the document:

- *"The load bank performed satisfactorily overall..."* (Satisfactory is not a number. If it passed, state the pass; if it failed, state the failure).
- *"Cooling was generally in line with expectations..."* (Expectations are unwritten wishes; cite the specification revision and state the measured deviation).
- *"A minor telemetry glitch occurred, but the trend looked stable..."* (A telemetry glitch is lost or corrupted data; call it a missing read or a frozen buffer).
- *"The system demonstrated robust potential for high-density operation..."* (A load bank is a calibrated test instrument, not a student seeking encouragement).

Whenever you catch yourself writing a sentence designed to make a contractor, a vendor, or a client feel comfortable about a failed number, delete the sentence. Replace it with the measured value, the cited limit, and the verdict.

## The order of the first page

The first page of the flash report must follow this strict vertical order:

1. **Title & Run Identification Block** (Run ID, Date, Facility Location, Ambient Dew Point).
2. **The Sentence of Acceptance or Refusal** (Prominently displayed in bold text inside a dedicated summary panel).
3. **The Five Passes Audit Table** (Pretest, Gradient, Overload, Step Change, Single-Feed Fault with measured values, tolerances, and verdicts).
4. **The Consistency & Energy Closure Metrics** (Calculated CVs, Enthalpy Closure Ratio, Non-Zero Variance certification).
5. **The Authority Signatures Block** (Dated signatures of Sheet Owner, Operator, Recorder, and Stranger).

If a stranger reads only this first page, they possess 100% of the contractual and technical truth of the test run. The remaining pages exist solely to prove that this first page told the truth.

## Decisions to record

Before publishing the flash report, confirm:

- That the opening sentence has been selected—either the Sentence of Acceptance or the Sentence of Refusal—with zero euphemistic hedging.
- That all numbers embedded in the opening sentence exactly match the underlying data blocks.
- That the four required signatures have been affixed directly beneath the opening declaration.


# 12. Automated charting and visual integrity

An automated report generator or supervisory dashboard is a powerful tool for converting raw telemetry into rapid visual representations. However, an automated chart is not an independent authority. It is merely a visual projection of the numbers recorded in the underlying data blocks.

If a visual chart and a flash-report data block disagree, the numbers in the data block always govern. A handsome, smooth curve rendered by a plotting library does not possess the authority to pass a cell that the raw data table failed.

Furthermore, charting in commissioning is fraught with subtle visual deceptions—some accidental, some intentional. An uncalibrated vertical axis can flatten a dangerous 15% flow starvation until it looks like a hair-thin line, while a mislabeled title can cause an auditor to mistake electrical power consumption for certified liquid cooling capacity.

This chapter defines the strict rules of automated charting, visual scaling ethics, and required plot layouts.

## What the operator must set before any curve is drawn

An automated reporting script must never be allowed to guess the boundaries of its dataset. Before generating a single chart, the Operator must explicitly define two parameters in the script configuration:

1. **The Exact Time Window**: The start and end timestamps, defined to the exact second (e.g., `START = 2026-10-14T14:00:00Z`, `END = 2026-10-14T15:30:00Z`). The script must pull data strictly from within this window. An automated report that uses an ambiguous, floating window (such as "the last 60 minutes") will slide forward during review, altering calculated means as the system cools down.
2. **The Explicit Unit Roster**: The exact list of load-bank cabinet serial numbers active in the test (e.g., `UNITS = ["LB-01", "LB-02", "LB-03", "LB-04"]`). Never permit a reporting template to retain hardcoded unit lists from an earlier job. If a template titled "18-Cabinet Row Test" is run on a day when only 4 cabinets are connected, the resulting figures will be an embarrassing administrative mess.

Every generated chart must print its time window and active unit roster directly into its upper subtitle banner.

## The two-chart requirement: Overlaid cluster vs. individual deep dive

Whenever a physical parameter is presented in the automated report, generating a single aggregated chart is prohibited. A single chart showing only the cluster sum or cluster average conceals cabinet-level divergence.

The reporting engine must generate **two complementary charts** for every monitored quantity:

### Chart A: The Overlaid Cluster Chart
All parallel cabinets are plotted together on a single set of axes, using high-contrast, distinguishable line colors:
- This allows an auditor to instantly see if one cabinet "leaves the herd"—for example, observing three cabinets tracking at 176 LPM while Cabinet 4 drops to 124 LPM.
- The cluster arithmetic mean (μ) is plotted as a bold dashed yellow line through the center of the band.

### Chart B: The Individual Cabinet Deep-Dive Chart
Each individual cabinet is given its own dedicated plot panel with its own optimized vertical axis:
- This prevents a common scaling deception: if Cabinet 4's return temperature rises from 45.0°C to 49.8°C, plotting it on an overlaid chart whose vertical axis spans from 0°C to 100°C will make the 4.8K spike appear negligible.
- On its dedicated deep-dive chart, the vertical axis spans tightly across the operating window (e.g., 30°C to 55°C), ensuring that the temperature rise and any high-frequency hunting are clearly visible.

## The four summary statistics beneath every chart

Beneath every generated plot panel, the automated reporting engine must calculate and print a standardized summary table containing four specific metrics for that specific window:

1. **Minimum Value ($\min$)**
2. **Maximum Value ($\max$)**
3. **Arithmetic Mean (μ)**
4. **Median Value ($\tilde{x}$)**

### Why the Median is Mandatory
In automated telemetry ingestion, electrical contactor switching and high-voltage breaker operations can induce an electromagnetic interference (EMI) pulse that causes an analog-to-digital converter (ADC) to log a single, spurious 1-millisecond spike (e.g., logging a single sample of 1200 kW before returning to 120.0 kW).
- In a 900-sample dwell, that single bad sample will pull the arithmetic mean upward by 1.2 kW, distorting the energy closure calculation.
- The median is inherently robust against isolated outlier spikes. Comparing the mean (μ = 121.2 kW) against the median ($\tilde{x} = 120.0 kW$) immediately exposes the presence of an asymmetric spike.
- If the maximum and minimum are identical ($\max = \min = 45.000°C$), the reporting engine must automatically highlight the table in red with the label: **"WARNING: ZERO VARIANCE DETECTED (STALE BUFFER)."**

## The core chart categories

The automated report must produce five standardized chart suites:

### 1. Electrical Power Suite
- Total active cluster power (kW) over time.
- Individual cabinet active power overlaid and separate.
- 3-phase line-to-line voltages and feeder phase currents.
- Verification that Feeder A and Feeder B share power symmetrically (50% ± 1.0%).

### 2. Coolant Hydraulics Suite
- Volumetric flow rate per cabinet (Q_v, reported in LPM).
- Manifold differential pressure (ΔP = P_in - P_out, reported in kPa).
- Total secondary loop flow rate, explicitly derived as the sum of branch flow meters.

### 3. Thermal Enthalpy Suite
- Secondary coolant supply temperature (T_in) and return temperature (T_out) per cabinet.
- Differential temperature rise (ΔT = T_out - T_in) per cabinet.
- **The Sign Check Gate**: The difference must be strictly positive (T_out > T_in). If a plumbing error reversed the hoses, ΔT will plot as negative. The plotting script is strictly forbidden from applying an absolute value function (`abs(delta_t)`) to make a reversed connection look correct! A negative ΔT must plot as negative and trigger an automated FAIL flag.

### 4. True Inferred Heat vs. Electrical Power Suite
- Electrical active power (P_elec) plotted alongside true inferred liquid enthalpy (Q_liquid = ṁ C_p ΔT).
- Under no circumstances may an electrical power trace be re-titled as "Cooling Power"!
- Electrical power is energy delivered from the switchgear; cooling power is thermal energy absorbed by the fluid stream. Plotting them on the same axis with distinct colors immediately exposes any internal bypass leakage or missing heat.

### 5. Companion Air Suite
- Intake dry-bulb air temperature (T_air,in) and exhaust air temperature (T_air,out).
- Air temperature differential (ΔT_air).
- Inferred air sensible heat (Q_air).

## Rules of visual scaling ethics

Visual scales must never be manipulated to flatter the performance of the equipment. The following plotting rules are mandatory:

- **Ban on Suppressed Zeroes for Capacity Claims**: When plotting total power or total flow against rated nameplate duty, the vertical axis must include the zero baseline so the viewer can see the true magnitude of steps.
- **Ban on Over-Expanded Axes to Hide Variance**: When plotting temperature stability or flow uniformity across steady dwells, the vertical axis must not be artificially expanded to ± 100 K or ± 500 LPM to make severe hunting look like a straight line. The axis must be scaled tightly to the cited tolerance envelope (e.g., T_nominal ± 5.0 K).
- **Explicit Gridlines**: Every chart must render light horizontal and vertical gridlines at standard engineering intervals (e.g., every 5 minutes, every 10 kW, every 1.0 K) to permit rapid visual auditing without a digital ruler.

## Decisions to record

In the charting section of the flash report, document:

- The exact start and stop timestamps of the plotting window.
- The confirmed list of active cabinet serial numbers included in the visual generation.
- The sampling resolution of each plotted channel (1s raw vs 60s rolling mean).
- Confirmation that no absolute value transforms or artificial smoothing filters were applied to raw series.


# 13. Public sources and citation integrity

A flash report or commissioning document cell may cite an established public standard or published engineering guideline. It may never be replaced by one.

In modern mission-critical engineering, citation discipline protects both technical rigor and legal integrity. Citing an industry standard demonstrates that your verification methodology rests on defensible, peer-reviewed engineering consensus. However, copying copyrighted tables from private vendor handbooks or pasting proprietary customer schematics into a public report invites immediate copyright liability and non-disclosure violations.

This chapter defines the strict rules governing citations, intellectual property boundaries, and acceptable public engineering sources.

## What a citation may do and what it may not

A citation is a pointer to an external authority that supports an engineering method, a safety definition, or an environmental classification. 

### What a Citation May Do:
- **Establish Environmental Classes**: A citation to ASHRAE TC 9.9 may support the sentence: *"The secondary loop coolant supply temperature was audited against the ASHRAE Liquid Cooling Class W4 envelope (32°C to 45°C)."*
- **Define Electrical Ground Rules**: A citation to IEC 60204-1 or NFPA 70 may support the sentence: *"Main circuit disconnects and emergency stop interlocks were verified in compliance with IEC 60204-1, Section 9.2 (Stop Category 0: Uncontrolled stop by immediate removal of power to the machine actuators)."*
- **Anchor Commissioning Process Terminology**: A citation to ASHRAE Guideline 0-2019 may support the five-phase commissioning hierarchy (Level 1 Factory Witness Testing through Level 5 Integrated System Testing).
- **Reference Algorithmic Methods**: Citations to Romano et al. (arXiv:2607.19961) and Fearnhead et al. (DOI:10.1080/10618600.2018.1512868) establish the mathematical peer review of the Focus and CPOP changepoint algorithms.

### What a Citation May NOT Do:
- **A Citation Cannot Fill a Measured Cell**: Citing an NVIDIA GB200 NVL72 marketing white paper does not fulfill the duty to measure live return temperature on the test floor. An observed cell requires an observed reading from a calibrated physical sensor.
- **A Citation Cannot Waive a Missing Line**: You may not write *"Single-feed fault test omitted per industry practice"* and cite a generic commissioning handbook. A handbook cannot waive a contractually mandated test scene.
- **A Citation Must Not Be a Paste**: You may not photocopy or paste proprietary vendor curves, confidential customer floorplans, or copyrighted standard text into your report. Cite the document by formal title, issuing body, revision number, and publication year.

## Authorized public engineering references

The methodology of this field guide aligns with the following public, non-proprietary standards and industry bodies:

1. **ASHRAE Guideline 0-2019**: *The Commissioning Process*. Defines the standardized quality-focused commissioning process for facilities, including Owner’s Project Requirements (OPR), Basis of Design (BOD), and Verification Checklists.
2. **ASHRAE Guideline 1.1-2007**: *HVAC&R Technical Requirements for The Commissioning Process*. Governs functional performance testing protocols for primary and secondary fluid handling loops.
3. **ASHRAE TC 9.9**: *Thermal Guidelines for Data Processing Environments (5th Edition, 2021)*. Defines liquid cooling environmental classifications (Classes W1 through W5) and facility ambient dew point limits for condensation control.
4. **IEC 60204-1 (Edition 6.0, 2016)**: *Safety of Machinery – Electrical Equipment of Machines – Part 1: General Requirements*. Governs electrical isolation, overcurrent protection, emergency stop hardwired loops, and dielectric withstand tests for industrial machines.
5. **NFPA 70 (National Electrical Code, 2023 Edition)**: Article 645 (Information Technology Equipment) and Article 250 (Grounding and Bonding).
6. **Open Compute Project (OCP) Liquid Cooling Guidelines**: Open standards governing secondary fluid loop cleanliness, material compatibility (wetted metallurgy), and quick-disconnect classifications—explicitly distinguishing blade-level blind mates (UQD) from full-flow manifold test couplings (such as Danfoss FD83).
7. **ISA-5.1-2009**: *Instrumentation Symbols and Identification*. Governs the standardized drafting of Piping & Instrumentation Diagrams (P&IDs) for liquid cooling loops.

## Defending against vendor proposal evasion

A common tactic employed by under-prepared equipment suppliers during commissioning meetings is presenting a generic white paper or academic preprint in response to a failed test cell.

If a load-bank cabinet fails its 15-minute dwell due to severe flow starvation, and the vendor submits a published paper showing that "advanced microchannel cold plates can tolerate temporary boiling," reject the submission immediately.
- The white paper is an academic document describing a laboratory experiment under controlled conditions.
- Your test is an acceptance verification of a specific, contracted machine standing in for an NVL72-class production rack.
- The flash report records what the physical machine did on the floor against the cited specification revision. It does not debate academic possibilities.

Hold the boundary. Insist that citations remain bibliography lines, while the cells remain yours.

## Decisions to record

In the compliance and citation section of the flash report, document:

- The formal title, issuing organization, edition, and revision of every external standard cited in the report.
- The certification that no proprietary vendor text, confidential customer data, or copyrighted schematics were pasted into the document.
- The signed statement confirming that all technical limits were evaluated against the frozen project specification revision then in force.


# 14. Telemetry acquisition, Modbus-TCP, and MQTT pipelines

A flash report or automated chart is only as honest as the digital telemetry pipeline that populated its cells. 

In modern megawatt-scale data center testing, telemetry does not magically appear inside a database. It makes a series of discrete, physical and digital hops: from a wetted immersion RTD element, through a local analog-to-digital converter (ADC), across an industrial Modbus-TCP fieldbus, through an edge collector gateway, and over an MQTT message broker into an immutable time-series store.

If any single hop in that chain fails silently—if an edge poller stamps a fresh timestamp onto an un-updated memory buffer, or if an MQTT broker publishes a cached "retained" message from yesterday—the resulting flash report is pure fiction.

This chapter defines the technical specifications of each hop, detailing the exact Modbus register structures, byte-ordering conventions, Quality Bitmask architectures, and MQTT payload schemas required to guarantee data integrity.

(See Figure 02 for the end-to-end telemetry hop architecture, the IEEE-754 word-swapping trap, the 16-bit Quality Bitmask register, and the standardized JSON payload schema).

## Hop 1 & 2: Physical sensor to local transmitter

The journey begins at the physical process boundary:
- **Temperature**: 4-wire Class A Pt100 RTD elements immersed directly into the central core flow ($1/3 \sim 1/2 D$) of the manifold drops, packed with zinc oxide thermal compound inside angled 45° thermowells.
- **Volumetric Flow**: Inline vortex shedding flow meters providing pulse or high-frequency digital frequency outputs, immune to fluid viscosity shifts across the operating temperature band.
- **Differential Pressure**: Piezoresistive static pressure transmitters connected to flush, polished static taps drilled perpendicular to the pipe wall.

At the transmitter, high-accuracy 24-bit Sigma-Delta ADCs sample the physical bridge at 1 kHz, applying a local digital moving average filter to output a calibrated reading once per second (**1 Hz**).

## Hop 3: Modbus-TCP fieldbus architecture

The load-bank internal controller exposes its operational parameters over standard industrial **Modbus-TCP (Ethernet Port 502)** or Modbus-RTU (RS-485 serial bus operating at 115,200 baud, 8-N-1):

- **Discrete Coils (Function 0x01 / 0x05)**: Binary control states—solenoid valve positions (V-101 open/closed), immersion heater contactor feedback states, emergency stop circuit continuity, and leak rope relay status.
- **Input Registers (30001+, Function 0x04)**: Read-only sensor measurements generated directly by local hardware ADC channels.
- **Holding Registers (40001+, Function 0x03 / 0x06 / 0x10)**: Commanded load setpoints, operating mode configurations, and alarm limit thresholds.

### The IEEE-754 32-bit float byte-ordering trap
A single 16-bit Modbus register cannot store a 32-bit floating-point engineering quantity (such as a temperature reading of 45.12°C). Floating-point values require two consecutive 16-bit registers (4 bytes total).

Different microcontroller architectures implement different word-ordering conventions. If the edge gateway assumes the wrong word order, numbers will be completely corrupted:
- **CDAB (Big-Endian with Word Swap)**: The industrial standard for Modbus floats.
 - Reg 40001 = `0x4234`, Reg 40002 = `0x0000` $\implies$ Evaluates correctly to **45.00°C**.
- **ABCD (Big-Endian Direct)**:
 - Reg 40001 = `0x0000`, Reg 40002 = `0x4234` $\implies$ Evaluates to **1.87 × 10^{-38}** (Microscopic garbage!).
- **BADC (Little-Endian with Byte Swap)**: Evaluates to completely different arbitrary values.

The flash report's working setup sheet must cite the exact word-ordering convention used by the controller firmware. A temperature that suddenly jumps between seasons during commissioning is not an environmental miracle; it is an unverified word-swap parse error. Fix the parse in the edge gateway configuration; do not overwrite the raw incoming hex bytes.

### The mandatory 16-bit Quality Bitmask register (Reg 40050)
A raw number without a quality flag is an unverified assertion. The load-bank controller must maintain a dedicated **16-bit Quality Bitmask Register (Register 40050)** updated in real-time by internal firmware diagnostics:

- **Bit 0 (`0x0001`)**: `SUPPLY_TEMP_VALID` (1 = Healthy, 0 = Fault/Open-circuit)
- **Bit 1 (`0x0002`)**: `RETURN_TEMP_VALID` (1 = Healthy, 0 = Fault/Open-circuit)
- **Bit 2 (`0x0004`)**: `FLOW_METER_VALID` (1 = Healthy, 0 = Fault/Pulse-lost)
- **Bit 4 (`0x0010`)**: `SENSOR_STALE_ALERT` (Asserted if ADC repeats identical value for > 3s)
- **Bit 5 (`0x0020`)**: `COMM_TIMEOUT` (Asserted if internal transmitter bus times out > 250ms)
- **Bit 6 (`0x0040`)**: `OUT_OF_RANGE` (Asserted if RTD resistance breaches physical envelope)

If Register 40050 asserts Bit 4, 5, or 6, the edge gateway must immediately classify the reading as **FAULT** and log a missing gap, rather than publishing the corrupted number downstream.

## Hop 4: Edge gateway active polling

The edge gateway runs a deterministic 1 Hz polling loop querying the load-bank Modbus controller:
- The poller queries the input and quality registers every 1,000 milliseconds.
- **The Timeout Policy**: If the Modbus slave fails to respond within 250 milliseconds, the poller logs a **COMMUNICATION TIMEOUT** for that second.
- **Strict Ban on Painting Forward**: The edge gateway is strictly forbidden from caching the last successful reading and stamping it with the new second's timestamp! Painting forward the previous reading to prevent an empty cell is an intentional fabrication of data. A failed poll must be logged as `NaN` or `MISSING`. If three consecutive polls fail, the plateau is marked **INVALID**.

## Hop 5: MQTT telemetry broker and JSON schema

The edge gateway packages the live 1-second telemetry and publishes it to a local MQTT message broker:
- **Topic Hierarchy**: Must follow a clean, hierarchical asset topology:
 `dc/[hall_id]/[rack_id]/telemetry` (e.g., `dc/hall-03/lb-01/telemetry`)
- **Quality of Service**: Must use **QoS 1 (At Least Once Delivery)** with local persistence buffering to guarantee that network switch hiccups do not cause lost packets.

### The JSON Telemetry Schema
Every message published to the broker must conform to a standardized JSON schema containing timestamp, electrical, hydraulic, and quality blocks:

```json
{
 "timestamp": "2026-10-14T14:22:15.000Z",
 "rack_id": "LB-NVL72-01",
 "run_id": "RUN-2026-OCT-CX01",
 "commanded_kw": 120.0,
 "electrical": {
 "feeder_a_kw": 60.1,
 "feeder_b_kw": 59.9,
 "total_kw": 120.0,
 "voltage_v": 415.2,
 "current_a": 167.1,
 "pf": 0.999
 },
 "hydraulics": {
 "flow_lpm": 176.4,
 "supply_c": 35.08,
 "return_c": 45.12,
 "delta_t_k": 10.04,
 "dp_kpa": 112.5,
 "thermal_kw": 98.6
 },
 "companion_air": {
 "inlet_c": 24.2,
 "outlet_c": 38.5,
 "air_kw": 18.9
 },
 "quality": {
 "mask": "0x0007",
 "stale_flag": false,
 "raw_samples": 60
 }
}
```

### Two Lethal MQTT Habits to Forbid
1. **The Retained Message Trap**: In the MQTT protocol, a publisher can mark a message as "retained," causing the broker to store it and instantly deliver it to any new subscriber that connects later. If an automated flash-report script connects to the broker and ingests a retained message, it may ingest a reading that was published three days ago during a shop test! The test plan must mandate: **All telemetry publishers must set `retained = false`**.
2. **Last-Will-and-Testament Misinterpretation**: The broker's Last-Will-and-Testament (LWT) message (published when an edge gateway disconnects unexpectedly) must publish an explicit death payload (`{"status": "OFFLINE", "quality": "DEAD"}`). The reporting engine must recognize this payload immediately and halt dwell timers.

## The pre-heat stale proof test

Before commanding heat on the day of the test, the test team must execute the **Pre-Heat Stale Proof Test**:
1. With the data pipeline running and logging zero-load baseline data, an operator physically disconnects the signal cable of Return Temperature Sensor RTD-102 (or unplugs the Modbus Ethernet cable from Cabinet 2).
2. The Recorder monitors the live dashboard and the exported CSV file.
3. **The Proof of Compliance**: The export must instantly record `NaN`, `GAP`, or `DISCONNECTED` within 1 second, and the Quality Bitmask must transition to `0x0040` (Sensor Fault).
4. **The Proof of Failure**: If the dashboard or export continues to display 35.0°C with moving timestamps, the pipeline is guilty of painting forward stale data. The test is stopped immediately. You do not add heat until the telemetry pipeline proves it can honestly report a dead sensor.

## Decisions to record

In the acquisition section of the flash report, document:

- The confirmed Modbus register map revision and the verified float byte-ordering format (CDAB / Big-Endian Word Swap).
- The exact polling interval (1,000ms) and confirmed timeout threshold (250ms).
- The MQTT broker endpoint, topic string, and confirmation that retained messages were disabled.
- The certified execution of the Pre-Heat Stale Proof Test, noting the exact second the sensor was unplugged and the second the pipeline registered the gap.


# 15. Algorithmic analysis: Online detectors and offline CPOP

The five scene passes remain the ultimate human judgment of a load-bank test. An algorithm does not get a pen. 

However, in modern commissioning campaigns involving multiple parallel megawatt-class clusters, algorithmic anomaly detection serves as an invaluable, objective "ruler." It identifies subtle physical transitions that the human eye might miss—an uncommanded hydraulic valve creeping closed during an ostensibly steady dwell, a single heater element burning out inside an immersion shell, or a secondary coolant flow diversion caused by an unrecorded facility valve maneuver.

This chapter defines the strict operational boundaries governing two online changepoint detection frameworks (**Focus** and **FLOC**) and one offline piecewise-linear fitting method (**CPOP**).

(See Figure 05 for the multi-tier load test waveforms, the online trigger timeline, the offline piecewise-linear segmentation, and the algorithmic candidate classification protocol).

## Online versus offline: The fundamental distinction

The flash report enforces an absolute distinction between online and offline methods:

- **Online Methods (Focus, FLOC)**: Run sequentially in real-time as telemetry arrives second-by-second during an active test window. They may emit candidate event flags while the machine is operating. They are designed for live situational awareness.
- **Offline Methods (CPOP)**: Run strictly *after the export file has been stopped, closed, and cryptographically hashed*. They analyze the complete historical time series globally.

### Two Cardinal Protocol Rules:
1. **Never run an offline method on a live, growing file and call the result "online."** An offline algorithm assumes it has access to the full dataset; running it on an unclosed stream produces unstable edge artifacts that generate false alarms.
2. **Never run an online detector on a file that has already been edited, cleaned, or filtered, and call the result a "discovery."** An online detector must evaluate the raw stream in real-time. Running it on an edited CSV after the test is simply fitting a curve to a fait accompli.

## Online detector 1: Focus

**Focus** (Fast Online Changepoint Detection for Poisson and Gaussian streams) monitors a single continuous telemetry channel to detect shifts in mean or variance without requiring the file to end. 

The mathematical method is documented in the peer-reviewed literature by Romano, Ward, Fan, Rigaill, Runge, Eckley, and Fearnhead (*arXiv:2607.19961*, 2026). If you use Focus in your commissioning pipeline, cite that paper by title; do not reproduce its derivation inside the flash report.

### Operational Rules for Focus
- **Single Channel Monitoring**: Focus must be applied to **one raw physical channel at a time**—specifically return coolant temperature (T_out), volumetric flow (Q_v), or active power (P_elec). Applying it to a blended composite index (such as an artificial "cooling performance index") obscures the physical root cause of a detected shift.
- **Pre-Declared Threshold**: The anomaly detection threshold (λ) must be calculated and written onto the requirements sheet *before the test window opens*.
- **The Ban on Post-Hoc Retuning**: If Focus triggers an alert during a dwell, you are strictly forbidden from lowering the sensitivity or moving the threshold to silence the alert! Altering a threshold after seeing the data is a confession that the process was unstable. Record the candidate timestamp and proceed.

## Online detector 2: FLOC

**FLOC (Fast Localized Online Changepoints)** is a complementary online detector designed to track local variance ratios and short-term trend shifts across adjacent sliding windows (e.g., comparing a 30-second trailing window against a 120-second historical baseline).

### What an Online Hit Means
When Focus or FLOC triggers an alert during an active test, that hit is a **candidate timestamp**. It is not an automated verdict.

The Operator and Recorder must handle the candidate timestamp through a strict comparison protocol:
1. **Compare the Hit Against the Operator's Command Log**: 
 - If the candidate hit occurs at `14:30:02 UTC`, and the Operator's command log confirms that a load step from 60kW to 90kW was commanded at `14:30:00 UTC`, the hit is classified as an **EXPECTED STEP**. The detector simply noticed the scene transition you commanded.
 - If the candidate hit occurs at `14:42:15 UTC`—twelve minutes into a 15-minute steady dwell where no command was issued—the hit is classified as an **UNCOMMANDED MID-HOLD BREAK**.
2. **The Human Action for a Mid-Hold Break**:
 - The Recorder marks the plateau for immediate inspection.
 - If the pre-declared test protocol mandates that uncommanded breaks require an abort, heat is de-energized.
 - If the protocol allows completion, the dwell is completed, but the steady-state hold is **SPLIT** at the hit timestamp. The period prior to the hit may be evaluated for partial compliance; the period after the hit does not inherit the pass.

### The Ban on Averaging Disagreeing Hits
If FLOC triggers an alert at `14:42:10 UTC` and Focus triggers an alert at `14:42:25 UTC`, **never average the two timestamps** (`14:42:17.5 UTC`) and call that the changepoint! Averaging two algorithmic outputs creates a synthetic timestamp that corresponds to nothing in physical reality. Log both candidate times side-by-side in the report, and let the human auditor inspect the raw 1-second samples around both points.

## Offline method: CPOP (Continuous Piecewise-Linear Optimal Partitioning)

Once the testing campaign is complete, the export file is stopped, and the SHA-256 hash is sealed, the engineering team may apply **CPOP** to analyze steady-state holds.

Documented by Fearnhead, Maidstone, and Letchford (*Journal of Computational and Graphical Statistics*, 2019, DOI: 10.1080/10618600.2018.1512868), CPOP fits a continuous piecewise-linear model to a time series, identifying the exact moments where the physical slope of the data changed while minimizing an L2 fit cost with a penalty β on the number of slope changes:

$$\text{Cost} = \min_{K, \tau} \sum_{k=0}^K \sum_{i=\tau_k+1}^{\tau_{k+1}} (y_i - f_k(i))^2 + \beta \cdot K$$

where K is the number of changepoints, f_k is a linear segment, and β is the pre-declared penalty parameter.

### What CPOP Evaluates
CPOP is applied exclusively to the steady-state hold portion of a dwell, deliberately excluding the known thermal warm-up transient (t ≥ 4τ).
- **A Single Clean Slope (K = 0)**: If CPOP fits the hold as a single horizontal line with near-zero slope (|m| ≤ 0.001 K/s), it provides mathematical confirmation that the plateau achieved true thermal equilibrium.
- **A Mid-Hold Slope Break (K ≥ 1)**: If CPOP detects a changepoint in the middle of a steady hold, it indicates that a physical shift occurred:
 - If electrical power is flat, but fluid temperature slope suddenly turns upward, CPOP has detected a hydraulic flow restriction (such as an un-commanded valve drift or strainer fouling).
 - If fluid temperature slope suddenly turns downward, it reveals a bypass valve leak mixing cold fluid into the return stream.

### What CPOP Cannot Say
- CPOP cannot say that the plateau passed.
- CPOP cannot verify that the temperature rise agrees with electrical power.
- CPOP cannot confirm that the temperature differential has the correct sign (T_out > T_in). A beautifully fitted single slope that represents cold liquid entering hot and leaving colder is still a failed sign check!

CPOP is a ruler that measures geometric slopes. The requirements sheet and the human engineer provide the judgment.

## Decisions to record

In the algorithmic analysis section of the flash report, document:

- The software implementation names and version numbers for Focus, FLOC, and CPOP.
- The pre-declared anomaly threshold λ and offline penalty β written before data ingestion.
- The complete table of all candidate trigger timestamps, side-by-side with the Operator's command log timestamps.
- The human classification for every candidate: *Expected Step*, *Inspect / Split Hold*, or *No Impact*.
- The initials of the Stranger certifying that algorithmic tools were used solely as diagnostic rulers and did not issue automated verdicts.


# 16. Diagnostic casebook: How to handle an algorithmic hit

The changepoint detection algorithms described in the previous chapter generate timestamps. This final chapter provides the practical diagnostic casebook for what an engineer, an operator, and a third-party auditor must physically do when an algorithm emits a hit.

The scenarios presented here are composite operational case studies drawn from real commissioning campaigns on multi-megawatt high-density liquid cooling installations. If a case feels uncomfortably familiar, it is because these failure modes recur across the industry whenever teams attempt to rush a load-bank test.

## Case 1: The hit matches the commanded step

### The Operational Evidence
Focus or FLOC triggers an alert at `14:15:02 UTC`. The Operator’s log confirms that a commanded load step from 25% (30kW) to 50% (60kW) was initiated at `14:15:00 UTC`. Active electrical power stepped cleanly within 1.2 seconds, and return coolant temperature began a smooth exponential rise (τ ≈ 45 s).

### The Diagnostic Determination
- **Human Classification**: **EXPECTED STEP**.
- **Action**: The hit is documented in the audit log alongside the command timestamp (Δt = +2.0 s, well within the permissible 5-second control delay).
- **The Pitfall to Avoid**: Do not conclude that the detector is "too sensitive" and attempt to raise the detection threshold so that the next step is silent! Silence on a commanded step is proof that your detector is deaf. An honest algorithm *should* notice a commanded load step. Log the event and proceed.

## Case 2: An uncommanded hit inside a steady hold

### The Operational Evidence
The load bank is seven minutes into a planned 15-minute steady dwell at 100% load (120kW). Commanded electrical power has not moved. At `14:37:18 UTC`, FLOC triggers an alert on the return temperature channel. 

Upon examining the live data block, the Operator observes:
- Active electrical power remains perfectly constant at 120.1 kW.
- Volumetric flow rate on Cabinet 2 has drifted downward from 176.4 LPM to 142.1 LPM.
- Return coolant temperature on Cabinet 2 is ramping upward from 45.1°C to 48.9°C (ΔT expanding from 10.0K to 13.8K).

### The Diagnostic Determination
- **Human Classification**: **UNCOMMANDED MID-HOLD BREAK (HYDRAULIC ANOMALY)**.
- **Physical Root Cause**: A modulating trim valve actuator slipped under fluid pressure, an inline 50μm bypass strainer began clogging with construction swarf, or an operator accidentally nudged a manual ball valve on the secondary manifold.
- **Action**:
 1. If the pre-declared safety rule dictates that temperature drift above 48.0°C requires a halt, trip the heaters immediately.
 2. If the run completes without tripping, **SPLIT THE DWELL** at `14:37:18 UTC`. The first seven minutes prior to the break may stand as partial steady-state evidence. The final eight minutes **FAIL** the dwell stability criterion and cannot be used for the 100% capacity sign-off.
 3. Under no circumstances may an engineer average the entire 15-minute window into a single synthetic plateau! Averaging a deteriorating flow into an earlier healthy flow creates a comfortable fiction that masks hydraulic degradation.

## Case 3: Two online detectors disagree

### The Operational Evidence
During a 15-minute dwell, FLOC triggers an alert at `15:10:14 UTC`. Focus triggers an alert eighteen seconds later, at `15:10:32 UTC`. The Operator’s command log is completely quiet.

### The Diagnostic Determination
- **Human Classification**: **INSPECT RAW SCATTER**.
- **Action**:
 1. **Strict Ban on Averaging**: Never average the two timestamps (`15:10:23 UTC`)! An averaged timestamp is an imaginary artifact.
 2. Inspect the raw 1-second samples across the 60-second window spanning both hits.
 3. Frequently, FLOC (which evaluates local variance ratios) fires first because convective turbulence began to widen, while Focus (which evaluates cumulative sum shifts) fires second after the mean temperature drifted past its likelihood threshold.
 4. Both timestamps are recorded in the changepoint table as candidate bounds for a single continuous disturbance window: `[15:10:14 to 15:10:32 UTC]`. The human auditor evaluates the physical cause within that bracket.

## Case 4: The detector is quiet, but the channel is stale

### The Operational Evidence
A 15-minute dwell at 100% load finishes. Neither Focus nor FLOC emitted a single alert. A junior technician reports that the run was "extraordinarily stable."

Upon inspecting the raw CSV file, the Stranger observes that Return Temperature RTD-102 reported exactly 45.000000°C for 900 consecutive seconds. The calculated sample variance across the dwell is $σ² \equiv 0.000000 K²$.

### The Diagnostic Determination
- **Human Classification**: **STALE DATA / BUFFER FREEZE FRAUD**.
- **Physical Reality**: The detector was quiet because its input was dead! Changepoint algorithms evaluate deviations in numerical series; if the series is a flat constant, the algorithm sees zero deviations and remains silent.
- **Action**:
 1. The silence of the detector is evidence of telemetry failure, not process stability.
 2. The plateau is marked **FAIL** on the data quality gate.
 3. The edge gateway communication thread or ADC driver must be diagnosed and restarted, and the entire load step must be re-run from scratch.

## Case 5: Offline CPOP marks a slope break at the start of a hold

### The Operational Evidence
The test run is complete, the file is closed, and CPOP is executed on the 100% load dwell. CPOP identifies a slope change at Minute 02 of the 15-minute hold. Commanded electrical power was constant throughout.

### The Diagnostic Determination
- **Human Classification**: **TRANSIENT BOX MISALIGNMENT**.
- **Physical Root Cause**: The Operator drew the steady-state evaluation box too early! The first two minutes of the dwell represented the physical thermal warm-up transient of the fluid loop and the heavy stainless steel vessel shell (τ ≈ 45 s). During those two minutes, fluid temperature was still curving upward toward its asymptotic limit. CPOP correctly identified the transition from the curved warm-up transient to the horizontal steady plateau.
- **Action**:
 1. Do not claim that "the plateau failed CPOP."
 2. Adjust the analytical evaluation box on the project sheet to start at Minute 04 (t ≥ 4τ).
 3. Re-run CPOP on the truncated window `[Minute 04 to Minute 15]`. If CPOP now fits the remaining 11 minutes as a single clean horizontal slope (|m| ≤ 0.001 K/s), the steady-state plateau is mathematically verified.
 4. Document the thermal time constant (τ = 45 s) in the report as the engineering justification for the window boundary.

## Case 6: CPOP detects a mid-hold slope break while power is flat

### The Operational Evidence
On a closed file, CPOP analyzes a 15-minute dwell and places an unambiguous slope break at Minute 09. Active electrical power is a single horizontal slope (P_elec = 120.1 kW ± 0.1 kW). Volumetric flow is also flat. But the temperature slope transitions from 0.000 K/s (horizontal) to +0.008 K/s (climbing upward).

### The Diagnostic Determination
- **Human Classification**: **PRIMARY FACILITY COOLING DRIFT**.
- **Physical Root Cause**: Because electrical power and secondary flow were constant, the rising return temperature cannot be caused by the load bank. It was caused by the **primary facility chilled water loop**: the facility central chiller plant experienced a cooling tower fan stage drop, causing secondary supply coolant entering the load bank (T_in) to warm up from 35.0°C to 37.2°C.
- **Action**:
 1. Verify the supply temperature channel: if T_in mirrors the slope of T_out, the load bank's internal temperature rise (ΔT = T_out - T_in) remained perfectly flat at 10.04K.
 2. Write an honest boundary sentence attributing the temperature rise to primary facility supply drift (External Gear - CDU Line).
 3. The load bank's thermal capacity stands verified; the facility primary loop stability is logged as a limitation.

## Case 7: CPOP is clean, but the thermal sign is wrong

### The Operational Evidence
CPOP fits a 15-minute full-load dwell with a flawless, single horizontal slope (K = 0, zero variance). But the measured supply temperature is 45.1°C and return temperature is 35.0°C.

### The Diagnostic Determination
- **Human Classification**: **REVERSED HYDRAULIC CONNECTION**.
- **Physical Reality**: The test crew connected the supply hose to the load-bank return port and the return hose to the supply port! The fluid is entering hot from a neighboring heat exchanger and leaving colder, or the software channel labels were inverted in the Modbus translation table.
- **Action**:
 1. An algorithm does not know the physical meaning of "supply" and "return"; it only fits numbers. A clean slope of the wrong sign is still a catastrophic failure of the sign check.
 2. The run is an immediate **FAIL**.
 3. Under no circumstances may an engineer apply an absolute value function to invert the sign on the final slide! Correct the hose routing or fix the channel label on the test floor, and repeat the run in broad daylight.

## Case 8: Someone demands a single number for an executive slide

### The Operational Evidence
A project manager or executive approaches the test desk before the formal report is assembled and demands: *"Just give me a single number for the changepoint on Cabinet 3 so I can paste it into the morning slide deck."*

You have an Operator log showing a step command at `14:20:00`, a FLOC hit at `14:20:03`, a Focus hit at `14:20:18`, and a CPOP slope transition at `14:23:45`.

### The Diagnostic Determination
- **The Engineer's Response**:
 1. **Refuse to Provide an Averaged Number**: You may not calculate $\frac{14:20:00 + 14:20:03 + 14:20:18 + 14:23:45}{4}$ and hand over a fabricated timestamp of `14:21:01.5`!
 2. **Present the Auditable Table**: Provide the structured table:
 - *Commanded Step Time*: `14:20:00 UTC`
 - *Online Detection Window*: `14:20:03 to 14:20:18 UTC`
 - *Thermal Settling Horizon (CPOP)*: `14:23:45 UTC` (Settling time Δt = 225 s)
 - *Human Classification*: **EXPECTED LOAD STEP (PASS)**
 3. If the executive refuses to show the table, the slide gets only the human verdict and the command time. It does not get an invented intermediate number.

## Summary: The standard procedure on the day

Follow this exact chronological protocol during every testing campaign:

1. **Before Heat**: Verify the immutable raw CSV logging path. Confirm that Focus, FLOC, and CPOP thresholds are frozen on the sheet. Run the Pre-Heat Stale Proof Test (disconnect one sensor and prove the pipeline registers a gap).
2. **During the Active Window**: Monitor the live telemetry stream. For every online candidate hit, immediately record the timestamp beside the Operator's command log. Apply the pre-written rule: mark or halt. Never extend a dwell to "see if a hit disappears."
3. **After File Closing**: Cryptographically hash the raw CSV file (SHA-256). Run offline CPOP on the steady dwell boxes (excluding the initial 4τ warm-up window).
4. **Compile the Audit Table**: Align all candidate hits against command log events. Initial the human classification for every row (*Expected Step*, *Inspect / Split Hold*, *No Impact*).
5. **Enforce the Five Passes**: Transfer the verified findings to the first page of the flash report. Sign the Sentence of Acceptance or file the explicit Sentence of Refusal.
