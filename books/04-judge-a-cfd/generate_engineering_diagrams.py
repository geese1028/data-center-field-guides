#!/usr/bin/env python3
"""
Generate Flagship High-Resolution Engineering Diagrams for Book 04:
Judge a CFD Model for Data Centers: Field Benchmarking and Report Auditing

Output directory: books/04-judge-a-cfd/figures/
Resolution: 1800 x 1100 px, 300 DPI aesthetic, high-contrast industrial vector style.
Colors: Dark slate theme (BG: #12151c, Card: #1a202c, Cyan: #00e5ff, Blue: #2979ff,
        Orange/Warning: #ff9100, Green/Pass: #00e676, Red/Fail: #ff1744, White: #ffffff).
"""

import math
import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path("/Users/geese/Downloads/book/books/04-judge-a-cfd")
FIG_DIR = ROOT / "figures"
FONT_DIR = Path("/Users/geese/Downloads/book/books/01-liquid-load-bank/fonts")

# Palette constants
BG_COLOR = (18, 21, 28)          # #12151c Deep charcoal slate
PANEL_BG = (26, 32, 44)          # #1a202c Technical card surface
PANEL_BORDER = (45, 55, 72)      # #2d3748 Border outline
GRID_COLOR = (30, 36, 48)        # Subtle coordinate grid
TEXT_MAIN = (255, 255, 255)      # Pure white
TEXT_MUTED = (160, 174, 192)     # Cool silver grey
CYAN = (0, 229, 255)             # Accent cyan (Cold air / Inlets)
BLUE = (41, 121, 255)            # Primary blue (Supply air / Pressure)
AMBER = (255, 171, 0)            # Warning / Recirculation / Transient
RED = (255, 23, 68)              # Hot exhaust air / Hotspots / Refused statements
GREEN = (0, 230, 118)            # Pass / Capture Index >= 90% / Compliant
PURPLE = (179, 136, 255)         # Mesh / Residuals / Mathematics

W, H = 1800, 1100

def get_font(size: int, bold: bool = False):
    font_file = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    font_path = FONT_DIR / font_file
    if font_path.exists():
        return ImageFont.truetype(str(font_path), size)
    return ImageFont.load_default()

