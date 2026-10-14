# 8. External gear and facility boundaries

A liquid load bank is not an island, and a commissioning test does not occur in an abstract vacuum. The load bank connects directly to live facility infrastructure: to a Coolant Distribution Unit (CDU), to an uninterruptible power supply (UPS) or automatic transfer switch (ATS), and to computer room air handlers (CRAH).

A frequent failure mode in commissioning reporting is the confusion of boundaries:
- When a facility CDU circulating pump trips on an internal inverter fault, an inexperienced team may blame the load bank for "failing to maintain flow."
- Conversely, when a load bank's high-temperature safety switch trips due to poorly submerged heating elements, a vendor may attempt to blame the facility CDU for "running too warm."

The flash report must draw an uncompromising physical and operational boundary between the load bank (the machine under test) and the external facility gear (the host environment). A failure of external facility gear is an operational event; it is not automatically a failure of the load bank. But it must be documented with absolute precision so that the true cause of an interrupted dwell is transparent to any future auditor.

## The four external gear lines

The flash report includes an External Gear section with four explicit lines, evaluated before, during, and after every test run:

### Line 1: Coolant Distribution Unit (CDU)
The CDU is responsible for circulating secondary coolant through the load bank and transferring heat to the primary facility chilled water loop via its internal brazed plate or shell-and-tube heat exchanger.

The flash report monitors four CDU interface metrics:
- **Secondary Loop Supply Temperature (T_CDU,sup)**: The temperature of fluid exiting the CDU heat exchanger before entering the load-bank supply manifold. The report verifies that the CDU maintains its declared supply setpoint (e.g., 35.0°C ± 1.0 K). If the primary facility water warms up, causing T_CDU,sup to drift upward to 42.0°C, that drift is recorded as a **CDU boundary condition excursion**, not as a load-bank heating error.
- **Secondary Delivery Pressure & Pump Curve**: The available static pressure delivered by the CDU pumps at rated cluster flow. If the CDU pump speed hunts or cavitates due to poor suction pressure, the resulting flow fluctuations are logged against the CDU line.
- **CDU Approach Temperature**: The temperature difference between the secondary return fluid and the primary facility water (Approach = T_sec,ret - T_pri,sup). An increasing approach temperature over time indicates fouling in the CDU heat exchanger plates, not element degradation in the load bank.

### Line 2: Uninterruptible Power Supply (UPS) & Automatic Transfer Switch (ATS)
The electrical power feeding the load bank originates from facility distribution switchboards, often backed by static UPS modules or diesel generator ATS gear.

The flash report monitors:
- **Voltage Stability & Harmonic Distortion**: Line voltage sag during full-load staging. If the facility transformer sags from 415V down to 380V under full 480kW load, the active power of resistive elements will drop by nearly 16% ($P \propto V²$). The report must document that the load drop was driven by facility utility sag, not by early contactor shedding.
- **ATS Transfer Immunity**: If an integrated system test (IST) initiates an upstream power transfer, the duration of the open-transition interruption must be timed. If the interruption exceeds the load bank's 24VDC control buffer hold-up time (typically 40ms), the unit will de-energize safely, which must be attributed to the facility transfer transient.

### Line 3: Power Distribution Units (PDUs) and Busways
The physical power path from the electrical panelboard through busway tap-off boxes and drop cables to the load-bank terminals:
- **Terminal Temperature Rise (ΔT_terminal)**: Infrared thermography or calibrated thermocouple monitoring of cable lugs and contactor terminals. Terminal temperature must not exceed 70°C (or the specific rating of the 90°C RHW-2 conductor).
- **Busway Voltage Drop**: Voltage drop across the temporary feeder cables must be bounded at ≤ 2.0%.

### Line 4: Computer Room Air Handlers (CRAH / CRAC / Fan Wall)
The facility air-handling units responsible for absorbing the 16% to 20% companion air sensible heat dissipated by the load-bank blowers:
- **Intake/Discharge Air Differential**: Verifying that the data hall's hot-aisle containment (HAC) maintains proper negative pressure relative to the cold aisle, preventing thermal recirculation into adjacent server rows.
- **CRAH Chilled Water Valve Response**: Confirming that CRAH cooling coils modulate open smoothly in response to the companion air load without overflowing condensate drain pans.

## How to write an honest boundary sentence

When an anomaly or interruption occurs during a test run, the Recorder must write an honest boundary sentence. 

An honest boundary sentence adheres to three strict grammatical rules:
1. **It names the exact physical parameter that breached a threshold.**
2. **It names the specific side of the boundary where the breach occurred.**
3. **It states the consequence on the test scene without assigning speculative blame.**

### Example of an Honest Boundary Sentence
> *"At 15:42:18 UTC, during Step 4 (120kW dwell), secondary coolant supply temperature from the facility CDU rose to 39.8°C (exceeding the cited pretest boundary of 36.5°C). The load bank maintained rated electrical load (120.1kW) and normal flow (176.4 LPM), but return temperature reached 49.9°C, triggering an automated overtemperature supervisory alarm. The dwell was halted at Minute 11 by operator command. Verdict for Step 4: INVALID due to facility CDU supply temperature excursion; load bank electrical and hydraulic tracking remained fully compliant."*

### Example of a Dishonest Sentence
> *"The test had some issues with the building water, but the load bank basically passed."*

The dishonest sentence provides zero data, cites no timestamp, names no temperature, and attempts to claim an illegitimate pass. An auditor will reject it instantly. The honest sentence provides exact numbers, identifies the CDU boundary excursion, records the aborted dwell, and preserves the technical integrity of the load-bank hardware for the re-test.

## External gear pass/fail status

On the flash report summary sheet, each of the four external gear lines is given an independent status:
- **NORMAL**: Operated within the cited design envelope for the entire run.
- **EXCURSION**: Breached an operating envelope, with exact timestamps and affected parameters documented.
- **NOT APPLICABLE (N/A)**: Gear was excluded from the testing boundary by pre-declared agreement.

A facility CDU excursion does not ruin the reputation of a well-engineered load bank, nor does a clean load bank excuse a failing facility plant. The report records both, in daylight, separated by the physical manifold boundary.

## Decisions to record

In the external gear section of the flash report, record:

- The serial number, model, and firmware version of the facility CDU and its primary loop chilled water temperature.
- The upstream transformer / UPS bus voltage and phase balance during the maximum load step.
- The maximum observed cable lug terminal temperature during the full-load dwell.
- The operational status of the facility CRAH units and hot-aisle containment integrity.
- Any honest boundary sentences explaining test pauses or aborted dwells, signed by both the Operator and the Stranger.
