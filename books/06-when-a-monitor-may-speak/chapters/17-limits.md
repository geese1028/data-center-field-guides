# 17. What This Book Does Not Own

A field guide that pretends to own the entire domain of software development, industrial automation, and corporate legal governance is an operational hazard.

Operational excellence requires establishing rigid, uncompromising boundaries around what this book owns and what belongs to external engineering and legal authorities.

## It Does Not Own a Software Product or Brand

This book does not endorse, review, or digest any commercial Building Management System (BMS), Supervisory Control and Data Acquisition (SCADA) platform, Data Center Infrastructure Management (DCIM) software suite, or telemetry database engine:
- It does not retell the user manuals of Schneider Wonderware, Siemens Desigo, Johnson Controls Metasys, Honeywell Forge, or open-source platforms like Prometheus or Grafana.
- It does not provide code snippets for configuring commercial time-series databases or tuning SQL query indexes.

The principles in this book are vendor-agnostic physical, mathematical, and procedural laws. If a software vendor claims their proprietary artificial intelligence platform renders deadbands, dwell filters, quality bitmasks, or human promotion gates obsolete, that vendor is selling snake oil. The laws of operational telemetry apply equally to a multimillion-dollar enterprise suite and a command-line script running on an edge microcontroller.

## It Does Not Own Statutory Safety Codes and Building Standards

This book cites statutory engineering standards by title, edition, and year. It deliberately does not transcribe their copyrighted text:
- **NFPA 70E (Standard for Electrical Safety in the Workplace)** governs your arc-flash approach boundaries, energized work permits, and electrical PPE categories.
- **NFPA 72 (National Fire Alarm and Signaling Code)** governs the physical installation, wiring survivability, and annunciation of smoke detectors and emergency horns.
- **OSHA 29 CFR 1910.147** establishes federal statutory requirements for zero-energy Lockout/Tagout (LOTO) verification.
- **ASHRAE TC 9.9** establishes environmental envelopes for data processing environments. ASHRAE has explicitly stated that its technical publication content is protected under international copyright law and may not be digested, ingested, or transformed into AI derivative works without formal written authorization.

Purchase official, licensed copies of these standards from their respective publishers (ANSI, NFPA, ASHRAE, ISO). Keep them in the site engineering library. Never copy and paste standard clauses into your shift logs and claim them as your site's private creation.

## It Does Not Own the Customer's Application Telemetry

This book does not own:
- Your customer's distributed application software, database query latencies, microservice trace identifiers, or network packet routing topologies.
- Your customer's server operating system logs, CPU utilization metrics, or GPU memory allocation performance.

The boundary between facility infrastructure and customer IT hardware is absolute:
- The facility owns the electrical voltage, frequency, and current delivered to the input receptacles of the server rack power distribution units (ePDUs).
- The facility owns the volumetric flow rate, static pressure, and supply temperature of the secondary coolant delivered to the rack manifold supply coupling.
- The customer owns everything that occurs inside the server chassis beyond the power supply and cold plate interface.

Never attempt to diagnose a customer's software database deadlock from a facility electrical meter, and never permit a customer's software engineer to dictate mechanical chiller staging setpoints. Respect the physical interface boundary.

## Decisions to Record

- The official, licensed copies of statutory engineering standards maintained in the site library.
- The physical demarcation boundary between facility infrastructure and customer IT hardware.
- The operational protocol confirming that telemetry rules remain binding regardless of software vendor brand.

## Separation Between Advisory Telemetry and Safety-Instrumented Hardware Interlocks

The most critical architectural boundary in this volume is the **Hardware Safety Separation Rule (IEC 61508 / IEC 61511)**: a software monitoring dashboard, cloud historian, or machine-learning optimization engine is **never** a Safety Instrumented System (SIS).

| Protection Function | Permitted Software BMS/SCADA Role | Mandatory Hardwired Safety Interlock (SIL-2/SIL-3) |
| :--- | :--- | :--- |
| **Load Bank / Heater Over-Temperature** | Trend logging & pre-alarm warning at $48.0^\circ\text{C}$ | Mechanical bimetallic thermostat + hardwired contactor shunt trip ($\le 20\,\text{ms}$) |
| **Generator / Transformer Internal Fault** | SOE timestamp capture & COMTRADE waveform download | Hardwired 86 Lockout Relay & 87 Differential Relay direct to breaker trip coil |
| **Cooling Tower Basin Low Level** | Refill valve command & operator warning banner | Hardwired float switch wired in series with condenser pump starter coil |
| **Room Clean-Agent Pre-Discharge** | HVAC smoke damper status display | Hardwired UL-864 Fire Alarm Control Panel (FACP) abort & release circuit |
