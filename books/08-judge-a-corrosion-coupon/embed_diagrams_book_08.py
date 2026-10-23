#!/usr/bin/env python3
"""
Embed flagship diagrams and enrich Book 08: Judge a Corrosion Coupon
Author: Tristan (Data Center Field Guides)
"""

from pathlib import Path

ROOT = Path("/Users/geese/Downloads/book/books/08-judge-a-corrosion-coupon")
CHAP = ROOT / "chapters"
SHEET = ROOT / "sheets"

def add_fig_if_missing(filepath, fig_md, anchor_text):
    text = filepath.read_text(encoding="utf-8")
    if fig_md not in text:
        if anchor_text in text:
            text = text.replace(anchor_text, f"{anchor_text}\n\n{fig_md}\n")
        else:
            text = text + f"\n\n{fig_md}\n"
        filepath.write_text(text, encoding="utf-8")
        print(f"Embedded in {filepath.name}")

# 1. 00-how-to-use.md & 02-coupon.md
fig01_md = "![Dual Copper & Silver Corrosion Coupon Anatomy](../figures/fig-01-isa-coupon-anatomy-and-reactivity-rate.png)"
p00 = CHAP / "00-how-to-use.md"
t00 = p00.read_text(encoding="utf-8")
if fig01_md not in t00:
    t00 = t00.replace("## What you may copy", f"```\n+-----------------------------------------------------------------------------+\n|                   ATMOSPHERIC CORROSION GATING PIPELINE                     |\n|                                                                             |\n|  [OUTDOOR SMOG] ---> [CHEMICAL SCRUBBERS] ---> [DATA HALL WHITESPACE]       |\n|  H2S, SO2, NOx, Cl2   Carbon & Permanganate     Positive Pressure: +20 Pa   |\n|                       Breakthrough <= 5%        Class G1: Cu < 300Å, Ag<200Å|\n+-----------------------------------------------------------------------------+\n```\n\n{fig01_md}\n\n## What you may copy")
    p00.write_text(t00, encoding="utf-8")
    print("Updated 00-how-to-use.md")

add_fig_if_missing(CHAP / "02-coupon.md", fig01_md, "## Two metals, not an average")

# 2. 01-what.md & 13-report.md
fig02_md = "![ISA-71.04-2013 Environmental Severity Classification Matrix](../figures/fig-02-isa-71-04-severity-classification-matrix.png)"
add_fig_if_missing(CHAP / "01-what.md", fig02_md, "## What a result is allowed to mean")
add_fig_if_missing(CHAP / "13-report.md", fig02_md, "## What has to be on it")

# 3. 03-place.md & 22-drawing.md
fig03_md = "![Data Center Coupon Spatial Placement Architecture](../figures/fig-03-data-hall-coupon-placement-topology.png)"
add_fig_if_missing(CHAP / "03-place.md", fig03_md, "## Places you do not hang")
add_fig_if_missing(CHAP / "22-drawing.md", fig03_md, "## What the drawing must show")

# 4. 14-media.md & 15-spent.md
fig04_md = "![Chemical Filtration Media & Gas Breakthrough Dynamics](../figures/fig-04-chemical-filtration-media-and-breakthrough.png)"
add_fig_if_missing(CHAP / "14-media.md", fig04_md, "## The questions that gate acceptance")
add_fig_if_missing(CHAP / "15-spent.md", fig04_md, "## Color is not the measurement")

# 5. 05-seal.md & 06-makeup.md
fig05_md = "![Makeup Air Positive Pressurization & Envelope Sealing](../figures/fig-05-makeup-air-pressurization-and-leak-paths.png)"
add_fig_if_missing(CHAP / "05-seal.md", fig05_md, "## Leaks you cannot buy a machine to fix")
add_fig_if_missing(CHAP / "06-makeup.md", fig05_md, "## Pressure is the first filter")

# 6. 07-live.md & 21-again.md
fig06_md = "![Passive Reactivity Coupons vs. Real-Time QCM Telemetry](../figures/fig-06-passive-coupons-vs-realtime-qcm-monitors.png)"
add_fig_if_missing(CHAP / "07-live.md", fig06_md, "## A live box is not the strip")
add_fig_if_missing(CHAP / "21-again.md", fig06_md, "## When to hang again")

# 7. 08-refuse.md, 09-sheet.md, and sheets/coupon.md
fig07_md = "![The Master Atmospheric Corrosion Coupon Ledger & Refusal Sheet](../figures/fig-07-master-corrosion-coupon-sheet-and-refusal.png)"
add_fig_if_missing(CHAP / "08-refuse.md", fig07_md, "## Before and after is not a class")
add_fig_if_missing(CHAP / "09-sheet.md", fig07_md, "## The coupon")
add_fig_if_missing(SHEET / "coupon.md", fig07_md, "## The coupon")

