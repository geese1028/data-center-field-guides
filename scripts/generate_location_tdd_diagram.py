#!/usr/bin/env python3
"""
Generate Flagship Engineering Diagram for:
Data Center Facility Location Due Diligence (Site Selection & Physical Audit)
Author: Tristan (Data Center Field Guides)
Resolution: 1800 x 1100, publication-grade vector styling.
Palette: Deep midnight navy / gold / emerald / rose / cyan / purple.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import shutil

OUT_SITE = Path("/Users/geese/Downloads/book/site/blog/figures/flagship")
OUT_BOOK = Path("/Users/geese/Downloads/book/books/09-walk-a-tdd/figures")
FONT_DIR = Path("/Users/geese/Downloads/book/books/01-liquid-load-bank/fonts")

OUT_SITE.mkdir(parents=True, exist_ok=True)
OUT_BOOK.mkdir(parents=True, exist_ok=True)

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


def draw_header(d, title, subtitle):
    d.rectangle((40, 35, 1760, 115), fill=PANEL, outline=BORDER, width=2)
    d.text((60, 48), title.upper(), font=get_font(24, True), fill=GOLD)
    d.text((60, 82), subtitle, font=get_font(16), fill=MUTED)
    d.text((1400, 58), "SITE SELECTION TDD // FIELD GUIDE", font=get_font(15, True), fill=CYAN)


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


def generate_diagram():
    im, d = new_canvas()
    draw_header(d, "DATA CENTER FACILITY LOCATION DUE DILIGENCE: 6-VECTOR RISK TAXONOMY",
                "The Physical Site Selection Audit: Grid Diversity, 500-Yr Hydrology, Geotechnical Bearing, and Environmental Fitness")

    # 6 Vector Cards arranged in a 3x2 grid
    cards = [
        # Col 1, Row 1
        (50, 140, 540, 370, "1. UTILITY INTERCONNECT & DIVERSITY", CYAN, [
            ("• Substation Proximity:", "≤ 3.0 km dedicated MV feeder routing to transmission node"),
            ("• Substation Diversity:", "Dual feeds from 2 independent transmission busbars (2N)"),
            ("• Civil Duct Bank:", "Opposite property perimeter entries (> 20 m vault distance)"),
            ("• Contractual Gate:", "Firm uncurtailable reservation; check clawback timeline"),
        ]),
        # Col 2, Row 1
        (630, 140, 540, 370, "2. CIVIL HYDROLOGY & 500-YR FLOOD", GOLD, [
            ("• Base Flood Elevation:", "Finished Floor Level (FFL) ≥ +1.0 m to +1.5 m above 500-yr BFE"),
            ("• Retention Basin:", "100-yr, 24-hr storm capacity on site (Rational Method: Q=CIA)"),
            ("• Storm Sewer Reliance:", "Zero reliance on off-site municipal drainage during peak surge"),
            ("• Groundwater Uplift:", "Dual-membrane slab tanking with auto dewatering sumps"),
        ]),
        # Col 3, Row 1
        (1210, 140, 540, 370, "3. GEOTECHNICAL & NVL72 STRUCTURAL", PURPLE, [
            ("• Soil Bearing Capacity:", "q_allowable ≥ 250-350 kPa across all transformer & hall pads"),
            ("• Heavy AI Whitespace:", "Slab rated for 20-25 kN/m² UDL; point caster load ≥ 4.5 kN"),
            ("• Liquefaction Risk:", "Borehole N_SPT ≥ 30; shear wave velocity Vs30 ≥ 360 m/s"),
            ("• Post-Tensioned Slabs:", "Certified GPR scans mandatory before core-drilling for CDU"),
        ]),
        # Col 1, Row 2
        (50, 530, 540, 340, "4. SETBACKS & MICRO-VIBRATION", GREEN, [
            ("• Freight Rail & Highway:", "≥ 150 m setback to avoid VC-A / VC-B vibration intrusion"),
            ("• Vibration Metric:", "Peak Particle Velocity (PPV) < 50 μm/s (protects optical gear)"),
            ("• Flight Path Clearances:", "FAA Part 77 obstacle evaluation; ≥ 8 km radar clearance"),
            ("• Hazardous Proximity:", "≥ 3.0 km radius from chemical plants, pipelines & refineries"),
        ]),
        # Col 2, Row 2
        (630, 530, 540, 340, "5. ATMOSPHERIC & ISA-71.04 CORROSION", CYAN, [
            ("• Airborne Reactivity:", "ISA-71.04 Class G1 compliance: d_Cu < 300 Å, d_Ag < 200 Å/30d"),
            ("• Agricultural Emissions:", "Ammonia & sulfur baseline audits within 5 km agricultural zone"),
            ("• Emergency Makeup Air:", "Deep-bed chemical gas-phase filtration (EBCT ≥ 0.2 s)"),
            ("• Blank Testing:", "Lot-matched Field Travel Blank (FTB ≤ 35 Å) verified by lab"),
        ]),
        # Col 3, Row 2
        (1210, 530, 540, 340, "6. WATER RIGHTS & FUEL AUTONOMY", GOLD, [
            ("• Industrial Water Rights:", "Firm municipal allocation (m³/day) or zero-water dry cooling"),
            ("• Dual-Source Makeup:", "On-site 48-72 hour raw water storage for wet cooling mode"),
            ("• Bulk Diesel Reserve:", "72h continuous full-load generation (ASTM D975 / D2709)"),
            ("• Automated Fuel Loop:", "Duplex filtration polishing every 30-45d (< 50 ppm H2O)"),
        ]),
    ]

    for x, y, w, h, title, color, items in cards:
        d.rectangle((x, y, x + w, y + h), fill=PANEL, outline=color, width=2)
        d.rectangle((x, y, x + w, y + 42), fill=color)
        d.text((x + 16, y + 10), title, font=get_font(16, True), fill=(10, 15, 29))

        item_y = y + 56
        for heading, desc in items:
            d.text((x + 16, item_y), heading, font=get_font(13, True), fill=TEXT)
            desc_lines = wrap_text(d, desc, get_font(12), w - 40)
            cur_y = item_y + 18
            for line in desc_lines:
                d.text((x + 28, cur_y), line, font=get_font(12), fill=MUTED)
                cur_y += 16
            item_y = cur_y + 8

    # Bottom Banner: The Fatal Flaw (Deal Breaker) Refusal Gate
    d.rectangle((50, 890, 1750, 1060), fill=(40, 15, 20), outline=RED, width=2)
    d.rectangle((50, 890, 1750, 930), fill=RED)
    d.text((65, 900), "FATAL FLAW REFUSAL GATE // IMMEDIATE TRANSACTION SHUTDOWN", font=get_font(16, True), fill=TEXT)

    flaws = [
        "1. SINGLE TRANSMISSION BUSBAR: Two 10 kV feeders sharing a single upstream transformer or street trench.",
        "2. UNMITIGATED FLOOD EXPOSURE: Property footprint inside 100-yr or 500-yr flood plain without certified civil levee.",
        "3. CURTAILABLE POWER CONTRACT: Utility reservation subject to discretionary grid curtailment without firm backing.",
        "4. ACTIVE SEISMIC FAULT / LIQUEFACTION: Unremediated liquefiable subsoil layer under high-load whitespace pad."
    ]

    fy = 945
    for flaw in flaws:
        d.text((70, fy), flaw, font=get_font(13, True), fill=(254, 202, 202))
        fy += 26

    # Save to blog and books
    filename = "fig-facility-location-due-diligence-matrix.png"
    target_site = OUT_SITE / filename
    target_book = OUT_BOOK / filename

    im.save(target_site, "PNG", optimize=True)
    shutil.copyfile(target_site, target_book)
    print(f"Generated {target_site} successfully!")

if __name__ == "__main__":
    generate_diagram()
