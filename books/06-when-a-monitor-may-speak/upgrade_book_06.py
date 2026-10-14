#!/usr/bin/env python3
"""
Full text upgrade generator for Book 06: When a Monitor May Speak
Author: Tristan (Data Center Field Guides)
"""

from pathlib import Path

ROOT = Path("/Users/geese/Downloads/book/books/06-when-a-monitor-may-speak")
CHAP = ROOT / "chapters"
SHEET = ROOT / "sheets"

chapters = {}

chapters["00-how-to-use.md"] = """# 0. How to Use This Book

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

```
+-----------------------------------------------------------------------------+
|                       OPERATIONAL TELEMETRY PIPELINE                        |
|                                                                             |
|  [PHYSICAL SENSOR]  4-20mA / RTD / Contact / CT / PT Transducer             |
|         |                                                                   |
|  [POINT INGESTION]  Value + UTC Timestamp (PTP/NTP) + Source URI + Quality  |
|         |                                                                   |
|  [QUALITY GATE]     Quality Bitmask == GOOD (0x00)?                         |
|         |           --> NO: Quench alarming; flag STALE/FAULT telemetry     |
|         |           --> YES: Pass to Signal Processing Filter               |
|         |                                                                   |
|  [SIGNAL FILTER]    Apply Analog Deadband Hysteresis (Delta-H)              |
|         |           Evaluate Continuous Dwell Window (t >= t_dwell)         |
|         |           Anti-Flap Quarantine Engine (N_toggles >= 4 in 10 min)  |
|         |                                                                   |
|  [ALARM STORM MASK] Topology-Aware Parent-Child Dependency Suppression      |
|         |           Upstream breaker trip mutes downstream symptom alarms   |
|         |                                                                   |
|  [HUMAN GATEWAY]    An Alert is NOT an Incident!                            |
|         |           Only designated Duty Manager may promote based on:      |
|         |           (1) SLA breach, (2) Life safety, (3) Redundancy loss    |
|         |                                                                   |
|  [THE 5-LINE PAGE]  Time, Point & Path, Line, Person Woken, First Look/Stop |
+-----------------------------------------------------------------------------+
```

![Anatomy of an Operational Point & Quality Bitmask](../figures/fig-01-point-anatomy-and-quality-flag.png)

A monitor that disagrees with a walked physical measurement does not win simply by being automated. When the digital screen reports that a CDU secondary loop is operating at $28.0^\circ\text{C}$ while the technician's calibrated hand-held probe reads $34.5^\circ\text{C}$, the physical probe wins every single time until the digital channel is proven, re-calibrated, and accepted under a forced-failure test.

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
"""

chapters["01-point.md"] = """# 1. What a Point Must Have

A point is not a colorful widget, a sparkline, or a text label on an operator workstation. A point is an immutable data structure composed of four indispensable elements:

$$P = \{ V, \, t_{\text{UTC}}, \, \text{URI}_{\text{source}}, \, Q \}$$

Where:
- $V$ is the measured engineering value (Float64, Boolean, or Discrete Enum).
- $t_{\text{UTC}}$ is the synchronized UTC timestamp with millisecond resolution.
- $\text{URI}_{\text{source}}$ is the physical hardware origin path down to the terminal block.
- $Q$ is the quality bitmask certifying the integrity of the signal.

```
+-----------------------------------------------------------------------------+
|                      THE FOUR PILLARS OF A POINT                            |
|                                                                             |
|  [1. VALUE]         Float64 / Boolean / Discrete State                      |
|                     • Strictly defined engineering units (°C, kPa, LPM, A)  |
|                     • Scaling applied once at ingestion; raw counts logged  |
|                                                                             |
|  [2. TIMESTAMP]     UTC Timestamp synchronized via PTP / NTP Stratum-1      |
|                     • Source generation time, NOT database arrival time     |
|                     • Sub-millisecond resolution for electrical SOE events  |
|                                                                             |
|  [3. SOURCE PATH]   Immutable Physical Hardware Address                     |
|                     • modbus://cdu-04/reg-40102 or bacnet://bms-pod3/ai-14  |
|                     • Fully decoupled from UI display labels                |
|                                                                             |
|  [4. QUALITY MASK]  Hardware & Communication Status Bitmask                 |
|                     • 0x00 = GOOD (Verified fresh and valid)                |
|                     • 0x01 = STALE (Missed polling intervals; t > 3*T_poll) |
|                     • 0x02 = UNCERTAIN (Out of calibration range)           |
|                     • 0x04 = BAD / FAULT (Wire break, short, CRC failure)   |
+-----------------------------------------------------------------------------+
```

![Anatomy of an Operational Point & Quality Bitmask](../figures/fig-01-point-anatomy-and-quality-flag.png)

Without the timestamp, you cannot distinguish an instantaneous physical change from an echo of the last good reading. Without the physical source path, you cannot distinguish a direct physical transducer from a software calculation that consumed five other unverified inputs. Without the quality mark, a communication timeout or a severed RS-485 cable will dress itself as a perfectly calm, steady horizontal line.

If any of the four elements is missing or corrupted, the point is **SILENT**.
It may be archived to disk for diagnostic debugging. It may never trigger an audible horn, page an on-call engineer, close an active incident ticket, or populate a contractual capacity ledger. Silence is not a failure of the physical plant; silence is the mandatory operational quarantine of an unverified data point.

## The Operational Taxonomy of Points

Every data point entering the facility monitoring fabric must be classified into its precise structural category:

1. **Polled Points**: An active request-response inquiry (e.g., Modbus RTU/TCP read holding registers, SNMP GET requests). The supervisory engine queries the device, and the device responds or times out. Silence following a scheduled poll is a communication failure ($Q = \text{STALE}$); it is not proof that the plant is resting in a safe state.
2. **Pushed Points**: Asynchronous or periodic telemetry transmitted autonomously by an edge controller (e.g., MQTT publish, OPC UA subscription, syslog datagrams). A pushed point requires an explicit heartbeat specification: if the edge controller transmits only on value change, a periodic heartbeat message must be mandated. Without a heartbeat, prolonged silence cannot be distinguished from a crashed CPU.
3. **Unsolicited Traps / Exceptions**: An asynchronous alert declaring that an internal threshold was crossed (e.g., SNMP trap, BACnet Change-of-Value notification). A trap is an historical claim about a past state transition; it is not a continuous measurement of the state right now. A trap delayed in network transit is an old story. Never plot an unsolicited trap as a real-time analog trend.
4. **Calculated / Synthetic Points**: A mathematical transformation derived from other base points (e.g., plate heat exchanger approach temperature $\Delta T_{\text{approach}} = T_{\text{TCS, supply}} - T_{\text{FWS, supply}}$, total hall power $P_{\text{total}} = \sum P_{\text{PDU}}$, or room average temperatures). A calculated point is never a physical sensor. Every synthetic point must declare its exact mathematical formula and constituent input tags. If any single input tag forfeits its `GOOD` quality flag, the calculated point immediately drops to `BAD` or `UNCERTAIN`.
5. **Discrete Contact States**: A binary open/closed or energized/de-energized circuit (e.g., auxiliary dry contact on a circuit breaker, optical float switch on a leak basin). A contact is an instantaneous electrical state; it is not a proxy for fluid flow, cooling capacity, or thermal performance. A closed breaker contact does not prove that current is flowing through the busbar.

## The Name Is Not the Source

Never confuse a user interface tag with a physical hardware address.

A label that reads *"Secondary Loop Supply Temperature"* is a cosmetic alias written for human operators. Platforms change, database schemas are refactored, and graphical screens are rebuilt during upgrades. The immutable hardware source path must be recorded down to the physical wiring layer:

$$\text{modbus://cdu-04-rtu/slave-01/reg-40102} \quad \longrightarrow \quad \text{CDU-04 TCS Supply RTD (PT100 Channel A)}$$

The site configuration management database must maintain a rigorous three-column translation dictionary:
1. **Hardware Source URI**: Protocol, controller network address, register/object ID, and physical terminal pin.
2. **Engineering P&ID / SLD Tag**: The exact alphanumeric tag appearing on the certified construction drawings (e.g., `TT-CDU-101A`).
3. **Engineering Units & Scaling**: Physical unit ($\text{kPa}$, $^\circ\text{C}$, $\text{LPM}$, $\text{kW}$) and the single mathematical multiplier applied at ingestion.

If a point's hardware address cannot be traced directly to a terminal block on a verified schematic, the point is an unmapped orphan. It does not speak.

## Scaling Applied Once

Engineering scale factors must be applied exactly once in the data ingestion pipeline, and that location must be documented in writing.

A raw 16-bit unsigned integer value of `2845` read from a Modbus register representing $28.45^\circ\text{C}$ requires a scale multiplier of $0.01$. If the field RTU applies the scaling factor and transmits `28.45`, and the central SCADA collector subsequently applies the same $0.01$ multiplier, the console displays $0.28^\circ\text{C}$, triggering an immediate false Low-Temperature freeze alarm.

Conversely, if an edge gateway strips the decimal scaling and the central platform fails to apply it, the system displays $2845^\circ\text{C}$, triggering a High-High emergency trip.

The immutable rule of data scaling is: **Store the raw integer counts in the telemetry archive alongside the engineering conversion formula.** Never overwrite the raw transducer telemetry with a transformed value. Overwriting raw sensor data destroys the audit trail needed for forensic root-cause analysis following a catastrophic plant transient.

## Decisions to Record

- The physical hardware source URI, engineering P&ID tag, and verified unit for every active point.
- The single software layer where scaling multipliers and calibration offsets are applied.
- The mathematical formula and constituent input dependencies for every calculated synthetic point.
- The explicit rule declaring that any point lacking a verified hardware path or quality mark remains silent.
"""

chapters["02-accept.md"] = """# 2. Accept the Source Before It Speaks

A data stream from a new monitoring system, a third-party gateway, or a refurbished switchgear line-up is guilty until proven innocent. Never allow a new point to sound control room alarms, page on-call engineers, or populate contractual SLA reports based on a successful vendor demonstration.

```
+-----------------------------------------------------------------------------+
|                        POINT ACCEPTANCE GATEWAY                             |
|                                                                             |
|  [STAGE 1] Physical Loop Verification (Calibrated source applied at probe)  |
|      |                                                                      |
|  [STAGE 2] Full-Scale & Zero-Scale Range Check (0% / 50% / 100% calibration)|
|      |                                                                      |
|  [STAGE 3] The Forced-Failure Test (Physically sever wire / kill power)     |
|      |     • PASS: Console transitions to STALE / FAULT within 3x interval  |
|      |     • FAIL: Console holds last value or stays green -> REJECTED      |
|      |                                                                      |
|  [STAGE 4] Dwell & Deadband Functional Validation under simulated noise     |
|      |                                                                      |
|  [STAGE 5] Master Point Sheet Signed by Duty Manager & Commissioning Lead   |
+-----------------------------------------------------------------------------+
```

![The Master Point Sheet and Audit Lifecycle](../figures/fig-07-master-point-sheet-and-audit-lifecycle.png)

A point is accepted into production operations only after it has survived the **Forced-Failure Test**. If a monitoring channel cannot detect and correctly report its own physical death, it is an operational hazard that will mislead technicians during a crisis.

## The Physical Loop Calibration

Before a software point is connected to an alarm rule, the complete end-to-end analog loop must be physically verified:
1. **Zero-Scale Verification**: Inject $4.00\,\text{mA}$ (or $0.0\,\text{V}$) at the sensor transmitter terminals using a calibrated precision current loop calibrator (e.g., Fluke 789). Verify that the SCADA console displays exactly $0.0\%$ of scale (e.g., $0.0\,\text{bar}$ on a $0 - 10\,\text{bar}$ pressure transducer) within $\pm 0.25\%$ span accuracy.
2. **Mid-Scale Verification**: Inject $12.00\,\text{mA}$. Verify that the console displays exactly $5.00\,\text{bar}$.
3. **Full-Scale Verification**: Inject $20.00\,\text{mA}$. Verify that the console displays exactly $10.00\,\text{bar}$.

If the console display drifts or exhibits non-linear response across the three points, the loop fails acceptance. Check for common-mode ground loops, unshielded signal cabling running parallel to 480V VFD power conductors, or incorrect analog-to-digital (ADC) conversion gain settings in the programmable logic controller (PLC).

## The Mandatory Forced-Failure Test

The defining test of a monitoring source is not how it behaves when the plant is running smoothly; the defining test is how it behaves when the measurement path is violently destroyed.

With the sensor operating under normal conditions and reporting a valid reading on the central console, execute the Forced-Failure Test:
1. **Physical Disconnect**: Physically unscrew the signal conductor from the analog input terminal block, or disconnect the RS-485 serial communication cable from the gateway.
2. **Start the Stopwatch**: Observe the operator workstation console.
3. **Audit the Console Reaction**:
   - **PASS Criteria**: Within three polling intervals ($t \le 3 \times T_{\text{poll}}$), the display tile must transition from `GREEN` to `GREY` or `AMBER-STRIPED`, the quality bitmask must transition to `STALE (0x01)` or `BAD (0x04)`, the value field must display `COMM_FAULT` or `NAN`, and all downstream automatic threshold alarms must be actively quenched.
   - **FAIL Criteria**: If the console continues displaying the last known good value (e.g., $28.4^\circ\text{C}$) in a healthy `GREEN` color, or if the central database quietly holds that number forward for minutes while the sensor is disconnected, **the point fails acceptance immediately**.

A monitoring platform that holds the last known good value forward during a communication loss is an engine of operational deception. If a cooling loop pipe bursts and severs the communication wire to the pressure sensor, a system that holds the last value will report normal pressure while the server hall floods.

Never accept an explanation from a software vendor that *"the system caches the last value to prevent visual flickering on the dashboard."* Caching an unverified value during a communication failure is not UI smoothing; it is a structural failure of monitoring integrity.

## Digital Network Loop Validation

For digital fieldbuses (BACnet/IP, Modbus TCP, OPC UA, SNMP):
- Audit the communication network round-trip time (RTT). The 99th percentile latency must remain strictly below $100\,\text{ms}$.
- Verify packet error rates and CRC checksum rejections. If serial CRC errors exceed $0.1\%$ of total polling requests, the communication channel is physically compromised by electrical noise or improper bus termination resistors ($120\,\Omega$ end-of-line resistors missing).
- Verify slave controller address uniqueness. Duplicate Modbus slave IDs or colliding BACnet Device Object Identifiers will cause alternating telemetry packets from two different physical machines to interleave into a single database trend, creating wild, impossible oscillations.

## Decisions to Record

- The physical calibration certificate numbers and calibration dates for all test instruments used during loop verification.
- The exact execution timestamp and observed console reaction for the Forced-Failure Test.
- The measured communication round-trip latency and CRC error rate across digital fieldbuses.
- Formal sign-off on the Master Point Sheet authorizing the point to transition from Commissioning Quarantine into Active Production.
"""

