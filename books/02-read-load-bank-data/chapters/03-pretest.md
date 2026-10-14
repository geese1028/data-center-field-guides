# 3. The pretest cells

The pretest gate asks a blunt, unyielding question: is this load bank cluster, on this specific day, operating inside the hydraulic, thermal, and electrical boundaries defined by the cited engineering specification?

The pretest is not the thermal gradient. It is the gatekeeper that permits the gradient test to count. If any pretest cell is out of bounds, you do not proceed to step-load testing. Attempting to run a 120kW heat test on a hydronic loop that cannot deliver its rated volumetric flow or that enters at an out-of-spec temperature will merely produce an invalid, unrepeatable heat balance that wastes hours of facility run-time.

## The liquid pretest cells

For secondary liquid loops simulating high-density AI clusters, the pretest section of the flash report requires three distinct hydraulic cells, evaluated per cabinet and across the manifold:

### 1. Volumetric flow rate per cabinet (Q_v)
The specification must declare a minimum flow floor (e.g., Q_floor ≥ 170.0 LPM for an educational 120kW NVL72-class reference model operating at ΔT = 10.0 K). 

- **Audited Parameter**: Measured volumetric flow rate entering each parallel cabinet under full facility CDU circulation.
- **Why the Cell Fails**: If flow drops below the floor (for instance, reading 155.0 LPM due to an un-opened balancing valve, an undersized hose ferrule, or a partially clogged strainer), liquid velocity across the heating elements drops. At lower velocities, convective heat transfer coefficients degrade, boundary layer sheath temperatures spike, and the fluid undergoes excessive localized thermal expansion.
- **Per-Cabinet vs. Header Sum**: The pretest line must record the flow for *each individual cabinet*, not merely the total secondary loop header flow. A header flow of 700 LPM across four cabinets can appear perfectly healthy while hiding a lethal hydraulic imbalance: Cabinets 1, 2, and 3 may receive 200 LPM each, while Cabinet 4 is starved at 100 LPM. If Cabinet 4 is starved, Cabinet 4 fails the pretest line immediately.

### 2. Coolant supply temperature (T_in)
The secondary loop supply coolant delivered by the facility CDU must sit squarely inside the declared commissioning envelope (typically 35.0°C ± 1.5 K for ASHRAE W4/W5 warm-water liquid architectures).

- **Audited Parameter**: Primary liquid supply temperature measured by an immersion 4-wire Pt100 RTD penetrating the high-velocity core stream ($1/3 \sim 1/2 D$) of the manifold drop.
- **The Dew Point Safety Floor**: In addition to the nominal setpoint band, the pretest must verify that supply temperature satisfies the absolute non-condensation rule:
 $$T_{\text{in}} \ge T_{\text{dp}} + 2.0\,\text{K}$$
 where T_dp is the live dew point calculated from data hall dry-bulb temperature and relative humidity. If chilled coolant enters at 18.0°C while the data hall dew point is 21.5°C, uninsulated quick disconnects and EPDM hoses will sweat profusely, dripping water directly onto underlying electrical trays. That is an immediate pretest FAIL.
- **Temperature-Dependent Flow Adjustment**: If the facility loop is running colder than nominal design (e.g., entering at 25.0°C on an unconditioned morning), the fluid viscosity increases by nearly 30%. The flow floor must cite the temperature at which it was calibrated. A flow floor copied from a 40.0°C test cannot be directly applied to a 20.0°C fluid without hydraulic correction.

### 3. Manifold differential pressure (ΔP)
The hydraulic impedance across the load bank must match the physical IT rack's certified pressure drop curve within a pre-declared tolerance (typically ΔP_rated = 112.0 kPa ± 5.0 kPa at 176.5 LPM).

- **Audited Parameter**: Static differential pressure measured between the supply inlet manifold tap and return outlet manifold tap (ΔP = P_in - P_out).
- **Inspection for Fraudulent Taps**: The pretest must verify that pressure taps are clean, deburred, perpendicular to the pipe wall, and equipped with snubber valves to eliminate high-frequency turbulence noise. A differential pressure reading taken across throttled isolation ball valves or restrictive adapters measures pipe friction, not rack impedance.

## The companion air pretest cells

If your test campaign includes an air-cooled companion load (which is mandatory when verifying the 80:20 or 85:15 sensible heat split of NVL72-class architectures), the pretest section must include two dedicated air cells:

1. **Intake Air Temperature (T_air,in)**: Ambient dry-bulb air entering the load bank's front perforations must sit within the facility design range (typically 22.0°C to 27.0°C in accordance with ASHRAE TC 9.9 Thermal Guidelines). If return air from a previous uncontained test has short-circuited into the intake, elevating T_air,in to 42.0°C, the air section will experience early thermal throttling.
2. **Auxiliary Blower Airflow Velocity**: Air velocity across the auxiliary heating stages must be confirmed using a calibrated hot-wire anemometer or differential pressure sensor across the intake filter grille, ensuring that airflow meets the minimum convective threshold (Q_air ≥ 1200 CFM per 20kW air module) to prevent element overheat.

If the air companion load is excluded from the contract scope, the cell must be explicitly marked **NOT APPLICABLE (N/A)** in ink prior to the run. You may not discover halfway through the pretest that an air velocity meter was forgotten, and then retroactively claim that air testing was "not applicable."

## Match the document, do not become the document

A common pitfall in commissioning reports is copying pages of vendor marketing datasheets into the appendix and claiming that the test "matches the datasheet."

A vendor datasheet is a commercial proposal. It is not an engineering verification. The flash report must maintain a strict, professional separation:
- The requirements sheet defines the cited limit (e.g., *"DOC-NVL72-SPEC Rev 2.4, Table 3: Minimum secondary flow = 170.0 LPM"*).
- The pretest table records the actual observed number measured by a calibrated instrument on the test floor (e.g., *"Cabinet #01 = 176.4 LPM at 14:02:15 UTC"*).
- The verdict column records the mathematical comparison: **PASS** (within tolerance) or **FAIL** (outside tolerance).

A reader must be able to see the cited limit, the measured value, the timestamp, and the verdict side-by-side on a single page. If an audit team cannot trace the measured number to a real instrument tag, or cannot trace the limit to a frozen document revision, the cell is open. An open cell means the pretest line is **FAIL**.

## Decisions to record

Before signing the pretest section of the flash report, verify that the following items are fully documented:

- The cited specification document title, revision mark, and issue date for all hydraulic limits.
- The measured volumetric flow rate for each individual cabinet in the parallel cluster.
- The verified coolant supply temperature and the calculated data hall dew point margin.
- The measured manifold differential pressure ΔP across clean, deburred taps.
- The companion air intake temperature and velocity (or the signed N/A scope reduction).
- The final pass/fail determination for the pretest gate, initialed by the Sheet Owner and the Operator.
