# 0. How to use this book

This book is for the person who runs a load-bank test on a liquid-cooled data center hall before production IT equipment arrives. The load bank is already accepted. You can already parse telemetry and flash reports. The job in front of you is to connect that load bank in place of the high-density rack, heat the plant on purpose under controlled thermal steps, and leave the hall with engineering records that a third-party auditor, insurer, or hyperscaler operations team can inspect without a telephone call.

It is not a building commissioning manual. The overarching method statement tells you which contract deliverables to file and which completion certificates you are legally authorized to sign. The work itself is the verification of the liquid loop: physical uncrating, megger and ground isolation, secondary flushing and hydrostatic pressure holds, cold pump curve baselining, alarm loops, multi-tier thermal steps, transient failure rides, and a structured shutdown. If a paragraph starts to become an architectural tour of the facility, cut it. Leave the engineering sheet.

```
+---------------------------------------------------------------------------------------------+
| THREE INDEPENDENT COMMISSIONING GATES |
+------------------------------+------------------------------+-------------------------------+
| THE SCRIPT DRAFT | THE FIELD EXECUTION | THE AUDITED PACK |
| Pre-approved tolerances, | One person measures, | Seven completed sheets, |
| instrument calibration IDs, | one writes in ink; | trend logs, raw time series, |
| and non-negotiable stops | zero unapproved overrides | and signed punch registers |
+------------------------------+------------------------------+-------------------------------+
```

If you are on the tools tomorrow, turn to Chapter 16 and take the master sheets onto the floor. Read Chapters 2 and 3 before anyone asks you to sign a Level 1 or Level 4 certificate; those chapters prevent a field walk-through from being filed into a factory acceptance binder. They keep two distinct commissioning numbering systems from destroying project compliance.

When the test window closes, you must hand over seven complete sheets, filled in ink or marked explicitly as out of scope in writing. A blank cell is an automated stop. A number copied from the previous job is a fabricated record with units attached. The load percentage, dwell duration, and hydraulic limit come from the approved test script or the engineering specification in force. This book does not invent them.

## What you may copy

You may copy the sheets in Chapter 16 into your project file, print them on waterproof paper, and fill them on the floor. You may not paste sentences from this book into a site method statement and call them the data hall's mandatory operating rule. The hall has its own operational permits, its own electrical flash boundaries, and its own piping and instrumentation diagrams (P&IDs). These sheets define what those permits and scripts must cover; they do not replace the engineer of record.

Two people must be on the tools for every test sequence: one measures with calibrated instrumentation, and one records in ink. The person authorized to command heat is a single name, written on the sheet before the first breaker is closed. Universal stop authority belongs to every person in the room.

## Decisions to record before the first step

- The exact boundary sentence this load-bank test is commissioned to prove.
- The physical test unit: which coolant distribution unit (CDU), which manifold trunk, and which rack positions—not an abstract hall.
- Which of the seven sheets this test will execute, and which are designated as not applicable in signed writing.
- The designated single authority permitted to command thermal load.
- The physical location of the emergency stop mechanisms and the secondary de-energization path.

---

# 1. The claim

A liquid cooling verification project fails during its first week when nobody writes down the exact sentence it is hired to prove. "The liquid cooling works" is not an engineering claim; it is an aspirational wish. An auditable claim sentence names the physical plant, the electrical and hydraulic duty the load bank simulates, the facility water supply boundary conditions, and the exact commercial decision the facility owner will make when the test pack is returned.

On the AI data hall projects from which this field guide is drawn, that commercial decision was whether the facility cooling infrastructure was legally and mechanically acceptable for IT deployment. It was not whether an accelerated compute chip would successfully run a distributed model training workload. It was not whether a prototype liquid load bank met manufacturing R&D standards. Those claims belong to other engineering scopes, other test benches, and other signatures.

```
+----------------------------------------------------------------------------------------------------+
| THE BOUNDARY OF THE CLAIM SENTENCE |
+------------------------------------+---------------------------------------------------------------+
| WHAT THE CLAIM LEGALLY PROVES | WHAT THE CLAIM CANNOT PROVE |
+------------------------------------+---------------------------------------------------------------+
| • CDU heat transfer at 1.2 MW duty | • Silicon compute efficiency or tensor performance |
| • Secondary pump N+1 failover speed| • Quick-disconnect long-term galvanic corrosion rates |
| • Manifold reverse-return balance | • Facility central chiller plant seasonal free-cooling PUE |
| • Enthalpy heat closure >= 97.0% | • Prototype load-bank heater element manufacturing durability|
| • 2N electrical feed transfer ride | • Facility building envelope structural wind-load compliance |
+------------------------------------+---------------------------------------------------------------+
```

## Formulating the project claim

Draft the sentence before you count load banks. The required machine count and electrical topology are consequences of the sentence, not its origin. If the claim is restricted to a single 1.2 MW in-row Coolant Distribution Unit (CDU) feeding ten 120 kW rack footprints, you do not deploy forty load banks across an entire row simply because the general contractor rented them for the month. If the claim encompasses the white space envelope—including the CRAH units or fan walls that capture the residual 15% to 20% convective air load escaped from the liquid cold plates—then the air-side thermal boundary must be explicitly stated in the claim sentence, or the test is structurally invalid.

In full facility commissioning, the Owner’s Project Requirements (OPR) is an exhaustive contractual volume. On a liquid cooling verification that commences after the facility structure and mechanical piping are already erected, you require that same governance distilled into a single, binding page:
1. What operational metrics must be demonstrated before production servers are cleared for delivery?
2. Which physical systems are inside the verification boundary?
3. Which plant systems are explicitly excluded?

If the owner already possesses an approved OPR page, audit it against the physical piping on the floor. Do not silently amend it in the margins of a field test script. If the owner lacks this document, the one-page claim is the prerequisite paper you draft and get signed in ink before uncrating a single tool. An unsigned claim guarantees that the final closeout meeting will degenerate into a dispute over what the testing party was compensated to demonstrate.

## Auditing the Basis of Design (BOD)

The Basis of Design (BOD) is the companion document. It articulates the engineering assumptions, heat transfer coefficients, and control logic intended to fulfill the owner's claim. You audit the BOD against the physical data hall as it stands, not against the preliminary design drawings.

You never average out the difference between drawing and installation. If the BOD specifies a DN150 reverse-return secondary header with 25% Propylene Glycol (PG25) fluid, and the as-built installation is a DN100 direct-return manifold charged with demineralized water and corrosion inhibitors, that discrepancy is not an acceptable "field adjustment." It is a critical design deviation that must be recorded on the claim cover before anyone plots a pump curve or declares the system "compliant."

What the verification cannot prove must sit on the same page as what it proves. It does not certify the server manufacturer's warranty. It does not accept the liquid load bank itself; that acceptance occurred under the factory protocols of Book 01, or it did not, and this verification will not quietly perform factory acceptance testing under the guise of site commissioning. It does not validate an unlisted quick disconnect coupling, an unverified biocidal chemistry, or a minimum flow floor that the project specification has failed to quantify. Those data cells remain blank until the test script cites the governing document. A blank cell is an intentional stop. An unverified number recalled from memory is a defect disguised as data.

Finally, the claim establishes the operational state of the hall:
- **Empty Hall Verification**: Conducted before any production IT hardware or live network fabric is energized in the room.
- **Maintenance Outage Window**: Conducted on an isolated loop during a scheduled facility shutdown.
- **Live Hall Proximity**: Conducted on a shared mechanical plant where adjacent rows support active production workloads.

A method statement written for an empty data hall that is applied to a live facility without explicit risk mitigation is an unapproved incident waiting to trigger a client outage. If the facility is live, the site's Standard Operating Procedures (SOPs) and Method of Procedure (MOP) protocols supersede this book, and their governing document numbers must head the claim sheet.

## Decisions to record before test start

- The signed project claim sentence, countersigned by Owner PE and Cx Lead.
- The physical equipment inventory within scope, and the list of excluded plant.
- The specific Basis of Design (BOD) revision audited, including all logged physical deviations.
- The concrete commercial decision the owner will make from the verified test pack.
- The operational state of the facility (empty, planned outage, or live data hall rules).

---

# 2. Twelve products, in order

Professional commissioning does not begin with thermal energy. It begins with a strict sequence of twelve engineering products. If you skip a product in this hierarchy, every subsequent signature is certifying work that was never legally documented or physically witnessed.

The twelve products constitute a progression of accountability, not a project management calendar. In an existing data hall where physical construction is already complete, certain products represent documentation you audit and attach rather than activities you execute from scratch. However, none of the twelve products may be omitted through silence.

```
+--------------------------------------------------------------------------------------------------+
| THE TWELVE COMMISSIONING PRODUCTS IN ORDER |
+----+----------------------------------+----------------------------------------------------------+
| 01 | Owner's Project Requirements | The auditable claim sentence and operational boundary. |
| 02 | Basis of Design (BOD) | The design engineer's roadmap for satisfying the OPR. |
| 03 | Approval of OPR & BOD | Mutual signed baseline before scripts are authored. |
| 04 | Design Review Record | Formal record of design audit or signed scope exclusion. |
| 05 | Commissioning Plan (Cx Plan) | Scope, schedule, gates, protocols, and team governance. |
| 06 | Specification Requirements Audit | Traceability matrix of contract testing clauses. |
| 07 | Construction Checklists (PFC) | Static, de-energized, pre-functional QA/QC verification. |
| 08 | Functional Test Procedures (FPT) | Pre-approved, step-by-step dynamic execution scripts. |
| 09 | Verification & Witness Records | Third-party witnessed execution logs and field sheets. |
| 10 | Issues Log / Punch List Register | Tracked register of defects, owners, and closure tests. |
| 11 | Regular Commissioning Reports | Daily shift notes and weekly executive summaries. |
| 12 | Systems Manual & Final Cx Report | Complete as-tested operational baseline and turnover pack.|
+----+----------------------------------+----------------------------------------------------------+
```

## The Products Deconstructed

### 01. The Owner's Project Requirements (OPR)
This is the auditable claim defined in Chapter 1. It explicitly establishes the temperature, flow, electrical density, and redundancy metrics required for IT operational acceptance.

### 02. The Basis of Design (BOD)
The document authored by the Mechanical, Electrical, and Plumbing (MEP) engineer of record explaining how the plant equipment, pipe diameters, control loops, and pumps achieve the OPR. On a landed verification job, you obtain the latest as-built revision. You do not draft a competing BOD in the field test report.

### 03. Review and Approval of OPR and BOD
Formal sign-off by the key stakeholders—the facility owner, the general contractor, and the commissioning authority (CxA). An unapproved requirement is merely a working draft. A test executed against an unapproved draft can be rejected when the owner changes leadership, forcing expensive re-mobilization.

### 04. The Design Review Record
A documented audit of the hydraulic and electrical schematics against industry guidelines (such as ASHRAE Technical Committee 9.9 and Open Compute Project standards). If your contract starts after facility completion, this product is either the documented verification of previous design reviews, or an explicit written statement signed by the owner stating that design auditing is excluded from your scope. It is never left as a blank space in the closeout index.

### 05. The Commissioning Plan (Cx Plan)
The master governance document. It defines the testing boundaries, resource allocations, witnessing protocols, communication matrices, and gating rules. A Gantt chart is not a commissioning plan; a Gantt chart is a timeline visualization. The Cx Plan articulates the technical gates, the stop criteria, and the document management structure.

### 06. Commissioning Requirements in Contract Documents
The audit of testing clauses embedded within mechanical and electrical contract specifications (such as CSI Division 23 for HVAC and Division 26 for Electrical). In an existing facility, you cannot modify finished contracts; you compile a matrix indicating which specific testing clauses you are verifying against, and which cannot be fulfilled due to historical documentation omissions.

### 07. Construction Checklists (Pre-Functional Checklists - PFC)
The physical, static verification sheets completed while the plant is completely de-energized. These verify equipment tags, physical alignment, uncrating condition, torque marks on electrical lugs, pipeline hydrostatic pressure holds, and system flushing. A physical walk-through conducted without a pre-printed checklist is merely an informal stroll.

### 08. Functional Test Procedures (FPT)
The approved, step-by-step test scripts governing every dynamic sequence. Each procedure must document the initial conditions, exact step instructions, instrument classes, expected numerical bands, and specific stop limits. An execution script authored on site the morning of the test is an unacceptable draft; its "expected results" inevitably mirror whatever the mechanical plant happens to do.

### 09. Verification and Witness Records
The physical execution of the approved scripts. Witnessing and executing are separate legal duties. The technician operating the control valves and breaker handles cannot act as the sole witness accepting the line item. When a single individual wears both hats, unconscious bias inevitably compromises the data.

### 10. The Issues Log / Punch List Register
An exhaustive tracker recording every defect, deviation, leak, sensor error, and control oscillation. Each entry must document the date, script step, severity tier, responsible contractor, required remediation, and re-test acceptance criteria. A defect noted only in a verbal conversation or chat thread does not legally exist.

### 11. Regular Commissioning Reports
Daily shift notes submitted at the end of each operational window, and weekly summary reports distributed to executive stakeholders. The reporting format must be agreed upon at the kickoff meeting, including the format for days where testing was halted. A blank day without a daily report is a failure of project controls.

### 12. The Systems Manual and Final Commissioning Report
The comprehensive handover archive. It includes all signed master sheets, calibrated instrument certificates, raw time-series data files, BMS trend logs, resolved punch lists, and the operational guidelines required by facility engineers to operate the plant within its verified boundaries.

Do not renumber or combine these twelve deliverables to accommodate local contractor habits. If a specific product is excluded by contract, the Commissioning Plan must explicitly state that exclusion, and the Final Report must reaffirm it. Professional compliance is preserved by documenting boundaries, never by silence.

## Decisions to record before test start

- The twelve products classified as: to be produced, to be attached from prior work, or excluded in signed writing.
- The approved document numbering convention and revision control policy.
- The hosting repository and security permissions for the master Issues Log.
- The distribution list and deadline hours for daily shift notes.

---

# 3. Two numberings

This chapter prevents an accurate site test report from being filed into an audit binder as fraudulent documentation.

In global mission-critical data center commissioning, documentation is structured around seven standard completion certificate tiers. Simultaneously, local mechanical contractors frequently communicate using a colloquial "three-stage" vocabulary. When these two vocabularies are carelessly conflated, audit compliance collapses.

![Commissioning Gate Ladder](../figures/fig-01-cx-gate-ladder.png)

## The Global Standard: Levels 0 Through 6

Modern commissioning frameworks (governed by ASHRAE Guideline 0-2019, ASHRAE Guideline 1.1, and the AABC Commissioning Group) define seven formal completion certificates:

- **Level 0: Design and Planning.** Audit of OPR, BOD, and engineering specifications. Certification that design intent and commissioning requirements are fully integrated.
- **Level 1: Factory Acceptance Testing (FAT).** Witnessed testing at the manufacturing plant (CDU vendor, chiller factory, load-bank fabricator). Validates pressure vessels, pump curves, and controls under factory conditions.
- **Level 2: Component Delivery, Receipt, and Static QA.** Uncrating, physical visual inspection, seismic anchoring verification, torque testing, and static de-energized electrical insulation checks.
- **Level 3: Pre-Functional Checks (PFC) and System Start-Up.** Chemical pipe flushing, hydrostatic pressure holds, vacuum deaeration, fluid charging, initial equipment energization, and manufacturer startup.
- **Level 4: Functional Performance Testing (FPT).** Dynamic testing of individual, isolated machines. Proves autonomous CDU pump sequencing, modulating valve response, local VFD control loops, and instrument point-to-point telemetry.
- **Level 5: Integrated System Testing (IST).** Multi-system dynamic verification under full simulated thermal heat. Verifies row-level manifold balance, multi-tier thermal steps, 2N power loss failover, primary cooling interruption ride-through, and emergency shutdown cascades.
- **Level 6: Close-Out, Turnover, and Operations Handover.** Resolution of all punch list items, final systems manual submission, operations team training, and handover to live site facilities engineering.

