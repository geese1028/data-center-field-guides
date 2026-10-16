#!/usr/bin/env python3
import html
import math
import re
import zipfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path("/Users/geese/Downloads/book/books/01-liquid-load-bank")
CHAP = ROOT / "chapters"
FIG = ROOT / "figures"
OUT = ROOT / "epub" / "design-and-build-a-liquid-load-bank.epub"
BUILD = ROOT / "epub" / "build"

# Tech Innovation, theme-factory: #0066ff #00ffff #1e1e1e #ffffff, DejaVu Sans
BG = (30, 30, 30)
BLUE = (0, 102, 255)
CYAN = (0, 255, 255)
GRID = (42, 42, 42)
TEXT = (255, 255, 255)
MUTED = (190, 190, 190)
FONT_DIR = ROOT / "fonts"


def font(size, bold=False):
    path = FONT_DIR / ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf")
    return ImageFont.truetype(str(path), size)


def wrap(draw, text, fnt, width):
    lines = []
    for para in text.split("\n"):
        words = para.split()
        cur = ""
        for word in words:
            trial = word if not cur else cur + " " + word
            if draw.textlength(trial, font=fnt) <= width:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = word
        lines.append(cur)
    return lines


def new_canvas(w, h):
    im = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(im)
    for x in range(0, w, 40):
        d.line((x, 0, x, h), fill=GRID, width=1)
    for y in range(0, h, 40):
        d.line((0, y, w, y), fill=GRID, width=1)
    d.rectangle((18, 18, w - 19, h - 19), outline=BLUE, width=2)
    return im, d


def corners(d, xy, color=BLUE, arm=18):
    x0, y0, x1, y1 = xy
    for x, y, sx, sy in (
        (x0, y0, 1, 1),
        (x1, y0, -1, 1),
        (x0, y1, 1, -1),
        (x1, y1, -1, -1),
    ):
        d.line((x, y, x + sx * arm, y), fill=color, width=2)
        d.line((x, y, x, y + sy * arm), fill=color, width=2)


def panel(d, xy, index, title, lines):
    x0, y0, x1, y1 = xy
    d.rectangle(xy, outline=BLUE, width=2)
    corners(d, xy, CYAN)
    d.rectangle((x0, y0, x1, y0 + 36), fill=BLUE)
    d.text((x0 + 14, y0 + 8), index, font=font(16, bold=True), fill=CYAN)
    d.text((x0 + 64, y0 + 8), title.upper(), font=font(18, bold=True), fill=TEXT)
    y = y0 + 56
    for line in lines:
        d.text((x0 + 18, y), line, font=font(20), fill=TEXT)
        y += 32


def arrow(d, x0, y, x1):
    d.line((x0 + 6, y, x1 - 16, y), fill=CYAN, width=2)
    d.polygon([(x1, y), (x1 - 14, y - 7), (x1 - 14, y + 7)], fill=CYAN)
    d.ellipse((x0, y - 4, x0 + 8, y + 4), outline=CYAN, width=2)


def save(im, name):
    FIG.mkdir(parents=True, exist_ok=True)
    path = FIG / name
    im.save(path, "PNG")
    return path


def draw_cover():
    im, d = new_canvas(1600, 2560)
    d.rectangle((70, 160, 90, 2200), fill=CYAN)
    d.text((140, 180), "01  /  FIELD GUIDE", font=font(28, bold=True), fill=CYAN)
    d.text((140, 240), "LIQUID  LOOP  INTERFACE", font=font(26, bold=True), fill=BLUE)
    y = 420
    display = font(72, bold=True)
    for line in wrap(d, "DESIGN AND BUILD A LIQUID LOAD BANK", display, 1280):
        d.text((140, y), line, font=display, fill=TEXT)
        y += 100
    d.text((140, y + 20), "FOR NVL72-CLASS RACKS", font=font(52, bold=True), fill=CYAN)
    d.line((140, y + 130, 900, y + 130), fill=CYAN, width=2)
    d.text((140, y + 160), "SPECIFY THE STAND-IN.  ACCEPT THE PROTOTYPE.", font=font(26), fill=TEXT)
    d.text((140, y + 210), "DO NOT INVENT THE INTERFACE.", font=font(26), fill=TEXT)
    panel(d, (140, 1680, 1460, 2140), "SYS", "Rack-side stand-in", [
        "HEAT  +  FLOW  +  DIFFERENTIAL PRESSURE",
        "SCRIPT  ->  RACK COMMAND  ->  LOAD SWITCH",
        "FOUR GATES.  NO HEAT RUN ON A FAILED HOSE.",
    ])
    d.text((140, 2260), "TRISTAN", font=font(34, bold=True), fill=CYAN)
    d.text((140, 2320), "DATA CENTER FIELD GUIDES // ED. 2026", font=font(26, bold=True), fill=TEXT)
    FIG.mkdir(parents=True, exist_ok=True)
    png = FIG / "cover.png"
    jpg = FIG / "cover.jpg"
    im.save(png, "PNG")
    im.convert("RGB").save(jpg, "JPEG", quality=95, optimize=True)
    return png, jpg