chapters["03-clock.md"] = """# 3. The Clock

In mission-critical data center operations, time is not a cosmetic label formatted for human readability; time is the primary coordinate of physical causality.

$$\Delta t = t_2 - t_1$$

If the clock on your Electrical Power Monitoring System (EPMS) drifts by even two seconds relative to the Building Management System (BMS), cause and effect will be mathematically inverted during post-incident forensics. A chiller electrical trip that caused a primary cooling flow collapse will appear in the combined logs as a cooling flow collapse that magically caused an upstream electrical trip three seconds before the breaker opened.

```
+-----------------------------------------------------------------------------+
|                  TIME SYNCHRONIZATION ACCURACY ENVELOPE                     |
|                                                                             |
|  Protocol / Standard   Synchronization Precision   Target Subsystems        |
|  --------------------  --------------------------  -----------------------  |
|  IEEE 1588v2 (PTP)     <= 1.0 Microsecond (1 µs)   Protective Relays, DFRs  |
|  IRIG-B (Hardwired)    <= 10.0 Microseconds (10 µs) MV Switchgear, Breakers |
|  NTP Stratum-1 (GNSS)  <= 1.0 Millisecond (1 ms)   BMS Servers, RTUs, PLCs  |
|  Modbus Serial Polling 1.0 to 5.0 Seconds (UNRATED) Field Sensors (No SOE)  |
+-----------------------------------------------------------------------------+
```

![Sequence of Events and Time Synchronization](../figures/fig-06-sequence-of-events-microsecond-chronology.png)

## Measurement Time vs. Ingestion Arrival Time

Every operational data point entering a database must record two distinct temporal timestamps:
1. **Measurement Timestamp ($t_{\text{meas}}$)**: The precise instant the physical transducer sampled the electrical current, temperature, or pressure at the edge controller.
2. **Ingestion Timestamp ($t_{\text{ingest}}$)**: The instant the central database server received, parsed, and committed the telemetry record to disk.

The difference between the two is the transmission latency skew:

$$\Delta t_{\text{skew}} = t_{\text{ingest}} - t_{\text{meas}}$$

A common architectural failure in cheap monitoring platforms is stamping telemetry exclusively with $t_{\text{ingest}}$ at the database gateway. When network congestion, message queue backlogs, or database disk I/O bottlenecks delay message processing by thirty seconds, all telemetry packets arriving in that delayed burst receive identical ingestion timestamps.

When plotted on a graph, thirty seconds of dynamic physical transients collapse into a single vertical step, obscuring pump ramp-down curves, breaker trip sequences, and pressure shock waves.

Any system used for incident root-cause analysis must timestamp points at the edge transducer source ($t_{\text{meas}}$). Ingestion time ($t_{\text{ingest}}$) is an IT pipeline performance metric; it is not the time the plant changed.

## Sequence of Events (SOE) and Microsecond Resolution

In medium-voltage and low-voltage electrical switchgear, physical circuit breaker clearing events occur on the order of cycles ($16.6\,\text{ms}$ at $60\,\text{Hz}$, $20.0\,\text{ms}$ at $50\,\text{Hz}$):
- A zone-selective interlocking (ZSI) restraint signal travels in $10\,\text{ms}$.
- A high-speed vacuum circuit breaker mechanism parts its primary contacts in $30\,\text{ms}$ to $50\,\text{ms}$.
- An automatic transfer switch (ATS) detects voltage loss and signals generator cranking in $100\,\text{ms}$.

If your electrical monitoring architecture relies on a central SCADA server polling power meters over serial Modbus RTU at 5-second scan intervals, you do not have a Sequence of Events recording system. You have an historical ledger that tells you what already happened five seconds ago.

For critical electrical switchgear and generator paralleling buses, Sequence of Events (SOE) recording must be executed at the protective relay level using **IEEE 1588 Precision Time Protocol (PTP)** or dedicated **IRIG-B** optical timing distribution. Protective relays (e.g., SEL, ABB, Schneider) must latch event timestamps locally in non-volatile memory with **1-millisecond resolution** ($1.0\,\text{ms}$) at the physical auxiliary contact bounce.

## Clock Skew, Drift, and Rejection of Artificial Merges

When auditing an incident involving multiple independent logging systems (e.g., utility revenue meters, mechanical chillers, server operating system syslog servers), verify the time synchronization source of each platform before attempting to correlate events.

If the mechanical chiller plant controller synchronizes via an unsynchronized internal crystal oscillator that drifts by 45 seconds per month, and the electrical switchgear synchronizes via a roof-mounted GPS antenna:
- **Do not average the clocks** to make the charts align aesthetically. Averaging two drifting clocks invents an imaginary third timeline that matches no physical reality.
- **Do not stretch or compress the timeline** using digital interpolation to force breaker trips to line up with water temperature spikes.
- Calculate the mathematically verified offset ($\Delta t_{\text{offset}}$) between the two systems at a known common physical anchor point (e.g., the exact millisecond utility grid power collapsed). Apply that constant offset explicitly as an annotated correction, or state in writing on the incident log: *"Thermal logs and electrical logs cannot be correlated with sub-minute precision due to uncalibrated clock drift."*

An explicit statement of temporal uncertainty is an honest engineering finding. An artificially manipulated chart is a falsification of telemetry evidence.

## Decisions to Record

- The primary synchronization standard (PTP / NTP Stratum-1 / IRIG-B) deployed for each subsystem.
- The verified clock drift tolerance ($\le 1.0\,\text{ms}$ for electrical switchgear, $\le 1.0\,\text{s}$ for thermal BMS).
- The explicit separation between edge measurement timestamp ($t_{\text{meas}}$) and central database ingestion timestamp ($t_{\text{ingest}}$).
- Any observed clock offset between disjoint monitoring databases documented prior to joint forensic analysis.
"""

chapters["04-quality.md"] = """# 4. Live, Stale, Missing

A monitoring point displayed on an operations workstation console exists in one of three absolute states:
1. **LIVE (0x00)**: The measured value is verified fresh, arrived within its designated polling interval, and originated from a healthy physical transducer.
2. **STALE (0x01)**: The system is displaying an older cached value because newer telemetry packets failed to arrive within the designated timeout window.
3. **MISSING / FAULT (0x04)**: The communication link is severed, the transducer loop is open, or the channel is reporting an unrecoverable electrical error.

```
+-----------------------------------------------------------------------------+
|                          QUALITY BITMASK SPECIFICATION                      |
|                                                                             |
|  Bitmask  Quality State  Operational Capability    Console Presentation     |
|  -------  -------------  ------------------------  -----------------------  |
|  0x00     GOOD (LIVE)    Valid for SLA & Alarms    Standard Green / White   |
|  0x01     STALE          Visible for Trends Only   Amber Stripe (Muted)     |
|  0x02     UNCERTAIN      Engineering Audit Only    Question Mark (?) Icon   |
|  0x04     BAD / FAULT    Quarantined; No Alarms    Grey / Red Border (Comm) |
+-----------------------------------------------------------------------------+
```

![Anatomy of an Operational Point & Quality Bitmask](../figures/fig-01-point-anatomy-and-quality-flag.png)

Never invent a fourth state called "Unknown" and then treat it operationally as if it were Live. A point is Live only when every single verification test passes.

## The Mathematical Definition of Stale

A point transitions from `LIVE` to `STALE` according to a rigid mathematical rule:

$$t_{\text{current}} - t_{\text{last\_good}} > K_{\text{stale}} \times T_{\text{poll}}$$

Where:
- $T_{\text{poll}}$ is the configured polling interval (e.g., $1.0\,\text{s}$ for secondary cooling pressure, $5.0\,\text{s}$ for battery float voltage).
- $K_{\text{stale}}$ is the stale multiplier constant, which must be configured strictly to **$K_{\text{stale}} = 3$**.

If a secondary cooling supply pressure point configured for a 1-second polling interval fails to deliver a valid telemetry packet for more than 3.0 seconds ($t > 3 \times 1.0\,\text{s}$), the point immediately forfeits its `LIVE` status. Its quality flag flips to `STALE (0x01)`.

The console must immediately:
- Alter the graphical display from solid green to an amber-striped pattern or muted grey.
- Display the timestamp of the last valid reading ($t_{\text{last\_good}}$) alongside the value; never replace that timestamp with the current time of day.
- **Actively quench all downstream threshold alarm rules.** If the pressure had been hovering near an alarm boundary before communication failed, the system must not fire a false "Low Pressure Alarm." Instead, it raises a single, unambiguous **"Telemetry Loss Defect"** on the communication channel.

A stale point may never be used to close a production incident, verify contractual SLA delivery, prove thermal dwell stability, or populate a capacity allocation ledger. If the sole evidence that a cooling loop stabilized after a pump trip is a flat line from a stale sensor, the incident remains fully open on the Duty Manager's board.

## Missing Is Not Zero

In computational telemetry, zero is a valid physical measurement.
- Zero volts means a busbar is completely de-energized.
- Zero liters per minute means fluid flow has completely ceased.
- Zero degrees Celsius means liquid has reached the freezing point of pure water.

`MISSING` is the total absence of a physical measurement.

A graphical trend engine that drops missing telemetry packets and quietly draws a smooth straight line connecting the surrounding data points has manufactured a physical fiction. By connecting a measurement from 14:00 ($3.5\,\text{bar}$) to a measurement from 14:15 ($3.4\,\text{bar}$) across a 15-minute telemetry dropout, the graph hides the fact that at 14:07 the pressure may have plunged to zero when a bypass valve slammed shut.

Every telemetry charting engine must display a visible, discontinuous gap whenever points are missing. If data was not collected, the graph must show blank white space. Connecting points across a communication void is an operational deception.

## How a Screen Lies While Looking Calm

Facility managers must train operators to recognize the subtle failure modes where a monitoring dashboard appears calm while the underlying plant is burning:
1. **The Frozen Database Cache**: The graphical web tile displays a steady, reassuring reading of $22.4^\circ\text{C}$ in green because the web server's background cache failed to refresh from the SQL database three hours ago.
2. **The Ingestion Timestamp Mask**: The database server continuously updates the record's timestamp every five seconds, creating the appearance of live data, while the field RTU has been hung in an unhandled exception loop since dawn, re-transmitting the same cached memory buffer.
3. **The Suppressed Gap Trend**: The trending software automatically interpolates across missing data packets, producing smooth, gentle sine waves that conceal severe hydraulic water hammer spikes.
4. **The Silent Setpoint Override**: A technician temporarily raised an alarm threshold from $28.0^\circ\text{C}$ to $45.0^\circ\text{C}$ during a previous shift to silence a nuisance horn, failing to record the change. The screen remains quiet because the alarm boundary was moved to an impossible limit.

Audit your screens with the Forced-Failure Test. Physically disconnect the sensor. If the screen does not scream within ten seconds, the screen is an operational liability.

## Decisions to Record

- The explicit timeout multiplier ($K_{\text{stale}} = 3$) configured for every polling loop.
- The visual presentation rules enforcing discontinuous gaps across missing data intervals.
- The operational protocol prohibiting stale points from closing active incident tickets.
- The site register of all unverified points currently quarantined under `BAD` or `STALE` quality marks.
"""

