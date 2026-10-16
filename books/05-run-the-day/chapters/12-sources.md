# 12. Titles, Standards, and the Copyright Line

A professional operations team cites its sources with exact academic and legal rigor. We operate to published, peer-reviewed engineering standards, statutory safety codes, and binding commercial agreements.

## Authoritative Engineering Standards & Codes

When drafting Methods of Procedure (MOP), Emergency Operating Procedures (EOP), or contractual SLA delivery reports, cite these authoritative titles directly:

1. **Electrical Safety and Installation**:
 - **NFPA 70E (2024 Edition)**: *Standard for Electrical Safety in the Workplace*. Governs energized electrical work permits, arc-flash risk assessments, approach boundaries, and PPE categories.
 - **NFPA 70 (2023 Edition)**: *National Electrical Code (NEC)*. Governs overcurrent protection, grounding, bonding, and critical operations power systems (COPS, Article 708).
 - **IEEE Standard 1584-2018**: *IEEE Guide for Performing Arc-Flash Hazard Calculations*. Governs incident energy calculations and boundary modeling.
 - **OSHA 29 CFR 1910.147**: *The Control of Hazardous Energy (Lockout/Tagout)*. Federal statutory requirements for zero-energy isolation verification.

2. **Thermal and Environmental Guidelines**:
 - **ASHRAE TC 9.9 (Fifth Edition, 2021)**: *Thermal Guidelines for Data Processing Environments*. Establishes recommended and allowable environmental envelopes for air-cooled equipment (Classes A1–A4) and liquid-cooled hardware (Classes W1–W5 / W27–W45).
 - **ASHRAE Standard 90.4-2022**: *Energy Standard for Data Centers*. Establishes mechanical and electrical energy efficiency performance minimums (Mechanical Load Component and Electrical Loss Component).

3. **Facility Operational Reliability and Sustainability**:
 - **Uptime Institute Tier Standard**: *Operational Sustainability (2020 Edition)*. Defines operational behaviors, maintenance management, staffing levels, and risk mitigation across Tier I through Tier IV topologies.
 - **TIA-942-B (2017 / Addendum 2020)**: *Telecommunications Infrastructure Standard for Data Centers*. Governs architectural, electrical, mechanical, and physical security redundancy levels (Rated 1 to Rated 4).

4. **Service Management and Business Continuity**:
 - **ISO/IEC 20000-1:2018**: *Information technology — Service management — Part 1: Service management system requirements*. Governs formal change management, incident handling, and service delivery.
 - **ISO 22301:2019**: *Security and resilience — Business continuity management systems — Requirements*. Framework for operational disaster recovery and incident escalation.
 - **ISO 55001:2014**: *Asset management — Management systems — Requirements*. Systematic lifecycle governance of critical physical infrastructure assets.

5. **Operational Guidelines (OpenViking Repository)**:
 - **ALZJ-YW-2.6XZ02**: *IT Whitespace Physical Shift Inspection Operational Guidelines*. Governs multi-sensory inspection rounds, PDU thermal scans, containment differential pressure verification, and quick-disconnect leak audits.
 - **ALZJ-YW-2.6XZ10**: *Liquid Cooling Infrastructure & CDU Operational Guidelines*. Governs primary/secondary loop hydraulic pressures (0.15–0.90 MPa), pump differential pressure limits (< 1.0 bar), plate heat exchanger approach criteria (< 8.0 K), propylene glycol refractometer testing (25.0% wt), and reverse osmosis makeup water chemistry.

## The Copyright Line

This book teaches an operational philosophy and provides an immutable Day Sheet for managing production data center shifts. It is not an official digest, authorized summary, or translation of any third-party course, commercial product manual, or proprietary standard.

All trademarks, service marks, certification titles, and standard identifiers mentioned in this book are the intellectual property of their respective owners:
- *CDFOM*, *CDCS*, and *EPI* are trademarks or registered trademarks of Enterprise Privacy Institute / Enterprise PRATA Pte Ltd.
- *ITIL* is a registered trademark of AXELOS Limited.
- *Uptime Institute* and *Tier Standard* are registered trademarks of Uptime Institute, LLC.
- *ASHRAE* is a registered trademark of the American Society of Heating, Refrigerating and Air-Conditioning Engineers, Inc.
- *NFPA* is a registered trademark of the National Fire Protection Association.
- *Danfoss* and *FD83* are trademarks of Danfoss A/S.
- *NVIDIA*, *NVLink*, and *NVL72* are trademarks of NVIDIA Corporation.

The mention of these titles is strictly for nominative reference, citation, and educational compliance purposes under fair use doctrine. Nothing herein implies endorsement, sponsorship, affiliation, or certification by any of the aforementioned entities.

## Decisions to Record

- The exact editions and publication dates of all standards cited in site procedures.
- Confirmation that no copyrighted standard text or client confidential data was pasted into shift logs.
- The active licensing and training plan for site operations staff.

## Cross-Reference Matrix of Critical Facility Operations Standards

Every rule enforced on the Master Day Sheet maps directly to an auditable international engineering, electrical safety, or operational standard:

| Standard / Code | Issuing Body | Governing Operational Domain in Volume 05 | Mandatory Shift Application |
| :--- | :--- | :--- | :--- |
| **NFPA 70E** | National Fire Protection Association | Electrical Safety in the Workplace, Arc-Flash Boundaries, PPE categories, LOTO | Governs energized switching exclusions and Live-Dead-Live proofs |
| **OSHA 29 CFR 1910.147** | U.S. Dept. of Labor (OSHA) | The Control of Hazardous Energy (Lockout/Tagout) | Governs one-person-one-lock LOTO hardware and group lockboxes |
| **ASHRAE TC 9.9** | ASHRAE | Thermal Guidelines for Data Processing Environments (Air A1–A4, Liquid W1–W5) | Governs whitespace intake and CDU supply temperature corridors |
| **IEEE Std 493 (Gold Book) & 3006** | IEEE | Design and Operational Reliability of Industrial and Commercial Power Systems | Governs 2N redundancy loading ceilings and maintenance bypass risk |
| **ISO/IEC 22237 (EN 50600-3-1)** | ISO / CEN-CENELEC | Data Centre Facilities and Infrastructures — Operational Management Information | Governs SOP/MOP/EOP documentation hierarchy and shift handovers |

## Annual Operational Audit and Standard Revision Control

At the start of every calendar year, the Chief Engineer and Operations Manager review the site's SOP, MOP, and EOP library against the latest published editions of NFPA 70E, ASHRAE TC 9.9, and IEEE 3006. Every procedure cover sheet carries an explicit **Last Reviewed Date** and **Next Mandatory Review Date ($\le 12\,\text{months}$)**; any MOP whose review date has lapsed is automatically locked in the document management system until re-walked on the physical floor.