def draw_boundary():
    im, d = new_canvas(1400, 760)
    d.text((40, 28), "FIG 01   BOUNDARY", font=font(22, bold=True), fill=CYAN)
    d.text((40, 62), "Where the load bank stops", font=font(34, bold=True), fill=TEXT)
    panel(d, (40, 160, 400, 560), "01", "Building side", ["Heat rejection", "Not this unit", "Do not size the hose", "from this loop"])
    panel(d, (500, 160, 900, 560), "02", "Heat exchanger", ["CDU boundary", "Two waters", "Do not average them"])
    panel(d, (1000, 160, 1360, 560), "03", "Rack side", ["Load bank sits here", "Heat and resistance", "instead of the IT"])
    arrow(d, 400, 360, 500)
    arrow(d, 900, 360, 1000)
    d.text((40, 640), "NAME THE SIDE BEFORE YOU NAME A FITTING.", font=font(22, bold=True), fill=CYAN)
    return save(im, "fig-boundary.png")


def draw_command():
    im, d = new_canvas(1400, 820)
    d.text((40, 24), "FIG 02   COMMAND PATH", font=font(22, bold=True), fill=CYAN)
    d.text((40, 58), "Script must reach the switch", font=font(34, bold=True), fill=TEXT)
    panel(d, (40, 130, 400, 320), "01", "Script", ["Test task", "Not a person clicking"])
    panel(d, (500, 130, 900, 320), "02", "Rack command", ["One instruction", "for the stand-in"])
    panel(d, (1000, 130, 1360, 320), "03", "Load bank", ["On, off, step", "Script must reach it"])
    arrow(d, 400, 225, 500)
    arrow(d, 900, 225, 1000)
    panel(d, (40, 400, 660, 740), "A", "Unit sensors", ["Supply / return temperature", "Supply / return pressure", "Flow", "Valve position, leak"])
    panel(d, (740, 400, 1360, 740), "B", "Rack-side sensors", ["Same five quantities", "Other side of the hose", "Without these, no comparison"])
    return save(im, "fig-command.png")


def draw_gates():
    im, d = new_canvas(1400, 1040)
    d.text((40, 24), "FIG 03   ACCEPTANCE", font=font(22, bold=True), fill=CYAN)
    d.text((40, 58), "Four gates, in order", font=font(34, bold=True), fill=TEXT)
    steps = [
        ("01", "Static", "Reaches, hose, spare, leak look"),
        ("02", "Power and data", "Points live, stale marked, local stop"),
        ("03", "Steps", "Quarter, half, three quarters, full, zero"),
        ("04", "Overload", "Named visit, then leave"),
    ]
    y = 140
    for index, name, detail in steps:
        panel(d, (160, y, 1240, y + 160), index, name, [detail])
        if index != "04":
            d.line((700, y + 160, 700, y + 196), fill=CYAN, width=2)
        y += 200
    d.text((40, 980), "A FAILED EARLIER GATE DOES NOT GET A HEAT RUN.", font=font(22, bold=True), fill=CYAN)
    return save(im, "fig-gates.png")


def header(d, kicker, title):
    d.text((40, 24), kicker, font=font(22, bold=True), fill=CYAN)
    d.text((40, 58), title, font=font(34, bold=True), fill=TEXT)


def chips(d, items, y, h=150):
    n = len(items)
    gap = 16
    left, right = 40, 1360
    w = (right - left - gap * (n - 1)) // n
    x = left
    for index, title, line in items:
        panel(d, (x, y, x + w, y + h), index, title, [line])
        x += w + gap


def draw_functions():
    im, d = new_canvas(1400, 620)
    header(d, "FIG 04   REQUIREMENT", "Six functions, or a written reduction")
    chips(d, [
        ("01", "Flow", "Adjustable and held"),
        ("02", "Temperatures", "Supply and return"),
        ("03", "Flow read", "On the loaded path"),
    ], 150, 170)
    chips(d, [
        ("04", "Pressure", "Both sides of the difference"),
        ("05", "Heat steps", "Sit, do not slam"),
        ("06", "Overtemp", "Stop and alarm"),
    ], 360, 170)
    return save(im, "fig-functions.png")


