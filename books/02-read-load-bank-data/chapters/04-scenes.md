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
