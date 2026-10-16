# 0. How to use this book

This book has two explicit engineering jobs:
1. **Benchmark the Physical Room**: Establish a disciplined, multi-point field measurement protocol so that a numerical fluid dynamics simulation can be calibrated against physical reality rather than artistic intuition.
2. **Audit the Simulation Report**: Use the resulting computational fluid dynamics (CFD) report to make exactly one verified engineering decision, while formally refusing the speculative conclusions consultants frequently attempt to extract from color-contour plots.

It is not a CFD solver manual. It will not teach you how to click buttons inside ANSYS Fluent, Cadence Celsius EC (6SigmaDCX), or OpenFOAM, nor will it provide a decorative tour of rainbow temperature slices. 

The preceding books in this series accepted the liquid load bank under factory conditions (Book 01), audited high-frequency telemetry flash reports (Book 02), and executed the multi-megawatt thermal verification on the data hall floor (Book 03). This book begins when an engineering consultant, equipment vendor, or design firm hands you a bound CFD simulation report, or when you are tasked with capturing the physical baseline data that will determine whether that model may legally speak for the facility.

**THE TWO CONTRACTUAL AUDIT ROLES OF CFD**

| 1. PHYSICAL BENCHMARKING (FLOOR) | 2. REPORT AUDITING (DESK) |
| :--- | :--- |
| • 2-point CRAH supply averages | • Deconstruct the 6 mandatory input blocks |
| • 3-point CRAH return averages | • Audit solver residuals (< 10^-4) & mass balance (< 0.1%) |
| • 3-tier rack inlet probe trees | • Enforce single permitted decision domain |
| • Active PDU kW (zero nameplate) | • Strike speculative statements ("Hall Passed", "Add 50 kW") |

When you conclude your audit, you must deliver two completed, auditable master sheets:
- **Sheet 1 (The Measurement & Calibration Record)**: Documents exactly where field probes were placed, how many points were averaged at each cooling unit opening, the three-tier vertical rack inlet temperatures, the active electrical feed power, and the named physical inputs altered during model calibration.
- **Sheet 2 (The Report Use & Decision Gate)**: Records the single decision the CFD report is authorized to support, verifies the presence of the six mandatory input blocks, confirms that every plot specifies its cutting plane coordinates, and formally logs the speculative sentences that were struck from the report executive summary.

If you are walking into the data hall tomorrow with thermal probes, turn to Chapter 6 and print Sheet 1. A blank cell is an automated stop. An inlet temperature copied from a previous facility report is a fabricated record.

## What you may copy

You may copy the master sheet headings, measurement grids, and audit checklists into your project commissioning file. You may not paste a colorful CFD temperature contour into a facility executive summary and declare that the image constitutes an engineering validation. 

The data hall has its own mechanical P&IDs, architectural layouts, and thermal boundary conditions. This field guide dictates what must be physically measured before a numerical model is permitted to represent those drawings, and establishes the strict boundaries within which a completed report may be used. It does not replace the professional engineer of record.

## Governing Physics and Operational Audit Scope of Data Hall CFD

In high-density data center environments—where air-cooled enterprise racks share whitespace boundaries with 120 kW+ liquid-cooled AI clusters carrying an 80:20 liquid-to-air heat split—Computational Fluid Dynamics (CFD) is frequently misused as a substitute for physical commissioning. A numerical simulation solves discretized approximations of the Navier-Stokes continuity, momentum, and energy conservation equations across millions of finite-volume cells:

$$\nabla \cdot (\rho \vec{u}) = 0$$

$$\rho (\vec{u} \cdot \nabla)\vec{u} = -\nabla p + \nabla \cdot \left[ (\mu + \mu_t) \left( \nabla \vec{u} + (\nabla \vec{u})^T \right) \right] + \rho \vec{g} \beta (T - T_{\text{ref}})$$

$$\rho c_p (\vec{u} \cdot \nabla T) = \nabla \cdot \left( (k + k_t) \nabla T \right) + q'''_{\text{source}}$$

While the differential equations are exact in continuous space, commercial data hall CFD models rely on Reynolds-Averaged Navier-Stokes (RANS) turbulence closures (typically standard $k$-$\varepsilon$, realizable $k$-$\varepsilon$, or $k$-$\omega$ SST) and coarse porous-media approximations for perforated floor tiles, server chassis impedances, and underfloor cable obstructions. Without empirical field benchmarking against calibrated physical instruments, a converged CFD color contour can easily deviate from physical rack inlet temperatures by $4.0\,\text{K}$ to $9.5\,\text{K}$.

| Audit Governance Dimension | Unverified Design CFD (Pre-Construction) | Field-Benchmarked Operational CFD (Post-Walk) | Contractual Consequence at Handover |
| :--- | :--- | :--- | :--- |
| **Boundary Heat Sources ($q'''$)** | Nominal IT nameplate power or sales density targets | Revenue-grade 3-phase PDU active power ($P_{\text{elec}} - Q_{\text{liquid}}$) | Unverified models overestimate air heat by 30%–80%; refused for CapEx approval |
| **Perforated Tile Flow ($Q_{\text{tile}}$)** | Idealized uniform open-area percentage ($25\%$ or $50\%$) | Capture-hood volumetric balometer survey across aisle matrix | Captures sub-floor Bernoulli Venturi starvation and damper settings |
| **Containment Leakage ($A_{\text{leak}}$)** | Zero-leakage sealed CAD solid walls | Walked differential pressure ($\Delta P_{\text{aisle}}$) & effective orifice area | Quantifies hot-aisle bypass across unblanked U-slots and cable cutouts |
| **Cabinet Inlet Verification** | Volume-averaged cold-aisle air temperature | 3-tier vertical sensor tree ($0.3\,\text{m}, 1.2\,\text{m}, 1.8\,\text{m}$) at rack bezel | Prevents top-of-rack thermal throttling masked by spatial averaging |
| **Permitted Engineering Decision** | Early-stage architectural duct and plenum sizing only | Comparative ranking of candidate physical airflow remedies | Never accepted as standalone proof of SLA thermal compliance |

### The Four Non-Negotiable Rules of This Volume

1. **Physical Walk Precedes Numerical Trust**: No simulation report may be cited in an operational or handover meeting unless Sheet 1 (Field Measurement Protocol) has been executed on the physical floor under matching electrical load and cooling unit states.
2. **Boundary Calibration Is Physical, Not Cosmetic**: When a simulation disagrees with walked thermometer and balometer readings, the modeler may only adjust verified physical boundary inputs (measured PDU kilowatts, measured CRAH discharge temperatures, measured tile open areas, and surveyed leakage gaps). Altering turbulent viscosity ratios or inventing phantom momentum sources to force agreement at one rack invalidates the entire model.
3. **Worst-Elevation Governance**: Rack thermal compliance is governed by the single highest measured or predicted intake sensor elevation ($T_{\text{inlet, max}} = \max(T_{0.3}, T_{1.2}, T_{1.8})$), never by a room, row, or vertical cabinet average.
4. **Comparative Scope Limitation**: Even a calibrated CFD model is an interpolation tool used to choose between physical interventions (blanking panels, containment curtains, tile swaps, CRAH fan staging). The final acceptance of the chosen remedy is always a second physical walk with calibrated instruments.

## Pre-Benchmarking Gate Checklist and Instrumentation Readiness

Before deploying field technicians into an active whitespace to execute Sheet 1, the audit lead verifies that the data hall is operating in a repeatable quasi-steady thermal state. Taking air temperature and balometer readings while IT racks are ramping workload or while a chilled-water plant is staging a secondary chiller introduces transient drift ($\partial T / \partial t \neq 0$) that violates the steady-state RANS formulation of the CFD model.

$$\left| \frac{\partial T_{\text{return, CRAH}}}{\partial t} \right| \le 0.15\,\text{K / 15 min}, \qquad \left| \frac{\partial P_{\text{PDU, total}}}{\partial t} \right| \le 2.0\% \text{ / 15 min}$$

| Pre-Walk Readiness Gate | Field Verification Method | Quantitative Pass Criterion | Action if Gate Fails |
| :--- | :--- | :--- | :--- |
| **1. Electrical Load Stability** | Poll total hall PDU kW every $60\,\text{s}$ for $30\,\text{min}$ | Load variance $\le \pm 2.0\%$ across window | Postpone walk until batch compute job or load bank stabilizes |
| **2. Chilled Water Supply Stability** | Check CRAH entering water temperature ($T_{\text{CHW, in}}$) | $T_{\\text{CHW, in}}$ within $\\pm 0.3\\,\\text{K}$ of design setpoint | Hold chiller staging and economizer valve transitions during walk |
| **3. Containment Door Integrity** | Inspect both aisle end-doors and roof panels | All doors latched; zero propped-open maintenance doors | Close all doors and wait $15\,\text{min}$ for plenum $\\Delta P$ re-equilibration |
| **4. Instrument Thermal Soak** | Place RTD trees and balometer in hall $20\,\text{min}$ prior | Zero-offset cross-check in agitated ice/ambient bath $\le 0.10\,\text{K}$ | Reject any probe drifting outside IEC 60751 Class A tolerance |

## Case Study: Why Unbenchmarked Design CFD Fails on Day One of Live IT Load

In a representative $15\,\text{MW}$ hall deployment, a pre-construction CFD study modeled $120$ cabinets at a uniform $10.0\,\text{kW/rack}$ using idealized $25\%$ open-area floor grates and assumed zero underfloor blockage. When the hall was energized with heterogeneous enterprise and AI storage racks ranging from $3.5\,\text{kW}$ to $28.0\,\text{kW}$, twelve cabinets in Row C triggered intake high-temperature warnings ($31.4^\circ\text{C}$) despite total CRAH airflow exceeding server demand by $35\%$. Walking Sheet 1 immediately revealed that three $200\,\text{mm}$ fire-sprinkler mains and power busway drop-rods obstructed the subfloor plenum feeding Row C, starving its tiles to $240\,\text{CFM}$ while unblanked 1U slots allowed hot exhaust to recirculate directly into the top third of the cabinets. This volume prevents that exact failure by forcing physical boundary verification before any simulation claim is accepted.

