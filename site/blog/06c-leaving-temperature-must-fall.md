---
title: "Leaving water should fall as the fan speeds up"
description: "Enforcing physical monotonicity constraints ($\partial T_{\text{leave}} / \partial N_{\text{fan}} \le 0$) on data center cooling tower models so collinear data cannot invert fan control."
slug: leaving-temperature-must-fall
book: "When a Monitor May Speak"
book_number: 6
primary_keyword: "cooling tower Merkel equation monotonic constraint"
secondary_keywords: ["cooling tower Merkel equation monotonic constraint protocol", "data center cooling constraint audit", "when a monitor may speak field guide", "mission critical facility commissioning standard"]
schema_type: "TechArticle"
publish_date: "2026-10-16"
---

# Leaving water should fall as the fan speeds up

> **Direct Answer Block**: Enforcing physical monotonicity constraints ($\partial T_{\text{leave}} / \partial N_{\text{fan}} \le 0$) on data center cooling tower models so collinear data cannot invert fan control. In mission-critical data center commissioning and operations, engineers enforce this boundary using deterministic physical equations, calibrated field instrumentation, and auditable sign-off gates rather than relying on vendor brochure summaries, uncalibrated software plots, or verbal assurances. Every measurement and state transition must be recorded with synchronized UTC timestamps and explicit pass/fail thresholds before a signature is granted.

![The leaving temperature must not rise with fan speed.](figures/flagship/fig-04-alarm-storm-suppression-and-topology.png)

Before a search is allowed to propose a fan speed, the fit has to obey the machine. More air across the fill should not make the leaving water warmer, all else held. If your predicted leaving temperature rises as fan speed rises, the prediction is wrong. Do not ask which speed minimizes power on a curve that has the physics backwards.

This check is not a tuned coefficient. It is a sign. Hold the conditions you are not allowed to move. Step the fan handle across speeds the archive actually contains. Read the predicted leaving temperature. It should not climb. If it climbs, stop. The fault may be the fit, a swapped sensor, a tower that is not the tower you named, or hours you failed to mark as off. Find which. Do not paper over it with a second model that is smoother.

A neural net is not excused. A line is not excused. If the flexible model can memorize a backwards tower, it will. The sign check is how you notice. A model that passes the sign check on the speeds you saw has still not earned the speeds you did not see.

Do not publish the curve, the site, or the kilowatts. The decision is the sign. Wrong sign, no search, no setpoint, no sentence about savings.

---

## 1. First-Principles Engineering Formulation and Governing Mathematics

In high-density data center environments, verbal summaries and qualitative status tiles routinely obscure incipient physical failures. Whether auditing a $120\,\text{kW}$ liquid-cooled rack boundary, evaluating a 1-second telemetry time series, or verifying plant redundancy prior to handover, the governing physical relationship for this protocol is expressed as:

$$\frac{\partial T_{\text{water, out}}}{\partial N_{\text{fan}}} \le 0, \qquad \frac{K a V}{L} = \int_{T_{\text{out}}}^{T_{\text{in}}} \frac{c_{p,w} \, dT}{h_s(T) - h_{\text{air}}}$$

When any term on the left-hand or right-hand side of this relationship is left unmeasured, inferred from an uncalibrated nameplate, or averaged across an unverified time window, the resulting engineering record cannot support a valid operational signature. Field engineers must verify each physical variable independently using NIST/ISO 17025 traceable instruments before proceeding to the next gate in the sequence.

| Audit Verification Parameter | Unacceptable / Defective Field Practice | Auditable First-Principles Requirement | Mandatory Action on Failure |
| :--- | :--- | :--- | :--- |
| **Primary Boundary Definition** | Implied by vendor brochure or slide deck | Explicitly bounded on stamped P&ID / SLD with tag IDs | Halt acceptance; issue formal boundary clarification |
| **Measurement & Telemetry Proof** | Single uncalibrated display reading or 60-sec average | Calibrated Class A/0.5S sensor with 1-sec UTC timestamp | Reject dataset; classify point as `0x40` Stale or `0x80` Bad |
| **Pass / Fail Acceptance Gate** | Qualitative "Looks OK" or "Within Normal Range" | Quantitative numerical corridor cited from revision in force | Log Category A/B defect; withhold retainage or permit |
| **Custody & Sign-Off Record** | Single bundled "Accepted" signature at end of meeting | Scoped, dated sentence naming exact proved & unproved lines | Strike unsupported claims; issue Conditional Refusal |

---

## 2. Deep-Dive Technical Protocol and Field Implementation

The following field protocol—adapted directly from **Volume 06: *When a Monitor May Speak***—establishes the step-by-step verification mechanics required on the data hall floor:

A telemetry engineer who believes that software monitoring rules apply only to cloud servers and database clusters while mechanical chillers and electrical switchgear operate under "facilities folklore" does not understand critical infrastructure.

