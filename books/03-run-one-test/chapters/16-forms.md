# 16. The sheets

Copy these master engineering forms into your project binder. Fill every cell in ink on the data hall floor. One engineer measures with calibrated instruments; a second engineer records the reading. A blank cell is an automated stop. A number copied from memory is a defect.

---

## Sheet 1. Pre-Energization Static QA & Hydraulic Verification (Level 2 / Level 3)

**Project Name**: __________________________ **Data Hall / Room ID**: __________________________ 
**Test Unit (CDU / Row ID)**: ________________ **Date of Verification**: __________________________ 
**Lead Electrical PE**: ____________________ **Lead Mechanical PE**: __________________________ 
**Measurement Tech**: ______________________ **Ink Recording Tech**: __________________________ 

### 1. Physical Uncrating, Structural & Coupling Inspection
- [ ] Load-bank frames inspected for shipping damage, weld cracks, or caster deformation: **PASS / FAIL**
- [ ] Quick-disconnect couplings inspected (Danfoss Hansen FD83 / ISO 16028): **PASS / FAIL**
- [ ] EPDM internal elastomeric seals inspected under magnification (zero cuts, tears, or burrs): **PASS / FAIL**
- [ ] High-pressure secondary flexible hoses inspected (wire-braided, rated ≥ 1.5× MAOP): **PASS / FAIL**
- [ ] Hose routing verified: zero kinks, all bends exceed minimum allowable bend radius: **PASS / FAIL**
- [ ] Seismic anchoring and floor pedestal understructure verified against structural PE drawings: **PASS / FAIL**

### 2. De-Energized Electrical Isolation & Safety Testing (LOTO Enforced)
- **Insulation Resistance Tester Model & Serial Number**: ____________________ **Calibration Expiry**: ____________ 
- **Test Voltage Applied**: 1000V DC for 60 seconds continuous 
 - Phase A to Phase B: __________ MΩ (Limit: ≥ 100.0 MΩ) — **PASS / FAIL** 
 - Phase B to Phase C: __________ MΩ (Limit: ≥ 100.0 MΩ) — **PASS / FAIL** 
 - Phase C to Phase A: __________ MΩ (Limit: ≥ 100.0 MΩ) — **PASS / FAIL** 
 - Phase A to Ground (PE): ______ MΩ (Limit: ≥ 100.0 MΩ) — **PASS / FAIL** 
 - Phase B to Ground (PE): ______ MΩ (Limit: ≥ 100.0 MΩ) — **PASS / FAIL** 
 - Phase C to Ground (PE): ______ MΩ (Limit: ≥ 100.0 MΩ) — **PASS / FAIL** 
- **Ground Bond Continuity**: Chassis to Main Facility Ground Busbar: __________ Ω (Limit: ≤ 0.10 Ω) — **PASS / FAIL** 
- **Phase Sequence & Rotation Indicator**: Tested at supply tap box: **CLOCKWISE (A-B-C) / COUNTER-CLOCKWISE** 
 *(CRITICAL: If phase sequence is not clockwise, do NOT energize. Reverse rotation will destroy canned pump bearings.)*

### 3. Secondary Hydraulic Flush, Hydrostatic Hold & Volume Audit
- [ ] Secondary loop chemical flushing completed per BSRIA BG 29/2020 (≥ 1.5 m/s scouring velocity): **ATTACHED** 
- [ ] Strainers inspected and cleaned; ISO 4406 fluid cleanliness certificate: **ATTACHED** 
- **Hydrostatic Pressure Hold**: 
 - Maximum Allowable Operating Pressure (MAOP): __________ bar 
 - Test Hold Pressure Applied (1.5× MAOP): __________ bar 
 - Start Timestamp: ____________________ End Timestamp: ____________________ (Duration: ≥ 2.0 hours) 
 - Start Pressure: __________ bar End Pressure: __________ bar Pressure Decay (ΔP): __________ bar 
 - Acceptance Standard: ΔP ≤ 0.0 bar (accounting for thermal stabilization). Leak rate: **ZERO DROPS / MIN** 
 - Verification Verdict: **PASS / FAIL** 
