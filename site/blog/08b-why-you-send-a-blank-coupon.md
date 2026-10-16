---
title: "Why a corrosion test needs a blank coupon"
description: "Why every batch of exposed data center corrosion coupons must travel with an unopened, lot-matched Field Travel Blank (FTB) to isolate transit and lab background noise."
slug: why-you-send-a-blank-coupon
book: "Judge a Corrosion Coupon"
book_number: 8
primary_keyword: "field travel blank corrosion coupon quality control"
secondary_keywords: ["field travel blank corrosion coupon quality control protocol", "data center field control audit", "judge a corrosion coupon field guide", "mission critical facility commissioning standard"]
schema_type: "TechArticle"
publish_date: "2026-10-16"
---

# Why a corrosion test needs a blank coupon

> **Direct Answer Block**: Why every batch of exposed data center corrosion coupons must travel with an unopened, lot-matched Field Travel Blank (FTB) to isolate transit and lab background noise. In mission-critical data center commissioning and operations, engineers enforce this boundary using deterministic physical equations, calibrated field instrumentation, and auditable sign-off gates rather than relying on vendor brochure summaries, uncalibrated software plots, or verbal assurances. Every measurement and state transition must be recorded with synchronized UTC timestamps and explicit pass/fail thresholds before a signature is granted.

![The blank bounds the trip.](figures/flagship/fig-06-passive-coupons-vs-realtime-qcm-monitors.png)

The strip that hung in the room is the sample. The strip that traveled in a sealed bag and never saw that air is the blank. It tells you what the mailer, the vehicle, and the lab did to the metal. Without it, a bad rate might be the journey. You will treat a room for a courier. A fine rate might be the bag. You will sign fit for a trip.

Send a blank from the same lot, same metal, same mailer. If the lab will not report it apart from the sample, you do not know what fraction of the rate is the room. Do not assign the whole rate to the boards. Do not open the blank to show a visitor a clean strip. An opened blank is spoiled. A spoiled blank does not clear the trip.

The blank does not replace a room coupon, and a clean blank does not average away a bad board-face strip. It only bounds the trip. If the blank moved as much as the sample, the place sentence is refused until the trip is understood. That refusal does not require the digits reprinted here. It requires the comparison the report already printed, read honestly.

No blank is allowed only if you are not signing a fit class. A harsh result can still be a reason to look. Fit without a blank is fit you cannot separate from the mailer. Do not write "subject to blank later." Later does not reconstruct a bag you did not send. File the blank's report next to the sample's. A blank filed somewhere else will be forgotten the day someone wants the word fit.

---

## 1. First-Principles Engineering Formulation and Governing Mathematics

In high-density data center environments, verbal summaries and qualitative status tiles routinely obscure incipient physical failures. Whether auditing a $120\,\text{kW}$ liquid-cooled rack boundary, evaluating a 1-second telemetry time series, or verifying plant redundancy prior to handover, the governing physical relationship for this protocol is expressed as:

$$d_{\text{blank, Cu}} \le 35\,\text{\AA} \;\land\; d_{\text{blank, Ag}} \le 25\,\text{\AA} \implies \text{Valid Chain of Custody}$$

When any term on the left-hand or right-hand side of this relationship is left unmeasured, inferred from an uncalibrated nameplate, or averaged across an unverified time window, the resulting engineering record cannot support a valid operational signature. Field engineers must verify each physical variable independently using NIST/ISO 17025 traceable instruments before proceeding to the next gate in the sequence.

| Audit Verification Parameter | Unacceptable / Defective Field Practice | Auditable First-Principles Requirement | Mandatory Action on Failure |
| :--- | :--- | :--- | :--- |
| **Primary Boundary Definition** | Implied by vendor brochure or slide deck | Explicitly bounded on stamped P&ID / SLD with tag IDs | Halt acceptance; issue formal boundary clarification |
| **Measurement & Telemetry Proof** | Single uncalibrated display reading or 60-sec average | Calibrated Class A/0.5S sensor with 1-sec UTC timestamp | Reject dataset; classify point as `0x40` Stale or `0x80` Bad |
| **Pass / Fail Acceptance Gate** | Qualitative "Looks OK" or "Within Normal Range" | Quantitative numerical corridor cited from revision in force | Log Category A/B defect; withhold retainage or permit |
| **Custody & Sign-Off Record** | Single bundled "Accepted" signature at end of meeting | Scoped, dated sentence naming exact proved & unproved lines | Strike unsupported claims; issue Conditional Refusal |

---

