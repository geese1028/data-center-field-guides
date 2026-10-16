#!/usr/bin/env python3
"""
Generate Flagship High-Resolution Engineering Diagrams for Book 05:
Run the Data Center Day: What the manager must sign before the shift ends

Output directory: books/05-run-the-day/figures/
Resolution: 1800 x 1100 px, 300 DPI aesthetic, high-contrast industrial vector style.
Colors: Dark slate theme (BG: #12151c, Card: #1a202c, Cyan: #00e5ff, Blue: #2979ff,
        Orange/Warning: #ff9100, Green/Pass: #00e676, Red/Fail: #ff1744, White: #ffffff).
"""

import math
import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path("/Users/geese/Downloads/book/books/05-run-the-day")
FIG_DIR = ROOT / "figures"
FONT_DIR = Path("/Users/geese/Downloads/book/books/01-liquid-load-bank/fonts")

# Palette constants
BG_COLOR = (18, 21, 28)          # #12151c Deep charcoal slate
PANEL_BG = (26, 32, 44)          # #1a202c Technical card surface
PANEL_BORDER = (45, 55, 72)      # #2d3748 Border outline
GRID_COLOR = (30, 36, 48)        # Subtle coordinate grid
TEXT_MAIN = (255, 255, 255)      # Pure white
TEXT_MUTED = (160, 174, 192)     # Cool silver grey
CYAN = (0, 229, 255)             # Accent cyan (Cooling / Operations)
BLUE = (41, 121, 255)            # Primary blue (Power / Baseline)
AMBER = (255, 171, 0)            # Warning / Impairments / MOP Change
RED = (255, 23, 68)              # Failure / Incidents / Lockout
GREEN = (0, 230, 118)            # Pass / Healthy / Handover Cleared
PURPLE = (179, 136, 255)         # Governance / Capacity / Contracts

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
        draw.line([(cx, cy), (cx + dy, cy)], fill=CYAN, width=3)

    # 3. Header Banner
    draw.rectangle([(30, 30), (W - 30, 110)], fill=PANEL_BG, outline=PANEL_BORDER, width=2)
    draw.text((50, 42), "FIELD GUIDE 05 // DATA CENTER OPERATIONS & SHIFT GOVERNANCE", font=get_font(15, bold=True), fill=CYAN)
    draw.text((50, 68), title.upper(), font=get_font(24, bold=True), fill=TEXT_MAIN)
    draw.text((50, 96), subtitle, font=get_font(13, bold=False), fill=TEXT_MUTED)

    if sheet_ref:
        s_box_w = 310
        draw.rectangle([(W - 45 - s_box_w, 42), (W - 45, 98)], fill=(15, 23, 42), outline=CYAN, width=1)
        draw.text((W - 35 - s_box_w, 52), "REFERENCED MASTER FORM", font=get_font(11, bold=True), fill=AMBER)
        draw.text((W - 35 - s_box_w, 72), sheet_ref, font=get_font(13, bold=True), fill=CYAN)

    # 4. Footer Status Bar
    draw.rectangle([(30, H - 55), (W - 30, H - 30)], fill=PANEL_BG, outline=PANEL_BORDER, width=1)
    draw.text((50, H - 48), "MISSION-CRITICAL OPERATIONS // UPTIME INSTITUTE M&O // ZERO UNLOGGED IMPAIRMENTS // RIGOROUS SIGN-OFF",
              font=get_font(12, bold=False), fill=TEXT_MUTED)
    footer_tag = "TRISTAN DATA CENTER FIELD GUIDES // ED. 2026"
    ftw = draw.textlength(footer_tag, font=get_font(12, bold=True))
    draw.text((W - 80 - ftw, H - 48), footer_tag, font=get_font(12, bold=True), fill=CYAN)

    return img, draw

