#!/usr/bin/env python3
"""
Embed flagship diagrams and enrich Book 07: Refuse the Handover
Author: Tristan (Data Center Field Guides)
"""

from pathlib import Path

ROOT = Path("/Users/geese/Downloads/book/books/07-refuse-the-handover")
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

# 1. 00-how-to-use.md
p00 = CHAP / "00-how-to-use.md"
t00 = p00.read_text(encoding="utf-8")
fig01_md = "![The Handover Gatekeeper Architecture](../figures/fig-01-handover-gatekeeper-architecture.png)"
if fig01_md not in t00:
    t00 = t00.replace("## Who this is for", f"```\n+-----------------------------------------------------------------------------+\n|                        THE TURNOVER GATEKEEPER                              |\n|                                                                             |\n|  [CONSTRUCTION & CX] ---> [THE TURNOVER GATE] ---> [COMMERCIAL OPERATIONS]  |\n|                            • Review As-Builts       • Sole LOTO Custody     |\n|                            • Audit Punch Lists      • 99.999% SLA Clock     |\n|                            • Demand 200% Escrow     • 15-Min Client Notice  |\n|                            • SIGN OR REFUSE                                 |\n+-----------------------------------------------------------------------------+\n```\n\n{fig01_md}\n\n## Who this is for")
    p00.write_text(t00, encoding="utf-8")
    print("Updated 00-how-to-use.md")

# 2. 01-signature.md
add_fig_if_missing(CHAP / "01-signature.md", fig01_md, "## What the sentence may say")

# 3. 08-punch.md & 21-minor.md
fig02_md = "![The Punch List Defect Triad Matrix](../figures/fig-02-punchlist-defect-triad-matrix.png)"
add_fig_if_missing(CHAP / "08-punch.md", fig02_md, "## Waivers you will live with")
add_fig_if_missing(CHAP / "21-minor.md", fig02_md, "## What you do not call minor")

# 4. 18-drawings.md & 03-missing.md
fig03_md = "![As-Built vs. Redline Forensic Custody Audit](../figures/fig-03-as-built-redline-custody-audit.png)"
add_fig_if_missing(CHAP / "18-drawings.md", fig03_md, "## What you refuse")
add_fig_if_missing(CHAP / "03-missing.md", fig03_md, "## What is missing from the pack")

# 5. 12-conditional.md
fig04_md = "![The Conditional Acceptance Escrow & Retainage Ladder](../figures/fig-04-conditional-acceptance-escrow-ladder.png)"
add_fig_if_missing(CHAP / "12-conditional.md", fig04_md, "## An end date")

# 6. 10-levels.md & 02-not-the-tester.md
fig05_md = "![Commissioning Levels Gating Pyramid](../figures/fig-05-commissioning-levels-gating-pyramid.png)"
add_fig_if_missing(CHAP / "10-levels.md", fig05_md, "## The levels you were promised")
add_fig_if_missing(CHAP / "02-not-the-tester.md", fig05_md, "## Two hats, not two coats")

# 7. 19-custody.md & 09-operate.md
fig06_md = "![Physical Custody Transfer and Lockout/Tagout Interlocking](../figures/fig-06-custody-transfer-and-loto-handover.png)"
add_fig_if_missing(CHAP / "19-custody.md", fig06_md, "## The key and the door")
add_fig_if_missing(CHAP / "09-operate.md", fig06_md, "## The shift cannot operate a promise")

# 8. 15-sheet.md & sheets/refusal.md
fig07_md = "![The Master Refusal Sheet and Dissent Ledger](../figures/fig-07-master-refusal-sheet-and-dissent-ledger.png)"
add_fig_if_missing(CHAP / "15-sheet.md", fig07_md, "## How to fill it")
add_fig_if_missing(SHEET / "refusal.md", fig07_md, "## Their page")

