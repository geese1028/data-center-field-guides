# 0. How to use this book

This book has two explicit engineering jobs:
1. **Benchmark the Physical Room**: Establish a disciplined, multi-point field measurement protocol so that a numerical fluid dynamics simulation can be calibrated against physical reality rather than artistic intuition.
2. **Audit the Simulation Report**: Use the resulting computational fluid dynamics (CFD) report to make exactly one verified engineering decision, while formally refusing the speculative conclusions consultants frequently attempt to extract from color-contour plots.

It is not a CFD solver manual. It will not teach you how to click buttons inside ANSYS Fluent, Cadence Celsius EC (6SigmaDCX), or OpenFOAM, nor will it provide a decorative tour of rainbow temperature slices. 

The preceding books in this series accepted the liquid load bank under factory conditions (Book 01), audited high-frequency telemetry flash reports (Book 02), and executed the multi-megawatt thermal verification on the data hall floor (Book 03). This book begins when an engineering consultant, equipment vendor, or design firm hands you a bound CFD simulation report, or when you are tasked with capturing the physical baseline data that will determine whether that model may legally speak for the facility.

```
+----------------------------------------------------------------------------------------------------+
| THE TWO CONTRACTUAL AUDIT ROLES OF CFD |
+------------------------------------+---------------------------------------------------------------+
| 1. PHYSICAL BENCHMARKING (FLOOR) | 2. REPORT AUDITING (DESK) |
+------------------------------------+---------------------------------------------------------------+
| • 2-point CRAH supply averages | • Deconstruct the 6 mandatory input blocks |
| • 3-point CRAH return averages | • Audit solver residuals (< 10^-4) & mass balance (< 0.1%) |
| • 3-tier rack inlet probe trees | • Enforce single permitted decision domain |
| • Active PDU kW (zero nameplate) | • Strike speculative statements ("Hall Passed", "Add 50 kW") |
+------------------------------------+---------------------------------------------------------------+
```

When you conclude your audit, you must deliver two completed, auditable master sheets:
- **Sheet 1 (The Measurement & Calibration Record)**: Documents exactly where field probes were placed, how many points were averaged at each cooling unit opening, the three-tier vertical rack inlet temperatures, the active electrical feed power, and the named physical inputs altered during model calibration.
- **Sheet 2 (The Report Use & Decision Gate)**: Records the single decision the CFD report is authorized to support, verifies the presence of the six mandatory input blocks, confirms that every plot specifies its cutting plane coordinates, and formally logs the speculative sentences that were struck from the report executive summary.

If you are walking into the data hall tomorrow with thermal probes, turn to Chapter 6 and print Sheet 1. A blank cell is an automated stop. An inlet temperature copied from a previous facility report is a fabricated record.

## What you may copy

You may copy the master sheet headings, measurement grids, and audit checklists into your project commissioning file. You may not paste a colorful CFD temperature contour into a facility executive summary and declare that the image constitutes an engineering validation. 

The data hall has its own mechanical P&IDs, architectural layouts, and thermal boundary conditions. This field guide dictates what must be physically measured before a numerical model is permitted to represent those drawings, and establishes the strict boundaries within which a completed report may be used. It does not replace the professional engineer of record.

## Decisions to record before reading the report

- The single contractual decision the CFD report is commissioned to answer.
- The physical multi-point calibration grid executed on the data hall floor.
- The specific sentences you will formally refuse to sign based solely on color contours.
- The reference date of the physical measurements compared against the model geometry freeze date.

---

# 1. The points: field measurement protocol

A computational fluid dynamics report that has not been benchmarked against calibrated physical instruments is an artistic opinion rendered in partial differential equations. If an engineering consultant presents a simulation report based entirely on uncalibrated assumptions, that document must be stamped on its cover: **"UNVERIFIED DESIGN HYPOTHESIS"**. 

If the report is intended to serve as an operational baseline for an existing, physical data hall, physical field benchmarking must precede any interpretation of the results.

![Field Physical Measurement Protocol](../figures/fig-05-multi-point-field-benchmarking.png)

## The Minimal Field Benchmarking Grid

Do not attempt to deploy hundreds of temporary thermocouples in an undisciplined mesh across the whitespace. An unorganized cloud of sensor readings creates confusion rather than calibration. The standard benchmarking protocol focuses on high-precision data capture at critical fluid boundaries:

### 1. Cooling Unit (CRAH / In-Row / Fan Wall) Openings
- **Supply Air Discharge**: Measure air temperature at the discharge opening using calibrated fast-response thermistors or PT100 probes. You must average **at least two distinct points** across the discharge plane (S_1, S_2). Taking a casual reading with a handheld thermometer standing two meters out in the aisle is unacceptable; room air entrainment cools or warms the air stream before it reaches the floor, distorting the unit's true thermodynamic discharge.
- **Return Air Grille**: Measure air temperature across the return grille using **at least three distinct points** (R_1, R_2, R_3) distributed across the top, center, and bottom of the intake face. Return grilles frequently exhibit thermal stratification of 3.0 K to 6.0 K between their lower and upper edges. A single sensor taped to the center of the grille produces a misleading return temperature value.

$$\bar{T}_{\text{supply}} = \frac{1}{2} \sum_{i=1}^{2} S_i, \quad \bar{T}_{\text{return}} = \frac{1}{3} \sum_{j=1}^{3} R_j$$

### 2. Cabinet Intake and Exhaust Profiles
At every cabinet position designated in the project claim (or every high-density load-bank rack footprint), measure air temperature along a standardized vertical intake tree:
- **Bottom Intake (T_1)**: 0.3 m above finished floor (approximately rack unit U06). Evaluates floor jet entrainment and underfloor tile plume delivery.
- **Middle Intake (T_2)**: 1.2 m above finished floor (approximately rack unit U24). Serves as the core reference intake temperature for the server chassis array.
- **Top Intake (T_3)**: 1.8 m above finished floor (approximately rack unit U42). Evaluates hot air recirculation rolling over the top of the cabinet or escaping containment roof joints.

