# 4. People and the governance ring

A liquid cooling verification conducted without clearly designated individual roles rapidly degenerates into an uncoordinated group discussion. The standard method statement calls for an exhaustive RACI matrix (Responsible, Accountable, Consulted, Informed). In the high-stakes environment of a live or near-live data hall, that structure must be distilled into three distinct commercial entities and five specific engineering functions.

**THE THREE-PARTY GOVERNANCE TRIANGLE**

| THE FACILITY OWNER (Client / Hyperscaler Ops) | Witnesses execution, authorizes deviations, and signs off final certificate tiers. Does not operate tools. |
| :--- | :--- |
| THE VERIFICATION AUTHORITY (CxA) (Independent Testing Agency) | Authors Cx Plan & scripts, manages calibration, directs steps, records data, and audits punch list. Never closes own defect. |
| THE TRADE CONSTRUCTOR (General / Mechanical / Electrical) | Supplies as-built drawings, operates breakers and valves, and performs physical punch list repairs under permit. |

## The Three Commercial Parties

The boundary between these three entities must be strictly enforced.
- **The Facility Owner**: Holds ultimate commercial authority. They witness the critical operational steps and sign the Level 4 and Level 5 completion certificates. The owner’s representative does not write field scripts while standing in the aisle, nor do they turn valve handles.
- **The Verification Party**: Authors the Commissioning Plan and test scripts, directs the execution sequence, and witnesses every measurement. They maintain the master punch list and will never sign off on their own punch list item without an independent secondary inspection.
- **The Constructor**: Provides original equipment submittals and as-built drawings, energizes breakers, operates manual isolation valves, and physically rectifies defects identified on the punch list.

If a single engineering firm is contracted to perform both construction and commissioning, that conflict of interest must be formally documented on page one of the Commissioning Plan. When the installer and the verification witness belong to the same organizational hierarchy, project governance is inherently compromised unless separate, non-reporting personnel execute and witness each task.

## The Five Functional Hands

Within the testing team on the floor, five distinct technical functions must be staffed. These represent functional responsibilities rather than a requirement for five separate bodies; on a smaller test, one experienced engineer may cover multiple disciplines. However, no individual may act as the sole witness for an operational task they physically performed.

**THE FIVE FUNCTIONAL DISCIPLINES**

| 1. TEST LEAD | Owns the approved testing window, enforces the claim, directs step timing, manages communications, and holds sole authority to initiate thermal load. |
| :--- | :--- |
| 2. ELECTRICAL PE | Directs lock-out/tag-out (LOTO), conducts megger insulation & ground testing, verifies phase rotation, monitors upstream PDU trip curves, and runs IR scans |
| 3. MECHANICAL PE | Manages secondary fluid loop, oversees hydrostatic pressure holds & venting, audits CDU pump curves, and tracks quick disconnect seal integrity. |
| 4. CONTROLS PE | Cross-checks BMS telemetry against calibrated field gauges, validates Modbus/ BACnet registers, and injects hardware alarm faults to verify trip logic. |
| 5. TEST TECH | Manages physical load-bank connections, verifies instrument calibration logs, records all measured values in ink on master sheets, and maintains archives. |

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

**COMMAND AND STOP GOVERNANCE**

| WHO MAY COMMAND HEAT | WHO MAY CALL AN EMERGENCY STOP |
| :--- | :--- |
| • Exactly ONE named person on site. | • EVERY PERSON in the room. |
| • Recorded in ink on Sheet 3 before first step. | • Requires zero consensus or prior approval. |
| • Must confirm all prerequisite gates are signed. | • Overrides all project schedules and costs. |
| • Operates strictly within approved script steps. | • Survives the organizational chart completely. |

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
