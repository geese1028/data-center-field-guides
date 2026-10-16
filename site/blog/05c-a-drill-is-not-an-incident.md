---
title: "A drill record is not an incident review"
description: "Why emergency EOP drill records and post-incident Root Cause Analysis (RCA) reports must be filed in separate ledgers with distinct verification metrics."
slug: a-drill-is-not-an-incident
book: "Run the Data Center Day: What the Manager Must Sign Before the Shift Ends"
book_number: 5
primary_keyword: "data center emergency drill vs incident RCA"
secondary_keywords: ["data center emergency drill vs incident RCA protocol", "data center data RCA audit", "run the day field guide", "mission critical facility commissioning standard"]
schema_type: "TechArticle"
publish_date: "2026-10-16"
---

# A drill record is not an incident review

> **Direct Answer Block**: Why emergency EOP drill records and post-incident Root Cause Analysis (RCA) reports must be filed in separate ledgers with distinct verification metrics. In mission-critical data center commissioning and operations, engineers enforce this boundary using deterministic physical equations, calibrated field instrumentation, and auditable sign-off gates rather than relying on vendor brochure summaries, uncalibrated software plots, or verbal assurances. Every measurement and state transition must be recorded with synchronized UTC timestamps and explicit pass/fail thresholds before a signature is granted.

![Drill versus incident](figures/flagship/fig-03-shift-round-inspection-topology.png)

Operators drill. The record shows a date, a scenario, and often a conclusion that the team passed. That record is evidence the exercise happened. It is not evidence the last real incident was handled, and it is not a test of the plant.

Read the drill for three lines. Was the scenario the stop your contract cares about, or a classroom topic. Did the person who would be called on that shift take part, or only the people who were free. Was the result a gap in the paper, written, or a score. A score without a gap is a mood. Moods do not change the emergency paper.

A drill that never fails is not a strong system. It is an exercise that could not see a miss. One owned change to the paper, or an explicit none with a reason, is a review. A sign-in sheet is not.

Do not paste the scenario, the phone tree, or the site's hazards into a public note. Those are theirs. The method is the three lines. If a due diligence is shown only the annual drill and not the last incident note, write what you were shown. Do not upgrade a drill into an incident history.

---

## 1. First-Principles Engineering Formulation and Governing Mathematics

In high-density data center environments, verbal summaries and qualitative status tiles routinely obscure incipient physical failures. Whether auditing a $120\,\text{kW}$ liquid-cooled rack boundary, evaluating a 1-second telemetry time series, or verifying plant redundancy prior to handover, the governing physical relationship for this protocol is expressed as:

$$t_{\text{drill\_execution}} \le t_{\text{SLA\_budget}}, \qquad \text{Incident Closure} \iff \text{COMTRADE + SOE + Physical Fix Verified}$$

When any term on the left-hand or right-hand side of this relationship is left unmeasured, inferred from an uncalibrated nameplate, or averaged across an unverified time window, the resulting engineering record cannot support a valid operational signature. Field engineers must verify each physical variable independently using NIST/ISO 17025 traceable instruments before proceeding to the next gate in the sequence.

| Audit Verification Parameter | Unacceptable / Defective Field Practice | Auditable First-Principles Requirement | Mandatory Action on Failure |
| :--- | :--- | :--- | :--- |
| **Primary Boundary Definition** | Implied by vendor brochure or slide deck | Explicitly bounded on stamped P&ID / SLD with tag IDs | Halt acceptance; issue formal boundary clarification |
| **Measurement & Telemetry Proof** | Single uncalibrated display reading or 60-sec average | Calibrated Class A/0.5S sensor with 1-sec UTC timestamp | Reject dataset; classify point as `0x40` Stale or `0x80` Bad |
| **Pass / Fail Acceptance Gate** | Qualitative "Looks OK" or "Within Normal Range" | Quantitative numerical corridor cited from revision in force | Log Category A/B defect; withhold retainage or permit |
| **Custody & Sign-Off Record** | Single bundled "Accepted" signature at end of meeting | Scoped, dated sentence naming exact proved & unproved lines | Strike unsupported claims; issue Conditional Refusal |

---

## 2. Deep-Dive Technical Protocol and Field Implementation

The following field protocol—adapted directly from **Volume 05: *Run the Data Center Day: What the Manager Must Sign Before the Shift Ends***—establishes the step-by-step verification mechanics required on the data hall floor:

An incident is any event where critical infrastructure fails to deliver the contractual service envelope, where a human life is endangered, or where the facility enters an unstable state that will imminently cause either outcome.

| **INCIDENT ESCALATION TIMELINE** |
| :--- |
| [T = 00:00] EVENT DISCOVERY (Telemetry trip, acoustic alarm, visual) |
| ↓ |
| [T + 02:00] STOP & ASSESS: Silence horn; identify failing subsystem |
| ↓ |
| [T + 05:00] EXECUTE EOP: Stabilize nearest safe state; isolate hazard |
| ↓ |
| [T + 10:00] SUMMON INCIDENT COMMAND: Establish incident log; assign roles |
| ↓ |
| [T + 15:00] CLIENT SLA NOTIFICATION: Send factual notice (NO HYPOTHESES) |
| ↓ |
| [T + 60:00] TECHNICAL CONTAINMENT: Deploy MOP repairs; continuous updates |
| ↓ |
| [POST-EVENT] ROOT CAUSE ANALYSIS (RCA): Fishbone, 5-Whys, 1 owned action |


A noisy alarm that does not threaten service delivery or human safety is an annoyance. Do not elevate it to an emergency. Conversely, never downgrade a genuine service degradation because the equipment room appears quiet and calm. The sole metric of an incident is service delivery and personnel safety.

## The Incident Severity Classification

Every abnormal event must be classified into one of three strict severity tiers within two minutes of discovery:

**INCIDENT SEVERITY CLASSIFICATION**

| Tier | Classification | Operational Impact Client Noti | fication |
| :--- | :--- | :--- | :--- |
| P1 Cr | itical Total lo | ss of power or cooling <= 15 M | in; Hourly Upd |
| to IT | load; human li | fe safety |  |
| P2 Ma | jor Loss of sys | tem redundancy <= 30 Min; 2-Ho | ur Upd |
| (N-1 | state); high te | mp warning |  |
| P3 Mi | nor Single comp | onent failure with Shift Summa | ry Log |
| zero | redundancy impa | ct |  |

## The First Hour: The Incident Clock

During a live incident, human memory degrades rapidly under adrenaline. Technicians remember actions out of sequence; managers compress twenty minutes of hesitation into five minutes of remembered decisiveness.

The duty manager must open an immutable, time-stamped **Incident Chronology Log** at the exact minute the event begins:

| **INCIDENT CHRONOLOGY LOG** |
| :--- |
| [09:14:22] EPMS reports Breaker B-SWG-02 instantaneous trip on feeder B |
| [09:16:00] Duty Manager initiates EOP-E-04 (Loss of 2N Feeder B) |
| [09:18:45] Technician Chen confirms Bus A carrying 82% total load |
| [09:21:10] Safe State 1 reached: IT load stable on single feed |
| [09:24:00] Client SLA Notice 1 transmitted via portal (T+10 min) |
| [09:32:00] Infrared scan of Bus A switchgear shows 58°C; stable |
| [09:45:00] Switchgear vendor called; ticket #84920 opened |

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

| **CLIENT NOTIFICATION DISCIPLINE** |
| :--- |
| [PERMITTED FACTUAL NOTICE] |
| "At 09:14 UTC, Electrical Feeder B experienced an automatic trip. |
| All critical IT whitespace remains fully powered via redundant |
| Feeder A. The facility is currently operating in an N-1 state. |
| Operations teams are investigating the cause of the Feeder B trip. |
| The next formal update will be provided at 10:15 UTC." |
| [PROHIBITED SPECULATIVE NOTICE] |
| "We think a contractor bumped a relay on Feeder B, or maybe the |
| utility had a lightning strike down the road. We are resetting the |
| breaker now and hope to have it back in ten minutes." |

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

## Post-Incident Root Cause Analysis (RCA) and the Five-Layer Evidence Hierarchy

When an unplanned equipment trip or SLA excursion occurs, the shift manager's immediate duty during the shift is **stabilization at the First Safe State** and **forensic preservation of transient evidence**. Volatile waveform buffers inside protective relays and UPS event logs overwrite themselves if power is cycled or if a technician clears latches before downloading the fault record.

### The Forensic Evidence Preservation Sequence

