# 15. Which sheet to hold

Chapter 16 provides the seven master engineering record sheets. Print them on waterproof paper, assemble them in a dedicated field binder, and take them onto the data hall floor.

Do not attempt to summarize these grids into high-level descriptive paragraphs after the test concludes, discarding the raw field data. An auditor inspecting a verification package expects to see the actual ink impressions, timestamped entries, witness initials, and instrument serial numbers recorded while standing in the aisle.

**THE SEVEN MASTER FIELD SHEETS**

| SHEET | TITLE & VERIFICATION SCOPE | CX TIER | RESPONSIBLE LEAD | MANDATORY EXECUTION TIMING |
| :--- | :--- | :--- | :--- | :--- |
| 01 | Pre-Energization Static QA & Hydraulic Hold Check | Level 2 / 3 | Electrical PE & Mechanical PE | Before closing any supply breaker or opening fluid. |
| 02 | Autonomous CDU Protection & Physical Alarm Injections | Level 4 FPT | Controls PE & Mechanical PE | Before introducing any thermal heat to the loop. |
| 03 | Multi-Stage Thermal Step & Enthalpy Heat Closure Log | Level 5 IST | Test Lead & Test Technician | One distinct copy executed per thermal step rung. |
| 04 | Dynamic Transient Failure & Redundancy Ride-Through Log | Level 5 IST | Test Lead & Controls PE | Executed at 100% full load during simulated faults. |
| 05 | Controlled De-Energization & Demobilization Protocol | Closeout Level 6 | Test Lead & Electrical PE | Executed in strict order during shift shutdown. |
| 06 | Cold No-Heat Baseline Pump & Loop Resistance Curve | Level 4 / 5 | Mechanical PE & Test Technician | Executed at 20°C with VFD modulation locked off. |
| 07 | CDU Autonomous Control Logic & Supervisory Interface Audit | Level 4 / 5 | Controls PE & Vendor Specialist | Executed across all units with vendor logic attached |

## Floor Execution Rules

1. **Two People on the Tools**: One engineer operates the calibrated measurement instrument; a second engineer logs the measured value in ink. Never attempt to read a display, remember the number, and write it down five minutes later.
2. **Every Cell Is an Obligation**: A blank cell is an automated stop. If a parameter is not included in the scope of this specific test, mark it **"N/A (Out of Scope per Claim Rev [X])"** and initial the entry. Never leave a cell empty.
3. **Copy Sheet 3 per Thermal Step**: Sheet 3 is not a single form. Print multiple copies. Execute a separate, complete Sheet 3 for each step in the thermal ladder (25%, 50%, 75%, 100%, and 110%). Never combine data from multiple load steps onto a single sheet.
4. **Attach Raw Telemetry Checksums**: Record the file name and SHA-256 checksum of the corresponding high-frequency CSV log directly in the header of each sheet.
5. **No Retroactive Alterations**: If an entry was written incorrectly, draw a single horizontal line through the error, write the correct value alongside, and initial the correction. Never use correction fluid or scribble over a field entry.

## The Physical Binder Assembly

Organize the physical field binder into seven dedicated tabs corresponding to the seven sheets. Precede each tab with the approved test script revision and the instrument calibration certificates required for that phase.

When testing concludes, this physical binder is scanned in full color and forms the permanent core of the Level 6 Final Commissioning Report.
