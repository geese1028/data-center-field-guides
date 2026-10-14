---
name: book-design
description: Use when making figures, a cover, EPUB3, or print typesetting for an accepted or owner-approved field guide. Trigger on 插图, 排版, EPUB, cover, epubcheck.
---

# Book design

Typeset the approved manuscript. Do not rewrite the technical claims.

## Figures

Draw original figures in the series look: near-black field, fine cyan grid, amber index labels, DIN or monospace type. No cream handbook boxes, no vendor screenshots, no site drawings, no NVIDIA logos, no photographs of equipment. Each figure has a caption that states what decision it supports. Prefer SVG source and PNG in the EPUB. Place a figure where the prose needs it: boundary, command path, acceptance gates. Do not decorate.

## EPUB3

Build EPUB3 under `books/<slug>/epub/`. One XHTML file per chapter. CSS sets a serif body, a sans heading, and a figure width of 100 percent. The cover is an original PNG, 1600 by 2560. The package `mimetype` is stored first and uncompressed.

## Check

Run epubcheck if Java is available. If it is not, say so, and still check: mimetype first, container.xml, nav, unique ids, escaped text, images declared in the manifest. Do not claim the file passed epubcheck unless the tool ran.

## Out of scope

Do not log into KDP. Do not buy reviews. Do not generate ads.
