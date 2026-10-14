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