- [ ] Vacuum deaeration and thorough air purge completed; sight glasses clear of microbubbles: **PASS / FAIL** 
- **Secondary Fluid Inventory Calculation**: 
 - CDU Internal Volume: __________ L 
 - Manifold Distribution Volume: __________ L 
 - Flexible Hoses Volume: __________ L 
 - Load-Bank Internal Volume: __________ L 
 - **Total Secondary Fluid Inventory (V_total)**: __________ L 
- **Fluid Chemistry Baseline**: Refractometer PG Concentration: __________ % (Target: 25.0% ± 0.5%) 

### 4. Upstream Protective Coordination Audit
- Upstream PDU Breaker Frame Rating: __________ A Trip Plug Rating: __________ A 
- Electronic LSIG Settings: Long Time: ______ s Short Time Pickup: ______ x Instantaneous: ______ x 
- [ ] Protective coordination curves verified against load-bank inrush characteristics: **PASS / FAIL** 

**SHEET 1 GATE VERDICT**: [ ] **STAGE PASSED — CLEARED FOR LEVEL 4** [ ] **STAGE BLOCKED (OPEN DEFECT)** 
**Lead Electrical PE Signature**: ________________________ **Date**: __________________ 
**Lead Mechanical PE Signature**: ________________________ **Date**: __________________ 

---

## Sheet 2. Autonomous CDU Protection & Physical Alarm Injections (Level 4 FPT)

**Project Name**: __________________________ **Data Hall / Room ID**: __________________________ 
**CDU Asset Tag**: __________________________ **Firmware / Software Rev**: ______________________ 
**Lead Controls PE**: ______________________ **Mechanical PE**: ______________________________ 
**Facility Operations Witness**: ____________ **Test Date & Shift**: ____________________________ 

*Every alarm row must be physically injected at the sensor or field wiring. Software setpoint simulation is prohibited.*

| ALARM DESCRIPTION | PHYSICAL INJECTION METHOD | LOCAL SOUNDER / BEACON | CDU HMI ANNUNCIATOR | SUPERVISORY BMS TIMESTAMP | INTERLOCK TRIP ACTION | AUDIT VERDICT (PASS / FAIL / NOT DEMONSTRATED) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Secondary Low Flow** | Throttle supply balancing valve until flow drops below low setpoint (<90 m³/h) | [ ] Aud [ ] Vis | [ ] Alert logged | [ ] Logged: ________ | Trips load-bank interlock relay | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Secondary High Supply T** | Apply calibrated thermal bath or resistor bridge to PT100 immersion probe (>45.0°C) | [ ] Aud [ ] Vis | [ ] Alert logged | [ ] Logged: ________ | Triggers load-bank staged heat shed | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Secondary Low Pressure** | Partially vent pressure transmitter isolation block until P < 100 kPa | [ ] Aud [ ] Vis | [ ] Alert logged | [ ] Logged: ________ | Locks out electric heaters | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Expansion Tank Low Level**| Manually actuate magnetic float test stem to minimum low-level cutoff | [ ] Aud [ ] Vis | [ ] Alert logged | [ ] Logged: ________ | Commands auto-makeup pump START | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Primary Low Water Flow** | Throttle primary FWS isolation valve until flow < 50 m³/h | [ ] Aud [ ] Vis | [ ] Alert logged | [ ] Logged: ________ | Modulates TCV to 100% full open | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Primary High Supply Temp**| Elevate primary water temp or inject sensor offset (> 35.0°C) | [ ] Aud [ ] Vis | [ ] Alert logged | [ ] Logged: ________ | Warning logged; flags facility PUE | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Lead Pump VFD Inverter Trip**| Disconnect digital fault input or open VFD control power breaker | [ ] Aud [ ] Vis | [ ] Alert logged | [ ] Logged: ________ | Starts Standby Pump within ≤ 1.5 s | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Internal Catch-Pan Leak** | Apply 5 mL demineralized water across optical / float catch-pan sensor | [ ] Aud [ ] Vis | [ ] Alert logged | [ ] Logged: ________ | Isolates CDU; trips load-bank contactor | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **External Sensing Rope Leak**| Wet external perimeter sensing rope along secondary manifold tray | [ ] Aud [ ] Vis | [ ] Alert logged | [ ] Logged: ________ | Pinpoints location; trips alert | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Emergency Stop Pushbutton**| Depress physical red mushroom E-Stop button on CDU front door | [ ] Aud [ ] Vis | [ ] Alert logged | [ ] Logged: ________ | Drops 24V bus; cuts pump & heater relays | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |

### Hardware Interlock and Standby Failover Times
- Standby Pump Auto-Start Measured Delay: __________ ms (Limit: ≤ 500 ms) 
- Secondary Flow Restoration Measured Time: ______ s (Limit: ≤ 1.5 s) 
- Minimum Secondary Loop Pressure During Failover: ______ kPa (Limit: ≥ 100 kPa) 
- Physical E-Stop Power Cut Measured Delay: ______ ms (Limit: ≤ 50 ms) 

**SHEET 2 GATE VERDICT**: [ ] **LEVEL 4 PASSED — CLEARED FOR LEVEL 5** [ ] **LEVEL 4 BLOCKED (OPEN DEFECT)** 
**Lead Controls PE Signature**: ________________________ **Date**: __________________ 
**Facility Operations Witness**: ________________________ **Date**: __________________ 

---

## Sheet 3. Multi-Stage Thermal Step & Enthalpy Heat Closure Log (Level 5 IST)

*Execute one dedicated copy of Sheet 3 for each thermal step rung: 25%, 50%, 75%, 100%, and 110%.*

**Step Number**: Step _____ of 5 **Target Thermal Load**: __________ kW (______ % of Rated Capacity) 
**Step Start Timestamp**: ____________________ **Equilibrium Timestamp**: ____________________ 
**Total Dwell Duration**: __________ minutes (Minimum requirement: ≥ 45 min; 100% soak ≥ 4.0 h) 
**High-Frequency CSV File Name**: __________________________ **SHA-256 Checksum**: ________________________ 

### 1. Thermodynamic & Enthalpy Heat Balance Telemetry

| PARAMETER | SCRIPT SPEC LIMIT | MEASURED VALUE (FIELD REF) | BMS / TELEMETRY LOG | AUDIT DELTA |
| :--- | :--- | :--- | :--- | :--- |
| **Active 3-Phase Power (P_elec)** | Target: _____ kW ± 1.5% | __________ kW (Class 0.2) | __________ kW | ______ % |
| **Primary Supply Temp ($T_pri\_sup$)** | Nominal: 30.0°C ± 1.0 K | __________ °C | __________ °C | ______ K |
| **Primary Return Temp ($T_pri\_ret$)** | Expected: ≤ 36.5°C | __________ °C | __________ °C | ______ K |
| **Primary Volumetric Flow (Q_pri)** | Maximum: ≤ 180 m³/h | __________ m³/h | __________ m³/h | ______ % |
| **Primary Differential Pressure (ΔP_pri)**| Design: ≤ 120 kPa across PHE | __________ kPa | __________ kPa | ______ kPa |
| **Secondary Supply Temp ($T_sec\_sup$)** | Setpoint: 40.0°C ± 0.5 K | __________ °C (PT100 Ref) | __________ °C | ______ K |
| **Secondary Return Temp ($T_sec\_ret$)** | Expected: ≤ 50.5°C | __________ °C (PT100 Ref) | __________ °C | ______ K |
| **Secondary Fluid Delta-T (ΔT_sec)** | Design: 10.0 K ± 0.5 K | __________ K | __________ K | ______ K |
| **Secondary Volumetric Flow (Q_sec)** | Design: 115.0 m³/h ± 3.0% | __________ m³/h (Ultrasonic) | __________ m³/h | ______ % |
| **Secondary Pump VFD Frequency** | Operating range: 30.0 to 50.0 Hz | __________ Hz | __________ Hz | ______ Hz |
| **Secondary Pump Differential P (ΔP_pump)**| Design: 220 kPa ± 10 kPa | __________ kPa | __________ kPa | ______ kPa |
| **Primary TCV Valve Position** | Modulating tracking (0-100%) | __________ % open | __________ % open | ______ % |