Within the first $60$ minutes after stabilizing the plant, before any reset button is pressed or any vendor replaces a circuit board, the shift team must capture and lock five layers of timestamped evidence:
1. **COMTRADE Oscillography Waveforms (IEEE C37.111)**: Export high-speed ($4\,\text{kHz}$ to $16\,\text{kHz}$) voltage and current fault waveforms from MV/LV protective relays and UPS inverters covering $10$ cycles pre-fault and $30$ cycles post-fault.
2. **Sequence of Events (SOE) Microsecond Ledger**: Export the PTP-synchronized ($\pm 1\,\text{ms}$) digital state transitions showing the exact first-out initiator breaker or sensor contact.
3. **Physical Relay Targets and Mechanical Flags**: Photograph mechanical drop-flags, breaker spring-charge indicators, and pressure relief rupture discs *before* resetting any latch.
4. **Fluid and Chemical Samples**: If a liquid cooling loop or diesel generator tripped, draw a sealed $500\,\text{mL}$ fluid sample for particulate/glycol/fuel analysis before flushing or refilling.
5. **Witness Timeline Statements**: Record independent written timestamps from each shift technician before group discussion merges their recollections.

## Customer Incident Communication Cadence and Factual Bulletin Rules

During an active Severity 1 or Severity 2 incident, external customer notifications are issued on a strict **15-Minute / 30-Minute Factual Heartbeat** by the Incident Commander—never by the hands-on switching technicians on the floor. Every bulletin states three verified facts only: (1) UTC timestamp and affected boundary, (2) current physical state of the plant (e.g., *Load supported on N+1 Generator Bus B; Hall Temperatures 23.4°C*), and (3) timestamp of the next scheduled update. Speculating on root cause before COMTRADE and SOE logs are analyzed is strictly prohibited.

---

## 3. Field Verification Checklist and Instrumentation Hygiene

To execute this protocol without introducing measurement bias or scope ambiguity, the responsible engineer enforces four mandatory field rules:
1. **Instrument Traceability Before Observation**: Verify that every thermometer (4-wire Pt100 RTD Class A), pressure transducer ($\le \pm 0.1\%$ span), flowmeter, balometer, or power analyzer carries a current calibration certificate and passes a pre-test zero/span check on the day of the walk.
2. **Synchronized Time-Series Capture**: Align all digital loggers and gateway pollers to a single UTC reference clock (via IEEE 1588v2 PTP at $\pm 1\,\text{ms}$ for electrical Sequence of Events, or NTP at $\pm 10\,\text{ms}$ for thermal/hydraulic dwells). Never merge unsynchronized CSV files by row index.
3. **Explicit Isolation of Disturbances vs. Control Handles**: Hold upstream supply temperatures, parallel cabinet loads, and containment door states constant during the observation dwell so that transient plant drift is never mistaken for steady-state equipment performance.
4. **Written Record Prior to Signature**: Record every boundary tag, measured value, uncertainty tolerance, and open limitation in ink on the controlled project sheet before leaving the equipment line-up.

---

## Frequently Asked Questions (FAQ)

### Why does "A drill record is not an incident review" matter during high-density data center commissioning and operations?
Why emergency EOP drill records and post-incident Root Cause Analysis (RCA) reports must be filed in separate ledgers with distinct verification metrics. When project teams bypass this rule to meet a commercial schedule milestone, unverified physical assumptions—such as hidden hydraulic pressure drops, unlogged polling gaps, unblanked bypass leakage, or uncalibrated sensor offsets—transfer directly into live 24/7 production as latent single points of failure.

### How do you quantitatively verify compliance with "data center emergency drill vs incident RCA" on the physical floor?
Compliance is verified by executing the governing mathematical balance ($$t_{\text{drill\_execution}} \le t_{\text{SLA\_budget}}, \qquad \text{Incident Closure} \iff \text{COMTRADE + SOE + Physical Fix Verified}$$) using independent, calibrated field instruments across a stabilized steady-state dwell window (minimum 15 to 30 minutes for thermal and hydraulic systems), and confirming that the discrepancy between primary and secondary measurements remains strictly within the pre-declared acceptance band.

### What should an engineer do if a contractor or vendor submits a report that violates this protocol?
The reviewing engineer must refuse to sign the broad acceptance sentence, mark the specific line item as **Unproved / Defective** on the official audit sheet, and either require a witnessed re-test under a corrected script or isolate the unproved scope under a time-bounded Conditional Acceptance with a $150\%$ to $200\%$ financial retainage escrow holdback.

---

From *Run the Data Center Day: What the Manager Must Sign Before the Shift Ends*, Tristan, Data Center Field Guides.

Related: [An EOP stops at the first safe state](05b-eop-stops.md).
