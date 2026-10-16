# 6. An Alert Is Not an Incident

The most destructive operational error an organization can commit is wiring an automated monitoring software alert directly into a contractual client notification pipeline.

An alert is a row in a software database. It is a mathematical statement that a specific telemetry stream crossed a pre-programmed threshold inside a digital controller.

An incident is a business, technical, and legal event. It is an operational state where contractual service delivery has failed, where human safety is endangered, or where plant redundancy has collapsed to an extent that imminent catastrophic failure is probable.

**ALERT VS. INCIDENT GOVERNANCE**

| Dimension Software | Alert Production Incident |  |
| :--- | :--- | :--- |
| Origin Automated SC | ADA / BMS Engine Human Operat | ional Command |
| Volume Hundreds per | week Rare (Zero is the goal) |  |
| Authority Required | Software algorithm Licensed D | uty Manager |
| Client Visibility S | trictly Internal / Muted Form | al Contractual SLA |
| Resolution Action A | uto-clear / Sensor tuning For | mal EOP / MOP / RCA |

![The Human Escalation Gate: An Alert is Not an Incident](../figures/fig-03-alert-to-incident-escalation-gate.png)

A software dashboard does not hold a pen. A monitoring algorithm does not possess a professional engineering license. Only a qualified human being—specifically the licensed Duty Manager or designated Enterprise Command Center (ECC) Lead—possesses the legal and operational authority to promote an alert into a production incident.

## The Three Promotion Criteria

An operational alert may be promoted to an incident if and only if it satisfies at least one of **The Three Mandatory Promotion Tests**:

### Test 1: Contractual SLA Boundary Excursion
Did the physical condition breach a legally binding parameter defined in the client Master Services Agreement (MSA)?
- Total loss of electrical power to customer IT server racks (either A or B feed in a 2N topology, or both).
- Secondary technology cooling loop supply temperature exceeding contractual envelope (T_supply > 32.0°C) for longer than the contractual rolling average window (e.g., > 5 continuous minutes).
- Cold aisle rack intake air temperature exceeding ASHRAE TC 9.9 Class A1 allowable limits (T_air > 27.0°C).

If the event breaches an SLA parameter, it is an immediate **P1 Critical Incident**. The contractual notification clock begins ticking instantly.

### Test 2: Threat to Human Life Safety
Does the condition endanger human personnel working on site?
- Electrical arc-flash, explosion, or switchgear fire.
- Activation of optical smoke detection (VESDA) confirmed across multiple zones.
- Toxic or asphyxiating chemical release (refrigerant leak, battery hydrogen off-gassing, nitrogen purging failure).
- Structural flooding or seismic damage.

If human safety is threatened, it is an immediate **P1 Critical Incident**. Execute the site emergency evacuation procedure immediately.

### Test 3: System Redundancy Collapse (N-1 State)
Did the failure eliminate surviving plant redundancy, leaving the facility vulnerable to a single-point failure?
- Trip of 2N Electrical Bus A, forcing 100% of critical load onto surviving Bus B.
- Trip of primary centrifugal chiller in an N+1 plant, leaving zero standby cooling capacity.
- Secondary cooling distribution unit (CDU) operating on single-pump bypass due to an electrical VFD failure.

If redundancy has collapsed, it is an immediate **P2 Major Incident**. Redundant capacity must be restored or emergency load shedding initiated before a second failure occurs.

## If None of the Three Tests Pass

If an alert does not breach an SLA, does not threaten human safety, and does not collapse plant redundancy, **it is not an incident**.

An alert reporting that Chiller 3 oil filter differential pressure reached 0.8 bar (warning threshold) while the chiller continues operating stably with an approach temperature of 1.1 K is an internal operational maintenance task. It belongs on the shift technician's computerized work-order queue.

Promoting a routine maintenance warning to an incident:
- Clogs executive incident communication channels.
- Distracts on-duty engineers from executing critical shift rounds.
- Generates unnecessary panic among commercial client representatives.

Keep internal maintenance warnings strictly within the facility maintenance ticketing system. Never allow a monitoring screen to declare an incident autonomously.

## Decisions to Record

- The specific operational role (Duty Manager / ECC Lead) authorized to promote alerts to incidents.
- The audited test checklist (SLA, Safety, Redundancy) applied prior to incident ticket creation.
- The formal rejection of automated incident dispatching directly from telemetry triggers.
- The separation between internal maintenance work orders and client-facing incident records.

## Quantitative Alert-to-Incident Escalation Matrix and Pager Fatigue Prevention

To protect on-call human cognition, monitoring thresholds are partitioned into three strict severity tiers based on remaining time-to-SLA-breach ($\tau_{\text{margin}}$) and required human intervention authority:

| Telemetry Event Tier | Physical / Redundancy State | Remaining SLA Margin ($\tau_{\text{margin}}$) | Permitted Notification Channel | Mandatory Closure Requirement |
| :--- | :--- | :--- | :--- | :--- |
| **Tier 3: Diagnostic Log** | Single sensor drift or minor VFD speed hunt within normal band | $\tau_{\text{margin}} = \infty$ (No redundancy loss) | Historian log & next-day shift queue (Zero audible/push alert) | Reviewed during daily morning log triage |
| **Tier 2: Actionable Warning** | Redundant component degraded (e.g., 1 of N+2 pumps faulted; filter $\Delta P$ high) | $\tau_{\text{margin}} > 8.0\,\text{hours}$ | Control room console banner + work-order ticket | Closed by completed maintenance ticket + point clear |
| **Tier 1: Critical Incident Page** | Active loss of N+1/2N boundary or imminent thermal/power excursion | $\tau_{\text{margin}} < 30\,\text{minutes}$ | Immediate Pager / Phone wake-up + EOP activation | Formal Incident Record + witnessed physical verification |
