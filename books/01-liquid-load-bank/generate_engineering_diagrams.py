#!/usr/bin/env python3
"""
Generate High-Quality Industrial Engineering Diagrams for:
Design and Build a Liquid Load Bank for NVL72 Racks

Uses Pillow with clean vector-style antialiasing, high-contrast crisp line weights,
standard engineering symbols (P&ID ISA-5.1, electrical single-line, cutaways, waveforms).
"""
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path("/Users/geese/Downloads/book/books/01-liquid-load-bank")
FIG = ROOT / "figures"
FONT_DIR = ROOT / "fonts"

W = 1800
H = 1100

# Color Palette (High-Contrast Professional Engineering Clean Style)
BG = (252, 252, 254)          # Clean off-white
HEADER_BG = (15, 23, 42)      # Slate-900 dark header
HEADER_TEXT = (255, 255, 255)
HEADER_SUB = (148, 163, 184)  # Slate-400
PANEL_BG = (255, 255, 255)
PANEL_BORDER = (203, 213, 225)# Slate-300
GRID = (241, 245, 249)        # Slate-100

NAVY = (30, 41, 59)           # Slate-800
PIPE_COLD = (2, 132, 199)     # Sky-600 Blue
PIPE_HOT = (225, 29, 72)      # Rose-600 Red
VALVE_BODY = (100, 116, 139)  # Slate-500
GREEN = (22, 163, 74)         # Emerald-600
AMBER = (217, 119, 6)         # Amber-600
RED = (220, 38, 38)           # Red-600
PURPLE = (126, 34, 206)       # Purple-700
TEXT_MAIN = (15, 23, 42)      # Dark text
TEXT_MUTED = (71, 85, 105)    # Medium slate

def get_font(size, bold=False):
    ttf = FONT_DIR / ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf")
    return ImageFont.truetype(str(ttf), size)

def base_canvas(title, subtitle, fig_no=""):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    
    # Background subtle grid
    for x in range(0, W, 50):
        d.line((x, 100, x, H), fill=GRID, width=1)
    for y in range(100, H, 50):
        d.line((0, y, W, y), fill=GRID, width=1)
        
    # Header Bar
    d.rectangle((0, 0, W, 90), fill=HEADER_BG)
    d.rectangle((0, 86, W, 90), fill=PIPE_COLD)
    
    if fig_no:
        d.rectangle((30, 20, 130, 70), fill=PIPE_COLD)
        d.text((45, 32), fig_no, font=get_font(26, True), fill=HEADER_TEXT)
        x_text = 150
    else:
        x_text = 40
        
    d.text((x_text, 18), title, font=get_font(28, True), fill=HEADER_TEXT)
    d.text((x_text, 54), subtitle, font=get_font(18, False), fill=HEADER_SUB)
    
    # Footer border
    d.rectangle((0, H - 36, W, H), fill=(241, 245, 249))
    d.line((0, H - 36, W, H - 36), fill=PANEL_BORDER, width=1)
    d.text((40, H - 26), "DATA CENTER FIELD GUIDES  |  VOLUME 01: DESIGN & BUILD A LIQUID LOAD BANK", font=get_font(13, True), fill=TEXT_MUTED)
    d.text((W - 360, H - 26), "ISO/ISA REFERENCE SPECIFICATION", font=get_font(12, False), fill=TEXT_MUTED)
    
    return im, d

def draw_card(d, xy, title, fill=PANEL_BG, border=PANEL_BORDER, badge="", badge_color=PIPE_COLD):
    x0, y0, x1, y1 = xy
    d.rectangle(xy, fill=fill, outline=border, width=2)
    d.rectangle((x0, y0, x1, y0 + 34), fill=(248, 250, 252))
    d.line((x0, y0 + 34, x1, y0 + 34), fill=border, width=1)
    d.text((x0 + 16, y0 + 8), title, font=get_font(16, True), fill=TEXT_MAIN)
    if badge:
        btw = d.textlength(badge, font=get_font(12, True))
        bx1 = min(x1 - 10, 1720)
        bx0 = bx1 - btw - 16
        d.rectangle((bx0, y0 + 6, bx1, y0 + 28), fill=badge_color)
        d.text((bx0 + 8, y0 + 8), badge, font=get_font(12, True), fill=(255, 255, 255))

