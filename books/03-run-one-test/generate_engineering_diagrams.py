#!/usr/bin/env python3
"""
Generate Flagship High-Resolution Engineering Diagrams for Book 03:
Finish a Liquid Cooling Verification: Seven sheets for one load-bank test

Output directory: books/03-run-one-test/figures/
Resolution: 1800 x 1100 px, 300 DPI aesthetic, high-contrast industrial vector style.
Colors: Dark slate theme (BG: #12151c, Card: #1a202c, Cyan: #00e5ff, Blue: #2979ff,
        Orange/Warning: #ff9100, Green/Pass: #00e676, Red/Fail: #ff1744, White: #ffffff).
"""

import math
import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path("/Users/geese/Downloads/book/books/03-run-one-test")
FIG_DIR = ROOT / "figures"
FONT_DIR = Path("/Users/geese/Downloads/book/books/01-liquid-load-bank/fonts")

# Palette constants
BG_COLOR = (18, 21, 28)          # #12151c Deep charcoal slate
PANEL_BG = (26, 32, 44)          # #1a202c Technical card surface
PANEL_BORDER = (45, 55, 72)      # #2d3748 Border outline
GRID_COLOR = (30, 36, 48)        # Subtle coordinate grid
TEXT_MAIN = (255, 255, 255)      # Pure white
TEXT_MUTED = (160, 174, 192)     # Cool silver grey
CYAN = (0, 229, 255)             # Accent cyan (Flow / TCS secondary)
BLUE = (41, 121, 255)            # Primary blue (FWS primary / Power)
AMBER = (255, 171, 0)            # Warning / Transient
RED = (255, 23, 68)              # Failure / Blocker / Stop
GREEN = (0, 230, 118)            # Pass / Healthy / Nominal
PURPLE = (179, 136, 255)         # Logic / Bitmask / Controls

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
    draw.text((50, 42), "FIELD GUIDE 03 // LIQUID VERIFICATION & SEVEN SHEETS", font=get_font(15, bold=True), fill=CYAN)
    draw.text((50, 68), title.upper(), font=get_font(24, bold=True), fill=TEXT_MAIN)
    draw.text((50, 96), subtitle, font=get_font(13, bold=False), fill=TEXT_MUTED)

    if sheet_ref:
        s_box_w = 260
        draw.rectangle([(W - 50 - s_box_w, 42), (W - 50, 98)], fill=(15, 23, 42), outline=CYAN, width=1)
        draw.text((W - 40 - s_box_w, 52), "REFERENCED MASTER FORM", font=get_font(11, bold=True), fill=AMBER)
        draw.text((W - 40 - s_box_w, 72), sheet_ref, font=get_font(15, bold=True), fill=CYAN)

    # 4. Footer Status Bar
    draw.rectangle([(30, H - 55), (W - 30, H - 30)], fill=PANEL_BG, outline=PANEL_BORDER, width=1)
    draw.text((50, H - 48), "ASHRAE 0-2019 / ACG GUIDELINE // NON-PROPRIETARY 120kW NVL72 BASELINE // STRICT WITNESS PROTOCOL",
              font=get_font(12, bold=False), fill=TEXT_MUTED)
    footer_tag = "TRISTAN DATA CENTER FIELD GUIDES // ED. 2026"
    ftw = draw.textlength(footer_tag, font=get_font(12, bold=True))
    draw.text((W - 80 - ftw, H - 48), footer_tag, font=get_font(12, bold=True), fill=CYAN)

    return img, draw

# ==============================================================================
# DIAGRAM 1: Commissioning Gate Ladder & Milestone Verification Sequence
# ==============================================================================
def draw_fig_01():
    img, draw = create_base_canvas(
        title="Commissioning Gate Ladder & Multi-Level Verification Hierarchy",
        subtitle="Mapping ASHRAE Levels 0-6 to the Field 3-Stage Protocol with Mandatory Pre-Requisite Gating",
        sheet_ref="SHEET 1 & LEVEL MAP"
    )

    # Main workflow cards across horizontal timeline
    levels = [
        ("LEVEL 0", "Design & OPR", "ASHRAE Guideline 0",
         ["• Owner Project Requirements (OPR)", "• Basis of Design (BOD) Audit", "• Flow & P&ID Schematic Sign-off", "• Non-negotiable limits established"],
         PANEL_BG, CYAN),
        ("LEVEL 1", "Factory Acceptance (FAT)", "Vendor Factory Witness",
         ["• CDU Factory Pressure & Leak Test", "• VFD Pump Baseline Curves", "• Load Bank Ingress & Safety Sign-off", "• Factory Calibration Certificates"],
         PANEL_BG, BLUE),
        ("LEVEL 2", "Receipt & Static QA", "Stage 1: Pre-Start-Up",
         ["• Physical uncrating inspection", "• Fitting & hose seal verification", "• Megger test: R_insul >= 100 MOhm", "• Phase rotation check (A-B-C)"],
         PANEL_BG, AMBER),
        ("LEVEL 3", "PFC & Hydraulic Hold", "Stage 1: Clean & Fill",
         ["• Flushing velocity >= 1.5 m/s", "• Hydrostatic hold: 1.5x WP (2h)", "• Air purge & deaeration verified", "• Expansion tank N2 cushion set"],
         PANEL_BG, PURPLE),
        ("LEVEL 4", "Functional Performance (FPT)", "Stage 2: Single System",
         ["• Autonomous CDU pump start/stop", "• Cold no-heat pump curve baseline", "• N+1 pump trip auto-changeover", "• 100% Alarm loop physical injection"],
         PANEL_BG, CYAN),
        ("LEVEL 5", "Integrated Systems (IST)", "Stage 3: Full Thermal Load",
         ["• Multi-tier heat ladder (25-100%)", "• 110% Overload margin dwell", "• 2N Feeder A power loss pull", "• Enthalpy closure reconciliation >= 97%"],
         PANEL_BG, GREEN),
        ("LEVEL 6", "Turnover & Closeout", "Final Operations Handover",
         ["• 100% Punch List Cat 1/2 cleared", "• 7 Signed Field Master Sheets", "• Trend log archive & checksum", "• Systems Manual & Ops sign-off"],
         PANEL_BG, (16, 185, 129))
    ]

    card_w = 224
    gap = 16
    start_x = 45
    card_y = 140
    card_h = 440

    for i, (lvl, title, sub, bullets, bg, border_c) in enumerate(levels):
        cx = start_x + i * (card_w + gap)
        # Card frame
        draw.rectangle([(cx, card_y), (cx + card_w, card_y + card_h)], fill=bg, outline=border_c, width=2)
        # Header banner
        draw.rectangle([(cx, card_y), (cx + card_w, card_y + 40)], fill=(20, 26, 38), outline=border_c, width=1)
        draw.text((cx + 12, card_y + 10), lvl, font=get_font(15, bold=True), fill=border_c)

        draw.text((cx + 12, card_y + 48), title, font=get_font(14, bold=True), fill=TEXT_MAIN)
        draw.text((cx + 12, card_y + 70), sub, font=get_font(11, bold=False), fill=TEXT_MUTED)
        draw.line([(cx + 10, card_y + 92), (cx + card_w - 10, card_y + 92)], fill=PANEL_BORDER, width=1)

        # Bullets
        by = card_y + 106
        for b in bullets:
            draw.text((cx + 10, by), b, font=get_font(11, bold=False), fill=TEXT_MAIN)
            by += 38

        # Gate Interlock icon at bottom of card
        draw.rectangle([(cx + 15, card_y + card_h - 48), (cx + card_w - 15, card_y + card_h - 15)],
                       fill=(15, 23, 42), outline=border_c, width=1)
        draw.text((cx + 25, card_y + card_h - 40), f"GATE {i}: 100% SIGN-OFF", font=get_font(10, bold=True), fill=border_c)

        # Arrow to next card
        if i < len(levels) - 1:
            arrow_x = cx + card_w + 3
            arrow_y = card_y + card_h // 2
            draw.polygon([(arrow_x, arrow_y - 8), (arrow_x + 12, arrow_y), (arrow_x, arrow_y + 8)], fill=CYAN)

    # Lower Section: Hard Interlock Rules & Field Translation Matrix
    rule_y = 610
    draw.rectangle([(45, rule_y), (W - 45, H - 75)], fill=PANEL_BG, outline=PANEL_BORDER, width=2)
    draw.rectangle([(45, rule_y), (W - 45, rule_y + 36)], fill=(20, 26, 38), outline=PANEL_BORDER, width=1)
    draw.text((65, rule_y + 8), "COMMISSIONING GOVERNANCE: THREE NON-NEGOTIABLE INTERLOCK LAWS", font=get_font(14, bold=True), fill=AMBER)

    laws = [
        ("LAW 1: NO PHASE HOPPING",
         "Never begin Level 4 (Single System FPT) while Level 3 hydrostatic pressure holds or flush certificates remain open. A leak or debris in a heat exchanger under thermal load permanently contaminates the CDU plates and invalidates pump baseline curves.",
         RED),
        ("LAW 2: THE DIALECT TRAP",
         "A contractor calling their testing 'Stage 1, 2, 3' must never file Stage 1 as Level 1 FAT! Level 1 is a factory witness test. Filing a site walk-through into an L1 certificate is audit fraud. Explicitly map local terms on page one of the Cx Plan.",
         CYAN),
        ("LAW 3: PUNCH LIST INTERLOCK",
         "Category 1 defects (leaks, trip failures, reversed phases, missing E-Stops) act as automated mechanical interlocks. No Level 5 heat command may be issued while a Cat 1 defect is open. Waivers require unanimous Owner PE and CxA signatures.",
         GREEN)
    ]

    law_w = 540
    for j, (ltitle, ldesc, lcol) in enumerate(laws):
        lx = 65 + j * (law_w + 25)
        ly = rule_y + 55
        draw.rectangle([(lx, ly), (lx + law_w, ly + 310)], fill=(18, 22, 32), outline=lcol, width=1)
        draw.rectangle([(lx, ly), (lx + law_w, ly + 34)], fill=(26, 32, 44), outline=lcol, width=1)
        draw.text((lx + 12, ly + 8), ltitle, font=get_font(13, bold=True), fill=lcol)

        # Word wrap text inside law box
        words = ldesc.split()
        line = ""
        ty = ly + 48
        for w in words:
            test_line = line + " " + w if line else w
            if draw.textlength(test_line, font=get_font(12)) < (law_w - 24):
                line = test_line
            else:
                draw.text((lx + 12, ty), line, font=get_font(12), fill=TEXT_MAIN)
                ty += 24
                line = w
        if line:
            draw.text((lx + 12, ty), line, font=get_font(12), fill=TEXT_MAIN)

    save_path = FIG_DIR / "fig-01-cx-gate-ladder.png"
    img.save(save_path, "PNG")
    print(f"Saved: {save_path}")