## The Local Dialect: Three Stages

On a retrofit project or a completed hall where a liquid verification team is mobilized specifically for a load-bank campaign, contractors routinely use an informal three-stage shorthand:
- **Stage 1: Static Acceptance (No Energy).** Physical installation, cable checks, hose connections, and pressure holds.
- **Stage 2: Single-System Function.** Individual CDU startup, pump rotation, and local alarms.
- **Stage 3: Integrated Thermal Performance.** Energizing the load banks, stepping through heat, and simulating facility power drops.

The stage sequence itself is logically sound: you do not energize equipment that has not passed static inspection, and you do not apply thermal load to a loop whose pumps have not been functionally proven. The hazard lies in the numbering.

## The Compliance Trap

Contractors frequently label their Stage 1 static walk-through as "Level 1 Testing" in project folders. When an auditor or client compliance officer reviews the project binders, they open the tab marked "Level 1: Factory Acceptance Testing" and discover a clipboard checklist verifying that secondary hoses were unboxed and clamped to a manifold.

Filing a site walk-through into a factory acceptance binder is documentation fraud. Even if every checkbox on that site checklist represents diligent physical work, the certificate is invalid because Level 1 requires factory test bench data, factory calibration sheets, and manufacturing witness signatures.

To prevent this compliance breach, the first page of the Commissioning Plan must feature a prominent cross-reference matrix:

```
+----------------------------------------------------------------------------------------------------+
| COMMISSIONING TIER TRANSLATION MATRIX |
+--------------------------+----------------------------+--------------------------------------------+
| GLOBAL CERTIFICATE TIER | LOCAL FIELD CONTRACTOR TERM| MANDATORY VERIFICATION BOUNDARY |
+--------------------------+----------------------------+--------------------------------------------+
| Level 0: Design Audit | Excluded / Attached | OPR & BOD sign-off; design review waiver. |
| Level 1: Factory Testing | FAT Vendor Documentation | Factory test records attached as evidence. |
| Level 2: Site Receipt QA | Stage 1 (Static Part A) | Sheet 1: Unpack, megger, phase rotation. |
| Level 3: PFC & Start-Up | Stage 1 (Static Part B) | Sheet 1: Flush, hydro-hold, fill and vent. |
| Level 4: Functional (FPT)| Stage 2 (Single System) | Sheet 2, Sheet 6, Sheet 7: CDU & alarms. |
| Level 5: Integrated (IST)| Stage 3 (Heat Window) | Sheet 3, Sheet 4: Thermal ladder & 2N pull.|
| Level 6: Turnover | Closeout Handover | Sheet 5, Punch list clearance, Cx pack. |
+--------------------------+----------------------------+--------------------------------------------+
```

## Mandatory Gating and Interlock Rules

A core tenet of commissioning governance is that no project may advance across a level boundary while unresolved defects exist in the preceding tier:

1. **Static Prerequisite Gate**: Level 4 Functional Performance Testing cannot commence if Level 3 Pre-Functional Checklists remain unsigned. Operating a CDU pump through an unverified, un-flushed secondary loop risks circulating metal shavings and construction debris directly into plate heat exchangers and quick disconnect valves.
2. **Thermal Prerequisite Gate**: Level 5 Integrated System Testing cannot commence if Level 4 single-system safety trips or pump changeover routines have failed. Introducing megawatts of thermal energy into a system with an unverified N+1 pump changeover guarantees an uncontrolled thermal runaway when a pump inevitably trips.
3. **The "Fix It During Heat" Trap**: When a contractor pleads, "Let us proceed with the heat test today and we will resolve the pump changeover issue tomorrow," the Commissioning Lead must issue an immediate stop. Thermal energy does not rectify mechanical and electrical defects; it magnifies them under high risk.

If an owner chooses to waive an open defect to maintain an aggressive project schedule, that waiver must be documented as a formal written deviation signed in ink by the Owner’s Project Engineer. The waiver must explicitly define the compensatory safety controls deployed on site. An informal verbal agreement is completely invalid.

## Decisions to record before test start

- The mapping between local stage terms and formal Level 0–6 certificate binders.
- The specific certificate levels this verification scope is authorized to issue.
- The certificate levels excluded from scope, accompanied by formal scope letters.
- The non-negotiable prerequisite gates governing transitions between Levels 2/3, Level 4, and Level 5.
- The single authority empowered to execute formal deviation waivers.

---

# 4. People and the governance ring

A liquid cooling verification conducted without clearly designated individual roles rapidly degenerates into an uncoordinated group discussion. The standard method statement calls for an exhaustive RACI matrix (Responsible, Accountable, Consulted, Informed). In the high-stakes environment of a live or near-live data hall, that structure must be distilled into three distinct commercial entities and five specific engineering functions.

```
+----------------------------------------------------------------------------------------------------+
| THE THREE-PARTY GOVERNANCE TRIANGLE |
+------------------------------------+---------------------------------------------------------------+
| THE FACILITY OWNER | Witnesses execution, authorizes deviations, and signs off |
| (Client / Hyperscaler Ops) | final certificate tiers. Does not operate tools. |
+------------------------------------+---------------------------------------------------------------+
| THE VERIFICATION AUTHORITY (CxA) | Authors Cx Plan & scripts, manages calibration, directs steps,|
| (Independent Testing Agency) | records data, and audits punch list. Never closes own defect. |
+------------------------------------+---------------------------------------------------------------+
| THE TRADE CONSTRUCTOR | Supplies as-built drawings, operates breakers and valves, |
| (General / Mechanical / Electrical)| and performs physical punch list repairs under permit. |
+------------------------------------+---------------------------------------------------------------+
```

## The Three Commercial Parties

The boundary between these three entities must be strictly enforced.
- **The Facility Owner**: Holds ultimate commercial authority. They witness the critical operational steps and sign the Level 4 and Level 5 completion certificates. The owner’s representative does not write field scripts while standing in the aisle, nor do they turn valve handles.
- **The Verification Party**: Authors the Commissioning Plan and test scripts, directs the execution sequence, and witnesses every measurement. They maintain the master punch list and will never sign off on their own punch list item without an independent secondary inspection.
- **The Constructor**: Provides original equipment submittals and as-built drawings, energizes breakers, operates manual isolation valves, and physically rectifies defects identified on the punch list.

If a single engineering firm is contracted to perform both construction and commissioning, that conflict of interest must be formally documented on page one of the Commissioning Plan. When the installer and the verification witness belong to the same organizational hierarchy, project governance is inherently compromised unless separate, non-reporting personnel execute and witness each task.

## The Five Functional Hands

Within the testing team on the floor, five distinct technical functions must be staffed. These represent functional responsibilities rather than a requirement for five separate bodies; on a smaller test, one experienced engineer may cover multiple disciplines. However, no individual may act as the sole witness for an operational task they physically performed.

```
+--------------------------------------------------------------------------------------------------+
| THE FIVE FUNCTIONAL DISCIPLINES |
+-------------------+------------------------------------------------------------------------------+
| 1. TEST LEAD | Owns the approved testing window, enforces the claim, directs step timing, |
| | manages communications, and holds sole authority to initiate thermal load. |
+-------------------+------------------------------------------------------------------------------+
| 2. ELECTRICAL PE | Directs lock-out/tag-out (LOTO), conducts megger insulation & ground testing,|
| | verifies phase rotation, monitors upstream PDU trip curves, and runs IR scans|
+-------------------+------------------------------------------------------------------------------+
| 3. MECHANICAL PE | Manages secondary fluid loop, oversees hydrostatic pressure holds & venting, |
| | audits CDU pump curves, and tracks quick disconnect seal integrity. |
+-------------------+------------------------------------------------------------------------------+
| 4. CONTROLS PE | Cross-checks BMS telemetry against calibrated field gauges, validates Modbus/|
| | BACnet registers, and injects hardware alarm faults to verify trip logic. |
+-------------------+------------------------------------------------------------------------------+
| 5. TEST TECH | Manages physical load-bank connections, verifies instrument calibration logs,|
| | records all measured values in ink on master sheets, and maintains archives. |
+-------------------+------------------------------------------------------------------------------+
```

### 1. The Test Lead
Owns the approved testing window, coordinates with facility operations, directs step transitions, and ensures testing adheres strictly to the approved script revision. The Test Lead does not hold an instrument in their hand; their attention is focused on system stability, protocol compliance, and overall safety.

### 2. The Electrical Engineer
Directs lock-out/tag-out (LOTO) protocols, conducts static megger insulation resistance tests, verifies phase sequence with a rotation meter, audits upstream breaker settings, and performs thermal imaging on all high-current busbars, cables, and contactors. Phase rotation is a safety-critical electrical parameter; a reversed phase sequence can cause a canned secondary pump to spin backward, resulting in severe cavitation, zero pressure development, and rapid impeller destruction.

### 3. The Mechanical Engineer
Oversees the fluid path: secondary piping, hose routing, quick disconnect couplings, air venting, and chemical fluid composition. They verify the hydrostatic pressure test records, monitor expansion tank nitrogen pre-charge levels, and supervise the baseline pump curve execution.

### 4. The Controls Engineer
Cross-checks the Building Management System (BMS) and CDU supervisory interface against calibrated field instruments. They confirm register addresses, verify sensor offset calibrations, and orchestrate the simulated alarm tests (such as low flow, high temperature, and liquid leak detection). A BMS display that merely mirrors another display is not an accepted control verification.

### 5. The Test Technician
Verifies physical equipment against the packing list, monitors tool calibration certificates, and manages the field record sheets. One technician measures with calibrated field instruments while a second technician immediately logs the readings in ink. A lost record sheet voids the test day, regardless of how well the mechanical plant performed.

## Authority to Command Heat vs. Universal Stop Authority

The distribution of authority during dynamic testing follows two absolute rules:

1. **Singular Command Authority**: Thermal heat may be commanded by exactly **one individual**—the designated Test Lead. That individual's name is recorded in ink on Sheet 3 before the first breaker is engaged. No load step may be initiated by verbal suggestion from the owner, the contractor, or an observing vendor.
2. **Universal Stop Authority**: An emergency stop may be called by **any individual present in the data hall**. This authority is absolute, non-negotiable, and requires no prior approval from the Test Lead. If a technician spots a leaking quick disconnect, an electrical apprentice detects an unusual odor, or an observer feels uncertain about an operational transient, they call an immediate stop. The system is shut down instantly without debate.

```
+----------------------------------------------------------------------------------------------------+
| COMMAND AND STOP GOVERNANCE |
+--------------------------------------------------+-------------------------------------------------+
| WHO MAY COMMAND HEAT | WHO MAY CALL AN EMERGENCY STOP |
+--------------------------------------------------+-------------------------------------------------+
| • Exactly ONE named person on site. | • EVERY PERSON in the room. |
| • Recorded in ink on Sheet 3 before first step. | • Requires zero consensus or prior approval. |
| • Must confirm all prerequisite gates are signed.| • Overrides all project schedules and costs. |
| • Operates strictly within approved script steps.| • Survives the organizational chart completely. |
+--------------------------------------------------+-------------------------------------------------+
```

## The Kickoff Meeting Governance

These responsibilities are formalized during the Commissioning Kickoff Meeting, held prior to site mobilization. Attendance is mandatory for all personnel authorized to execute or witness testing.

The kickoff meeting achieves five non-negotiable outcomes:
1. All functional roles are assigned to named individuals with 24-hour contact details.
2. The specific test script document numbers and their approved revision numbers are frozen.
3. The definition of the "Approved for Execution" document status is formally established; any script in "Draft," "Under Review," or "Informational" status is legally prohibited from floor execution.
4. The master Issues Log repository is established with clear read/write access controls.
5. The emergency escalation chain is verified, including the utility isolation lead, the fire systems engineer, and the mechanical spill containment lead.

## Decisions to record before test start

- The three participating corporate entities, noting any dual-role appointments.
- The names, contact numbers, and professional licenses assigned to each of the five functional roles.
- The single designated individual authorized to command thermal load.
- Re-affirmation that every individual on site holds unhindered emergency stop authority.
- The formal script approval status that authorizes floor testing.

---

# 5. The weeks before the window

The thermal heat window in a data hall typically spans only a few days. The commissioning project itself is the intense month of preparation surrounding those days. Seasoned commissioning engineers treat the preparation month as the decisive phase of the project, with the heat window serving merely as the witnessed validation.

A test team that rolls load banks into an unfamiliar hall without a rigorous pre-mobilization survey will waste the first half of their thermal window diagnosing missing adapters, tripping upstream PDU breakers, or arguing about unverified floor loading ratings.

```
+----------------------------------------------------------------------------------------------------+
| PRE-MOBILIZATION MILESTONE TIMELINE |
+-------------------+--------------------------------------------------------------------------------+
| T - 4 WEEKS | Site Access & Structural Survey: Path-of-travel, freight elevator capacity, |
| | floor live load (kN/m²), electrical tap boxes, and manifold connection audit. |
+-------------------+--------------------------------------------------------------------------------+
| T - 3 WEEKS | Calibration & Instrumentation Audit: ISO 17025 certificates verified for all |
| | power meters, ultrasonic flowmeters, PT100 immersion probes, and IR cameras. |
+-------------------+--------------------------------------------------------------------------------+
| T - 2 WEEKS | Emergency Response & MOP Authorization: Chemical spill containment, E-Stop |
| | procedures, and energization permits signed by Owner and Facility Operations. |
+-------------------+--------------------------------------------------------------------------------+
| T - 1 WEEK | Floor Readiness & Blank Sheets: Script revision freeze, master sheets printed |
| | in ink, test gear staged on site, secondary loop flushed and statically tested.|
+-------------------+--------------------------------------------------------------------------------+
```

## Equipment Count and Spare Strategy

Do not finalize an equipment rental order until the claim sentence is formally signed. Sizing load banks from a generic template risks ordering the wrong topology. Calculate the equipment count directly from the certified claim:
- **Liquid Thermal Duty**: Total kW simulated at the secondary manifold (e.g., ten 120 kW load banks for a 1.2 MW row).
- **Air-Side Rejection**: If the claim includes whitespace thermal stability, ensure the 15% to 20% convective air load is accounted for via dedicated fan-assisted load-bank coils or auxiliary air heaters.
- **The N+1 Cold Spare Path**: Always mobilize an additional load bank, spare high-pressure hoses, and duplicate quick-disconnect couplings. A load bank that suffers a control board failure or transit damage during transport is a logistical reality; having a verified spare staged on site keeps the multi-million-dollar testing window on schedule.

## The Site Access and Structural Survey

The site survey is a critical engineering gate, not an informal walk-through. It answers four mandatory questions:

1. **Path-of-Travel and Ingress**: Can the equipment physically navigate the route from the loading dock to the data hall? Measure freight elevator door clearances, elevator weight limits, corridor turn radii, and ramp slopes. Confirm that the access path does not require rolling heavy load-bank castors across unfinished tile seams or unprotected raised floor panels.
2. **Structural Floor Loading**: Verify that the combined weight of the load banks, coolant-filled manifolds, and personnel does not exceed the floor's live-load rating (typically 12.0 kN/m² to 15.0 kN/m² for heavy data halls). Verify this against structural engineering stamped drawings. Inspect raised-floor pedestal understructure, stringer bolting, and seismic bracing.
3. **Electrical Infrastructure Tap**: Inspect the Power Distribution Units (PDUs) or overhead busway tap boxes feeding the test row. Verify breaker frame sizes, trip unit settings (electronic LSIG parameters), phase pinout configurations, and receptacle types. Compare the load bank’s inrush and rated full-load amperage against the upstream protective coordination curve to prevent tripping upstream sub-station breakers during step loading.
4. **Hydraulic Interfaces**: Physically inspect the secondary supply and return manifold taps. Document pipe diameters, isolation valve models, and quick-disconnect coupling geometries (e.g., Danfoss Hansen FD83 series or ISO 16028 flush-face couplings). Never assume fitting interchangeability; verify gender, thread pitch, and O-ring elastomer compatibility (EPDM for glycol/water loops; never use standard Buna-N with high-temperature glycols).