The physical plant—the medium-voltage transformers, centrifugal chillers, secondary cooling distribution units (CDUs), and air handling units—is governed by identical telemetry laws:
- A pressure transducer requires an audited quality bitmask.
- A water temperature sensor requires deadband hysteresis and continuous dwell filtering.
- A chiller electrical trip requires microsecond time synchronization.
- A pump room alarm storm requires topological dependency masking.

**FACILITY TELEMETRY GOVERNANCE MATRIX**

| Subsystem / Instrument S | tandard Telemetry Parameter G | overning Code |
| :--- | :--- | :--- |
| MV Switchgear (35kV) Bus | Voltage, Current, THD, PF GB | /T 51409-2020 |
| Dry-Type Transformers Wi | nding Temperature (< 90°C) IE | EE C57.12 / NFPA |
| UPS Battery Rooms DC Flo | at Voltage, Ambient T IEEE 11 | 88 / 1491 |
| Centrifugal Chillers Con | denser Approach (<= 1.5K) ASH | RAE Standard 90.4 |
| Secondary CDU Loops Pres | sure (0.15 - 0.90 MPa) OpenVi | king 2.6XZ10 |
| Secondary Coolant Chem 2 | 5.0% Propylene Glycol wt ASTM | D3306 / D1384 |
| IT Whitespace Aisles Con | tainment DP (>= 5.0 Pa) ASHRA | E TC 9.9 |

Following the authoritative engineering standards outlined in **GB/T 51409-2020** (*Technical Standard for Integrated Monitoring System of Data Centers*) and OpenViking operational guidelines (`DCFG-SOP-WHITESPACE-01` and `DCFG-SOP-LIQUID-01`), every physical facility point must be operated under rigorous engineering constraints.

## The Walked Reading Wins

The physical measurement taken by a qualified technician using a calibrated, certified hand-held instrument **always supersedes the digital telemetry tile on the SCADA screen**.

If the central BMS workstation reports that the secondary cooling loop supply temperature is operating comfortably at 28.0°C (`GREEN`), but the shift technician walks the room with a calibrated PT100 immersion probe or calibrated infrared camera and measures 34.2°C:
1. **The physical reading wins instantly**. The facility is operating in a high-temperature excursion state.
2. The technician does not average the two numbers and assume the temperature is 31.1°C.
3. The technician logs both readings into the shift register with exact timestamps:
 `08:15 UTC: SCADA reports 28.0°C | Fluke Calibrated Probe reads 34.2°C`.
4. The digital telemetry point is immediately quarantined: its quality flag is set to `UNCERTAIN (0x02)` or `BAD (0x04)`.
5. The digital sensor is subjected to an immediate physical loop calibration and forced-failure test.

Never permit a software engineer or remote monitoring specialist to argue that *"the digital sensor must be right because it was installed by the factory."* Sensors drift, thermal wells accumulate air gaps, RTD lead resistance degrades, and analog-to-digital converters lose calibration. The verified tool in the technician's hand is the ultimate anchor of truth.

## Critical Facility Telemetry Parameters

Per OpenViking `DCFG-SOP-LIQUID-01` for high-density liquid cooling infrastructure:

### 1. The CDU Pressure Envelope
- Primary Facility Water System (FWS) supply pressure: 0.15 MPa to 0.90 MPa.
- Secondary Technology Cooling System (TCS) supply pressure: 0.15 MPa to 0.90 MPa.
- Secondary loop pump differential pressure (ΔP_pump): Strictly < 1.0 bar. A differential pressure > 1.0 bar indicates severe piping blockage, a clogged 50-micron filter element, or an accidentally closed manifold isolation valve.
- Any drop in secondary static pressure below 0.12 MPa triggers an immediate **Low Pressure Alarm**, indicating coolant leakage or thermal expansion tank bladder failure.

### 2. Plate Heat Exchanger Thermal Approach
The approach temperature across the CDU plate heat exchanger:

$$\Delta T_{\text{approach}} = T_{\text{TCS, supply}} - T_{\text{FWS, supply}} \le 8.0\,\text{K}$$

During steady-state operation, ΔT_approach must remain strictly ≤ 8.0 K (typically 3.0 K to 5.0 K). If the approach temperature creeps above 8.0 K under constant heat load, the heat exchanger plates are suffering from biological slime, mineral scaling, or particulate fouling, requiring chemical clean-in-place (CIP) flushing.

### 3. Propylene Glycol Concentration & Refractometer Testing
Per ASTM D3306 and OpenViking standards, secondary coolant must be maintained at **25.0% propylene glycol by weight** (± 1.0%):
- Freeze protection: -11.5°C.
- Burst protection: -22.0°C.
- Specific gravity: 1.026 ± 0.003 at 20°C.
- Coolant conductivity: < 10 μS/cm.
- Coolant pH: 7.5 to 9.0.

