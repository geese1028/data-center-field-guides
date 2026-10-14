# 0. How to Use This Book

This book is for the person who manages a data center day. It is the shift, the work that is allowed to happen, the thing that went wrong, and the sentence you can still say at the end of the day.

It is not a facilities-operations course. It is not a substitute for sitting one. Certified Data Centre Facilities Operations Manager (CDFOM) and Certified Data Centre Facilities Operations Specialist (CDCS) are course titles. This book does not retell their slides, their multiple-choice exercises, or their examinations. If you need the credential for your client's vendor matrix, take the course from the organization that owns it.

It is not a copy of a service-management library, a security standard, a design standard, or a safety code. ITIL, ISO/IEC 20000, ISO 22301, ISO 55001, NFPA 70E, and OSHA 1910 have titles and editions. Cite them. Do not paste them. A manager who pastes sixty pages of corporate boilerplate into a shift folder has not run the facility; they have built a paper wall to hide behind when a chiller trips.

The earlier books in this series stop at a machine, a file, a test, or a model:
- Book 01 builds the liquid load bank and instruments the manifold.
- Book 02 reads the thermal and hydraulic flash report.
- Book 03 executes the seven sheets of commissioning verification.
- Book 04 audits the computational fluid dynamics model against physical measurements.

This book starts when the commissioning agents have packed their pelican cases, the temporary load banks are on the flatbed trucks, the IT servers are live, and someone will be blamed if the hall goes dark.

```
+-----------------------------------------------------------------------------+
| DATA CENTER SHIFT LIFECYCLE |
| |
| [07:00] Incoming & Outgoing Joint Walkthrough (30 min, 6 physical stations)|
| | |
| [07:30] Shift Handover Gate (Sign Day Sheet: Impairments, Permits, MOPs) |
| | |
| [08:00] Morning Baseline Telemetry & Catch-Pan Inspection |
| | |
| [10:00] Authorized Maintenance Window (MOP Execution, LOTO, Active Escort) |
| | |
| [14:00] Afternoon Deep Round (Acoustic, Thermal IR, Refractometer, DPs) |
| | |
| [18:30] Pre-Close Audit: Clear Permits, Verify Normal Configurations |
| | |
| [19:00] The Closeout Sentence: The single binding statement of the day |
+-----------------------------------------------------------------------------+
```

![Shift Lifecycle and Handover Architecture](../figures/fig-01-shift-lifecycle-and-handover.png)

When you finish each day, you must be able to hand over one day sheet. It names who is on shift, what work is permitted, what changed, what you physically walked, what failed, and what you will not claim. It is in Chapter 10 and in `sheets/day.md`. If you are the incoming manager tomorrow morning, start there.

## What You May Copy

You may copy the sheet headings into your own operations logbook or site management software. You may not paste a sentence from this book into a customer Service Level Agreement (SLA) and call it their operational rule. Their facility has its own operating permits, its own contractual notice windows, and its own emergency escalation paths. This book tells you what those documents must enforce. It does not replace them.

## Decisions to Record

- The single binding sentence the day is allowed to support.
- The standard, code, or contract you will cite by title and edition, and not paste.
- The day sheet you will physically sign before you hand the radio to the next shift.

---

# 1. What the Manager Owns Today

A manager who tries to own the design, the customer's application software, and the vendor's factory warranty at once owns none of them. Today you own the operating state of the facility, the people who may touch it, and the immutable record of what was done.

You do not own whether a customer's distributed database correctly shards its data across clusters. You own whether the dual power feeds, the cooling loop flow rate, and the physical security envelope you sold them were delivered within the contractually signed parameters. If the contract is silent on a topic, you do not invent a promise in the daily operations log. A customer technical director who is yelling on a conference call is not a new contract clause.

You do not own a plant redesign. A change that alters how the electrical switchgear or the secondary cooling loop fails is an engineering capital project, requiring peer review, protective relay coordination studies, and executive sign-off. Daily operations may propose it. Daily operations may never smuggle it into a scheduled maintenance window and call it a "routine operational adjustment." If the work requires an electrical single-line diagram (SLD) or a piping and instrumentation diagram (P&ID) to be redrawn, it is not today's maintenance. Stop the tools.

You do not own the framed certificates on the reception wall. An ISO 9001 plaque, an Uptime Institute Tier IV design certificate, or a corporate sustainability award is not evidence that today's shift operated competently. Evidence is the day sheet: names of qualified operators on site, active permits to work, recorded physical rounds, and the incident you refused to hide.

## The First Half Hour

Read four things before you open a telemetry dashboard, check an email, or drink your coffee:

1. **Impairments carried from the previous shift**: Any generator locked out of automatic start, any fire zone disabled on the VESDA panel, any secondary cooling distribution unit (CDU) running on single-pump bypass, or any uninterruptible power supply (UPS) running on static bypass.
2. **Permits still open, and the exact minute each expires**: A Permit to Work (PTW) is a temporary lease on risk. If a permit expired at 06:00 and the vendor is still inside the medium-voltage switchgear room, the facility is operating in an unauthorized state.
3. **Incidents still open, and who owns each ticket**: If an incident occurred during the night, identify who holds the technical lead and what safe state was established.
4. **Changes whose execution window is today, and who formally accepted the risk**: Verify that every scheduled change has an approved Method of Procedure (MOP) with an unambiguous back-out plan.

```
+-------------------------------------------------------------------------+
| THE FOUR MANDATORY PRE-SHIFT CHECKS |
| |
| [1] Active Impairments --> Fire suppression, bypass valves, UPS N-1 |
| [2] Open Permits --> Location, work scope, expiration timestamp |
| [3] Active Incidents --> Severity, containment state, named owner |
| [4] Today's Changes --> Approved MOP, risk acceptor, back-out plan |
+-------------------------------------------------------------------------+
```

If any of the four is missing from the turnover log, the handover has failed. Do not accept the radio. Do not sign the log. A facility manager who signs an incomplete turnover inherits every hidden defect, every disabled safety interlock, and every unrecorded trip that happened during the previous twelve hours.

Once the four items are reviewed, walk the physical locations where today's work will occur before the vendor or contractor arrives at the security gate. Inspect the specific electrical panel, the isolation valves, and the service corridor. If the physical conditions on the ground make it impossible to isolate the equipment safely according to the written procedure, the paper is wrong. Cancel the work. Never discover that a manual isolation valve is seized or that a bypass breaker is padlocked with the equipment already opened.

Write the single binding sentence for the day before the morning rush begins. In a professional facility, that sentence is intentionally boring:
> *"The critical power and cooling infrastructure remained strictly within contractual SLA envelope; all authorized maintenance tasks were completed under approved MOPs without service disruption; no unrecorded impairments exist on site."*

If you cannot sign that exact sentence at the end of the shift, the day was an operational failure, even if the executive dashboards were glowing green.

## What You Do Not Delegate

You may delegate turning a valve handle, racking out a 480V circuit breaker, or taking differential pressure readings across a bag filter. You may never delegate:
- The decision that the facility is still operating within contractual SLA.
- The authorization to initiate an intrusive change window.
- The decision to issue an incident notification to the customer.

Those three responsibilities stay exclusively with the licensed operations manager on duty, or with the formally designated deputy named in writing on the shift roster. A corporate chat group is not a designated deputy.

## Decisions to Record

- The operating service standard, cited by exact contract title and section number.
- What you explicitly will not promise to the client today.
- The four turnover checks: verified present, or flagged as missing.
- The binding closeout sentence you intend to sign at the end of the shift.

---

# 2. People on Shift

A data center does not run on software telemetry. It runs on the competence, licensing, and physical discipline of the technicians walking the plant floors. If you do not know the exact qualifications of the people holding the master keys, you do not control the plant.

```
+-----------------------------------------------------------------------------+
| SHIFT QUALIFICATION & GATING MATRIX |
| |
| Role Certifications Required Authorized Scope |
| ------------------ ---------------------------- ----------------------- |
| Duty Manager CDFOM / Operations License Overall SLA & Permits |
| Lead Electrician High-Voltage (HV/LV) License Switchgear, Transformers |
| Cooling Specialist Refrigeration / HVAC License Chillers, CDUs, Glycol |
| Shift Technician Data Center Facilities Cert Rounds, Telemetry, Logs |
| Escort / Safety OSHA 30 / First Aid / CPR Vendor Supervision, LOTO |
+-----------------------------------------------------------------------------+
```

## Licensing and Statutory Requirements

In high-density AI data centers housing megawatt-scale liquid cooling and multi-megavolt-ampere electrical substations, generic facility technicians are an existential liability. Operational tasks require statutory certification:
- **Electrical Operations**: Any switching, racking, or live testing on medium-voltage (10kV/35kV) or low-voltage (400V/480V) switchgear must be performed exclusively by certified high-voltage/low-voltage electricians holding valid governmental licenses.
- **Cooling & Chemical Operations**: Operating centrifugal chillers, industrial cooling towers, and primary/secondary pumping stations requires licensed refrigeration technicians certified in pressurized refrigerant handling and industrial water treatment.

Per OpenViking operational guidelines (`ALZJ-YW-2.6XZ10`), liquid cooling operations involving secondary distribution units (CDUs), primary facility water systems (FWS), and rack-level manifolds require verified technical training on chemical biocides, glycol concentration measurement, and leak containment protocols.

If a technician on shift lacks the statutory license for high-voltage switching, their name may not appear on an electrical switching ticket. If an unlicensed contractor is found with an open panel door, work stops immediately.

## The Two-Person Rule

No critical switching operation, high-voltage racking, or valve isolation on a primary cooling loop may ever be performed by a solo technician.