chapters["05-line.md"] = """# 5. The Line, the Dwell, the Flap

Drawing an alarm threshold as a single, knife-edge mathematical line on an analog data stream is an engineering design failure.

An analog sensor operating in an industrial environment is naturally subject to electrical noise, thermal turbulence, and pump pressure pulsations. If a high-temperature alarm threshold is set at exactly $30.0^\circ\text{C}$ without filtering, a fluid stream fluctuating between $29.99^\circ\text{C}$ and $30.01^\circ\text{C}$ will cross the threshold twenty times a minute.

This phenomenon—known as **alarm chattering or flapping**—floods the control room console, triggers hundreds of automated text messages, induces acute alarm fatigue, and trains operators to ignore sirens.

```
+-----------------------------------------------------------------------------+
|                      ANALOG THRESHOLDING ARCHITECTURE                       |
|                                                                             |
|  [HIGH-HIGH (HH)]  Trip / EOP Line (e.g. 40.0°C) - Immediate Auto Action    |
|                                                                             |
|  [HIGH ALARM (H)]  SLA Warning Line (e.g. 32.0°C)                           |
|        ^                                                                    |
|        |           HYSTERESIS DEADBAND ZONE (Delta-H = 2.0 K)               |
|        v           Point must fall below 30.0°C before alarm clears         |
|  [RESET LINE]      --------------------------------------------------       |
|                                                                             |
|  [NOMINAL]         Normal Operating Setpoint (e.g. 25.0°C)                  |
|                                                                             |
|  [LOW ALARM (L)]   Condensation Risk Line (e.g. 18.0°C)                     |
+-----------------------------------------------------------------------------+
```

![Thresholding Dynamics: Deadband Hysteresis and Dwell Filtering](../figures/fig-02-threshold-deadband-and-dwell-filter.png)

To prevent alarm chatter, every analog monitoring point must implement three mathematical filtering layers:
1. **Hysteresis Deadbands ($\Delta_{\text{deadband}}$)**
2. **Continuous Dwell Time Windows ($t_{\text{dwell}}$)**
3. **Anti-Flap Quarantine Envelopes ($N_{\text{flap}}$)**

## The Mathematics of Hysteresis Deadbands

An alarm threshold must possess distinct activation and deactivation boundaries.

For a High Alarm condition ($T_{\text{high}}$):
- **Activation Rule**: The alarm state transitions from `NORMAL` to `ALARM` only when the measured value exceeds the upper threshold:

$$V(t) \ge T_{\text{high}}$$

- **Deactivation (Reset) Rule**: The alarm state does not return to `NORMAL` when the value dips back below $T_{\text{high}}$. The alarm remains latched until the value drops below the threshold minus the hysteresis deadband:

$$V(t) \le T_{\text{high}} - \Delta_{\text{deadband}}$$

Where:
- $\Delta_{\text{deadband}}$ is the configured hysteresis offset (typically $1.0\,\text{K}$ to $2.0\,\text{K}$ for temperature loops, and $0.2\,\text{bar}$ to $0.5\,\text{bar}$ for hydraulic loops).

If the High Alarm is configured at $32.0^\circ\text{C}$ with a deadband of $2.0\,\text{K}$, the alarm triggers when temperature reaches $32.0^\circ\text{C}$. As the cooling system responds and temperature recedes to $31.5^\circ\text{C}$, the alarm **stays active**. It clears only when the temperature drops cleanly below $30.0^\circ\text{C}$ ($32.0 - 2.0$). Hysteresis completely eliminates boundary oscillation.

## The Continuous Dwell Window

A physical parameter must demonstrate that an excursion is sustained, rather than a momentary electrical glitch or transient hydraulic wave, before waking an engineer:

$$\text{Trigger Condition}: \quad \forall t \in [t_0, \, t_0 + t_{\text{dwell}}], \quad V(t) \ge T_{\text{high}}$$

Where:
- $t_{\text{dwell}}$ is the continuous dwell duration.

The value of $t_{\text{dwell}}$ must be carefully matched to the physical thermal and mechanical inertia of the monitored system:
- **Secondary Cooling Fluid Temperature**: $t_{\text{dwell}} = 10.0\,\text{s}$ to $15.0\,\text{s}$. A 2-second fluid temperature spike caused by a sensor electrical blip does not threaten GPU silicon; a 15-second sustained excursion indicates true heat exchanger starvation.
- **Underfloor Air Plenum Static Differential Pressure**: $t_{\text{dwell}} = 10.0\,\text{s}$. A momentary air pressure dip caused by an operator opening a containment door for four seconds must not sound a low-pressure alarm.
- **Electrical Bus Under-Voltage**: $t_{\text{dwell}} = 0.1\,\text{s}$ to $0.5\,\text{s}$ (100 to 500 ms). Electrical systems possess virtually zero thermal inertia; an undervoltage condition exceeding a few cycles requires immediate protective reaction.

If a point crosses an alarm threshold and recedes prior to satisfying $t_{\text{dwell}}$, the event is archived as a transient log entry; it does not sound an audible horn or dispatch an automated page.

## The Anti-Flap Quarantine Engine

Even with deadbands and dwell delays, a severely degraded sensor—such as an RTD with a loose terminal screw vibrating against a pump frame—can oscillate violently across wide boundaries.

The monitoring engine must implement an automated **Anti-Flap Quarantine Algorithm**:

$$\text{If } N_{\text{transitions}} \ge N_{\text{flap\_max}} \quad \text{within rolling window } W_{\text{flap}}, \quad \text{engage FLAPPING\_LATCH}$$

Standard operational parameters:
- Maximum transitions allowed: $N_{\text{flap\_max}} = 4$ transitions (`NORMAL` $\leftrightarrow$ `ALARM`).
- Rolling evaluation window: $W_{\text{flap}} = 10\,\text{minutes}$.

When a point trips the anti-flap limit:
1. The point transitions into the `FLAPPING_LATCH` state.
2. Control room audible horns, automated SMS gateways, and client SLA portals for this specific point are **instantly muted**.
3. A single, high-priority **"Sensor Flap Defect"** is dispatched to the shift technician's maintenance queue: *"Point CDU-02-T_sup quarantined for excessive state oscillation. Physical wire inspection required."*
4. The analog telemetry values continue logging to disk at full resolution for diagnostic analysis.
5. The point remains quarantined until a technician physically inspects the device and a manager executes a manual unlatch command, or until the sensor demonstrates 60 continuous minutes of zero-alarm stability.

Anti-flap quarantine protects the sanity of operational personnel while maintaining complete technical accountability.

## Decisions to Record

- The explicit numerical deadband ($\Delta_{\text{deadband}}$) assigned to every analog alarm threshold.
- The continuous dwell duration ($t_{\text{dwell}}$) configured per subsystem, justified by thermal/electrical physics.
- The active anti-flap quarantine limits ($N_{\text{flap\_max}} = 4$ in $10\,\text{min}$) enforced on the SCADA server.
- The registry of all points currently held in anti-flap quarantine, with assigned technician names.
"""

chapters["06-alert.md"] = """# 6. An Alert Is Not an Incident

The most destructive operational error an organization can commit is wiring an automated monitoring software alert directly into a contractual client notification pipeline.

An alert is a row in a software database. It is a mathematical statement that a specific telemetry stream crossed a pre-programmed threshold inside a digital controller.

An incident is a business, technical, and legal event. It is an operational state where contractual service delivery has failed, where human safety is endangered, or where plant redundancy has collapsed to an extent that imminent catastrophic failure is probable.

```
+-----------------------------------------------------------------------------+
|                      ALERT VS. INCIDENT GOVERNANCE                          |
|                                                                             |
|  Dimension           Software Alert                Production Incident      |
|  ------------------  ----------------------------  -----------------------  |
|  Origin              Automated SCADA / BMS Engine  Human Operational Command|
|  Volume              Hundreds per week             Rare (Zero is the goal)  |
|  Authority Required  Software algorithm            Licensed Duty Manager    |
|  Client Visibility   Strictly Internal / Muted     Formal Contractual SLA   |
|  Resolution Action   Auto-clear / Sensor tuning    Formal EOP / MOP / RCA   |
+-----------------------------------------------------------------------------+
```

![The Human Escalation Gate: An Alert is Not an Incident](../figures/fig-03-alert-to-incident-escalation-gate.png)

A software dashboard does not hold a pen. A monitoring algorithm does not possess a professional engineering license. Only a qualified human being—specifically the licensed Duty Manager or designated Enterprise Command Center (ECC) Lead—possesses the legal and operational authority to promote an alert into a production incident.

## The Three Promotion Criteria

An operational alert may be promoted to an incident if and only if it satisfies at least one of **The Three Mandatory Promotion Tests**:

### Test 1: Contractual SLA Boundary Excursion
Did the physical condition breach a legally binding parameter defined in the client Master Services Agreement (MSA)?
- Total loss of electrical power to customer IT server racks (either A or B feed in a 2N topology, or both).
- Secondary technology cooling loop supply temperature exceeding contractual envelope ($T_{\text{supply}} > 32.0^\circ\text{C}$) for longer than the contractual rolling average window (e.g., $> 5$ continuous minutes).
- Cold aisle rack intake air temperature exceeding ASHRAE TC 9.9 Class A1 allowable limits ($T_{\text{air}} > 27.0^\circ\text{C}$).

If the event breaches an SLA parameter, it is an immediate **P1 Critical Incident**. The contractual notification clock begins ticking instantly.

### Test 2: Threat to Human Life Safety
Does the condition endanger human personnel working on site?
- Electrical arc-flash, explosion, or switchgear fire.
- Activation of optical smoke detection (VESDA) confirmed across multiple zones.
- Toxic or asphyxiating chemical release (refrigerant leak, battery hydrogen off-gassing, nitrogen purging failure).
- Structural flooding or seismic damage.

If human safety is threatened, it is an immediate **P1 Critical Incident**. Execute the site emergency evacuation procedure immediately.

### Test 3: System Redundancy Collapse ($N-1$ State)
Did the failure eliminate surviving plant redundancy, leaving the facility vulnerable to a single-point failure?
- Trip of 2N Electrical Bus A, forcing 100% of critical load onto surviving Bus B.
- Trip of primary centrifugal chiller in an $N+1$ plant, leaving zero standby cooling capacity.
- Secondary cooling distribution unit (CDU) operating on single-pump bypass due to an electrical VFD failure.

If redundancy has collapsed, it is an immediate **P2 Major Incident**. Redundant capacity must be restored or emergency load shedding initiated before a second failure occurs.

## If None of the Three Tests Pass

If an alert does not breach an SLA, does not threaten human safety, and does not collapse plant redundancy, **it is not an incident**.

An alert reporting that Chiller 3 oil filter differential pressure reached $0.8\,\text{bar}$ (warning threshold) while the chiller continues operating stably with an approach temperature of $1.1\,\text{K}$ is an internal operational maintenance task. It belongs on the shift technician's computerized work-order queue.

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
"""

