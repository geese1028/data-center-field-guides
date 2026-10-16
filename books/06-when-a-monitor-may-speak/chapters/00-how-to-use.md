# 0. How to Use This Book

This book is for the person who must decide whether a screen is allowed to wake someone. The screen may be a Building Management System (BMS), an Electrical Power Monitoring System (EPMS), a SCADA terminal, a log store, a wall of red alarm tiles, or an AI-generated health score that an executive wants to treat as a verdict.

The rule is uncompromising: **A point speaks only after it possesses a synchronized clock, a verified hardware source path, a quality mark, an audited threshold with deadband hysteresis, and a named human who holds the sole authority to turn an alert into an incident.**

It is not a product manual. It is not a guided tour of a vendor's graphical user interface. It is not a customer's Modbus register map rewritten in cleaner English. The methods in this book originate from decades of mission-critical facility and infrastructure telemetry: analog instrumentation, digital sequence of events, transient line filtering, and alarm storm containment. The specific customer identities, classified site names, and commercial monitoring software brands remain out. If a sentence in this book begins to resemble a sales slide from a monitoring software demo, it does not belong.

The earlier books in this series established the physical baselines:
- Book 01 builds the liquid load bank and instruments the manifold.
- Book 02 reads the thermal and hydraulic flash report.
- Book 03 finishes the seven sheets of commissioning verification.
- Book 04 audits the CFD model against physical measurements.
- Book 05 runs the daily shift, manages work permits, and enforces the 2N capacity ceiling.

This book is the operational bridge between physical reality and digital telemetry. It establishes when a dashboard is permitted to speak at all. It does not replace the physical pressure gauge, the walked infrared thermography scan, or the signed shift logbook.

| **OPERATIONAL TELEMETRY PIPELINE** |
| :--- |
| [PHYSICAL SENSOR] 4-20mA / RTD / Contact / CT / PT Transducer |
| ↓ |
| [POINT INGESTION] Value + UTC Timestamp (PTP/NTP) + Source URI + Quality |
| ↓ |
| [QUALITY GATE] Quality Bitmask == GOOD (0x00)? |
| → NO: Quench alarming; flag STALE/FAULT telemetry |
| → YES: Pass to Signal Processing Filter |
| ↓ |
| [SIGNAL FILTER] Apply Analog Deadband Hysteresis (Delta-H) |
| Evaluate Continuous Dwell Window (t >= t_dwell) |
| Anti-Flap Quarantine Engine (N_toggles >= 4 in 10 min) |
| ↓ |
| [ALARM STORM MASK] Topology-Aware Parent-Child Dependency Suppression |
| Upstream breaker trip mutes downstream symptom alarms |
| ↓ |
| [HUMAN GATEWAY] An Alert is NOT an Incident! |
| Only designated Duty Manager may promote based on: |
| (1) SLA breach, (2) Life safety, (3) Redundancy loss |
| ↓ |
| [THE 5-LINE PAGE] Time, Point & Path, Line, Person Woken, First Look/Stop |

A monitor that disagrees with a walked physical measurement does not win simply by being automated. When the digital screen reports that a CDU secondary loop is operating at 28.0°C while the technician's calibrated hand-held probe reads 34.5°C, the physical probe wins every single time until the digital channel is proven, re-calibrated, and accepted under a forced-failure test.

## Who This Is For

The person on the hook is not the systems integrator who pulled the shielded twisted-pair cable or installed the telemetry collector. The person on the hook is the operational lead who will be asked at 08:00 why a technician was woken at 02:30, or—far worse—why nobody was woken while an inverter on UPS Bus B quietly cooked its DC filter capacitors until the busway tripped.

That person may sit in central facility engineering, in the Enterprise Command Center (ECC), or on the shift operations desk. This book does not split rules by corporate department. A dry-contact float switch on a catch basin and an error log from a high-voltage breaker relay are both operational points. They do not get different definitions of truth.

You do not need a commercial software certification to apply these rules. If your organization manages incidents through ITIL, ISO/IEC 20000, or a proprietary Computerized Maintenance Management System (CMMS), cite that standard's edition in your site operating file. This book establishes the physical, mathematical, and procedural boundaries that determine what the monitoring software is allowed to do before it touches a human nerve.

## What You May Copy

You may copy the Master Point Sheet headings from Chapter 16 and `sheets/point.md` into your site configuration management database. You may not copy proprietary vendor code, proprietary detector weighting factors, or customer-specific telemetry point lists into a public document.

Do not attach false mathematical precision to an uncalibrated system. If you have not executed an empirical, counted benchmark test of true positives, false positives, true negatives, and false negatives under live transient conditions, you do not have an "AI anomaly detection accuracy rate." You have an unvalidated algorithm, and this book will not allow you to use it to wake an on-call engineer.

## Decisions to Record

- The exact operational decision this screen is permitted to support, stated in one unambiguous sentence.
- The specific points you will mute and keep silent until their Point Sheet is completely audited.
- The named individual who holds the exclusive authority to promote a software alert into a production incident.

## Quantitative Telemetry Governance and Signal Integrity Architecture

In a modern hyperscale or colocation data center, a single 20 MW facility exposes between $45,000$ and $120,000$ hardware and software monitoring points across its Building Management System (BMS), Electrical Power Monitoring System (EPMS), Generator Supervisory Control and Data Acquisition (SCADA), and Liquid Coolant Distribution Unit (CDU) controllers. When an unvetted monitoring screen is allowed to page on-call engineers directly from raw register thresholds—without clock synchronization, quality bitmask filtering, hysteresis deadbands, or topology suppression—the control room experiences two fatal failure modes:
1. **The Silent Green Lie**: A protocol gateway freezes and repeats its last cached value (`34.8°C`), displaying a calm green tile while the physical CDU pump is cavitating at `68.0°C`.
2. **The Cascading Alarm Storm**: A single upstream medium-voltage feeder trip triggers $1,400$ downstream low-voltage, PDU, and CRAH loss-of-power pages within $3$ seconds, blinding the shift operator to the root-cause breaker.

| Telemetry Governance Gate | Mathematical / Protocol Requirement | Operational Failure Prevented | Chapter Reference |
| :--- | :--- | :--- | :--- |
| **1. Point Tuple Completeness** | $P = \{V, \, t_{\text{UTC}}, \, \text{URI}_{\text{source}}, \, Q_{\text{mask}}\}$ | Anonymous or un-timestamped register values on HMI | Chapters 1 & 2 |
| **2. Clock Synchronization** | PTP IEEE 1588v2 ($|\Delta t| \le 1\,\text{ms}$) / NTP ($\le 10\,\text{ms}$) | Inverted causal ordering in post-trip Sequence of Events (SOE) | Chapter 3 |
| **3. Quality Bitmask Separation** | Explicit state machine: `0x00` Good, `0x40` Uncertain/Stale, `0x80` Bad | Rendering stale or disconnected sensors as normal green tiles | Chapter 4 |
| **4. Hysteresis & Dwell Filter** | Trigger at $V \ge T_{\text{high}}$ for $t \ge t_{\text{dwell}}$; clear at $V \le T_{\text{high}} - \Delta H$ | Chattering alarm floods from turbulent sensor noise | Chapter 5 |
| **5. Topological Suppression** | Parent-child directed acyclic graph ($G = (V, E)$) root-cause masking | $1,000+$ child alerts burying the primary breaker trip | Chapter 8 |
