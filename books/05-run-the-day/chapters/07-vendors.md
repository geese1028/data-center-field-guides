# 7. Vendors and Contractors

A third-party vendor or equipment manufacturer technician working inside your data center is a pair of hands operating under your legal permit. They are not an autonomous entity that you can leave unsupervised in an electrical vault.

| **VENDOR GOVERNANCE GATEWAY** |
| :--- |
| [GATE 1] Pre-Arrival Scope: Specific task, approved MOP, tool registry |
| ↓ |
| [GATE 2] Security & Safety In-Brief: Badge issued, LOTO verified, PPE audit |
| ↓ |
| [GATE 3] Active Escort: Qualified site technician assigned; never unescorted |
| ↓ |
| [GATE 4] Scope Boundary Enforcement: Stop Work if task leaves written MOP |
| ↓ |
| [GATE 5] Technical Closeout: Physical audit of work, old parts, site clean |
| ↓ |
| [GATE 6] Commercial Separation: Technical sign-off != Commercial invoice |

A manager who signs a visitor badge, points toward the battery room, and returns to their office has abandoned control of the facility. If that vendor drops a ratchet across a 480V busbar or opens the wrong isolation valve, the outage belongs to the manager, not the vendor.

## Pre-Arrival Scope Definition

Before a vendor crosses the security turnstile, their operational scope must be defined in writing with unambiguous boundaries:
- Exactly which equipment tag they are authorized to touch (e.g., *"Centrifugal Chiller CH-02 compressor oil filter assembly only"*).
- Exactly which equipment they are strictly prohibited from touching (e.g., *"Do not touch condenser water isolation valves or adjacent chiller CH-01 control panel"*).
- The definition of "Done": What specific physical tests, pressure readings, or operational milestones must be verified before the equipment is considered repaired.
- Deliverables required before departure: Factory field service report, calibrated tool test logs, serial numbers of all installed replacement components, and physical surrender of all failed parts for root-cause analysis.

A vendor work order that reads *"Annual preventive maintenance on UPS system"* is an invitation to disaster. It specifies no boundaries, no test limits, and no operational constraints. If the vendor does not provide an itemized, step-by-step MOP seventy-two hours in advance, cancel the site visit.

## The Dedicated Site Host

Every vendor working within critical electrical, mechanical, or whitespace areas must be accompanied by a dedicated, qualified site host from your operational shift team.

The site host does not perform the vendor's physical labor. The host's duties are:
1. **Scope Boundary Enforcement**: Continuously observe the vendor's actions. If the technician reaches toward an adjacent switchgear cubicle or begins opening a valve not listed in the MOP, the host immediately commands Stop Work.
2. **Emergency Reaction**: In the event of an arc-flash, chemical splash, or equipment trip, the host initiates the site Emergency Operating Procedure (EOP), summons medical support, and directs the safe-state isolation.
3. **Escort Control**: Ensure the vendor remains within the authorized physical work envelope and never wanders through production aisles unsupervised.

### Eliminating Casual Scope Creep ("While We're Here")

The most dangerous words in data center operations are a vendor technician saying:
> *"While we have the panel cover off, do you want me to quickly adjust the sensitivity setting on this ground-fault relay?"*

The answer is always an uncompromising **"No."**

A useful task discovered with the equipment open is not a helpful favor; it is an unreviewed, unpermitted engineering change:
- It possesses no approved MOP.
- It has undergone no Change Advisory Board risk assessment.
- It has no calculated back-out plan.
- The control room has not logged the plant into an abnormal operating state.

If the vendor identifies an unexpected defect or recommended adjustment during their work, log the finding into the site defect register. It will be scheduled, reviewed, and executed during a future authorized maintenance window under its own permit. Never allow spontaneous scope creep in a live facility.

## Technical Acceptance vs. Commercial Invoicing

Never allow the commercial urgency of a vendor's billing cycle to compromise technical acceptance.

Technical acceptance is a rigorous engineering verification that the equipment has been restored to full operational capability:
- The equipment has operated under full thermal or electrical load without abnormal vibration, temperature excursions, or fluid leakage.
- All digital communication channels (Modbus, BACnet, SNMP) between the equipment and the central BMS/EPMS have been re-established and verified.
- The work area has been cleaned, all debris, loose zip ties, and wire clippings removed, and all physical panel covers, dead-front shields, and safety interlocks re-installed.
- All old, failed components (burned contactors, worn mechanical seals, degraded capacitors) have been tagged, boxed, and transferred to the site quarantine storage room for forensic inspection.

The document you sign at the end of the vendor's visit is exclusively a **Field Service Verification of Work Performed**. It verifies that the vendor was on site and performed the numbered steps in the MOP.

It does not constitute commercial acceptance of the invoice, and it does not waive the facility owner's right to pursue warranty claims if latent defects emerge during subsequent operations. If commercial representatives press you to sign an unconditional commercial completion certificate before functional load testing is complete, note on the sheet: *"Work performed visually verified; functional technical acceptance pending 24-hour live load dwell."*

## Decisions to Record

- Pre-approved vendor scope of work and attached MOP registry number.
- Name of the dedicated on-shift site host assigned to the vendor.
- Scope boundary check: Confirmed zero deviation from written MOP, or recorded Stop Work command.
- Technical acceptance signed only after physical inspection and live load dwell verification.
- Serial numbers of installed components and quarantine bin location of failed parts.

## Third-Party Vendor Governance: Laptop Air-Gap, Firmware Checksums, and Tool Control

A manufacturer field service engineer (FSE) arriving to service a chiller VFD, a UPS static switch controller, or a liquid CDU PLC brings three severe operational vectors into the facility: unvetted laptop interfaces, unverified firmware binaries, and uncalibrated torque/test tools.

| Vendor Control Gate | Physical / Cyber Inspection Requirement | Quantitative Pass Criterion | Immediate Stop-Work Condition |
| :--- | :--- | :--- | :--- |
| **Gate 1: Method & Insurance** | Site-specific MOP cross-checked against actual cabinet serial numbers | Exact match to site SLD/P&ID tags | Generic factory procedure referencing wrong model/voltage |
| **Gate 2: Laptop & Media Hygiene** | Vendor service laptop cellular/Wi-Fi disabled; USB media scanned at kiosk | SHA-256 firmware hash matches OEM release bulletin | Laptop bridged simultaneously to corporate LTE and PLC Ethernet |
| **Gate 3: Calibrated Tool Audit** | Torque wrenches, multimeters, and pressure gauges checked for valid cert | NIST/ISO 17025 calibration sticker within 12-month validity | Uncalibrated gauge used to set safety relief or pressure switch |
| **Gate 4: Parameter Diff Backup** | Full backup of existing PLC/relay parameter file exported before write | Line-by-line diff confirms only authorized registers changed | Firmware flashed without saving local copy of running config |

## Escort-to-Vendor Ratios and Red-Zone / Green-Zone Work Permits

Inside energized electrical rooms, battery rooms, and live customer whitespace (Red Zones), the facility enforces a strict **1:1 or 1:2 Qualified Escort Ratio**: one Badged Critical Facility Technician must remain within direct line-of-sight and earshot of the vendor technician at all times. If the escort must leave the room for any reason, the vendor must step out into the corridor until relief arrives.
