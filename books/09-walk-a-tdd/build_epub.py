#!/usr/bin/env python3
"""
EPUB Builder for Book 09: Walk a TDD
Author: Tristan (Data Center Field Guides)
Compiles upgraded markdown chapters, modern typography, tables, and flagship figures into standard EPUB3.
"""

import html
import re
import zipfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path("/Users/geese/Downloads/book/books/09-walk-a-tdd")
CHAP = ROOT / "chapters"
SHEETS = ROOT / "sheets"
FIG = ROOT / "figures"
OUT = ROOT / "epub" / "walk-a-tdd.epub"
FONT_DIR = Path("/Users/geese/Downloads/book/books/01-liquid-load-bank/fonts")

TITLE = "Walk a TDD"
SUBTITLE = "Technical Due Diligence: What a lender or buyer may rely on"

BG = (10, 15, 29)          # Deep midnight navy
NAVY = (30, 58, 138)       # Institutional lender blue
GOLD = (217, 119, 6)       # Amber / gold financing accent
TEXT = (248, 250, 252)     # White text
MUTED = (148, 163, 184)    # Cool grey
GRID = (23, 37, 60)        # Dark corporate grid


def font(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    path = FONT_DIR / name
    if not path.exists():
        path = Path("/Library/Fonts/Arial Unicode.ttf")
    return ImageFont.truetype(str(path), size)


def wrap(draw, text, fnt, width):
    lines = []
    for para in text.split("\n"):
        cur = ""
        for word in para.split():
            trial = word if not cur else cur + " " + word
            if draw.textlength(trial, font=fnt) <= width:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = word
        if cur:
            lines.append(cur)
    return lines


def new_canvas(w, h):
    im = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(im)
    for x in range(0, w, 40):
        d.line([(x, 0), (x, h)], fill=GRID, width=1)
    for y in range(0, h, 40):
        d.line([(0, y), (w, y)], fill=GRID, width=1)
    d.rectangle((20, 20, w - 21, h - 21), outline=NAVY, width=3)
    d.rectangle((40, 40, w - 41, h - 41), outline=GOLD, width=1)
    return im, d


def draw_cover():
    w, h = 1600, 2400
    im, d = new_canvas(w, h)

    # Header category pill
    d.rectangle((100, 140, 1500, 260), fill=NAVY, outline=GOLD, width=2)
    d.text((140, 175), "DATA CENTER FIELD GUIDES // BOOK 09", font=font(34, True), fill=GOLD)
    d.text((1120, 175), "AUDIT // TDD", font=font(34, True), fill=TEXT)

    # Main Title Box
    d.rectangle((100, 320, 1500, 940), fill=(15, 23, 42), outline=GOLD, width=3)
    d.text((150, 370), "WALK A TDD", font=font(92, True), fill=TEXT)
    d.line([(150, 500), (1450, 500)], fill=GOLD, width=4)

    sub_lines = wrap(d, SUBTITLE, font(44), 1300)
    sy = 540
    for sl in sub_lines:
        d.text((150, sy), sl, font=font(44), fill=GOLD)
        sy += 65

    meta = "A Field Guide to Technical Due Diligence, Site Audits, Utility Substation Diversity, Hydrology, Structural Floor Loading, and Financing Opinions"
    my = sy + 30
    for ml in wrap(d, meta, font(28), 1300):
        d.text((150, my), ml, font=font(28), fill=MUTED)
        my += 44

    # Central Technical Architectural Callout Box
    d.rectangle((100, 1000, 1500, 1900), fill=(23, 37, 60), outline=NAVY, width=2)
    d.rectangle((100, 1000, 1500, 1100), fill=NAVY)
    d.text((140, 1030), "THE SIX CRITICAL PILLARS OF INDEPENDENT SITE AUDIT", font=font(32, True), fill=GOLD)

    pillars = [
        ("01 :: CIVIL & SITE", "FEMA 500-yr BFE (+1.0m FFL) // Rational Runoff Q=CIA // SDC D-F Bracing"),
        ("02 :: POWER & GRID", "True Transmission Diversity // No Shared Duct Banks // N-1 Feeder 100%"),
        ("03 :: FUEL & WATER", "72h Diesel Autonomy // Duplex Polishing ASTM D975 // 48h Evaporative Water"),
        ("04 :: STRUCTURAL", "18-25 kN/m2 AI Rack Load // CISCA 15kN Pedestal // PT Slab Radar Scan"),
        ("05 :: PERMITTING", "Unconditional Occupancy Certificate // Phase I/II ESA // Clean Easements"),
        ("06 :: GOVERNANCE", "Three-Tier Risk Matrix // CP Escrow (150-200%) // Refusal Covenant"),
    ]

    py = 1130
    for tag, desc in pillars:
        d.rectangle((140, py, 1460, py + 105), fill=(10, 15, 29), outline=GRID, width=1)
        d.text((170, py + 18), tag, font=font(26, True), fill=GOLD)
        d.text((170, py + 58), desc, font=font(22), fill=TEXT)
        py += 122

    # Footer Author Band
    d.rectangle((100, 1960, 1500, 2260), fill=NAVY, outline=GOLD, width=2)
    d.text((140, 2010), "AUTHOR: TRISTAN", font=font(40, True), fill=TEXT)
    d.text((140, 2075), "Data Center Field Guide Series // First Edition, 2026", font=font(26), fill=MUTED)
    d.text((140, 2125), "Independent Engineering Verification & Syndicated Debt Due Diligence", font=font(24), fill=GOLD)
    d.text((1050, 2075), "VERIFIED TDD", font=font(38, True), fill=GOLD)

    FIG.mkdir(parents=True, exist_ok=True)
    im.save(FIG / "cover.jpg", quality=95)
    print("Cover image saved to:", FIG / "cover.jpg")


def md_to_blocks(text, base):
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

    img_re = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
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
        elif img_re.search(stripped):
            flush_p()
            flush_list()
            m = img_re.search(stripped)
            alt = m.group(1)
            src = m.group(2)
            resolved = (base / src).resolve()
            blocks.append(("img", (alt, resolved)))
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


def inline_format(text):
    safe = html.escape(text)
    safe = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", safe)
    safe = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", safe)
    safe = re.sub(r"`([^`]+)`", r"<code>\1</code>", safe)
    safe = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', safe)
    return safe


def blocks_to_xhtml(blocks):
    parts = []
    figs = []
    for kind, data in blocks:
        if kind == "h1":
            parts.append(f"<h1>{html.escape(data)}</h1>")
        elif kind == "h2":
            parts.append(f"<h2>{html.escape(data)}</h2>")
        elif kind == "h3":
            parts.append(f"<h3>{html.escape(data)}</h3>")
        elif kind == "p":
            parts.append(f"<p>{inline_format(data)}</p>")
        elif kind == "blockquote":
            parts.append(f"<blockquote><p>{inline_format(data)}</p></blockquote>")
        elif kind == "pre":
            parts.append(f"<pre><code>{html.escape(data)}</code></pre>")
        elif kind == "ul":
            lis = "".join(f"<li>{inline_format(x)}</li>" for x in data)
            parts.append(f"<ul>{lis}</ul>")
        elif kind == "table":
            header = data[0]
            rows = data[1:]
            th = "".join(f"<th>{inline_format(c)}</th>" for c in header)
            tr = "".join("<tr>" + "".join(f"<td>{inline_format(c)}</td>" for c in r) + "</tr>" for r in rows)
            parts.append(f"<table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>")
        elif kind == "img":
            alt, path = data
            name = path.name
            figs.append((name, path))
            parts.append(
                f'<figure><img src="images/{html.escape(name)}" alt="{html.escape(alt)}"/>'
                f"<figcaption>{html.escape(alt)}</figcaption></figure>"
            )
    return "\n".join(parts), figs


def xhtml(title, body):
    return f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="en">
<head>
<title>{html.escape(title)}</title>
<meta charset="utf-8"/>
<link rel="stylesheet" type="text/css" href="styles.css"/>
</head>
<body>
{body}
</body>
</html>
"""


CSS = """
@font-face { font-family: "DejaVu Sans"; src: url("fonts/DejaVuSans.ttf"); }
@font-face { font-family: "DejaVu Sans"; src: url("fonts/DejaVuSans-Bold.ttf"); font-weight: bold; }

body {
    font-family: "DejaVu Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    line-height: 1.55;
    margin: 1.4em 8%;
    color: #1e293b;
    background-color: #ffffff;
}

h1 {
    font-family: "DejaVu Sans", sans-serif;
    font-weight: bold;
    font-size: 1.65em;
    line-height: 1.25;
    margin-top: 1.2em;
    margin-bottom: 0.6em;
    color: #1e3a8a;
    border-bottom: 2px solid #dbeafe;
    padding-bottom: 0.25em;
}

h2 {
    font-family: "DejaVu Sans", sans-serif;
    font-weight: bold;
    font-size: 1.25em;
    margin-top: 1.6em;
    margin-bottom: 0.5em;
    color: #0f172a;
    border-bottom: 1px solid #f1f5f9;
    padding-bottom: 0.2em;
}

h3 {
    font-family: "DejaVu Sans", sans-serif;
    font-weight: bold;
    font-size: 1.05em;
    margin-top: 1.2em;
    margin-bottom: 0.4em;
    color: #d97706;
}

p {
    margin: 0.75em 0;
    text-align: justify;
}

ul {
    margin: 0.6em 0 0.8em 1.4em;
    padding-left: 0;
}

li {
    margin: 0.35em 0;
}

blockquote {
    margin: 1em 0;
    padding: 0.6em 1.2em;
    background-color: #eff6ff;
    border-left: 4px solid #1e3a8a;
    color: #1e40af;
    font-style: italic;
}

pre {
    background-color: #0a0f1d;
    color: #f8fafc;
    padding: 0.8em 1em;
    border-radius: 4px;
    overflow-x: auto;
    font-size: 0.85em;
    line-height: 1.4;
    margin: 1em 0;
}

code {
    font-family: "Courier New", Courier, monospace;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin: 1.2em 0;
    font-size: 0.88em;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}

th, td {
    border: 1px solid #cbd5e1;
    padding: 0.45em 0.65em;
    vertical-align: top;
    text-align: left;
}

th {
    background: #1e3a8a;
    color: #ffffff;
    font-weight: bold;
}

tr:nth-child(even) {
    background-color: #f8fafc;
}

figure {
    margin: 1.8em 0;
    page-break-inside: avoid;
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    padding: 0.5em;
    text-align: center;
}

img {
    width: 100%;
    height: auto;
    border-radius: 2px;
}

figcaption {
    font-family: "DejaVu Sans", sans-serif;
    font-size: 0.85em;
    font-weight: bold;
    margin-top: 0.6em;
    color: #1e3a8a;
}

nav ol {
    line-height: 1.6;
    padding-left: 1.5em;
}

nav li {
    margin: 0.4em 0;
}

nav a {
    text-decoration: none;
    color: #1e3a8a;
}

nav a:hover {
    text-decoration: underline;
}
"""


def main():
    print("Building Book 09 EPUB: Walk a TDD...")
    draw_cover()
    
    # 1. Assemble complete manuscript.md
    chapters = sorted(CHAP.glob("*.md"))
    sheet_files = sorted(SHEETS.glob("*.md")) if SHEETS.exists() else []
    
    manuscript_path = ROOT / "manuscript.md"
    manuscript_content = []
    
    items = []
    images = {}
    
    for path in chapters:
        text = path.read_text(encoding="utf-8")
        manuscript_content.append(text)
        blocks = md_to_blocks(text, path.parent)
        title = next((t for k, t in blocks if k == "h1"), path.stem)
        body, figs = blocks_to_xhtml(blocks)
        for name, src in figs:
            images[name] = src
        items.append((f"chap-{len(items)+1:02d}.xhtml", title, body))
        
    for path in sheet_files:
        text = path.read_text(encoding="utf-8")
        manuscript_content.append(text)
        blocks = md_to_blocks(text, path.parent)
        title = next((t for k, t in blocks if k == "h1"), f"Sheet: {path.stem}")
        body, figs = blocks_to_xhtml(blocks)
        for name, src in figs:
            images[name] = src
        items.append((f"chap-{len(items)+1:02d}.xhtml", f"Appendix: {title}", body))

    manuscript_path.write_text("\n\n---\n\n".join(manuscript_content), encoding="utf-8")
    print(f"Assembled manuscript: {manuscript_path} ({len(manuscript_content)} sections)")

    nav_items = '<li><a href="copyright.xhtml">Copyright</a></li>\n' + "\n".join(
        f'<li><a href="{name}">{html.escape(title)}</a></li>' for name, title, _ in items
    )
    nav = xhtml("Contents", f'<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>{nav_items}</ol></nav>')
    colophon = xhtml(
        "Copyright",
        f"""<section epub:type="copyright-page">
<h1>Copyright</h1>
<p><em>{html.escape(TITLE)}</em></p>
<p>Tristan. Data Center Field Guides. First edition, 2026.</p>
<p>Copyright 2026. All rights reserved.</p>
<p>A reader may copy the visit sheet headings into a financing or technical audit file. A reader may not paste standard text or equipment serials into a lender's report and call it an independent finding.</p>
<p>This book is an operational field guide for technical due diligence, site selection, civil hydrology, structural floor loading, and financing opinions. It is not an official legal covenant, a structural engineering stamp, or a credit rating model.</p>
<p>The text and the figures in this edition are AI-generated. Figure labels are English. Translations, where they exist, are separate editions.</p>
<p>List price 6.99 USD. Not enrolled in an exclusive program.</p>
</section>""",
    )
    cover_doc = xhtml("Cover", '<section epub:type="cover"><img src="images/cover.jpg" alt="Cover"/></section>')
    manifest = [
        '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
        '<item id="css" href="styles.css" media-type="text/css"/>',
        '<item id="font-regular" href="fonts/DejaVuSans.ttf" media-type="font/ttf"/>',
        '<item id="font-bold" href="fonts/DejaVuSans-Bold.ttf" media-type="font/ttf"/>',
        '<item id="cover-img" href="images/cover.jpg" media-type="image/jpeg" properties="cover-image"/>',
        '<item id="cover" href="cover.xhtml" media-type="application/xhtml+xml"/>',
        '<item id="copyright" href="copyright.xhtml" media-type="application/xhtml+xml"/>',
    ]
    spine = ['<itemref idref="cover"/>', '<itemref idref="copyright"/>', '<itemref idref="nav"/>']
    for name in sorted(images):
        manifest.append(f'<item id="img-{name.replace(".", "-")}" href="images/{name}" media-type="image/png"/>')
    for i, (name, _title, _) in enumerate(items, 1):
        manifest.append(f'<item id="c{i}" href="{name}" media-type="application/xhtml+xml"/>')
        spine.append(f'<itemref idref="c{i}"/>')
    opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="uid" version="3.0" xml:lang="en">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="uid">urn:uuid:book-09-walk-a-tdd</dc:identifier>
<dc:title>{html.escape(TITLE)}</dc:title>
<dc:language>en</dc:language>
<dc:creator>Tristan</dc:creator>
<dc:rights>Copyright 2026. Text and figures are AI-generated.</dc:rights>
<meta property="dcterms:modified">2026-10-14T00:00:00Z</meta>
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
    OUT.parent.mkdir(parents=True, exist_ok=True)
    if OUT.exists():
        OUT.unlink()

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
        for name, _title, body in items:
            add(zf, f"OEBPS/{name}", xhtml(_title, body))
        zf.write(FIG / "cover.jpg", "OEBPS/images/cover.jpg")
        for name, path in images.items():
            if not path.exists():
                raise SystemExit(f"missing figure {path}")
            zf.write(path, f"OEBPS/images/{name}")
        zf.write(FONT_DIR / "DejaVuSans.ttf", "OEBPS/fonts/DejaVuSans.ttf")
        zf.write(FONT_DIR / "DejaVuSans-Bold.ttf", "OEBPS/fonts/DejaVuSans-Bold.ttf")
    print(f"Successfully compiled: {OUT}")
    print(f"File size: {OUT.stat().st_size:,} bytes")
    print(f"Chapters embedded: {len(items)}")
    print(f"Flagship images embedded: {len(images)}")


if __name__ == "__main__":
    main()
