# 6. Scripts before heat

No dynamic commissioning test may be executed from memory or oral instructions. A test conducted without a pre-approved, step-by-step test script is merely an informal equipment demonstration. It cannot support an engineering completion certificate.

A script that the testing team drafted but which the Owner’s Project Engineer has not formally reviewed and signed is merely an internal working document. It carries no contractual authority. Executing against an unapproved draft leaves the testing team fully exposed to commercial disputes and legal liability if an equipment failure occurs.

```
+----------------------------------------------------------------------------------------------------+
| COMMISSIONING DOCUMENT HIERARCHY |
+------------------------------------+---------------------------------------------------------------+
| 1. CODES & STANDARDS | ASHRAE 0-2019, ASHRAE 90.4, NFPA 70, IEC 60364, BSRIA BG 29. |
+------------------------------------+---------------------------------------------------------------+
| 2. CONTRACT SPECIFICATIONS & BOD | CSI Div 23 & 26, Owner Project Requirements, As-Built P&IDs. |
+------------------------------------+---------------------------------------------------------------+
| 3. COMMISSIONING PLAN (Cx Plan) | Governance rules, level gates, witness protocols, schedules. |
+------------------------------------+---------------------------------------------------------------+
| 4. FUNCTIONAL TEST PROCEDURES (FPT)| Pre-approved, step-by-step scripts with exact numeric bands. |
+------------------------------------+---------------------------------------------------------------+
| 5. MASTER FIELD SHEETS (INK LOGS) | Floor records signed in ink; raw time-series sensor files. |
+------------------------------------+---------------------------------------------------------------+
```

## The Anatomy of an Auditable Test Script

Every Functional Test Procedure (FPT) and Integrated System Test (IST) script must be structured with consistent, auditable engineering sections:

1. **Test Scope and Boundary**: The specific mechanical and electrical components under test, and the exact physical boundary separating them from adjacent operational equipment.
2. **Governing Reference Documents**: Direct citations of the governing P&ID revision, electrical single-line diagram (SLD), and equipment submittals. Every tolerance must reference a specific contract clause or manufacturer standard; an acceptance tolerance with no cited source is merely an unverified opinion.
3. **Instrumentation and Calibration Schedule**: The specific instrument classes, serial numbers, and calibration certificate IDs required to execute the procedure.
4. **Prerequisite Verification Gate**: Written verification that all preceding level requirements (such as static uncrating, de-energized megger checks, and hydrostatic pressure holds) are fully signed off.
5. **Safety Controls and Environmental Boundaries**: Mandatory Personal Protective Equipment (PPE), arc-flash boundary definitions, spill containment staging, and verified emergency stop paths.
6. **Step-by-Step Execution Sequence**: A sequential table detailing every manual action, the exact physical feedback to observe, the expected numerical tolerance band, and dedicated sign-off cells for measured data and witness initials.
7. **Explicit Stop Conditions**: Clear operational limits that mandate an immediate test halt if breached (such as secondary coolant temperature exceeding 45.0°C, secondary pressure dropping below 100 kPa, or supply phase voltage unbalance exceeding 2.0%).

```
+----------------------------------------------------------------------------------------------------+
| STANDARD TEST SCRIPT STEP STRUCTURE |
+----+-----------------------+-----------------------------+--------------------+-------+------------+
|STEP| ACTION COMMAND | EXPECTED PHYSICAL RESULT | ACCEPTANCE BAND |MEASURE|SIGN / TIME |
+----+-----------------------+-----------------------------+--------------------+-------+------------+
|4.2 | Ramp Load Bank to 50% | Active power stabilizes | 600 kW +/- 1.5% | [ ] | Init: ____ |
| | (Step 2: 600 kW total)| Secondary supply T increases| 36.0°C +/- 0.5°C | [ ] | Time: ____ |
| | Dwell: 45 minutes | Heat balance closure ratio | 97.0% to 101.5% | [ ] | Sheet 3 ref|
+----+-----------------------+-----------------------------+--------------------+-------+------------+
```

## Freezing Script Revisions on the Floor

