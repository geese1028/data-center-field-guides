#!/usr/bin/env python3
"""
Build script for EPUB edition of:
Finish a Liquid Cooling Verification: Seven sheets for one load-bank test

Compiles all 17 chapters from chapters/*.md and embeds 7 flagship engineering diagrams.
Applies modern typographic styling, semantic HTML5/XHTML, and strict EPUB 3.0 packaging.
"""

import html
import re
import zipfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path("/Users/geese/Downloads/book/books/03-run-one-test")
CHAP = ROOT / "chapters"
FIG = ROOT / "figures"
OUT = ROOT / "epub" / "finish-a-liquid-cooling-verification.epub"
FONT_DIR = Path("/Users/geese/Downloads/book/books/01-liquid-load-bank/fonts")

BG = (18, 21, 28)
BLUE = (0, 102, 255)
CYAN = (0, 229, 255)
GRID = (30, 36, 48)
TEXT = (255, 255, 255)
TITLE = "Finish a Liquid Cooling Verification"
SUB = "Seven sheets for one load-bank test"


def font(size, bold=False):
    path = FONT_DIR / ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf")
    if path.exists():
        return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


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
        if cur:
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


def draw_cover():
    im, d = new_canvas(1600, 2560)
    # Accent cyan bar
    d.rectangle((70, 160, 90, 2100), fill=CYAN)
    d.text((140, 180), "03  /  FIELD GUIDE", font=font(28, bold=True), fill=CYAN)
    d.text((140, 240), "LIQUID COOLING VERIFICATION", font=font(26, bold=True), fill=BLUE)
    y = 420
    display = font(64, bold=True)
    for line in wrap(d, "FINISH A LIQUID COOLING VERIFICATION", display, 1280):
        d.text((140, y), line, font=display, fill=TEXT)
        y += 88
    d.line((140, y + 30, 980, y + 30), fill=CYAN, width=2)
    d.text((140, y + 60), "SEVEN SHEETS.  ONE LOAD-BANK TEST.", font=font(28), fill=TEXT)
    d.text((140, y + 110), "A BLANK CELL IS A STOP.  AUDIT BEFORE IT ARRIVES.", font=font(28), fill=TEXT)

    # Technical block
    d.rectangle((140, y + 200, 1300, y + 420), fill=(26, 32, 44), outline=BLUE, width=2)
    d.text((170, y + 230), "LEVEL 0 THROUGH LEVEL 6 COMMISSIONING HIERARCHY", font=font(20, bold=True), fill=CYAN)
    d.text((170, y + 275), "• BSRIA BG 29/2020 Secondary Flushing & 1.5x MAOP Hydrostatic Hold", font=font(18), fill=TEXT)
    d.text((170, y + 315), "• Cold No-Heat Baseline Pump Curve & Thermal Viscosity Shift Decoupling", font=font(18), fill=TEXT)
    d.text((170, y + 355), "• Multi-Tier Thermal Heat Ladder (0-110%) & Enthalpy Reconciliation >= 97%", font=font(18), fill=TEXT)

    d.text((140, 2280), "TRISTAN", font=font(34, bold=True), fill=CYAN)
    d.text((140, 2340), "DATA CENTER FIELD GUIDES // ED. 2026", font=font(26, bold=True), fill=TEXT)
    FIG.mkdir(parents=True, exist_ok=True)
    png = FIG / "cover.png"
    jpg = FIG / "cover.jpg"
    im.save(png, "PNG")
    im.convert("RGB").save(jpg, "JPEG", quality=95, optimize=True)
    return png, jpg


import sys
sys.path.insert(0, str(ROOT.parent))
from epub_renderer import (
    SHARED_CSS as CSS,
    blocks_to_xhtml,
    inline_format,
    md_to_blocks,
)


def xhtml(title, body, lang="en"):
    return f"""<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{lang}" lang="{lang}">
<head>
<meta charset="utf-8"/>
<title>{html.escape(title)}</title>
<link rel="stylesheet" type="text/css" href="styles.css"/>
</head>
<body>
{body}
</body>
</html>
"""


def main():
    print("Building Book 03 EPUB...")
    draw_cover()
    chapters = sorted(CHAP.glob("*.md"))
    items = []
    images = {}
    for path in chapters:
        blocks = md_to_blocks(path.read_text(), path.parent)
        title = next((t for k, t in blocks if k == "h1"), path.stem)
        body, figs = blocks_to_xhtml(blocks)
        for name, src in figs:
            images[name] = src
        items.append((f"chap-{len(items)+1:02d}.xhtml", title, body))

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
<p>A reader may copy the master sheet headings and checklists into a project commissioning file. A reader may not paste a sentence from this book into a site method statement and call it the hall's binding rule.</p>
<p>This book is an operational field guide for liquid load-bank verification. It is not a building commissioning manual, a vendor specification, or a facility operating procedure. Limits belong to the approved script, or to the specification then in force.</p>
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
<dc:identifier id="uid">urn:uuid:book-03-finish-a-liquid-cooling-verification</dc:identifier>
<dc:title>{html.escape(TITLE)}</dc:title>
<dc:language>en</dc:language>
<dc:creator>Tristan</dc:creator>
<dc:rights>Copyright 2026. Text and figures are AI-generated.</dc:rights>
<meta property="dcterms:modified">2026-10-13T00:00:00Z</meta>
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
