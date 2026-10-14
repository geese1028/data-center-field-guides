#!/usr/bin/env python3
"""
Generate Flagship Engineering Diagrams for Book 06: When a Monitor May Speak
Author: Tristan (Data Center Field Guides)
Resolution: 1800 x 1100, publication-grade vector styling.
Palette: Deep slate blue / telemetry cyan / alert amber / crimson / emerald green.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = Path("/Users/geese/Downloads/book/books/06-when-a-monitor-may-speak/figures")
FONT_DIR = Path("/Users/geese/Downloads/book/books/01-liquid-load-bank/fonts")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Theme Palette (Mission-Critical Telemetry & Alarms)
BG = (15, 23, 42)          # Deep slate blue
PANEL = (30, 41, 59)       # Medium slate
GRID = (51, 65, 85)        # Slate grid lines
TEXT = (248, 250, 252)     # Bright white
MUTED = (148, 163, 184)    # Cool grey
CYAN = (6, 182, 212)       # Telemetry / Sensor digital stream
AMBER = (245, 158, 11)     # Warning / Dwell / Deadband
RED = (239, 68, 68)        # Alarm / High-High / Trip
GREEN = (34, 197, 94)      # Normal / Quality Good / SLA Met
BLUE = (59, 130, 246)      # Data bus / PTP clock / Engineering


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
    for y in range(0, h, 50):
        d.line((0, y, w, y), fill=GRID, width=1)
    d.rectangle((20, 20, w - 21, h - 21), outline=CYAN, width=2)
    return im, d


def draw_header(d, num, title, subtitle):
    d.rectangle((40, 35, 1760, 115), fill=PANEL, outline=CYAN, width=2)
    d.text((60, 48), f"FIGURE 06.{num} :: {title.upper()}", font=get_font(24, True), fill=CYAN)
    d.text((60, 82), subtitle, font=get_font(16), fill=MUTED)
    d.text((1500, 58), "BOOK 06 // TELEMETRY", font=get_font(16, True), fill=AMBER)


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
# FIG 1: Point Anatomy & Quality Bitmask
# -------------------------------------------------------------
def fig_01():
    im, d = new_canvas()
    draw_header(d, 1, "Anatomy of an Operational Point & Quality Bitmask",
                "A point is not a number on a screen. A point is a value, synchronized timestamp, origin path, and quality mark.")

    # 4 Core Pillars of a Point
    pillars = [
        ("1. MEASURED VALUE", "Float64 / Boolean / Discrete Enum", "• Engineering units strictly enforced (°C, kPa, LPM, A)\n• Single scale factor applied once at collector\n• Raw electrical voltage/counts preserved in store\n• No pre-smoothing that masks hydraulic transients", CYAN),
        ("2. SYNCHRONIZED CLOCK", "UTC Timestamp with Nanosecond / ms", "• Sourced from NTP / PTP Stratum-1 time server\n• Maximum allowable drift: <= 5.0 ms across DC\n• Sequence-of-Events (SOE) timestamped at source\n• Arrival timestamp separated from origin timestamp", BLUE),
        ("3. HARDWARE SOURCE PATH", "Immutable Physical Topology URI", "• Complete bus address: modbus://cdu-04/reg-40102\n• Physical rack, cabinet, and pin allocation\n• Human tag mapped via strict 3-column dictionary\n• Survives UI platform migrations without renaming", AMBER),
        ("4. QUALITY BITMASK", "Status Flag Byte (Mandatory Gate)", "• 0x00 = GOOD (Value verified and fresh)\n• 0x01 = STALE (Failed polling window; t > 3*T_poll)\n• 0x02 = UNCERTAIN (Sensor out of calibration)\n• 0x04 = BAD / FAULT (Wire break / short / timeout)", GREEN),
    ]

    for i, (title, sub, body, col) in enumerate(pillars):
        x = 60 + i * 425
        y = 150
        d.rectangle((x, y, x + 400, y + 420), fill=PANEL, outline=col, width=2)
        d.rectangle((x, y, x + 400, y + 50), fill=(20, 28, 45), outline=col, width=1)
        d.text((x + 15, y + 12), title, font=get_font(18, True), fill=col)
        d.text((x + 15, y + 60), sub, font=get_font(13, True), fill=MUTED)
        d.line((x + 15, y + 85, x + 385, y + 85), fill=GRID, width=1)

        lines = body.split("\n")
        yy = y + 105
        for l in lines:
            d.text((x + 15, yy), l, font=get_font(13), fill=TEXT)
            yy += 32

    # Bottom Architectural Box: The Quality Gating Rule
    d.rectangle((60, 610, 1740, 1040), fill=(24, 32, 47), outline=CYAN, width=2)
    d.text((90, 635), "THE CARDINAL QUALITY LAW: SILENCE OVER HALLUCINATION", font=get_font(20, True), fill=CYAN)

    rules = [
        ("RULE 1: NO SILENT INTERPOLATION", "When a sensor communication fails, a monitor must NEVER hold the last known good value forward indefinitely. A flat line is a lie. After 3 missed polling intervals (t > 3 * T_poll), the point's quality flips to STALE (0x01) and display turns GREY.", AMBER),
        ("RULE 2: QUALITY-GATED ALARMING", "An alert may ONLY be triggered if Quality == GOOD (0x00). If quality is STALE, BAD, or UNCERTAIN, the system raises a 'Telemetry Loss Defect', NOT a temperature or pressure alarm. Never wake an on-call engineer for an imaginary plant trip caused by a severed RS-485 wire.", RED),
        ("RULE 3: CALCULATED POINTS ARE NOT SENSORS", "Room averages, delta-Ts, and health scores are mathematical calculations. A calculated point must explicitly declare its constituent inputs. If any single input point has Quality != GOOD, the calculated point immediately forfeits its quality mark.", BLUE),
        ("RULE 4: RAW LOG PRESERVATION", "Database storage must preserve the raw telemetry telegrams alongside transformed values. Conversion, scaling, and calibration offsets must be versioned and auditable. Overwriting raw sensor data to make reports look clean is an operational fraud.", GREEN),
    ]

    for j, (rt, rb, rc) in enumerate(rules):
        bx = 90 + (j % 2) * 820
        by = 685 + (j // 2) * 165
        d.rectangle((bx, by, bx + 780, by + 145), fill=PANEL, outline=rc, width=1)
        d.text((bx + 20, by + 15), rt, font=get_font(15, True), fill=rc)
        # wrap text
        words = rb.split()
        cur, l_list = "", []
        for w in words:
            if d.textlength(cur + " " + w, font=get_font(13)) <= 740:
                cur += (" " if cur else "") + w
            else:
                l_list.append(cur)
                cur = w
        if cur:
            l_list.append(cur)
        for k, line in enumerate(l_list):
            d.text((bx + 20, by + 45 + k * 22), line, font=get_font(13), fill=TEXT)

    im.save(OUT_DIR / "fig-01-point-anatomy-and-quality-flag.png", "PNG")
    print("Saved: fig-01-point-anatomy-and-quality-flag.png")


# -------------------------------------------------------------
# FIG 2: Thresholds, Deadband, Dwell, Anti-Flap
# -------------------------------------------------------------
def fig_02():
    im, d = new_canvas()
    draw_header(d, 2, "Thresholding Dynamics: Deadband Hysteresis and Dwell Filtering",
                "How to prevent alarm chatter. Raw analog noise must be filtered by deadbands, dwell delays, and flap suppression.")

    # Left: The Analog Waveform & Threshold Hierarchy (0 to 1100, x: 60 to 980)
    d.rectangle((60, 150, 1020, 1040), fill=PANEL, outline=CYAN, width=2)
    d.text((90, 175), "ANALOG WAVEFORM & HYSTERESIS DEADBAND GEOMETRY", font=get_font(18, True), fill=CYAN)

    gx, gy, gw, gh = 100, 230, 880, 520
    d.rectangle((gx, gy, gx + gw, gy + gh), fill=(15, 23, 42), outline=GRID, width=1)

    # Grid & Threshold lines
    # HH Trip: 40°C -> y = 290
    # H Warning: 32°C -> y = 390
    # Deadband return: 30°C -> y = 430
    # Normal: 25°C -> y = 550
    # L Warning: 18°C -> y = 670

    d.line((gx, 290, gx + gw, 290), fill=RED, width=2)
    d.text((gx + 15, 265), "HIGH-HIGH (HH) TRIP THRESHOLD: 40.0°C (EOP Action / Chiller Stage)", font=get_font(13, True), fill=RED)

    d.line((gx, 390, gx + gw, 390), fill=AMBER, width=2)
    d.text((gx + 15, 365), "HIGH (H) ALARM THRESHOLD: 32.0°C (SLA Warning)", font=get_font(13, True), fill=AMBER)

    # Deadband band
    d.rectangle((gx, 390, gx + gw, 430), fill=(245, 158, 11, 40), outline=None)
    d.line((gx, 430, gx + gw, 430), fill=MUTED, width=1)
    d.text((gx + 15, 435), "DEADBAND (HYSTERESIS) RESET LINE: 30.0°C (Delta = 2.0 K)", font=get_font(12, True), fill=MUTED)

    d.line((gx, 550, gx + gw, 550), fill=GREEN, width=1)
    d.text((gx + 15, 525), "NOMINAL OPERATING SETPOINT: 25.0°C", font=get_font(13, True), fill=GREEN)

    d.line((gx, 670, gx + gw, 670), fill=BLUE, width=2)
    d.text((gx + 15, 645), "LOW (L) ALARM THRESHOLD: 18.0°C (Condensation Risk)", font=get_font(13, True), fill=BLUE)

    # Simulated curve with noisy transient and sustained excursion
    points = [
        (100, 550), (160, 545), (220, 560), (280, 530), (340, 510),
        # Noise spike crossing High Alarm briefly (t < dwell)
        (380, 420), (410, 370), (430, 360), (450, 395), (480, 470),
        # Normal return
        (520, 540), (560, 530),
        # Sustained Excursion crossing H and dwelling
        (600, 440), (640, 380), (680, 350), (720, 340), (760, 345), (800, 350),
        # Drop back into deadband (31°C) -> Alarm MUST NOT CLEAR yet!
        (840, 410), (880, 420),
        # Finally crosses below 30°C reset line
        (920, 450), (960, 520)
    ]
    for k in range(len(points) - 1):
        d.line((points[k], points[k+1]), fill=CYAN, width=3)

    # Callout 1: Noise Spike Suppressed by Dwell
    d.rectangle((370, 320, 500, 355), fill=PANEL, outline=AMBER, width=1)
    d.text((375, 325), "Transient Noise (t < 5s)\nNO ALARM FIRED", font=get_font(11, True), fill=AMBER)

    # Callout 2: Sustained Dwell -> Alarm Fires
    d.rectangle((670, 270, 810, 330), fill=PANEL, outline=RED, width=1)
    d.text((675, 275), "Dwell t >= 10.0s\nALARM FIRED AT T_0+10s", font=get_font(11, True), fill=RED)

    # Callout 3: In Deadband -> Alarm Stays Latched
    d.rectangle((820, 450, 960, 505), fill=PANEL, outline=MUTED, width=1)
    d.text((825, 455), "In Deadband (31°C)\nALARM STAYS LATCHED", font=get_font(11, True), fill=MUTED)

    # Explanatory Notes under graph
    d.text((90, 780), "THE MATHEMATICS OF DEADBAND & DWELL", font=get_font(16, True), fill=CYAN)
    d.text((90, 815), "1. Dwell Window (t_dwell): Alarm fires ONLY if T(t) > T_high for continuous interval Delta_t >= t_dwell.", font=get_font(13), fill=TEXT)
    d.text((90, 845), "2. Hysteresis (Delta_H): Once in alarm, state clears ONLY when T(t) <= T_high - Delta_H (e.g. 32°C - 2K = 30°C).", font=get_font(13), fill=TEXT)
    d.text((90, 875), "3. Chattering Elimination: Without deadband, a sensor wavering at 32.01°C / 31.99°C generates 200 alarms per hour.", font=get_font(13), fill=TEXT)

    # Right: Anti-Flap Suppression Engine (x: 1060 to 1740)
    d.rectangle((1060, 150, 1740, 1040), fill=PANEL, outline=AMBER, width=2)
    d.text((1090, 175), "ANTI-FLAP QUARANTINE ENGINE", font=get_font(18, True), fill=AMBER)

    flap_steps = [
        ("STAGE 1: FLAP DETECTION", "Monitoring engine tracks state transitions (Normal <-> Alarm) over a rolling 10-minute window.\n• Flap Limit (N_flap): 4 toggles in 10 minutes.\n• Typical cause: Loose RTD terminal, faulty relay contact, or hunting bypass valve actuator.", CYAN),
        ("STAGE 2: AUTOMATIC QUARANTINE", "When N_toggles >= 4, point enters 'FLAPPING_LATCH' state.\n• Audible bells and operator popups are MUTED.\n• Paging and SMS escalation queues are BLOCKED.\n• Telemetry stream remains recorded to disk.\n• Single notification sent: 'Point CDU-04-T_sup quarantined for flap'.", AMBER),
        ("STAGE 3: ROOT-CAUSE INVESTIGATION", "Quarantine prevents operator alarm fatigue while protecting the console.\n• Technician assigned to physically inspect wire terminations.\n• Calibrated oscilloscope or loop calibrator connected.\n• Digital filter damping constant adjusted if necessary.", BLUE),
        ("STAGE 4: CONTROLLED RESTORATION", "Point remains in quarantine until:\n1. Sensor exhibits continuous stable behavior for >= 30 minutes.\n2. Duty Manager executes manual unlatch command.\n3. Automatic self-clearing after 60 min if zero transitions occur.", GREEN),
    ]

    fy = 220
    for st, sd, sc in flap_steps:
        d.rectangle((1090, fy, 1710, fy + 180), fill=(20, 28, 45), outline=sc, width=1)
        d.text((1110, fy + 15), st, font=get_font(16, True), fill=sc)
        lines = sd.split("\n")
        ly = fy + 45
        for l in lines:
            wrapped = wrap_text(d, l, get_font(13), 580)
            for wl in wrapped:
                d.text((1110, ly), wl, font=get_font(13), fill=TEXT)
                ly += 22
        fy += 195

    im.save(OUT_DIR / "fig-02-threshold-deadband-and-dwell-filter.png", "PNG")
    print("Saved: fig-02-threshold-deadband-and-dwell-filter.png")


# -------------------------------------------------------------
# FIG 3: Alert to Incident Escalation Gate
# -------------------------------------------------------------
def fig_03():
    im, d = new_canvas()
    draw_header(d, 3, "The Human Escalation Gate: An Alert is Not an Incident",
                "A software alert is an internal database record. An incident is a contractual business event requiring executive command.")

    # 3-Zone Flow: Left: Raw Alarms -> Middle: The Human Gate -> Right: Incident Management
    # Zone 1: Raw Telemetry Alarms
    d.rectangle((60, 150, 520, 1040), fill=PANEL, outline=CYAN, width=2)
    d.text((80, 175), "ZONE 1: SOFTWARE ALERTS", font=get_font(18, True), fill=CYAN)
    d.text((80, 205), "Automated, high-volume telemetry events", font=get_font(13), fill=MUTED)

    alert_cards = [
        ("BMS-ALM-1029", "CDU Pump 2 Low DP Warning", "DP = 0.85 bar (Thresh: 0.90 bar)\nQuality: GOOD | Dwell: 12s\nSeverity: Warning (Level 3)", AMBER),
        ("EPMS-ALM-4011", "UPS-01 Battery String Float Low", "V_float = 535 VDC (Thresh: 540)\nQuality: GOOD | Dwell: 60s\nSeverity: Warning (Level 3)", BLUE),
        ("BMS-ALM-8820", "Cold Aisle Pod 3 High Temp", "T = 27.8°C (Thresh: 27.0°C)\nQuality: GOOD | Dwell: 30s\nSeverity: Major (Level 2)", RED),
        ("FIRE-ALM-0012", "VESDA Pod 4 Alert Stage 1", "Smoke = 0.08% /m (Thresh: 0.06)\nQuality: GOOD | Latched\nSeverity: Critical (Level 1)", RED),
    ]

    ay = 245
    for tag, title, body, col in alert_cards:
        d.rectangle((80, ay, 500, ay + 175), fill=(20, 28, 45), outline=col, width=1)
        d.text((95, ay + 12), tag, font=get_font(14, True), fill=col)
        d.text((95, ay + 38), title, font=get_font(14, True), fill=TEXT)
        lines = body.split("\n")
        byy = ay + 68
        for l in lines:
            d.text((95, byy), l, font=get_font(12), fill=MUTED)
            byy += 22
        ay += 195

    # Center: The Gating Filter & Decision Tree
    d.rectangle((560, 150, 1240, 1040), fill=(24, 32, 47), outline=AMBER, width=2)
    d.text((580, 175), "ZONE 2: THE HUMAN ESCALATION GATE", font=get_font(18, True), fill=AMBER)
    d.text((580, 205), "The screen does not hold a pen. Only a human decides.", font=get_font(13), fill=MUTED)

    # 3 Mandatory Promotion Tests
    tests = [
        ("GATE TEST 1: CONTRACTUAL SLA IMPACT?", "Did the excursion breach an SLA threshold (power loss to IT, secondary fluid temp > 32°C for > 5 min, rack intake air > 27°C)?\n• NO: Stays an internal Facility Maintenance Ticket.\n• YES: Mandatory promotion to P1/P2 Incident.", RED),
        ("GATE TEST 2: HUMAN LIFE SAFETY THREAT?", "Does the condition threaten human life (electrical arc-flash, toxic refrigerant leak, VESDA smoke confirmation, structural collapse)?\n• NO: Proceed to Gate Test 3.\n• YES: Immediate Emergency EOP execution & P1 Incident.", RED),
        ("GATE TEST 3: REDUNDANCY COLLAPSE (N-1)?", "Did the event eliminate surviving plant redundancy (e.g. 2N feeder A lost, surviving on B; or primary chiller trip, running N+0)?\n• NO: Resolved via routine shift work order.\n• YES: Mandatory promotion to P2 Major Incident.", AMBER),
    ]

    ty = 245
    for tt, tb, tc in tests:
        d.rectangle((580, ty, 1220, ty + 160), fill=PANEL, outline=tc, width=1)
        d.text((600, ty + 15), tt, font=get_font(15, True), fill=tc)
        lines = tb.split("\n")
        lyy = ty + 45
        for l in lines:
            d.text((600, lyy), l, font=get_font(13), fill=TEXT)
            lyy += 24
        ty += 180

    # Gate Decision Box
    d.rectangle((580, 800, 1220, 1010), fill=(20, 28, 45), outline=CYAN, width=2)
    d.text((600, 820), "WHO HOLDS THE AUTHORITY TO PROMOTE?", font=get_font(16, True), fill=CYAN)
    d.text((600, 855), "• Permitted: Licensed Duty Manager or formally designated ECC Lead.", font=get_font(13, True), fill=GREEN)
    d.text((600, 885), "• Prohibited: Monitoring software AI, vendor bots, junior interns, group chats.", font=get_font(13, True), fill=RED)
    d.text((600, 915), "• Accountability: The person who promotes signs their name and starts the SLA clock.", font=get_font(13), fill=TEXT)
    d.text((600, 945), "• Demotion: Demoting an active incident requires formal RCA evidence, not optimism.", font=get_font(13), fill=TEXT)

    # Zone 3: Formal Incident Management
    d.rectangle((1280, 150, 1740, 1040), fill=PANEL, outline=RED, width=2)
    d.text((1300, 175), "ZONE 3: PRODUCTION INCIDENT", font=get_font(18, True), fill=RED)
    d.text((1300, 205), "Formal business and legal response", font=get_font(13), fill=MUTED)

    inc_boxes = [
        ("1. INCIDENT BRIDGE OPENED", "• Technical Commander assigned\n• Dedicated voice conference active\n• Scribe records timeline microsecond-by-microsecond", BLUE),
        ("2. 15-MINUTE CLIENT NOTICE", "• Contractual SLA clock running\n• Facts only: Timestamp, hall, symptoms\n• Hypotheses strictly forbidden", RED),
        ("3. EOP SAFE-STATE RESTORATION", "• Muscle-memory emergency execution\n• Plant brought to nearest stable mode\n• Hands off controls; no heroics", GREEN),
        ("4. POST-INCIDENT RCA", "• 5-Whys and Fishbone forensic review\n• Exactly 1 owned operational change\n• Defect tracked on handover sheet", AMBER),
    ]

    iy = 245
    for it, ib, ic in inc_boxes:
        d.rectangle((1300, iy, 1720, iy + 175), fill=(20, 28, 45), outline=ic, width=1)
        d.text((1315, iy + 15), it, font=get_font(14, True), fill=ic)
        lines = ib.split("\n")
        iyy = iy + 50
        for l in lines:
            d.text((1315, iyy), l, font=get_font(13), fill=TEXT)
            iyy += 24
        iy += 195

    # Connecting Arrows
    d.line((500, 520, 560, 520), fill=CYAN, width=3)
    d.line((1220, 520, 1280, 520), fill=RED, width=3)

    im.save(OUT_DIR / "fig-03-alert-to-incident-escalation-gate.png", "PNG")
    print("Saved: fig-03-alert-to-incident-escalation-gate.png")


# -------------------------------------------------------------
# FIG 4: Alarm Storm Suppression & Topological Root-Cause
# -------------------------------------------------------------
def fig_04():
    im, d = new_canvas()
    draw_header(d, 4, "Topology-Aware Ingestion: Alarm Storm Suppression",
                "How a single upstream utility trip spawns 500 downstream cascade alarms, and how dependency masking squashes the storm.")

    # Top Box: The Single Physical Trigger
    d.rectangle((60, 150, 1740, 290), fill=PANEL, outline=RED, width=2)
    d.text((90, 175), "UPSTREAM ROOT EVENT: 35kV UTILITY FEEDER A BREAKER TRIP (TIME: T_0)", font=get_font(20, True), fill=RED)
    d.text((90, 215), "Primary 35kV utility incoming breaker trips due to off-site grid fault. Bus A de-energizes instantly. Transients propagate through all downstream plant.", font=get_font(14), fill=TEXT)
    d.text((90, 245), "Without topological suppression, the BMS/EPMS console receives 548 individual alarms within 6.2 seconds.", font=get_font(14, True), fill=AMBER)

    # Middle Left: The Raw Alarm Storm (Unsuppressed Chaos)
    d.rectangle((60, 320, 880, 1040), fill=(25, 20, 25), outline=RED, width=2)
    d.text((80, 345), "UNFILTERED CONSOLE (ALARM STORM - 548 ALARMS)", font=get_font(18, True), fill=RED)
    d.text((80, 375), "Operator blinded by screaming alarms; critical root cause buried on page 14.", font=get_font(13), fill=MUTED)

    storm_items = [
        ("T+0.015s", "SWG-01-M1 Overcurrent Trip Relay Actuated", RED),
        ("T+0.080s", "480V Substation Main Bus A Under-Voltage Alarm", RED),
        ("T+0.120s", "UPS-01 Static Bypass Input Frequency Out of Spec", AMBER),
        ("T+0.125s", "UPS-02 Static Bypass Input Frequency Out of Spec", AMBER),
        ("T+0.250s", "UPS-01 / 02 Transfer to Battery Power (120 strings)", RED),
        ("T+0.400s", "Chiller CH-01 Compressor VFD Bus Under-Voltage Trip", RED),
        ("T+0.410s", "Chiller CH-02 Compressor VFD Bus Under-Voltage Trip", RED),
        ("T+0.850s", "Primary Chilled Water Pumps P-01 / P-02 Stop Flow", RED),
        ("T+1.200s", "CRAH Units 1-16 Fan VFD Under-Voltage Alarms (16x)", AMBER),
        ("T+2.500s", "Rack PDU A-Feeds (480 racks) Report Input Power Lost", RED),
        ("T+3.800s", "Secondary CDU Supply Temperature High Warning (4x)", AMBER),
        ("T+5.500s", "Diesel Generators GEN-01 / 02 Auto-Start Signal Sent", GREEN),
    ]

    sy = 415
    for ts, msg, col in storm_items:
        d.rectangle((80, sy, 860, sy + 42), fill=PANEL, outline=col, width=1)
        d.text((95, sy + 11), ts, font=get_font(13, True), fill=CYAN)
        d.text((210, sy + 11), msg, font=get_font(13), fill=col)
        sy += 50

    # Middle Right: Topological Parent-Child Masking Engine
    d.rectangle((920, 320, 1740, 1040), fill=(20, 30, 45), outline=GREEN, width=2)
    d.text((940, 345), "TOPOLOGICAL INGESTION ENGINE (1 INCIDENT + ROOT CAUSE)", font=get_font(18, True), fill=GREEN)
    d.text((940, 375), "Parent-child dependency tree quenches downstream symptom alarms automatically.", font=get_font(13), fill=MUTED)

    d.rectangle((940, 415, 1720, 570), fill=PANEL, outline=CYAN, width=2)
    d.text((965, 435), "CONSOLIDATED P1 INCIDENT DISPLAY (CONSOLE PRESENTATION)", font=get_font(16, True), fill=CYAN)
    d.text((965, 470), "INCIDENT #2026-10-14-001 :: LOSS OF 35kV UTILITY FEEDER A", font=get_font(15, True), fill=RED)
    d.text((965, 500), "• Root Cause Point: SWG-35kV-M1 Status = OPEN | Time: 09:14:22.015 UTC", font=get_font(13, True), fill=TEXT)
    d.text((965, 530), "• Surviving State: Bus B Carrying 100% Load (82% of capacity) | IT Whitespace Stable", font=get_font(13, True), fill=GREEN)

    # Dependency Tree Diagram
    d.rectangle((940, 600, 1720, 1010), fill=(15, 23, 42), outline=GRID, width=1)
    d.text((965, 620), "AUTOMATIC SUPPRESSION RULES INGESTED:", font=get_font(15, True), fill=AMBER)

    suppress_rules = [
        ("RULE 1: BREAKER-DRIVEN QUENCHING", "If Main Bus Incomer trips, automatically MUTE and collapse all downstream under-voltage alarms from downstream distribution panels, UPS rectifiers, and motor control centers (MCCs)."),
        ("RULE 2: PUMP TRIP MUTES FLOW ALARMS", "If Secondary CDU Pump P-01 status == STOPPED due to an electrical trip, suppress the downstream 'Low Loop Flow Rate' alarm for that unit. Do not report flow loss as a mysterious piping defect when the pump motor is unpowered."),
        ("RULE 3: TIME-ALIGNED ROOT CORRELATION", "Events occurring within a 500 ms window along an electrical branch are correlated to the uppermost topological breaker. The top breaker gets the alarm; the children become 'Correlated Symptoms' on the incident ticket."),
        ("RULE 4: SINGLE ALARM SOUND RULE", "The control room horn sounds ONCE for the root event. It DOES NOT re-trigger 548 times for every downstream device. Operators maintain auditory focus to execute the EOP."),
    ]

    ry = 650
    for rhead, rdesc in suppress_rules:
        d.text((965, ry), rhead, font=get_font(13, True), fill=CYAN)
        rd_lines = wrap_text(d, rdesc, get_font(12), 730)
        for idx, rdl in enumerate(rd_lines):
            d.text((965, ry + 20 + idx * 17), rdl, font=get_font(12), fill=TEXT)
        ry += 82

    im.save(OUT_DIR / "fig-04-alarm-storm-suppression-and-topology.png", "PNG")
    print("Saved: fig-04-alarm-storm-suppression-and-topology.png")


# -------------------------------------------------------------
# FIG 5: Maintenance Window & MOP Interlocking
# -------------------------------------------------------------
def fig_05():
    im, d = new_canvas()
    draw_header(d, 5, "Maintenance Window Masking and Failsafe Watchdogs",
                "How to mute alarms during authorized maintenance without leaving dangerous blind spots when the window ends.")

    # 3 Column Architecture: Window Inception -> Masking Active -> Watchdog Expiration
    cols = [
        ("1. WINDOW INCEPTION GATE", "MOP & PTW Authorization", [
            ("CAB Approval Attached", "Every masked window requires a formal Change Advisory Board ticket number."),
            ("Explicit Point Mask List", "MOP must name the EXACT point IDs to be muted. Muting an entire substation or 'all alarms' is prohibited."),
            ("Maximum Window Duration", "Hard limit defined in advance (e.g. 120 minutes). Open-ended maintenance windows are forbidden."),
            ("Surviving Redundancy Audit", "BMS verifies that redundant unit is 100% healthy before permitting mask activation."),
        ], CYAN),
        ("2. ACTIVE MASKING ENVELOPE", "The Controlled Blind Spot", [
            ("Telemetry Preserved to Disk", "Values are still logged at full resolution. Muting only disables horn, paging, and client SLA portals."),
            ("Visual Watermark on Console", "Any screen displaying a masked point shows a prominent diagonal AMBER STRIPE and warning icon."),
            ("Control Room Whiteboard", "Duty Manager writes masked equipment tag and expiration time on physical abnormal state board."),
            ("Local Hardware Annunciation", "Local panel sirens remain active to protect technician standing in front of the gear."),
        ], AMBER),
        ("3. FAILSAFE WATCHDOG GATE", "Zero Forgotten Impairments", [
            ("Countdown Timer Expired", "When window closes, system DOES NOT silently remain muted."),
            ("Pre-Unmask Warning (T-15m)", "Console alerts Duty Manager: 'MOP Window for Chiller CH-02 closes in 15 min. Complete or extend.'"),
            ("Automatic Re-Arming", "At T=0, points automatically re-arm. If equipment is still abnormal, alarms sound immediately."),
            ("Formal Unmask Verification", "Duty Manager must execute functional walk and sign unmask ledger on handover sheet."),
        ], GREEN),
    ]

    for i, (title, sub, items, col) in enumerate(cols):
        x = 60 + i * 570
        d.rectangle((x, 150, x + 540, 1040), fill=PANEL, outline=col, width=2)
        d.text((x + 20, 175), title, font=get_font(18, True), fill=col)
        d.text((x + 20, 205), sub, font=get_font(13), fill=MUTED)
        d.line((x + 20, 230, x + 520, 230), fill=GRID, width=1)

        iy = 250
        for itit, idesc in items:
            d.rectangle((x + 20, iy, x + 520, iy + 165), fill=(20, 28, 45), outline=col, width=1)
            d.text((x + 35, iy + 15), itit, font=get_font(15, True), fill=col)
            # wrap text
            words = idesc.split()
            cur, l_list = "", []
            for w in words:
                if d.textlength(cur + " " + w, font=get_font(12)) <= 460:
                    cur += (" " if cur else "") + w
                else:
                    l_list.append(cur)
                    cur = w
            if cur:
                l_list.append(cur)
            for k, line in enumerate(l_list):
                d.text((x + 35, iy + 45 + k * 22), line, font=get_font(12), fill=TEXT)
            iy += 185

    im.save(OUT_DIR / "fig-05-maintenance-window-masking-matrix.png", "PNG")
    print("Saved: fig-05-maintenance-window-masking-matrix.png")


# -------------------------------------------------------------
# FIG 6: SOE & Microsecond Chronology
# -------------------------------------------------------------
def fig_06():
    im, d = new_canvas()
    draw_header(d, 6, "Sequence of Events (SOE) and Time Synchronization",
                "Why a 1-minute BMS polling cycle cannot explain a transient trip, and why microsecond PTP clocks are required for root-cause forensics.")

    # Top: The Clock Synchronization Hierarchy
    d.rectangle((60, 150, 1740, 360), fill=PANEL, outline=BLUE, width=2)
    d.text((90, 175), "DATA CENTER CLOCK SYNCHRONIZATION HIERARCHY", font=get_font(18, True), fill=BLUE)

    clock_tiers = [
        ("TIER 1: GNSS STRATUM-0", "GPS / GLONASS atomic clock roof antenna. Nanosecond reference pulse.", CYAN),
        ("TIER 2: PTP IEEE 1588v2", "Boundary switches & relay clocks. Synchronized to <= 1.0 microsecond.", BLUE),
        ("TIER 3: IRIG-B DIGITAL BUS", "Hardwired sync to electrical protective relays & digital fault recorders (DFRs).", GREEN),
        ("TIER 4: NTP SERVERS", "General IT & server telemetry. Accuracy within 1.0 to 5.0 milliseconds.", AMBER),
        ("TIER 5: BMS POLLING LOOP", "Serial Modbus polling (1 to 5 seconds). UNUSABLE FOR SOE FORENSICS.", RED),
    ]

    for k, (ct, cd, cc) in enumerate(clock_tiers):
        cx = 90 + k * 325
        d.rectangle((cx, 215, cx + 305, 335), fill=(20, 28, 45), outline=cc, width=1)
        d.text((cx + 15, 230), ct, font=get_font(13, True), fill=cc)
        words = cd.split()
        cur, l_list = "", []
        for w in words:
            if d.textlength(cur + " " + w, font=get_font(11)) <= 275:
                cur += (" " if cur else "") + w
            else:
                l_list.append(cur)
                cur = w
        if cur:
            l_list.append(cur)
        for idx, line in enumerate(l_list):
            d.text((cx + 15, 260 + idx * 20), line, font=get_font(11), fill=TEXT)

    # Bottom: Side-by-Side Comparison of Same Event
    # Left: 1-Minute BMS Polling (The Lie)
    d.rectangle((60, 390, 880, 1040), fill=(25, 20, 25), outline=RED, width=2)
    d.text((80, 415), "POOR TELEMETRY: 1-MINUTE BMS POLLING (INVERTED CAUSE)", font=get_font(17, True), fill=RED)
    d.text((80, 445), "Polling captures all events inside one bulk update; causes appear in reverse order.", font=get_font(13), fill=MUTED)

    bms_log = [
        ("09:14:00.000", "BMS Poll Cycle #4120 - All systems reporting NORMAL", GREEN),
        ("09:15:00.000", "BMS Poll Cycle #4121 - BATCH UPDATE RECEIVED:", RED),
        ("  --> (Point 1)", "CRAH-04 Low Airflow Alarm Recorded", AMBER),
        ("  --> (Point 2)", "Chiller CH-01 Flow Failure Recorded", AMBER),
        ("  --> (Point 3)", "UPS-01 On Battery Recorded", RED),
        ("  --> (Point 4)", "Feeder A Breaker Open Recorded", RED),
        ("CONCLUSION", "BMS shows CRAH failure FIRST, leading engineer to falsely blame mechanical airflow for the electrical blackout!", RED),
    ]

    by = 485
    for ts, txt, col in bms_log:
        d.text((80, by), ts, font=get_font(13, True), fill=CYAN if not ts.startswith("CON") else RED)
        txt_lines = wrap_text(d, txt, get_font(13), 620)
        for idx, tl in enumerate(txt_lines):
            d.text((230, by + idx * 18), tl, font=get_font(13), fill=col)
        by += max(50, len(txt_lines) * 20 + 10)

    # Right: Microsecond Sequence of Events (The Truth)
    d.rectangle((920, 390, 1740, 1040), fill=(20, 30, 45), outline=GREEN, width=2)
    d.text((940, 415), "SOE TELEMETRY: 1-MS TIME-STAMPED HARDWARE CHRONOLOGY", font=get_font(17, True), fill=GREEN)
    d.text((940, 445), "Protective relays latch timestamps locally at the physical contact contactor.", font=get_font(13), fill=MUTED)

    soe_log = [
        ("09:14:22.012 UTC", "Feeder A Cable Differential Relay 87L Trips (Real Root Cause)", RED),
        ("09:14:22.045 UTC", "Main Breaker 52-1 Trip Coil Energized; Contacts Part (33 ms)", RED),
        ("09:14:22.068 UTC", "Bus A Voltage Collapses to 0V (Recorded by DFR)", RED),
        ("09:14:22.082 UTC", "UPS-01 Rectifier SCRs Commutate Off; Inverter Takes Battery (14 ms)", AMBER),
        ("09:14:22.350 UTC", "Chiller CH-01 Compressor Under-Voltage Relay Drops Out (282 ms)", AMBER),
        ("09:14:25.100 UTC", "CRAH-04 Fan Airflow Sensor Reaches Low Threshold (3.088s later)", BLUE),
        ("CONCLUSION", "Microsecond SOE proves electrical cable fault tripped breaker 3 seconds before fans lost airflow. Zero ambiguity.", GREEN),
    ]

    sy = 485
    for ts, txt, col in soe_log:
        d.text((940, sy), ts, font=get_font(13, True), fill=CYAN if not ts.startswith("CON") else GREEN)
        txt_lines = wrap_text(d, txt, get_font(13), 570)
        for idx, tl in enumerate(txt_lines):
            d.text((1130, sy + idx * 18), tl, font=get_font(13), fill=col)
        sy += max(50, len(txt_lines) * 20 + 10)

    im.save(OUT_DIR / "fig-06-sequence-of-events-microsecond-chronology.png", "PNG")
    print("Saved: fig-06-sequence-of-events-microsecond-chronology.png")


# -------------------------------------------------------------
# FIG 7: Master Point Sheet Ledger
# -------------------------------------------------------------
def fig_07():
    im, d = new_canvas()
    draw_header(d, 7, "The Master Point Sheet and Audit Lifecycle",
                "The complete operational contract of a point: Addressing, sampling rate, filtering, deadbands, gating, and ownership.")

    # Top Overview Box
    d.rectangle((60, 150, 1740, 240), fill=PANEL, outline=CYAN, width=2)
    d.text((90, 165), "THE POINT CONTRACT: NO POINT SPEAKS WITHOUT A SIGNED LEDGER", font=get_font(18, True), fill=CYAN)
    d.text((90, 195), "Every point displayed in the control room must possess an audited row on the Master Point Sheet. If a column is blank, the point is muted.", font=get_font(13), fill=TEXT)

    # Table of Points (Simulated Master Ledger)
    headers = ["TAG / NAME", "HARDWARE PATH", "UNIT", "SCAN", "DEADBAND", "DWELL", "ALARM LIMIT", "ESCALATION", "OWNER"]
    col_w = [220, 280, 80, 80, 110, 100, 280, 260, 150]
    tx, ty = 60, 260

    # Draw Table Header
    d.rectangle((tx, ty, tx + 1680, ty + 40), fill=(20, 28, 45), outline=CYAN, width=1)
    hx = tx + 10
    for idx, h in enumerate(headers):
        d.text((hx, ty + 10), h, font=get_font(12, True), fill=CYAN)
        hx += col_w[idx]

    rows = [
        ("CDU-01-T_SUP", "modbus://cdu-01/reg-40102", "°C", "1.0s", "0.5 K", "10.0s", "H: 30.0°C | HH: 34.0°C", "P2 Major (Duty Mgr)", "Mech Lead"),
        ("CDU-01-DP_PUMP", "modbus://cdu-01/reg-40106", "bar", "1.0s", "0.1 bar", "5.0s", "L: 0.8 bar | LL: 0.5 bar", "P2 Major (Duty Mgr)", "Mech Lead"),
        ("SWG-01-V_BUS_A", "iec61850://swg-01/v_meas", "V", "0.02s", "5.0 V", "0.1s", "LL: 420V (Instant Trip)", "P1 Critical (Exec SLA)", "Elec Lead"),
        ("POD-03-DP_FLOOR", "bacnet://bms-pod3/ai-14", "Pa", "2.0s", "1.0 Pa", "15.0s", "L: 3.0 Pa | LL: 1.5 Pa", "Ticket (Shift Tech)", "HVAC Tech"),
        ("UPS-01-T_BATT", "snmp://ups-01/oid-batt-temp", "°C", "5.0s", "1.0 K", "60.0s", "H: 26.0°C | HH: 30.0°C", "P2 Major (Duty Mgr)", "Elec Lead"),
        ("VESDA-02-SMOKE", "contact://fap-02/relay-3", "State", "0.1s", "N/A", "2.0s", "Stage 1: Alert | Stage 2: Fire", "P1 Critical (EPO/EOP)", "Safety Off"),
        ("CDU-01-GLYCOL_PG", "lab://sample-cdu-01/refr", "% PG", "Manual", "N/A", "N/A", "L: 23.0% | H: 27.0%", "Work Order (Shift Round)", "Chem Lead"),
        ("GEN-01-FUEL_LVL", "4-20mA://tank-01/chan-1", "%", "10.0s", "2.0 %", "30.0s", "L: 60% | LL: 40% (Call Fuel)", "P2 Major (Supply SLA)", "Duty Mgr"),
    ]

    ry = ty + 40
    for r in rows:
        d.rectangle((tx, ry, tx + 1680, ry + 42), fill=PANEL if (ry // 42) % 2 == 0 else (24, 32, 47), outline=GRID, width=1)
        rx = tx + 10
        for cidx, val in enumerate(r):
            col = CYAN if cidx == 0 else (AMBER if cidx in (6, 7) else TEXT)
            d.text((rx, ry + 12), val, font=get_font(12, True if cidx in (0, 7) else False), fill=col)
            rx += col_w[cidx]
        ry += 42

    # Bottom Architectural Lifecycle
    d.rectangle((60, 640, 1740, 1040), fill=(20, 28, 45), outline=AMBER, width=2)
    d.text((90, 665), "THE 4 STAGES OF A POINT'S OPERATIONAL LIFECYCLE", font=get_font(18, True), fill=AMBER)

    stages = [
        ("STAGE 1: ACCEPTANCE GATE", "Before a point enters production:\n• Physical loop test verified with calibrated source.\n• Zero-scale and full-scale verified at console.\n• Point sheet signed by Commissioning Agent & Duty Mgr.\n• Unverified points stay tagged 'COMMISSIONING_MUTE'.", CYAN),
        ("STAGE 2: STEADY-STATE RUN", "During normal production shifts:\n• Quality bitmask monitored for staleness.\n• Dwell and deadband prevent alarm chatter.\n• Monthly calibration drift checks logged.\n• Sensor surface inspected for physical fouling.", GREEN),
        ("STAGE 3: CHANGE / MOP GOVERNANCE", "When equipment is serviced:\n• Point placed into 'MOP_SUPPRESSED' state.\n• Watchdog timer countdown active.\n• Physical whiteboard notes active override.\n• Automatic re-arming upon window expiration.", AMBER),
        ("STAGE 4: DECOMMISSIONING", "When equipment is retired:\n• Point deleted from active alarm polling tree.\n• Historical logs archived to cold storage.\n• Point sheet marked 'RETIRED' with date & engineer ID.\n• Never leave orphaned points polling dead wires.", RED),
    ]

    for sidx, (stitle, sbody, scol) in enumerate(stages):
        sx = 90 + sidx * 405
        d.rectangle((sx, 710, sx + 380, 1000), fill=PANEL, outline=scol, width=1)
        d.text((sx + 15, 730), stitle, font=get_font(15, True), fill=scol)
        lines = sbody.split("\n")
        syy = 765
        for l in lines:
            d.text((sx + 15, syy), l, font=get_font(12), fill=TEXT)
            syy += 24

    im.save(OUT_DIR / "fig-07-master-point-sheet-and-audit-lifecycle.png", "PNG")
    print("Saved: fig-07-master-point-sheet-and-audit-lifecycle.png")


def main():
    print("Generating Flagship Engineering Diagrams for Book 06: When a Monitor May Speak...")
    fig_01()
    fig_02()
    fig_03()
    fig_04()
    fig_05()
    fig_06()
    fig_07()
    print("All 7 Engineering Diagrams successfully generated for Book 06!")


if __name__ == "__main__":
    main()
