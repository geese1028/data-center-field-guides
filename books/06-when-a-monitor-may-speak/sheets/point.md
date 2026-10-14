# The Master Point Sheet

The Master Point Sheet is the legal, operational, and technical contract between a physical instrument and the operational staff of the data center.
Copy these headings into the site file or shift configuration database. One sheet per point that might wake a person. A blank line is a part of the point you have not managed.

---

## 1. Point Identification & Hardware Topology

- **Human-Readable Diagram Tag**: `___________________________________________`
- **Functional Description**: `_______________________________________________`
- **Subsystem Category**: `[ELECTRICAL / HVAC / LIQUID CDU / FIRE / LIFE SAFETY]`
- **Point Kind**: `[POLLED / PUSHED / TRAP / LOG LINE / CALCULATED / CONTACT]`
- **Hardware Source URI**: `___________________________________________________`
- **P&ID / SLD Drawing Reference Number**: `___________________________________`
- **Physical Wire / Terminal Block ID**: `_____________________________________`
- **Engineering Units**: `[°C / kPa / bar / LPM / V / A / kW / Discrete]`
- **Scaling Multiplier & Ingestion Layer**: `_________________________________`
- **Single Permitted Sentence This Point Supports**:
 > *"This point is authorized to support the operational claim that: ____________________________________________________________________"*

---

## 2. Temporal & Quality Integrity

- **Configured Polling / Push Interval (T_poll)**: `_____ Seconds`
- **Time Synchronization Standard**: `[PTP IEEE 1588 / NTP Stratum-1 / IRIG-B]`
- **Timestamp Location**: `[EDGE TRANSDUCER (t_meas) / DATABASE INGESTION]`
- **Stale Timeout Constant**: `K_stale = 3` (Transitions to `STALE` at: `_____ s`)
- **Visual Presentation of Missing Data**: `[DISCONTINUOUS GAP ENFORCED: Y / N]`
- **Forced-Failure Test Executed**: `[YES / NO]`
 - Execution Date & Timestamp: `_____________________________________________`
 - Observed Reaction: `[PASSED: FLIPPED TO STALE & QUENCHED / FAILED: CACHED]`
- **Quality Bitmask Supported**: `[0x00=GOOD, 0x01=STALE, 0x02=UNCERTAIN, 0x04=BAD]`

---

## 3. Thresholds, Deadband, and Filtering

- **High-High (HH) Trip Threshold**: `_______` (Dwell Duration: `_____ s`)
- **High Alarm (H) Threshold**: `_______` (Dwell Duration: `_____ s`)
- **Low Alarm (L) Threshold**: `_______` (Dwell Duration: `_____ s`)
- **Low-Low (LL) Trip Threshold**: `_______` (Dwell Duration: `_____ s`)
- **Hysteresis Deadband Offset (Δ_deadband)**: `_______ Units`
 - Calculated Alarm Reset Line: `_______`
- **Anti-Flap Quarantine Trigger**: `4 transitions in 10 minutes`
- **Quarantine Action**: `Mute audible sirens, block SMS, log to maintenance queue`

---

## 4. Human Governance & Paging

- **Authorized Operational Owner**: `__________________________________________`
- **Designated Deputy Role**: `________________________________________________`
- **Human Promotion Authority**: `[LICENSED DUTY MANAGER ONLY]`
- **Permitted Paging Destinations**: `[FIVE-LINE PAGER / SMS GATEWAY / NONE]`
- **Emergency Action Citing Approved EOP**:
 - EOP Document Number: `___________________________________________________`
 - First Safe-State Directive: `____________________________________________`

---

## 5. Lifecycle Authorization Sign-Off

- **Commissioning Lead Signature**: `________________________________________`
- **Duty Manager Signature**: `_____________________________________________`
- **Approval Date & Expiration Audit Date**: `_______________________________`