A survey note documenting any inaccessible areas, unverified valves, or undocumented circuit breakers must be formally published. Undocumented physical interfaces must be resolved as formal pre-mobilization deviations before equipment leaves the warehouse.

## Instrument Traceability and Calibration Standards

All verification measurements are legally dependent on the calibration integrity of the field instruments. A measurement recorded with an uncalibrated instrument is merely an unverified opinion.

Every field instrument deployed during the campaign must possess an active, traceable calibration certificate (ISO/IEC 17025 accredited) that remains valid throughout the entire duration of the testing window:

```
+----------------------------------------------------------------------------------------------------+
| MINIMUM INSTRUMENT ACCURACY STANDARDS |
+--------------------------+-----------------------+-------------------------------------------------+
| INSTRUMENT CLASS | ACCURACY STANDARD | MANDATORY FIELD DEPLOYMENT SPECIFICATION |
+--------------------------+-----------------------+-------------------------------------------------+
| Power Quality Analyzer | Class 0.2 (0.2% FS) | Calibrated 3-phase active power & THD analyzer. |
| Ultrasonic Flow Meter | Class 0.5 (+/- 0.5%) | Dual-channel transit-time clamp-on; 10D/5D run. |
| Immersion Temp Probes | 4-wire PT100 1/3 DIN | Calibrated to +/- 0.05 K; high-thermal paste. |
| Differential Pressure | +/- 0.1% Full Scale | Calibrated piezoresistive transmitter. |
| Thermal Imaging Camera | NETD < 40 mK; +/- 1 K | Calibrated focal plane array (384x288 min). |
+--------------------------+-----------------------+-------------------------------------------------+
```

If an instrument's calibration expires during the project, it must be removed from service and replaced with a certified backup. An expired certificate invalidates all data recorded from that moment forward.

## The Emergency Action Plan (EAP) and Site Permits

Before making the first mechanical connection, the Emergency Action Plan must be reviewed and signed by all parties. The plan must explicitly detail actions for four specific scenarios:
1. **Secondary Fluid Spill / Leak**: Immediate pump isolation, vacuum recovery, spill containment socks deployed, and environmental reporting.
2. **Electrical Flash / Insulation Failure**: Immediate upstream PDU emergency trip, arc flash perimeter controls, and medical emergency escalation.
3. **Uncontrolled Thermal Runaway**: Immediate load-bank de-energization sequence, CDU bypass valve override, and facility chilled water max-flow command.
4. **Life Safety Alarm (VESDA / Fire Suppression Activation)**: Evacuation paths, personnel accountability, and coordination with automated EPO circuits.

All required working permits must be secured prior to mobilizing tools:
- **Energization Permit**: Authorization to close breakers and energize temporary loads.
- **Hot Work Permit**: Required if any welding, soldering, or thermal stress tests are planned.
- **Mechanical Fluid Permit**: Authorization to connect to facility liquid loops, purge air, and circulate fluid.

## Pre-Printed Master Sheets and Shift Reporting

Design and print all blank master record sheets (Chapter 16) before arriving on site. Each sheet must clearly list the script step number, instrument ID, and expected numerical tolerance bands, with blank cells reserved for physical field measurements. Developing record sheets after testing starts invariably leads to omitted parameters and selective logging.

Establish the daily shift reporting protocol during the kickoff meeting. Every operational shift concludes with a formal Daily Shift Note detailing:
- The exact test script revision executed.
- Ambient environmental conditions and facility baseline state.
- Key operational milestones achieved.
- Unscheduled stops or safety halts, including root-cause assessments.
- Newly logged punch list items and any re-tested closures.
- Confirmed schedule and test scripts for the subsequent shift.

If testing was halted for the day due to upstream facility issues or mechanical failures, a Daily Shift Note must still be published stating: "Zero scripts executed; testing halted due to [specific reason]." A missing shift note creates an audit gap that cannot be repaired after demobilization.

## Decisions to record before test start

- The load-bank capacity and cold spare allocation, validated against the claim.
- The signed site survey report, including verification of floor loading and electrical capacities.
- The instrument calibration register, including serial numbers, certificate IDs, and expiration dates.
- The signed Emergency Action Plan and all active operational permits.
- Confirmation that physical master record sheets are printed and staged on site.

---

# 6. Scripts before heat

No dynamic commissioning test may be executed from memory or oral instructions. A test conducted without a pre-approved, step-by-step test script is merely an informal equipment demonstration. It cannot support an engineering completion certificate.

A script that the testing team drafted but which the Owner’s Project Engineer has not formally reviewed and signed is merely an internal working document. It carries no contractual authority. Executing against an unapproved draft leaves the testing team fully exposed to commercial disputes and legal liability if an equipment failure occurs.

```
+----------------------------------------------------------------------------------------------------+
| COMMISSIONING DOCUMENT HIERARCHY |
+------------------------------------+---------------------------------------------------------------+
| 1. CODES & STANDARDS | ASHRAE 0-2019, ASHRAE 90.4, NFPA 70, IEC 60364, BSRIA BG 29. |
+------------------------------------+---------------------------------------------------------------+
| 2. CONTRACT SPECIFICATIONS & BOD | CSI Div 23 & 26, Owner Project Requirements, As-Built P&IDs. |
+------------------------------------+---------------------------------------------------------------+
| 3. COMMISSIONING PLAN (Cx Plan) | Governance rules, level gates, witness protocols, schedules. |
+------------------------------------+---------------------------------------------------------------+
| 4. FUNCTIONAL TEST PROCEDURES (FPT)| Pre-approved, step-by-step scripts with exact numeric bands. |
+------------------------------------+---------------------------------------------------------------+
| 5. MASTER FIELD SHEETS (INK LOGS) | Floor records signed in ink; raw time-series sensor files. |
+------------------------------------+---------------------------------------------------------------+
```

## The Anatomy of an Auditable Test Script

Every Functional Test Procedure (FPT) and Integrated System Test (IST) script must be structured with consistent, auditable engineering sections:

1. **Test Scope and Boundary**: The specific mechanical and electrical components under test, and the exact physical boundary separating them from adjacent operational equipment.
2. **Governing Reference Documents**: Direct citations of the governing P&ID revision, electrical single-line diagram (SLD), and equipment submittals. Every tolerance must reference a specific contract clause or manufacturer standard; an acceptance tolerance with no cited source is merely an unverified opinion.
3. **Instrumentation and Calibration Schedule**: The specific instrument classes, serial numbers, and calibration certificate IDs required to execute the procedure.
4. **Prerequisite Verification Gate**: Written verification that all preceding level requirements (such as static uncrating, de-energized megger checks, and hydrostatic pressure holds) are fully signed off.
5. **Safety Controls and Environmental Boundaries**: Mandatory Personal Protective Equipment (PPE), arc-flash boundary definitions, spill containment staging, and verified emergency stop paths.
6. **Step-by-Step Execution Sequence**: A sequential table detailing every manual action, the exact physical feedback to observe, the expected numerical tolerance band, and dedicated sign-off cells for measured data and witness initials.
7. **Explicit Stop Conditions**: Clear operational limits that mandate an immediate test halt if breached (such as secondary coolant temperature exceeding 45.0°C, secondary pressure dropping below 100 kPa, or supply phase voltage unbalance exceeding 2.0%).

```
+----------------------------------------------------------------------------------------------------+
| STANDARD TEST SCRIPT STEP STRUCTURE |
+----+-----------------------+-----------------------------+--------------------+-------+------------+
|STEP| ACTION COMMAND | EXPECTED PHYSICAL RESULT | ACCEPTANCE BAND |MEASURE|SIGN / TIME |
+----+-----------------------+-----------------------------+--------------------+-------+------------+
|4.2 | Ramp Load Bank to 50% | Active power stabilizes | 600 kW +/- 1.5% | [ ] | Init: ____ |
| | (Step 2: 600 kW total)| Secondary supply T increases| 36.0°C +/- 0.5°C | [ ] | Time: ____ |
| | Dwell: 45 minutes | Heat balance closure ratio | 97.0% to 101.5% | [ ] | Sheet 3 ref|
+----+-----------------------+-----------------------------+--------------------+-------+------------+
```

## Freezing Script Revisions on the Floor

The Commissioning Kickoff Meeting establishes the specific approval status required before a script may be executed on the floor. Only scripts bearing the formal status stamp **"APPROVED FOR EXECUTION - REV [X]"** are permitted in the data hall.

If during testing the mechanical plant exhibits unexpected dynamics that the approved script did not anticipate, modifying the script on the floor with a pencil note is strictly prohibited. Uncontrolled redlining allows the test procedure to quietly adapt to whatever the plant happens to do.

When a procedural modification is necessary:
- The Test Lead pauses the test.
- A formal Engineering Change Notice (ECN) is drafted documenting the deviation, its technical justification, and the amended steps.
- The ECN is signed by the Test Lead, the Contractor Lead, and the Owner’s Project Engineer.
- The script revision is incremented (e.g., Rev 1.0 to Rev 1.1) and re-issued.

If the owner refuses the ECN, testing resumes under the original script, and the failure of the plant to meet the original expected result is logged on the master punch list.

## The Mandatory Script Suite for a High-Density Liquid Hall

A complete verification campaign requires a comprehensive suite of distinct, standalone scripts. Attempting to combine multiple operational verifications into a single high-level procedure produces an unwieldy document that inevitably glosses over critical safety and performance checks.

The verification campaign requires nine dedicated test scripts:

### Phase 1: Static Pre-Start Checklists (Level 2 / Level 3)
- **Script 01: Physical Uncrating, Alignment & Visual QA**: Verification of load-bank chassis integrity, hose routing, fitting seals, and seismic tie-downs.
- **Script 02: De-Energized Electrical Megger & Phase Rotation**: Insulation resistance testing (≥ 100 MΩ at 1000V DC), ground continuity (≤ 0.1 Ω), and confirmation of clockwise A-B-C phase sequence.
- **Script 03: Secondary Loop Flushing, Hydrostatic Hold & Air Purge**: Chemical flushing velocity verification (≥ 1.5 m/s per BSRIA BG 29/2020), hydrostatic pressure hold (1.5× working pressure for 2 hours with zero decay), and automatic deaeration.

### Phase 2: Single-System Functional Testing (Level 4 FPT)
- **Script 04: Autonomous CDU Startup, Flow & Pressure Baseline**: Verification of canned pump VFD ramp profiles, manual differential-pressure setpoint tracking, and cold system resistance.
- **Script 05: CDU N+1 Pump Failover & Autonomous Control**: Physical tripping of the primary pump VFD; verification of standby pump auto-start within < 1.5 s with zero loop cavitation.
- **Script 06: Alarm Injection & Point-to-Point Telemetry**: Physical injection of simulated faults (secondary low flow, expansion tank low level, leak detection rope wetting) and cross-checking BMS telemetry against local instrumentation.

### Phase 3: Integrated System Testing (Level 5 IST)
- **Script 07: Cold No-Heat Baseline Pump Curve**: Hydraulic head versus flow profiling across 4 manual valve throttling points with automated VFD control locked off.
- **Script 08: Multi-Tier Thermal Heat Ladder & Overload Dwell**: Stepped thermal execution (25%, 50%, 75%, 100% full design load, and 110% overload margin) with minimum 45-minute dwells and a 4-hour full-load soak.
- **Script 09: Dynamic Transient Failure & Emergency Shutdown**: 2N primary power feed cut, facility chilled water loss ride-through, and controlled de-energization shutdown sequence.

## The "One Script, One Signature" Principle

Every script in the suite stands as an independent contractual document with its own dedicated sign-off block. Combining a successful cold pump curve and a failed thermal overload step into a single combined signature creates a fundamentally ambiguous record.

Each script must produce its own unambiguous verdict: **PASS**, **FAIL**, or **NOT EXECUTED**. Any unresolved failure within a script immediately generates an entry in the master Issues Log.

## Decisions to record before test start

- The comprehensive list of all nine test scripts, with frozen revision numbers and signed approval stamps.
- The contract document numbers supporting every numerical tolerance and acceptance band.
- The formal ECN process for handling floor revisions.
- Confirmation that no script is in draft status.

---

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

---

# 8. One system at a time

Dynamic verification with multiple interconnected systems under thermal load is a later, integrated phase. This phase is dedicated to validating one machine at a time, executing the precise operational logic defined in its standalone test script while all adjacent systems remain quiet.

In the global commissioning hierarchy, this is **Level 4 Functional Performance Testing (FPT)**. It validates the autonomous protection, modulating control loops, and physical alarms of individual machines before they are subjected to multi-megawatt thermal stress. Filing single-system testing under Level 5 Integrated Systems Testing simply because the equipment is physically located in the data hall is a serious documentation error.

![CDU Hydraulic P&ID Architecture](../figures/fig-02-cdu-hydraulic-pandid.png)

## Autonomous Coolant Distribution Unit (CDU) Verification

The Coolant Distribution Unit is the critical hydraulic interface separating the facility primary water system (FWS) from the secondary technology cooling system (TCS). Before any thermal load is applied by the load banks, the CDU must prove its ability to control fluid circulation autonomously under Script 04 and Script 05.

### 1. Pump Startup, VFD Modulation, and Soft-Start
Energize the CDU secondary pumps with the primary facility loop isolated. Execute controlled start and stop cycles:
- Verify that the Variable Frequency Drives (VFDs) ramp the canned centrifugal pumps smoothly over their configured acceleration curve (typically 10 to 15 seconds) without causing electrical current spikes or hydraulic surges.
- Verify manual frequency override: drive the VFDs across their operating range (30.0 Hz to 50.0/60.0 Hz) and record motor current, power factor, and bearing vibration signatures.

### 2. N+1 Secondary Pump Auto-Changeover
Modern high-density CDUs employ an N+1 secondary pumping configuration (e.g., dual 100% capacity pumps, P-1A Lead and P-1B Standby). The automatic changeover logic must be verified through physical trip simulation:
- Operate Pump P-1A at 100% nominal speed with the loop at design operating flow.
- Simulate an electrical trip by opening the control circuit breaker to the P-1A inverter or triggering its digital fault input.
- **Acceptance Criteria**:
 - The local CDU controller must detect the fault, log a critical alarm, and issue a start command to standby Pump P-1B within ≤ 500 ms.
 - Standby Pump P-1B must accelerate to full operating speed and restore secondary differential pressure within ≤ 1.5 seconds.
 - The discharge non-return check valve on Pump P-1A must seat firmly without violent hydraulic slam (peak water hammer pulse must not exceed ± 50 kPa).
 - Secondary loop differential pressure must not drop below the minimum cavitation floor (100 kPa), ensuring continuous flow through the load banks without triggering false thermal trips.

### 3. Modulating Temperature Control Valve (TCV) Tracking
The primary loop Temperature Control Valve (TCV-101, typically a modulating 2-way or 3-way globe valve with an electronic actuator) regulates primary facility chilled water flow through the Plate Heat Exchanger (PHE-101) to maintain secondary supply temperature:
- Drive the actuator through its full control range using a 0–10V DC or 4–20 mA calibration source.
- Verify full-stroke opening and closing times against the manufacturer submittal (typically τ ≤ 30 seconds).
- Verify fail-safe position upon loss of control power: TCV-101 must fail mechanically open (100% primary flow) or hold last position depending on facility design intent.
- Verify seat leakage integrity: with the valve commanded 100% closed, confirm that primary flow drops to zero (leakage class ANSI/FCI 70-2 Class IV or better).

### 4. Secondary Differential Pressure Bypass Valve (BPV)
Inspect modulating bypass valve BPV-201, installed across secondary supply and return headers. Verify that as downstream manifold balancing valves are throttled, the BPV modulates open smoothly to maintain constant pump head, preventing impeller dead-heading.