## 2. Deep-Dive Technical Protocol and Field Implementation

The following field protocol—adapted directly from **Volume 08: *Judge a Corrosion Coupon***—establishes the step-by-step verification mechanics required on the data hall floor:

A coupon that traveled in a sealed bag, and was never hung, is a blank. It tells you what the mailer, the vehicle, and the lab did to the metal before anyone calls the result the room. Without it, a bad rate might be the journey. You will then treat a room for a courier. Hang the real strips. Send a blank from the same lot, same metal, same mailer, unopened to the air you care about. If the lab cannot tell a blank from a sample in the report, ask them to. If they will not, you do not know what fraction of the rate is the trip. Do not assign the whole rate to the boards.

The blank is not a second room. It does not clear a bad board-face strip by being cleaner, and it does not condemn the room by being dirty. It bounds the trip. Write both rates as filed, in their report, not in this piece. If the blank moved as much as the sample, the sample's place sentence is refused until you understand the trip. That refusal does not need their number reprinted. It needs the comparison they already printed, read honestly.

## The lot

Strips from different lots are not a pair, even if both say silver. A lot that was already tarnished in the tin is a tainted zero. Ask whether the lab or the vendor records the lot. If nobody does, say so. You can still hang them. You cannot call a small difference between two hangs a trend. Trend needs the same lot, or an explicit statement that lot does not matter, from the method, not from hope.

Do not touch the face you intend them to read. Skin, cleaner, and a glove that is not the one their method names are a treatment you did not record. If their method is silent, silence is not permission. Handle by the edge, or do not handle. This is not a procedure for preparing metal. It is a refusal to become an unrecorded source.

## Opening the bag

Open the sample bag at the place, at the start time you will write, not in the office the day before. An hour on a desk is an hour in the wrong air, and it will be averaged into the room. If you must stage them, keep them sealed and write the staging. Sealed and forgotten in a hot cabinet is still a condition. Note it, or do not use the rate for a fine class.

Take them down into a bag at the end time, at the place. A strip carried open across the hall, then across a loading dock, has a second exposure. That second exposure is usually shorter than the hang. It is still unaudited. Bag at the place. The blank never leaves its bag. If someone opened the blank "just to check," it is not a blank. Mark it spoiled. Do not average it into a story that the trip was clean.

## What the lab owes the blank

The report names the blank's metal and that it was not exposed by you, or it does not mention a blank. No mention: write "no blank" on the sheet. No blank is allowed only if you are not signing a fine class. A coarse, obvious attack may still be discussed as a hypothesis. A class that means "fit" requires the trip to have been bounded. Otherwise fit may be the bag, or the attack may be the bag. You cannot tell. Not telling is a refusal, not a delay. Do not write "subject to blank later." Later does not reconstruct a bag you did not send.

Keep the blank's report in the same file as the sample's report. A blank filed somewhere else will be forgotten the day someone wants a fit sentence. Forgotten blank, no fit class. That is the whole rule, applied at filing time rather than in the meeting.

## Statistical Quality Control Using Field Travel Blanks (FTB) and Lot Controls

### Detecting Transit Contamination, Mailer Outgassing, and Lab Stripping Offset

Under **ANSI/ISA-71.04-2013** (*Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*) and **ASHRAE TC 9.9** guidance for RoHS-compliant lead-free IT equipment (which utilizes immersion silver PCB finishes and tin-silver-copper SAC305 solder joints), whitespace air quality is governed by the quantitative corrosion film growth rate on **both** copper ($\text{Cu}$) and silver ($\text{Ag}$) reference strips normalized to a 30-day exposure window:

$$d_{\text{blank}} \le 35\,\text{\AA} \text{ (Cu)} \;\land\; d_{\text{blank}} \le 25\,\text{\AA} \text{ (Ag)} \implies \text{Valid Chain of Custody}$$

Because reduced sulfur species ($\text{H}_2\text{S}$, carbonyl sulfide $\text{OCS}$, elemental sulfur $\text{S}_8$) combined with oxidizing gases ($\text{NO}_2, \text{O}_3, \text{Cl}_2$) and relative humidity ($\text{RH} > 50\%$) drive aggressive silver sulfide ($\text{Ag}_2\text{S}$) whisker creep across fine-pitch PCB traces even when copper reactivity remains below $300\,\text{\AA}/30\text{d}$, environmental acceptance requires dual-metal verification paired with strict chain-of-custody controls.