The two-person rule requires:
1. **The Performer**: The certified technician holding the approved Method of Procedure (MOP) who physically touches the control switch, breaker handle, or isolation valve.
2. **The Checker**: An equally qualified technician standing immediately behind the performer, holding the printed procedure, reading each step aloud, verifying equipment tags (e.g., confirming breaker label `SWG-01-4A` matches the ticket before racking), and maintaining emergency stop awareness.

The checker's sole duty during the operation is verification and safety. If the performer begins reaching for the wrong breaker handle or turns a valve in the wrong sequence, the checker possesses absolute authority to halt the operation instantly.

```
+-------------------------------------------------------------------------+
| THE TWO-PERSON RULE |
| |
| +------------------+ +------------------+ |
| | THE CHECKER | | THE PERFORMER | |
| | Holds MOP sheet | | Touches switch | |
| | Reads step loud | ----------> | Points to label | |
| | Verifies tag ID | | Executes action | |
| | Has Stop Power | | Reports status | |
| +------------------+ +------------------+ |
+-------------------------------------------------------------------------+
```

## Stop Work Authority (SWA)

Every individual entering the facility—from the senior operations director to an apprentice cable puller—possesses full, unconditional Stop Work Authority.

Stop Work Authority is triggered whenever:
- Physical conditions in the room diverge from the assumptions in the written MOP.
- An unexpected alarm sounds on the Building Management System (BMS) or Electrical Power Monitoring System (EPMS).
- Water droplets, fluid pooling, or abnormal chemical odors are detected near electrical equipment.
- A required safety barricade, personal protective equipment (PPE), or Lockout/Tagout (LOTO) lock is missing or compromised.
- An operator experiences confusion or uncertainty regarding the next procedural step.

When Stop Work is invoked:
1. Equipment is immediately placed into the nearest stable, safe state defined in the procedure.
2. Tools are set down; no further valves or switches are moved.
3. The duty manager is summoned to the work location.
4. Work resumes only after the ambiguity is resolved and documented in writing on the permit.

No technician or contractor may ever be reprimanded, penalized, or questioned for invoking Stop Work in good faith. A facility culture where technicians hesitate to call Stop Work because of schedule pressure is a facility waiting for a multi-megawatt blackout.

## The 30-Minute Joint Walkthrough

Never execute a shift handover sitting behind desks in the control room. A handover completed over coffee is an abdication of duty.

The incoming duty manager and outgoing duty manager must complete a mandatory 30-minute joint physical walkthrough of the six critical facility zones before signing the Day Sheet:
1. **Medium-Voltage Substation**: Inspect 35kV/10kV switchgear, breaker spring charge indicators, SF6 gas pressure gauges, and battery charger status.
2. **Transformer Vaults**: Inspect dry-type/oil-filled transformer winding temperatures (ensure T < 90°C), cooling fan operation, and listen for abnormal acoustic harmonics.
3. **UPS & Battery Rooms**: Verify DC bus float voltages, individual string temperatures (T < 25°C), inspect for battery post corrosion or swelling, and verify hydrogen exhaust fan airflow.
4. **Central Chiller & Pumping Plant**: Check chiller approach temperatures (ΔT_approach ≤ 1.5 K), condenser head pressures, variable frequency drive (VFD) frequencies, and acoustic vibration.
5. **CDU Liquid Stations**: Verify primary/secondary pressures (0.15 - 0.90 MPa), pump differential pressures (ΔP < 1.0 bar), expansion tank fluid levels, and inspect catch basins for moisture.
6. **AI Whitespace Halls**: Walk hot and cold aisles, inspect power distribution units (PDUs) for thermal hotspots, verify tile differential pressure (ΔP ≥ 5 Pa), and check quick-disconnect couplings (FD83/UQD) for weeping.

Both managers must walk the entire path side-by-side. If the outgoing manager refuses to walk the floor, the incoming manager assumes all plant equipment is in an unverified state and notes the refusal on the turnover log.

## Decisions to Record

- Names of all on-shift personnel, their verified license numbers, and expiration dates.
- Confirmation that high-voltage and critical fluid operations adhere to the two-person rule.
- Any invocation of Stop Work Authority during the shift, detailing the cause and resolution.
- Completed 30-minute joint physical walkthrough signed by both incoming and outgoing managers.

---

# 3. The Service You Sold

Customers do not buy your diesel fuel tanks, your titanium plate heat exchangers, or your personal dedication. Customers buy an SLA: a mathematically defined service contract guaranteeing electrical availability, thermal delivery, and escalation timing. If you cannot cite the exact clause in the master service agreement, you are operating on hearsay.

```
+-----------------------------------------------------------------------------+
| SERVICE BOUNDARY MATRIX |
| |
| Contract Parameter Guaranteed Limit Measurement Source |
| ----------------------- ------------------------- --------------------- |
| AC Power Availability 99.999% (Five Nines) Active PDU Revenue Mtrs|
| Secondary Supply Temp 25.0°C to 32.0°C (W3/W4) CDU TCS Supply RTD Tree|
| Primary Chilled Water 12.0°C to 18.0°C FWS Header Flow/Temp |
| Air Temperature (Rack) 18.0°C to 27.0°C (ASHRAE) Cold Aisle Sensors (3h)|
| Incident Notice Clock <= 15 Minutes from T-0 Client Portal & Phone |
+-----------------------------------------------------------------------------+
```

## Contractual Service Limits vs. Engineering Margins

Operating a data center requires distinguishing between three distinct boundaries:
1. **Design Setpoints**: The optimal operating conditions engineered into the control sequences (e.g., CDU secondary supply at 28.0°C, cold aisle air at 22.0°C).
2. **Operational Alarm Limits**: The internal facility thresholds that alert technicians to take corrective action before client impact occurs (e.g., secondary supply reaches 30.5°C, prompting standby pump start or chiller staging).
3. **Contractual Breach Limits**: The legal boundaries defined in the client SLA that trigger service credit penalties and default notices (e.g., secondary supply exceeding 32.0°C for > 5 continuous minutes, or rack intake air exceeding 27.0°C).

Never allow the client's commercial representative to treat an internal operational alarm as a contractual service breach. Conversely, never allow your shift team to dismiss a temperature excursion that crossed the SLA threshold simply because "it only spiked for three minutes." If the contract measures excursions in 60-second rolling averages, a three-minute spike is an SLA violation. Log it.

## The Availability Equation

Data center availability (A) is calculated as:

$$A = \frac{\text{Total Period Minutes} - \text{Outage Minutes}}{\text{Total Period Minutes}}  \times 100\%$$

In modern multi-tenant colocation and hyperscale build-to-suit contracts, "Outage Minutes" are defined with extreme legal precision:
- Does an outage require loss of power on both A and B cords of a 2N rack, or does loss of redundancy on a single cord constitute a fractional outage?
- If a customer's server continues running on cord B while cord A is de-energized, does the SLA clock run?
- If a liquid cooling CDU drops from N+1 dual pumps to single pump operation without thermal derating, has an outage occurred?

The duty manager must know the contractual answer to these questions before an event occurs. During a live incident, there is no time to consult external legal counsel.

## The Notice Period Clock

When an infrastructure excursion crosses an SLA threshold, the clock begins ticking immediately:

$$\Delta t_{\text{notice}} = t_{\text{sent}} - t_{\text{detect}} \le T_{\text{contractual}}$$

Most hyperscale SLAs require formal incident notification within **15 minutes** of initial detection (T_contractual ≤ 15 min).

```
+-------------------------------------------------------------------------+
| THE 15-MINUTE NOTIFICATION WINDOW |
| |
| T = 00:00 Alarms trigger on BMS/EPMS; trip detected |
| T + 05:00 Duty Manager verifies event; stabilizes safe state |
| T + 10:00 Draft incident notification: Symptom, Time, Impacted Halls |
| T + 14:00 Notification transmitted to client technical contacts |
| T + 15:00 Contractual SLA notification deadline expires |
+-------------------------------------------------------------------------+
```

A common failure among novice operations managers is delaying the initial customer notification while technicians investigate the root cause. This is a contractual disaster. A client will forgive a transformer trip that was stabilized within minutes; they will never forgive discovering their servers are down from their own telemetry while the data center manager remained silent for forty minutes.

Send the notification at minute 12. State the observed facts: the timestamp of the event, the affected electrical buses or cooling loops, the current status of the emergency systems, and the timestamp of the next update. Keep root-cause theories completely off the wire.

## What You Do Not Report as Owed

Measure only what the contract specifies. Generating internal operational metrics—such as real-time Power Usage Effectiveness (PUE), Carbon Usage Effectiveness (CUE), or Water Usage Effectiveness (WUE)—is vital for facility engineering and corporate sustainability reporting. However, do not paste internal PUE calculations into a daily SLA delivery certificate unless the contract explicitly defines PUE as a billable SLA parameter.

If an efficiency ratio is not part of the commercial contract, reporting it on a daily client log turns an internal engineering aspiration into an external target that clients will use to dispute invoices. Keep contractual delivery logs strictly separated from internal engineering analytics.

## Decisions to Record

- The exact master contract title, amendment number, and clause governing today's service.
- The authoritative telemetry meter ID and clock source used for contractual timekeeping.
- The contractual notification window (T_contractual) in minutes.
- Any SLA excursion observed during the shift, recorded with microsecond timestamps from the sequence-of-events recorder.

---

# 4. Work That Is Allowed

Work performed in a production data center without a validated, written method is not engineering; it is gambling with the customer's business.

