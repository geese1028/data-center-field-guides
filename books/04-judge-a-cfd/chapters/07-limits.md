# 7. What this book does not own

This field guide will inevitably be misused by individuals seeking an all-inclusive textbook on computational fluid dynamics. Establish strict professional boundaries here.

A field audit method maintains integrity only when its boundaries are sharply drawn. Expanding this guide into software solver programming or mechanical design dilutes its authority.

```
+----------------------------------------------------------------------------------------------------+
| EXPLICIT NEGATIVE SCOPE BOUNDARIES |
+------------------------------------+---------------------------------------------------------------+
| WHAT THIS BOOK OWNS | WHAT THIS BOOK CANNOT AND DOES NOT OWN |
+------------------------------------+---------------------------------------------------------------+
| • Field multi-point calibration | • Commercial CFD solver algorithms, source code, or GUI menus |
| • Quantitative error metrics (MAE) | • Book 01 Scope: Load-bank design, manufacturing, and FAT |
| • The 6 mandatory input blocks | • Book 02 Scope: Telemetry anomaly algorithms (FLOC/Focus) |
| • Four permitted decision domains | • Book 03 Scope: Physical Level 5 load-bank floor testing |
| • Refusal of color-map speculation | • Silicon Physics: Chip junction temps ($T_j$), NVLink, AI ops|
| • The two master audit sheets | • Facility Design: Architectural, structural, and central MEP |
| • ASHRAE TC 9.9 compliance audit | • Next Facility: Copying room-specific averages across halls |
+------------------------------------+---------------------------------------------------------------+
```

## The Dedicated Boundaries

### 1. It Does Not Own the Solver Code or Commercial Software Menus
This book governs how to measure a physical room and how to audit an engineering report. It does not teach the internal finite-volume discretization schemes of commercial solvers (such as SIMPLE, PISO, or coupled algorithms), nor does it guide users through software menu interfaces. Those operations belong in the vendor’s documentation. Software mastery is not a substitute for physical measurement.

### 2. It Does Not Own Equipment Factory Acceptance (Book 01)
A CFD simulation model represents physical equipment through numerical boundary conditions (fan curves, pressure drop coefficients, and heat dissipation source terms). It does not certify that the physical load bank or server chassis was constructed safely, that its internal electrical contactors meet UL/IEC standards, or that its frame withstands seismic stress. Equipment acceptance belongs exclusively to Book 01.

### 3. It Does Not Own Telemetry Verification (Book 02)
This book cross-checks steady-state physical measurements against simulation probes. The mathematical validation of real-time time-series telemetry—including changepoint detection (FLOC/Focus), variance gating (σ² > 0), and quality bitmask verification—belongs to Book 02. A calm-looking CFD plot cannot override a time-series telemetry log that reveals thermal hunting.

### 4. It Does Not Own Physical Commissioning Verification (Book 03)
A CFD simulation is a predictive mathematical model; it is not a physical commissioning test. It cannot demonstrate that an actual N+1 pump will switch over in ≤ 1.5 seconds, that a check valve will seat without water hammer, or that electrical busbars will not overheat under full load. Physical facility verification belongs exclusively to the Level 5 integrated test procedures of Book 03.

### 5. It Does Not Own Silicon Performance and Compute Reliability
A whitespace CFD model resolves airflow and temperature fields in the air volume surrounding server racks. It possesses zero visibility into microchannel cold plate fluid dynamics, thermal interface material (TIM) degradation, silicon junction temperatures (T_j), or GPU memory throttling. A server rack operating in a 22.0°C cold aisle can still fail due to internal hardware defects. This book speaks strictly to the fluid boundary at the server intake bezel.

### 6. It Does Not Own the Next Data Hall
The physical measurement methodology (supply 2-point, return 3-point, 3-tier rack intake tree) and the report audit framework (the four permitted decisions and the refusal matrix) can be applied universally across mission-critical facilities. However, the specific numerical values—the measured temperatures, room flow rates, and calibration inputs—belong exclusively to the specific data hall audited. Copying numerical data from this report into another facility turns engineering verification into an unverified copy-paste exercise.

## Decisions to record before test start

- Re-affirmation that the commercial CFD solver manual is referenced, not duplicated.
- Explicit acknowledgment that CFD simulation does not replace Book 03 physical load-bank testing.
- The signed statement on Sheet 2 affirming that the report does not assert silicon reliability claims.
