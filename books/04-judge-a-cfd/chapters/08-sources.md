# 8. Public sources, and the copyright line

This field guide teaches an operational audit methodology for field benchmarking and evaluating computational fluid dynamics reports. It does not digest, transcribe, or duplicate proprietary engineering standards, commercial solver code, or confidential data center architectural drawings.

An engineering standard that can be purchased from an issuing standards body is not a document that may be reproduced in an external manual. Citing a standard by title, year, and specific equation to establish a legal audit threshold is standard professional practice; reproducing extensive passages from those standards within an AI-generated text is improper.

```
+----------------------------------------------------------------------------------------------------+
| NORMATIVE INDUSTRY STANDARDS CITED |
+----------------------+-----------------------------------------------------------------------------+
| ASME V&V 20 | "Standard for Verification and Validation in Computational Fluid Dynamics |
| | and Heat Transfer". Foundational principles for numerical discretization |
| | error (GCI) and validation comparison error metrics. |
+----------------------+-----------------------------------------------------------------------------+
| ASHRAE GUIDELINE 14 | "Measurement of Energy, Demand, and Water Savings". Establishes statistical |
| | calibration criteria: Mean Bias Error (NMBE) and Root Mean Square Error. |
+----------------------+-----------------------------------------------------------------------------+
| ASHRAE TC 9.9 | "Thermal Guidelines for Data Processing Environments" (5th Edition, 2021). |
| | Defines environmental classes (Class A1-A4), Recommended & Allowable bands. |
+----------------------+-----------------------------------------------------------------------------+
| GB 50174 | "Code for Design of Data Centers" (Chinese National Standard). Normative |
| | guidelines for data center airflow organization and numerical simulation. |
+----------------------+-----------------------------------------------------------------------------+
| SHARMA & HERRICK | "Dimensionless Parameters for Evaluation of Thermal Performance in Large- |
| (ASME 2002) | Scale Data Centers". Mathematical formulation of SHI and RHI indices. |
+----------------------+-----------------------------------------------------------------------------+
| HERRLIN (ASHRAE 2005)| "Rack Cooling Index (RCI): A Novel Metric for Evaluating Data Center |
| | Cooling Performance". Mathematical formulation of RCI_HI and RCI_LO. |
+----------------------+-----------------------------------------------------------------------------+
```

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

## Decisions to record before test start

- The complete list of governing codes, guidelines, and technical papers cited in the CFD audit report, with publication dates.
- The specific edition of ASHRAE TC 9.9 cited in the project specifications.
- Formal confirmation that client-confidential architectural CAD models and vendor proprietary internal fan tables are preserved within local project files.