```
+-----------------------------------------------------------------------------+
| OPERATIONAL DOCUMENTATION PYRAMID |
| |
| /\ |
| / \ |
| / PTW\ PERMIT TO WORK |
| /------\ Who, Where, When, Tools |
| / \ |
| / MOP \ METHOD OF PROCEDURE |
| /------------\ Step-by-Step, Isolations, Backout|
| / \ |
| / SOP \ STANDARD OPERATING PROCEDURE |
| /------------------\ Routine Shift Rounds & Valve Lineups|
| / \ |
| / EOP \ EMERGENCY OPERATING PROCEDURE |
| /------------------------\ Immediate Muscle Memory Safe-State |
+-----------------------------------------------------------------------------+
```

![Procedural Governance Pyramid](../figures/fig-02-sop-mop-eop-governance-pyramid.png)

Four distinct operational documents govern every physical action on site. Never conflate their functions.

## Standard Operating Procedures (SOP)

An SOP governs recurring, baseline operations where the system configuration remains within normal operating limits:
- Executing daily physical shift rounds.
- Conducting chemical water sampling and glycol refractometer tests.
- Operating the manual bypass valve on a water softener skid.
- Performing routine filter differential pressure checks.

Every SOP must exist as a printed, laminated document physically located at the point of work (e.g., mounted inside the CDU enclosure or on the wall of the water treatment plant). An SOP that exists only as a PDF buried in a corporate intranet directory is useless to a technician holding a sample flask.

## Method of Procedure (MOP)

A MOP governs any scheduled, non-routine activity that touches critical infrastructure, alters equipment redundancy, or introduces risk of electrical or thermal disruption:
- Racking in or racking out a 480V air circuit breaker.
- Isolating a primary plate heat exchanger for acid cleaning.
- Replacing a mechanical seal on a 75 kW secondary loop pump.
- Updating firmware on a central Building Management System controller.

Every MOP must contain six mandatory structural sections:
1. **Scope and Equipment Identification**: Explicitly naming the assets by unique equipment tag, building, room, and coordinate.
2. **Pre-Requisite Conditions**: Verifying that redundant systems (N+1 or 2N) are 100% operational, fully available, and free of active alarms before work commences.
3. **Required Personal Protective Equipment (PPE) & Specialized Tools**: Arc-flash suits, calibrated torque wrenches, insulated tools, pressure gauges, and spill containment kits.
4. **Step-by-Step Execution Sequence**: Numbered, sequential actions with checkboxes and signature blocks for both the Performer and Checker at every single step.
5. **Detailed Back-Out Plan**: The precise, pre-calculated sequence of actions required to abort the work and return the plant to a 100% stable, redundant operational state at any point during the window.
6. **Sign-Off and Technical Acceptance**: Formal verification that the equipment has been restored to service, tested under load, and that all temporary jumpers, LOTO padlocks, and tools have been removed.

A MOP drafted or edited on a clipboard while standing in front of an open electrical cabinet is an incident report waiting to happen. If a procedural step cannot be completed as written, the technician must stop work, back out to the last safe step, and seek formal engineering re-approval.

## Emergency Operating Procedures (EOP)

An EOP governs the immediate, high-stress response during an active equipment failure or catastrophic event:
- Uncontrolled secondary liquid cooling loop leak (> 50 LPM).
- Complete loss of external utility medium-voltage grid power.
- Catastrophic failure of an automatic transfer switch (ATS).
- Chiller plant electrical bus fire requiring emergency power off (EPO).

An EOP is designed for raw muscle memory. It must never exceed **two pages** in length. An EOP that contains twenty pages of narrative text is an engineering textbook, not an emergency procedure.

An effective EOP names only three things:
1. **The Stop**: The immediate manual actions to halt further damage (e.g., hit the emergency isolation valve button `EIV-101`, trip the battery disconnect breaker).
2. **The Call**: The exact operational role or phone number to summon emergency response (e.g., Duty Manager radio channel 1, municipal fire dispatch).
3. **The First Safe State**: The verified stable operating mode to hold while incident management takes over (e.g., transition remaining IT load to secondary bus B, engage emergency glycol makeup pump).

Once the first safe state is secured, the EOP ends. All subsequent investigative, restoration, or repair work converts immediately into a planned operation governed by a formal MOP.

## Permit to Work (PTW)

A Permit to Work sits atop the procedural framework. It is the legal and operational authorization granted by the Duty Manager permitting specific individuals to execute an approved MOP within an exact physical space during a defined time window.

A valid PTW enforces four hard constraints:
- **Location**: Specific room, aisle, and cabinet. Working outside the permit boundary is a direct safety violation.
- **Time Window**: Explicit start and end timestamps. An expired permit is an immediate Stop Work command.
- **Personnel**: Named individuals with verified qualification records on file.
- **Lockout/Tagout (LOTO)**: Verification that all hazardous electrical, hydraulic, pneumatic, and chemical energy sources are physically locked, tagged, and zero-energy verified (test-before-touch).

```
+-------------------------------------------------------------------------+
| PTW & LOTO AUDIT GATES |
| |
| [GATE 1] Approved MOP attached with complete back-out procedure |
| [GATE 2] Personnel qualifications verified against site trade matrix |
| [GATE 3] Zero Energy Verification: Multi-meter test & pressure bleed |
| [GATE 4] Physical LOTO hasp, red lock, and danger tag applied |
| [GATE 5] Redundancy check: Alternate path verified carrying load |
+-------------------------------------------------------------------------+
```

## Critical Spares Verification

No maintenance procedure may commence until all critical replacement parts are physically present at the job site.

A "critical spare" is not whatever parts happen to be sitting in the warehouse. A critical spare is the exact component whose failure or unavailability would prevent the execution of the MOP's back-out plan. For a secondary CDU pump replacement, the critical spares include:
- Replacement mechanical seal assembly with matching EPDM elastomers.
- Set of factory-spec mating gaskets for suction and discharge flanged connections.
- 50 liters of pre-mixed 25% propylene glycol solution.
- Calibrated torque wrench with current calibration certificate.

If the technician opens the CDU enclosure and then discovers that the replacement flange gasket is missing from the parts cage, the job does not start. Hoping that the old gasket can be scraped off and reused without leaking is how secondary cooling loops spray glycol across 400V busways.

## Decisions to Record

- All active SOPs verified present as physical, readable documents at the equipment.
- All MOPs approved for today's shift, with service impact classifications recorded.
- LOTO registry numbers and physical padlock tag IDs applied to equipment.
- Exact expiration timestamps for all active Permits to Work.
- Confirmation that all critical spares were visually inspected and verified on site before permit issuance.

---

# 5. Change

Most catastrophic data center outages are not caused by lightning strikes, earthquakes, or manufacturer component defects. Most catastrophic outages are changes that were casually categorized as "routine maintenance."

```
+-----------------------------------------------------------------------------+
| CHANGE EXECUTION LIFECYCLE |
| |
| [T - 72h] Engineering Review: Risk assessment, single-point failure audit |
| | |
| [T - 24h] Change Advisory Board (CAB) Sign-Off: Risk accepted in writing |
| | |
| [T - 02h] Pre-Window Verification: Redundant plant 100% healthy, no alarms |
| | |
| [T = 00h] Maintenance Window Opens: Abnormal state posted on shift board |
| | |
| [T + Execution] Step-by-Step MOP Execution under Two-Person Rule |
| | |
| [T + Verification] Functional Load Verification: Telemetry confirms service|
| | |
| [T + Close] Post-Change Sign-Off: Abnormal state cleared, turnover updated |
+-----------------------------------------------------------------------------+
```

## What Constitutes a Change

A change is any physical, electrical, mechanical, or logical action that alters:
- How the critical infrastructure fails under transient conditions.
- How the plant is operated, monitored, or controlled by technicians.
- The redundancy, capacity, or path configuration delivered to the customer.

Replacing an indicator LED with an identical factory part is maintenance, provided the task requires no electrical isolation and introduces no risk of control bus short-circuiting. Replacing a thermal-magnetic circuit breaker with one possessing a different trip curve, altering a variable frequency drive's acceleration ramp rate, modifying a Building Management System PID loop tuning parameter, or adjusting a CDU secondary loop temperature setpoint by even 0.5 K is a change.

Transferring critical server load from electrical Bus A to Bus B—even for twenty minutes—is a critical change. If an unexpected transient occurs on Bus B while Bus A is isolated, the entire facility drops. If an operational action prompts any debate over whether it constitutes maintenance or change, default immediately to treating it as a change.

## The Change Advisory Board and Risk Acceptance

Every change requires formal approval from the Change Advisory Board (CAB) prior to execution.

The CAB submission must document:
1. **The Operational Justification**: Why the change must occur. "The vendor technician was already on site for another job" is never an acceptable justification. Acceptable justifications are resolving a logged defect, accommodating contracted capacity expansion, or mitigating an identified safety vulnerability.
2. **The Operational Risk Level**: Classified according to potential customer impact:
 - **Level 1 (Critical)**: Intrusive work touching active power distribution or primary cooling loops serving production IT workloads. Requires executive operations director sign-off and mandatory customer notification.
 - **Level 2 (Major)**: Work on redundant (N+1) systems where failure of the surviving system during the window would result in customer impact.
 - **Level 3 (Minor)**: Non-intrusive work on auxiliary or support systems where physical and electrical separation guarantees zero service risk.
3. **The Risk Acceptor**: A named senior leader who possesses the contractual and financial authority to accept the risk of the change. The field technician holding the torque wrench is not the risk acceptor. If the named risk acceptor is unreachable, the maintenance window does not open.

## The Abnormal State Board

During the maintenance window, the facility enters a named, temporary **Abnormal Operating State**.

The exact nature of this abnormal state must be:
- Written prominently on the physical whiteboard in the central control room.
- Displayed on the digital Building Management System banner across all operator workstations.
- Recorded explicitly on the shift handover log.

