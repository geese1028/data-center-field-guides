# 19. Public sources, and the copyright line

This chapter is the rule for every citation in the book. The earlier chapters name documents. They do not reproduce them. If a later edit pastes a table, a figure, a class limit, or a paragraph from any of those documents, delete the paste. A citation is a pointer. A paste is a different work, and often one you are not allowed to publish.

## What “public” does not mean

A page anyone can open is not a page anyone can copy. NVIDIA’s product page is public and still NVIDIA’s. ASHRAE posts titles of free technical bulletins and still claims the text. A code you can buy is not a code you can transcribe into a field guide. Open Compute Project specifications are often downloadable and still have a license. Read the license. The default in this book is: title, publisher, edition or date, and the question the document is supposed to answer. Not the answer, copied.

ASHRAE states, on its data center resource page, that content from ASHRAE publications and related ASHRAE intellectual property may not be entered into an AI tool, and that derivative works of that intellectual property made with AI require ASHRAE’s written permission. This manuscript follows that line. It names ASHRAE documents. It does not digest them, paraphrase their tables, or restyle their water-quality limits into a checklist. If you need those limits, you read the edition you are licensed to read, and you cite that edition on your own project sheet, inside the system that is allowed to hold it.

The same restraint applies to NVIDIA datasheets, to NFPA and IEC texts, and to any vendor interface specification. The project sheet may hold a value you are allowed to use on the project. This book may not.

## How a citation earns a cell

A public document earns a cell only if it is the document that governs the interface or the code you are actually under. A blog post that describes a rack does not set flow. A product page that says a rack is liquid-cooled tells you the stand-in must be liquid, not air. It does not fill the duty set. A handbook chapter on data centers tells you the building problem is real. It does not design your load bank.

Write the citation as: title, organization, edition or revision, date you read it, and the cell it is allowed to inform. If you cannot name the edition, the cell stays unknown. “ASHRAE” is not an edition. “The NVIDIA page” is not an edition. “The code” is not an edition.

## Rack-side and building-side, in this book’s words

Industry literature separates the water that rejects heat from the building and the water that would have flowed through the IT. The names differ by publisher and by year. This book does not adopt a publisher’s glossary by copying it. It uses two names of its own, already used in the liquid-path chapter.

Rack-side is the closed loop that would have served the rack. The load bank sits here. It presents heat and resistance instead of the IT. CDU-side, or building-side, is the loop that brings heat to the plant: towers, chillers, or whatever the hall uses. A heat exchanger, usually inside a coolant distribution unit, is the boundary. The two waters are not the same water unless a cited design says they are, and that design is unusual for a cold-plate rack.

Primary and secondary are words you will see in ASHRAE titles and in vendor drawings. Do not assume they match this book’s rack-side and CDU-side until you have read the edition and written a one-line glossary. If the edition uses the words the other way around, your glossary wins inside your file, and the citation records their words. Mixing them without a glossary is how a valve on the building loop gets specified as if it were the rack fitting.

What you take from that literature, without quoting it, is the boundary problem: chemistry, dirt, temperature, and pressure on the building side are not automatically acceptable on the rack side. The heat exchanger exists because they are not. Your materials row cites the coolant on the rack side. It does not cite “facility water” and stop.

## What NVIDIA’s public page is allowed to do

NVIDIA’s public product page for the GB200 NVL72 describes that system as a rack-scale, liquid-cooled design, and states a configuration of 36 Grace CPUs and 72 Blackwell GPUs. A later public page describes the GB300 NVL72 as fully liquid-cooled and rack-scale as well. Those sentences justify the claim that an air heater is the wrong stand-in for this class of rack. They do not justify a flow, a pressure, a fitting family, or a temperature window.

The same page links a datasheet. If the datasheet contains interface numbers, those numbers live in the datasheet’s revision, on your project sheet, if you are allowed to use them there. They do not move into this book. Marketing comparisons on the product page, multiples against an older platform, are not acceptance criteria. Do not let a factor of thirty, or any other factor, into a duty cell. The cell needs the cited interface document, not a performance slogan.

