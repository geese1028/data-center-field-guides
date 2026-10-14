#!/usr/bin/env python3
import html
import re
import zipfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path("/Users/geese/Downloads/book/books/02-read-load-bank-data")
CHAP = ROOT / "chapters"
FIG = ROOT / "figures"
OUT = ROOT / "epub" / "read-and-use-load-bank-data.epub"
FONT_DIR = Path("/Users/geese/Downloads/book/books/01-liquid-load-bank/fonts")

BG = (30, 30, 30)
BLUE = (0, 102, 255)
CYAN = (0, 255, 255)
GRID = (42, 42, 42)
TEXT = (255, 255, 255)


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


def save(im, name):
    FIG.mkdir(parents=True, exist_ok=True)
    path = FIG / name
    im.save(path, "PNG")
    return path


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


def draw_cover():
    im, d = new_canvas(1600, 2560)
    d.rectangle((70, 160, 90, 2200), fill=CYAN)
    d.text((140, 180), "02  /  FIELD GUIDE", font=font(28, bold=True), fill=CYAN)
    d.text((140, 240), "FLASH REPORT", font=font(26, bold=True), fill=BLUE)
    y = 420
    display = font(72, bold=True)
    for line in wrap(d, "READ AND USE LOAD BANK DATA", display, 1280):
        d.text((140, y), line, font=display, fill=TEXT)
        y += 100
    d.line((140, y + 40, 900, y + 40), fill=CYAN, width=2)
    d.text((140, y + 70), "FIVE PASSES.  ONE SENTENCE.", font=font(28), fill=TEXT)
    d.text((140, y + 120), "A HIT IS A TIME, NOT A PASS.", font=font(28), fill=TEXT)
    panel(d, (140, 1680, 1460, 2140), "RPT", "What the file must show", [
        "PRETEST  GRADIENT  OVERLOAD  STEP  FEED",
        "LIVE SAMPLES.  STALE IS NOT STEADY.",
        "CITE THE LIMIT.  DO NOT PASTE IT.",
    ])
    d.text((140, 2300), "TRISTAN", font=font(34, bold=True), fill=CYAN)
    d.text((140, 2360), "DATA CENTER FIELD GUIDES // ED. 2026", font=font(26, bold=True), fill=TEXT)
    FIG.mkdir(parents=True, exist_ok=True)
    png = FIG / "cover.png"
    jpg = FIG / "cover.jpg"
    im.save(png, "PNG")
    im.convert("RGB").save(jpg, "JPEG", quality=95, optimize=True)
    return png


