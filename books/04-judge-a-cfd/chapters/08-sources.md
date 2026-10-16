# 8. Public sources, and the copyright line

This field guide teaches an operational audit methodology for field benchmarking and evaluating computational fluid dynamics reports. It does not digest, transcribe, or duplicate proprietary engineering standards, commercial solver code, or confidential data center architectural drawings.

An engineering standard that can be purchased from an issuing standards body is not a document that may be reproduced in an external manual. Citing a standard by title, year, and specific equation to establish a legal audit threshold is standard professional practice; reproducing extensive passages from those standards within an AI-generated text is improper.

**NORMATIVE INDUSTRY STANDARDS CITED**

| ASME V&V 20 | "Standard for Verification and Validation in Computational Fluid Dynamics and Heat Transfer". Foundational principles for numerical discretization error (GCI) and validation comparison error metrics. |
| :--- | :--- |
| ASHRAE GUIDELINE 14 | "Measurement of Energy, Demand, and Water Savings". Establishes statistical calibration criteria: Mean Bias Error (NMBE) and Root Mean Square Error. |
| ASHRAE TC 9.9 | "Thermal Guidelines for Data Processing Environments" (5th Edition, 2021). Defines environmental classes (Class A1-A4), Recommended & Allowable bands. |
| GB 50174 | "Code for Design of Data Centers" (Chinese National Standard). Normative guidelines for data center airflow organization and numerical simulation. |
| SHARMA & HERRICK (ASME 2002) | "Dimensionless Parameters for Evaluation of Thermal Performance in Large- Scale Data Centers". Mathematical formulation of SHI and RHI indices. |
| HERRLIN (ASHRAE 2005) | "Rack Cooling Index (RCI): A Novel Metric for Evaluating Data Center Cooling Performance". Mathematical formulation of RCI_HI and RCI_LO. |

## Application of Normative Standards

The physical measurement protocols established in Chapter 1—including the 2-point cooling supply average, 3-point return grille average, and 3-tier vertical intake probe tree—derive from standard experimental airflow benchmarking practices adapted specifically for mission-critical data center validation.

Statistical error validation metrics (MAE ≤ 1.0 K, RMSE ≤ 1.5 K, |NMBE| ≤ 5.0%) combine the principles of ASME V&V 20 and ASHRAE Guideline 14. An engineering consultant whose simulation diverges from physical measurements by more than these thresholds has not delivered a validated model; they have delivered an uncalibrated design estimate.

The thermal evaluation criteria articulated in Chapter 4 derive directly from ASHRAE TC 9.9 (5th Edition, 2021). The Class A1 Recommended envelope (18.0°C to 27.0°C, maximum dew point 15.0°C) and Allowable envelope (15.0°C to 32.0°C) represent the global benchmark for enterprise compute hardware. This book cites these temperature and humidity thresholds; it does not reproduce the proprietary psychrometric charts published by ASHRAE.

Dimensionless airflow performance evaluation incorporates the peer-reviewed engineering formulations of Sharma and Herrick (Supply Heat Index and Return Heat Index) and Herrlin (Rack Cooling Index). These metrics provide mathematical objectivity, replacing subjective visual evaluations of color-contour plots with verifiable numerical criteria.

## Non-Proprietary Reference Architecture

To provide concrete, meaningful numerical yardsticks without disclosing proprietary manufacturer IP or client-confidential data, this book utilizes a non-proprietary reference architecture:
- **Hybrid Compute Footprint**: 120 kW virtual compute rack simulating high-density accelerated architectures (such as an NVL72 / GB200 class footprint).
- **Thermal Energy Split**: 80.0% (96.0 kW) direct-to-chip secondary liquid cooling; 20.0% (24.0 kW) convective air release into the whitespace.
- **Airflow Delivery**: Raised-floor plenum (800 mm clear void depth) with downflow EC-fan CRAH units discharging at 5.5 m/s, feeding Cold Aisle Containment (CAC) rows via 40% free-area perforated tiles.

Specific manufacturer CAD geometries, proprietary server internal fan tables, client-confidential network topologies, and proprietary data hall drawings belong in the project's secure archives under signed Non-Disclosure Agreements (NDAs). They must never be published in open reference guides.

## Quantitative Cross-Reference Matrix of Public Thermal and Airflow Standards

When drafting project specifications or auditing a consultant's CFD report on Sheet 1 and Sheet 2, the engineer must cite the exact public standard that governs each physical measurement instrument, environmental envelope, and uncertainty calculation. Never allow a consultant to cite "industry standard CFD practices" without naming the specific document, edition, and measurement class.