## BMS Telemetry and Field Instrument Point-to-Point Checks

Never assume that a value displayed on a Building Management System (BMS) screen or CDU human-machine interface (HMI) reflects physical reality. Every telemetry point defined in the project claim must undergo physical point-to-point cross-checking against calibrated field reference instruments:

```
+----------------------------------------------------------------------------------------------------+
| POINT-TO-POINT TELEMETRY CALIBRATION AUDIT |
+---------------------+-------------------+---------------------+------------------+-----------------+
| TELEMETRY POINT | BMS / HMI READING | FIELD CALIBRATED REF| ALLOWABLE DELTA | AUDIT VERDICT |
+---------------------+-------------------+---------------------+------------------+-----------------+
| Secondary Supply T | 40.12 °C | 40.08 °C (PT100) | +/- 0.30 K | PASS |
| Secondary Return T | 50.25 °C | 50.15 °C (PT100) | +/- 0.30 K | PASS |
| Secondary Flow Rate | 115.4 m³/h | 116.1 m³/h (Ultrason)| +/- 2.0% | PASS |
| Secondary Supply P | 285.0 kPa | 282.5 kPa (Gauge) | +/- 10.0 kPa | PASS |
| Secondary Return P | 115.0 kPa | 118.0 kPa (Gauge) | +/- 10.0 kPa | PASS |
| Expansion Tank Level| 68.0 % | 67.5 % (Sight Glass)| +/- 3.0 % | PASS |
+---------------------+-------------------+---------------------+------------------+-----------------+
```

If a discrepancy exceeds the allowable tolerance, the sensor offset must be recalibrated or the sensor replaced. Never adjust the acceptable tolerance band to match a drifting sensor.

## Physical Hardware Alarm Injection

Alarms must be validated through physical hardware injection. Simulating an alarm by altering a software setpoint in a configuration file or toggling a bit in an engineering workstation is completely unacceptable. Software simulation proves that software can read a variable; it does not prove that the physical sensor, field wiring, and relay logic function under real-world conditions.

Execute physical alarm testing under Script 06:
- **Secondary Low Flow Alarm**: Gradually throttle the manual isolation valve on the secondary supply header until the electromagnetic flowmeter registers flow dropping below the low-flow trip threshold. Confirm that the CDU controller sounds the local alarm horn, illuminates the red beacon, transmits an urgent Modbus/BACnet alarm to the central BMS, and trips the load-bank interlock relay.
- **Expansion Tank Low Liquid Level**: Manually depress the test lever on the expansion tank magnetic float switch. Verify that the CDU alerts the operator, locks out the electric heaters, and commands the automatic makeup water pump to start.
- **Secondary Loop Liquid Leak Detection**: Apply 5 mL of demineralized water across the external leak detection sensing rope positioned beneath the CDU piping connections and the manifold tray. Verify that the leak detection controller triggers within < 2.0 seconds, displays the exact leak distance location, and sends a critical latching alarm to the supervisory BMS.

```
+----------------------------------------------------------------------------------------------------+
| THREE POSSIBLE AUDIT VERDICTS FOR AN ALARM |
+-------------------+--------------------------------------------------------------------------------+
| 1. PASS | Alarm physically injected at sensor; local annunciator active; BMS logged |
| | event with correct timestamp and description; interlock executed cleanly. |
+-------------------+--------------------------------------------------------------------------------+
| 2. FAIL | Alarm injected but sensor failed to detect; delay exceeded tolerance; |
| | interlock relay failed to drop; logged immediately on Master Punch List. |
+-------------------+--------------------------------------------------------------------------------+
| 3. NOT | Equipment lacks the physical sensor, wiring, or software register to raise |
| DEMONSTRATED | this alarm. Explicitly logged as "NOT DEMONSTRATED" on Sheet 2. Never "PASS". |
+-------------------+--------------------------------------------------------------------------------+
```

If a specific alarm cannot be demonstrated because the hardware was omitted during construction, the line on Sheet 2 must be recorded as **NOT DEMONSTRATED**. Logging an untested alarm as "PASS" because "the vendor promised the logic works" is a serious professional breach.

## The Level 4 Prerequisite Gate

Level 4 functional performance testing concludes when all single-system scripts are fully executed and signed. Any failed alarm injection, uncalibrated sensor, or hunting control valve must be formally resolved and re-tested before the facility advances to multi-system thermal testing.

## Decisions to record before test start

- CDU pump soft-start and VFD frequency tracking logs.
- The witnessed N+1 secondary pump auto-changeover transient records (switchover delay ≤ 1.5 s).
- The point-to-point telemetry calibration log across all critical monitoring points.
- The physical alarm injection log, noting all Pass, Fail, and Not Demonstrated items.
- Confirmation that all Level 4 prerequisites are signed off prior to opening Level 5.

---

# 9. The heat window

The thermal heat window is the phase most heavily photographed by stakeholders. It is not the entire project; it is the culmination earned through the disciplined execution of the preceding chapters.

In the global commissioning framework, this is **Level 5 Integrated System Testing (IST)**. Your responsibility during this window is to execute the approved dynamic test scripts in strict sequence, maintain disciplined dwell durations, log high-precision telemetry, and enforce stop criteria immediately when a threshold is breached. It is not an opportunity to improvise new test procedures on the fly.

![Cold vs Hot Pump Curves](../figures/fig-03-pump-curves-cold-vs-hot.png)

## Script 07: The Cold No-Heat Baseline Pump Curve

Before introducing thermal energy, you must execute Script 07 to establish the baseline hydraulic resistance of the secondary loop.

### Why Baseline Before Heat?
The secondary heat transfer fluid—typically 25% Propylene Glycol (PG25) or treated demineralized water—exhibits a significant viscosity shift across its operating temperature range:
- At 20.0°C, the kinematic viscosity of PG25 is $\nu ≈ 2.45 mm²/s$ (μ ≈ 2.50 cP).
- At 50.0°C, its kinematic viscosity drops by more than 50% to $\nu ≈ 1.15 mm²/s$ (μ ≈ 1.10 cP).

This viscosity drop reduces pipe wall shear stress and turbulent frictional resistance. For an identical volumetric flow rate, the pressure drop across secondary manifolds and quick-disconnect fittings decreases significantly at 50°C compared to 20°C.

If you fail to baseline the hydraulic resistance cold, you cannot decouple piping frictional resistance from thermal fluid thinning. If a flow anomaly occurs later under full heat, an auditor cannot determine whether it stems from pump impeller wear, piping blockage, or fluid thinning.

### Execution Protocol for Sheet 6
1. **Lock Out VFD Modulation**: Lock the CDU secondary pump in manual frequency override at 50.0 Hz (or 60.0 Hz nominal design). Automatic differential pressure tracking must be verified as disabled.
2. **Four-Point Throttling Profile**: Gradually throttle the main secondary balancing valve to establish four distinct hydraulic operating points:
 - Point 1: 100% Wide Open (Maximum Flow)
 - Point 2: 80% Equivalent Flow Setpoint
 - Point 3: 60% Equivalent Flow Setpoint
 - Point 4: 40% Equivalent Flow Setpoint
3. **Log Head vs. Flow**: At each point, record volumetric flow Q using the ultrasonic meter, and differential pressure ΔP across the pump and the secondary manifold.
4. **Acceptance Standard**: The measured cold curve must match the manufacturer's certified pump curve within ± 5.0%. Fluid temperature must remain stable within ± 0.5 K throughout the run.

![Integrated Thermal Ladder and Dwell](../figures/fig-05-thermal-ladder-and-dwell.png)

## Script 08: The Multi-Tier Thermal Heat Ladder

Once the cold hydraulic baseline is signed off, thermal loading commences under Script 08. The thermal ladder is a progressive sequence designed to verify that the facility power distribution, CDU heat exchangers, primary water loop, and whitespace air management stabilize at each load increment.

```
+----------------------------------------------------------------------------------------------------+
| THERMAL LADDER STAGE PARAMETERS |
+-------+------------+------------+--------------------+----------------------+----------------------+
| STAGE | THERMAL LOAD| DESIGN kW | MINIMUM DWELL TIME | STABILIZATION GOAL | SHEET REFERENCED |
+-------+------------+------------+--------------------+----------------------+----------------------+
| 1 | 25% Step | 300 kW | 45 minutes | Initial TCV tracking | Sheet 3 (Copy 1) |
| 2 | 50% Step | 600 kW | 45 minutes | Partial-load balance | Sheet 3 (Copy 2) |
| 3 | 75% Step | 900 kW | 45 minutes | Hydraulic shift audit| Sheet 3 (Copy 3) |
| 4 | 100% Step | 1200 kW | 4.0 hours soak | Full-load equilibrium| Sheet 3 (Copy 4) |
| 5 | 110% Step | 1320 kW | 60 minutes | Overload stress test | Sheet 3 (Copy 5) |
+-------+------------+------------+--------------------+----------------------+----------------------+
```

### The Thermal Equilibrium Dwell Criteria
Never advance to the next load step based solely on elapsed time. A load stage is deemed complete only when the system achieves verified **thermal equilibrium**:

$$\left| \frac{dT_{\text{supply}}}{dt} \right| \le 0.20\,\text{K} \text{ over a continuous 10-minute window}$$

If secondary supply temperature is still rising or oscillating due to control valve hunting, the dwell must be extended. Advancing to a higher thermal rung with an unstable control loop compounds thermal instability and risks tripping high-temperature safety limits.

### Enthalpy Heat Balance Reconciliation
At each thermal step, reconcile the active electrical energy consumed against the thermal heat absorbed by the secondary fluid:

$$Q_{\text{liquid}} = \dot{m} \cdot c_p(T_{\text{bulk}}) \cdot (T_{\text{return}} - T_{\text{supply}})$$

Where:
- ṁ = ρ · Q is the mass flow rate (kg/s).
- c_p is the specific heat capacity of PG25 evaluated at bulk fluid temperature (kJ/kg·K).
- P_elec is active 3-phase power measured by the Class 0.2 reference meter (kW).

**Acceptance Standard**: The heat balance closure ratio $\eta = \frac{Q_{\text{liquid}}}{P_{\text{elec}}}$ must maintain:

$$97.0\% \le \eta \le 101.5\%$$

A closure ratio below 97.0% indicates either significant measurement error (such as inaccurate fluid density, incorrect glycol concentration, or untuned flowmeters) or excessive convective heat loss into the whitespace air. A closure ratio exceeding 101.5% is thermodynamically impossible and signals a calibration error.

### Infrared (IR) Thermography Inspection
At 30 minutes into the 100% full-load dwell, conduct an infrared thermographic survey of all electrical distribution equipment:
- Scan all upstream PDU breaker lugs, busway tap box connections, contactor terminals, and load-bank power receptacles.
- **Acceptance Standard**: No electrical terminal may exceed **75.0°C** absolute temperature, and phase-to-phase temperature unbalance across identical terminations must not exceed **5.0 K**. Any loose terminal generating a thermal hot spot is logged on Sheet 3 as an electrical defect.

### Script 08 Overload and Transient Steps
- **110% Overload Margin Test**: Operates the system at 1320 kW for 60 minutes to demonstrate that facility breakers, busbars, and primary cooling capacity maintain safe operational margins above rated capacity.
- **Step-Change Thermal Shock Test**: Initiates an abrupt load shed from $100% \to 30%$ in a single step, holds for 30 minutes, and then steps abruptly back from $30% \to 100%$. This validates that the CDU primary modulating valve (TCV-101) can follow rapid compute workload swings without hunting or causing secondary supply temperature overshoot (ΔT_overshoot ≤ 1.5 K).

## Multi-Rack Secondary Flow Uniformity

During the 100% full-load dwell, measure the flow rate through each individual load bank along the manifold row. As demonstrated in Figure 04, direct-return piping systems tend to starve the furthest rack, whereas reverse-return (Tichelmann) loops maintain uniform pressure drops.

**Acceptance Standard**:
1. Individual load-bank flow deviation from average must not exceed **± 7.5%**.
2. The row-wide Coefficient of Variation ($CV = \frac{\sigma}{\mu} \cdot 100\%$) across all ten load banks must satisfy:

$$CV \le 5.0\%$$

## Dew Point Margin Enforcement

Throughout all thermal testing, monitor ambient data hall relative humidity and dry-bulb temperature. Calculate the real-time air dew point T_dew.

**Acceptance Standard**: The secondary supply temperature T_supply must continuously exceed the room dew point by at least **2.0 K**:

$$T_{\text{supply}} - T_{\text{dew}} \ge 2.0\,\text{K}$$

If secondary supply temperature drops toward the dew point, the CDU mixing valve logic is defective, creating an immediate condensation hazard across uninsulated manifold piping.

## Decisions to record before test start

- The witnessed cold no-heat baseline pump curve filed on Sheet 6.
- The completed multi-tier thermal ladder logs (Sheets 3-1 through 3-5).
- The calculated enthalpy heat balance closure ratio at each step (≥ 97.0%).
- The infrared thermography survey log, recording peak termination temperatures.
- The multi-rack flow uniformity calculation (CV ≤ 5.0%).
- Continuous verification that secondary coolant temperature stayed ≥ 2.0 K above hall dew point.

---

# 10. Stops, and the order out

An emergency stop in a data hall is not a suggestion in an emergency response manual. It is a physical safety circuit wired to de-energize equipment rapidly and safely.

The first book established that the load bank’s internal safety stop operates autonomously and survives the loss of supervisory networks. This book governs who is authorized to activate that stop, and who is permitted to override it.

The operational rule is absolute: **Nobody may override an emergency stop once called.** If a technician, apprentice, or observer calls a stop due to a suspected leak, an electrical anomaly, or personal safety concern, testing terminates instantly. A Test Lead who responds, "Hold on, let me observe the thermal curve for thirty seconds," has committed a grave safety violation. From that second forward, the session ceases to be an engineering test; it becomes a formal incident investigation.

![Dynamic Failure Mode Oscillograms](../figures/fig-06-transient-failure-scenarios.png)

## Script 09: Dynamic Transient Failure Verification

Integrated testing under Script 09 validates that the data hall cooling system can survive catastrophic facility disruptions without compromising compute hardware. These tests simulate real-world failure modes and log the resulting transient recovery curves on Sheet 4:

### 1. Secondary Pump Trip and Auto-Changeover
With the system operating at 100% full thermal load (1.2 MW), physically trip the operating secondary pump (Pump P-1A):
- **Acceptance Criteria**: The standby pump (Pump P-1B) must detect the loss of differential pressure, start automatically, and restore design loop flow within ≤ 1.5 seconds.
- Peak water hammer pressure surge on check valve closure must not exceed ± 50 kPa.
- Secondary loop differential pressure must not drop below the minimum cavitation floor (100 kPa).

### 2. 2N Electrical Feeder A Loss / ATS Transfer
With the CDU operating under dual-feed 2N power distribution, trip the primary Feeder A circuit breaker:
- **Acceptance Criteria**: The Static Transfer Switch (STS) or Automatic Transfer Switch (ATS) must transfer to Feeder B within ≤ 16 milliseconds (less than one AC cycle).
- The CDU’s 24V DC control bus must maintain constant voltage without dipping below the PLC's dropout threshold.
- The CDU controller must **not reboot**. A controller reboot during an electrical bus transfer is an immediate failure of the Level 5 test.
- The secondary pump VFDs must either ride through the bus transfer seamlessly or recover full operating frequency within < 3.0 seconds.

### 3. Primary Chilled Water Supply Interruption (FWS Loss)
With the secondary loop operating at 100% thermal load, simulate a total loss of facility primary cooling water by rapidly closing the primary supply isolation valve:
- This test measures the **hydraulic thermal inertia** of the secondary circuit.
- As primary heat extraction drops to zero, the thermal energy injected by the load banks is absorbed entirely by the sensible heat capacity of the secondary fluid mass:

$$\frac{dT_{\text{supply}}}{dt} = \frac{P_{\text{load}}}{M_{\text{fluid}} \cdot c_p}$$

- **Acceptance Criteria**:
 - The time required for secondary supply temperature to climb from nominal 40.0°C to the High Temperature Alarm threshold of 45.0°C must be at least **40 seconds** (t_buffer ≥ 40 s).
 - Upon reaching 45.0°C, the CDU must automatically issue a High-Temp Warning and initiate a staged load shed.
 - If temperature reaches the Emergency Critical Limit of **50.0°C**, the emergency interlock circuit must trip all load-bank power contactors instantly, halting heat input before boiling or mechanical seal failure occurs.

### 4. BMS Communication Severance
With the loop running under full thermal load, physically disconnect the Modbus-TCP and BACnet network cables linking the CDU PLC to the central facility BMS:
- **Acceptance Criteria**: The CDU local controller must continue operating autonomously without disruption. Secondary pump speeds and modulating valve positions must remain stable under local PID setpoint tracking. The CDU must never hunt, oscillate, or fail open due to a lost external supervisory connection.

## The Controlled Order Out (Sheet 5)

Demobilizing from a multi-megawatt thermal test requires the same operational discipline as initiating it. The de-energization and shutdown sequence must be executed in a strict, non-reversible order.

```
+----------------------------------------------------------------------------------------------------+
| MANDATORY SHUTDOWN EXECUTION SEQUENCE |
+----+-----------------------------+-----------------------------------------------------------------+
|STEP| ACTION COMMAND | ENGINEERING SAFETY RATIONALE |
+----+-----------------------------+-----------------------------------------------------------------+
| 01 | SHED THERMAL LOAD TO 0 kW | Cut all heater contactors/SCRs. Never interrupt fluid flow |
| | | while 1.2 MW of electrical heat is active! |
+----+-----------------------------+-----------------------------------------------------------------+
| 02 | OPEN LOAD-BANK BREAKERS | Lock out and tag out (LOTO) all primary electrical feeds. |
| | | Prove circuits dead with calibrated voltage detector. |
+----+-----------------------------+-----------------------------------------------------------------+
| 03 | 10-MINUTE FLUID COOLDOWN | Maintain secondary pump circulation for 10 minutes to remove |
| | | residual core heat from elements and prevent localized boiling. |
+----+-----------------------------+-----------------------------------------------------------------+
| 04 | STOP CDU SECONDARY PUMPS | Power down pumps only after secondary fluid temperature drops |
| | | safely below 30.0°C. Confirm differential pressure is 0 kPa. |
+----+-----------------------------+-----------------------------------------------------------------+
| 05 | ISOLATE & DISCONNECT HOSES | Close manifold isolation valves, relieve residual static head, |
| | | and disconnect quick-disconnect couplings into catch buckets. |
+----+-----------------------------+-----------------------------------------------------------------+
```

> **CRITICAL REVERSE-SEQUENCE WARNING**: Never reverse Steps 1 and 4! Stopping fluid circulation while megawatts of electrical heat are engaged will cause the stagnant fluid inside the heating channels to flash into steam within seconds. The resulting rapid vapor expansion creates an explosive pressure surge that will blow out hose crimps, destroy sensor diaphragms, and present a catastrophic scalding hazard to personnel in the aisle. Sheet 5 requires every step to be ticked in strict chronological order; a tick out of sequence voids the sheet.

## Data Security and Immediate Dual Backup

Before a single cable or instrument is packed into a shipping crate, all test data must be securely backed up:
- Export all raw high-frequency CSV logs from the load banks, power quality analyzers, and ultrasonic flowmeters.
- Export all 1-second trend logs from the CDU local PLC and the central facility BMS.
- Archive all high-resolution thermal imaging captures and digital photos of the physical master sheets.

Create two independent backups on physically separate storage media (e.g., one on a secure on-site workstation, and a second on an encrypted external drive). A storage drive packed into a shipping crate is not an accessible backup. If that crate is delayed or lost in transit, the commissioning campaign cannot be certified, and the entire multi-week test must be repeated.

## Demobilization and Site Restoration

Demobilization concludes with an inventory audit:
- Count every quick-disconnect coupling, flexible hose, adapter, and blanking cap against the uncrating inventory logged on Sheet 1.
- Install pressure-rated protective dust caps on all manifold supply and return ports.
- Inspect the data hall floor tiles, cable trays, and walls for any transport scuffs, fluid droplets, or residual debris.
- Restore all permanent facility valves, electrical breakers, and BMS control loops to their baseline operational configurations.

The Daily Shift Note for the final day states that testing is concluded, documents the physical location of the data archives, and summarizes open punch list items. It does not declare that the facility "passed." Final certification occurs only after the formal commissioning report is audited and approved.

## Decisions to record before test start

- The witnessed emergency stop test, confirming that physical stop circuits cut heat instantly.
- The dynamic transient test logs recorded on Sheet 4 (pump trip, 2N power loss, FWS cut, BMS cut).
- The signed shutdown sequence log on Sheet 5, executed in strict chronological order.
- The physical storage locations and cryptographic checksums of the dual data backups.
- The completed demobilization inventory, confirming zero lost fittings or temporary modifications.

---

# 11. The punch list

An installation defect or performance failure that is not logged in the official Commissioning Issues Log does not legally exist. While this omission may be convenient for a contractor rushing to demobilize, it presents an unacceptable operational hazard to the facility operations team who must operate the hall once live IT loads arrive.

The master punch list is established during the Commissioning Kickoff Meeting, not after the first secondary coolant leak is discovered. Every logged entry must feature an unambiguous description that an external auditor can comprehend: the specific equipment tag, governing P&ID reference, failed script step number, failure mode, assigned contractor, required remediation, and the specific re-test criteria required for closeout. A vague log entry stating "CDU issue" is completely unacceptable.

![Commissioning Punch List Governance Matrix](../figures/fig-07-punchlist-governance-matrix.png)

## The Three Defect Severity Tiers

Every finding logged in the Issues Log must be classified into one of three standardized severity tiers:

```
+----------------------------------------------------------------------------------------------------+
| DEFECT SEVERITY CLASSIFICATION |
+------------+-------------------------------+-------------------------------------------------------+
| TIER | DEFINITION & EXAMPLES | COMMISSIONING STAGE INTERLOCK IMPACT |
+------------+-------------------------------+-------------------------------------------------------+
| CATEGORY 1 | Critical Safety / Blocker: | ABSOLUTE HARD STOP. Prohibits progression to the next |
| | Active leak > 0 drops/min; | commissioning level. Level 5 thermal energization is |
| | phase reversal; failed E-Stop;| legally prohibited while any Cat 1 item remains open. |
| | pump swap timeout > 1.5 s; | |
| | insulation < 100 MOhm. | |
+------------+-------------------------------+-------------------------------------------------------+
| CATEGORY 2 | Major Operability Deviation: | CONDITIONAL PROGRESSION. Progression permitted only |
| | Enthalpy closure < 97.0%; | if Owner PE signs an explicit deviation waiver with |
| | rack flow variation CV > 5.0%;| operational mitigations. 14-calendar-day resolution. |
| | sensor drift > 0.5 K; | Mandatory re-test required. |
| | control valve hunting. | |
+------------+-------------------------------+-------------------------------------------------------+
| CATEGORY 3 | Minor Cosmetic / Documentation| NO INTERLOCK. Does not impede dynamic testing or |
| | Inverted pipe flow arrow; | milestone certificates. Verified via photographic |
| | cable tray paint scratch; | evidence within 30 days post-turnover. |
| | smudged calibration label. | |
+------------+-------------------------------+-------------------------------------------------------+
```

## The Stage Interlock and the Waiver Protocol

The foundational rule governing data center commissioning is that **no project may advance across a milestone boundary while an open Category 1 defect remains unresolved**.

The punch list is where contractors frequently attempt to negotiate around this rule. A contractor plea stating, "We understand the primary check valve is leaking slightly on reverse flow, but let us proceed with the 100% heat step and we will repair the valve during demobilization," must be rejected. Initiating high-load thermal testing with a compromised check valve risks reverse-flow pump cavitation, severe hydraulic shock, and catastrophic pump motor burn-out.

If the facility owner decides to proceed despite an open Category 2 operability deviation to meet an inflexible business delivery deadline, that decision must be formalized via a signed **Deviation Waiver**. The waiver must articulate:
1. The exact technical deficiency and governing specification clause.
2. The operational risk assessment and potential failure modes.
3. The specific compensatory safety controls deployed during the test window.
4. The contractual commitment and schedule for remediation and witnessed re-testing.

A verbal agreement or casual text message is completely invalid. An unwritten waiver is merely an agreement to be surprised by an operational failure.

## Remediation and Retest Governance

The division of responsibility during punch list resolution must be strictly maintained:
- **The Trade Contractor**: Performs physical repairs under formal facility work permits.
- **The Verification Party**: Audits the repair, inspects physical work, directs the re-test script, and records the new data. The verification team never repairs mechanical or electrical plant, as doing so destroys their independent audit posture.
- **The Facility Owner**: Witnesses the re-test and countersigns the closeout entry.

A punch list line item cannot be closed by a contractor submitting an email stating, "The technician adjusted the valve parameter." Closing a line item requires the exact same level of engineering evidence demanded by the original script: a fully executed, witnessed re-test data sheet demonstrating that the parameter meets specification.

## Retesting Scope and Commercial Boundaries

A witnessed re-test incurs real costs in engineering hours, facility utility power, and temporary equipment rental. The Commissioning Plan must explicitly define upfront whether re-testing is covered within the base project scope or requires a formal change order.

Establishing this commercial boundary early prevents disputes when a complex test must be repeated due to a contractor's defective installation. However, commercial negotiations must never compromise technical standards: an unapproved re-test executed without a formal script revision is not a valid verification; it is merely an unrecorded equipment cycle.

## Post-Demobilization Desktop Defects

Certain defects become apparent only after demobilization, when high-frequency telemetry logs and power meter CSVs are analyzed on an engineering workstation.

If an enthalpy heat balance calculation reveals that closure dropped to 92.0% during the final thermal hour, or if frequency analysis detects low-amplitude VFD hunting, that finding must be formally logged in the master Issues Log with its post-processing discovery date.

The Test Lead must carefully distinguish between:
- **A Data Acquisition Defect**: Such as a desynchronized NTP clock, corrupted CSV formatting, or an uncalibrated current transducer.
- **A Physical Plant Failure**: Such as a slipping pump belt, scaling on a heat exchanger plate, or a failing thyristor module.

Conflating a data acquisition error with a physical plant defect wastes contractor resources investigating healthy equipment; conversely, mislabeling a physical plant failure as a telemetry glitch allows a defective cooling system to be handed over to live IT operations.

## The Closeout Requirement

When every Category 1 and Category 2 defect logged across the executed commissioning levels is fully resolved and verified through witnessed re-testing, the Commissioning Authority may certify the closeout. An oral agreement during the final closeout meeting that "everything is resolved" carries no legal weight. The completed master Issues Log must be printed, reviewed, and signed in ink by all three parties.

## Decisions to record before test start

- The location, hosting security, and software platform for the master Issues Log.
- Named individuals authorized to log defects, execute repairs, witness re-tests, and close entries.
- The formal Deviation Waiver template, including mandatory risk assessments and mitigation plans.
- The commercial agreement governing re-testing costs and schedule allocations.
- The printed, signed master Issues Log with all items verified as closed prior to Level 6 turnover.

---

# 12. Close-out and turnover

A successful thermal heat test is not a facility turnover. Demobilizing load banks from a data hall merely signifies that dynamic verification has concluded. The formal transition of the facility from construction into live IT operations occurs under **Level 6 Close-Out, Turnover, and Operations Handover**.

A turnover certificate signed while punch list items remain unresolved or before the final commissioning report is audited is legally defective. Level 6 turnover is the formal milestone where the Facility Owner, the General Contractor, and the Commissioning Authority collectively certify that the mechanical, electrical, and control systems satisfy the Owner's Project Requirements and are safe to receive high-density compute infrastructure.

```
+----------------------------------------------------------------------------------------------------+
| LEVEL 6 TURNOVER DOCUMENT ARCHITECTURE |
+----+--------------------------------+--------------------------------------------------------------+
| 01 | EXECUTIVE SUMMARY & VERIFIED | The signed claim sentence, final project verdict, and |
| | CLAIM STATEMENT | summary of operational thermal capacity demonstrated. |
+----+--------------------------------+--------------------------------------------------------------+
| 02 | SCOPE BOUNDARIES & EXCLUSION | Explicit scope letters documenting unexecuted levels, |
| | LETTERS | seasonal deferred testing, and third-party systems out. |
+----+--------------------------------+--------------------------------------------------------------+
| 03 | MASTER MILESTONE CERTIFICATES | Formal signed completion certificates for Levels 2, 3, 4, 5. |
+----+--------------------------------+--------------------------------------------------------------+
| 04 | THE SEVEN SIGNED MASTER SHEETS | Sheets 1 through 7, fully executed, logged in ink, signed. |
+----+--------------------------------+--------------------------------------------------------------+
| 05 | INSTRUMENT CALIBRATION LOG | Traceable ISO 17025 calibration certificates for all tools. |
+----+--------------------------------+--------------------------------------------------------------+
| 06 | TIME-SERIES DATA REPOSITORY | Complete raw CSV logs, BMS trend exports, cryptographic SHA. |
+----+--------------------------------+--------------------------------------------------------------+
| 07 | RESOLVED ISSUES REGISTER | Master Punch List showing 100% Cat 1 & Cat 2 items closed. |
+----+--------------------------------+--------------------------------------------------------------+
| 08 | SYSTEMS MANUAL SUPPLEMENT | As-tested pump curves, operating bands, fail-safe setpoints. |
+----+--------------------------------+--------------------------------------------------------------+
| 09 | OPERATIONS TRAINING RECORDS | Witnessed sign-off of facility staff SOP walkthrough. |
+----+--------------------------------+--------------------------------------------------------------+
```

## Structure of the Final Commissioning Report

The Final Commissioning Report is the permanent engineering baseline of the liquid cooling infrastructure. Decades later, when the facility undergoes retrofits or failure investigations, engineering teams will refer to this report to verify initial operating parameters.

The report must be compiled with nine standardized sections:

### 1. Executive Summary and Certified Claim
Opens with the exact, unedited claim sentence formulated in Chapter 1. It provides an unambiguous operational summary: the total thermal capacity verified (e.g., 1.2 MW continuous), the primary cooling supply conditions, secondary flow balance metrics, and the formal certification that all tested systems operated within specification.

### 2. Scope Boundaries and Formal Exclusion Letters
A rigorous definition of boundaries. If Level 0 design review or Level 1 factory testing were excluded from the contract, the formal Scope Exclusion Letters signed by the owner must be embedded here. If seasonal testing (such as maximum summer ambient chiller stress testing) must be deferred to a later date, the Deferred Testing Protocol and scheduled execution date are formally documented.

### 3. Master Milestone Completion Certificates
Formal certificate pages for Level 2 (Receipt QA), Level 3 (PFC and Start-Up), Level 4 (Single-System FPT), and Level 5 (Integrated System IST). Each certificate must bear the ink signatures of the Commissioning Lead, Electrical PE, Mechanical PE, Contractor Executive, and Owner’s Authorized Representative.

### 4. The Seven Master Field Sheets
The completed, physical field record sheets (Sheets 1 through 7 from Chapter 16), scanned in full color showing all ink entries, witness initials, step timestamps, and field notes.

### 5. Calibrated Instrument Register
A complete traceability log listing every multimeter, power quality analyzer, ultrasonic flowmeter, digital thermometer, differential pressure transmitter, and thermal imaging camera deployed during testing. Embed copies of their ISO/IEC 17025 calibration certificates.

