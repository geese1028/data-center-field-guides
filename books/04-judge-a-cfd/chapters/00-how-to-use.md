# 0. How to use this book

This book has two explicit engineering jobs:
1. **Benchmark the Physical Room**: Establish a disciplined, multi-point field measurement protocol so that a numerical fluid dynamics simulation can be calibrated against physical reality rather than artistic intuition.
2. **Audit the Simulation Report**: Use the resulting computational fluid dynamics (CFD) report to make exactly one verified engineering decision, while formally refusing the speculative conclusions consultants frequently attempt to extract from color-contour plots.

It is not a CFD solver manual. It will not teach you how to click buttons inside ANSYS Fluent, Cadence Celsius EC (6SigmaDCX), or OpenFOAM, nor will it provide a decorative tour of rainbow temperature slices. 

The preceding books in this series accepted the liquid load bank under factory conditions (Book 01), audited high-frequency telemetry flash reports (Book 02), and executed the multi-megawatt thermal verification on the data hall floor (Book 03). This book begins when an engineering consultant, equipment vendor, or design firm hands you a bound CFD simulation report, or when you are tasked with capturing the physical baseline data that will determine whether that model may legally speak for the facility.

```
+----------------------------------------------------------------------------------------------------+
| THE TWO CONTRACTUAL AUDIT ROLES OF CFD |
+------------------------------------+---------------------------------------------------------------+
| 1. PHYSICAL BENCHMARKING (FLOOR) | 2. REPORT AUDITING (DESK) |
+------------------------------------+---------------------------------------------------------------+
| • 2-point CRAH supply averages | • Deconstruct the 6 mandatory input blocks |
| • 3-point CRAH return averages | • Audit solver residuals (< 10^-4) & mass balance (< 0.1%) |
| • 3-tier rack inlet probe trees | • Enforce single permitted decision domain |
| • Active PDU kW (zero nameplate) | • Strike speculative statements ("Hall Passed", "Add 50 kW") |
+------------------------------------+---------------------------------------------------------------+
```

When you conclude your audit, you must deliver two completed, auditable master sheets:
- **Sheet 1 (The Measurement & Calibration Record)**: Documents exactly where field probes were placed, how many points were averaged at each cooling unit opening, the three-tier vertical rack inlet temperatures, the active electrical feed power, and the named physical inputs altered during model calibration.
- **Sheet 2 (The Report Use & Decision Gate)**: Records the single decision the CFD report is authorized to support, verifies the presence of the six mandatory input blocks, confirms that every plot specifies its cutting plane coordinates, and formally logs the speculative sentences that were struck from the report executive summary.

If you are walking into the data hall tomorrow with thermal probes, turn to Chapter 6 and print Sheet 1. A blank cell is an automated stop. An inlet temperature copied from a previous facility report is a fabricated record.

## What you may copy

You may copy the master sheet headings, measurement grids, and audit checklists into your project commissioning file. You may not paste a colorful CFD temperature contour into a facility executive summary and declare that the image constitutes an engineering validation. 

The data hall has its own mechanical P&IDs, architectural layouts, and thermal boundary conditions. This field guide dictates what must be physically measured before a numerical model is permitted to represent those drawings, and establishes the strict boundaries within which a completed report may be used. It does not replace the professional engineer of record.

## Decisions to record before reading the report

- The single contractual decision the CFD report is commissioned to answer.
- The physical multi-point calibration grid executed on the data hall floor.
- The specific sentences you will formally refuse to sign based solely on color contours.
- The reference date of the physical measurements compared against the model geometry freeze date.
