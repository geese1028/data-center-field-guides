# 7. The data block and heat balance reconciliation

Every load plateau that the flash report claims as evidence must possess an identical, standardized data block. 

A data block is not an unstructured collection of numbers thrown onto a page. It is a systematic thermodynamic balance sheet containing five mandatory sections:
1. **Setpoints & Commands** (The pre-declared intention);
2. **Initial State Baseline** (The reference condition immediately prior to the step);
3. **Electrical Distribution Data** (The verified energy delivered to the elements);
4. **Hydraulic Enthalpy Data** (The heat absorbed into the liquid stream);
5. **Companion Air & Thermal Closure** (The total first-principles energy balance reconciliation).

Missing any one of these five headings is not an economical formatting choice; it is an omission of a fundamental engineering claim. (See Figure 06 for the complete energy decomposition Sankey, the four-step reconciliation table, and the four diagnostic failure modes).

## Heading 1: Setpoints and commands

The first section of the data block records the commands issued to the machine *before* the dwell began:
- Commanded electrical load: e.g., 120.0 kW (or the specific percentage of rated duty: 25%, 50%, 75%, 100%, 110%).
- Commanded power split across dual feeders: e.g., Feeder A = 60.0 kW, Feeder B = 60.0 kW.
- Commanded modulating valve position: e.g., TCV = 100% full open (or locked balancing valve position = 4.2 turns).
- Commanded companion air blower speed: e.g., 100% (or fixed 1200 CFM).

A command value must be recorded from the supervisory control log before the clock starts. Reconstructing the "command" by averaging the observed power during the dwell is a circular calculation: it turns a measured result into an artificial setpoint.

## Heading 2: Initial state baseline

The second section documents the condition of the system during the minute immediately preceding the step transition:
- Starting coolant supply temperature (T_in,init) and return temperature (T_out,init).
- Starting volumetric flow rate (Q_v,init) and manifold differential pressure (ΔP_init).
- Timestamp of the baseline minute (start and end to the second).

This baseline is essential for separating the steady-state thermal gain from any background temperature drift occurring within the facility primary cooling loop.

## Heading 3: Electrical distribution data

The third section details the active electrical power drawn by the heating elements. In an industrial 415V 3-phase dual-feeder configuration, reporting a single aggregated "kilowatts" figure is inadequate. The report must provide:
- **Feeder A Metrics**: Line-to-line voltages (V_AB, V_BC, V_CA), line currents (I_A, I_B, I_C), total Feeder A active power (P_A), and power factor (PF_A).
- **Feeder B Metrics**: Line-to-line voltages, line currents, total Feeder B active power (P_B), and power factor (PF_B).
- **Total Active Power**: 
 $$P_{\text{elec}} = P_A + P_B$$
- **Phase Balance Verification**: Current unbalance across phases must satisfy I_unbalance ≤ 2.0%. A severely unbalanced current indicates that one resistor bank has failed open or that an internal contactor pole is pitted and failing to seat.

## Heading 4: Hydraulic enthalpy data

The fourth section captures the cooling fluid's thermodynamic absorption of heat. This requires high-accuracy metrology across six physical parameters:
1. **Supply Coolant Temperature (T_in)**: Measured via 4-wire Pt100 RTD immersed in the core flow ($1/3 \sim 1/2 D$).
2. **Return Coolant Temperature (T_out)**: Measured downstream of the heating vessel after full fluid mixing.
3. **Net Temperature Rise (ΔT)**: 
 $$\Delta T = T_{\text{out}} - T_{\text{in}}$$
4. **Volumetric Flow Rate (Q_v)**: Measured via calibrated vortex shedding flow meter (reported in liters per minute, LPM).
5. **Fluid Thermophysical Properties**: Density (ρ) and specific heat capacity (C_p) must be evaluated at the mean bulk fluid temperature:
 $$\bar{T} = \frac{T_{\text{in}} + T_{\text{out}}}{2}$$
 For a standard 25% Propylene Glycol / 75% Water solution (PG25) at $\bar{T} = 40.0°C$, the standard values are:
 $$\rho = 1025.0\,\text{kg/m}^3, \quad C_p = 3.980\,\text{kJ/(kg}\cdot\text{K)}$$
6. **Inferred Liquid Thermal Heat (Q_liquid)**: 
 Derived directly from first-principles thermodynamics:
 $$Q_{\text{liquid}} = \dot{m} \cdot C_p \cdot \Delta T = \left( Q_v \times \frac{\rho}{60,000} \right) \cdot C_p \cdot (T_{\text{out}} - T_{\text{in}})$$