In uncontained or partially contained rows, T_3 is frequently 5.0 K to 10.0 K hotter than T_1. Averaging all three points into a single "cabinet temperature" obscures localized thermal stress. Each vertical elevation must be recorded independently on Sheet 1.

### 3. Exhaust Discharge Face
Measure exhaust temperature at the rear perforated door at the same three vertical elevations. The local delta-T across the server chassis (ΔT_rack = T_exhaust - T_intake) provides the empirical boundary condition needed to verify internal server fan mass flow rates:

$$\dot{m}_{\text{server}} = \frac{P_{\text{rack}}}{c_p \cdot (\bar{T}_{\text{exhaust}} - \bar{T}_{\text{intake}})}$$

## The Electrical Nameplate Fallacy

Thermal heat input into the CFD model must be sourced directly from active electrical feed telemetry, never from manufacturer nameplate ratings.

The power rating stamped on a server power supply unit (e.g., 1600 W PSU on a 2U chassis) represents an electrical safety maximum, sizing the branch circuit conductors and overcurrent protective devices. Under actual production compute workloads, that chassis may consume only 650 W to 850 W; an idle server may draw less than 250 W.

```
+----------------------------------------------------------------------------------------------------+
| THE NAMEPLATE INFLATION TRAP |
+--------------------------+-----------------------+-----------------------+-------------------------+
| EQUIPMENT CLASS | NAMEPLATE RATING (kW) | ACTIVE MEASURED (kW) | MODEL OVERESTIMATION |
+--------------------------+-----------------------+-----------------------+-------------------------+
| High-Density AI Rack | 160.0 kW (PSU Sum) | 120.0 kW (Active PDU) | + 33.3% False Heat |
| Enterprise Server Rack | 14.5 kW (PSU Sum) | 8.2 kW (Active PDU) | + 76.8% False Heat |
| Core Network Spine Rack | 22.0 kW (PSU Sum) | 11.4 kW (Active PDU) | + 93.0% False Heat |
+--------------------------+-----------------------+-----------------------+-------------------------+
```

If a CFD modeler inputs server nameplate ratings into their software, the model injects 40% to 80% more thermal energy into the simulated whitespace than physically exists. The simulation will predict widespread thermal throttling, red hot spots, and cooling plant failure. 

The data center operator will then be urged to spend capital adding unnecessary CRAH units or lowering chilled water setpoints. Always read active 3-phase kW from the PDU smart meter or revenue-grade branch circuit monitor on the day of testing, and verify that this number is the heat source term assigned to that rack in the simulation software.

## Spatial Alignment of Numerical Probes

Every measurement point logged on Sheet 1 must correspond to an identical numerical sampling probe within the CFD solver's computational domain.

A numerical probe placed in the center of the cold aisle in software cannot be compared against a physical thermocouple taped to a server front bezel. Air velocity and temperature gradients in the boundary layer immediately adjacent to the perforated door are steep. 

If the numerical probe coordinates do not match the physical coordinates within ± 50 mm, the delta between simulation and reality is a spatial sampling error, not a model defect.

## Date Synchronization and Layout Freezes

Record the calendar date and shift timestamp of the physical field measurements alongside the geometry freeze date of the CAD model.

Data centers are dynamic environments. Over the course of three months, facility technicians install blanking panels, re-route underfloor power cables, adjust CRAH fan speed setpoints, and add floor grilles. 

If your temperature measurements were taken in November on an as-built layout, and the CFD consultant ran their model using an architectural schematic from the previous February, the model does not represent the room you measured. The report must state which layout revision is modeled; an undocumented mixture of dates invalidates the calibration.

## Decisions to record before test start

- The specific cooling units measured, noting supply opening points (S_1, S_2) and return opening points (R_1, R_2, R_3).
- The surveyed cabinet rows, recording vertical inlet probe readings at 0.3 m, 1.2 m, and 1.8 m.
- Sourcing of electrical heat: documented from active PDU meters, with the nameplate rating explicitly rejected.
- Physical coordinates of all field probes mapped to the numerical model grid.
- Measurement execution date compared against model CAD freeze date.

---

# 2. How a measurement is allowed to change the model

Model calibration is not the process of manipulating software settings until a simulated temperature contour matches a physical thermocouple reading. Calibration by curve-fitting produces an illusion of accuracy; it does not produce a predictive model of the data hall.

Under governing engineering standards—including **ASME V&V 20** (*Standard for Verification and Validation in Computational Fluid Dynamics and Heat Transfer*) and **ASHRAE Guideline 14**—calibration is the rigorous identification and correction of physical boundary input errors.

![CFD Verification and Validation Lifecycle](../figures/fig-01-cfd-audit-lifecycle.png)

## The Permitted Calibration Inputs

If your physical field measurements (from Sheet 1) diverge from the CFD simulation results, you are permitted to alter **only those physical parameters that you can touch, walk to, and independently verify in the room**.

```
+----------------------------------------------------------------------------------------------------+
| PERMITTED VS PROHIBITED MODEL CALIBRATIONS |
+------------------------------------+---------------------------------------------------------------+
| PERMITTED CALIBRATION PARAMETERS | PROHIBITED MATHEMATICAL MANIPULATIONS |
| (PHYSICAL INPUTS YOU CAN TOUCH) | (ARBITRARY MODEL CURVE-FITTING) |
+------------------------------------+---------------------------------------------------------------+
| • Missing blanking panel added | • Artificial turbulent viscosity multiplier adjusted |
| • Blocked floor tile free area % | • Fictitious boundary heat transfer coefficients |
| • Unsealed cable penetration hole | • Arbitrary server airflow multiplier factors |
| • Containment door gap modeled | • Inverting or shifting the temperature color scale bar |
| • Nameplate kW replaced by PDU kW | • Manually overwriting cell temperatures near hotspots |
| • CRAH supply T set to opening avg | • Unnamed 'fudge factors' applied to momentum source terms |
+------------------------------------+---------------------------------------------------------------+
```

