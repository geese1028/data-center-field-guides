#!/usr/bin/env python3
"""
Generate Flagship Engineering Diagrams for Book 09: Walk a TDD
Author: Tristan (Data Center Field Guides)
Focus: Technical Due Diligence (TDD), Site Selection, Utility Substation Diversity,
Natural Hazards & Hydrology, Onsite Fuel/Water Autonomy, CPTED Physical Security,
Structural Floor Loading for NVL72 Racks, and Financing Opinion Governance.
Resolution: 1800 x 1100, publication-grade vector styling.
Palette: Deep midnight navy / gold / emerald / rose / cyan / purple.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = Path("/Users/geese/Downloads/book/books/09-walk-a-tdd/figures")
FONT_DIR = Path("/Users/geese/Downloads/book/books/01-liquid-load-bank/fonts")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Theme Palette (Institutional Due Diligence & Technical Audit)
BG = (10, 15, 29)          # Deep midnight navy
PANEL = (23, 37, 60)       # Dark corporate slate
GRID = (38, 55, 85)        # Structural grid
TEXT = (248, 250, 252)     # Crisp white
MUTED = (148, 163, 184)    # Slate grey
GOLD = (245, 158, 11)      # Financing / Amber caution / Deal underwriting
NAVY = (30, 58, 138)       # Institutional lender blue
RED = (239, 68, 68)        # Fatal Flaw / Rejection / Showstopper
GREEN = (16, 185, 129)     # Pass / Clean title / Condition verified
CYAN = (6, 182, 212)       # Utility grid / Telemetry / Engineering path
PURPLE = (147, 51, 234)    # Structural / Civil / Seismic
BORDER = (59, 130, 246)    # Blue border accent


def get_font(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    path = FONT_DIR / name
    if not path.exists():
        path = Path("/Library/Fonts/Arial Unicode.ttf")
    return ImageFont.truetype(str(path), size)


def new_canvas(w=1800, h=1100):
    im = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(im)
    for x in range(0, w, 50):
        d.line((x, 0, x, h), fill=GRID, width=1)
    for y in range(0, h, 40):
        d.line((0, y, w, y), fill=GRID, width=1)
    d.rectangle((20, 20, w - 21, h - 21), outline=BORDER, width=2)
    return im, d


def draw_header(d, num, title, subtitle):
    d.rectangle((40, 35, 1760, 115), fill=PANEL, outline=BORDER, width=2)
    d.text((60, 48), f"FIGURE 09.{num} :: {title.upper()}", font=get_font(24, True), fill=GOLD)
    d.text((60, 82), subtitle, font=get_font(16), fill=MUTED)
    d.text((1440, 58), "BOOK 09 // AUDIT TDD", font=get_font(16, True), fill=CYAN)


def wrap_text(d, text, font, max_width):
    words = text.split(" ")
    lines = []
    cur = []
    for w in words:
        test = " ".join(cur + [w])
        if d.textlength(test, font=font) <= max_width:
            cur.append(w)
        else:
            if cur:
                lines.append(" ".join(cur))
                cur = [w]
            else:
                lines.append(w)
                cur = []
    if cur:
        lines.append(" ".join(cur))
    return lines


# -------------------------------------------------------------
# FIGURE 1: TDD Framework & Fatal Flaw Gating
# -------------------------------------------------------------
def fig_01():
    im, d = new_canvas()
    draw_header(d, 1, "TDD AUDIT FRAMEWORK & FATAL FLAW GATING",
                "The 4-Stage Independent Review: Desk Audit, Physical Walk, Red-Flag Interim, and CP/CS Covenant Closing")

    # 4 Sequential Stages across horizontal banner
    stages = [
        ("STAGE 1: DESK REVIEW", "Virtual Data Room (VDR)",
         ["• Utility Interconnection SLA", "• Single-Line Diagrams (SLD)", "• Environmental Phase I ESA", "• Building Permits & Title Deeds"],
         CYAN, 50),
        ("STAGE 2: PHYSICAL WALK", "On-Site Asset Verification",
         ["• Count: Reconcile vs Asset List", "• Identity Sample: N_s = sqrt(N)+1", "• Operational Running Check", "• Witness / Document Separation"],
         GOLD, 480),
        ("STAGE 3: RED-FLAG REPORT", "48-Hour Interim Findings",
         ["• Fatal Flaws (Deal Breakers)", "• Material CAPEX Catch-Up", "• Single Points of Failure (SPOF)", "• Capacity & Utility Discrepancies"],
         RED, 910),
        ("STAGE 4: OPINION & COVENANTS", "Financing / M&A Closing",
         ["• Conditions Precedent (CP)", "• Conditions Subsequent (CS)", "• Escrow Holdback (150-200%)", "• Strictly Disclaim Projections"],
         GREEN, 1340),
    ]

    for title, sub, bullets, color, x in stages:
        d.rectangle((x, 140, x + 410, 480), fill=PANEL, outline=color, width=2)
        d.rectangle((x, 140, x + 410, 195), fill=color)
        d.text((x + 15, 150), title, font=get_font(18, True), fill=(10, 15, 29))
        d.text((x + 15, 172), sub, font=get_font(13, True), fill=(15, 23, 42))

        y = 215
        for b in bullets:
            d.text((x + 15, y), b, font=get_font(14), fill=TEXT)
            y += 40

    # Arrows between stages
    for ax in [465, 895, 1325]:
        d.polygon([(ax - 10, 310), (ax + 10, 310), (ax, 325)], fill=GOLD)
        d.line([(ax - 15, 310), (ax + 10, 310)], fill=GOLD, width=4)

    # Lower Section: 3-Tier Risk Hierarchy & Fatal Flaw Gating
    d.rectangle((50, 510, 1750, 1050), fill=PANEL, outline=BORDER, width=2)
    d.rectangle((50, 510, 1750, 560), fill=(15, 23, 42))
    d.text((70, 523), "THE THREE-TIER TECHNICAL RISK TAXONOMY & DEAL IMPACT HIERARCHY", font=get_font(19, True), fill=GOLD)

    tiers = [
        ("TIER 1: FATAL FLAW (RED FLAG)", RED,
         "Immediate Deal-Breaker / Syndication Stop",
         ["1. Utility grid connection missing firm reservation or capacity clawback clause active.",
          "2. Property located inside 100-yr / 500-yr flood plain without certified civil levee protection.",
          "3. Building lacks final Certificate of Occupancy or unpermitted structural alterations.",
          "4. High-voltage utility easement crosses whitespace or unresolvable right-of-way encumbrance.",
          "5. Chilled water or fuel storage has no physical path for 72-hour autonomous emergency run."],
         70),
        ("TIER 2: MATERIAL DEFICIENCY (AMBER FLAG)", GOLD,
         "Condition Precedent (CP) / Escrow Holdback",
         ["1. Standby generator fuel polishing system absent; fuel stagnant > 180 days (ASTM D975).",
          "2. Floor live load capacity (10-12 kN/m2) inadequate for planned NVL72 AI racks (20-25 kN/m2).",
          "3. Single point of failure in cooling makeup water header; N+1 chillers share common valve.",
          "4. Incomplete commissioning records (Level 4 integrated systems test not witnessed/certified).",
          "5. Fire suppression pipe routes directly above electrical switchgear without drip trays."],
         630),
        ("TIER 3: OPERATIONAL DEFECT (GREEN FLAG)", GREEN,
         "Condition Subsequent (CS) / 90-Day Post-Close Cure",
         ["1. As-built CAD drawings lack field redline reconciliation; asset tags missing on 5% valves.",
          "2. Maintenance SLA contracts nearing expiration; spare parts inventory below minimum 30-day stock.",
          "3. Minor architectural sealant cracks on perimeter loading dock; no water infiltration visible.",
          "4. Thermographic IR scan reveals 3 loose terminal lugs in secondary sub-distribution boards.",
          "5. Operations shift logbooks kept in paper format; telemetry BMS historian lacks 1-year archive."],
         1190),
    ]

    for title, col, action, items, tx in tiers:
        d.rectangle((tx, 580, tx + 530, 1025), fill=(15, 23, 42), outline=col, width=2)
        d.rectangle((tx, 580, tx + 530, 625), fill=col)
        d.text((tx + 12, 590), title, font=get_font(15, True), fill=(10, 15, 29))
        d.text((tx + 12, 638), action, font=get_font(14, True), fill=col)
        d.line([(tx + 10, 660), (tx + 520, 660)], fill=GRID, width=1)

        iy = 672
        for it in items:
            wrapped = wrap_text(d, it, get_font(12), 490)
            for wline in wrapped:
                d.text((tx + 16, iy), wline, font=get_font(12), fill=TEXT)
                iy += 19
            iy += 21

    im.save(OUT_DIR / "fig-01-tdd-audit-framework-and-red-flags.png", quality=95)
    print("Rendered Figure 09.1")


# -------------------------------------------------------------
# FIGURE 2: Utility Substation Diversity & Single-Line Reality
# -------------------------------------------------------------
def fig_02():
    im, d = new_canvas()
    draw_header(d, 2, "UTILITY SUBSTATION DIVERSITY & GRID DUAL-FEED REALITY",
                "True Physical Grid Diversity vs. Single-Bus Illusion: Transmission Nodes, Dual Feeds, and Common Points of Failure")

    # Left: The Illusion of Dual Feed (Marketing Claim)
    d.rectangle((50, 140, 880, 680), fill=PANEL, outline=RED, width=2)
    d.rectangle((50, 140, 880, 190), fill=RED)
    d.text((70, 152), "THE ILLUSION: PSEUDO-DIVERSE 'DUAL FEED' (MARKETING CLAIM)", font=get_font(17, True), fill=(10, 15, 29))

    # Diagram of Fake Diversity
    d.rectangle((200, 215, 730, 275), fill=(15, 23, 42), outline=MUTED, width=1)
    d.text((220, 230), "UTILITY TRANSMISSION SUBSTATION (SINGLE 220kV BUS)", font=get_font(15, True), fill=CYAN)
    d.text((220, 252), "Common Breaker / Shared Bus Section :: Single Point of Failure", font=get_font(13), fill=MUTED)

    # Two lines coming from same box
    d.line([(350, 275), (350, 360)], fill=RED, width=3)
    d.line([(580, 275), (580, 360)], fill=RED, width=3)
    d.text((260, 310), "Feeder A (10kV)", font=get_font(12), fill=RED)
    d.text((600, 310), "Feeder B (10kV)", font=get_font(12), fill=RED)

    # Shared common duct bank (THE FATAL TRAP)
    d.rectangle((220, 360, 710, 440), fill=(40, 20, 20), outline=RED, width=2)
    d.text((240, 375), "SHARED UNDERGROUND TRENCH / MANHOLE", font=get_font(14, True), fill=RED)
    d.text((240, 400), "Cables run in adjacent ducts; single backhoe cut destroys both feeds!", font=get_font(12), fill=TEXT)

    # Converge into building
    d.line([(465, 440), (465, 500)], fill=RED, width=3)
    d.rectangle((200, 500, 730, 570), fill=(15, 23, 42), outline=RED, width=1)
    d.text((220, 515), "CAMPUS MEDIUM-VOLTAGE SUBSTATION", font=get_font(15, True), fill=TEXT)
    d.text((220, 538), "RESULT: Total Campus Blackout during utility bus fault or trench dig", font=get_font(13, True), fill=RED)

    # Critique box
    d.rectangle((70, 590, 860, 665), fill=(15, 23, 42), outline=RED, width=1)
    d.text((85, 602), "CRITICAL TDD FINDING: Zero independent grid reliability.", font=get_font(14, True), fill=RED)
    d.text((85, 625), "Two account numbers on two bills does NOT prove physical separation. Require full utility GIS route map.", font=get_font(12), fill=TEXT)

    # Right: True Physical Grid Diversity
    d.rectangle((920, 140, 1750, 680), fill=PANEL, outline=GREEN, width=2)
    d.rectangle((920, 140, 1750, 190), fill=GREEN)
    d.text((940, 152), "THE REALITY: TRUE PHYSICAL TRANSMISSION DIVERSITY (TIER III / IV)", font=get_font(17, True), fill=(10, 15, 29))

    # Two separate substations
    d.rectangle((950, 215, 1310, 275), fill=(15, 23, 42), outline=GREEN, width=1)
    d.text((965, 230), "SUBSTATION 'NORTH' (220kV)", font=get_font(15, True), fill=GREEN)
    d.text((965, 252), "Grid Source Alpha // Ind. Transformer", font=get_font(12), fill=MUTED)

    d.rectangle((1360, 215, 1720, 275), fill=(15, 23, 42), outline=GREEN, width=1)
    d.text((1375, 230), "SUBSTATION 'SOUTH' (110kV)", font=get_font(15, True), fill=GREEN)
    d.text((1375, 252), "Grid Source Beta // Separate Substation", font=get_font(12), fill=MUTED)

    # Diverse geographical paths
    d.line([(1130, 275), (1105, 420)], fill=GREEN, width=3)
    d.line([(1540, 275), (1565, 420)], fill=GREEN, width=3)
    d.text((960, 335), "Route A: North Highway\nDirect buried duct bank", font=get_font(12), fill=CYAN)
    d.text((1310, 335), "Route B: East Rail Corridor\n> 2.5 km Physical Separation", font=get_font(12), fill=CYAN)

    # Independent building entries
    d.rectangle((950, 420, 1260, 480), fill=(15, 23, 42), outline=GREEN, width=1)
    d.text((965, 435), "NORTH ELECTRICAL VAULT", font=get_font(13, True), fill=TEXT)
    d.text((965, 455), "Independent Switchgear A", font=get_font(12), fill=MUTED)

    d.rectangle((1410, 420, 1720, 480), fill=(15, 23, 42), outline=GREEN, width=1)
    d.text((1425, 435), "SOUTH ELECTRICAL VAULT", font=get_font(13, True), fill=TEXT)
    d.text((1425, 455), "Independent Switchgear B", font=get_font(12), fill=MUTED)

    # 2N / 2(N+1) Distribution
    d.line([(1105, 480), (1200, 530)], fill=GREEN, width=3)
    d.line([(1565, 480), (1470, 530)], fill=GREEN, width=3)
    d.rectangle((1100, 530, 1570, 580), fill=(15, 23, 42), outline=GOLD, width=1)
    d.text((1120, 545), "BUS-TIE BREAKER WITH MECHANICAL / KIRK-KEY INTERLOCK", font=get_font(13, True), fill=GOLD)

    # Approval note
    d.rectangle((940, 600, 1730, 665), fill=(15, 23, 42), outline=GREEN, width=1)
    d.text((955, 612), "TDD EVIDENCE REQUIRED: Utility GIS routing survey, independent substation names,", font=get_font(13, True), fill=GREEN)
    d.text((955, 635), "dual property entry vaults (>20m apart), and certified breaker transfer schemes.", font=get_font(12), fill=TEXT)

    # Bottom Banner: Due Diligence Power Audit Checklist
    d.rectangle((50, 710, 1750, 1050), fill=PANEL, outline=BORDER, width=2)
    d.rectangle((50, 710, 1750, 760), fill=(15, 23, 42))
    d.text((70, 725), "TECHNICAL DUE DILIGENCE AUDIT CHECKLIST: ELECTRICAL INFRASTRUCTURE", font=get_font(18, True), fill=GOLD)

    chk = [
        ("1. CAPACITY ALLOCATION", "Verify utility firm capacity allocation letter vs contract IT demand. Is capacity reserved or subject to curtailment?", CYAN),
        ("2. N-1 CONTINGENCY", "Can either utility feed carry 100% of maximum facility peak load plus battery charging demand continuously?", GREEN),
        ("3. TRANSFER TOPOLOGY", "Is the ATS open-transition (break-before-make 2-10s) or closed-transition? Does UPS ride through seamlessly?", GOLD),
        ("4. ARC FLASH & FAULT", "Inspect fault current calculations (I_sc >= 40kA or 65kA). Are arc-flash warning labels dated within 3 years?", RED),
        ("5. METER ACCURACY", "Reconcile utility revenue meters against facility BMS meters. Check power factor penalties (PF >= 0.95 required).", TEXT),
    ]

    cy = 780
    for title, desc, col in chk:
        d.text((80, cy), title, font=get_font(15, True), fill=col)
        d.text((360, cy), desc, font=get_font(14), fill=TEXT)
        d.line([(70, cy + 38), (1730, cy + 38)], fill=GRID, width=1)
        cy += 50

    im.save(OUT_DIR / "fig-02-utility-substation-and-grid-diversity.png", quality=95)
    print("Rendered Figure 09.2")


# -------------------------------------------------------------
# FIGURE 3: Natural Hazard Hydrology & Seismic Envelopes
# -------------------------------------------------------------
def fig_03():
    im, d = new_canvas()
    draw_header(d, 3, "NATURAL HAZARD HYDROLOGY, 500-YR FLOOD & SEISMIC DESIGN",
                "FEMA / GB 50174 Base Flood Elevations, Stormwater Detention, Hydrostatic Uplift, and Seismic Lateral Restraints")

    # Left Panel: Hydrology & Flood Plain Elevation Profile
    d.rectangle((50, 140, 980, 1050), fill=PANEL, outline=CYAN, width=2)
    d.rectangle((50, 140, 980, 195), fill=CYAN)
    d.text((70, 155), "CIVIL HYDROLOGY & FLOOD PLAIN ELEVATION BENCHMARKS", font=get_font(18, True), fill=(10, 15, 29))

    # Cross section drawing
    # Elevations
    d.text((70, 220), "Elevation Relative to Mean Sea Level (MSL)", font=get_font(14, True), fill=GOLD)

    # Levels
    levels = [
        ("+14.50 m", "CRITICAL IT WHITESPACE FINISHED FLOOR LEVEL (FFL)", GREEN, 260,
         "Mandatory: >= 1.0 m above 500-year Base Flood Elevation (BFE)"),
        ("+13.20 m", "GENERATOR & SUBSTATION EQUIPMENT PLINTH LEVEL", CYAN, 370,
         "Heavy plant elevated on reinforced concrete piers above high water"),
        ("+12.00 m", "500-YEAR BASE FLOOD ELEVATION (0.2% ANNUAL CHANCE BFE)", RED, 480,
         "Strict international standard for Tier III/IV mission-critical facilities"),
        ("+10.80 m", "100-YEAR BASE FLOOD ELEVATION (1.0% ANNUAL CHANCE BFE)", GOLD, 590,
         "FEMA Zone A/AE minimum; completely unacceptable benchmark for data centers"),
        ("+9.50 m", "SURROUNDING EXTERNAL GRADE & ROAD LEVEL", MUTED, 700,
         "Site perimeter road; subject to sheet runoff and pooling during flash storms"),
        ("+6.00 m", "HISTORICAL HIGH WATER TABLE (HYDROSTATIC PRESSURE)", PURPLE, 810,
         "Sub-grade uplift force: Requires dual membrane waterproofing & sump pumps"),
    ]

    for elev, label, col, y, note in levels:
        d.line([(180, y + 15), (950, y + 15)], fill=col, width=2)
        d.rectangle((70, y, 170, y + 30), fill=col)
        d.text((75, y + 6), elev, font=get_font(13, True), fill=(10, 15, 29))
        d.text((190, y), label, font=get_font(14, True), fill=col)
        d.text((190, y + 22), note, font=get_font(12), fill=TEXT)

    # Stormwater formula box
    d.rectangle((70, 890, 960, 1020), fill=(15, 23, 42), outline=CYAN, width=1)
    d.text((90, 905), "STORMWATER RETENTION BASIN SIZING FORMULA (RATIONAL METHOD)", font=get_font(14, True), fill=CYAN)
    d.text((90, 935), "Q = C * I * A", font=get_font(18, True), fill=GOLD)
    d.text((250, 935), ":: Q = Peak Runoff (m3/s) | C = Runoff Coeff (0.90 for roofs/paved)", font=get_font(13), fill=TEXT)
    d.text((90, 970), "Mandatory 100-year 24-hour storm retention on-site without city storm sewer reliance.", font=get_font(12), fill=MUTED)
    d.text((90, 992), "TDD Verification: Check retention pond volume, weir elevation, and backup diesel sump pumps.", font=get_font(12), fill=GREEN)

    # Right Panel: Seismic & Environmental Buffer Zones
    d.rectangle((1010, 140, 1750, 1050), fill=PANEL, outline=PURPLE, width=2)
    d.rectangle((1010, 140, 1750, 195), fill=PURPLE)
    d.text((1030, 155), "SEISMIC DESIGN & CRITICAL PERIMETER HAZARD BUFFERS", font=get_font(18, True), fill=(10, 15, 29))

    # Seismic standards
    d.text((1030, 220), "SEISMIC RESTRAINT DESIGN CRITERIA (IBC / GB 50011)", font=get_font(16, True), fill=GOLD)

    seismic_items = [
        ("Seismic Design Category (SDC)", "SDC D, E, or F require full non-structural component bracing.", CYAN),
        ("Peak Ground Acceleration (PGA)", "Verify site geotechnical survey: PGA >= 0.25g requires seismic snubbers.", TEXT),
        ("Component Importance Factor", "Ip = 1.5 (Life safety / Mission critical operation following earthquake).", GREEN),
        ("Equipment Snubbers", "Transformers, chillers, generators, and UPS racks anchored to slab.", TEXT),
        ("Raised Floor Pedestals", "Diagonal seismic strut bracing tied directly to reinforced structural slab.", GOLD),
    ]

    sy = 260
    for title, desc, col in seismic_items:
        d.text((1040, sy), f"• {title}:", font=get_font(14, True), fill=col)
        d.text((1040, sy + 22), f"  {desc}", font=get_font(13), fill=TEXT)
        sy += 55

    d.line([(1030, sy + 10), (1730, sy + 10)], fill=GRID, width=1)

    # Environmental buffers
    d.text((1030, sy + 30), "PERIMETER HAZARD EXCLUSION BUFFERS", font=get_font(16, True), fill=GOLD)

    buffers = [
        ("AIRPORT FLIGHT PATHS", "Minimum 8.0 km from commercial airport runway centerline. Check FAA Part 77 airspace obstruction surfaces and vibration contours.", RED),
        ("HAZMAT / CHEMICAL SITES", "Minimum 1.5 km buffer from chemical refineries, fertilizer plants, and toxic gas storage. Verify ambient H2S/SO2 levels.", GOLD),
        ("RAILROAD & HIGHWAY", "Minimum 150 m buffer from freight rail corridors (vibration transmission and hazardous cargo derailment shockwaves).", TEXT),
        ("HIGH-VOLTAGE LINES", "No high-voltage transmission lines (>110kV) crossing directly over site whitespace footprint (EMF interference & cable collapse).", PURPLE),
    ]

    by = sy + 70
    for btitle, bdesc, bcol in buffers:
        d.rectangle((1030, by, 1730, by + 90), fill=(15, 23, 42), outline=bcol, width=1)
        d.text((1045, by + 10), btitle, font=get_font(14, True), fill=bcol)
        b_lines = wrap_text(d, bdesc, get_font(12), 660)
        for idx, bl in enumerate(b_lines):
            d.text((1045, by + 35 + idx * 18), bl, font=get_font(12), fill=TEXT)
        by += 105

    im.save(OUT_DIR / "fig-03-natural-hazards-and-flood-plain-hydrology.png", quality=95)
    print("Rendered Figure 09.3")


# -------------------------------------------------------------
# FIGURE 4: Onsite Fuel & Water Autonomy
# -------------------------------------------------------------
def fig_04():
    im, d = new_canvas()
    draw_header(d, 4, "ON-SITE FUEL AND WATER EMERGENCY AUTONOMY ENVELOPES",
                "72-Hour Full-Load Diesel Storage, Duplex Fuel Polishing, and Thermal Buffer Storage Sizing")

    # Left: Emergency Diesel Storage & Delivery Path
    d.rectangle((50, 140, 880, 1050), fill=PANEL, outline=GOLD, width=2)
    d.rectangle((50, 140, 880, 195), fill=GOLD)
    d.text((70, 155), "72-HOUR DIESEL AUTONOMY & FUEL POLISHING ARCHITECTURE", font=get_font(17, True), fill=(10, 15, 29))

    # Fuel Calculation Box
    d.rectangle((70, 215, 860, 360), fill=(15, 23, 42), outline=GOLD, width=1)
    d.text((90, 230), "DIESEL STORAGE CAPACITY SIZING FORMULA", font=get_font(15, True), fill=GOLD)
    d.text((90, 260), "V_total = N_gen * m_fuel * t_run * 1.15", font=get_font(17, True), fill=CYAN)
    d.text((90, 295), "Example: 10 x 2.5 MW Gensets @ 540 L/hr fuel burn rate for 72 hours:", font=get_font(13), fill=TEXT)
    d.text((90, 320), "V_total = 10 * 540 * 72 * 1.15 = 447,120 Liters (~448 m3 storage)", font=get_font(14, True), fill=GREEN)

    # Physical Fuel Path Diagram
    d.rectangle((70, 380, 860, 780), fill=(15, 23, 42), outline=MUTED, width=1)
    d.text((90, 395), "BULK UNDERGROUND STORAGE TANKS (UST) - DUAL WALL FIBERGLASS", font=get_font(13, True), fill=CYAN)
    d.text((90, 418), "Equipped with continuous interstitial leak sensors and automatic tank gauge (ATG)", font=get_font(11), fill=MUTED)

    # Duplex polishing loop
    d.rectangle((100, 455, 830, 565), fill=(20, 30, 50), outline=CYAN, width=1)
    d.text((120, 470), "AUTOMATED DUPLEX FUEL POLISHING SYSTEM (24/7 OPERATION)", font=get_font(14, True), fill=CYAN)
    d.text((120, 500), "• Water Separator: Strips emulsified water (< 50 ppm per ASTM D2709)", font=get_font(12), fill=TEXT)
    d.text((120, 520), "• 2-Micron Particulate Filter: Removes sediment, rust & microbial sludge", font=get_font(12), fill=TEXT)
    d.text((120, 540), "• Turnover Cycle: 100% of fuel volume polished every 30 to 45 days", font=get_font(12), fill=GREEN)

    # Day tanks inside generator rooms
    d.rectangle((100, 585, 830, 685), fill=(20, 30, 50), outline=GOLD, width=1)
    d.text((120, 600), "GENERATOR DAY TANKS (AST) - 4 TO 8 HOUR RUNTIME CAPACITY", font=get_font(14, True), fill=GOLD)
    d.text((120, 625), "• Gravity / Duplex pump fill lines with automatic high-level shutoff valves", font=get_font(12), fill=TEXT)
    d.text((120, 645), "• Fusible-link thermal fire dump valves discharging fuel to bulk tanks", font=get_font(12), fill=RED)
    d.text((120, 665), "• Double-containment spill basin with leak sensors wired directly to BMS", font=get_font(12), fill=TEXT)

    # TDD Warning
    d.rectangle((70, 805, 860, 1025), fill=(35, 15, 15), outline=RED, width=1)
    d.text((90, 820), "CRITICAL TDD RED FLAG: STAGNANT FUEL DEGRADATION", font=get_font(15, True), fill=RED)
    d.text((90, 845), "Unpolished Ultra-Low Sulfur Diesel (ULSD) degrades within 6 to 12 months.", font=get_font(13), fill=TEXT)
    d.text((90, 870), "Bacteria and fungi grow at the water-diesel interface, creating dark asphaltic", font=get_font(13), fill=TEXT)
    d.text((90, 895), "sludge that clogs generator high-pressure common rail (HPCR) injectors in 10 minutes.", font=get_font(13), fill=TEXT)
    d.text((90, 930), "TDD AUDIT ACT: Pull a bottom fuel sample from each tank. If cloudy or black,", font=get_font(14, True), fill=GOLD)
    d.text((90, 955), "issue a Condition Precedent (CP) for full laboratory fuel assay & remediation.", font=get_font(14, True), fill=GOLD)

    # Right: Water Autonomy & Thermal Buffer
    d.rectangle((920, 140, 1750, 1050), fill=PANEL, outline=CYAN, width=2)
    d.rectangle((920, 140, 1750, 195), fill=CYAN)
    d.text((940, 155), "ON-SITE WATER STORAGE & THERMAL CHILLED WATER BUFFER", font=get_font(17, True), fill=(10, 15, 29))

    # Cooling Water Autonomy
    d.rectangle((940, 215, 1730, 480), fill=(15, 23, 42), outline=CYAN, width=1)
    d.text((960, 230), "EVAPORATIVE COOLING TOWER MAKEUP WATER SIZING", font=get_font(15, True), fill=CYAN)
    d.text((960, 260), "Evaporation Rate: ~1.5 to 2.2 L/kWh of thermal heat rejection", font=get_font(13), fill=TEXT)
    d.text((960, 285), "For a 20 MW IT load with wet cooling towers at design wet-bulb:", font=get_font(13), fill=MUTED)
    d.text((960, 310), "Daily Evaporation + Blowdown = 20,000 * 1.8 * 24 = 864,000 Liters / day", font=get_font(14, True), fill=GOLD)
    d.text((960, 345), "48-HOUR ON-SITE BULK WATER STORAGE REQUIREMENT:", font=get_font(14, True), fill=GREEN)
    d.text((960, 370), "Minimum 1,728 m3 raw water storage tanks on-site or dual diverse municipal feeds.", font=get_font(13), fill=TEXT)
    d.text((960, 400), "TDD Check: Is on-site water treated? Check biocide, scaling, and legionella test records.", font=get_font(12), fill=MUTED)

    # Thermal Energy Buffer Storage (TES)
    d.rectangle((940, 510, 1730, 780), fill=(15, 23, 42), outline=PURPLE, width=1)
    d.text((960, 525), "STRATIFIED CHILLED WATER THERMAL BUFFER STORAGE (TES)", font=get_font(15, True), fill=PURPLE)
    d.text((960, 555), "Purpose: Ride through chiller restart time during sudden utility outage.", font=get_font(13), fill=TEXT)
    d.text((960, 580), "Centrifugal chillers take 7 to 12 minutes to re-establish oil pressure and start compressor.", font=get_font(13), fill=MUTED)
    d.text((960, 615), "THERMAL BUFFER SIZING FORMULA:", font=get_font(14, True), fill=GOLD)
    d.text((960, 640), "V_tes = (Q_cooling * t_restart) / (rho * Cp * Delta_T)", font=get_font(16, True), fill=CYAN)
    d.text((960, 675), "Without an active TES tank or inline hydraulic expansion vessels,", font=get_font(13), fill=RED)
    d.text((960, 695), "high-density AI whitespace loop temperature will spike +10 deg C in 90 seconds!", font=get_font(13, True), fill=RED)
    d.text((960, 725), "TDD Check: Verify inline TES volume against total loop thermal inertia.", font=get_font(13), fill=GREEN)

    # Bottom summary box
    d.rectangle((940, 805, 1730, 1025), fill=(15, 23, 42), outline=BORDER, width=1)
    d.text((960, 820), "SUMMARY: THE INDEPENDENT AUTONOMY SCORECARD", font=get_font(15, True), fill=GOLD)
    d.text((960, 850), "• Fuel Autonomy: Minimum 72 hours @ 100% rated design load.", font=get_font(13), fill=TEXT)
    d.text((960, 875), "• Water Autonomy: Minimum 48 hours makeup buffer or closed-loop dry cooler fallback.", font=get_font(13), fill=TEXT)
    d.text((960, 900), "• Ride-Through Buffer: Minimum 15 minutes chilled water continuous circulation.", font=get_font(13), fill=TEXT)
    d.text((960, 935), "An unevidenced tank is just a metal cylinder. Demand calibration charts & live sensor readings.", font=get_font(13, True), fill=CYAN)

    im.save(OUT_DIR / "fig-04-onsite-fuel-and-water-autonomy-envelope.png", quality=95)
    print("Rendered Figure 09.4")


# -------------------------------------------------------------
# FIGURE 5: Physical Security & CPTED Perimeter
# -------------------------------------------------------------
def fig_05():
    im, d = new_canvas()
    draw_header(d, 5, "PHYSICAL SECURITY ZONES, CPTED PERIMETER & ANTI-RAM HARDENING",
                "ASTM F2656 Crash-Rated Barriers, 30m Standoff Distance, Concentric Envelopes, and Meet-Me Room Diversity")

    # Concentric Security Zones Diagram
    d.rectangle((50, 140, 1100, 1050), fill=PANEL, outline=BORDER, width=2)
    d.rectangle((50, 140, 1100, 195), fill=BORDER)
    d.text((70, 155), "CONCENTRIC DEFENSIVE PERIMETER & CPTED ARCHITECTURE", font=get_font(18, True), fill=(10, 15, 29))

    # Rings of defense
    rings = [
        ("ZONE 1: PROPERTY BOUNDARY", RED, 215, 345,
         "ASTM F2656 M50/P1 Anti-Ram Crash Fence & K12 Rated Hydraulic Bollards",
         ["• Stops 6,800 kg truck travelling at 80 km/h with <= 1.0 m penetration.",
          "• Vehicle Sally Port with interlocked drop-arm barrier and under-vehicle optical scanner.",
          "• Perimeter Fiber-Optic Intrusion Detection System (PIDS) mounted on weldmesh fence."]),
        ("ZONE 2: STANDOFF BUFFER (>= 30 METERS)", GOLD, 365, 495,
         "Clear Line-of-Sight Explosion & Attack Buffer Zone",
         ["• Minimum 30-meter clear distance between property line and data center outer wall.",
          "• Thermal-optical pan-tilt-zoom CCTV cameras with 100% boundary overlap; zero blind spots.",
          "• Anti-drone RF detection and directional radar monitoring perimeter airspace."]),
        ("ZONE 3: REINFORCED BUILDING ENVELOPE", CYAN, 515, 645,
         "Hardened Architectural Perimeter & Logistics Screening",
         ["• Blast-resistant pre-cast concrete exterior facade; zero exterior windows to whitespace.",
          "• Security Operations Center (SOC) 24/7/365 manned with bullet-resistant UL 752 Level 4 glass.",
          "• Dedicated loading dock with biometric airlock and X-ray pallet inspection."]),
        ("ZONE 4: IT WHITESPACE AIRLOCK / MANTRAP", PURPLE, 665, 795,
         "Multi-Factor Biometric Access & Anti-Tailgating Interlocks",
         ["• Weight-sensing dual-door mantrap airlocks; only one door open at any instant.",
          "• Dual-factor authentication: Encrypted smartcard + iris / facial biometric verification.",
          "• Zero unauthorized visitor access without continuous security staff escort."]),
        ("ZONE 5: TELECOM MEET-ME ROOMS (MMR-A & MMR-B)", GREEN, 815, 945,
         "Diverse Fiber Entry & Carrier Neutrality Hardening",
         ["• Dual independent MMR rooms separated by >= 50 meters inside facility footprint.",
          "• Diverse carrier duct banks entering from opposite street sides through concrete encased vaults.",
          "• Redundant DC power plants (-48V DC) and dedicated dry-pipe fire suppression."]),
    ]

    for title, col, y1, y2, desc, bullets in rings:
        d.rectangle((70, y1, 1080, y2), fill=(15, 23, 42), outline=col, width=2)
        d.rectangle((70, y1, 1080, y1 + 35), fill=col)
        d.text((85, y1 + 8), title, font=get_font(14, True), fill=(10, 15, 29))
        d.text((85, y1 + 45), desc, font=get_font(13, True), fill=col)

        by = y1 + 70
        for b in bullets:
            d.text((95, by), b, font=get_font(12), fill=TEXT)
            by += 20

    # Standoff summary note
    d.rectangle((70, 965, 1080, 1030), fill=(15, 23, 42), outline=MUTED, width=1)
    d.text((85, 978), "TDD AUDIT RULE: If standoff distance < 30m, demand civil blast vulnerability study.", font=get_font(13, True), fill=GOLD)
    d.text((85, 1002), "Verify crash test certifications for all perimeter gates and bollards from accredited labs.", font=get_font(12), fill=TEXT)

    # Right: Physical Security TDD Audit Verification Table
    d.rectangle((1130, 140, 1750, 1050), fill=PANEL, outline=GOLD, width=2)
    d.rectangle((1130, 140, 1750, 195), fill=GOLD)
    d.text((1150, 155), "SECURITY AUDIT: FIELD VERIFICATION POINTS", font=get_font(18, True), fill=(10, 15, 29))

    checks = [
        ("CCTV ARCHIVE RETENTION", "Are video feeds stored for minimum 90 days at 1080p / 15 fps? Verify random footage recall from 60 days ago.", CYAN),
        ("DOOR FORCED ALARMS", "Test a forced-door event on an emergency exit. Does SOC receive audible alert and pan camera within 3 seconds?", RED),
        ("KEY MANAGEMENT SYSTEM", "Audit electronic key locker. Are physical override keys tracked with tamper-evident seals and digital logs?", GOLD),
        ("PERIMETER LIGHTING", "Check nighttime illumination: Minimum 50 Lux along entire fence line and vehicle checkpoints.", TEXT),
        ("FIBER CONDUIT EASEMENT", "Inspect utility right-of-way documents for fiber entries. Are carrier manholes locked with tamper alarms?", GREEN),
        ("FIRE SPRINKLER CUTOFF", "Ensure pre-action fire sprinkler risers are secured inside locked cages with supervised tamper switches.", PURPLE),
    ]

    cy = 230
    for title, desc, col in checks:
        d.rectangle((1150, cy, 1730, cy + 110), fill=(15, 23, 42), outline=col, width=1)
        d.text((1165, cy + 12), title, font=get_font(14, True), fill=col)
        c_lines = wrap_text(d, desc, get_font(12), 540)
        for idx, cl in enumerate(c_lines):
            d.text((1165, cy + 38 + idx * 18), cl, font=get_font(12), fill=TEXT)
        cy += 130

    im.save(OUT_DIR / "fig-05-physical-security-and-cpted-perimeter.png", quality=95)
    print("Rendered Figure 09.5")


# -------------------------------------------------------------
# FIGURE 6: Structural Floor Loading & NVL72 AI Racks
# -------------------------------------------------------------
def fig_06():
    im, d = new_canvas()
    draw_header(d, 6, "STRUCTURAL FLOOR LOADING, CONCENTRATED LOADS & AI ACCELERATOR WEIGHT",
                "Live Load Allowances (15-25 kN/m2), NVL72 Heavy Liquid Racks, Point Loads, and Rigging Pathways")

    # Left: Loading Spectrum Comparison
    d.rectangle((50, 140, 880, 650), fill=PANEL, outline=PURPLE, width=2)
    d.rectangle((50, 140, 880, 195), fill=PURPLE)
    d.text((70, 155), "FLOOR UNIFORMLY DISTRIBUTED LOAD (UDL) SPECTRUM", font=get_font(18, True), fill=(10, 15, 29))

    densities = [
        ("TRADITIONAL ENTERPRISE RACK", "5.0 - 8.0 kN/m2 (~500 - 800 kg/m2)",
         "Legacy 5-10 kW racks; standard office building conversion", (100, 116, 139), 220),
        ("HYPERSCALE CLOUD STORAGE", "10.0 - 12.0 kN/m2 (~1,000 - 1,200 kg/m2)",
         "Dense 15-20 kW CPU servers; GB 50174 Class B standard", CYAN, 320),
        ("AI ACCELERATOR CLUSTER (NVL72)", "18.0 - 25.0 kN/m2 (~1,800 - 2,500 kg/m2)",
         "130 kW liquid-cooled racks (1,800 kg per rack footprint + coolant)", GOLD, 420),
        ("CENTRAL CHILLER & BATTERY PLANT", "25.0 - 35.0 kN/m2 (~2,500 - 3,500 kg/m2)",
         "VRLA battery banks, centrifugal chillers & medium-voltage transformers", RED, 520),
    ]

    for title, load, desc, col, y in densities:
        d.rectangle((70, y, 860, y + 80), fill=(15, 23, 42), outline=col, width=1)
        d.rectangle((70, y, 200, y + 80), fill=col)
        d.text((80, y + 25), load.split()[0], font=get_font(18, True), fill=(10, 15, 29))
        d.text((220, y + 15), title, font=get_font(15, True), fill=col)
        d.text((220, y + 42), f"{load} :: {desc}", font=get_font(12), fill=TEXT)

    # Right: NVL72 Rack Footprint & Point Load Physics
    d.rectangle((920, 140, 1750, 650), fill=PANEL, outline=GOLD, width=2)
    d.rectangle((920, 140, 1750, 195), fill=GOLD)
    d.text((940, 155), "NVL72 RACK CONCENTRATED POINT LOADS & PEDESTAL STRESS", font=get_font(18, True), fill=(10, 15, 29))

    d.rectangle((940, 220, 1730, 420), fill=(15, 23, 42), outline=GOLD, width=1)
    d.text((960, 235), "CONCENTRATED CASTER LOAD CALCULATION", font=get_font(15, True), fill=GOLD)
    d.text((960, 265), "NVL72 Operating Weight: ~1,800 kg (with manifold, blind-mate hoses & liquid)", font=get_font(13), fill=TEXT)
    d.text((960, 290), "4 Caster Wheels during transit: P_point = 1,800 kg / 4 = 450 kg (~4.41 kN per caster)", font=get_font(14, True), fill=CYAN)
    d.text((960, 325), "RAISED FLOOR PEDESTAL SPECIFICATION:", font=get_font(14, True), fill=GREEN)
    d.text((960, 350), "• Concentrated load rating: >= 15 kN (CISCA / MOB PSA)", font=get_font(13), fill=TEXT)
    d.text((960, 375), "• Rolling load rating: >= 10 kN to avoid panel punching failure during rack roll-in", font=get_font(13), fill=TEXT)

    # Post-tensioned slab warning
    d.rectangle((940, 440, 1730, 620), fill=(35, 15, 15), outline=RED, width=1)
    d.text((960, 455), "POST-TENSIONED SLAB CORING RESTRICTIONS (THE LIQUID RETROFIT TRAP)", font=get_font(14, True), fill=RED)
    d.text((960, 485), "Drilling floor penetrations for CDU liquid cooling headers through post-tensioned slabs", font=get_font(12), fill=TEXT)
    d.text((960, 508), "can sever high-tensile steel tendons, triggering catastrophic building collapse!", font=get_font(12, True), fill=RED)
    d.text((960, 540), "TDD AUDIT ACT: Demand Ground Penetrating Radar (GPR) scan reports and structural", font=get_font(13, True), fill=GOLD)
    d.text((960, 565), "engineer stamped penetration drawings before approving any liquid cooling retrofit.", font=get_font(13, True), fill=GOLD)

    # Bottom: Rigging, Freight Elevator & Logistics Audit Checklist
    d.rectangle((50, 680, 1750, 1050), fill=PANEL, outline=BORDER, width=2)
    d.rectangle((50, 680, 1750, 730), fill=(15, 23, 42))
    d.text((70, 695), "RIGGING PATHWAY & FREIGHT LOGISTICS PHYSICAL AUDIT", font=get_font(18, True), fill=GOLD)

    rigging = [
        ("1. FREIGHT ELEVATOR CAPACITY", "Payload rating >= 3,500 kg (~3.5 metric tons). Cab dimensions minimum 2.4m (W) x 2.4m (H) x 3.0m (D) to clear NVL72 crate.", CYAN),
        ("2. LOADING DOCK RAMP SLOPE", "Maximum slope <= 5% (1:20). Steep ramps cause heavy rack caster lockup or tipping risk (center of gravity H_cog >= 1.1m).", GOLD),
        ("3. CORRIDOR TURNING RADII", "Check all hallway corners and airlock door widths (minimum 1.5m clear double doors). Zero step changes or unramped thresholds.", TEXT),
        ("4. SLAB VIBRATION LIMITS", "Confirm VC-A or VC-B vibration criteria (<= 50 um/s RMS) to prevent hard drive / optical transceiver micro-dislocations.", PURPLE),
        ("5. OVERHEAD CRANE HOIST", "Verify ceiling hook anchor points (WLL >= 2,000 kg) above heavy transformer and liquid CDU service maintenance areas.", GREEN),
    ]

    ry = 750
    for rtitle, rdesc, rcol in rigging:
        d.text((80, ry), rtitle, font=get_font(14, True), fill=rcol)
        d.text((380, ry), rdesc, font=get_font(13), fill=TEXT)
        d.line([(70, ry + 42), (1730, ry + 42)], fill=GRID, width=1)
        ry += 55

    im.save(OUT_DIR / "fig-06-structural-floor-loading-and-expansion-limits.png", quality=95)
    print("Rendered Figure 09.6")


# -------------------------------------------------------------
# FIGURE 7: Master TDD Scorecard & Financing Opinion Ledger
# -------------------------------------------------------------
def fig_07():
    im, d = new_canvas()
    draw_header(d, 7, "MASTER TDD SCORECARD & FINANCING OPINION LEDGER",
                "The 6-Pillar Risk Matrix, Red-Flag Triggers, and Condition Precedent (CP) Escrow Enforcement")

    # Left: The 6-Pillar Assessment Matrix
    d.rectangle((50, 140, 1080, 1050), fill=PANEL, outline=BORDER, width=2)
    d.rectangle((50, 140, 1080, 195), fill=BORDER)
    d.text((70, 155), "THE SIX PILLARS OF DATA CENTER TECHNICAL DUE DILIGENCE", font=get_font(18, True), fill=(10, 15, 29))

    pillars = [
        ("PILLAR 1: CIVIL & SITE", "FEMA 500-yr flood level, seismic SDC, soil subsidence, perimeter blast standoff >= 30m, zoning permits.", GREEN, 220),
        ("PILLAR 2: POWER & GRID", "True dual-feed substation diversity, capacity allocation letter, 72h fuel autonomy, N+1 generator redundancy.", GOLD, 340),
        ("PILLAR 3: COOLING & WATER", "Chiller N+1 capacity, 48h makeup water reserve, stratified thermal buffer tank, closed-loop CDU readiness.", CYAN, 460),
        ("PILLAR 4: STRUCTURAL & LOAD", "Live floor load >= 20 kN/m2 for AI racks, elevator payload >= 3.5t, post-tensioned slab integrity, seismic bracing.", PURPLE),
        ("PILLAR 5: PERMITS & LEGAL", "Building occupancy certificate, environmental Phase I/II clearance, fire department acceptance, grid rights-of-way.", RED),
        ("PILLAR 6: O&M & SPARES", "24/7 technical shift roster, certified MOP/SOP library, critical spares on-site, OEM service level agreements.", GREEN),
    ]

    py = 215
    for ptitle, pdesc, pcol in [
        ("PILLAR 1: CIVIL & SITE", "FEMA 500-yr flood level, seismic SDC, soil subsidence, perimeter blast standoff >= 30m, zoning permits.", GREEN),
        ("PILLAR 2: POWER & GRID", "True dual-feed substation diversity, capacity allocation letter, 72h fuel autonomy, N+1 generator redundancy.", GOLD),
        ("PILLAR 3: COOLING & WATER", "Chiller N+1 capacity, 48h makeup water reserve, stratified thermal buffer tank, closed-loop CDU readiness.", CYAN),
        ("PILLAR 4: STRUCTURAL & LOAD", "Live floor load >= 20 kN/m2 for AI racks, elevator payload >= 3.5t, post-tensioned slab integrity, seismic bracing.", PURPLE),
        ("PILLAR 5: PERMITS & LEGAL", "Building occupancy certificate, environmental Phase I/II clearance, fire department acceptance, grid rights-of-way.", RED),
        ("PILLAR 6: O&M & SPARES", "24/7 technical shift roster, certified MOP/SOP library, critical spares on-site, OEM service level agreements.", GREEN),
    ]:
        d.rectangle((70, py, 1060, py + 105), fill=(15, 23, 42), outline=pcol, width=1)
        d.rectangle((70, py, 280, py + 105), fill=pcol)
        d.text((85, py + 40), ptitle.split(":")[0], font=get_font(15, True), fill=(10, 15, 29))
        d.text((300, py + 15), ptitle, font=get_font(15, True), fill=pcol)
        p_lines = wrap_text(d, pdesc, get_font(12), 740)
        for idx, pl in enumerate(p_lines):
            d.text((300, py + 45 + idx * 18), pl, font=get_font(12), fill=TEXT)
        py += 125

    # Right: Financing Governance Ladder & Refusal Mechanism
    d.rectangle((1120, 140, 1750, 1050), fill=PANEL, outline=GOLD, width=2)
    d.rectangle((1120, 140, 1750, 195), fill=GOLD)
    d.text((1140, 155), "FINANCING GOVERNANCE & OPINION LADDER", font=get_font(18, True), fill=(10, 15, 29))

    # Ladder steps
    steps = [
        ("UNCONDITIONAL PASS (CLEAN OPINION)", GREEN,
         "All 6 pillars verified against primary records. Full dual feeds evidenced. 100% of CP items closed. Debt syndication authorized.", 220),
        ("CONDITIONAL CLOSE (ESCROW HOLD-BACK)", GOLD,
         "Tier 2 deficiencies identified (e.g. fuel polishing retrofit, spare parts restock). Loan closes with 150-200% CAPEX held in escrow until cured.", 400),
        ("MATERIAL ADVERSE FINDING (DEAL RE-TRADE)", (249, 115, 22),
         "Capacity derating required (e.g. cooling plant limited to 15 MW instead of 20 MW). Facility purchase price renegotiated downward.", 580),
        ("FORMAL TECHNICAL REFUSAL (FATAL FLAW)", RED,
         "Uninsurable flood risk, lack of grid reservation, unpermitted whitespace, or refusal of physical site access. Lender's engineer withholds signature.", 760),
    ]

    for stitle, scol, sdesc, sy in steps:
        d.rectangle((1140, sy, 1730, sy + 150), fill=(15, 23, 42), outline=scol, width=2)
        d.rectangle((1140, sy, 1730, sy + 40), fill=scol)
        d.text((1155, sy + 10), stitle, font=get_font(14, True), fill=(10, 15, 29))
        s_lines = wrap_text(d, sdesc, get_font(13), 550)
        for idx, sl in enumerate(s_lines):
            d.text((1155, sy + 55 + idx * 20), sl, font=get_font(13), fill=TEXT)

    # Refusal statement template
    d.rectangle((1140, 940, 1730, 1030), fill=(35, 15, 15), outline=RED, width=1)
    d.text((1155, 952), "THE INDEPENDENT ENGINEER REFUSAL COVENANT:", font=get_font(13, True), fill=RED)
    d.text((1155, 975), "'The Independent Engineer certifies only what was physically witnessed or verified", font=get_font(11), fill=TEXT)
    d.text((1155, 995), "against primary utility/permit records. Spoken redundancy is explicitly disclaimed.'", font=get_font(11), fill=GOLD)

    im.save(OUT_DIR / "fig-07-master-tdd-scorecard-and-refusal-matrix.png", quality=95)
    print("Rendered Figure 09.7")


if __name__ == "__main__":
    print("Generating Flagship Engineering Diagrams for Book 09: Walk a TDD...")
    fig_01()
    fig_02()
    fig_03()
    fig_04()
    fig_05()
    fig_06()
    fig_07()
    print("All 7 diagrams generated successfully in:", OUT_DIR)