For the baseline educational reference model operating at rated full duty (Q_v = 176.5 LPM, ΔT = 10.04 K):
$$\dot{m} = 176.5 \times \frac{1025.0}{60,000} = 3.015\,\text{kg/s}$$
$$Q_{\text{liquid}} = 3.015\,\text{kg/s} \times 3.980\,\text{kJ/(kg}\cdot\text{K)} \times 10.04\,\text{K} = 120.48\,\text{kW} \times \text{split ratio} \approx 98.6\,\text{kW}$$

## Heading 5: Companion air & first-principles thermal closure

In NVL72-class AI architectures, approximately 16% to 20% of total rack heat is rejected directly into the data hall air by optical transceivers, motherboard power conversion stages, and memory modules. The companion air section must capture this sensible heat:
- Intake dry-bulb air temperature (T_air,in) and discharge air temperature (T_air,out).
- Air mass flow rate (ṁ_air) derived from blower RPM and calibrated nozzle differential pressure.
- Inferred air sensible heat:
 $$Q_{\text{air}} = \dot{m}_{\text{air}} \cdot C_{p,\text{air}} \cdot (T_{\text{air,out}} - T_{\text{air,in}})$$

### The First-Principles Energy Balance Equation
By the first law of thermodynamics, the active electrical energy delivered to the load bank must equal the total heat leaving the cabinet boundaries plus any uninsulated parasitic losses:
$$P_{\text{elec}} = Q_{\text{liquid}} + Q_{\text{air}} + Q_{\text{chassis\_loss}}$$

Where uninsulated chassis skin loss ($Q_chassis\_loss$) through natural convection and radiation is typically bounded at ≤ 2.0% of total power when proper internal ceramic blanket insulation is installed.

### The Enthalpy Closure Ratio Gate
The flash report evaluates the **Enthalpy Closure Ratio**:
$$\text{Closure Ratio} = \left[ 1.0 - \frac{|P_{\text{elec}} - (Q_{\text{liquid}} + Q_{\text{air}})|}{P_{\text{elec}}} \right] \times 100\%$$

To achieve a **PASS** on the step data block, the energy closure must satisfy:
$$\text{Closure Ratio} \ge 97.0\% \quad \left( \text{or an energy discrepancy } \le 3.0\% \right)$$

If P_elec = 120.0 kW, but the sum of liquid enthalpy (Q_liquid = 75.0 kW) and air heat (Q_air = 19.0 kW) is only 94.0 kW, the closure ratio is only 78.3%! There is 26.0 kW of missing energy!
- This discrepancy cannot be glossed over by adding an undocumented "efficiency factor" or "loss correction."
- An enthalpy closure failure of 26 kW indicates a severe physical defect: fluid is short-circuiting around the heating vessel via an open bypass valve, the flow meter calibration factor (K-factor) is incorrect, or the RTDs are seated in stagnant dead-leg stubs.
- An energy closure failure fails the step plateau unconditionally.

## Reporting hierarchy: One cabinet, then the cluster summary

When reporting multi-cabinet test clusters:
1. Each individual cabinet must have its own discrete data block printed first, with all five headings and four-summary statistics ($\min, \max, μ, σ$).
2. Beneath the individual cabinet blocks, the **Cluster Summary Block** is compiled, reporting total electrical power, total liquid enthalpy absorption, total air heat, and the cluster-wide Enthalpy Closure Ratio.

A cluster summary that looks calm and balanced cannot outvote an individual cabinet that failed its energy closure. If Cabinet 4 has 20kW of missing heat while Cabinets 1, 2, and 3 are balanced, Cabinet 4 is a failure. You do not average Cabinet 4 into the cluster to manufacture a synthetic pass.

## Decisions to record

For every step data block compiled in the flash report, record:

- The commanded setpoints for active power, dual-feeder split, and trim valve position.
- The pre-step initial baseline fluid and air temperatures.
- The 3-phase electrical voltages, currents, power factors, and total active power P_elec.
- The measured fluid temperatures, volumetric flow, fluid density, specific heat, and inferred liquid enthalpy Q_liquid.
- The measured air temperatures, airflow rate, and inferred companion air heat Q_air.
- The calculated First-Principles Enthalpy Closure Ratio, certifying that closure ≥ 97.0%.
- The initials of the Recorder and the Stranger confirming the energy balance.
