# 16. The Master Point Sheet

The Master Point Sheet is the legal, operational, and technical contract between a physical instrument and the operational staff of the data center.

Copy the headings below into your facility's configuration management database or printed turnover binder. **One sheet per critical point.**

```
+-----------------------------------------------------------------------------+
| MASTER POINT SHEET LEDGER |
| |
| [SECTION 1] HARDWARE IDENTITY & TOPOLOGY |
| • Tag & Human Name --> TT-CDU-01-TCS-SUP (Secondary Supply Temp) |
| • Kind of Point --> Polled Analog Input (Modbus TCP) |
| • Hardware Source URI --> modbus://cdu-01-gateway/slave-01/reg-40102 |
| • Engineering Unit --> °C (Scale factor: 0.01 applied at ingestion) |
| • Physical Drawing Ref --> P&ID Drawing PID-M-CDU-001 Rev 4 |
| |
| [SECTION 2] TIME & COMMUNICATION INTEGRITY |
| • Polling Interval --> 1.0 Second (Expected continuous stream) |
| • Timing Source --> PTP IEEE 1588v2 (Stratum-1 GPS Antenna) |
| • Timeout Multiplier --> K_stale = 3 (Fails to STALE at t > 3.0s) |
| • Forced-Failure Status --> PASSED (Tested: 2026-10-10 by Commissioning) |
| |
| [SECTION 3] SIGNAL FILTERING & THRESHOLDS |
| • High-High Trip (HH) --> 36.0°C (Dwell: 5.0s | Automatic Chiller Stage) |
| • High Alarm (H) --> 32.0°C (Dwell: 15.0s | SLA Warning) |
| • Hysteresis Deadband --> Delta-H = 2.0 K (Reset Line: 30.0°C) |
| • Anti-Flap Quarantine --> 4 toggles in 10 min -> Latch & Mute |
| |
| [SECTION 4] GOVERNANCE & PROMOTION |
| • Promotion Authority --> Licensed Duty Manager ONLY |
| • Emergency Paging --> Five-Line Format to Lead Mechanical Engineer |
| • Operational Owner --> Thomas Miller (Lead Mechanical Engineer) |
+-----------------------------------------------------------------------------+
```

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