### Step-by-Step Field Walk Workflow for Commissioning Engineers

When executing this volume on site, divide the field team into two synchronized pairs:
1. **Thermometry & Electrical Logging Pair**: Walks every cabinet row with the 3-tier vertical Pt100 intake/exhaust tree ($0.3\,\text{m}, 1.2\,\text{m}, 1.8\,\text{m}$), recording 60-second time-averaged temperatures alongside simultaneous 3-phase PDU active power ($\text{kW}$) and liquid CDU manifold enthalpy ($\dot{m} c_p \Delta T$).
2. **Pneumatic & Containment Pressure Pair**: Walks every cold aisle with the backpressure-compensated capture-hood balometer and digital micro-manometer, recording tile volumetric delivery ($Q_{\text{tile}}$), subfloor static pressure ($\Delta P_{\text{plenum}}$), containment differential pressure ($\Delta P_{\text{CAC}}$), and open bypass orifice areas ($A_{\text{leak}}$).

## Decisions to record before reading the report

- The single contractual decision the CFD report is commissioned to answer.
- The physical multi-point calibration grid executed on the data hall floor.
- The specific sentences you will formally refuse to sign based solely on color contours.
- The reference date of the physical measurements compared against the model geometry freeze date.

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

**THE NAMEPLATE INFLATION TRAP**

| EQUIPMENT CLASS | NAMEPLATE RATING (kW) | ACTIVE MEASURED (kW) | MODEL OVERESTIMATION |
| :--- | :--- | :--- | :--- |
| High-Density AI Rack Enterprise Server Rack Core Network Spine Rack | 160.0 kW (PSU Sum) 14.5 kW (PSU Sum) 22.0 kW (PSU Sum) | 120.0 kW (Active PDU) 8.2 kW (Active PDU) 11.4 kW (Active PDU) | + 33.3% False Heat + 76.8% False Heat + 93.0% False Heat |

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

## Pneumatic Airflow Metrology and Uncertainty Budgets

Temperature measurements alone cannot constrain a data hall CFD model because temperature is a ratio of thermal power to mass flow rate ($\Delta T = Q / (\dot{m} c_p)$). If a simulation underpredicts both rack power and airflow by $35\%$, the simulated temperature rise $\Delta T$ will accidentally match the field temperature while the underlying velocity field and recirculation plumes are completely wrong. Therefore, Sheet 1 requires simultaneous pneumatic airflow and differential pressure measurements alongside the 3-tier thermometry grid.

### Capture-Hood Balometer Protocol for Perforated Floor Tiles

To establish the true supply boundary condition from a raised-floor plenum, volumetric airflow ($Q_{\text{tile}}$) must be measured across a representative sample of perforated floor tiles (minimum every third tile along each cold aisle, plus both end-of-row tiles adjacent to high-pressure or high-velocity zones):

$$Q_{\text{tile}} = C_d \cdot A_{\text{free}} \cdot \sqrt{\frac{2 \Delta P_{\text{plenum}}}{\rho_{\text{air}}}}$$

Where:
- $C_d$ is the empirical discharge coefficient of the perforated grille and damper assembly (typically $0.60$ to $0.78$).
- $A_{\text{free}}$ is the net open perforated area of the $600\,\text{mm} \times 600\,\text{mm}$ tile ($\text{m}^2$).
- $\Delta P_{\text{plenum}} = P_{\text{subfloor}} - P_{\text{aisle}}$ is the local static pressure differential across the tile ($\text{Pa}$).
- $\rho_{\text{air}}$ is the local air density ($\approx 1.18\,\text{kg/m}^3$ at $24^\circ\text{C}$ sea level).

When placing a capture-hood balometer over a perforated floor tile, the hood skirt itself introduces a parasitic backpressure resistance ($\Delta P_{\text{hood}}$). In low-pressure plenums ($\Delta P_{\text{plenum}} < 12\,\text{Pa}$) or on high-open-area grates ($> 50\%$ open area), an uncompensated hood chokes the tile jet and under-reads true volumetric flow by $10\%$ to $18\%$. Always use a powered zero-pressure-drop (backpressure-compensated) balometer or cross-check the capture hood against a 16-point hot-wire anemometer traverse conducted $50\,\text{mm}$ above the tile face.

| Field Metrology Instrument | Measured Parameter | Minimum Calibration Class | Mandatory Field Deployment Rule |
| :--- | :--- | :--- | :--- |
| **4-Wire Pt100 RTD / Thermistor Tree** | Rack intake ($0.3, 1.2, 1.8\,\text{m}$) & CRAH $T_{\text{sup}}/T_{\text{ret}}$ | $\pm 0.15^\circ\text{C}$ (IEC 60751 Class A) | Radiation-shielded tip; $50\,\text{mm}$ standoff in front of bezel |
| **Backpressure-Compensated Balometer** | Perforated floor tile volumetric flow ($Q_{\text{tile}}$) | $\pm 3.0\%$ of reading $\pm 12\,\text{m}^3\text{/h}$ | Skirt sealed flush to floor; automatic backpressure compensation active |
| **Hot-Wire / Vane Anemometer Grid** | CRAH coil face velocity & open cutout jets | $\pm 2.0\%$ of reading $\pm 0.03\,\text{m/s}$ | Minimum 12-point equal-area traverse across discharge opening |
| **Micro-Manometer (Differential $\Delta P$)** | Subfloor-to-aisle & cold-to-hot containment $\Delta P$ | $\pm 1.0\%$ of reading $\pm 0.2\,\text{Pa}$ | Static pressure tip oriented perpendicular to local shear flow |
| **Revenue-Grade 3-Phase PDU Meter** | True active electrical power ($P_{\text{elec}}$) per rack | IEC 62053-22 Class 0.5S ($\pm 0.5\%$) | Simultaneous timestamped poll during thermal equilibrium dwell |

### Accounting for Hybrid Liquid-Air Heat Splits on High-Density Racks

In halls housing direct-to-chip liquid-cooled racks (such as NVL72 clusters or dense GPU pods), feeding total electrical PDU power ($P_{\text{elec}}$) into the airspace CFD domain is an immediate fatal error. The sensible heat rejected into the room air ($Q_{\text{air}}$) is strictly the residual after subtracting the enthalpy absorbed by the secondary coolant loop:

$$Q_{\text{air}} = P_{\text{elec}} - \dot{m}_{\text{coolant}} \cdot c_{p,\text{coolant}} \cdot \left( T_{\text{coolant, out}} - T_{\text{coolant, in}} \right)$$

For a $120.0\,\text{kW}$ rack operating at an $82\%$ liquid capture fraction ($Q_{\text{liquid}} = 98.4\,\text{kW}$), only $21.6\,\text{kW}$ enters the air stream via rear door fans and power shelves. Every hybrid rack on Sheet 1 must record both $P_{\text{elec}}$ and $Q_{\text{liquid}}$ so the CFD boundary condition reflects true sensible air heating.

## Subfloor Static Pressure Mapping and Bernoulli Venturi Starvation

In raised-floor plenums with shallow slab-to-slab heights ($450\,\text{mm}$ to $600\,\text{mm}$) and high-capacity perimeter CRAH units, high horizontal air velocity ($v_{\text{plenum}} > 4.5\,\text{m/s}$) immediately downstream of the CRAH discharge converts static pressure into dynamic velocity head according to Bernoulli's equation along a subfloor streamline:

$$P_{\text{static}}(x) + \frac{1}{2} \rho v_{\text{plenum}}(x)^2 + \Delta P_{\text{loss}}(0 \to x) = P_{\text{total, CRAH}}$$

When dynamic pressure $\frac{1}{2}\rho v_{\text{plenum}}^2$ exceeds the static plenum pressure near the first two perforated floor tiles adjacent to a CRAH discharge, the local static gauge pressure $P_{\text{static}}(x) - P_{\text{aisle}}$ drops near zero or turns negative! Instead of discharging conditioned cold air upward into the cold aisle, those first two perforated tiles either stall ($Q_{\text{tile}} \approx 0$) or **induct warm room air downward into the subfloor plenum** (the Venturi reverse-flow effect).

| Distance from CRAH Discharge | Subfloor Horizontal Velocity ($v_{\text{plenum}}$) | Dynamic Pressure Head ($\frac{1}{2}\rho v^2$) | Local Static $\Delta P_{\text{tile}}$ | Observed Perforated Tile Behavior |
| :--- | :--- | :--- | :--- | :--- |
| **$0.6\,\text{m}$ (Tile 1, Unbaffled)** | $6.2\,\text{m/s}$ | $22.7\,\text{Pa}$ | $-2.5\,\text{Pa}$ (Negative!) | **Reverse suction**: warm aisle air pulled into floor |
| **$1.8\,\text{m}$ (Tile 3, Transition)** | $4.1\,\text{m/s}$ | $9.9\,\text{Pa}$ | $+8.4\,\text{Pa}$ | Severe under-delivery ($310\,\text{CFM}$ vs $750\,\text{CFM}$ target) |
| **$4.8\,\text{m}$ (Tile 8, Mid-Row)** | $1.8\,\text{m/s}$ | $1.9\,\text{Pa}$ | $+18.5\,\text{Pa}$ | Nominal balanced delivery ($760\,\text{CFM}$) |
| **$9.6\,\text{m}$ (Tile 16, Dead-End)** | $0.4\,\text{m/s}$ | $0.1\,\text{Pa}$ | $+21.2\,\text{Pa}$ (Static regain) | Over-delivery ($840\,\text{CFM}$) unless damped |