Every parameter modified during calibration must be documented by name, location, and physical justification on Sheet 1:
1. **Missing Blanking Panels**: A survey discovers that Rack 12 has two empty 1U slots without blanking panels. The modeler updates the numerical rack face from a solid boundary to an open orifice with 25 L/s of hot exhaust recirculation.
2. **Floor Grille Obstructions**: An underfloor cabling bundle blocks 30% of the free area beneath Tile 04. The modeler updates the tile free open area ratio from 40% to 28%.
3. **Cable Penetration Leakage**: The model assumed sealed raised-floor grommets, but physical inspection reveals three unsealed 200× 200 mm cable cutouts beneath the PDU. The modeler adds these penetrations as open parasitic floor orifices.
4. **Supply Temperature Sourcing**: The simulation assumed a design supply temperature of 18.0°C, but calibrated field probes measure the actual CRAH discharge opening at 20.5°C. The modeler updates the boundary condition to reflect the physical operating setpoint.
5. **Electrical Power Sourcing**: The modeler replaces an initial 15.0 kW nameplate assumption with the physical 8.4 kW reading captured by the PDU branch monitor.

If an adjustment cannot be tied to a documented physical feature within the whitespace, it is strictly prohibited. An anonymous multiplier inserted into a script is an admission of failure disguised as a calibration parameter.

## Quantitative Validation Error Metrics

To determine whether a simulation achieves acceptable convergence with physical reality, the model must be audited against quantitative statistical criteria across all benchmarking probes (N ≥ 12 points minimum):

### 1. Mean Absolute Error (MAE)
Quantifies the average magnitude of absolute error across all sampled measurement locations:

$$\text{MAE} = \frac{1}{N} \sum_{i=1}^{N} \left| T_{\text{sim}, i} - T_{\text{meas}, i} \right|$$

**Acceptance Standard**: MAE ≤ 1.0 K. An average temperature divergence exceeding 1.0 K across the room indicates a fundamental mismatch in airflow distribution.

### 2. Root Mean Square Error (RMSE)
Penalizes severe localized outliers more heavily than MAE:

$$\text{RMSE} = \sqrt{\frac{1}{N} \sum_{i=1}^{N} \left( T_{\text{sim}, i} - T_{\text{meas}, i} \right)^2}$$

**Acceptance Standard**: RMSE ≤ 1.5 K.

### 3. Normalised Mean Bias Error (NMBE)
Determines whether the simulation exhibits a systemic global bias (consistently over-predicting or under-predicting room temperatures):

$$\text{NMBE} = \frac{\sum_{i=1}^{N} \left( T_{\text{sim}, i} - T_{\text{meas}, i} \right)}{N \cdot \bar{T}_{\text{meas}}} \times 100\%$$

**Acceptance Standard**: |NMBE| ≤ 5.0%. A positive bias exceeding 5% indicates artificial thermal trapping; a negative bias exceeding -5% indicates unmodeled parasitic cooling or excessive simulated airflow.

### 4. Maximum Localized Outlier ($Δ_\max$)
Audits the single worst discrepancy across the computational domain:

$$\Delta_{\max} = \max_{1 \le i \le N} \left| T_{\text{sim}, i} - T_{\text{meas}, i} \right|$$

**Acceptance Standard**: $Δ_\max ≤ 2.5 K$. If any individual server intake probe diverges by more than 2.5 K, that cabinet must be treated as an unresolved localized airflow anomaly.

## The Two-Iteration Stopping Rule

Model calibration must not become an open-ended exercise in numerical tuning until the consultant produces an agreeable plot.

Enforce the **Two-Iteration Stopping Rule**:
- **Pass 1**: The baseline model is run using as-built drawings and active PDU electrical readings. If errors exceed the acceptance criteria, the physical survey data is cross-checked to identify documented physical anomalies (e.g., missing blanking panels or blocked tiles).
- **Pass 2**: The identified physical corrections are incorporated into the model geometry, and the solver is re-run.

If after Pass 2 the model still fails to achieve MAE ≤ 1.0 K and RMSE ≤ 1.5 K, **stop all further calibration**.

The Commissioning Lead must write **"MODEL NOT CALIBRATED"** in bold ink across the cover of the report. An uncalibrated model may still serve as an abstract conceptual comparison between two design options in pre-construction; it is legally disqualified from certifying the compliance or capacity of the physical data hall.

## Decisions to record before test start

- The full inventory of physical parameters modified between Pass 1 and Pass 2.
- The calculated statistical error metrics (MAE, RMSE, NMBE, and $Δ_\max$).
- Confirmation of whether the model satisfied the statistical validation gates.
- Formal marking of the report as either "CALIBRATED AGAINST PHYSICAL FACILITY" or "NOT CALIBRATED".

---

# 3. Aerodynamics and how to read the report

Before evaluating the conclusions of a computational fluid dynamics report, you must understand the physical aerodynamics governing data center airflow, and audit the report block by block in the order it has to be true.

A CFD report that opens with colorful 3D rendering slices is attempting to secure your approval before you examine the underlying physics. Ignore the color plots on your first reading. Turn immediately to the mechanical boundary conditions and verify the fluid dynamics.

![Underfloor Plenum Dynamics](../figures/fig-02-underfloor-plenum-hydraulics.png)

## Underfloor Plenum Dynamics and Static Pressure Regain

In a raised-floor data hall, the space beneath the floor acts as a shared pressurized distribution plenum. Airflow exiting a downflow CRAH unit behaves according to fundamental fluid mechanics governed by the Bernoulli principle and momentum conservation:

$$P_{\text{total}} = P_{\text{static}} + \frac{1}{2} \rho v^2$$

As shown in Figure 02, high-velocity air discharged from a CRAH fan (v > 5.0 m/s) possesses high dynamic pressure ($\frac{1}{2} \rho v^2$) but depressed static pressure (P_static). 

As this air jet travels along the plenum axis away from the unit, frictional drag against the subfloor slab and deceleration against the plenum end-wall cause the fluid velocity to decay. As velocity drops, kinetic energy converts into static pressure—a phenomenon known as **static pressure regain** (the momentum recovery effect):

