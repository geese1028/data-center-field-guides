# 5. The weeks before the window

The thermal heat window in a data hall typically spans only a few days. The commissioning project itself is the intense month of preparation surrounding those days. Seasoned commissioning engineers treat the preparation month as the decisive phase of the project, with the heat window serving merely as the witnessed validation.

A test team that rolls load banks into an unfamiliar hall without a rigorous pre-mobilization survey will waste the first half of their thermal window diagnosing missing adapters, tripping upstream PDU breakers, or arguing about unverified floor loading ratings.

```
+----------------------------------------------------------------------------------------------------+
| PRE-MOBILIZATION MILESTONE TIMELINE |
+-------------------+--------------------------------------------------------------------------------+
| T - 4 WEEKS | Site Access & Structural Survey: Path-of-travel, freight elevator capacity, |
| | floor live load (kN/m²), electrical tap boxes, and manifold connection audit. |
+-------------------+--------------------------------------------------------------------------------+
| T - 3 WEEKS | Calibration & Instrumentation Audit: ISO 17025 certificates verified for all |
| | power meters, ultrasonic flowmeters, PT100 immersion probes, and IR cameras. |
+-------------------+--------------------------------------------------------------------------------+
| T - 2 WEEKS | Emergency Response & MOP Authorization: Chemical spill containment, E-Stop |
| | procedures, and energization permits signed by Owner and Facility Operations. |
+-------------------+--------------------------------------------------------------------------------+
| T - 1 WEEK | Floor Readiness & Blank Sheets: Script revision freeze, master sheets printed |
| | in ink, test gear staged on site, secondary loop flushed and statically tested.|
+-------------------+--------------------------------------------------------------------------------+
```

## Equipment Count and Spare Strategy

Do not finalize an equipment rental order until the claim sentence is formally signed. Sizing load banks from a generic template risks ordering the wrong topology. Calculate the equipment count directly from the certified claim:
- **Liquid Thermal Duty**: Total kW simulated at the secondary manifold (e.g., ten 120 kW load banks for a 1.2 MW row).
- **Air-Side Rejection**: If the claim includes whitespace thermal stability, ensure the 15% to 20% convective air load is accounted for via dedicated fan-assisted load-bank coils or auxiliary air heaters.
- **The N+1 Cold Spare Path**: Always mobilize an additional load bank, spare high-pressure hoses, and duplicate quick-disconnect couplings. A load bank that suffers a control board failure or transit damage during transport is a logistical reality; having a verified spare staged on site keeps the multi-million-dollar testing window on schedule.

## The Site Access and Structural Survey

The site survey is a critical engineering gate, not an informal walk-through. It answers four mandatory questions:

1. **Path-of-Travel and Ingress**: Can the equipment physically navigate the route from the loading dock to the data hall? Measure freight elevator door clearances, elevator weight limits, corridor turn radii, and ramp slopes. Confirm that the access path does not require rolling heavy load-bank castors across unfinished tile seams or unprotected raised floor panels.
2. **Structural Floor Loading**: Verify that the combined weight of the load banks, coolant-filled manifolds, and personnel does not exceed the floor's live-load rating (typically 12.0 kN/m² to 15.0 kN/m² for heavy data halls). Verify this against structural engineering stamped drawings. Inspect raised-floor pedestal understructure, stringer bolting, and seismic bracing.
3. **Electrical Infrastructure Tap**: Inspect the Power Distribution Units (PDUs) or overhead busway tap boxes feeding the test row. Verify breaker frame sizes, trip unit settings (electronic LSIG parameters), phase pinout configurations, and receptacle types. Compare the load bank’s inrush and rated full-load amperage against the upstream protective coordination curve to prevent tripping upstream sub-station breakers during step loading.
4. **Hydraulic Interfaces**: Physically inspect the secondary supply and return manifold taps. Document pipe diameters, isolation valve models, and quick-disconnect coupling geometries (e.g., Danfoss Hansen FD83 series or ISO 16028 flush-face couplings). Never assume fitting interchangeability; verify gender, thread pitch, and O-ring elastomer compatibility (EPDM for glycol/water loops; never use standard Buna-N with high-temperature glycols).