def draw_duty():
    im, d = new_canvas(1400, 720)
    header(d, "FIG 05   DUTY", "One set, not five wishes")
    panel(d, (500, 250, 900, 470), "SET", "Operating point", ["Missing one", "imitates the others"])
    satellites = [
        (40, 150, "Heat"),
        (1040, 150, "Flow"),
        (40, 500, "Diff. pressure"),
        (1040, 500, "Temperatures"),
        (500, 540, "Elec. power"),
    ]
    for x, y, name in satellites:
        d.rectangle((x, y, x + 320, y + 70), outline=BLUE, width=2)
        d.text((x + 16, y + 20), name, font=font(22, bold=True), fill=TEXT)
    d.line((360, 185, 500, 300), fill=CYAN, width=2)
    d.line((1040, 185, 900, 300), fill=CYAN, width=2)
    d.line((360, 535, 500, 420), fill=CYAN, width=2)
    d.line((1040, 535, 900, 420), fill=CYAN, width=2)
    d.line((660, 540, 660, 470), fill=CYAN, width=2)
    return save(im, "fig-duty.png")


def draw_ports():
    im, d = new_canvas(1400, 560)
    header(d, "FIG 06   LIQUID PATH", "Three checks before the loop is full")
    chips(d, [
        ("01", "Isolation", "Visible open or closed"),
        ("02", "Spare", "Same duty, or not a spare"),
        ("03", "Hose", "Routed in position, at pressure"),
    ], 180, 240)
    return save(im, "fig-ports.png")


def draw_authority():
    im, d = new_canvas(1400, 560)
    header(d, "FIG 07   AUTHORITY", "Write who is allowed to move what")
    chips(d, [
        ("A", "Interface flow", "What the manifold sees"),
        ("B", "Heat-section flow", "What touches the heaters"),
        ("C", "Heat", "Commanded power"),
    ], 180, 240)
    return save(im, "fig-authority.png")


def draw_safe():
    im, d = new_canvas(1400, 560)
    header(d, "FIG 08   SAFE STATE", "Both tests end with heat off")
    panel(d, (40, 180, 620, 430), "01", "Command zero", ["Heat off", "Flow still readable if designed"])
    panel(d, (760, 180, 1360, 430), "02", "Kill control power", ["Heat off", "Not latched on"])
    d.text((40, 470), "IF KILLING CONTROL POWER TURNS HEAT ON, STOP.", font=font(22, bold=True), fill=CYAN)
    return save(im, "fig-safe.png")


def draw_exit():
    im, d = new_canvas(1400, 520)
    header(d, "FIG 09   DATA EXIT", "Four duties, in this order")
    chips(d, [
        ("01", "Collect", "No typing off a panel"),
        ("02", "Store", "Survives the run"),
        ("03", "Show", "Live, in the room"),
        ("04", "Export", "A file, not a photo"),
    ], 180, 220)
    return save(im, "fig-exit.png")


def draw_stops():
    im, d = new_canvas(1400, 700)
    header(d, "FIG 10   STOPS", "Five stops. A failed sensor removes heat.")
    chips(d, [
        ("01", "Overtemp", "Removes heat"),
        ("02", "Overpressure", "Not only the CDU"),
        ("03", "Leak", "Local, network dead"),
    ], 160, 180)
    chips(d, [
        ("04", "Electrical", "Earth tested, lockable"),
        ("05", "Wrong valve", "Labeled by function"),
    ], 400, 180)
    return save(im, "fig-stops.png")


def draw_steps():
    im, d = new_canvas(1400, 420)
    header(d, "FIG 11   STEPS", "Default shape when the sheet has no other citation")
    chips(d, [
        ("01", "1/4", "Sit"),
        ("02", "1/2", "Sit"),
        ("03", "3/4", "Sit"),
        ("04", "Full", "Sit"),
        ("05", "Zero", "Then a named overload"),
    ], 160, 160)
    return save(im, "fig-steps.png")


def draw_file():
    im, d = new_canvas(1400, 620)
    header(d, "FIG 12   DELIVERY", "The file a stranger can use")
    chips(d, [
        ("01", "Claim", "Represents / does not"),
        ("02", "Duty", "Cited, or unknown"),
        ("03", "Diagram", "One line, redrawable"),
    ], 160, 160)
    chips(d, [
        ("04", "Points", "Functions, not registers"),
        ("05", "Record", "Fails kept"),
        ("06", "Limits", "Does not, therefore must not"),
    ], 360, 160)
    return save(im, "fig-file.png")