Standard coarse-grid CFD models that represent the entire raised floor as a uniform constant-pressure boundary completely miss Bernoulli static-pressure recovery and Venturi tile reversal. Sheet 1 therefore requires measuring static $\Delta P_{\text{tile}}$ at the first tile, mid-row tile, and last tile of every cold aisle.

## Pitot-Static Traverse and Coil Enthalpy Cross-Checks on Perimeter CRAH Units

When a CRAH unit's internal BMS supply-air sensor or fan-speed flow estimate is suspected of drift, the field benchmarking team verifies total unit volumetric airflow ($Q_{\text{CRAH}}$) against the waterside chilled-water enthalpy balance across the cooling coil:

$$Q_{\text{waterside}} = \dot{m}_{\text{CHW}} \cdot c_{p,\text{water}} \cdot \left( T_{\text{CHW, return}} - T_{\text{CHW, supply}} \right) = \dot{m}_{\text{air}} \cdot \left( h_{\text{air, return}} - h_{\text{air, supply}} \right)$$

Under sensible-only dry-coil operation (when $T_{\text{CHW, supply}} > T_{\text{dp, hall}}$), the airside mass flow rate must agree with the waterside heat balance within $\pm 6.0\%$. Any larger discrepancy proves either scaled ultrasonic water flow meters or severe air-velocity maldistribution across the discharge plenum.

| CRAH Cross-Check Parameter | Waterside Measurement Method | Airside Measurement Method | Maximum Allowable Discrepancy |
| :--- | :--- | :--- | :--- |
| **Sensible Heat Duty ($Q_{\text{CRAH}}$)** | Ultrasonic flowmeter $\dot{m}_{\text{CHW}}$ + paired immersion RTDs | 16-point velocity traverse $\times \rho c_p (T_{\text{ret}} - T_{\text{sup}})$ | $\le \pm 6.0\%$ at steady state |
| **Supply Air Temperature ($T_{\text{sup}}$)** | Verified above coil leaving water temp ($T_{\text{CHW, in}} + \Delta T_{\text{app}}$) | Arithmetic mean of $S_1, S_2$ discharge plane RTDs | $\le \pm 0.4\,\text{K}$ vs BMS point |
| **Return Air Temperature ($T_{\text{ret}}$)** | Verified below coil leaving water limit | Area-weighted mean of $R_1, R_2, R_3$ intake grille RTDs | $\le \pm 0.5\,\text{K}$ vs BMS point |

## Decisions to record before test start

- The specific cooling units measured, noting supply opening points (S_1, S_2) and return opening points (R_1, R_2, R_3).
- The surveyed cabinet rows, recording vertical inlet probe readings at 0.3 m, 1.2 m, and 1.8 m.
- Sourcing of electrical heat: documented from active PDU meters, with the nameplate rating explicitly rejected.
- Physical coordinates of all field probes mapped to the numerical model grid.
- Measurement execution date compared against model CAD freeze date.

# 2. How a measurement is allowed to change the model

Model calibration is not the process of manipulating software settings until a simulated temperature contour matches a physical thermocouple reading. Calibration by curve-fitting produces an illusion of accuracy; it does not produce a predictive model of the data hall.

Under governing engineering standards—including **ASME V&V 20** (*Standard for Verification and Validation in Computational Fluid Dynamics and Heat Transfer*) and **ASHRAE Guideline 14**—calibration is the rigorous identification and correction of physical boundary input errors.

![CFD Verification and Validation Lifecycle](../figures/fig-01-cfd-audit-lifecycle.png)

## The Permitted Calibration Inputs

If your physical field measurements (from Sheet 1) diverge from the CFD simulation results, you are permitted to alter **only those physical parameters that you can touch, walk to, and independently verify in the room**.

**PERMITTED VS PROHIBITED MODEL CALIBRATIONS**

| PERMITTED CALIBRATION PARAMETERS (PHYSICAL INPUTS YOU CAN TOUCH) | PROHIBITED MATHEMATICAL MANIPULATIONS (ARBITRARY MODEL CURVE-FITTING) |
| :--- | :--- |
| • Missing blanking panel added | • Artificial turbulent viscosity multiplier adjusted |
| • Blocked floor tile free area % | • Fictitious boundary heat transfer coefficients |
| • Unsealed cable penetration hole | • Arbitrary server airflow multiplier factors |
| • Containment door gap modeled | • Inverting or shifting the temperature color scale bar |
| • Nameplate kW replaced by PDU kW | • Manually overwriting cell temperatures near hotspots |
| • CRAH supply T set to opening avg | • Unnamed 'fudge factors' applied to momentum source terms |

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

## Quantitative Model Calibration Criteria and Mesh Independence

A calibrated CFD model is not achieved by visually matching a red spot on a color plot to a warm cabinet in the hall. Visual pattern matching is subjective and easily manipulated by shifting the color legend scale by $2^\circ\text{C}$. Engineering calibration requires satisfying quantitative statistical error metrics across all $N$ surveyed physical benchmark locations simultaneously, paired with a documented Grid Convergence Index (GCI) proving that numerical discretization errors do not dominate the solution.

### Statistical Calibration Acceptance Thresholds

Let $T_{i,\text{sim}}$ and $T_{i,\text{meas}}$ denote the simulated and physically measured temperatures at benchmark sensor location $i \in \{1, \dots, N\}$, and let $\Delta T_{\text{hall}} = \bar{T}_{\text{return}} - \bar{T}_{\text{supply}}$ denote the characteristic hall temperature rise (typically $10.0\,\text{K}$ to $14.0\,\text{K}$). A model is contractually calibrated only when all four error metrics fall within the tolerances below:

$$\text{MAE}_T = \frac{1}{N} \sum_{i=1}^{N} \left| T_{i,\text{sim}} - T_{i,\text{meas}} \right| \le 1.5\,\text{K}$$

$$\text{RMSE}_T = \sqrt{\frac{1}{N} \sum_{i=1}^{N} \left( T_{i,\text{sim}} - T_{i,\text{meas}} \right)^2} \le 2.0\,\text{K}$$

$$\text{MBE}_T = \frac{1}{N} \sum_{i=1}^{N} \left( T_{i,\text{sim}} - T_{i,\text{meas}} \right) \in [-0.8\,\text{K}, \, +0.8\,\text{K}]$$

$$\varepsilon_{Q,\text{CRAH}} = \frac{\left| \sum Q_{\text{CRAH, sim}} - \sum Q_{\text{CRAH, meas}} \right|}{\sum Q_{\text{CRAH, meas}}} \le 5.0\%$$

If the Mean Bias Error ($\text{MBE}_T$) exceeds $\pm 0.8\,\text{K}$, the simulation has an unclosed global energy balance—meaning the total electrical heat entered into the model does not match the enthalpy removed by the CRAH boundary conditions ($\sum P_{\text{air}} \neq \sum \dot{m}_{\text{CRAH}} c_p \Delta T_{\text{CRAH}}$).

| Calibration Parameter | Permitted Physical Adjustment Source | Prohibited Unphysical "Knob Twisting" | Verification Audit Method |
| :--- | :--- | :--- | :--- |
| **Perforated Tile Loss Coefficient ($K$)** | Adjust to match balometer flow vs measured $\Delta P_{\text{plenum}}$ | Assigning arbitrary fixed velocities to individual tiles | Compare simulated tile $\Delta P$-$Q$ curve to manufacturer/balometer data |
| **Subfloor Blockage Porosity ($\gamma$)** | Mapped to physical cable tray & pipe dimensions under rows | Adding invisible baffle walls in empty underfloor zones | Inspect solver geometry wireframe with floor slab hidden |
| **Server Chassis Impedance ($R_{\text{rack}}$)** | Derived from OEM fan curve ($\Delta P$ vs CFM at measured $T_{\text{in}}$) | Forcing fixed exhaust temperature instead of heat flux $Q_{\text{air}}$ | Verify rack object is modeled as a power source + fan curve |
| **Containment Leakage Area ($A_{\text{leak}}$)** | Measured missing blanking U-slots, brush strips, door gaps | Altering global air thermal conductivity $k_t$ or gravity $\vec{g}$ | Audit solver turbulence model constants ($C_\mu = 0.09, \text{Pr}_t = 0.85$) |

### Grid Convergence Index (GCI) and Solver Residual Hygiene

Before accepting any simulation run—whether baseline or calibrated—the audit must verify numerical convergence. First, scaled iterative residuals must drop below $10^{-4}$ for continuity, momentum ($u, v, w$), and turbulence ($k, \varepsilon$), and below $10^{-6}$ for energy, while point monitors placed at the top intake ($1.8\,\text{m}$) of the three hottest racks must exhibit flat asymptotic stability ($\pm 0.1\,\text{K}$ over the final 200 iterations).

Second, if the computational mesh uses $500\,\text{mm}$ coarse hex cells across a $25\,\text{mm}$ unblanked server U-slot or a $15\,\text{mm}$ underfloor cable cutout, numerical diffusion smears out the high-velocity bypass jet entirely. Require the modeler to demonstrate mesh sensitivity across at least two grid densities ($N_{\text{coarse}}$ and $N_{\text{fine}}$ with refinement ratio $r = (N_{\text{fine}}/N_{\text{coarse}})^{1/3} \ge 1.3$), verifying that the Roache Grid Convergence Index at critical rack inlets satisfies:

$$\text{GCI}_{\text{fine}} = \frac{1.25 \cdot \left| \frac{T_{\text{fine}} - T_{\text{coarse}}}{T_{\text{fine}}} \right|}{r^p - 1} \le 2.0\%$$

## Turbulence Closure Sensitivity: Standard $k$-$\varepsilon$ vs. $k$-$\omega$ SST in Buoyant Plumes

When auditing a consultant's CFD solver setup on Sheet 1, the engineer must inspect which Reynolds-Averaged Navier-Stokes (RANS) turbulence model was selected to close the Reynolds stress tensor $-\rho \overline{u'_i u'_j}$. In data hall aerodynamics, flow regimes span forced-convection turbulent jets exiting floor grates ($\text{Re} > 35,000$) and buoyancy-driven natural convection plumes rising from hot aisles ($\text{Ri} = \text{Gr} / \text{Re}^2 \approx 0.5\text{--}3.0$):

$$\text{Ri} = \frac{g \beta \Delta T L_{\text{char}}}{v_{\text{char}}^2}$$

| RANS Turbulence Closure | Mathematical Transport Equations | Strengths in Whitespace CFD | Known Pathological Bias in Data Halls |
| :--- | :--- | :--- | :--- |
| **Indoor Zero-Equation / Algebraic** | $\mu_t = 0.03874 \rho v L_{\text{wall}}$ | Fast convergence on laptop meshes | Over-diffuses floor jets; underpredicts top-of-rack hotspots by $3\text{--}5\,\text{K}$ |
| **Standard $k$-$\varepsilon$ (Launder-Spalding)** | Turbulent kinetic energy $k$ & dissipation $\varepsilon$ | Robust industrial baseline for high-$\text{Re}$ jets | Overpredicts turbulent kinetic energy at impingement stagnation points |
| **Realizable $k$-$\varepsilon$ with Buoyancy** | Variable $C_\mu$ + full buoyancy generation $G_b$ | Accurately captures round/slot tile jet spreading rates | Preferred baseline for raised-floor & containment audits |
| **$k$-$\omega$ SST (Menter)** | Blends near-wall $k$-$\omega$ with free-stream $k$-$\varepsilon$ | Resolves adverse pressure gradients & separation | Requires fine boundary mesh ($y^+ \le 5$); diverges on poor hex grids |

If a consultant switches turbulence models between the baseline run and the proposed remedy run, the comparison on Sheet 2 is invalid. The exact same turbulence closure and buoyancy terms ($G_b$) must be locked across all comparative runs.

## Auditing Porous-Media Server Chassis Impedance Curves ($\Delta P$ vs. $Q$)

In commercial CFD solvers, a 42U server cabinet is modeled as a lumped porous-media volume with an inertial resistance factor $\beta_i$ and viscous resistance $\alpha_i$:

$$\Delta P_{\text{chassis}} = \left( \alpha_i \mu v + \frac{1}{2} \beta_i \rho v^2 \right) L_{\text{chassis}}$$

If the modeler leaves internal server fan curves disabled or sets chassis porosity to $100\%$ open space, the simulated cold-aisle air flows lazily through the rack at uniform velocity rather than being actively drawn by server axial fans ($85\text{--}120\,\text{CFM/kW}$). Sheet 1 requires verifying that every active cabinet U-space in the model carries an active fan mass-flow boundary coupled to its measured PDU electrical heat dissipation.

### Detecting Over-Tuned Local Artificial Resistance Patches

A common deceptive practice when a CFD model fails calibration at a specific cabinet (e.g., Rack `R02-08`) is inserting an invisible local momentum sink or artificial baffle plate directly in front of `R02-08` inside the software domain so that the local temperature rises to match the field thermometer. To catch this, require the consultant to export a complete **Object & Resistance Table** directly from the solver database listing the $(x, y, z)$ bounding box, porosity $\gamma$, and loss coefficient $K$ of every sub-volume in the model. Any object in the solver table that does not correspond to a physical obstruction verified during the floor walk disqualifies the calibration.

## Decisions to record before test start

- The full inventory of physical parameters modified between Pass 1 and Pass 2.
- The calculated statistical error metrics (MAE, RMSE, NMBE, and $Δ_\max$).
- Confirmation of whether the model satisfied the statistical validation gates.
- Formal marking of the report as either "CALIBRATED AGAINST PHYSICAL FACILITY" or "NOT CALIBRATED".

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

## Quantitative Air-Management Indices: SHI, RHI, RCI, and Capture Index

Reading a CFD report requires translating qualitative 3D streamline ribbons into dimensionless thermodynamic performance indices. Industry standards—including ASHRAE TC 9.9 and Uptime Institute whitespace metrics—evaluate airflow separation using four coupled mathematical indices that expose whether a cooling problem is caused by insufficient cold air supply (starvation) or parasitic mixing of hot exhaust (recirculation).

### 1. Supply Heat Index (SHI) and Return Heat Index (RHI)

Defined by Sharma et al. and adopted across enterprise data hall audits, the **Supply Heat Index ($\text{SHI}$)** measures the fraction of total rack heat pickup that occurs *before* the cooling air ever enters the server intake bezel due to hot-aisle infiltration, over-the-top roll, or missing blanking panels:

$$\text{SHI} = \frac{\delta Q}{Q + \delta Q} = \frac{\sum_{j} \sum_{i} \dot{m}_{i,j}^{\text{rack}} c_p \left( T_{\text{in}, i,j}^{\text{rack}} - T_{\text{ref}}^{\text{supply}} \right)}{\sum_{j} \sum_{i} \dot{m}_{i,j}^{\text{rack}} c_p \left( T_{\text{out}, i,j}^{\text{rack}} - T_{\text{ref}}^{\text{supply}} \right)}$$

Conversely, the **Return Heat Index ($\text{RHI}$)** measures the fraction of cooling air that actually absorbs server heat rather than bypassing directly from the floor tiles into the CRAH return grilles:

$$\text{RHI} = \frac{Q}{Q + \delta Q} = 1 - \text{SHI}$$

In a well-sealed cold-aisle or hot-aisle containment architecture, $\text{SHI}$ must satisfy $\text{SHI} \le 0.15$ (and $\text{RHI} \ge 0.85$). When $\text{SHI} > 0.25$, lowering the CRAH supply water setpoint is a waste of chiller energy because more than a quarter of the cooling stream is being contaminated by hot exhaust recirculation before reaching the silicon.

### 2. Rack Cooling Index ($\text{RCI}_{\text{HI}}$ and $\text{RCI}_{\text{LO}}$)

While $\text{SHI}$ evaluates aerodynamic mixing, the **Rack Cooling Index ($\text{RCI}$)** evaluates compliance against the ASHRAE TC 9.9 Recommended and Allowable thermal envelopes across all $N$ rack intake nodes:

$$\text{RCI}_{\text{HI}} = \left[ 1 - \frac{\sum_{i=1}^{N} \max\left(0, \, T_{\text{in}, i} - T_{\text{max, rec}}\right)}{N \cdot \left( T_{\text{max, allow}} - T_{\text{max, rec}} \right)} \right] \times 100\%$$

$$\text{RCI}_{\text{LO}} = \left[ 1 - \frac{\sum_{i=1}^{N} \max\left(0, \, T_{\text{min, rec}} - T_{\text{in}, i}\right)}{N \cdot \left( T_{\text{min, rec}} - T_{\text{min, allow}} \right)} \right] \times 100\%$$

For ASHRAE Class A1/A2 whitespace ($T_{\text{max, rec}} = 27.0^\circ\text{C}$, $T_{\text{max, allow}} = 32.0^\circ\text{C}$ for A1 or $35.0^\circ\text{C}$ for A2), an auditable hall requires $\text{RCI}_{\text{HI}} \ge 96.0\%$. If a vendor report claims "average room temperature is $23.5^\circ\text{C}$" while four end-of-row racks sit at $31.2^\circ\text{C}$, $\text{RCI}_{\text{HI}}$ immediately drops and exposes the localized violation.

| Aerodynamic Diagnostic Metric | Mathematical Formula | Target Commissioning Pass Band | Physical Failure Mode Indicated by Violation |
| :--- | :--- | :--- | :--- |
| **Supply Heat Index ($\text{SHI}$)** | $\delta Q / (Q + \delta Q)$ | $\le 0.15$ (Contained) / $\le 0.20$ (Open) | Hot exhaust roll-over, unblanked U-slots, negative aisle $\Delta P$ |
| **Return Heat Index ($\text{RHI}$)** | $Q / (Q + \delta Q) = 1 - \text{SHI}$ | $\ge 0.85$ (Contained) / $\ge 0.80$ (Open) | Excessive tile supply flow bypassing racks directly to return |
| **Rack Cooling Index High ($\text{RCI}_{\text{HI}}$)** | $1 - \frac{\sum (T_i - T_{\text{rec}})_+}{N(T_{\text{allow}} - T_{\text{rec}})}$ | $\ge 96.0\%$ ($100\%$ ideal) | Localized top-of-rack or end-of-row thermal excursions |
| **Flow Provisioning Ratio ($\Phi$)** | $\sum Q_{\text{tile, aisle}} / \sum Q_{\text{rack, demand}}$ | $1.05 \le \Phi \le 1.25$ | $\Phi < 1.0$: Severe aisle starvation; $\Phi > 1.35$: Fan energy waste |
| **Containment Differential ($\Delta P_{\text{CAC}}$)** | $P_{\text{cold\_aisle}} - P_{\text{hot\_aisle}}$ | $+1.5\,\text{Pa} \le \Delta P_{\text{CAC}} \le +5.0\,\text{Pa}$ | $\Delta P < 0$: Hot air sucked into cold aisle; $\Delta P > 10\,\text{Pa}$: Door force hazard |

