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


def corners(d, xy, color=CYAN, arm=14):
    x0, y0, x1, y1 = xy
    for x, y, sx, sy in ((x0, y0, 1, 1), (x1, y0, -1, 1), (x0, y1, 1, -1), (x1, y1, -1, -1)):
        d.line((x, y, x + sx * arm, y), fill=color, width=2)
        d.line((x, y, x, y + sy * arm), fill=color, width=2)


def header(d, kicker, title):
    d.text((40, 28), kicker, font=font(20, bold=True), fill=CYAN)
    d.text((40, 58), title, font=font(30, bold=True), fill=TEXT)


def save(im, name):
    FIG.mkdir(parents=True, exist_ok=True)
    path = FIG / name
    im.save(path, "PNG")
    return path


def panel(d, xy, index, title, lines, head=BLUE):
    x0, y0, x1, y1 = xy
    d.rectangle(xy, outline=BLUE, width=2)
    corners(d, xy)
    d.rectangle((x0, y0, x1, y0 + 32), fill=head)
    d.text((x0 + 10, y0 + 6), index, font=font(14, bold=True), fill=CYAN)
    d.text((x0 + 48, y0 + 6), title.upper(), font=font(15, bold=True), fill=TEXT)
    y = y0 + 44
    for line in lines:
        d.text((x0 + 12, y), line, font=font(16), fill=TEXT)
        y += 24


def chips(name, kicker, title, items, footer, cols=4, row_h=148):
    rows = (len(items) + cols - 1) // cols
    height = 150 + rows * (row_h + 16) + (36 if footer else 10)
    im, d = new_canvas(1400, height)
    header(d, kicker, title)
    gap, left, top = 14, 40, 130
    w = (1320 - gap * (cols - 1)) // cols
    for i, item in enumerate(items):
        col, row = i % cols, i // cols
        x = left + col * (w + gap)
        y = top + row * (row_h + 16)
        panel(d, (x, y, x + w, y + row_h), item[0], item[1], item[2:])
    if footer:
        d.text((40, height - 48), footer, font=font(18, bold=True), fill=CYAN)
    return save(im, name)


def three():
    return chips(
        "fig-three.png", "FIG 07   THREE BOOKS", "Three jobs. Do not mix the signatures.",
        [
            ("01", "Build", "Accept the load bank.", "Not this book."),
            ("02", "Read", "Judge the file.", "A hit is a time."),
            ("03", "Run", "Finish the test.", "Sheets, then leave."),
        ],
        "A CALM CURVE DOES NOT ACCEPT THE MACHINE.",
        cols=3, row_h=160,
    )


def claim():
    return chips(
        "fig-claim.png", "FIG 08   THE CLAIM", "Write both columns before you count load banks.",
        [
            ("IN", "Proves", "The plant, with a load", "bank standing in."),
            ("IN", "Decision", "Hand toward IT,", "or not yet."),
            ("OUT", "Does not", "Boot the rack.", "Train a model."),
            ("OUT", "Does not", "Accept the prototype.", "Invent a flow."),
        ],
        "A REMEMBERED NUMBER FROM THE LAST HALL IS NOT A CITATION.",
        cols=4, row_h=170,
    )


def twelve():
    items = [
        ("01", "OPR", "The claim."),
        ("02", "BOD", "How it was meant."),
        ("03", "Approve", "Both, before tests."),
        ("04", "Design", "Attach, or cut in writing."),
        ("05", "Plan", "Gates, not a bar chart."),
        ("06", "Contract", "What you can still verify."),
        ("07", "Checklists", "Before energy."),
        ("08", "Scripts", "Expected result first."),
        ("09", "Witness", "Not the same as execute."),
        ("10", "Register", "Owner, state, close."),
        ("11", "Reports", "A blank day is a note."),
        ("12", "Manual", "Stops, gaps, deviations."),
    ]
    return chips(
        "fig-twelve.png", "FIG 09   PRODUCTS", "Twelve products. Silence is not a cut.",
        items, "IF YOU WILL NOT DO ONE, SAY SO ON PAGE ONE.", cols=4, row_h=120,
    )


