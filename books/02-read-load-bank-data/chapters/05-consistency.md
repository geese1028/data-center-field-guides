# 5. Consistency and multi-cabinet uniformity

A single sensor can report a plausible, attractive number and still be fundamentally disconnected from physical reality. In high-density data halls where multiple parallel load banks simulate an entire AI cluster row, evaluating units in isolation is inadequate.

The flash report requires a rigorous mathematical test of multi-cabinet consistency: do the instruments and machines that claim to be identical twins on the same secondary manifold behave like identical twins under full load?

In this field guide, consistency is not an informal impression or a visual appraisal of parallel graphs. It is defined by a strict mathematical metric: the **Coefficient of Variation (CV)**.

$$\text{CV} = \left( \frac{\sigma}{\mu} \right) \times 100\% = \left[ \frac{\sqrt{\frac{1}{N} \sum_{i=1}^N (x_i - \mu)^2}}{\mu} \right] \times 100\%$$

where N is the number of parallel load-bank cabinets in the cluster, μ is the arithmetic group mean, and σ is the sample standard deviation. 

(See Figure 03 for the multi-cabinet hydraulic distribution schematic, manifold pressure gradients, and the comparative case studies of balanced vs. starved clusters).

## Where the CV metric applies

The flash report calculates CV across four physical dimensions during the steady-state dwell of every load step:

### 1. Electrical active power uniformity (CV ≤ 1.0%)
Across all parallel load-bank cabinets, active electrical power draw must be balanced within a 1.0% envelope. Resistors manufactured from high-grade Nickel-Chromium (NiCr 80/20) alloys have a strict resistance tolerance (± 2.0% cold, expanding to ± 1.0% across balanced 3-phase delta configurations). 
- If four parallel cabinets are commanded to 120kW, and three draw 120.2kW while Cabinet 4 draws only 108.5kW, the electrical CV spikes to 4.8%.
- An electrical CV exceeding 1.0% indicates a loose terminal lug, a blown branch fuse, a burnt SSR, or an uncalibrated current transducer (CT). It fails the electrical consistency line immediately.

### 2. Coolant volumetric flow uniformity (CV ≤ 5.0%)
In a properly balanced secondary cooling distribution network, every parallel IT rack must receive an identical share of the total liquid stream.
- For four 120kW units operating on a common manifold with a total delivery of 706 LPM, the ideal branch flow is 176.5 LPM per unit.
- Liquid flow rates across all active cabinets must satisfy **CV ≤ 5.0%**.
- A flow CV exceeding 5.0% reveals hydraulic maldistribution—typically caused by unequal branch hose lengths, sharp 90° elbow kinks, improperly seated quick-disconnect internal check valves, or unadjusted branch balancing valves.

### 3. Return coolant temperature rise uniformity (CV ≤ 3.0%)
If electrical power is uniform (CV ≤ 1.0%) and liquid flow is uniform (CV ≤ 5.0%), thermodynamics dictates that the return coolant temperature rise (ΔT = T_out - T_in) must also be uniform.
- Across all cabinets, temperature rise must satisfy **CV ≤ 3.0%**.
- If Cabinet 1 through 3 exhibit ΔT = 10.0 K while Cabinet 4 exhibits ΔT = 14.5 K, Cabinet 4 is experiencing localized heat concentration (frequently driven by low flow). Conversely, if Cabinet 4 exhibits ΔT = 2.1 K, it is suffering from internal fluid short-circuiting around its heating core.

### 4. Manifold differential pressure uniformity (CV ≤ 5.0%)
Differential pressure measured across the supply and return ports of each individual cabinet must satisfy **CV ≤ 5.0%**. This verifies that all chassis present identical hydraulic impedance to the facility CDU pumps.

## The hydraulic danger: Direct-return vs. reverse-return manifolds

The consistency chapter exposes the single most common piping defect in temporary liquid load-bank installations: **direct-return manifold starvation**.

