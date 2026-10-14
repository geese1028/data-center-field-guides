# 15. Which sheet to hold

Chapter 16 provides the seven master engineering record sheets. Print them on waterproof paper, assemble them in a dedicated field binder, and take them onto the data hall floor.

Do not attempt to summarize these grids into high-level descriptive paragraphs after the test concludes, discarding the raw field data. An auditor inspecting a verification package expects to see the actual ink impressions, timestamped entries, witness initials, and instrument serial numbers recorded while standing in the aisle.

```
+----------------------------------------------------------------------------------------------------+
| THE SEVEN MASTER FIELD SHEETS |
+-------+-------------------------------+-------------+------------------+---------------------------+
| SHEET | TITLE & VERIFICATION SCOPE | CX TIER | RESPONSIBLE LEAD | MANDATORY EXECUTION TIMING|
+-------+-------------------------------+-------------+------------------+---------------------------+
| 01 | Pre-Energization Static QA | Level 2 / 3 | Electrical PE & | Before closing any supply |
| | & Hydraulic Hold Check | | Mechanical PE | breaker or opening fluid. |
+-------+-------------------------------+-------------+------------------+---------------------------+
| 02 | Autonomous CDU Protection | Level 4 FPT | Controls PE & | Before introducing any |
| | & Physical Alarm Injections | | Mechanical PE | thermal heat to the loop. |
+-------+-------------------------------+-------------+------------------+---------------------------+
| 03 | Multi-Stage Thermal Step & | Level 5 IST | Test Lead & | One distinct copy executed|
| | Enthalpy Heat Closure Log | | Test Technician | per thermal step rung. |
+-------+-------------------------------+-------------+------------------+---------------------------+
| 04 | Dynamic Transient Failure & | Level 5 IST | Test Lead & | Executed at 100% full load|
| | Redundancy Ride-Through Log | | Controls PE | during simulated faults. |
+-------+-------------------------------+-------------+------------------+---------------------------+
| 05 | Controlled De-Energization & | Closeout | Test Lead & | Executed in strict order |
| | Demobilization Protocol | Level 6 | Electrical PE | during shift shutdown. |
+-------+-------------------------------+-------------+------------------+---------------------------+
| 06 | Cold No-Heat Baseline Pump | Level 4 / 5 | Mechanical PE & | Executed at 20°C with VFD |
| | & Loop Resistance Curve | | Test Technician | modulation locked off. |
+-------+-------------------------------+-------------+------------------+---------------------------+
| 07 | CDU Autonomous Control Logic | Level 4 / 5 | Controls PE & | Executed across all units |
| | & Supervisory Interface Audit | | Vendor Specialist| with vendor logic attached|
+-------+-------------------------------+-------------+------------------+---------------------------+
```

## Floor Execution Rules

1. **Two People on the Tools**: One engineer operates the calibrated measurement instrument; a second engineer logs the measured value in ink. Never attempt to read a display, remember the number, and write it down five minutes later.
2. **Every Cell Is an Obligation**: A blank cell is an automated stop. If a parameter is not included in the scope of this specific test, mark it **"N/A (Out of Scope per Claim Rev [X])"** and initial the entry. Never leave a cell empty.
3. **Copy Sheet 3 per Thermal Step**: Sheet 3 is not a single form. Print multiple copies. Execute a separate, complete Sheet 3 for each step in the thermal ladder (25%, 50%, 75%, 100%, and 110%). Never combine data from multiple load steps onto a single sheet.
4. **Attach Raw Telemetry Checksums**: Record the file name and SHA-256 checksum of the corresponding high-frequency CSV log directly in the header of each sheet.
5. **No Retroactive Alterations**: If an entry was written incorrectly, draw a single horizontal line through the error, write the correct value alongside, and initial the correction. Never use correction fluid or scribble over a field entry.

## The Physical Binder Assembly

Organize the physical field binder into seven dedicated tabs corresponding to the seven sheets. Precede each tab with the approved test script revision and the instrument calibration certificates required for that phase.

When testing concludes, this physical binder is scanned in full color and forms the permanent core of the Level 6 Final Commissioning Report.