chapters["07-page.md"] = """# 7. What a Page Must Contain

Waking an on-call engineer at 02:30 in the morning is a severe operational intervention. When a human being is ripped from deep sleep by an emergency pager or phone siren, their cognitive faculties are impaired by sleep inertia for at least five to ten minutes.

If the emergency page consists of a cryptic string of hexadecimal characters, a raw database error dump, a vague corporate slogan, or a five-page automated telemetry report, the engineer will spend crucial minutes trying to decipher what broke.

Every automated emergency page dispatched by a critical monitoring system must fit into **The Five Mandatory Lines**:

```
+-----------------------------------------------------------------------------+
|                          THE FIVE-LINE EMERGENCY PAGE                       |
|                                                                             |
|  LINE 1: EXACT TIME      --> 2026-10-14 02:34:12 UTC (Source measurement t) |
|  LINE 2: POINT & PATH    --> CDU-04 TCS Supply Temp (modbus://cdu-04/40102) |
|  LINE 3: THE VALUE/LINE  --> T = 33.4°C (Exceeded High Alarm Line: 32.0°C)  |
|  LINE 4: PERSON WOKEN    --> Lead Mech Engineer (Shift Roster Tier 1)       |
|  LINE 5: THE FIRST STOP  --> Verify EOP-M-02 (CDU-04 Staging) & Confirm Live|
+-----------------------------------------------------------------------------+
```

![The Human Escalation Gate: An Alert is Not an Incident](../figures/fig-03-alert-to-incident-escalation-gate.png)

If a page cannot deliver those five clean lines, the page must not be transmitted.

## Detailed Breakdown of the Five Lines

1. **Line 1: Exact Measurement Timestamp**:
   The exact UTC time the physical condition was sampled at the edge transducer, including date, minute, and second. Not the time the database server processed the message, and not a relative timestamp like *"5 minutes ago."*
2. **Line 2: Point Name and Hardware Origin Path**:
   The human-readable engineering tag from the mechanical or electrical drawings (`TT-CDU-101A`), followed immediately by the physical hardware address (`modbus://cdu-04/reg-40102`). The engineer must know the exact physical machine to walk toward.
3. **Line 3: The Active Value and the Line It Crossed**:
   The measured engineering value, its units, and the exact threshold that was violated:
   `Measured: 33.4°C | Threshold: 32.0°C (Dwell: 15s verified)`.
   Never transmit a generic message stating *"Temperature Alarm."* The engineer must know whether the value is creeping $0.5\,\text{K}$ over warning, or screaming $15.0\,\text{K}$ over catastrophic trip.
4. **Line 4: The Person Woken and Coverage Tier**:
   The specific individual's name and role from today's active shift roster:
   `Dispatched to: M. Vance (Lead Mechanical) | Roster Shift 2`.
   This eliminates ambiguity over who holds the active response obligation.
5. **Line 5: The First Look and the First Stop (EOP Action)**:
   The immediate, pre-engineered operational directive citing the site Emergency Operating Procedure:
   `Action: Confirm sensor LIVE; Execute EOP-M-02 (CDU Standby Pump Engagement). Hands off controls until safe state confirmed.`
   Do not include speculative diagnostic theories. Name the pre-approved safe-state action.

## What You Must Never Put in a Page

To preserve cognitive clarity and comply with strict information security requirements, never include the following items in an automated page:
- Passwords, API tokens, VPN credentials, or internal SSH connection strings.
- Complete network topology diagrams, internal IP addresses, or customer server hostnames.
- Unfiltered customer application logs, database stack traces, or memory dumps.
- Speculative root-cause hypotheses (e.g., *"We think the vendor broke the valve"*).
- Corporate marketing language, apology statements, or executive reassurances.

## The Mandatory Four-Part Reply

An emergency page is not closed when the engineer acknowledges the notification on their mobile phone. Clicking an "Acknowledge" button in an app simply proves that a finger touched glass; it does not prove the plant is safe.

Within fifteen minutes of receiving the page, the responding engineer must log **The Mandatory Four-Part Reply** into the central operations ledger:
1. **Timestamp Acknowledged**: The exact minute the engineer opened the telemetry console or arrived on the plant floor.
2. **Quality Verification**: Confirmation of whether the telemetry point was still reporting `LIVE` quality when inspected, or if it had dropped to `STALE` or `BAD`.
3. **Physical Reality Observed**: What the engineer saw on the ground (e.g., *"Local analog dial gauge on CDU-04 reads 0.45 MPa; mechanical seal dry; no fluid pooling"*), keeping physical observations strictly separated from speculative guesses.
4. **Escalation / Promotion Verdict**: Whether the event was resolved under standard operating procedures, or promoted to a formal P1/P2 Incident under the three promotion tests.

If the engineer fails to log the four-part reply within the contractual escalation window (typically 15 minutes), the monitoring engine automatically escalates the page to the next senior leader named on the roster.

## Decisions to Record

- The strict Five-Line message format enforced across all automated paging gateways.
- The active paging escalation ladder, defining names, phone numbers, and timeout windows.
- The Four-Part Reply protocol required from every responding engineer.
- The post-shift audit logging every emergency page transmitted and verifying compliance.
"""

chapters["08-many.md"] = """# 8. Many Alerts, One Event

When a major electrical or mechanical failure strikes a hyperscale data center, the supervisory console does not receive a polite, single notification stating *"Transformer 1 Tripped."*

Instead, within a six-second window, the console is hit by an explosive **Alarm Storm** of 500 to 2,000 cascading alarms:
- High-voltage switchgear reports breaker trip.
- 480V distribution boards report under-voltage.
- Uninterruptible power supplies report static bypass out of frequency.
- UPS battery strings report rapid high-rate discharge.
- Central chillers report compressor VFD DC-bus undervoltage shutdown.
- Primary chilled water pumps report loss of flow.
- Hundreds of computer room air handling (CRAH) units report fan failure.
- Thousands of server rack power distribution units report loss of A-feed input voltage.

```
+-----------------------------------------------------------------------------+
|                     TOPOLOGICAL ALARM STORM SUPPRESSION                     |
|                                                                             |
|  [UPSTREAM ROOT EVENT] 35kV Utility Feeder Breaker Trip (Time: T_0)         |
|           |                                                                 |
|           +---> [PARENT NODE] Main Incomer Breaker Open                     |
|           |          |                                                      |
|           |          v                                                      |
|           |     TOPOLOGICAL INGESTION ENGINE: Ingests parent event;         |
|           |     ACTIVELY QUENCHES all downstream dependent symptom alarms:  |
|           |          |                                                      |
|           |          +---x [SUPPRESSED] 480V Substation Under-Voltage       |
|           |          +---x [SUPPRESSED] UPS Transfer to Battery (12 units)  |
|           |          +---x [SUPPRESSED] Chiller Compressor Trips (4 units)  |
|           |          +---x [SUPPRESSED] CRAH Fan Low Airflow (32 units)     |
|           |          +---x [SUPPRESSED] Server Rack PDU A-Lost (480 racks)  |
|           |                                                                 |
|           v                                                                 |
|  [CONSOLIDATED DISPLAY] Single P1 Incident Ticket: "Feeder A Incomer Open"  |
|                         Symptom count: 548 suppressed | Surviving: Bus B OK |
+-----------------------------------------------------------------------------+
```

![Topology-Aware Ingestion: Alarm Storm Suppression](../figures/fig-04-alarm-storm-suppression-and-topology.png)

An operator presented with 2,000 screaming alarm banners on five monitors is rendered cognitively blind. The critical root-cause alarm—the tripped utility feeder breaker—is buried on page 18 of the alarm list, while the operator fruitlessly attempts to silence hundreds of secondary fan alarms.

## The Principle of Topological Dependency Masking

A professional data center supervisory engine must implement **Topology-Aware Ingestion**:

$$E_{\text{child}} \prec E_{\text{parent}}$$

If an upstream physical parent node transitions into an unpowered or isolated state, the supervisory engine must **automatically quench and consolidate all downstream child symptom alarms**.

### Core Suppression Rules:
1. **Breaker-Driven Electrical Quenching**:
   When an electrical circuit breaker opens (e.g., `SWG-01-M1`), the monitoring engine identifies all downstream electrical panels, transformers, UPS rectifiers, and PDUs fed from that breaker bus. The system raises a single primary incident for the breaker trip; it mutes and collapses all downstream under-voltage alarms into a collapsible symptom list attached to the parent ticket.
2. **Pump-Driven Hydraulic Quenching**:
   When a primary chilled water pump trips on an electrical fault (`P-01 Status == STOPPED`), the engine immediately quenches the downstream *"P-01 Low Discharge Flow"* and *"P-01 Low Differential Pressure"* alarms. Reporting that an unpowered pump is failing to generate flow is noise. The alarm belongs to the pump motor trip, not the fluid flow.
3. **Chiller-Driven Thermal Quenching**:
   When a central chiller shuts down, downstream chilled water supply temperature alarms for that specific evaporator barrel are correlated directly to the chiller shutdown event.

Topological suppression reduces 500 chaotic alarms into **exactly one actionable incident ticket**.

## Time-Aligned Correlation Windows

Parent-child relationships must be evaluated within a strict, pre-calculated temporal correlation window:

$$\Delta t_{\text{correlation}} \le T_{\text{window}} \quad (\text{typically } 500\,\text{ms to } 2.0\,\text{s})$$

When an upstream electrical event occurs:
- All alarms occurring along that electrical branch within $T_{\text{window}}$ are ingested into the correlation engine.
- The topological root (the highest breaker in the single-line diagram) is designated as the **Root Cause Candidate**.
- The control room horn sounds **exactly once**. It does not re-sound 500 times for every downstream branch breaker. Operators maintain cognitive composure to execute the Emergency Operating Procedure.

## Preserving the Count and the Audit Trail

Suppression does not mean deletion.
Muting downstream symptom alarms on the live operator console must never delete those records from the historical database.

The consolidated incident ticket displayed on the Duty Manager's workstation must display:
- **The Primary Root Event**: `INCIDENT #1049 :: 35kV Feeder A Breaker Trip (09:14:22 UTC)`.
- **The Correlated Symptom Count**: `548 Downstream Alarms Ingested & Collapsed`.
- **The Drill-Down Capability**: A single click allows the engineer to expand the ticket and inspect every individual millisecond timestamp, voltage decay curve, and relay trip flag across all 548 devices.

An operations manager who suppresses alarms by permanently disabling database logging has destroyed the legal and forensic record. An operations manager who uses topological dependency masking presents a clean, actionable screen to the operator while preserving full forensic fidelity in the archive.

## Decisions to Record

- The physical single-line diagrams (SLD) and mechanical P&IDs ingested into the topological correlation engine.
- The exact temporal correlation window ($T_{\text{window}} = 2.0\,\text{s}$) configured for alarm storm collapsing.
- The rule mandating that control room sirens trigger once per topological incident rather than once per symptom.
- The audit verification confirming that all collapsed symptom alarms remain fully inspectable in the database.
"""

chapters["09-window.md"] = """# 9. A Window You Already Opened

The second most common cause of catastrophic data center outages—behind changes called maintenance—is the forgotten alarm suppression window.

When technicians execute maintenance under an approved Method of Procedure (MOP) (e.g., overhauling a centrifugal chiller compressor, replacing a secondary CDU pump seal, or testing an emergency diesel generator), the equipment being serviced will generate continuous, violent alarm excursions.

To prevent these expected maintenance transients from sounding control room horns, triggering automated paging escalation ladders, or falsely penalizing contractual SLA availability metrics, the Duty Manager places the affected equipment points into **Maintenance Window Masking**.

```
+-----------------------------------------------------------------------------+
|                  MAINTENANCE WINDOW GOVERNANCE ENVELOPE                     |
|                                                                             |
|  [PRE-WINDOW GATE]                                                          |
|  • Approved MOP & PTW Attached | CAB Ticket Verified                        |
|  • Explicit Point Mask List (Muting entire plant/hall is strictly forbidden)|
|  • Countdown Timer Initialized (Hard ceiling: e.g. 120 minutes)             |
|                                                                             |
|  [DURING THE WINDOW]                                                        |
|  • Telemetry fully recorded to disk; only horns and paging muted            |
|  • Workstation displays diagonal AMBER WATERMARK on masked screens          |
|  • Physical abnormal state whiteboard updated in central control room       |
|                                                                             |
|  [FAILSAFE WATCHDOG GATE]                                                   |
|  • T - 15 min: Pre-Unmask Warning dispatched to Duty Manager console        |
|  • T = 0 min:  Window EXPIRES; points automatically RE-ARM                  |
|  • Duty Manager must sign physical unmask verification ledger               |
+-----------------------------------------------------------------------------+
```

![Maintenance Window Masking and Failsafe Watchdogs](../figures/fig-05-maintenance-window-masking-matrix.png)

A maintenance mask is a temporary, highly dangerous operational blind spot. If a maintenance window is opened without a hard expiration countdown, or if an engineer forgets to unmask the points when the shift ends, the facility operates in an unmonitored state.

Three days later, when that newly overhauled chiller experiences an oil pump seizure, the monitoring system remains completely silent because the alarm suppression was never removed.

## The Rules of Maintenance Masking

Every maintenance window masking operation must adhere to five mandatory structural constraints:

1. **Explicit Point Scope (No Wildcard Muting)**:
   The MOP must name the exact, individual point tags to be masked (e.g., `TT-CH-02-COND-OUT`, `PT-CH-02-OIL`). Muting an entire mechanical plant, an entire electrical substation, or using wildcard masks (`CH-02-*`) is strictly prohibited. If a technician is servicing the compressor oil pump, the evaporator freeze protection points must remain fully active.
2. **Hard Countdown Timers (No Open-Ended Windows)**:
   Every maintenance mask must possess an immutable, hard expiration timestamp (e.g., `Start: 10:00 UTC | End: 12:00 UTC`). An open-ended maintenance window with no pre-programmed expiration is an operational defect. The SCADA software must reject any mask configuration that lacks an end time.
3. **Telemetry Preserved to Disk**:
   Masking disables control room sirens, automated paging relays, and client SLA portal notifications. Masking **never** stops the logging of raw telemetry to disk. Every pressure pulsation, current spike, and valve transition during the maintenance window must be recorded at full resolution for post-maintenance commissioning review.
4. **Visual Watermarking on the Console**:
   Any workstation screen, mimic diagram, or dashboard displaying a point currently under maintenance masking must display a prominent, impossible-to-ignore visual indicator: a bold, diagonal amber-striped watermark across the tile with the text: `POINT UNDER MOP MASKING - EXPIRATION IN 42 MIN`.
5. **The Physical Whiteboard Interlock**:
   The Duty Manager must physically write the masked equipment tag, the MOP ticket number, and the exact expiration time on the central control room whiteboard before issuing the Permit to Work.

## The Failsafe Watchdog and Auto-Rearm

When the scheduled maintenance window reaches its pre-programmed end timestamp, the monitoring engine **must not silently remain masked**.

The system must execute a **Failsafe Watchdog Sequence**:
- **At $T - 15\,\text{minutes}$**: The central console generates a high-priority yellow warning prompt to the Duty Manager: *"MOP Window for Chiller CH-02 expires in 15 minutes. Prepare for unmasking or submit formal CAB extension."*
- **At $T = 0$ (Expiration)**: The system automatically unmasks all suppressed points and re-arms all alarm rules.
- If the equipment is still opened, unpowered, or in an abnormal operating state when the window expires, **the alarms sound immediately**.

This design forces operational accountability. If the contractor is running behind schedule, they cannot quietly pack their tools and leave the facility in a broken, muted state. The manager must formally review the situation, verify plant safety, and explicitly authorize a window extension.

## Formal Post-Maintenance Unmask Verification

Before a maintenance ticket can be closed, the Duty Manager must execute a formal **Unmask Verification Walk**:
1. Verify that all temporary mechanical bypass hoses, electrical grounding clusters, and Lockout/Tagout (LOTO) padlocks have been removed.
2. Verify that equipment isolation valves have been returned to their normal operating positions and locked/car-sealed.
3. Observe the SCADA console as the equipment is re-energized and operated under live load for a minimum 30-minute dwell period.
4. Verify that all telemetry channels are reporting `LIVE (0x00)` quality with normal operating values.
5. Physically sign the unmasking ledger on the Master Day Sheet, documenting that the plant has returned to a fully monitored, fully redundant operational baseline.

## Decisions to Record

- The explicit registry of all points masked during the shift, linked to approved MOP ticket numbers.
- The hard start and expiration timestamps for every active maintenance window.
- The formal verification that all masked telemetry was recorded to disk at full resolution.
- The signed unmasking ledger confirming that all points were re-armed and verified live under load.
"""