As illustrated in Figure 03:
- In a **Direct-Return (First-In, First-Out)** manifold, the first load bank (Rack 1) is closest to both the primary supply feed and the primary return collector. Rack 1 experiences the shortest hydraulic circuit and the highest available differential pressure (ΔP). The farthest unit (Rack 4) sits at the hydraulic dead-end, where supply pressure has decayed due to pipe friction and return back-pressure has accumulated.
- Without individual branch balancing valves, Rack 4 receives significantly degraded flow (e.g., 124.0 LPM vs 192.0 LPM at Rack 1). This results in a disastrous flow CV of **18.25%**!
- In an attempt to mask this failure, inexperienced teams will calculate an "average cluster flow" (168.25 LPM) and declare the test passed. Meanwhile, in Rack 4, fluid velocity has collapsed, sheath temperatures are soaring toward 85°C trip limits, and the CDU pumps are operating in an unstable region.
- In a **Reverse-Return (Tichelmann)** piping loop, the first unit fed is the last unit returned, ensuring that total equivalent pipe length is identical across all four branches. The resulting flow CV easily drops to **0.33%**, guaranteeing true hydraulic fidelity.

The flash report requires the CV of flow to be calculated and printed on the first page. A high CV immediately exposes direct-return starvation before real compute hardware is deployed.

## The evaluation window rules

The consistency analysis must be performed over a continuous **five-minute evaluation window** taken during the final, steady portion of a 15-minute load dwell.
- The window must be sampled at **1 Hz** (one live reading per second per channel).
- The window must be strictly confined to steady state. It must never span across a load step transition or an operator valve adjustment. Including a power step within the window artificially inflates variance, causing an honest set of cabinets to fail the calculation.
- If a load step was held for only 3 minutes, you do not have sufficient steady-state data to compute CV. In that case, you must mark the consistency line **NOT RUN** or repeat the step with a proper dwell. You may not stretch the window backward into the transient warm-up to collect enough points.

## What CV cannot say: The zero-variance fraud

A low CV proves that the cluster agrees with itself. It does not prove that the cluster is correct.

Consider two dangerous failure modes that produce deceptively low CVs:
1. **Uniformly Out of Spec**: All four cabinets receive an identical flow of 130.0 LPM against a specified floor of 170.0 LPM. The standard deviation is zero, and the calculated flow CV is a spotless 0.00%. Yet the cluster is uniformly starved! This passes the consistency line, but it fails the Pretest line unconditionally. Uniform failure is still failure.
2. **The Stale / Frozen Data Fraud**: If an edge gateway communication thread crashes, or if a Modbus poller repeatedly logs cached values without reading live registers, the recorded values across all four cabinets will remain mathematically frozen. A dead group will report a standard deviation of σ = 0.000 and a calculated CV of **0.00%**!

A CV of exactly 0.00% is not a mark of engineering perfection; in a turbulent fluid loop, it is physical proof of telemetry fraud. Real turbulent convection always generates microscopic thermal and pressure fluctuations. 

Therefore, before any calculated CV can be accepted in the flash report:
- The supervisory system must verify that **sample variance σ² > 0** across all channels.
- The 16-bit Quality Bitmask must confirm that no channel has its "STALE / FROZEN" bit asserted.

If the variance is zero or the quality bit is faulted, the calculated CV is paint. Fail the line.

## Decisions to record

In the consistency section of the flash report, record the following facts:

- The pre-declared CV threshold limits for electrical power (≤ 1.0%), liquid flow (≤ 5.0%), temperature rise (≤ 3.0%), and differential pressure (≤ 5.0%).
- The exact 5-minute time window (start and end timestamps to the second) used for the steady-state calculation.
- The arithmetic mean (μ), sample standard deviation (σ), and calculated CV for each parameter across all parallel cabinets.
- The certified non-zero variance check (σ² > 0) confirming that live turbulent jitter was present on every channel.
- The signed pass/fail verdict for multi-cabinet consistency, initialed by the Stranger.