## Auditing Capture Index ($\text{CI}$) and Containment Pressurization Balance

In addition to $\text{SHI}$ and $\text{RCI}$, modern whitespace audits evaluate the **Cold-Aisle Capture Index ($\text{CI}_{\text{cold}}$)** and **Hot-Aisle Capture Index ($\text{CI}_{\text{hot}}$)** using passive tracer-species transport equations in the CFD solver:

$$\text{CI}_{\text{cold}, i} = \frac{\sum_{t} \dot{m}_{i, t}^{\text{tile}\to\text{rack}}}{\dot{m}_i^{\text{rack}}}, \qquad \text{CI}_{\text{hot}, i} = \frac{\sum_{c} \dot{m}_{i, c}^{\text{rack}\to\text{CRAH}}}{\dot{m}_i^{\text{rack}}}$$

 specifically:
- $\text{CI}_{\text{cold}, i}$ is the mass fraction of air ingested by Rack $i$ that originated directly from the dedicated cold-aisle supply tiles (target $\ge 92\%$).
- $\text{CI}_{\text{hot}, i}$ is the mass fraction of hot exhaust discharged by Rack $i$ that is captured directly by the return plenum or CRAH intakes without escaping into the room (target $\ge 92\%$).

### Mass-Flow Balance and Door-Opening Force Limits in Contained Aisles

When sizing cold-aisle containment (CAC) or hot-aisle containment (HAC), total CRAH supply volumetric flow ($\sum Q_{\text{CRAH}}$) must exceed total server fan demand ($\sum Q_{\text{server}}$) by a controlled positive over-provisioning margin ($\Delta Q_{\text{excess}} = 5\%$ to $15\%$) so that air leaks *out* of the cold aisle rather than infiltrating *in*:

$$\Delta P_{\text{CAC}} = \frac{\rho_{\text{air}}}{2} \left( \frac{\sum Q_{\text{CRAH}} - \sum Q_{\text{server}}}{C_d \cdot A_{\text{containment\_leak}}} \right)^2 \in [+1.5\,\text{Pa}, \, +5.0\,\text{Pa}]$$

However, if a tight containment enclosure is over-pressurized beyond $+12.0\,\text{Pa}$ to $+15.0\,\text{Pa}$, the pneumatic force exerted across a $2.1\,\text{m} \times 1.0\,\text{m}$ hinged containment door ($F = \Delta P \cdot A_{\text{door}} \approx 30\,\text{N}$) prevents the mechanical door closer from latching shut, or violates NFPA 101 life-safety egress force limits! Always verify both the lower bound ($\ge +1.5\,\text{Pa}$) and upper bound ($\le +8.0\,\text{Pa}$) during the physical walk.

## Evaluating Thermal Stratification Gradients ($\partial T / \partial z$) in High-Bay Whitespace

In modern hyperscale data halls with $4.5\,\text{m}$ to $6.0\,\text{m}$ slab-to-ceiling heights and overhead hot-aisle return plenums, vertical temperature stratification $\partial T / \partial z$ governs whether hot exhaust air stays buoyant above the rack line or mixes downward into the cold aisle. The dimensionless Archimedes / Richardson number across the aisle height $H_{\text{rack}}$ must be evaluated at the lowest turndown CRAH fan speed to confirm that buoyancy forces do not stall cold supply jets before they reach the $1.8\,\text{m}$ top server intake elevation.

| Rack Elevation Zone | Standard Measurement Height | Typical Dominant Aerodynamic Mechanism | Primary Diagnostic Signature of Failure |
| :--- | :--- | :--- | :--- |
| **Lower Zone (U01–U14)** | $z = 0.3\,\text{m}$ | High-momentum floor tile jet & Venturi entrainment | $T_{0.3\text{m}} > T_{\text{sup}} + 3\,\text{K}$ indicates subfloor Venturi reverse induction |
| **Middle Zone (U15–U30)** | $z = 1.2\,\text{m}$ | Core horizontal cross-flow into server fan array | $T_{1.2\text{m}} > T_{0.3\text{m}} + 2\,\text{K}$ indicates unblanked adjacent U-slot bypass |
| **Upper Zone (U31–U48)** | $z = 1.8\,\text{m}$ | Buoyant exhaust plume roll-over & roof curtain leakage | $T_{1.8\text{m}} > T_{0.3\text{m}} + 5\,\text{K}$ indicates aisle starvation ($\Phi < 1.0$) or roof gap |

## Decisions to record before test start

- Verification that underfloor plenum static regain and tile momentum were physically resolved.
- Sourcing of aisle containment leakage coefficients and door delta-P.
- The convective air heat fraction assigned to liquid racks (verifying ≈ 20% convective air split).
- Audit of the six mandatory input blocks.
- Verification that solver residuals satisfied continuity < 10^{-4} and energy < 10^{-6}.

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

**ASHRAE CLASS A1 THERMAL ENVELOPE AUDIT**

| ENVIRONMENTAL PARAMETER | RECOMMENDED ENVELOPE | ALLOWABLE ENVELOPE | AUDIT VIOLATION LIMIT |
| :--- | :--- | :--- | :--- |
| Dry-Bulb Temperature Dew Point Temperature Maximum Relative Humidity | 18.0°C to 27.0°C 5.5°C to 15.0°C 60% RH | 15.0°C to 32.0°C -12.0°C to 17.0°C 80% RH | > 32.0°C or < 15.0°C > 17.0°C (Condensation) > 80% RH |

### The Rack Cooling Index (RCI)
To summarize row-wide compliance mathematically, the report should compute the **Rack Cooling Index**:
- **RCI_HI (High-Temperature Compliance)**: Measures the percentage of intake points operating within the Recommended maximum (27.0°C) without any points breaching the Allowable ceiling (32.0°C). Target: RCI_HI ≥ 95% (Ideal: 100%).
- **RCI_LO (Low-Temperature Compliance)**: Measures protection against overcooling below the minimum floor (18.0°C). Target: RCI_LO ≥ 95%.

## The Palette Manipulation Trap

The primary mechanism of visual deception in CFD reporting is the arbitrary manipulation of the temperature color contour scale:
- A modeler who wishes to present a dangerously overheated room as healthy can simply adjust the palette upper bound to 45.0°C. On that scale, a server intake operating at 30.0°C (severely overheated) renders in a calming blue-green hue.
- Conversely, a modeler seeking to justify an unnecessary cooling expansion can set the palette upper bound to 24.0°C. On that scale, a healthy intake at 23.5°C renders in an alarming fiery red.

**The Color Scale Audit Law**: Never evaluate a CFD report from color contours alone. Always extract the numerical probe values from cutting planes, and insist that all comparative plots be normalized to an identical, fixed scale (15.0°C to 35.0°C).

## Quantitative Comparative Ranking of Physical Remedy Families

When using a calibrated CFD model to select an engineering remedy for an overheating row, candidate interventions must be evaluated using a standardized marginal cost-per-degree reduction metric and worst-node thermal recovery ($\Delta T_{\text{peak}}$). Never authorize a high-capital mechanical plant expansion (such as adding a new CRAH unit or lowering chilled-water supply temperature across the entire central plant) before modeling and exhausting zero-energy aerodynamic sealing remedies.

### The Airflow Remedy Hierarchy and Orifice Leakage Elimination

Underfloor and containment bypass leakage is governed by the sharp-edged orifice equation. Across every unsealed cable cutout, missing floor tile brush grommet, or unblanked 1U server slot of area $A_{\text{leak}}$, the parasitic volumetric flow rate $Q_{\text{leak}}$ lost from the pressurized plenum or aisle is:

$$Q_{\text{leak}} = C_d \cdot A_{\text{leak}} \cdot \sqrt{\frac{2 \Delta P}{\rho_{\text{air}}}}$$

At a standard raised-floor static pressure of $\Delta P = 20.0\,\text{Pa}$ ($C_d \approx 0.65, \rho = 1.18\,\text{kg/m}^3$), a single unsealed $150\,\text{mm} \times 300\,\text{mm}$ ($0.045\,\text{m}^2$) rear cable cutout under a cabinet leaks:

$$Q_{\text{leak}} = 0.65 \times 0.045\,\text{m}^2 \times \sqrt{\frac{2 \times 20.0}{1.18}} = 0.170\,\text{m}^3\text{/s} \approx 360\,\text{CFM}$$

Across a 20-rack row, twenty unsealed rear cable cutouts waste $7,200\,\text{CFM}$—the entire cooling output of a $60\,\text{kW}$ CRAH unit—blowing conditioned supply air straight into the hot exhaust chimney before it ever touches a server intake!

| Remedy Priority Tier | Physical Intervention Family | Typical Peak Inlet Reduction ($\Delta T_{\text{peak}}$) | Parasitic Fan/Chiller Power Impact | Mandatory Post-Install Field Verification |
| :--- | :--- | :--- | :--- | :--- |
| **Tier 1 (Zero Energy)** | Install 1U/2U snap-in blanking panels across all empty rack spaces | $-2.5\,\text{K}$ to $-6.0\,\text{K}$ at adjacent intakes | $0.0\,\text{kW}$ (reduces server fan speed) | Visual zero-daylight check + 3-point intake RTD re-walk |
| **Tier 2 (Plenum Sealing)** | Brush grommets & air-tight pillows on all underfloor cable cutouts | Increases aisle tile $\Delta P$ by $+3$ to $+8\,\text{Pa}$ | Allows $-5\%$ to $-12\%$ CRAH VFD reduction | Subfloor static $\Delta P$ manometer check & balometer re-read |
| **Tier 3 (Impedance Tuning)** | Swap $25\%$ vs $50\%$ perforated tiles & adjust subfloor dampers | Eliminates end-of-row Venturi starvation ($-3.0\,\text{K}$) | Neutral ($0.0\,\text{kW}$) | Capture-hood balometer traverse along entire row |
| **Tier 4 (Containment)** | End-of-row self-closing doors & roof containment baffles | Reduces $\text{SHI}$ from $>0.30$ to $<0.12$ | Enables $+2.0\,\text{K}$ chilled water setpoint raise | Differential pressure $\Delta P_{\text{CAC}} \in [+1.5, +4.0\,\text{Pa}]$ |
| **Tier 5 (Last Resort)** | Increase CRAH VFD fan speed or lower CHW supply setpoint | Masks leakage via brute-force over-blowing | $+15\%$ to $+40\%$ cubic fan power ($P \propto N^3$) | Requires written sign-off proving Tiers 1–4 were exhausted |