chapters["10-score.md"] = """# 10. A Score Does Not Get a Pen

In modern data center operations, management dashboards and vendor platforms increasingly feature aggregated composite metrics: "Facility Health Scores," "AI Risk Indexes," "PUE Optimality Ratings," or "Predicted Time-to-Failure Scores."

A health score is typically a normalized number from 0 to 100, or a cheerful green-yellow-red circular gauge that attempts to summarize the operational status of an entire multi-megawatt campus into a single executive graphic.

The absolute operational law of data center engineering is: **A score does not get a pen.**

```
+-----------------------------------------------------------------------------+
|                          COMPOSITE SCORE ANATOMY                            |
|                                                                             |
|      0.40 * (Chiller Delta-T)   --> Healthy (Score = 98)                    |
|  +   0.30 * (UPS Efficiency)    --> Healthy (Score = 96)                    |
|  +   0.20 * (Cold Aisle Air)    --> Healthy (Score = 95)                    |
|  +   0.10 * (CDU Pump Vibration)--> CATASTROPHIC FAILURE (Score = 0)        |
|  =========================================================================  |
|      WEIGHTED COMPOSITE SCORE   --> 89.1 / 100 ("EXCELLENT HEALTH" - GREEN) |
|                                                                             |
|  REALITY: CDU Pump mechanical seal has disintegrated; bearing is seizing;   |
|  secondary loop flow is collapsing; GPU cluster will overheat in 2 minutes. |
+-----------------------------------------------------------------------------+
```

A composite score is a mathematical abstraction. It is an opinion created by an algorithm that took forty genuine physical measurements, multiplied each by an arbitrary weighting factor, added them together, and divided by a constant.

A score may be observed as a long-term trending indicator. A score may never wake an on-call engineer, close an incident ticket, authorize an intrusive maintenance window, or—above all—automatically command physical plant equipment.

## The Flaw of Weighted Averages: The Drowning Metric

The fatal flaw of any composite health index is the mathematics of weighted averaging.

Consider an AI compute hall cooled by high-density liquid cooling CDUs. The monitoring software calculates an overall "Cooling Subsystem Health Score" based on a weighted formula:

$$\text{Health Score} = 0.40 \cdot S_{\text{chiller}} + 0.30 \cdot S_{\text{ups}} + 0.20 \cdot S_{\text{crah}} + 0.10 \cdot S_{\text{cdu\_vibration}}$$

During normal operations, every subsystem operates perfectly ($S = 100$), yielding a composite Health Score of $100$.

Now, the mechanical bearing on the primary running secondary CDU pump experiences catastrophic fatigue. The physical vibration transducer detects explosive acceleration ($12.5\,\text{mm/s RMS}$, far above the $4.5\,\text{mm/s}$ destruction threshold). The CDU vibration score plunges instantly to **Zero** ($S_{\text{cdu\_vibration}} = 0$).

The central executive dashboard calculates the new composite score:

$$\text{Health Score} = (0.40 \cdot 100) + (0.30 \cdot 100) + (0.20 \cdot 100) + (0.10 \cdot 0) = 90.0$$

The dashboard presents a radiant green tile reading **90.0 / 100: Plant State Excellent**.

The executive looking at the dashboard sips coffee, completely unaware that sixty seconds later the pump bearing will seize, the pump impeller will shear its drive shaft, secondary coolant flow will halt, and 72 high-density GPU racks will initiate thermal emergency shutdown.

In mission-critical engineering, **critical physical limits are non-linear and non-compensatory**.
You cannot compensate for an exploding pump bearing by having exceptionally cool water in the chiller, any more than a human being can compensate for a stopped heart by having exceptionally healthy kidneys.

## Why a Score May Never Control Equipment

Never allow a closed-loop automated control sequence to execute physical plant actions—such as starting chillers, racking breakers, or opening bypass valves—based on a composite health score or an artificial intelligence machine learning model.

An automated control system must operate exclusively on deterministic, single-variable physical measurements:
- Start Standby Chiller if and only if: `Primary Chilled Water Supply Temp > 15.0°C for continuous t >= 60.0s`.
- Transfer to Battery Power if and only if: `Input Bus AC Voltage < 420V for continuous t >= 16.0ms`.
- Engage Secondary CDU Backup Pump if and only if: `Pump Differential Pressure < 0.6 bar for continuous t >= 3.0s`.

When an automated control sequence acts on a composite score, the physical rationale for equipment switching becomes a black box:
- The chiller starts, but nobody knows which specific parameter triggered the start.
- A bypass valve closes because a machine learning model detected an "anomaly score of 0.84," while the physical flow was completely stable.
- Control loops begin hunting and fighting each other because the weighting factors in the algorithm interact unpredictably during non-linear plant transients.

Control commands belong exclusively to certified, deterministic programmable logic controllers (PLCs) executing readable, auditable ladder logic or function block diagrams. Keep composite scores confined to executive summary slides.

## Decisions to Record

- The explicit rule prohibiting composite health scores from triggering automated control actions or emergency pages.
- The mathematical formula, weighting constants, and input dependencies for every composite score displayed on site.
- The deterministic, single-variable physical threshold criteria governing all automated equipment failovers.
- The protocol requiring operators to audit underlying physical telemetry rather than composite index gauges.
"""

chapters["11-path.md"] = """# 11. A Path Is Not a Cause

When an operational incident occurs, human beings experience an overwhelming psychological urge to connect data points into a narrative.

The monitoring screen displays five red icons:
1. `09:14:00` - Outside air wet-bulb temperature reached $28.5^\circ\text{C}$.
2. `09:14:05` - Chiller CH-02 compressor power surged to $450\,\text{kW}$.
3. `09:14:12` - Secondary CDU supply fluid temperature crept to $31.8^\circ\text{C}$.
4. `09:14:18` - An electrical feeder circuit breaker tripped on Bus B.
5. `09:14:25` - A technician badged through the security door of Switchgear Room 2.

The human mind immediately constructs a story:
> *"The hot outside weather overloaded the chiller, which caused the CDU temperature to rise, which pulled too much power and tripped the circuit breaker right when the technician opened the door."*

This is the narrative fallacy in operational engineering. It confuses temporal proximity and physical topology with physical causation.

```
+-----------------------------------------------------------------------------+
|                          CAUSALITY VS. TOPOLOGY                             |
|                                                                             |
|  PHYSICAL TOPOLOGY (The Path)      --> Physical wires, pipes, and buses     |
|                                        Tells you what COULD interact        |
|                                                                             |
|  TEMPORAL SEQUENCE (The Clock)     --> Order of millisecond arrival         |
|                                        Tells you what happened FIRST        |
|                                                                             |
|  ENGINEERING FORENSICS (The Cause) --> Conservation of energy, metallurgy,  |
|                                        electrical protective relay targets  |
|                                        Tells you WHY it happened            |
+-----------------------------------------------------------------------------+
```

A physical path (the electrical busway, the chilled water piping header, the network cable) tells you where energy and data are capable of flowing. It does not prove that a specific energy transfer caused a failure.

## The Three Tests of Physical Causation

Before an operational review or Root Cause Analysis (RCA) may declare that Event A caused Event B, the hypothesis must pass **The Three Laws of Forensic Causation**:

### Law 1: The Strict Temporal Precedence Law
Event A must precede Event B in true, synchronized source measurement time ($t_{\text{meas}}$):

$$t_{\text{meas}}(A) < t_{\text{meas}}(B)$$

If Event A occurred at `09:14:18.045 UTC` and Event B occurred at `09:14:18.012 UTC`, Event A cannot be the cause of Event B, regardless of how neatly it fits a narrative. Verify time synchronization via PTP/IRIG-B before asserting temporal precedence.

### Law 2: The Physical Energy Transfer Mechanism
There must exist an unbroken, verifiable physical mechanism governed by the laws of thermodynamics, fluid mechanics, or electromagnetism capable of transmitting sufficient energy to induce the observed failure:
- If a breaker tripped on instantaneous magnetic overcurrent ($I > 5000\,\text{A}$), there must exist evidence of a dead short-circuit or massive mechanical seizure. An ambient temperature increase of $0.5\,\text{K}$ cannot induce an instantaneous magnetic trip on a 4000A breaker.
- If a pump cavitated, there must exist physical evidence that net positive suction head available ($\text{NPSH}_a$) dropped below net positive suction head required ($\text{NPSH}_r$). Saying the pump cavitated because *"the water was warm"* without checking the suction pressure transducer is unverified speculation.

### Law 3: Protective Relay Target Confirmation
In electrical systems, modern microprocessor-based protective relays (e.g., Schweitzer Engineering Laboratories, GE Multilin) latch explicit **Protective Relay Elements (Targets)** into non-volatile memory when commanding a trip:
- Element `50P` = Instantaneous Phase Overcurrent.
- Element `51N` = Time-Delay Neutral Ground Fault.
- Element `87T` = Transformer Differential Current Mismatch.
- Element `27` = Under-Voltage Drop.

If the protective relay latched element `51N` (Ground Fault), the cause was a breakdown of electrical insulation to earth (e.g., water ingress into a conduit or a pinched cable lug). Asserting that the breaker tripped because of *"overload from the chiller"* (Element `51P`) directly contradicts the physical relay target. The relay target is the hard evidence; the engineer's narrative is a story.

## Labeling Hypotheses in the Operations Log

During a live incident investigation, intermediate working theories are necessary to direct troubleshooting. However, every unverified theory must be rigorously labeled in the site logbook:

```
+-------------------------------------------------------------------------+
|                  LOGBOOK FORENSIC DISCIPLINE                            |
|                                                                         |
|  [PERMITTED FACTUAL LOG ENTRY]                                          |
|  "09:14:18.045 UTC: Breaker SWG-02-4B tripped. Relay 87T target latched.|
|  Winding resistance test shows Phase B to ground resistance = 0.2 ohms. |
|  CONCLUSION: Phase B internal transformer winding breakdown to earth."   |
|                                                                         |
|  [PROHIBITED SPECULATIVE LOG ENTRY]                                     |
|  "Chiller CH-02 probably pulled too much juice because it was hot out   |
|  and tripped the breaker. We reset it and hope it holds."               |
+-------------------------------------------------------------------------+
```

An unverified hypothesis that is written into an operational turnover report without the word **"HYPOTHESIS"** prominently stamped on it will be inherited by the morning executive meeting as an established physical fact.

Once a false narrative enters executive slide decks, it takes weeks of contentious debate to dislodge, wasting hundreds of engineering hours solving an imaginary problem while the real physical defect—a compromised cable termination or a leaking pipe seal—remains unaddressed in the whitespace.

## Decisions to Record

- The immutable distinction between physical topological paths and verified root causes.
- The mandatory extraction and recording of microprocessor relay target codes prior to any breaker reset.
- The strict requirement that all working theories be formally labeled as `HYPOTHESIS` until verified.
- The physical energy balance calculations required to substantiate any forensic RCA claim.
"""

