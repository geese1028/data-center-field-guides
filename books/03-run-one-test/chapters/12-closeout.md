# 12. Close-out and turnover

A successful thermal heat test is not a facility turnover. Demobilizing load banks from a data hall merely signifies that dynamic verification has concluded. The formal transition of the facility from construction into live IT operations occurs under **Level 6 Close-Out, Turnover, and Operations Handover**.

A turnover certificate signed while punch list items remain unresolved or before the final commissioning report is audited is legally defective. Level 6 turnover is the formal milestone where the Facility Owner, the General Contractor, and the Commissioning Authority collectively certify that the mechanical, electrical, and control systems satisfy the Owner's Project Requirements and are safe to receive high-density compute infrastructure.

**LEVEL 6 TURNOVER DOCUMENT ARCHITECTURE**

| 01 | EXECUTIVE SUMMARY & VERIFIED CLAIM STATEMENT | The signed claim sentence, final project verdict, and summary of operational thermal capacity demonstrated. |
| :--- | :--- | :--- |
| 02 | SCOPE BOUNDARIES & EXCLUSION LETTERS | Explicit scope letters documenting unexecuted levels, seasonal deferred testing, and third-party systems out. |
| 03 | MASTER MILESTONE CERTIFICATES | Formal signed completion certificates for Levels 2, 3, 4, 5. |
| 04 | THE SEVEN SIGNED MASTER SHEETS | Sheets 1 through 7, fully executed, logged in ink, signed. |
| 05 | INSTRUMENT CALIBRATION LOG | Traceable ISO 17025 calibration certificates for all tools. |
| 06 | TIME-SERIES DATA REPOSITORY | Complete raw CSV logs, BMS trend exports, cryptographic SHA. |
| 07 | RESOLVED ISSUES REGISTER | Master Punch List showing 100% Cat 1 & Cat 2 items closed. |
| 08 | SYSTEMS MANUAL SUPPLEMENT | As-tested pump curves, operating bands, fail-safe setpoints. |
| 09 | OPERATIONS TRAINING RECORDS | Witnessed sign-off of facility staff SOP walkthrough. |

## Structure of the Final Commissioning Report

The Final Commissioning Report is the permanent engineering baseline of the liquid cooling infrastructure. Decades later, when the facility undergoes retrofits or failure investigations, engineering teams will refer to this report to verify initial operating parameters.

The report must be compiled with nine standardized sections:

### 1. Executive Summary and Certified Claim
Opens with the exact, unedited claim sentence formulated in Chapter 1. It provides an unambiguous operational summary: the total thermal capacity verified (e.g., 1.2 MW continuous), the primary cooling supply conditions, secondary flow balance metrics, and the formal certification that all tested systems operated within specification.

### 2. Scope Boundaries and Formal Exclusion Letters
A rigorous definition of boundaries. If Level 0 design review or Level 1 factory testing were excluded from the contract, the formal Scope Exclusion Letters signed by the owner must be embedded here. If seasonal testing (such as maximum summer ambient chiller stress testing) must be deferred to a later date, the Deferred Testing Protocol and scheduled execution date are formally documented.

### 3. Master Milestone Completion Certificates
Formal certificate pages for Level 2 (Receipt QA), Level 3 (PFC and Start-Up), Level 4 (Single-System FPT), and Level 5 (Integrated System IST). Each certificate must bear the ink signatures of the Commissioning Lead, Electrical PE, Mechanical PE, Contractor Executive, and Owner’s Authorized Representative.

### 4. The Seven Master Field Sheets
The completed, physical field record sheets (Sheets 1 through 7 from Chapter 16), scanned in full color showing all ink entries, witness initials, step timestamps, and field notes.

### 5. Calibrated Instrument Register
A complete traceability log listing every multimeter, power quality analyzer, ultrasonic flowmeter, digital thermometer, differential pressure transmitter, and thermal imaging camera deployed during testing. Embed copies of their ISO/IEC 17025 calibration certificates.

### 6. Raw Time-Series Data Repository
A structured archive containing the 1-second raw telemetry exports from the load banks, power meters, and BMS trend logs. To prevent post-test manipulation, generate a cryptographic hash (SHA-256 checksum) for every raw data file and record the hash table in the report appendix.

### 7. Resolved Master Issues Register
The final, printed copy of the Commissioning Issues Log. Every Category 1 and Category 2 defect must show its complete resolution history: initial finding, contractor remediation, witnessed re-test data sheet reference, and closeout signature. Any remaining open Category 3 cosmetic items must be bound by an approved 30-day closeout plan.

### 8. Systems Manual Operational Supplement
The operational bridge between commissioning data and daily facility operations. This section extracts critical baseline characteristics from the test data:
- The verified cold no-heat pump curve versus hot operating points (Sheet 6).
- Calibrated PID loop parameters for the primary modulating valve (TCV-101).
- The exact secondary fluid inventory (V_total) and glycol concentration (Refractometer verified 25.0% ± 0.5%).
- The emergency interlock logic matrix, defining hardware trip thresholds.

### 9. Operations Team Training Sign-Off
Documentation of formal operational handover training conducted with site facility engineers. Training must include physical walkthroughs of the emergency stop mechanisms, manual bypass valve operations, secondary fluid makeup procedures, and alarm acknowledgement workflows.

## The Final Page Boundary Statement

The final page of the report must protect the testing party and the owner by clearly stating what the verification did not cover:

| **FORMAL BOUNDARY STATEMENT** |
| :--- |
| "This verification campaign certifies the performance of the liquid cooling infrastructure under |
| simulated electrical and thermal load conditions as explicitly documented herein. It does not |
| certify the operational reliability, compute workload throughput, or warranty compliance of |
| production IT hardware. Systems marked as excluded or not demonstrated remain outside the scope |
| of this certification. All verified capacities are contingent upon the facility operating within |
| the environmental, electrical, and hydraulic boundaries established in this report." |

## Decisions to record before test start

- The final report template and documentation archive format.
- Confirmation that 100% of Category 1 and Category 2 punch list items are closed.
- The SHA-256 cryptographic checksum register for all raw telemetry files.
- The formal Level 6 Turnover Certificate, signed by all primary stakeholders.
- The signed Facility Operations Training Register and Systems Manual supplement.