### 6. Raw Time-Series Data Repository
A structured archive containing the 1-second raw telemetry exports from the load banks, power meters, and BMS trend logs. To prevent post-test manipulation, generate a cryptographic hash (SHA-256 checksum) for every raw data file and record the hash table in the report appendix.

### 7. Resolved Master Issues Register
The final, printed copy of the Commissioning Issues Log. Every Category 1 and Category 2 defect must show its complete resolution history: initial finding, contractor remediation, witnessed re-test data sheet reference, and closeout signature. Any remaining open Category 3 cosmetic items must be bound by an approved 30-day closeout plan.

### 8. Systems Manual Operational Supplement
The operational bridge between commissioning data and daily facility operations. This section extracts critical baseline characteristics from the test data:
- The verified cold no-heat pump curve versus hot operating points (Sheet 6).
- Calibrated PID loop parameters for the primary modulating valve (TCV-101).
- The exact secondary fluid inventory (V_total) and glycol concentration (Refractometer verified 25.0% ± 0.5%).
- The emergency interlock logic matrix, defining hardware trip thresholds.

### 9. Operations Team Training Sign-Off
Documentation of formal operational handover training conducted with site facility engineers. Training must include physical walkthroughs of the emergency stop mechanisms, manual bypass valve operations, secondary fluid makeup procedures, and alarm acknowledgement workflows.

## The Final Page Boundary Statement

The final page of the report must protect the testing party and the owner by clearly stating what the verification did not cover:

```
+----------------------------------------------------------------------------------------------------+
| FORMAL BOUNDARY STATEMENT |
| |
| "This verification campaign certifies the performance of the liquid cooling infrastructure under |
| simulated electrical and thermal load conditions as explicitly documented herein. It does not |
| certify the operational reliability, compute workload throughput, or warranty compliance of |
| production IT hardware. Systems marked as excluded or not demonstrated remain outside the scope |
| of this certification. All verified capacities are contingent upon the facility operating within |
| the environmental, electrical, and hydraulic boundaries established in this report." |
+----------------------------------------------------------------------------------------------------+
```

## Decisions to record before test start

- The final report template and documentation archive format.
- Confirmation that 100% of Category 1 and Category 2 punch list items are closed.
- The SHA-256 cryptographic checksum register for all raw telemetry files.
- The formal Level 6 Turnover Certificate, signed by all primary stakeholders.
- The signed Facility Operations Training Register and Systems Manual supplement.

---

# 13. What this project does not own

This book will inevitably be misused by individuals who attempt to expand it into an exhaustive encyclopedia of all liquid cooling engineering. Establish clear professional boundaries here.

A commissioning verification project maintains legal and engineering authority only when its boundaries are sharply defined. Expanding a verification scope into adjacent engineering disciplines on the fly produces flawed testing, diluted accountability, and severe contractual disputes.

```
+----------------------------------------------------------------------------------------------------+
| EXPLICIT NEGATIVE SCOPE BOUNDARIES |
+------------------------------------+---------------------------------------------------------------+
| WHAT THIS PROJECT VERIFIES | WHAT THIS PROJECT CANNOT AND DOES NOT OWN |
+------------------------------------+---------------------------------------------------------------+
| • Simulated thermal heat transfer | • Book 01 Scope: Load-bank design, R&D, and manufacturing QA |
| • Secondary pump curve baseline | • Book 02 Scope: Telemetry math, anomaly detection algorithms|
| • 2N electrical feed transfer ride | • Facility Design: Architectural, structural, MEP engineering|
| • Multi-rack manifold flow balance | • Silicon Performance: GPU compute, memory bus, AI workload |
| • CDU local autonomous safety loops| • Metallurgy & Chemistry: Water corrosion, biocide (Book 08) |
| • Physical hardware alarm trips | • Next Data Hall: Extrapolated universal building code rules |
+------------------------------------+---------------------------------------------------------------+
```

## The Dedicated Boundaries

### 1. It Does Not Own the Load Bank Design (Book 01)
This verification assumes that the liquid load bank deployed on the floor has already undergone full factory acceptance testing, chassis isolation verification, and flow bench characterization under the disciplines of Book 01. If the load bank arrives on site as an unverified prototype with leaking internal braze joints or unstable SCR controllers, the Commissioning Lead must refuse to connect it. A site commissioning campaign must never be converted into an ad-hoc equipment R&D laboratory.

### 2. It Does Not Own the Telemetry Interpretation (Book 02)
This verification logs raw physical measurements and witnessed timestamps. The algorithmic reconciliation of the flash report, changepoint analysis (FLOC/Focus), and the statistical validation of data integrity belong to the disciplines of Book 02. A stable-looking thermal curve on a BMS monitor is not an accepted pass until the raw data files pass rigorous variance and quality-bitmask audits. Conversely, the field testing team must not invent alternative, lenient acceptance criteria on site simply because client executives are observing the test.

### 3. It Does Not Own Facility MEP Design
The verification team verifies the physical plant against the approved Basis of Design. If the plant fails to maintain secondary supply temperature because the central chiller plant was undersized, or because the secondary header diameter causes excessive frictional head loss, that failure is an installation deviation or design deficiency. The verification team documents the physical performance in ink; they do not redesign the facility piping on site or issue comforting statements that the installation is "close enough."

### 4. It Does Not Own Fluid Chemistry and Metallurgy (Book 08)
The verification team audits basic fluid parameters (refractometer glycol concentration ± 0.5%, turbidity, and initial pH) as prerequisites for testing. They do not certify long-term metallurgical compatibility, galvanic corrosion rates between copper cold plates and aluminum manifolds, or biocide degradation curves. Those long-term chemical verifications belong to the disciplines of Book 08.

### 5. It Does Not Own the Silicon Compute Infrastructure
A liquid load bank simulates the bulk electrical dissipation and hydraulic pressure drop of an accelerated compute rack (such as an NVL72 footprint). It does not contain silicon microprocessors, optical transceivers, or NVLink network fabrics. A load bank that operates stably under a 120 kW thermal step has proven that the cooling loop can extract 120 kW of heat; it has not proven that a production compute rack will boot, train a large neural network, or avoid silicon thermal throttling.

### 6. It Does Not Own the Next Data Hall
The procedural workflow established in this book—the sequence of twelve products, the six-level hierarchy, the five functional roles, and the seven master sheets—can be applied universally across mission-critical facilities. However, the specific numerical parameters (the exact kW steps, dwell durations, flow tolerances, and maximum operating temperatures) are unique to the specific contract in force. Copying numerical values from this data hall into a different facility without independent engineering analysis turns this field guide into an unverified copy-paste exercise.

## Decisions to record before test start

- The load-bank factory acceptance certificate reference (Book 01), or formal refusal to connect.
- The formal data audit procedure adopted from Book 02.
- The explicit list of excluded engineering disciplines, documented on the claim sheet and reaffirmed in the final report.

---

# 14. Public sources, and the copyright line

This field guide articulates an operational methodology for executing and auditing liquid cooling verification tests. It does not digest, transcribe, or duplicate proprietary industry codes, standards, vendor confidential engineering designs, or copyrighted contract templates.

An engineering standard that can be purchased from an issuing standards body is not a document that may be reproduced in an external text. Citing a standard by title, year, and specific section number to establish a legal testing tolerance is standard engineering practice; reproducing extensive passages from those standards within an AI-generated manual is improper.

```
+----------------------------------------------------------------------------------------------------+
| NORMATIVE INDUSTRY STANDARDS CITED |
+----------------------+-----------------------------------------------------------------------------+
| ASHRAE GUIDELINE 0 | "The Commissioning Process" (2019 Edition). Foundational principles for |
| | commissioning scope, Owner's Project Requirements (OPR), and BOD auditing. |
+----------------------+-----------------------------------------------------------------------------+
| ASHRAE GUIDELINE 1.1 | "HVAC&R Technical Requirements for The Commissioning Process" (2007/2014). |
| | Methodologies for pre-functional checklists and functional performance. |
+----------------------+-----------------------------------------------------------------------------+
| ACG GUIDELINE | AABC Commissioning Group "Commissioning Guideline for Building Systems". |
| | Independent third-party verification protocols and witness standards. |
+----------------------+-----------------------------------------------------------------------------+
| BSRIA BG 29/2020 | "Pre-Commission Cleaning of Pipework Systems" (6th Edition). Strict criteria|
| | for scouring velocities, chemical flushing, and solid particulate counts. |
+----------------------+-----------------------------------------------------------------------------+
| NFPA 70 / IEC 60364 | National Electrical Code (NEC) and International Electrotechnical |
| | Commission standards for branch circuit protection, grounding, and LOTO. |
+----------------------+-----------------------------------------------------------------------------+
| ISA-5.1 | "Instrumentation Symbols and Identification". Standard P&ID symbology for |
| | process flow diagrams, transmitters (TT, PT, FT), and control valves (TCV). |
+----------------------+-----------------------------------------------------------------------------+
```

## Application of Normative Standards

The twelve engineering products articulated in Chapter 2 represent the structural sequence required by modern commissioning governance. They derive from standard industry methodologies (including ASHRAE Guideline 0 and ACG publications) adapted specifically for mission-critical liquid cooling verification.

The completion certificate hierarchy (Levels 0 through 6) reflects the recognized standard across global data center engineering:
- Level 0: Design & Planning
- Level 1: Factory Acceptance Testing
- Level 2: Component Delivery & Receipt QA
- Level 3: Pre-Functional Checks & Start-Up
- Level 4: Functional Performance Testing
- Level 5: Integrated System Testing
- Level 6: Close-Out & Operations Handover

The local "three-stage" terminology frequently used by contractors on the floor is a regional field shorthand. It does not supersede global commissioning certificate tiers. When adopting either framework, the Commissioning Plan must explicitly define on page one which legal signatures the resulting documentation is authorized to support.

## Electrical and Mechanical Code Compliance

Electrical safety checks—including the 100 MΩ insulation resistance threshold and the 0.1 Ω ground continuity limit—derive from NFPA 70 (NEC Article 250 and Article 645 for Information Technology Equipment) and international standard IEC 60204-1 (Safety of Machinery - Electrical Equipment of Machines). A field test script must never attempt to transcribe extensive electrical code articles into its procedure; it cites the governing article number, and the local Electrical Inspector Having Jurisdiction (AHJ) enforces the binding adoption.

Secondary fluid preparation, hydrostatic pressure holding, and system deaeration follow the principles of BSRIA BG 29/2020 and ASME B31.3 (Process Piping). The scouring flush velocity (≥ 1.5 m/s) and the hydrostatic hold requirement (1.5× MAOP for 2 hours with zero decay) are established mechanical engineering standards for hydronic piping.

## Non-Proprietary Reference Baseline

To provide concrete, meaningful numerical yardsticks without disclosing proprietary manufacturer IP or client-confidential data, this book utilizes a non-proprietary reference architecture:
- **Compute Footprint**: Standard 120 kW virtual compute rack simulating high-density accelerated architectures (such as an NVL72-class rack footprint).
- **Cooling Unit**: 1.2 MW in-row or centralized Coolant Distribution Unit (CDU) utilizing dual N+1 canned centrifugal pumps and a titanium plate heat exchanger.
- **Cooling Chemistry**: 25% Propylene Glycol (PG25) with corrosion inhibitors, operating between 40.0°C supply and 50.0°C return.

Specific manufacturer submittals, proprietary PLC control algorithms, client-confidential network schemas, and proprietary quick-disconnect dimensions belong in the project's secure archives under signed Non-Disclosure Agreements (NDAs). They must never be published in open reference guides.

## Decisions to record before test start

- The complete list of governing codes, standards, and guidelines cited in the Commissioning Plan, with publication years.
- The contractual document number supporting each tolerance value.
- Re-affirmation that proprietary vendor IP and confidential site drawings are preserved within local project files.

---

# 15. Which sheet to hold

Chapter 16 provides the seven master engineering record sheets. Print them on waterproof paper, assemble them in a dedicated field binder, and take them onto the data hall floor.

Do not attempt to summarize these grids into high-level descriptive paragraphs after the test concludes, discarding the raw field data. An auditor inspecting a verification package expects to see the actual ink impressions, timestamped entries, witness initials, and instrument serial numbers recorded while standing in the aisle.

```
+----------------------------------------------------------------------------------------------------+
| THE SEVEN MASTER FIELD SHEETS |
+-------+-------------------------------+-------------+------------------+---------------------------+
| SHEET | TITLE & VERIFICATION SCOPE | CX TIER | RESPONSIBLE LEAD | MANDATORY EXECUTION TIMING|
+-------+-------------------------------+-------------+------------------+---------------------------+
| 01 | Pre-Energization Static QA | Level 2 / 3 | Electrical PE & | Before closing any supply |
| | & Hydraulic Hold Check | | Mechanical PE | breaker or opening fluid. |
+-------+-------------------------------+-------------+------------------+---------------------------+
| 02 | Autonomous CDU Protection | Level 4 FPT | Controls PE & | Before introducing any |
| | & Physical Alarm Injections | | Mechanical PE | thermal heat to the loop. |
+-------+-------------------------------+-------------+------------------+---------------------------+
| 03 | Multi-Stage Thermal Step & | Level 5 IST | Test Lead & | One distinct copy executed|
| | Enthalpy Heat Closure Log | | Test Technician | per thermal step rung. |
+-------+-------------------------------+-------------+------------------+---------------------------+
| 04 | Dynamic Transient Failure & | Level 5 IST | Test Lead & | Executed at 100% full load|
| | Redundancy Ride-Through Log | | Controls PE | during simulated faults. |
+-------+-------------------------------+-------------+------------------+---------------------------+
| 05 | Controlled De-Energization & | Closeout | Test Lead & | Executed in strict order |
| | Demobilization Protocol | Level 6 | Electrical PE | during shift shutdown. |
+-------+-------------------------------+-------------+------------------+---------------------------+
| 06 | Cold No-Heat Baseline Pump | Level 4 / 5 | Mechanical PE & | Executed at 20°C with VFD |
| | & Loop Resistance Curve | | Test Technician | modulation locked off. |
+-------+-------------------------------+-------------+------------------+---------------------------+
| 07 | CDU Autonomous Control Logic | Level 4 / 5 | Controls PE & | Executed across all units |
| | & Supervisory Interface Audit | | Vendor Specialist| with vendor logic attached|
+-------+-------------------------------+-------------+------------------+---------------------------+
```

## Floor Execution Rules

1. **Two People on the Tools**: One engineer operates the calibrated measurement instrument; a second engineer logs the measured value in ink. Never attempt to read a display, remember the number, and write it down five minutes later.
2. **Every Cell Is an Obligation**: A blank cell is an automated stop. If a parameter is not included in the scope of this specific test, mark it **"N/A (Out of Scope per Claim Rev [X])"** and initial the entry. Never leave a cell empty.
3. **Copy Sheet 3 per Thermal Step**: Sheet 3 is not a single form. Print multiple copies. Execute a separate, complete Sheet 3 for each step in the thermal ladder (25%, 50%, 75%, 100%, and 110%). Never combine data from multiple load steps onto a single sheet.
4. **Attach Raw Telemetry Checksums**: Record the file name and SHA-256 checksum of the corresponding high-frequency CSV log directly in the header of each sheet.
5. **No Retroactive Alterations**: If an entry was written incorrectly, draw a single horizontal line through the error, write the correct value alongside, and initial the correction. Never use correction fluid or scribble over a field entry.

## The Physical Binder Assembly

Organize the physical field binder into seven dedicated tabs corresponding to the seven sheets. Precede each tab with the approved test script revision and the instrument calibration certificates required for that phase.

When testing concludes, this physical binder is scanned in full color and forms the permanent core of the Level 6 Final Commissioning Report.

---

# 16. The sheets

Copy these master engineering forms into your project binder. Fill every cell in ink on the data hall floor. One engineer measures with calibrated instruments; a second engineer records the reading. A blank cell is an automated stop. A number copied from memory is a defect.

