# 6. The two sheets

Copy these master audit sheets into your project commissioning binder. Sheet 1 governs the physical field measurement protocol on the data hall floor; Sheet 2 governs the technical deconstruction of the CFD simulation report at your desk.

Fill every cell in ink. A blank cell is an automated stop. An unverified temperature copied from memory is a defect.

---

## Sheet 1. Physical Field Measurement & Model Calibration Log

**Project Name**: __________________________ **Data Hall / Room ID**: __________________________ 
**Physical Measurement Date**: ____________ **Model CAD Freeze Date**: ________________________ 
*(If measurement date and CAD freeze date differ, state which layout temperatures belong to: __________________)* 
**Lead Mechanical Auditor**: ________________ **Measurement Technician**: ______________________ 
**Calibrated Thermometer Model & S/N**: ____________________ **Calibration Expiry**: ____________ 

### 1. Cooling Unit (CRAH / In-Row / Fan Wall) Face Measurements
*Supply opening must average at least two points at the discharge face. Return opening must average at least three points across the intake face. Never measure in the aisle.*

| UNIT ASSET TAG | SUPPLY DISCHARGE S1 (°C) | SUPPLY DISCHARGE S2 (°C) | SUPPLY AVERAGE S_AVG (°C) | AT OPENING? (Y/N) | RETURN INTAKE R1 (°C) | RETURN INTAKE R2 (°C) | RETURN INTAKE R3 (°C) | RETURN AVERAGE R_AVG (°C) | AT OPENING? (Y/N) | OPERATING FAN SPEED (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **CRAH-01** | ______ °C | ______ °C | ______ °C | [ ] Y [ ] N | ______ °C | ______ °C | ______ °C | ______ °C | [ ] Y [ ] N | ______ % |
| **CRAH-02** | ______ °C | ______ °C | ______ °C | [ ] Y [ ] N | ______ °C | ______ °C | ______ °C | ______ °C | [ ] Y [ ] N | ______ % |
| **CRAH-03** | ______ °C | ______ °C | ______ °C | [ ] Y [ ] N | ______ °C | ______ °C | ______ °C | ______ °C | [ ] Y [ ] N | ______ % |
| **CRAH-04** | ______ °C | ______ °C | ______ °C | [ ] Y [ ] N | ______ °C | ______ °C | ______ °C | ______ °C | [ ] Y [ ] N | ______ % |
| **CRAH-05** | ______ °C | ______ °C | ______ °C | [ ] Y [ ] N | ______ °C | ______ °C | ______ °C | ______ °C | [ ] Y [ ] N | ______ % |
| **CRAH-06** | ______ °C | ______ °C | ______ °C | [ ] Y [ ] N | ______ °C | ______ °C | ______ °C | ______ °C | [ ] Y [ ] N | ______ % |

### 2. Cabinet Intake & Exhaust Temperature Trees
*Measure vertical elevations at intake front door: T1 (0.3m / ~U06), T2 (1.2m / ~U24), T3 (1.8m / ~U42). Active power must be sourced from PDU smart meters, never nameplate ratings.*

| CABINET / RACK ID | ACTIVE PDU POWER (kW) | INTAKE T1 BOT 0.3m (°C) | INTAKE T2 MID 1.2m (°C) | INTAKE T3 TOP 1.8m (°C) | EXHAUST REAR T_EXH (°C) | DELTA-T T_EXH - T2 (K) | IN NUMERICAL MODEL? (Y/N) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Rack 01** | ______ kW | ______ °C | ______ °C | ______ °C | ______ °C | ______ K | [ ] Y [ ] N |
| **Rack 02** | ______ kW | ______ °C | ______ °C | ______ °C | ______ °C | ______ K | [ ] Y [ ] N |
| **Rack 03** | ______ kW | ______ °C | ______ °C | ______ °C | ______ °C | ______ K | [ ] Y [ ] N |
| **Rack 04** | ______ kW | ______ °C | ______ °C | ______ °C | ______ °C | ______ K | [ ] Y [ ] N |
| **Rack 05** | ______ kW | ______ °C | ______ °C | ______ °C | ______ °C | ______ K | [ ] Y [ ] N |
| **Rack 06** | ______ kW | ______ °C | ______ °C | ______ °C | ______ °C | ______ K | [ ] Y [ ] N |
| **Rack 07** | ______ kW | ______ °C | ______ °C | ______ °C | ______ °C | ______ K | [ ] Y [ ] N |
| **Rack 08** | ______ kW | ______ °C | ______ °C | ______ °C | ______ °C | ______ K | [ ] Y [ ] N |
| **Rack 09** | ______ kW | ______ °C | ______ °C | ______ °C | ______ °C | ______ K | [ ] Y [ ] N |
| **Rack 10** | ______ kW | ______ °C | ______ °C | ______ °C | ______ °C | ______ K | [ ] Y [ ] N |

### 3. Model Calibration Parameters (Physical Inputs Altered)
*Document only physical inputs you can physically touch in the room. Arbitrary mathematical multipliers are strictly prohibited.*

| ITERATION | PHYSICAL INPUT ALTERED IN MODEL | PHYSICAL ROOM LOCATION | INITIAL ASSUMPTION | CORRECTED PHYSICAL INPUT | RERUN PERFORMED? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Pass 1** | e.g. Missing 1U blanking panel added | Rack 04, slots U21-U22 | Solid sealed face | Open 25 L/s recirculation | [ ] YES [ ] NO |
| **Pass 2** | e.g. Floor tile cable cutout unsealed | Beneath PDU 02 | Sealed grommet | 200x200mm open orifice | [ ] YES [ ] NO |
| **Pass 3** | e.g. CRAH-03 supply temp updated | Discharge face | 18.0°C (Brochure) | 20.4°C (Calibrated Field Ref)| [ ] YES [ ] NO |

### 4. Statistical Validation Error Gates (ASME V&V 20 Standards)
- Number of Sampled Benchmarking Probes (N): __________ (Minimum requirement: N ≥ 12) 
- **Mean Absolute Error (MAE)**: MAE = __________ K (Acceptance Limit: ≤ 1.0 K) — **PASS / FAIL** 
- **Root Mean Square Error (RMSE)**: RMSE = __________ K (Acceptance Limit: ≤ 1.5 K) — **PASS / FAIL** 
- **Normalised Mean Bias Error (NMBE)**: NMBE = __________ % (Acceptance Limit: |NMBE| ≤ 5.0%) — **PASS / FAIL** 
- **Maximum Localized Outlier ($Δ_\max$)**: $Δ_\max = __________ K$ (Acceptance Limit: ≤ 2.5 K) — **PASS / FAIL** 

**SHEET 1 CALIBRATION VERDICT**: 
[ ] **MODEL FULLY CALIBRATED AGAINST PHYSICAL DATA HALL** 
[ ] **MODEL NOT CALIBRATED (EXCEEDS STATISTICAL ERROR LIMITS — REPORT CANNOT SPEAK FOR THIS ROOM)** 
**Lead Mechanical Auditor Signature**: ________________________ **Date**: __________________ 

---

## Sheet 2. CFD Report Audit & Decision Gate Sheet

**Project Name**: __________________________ **Data Hall / Room ID**: __________________________ 
**CFD Consultant Firm**: ____________________ **Report Document ID & Rev**: ____________________ 
**Auditing Commissioning Lead**: ____________ **Date of Audit**: ________________________________ 

### 1. Purpose & Single Authorized Decision Domain
- Exact Statement of Purpose (copied verbatim from report): 
 *"____________________________________________________________________________________________"* 
 *(If purpose is absent or vague, write "PURPOSE NOT STATED" and halt review.)* 
- **Single Authorized Decision Domain (Select exactly ONE; mark other three N/A)**: 
 - [ ] **Domain 1**: Pre-Construction Design Comparison (Option A vs Option B) 
 - [ ] **Domain 2**: As-Built Hall Compliance Evaluation (Requires Sheet 1 Calibration) 
 - [ ] **Domain 3**: Operational Hotspot Root-Cause Analysis (Requires touchable input) 
 - [ ] **Domain 4**: N-1 Emergency Failure Ride-Through (Requires transient time-stepping) 

### 2. Audit of Six Mandatory Input Blocks
- [ ] **Block 1: Whitespace Geometry**: Slab height, floor void depth (H_void), and partitions documented: **YES / NO** 
- [ ] **Block 2: IT Equipment Specifications**: Server form factors, fan P-Q curves, and active PDU kW documented: **YES / NO** 
- [ ] **Block 3: Mechanical Cooling Equipment**: Discharge dimensions, fan curves, and supply setpoints documented: **YES / NO** 
- [ ] **Block 4: Airflow Obstacles & Leakage**: Cable trays, underfloor piping, and containment leakage modeled: **YES / NO** 
- [ ] **Block 5: Discretization & Mesh Independence**: Grid Convergence Index (GCI) verified; total cell count: ______ : **YES / NO** 
- [ ] **Block 6: Solver Convergence Records**: Navier-Stokes turbulence model stated (k-ε / k-ω): **YES / NO** 

### 3. Solver Mathematical Convergence Verification
- Continuity & Momentum Residuals Final Decayed Value: __________ (Limit: < 10^{-4}) — **PASS / FAIL** 
- Energy / Enthalpy Residual Final Decayed Value: __________ (Limit: < 10^{-6}) — **PASS / FAIL** 
- Global Mass Imbalance: $\left|\frac{\sum \dot{m}_{\text{in}} - \sum \dot{m}_{\text{out}}}{\sum \dot{m}_{\text{in}}}\right| \times 100\% = \text{__________ \%}$ (Limit: ≤ 0.10%) — **PASS / FAIL** 
- Point Temperature Monitors: Convergence history shows flat steady-state lines: **YES / NO** 

### 4. Cutting Plane & Color Scale Normalization Audit
- [ ] Every temperature contour plot names its cutting plane coordinate (e.g., Z = 1.2 m or Centerline Row 2): **YES / NO** 
- [ ] Comparative color scales normalized to standard fixed temperature range (15.0°C to 35.0°C): **YES / NO** 
 *(If color scales are arbitrary or shifting between options, set plots aside as decorative posters.)* 

### 5. Dimensionless Indices & ASHRAE TC 9.9 Compliance
- Supply Heat Index across monitored cabinets: SHI = __________ (Acceptance Limit: ≤ 0.15) — **PASS / FAIL** 
- Return Heat Index across monitored cooling units: RHI = __________ (Target: ≥ 0.85) — **PASS / FAIL** 
- Cold Aisle Capture Index: CI = __________ % (Acceptance Limit: ≥ 90.0%) — **PASS / FAIL** 
- **ASHRAE Class A1 Compliance**: 
 - Peak Cabinet Intake Temperature: __________ °C (Limit: Recommended ≤ 27.0°C; Allowable ≤ 32.0°C) 
 - Minimum Cabinet Intake Temperature: __________ °C (Limit: Recommended ≥ 18.0°C; Allowable ≥ 15.0°C) 
 - High-Temperature Compliance: RCI_HI = __________ % (Target: ≥ 95.0%) — **PASS / FAIL** 
 - Low-Temperature Compliance: RCI_LO = __________ % (Target: ≥ 95.0%) — **PASS / FAIL** 

### 6. Hybrid Liquid/Air Convection Verification (If Liquid Racks Present)
- [ ] Liquid rack model explicitly assigns ≈ 20% convective heat release to whitespace air: **YES / NO / N/A** 
 *(If liquid racks are modeled as 100% liquid-cooled with zero air heat, reject the report immediately.)* 
- [ ] Book 03 Liquid Load-Bank Verification Sheet attached: **YES / NO / OUT OF SCOPE** 

### 7. Speculative Sentence Refusal Log
*List all sentences in the draft report that were formally struck by the auditor:* 
1. Struck: *"________________________________________________________________________________"* 
2. Struck: *"________________________________________________________________________________"* 
3. Struck: *"________________________________________________________________________________"* 
- Proposed Physical Remedies Accompanied by Formal Rerun Scripts?: **YES / NO (MARKED UNVERIFIED)** 

**SHEET 2 REPORT AUDIT VERDICT**: 
[ ] **CFD REPORT ACCEPTED TO SUPPORT THE SINGLE STATED DECISION** 
[ ] **CFD REPORT REJECTED (DEFECTIVE INPUTS / FAILED CONVERGENCE / UNCALIBRATED)** 
**Auditing Commissioning Lead Signature**: ________________________ **Date**: __________________ 
**Facility Owner Representative Signature**: ____________________ **Date**: __________________

## Worked Numerical Example: Completing Sheet 1 and Sheet 2 on a Hybrid Hall

To illustrate how Sheet 1 (Field Benchmarking & Model Calibration) and Sheet 2 (Comparative Remedy Selection) govern an actual engineering decision, consider a commissioning audit of **Hall B, Row 04** containing ten high-density hybrid racks (`R04-01` through `R04-10`, each drawing $120.0\,\text{kW}$ total PDU power with $98.4\,\text{kW}$ captured by the PG25 liquid loop and $21.6\,\text{kW}$ rejected to the air stream) flanked by two enterprise network cabinets (`R04-11` and `R04-12`, $12.0\,\text{kW}$ air-cooled).

### Step 1: Auditing the Uncalibrated Baseline Submission

The contractor initially submits a baseline CFD report claiming all twelve cabinets pass ASHRAE Class A1 ($T_{\text{inlet}} \le 27.0^\circ\text{C}$), with a predicted maximum intake temperature of $25.4^\circ\text{C}$ at `R04-12` ($1.8\,\text{m}$). However, when the commissioning engineer executes the Sheet 1 physical walk with a calibrated 3-tier Pt100 tree and backpressure-compensated balometer:
- Physical temperature at `R04-12` ($1.8\,\text{m}$) reads **$30.8^\circ\text{C}$** (a $+5.4\,\text{K}$ calibration error, violating both the $27.0^\circ\text{C}$ ASHRAE threshold and the $\pm 1.5\,\text{K}$ model calibration gate).
- Balometer readings on tiles `T04-11` and `T04-12` read **$410\,\text{CFM}$** against the model's idealized **$820\,\text{CFM}$**, caused by a $400\,\text{mm}$ chilled-water header pipe obstructing the underfloor plenum directly beneath the end of Row 04 and twelve unblanked 1U slots in `R04-11`.

$$\Delta T_{\text{error, R04-12}} = |25.4^\circ\text{C} - 30.8^\circ\text{C}| = 5.4\,\text{K} > 1.5\,\text{K} \implies \mathbf{\text{SHEET 1 STATUS: REFUSED}}$$

### Step 2: Physical Boundary Correction and Remedy Ranking on Sheet 2

The modeler adds the physical $400\,\text{mm}$ underfloor pipe obstruction, sets the measured $12 \times 1\text{U}$ unblanked slot orifice area ($A_{\text{leak}} = 0.025\,\text{m}^2$), and re-runs the baseline. The calibrated model now predicts $30.4^\circ\text{C}$ at `R04-12` ($1.8\,\text{m}$), achieving $\text{MAE}_T = 0.72\,\text{K}$ and $\text{RMSE}_T = 0.94\,\text{K}$ across all 36 rack sensors (**Sheet 1 Status: CALIBRATED**).

Three physical remedies are then simulated on the calibrated model and recorded on Sheet 2:

| Candidate Remedy ID | Physical Modification Modeled | Simulated `R04-12` ($1.8\,\text{m}$) | Simulated Row $\text{SHI}$ | CRAH Fan Power Delta | Sheet 2 Audit Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Calibrated Baseline** | As-walked hall (unblanked 12U + pipe blockage) | $30.4^\circ\text{C}$ (Meas: $30.8^\circ\text{C}$) | $0.29$ (Fail) | $0.0\,\text{kW}$ (Baseline) | **Fails ASHRAE $27.0^\circ\text{C}$** |
| **Remedy Option A** | Increase CRAH-03 & CRAH-04 fan speed $75\% \to 95\%$ | $27.9^\circ\text{C}$ | $0.26$ (Fail) | $+18.4\,\text{kW}$ continuous | **Rejected** (Still $>27^\circ\text{C}$, high kW) |
| **Remedy Option B** | Install 12U blanking panels + seal rear cable cutouts | $26.8^\circ\text{C}$ | $0.14$ (Pass) | $0.0\,\text{kW}$ | **Partial Pass** (Margin only $0.2\,\text{K}$) |
| **Remedy Option C** | **Option B + swap `T04-11`/`12` to $50\%$ high-flow grates** | **$24.1^\circ\text{C}$** | **$0.09$ (Pass)** | **$0.0\,\text{kW}$** | **Selected for Physical Trial** |

Following physical installation of Remedy Option C, the mandatory post-change walk records **$24.3^\circ\text{C}$** at `R04-12` ($1.8\,\text{m}$) and **$790\,\text{CFM}$** on the swapped grates, closing Sheet 2 with empirical field proof.

## Mandatory Sign-Off Block and Calibration Instrument Traceability Log

Every completed Sheet 1 and Sheet 2 package filed in the facility engineering archive must attach the **Instrument Traceability Table** listing the serial number, NIST/ISO 17025 calibration certificate ID, calibration due date, and pre-walk ice-bath / zero-pressure offset check for every RTD probe, balometer hood, micro-manometer, and clamp meter used during the walk. A sheet bearing temperatures without instrument serial numbers is treated as an unverified estimate and refused at handover.

| Instrument Asset Tag | Instrument Type & Make/Model | Calibration Cert ID & Expiry | Pre-Walk Zero / Reference Check | Assigned Survey Team Member |
| :--- | :--- | :--- | :--- | :--- |
| `MET-RTD-01..06` | 4-Wire Pt100 Class A Vertical Tree | ISO-17025 Cert `#88412` (Valid) | Ice-bath $0.00^\circ\text{C} \pm 0.04\,\text{K}$ verified | Lead Thermal Commissioning Tech |
| `MET-BAL-02` | Powered Backpressure-Compensated Balometer | NIST Traceable `#44109` (Valid) | Sealed zero-flow offset $= 0.0\,\text{CFM}$ | Pneumatic Balance Engineer |
| `MET-MAN-04` | Digital Micro-Manometer ($0\text{--}250\,\text{Pa}$) | ISO-17025 Cert `#91023` (Valid) | Loop-shorted zero $= 0.00\,\text{Pa}$ | Pneumatic Balance Engineer |
| `MET-EPMS-A/B` | Revenue-Grade Rack PDU Branch Meters | IEC 62053-22 Class 0.5S | Cross-checked vs Fluke 435-II analyzer | Electrical Commissioning Lead |