### 2. Thermal Equilibrium and Enthalpy Closure Calculations
- **Thermal Stabilization Rate**: $\left|\frac{dT_{\text{supply}}}{dt}\right| = \text{__________ K / 10 min}$ (Acceptance Limit: ≤ 0.20 K / 10 min) — **PASS / FAIL** 
- **Secondary Liquid Heat Extraction**: 
 $$Q_{\text{liquid}} = \dot{m} \cdot c_p \cdot (T_{\text{return}} - T_{\text{supply}}) = \text{__________ kW}$$ 
 *(Evaluate ρ and c_p for 25% Propylene Glycol at bulk temperature: $T_{\text{bulk}} = \frac{T_{\text{sup}} + T_{\text{ret}}}{2}$)* 
- **Enthalpy Heat Closure Ratio**: 
 $$\eta = \frac{Q_{\text{liquid}}}{P_{\text{elec}}} \times 100\% = \text{__________ \%} \quad (\text{Acceptance Band: } 97.0\% \le \eta \le 101.5\%)$$ — **PASS / FAIL** 
- **Dew Point Margin**: 
 - Data Hall Ambient Temperature: ______ °C Relative Humidity: ______ % Calculated Dew Point: ______ °C 
 - Margin: $T_sec\_sup - T_dew = __________ K$ (Acceptance Limit: ≥ 2.0 K) — **PASS / FAIL** 

### 3. Electrical Infrared (IR) Thermography Scan (30 Min into Step)
- Thermal Imaging Camera Model & Serial Number: ____________________ Calibration Expiry: ____________ 
- Peak Terminal Temperature Recorded: __________ °C (Acceptance Limit: ≤ 75.0°C) — **PASS / FAIL** 
- Physical Location of Hottest Terminal: __________________________________________________ 
- Maximum Phase-to-Phase Delta-T: __________ K (Acceptance Limit: ≤ 5.0 K) — **PASS / FAIL** 

### 4. Multi-Rack Secondary Flow Distribution Survey (10 Load Banks)

| RACK ID | LOAD BANK SERIAL | VOLUMETRIC FLOW (LPM) | DELTA FROM MEAN (%) | RACK dP (kPa) | PASS / FAIL |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Rack 01** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] PASS [ ] FAIL |
| **Rack 02** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] PASS [ ] FAIL |
| **Rack 03** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] PASS [ ] FAIL |
| **Rack 04** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] PASS [ ] FAIL |
| **Rack 05** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] PASS [ ] FAIL |
| **Rack 06** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] PASS [ ] FAIL |
| **Rack 07** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] PASS [ ] FAIL |
| **Rack 08** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] PASS [ ] FAIL |
| **Rack 09** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] PASS [ ] FAIL |
| **Rack 10** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] PASS [ ] FAIL |
| **ROW STATS**| **Mean Flow: _______ LPM** | **Std Dev (σ): _______** | **CV ($\frac{\sigma}{\mu}\times 100\%$): _______ %** | Limit: ≤ 5.0% | **PASS / FAIL** |

**SHEET 3 STEP VERDICT**: [ ] **THERMAL STEP ACCEPTED** [ ] **STEP FAILED / UNSTABLE** 
**Authorized Test Lead (Command Authority)**: ____________________ **Signature**: __________________ 
**Lead Electrical PE Signature**: ________________________ **Date**: __________________ 
**Lead Mechanical PE Signature**: ________________________ **Date**: __________________ 

---

## Sheet 4. Dynamic Transient Failure & Redundancy Ride-Through Log (Level 5 IST)

**Project Name**: __________________________ **Data Hall / Room ID**: __________________________ 
**CDU Asset Tag**: __________________________ **Base Load During Test**: 1200 kW (100% Design Load) 
**Test Lead Signature**: ____________________ **Controls PE Signature**: ________________________ 
**Facility Owner Witness**: ________________ **Date & Shift Timestamp**: ______________________ 

*The steady-state recovered curve is not the pass. Record pre-event baseline, peak transient deflection, and recovery duration.*

