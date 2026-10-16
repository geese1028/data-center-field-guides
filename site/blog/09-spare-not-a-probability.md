---
title: "A spare is evidence. A failure probability is not."
description: "Why theoretical vendor MTBF probabilities cannot substitute for physical on-shelf critical spares (breaker coils, VFD igbts, CDU seals) during a Technical Due Diligence audit."
slug: spare-not-a-probability
book: "Walk a TDD: Technical Due Diligence Physical Site Audit"
book_number: 9
primary_keyword: "data center critical spares vs MTBF probability TDD"
secondary_keywords: ["data center critical spares vs MTBF probability TDD protocol", "data center data TDD audit", "walk a tdd field guide", "mission critical facility commissioning standard"]
schema_type: "TechArticle"
publish_date: "2026-10-16"
---

# A spare is evidence. A failure probability is not.

> **Direct Answer Block**: Why theoretical vendor MTBF probabilities cannot substitute for physical on-shelf critical spares (breaker coils, VFD igbts, CDU seals) during a Technical Due Diligence audit. In mission-critical data center commissioning and operations, engineers enforce this boundary using deterministic physical equations, calibrated field instrumentation, and auditable sign-off gates rather than relying on vendor brochure summaries, uncalibrated software plots, or verbal assurances. Every measurement and state transition must be recorded with synchronized UTC timestamps and explicit pass/fail thresholds before a signature is granted.

![Spare, person, stop. Not a probability.](figures/flagship/fig-02-utility-substation-and-grid-diversity.png)

A small calculated chance that several machines fail together looks like engineering. It is a story, unless the failure figure comes from a document you may cite, for this equipment, and you are allowed to use it. A figure half remembered from "industry practice" is not that document. The product will be quoted as your judgment that simultaneous failure can be ignored.

The check that belongs in the opinion is ordinary. Is there a spare for the failure the contract assumes, on a shelf a second person can find, or only on a list. Is there a person on the roster for the hour that matters, and can that person say the first safe state without the binder. Is the emergency paper short enough to be that stop, or is it a repair manual. Seen, documented, or only spoken. Spoken does not enter the opinion as tested.

Redundancy on a slide is the same trap. Two feeds drawn are not two feeds tested. A generator brochure runtime is not a test. Design kilowatts are not tonight's load. Do not add them to look complete. Do not fill the gap with a probability.

If any of the practical checks is missing, the service level is not evidenced. You do not need a tiny number to say that. A tiny number would hide it.

---

## 1. First-Principles Engineering Formulation and Governing Mathematics

In high-density data center environments, verbal summaries and qualitative status tiles routinely obscure incipient physical failures. Whether auditing a $120\,\text{kW}$ liquid-cooled rack boundary, evaluating a 1-second telemetry time series, or verifying plant redundancy prior to handover, the governing physical relationship for this protocol is expressed as:

$$\text{MTTR}_{\text{without\_spare}} = t_{\text{OEM\_lead\_time}} \gg \tau_{\text{redundancy\_survival}}$$

When any term on the left-hand or right-hand side of this relationship is left unmeasured, inferred from an uncalibrated nameplate, or averaged across an unverified time window, the resulting engineering record cannot support a valid operational signature. Field engineers must verify each physical variable independently using NIST/ISO 17025 traceable instruments before proceeding to the next gate in the sequence.

| Audit Verification Parameter | Unacceptable / Defective Field Practice | Auditable First-Principles Requirement | Mandatory Action on Failure |
| :--- | :--- | :--- | :--- |
| **Primary Boundary Definition** | Implied by vendor brochure or slide deck | Explicitly bounded on stamped P&ID / SLD with tag IDs | Halt acceptance; issue formal boundary clarification |
| **Measurement & Telemetry Proof** | Single uncalibrated display reading or 60-sec average | Calibrated Class A/0.5S sensor with 1-sec UTC timestamp | Reject dataset; classify point as `0x40` Stale or `0x80` Bad |
| **Pass / Fail Acceptance Gate** | Qualitative "Looks OK" or "Within Normal Range" | Quantitative numerical corridor cited from revision in force | Log Category A/B defect; withhold retainage or permit |
| **Custody & Sign-Off Record** | Single bundled "Accepted" signature at end of meeting | Scoped, dated sentence naming exact proved & unproved lines | Strike unsupported claims; issue Conditional Refusal |

---

## 2. Deep-Dive Technical Protocol and Field Implementation

The following field protocol—adapted directly from **Volume 09: *Walk a TDD: Technical Due Diligence Physical Site Audit***—establishes the step-by-step verification mechanics required on the data hall floor:

A plant does not meet a service level because the equipment is redundant on a slide. It meets it if someone is there, the stop is findable, and the part the job refuses to start without is in a place a second person can find.

The roster is a document, not a name they mention. Who covers the hour the contract cares about. A team name is not a person. If the roster and the interview disagree, write both. Do not pick the kinder one.

Procedures: you sample, you do not certify the binder. Standing, change, and emergency, one of each if they exist. Can the person say the stop. Does the emergency paper end at the first safe state, or is it a repair manual. A twenty-page emergency paper is a finding about the paper, not a compliment about thoroughness. The day book already split those three. Use the split. Do not paste their procedures.

Spares: the rule, not the catalog. Which job will not start without which part, and whether that part was seen or only listed. A list you did not check is their claim. A price list is not a spare. Training is a signature that the pages were shown, not a slide attendance sheet, if they claim the staff can run the platform.

