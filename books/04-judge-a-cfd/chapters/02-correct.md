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
