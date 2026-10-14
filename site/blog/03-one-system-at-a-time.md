---
title: One liquid system at a time
description: Why a liquid-hall verification runs one system before the integrated heat window, and what an open fail blocks.
book: Finish a Liquid Cooling Verification
slug: one-system-at-a-time
---

# One liquid system at a time

![One system before the integrated heat window.](figures/levels.png)

*Original diagram. Not a site record.*


A liquid hall is more than one machine sharing pipes. If you heat the whole hall before one system has shown it can run, a failure has too many owners. The landed order that survives without site names is simple: survey, static checks, one system at a time, a no-heat pump curve, then the heat scripts, then shutdown, then the report.

The no-heat curve matters. It tells you the pumps and the path before energy confuses the picture. Skipping it because the schedule wants heat is how a flow problem is discovered as a temperature problem.

An open fail blocks the next stage. "We will watch it during heat" is not a close. It is a decision to run later with a known defect, and it needs a waiver that says what you will do if the defect appears under heat. A waiver without that sentence is permission to be surprised.

Do not mix a bad file with a plant fail. If the load bank file is not a valid test, that is not yet a punch item against the constructor. Separate the owners before you write the line.

From *Finish a Liquid Cooling Verification*, Tristan, Data Center Field Guides. No store link until the Kindle edition is listed.

Related: [A hit is a time, not a pass](02-a-hit-is-a-time.md).
