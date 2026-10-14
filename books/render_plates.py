#!/usr/bin/env python3
"""Readable record plates. White field. The figure is the sheet, not a slogan."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FONT = Path("/Users/geese/Downloads/book/books/01-liquid-load-bank/fonts/DejaVuSans.ttf")
FONTB = Path("/Users/geese/Downloads/book/books/01-liquid-load-bank/fonts/DejaVuSans-Bold.ttf")
ROOT = Path("/Users/geese/Downloads/book/books")
W = 1400


def font(size, bold=False):
    return ImageFont.truetype(str(FONTB if bold else FONT), size)


def wrap(draw, text, fnt, width):
    lines = []
    for para in text.split("\n"):
        if para == "":
            lines.append("")
            continue
        cur = ""
        for word in para.split(" "):
            trial = word if not cur else cur + " " + word
            if draw.textlength(trial, font=fnt) <= width:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = word
        lines.append(cur)
    return lines


def plate(rel, title, body):
    scratch = Image.new("RGB", (W, 200), "white")
    d = ImageDraw.Draw(scratch)
    title_lines = wrap(d, title, font(22, True), W - 80)
    body_lines = []
    for block in body:
        body_lines.extend(wrap(d, block, font(18), W - 80))
        body_lines.append("")
    h = 48 + len(title_lines) * 32 + 16 + len(body_lines) * 28 + 40
    im = Image.new("RGB", (W, h), "white")
    d = ImageDraw.Draw(im)
    y = 36
    for line in title_lines:
        d.text((40, y), line, font=font(22, True), fill=(17, 17, 17))
        y += 32
    y += 12
    d.line((40, y, W - 40, y), fill=(17, 17, 17), width=2)
    y += 18
    for line in body_lines:
        if line:
            d.text((40, y), line, font=font(18), fill=(17, 17, 17))
        y += 28
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    im.save(path, "PNG")
    return path