### The Fan Affinity Law Penalty of Brute-Force Over-Blowing

When a CFD consultant recommends increasing CRAH fan speed from $75\%$ to $95\%$ instead of sealing $0.8\,\text{m}^2$ of containment and floor cutouts, the facility pays a cubic electrical penalty governed by the fan affinity laws:

$$\frac{Q_2}{Q_1} = \frac{N_2}{N_1}, \qquad \frac{\Delta P_2}{\Delta P_1} = \left( \frac{N_2}{N_1} \right)^2, \qquad \frac{P_{\text{fan}, 2}}{P_{\text{fan}, 1}} = \left( \frac{N_2}{N_1} \right)^3$$

Increasing fan speed by $26.7\%$ ($95 / 75 = 1.267$) increases fan shaft power consumption by $(1.267)^3 = 2.03\times$ ($+103\%$ more electrical power), which simultaneously adds extra fan motor heat straight back into the supply air stream. Sheet 2 therefore requires testing passive geometric sealing (Tiers 1–4) in the model before any active mechanical speed or temperature change is considered.

## Economic Capital Avoidance: Quantifying Chiller Lift vs. Aerodynamic Sealing

Every degree Kelvin of cold-aisle hot-air contamination ($\Delta T_{\text{recirc}} = T_{\text{intake}} - T_{\text{supply}}$) forces the facility operator to depress the central chilled-water supply setpoint ($T_{\text{CHW, sup}}$) by an equivalent margin to keep server intakes below the $27.0^\circ\text{C}$ ASHRAE recommended line. Lowering $T_{\text{CHW, sup}}$ increases the thermodynamic compressor lift across the central centrifugal chillers and drastically reduces hours of free waterside economizer operation:

$$\text{COP}_{\text{Carnot}} = \frac{T_{\text{evap}}}{T_{\text{cond}} - T_{\text{evap}}}, \qquad \frac{\Delta P_{\text{chiller}}}{\Delta T_{\text{CHW, sup}}} \approx -2.8\% \text{ to } -3.5\% \text{ per K}$$

Across a $20\,\text{MW}$ data center campus operating at a mechanical cooling load factor of $0.18$, eliminating a $4.0\,\text{K}$ containment bypass recirculation defect via $\$12,000$ of blanking panels and subfloor grommets allows raising the chilled-water supply temperature by $+4.0\,\text{K}$. This reduces annual chiller compressor energy by roughly $11\%$ to $14\%$—saving over $3.5\,\text{GWh/year}$ ($\approx \$350,000/\text{year}$ in recurring OPEX) while unlocking $1,400+$ additional hours of compressor-free waterside economization.

## Verifying Post-Remedy Stability Across Turndown and Partial-Load Regimes

An airflow remedy selected on Sheet 2 must be verified not only at $100\%$ peak hall load, but also at $30\%$ partial-load turndown when variable-frequency CRAH fans slow down to their minimum static-pressure floor ($35\%\text{--}40\%$ speed). At low fan speeds, underfloor plenum static pressure drops from $20\,\text{Pa}$ to $5\,\text{Pa}$, while server internal fans continue drawing full volumetric airflow whenever compute bursts occur. Always run a second comparative check on Sheet 2 at minimum CRAH VFD turndown to guarantee that $\Phi = \sum Q_{\text{CRAH}} / \sum Q_{\text{server}}$ never falls below $1.05$.

### Preventing Control-Loop Hunting Between CRAH Differential Pressure Sensors and Server Fans

When containment remedies (Tier 4) are installed, the location of the BMS static differential pressure tubes ($\Delta P_{\text{ctrl}}$) controlling CRAH VFD speed determines whether the aisle remains stable or oscillates violently. If a single $\Delta P$ tube is mounted next to a hinged aisle door or directly above a high-velocity floor grate, opening the door or ramping a single NVL72 rear fan wall causes the CRAH VFD loop to hunt between $40\%$ and $100\%$ speed every $90$ seconds. Specify at least three manifolded or median-selected $\Delta P_{\text{CAC}}$ sensors positioned at the quarter-points ($L/4, L/2, 3L/4$) of each contained aisle at $1.5\,\text{m}$ height, damped with a $10$-second moving-average filter.

## Decisions to record before test start

- The single permitted decision domain selected for this report, with the other three marked as not applicable.
- The specific edition of ASHRAE TC 9.9 cited in the project specification.
- Verification that dimensionless metrics (SHI ≤ 0.15, CI ≥ 90%) are reported.
- Confirmation that color contour scales are normalized to fixed numerical limits.

# 5. Sentences you do not write

A CFD simulation report will invariably present conclusions and recommendations drafted by the model author. Most of these sentences are not yours to sign.

As a Commissioning Lead, technical auditor, or facility engineer, your professional duty is to maintain strict evidentiary standards. You must identify speculative or unverified statements in the consultant's draft and formally strike them from the executive summary before the report is accepted.

![CFD Report Decision and Refusal Matrix](../figures/fig-07-cfd-decision-and-refusal-matrix.png)

## The Four Primary Refused Statements

**PROHIBITED CFD REPORT STATEMENTS**

| PROHIBITED STATEMENT IN DRAFT | MANDATORY AUDIT REFUSAL RATIONALE & REMEDIATION |
| :--- | :--- |
| 1. "The data hall has passed commissioning." | REFUSED. CFD is a mathematical simulation, not a physical test. Commissioning pass/fail is proven exclusively by Level 5 physical load-bank testing (Book 03). Strike sentence. |
| 2. "Add 100 kW of cooling capacity to eliminate the hotspot." | REFUSED. An untested proposal is not an engineering result. Must be modeled as a verified rerun script with the new unit added. If not rerun, label: "PROPOSAL - NOT DEMONSTRATED". |
| 3. "Compute servers will train AI workloads reliably." | REFUSED. CFD simulates whitespace air temperatures; it does not model silicon junction temperatures, throttling, or NVLink. Strike sentence. Limit claim strictly to intake air envelope. |
| 4. "Streamline velocity confirms airflow rate is 450 L/s." | REFUSED. A streamline shows flow direction, not mass flux. Demand numerical surface integral or physical hood data. |

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

## Forensic Detection of Manipulated CFD Contours and N-1 Failure Modeling

In commercial commissioning disputes, CFD reports are frequently formatted to make a marginal or failing whitespace design appear compliant. Beyond verbal over-claims like *"the hall is optimized,"* the reviewing engineer must audit the visual and numerical artifacts of the report to detect four classic manipulation techniques.

### 1. Horizontal Slice Plane Elevation Cherry-Picking

A standard 42U–48U server rack stands $2.0\,\text{m}$ to $2.25\,\text{m}$ tall. Buoyancy-driven hot exhaust air naturally stratifies near the ceiling and rolls over the top of uncontained rows, or leaks through roof brush gaps at $1.7\,\text{m}$ to $2.0\,\text{m}$ elevation. If a consultant presents only a single horizontal temperature contour slice cut at $z = 1.0\,\text{m}$ (waist height), the plot will show a uniform blue/green cold aisle ($22^\circ\text{C}$) while servers mounted at U38–U45 ($z = 1.85\,\text{m}$) are ingesting $33.5^\circ\text{C}$ recirculated exhaust air.

$$T_{\text{slice}}(z = 1.0\,\text{m}) \ll \max_{z \in [0.2, 2.0]} T_{\text{bezel}}(x, y, z)$$

Refuse any CFD package that omits horizontal temperature slices at $z = 1.8\,\text{m}$ (Top Intake) or omits front-bezel surface temperature maps across every cabinet row.

### 2. Steady-State N-1 CRAH Failure vs. Transient Thermal Flywheel Claims

A simulation labeled "N-1 Cooling Failure Pass" must state which specific CRAH unit was tripped and whether the solver ran to a true steady-state equilibrium or was halted after an arbitrary $60$-second transient window. When a CRAH unit trips:
1. Its motorized isolation damper must close (or backdraft reverse-flow through the stopped fan wheel must be explicitly modeled as an open bypass orifice inside the CRAH cabinet).
2. If the modeler deletes the tripped CRAH opening as a solid wall without verifying that motorized backdraft dampers are physically installed on site, the model hides the catastrophic subfloor pressure collapse caused by supply air short-circuiting backwards up through the idle CRAH unit!

$$Q_{\text{backdraft}} = C_d \cdot A_{\text{CRAH\_wheel}} \cdot \sqrt{\frac{2 \left( P_{\text{subfloor}} - P_{\text{return}} \right)}{\rho_{\text{air}}}}$$

