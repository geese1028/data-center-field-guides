# 9. Automated fields and human judgment

Modern commissioning platforms use automated data ingestion scripts, Python pipelines, and cloud dashboards to ingest thousands of Modbus and MQTT telemetry points per second. Automation is efficient, consistent, and immune to manual calculation fatigue.

However, an automated script that calculates numbers must never be confused with an automated script that grants technical acceptance.

The flash report establishes an unyielding boundary between two distinct categories of cells:
1. **Script-Filled Cells**: Arithmetic and statistical quantities computed deterministically from raw telemetry.
2. **Human-Filled Cells**: Qualitative verdicts, contractual compliance determinations, and legal signatures of technical acceptance.

An algorithm does not hold a professional engineering license, cannot appear in court, and cannot take financial or operational responsibility for a data hall fire. An algorithm calculates numbers; a human writes the verdict.

## What a script is allowed to fill

Automated scripts, ingestion pipelines, and database aggregation queries are ideally suited for deterministic mathematics. A script may—and should—fill the following fields without human intervention:

- **Timestamps and Sample Counts**: Exact start and end times to the millisecond, duration of dwells in seconds, and the total count of valid raw 1-second samples received per channel.
- **Statistical Summaries**: Arithmetic mean (μ), minimum ($\min$), maximum ($\max$), sample standard deviation (σ), and variance (σ²) across defined time windows.
- **Derived Physical Calculations**: Mass flow rate (ṁ), bulk fluid density (ρ), specific heat capacity (C_p), liquid enthalpy absorption (Q_liquid), and companion air sensible heat (Q_air).
- **Multi-Cabinet Metrics**: Group means, group standard deviations, and the Coefficient of Variation (CV) across parallel cabinets.
- **Enthalpy Closure Ratios**: The exact percentage closure between active electrical power and total thermodynamic heat dissipation (P_elec vs Q_liquid + Q_air).
- **Algorithmic Anomaly Flags**: Automated alerts indicating zero-variance flatlines (σ² ≤ 1.0 × 10^{-4}), missing communication gaps, out-of-range sensor readings, and changepoint candidate trigger times from Focus, FLOC, or CPOP.

A computer executes arithmetic faster and with far greater precision than a human with a pocket calculator. Let the script do the arithmetic.

## What a script is strictly forbidden from writing

Under no circumstances may an automated script, a dashboard macro, or an AI model generate the words:
- **PASS**
- **FAIL**
- **NOT RUN**
- **WAIVED**

An automated script that evaluates a row, observes that the calculated temperature is 45.1°C against an upper limit of 46.0°C, and automatically stamps the word "PASS" onto the PDF has exceeded its authority.

### Why Automated "Pass" is Dangerous
Consider what an algorithm cannot know:
- The algorithm does not know that the RTD reporting 45.1°C was accidentally installed in a cold dead-leg stub rather than the active stream.
- The algorithm does not know that a temporary bypass hose was kinked behind the cabinet, or that an unrecorded manual valve adjustment was performed during the hold.
- The algorithm does not know that the client issued an emergency verbal bulletin that morning shifting the test envelope from 46.0°C down to 44.0°C.

An automated script that writes "PASS" lulls the engineering team into a false sense of security. Operators stop looking at physical pipes, stop listening for pump cavitation, and stop verifying instrument calibration tags, assuming that "the software is handling compliance."

In this field guide, the verdict cells on the flash report template are born blank. They can only be filled by a human hand using an ink pen or an authenticated digital cryptographic signature.

## The crime of the human override

The inverse failure mode is equally toxic: a human being who observes a failed mathematical cell calculated by the script and overwrites the verdict with an unauthorized "PASS."

If the script correctly calculates that flow CV is **7.2%** against a maximum threshold of **5.0%**, an engineer may not write "PASS" beside that cell and add a verbal excuse: *"Flow was a little uneven, but overall cooling looked fine."*

That action is not an engineering interpretation. It is an unrecorded, illegitimate waiver. 

If a calculated cell fails:
- The human verdict for that line must be **FAIL**.
- If the project team genuinely believes that the failure does not compromise the broader commissioning objective, the Sheet Owner must invoke the formal **Waiver Protocol**:
 1. Revise the design basis specification to explicitly widen the tolerance from 5.0% to 7.5%;
 2. Assign a new document revision mark (e.g., Rev 2.5);
 3. Formally re-classify the claim as a known limitation;
 4. Obtain written, signed authorization from the facility owner.

A waiver executed in broad daylight with an updated document revision is an auditable engineering decision. A human "PASS" written over a failed cell in the dark of a spreadsheet is a falsification of the test record.

## Designing the two-column interface

To enforce this discipline in software and print, every flash report template must implement a strict **Two-Column Interface**:

| Left Column: Automated Data Block (Script Owned) | Right Column: Evaluation & Verdict (Human Owned) |
| :--- | :--- |
| • Commanded Power: 120.0 kW | • Cited Limit Citation: DOC-SPEC Rev 2.4, Table 2 |
| • Measured Power: 120.2 kW | • Verified Feeder Balance: Phase unbalance < 1.0% |
| • Inferred Liquid Heat: 98.6 kW | • Thermodynamic Plausibility: Confirmed |
| • Enthalpy Closure: 98.0% | • Hardware Physical Inspection: No leaks / Normal sound |
| • Calculated Flow CV: 2.95% (σ = 5.21 LPM) | • Consistency Verification: Passed within 5.0% threshold |
| • Quality Mask: 0x0007 (Valid, σ² > 0) | • **Human Verdict**: **PASS** [Initials: E.V., Lead CxA] |

The left column contains un-retouched numbers generated by code. The right column contains human scrutiny, manual verification checks, and the final responsible signature.

## Decisions to record

In the governance section of the flash report, record:

- The software version, script checksum (SHA-256 hash), and repository branch of the automated data aggregation pipeline.
- The certified statement that all verdict cells (Pass/Fail/Not Run) were manually reviewed and entered by the designated human authorities.
- Any formal waivers invoked during the campaign, referencing the authorized document revision and the owner's signature.