1. **Near-CRAH Floor Tiles**: Perforated tiles installed directly adjacent to the CRAH discharge face experience low static pressure (frequently < 5 Pa). In poorly designed plenums, the Bernoulli effect can cause local static pressure to drop below zero relative to the whitespace (P_static < 0 Pa). When this occurs, the perforated tile behaves as an intake: instead of discharging cold air, it sucks hot air from the aisle downward into the plenum.
2. **Plenum Dead-End Tiles**: Perforated tiles located at the far end of the row (near plenum bulkheads) experience the highest static pressure (frequently 30 Pa to 45 Pa) and discharge the highest volumetric flow rates.

A competent CFD model must resolve these underfloor momentum vectors with high spatial resolution. If a model treats the raised floor void as a uniform, constant-pressure reservoir (a lumped parameter box), it completely fails to predict near-unit tile starvation.

![Aisle Containment Aerodynamics](../figures/fig-03-containment-leakage-aerodynamics.png)

## Aisle Containment and Parasitic Leakage Aerodynamics

Aisle containment systems—Cold Aisle Containment (CAC) and Hot Aisle Containment (HAC)—are designed to eliminate the thermodynamic mixing of supply and exhaust air. However, their physical performance depends on pressure balance and airtight sealing, as shown in Figure 03:

### 1. Pressure Differential Across Containment Doors
The pressure inside an enclosed cold aisle must be maintained slightly positive relative to the hot whitespace (+2.0 Pa to +5.0 Pa). 
- If cooling units supply excess air, aisle pressure rises (> 15 Pa), forcing containment doors open and wasting fan energy through ceiling seams.
- If cooling unit airflow falls below the aggregate demand of the server fans ($\sum Q_{\text{CRAH}} < \sum Q_{\text{server}}$), the cold aisle drops into **negative pressure**. A negative cold aisle pulls hot exhaust air backward through cable penetrations, unsealed floor tiles, and door sweeps, triggering rapid server intake temperature spikes.

### 2. Parasitic Leakage Paths
A simulation that treats containment structures as perfectly hermetic seals is fundamentally flawed. In actual data halls, air escapes through multiple parasitic pathways:
- **Missing Blanking Panels**: A single missing 1U blanking panel in an active rack allows up to 25 L/s (50 CFM) of hot exhaust air to short-circuit directly back into the server intake.
- **Underfloor Cable Penetrations**: An unsealed 200× 200 mm cable cutout allows 150 L/s of cold plenum air to escape into the hot aisle, bypassing compute equipment entirely.
- **Brush Grommets**: Even high-quality nylon brush grommets exhibit a leakage area of 10% to 15% under a 20 Pa plenum differential pressure.

Every containment model must explicitly include leakage coefficients based on physical site audits.

![Hybrid Liquid-Air Thermal Split](../figures/fig-04-hybrid-liquid-air-thermal-split.png)

## The Hybrid Liquid-Cooled AI Hall Reality

The most dangerous assumption in modern data center engineering is the belief that high-density liquid-cooled compute clusters (such as NVL72 or GB200 architectures) require no airflow modeling.

As demonstrated in Figure 04, direct-to-chip liquid cooling extracts approximately **80% of total rack heat** (typically 96.0 kW on a 120.0 kW rack footprint) directly from GPU and CPU silicon into the secondary glycol loop. However, the remaining **20% of rack heat (24.0 kW per rack)** is convected directly into the whitespace air by:
- Optical transceivers (OSFP/QSFP modules) on high-speed network switches.
- Switched-mode power supply units (PSUs) and 48V busbar resistance.
- Voltage regulator modules (VRMs), memory buffers, and auxiliary motherboard silicon.

For a modest row of ten NVL72 compute racks, that residual 20% air heat totals **240.0 kW**—the convective heat equivalent of 40 standard enterprise server racks dumped directly into the room. 

If a CFD model ignores this 240 kW convective load under the assumption that the hall is "liquid-cooled," optical transceivers rated for 70.0°C will heat-soak at 85.0°C+, resulting in optical signal degradation, dropped network packets, and training cluster halts. A CFD report for a liquid-cooled data hall that omits the air-side convective thermal split must be rejected immediately.

## The Six Mandatory Input Blocks of a CFD Report

To audit a CFD report systematically, examine the document in six sequential blocks:

1. **The Statement of Purpose**: Exactly one unambiguous sentence stating what operational question the simulation is commissioned to answer. If the purpose is absent or vague ("optimize the room"), halt the review.
2. **The Whitespace Geometry Block**: Room dimensions, slab-to-slab clear height, raised-floor void depth (H_void), structural drop beams, overhead cable tray congestion percentage, and partition locations.
3. **The IT Equipment Block**: Rack layouts, physical server form factors, front-to-back airflow direction, active electrical kW per rack (from PDU telemetry), internal fan P-Q curves, and blanking panel status.
4. **The Mechanical Cooling Block**: CRAH or fan wall locations, unit supply opening dimensions, supply air discharge velocities, operating setpoints, return opening dimensions, and fan curve definitions.
5. **The Discretization and Mesh Block**: Grid topology (structured hexahedral vs. unstructured polyhedral), total cell count (N_cells), boundary layer inflation layers, and Grid Convergence Index (GCI) verification.
6. **The Solver Convergence Block**: The specific Navier-Stokes turbulence model utilized (e.g., standard k-ε, Realizable k-ε, or SST k-ω), convergence residual histories, and global mass/energy balance closure.

## Mandatory Solver Convergence Standards

A simulation cannot be evaluated until its mathematical convergence is proven:
- **Momentum Residuals**: Normalized continuity, x-velocity, y-velocity, and z-velocity residuals must decay monotonically below **10^{-4}**.
- **Energy Residual**: Normalized enthalpy/energy residual must decay below **10^{-6}**.
- **Global Mass Imbalance**: The net difference between total air mass entering the room and total air mass exiting the room must be less than **0.1%**:

$$\left| \frac{\sum \dot{m}_{\text{supply}} - \sum \dot{m}_{\text{exhaust}}}{\sum \dot{m}_{\text{supply}}} \right| \times 100\% \le 0.10\%$$

