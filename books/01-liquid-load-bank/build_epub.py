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


def inline_format(text):
    safe = html.escape(text)
    safe = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", safe)
    safe = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", safe)
    safe = re.sub(r"`([^`]+)`", r"<code>\1</code>", safe)
    safe = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', safe)
    return safe


def md_to_blocks(text):
    lines = text.replace("\r\n", "\n").split("\n")
    blocks = []
    buf = []
    list_buf = []
    table = []
    code_buf = []
    in_code = False

    def flush_p():
        if buf:
            blocks.append(("p", " ".join(buf).strip()))
            buf.clear()

    def flush_list():
        if list_buf:
            blocks.append(("ul", list(list_buf)))
            list_buf.clear()

    def flush_table():
        if table:
            rows = []
            for raw in table:
                cells = [c.strip() for c in raw.strip().strip("|").split("|")]
                if cells and not all(set(c) <= set("-: ") for c in cells):
                    rows.append(cells)
            if rows:
                blocks.append(("table", rows))
            table.clear()

    def flush_code():
        if code_buf:
            blocks.append(("pre", "\n".join(code_buf)))
            code_buf.clear()

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("```"):
            flush_p()
            flush_list()
            flush_table()
            if in_code:
                flush_code()
                in_code = False
            else:
                in_code = True
            continue

        if in_code:
            code_buf.append(line)
            continue

        if stripped.startswith("|") and stripped.endswith("|"):
            flush_p()
            flush_list()
            table.append(stripped)
            continue
        else:
            flush_table()

        if stripped.startswith("# "):
            flush_p()
            flush_list()
            blocks.append(("h1", stripped[2:].strip()))
        elif stripped.startswith("## "):
            flush_p()
            flush_list()
            blocks.append(("h2", stripped[3:].strip()))
        elif stripped.startswith("### "):
            flush_p()
            flush_list()
            blocks.append(("h3", stripped[4:].strip()))
        elif stripped.startswith("> "):
            flush_p()
            flush_list()
            blocks.append(("blockquote", stripped[2:].strip()))
        elif stripped.startswith("- ") or stripped.startswith("* "):
            flush_p()
            list_buf.append(stripped[2:].strip())
        elif re.match(r"^\d+\.\s+", stripped):
            flush_p()
            list_buf.append(re.sub(r"^\d+\.\s+", "", stripped))
        elif stripped == "" or stripped == "---":
            flush_p()
            flush_list()
        else:
            flush_list()
            buf.append(stripped)

    flush_p()
    flush_list()
    flush_table()
    flush_code()
    return blocks


def blocks_to_xhtml(blocks, figures):
    parts = []
    inserted = set()
    for kind, data in blocks:
        if kind == "h1":
            safe = inline_format(data)
            parts.append(f"<h1>{safe}</h1>")
            check_text = data
        elif kind == "h2":
            safe = inline_format(data)
            parts.append(f"<h2>{safe}</h2>")
            check_text = data
        elif kind == "h3":
            safe = inline_format(data)
            parts.append(f"<h3>{safe}</h3>")
            check_text = data
        elif kind == "p":
            parts.append(f"<p>{inline_format(data)}</p>")
            continue
        elif kind == "blockquote":
            parts.append(f"<blockquote><p>{inline_format(data)}</p></blockquote>")
            continue
        elif kind == "pre":
            parts.append(f"<pre><code>{html.escape(data)}</code></pre>")
            continue
        elif kind == "ul":
            lis = "".join(f"<li>{inline_format(x)}</li>" for x in data)
            parts.append(f"<ul>{lis}</ul>")
            continue
        elif kind == "table":
            header = data[0]
            rows = data[1:]
            th = "".join(f"<th>{inline_format(c)}</th>" for c in header)
            tr = "".join("<tr>" + "".join(f"<td>{inline_format(c)}</td>" for c in r) + "</tr>" for r in rows)
            parts.append(f"<table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>")
            continue
        else:
            continue

        for key, fig in figures.items():
            if fig and key in check_text and key not in inserted:
                parts.append(fig)
                inserted.add(key)
    return "\n".join(parts)