# ==============================================================================
# DIAGRAM 1: Data Center 24-Hour Shift Lifecycle & Bilateral Handover Protocol
# ==============================================================================
def draw_fig_01():
    img, draw = create_base_canvas(
        title="24-Hour Shift Lifecycle & Bilateral Handover Governance",
        subtitle="Chronological Rhythm: Shift Briefing, Routine Rounds, MOP Windows, Joint Walkthrough, and Handover Sign-Off",
        sheet_ref="DAY SHEET: BEFORE & CLOSE"
    )

    # Horizontal timeline of 24-hour cycle: Day Shift (08:00 - 20:00) vs Night Shift (20:00 - 08:00)
    phases = [
        ("07:30 - 08:00", "Bilateral Joint Walkthrough", "Pre-Shift Handover Gate",
         ["• Joint physical inspection of plant", "• Active alarms & bypassed zones", "• Review open permits & MOP tickets", "• Dual ink signature on Day Sheet"],
         CYAN),
        ("08:00 - 10:00", "Morning Operational Round", "Routine Verification (SOP)",
         ["• MV/LV switchgear & transformer inspection", "• UPS battery float voltage audit", "• Chilled water & CDU loop pressures", "• Log all anomalies in Issues Register"],
         BLUE),
        ("10:00 - 16:00", "High-Risk Maintenance (MOP)", "Approved Change Windows",
         ["• Vendor escort & access authorization", "• Pre-task risk briefing & LOTO", "• Mandatory Rollback plan on site", "• Live telemetry monitoring during work"],
         AMBER),
        ("16:00 - 18:00", "Afternoon Capacity Audit", "Energy & Redundancy Check",
         ["• Audit 2N power loading (< 45% rule)", "• PUE / WUE shift calculation", "• Close out completed work permits", "• Verify plant restored to normal state"],
         PURPLE),
        ("19:30 - 20:00", "Evening Handover & Turnover", "End-of-Shift Sign-Off",
         ["• Bilateral handover to Night Shift", "• Unresolved impairments passed on", "• Single verifiable sentence signed", "• Handover binder locked in safe"],
         GREEN)
    ]

    card_w = 320
    gap = 25
    start_x = 55
    card_y = 150
    card_h = 430

    for i, (t_range, title, sub, bullets, border_c) in enumerate(phases):
        cx = start_x + i * (card_w + gap)
        draw.rectangle([(cx, card_y), (cx + card_w, card_y + card_h)], fill=PANEL_BG, outline=border_c, width=2)
        draw.rectangle([(cx, card_y), (cx + card_w, card_y + 38)], fill=(20, 26, 38), outline=border_c, width=1)
        draw.text((cx + 15, card_y + 10), t_range, font=get_font(13, bold=True), fill=border_c)

        draw.text((cx + 15, card_y + 48), title, font=get_font(13, bold=True), fill=TEXT_MAIN)
        draw.text((cx + 15, card_y + 70), sub, font=get_font(10, bold=True), fill=TEXT_MUTED)
        draw.line([(cx + 12, card_y + 92), (cx + card_w - 12, card_y + 92)], fill=PANEL_BORDER, width=1)

        by = card_y + 108
        for b in bullets:
            draw.text((cx + 12, by), b, font=get_font(11), fill=TEXT_MAIN)
            by += 40

        # Bottom gate marker
        draw.rectangle([(cx + 15, card_y + card_h - 45), (cx + card_w - 15, card_y + card_h - 15)],
                       fill=(15, 23, 42), outline=border_c, width=1)
        draw.text((cx + 25, card_y + card_h - 35), f"MILESTONE {i+1}: COMPLETE", font=get_font(10, bold=True), fill=border_c)

        if i < len(phases) - 1:
            arrow_x = cx + card_w + 5
            arrow_y = card_y + card_h // 2
            draw.polygon([(arrow_x, arrow_y - 8), (arrow_x + 15, arrow_y), (arrow_x, arrow_y + 8)], fill=CYAN)

    # Lower Section: The Three Iron Laws of Shift Handover
    rule_y = 610
    draw.rectangle([(45, rule_y), (W - 45, H - 75)], fill=PANEL_BG, outline=PANEL_BORDER, width=2)
    draw.rectangle([(45, rule_y), (W - 45, rule_y + 36)], fill=(20, 26, 38), outline=PANEL_BORDER, width=1)
    draw.text((65, rule_y + 8), "THE THREE GOVERNING LAWS OF DATA CENTER SHIFT TURNOVER", font=get_font(14, bold=True), fill=AMBER)

    laws = [
        ("LAW 1: ZERO SILENT IMPAIRMENTS",
         "An unlogged impairment is an immediate disciplinary violation. If an alarm point was masked, a fire zone isolated, a cooling valve locked in manual, or a breaker bypassed during your shift, it must be documented in bold ink on the Day Sheet. Carrying an unlogged defect into the next shift is how minor maintenance becomes a catastrophic facility blackout.",
         RED),
        ("LAW 2: THE PHYSICAL WALKTHROUGH IS SACRED",
         "Never sign a shift handover sitting in the control room. Both incoming and outgoing shift managers must physically walk the plant together: inspect the battery room for thermal anomalies, smell the switchgear corridors for ozone/burning insulation, and verify CDU expansion tank levels with your own eyes before picking up the pen.",
         CYAN),
        ("LAW 3: THE SINGLE SIGNED SENTENCE",
         "The shift manager signs exactly one auditable sentence before clocking out: 'The facility infrastructure has been verified in compliance with SLA terms, with [X] documented impairments and zero unlogged alarms.' If you cannot truthfully sign that sentence, the shift is not handed over and you do not leave the facility.",
         GREEN)
    ]

    law_w = 540
    for j, (ltitle, ldesc, lcol) in enumerate(laws):
        lx = 65 + j * (law_w + 25)
        ly = rule_y + 55
        draw.rectangle([(lx, ly), (lx + law_w, ly + 310)], fill=(18, 22, 32), outline=lcol, width=1)
        draw.rectangle([(lx, ly), (lx + law_w, ly + 34)], fill=(26, 32, 44), outline=lcol, width=1)
        draw.text((lx + 12, ly + 8), ltitle, font=get_font(13, bold=True), fill=lcol)

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

    save_path = FIG_DIR / "fig-01-shift-lifecycle-and-handover.png"
    img.save(save_path, "PNG")
    print(f"Saved: {save_path}")

