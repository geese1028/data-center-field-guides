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