- **Point Monitor History**: Point temperature monitors placed at critical server intakes must be plotted over solver iterations. If point temperatures are still drifting upwards or oscillating when the solver stops, the calculation was halted prematurely and the results are invalid.

## Decisions to record before test start

- Verification that underfloor plenum static regain and tile momentum were physically resolved.
- Sourcing of aisle containment leakage coefficients and door delta-P.
- The convective air heat fraction assigned to liquid racks (verifying ≈ 20% convective air split).
- Audit of the six mandatory input blocks.
- Verification that solver residuals satisfied continuity < 10^{-4} and energy < 10^{-6}.

---

# 4. What the report is allowed to decide

A computational fluid dynamics report is contractually permitted to support exactly **one decision**. State that decision on the cover before reviewing the simulation plots. 

In mission-critical data center engineering, four distinct decision domains are legitimate. Using a report commissioned for one domain to justify decisions in another—or attempting to address multiple domains simultaneously—inevitably leads to misapplied engineering and flawed capital expenditures.

![Airflow Performance Metrics and ASHRAE Envelopes](../figures/fig-06-thermal-indexes-and-ashrae-envelopes.png)

## The Four Permitted Decision Domains

### 1. Pre-Construction Design Comparison
- **Permitted Scope**: Comparing Layout Option A against Layout Option B before any physical construction begins (for example, comparing an 800 mm raised-floor plenum against a flooded-aisle flat slab, or evaluating hot aisle containment versus cold aisle containment).
- **Authorized Finding**: The report may conclude: *"Option A achieves 3.8 K lower peak rack intake temperatures and a 12% higher Cold Aisle Capture Index than Option B under identical boundary conditions."*
- **Boundary Restriction**: The report **cannot** state that Option A meets as-built contract specifications. Nothing has been built. This use requires zero physical field measurements; its validity depends entirely on ensuring that both options were discretized with identical mesh density and executed under identical solver convergence criteria.

### 2. Built-Hall Compliance Audit
- **Permitted Scope**: Verifying that a completed, physical data hall satisfies contract airflow and thermal specifications prior to IT hardware deployment.
- **Authorized Finding**: The report may conclude: *"The calibrated model demonstrates that with all designated cooling units active at nominal setpoints, 100% of server intake planes operate within the ASHRAE Recommended A1 thermal envelope."*
- **Boundary Restriction**: This use **requires** the multi-point physical field measurements from Chapter 1 and the statistical validation audit (MAE ≤ 1.0 K) from Chapter 2. Without physical benchmarking, a built-hall compliance report is merely a pre-construction design model that arrived late.

### 3. Operational Hotspot Root-Cause Analysis
- **Permitted Scope**: Diagnosing the physical cause of localized overheating in an operating data hall, and evaluating proposed physical remediation measures.
- **Authorized Finding**: The report may conclude: *"The 31.5°C intake hotspot at Rack 18 is caused by severe underfloor plenum jet entrainment depleting static pressure to -2.5 Pa at Tile 07. Simulating the addition of underfloor air baffles restores plenum pressure to +14.0 Pa and reduces peak intake temperature to 23.2°C."*
- **Boundary Restriction**: The identified root cause must correspond to a physical input you can touch in the room. Furthermore, a proposed remediation is not a verified conclusion until the consultant executes a formal **rerun script** demonstrating that the modification eliminates the hotspot without creating secondary deficits elsewhere in the hall.

### 4. N-1 Emergency Failure Ride-Through
- **Permitted Scope**: Evaluating airflow redistribution, intake temperature excursions, and thermal runaway timelines following the sudden loss of an active CRAH unit or chiller feed.
- **Authorized Finding**: The report may conclude: *"Upon the simulated trip of CRAH-02, cold aisle static pressure decays within 4.5 seconds, and Rack 09 intake temperature breaches the ASHRAE Allowable threshold of 32.0°C after 8.5 minutes of continued operation."*
- **Boundary Restriction**: This application requires **transient, time-accurate numerical solving** (dt ≤ 1.0 s). A steady-state simulation cannot narrate a timeline; evaluating thermal ride-through using a steady-state run falsely assumes that fluid velocities and thermal plumes transition instantaneously without thermal inertia.

## Dimensionless Airflow Performance Indices

A rigorous CFD report moves beyond simple temperature plots to evaluate objective, dimensionless airflow performance indices:

### 1. Supply Heat Index (SHI) and Return Heat Index (RHI)
Developed by Sharma and Herrick, these indices quantify the degree of thermal contamination across the whitespace:

$$\text{SHI} = \frac{T_{\text{in}} - T_{\text{supply}}}{T_{\text{exhaust}} - T_{\text{supply}}}, \quad \text{RHI} = \frac{T_{\text{return}} - T_{\text{supply}}}{T_{\text{exhaust}} - T_{\text{supply}}} = 1 - \text{SHI}$$

Where:
- T_in is the rack intake temperature.
- T_supply is cooling unit discharge temperature.
- T_exhaust is server rear discharge temperature.
- T_return is cooling unit return grille temperature.

**Acceptance Standard**:
- SHI = 0.00 represents perfect containment (zero recirculation of hot exhaust air into the intake stream).
- Industry standard for modern contained data centers is **SHI ≤ 0.15**.
- An SHI > 0.30 indicates defective aisle containment, severe blanking panel leakage, or gross airflow deficits.

### 2. Cold Aisle Capture Index (CI)
Quantifies the percentage of air ingested by a server intake that originates directly from local perforated tiles or supply grilles, rather than recirculated room air:

$$\text{CI} = \frac{Q_{\text{conditioned\_intake}}}{Q_{\text{total\_server\_demand}}} \times 100\%$$

**Acceptance Standard**:
- **High-Performance Containment**: CI ≥ 90%.
- **Marginal Aisle**: 75% ≤ CI < 90%.
- **Severe Ingestion Deficit**: CI < 70% (indicates cold aisle starvation where server fans pull hot exhaust air from the room).

## Compliance against ASHRAE TC 9.9 Thermal Envelopes

