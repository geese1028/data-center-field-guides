# 12. Automated charting and visual integrity

An automated report generator or supervisory dashboard is a powerful tool for converting raw telemetry into rapid visual representations. However, an automated chart is not an independent authority. It is merely a visual projection of the numbers recorded in the underlying data blocks.

If a visual chart and a flash-report data block disagree, the numbers in the data block always govern. A handsome, smooth curve rendered by a plotting library does not possess the authority to pass a cell that the raw data table failed.

Furthermore, charting in commissioning is fraught with subtle visual deceptions—some accidental, some intentional. An uncalibrated vertical axis can flatten a dangerous 15% flow starvation until it looks like a hair-thin line, while a mislabeled title can cause an auditor to mistake electrical power consumption for certified liquid cooling capacity.

This chapter defines the strict rules of automated charting, visual scaling ethics, and required plot layouts.

## What the operator must set before any curve is drawn

An automated reporting script must never be allowed to guess the boundaries of its dataset. Before generating a single chart, the Operator must explicitly define two parameters in the script configuration:

1. **The Exact Time Window**: The start and end timestamps, defined to the exact second (e.g., `START = 2026-10-14T14:00:00Z`, `END = 2026-10-14T15:30:00Z`). The script must pull data strictly from within this window. An automated report that uses an ambiguous, floating window (such as "the last 60 minutes") will slide forward during review, altering calculated means as the system cools down.
2. **The Explicit Unit Roster**: The exact list of load-bank cabinet serial numbers active in the test (e.g., `UNITS = ["LB-01", "LB-02", "LB-03", "LB-04"]`). Never permit a reporting template to retain hardcoded unit lists from an earlier job. If a template titled "18-Cabinet Row Test" is run on a day when only 4 cabinets are connected, the resulting figures will be an embarrassing administrative mess.

Every generated chart must print its time window and active unit roster directly into its upper subtitle banner.

## The two-chart requirement: Overlaid cluster vs. individual deep dive

Whenever a physical parameter is presented in the automated report, generating a single aggregated chart is prohibited. A single chart showing only the cluster sum or cluster average conceals cabinet-level divergence.

The reporting engine must generate **two complementary charts** for every monitored quantity:

### Chart A: The Overlaid Cluster Chart
All parallel cabinets are plotted together on a single set of axes, using high-contrast, distinguishable line colors:
- This allows an auditor to instantly see if one cabinet "leaves the herd"—for example, observing three cabinets tracking at 176 LPM while Cabinet 4 drops to 124 LPM.
- The cluster arithmetic mean (μ) is plotted as a bold dashed yellow line through the center of the band.

### Chart B: The Individual Cabinet Deep-Dive Chart
Each individual cabinet is given its own dedicated plot panel with its own optimized vertical axis:
- This prevents a common scaling deception: if Cabinet 4's return temperature rises from 45.0°C to 49.8°C, plotting it on an overlaid chart whose vertical axis spans from 0°C to 100°C will make the 4.8K spike appear negligible.
- On its dedicated deep-dive chart, the vertical axis spans tightly across the operating window (e.g., 30°C to 55°C), ensuring that the temperature rise and any high-frequency hunting are clearly visible.

## The four summary statistics beneath every chart

Beneath every generated plot panel, the automated reporting engine must calculate and print a standardized summary table containing four specific metrics for that specific window:

1. **Minimum Value ($\min$)**
2. **Maximum Value ($\max$)**
3. **Arithmetic Mean (μ)**
4. **Median Value ($\tilde{x}$)**

### Why the Median is Mandatory
In automated telemetry ingestion, electrical contactor switching and high-voltage breaker operations can induce an electromagnetic interference (EMI) pulse that causes an analog-to-digital converter (ADC) to log a single, spurious 1-millisecond spike (e.g., logging a single sample of 1200 kW before returning to 120.0 kW).
- In a 900-sample dwell, that single bad sample will pull the arithmetic mean upward by 1.2 kW, distorting the energy closure calculation.
- The median is inherently robust against isolated outlier spikes. Comparing the mean (μ = 121.2 kW) against the median ($\tilde{x} = 120.0 kW$) immediately exposes the presence of an asymmetric spike.
- If the maximum and minimum are identical ($\max = \min = 45.000°C$), the reporting engine must automatically highlight the table in red with the label: **"WARNING: ZERO VARIANCE DETECTED (STALE BUFFER)."**

## The core chart categories

The automated report must produce five standardized chart suites:

### 1. Electrical Power Suite
- Total active cluster power (kW) over time.
- Individual cabinet active power overlaid and separate.
- 3-phase line-to-line voltages and feeder phase currents.
- Verification that Feeder A and Feeder B share power symmetrically (50% ± 1.0%).

### 2. Coolant Hydraulics Suite
- Volumetric flow rate per cabinet (Q_v, reported in LPM).
- Manifold differential pressure (ΔP = P_in - P_out, reported in kPa).
- Total secondary loop flow rate, explicitly derived as the sum of branch flow meters.

### 3. Thermal Enthalpy Suite
- Secondary coolant supply temperature (T_in) and return temperature (T_out) per cabinet.
- Differential temperature rise (ΔT = T_out - T_in) per cabinet.
- **The Sign Check Gate**: The difference must be strictly positive (T_out > T_in). If a plumbing error reversed the hoses, ΔT will plot as negative. The plotting script is strictly forbidden from applying an absolute value function (`abs(delta_t)`) to make a reversed connection look correct! A negative ΔT must plot as negative and trigger an automated FAIL flag.

### 4. True Inferred Heat vs. Electrical Power Suite
- Electrical active power (P_elec) plotted alongside true inferred liquid enthalpy (Q_liquid = ṁ C_p ΔT).
- Under no circumstances may an electrical power trace be re-titled as "Cooling Power"!
- Electrical power is energy delivered from the switchgear; cooling power is thermal energy absorbed by the fluid stream. Plotting them on the same axis with distinct colors immediately exposes any internal bypass leakage or missing heat.

### 5. Companion Air Suite
- Intake dry-bulb air temperature (T_air,in) and exhaust air temperature (T_air,out).
- Air temperature differential (ΔT_air).
- Inferred air sensible heat (Q_air).

## Rules of visual scaling ethics

Visual scales must never be manipulated to flatter the performance of the equipment. The following plotting rules are mandatory:

- **Ban on Suppressed Zeroes for Capacity Claims**: When plotting total power or total flow against rated nameplate duty, the vertical axis must include the zero baseline so the viewer can see the true magnitude of steps.
- **Ban on Over-Expanded Axes to Hide Variance**: When plotting temperature stability or flow uniformity across steady dwells, the vertical axis must not be artificially expanded to ± 100 K or ± 500 LPM to make severe hunting look like a straight line. The axis must be scaled tightly to the cited tolerance envelope (e.g., T_nominal ± 5.0 K).
- **Explicit Gridlines**: Every chart must render light horizontal and vertical gridlines at standard engineering intervals (e.g., every 5 minutes, every 10 kW, every 1.0 K) to permit rapid visual auditing without a digital ruler.

## Decisions to record

In the charting section of the flash report, document:

- The exact start and stop timestamps of the plotting window.
- The confirmed list of active cabinet serial numbers included in the visual generation.
- The sampling resolution of each plotted channel (1s raw vs 60s rolling mean).
- Confirmation that no absolute value transforms or artificial smoothing filters were applied to raw series.
