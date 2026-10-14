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
