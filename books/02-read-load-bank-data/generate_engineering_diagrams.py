#!/usr/bin/env python3
"""
Generate High-Quality Industrial Engineering Diagrams for:
Book 02: Read and Use Load Bank Data (A field guide to the flash report)

Uses Pillow with clean vector-style antialiasing, high-contrast crisp line weights,
professional data-acquisition, P&ID, waveform, and audit report layouts.
"""
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path("/Users/geese/Downloads/book/books/02-read-load-bank-data")
FIG = ROOT / "figures"
FONT_DIR = Path("/Users/geese/Downloads/book/books/01-liquid-load-bank/fonts")

W = 1800
H = 1100

# Color Palette (High-Contrast Professional Clean Style)
BG = (252, 252, 254)          # Clean off-white
HEADER_BG = (15, 23, 42)      # Slate-900 dark header
HEADER_TEXT = (255, 255, 255)
HEADER_SUB = (148, 163, 184)  # Slate-400
PANEL_BG = (255, 255, 255)
PANEL_BORDER = (203, 213, 225)# Slate-300
GRID = (241, 245, 249)        # Slate-100

NAVY = (30, 41, 59)           # Slate-800
BLUE_MAIN = (2, 132, 199)     # Sky-600
RED_ACCENT = (225, 29, 72)    # Rose-600
GREEN_PASS = (22, 163, 74)    # Emerald-600
AMBER_WARN = (217, 119, 6)    # Amber-600
PURPLE_ALGO = (126, 34, 206)  # Purple-700
TEXT_MAIN = (15, 23, 42)      # Dark text
TEXT_MUTED = (71, 85, 105)    # Slate-600

def get_font(size, bold=False):
    ttf = FONT_DIR / ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf")
    return ImageFont.truetype(str(ttf), size)

def base_canvas(title, subtitle, fig_no=""):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    
    # Background subtle grid
    for x in range(0, W, 50):
        d.line((x, 0, x, H), fill=GRID, width=1)
    for y in range(0, H, 50):
        d.line((0, y, W, y), fill=GRID, width=1)
        
    # Dark Header
    d.rectangle((0, 0, W, 85), fill=HEADER_BG)
    if fig_no:
        d.rectangle((30, 18, 150, 68), fill=BLUE_MAIN)
        d.text((45, 28), fig_no, font=get_font(22, True), fill=(255, 255, 255))
        d.text((170, 20), title, font=get_font(26, True), fill=HEADER_TEXT)
        d.text((170, 52), subtitle, font=get_font(15), fill=HEADER_SUB)
    else:
        d.text((40, 20), title, font=get_font(26, True), fill=HEADER_TEXT)
        d.text((40, 52), subtitle, font=get_font(15), fill=HEADER_SUB)
        
    # Footer
    d.line((40, H - 35, W - 40, H - 35), fill=PANEL_BORDER, width=1)
    d.text((40, H - 28), "DATA CENTER FIELD GUIDES · BOOK 02: READ AND USE LOAD BANK DATA", font=get_font(12, True), fill=TEXT_MUTED)
    d.text((W - 360, H - 28), "SPECIFY THE STAND-IN · ACCEPT THE FILE", font=get_font(12, True), fill=TEXT_MUTED)
    return im, d

def draw_panel(d, xy, title="", bg=PANEL_BG, border=PANEL_BORDER):
    x0, y0, x1, y1 = xy
    d.rectangle(xy, fill=bg, outline=border, width=2)
    if title:
        d.rectangle((x0, y0, x1, y0 + 34), fill=(241, 245, 249), outline=border, width=1)
        d.text((x0 + 14, y0 + 8), title, font=get_font(14, True), fill=NAVY)

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

