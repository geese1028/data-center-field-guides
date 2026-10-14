# 13. Public sources and citation integrity

A flash report or commissioning document cell may cite an established public standard or published engineering guideline. It may never be replaced by one.

In modern mission-critical engineering, citation discipline protects both technical rigor and legal integrity. Citing an industry standard demonstrates that your verification methodology rests on defensible, peer-reviewed engineering consensus. However, copying copyrighted tables from private vendor handbooks or pasting proprietary customer schematics into a public report invites immediate copyright liability and non-disclosure violations.

This chapter defines the strict rules governing citations, intellectual property boundaries, and acceptable public engineering sources.

## What a citation may do and what it may not

A citation is a pointer to an external authority that supports an engineering method, a safety definition, or an environmental classification. 

### What a Citation May Do:
- **Establish Environmental Classes**: A citation to ASHRAE TC 9.9 may support the sentence: *"The secondary loop coolant supply temperature was audited against the ASHRAE Liquid Cooling Class W4 envelope (32°C to 45°C)."*
- **Define Electrical Ground Rules**: A citation to IEC 60204-1 or NFPA 70 may support the sentence: *"Main circuit disconnects and emergency stop interlocks were verified in compliance with IEC 60204-1, Section 9.2 (Stop Category 0: Uncontrolled stop by immediate removal of power to the machine actuators)."*
- **Anchor Commissioning Process Terminology**: A citation to ASHRAE Guideline 0-2019 may support the five-phase commissioning hierarchy (Level 1 Factory Witness Testing through Level 5 Integrated System Testing).
- **Reference Algorithmic Methods**: Citations to Romano et al. (arXiv:2607.19961) and Fearnhead et al. (DOI:10.1080/10618600.2018.1512868) establish the mathematical peer review of the Focus and CPOP changepoint algorithms.

### What a Citation May NOT Do:
- **A Citation Cannot Fill a Measured Cell**: Citing an NVIDIA GB200 NVL72 marketing white paper does not fulfill the duty to measure live return temperature on the test floor. An observed cell requires an observed reading from a calibrated physical sensor.
- **A Citation Cannot Waive a Missing Line**: You may not write *"Single-feed fault test omitted per industry practice"* and cite a generic commissioning handbook. A handbook cannot waive a contractually mandated test scene.
- **A Citation Must Not Be a Paste**: You may not photocopy or paste proprietary vendor curves, confidential customer floorplans, or copyrighted standard text into your report. Cite the document by formal title, issuing body, revision number, and publication year.

## Authorized public engineering references

The methodology of this field guide aligns with the following public, non-proprietary standards and industry bodies:

1. **ASHRAE Guideline 0-2019**: *The Commissioning Process*. Defines the standardized quality-focused commissioning process for facilities, including Owner’s Project Requirements (OPR), Basis of Design (BOD), and Verification Checklists.
2. **ASHRAE Guideline 1.1-2007**: *HVAC&R Technical Requirements for The Commissioning Process*. Governs functional performance testing protocols for primary and secondary fluid handling loops.
3. **ASHRAE TC 9.9**: *Thermal Guidelines for Data Processing Environments (5th Edition, 2021)*. Defines liquid cooling environmental classifications (Classes W1 through W5) and facility ambient dew point limits for condensation control.
4. **IEC 60204-1 (Edition 6.0, 2016)**: *Safety of Machinery – Electrical Equipment of Machines – Part 1: General Requirements*. Governs electrical isolation, overcurrent protection, emergency stop hardwired loops, and dielectric withstand tests for industrial machines.
5. **NFPA 70 (National Electrical Code, 2023 Edition)**: Article 645 (Information Technology Equipment) and Article 250 (Grounding and Bonding).
6. **Open Compute Project (OCP) Liquid Cooling Guidelines**: Open standards governing secondary fluid loop cleanliness, material compatibility (wetted metallurgy), and quick-disconnect classifications—explicitly distinguishing blade-level blind mates (UQD) from full-flow manifold test couplings (such as Danfoss FD83).
7. **ISA-5.1-2009**: *Instrumentation Symbols and Identification*. Governs the standardized drafting of Piping & Instrumentation Diagrams (P&IDs) for liquid cooling loops.

## Defending against vendor proposal evasion

A common tactic employed by under-prepared equipment suppliers during commissioning meetings is presenting a generic white paper or academic preprint in response to a failed test cell.

If a load-bank cabinet fails its 15-minute dwell due to severe flow starvation, and the vendor submits a published paper showing that "advanced microchannel cold plates can tolerate temporary boiling," reject the submission immediately.
- The white paper is an academic document describing a laboratory experiment under controlled conditions.
- Your test is an acceptance verification of a specific, contracted machine standing in for an NVL72-class production rack.
- The flash report records what the physical machine did on the floor against the cited specification revision. It does not debate academic possibilities.

Hold the boundary. Insist that citations remain bibliography lines, while the cells remain yours.

## Decisions to record

In the compliance and citation section of the flash report, document:

- The formal title, issuing organization, edition, and revision of every external standard cited in the report.
- The certification that no proprietary vendor text, confidential customer data, or copyrighted schematics were pasted into the document.
- The signed statement confirming that all technical limits were evaluated against the frozen project specification revision then in force.