The Commissioning Kickoff Meeting establishes the specific approval status required before a script may be executed on the floor. Only scripts bearing the formal status stamp **"APPROVED FOR EXECUTION - REV [X]"** are permitted in the data hall.

If during testing the mechanical plant exhibits unexpected dynamics that the approved script did not anticipate, modifying the script on the floor with a pencil note is strictly prohibited. Uncontrolled redlining allows the test procedure to quietly adapt to whatever the plant happens to do.

When a procedural modification is necessary:
- The Test Lead pauses the test.
- A formal Engineering Change Notice (ECN) is drafted documenting the deviation, its technical justification, and the amended steps.
- The ECN is signed by the Test Lead, the Contractor Lead, and the Owner’s Project Engineer.
- The script revision is incremented (e.g., Rev 1.0 to Rev 1.1) and re-issued.

If the owner refuses the ECN, testing resumes under the original script, and the failure of the plant to meet the original expected result is logged on the master punch list.

## The Mandatory Script Suite for a High-Density Liquid Hall

A complete verification campaign requires a comprehensive suite of distinct, standalone scripts. Attempting to combine multiple operational verifications into a single high-level procedure produces an unwieldy document that inevitably glosses over critical safety and performance checks.

The verification campaign requires nine dedicated test scripts:

### Phase 1: Static Pre-Start Checklists (Level 2 / Level 3)
- **Script 01: Physical Uncrating, Alignment & Visual QA**: Verification of load-bank chassis integrity, hose routing, fitting seals, and seismic tie-downs.
- **Script 02: De-Energized Electrical Megger & Phase Rotation**: Insulation resistance testing (≥ 100 MΩ at 1000V DC), ground continuity (≤ 0.1 Ω), and confirmation of clockwise A-B-C phase sequence.
- **Script 03: Secondary Loop Flushing, Hydrostatic Hold & Air Purge**: Chemical flushing velocity verification (≥ 1.5 m/s per BSRIA BG 29/2020), hydrostatic pressure hold (1.5× working pressure for 2 hours with zero decay), and automatic deaeration.

### Phase 2: Single-System Functional Testing (Level 4 FPT)
- **Script 04: Autonomous CDU Startup, Flow & Pressure Baseline**: Verification of canned pump VFD ramp profiles, manual differential-pressure setpoint tracking, and cold system resistance.
- **Script 05: CDU N+1 Pump Failover & Autonomous Control**: Physical tripping of the primary pump VFD; verification of standby pump auto-start within < 1.5 s with zero loop cavitation.
- **Script 06: Alarm Injection & Point-to-Point Telemetry**: Physical injection of simulated faults (secondary low flow, expansion tank low level, leak detection rope wetting) and cross-checking BMS telemetry against local instrumentation.

### Phase 3: Integrated System Testing (Level 5 IST)
- **Script 07: Cold No-Heat Baseline Pump Curve**: Hydraulic head versus flow profiling across 4 manual valve throttling points with automated VFD control locked off.
- **Script 08: Multi-Tier Thermal Heat Ladder & Overload Dwell**: Stepped thermal execution (25%, 50%, 75%, 100% full design load, and 110% overload margin) with minimum 45-minute dwells and a 4-hour full-load soak.
- **Script 09: Dynamic Transient Failure & Emergency Shutdown**: 2N primary power feed cut, facility chilled water loss ride-through, and controlled de-energization shutdown sequence.

## The "One Script, One Signature" Principle

Every script in the suite stands as an independent contractual document with its own dedicated sign-off block. Combining a successful cold pump curve and a failed thermal overload step into a single combined signature creates a fundamentally ambiguous record.

Each script must produce its own unambiguous verdict: **PASS**, **FAIL**, or **NOT EXECUTED**. Any unresolved failure within a script immediately generates an entry in the master Issues Log.

## Decisions to record before test start

- The comprehensive list of all nine test scripts, with frozen revision numbers and signed approval stamps.
- The contract document numbers supporting every numerical tolerance and acceptance band.
- The formal ECN process for handling floor revisions.
- Confirmation that no script is in draft status.