def levels():
    im, d = new_canvas(1400, 860)
    header(d, "FIG 10   TWO NUMBERS", "Do not file a true walk-through under a false level.")
    d.text((60, 128), "CERTIFICATE", font=font(16, bold=True), fill=CYAN)
    d.text((820, 128), "WHERE THE SHEET FILES", font=font(16, bold=True), fill=CYAN)
    left = [
        "L0  Design and planning",
        "L1  Factory testing",
        "L2  Delivery, pre-start",
        "L3  Start-up",
        "L4  Functional, one machine",
        "L5  Integrated, the heat",
        "L6  Close-out",
    ]
    for i, line in enumerate(left):
        y = 168 + i * 78
        d.rectangle((50, y, 520, y + 58), outline=BLUE, width=2)
        d.text((66, y + 16), line, font=font(18, bold=True), fill=TEXT)
    # L2 y=168+156=324, L4 y=168+312=480, L5 y=168+390=558, L1 y=168+78=246
    pairs = [
        (324, "Static, no energy", "Not factory."),
        (480, "One machine", "Not the heat window."),
        (558, "Heat window", "Not a turnover."),
    ]
    for y, title, note in pairs:
        d.line((520, y + 29, 760, y + 29), fill=CYAN, width=2)
        d.rectangle((760, y, 1320, y + 58), outline=CYAN, width=2)
        d.text((776, y + 6), title, font=font(18, bold=True), fill=TEXT)
        d.text((776, y + 30), note, font=font(15), fill=CYAN)
    d.line((520, 275, 700, 200), fill=BLUE, width=2)
    d.line((680, 188, 760, 200), fill=BLUE, width=2)
    d.text((530, 176), "DO NOT FILE STATIC HERE", font=font(15, bold=True), fill=BLUE)
    d.text((50, 800), "A SIGNED L1 WITH A STATIC SHEET ATTACHED IS A FALSE DOCUMENT.", font=font(18, bold=True), fill=CYAN)
    return save(im, "fig-levels.png")


def parties():
    return chips(
        "fig-parties.png", "FIG 11   PARTIES", "Three hats. A shared hat needs a sentence.",
        [
            ("01", "Owner", "Witnesses.", "Signs the result."),
            ("02", "Verification", "Writes the script.", "Does not close its own fail."),
            ("03", "Constructor", "Holds the hall file.", "Fixes the punch list."),
        ],
        "WITNESS AND FIXER ON ONE SIGNATURE IS HOW A DEFECT DISAPPEARS.",
        cols=3, row_h=160,
    )


def hands():
    return chips(
        "fig-hands.png", "FIG 12   HANDS", "Five functions. Headcount can be smaller. The check cannot.",
        [
            ("01", "Lead", "Owns the stop decision."),
            ("02", "Electrical", "Phase, breakers, transfer."),
            ("03", "Mechanical", "Vent, hold, the curve."),
            ("04", "Controls", "Screen versus instrument."),
            ("05", "Technician", "Sheets, backup, the list."),
        ],
        "ONE PERSON MAY NOT CHECK THE LINE THEY JUST PERFORMED.",
        cols=5, row_h=150,
    )


def command():
    im, d = new_canvas(1400, 520)
    header(d, "FIG 13   AUTHORITY", "One name commands heat. Every name may stop.")
    panel(d, (60, 160, 660, 400), "01", "Command heat", ["One name.", "Written before the step.", "Nobody else adds a fraction."])
    panel(d, (740, 160, 1340, 400), "02", "Hit the stop", ["Every person in the room.", "No radio required.", "No one may override it."])
    d.text((40, 450), "HOLD ON, LET ME SEE THE CURVE  =  THE PROJECT HAS ENDED.", font=font(18, bold=True), fill=CYAN)
    return save(im, "fig-command.png")


def month():
    im, d = new_canvas(1400, 480)
    header(d, "FIG 14   TIME", "The month is the work. The window is the photograph.")
    d.rectangle((60, 180, 980, 300), outline=BLUE, width=2)
    d.text((80, 214), "SURVEY    SCRIPTS    STATIC    ONE SYSTEM    PUNCH    PACK", font=font(18, bold=True), fill=TEXT)
    d.rectangle((1000, 170, 1320, 310), outline=CYAN, width=3)
    corners(d, (1000, 170, 1320, 310))
    d.text((1040, 200), "HEAT", font=font(28, bold=True), fill=CYAN)
    d.text((1030, 248), "A few days", font=font(18), fill=TEXT)
    d.text((40, 380), "A LATE CRATE DOES NOT EARN THE RIGHT TO SKIP STATIC.", font=font(18, bold=True), fill=CYAN)
    return save(im, "fig-month.png")