def create_base_canvas(title: str, subtitle: str, sheet_ref: str = ""):
    img = Image.new("RGB", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # 1. Subtle background grid
    grid_spacing = 40
    for x in range(0, W, grid_spacing):
        draw.line([(x, 0), (x, H)], fill=GRID_COLOR, width=1)
    for y in range(0, H, grid_spacing):
        draw.line([(0, y), (W, y)], fill=GRID_COLOR, width=1)

    # 2. Outer Technical Border
    draw.rectangle([(20, 20), (W - 20, H - 20)], outline=PANEL_BORDER, width=2)
    # Corner registration marks
    arm = 18
    for cx, cy in [(20, 20), (W - 20, 20), (20, H - 20), (W - 20, H - 20)]:
        dx = arm if cx == 20 else -arm
        dy = arm if cy == 20 else -arm
        draw.line([(cx, cy), (cx + dx, cy)], fill=CYAN, width=3)
        draw.line([(cx, cy), (cx, cy + dy)], fill=CYAN, width=3)

    # 3. Header Banner
    draw.rectangle([(30, 30), (W - 30, 110)], fill=PANEL_BG, outline=PANEL_BORDER, width=2)
    draw.text((50, 42), "FIELD GUIDE 04 // DATA CENTER CFD AUDIT & BENCHMARKING", font=get_font(15, bold=True), fill=CYAN)
    draw.text((50, 68), title.upper(), font=get_font(24, bold=True), fill=TEXT_MAIN)
    draw.text((50, 96), subtitle, font=get_font(13, bold=False), fill=TEXT_MUTED)

    if sheet_ref:
        s_box_w = 310
        draw.rectangle([(W - 45 - s_box_w, 42), (W - 45, 98)], fill=(15, 23, 42), outline=CYAN, width=1)
        draw.text((W - 35 - s_box_w, 52), "REFERENCED MASTER FORM", font=get_font(11, bold=True), fill=AMBER)
        draw.text((W - 35 - s_box_w, 72), sheet_ref, font=get_font(13, bold=True), fill=CYAN)

    # 4. Footer Status Bar
    draw.rectangle([(30, H - 55), (W - 30, H - 30)], fill=PANEL_BG, outline=PANEL_BORDER, width=1)
    draw.text((50, H - 48), "ASME V&V 20 / ASHRAE TC 9.9 GUIDELINES // FIELD PHYSICAL CALIBRATION // ZERO BLIND COLOR ACCEPTANCE",
              font=get_font(12, bold=False), fill=TEXT_MUTED)
    footer_tag = "TRISTAN DATA CENTER FIELD GUIDES // ED. 2026"
    ftw = draw.textlength(footer_tag, font=get_font(12, bold=True))
    draw.text((W - 80 - ftw, H - 48), footer_tag, font=get_font(12, bold=True), fill=CYAN)

    return img, draw

# ==============================================================================
# DIAGRAM 1: CFD Verification & Validation Lifecycle Matrix
# ==============================================================================
def draw_fig_01():
    img, draw = create_base_canvas(
        title="CFD Verification & Validation Lifecycle Architecture",
        subtitle="ASME V&V 20 Pipeline: Geometric Model, Mesh Convergence, Residual Audit, and Field Calibration",
        sheet_ref="SHEET 1 & SHEET 2"
    )

    steps = [
        ("STAGE 1", "Geometry & Inputs", "Boundary Definition",
         ["• Room envelope & floor void", "• CRAH fan curves & heat sinks", "• Server P-Q impedance curves", "• Actual measured feed kW (no nameplate)"],
         PANEL_BG, CYAN),
        ("STAGE 2", "Mesh Independence", "Discretization Audit",
         ["• Grid Convergence Index (GCI)", "• Sub-grid perforated tile cells", "• Boundary layer inflation (y+)", "• Total cell count: 5M to 20M cells"],
         PANEL_BG, BLUE),
        ("STAGE 3", "Solver Convergence", "Mathematical Balance",
         ["• Momentum residuals < 10^-4", "• Energy residual < 10^-6", "• Global mass imbalance < 0.1%", "• Temperature probe monitors flat"],
         PANEL_BG, PURPLE),
        ("STAGE 4", "Field Benchmarking", "Physical Calibration",
         ["• 2-point CRAH supply averages", "• 3-point CRAH return averages", "• 3-tier rack inlet probe trees", "• Ultrasonic tile velocity profile"],
         PANEL_BG, AMBER),
        ("STAGE 5", "Single Decision Gate", "Contractual Handover",
         ["• Design option A vs B ranking", "• As-built compliance audit", "• Root-cause air recirculation", "• Zero ungrounded silicon claims"],
         PANEL_BG, GREEN)
    ]

    card_w = 320
    gap = 25
    start_x = 55
    card_y = 140
    card_h = 440

    for i, (stg, title, sub, bullets, bg, border_c) in enumerate(steps):
        cx = start_x + i * (card_w + gap)
        draw.rectangle([(cx, card_y), (cx + card_w, card_y + card_h)], fill=bg, outline=border_c, width=2)
        draw.rectangle([(cx, card_y), (cx + card_w, card_y + 40)], fill=(20, 26, 38), outline=border_c, width=1)
        draw.text((cx + 15, card_y + 10), stg, font=get_font(15, bold=True), fill=border_c)

        draw.text((cx + 15, card_y + 50), title, font=get_font(14, bold=True), fill=TEXT_MAIN)
        draw.text((cx + 15, card_y + 72), sub, font=get_font(11, bold=False), fill=TEXT_MUTED)
        draw.line([(cx + 12, card_y + 94), (cx + card_w - 12, card_y + 94)], fill=PANEL_BORDER, width=1)

        by = card_y + 110
        for b in bullets:
            draw.text((cx + 12, by), b, font=get_font(11, bold=False), fill=TEXT_MAIN)
            by += 40

        # Status badge at bottom
        draw.rectangle([(cx + 15, card_y + card_h - 48), (cx + card_w - 15, card_y + card_h - 15)],
                       fill=(15, 23, 42), outline=border_c, width=1)
        draw.text((cx + 25, card_y + card_h - 38), f"AUDIT GATE {i+1}: SIGN-OFF", font=get_font(10, bold=True), fill=border_c)

        if i < len(steps) - 1:
            arrow_x = cx + card_w + 5
            arrow_y = card_y + card_h // 2
            draw.polygon([(arrow_x, arrow_y - 8), (arrow_x + 15, arrow_y), (arrow_x, arrow_y + 8)], fill=CYAN)

    # Lower Section: Three Non-Negotiable Audit Laws of CFD
    rule_y = 610
    draw.rectangle([(45, rule_y), (W - 45, H - 75)], fill=PANEL_BG, outline=PANEL_BORDER, width=2)
    draw.rectangle([(45, rule_y), (W - 45, rule_y + 36)], fill=(20, 26, 38), outline=PANEL_BORDER, width=1)
    draw.text((65, rule_y + 8), "GOVERNING CFD AUDIT LAWS: PREVENTING COLOR-MAP ILLUSIONS", font=get_font(14, bold=True), fill=AMBER)

    laws = [
        ("LAW 1: THE INPUT CEILING TRAP",
         "A simulation that uses server electrical nameplate ratings (e.g. 1500W PSU rating for a 650W server) inflates whitespace thermal heat by 40-60%. The model will predict catastrophic hot spots that do not exist in reality. Always input active feed kW.",
         RED),
        ("LAW 2: MESH CONVERGENCE IS MANDATORY",
         "A pretty color contour generated from a coarse 300,000-cell mesh is a decorative rendering, not a fluid dynamics calculation. Perforated tiles require at least 5-10 cell layers across the tile depth to accurately capture jet separation and pressure drop.",
         CYAN),
        ("LAW 3: CALIBRATION IS NAMED PARAMETERS",
         "Tuning a CFD model does not mean adjusting artificial 'multiplier factors' until the plot matches a thermometer. Valid calibration consists exclusively of verifying physical inputs you can touch: a missing blanking panel, an open containment door, or a blocked grille.",
         GREEN)
    ]

    law_w = 540
    for j, (ltitle, ldesc, lcol) in enumerate(laws):
        lx = 65 + j * (law_w + 20)
        ly = rule_y + 55
        draw.rectangle([(lx, ly), (lx + law_w, ly + 310)], fill=(18, 22, 32), outline=lcol, width=1)
        draw.rectangle([(lx, ly), (lx + law_w, ly + 34)], fill=(26, 32, 44), outline=lcol, width=1)
        draw.text((lx + 12, ly + 8), ltitle, font=get_font(13, bold=True), fill=lcol)

        words = ldesc.split()
        line = ""
        ty = ly + 48
        for w in words:
            test_line = line + " " + w if line else w
            if draw.textlength(test_line, font=get_font(12)) < (law_w - 30):
                line = test_line
            else:
                draw.text((lx + 12, ty), line, font=get_font(12), fill=TEXT_MAIN)
                ty += 24
                line = w
        if line:
            draw.text((lx + 12, ty), line, font=get_font(12), fill=TEXT_MAIN)

    save_path = FIG_DIR / "fig-01-cfd-audit-lifecycle.png"
    img.save(save_path, "PNG")
    print(f"Saved: {save_path}")

# ==============================================================================
# DIAGRAM 2: Underfloor Plenum Pressure Dynamics & Tile Discharge Profile
# ==============================================================================
def draw_fig_02():
    img, draw = create_base_canvas(
        title="Underfloor Plenum Pressure Dynamics & Static Pressure Regain",
        subtitle="High-Velocity CRAH Discharge Jet vs. Momentum Recovery Effect along a 20-Meter Cold Aisle",
        sheet_ref="SHEET 1 (PLENUM CALIBRATION)"
    )

    # Upper Half: Physical Elevation Diagram of Raised Floor & CRAH
    elev_x0, elev_y0 = 60, 150
    elev_w, elev_h = 1680, 420
    draw.rectangle([(elev_x0, elev_y0), (elev_x0 + elev_w, elev_y0 + elev_h)], fill=(16, 20, 28), outline=PANEL_BORDER, width=2)
    draw.rectangle([(elev_x0, elev_y0), (elev_x0 + elev_w, elev_y0 + 32)], fill=(20, 26, 38), outline=PANEL_BORDER, width=1)
    draw.text((elev_x0 + 15, elev_y0 + 8), "CROSS-SECTIONAL ELEVATION: CRAH DISCHARGE INTO RAISED FLOOR VOID (DEPTH: 800mm)", font=get_font(12, bold=True), fill=CYAN)

    # Raised Floor Line
    rf_y = elev_y0 + 260
    draw.line([(elev_x0, rf_y), (elev_x0 + elev_w, rf_y)], fill=PANEL_BORDER, width=3) # Floor tiles
    # Subfloor Slab
    slab_y = elev_y0 + elev_h - 20
    draw.line([(elev_x0, slab_y), (elev_x0 + elev_w, slab_y)], fill=(80, 90, 105), width=6)
    draw.text((elev_x0 + 20, slab_y - 25), "Concrete Subfloor Slab", font=get_font(11), fill=TEXT_MUTED)

    # CRAH Unit on Left
    crah_w = 180
    draw.rectangle([(elev_x0 + 20, elev_y0 + 50), (elev_x0 + 20 + crah_w, rf_y)], fill=(26, 36, 52), outline=BLUE, width=3)
    draw.text((elev_x0 + 40, elev_y0 + 120), "CRAH-01", font=get_font(18, bold=True), fill=TEXT_MAIN)
    draw.text((elev_x0 + 35, elev_y0 + 150), "Downflow EC Fan", font=get_font(11), fill=CYAN)
    draw.text((elev_x0 + 45, elev_y0 + 175), "150 kW / 12 m³/s", font=get_font(11), fill=TEXT_MUTED)

    # Discharge jet into plenum (under floor)
    jet_y0 = rf_y + 10
    draw.polygon([(elev_x0 + 20 + crah_w // 2, rf_y), (elev_x0 + 300, slab_y - 10), (elev_x0 + 100, slab_y - 10)], fill=(20, 45, 80))
    # Flow velocity arrows (Blue)
    for ax in range(elev_x0 + 120, elev_x0 + 700, 100):
        draw.line([(ax, slab_y - 45), (ax + 70, slab_y - 45)], fill=BLUE, width=3)
        draw.polygon([(ax + 70, slab_y - 50), (ax + 85, slab_y - 45), (ax + 70, slab_y - 40)], fill=BLUE)
    draw.text((elev_x0 + 280, slab_y - 75), "High-Velocity Discharge Jet (V > 5.5 m/s) -> Low Static Pressure", font=get_font(11, bold=True), fill=AMBER)

    # Perforated Tiles along the raised floor
    tile_w = 80
    gap_tile = 60
    n_tiles = 10
    start_tile_x = elev_x0 + 260

    # Draw cold aisle racks above the tiles
    for t_idx in range(n_tiles):
        tx = start_tile_x + t_idx * (tile_w + gap_tile)
        # Perforated tile symbol (dashed)
        draw.rectangle([(tx, rf_y - 4), (tx + tile_w, rf_y + 4)], fill=CYAN, outline=TEXT_MAIN, width=1)
        draw.text((tx + 10, rf_y - 20), f"TILE {t_idx+1}", font=get_font(9, bold=True), fill=CYAN)

        # Flow vectors rising through tiles
        # Near CRAH: low flow or negative induction!
        # Far from CRAH: high flow due to static pressure regain!
        if t_idx < 2:
            # Low flow or vortex induction
            draw.line([(tx + tile_w // 2, rf_y - 5), (tx + tile_w // 2, rf_y - 45)], fill=AMBER, width=2)
            draw.text((tx - 5, rf_y - 60), "180 L/s", font=get_font(10, bold=True), fill=AMBER)
        elif t_idx < 7:
            # Medium flow
            draw.line([(tx + tile_w // 2, rf_y - 5), (tx + tile_w // 2, rf_y - 85)], fill=CYAN, width=3)
            draw.text((tx - 5, rf_y - 100), f"{320 + t_idx*30} L/s", font=get_font(10, bold=True), fill=CYAN)
        else:
            # High flow at dead-end
            draw.line([(tx + tile_w // 2, rf_y - 5), (tx + tile_w // 2, rf_y - 120)], fill=GREEN, width=4)
            draw.text((tx - 5, rf_y - 135), f"{540 + (t_idx-7)*40} L/s", font=get_font(10, bold=True), fill=GREEN)

    # Plenum Dead-End Wall on right
    draw.rectangle([(elev_x0 + elev_w - 30, elev_y0 + 50), (elev_x0 + elev_w, slab_y)], fill=(50, 60, 75))
    draw.text((elev_x0 + elev_w - 180, slab_y - 60), "Plenum End Wall", font=get_font(11, bold=True), fill=TEXT_MUTED)

    # Lower Half: Graph of Static Pressure vs Dynamic Velocity
    graph_y0 = 600
    graph_h = 420
    draw.rectangle([(elev_x0, graph_y0), (elev_x0 + elev_w, graph_y0 + graph_h)], fill=(16, 20, 28), outline=PANEL_BORDER, width=2)
    draw.rectangle([(elev_x0, graph_y0), (elev_x0 + elev_w, graph_y0 + 32)], fill=(20, 26, 38), outline=PANEL_BORDER, width=1)
    draw.text((elev_x0 + 15, graph_y0 + 8), "UNDERFLOOR STATIC PRESSURE (Pa) & VELOCITY (m/s) ALONG PLENUM AXIS", font=get_font(12, bold=True), fill=CYAN)

    gx0, gy0 = elev_x0 + 80, graph_y0 + 60
    gw, gh = elev_w - 160, graph_h - 100
    gx1, gy1 = gx0 + gw, gy0 + gh

    # Grid lines
    for i in range(1, 11):
        x = gx0 + int(i * gw / 10)
        draw.line([(x, gy0), (x, gy1)], fill=(28, 35, 48), width=1)
        draw.text((x - 15, gy1 + 10), f"{i * 2}m", font=get_font(10), fill=TEXT_MUTED)

    # Y-axis (Pressure: -10 Pa to +45 Pa)
    for p_val in range(-10, 50, 10):
        y = gy1 - int(((p_val + 10) / 55) * gh)
        draw.line([(gx0, y), (gx1, y)], fill=(28, 35, 48), width=1)
        draw.text((gx0 - 45, y - 6), f"{p_val}Pa", font=get_font(10), fill=CYAN)

    # Zero pressure reference line
    zero_y = gy1 - int((10 / 55) * gh)
    draw.line([(gx0, zero_y), (gx1, zero_y)], fill=(70, 80, 95), width=2)

    # Plot 1: Static Pressure Curve (Ascending due to Bernoulli regain: P_s = P_tot - 0.5 * rho * v^2)
    pts_static_p = []
    for d_step in range(0, 101):
        dist = d_step / 100.0 * 20.0 # meters
        # Low pressure near CRAH (4 Pa), rising to 38 Pa at dead end
        p_stat = 4.0 + 34.0 * (1.0 - math.exp(-dist / 6.0))
        px = gx0 + int((dist / 20.0) * gw)
        py = gy1 - int(((p_stat + 10) / 55) * gh)
        pts_static_p.append((px, py))
    draw.line(pts_static_p, fill=CYAN, width=4)
    draw.text((gx0 + int(0.7 * gw), gy1 - int((36 + 10)/55 * gh) - 20), "Static Pressure P_stat (Bernoulli Regain)", font=get_font(12, bold=True), fill=CYAN)

    # Plot 2: Velocity Curve (Decaying from 6.0 m/s to 0.5 m/s)
    pts_vel = []
    for d_step in range(0, 101):
        dist = d_step / 100.0 * 20.0
        v = 6.0 * math.exp(-dist / 7.0) # m/s
        # Scale to match graph display
        py = gy1 - int(((v * 6.5 + 10) / 55) * gh)
        px = gx0 + int((dist / 20.0) * gw)
        pts_vel.append((px, py))
    draw.line(pts_vel, fill=AMBER, width=3)
    draw.text((gx0 + 80, gy1 - int((40 + 10)/55 * gh)), "Plenum Jet Velocity V (m/s)", font=get_font(11, bold=True), fill=AMBER)

    # Callout Annotation on Left: Jet Entrainment
    draw.rectangle([(gx0 + 30, zero_y - 70), (gx0 + 260, zero_y - 15)], fill=(30, 20, 25), outline=RED, width=1)
    draw.text((gx0 + 40, zero_y - 62), "HIGH JET VELOCITY ZONE", font=get_font(10, bold=True), fill=RED)
    draw.text((gx0 + 40, zero_y - 45), "Bernoulli effect depresses static P;", font=get_font(9), fill=TEXT_MUTED)
    draw.text((gx0 + 40, zero_y - 30), "Risk of hot air suction through tile!", font=get_font(9), fill=TEXT_MUTED)

    # Callout Annotation on Right: Static Regain
    draw.rectangle([(gx1 - 280, gy0 + 40), (gx1 - 30, gy0 + 105)], fill=(20, 32, 25), outline=GREEN, width=1)
    draw.text((gx1 - 270, gy0 + 50), "STATIC MOMENTUM REGAIN", font=get_font(10, bold=True), fill=GREEN)
    draw.text((gx1 - 270, gy0 + 68), "Jet decelerates against end wall;", font=get_font(9), fill=TEXT_MUTED)
    draw.text((gx1 - 270, gy0 + 84), "Static head drives maximum airflow.", font=get_font(9), fill=TEXT_MUTED)

    save_path = FIG_DIR / "fig-02-underfloor-plenum-hydraulics.png"
    img.save(save_path, "PNG")
    print(f"Saved: {save_path}")

# ==============================================================================
# DIAGRAM 3: Aisle Containment Leakage Aerodynamics
# ==============================================================================
def draw_fig_03():
    img, draw = create_base_canvas(
        title="Aisle Containment Aerodynamics & Parasitic Leakage Paths",
        subtitle="Hot Air Recirculation Mechanics: Missing Blanking Panels, Brush Grommets, and Door Deflections",
        sheet_ref="SHEET 1 & SHEET 2"
    )

    # Two Main Panels: Left = Cold Aisle Containment (CAC), Right = Hot Aisle Containment (HAC)
    pw = 810
    ph = 860
    py = 150

    # LEFT PANEL: Cold Aisle Containment (CAC)
    draw.rectangle([(50, py), (50 + pw, py + ph)], fill=PANEL_BG, outline=CYAN, width=2)
    draw.rectangle([(50, py), (50 + pw, py + 34)], fill=(16, 30, 48), outline=CYAN, width=1)
    draw.text((70, py + 8), "SYSTEM A: COLD AISLE CONTAINMENT (CAC) WITH DEFECT AUDIT", font=get_font(13, bold=True), fill=CYAN)

    # Diagram of CAC
    cx0, cy0 = 90, py + 60
    # Left Rack Row
    draw.rectangle([(cx0, cy0 + 60), (cx0 + 160, cy0 + 520)], fill=(20, 26, 38), outline=BLUE, width=2)
    draw.text((cx0 + 35, cy0 + 140), "ROW A (RACKS)", font=get_font(13, bold=True), fill=TEXT_MAIN)
    # Right Rack Row
    draw.rectangle([(cx0 + 440, cy0 + 60), (cx0 + 600, cy0 + 520)], fill=(20, 26, 38), outline=BLUE, width=2)
    draw.text((cx0 + 475, cy0 + 140), "ROW B (RACKS)", font=get_font(13, bold=True), fill=TEXT_MAIN)

    # Cold Aisle in middle
    ca_x0, ca_x1 = cx0 + 160, cx0 + 440
    draw.rectangle([(ca_x0, cy0 + 60), (ca_x1, cy0 + 520)], fill=(15, 28, 45), outline=CYAN, width=1)
    draw.text((ca_x0 + 55, cy0 + 100), "ENCLOSED COLD AISLE", font=get_font(14, bold=True), fill=CYAN)
    draw.text((ca_x0 + 75, cy0 + 130), "T_sup = 20.0°C", font=get_font(12, bold=True), fill=CYAN)

    # Ceiling Containment Roof
    draw.rectangle([(ca_x0, cy0 + 45), (ca_x1, cy0 + 60)], fill=(40, 55, 75), outline=CYAN, width=2)
    draw.text((ca_x0 + 85, cy0 + 25), "Clear Ceiling Roof Panels", font=get_font(10), fill=TEXT_MUTED)

    # DEFECT 1: Missing Blanking Panel on Row A
    draw.rectangle([(cx0 + 140, cy0 + 240), (cx0 + 160, cy0 + 290)], fill=RED, outline=TEXT_MAIN, width=2)
    # Hot air backflow arrow
    draw.polygon([(cx0 + 190, cy0 + 265), (cx0 + 150, cy0 + 260), (cx0 + 150, cy0 + 270)], fill=RED)
    draw.line([(cx0 + 120, cy0 + 265), (cx0 + 220, cy0 + 265)], fill=RED, width=3)
    draw.text((ca_x0 + 25, cy0 + 250), "HOT RECIRCULATION", font=get_font(11, bold=True), fill=RED)
    draw.text((ca_x0 + 25, cy0 + 270), "Missing 1U blank: 25 L/s bypass!", font=get_font(10), fill=AMBER)

    # DEFECT 2: Unsealed Floor Cutout under Row B
    draw.rectangle([(cx0 + 440, cy0 + 500), (cx0 + 520, cy0 + 520)], fill=AMBER, outline=RED, width=2)
    draw.line([(cx0 + 480, cy0 + 540), (cx0 + 480, cy0 + 480)], fill=CYAN, width=3)
    draw.polygon([(cx0 + 475, cy0 + 480), (cx0 + 480, cy0 + 465), (cx0 + 485, cy0 + 480)], fill=CYAN)
    draw.text((cx0 + 420, cy0 + 550), "Unsealed Cable Penetration (Air Short-Circuit)", font=get_font(10, bold=True), fill=AMBER)

    # Bottom notes for CAC
    draw.rectangle([(70, py + ph - 220), (50 + pw - 20, py + ph - 20)], fill=(18, 24, 34), outline=PANEL_BORDER, width=1)
    draw.text((85, py + ph - 205), "CAC AUDIT VERIFICATION RULES:", font=get_font(12, bold=True), fill=TEXT_MAIN)
    draw.text((85, py + ph - 175), "• Aisle Pressure Balance: Delta-P across door must stay within +2.0 to +5.0 Pa.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((85, py + ph - 150), "• Negative Aisle Pressure Warning: If server fans exceed tile flow, cold aisle goes", font=get_font(11), fill=AMBER)
    draw.text((85, py + ph - 130), "  negative, pulling hot room air backward through any unsealed seam.", font=get_font(11), fill=AMBER)
    draw.text((85, py + ph - 105), "• 100% Blanking Panel Mandate: Every empty 'U' space must have sealed blanking.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((85, py + ph - 80), "• Brush Grommets: Mandatory on all underfloor cable penetrations.", font=get_font(11), fill=TEXT_MUTED)

    # RIGHT PANEL: Hot Aisle Containment (HAC)
    rx0 = 940
    draw.rectangle([(rx0, py), (rx0 + pw, py + ph)], fill=PANEL_BG, outline=RED, width=2)
    draw.rectangle([(rx0, py), (rx0 + pw, py + 34)], fill=(35, 18, 24), outline=RED, width=1)
    draw.text((rx0 + 20, py + 8), "SYSTEM B: HOT AISLE CONTAINMENT (HAC) WITH CHIMNEY EXHAUST", font=get_font(13, bold=True), fill=RED)

    # Diagram of HAC
    hx0, hy0 = rx0 + 40, py + 60
    # Left Rack Row
    draw.rectangle([(hx0, hy0 + 60), (hx0 + 160, hy0 + 520)], fill=(20, 26, 38), outline=BLUE, width=2)
    draw.text((hx0 + 35, hy0 + 140), "ROW A (RACKS)", font=get_font(13, bold=True), fill=TEXT_MAIN)
    # Right Rack Row
    draw.rectangle([(hx0 + 440, hy0 + 60), (hx0 + 600, hy0 + 520)], fill=(20, 26, 38), outline=BLUE, width=2)
    draw.text((hx0 + 475, hy0 + 140), "ROW B (RACKS)", font=get_font(13, bold=True), fill=TEXT_MAIN)

    # Hot Aisle in middle
    ha_x0, ha_x1 = hx0 + 160, hx0 + 440
    draw.rectangle([(ha_x0, hy0 + 60), (ha_x1, hy0 + 520)], fill=(45, 18, 22), outline=RED, width=1)
    draw.text((ha_x0 + 65, hy0 + 100), "ENCLOSED HOT AISLE", font=get_font(14, bold=True), fill=RED)
    draw.text((ha_x0 + 80, hy0 + 130), "T_exh = 38.0°C", font=get_font(12, bold=True), fill=RED)

    # Overhead Plafond / Chimney Return to Ceiling Plenum
    draw.rectangle([(ha_x0 + 40, hy0 - 30), (ha_x1 - 40, hy0 + 60)], fill=(55, 25, 30), outline=AMBER, width=2)
    draw.text((ha_x0 + 60, hy0 - 15), "Exhaust Chimney -> Ceiling", font=get_font(10, bold=True), fill=AMBER)
    # Upward hot exhaust arrows
    for ax in [ha_x0 + 80, ha_x0 + 140, ha_x0 + 200]:
        draw.line([(ax, hy0 + 240), (ax, hy0)], fill=RED, width=3)
        draw.polygon([(ax - 6, hy0 + 15), (ax, hy0), (ax + 6, hy0 + 15)], fill=RED)

    # Entire room outside is flooded with cold supply air!
    draw.text((hx0 - 10, hy0 + 320), "Cold Room Air", font=get_font(11, bold=True), fill=CYAN)
    draw.text((hx0 - 10, hy0 + 340), "22.0°C Whitespace", font=get_font(10), fill=TEXT_MUTED)

    draw.text((hx0 + 610, hy0 + 320), "Cold Room Air", font=get_font(11, bold=True), fill=CYAN)
    draw.text((hx0 + 610, hy0 + 340), "22.0°C Whitespace", font=get_font(10), fill=TEXT_MUTED)

    # Bottom notes for HAC
    draw.rectangle([(rx0 + 20, py + ph - 220), (rx0 + pw - 20, py + ph - 20)], fill=(18, 24, 34), outline=PANEL_BORDER, width=1)
    draw.text((rx0 + 35, py + ph - 205), "HAC AUDIT VERIFICATION RULES:", font=get_font(12, bold=True), fill=TEXT_MAIN)
    draw.text((rx0 + 35, py + ph - 175), "• Chimney Air Velocity: Exhaust velocity should be maintained between 2.0 - 3.5 m/s.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((rx0 + 35, py + ph - 150), "• Whitespace Working Comfort: Technicians work in cold space (22°C), improving safety.", font=get_font(11), fill=GREEN)
    draw.text((rx0 + 35, py + ph - 125), "• Containment Leakage Direction: Any door leak pushes COLD air INTO hot aisle,", font=get_font(11), fill=TEXT_MUTED)
    draw.text((rx0 + 35, py + ph - 105), "  preventing hot air from spilling into the room (thermal containment fail-safe).", font=get_font(11), fill=TEXT_MUTED)
    draw.text((rx0 + 35, py + ph - 80), "• CFD Modeling Rule: Model must explicitly include ceiling plenum return ducting.", font=get_font(11), fill=AMBER)

    save_path = FIG_DIR / "fig-03-containment-leakage-aerodynamics.png"
    img.save(save_path, "PNG")
    print(f"Saved: {save_path}")

# ==============================================================================
# DIAGRAM 4: Hybrid Liquid/Air Thermal Energy Split in High-Density AI Halls
# ==============================================================================
def draw_fig_04():
    img, draw = create_base_canvas(
        title="Hybrid Liquid-Cooled AI Hall: Thermal Energy Split & Air Convection",
        subtitle="120 kW NVL72/GB200 Footprint: 80% Direct-to-Chip Liquid vs. 20% Residual Air Heat Rejection",
        sheet_ref="SHEET 2 & CHAPTER 4"
    )

    # Center Rack Representation (NVL72 Footprint)
    rack_x = 720
    rack_y = 180
    rack_w = 360
    rack_h = 560

    draw.rectangle([(rack_x, rack_y), (rack_x + rack_w, rack_y + rack_h)], fill=(22, 28, 40), outline=CYAN, width=3)
    draw.rectangle([(rack_x, rack_y), (rack_x + rack_w, rack_y + 40)], fill=(16, 22, 32), outline=CYAN, width=1)
    draw.text((rack_x + 35, rack_y + 12), "120 kW HIGH-DENSITY AI RACK", font=get_font(14, bold=True), fill=TEXT_MAIN)

    # Internal Rack Components
    draw.rectangle([(rack_x + 20, rack_y + 60), (rack_x + rack_w - 20, rack_y + 240)], fill=(15, 35, 55), outline=CYAN, width=2)
    draw.text((rack_x + 35, rack_y + 75), "COMPUTE TRAY ARRAY (72 GPUs / 36 CPUs)", font=get_font(11, bold=True), fill=CYAN)
    draw.text((rack_x + 35, rack_y + 105), "• Direct-to-Chip Cold Plates (Copper / Microchannel)", font=get_font(10), fill=TEXT_MAIN)
    draw.text((rack_x + 35, rack_y + 130), "• Liquid-Cooled Silicon Load: 96.0 kW (80.0%)", font=get_font(12, bold=True), fill=GREEN)
    draw.text((rack_x + 35, rack_y + 160), "• Coolant: 25% Propylene Glycol @ 100 LPM", font=get_font(10), fill=TEXT_MUTED)

    draw.rectangle([(rack_x + 20, rack_y + 260), (rack_x + rack_w - 20, rack_y + 420)], fill=(45, 25, 20), outline=AMBER, width=2)
    draw.text((rack_x + 35, rack_y + 275), "AIR-COOLED SUBSYSTEMS & ANCILLARY LOAD", font=get_font(11, bold=True), fill=AMBER)
    draw.text((rack_x + 35, rack_y + 305), "• Optical Transceivers (OSFP) & High-Speed PCIe Fabric", font=get_font(10), fill=TEXT_MAIN)
    draw.text((rack_x + 35, rack_y + 330), "• 48V Power Supply Units (PSUs) & Voltage Regulators", font=get_font(10), fill=TEXT_MAIN)
    draw.text((rack_x + 35, rack_y + 355), "• Convective Air Heat Release: 24.0 kW (20.0%)", font=get_font(12, bold=True), fill=RED)
    draw.text((rack_x + 35, rack_y + 385), "• Internal Airflow Demand: 1400 CFM (660 L/s)", font=get_font(10), fill=TEXT_MUTED)

    # Bottom Cable & Manifold Entrance
    draw.rectangle([(rack_x + 20, rack_y + 440), (rack_x + rack_w - 20, rack_y + 530)], fill=(20, 26, 36), outline=PANEL_BORDER, width=1)
    draw.text((rack_x + 35, rack_y + 460), "Secondary Quick-Disconnect Manifold (DN38)", font=get_font(10), fill=TEXT_MUTED)
    draw.text((rack_x + 35, rack_y + 485), "3-Phase 415V Dual 100A Busway Feeders", font=get_font(10), fill=TEXT_MUTED)

    # LEFT PATH: Secondary Liquid Cooling Path (80% / 96 kW)
    liq_x = 120
    liq_y = 260
    draw.rectangle([(liq_x, liq_y), (liq_x + 420, liq_y + 320)], fill=(16, 26, 40), outline=CYAN, width=2)
    draw.rectangle([(liq_x, liq_y), (liq_x + 420, liq_y + 36)], fill=(20, 35, 55), outline=CYAN, width=1)
    draw.text((liq_x + 15, liq_y + 10), "PRIMARY HEAT EXTRACTION PATH (LIQUID)", font=get_font(12, bold=True), fill=CYAN)
    draw.text((liq_x + 20, liq_y + 55), "COOLANT DISTRIBUTION UNIT (CDU)", font=get_font(14, bold=True), fill=TEXT_MAIN)
    draw.text((liq_x + 20, liq_y + 85), "• Heat Duty: 96.0 kW per rack (1.2 MW Row Total)", font=get_font(11, bold=True), fill=GREEN)
    draw.text((liq_x + 20, liq_y + 115), "• Supply Temp: 40.0°C // Return Temp: 50.0°C", font=get_font(11), fill=TEXT_MAIN)
    draw.text((liq_x + 20, liq_y + 145), "• Flow: 1.67 L/s (100 LPM) per rack", font=get_font(11), fill=TEXT_MAIN)
    draw.text((liq_x + 20, liq_y + 175), "• Rejected directly to primary cooling tower / FWS", font=get_font(11), fill=TEXT_MUTED)
    draw.text((liq_x + 20, liq_y + 205), "• Verified under Book 03 Verification Protocol", font=get_font(11, bold=True), fill=AMBER)

    # Pipe Arrow connecting rack to CDU (Liquid Supply & Return)
    draw.line([(rack_x, rack_y + 150), (liq_x + 420, liq_y + 150)], fill=CYAN, width=5)
    draw.polygon([(liq_x + 420 + 20, liq_y + 142), (liq_x + 420, liq_y + 150), (liq_x + 420 + 20, liq_y + 158)], fill=CYAN)
    draw.text((liq_x + 460, liq_y + 125), "96.0 kW Liquid", font=get_font(11, bold=True), fill=CYAN)

    # RIGHT PATH: Residual Air Convection Path (20% / 24 kW)
    air_x = 1260
    air_y = 260
    draw.rectangle([(air_x, air_y), (air_x + 420, air_y + 320)], fill=(32, 20, 24), outline=RED, width=2)
    draw.rectangle([(air_x, air_y), (air_x + 420, air_y + 36)], fill=(45, 20, 28), outline=RED, width=1)
    draw.text((air_x + 15, air_y + 10), "RESIDUAL HEAT REJECTION PATH (AIR CFD)", font=get_font(12, bold=True), fill=RED)
    draw.text((air_x + 20, air_y + 55), "CRAH UNITS / FAN WALL ARRAYS", font=get_font(14, bold=True), fill=TEXT_MAIN)
    draw.text((air_x + 20, air_y + 85), "• Heat Duty: 24.0 kW per rack (240 kW Row Total)", font=get_font(11, bold=True), fill=RED)
    draw.text((air_x + 20, air_y + 115), "• Exhaust Air Temp: 42.0°C to 48.0°C", font=get_font(11), fill=TEXT_MAIN)
    draw.text((air_x + 20, air_y + 145), "• Whitespace Supply Air Temp: 22.0°C", font=get_font(11), fill=TEXT_MAIN)
    draw.text((air_x + 20, air_y + 175), "• Governs thermal comfort & optical transceiver life", font=get_font(11), fill=TEXT_MUTED)
    draw.text((air_x + 20, air_y + 205), "• PRIMARY GOVERNING SCOPE OF BOOK 04 CFD", font=get_font(11, bold=True), fill=CYAN)

    # Air Plume Arrow connecting rack to CRAH
    draw.line([(rack_x + rack_w, rack_y + 340), (air_x, air_y + 150)], fill=RED, width=5)
    draw.polygon([(air_x - 20, air_y + 142), (air_x, air_y + 150), (air_x - 20, air_y + 158)], fill=RED)
    draw.text((rack_x + rack_w + 35, rack_y + 315), "24.0 kW Air Exhaust", font=get_font(11, bold=True), fill=RED)

    # Bottom Callout: The Critical Engineering Warning
    draw.rectangle([(120, H - 280), (W - 120, H - 75)], fill=(15, 23, 42), outline=AMBER, width=2)
    draw.rectangle([(120, H - 280), (W - 120, H - 245)], fill=(28, 35, 48), outline=AMBER, width=1)
    draw.text((140, H - 268), "CRITICAL CFD AUDIT TRAP: THE 'ZERO AIR HEAT' FALLACY IN LIQUID DATA HALLS", font=get_font(13, bold=True), fill=AMBER)

    draw.text((140, H - 225),
              "1. Modern marketing literature often promotes '100% liquid-cooled racks.' In reality, no commercial AI compute architecture is 100% liquid-cooled.",
              font=get_font(11, bold=True), fill=TEXT_MAIN)
    draw.text((140, H - 200),
              "2. For a 10-rack NVL72 cluster, the 20% residual convective heat totals 240 kW—the heat equivalent of 40 standard enterprise server racks!",
              font=get_font(11), fill=TEXT_MUTED)
    draw.text((140, H - 175),
              "3. If a CFD model omits this 24 kW/rack air load, it will predict freezing cold aisles. In the physical room, optical transceivers rated for 70°C",
              font=get_font(11), fill=TEXT_MUTED)
    draw.text((140, H - 150),
              "   will heat-soak at 85°C+, causing link degradation and silent data corruption. A CFD report for a liquid hall that omits air heat must be REJECTED.",
              font=get_font(11, bold=True), fill=RED)

    save_path = FIG_DIR / "fig-04-hybrid-liquid-air-thermal-split.png"
    img.save(save_path, "PNG")
    print(f"Saved: {save_path}")

# ==============================================================================
# DIAGRAM 5: Multi-Point Physical Field Benchmarking Protocol
# ==============================================================================
def draw_fig_05():
    img, draw = create_base_canvas(
        title="Physical Field Benchmarking Protocol & Measurement Planes",
        subtitle="Standardized Sensor Topology: Supply Opening 2-Point, Return 3-Point, and 3-Tier Rack Probe Trees",
        sheet_ref="SHEET 1 (MEASUREMENT)"
    )

    # Left Section: CRAH Unit Measurement Planes
    crah_x = 80
    crah_y = 160
    crah_w = 480
    crah_h = 560
    draw.rectangle([(crah_x, crah_y), (crah_x + crah_w, crah_y + crah_h)], fill=PANEL_BG, outline=BLUE, width=2)
    draw.rectangle([(crah_x, crah_y), (crah_x + crah_w, crah_y + 34)], fill=(20, 28, 45), outline=BLUE, width=1)
    draw.text((crah_x + 15, crah_y + 8), "COOLING UNIT (CRAH) MEASUREMENT PLANES", font=get_font(12, bold=True), fill=BLUE)

    # Draw CRAH Unit Elevation
    draw.rectangle([(crah_x + 60, crah_y + 80), (crah_x + 420, crah_y + 460)], fill=(18, 22, 32), outline=TEXT_MUTED, width=2)
    draw.text((crah_x + 180, crah_y + 240), "CRAH UNIT", font=get_font(16, bold=True), fill=TEXT_MUTED)

    # Return Air Opening (Top)
    ret_y = crah_y + 80
    draw.rectangle([(crah_x + 90, ret_y), (crah_x + 390, ret_y + 40)], fill=(40, 20, 25), outline=RED, width=2)
    draw.text((crah_x + 130, ret_y - 25), "Top Return Air Grille (3 Points)", font=get_font(11, bold=True), fill=RED)

    # 3 Points on Return
    for idx, rx in enumerate([crah_x + 130, crah_x + 240, crah_x + 350], 1):
        draw.ellipse([(rx - 10, ret_y + 10), (rx + 10, ret_y + 30)], fill=RED, outline=TEXT_MAIN, width=2)
        draw.text((rx - 6, ret_y + 12), f"R{idx}", font=get_font(10, bold=True), fill=TEXT_MAIN)
    draw.text((crah_x + 80, ret_y + 50), "Average = (R1 + R2 + R3) / 3 [Strictly at opening]", font=get_font(10), fill=TEXT_MUTED)

    # Supply Air Opening (Bottom / Discharge)
    sup_y = crah_y + 420
    draw.rectangle([(crah_x + 90, sup_y), (crah_x + 390, sup_y + 40)], fill=(15, 35, 55), outline=CYAN, width=2)
    draw.text((crah_x + 120, sup_y + 55), "Downflow Discharge (At least 2 Points)", font=get_font(11, bold=True), fill=CYAN)

    # 2 Points on Supply
    for idx, sx in enumerate([crah_x + 170, crah_x + 310], 1):
        draw.ellipse([(sx - 10, sup_y + 10), (sx + 10, sup_y + 30)], fill=CYAN, outline=TEXT_MAIN, width=2)
        draw.text((sx - 6, sup_y + 12), f"S{idx}", font=get_font(10, bold=True), fill=TEXT_MAIN)
    draw.text((crah_x + 80, sup_y + 85), "Average = (S1 + S2) / 2 [Never in open aisle]", font=get_font(10), fill=TEXT_MUTED)

    # Right Section: Server Cabinet 3-Tier Probe Tree
    cab_x = 640
    cab_y = 160
    cab_w = 540
    cab_h = 560
    draw.rectangle([(cab_x, cab_y), (cab_x + cab_w, cab_y + cab_h)], fill=PANEL_BG, outline=CYAN, width=2)
    draw.rectangle([(cab_x, cab_y), (cab_x + cab_w, cab_y + 34)], fill=(16, 32, 45), outline=CYAN, width=1)
    draw.text((cab_x + 15, cab_y + 8), "SERVER CABINET INLET & EXHAUST PROBE TREES", font=get_font(12, bold=True), fill=CYAN)

    # Cabinet Frame (48U / 2.2m)
    draw.rectangle([(cab_x + 160, cab_y + 70), (cab_x + 380, cab_y + 500)], fill=(18, 24, 34), outline=TEXT_MAIN, width=2)
    draw.text((cab_x + 220, cab_y + 270), "48U RACK", font=get_font(16, bold=True), fill=TEXT_MUTED)

    # 3-Tier Inlets on Left (Front Door / Cold Aisle)
    tiers = [
        ("TOP (1.8m / ~42U)", cab_y + 120, "T3 (Risk: Hot air recirculation cap)"),
        ("MID (1.2m / ~24U)", cab_y + 270, "T2 (Reference core inlet)"),
        ("BOT (0.3m / ~06U)", cab_y + 440, "T1 (Risk: Floor jet entrainment)")
    ]

    for label, ty, desc in tiers:
        # Inlet Probe (Front)
        draw.ellipse([(cab_x + 140, ty - 10), (cab_x + 160, ty + 10)], fill=CYAN, outline=TEXT_MAIN, width=2)
        draw.text((cab_x + 25, ty - 6), label, font=get_font(10, bold=True), fill=CYAN)
        draw.line([(cab_x + 130, ty), (cab_x + 140, ty)], fill=CYAN, width=2)

        # Exhaust Probe (Back)
        draw.ellipse([(cab_x + 380, ty - 10), (cab_x + 400, ty + 10)], fill=RED, outline=TEXT_MAIN, width=2)
        draw.text((cab_x + 415, ty - 6), "EXH", font=get_font(10, bold=True), fill=RED)

    draw.text((cab_x + 40, cab_y + 520), "ASHRAE TC 9.9 3-Point Inlet Tree: Validates stratification & capture.", font=get_font(10, bold=True), fill=TEXT_MUTED)

    # Far Right: Statistical Calibration Pass/Fail Criteria
    cal_x = 1240
    cal_y = 160
    cal_w = 480
    cal_h = 560
    draw.rectangle([(cal_x, cal_y), (cal_x + cal_w, cal_y + cal_h)], fill=PANEL_BG, outline=GREEN, width=2)
    draw.rectangle([(cal_x, cal_y), (cal_x + cal_w, cal_y + 34)], fill=(16, 32, 24), outline=GREEN, width=1)
    draw.text((cal_x + 15, cal_y + 8), "ASME V&V 20 BENCHMARK METRICS", font=get_font(12, bold=True), fill=GREEN)

    metrics = [
        ("MEAN ABSOLUTE ERROR (MAE)", "MAE = (1/N) * SUM |T_sim - T_meas|\nAcceptance Standard: MAE <= 1.0 K", GREEN),
        ("ROOT MEAN SQUARE ERROR (RMSE)", "RMSE = SQRT[ (1/N) * SUM (T_sim - T_meas)^2 ]\nAcceptance Standard: RMSE <= 1.5 K", GREEN),
        ("NORMALISED MEAN BIAS (NMBE)", "NMBE = [ SUM (T_sim - T_meas) / (N * T_mean) ]\nAcceptance Standard: |NMBE| <= 5.0%", GREEN),
        ("LOCAL HOTSPOT ERROR (DELTA_MAX)", "MAX |T_sim - T_meas| across all points\nHard Failure Limit: DELTA_MAX <= 2.5 K", AMBER)
    ]

    my = cal_y + 60
    for m_title, m_desc, m_col in metrics:
        draw.rectangle([(cal_x + 15, my), (cal_x + cal_w - 15, my + 100)], fill=(18, 24, 32), outline=m_col, width=1)
        draw.text((cal_x + 25, my + 10), m_title, font=get_font(11, bold=True), fill=m_col)
        draw.text((cal_x + 25, my + 38), m_desc, font=get_font(10), fill=TEXT_MAIN)
        my += 115

    # Bottom Protocol Summary
    draw.rectangle([(80, H - 280), (W - 80, H - 75)], fill=(15, 23, 42), outline=PANEL_BORDER, width=1)
    draw.text((100, H - 265), "MANDATORY FIELD MEASUREMENT PROTOCOL BEFORE READING CFD COLORS", font=get_font(12, bold=True), fill=CYAN)
    draw.text((100, H - 235), "1. Measurement Date Synchronization: Record physical measurement date next to model layout date. A mixed year is not a calibration.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((100, H - 210), "2. Strict Point Locations: Sensors in model must match physical probe locations. Never compare a cabinet inlet to a room average.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((100, H - 185), "3. Active Power Sourcing: Input active kW from PDU telemetry; never use server nameplate ratings.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((100, H - 160), "4. Correction Rule: If model and measurement disagree, change an input you can physically touch (blanking, grille, unit state) and rerun.", font=get_font(11), fill=AMBER)
    draw.text((100, H - 135), "   If you cannot name a physical input to change, mark the report 'NOT CORRECTED'.", font=get_font(11), fill=AMBER)

    save_path = FIG_DIR / "fig-05-multi-point-field-benchmarking.png"
    img.save(save_path, "PNG")
    print(f"Saved: {save_path}")

# ==============================================================================
# DIAGRAM 6: Data Center Airflow Metrics: SHI, RHI, Capture Index (CI) & ASHRAE
# ==============================================================================
def draw_fig_06():
    img, draw = create_base_canvas(
        title="Airflow Performance Metrics: SHI, RHI, Capture Index & ASHRAE Bands",
        subtitle="Evaluating Cold Air Utilization Efficiency and Compliance against ASHRAE TC 9.9 Thermal Envelopes",
        sheet_ref="SHEET 2 & CHAPTER 4"
    )

    # Left Section: Dimensionless Airflow Indices (SHI, RHI, CI)
    idx_x = 80
    idx_y = 160
    idx_w = 800
    idx_h = 560
    draw.rectangle([(idx_x, idx_y), (idx_x + idx_w, idx_y + idx_h)], fill=PANEL_BG, outline=CYAN, width=2)
    draw.rectangle([(idx_x, idx_y), (idx_x + idx_w, idx_y + 34)], fill=(16, 28, 45), outline=CYAN, width=1)
    draw.text((idx_x + 15, idx_y + 8), "DIMENSIONLESS AIRFLOW INDICES (SHARMA & HERRICK)", font=get_font(13, bold=True), fill=CYAN)

    indices = [
        ("1. SUPPLY HEAT INDEX (SHI)",
         "SHI = (T_in - T_sup) / (T_out - T_sup)\n"
         "Measures the fraction of heat in the rack inlet caused by hot exhaust recirculation.\n"
         "• Perfect isolation (Zero recirculation): SHI = 0.00\n"
         "• Acceptable industry standard: SHI <= 0.15\n"
         "• Defective airflow (Severe recirculation): SHI > 0.30",
         CYAN),
        ("2. RETURN HEAT INDEX (RHI)",
         "RHI = (T_ret - T_sup) / (T_out - T_sup) = 1 - SHI\n"
         "Measures the fraction of rack exhaust heat that successfully reaches cooling unit.\n"
         "• Perfect heat extraction: RHI = 1.00\n"
         "• Target threshold: RHI >= 0.85\n"
         "• Bypassed cooling airflow: RHI < 0.70",
         BLUE),
        ("3. COLD AISLE CAPTURE INDEX (CI)",
         "CI = (Airflow ingested by rack directly from perforated tiles) / (Total rack airflow)\n"
         "• Premium containment: CI >= 90%\n"
         "• Marginal performance: 75% <= CI < 90%\n"
         "• Severe hot air ingestion: CI < 70%",
         GREEN)
    ]

    iy = idx_y + 55
    for i_title, i_body, i_col in indices:
        draw.rectangle([(idx_x + 20, iy), (idx_x + idx_w - 20, iy + 145)], fill=(18, 24, 34), outline=i_col, width=1)
        draw.text((idx_x + 35, iy + 10), i_title, font=get_font(12, bold=True), fill=i_col)
        draw.text((idx_x + 35, iy + 35), i_body, font=get_font(10), fill=TEXT_MAIN)
        iy += 160

    # Right Section: ASHRAE TC 9.9 Thermal Envelopes
    ash_x = 920
    ash_y = 160
    ash_w = 800
    ash_h = 560
    draw.rectangle([(ash_x, ash_y), (ash_x + ash_w, ash_y + ash_h)], fill=PANEL_BG, outline=GREEN, width=2)
    draw.rectangle([(ash_x, ash_y), (ash_x + ash_w, ash_y + 34)], fill=(16, 32, 24), outline=GREEN, width=1)
    draw.text((ash_x + 15, ash_y + 8), "ASHRAE TC 9.9 THERMAL COMPLIANCE ENVELOPES", font=get_font(13, bold=True), fill=GREEN)

    # Visual Spectrum Bars for Thermal Classes
    bar_x0 = ash_x + 50
    bar_y0 = ash_y + 80
    bar_w = 700
    bar_h = 45

    # Recommended Class A1 (18°C to 27°C)
    draw.rectangle([(bar_x0, bar_y0), (bar_x0 + bar_w, bar_y0 + bar_h)], fill=(20, 24, 32), outline=PANEL_BORDER, width=1)
    # 18-27C is green (scaled across 10C to 45C = 35C range)
    rec_x0 = bar_x0 + int(((18 - 10) / 35) * bar_w)
    rec_x1 = bar_x0 + int(((27 - 10) / 35) * bar_w)
    draw.rectangle([(rec_x0, bar_y0), (rec_x1, bar_y0 + bar_h)], fill=(16, 60, 35), outline=GREEN, width=2)
    draw.text((rec_x0 + 20, bar_y0 + 12), "RECOMMENDED ENVELOPE: 18.0°C to 27.0°C", font=get_font(11, bold=True), fill=GREEN)

    # Allowable Class A1 (15°C to 32°C)
    bar_y1 = bar_y0 + 90
    draw.rectangle([(bar_x0, bar_y1), (bar_x0 + bar_w, bar_y1 + bar_h)], fill=(20, 24, 32), outline=PANEL_BORDER, width=1)
    all_x0 = bar_x0 + int(((15 - 10) / 35) * bar_w)
    all_x1 = bar_x0 + int(((32 - 10) / 35) * bar_w)
    draw.rectangle([(all_x0, bar_y1), (all_x1, bar_y1 + bar_h)], fill=(20, 45, 60), outline=CYAN, width=2)
    draw.text((all_x0 + 20, bar_y1 + 12), "ALLOWABLE CLASS A1: 15.0°C to 32.0°C (Max RH 80%)", font=get_font(11, bold=True), fill=CYAN)

    # Critical Exceedance (> 32°C)
    crit_x0 = all_x1
    draw.rectangle([(crit_x0, bar_y1), (bar_x0 + bar_w, bar_y1 + bar_h)], fill=(60, 20, 25), outline=RED, width=2)
    draw.text((crit_x0 + 15, bar_y1 + 12), "CRITICAL > 32°C", font=get_font(11, bold=True), fill=RED)

    # Explanation notes on ASHRAE
    ay = bar_y1 + 80
    draw.text((ash_x + 50, ay), "RACK COOLING INDEX (RCI) METRICS:", font=get_font(12, bold=True), fill=TEXT_MAIN)
    ay += 25
    draw.text((ash_x + 50, ay), "• RCI_HI (High-Temp Compliance): Percentage of rack intake points operating within", font=get_font(10), fill=TEXT_MUTED)
    ay += 18
    draw.text((ash_x + 50, ay), "  the Recommended max (27°C) with zero points exceeding Allowable max (32°C).", font=get_font(10), fill=TEXT_MUTED)
    ay += 25
    draw.text((ash_x + 50, ay), "• Target: RCI_HI >= 95% (Ideal: 100%). If RCI_HI < 90%, hot spots exist.", font=get_font(10, bold=True), fill=GREEN)
    ay += 30
    draw.text((ash_x + 50, ay), "• RCI_LO (Low-Temp Compliance): Percentage of points above minimum floor (18°C).", font=get_font(10), fill=TEXT_MUTED)
    ay += 18
    draw.text((ash_x + 50, ay), "  Prevents energy waste caused by overcooling whitespace below dew point margin.", font=get_font(10), fill=TEXT_MUTED)

    # Bottom Audit Rule Box
    draw.rectangle([(80, H - 280), (W - 80, H - 75)], fill=(15, 23, 42), outline=PANEL_BORDER, width=1)
    draw.text((100, H - 265), "CFD COLOR SCALE AUDIT LAW: THE PALETTE MANIPULATION TRAP", font=get_font(12, bold=True), fill=AMBER)
    draw.text((100, H - 235), "1. A CFD author can make an overheated data hall look perfectly blue simply by setting the palette maximum to 45°C.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((100, H - 210), "2. Conversely, a healthy room can be made to look dangerously red by setting the palette maximum to 26°C.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((100, H - 185), "3. NEVER judge a CFD report from color contours alone! Always inspect the numerical temperature values at physical probe planes.", font=get_font(11, bold=True), fill=RED)
    draw.text((100, H - 160), "4. The color bar is not a standard; ASHRAE TC 9.9 is the standard. Re-scale all CFD plots to fixed 15°C - 35°C before acceptance.", font=get_font(11), fill=TEXT_MAIN)

    save_path = FIG_DIR / "fig-06-thermal-indexes-and-ashrae-envelopes.png"
    img.save(save_path, "PNG")
    print(f"Saved: {save_path}")

# ==============================================================================
# DIAGRAM 7: CFD Report Decision Authority & Refusal Matrix
# ==============================================================================
def draw_fig_07():
    img, draw = create_base_canvas(
        title="CFD Report Decision Authority & Mandatory Statement Refusal Matrix",
        subtitle="Four Contractually Permitted Decision Domains vs. Prohibited Speculative Statements",
        sheet_ref="SHEET 2 (DECISION AUDIT)"
    )

    # Left: 4 Permitted Decision Domains
    left_x = 60
    top_y = 150
    pw = 800
    ph = 860

    draw.rectangle([(left_x, top_y), (left_x + pw, top_y + ph)], fill=PANEL_BG, outline=GREEN, width=2)
    draw.rectangle([(left_x, top_y), (left_x + pw, top_y + 36)], fill=(16, 32, 24), outline=GREEN, width=1)
    draw.text((left_x + 15, top_y + 8), "FOUR CONTRACTUALLY PERMITTED DECISION DOMAINS", font=get_font(13, bold=True), fill=GREEN)

    domains = [
        ("1. PRE-CONSTRUCTION DESIGN COMPARISON",
         "Permitted Scope: Comparing Option A vs Option B under identical boundary rules.\n"
         "Allowed Verdict: 'Option A achieves 4.2 K lower peak rack inlet temperatures than Option B.'\n"
         "Boundary Condition: Does not require site measurements; requires identical numerical meshes.",
         GREEN),
        ("2. BUILT-HALL COMPLIANCE EVALUATION",
         "Permitted Scope: Validating as-built room airflow against design intent.\n"
         "Allowed Verdict: 'Calibrated model demonstrates that with all CRAHs active, 100% of rack inlets satisfy ASHRAE Recommended A1.'\n"
         "Boundary Condition: Requires Sheet 1 multi-point calibration with MAE <= 1.0 K.",
         GREEN),
        ("3. OPERATIONAL HOTSPOT ROOT-CAUSE ANALYSIS",
         "Permitted Scope: Diagnosing physical causes for specific overheating cabinets.\n"
         "Allowed Verdict: 'Hotspot at Rack 14 is driven by 3 missing blanking panels causing 180 L/s local recirculation.'\n"
         "Boundary Condition: The root cause must be an input you can physically walk to in the room.",
         CYAN),
        ("4. N-1 EMERGENCY FAILURE RIDE-THROUGH",
         "Permitted Scope: Predicting temperature rise following loss of one CRAH unit.\n"
         "Allowed Verdict: 'Upon loss of CRAH-03, Rack 08 inlet rises from 22.1°C to 28.4°C over 12 minutes.'\n"
         "Boundary Condition: Requires transient time-stepping; steady-state cannot narrate a timeline.",
         AMBER)
    ]

    dy = top_y + 55
    for d_title, d_desc, d_col in domains:
        draw.rectangle([(left_x + 15, dy), (left_x + pw - 15, dy + 175)], fill=(18, 24, 32), outline=d_col, width=1)
        draw.text((left_x + 25, dy + 10), d_title, font=get_font(11, bold=True), fill=d_col)
        draw.text((left_x + 25, dy + 35), d_desc, font=get_font(10), fill=TEXT_MAIN)
        dy += 195

    # Right: Prohibited Statements & Refusal Rules
    rx0 = 940
    draw.rectangle([(rx0, top_y), (rx0 + pw, top_y + ph)], fill=PANEL_BG, outline=RED, width=2)
    draw.rectangle([(rx0, top_y), (rx0 + pw, top_y + 36)], fill=(35, 18, 24), outline=RED, width=1)
    draw.text((rx0 + 15, top_y + 8), "PROHIBITED SPECULATIVE STATEMENTS (MANDATORY REFUSAL)", font=get_font(13, bold=True), fill=RED)

    refusals = [
        ("REFUSAL 1: 'THE HALL HAS PASSED COMMISSIONING'",
         "Reason for Refusal: A CFD model is a mathematical simulation, not a physical test.\n"
         "Commissioning pass/fail is proven exclusively by physical load-bank testing (Book 03).\n"
         "Action: Refuse signature. Demand physical Level 5 IST data sheets.",
         RED),
        ("REFUSAL 2: 'ADD 100 kW COOLING CAPACITY TO FIX THE ROOM'",
         "Reason for Refusal: This is an unverified proposal, not an engineering conclusion.\n"
         "Action: Refuse to purchase equipment until the consultant runs a verified rerun script\n"
         "with the proposed unit added to the model geometry and proves it eliminates the hotspot.",
         RED),
        ("REFUSAL 3: 'THE SERVERS WILL TRAIN AI WORKLOADS RELIABLY'",
         "Reason for Refusal: CFD simulates whitespace air temperatures; it does not model\n"
         "silicon junction temperatures, clock throttling, NVLink errors, or software crashes.\n"
         "Action: Strike sentence from report. Limit claim strictly to air boundary temperatures.",
         AMBER),
        ("REFUSAL 4: 'A STREAMLINE PROVES FLOW RATE IS 450 L/s'",
         "Reason for Refusal: A streamline shows velocity direction, not mass flow rate.\n"
         "Action: Require integrated volumetric flux across opening or physical ultrasonic measurement.",
         AMBER)
    ]

    ry = top_y + 55
    for r_title, r_desc, r_col in refusals:
        draw.rectangle([(rx0 + 15, ry), (rx0 + pw - 15, ry + 175)], fill=(24, 18, 22), outline=r_col, width=1)
        draw.text((rx0 + 25, ry + 10), r_title, font=get_font(11, bold=True), fill=r_col)
        draw.text((rx0 + 25, ry + 35), r_desc, font=get_font(10), fill=TEXT_MAIN)
        ry += 195

    save_path = FIG_DIR / "fig-07-cfd-decision-and-refusal-matrix.png"
    img.save(save_path, "PNG")
    print(f"Saved: {save_path}")

def main():
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    print("Generating Flagship Engineering Diagrams for Book 04...")
    draw_fig_01()
    draw_fig_02()
    draw_fig_03()
    draw_fig_04()
    draw_fig_05()
    draw_fig_06()
    draw_fig_07()
    print("All 7 Engineering Diagrams successfully generated for Book 04!")

if __name__ == "__main__":
    main()