# prefix, heading, filename, caption, kicker, title, rows, footer
FIGS = [
    ("00-", "How to read it", "fig-shape.png", "Figure 1. The flash report is the object. The curve is not.",
     "SHAPE", "Three books, three jobs", [[
        ("01", "Build", "Accept the prototype"),
        ("02", "This book", "Judge the file"),
        ("03", "One test", "Seven sheets, then leave"),
     ]], None),
    ("01-", "Why five", "fig-01-flash-report-structure.png", "Figure 01. Flash Report Architecture: The One-Page Audit Format, 5 Mandatory Passes, and Authority Sign-Off.",
     "PASSES", "Five lines, then the overall", [[
        ("01", "Pretest", "Fit to test"),
        ("02", "Gradient", "Steps recognizable"),
        ("03", "Overload", "A visit, then leave"),
     ], [
        ("04", "Step", "Jump, then dwell"),
        ("05", "One feed", "Each path named"),
     ]], "NOT RUN IS NOT A PASS."),
    ("02-", "Four lines", "fig-prep.png", "Figure 3. A failed preparation is not a mild gradient.",
     "PREP", "Before heat counts", [[
        ("01", "Filled", "All units"),
        ("02", "Powered", "The feed on the sheet"),
        ("03", "Self-check", "Every unit"),
        ("04", "No load", "Long enough to show a dead sensor"),
     ]], None),
    ("03-", "Liquid", "fig-pretest.png", "Figure 4. The number stays on the cited sheet.",
     "PRETEST", "Three cells, or the gradient does not count", [[
        ("01", "Flow", "Per unit"),
        ("02", "Temperature", "Every sensor in the sentence"),
        ("03", "Pressure", "The difference you named"),
     ]], None),
    ("04-", "Single Feed", "fig-07-single-feed-transient.png", "Figure 07. 2N Single-Feed Loss Transient: Electromechanical Contactor Clearing (<20ms) and Control Bus Immunity.",
     "SCENES", "Four functions after the pretest", [[
        ("01", "Steps", "Hold, do not wander"),
        ("02", "Overload", "Enter and leave"),
        ("03", "Jump", "Command first"),
        ("04", "One feed", "Each path is the failed one"),
     ]], None),
    ("05-", "Where the CV", "fig-03-multicabinet-uniformity.png", "Figure 03. Multi-Cabinet Hydraulic & Thermal Uniformity: Manifold Distribution and Coefficient of Variation (CV) Thresholds.",
     "CV", "Agreement with itself", [[
        ("01", "Electrical", "Tighter band"),
        ("02", "Liquid", "Written before the run"),
        ("03", "Air", "Only if air is in the claim"),
     ]], "A DEAD GROUP CAN SCORE ZERO."),
    ("06-", "Raw acquisition", "fig-04-sampling-and-stale-data.png", "Figure 04. Metrology Sampling: 1-Second Turbulent Jitter vs. 60-Second Mean and Buffer-Freeze Flatline Detection.",
     "POINT", "Keep both", [[
        ("01", "Raw", "One second, or the sheet's rate"),
        ("02", "Mean", "Sixty live samples"),
        ("03", "Gap", "A failed read is not a point"),
     ]], None),
    ("07-", "Heading 1: Setpoints", "fig-06-heat-balance-reconciliation.png", "Figure 06. Thermodynamic Heat Balance Reconciliation: Electrical Power vs. Liquid Enthalpy vs. Air Heat.",
     "BLOCK", "The same block on every step", [[
        ("01", "Setpoint", "Written before the dwell"),
        ("02", "Electrical", "Paths, not one total"),
        ("03", "Liquid", "Manifold and unit"),
        ("04", "Air", "Or not applicable"),
     ]], None),
    ("08-", "External gear", "fig-gear.png", "Figure 9. A CDU fail is not automatically a load-bank fail.",
     "GEAR", "Separate lines", [[
        ("01", "CDU", "Pass, fail, or not applicable"),
        ("02", "UPS", "Named before the run"),
        ("03", "Distribution", "Rise, if the claim needs it"),
        ("04", "Air handler", "Not a green lamp"),
     ]], None),
    ("09-", "Automatic", "fig-fields.png", "Figure 10. A script may fill a number. It may not write pass.",
     "FIELDS", "Two kinds of cell", [[
        ("01", "Script", "Times, means, CV"),
        ("02", "Person", "Pass, fail, not applicable"),
     ]], "A HUMAN PASS OVER A FAILED CELL IS AN EDIT."),
    ("10-", "Do not leave out", "fig-cut.png", "Figure 11. Short is allowed. A missing fail is not.",
     "CUT", "The formal report", [[
        ("01", "Keep", "Fails, cited limits, clocks"),
        ("02", "Drop", "Raw rows, site names, posters"),
     ]], None),
    ("11-", "Order", "fig-sentence.png", "Figure 12. The first paragraph is the claim or the refusal.",
     "SENTENCE", "Order of the page", [[
        ("01", "Sentence", "Or the refusal"),
        ("02", "Five lines", "Including not run"),
        ("03", "Failed cells", "Each with a time range"),
     ]], None),
    ("12-", "How a chart is built", "fig-charts.png", "Figure 13. Power plotted as cooling is a defect.",
     "CHARTS", "Two pictures, one window", [[
        ("01", "Window", "Chosen by a person"),
        ("02", "Overlay", "Who left the group"),
        ("03", "Per unit", "The scale cannot hide it"),
     ]], "TITLE THE QUANTITY. NOT THE REGISTER."),
    ("13-", "What a citation may do", "fig-cite.png", "Figure 14. A title may fill a cell. It may not become the cell.",
     "CITE", "Pointer, not a paste", [[
        ("01", "Title", "And revision"),
        ("02", "Date read", "The page will move"),
        ("03", "No table", "Not in this book"),
     ]], None),
    ("14-", "Hop 3: Modbus-TCP", "fig-02-telemetry-pipeline.png", "Figure 02. Telemetry Hop Architecture: Sensor Immersion to Modbus-TCP, Quality Bitmask, and MQTT Payloads.",
     "HOP", "Measure, poll, carry", [[
        ("01", "Sensor", "The place, not the name"),
        ("02", "Modbus", "Ask, or mark the miss"),
        ("03", "MQTT", "Carry. Do not measure."),
     ]], "RETAINED IS NOT A SAMPLE FROM THE DWELL."),
    ("15-", "Online versus offline", "fig-05-changepoint-detection.png", "Figure 05. Changepoint Detection Waveforms: Online Focus/FLOC Candidate Triggers vs. Offline CPOP Piecewise Slopes.",
     "WHEN", "Two times to speak", [[
        ("01", "FLOC", "During the window"),
        ("02", "Focus", "One channel, one threshold"),
        ("03", "CPOP", "After the export stops"),
     ]], None),
    ("16-", "Before any case", "fig-hit.png", "Figure 17. A hit is a time. The command log is the neighbor.",
     "HIT", "Three words, written first", [[
        ("01", "Expected", "The step you commanded"),
        ("02", "Inspect", "Split the hold"),
        ("03", "No change", "The pass line stands"),
     ]], "DO NOT AVERAGE TWO HIT TIMES."),
]