If a refractometer test reveals PG concentration < 23.0%, the fluid loses biostatic efficacy, permitting bacterial colonies to form biofilms on micro-channel cold plates. If PG concentration exceeds 27.0%, dynamic fluid viscosity increases drastically ($\nu > 2.8\,\text{mm}^2/\text{s}$), spiking pumping power and reducing turbulent heat transfer.

## Electrical Power Quality Telemetry

Per GB/T 51409-2020 and IEEE 1159:
- **Voltage Tolerance**: ± 5.0% of nominal rated voltage at utilization panels.
- **Frequency Stability**: 50 ± 0.2 Hz (or 60 ± 0.2 Hz). A frequency excursion > 0.5 Hz indicates catastrophic grid instability requiring immediate transition to isolated diesel generation.
- **Power Factor**: Maintained ≥ 0.95 lagging across all active operating loads.
- **Total Harmonic Distortion (THD)**: Voltage THD ≤ 5.0%; individual harmonic voltage distortion ≤ 3.0%.

If electrical power monitoring telemetry detects current harmonic resonance, switchgear busbars will experience severe inductive heating, leading to catastrophic bus duct insulation breakdown even when overall kilowatt load is well below nameplate rating.

## Decisions to Record

- The physical calibration registry of all hand-held test instruments used during shift rounds.
- The exact CDU operating pressures, pump differential pressures, and thermal approach temperatures logged per shift.
- The weekly optical refractometer, conductivity, and pH measurements logged for secondary cooling loops.
- The protocol establishing that walked physical measurements unconditionally override digital SCADA screens.

---

## 3. Field Verification Checklist and Instrumentation Hygiene

To execute this protocol without introducing measurement bias or scope ambiguity, the responsible engineer enforces four mandatory field rules:
1. **Instrument Traceability Before Observation**: Verify that every thermometer (4-wire Pt100 RTD Class A), pressure transducer ($\le \pm 0.1\%$ span), flowmeter, balometer, or power analyzer carries a current calibration certificate and passes a pre-test zero/span check on the day of the walk.
2. **Synchronized Time-Series Capture**: Align all digital loggers and gateway pollers to a single UTC reference clock (via IEEE 1588v2 PTP at $\pm 1\,\text{ms}$ for electrical Sequence of Events, or NTP at $\pm 10\,\text{ms}$ for thermal/hydraulic dwells). Never merge unsynchronized CSV files by row index.
3. **Explicit Isolation of Disturbances vs. Control Handles**: Hold upstream supply temperatures, parallel cabinet loads, and containment door states constant during the observation dwell so that transient plant drift is never mistaken for steady-state equipment performance.
4. **Written Record Prior to Signature**: Record every boundary tag, measured value, uncertainty tolerance, and open limitation in ink on the controlled project sheet before leaving the equipment line-up.

---

## Frequently Asked Questions (FAQ)

### Why does "Leaving water should fall as the fan speeds up" matter during high-density data center commissioning and operations?
Enforcing physical monotonicity constraints ($\partial T_{\text{leave}} / \partial N_{\text{fan}} \le 0$) on data center cooling tower models so collinear data cannot invert fan control. When project teams bypass this rule to meet a commercial schedule milestone, unverified physical assumptions—such as hidden hydraulic pressure drops, unlogged polling gaps, unblanked bypass leakage, or uncalibrated sensor offsets—transfer directly into live 24/7 production as latent single points of failure.

### How do you quantitatively verify compliance with "cooling tower Merkel equation monotonic constraint" on the physical floor?
Compliance is verified by executing the governing mathematical balance ($$\frac{\partial T_{\text{water, out}}}{\partial N_{\text{fan}}} \le 0, \qquad \frac{K a V}{L} = \int_{T_{\text{out}}}^{T_{\text{in}}} \frac{c_{p,w} \, dT}{h_s(T) - h_{\text{air}}}$$) using independent, calibrated field instruments across a stabilized steady-state dwell window (minimum 15 to 30 minutes for thermal and hydraulic systems), and confirming that the discrepancy between primary and secondary measurements remains strictly within the pre-declared acceptance band.

### What should an engineer do if a contractor or vendor submits a report that violates this protocol?
The reviewing engineer must refuse to sign the broad acceptance sentence, mark the specific line item as **Unproved / Defective** on the official audit sheet, and either require a witnessed re-test under a corrected script or isolate the unproved scope under a time-bounded Conditional Acceptance with a $150\%$ to $200\%$ financial retainage escrow holdback.

---

From *When a Monitor May Speak*, Tristan, Data Center Field Guides.

Related: [Fixed inputs are not fan handles](06c-fixed-and-adjustable.md).