When the public name moves, from one rack generation to the next, the method does not move with the slogan. You cite the generation you are standing in for, by the page or datasheet revision you actually used. A book that freezes one generation’s marketing name as the permanent duty is obsolete on purpose. This book says NVL72-class so that the citation can name the generation.

## Electrical control, as categories

Two codes can apply, and they apply to different sides of the plug.

The premises wiring code governs the hall: in the United States, NFPA 70, the National Electrical Code, in the edition the authority having jurisdiction has adopted. Elsewhere, the national adoption of IEC 60364 or the local wiring rules. This book does not design the hall. It requires the power interface line to name the code and edition that the feed was built to, or to mark that unknown.

The equipment rules govern the unit. IEC 60204-1, safety of machinery, electrical equipment of machines, is the usual international place to look for a machine that has heaters, a control circuit, and a disconnect. A product-safety listing the builder actually claims, under UL, IEC, or the mark they print, is the other place. Name the standard and the edition. Do not copy articles into the acceptance sheet. Copy the test names you will run, and the pass criteria from the edition you hold.

The control requirements this book will defend, in its own words, are these. A lockable disconnect that removes heater power and cannot be overridden by a remote command. Overcurrent protection that opens heat, with a known state of the control supply when it opens. A protective earth that is tested. A control circuit whose loss removes heat. A stop that does not ask a network for permission. Liquid that cannot track into live parts. Those are the gates. The code edition tells you the test method where the code has one. Where it does not, you write the method, and you do not pretend the code said it.

ASHRAE’s titled bulletin “Data Center Power Equipment Thermal Guidelines and Best Practices” is about the thermal environment of power equipment, not a substitute for the wiring code. Cite it if the project needs that subject. Do not extract it.

## Titles worth a bibliography line

Put these on the project bibliography as titles to obtain, not as text to paste.

ASHRAE TC 9.9, and the Datacom Encyclopedia or the remaining Datacom Series titles your edition still sells. In particular, look up the current liquid-cooling title, the water-cooled server material, and the thermal guidelines. ANSI/ASHRAE Standard 90.4, energy standard for data centers, if someone tries to make this load bank carry the hall’s energy claim. It should not. ASHRAE Handbook, HVAC Applications, chapter on data centers and telecommunication facilities, current volume. The free-titled bulletins listed on ASHRAE’s data center resource page, including the liquid-cooling emergence paper, the water-cooled servers paper, and the power-equipment thermal paper. Read them under whatever license the download grants. Do not feed them to a tool and do not reprint them here.

NVIDIA data-center catalog, https://www.nvidia.com/en-us/data-center/, read 11 October 2026. From that catalog, the pages that can inform this book are the GB200 NVL72 product page, the GB300 NVL72 product page, and the datasheets those pages link. The catalog also points at a data-center GPU line card, a resource hub, MLPerf results, NVIDIA-Certified Systems, and a qualified system catalog. Those identify products. They do not set coolant flow. Chapter 2 records the configuration facts taken from the two NVL72 pages and the rule that memory bandwidth is not flow. Re-read the live page before you copy a number onto a project sheet. The page will move. This book’s date will not.

NFPA 70, adopted edition, for a United States feed. IEC 60364, national adoption, for the premises side elsewhere. IEC 60204-1, edition cited, for the machine. The product-safety standard named on the unit’s marking, if any.

Open Compute Project cooling or liquid-cooling specifications, only if the interface owner has adopted one, and only under that specification’s license.

None of these titles outrank the interface specification then in force for the rack you will mate to. They inform the blank. They do not fill it by being famous.

## Decisions to record

- The bibliography on the project sheet: title, edition, date read, cell it may inform.
- A line that ASHRAE text, NVIDIA datasheet tables, and code articles are not pasted into any file that will be published.
- The glossary line: rack-side and CDU-side, and whether the cited edition’s primary and secondary match those words.
- The electrical split: premises code edition for the feed, equipment standard edition for the unit.