def survey():
    return chips(
        "fig-survey.png", "FIG 15   SURVEY", "Four questions. No drawing pasted into the note.",
        [
            ("01", "Path", "Can it arrive."),
            ("02", "Structure", "Can it stand."),
            ("03", "Interface", "The point exists."),
            ("04", "Monitor", "What the screen cannot show."),
        ],
        "WHAT YOU COULD NOT SEE IS AN OPEN ITEM.",
        cols=4, row_h=140,
    )


def blank():
    im, d = new_canvas(1400, 480)
    header(d, "FIG 16   A BLANK", "A blank cell is a stop. A borrowed number is a lie.")
    panel(d, (60, 160, 660, 380), "01", "Blank limit", ["Do not run that line.", "Do not call it a pass.", "Cite the spec, or wait."])
    panel(d, (740, 160, 1340, 380), "02", "Last hall's number", ["Not a citation.", "Not this script.", "Leave it out."])
    return save(im, "fig-blank.png")


def scriptset():
    items = [
        ("01", "Unpack", "Fittings, scars."),
        ("02", "Static electrical", "Locked out."),
        ("03", "Fill and vent", "Or a record you read."),
        ("04", "Breaker trace", "Before any overload."),
        ("05", "One CDU", "Start, stop, changeover."),
        ("06", "Alarms", "Or not demonstrated."),
        ("07", "No-heat curve", "Only if the script asks."),
        ("08", "Ladder", "Its own signature."),
        ("09", "One unit pulled", "The transient."),
        ("10", "One path", "This CDU, then the hall."),
        ("11", "Step change", "Not the ladder."),
        ("12", "Shutdown", "Order ticked."),
    ]
    return chips(
        "fig-script-set.png", "FIG 17   ONE SCRIPT", "One claim, one signature. Drop a line only in writing.",
        items, "A BLUR OF FOUR TESTS ON ONE SCRIBBLE IS NOT A RESULT.", cols=4, row_h=120,
    )


def static():
    im, d = new_canvas(1400, 420)
    header(d, "FIG 18   BEFORE ENERGY", "This order. Heat is not a way to find a cracked fitting.")
    labels = ["UNPACK", "LOCK OUT", "PHASE", "VENT", "HOLD", "BREAKERS UP"]
    x = 50
    for i, lab in enumerate(labels):
        d.rectangle((x, 190, x + 200, 280), outline=CYAN if i == 0 else BLUE, width=2)
        d.text((x + 16, 218), f"{i+1:02d}", font=font(14, bold=True), fill=CYAN)
        d.text((x + 16, 240), lab, font=font(16, bold=True), fill=TEXT)
        if i < len(labels) - 1:
            d.line((x + 200, 235, x + 214, 235), fill=CYAN, width=2)
        x += 214
    d.text((40, 340), "A CELL WITH NO LIMIT STAYS A STOP. THIS BOOK DOES NOT PRINT THE OHMS.", font=font(18, bold=True), fill=CYAN)
    return save(im, "fig-static.png")


def phase():
    im, d = new_canvas(1400, 460)
    header(d, "FIG 19   PHASE", "Wrong order can reverse a pump. That is an electrical fact.")
    panel(d, (60, 160, 660, 360), "01", "Look", ["Phase order written.", "Not the word ok.", "Blank means no energy."])
    panel(d, (740, 160, 1340, 360), "02", "If wrong", ["Pump can reverse.", "Do not start the fill", "and hope."])
    return save(im, "fig-phase.png")


def onemachine():
    return chips(
        "fig-one.png", "FIG 20   ONE MACHINE", "The others stay quiet enough that a fail has an owner.",
        [
            ("01", "CDU alone", "Start, stop, pumps."),
            ("02", "Air side alone", "If the claim includes it."),
            ("03", "Monitor", "Against a field instrument."),
            ("04", "Then heat", "Only if this stage passed."),
        ],
        "A SCREEN THAT AGREES WITH ANOTHER SCREEN IS NOT A PASS.",
        cols=4, row_h=150,
    )


def alarm():
    return chips(
        "fig-alarm.png", "FIG 21   ALARMS", "Three answers. The third is not a kindness.",
        [
            ("Y", "Pass", "You raised it.", "Local and monitor."),
            ("N", "Fail", "You raised it.", "It did not come."),
            ("ND", "Not shown", "The unit cannot raise it.", "Do not write pass."),
        ],
        "A SPREADSHEET ALARM IS NOT A FIELD TEST.",
        cols=3, row_h=170,
    )


