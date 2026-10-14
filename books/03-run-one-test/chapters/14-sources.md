# 14. Public sources, and the copyright line

This field guide articulates an operational methodology for executing and auditing liquid cooling verification tests. It does not digest, transcribe, or duplicate proprietary industry codes, standards, vendor confidential engineering designs, or copyrighted contract templates.

An engineering standard that can be purchased from an issuing standards body is not a document that may be reproduced in an external text. Citing a standard by title, year, and specific section number to establish a legal testing tolerance is standard engineering practice; reproducing extensive passages from those standards within an AI-generated manual is improper.

```
+----------------------------------------------------------------------------------------------------+
| NORMATIVE INDUSTRY STANDARDS CITED |
+----------------------+-----------------------------------------------------------------------------+
| ASHRAE GUIDELINE 0 | "The Commissioning Process" (2019 Edition). Foundational principles for |
| | commissioning scope, Owner's Project Requirements (OPR), and BOD auditing. |
+----------------------+-----------------------------------------------------------------------------+
| ASHRAE GUIDELINE 1.1 | "HVAC&R Technical Requirements for The Commissioning Process" (2007/2014). |
| | Methodologies for pre-functional checklists and functional performance. |
+----------------------+-----------------------------------------------------------------------------+
| ACG GUIDELINE | AABC Commissioning Group "Commissioning Guideline for Building Systems". |
| | Independent third-party verification protocols and witness standards. |
+----------------------+-----------------------------------------------------------------------------+
| BSRIA BG 29/2020 | "Pre-Commission Cleaning of Pipework Systems" (6th Edition). Strict criteria|
| | for scouring velocities, chemical flushing, and solid particulate counts. |
+----------------------+-----------------------------------------------------------------------------+
| NFPA 70 / IEC 60364 | National Electrical Code (NEC) and International Electrotechnical |
| | Commission standards for branch circuit protection, grounding, and LOTO. |
+----------------------+-----------------------------------------------------------------------------+
| ISA-5.1 | "Instrumentation Symbols and Identification". Standard P&ID symbology for |
| | process flow diagrams, transmitters (TT, PT, FT), and control valves (TCV). |
+----------------------+-----------------------------------------------------------------------------+
```

## Application of Normative Standards

The twelve engineering products articulated in Chapter 2 represent the structural sequence required by modern commissioning governance. They derive from standard industry methodologies (including ASHRAE Guideline 0 and ACG publications) adapted specifically for mission-critical liquid cooling verification.

The completion certificate hierarchy (Levels 0 through 6) reflects the recognized standard across global data center engineering:
- Level 0: Design & Planning
- Level 1: Factory Acceptance Testing
- Level 2: Component Delivery & Receipt QA
- Level 3: Pre-Functional Checks & Start-Up
- Level 4: Functional Performance Testing
- Level 5: Integrated System Testing
- Level 6: Close-Out & Operations Handover

The local "three-stage" terminology frequently used by contractors on the floor is a regional field shorthand. It does not supersede global commissioning certificate tiers. When adopting either framework, the Commissioning Plan must explicitly define on page one which legal signatures the resulting documentation is authorized to support.

## Electrical and Mechanical Code Compliance

Electrical safety checks—including the 100 MΩ insulation resistance threshold and the 0.1 Ω ground continuity limit—derive from NFPA 70 (NEC Article 250 and Article 645 for Information Technology Equipment) and international standard IEC 60204-1 (Safety of Machinery - Electrical Equipment of Machines). A field test script must never attempt to transcribe extensive electrical code articles into its procedure; it cites the governing article number, and the local Electrical Inspector Having Jurisdiction (AHJ) enforces the binding adoption.

Secondary fluid preparation, hydrostatic pressure holding, and system deaeration follow the principles of BSRIA BG 29/2020 and ASME B31.3 (Process Piping). The scouring flush velocity (≥ 1.5 m/s) and the hydrostatic hold requirement (1.5× MAOP for 2 hours with zero decay) are established mechanical engineering standards for hydronic piping.

## Non-Proprietary Reference Baseline

To provide concrete, meaningful numerical yardsticks without disclosing proprietary manufacturer IP or client-confidential data, this book utilizes a non-proprietary reference architecture:
- **Compute Footprint**: Standard 120 kW virtual compute rack simulating high-density accelerated architectures (such as an NVL72-class rack footprint).
- **Cooling Unit**: 1.2 MW in-row or centralized Coolant Distribution Unit (CDU) utilizing dual N+1 canned centrifugal pumps and a titanium plate heat exchanger.
- **Cooling Chemistry**: 25% Propylene Glycol (PG25) with corrosion inhibitors, operating between 40.0°C supply and 50.0°C return.

Specific manufacturer submittals, proprietary PLC control algorithms, client-confidential network schemas, and proprietary quick-disconnect dimensions belong in the project's secure archives under signed Non-Disclosure Agreements (NDAs). They must never be published in open reference guides.

## Decisions to record before test start

- The complete list of governing codes, standards, and guidelines cited in the Commissioning Plan, with publication years.
- The contractual document number supporting each tolerance value.
- Re-affirmation that proprietary vendor IP and confidential site drawings are preserved within local project files.