| CFD Report Defect / Manipulation | Visual Symptom in Submitted PDF | Underlying Numerical Mechanism | Mandatory Refusal & Remediation Action |
| :--- | :--- | :--- | :--- |
| **Mid-Height Slice Selection** | Only $z = 1.0\,\text{m}$ plan view shown; no $1.8\,\text{m}$ slice | Masks buoyancy stratification and top-of-rack roll-over | Demand horizontal cuts at $0.3\,\text{m}, 1.2\,\text{m}, 1.8\,\text{m}$ + rack bezel maps |
| **Truncated Color Scale Bar** | Legend capped at $35^\circ\text{C}$ (green) or $40^\circ\text{C}$ (red) | Compresses ASHRAE $27^\circ\text{C}$ threshold into cool blue/cyan | Require discrete threshold contour step at exact $27.0^\circ\text{C}$ limit |
| **Sealed Idle CRAH in N-1 Run** | N-1 subfloor static pressure remains uniform | Stopped CRAH modeled as solid wall without physical damper | Model open backdraft resistance unless physical damper is witnessed |
| **Volume-Averaged Rack Metric** | Table lists "Mean Rack Temp" instead of peak node | Averages cold bottom intake ($19^\circ\text{C}$) with hot top ($32^\circ\text{C}$) | Reject table; require $\max(T_{0.3}, T_{1.2}, T_{1.8})$ per cabinet ID |

## Auditing Boundary Condition Completeness in Submitted Solver Decks

When a CFD consultant submits a PDF report without providing the solver boundary-condition summary table, the reviewer cannot verify whether the laws of conservation of mass and energy were respected. Require every CFD submission to include the **Global Boundary Conservation Ledger** directly in the report preface:

$$\sum_{k=1}^{N_{\text{CRAH}}} \dot{m}_{\text{CRAH}, k} \cdot c_p \cdot \left( T_{\text{return}, k} - T_{\text{supply}, k} \right) = \sum_{j=1}^{N_{\text{racks}}} Q_{\text{air}, j} + Q_{\text{envelope}} + Q_{\text{lighting}} \quad (\pm 1.0\%)$$

| Mandatory Solver Deck Disclosure | Required Engineering Unit | What a Missing or Mismatched Value Proves |
| :--- | :--- | :--- |
| **Total Domain Mesh Cell Count** | Millions of cells ($\ge 5\text{--}15\,\text{M}$ per hall) | $< 500\text{k}$ cells indicates a coarse cartoon grid incapable of resolving U-slots |
| **Sum of Active Rack Heat Sources ($\sum Q_{\text{air}}$)** | $\text{kW}$ (Sensible air fraction only) | Must match active PDU kW minus CDU liquid heat ($P_{\text{elec}} - Q_{\text{liq}}$) |
| **Sum of CRAH Enthalpy Removal ($\sum Q_{\text{CRAH}}$)** | $\text{kW}$ ($\sum \dot{m} c_p \Delta T$) | If $\left|\sum Q_{\text{CRAH}} - \sum Q_{\text{air}}\right| > 2\%$, the solver never converged thermally |
| **Server Flow Law ($Q_{\text{server}}$ vs $T_{\text{in}}$)** | $\text{CFM/kW}$ curve (e.g., $85 \to 125\,\text{CFM/kW}$) | Fixed-flow server models miss thermal fan ramp-up and aisle starvation |

## Rejecting Extrapolated "Phase 2" Claims From Unreconciled Phase 1 Geometries

Contractors frequently attempt to reuse a Phase 1 CFD report (calibrated when the hall held $20$ cabinets at $5\,\text{kW}$) to certify a Phase 2 expansion adding $80$ dense AI cabinets at $40\text{--}120\,\text{kW}$ without re-benchmarking the subfloor plenum or primary chilled-water hydraulic loop. Nonlinear fluid friction ($\Delta P \propto Q^2$) guarantees that tripling volumetric airflow increases plenum and duct pressure losses by $900\%$. Any expansion exceeding $+20\%$ of benchmarked hall thermal load requires a fresh Sheet 1 physical baseline walk.

### Summary of Automatic Refusal Triggers for Whitespace Simulation Submittals

1. **Missing Physical Benchmark Walk**: No Sheet 1 field readings attached for an existing hall.
2. **Nameplate Power Inflation**: Heat sources assigned from PSU nameplate ratings instead of active metered PDU kilowatts.
3. **Uncompensated Liquid Split**: Hybrid liquid/air racks modeled without subtracting measured CDU enthalpy ($Q_{\text{liquid}}$).
4. **Slice Plane Omission**: Missing horizontal temperature contours at $z = 1.8\,\text{m}$ (Top Intake) or missing front-bezel temperature maps.
5. **Unverified N-1 Damper Assumption**: Tripped CRAH units modeled as sealed walls without witnessed motorized backdraft dampers.

## Decisions to record before test start

- The comprehensive list of speculative sentences struck from the consultant's draft.
- Documentation that all proposed physical remedies are accompanied by formal rerun scripts.
- Formal reaffirmation that the CFD report does not replace Book 03 physical load-bank testing.
- Sign-off by the Commissioning Lead that the executive summary contains only authorized findings.

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

# 7. What this book does not own

This field guide will inevitably be misused by individuals seeking an all-inclusive textbook on computational fluid dynamics. Establish strict professional boundaries here.

A field audit method maintains integrity only when its boundaries are sharply drawn. Expanding this guide into software solver programming or mechanical design dilutes its authority.

**EXPLICIT NEGATIVE SCOPE BOUNDARIES**

| WHAT THIS BOOK OWNS | WHAT THIS BOOK CANNOT AND DOES NOT OWN |
| :--- | :--- |
| • Field multi-point calibration | • Commercial CFD solver algorithms, source code, or GUI menus |
| • Quantitative error metrics (MAE) | • Book 01 Scope: Load-bank design, manufacturing, and FAT |
| • The 6 mandatory input blocks | • Book 02 Scope: Telemetry anomaly algorithms (FLOC/Focus) |
| • Four permitted decision domains | • Book 03 Scope: Physical Level 5 load-bank floor testing |
| • Refusal of color-map speculation | • Silicon Physics: Chip junction temps ($T_j$), NVLink, AI ops |
| • The two master audit sheets | • Facility Design: Architectural, structural, and central MEP |
| • ASHRAE TC 9.9 compliance audit | • Next Facility: Copying room-specific averages across halls |

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

## Boundary Between Aerodynamic Modeling and Safety-Critical Facility Systems

A recurring governance failure in data center design reviews is allowing a whitespace CFD report to encroach upon life-safety, fire-suppression, or liquid-loop hydraulic engineering domains. Because CFD software packages can render smoke plumes, pipe networks, and structural beams in the same 3D viewport, project teams are frequently tempted to treat a thermal airflow consultant's model as a multi-disciplinary certification.

### Explicit Domain Exclusions and Required Specialist Instruments

1. **Clean-Agent Fire Suppression Hold-Time & Acoustic Nozzle Overpressure**:
   When a gaseous clean-agent system (such as FK-5-1-12 / Novec 1230 or IG-541 Inergen) discharges into a data hall, two physical phenomena govern survival: peak acoustic sound pressure level ($\text{SPL} < 120\,\text{dB}$ at hard-disk trays to prevent head crashes) and lower-layer concentration hold time ($t_{\text{hold}} \ge 10\,\text{minutes}$ per NFPA 2001). Standard whitespace thermal CFD does not resolve multiphase nozzle flashing, acoustic shock waves, or room envelope hydrostatic pressure relief damper dynamics. Clean-agent certification requires a physical NFPA 2001 Door Fan Enclosure Integrity Test and listed OEM hydraulic flow calculation software—never a general-purpose thermal CFD model.
2. **Secondary Liquid Cooling Manifold Cavitation and Water Hammer**:
   3D room-level CFD models treat liquid-cooled racks as simplified lumped heat sinks ($Q_{\text{air}} = P_{\text{elec}} - Q_{\text{liquid}}$). They do not solve 1D acoustic wave propagation (Joukowsky water hammer $\Delta P = \rho c \Delta v$) or local vapor pressure cavitation across Danfoss FD83 quick disconnects and modulating trim valves. Those hydraulic boundaries belong exclusively to Volume 01 (*Design and Build a Liquid Load Bank*), Volume 02 (*Read and Use Load Bank Data*), and Volume 03 (*Finish a Liquid Cooling Verification*).
3. **Structural Raised-Floor Pedestal Buckling Under Heavy AI Racks**:
   Cutting perforated tile openings or routing large chilled-water headers under a raised floor alters stringer continuity, while an NVL72-class liquid rack imposes point loads exceeding $1,800\,\text{kg}$ to $2,500\,\text{kg}$. Moving floor tiles in a CFD model is a mouse click; moving tiles or cutting stringers in a physical hall requires a licensed structural engineer's stamped pedestal axial and seismic lateral load calculation.

| Engineering Question | Why Whitespace Thermal CFD Cannot Answer It | Governing Physical Test or Volume |
| :--- | :--- | :--- |
| **Will clean-agent gas hold concentration for 10 min?** | RANS thermal mesh omits micro-cracks & hydrostatic relief dampers | NFPA 2001 Physical Door Fan Integrity Test |
| **Will CDU trip cause secondary loop water hammer?** | Incompressible 3D air solver omits fluid acoustic wave speed $c$ | Volume 01 & Volume 03 Transient Valve Closure Test |
| **Are BMS intake temperature alarms reliable?** | CFD assumes static boundary inputs; ignores sensor ADC/clock faults | Volume 06 (*When a Monitor May Speak*) Forced-Failure Test |
| **Is the hall ready for commercial operations handover?** | A calibrated simulation is still a model, not an integrated plant test | Volume 07 (*Refuse the Handover*) Gatekeeper Protocol |

## Transient Thermal Ride-Through and UPS-Backed Pump/Fan Sequencing