The performance of server intakes must be audited directly against the governing **ASHRAE TC 9.9 Thermal Guidelines for Data Processing Environments** (Class A1 envelope):

```
+----------------------------------------------------------------------------------------------------+
| ASHRAE CLASS A1 THERMAL ENVELOPE AUDIT |
+--------------------------+-----------------------+-----------------------+-------------------------+
| ENVIRONMENTAL PARAMETER | RECOMMENDED ENVELOPE | ALLOWABLE ENVELOPE | AUDIT VIOLATION LIMIT |
+--------------------------+-----------------------+-----------------------+-------------------------+
| Dry-Bulb Temperature | 18.0°C to 27.0°C | 15.0°C to 32.0°C | > 32.0°C or < 15.0°C |
| Dew Point Temperature | 5.5°C to 15.0°C | -12.0°C to 17.0°C | > 17.0°C (Condensation) |
| Maximum Relative Humidity| 60% RH | 80% RH | > 80% RH |
+--------------------------+-----------------------+-----------------------+-------------------------+
```

### The Rack Cooling Index (RCI)
To summarize row-wide compliance mathematically, the report should compute the **Rack Cooling Index**:
- **RCI_HI (High-Temperature Compliance)**: Measures the percentage of intake points operating within the Recommended maximum (27.0°C) without any points breaching the Allowable ceiling (32.0°C). Target: RCI_HI ≥ 95% (Ideal: 100%).
- **RCI_LO (Low-Temperature Compliance)**: Measures protection against overcooling below the minimum floor (18.0°C). Target: RCI_LO ≥ 95%.

## The Palette Manipulation Trap

The primary mechanism of visual deception in CFD reporting is the arbitrary manipulation of the temperature color contour scale:
- A modeler who wishes to present a dangerously overheated room as healthy can simply adjust the palette upper bound to 45.0°C. On that scale, a server intake operating at 30.0°C (severely overheated) renders in a calming blue-green hue.
- Conversely, a modeler seeking to justify an unnecessary cooling expansion can set the palette upper bound to 24.0°C. On that scale, a healthy intake at 23.5°C renders in an alarming fiery red.

**The Color Scale Audit Law**: Never evaluate a CFD report from color contours alone. Always extract the numerical probe values from cutting planes, and insist that all comparative plots be normalized to an identical, fixed scale (15.0°C to 35.0°C).

## Decisions to record before test start

- The single permitted decision domain selected for this report, with the other three marked as not applicable.
- The specific edition of ASHRAE TC 9.9 cited in the project specification.
- Verification that dimensionless metrics (SHI ≤ 0.15, CI ≥ 90%) are reported.
- Confirmation that color contour scales are normalized to fixed numerical limits.

---

# 5. Sentences you do not write

A CFD simulation report will invariably present conclusions and recommendations drafted by the model author. Most of these sentences are not yours to sign.

As a Commissioning Lead, technical auditor, or facility engineer, your professional duty is to maintain strict evidentiary standards. You must identify speculative or unverified statements in the consultant's draft and formally strike them from the executive summary before the report is accepted.

![CFD Report Decision and Refusal Matrix](../figures/fig-07-cfd-decision-and-refusal-matrix.png)

## The Four Primary Refused Statements

```
+----------------------------------------------------------------------------------------------------+
| PROHIBITED CFD REPORT STATEMENTS |
+------------------------------------+---------------------------------------------------------------+
| PROHIBITED STATEMENT IN DRAFT | MANDATORY AUDIT REFUSAL RATIONALE & REMEDIATION |
+------------------------------------+---------------------------------------------------------------+
| 1. "The data hall has passed | REFUSED. CFD is a mathematical simulation, not a physical |
| commissioning." | test. Commissioning pass/fail is proven exclusively by Level 5|
| | physical load-bank testing (Book 03). Strike sentence. |
+------------------------------------+---------------------------------------------------------------+
| 2. "Add 100 kW of cooling capacity | REFUSED. An untested proposal is not an engineering result. |
| to eliminate the hotspot." | Must be modeled as a verified rerun script with the new unit |
| | added. If not rerun, label: "PROPOSAL - NOT DEMONSTRATED". |
+------------------------------------+---------------------------------------------------------------+
| 3. "Compute servers will train AI | REFUSED. CFD simulates whitespace air temperatures; it does not|
| workloads reliably." | model silicon junction temperatures, throttling, or NVLink. |
| | Strike sentence. Limit claim strictly to intake air envelope. |
+------------------------------------+---------------------------------------------------------------+
| 4. "Streamline velocity confirms | REFUSED. A streamline shows flow direction, not mass flux. |
| airflow rate is 450 L/s." | Demand numerical surface integral or physical hood data. |
+------------------------------------+---------------------------------------------------------------+
```

### Refusal 1: "The Data Hall Has Passed Commissioning"
A consultant whose simulation shows comfortable blue contours across all server aisles will frequently conclude: *"Based on CFD modeling, the data hall cooling system has successfully passed commissioning and is cleared for IT deployment."*

**The Refusal**: You must refuse this sentence in ink. A numerical fluid dynamics model—no matter how finely meshed or beautifully rendered—is a simulation of reality, not reality itself. 

The physical data hall has not passed commissioning until physical liquid load banks are energized on the floor, electrical breakers are closed, secondary fluid pumps undergo physical N+1 trip failovers, and thermal enthalpy balance closures exceed 97.0% under the witnessed Level 5 protocols of Book 03. 

If the consultant's sentence is allowed to stand, an insurer or client auditor can argue that physical load-bank testing was deemed unnecessary because a computer model "passed" the facility. Strike the sentence; replace it with: *"The calibrated simulation predicts that the whitespace airflow distribution satisfies design thermal envelopes under the specified steady-state boundary conditions."*

### Refusal 2: "Add 100 kW of Cooling Capacity to Fix the Hotspot"
When a model reveals an intake hotspot exceeding 30.0°C, the report frequently offers a broad remedial recommendation: *"It is recommended that the operator add an additional 100 kW CRAH unit to Row 4 to resolve the hotspot."*