---

## Sheet 1. Pre-Energization Static QA & Hydraulic Verification (Level 2 / Level 3)

**Project Name**: __________________________ **Data Hall / Room ID**: __________________________ 
**Test Unit (CDU / Row ID)**: ________________ **Date of Verification**: __________________________ 
**Lead Electrical PE**: ____________________ **Lead Mechanical PE**: __________________________ 
**Measurement Tech**: ______________________ **Ink Recording Tech**: __________________________ 

### 1. Physical Uncrating, Structural & Coupling Inspection
- [ ] Load-bank frames inspected for shipping damage, weld cracks, or caster deformation: **PASS / FAIL**
- [ ] Quick-disconnect couplings inspected (Danfoss Hansen FD83 / ISO 16028): **PASS / FAIL**
- [ ] EPDM internal elastomeric seals inspected under magnification (zero cuts, tears, or burrs): **PASS / FAIL**
- [ ] High-pressure secondary flexible hoses inspected (wire-braided, rated ≥ 1.5× MAOP): **PASS / FAIL**
- [ ] Hose routing verified: zero kinks, all bends exceed minimum allowable bend radius: **PASS / FAIL**
- [ ] Seismic anchoring and floor pedestal understructure verified against structural PE drawings: **PASS / FAIL**

### 2. De-Energized Electrical Isolation & Safety Testing (LOTO Enforced)
- **Insulation Resistance Tester Model & Serial Number**: ____________________ **Calibration Expiry**: ____________ 
- **Test Voltage Applied**: 1000V DC for 60 seconds continuous 
 - Phase A to Phase B: __________ MΩ (Limit: ≥ 100.0 MΩ) — **PASS / FAIL** 
 - Phase B to Phase C: __________ MΩ (Limit: ≥ 100.0 MΩ) — **PASS / FAIL** 
 - Phase C to Phase A: __________ MΩ (Limit: ≥ 100.0 MΩ) — **PASS / FAIL** 
 - Phase A to Ground (PE): ______ MΩ (Limit: ≥ 100.0 MΩ) — **PASS / FAIL** 
 - Phase B to Ground (PE): ______ MΩ (Limit: ≥ 100.0 MΩ) — **PASS / FAIL** 
 - Phase C to Ground (PE): ______ MΩ (Limit: ≥ 100.0 MΩ) — **PASS / FAIL** 
- **Ground Bond Continuity**: Chassis to Main Facility Ground Busbar: __________ Ω (Limit: ≤ 0.10 Ω) — **PASS / FAIL** 
- **Phase Sequence & Rotation Indicator**: Tested at supply tap box: **CLOCKWISE (A-B-C) / COUNTER-CLOCKWISE** 
 *(CRITICAL: If phase sequence is not clockwise, do NOT energize. Reverse rotation will destroy canned pump bearings.)*

### 3. Secondary Hydraulic Flush, Hydrostatic Hold & Volume Audit
- [ ] Secondary loop chemical flushing completed per BSRIA BG 29/2020 (≥ 1.5 m/s scouring velocity): **ATTACHED** 
- [ ] Strainers inspected and cleaned; ISO 4406 fluid cleanliness certificate: **ATTACHED** 
- **Hydrostatic Pressure Hold**: 
 - Maximum Allowable Operating Pressure (MAOP): __________ bar 
 - Test Hold Pressure Applied (1.5× MAOP): __________ bar 
 - Start Timestamp: ____________________ End Timestamp: ____________________ (Duration: ≥ 2.0 hours) 
 - Start Pressure: __________ bar End Pressure: __________ bar Pressure Decay (ΔP): __________ bar 
 - Acceptance Standard: ΔP ≤ 0.0 bar (accounting for thermal stabilization). Leak rate: **ZERO DROPS / MIN** 
 - Verification Verdict: **PASS / FAIL** 
- [ ] Vacuum deaeration and thorough air purge completed; sight glasses clear of microbubbles: **PASS / FAIL** 
- **Secondary Fluid Inventory Calculation**: 
 - CDU Internal Volume: __________ L 
 - Manifold Distribution Volume: __________ L 
 - Flexible Hoses Volume: __________ L 
 - Load-Bank Internal Volume: __________ L 
 - **Total Secondary Fluid Inventory (V_total)**: __________ L 
- **Fluid Chemistry Baseline**: Refractometer PG Concentration: __________ % (Target: 25.0% ± 0.5%) 

### 4. Upstream Protective Coordination Audit
- Upstream PDU Breaker Frame Rating: __________ A Trip Plug Rating: __________ A 
- Electronic LSIG Settings: Long Time: ______ s Short Time Pickup: ______ x Instantaneous: ______ x 
- [ ] Protective coordination curves verified against load-bank inrush characteristics: **PASS / FAIL** 

**SHEET 1 GATE VERDICT**: [ ] **STAGE PASSED — CLEARED FOR LEVEL 4** [ ] **STAGE BLOCKED (OPEN DEFECT)** 
**Lead Electrical PE Signature**: ________________________ **Date**: __________________ 
**Lead Mechanical PE Signature**: ________________________ **Date**: __________________ 

---

## Sheet 2. Autonomous CDU Protection & Physical Alarm Injections (Level 4 FPT)

**Project Name**: __________________________ **Data Hall / Room ID**: __________________________ 
**CDU Asset Tag**: __________________________ **Firmware / Software Rev**: ______________________ 
**Lead Controls PE**: ______________________ **Mechanical PE**: ______________________________ 
**Facility Operations Witness**: ____________ **Test Date & Shift**: ____________________________ 

*Every alarm row must be physically injected at the sensor or field wiring. Software setpoint simulation is prohibited.*

| ALARM DESCRIPTION | PHYSICAL INJECTION METHOD | LOCAL SOUNDER / BEACON | CDU HMI ANNUNCIATOR | SUPERVISORY BMS TIMESTAMP | INTERLOCK TRIP ACTION | AUDIT VERDICT (PASS / FAIL / NOT DEMONSTRATED) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Secondary Low Flow** | Throttle supply balancing valve until flow drops below low setpoint (<90 m³/h) | [ ] Aud [ ] Vis | [ ] Alert logged | [ ] Logged: ________ | Trips load-bank interlock relay | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Secondary High Supply T** | Apply calibrated thermal bath or resistor bridge to PT100 immersion probe (>45.0°C) | [ ] Aud [ ] Vis | [ ] Alert logged | [ ] Logged: ________ | Triggers load-bank staged heat shed | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Secondary Low Pressure** | Partially vent pressure transmitter isolation block until P < 100 kPa | [ ] Aud [ ] Vis | [ ] Alert logged | [ ] Logged: ________ | Locks out electric heaters | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Expansion Tank Low Level**| Manually actuate magnetic float test stem to minimum low-level cutoff | [ ] Aud [ ] Vis | [ ] Alert logged | [ ] Logged: ________ | Commands auto-makeup pump START | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Primary Low Water Flow** | Throttle primary FWS isolation valve until flow < 50 m³/h | [ ] Aud [ ] Vis | [ ] Alert logged | [ ] Logged: ________ | Modulates TCV to 100% full open | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Primary High Supply Temp**| Elevate primary water temp or inject sensor offset (> 35.0°C) | [ ] Aud [ ] Vis | [ ] Alert logged | [ ] Logged: ________ | Warning logged; flags facility PUE | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Lead Pump VFD Inverter Trip**| Disconnect digital fault input or open VFD control power breaker | [ ] Aud [ ] Vis | [ ] Alert logged | [ ] Logged: ________ | Starts Standby Pump within ≤ 1.5 s | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Internal Catch-Pan Leak** | Apply 5 mL demineralized water across optical / float catch-pan sensor | [ ] Aud [ ] Vis | [ ] Alert logged | [ ] Logged: ________ | Isolates CDU; trips load-bank contactor | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **External Sensing Rope Leak**| Wet external perimeter sensing rope along secondary manifold tray | [ ] Aud [ ] Vis | [ ] Alert logged | [ ] Logged: ________ | Pinpoints location; trips alert | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Emergency Stop Pushbutton**| Depress physical red mushroom E-Stop button on CDU front door | [ ] Aud [ ] Vis | [ ] Alert logged | [ ] Logged: ________ | Drops 24V bus; cuts pump & heater relays | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |

### Hardware Interlock and Standby Failover Times
- Standby Pump Auto-Start Measured Delay: __________ ms (Limit: ≤ 500 ms) 
- Secondary Flow Restoration Measured Time: ______ s (Limit: ≤ 1.5 s) 
- Minimum Secondary Loop Pressure During Failover: ______ kPa (Limit: ≥ 100 kPa) 
- Physical E-Stop Power Cut Measured Delay: ______ ms (Limit: ≤ 50 ms) 

**SHEET 2 GATE VERDICT**: [ ] **LEVEL 4 PASSED — CLEARED FOR LEVEL 5** [ ] **LEVEL 4 BLOCKED (OPEN DEFECT)** 
**Lead Controls PE Signature**: ________________________ **Date**: __________________ 
**Facility Operations Witness**: ________________________ **Date**: __________________ 

---

## Sheet 3. Multi-Stage Thermal Step & Enthalpy Heat Closure Log (Level 5 IST)

*Execute one dedicated copy of Sheet 3 for each thermal step rung: 25%, 50%, 75%, 100%, and 110%.*

**Step Number**: Step _____ of 5 **Target Thermal Load**: __________ kW (______ % of Rated Capacity) 
**Step Start Timestamp**: ____________________ **Equilibrium Timestamp**: ____________________ 
**Total Dwell Duration**: __________ minutes (Minimum requirement: ≥ 45 min; 100% soak ≥ 4.0 h) 
**High-Frequency CSV File Name**: __________________________ **SHA-256 Checksum**: ________________________ 

### 1. Thermodynamic & Enthalpy Heat Balance Telemetry

| PARAMETER | SCRIPT SPEC LIMIT | MEASURED VALUE (FIELD REF) | BMS / TELEMETRY LOG | AUDIT DELTA |
| :--- | :--- | :--- | :--- | :--- |
| **Active 3-Phase Power (P_elec)** | Target: _____ kW ± 1.5% | __________ kW (Class 0.2) | __________ kW | ______ % |
| **Primary Supply Temp ($T_pri\_sup$)** | Nominal: 30.0°C ± 1.0 K | __________ °C | __________ °C | ______ K |
| **Primary Return Temp ($T_pri\_ret$)** | Expected: ≤ 36.5°C | __________ °C | __________ °C | ______ K |
| **Primary Volumetric Flow (Q_pri)** | Maximum: ≤ 180 m³/h | __________ m³/h | __________ m³/h | ______ % |
| **Primary Differential Pressure (ΔP_pri)**| Design: ≤ 120 kPa across PHE | __________ kPa | __________ kPa | ______ kPa |
| **Secondary Supply Temp ($T_sec\_sup$)** | Setpoint: 40.0°C ± 0.5 K | __________ °C (PT100 Ref) | __________ °C | ______ K |
| **Secondary Return Temp ($T_sec\_ret$)** | Expected: ≤ 50.5°C | __________ °C (PT100 Ref) | __________ °C | ______ K |
| **Secondary Fluid Delta-T (ΔT_sec)** | Design: 10.0 K ± 0.5 K | __________ K | __________ K | ______ K |
| **Secondary Volumetric Flow (Q_sec)** | Design: 115.0 m³/h ± 3.0% | __________ m³/h (Ultrasonic) | __________ m³/h | ______ % |
| **Secondary Pump VFD Frequency** | Operating range: 30.0 to 50.0 Hz | __________ Hz | __________ Hz | ______ Hz |
| **Secondary Pump Differential P (ΔP_pump)**| Design: 220 kPa ± 10 kPa | __________ kPa | __________ kPa | ______ kPa |
| **Primary TCV Valve Position** | Modulating tracking (0-100%) | __________ % open | __________ % open | ______ % |

### 2. Thermal Equilibrium and Enthalpy Closure Calculations
- **Thermal Stabilization Rate**: $\left|\frac{dT_{\text{supply}}}{dt}\right| = \text{__________ K / 10 min}$ (Acceptance Limit: ≤ 0.20 K / 10 min) — **PASS / FAIL** 
- **Secondary Liquid Heat Extraction**: 
 $$Q_{\text{liquid}} = \dot{m} \cdot c_p \cdot (T_{\text{return}} - T_{\text{supply}}) = \text{__________ kW}$$ 
 *(Evaluate ρ and c_p for 25% Propylene Glycol at bulk temperature: $T_{\text{bulk}} = \frac{T_{\text{sup}} + T_{\text{ret}}}{2}$)* 
- **Enthalpy Heat Closure Ratio**: 
 $$\eta = \frac{Q_{\text{liquid}}}{P_{\text{elec}}} \times 100\% = \text{__________ \%} \quad (\text{Acceptance Band: } 97.0\% \le \eta \le 101.5\%)$$ — **PASS / FAIL** 
- **Dew Point Margin**: 
 - Data Hall Ambient Temperature: ______ °C Relative Humidity: ______ % Calculated Dew Point: ______ °C 
 - Margin: $T_sec\_sup - T_dew = __________ K$ (Acceptance Limit: ≥ 2.0 K) — **PASS / FAIL** 

### 3. Electrical Infrared (IR) Thermography Scan (30 Min into Step)
- Thermal Imaging Camera Model & Serial Number: ____________________ Calibration Expiry: ____________ 
- Peak Terminal Temperature Recorded: __________ °C (Acceptance Limit: ≤ 75.0°C) — **PASS / FAIL** 
- Physical Location of Hottest Terminal: __________________________________________________ 
- Maximum Phase-to-Phase Delta-T: __________ K (Acceptance Limit: ≤ 5.0 K) — **PASS / FAIL** 

### 4. Multi-Rack Secondary Flow Distribution Survey (10 Load Banks)

| RACK ID | LOAD BANK SERIAL | VOLUMETRIC FLOW (LPM) | DELTA FROM MEAN (%) | RACK dP (kPa) | PASS / FAIL |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Rack 01** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] PASS [ ] FAIL |
| **Rack 02** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] PASS [ ] FAIL |
| **Rack 03** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] PASS [ ] FAIL |
| **Rack 04** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] PASS [ ] FAIL |
| **Rack 05** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] PASS [ ] FAIL |
| **Rack 06** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] PASS [ ] FAIL |
| **Rack 07** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] PASS [ ] FAIL |
| **Rack 08** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] PASS [ ] FAIL |
| **Rack 09** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] PASS [ ] FAIL |
| **Rack 10** | LB-________________ | __________ LPM | ______ % | ______ kPa | [ ] PASS [ ] FAIL |
| **ROW STATS**| **Mean Flow: _______ LPM** | **Std Dev (σ): _______** | **CV ($\frac{\sigma}{\mu}\times 100\%$): _______ %** | Limit: ≤ 5.0% | **PASS / FAIL** |

**SHEET 3 STEP VERDICT**: [ ] **THERMAL STEP ACCEPTED** [ ] **STEP FAILED / UNSTABLE** 
**Authorized Test Lead (Command Authority)**: ____________________ **Signature**: __________________ 
**Lead Electrical PE Signature**: ________________________ **Date**: __________________ 
**Lead Mechanical PE Signature**: ________________________ **Date**: __________________ 

---

## Sheet 4. Dynamic Transient Failure & Redundancy Ride-Through Log (Level 5 IST)

**Project Name**: __________________________ **Data Hall / Room ID**: __________________________ 
**CDU Asset Tag**: __________________________ **Base Load During Test**: 1200 kW (100% Design Load) 
**Test Lead Signature**: ____________________ **Controls PE Signature**: ________________________ 
**Facility Owner Witness**: ________________ **Date & Shift Timestamp**: ______________________ 

*The steady-state recovered curve is not the pass. Record pre-event baseline, peak transient deflection, and recovery duration.*

