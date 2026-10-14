#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path("/Users/geese/Downloads/book/books/03-run-one-test")
FIG = ROOT / "figures"
FONT_DIR = Path("/Users/geese/Downloads/book/books/01-liquid-load-bank/fonts")

BG = (30, 30, 30)
BLUE = (0, 102, 255)
CYAN = (0, 255, 255)
GRID = (42, 42, 42)
TEXT = (255, 255, 255)
DIM = (180, 180, 180)


def font(size, bold=False):
    path = FONT_DIR / ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf")
    return ImageFont.truetype(str(path), size)


def new_canvas(w, h):
    im = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(im)
    for x in range(0, w, 40):
        d.line((x, 0, x, h), fill=GRID, width=1)
    for y in range(0, h, 40):
        d.line((0, y, w, y), fill=GRID, width=1)
    d.rectangle((18, 18, w - 19, h - 19), outline=BLUE, width=2)
    return im, d


def corners(d, xy, color=CYAN, arm=16):
    x0, y0, x1, y1 = xy
    for x, y, sx, sy in ((x0, y0, 1, 1), (x1, y0, -1, 1), (x0, y1, 1, -1), (x1, y1, -1, -1)):
        d.line((x, y, x + sx * arm, y), fill=color, width=2)
        d.line((x, y, x, y + sy * arm), fill=color, width=2)


def header(d, kicker, title):
    d.text((40, 28), kicker, font=font(20, bold=True), fill=CYAN)
    d.text((40, 58), title, font=font(32, bold=True), fill=TEXT)


def save(im, name):
    FIG.mkdir(parents=True, exist_ok=True)
    path = FIG / name
    im.save(path, "PNG")
    return path


def panel(d, xy, index, title, lines):
    x0, y0, x1, y1 = xy
    d.rectangle(xy, outline=BLUE, width=2)
    corners(d, xy)
    d.rectangle((x0, y0, x1, y0 + 34), fill=BLUE)
    d.text((x0 + 12, y0 + 7), index, font=font(15, bold=True), fill=CYAN)
    d.text((x0 + 52, y0 + 7), title.upper(), font=font(16, bold=True), fill=TEXT)
    y = y0 + 50
    for line in lines:
        d.text((x0 + 14, y), line, font=font(18), fill=TEXT)
        y += 28


def faults():
    im, d = new_canvas(1400, 620)
    header(d, "FIG 01   CDU FAULTS", "Open one thing. Write what held.")
    rows = [
        ("01", "Sensor", "Alarm. Drop that sensor."),
        ("02", "PLC", "Running unit holds."),
        ("03", "Drive power", "Alarm, then switch."),
        ("04", "Drive fault", "Alarm, then switch."),
        ("05", "Drive comms", "Hold. Start standby."),
        ("06", "Group master", "Keep running. Self-hold."),
        ("07", "Valve power", "Self-hold."),
        ("08", "One ATS path", "Switch. One CDU only."),
    ]
    gap, left, top = 16, 40, 140
    w, h = 320, 150
    for i, item in enumerate(rows):
        col, row = i % 4, i // 4
        x = left + col * (w + gap)
        y = top + row * (h + gap)
        panel(d, (x, y, x + w, y + h), item[0], item[1], [item[2], "One row. One clock."])
    d.text((40, 560), "NO VENDOR LOGIC ATTACHED  =  NOT DEMONSTRATED.  NOT A PASS.", font=font(20, bold=True), fill=CYAN)
    return save(im, "cdu-faults.png")


def ats():
    im, d = new_canvas(1400, 640)
    header(d, "FIG 02   ONE CDU", "Open one path. The other must carry it.")
    # two feeds into one CDU
    d.rectangle((80, 220, 280, 300), outline=CYAN, width=2)
    d.rectangle((80, 360, 280, 440), outline=BLUE, width=2)
    d.text((100, 244), "PATH A", font=font(22, bold=True), fill=CYAN)
    d.text((100, 384), "PATH B", font=font(22, bold=True), fill=TEXT)
    d.line((280, 260, 520, 340), fill=CYAN, width=3)
    d.line((280, 400, 520, 360), fill=BLUE, width=3)
    d.rectangle((520, 250, 880, 430), outline=BLUE, width=2)
    corners(d, (520, 250, 880, 430))
    d.text((548, 280), "THIS CDU", font=font(22, bold=True), fill=TEXT)
    d.text((548, 324), "Controller reboot?  Y / N", font=font(20), fill=TEXT)
    d.text((548, 364), "Cooling stopped?  Y / N", font=font(20), fill=TEXT)
    d.text((940, 250), "THEN SWAP", font=font(18, bold=True), fill=CYAN)
    d.text((940, 290), "Open B.", font=font(20), fill=TEXT)
    d.text((940, 326), "A must carry it.", font=font(20), fill=TEXT)
    d.text((940, 362), "Repeat for every", font=font(20), fill=TEXT)
    d.text((940, 398), "CDU in the unit.", font=font(20), fill=TEXT)
    d.text((40, 520), "THIS IS NOT A HALL FEEDER OPENING. THAT IS A DIFFERENT SHEET.", font=font(20, bold=True), fill=CYAN)
    d.text((40, 564), "A hall path test does not sign this box.", font=font(20), fill=DIM)
    return save(im, "cdu-ats.png")