# ==============================================================================
# DIAGRAM 2: SOP, MOP, EOP Operational Hierarchy & Risk Gating
# ==============================================================================
def draw_fig_02():
    img, draw = create_base_canvas(
        title="Data Center Operational Procedure Hierarchy: SOP, MOP, and EOP",
        subtitle="Standard Operations (SOP), Method of Procedure (MOP) Change Control, and Emergency Operations (EOP)",
        sheet_ref="DAY SHEET: WORK & CHANGE"
    )

    # 3 Large Tier Columns
    col_w = 540
    start_x = 55
    gap_x = 30
    card_y = 150
    card_h = 520

    tiers = [
        ("SOP: STANDARD OPERATING PROCEDURE",
         "ROUTINE, REPEATABLE, LOW-RISK BASELINE TASKS",
         CYAN,
         [
             ("SCOPE & PURPOSE", "Governs daily baseline operational routines: shift inspection rounds, air filter differential pressure checks, demineralized water top-off, and routine visual logs."),
             ("AUTHORIZATION LEVEL", "Executed by qualified shift technicians under general supervisor oversight. Requires zero client pre-notification if facility redundancy is untouched."),
             ("MANDATORY PREREQUISITES", "• Active electrical/refrigeration trade license\n• Standard PPE (safety boots, safety glasses)\n• Pre-printed shift inspection checklist (Sheet 1)"),
             ("FAILURE PROTOCOL", "Any parameter out of band is flagged immediately on the master Issues Log; escalate to MOP or EOP if safety is compromised.")
         ]),
        ("MOP: METHOD OF PROCEDURE",
         "HIGH-RISK MAINTENANCE, SWITCHING & PHYSICAL CHANGES",
         AMBER,
         [
             ("SCOPE & PURPOSE", "Governs intrusive maintenance and configuration adjustments: electrical breaker switching, transformer oil sampling, CDU pump maintenance, firmware updates."),
             ("AUTHORIZATION LEVEL", "Requires Multi-Tier Change Advisory Board (CAB) sign-off, Facility Director approval, and client SLA notification 7-14 days in advance."),
             ("MANDATORY PREREQUISITES", "• Approved MOP with step-by-step instructions\n• Non-negotiable written Rollback / Back-out plan\n• Physical LOTO and active work permit in hand\n• Dedicated Safety Observer (Two-person rule)"),
             ("FAILURE PROTOCOL", "If an operation exceeds the time window or an unexpected transient occurs, execute the Rollback Plan immediately. Never improvise.")
         ]),
        ("EOP: EMERGENCY OPERATING PROCEDURE",
         "RAPID CONTAINMENT OF ACTIVE CATASTROPHIC INCIDENTS",
         RED,
         [
             ("SCOPE & PURPOSE", "Pre-scripted, muscle-memory actions executed during major failures: secondary coolant spill, electrical arc flash, primary cooling loss, fire alarm trip."),
             ("AUTHORIZATION LEVEL", "Executed IMMEDIATELY by ANY shift personnel on site. Requires ZERO prior consensus or managerial approval."),
             ("MANDATORY PREREQUISITES", "• Verified emergency stop and isolator locations\n• Spill containment socks and suction equipment\n• Arc-flash rated PPE (Category 4 / 40 cal/cm²)\n• Uninhibited access to utility manual trip valves"),
             ("FAILURE PROTOCOL", "Priority 1: Human life safety. Priority 2: Contain the hazard. Priority 3: Stabilize surviving IT infrastructure.")
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

    # Bottom MOP Execution Lifecycle Banner
    wf_y = 690
    draw.rectangle([(55, wf_y), (W - 55, H - 75)], fill=PANEL_BG, outline=PANEL_BORDER, width=2)
    draw.rectangle([(55, wf_y), (W - 55, wf_y + 36)], fill=(20, 26, 38), outline=PANEL_BORDER, width=1)
    draw.text((75, wf_y + 8), "MANDATORY MOP EXECUTION LIFECYCLE (ZERO ACCIDENTS / ZERO UNPLANNED OUTAGES)", font=get_font(13, bold=True), fill=CYAN)

    steps = [
        ("1. PEER REVIEW", "Written by certified PE; audited by second senior engineer."),
        ("2. CAB APPROVAL", "Formally approved by Change Advisory Board 7 days in advance."),
        ("3. PRE-JOB BRIEF", "All technicians walk through steps, hazards, and abort criteria."),
        ("4. TWO-PERSON EXEC", "One engineer executes; second engineer verifies & checks off."),
        ("5. RESTORATION", "Verify plant restored to normal; signed closeout on Day Sheet.")
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
            if draw.textlength(test_line, font=get_font(10)) < (sw - 16):
                cur_line = test_line
            else:
                draw.text((sx + 8, ty), cur_line, font=get_font(10), fill=TEXT_MAIN)
                ty += 16
                cur_line = w
        if cur_line:
            draw.text((sx + 8, ty), cur_line, font=get_font(10), fill=TEXT_MAIN)

    save_path = FIG_DIR / "fig-02-sop-mop-eop-governance-pyramid.png"
    img.save(save_path, "PNG")
    print(f"Saved: {save_path}")

# ==============================================================================
# DIAGRAM 3: Physical Shift Inspection Round (巡检) Topology
# ==============================================================================
def draw_fig_03():
    img, draw = create_base_canvas(
        title="Physical Shift Inspection Round Topology & Audit Gates",
        subtitle="Standardized Physical Inspection Path: MV Substation to High-Density Liquid Whitespace",
        sheet_ref="DAY SHEET: ROUND"
    )

    # 6 Stop Stations along the inspection path
    stations = [
        ("STATION 1", "MV Substation & Generators", "Electrical Yard",
         ["• Utility grid breaker status & phase voltages", "• Generator block heaters (40-50°C)", "• Starter battery charger float voltage (27.2V)", "• Day tank fuel level >= 90% capacity"],
         BLUE),
        ("STATION 2", "Transformer & Switchgear Rooms", "Low-Voltage Distribution",
         ["• Transformer winding temperatures (< 90°C)", "• Visual inspection for corona/arcing tracks", "• Olfactory check for ozone / hot insulation", "• Main incoming breaker loading (< 45% rule)"],
         CYAN),
        ("STATION 3", "UPS & Battery Enclosures", "Energy Storage Yard",
         ["• Battery string pilot cell float voltages", "• Visual check for casing swelling/acid leaks", "• Infrared spot check on inter-cell busbars", "• Room temperature verified within 20-25°C"],
         PURPLE),
        ("STATION 4", "Central Chiller Plant & Towers", "Primary Hydronic Yard",
         ["• Chiller evaporator & condenser approach temps", "• Primary chilled water supply temp (e.g. 12°C)", "• Condenser water basin water quality & biocide", "• Cooling tower fan vibration & belt tension"],
         BLUE),
        ("STATION 5", "Secondary CDU Hydronic Room", "Liquid Cooling Core",
         ["• Pump suction & discharge pressures (0.15-0.9 MPa)", "• Plate heat exchanger differential pressure", "• Diaphragm expansion tank N2 cushion level", "• Automatic vacuum deaerator sight glass check"],
         CYAN),
        ("STATION 6", "High-Density AI Whitespace", "Compute White Floor",
         ["• Aisle containment differential pressure (+2 to +5 Pa)", "• Visual inspection of secondary manifold hoses", "• Ultrasonic check on cold aisle tile velocities", "• Catch pan & leak detection sensing ropes dry"],
         GREEN)
    ]

    card_w = 260
    gap = 20
    start_x = 55
    card_y = 150
    card_h = 440

    for i, (stg, title, sub, bullets, border_c) in enumerate(stations):
        cx = start_x + i * (card_w + gap)
        draw.rectangle([(cx, card_y), (cx + card_w, card_y + card_h)], fill=PANEL_BG, outline=border_c, width=2)
        draw.rectangle([(cx, card_y), (cx + card_w, card_y + 38)], fill=(20, 26, 38), outline=border_c, width=1)
        draw.text((cx + 12, card_y + 10), stg, font=get_font(12, bold=True), fill=border_c)

        draw.text((cx + 12, card_y + 48), title, font=get_font(12, bold=True), fill=TEXT_MAIN)
        draw.text((cx + 12, card_y + 70), sub, font=get_font(10, bold=True), fill=TEXT_MUTED)
        draw.line([(cx + 10, card_y + 92), (cx + card_w - 10, card_y + 92)], fill=PANEL_BORDER, width=1)

        by = card_y + 108
        for b in bullets:
            words = b.split(" ")
            line = ""
            for w in words:
                test_line = line + " " + w if line else w
                if draw.textlength(test_line, font=get_font(10)) < (card_w - 20):
                    line = test_line
                else:
                    draw.text((cx + 10, by), line, font=get_font(10), fill=TEXT_MAIN)
                    by += 15
                    line = w
            if line:
                draw.text((cx + 10, by), line, font=get_font(10), fill=TEXT_MAIN)
                by += 20

        # Bottom gate marker
        draw.rectangle([(cx + 12, card_y + card_h - 45), (cx + card_w - 12, card_y + card_h - 15)],
                       fill=(15, 23, 42), outline=border_c, width=1)
        draw.text((cx + 18, card_y + card_h - 35), f"CHECKPOINT {i+1} OK", font=get_font(10, bold=True), fill=border_c)

        if i < len(stations) - 1:
            arrow_x = cx + card_w + 3
            arrow_y = card_y + card_h // 2
            draw.polygon([(arrow_x, arrow_y - 6), (arrow_x + 12, arrow_y), (arrow_x, arrow_y + 6)], fill=CYAN)

    # Lower Section: Physical Senses in Operational Inspections
    rule_y = 620
    draw.rectangle([(45, rule_y), (W - 45, H - 75)], fill=PANEL_BG, outline=PANEL_BORDER, width=2)
    draw.rectangle([(45, rule_y), (W - 45, rule_y + 36)], fill=(20, 26, 38), outline=PANEL_BORDER, width=1)
    draw.text((65, rule_y + 8), "THE FOUR SENSORY DISCIPLINES OF THE PROFESSIONAL SHIFT ROUND", font=get_font(14, bold=True), fill=AMBER)

    senses = [
        ("1. VISUAL AUDIT", "Inspect valve indicators, analog gauges, sight glasses, and LED status beacons. Look for pipe weeping, condensate pooling, and loose mechanical fasteners. Never rely solely on BMS screens.", CYAN),
        ("2. ACOUSTIC DISCIPLINE", "Listen to mechanical equipment. A cavitation crackle in a centrifugal pump, high-frequency whining in a bearing, or 100 Hz hum in a transformer indicates imminent mechanical failure.", GREEN),
        ("3. THERMAL PROBING", "Use a calibrated infrared thermometer gun on all high-current disconnects, cable lugs, and pipe elbows. Any phase delta-T exceeding 5.0 K must be logged immediately as a defect.", AMBER),
        ("4. OLFACTORY DETECTION", "Human olfactory senses detect electrical overheating hours before smoke detectors trigger. A smell of hot varnish, melted PVC, or ozone indicates insulation degradation.", RED)
    ]

    sw = 400
    for j, (stitle, sdesc, scol) in enumerate(senses):
        sx = 65 + j * (sw + 20)
        sy = rule_y + 55
        draw.rectangle([(sx, sy), (sx + sw, sy + 290)], fill=(18, 22, 32), outline=scol, width=1)
        draw.rectangle([(sx, sy), (sx + sw, sy + 32)], fill=(26, 32, 44), outline=scol, width=1)
        draw.text((sx + 10, sy + 7), stitle, font=get_font(12, bold=True), fill=scol)

        words = sdesc.split()
        line = ""
        ty = sy + 45
        for w in words:
            test_line = line + " " + w if line else w
            if draw.textlength(test_line, font=get_font(11)) < (sw - 20):
                line = test_line
            else:
                draw.text((sx + 10, ty), line, font=get_font(11), fill=TEXT_MAIN)
                ty += 22
                line = w
        if line:
            draw.text((sx + 10, ty), line, font=get_font(11), fill=TEXT_MAIN)

    save_path = FIG_DIR / "fig-03-shift-round-inspection-topology.png"
    img.save(save_path, "PNG")
    print(f"Saved: {save_path}")

# ==============================================================================
# DIAGRAM 4: 2N Electrical Power Capacity & Redundancy Ceiling
# ==============================================================================
def draw_fig_04():
    img, draw = create_base_canvas(
        title="2N Electrical Capacity Allocation & Redundancy Headroom Ceiling",
        subtitle="The 45% Loading Limit Rule: Preventing Cascade Breaker Tripping during Instantaneous Bus Transfer",
        sheet_ref="DAY SHEET: CAPACITY"
    )

    # Graph canvas for Feeder A vs Feeder B Loading
    gx0, gy0 = 100, 180
    gw, gh = 1050, 560
    gx1, gy1 = gx0 + gw, gy0 + gh

    draw.rectangle([(gx0, gy0), (gx1, gy1)], fill=(16, 20, 28), outline=PANEL_BORDER, width=2)

    # Draw two large bar columns: Feeder A and Feeder B
    bar_w = 260
    fa_x = gx0 + 160
    fb_x = gx0 + 620

    # Y-axis (Percentage of Transformer / UPS Nameplate: 0% to 100%)
    for pct in range(0, 110, 10):
        y = gy1 - int((pct / 100.0) * gh)
        draw.line([(gx0, y), (gx1, y)], fill=(28, 35, 48), width=1)
        draw.text((gx0 - 45, y - 6), f"{pct}%", font=get_font(11), fill=TEXT_MUTED)

    draw.text((gx0 - 80, gy0 - 30), "Feeder Load (% kVA)", font=get_font(12, bold=True), fill=TEXT_MAIN)

    # 45% SAFE REDUNDANCY CEILING LINE
    ceil_45_y = gy1 - int((45.0 / 100.0) * gh)
    draw.line([(gx0, ceil_45_y), (gx1, ceil_45_y)], fill=GREEN, width=3)
    draw.text((gx1 - 320, ceil_45_y - 20), "45% SAFE REDUNDANCY CEILING", font=get_font(12, bold=True), fill=GREEN)

    # 50% HARD OVERLOAD LINE (If either feeder > 50%, loss of other causes >100% overload!)
    ceil_50_y = gy1 - int((50.0 / 100.0) * gh)
    draw.line([(gx0, ceil_50_y), (gx1, ceil_50_y)], fill=RED, width=2)
    draw.text((gx1 - 340, ceil_50_y - 20), "50% CATASTROPHIC DANGER THRESHOLD", font=get_font(11, bold=True), fill=RED)

    # Normal Shift Loading: Feeder A = 41%, Feeder B = 42%
    fa_h = int((41.0 / 100.0) * gh)
    draw.rectangle([(fa_x, gy1 - fa_h), (fa_x + bar_w, gy1)], fill=(20, 45, 80), outline=CYAN, width=2)
    draw.text((fa_x + 50, gy1 - fa_h - 30), "FEEDER A: 41.0%", font=get_font(14, bold=True), fill=CYAN)
    draw.text((fa_x + 35, gy1 - fa_h + 30), "Active Compute Load", font=get_font(12), fill=TEXT_MAIN)
    draw.text((fa_x + 55, gy1 - fa_h + 60), "1025 kVA / 2500 kVA", font=get_font(11), fill=TEXT_MUTED)

    fb_h = int((42.0 / 100.0) * gh)
    draw.rectangle([(fb_x, gy1 - fb_h), (fb_x + bar_w, gy1)], fill=(20, 45, 80), outline=CYAN, width=2)
    draw.text((fb_x + 50, gy1 - fb_h - 30), "FEEDER B: 42.0%", font=get_font(14, bold=True), fill=CYAN)
    draw.text((fb_x + 35, gy1 - fb_h + 30), "Active Compute Load", font=get_font(12), fill=TEXT_MAIN)
    draw.text((fb_x + 55, gy1 - fb_h + 60), "1050 kVA / 2500 kVA", font=get_font(11), fill=TEXT_MUTED)

    # Post-Failure Dynamic Simulation Bar (Feeder A tripped -> Feeder B takes 100% load: 41% + 42% = 83%)
    f_total_y = gy1 - int((83.0 / 100.0) * gh)
    draw.line([(fb_x, f_total_y), (fb_x + bar_w, f_total_y)], fill=AMBER, width=3)
    draw.text((fb_x + 15, f_total_y - 22), "Post-Trip Load on B: 83.0% (Safe < 90%)", font=get_font(11, bold=True), fill=AMBER)

    # Right side explanation panel
    pan_x = gx1 + 40
    pan_y = gy0
    pan_w = W - pan_x - 55
    draw.rectangle([(pan_x, pan_y), (pan_x + pan_w, gy1)], fill=PANEL_BG, outline=CYAN, width=2)
    draw.rectangle([(pan_x, pan_y), (pan_x + pan_w, pan_y + 36)], fill=(20, 26, 38), outline=CYAN, width=1)
    draw.text((pan_x + 15, pan_y + 10), "CAPACITY ALLOCATION AUDIT LAWS", font=get_font(13, bold=True), fill=CYAN)

    laws_cap = [
        ("1. THE 45% CAPACITY LIMIT RULE",
         "In a 2N redundant electrical architecture, neither distribution bus may ever exceed 45.0% of its rated transformer or UPS capacity during steady-state operations. A 10% safety margin (45% to 50%) is mandatory to accommodate dynamic step-transients, harmonic inrush currents, and power factor degradation."),
        ("2. THE 50% CASCADE TRIP TRAP",
         "If Feeder A operates at 52% and Feeder B operates at 51%, the facility appears operational. However, if Feeder A trips, Feeder B must instantly absorb 103% load. The surviving main breaker will trip on thermal-magnetic overload, causing a total data hall blackout. Operating > 50% is a critical defect."),
        ("3. CAPACITY RESERVATIONS VS DRAW",
         "Never sell or provision compute capacity based on instantaneous average load! Compute clusters spike from idle to 100% power within milliseconds during AI training job launches. Always provision against peak PDU capacity."),
        ("4. UNVERIFIED ENERGIZATION BAN",
         "Never energize a new IT cabinet 'to see if the breaker holds.' Every capacity addition must be formally calculated against the surviving-bus failure model before the breaker handle is closed.")
    ]
    ry = pan_y + 50
    for r_title, r_desc in laws_cap:
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

    # Bottom summary box
    draw.rectangle([(100, H - 230), (W - 45, H - 75)], fill=(15, 23, 42), outline=PANEL_BORDER, width=1)
    draw.text((120, H - 215), "SHIFT MANAGER SIGN-OFF RULE FOR CAPACITY", font=get_font(12, bold=True), fill=GREEN)
    draw.text((120, H - 185), "• Contracted Capacity: Verified against client service contract schedule and SLA limits.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((120, H - 160), "• Monitored Peak kVA: Highest 15-minute rolling average recorded during the shift.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((120, H - 135), "• Single-Feed Surviving Headroom: S_surviving = (kVA_A + kVA_B) / S_rated. Must remain <= 90.0% at all times.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((120, H - 110), "• Prohibited Request: Any client request to energize loads that breach 45% must be formally REJECTED on the Day Sheet.", font=get_font(11), fill=AMBER)

    save_path = FIG_DIR / "fig-04-2n-power-capacity-and-redundancy-ceiling.png"
    img.save(save_path, "PNG")
    print(f"Saved: {save_path}")

# ==============================================================================
# DIAGRAM 5: Liquid Cooling CDU & Primary/Secondary Circuit Shift Audit Matrix
# ==============================================================================
def draw_fig_05():
    img, draw = create_base_canvas(
        title="Liquid Cooling CDU & Hydronic Circuit Shift Audit Matrix",
        subtitle="Operational Inspection Gates: Pressures, Glycol Refractometry, Filter Delta-P, and Deaerator Checks",
        sheet_ref="DAY SHEET: ROUND & WORK"
    )

    # 4 Quadrants representing key inspection zones:
    # Q1: Pump Skid & Pressures // Q2: Fluid Chemistry & Expansion Tank
    # Q3: Heat Exchanger & Approach // Q4: Manifolds & Catch Pan Leak Ropes
    quad_w = 810
    quad_h = 370

    quads = [
        ("ZONE 1: PUMP SKID & HYDRAULIC PRESSURES", 50, 140, CYAN),
        ("ZONE 2: FLUID CHEMISTRY & NITROGEN CUSHION", 940, 140, PURPLE),
        ("ZONE 3: PLATE HEAT EXCHANGER & APPROACH", 50, 540, BLUE),
        ("ZONE 4: SECONDARY MANIFOLDS & LEAK SENSING", 940, 540, GREEN)
    ]

    for title_q, qx, qy, col in quads:
        draw.rectangle([(qx, qy), (qx + quad_w, qy + quad_h)], fill=PANEL_BG, outline=col, width=2)
        draw.rectangle([(qx, qy), (qx + quad_w, qy + 32)], fill=(20, 26, 38), outline=col, width=1)
        draw.text((qx + 15, qy + 8), title_q, font=get_font(13, bold=True), fill=col)

    # Zone 1 Details
    z1_x, z1_y = 70, 190
    draw.text((z1_x, z1_y), "MANDATORY PUMP OPERATING VERIFICATION:", font=get_font(12, bold=True), fill=TEXT_MAIN)
    draw.text((z1_x, z1_y + 25), "• Canned Motor Pump Export Pressure: 0.15 - 0.90 MPa nominal operating range.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((z1_x, z1_y + 50), "• Differential Pressure Across Pumps: Must remain < 1.0 bar (100 kPa) fluctuation.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((z1_x, z1_y + 75), "• Operating Frequency: Both lead/lag VFDs verified in AUTO mode at 45.0 - 50.0 Hz.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((z1_x, z1_y + 100), "• Manual Valve Check: P1 valve OPEN, F1 bypass filter valve CLOSED (normal run).", font=get_font(11), fill=AMBER)
    draw.text((z1_x, z1_y + 125), "• Vibration & Acoustic Check: Zero cavitation crackling or bearing whining.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((z1_x, z1_y + 155), "FAILURE ACTION: If pump discharge pressure drops below 0.12 MPa, execute EOP-LC-01.", font=get_font(11, bold=True), fill=RED)

    # Zone 2 Details
    z2_x, z2_y = 960, 190
    draw.text((z2_x, z2_y), "FLUID QUALITY & EXPANSION CONTROL:", font=get_font(12, bold=True), fill=TEXT_MAIN)
    draw.text((z2_x, z2_y + 25), "• Optical Refractometer Check: 25.0% +/- 1.0% Propylene Glycol concentration.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((z2_x, z2_y + 50), "• Fluid Conductivity: Must remain < 10.0 uS/cm (tested via handheld meter).", font=get_font(11), fill=TEXT_MUTED)
    draw.text((z2_x, z2_y + 75), "• Expansion Tank N2 Cushion: Pre-charge pressure verified at 1.8 bar +/- 0.1 bar.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((z2_x, z2_y + 100), "• Diaphragm Tank Liquid Level: Visual sight glass shows 40% to 70% level.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((z2_x, z2_y + 125), "• Vacuum Deaerator Sight Tube: Clear of microbubbles; zero froth formation.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((z2_x, z2_y + 155), "FAILURE ACTION: If conductivity exceeds 25 uS/cm, schedule deionizer canister replacement.", font=get_font(11, bold=True), fill=AMBER)

    # Zone 3 Details
    z3_x, z3_y = 70, 590
    draw.text((z3_x, z3_y), "HEAT EXCHANGER THERMODYNAMIC EFFICIENCY:", font=get_font(12, bold=True), fill=TEXT_MAIN)
    draw.text((z3_x, z3_y + 25), "• Approach Temperature: T_sec_sup (40°C) - T_pri_sup (32°C) <= 8.0 K approach.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((z3_x, z3_y + 50), "• PHE Liquid-Side Pressure Drop: Delta-P across secondary plates <= 45 kPa.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((z3_x, z3_y + 75), "• Primary TCV Modulating Valve: Verify position matches heat load (30-80% open).", font=get_font(11), fill=TEXT_MUTED)
    draw.text((z3_x, z3_y + 100), "• Heat Rejection Balance: Secondary liquid heat matches primary water absorption +/- 3%.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((z3_x, z3_y + 125), "• Fouling Indication: Plate Delta-P rise > 20% indicates particulate fouling on strainer.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((z3_x, z3_y + 155), "FAILURE ACTION: Approach temp > 10.0 K indicates PHE scaling or primary flow starvation.", font=get_font(11, bold=True), fill=RED)

    # Zone 4 Details
    z4_x, z4_y = 960, 590
    draw.text((z4_x, z4_y), "MANIFOLDS & LEAKAGE SENSING INTERLOCKS:", font=get_font(12, bold=True), fill=TEXT_MAIN)
    draw.text((z4_x, z4_y + 25), "• Catch Pan Inspection: Internal CDU catch pan verified completely dry.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((z4_x, z4_y + 50), "• Optical Sensor Test: Check LED status beacon on catch pan optical sensor.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((z4_x, z4_y + 75), "• External Sensing Rope: Perimeter rope along manifold trenches shows 'NORMAL' loop.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((z4_x, z4_y + 100), "• Quick-Disconnect Couplings: Physical wipe test on Danfoss FD83 couplings (0 drops/min).", font=get_font(11), fill=TEXT_MUTED)
    draw.text((z4_x, z4_y + 125), "• Manifold Isolation Valves: Verified wired and locked in fully open position.", font=get_font(11), fill=TEXT_MUTED)
    draw.text((z4_x, z4_y + 155), "FAILURE ACTION: Any liquid droplet triggers immediate isolation and incident report.", font=get_font(11, bold=True), fill=RED)

    # Bottom strip
    draw.rectangle([(50, H - 75), (W - 50, H - 45)], fill=(15, 23, 42), outline=PANEL_BORDER, width=1)
    draw.text((70, H - 65), "SHIFT SIGN-OFF RULE: Every CDU parameter must be logged in ink during the shift round. A blank cell blocks handover.",
              font=get_font(11, bold=True), fill=AMBER)

    save_path = FIG_DIR / "fig-05-liquid-cdu-shift-inspection-checklist.png"
    img.save(save_path, "PNG")
    print(f"Saved: {save_path}")

# ==============================================================================
# DIAGRAM 6: Incident Escalation & SLA Communication Timeline
# ==============================================================================
def draw_fig_06():
    img, draw = create_base_canvas(
        title="Incident Escalation Lifecycle & Client SLA Communication Timeline",
        subtitle="Severity Classification (P1/P2/P3), T-0 Discovery, Safe State Stabilization, and the 15-Minute Rule",
        sheet_ref="DAY SHEET: INCIDENT"
    )

    # Top Section: Incident Severity Tiers (P1, P2, P3)
    tier_w = 540
    start_x = 55
    top_y = 150
    tier_h = 240

    tiers_inc = [
        ("PRIORITY 1: CRITICAL OUTAGE (P1)",
         "CATASTROPHIC SERVICE INTERRUPTION / SAFETY",
         RED,
         "• Definition: Total loss of critical IT power or liquid cooling to active compute.\n"
         "• Communication SLA: Initial client notice within 15 MINUTES of T-0.\n"
         "• Management Bridge: Senior engineering conference bridge open in 5 min.\n"
         "• Update Cadence: Status bulletins every 30 minutes until resolution."),
        ("PRIORITY 2: REDUNDANCY COMPROMISED (P2)",
         "LOSS OF SYSTEM REDUNDANCY (AT-RISK STATE)",
         AMBER,
         "• Definition: N+1 pump trip, single UPS bus failure, generator in fault (IT load intact).\n"
         "• Communication SLA: Client notification within 30 MINUTES of T-0.\n"
         "• Action: Mobilize tier-2 vendor specialists under emergency MOP.\n"
         "• Update Cadence: Formal status update every 2 hours."),
        ("PRIORITY 3: MINOR NON-IMPACTING (P3)",
         "OPERATIONAL DEFECT / ZERO SLA EXPOSURE",
         GREEN,
         "• Definition: Isolated telemetry sensor failure, minor cosmetic casing scratch.\n"
         "• Communication SLA: Logged in daily shift report; zero emergency broadcast.\n"
         "• Resolution Window: Standard 14-day closeout tracking in master register.\n"
         "• Update Cadence: Reviewed during weekly operations meeting.")
    ]

    for i, (t_title, t_sub, t_col, t_desc) in enumerate(tiers_inc):
        cx = start_x + i * (tier_w + 30)
        draw.rectangle([(cx, top_y), (cx + tier_w, top_y + tier_h)], fill=PANEL_BG, outline=t_col, width=2)
        draw.rectangle([(cx, top_y), (cx + tier_w, top_y + 36)], fill=(20, 26, 38), outline=t_col, width=1)
        draw.text((cx + 15, top_y + 8), t_title, font=get_font(12, bold=True), fill=t_col)
        draw.text((cx + 15, top_y + 45), t_sub, font=get_font(10, bold=True), fill=TEXT_MUTED)

        sy = top_y + 75
        lines = t_desc.split("\n")
        for l in lines:
            draw.text((cx + 15, sy), l, font=get_font(10), fill=TEXT_MAIN)
            sy += 22

    # Lower Section: Chronological Incident Response Timeline
    tl_y = 420
    tl_h = 470
    draw.rectangle([(55, tl_y), (W - 55, tl_y + tl_h)], fill=PANEL_BG, outline=PANEL_BORDER, width=2)
    draw.rectangle([(55, tl_y), (W - 55, tl_y + 36)], fill=(20, 26, 38), outline=PANEL_BORDER, width=1)
    draw.text((75, tl_y + 8), "THE INCIDENT TIMELINE: FROM T-0 DETECTION TO FORMAL ROOT CAUSE ANALYSIS", font=get_font(13, bold=True), fill=CYAN)

    milestones = [
        ("T-0: DETECTION", "Event occurs; alarm annunciates on BMS / buzzer triggers. Record exact timestamp to the second.", RED),
        ("T + 3 MIN: TRIAGE", "Shift manager assesses physical safety, determines P1/P2/P3 severity, and directs initial EOP.", AMBER),
        ("T + 8 MIN: SAFE STATE", "System stabilized in hardware safe-state (e.g. secondary loop isolated, standby pump running).", GREEN),
        ("T + 15 MIN: CLIENT SLA", "First client flash notice broadcast: FACTS ONLY. Zero unverified speculation or theories.", CYAN),
        ("T + 60 MIN: RESTORATION", "Plant restored to nominal operational configuration under supervised emergency MOP.", BLUE),
        ("T + 24 H: FORMAL RCA", "Root Cause Analysis published with 5-Why methodology and permanent corrective action plan.", PURPLE)
    ]

    mw = (W - 170) // 6
    for m_idx, (mtitle, mdesc, mcol) in enumerate(milestones):
        mx = 75 + m_idx * (mw + 12)
        my = tl_y + 55
        draw.rectangle([(mx, my), (mx + mw, my + 380)], fill=(16, 20, 28), outline=mcol, width=1)
        draw.rectangle([(mx, my), (mx + mw, my + 32)], fill=(26, 34, 48), outline=mcol, width=1)
        draw.text((mx + 8, my + 8), mtitle, font=get_font(10, bold=True), fill=mcol)

        words = mdesc.split(" ")
        cur_line = ""
        ty = my + 48
        for w in words:
            test_line = cur_line + " " + w if cur_line else w
            if draw.textlength(test_line, font=get_font(10)) < (mw - 16):
                cur_line = test_line
            else:
                draw.text((mx + 8, ty), cur_line, font=get_font(10), fill=TEXT_MAIN)
                ty += 18
                cur_line = w
        if cur_line:
            draw.text((mx + 8, ty), cur_line, font=get_font(10), fill=TEXT_MAIN)

    save_path = FIG_DIR / "fig-06-incident-escalation-and-sla-timeline.png"
    img.save(save_path, "PNG")
    print(f"Saved: {save_path}")

# ==============================================================================
# DIAGRAM 7: Shift Manager End-of-Shift Sign-Off Sheet
# ==============================================================================
def draw_fig_07():
    img, draw = create_base_canvas(
        title="Shift Manager End-of-Shift Sign-Off & Impairment Reconciliation",
        subtitle="The Operational Ledger: Bilateral Verification, Open Work Permits, Active Impairments, and the Signature",
        sheet_ref="MASTER DAY SHEET"
    )

    # Layout mimicking the Master Day Sheet
    # 3 Main Panes: Left = Pre-Shift Baseline // Middle = Active Work & Rounds // Right = Closeout & Signature
    pw = 540
    ph = 860
    py = 150

    # PANE 1: Pre-Shift Baseline & Handover
    p1_x = 55
    draw.rectangle([(p1_x, py), (p1_x + pw, py + ph)], fill=PANEL_BG, outline=CYAN, width=2)
    draw.rectangle([(p1_x, py), (p1_x + pw, py + 36)], fill=(16, 28, 45), outline=CYAN, width=1)
    draw.text((p1_x + 15, py + 8), "SECTION 1: PRE-SHIFT BASELINE & HANDOVER", font=get_font(12, bold=True), fill=CYAN)

    y1 = py + 55
    items1 = [
        "• Shift Date & Operational Shift ID (Day / Night)",
        "• Outgoing Shift Manager Handover Accepted: YES / NO",
        "• Active Impairments Carried In (Count & Severity): ____",
        "• Open Work Permits from Previous Shift (LOTO / Hot Work)",
        "• Unresolved Incidents in Investigation State: ____",
        "• Shift Roster: 5 Qualified Trades on Floor (PE / Tech)",
        "• Emergency Response Equipment Inspected & Verified: YES",
        "• Client Service Contracts Active: SLA Terms Cited"
    ]
    for itm in items1:
        draw.text((p1_x + 15, y1), itm, font=get_font(10), fill=TEXT_MAIN)
        y1 += 32

    # PANE 2: Active Work, Changes & Rounds
    p2_x = 630
    draw.rectangle([(p2_x, py), (p2_x + pw, py + ph)], fill=PANEL_BG, outline=AMBER, width=2)
    draw.rectangle([(p2_x, py), (p2_x + pw, py + 36)], fill=(35, 26, 18), outline=AMBER, width=1)
    draw.text((p2_x + 15, py + 8), "SECTION 2: WORK PERMITS, MOPS & ROUNDS", font=get_font(12, bold=True), fill=AMBER)

    y2 = py + 55
    items2 = [
        "• Standing Morning & Afternoon Shift Rounds: 100% COMPLETE",
        "• Station 1 (Substation) & Station 2 (Transformers) Verified OK",
        "• Station 3 (UPS) & Station 4 (Chillers) Logged in Ink",
        "• Station 5 (CDU Secondary Fluid) & Station 6 (AI Whitespace)",
        "• Approved MOPs Executed Today: Ticket Numbers Listed",
        "• Mandatory Rollback Plan Present on Site: YES / NO",
        "• Spares & Consumables Staged Before Tools: VERIFIED",
        "• Vendor Escorts & Access Badges Logged Out: YES"
    ]
    for itm in items2:
        draw.text((p2_x + 15, y2), itm, font=get_font(10), fill=TEXT_MAIN)
        y2 += 32

    # PANE 3: Capacity, Closeout & The Final Signature
    p3_x = 1205
    draw.rectangle([(p3_x, py), (p3_x + pw, py + ph)], fill=PANEL_BG, outline=GREEN, width=2)
    draw.rectangle([(p3_x, py), (p3_x + pw, py + 36)], fill=(16, 32, 24), outline=GREEN, width=1)
    draw.text((p3_x + 15, py + 8), "SECTION 3: CAPACITY, CLOSEOUT & SIGNATURE", font=get_font(12, bold=True), fill=GREEN)

    y3 = py + 55
    items3 = [
        "• Contracted IT Capacity vs Measured Peak kW Audited",
        "• 2N Power Loading Verified <= 45.0% on Both Feeders",
        "• Shift PUE Calculated: 1.14 // WUE Calculated: 0.18 L/kWh",
        "• New Defect Punch Items Logged Today: [  ] None  [  ] Count: __",
        "• Shift Handover Prepared in Ink for Incoming Night Manager",
        "• Lockout Keys Staged in Dual-Custody Key Safe: VERIFIED"
    ]
    for itm in items3:
        draw.text((p3_x + 15, y3), itm, font=get_font(10), fill=TEXT_MAIN)
        y3 += 32

    # The Final Signature Box at bottom of Pane 3
    sig_y = py + ph - 240
    draw.rectangle([(p3_x + 15, sig_y), (p3_x + pw - 15, py + ph - 20)], fill=(15, 24, 34), outline=GREEN, width=2)
    draw.text((p3_x + 25, sig_y + 12), "THE SHIFT MANAGER'S BINDING SENTENCE:", font=get_font(10, bold=True), fill=AMBER)
    draw.text((p3_x + 25, sig_y + 35), '"The data center facility infrastructure has been verified', font=get_font(10, bold=True), fill=TEXT_MAIN)
    draw.text((p3_x + 25, sig_y + 55), 'in compliance with contract SLA terms, with zero unlogged', font=get_font(10, bold=True), fill=TEXT_MAIN)
    draw.text((p3_x + 25, sig_y + 75), 'impairments and zero bypassed safety circuits."', font=get_font(10, bold=True), fill=TEXT_MAIN)

    draw.text((p3_x + 25, sig_y + 115), "Outgoing Shift Manager Signature: ____________________", font=get_font(10), fill=TEXT_MUTED)
    draw.text((p3_x + 25, sig_y + 145), "Incoming Shift Manager Signature: ____________________", font=get_font(10), fill=TEXT_MUTED)
    draw.text((p3_x + 25, sig_y + 175), "Timestamp of Formal Handover: 2026-10-14 20:00:00", font=get_font(10, bold=True), fill=CYAN)

    save_path = FIG_DIR / "fig-07-manager-shift-closeout-sheet.png"
    img.save(save_path, "PNG")
    print(f"Saved: {save_path}")

def main():
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    print("Generating Flagship Engineering Diagrams for Book 05...")
    draw_fig_01()
    draw_fig_02()
    draw_fig_03()
    draw_fig_04()
    draw_fig_05()
    draw_fig_06()
    draw_fig_07()
    print("All 7 Engineering Diagrams successfully generated for Book 05!")

if __name__ == "__main__":
    main()