### Scenario 1: Secondary Pump Trip & Auto-Changeover (N+1 VFD Swap)
- Pre-Event Operating Pump: Pump P-1A (Speed: 50.0 Hz, Flow: 115.0 m³/h, dP: 220 kPa) 
- Simulated Trip Injection Method: Inverter digital fault trigger at timestamp: ____________________ 
- Standby Pump P-1B Auto-Start Detected: __________ ms (Limit: ≤ 500 ms) 
- Minimum Secondary dP Recorded: __________ kPa (Limit: ≥ 100.0 kPa; no cavitation) 
- Peak Water Hammer Pressure Surge: __________ kPa (Limit: ≤ ± 50.0 kPa) 
- Secondary Flow Restored to ≥ 95% Design: __________ s (Limit: ≤ 1.5 seconds) 
- Load-Bank Thermal Interlock Tripped?: **YES (FAIL) / NO (PASS)** 
- Scenario 1 Verdict: **PASS / FAIL** 

### Scenario 2: 2N Electrical Feeder A Loss / ATS Bus Transfer
- Feeder A Breaker Tripped at Timestamp: ____________________ 
- Bus Transfer Switch Transition Duration: __________ ms (Limit: ≤ 16.0 ms) 
- CDU 24V DC Control Bus Voltage Minimum: __________ V DC (Limit: ≥ 22.0 V DC; zero dip) 
- CDU PLC Controller Reboot Observed?: **YES (CRITICAL FAIL) / NO (PASS)** 
- Secondary Pump VFD Ride-Through / Recovery: __________ s (Limit: ≤ 3.0 s) 
- Feeder B Steady-State Voltage: __________ V Current: __________ A 
- Scenario 2 Verdict: **PASS / FAIL** 

### Scenario 3: Primary Chilled Water Interruption (Thermal Inertia Ride-Through)
- Primary FWS Isolation Valve Commanded Closed at Timestamp: ____________________ 
- Secondary Supply Temp Pre-Trip: 40.0 °C Load Maintained: 1200 kW 
- Rate of Secondary Temperature Rise: $\frac{dT}{dt} = \text{__________ K / s}$ 
- Buffer Time to High Temp Alarm (45.0°C): __________ s (Limit: t_buffer ≥ 40.0 s) 
- Automated Load Shed Initiated by CDU Alert?: **YES / NO** 
- Emergency Over-Temperature Trip Actuated (50.0°C): Timestamp: ____________________ 
- All Load-Bank Heaters De-Energized Instantly?: **YES / NO** (Peak fluid temp: ______ °C) 
- Scenario 3 Verdict: **PASS / FAIL** 

### Scenario 4: BMS Communication Severance (Autonomous Local Fail-Safe)
- Modbus-TCP / BACnet Ethernet Cable Disconnected at Timestamp: ____________________ 
- CDU Local PLC Switched to Autonomous Standalone Mode?: **YES / NO** 
- Secondary Pump Speed Oscillation / Hunting Observed?: **YES (FAIL) / NO (PASS)** 
- Modulating TCV-101 Valve Drift / Hunting Observed?: **YES (FAIL) / NO (PASS)** 
- Secondary Supply Temp Maintained at 40.0°C ± 0.5 K for 30 Minutes: **PASS / FAIL** 
- Scenario 4 Verdict: **PASS / FAIL** 

### Scenario 5: Rapid Thermal Step-Change Shock ($100% \to 30% \to 100%$)
- Step Down from 1200 kW to 360 kW at Timestamp: ____________________ 
 - Minimum Secondary Supply Temp Undershoot: __________ °C (Limit: ≥ 38.5°C) 
 - TCV-101 Response Stabilization Time: __________ s (Limit: ≤ 45 s) 
- Step Up from 360 kW to 1200 kW at Timestamp: ____________________ 
 - Maximum Secondary Supply Temp Overshoot: __________ °C (Limit: ≤ 41.5°C) 
 - Secondary Fluid Flow Maintained Stable ± 2.0%: **PASS / FAIL** 
