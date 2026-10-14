# 14. Telemetry acquisition, Modbus-TCP, and MQTT pipelines

A flash report or automated chart is only as honest as the digital telemetry pipeline that populated its cells. 

In modern megawatt-scale data center testing, telemetry does not magically appear inside a database. It makes a series of discrete, physical and digital hops: from a wetted immersion RTD element, through a local analog-to-digital converter (ADC), across an industrial Modbus-TCP fieldbus, through an edge collector gateway, and over an MQTT message broker into an immutable time-series store.

If any single hop in that chain fails silently—if an edge poller stamps a fresh timestamp onto an un-updated memory buffer, or if an MQTT broker publishes a cached "retained" message from yesterday—the resulting flash report is pure fiction.

This chapter defines the technical specifications of each hop, detailing the exact Modbus register structures, byte-ordering conventions, Quality Bitmask architectures, and MQTT payload schemas required to guarantee data integrity.

(See Figure 02 for the end-to-end telemetry hop architecture, the IEEE-754 word-swapping trap, the 16-bit Quality Bitmask register, and the standardized JSON payload schema).

## Hop 1 & 2: Physical sensor to local transmitter

The journey begins at the physical process boundary:
- **Temperature**: 4-wire Class A Pt100 RTD elements immersed directly into the central core flow ($1/3 \sim 1/2 D$) of the manifold drops, packed with zinc oxide thermal compound inside angled 45° thermowells.
- **Volumetric Flow**: Inline vortex shedding flow meters providing pulse or high-frequency digital frequency outputs, immune to fluid viscosity shifts across the operating temperature band.
- **Differential Pressure**: Piezoresistive static pressure transmitters connected to flush, polished static taps drilled perpendicular to the pipe wall.

At the transmitter, high-accuracy 24-bit Sigma-Delta ADCs sample the physical bridge at 1 kHz, applying a local digital moving average filter to output a calibrated reading once per second (**1 Hz**).

## Hop 3: Modbus-TCP fieldbus architecture

The load-bank internal controller exposes its operational parameters over standard industrial **Modbus-TCP (Ethernet Port 502)** or Modbus-RTU (RS-485 serial bus operating at 115,200 baud, 8-N-1):

- **Discrete Coils (Function 0x01 / 0x05)**: Binary control states—solenoid valve positions (V-101 open/closed), immersion heater contactor feedback states, emergency stop circuit continuity, and leak rope relay status.
- **Input Registers (30001+, Function 0x04)**: Read-only sensor measurements generated directly by local hardware ADC channels.
- **Holding Registers (40001+, Function 0x03 / 0x06 / 0x10)**: Commanded load setpoints, operating mode configurations, and alarm limit thresholds.

### The IEEE-754 32-bit float byte-ordering trap
A single 16-bit Modbus register cannot store a 32-bit floating-point engineering quantity (such as a temperature reading of 45.12°C). Floating-point values require two consecutive 16-bit registers (4 bytes total).

Different microcontroller architectures implement different word-ordering conventions. If the edge gateway assumes the wrong word order, numbers will be completely corrupted:
- **CDAB (Big-Endian with Word Swap)**: The industrial standard for Modbus floats.
 - Reg 40001 = `0x4234`, Reg 40002 = `0x0000` $\implies$ Evaluates correctly to **45.00°C**.
- **ABCD (Big-Endian Direct)**:
 - Reg 40001 = `0x0000`, Reg 40002 = `0x4234` $\implies$ Evaluates to **1.87 × 10^{-38}** (Microscopic garbage!).
- **BADC (Little-Endian with Byte Swap)**: Evaluates to completely different arbitrary values.

The flash report's working setup sheet must cite the exact word-ordering convention used by the controller firmware. A temperature that suddenly jumps between seasons during commissioning is not an environmental miracle; it is an unverified word-swap parse error. Fix the parse in the edge gateway configuration; do not overwrite the raw incoming hex bytes.

### The mandatory 16-bit Quality Bitmask register (Reg 40050)
A raw number without a quality flag is an unverified assertion. The load-bank controller must maintain a dedicated **16-bit Quality Bitmask Register (Register 40050)** updated in real-time by internal firmware diagnostics:

- **Bit 0 (`0x0001`)**: `SUPPLY_TEMP_VALID` (1 = Healthy, 0 = Fault/Open-circuit)
- **Bit 1 (`0x0002`)**: `RETURN_TEMP_VALID` (1 = Healthy, 0 = Fault/Open-circuit)
- **Bit 2 (`0x0004`)**: `FLOW_METER_VALID` (1 = Healthy, 0 = Fault/Pulse-lost)
- **Bit 4 (`0x0010`)**: `SENSOR_STALE_ALERT` (Asserted if ADC repeats identical value for > 3s)
- **Bit 5 (`0x0020`)**: `COMM_TIMEOUT` (Asserted if internal transmitter bus times out > 250ms)
- **Bit 6 (`0x0040`)**: `OUT_OF_RANGE` (Asserted if RTD resistance breaches physical envelope)

