# 16. The Master Point Sheet

The Master Point Sheet is the legal, operational, and technical contract between a physical instrument and the operational staff of the data center.

Copy the headings below into your facility's configuration management database or printed turnover binder. **One sheet per critical point.**

| **MASTER POINT SHEET LEDGER** |
| :--- |
| [SECTION 1] HARDWARE IDENTITY & TOPOLOGY |
| • Tag & Human Name → TT-CDU-01-TCS-SUP (Secondary Supply Temp) |
| • Kind of Point → Polled Analog Input (Modbus TCP) |
| • Hardware Source URI → modbus://cdu-01-gateway/slave-01/reg-40102 |
| • Engineering Unit → °C (Scale factor: 0.01 applied at ingestion) |
| • Physical Drawing Ref → P&ID Drawing PID-M-CDU-001 Rev 4 |
| [SECTION 2] TIME & COMMUNICATION INTEGRITY |
| • Polling Interval → 1.0 Second (Expected continuous stream) |
| • Timing Source → PTP IEEE 1588v2 (Stratum-1 GPS Antenna) |
| • Timeout Multiplier → K_stale = 3 (Fails to STALE at t > 3.0s) |
| • Forced-Failure Status → PASSED (Tested: 2026-10-10 by Commissioning) |
| [SECTION 3] SIGNAL FILTERING & THRESHOLDS |
| • High-High Trip (HH) → 36.0°C (Dwell: 5.0s \| Automatic Chiller Stage) |
| • High Alarm (H) → 32.0°C (Dwell: 15.0s \| SLA Warning) |
| • Hysteresis Deadband → Delta-H = 2.0 K (Reset Line: 30.0°C) |
| • Anti-Flap Quarantine → 4 toggles in 10 min -> Latch & Mute |
| [SECTION 4] GOVERNANCE & PROMOTION |
| • Promotion Authority → Licensed Duty Manager ONLY |
| • Emergency Paging → Five-Line Format to Lead Mechanical Engineer |
| • Operational Owner → Thomas Miller (Lead Mechanical Engineer) |

![The Master Point Sheet and Audit Lifecycle](../figures/fig-07-master-point-sheet-and-audit-lifecycle.png)

A blank line on the Point Sheet represents an unverified parameter, a potential source of false alarms, and an operational vulnerability. If a point cannot fill every line on this sheet, **it is silent**. It may be stored; it may not page.

---

## The Master Point Sheet Specification

### 1. Point Identification & Hardware Topology
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

### 2. Temporal & Quality Integrity
- **Configured Polling / Push Interval (T_poll)**: `_____ Seconds`
- **Time Synchronization Standard**: `[PTP IEEE 1588 / NTP Stratum-1 / IRIG-B]`
- **Timestamp Location**: `[EDGE TRANSDUCER (t_meas) / DATABASE INGESTION]`
- **Stale Timeout Constant**: `K_stale = 3` (Transitions to `STALE` at: `_____ s`)
- **Visual Presentation of Missing Data**: `[DISCONTINUOUS GAP ENFORCED: Y / N]`
- **Forced-Failure Test Executed**: `[YES / NO]`
 - Execution Date & Timestamp: `_____________________________________________`
 - Observed Reaction: `[PASSED: FLIPPED TO STALE & QUENCHED / FAILED: CACHED]`
- **Quality Bitmask Supported**: `[0x00=GOOD, 0x01=STALE, 0x02=UNCERTAIN, 0x04=BAD]`

### 3. Thresholds, Deadband, and Filtering
- **High-High (HH) Trip Threshold**: `_______` (Dwell Duration: `_____ s`)
- **High Alarm (H) Threshold**: `_______` (Dwell Duration: `_____ s`)
- **Low Alarm (L) Threshold**: `_______` (Dwell Duration: `_____ s`)
- **Low-Low (LL) Trip Threshold**: `_______` (Dwell Duration: `_____ s`)
- **Hysteresis Deadband Offset (Δ_deadband)**: `_______ Units`
 - Calculated Alarm Reset Line: `_______`
- **Anti-Flap Quarantine Trigger**: `4 transitions in 10 minutes`
- **Quarantine Action**: `Mute audible sirens, block SMS, log to maintenance queue`

### 4. Human Governance & Paging
- **Authorized Operational Owner**: `__________________________________________`
- **Designated Deputy Role**: `________________________________________________`
- **Human Promotion Authority**: `[LICENSED DUTY MANAGER ONLY]`
- **Permitted Paging Destinations**: `[FIVE-LINE PAGER / SMS GATEWAY / NONE]`
- **Emergency Action Citing Approved EOP**:
 - EOP Document Number: `___________________________________________________`
 - First Safe-State Directive: `____________________________________________`

### 5. Lifecycle Authorization Sign-Off
- **Commissioning Lead Signature**: `________________________________________`
- **Duty Manager Signature**: `_____________________________________________`
- **Approval Date & Expiration Audit Date**: `_______________________________`

## Complete Master Point Sheet Register Schema

Every critical alarm point authorized to wake an engineer or trigger an automated control action must be registered in the site **Master Point Sheet** with all twelve mandatory columns populated and verified:

| Field Column | Engineering Example (`CDU-02-DP-SUP`) | Validation Method at Commissioning |
| :--- | :--- | :--- |
| **1. Canonical Point Tag ID** | `HALLA.CDU02.SEC.DP_MANIFOLD` | Matches P&ID tag and physical phenolic label |
| **2. Physical Sensor & Range** | Piezoresistive DPT, $0\text{--}250\,\text{kPa}$ ($4\text{--}20\,\text{mA}$) | Calibrated loop injection at $4, 12, 20\,\text{mA}$ |
| **3. Protocol & Register Map** | Modbus TCP `10.20.4.12:502`, Holding Reg `40112` (`FLOAT32_ABCD`) | Verified byte order against local gauge reading |
| **4. Time Sync Source** | IEEE 1588v2 PTP Grandmaster `GM-01` ($\pm 1\,\text{ms}$) | Source timestamp preserved end-to-end |
| **5. Polling & Stale Timeout** | Poll $t_{\text{poll}} = 1.0\,\text{s}$; Stale timeout $t_{\text{stale}} = 3.0\,\text{s}$ | Tested by pulling Ethernet patch cord |
| **6. Threshold, Dwell & Deadband** | Low Warn: $\le 85\,\text{kPa}$ ($t_d = 5\,\text{s}, \Delta H = 4\,\text{kPa}$) | Verified via ramped pressure injection |
| **7. Parent Dependency Tag** | `HALLA.CDU02.PUMP_STATUS_RUN` | Child alert suppressed when CDU is intentionally stopped |
| **8. Linked EOP / Action ID** | `EOP-LIQ-04: Secondary Loop Low Differential Pressure` | Included verbatim in outgoing pager payload |
