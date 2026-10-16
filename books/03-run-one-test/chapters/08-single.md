# 8. One system at a time

Dynamic verification with multiple interconnected systems under thermal load is a later, integrated phase. This phase is dedicated to validating one machine at a time, executing the precise operational logic defined in its standalone test script while all adjacent systems remain quiet.

In the global commissioning hierarchy, this is **Level 4 Functional Performance Testing (FPT)**. It validates the autonomous protection, modulating control loops, and physical alarms of individual machines before they are subjected to multi-megawatt thermal stress. Filing single-system testing under Level 5 Integrated Systems Testing simply because the equipment is physically located in the data hall is a serious documentation error.

![CDU Hydraulic P&ID Architecture](../figures/fig-02-cdu-hydraulic-pandid.png)

## Autonomous Coolant Distribution Unit (CDU) Verification

The Coolant Distribution Unit is the critical hydraulic interface separating the facility primary water system (FWS) from the secondary technology cooling system (TCS). Before any thermal load is applied by the load banks, the CDU must prove its ability to control fluid circulation autonomously under Script 04 and Script 05.

### 1. Pump Startup, VFD Modulation, and Soft-Start
Energize the CDU secondary pumps with the primary facility loop isolated. Execute controlled start and stop cycles:
- Verify that the Variable Frequency Drives (VFDs) ramp the canned centrifugal pumps smoothly over their configured acceleration curve (typically 10 to 15 seconds) without causing electrical current spikes or hydraulic surges.
- Verify manual frequency override: drive the VFDs across their operating range (30.0 Hz to 50.0/60.0 Hz) and record motor current, power factor, and bearing vibration signatures.

### 2. N+1 Secondary Pump Auto-Changeover
Modern high-density CDUs employ an N+1 secondary pumping configuration (e.g., dual 100% capacity pumps, P-1A Lead and P-1B Standby). The automatic changeover logic must be verified through physical trip simulation:
- Operate Pump P-1A at 100% nominal speed with the loop at design operating flow.
- Simulate an electrical trip by opening the control circuit breaker to the P-1A inverter or triggering its digital fault input.
- **Acceptance Criteria**:
 - The local CDU controller must detect the fault, log a critical alarm, and issue a start command to standby Pump P-1B within ≤ 500 ms.
 - Standby Pump P-1B must accelerate to full operating speed and restore secondary differential pressure within ≤ 1.5 seconds.
 - The discharge non-return check valve on Pump P-1A must seat firmly without violent hydraulic slam (peak water hammer pulse must not exceed ± 50 kPa).
 - Secondary loop differential pressure must not drop below the minimum cavitation floor (100 kPa), ensuring continuous flow through the load banks without triggering false thermal trips.

### 3. Modulating Temperature Control Valve (TCV) Tracking
The primary loop Temperature Control Valve (TCV-101, typically a modulating 2-way or 3-way globe valve with an electronic actuator) regulates primary facility chilled water flow through the Plate Heat Exchanger (PHE-101) to maintain secondary supply temperature:
- Drive the actuator through its full control range using a 0–10V DC or 4–20 mA calibration source.
- Verify full-stroke opening and closing times against the manufacturer submittal (typically τ ≤ 30 seconds).
- Verify fail-safe position upon loss of control power: TCV-101 must fail mechanically open (100% primary flow) or hold last position depending on facility design intent.
- Verify seat leakage integrity: with the valve commanded 100% closed, confirm that primary flow drops to zero (leakage class ANSI/FCI 70-2 Class IV or better).

### 4. Secondary Differential Pressure Bypass Valve (BPV)
Inspect modulating bypass valve BPV-201, installed across secondary supply and return headers. Verify that as downstream manifold balancing valves are throttled, the BPV modulates open smoothly to maintain constant pump head, preventing impeller dead-heading.

## BMS Telemetry and Field Instrument Point-to-Point Checks

Never assume that a value displayed on a Building Management System (BMS) screen or CDU human-machine interface (HMI) reflects physical reality. Every telemetry point defined in the project claim must undergo physical point-to-point cross-checking against calibrated field reference instruments:

**POINT-TO-POINT TELEMETRY CALIBRATION AUDIT**

| TELEMETRY POINT | BMS / HMI READING | FIELD CALIBRATED REF | ALLOWABLE DELTA | AUDIT VERDICT |
| :--- | :--- | :--- | :--- | :--- |
| Secondary Supply T | 40.12 °C | 40.08 °C (PT100) | +/- 0.30 K | PASS |
| Secondary Return T | 50.25 °C | 50.15 °C (PT100) | +/- 0.30 K | PASS |
| Secondary Flow Rate | 115.4 m³/h | 116.1 m³/h (Ultrason) | +/- 2.0% | PASS |
| Secondary Supply P | 285.0 kPa | 282.5 kPa (Gauge) | +/- 10.0 kPa | PASS |
| Secondary Return P | 115.0 kPa | 118.0 kPa (Gauge) | +/- 10.0 kPa | PASS |
| Expansion Tank Level | 68.0 % | 67.5 % (Sight Glass) | +/- 3.0 % | PASS |

If a discrepancy exceeds the allowable tolerance, the sensor offset must be recalibrated or the sensor replaced. Never adjust the acceptable tolerance band to match a drifting sensor.

## Physical Hardware Alarm Injection

Alarms must be validated through physical hardware injection. Simulating an alarm by altering a software setpoint in a configuration file or toggling a bit in an engineering workstation is completely unacceptable. Software simulation proves that software can read a variable; it does not prove that the physical sensor, field wiring, and relay logic function under real-world conditions.

Execute physical alarm testing under Script 06:
- **Secondary Low Flow Alarm**: Gradually throttle the manual isolation valve on the secondary supply header until the electromagnetic flowmeter registers flow dropping below the low-flow trip threshold. Confirm that the CDU controller sounds the local alarm horn, illuminates the red beacon, transmits an urgent Modbus/BACnet alarm to the central BMS, and trips the load-bank interlock relay.
- **Expansion Tank Low Liquid Level**: Manually depress the test lever on the expansion tank magnetic float switch. Verify that the CDU alerts the operator, locks out the electric heaters, and commands the automatic makeup water pump to start.
- **Secondary Loop Liquid Leak Detection**: Apply 5 mL of demineralized water across the external leak detection sensing rope positioned beneath the CDU piping connections and the manifold tray. Verify that the leak detection controller triggers within < 2.0 seconds, displays the exact leak distance location, and sends a critical latching alarm to the supervisory BMS.

**THREE POSSIBLE AUDIT VERDICTS FOR AN ALARM**

| 1. PASS | Alarm physically injected at sensor; local annunciator active; BMS logged event with correct timestamp and description; interlock executed cleanly. |
| :--- | :--- |
| 2. FAIL | Alarm injected but sensor failed to detect; delay exceeded tolerance; interlock relay failed to drop; logged immediately on Master Punch List. |
| 3. NOT DEMONSTRATED | Equipment lacks the physical sensor, wiring, or software register to raise this alarm. Explicitly logged as "NOT DEMONSTRATED" on Sheet 2. Never "PASS". |

If a specific alarm cannot be demonstrated because the hardware was omitted during construction, the line on Sheet 2 must be recorded as **NOT DEMONSTRATED**. Logging an untested alarm as "PASS" because "the vendor promised the logic works" is a serious professional breach.

## The Level 4 Prerequisite Gate

Level 4 functional performance testing concludes when all single-system scripts are fully executed and signed. Any failed alarm injection, uncalibrated sensor, or hunting control valve must be formally resolved and re-tested before the facility advances to multi-system thermal testing.

## Decisions to record before test start

- CDU pump soft-start and VFD frequency tracking logs.
- The witnessed N+1 secondary pump auto-changeover transient records (switchover delay ≤ 1.5 s).
- The point-to-point telemetry calibration log across all critical monitoring points.
- The physical alarm injection log, noting all Pass, Fail, and Not Demonstrated items.
- Confirmation that all Level 4 prerequisites are signed off prior to opening Level 5.