- Scenario 5 Verdict: **PASS / FAIL** 

**SHEET 4 DYNAMIC VERDICT**: [ ] **ALL TRANSIENT TESTS PASSED** [ ] **TRANSIENT FAILURES LOGGED** 
**Lead Test Lead Signature**: ________________________ **Date**: __________________ 
**Facility Owner Witness**: ________________________ **Date**: __________________ 

---

## Sheet 5. Controlled De-Energization, Cooldown & Demobilization Protocol

**Project Name**: __________________________ **Data Hall / Room ID**: __________________________ 
**Test Unit Asset Tag**: ____________________ **Shift Date & Time**: ____________________________ 
**Test Lead (Directing Shutdown)**: ________ **Lead Electrical PE**: __________________________ 
**Lead Mechanical PE**: ____________________ **Safety Lead**: ________________________________ 

*Every shutdown step must be executed and ticked in strict chronological sequence. Reversing steps voids this sheet.*

### 1. Mandatory Sequential De-Energization Steps

- [ ] **STEP 01: Shed Active Thermal Load to 0 kW** 
 *Command all load-bank heater stages to 0 kW via controller. Verify all thyristor SCR firing pulses cease and magnetic contactors drop open. Active power verified 0.0 kW.* 
 Timestamp: ____________________ Initials: ________ 

- [ ] **STEP 02: Open & Lock Out Load-Bank Power Feeders (LOTO)** 
 *Open load-bank branch circuit breakers at the PDU or overhead tap box. Apply lockout padlocks and danger tags. Verify circuits are dead with calibrated voltage detector.* 
 Timestamp: ____________________ Initials: ________ 

- [ ] **STEP 03: 10-Minute Fluid Circulation Cooldown Soak** 
 *CRITICAL: Maintain CDU secondary pumps running at 50.0 Hz for minimum 10 minutes with heaters dead. This removes latent heat from heater sheaths and prevents localized fluid boiling.* 
 Start Time: ____________________ End Time: ____________________ (Secondary Fluid Temp: ______ °C) 
 Initials: ________ 

- [ ] **STEP 04: Controlled Power Down of CDU Secondary Pumps** 
 *Stop CDU secondary pumps only after fluid temperature drops below 30.0°C. Confirm differential pressure decays smoothly to 0.0 kPa.* 
 Timestamp: ____________________ Initials: ________ 

- [ ] **STEP 05: Isolate Secondary Manifolds & Disconnect Hoses** 
 *Close secondary supply and return manual isolation valves. Relieve residual static head pressure via bleed valves into catch buckets. Disconnect quick-disconnect couplings.* 
 *(CRITICAL: If this step was ticked prior to Step 04, this sheet is immediately VOID.)* 
 Timestamp: ____________________ Initials: ________ 

### 2. Cryptographic Data Archive Verification
- [ ] Raw 1-second load-bank CSV telemetry exported and verified: **YES / NO** 
- [ ] 1-second BMS / PLC trend logs exported across all test timestamps: **YES / NO** 
- [ ] High-resolution infrared thermography captures and digital photos archived: **YES / NO** 
- Primary Secure Storage Location: __________________________________________________ 
- Secondary Redundant Offline Location: ____________________________________________ 
- Master Archive SHA-256 Checksum: ________________________________________________ 

### 3. Demobilization Inventory & Facility Restoration
- [ ] All quick-disconnect couplings and hoses counted out against Sheet 1 inventory: **ZERO MISSING** 
- [ ] Pressure-rated protective dust caps installed on all manifold supply and return ports: **YES / NO** 
- [ ] Permanent facility valves, circuit breakers, and BMS setpoints restored to baseline: **YES / NO** 
- [ ] Data hall raised floor tiles, pedestal stringers, and cable trays inspected for cleanliness: **YES / NO** 

**SHEET 5 CLOSEOUT VERDICT**: [ ] **SHUTDOWN EXECUTED IN RIGOROUS COMPLIANCE** 
**Authorized Test Lead Signature**: ________________________ **Date**: __________________ 
**Lead Electrical PE Signature**: ________________________ **Date**: __________________ 

---