If Register 40050 asserts Bit 4, 5, or 6, the edge gateway must immediately classify the reading as **FAULT** and log a missing gap, rather than publishing the corrupted number downstream.

## Hop 4: Edge gateway active polling

The edge gateway runs a deterministic 1 Hz polling loop querying the load-bank Modbus controller:
- The poller queries the input and quality registers every 1,000 milliseconds.
- **The Timeout Policy**: If the Modbus slave fails to respond within 250 milliseconds, the poller logs a **COMMUNICATION TIMEOUT** for that second.
- **Strict Ban on Painting Forward**: The edge gateway is strictly forbidden from caching the last successful reading and stamping it with the new second's timestamp! Painting forward the previous reading to prevent an empty cell is an intentional fabrication of data. A failed poll must be logged as `NaN` or `MISSING`. If three consecutive polls fail, the plateau is marked **INVALID**.

## Hop 5: MQTT telemetry broker and JSON schema

The edge gateway packages the live 1-second telemetry and publishes it to a local MQTT message broker:
- **Topic Hierarchy**: Must follow a clean, hierarchical asset topology:
 `dc/[hall_id]/[rack_id]/telemetry` (e.g., `dc/hall-03/lb-01/telemetry`)
- **Quality of Service**: Must use **QoS 1 (At Least Once Delivery)** with local persistence buffering to guarantee that network switch hiccups do not cause lost packets.

### The JSON Telemetry Schema
Every message published to the broker must conform to a standardized JSON schema containing timestamp, electrical, hydraulic, and quality blocks:

```json
{
 "timestamp": "2026-10-14T14:22:15.000Z",
 "rack_id": "LB-NVL72-01",
 "run_id": "RUN-2026-OCT-CX01",
 "commanded_kw": 120.0,
 "electrical": {
 "feeder_a_kw": 60.1,
 "feeder_b_kw": 59.9,
 "total_kw": 120.0,
 "voltage_v": 415.2,
 "current_a": 167.1,
 "pf": 0.999
 },
 "hydraulics": {
 "flow_lpm": 176.4,
 "supply_c": 35.08,
 "return_c": 45.12,
 "delta_t_k": 10.04,
 "dp_kpa": 112.5,
 "thermal_kw": 98.6
 },
 "companion_air": {
 "inlet_c": 24.2,
 "outlet_c": 38.5,
 "air_kw": 18.9
 },
 "quality": {
 "mask": "0x0007",
 "stale_flag": false,
 "raw_samples": 60
 }
}
```

### Two Lethal MQTT Habits to Forbid
1. **The Retained Message Trap**: In the MQTT protocol, a publisher can mark a message as "retained," causing the broker to store it and instantly deliver it to any new subscriber that connects later. If an automated flash-report script connects to the broker and ingests a retained message, it may ingest a reading that was published three days ago during a shop test! The test plan must mandate: **All telemetry publishers must set `retained = false`**.
2. **Last-Will-and-Testament Misinterpretation**: The broker's Last-Will-and-Testament (LWT) message (published when an edge gateway disconnects unexpectedly) must publish an explicit death payload (`{"status": "OFFLINE", "quality": "DEAD"}`). The reporting engine must recognize this payload immediately and halt dwell timers.

## The pre-heat stale proof test

Before commanding heat on the day of the test, the test team must execute the **Pre-Heat Stale Proof Test**:
1. With the data pipeline running and logging zero-load baseline data, an operator physically disconnects the signal cable of Return Temperature Sensor RTD-102 (or unplugs the Modbus Ethernet cable from Cabinet 2).
2. The Recorder monitors the live dashboard and the exported CSV file.
3. **The Proof of Compliance**: The export must instantly record `NaN`, `GAP`, or `DISCONNECTED` within 1 second, and the Quality Bitmask must transition to `0x0040` (Sensor Fault).
4. **The Proof of Failure**: If the dashboard or export continues to display 35.0°C with moving timestamps, the pipeline is guilty of painting forward stale data. The test is stopped immediately. You do not add heat until the telemetry pipeline proves it can honestly report a dead sensor.

## Decisions to record

In the acquisition section of the flash report, document:

- The confirmed Modbus register map revision and the verified float byte-ordering format (CDAB / Big-Endian Word Swap).
- The exact polling interval (1,000ms) and confirmed timeout threshold (250ms).
- The MQTT broker endpoint, topic string, and confirmation that retained messages were disabled.
- The certified execution of the Pre-Heat Stale Proof Test, noting the exact second the sensor was unplugged and the second the pipeline registered the gap.