```
+-------------------------------------------------------------------------+
| CONTROL ROOM ABNORMAL STATE BOARD |
| |
| [ACTIVE IMPAIRMENT] Chiller CH-03 isolated for condenser overhaul |
| [SURVIVING REDUNDANCY] 3 of 4 chillers operating; redundancy = N+0 |
| [RISK] Loss of CH-01 or CH-02 triggers automatic load shedding |
| [WINDOW] 2026-10-14 10:00 to 14:00 UTC | Risk Acceptor: J. Vance (VP) |
| [BACK-OUT DEADLINE] 13:00 UTC (If not re-assembled, abort and restore) |
+-------------------------------------------------------------------------+
```

An abnormal state that finishes in the physical sense (e.g., the mechanic tightens the final bolt) but is not formally cleared on the control room board and turnover log remains an open operational hazard. If an unexpected alarm occurs two hours later, the incoming shift will troubleshoot based on the assumption of a normal plant configuration, leading to erroneous switching decisions and cascading equipment trips.

## Pre-Window Verification and Back-Out Execution

Never initiate a change window based on the assumption that redundant systems are operational. Two hours prior to opening the window (T-2 h), the duty team must perform a comprehensive pre-window audit:
- Verify that all surviving redundant units (2N electrical feeders, N+1 chillers, standby generator sets) are online, running stably, and completely free of active or latent alarms.
- Confirm that no severe weather alerts (lightning storms, grid instability, extreme heat waves) are forecast during the execution window.
- Verify that external emergency service support (utility grid operators, fuel delivery vendors, specialized service contractors) is on standby.

Every MOP must include an unambiguous **Back-Out Deadline**. The back-out deadline is the absolute point in time during the maintenance window beyond which work must halt and the plant must be restored to its baseline configuration, regardless of progress. If a six-hour maintenance window has a two-hour restoration sequence, the back-out deadline is reached precisely four hours into the window (T+4 h). If the new component is not fully commissioned by that minute, the technician must execute the back-out procedure. Never allow a contractor to negotiate for "just thirty more minutes" while the maintenance window expires.

## Technical Verification vs. Commercial Completion

A change is not closed when the vendor packs their toolboxes, hands over an invoice, and departs the security gate. A change is closed only when the facility manager completes rigorous technical verification against the baseline SLA:
- The modified equipment has been energized and operated under live thermal and electrical load for a minimum dwell period (typically 30 to 60 minutes).
- Telemetry confirms that operating temperatures, pressures, vibration signatures, and electrical phase balances match pre-change specifications.
- All alarms that were disabled or muted during the procedure have been re-enabled and functionally verified via loop testing.
- The Sequence of Events (SOE) recorder confirms that no unrecorded transient spikes or ground faults were introduced during switching.

If technical verification cannot be completed satisfactorily, the change is formally classified as **Paused with Active Defect**, an incident ticket is generated, and the system is placed under active continuous monitoring with an assigned engineer.

## Decisions to Record

- Full registry of today's executed changes, detailing old parameter values and new parameter values.
- Name and title of the formal risk acceptor for each change ticket.
- Exact start and close timestamps for each maintenance window.
- Recorded abnormal states posted on the control room board and shift handover.
- Formal technical verification signed off under live load conditions.

---

# 6. The Shift Inspection Round

Telemetry dashboards lie. A Building Management System (BMS) pressure transducer can drift out of calibration; an optical smoke detector can accumulate dust and report clear; an RTD temperature sensor can fail high and be clamped by a bad software filter.

The physical shift round is the ultimate verification that the physical reality of the data center matches the mathematical model in the control room.

```
+-----------------------------------------------------------------------------+
| SHIFT ROUND PHYSICAL INSPECTION TOPOLOGY |
| |
| [STATION 1] MV Substation & Switchgear (35kV/10kV Gas, Springs, Relays) |
| | |
| [STATION 2] Transformer Vaults (Winding Temps, Acoustic Hum, Lugs) |
| | |
| [STATION 3] UPS & Battery Rooms (DC Float Voltage, String Temps, Exhaust) |
| | |
| [STATION 4] Central Chiller Plant (Approach Temp, Oil Pressure, Head Press)|
| | |
| [STATION 5] Liquid CDU Stations (0.15-0.90 MPa, Refractometer, Catch Pan) |
| | |
| [STATION 6] AI Whitespace & NVL72 Racks (Thermal IR, Delta-P, FD83 Couplings)|
+-----------------------------------------------------------------------------+
```

![Shift Round Inspection Topology](../figures/fig-03-shift-round-inspection-topology.png)

A technician walking the round is not an errand runner checking boxes on a clipboard. A technician on the round is an active, multi-sensory diagnostic instrument.

## The Multi-Sensory Inspection Discipline

Every square meter of a production data center must be audited across four sensory channels:
1. **Visual**: Inspect equipment for fluid drips, staining, discoloration, rust, loose fasteners, bulging capacitors, blistered paint indicating extreme heat, and verify mechanical analog gauge needles against digital telemetry readings.
2. **Acoustic**: Listen for cavitation in pump volutes (sounds like pumping gravel), harmonic buzzing in transformers indicating loose laminations or core saturation, bearing squeal in fan motors, and whistling air leaks around aisle containment doors.
3. **Thermal**: Use calibrated handheld infrared (IR) cameras to sweep electrical busbar connections, circuit breaker terminals, cable lugs, and mechanical bearings. Any connection exhibiting a temperature > 70°C or a phase-to-phase differential ΔT > 10 K is an immediate Category 1 defect.
4. **Olfactory**: Sniff for the sharp, pungent scent of burning electrical insulation (ozone and overheated phenolic resin), the sweet odor of atomized propylene glycol from a micro-leak, or the sulfurous stench of an off-gassing lead-acid battery.

## The Six Critical Inspection Stations

Following the operational standards outlined in OpenViking (`ALZJ-YW-2.6XZ02` for IT Whitespace and `ALZJ-YW-2.6XZ10` for Liquid Cooling Infrastructure), the shift inspection round traverses six mandatory stations:

```
+-----------------------------------------------------------------------------+
| CRITICAL STATION INSPECTION METRICS |
| |
| Station / System Standard Parameter Rejection Threshold |
| ----------------------- ------------------------ ---------------------- |
| MV Switchgear SF6 Gas Pressure Nominal Low Pressure Alarm Trip |
| Transformers Winding Temp < 90°C Temp >= 110°C (Alarm) |
| UPS Battery Rooms Ambient Temp 20°C - 25°C Temp > 28°C / Swelling |
| Chiller Plant Condenser Approach <1.5K Approach >= 2.5 K |
| CDU Secondary Loop Pressure 0.15 - 0.90 MPa Pressure < 0.12 MPa |
| CDU Glycol Mix 25.0% PG (+/- 1.0%) PG < 23% or > 27% |
| IT Whitespace Aisles Underfloor DP >= 5.0 Pa DP < 2.5 Pa (Air Starve)|
| Liquid Racks (NVL72) FD83/UQD Couplings Dry Any Active Fluid Droplet|
+-----------------------------------------------------------------------------+
```

![CDU Shift Inspection Checklist](../figures/fig-05-liquid-cdu-shift-inspection-checklist.png)

### Station 1: Medium-Voltage Substation & Switchgear
- Inspect 35kV and 10kV circuit breaker spring charge indicators (verify charged state).
- Check SF6 gas pressure indicators on gas-insulated switchgear (GIS); ensure needles sit securely in the green zone.
- Verify DC control bus battery charger voltage (125 VDC ± 2%) and ensure zero ground-fault alarms exist on the ungrounded DC control system.

### Station 2: Transformer Vaults
- Verify digital winding temperature indicators on dry-type transformers (normal operating range: 60°C - 85°C; alarm threshold at 110°C; automatic trip at 130°C).
- Inspect forced-air cooling fans for physical obstruction and bearing vibration.
- Check oil-filled transformers for tank oil level, silica gel desiccant color (deep blue; pink indicates moisture saturation requiring immediate replacement), and inspect tank seams for weeping oil.

### Station 3: UPS & Battery Rooms
- Record DC bus float voltages and battery charging currents across all static UPS modules.
- Audit battery room ambient temperature (maintain strictly between 20°C and 25°C; lead-acid battery design life degrades by 50% for every 8 K rise above 25°C).
- Visually inspect individual VRLA battery jars for case bulging, terminal post corrosion, or electrolyte leaking; for lithium-ion systems, verify that the Battery Management System (BMS) reports zero cell voltage imbalances (> 50 mV).
- Confirm hydrogen exhaust fan operation by feeling airflow at the intake louvers.

### Station 4: Central Chiller & Pumping Plant
- Audit chiller operating logs: verify that condenser water approach temperature is ≤ 1.5 K (ΔT_approach = T_cond, leaving - T_tower, entering). An approach temperature > 2.5 K indicates severe tube fouling or scaling requiring chemical brushing.
- Check compressor oil levels, oil pressures, and oil return temperatures.
- Audit chilled water pump differential pressures (ΔP) and verify that secondary variable speed drives are modulating correctly without hunting.