Maintenance policy and lifespan are claims about the future. You may note the manufacturer's stated life if a document says it, and you say you did not test the life. You may not convert a depreciation period in a contract into a technical life. Those are different sentences. Counsel owns the first. You refuse to dress it as the second.

## Auditing 24/7 Shift Roster Sufficiency, Licensing, and Critical Spare Parts

In institutional M&A acquisitions and project finance underwriting for mission-critical data centers, every qualitative observation recorded during the site walk must be translated into a deterministic commercial or contractual parameter for the investment committee and lending syndicate:

$$\text{FTE}_{\text{actual}} \ge 4.2 \times N_{\text{continuous\_posts}}, \quad \text{MTTR}_{\text{spare}} \le \tau_{\text{SLA}}$$

An observation that merely remarks on plant appearance without quantifying its impact on **Firm Deliverable IT Capacity ($\text{MW}$)**, **Single-Point-of-Failure ($\text{SPOF}$) Availability**, **Immediate Catch-Up Capital Expenditure ($\text{CapEx}$)**, or **Conditions Precedent ($\text{CP}$) / Conditions Subsequent ($\text{CS}$)** fails to protect the relying party.

| TDD Audit Evaluation Axis | Seller / Data Room Presentation | Independent Engineer Verification Protocol | Financing / Acquisition Covenant Impact |
| :--- | :--- | :--- | :--- |
| **Primary Audit Objective** | Auditing 24/7 Shift Roster Sufficiency, Licensing, and Critical Spare Parts | Cross-check VDR contracts against physical nameplates & test logs | Convert unverified claims into explicit CP/CS or valuation haircuts |
| **Sampling & Evidence Rule** | Curated tour of flagship hall or summary slide | Statistical random sample ($n = \lceil\sqrt{N}\rceil + 1$) chosen by auditor | Any sample mismatch triggers expanded $100\%$ population audit |
| **Redundancy & Capacity Gate** | Nameplate sum of generators, chillers, or transformers | Derate for $99.6\%$ ASHRAE extreme wet-bulb and N+1/2N fault paths | Lock underwritten revenue model to firm derated MW ceiling |
| **Financial Protection Mechanism** | Seller warranty representation in purchase agreement | Quantify remediation cost $C_{\text{fix}}$ + schedule delay risk | Require $150\%\text{--}200\%$ cash escrow holdback at financial close |

---

## 3. Field Verification Checklist and Instrumentation Hygiene

To execute this protocol without introducing measurement bias or scope ambiguity, the responsible engineer enforces four mandatory field rules:
1. **Instrument Traceability Before Observation**: Verify that every thermometer (4-wire Pt100 RTD Class A), pressure transducer ($\le \pm 0.1\%$ span), flowmeter, balometer, or power analyzer carries a current calibration certificate and passes a pre-test zero/span check on the day of the walk.
2. **Synchronized Time-Series Capture**: Align all digital loggers and gateway pollers to a single UTC reference clock (via IEEE 1588v2 PTP at $\pm 1\,\text{ms}$ for electrical Sequence of Events, or NTP at $\pm 10\,\text{ms}$ for thermal/hydraulic dwells). Never merge unsynchronized CSV files by row index.
3. **Explicit Isolation of Disturbances vs. Control Handles**: Hold upstream supply temperatures, parallel cabinet loads, and containment door states constant during the observation dwell so that transient plant drift is never mistaken for steady-state equipment performance.
4. **Written Record Prior to Signature**: Record every boundary tag, measured value, uncertainty tolerance, and open limitation in ink on the controlled project sheet before leaving the equipment line-up.

---

## Frequently Asked Questions (FAQ)

### Why does "A spare is evidence. A failure probability is not." matter during high-density data center commissioning and operations?
Why theoretical vendor MTBF probabilities cannot substitute for physical on-shelf critical spares (breaker coils, VFD igbts, CDU seals) during a Technical Due Diligence audit. When project teams bypass this rule to meet a commercial schedule milestone, unverified physical assumptions—such as hidden hydraulic pressure drops, unlogged polling gaps, unblanked bypass leakage, or uncalibrated sensor offsets—transfer directly into live 24/7 production as latent single points of failure.

### How do you quantitatively verify compliance with "data center critical spares vs MTBF probability TDD" on the physical floor?
Compliance is verified by executing the governing mathematical balance ($$\text{MTTR}_{\text{without\_spare}} = t_{\text{OEM\_lead\_time}} \gg \tau_{\text{redundancy\_survival}}$$) using independent, calibrated field instruments across a stabilized steady-state dwell window (minimum 15 to 30 minutes for thermal and hydraulic systems), and confirming that the discrepancy between primary and secondary measurements remains strictly within the pre-declared acceptance band.

### What should an engineer do if a contractor or vendor submits a report that violates this protocol?
The reviewing engineer must refuse to sign the broad acceptance sentence, mark the specific line item as **Unproved / Defective** on the official audit sheet, and either require a witnessed re-test under a corrected script or isolate the unproved scope under a time-bounded Conditional Acceptance with a $150\%$ to $200\%$ financial retainage escrow holdback.

---

From *Walk a TDD: Technical Due Diligence Physical Site Audit*, Tristan, Data Center Field Guides.

Related: [A nameplate is not used capacity](05-nameplate-is-not-capacity.md).