**The Refusal**: This is an untested proposal, not an engineering finding. In data center fluid dynamics, blindly adding airflow or cooling capacity to an existing room frequently exacerbates localized hot spots:
- Adding a high-velocity CRAH discharge near an existing unit can increase underfloor velocity, deepening Bernoulli static pressure depression and starving adjacent floor tiles.
- The additional fan energy increases overall heat rejection demand.

A remedial recommendation becomes an accepted engineering finding **only when the consultant incorporates the proposed unit into the model geometry, reruns the simulation under identical scene rules, and proves that the modification resolves the hotspot without creating new secondary deficits**. If the rerun script is not included in the report, label the sentence: *"UNVERIFIED PROPOSAL — RERUN NOT PERFORMED"*.

### Refusal 3: "Compute Servers Will Train AI Workloads Reliably"
Consultants frequently extrapolate macro-scale airflow predictions into silicon reliability claims: *"The model confirms that the AI accelerator clusters will operate continuously without thermal throttling during multi-node model training."*

**The Refusal**: A room-scale CFD model computes macro-scale convective air patterns in the whitespace. It possesses zero visibility into:
- Micro-scale thermal resistance across the cold plate interface (TIM-1 and TIM-2 thermal interface materials).
- Localized hotspot heat fluxes on GPU silicon dies exceeding 100 W/cm².
- Autonomous dynamic frequency scaling (DVFS) algorithms embedded within the processor microcode.
- High-speed NVLink optical transceiver bit error rates.

A server operating in a 22.0°C cold aisle can still experience catastrophic silicon throttling if its internal cold plate possesses microchannel scaling, or if secondary glycol flow is throttled. Strike any sentence purporting to predict silicon reliability or workload stability. The report speaks exclusively about the fluid boundary at the rack face.

### Refusal 4: "Streamline Velocity Confirms Tile Flow Is 450 L/s"
A report that displays elegant 3D particle traces or ribbon streamlines will sometimes assert volumetric airflow quantities based on the visual density of the lines: *"The streamlines exiting Tile 06 indicate a delivery rate of 450 L/s into the cold aisle."*

**The Refusal**: A streamline is a mathematical line everywhere tangent to the instantaneous fluid velocity vector. It visualizes the direction of travel; it does not measure volumetric mass flux. 

Volumetric flow rate across a boundary must be calculated via a formal surface integral of the normal velocity vector across all boundary face cells:

$$Q = \int_{A} (\vec{v} \cdot \vec{n}) \, dA \approx \sum_{k=1}^{M} v_{n, k} \cdot A_k$$

If the report does not present this numerical integration—or if physical flow hood measurements were not taken—the flow rate claim is an unverified visual estimate.

## Decisions to record before test start

- The comprehensive list of speculative sentences struck from the consultant's draft.
- Documentation that all proposed physical remedies are accompanied by formal rerun scripts.
- Formal reaffirmation that the CFD report does not replace Book 03 physical load-bank testing.
- Sign-off by the Commissioning Lead that the executive summary contains only authorized findings.

---

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

---

# 7. What this book does not own

This field guide will inevitably be misused by individuals seeking an all-inclusive textbook on computational fluid dynamics. Establish strict professional boundaries here.

A field audit method maintains integrity only when its boundaries are sharply drawn. Expanding this guide into software solver programming or mechanical design dilutes its authority.

```
+----------------------------------------------------------------------------------------------------+
| EXPLICIT NEGATIVE SCOPE BOUNDARIES |
+------------------------------------+---------------------------------------------------------------+
| WHAT THIS BOOK OWNS | WHAT THIS BOOK CANNOT AND DOES NOT OWN |
+------------------------------------+---------------------------------------------------------------+
| • Field multi-point calibration | • Commercial CFD solver algorithms, source code, or GUI menus |
| • Quantitative error metrics (MAE) | • Book 01 Scope: Load-bank design, manufacturing, and FAT |
| • The 6 mandatory input blocks | • Book 02 Scope: Telemetry anomaly algorithms (FLOC/Focus) |
| • Four permitted decision domains | • Book 03 Scope: Physical Level 5 load-bank floor testing |
| • Refusal of color-map speculation | • Silicon Physics: Chip junction temps ($T_j$), NVLink, AI ops|
| • The two master audit sheets | • Facility Design: Architectural, structural, and central MEP |
| • ASHRAE TC 9.9 compliance audit | • Next Facility: Copying room-specific averages across halls |
+------------------------------------+---------------------------------------------------------------+
```

## The Dedicated Boundaries

### 1. It Does Not Own the Solver Code or Commercial Software Menus
This book governs how to measure a physical room and how to audit an engineering report. It does not teach the internal finite-volume discretization schemes of commercial solvers (such as SIMPLE, PISO, or coupled algorithms), nor does it guide users through software menu interfaces. Those operations belong in the vendor’s documentation. Software mastery is not a substitute for physical measurement.

### 2. It Does Not Own Equipment Factory Acceptance (Book 01)
A CFD simulation model represents physical equipment through numerical boundary conditions (fan curves, pressure drop coefficients, and heat dissipation source terms). It does not certify that the physical load bank or server chassis was constructed safely, that its internal electrical contactors meet UL/IEC standards, or that its frame withstands seismic stress. Equipment acceptance belongs exclusively to Book 01.

### 3. It Does Not Own Telemetry Verification (Book 02)
This book cross-checks steady-state physical measurements against simulation probes. The mathematical validation of real-time time-series telemetry—including changepoint detection (FLOC/Focus), variance gating (σ² > 0), and quality bitmask verification—belongs to Book 02. A calm-looking CFD plot cannot override a time-series telemetry log that reveals thermal hunting.

### 4. It Does Not Own Physical Commissioning Verification (Book 03)
A CFD simulation is a predictive mathematical model; it is not a physical commissioning test. It cannot demonstrate that an actual N+1 pump will switch over in ≤ 1.5 seconds, that a check valve will seat without water hammer, or that electrical busbars will not overheat under full load. Physical facility verification belongs exclusively to the Level 5 integrated test procedures of Book 03.