chapters["12-facility.md"] = """# 12. The Same Rules on the Plant

A telemetry engineer who believes that software monitoring rules apply only to cloud servers and database clusters while mechanical chillers and electrical switchgear operate under "facilities folklore" does not understand critical infrastructure.

The physical plant—the medium-voltage transformers, centrifugal chillers, secondary cooling distribution units (CDUs), and air handling units—is governed by identical telemetry laws:
- A pressure transducer requires an audited quality bitmask.
- A water temperature sensor requires deadband hysteresis and continuous dwell filtering.
- A chiller electrical trip requires microsecond time synchronization.
- A pump room alarm storm requires topological dependency masking.

```
+-----------------------------------------------------------------------------+
|                      FACILITY TELEMETRY GOVERNANCE MATRIX                   |
|                                                                             |
|  Subsystem / Instrument   Standard Telemetry Parameter  Governing Code      |
|  -----------------------  ----------------------------  ------------------  |
|  MV Switchgear (35kV)     Bus Voltage, Current, THD, PF GB/T 51409-2020     |
|  Dry-Type Transformers    Winding Temperature (< 90°C)  IEEE C57.12 / NFPA  |
|  UPS Battery Rooms        DC Float Voltage, Ambient T   IEEE 1188 / 1491    |
|  Centrifugal Chillers     Condenser Approach (<= 1.5K)  ASHRAE Standard 90.4|
|  Secondary CDU Loops      Pressure (0.15 - 0.90 MPa)    OpenViking 2.6XZ10  |
|  Secondary Coolant Chem   25.0% Propylene Glycol wt     ASTM D3306 / D1384  |
|  IT Whitespace Aisles     Containment DP (>= 5.0 Pa)    ASHRAE TC 9.9       |
+-----------------------------------------------------------------------------+
```

![CDU Shift Inspection Checklist](../figures/fig-05-liquid-cdu-shift-inspection-checklist.png)

Following the authoritative engineering standards outlined in **GB/T 51409-2020** (*Technical Standard for Integrated Monitoring System of Data Centers*) and OpenViking operational guidelines (`ALZJ-YW-2.6XZ02` and `ALZJ-YW-2.6XZ10`), every physical facility point must be operated under rigorous engineering constraints.

## The Walked Reading Wins

The physical measurement taken by a qualified technician using a calibrated, certified hand-held instrument **always supersedes the digital telemetry tile on the SCADA screen**.

If the central BMS workstation reports that the secondary cooling loop supply temperature is operating comfortably at $28.0^\circ\text{C}$ (`GREEN`), but the shift technician walks the room with a calibrated PT100 immersion probe or calibrated infrared camera and measures $34.2^\circ\text{C}$:
1. **The physical reading wins instantly**. The facility is operating in a high-temperature excursion state.
2. The technician does not average the two numbers and assume the temperature is $31.1^\circ\text{C}$.
3. The technician logs both readings into the shift register with exact timestamps:
   `08:15 UTC: SCADA reports 28.0°C | Fluke Calibrated Probe reads 34.2°C`.
4. The digital telemetry point is immediately quarantined: its quality flag is set to `UNCERTAIN (0x02)` or `BAD (0x04)`.
5. The digital sensor is subjected to an immediate physical loop calibration and forced-failure test.

Never permit a software engineer or remote monitoring specialist to argue that *"the digital sensor must be right because it was installed by the factory."* Sensors drift, thermal wells accumulate air gaps, RTD lead resistance degrades, and analog-to-digital converters lose calibration. The verified tool in the technician's hand is the ultimate anchor of truth.

## Critical Facility Telemetry Parameters

Per OpenViking `ALZJ-YW-2.6XZ10` for high-density liquid cooling infrastructure:

### 1. The CDU Pressure Envelope
- Primary Facility Water System (FWS) supply pressure: $0.15\,\text{MPa}$ to $0.90\,\text{MPa}$.
- Secondary Technology Cooling System (TCS) supply pressure: $0.15\,\text{MPa}$ to $0.90\,\text{MPa}$.
- Secondary loop pump differential pressure ($\Delta P_{\text{pump}}$): Strictly $< 1.0\,\text{bar}$. A differential pressure $> 1.0\,\text{bar}$ indicates severe piping blockage, a clogged 50-micron filter element, or an accidentally closed manifold isolation valve.
- Any drop in secondary static pressure below $0.12\,\text{MPa}$ triggers an immediate **Low Pressure Alarm**, indicating coolant leakage or thermal expansion tank bladder failure.

### 2. Plate Heat Exchanger Thermal Approach
The approach temperature across the CDU plate heat exchanger:

$$\Delta T_{\text{approach}} = T_{\text{TCS, supply}} - T_{\text{FWS, supply}} \le 8.0\,\text{K}$$

During steady-state operation, $\Delta T_{\text{approach}}$ must remain strictly $\le 8.0\,\text{K}$ (typically $3.0\,\text{K}$ to $5.0\,\text{K}$). If the approach temperature creeps above $8.0\,\text{K}$ under constant heat load, the heat exchanger plates are suffering from biological slime, mineral scaling, or particulate fouling, requiring chemical clean-in-place (CIP) flushing.

### 3. Propylene Glycol Concentration & Refractometer Testing
Per ASTM D3306 and OpenViking standards, secondary coolant must be maintained at **25.0% propylene glycol by weight** ($\pm 1.0\%$):
- Freeze protection: $-11.5^\circ\text{C}$.
- Burst protection: $-22.0^\circ\text{C}$.
- Specific gravity: $1.026 \pm 0.003$ at $20^\circ\text{C}$.
- Coolant conductivity: $< 10\,\mu\text{S}/\text{cm}$.
- Coolant pH: $7.5$ to $9.0$.

If a refractometer test reveals PG concentration $< 23.0\%$, the fluid loses biostatic efficacy, permitting bacterial colonies to form biofilms on micro-channel cold plates. If PG concentration exceeds $27.0\%$, dynamic fluid viscosity increases drastically ($\nu > 2.8\,\text{mm}^2/\text{s}$), spiking pumping power and reducing turbulent heat transfer.

## Electrical Power Quality Telemetry

Per GB/T 51409-2020 and IEEE 1159:
- **Voltage Tolerance**: $\pm 5.0\%$ of nominal rated voltage at utilization panels.
- **Frequency Stability**: $50 \pm 0.2\,\text{Hz}$ (or $60 \pm 0.2\,\text{Hz}$). A frequency excursion $> 0.5\,\text{Hz}$ indicates catastrophic grid instability requiring immediate transition to isolated diesel generation.
- **Power Factor**: Maintained $\ge 0.95$ lagging across all active operating loads.
- **Total Harmonic Distortion (THD)**: Voltage THD $\le 5.0\%$; individual harmonic voltage distortion $\le 3.0\%$.

If electrical power monitoring telemetry detects current harmonic resonance, switchgear busbars will experience severe inductive heating, leading to catastrophic bus duct insulation breakdown even when overall kilowatt load is well below nameplate rating.

## Decisions to Record

- The physical calibration registry of all hand-held test instruments used during shift rounds.
- The exact CDU operating pressures, pump differential pressures, and thermal approach temperatures logged per shift.
- The weekly optical refractometer, conductivity, and pH measurements logged for secondary cooling loops.
- The protocol establishing that walked physical measurements unconditionally override digital SCADA screens.
"""

chapters["13-morning.md"] = """# 13. The Morning After

The most critical operational review in a data center does not take place in the middle of a screaming incident; it takes place at 08:30 the following morning.

The morning review is the audit of the night's telemetry, alarms, pages, and operational decisions. Its purpose is not to retell personal anxiety, assign emotional blame, or exchange mutual congratulations that the facility did not black out.

Its purpose is to enforce **The Four Audits of the Morning Ledger**:
1. Did any alert wake a human being without meeting the Five-Line Page requirement?
2. Did any point cross an alarm threshold without having an audited row on the Master Point Sheet?
3. Did any monitoring system experience unrecorded clock drift, dropped gaps, or silent value caching?
4. Did any active incident close without exactly **one concrete, owned, dated operational change**?

```
+-----------------------------------------------------------------------------+
|                          THE MORNING AUDIT MATRIX                           |
|                                                                             |
|  Audit Dimension     Verification Standard         Failure Resolution       |
|  ------------------  ----------------------------  -----------------------  |
|  Paging Hygiene      Every page met 5-line rule    Mute chattier points     |
|  Point Integrity     Zero orphan points triggered  Audit Master Point Sheet |
|  Quality Watchdog    Zero frozen cached values     Execute Forced-Failure   |
|  Incident Ownership  1 owned action assigned       Block ticket closeout    |
+-----------------------------------------------------------------------------+
```

## The Audit of Every Page

Every automated page dispatched during the previous twenty-four hours must be reviewed against the shift turnover logbook:
- **Was the page justified by the Three Promotion Tests?** Did it represent an SLA breach, a life safety hazard, or a redundancy collapse? If a technician was woken at 03:00 for a minor warning that had zero operational urgency, the alarm rule failed. The threshold, deadband, or dwell time must be adjusted immediately.
- **Did the page comply with the Five Mandatory Lines?** Did it contain the exact timestamp, the point and path, the value and line, the person woken, and the immediate safe-state action?
- **Was the Four-Part Reply logged within fifteen minutes?** Did the responding engineer record the acknowledgment time, verify signal quality, document observed physical reality, and confirm the escalation status?

If an automated alarm paged an engineer three times for the same transient fluctuation within twenty minutes, the anti-flap quarantine engine failed to engage. Log a defect against the monitoring software configuration.

## The Hunting of Orphan Points

An **orphan point** is any telemetry point that triggered an alarm, appeared on a graphic, or sent a notification without possessing a signed, approved row on the Master Point Sheet:
- It has no documented hardware path.
- It has no audited deadband or dwell window.
- It has no named operational owner.

During the morning review, every active alarm on the system is cross-referenced against the Master Point Sheet.
If an orphan point is discovered:
1. **The point is muted instantly**.
2. Its alarm rules are disabled.
3. The point is placed into the Commissioning Quarantine queue.
4. The systems integrator or engineer who enabled the point in the production SCADA database without a signed Point Sheet receives a formal operational non-conformance notice.

Never allow an unverified point to remain active in production while someone "promises to fill out the paperwork next week." If the paperwork is not signed, the point does not speak.

## The Single Owned Action

A post-incident review that concludes with vague, generalized recommendations is an operational failure:
- *"Technicians must pay closer attention to CDU pump alarms."*
- *"We need to improve our situational awareness."*
- *"Operations will monitor the situation closely."*

None of these statements constitutes an engineering control. None of them prevents an identical incident from occurring next Tuesday.

Every incident reviewed in the morning meeting must produce **exactly one concrete, owned, dated operational change**:
- **Design Change**: *"Install mechanical interposing relay on Chiller 2 trip circuit to isolate electrical noise. Owner: J. Vance (Elec Lead). Due: 2026-10-21."*
- **Procedural Change**: *"Revise MOP-E-04 to mandate secondary phase rotation verification with rotation meter prior to racking breaker. Owner: R. Chen (Operations). Due: 2026-10-18."*
- **Inspection Change**: *"Add daily optical refractometer sampling to Station 5 shift round checklist. Owner: T. Miller (Mech Lead). Due: 2026-10-15."*
- **Hardware Change**: *"Procure calibrated vacuum filling skid with 5-micron particulate filter to eliminate air binding. Owner: Procurement. Due: 2026-10-25."*

The action must have one named human owner and one calendar completion date. The action is entered into the site computerized maintenance management system (CMMS) and tracked daily on the shift handover log until physically closed.

## Decisions to Record

- The audited count of all automated pages dispatched during the previous 24 hours.
- Any unverified orphan points identified and quarantined during the review.
- The single owned, dated corrective action resulting from every reviewed incident.
- The formal sign-off of the morning review ledger by the Operations Director.
"""

