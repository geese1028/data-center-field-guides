# 0. How to use this book

This book is for the person who runs a load-bank test on a liquid-cooled data center hall before production IT equipment arrives. The load bank is already accepted. You can already parse telemetry and flash reports. The job in front of you is to connect that load bank in place of the high-density rack, heat the plant on purpose under controlled thermal steps, and leave the hall with engineering records that a third-party auditor, insurer, or hyperscaler operations team can inspect without a telephone call.

It is not a building commissioning manual. The overarching method statement tells you which contract deliverables to file and which completion certificates you are legally authorized to sign. The work itself is the verification of the liquid loop: physical uncrating, megger and ground isolation, secondary flushing and hydrostatic pressure holds, cold pump curve baselining, alarm loops, multi-tier thermal steps, transient failure rides, and a structured shutdown. If a paragraph starts to become an architectural tour of the facility, cut it. Leave the engineering sheet.

**THREE INDEPENDENT COMMISSIONING GATES**

| THE SCRIPT DRAFT Pre-approved tolerances, instrument calibration IDs, and non-negotiable stops | THE FIELD EXECUTION One person measures, one writes in ink; zero unapproved overrides | THE AUDITED PACK Seven completed sheets, trend logs, raw time series, and signed punch registers |
| :--- | :--- | :--- |

If you are on the tools tomorrow, turn to Chapter 16 and take the master sheets onto the floor. Read Chapters 2 and 3 before anyone asks you to sign a Level 1 or Level 4 certificate; those chapters prevent a field walk-through from being filed into a factory acceptance binder. They keep two distinct commissioning numbering systems from destroying project compliance.

When the test window closes, you must hand over seven complete sheets, filled in ink or marked explicitly as out of scope in writing. A blank cell is an automated stop. A number copied from the previous job is a fabricated record with units attached. The load percentage, dwell duration, and hydraulic limit come from the approved test script or the engineering specification in force. This book does not invent them.

## What you may copy

You may copy the sheets in Chapter 16 into your project file, print them on waterproof paper, and fill them on the floor. You may not paste sentences from this book into a site method statement and call them the data hall's mandatory operating rule. The hall has its own operational permits, its own electrical flash boundaries, and its own piping and instrumentation diagrams (P&IDs). These sheets define what those permits and scripts must cover; they do not replace the engineer of record.

Two people must be on the tools for every test sequence: one measures with calibrated instrumentation, and one records in ink. The person authorized to command heat is a single name, written on the sheet before the first breaker is closed. Universal stop authority belongs to every person in the room.

## Decisions to record before the first step

- The exact boundary sentence this load-bank test is commissioned to prove.
- The physical test unit: which coolant distribution unit (CDU), which manifold trunk, and which rack positions—not an abstract hall.
- Which of the seven sheets this test will execute, and which are designated as not applicable in signed writing.
- The designated single authority permitted to command thermal load.
- The physical location of the emergency stop mechanisms and the secondary de-energization path.