def draw_all():
    draw_cover()
    for row in FIGS:
        _, _, filename, _, kicker, title, rows, footer = row
        if filename.startswith("fig-0"):
            continue
        label = int(row[3].split(".")[0].replace("Figure ", ""))
        draw_board(filename, label, kicker, title, rows, footer)
    try:
        import generate_engineering_diagrams
        generate_engineering_diagrams.fig_01_flash_report()
        generate_engineering_diagrams.fig_02_telemetry_pipeline()
        generate_engineering_diagrams.fig_03_multicabinet_uniformity()
        generate_engineering_diagrams.fig_04_sampling_and_stale()
        generate_engineering_diagrams.fig_05_changepoint()
        generate_engineering_diagrams.fig_06_heat_balance()
        generate_engineering_diagrams.fig_07_single_feed_transient()
    except Exception as exc:
        print(f"Notice: generate_engineering_diagrams: {exc}")


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


def fig_html(src, caption):
    return (
        f'<figure><img src="images/{src}" alt="{html.escape(caption)}"/>'
        f"<figcaption>{html.escape(caption)}</figcaption></figure>"
    )


def inline_format(text):
    safe = html.escape(text)
    safe = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", safe)
    safe = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", safe)
    safe = re.sub(r"`([^`]+)`", r"<code>\1</code>", safe)
    safe = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', safe)
    return safe


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
            items = "".join(f"<li>{inline_format(item)}</li>" for item in data)
            parts.append(f"<ul>{items}</ul>")
            continue
        elif kind == "table":
            rows = []
            for i, cells in enumerate(data):
                tag = "th" if i == 0 else "td"
                cells_html = "".join(f"<{tag}>{inline_format(c)}</{tag}>" for c in cells)
                rows.append(f"<tr>{cells_html}</tr>")
            parts.append(f"<table><tbody>{''.join(rows)}</tbody></table>")
            continue
        else:
            continue

        for key, fig in figures.items():
            if fig and key in check_text and key not in inserted:
                parts.append(fig)
                inserted.add(key)
    return "\n".join(parts)


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
blockquote { border-left: 3px solid #0066ff; margin: 1em 0; padding-left: 1em; color: #444; }
pre { background: #f4f4f4; padding: 0.8em; overflow-x: auto; font-size: 0.88em; border-radius: 4px; }
code { font-family: monospace; }
table { width: 100%; border-collapse: collapse; margin: 1.2em 0; font-size: 0.9em; }
th, td { border: 1px solid #cbd5e1; padding: 8px 12px; text-align: left; }
th { background-color: #f1f5f9; font-weight: bold; color: #0f172a; }
"""


def main():
    draw_all()
    images = {p.name: p for p in sorted(FIG.glob("*.png"))}
    chapters = sorted(CHAP.glob("*.md"))
    items = []
    for path in chapters:
        blocks = md_to_blocks(path.read_text(encoding="utf-8"))
        title = next((t for k, t in blocks if k == "h1"), path.stem)
        figures = {}
        for prefix, heading, src, caption, *_rest in FIGS:
            if path.name.startswith(prefix):
                figures[heading] = fig_html(src, caption)
        body = blocks_to_xhtml(blocks, figures)
        items.append((f"chap-{len(items)+1:02d}.xhtml", title, body))

    nav_items = '<li><a href="copyright.xhtml">Copyright</a></li>\n' + "\n".join(
        f'<li><a href="{name}">{html.escape(title)}</a></li>' for name, title, _ in items
    )
    nav = xhtml("Contents", f'<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>{nav_items}</ol></nav>')
    colophon = xhtml(
        "Copyright",
        """<section epub:type="copyright-page">
<h1>Copyright</h1>
<p><em>Read and Use Load Bank Data</em></p>
<p>Tristan. Data Center Field Guides. First edition, 2026.</p>
<p>Copyright 2026. All rights reserved.</p>
<p>A reader may copy the headings of the flash report into their own sheet. A reader may not paste a sentence from this book into a vendor manual and call it a specification.</p>
<p>This book is a field guide. It is not a vendor specification or a site procedure. Limits belong to the document then in force, cited by title and revision.</p>
<p>The text and the figures in this edition are AI-generated.</p>
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
        manifest.append(f'<item id="c{i}" href="{name}" media-type="application/xhtml+xml"/>')
        spine.append(f'<itemref idref="c{i}"/>')
    opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="uid" version="3.0" xml:lang="en">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="uid">urn:uuid:book-02-read-load-bank-data</dc:identifier>
<dc:title>Read and Use Load Bank Data</dc:title>
<dc:language>en</dc:language>
<dc:creator>Tristan</dc:creator>
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