### Station 5: Secondary Cooling Distribution Units (CDU)
Per OpenViking `ALZJ-YW-2.6XZ10`, the CDU is the mechanical heart of high-density AI clusters:
- **Pressure Envelope**: Verify primary facility water system (FWS) supply pressure and secondary technology cooling system (TCS) supply pressure remain strictly between 0.15 MPa and 0.90 MPa. Verify that pump differential pressure is < 1.0 bar.
- **Thermal Performance**: Verify that plate heat exchanger approach temperature (ΔT_approach = T_TCS, supply - T_FWS, supply) does not exceed 8.0 K. An approach > 8.0 K indicates biological fouling or particulate clogging on the plate surfaces.
- **Fluid Chemistry**: Use a calibrated optical refractometer to test secondary coolant. Propylene glycol concentration must measure precisely **25.0% by weight** (± 1.0%), providing freeze protection down to -11.5°C and burst protection down to -22.0°C. Coolant conductivity must measure < 10 μ S/ cm, with pH maintained between 7.5 and 9.0.
- **Physical Integrity**: Inspect the internal CDU catch pan and base frame for moisture. Verify that the continuous rope leak detection sensor is completely dry and properly positioned. Check the nitrogen pre-charge pressure on the thermal expansion tank (P_0 = P_fill - 0.2 bar).

### Station 6: AI Whitespace & NVL72 Racks
Per OpenViking `ALZJ-YW-2.6XZ02`:
- **Electrical Distribution**: Inspect remote power panels (RPPs) and power distribution units (PDUs). Sweep circuit breakers and terminal lugs with an infrared camera to detect loose terminations.
- **Airflow Containment**: Audit cold aisle containment (CAC) or hot aisle containment (HAC). Verify that differential pressure across the raised floor or containment barrier remains ≥ 5.0 Pa. Verify that all unpopulated rack units contain blanking panels; a single missing 1U panel permits 25 L/s of air bypass, creating localized hot spots.
- **Liquid Cooling Manifolds & Couplings**: Audit rack-level vertical distribution manifolds. Inspect all quick-disconnect couplings (Danfoss FD83 or Universal Quick Disconnects) serving compute trays and NVLink switch trays. Any sign of fluid weeping, crusting, or drop formation is an immediate Stop Work condition requiring tray isolation. Check that drip trays under the rack manifolds are clean and dry.

## The Immediate Defect Entry Rule

If you discover a defect during the shift round, it must be entered into the site computerized maintenance management system (CMMS) or physical defect register **before you leave the room**.

Taking a photograph on a personal mobile phone with the intention of logging the issue at the end of the shift is unacceptable:
- A defect entered into the register has a physical timestamp, an asset ID, a priority classification, and an assigned owner.
- A photograph on a smartphone is an unmanaged private note that is forgotten when an alarm sounds thirty minutes later.

If the defect impairs equipment redundancy or causes operating parameters to cross an SLA threshold, the shift round halts immediately, the duty manager is notified via radio, and an incident ticket is generated on the spot. Never complete the round and casually mention a leaking CDU pump during lunch.

## Decisions to Record

- Physical inspection route completed, with start and completion timestamps and technician signatures.
- Specific operating parameters logged at all six inspection stations.
- Handheld refractometer, conductivity, and pH measurements logged for the secondary cooling loop.
- All defects entered into the formal site register prior to exiting each room, or an explicit statement of zero defects found.

---

# 7. Vendors and Contractors

A third-party vendor or equipment manufacturer technician working inside your data center is a pair of hands operating under your legal permit. They are not an autonomous entity that you can leave unsupervised in an electrical vault.

```
+-----------------------------------------------------------------------------+
| VENDOR GOVERNANCE GATEWAY |
| |
| [GATE 1] Pre-Arrival Scope: Specific task, approved MOP, tool registry |
| | |
| [GATE 2] Security & Safety In-Brief: Badge issued, LOTO verified, PPE audit |
| | |
| [GATE 3] Active Escort: Qualified site technician assigned; never unescorted|
| | |
| [GATE 4] Scope Boundary Enforcement: Stop Work if task leaves written MOP |
| | |
| [GATE 5] Technical Closeout: Physical audit of work, old parts, site clean |
| | |
| [GATE 6] Commercial Separation: Technical sign-off != Commercial invoice |
+-----------------------------------------------------------------------------+
```

A manager who signs a visitor badge, points toward the battery room, and returns to their office has abandoned control of the facility. If that vendor drops a ratchet across a 480V busbar or opens the wrong isolation valve, the outage belongs to the manager, not the vendor.

## Pre-Arrival Scope Definition

Before a vendor crosses the security turnstile, their operational scope must be defined in writing with unambiguous boundaries:
- Exactly which equipment tag they are authorized to touch (e.g., *"Centrifugal Chiller CH-02 compressor oil filter assembly only"*).
- Exactly which equipment they are strictly prohibited from touching (e.g., *"Do not touch condenser water isolation valves or adjacent chiller CH-01 control panel"*).
- The definition of "Done": What specific physical tests, pressure readings, or operational milestones must be verified before the equipment is considered repaired.
- Deliverables required before departure: Factory field service report, calibrated tool test logs, serial numbers of all installed replacement components, and physical surrender of all failed parts for root-cause analysis.

A vendor work order that reads *"Annual preventive maintenance on UPS system"* is an invitation to disaster. It specifies no boundaries, no test limits, and no operational constraints. If the vendor does not provide an itemized, step-by-step MOP seventy-two hours in advance, cancel the site visit.

## The Dedicated Site Host

Every vendor working within critical electrical, mechanical, or whitespace areas must be accompanied by a dedicated, qualified site host from your operational shift team.

The site host does not perform the vendor's physical labor. The host's duties are:
1. **Scope Boundary Enforcement**: Continuously observe the vendor's actions. If the technician reaches toward an adjacent switchgear cubicle or begins opening a valve not listed in the MOP, the host immediately commands Stop Work.
2. **Emergency Reaction**: In the event of an arc-flash, chemical splash, or equipment trip, the host initiates the site Emergency Operating Procedure (EOP), summons medical support, and directs the safe-state isolation.
3. **Escort Control**: Ensure the vendor remains within the authorized physical work envelope and never wanders through production aisles unsupervised.

### Eliminating Casual Scope Creep ("While We're Here")

The most dangerous words in data center operations are a vendor technician saying:
> *"While we have the panel cover off, do you want me to quickly adjust the sensitivity setting on this ground-fault relay?"*

The answer is always an uncompromising **"No."**

A useful task discovered with the equipment open is not a helpful favor; it is an unreviewed, unpermitted engineering change:
- It possesses no approved MOP.
- It has undergone no Change Advisory Board risk assessment.
- It has no calculated back-out plan.
- The control room has not logged the plant into an abnormal operating state.

If the vendor identifies an unexpected defect or recommended adjustment during their work, log the finding into the site defect register. It will be scheduled, reviewed, and executed during a future authorized maintenance window under its own permit. Never allow spontaneous scope creep in a live facility.

## Technical Acceptance vs. Commercial Invoicing

Never allow the commercial urgency of a vendor's billing cycle to compromise technical acceptance.

Technical acceptance is a rigorous engineering verification that the equipment has been restored to full operational capability:
- The equipment has operated under full thermal or electrical load without abnormal vibration, temperature excursions, or fluid leakage.
- All digital communication channels (Modbus, BACnet, SNMP) between the equipment and the central BMS/EPMS have been re-established and verified.
- The work area has been cleaned, all debris, loose zip ties, and wire clippings removed, and all physical panel covers, dead-front shields, and safety interlocks re-installed.
- All old, failed components (burned contactors, worn mechanical seals, degraded capacitors) have been tagged, boxed, and transferred to the site quarantine storage room for forensic inspection.

The document you sign at the end of the vendor's visit is exclusively a **Field Service Verification of Work Performed**. It verifies that the vendor was on site and performed the numbered steps in the MOP.

It does not constitute commercial acceptance of the invoice, and it does not waive the facility owner's right to pursue warranty claims if latent defects emerge during subsequent operations. If commercial representatives press you to sign an unconditional commercial completion certificate before functional load testing is complete, note on the sheet: *"Work performed visually verified; functional technical acceptance pending 24-hour live load dwell."*

## Decisions to Record

- Pre-approved vendor scope of work and attached MOP registry number.
- Name of the dedicated on-shift site host assigned to the vendor.
- Scope boundary check: Confirmed zero deviation from written MOP, or recorded Stop Work command.
- Technical acceptance signed only after physical inspection and live load dwell verification.
- Serial numbers of installed components and quarantine bin location of failed parts.

---

# 8. When It Fails

An incident is any event where critical infrastructure fails to deliver the contractual service envelope, where a human life is endangered, or where the facility enters an unstable state that will imminently cause either outcome.

```
+-----------------------------------------------------------------------------+
| INCIDENT ESCALATION TIMELINE |
| |
| [T = 00:00] EVENT DISCOVERY (Telemetry trip, acoustic alarm, visual) |
| | |
| [T + 02:00] STOP & ASSESS: Silence horn; identify failing subsystem |
| | |
| [T + 05:00] EXECUTE EOP: Stabilize nearest safe state; isolate hazard |
| | |
| [T + 10:00] SUMMON INCIDENT COMMAND: Establish incident log; assign roles |
| | |
| [T + 15:00] CLIENT SLA NOTIFICATION: Send factual notice (NO HYPOTHESES) |
| | |
| [T + 60:00] TECHNICAL CONTAINMENT: Deploy MOP repairs; continuous updates|
| | |
| [POST-EVENT] ROOT CAUSE ANALYSIS (RCA): Fishbone, 5-Whys, 1 owned action |
+-----------------------------------------------------------------------------+
```

![Incident Escalation and SLA Timeline](../figures/fig-06-incident-escalation-and-sla-timeline.png)

A noisy alarm that does not threaten service delivery or human safety is an annoyance. Do not elevate it to an emergency. Conversely, never downgrade a genuine service degradation because the equipment room appears quiet and calm. The sole metric of an incident is service delivery and personnel safety.

## The Incident Severity Classification

Every abnormal event must be classified into one of three strict severity tiers within two minutes of discovery:

```
+-----------------------------------------------------------------------------+
| INCIDENT SEVERITY CLASSIFICATION |
| |
| Tier Classification Operational Impact Client Notification |
| ---- -------------- ----------------------------- ------------------- |
| P1 Critical Total loss of power or cooling <= 15 Min; Hourly Upd |
| to IT load; human life safety |
| P2 Major Loss of system redundancy <= 30 Min; 2-Hour Upd |
| (N-1 state); high temp warning |
| P3 Minor Single component failure with Shift Summary Log |
| zero redundancy impact |
+-----------------------------------------------------------------------------+
```

## The First Hour: The Incident Clock

During a live incident, human memory degrades rapidly under adrenaline. Technicians remember actions out of sequence; managers compress twenty minutes of hesitation into five minutes of remembered decisiveness.

The duty manager must open an immutable, time-stamped **Incident Chronology Log** at the exact minute the event begins:

```
+-------------------------------------------------------------------------+
| INCIDENT CHRONOLOGY LOG |
| |
| [09:14:22] EPMS reports Breaker B-SWG-02 instantaneous trip on feeder B|
| [09:16:00] Duty Manager initiates EOP-E-04 (Loss of 2N Feeder B) |
| [09:18:45] Technician Chen confirms Bus A carrying 82% total load |
| [09:21:10] Safe State 1 reached: IT load stable on single feed |
| [09:24:00] Client SLA Notice 1 transmitted via portal (T+10 min) |
| [09:32:00] Infrared scan of Bus A switchgear shows 58°C; stable |
| [09:45:00] Switchgear vendor called; ticket #84920 opened |
+-------------------------------------------------------------------------+
```

Log every event with exact timestamps:
- The minute the alarm was detected on the monitoring console.
- Exactly what was observed on the physical instruments, not what someone assumed happened.
- The exact EOP executed, the safe state achieved, and the minute that state was confirmed.
- The names of all individuals summoned to the incident team.
- The minute the client notification was transmitted, and the exact text sent.
- What actions were intentionally rejected or deferred to protect the remaining live systems.

## Muscle Memory Safe State vs. Heroic Troubleshooting

When alarms sound and equipment trips, an untrained technician's instinctive reaction is to start flipping switches, resetting tripped breakers, or opening bypass valves in a desperate attempt to restore the offline unit.

This "heroic troubleshooting" is how a minor single-component trip escalates into a catastrophic full-facility blackout:
- A circuit breaker that tripped on instantaneous overcurrent may have cleared a catastrophic phase-to-phase dead short. Resetting that breaker without testing will cause an explosive arc-flash that destroys the entire switchgear line-up.
- A secondary CDU pump that tripped on low suction pressure may indicate an empty expansion tank or a burst pipe. Forcing the standby pump to start without investigating will run the mechanical seal dry and burn out the motor.

The absolute operational rule during an incident is:
1. **Execute the Emergency Operating Procedure (EOP)** to establish the nearest pre-engineered Safe State.
2. **Stop**. Take your hands off the controls.
3. Verify that surviving redundant systems are carrying the load stably.
4. Begin systematic forensic investigation under an approved MOP.

The hero who attempts to repair live equipment while sirens are wailing belongs in an action movie, not an industrial data center. In an industrial data center, we value the disciplined technician who stabilizes the plant, stands back, and adheres to procedure.

## Keeping Hypotheses Off the First Client Notice

When drafting the initial incident notification to the customer, follow this rigid rule: **Report only confirmed physical facts; keep hypotheses completely off the notification.**

```
+-------------------------------------------------------------------------+
| CLIENT NOTIFICATION DISCIPLINE |
| |
| [PERMITTED FACTUAL NOTICE] |
| "At 09:14 UTC, Electrical Feeder B experienced an automatic trip. |
| All critical IT whitespace remains fully powered via redundant |
| Feeder A. The facility is currently operating in an N-1 state. |
| Operations teams are investigating the cause of the Feeder B trip. |
| The next formal update will be provided at 10:15 UTC." |
| |
| [PROHIBITED SPECULATIVE NOTICE] |
| "We think a contractor bumped a relay on Feeder B, or maybe the |
| utility had a lightning strike down the road. We are resetting the |
| breaker now and hope to have it back in ten minutes." |
+-------------------------------------------------------------------------+
```

If you transmit a speculative theory in your first notice and subsequent engineering forensics prove that theory wrong:
- You destroy the customer's trust in your operational competence.
- You provide the customer's legal team with ammunition to claim gross negligence.
- You force your team to spend hours explaining why the initial story changed instead of focusing on technical restoration.

State the symptom, the timestamp, the affected systems, the current containment state, and the time of the next update. Say nothing else.

## The Single Owned Action (Post-Incident RCA)

An incident is not closed when the equipment is re-energized and the alarms clear. An incident is closed only when a formal Root Cause Analysis (RCA) is conducted and results in **one concrete, owned, dated operational change**.

A post-incident review meeting where managers gather to commiserate, retell their anxiety, and conclude that *"technicians need to be more careful"* is an utter waste of time. "Being more careful" is not an engineering control.

An authentic post-incident corrective action changes:
- An engineering design (e.g., install interposing isolation relays to eliminate common-mode trip circuits).
- A maintenance procedure (e.g., revise MOP to mandate dual torque checks on 480V cable lugs).
- An inspection round (e.g., add daily refractometer sampling to the CDU shift checklist).
- A physical tool or spare (e.g., procure calibrated vacuum filling skids to eliminate air binding in cooling loops).

The corrective action must have a single named owner and a binding completion deadline. If the post-incident review proposes five diffuse recommendations, none of them will be implemented. Select the single most impactful structural fix, assign it to an owner, and track it to completion on the daily handover log.

## Decisions to Record

- Incident classification (P1 / P2 / P3) and exact discovery timestamp.
- Chronology log detailing all actions, safe states reached, and personnel involved.
- Copy of the initial client notification, verifying zero speculative hypotheses were included.
- Technical restoration confirmation signed under steady-state load conditions.
- The single owned, dated corrective action resulting from the Root Cause Analysis.

---

# 9. Capacity, Without an Invented Number

A facility manager's daily capacity duty is governed by three fundamental questions:
1. What capacity did you contractually sell to the customer?
2. What capacity is physically utilized at this exact moment?
3. What capacity will survive if your largest single component fails right now?

```
+-----------------------------------------------------------------------------+
| THE 2N CAPACITY REDUNDANCY CEILING |
| |
| 100% +----------------------------------------------------------------+ |
| | UNUSABLE DANGER ZONE | |
| | If Bus A trips, Bus B instantly overloads and blackouts | |
| 90% +================================================================+ |
| | MAXIMUM SURVIVING LOAD (90%) | |
| | | |
| 50% + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -+ |
| | THE 45% RULE: MAXIMUM STEADY-STATE PERMITTED | |
| 45% +----------------------------------------------------------------+ |
| | | |
| | SAFE 2N OPERATING ENVELOPE | |
| | Bus A Load <= 45% | Bus B Load <= 45% | |
| 0 +----------------------------------------------------------------+ |
+-----------------------------------------------------------------------------+
```

![2N Power Redundancy Ceiling](../figures/fig-04-2n-power-capacity-and-redundancy-ceiling.png)

If you cannot answer those three questions with mathematical certainty from verified metering records, you do not know whether today's proposed maintenance or server deployment is safe.

## The Mathematics of 2N Redundancy: The 45% Rule

The most widespread and deadly operational myth in data center management is the belief that in a 2N redundant electrical architecture, each power path can be safely operated up to **50% of its rated nameplate capacity**.

This is a mathematical trap that has caused catastrophic multi-megawatt cascade outages across the industry:

$$P_{\text{total}} = P_{\text{Bus A}} + P_{\text{Bus B}}$$

Consider a 2N electrical busbar rated for 2000 kVA. The operations manager observes that Bus A is carrying 1040 kVA (52% load) and Bus B is carrying 1020 kVA (51% load). The manager assumes that because neither busbar is overloaded, the system is operating comfortably within its safety margin.

Now, an upstream transformer feeding Bus A trips.
Within milliseconds, all dual-corded IT server power supplies attached to Bus A transfer their electrical load onto Bus B.

The total instantaneous load imposed on Bus B becomes:

$$P_{\text{Bus B, transient}} = 1040\,\text{kVA} + 1020\,\text{kVA} = 2060\,\text{kVA} \quad (103\% \text{ of rated capacity})$$

Bus B is instantly overloaded. The main circuit breaker for Bus B senses sustained overcurrent and trips after a brief time-delay curve, plunging the entire data hall into total darkness. A facility designed for complete 2N fault tolerance experienced a 100% catastrophic blackout from a single component failure.

To prevent cascade tripping, every 2N electrical distribution path must adhere strictly to **The 45% Loading Rule**:

$$P_{\text{steady-state}} \le 0.45  \times P_{\text{rated}}$$

Under the 45% rule:
- Bus A carries ≤ 45% (900 kVA).
- Bus B carries ≤ 45% (900 kVA).
- If Bus A trips, the surviving Bus B inherits a total load of 900 + 900 = 1800 kVA (90% of rated capacity).
- Bus B operates stably with a 10% safety buffer, well below the thermal-magnetic trip threshold, allowing technicians to manage the contingency safely.

Any shift manager who permits a 2N electrical busbar to exceed 45% steady-state utilization has compromised the facility's redundancy and is operating in an unrated, high-risk state.

## Secondary Cooling Loop Hydraulic Capacity

In liquid-cooled AI whitespace housing high-density compute racks (such as NVIDIA NVL72 architectures consuming up to 132 kW per rack), hydraulic capacity governance is as vital as electrical capacity:

```
+-----------------------------------------------------------------------------+
| CDU HYDRAULIC CAPACITY CEILING |
| |
| Parameter Rated Design Limit Operational Redundancy Limit |
| ------------------ ------------------------ --------------------------- |
| Total Heat Removal 1200 kW per CDU <= 1000 kW (83% of PHE cap) |
| Secondary Flow Rate 1440 LPM (24 LPS) <= 1200 LPM (Single Pump N) |
| Supply Temperature 25.0°C - 32.0°C (W3/W4) <= 30.0°C (At Max Ambient) |
| Pump Configuration N+1 Dual VFD Pumps 1 Pump Run / 1 Standby Auto |
| Loop Pressure 0.15 - 0.90 MPa Head Loss Delta-P < 1.0 bar |
+-----------------------------------------------------------------------------+
```

When evaluating a customer's request to install additional high-density liquid-cooled racks, the duty manager must evaluate hydraulic constraints:
1. **Total Flow Availability**: Verify that the secondary pumps can deliver the required volumetric flow rate (q_v) to maintain cold plate turbulent flow:

$$q_v = \frac{Q}{\rho \cdot c_p \cdot \Delta T}$$

Where:
- Q is the total thermal heat dissipation ( kW).
- $
- ρ is the density of 25% propylene glycol (1026\, kg/m^3at30°C$).
- c_p is the specific heat capacity (3.92 kJ/( kg· K)).
- ΔT is the fluid temperature rise across the rack manifold (typically 10.0 K).

2. **Hydraulic Imbalance and Direct-Return Starvation**: As additional racks are connected to a secondary distribution manifold, friction losses (ΔP_f) increase quadratically with flow velocity (v):

$$\Delta P_f = f \cdot \frac{L}{D} \cdot \frac{\rho v^2}{2}$$

If the manifold was plumbed in a direct-return configuration rather than a reverse-return (Tichelmann) loop, adding load to the far end of the row will starve the index rack, causing immediate thermal throttling on the GPUs.

Never approve a liquid load addition based on a verbal assurance from the customer that "the pumps look big enough." Demand the certified hydraulic flow simulation and pressure drop calculations before issuing a connection permit.

## The Myth of "Trying" the Load

When a customer or project installation team requests permission to energize additional server racks that exceed the calculated capacity envelope, they will often suggest:
> *"Let's just energize the racks and watch the meters for twenty minutes to see if the breakers hold."*

This is the operational equivalent of testing the thickness of ice by driving a thirty-ton truck onto it.

Energizing equipment "to see if it holds":
- Subjects electrical busbars and transformers to massive inrush currents and thermal shock.
- Risks tripping upstream protective relays, triggering an instantaneous outage for adjacent live customers.
- Replaces rigorous mathematical engineering with reckless gambling.

If a requested load deployment exceeds either the contractual allocation or the 45% redundancy ceiling, the Duty Manager must refuse authorization immediately. Halt the energization. The customer must submit a formal engineering study and negotiate an amended contract before a single additional circuit breaker is closed.

## Decisions to Record

- Contractual capacity sold, cited by customer contract clause and rack ID.
- Active electrical load recorded per busbar, verifying compliance with the 45% redundancy rule.
- Hydraulic secondary loop flow rate, supply temperature, and differential pressure logged per CDU.
- Remaining capacity after a single worst-case component failure: verified via named engineering study, or recorded as unknown.
- Any request exceeding safe operational capacity rejected in writing; zero energization "to try."

---

# 10. The Master Day Sheet

The Master Day Sheet is the binding legal, technical, and operational ledger of the data center shift.

```
+-----------------------------------------------------------------------------+
| MASTER DAY SHEET STRUCTURE |
| |
| [SECTION 1] Pre-Shift Turnover Audit (Impairments, Permits, Incidents, MOP)|
| | |
| [SECTION 2] Authorized Work & PTW Registry (Scope, LOTO, Expiration Clocks)|
| | |
| [SECTION 3] Physical Shift Round Log (6 Stations, Multi-Sensory Parameters)|
| | |
| [SECTION 4] Incident & Escalation Chronology (Classification, T-15 SLA) |
| | |
| [SECTION 5] Capacity & Redundancy Audit (45% Power Rule, CDU Hydraulics) |
| | |
| [SECTION 6] The Final Closeout Sentence (The single immutable signature) |
+-----------------------------------------------------------------------------+
```

![Manager Shift Closeout Sheet](../figures/fig-07-manager-shift-closeout-sheet.png)

Copy the headings below into your facility's operational software or printed turnover logbook. A blank line on the Day Sheet represents a part of the facility you did not inspect, a risk you did not manage, and an outage you will own.

---

## 1. Before the Shift (Handover Gate)