def draw_valve(d, x, y, size=16, color=VALVE_BODY, label=""):
    # Two opposing triangles
    d.polygon([(x - size, y - size), (x - size, y + size), (x + size, y)], fill=color)
    d.polygon([(x + size, y - size), (x + size, y + size), (x - size, y)], fill=color)
    d.line((x, y, x, y - size - 6), fill=NAVY, width=2)
    d.line((x - size//2, y - size - 6, x + size//2, y - size - 6), fill=NAVY, width=3)
    if label:
        d.text((x - 20, y + size + 6), label, font=get_font(12, True), fill=TEXT_MUTED)

def draw_danfoss_coupling(d, x, y, label="Danfoss FD83", align="center"):
    # High-flow dual interlock coupling symbol
    d.rectangle((x - 22, y - 18, x + 22, y + 18), fill=(226, 232, 240), outline=NAVY, width=2)
    d.rectangle((x - 14, y - 24, x + 14, y - 18), fill=AMBER, outline=NAVY, width=2) # Dual interlock latch
    d.rectangle((x - 14, y + 18, x + 14, y + 24), fill=AMBER, outline=NAVY, width=2)
    d.line((x - 2, y - 16, x - 2, y + 16), fill=NAVY, width=3)
    d.line((x + 2, y - 16, x + 2, y + 16), fill=NAVY, width=3)
    f_lbl = get_font(12, True)
    f_sub = get_font(11, False)
    w_lbl = d.textlength(label, font=f_lbl)
    w_sub = d.textlength("Dual Interlock", font=f_sub)
    if align == "outside_left":
        tx_lbl = x - 28 - w_lbl
        tx_sub = x - 28 - w_sub
    elif align == "right":
        tx_lbl = x + 20 - w_lbl
        tx_sub = x + 20 - w_sub
    elif align == "left":
        tx_lbl = x - 22
        tx_sub = x - 22
    else:
        tx_lbl = x - w_lbl / 2
        tx_sub = x - w_sub / 2
    d.text((tx_lbl, y + 28), label, font=f_lbl, fill=PIPE_COLD)
    d.text((tx_sub, y + 44), "Dual Interlock", font=f_sub, fill=TEXT_MUTED)

def draw_sensor(d, x, y, code, desc=""):
    # Circle with instrument code
    r = 22
    d.ellipse((x - r, y - r, x + r, y + r), fill=(255, 255, 255), outline=NAVY, width=2)
    d.text((x - (len(code)*5), y - 9), code, font=get_font(13, True), fill=NAVY)
    if desc:
        d.text((x - 35, y + r + 4), desc, font=get_font(11, False), fill=TEXT_MUTED)

# -------------------------------------------------------------
# FIGURE 1: CDU vs Rack Boundary Architecture & 80:20 Split
# -------------------------------------------------------------
def fig_01_boundary():
    im, d = base_canvas(
        "PRIMARY CDU FACILITY LOOP vs. SECONDARY RACK-SIDE LOAD BANK BOUNDARY",
        "Hydraulic demarcation, dual-interlock connection points, and 80:20 liquid/air thermal split",
        "FIG 01"
    )
    
    # 3 Main Zones
    # Zone 1: Primary Facility Loop
    draw_card(d, (40, 120, 520, 780), "PRIMARY FACILITY LOOP (FWS)", badge="BUILDING SIDE", badge_color=TEXT_MUTED)
    # Zone 2: CDU System
    draw_card(d, (560, 120, 1140, 780), "COOLANT DISTRIBUTION UNIT", badge="CDU BOUNDARY", badge_color=NAVY)
    # Zone 3: Secondary Rack-Side Load Bank
    draw_card(d, (1180, 120, 1760, 780), "SECONDARY RACK LOAD BANK", badge="RACK STAND-IN SIDE", badge_color=PIPE_COLD)
    
    # Primary Components
    d.rectangle((80, 220, 480, 320), fill=(241, 245, 249), outline=PANEL_BORDER, width=2)
    d.text((100, 240), "Facility Chilled Water / Cooling Tower", font=get_font(16, True), fill=NAVY)
    d.text((100, 270), "Primary Supply: ~15°C - 30°C (FWS)", font=get_font(14), fill=PIPE_COLD)
    d.text((100, 292), "Water Treatment: Building HVAC Chem", font=get_font(13), fill=TEXT_MUTED)
    
    d.rectangle((80, 400, 480, 500), fill=(241, 245, 249), outline=PANEL_BORDER, width=2)
    d.text((100, 420), "Primary Return Manifold", font=get_font(16, True), fill=NAVY)
    d.text((100, 450), "Primary Return: ~25°C - 42°C", font=get_font(14), fill=PIPE_HOT)
    
    # CDU Internals
    # Heat Exchanger
    d.rectangle((590, 200, 825, 460), fill=(224, 231, 255), outline=PURPLE, width=2)
    d.text((605, 220), "Plate Heat Exchanger", font=get_font(15, True), fill=PURPLE)
    d.text((635, 245), "(PHE Boundary)", font=get_font(14, True), fill=PURPLE)
    d.text((610, 290), "• Liquid-to-Liquid", font=get_font(13), fill=NAVY)
    d.text((610, 315), "• 4°C Approach ATD", font=get_font(13), fill=NAVY)
    d.text((610, 340), "• Complete Isolation", font=get_font(13), fill=NAVY)
    d.text((610, 365), "  (Zero Cross-Fluid)", font=get_font(13), fill=NAVY)
    
    # Secondary Pump Skid
    d.rectangle((855, 200, 1110, 360), fill=(241, 245, 249), outline=NAVY, width=2)
    d.text((875, 220), "Secondary VFD Pumps", font=get_font(16, True), fill=NAVY)
    d.text((875, 250), "• N+1 / 2N Redundancy", font=get_font(14), fill=NAVY)
    d.text((875, 275), "• High Flow: 150-200+ LPM", font=get_font(14), fill=PIPE_COLD)
    d.text((875, 300), "• Expansion Tank & Res", font=get_font(13), fill=TEXT_MUTED)
    
    # Dew Point Controller
    d.rectangle((590, 520, 1115, 740), fill=(254, 243, 199), outline=AMBER, width=2)
    d.text((610, 540), "CRITICAL: Dew Point Interlock Control (TDp)", font=get_font(16, True), fill=AMBER)
    d.text((610, 575), "• Room Humidity & Temp Sensor feeds Hall Dew Point (TDp)", font=get_font(13), fill=NAVY)
    d.text((610, 605), "• Rule: Supply Temp T_in >= TDp + 2.0°C Safety Margin", font=get_font(13, True), fill=RED)
    d.text((610, 635), "• If T_in approaches TDp: Modulating bypass valve closes immediately", font=get_font(12), fill=NAVY)
    d.text((610, 665), "• Failure mode without interlock: Condensation drips onto busbars!", font=get_font(12, True), fill=RED)
    
    # Pipes: Primary
    d.line((480, 270, 590, 270), fill=PIPE_COLD, width=6)
    d.line((480, 440, 590, 440), fill=PIPE_HOT, width=6)
    
    # Secondary Loop from CDU to Load Bank
    # Supply Pipe
    d.line((1110, 270, 1260, 270), fill=PIPE_COLD, width=8)
    # Return Pipe
    d.line((1260, 420, 1000, 420), fill=PIPE_HOT, width=8)
    d.line((1000, 420, 1000, 460), fill=PIPE_HOT, width=8)
    d.line((1000, 460, 825, 460), fill=PIPE_HOT, width=8)
    
    # Danfoss Couplings at the Boundary
    draw_danfoss_coupling(d, 1160, 270, "Danfoss FD83 Supply", align="center")
    draw_danfoss_coupling(d, 1160, 420, "Danfoss FD83 Return", align="center")
    
    # Secondary Load Bank Internals
    d.rectangle((1260, 200, 1730, 600), fill=(248, 250, 252), outline=PIPE_COLD, width=2)
    d.text((1280, 220), "Liquid Load Bank Core (120 kW)", font=get_font(18, True), fill=PIPE_COLD)
    d.text((1280, 255), "• Multistage Immersion Elements", font=get_font(14), fill=NAVY)
    d.text((1280, 280), "• Full Hydraulic Drop Emulation", font=get_font(14), fill=NAVY)
    d.text((1280, 305), "• Modbus-TCP / Local PLC", font=get_font(14), fill=NAVY)
    d.text((1280, 330), "• PT100 Supply & Return RTDs", font=get_font(14), fill=PIPE_HOT)
    d.text((1280, 355), "• Dual High/Low Pressure Taps", font=get_font(14), fill=NAVY)
    d.text((1280, 380), "• High-Flow Turbine/Mag Meter", font=get_font(14), fill=PIPE_COLD)
    
    # Bottom Zone: 80/20 Air-Liquid Split
    draw_card(d, (40, 810, 1760, 1040), "THE 80:20 / 85:15 AIR-LIQUID THERMAL SPLIT PRINCIPLE", badge="FACILITY INTEGRATION", badge_color=PIPE_HOT)
    d.rectangle((60, 860, 900, 1010), fill=(239, 246, 255), outline=PIPE_COLD, width=1)
    d.text((80, 875), "80% - 85% Thermal Heat: Liquid Loop (Cold Plates)", font=get_font(16, True), fill=PIPE_COLD)
    d.text((80, 905), "• Direct conduction from GPU & CPU silicon dies into secondary liquid loop.", font=get_font(13), fill=NAVY)
    d.text((80, 930), "• Liquid load bank must absorb this primary 80-85% bulk load (e.g., 100-120kW).", font=get_font(13), fill=NAVY)
    d.text((80, 955), "• Flow: 150 - 200+ LPM per rack at standard ΔT = 10K.", font=get_font(13, True), fill=NAVY)
    
    d.rectangle((930, 860, 1740, 1010), fill=(255, 241, 242), outline=PIPE_HOT, width=1)
    d.text((950, 875), "15% - 20% Residual Sensible Heat: Hall Air (CRAH)", font=get_font(16, True), fill=PIPE_HOT)
    d.text((950, 905), "• Radiated by optical transceivers, VRM stages, DIMMs, busbars & power shelves.", font=get_font(13), fill=NAVY)
    d.text((950, 930), "• MUST be paired with companion air-cooled load bank (8-15kW) in hall testing!", font=get_font(13, True), fill=RED)
    d.text((950, 955), "• Critical Rule: Liquid-only tests leave room CRAH & containment unverified.", font=get_font(13), fill=NAVY)
    
    path = FIG / "fig-01-boundary-architecture.png"
    im.save(path, "PNG")
    return path

# -------------------------------------------------------------
# FIGURE 2: P&ID Diagram (ISA-5.1)
# -------------------------------------------------------------
def fig_02_pid():
    im, d = base_canvas(
        "LIQUID LOAD BANK PIPING & INSTRUMENTATION DIAGRAM (P&ID)",
        "ISA-5.1 Standard: Danfoss FD83 couplings, dual isolation, straight runs, and bypass loop",
        "FIG 02"
    )
    
    # Boundary Frame of Load Bank Chassis
    d.rectangle((260, 140, 1680, 960), fill=(255, 255, 255), outline=NAVY, width=3)
    d.text((285, 160), "LOAD BANK ENCLOSURE CHASSIS BOUNDARY (STAINLESS 304 PIPING)", font=get_font(16, True), fill=NAVY)
    
    # Flow Lines
    # Supply Main Line: enters at X=80, Y=300 -> X=1240
    d.line((80, 300, 1240, 300), fill=PIPE_COLD, width=8)
    # Return Main Line: exits at X=1240, Y=780 -> X=80
    d.line((1240, 780, 80, 780), fill=PIPE_HOT, width=8)
    
    # Arrows for flow direction
    # Supply arrow
    d.polygon([(490, 300), (470, 290), (470, 310)], fill=PIPE_COLD)
    d.polygon([(900, 300), (880, 290), (880, 310)], fill=PIPE_COLD)
    # Return arrow
    d.polygon([(880, 780), (900, 770), (900, 790)], fill=PIPE_HOT)
    d.polygon([(470, 780), (490, 770), (490, 790)], fill=PIPE_HOT)
    
    # Couplings at Boundary (Left Edge at X=260, labels placed cleanly to the left of X=235 so chassis line never crosses text)
    draw_danfoss_coupling(d, 260, 300, "SUPPLY: Danfoss FD83-2051", align="outside_left")
    draw_danfoss_coupling(d, 260, 780, "RETURN: Danfoss FD83-2051", align="outside_left")
    
    # Supply Isolation Valve V-101
    draw_valve(d, 360, 300, size=20, color=NAVY, label="V-101 (Isolation)")
    
    # Pre-commissioning Flushing Bypass Loop (starts at X=455, completely clear of V-101 label)
    d.line((455, 300, 455, 500), fill=PIPE_COLD, width=4)
    d.line((455, 500, 520, 500), fill=PIPE_COLD, width=4)
    # Bypass Strainer (Filter)
    d.rectangle((520, 480, 580, 520), fill=(254, 243, 199), outline=AMBER, width=2)
    d.text((526, 492), "50 μm", font=get_font(12, True), fill=NAVY)
    d.text((505, 526), "Flushing Strainer", font=get_font(11), fill=TEXT_MUTED)
    d.line((580, 500, 740, 500), fill=PIPE_HOT, width=4)
    draw_valve(d, 640, 500, size=16, color=AMBER, label="V-105 (Bypass)")
    d.line((740, 500, 740, 780), fill=PIPE_HOT, width=4)
    
    # Upstream Straight Section 10D
    d.rectangle((450, 275, 585, 285), fill=AMBER)
    d.text((462, 255), "≥ 10D Straight Run", font=get_font(12, True), fill=AMBER)
    
    # Flow Meter FT-101
    d.rectangle((600, 280, 680, 320), fill=(241, 245, 249), outline=NAVY, width=2)
    d.text((615, 292), "METER", font=get_font(13, True), fill=NAVY)
    draw_sensor(d, 640, 210, "FT", "Flow Transmitter")
    d.line((640, 232, 640, 280), fill=NAVY, width=2)
    
    # Downstream Straight Section 5D
    d.rectangle((700, 275, 780, 285), fill=AMBER)
    d.text((710, 255), "≥ 5D Run", font=get_font(12, True), fill=AMBER)
    
    # Temperature Transmitter TT-101 (Supply)
    draw_sensor(d, 830, 210, "TT1", "Inlet Pt100 RTD")
    d.line((830, 232, 830, 300), fill=NAVY, width=2)
    
    # Pressure Tap High PT-101H
    draw_sensor(d, 950, 210, "PT1", "Supply Press.")
    d.line((950, 232, 950, 300), fill=NAVY, width=2)
    
    # Modulating Flow Control Valve TCV-101
    draw_valve(d, 1080, 300, size=22, color=PIPE_COLD, label="TCV-101 (Modulating)")
    d.rectangle((1065, 240, 1095, 266), fill=(254, 243, 199), outline=AMBER, width=2)
    d.text((1072, 246), "M", font=get_font(14, True), fill=NAVY)
    d.line((1080, 266, 1080, 280), fill=NAVY, width=2)
    
    # Heater Core Vessel
    d.rectangle((1210, 235, 1620, 840), fill=(255, 241, 242), outline=RED, width=3)
    d.text((1235, 255), "ELECTRIC IMMERSION HEATER VESSEL", font=get_font(15, True), fill=RED)
    d.text((1235, 280), "Total: 120 kW (3-Phase Stepped)", font=get_font(13, True), fill=NAVY)
    
    # Internal heater stages (routed via left supply manifold at X=1240 and right return manifold at X=1590 so zero lines cross text!)
    d.line((1240, 300, 1240, 590), fill=PIPE_COLD, width=5)
    d.line((1590, 370, 1590, 780), fill=PIPE_HOT, width=5)
    d.line((1590, 780, 1240, 780), fill=PIPE_HOT, width=8)
    for idx, (label, kw) in enumerate([("Stage 1", "30 kW"), ("Stage 2", "45 kW"), ("Stage 3", "45 kW")]):
        y_box = 330 + idx * 110
        d.rectangle((1270, y_box, 1560, y_box + 80), fill=(255, 255, 255), outline=RED, width=2)
        d.text((1288, y_box + 15), f"{label}: {kw} Heating Bank", font=get_font(14, True), fill=RED)
        d.text((1288, y_box + 42), "Incoloy 800 Elements / Over-temp Snap", font=get_font(12), fill=TEXT_MUTED)
        # Clean side manifold connections
        d.line((1240, y_box + 40, 1270, y_box + 40), fill=PIPE_COLD, width=4)
        d.line((1560, y_box + 40, 1590, y_box + 40), fill=PIPE_HOT, width=4)
        
    # Pressure Tap Low PT-102L
    draw_sensor(d, 950, 870, "PT2", "Return Press.")
    d.line((950, 848, 950, 780), fill=NAVY, width=2)
    
    # Differential Pressure Transmitter DPT-101 (routed neatly to the right so sense lines never cut through labels)
    draw_sensor(d, 950, 540, "DPT", "Delta-P (Rack Drop)")
    d.line((950, 300, 950, 518), fill=AMBER, width=2)
    d.line((950, 590, 950, 780), fill=AMBER, width=2)
    
    # Temperature Transmitter TT-102 (Return)
    draw_sensor(d, 830, 870, "TT2", "Outlet Pt100 RTD")
    d.line((830, 848, 830, 780), fill=NAVY, width=2)
    
    # Return Isolation Valve V-102
    draw_valve(d, 350, 780, size=20, color=NAVY, label="V-102 (Isolation)")
    
    # Ancillaries: Automatic Air Vent (AAV) at top
    d.line((1460, 235, 1460, 180), fill=PIPE_COLD, width=3)
    draw_valve(d, 1460, 180, size=12, color=NAVY)
    d.ellipse((1445, 145, 1475, 165), fill=(241, 245, 249), outline=NAVY, width=2)
    d.text((1485, 150), "AAV-101 (Auto Vent)", font=get_font(12, True), fill=NAVY)
    
    # Drain Valve at lowest point
    d.line((1260, 840, 1260, 885), fill=PIPE_HOT, width=3)
    draw_valve(d, 1260, 885, size=12, color=NAVY)
    d.rectangle((1250, 905, 1270, 915), fill=AMBER, outline=NAVY, width=2)
    d.text((1280, 900), "V-103 Drain (Captive Cap)", font=get_font(12, True), fill=NAVY)
    
    # Drip Tray and Leak Rope
    d.rectangle((240, 932, 1660, 950), fill=(226, 232, 240), outline=NAVY, width=2)
    d.line((260, 941, 1640, 941), fill=AMBER, width=3)
    d.text((260, 912), "Full Containment Drip Tray with Conductive Leak Sensing Rope (LS-101)", font=get_font(13, True), fill=AMBER)
    
    path = FIG / "fig-02-loadbank-pid.png"
    im.save(path, "PNG")
    return path

# -------------------------------------------------------------
# FIGURE 3: Sensor Installation & Metrology Cutaway
# -------------------------------------------------------------
def fig_03_sensor_cutaway():
    im, d = base_canvas(
        "SENSOR INSTALLATION METROLOGY: CORE IMMERSION vs. DEAD-LEG FRAUD",
        "Fluid boundary layer physics, thermowell tip location, and static pressure tap deburring",
        "FIG 03"
    )
    
    # Left Panel: Acceptable
    draw_card(d, (40, 120, 880, 1020), "ACCEPTABLE: CORE STREAM BULK IMMERSION", badge="VERIFIED COMPLIANCE", badge_color=GREEN)
    
    # Pipe drawing (Left)
    d.rectangle((100, 290, 820, 490), fill=(226, 232, 240), outline=NAVY, width=3)
    d.rectangle((100, 320, 820, 460), fill=(239, 246, 255)) # Liquid flow core
    
    # Parabolic flow velocity profile
    for idx in range(11):
        y_val = 330 + idx * 12
        vel_len = int(120 * math.sin((idx + 0.5) / 11 * math.pi))
        d.line((160, y_val, 160 + vel_len, y_val), fill=PIPE_COLD, width=2)
        d.polygon([(160 + vel_len, y_val), (150 + vel_len, y_val - 3), (150 + vel_len, y_val + 3)], fill=PIPE_COLD)
    d.text((120, 468), "Parabolic Velocity Profile (Core: V_max)", font=get_font(13, True), fill=PIPE_COLD)
    
    # Angled Thermowell 45 deg
    d.line((480, 225, 480, 290), fill=NAVY, width=12) # Weldolet
    # Probe into core
    d.line((480, 290, 555, 390), fill=(148, 163, 184), width=14)
    d.line((480, 290, 555, 390), fill=AMBER, width=6) # RTD element
    d.ellipse((545, 380, 565, 400), fill=RED) # Sensing tip
    d.text((575, 382), "Tip in Core Stream (1/3 - 1/2 D)", font=get_font(14, True), fill=RED)
    
    # Pressure Tap (Flush) - stem routed below text so zero overlap
    d.rectangle((310, 280, 326, 290), fill=NAVY)
    d.line((318, 230, 318, 280), fill=NAVY, width=3)
    d.text((220, 182), "Flush Deburred Tap", font=get_font(13, True), fill=NAVY)
    d.text((220, 202), "(Zero Burr / Zero Recess)", font=get_font(12), fill=TEXT_MUTED)
    
    # Bullet checklist (Left)
    d.rectangle((100, 540, 820, 980), fill=(240, 253, 244), outline=GREEN, width=2)
    d.text((120, 560), "METROLOGY EVIDENCE CRITERIA:", font=get_font(16, True), fill=GREEN)
    d.text((120, 600), "1. Sensor Tip Depth: Placed at 35% - 50% pipe inner diameter.", font=get_font(14, True), fill=NAVY)
    d.text((140, 625), "Guarantees measurement of bulk mixed temperature, not cold wall.", font=get_font(13), fill=TEXT_MUTED)
    d.text((120, 660), "2. Angle of Attack: 45° angled upstream into oncoming stream.", font=get_font(14, True), fill=NAVY)
    d.text((140, 685), "Increases convective heat transfer, minimizes flow stagnation wake.", font=get_font(13), fill=TEXT_MUTED)
    d.text((120, 720), "3. Thermal Compound: Thermowell packed with zinc oxide paste.", font=get_font(14, True), fill=NAVY)
    d.text((140, 745), "Thermal time constant tau < 2.5 seconds during power step transients.", font=get_font(13), fill=TEXT_MUTED)
    d.text((120, 780), "4. Pressure Tap Geometry: Piezometer ring or flush-ground orifice.", font=get_font(14, True), fill=NAVY)
    d.text((140, 805), "True static head without dynamic velocity error components.", font=get_font(13), fill=TEXT_MUTED)
    d.text((120, 850), "GATE VERDICT: APPROVED FOR PRECISION HEAT BALANCE", font=get_font(15, True), fill=GREEN)
    
    # Right Panel: Rejected
    draw_card(d, (920, 120, 1760, 1020), "REJECTED: DEAD-LEG CAVITY & TURBULENT RECESSED TAPS", badge="FALSE COMPLIANCE", badge_color=RED)
    
    # Pipe drawing (Right) shifted down to Y=290..490 so dead-leg tee stays cleanly below card header!
    d.rectangle((980, 290, 1700, 490), fill=(226, 232, 240), outline=NAVY, width=3)
    d.rectangle((980, 320, 1700, 460), fill=(239, 246, 255))
    
    # Dead leg vertical tee (starts at Y=195, well below card header at Y=154)
    d.rectangle((1320, 195, 1420, 290), fill=(226, 232, 240), outline=NAVY, width=3)
    d.rectangle((1335, 198, 1405, 320), fill=(254, 226, 226)) # Stagnant water pocket
    d.text((1435, 210), "DEAD-LEG TEE STUB (100mm)", font=get_font(14, True), fill=RED)
    d.text((1435, 235), "Stagnant uncirculated pocket", font=get_font(13), fill=TEXT_MUTED)
    
    # Sensor stranded in dead leg
    d.line((1370, 182, 1370, 255), fill=NAVY, width=10)
    d.ellipse((1360, 250, 1380, 270), fill=AMBER)
    d.text((1285, 162), "RTD Stranded in Dead Leg", font=get_font(13, True), fill=RED)
    
    # Turbulent throttle valve right upstream of pressure tap
    draw_valve(d, 1120, 390, size=24, color=NAVY, label="Throttling Valve")
    # Swirling eddies
    d.text((1165, 345), "Turbulent Eddies & Cavitation", font=get_font(12, True), fill=AMBER)
    # Bad pressure tap in turbulence
    d.line((1210, 290, 1210, 240), fill=RED, width=3)
    d.text((1115, 215), "Recessed Burred Tap", font=get_font(13, True), fill=RED)
    
    # Bullet checklist (Right)
    d.rectangle((980, 540, 1700, 980), fill=(254, 242, 242), outline=RED, width=2)
    d.text((1000, 560), "FALSE COMPLIANCE FAILURE MODES:", font=get_font(16, True), fill=RED)
    d.text((1000, 600), "1. Stagnant Cavity Lag: Liquid in tee pocket does not circulate.", font=get_font(14, True), fill=NAVY)
    d.text((1020, 625), "Temperature lags actual stream by 15-30 minutes; step changes invisible.", font=get_font(13), fill=TEXT_MUTED)
    d.text((1000, 660), "2. Pipe-Wall Thermal Conduction: Measures ambient chassis metal.", font=get_font(14, True), fill=NAVY)
    d.text((1020, 685), "On a hot afternoon reads high; on a winter morning reads false low.", font=get_font(13), fill=TEXT_MUTED)
    d.text((1000, 720), "3. Eddy-Zone Pressure Error: Located right behind a throttling gate.", font=get_font(14, True), fill=NAVY)
    d.text((1020, 745), "Bernoulli dynamic head converts to false static pressure swings.", font=get_font(13), fill=TEXT_MUTED)
    d.text((1000, 780), "4. Dry Thermowell: Air-filled well creates massive thermal barrier.", font=get_font(14, True), fill=NAVY)
    d.text((1020, 805), "Unit appears 'stable' only because the sensor cannot see the water.", font=get_font(13), fill=TEXT_MUTED)
    d.text((1000, 850), "GATE VERDICT: IMMEDIATE STOP & FAIL AT GATE 1", font=get_font(15, True), fill=RED)
    
    path = FIG / "fig-03-sensor-installation.png"
    im.save(path, "PNG")
    return path

# -------------------------------------------------------------
# FIGURE 4: 2N Electrical Distribution & Hardwired Safety Loop
# -------------------------------------------------------------
def fig_04_electrical():
    im, d = base_canvas(
        "2N ELECTRICAL DISTRIBUTION & HARDWIRED CLASS-1 SAFETY INTERLOCK",
        "A/B dual-feeder staging, ATS transfer behavior, and firmware-independent emergency trip",
        "FIG 04"
    )
    
    # 2 Subsections: Left = Power Distribution (2N); Right = Hardwired Safety Loop
    draw_card(d, (40, 120, 880, 1020), "2N DUAL-FEEDER POWER ARCHITECTURE", badge="POWER TRAIN", badge_color=PIPE_COLD)
    draw_card(d, (920, 120, 1760, 1020), "CLASS-1 HARDWIRED EMERGENCY TRIP LOOP", badge="FAIL-SAFE ARCHITECTURE", badge_color=RED)
    
    # Left: Dual Feeder Lines
    # Feeder A
    d.rectangle((80, 180, 420, 270), fill=(241, 245, 249), outline=NAVY, width=2)
    d.text((100, 195), "FEEDER A: 400V 3-Phase + PE", font=get_font(15, True), fill=PIPE_COLD)
    d.text((100, 222), "Source: UPS-A / PDU-A (100A)", font=get_font(13), fill=NAVY)
    d.text((100, 242), "Main Breaker: CB-101A (Lockable)", font=get_font(13), fill=TEXT_MUTED)
    
    # Feeder B
    d.rectangle((500, 180, 840, 270), fill=(241, 245, 249), outline=NAVY, width=2)
    d.text((520, 195), "FEEDER B: 400V 3-Phase + PE", font=get_font(15, True), fill=PIPE_COLD)
    d.text((520, 222), "Source: UPS-B / PDU-B (100A)", font=get_font(13), fill=NAVY)
    d.text((520, 242), "Main Breaker: CB-101B (Lockable)", font=get_font(13), fill=TEXT_MUTED)
    
    # Power Staging Logic
    d.rectangle((80, 320, 840, 480), fill=(255, 255, 255), outline=AMBER, width=2)
    d.text((100, 335), "SINGLE-FEED LOSS DROP TEST (Gate 3 Required):", font=get_font(16, True), fill=AMBER)
    d.text((100, 370), "• Normal 2N State: Feeder A carries Banks 1 & 2; Feeder B carries Banks 3 & 4.", font=get_font(14), fill=NAVY)
    d.text((100, 400), "• Loss of Feeder A Simulation: Trip CB-101A while operating at 100% Load.", font=get_font(14, True), fill=RED)
    d.text((100, 430), "• Expected Response: Banks 1 & 2 drop instantly; Feeder B does NOT trip on overcurrent.", font=get_font(13), fill=NAVY)
    d.text((100, 452), "• Control Bus (24VDC) stays alive via dual diode OR-gate without microsecond brownout.", font=get_font(13, True), fill=GREEN)
    
    # Contactors & Heating Elements
    for idx, name in enumerate(["Heater Bank 1 (30kW)", "Heater Bank 2 (30kW)", "Heater Bank 3 (30kW)", "Heater Bank 4 (30kW)"]):
        y_b = 520 + idx * 115
        d.rectangle((80, y_b, 840, y_b + 95), fill=(248, 250, 252), outline=NAVY, width=1)
        d.rectangle((100, y_b + 20, 220, y_b + 70), fill=(224, 231, 255), outline=NAVY, width=2)
        d.text((115, y_b + 35), f"Contactor K{idx+1}", font=get_font(13, True), fill=NAVY)
        d.line((220, y_b + 45, 340, y_b + 45), fill=NAVY, width=3)
        d.rectangle((340, y_b + 15, 620, y_b + 75), fill=(254, 242, 242), outline=RED, width=2)
        d.text((360, y_b + 32), name, font=get_font(14, True), fill=RED)
        d.text((360, y_b + 52), "Incoloy Immersion Elements", font=get_font(12), fill=TEXT_MUTED)
        d.text((650, y_b + 35), f"Feed {'A' if idx < 2 else 'B'}", font=get_font(14, True), fill=PIPE_COLD)
        
    # Right: Hardwired Safety Interlock Loop
    d.rectangle((960, 180, 1720, 310), fill=(254, 242, 242), outline=RED, width=2)
    d.text((980, 195), "HARDWIRED SAFETY PRINCIPLE (CLASS-1 FAIL-SAFE):", font=get_font(16, True), fill=RED)
    d.text((980, 230), "• ZERO dependence on PLC software, Modbus commands, or OS heartbeats.", font=get_font(14, True), fill=NAVY)
    d.text((980, 255), "• If any mechanical safety contact opens, the main contactor coil power is cut directly.", font=get_font(13), fill=NAVY)
    d.text((980, 280), "• Physical opening time: < 20 milliseconds. Contactors drop open by spring return.", font=get_font(13, True), fill=RED)
    
    # Schematic Series Loop
    d.text((980, 340), "24VDC EMERGENCY CONTACTOR COIL CIRCUIT (SERIES LOOP):", font=get_font(15, True), fill=NAVY)
    
    # Loop blocks in vertical series
    loop_items = [
        ("1. E-STOP PUSHBUTTON (ES-101)", "Red mushroom cap, latching twist-to-release on front door panel", RED),
        ("2. BIMETAL OVER-TEMP THERMOSTAT (TS-101)", "Mechanical snap disc welded directly to heater shell; trips at 85°C", RED),
        ("3. LOW-FLOW DIFFERENTIAL SWITCH (FS-101)", "Mechanical diaphragm contact; opens if flow drops below minimum 30 LPM", AMBER),
        ("4. CONTAINMENT LEAK RELAY (LR-101)", "Optical / conductive sensing rope in bottom pan detects spilled coolant", AMBER),
        ("5. CONTROL POWER WATCHDOG (WD-101)", "Hardware retriggerable timer; drops coil if PLC firmware halts", NAVY),
    ]
    
    for idx, (title, desc, col) in enumerate(loop_items):
        y_l = 380 + idx * 95
        d.rectangle((960, y_l, 1660, y_l + 75), fill=(255, 255, 255), outline=col, width=2)
        d.ellipse((980, y_l + 25, 1005, y_l + 50), fill=col)
        d.text((1020, y_l + 15), title, font=get_font(14, True), fill=col)
        d.text((1020, y_l + 42), desc, font=get_font(12), fill=TEXT_MUTED)
        # Series wire down
        if idx < 4:
            d.line((1310, y_l + 75, 1310, y_l + 95), fill=RED, width=4)
            
    # Coil at end of series loop (widened so green text fits with generous margin)
    d.rectangle((1040, 890, 1580, 980), fill=(241, 245, 249), outline=NAVY, width=3)
    d.text((1080, 908), "MAIN POWER CONTACTOR COILS (K1..K4)", font=get_font(15, True), fill=NAVY)
    d.text((1080, 935), "Spring-loaded force-guided contacts. De-energize to open.", font=get_font(13, True), fill=GREEN)
    d.line((1310, 855, 1310, 890), fill=RED, width=4)
    
    path = FIG / "fig-04-electrical-interlock-2n.png"
    im.save(path, "PNG")
    return path

# -------------------------------------------------------------
# FIGURE 5: Four-Quadrant Time Series Diagnostic Signatures
# -------------------------------------------------------------
def fig_05_timeseries():
    im, d = base_canvas(
        "FOUR-QUADRANT TIME-SERIES DIAGNOSTIC SIGNATURES",
        "Validating steady plateaus against stale data flatlines, thermal bypass, and water hammer",
        "FIG 05"
    )
    
    # 4 Quadrants
    # Q1: Top-Left (Valid Plateau)
    draw_card(d, (40, 120, 880, 560), "A. VALID THERMAL PLATEAU & STEADY DWELL", badge="ACCEPTED PROOF", badge_color=GREEN)
    # Q2: Top-Right (Stale Data)
    draw_card(d, (920, 120, 1760, 560), "B. STALE DATA CORRUPTION (FROZEN SENSOR)", badge="FRAUD DETECTED", badge_color=RED)
    # Q3: Bottom-Left (Bypass Leak)
    draw_card(d, (40, 580, 880, 1020), "C. INTERNAL BYPASS LEAK / SHORT-CIRCUIT", badge="DEFECTIVE COUPLING", badge_color=AMBER)
    # Q4: Bottom-Right (Water Hammer)
    draw_card(d, (920, 580, 1760, 1020), "D. WATER HAMMER & VALVE BOUNCE TRANSIENT", badge="HYDRAULIC SHOCK", badge_color=RED)
    
    # Helper to draw chart box inside card
    def chart_box(x0, y0, x1, y1):
        d.rectangle((x0, y0, x1, y1), fill=(255, 255, 255), outline=PANEL_BORDER, width=1)
        # Dotted grid lines
        for y_g in range(y0 + 40, y1, 50):
            d.line((x0, y_g, x1, y_g), fill=(241, 245, 249), width=1)
        for x_g in range(x0 + 80, x1, 100):
            d.line((x_g, y0, x_g, y1), fill=(241, 245, 249), width=1)
        # Axes
        d.line((x0, y1, x1, y1), fill=NAVY, width=2)
        d.line((x0, y0, x0, y1), fill=NAVY, width=2)
        d.text((x1 - 60, y1 + 8), "Time (min)", font=get_font(11), fill=TEXT_MUTED)
        
    # --- Q1: Valid Plateau ---
    chart_box(80, 190, 840, 480)
    # Curve 1: Power Step (30kW -> 60kW -> 120kW)
    pts_p = [(80, 420), (240, 420), (240, 340), (480, 340), (480, 240), (840, 240)]
    for i in range(len(pts_p)-1):
        d.line((pts_p[i], pts_p[i+1]), fill=NAVY, width=3)
    # Curve 2: Return Temp (Exponential lag curve)
    pts_t = []
    for x_i in range(80, 840, 5):
        if x_i < 240:
            y_i = 440
        elif x_i < 480:
            tau = (x_i - 240) / 40.0
            y_i = int(440 - (440 - 365) * (1 - math.exp(-tau)))
        else:
            tau = (x_i - 480) / 45.0
            y_i = int(365 - (365 - 265) * (1 - math.exp(-tau)))
        pts_t.append((x_i, y_i))
    d.line(pts_t, fill=PIPE_HOT, width=3)
    # Dwell annotation (widened box so text fits cleanly inside)
    d.rectangle((500, 285, 830, 330), fill=(240, 253, 244), outline=GREEN, width=2)
    d.text((512, 300), "Steady Dwell: ΔT=10.0K (Q_therm = P_elec ±3%)", font=get_font(11, True), fill=GREEN)
    d.text((80, 500), "Legend: [Dark: Commanded kW]  [Red: Return Temp RTD]  [Blue: Flow Meter]", font=get_font(12, True), fill=NAVY)
    d.text((80, 525), "Pass: Smooth thermal lag response, holds steady plateau for >= 15 min dwell.", font=get_font(12), fill=TEXT_MUTED)
    
    # --- Q2: Stale Data ---
    chart_box(960, 190, 1720, 480)
    # Command steps up
    d.line([(960, 420), (1160, 420), (1160, 240), (1720, 240)], fill=NAVY, width=3)
    # Stale line: perfect horizontal line with ZERO noise
    d.line([(960, 380), (1720, 380)], fill=RED, width=3)
    d.rectangle((1240, 340, 1680, 420), fill=(254, 242, 242), outline=RED, width=2)
    d.text((1260, 355), "FROZEN STALE DATA DETECTED!", font=get_font(13, True), fill=RED)
    d.text((1260, 375), "Mathematical variance sigma^2 = 0.0000", font=get_font(12), fill=NAVY)
    d.text((1260, 395), "Firmware repeating last good value!", font=get_font(12, True), fill=RED)
    d.text((960, 500), "Fraud Alert: Sensor disconnected or Modbus buffer locked.", font=get_font(12, True), fill=RED)
    d.text((960, 525), "Instant Gate 2 Fail: A reading without sensor micro-noise is a fabricated record.", font=get_font(12), fill=TEXT_MUTED)
    
    # --- Q3: Bypass Leak ---
    chart_box(80, 650, 840, 940)
    # 120kW commanded
    d.line([(80, 720), (300, 720), (300, 680), (840, 680)], fill=NAVY, width=3)
    # Delta-T barely rises!
    d.line([(80, 900), (300, 900), (450, 880), (840, 875)], fill=AMBER, width=3)
    d.rectangle((360, 760, 800, 840), fill=(254, 243, 199), outline=AMBER, width=2)
    d.text((380, 775), "HEAT STORY COLLAPSE: ΔT only 1.2K @ 120kW", font=get_font(13, True), fill=AMBER)
    d.text((380, 795), "Energy Balance: Inferred Heat = 14kW vs Electrical = 120kW", font=get_font(12), fill=NAVY)
    d.text((380, 815), "Cause: 85% of fluid short-circuiting through leaky bypass!", font=get_font(12, True), fill=RED)
    d.text((80, 960), "Defect: Fluid bypass valve left cracked open or internal baffle seal blown.", font=get_font(12, True), fill=AMBER)
    d.text((80, 985), "Gate 3 Stop: The contactors are hot, but the water never met the heat.", font=get_font(12), fill=TEXT_MUTED)
    
    # --- Q4: Water Hammer ---
    chart_box(960, 650, 1720, 940)
    # Pressure trace with violent spikes
    pts_wh = [(960, 840), (1150, 840)]
    # Valve slam at 1150
    pts_wh.extend([
        (1160, 670), (1175, 930), (1190, 710), (1205, 900),
        (1220, 760), (1240, 870), (1260, 810), (1300, 840), (1720, 840)
    ])
    d.line(pts_wh, fill=RED, width=3)
    d.line([(960, 720), (1720, 720)], fill=AMBER, width=2) # Pressure rating limit
    d.text((1400, 700), "Max Safe Working Pressure Limit (10 bar)", font=get_font(12, True), fill=AMBER)
    d.rectangle((1280, 860, 1680, 930), fill=(254, 242, 242), outline=RED, width=2)
    d.text((1300, 875), "SEVERE WATER HAMMER PEAK!", font=get_font(13, True), fill=RED)
    d.text((1300, 898), "Peak ΔP > 3.2x nominal operating head", font=get_font(12), fill=NAVY)
    d.text((960, 960), "Violent Transient: Fast solenoid closure without ramp damper destroys hose ferrules.", font=get_font(12, True), fill=RED)
    d.text((960, 985), "Gate 1/3 Stop: Modulating valves must have programmed minimum 3-second stroke ramp.", font=get_font(12), fill=TEXT_MUTED)
    
    path = FIG / "fig-05-timeseries-diagnostics.png"
    im.save(path, "PNG")
    return path

# -------------------------------------------------------------
# FIGURE 6: Sequential Acceptance Gate State Machine
# -------------------------------------------------------------
def fig_06_state_machine():
    im, d = base_canvas(
        "SEQUENTIAL PROTOTYPE ACCEPTANCE GATES & HARD WAIVER BARRIER",
        "Strict dependency state machine: zero hallway bypasses, fail-closed interlocks, and legal waiver protocols",
        "FIG 06"
    )
    
    # 4 Main Gate Columns
    gates = [
        ("GATE 1: STATIC & MECHANICAL", "• Danfoss FD83 lock pin check\n• Hose bend radius R >= 6D\n• 1.5x Hydrostatic hold\n• Zero weep at joints\n• Electrical drip-cup test\n• Module single-person pull", PIPE_COLD),
        ("GATE 2: POWER & TELEMETRY", "• Megger DC1000V >= 10MΩ\n• Dielectric AC1.5kV / 1 min\n• Stale-data sensor pull test\n• Loss-of-network fail-safe\n• E-Stop <20ms contact drop\n• Modbus register poll ok", PURPLE),
        ("GATE 3: STEPPED LOAD & DWELL", "• 25% / 50% / 75% / 100% Steps\n• >= 15 min Dwell per plateau\n• Thermal balance Q=m·Cp·ΔT\n• 2N Single-feed loss test\n• Sudden increase step test\n• Zero unexplained alarms", AMBER),
        ("GATE 4: OVERLOAD & CLOSE-OUT", "• 110%-120% Transient visit\n• Dwell strictly <= 10 min\n• Safe-off cool-down curve\n• Stranger file audit pass\n• Warranty log & limits sign\n• Final handover pack", GREEN)
    ]
    
    for idx, (title, checklist, col) in enumerate(gates):
        x0 = 50 + idx * 430
        x1 = x0 + 390
        d.rectangle((x0, 140, x1, 680), fill=(255, 255, 255), outline=col, width=3)
        d.rectangle((x0, 140, x1, 195), fill=col)
        d.text((x0 + 16, 155), title, font=get_font(16, True), fill=(255, 255, 255))
        
        # Checklist
        y_txt = 220
        for line in checklist.split("\n"):
            d.text((x0 + 20, y_txt), line, font=get_font(14, True if "•" in line else False), fill=NAVY)
            y_txt += 32
            
        # Status Box at bottom of card
        d.rectangle((x0 + 20, 580, x1 - 20, 650), fill=(248, 250, 252), outline=PANEL_BORDER, width=1)
        d.text((x0 + 35, 595), f"GATE {idx+1} PASS LINE:", font=get_font(13, True), fill=col)
        d.text((x0 + 35, 620), "Must be signed before next gate", font=get_font(12), fill=TEXT_MUTED)
        
        # Connecting forward arrows
        if idx < 3:
            x_arr = x1
            y_arr = 380
            d.line((x_arr, y_arr, x_arr + 40, y_arr), fill=GREEN, width=6)
            d.polygon([(x_arr + 40, y_arr), (x_arr + 25, y_arr - 8), (x_arr + 25, y_arr + 8)], fill=GREEN)
            
    # Bottom Zone: The Hallway Shortcut Prohibition vs Legal Waiver Path
    d.rectangle((50, 720, 1750, 1020), fill=(254, 242, 242), outline=RED, width=3)
    d.rectangle((50, 720, 1750, 765), fill=RED)
    d.text((70, 732), "THE HALLWAY SHORTCUT TRAP vs. THE LEGAL WAIVER PROTOCOL", font=get_font(18, True), fill=(255, 255, 255))
    
    # Left Box: Illegal Shortcut
    d.rectangle((80, 785, 870, 995), fill=(255, 255, 255), outline=RED, width=2)
    d.text((100, 805), "FORBIDDEN: THE 'LET'S DO THE HEAT RUN FIRST' FRAUD", font=get_font(15, True), fill=RED)
    d.text((100, 835), "• Trap: Contractor arrives with delivery truck waiting outside at 4:00 PM.", font=get_font(13), fill=NAVY)
    d.text((100, 860), "• Pressure: Hose leaks or Megger failed, but they ask to 'run heat anyway to save time'.", font=get_font(13), fill=NAVY)
    d.text((100, 885), "• Reality: Running 120kW on an unverified hose turns a punch list into a catastrophic fire/spill.", font=get_font(13, True), fill=RED)
    d.text((100, 915), "• HARD LAW: An open Gate 1 fail automatically physically blocks Gate 2 & 3.", font=get_font(13, True), fill=NAVY)
    d.text((100, 945), "• The recorder must write: 'Gate 3 not started due to open Gate 1 fail.'", font=get_font(13, True), fill=GREEN)
    
    # Right Box: Legal Waiver Protocol
    d.rectangle((910, 785, 1720, 995), fill=(255, 255, 255), outline=GREEN, width=2)
    d.text((930, 805), "LEGAL COMPLIANCE: THE FORMAL WAIVER PROTOCOL", font=get_font(15, True), fill=GREEN)
    d.text((930, 835), "• A waiver is NEVER an edit whispered in the hallway. It is a signed contract amendment.", font=get_font(13), fill=NAVY)
    d.text((930, 860), "• Required Action: If 120kW cannot be reached, the continuous rating MUST be derated to 60kW.", font=get_font(13, True), fill=NAVY)
    d.text((930, 885), "• Rule: You may drop the test evidence ONLY by formally reducing the product claim.", font=get_font(13, True), fill=GREEN)
    d.text((930, 915), "• Signatures: Sheet Owner + Scope Signer must sign the Limitations Log on the same day.", font=get_font(13), fill=NAVY)
    d.text((930, 945), "• Deliverable: The unit ships as 'Accepted with 60kW limitation', not a false pass.", font=get_font(13), fill=TEXT_MUTED)
    
    path = FIG / "fig-06-gate-statemachine.png"
    im.save(path, "PNG")
    return path

# -------------------------------------------------------------
# FIGURE 7: 120kW Reference Sandbox Calculation Model
# -------------------------------------------------------------
def fig_07_sandbox_model():
    im, d = base_canvas(
        "EDUCATIONAL REFERENCE SANDBOX: 120kW VIRTUAL RACK HEAT BALANCE",
        "Thermodynamic dimensioning, PG25 fluid physics, mass flow derivation, and dew point envelope",
        "FIG 07"
    )
    
    # 3 Main Pillars (shortened headers so zero badge collision)
    draw_card(d, (40, 120, 560, 1020), "1. BASELINE DESIGN INPUTS", badge="120 kW RACK MODEL", badge_color=PIPE_COLD)
    draw_card(d, (600, 120, 1200, 1020), "2. THERMODYNAMIC DERIVATION", badge="FIRST-PRINCIPLES MATH", badge_color=NAVY)
    draw_card(d, (1240, 120, 1760, 1020), "3. DEW POINT ENVELOPE", badge="SAFETY BOUNDARY", badge_color=AMBER)
    
    # Pillar 1: Baseline Inputs
    inputs = [
        ("Nominal Rack Thermal Load", "P_thermal = 120.0 kW", PIPE_COLD),
        ("Secondary Coolant Media", "25% Propylene Glycol (PG25)", NAVY),
        ("Coolant Density (@40°C)", "rho = 1025 kg/m³", NAVY),
        ("Specific Heat Capacity", "Cp = 3.980 kJ/(kg·K)", NAVY),
        ("Design Supply Temperature", "T_supply = 35.0 °C", PIPE_COLD),
        ("Design Return Temperature", "T_return = 45.0 °C", PIPE_HOT),
        ("Design Temperature Rise", "ΔT = 10.0 K (Nominal)", PIPE_HOT),
        ("Coupling Family", "Danfoss FD83-2051 (2\" Full Flow)", PIPE_COLD),
        ("Internal Pipe Size", "DN32 (1-1/4\" Sanitary 304)", NAVY),
    ]
    for idx, (lbl, val, col) in enumerate(inputs):
        y_p = 180 + idx * 85
        d.rectangle((60, y_p, 540, y_p + 70), fill=(248, 250, 252), outline=PANEL_BORDER, width=1)
        d.text((80, y_p + 12), lbl, font=get_font(13), fill=TEXT_MUTED)
        d.text((80, y_p + 35), val, font=get_font(15, True), fill=col)
        
    # Pillar 2: Derivations & Calculations
    # Box 1: Mass Flow
    d.rectangle((620, 180, 1180, 360), fill=(239, 246, 255), outline=PIPE_COLD, width=2)
    d.text((640, 195), "STEP 1: MASS & VOLUMETRIC FLOW RATE", font=get_font(15, True), fill=PIPE_COLD)
    d.text((640, 230), "• First Law Thermal Formula: P = m_dot · Cp · ΔT", font=get_font(14, True), fill=NAVY)
    d.text((640, 260), "  m_dot = 120 kW / (3.980 kJ/kg·K × 10.0 K) = 3.015 kg/s", font=get_font(14), fill=NAVY)
    d.text((640, 290), "• Volumetric Flow Conversion (Q_v):", font=get_font(14, True), fill=NAVY)
    d.text((640, 315), "  Q_v = (3.015 / 1025) × 60,000 = 176.5 L/min (46.6 GPM)", font=get_font(14, True), fill=PIPE_COLD)
    
    # Box 2: Pipe Velocity & Erosion
    d.rectangle((620, 390, 1180, 570), fill=(240, 253, 244), outline=GREEN, width=2)
    d.text((640, 405), "STEP 2: FLUID VELOCITY & EROSION CHECK", font=get_font(15, True), fill=GREEN)
    d.text((640, 440), "• DN32 Pipe Inner Diameter: d_i = 32.0 mm (Area = 8.04 cm²)", font=get_font(13), fill=NAVY)
    d.text((640, 470), "• Flow Velocity v = Q_v / Area = 2.45 m/s", font=get_font(15, True), fill=NAVY)
    d.text((640, 500), "• Engineering Rule of Thumb: v < 3.0 m/s for copper/stainless", font=get_font(13), fill=NAVY)
    d.text((640, 525), "  Pass: 2.45 m/s avoids acoustic noise & particulate erosion.", font=get_font(13, True), fill=GREEN)
    
    # Box 3: Hydraulic Drop Model
    d.rectangle((620, 600, 1180, 980), fill=(255, 255, 255), outline=NAVY, width=2)
    d.text((640, 615), "STEP 3: HYDRAULIC RESISTANCE DROP (ΔP)", font=get_font(15, True), fill=NAVY)
    d.text((640, 650), "• Quadratic Flow Law: ΔP = k_rack · (Q_v)²", font=get_font(14, True), fill=NAVY)
    d.text((640, 680), "• Target Resistance @ 176.5 LPM: ΔP_nom = 115 kPa (1.15 bar)", font=get_font(13, True), fill=PIPE_COLD)
    d.text((640, 715), "• Acceptance Tolerance Band: ± 10% (103.5 kPa - 126.5 kPa)", font=get_font(13), fill=TEXT_MUTED)
    d.text((640, 755), "DIAGNOSTIC TEST CASE: Thermal Mystery Discovered", font=get_font(14, True), fill=RED)
    d.text((640, 785), "• Field Reading: Electrical=120kW, Flow=176.5LPM, but ΔT=6.0K!", font=get_font(13), fill=NAVY)
    d.text((640, 810), "• Deduction: Q_therm = 3.015 × 3.98 × 6.0 = 72.0 kW (-48 kW!)", font=get_font(13, True), fill=RED)
    d.text((640, 840), "• Investigation tree: 1) Leaking bypass valve? 2) Failed elements?", font=get_font(13), fill=NAVY)
    d.text((640, 865), "  3) False sensor calibration? 4) Unmeasured air heat radiation?", font=get_font(13), fill=NAVY)
    d.text((640, 900), "VERDICT: NEVER adjust calibration constants to force agreement!", font=get_font(12, True), fill=RED)
    
    # Pillar 3: Dew Point Safety Envelope
    d.rectangle((1260, 180, 1740, 480), fill=(254, 243, 199), outline=AMBER, width=2)
    d.text((1280, 195), "DEW POINT (TDp) SAFETY ENVELOPE", font=get_font(16, True), fill=AMBER)
    d.text((1280, 235), "Data Hall Conditions:", font=get_font(14, True), fill=NAVY)
    d.text((1280, 260), "• Air Temp T_air = 28.0 °C", font=get_font(13), fill=NAVY)
    d.text((1280, 285), "• Relative Humidity RH = 65%", font=get_font(13), fill=NAVY)
    d.text((1280, 310), "• Calculated Dew Point: TDp = 20.8 °C", font=get_font(14, True), fill=RED)
    d.text((1280, 350), "Required Supply Safety Margin:", font=get_font(14, True), fill=NAVY)
    d.text((1280, 375), "• T_supply_min = TDp + 2.0 K = 22.8 °C", font=get_font(15, True), fill=PIPE_COLD)
    d.text((1280, 410), "Condensation Hazard Zone:", font=get_font(13, True), fill=RED)
    d.text((1280, 435), "If T_supply < 20.8°C -> Droplets form on hoses!", font=get_font(13, True), fill=RED)
    
    # Checklist for Acceptance Sheet
    d.rectangle((1260, 520, 1740, 980), fill=(241, 245, 249), outline=NAVY, width=2)
    d.text((1280, 540), "ACCEPTANCE SHEET PRE-FILL CELLS:", font=get_font(15, True), fill=NAVY)
    d.text((1280, 575), "• Cell 01: Rated Power = 120.0 kW (Cite)", font=get_font(13), fill=NAVY)
    d.text((1280, 605), "• Cell 02: Design Flow = 176.5 LPM ±5%", font=get_font(13), fill=NAVY)
    d.text((1280, 635), "• Cell 03: Design ΔT = 10.0 K (35°C -> 45°C)", font=get_font(13), fill=NAVY)
    d.text((1280, 665), "• Cell 04: Max ΔP = 115 kPa @ rated flow", font=get_font(13), fill=NAVY)
    d.text((1280, 695), "• Cell 05: TDp Safety Shutoff = TDp + 2.0K", font=get_font(13, True), fill=RED)
    d.text((1280, 725), "• Cell 06: Coupling = Danfoss FD83-2051", font=get_font(13, True), fill=PIPE_COLD)
    d.text((1280, 755), "• Cell 07: Megger = DC1000V >= 10MΩ", font=get_font(13), fill=NAVY)
    d.text((1280, 785), "• Cell 08: Air Load Split = 15kW CRAH", font=get_font(13), fill=PIPE_HOT)
    d.text((1280, 830), "CONCLUSION: A calculated sandbox gives the", font=get_font(14, True), fill=NAVY)
    d.text((1280, 855), "reader exact numerical yardsticks without", font=get_font(14, True), fill=NAVY)
    d.text((1280, 880), "compromising vendor non-disclosure.", font=get_font(14, True), fill=NAVY)
    
    path = FIG / "fig-07-sandbox-calculation-model.png"
    im.save(path, "PNG")
    return path

if __name__ == "__main__":
    print("Generating Engineering Diagrams...")
    p1 = fig_01_boundary()
    print("Generated:", p1)
    p2 = fig_02_pid()
    print("Generated:", p2)
    p3 = fig_03_sensor_cutaway()
    print("Generated:", p3)
    p4 = fig_04_electrical()
    print("Generated:", p4)
    p5 = fig_05_timeseries()
    print("Generated:", p5)
    p6 = fig_06_state_machine()
    print("Generated:", p6)
    p7 = fig_07_sandbox_model()
    print("Generated:", p7)
    print("All 7 Engineering Diagrams generated successfully!")