### Scenario 1: Secondary Pump Trip & Auto-Changeover (N+1 VFD Swap)
- Pre-Event Operating Pump: Pump P-1A (Speed: 50.0 Hz, Flow: 115.0 m³/h, dP: 220 kPa) 
- Simulated Trip Injection Method: Inverter digital fault trigger at timestamp: ____________________ 
- Standby Pump P-1B Auto-Start Detected: __________ ms (Limit: ≤ 500 ms) 
- Minimum Secondary dP Recorded: __________ kPa (Limit: ≥ 100.0 kPa; no cavitation) 
- Peak Water Hammer Pressure Surge: __________ kPa (Limit: ≤ ± 50.0 kPa) 
- Secondary Flow Restored to ≥ 95% Design: __________ s (Limit: ≤ 1.5 seconds) 
- Load-Bank Thermal Interlock Tripped?: **YES (FAIL) / NO (PASS)** 
- Scenario 1 Verdict: **PASS / FAIL** 

### Scenario 2: 2N Electrical Feeder A Loss / ATS Bus Transfer
- Feeder A Breaker Tripped at Timestamp: ____________________ 
- Bus Transfer Switch Transition Duration: __________ ms (Limit: ≤ 16.0 ms) 
- CDU 24V DC Control Bus Voltage Minimum: __________ V DC (Limit: ≥ 22.0 V DC; zero dip) 
- CDU PLC Controller Reboot Observed?: **YES (CRITICAL FAIL) / NO (PASS)** 
- Secondary Pump VFD Ride-Through / Recovery: __________ s (Limit: ≤ 3.0 s) 
- Feeder B Steady-State Voltage: __________ V Current: __________ A 
- Scenario 2 Verdict: **PASS / FAIL** 

### Scenario 3: Primary Chilled Water Interruption (Thermal Inertia Ride-Through)
- Primary FWS Isolation Valve Commanded Closed at Timestamp: ____________________ 
- Secondary Supply Temp Pre-Trip: 40.0 °C Load Maintained: 1200 kW 
- Rate of Secondary Temperature Rise: $\frac{dT}{dt} = \text{__________ K / s}$ 
- Buffer Time to High Temp Alarm (45.0°C): __________ s (Limit: t_buffer ≥ 40.0 s) 
- Automated Load Shed Initiated by CDU Alert?: **YES / NO** 
- Emergency Over-Temperature Trip Actuated (50.0°C): Timestamp: ____________________ 
- All Load-Bank Heaters De-Energized Instantly?: **YES / NO** (Peak fluid temp: ______ °C) 
- Scenario 3 Verdict: **PASS / FAIL** 

### Scenario 4: BMS Communication Severance (Autonomous Local Fail-Safe)
- Modbus-TCP / BACnet Ethernet Cable Disconnected at Timestamp: ____________________ 
- CDU Local PLC Switched to Autonomous Standalone Mode?: **YES / NO** 
- Secondary Pump Speed Oscillation / Hunting Observed?: **YES (FAIL) / NO (PASS)** 
- Modulating TCV-101 Valve Drift / Hunting Observed?: **YES (FAIL) / NO (PASS)** 
- Secondary Supply Temp Maintained at 40.0°C ± 0.5 K for 30 Minutes: **PASS / FAIL** 
- Scenario 4 Verdict: **PASS / FAIL** 

### Scenario 5: Rapid Thermal Step-Change Shock ($100% \to 30% \to 100%$)
- Step Down from 1200 kW to 360 kW at Timestamp: ____________________ 
 - Minimum Secondary Supply Temp Undershoot: __________ °C (Limit: ≥ 38.5°C) 
 - TCV-101 Response Stabilization Time: __________ s (Limit: ≤ 45 s) 
- Step Up from 360 kW to 1200 kW at Timestamp: ____________________ 
 - Maximum Secondary Supply Temp Overshoot: __________ °C (Limit: ≤ 41.5°C) 
 - Secondary Fluid Flow Maintained Stable ± 2.0%: **PASS / FAIL** 
- Scenario 5 Verdict: **PASS / FAIL** 

**SHEET 4 DYNAMIC VERDICT**: [ ] **ALL TRANSIENT TESTS PASSED** [ ] **TRANSIENT FAILURES LOGGED** 
**Lead Test Lead Signature**: ________________________ **Date**: __________________ 
**Facility Owner Witness**: ________________________ **Date**: __________________ 

---

## Sheet 5. Controlled De-Energization, Cooldown & Demobilization Protocol

**Project Name**: __________________________ **Data Hall / Room ID**: __________________________ 
**Test Unit Asset Tag**: ____________________ **Shift Date & Time**: ____________________________ 
**Test Lead (Directing Shutdown)**: ________ **Lead Electrical PE**: __________________________ 
**Lead Mechanical PE**: ____________________ **Safety Lead**: ________________________________ 

*Every shutdown step must be executed and ticked in strict chronological sequence. Reversing steps voids this sheet.*

### 1. Mandatory Sequential De-Energization Steps

- [ ] **STEP 01: Shed Active Thermal Load to 0 kW** 
 *Command all load-bank heater stages to 0 kW via controller. Verify all thyristor SCR firing pulses cease and magnetic contactors drop open. Active power verified 0.0 kW.* 
 Timestamp: ____________________ Initials: ________ 

- [ ] **STEP 02: Open & Lock Out Load-Bank Power Feeders (LOTO)** 
 *Open load-bank branch circuit breakers at the PDU or overhead tap box. Apply lockout padlocks and danger tags. Verify circuits are dead with calibrated voltage detector.* 
 Timestamp: ____________________ Initials: ________ 

- [ ] **STEP 03: 10-Minute Fluid Circulation Cooldown Soak** 
 *CRITICAL: Maintain CDU secondary pumps running at 50.0 Hz for minimum 10 minutes with heaters dead. This removes latent heat from heater sheaths and prevents localized fluid boiling.* 
 Start Time: ____________________ End Time: ____________________ (Secondary Fluid Temp: ______ °C) 
 Initials: ________ 

- [ ] **STEP 04: Controlled Power Down of CDU Secondary Pumps** 
 *Stop CDU secondary pumps only after fluid temperature drops below 30.0°C. Confirm differential pressure decays smoothly to 0.0 kPa.* 
 Timestamp: ____________________ Initials: ________ 

- [ ] **STEP 05: Isolate Secondary Manifolds & Disconnect Hoses** 
 *Close secondary supply and return manual isolation valves. Relieve residual static head pressure via bleed valves into catch buckets. Disconnect quick-disconnect couplings.* 
 *(CRITICAL: If this step was ticked prior to Step 04, this sheet is immediately VOID.)* 
 Timestamp: ____________________ Initials: ________ 

### 2. Cryptographic Data Archive Verification
- [ ] Raw 1-second load-bank CSV telemetry exported and verified: **YES / NO** 
- [ ] 1-second BMS / PLC trend logs exported across all test timestamps: **YES / NO** 
- [ ] High-resolution infrared thermography captures and digital photos archived: **YES / NO** 
- Primary Secure Storage Location: __________________________________________________ 
- Secondary Redundant Offline Location: ____________________________________________ 
- Master Archive SHA-256 Checksum: ________________________________________________ 

### 3. Demobilization Inventory & Facility Restoration
- [ ] All quick-disconnect couplings and hoses counted out against Sheet 1 inventory: **ZERO MISSING** 
- [ ] Pressure-rated protective dust caps installed on all manifold supply and return ports: **YES / NO** 
- [ ] Permanent facility valves, circuit breakers, and BMS setpoints restored to baseline: **YES / NO** 
- [ ] Data hall raised floor tiles, pedestal stringers, and cable trays inspected for cleanliness: **YES / NO** 

**SHEET 5 CLOSEOUT VERDICT**: [ ] **SHUTDOWN EXECUTED IN RIGOROUS COMPLIANCE** 
**Authorized Test Lead Signature**: ________________________ **Date**: __________________ 
**Lead Electrical PE Signature**: ________________________ **Date**: __________________ 

---

## Sheet 6. Cold No-Heat Baseline Pump & Loop Resistance Curve

**Project Name**: __________________________ **Data Hall / Room ID**: __________________________ 
**CDU Asset Tag**: __________________________ **Pump Tag (A/B)**: ______________________________ 
**Lead Mechanical PE**: ____________________ **Measurement Tech**: __________________________ 
**Secondary Fluid Chemistry**: 25.0% PG **Measured Fluid Temp**: __________ °C (Target: 20.0°C ± 1.0 K) 

*Heat command must be interlocked to 0 kW. VFD frequency must be locked in manual override at 50.0 Hz (or 60.0 Hz).*

### 1. Verification of Prerequisite Baseline Controls
- [ ] Electrical heaters verified locked out; active electrical load is 0.0 kW: **CONFIRMED** 
- [ ] Automatic VFD differential pressure modulation disabled: **MANUAL LOCKOUT CONFIRMED** 
- [ ] Operating VFD frequency fixed and verified via calibrated tachometer/register: **50.0 Hz** 
- [ ] Refractometer confirmed secondary glycol concentration: **25.0% ± 0.5% PG** 

### 2. Four-Point Valve Throttling Hydraulic Data

| THROTTLING STEP | VALVE COMMAND POSITION | MEASURED FLOW Q (m³/h) | MEASURED FLOW Q (LPM) | PUMP HEAD ΔP_pump (kPa) | MANIFOLD dP ΔP_man (kPa) | MOTOR CURRENT (A) | VFD POWER (kW) | CONTROL MODULATION OFF? |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Point 1: Max Flow** | 100% Fully Open | __________ m³/h | __________ LPM | ______ kPa | ______ kPa | ______ A | ______ kW | [ ] YES (Locked) |
| **Point 2: 80% Flow** | Throttled (~80%) | __________ m³/h | __________ LPM | ______ kPa | ______ kPa | ______ A | ______ kW | [ ] YES (Locked) |
| **Point 3: 60% Flow** | Throttled (~60%) | __________ m³/h | __________ LPM | ______ kPa | ______ kPa | ______ A | ______ kW | [ ] YES (Locked) |
| **Point 4: 40% Flow** | Throttled (~40%) | __________ m³/h | __________ LPM | ______ kPa | ______ kPa | ______ A | ______ kW | [ ] YES (Locked) |

### 3. Hydraulic Curve Acceptance Audit
- Vendor Certified Submittal Pump Curve Reference: Document ID: ____________________ Rev: ______ 
- Point 1 Head vs Flow Deviation from Certified Curve: __________ % (Limit: ≤ ± 5.0%) 
- Point 2 Head vs Flow Deviation from Certified Curve: __________ % (Limit: ≤ ± 5.0%) 
- Point 3 Head vs Flow Deviation from Certified Curve: __________ % (Limit: ≤ ± 5.0%) 
- Point 4 Head vs Flow Deviation from Certified Curve: __________ % (Limit: ≤ ± 5.0%) 
- Maximum Secondary Fluid Temperature Rise During Run: __________ K (Limit: ≤ 0.5 K) 

**SHEET 6 BASELINE VERDICT**: [ ] **COLD PUMP CURVE ACCEPTED & FILED** [ ] **CURVE OUT OF TOLERANCE** 
**Lead Mechanical PE Signature**: ________________________ **Date**: __________________ 
**Test Technician Signature**: ____________________________ **Date**: __________________ 

---

## Sheet 7. CDU Autonomous Control Logic & Supervisory Interface Audit

**Project Name**: __________________________ **Data Hall / Room ID**: __________________________ 
**CDU Asset Tag**: __________________________ **Vendor Logic Doc Ref**: __________________________ 
**Lead Controls PE**: ______________________ **Vendor Commissioning Engineer**: ________________ 

*Vendor control logic submittal must be attached to this sheet. If documentation is missing, mark NOT DEMONSTRATED.*

### 1. Autonomous Control Logic Failure Modes

| CONTROL SCENARIO | EXPECTED VENDOR LOGIC SPECIFICATION | PHYSICAL SIMULATION RESULT | AUDIT VERDICT |
| :--- | :--- | :--- | :--- |
| **Primary Control Temp Sensor Disconnected** | Controller detects open-circuit loop; generates critical alarm; rejects sensor and automatically reverts to redundant secondary immersion sensor. | Controller alarmed instantly; switched to TT-202; zero valve hunting observed. | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Primary Differential P Sensor Line Severed**| Controller flags transmitter signal loss (4-20mA out of range); locks VFD at last stable frequency; prevents pump runout. | Alarm annunciated; VFD maintained 48.2 Hz stable; differential pressure held. | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Operating PLC Controller Power Severed** | System enters hardware fail-safe: primary modulating valve fails 100% open; running secondary pump continues at max line frequency.| TCV spring-returned to 100% open; pump continued circulating; no thermal trip. | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Pump VFD Internal Inverter Overload Fault**| Inverter output trips; auxiliary contact signals CDU PLC; standby pump starts and achieves pressure within ≤ 1.5 s. | Standby pump P-1B started in 1.1s; loop pressure held ≥ 120 kPa. | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Modbus-RTU Drive Comm Cable Severed** | Drive loses serial communication heartbeat; holds last commanded speed; CDU logs comms loss alarm without stopping loop. | Drive maintained 50.0 Hz; comm alarm logged on HMI; fluid flow continued. | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Group-Control Master Network Severed** | Unit detects loss of group master token; autonomous local controller assumes standalone PID loop tracking seamlessly. | Unit transitioned to local mode in 800ms; secondary supply T maintained 40.0°C. | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Electric Actuator 24V Power Loss** | Actuator internal spring-return or supercapacitor drives valve mechanism to 100% full-open position. | Valve driven mechanically to 100% open; maximum primary chilled water available. | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |
| **Expansion Tank High-Pressure Relief Trip**| Relief valve opens at 6.0 bar; high-pressure switch trips; CDU stops makeup pump and sends high-priority alarm. | Switch tripped at 5.8 bar; makeup pump locked out; alarm received by BMS. | [ ] PASS [ ] FAIL [ ] NOT DEMONSTRATED |

### 2. Ring Header Sectional Isolation (Only if Secondary is Ring Topology)
- [ ] Nearest secondary branch isolation valve closed and reopened: 
 *Load-bank thermal stability maintained: **YES / NO** CDU supply pressure stable: **YES / NO*** 
- [ ] Farthest secondary branch isolation valve closed and reopened: 
 *Load-bank thermal stability maintained: **YES / NO** CDU supply pressure stable: **YES / NO*** 

### 3. Supervisory BMS Telemetry Register Consistency Audit

| TELEMETRY PARAMETER | BMS POINT TAG | CDU LOCAL DISPLAY | CALIBRATED FIELD REF | TELEMETRY DISCREPANCY | AUDIT LIMIT | VERDICT |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Secondary Supply T** | `CDU01_TCS_SUP_T` | 40.10 °C | 40.08 °C | 0.02 K | ≤ ± 0.30 K | **PASS / FAIL** |
| **Secondary Return T** | `CDU01_TCS_RET_T` | 50.15 °C | 50.12 °C | 0.03 K | ≤ ± 0.30 K | **PASS / FAIL** |
| **Secondary Flow Rate** | `CDU01_TCS_FLOW` | 115.8 m³/h | 116.1 m³/h | 0.26 % | ≤ ± 2.0% | **PASS / FAIL** |
| **Secondary Supply P** | `CDU01_TCS_SUP_P` | 282.0 kPa | 280.5 kPa | 1.5 kPa | ≤ ± 10.0 kPa| **PASS / FAIL** |
| **Primary TCV Position**| `CDU01_TCV_POS` | 64.0 % | 64.5 % (Stroked) | 0.5 % | ≤ ± 2.0% | **PASS / FAIL** |

**SHEET 7 LOGIC VERDICT**: [ ] **CDU AUTONOMOUS LOGIC CERTIFIED** [ ] **LOGIC DEFICIENCIES NOTED** 
**Lead Controls PE Signature**: ________________________ **Date**: __________________ 
**Vendor Commissioning Engineer**: ____________________ **Date**: __________________

---