| Governing Standard / Guideline | Issuing Organization | Specific Technical Scope in Whitespace & CFD Audits | Mandatory Field / Audit Application |
| :--- | :--- | :--- | :--- |
| **ASHRAE Thermal Guidelines for Data Processing Environments (5th Ed.)** | ASHRAE TC 9.9 | Defines Classes A1–A4 dry-bulb ($18\text{--}27^\circ\text{C}$ rec), dew-point, RH, and liquid classes W1–W5 | Governs maximum allowable intake temperature at $0.3, 1.2, 1.8\,\text{m}$ bezel elevations |
| **ASHRAE Guideline 0 & Guideline 202** | ASHRAE | Defines the Commissioning Process (Levels 1 through 5 IST) | Establishes that a simulation (Level 0/Design) never substitutes for Level 4/5 physical IST |
| **ASME V&V 20 (Standard for Verification and Validation in Computational Fluid Dynamics)** | ASME | Formal mathematical framework for numerical uncertainty ($U_{\text{num}}$), input uncertainty ($U_{\text{input}}$), and validation comparison error ($E$) | Governs Grid Convergence Index ($\text{GCI}$) and physical validation error bounds on Sheet 1 |
| **ISO/IEC 30134-2 & EN 50600-2-3** | ISO / CEN-CENELEC | Environmental control, airflow efficiency, and PUE/RCI whitespace thermal management metrics | Governs $\text{RCI}_{\text{HI}}$, $\text{RCI}_{\text{LO}}$, and containment pressure differential auditing |
| **ANSI/ASHRAE Standard 111** | ASHRAE | Measurement, testing, adjusting, and balancing (TAB) of building HVAC systems | Governs Pitot-tube duct traverses, capture-hood balometer accuracy, and coil face velocity grids |
| **IEC 60751** | IEC | Industrial platinum resistance thermometers and platinum temperature sensors | Governs Class A ($\pm 0.15^\circ\text{C}$) 4-wire Pt100 RTD calibration for vertical intake trees |

### Formal Validation Uncertainty Equation (ASME V&V 20)

Under ASME V&V 20, the comparison error $E$ between a simulation result $S$ and an experimental field measurement $D$ at any rack intake location is evaluated against the combined validation uncertainty $u_{\text{val}}$:

$$E = S - D, \qquad u_{\text{val}} = \sqrt{u_{\text{num}}^2 + u_{\text{input}}^2 + u_D^2}$$

Where $u_{\text{num}}$ is the numerical discretization uncertainty derived from the Grid Convergence Index, $u_{\text{input}}$ is the uncertainty propagated from boundary measurements (PDU power $\pm 0.5\%$, balometer flow $\pm 3.0\%$), and $u_D$ is the sensor calibration uncertainty ($\pm 0.15\,\text{K}$). Only when $|E| \le u_{\text{val}}$ across the benchmark array can the computational model claim physical validation within instrument precision.

## Archival Retention Requirements for Field Benchmark and CFD Model Files

To ensure that a calibrated whitespace model remains usable across the multi-year lifecycle of the data hall—when new high-density liquid/air pods are added in Phase 2 or Phase 3—the closeout binder must archive the raw digital artifacts alongside the PDF report:

| Archive Deliverable | Required File Format | Retention Owner & Location | Operational Purpose |
| :--- | :--- | :--- | :--- |
| **Raw Field Benchmark Dataset** | `.csv` / `.parquet` with ISO 8601 timestamps | Facility Engineering Historian | Proves physical baseline $T_1, T_2, T_3$, balometer CFM, and PDU kW |
| **3D Geometry & Native Solver File** | `.step` / `.iges` + native solver case file | Site Document Control Vault | Allows re-running future rack additions without rebuilding geometry |
| **Signed Sheet 1 & Sheet 2 PDFs** | Searchable PDF/A with wet/digital signatures | Commissioning Closeout Binder | Legal record of calibration pass ($\text{MAE}_T \le 1.5\,\text{K}$) and chosen remedy |

## Summary Verification Checklist for Independent CFD Peer Reviewers

Before signing the peer-review block on any whitespace simulation report:
1. Confirm Sheet 1 physical measurements ($S_1, S_2, R_1, R_2, R_3$ and $T_{0.3}, T_{1.2}, T_{1.8}$) are attached in raw CSV format.
2. Confirm $\text{MAE}_T \le 1.5\,\text{K}$, $\text{RMSE}_T \le 2.0\,\text{K}$, and global energy balance closure $\le 1.0\%$.
3. Confirm $\text{GCI}_{\text{fine}} \le 2.0\%$ across a minimum 2-grid mesh refinement study.
4. Confirm all candidate remedies on Sheet 2 were tested under identical turbulence closures and followed by a post-change physical verification walk.

## Decisions to record before test start

- The complete list of governing codes, guidelines, and technical papers cited in the CFD audit report, with publication dates.
- The specific edition of ASHRAE TC 9.9 cited in the project specifications.
- Formal confirmation that client-confidential architectural CAD models and vendor proprietary internal fan tables are preserved within local project files.
