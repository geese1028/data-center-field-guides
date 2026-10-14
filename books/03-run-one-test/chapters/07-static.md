# 7. Static, no energy

The static, de-energized verification phase is where a commissioning project establishes the safety foundation for all subsequent dynamic testing. It is also the phase contractors are most tempted to compress when equipment shipping is delayed.

Compromising the static phase to recover lost calendar time is an unacceptable operational risk. A sheared quick-disconnect O-ring, a pinched cable conductor, an un-purged air pocket, or an inverted electrical phase will inevitably trigger an unscheduled shutdown during dynamic testing—a far more hazardous and expensive way to discover an installation defect.

In the global commissioning hierarchy, this work constitutes **Level 2 (Delivery and Static QA)** and **Level 3 (Pre-Functional Checks and Start-Up)**. It must be filed under those certificate tabs, never mislabeled as Level 1 Factory Acceptance.

![Multi-Cabinet Manifold Balance](../figures/fig-04-multi-rack-manifold-hydraulics.png)

## Uncrating, Physical Inspection, and Mechanical Fittings

Every piece of equipment delivered to the data hall must be inventoried against the packing list:
- **Chassis and Caster Inspection**: Check load-bank frames for shipping deformation, loose structural fasteners, or damaged casters that could compromise floor loading.
- **Quick-Disconnect Couplings**: Inspect every secondary quick-disconnect fitting (such as Danfoss Hansen FD83 couplings or ISO 16028 dry-break couplings). Verify that coupling locking collars engage smoothly without galling. Inspect internal EPDM elastomeric seals under magnification for cuts, pinholes, or manufacturing burrs. Never use petroleum-based grease on EPDM seals; use only approved silicone-based or system-compatible lubricants.
- **Hose Assemblies**: Verify hose tags. All flexible secondary hoses must be wire-braided synthetic rubber or reinforced PTFE rated for at least 1.5× the maximum secondary operating pressure and certified for continuous operation at 70°C. Inspect bend radii to ensure no hose is kinked below the manufacturer's minimum allowable radius.

## De-Energized Electrical Isolation and Safety Checks

All electrical verification in this phase is conducted with upstream supply circuits locked out and tagged out (LOTO) and confirmed de-energized using an approved voltage detector:

### 1. Insulation Resistance (Megger Test)
Using a calibrated insulation tester, apply 1000V DC for 60 seconds between:
- Phase A to Phase B, Phase B to Phase C, Phase C to Phase A.
- Each individual phase conductor to Equipment Ground (PE).
- Neutral conductor (if present) to Equipment Ground.

**Acceptance Standard**: Insulation resistance must exceed 100 MΩ minimum. Any reading below 20 MΩ indicates moisture ingress or compromised insulation and acts as an absolute bar to energization.

### 2. Ground Continuity Bond Test
Using a calibrated micro-ohmmeter, measure resistance between the load-bank chassis ground terminal, internal heater element frames, and the facility Main Grounding Busbar (MGB).

**Acceptance Standard**: Ground bond resistance must not exceed 0.1 Ω. A poor ground connection creates a lethal touch-potential hazard if an insulation failure occurs during multi-megawatt testing.

### 3. Phase Sequence and Rotation Verification
Before connecting the load-bank power cables to the facility PDU or busway tap box, measure phase rotation at the supply receptacle using an approved phase sequence indicator.

**Acceptance Standard**: Phase rotation must be strictly clockwise ($L_1 \to L_2 \to L_3$ / $A \to B \to C$).

> **CRITICAL PUMP SAFETY NOTE**: In a liquid-cooled data hall, CDU secondary pumps are typically hermetically sealed, canned motor centrifugal pumps. If an inverted phase sequence ($A \to C \to B$) is applied, the pump motor will spin in reverse. A centrifugal impeller rotating backward produces almost zero dynamic head, causes severe fluid churning and cavitation, and can destroy the thrust bearings within minutes. The phase rotation cell on Sheet 1 must record verified clockwise rotation; if blank, energization is strictly prohibited.

## Mechanical Secondary Flushing, Hydrostatic Hold, and Air Purge

The fluid loop connecting the CDU, distribution manifolds, and load banks must undergo rigorous pre-commissioning preparation:

### 1. Pre-Commission Pipe Flushing (BSRIA BG 29/2020 Standard)
Never circulate fluid through a newly installed secondary loop directly into the load-bank heating channels or CDU heat exchanger. The secondary loop must first be flushed through temporary bypass loops at a minimum scouring velocity of 1.5 m/s to dislodge construction scale, slag, and pipe debris. Clean inline strainers repeatedly until particulate counts meet ISO 4406 cleanliness standards (typically 16/14/11).

### 2. Hydrostatic Pressure Hold
Once flushed and connected, the secondary circuit—including all manifolds, flexible hoses, and load-bank internal heat exchangers—is pressurized with water or 25% Propylene Glycol to **1.5× Maximum Allowable Operating Pressure (MAOP)** (typically 6.0 bar to 9.0 bar for standard data center secondary circuits).

**Acceptance Standard**:
- The pressure must be held continuously for **2.0 hours minimum**.
- Calibrated digital pressure logging must show zero measurable pressure decay (ΔP ≤ 0.0 bar), accounting for fluid thermal expansion.
- Every mechanical joint, threaded adapter, and quick disconnect must undergo a visual inspection with clean white absorbent paper. The allowable leak rate is **zero drops per minute**.

### 3. Thorough Air Venting and Vacuum Deaeration
Entrained air microbubbles are a primary cause of commissioning anomalies. Air trapped inside heat exchanger channels forms insulating barriers that artificially degrade apparent heat transfer coefficients, while bubbles passing through ultrasonic flow meters disrupt transit-time acoustic signals. 

Engage high-point automatic air vents and run the secondary vacuum deaerator until visual sight glasses show zero foam and dissolved oxygen levels drop within specification.

## Fluid Volume Audit

Calculate and document the exact secondary fluid inventory of the test system on Sheet 1:

$$V_{\text{total}} = V_{\text{CDU\_internal}} + \sum (V_{\text{manifold}}) + \sum (V_{\text{hoses}}) + \sum (V_{\text{load\_banks}})$$

Documenting the physical fluid mass (M_fluid = ρ · V_total) is essential for validating the thermal inertia calculations required during Level 5 integrated system testing.

## Upstream Electrical Protective Coordination

Trace the electrical distribution path upward from the load-bank tap box to the row PDU and upstream sub-station transformer. Audit the breaker trip unit settings:
- Verify that electronic trip units (LSIG) have their instantaneous pickup (I_i) and short-time delay (I_sd) coordinated above the inrush characteristics of the load bank’s internal transformer or SCR heater controllers.
- Confirm that ground-fault alarm thresholds are properly set so that residual capacitive filter leakage does not trip the primary sub-feed breaker during the initial heating step.

## The Static Prerequisite Gate

The static stage concludes with a formal review of Sheet 1. Every checkbox must be marked **PASS** in ink, or accompanied by a formal engineering punch list item. If any open defect remains in the electrical insulation, ground bond, phase rotation, or hydrostatic pressure hold, the project gate is closed. Dynamic energization cannot proceed.

## Decisions to record before test start

- The uncrating inspection log, recording all fitting counts and physical seal audits.
- The certified megger insulation and ground resistance values, signed by the Electrical PE.
- The verified clockwise phase sequence, signed in ink.
- The witnessed hydrostatic pressure test certificate (test pressure, hold duration, zero drop).
- The calculated total secondary fluid volume (V_total).
- The upstream PDU breaker trip settings and protective coordination audit.
