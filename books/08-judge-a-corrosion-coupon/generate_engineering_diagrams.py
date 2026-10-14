#!/usr/bin/env python3
"""
Generate Flagship Engineering Diagrams for Book 08: Judge a Corrosion Coupon
Author: Tristan (Data Center Field Guides)
Focus: Airborne Gaseous Reactivity Coupons, ISA-71.04-2013, Copper/Silver Metallurgy,
Chemical Filtration Media, Makeup Air Pressurization, and Real-Time QCM Monitors.
Resolution: 1800 x 1100, publication-grade vector styling.
Palette: Deep slate blue / copper amber / silver grey / corrosion rust / acid green.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = Path("/Users/geese/Downloads/book/books/08-judge-a-corrosion-coupon/figures")
FONT_DIR = Path("/Users/geese/Downloads/book/books/01-liquid-load-bank/fonts")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Theme Palette (Atmospheric Corrosion & Environmental Reactivity)
BG = (15, 23, 42)          # Deep slate blue
PANEL = (30, 41, 59)       # Medium slate
GRID = (51, 65, 85)        # Slate grid
TEXT = (248, 250, 252)     # Crisp white
MUTED = (148, 163, 184)    # Cool grey
COPPER = (217, 119, 6)     # Pure copper C11000 / warm amber
SILVER = (226, 232, 240)   # Pure silver 99.99% / cool platinum
RUST = (220, 38, 38)       # Severe corrosion / Class GX
RED = (239, 68, 68)        # Alarm / Rejection
AMBER = (245, 158, 11)     # Warning / Class G2 / G3
GREEN = (34, 197, 94)      # Class G1 Mild / Clean Air
CYAN = (6, 182, 212)       # QCM Telemetry / Gas Monitoring
ACID = (234, 179, 8)       # Chemical media / sulfur acid


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
    d.rectangle((20, 20, w - 21, h - 21), outline=COPPER, width=2)
    return im, d


def draw_header(d, num, title, subtitle):
    d.rectangle((40, 35, 1760, 115), fill=PANEL, outline=COPPER, width=2)
    d.text((60, 48), f"FIGURE 08.{num} :: {title.upper()}", font=get_font(24, True), fill=COPPER)
    d.text((60, 82), subtitle, font=get_font(16), fill=MUTED)
    d.text((1440, 58), "BOOK 08 // AIR CORROSION", font=get_font(16, True), fill=CYAN)


def wrap_text(d, text, font, max_width):
    words = str(text).split(" ")
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
# FIG 1: Dual Copper & Silver Coupon Anatomy
# -------------------------------------------------------------
def fig_01():
    im, d = new_canvas()
    draw_header(d, 1, "Dual Copper & Silver Corrosion Coupon Anatomy (ISA-71.04)",
                "Standard atmospheric reactivity monitoring specimens. The normalized 30-day reactivity equation and why measuring both metals is mandatory.")

    # Left: Physical Coupon Geometry (x: 60 to 860)
    d.rectangle((60, 150, 860, 1040), fill=PANEL, outline=COPPER, width=2)
    d.text((80, 175), "STANDARD DUAL-METAL REACTIVITY COUPON", font=get_font(17, True), fill=COPPER)

    # Carrier frame
    fx, fy, fw, fh = 140, 230, 640, 320
    d.rectangle((fx, fy, fx + fw, fy + fh), fill=(20, 28, 45), outline=TEXT, width=2)
    d.text((fx + 180, fy + 20), "INERT PTFE / ACRYLIC CARRIER", font=get_font(13, True), fill=MUTED)

    # Copper strip
    d.rectangle((fx + 60, fy + 60, fx + 260, fy + 260), fill=COPPER, outline=TEXT, width=1)
    d.text((fx + 90, fy + 140), "COPPER (Cu)\n99.99% PURE", font=get_font(15, True), fill=TEXT)

    # Silver strip
    d.rectangle((fx + 380, fy + 60, fx + 580, fy + 260), fill=SILVER, outline=TEXT, width=1)
    d.text((fx + 405, fy + 140), "SILVER (Ag)\n99.99% PURE", font=get_font(15, True), fill=BG)

    d.text((fx + 60, fy + 280), "Measures: H2S, SO2, Moisture", font=get_font(12, True), fill=COPPER)
    d.text((fx + 380, fy + 280), "Measures: Cl2, Ozone, Reduced S", font=get_font(12, True), fill=CYAN)

    # Metadata specs below graphic
    specs = [
        ("WHY MEASURING BOTH IS MANDATORY", "• Modern lead-free circuit boards use immersion silver (ImAg) and SAC solder.\n• Silver reacts violently to chlorine and reduced sulfur gases that leave copper untouched.\n• Copper reacts strongly to sulfur dioxide and relative humidity.\n• A report showing 'Clean Copper' with an unmeasured silver strip is NOT A PASS."),
        ("COULOMETRIC REDUCTION METHOD", "• Laboratory determines corrosion product film thickness via cathodic reduction.\n• Precision: Measured in Angstroms (1 Å = 10⁻¹⁰ meters = 0.1 nanometers).\n• Identifies specific compound salts: Cu2S, Cu2O, Ag2S, AgCl."),
        ("EXPOSURE TIMING WINDOW", "• Standard exposure: Exactly 30 to 90 continuous days in live airflow.\n• Normalized rate: R_30 = (Film Thickness * 30) / Exposure Days.\n• Exposures under 14 days are invalid due to initial surface passivation dynamics."),
    ]

    sy = 580
    for stit, sdesc in specs:
        d.rectangle((80, sy, 840, sy + 135), fill=(20, 28, 45), outline=GRID, width=1)
        d.text((95, sy + 12), stit, font=get_font(14, True), fill=COPPER)
        lines = sdesc.split("\n")
        yy = sy + 36
        for l in lines:
            d.text((95, yy), l, font=get_font(12), fill=TEXT)
            yy += 22
        sy += 150

    # Right: The Mathematical Normalization Equation (x: 900 to 1740)
    d.rectangle((900, 150, 1740, 1040), fill=(24, 32, 47), outline=CYAN, width=2)
    d.text((920, 175), "THE 30-DAY NORMALIZED REACTIVITY EQUATION", font=get_font(18, True), fill=CYAN)

    # Big Equation Box
    d.rectangle((920, 220, 1720, 420), fill=PANEL, outline=CYAN, width=2)
    d.text((950, 245), "NORMALIZED REACTIVITY RATE EQUATION:", font=get_font(16, True), fill=CYAN)
    d.text((950, 290), "R_30 = [ X_film * 30 ] / T_days", font=get_font(28, True), fill=ACID)
    d.text((950, 350), "Where:", font=get_font(14, True), fill=TEXT)
    d.text((950, 375), "• X_film = Total corrosion product thickness in Angstroms (Å)", font=get_font(13), fill=MUTED)
    d.text((950, 400), "• T_days = Verified physical calendar exposure duration in days", font=get_font(13), fill=MUTED)

    # Worked Example
    d.rectangle((920, 460, 1720, 1010), fill=PANEL, outline=GRID, width=1)
    d.text((950, 480), "WORKED LAB EXAMPLE: LEAD-FREE AI COMPUTE HALL", font=get_font(15, True), fill=COPPER)

    example_steps = [
        ("Deployment Period", "Coupon hung: 2026-07-01 | Retrieved: 2026-09-29 -> T = 90 Days"),
        ("Copper Analysis (Cu)", "Cathodic reduction film thickness: X_Cu = 240 Å of Cu2S/Cu2O"),
        ("Normalized Copper Rate", "R_Cu = (240 * 30) / 90 = 80 Å / 30 Days  [PASSES CLASS G1 < 300 Å]"),
        ("Silver Analysis (Ag)", "Cathodic reduction film thickness: X_Ag = 1,440 Å of Ag2S/AgCl"),
        ("Normalized Silver Rate", "R_Ag = (1440 * 30) / 90 = 480 Å / 30 Days [FAILS CLASS G1 < 200 Å!]"),
        ("ISA-71.04 RATING", "OVERALL CLASSIFICATION: CLASS G2 (MODERATE CORROSIVE)"),
        ("OPERATIONAL VERDICT", "Copper was green (80 Å), but Silver failed (480 Å)! IT server warranty VOID. REFUSE."),
    ]

    ey = 520
    for etit, evalue in example_steps:
        d.text((950, ey), etit + ":", font=get_font(13, True), fill=CYAN if not "VERDICT" in etit else RED)
        wlines = wrap_text(d, evalue, get_font(12, True if "VERDICT" in etit else False), 480)
        yy = ey
        for wl in wlines:
            d.text((1220, yy), wl, font=get_font(12, True if "VERDICT" in etit else False), fill=TEXT if not "VERDICT" in etit else RED)
            yy += 18
        ey += max(68, yy - ey + 24)

    im.save(OUT_DIR / "fig-01-isa-coupon-anatomy-and-reactivity-rate.png", "PNG")
    print("Saved: fig-01-isa-coupon-anatomy-and-reactivity-rate.png")


# -------------------------------------------------------------
# FIG 2: ISA-71.04 Severity Classification Matrix
# -------------------------------------------------------------
def fig_02():
    im, d = new_canvas()
    draw_header(d, 2, "ISA-71.04-2013 Environmental Severity Classification Matrix",
                "Severity levels G1 through GX. How micro-corrosion destroys lead-free immersion silver PCBs and creeps across solder micro-vias.")

    # Left: Severity Table (x: 60 to 920)
    d.rectangle((60, 150, 920, 1040), fill=PANEL, outline=GREEN, width=2)
    d.text((80, 175), "ISA-71.04-2013 SEVERITY TIERS (ANGSTROMS / 30 DAYS)", font=get_font(17, True), fill=GREEN)

    headers = ["SEVERITY CLASS", "COPPER RATE", "SILVER RATE", "HARDWARE IMPACT"]
    widths = [180, 180, 180, 280]
    ty = 220

    # Header Row
    d.rectangle((80, ty, 900, ty + 38), fill=(20, 28, 45), outline=GRID, width=1)
    hx = 90
    for idx, h in enumerate(headers):
        d.text((hx, ty + 10), h, font=get_font(12, True), fill=GREEN)
        hx += widths[idx]

    rows = [
        ("G1 - MILD", "< 300 Å", "< 200 Å", "Clean. IT warranty valid. Reliable."),
        ("G2 - MODERATE", "300 - 1000 Å", "200 - 1000 Å", "Corrosion measurable. Risk to silver."),
        ("G3 - HARSH", "1000 - 2000 Å", "1000 - 2000 Å", "Aggressive attack. Rapid failure."),
        ("GX - SEVERE", ">= 2000 Å", ">= 2000 Å", "Immediate failure. Electronic rot."),
    ]

    ry = ty + 38
    for r in rows:
        col = GREEN if "G1" in r[0] else (AMBER if "G2" in r[0] else (RUST if "G3" in r[0] else RED))
        d.rectangle((80, ry, 900, ry + 55), fill=(20, 28, 45) if (ry // 55) % 2 == 0 else PANEL, outline=GRID, width=1)
        rx = 90
        for cidx, val in enumerate(r):
            d.text((rx, ry + 16), val, font=get_font(12, True if cidx == 0 else False), fill=col if cidx == 0 else TEXT)
            rx += widths[cidx]
        ry += 55

    # Narrative explanation below table
    d.text((80, 520), "THE HARD G1 CONTRACTUAL GATING LAW", font=get_font(15, True), fill=COPPER)
    d.text((80, 550), "• Enterprise IT manufacturers (Dell, HPE, Cisco, NVIDIA) require Class G1 environmental compliance.", font=get_font(12), fill=TEXT)
    d.text((80, 575), "• If an operational hall operates in Class G2 or G3, hardware component warranties are VOID.", font=get_font(12, True), fill=RED)
    d.text((80, 600), "• RoHS lead-free solders (SAC305) and immersion silver PCB traces are 50x more sensitive to gaseous sulfur", font=get_font(12), fill=TEXT)
    d.text((80, 620), "  than obsolete leaded (Sn/Pb) boards from twenty years ago.", font=get_font(12), fill=TEXT)
    d.text((80, 650), "• Never accept Class G2 as 'good enough.' G2 is an active chemical attack on server motherboards.", font=get_font(12, True), fill=AMBER)

    # Right: Creep Corrosion & Micro-Via Failure Graphic (x: 960 to 1740)
    d.rectangle((960, 150, 1740, 1040), fill=(24, 32, 47), outline=RED, width=2)
    d.text((980, 175), "CREEP CORROSION MECHANISM ON LEAD-FREE PCBS", font=get_font(17, True), fill=RED)

    # Visual PCB Traces
    d.rectangle((1000, 220, 1700, 560), fill=PANEL, outline=TEXT, width=1)
    # PCB Green substrate
    d.rectangle((1020, 240, 1680, 540), fill=(20, 83, 45), outline=GRID, width=1)
    # Trace A and Trace B
    d.rectangle((1060, 300, 1300, 340), fill=COPPER, outline=TEXT, width=1)
    d.rectangle((1400, 300, 1640, 340), fill=COPPER, outline=TEXT, width=1)
    d.text((1070, 312), "Trace A (12V DC)", font=get_font(12, True), fill=TEXT)
    d.text((1410, 312), "Trace B (Ground)", font=get_font(12, True), fill=TEXT)

    # Dendritic Creep between traces
    for dx in range(1300, 1400, 8):
        d.line((dx, 320, dx + 6, 315), fill=SILVER, width=2)
        d.line((dx, 320, dx + 6, 325), fill=SILVER, width=2)
    d.text((1270, 270), "SILVER DENDRITE WHISKERS\nCreeping across soldermask", font=get_font(12, True), fill=RED)

    d.text((1000, 600), "HOW SILVER SULFIDE (Ag2S) DESTROYS SERVER BOARDS:", font=get_font(15, True), fill=ACID)
    steps = [
        ("1. Sulfur Adsorption", "Gaseous H2S or sulfur vapor reacts with silver metal plating on SMD resistors."),
        ("2. Volumetric Expansion", "Silver sulfide (Ag2S) crystal structure expands and cracks the conformal coating."),
        ("3. Dendritic Creep", "Conductive Ag2S dendrites migrate across the FR4 soldermask surface between adjacent pins."),
        ("4. Electrical Short-Circuit", "Dendrite bridges 12V rail to ground, sparking an unrecoverable server motherboard trip."),
    ]
    dy = 640
    for stit, sdesc in steps:
        d.text((1000, dy), stit + ":", font=get_font(13, True), fill=CYAN)
        wlines = wrap_text(d, sdesc, get_font(12), 510)
        yy = dy
        for wl in wlines:
            d.text((1200, yy), wl, font=get_font(12), fill=TEXT)
            yy += 18
        dy += max(45, yy - dy + 15)

    im.save(OUT_DIR / "fig-02-isa-71-04-severity-classification-matrix.png", "PNG")
    print("Saved: fig-02-isa-71-04-severity-classification-matrix.png")


# -------------------------------------------------------------
# FIG 3: Coupon Placement Topology
# -------------------------------------------------------------
def fig_03():
    im, d = new_canvas()
    draw_header(d, 3, "Data Center Coupon Spatial Placement Architecture",
                "Where to hang coupons. Airflow velocity windows, height elevations, and the 4 mandatory test stations.")

    # 4 Gating Stations Layout
    d.rectangle((60, 150, 1740, 680), fill=(20, 28, 45), outline=CYAN, width=2)
    d.text((90, 175), "THE FOUR MANDATORY COUPON MONITORING STATIONS", font=get_font(18, True), fill=CYAN)

    stations = [
        ("STATION 1: RAW OUTDOOR MAKEUP", "Outdoor Air Intake Louver", "• Establishes environmental ambient baseline.\n• Detects seasonal smog, agricultural H2S, industrial SO2.\n• Demonstrates raw threat entering building.\n• Elevation: 2.0m above grade, sheltered from rain.", CYAN),
        ("STATION 2: POST-FILTER DISCHARGE", "Chemical Filtration Unit Discharge", "• Proves single-pass chemical filter efficiency.\n• Verified Class G1 air entering supply duct.\n• Breakthrough warning: If Station 2 exceeds G1, media is spent.\n• Location: Immediately downstream of deep-bed carbon.", GREEN),
        ("STATION 3: COLD AISLE IT INGESTION", "Server Rack Ingestion Face", "• The ultimate contractual SLA boundary.\n• Elevation: 1.2m (mid-rack server level).\n• Velocity: 0.5 to 1.5 m/s in primary air stream.\n• Must remain Class G1 under all operating loads.", COPPER),
        ("STATION 4: HOT AISLE EXHAUST", "Hot Aisle Containment / Ceiling Return", "• Verifies room recirculation dynamics.\n• Detects internal outgassing from PVC cables & packaging.\n• Elevated temperature (35°C to 45°C) accelerates corrosion kinetics.\n• Proves total room chemical balance.", AMBER),
    ]

    for k, (stit, sloc, sbody, scol) in enumerate(stations):
        sx = 90 + k * 410
        d.rectangle((sx, 220, sx + 380, 650), fill=PANEL, outline=scol, width=2)
        d.text((sx + 15, 240), stit, font=get_font(14, True), fill=scol)
        d.text((sx + 15, 270), sloc, font=get_font(12, True), fill=MUTED)
        d.line((sx + 15, 295, sx + 365, 295), fill=GRID, width=1)
        lines = sbody.split("\n")
        yy = 315
        for l in lines:
            wlines = wrap_text(d, l, get_font(12), 350)
            for wl in wlines:
                d.text((sx + 15, yy), wl, font=get_font(12), fill=TEXT)
                yy += 20
            yy += 6

    # Bottom Half: Installation Errors to Refuse
    d.rectangle((60, 720, 1740, 1040), fill=PANEL, outline=RED, width=2)
    d.text((90, 745), "CORROSION COUPON HANGING ERRORS THAT VOID THE TEST", font=get_font(16, True), fill=RED)

    errors = [
        ("THE DEAD AIR POCKET ERROR", "Hanging a coupon inside a quiet corner, behind a structural column, or inside an empty unpowered server cabinet where air velocity is zero (v < 0.1 m/s). Without airflow, gaseous boundary layer starvation occurs, reporting false G1 clean air."),
        ("THE HUMIDIFIER BLAST ERROR", "Hanging a coupon directly in front of an ultrasonic humidifier mist discharge or direct cooling coil carryover. Water droplets soak the strip, triggering liquid droplet oxidation rather than atmospheric gas reactivity."),
        ("THE BARE-FINGER CONTAMINATION", "Touching the metal coupon surface with bare human fingers during hanging or retrieval. Fingerprint skin oils contain sodium chloride (salt) and fatty acids that cause localized finger-shaped corrosion patches. Use powder-free nitrile gloves."),
        ("THE UNACCOMPANIED BLANK ERROR", "Deploying coupons without a sealed 'Travel Blank' control coupon. A travel blank travels to the site, remains unopened in its hermetic bag, and returns to the lab. Without a blank, shipping contamination cannot be mathematically subtracted."),
    ]

    ey = 785
    for etit, edesc in errors:
        d.text((90, ey), etit + ":", font=get_font(13, True), fill=CYAN)
        wlines = wrap_text(d, edesc, get_font(12), 1330)
        yy = ey
        for wl in wlines:
            d.text((370, yy), wl, font=get_font(12), fill=TEXT)
            yy += 18
        ey += max(55, yy - ey + 15)

    im.save(OUT_DIR / "fig-03-data-hall-coupon-placement-topology.png", "PNG")
    print("Saved: fig-03-data-hall-coupon-placement-topology.png")


# -------------------------------------------------------------
# FIG 4: Chemical Filtration Media & Breakthrough
# -------------------------------------------------------------
def fig_04():
    im, d = new_canvas()
    draw_header(d, 4, "Chemical Filtration Media & Gas Breakthrough Dynamics",
                "Deep-bed scrubbers. Impregnated carbon, potassium permanganate alumina, and spent media remaining life testing.")

    # Left: Media Types (x: 60 to 860)
    d.rectangle((60, 150, 860, 1040), fill=PANEL, outline=ACID, width=2)
    d.text((80, 175), "GAS PURIFICATION MEDIA CLASSIFICATION", font=get_font(17, True), fill=ACID)

    medias = [
        ("1. VIRGIN ACTIVATED CARBON (VAC)", "Target: High Molecular Weight VOCs & Hydrocarbons\n• Base material: Bituminous coal or coconut shell.\n• Mechanism: Physical adsorption inside micropores.\n• Ineffective for: H2S, SO2, Chlorine, Ammonia.\n• CTC Activity: Minimum >= 60% by weight.", CYAN),
        ("2. CAUSTIC IMPREGNATED CARBON", "Target: Acid Gases (H2S, SO2, HF, HCl)\n• Impregnation: 4% to 8% Potassium Hydroxide (KOH).\n• Mechanism: Chemisorption neutralization.\n• Forms stable potassium salts on pore surfaces.\n• Must maintain minimum 40% relative humidity to activate.", COPPER),
        ("3. OXIDIZING PERMANGANATE ALUMINA", "Target: Reduced Sulfur, Ethylene, Nitric Oxide (NOx)\n• Base: Active porous alumina (Al2O3) impregnated with 4% to 8% Potassium Permanganate (KMnO4).\n• Mechanism: Permanent chemical oxidation.\n• Color change: Purple (Fresh) -> Brown (Spent).", (168, 85, 247)),
        ("4. DUAL-BED BLENDED SYSTEM", "The Standard Mission-Critical Configuration\n• Stage 1 (Upstream): Impregnated Carbon (Acid gas bulk strip).\n• Stage 2 (Downstream): Permanganate Alumina (Fine polish).", GREEN),
    ]

    my = 220
    for mtit, mdesc, mcol in medias:
        d.rectangle((80, my, 840, my + 175), fill=(20, 28, 45), outline=mcol, width=1)
        d.text((95, my + 15), mtit, font=get_font(15, True), fill=mcol)
        lines = mdesc.split("\n")
        yy = my + 45
        for l in lines:
            d.text((95, yy), l, font=get_font(12), fill=TEXT)
            yy += 24
        my += 195

    # Right: Breakthrough Curve Graphic (x: 900 to 1740)
    d.rectangle((900, 150, 1740, 1040), fill=(24, 32, 47), outline=RED, width=2)
    d.text((920, 175), "MEDIA BREAKTHROUGH CURVE & SPENT TESTING", font=get_font(17, True), fill=RED)

    # Breakthrough graph
    gx, gy, gw, gh = 940, 240, 760, 360
    d.rectangle((gx, gy, gx + gw, gy + gh), fill=PANEL, outline=GRID, width=1)

    # Axes
    d.line((gx + 60, gy + 320, gx + 720, gy + 320), fill=MUTED, width=2) # Time axis
    d.line((gx + 60, gy + 40, gx + 60, gy + 320), fill=MUTED, width=2)   # Concentration axis
    d.text((gx + 70, gy + 325), "Time (Months in Service) --->", font=get_font(12), fill=MUTED)
    d.text((gx + 10, gy + 20), "Outlet Gas Conc (C_out / C_in)", font=get_font(12), fill=MUTED)

    # 5% Breakthrough Line
    d.line((gx + 60, gy + 220, gx + 720, gy + 220), fill=AMBER, width=1)
    d.text((gx + 80, gy + 200), "5% BREAKTHROUGH ACTION LINE (Cure Deadline)", font=get_font(11, True), fill=AMBER)

    # Breakthrough curve
    b_pts = [
        (gx + 60, gy + 315), (gx + 180, gy + 315), (gx + 300, gy + 312),
        (gx + 420, gy + 300), (gx + 480, gy + 270), (gx + 540, gy + 220), # crosses 5%
        (gx + 600, gy + 120), (gx + 660, gy + 60) # steep breakthrough
    ]
    for k in range(len(b_pts) - 1):
        d.line((b_pts[k], b_pts[k+1]), fill=RED, width=3)

    d.text((gx + 545, gy + 230), "Day 240: Media Spent!", font=get_font(12, True), fill=RED)

    # Testing protocols below graph
    d.rectangle((940, 630, 1700, 1000), fill=PANEL, outline=GRID, width=1)
    d.text((960, 650), "SPENT MEDIA LABORATORY GATING TESTS (ASTM D2854 / D3838)", font=get_font(15, True), fill=CYAN)

    tests = [
        ("Apparent Density (AD)", "Fresh media: 0.50 g/cm³ -> Spent media: 0.65 g/cm³ (Loaded with sulfur/acid salts)."),
        ("Active Permanganate Titration", "Fresh KMnO4: 4.0% wt -> Rejection Threshold: <= 0.5% wt (Oxidizing capacity dead)."),
        ("Carbon CTC Retention", "Measures residual micro-porosity. Rejection: CTC activity drops below 20% of virgin rating."),
        ("Operational Rule", "Sample media every 90 days. When remaining life reaches 15%, procure media replacement."),
    ]
    tyy = 690
    for ttit, tdesc in tests:
        d.text((960, tyy), ttit + ":", font=get_font(13, True), fill=COPPER)
        wlines = wrap_text(d, tdesc, get_font(12), 480)
        yy = tyy
        for wl in wlines:
            d.text((1200, yy), wl, font=get_font(12), fill=TEXT)
            yy += 18
        tyy += max(65, yy - tyy + 20)

    im.save(OUT_DIR / "fig-04-chemical-filtration-media-and-breakthrough.png", "PNG")
    print("Saved: fig-04-chemical-filtration-media-and-breakthrough.png")


# -------------------------------------------------------------
# FIG 5: Makeup Air Pressurization & Infiltration
# -------------------------------------------------------------
def fig_05():
    im, d = new_canvas()
    draw_header(d, 5, "Makeup Air Positive Pressurization & Envelope Sealing",
                "Why a multi-million-dollar chemical scrubber is useless if negative room pressure sucks untreated raw outdoor air through building cracks.")

    # Center: The Data Hall Aerodynamic Balance Diagram
    dx, dy, dw, dh = 60, 150, 1740, 540
    d.rectangle((dx, dy, dx + dw, dy + dh), fill=(20, 28, 45), outline=GREEN, width=2)
    d.text((80, 175), "THE PRESSURIZATION FIREWALL: +15 Pa TO +25 Pa POSITIVE PRESSURE", font=get_font(17, True), fill=GREEN)

    # Outdoor vs Indoor boundary
    # Outdoor Zone (Left)
    d.rectangle((80, 220, 480, 650), fill=(30, 41, 59), outline=RUST, width=2)
    d.text((100, 240), "OUTDOOR ENVIRONMENT\n(CORROSIVE AMBIENT AIR)", font=get_font(14, True), fill=RUST)
    d.text((100, 290), "• Pressure: P_atm = 0.0 Pa (Reference)\n• Contaminants: H2S, SO2, NOx, Cl2\n• Relative Humidity: High / Fog", font=get_font(12), fill=MUTED)

    # Chemical Makeup Unit
    d.rectangle((480, 260, 780, 400), fill=PANEL, outline=CYAN, width=2)
    d.text((500, 280), "MAKEUP AIR UNIT (MAU)\nChemical Scrubber Bed\nFlow: Q_makeup", font=get_font(13, True), fill=CYAN)
    d.line((480, 330, 780, 330), fill=GREEN, width=4)

    # Data Hall Protected Envelope (Right)
    d.rectangle((780, 220, 1720, 650), fill=(15, 23, 42), outline=GREEN, width=2)
    d.text((800, 240), "DATA HALL PROTECTED ENVELOPE (POSITIVE PRESSURE: +20.0 Pa)", font=get_font(16, True), fill=GREEN)
    d.text((800, 275), "Class G1 Clean Air Environment (< 300 Å Cu / < 200 Å Ag)", font=get_font(13, True), fill=CYAN)

    # Leakage arrows out
    d.line((1100, 650, 1100, 680), fill=GREEN, width=3)
    d.text((950, 615), "Controlled Outward Exfiltration (Zero Infiltration Permitted)", font=get_font(12, True), fill=GREEN)

    # Infiltration paths (The Enemies)
    d.rectangle((800, 320, 1700, 520), fill=PANEL, outline=GRID, width=1)
    d.text((820, 335), "UNCONTROLLED LEAK PATHS THAT VOID CORROSION PROTECTION:", font=get_font(14, True), fill=RED)

    leaks = [
        ("Cable Penetrations", "Unsealed conduit sleeves and cable trays penetrating external walls."),
        ("Raised Floor Perimeters", "Gap between raised floor stringers and un-caulked precast concrete walls."),
        ("Emergency Exit Doors", "Damaged perimeter neoprene weatherstripping; doors propped open by staff."),
        ("Drain Traps & P-Traps", "Dry air conditioning condensate drain traps allowing raw sewer gas into whitespace."),
    ]
    ly = 370
    for ltit, ldesc in leaks:
        d.text((820, ly), "• " + ltit + ":", font=get_font(12, True), fill=AMBER)
        d.text((1020, ly), ldesc, font=get_font(12), fill=TEXT)
        ly += 32

    # Bottom Half: The Mathematical Pressurization Calculation
    d.rectangle((60, 720, 1740, 1040), fill=PANEL, outline=GRID, width=1)
    d.text((80, 745), "THE AIR BALANCE GOVERNING EQUATION", font=get_font(16, True), fill=CYAN)

    d.text((80, 785), "Q_makeup = Q_exhaust + Q_exfiltration", font=get_font(20, True), fill=ACID)
    d.text((80, 825), "• Q_makeup: Purified air delivered by chemical makeup unit.", font=get_font(13), fill=TEXT)
    d.text((80, 855), "• Q_exhaust: Air discharged by battery room and restroom exhaust fans.", font=get_font(13), fill=TEXT)
    d.text((80, 885), "• Q_exfiltration = C * A_leak * (Delta_P)^0.65 : Outward air leaking through envelope cracks at +20 Pa.", font=get_font(13), fill=MUTED)
    d.text((80, 925), "THE OPERATIONAL LAW: If Delta_P drops below +10.0 Pa, the makeup fan speed must ramp up immediately.", font=get_font(13, True), fill=AMBER)
    d.text((80, 955), "A room with Delta_P <= 0 Pa is in INFILTRATION FAILURE. Contaminated outdoor air is entering unchecked.", font=get_font(13, True), fill=RED)

    im.save(OUT_DIR / "fig-05-makeup-air-pressurization-and-leak-paths.png", "PNG")
    print("Saved: fig-05-makeup-air-pressurization-and-leak-paths.png")


# -------------------------------------------------------------
# FIG 6: Passive Coupons vs. Real-Time QCM Monitors
# -------------------------------------------------------------
def fig_06():
    im, d = new_canvas()
    draw_header(d, 6, "Passive Reactivity Coupons vs. Real-Time QCM Telemetry",
                "30-day passive integration vs 1-minute Quartz Crystal Microbalance (QCM) telemetry. Detecting short-duration generator exhaust spikes.")

    # Left: Passive Coupon Limits (x: 60 to 860)
    d.rectangle((60, 150, 860, 1040), fill=PANEL, outline=MUTED, width=2)
    d.text((80, 175), "PASSIVE CORROSION COUPONS (30-90 DAYS)", font=get_font(17, True), fill=MUTED)
    d.text((80, 205), "The Historical Integrated Average", font=get_font(13), fill=MUTED)

    pass_items = [
        ("NATURE OF RESULT", "Provides a single, historical, time-weighted average rate over 30 to 90 days. It is a postmortem confirmation of past air quality."),
        ("THE TRANSIENT DILUTION FLAW", "A violent 4-hour toxic gas event (e.g. diesel generator testing exhaust sucked into fresh air intake) is diluted across 30 days. The coupon reports 'Class G1 Clean', hiding the event that damaged the boards."),
        ("TURNAROUND LATENCY", "Requires unhanging, mailing to an analytical laboratory, coulometric chemical reduction, and reporting: Latency is 14 to 28 days."),
        ("PRIMARY UTILITY", "The definitive legal baseline for manufacturer warranty audits and quarterly SLA compliance verification."),
    ]

    py = 250
    for ptit, pdesc in pass_items:
        d.rectangle((80, py, 840, py + 165), fill=(20, 28, 45), outline=GRID, width=1)
        d.text((95, py + 15), ptit, font=get_font(14, True), fill=COPPER)
        words = pdesc.split()
        cur, l_list = "", []
        for w in words:
            if d.textlength(cur + " " + w, font=get_font(12)) <= 700:
                cur += (" " if cur else "") + w
            else:
                l_list.append(cur)
                cur = w
        if cur:
            l_list.append(cur)
        for k, line in enumerate(l_list):
            d.text((95, py + 45 + k * 22), line, font=get_font(12), fill=TEXT)
        py += 185

    # Right: Real-Time QCM Telemetry (x: 900 to 1740)
    d.rectangle((900, 150, 1740, 1040), fill=(24, 32, 47), outline=CYAN, width=2)
    d.text((920, 175), "REAL-TIME QUARTZ CRYSTAL MICROBALANCE (QCM)", font=get_font(17, True), fill=CYAN)
    d.text((920, 205), "Active Micro-Mass Telemetry (1-Minute Resolution)", font=get_font(13), fill=MUTED)

    # QCM Physics Box
    d.rectangle((920, 240, 1720, 480), fill=PANEL, outline=CYAN, width=1)
    d.text((945, 260), "QCM MEASUREMENT PRINCIPLE (THE SAUERBREY EQUATION):", font=get_font(15, True), fill=CYAN)
    d.text((945, 295), "Delta_f = - C_f * Delta_m", font=get_font(24, True), fill=ACID)
    d.text((945, 345), "• Quartz crystal coated with thin film of pure Copper or Silver.", font=get_font(12), fill=TEXT)
    d.text((945, 370), "• Resonates at high frequency (e.g. 6 MHz).", font=get_font(12), fill=TEXT)
    d.text((945, 395), "• As corrosive gases react with metal, mass increases (Delta_m).", font=get_font(12), fill=TEXT)
    d.text((945, 420), "• Resonance frequency drops proportionally (Delta_f): 1 Å sensitivity!", font=get_font(12, True), fill=GREEN)

    # Transient Spike Detection Box
    d.rectangle((920, 510, 1720, 1010), fill=PANEL, outline=GRID, width=1)
    d.text((945, 530), "REAL-TIME INCIDENT DETECTION CAPABILITY", font=get_font(15, True), fill=AMBER)

    qcm_benefits = [
        ("INSTANT EXCURSION ALARM", "Detects toxic gas ingress within 15 minutes of occurrence, triggering damper closure."),
        ("SOURCE CORRELATION", "Correlates gas spikes to specific physical events: diesel generator starts, chemical spill, roof tarring, or agricultural manure spreading."),
        ("FILTER FAILURE WARNING", "Monitors chemical scrubber discharge in real-time; sounds alarm the instant media breaks through."),
        ("OPERATIONAL GATING RULE", "Use QCM telemetry for real-time control room alarming; use 30-day passive coupons for legal SLA warranty compliance."),
    ]

    qy = 575
    for qtit, qdesc in qcm_benefits:
        d.text((945, qy), qtit + ":", font=get_font(13, True), fill=CYAN)
        wlines = wrap_text(d, qdesc, get_font(12), 500)
        yy = qy
        for wl in wlines:
            d.text((1200, yy), wl, font=get_font(12), fill=TEXT)
            yy += 18
        qy += max(100, yy - qy + 25)

    im.save(OUT_DIR / "fig-06-passive-coupons-vs-realtime-qcm-monitors.png", "PNG")
    print("Saved: fig-06-passive-coupons-vs-realtime-qcm-monitors.png")


# -------------------------------------------------------------
# FIG 7: Master Corrosion Coupon Sheet & Refusal
# -------------------------------------------------------------
def fig_07():
    im, d = new_canvas()
    draw_header(d, 7, "The Master Atmospheric Corrosion Coupon Ledger & Refusal Sheet",
                "The immutable site and laboratory record. Pre-test blanks, 30-day normalized rates, ISA severity class, and the signed operational refusal.")

    # Top Overview Box
    d.rectangle((60, 150, 1740, 230), fill=PANEL, outline=COPPER, width=2)
    d.text((90, 165), "THE CORROSION CONTRACT: NO AIR ENVELOPE CLAIMED WITHOUT DUAL-METAL LAB DATA", font=get_font(18, True), fill=COPPER)
    d.text((90, 195), "A clean particle count or an air filter replacement invoice is NOT evidence of corrosion control.", font=get_font(13), fill=TEXT)
    d.text((90, 215), "Evidence is the certified coulometric reduction report: Copper Rate + Silver Rate + Travel Blank control.", font=get_font(13, True), fill=CYAN)

    # Simulated Master Coupon Sheet Table
    headers = ["STATION / ID", "COUPON SN", "BLANK SN", "EXPOSURE", "CU RATE", "AG RATE", "ISA CLASS", "VERDICT"]
    widths = [240, 180, 180, 180, 180, 180, 180, 260]
    tx, ty = 60, 250

    # Header Row
    d.rectangle((tx, ty, tx + 1640, ty + 40), fill=(20, 28, 45), outline=COPPER, width=1)
    hx = tx + 10
    for idx, h in enumerate(headers):
        d.text((hx, ty + 10), h, font=get_font(12, True), fill=COPPER)
        hx += widths[idx]

    rows = [
        ("STATION 1: FRESH INTAKE", "CP-OUT-01", "BLK-01", "90 Days", "1,240 Å/30d", "2,850 Å/30d", "Class GX", "BASELINE (Raw Ambient Smog)"),
        ("STATION 2: MAU SCRUBBER", "CP-MAU-01", "BLK-01", "90 Days", "65 Å/30d", "110 Å/30d", "Class G1", "ACCEPTED (Scrubber Operating)"),
        ("STATION 3: POD 1 COLD AISLE", "CP-POD1-01", "BLK-02", "90 Days", "120 Å/30d", "180 Å/30d", "Class G1", "ACCEPTED (SLA Warranty Met)"),
        ("STATION 3: POD 2 COLD AISLE", "CP-POD2-01", "BLK-02", "90 Days", "210 Å/30d", "540 Å/30d", "Class G2", "REFUSED (Silver Exceeded 200Å)"),
        ("STATION 4: HOT RETURN", "CP-RET-01", "BLK-03", "90 Days", "280 Å/30d", "420 Å/30d", "Class G2", "CONDITIONAL (Cable Outgassing)"),
        ("SERVER SUITE 4 (UNSEALED)", "CP-STE4-01", "BLK-03", "90 Days", "850 Å/30d", "1,600 Å/30d", "Class G3", "REFUSED (Pressure Defect -0.5Pa)"),
    ]

    ry = ty + 40
    for r in rows:
        d.rectangle((tx, ry, tx + 1640, ry + 42), fill=PANEL if (ry // 42) % 2 == 0 else (24, 32, 47), outline=GRID, width=1)
        rx = tx + 10
        for cidx, val in enumerate(r):
            col = RED if "REFUSED" in val else (GREEN if "ACCEPTED" in val else (AMBER if "CONDITIONAL" in val else TEXT))
            d.text((rx, ry + 12), val, font=get_font(12, True if cidx in (0, 6, 7) else False), fill=col)
            rx += widths[cidx]
        ry += 42

    # Bottom Architectural Box: The Refusal Statement
    d.rectangle((60, 560, 1740, 1040), fill=(20, 28, 45), outline=RED, width=2)
    d.text((90, 585), "THE STATEMENT OF OPERATIONAL REFUSAL (CLASS G2 / G3 EXCURSION)", font=get_font(17, True), fill=RED)

    refusal_sections = [
        ("SECTION 1: THE OBSERVED LABORATORY EVIDENCE", "Laboratory Report #LAB-2026-904 confirms that Data Hall Pod 2 experienced normalized gaseous reactivity rates of R_Cu = 210 Å/30d and R_Ag = 540 Å/30d over the 90-day exposure period ending 2026-09-29.\nUnder ISA-71.04-2013, this constitutes an environmental classification of CLASS G2 (MODERATE)."),
        ("SECTION 2: CONTRACTUAL & TECHNICAL IMPACT", "The Master Services Agreement mandates Class G1 (< 300 Å Cu / < 200 Å Ag) environmental compliance to protect lead-free immersion silver circuit boards.\nOperating in Class G2 voids manufacturer component warranties and introduces active risk of silver sulfide creep corrosion across micro-vias."),
        ("SECTION 3: MANDATORY OPERATIONAL ACTIONS (THE REFUSAL DIRECTIVE)", "1. Operational acceptance of Data Hall Pod 2 is REFUSED until air quality is remediated to Class G1.\n2. Infiltration audit: Inspect all cable penetration firestops and envelope seals for air leakage.\n3. Chemical media audit: Perform apparent density and permanganate titration tests on MAU-02 scrubber beds.\n4. Positive pressure check: Verify cold aisle differential pressure remains strictly >= +15.0 Pa relative to outdoors."),
        ("SECTION 4: SIGNED STATEMENT OF OPERATIONAL DISSENT", "“I certify that the environmental air envelope in Data Hall Pod 2 does NOT satisfy the contractual criteria for lead-free electronic hardware protection. Commercial handover is REFUSED.”\nSigned: Marcus Vance, PE, Operations Director | Date: 2026-10-14"),
    ]

    sy = 630
    for stit, sdesc in refusal_sections:
        d.rectangle((90, sy, 1710, sy + 88), fill=PANEL, outline=GRID, width=1)
        d.text((110, sy + 10), stit, font=get_font(13, True), fill=AMBER if "SECTION 1" in stit or "SECTION 2" in stit else (RED if "SECTION 3" in stit else CYAN))
        lines = sdesc.split("\n")
        yy = sy + 32
        for l in lines:
            d.text((110, yy), l, font=get_font(11), fill=TEXT)
            yy += 18
        sy += 98

    im.save(OUT_DIR / "fig-07-master-corrosion-coupon-sheet-and-refusal.png", "PNG")
    print("Saved: fig-07-master-corrosion-coupon-sheet-and-refusal.png")


def main():
    print("Generating Flagship Engineering Diagrams for Book 08: Judge a Corrosion Coupon...")
    fig_01()
    fig_02()
    fig_03()
    fig_04()
    fig_05()
    fig_06()
    fig_07()
    print("All 7 Engineering Diagrams successfully generated for Book 08!")


if __name__ == "__main__":
    main()