def heatorder():
    im, d = new_canvas(1400, 440)
    header(d, "FIG 22   HEAT ORDER", "Separate signatures. The afternoon is not a quieter jurisdiction.")
    labels = ["NO-HEAT\nCURVE", "LADDER", "OVERLOAD\nIF CLAIMED", "PULL ONE\nUNIT", "STEP\nCHANGE", "STOP"]
    x = 48
    for i, lab in enumerate(labels):
        d.rectangle((x, 180, x + 200, 320), outline=BLUE, width=2)
        corners(d, (x, 180, x + 200, 320))
        yy = 210
        for line in lab.split("\n"):
            d.text((x + 16, yy), line, font=font(16, bold=True), fill=TEXT)
            yy += 28
        if i < len(labels) - 1:
            d.line((x + 200, 250, x + 216, 250), fill=CYAN, width=2)
        x += 220
    d.text((40, 370), "MORE HEAT, TO BE SURE, IS A NEW SCRIPT.", font=font(18, bold=True), fill=CYAN)
    return save(im, "fig-heat-order.png")


def axes(d, x0, y0, x1, y1):
    d.line((x0, y1, x1, y1), fill=DIM, width=2)
    d.line((x0, y0, x0, y1), fill=DIM, width=2)


def ladder():
    im, d = new_canvas(1400, 640)
    header(d, "FIG 23   LADDER", "Hold the rung. Do not jump to the top.")
    axes(d, 100, 160, 1280, 460)
    d.text((40, 280), "HEAT", font=font(14, bold=True), fill=DIM)
    steps = [(140, 400), (340, 400), (340, 340), (540, 340), (540, 280), (760, 280), (760, 210), (1040, 210)]
    d.line(steps, fill=CYAN, width=3)
    d.text((160, 480), "DWELL", font=font(16, bold=True), fill=CYAN)
    d.text((400, 480), "DWELL", font=font(16, bold=True), fill=CYAN)
    d.text((600, 480), "DWELL", font=font(16, bold=True), fill=CYAN)
    d.text((820, 480), "DWELL", font=font(16, bold=True), fill=CYAN)
    d.line((200, 390, 980, 200), fill=BLUE, width=2)
    d.text((420, 250), "NOT THIS JUMP", font=font(16, bold=True), fill=BLUE)
    d.text((40, 560), "NO SCALE. THE SCRIPT NAMES THE RUNG AND THE DWELL.", font=font(18, bold=True), fill=CYAN)
    return save(im, "fig-ladder.png")


def pump():
    im, d = new_canvas(1400, 640)
    header(d, "FIG 24   NO-HEAT CURVE", "Heat is zero. Automatic control is off. Or it is not this curve.")
    axes(d, 120, 150, 900, 500)
    d.text((40, 300), "dP", font=font(16, bold=True), fill=DIM)
    d.text((460, 520), "FLOW", font=font(16, bold=True), fill=DIM)
    pts = [(180, 420), (320, 360), (480, 300), (680, 230)]
    d.line(pts, fill=CYAN, width=3)
    for x, y in pts:
        d.ellipse((x - 8, y - 8, x + 8, y + 8), outline=CYAN, width=2)
    panel(d, (980, 180, 1340, 460), "OFF", "Prove it", ["Controller did not", "change the speed.", "Valve position", "is the script's.", "Four points or", "as many as named."])
    d.text((40, 575), "NO NUMBERS ON THIS FIGURE.", font=font(18, bold=True), fill=CYAN)
    return save(im, "fig-pump.png")


def stepchange():
    im, d = new_canvas(1400, 640)
    header(d, "FIG 25   STEP CHANGE", "Low, peak, high, valley, middle. Not the ladder.")
    axes(d, 100, 150, 1300, 460)
    d.text((36, 280), "TEMP", font=font(14, bold=True), fill=DIM)
    pts = [(140, 380), (300, 380), (360, 200), (560, 210), (620, 300), (820, 320), (900, 250), (1180, 250)]
    d.line(pts, fill=CYAN, width=3)
    tags = [(150, 400, "LOW"), (400, 160, "PEAK"), (560, 160, "HIGH"), (700, 340, "VALLEY"), (980, 200, "MIDDLE")]
    for x, y, lab in tags:
        d.text((x, y), lab, font=font(16, bold=True), fill=CYAN)
    d.text((40, 540), "ALARM OR NOT, AT THE HIGH AND AT THE MIDDLE. NO SCALE.", font=font(18, bold=True), fill=CYAN)
    return save(im, "fig-step.png")