chapters["14-night.md"] = """# 14. One Night, as a Method

To understand how these principles operate under the pressure of a live production shift, consider a realistic operational narrative from a 60 MW hyperscale data center housing high-density liquid-cooled AI clusters.

The date is October 14, 2026. The shift runs from 19:00 to 07:00 UTC.

```
+-----------------------------------------------------------------------------+
|                         A LIVE PRODUCTION SHIFT LOG                         |
|                                                                             |
|  [21:15:00 UTC]  Night Physical Shift Round Completed (6 Stations Normal)   |
|  [01:42:10 UTC]  Transient Pressure Spike on Secondary Loop CDU-02          |
|  [01:42:15 UTC]  Dwell Filter (t_dwell = 10s) Prevents False Chattering Alarm|
|  [02:18:22 UTC]  Genuine Excursion: Secondary TCS Supply Temp Reaches 32.5°C|
|  [02:18:37 UTC]  Dwell Met (15s); High Alarm Latches; Quality = GOOD (0x00) |
|  [02:18:40 UTC]  Five-Line Emergency Page Dispatched to Lead Mech Engineer  |
|  [02:26:00 UTC]  Engineer Logs 4-Part Reply; Physical Gauge Verifies 32.8°C |
|  [02:28:00 UTC]  Duty Manager Promotes Event to P2 Major Incident (N-1)     |
|  [02:32:00 UTC]  Execute EOP-M-04: Standby Chiller CH-04 Started; Safe State|
|  [02:45:00 UTC]  TCS Temperature Recedes Below 30.0°C (Deadband Cleared)   |
|  [03:15:00 UTC]  Incident Closed; Single Owned Action Assigned to Mech Lead |
+-----------------------------------------------------------------------------+
```

## The Evening Baseline (19:00 - 21:30 UTC)

The incoming Duty Manager, Marcus Vance, completes the mandatory 30-minute joint physical walkthrough with the outgoing manager. They inspect the six stations: Medium-Voltage Substation, Transformer Vaults, UPS Battery Rooms, Chiller Plant, CDU Stations, and AI Whitespace.

At 21:15 UTC, Technician Chen completes the evening shift round:
- Medium-Voltage 35kV switchgear: SF6 gas pressures normal; battery charger voltage $125.4\,\text{VDC}$.
- Transformers: Maximum winding temperature $74.2^\circ\text{C}$ on Transformer TX-01B.
- Central Chiller Plant: Chillers CH-01, CH-02, and CH-03 operating; condenser approach temperatures $1.1\,\text{K}$, $1.2\,\text{K}$, $1.2\,\text{K}$ (all well below $1.5\,\text{K}$ limit).
- Secondary CDU Stations: Primary FWS pressure $0.45\,\text{MPa}$; secondary TCS supply pressure $0.38\,\text{MPa}$; pump differential pressure $0.78\,\text{bar}$ ($< 1.0\,\text{bar}$).
- Refractometer Check on CDU-02: Exactly **25.0% propylene glycol**; conductivity $4.2\,\mu\text{S}/\text{cm}$; pH $8.4$.
- AI Whitespace: Cold aisle differential pressure $+7.2\,\text{Pa}$; quick-disconnect couplings (Danfoss FD83) dry; zero fluid pooling in catch basins.

The Master Day Sheet is signed. Redundancy is verified at $2N$ electrical and $N+1$ mechanical.

## The Transient Spike: Filtered by Dwell (01:42 UTC)

At 01:42:10 UTC, a rapid hydraulic transient occurs on Secondary Cooling Loop 2. A 3-way control valve on a high-density compute rack modulates abruptly in response to an AI workload step.

The secondary supply pressure transducer (`PT-CDU-02-TCS-SUP`) detects a sharp pressure drop to $0.11\,\text{MPa}$ (below the $0.12\,\text{MPa}$ low alarm line).
- **The Dwell Filter Evaluates**: The configured dwell time for this point is $t_{\text{dwell}} = 10.0\,\text{s}$.
- The pressure remains low for $4.2\,\text{seconds}$ as the variable frequency drive ramps pump speed from $42\,\text{Hz}$ to $48\,\text{Hz}$.
- At $t = 4.8\,\text{seconds}$, pressure recovers stably to $0.35\,\text{MPa}$.
- **Operational Result**: The continuous dwell condition was not satisfied ($4.2\,\text{s} < 10.0\,\text{s}$). The event is recorded in the high-speed telemetry log, but **no alarm sounds in the control room, and no page is sent**. The engineer sleeps undisturbed.

## The Genuine Excursion and the Five-Line Page (02:18 UTC)

At 02:18:22 UTC, primary facility water system (FWS) temperature rises due to a cooling tower fan VFD fault.
The secondary technology cooling supply temperature on CDU-02 (`TT-CDU-02-TCS-SUP`) crosses the High Alarm threshold of $32.0^\circ\text{C}$, reaching $32.5^\circ\text{C}$.

1. **The Quality Check**: The SCADA engine verifies Quality Bitmask = `0x00 (GOOD)`.
2. **The Dwell Verification**: The temperature remains continuously above $32.0^\circ\text{C}$ for $15.0\,\text{seconds}$ ($t_{\text{dwell}} = 15.0\,\text{s}$).
3. **The Alarm Latches**: At 02:18:37 UTC, the High Alarm activates.
4. **The Five-Line Page Dispatches** at 02:18:40 UTC:
   ```
   [LINE 1] 2026-10-14 02:18:22 UTC
   [LINE 2] CDU-02 TCS Supply Temp (modbus://cdu-02/reg-40102)
   [LINE 3] T = 32.5°C (Exceeded High Alarm Line: 32.0°C | Dwell: 15s)
   [LINE 4] Dispatched to: T. Miller (Lead Mech) | Shift 2
   [LINE 5] Action: Confirm sensor LIVE; Execute EOP-M-04 (Chiller Staging).
   ```

## The Four-Part Reply and Safe-State Restoration (02:26 - 03:15 UTC)

At 02:26:00 UTC, Mechanical Lead Thomas Miller arrives in the CDU plant room and enters his Four-Part Reply via the mobile terminal:
- **Time Acknowledged**: `02:26:00 UTC`.
- **Quality Verified**: `Point TT-CDU-02-TCS-SUP reporting LIVE (0x00)`.
- **Observed Physical Reality**: `Local analog immersion dial gauge reads 32.8°C; CDU secondary flow 1380 LPM; primary FWS supply temperature elevated at 24.5°C`.
- **Escalation**: `Event promoted to P2 Major Incident (Redundancy threatened: secondary temps near W4 SLA limit)`.

At 02:28:00 UTC, Duty Manager Vance authorizes execution of **EOP-M-04**:
- Standby Chiller CH-04 is manually commanded to start and stages online within 180 seconds.
- Primary FWS supply water temperature drops rapidly from $24.5^\circ\text{C}$ to $14.0^\circ\text{C}$.
- Plate heat exchanger approach temperature restores to $3.8\,\text{K}$.
- Secondary TCS supply temperature recedes below $32.0^\circ\text{C}$ at 02:41 UTC.
- **The Hysteresis Deadband Holds**: The alarm remains latched until 02:45:00 UTC, when temperature drops below the reset line of $30.0^\circ\text{C}$ ($32.0 - 2.0\,\text{K}$). The alarm clears cleanly without chattering.

## The Post-Incident Closeout (03:15 UTC)

The Duty Manager conducts the incident closeout:
- Contractual SLA analysis: Secondary temperature exceeded $32.0^\circ\text{C}$ for a total duration of 22 minutes, but remained strictly below the contractual emergency limit of $35.0^\circ\text{C}$. IT servers experienced zero thermal throttling.
- Incident classified as **P2 Major Incident - Mitigated**.
- **The Single Owned Corrective Action Assigned**:
  > *"Replace faulty VFD cooling fan on Cooling Tower 2 motor drive. Owner: T. Miller (Lead Mech). Due: 2026-10-16 12:00 UTC."*

The shift concludes at 07:00 UTC. The Master Day Sheet is signed. Not a single unrecorded impairment exists on site.

## Decisions to Record

- The complete, time-stamped incident chronology log matching the live night scenario.
- The verification that dwell filtering successfully prevented false alarms during transient operations.
- The execution of the Five-Line Page and verified receipt of the Four-Part Reply within SLA.
- The single owned, dated corrective action resulting from the incident review.
"""

chapters["15-demo.md"] = """# 15. A Demo Is Not an Acceptance

Software sales demonstrations are carefully choreographed theatrical performances.

In a sales demonstration:
- Telemetry data is streamed over a pristine, isolated gigabit local area network with zero packet jitter.
- The demonstration database contains perfectly clean simulated time-series data with zero missing intervals.
- The graphical user interface features stunning 3D digital twins, animated rotating pump impellers, and sleek dark-mode glassmorphism styling.
- The machine learning anomaly detector effortlessly identifies a pre-staged artificial cooling spike and highlights it in glowing neon pink.

An operational data center is not a software demonstration:
- Telemetry travels over fifteen-year-old shielded twisted-pair cables through medium-voltage transformer vaults filled with severe electromagnetic interference (EMI).
- Field RTU microcontrollers hang unexpectedly due to buffer overruns.
- Third-party serial gateways drop packets during heavy broadcast storms.
- Real physical failures are messy, chaotic, and non-linear.

Never sign an operational acceptance certificate for a monitoring platform, SCADA upgrade, or DCIM suite based on a vendor demonstration.

```
+-----------------------------------------------------------------------------+
|                      DEMO VS. PRODUCTION ACCEPTANCE                         |
|                                                                             |
|  Vendor Demo Claim             Production Physical Reality                  |
|  ----------------------------  -------------------------------------------  |
|  "AI detects all anomalies"    Triggers 400 false alarms on morning round   |
|  "Zero-configuration setup"    Requires weeks of manual register mapping    |
|  "Seamless protocol bridge"    Drops packets under Modbus serial broadcast  |
|  "Real-time visual twin"       Lags physical plant reality by 45 seconds    |
+-----------------------------------------------------------------------------+
```

## The Five Mandatory Production Acceptance Tests

Before any new monitoring platform is permitted to sound alarms or display operational status in the central control room, it must pass **The Five Rigorous Acceptance Gates**:

### Gate 1: The Severed Wire Test (Hardware Fault Integrity)
Physically disconnect the RS-485 serial communication cable or pull the Ethernet patch cord from a live field controller:
- **PASS**: The platform marks all dependent points as `BAD / FAULT (0x04)` within three polling intervals ($t \le 3 \times T_{\text{poll}}$), displays a prominent visual communication failure banner, and actively quenches all downstream threshold alarms.
- **FAIL**: The platform holds the last known good value forward, continues displaying a healthy green icon, or reports zero.

### Gate 2: The High-Load Broadcast Storm Test (Communication Resilience)
Subject the monitoring network to a simulated packet flood (e.g., streaming high-frequency power quality waveform captures while simultaneously polling 10,000 Modbus registers):
- **PASS**: The core protective alarming engine maintains deterministic priority queuing; critical breaker trip alarms are delivered in $\le 100\,\text{ms}$; the supervisory server CPU utilization remains $\le 65\%$.
- **FAIL**: Telemetry messages drop; the web interface freezes; the database experiences lock contention; alarms arrive delayed by minutes.

### Gate 3: The Clock Drift and Power-Cycle Test
Disconnect the monitoring server from its external NTP/PTP timing source for 48 hours, then cycle utility power to the server rack:
- **PASS**: The server boots cleanly into an uncorrupted state; local hardware clocks re-synchronize to the Stratum-1 master within 60 seconds; no duplicate or out-of-order timestamps are committed to the historical archive.
- **FAIL**: Database tables corrupt; timestamps jump backward; the system re-announces 500 historical alarms as if they occurred today.

### Gate 4: The Transient Wave Dwell & Anti-Flap Audit
Inject a synthetic fluctuating analog signal that wavers across an alarm boundary twenty times in five minutes:
- **PASS**: The hysteresis deadband prevents boundary chatter; the dwell window suppresses transient noise spikes; the anti-flap engine latches after four transitions and mutes audible horns.
- **FAIL**: The system sounds the control room siren twenty times, dispatches twenty automated text messages, and crashes the SMS gateway queue.

### Gate 5: The Forensic Sequence-of-Events (SOE) Audit
Simulate a simultaneous medium-voltage breaker trip and automatic transfer switch (ATS) failover:
- **PASS**: The system extracts microsecond hardware timestamps from the protective relays and displays the events in true, verified chronological sequence.
- **FAIL**: The system timestamps events at database ingestion, displaying the downstream fan failure before the upstream breaker trip.

If a vendor's software fails even one of these five acceptance gates, **refuse acceptance**. Do not sign the commissioning completion certificate. Do not let commercial pressure from procurement force you to deploy an unvalidated system into a live production facility.

## Decisions to Record

- The formal test records and raw data captures for all five production acceptance gates.
- The signed statement confirming that sales demonstrations were excluded from technical acceptance.
- The verified network bandwidth and latency benchmarks recorded under simulated storm conditions.
- The final operational acceptance certificate signed by the Operations Director and Lead Electrical Engineer.
"""