# Update 11-sources.md with complete standards
p11 = CHAP / "11-sources.md"
content_11 = """# 11. Titles, Standards, and the Copyright Line

This book teaches an operational coupon sheet. It does not digest an environmental engineering standard, a chemical media manufacturer's brochure, or a laboratory test procedure.

The method is the one used when airborne corrosive gases—not dust and not liquid pipe water—attack circuit board metallurgy: hang dual copper and silver strips where the boards ingest air, keep the exposure clock visible, refuse to let copper stand in for silver, seal uncontrolled building envelope penetrations before purchasing purification machinery, maintain positive room pressurization (+15 Pa to +25 Pa), and demand certified coulometric reduction lab reports before signing a Class G1 warranty certificate.

## Authoritative Environmental & Chemical Standards

When drafting coupon monitoring specifications, chemical scrubber submittals, or environmental refusal sheets, cite these authoritative standards directly:

1. **Environmental Gaseous Contamination Standards**:
   - **ANSI/ISA-71.04-2013**: *Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*. The foundational standard defining environmental severity levels (Class G1 Mild, G2 Moderate, G3 Harsh, GX Severe) based on copper and silver reactivity rates in Angstroms per 30 days.
   - **ASHRAE TC 9.9 (Fifth Edition, 2021)**: *Thermal Guidelines for Data Processing Environments*. Establishes gaseous contamination limits for mission-critical IT facilities, mandating Class G1 compliance to prevent creep corrosion on lead-free immersion silver circuit boards.
   - **ISO 14644-8:2022**: *Cleanrooms and associated controlled environments — Part 8: Assessment of air cleanliness by chemical concentration (ACC)*. Framework for airborne molecular contamination (AMC) monitoring.

2. **Laboratory Test Methods & Metallurgy Standards**:
   - **ASTM B825-19**: *Standard Test Method for Coulometric Reduction of Surface Films on Metallic Test Samples*. The authoritative laboratory method for determining Angstrom thickness of copper and silver sulfide and chloride corrosion films.
   - **ASTM B810-01a (Reapproved 2017)**: *Standard Test Method for Calibration of Atmospheric Corrosion Test Chambers by Change in Mass of Copper Coupons*.
   - **ASTM B826-09 (Reapproved 2015)**: *Standard Test Method for Monitoring Atmospheric Corrosion with Quartz Crystal Microbalances (QCM)*. Governs real-time micro-mass acoustic telemetry.

3. **Chemical Filtration Media Testing Standards**:
   - **ASTM D2854-09 (Reapproved 2019)**: *Standard Test Method for Apparent Density of Activated Carbon*. Core test for determining media saturation and remaining chemical life.
   - **ASTM D3838-05 (Reapproved 2017)**: *Standard Test Method for pH of Activated Carbon*.
   - **ASTM D3467-04 (Reapproved 2020)**: *Standard Test Method for Carbon Tetrachloride (CTC) Activity of Activated Carbon*. Governs micropore volume and gas adsorption capacity.

4. **Data Center Facility Guidelines (OpenViking Repository)**:
   - `DCFG-SOP-WHITESPACE-01`: *IT Whitespace Physical Shift Inspection Operational Guidelines*. Governs positive pressure auditing and odor detection.
   - `DCFG-SOP-LIQUID-01`: *Liquid Cooling Infrastructure & CDU Operational Guidelines*. Governs secondary loop water chemistry, glycol testing, and chemical biocide control.

## The Copyright Line

This book teaches an operational monitoring philosophy and provides a Master Corrosion Coupon Sheet for governing data center environmental air quality. It is not an official digest, authorized summary, or translation of any third-party course, commercial media catalog, or proprietary standard.

All trademarks, service marks, standard identifiers, and brand names mentioned in this book are the intellectual property of their respective owners:
- *ISA* is a registered trademark of the International Society of Automation.
- *ASHRAE* is a registered trademark of the American Society of Heating, Refrigerating and Air-Conditioning Engineers, Inc.
- *ASTM* is a registered trademark of ASTM International.
- *Dell*, *HPE*, *Cisco*, and *NVIDIA* are trademarks or registered trademarks of their respective corporations.

The mention of these titles and technologies is strictly for nominative reference, technical citation, and educational compliance purposes under fair use doctrine. Nothing herein implies endorsement, sponsorship, affiliation, or certification by any of the aforementioned entities.

## Decisions to Record

- The exact titles, editions, and publication dates of all standards cited in the coupon monitoring report.
- Confirmation that no proprietary media formulations or client confidential site data were pasted into public logs.
- The active calibration registry for all handheld differential pressure manometers and QCM real-time monitors.
"""
p11.write_text(content_11.strip() + "\n", encoding="utf-8")
print("Updated 11-sources.md")

# Rebuild combined manuscript.md
manuscript = ROOT / "manuscript.md"
manuscript_parts = []
for fn in sorted(CHAP.glob("*.md")):
    manuscript_parts.append(fn.read_text(encoding="utf-8").strip())
manuscript.write_text("\n\n---\n\n".join(manuscript_parts) + "\n", encoding="utf-8")
print(f"Written combined manuscript: {manuscript} ({len(manuscript.read_text().split())} words)")