A survey note documenting any inaccessible areas, unverified valves, or undocumented circuit breakers must be formally published. Undocumented physical interfaces must be resolved as formal pre-mobilization deviations before equipment leaves the warehouse.

## Instrument Traceability and Calibration Standards

All verification measurements are legally dependent on the calibration integrity of the field instruments. A measurement recorded with an uncalibrated instrument is merely an unverified opinion.

Every field instrument deployed during the campaign must possess an active, traceable calibration certificate (ISO/IEC 17025 accredited) that remains valid throughout the entire duration of the testing window:

```
+----------------------------------------------------------------------------------------------------+
| MINIMUM INSTRUMENT ACCURACY STANDARDS |
+--------------------------+-----------------------+-------------------------------------------------+
| INSTRUMENT CLASS | ACCURACY STANDARD | MANDATORY FIELD DEPLOYMENT SPECIFICATION |
+--------------------------+-----------------------+-------------------------------------------------+
| Power Quality Analyzer | Class 0.2 (0.2% FS) | Calibrated 3-phase active power & THD analyzer. |
| Ultrasonic Flow Meter | Class 0.5 (+/- 0.5%) | Dual-channel transit-time clamp-on; 10D/5D run. |
| Immersion Temp Probes | 4-wire PT100 1/3 DIN | Calibrated to +/- 0.05 K; high-thermal paste. |
| Differential Pressure | +/- 0.1% Full Scale | Calibrated piezoresistive transmitter. |
| Thermal Imaging Camera | NETD < 40 mK; +/- 1 K | Calibrated focal plane array (384x288 min). |
+--------------------------+-----------------------+-------------------------------------------------+
```

If an instrument's calibration expires during the project, it must be removed from service and replaced with a certified backup. An expired certificate invalidates all data recorded from that moment forward.

## The Emergency Action Plan (EAP) and Site Permits

Before making the first mechanical connection, the Emergency Action Plan must be reviewed and signed by all parties. The plan must explicitly detail actions for four specific scenarios:
1. **Secondary Fluid Spill / Leak**: Immediate pump isolation, vacuum recovery, spill containment socks deployed, and environmental reporting.
2. **Electrical Flash / Insulation Failure**: Immediate upstream PDU emergency trip, arc flash perimeter controls, and medical emergency escalation.
3. **Uncontrolled Thermal Runaway**: Immediate load-bank de-energization sequence, CDU bypass valve override, and facility chilled water max-flow command.
4. **Life Safety Alarm (VESDA / Fire Suppression Activation)**: Evacuation paths, personnel accountability, and coordination with automated EPO circuits.

All required working permits must be secured prior to mobilizing tools:
- **Energization Permit**: Authorization to close breakers and energize temporary loads.
- **Hot Work Permit**: Required if any welding, soldering, or thermal stress tests are planned.
- **Mechanical Fluid Permit**: Authorization to connect to facility liquid loops, purge air, and circulate fluid.

## Pre-Printed Master Sheets and Shift Reporting

Design and print all blank master record sheets (Chapter 16) before arriving on site. Each sheet must clearly list the script step number, instrument ID, and expected numerical tolerance bands, with blank cells reserved for physical field measurements. Developing record sheets after testing starts invariably leads to omitted parameters and selective logging.

Establish the daily shift reporting protocol during the kickoff meeting. Every operational shift concludes with a formal Daily Shift Note detailing:
- The exact test script revision executed.
- Ambient environmental conditions and facility baseline state.
- Key operational milestones achieved.
- Unscheduled stops or safety halts, including root-cause assessments.
- Newly logged punch list items and any re-tested closures.
- Confirmed schedule and test scripts for the subsequent shift.

If testing was halted for the day due to upstream facility issues or mechanical failures, a Daily Shift Note must still be published stating: "Zero scripts executed; testing halted due to [specific reason]." A missing shift note creates an audit gap that cannot be repaired after demobilization.

## Decisions to record before test start

- The load-bank capacity and cold spare allocation, validated against the claim.
- The signed site survey report, including verification of floor loading and electrical capacities.
- The instrument calibration register, including serial numbers, certificate IDs, and expiration dates.
- The signed Emergency Action Plan and all active operational permits.
- Confirmation that physical master record sheets are printed and staged on site.