def ring():
    im, d = new_canvas(1400, 720)
    header(d, "FIG 03   RING", "Nearest branch, then the farthest. Only if it is a ring.")
    # CDU box
    d.rectangle((80, 280, 260, 420), outline=CYAN, width=2)
    d.text((108, 330), "CDU", font=font(28, bold=True), fill=CYAN)
    loop = [(300, 240), (1180, 240), (1180, 500), (300, 500), (300, 240)]
    d.line(loop, fill=BLUE, width=4)
    d.line((260, 330, 300, 280), fill=BLUE, width=3)
    d.line((260, 370, 300, 460), fill=BLUE, width=3)
    # near valve
    d.rectangle((340, 300, 520, 390), outline=CYAN, width=2)
    corners(d, (340, 300, 520, 390))
    d.text((360, 322), "NEAREST", font=font(18, bold=True), fill=CYAN)
    d.text((360, 350), "Open, then close", font=font(16), fill=TEXT)
    # far valve
    d.rectangle((860, 300, 1080, 390), outline=BLUE, width=2)
    corners(d, (860, 300, 1080, 390), BLUE)
    d.text((900, 322), "FARTHEST", font=font(18, bold=True), fill=TEXT)
    d.text((888, 350), "Open, then close", font=font(16), fill=TEXT)
    d.text((40, 600), "EACH MOVE: LOAD BANKS STABLE?   SECONDARY TEMPERATURE STABLE?   FLOW STABLE?", font=font(18, bold=True), fill=CYAN)
    d.text((40, 648), "NOT A RING  =  N/A.  DO NOT INVENT A LOOP.", font=font(20, bold=True), fill=TEXT)
    return save(im, "cdu-ring.png")


def compare():
    im, d = new_canvas(1400, 640)
    header(d, "FIG 04   TWO READINGS", "Pipe sensor against the CDU. Difference, then the limit.")
    panel(d, (60, 180, 420, 420), "01", "Pipe sensor", ["Named in the script.", "Not a pasted point list."])
    panel(d, (500, 180, 860, 420), "02", "CDU reading", ["Same quantity.", "Same clock."])
    panel(d, (940, 180, 1340, 420), "03", "Difference", ["Limit from the spec.", "Blank limit, no pass."])
    d.line((420, 300, 500, 300), fill=CYAN, width=3)
    d.line((860, 300, 940, 300), fill=CYAN, width=3)
    d.text((40, 500), "ONE ROW PER POINT THE SCRIPT NAMES.  STOP WHEN THE SCRIPT STOPS.", font=font(20, bold=True), fill=CYAN)
    d.text((40, 548), "A screen that agrees with another screen is not this test.", font=font(20), fill=DIM)
    return save(im, "cdu-compare.png")


def logic():
    im, d = new_canvas(1400, 780)
    header(d, "FIG 05   VENDOR LOGIC", "Eight logics. No attachment, no pass.")
    items = [
        ("01", "3-way valve", "Versus supply temp"),
        ("02", "Pump and bypass", "Speed and the valve"),
        ("03", "Pressure", "Difference control"),
        ("04", "Flow", "How flow is held"),
        ("05", "Rotation", "Which unit runs"),
        ("06", "Fault switch", "Who takes over"),
        ("07", "Trigger alarms", "What starts a switch"),
        ("08", "One sensor dead", "Temp or pressure"),
    ]
    gap, left, top = 16, 40, 150
    w, h = 320, 140
    for i, item in enumerate(items):
        col, row = i % 4, i // 4
        x = left + col * (w + gap)
        y = top + row * (h + 20)
        panel(d, (x, y, x + w, y + h), item[0], item[1], [item[2]])
    d.text((40, 700), "ATTACH THE VENDOR PAGE.  JUDGE IT.  DO NOT RETELL IT HERE.", font=font(20, bold=True), fill=CYAN)
    return save(im, "cdu-logic.png")


def transient():
    im, d = new_canvas(1400, 720)
    header(d, "FIG 06   THE TRANSIENT", "The pull is the result. The flat line after is not.")
    # axes
    x0, y0, x1, y1 = 120, 180, 1280, 520
    d.line((x0, y1, x1, y1), fill=DIM, width=2)
    d.line((x0, y0, x0, y1), fill=DIM, width=2)
    d.text((x0, y1 + 16), "INJECT", font=font(16, bold=True), fill=CYAN)
    d.text((520, y1 + 16), "PEAK OR VALLEY", font=font(16, bold=True), fill=CYAN)
    d.text((980, y1 + 16), "RECOVERED", font=font(16, bold=True), fill=DIM)
    d.text((28, 300), "TEMP", font=font(16, bold=True), fill=DIM)
    # schematic trace: flat, spike, settle
    pts = [(140, 400), (360, 400), (420, 240), (560, 250), (700, 360), (900, 390), (1240, 390)]
    d.line(pts, fill=CYAN, width=3)
    d.ellipse((350, 390, 372, 412), outline=CYAN, width=2)
    d.ellipse((548, 238, 572, 262), outline=CYAN, width=2)
    d.line((900, 180, 900, 530), fill=BLUE, width=2)
    d.text((920, 188), "NOT THE PASS", font=font(18, bold=True), fill=BLUE)
    d.text((40, 600), "WRITE THE CLOCK AT INJECT, AT THE PEAK, AND AT ABANDON OR RECOVER.", font=font(18, bold=True), fill=CYAN)
    d.text((40, 644), "NO SCALE ON THIS FIGURE. THE SCRIPT NAMES THE LIMIT.", font=font(18), fill=DIM)
    return save(im, "cdu-transient.png")


if __name__ == "__main__":
    for fn in (faults, ats, ring, compare, logic, transient):
        print(fn())