## Sheet 6. Cold No-Heat Baseline Pump & Loop Resistance Curve

**Project Name**: __________________________ **Data Hall / Room ID**: __________________________ 
**CDU Asset Tag**: __________________________ **Pump Tag (A/B)**: ______________________________ 
**Lead Mechanical PE**: ____________________ **Measurement Tech**: __________________________ 
**Secondary Fluid Chemistry**: 25.0% PG **Measured Fluid Temp**: __________ °C (Target: 20.0°C ± 1.0 K) 

*Heat command must be interlocked to 0 kW. VFD frequency must be locked in manual override at 50.0 Hz (or 60.0 Hz).*

### 1. Verification of Prerequisite Baseline Controls
- [ ] Electrical heaters verified locked out; active electrical load is 0.0 kW: **CONFIRMED** 
- [ ] Automatic VFD differential pressure modulation disabled: **MANUAL LOCKOUT CONFIRMED** 
- [ ] Operating VFD frequency fixed and verified via calibrated tachometer/register: **50.0 Hz** 
- [ ] Refractometer confirmed secondary glycol concentration: **25.0% ± 0.5% PG** 

### 2. Four-Point Valve Throttling Hydraulic Data

| THROTTLING STEP | VALVE COMMAND POSITION | MEASURED FLOW Q (m³/h) | MEASURED FLOW Q (LPM) | PUMP HEAD ΔP_pump (kPa) | MANIFOLD dP ΔP_man (kPa) | MOTOR CURRENT (A) | VFD POWER (kW) | CONTROL MODULATION OFF? |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Point 1: Max Flow** | 100% Fully Open | __________ m³/h | __________ LPM | ______ kPa | ______ kPa | ______ A | ______ kW | [ ] YES (Locked) |
| **Point 2: 80% Flow** | Throttled (~80%) | __________ m³/h | __________ LPM | ______ kPa | ______ kPa | ______ A | ______ kW | [ ] YES (Locked) |
| **Point 3: 60% Flow** | Throttled (~60%) | __________ m³/h | __________ LPM | ______ kPa | ______ kPa | ______ A | ______ kW | [ ] YES (Locked) |
| **Point 4: 40% Flow** | Throttled (~40%) | __________ m³/h | __________ LPM | ______ kPa | ______ kPa | ______ A | ______ kW | [ ] YES (Locked) |

### 3. Hydraulic Curve Acceptance Audit
- Vendor Certified Submittal Pump Curve Reference: Document ID: ____________________ Rev: ______ 
- Point 1 Head vs Flow Deviation from Certified Curve: __________ % (Limit: ≤ ± 5.0%) 
- Point 2 Head vs Flow Deviation from Certified Curve: __________ % (Limit: ≤ ± 5.0%) 
- Point 3 Head vs Flow Deviation from Certified Curve: __________ % (Limit: ≤ ± 5.0%) 
- Point 4 Head vs Flow Deviation from Certified Curve: __________ % (Limit: ≤ ± 5.0%) 
- Maximum Secondary Fluid Temperature Rise During Run: __________ K (Limit: ≤ 0.5 K) 

**SHEET 6 BASELINE VERDICT**: [ ] **COLD PUMP CURVE ACCEPTED & FILED** [ ] **CURVE OUT OF TOLERANCE** 
**Lead Mechanical PE Signature**: ________________________ **Date**: __________________ 
**Test Technician Signature**: ____________________________ **Date**: __________________ 

---

## Sheet 7. CDU Autonomous Control Logic & Supervisory Interface Audit

**Project Name**: __________________________ **Data Hall / Room ID**: __________________________ 
**CDU Asset Tag**: __________________________ **Vendor Logic Doc Ref**: __________________________ 
**Lead Controls PE**: ______________________ **Vendor Commissioning Engineer**: ________________ 

*Vendor control logic submittal must be attached to this sheet. If documentation is missing, mark NOT DEMONSTRATED.*

### 1. Autonomous Control Logic Failure Modes