# ==============================================================================
# FIGURE 01: Flash Report Architecture & Executive Summary Layout
# ==============================================================================
def fig_01_flash_report():
    im, d = base_canvas(
        "FLASH REPORT ARCHITECTURE: THE ONE-PAGE AUDIT FORMAT",
        "The 5 Mandatory Passes, Preparation Block, Cited Limits & Stranger Sign-Off",
        "FIG 01"
    )
    
    # Left Block: Metadata & Preparation
    draw_panel(d, (40, 105, 540, 480), "RUN METADATA & PREPARATION BLOCK")
    meta = [
        ("Run Identification:", "LB-TEST-2026-H01-A"),
        ("Facility / Hall:", "AI Data Hall #03, Secondary Loop"),
        ("Design Basis Sheet:", "DOC-SPEC-LB-NVL72 Rev 2.4 (Cited)"),
        ("Coolant Spec:", "25% Propylene Glycol (PG25) @ 35°C"),
        ("Primary Feeders:", "2N Dual Feeder A & B (415V, 3-Phase)"),
        ("Test Unit Count:", "4x 120kW Parallel Cabinets (480kW Net)"),
        ("Ambient Air Dew Point:", "T_dp = 19.4°C (Condensation Margin = 15.6K)"),
    ]
    y = 150
    for label, val in meta:
        d.text((55, y), label, font=get_font(13, True), fill=TEXT_MAIN)
        d.text((235, y), val, font=get_font(13), fill=BLUE_MAIN)
        y += 26
        
    d.line((55, 340, 525, 340), fill=PANEL_BORDER, width=1)
    d.text((55, 350), "PREPARATION GATE (PRE-HEAT BASELINE):", font=get_font(14, True), fill=NAVY)
    prep_items = [
        ("[PASS] 1. All units filled & vented (Zero trapped air)", GREEN_PASS),
        ("[PASS] 2. Power feed verified against site code", GREEN_PASS),
        ("[PASS] 3. Unit self-check: contactors & trips cleared", GREEN_PASS),
        ("[PASS] 4. 10-Min Zero-Load Hold: sensors alive & reading", GREEN_PASS),
    ]
    y = 378
    for item, col in prep_items:
        d.text((55, y), item, font=get_font(13, True), fill=col)
        y += 24

    # Right Block: The Five Passes Table
    draw_panel(d, (560, 105, 1760, 480), "THE FIVE MANDATORY SCENE PASSES (OVERALL VERDICT REQUIRES ALL 5)")
    headers = ["SCENE NAME", "CITED REQUIREMENT", "OBSERVED EVIDENCE", "DWELL TIME", "DEVIATION", "VERDICT"]
    cols = [575, 700, 1030, 1345, 1470, 1645]
    
    # Table header bar
    d.rectangle((560, 140, 1760, 172), fill=NAVY)
    for i, h in enumerate(headers):
        d.text((cols[i], 148), h, font=get_font(12, True), fill=(255, 255, 255))
        
    rows = [
        ("1. Pretest", "Flow >= 170 LPM/cab, ΔP <= 115 kPa", "Flow = 176.2 LPM, ΔP = 111.4 kPa", "10 min hold", "+3.6% / -3.1%", "PASS", GREEN_PASS),
        ("2. Gradient", "Step plateaus (25, 50, 75, 100%)", "Steps 30->60->90->120 kW tracked", "15 min/step", "ΔT rise < 2.0%", "PASS", GREEN_PASS),
        ("3. Overload", "110% rating (132 kW) visited & exited", "Entered 14:15, exited cleanly 14:20", "5 min visit", "Zero trip/alarm", "PASS", GREEN_PASS),
        ("4. Step Jump", "Instant 30 kW -> 120 kW step command", "Tracked < 1.5s, zero water hammer", "10 min dwell", "Overshoot < 2.5%", "PASS", GREEN_PASS),
        ("5. Single-Feed", "Feeder A dropped @ 100%; B holds 50%", "Cleared in 14 ms; PLC zero dip", "10 min hold", "Zero reboot", "PASS", GREEN_PASS),
    ]
    y = 182
    for name, req, obs, dwell, dev, verd, vcol in rows:
        d.rectangle((560, y - 4, 1760, y + 42), fill=(255, 255, 255) if (y//40)%2==0 else (248, 250, 252))
        d.text((cols[0], y + 8), name, font=get_font(12, True), fill=NAVY)
        d.text((cols[1], y + 8), req, font=get_font(11), fill=TEXT_MUTED)
        d.text((cols[2], y + 8), obs, font=get_font(11), fill=TEXT_MAIN)
        d.text((cols[3], y + 8), dwell, font=get_font(11), fill=TEXT_MUTED)
        d.text((cols[4], y + 8), dev, font=get_font(11), fill=BLUE_MAIN)
        d.rectangle((cols[5] - 6, y + 4, cols[5] + 80, y + 32), fill=(220, 252, 231), outline=vcol, width=1)
        d.text((cols[5] + 12, y + 8), verd, font=get_font(13, True), fill=vcol)
        y += 46
        
    d.rectangle((560, y + 8, 1760, y + 54), fill=(241, 245, 249), outline=BLUE_MAIN, width=2)
    d.text((580, y + 18), "OVERALL RESULT: PASS", font=get_font(18, True), fill=GREEN_PASS)
    d.text((850, y + 20), "Rule: Overall Pass requires all attempted lines. A missing line is 'NOT RUN'. A pretty curve never outvotes a blank cell.", font=get_font(13, True), fill=NAVY)

    # Bottom Left: Uniformity & CV Table
    draw_panel(d, (40, 505, 860, 1030), "MULTI-CABINET CONSISTENCY & COEFFICIENT OF VARIATION (CV)")
    d.text((55, 545), "Uniformity Metric: CV = (Standard Deviation / Mean) × 100% across parallel cabinets", font=get_font(13), fill=TEXT_MUTED)
    
    cv_rows = [
        ("Electrical Power Uniformity", "Mean = 120.1 kW", "StdDev = 0.82 kW", "CV = 0.68%", "Limit <= 1.0%", "PASS", GREEN_PASS),
        ("Coolant Flow Uniformity", "Mean = 176.5 LPM", "StdDev = 5.21 LPM", "CV = 2.95%", "Limit <= 5.0%", "PASS", GREEN_PASS),
        ("Return Liquid Temp Uniformity", "Mean = 45.08 °C", "StdDev = 0.41 °C", "CV = 0.91%", "Limit <= 2.0%", "PASS", GREEN_PASS),
        ("Differential Pressure ΔP", "Mean = 112.4 kPa", "StdDev = 3.80 kPa", "CV = 3.38%", "Limit <= 5.0%", "PASS", GREEN_PASS),
        ("Companion Air Heat Ratio", "Mean = 18.2 kW", "StdDev = 0.35 kW", "CV = 1.92%", "Limit <= 2.5%", "PASS", GREEN_PASS),
    ]
    y = 575
    for name, m, sd, cv, lim, v, col in cv_rows:
        d.rectangle((55, y, 845, y + 68), fill=(255, 255, 255), outline=PANEL_BORDER, width=1)
        d.text((70, y + 8), name, font=get_font(14, True), fill=NAVY)
        d.text((70, y + 36), f"{m}  |  {sd}", font=get_font(12), fill=TEXT_MUTED)
        d.text((450, y + 12), cv, font=get_font(16, True), fill=BLUE_MAIN)
        d.text((450, y + 38), lim, font=get_font(12), fill=TEXT_MUTED)
        d.rectangle((720, y + 14, 825, y + 50), fill=(220, 252, 231), outline=col, width=1)
        d.text((745, y + 20), v, font=get_font(14, True), fill=col)
        y += 76
        
    d.text((55, 965), "NOTE ON DATA INTEGRITY: A dead or frozen sensor channel yields CV = 0.00%.", font=get_font(12, True), fill=RED_ACCENT)
    d.text((55, 988), "Quality Bitmask validation must confirm sensor variance σ > 0 before CV is accepted.", font=get_font(12), fill=TEXT_MUTED)

    # Bottom Right: Signatures & Auditor Block
    draw_panel(d, (880, 505, 1760, 1030), "AUTHORITY SIGN-OFF: FOUR SEPARATE ROLES")
    roles = [
        ("1. Sheet Owner (The Specification Custodian)", "Verifies that all limits match the cited revision. May not quietly waive a cell in the hall.", "Signed: Eleanor Vance, Lead Cx Engineer"),
        ("2. Operator (The Control Pilot)", "Commands load plateaus, dwell intervals, and manual trips. Did not author the controller firmware.", "Signed: Marcus Brody, Operations Technician"),
        ("3. Recorder (The Objective Chronicler)", "Logs raw timestamps, alarms, and boring passes without smoothing or discarding bad runs.", "Signed: David Chen, Test Recorder"),
        ("4. The Stranger (Independent Audit Authority)", "Was not involved in fabrication or commissioning. Received the raw CSV export and validated files.", "Signed: Dr. Sarah Jenkins, Third-Party CxA"),
    ]
    y = 550
    for title_r, desc_r, sign_r in roles:
        d.rectangle((895, y, 1745, y + 90), fill=(248, 250, 252), outline=PANEL_BORDER, width=1)
        d.text((915, y + 8), title_r, font=get_font(14, True), fill=NAVY)
        d.text((915, y + 34), desc_r, font=get_font(12), fill=TEXT_MUTED)
        d.text((915, y + 60), sign_r, font=get_font(13, True), fill=BLUE_MAIN)
        y += 100
        
    d.rectangle((895, 955, 1745, 1015), fill=NAVY)
    d.text((915, 968), "FINAL VERDICT CLAUSE: \"We certify that this Flash Report reflects raw, un-retouched telemetry.", font=get_font(13, True), fill=(255, 255, 255))
    d.text((915, 990), "No stale repeats were painted forward, and no failed plateaus were averaged out.\"", font=get_font(13), fill=HEADER_SUB)

    path = FIG / "fig-01-flash-report-structure.png"
    im.save(path, "PNG")
    return path

# ==============================================================================
# FIGURE 02: End-to-End Telemetry Acquisition Pipeline
# ==============================================================================
def fig_02_telemetry_pipeline():
    im, d = base_canvas(
        "TELEMETRY HOP ARCHITECTURE: PHYSICAL SENSOR TO FLASH REPORT",
        "Modbus-TCP Polling, IEEE-754 Word Swapping, Quality Bitmask & MQTT Topic Rules",
        "FIG 02"
    )
    
    stages = [
        ("STAGE 1: SENSOR", "Physical Metrology", [
            "• Pt100 RTD 4-Wire Immersion",
            "• Vortex Shedding Flow Meter",
            "• Static DPT Perpendicular Tap",
            "• Class 0.2 Power Transducer",
            "• Core Stream Immersion (1/3~1/2D)"
        ], (2, 132, 199)),
        
        ("STAGE 2: TRANSMITTER", "ADC & Local Engine", [
            "• 24-Bit Sigma-Delta ADC (1kHz)",
            "• Local 1-Second Digital Filter",
            "• IEEE-754 32-bit Float Format",
            "• Word Swapping Configuration",
            "• Local Raw Timestamp Engine"
        ], (30, 41, 59)),
        
        ("STAGE 3: MODBUS-TCP", "Industrial Bus / Port 502", [
            "• Discrete Coils: Valve/Trip Status",
            "• Input Regs (30001+): Read-Only",
            "• Holding Regs (40001+): Commanded",
            "• Dedicated Quality Reg (40050):",
            "  Bit 0=OK, 1=Stale, 2=Fault"
        ], (126, 34, 206)),
        
        ("STAGE 4: EDGE GATEWAY", "Active Poller (1 Hz)", [
            "• Deterministic 1s Poll Loop",
            "• Timeout Handler: Mark MISSING",
            "• STRICT BAN ON PAINTING FORWARD",
            "• Jitter Logging (<10ms delta)",
            "• NTP Network Clock Synchronized"
        ], (217, 119, 6)),
        
        ("STAGE 5: MQTT BROKER", "Telemetry Publisher", [
            "• Topic: dc/hall/rack/telemetry",
            "• QoS 1 (At least once delivery)",
            "• JSON Payload with 'quality_code'",
            "• STRICT BAN ON RETAINED MSG",
            "• Last-Will-and-Testament Fault"
        ], (22, 163, 74)),
        
        ("STAGE 6: FLASH REPORT", "Audit & Analysis Engine", [
            "• Immutable Raw CSV Store",
            "• 60-Second Rolling Window Mean",
            "• Variance Check: Flag σ² = 0",
            "• Online Focus/FLOC Detection",
            "• Automated One-Page Generator"
        ], (225, 29, 72)),
    ]
    
    w_box = 260
    gap = 26
    start_x = 45
    y_box = 120
    h_box = 320
    
    for i, (title, sub, bullets, col) in enumerate(stages):
        x = start_x + i * (w_box + gap)
        d.rectangle((x, y_box, x + w_box, y_box + h_box), fill=PANEL_BG, outline=col, width=2)
        d.rectangle((x, y_box, x + w_box, y_box + 44), fill=col)
        d.text((x + 12, y_box + 8), title, font=get_font(13, True), fill=(255, 255, 255))
        d.text((x + 12, y_box + 26), sub, font=get_font(11), fill=(241, 245, 249))
        
        by = y_box + 58
        for b in bullets:
            d.text((x + 12, by), b, font=get_font(12), fill=TEXT_MAIN)
            by += 28
            
        # Draw Arrow to next stage
        if i < len(stages) - 1:
            ax = x + w_box
            ay = y_box + h_box // 2
            d.line((ax, ay, ax + gap, ay), fill=BLUE_MAIN, width=3)
            d.polygon([(ax + gap, ay), (ax + gap - 10, ay - 6), (ax + gap - 10, ay + 6)], fill=BLUE_MAIN)

    # Lower Section: Real Data vs Stale Repeat Protocol Details
    draw_panel(d, (40, 470, 880, 1030), "PROTOCOL INTEGRITY: BYTE ORDERING & THE QUALITY BITMASK")
    d.text((55, 510), "1. Modbus IEEE-754 32-Bit Float Byte Order Trap:", font=get_font(15, True), fill=NAVY)
    d.text((55, 535), "Two 16-bit registers hold one 32-bit float. Swapping High/Low words alters values drastically:", font=get_font(13), fill=TEXT_MUTED)
    
    d.rectangle((55, 565, 860, 645), fill=(248, 250, 252), outline=PANEL_BORDER, width=1)
    d.text((68, 575), "Correct (CDAB / Big-Endian Word Swap):", font=get_font(12, True), fill=NAVY)
    d.text((355, 575), "Reg 40001: 0x4234, Reg 40002: 0x0000 => 45.00 °C", font=get_font(12, True), fill=GREEN_PASS)
    d.text((68, 605), "Corrupted (ABCD / Big-Endian Direct):", font=get_font(12, True), fill=NAVY)
    d.text((355, 605), "Reg 40001: 0x0000, Reg 40002: 0x4234 => 1.87e-38 °C (GARBAGE)", font=get_font(12, True), fill=RED_ACCENT)
    
    d.text((55, 665), "2. The Mandatory 16-Bit Quality Bitmask Register (Reg 40050):", font=get_font(15, True), fill=NAVY)
    d.text((55, 690), "Every telemetry frame must include hardware-level validity flags for all channels:", font=get_font(13), fill=TEXT_MUTED)
    
    bit_items = [
        ("Bit 0x0001", "SUPPLY_TEMP_OK", "Normal live reading", GREEN_PASS),
        ("Bit 0x0002", "RETURN_TEMP_OK", "Normal live reading", GREEN_PASS),
        ("Bit 0x0004", "FLOW_RATE_OK", "Normal live reading", GREEN_PASS),
        ("Bit 0x0010", "SENSOR_STALE", "ADC repeated previous value (BUFFER FROZEN)", RED_ACCENT),
        ("Bit 0x0020", "COMM_TIMEOUT", "Modbus polling cycle timed out (>250ms)", RED_ACCENT),
        ("Bit 0x0040", "OUT_OF_RANGE", "Resistance open-circuit / thermocouple break", RED_ACCENT),
    ]
    by = 720
    for bit, name, desc, col in bit_items:
        d.rectangle((55, by, 860, by + 34), fill=(255, 255, 255), outline=PANEL_BORDER, width=1)
        d.text((70, by + 8), bit, font=get_font(12, True), fill=col)
        d.text((180, by + 8), name, font=get_font(12, True), fill=NAVY)
        d.text((400, by + 8), desc, font=get_font(12), fill=TEXT_MUTED)
        by += 40

    d.text((55, 975), "CRITICAL CX RULE: If Quality Bitmask has Bit 4 or 5 set, the data block is FAULT.", font=get_font(13, True), fill=RED_ACCENT)
    d.text((55, 998), "The Flash Report must reject the timestamp rather than calculating a fictitious mean.", font=get_font(12), fill=TEXT_MUTED)

    # Lower Right: MQTT JSON Schema & Payload Architecture
    draw_panel(d, (900, 470, 1760, 1030), "MQTT JSON TELEMETRY PAYLOAD SPECIFICATION (QoS 1)")
    d.text((915, 510), "Standard Telemetry Message Published Once Per Second:", font=get_font(14, True), fill=NAVY)
    
    code_lines = [
        "{",
        '  "timestamp": "2026-10-14T14:22:15.000Z",',
        '  "rack_id": "LB-NVL72-01",',
        '  "run_id": "RUN-2026-OCT-CX01",',
        '  "commanded_kw": 120.0,',
        '  "electrical": {',
        '    "feeder_a_kw": 60.1, "feeder_b_kw": 59.9, "total_kw": 120.0,',
        '    "voltage_v": 415.2, "current_a": 167.1, "pf": 0.999',
        '  },',
        '  "hydraulics": {',
        '    "flow_lpm": 176.4, "supply_c": 35.08, "return_c": 45.12,',
        '    "delta_t_k": 10.04, "dp_kpa": 112.5, "thermal_kw": 98.6',
        '  },',
        '  "companion_air": { "inlet_c": 24.2, "outlet_c": 38.5, "air_kw": 18.9 },',
        '  "quality": { "mask": "0x0007", "stale_flag": false, "raw_samples": 60 }',
        "}"
    ]
    d.rectangle((915, 540, 1745, 930), fill=(15, 23, 42), outline=NAVY, width=1)
    cy = 555
    for cl in code_lines:
        col = (255, 255, 255)
        if '"quality"' in cl or '"mask"' in cl or '"stale_flag"' in cl:
            col = (250, 204, 21)
        elif '"thermal_kw"' in cl or '"delta_t_k"' in cl or '"total_kw"' in cl:
            col = (56, 189, 248)
        d.text((935, cy), cl, font=get_font(13), fill=col)
        cy += 24
        
    d.text((915, 950), "• BAN ON RETAINED MESSAGES: Broker must never cache last message as 'retained'.", font=get_font(13, True), fill=RED_ACCENT)
    d.text((915, 975), "• CLOCK SKEW ENVELOPE: Edge gateway and collector timestamps must agree within ±200ms.", font=get_font(13), fill=TEXT_MAIN)
    d.text((915, 1000), "• MISSING READ POLICY: 1 missing sample = gap; 3 consecutive misses = plateau marked INVALID.", font=get_font(13, True), fill=NAVY)

    path = FIG / "fig-02-telemetry-pipeline.png"
    im.save(path, "PNG")
    return path

# ==============================================================================
# FIGURE 03: Multi-Cabinet Hydraulic & Thermal Uniformity (CV Metric)
# ==============================================================================
def fig_03_multicabinet_uniformity():
    im, d = base_canvas(
        "MULTI-CABINET HYDRAULIC & THERMAL UNIFORMITY (CV METRIC)",
        "Manifold Flow Balance, Coefficient of Variation Thresholds & Starvation Detection",
        "FIG 03"
    )
    
    # Top Section: Manifold & Parallel Cabinet Diagram
    draw_panel(d, (40, 105, 1760, 480), "PARALLEL LIQUID LOAD BANK CLUSTER: REVERSE-RETURN SECONDARY MANIFOLD")
    
    # Supply and Return Headers
    d.rectangle((100, 160, 1660, 185), fill=BLUE_MAIN)
    d.text((120, 164), "SECONDARY SUPPLY MANIFOLD (COLD PG25 @ 35.0°C, P_sup = 4.20 bar)", font=get_font(14, True), fill=(255, 255, 255))
    
    d.rectangle((100, 400, 1660, 425), fill=RED_ACCENT)
    d.text((120, 404), "SECONDARY RETURN MANIFOLD (HOT PG25 @ 45.0°C, P_ret = 3.05 bar)", font=get_font(14, True), fill=(255, 255, 255))
    
    # 4 Cabinets
    cab_w = 260
    cab_h = 160
    cab_xs = [220, 600, 980, 1360]
    
    for i, x in enumerate(cab_xs, 1):
        # Supply Drop
        d.line((x + 60, 185, x + 60, 220), fill=BLUE_MAIN, width=6)
        # Return Riser
        d.line((x + 200, 360, x + 200, 400), fill=RED_ACCENT, width=6)
        
        # Cabinet Body
        is_starved = (i == 4)
        c_fill = (254, 242, 242) if is_starved else (240, 253, 244)
        c_border = RED_ACCENT if is_starved else GREEN_PASS
        
        d.rectangle((x, 220, x + cab_w, 360), fill=c_fill, outline=c_border, width=2)
        d.rectangle((x, 220, x + cab_w, 252), fill=c_border)
        d.text((x + 12, 228), f"RACK LOAD BANK #{i:02d}", font=get_font(13, True), fill=(255, 255, 255))
        
        if not is_starved:
            flow_str = f"Flow: 176.{i} LPM"
            dp_str = "ΔP: 112 kPa"
            t_str = "T_out: 45.1 °C"
            kw_str = "Load: 120 kW"
            status = "BALANCED (PASS)"
            s_col = GREEN_PASS
        else:
            flow_str = "Flow: 124.0 LPM (LOW!)"
            dp_str = "ΔP: 78 kPa"
            t_str = "T_out: 49.8 °C (OVERTEMP!)"
            kw_str = "Load: 120 kW"
            status = "STARVED! (FAIL)"
            s_col = RED_ACCENT
            
        d.text((x + 14, 260), flow_str, font=get_font(12, True), fill=TEXT_MAIN)
        d.text((x + 14, 280), dp_str, font=get_font(12), fill=TEXT_MUTED)
        d.text((x + 14, 300), t_str, font=get_font(12, True), fill=s_col)
        d.text((x + 14, 320), kw_str, font=get_font(12), fill=TEXT_MAIN)
        d.text((x + 14, 338), status, font=get_font(11, True), fill=s_col)
        
    d.text((100, 445), "HYDRAULIC WARNING: Direct-return piping creates severe hydraulic pressure gradient. Rack #04 suffers starvation without balancing valves.", font=get_font(13, True), fill=RED_ACCENT)

    # Bottom Left: The CV Formula & Criteria Table
    draw_panel(d, (40, 505, 880, 1030), "COEFFICIENT OF VARIATION (CV) MATHEMATICAL MODEL")
    
    # Formula Box
    d.rectangle((60, 550, 860, 650), fill=(241, 245, 249), outline=BLUE_MAIN, width=1)
    d.text((80, 565), "MATHEMATICAL DEFINITION OF CV (UNIFORMITY METRIC):", font=get_font(13, True), fill=NAVY)
    d.text((80, 595), "CV = ( σ / μ ) × 100%  =  [ √ ( (1/N) Σ (x_i - μ)² )  /  μ ] × 100%", font=get_font(16, True), fill=BLUE_MAIN)
    d.text((80, 625), "where N = number of parallel load bank racks, μ = group mean, σ = standard deviation", font=get_font(12), fill=TEXT_MUTED)
    
    d.text((60, 670), "STANDARDIZED FLASH REPORT THRESHOLDS:", font=get_font(14, True), fill=NAVY)
    
    th_rows = [
        ("Electrical Active Power (kW)", "CV <= 1.0%", "Balanced resistor tolerance, identical voltage taps"),
        ("Coolant Volumetric Flow (LPM)", "CV <= 5.0%", "Balanced secondary manifolds & equal branch piping"),
        ("Return Temperature Rise (ΔT)", "CV <= 3.0%", "Uniform heat transfer without internal bypass leaks"),
        ("Manifold Differential Pressure (kPa)", "CV <= 5.0%", "Identical hydraulic resistance across all cabinets"),
        ("Companion Air Temperature Rise (K)", "CV <= 2.5%", "Symmetric air distribution into hot aisle containment"),
    ]
    y = 705
    for param, limit, desc in th_rows:
        d.rectangle((60, y, 860, y + 48), fill=(255, 255, 255), outline=PANEL_BORDER, width=1)
        d.text((75, y + 8), param, font=get_font(13, True), fill=NAVY)
        d.text((450, y + 8), limit, font=get_font(13, True), fill=BLUE_MAIN)
        d.text((75, y + 28), desc, font=get_font(11), fill=TEXT_MUTED)
        y += 56
        
    d.text((60, 990), "NOTE: A dead group has CV = 0.00%. The quality bitmask must certify live variance first.", font=get_font(12, True), fill=RED_ACCENT)

    # Bottom Right: Comparative Case Studies (Balanced vs Starved)
    draw_panel(d, (900, 505, 1760, 1030), "CASE STUDY COMPARISON: BALANCED CLUSTER vs. STARVED RACK")
    
    # Balanced Case
    d.rectangle((920, 550, 1740, 750), fill=(240, 253, 244), outline=GREEN_PASS, width=1)
    d.text((940, 565), "CASE A: COMPLIANT BALANCED RUN (Racks 1-4 with Balancing Valves)", font=get_font(14, True), fill=GREEN_PASS)
    d.text((940, 595), "• Flow Rates: 176.1, 177.2, 176.8, 175.9 LPM", font=get_font(13), fill=TEXT_MAIN)
    d.text((940, 620), "• Mean Flow μ = 176.5 LPM, StdDev σ = 0.58 LPM", font=get_font(13, True), fill=NAVY)
    d.text((940, 645), "• Calculated Flow CV = (0.58 / 176.5) × 100% = 0.33%  (Pass, well under 5.0% threshold)", font=get_font(13, True), fill=GREEN_PASS)
    d.text((940, 675), "• Outlet Temperatures: 45.1, 45.0, 45.1, 45.2 °C (Uniform ΔT = 10.1K ± 0.1K)", font=get_font(13), fill=TEXT_MAIN)
    d.text((940, 700), "• Heat Story Agreement: Each rack absorbs 98.4kW ± 0.5kW liquid enthalpy.", font=get_font(13), fill=TEXT_MUTED)
    d.text((940, 725), "• CONCLUSION: Uniform rack resistance verified; CDU secondary loop validated.", font=get_font(13, True), fill=GREEN_PASS)

    # Starved Case
    d.rectangle((920, 770, 1740, 990), fill=(254, 242, 242), outline=RED_ACCENT, width=1)
    d.text((940, 785), "CASE B: HYDRAULIC STARVATION FAILURE (Rack 4 Under-Supplied)", font=get_font(14, True), fill=RED_ACCENT)
    d.text((940, 815), "• Flow Rates: 192.0, 185.0, 172.0, 124.0 LPM (Rack 4 choked due to branch line)", font=get_font(13), fill=TEXT_MAIN)
    d.text((940, 840), "• Mean Flow μ = 168.25 LPM, StdDev σ = 30.7 LPM", font=get_font(13, True), fill=NAVY)
    d.text((940, 865), "• Calculated Flow CV = (30.7 / 168.25) × 100% = 18.25%  (CRITICAL FAIL > 5.0%)", font=get_font(13, True), fill=RED_ACCENT)
    d.text((940, 895), "• Outlet Temperatures: 43.8, 44.5, 45.6, 49.8 °C (Rack 4 rises to dangerous 49.8°C!)", font=get_font(13), fill=RED_ACCENT)
    d.text((940, 920), "• Consequence: Rack 4 triggers thermal trip alarm; CDU pump runs in sub-optimal curve.", font=get_font(13), fill=TEXT_MUTED)
    d.text((940, 945), "• FLASH REPORT VERDICT: FAIL on Consistency line; DO NOT COMMISSION PRODUCTION GPUS.", font=get_font(13, True), fill=RED_ACCENT)

    path = FIG / "fig-03-multicabinet-uniformity.png"
    im.save(path, "PNG")
    return path

# ==============================================================================
# FIGURE 04: Metrology Sampling & Stale Data Detection
# ==============================================================================
def fig_04_sampling_and_stale():
    im, d = base_canvas(
        "METROLOGY SAMPLING: 1s RAW SAMPLES vs. 60s MEAN & STALE FRAUD",
        "Turbulent Variance (σ² > 0) vs. Buffer Freeze Flatline (σ² = 0)",
        "FIG 04"
    )
    
    # Left Panel: Real Physical Turbulent Stream
    draw_panel(d, (40, 105, 880, 680), "PANEL A: GENUINE PHYSICAL STREAM (TURBULENT CONVECTIVE NOISE)")
    d.rectangle((60, 150, 860, 480), fill=(15, 23, 42))
    
    # Grid lines inside plot
    for y_val in [200, 260, 320, 380, 440]:
        d.line((60, y_val, 860, y_val), fill=(30, 41, 59), width=1)
        
    d.text((70, 160), "Return Coolant Temp (°C) — 1s Raw Samples vs 60s Rolling Mean", font=get_font(12, True), fill=(148, 163, 184))
    d.text((70, 250), "45.5°C", font=get_font(11), fill=(148, 163, 184))
    d.text((70, 310), "45.0°C", font=get_font(11), fill=(148, 163, 184))
    d.text((70, 370), "44.5°C", font=get_font(11), fill=(148, 163, 184))
    
    # Draw simulated physical noisy scatter
    pts_raw = []
    pts_mean = []
    import random
    random.seed(42)
    for x_i in range(100, 840, 4):
        # Raw noisy point around 45.0 with Gaussian noise
        noise = math.sin(x_i * 0.05) * 8 + (random.random() - 0.5) * 22
        y_pt = 310 + int(noise)
        d.ellipse((x_i - 2, y_pt - 2, x_i + 2, y_pt + 2), fill=(56, 189, 248))
        
        # Mean point (smoother)
        y_m = 310 + int(math.sin(x_i * 0.05) * 8)
        pts_mean.append((x_i, y_m))
        
    for i in range(len(pts_mean) - 1):
        d.line((pts_mean[i], pts_mean[i+1]), fill=(250, 204, 21), width=3)
        
    d.rectangle((60, 500, 860, 660), fill=(240, 253, 244), outline=GREEN_PASS, width=1)
    d.text((80, 515), "STATISTICAL ATTRIBUTES OF LIVE FLOW:", font=get_font(14, True), fill=GREEN_PASS)
    d.text((80, 540), "• Sample Count: 60 live samples per 1-minute block (100% retention)", font=get_font(12), fill=TEXT_MAIN)
    d.text((80, 565), "• Turbulent Variance: σ² = 0.038 K²  (σ = 0.195 K)  => σ > 0 confirmed", font=get_font(13, True), fill=NAVY)
    d.text((80, 590), "• Physical Reality: Micro-convective eddies prevent absolute flatness.", font=get_font(12), fill=TEXT_MUTED)
    d.text((80, 615), "• Rolling 60s Mean: Plotted as single representative point for Flash Report.", font=get_font(12), fill=TEXT_MUTED)
    d.text((80, 638), "• VERDICT: LIVE STREAM CONFIRMED (PASS)", font=get_font(13, True), fill=GREEN_PASS)

    # Right Panel: Stale / Frozen Data Fraud
    draw_panel(d, (900, 105, 1760, 680), "PANEL B: STALE DATA / BUFFER FREEZE (ZERO VARIANCE FRAUD)")
    d.rectangle((920, 150, 1740, 480), fill=(15, 23, 42))
    
    for y_val in [200, 260, 320, 380, 440]:
        d.line((920, y_val, 1740, y_val), fill=(30, 41, 59), width=1)
        
    d.text((930, 160), "Return Coolant Temp (°C) — Mathematical Flatline Echoed by Controller", font=get_font(12, True), fill=(148, 163, 184))
    d.text((930, 250), "45.5°C", font=get_font(11), fill=(148, 163, 184))
    d.text((930, 310), "45.0°C", font=get_font(11), fill=(148, 163, 184))
    d.text((930, 370), "44.5°C", font=get_font(11), fill=(148, 163, 184))
    
    # Draw perfectly flat line
    d.line((960, 310, 1700, 310), fill=(239, 68, 68), width=4)
    for x_i in range(960, 1700, 25):
        d.ellipse((x_i - 3, 307, x_i + 3, 313), fill=(255, 255, 255))
        
    d.rectangle((1200, 220, 1680, 280), fill=(220, 38, 38))
    d.text((1220, 235), "BUFFER FROZEN: σ² = 0.0000", font=get_font(16, True), fill=(255, 255, 255))
    d.text((1220, 255), "Controller repeating cached value", font=get_font(12), fill=(254, 202, 202))
    
    d.rectangle((920, 500, 1740, 660), fill=(254, 242, 242), outline=RED_ACCENT, width=1)
    d.text((940, 515), "ANATOMY OF A TELEMETRY FRAUD (FROZEN REPEATS):", font=get_font(14, True), fill=RED_ACCENT)
    d.text((940, 540), "• Symptom: 60 identical readings down to the last float bit (45.000000°C).", font=get_font(12), fill=TEXT_MAIN)
    d.text((940, 565), "• Calculated Variance: σ² = 0.000000 K²  => Physically impossible in liquid.", font=get_font(13, True), fill=RED_ACCENT)
    d.text((940, 590), "• Root Cause: ADC driver crashed or Modbus poller stamped fresh time on stale RAM.", font=get_font(12), fill=TEXT_MUTED)
    d.text((940, 615), "• Cx Rule: ZERO VARIANCE = IMMEDIATE FAIL of plateau and consistency check.", font=get_font(12, True), fill=NAVY)
    d.text((940, 638), "• VERDICT: STALE DATA FRAUD (AUTOMATIC REJECTION)", font=get_font(13, True), fill=RED_ACCENT)

    # Bottom Full-Width: Statistical Rules & Data Block Engine
    draw_panel(d, (40, 705, 1760, 1030), "FLASH REPORT STATISTICAL AGGREGATION & DATA AUDIT RULES")
    
    rules = [
        ("Rule 01: 60-Second Mean Aggregation", "A plotted point must be the arithmetic mean of 60 raw 1-second samples: μ = (1/60) Σ x_i. If a raw point is missing or corrupted, mark the minute partial."),
        ("Rule 02: Variance Rejection Gate", "If the 60-sample sample variance σ² drops below 1e-4 K² over any continuous 5-minute dwell, the channel is classified as 'BUFFER FROZEN' and rejected."),
        ("Rule 03: Four-Summary Requirement", "Every step data block must report: (1) Minimum, (2) Maximum, (3) Arithmetic Mean, and (4) Standard Deviation. A mean without a maximum hides peak thermal excursions."),
        ("Rule 04: Never Paint Over Gaps", "If Modbus polling fails for 10 seconds, leave a gap in the timeline. Fabricating interpolation or painting the last known value forward is an audit crime."),
    ]
    y = 750
    for r_title, r_desc in rules:
        d.rectangle((60, y, 1740, y + 58), fill=(248, 250, 252), outline=PANEL_BORDER, width=1)
        d.text((80, y + 8), r_title, font=get_font(14, True), fill=NAVY)
        d.text((80, y + 32), r_desc, font=get_font(12), fill=TEXT_MUTED)
        y += 66

    path = FIG / "fig-04-sampling-and-stale-data.png"
    im.save(path, "PNG")
    return path

# ==============================================================================
# FIGURE 05: Changepoint Detection (Focus / FLOC / CPOP)
# ==============================================================================
def fig_05_changepoint():
    im, d = base_canvas(
        "CHANGEPOINT DETECTION: ONLINE (FOCUS/FLOC) vs. OFFLINE (CPOP)",
        "Algorithmic Rulers for Candidate Time Identification Across Load Step Regimes",
        "FIG 05"
    )
    
    # Top Panel: Time Series & Detector Output
    draw_panel(d, (40, 105, 1760, 620), "MULTI-TIER LOAD TEST WAVEFORMS & ALGORITHMIC TRIGGER TIMELINES")
    d.rectangle((60, 150, 1740, 480), fill=(15, 23, 42))
    
    # Horizontal reference lines
    for y_val in [200, 280, 360, 440]:
        d.line((60, y_val, 1740, y_val), fill=(30, 41, 59), width=1)
        
    d.text((70, 156), "Waveforms (00:00 - 01:20)", font=get_font(12, True), fill=(148, 163, 184))
    
    # Draw Multi-Step Profile:
    # 00-15: 30kW, 15-30: 60kW, 30-45: 90kW, 45-60: 120kW, 60-65: 132kW (Overload), 65-75: 60kW (Single Feed)
    steps = [
        (100, 420, 300, 420),    # 30kW
        (300, 360, 600, 360),    # 60kW
        (600, 300, 900, 300),    # 90kW
        (900, 240, 1200, 240),   # 120kW
        (1200, 210, 1300, 210),  # 132kW Overload
        (1300, 360, 1650, 360),  # 60kW Feeder A loss
    ]
    # Commanded Power (Yellow)
    for i in range(len(steps)):
        x0, y0, x1, y1 = steps[i]
        d.line((x0, y0, x1, y1), fill=(250, 204, 21), width=3)
        if i < len(steps) - 1:
            nx0, ny0, _, _ = steps[i+1]
            d.line((x1, y1, nx0, ny0), fill=(250, 204, 21), width=3)
            
    # Temperature profile (Cyan, with physical thermal lag tau=45s)
    t_pts = []
    for x in range(100, 1650, 5):
        if x < 300: target_y = 425
        elif x < 600: target_y = 365
        elif x < 900: target_y = 305
        elif x < 1200: target_y = 245
        elif x < 1300: target_y = 215
        else: target_y = 365
        
        # Add smooth curve + slight mid-hold anomaly at x=780
        if 760 <= x <= 820:
            target_y += 28 # Anomaly bump!
        t_pts.append((x, target_y))
        
    for i in range(len(t_pts) - 1):
        d.line((t_pts[i], t_pts[i+1]), fill=(56, 189, 248), width=2)
        
    # Detector Markers
    # 1. Commanded Steps (Trigger at x=300, 600, 900, 1200, 1300)
    cmd_triggers = [300, 600, 900, 1200, 1300]
    for ct in cmd_triggers:
        d.line((ct, 150, ct, 480), fill=(148, 163, 184), width=1)
        d.rectangle((ct - 25, 170, ct + 25, 195), fill=(30, 41, 59), outline=(148, 163, 184))
        d.text((ct - 20, 174), "STEP", font=get_font(10, True), fill=(255, 255, 255))
        
    # 2. Mid-Hold Anomaly Trigger at x=775
    d.line((775, 150, 775, 480), fill=RED_ACCENT, width=2)
    d.rectangle((720, 170, 830, 198), fill=RED_ACCENT)
    d.text((728, 174), "FLOC HIT!", font=get_font(11, True), fill=(255, 255, 255))
    
    # Bottom Indicators inside Panel
    d.rectangle((60, 500, 1740, 600), fill=(248, 250, 252), outline=PANEL_BORDER, width=1)
    d.text((80, 515), "ALGORITHMIC CANDIDATE CLASSIFICATION PROTOCOL:", font=get_font(13, True), fill=NAVY)
    d.text((80, 540), "• Hit at t=300, 600, 900: Matches commanded step time in PLC log => Human classification: 'EXPECTED STEP' (PASS)", font=get_font(12), fill=GREEN_PASS)
    d.text((80, 565), "• Hit at t=775: Uncommanded mid-hold thermal slope break => Human classification: 'INSPECT / SPLIT HOLD' (FAIL)", font=get_font(12, True), fill=RED_ACCENT)

    # Bottom Left: Online Detectors (Focus / FLOC)
    draw_panel(d, (40, 640, 880, 1030), "ONLINE CHANGEPOINT ENGINES: FOCUS & FLOC")
    d.text((55, 680), "1. Focus (Romano et al., arXiv:2607.19961):", font=get_font(14, True), fill=NAVY)
    d.text((55, 705), "• Runs sequentially in real-time during live load window.", font=get_font(12), fill=TEXT_MUTED)
    d.text((55, 725), "• Watches single physical channel (power, return temp, or flow).", font=get_font(12), fill=TEXT_MUTED)
    d.text((55, 745), "• Fixed threshold written on sheet beforehand (never retuned live).", font=get_font(12, True), fill=NAVY)
    
    d.text((55, 785), "2. FLOC (Fast Localized Online Changepoints):", font=get_font(14, True), fill=NAVY)
    d.text((55, 810), "• Dual-window variance ratio tracker for early drift detection.", font=get_font(12), fill=TEXT_MUTED)
    d.text((55, 830), "• Fires candidates on sudden valve slips or heater element dropouts.", font=get_font(12), fill=TEXT_MUTED)
    
    d.rectangle((55, 865, 860, 1010), fill=(254, 242, 242), outline=RED_ACCENT, width=1)
    d.text((70, 880), "STRICT OPERATIONAL BANS FOR ONLINE ALGORITHMS:", font=get_font(13, True), fill=RED_ACCENT)
    d.text((70, 905), "• NEVER allow an algorithm to extend dwell or move valves autonomously.", font=get_font(12), fill=TEXT_MAIN)
    d.text((70, 930), "• NEVER average two disagreeing hit times (e.g. Focus=14:10, FLOC=14:12).", font=get_font(12), fill=TEXT_MAIN)
    d.text((70, 955), "• Log both timestamps side-by-side; an engineer audits the raw samples.", font=get_font(12, True), fill=NAVY)
    d.text((70, 980), "• Quiet detector on stale channel is proof of paint, not proof of steadiness.", font=get_font(12), fill=RED_ACCENT)

    # Bottom Right: Offline Fitting (CPOP)
    draw_panel(d, (900, 640, 1760, 1030), "OFFLINE PARTITIONING: CPOP (Fearnhead et al., 2019)")
    d.text((915, 680), "Continuous Piecewise-Linear Optimal Partitioning (CPOP):", font=get_font(14, True), fill=NAVY)
    d.text((915, 705), "• Mathematical Formulation: Minimizes L2 fit cost with slope change penalty β:", font=get_font(12), fill=TEXT_MUTED)
    
    d.rectangle((915, 730, 1740, 785), fill=(241, 245, 249), outline=BLUE_MAIN, width=1)
    d.text((935, 742), "Cost = min_{K, τ}  Σ_{k=0}^K  Σ_{i=τ_k+1}^{τ_{k+1}} ( y_i - f_k(i) )²  +  β · K", font=get_font(15, True), fill=BLUE_MAIN)
    d.text((935, 765), "where K = number of changepoints, f_k = linear segment, β = pre-declared penalty", font=get_font(11), fill=TEXT_MUTED)
    
    d.text((915, 805), "RULES OF CPOP AUDIT ENGAGEMENT:", font=get_font(14, True), fill=NAVY)
    d.text((915, 830), "1. Runs ONLY after the export file is stopped and closed.", font=get_font(12), fill=TEXT_MAIN)
    d.text((915, 855), "2. Penalty β is chosen and frozen before opening the data (no curve-fitting).", font=get_font(12), fill=TEXT_MAIN)
    d.text((915, 880), "3. Applied to steady dwell boxes, excluding the known transient warm-up.", font=get_font(12), fill=TEXT_MAIN)
    
    d.rectangle((915, 915, 1740, 1010), fill=NAVY)
    d.text((935, 930), "THE GOLDEN AUDIT APHORISM:", font=get_font(13, True), fill=(250, 204, 21))
    d.text((935, 955), "\"CPOP is a ruler, not a judge. It marks where slopes break.", font=get_font(13, True), fill=(255, 255, 255))
    d.text((935, 980), "The human signature on the sheet decides whether the plateau stands or falls.\"", font=get_font(13), fill=HEADER_SUB)

    path = FIG / "fig-05-changepoint-detection.png"
    im.save(path, "PNG")
    return path

# ==============================================================================
# FIGURE 06: Thermodynamic Heat Balance Reconciliation
# ==============================================================================
def fig_06_heat_balance():
    im, d = base_canvas(
        "THERMODYNAMIC HEAT BALANCE RECONCILIATION & LOSS DECOMPOSITION",
        "First-Principles Verification: Electrical Power vs. Coolant Enthalpy vs. Air Heat",
        "FIG 06"
    )
    
    # Left Panel: Sankey & Energy Flow Stack
    draw_panel(d, (40, 105, 880, 680), "ENERGY DECOMPOSITION SANKEY (120 kW RATED DUTY)")
    
    # Electrical Input Bar (widened to X=285 so P_elec = 120.0 kW fits completely inside)
    d.rectangle((70, 160, 285, 480), fill=NAVY)
    d.text((85, 175), "ELECTRICAL POWER", font=get_font(14, True), fill=(255, 255, 255))
    d.text((85, 200), "P_elec = 120.0 kW", font=get_font(16, True), fill=(56, 189, 248))
    d.text((85, 232), "3-Phase 415V AC", font=get_font(12), fill=HEADER_SUB)
    d.text((85, 252), "Current = 167.1 A", font=get_font(12), fill=HEADER_SUB)
    d.text((85, 272), "PF = 0.999", font=get_font(12), fill=HEADER_SUB)
    
    # Three Output Streams
    # 1. Liquid Stream (82%)
    d.line((285, 220, 420, 220), fill=BLUE_MAIN, width=80)
    d.rectangle((420, 180, 860, 310), fill=(240, 253, 244), outline=BLUE_MAIN, width=2)
    d.text((438, 195), "LIQUID ENTHALPY ABSORPTION (82.0%)", font=get_font(14, True), fill=BLUE_MAIN)
    d.text((438, 222), "Q_liquid = 98.4 kW (176.5 LPM @ ΔT = 10.0 K)", font=get_font(14, True), fill=NAVY)
    d.text((438, 252), "Equation: Q = m_dot · Cp · (T_return - T_supply)", font=get_font(12), fill=TEXT_MUTED)
    d.text((438, 275), "Target Range: 97.2 kW ~ 99.6 kW (±2.0% tolerance)", font=get_font(12, True), fill=GREEN_PASS)
    
    # 2. Companion Air Load (16%)
    d.line((285, 360, 420, 360), fill=RED_ACCENT, width=35)
    d.rectangle((420, 335, 860, 435), fill=(254, 242, 242), outline=RED_ACCENT, width=2)
    d.text((438, 348), "COMPANION AIR SENSIBLE HEAT (16.0%)", font=get_font(13, True), fill=RED_ACCENT)
    d.text((438, 372), "Q_air = 19.2 kW  (CRAH Coil Verification)", font=get_font(14, True), fill=NAVY)
    d.text((438, 400), "Radiated by fan bank, VRMs & uncooled boards", font=get_font(12), fill=TEXT_MUTED)
    
    # 3. Parasitic Chassis Skin Loss (2%)
    d.line((285, 450, 420, 450), fill=(100, 116, 139), width=15)
    d.rectangle((420, 445, 860, 525), fill=(248, 250, 252), outline=PANEL_BORDER, width=2)
    d.text((438, 455), "SKIN & CABLING LOSSES (2.0%)", font=get_font(12, True), fill=NAVY)
    d.text((438, 475), "Q_loss = 2.4 kW  (Natural Convection + Busbar R*I²)", font=get_font(13, True), fill=TEXT_MUTED)
    d.text((438, 498), "Insulation barrier keeps cabinet touch temp < 40°C", font=get_font(11), fill=TEXT_MUTED)
    
    # Bottom Equation Box
    d.rectangle((70, 550, 860, 650), fill=(241, 245, 249), outline=BLUE_MAIN, width=1)
    d.text((90, 565), "FIRST-PRINCIPLES CONSERVATION OF ENERGY BALANCE:", font=get_font(13, True), fill=NAVY)
    d.text((90, 595), "P_elec  =  Q_liquid  +  Q_air  +  Q_chassis_loss  =  120.0 kW", font=get_font(16, True), fill=BLUE_MAIN)
    d.text((90, 625), "Net Enthalpy Closure Ratio: | P_elec - (Q_liq + Q_air) | / P_elec <= 3.0%", font=get_font(12, True), fill=GREEN_PASS)

    # Right Panel: Four-Quadrant Failure Case Studies
    draw_panel(d, (900, 105, 1760, 680), "FOUR DIAGNOSTIC FAILURE DISCREPANCIES (HEAT BALANCE AUDIT)")
    
    cases = [
        ("FAULT 1: THE SHORT-CIRCUITED BYPASS", "P_elec = 120 kW, Q_liquid = 22 kW (82% Heat Missing!)", "Flow is normal (176 LPM), but return temperature rise is only 1.8 K instead of 10.0 K. Internal bypass valve V-105 left open or heater baffle seal ruptured. Cold liquid short-circuits around elements.", RED_ACCENT),
        ("FAULT 2: LOW-FLOW CAVITATION EXCURSION", "P_elec = 120 kW, ΔT = 24.5 K (Dangerous Boiling Spike!)", "Flow collapsed to 72 LPM due to clogged 50μm strainer. Return temperature skyrockets to 59.5°C. Power looks steady, but extreme ΔT threatens hose EPDM lining and risks heater dry-fire.", RED_ACCENT),
        ("FAULT 3: THE AIR-REVERSE THEFT", "Q_air Negative or Unmeasured", "If air containment plenum is inverted, hot air recirculates into load bank intakes. Inlet air exceeds 42°C, causing companion air heaters to trip on high intake limits before liquid dwell finishes.", AMBER_WARN),
        ("FAULT 4: TRANSIENT PREMATURE EVALUATION", "Heat Balance Taken During Minute 01 of Step", "Massive cold thermal inertia of 150 kg stainless steel shell absorbs 35 kW transient heat. Evaluating balance before 10-minute stabilization falsely accuses heaters of under-power.", NAVY),
    ]
    y = 150
    for c_title, c_stats, c_desc, c_col in cases:
        d.rectangle((920, y, 1740, y + 115), fill=(255, 255, 255), outline=c_col, width=1)
        d.text((940, y + 8), c_title, font=get_font(13, True), fill=c_col)
        d.text((940, y + 30), c_stats, font=get_font(12, True), fill=NAVY)
        cd_lines = wrap_text(d, c_desc, get_font(11), 770)
        for idx, cdl in enumerate(cd_lines):
            d.text((940, y + 52 + idx * 17), cdl, font=get_font(11), fill=TEXT_MUTED)
        y += 128

    # Bottom Full-Width Table: Four-Step Heat Balance Reconciliation Data (fixed column spacing so STEP and COMMAND never collide)
    draw_panel(d, (40, 705, 1760, 1030), "REPRESENTATIVE FLASH REPORT HEAT RECONCILIATION TABLE (FOUR LOAD STEPS)")
    t_headers = ["STEP", "COMMAND", "P_ELEC (kW)", "FLOW (LPM)", "T_IN (°C)", "T_OUT (°C)", "ΔT (K)", "Q_LIQ (kW)", "Q_AIR (kW)", "CLOSURE", "STATUS"]
    t_cols = [70, 205, 330, 465, 600, 715, 835, 950, 1095, 1245, 1480]
    
    d.rectangle((60, 745, 1740, 775), fill=NAVY)
    for i, th in enumerate(t_headers):
        d.text((t_cols[i], 752), th, font=get_font(12, True), fill=(255, 255, 255))
        
    t_rows = [
        ("Step 1 (25%)", "30.0 kW", "30.1 kW", "176.4 LPM", "35.01", "37.52", "2.51 K", "24.6 kW", "4.8 kW", "97.7% (Pass)", "BALANCED", GREEN_PASS),
        ("Step 2 (50%)", "60.0 kW", "60.2 kW", "176.5 LPM", "35.04", "40.06", "5.02 K", "49.3 kW", "9.6 kW", "97.8% (Pass)", "BALANCED", GREEN_PASS),
        ("Step 3 (75%)", "90.0 kW", "90.1 kW", "176.6 LPM", "35.06", "42.59", "7.53 K", "74.0 kW", "14.4 kW", "98.1% (Pass)", "BALANCED", GREEN_PASS),
        ("Step 4 (100%)", "120.0 kW", "120.2 kW", "176.5 LPM", "35.08", "45.12", "10.04 K", "98.6 kW", "19.2 kW", "98.0% (Pass)", "BALANCED", GREEN_PASS),
        ("Step 5 (110%)", "132.0 kW", "132.3 kW", "176.7 LPM", "35.10", "46.15", "11.05 K", "108.6 kW", "21.1 kW", "98.0% (Pass)", "OVERLOAD VISIT", BLUE_MAIN),
    ]
    y = 785
    for st, cmd, pe, fl, tin, tout, dt, ql, qa, clo, stat, scol in t_rows:
        d.rectangle((60, y, 1740, y + 42), fill=(255, 255, 255) if (y//40)%2==0 else (248, 250, 252))
        d.text((t_cols[0], y + 10), st, font=get_font(12, True), fill=NAVY)
        d.text((t_cols[1], y + 10), cmd, font=get_font(12), fill=TEXT_MUTED)
        d.text((t_cols[2], y + 10), pe, font=get_font(12, True), fill=NAVY)
        d.text((t_cols[3], y + 10), fl, font=get_font(12), fill=TEXT_MAIN)
        d.text((t_cols[4], y + 10), tin, font=get_font(12), fill=TEXT_MUTED)
        d.text((t_cols[5], y + 10), tout, font=get_font(12), fill=TEXT_MUTED)
        d.text((t_cols[6], y + 10), dt, font=get_font(12, True), fill=BLUE_MAIN)
        d.text((t_cols[7], y + 10), ql, font=get_font(12, True), fill=BLUE_MAIN)
        d.text((t_cols[8], y + 10), qa, font=get_font(12), fill=RED_ACCENT)
        d.text((t_cols[9], y + 10), clo, font=get_font(12, True), fill=GREEN_PASS)
        d.text((t_cols[10], y + 10), stat, font=get_font(12, True), fill=scol)
        y += 44

    path = FIG / "fig-06-heat-balance-reconciliation.png"
    im.save(path, "PNG")
    return path

# ==============================================================================
# FIGURE 07: 2N Single-Feed Fault Transient Waveforms
# ==============================================================================
def fig_07_single_feed_transient():
    im, d = base_canvas(
        "2N SINGLE-FEED LOSS TRANSIENT: ELECTROMECHANICAL & CONTROL DYNAMICS",
        "Breaker Trip, <20ms Contactor Drop, Zero Control Bus Brownout & Pressure Surge",
        "FIG 07"
    )
    
    # Waveform Display Area
    draw_panel(d, (40, 105, 1760, 680), "SYNCHRONIZED OSCILLOGRAM: FEEDER A INTENTIONAL BREAKER TRIP (TIME: -5s TO +25s)")
    d.rectangle((60, 150, 1740, 650), fill=(15, 23, 42))
    
    # Vertical Trip Line at t = 500 (T_trip = 0.00s)
    trip_x = 520
    d.line((trip_x, 150, trip_x, 650), fill=(239, 68, 68), width=2)
    d.rectangle((trip_x - 70, 160, trip_x + 70, 190), fill=RED_ACCENT)
    d.text((trip_x - 62, 168), "t = 0.00s TRIP!", font=get_font(12, True), fill=(255, 255, 255))
    
    # Grid lines
    for gy in [230, 310, 390, 470, 550]:
        d.line((60, gy, 1740, gy), fill=(30, 41, 59), width=1)
        
    # Channel 1: Feeder A AC Voltage (Sky Blue)
    d.text((80, 205), "CH1: Feeder A AC Voltage (415VAC Line-to-Line)", font=get_font(12, True), fill=(56, 189, 248))
    d.line((100, 230, trip_x, 230), fill=(56, 189, 248), width=3)
    d.line((trip_x, 230, trip_x + 2, 280), fill=(56, 189, 248), width=3)
    d.line((trip_x + 2, 280, 1700, 280), fill=(56, 189, 248), width=3) # Drops to 0V
    d.text((1550, 260), "0.0 VAC", font=get_font(12, True), fill=(56, 189, 248))
    
    # Channel 2: Contactor Coil & Contacts (Clearing < 20ms)
    d.text((80, 290), "CH2: Bank 1 & 2 Main Contactor Auxiliary State", font=get_font(12, True), fill=(250, 204, 21))
    d.line((100, 310, trip_x + 14, 310), fill=(250, 204, 21), width=3)
    d.line((trip_x + 14, 310, trip_x + 14, 350), fill=(250, 204, 21), width=3)
    d.line((trip_x + 14, 350, 1700, 350), fill=(250, 204, 21), width=3)
    d.text((trip_x + 25, 325), "Δt = 14 ms (< 20ms REQUIREMENT MET)", font=get_font(12, True), fill=(250, 204, 21))
    
    # Channel 3: Commanded & Active Load (Drops from 120kW to 60kW) - shifted 120.0 kW label below line so zero overlap with CH3 title
    d.text((80, 368), "CH3: Active Load Bank Electrical Power (kW)", font=get_font(12, True), fill=(22, 163, 74))
    d.line((100, 390, trip_x + 15, 390), fill=(22, 163, 74), width=4)
    d.line((trip_x + 15, 390, trip_x + 25, 430), fill=(22, 163, 74), width=4)
    d.line((trip_x + 25, 430, 1700, 430), fill=(22, 163, 74), width=4) # 60kW steady
    d.text((100, 400), "120.0 kW (Full Load)", font=get_font(12, True), fill=(22, 163, 74))
    d.text((1530, 408), "60.0 kW (Feeder B Only)", font=get_font(12, True), fill=(22, 163, 74))
    
    # Channel 4: 24VDC PLC & Sensor Control Bus (Zero Brownout!)
    d.text((80, 450), "CH4: 24VDC Supervisory PLC & Sensor Power Bus", font=get_font(12, True), fill=(168, 85, 247))
    d.line((100, 470, 1700, 470), fill=(168, 85, 247), width=3) # Perfectly flat line!
    d.text((trip_x + 25, 452), "ZERO BROWNOUT DIP! (Diode OR-ed Dual PSU holds 24.1VDC)", font=get_font(12, True), fill=(168, 85, 247))
    d.text((1550, 452), "24.1 VDC (FLAT)", font=get_font(12, True), fill=(168, 85, 247))
    
    # Channel 5: Secondary Coolant Pressure Waveform (Hydraulic Surge)
    d.text((80, 530), "CH5: Coolant Manifold Differential Pressure (kPa)", font=get_font(12, True), fill=(244, 63, 94))
    # Draw small damped pressure ripple at trip_x
    p_pts = [(100, 550), (trip_x, 550), (trip_x + 10, 535), (trip_x + 25, 560), (trip_x + 45, 545), (trip_x + 70, 550), (1700, 550)]
    for i in range(len(p_pts) - 1):
        d.line((p_pts[i], p_pts[i+1]), fill=(244, 63, 94), width=2)
    d.text((trip_x + 85, 535), "Minor Pressure Pulse: ΔP_surge = +8 kPa (Damped, No Water Hammer)", font=get_font(12), fill=(244, 63, 94))

    # Bottom Left: Acceptance Rules for Single-Feed Loss (spaced cleanly so FATAL 2N FAIL sits below Criterion 5)
    draw_panel(d, (40, 705, 880, 1030), "2N DROP TEST PASS/FAIL ACCEPTANCE CRITERIA")
    
    crit = [
        ("Criterion 1: Contactor Clearing Time", "< 20 milliseconds", "Observed: 14 ms (PASS)", GREEN_PASS),
        ("Criterion 2: Feeder B Current Transient", "< 115% nominal rated", "Observed: 104% (No upstream trip)", GREEN_PASS),
        ("Criterion 3: Control Bus Voltage Ripple", "< 50 mV dip", "Observed: 12 mV dip (Zero brownout)", GREEN_PASS),
        ("Criterion 4: Modbus / Telemetry Stream", "Zero missed packets", "Observed: Telemetry stream continuous", GREEN_PASS),
        ("Criterion 5: Shedding Accuracy", "50.0% ± 1.0% load shed", "Observed: Shed 60.1 kW out of 120.2 kW", GREEN_PASS),
    ]
    y = 744
    for name, lim, obs, col in crit:
        d.rectangle((60, y, 860, y + 43), fill=(255, 255, 255), outline=PANEL_BORDER, width=1)
        d.text((75, y + 6), name, font=get_font(13, True), fill=NAVY)
        d.text((420, y + 5), lim, font=get_font(11), fill=TEXT_MUTED)
        d.text((420, y + 23), obs, font=get_font(12, True), fill=col)
        y += 48
        
    d.text((60, 994), "FATAL 2N FAIL: If Feeder A drop reboots the PLC or drops Modbus, the unit FAILS.", font=get_font(12, True), fill=RED_ACCENT)

    # Bottom Right: Fail-Safe Physical Implementation (spaced cleanly so all 4 items stay above dark box)
    draw_panel(d, (900, 705, 1760, 1030), "PHYSICAL IMPLEMENTATION: DIODE-OR DUAL 24VDC ARCHITECTURE")
    d.text((920, 742), "How Zero-Dip Control Immunity is Achieved in Hardware:", font=get_font(14, True), fill=NAVY)
    
    notes = [
        ("1. Redundant Power Supply Units (PSU-A & PSU-B):", "PSU-A is fed exclusively from Feeder A (415V/230V); PSU-B from Feeder B. Industrial DIN-rail 24VDC / 10A."),
        ("2. Active Schottky Diode OR-ing Redundancy Module:", "Combines outputs into a common 24VDC control bus with zero crossover switching transient (< 0.1ms)."),
        ("3. Hold-Up Buffer Capacitor (40ms Energy Storage):", "Provides auxiliary capacitive hold-up to absorb any line voltage sag during utility transfer switch transitions."),
        ("4. Segregated Contactor Control Circuits:", "Contactor coils for Bank 1/2 are interlocked with Feeder A; Bank 3/4 with Feeder B. Pure spring-return drop."),
    ]
    y = 770
    for n_title, n_desc in notes:
        d.text((920, y), n_title, font=get_font(12, True), fill=BLUE_MAIN)
        d.text((920, y + 20), n_desc, font=get_font(11), fill=TEXT_MUTED)
        y += 46
        
    d.rectangle((920, 962, 1740, 1015), fill=NAVY)
    d.text((940, 974), "FLASH REPORT REQUIREMENT: Test both paths sequentially.", font=get_font(13, True), fill=(255, 255, 255))
    d.text((940, 994), "Trip Feeder A, restore, dwell, then trip Feeder B. Both must pass.", font=get_font(12), fill=HEADER_SUB)

    path = FIG / "fig-07-single-feed-transient.png"
    im.save(path, "PNG")
    return path

if __name__ == "__main__":
    print("Generating Engineering Diagrams for Book 02...")
    FIG.mkdir(parents=True, exist_ok=True)
    p1 = fig_01_flash_report()
    print("Generated:", p1)
    p2 = fig_02_telemetry_pipeline()
    print("Generated:", p2)
    p3 = fig_03_multicabinet_uniformity()
    print("Generated:", p3)
    p4 = fig_04_sampling_and_stale()
    print("Generated:", p4)
    p5 = fig_05_changepoint()
    print("Generated:", p5)
    p6 = fig_06_heat_balance()
    print("Generated:", p6)
    p7 = fig_07_single_feed_transient()
    print("Generated:", p7)
    print("All 7 Engineering Diagrams generated successfully for Book 02!")
