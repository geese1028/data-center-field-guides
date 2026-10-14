# 10. The formal report package

A flash report is designed for rapid, on-site technical triage. It delivers the immediate five-line verdict within two hours of a load-bank test shutdown so that facility managers, commissioning directors, and contractor leads can determine whether to advance to the next commissioning phase or hold the site for corrective repairs.

However, the flash report does not vanish when the shift ends. It forms the permanent core of the **Formal Commissioning Verification Handover Package**—the legal and technical dossier that survives into the operational life of the data center and is archived for insurance underwriters, hyperscale tenant audits, and annual facility recertifications.

A formal package that is eighty pages of marketing brochures and un-indexed raw data dumps will be discarded by an auditor. Conversely, a package that is too brief to defend its numbers will be rejected. 

This chapter defines exactly what to keep in the formal handover package, what to ruthlessly discard, and how to structure the archive so that a stranger can verify its integrity ten years after the test crew has demobilized.

## What must be kept: The seven essential artifacts

The formal handover package must contain seven discrete, numbered artifacts. If any one of these seven is missing, the package is incomplete:

### Artifact 1: The One-Page Executive Flash Report
The definitive summary sheet defined in Chapter 1 and illustrated in Figure 01:
- The run metadata (Run ID, facility location, date, cited specification revision).
- The five scene passes table (Pretest, Gradient, Overload, Step Change, Single-Feed Fault) with measured values, dwell durations, and explicit PASS/FAIL/NOT RUN verdicts.
- The overall test verdict clause.
- The wet ink or cryptographic signatures of all four designated roles (Sheet Owner, Operator, Recorder, Stranger).

### Artifact 2: The Preparation and Baseline Certificate
Documentation proving that the test cluster was fit to test before heat was commanded:
- The four preparation gates verified and signed.
- The cold 10-minute stabilization log, including the one-minute baseline averages.
- The cold hydraulic impedance calibration record, noting locked balancing valve positions and baseline differential pressure (ΔP).

### Artifact 3: The Multi-Cabinet Consistency Sheet
The statistical evaluation of cluster balance across all parallel load banks:
- The calculated Coefficient of Variation (CV) for electrical active power (CV ≤ 1.0%), coolant flow (CV ≤ 5.0%), temperature rise (CV ≤ 3.0%), and manifold pressure (CV ≤ 5.0%).
- The certified non-zero variance check (σ² > 0) proving that live turbulent flow was present and that no channel was echoing cached/frozen data.

### Artifact 4: The Step Data Blocks and Enthalpy Closure Tables
The complete thermodynamic balance sheet for every load step (25%, 50%, 75%, 100%, 110%):
- The Four-Summary statistics (Minimum, Maximum, Arithmetic Mean, Standard Deviation) for all electrical, liquid, and air channels.
- The first-principles thermodynamic energy balance: active electrical power (P_elec) compared against liquid enthalpy (Q_liquid = ṁ C_p ΔT) and companion air sensible heat (Q_air).
- The certified Enthalpy Closure Ratio (≥ 97.0%).

### Artifact 5: The Time-Series Oscillograms and Charts
High-resolution, vector-quality charts generated from the immutable raw data:
- Overlaid power and temperature waveforms for all parallel units, plotted on scales that honestly reveal individual cabinet divergence.
- Annotated dynamic step-change response plots, detailing settling times and peak hydraulic pressure pulses.
- The 2N single-feed loss transient oscillogram, capturing contactor clearing (< 20ms) and zero-dip control bus stability.

### Artifact 6: The Algorithmic Changepoint and Anomaly Audit Log
The complete log of automated algorithmic scrutiny:
- Online Focus and FLOC candidate trigger times compared chronologically against the Operator's command log.
- Offline CPOP piecewise-linear slope segments across steady dwell boxes.
- Human classification tags initialed for every candidate: *Expected Step*, *Inspect / Split Hold*, or *No Impact*.

### Artifact 7: The Cryptographically Signed Raw CSV Data Archive
The full, un-retouched 1-second raw telemetry file exported directly from the edge gateway:
- Every active sensor channel recorded once per second with ISO-8601 UTC timestamps.
- Accompanied by a formal SHA-256 cryptographic checksum file (e.g., `LB_TEST_2026_H01_RAW.csv.sha256`) generated immediately upon file closing, guaranteeing that raw numbers have not been modified, filtered, or retroactively edited.

## What must be ruthlessly discarded

A formal handover package is an engineering audit record, not an advertising portfolio. The following items must be strictly excluded:

- **Uncalibrated Smartphone Photographs**: Do not include dozens of blurry smartphone photos of illuminated panel lamps, operator faces, or cable bundles. A photograph of a green LED is a souvenir; it is not evidence of electrical continuity or fluid enthalpy. (High-resolution thermal imaging captures with calibrated temperature scales are permitted only as supporting documentation for terminal lug checks).
- **Vendor Marketing Brochures & 3D Renderings**: Do not pad the document with glossy sales brochures, computer-generated concept art, or corporate profile slides. The audit package belongs to the physical machine on the floor, not the sales brochure.
- **Unredacted Confidential Client Data**: Do not include customer tenant identities, proprietary AI model names, unredacted security access codes, or internal corporate IP addresses. The report verifies thermodynamic and electrical performance; it does not map private data networks.
- **Un-Indexed Multi-Gigabyte Raw Log Dumps**: Do not paste millions of unformatted raw JSON log lines or raw terminal outputs into the PDF appendix. Store the raw CSV archive in a separate secure digital repository, cite its SHA-256 hash, and keep the formal report PDF clean, readable, and focused.

## The structure of the archive folder

Organize the final digital handover package into a clean, standardized folder directory structure:

```
├── 01_Executive_Flash_Report.pdf # The signed 1-page summary
├── 02_Preparation_and_Baseline.pdf # Cold gates & hydraulic calibration
├── 03_Consistency_and_Uniformity.pdf # CV calculations & multi-cabinet balance
├── 04_Step_Data_Blocks_and_Enthalpy.pdf # Thermodynamic reconciliation tables
├── 05_Time_Series_Charts.pdf # High-res oscillograms & dynamic steps
├── 06_Changepoint_Audit_Log.pdf # Focus / FLOC / CPOP candidate log
├── 07_Raw_Telemetry_Archive/
│ ├── LB_RAW_1HZ_TELEMETRY.csv # Complete 1s raw data file
│ └── LB_RAW_1HZ_TELEMETRY.csv.sha256 # Immutable SHA-256 cryptographic hash
└── 08_Calibration_Certificates/
 ├── PT100_RTD_Calibration.pdf # NIST/ISO 17025 calibration sheets
 ├── Vortex_Flow_Meter_Cal.pdf # Factory flow calibration certificate
 └── Power_Transducer_Class02.pdf # Electrical meter calibration tag
```

When an auditor or commissioning agent receives this package, they can verify the SHA-256 hash of the raw CSV file in five seconds, re-run the aggregation calculations in Python, and independently confirm every number on the executive flash report.

That is the standard of an engineering field guide.

## Decisions to record

Before sealing the formal handover package, verify and document:

- The calculated SHA-256 checksum of the raw CSV telemetry file, signed by the Recorder.
- The archive storage URI or repository location where the immutable raw files are stored.
- The list of all included instrument calibration certificates and their expiration dates.
- The final acceptance signatures of the Sheet Owner and the Third-Party CxA.