def draw_electrical():
    im, d = new_canvas(1400, 560)
    header(d, "FIG 13   POWER", "Two codes, two sides of the plug")
    panel(d, (40, 180, 640, 450), "HALL", "Premises code", ["NFPA 70 or local IEC 60364", "Edition the hall adopted", "This book does not design it"])
    panel(d, (760, 180, 1360, 450), "UNIT", "Equipment standard", ["IEC 60204-1, edition cited", "Mark on the nameplate", "Lockable disconnect wins"])
    return save(im, "fig-electrical.png")


import sys
sys.path.insert(0, str(ROOT.parent))
from epub_renderer import (
    SHARED_CSS as CSS,
    blocks_to_xhtml,
    fig_html,
    inline_format,
    md_to_blocks,
)


def xhtml(title, body, css="styles.css"):
    return f"""<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="en" lang="en">
<head>
<meta charset="utf-8"/>
<title>{html.escape(title)}</title>
<link rel="stylesheet" type="text/css" href="{css}"/>
</head>
<body>
{body}
</body>
</html>
"""


EXTRA = []


def main():
    FIG.mkdir(parents=True, exist_ok=True)
    for old_png in FIG.glob("fig-*.png"):
        if not old_png.name.startswith("fig-0"):
            old_png.unlink()
    draw_cover()

    # Generate the 7 industrial engineering diagrams
    try:
        import generate_engineering_diagrams
        generate_engineering_diagrams.fig_01_boundary()
        generate_engineering_diagrams.fig_02_pid()
        generate_engineering_diagrams.fig_03_sensor_cutaway()
        generate_engineering_diagrams.fig_04_electrical()
        generate_engineering_diagrams.fig_05_timeseries()
        generate_engineering_diagrams.fig_06_state_machine()
        generate_engineering_diagrams.fig_07_sandbox_model()
    except Exception as exc:
        print(f"Notice: generate_engineering_diagrams: {exc}")

    images = {
        p.name: p
        for p in sorted(FIG.glob("*.png"))
        if p.name == "cover.png" or p.name.startswith("fig-0")
    }
    chapters = sorted(CHAP.glob("*.md"))
    items = []
    placements = {
        "01-": [
            ("Air-cooled load", "fig-01-boundary-architecture.png", "Figure 01. Primary CDU Facility Loop vs. Secondary Rack-Side Load Bank Boundary & 80:20 Sensible Heat Split."),
        ],
        "02-": [
            ("The educational baseline sandbox", "fig-07-sandbox-calculation-model.png", "Figure 07. Educational Reference Sandbox: 120 kW Virtual Rack Thermodynamic & Hydraulic Derivation Model."),
        ],
        "03-": [
            ("What fittings are for: Danfoss FD83", "fig-02-loadbank-pid.png", "Figure 02. Liquid Load Bank Piping & Instrumentation Diagram (P&ID) with Danfoss FD83 Couplings & 50 μm Bypass Flushing Loop."),
        ],
        "05-": [
            ("Placement: Core immersion metrology", "fig-03-sensor-installation.png", "Figure 03. Sensor Installation Metrology: Core Stream Immersion vs. Dead-Leg Stub Pitfalls."),
        ],
        "06-": [
            ("Overtemperature and the Class-1 hardwired", "fig-04-electrical-interlock-2n.png", "Figure 04. 2N Dual-Feeder Electrical Distribution & Class-1 Hardwired Emergency Trip Loop."),
        ],
        "07-": [
            ("Accept the prototype", "fig-06-gate-statemachine.png", "Figure 06. Sequential Prototype Acceptance Gate State Machine & Hard Waiver Protocols."),
        ],
        "15-": [
            ("Four-quadrant time-series diagnostics", "fig-05-timeseries-diagnostics.png", "Figure 05. Four-Quadrant Time-Series Diagnostic Signatures: Valid Plateaus vs. Stale Data, Bypass Leak, and Water Hammer."),
        ],
    }
    for i, path in enumerate(chapters, 1):
        blocks = md_to_blocks(path.read_text(encoding="utf-8"), path.parent)
        title = next((t for k, t in blocks if k == "h1"), path.stem)
        figures = {}
        for prefix, rows in placements.items():
            if path.name.startswith(prefix):
                for heading, src, caption in rows:
                    figures[heading] = fig_html(src, caption)
        body = blocks_to_xhtml(blocks, figures)
        fname = f"chap-{i:02d}.xhtml"
        items.append((fname, title, body))

    nav_items = "\n".join(
        f'<li><a href="{name}">{html.escape(title)}</a></li>' for name, title, _ in items
    )
    nav_items = '<li><a href="copyright.xhtml">Copyright</a></li>\n' + nav_items
    nav = xhtml("Contents", f"<nav epub:type=\"toc\" id=\"toc\"><h1>Contents</h1><ol>{nav_items}</ol></nav>")
    colophon = xhtml(
        "Copyright",
        """<section epub:type="copyright-page">
<h1>Copyright</h1>
<p><em>Design and Build a Liquid Load Bank for NVL72 Racks</em></p>
<p>tristan. Data Center Field Guides. First edition, 2026.</p>
<p>Copyright 2026. All rights reserved.</p>
<p>A reader may copy the headings of the requirements list, the four gate names, and the rule that a quantity without a false story is an ornament, into their own project sheet. A reader may not paste a sentence from this book into a vendor manual and call it a specification.</p>
<p>This book is a field guide. It is not a vendor specification, a fabrication package, or a site procedure. Interface numbers belong to the specification then in force, cited by title and revision. Titles of standards are named. Their text is not reproduced.</p>
<p>The text and the figures in this edition are AI-generated. No translation of this edition exists.</p>
<p>List price 12.99 USD. Not enrolled in an exclusive program.</p>
</section>""",
    )
    cover_doc = xhtml(
        "Cover",
        '<section epub:type="cover"><img src="images/cover.png" alt="Cover"/></section>',
    )

    manifest = [
        '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
        '<item id="css" href="styles.css" media-type="text/css"/>',
        '<item id="font-regular" href="fonts/DejaVuSans.ttf" media-type="font/ttf"/>',
        '<item id="font-bold" href="fonts/DejaVuSans-Bold.ttf" media-type="font/ttf"/>',
        '<item id="cover-img" href="images/cover.png" media-type="image/png" properties="cover-image"/>',
        '<item id="cover" href="cover.xhtml" media-type="application/xhtml+xml"/>',
        '<item id="copyright" href="copyright.xhtml" media-type="application/xhtml+xml"/>',
    ]
    for name in images:
        if name == "cover.png":
            continue
        manifest.append(
            f'<item id="{name.replace(".png", "")}" href="images/{name}" media-type="image/png"/>'
        )
    spine = ['<itemref idref="cover"/>', '<itemref idref="copyright"/>', '<itemref idref="nav"/>']
    for i, (name, title, _) in enumerate(items, 1):
        manifest.append(
            f'<item id="c{i}" href="{name}" media-type="application/xhtml+xml"/>'
        )
        spine.append(f'<itemref idref="c{i}"/>')

    opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="uid" version="3.0" xml:lang="en">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="uid">urn:uuid:book-01-liquid-load-bank</dc:identifier>