# ==============================================================================
# DIAGRAM 2: Liquid Cooling Distribution Unit (CDU) Piping & Instrumentation Diagram (P&ID)
# ==============================================================================
def draw_fig_02():
    img, draw = create_base_canvas(
        title="1.2 MW Liquid Cooling Distribution Unit (CDU) P&ID Architecture",
        subtitle="Primary/Secondary Hydraulic Separation, Modulating Control Loops, and Instrument Tap Locations",
        sheet_ref="SHEET 2 & SHEET 7"
    )

    # Draw primary circuit (Facility Water System - FWS) on the left
    # Draw Plate Heat Exchanger (PHE) in the middle
    # Draw secondary circuit (Technology Cooling System - TCS) on the right

    # Center PHE
    phe_x = 750
    phe_y = 260
    phe_w = 160
    phe_h = 320
    draw.rectangle([(phe_x, phe_y), (phe_x + phe_w, phe_y + phe_h)], fill=(20, 30, 48), outline=CYAN, width=3)
    draw.line([(phe_x, phe_y), (phe_x + phe_w, phe_y + phe_h)], fill=BLUE, width=2)
    draw.line([(phe_x, phe_y + phe_h), (phe_x + phe_w, phe_y)], fill=CYAN, width=2)
    draw.text((phe_x + 35, phe_y + 130), "PHE-101", font=get_font(18, bold=True), fill=TEXT_MAIN)
    draw.text((phe_x + 15, phe_y + 160), "1.2 MW Counterflow", font=get_font(11, bold=False), fill=TEXT_MUTED)
    draw.text((phe_x + 20, phe_y + 180), "Titanium / SS316L", font=get_font(11, bold=False), fill=TEXT_MUTED)

    # PRIMARY SIDE (Left: FWS)
    draw.text((120, 140), "PRIMARY FACILITY WATER LOOP (FWS / FWR)", font=get_font(16, bold=True), fill=BLUE)
    draw.text((120, 165), "Design: 30°C Supply / 36°C Return // Chilled or Warm Plant Loop", font=get_font(12), fill=TEXT_MUTED)

    # Primary Supply line (Top left)
    draw.line([(80, 290), (phe_x, 290)], fill=BLUE, width=5)
    draw.polygon([(phe_x - 15, 283), (phe_x, 290), (phe_x - 15, 297)], fill=BLUE) # arrow
    draw.text((90, 260), "FWS Supply Header (DN150)", font=get_font(12, bold=True), fill=BLUE)

    # Primary Return line (Bottom left)
    draw.line([(phe_x, 530), (80, 530)], fill=BLUE, width=5)
    draw.polygon([(80 + 15, 523), (80, 530), (80 + 15, 537)], fill=BLUE)
    draw.text((90, 545), "FWR Return Header (DN150)", font=get_font(12, bold=True), fill=BLUE)

    # Primary Instruments: TCV-101 modulating valve on return
    tcv_x = 420
    tcv_y = 530
    draw.polygon([(tcv_x - 25, tcv_y - 20), (tcv_x + 25, tcv_y + 20), (tcv_x + 25, tcv_y - 20), (tcv_x - 25, tcv_y + 20)], fill=(40, 50, 70), outline=AMBER)
    draw.rectangle([(tcv_x - 8, tcv_y - 45), (tcv_x + 8, tcv_y - 20)], fill=AMBER)
    draw.text((tcv_x - 30, tcv_y - 65), "TCV-101", font=get_font(12, bold=True), fill=AMBER)
    draw.text((tcv_x - 45, tcv_y + 28), "Modulating 0-10V", font=get_font(10), fill=TEXT_MUTED)

    # Primary Strainer & Flow Meter (FT-101)
    str_x = 280
    draw.rectangle([(str_x - 15, 275), (str_x + 15, 305)], fill=PANEL_BG, outline=TEXT_MAIN, width=2)
    draw.text((str_x - 20, 245), "STR-101 (50 mesh)", font=get_font(10), fill=TEXT_MUTED)

    ft1_x = 520
    draw.ellipse([(ft1_x - 18, 272), (ft1_x + 18, 308)], fill=PANEL_BG, outline=GREEN, width=2)
    draw.text((ft1_x - 12, 282), "FT", font=get_font(11, bold=True), fill=GREEN)
    draw.text((ft1_x - 20, 320), "FT-101 (Mag)", font=get_font(10), fill=TEXT_MUTED)

    # SECONDARY SIDE (Right: TCS)
    draw.text((1000, 140), "SECONDARY TECHNOLOGY COOLING SYSTEM (TCS)", font=get_font(16, bold=True), fill=CYAN)
    draw.text((1000, 165), "Design: 40°C Supply / 50°C Return // PG25 or Treated Water // N+1 Pumps", font=get_font(12), fill=TEXT_MUTED)

    # Secondary Supply line (Bottom to IT Racks)
    draw.line([(phe_x + phe_w, 330), (1700, 330)], fill=CYAN, width=5)
    draw.polygon([(1700, 330), (1685, 323), (1685, 337)], fill=CYAN)
    draw.text((1480, 305), "TCS Supply to Racks (DN150)", font=get_font(12, bold=True), fill=CYAN)

    # Secondary Return line (Top from IT Racks into pumps)
    draw.line([(1700, 490), (1150, 490)], fill=CYAN, width=5)
    draw.polygon([(1150 + 15, 483), (1150, 490), (1150 + 15, 497)], fill=CYAN)
    draw.text((1480, 505), "TCS Return from Racks (DN150)", font=get_font(12, bold=True), fill=CYAN)

    # Dual Secondary Pumps (N+1 VFD Canned Pumps)
    p_x = 1050
    # Pump A
    draw.ellipse([(p_x - 30, 420), (p_x + 30, 480)], fill=PANEL_BG, outline=CYAN, width=3)
    draw.text((p_x - 18, 442), "P-1A", font=get_font(12, bold=True), fill=CYAN)
    draw.text((p_x - 25, 400), "VFD Lead", font=get_font(10), fill=GREEN)
    # Pump B
    draw.ellipse([(p_x - 30, 520), (p_x + 30, 580)], fill=PANEL_BG, outline=CYAN, width=3)
    draw.text((p_x - 18, 542), "P-1B", font=get_font(12, bold=True), fill=CYAN)
    draw.text((p_x - 35, 590), "VFD Standby", font=get_font(10), fill=AMBER)

    # Connect manifold to pumps and into PHE
    draw.line([(1150, 490), (1150, 450), (p_x + 30, 450)], fill=CYAN, width=3)
    draw.line([(1150, 490), (1150, 550), (p_x + 30, 550)], fill=CYAN, width=3)
    draw.line([(p_x - 30, 450), (950, 450)], fill=CYAN, width=3)
    draw.line([(p_x - 30, 550), (950, 550)], fill=CYAN, width=3)
    draw.line([(950, 450), (950, 510), (phe_x + phe_w, 510)], fill=CYAN, width=5)

    # Check valves after pumps
    for py in [450, 550]:
        draw.polygon([(990, py - 12), (990, py + 12), (1010, py)], fill=PANEL_BG, outline=CYAN, width=1)

    # Secondary Bypass Valve (BPV-201)
    bpv_x = 1380
    draw.line([(bpv_x, 330), (bpv_x, 490)], fill=AMBER, width=3) # bypass line
    draw.polygon([(bpv_x - 15, 400), (bpv_x + 15, 420), (bpv_x + 15, 400), (bpv_x - 15, 420)], fill=(40, 50, 70), outline=AMBER)
    draw.text((bpv_x + 22, 405), "BPV-201 (dP Bypass)", font=get_font(11, bold=True), fill=AMBER)

    # Filter & Deaerator Skid
    skid_x = 1250
    skid_y = 620
    draw.rectangle([(skid_x, skid_y), (skid_x + 380, skid_y + 110)], fill=(20, 26, 38), outline=PURPLE, width=2)
    draw.text((skid_x + 15, skid_y + 12), "WATER QUALITY & EXPANSION SKID", font=get_font(12, bold=True), fill=PURPLE)
    draw.text((skid_x + 15, skid_y + 36), "• 50 um Micro-filter with delta-P switch", font=get_font(11), fill=TEXT_MAIN)
    draw.text((skid_x + 15, skid_y + 58), "• Automatic Vacuum Deaerator (Air Purge)", font=get_font(11), fill=TEXT_MAIN)
    draw.text((skid_x + 15, skid_y + 80), "• Diaphragm Expansion Tank (N2 Cushion: 1.8 bar)", font=get_font(11), fill=TEXT_MAIN)

    # Key Commissioning Taps callout box at bottom left
    draw.rectangle([(80, 620), (680, H - 80)], fill=PANEL_BG, outline=CYAN, width=2)
    draw.rectangle([(80, 620), (680, 656)], fill=(20, 26, 38), outline=CYAN, width=1)
    draw.text((95, 630), "MANDATORY WITNESS INSTRUMENT TAPS FOR LEVEL 4/5 TESTING", font=get_font(13, bold=True), fill=CYAN)

    taps = [
        ("TT-201 / TT-202 (Calibrated PT100 1/3 DIN)", "Secondary supply & return immersion thermowells. Used to cross-check BMS against handheld reference calibrated to +/-0.05 K."),
        ("PT-201 / PT-202 (High-Accuracy Transmitters)", "Differential pressure across PHE and across secondary supply/return manifold for pump curve verification."),
        ("FT-201 (Electromagnetic / Ultrasonic Ports)", "Direct secondary flow verification. BSRIA guidelines require dual transducer clamp-on audit ports on straight 10D/5D pipe runs."),
        ("LS-201 & Leak Rope Sensor Interlocks", "Internal CDU catch-pan optical sensor and external perimeter sensing rope. Must physically trip alarm within < 2.0s.")
    ]
    ty = 670
    for title_tap, desc_tap in taps:
        draw.text((95, ty), f"• {title_tap}", font=get_font(11, bold=True), fill=AMBER)
        words = desc_tap.split()
        line = ""
        ty += 20
        for w in words:
            test_line = line + " " + w if line else w
            if draw.textlength(test_line, font=get_font(11)) < 560:
                line = test_line
            else:
                draw.text((110, ty), line, font=get_font(11), fill=TEXT_MAIN)
                ty += 18
                line = w
        if line:
            draw.text((110, ty), line, font=get_font(11), fill=TEXT_MAIN)
            ty += 26

    save_path = FIG_DIR / "fig-02-cdu-hydraulic-pandid.png"
    img.save(save_path, "PNG")
    print(f"Saved: {save_path}")