While steady-state RANS CFD cannot certify clean-agent gas hold times or pipe water hammer, operators frequently ask whether a 3D unsteady (transient) CFD run can certify the hall's **Thermal Ride-Through Time ($\tau_{\text{ride}}$)** during a complete mechanical power outage. Even transient CFD must be treated with extreme caution unless internal server thermal mass ($M_{\text{copper/aluminum}} c_p$) and CRAH fan coast-down inertia ($J \omega$) are physically benchmarked.

For rapid operational gating, first-principles lumped-capacitance energy balance provides a transparent, auditable lower bound on whitespace air ride-through time before intake air reaches $T_{\text{max, allow}} = 32.0^\circ\text{C}$:

$$\tau_{\text{ride, air}} = \frac{V_{\text{cold\_aisle}} \cdot \rho_{\text{air}} \cdot c_{p,\text{air}} \cdot \left( T_{\text{max, allow}} - T_{\text{initial}} \right)}{Q_{\text{air, hall}}}$$

In a contained cold aisle of volume $V_{\text{cold\_aisle}} = 120\,\text{m}^3$ serving $400\,\text{kW}$ of air-cooled IT load ($T_{\text{initial}} = 22.0^\circ\text{C}$), the pure air-volume thermal buffer lasts less than **3.6 seconds** ($120 \times 1.18 \times 1.005 \times 10 / 400 = 3.56\,\text{s}$) once CRAH fans lose power! Putting CRAH fans and secondary liquid CDU pumps on Uninterruptible Power Supply (UPS) or ultra-capacitor ride-through is therefore an electrical architecture mandate that no CFD simulation can talk its way around.

## Structural and Acoustic Limits of High-Velocity Perforated Floor Grates

When swapping standard $25\%$ perforated tiles for $55\%$ or $68\%$ high-capacity cast-aluminum grates on Sheet 2, two non-CFD physical limits must be checked on the floor:
1. **Rolling Load Rating (CISCA Recommended Test Procedures)**: Verify that the replacement high-flow grate is rated for the concentrated caster rolling load ($1,350\,\text{kg}$ to $2,200\,\text{kg}$) of fully populated NVL72 or storage racks along the transport path.
2. **Occupational Acoustic Noise (OSHA 85 dBA Limit)**: High-velocity air jets ($\ge 5.0\,\text{m/s}$) whistling through directional louver grates combined with rear-door server fan walls can push aisle sound pressure levels above $85\,\text{dBA}$, requiring mandatory hearing protection signage on the hall doors.

## Decisions to record before test start

- Re-affirmation that the commercial CFD solver manual is referenced, not duplicated.
- Explicit acknowledgment that CFD simulation does not replace Book 03 physical load-bank testing.
- The signed statement on Sheet 2 affirming that the report does not assert silicon reliability claims.

# 8. Public sources, and the copyright line

This field guide teaches an operational audit methodology for field benchmarking and evaluating computational fluid dynamics reports. It does not digest, transcribe, or duplicate proprietary engineering standards, commercial solver code, or confidential data center architectural drawings.

An engineering standard that can be purchased from an issuing standards body is not a document that may be reproduced in an external manual. Citing a standard by title, year, and specific equation to establish a legal audit threshold is standard professional practice; reproducing extensive passages from those standards within an AI-generated text is improper.

**NORMATIVE INDUSTRY STANDARDS CITED**

| ASME V&V 20 | "Standard for Verification and Validation in Computational Fluid Dynamics and Heat Transfer". Foundational principles for numerical discretization error (GCI) and validation comparison error metrics. |
| :--- | :--- |
| ASHRAE GUIDELINE 14 | "Measurement of Energy, Demand, and Water Savings". Establishes statistical calibration criteria: Mean Bias Error (NMBE) and Root Mean Square Error. |
| ASHRAE TC 9.9 | "Thermal Guidelines for Data Processing Environments" (5th Edition, 2021). Defines environmental classes (Class A1-A4), Recommended & Allowable bands. |
| GB 50174 | "Code for Design of Data Centers" (Chinese National Standard). Normative guidelines for data center airflow organization and numerical simulation. |
| SHARMA & HERRICK (ASME 2002) | "Dimensionless Parameters for Evaluation of Thermal Performance in Large- Scale Data Centers". Mathematical formulation of SHI and RHI indices. |
| HERRLIN (ASHRAE 2005) | "Rack Cooling Index (RCI): A Novel Metric for Evaluating Data Center Cooling Performance". Mathematical formulation of RCI_HI and RCI_LO. |

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

## Quantitative Cross-Reference Matrix of Public Thermal and Airflow Standards

When drafting project specifications or auditing a consultant's CFD report on Sheet 1 and Sheet 2, the engineer must cite the exact public standard that governs each physical measurement instrument, environmental envelope, and uncertainty calculation. Never allow a consultant to cite "industry standard CFD practices" without naming the specific document, edition, and measurement class.

| Governing Standard / Guideline | Issuing Organization | Specific Technical Scope in Whitespace & CFD Audits | Mandatory Field / Audit Application |
| :--- | :--- | :--- | :--- |
| **ASHRAE Thermal Guidelines for Data Processing Environments (5th Ed.)** | ASHRAE TC 9.9 | Defines Classes A1–A4 dry-bulb ($18\text{--}27^\circ\text{C}$ rec), dew-point, RH, and liquid classes W1–W5 | Governs maximum allowable intake temperature at $0.3, 1.2, 1.8\,\text{m}$ bezel elevations |
| **ASHRAE Guideline 0 & Guideline 202** | ASHRAE | Defines the Commissioning Process (Levels 1 through 5 IST) | Establishes that a simulation (Level 0/Design) never substitutes for Level 4/5 physical IST |
| **ASME V&V 20 (Standard for Verification and Validation in Computational Fluid Dynamics)** | ASME | Formal mathematical framework for numerical uncertainty ($U_{\text{num}}$), input uncertainty ($U_{\text{input}}$), and validation comparison error ($E$) | Governs Grid Convergence Index ($\text{GCI}$) and physical validation error bounds on Sheet 1 |
| **ISO/IEC 30134-2 & EN 50600-2-3** | ISO / CEN-CENELEC | Environmental control, airflow efficiency, and PUE/RCI whitespace thermal management metrics | Governs $\text{RCI}_{\text{HI}}$, $\text{RCI}_{\text{LO}}$, and containment pressure differential auditing |
| **ANSI/ASHRAE Standard 111** | ASHRAE | Measurement, testing, adjusting, and balancing (TAB) of building HVAC systems | Governs Pitot-tube duct traverses, capture-hood balometer accuracy, and coil face velocity grids |
| **IEC 60751** | IEC | Industrial platinum resistance thermometers and platinum temperature sensors | Governs Class A ($\pm 0.15^\circ\text{C}$) 4-wire Pt100 RTD calibration for vertical intake trees |

### Formal Validation Uncertainty Equation (ASME V&V 20)

Under ASME V&V 20, the comparison error $E$ between a simulation result $S$ and an experimental field measurement $D$ at any rack intake location is evaluated against the combined validation uncertainty $u_{\text{val}}$:

$$E = S - D, \qquad u_{\text{val}} = \sqrt{u_{\text{num}}^2 + u_{\text{input}}^2 + u_D^2}$$

Where $u_{\text{num}}$ is the numerical discretization uncertainty derived from the Grid Convergence Index, $u_{\text{input}}$ is the uncertainty propagated from boundary measurements (PDU power $\pm 0.5\%$, balometer flow $\pm 3.0\%$), and $u_D$ is the sensor calibration uncertainty ($\pm 0.15\,\text{K}$). Only when $|E| \le u_{\text{val}}$ across the benchmark array can the computational model claim physical validation within instrument precision.

## Archival Retention Requirements for Field Benchmark and CFD Model Files

To ensure that a calibrated whitespace model remains usable across the multi-year lifecycle of the data hall—when new high-density liquid/air pods are added in Phase 2 or Phase 3—the closeout binder must archive the raw digital artifacts alongside the PDF report:

| Archive Deliverable | Required File Format | Retention Owner & Location | Operational Purpose |
| :--- | :--- | :--- | :--- |
| **Raw Field Benchmark Dataset** | `.csv` / `.parquet` with ISO 8601 timestamps | Facility Engineering Historian | Proves physical baseline $T_1, T_2, T_3$, balometer CFM, and PDU kW |
| **3D Geometry & Native Solver File** | `.step` / `.iges` + native solver case file | Site Document Control Vault | Allows re-running future rack additions without rebuilding geometry |
| **Signed Sheet 1 & Sheet 2 PDFs** | Searchable PDF/A with wet/digital signatures | Commissioning Closeout Binder | Legal record of calibration pass ($\text{MAE}_T \le 1.5\,\text{K}$) and chosen remedy |

## Summary Verification Checklist for Independent CFD Peer Reviewers

Before signing the peer-review block on any whitespace simulation report:
1. Confirm Sheet 1 physical measurements ($S_1, S_2, R_1, R_2, R_3$ and $T_{0.3}, T_{1.2}, T_{1.8}$) are attached in raw CSV format.
2. Confirm $\text{MAE}_T \le 1.5\,\text{K}$, $\text{RMSE}_T \le 2.0\,\text{K}$, and global energy balance closure $\le 1.0\%$.
3. Confirm $\text{GCI}_{\text{fine}} \le 2.0\%$ across a minimum 2-grid mesh refinement study.
4. Confirm all candidate remedies on Sheet 2 were tested under identical turbulence closures and followed by a post-change physical verification walk.

## Decisions to record before test start

- The complete list of governing codes, guidelines, and technical papers cited in the CFD audit report, with publication dates.
- The specific edition of ASHRAE TC 9.9 cited in the project specifications.
- Formal confirmation that client-confidential architectural CAD models and vendor proprietary internal fan tables are preserved within local project files.