# Update 17-sources.md with complete standards
p17 = CHAP / "17-sources.md"
content_17 = """# 17. Titles, Standards, and the Copyright Line

This book teaches an operational refusal sheet. It does not digest a commissioning pack, a customer's acceptance procedure, or an engineering standard.

The method is the one used when a turnover pack is on the table and someone demands an unearned wide sentence: match the signature strictly to witnessed physical evidence, keep the tester's hat off the operator's signature, refuse an unjudged flash file, refuse an unmeasured CFD picture, refuse an uncalibrated SCADA screen, refuse an unmeasured nameplate capacity, refuse an open Category 1 punch line, refuse a sales slide offered as staff training, and strike every certificate presented in the wrong slot.

Conditional acceptance is an explicit refusal of everything remaining, bound by a 200% financial escrow retainage and a 30-day cure deadline in the same document, or it is not acceptance.

## Authoritative Commissioning & Acceptance Standards

When authoring handover refusal sheets, commissioning scripts, or punch list dispute letters, cite these authoritative engineering titles directly:

1. **Building Commissioning & Verification Standards**:
   - **ASHRAE Guideline 0-2019**: *The Commissioning Process*. Establishes the foundational requirements for Owner's Project Requirements (OPR), Basis of Design (BOD), and commissioning documentation across all building phases.
   - **ASHRAE Standard 202-2018**: *Commissioning Process for Buildings and Systems*. Defines minimum legal and technical requirements for professional commissioning procedures.
   - **ACG Commissioning Guideline (Second Edition)**: *AABC Commissioning Group*. Standard for certified third-party total building commissioning and independent witness testing.
   - **NEBB Procedural Standards (2019 Edition)**: *Procedural Standards for Building Systems Commissioning*. Standards for mechanical testing, adjusting, and balancing (TAB) and electrical testing.

2. **National & Statutory Infrastructure Acceptance Codes**:
   - **GB 50462-2015**: *Code for Construction and Acceptance of Data Center Infrastructure (数据中心基础设施施工及验收规范)*. National standard governing civil, electrical, HVAC, water supply, lightning protection, and integrated monitoring acceptance testing.
   - **GB 50300-2013**: *Unified Standard for Constructional Quality Acceptance of Building Engineering (建筑工程施工质量验收统一标准)*. Governs acceptance lot partitioning, hidden work inspection records, and statutory handover gating.
   - **GB 50303-2015**: *Code for Acceptance of Construction Quality of Electrical Installation in Building (建筑电气工程施工质量验收规范)*. Governs transformer insulation resistance, circuit breaker trip settings, and earthing grid impedance testing.
   - **GB 50243-2016**: *Code of Acceptance for Construction Quality of Ventilation and Air Conditioning Works (通风与空调工程施工质量验收规范)*. Governs duct leakage testing, pipe pressure testing, and chiller balancing.
   - **GB 50339-2013**: *Code for Acceptance of Quality of Intelligent Building Systems (智能建筑工程质量验收规范)*. Governs BMS/EPMS automated controls and sensor calibration acceptance.

3. **Electrical Safety and Operational Custody Standards**:
   - **NFPA 70E (2024 Edition)**: *Standard for Electrical Safety in the Workplace*. Establishes energized work permits, arc-flash boundary calculations, and personal protective equipment categories.
   - **OSHA 29 CFR 1910.147**: *The Control of Hazardous Energy (Lockout/Tagout)*. Federal statutory mandate for zero-energy physical isolation prior to service turnover.
   - **OpenViking Operational Guidelines**:
     - `DCFG-SOP-WHITESPACE-01`: *IT Whitespace Physical Shift Inspection Operational Guidelines*.
     - `DCFG-SOP-LIQUID-01`: *Liquid Cooling Infrastructure & CDU Operational Guidelines*.

## The Copyright Line

This book teaches an operational philosophy and provides an auditable Master Refusal Sheet for governing facility handovers. It is not an official digest, authorized summary, or translation of any third-party course, commercial product manual, or proprietary standard.

All trademarks, service marks, certification titles, and standard identifiers mentioned in this book are the intellectual property of their respective owners:
- *ASHRAE* is a registered trademark of the American Society of Heating, Refrigerating and Air-Conditioning Engineers, Inc.
- *Uptime Institute* is a registered trademark of Uptime Institute, LLC.
- *NFPA* is a registered trademark of the National Fire Protection Association.
- *NEBB* is a registered trademark of the National Environmental Balancing Bureau.
- *ACG* is a registered trademark of the AABC Commissioning Group.
- *Danfoss* and *FD83* are trademarks of Danfoss A/S.
- *NVIDIA*, *NVLink*, and *NVL72* are trademarks of NVIDIA Corporation.

The mention of these titles is strictly for nominative reference, technical citation, and educational compliance purposes under fair use doctrine. Nothing herein implies endorsement, sponsorship, affiliation, or certification by any of the aforementioned entities.

## Decisions to Record

- The exact titles, editions, and publication dates of all standards cited in the turnover dossier.
- Confirmation that no copyrighted standard text or contractor proprietary methods were pasted into shift turnover sheets.
- The signed statement confirming that commercial milestone payment schedules were excluded from technical acceptance.
"""
p17.write_text(content_17.strip() + "\n", encoding="utf-8")
print("Updated 17-sources.md")

# Rebuild combined manuscript.md
manuscript = ROOT / "manuscript.md"
manuscript_parts = []
for fn in sorted(CHAP.glob("*.md")):
    manuscript_parts.append(fn.read_text(encoding="utf-8").strip())
manuscript.write_text("\n\n---\n\n".join(manuscript_parts) + "\n", encoding="utf-8")
print(f"Written combined manuscript: {manuscript} ({len(manuscript.read_text().split())} words)")