| Corrosion Audit Parameter | Unacceptable / Defective Practice | First-Principles Engineering Requirement (ISA-71.04 / ASTM B825) | Mandatory Refusal or Remediation Action |
| :--- | :--- | :--- | :--- |
| **Core Chapter Focus** | Invalidating Fit Classifications When Travel Blanks Exceed Baseline Noise | Dual $\text{Cu} + \text{Ag}$ coulometric reduction with documented exposure timestamps | Refuse any environmental fitness claim missing $\text{Ag}$ or hang interval |
| **Class G1 Mild Pass Gate** | Quoting Copper rate alone ($<300\,\text{\AA}$) or visual strip color | $d_{\text{Cu}} < 300\,\text{\AA}/30\text{d}$ **AND** $d_{\text{Ag}} < 200\,\text{\AA}/30\text{d}$ (zero $\text{Cu}_2\text{S}$ on copper) | Classify G2 ($<1000/1000\,\text{\AA}$), G3 ($<2000/2000\,\text{\AA}$), or GX as non-compliant |
| **Chain of Custody & Blank** | Mailing strips without a sealed Field Travel Blank (`FTB`) | Sealed lot-matched travel blank $d_{\text{blank}} \le 25\text{--}35\,\text{\AA}$ subtracted/verified | Invalidate "Fit" certification if no unopened travel blank accompanied lot |
| **Filtration & Envelope Proof** | Installing recirculation filters in an unsealed negative-$\Delta P$ hall | Vapor-sealed envelope ($\Delta P \ge +12.5\,\text{Pa}$) + gas-matched media ($\text{EBCT} \ge 0.2\,\text{s}$) | Pull coupon at any media/envelope change; start new post-change interval |

---

## 3. Field Verification Checklist and Instrumentation Hygiene

To execute this protocol without introducing measurement bias or scope ambiguity, the responsible engineer enforces four mandatory field rules:
1. **Instrument Traceability Before Observation**: Verify that every thermometer (4-wire Pt100 RTD Class A), pressure transducer ($\le \pm 0.1\%$ span), flowmeter, balometer, or power analyzer carries a current calibration certificate and passes a pre-test zero/span check on the day of the walk.
2. **Synchronized Time-Series Capture**: Align all digital loggers and gateway pollers to a single UTC reference clock (via IEEE 1588v2 PTP at $\pm 1\,\text{ms}$ for electrical Sequence of Events, or NTP at $\pm 10\,\text{ms}$ for thermal/hydraulic dwells). Never merge unsynchronized CSV files by row index.
3. **Explicit Isolation of Disturbances vs. Control Handles**: Hold upstream supply temperatures, parallel cabinet loads, and containment door states constant during the observation dwell so that transient plant drift is never mistaken for steady-state equipment performance.
4. **Written Record Prior to Signature**: Record every boundary tag, measured value, uncertainty tolerance, and open limitation in ink on the controlled project sheet before leaving the equipment line-up.

---

## Frequently Asked Questions (FAQ)

### Why does "Why a corrosion test needs a blank coupon" matter during high-density data center commissioning and operations?
Why every batch of exposed data center corrosion coupons must travel with an unopened, lot-matched Field Travel Blank (FTB) to isolate transit and lab background noise. When project teams bypass this rule to meet a commercial schedule milestone, unverified physical assumptions—such as hidden hydraulic pressure drops, unlogged polling gaps, unblanked bypass leakage, or uncalibrated sensor offsets—transfer directly into live 24/7 production as latent single points of failure.

### How do you quantitatively verify compliance with "field travel blank corrosion coupon quality control" on the physical floor?
Compliance is verified by executing the governing mathematical balance ($$d_{\text{blank, Cu}} \le 35\,\text{\AA} \;\land\; d_{\text{blank, Ag}} \le 25\,\text{\AA} \implies \text{Valid Chain of Custody}$$) using independent, calibrated field instruments across a stabilized steady-state dwell window (minimum 15 to 30 minutes for thermal and hydraulic systems), and confirming that the discrepancy between primary and secondary measurements remains strictly within the pre-declared acceptance band.

### What should an engineer do if a contractor or vendor submits a report that violates this protocol?
The reviewing engineer must refuse to sign the broad acceptance sentence, mark the specific line item as **Unproved / Defective** on the official audit sheet, and either require a witnessed re-test under a corrected script or isolate the unproved scope under a time-bounded Conditional Acceptance with a $150\%$ to $200\%$ financial retainage escrow holdback.

---

From *Judge a Corrosion Coupon*, Tristan, Data Center Field Guides.

Related: [What a corrosion coupon report must show](08b-what-the-coupon-report-must-show.md).