chapters["16-sheet.md"] = """# 16. The Master Point Sheet

The Master Point Sheet is the legal, operational, and technical contract between a physical instrument and the operational staff of the data center.

Copy the headings below into your facility's configuration management database or printed turnover binder. **One sheet per critical point.**

```
+-----------------------------------------------------------------------------+
|                          MASTER POINT SHEET LEDGER                          |
|                                                                             |
|  [SECTION 1] HARDWARE IDENTITY & TOPOLOGY                                   |
|  • Tag & Human Name       --> TT-CDU-01-TCS-SUP (Secondary Supply Temp)     |
|  • Kind of Point          --> Polled Analog Input (Modbus TCP)              |
|  • Hardware Source URI    --> modbus://cdu-01-gateway/slave-01/reg-40102    |
|  • Engineering Unit       --> °C (Scale factor: 0.01 applied at ingestion)  |
|  • Physical Drawing Ref   --> P&ID Drawing PID-M-CDU-001 Rev 4              |
|                                                                             |
|  [SECTION 2] TIME & COMMUNICATION INTEGRITY                                 |
|  • Polling Interval       --> 1.0 Second (Expected continuous stream)       |
|  • Timing Source          --> PTP IEEE 1588v2 (Stratum-1 GPS Antenna)       |
|  • Timeout Multiplier     --> K_stale = 3 (Fails to STALE at t > 3.0s)      |
|  • Forced-Failure Status  --> PASSED (Tested: 2026-10-10 by Commissioning)  |
|                                                                             |
|  [SECTION 3] SIGNAL FILTERING & THRESHOLDS                                  |
|  • High-High Trip (HH)    --> 36.0°C (Dwell: 5.0s | Automatic Chiller Stage) |
|  • High Alarm (H)         --> 32.0°C (Dwell: 15.0s | SLA Warning)           |
|  • Hysteresis Deadband    --> Delta-H = 2.0 K (Reset Line: 30.0°C)          |
|  • Anti-Flap Quarantine   --> 4 toggles in 10 min -> Latch & Mute           |
|                                                                             |
|  [SECTION 4] GOVERNANCE & PROMOTION                                         |
|  • Promotion Authority    --> Licensed Duty Manager ONLY                    |
|  • Emergency Paging       --> Five-Line Format to Lead Mechanical Engineer  |
|  • Operational Owner      --> Thomas Miller (Lead Mechanical Engineer)      |
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
- **Configured Polling / Push Interval ($T_{\text{poll}}$)**: `_____ Seconds`
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
- **Hysteresis Deadband Offset ($\Delta_{\text{deadband}}$)**: `_______ Units`
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
"""

chapters["17-limits.md"] = """# 17. What This Book Does Not Own

A field guide that pretends to own the entire domain of software development, industrial automation, and corporate legal governance is an operational hazard.

Operational excellence requires establishing rigid, uncompromising boundaries around what this book owns and what belongs to external engineering and legal authorities.

## It Does Not Own a Software Product or Brand

This book does not endorse, review, or digest any commercial Building Management System (BMS), Supervisory Control and Data Acquisition (SCADA) platform, Data Center Infrastructure Management (DCIM) software suite, or telemetry database engine:
- It does not retell the user manuals of Schneider Wonderware, Siemens Desigo, Johnson Controls Metasys, Honeywell Forge, or open-source platforms like Prometheus or Grafana.
- It does not provide code snippets for configuring commercial time-series databases or tuning SQL query indexes.

The principles in this book are vendor-agnostic physical, mathematical, and procedural laws. If a software vendor claims their proprietary artificial intelligence platform renders deadbands, dwell filters, quality bitmasks, or human promotion gates obsolete, that vendor is selling snake oil. The laws of operational telemetry apply equally to a multimillion-dollar enterprise suite and a command-line script running on an edge microcontroller.

## It Does Not Own Statutory Safety Codes and Building Standards

This book cites statutory engineering standards by title, edition, and year. It deliberately does not transcribe their copyrighted text:
- **NFPA 70E (Standard for Electrical Safety in the Workplace)** governs your arc-flash approach boundaries, energized work permits, and electrical PPE categories.
- **NFPA 72 (National Fire Alarm and Signaling Code)** governs the physical installation, wiring survivability, and annunciation of smoke detectors and emergency horns.
- **OSHA 29 CFR 1910.147** establishes federal statutory requirements for zero-energy Lockout/Tagout (LOTO) verification.
- **ASHRAE TC 9.9** establishes environmental envelopes for data processing environments. ASHRAE has explicitly stated that its technical publication content is protected under international copyright law and may not be digested, ingested, or transformed into AI derivative works without formal written authorization.

Purchase official, licensed copies of these standards from their respective publishers (ANSI, NFPA, ASHRAE, ISO). Keep them in the site engineering library. Never copy and paste standard clauses into your shift logs and claim them as your site's private creation.

## It Does Not Own the Customer's Application Telemetry

This book does not own:
- Your customer's distributed application software, database query latencies, microservice trace identifiers, or network packet routing topologies.
- Your customer's server operating system logs, CPU utilization metrics, or GPU memory allocation performance.

The boundary between facility infrastructure and customer IT hardware is absolute:
- The facility owns the electrical voltage, frequency, and current delivered to the input receptacles of the server rack power distribution units (ePDUs).
- The facility owns the volumetric flow rate, static pressure, and supply temperature of the secondary coolant delivered to the rack manifold supply coupling.
- The customer owns everything that occurs inside the server chassis beyond the power supply and cold plate interface.

Never attempt to diagnose a customer's software database deadlock from a facility electrical meter, and never permit a customer's software engineer to dictate mechanical chiller staging setpoints. Respect the physical interface boundary.

## Decisions to Record

- The official, licensed copies of statutory engineering standards maintained in the site library.
- The physical demarcation boundary between facility infrastructure and customer IT hardware.
- The operational protocol confirming that telemetry rules remain binding regardless of software vendor brand.
"""

chapters["18-sources.md"] = """# 18. Titles, Standards, and the Copyright Line

A mission-critical operations team cites its sources with exact academic, engineering, and legal rigor. We operate strictly to published, peer-reviewed engineering standards, statutory safety codes, and binding commercial service agreements.

## Authoritative Engineering Standards & Codes

When authoring Methods of Procedure (MOP), SCADA point configuration specifications, or forensic Sequence of Events (SOE) incident reports, cite these authoritative titles directly:

1. **Data Center Monitoring and Automation Standards**:
   - **GB/T 51409-2020**: *Technical Standard for Integrated Monitoring System of Data Centers (数据中心综合监控系统工程技术标准)*. National standard governing operational telemetry parameters, switchgear statuses, voltage/current monitoring, chiller operating envelopes, and emergency alarm classification.
   - **ANSI/BICSI 002-2024**: *Data Center Design and Implementation Best Practices*. Establishes operational monitoring recommendations for mechanical, electrical, and plumbing (MEP) infrastructure.
   - **TIA-942-B (2017 / Addendum 2020)**: *Telecommunications Infrastructure Standard for Data Centers*. Defines infrastructure tier topologies and physical monitoring reliability requirements.

2. **Industrial Communication Protocols & Time Synchronization**:
   - **IEEE Standard 1588-2019 (PTPv2.1)**: *IEEE Standard for a Precision Clock Synchronization Protocol for Networked Measurement and Control Systems*. Governs sub-microsecond hardware timestamping for electrical Sequence of Events (SOE) recorders and protective relays.
   - **IEC 61850**: *Communication networks and systems for power utility automation*. International standard for substation electrical protection telemetry, GOOSE messaging, and digital fault recording (DFR).
   - **ANSI/ASHRAE Standard 135-2020**: *BACnet — A Data Communication Protocol for Building Automation and Control Networks (ISO 16484-5)*. Governs object identifiers, Change-of-Value (COV) reporting, and building management system telemetry.
   - **Modbus Application Protocol Specification v1.1b3**: *Modbus Organization (2012)*. Defines protocol structure, register addressing conventions, and exception response handling for serial RTU and TCP/IP industrial networks.
   - **RFC 5905**: *Network Time Protocol Version 4: Protocol and Algorithms Specification (IETF, 2010)*. Governs Stratum-1 clock synchronization across distributed server architectures.

3. **Facility Operational Reliability and Sustainability**:
   - **Uptime Institute Tier Standard**: *Operational Sustainability (2020 Edition)*. Defines operational behaviors, alarm management discipline, maintenance governance, and risk mitigation across critical facilities.
   - **ASHRAE TC 9.9 (Fifth Edition, 2021)**: *Thermal Guidelines for Data Processing Environments*. Establishes recommended and allowable environmental envelopes for air-cooled hardware (Classes A1–A4) and liquid-cooled hardware (Classes W1–W5 / W27–W45).
   - **ASTM D3306-21**: *Standard Specification for Glycol Base Engine Coolant for Heavy Duty Applications*. Governs chemical purity, freeze protection, specific gravity, and corrosion inhibitor chemistry for propylene glycol heat transfer loops.

4. **Incident Governance & Operational Guidelines (OpenViking Repository)**:
   - **HLDY-GLZD-SJGL**: *Tencent Huailai Dongyuan Data Center Incident Management System (腾讯怀来东园数据中心事件管理制度)*. Establishes incident severity tiers (P1/P2/P3), escalation clocks, and the 15-minute SLA notification protocol.
   - **HLDY-GZBD-SJGL-01**: *Tencent Incident Classification Directory (腾讯数据中心事件等级目录)*. Categorizes equipment failures by contractual customer impact.
   - **ALZJ-YW-2.6XZ02**: *IT Whitespace Physical Shift Inspection Operational Guidelines*. Governs multi-sensory shift rounds, containment differential pressure verification, and PDU thermal imaging.
   - **ALZJ-YW-2.6XZ10**: *Liquid Cooling Infrastructure & CDU Operational Guidelines*. Governs primary/secondary loop hydraulic pressures (0.15–0.90 MPa), pump differential pressure limits (< 1.0 bar), plate heat exchanger approach criteria (< 8.0 K), propylene glycol refractometer testing (25.0% wt), and reverse osmosis water chemistry.

## The Copyright Line

This book teaches an operational telemetry methodology and provides a Master Point Sheet for governing data center monitoring consoles. It is not an official digest, authorized summary, or translation of any third-party course, commercial product manual, or proprietary standard.

All trademarks, service marks, standard identifiers, and brand names mentioned in this book are the intellectual property of their respective owners:
- *BACnet* is a registered trademark of the American Society of Heating, Refrigerating and Air-Conditioning Engineers (ASHRAE).
- *Modbus* is a registered trademark of Schneider Electric USA, Inc., licensed to the Modbus Organization, Inc.
- *IEEE* is a registered trademark of the Institute of Electrical and Electronics Engineers, Inc.
- *Uptime Institute* is a registered trademark of Uptime Institute, LLC.
- *Danfoss* and *FD83* are trademarks of Danfoss A/S.
- *NVIDIA*, *NVLink*, and *NVL72* are trademarks of NVIDIA Corporation.

The mention of these titles and technologies is strictly for nominative reference, technical citation, and educational compliance purposes under fair use doctrine. Nothing herein implies endorsement, sponsorship, affiliation, or certification by any of the aforementioned entities.

## Decisions to Record

- The exact editions and publication dates of all standards cited in site monitoring specifications.
- Confirmation that no copyrighted standard text, proprietary register maps, or client confidential data was pasted into shift logs.
- The active calibration and verification schedule for all site telemetry instruments.
"""

# Upgraded Sheet in sheets/point.md
sheets_point = """# The Master Point Sheet

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

- **Configured Polling / Push Interval ($T_{\text{poll}}$)**: `_____ Seconds`
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
- **Hysteresis Deadband Offset ($\Delta_{\text{deadband}}$)**: `_______ Units`
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
"""

def main():
    print("Writing upgraded chapters for Book 06: When a Monitor May Speak...")
    for filename, content in chapters.items():
        filepath = CHAP / filename
        filepath.write_text(content.strip() + "\n", encoding="utf-8")
        print(f"Written: {filepath} ({len(content.split())} words)")
    
    sheet_file = SHEET / "point.md"
    sheet_file.write_text(sheets_point.strip() + "\n", encoding="utf-8")
    print(f"Written: {sheet_file} ({len(sheets_point.split())} words)")

    # Build combined manuscript.md
    manuscript = ROOT / "manuscript.md"
    manuscript_parts = []
    for fn in sorted(chapters.keys()):
        manuscript_parts.append(chapters[fn].strip())
    manuscript.write_text("\n\n---\n\n".join(manuscript_parts) + "\n", encoding="utf-8")
    print(f"Written combined manuscript: {manuscript} ({len(manuscript.read_text().split())} words)")

if __name__ == "__main__":
    main()
