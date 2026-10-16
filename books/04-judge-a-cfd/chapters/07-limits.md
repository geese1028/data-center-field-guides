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
