# 18. Titles, Standards, and the Copyright Line

A mission-critical operations team cites its sources with exact academic, engineering, and legal rigor. We operate strictly to published, peer-reviewed engineering standards, statutory safety codes, and binding commercial service agreements.

## Authoritative Engineering Standards & Codes

When authoring Methods of Procedure (MOP), SCADA point configuration specifications, or forensic Sequence of Events (SOE) incident reports, cite these authoritative titles directly:

1. **Data Center Monitoring and Automation Standards**:
 - **GB/T 51409-2020**: *Technical Standard for Integrated Monitoring System of Data Centers (数据中心综合监控系统工程技术标准)*. National standard governing operational telemetry parameters, switchgear statuses, voltage/current monitoring, chiller operating envelopes, and emergency alarm classification.
 - **ANSI/BICSI 002-2024**: *Data Center Design and Implementation Best Practices*. Establishes operational monitoring recommendations for mechanical, electrical, and plumbing (MEP) infrastructure.
 - **TIA-942-B (2017 / Addendum 2020)**: *Telecommunications Infrastructure Standard for Data Centers*. Defines infrastructure tier topologies and physical monitoring reliability requirements.

2. **Industrial Communication Protocols & Time Synchronization**:
 - **IEEE Standard 1588-2019 (PTPv2.1)**: *IEEE Standard for a Precision Clock Synchronization Protocol for Networked Measurement and Control Systems*. Governs sub-microsecond hardware timestamping for electrical Sequence of Events (SOE) recorders and protective relays.
 - **IEC 61850**: *Communication networks and systems for power utility automation*. International standard for substation electrical protection telemetry, GOOSE messaging, and digital fault recording (DFR).
 - **ANSI/ASHRAE Standard 135-2020**: *BACnet — A Data Communication Protocol for Building Automation and Control Networks (ISO 16484-5)*. Governs object identifiers, Change-of-Value (COV) reporting, and building management system telemetry.
 - **Modbus Application Protocol Specification v1.1b3**: *Modbus Organization (2012)*. Defines protocol structure, register addressing conventions, and exception response handling for serial RTU and TCP/IP industrial networks.
 - **RFC 5905**: *Network Time Protocol Version 4: Protocol and Algorithms Specification (IETF, 2010)*. Governs Stratum-1 clock synchronization across distributed server architectures.

3. **Facility Operational Reliability and Sustainability**:
 - **Uptime Institute Tier Standard**: *Operational Sustainability (2020 Edition)*. Defines operational behaviors, alarm management discipline, maintenance governance, and risk mitigation across critical facilities.
 - **ASHRAE TC 9.9 (Fifth Edition, 2021)**: *Thermal Guidelines for Data Processing Environments*. Establishes recommended and allowable environmental envelopes for air-cooled hardware (Classes A1–A4) and liquid-cooled hardware (Classes W1–W5 / W27–W45).
 - **ASTM D3306-21**: *Standard Specification for Glycol Base Engine Coolant for Heavy Duty Applications*. Governs chemical purity, freeze protection, specific gravity, and corrosion inhibitor chemistry for propylene glycol heat transfer loops.

4. **Incident Governance & Operational Guidelines (OpenViking Repository)**:
 - **DCFG-INCIDENT-SOP-01**: *Hyperscale Data Center Incident Management System*. Establishes incident severity tiers (P1/P2/P3), escalation clocks, and the 15-minute SLA notification protocol.
 - **DCFG-SEVERITY-CAT-01**: *Data Center Incident Severity & Impact Classification Directory*. Categorizes equipment failures by contractual customer impact.
 - **DCFG-SOP-WHITESPACE-01**: *IT Whitespace Physical Shift Inspection Operational Guidelines*. Governs multi-sensory shift rounds, containment differential pressure verification, and PDU thermal imaging.
 - **DCFG-SOP-LIQUID-01**: *Liquid Cooling Infrastructure & CDU Operational Guidelines*. Governs primary/secondary loop hydraulic pressures (0.15–0.90 MPa), pump differential pressure limits (< 1.0 bar), plate heat exchanger approach criteria (< 8.0 K), propylene glycol refractometer testing (25.0% wt), and reverse osmosis water chemistry.

## The Copyright Line

This book teaches an operational telemetry methodology and provides a Master Point Sheet for governing data center monitoring consoles. It is not an official digest, authorized summary, or translation of any third-party course, commercial product manual, or proprietary standard.

All trademarks, service marks, standard identifiers, and brand names mentioned in this book are the intellectual property of their respective owners:
- *BACnet* is a registered trademark of the American Society of Heating, Refrigerating and Air-Conditioning Engineers (ASHRAE).
- *Modbus* is a registered trademark of Schneider Electric USA, Inc., licensed to the Modbus Organization, Inc.
- *IEEE* is a registered trademark of the Institute of Electrical and Electronics Engineers, Inc.
- *Uptime Institute* is a registered trademark of Uptime Institute, LLC.
- *Danfoss* and *FD83* are trademarks of Danfoss A/S.
- *NVIDIA*, *NVLink*, and *NVL72* are trademarks of NVIDIA Corporation.

The mention of these titles and technologies is strictly for nominative reference, technical citation, and educational compliance purposes under fair use doctrine. Nothing herein implies endorsement, sponsorship, affiliation, or certification by any of the aforementioned entities.

## Decisions to Record

- The exact editions and publication dates of all standards cited in site monitoring specifications.
- Confirmation that no copyrighted standard text, proprietary register maps, or client confidential data was pasted into shift logs.
- The active calibration and verification schedule for all site telemetry instruments.

## Quantitative Cross-Reference Matrix of Telemetry, Alarm, and Time Standards

| Governing Standard | Issuing Organization | Technical Scope in Volume 06 | Mandatory Audit Application |
| :--- | :--- | :--- | :--- |
| **ANSI/ISA-18.2 (IEC 62682)** | ISA / IEC | Management of Alarm Systems for the Process Industries | Governs alarm rationalization, dwell/deadband tuning, and flood rate limits ($\le 1\text{--}2 / 10\,\text{min}$) |
| **EEMUA Publication 191** | EEMUA | Alarm Systems: A Guide to Design, Management and Procurement | Governs operator cognitive load limits, priority distribution (80% Low, 15% Med, 5% High), and alarm shelving |
| **IEEE Std 1588v2 (PTP) & C37.238** | IEEE | Precision Clock Synchronization Protocol for Networked Measurement and Control Systems | Governs sub-millisecond ($\pm 1\,\text{ms}$) Sequence of Events (SOE) timestamp accuracy |
| **IEC 62541 (OPC-UA Part 4 & 8)** | IEC | OPC Unified Architecture Data Access and StatusCode Quality Bitmasks | Governs `Good (0x00)`, `Uncertain (0x40)`, and `Bad (0x80)` data quality propagation |
| **NAMUR NE 43** | NAMUR | Standardization of the Signal Level for Failure Information of Digital Transmitters | Governs 4–20 mA analog fault current thresholds ($\le 3.6\,\text{mA}$ downscale, $\ge 21.0\,\text{mA}$ upscale) |
| **ASHRAE Guideline 14** | ASHRAE | Measurement of Energy, Demand, and Water Savings (CV-RMSE & NMBE) | Governs cooling-tower and chiller plant baseline regression model validation |