def shutdown():
    im, d = new_canvas(1400, 520)
    header(d, "FIG 26   OUT", "This order. The reverse voids the sheet.")
    labels = ["UNLOAD", "BREAKER", "STOP", "THEN LIQUID", "BACKUP", "COUNT OUT"]
    x = 48
    for i, lab in enumerate(labels):
        color = CYAN if i in (0, 3) else BLUE
        d.rectangle((x, 190, x + 200, 300), outline=color, width=2)
        d.text((x + 16, 228), lab, font=font(16, bold=True), fill=TEXT)
        if i < len(labels) - 1:
            d.polygon([(x + 204, 238), (x + 218, 245), (x + 204, 252)], fill=CYAN)
        x += 222
    d.text((40, 380), "LIQUID OPEN BEFORE THE STOP  =  VOID.", font=font(20, bold=True), fill=CYAN)
    d.text((40, 424), "A COPY ON THE CRATE IS NOT A BACKUP.", font=font(18, bold=True), fill=TEXT)
    return save(im, "fig-shutdown.png")


def punch():
    im, d = new_canvas(1400, 480)
    header(d, "FIG 27   PUNCH", "An open fail blocks the next stage.")
    panel(d, (50, 160, 430, 360), "01", "Open", ["Not we will watch", "it during heat."])
    d.line((430, 260, 500, 260), fill=CYAN, width=3)
    panel(d, (500, 160, 880, 360), "02", "Waiver", ["What you will do", "if it appears."])
    d.line((880, 260, 950, 260), fill=CYAN, width=3)
    panel(d, (950, 160, 1340, 360), "03", "Close", ["Same evidence", "as the first test."])
    d.text((40, 410), "A RETEST NOT IN A SCRIPT REVISION IS AN UNAPPROVED TEST.", font=font(18, bold=True), fill=CYAN)
    return save(im, "fig-punch.png")


def pack():
    items = [
        ("01", "Sentence", "Proved, or not."),
        ("02", "Open items", "Page two."),
        ("03", "Level map", "Issued and refused."),
        ("04", "Scripts", "Ran, and did not."),
        ("05", "File judgment", "From the second book."),
        ("06", "Register", "Printed."),
        ("07", "Calibration", "In date on the day."),
        ("08", "Gear returned", "Against the unpack list."),
    ]
    return chips(
        "fig-pack.png", "FIG 28   THE PACK", "The short pack. Empty tabs are a false document.",
        items, "DO NOT SIGN THE FULL CERTIFICATE SET FOR A JOB YOU DID NOT RUN.", cols=4, row_h=130,
    )


def witness():
    return chips(
        "fig-witness.png", "FIG 29   THREE WAYS", "Say which one. A reader should not have to call you.",
        [
            ("01", "Witnessed", "You were there."),
            ("02", "Accepted", "A record you opened.", "Name, date, section."),
            ("03", "Not done", "Scope letter.", "Not an empty tab."),
        ],
        "A FOLDER YOU DID NOT OPEN IS NOT A WITNESS.",
        cols=3, row_h=170,
    )


def sheets():
    items = [
        ("01", "Before connect", "Lockout, vent, volume."),
        ("02", "Alarms", "Or not demonstrated."),
        ("03", "One heat step", "Copy per rung."),
        ("04", "Failures", "Each signed alone."),
        ("05", "Shutdown", "Order ticked."),
        ("06", "No-heat curve", "Or N/A in writing."),
        ("07", "CDU logic", "Vendor page, or not shown."),
    ]
    return chips(
        "fig-sheets.png", "FIG 30   SHEETS", "Seven sheets. A paragraph is not a substitute.",
        items, "FILL THEM. DO NOT SUMMARIZE THEM AWAY.", cols=4, row_h=130,
    )


def twoperson():
    return chips(
        "fig-two.png", "FIG 31   ON THE TOOLS", "Two people. One clock.",
        [
            ("01", "Measures", "Instrument in hand."),
            ("02", "Writes", "The empty cell, now."),
            ("03", "Commands", "One name, heat only."),
        ],
        "A SHEET FILLED THAT NIGHT FROM MEMORY IS A DIFFERENT TEST.",
        cols=3, row_h=150,
    )


if __name__ == "__main__":
    for fn in (
        three, claim, twelve, levels, parties, hands, command, month, survey, blank,
        scriptset, static, phase, onemachine, alarm, heatorder, ladder, pump, stepchange,
        shutdown, punch, pack, witness, sheets, twoperson,
    ):
        print(fn())
