# 2. Accept the Source Before It Speaks

A data stream from a new monitoring system, a third-party gateway, or a refurbished switchgear line-up is guilty until proven innocent. Never allow a new point to sound control room alarms, page on-call engineers, or populate contractual SLA reports based on a successful vendor demonstration.

```
+-----------------------------------------------------------------------------+
| POINT ACCEPTANCE GATEWAY |
| |
| [STAGE 1] Physical Loop Verification (Calibrated source applied at probe) |
| | |
| [STAGE 2] Full-Scale & Zero-Scale Range Check (0% / 50% / 100% calibration)|
| | |
| [STAGE 3] The Forced-Failure Test (Physically sever wire / kill power) |
| | • PASS: Console transitions to STALE / FAULT within 3x interval |
| | • FAIL: Console holds last value or stays green -> REJECTED |
| | |
| [STAGE 4] Dwell & Deadband Functional Validation under simulated noise |
| | |
| [STAGE 5] Master Point Sheet Signed by Duty Manager & Commissioning Lead |
+-----------------------------------------------------------------------------+
```

![The Master Point Sheet and Audit Lifecycle](../figures/fig-07-master-point-sheet-and-audit-lifecycle.png)

A point is accepted into production operations only after it has survived the **Forced-Failure Test**. If a monitoring channel cannot detect and correctly report its own physical death, it is an operational hazard that will mislead technicians during a crisis.

## The Physical Loop Calibration

Before a software point is connected to an alarm rule, the complete end-to-end analog loop must be physically verified:
1. **Zero-Scale Verification**: Inject 4.00 mA (or 0.0 V) at the sensor transmitter terminals using a calibrated precision current loop calibrator (e.g., Fluke 789). Verify that the SCADA console displays exactly 0.0% of scale (e.g., 0.0 bar on a 0 - 10 bar pressure transducer) within ± 0.25% span accuracy.
2. **Mid-Scale Verification**: Inject 12.00 mA. Verify that the console displays exactly 5.00 bar.
3. **Full-Scale Verification**: Inject 20.00 mA. Verify that the console displays exactly 10.00 bar.

If the console display drifts or exhibits non-linear response across the three points, the loop fails acceptance. Check for common-mode ground loops, unshielded signal cabling running parallel to 480V VFD power conductors, or incorrect analog-to-digital (ADC) conversion gain settings in the programmable logic controller (PLC).

## The Mandatory Forced-Failure Test

The defining test of a monitoring source is not how it behaves when the plant is running smoothly; the defining test is how it behaves when the measurement path is violently destroyed.

With the sensor operating under normal conditions and reporting a valid reading on the central console, execute the Forced-Failure Test:
1. **Physical Disconnect**: Physically unscrew the signal conductor from the analog input terminal block, or disconnect the RS-485 serial communication cable from the gateway.
2. **Start the Stopwatch**: Observe the operator workstation console.
3. **Audit the Console Reaction**:
 - **PASS Criteria**: Within three polling intervals (t ≤ 3 × T_poll), the display tile must transition from `GREEN` to `GREY` or `AMBER-STRIPED`, the quality bitmask must transition to `STALE (0x01)` or `BAD (0x04)`, the value field must display `COMM_FAULT` or `NAN`, and all downstream automatic threshold alarms must be actively quenched.
 - **FAIL Criteria**: If the console continues displaying the last known good value (e.g., 28.4°C) in a healthy `GREEN` color, or if the central database quietly holds that number forward for minutes while the sensor is disconnected, **the point fails acceptance immediately**.

A monitoring platform that holds the last known good value forward during a communication loss is an engine of operational deception. If a cooling loop pipe bursts and severs the communication wire to the pressure sensor, a system that holds the last value will report normal pressure while the server hall floods.

Never accept an explanation from a software vendor that *"the system caches the last value to prevent visual flickering on the dashboard."* Caching an unverified value during a communication failure is not UI smoothing; it is a structural failure of monitoring integrity.

## Digital Network Loop Validation

For digital fieldbuses (BACnet/IP, Modbus TCP, OPC UA, SNMP):
- Audit the communication network round-trip time (RTT). The 99th percentile latency must remain strictly below 100 ms.
- Verify packet error rates and CRC checksum rejections. If serial CRC errors exceed 0.1% of total polling requests, the communication channel is physically compromised by electrical noise or improper bus termination resistors (120 Ω end-of-line resistors missing).
- Verify slave controller address uniqueness. Duplicate Modbus slave IDs or colliding BACnet Device Object Identifiers will cause alternating telemetry packets from two different physical machines to interleave into a single database trend, creating wild, impossible oscillations.

## Decisions to Record

- The physical calibration certificate numbers and calibration dates for all test instruments used during loop verification.
- The exact execution timestamp and observed console reaction for the Forced-Failure Test.
- The measured communication round-trip latency and CRC error rate across digital fieldbuses.
- Formal sign-off on the Master Point Sheet authorizing the point to transition from Commissioning Quarantine into Active Production.