### 5. It Does Not Own Silicon Performance and Compute Reliability
A whitespace CFD model resolves airflow and temperature fields in the air volume surrounding server racks. It possesses zero visibility into microchannel cold plate fluid dynamics, thermal interface material (TIM) degradation, silicon junction temperatures (T_j), or GPU memory throttling. A server rack operating in a 22.0°C cold aisle can still fail due to internal hardware defects. This book speaks strictly to the fluid boundary at the server intake bezel.

### 6. It Does Not Own the Next Data Hall
The physical measurement methodology (supply 2-point, return 3-point, 3-tier rack intake tree) and the report audit framework (the four permitted decisions and the refusal matrix) can be applied universally across mission-critical facilities. However, the specific numerical values—the measured temperatures, room flow rates, and calibration inputs—belong exclusively to the specific data hall audited. Copying numerical data from this report into another facility turns engineering verification into an unverified copy-paste exercise.

## Decisions to record before test start

- Re-affirmation that the commercial CFD solver manual is referenced, not duplicated.
- Explicit acknowledgment that CFD simulation does not replace Book 03 physical load-bank testing.
- The signed statement on Sheet 2 affirming that the report does not assert silicon reliability claims.

---

# 8. Public sources, and the copyright line

This field guide teaches an operational audit methodology for field benchmarking and evaluating computational fluid dynamics reports. It does not digest, transcribe, or duplicate proprietary engineering standards, commercial solver code, or confidential data center architectural drawings.

An engineering standard that can be purchased from an issuing standards body is not a document that may be reproduced in an external manual. Citing a standard by title, year, and specific equation to establish a legal audit threshold is standard professional practice; reproducing extensive passages from those standards within an AI-generated text is improper.

```
+----------------------------------------------------------------------------------------------------+
| NORMATIVE INDUSTRY STANDARDS CITED |
+----------------------+-----------------------------------------------------------------------------+
| ASME V&V 20 | "Standard for Verification and Validation in Computational Fluid Dynamics |
| | and Heat Transfer". Foundational principles for numerical discretization |
| | error (GCI) and validation comparison error metrics. |
+----------------------+-----------------------------------------------------------------------------+
| ASHRAE GUIDELINE 14 | "Measurement of Energy, Demand, and Water Savings". Establishes statistical |
| | calibration criteria: Mean Bias Error (NMBE) and Root Mean Square Error. |
+----------------------+-----------------------------------------------------------------------------+
| ASHRAE TC 9.9 | "Thermal Guidelines for Data Processing Environments" (5th Edition, 2021). |
| | Defines environmental classes (Class A1-A4), Recommended & Allowable bands. |
+----------------------+-----------------------------------------------------------------------------+
| GB 50174 | "Code for Design of Data Centers" (Chinese National Standard). Normative |
| | guidelines for data center airflow organization and numerical simulation. |
+----------------------+-----------------------------------------------------------------------------+
| SHARMA & HERRICK | "Dimensionless Parameters for Evaluation of Thermal Performance in Large- |
| (ASME 2002) | Scale Data Centers". Mathematical formulation of SHI and RHI indices. |
+----------------------+-----------------------------------------------------------------------------+
| HERRLIN (ASHRAE 2005)| "Rack Cooling Index (RCI): A Novel Metric for Evaluating Data Center |
| | Cooling Performance". Mathematical formulation of RCI_HI and RCI_LO. |
+----------------------+-----------------------------------------------------------------------------+
```

## Application of Normative Standards

The physical measurement protocols established in Chapter 1—including the 2-point cooling supply average, 3-point return grille average, and 3-tier vertical intake probe tree—derive from standard experimental airflow benchmarking practices adapted specifically for mission-critical data center validation.

Statistical error validation metrics (MAE ≤ 1.0 K, RMSE ≤ 1.5 K, |NMBE| ≤ 5.0%) combine the principles of ASME V&V 20 and ASHRAE Guideline 14. An engineering consultant whose simulation diverges from physical measurements by more than these thresholds has not delivered a validated model; they have delivered an uncalibrated design estimate.

The thermal evaluation criteria articulated in Chapter 4 derive directly from ASHRAE TC 9.9 (5th Edition, 2021). The Class A1 Recommended envelope (18.0°C to 27.0°C, maximum dew point 15.0°C) and Allowable envelope (15.0°C to 32.0°C) represent the global benchmark for enterprise compute hardware. This book cites these temperature and humidity thresholds; it does not reproduce the proprietary psychrometric charts published by ASHRAE.

Dimensionless airflow performance evaluation incorporates the peer-reviewed engineering formulations of Sharma and Herrick (Supply Heat Index and Return Heat Index) and Herrlin (Rack Cooling Index). These metrics provide mathematical objectivity, replacing subjective visual evaluations of color-contour plots with verifiable numerical criteria.

## Non-Proprietary Reference Architecture

To provide concrete, meaningful numerical yardsticks without disclosing proprietary manufacturer IP or client-confidential data, this book utilizes a non-proprietary reference architecture:
- **Hybrid Compute Footprint**: 120 kW virtual compute rack simulating high-density accelerated architectures (such as an NVL72 / GB200 class footprint).
- **Thermal Energy Split**: 80.0% (96.0 kW) direct-to-chip secondary liquid cooling; 20.0% (24.0 kW) convective air release into the whitespace.
- **Airflow Delivery**: Raised-floor plenum (800 mm clear void depth) with downflow EC-fan CRAH units discharging at 5.5 m/s, feeding Cold Aisle Containment (CAC) rows via 40% free-area perforated tiles.

Specific manufacturer CAD geometries, proprietary server internal fan tables, client-confidential network topologies, and proprietary data hall drawings belong in the project's secure archives under signed Non-Disclosure Agreements (NDAs). They must never be published in open reference guides.

## Decisions to record before test start

- The complete list of governing codes, guidelines, and technical papers cited in the CFD audit report, with publication dates.
- The specific edition of ASHRAE TC 9.9 cited in the project specifications.
- Formal confirmation that client-confidential architectural CAD models and vendor proprietary internal fan tables are preserved within local project files.

---