def fig_html(src, caption):
    return (
        f'<figure><img src="images/{src}" alt="{html.escape(caption)}"/>'
        f"<figcaption>{html.escape(caption)}</figcaption></figure>"
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


CSS = """
@font-face { font-family: "DejaVu Sans"; src: url("fonts/DejaVuSans.ttf"); }
@font-face { font-family: "DejaVu Sans"; src: url("fonts/DejaVuSans-Bold.ttf"); font-weight: bold; }
body { font-family: "DejaVu Sans", sans-serif; line-height: 1.45; margin: 1.2em 8%; color: #1e1e1e; }
h1 { font-family: "DejaVu Sans", sans-serif; font-weight: bold; font-size: 1.6em; line-height: 1.2; margin-top: 0; color: #0066ff; }
h2 { font-family: "DejaVu Sans", sans-serif; font-weight: bold; font-size: 1.15em; margin-top: 1.6em; color: #1e1e1e; }
h3 { font-family: "DejaVu Sans", sans-serif; font-weight: bold; font-size: 1.05em; margin-top: 1.3em; color: #1e293b; }
p { margin: 0.7em 0; }
figure { margin: 1.6em 0; page-break-inside: avoid; background: #ffffff; border: 1px solid #cbd5e1; border-radius: 6px; padding: 0.8em; text-align: center; }
img { width: 100%; max-width: 100%; height: auto; display: block; margin: 0 auto; }
figcaption { font-family: "DejaVu Sans", sans-serif; font-size: 0.9em; line-height: 1.4; margin-top: 0.6em; color: #0284c7; font-weight: bold; text-align: left; }
nav ol { line-height: 1.6; }
table { border-collapse: collapse; width: 100%; margin: 1.2em 0; font-size: 0.88em; }
th, td { border: 1px solid #cbd5e1; padding: 0.45em 0.65em; text-align: left; vertical-align: top; }
th { background: #0066ff; color: #ffffff; font-weight: bold; }
tr:nth-child(even) { background-color: #f8fafc; }
pre { background: #0f172a; color: #f8fafc; padding: 0.8em; border-radius: 4px; overflow-x: auto; }
code { font-family: monospace; font-size: 0.9em; }
blockquote { border-left: 4px solid #0066ff; margin: 1em 0; padding: 0.5em 1em; background: #eff6ff; }
ul, ol { margin: 0.6em 0 0.8em 1.4em; padding-left: 0; }
li { margin: 0.3em 0; }
"""


def draw_board(name, number, kicker, title, rows, footer=None):
    height = 150 + len(rows) * 200 + (40 if footer else 0)
    im, d = new_canvas(1400, height)
    header(d, f"FIG {number:02d}   {kicker}", title)
    y = 150
    for row in rows:
        chips(d, row, y, 160)
        y += 190
    if footer:
        d.text((40, height - 50), footer, font=font(20, bold=True), fill=CYAN)
    return save(im, name)


# prefix, heading, filename, caption, kicker, title, rows, footer
EXTRA = [
    ("00-", "What this volume owns", "fig-scope.png", "Figure 14. This volume stops at the prototype.",
     "SCOPE", "Three books, three jobs", [[
        ("01", "This book", "Specify and accept"),
        ("02", "Data book", "Read the export"),
        ("03", "Project book", "Run one hall test"),
     ]], None),
    ("00-", "Two documents, not ten", "fig-two-docs.png", "Figure 15. Extra documents wait until these two can leave the room.",
     "DOCUMENTS", "The only two that matter first", [[
        ("01", "Requirements", "What must be true"),
        ("02", "Acceptance", "How a fail looks"),
     ]], "A RENDERING IS NOT A THIRD DOCUMENT."),
    ("01-", "Three interface lines", "fig-interfaces.png", "Figure 16. Leave the part number blank until the citation fills it.",
     "INTERFACE", "Three lines on the same sheet", [[
        ("01", "Liquid", "Family, not a souvenir"),
        ("02", "Power", "Hall feed and unit need"),
        ("03", "Air companion", "Own line, or out"),
     ]], None),
    ("01-", "The evidence column", "fig-evidence.png", "Figure 17. A row without a do-not-ship cell is a wish.",
     "EVIDENCE", "Four cells, or it is not a requirement", [[
        ("01", "Statement", "A stranger can test it"),
        ("02", "Where", "Which side of the boundary"),
        ("03", "Evidence", "What the record shows"),
        ("04", "Do not ship", "The failure that stops it"),
     ]], None),
    ("02-", "Heat is not a nameplate", "fig-nameplate.png", "Figure 18. Closed contactors are not heat in the liquid.",
     "HEAT", "Two different quantities", [[
        ("01", "Electrical power", "What the feed delivered"),
        ("02", "Heat in liquid", "Flow times temperature rise"),
     ]], "JUDGE ONLY AFTER THE DWELL."),
    ("02-", "High flow as a design driver", "fig-high-flow.png", "Figure 19. High flow changes the machine, not just a setpoint.",
     "FLOW", "Three consequences", [[
        ("01", "Small rise", "Temperature alone can lie"),
        ("02", "Fittings dominate", "A gentle valve becomes a blockage"),
        ("03", "Branches split", "A header meter is not a module meter"),
     ]], None),
    ("02-", "What changes when the revision changes", "fig-revision.png", "Figure 20. A new PDF does not grow the pipe.",
     "REVISION", "Three honest answers", [[
        ("01", "Limitation", "Old window only"),
        ("02", "Modify", "Then re-accept the gates"),
        ("03", "Drop the claim", "Stop calling it a stand-in"),
     ]], None),
    ("03-", "Primary side and secondary side", "fig-loops.png", "Figure 21. Write your own glossary before you inherit theirs.",
     "LOOPS", "Do not average the two waters", [[
        ("01", "Building side", "Heat rejection"),
        ("02", "Exchanger", "The boundary"),
        ("03", "Rack side", "Where this unit sits"),
     ]], None),
    ("03-", "What fittings are for", "fig-fittings.png", "Figure 22. Pick the job. The citation names the family.",
     "FITTINGS", "Three jobs, no part numbers", [[
        ("01", "Quick disconnect", "Make and break"),
        ("02", "Clamped joint", "Inspect, do not snap daily"),
        ("03", "Valve", "Isolate or trim, not both unlabeled"),
     ]], None),
    ("03-", "Fill, vent, and the first liquid", "fig-fill.png", "Figure 23. A procedure that only works from memory is not in the file.",
     "FILL", "Sequence, not folklore", [[
        ("01", "Enter", "Named point"),
        ("02", "Vent", "High points open"),
        ("03", "Full", "No air in the heater branch"),
        ("04", "Look", "Then heat, not before"),
     ]], None),
    ("04-", "Steps are plateaus, not a knob", "fig-plateau.png", "Figure 24. A knob turn is not a dwell.",
     "PLATEAU", "A step has three times", [[
        ("01", "Start", "Command recorded"),
        ("02", "Hold", "Dwell on the sheet"),
        ("03", "End", "Heat story told or record-only"),
     ]], None),
    ("04-", "Sudden increase", "fig-sudden.png", "Figure 25. Hidden staging is a ramp. Call it a ramp.",
     "STEP", "Sudden is an order in the file", [[
        ("01", "Command", "Jumps first"),
        ("02", "Power", "Follows"),
        ("03", "Temperatures", "Move after, on one clock"),
     ]], None),
    ("04-", "Modules", "fig-modules.png", "Figure 26. A fault in one module does not become a fault in the loop.",
     "MODULES", "Two rules, not a brand", [[
        ("01", "Service", "Out without moving neighbors"),
        ("02", "Contain", "Fault stays local"),
        ("03", "Safe", "Loss of control removes heat"),
     ]], None),
    ("04-", "Failure modes worth writing down", "fig-failures.png", "Figure 27. Do not add power to explain a missing story.",
     "FAILURES", "Four stories that look like success", [[
        ("01", "Power, no rise", "Heat not in the liquid"),
        ("02", "Rise, flow falls", "Blockage or kink"),
        ("03", "One module hot", "Header cannot see it"),
        ("04", "Trip, no alarm", "The reason left with the test"),
     ]], None),
    ("05-", "Two sets, or you cannot compare", "fig-compare.png", "Figure 28. The unit can be right about itself and wrong about the manifold.",
     "COMPARE", "Two sets, one timeline", [[
        ("01", "Unit", "What the heaters see"),
        ("02", "Rack side", "What the hose delivers"),
        ("03", "Difference", "Expected, or a stop"),
     ]], None),
    ("05-", "Clock and interval", "fig-stale.png", "Figure 29. A fresh timestamp on an old value is a lie.",
     "TIME", "Missing is not the same as repeated", [[
        ("01", "Live", "New value, new time"),
        ("02", "Missing", "A gap you can see"),
        ("03", "Stale", "Last value painted forward"),
     ]], "STALE FAILS THE PLATEAU."),
    ("05-", "Alarms are sentences", "fig-alarms.png", "Figure 30. A single red lamp is a debate.",
     "ALARMS", "Each alarm has an action", [[
        ("01", "Overtemp", "Remove heat, latch"),
        ("02", "Low flow", "Remove heat"),
        ("03", "Sensor fault", "Do not keep the last setpoint"),
        ("04", "Valve", "Not in position"),
     ]], None),
    ("06-", "Overpressure", "fig-pressure.png", "Figure 31. The bench pump is often less polite than the CDU.",
     "PRESSURE", "Do not rely on a polite neighbor", [[
        ("01", "Source", "Highest pressure you will connect"),
        ("02", "Weakest part", "Hose, gauge, gasket, shell"),
        ("03", "Relief or sentence", "Where it goes, or a written ban"),
     ]], None),
    ("06-", "Leak", "fig-leak.png", "Figure 32. Heat off, then isolate. Not the other way around.",
     "LEAK", "Order matters", [[
        ("01", "Heat off", "First"),
        ("02", "Alarm local", "Network may be dead"),
        ("03", "Isolate", "If closing does not trap heat"),
     ]], None),
    ("06-", "Wrong valve", "fig-valve.png", "Figure 33. Every handle will be left where the last task needed it.",
     "VALVES", "Function in large text", [[
        ("01", "Label", "Return isolation, not V3"),
        ("02", "Line-up", "Recorded before heat"),
        ("03", "Spare swap", "Named person and a retest"),
     ]], None),
    ("07-", "Roles", "fig-roles.png", "Figure 34. The builder does not initial the stop line.",
     "ROLES", "Four names before the day", [[
        ("01", "Sheet owner", "Cannot edit a stop in the hall"),
        ("02", "Operator", "Commands the plateaus"),
        ("03", "Recorder", "Writes the boring passes"),
        ("04", "Stranger", "Was not in the build"),
     ]], None),
    ("07-", "Gate 1. Static and workmanship", "fig-gate1.png", "Figure 35. Compare the object to the sheet, not to a memory of the drawing.",
     "GATE 1", "Looks, not a narrative", [[
        ("01", "Reaches", "Hand on every valve"),
        ("02", "Hose", "Position of use, at pressure"),
        ("03", "Spare", "Matches the definition"),
        ("04", "Drip", "Does not enter the electrical section"),
     ]], None),
    ("07-", "Gate 2. Power and communications", "fig-gate2.png", "Figure 36. Load will not make a lying idle point honest.",
     "GATE 2", "Prove the lie before the heat", [[
        ("01", "Disconnect", "Remote heat does not start"),
        ("02", "Stale proof", "Disconnect a sensor on purpose"),
        ("03", "Power cycle", "Does not wake into heat"),
     ]], None),
    ("07-", "Gate 4. Overload", "fig-overload.png", "Figure 37. A visit is not a new rating.",
     "GATE 4", "Enter, look, leave", [[
        ("01", "Named level", "Written before the day"),
        ("02", "Person watching", "Not the person on the plot"),
        ("03", "Exit", "Then talk"),
     ]], None),
    ("07-", "After a fail", "fig-retest.png", "Figure 38. A small fix can kink the hose you just passed.",
     "RETEST", "Repeat the disturbed lines", [[
        ("01", "Fail", "One sentence of what was seen"),
        ("02", "Fix", "Not a pass"),
        ("03", "Repeat", "Every line the fix could touch"),
     ]], None),
    ("08-", "Known limitations", "fig-limits.png", "Figure 39. A limitation without a therefore is a worry.",
     "LIMITS", "The form that survives a meeting", [[
        ("01", "Does not", "The gap"),
        ("02", "Must not", "The use that gap forbids"),
        ("03", "Review date", "Or it becomes permanent by neglect"),
     ]], None),
    ("09-", "Kills", "fig-kills.png", "Figure 40. A false claim removed is finished engineering.",
     "KILLS", "Stop the claim. Do not decorate it.", [[
        ("01", "No citation", "Do not invent the interface"),
        ("02", "No heat story", "You may say the contactors closed"),
        ("03", "Stale as live", "The data claim dies"),
        ("04", "Stop asks the network", "Unattended heat ends"),
     ]], None),
    ("10-", "Header", "fig-sheet.png", "Figure 41. Status is written, unknown with a date, or cited.",
     "SHEET", "A header that plans to stay ignorant has no date", [[
        ("01", "Claim", "Represents and does not"),
        ("02", "Citation", "Title and revision"),
        ("03", "Unknown", "A date, or it is a blank forever"),
     ]], None),
    ("11-", "The bench is a piece of test equipment", "fig-bench.png", "Figure 42. A gentle bench accepts a smaller machine than the claim.",
     "BENCH", "Three minimums, or Gate 3 waits", [[
        ("01", "Absorb the heat", "Longest dwell"),
        ("02", "Deliver the flow", "Top of the band"),
        ("03", "Max pressure", "Versus the weakest wetted part"),
     ]], None),
    ("11-", "Second unit", "fig-second.png", "Figure 43. Twins are not the same unit until the gates say so.",
     "SECOND", "Reuse the sheet, not the initials", [[
        ("01", "Own record", "Own identity"),
        ("02", "Own image", "Software revision in the header"),
        ("03", "Own hose", "Routing is not inherited"),
     ]], None),
    ("13-", "The unit is the file plus the metal", "fig-change.png", "Figure 44. A hose swap is a different unit until the disturbed lines repeat.",
     "CHANGE", "Always a disturbance", [[
        ("01", "Hose or fitting", "Repeat reaches"),
        ("02", "Sensor", "Delete the old correction"),
        ("03", "Image", "Repeat the kill test"),
        ("04", "Coolant", "Materials row reopens"),
     ]], None),
    ("14-", "The day before", "fig-day.png", "Figure 45. Freeze the revision. The hallway does not get a pen.",
     "DAY", "Order of the day", [[
        ("01", "Freeze", "Sheet revision"),
        ("02", "Dry reaches", "Before liquid"),
        ("03", "Fill from the file", "Author silent"),
        ("04", "Heat last", "Export already running"),
     ]], None),
    ("15-", "The story has a direction", "fig-sign.png", "Figure 46. Do not take the absolute value of a reversed pair.",
     "SIGN", "Return hotter than supply, as the diagram defines those words", [[
        ("01", "Right sign", "Heat is in the stream"),
        ("02", "Wrong sign", "Hose or names are flipped"),
        ("03", "Absolute value", "Forbidden"),
     ]], None),
    ("16-", "First page", "fig-review.png", "Figure 47. Reconstructing the claim yourself will be kinder than the draft deserves.",
     "REVIEW", "Three blockers on page one", [[
        ("01", "Claim", "Stand-in, not a CDU"),
        ("02", "Citation", "Edition, or unknown"),
        ("03", "Limits", "Already started"),
     ]], None),
    ("17-", "Stopping", "fig-stop-claim.png", "Figure 48. Careful is not a cell.",
     "STOP", "A stop names a cell and a date", [[
        ("01", "Cell", "What is missing"),
        ("02", "Owner", "Who must fill it"),
        ("03", "Date", "Then drop the claim if it slips"),
     ]], None),
    ("19-", "What “public” does not mean", "fig-cite.png", "Figure 49. A page anyone can open is not a page anyone can copy.",
     "CITE", "Pointer, not a paste", [[
        ("01", "Title", "And edition"),
        ("02", "Date read", "The page will move"),
        ("03", "Cell", "What it may inform"),
        ("04", "No table", "Not in this book"),
     ]], None),
]


def draw_catalog():
    for row in EXTRA:
        _, _, filename, _, kicker, title, rows, footer = row
        number = int(filename.split("-")[0].replace("fig", "") or 0)
        # filename is fig-scope.png; number is in the kicker string via FIG label
        label = row[3].split(".")[0].replace("Figure ", "")
        draw_board(filename, int(label), kicker, title, rows, footer)


def main():
    FIG.mkdir(parents=True, exist_ok=True)
    for draw in (
        draw_cover, draw_boundary, draw_command, draw_gates, draw_functions,
        draw_duty, draw_ports, draw_authority, draw_safe, draw_exit, draw_stops,
        draw_steps, draw_file, draw_electrical, draw_catalog,
    ):
        draw()

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

    images = {p.name: p for p in sorted(FIG.glob("*.png"))}
    chapters = sorted(CHAP.glob("*.md"))
    items = []
    for i, path in enumerate(chapters, 1):
        blocks = md_to_blocks(path.read_text())
        title = next((t for k, t in blocks if k == "h1"), path.stem)
        placements = {
            "01-": [
                ("The six functions", "fig-functions.png", "Figure 4. Drop a function only by writing the reduction."),
                ("Air-cooled load", "fig-01-boundary-architecture.png", "Figure 01. Primary CDU Facility Loop vs. Secondary Rack-Side Load Bank Boundary & 80:20 Sensible Heat Split."),
            ],
            "02-": [
                ("The set, not the list", "fig-duty.png", "Figure 5. A missing quantity can imitate a healthy value of another."),
                ("The educational baseline sandbox", "fig-07-sandbox-calculation-model.png", "Figure 07. Educational Reference Sandbox: 120kW Virtual Rack Thermodynamic & Hydraulic Derivation Model."),
            ],
            "03-": [
                ("Isolation", "fig-ports.png", "Figure 6. Isolation, spare, and hose routing are acceptance items."),
                ("What fittings are for: Danfoss FD83", "fig-02-loadbank-pid.png", "Figure 02. Liquid Load Bank Piping & Instrumentation Diagram (P&ID) with Danfoss FD83 Couplings & 50μm Bypass Flushing Loop."),
            ],
            "04-": [
                ("Bypass, trim, and who is allowed to move flow", "fig-authority.png", "Figure 7. If A, B, and C are the same valve, say so."),
                ("Controls, only as far as heat requires", "fig-safe.png", "Figure 8. Command zero and kill control power are separate tests."),
            ],
            "05-": [
                ("Four duties of the exit", "fig-exit.png", "Figure 9. A platform that can show and cannot export has not finished."),
                ("The command path that already exists", "fig-command.png", "Figure 2. A script must be able to reach the load switch."),
                ("Placement: Core immersion metrology", "fig-03-sensor-installation.png", "Figure 03. Sensor Installation Metrology: Core Stream Immersion vs. Dead-Leg Stub Pitfalls."),
            ],
            "06-": [
                ("Overtemperature and the Class-1 hardwired", "fig-04-electrical-interlock-2n.png", "Figure 04. 2N Dual-Feeder Electrical Distribution & Class-1 Hardwired Emergency Trip Loop."),
                ("Electrical: 2N dual feeders", "fig-electrical.png", "Figure 13. The hall code and the unit standard are not the same citation."),
            ],
            "07-": [
                ("Accept the prototype", "fig-06-gate-statemachine.png", "Figure 06. Sequential Prototype Acceptance Gate State Machine & Hard Waiver Protocols."),
                ("Gate 3. Load steps", "fig-steps.png", "Figure 11. Sit on each step. The overload visit is not one of these sits."),
            ],
            "08-": [
                ("The file you must hand over", "fig-file.png", "Figure 12. Weight is not a file. These six items are."),
            ],
            "15-": [
                ("Four-quadrant time-series diagnostics", "fig-05-timeseries-diagnostics.png", "Figure 05. Four-Quadrant Time-Series Diagnostic Signatures: Valid Plateaus vs. Stale Data, Bypass Leak, and Water Hammer."),
            ],
        }
        for prefix, heading, filename, caption, *_rest in EXTRA:
            placements.setdefault(prefix, []).append((heading, filename, caption))
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
