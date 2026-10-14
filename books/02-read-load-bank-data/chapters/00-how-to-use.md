# 0. How to use this book

This book is about the flash report. Not the physical machine, and not the complete facility hall. The first book (*Design and Build a Liquid Load Bank for NVL72 Racks*) accepted the prototype load bank on the shop floor and at the bench. The third book (*Finish a Liquid Cooling Verification*) runs the comprehensive data hall commissioning campaign and leaves seven permanent operational sheets. This volume sits precisely between them: it governs the data that leaves the machine. It tells you what a test run must record, how raw telemetry is audited, and what mathematical evidence must exist in the file before anyone in the room is legally or technically permitted to write "PASS."

In mission-critical data center engineering, a liquid cooling test is not valid because an afternoon felt smooth, because a vendor smiled, or because an uncalibrated monitoring dashboard rendered a calm, horizontal line. A calm line is frequently the signature of a frozen buffer or an unpolled register. This field guide provides the rigorous methodology required to turn high-density liquid and air load-bank runs into an immutable, audit-grade flash report that a stranger can reconstruct from first principles.

The structure of this report is derived from actual operational commissioning campaigns executing Level 4 Functional Performance Testing (FPT) and Level 5 Integrated System Testing (IST) across megawatt-scale AI computing facilities. Where this method requires a flow rate, an operating temperature, a differential pressure, or an electrical voltage, this book preserves the cell and insists that the limiting value be filled from your own engineering specification or the equipment document then in force, cited by document title and revision. Do not invent an operating threshold out of folklore, and do not copy numbers from an obsolete drawing because a previous air-cooled hall happened to use them.

When you finish, you must be able to hand an independent auditor a flash report containing five explicit scene passes, a multi-cabinet consistency check, and an exhaustive data block for every commanded load plateau. If even a single required pass cannot be written, the overall test verdict is not a pass. A pretty curve does not outvote a blank cell.

## What this volume owns

This book owns the translation of live physical phenomena into an immutable digital record. Specifically, it owns:

1. **The Preparation Block**: The pre-heat validation gate that proves the test cluster is full, vented, properly powered, and thermally stable before a single watt of heat is energized.
2. **The Five Scene Passes**: The definitive five-line audit structure—Pretest, Gradient, Overload, Step Change, and Single-Feed Fault—that prevents partial demonstrations from masquerading as full verifications.
3. **Multi-Cabinet Consistency**: The statistical application of the Coefficient of Variation ($CV = \frac{\sigma}{\mu} \times 100\%$) across parallel load-bank cabinets to identify hydraulic imbalance, manifold starvation, and electrical phase asymmetry.
4. **Metrology & Sampling Rigor**: The strict distinction between 1-second raw turbulent samples and 60-second rolling means, accompanied by the variance check (σ² > 0) that immediately exposes frozen-register fraud.
5. **Thermodynamic Heat Reconciliation**: The first-principles energy balance comparing commanded electrical power against secondary liquid enthalpy absorption and companion air heat release (P_elec = Q_liquid + Q_air + Q_loss).
6. **Telemetry Hop Architecture**: The deterministic journey from physical immersion RTDs and vortex flow meters through Modbus-TCP registers and MQTT brokers, enforcing strict bans on painted gaps, stale repeats, and cached retained messages.
7. **Algorithmic Changepoint Rules**: The precise operational boundaries governing online detectors (Focus, FLOC) and offline fits (CPOP), establishing that algorithms serve only as rulers to suggest candidate inspection windows, never as automated sign-off authorities.

What this book does not own: it does not design your building hydronic plant, it does not size your central cooling towers or chillers, and it does not configure your site-specific DCIM network switches. Those belong to the facility design basis and the project book. This book stops at the boundary of the test file.

## Four distinct human roles

A test file cannot be audited if the person who wrote the software is the same person who signs the acceptance of its data. This book requires four distinct human roles to be named on the cover page of every flash report, even if staffing constraints require individuals to share duties across non-conflicting lines:

- **1. The Sheet Owner (Specification Custodian)**: The engineer who owns the technical requirements sheet and the cited document revision. The Sheet Owner ensures that all limits, floor values, and dwell intervals match the frozen design basis. The Sheet Owner is strictly forbidden from quietly weakening a stop condition or waiving a failed cell in the hallway during the pressure of a test run.
- **2. The Operator (Control Pilot)**: The technician or test engineer who commands the load bank stages, operates balancing valves, commands step jumps, and executes breaker trips. The Operator must not be the author of the controller's internal telemetry firmware.
- **3. The Recorder (Objective Chronicler)**: The person who logs chronological timestamps, notes raw register alarms, records boring passes, and documents uncommanded transients without smoothing the curve or discarding "inconvenient" initial runs.
- **4. The Stranger (Independent Audit Authority)**: An engineer or commissioning agent (CxA) who was not involved in the fabrication of the load bank or the installation of the temporary piping. The Stranger is handed the un-retouched raw CSV export and must be able to independently verify every mathematical claim without verbal coaching from the test crew.

If your commissioning team consists of only two people, the Stranger must still be an outside party—an owner's representative, a quality manager, or an engineer from an adjacent shift. Self-acceptance is the root cause of stale data surviving into production.

## What you may copy and what you may not

You may copy the structural headings of this field guide into your own engineering templates: the preparation block, the five passes, the consistency criteria, the step data blocks, and the external gear boundaries.

You may not copy a paragraph from this book into a vendor contract and call it an engineering specification. You may not paste a marketing rendering into the report and call it an equipment drawing. And you may not paste an unverified vendor CSV export into your handover package and call it an independent analysis.

## How to read and apply this guide

Read this field guide through once from start to finish to understand the interdependent architecture of the data pipeline. Then, execute the flash report in the exact chronological order of the testing day:

1. Record the preparation block and establish the cold baseline minute before commanding heat.
2. Verify all pretest cells against the cited engineering limits.
3. Walk the active scenes: the stepped gradient, the overload visit, the sudden step change, and the 2N single-feed loss drop test.
4. Execute the multi-cabinet consistency analysis across all parallel cabinets.
5. Compile the step data blocks and reconcile the thermodynamic heat balance.
6. Audit the telemetry stream for frozen registers and stale repeats.
7. Initial the final sentence or file the explicit refusal.

A skipped chapter or an unrecorded cell is how an unverified 60-second burst becomes an illegitimate 30-minute steady-state claim. Follow the method.

## Decisions to record

Before opening the first valve or powering the control bus, record these facts in ink:

- The unique Run Identification code (e.g., `LB-TEST-2026-H01-A`) and the data hall location.
- The exact document title and revision mark of the requirements specification then in force.
- The names and signatures of the four designated roles: Sheet Owner, Operator, Recorder, and Stranger.
- The full list of parallel load-bank cabinet serial numbers included in the test cluster.
- The list of scenes this specific run is contracted to attempt.
