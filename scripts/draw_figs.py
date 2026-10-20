#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FIG = Path("/Users/geese/Downloads/book/site/blog/figures")
FONT = Path("/Users/geese/Downloads/book/books/01-liquid-load-bank/fonts")
BG, BLUE, CYAN, GRID = (30, 30, 30), (0, 102, 255), (0, 255, 255), (42, 42, 42)
TEXT, DIM, RED = (255, 255, 255), (170, 170, 170), (255, 90, 90)
W, H = 1200, 680


def font(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(str(FONT / name), size)


def canvas():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    for x in range(0, W, 40):
        d.line((x, 0, x, H), fill=GRID)
    for y in range(0, H, 40):
        d.line((0, y, W, y), fill=GRID)
    d.rectangle((16, 16, W - 17, H - 17), outline=BLUE, width=2)
    return im, d


def header(d, kicker, title):
    d.text((36, 28), kicker, font=font(16, True), fill=CYAN)
    d.text((36, 54), title, font=font(28, True), fill=TEXT)


def box(d, xy, label, sub="", ok=True):
    color = CYAN if ok else RED
    d.rounded_rectangle(xy, radius=8, outline=color, width=2)
    x1, y1, x2, y2 = xy
    d.text((x1 + 16, y1 + 14), label, font=font(20, True), fill=TEXT)
    if sub:
        d.text((x1 + 16, y1 + 46), sub, font=font(16), fill=DIM)


def save(im, name):
    FIG.mkdir(parents=True, exist_ok=True)
    im.save(FIG / name, "PNG")


def not_a_cdu():
    im, d = canvas()
    header(d, "LOAD BANK", "Three jobs. Do not merge them.")
    box(d, (40, 160, 380, 520), "Load bank", "Heat and flow\nin place of the rack.")
    box(d, (420, 160, 760, 520), "CDU", "Supplies the loop.\nNot the load.")
    box(d, (800, 160, 1140, 520), "IT boot", "A different sentence.\nThe bank does not prove it.", ok=False)
    d.text((40, 560), "A slide multiple is not a flow. Cite the specification then in force, or leave the cell blank.", font=font(16), fill=DIM)
    save(im, "not-a-cdu.png")


def two_documents():
    im, d = canvas()
    header(d, "BEFORE METAL", "Two sheets. A drawing is not either of them.")
    box(d, (60, 160, 560, 500), "Requirements", "Duty. Faults. The sentence\nthe test may support.")
    box(d, (640, 160, 1140, 500), "Acceptance", "Gates. A forced gap.\nWhat a calm curve must not prove.")
    d.text((60, 540), "A gate invented after the first bad run is a caption.", font=font(18), fill=DIM)
    save(im, "two-documents.png")


def hit_time():
    im, d = canvas()
    header(d, "THE FILE", "A hit is a time. A pass is a sentence.")
    d.line((80, 360, 1100, 360), fill=DIM, width=2)
    d.line((200, 300, 200, 420), fill=CYAN, width=3)
    d.text((170, 440), "hit", font=font(18, True), fill=CYAN)
    d.text((80, 200), "value crossed a line", font=font(18), fill=TEXT)
    box(d, (620, 180, 1120, 500), "Pass, only if", "Clock. Dwell. Sign.\nHeat story. Scope.")
    save(im, "hit-time.png")


def gap():
    im, d = canvas()
    header(d, "A FAILED POLL", "Show the hole. Do not stamp a new time on the old value.")
    for i, x in enumerate(range(80, 520, 70)):
        d.ellipse((x, 300, x + 18, 318), fill=CYAN)
    d.line((560, 280, 640, 360), fill=RED, width=3)
    d.line((640, 280, 560, 360), fill=RED, width=3)
    d.text((540, 380), "gap", font=font(18, True), fill=RED)
    for x in range(700, 1100, 70):
        d.ellipse((x, 300, x + 18, 318), outline=DIM)
    d.text((80, 460), "Held-forward last value looks like a dwell. It is paint.", font=font(18), fill=DIM)
    save(im, "gap.png")


def two_clocks():
    im, d = canvas()
    header(d, "ONE DECISION, ONE CLOCK", "Do not average them.")
    box(d, (60, 180, 520, 480), "Measurement time", "When it happened.\nDwell and heat step use this.")
    box(d, (680, 180, 1140, 480), "Arrival time", "When the store got it.\nA late packet is an old event.", ok=False)
    d.text((540, 300), "not", font=font(22, True), fill=RED)
    save(im, "two-clocks.png")


def levels():
    im, d = canvas()
    header(d, "TWO MAPS", "Certificate Level 1 is factory. A static day is not.")
    rows = [
        ("0", "Design, concluded"),
        ("1", "Factory testing"),
        ("2", "Delivery, install, pre-start"),
        ("3", "Pre-functional, start-up"),
        ("4", "One system, functional"),
        ("5", "Heat window, integrated"),
        ("6", "Close-out, not the heat report"),
    ]
    y = 130
    for n, label in rows:
        color = RED if n == "1" else CYAN
        d.rounded_rectangle((50, y, 110, y + 58), radius=6, outline=color, width=2)
        d.text((68, y + 14), n, font=font(20, True), fill=color)
        d.text((140, y + 14), label, font=font(20), fill=TEXT)
        y += 70
    box(d, (760, 200, 1140, 460), "Local dialect", "Calling static checks\nLevel 1 does not make\nthem factory.", ok=False)
    save(im, "levels.png")


def inlet():
    im, d = canvas()
    header(d, "WHERE THE POINT SITS", "A room average is not a cabinet inlet.")
    d.rectangle((80, 200, 520, 520), outline=DIM, width=2)
    d.text((100, 220), "room average", font=font(18), fill=DIM)
    d.rectangle((620, 240, 1080, 480), outline=CYAN, width=3)
    d.text((650, 280), "inlet a person can walk to", font=font(22, True), fill=TEXT)
    d.text((650, 340), "Walked reading wins\nuntil the other point is corrected.", font=font(18), fill=DIM)
    save(im, "inlet.png")


def picture():
    im, d = canvas()
    header(d, "A REPORT", "Picture, or measurement. Not both by default.")
    box(d, (50, 180, 560, 520), "Picture", "Colors. No walked points.\nFile it. Do not sign airflow proved.", ok=False)
    box(d, (640, 180, 1140, 520), "Measurement", "Place. Instrument. Time.\nThe sentence it may support.")
    save(im, "picture.png")


def papers():
    im, d = canvas()
    header(d, "THREE PAPERS", "Do not invent a fourth name.")
    box(d, (40, 170, 380, 470), "SOP", "The same job, every time.\nA stop. A person. A record.")
    box(d, (410, 170, 790, 470), "MOP", "One change. Approved\nbefore the tools.")
    box(d, (820, 170, 1160, 470), "EOP", "Stop. Call. First safe state.\nThen a method, not a repair novel.")
    d.text((40, 520), "A permit names this work, this time, these people. It is not a fourth procedure.", font=font(18), fill=DIM)
    save(im, "papers.png")


def mop():
    im, d = canvas()
    header(d, "BEFORE THE TOOLS", "A method written during the job is a story.")
    items = ["What is isolated", "What still carries the load", "How you return", "How you back out", "Spare you will not start without"]
    y = 150
    for i, t in enumerate(items, 1):
        d.text((60, y), f"{i}  {t}", font=font(26), fill=TEXT if i < 5 else CYAN)
        y += 80
    save(im, "mop.png")


def incident():
    im, d = canvas()
    header(d, "FIRST HOUR", "Safe state, then stop. Cause is a hypothesis.")
    d.line((80, 300, 1100, 300), fill=DIM, width=2)
    for x, label in ((120, "knew"), (420, "safe"), (760, "called"), (1000, "told")):
        d.ellipse((x - 8, 292, x + 8, 308), fill=CYAN)
        d.text((x - 30, 330), label, font=font(18), fill=TEXT)
    d.text((80, 420), "Closing the icon is not closing the incident.", font=font(22), fill=RED)
    save(im, "incident.png")


def kw():
    im, d = canvas()
    header(d, "THREE NUMBERS", "Do not add them.")
    box(d, (40, 180, 360, 420), "Nameplate", "A label.", ok=False)
    box(d, (400, 180, 760, 420), "Design kW", "A drawing.", ok=False)
    box(d, (800, 180, 1140, 420), "Measured", "Live point, dated.\nOr the cell stays blank.")
    d.text((40, 480), "A whiteboard total is a new calculation. It does not get signed in the corridor.", font=font(18), fill=DIM)
    save(im, "kw.png")


def point():
    im, d = canvas()
    header(d, "BEFORE IT MAY SPEAK", "Value, time, source, quality. A name is not these.")
    for i, (label, sub) in enumerate((("Value", "unit, scaled once"), ("Time", "measurement, not arrival"), ("Source", "a path, not a brand"), ("Quality", "live, stale, or missing"))):
        x = 40 + i * 290
        box(d, (x, 200, x + 260, 460), label, sub)
    save(im, "point.png")


def stale():
    im, d = canvas()
    header(d, "GREEN IS NOT LIVE", "Stale may be shown. It may not close anything.")
    box(d, (50, 180, 360, 480), "Live", "Inside the interval.\nMay be compared to a line.")
    box(d, (420, 180, 760, 480), "Stale", "Old value, new paint.\nIncident stays open.", ok=False)
    box(d, (820, 180, 1140, 480), "Missing", "Not zero. Show the break.\nDo not connect the neighbors.", ok=False)
    save(im, "stale.png")


def score():
    im, d = canvas()
    header(d, "NO PEN", "A score may sort a queue. It may not close, pass, or notify.")
    box(d, (60, 200, 520, 500), "Allowed", "Sort. Show partial\nif an input is stale.")
    box(d, (640, 200, 1140, 500), "Forbidden", "Pass. Close. Customer notice.\nA quieter board after a weight change.", ok=False)
    save(im, "score.png")


def group():
    im, d = canvas()
    header(d, "A STORM", "Same window is not a cause.")
    box(d, (50, 180, 700, 500), "These arrived together", "Count. Sources. Times.\nThe row must open.")
    box(d, (760, 180, 1140, 500), "Caused", "Only with a named path.\nClock alone is not a path.", ok=False)
    save(im, "group.png")


def demo():
    im, d = canvas()
    header(d, "A DEMO ACCEPTS NOTHING ON YOURS", "Six shows. A slide is not a show.")
    items = ["Force a gap", "Two clocks", "Open the row", "Stale score refuses", "Window keeps the record", "Read the page aloud"]
    for i, t in enumerate(items):
        x = 50 + (i % 3) * 380
        y = 170 + (i // 3) * 200
        box(d, (x, y, x + 340, y + 150), t, "Shown, or not shown.")
    save(im, "demo.png")


def window():
    im, d = canvas()
    header(d, "A WINDOW", "Pages may stop. The record may not.")
    box(d, (50, 180, 560, 500), "Suppress", "Pages for the points named.\nStart, end, who may extend.")
    box(d, (640, 180, 1140, 500), "Keep", "Live, stale, missing.\nAlerts stored. A delete is a defect.", ok=False)
    save(im, "window.png")


def sentence():
    im, d = canvas()
    header(d, "THEIR PAGE", "Wider than the evidence. Strike, or do not sign.")
    box(d, (50, 180, 560, 500), "Their sentence", "Commissioned. Platform accepted.\nAir proved.", ok=False)
    box(d, (640, 180, 1140, 500), "Yours", "Scope. Date. Limit.\nSame document, or no yes.")
    save(im, "sentence.png")


def pages():
    im, d = canvas()
    header(d, "BEFORE THE PEN", "No sheet, no sentence.")
    labels = ["Proved sentence", "Level map", "File judgment", "Punch, printed", "Witness or document", "Operator pages"]
    for i, t in enumerate(labels):
        x = 40 + (i % 3) * 380
        y = 160 + (i // 3) * 200
        d.rounded_rectangle((x, y, x + 350, y + 150), radius=8, outline=CYAN, width=2)
        d.text((x + 20, y + 56), t, font=font(22, True), fill=TEXT)
    save(im, "pages.png")


def verbs():
    im, d = canvas()
    header(d, "THREE VERBS", "Substantially complete is not a fourth.")
    box(d, (40, 180, 380, 480), "Witnessed", "A person saw the step.")
    box(d, (410, 180, 790, 480), "Document", "A paper was filed.\nNot a changeover.")
    box(d, (820, 180, 1160, 480), "Not done", "Say so.\nDo not sample the hall.", ok=False)
    save(im, "verbs.png")


def metals():
    im, d = canvas()
    header(d, "BOTH METALS", "Calm copper does not clear silver.")
    box(d, (60, 180, 540, 500), "Copper", "One damage.\nNot the joints by itself.")
    box(d, (660, 180, 1140, 500), "Silver", "The joint metal.\nRead it, or do not claim the joints.")
    save(im, "metals.png")


def places():
    im, d = canvas()
    header(d, "ONE STRIP, ONE SENTENCE", "Discharge is not the room.")
    labels = [("Board face", True), ("Makeup before", True), ("Return", True), ("Unit discharge", False)]
    for i, (t, ok) in enumerate(labels):
        x = 40 + (i % 2) * 580
        y = 160 + (i // 2) * 220
        box(d, (x, y, x + 540, y + 180), t, "Supports the room." if ok else "Proves the unit outlet only.", ok=ok)
    save(im, "places.png")


def seal():
    im, d = canvas()
    header(d, "ORDER", "Close the holes you can see. Then buy. Then hang the after.")
    for i, t in enumerate(("Seal", "Treat makeup", "After coupon", "Loud season")):
        x = 50 + i * 280
        d.rounded_rectangle((x, 240, x + 240, 420), radius=8, outline=CYAN, width=2)
        d.text((x + 24, 300), str(i + 1), font=font(28, True), fill=CYAN)
        d.text((x + 24, 350), t, font=font(20, True), fill=TEXT)
    save(im, "seal.png")


def media():
    im, d = canvas()
    header(d, "A LINE ON A DRAWING", "Chemical filter is not a family.")
    box(d, (50, 180, 560, 520), "Ask", "Which family. Which fan.\nWhat spent means. Not a color.")
    box(d, (640, 180, 1140, 520), "Do not copy", "Recipe. Percentage. Bed depth.\nA catalog month.", ok=False)
    save(im, "media.png")


def blank_coupon():
    im, d = canvas()
    header(d, "TWO STRIPS", "The blank never sees the room.")
    box(d, (60, 180, 540, 500), "Sample", "Hung at the place.\nBagged there, at the end.")
    box(d, (660, 180, 1140, 500), "Blank", "Same lot. Sealed.\nBounds the trip. No blank, no fit class.")
    save(im, "blank-coupon.png")


def blank_u():
    im, d = canvas()
    header(d, "THE FACE", "An empty U is a bypass.")
    d.rectangle((80, 160, 420, 560), outline=CYAN, width=2)
    for y in (190, 270, 350, 430):
        d.rectangle((110, y, 390, y + 60), outline=DIM, width=2)
        d.text((140, y + 16), "blanked", font=font(16), fill=DIM)
    d.rectangle((110, 510, 390, 540), outline=RED, width=3)
    d.text((150, 512), "open U", font=font(16, True), fill=RED)
    d.text((480, 240), "Mostly blanked is not closed.", font=font(24), fill=TEXT)
    d.text((480, 300), "The open space is the path\nthe air will use.", font=font(20), fill=DIM)
    save(im, "blank-u.png")


def row_edges():
    im, d = canvas()
    header(d, "A ROW", "Top, sides, bottom. A product name closes none of them.")
    d.rectangle((200, 220, 1000, 520), outline=CYAN, width=3)
    d.text((520, 170), "top", font=font(20, True), fill=CYAN)
    d.text((80, 350), "side", font=font(20, True), fill=CYAN)
    d.text((1040, 350), "side", font=font(20, True), fill=CYAN)
    d.text((500, 560), "bottom, including cable cuts", font=font(20, True), fill=CYAN)
    save(im, "row-edges.png")


def floor():
    im, d = canvas()
    header(d, "UNDER THE TILE", "A missing tile is a supply leak. A ratio will not show it.")
    for i in range(8):
        x = 80 + (i % 4) * 140
        y = 180 + (i // 4) * 160
        outline = RED if i == 5 else DIM
        d.rectangle((x, y, x + 110, y + 120), outline=outline, width=3)
    d.text((700, 240), "Open tile", font=font(28, True), fill=RED)
    d.text((700, 300), "Cut larger than the cable.", font=font(20), fill=TEXT)
    d.text((700, 350), "List it. Do not recolor\na model that never had the hole.", font=font(20), fill=DIM)
    save(im, "floor.png")


if __name__ == "__main__":
    not_a_cdu()
    two_documents()
    hit_time()
    gap()
    two_clocks()
    levels()
    inlet()
    picture()
    papers()
    mop()
    incident()
    kw()
    point()
    stale()
    score()
    group()
    demo()
    window()
    sentence()
    pages()
    verbs()
    metals()
    places()
    seal()
    media()
    blank_coupon()
    blank_u()
    row_edges()
    floor()
    print("drew", len(list(FIG.glob('*.png'))))
