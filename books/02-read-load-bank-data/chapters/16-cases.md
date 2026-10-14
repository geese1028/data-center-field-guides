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
