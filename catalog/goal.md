# Goal

**Set:** 2026-10-11, after book 1 was submitted to KDP.  
**Owner order:** produce the remaining two books.

## Done

Book 1, *Design and Build a Liquid Load Bank for NVL72 Racks*, is submitted. Kindle eBook, author Tristan, 6.99 USD, 70% where the store allows it, not KDP Select. Review can take 72 hours. Do not start a paperback.

## Still to make

Two English field guides. Same rules as book 1. No client names, site IDs, drawings, point lists, quotes, or unconfirmed flow, temperature, pressure, or fitting family. Standards are titles only. ASHRAE text is not digested. NVIDIA marketing multiples are not duty.

Length is the contract band, 15,000–25,000 English words each. Do not pad to 50,000. Book 1 was the exception.

Do not build the EPUB, the cover, or the upload pack until the manuscript exists.

## Translation goal

Owner order, 2026-10-11. They cannot read the target languages. Translate both English books anyway. The 30-day wait is waived for this goal.

Languages, in order: Japanese, Indonesian, Korean, Thai, Arabic. Not Malay.

Rules: translate the English manuscript. Keep citations, pass-line names, and the rule that numbers come from the specification then in force. No local client names. Mark each edition AI-assisted. One language at a time. Book 2 first, then book 1.

Status: done. Both English books are translated into Japanese, Indonesian, Korean, Thai, and Arabic. AI-assisted. Not uploaded. Malay was not in this batch.

### Book 2. Read and Use Load Bank Data

The reader already has a file. The book teaches how to decide whether that file is a valid test. It does not teach how to build the unit.

The reader leaves with one judgment sheet: channels, one clock, dwell, sign, heat story, and the sentence they are allowed to write.

### Book 9. Walk a Technical Due Diligence

Manuscript written 2026-10-12. About 15,000 English words. Lender or buyer technical visit, method from a short on-site review. Not a design, not commissioning, not an audit of the tenant's system. No site, no party names, no serials, no failure-rate product. Sheet in `sheets/visit.md`. Not packaged. Not translated.

### Book 8. Judge a Corrosion Coupon

Expanded 2026-10-12. Gas on board metal, not pipe water and not dust. Copper and silver both, or silver is not claimed. Media chapter accepts a family, a path, and a spent test. It does not give a recipe. No site rates, no severity table. Sheet in `sheets/coupon.md`. Not packaged. Not translated.

### Book 7. Refuse the Handover

Manuscript written 2026-10-12. Receiver's refusal, not the tester's close-out. About 15,000 English words. A signature is a sentence. Missing file judgment, unmeasured model, screen never failed on purpose, nameplate capacity, open punch, slides as staff, wrong-slot certificate: those sentences are refused. No client handover text, no code paste, no site. Sheet in `sheets/refusal.md`. Not packaged. Not translated.

### Book 6. When a Monitor May Speak

Manuscript written 2026-10-12. About 15,000 English words. A point may wake a person only after the source passed a forced failure, and the point has a clock, a quality mark, a line written before the night, and a person who may promote an alert to an incident. Method from operations monitoring. No customer names, no product manual, no point list, no accuracy rate. DCIM is the same rules on facility points, not a product chapter. Sheet in `sheets/point.md`. Not packaged. Not translated.

### Book 5. Run the Data Center Day

Manuscript finished 2026-10-11. Manager's day, original text. CDFOM and CDFOS named as courses only. No course text, no pasted standards, no figures. English EPUB built. Not translated. Not uploaded.

### Book 4. Judge a Data Hall CFD

Started 2026-10-11. Revised the same day. Core is the measurement method and how a report may be used. Two sheets. No site names, no plot temperatures. Manuscript in `books/04-judge-a-cfd/chapters/`. Not packaged. Not translated.

### Book 3. Finish a Liquid Cooling Verification

Owner order, 2026-10-11, revised the same day. Not one afternoon. The reader already has an accepted load bank and can read a file. The book teaches how to finish a verification project on a liquid hall before IT arrives.

Method from the commission pack: twelve products, certificate levels 0–6, scripts approved before the day, a punch register, a close-out pack. Landed order from a liquid-hall job, with site names, people, and script magnitudes left out: survey, static checks, one system at a time, a no-heat pump curve, then the heat scripts, then shutdown, then the report.

The reader leaves with one project sheet. Two numberings must not be mixed: the certificate pack’s Level 1 is factory testing; the landed dialect called static acceptance Level 1.

## Kill

- A chapter that only restates book 1
- A number that is not cited
- A pasted table, code article, or vendor paragraph
- A plot that is a real customer's record

---

## Thanksgiving / Black Friday 2026 Parking Lot (Owner Order: 2026-10-21)

Do not pay full-price setup, activation, or membership fees right now. Revisit during Thanksgiving / Black Friday discount week (late November 2026):

1. **Leanpub**:
   - Status: Parked.
   - Action on Black Friday: Buy author membership/package during Thanksgiving / Black Friday sale discount.
   - Objective: Bulk upload Book 1, Book 2, Book 3, and translated editions.

2. **Draft2Digital (D2D)**:
   - Status: Parked ($20 USD activation fee gatekept).
   - Action on Black Friday: Check for Black Friday activation promo codes or fee waivers. Activate account and push multi-retailer distribution (Apple Books, Barnes & Noble, OverDrive/Libby).

---

## Rakuten Kobo Publishing Policy & Cadence (Owner Order: 2026-10-21)

