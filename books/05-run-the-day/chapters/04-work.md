# 4. Work That Is Allowed

Work performed in a production data center without a validated, written method is not engineering; it is gambling with the customer's business.

```
+-----------------------------------------------------------------------------+
| OPERATIONAL DOCUMENTATION PYRAMID |
| |
| /\ |
| / \ |
| / PTW\ PERMIT TO WORK |
| /------\ Who, Where, When, Tools |
| / \ |
| / MOP \ METHOD OF PROCEDURE |
| /------------\ Step-by-Step, Isolations, Backout|
| / \ |
| / SOP \ STANDARD OPERATING PROCEDURE |
| /------------------\ Routine Shift Rounds & Valve Lineups|
| / \ |
| / EOP \ EMERGENCY OPERATING PROCEDURE |
| /------------------------\ Immediate Muscle Memory Safe-State |
+-----------------------------------------------------------------------------+
```

![Procedural Governance Pyramid](../figures/fig-02-sop-mop-eop-governance-pyramid.png)

Four distinct operational documents govern every physical action on site. Never conflate their functions.

## Standard Operating Procedures (SOP)

An SOP governs recurring, baseline operations where the system configuration remains within normal operating limits:
- Executing daily physical shift rounds.
- Conducting chemical water sampling and glycol refractometer tests.
- Operating the manual bypass valve on a water softener skid.
- Performing routine filter differential pressure checks.

Every SOP must exist as a printed, laminated document physically located at the point of work (e.g., mounted inside the CDU enclosure or on the wall of the water treatment plant). An SOP that exists only as a PDF buried in a corporate intranet directory is useless to a technician holding a sample flask.

## Method of Procedure (MOP)

A MOP governs any scheduled, non-routine activity that touches critical infrastructure, alters equipment redundancy, or introduces risk of electrical or thermal disruption:
- Racking in or racking out a 480V air circuit breaker.
- Isolating a primary plate heat exchanger for acid cleaning.
- Replacing a mechanical seal on a 75 kW secondary loop pump.
- Updating firmware on a central Building Management System controller.

Every MOP must contain six mandatory structural sections:
1. **Scope and Equipment Identification**: Explicitly naming the assets by unique equipment tag, building, room, and coordinate.
2. **Pre-Requisite Conditions**: Verifying that redundant systems (N+1 or 2N) are 100% operational, fully available, and free of active alarms before work commences.
3. **Required Personal Protective Equipment (PPE) & Specialized Tools**: Arc-flash suits, calibrated torque wrenches, insulated tools, pressure gauges, and spill containment kits.
4. **Step-by-Step Execution Sequence**: Numbered, sequential actions with checkboxes and signature blocks for both the Performer and Checker at every single step.
5. **Detailed Back-Out Plan**: The precise, pre-calculated sequence of actions required to abort the work and return the plant to a 100% stable, redundant operational state at any point during the window.
6. **Sign-Off and Technical Acceptance**: Formal verification that the equipment has been restored to service, tested under load, and that all temporary jumpers, LOTO padlocks, and tools have been removed.

A MOP drafted or edited on a clipboard while standing in front of an open electrical cabinet is an incident report waiting to happen. If a procedural step cannot be completed as written, the technician must stop work, back out to the last safe step, and seek formal engineering re-approval.

## Emergency Operating Procedures (EOP)

An EOP governs the immediate, high-stress response during an active equipment failure or catastrophic event:
- Uncontrolled secondary liquid cooling loop leak (> 50 LPM).
- Complete loss of external utility medium-voltage grid power.
- Catastrophic failure of an automatic transfer switch (ATS).
- Chiller plant electrical bus fire requiring emergency power off (EPO).

An EOP is designed for raw muscle memory. It must never exceed **two pages** in length. An EOP that contains twenty pages of narrative text is an engineering textbook, not an emergency procedure.

An effective EOP names only three things:
1. **The Stop**: The immediate manual actions to halt further damage (e.g., hit the emergency isolation valve button `EIV-101`, trip the battery disconnect breaker).
2. **The Call**: The exact operational role or phone number to summon emergency response (e.g., Duty Manager radio channel 1, municipal fire dispatch).
3. **The First Safe State**: The verified stable operating mode to hold while incident management takes over (e.g., transition remaining IT load to secondary bus B, engage emergency glycol makeup pump).

Once the first safe state is secured, the EOP ends. All subsequent investigative, restoration, or repair work converts immediately into a planned operation governed by a formal MOP.

## Permit to Work (PTW)

A Permit to Work sits atop the procedural framework. It is the legal and operational authorization granted by the Duty Manager permitting specific individuals to execute an approved MOP within an exact physical space during a defined time window.

A valid PTW enforces four hard constraints:
- **Location**: Specific room, aisle, and cabinet. Working outside the permit boundary is a direct safety violation.
- **Time Window**: Explicit start and end timestamps. An expired permit is an immediate Stop Work command.
- **Personnel**: Named individuals with verified qualification records on file.
- **Lockout/Tagout (LOTO)**: Verification that all hazardous electrical, hydraulic, pneumatic, and chemical energy sources are physically locked, tagged, and zero-energy verified (test-before-touch).

```
+-------------------------------------------------------------------------+
| PTW & LOTO AUDIT GATES |
| |
| [GATE 1] Approved MOP attached with complete back-out procedure |
| [GATE 2] Personnel qualifications verified against site trade matrix |
| [GATE 3] Zero Energy Verification: Multi-meter test & pressure bleed |
| [GATE 4] Physical LOTO hasp, red lock, and danger tag applied |
| [GATE 5] Redundancy check: Alternate path verified carrying load |
+-------------------------------------------------------------------------+
```

## Critical Spares Verification

No maintenance procedure may commence until all critical replacement parts are physically present at the job site.

A "critical spare" is not whatever parts happen to be sitting in the warehouse. A critical spare is the exact component whose failure or unavailability would prevent the execution of the MOP's back-out plan. For a secondary CDU pump replacement, the critical spares include:
- Replacement mechanical seal assembly with matching EPDM elastomers.
- Set of factory-spec mating gaskets for suction and discharge flanged connections.
- 50 liters of pre-mixed 25% propylene glycol solution.
- Calibrated torque wrench with current calibration certificate.

If the technician opens the CDU enclosure and then discovers that the replacement flange gasket is missing from the parts cage, the job does not start. Hoping that the old gasket can be scraped off and reused without leaking is how secondary cooling loops spray glycol across 400V busways.

## Decisions to Record

- All active SOPs verified present as physical, readable documents at the equipment.
- All MOPs approved for today's shift, with service impact classifications recorded.
- LOTO registry numbers and physical padlock tag IDs applied to equipment.
- Exact expiration timestamps for all active Permits to Work.
- Confirmation that all critical spares were visually inspected and verified on site before permit issuance.