<dc:title>Design and Build a Liquid Load Bank for NVL72 Racks</dc:title>
<dc:language>en</dc:language>
<dc:creator>tristan</dc:creator>
<dc:rights>Copyright 2026. Text and figures are AI-generated.</dc:rights>
<meta property="dcterms:modified">2026-10-11T00:00:00Z</meta>
</metadata>
<manifest>
{chr(10).join(manifest)}
</manifest>
<spine>
{chr(10).join(spine)}
</spine>
</package>
"""
    container = """<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles>
<rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
</rootfiles>
</container>
"""
    if OUT.exists():
        OUT.unlink()
    OUT.parent.mkdir(parents=True, exist_ok=True)

    def add(zf, arc, data):
        zf.writestr(arc, data.encode("utf-8") if isinstance(data, str) else data)

    with zipfile.ZipFile(OUT, "w") as zf:
        info = zipfile.ZipInfo("mimetype")
        info.compress_type = zipfile.ZIP_STORED
        zf.writestr(info, "application/epub+zip")
        add(zf, "META-INF/container.xml", container)
        add(zf, "OEBPS/content.opf", opf)
        add(zf, "OEBPS/styles.css", CSS)
        add(zf, "OEBPS/nav.xhtml", nav)
        add(zf, "OEBPS/cover.xhtml", cover_doc)
        add(zf, "OEBPS/copyright.xhtml", colophon)
        for name, title, body in items:
            add(zf, f"OEBPS/{name}", xhtml(title, body))
        for arc, path in images.items():
            zf.write(path, f"OEBPS/images/{arc}")
        zf.write(FONT_DIR / "DejaVuSans.ttf", "OEBPS/fonts/DejaVuSans.ttf")
        zf.write(FONT_DIR / "DejaVuSans-Bold.ttf", "OEBPS/fonts/DejaVuSans-Bold.ttf")
    print(OUT, OUT.stat().st_size)


if __name__ == "__main__":
    main()