| CONTROL SCENARIO | EXPECTED VENDOR LOGIC SPECIFICATION | PHYSICAL SIMULATION RESULT | AUDIT VERDICT |
| :--- | :--- | :--- | :--- |
| **Primary Control Temp Sensor Disconnected** | Controller detects open-circuit loop; generates critical alarm; rejects sensor and automatically reverts to redundant secondary immersion sensor. | Controller alarmed instantly; switched to TT-202; zero valve hunting observed. | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Primary Differential P Sensor Line Severed**| Controller flags transmitter signal loss (4-20mA out of range); locks VFD at last stable frequency; prevents pump runout. | Alarm annunciated; VFD maintained 48.2 Hz stable; differential pressure held. | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Operating PLC Controller Power Severed** | System enters hardware fail-safe: primary modulating valve fails 100% open; running secondary pump continues at max line frequency.| TCV spring-returned to 100% open; pump continued circulating; no thermal trip. | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Pump VFD Internal Inverter Overload Fault**| Inverter output trips; auxiliary contact signals CDU PLC; standby pump starts and achieves pressure within ≤ 1.5 s. | Standby pump P-1B started in 1.1s; loop pressure held ≥ 120 kPa. | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Modbus-RTU Drive Comm Cable Severed** | Drive loses serial communication heartbeat; holds last commanded speed; CDU logs comms loss alarm without stopping loop. | Drive maintained 50.0 Hz; comm alarm logged on HMI; fluid flow continued. | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Group-Control Master Network Severed** | Unit detects loss of group master token; autonomous local controller assumes standalone PID loop tracking seamlessly. | Unit transitioned to local mode in 800ms; secondary supply T maintained 40.0°C. | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Electric Actuator 24V Power Loss** | Actuator internal spring-return or supercapacitor drives valve mechanism to 100% full-open position. | Valve driven mechanically to 100% open; maximum primary chilled water available. | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Expansion Tank High-Pressure Relief Trip**| Relief valve opens at 6.0 bar; high-pressure switch trips; CDU stops makeup pump and sends high-priority alarm. | Switch tripped at 5.8 bar; makeup pump locked out; alarm received by BMS. | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |

### 2. Ring Header Sectional Isolation (Only if Secondary is Ring Topology)
- [ ] Nearest secondary branch isolation valve closed and reopened: 
 *Load-bank thermal stability maintained: **YES / NO** CDU supply pressure stable: **YES / NO*** 
- [ ] Farthest secondary branch isolation valve closed and reopened: 
 *Load-bank thermal stability maintained: **YES / NO** CDU supply pressure stable: **YES / NO*** 

### 3. Supervisory BMS Telemetry Register Consistency Audit

| TELEMETRY PARAMETER | BMS POINT TAG | CDU LOCAL DISPLAY | CALIBRATED FIELD REF | TELEMETRY DISCREPANCY | AUDIT LIMIT | VERDICT |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Secondary Supply T** | `CDU01_TCS_SUP_T` | 40.10 °C | 40.08 °C | 0.02 K | ≤ ± 0.30 K | **PASS / FAIL** |
| **Secondary Return T** | `CDU01_TCS_RET_T` | 50.15 °C | 50.12 °C | 0.03 K | ≤ ± 0.30 K | **PASS / FAIL** |
| **Secondary Flow Rate** | `CDU01_TCS_FLOW` | 115.8 m³/h | 116.1 m³/h | 0.26 % | ≤ ± 2.0% | **PASS / FAIL** |
| **Secondary Supply P** | `CDU01_TCS_SUP_P` | 282.0 kPa | 280.5 kPa | 1.5 kPa | ≤ ± 10.0 kPa| **PASS / FAIL** |
| **Primary TCV Position**| `CDU01_TCV_POS` | 64.0 % | 64.5 % (Stroked) | 0.5 % | ≤ ± 2.0% | **PASS / FAIL** |

**SHEET 7 LOGIC VERDICT**: [ ] **CDU AUTONOMOUS LOGIC CERTIFIED** [ ] **LOGIC DEFICIENCIES NOTED** 
**Lead Controls PE Signature**: ________________________ **Date**: __________________ 
**Vendor Commissioning Engineer**: ____________________ **Date**: __________________ 