# ==============================================================================
# DIAGRAM 3: Pump Head vs Flow Operating Curve (Cold vs Hot Viscosity Shift)
# ==============================================================================
def draw_fig_03():
    img, draw = create_base_canvas(
        title="Secondary Pump Head-Flow Curves & Thermal Viscosity Shift",
        subtitle="Cold No-Heat Hydraulic Baseline (20°C) vs. 100% Thermal Load (50°C) System Resistance",
        sheet_ref="SHEET 6 (PUMP CURVE)"
    )

    # Graph plotting area
    gx0, gy0 = 120, 180
    gw, gh = 1050, 560
    gx1, gy1 = gx0 + gw, gy0 + gh

    draw.rectangle([(gx0, gy0), (gx1, gy1)], fill=(16, 20, 28), outline=PANEL_BORDER, width=2)

    # Sub-grid lines inside graph
    for i in range(1, 10):
        # vertical grid
        x = gx0 + int(i * gw / 10)
        draw.line([(x, gy0), (x, gy1)], fill=(28, 35, 48), width=1)
        q_val = i * 15 # 0 to 150 m3/h
        draw.text((x - 12, gy1 + 10), f"{q_val}", font=get_font(11), fill=TEXT_MUTED)

        # horizontal grid
        y = gy0 + int(i * gh / 10)
        draw.line([(gx0, y), (gx1, y)], fill=(28, 35, 48), width=1)
        h_val = (10 - i) * 40 # 0 to 400 kPa
        draw.text((gx0 - 45, y - 8), f"{h_val}", font=get_font(11), fill=TEXT_MUTED)

    draw.text((gx0 + gw // 2 - 80, gy1 + 35), "Volumetric Flow Rate Q (m³/h) [Secondary PG25]", font=get_font(13, bold=True), fill=TEXT_MAIN)
    draw.text((gx0 - 90, gy0 - 30), "Head H (kPa)", font=get_font(13, bold=True), fill=TEXT_MAIN)

    # Plot 1: Dual-Pump Parallel VFD 100% (50 Hz) curve (Descending quadratic curve)
    # H = H0 - a*Q^2
    pts_pump_dual = []
    for q_step in range(0, 130):
        # Q in m3/h
        q = q_step
        head = 380 - 0.016 * (q ** 2)
        px = gx0 + int((q / 150) * gw)
        py = gy1 - int((head / 400) * gh)
        if gy0 <= py <= gy1 and gx0 <= px <= gx1:
            pts_pump_dual.append((px, py))
    draw.line(pts_pump_dual, fill=CYAN, width=4)
    draw.text((pts_pump_dual[-1][0] - 220, pts_pump_dual[-1][1] - 25), "Dual Pumps 100% Speed (50Hz)", font=get_font(12, bold=True), fill=CYAN)

    # Plot 2: Single-Pump VFD 100% curve
    pts_pump_single = []
    for q_step in range(0, 95):
        q = q_step
        head = 370 - 0.038 * (q ** 2)
        px = gx0 + int((q / 150) * gw)
        py = gy1 - int((head / 400) * gh)
        if gy0 <= py <= gy1 and gx0 <= px <= gx1:
            pts_pump_single.append((px, py))
    draw.line(pts_pump_single, fill=AMBER, width=3)
    draw.text((pts_pump_single[-1][0] - 180, pts_pump_single[-1][1] - 20), "Single Pump 100% (Trip Mode)", font=get_font(12, bold=True), fill=AMBER)

    # Plot 3: Cold System Resistance Curve (20°C PG25, high viscosity nu = 2.45 mm2/s)
    # H_sys = k_cold * Q^1.85
    pts_sys_cold = []
    for q_step in range(0, 125):
        q = q_step
        head = 0.027 * (q ** 1.95)
        px = gx0 + int((q / 150) * gw)
        py = gy1 - int((head / 400) * gh)
        if gy0 <= py <= gy1 and gx0 <= px <= gx1:
            pts_sys_cold.append((px, py))
    draw.line(pts_sys_cold, fill=BLUE, width=3)
    draw.text((pts_sys_cold[-1][0] - 240, pts_sys_cold[-1][1] - 20), "Cold System Curve (20°C, mu=2.8 cP)", font=get_font(12, bold=True), fill=BLUE)

    # Plot 4: Hot System Resistance Curve (50°C PG25, low viscosity nu = 1.15 mm2/s)
    pts_sys_hot = []
    for q_step in range(0, 135):
        q = q_step
        head = 0.019 * (q ** 1.95)
        px = gx0 + int((q / 150) * gw)
        py = gy1 - int((head / 400) * gh)
        if gy0 <= py <= gy1 and gx0 <= px <= gx1:
            pts_sys_hot.append((px, py))
    draw.line(pts_sys_hot, fill=RED, width=3)
    draw.text((pts_sys_hot[-1][0] - 240, pts_sys_hot[-1][1] + 15), "Hot System Curve (50°C, mu=1.1 cP)", font=get_font(12, bold=True), fill=RED)

    # Highlight Intersection Point A (Cold Design Operating Point)
    # around Q = 100, H = 220
    pt_a_x = gx0 + int((102 / 150) * gw)
    pt_a_y = gy1 - int((214 / 400) * gh)
    draw.ellipse([(pt_a_x - 7, pt_a_y - 7), (pt_a_x + 7, pt_a_y + 7)], fill=GREEN, outline=TEXT_MAIN, width=2)
    draw.text((pt_a_x + 12, pt_a_y - 18), "POINT A: Cold Baseline (102 m³/h @ 214 kPa)", font=get_font(11, bold=True), fill=GREEN)

    # Highlight Intersection Point B (Hot Operating Point - Shifted)
    # around Q = 114, H = 172
    pt_b_x = gx0 + int((115 / 150) * gw)
    pt_b_y = gy1 - int((170 / 400) * gh)
    draw.ellipse([(pt_b_x - 7, pt_b_y - 7), (pt_b_x + 7, pt_b_y + 7)], fill=RED, outline=TEXT_MAIN, width=2)
    draw.text((pt_b_x + 12, pt_b_y + 10), "POINT B: Hot Full Load (115 m³/h @ 170 kPa)", font=get_font(11, bold=True), fill=RED)

    # Right side explanation panel
    pan_x = gx1 + 35
    pan_y = gy0
    pan_w = W - pan_x - 55
    draw.rectangle([(pan_x, pan_y), (pan_x + pan_w, gy1)], fill=PANEL_BG, outline=CYAN, width=2)
    draw.rectangle([(pan_x, pan_y), (pan_x + pan_w, pan_y + 36)], fill=(20, 26, 38), outline=CYAN, width=1)
    draw.text((pan_x + 15, pan_y + 10), "PHYSICAL PRINCIPLES & AUDIT RULES", font=get_font(13, bold=True), fill=CYAN)

    rules = [
        ("1. WHY PLOT BEFORE HEAT?",
         "Cold PG25 has 2.4x higher dynamic viscosity than at 50°C. Throttling and flow balance across quick disconnects must be recorded at 20°C with automated VFD control locked off. This decouples piping frictional resistance from thermal viscosity thinning."),
        ("2. VISCOSITY THINNING PHENOMENON",
         "As the loop heats from 20°C to 50°C, Reynolds number rises from 28,000 to >65,000 in DN40 branches. Wall shear stress drops, shifting system resistance from Point A down to Point B. Uncontrolled pumps will increase flow by 12-15% automatically."),
        ("3. THE VFD HUNTING TRAP",
         "If the CDU VFD is left in active delta-P tracking mode during heat ramping, the controller will ramp down frequency to counteract the lower resistance. An auditor cannot distinguish between pump degradation and fluid thinning without Sheet 6 baseline curves!"),
        ("4. ACCEPTANCE CRITERIA",
         "The cold curve must contain at least 4 distinct throttling steps (100%, 80%, 60%, 40% valve opening). Measured Head vs Flow must match vendor submittal within +/- 5.0% across all 4 points.")
    ]
    ry = pan_y + 50
    for r_title, r_desc in rules:
        draw.text((pan_x + 15, ry), r_title, font=get_font(11, bold=True), fill=AMBER)
        ry += 20
        words = r_desc.split()
        line = ""
        for w in words:
            test_line = line + " " + w if line else w
            if draw.textlength(test_line, font=get_font(10)) < (pan_w - 45):
                line = test_line
            else:
                draw.text((pan_x + 15, ry), line, font=get_font(10), fill=TEXT_MAIN)
                ry += 16
                line = w
        if line:
            draw.text((pan_x + 15, ry), line, font=get_font(10), fill=TEXT_MAIN)
            ry += 24

    # Bottom summary bar
    draw.rectangle([(120, H - 230), (W - 45, H - 75)], fill=(15, 23, 42), outline=PANEL_BORDER, width=1)
    draw.text((140, H - 215), "SHEET 6 MANDATORY VERIFICATION GATES", font=get_font(12, bold=True), fill=GREEN)
    draw.text((140, H - 185), "• Secondary Fluid Chemistry: Refractometer confirmed 25.0% +/- 1.0% Propylene Glycol before test start.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((140, H - 160), "• VFD Manual Lockout: Speed fixed at 50.0 Hz (measured by optical tachometer or calibrated frequency inverter register).", font=get_font(11), fill=TEXT_MUTED)
    draw.text((140, H - 135), "• 4-Point Valve Throttling: Manually logged with calibrated differential pressure transmitter across supply/return manifolds.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((140, H - 110), "• Zero Thermal Contamination: Heat command interlocked to OFF. Fluid temperature drift <= 0.5 K throughout run.", font=get_font(11), fill=TEXT_MUTED)

    save_path = FIG_DIR / "fig-03-pump-curves-cold-vs-hot.png"
    img.save(save_path, "PNG")
    print(f"Saved: {save_path}")

# ==============================================================================
# DIAGRAM 4: Multi-Rack Secondary Distribution: Reverse-Return Hydraulics & Balance
# ==============================================================================
def draw_fig_04():
    img, draw = create_base_canvas(
        title="Multi-Cabinet Secondary Distribution Hydraulics: Reverse-Return Balancing",
        subtitle="Hydraulic Pressure Profiles Across 10-Rack Row: Direct-Return Starvation vs. Tichelmann Uniformity",
        sheet_ref="SHEET 1 & SHEET 3"
    )

    # Two rows: Top = Direct Return (Flawed), Bottom = Reverse Return (Standard)
    # 10 Racks each
    n_racks = 10
    rack_w = 110
    rack_h = 160
    start_x = 240
    gap_x = 35

    # TOP SECTION: Direct-Return (Direct Starvation)
    top_y = 150
    draw.rectangle([(50, top_y), (W - 50, top_y + 360)], fill=PANEL_BG, outline=RED, width=2)
    draw.rectangle([(50, top_y), (W - 50, top_y + 34)], fill=(35, 20, 26), outline=RED, width=1)
    draw.text((70, top_y + 8), "CASE A: DIRECT-RETURN CONFIGURATION (REJECTED: END-RACK STARVATION)", font=get_font(14, bold=True), fill=RED)
    draw.text((W - 380, top_y + 10), "CV = 14.8% (EXCEEDS 5.0% LIMIT)", font=get_font(12, bold=True), fill=RED)

    # CDU on left
    draw.rectangle([(75, top_y + 60), (195, top_y + 260)], fill=(20, 26, 38), outline=CYAN, width=2)
    draw.text((105, top_y + 140), "CDU-1", font=get_font(18, bold=True), fill=CYAN)
    draw.text((85, top_y + 175), "Supply / Return", font=get_font(11), fill=TEXT_MUTED)

    # Supply Header (Blue, on top of racks)
    draw.line([(195, top_y + 80), (start_x + (n_racks - 1) * (rack_w + gap_x) + rack_w, top_y + 80)], fill=BLUE, width=5)
    # Direct Return Header (Cyan, also returns from left!)
    draw.line([(195, top_y + 240), (start_x + (n_racks - 1) * (rack_w + gap_x) + rack_w, top_y + 240)], fill=CYAN, width=5)

    # Racks
    flows_direct = [128, 122, 115, 108, 101, 94, 88, 81, 74, 66] # LPM, rack 10 starved!
    for i in range(n_racks):
        rx = start_x + i * (rack_w + gap_x)
        ry = top_y + 95
        flow = flows_direct[i]
        c_fill = (22, 30, 44) if flow >= 90 else (45, 20, 26)
        c_outline = CYAN if flow >= 90 else RED

        draw.rectangle([(rx, ry), (rx + rack_w, ry + 130)], fill=c_fill, outline=c_outline, width=1)
        draw.text((rx + 15, ry + 10), f"RACK {i+1:02d}", font=get_font(11, bold=True), fill=TEXT_MAIN)
        draw.text((rx + 15, ry + 32), "120 kW LB", font=get_font(10), fill=TEXT_MUTED)

        # Flow indicator
        draw.text((rx + 15, ry + 60), f"{flow} LPM", font=get_font(13, bold=True), fill=(GREEN if flow >= 95 else RED))
        draw.text((rx + 15, ry + 85), f"dP: {140 - i*11} kPa", font=get_font(10), fill=TEXT_MUTED)

        # Pipe drops
        draw.line([(rx + 30, top_y + 80), (rx + 30, ry)], fill=BLUE, width=2)
        draw.line([(rx + 80, ry + 130), (rx + 80, top_y + 240)], fill=CYAN, width=2)

    # Explanation text for Direct Return
    draw.text((70, top_y + 285),
              "Diagnostic Analysis: Cumulative friction in Supply and Return headers compounds. Rack 01 sees lowest loop resistance (128 LPM, overflow); "
              "Rack 10 suffers severe starved flow (66 LPM, -34% deviation), triggering high-temp chip alarms during 100% thermal step test.",
              font=get_font(11), fill=TEXT_MUTED)

    # BOTTOM SECTION: Reverse-Return (Tichelmann System)
    bot_y = 540
    draw.rectangle([(50, bot_y), (W - 50, bot_y + 360)], fill=PANEL_BG, outline=GREEN, width=2)
    draw.rectangle([(50, bot_y), (W - 50, bot_y + 34)], fill=(16, 32, 26), outline=GREEN, width=1)
    draw.text((70, bot_y + 8), "CASE B: REVERSE-RETURN (TICHELMANN) BALANCED HYDRAULIC LOOP (ACCEPTED)", font=get_font(14, bold=True), fill=GREEN)
    draw.text((W - 380, bot_y + 10), "CV = 2.1% (NOMINAL ENVELOPE <= 5.0%)", font=get_font(12, bold=True), fill=GREEN)

    # CDU on left
    draw.rectangle([(75, bot_y + 60), (195, bot_y + 260)], fill=(20, 26, 38), outline=CYAN, width=2)
    draw.text((105, bot_y + 140), "CDU-1", font=get_font(18, bold=True), fill=CYAN)
    draw.text((85, bot_y + 175), "Supply / Return", font=get_font(11), fill=TEXT_MUTED)

    # Supply Header (Blue, left to right)
    draw.line([(195, bot_y + 80), (start_x + (n_racks - 1) * (rack_w + gap_x) + rack_w, bot_y + 80)], fill=BLUE, width=5)
    # Reverse Return Header: collects left to right, then returns along dedicated return trunk back to CDU!
    draw.line([(start_x, bot_y + 240), (start_x + (n_racks - 1) * (rack_w + gap_x) + rack_w, bot_y + 240)], fill=CYAN, width=5)
    # Loop back trunk to CDU
    draw.line([(start_x + (n_racks - 1) * (rack_w + gap_x) + rack_w, bot_y + 240),
               (start_x + (n_racks - 1) * (rack_w + gap_x) + rack_w + 30, bot_y + 240),
               (start_x + (n_racks - 1) * (rack_w + gap_x) + rack_w + 30, bot_y + 270),
               (195, bot_y + 270)], fill=CYAN, width=5)
    draw.text((W // 2 - 80, bot_y + 280), "Tichelmann Reverse Return Trunk (Equal Path Length L_tot)", font=get_font(11, bold=True), fill=CYAN)

    flows_reverse = [102, 101, 100, 99, 98, 98, 99, 100, 101, 102] # Uniform ~100 LPM!
    for i in range(n_racks):
        rx = start_x + i * (rack_w + gap_x)
        ry = bot_y + 95
        flow = flows_reverse[i]

        draw.rectangle([(rx, ry), (rx + rack_w, ry + 130)], fill=(18, 26, 38), outline=CYAN, width=1)
        draw.text((rx + 15, ry + 10), f"RACK {i+1:02d}", font=get_font(11, bold=True), fill=TEXT_MAIN)
        draw.text((rx + 15, ry + 32), "120 kW LB", font=get_font(10), fill=TEXT_MUTED)

        draw.text((rx + 15, ry + 60), f"{flow} LPM", font=get_font(13, bold=True), fill=GREEN)
        draw.text((rx + 15, ry + 85), "dP: 110 kPa", font=get_font(10), fill=TEXT_MUTED)

        # Pipe drops
        draw.line([(rx + 30, bot_y + 80), (rx + 30, ry)], fill=BLUE, width=2)
        draw.line([(rx + 80, ry + 130), (rx + 80, bot_y + 240)], fill=CYAN, width=2)

    draw.text((70, bot_y + 315),
              "Audit Verification: In reverse-return piping, total hydraulic circuit length (Supply run + Return run) is identical for all racks. "
              "Flow variation is tightly bounded (CV = 2.1% <= 5.0%). All racks receive uniform cooling within +/- 2.5% of design setpoint.",
              font=get_font(11), fill=TEXT_MUTED)

    # Bottom summary guidance
    draw.rectangle([(50, H - 75), (W - 50, H - 45)], fill=(15, 23, 42), outline=PANEL_BORDER, width=1)
    draw.text((70, H - 65), "COMMISSIONING RULE: Never accept an uncalibrated manifold row. Measure static pressure at ends of Supply & Return headers before Level 5 heat.",
              font=get_font(11, bold=True), fill=AMBER)

    save_path = FIG_DIR / "fig-04-multi-rack-manifold-hydraulics.png"
    img.save(save_path, "PNG")
    print(f"Saved: {save_path}")

# ==============================================================================
# DIAGRAM 5: Integrated Thermal Step Ladder & Dwell Equilibrium Dynamics
# ==============================================================================
def draw_fig_05():
    img, draw = create_base_canvas(
        title="Level 5 Integrated Thermal Step Ladder & Dwell Equilibrium",
        subtitle="Dynamic Temperature, Power, and Heat Rejection Response Across 0% to 110% Heat Test Protocol",
        sheet_ref="SHEET 3 (ONE HEAT STEP)"
    )

    # Graph canvas
    gx0, gy0 = 100, 180
    gw, gh = 1150, 560
    gx1, gy1 = gx0 + gw, gy0 + gh

    draw.rectangle([(gx0, gy0), (gx1, gy1)], fill=(16, 20, 28), outline=PANEL_BORDER, width=2)

    # Timeline intervals (0 to 12 hours)
    for h_mark in range(0, 13):
        x = gx0 + int(h_mark * gw / 12)
        draw.line([(x, gy0), (x, gy1)], fill=(28, 35, 48), width=1)
        draw.text((x - 15, gy1 + 10), f"{h_mark}h", font=get_font(11), fill=TEXT_MUTED)

    draw.text((gx0 + gw // 2 - 60, gy1 + 35), "Test Window Elapsed Time (Hours)", font=get_font(13, bold=True), fill=TEXT_MAIN)

    # Left Y-Axis: Thermal Load (0 to 1400 kW)
    for p_mark in range(0, 15, 2):
        y = gy1 - int((p_mark * 100 / 1400) * gh)
        draw.line([(gx0, y), (gx1, y)], fill=(28, 35, 48), width=1)
        draw.text((gx0 - 65, y - 8), f"{p_mark*100}kW", font=get_font(11), fill=CYAN)
    draw.text((gx0 - 80, gy0 - 30), "Electric Power (kW)", font=get_font(12, bold=True), fill=CYAN)

    # Right Y-Axis: Temperature (°C)
    for t_mark in range(20, 65, 5):
        y = gy1 - int(((t_mark - 20) / 45) * gh)
        draw.text((gx1 + 15, y - 8), f"{t_mark}°C", font=get_font(11), fill=AMBER)
    draw.text((gx1 + 15, gy0 - 30), "Fluid Temp (°C)", font=get_font(12, bold=True), fill=AMBER)

    # Simulation coordinates for Ladder steps:
    # 0h-1h: Cold baseline (0 kW, 20°C)
    # 1h-2.5h: 25% (300 kW, T_sup=33°C, T_ret=37°C)
    # 2.5h-4.5h: 50% (600 kW, T_sup=36°C, T_ret=42°C)
    # 4.5h-6.5h: 75% (900 kW, T_sup=38°C, T_ret=46°C)
    # 6.5h-10h: 100% Full Design (1200 kW, T_sup=40°C, T_ret=50°C, Dwell 3.5h)
    # 10h-11h: 110% Overload Margin (1320 kW, T_sup=42°C, T_ret=53°C)
    # 11h-12h: Shock Step-Down (30% 360 kW cooldown)

    time_steps = [
        (0.0, 0, 22.0, 22.0),
        (1.0, 0, 22.0, 22.0),
        (1.1, 300, 25.0, 28.0),
        (2.5, 300, 32.5, 36.5),
        (2.6, 600, 34.0, 39.0),
        (4.5, 600, 36.0, 42.0),
        (4.6, 900, 37.0, 44.0),
        (6.5, 900, 38.0, 46.5),
        (6.6, 1200, 39.0, 48.0),
        (10.0, 1200, 40.0, 50.0), # Stable equilibrium
        (10.1, 1320, 41.0, 52.0),
        (11.0, 1320, 42.0, 53.5),
        (11.1, 360, 35.0, 40.0),
        (12.0, 360, 30.0, 33.0)
    ]

    pts_power = []
    pts_tsup = []
    pts_tret = []

    for t, p, t_sup, t_ret in time_steps:
        px = gx0 + int((t / 12.0) * gw)
        py_p = gy1 - int((p / 1400.0) * gh)
        py_ts = gy1 - int(((t_sup - 20.0) / 45.0) * gh)
        py_tr = gy1 - int(((t_ret - 20.0) / 45.0) * gh)

        pts_power.append((px, py_p))
        pts_tsup.append((px, py_ts))
        pts_tret.append((px, py_tr))

    # Draw curves
    draw.line(pts_power, fill=CYAN, width=3)
    draw.line(pts_tsup, fill=BLUE, width=3)
    draw.line(pts_tret, fill=RED, width=3)

    # Labels on steps
    draw.text((gx0 + int(1.4/12*gw), gy1 - int(380/1400*gh)), "25% (300kW)", font=get_font(11, bold=True), fill=CYAN)
    draw.text((gx0 + int(3.0/12*gw), gy1 - int(680/1400*gh)), "50% (600kW)", font=get_font(11, bold=True), fill=CYAN)
    draw.text((gx0 + int(5.0/12*gw), gy1 - int(980/1400*gh)), "75% (900kW)", font=get_font(11, bold=True), fill=CYAN)
    draw.text((gx0 + int(7.8/12*gw), gy1 - int(1260/1400*gh)), "100% DESIGN LOAD (1200kW)", font=get_font(12, bold=True), fill=GREEN)
    draw.text((gx0 + int(10.1/12*gw), gy1 - int(1360/1400*gh)), "110% OVERLOAD", font=get_font(10, bold=True), fill=AMBER)

    # Equilibrium Dwell Marker box
    eq_x0 = gx0 + int(7.5/12*gw)
    eq_x1 = gx0 + int(10.0/12*gw)
    draw.rectangle([(eq_x0, gy0 + 50), (eq_x1, gy1 - 50)], outline=GREEN, width=1)
    draw.text((eq_x0 + 15, gy0 + 65), "THERMAL EQUILIBRIUM DWELL", font=get_font(11, bold=True), fill=GREEN)
    draw.text((eq_x0 + 15, gy0 + 85), "• Criteria: dT/dt <= 0.2 K / 10 min", font=get_font(10), fill=TEXT_MAIN)
    draw.text((eq_x0 + 15, gy0 + 105), "• Heat Rejection Closure >= 97%", font=get_font(10), fill=TEXT_MAIN)
    draw.text((eq_x0 + 15, gy0 + 125), "• Supply Temp: 40.0°C +/- 0.5°C", font=get_font(10), fill=TEXT_MAIN)

    # Right side Audit Check panel
    pan_x = gx1 + 70
    pan_y = gy0
    pan_w = W - pan_x - 55
    draw.rectangle([(pan_x, pan_y), (pan_x + pan_w, gy1)], fill=PANEL_BG, outline=CYAN, width=2)
    draw.rectangle([(pan_x, pan_y), (pan_x + pan_w, pan_y + 36)], fill=(20, 26, 38), outline=CYAN, width=1)
    draw.text((pan_x + 15, pan_y + 10), "SHEET 3 FIELD AUDIT CHECKLIST", font=get_font(13, bold=True), fill=CYAN)

    checks = [
        ("1. MINIMUM DWELL TIME", "Never advance to the next heat rung prematurely. 25-75% rungs require >= 45 min dwell. 100% full design load requires minimum 4.0 hours continuous steady-state operation."),
        ("2. ENTHALPY RECONCILIATION", "Calculate Q_liquid = m_dot * c_p * (T_ret - T_sup). Compare against P_elec (Class 0.2 meter). The ratio Q_liquid / P_elec must remain between 97.0% and 101.5%."),
        ("3. IR SCAN TERMINATION GATE", "At 30 minutes into the 100% step, perform infrared camera inspection of all busbar connections, breaker lugs, and power pins. Maximum allowable terminal temp: <= 75°C."),
        ("4. DEW POINT MARGIN", "Secondary supply temperature must continuously exceed the hall air dew point by >= 2.0 K. If T_sup approaches dew point, CDU mixing logic is defective.")
    ]
    cy = pan_y + 50
    for c_title, c_desc in checks:
        draw.text((pan_x + 15, cy), c_title, font=get_font(11, bold=True), fill=AMBER)
        cy += 20
        words = c_desc.split()
        line = ""
        for w in words:
            test_line = line + " " + w if line else w
            if draw.textlength(test_line, font=get_font(10)) < (pan_w - 45):
                line = test_line
            else:
                draw.text((pan_x + 15, cy), line, font=get_font(10), fill=TEXT_MAIN)
                cy += 16
                line = w
        if line:
            draw.text((pan_x + 15, cy), line, font=get_font(10), fill=TEXT_MAIN)
            cy += 24

    # Bottom legend
    draw.rectangle([(100, H - 230), (W - 30, H - 75)], fill=(15, 23, 42), outline=PANEL_BORDER, width=1)
    draw.text((120, H - 215), "PARAMETER LEGEND & WITNESS ENVELOPE", font=get_font(12, bold=True), fill=TEXT_MAIN)
    # cyan line
    draw.line([(120, H - 180), (160, H - 180)], fill=CYAN, width=3)
    draw.text((170, H - 186), "P_elec: Total Active Electrical Load (kW)", font=get_font(11), fill=CYAN)
    # red line
    draw.line([(550, H - 180), (590, H - 180)], fill=RED, width=3)
    draw.text((600, H - 186), "TCS Return Temp (°C) [Limit: <= 52.0°C]", font=get_font(11), fill=RED)
    # blue line
    draw.line([(980, H - 180), (1020, H - 180)], fill=BLUE, width=3)
    draw.text((1030, H - 186), "TCS Supply Temp (°C) [Setpoint: 40.0°C +/- 0.5°C]", font=get_font(11), fill=BLUE)

    draw.text((120, H - 145), "FAILURE CONDITION: If TCS Return Temp breaches 53.0°C or secondary flow drops below 90% of nominal during dwell,", font=get_font(11), fill=AMBER)
    draw.text((120, H - 125), "the test must be immediately paused and held at 50% load until root cause is diagnosed. Never allow thermal runaway.", font=get_font(11), fill=TEXT_MUTED)

    save_path = FIG_DIR / "fig-05-thermal-ladder-and-dwell.png"
    img.save(save_path, "PNG")
    print(f"Saved: {save_path}")

# ==============================================================================
# DIAGRAM 6: Dynamic Failure Mode Response & Autonomous Control Ride-Through
# ==============================================================================
def draw_fig_06():
    img, draw = create_base_canvas(
        title="Dynamic Failure Mode Verification & Autonomous Control Ride-Through",
        subtitle="Transient Oscillograms for Pump Trip, 2N Power Loss, Primary Source Interruption, and BMS Cut",
        sheet_ref="SHEET 4 (FAILURES)"
    )

    # 4 Quadrants:
    # Top-Left: Scenario 1 - Secondary Pump A Trip & Auto-Changeover to Pump B
    # Top-Right: Scenario 2 - 2N Feeder A Loss / ATS Transfer
    # Bottom-Left: Scenario 3 - Primary Facility Water Loss (Thermal Ride-Through)
    # Bottom-Right: Scenario 4 - BMS Comms Loss / PLC Autonomous Local Fallback

    quad_w = 810
    quad_h = 370

    quads = [
        ("SCENARIO 1: SECONDARY PUMP TRIP & N+1 SWAP", 50, 140, CYAN),
        ("SCENARIO 2: 2N FEEDER A LOSS / STS TRANSFER", 940, 140, BLUE),
        ("SCENARIO 3: PRIMARY CHILLED WATER LOSS (FWS CUT)", 50, 540, RED),
        ("SCENARIO 4: BMS COMMUNICATION SEVERANCE", 940, 540, PURPLE)
    ]

    for title_q, qx, qy, col in quads:
        draw.rectangle([(qx, qy), (qx + quad_w, qy + quad_h)], fill=PANEL_BG, outline=col, width=2)
        draw.rectangle([(qx, qy), (qx + quad_w, qy + 32)], fill=(20, 26, 38), outline=col, width=1)
        draw.text((qx + 15, qy + 8), title_q, font=get_font(13, bold=True), fill=col)

    # ================= Scenario 1 (Pump Trip) =================
    # Oscillogram: Pump speed A drops 100->0, Pump speed B rises 0->100 in 1.2s
    # Pressure dP dips from 220 kPa to 110 kPa then recovers
    ox, oy = 70, 200
    ow, oh = 480, 260
    draw.rectangle([(ox, oy), (ox + ow, oy + oh)], fill=(16, 20, 28), outline=PANEL_BORDER, width=1)
    draw.line([(ox + 120, oy), (ox + 120, oy + oh)], fill=AMBER, width=1) # trip injection line
    draw.text((ox + 125, oy + 10), "TRIP INJECTED", font=get_font(10, bold=True), fill=AMBER)

    # Pump A speed curve (drops)
    pts_pa = [(ox, oy + 40), (ox + 120, oy + 40), (ox + 150, oy + oh - 20), (ox + ow, oy + oh - 20)]
    draw.line(pts_pa, fill=RED, width=2)
    draw.text((ox + 20, oy + 25), "Pump A VFD (Lead)", font=get_font(10), fill=RED)

    # Pump B speed curve (rises)
    pts_pb = [(ox, oy + oh - 20), (ox + 130, oy + oh - 20), (ox + 180, oy + 40), (ox + ow, oy + 40)]
    draw.line(pts_pb, fill=GREEN, width=2)
    draw.text((ox + ow - 130, oy + 25), "Pump B VFD (Lag)", font=get_font(10), fill=GREEN)

    # Pressure curve (dips and recovers)
    pts_dp = [(ox, oy + 80), (ox + 120, oy + 80), (ox + 150, oy + 180), (ox + 190, oy + 90), (ox + ow, oy + 80)]
    draw.line(pts_dp, fill=CYAN, width=3)
    draw.text((ox + ow - 160, oy + 95), "Secondary dP (220 kPa)", font=get_font(10), fill=CYAN)

    # Text criteria on right of Q1
    draw.text((ox + ow + 20, oy + 10), "ACCEPTANCE LIMITS:", font=get_font(11, bold=True), fill=TEXT_MAIN)
    draw.text((ox + ow + 20, oy + 35), "• Changeover Delay: <= 1.5 s", font=get_font(10), fill=GREEN)
    draw.text((ox + ow + 20, oy + 55), "• Min Loop dP: >= 100 kPa", font=get_font(10), fill=GREEN)
    draw.text((ox + ow + 20, oy + 75), "• Zero cavitation in pump head", font=get_font(10), fill=TEXT_MUTED)
    draw.text((ox + ow + 20, oy + 105), "AUDIT NOTE:", font=get_font(11, bold=True), fill=AMBER)
    draw.text((ox + ow + 20, oy + 125), "Check valve slam must not exceed", font=get_font(10), fill=TEXT_MUTED)
    draw.text((ox + ow + 20, oy + 145), "+/- 50 kPa water hammer pulse.", font=get_font(10), fill=TEXT_MUTED)
    draw.text((ox + ow + 20, oy + 165), "Flow must recover before LB trip.", font=get_font(10), fill=TEXT_MUTED)

    # ================= Scenario 2 (2N Power Loss) =================
    ox2, oy2 = 960, 200
    draw.rectangle([(ox2, oy2), (ox2 + ow, oy2 + oh)], fill=(16, 20, 28), outline=PANEL_BORDER, width=1)
    draw.line([(ox2 + 120, oy2), (ox2 + 120, oy2 + oh)], fill=RED, width=1)
    draw.text((ox2 + 125, oy2 + 10), "FEEDER A KILLED", font=get_font(10, bold=True), fill=RED)

    # Feeder A Voltage drops to 0
    pts_va = [(ox2, oy2 + 40), (ox2 + 120, oy2 + 40), (ox2 + 125, oy2 + oh - 20), (ox2 + ow, oy2 + oh - 20)]
    draw.line(pts_va, fill=RED, width=2)
    draw.text((ox2 + 20, oy2 + 25), "Feeder A Voltage (0V)", font=get_font(10), fill=RED)

    # Feeder B Voltage holds 400V
    draw.line([(ox2, oy2 + 60), (ox2 + ow, oy2 + 60)], fill=BLUE, width=2)
    draw.text((ox2 + ow - 140, oy2 + 45), "Feeder B Active (400V)", font=get_font(10), fill=BLUE)

    # CDU PLC Control Bus 24VDC (Zero Dip via Buffer Capacitor / UPS)
    draw.line([(ox2, oy2 + 120), (ox2 + ow, oy2 + 120)], fill=GREEN, width=3)
    draw.text((ox2 + ow - 170, oy2 + 105), "CDU 24VDC Bus (Zero Dip)", font=get_font(10), fill=GREEN)

    draw.text((ox2 + ow + 20, oy2 + 10), "ACCEPTANCE LIMITS:", font=get_font(11, bold=True), fill=TEXT_MAIN)
    draw.text((ox2 + ow + 20, oy2 + 35), "• Transfer Time: <= 16 ms", font=get_font(10), fill=GREEN)
    draw.text((ox2 + ow + 20, oy2 + 55), "• PLC Reboot: ZERO (Prohibited)", font=get_font(10), fill=GREEN)
    draw.text((ox2 + ow + 20, oy2 + 75), "• Pump VFD ride-through verified", font=get_font(10), fill=TEXT_MUTED)
    draw.text((ox2 + ow + 20, oy2 + 105), "AUDIT NOTE:", font=get_font(11, bold=True), fill=AMBER)
    draw.text((ox2 + ow + 20, oy2 + 125), "If CDU PLC reboots during ATS", font=get_font(10), fill=TEXT_MUTED)
    draw.text((ox2 + ow + 20, oy2 + 145), "transfer, Level 5 test is FAILED.", font=get_font(10), fill=TEXT_MUTED)
    draw.text((ox2 + ow + 20, oy2 + 165), "24V DC buffer PSU is required.", font=get_font(10), fill=TEXT_MUTED)

    # ================= Scenario 3 (Primary Water Loss) =================
    ox3, oy3 = 70, 600
    draw.rectangle([(ox3, oy3), (ox3 + ow, oy3 + oh)], fill=(16, 20, 28), outline=PANEL_BORDER, width=1)
    draw.line([(ox3 + 100, oy3), (ox3 + 100, oy3 + oh)], fill=RED, width=1)
    draw.text((ox3 + 105, oy3 + 10), "FWS VALVE ISOLATED", font=get_font(10, bold=True), fill=RED)

    # Primary flow drops to zero
    draw.line([(ox3, oy3 + 50), (ox3 + 100, oy3 + 50), (ox3 + 120, oy3 + oh - 20), (ox3 + ow, oy3 + oh - 20)], fill=BLUE, width=2)
    draw.text((ox3 + 20, oy3 + 35), "Primary Flow (0 m³/h)", font=get_font(10), fill=BLUE)

    # Secondary Temp rises steadily (Thermal Inertia)
    pts_t_rise = [(ox3, oy3 + 180), (ox3 + 100, oy3 + 180), (ox3 + ow - 40, oy3 + 40)]
    draw.line(pts_t_rise, fill=RED, width=3)
    draw.text((ox3 + ow - 190, oy3 + 30), "TCS Supply Temp (+0.35 K/s)", font=get_font(10, bold=True), fill=RED)

    # Trip limit line at 48°C
    draw.line([(ox3, oy3 + 70), (ox3 + ow, oy3 + 70)], fill=AMBER, width=1)
    draw.text((ox3 + 10, oy3 + 75), "Alarm Threshold 45.0°C", font=get_font(10), fill=AMBER)

    draw.text((ox3 + ow + 20, oy3 + 10), "THERMAL INERTIA RULER:", font=get_font(11, bold=True), fill=TEXT_MAIN)
    draw.text((ox3 + ow + 20, oy3 + 35), "• Buffer Time to 45°C: >= 40 s", font=get_font(10), fill=GREEN)
    draw.text((ox3 + ow + 20, oy3 + 55), "• Controlled Load Shed triggered", font=get_font(10), fill=GREEN)
    draw.text((ox3 + ow + 20, oy3 + 75), "• CDU TCV drives to 100% open", font=get_font(10), fill=TEXT_MUTED)
    draw.text((ox3 + ow + 20, oy3 + 105), "AUDIT NOTE:", font=get_font(11, bold=True), fill=AMBER)
    draw.text((ox3 + ow + 20, oy3 + 125), "Calculated loop volume determines", font=get_font(10), fill=TEXT_MUTED)
    draw.text((ox3 + ow + 20, oy3 + 145), "ride-through envelope: M*cp*dT.", font=get_font(10), fill=TEXT_MUTED)
    draw.text((ox3 + ow + 20, oy3 + 165), "Emergency cut before 50.0°C.", font=get_font(10), fill=TEXT_MUTED)

    # ================= Scenario 4 (BMS Cut) =================
    ox4, oy4 = 960, 600
    draw.rectangle([(ox4, oy4), (ox4 + ow, oy4 + oh)], fill=(16, 20, 28), outline=PANEL_BORDER, width=1)
    draw.line([(ox4 + 120, oy4), (ox4 + 120, oy4 + oh)], fill=PURPLE, width=1)
    draw.text((ox4 + 125, oy4 + 10), "MODBUS/BACNET CUT", font=get_font(10, bold=True), fill=PURPLE)

    # BMS Heartbeat drops
    draw.line([(ox4, oy4 + 50), (ox4 + 120, oy4 + 50), (ox4 + 125, oy4 + oh - 20), (ox4 + ow, oy4 + oh - 20)], fill=PURPLE, width=2)
    draw.text((ox4 + 20, oy4 + 35), "BMS Telemetry Comm Link (0)", font=get_font(10), fill=PURPLE)

    # Local PLC keeps pump speed and valve position constant
    draw.line([(ox4, oy4 + 110), (ox4 + ow, oy4 + 110)], fill=GREEN, width=3)
    draw.text((ox4 + ow - 190, oy4 + 95), "Local Loop Control Stable (40°C)", font=get_font(10), fill=GREEN)

    draw.text((ox4 + ow + 20, oy4 + 10), "ACCEPTANCE LIMITS:", font=get_font(11, bold=True), fill=TEXT_MAIN)
    draw.text((ox4 + ow + 20, oy4 + 35), "• Autonomous Fail-Safe: PASS", font=get_font(10), fill=GREEN)
    draw.text((ox4 + ow + 20, oy4 + 55), "• Valve Hunting: ZERO", font=get_font(10), fill=GREEN)
    draw.text((ox4 + ow + 20, oy4 + 75), "• Local alarm buzzer activated", font=get_font(10), fill=TEXT_MUTED)
    draw.text((ox4 + ow + 20, oy4 + 105), "AUDIT NOTE:", font=get_font(11, bold=True), fill=AMBER)
    draw.text((ox4 + ow + 20, oy4 + 125), "CDU must never depend on BMS to", font=get_font(10), fill=TEXT_MUTED)
    draw.text((ox4 + ow + 20, oy4 + 145), "survive. Local PLC handles PID", font=get_font(10), fill=TEXT_MUTED)
    draw.text((ox4 + ow + 20, oy4 + 165), "loops autonomously without cloud.", font=get_font(10), fill=TEXT_MUTED)

    # Bottom strip
    draw.rectangle([(50, H - 75), (W - 50, H - 45)], fill=(15, 23, 42), outline=PANEL_BORDER, width=1)
    draw.text((70, H - 65), "WITNESS PROTOCOL: Every transient test must record pre-event baseline, peak transient deflection, and time-to-steady-state.",
              font=get_font(11, bold=True), fill=AMBER)

    save_path = FIG_DIR / "fig-06-transient-failure-scenarios.png"
    img.save(save_path, "PNG")
    print(f"Saved: {save_path}")

# ==============================================================================
# DIAGRAM 7: Commissioning Punch List Category & Priority Governance Matrix
# ==============================================================================
def draw_fig_07():
    img, draw = create_base_canvas(
        title="Commissioning Punch List Governance & Defect Life-Cycle Matrix",
        subtitle="Defect Classification, Interlock Escalation, Root-Cause Rectification, and Witness Sign-Off Workflow",
        sheet_ref="PUNCH LIST REGISTER"
    )

    # Three Tier Cards horizontally
    col_w = 540
    start_x = 55
    gap_x = 30
    card_y = 150
    card_h = 520

    tiers = [
        ("CATEGORY 1: CRITICAL BLOCKER",
         "LIFE SAFETY, STRUCTURAL & HYDRAULIC BLOCKERS",
         RED,
         [
             ("DEFINITION", "Any condition causing life safety hazard, permanent mechanical damage, uncontrolled liquid leak, or electrical arc hazard."),
             ("TYPICAL FINDINGS", "• Fitting leak > 0 drops/min during hydrostatic hold\n• Phase rotation inverted (reverse pump rotation)\n• Emergency Stop button fails to trip contactor\n• Pump trip failover delay exceeds 1.5 seconds\n• Megger insulation resistance < 100 MOhm"),
             ("STAGE INTERLOCK", "ABSOLUTE HARD STOP. Prohibits progression to the next commissioning level. Level 5 heat command strictly blocked."),
             ("RESOLUTION SLA", "Immediate stop of shift. Mandatory root-cause engineering review. Requires 100% witness re-test before sign-off.")
         ]),
        ("CATEGORY 2: MAJOR OPERABILITY",
         "CAPACITY, BALANCE & CONTROL DEVIATIONS",
         AMBER,
         [
             ("DEFINITION", "System functions safely but fails design performance tolerances, heat closure criteria, or control stability envelopes."),
             ("TYPICAL FINDINGS", "• Enthalpy closure ratio < 97.0% at 100% load\n• Multi-rack flow uniformity CV > 5.0%\n• Secondary supply temp oscillation > +/- 1.0 K\n• BMS telemetry point discrepancy > 0.5 K\n• Check valve reverse leakage detectable"),
             ("STAGE INTERLOCK", "CONDITIONAL PROGRESSION. Allowed only if Owner PE signs explicit deviation waiver with mitigation protocol."),
             ("RESOLUTION SLA", "14 Calendar Days. Retest required for specific failed sub-system during scheduled retest window.")
         ]),
        ("CATEGORY 3: MINOR COSMETIC",
         "DOCUMENTATION, LABELS & SECONDARY PUNCH",
         GREEN,
         [
             ("DEFINITION", "Non-operational cosmetic defect, missing asset identification tag, or minor documentation omission."),
             ("TYPICAL FINDINGS", "• Pipe labeling arrow missing or inverted\n• Cable management tray scratch or paint chip\n• Instrument calibration sticker smudged\n• Filter DP gauge glass cover dirty\n• Spare fuse kit storage compartment unlatched"),
             ("STAGE INTERLOCK", "NO INTERLOCK. Does not impede Level 4 FPT or Level 5 IST execution. Permitted to proceed to handover."),
             ("RESOLUTION SLA", "30 Calendar Days post-turnover. Verified via photographic evidence in closeout punch register.")
         ])
    ]

    for i, (t_title, t_sub, t_col, sections) in enumerate(tiers):
        cx = start_x + i * (col_w + gap_x)
        draw.rectangle([(cx, card_y), (cx + col_w, card_y + card_h)], fill=PANEL_BG, outline=t_col, width=2)
        draw.rectangle([(cx, card_y), (cx + col_w, card_y + 40)], fill=(20, 26, 38), outline=t_col, width=1)
        draw.text((cx + 15, card_y + 10), t_title, font=get_font(13, bold=True), fill=t_col)
        draw.text((cx + 15, card_y + 48), t_sub, font=get_font(10, bold=True), fill=TEXT_MUTED)

        sy = card_y + 75
        for s_head, s_body in sections:
            draw.rectangle([(cx + 12, sy), (cx + col_w - 12, sy + 22)], fill=(28, 35, 48), outline=t_col, width=1)
            draw.text((cx + 18, sy + 4), s_head, font=get_font(10, bold=True), fill=t_col)
            sy += 28

            # Word wrap body
            lines = s_body.split("\n")
            for l in lines:
                words = l.split(" ")
                cur_line = ""
                for w in words:
                    test_line = cur_line + " " + w if cur_line else w
                    if draw.textlength(test_line, font=get_font(10)) < (col_w - 36):
                        cur_line = test_line
                    else:
                        draw.text((cx + 18, sy), cur_line, font=get_font(10), fill=TEXT_MAIN)
                        sy += 16
                        cur_line = w
                if cur_line:
                    draw.text((cx + 18, sy), cur_line, font=get_font(10), fill=TEXT_MAIN)
                    sy += 18
            sy += 8

    # Bottom Defect Resolution Workflow Lifecycle Banner
    wf_y = 690
    draw.rectangle([(55, wf_y), (W - 55, H - 75)], fill=PANEL_BG, outline=PANEL_BORDER, width=2)
    draw.rectangle([(55, wf_y), (W - 55, wf_y + 36)], fill=(20, 26, 38), outline=PANEL_BORDER, width=1)
    draw.text((75, wf_y + 8), "MANDATORY DEFECT RESOLUTION LIFECYCLE (ISO / ASHRAE CLOSEOUT AUDIT)", font=get_font(13, bold=True), fill=CYAN)

    steps = [
        ("1. LOGGED IN REGISTER", "Logged within 2 hours of occurrence with photo, timestamp, P&ID tag, and script step ref."),
        ("2. ROOT CAUSE AUDIT", "Mechanical / Electrical contractor provides written root cause analysis, not temporary patch."),
        ("3. REMEDIATION", "Contractor executes repair under formal hot-work or mechanical pipe isolation permit."),
        ("4. WITNESS RETEST", "Joint re-test executed with Verification Lead and Owner representative present."),
        ("5. FORMAL CLOSEOUT", "Item closed in register with retest data sheet attached and dual ink signatures.")
    ]

    sw = 318
    for s_idx, (stitle, sdesc) in enumerate(steps):
        sx = 75 + s_idx * (sw + 15)
        sy = wf_y + 55
        draw.rectangle([(sx, sy), (sx + sw, sy + 250)], fill=(16, 20, 28), outline=CYAN, width=1)
        draw.rectangle([(sx, sy), (sx + sw, sy + 30)], fill=(26, 34, 48), outline=CYAN, width=1)
        draw.text((sx + 8, sy + 7), stitle, font=get_font(10, bold=True), fill=CYAN)

        words = sdesc.split(" ")
        cur_line = ""
        ty = sy + 40
        for w in words:
            test_line = cur_line + " " + w if cur_line else w
            if draw.textlength(test_line, font=get_font(10)) < (sw - 20):
                cur_line = test_line
            else:
                draw.text((sx + 8, ty), cur_line, font=get_font(10), fill=TEXT_MAIN)
                ty += 16
                cur_line = w
        if cur_line:
            draw.text((sx + 8, ty), cur_line, font=get_font(10), fill=TEXT_MAIN)

    save_path = FIG_DIR / "fig-07-punchlist-governance-matrix.png"
    img.save(save_path, "PNG")
    print(f"Saved: {save_path}")

def main():
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    print("Generating Flagship Engineering Diagrams for Book 03...")
    draw_fig_01()
    draw_fig_02()
    draw_fig_03()
    draw_fig_04()
    draw_fig_05()
    draw_fig_06()
    draw_fig_07()
    print("All 7 Engineering Diagrams successfully generated!")

if __name__ == "__main__":
    main()