- **Shift Date & Time Window**: `________________________________________`
- **Duty Manager On Duty**: `___________________________________________`
- **Outgoing Duty Manager**: `_________________________________________`
- **Contractual SLA Standard Operating To**: `__________________________`
- **Notice Period for SLA Excursions**: `_____ Minutes`
- **What Operations Will Explicitly NOT Promise Today**: `_______________`
- **On-Shift Personnel & Verified Trade Qualifications**:
 - Lead Electrician (License # & Expiration): `_________________________`
 - Cooling Specialist (License # & Expiration): `______________________`
 - Shift Technicians on Duty: `________________________________________`
- **Tasks / Systems Not Covered by Today's Roster**: `___________________`
- **Handover from Previous Shift Read, Walked, and Accepted**: `[YES / NO]`
- **Active Impairments Carried In**:
 - Fire Suppression (VESDA / Gas Disarmed): `__________________________`
 - Electrical Redundancy Impairments (Bypass / N-0): `__________________`
 - Mechanical Redundancy Impairments (Manual VFD / Single Pump): `______`
- **Open Permits to Work (PTW) Carried In & Expiration Times**: `________`
- **Active Incidents Carried In & Assigned Technical Owners**: `__________`
- **Scheduled Changes for Today's Window & Named Risk Acceptors**: `______`

---

## 2. Authorized Work & Maintenance

- **Standing Shift Routines (SOPs) Completed**: `[YES / NO]`
- **Specific Intrusive Jobs Executed (Approved MOPs Only)**:
 - Job 1: Tag: `_________` Scope: `___________________` MOP #: `_______`
 - Job 2: Tag: `_________` Scope: `___________________` MOP #: `_______`
- **Permits Issued Today & Exact Expiration Timestamps**:
 - PTW #: `_________` Location: `____________` Closes at: `___________`
- **LOTO Zero-Energy Verification Completed (Lock IDs)**: `______________`
- **Critical Spares Inspected at Worksite Prior to Tool Touch**: `[YES / NO]`
- **Changes Executed Today**:
 - Asset ID: `____________` Old Parameter: `_________` New: `___________`
 - Risk Acceptor Name: `__________________` CAB Approval #: `___________`
 - Back-Out Plan Verified Prior to Window: `[YES / NO]`
- **Abnormal Operating State Displayed on Control Room Board**: `[YES / NO]`
- **Third-Party Vendors on Site**:
 - Vendor Name: `______________` Assigned Site Host: `__________________`
 - Work Kept Strictly Within Written Scope: `[YES / NO]`

---

## 3. Physical Shift Inspection Round

- **Inspection Round Route Walked**: `Station 1 through Station 6 Completed`
- **Round Start Time**: `________` **Completion Time**: `________`
- **Technician Name**: `________________________________________________`
- **Station 1 (MV Switchgear)**: SF6 Pressure Normal `[Y/N]` | Springs Charged `[Y/N]` | DC Bus Voltage: `____ V`
- **Station 2 (Transformers)**: Winding Max Temp: `____ °C` | Acoustic Normal `[Y/N]` | Oil Level: `____`
- **Station 3 (UPS & Battery)**: Ambient Temp: `____ °C` | DC Float: `____ V` | Zero Bulging / Leaks `[Y/N]`
- **Station 4 (Chiller Plant)**: Approach Temp: `____ K` | Oil Press: `____ bar` | VFD Vibration Normal `[Y/N]`
- **Station 5 (CDU Stations)**: TCS Supply Press: `____ MPa` | Glycol Refractometer: `____ % PG` | Catch Pans Dry `[Y/N]`
- **Station 6 (AI Whitespace)**: Containment DP: `____ Pa` | Max PDU IR Temp: `____ °C` | Couplings Dry `[Y/N]`
- **Defects Entered on Formal CMMS Register Before Exiting Rooms**: `[YES / NONE]`
- **Contractual SLA Maintained During Round**: `[YES / NO]`

---

## 4. Incident & Escalation Log

- **Incident Status**: `[NONE / ALARM ONLY / ACTIVE INCIDENT]`
- **Severity Classification**: `[P1 - CRITICAL / P2 - MAJOR / P3 - MINOR]`
- **Discovery Timestamp**: `HH:MM:SS UTC`
- **Observed Physical Symptoms (Facts Only)**: `__________________________`
- **EOP Executed & Safe State Achieved Timestamp**: `HH:MM:SS UTC`
- **Client Notification Transmitted Timestamp**: `HH:MM:SS UTC (<= 15 min)`
- **Confirmation: Hypotheses Kept Off Client Notice**: `[YES / NO]`
- **Incident Resolved or Carried Forward**: `[RESOLVED / CARRIED FORWARD]`
- **Single Owned Corrective Action Resulting from Event**: `______________`
 - Action Owner: `_____________________` Due Date: `____________________`

---

## 5. Capacity & Redundancy Governance

- **Contractual Power Sold**: `_______ kW` (Clause: `____________________`)
- **Active Power Utilized**: `_______ kW` (Revenue Meter Timestamp: `_____`)
- **2N Redundancy Rule Audit**:
 - Feeder / Bus A Utilization: `_______ %` (Must be <= 45.0%)
 - Feeder / Bus B Utilization: `_______ %` (Must be <= 45.0%)
- **Secondary Cooling Hydraulic Utilization**:
 - CDU Thermal Load: `_______ kW` (Must be <= 83% of PHE rating)
 - Secondary Flow Rate: `_______ LPM` | Supply Temp: `_______ °C`
- **Remaining Capacity After Worst-Case Single Failure**:
 - Calculated Value: `_______ kW` (Engineering Study Date: `___________`)
 - Status: `[VERIFIED BY STUDY / UNKNOWN]`
- **Unverified Load Energization Requests Rejected**: `[YES / NONE]`

---

## 6. End-of-Shift Closeout & Sign-Off

- **All Maintenance Windows Closed or Paused with Named Owner**: `[YES / NO]`
- **Abnormal Operating States Cleared from Control Room Board**: `[YES / NO]`
- **Handover Dossier Prepared for Incoming Shift**: `[YES / NO]`
- **The Single Binding Sentence You Can Honestly Sign**:
 > *"I certify on my professional license that during this shift, all critical power and cooling systems operated within contractual SLA boundaries, all work was executed under approved procedures without unrecorded impairments, and all logged defects possess named owners."*

- **Duty Manager Signature**: `__________________________________________`
- **License / Certification Number**: `_________________________________`
- **Date & Exact Timestamp**: `_________________________________________`

---

# 11. What This Book Does Not Own

A field guide that pretends to own the entire universe of data center engineering and legal governance is a danger to its readers. Operational clarity requires drawing rigid boundaries around what this book owns and what belongs to other authorities.

## It Does Not Own a Certification Course

This book does not grant you a credential.
Certified Data Centre Facilities Operations Manager (CDFOM), Certified Data Centre Facilities Operations Specialist (CDCS), and Certified Data Centre Sustainability Professional (CDCSP) are proprietary course titles owned by professional certification bodies (such as EPI and Uptime Institute).

Nothing in this book is an official curriculum, an authorized training manual, or an exam cheat sheet for those programs. If your client's master services contract mandates that the facility manager hold a specific certification, sit the formal course, pass the proctored examination, and pay the licensing fee to the issuing organization. A dog-eared paperback field guide on your desk will not satisfy an ISO auditor or a client procurement panel.

## It Does Not Own Standards, Codes, or Libraries

This book cites international standards, safety codes, and service-management frameworks by title, edition, and year. It deliberately does not reproduce their copyrighted clauses, annexes, or calculation tables:
- **NFPA 70E (Standard for Electrical Safety in the Workplace)** governs your arc-flash boundaries, PPE categories, and energized electrical work permits.
- **OSHA 29 CFR 1910.147** governs your physical Lockout/Tagout (LOTO) legal obligations.
- **ASHRAE TC 9.9** establishes thermal envelopes (Classes A1 to A4 for air cooling; Classes W1 to W5 for liquid cooling). ASHRAE has explicitly stated that its technical publication content is protected under copyright law and may not be digested, ingested, or transformed into AI derivative works without formal written authorization.
- **ISO/IEC 20000 and ITIL** govern service management, change management, and configuration databases.

Purchase official, licensed copies of these standards from their respective publishers (ANSI, NFPA, ASHRAE, ISO). Keep them in the site engineering library. Cite their clauses by exact number on your MOPs and incident reports. Never copy and paste copyrighted standard text into a public document and claim it as your site's private creation.

## It Does Not Own the Customer's Business

This book does not own:
- Your customer's application architecture, disaster recovery failover automation, or internal server telemetry.
- Your facility's architectural construction drawings, structural floor-loading calculations, or municipal zoning permits.
- The contractual lease price per kilowatt, utility tariff structures, or commercial power purchase agreements (PPAs).

Those documents belong exclusively to the client, the design engineering firm, and the commercial real estate entity. They reside in secure site archives, protected by non-disclosure agreements. Operations touches them only to verify physical interface boundaries and contractual SLA delivery limits.

## It Does Not Own Physical Testing or Computational Modeling

The earlier books in this field guide series own the physical machines, the data streams, the commissioning tests, and the computational airflow models:
- If you need to build and calibrate a high-density liquid load bank for NVL72 testing, open **Book 01**.
- If you need to analyze transient temperature spikes, flow rates, and flash reports, open **Book 02**.
- If you need to execute a full seven-sheet commissioning verification from Level 1 to Level 5, open **Book 03**.
- If you need to audit an engineering CFD report against physical multi-point anemometer readings, open **Book 04**.

This book begins when physical commissioning is complete and commercial operations are live. Operations may schedule future load-bank tests or commission CFD audits when plant configurations change, but operations may never substitute a daily guess or an unverified feeling for a certified physical measurement.

## Decisions to Record

- The professional credentials you and your shift personnel still need to obtain from accredited training bodies.
- The official standards and codes cited in today's MOPs, referenced by publisher, title, and edition.
- The physical engineering boundaries between facility infrastructure and client-owned IT hardware.

---

# 12. Titles, Standards, and the Copyright Line

A professional operations team cites its sources with exact academic and legal rigor. We operate to published, peer-reviewed engineering standards, statutory safety codes, and binding commercial agreements.

## Authoritative Engineering Standards & Codes

When drafting Methods of Procedure (MOP), Emergency Operating Procedures (EOP), or contractual SLA delivery reports, cite these authoritative titles directly:

1. **Electrical Safety and Installation**:
 - **NFPA 70E (2024 Edition)**: *Standard for Electrical Safety in the Workplace*. Governs energized electrical work permits, arc-flash risk assessments, approach boundaries, and PPE categories.
 - **NFPA 70 (2023 Edition)**: *National Electrical Code (NEC)*. Governs overcurrent protection, grounding, bonding, and critical operations power systems (COPS, Article 708).
 - **IEEE Standard 1584-2018**: *IEEE Guide for Performing Arc-Flash Hazard Calculations*. Governs incident energy calculations and boundary modeling.
 - **OSHA 29 CFR 1910.147**: *The Control of Hazardous Energy (Lockout/Tagout)*. Federal statutory requirements for zero-energy isolation verification.

2. **Thermal and Environmental Guidelines**:
 - **ASHRAE TC 9.9 (Fifth Edition, 2021)**: *Thermal Guidelines for Data Processing Environments*. Establishes recommended and allowable environmental envelopes for air-cooled equipment (Classes A1–A4) and liquid-cooled hardware (Classes W1–W5 / W27–W45).
 - **ASHRAE Standard 90.4-2022**: *Energy Standard for Data Centers*. Establishes mechanical and electrical energy efficiency performance minimums (Mechanical Load Component and Electrical Loss Component).

3. **Facility Operational Reliability and Sustainability**:
 - **Uptime Institute Tier Standard**: *Operational Sustainability (2020 Edition)*. Defines operational behaviors, maintenance management, staffing levels, and risk mitigation across Tier I through Tier IV topologies.
 - **TIA-942-B (2017 / Addendum 2020)**: *Telecommunications Infrastructure Standard for Data Centers*. Governs architectural, electrical, mechanical, and physical security redundancy levels (Rated 1 to Rated 4).

4. **Service Management and Business Continuity**:
 - **ISO/IEC 20000-1:2018**: *Information technology — Service management — Part 1: Service management system requirements*. Governs formal change management, incident handling, and service delivery.
 - **ISO 22301:2019**: *Security and resilience — Business continuity management systems — Requirements*. Framework for operational disaster recovery and incident escalation.
 - **ISO 55001:2014**: *Asset management — Management systems — Requirements*. Systematic lifecycle governance of critical physical infrastructure assets.

5. **Operational Guidelines (OpenViking Repository)**:
 - **ALZJ-YW-2.6XZ02**: *IT Whitespace Physical Shift Inspection Operational Guidelines*. Governs multi-sensory inspection rounds, PDU thermal scans, containment differential pressure verification, and quick-disconnect leak audits.
 - **ALZJ-YW-2.6XZ10**: *Liquid Cooling Infrastructure & CDU Operational Guidelines*. Governs primary/secondary loop hydraulic pressures (0.15–0.90 MPa), pump differential pressure limits (< 1.0 bar), plate heat exchanger approach criteria (< 8.0 K), propylene glycol refractometer testing (25.0% wt), and reverse osmosis makeup water chemistry.

## The Copyright Line

This book teaches an operational philosophy and provides an immutable Day Sheet for managing production data center shifts. It is not an official digest, authorized summary, or translation of any third-party course, commercial product manual, or proprietary standard.

All trademarks, service marks, certification titles, and standard identifiers mentioned in this book are the intellectual property of their respective owners:
- *CDFOM*, *CDCS*, and *EPI* are trademarks or registered trademarks of Enterprise Privacy Institute / Enterprise PRATA Pte Ltd.
- *ITIL* is a registered trademark of AXELOS Limited.
- *Uptime Institute* and *Tier Standard* are registered trademarks of Uptime Institute, LLC.
- *ASHRAE* is a registered trademark of the American Society of Heating, Refrigerating and Air-Conditioning Engineers, Inc.
- *NFPA* is a registered trademark of the National Fire Protection Association.
- *Danfoss* and *FD83* are trademarks of Danfoss A/S.
- *NVIDIA*, *NVLink*, and *NVL72* are trademarks of NVIDIA Corporation.

The mention of these titles is strictly for nominative reference, citation, and educational compliance purposes under fair use doctrine. Nothing herein implies endorsement, sponsorship, affiliation, or certification by any of the aforementioned entities.

## Decisions to Record

- The exact editions and publication dates of all standards cited in site procedures.
- Confirmation that no copyrighted standard text or client confidential data was pasted into shift logs.
- The active licensing and training plan for site operations staff.
