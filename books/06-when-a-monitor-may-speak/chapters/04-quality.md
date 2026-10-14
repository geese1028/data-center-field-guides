# 4. Live, Stale, Missing

A monitoring point displayed on an operations workstation console exists in one of three absolute states:
1. **LIVE (0x00)**: The measured value is verified fresh, arrived within its designated polling interval, and originated from a healthy physical transducer.
2. **STALE (0x01)**: The system is displaying an older cached value because newer telemetry packets failed to arrive within the designated timeout window.
3. **MISSING / FAULT (0x04)**: The communication link is severed, the transducer loop is open, or the channel is reporting an unrecoverable electrical error.

```
+-----------------------------------------------------------------------------+
| QUALITY BITMASK SPECIFICATION |
| |
| Bitmask Quality State Operational Capability Console Presentation |
| ------- ------------- ------------------------ ----------------------- |
| 0x00 GOOD (LIVE) Valid for SLA & Alarms Standard Green / White |
| 0x01 STALE Visible for Trends Only Amber Stripe (Muted) |
| 0x02 UNCERTAIN Engineering Audit Only Question Mark (?) Icon |
| 0x04 BAD / FAULT Quarantined; No Alarms Grey / Red Border (Comm) |
+-----------------------------------------------------------------------------+
```

![Anatomy of an Operational Point & Quality Bitmask](../figures/fig-01-point-anatomy-and-quality-flag.png)

Never invent a fourth state called "Unknown" and then treat it operationally as if it were Live. A point is Live only when every single verification test passes.

## The Mathematical Definition of Stale

A point transitions from `LIVE` to `STALE` according to a rigid mathematical rule:

$$t_{\text{current}} - t_{\text{last\_good}} > K_{\text{stale}}  \times T_{\text{poll}}$$

Where:
- T_poll is the configured polling interval (e.g., 1.0 s for secondary cooling pressure, 5.0 s for battery float voltage).
- K_stale is the stale multiplier constant, which must be configured strictly to **K_stale = 3**.

If a secondary cooling supply pressure point configured for a 1-second polling interval fails to deliver a valid telemetry packet for more than 3.0 seconds (t > 3 × 1.0 s), the point immediately forfeits its `LIVE` status. Its quality flag flips to `STALE (0x01)`.

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

A graphical trend engine that drops missing telemetry packets and quietly draws a smooth straight line connecting the surrounding data points has manufactured a physical fiction. By connecting a measurement from 14:00 (3.5 bar) to a measurement from 14:15 (3.4 bar) across a 15-minute telemetry dropout, the graph hides the fact that at 14:07 the pressure may have plunged to zero when a bypass valve slammed shut.

Every telemetry charting engine must display a visible, discontinuous gap whenever points are missing. If data was not collected, the graph must show blank white space. Connecting points across a communication void is an operational deception.

## How a Screen Lies While Looking Calm

Facility managers must train operators to recognize the subtle failure modes where a monitoring dashboard appears calm while the underlying plant is burning:
1. **The Frozen Database Cache**: The graphical web tile displays a steady, reassuring reading of 22.4°C in green because the web server's background cache failed to refresh from the SQL database three hours ago.
2. **The Ingestion Timestamp Mask**: The database server continuously updates the record's timestamp every five seconds, creating the appearance of live data, while the field RTU has been hung in an unhandled exception loop since dawn, re-transmitting the same cached memory buffer.
3. **The Suppressed Gap Trend**: The trending software automatically interpolates across missing data packets, producing smooth, gentle sine waves that conceal severe hydraulic water hammer spikes.
4. **The Silent Setpoint Override**: A technician temporarily raised an alarm threshold from 28.0°C to 45.0°C during a previous shift to silence a nuisance horn, failing to record the change. The screen remains quiet because the alarm boundary was moved to an impossible limit.

Audit your screens with the Forced-Failure Test. Physically disconnect the sensor. If the screen does not scream within ten seconds, the screen is an operational liability.

## Decisions to Record

- The explicit timeout multiplier (K_stale = 3) configured for every polling loop.
- The visual presentation rules enforcing discontinuous gaps across missing data intervals.
- The operational protocol prohibiting stale points from closing active incident tickets.
- The site register of all unverified points currently quarantined under `BAD` or `STALE` quality marks.
