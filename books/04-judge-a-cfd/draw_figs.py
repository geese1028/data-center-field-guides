#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FIG = Path("/Users/geese/Downloads/book/books/04-judge-a-cfd/figures")
FONT = Path("/Users/geese/Downloads/book/books/01-liquid-load-bank/fonts")
BG, BLUE, CYAN, GRID = (30, 30, 30), (0, 102, 255), (0, 255, 255), (42, 42, 42)
TEXT, DIM = (255, 255, 255), (170, 170, 170)


def font(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(str(FONT / name), size)


def canvas(w, h):
    im = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(im)
    for x in range(0, w, 40):
        d.line((x, 0, x, h), fill=GRID)
    for y in range(0, h, 40):
        d.line((0, y, w, y), fill=GRID)
    d.rectangle((16, 16, w - 17, h - 17), outline=BLUE, width=2)
    return im, d


def header(d, kicker, title):
    d.text((36, 28), kicker, font=font(18, True), fill=CYAN)
    d.text((36, 58), title, font=font(28, True), fill=TEXT)


def save(im, name):
    FIG.mkdir(parents=True, exist_ok=True)
    im.save(FIG / name)


def dot(d, x, y, r=7):
    d.ellipse((x - r, y - r, x + r, y + r), outline=CYAN, width=2)


def jobs():
    im, d = canvas(1400, 780)
    header(d, "FIG 01   TWO JOBS", "The points decide whether the report may speak about this room.")
    d.rectangle((40, 150, 680, 700), outline=CYAN, width=2)
    d.rectangle((40, 150, 680, 196), fill=CYAN)
    d.text((56, 160), "1  MEASURE", font=font(20, True), fill=BG)
    lines = [
        "Supply opening: at least two points, then the average.",
        "Return opening: three points, then the average.",
        "Cabinets the report will name: inlet and outlet.",
        "Power from the feed, never the nameplate.",
        "Write both dates. A mixed year is not a calibration.",
    ]
    y = 230
    for i, line in enumerate(lines, 1):
        d.text((64, y), f"{i:02d}", font=font(16, True), fill=CYAN)
        d.text((110, y), line, font=font(18), fill=TEXT)
        y += 72
    d.rectangle((720, 150, 1360, 700), outline=BLUE, width=2)
    d.rectangle((720, 150, 1360, 196), fill=BLUE)
    d.text((736, 160), "2  USE THE REPORT", font=font(20, True), fill=TEXT)
    lines = [
        "One decision, written before the colors.",
        "Design, built hall, operating cause, or failure.",
        "IT block and air-unit block, separate.",
        "A plot with no plane is set aside.",
        "A remedy with no rerun is a proposal.",
    ]
    y = 230
    for i, line in enumerate(lines, 1):
        d.text((744, y), f"{i:02d}", font=font(16, True), fill=CYAN)
        d.text((790, y), line, font=font(18), fill=TEXT)
        y += 72
    save(im, "fig-jobs.png")


def openings():
    im, d = canvas(1400, 860)
    header(d, "FIG 02   OPENINGS", "Stand at the face. The aisle is the wrong place.")
    # unit body
    d.rectangle((80, 180, 520, 760), outline=BLUE, width=2)
    d.text((100, 196), "UNIT FACE", font=font(16, True), fill=CYAN)
    # return opening
    d.rectangle((140, 250, 460, 420), outline=CYAN, width=2)
    d.text((156, 262), "RETURN OPENING", font=font(16, True), fill=CYAN)
    for i, x in enumerate((200, 300, 400)):
        dot(d, x, 340)
        d.text((x - 8, 360), str(i + 1), font=font(14, True), fill=CYAN)
    d.text((156, 382), "three points, then average", font=font(16), fill=TEXT)
    # supply opening
    d.rectangle((140, 500, 460, 680), outline=CYAN, width=2)
    d.text((156, 514), "SUPPLY OPENING", font=font(16, True), fill=CYAN)
    for i, x in enumerate((230, 370)):
        dot(d, x, 590)
        d.text((x - 8, 610), str(i + 1), font=font(14, True), fill=CYAN)
    d.text((156, 640), "at least two, then average", font=font(16), fill=TEXT)
    # aisle rejected
    d.rectangle((620, 250, 1320, 680), outline=BLUE, width=2)
    d.text((644, 270), "AISLE  —  DO NOT SUBSTITUTE", font=font(16, True), fill=BLUE)
    notes = [
        "A screen in the aisle is not the supply.",
        "One point called the return is a story.",
        "Write which opening. Write the count.",
        "Repeat for every unit that serves this room.",
    ]
    y = 400
    for note in notes:
        d.text((660, y), note, font=font(20), fill=TEXT)
        y += 48
    save(im, "fig-openings.png")


def cabinet():
    im, d = canvas(1400, 820)
    header(d, "FIG 03   THE ROW", "Walk it. Inlet and outlet. A room mean is not a cabinet.")
    labels = ["NOT WALKED", "THIS CABINET", "NOT WALKED"]
    colors = [DIM, CYAN, DIM]
    for i, (lab, col) in enumerate(zip(labels, colors)):
        x = 60 + i * 300
        d.rectangle((x, 180, x + 250, 620), outline=col, width=2)
        d.text((x + 16, 196), lab, font=font(14, True), fill=col)
        if i == 1:
            d.rectangle((x + 30, 260, x + 220, 400), outline=CYAN, width=2)
            d.text((x + 48, 280), "FRONT INLET", font=font(16, True), fill=CYAN)
            dot(d, x + 80, 340)
            dot(d, x + 160, 340)
            d.rectangle((x + 30, 440, x + 220, 580), outline=BLUE, width=2)
            d.text((x + 48, 460), "REAR OUTLET", font=font(16, True), fill=TEXT)
            dot(d, x + 80, 520)
            dot(d, x + 160, 520)
        else:
            d.text((x + 24, 380), "no points", font=font(18), fill=DIM)
    d.rectangle((980, 200, 1340, 620), outline=BLUE, width=2)
    d.text((1000, 230), "NOT THIS", font=font(18, True), fill=BLUE)
    d.text((1000, 280), "One number for", font=font(20), fill=TEXT)
    d.text((1000, 316), "the whole room,", font=font(20), fill=TEXT)
    d.text((1000, 352), "offered as every", font=font(20), fill=TEXT)
    d.text((1000, 388), "cabinet inlet.", font=font(20), fill=TEXT)
    d.text((1000, 470), "If the model has", font=font(18), fill=DIM)
    d.text((1000, 502), "no point here,", font=font(18), fill=DIM)
    d.text((1000, 534), "it cannot be", font=font(18), fill=DIM)
    d.text((1000, 566), "corrected here.", font=font(18), fill=DIM)
    save(im, "fig-cabinet.png")


def power():
    im, d = canvas(1400, 640)
    header(d, "FIG 04   HEAT IN", "The feed is the load. The nameplate is a ceiling.")
    d.rectangle((60, 200, 620, 520), outline=BLUE, width=2)
    d.text((80, 220), "NAMEPLATE", font=font(18, True), fill=BLUE)
    d.text((80, 280), "A maximum the maker printed.", font=font(20), fill=TEXT)
    d.text((80, 330), "Not what the cabinet", font=font(20), fill=TEXT)
    d.text((80, 366), "is rejecting today.", font=font(20), fill=TEXT)
    d.text((80, 440), "Leave it out of the model", font=font(18), fill=DIM)
    d.text((80, 472), "unless the claim says ceiling.", font=font(18), fill=DIM)
    d.rectangle((740, 200, 1340, 520), outline=CYAN, width=2)
    d.text((760, 220), "THE PATH", font=font(18, True), fill=CYAN)
    d.text((760, 280), "Cabinet strip, or the upstream", font=font(20), fill=TEXT)
    d.text((760, 316), "unit that actually feeds it.", font=font(20), fill=TEXT)
    d.text((760, 380), "Write the source on the sheet", font=font(18), fill=TEXT)
    d.text((760, 414), "before you compare.", font=font(18), fill=TEXT)
    d.text((760, 470), "If the model still has the plate,", font=font(18), fill=CYAN)
    d.text((760, 504), "replace it and rerun.", font=font(18), fill=CYAN)
    save(im, "fig-power.png")


def correct():
    im, d = canvas(1400, 820)
    header(d, "FIG 05   CORRECTION", "Disagreement is not averaged away.")
    d.rectangle((50, 150, 1340, 250), outline=CYAN, width=2)
    d.text((70, 182), "CABINET INLET IN THE REPORT   ≠   CABINET INLET YOU MEASURED", font=font(20, True), fill=CYAN)
    # allowed
    d.text((70, 280), "ALLOWED", font=font(16, True), fill=CYAN)
    steps = ["Name an input\nyou can walk to", "Change that\ninput only", "Rerun the\nsame scene", "Compare the\ninlet again"]
    x = 50
    for i, step in enumerate(steps):
        d.rectangle((x, 320, x + 250, 470), outline=CYAN, width=2)
        yy = 345
        for line in step.split("\n"):
            d.text((x + 16, yy), line, font=font(18), fill=TEXT)
            yy += 32
        if i < 3:
            d.line((x + 250, 395, x + 290, 395), fill=CYAN, width=2)
        x += 320
    d.text((70, 510), "Blank missing. Grille blocked. Aisle open. Unit off. Nameplate still in. Setpoint from a brochure.", font=font(16), fill=DIM)
    # refused
    d.rectangle((50, 560, 1340, 760), outline=BLUE, width=2)
    d.text((70, 580), "REFUSED", font=font(16, True), fill=BLUE)
    d.text((70, 630), "Blend the plot toward the meter until they agree.", font=font(22), fill=TEXT)
    d.text((70, 680), "A third tweak with no name. A color scale moved so the inlet looks fine.", font=font(20), fill=TEXT)
    save(im, "fig-correct.png")


def read_order():
    im, d = canvas(1400, 900)
    header(d, "FIG 06   THE FILE", "Read down. Do not open on the picture.")
    rows = [
        ("01", "PURPOSE", "One sentence. If missing, write purpose not stated. Do not invent one.", CYAN),
        ("02", "INPUTS", "Room, IT, cooling, blockage, sensors. Copied from another hall: stop.", TEXT),
        ("03", "SCENE", "Load, units on, containment, setpoints. Disagree with the list: two reports.", TEXT),
        ("04", "IT BLOCK", "Inlet and outlet for the cabinets named. Not one room average.", TEXT),
        ("05", "AIR BLOCK", "Supply, return, flow or pressure, unit by unit.", TEXT),
        ("06", "PLOTS", "After the blocks. Plane named, or set aside. A calm plane is still a choice.", BLUE),
        ("07", "SENTENCE", "Must point at a block. A color is not a block.", CYAN),
    ]
    y = 140
    for idx, title, line, col in rows:
        d.rectangle((40, y, 1360, y + 96), outline=col, width=2)
        d.text((56, y + 14), idx, font=font(16, True), fill=CYAN)
        d.text((120, y + 12), title, font=font(18, True), fill=TEXT)
        d.text((120, y + 48), line, font=font(18), fill=TEXT)
        y += 106
    save(im, "fig-read.png")


def use():
    im, d = canvas(1400, 860)
    header(d, "FIG 07   ONE DECISION", "Write it before the colors. The other three stay out.")
    cards = [
        ("DESIGN", "May say which option is worse.", "May not say it has been built.", "Measurements not required.", "Both options, same scene rules."),
        ("BUILT HALL", "May say this room meets the comparison.", "May not speak if not corrected.", "Points and a named rerun required.", "Liquid side is another book."),
        ("OPERATE", "May name a cause you can walk to.", "May not send you to rebuild on a color.", "If you cannot find the input, stop.", "A remedy is a second run."),
        ("FAILURE", "May show the inlet change.", "May not be a full-load plot plus a caption.", "Its own scene. Time only if computed.", "Steady means no narrated minute."),
    ]
    for i, (title, a, b, c, e) in enumerate(cards):
        col, row = i % 2, i // 2
        x, y = 40 + col * 680, 140 + row * 340
        d.rectangle((x, y, x + 650, y + 310), outline=BLUE, width=2)
        d.rectangle((x, y, x + 650, y + 40), fill=BLUE)
        d.text((x + 16, y + 8), title, font=font(18, True), fill=TEXT)
        d.text((x + 16, y + 60), a, font=font(18), fill=CYAN)
        d.text((x + 16, y + 100), b, font=font(18), fill=TEXT)
        d.text((x + 16, y + 160), c, font=font(16), fill=DIM)
        d.text((x + 16, y + 196), e, font=font(16), fill=DIM)
    save(im, "fig-uses.png")


def scale():
    im, d = canvas(1400, 720)
    header(d, "FIG 08   SAME FIELD", "Move the bar. The physics did not change. The color did.")
    def field(x0, title, hot_at):
        d.text((x0, 150), title, font=font(18, True), fill=CYAN)
        d.rectangle((x0, 200, x0 + 560, 520), outline=BLUE, width=2)
        # bands
        for i, frac in enumerate((0.15, 0.35, 0.55, 0.8)):
            y = 210 + i * 70
            d.rectangle((x0 + 20, y, x0 + 420, y + 56), outline=DIM, width=1)
        d.rectangle((x0 + 450, 210, x0 + 530, 500), outline=CYAN, width=2)
        d.text((x0 + 458, 220), "BAR", font=font(14, True), fill=CYAN)
        d.line((x0 + 490, hot_at, x0 + 530, hot_at), fill=CYAN, width=3)
        d.text((x0 + 20, 540), "Limit is not on this bar.", font=font(16), fill=TEXT)
    field(50, "SCALE A  —  LOOKS CALM", 460)
    field(760, "SCALE B  —  LOOKS HOT", 250)
    d.text((50, 650), "THE COMPARISON WAS WRITTEN BEFORE THE RUN: QUANTITY, LIMIT, EDITION.", font=font(18, True), fill=CYAN)
    save(im, "fig-scale.png")


def path():
    im, d = canvas(1400, 720)
    header(d, "FIG 09   PATH AND RATE", "Do not promote a line into a flow.")
    d.text((50, 150), "WHAT A STREAMLINE IS", font=font(16, True), fill=CYAN)
    d.rectangle((50, 190, 760, 560), outline=BLUE, width=2)
    pts = [(100, 480), (200, 360), (320, 400), (440, 280), (560, 300), (700, 220)]
    d.line(pts, fill=CYAN, width=3)
    for x, y in pts[1:-1]:
        dot(d, x, y, 5)
    d.text((80, 500), "A path the air took in this scene.", font=font(18), fill=TEXT)
    d.text((820, 150), "WHERE THE RATE LIVES", font=font(16, True), fill=CYAN)
    d.rectangle((820, 190, 1340, 560), outline=CYAN, width=2)
    d.text((844, 220), "AIR-UNIT BLOCK", font=font(18, True), fill=CYAN)
    rows = ["Unit", "Supply average", "Return average", "Flow or pressure", "From the claim"]
    y = 280
    for row in rows:
        d.text((844, y), row, font=font(20), fill=TEXT)
        d.line((844, y + 28, 1280, y + 28), fill=DIM, width=1)
        y += 48
    d.text((50, 640), "IF THE BLOCK HAS NO RATE, THE RATE IS ABSENT. ABSENT IS NOT A FINGER-TRACE.", font=font(16, True), fill=CYAN)
    save(im, "fig-path.png")


def sheets():
    im, d = canvas(1400, 640)
    header(d, "FIG 10   ORDER", "The use sheet is blank until the measurement sheet is filled.")
    d.rectangle((40, 160, 680, 560), outline=CYAN, width=2)
    d.text((60, 180), "MEASUREMENT", font=font(18, True), fill=CYAN)
    for i, line in enumerate([
        "Dates: measurement and layout",
        "Supply points, at the opening",
        "Return points, three",
        "Inlet and outlet, cabinets named",
        "Power source",
        "Input changed, or not corrected",
    ]):
        d.text((60, 240 + i * 46), line, font=font(18), fill=TEXT)
    d.polygon([(720, 340), (780, 360), (720, 380)], fill=CYAN)
    d.rectangle((820, 160, 1360, 560), outline=BLUE, width=2)
    d.text((840, 180), "USE", font=font(18, True), fill=TEXT)
    for i, line in enumerate([
        "Purpose, copied",
        "One decision",
        "Scene in four lines",
        "Blocks present, planes named",
        "Comparison written first",
        "Rerun, or not a conclusion",
    ]):
        d.text((840, 240 + i * 46), line, font=font(18), fill=TEXT)
    save(im, "fig-sheets.png")


if __name__ == "__main__":
    for fn in (jobs, openings, cabinet, power, correct, read_order, use, scale, path, sheets):
        fn()
        print(fn.__name__)