1. **Phase 1: English Editions Only (Vol 1–9)**
   - Priority: 1 book / day release cadence.
   - Book 1 (English) submitted 2026-10-21 (`abe1c1fa-14ef-4fcf-a1da-d1c23004386b`, ISBN `1990000032332`).
   - Books 2 through 9 to be published sequentially, one volume per day, 100% autonomous without user manual interaction.
2. **Phase 2: Japanese Editions Parked**
   - All 9 Japanese editions are **FROZEN** (`parked_audit_pending`).
   - Do NOT submit Japanese editions until the owner's Gemini 4 quota resets and a full technical review/audit is conducted.

---

## Production Release & Architecture Freeze: v2.0.0 (Owner Order: 2026-10-21)

Website and architectural milestone frozen at release `v2.0.0`:
- **Core Principle**: The web architecture, design layout, styling, and navigation are mature and frozen. Future development builds strictly upon `v2.0.0`.
- **Constraint**: No large architectural modifications to pages (`index.html`, `buy.html`, `about.html`, volume pillar pages, etc.) will occur without explicit owner direction.
- **Permitted Routine Changes**:
  1. Routine book publishing updates (adding new ASINs/IDs, lighting up store buttons via `scripts/sync_publishers.py`).
  2. Blog updates (publishing new engineering protocol articles, figures, and technical field checklists).

---

## Future Writing Pipeline: Gemini 4 / Argon Recovery (ETA: ~3d 7h / ~2026-10-24)

When Gemini 4 / Argon quota resets, execute the final verification, review, diagram generation, and publication packaging for the two flagship magnum opus projects:

### 1. 《物理智能体现场圣经》（The Physical AI Field Manual, Book 10）
- **Location**: `books/10-physical-ai-manual/`
- **Status**: **Complete 7-Chapter First Draft Written & Assembled (`manuscript.md`, 72 KB)**.
- **Chapters**:
  1. `01-agent-ground-truth-tri-layer.md`: Agent Ground Truth Tri-Layer vs LLM Hallucinations.
  2. `02-cdu-hydraulics-bypass-cheating.md`: SMCI 1.8MW CDU Hydraulics & Bypass Fraud Detection.
  3. `03-ten-refusal-redlines.md`: Levels 1-5 Commissioning & The Chief Engineer's 10 Veto Red Lines.
  4. `04-bsria-bg29-pipe-cleaning.md`: BSRIA BG 29 Pipe Cleaning & Zero SRB Tolerance.
  5. `05-alibaba-goc-alarm-suppression.md`: Alibaba GOC Alarm Suppression (`NA61-2`) & Multi-Dimensional Latency Matrix.
  6. `06-cfd-boundary-condition-audit.md`: Auditing CFD Boundary Conditions & Asymmetric Heat Loads (0.36kW vs 11.35kW).
  7. `07-ieee-grounding-srp.md`: IEEE Emerald Book Signal Reference Plane (SRP $\le 1\ \Omega$ at 10 MHz) & Grounding Impedance Audit.
- **Gemini 4 Next Actions**: Deep technical cross-verification, mathematical proof audit, SVG/PNG diagram generation via `generate_engineering_diagrams.py`, EPUB/HTML build.

### 2. 《跨界握手：数据中心物理与算力的双向穿透指南》（The Handshake: Vol 1 & Vol 2, Book 11）
- **Location**: `books/11-it-idc-handshake/`
- **Status**: **Complete 12-Chapter First Draft Written & Assembled (`manuscript.md`, 142 KB)**.
- **Chapters**:
  1. `01-reverse-airflow-tor.md`: ToR switch reverse airflow, AFI/AFO models, 58°C artificial lava fountain.
  2. `02-cable-snake-choke.md`: Cable bundles choking exhausts, 15-25 Pa backpressure, 5kW wasted fan power.
  3. `03-color-poka-yoke.md`: Visual poka-yoke, Yellow `#FFFF00` (A) vs Blue `#0C00CC` (B), Red `#DB0015` core, Green `#00FF41` temporary.
  4. `04-sla-paradox-four-nines.md`: The 99.99% fallacy, 5-minute outage vs 3-week storage split-brain/Raft recovery, inrush storm.
  5. `05-neutral-to-ground-standoff.md`: Neutral-to-ground voltage ($V_{\text{ng}} = 3.8\text{V}$) standoff, differential signaling logic ground shift.
  6. `06-ibm-silver-corrosion.md`: IBM System Center silver corrosion (Cu 38.2 Å vs Ag 621.5 Å), economizer dew point inversion, SAC305 creep corrosion.
  7. `07-tape-library-stray-field.md`: TS4500/LTO cold vault 24h acclimatization vs liquid bridge stiction; 2500A busway 120 Oe stray magnetic soft erasure.
  8. `08-floor-cutout-brush-grommet.md`: Underfloor cutout cold bypass vs missing 1U blanking panel negative pressure recirculation; GPU thermal throttling.
  9. `09-rail-depth-post-spacing.md`: 850mm chassis depth vs 650mm post spacing, uncloseable rear doors, HAC breach, 750mm EIA-310 post spacing.
  10. `10-transport-dock-floor-loading.md`: Gravity failures: 15cm dock drops, 2.1m elevator choke, 1.6-ton NVL72 rack floor punch-through & AIS standards.
  11. `11-power-sag-and-step-load.md`: 15ms PSU hold-up time vs ATS switching; AI distributed training MW-level step load pulse & generator governor oscillation.
  12. `12-contractor-50-redlines-and-agent.md`: Contractor 50 Red Lines & Cross-Boundary Interface Auditor Agent.
- **Gemini 4 Next Actions**: Peer review against vendor manuals, terminal layout styling, generation of cross-boundary architecture diagrams, EPUB/KDP compilation.


