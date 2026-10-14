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
