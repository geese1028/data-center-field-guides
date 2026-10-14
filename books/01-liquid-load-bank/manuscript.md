# 0. How to use this book

This book is a field guide for people who must specify and accept a liquid load bank that can stand in for an NVL72-class rack. It is not a fabrication package. It is not a vendor specification rewritten in friendlier English. It is not a site procedure.

When you finish it, you should be able to hand a stranger two documents and have those documents survive contact with a prototype. The first is a requirements list. The second is a prototype acceptance sheet. If you cannot produce those two documents from what you have written in the margins, you have not finished the book. You have only read it.

The load bank replaces the rack-side thermal duty and the rack-side hydraulic duty. It does not replace the coolant distribution unit. It does not accept the hall. It does not prove that the IT equipment will boot, train, or stay within its own limits. Those are different machines and different arguments. Mixing them is how a load-bank project becomes a liquid-cooling project with no owner.

## What this volume owns

This volume owns the decisions you must make before anyone cuts metal, and the gates you must pass before you call a prototype finished. It owns the functions the unit must perform, the quantities that define its duty, the liquid-path choices that keep it from becoming a leak with a heater, the heat-path choices that keep the heater honest, the instruments and the data exit, the stops that must work when the network does not, and the file you hand over with the machine.

It does not own how to read a month of test data. That is the next book. It does not own how to run one NVL72 test project in a hall, with people, windows, and a CDU that already exists. That is the book after. If a paragraph here starts to become a test plan for a building, or a method for cleaning a time series, cut it. Leave a pointer. Do not smuggle the later books into this one to make the page look complete.

## Who it is for

It is for the test engineer who will be blamed when the numbers do not match, and for the person who will sign the purchase or the build. It is not for a marketing reader who wants a tour of liquid cooling. It is not for a fabricator who needs hole sizes. If you need hole sizes, you need a drawing, and this book will tell you what that drawing must not be allowed to decide on its own.

You can use it if you have never built a load bank, provided you will write things down. You can use it if you have built several, provided you are willing to throw away the last project’s part numbers. Experience that arrives as a shopping list is not experience. It is residue.

## How to read it

Read in order the first time. The acceptance gates in the long chapter near the end only make sense if you have already decided what the unit is for. After that, use it as a checklist. Each chapter ends with decisions to record. A decision is one of three things: a sentence you will defend, a blank you will fill from the specification then in force, or an explicit deferral with a date and an owner. A silent skip is not a decision. It is how prototypes ship with a hose that cannot be isolated.

Keep a notebook, or a single file, with the same headings as the chapters. Do not annotate the book and call that the requirements list. The requirements list has to be able to leave your hands. The book stays here.

When a chapter says “do not write the number,” it means the number is not cleared for this book, or it is not stable enough to be a teaching example. It does not mean the number does not matter. It means you write the check, then you write the number on your own sheet, citing the document title and revision you actually used. A field guide that freezes a vendor figure becomes false on the day the vendor revises it. A field guide that tells you where the figure lives stays usable.

## The specification then in force

You will see that phrase often. It means the rack, manifold, and coolant documents that govern the interface on the day you accept the prototype, identified by title and revision, not by memory and not by a slide from last year. If two documents disagree, you do not average them. You record the disagreement and you stop the affected line of the acceptance sheet until someone who owns the interface picks one. This book will not pick it for you. Picking it here would be inventing a standard.

The same rule applies to electrical supply. Voltage, frequency, and connector family belong on your sheet because the hall you will plug into is real. They do not belong in this book as if one hall were the world.

## What “good” looks like before any metal exists

A good early package is dull. It has a one-page statement of what the load bank is allowed to represent. It has the six functions, each with an evidence column. It has a duty point written as a set of quantities, with the numeric cells either filled from a cited revision or marked unknown. It has a liquid-boundary sketch that a stranger can redraw from the prose. It has a point list of functions, not a register map. It has four acceptance gates with pass lines and stop lines. It has a known-limitations page that is already started, not a page you intend to write after the argument.

A bad early package is a rendering, a kilowatt number, and a promise that the software will be flexible. Flexibility is what people write when they have not chosen the steps. A rendering is what people show when they have not chosen the boundary.

## Two documents, not ten

You will be tempted to start a document set: a design basis, a philosophy, a compliance matrix, a risk register, a test strategy. Resist that until the two documents exist. The requirements list is the design basis. The acceptance sheet is the test strategy for the prototype. Extra documents are allowed after those two can be read without you in the room. Extra documents before that are how projects hide the fact that the six functions were never written down.

The requirements list is not a quote request, though a quote request can be cut from it. The acceptance sheet is not a factory test report, though the factory test should be forced to answer it. Keep the direction of dependence straight. The sheet judges the machine. The machine does not edit the sheet on the day, except through a waiver path you defined before the day.

## Composite examples

Later chapters use short composite scenes: a prototype on a bench, a hose that looked fine until it was filled, a display that repeated the last good value. They are teaching scenes. They are not a site, not a customer, and not a model number. If a scene starts to look like a place you have worked, that is because the failure mode is common, not because the book is publishing that place. Do not add the place back in when you copy a checklist into your project file.

## What you may copy out of this book

You may copy the headings of the requirements list, the four gate names, and the rule that a quantity without a false story is an ornament. You may not copy a sentence into a vendor manual and call it a specification. The sentences here are checks and reasons. A specification needs numbers, materials callouts, and an owner. Those come from your project, under your authority, on the day you have the revision in hand.

## A first sitting

If you only have an afternoon before a vendor meeting, do not skim for reassurance. Do this instead. Write the six functions in your own words. Write the duty as a set, and mark every number unknown that you cannot cite. Draw the liquid boundary and mark which side the unit sits on. Name the four gates. Put a date on the unknowns. That afternoon is worth more than a week of chassis sketches.

Then come back and read the chapter that attacks the unknown you are most tempted to leave blank. For most readers that is either the flow regime or the data exit. People are comfortable talking about heaters. They are less comfortable saying that a load bank which cannot be compared with the rack side is not yet a stand-in.

## Public sources for this chapter

Use a public document as a map, not as a chapter you are allowed to rewrite. The map for this volume is short. NVIDIA’s public GB200 NVL72 page says that class of rack is liquid-cooled and rack-scale. ASHRAE TC 9.9 is where the industry looks for cooling guidance, under license. NFPA 70 or the local wiring code, and IEC 60204-1, are where electrical stops get a legal name. Chapter 19 states the copyright line. Read it before you open a PDF into any tool. ASHRAE has said its publication content is not to be entered into an AI tool, and that AI derivative works of that content need written permission. This book names titles. It does not digest them.

## Decisions to record

- The two documents you will produce, and who signs each.
- Which later questions you are explicitly leaving to the data book and the project book.
- The title and revision of the interface specification, or the date by which that blank will be filled.
- The one-sentence statement of what this load bank is allowed to represent, and what it is not allowed to represent.


# 1. Write the requirement before the structure

People begin with a box. They ask how tall it is, what color the enclosure is, and whether the display can be branded. Those questions are not forbidden. They are simply too early. A box is a way of holding a job. If the job is vague, the box will be confident and wrong.

The job of this load bank is to present, at a liquid interface that can mate to an NVL72-class rack manifold, a heat load and a hydraulic load that the rest of the cooling chain can be exercised against. The job is not to look like a rack. The job is not to contain a CDU. The job is not to be a general laboratory heater that might, with enough adapters, be talked into the role.

Across the project material that shaped this book, the same functions appeared whenever someone tried to buy or accept a liquid load bank. Treat that recurrence as a warning, not as a catalog. If independent attempts keep asking for the same six things, those six things are the minimum. Anything you add is a project choice. Anything you drop is a decision to accept a blind spot, and it belongs on the limitations page.

## The six functions

Write them as functions, not as features. A feature is something a brochure can claim. A function is something an acceptance sheet can fail.

### Flow must be adjustable

The unit must let you change flow and hold the new flow long enough to believe it. Adjustable does not mean “a valve exists somewhere in the room.” It means the person running the prototype can move flow across the range the duty sheet requires, without rebuilding the hose, and can tell that the move happened.

A valve that is buried, unlabeled, or arranged so that the only way to reduce flow is to starve the entire path will be called adjustable on a quote and immovable on the day. Ask where the authority sits. On the unit, by a trim device you can see. By a bypass that changes how much of the flow sees the heat. By a request to some other machine. One of those is the design. “The system will balance” is not a design.

False compliance: a hand valve that can be set once by the person who built the unit, with no scale, no indication, and no second person able to return to the same point. That is a tuning secret, not an adjustment.

Evidence: during acceptance, flow is moved between at least two declared points and the indicated flow agrees with a check method you named in advance. The check method can be a temporary meter. It cannot be the same display you are trying to believe, and it cannot be a feeling that the hose is warm.

### Supply temperature and return temperature must be readable

Both. A single temperature is a mood. The difference between supply and return, read at declared locations, is the thermal evidence that heat entered the liquid. Supply means the liquid arriving at the load, or at the boundary you defined. Return means the liquid leaving it. If you mix those names up, every later argument is noise. Define them on the one-line diagram and never reuse the words for the CDU’s own supply and return without a qualifier.

Readable means a person and the test platform can both see the value, in declared units, with a timestamp. A thermometer in a pocket that someone can walk over and read is a check instrument. It is not a substitute for the unit’s own reading unless you have said, in the limitations, that this prototype has no remote temperature and the check instrument is the record. That limitation is allowed. Hiding it is not.

False compliance: a temperature shown on a local screen with no unit, updated “about every so often,” and no way to know whether the sensor is in the flow or in a dead leg. Dead-leg temperature is a story about a pocket of liquid, not about the stream.

Evidence: both temperatures appear in the exported record at the declared interval, and a check instrument at a defined point agrees within a tolerance you wrote before the test. If you have not earned the right to publish a tolerance, write the comparison as “record both, do not pretend they are the same instrument.” You may still fail the gate if they disagree by enough to change the heat-balance story. Disagreement that changes the story is a stop, even when you refused to invent a fake accuracy class.

### Flow must be readable

Adjustable flow that you cannot read is a knob. Readable flow that you cannot adjust is a weather report. You need both, and you need them on the same liquid path you claim to be loading. A flow meter on a bypass, reported as if it were the flow through the heat source, is a common way to pass a demonstration and fail a real hour.

Say where the meter sits relative to the heat and relative to any branch. Say what it cannot see. A meter downstream of a branch will not tell you how the branches shared the flow unless you have a meter on each branch you care about.

False compliance: a calculated flow, inferred from a pump curve and a valve angle, presented with the same confidence as a measured flow. Inference can be a check. It is not the primary reading unless your limitations page says the prototype has no flow meter and every conclusion is provisional. For a unit that claims to stand in for a high-flow rack, that limitation should usually kill the claim, not decorate it.

Evidence: the reading is in the record, in declared units, and a second method has been compared at least at the duty point and at one reduced point. The second method is named. “We looked at the pump” is not a name.

### Pressure must be readable

Pressure here means enough pressure information to know the hydraulic price of the flow you just asked for. At minimum, a reading on the inlet side of the unit and a reading on the outlet side, so a difference can be formed. A single gauge on a header tells you that the header is not open to atmosphere. It does not tell you what the load bank is doing to the loop.

The rack you are standing in for presents a resistance. If your unit’s resistance is a surprise, the CDU or the manifold will not experience the stand-in you think you built. You do not have to copy a published resistance curve into this book. You do have to put “differential pressure at the declared flow” on the duty sheet, and you do have to be able to read the two pressures that create it.

False compliance: a gauge installed where it is convenient to drill, upstream of a half-closed valve, labeled “pressure” with no indication of which pressure. Convenience taps are how people argue for a week about a number that was never the quantity in the requirement.

Evidence: both pressures, or a differential measurement whose high and low sides are defined on the diagram, appear in the record at the same times as flow. A tap that is isolated, valved off, or full of air is a failed reading, not a low reading.

### Heat load must be adjustable in steps

The unit must be able to sit at more than one heat load. Off and full is two states, not a step sequence. Acceptance and any later commissioning both need plateaus: a low step, a middle step, a high step, full, and a return to zero. They also need at least one increase that is sudden relative to the plateau, because a control loop that only understands a slow ramp will be believed in the shop and surprised in the test you care about.

Steps are declared on the acceptance sheet before the day. They may be fractions of the duty point. They are not a theater of modes with names no one will sit on. If you cannot name the plateaus, you are not ready to buy the heater sections.

False compliance: a percentage knob with no indication of electrical power or of heat into the liquid, and no dwell. Turning a knob during a tour is not a step test. A step has a start time, a hold, and an end.

Evidence: the record shows the plateaus, the power or heat command, and the thermal response. A plateau that never stabilizes is not automatically a failure of the load bank. It might be a failure of the loop you connected it to. The acceptance sheet must say which loop is in the room, so you do not blame the prototype for a heat sink it does not have. This book accepts the prototype, not the hall. Say so in the setup line of the sheet.

### Overtemperature must protect and must alarm

Protection without an alarm trains people to ignore a trip they cannot explain. An alarm without protection is a suggestion. You need both. Overtemperature is the one protection this chapter insists on by name, because a liquid load bank’s product is heat and its failure is heat in the wrong place. Other stops are in the safety chapter. Do not wait for that chapter to decide that silent trip is unacceptable.

The alarm has to say that it is overtemperature, not “fault.” The action has to remove heat even if the display is dead. Where the sensor sits matters: a sensor on a case, far from the element and far from the liquid, will either trip too late or trip on a hot afternoon. Put the location on the diagram.

False compliance: a software limit that stops commanding heat but leaves the contactors in a state that depends on a network heartbeat. If the heartbeat dies, you need to know whether heat stays on. The safe answer is that loss of control removes heat. Write the test for that, or admit you have not built a protection.

Evidence: a controlled approach to the limit, or a simulated sensor input whose method is written down, causes heat to come off and an alarm to be recorded. Do not invent a dangerous stunt to “see what happens.” The method of proving the stop is part of the requirement. If the only method is to overheat the prototype until something smells, the requirement is not finished.

## Three interface lines

Functions are what it does. Interfaces are where it touches the rest of the world. Add three lines to the same sheet. Leave part numbers blank until the specification then in force fills them.

Liquid connection. What family of fitting mates to the manifold hose, who supplies the hose, and how long the hose may be before routing becomes a kink. Family means the kind of joint, not a catalog number copied from the last hall. The person who owns the manifold owns the family. The person who owns the load bank owns the mating half and the hose routing. Write both names. A joint with two owners and no drawing of the boundary will leak in the argument before it leaks on the floor.

Power connection. What the unit needs, and what the hall can feed, are different facts. Record both. If they do not match, the design has an adapter problem or a site problem, and you must say which one you are solving. Do not hide an adapter inside the word “compatible.” Also record whether the load is single feed or can be split, only because splitting changes how you step the heat. This is not an electrical design chapter. It is a reminder that a liquid requirement with no power line is a requirement that cannot be turned on.

Companion air-cooled load and the 80:20 thermal split. A common mistake in liquid commissioning is assuming an NVL72-class rack rejects 100% of its heat to the liquid stream. It does not. In high-density AI architectures, between 15% and 20% of total rack power dissipates as sensible heat into the data hall air—radiated by optical transceivers, motherboard voltage regulator modules (VRMs), uncooled memory DIMMs, power supplies, and cabling losses. If a commissioning campaign tests the liquid loop in isolation while leaving the hall air unheated, the facility Computer Room Air Handlers (CRAH/CRAC) and containment airflow controls remain completely unverified. The requirements sheet must therefore include a companion air-cooled load line (typically 8kW to 20kW) paired with the liquid unit, with its own step control and overtemperature protection. (See Figure 01 for the physical demarcation and the 80:20 sensible heat split).

Dew point interlock line. The requirements sheet must define an explicit condensation boundary. When supply coolant enters below the data hall dew point (T_dp), uninsulated manifold hoses and quick disconnects sweat, creating droplet runoff that drips onto 48V/power distribution shelves. The sheet must specify: supply temperature must remain at least 2.0 K above facility dew point (T_in ≥ T_dp + 2.0 K), and approaching dew point triggers an immediate automated alert and closes modulating cooling valves.

## The evidence column

Each function line has four cells. The function, in a sentence a stranger can test. The side of the boundary where it is observed. The evidence that it works. The failure that means do not ship.

A line that cannot fill the last cell is a wish. “Flow is adjustable” fails that test if you cannot say what non-adjustment looks like. Non-adjustment looks like: the indicated flow does not move when the command moves, or it moves and will not hold for the dwell you named, or it moves on the local screen and not in the export. Pick the one that matches your design. Write it down.

The side cell stops a particular kind of cheating. Temperature observed only inside a vendor controller, with no defined tap, will be “observed” in a way you cannot audit. Say “liquid at the unit outlet” or “liquid at the rack-side hose, temporary probe.” Those are different sides. Both can be valid. Neither should be implied.

## A sheet you can fill this week

Make one table. Rows are the six functions plus the three interface lines. Columns are: statement, observed where, evidence, do-not-ship if, owner, status. Status is one of: written, unknown with a date, deferred with a reason, or cited to a document revision.

Do not add a column for “vendor response” yet. The vendor response is not the requirement. It is a claim you will test. If you mix them, the sheet becomes a correspondence log and stops being a specification.

Here is a filled row, generic on purpose. Statement: return temperature is readable at the unit outlet. Observed where: in the liquid leaving the heat section, not on the case. Evidence: value in the export at the declared interval, and a check probe within a band that does not change the heat-balance story. Do-not-ship if: the export repeats a stale value, or the only reading is a local screen with no time. Owner: the person signing acceptance. Status: written. Notice what is absent: no degree figure pretending to be universal, no sensor brand, no address.

Here is a bad row, also generic. Statement: high quality cooling performance. Observed where: system. Evidence: to be confirmed. Do-not-ship if: TBD. That row can survive a meeting and cannot survive a prototype. Delete it or rewrite it until the last cell hurts a little. If it does not hurt, it is not yet a stop condition.

## Who writes it

The person who will live with the data should draft it. The person who will pay for the metal should sign the scope lines. The person who owns the rack interface should fill or cite the fitting family and the duty window. If one person is all three, fine. If no person is the first, the sheet will describe a product rather than a measurement. Products are allowed to be vague. Measurements are not.

Set a rule for changes. A change to a do-not-ship cell after the prototype is built is a waiver, not an edit. Waivers have a name and a reason. Quiet edits have a way of happening in the margin of a spreadsheet at 11 p.m. Use a revision mark. The acceptance record will cite the revision. If it cites “the latest,” you will not be able to reconstruct what was agreed.

## What you are not allowed to import

Do not paste a site’s unit count into the sheet and call it the design basis. How many racks a hall wants to imitate is a project fact for a later book. This book is about one unit that can represent the rack-side duty you defined. If your project needs several units, the requirement for each unit is still this sheet, plus a line about whether they must be coordinated. Coordination is a control question. It is not a reason to skip the six functions on each unit.

Do not paste connector catalog numbers from an old pack. Cite the interface specification. If the old pack is the only place the number exists, you do not have an interface specification. You have a souvenir.

Do not paste a price, a rental rate, or a lead time. Those decide whether you build. They do not decide what “pass” means. Mixing them into the technical sheet is how a commercial argument deletes a sensor.

## Air-cooled load, and other neighbors

The air-cooled companion, if it exists, needs steps and an overtemperature alarm and a power interface. It does not need a flow meter. Do not let a template drag liquid columns into an air row, and do not let an air row’s simplicity convince you that the liquid row can drop pressure “to keep the sheet short.”

Other neighbors you will be offered: a temporary pump skid, a hose kit, a data logger someone already owns, a leak-detection string left over from another job. Each can be part of the evidence. None of them are the load bank unless you say they are in scope. Write “in the room for acceptance” as a setup list on the acceptance sheet. Write “part of the delivered unit” only for what must still be true after those loans go home.

This distinction saves prototypes. A unit that passed because a borrowed logger was brilliant, and that has no export of its own, did not pass the data-exit function. It passed a day. The requirements list is about the delivered unit. The setup list is about the day. Keep both, and do not let them merge.

## Requirement versus design

Once the sheet exists, design may start. Design chooses elements, valves, and enclosures that make the sheet true. Design does not get to delete a row because the chosen element cannot do it. If the element cannot do it, you change the element or you change the sheet through the revision rule, in daylight.

You will hear that some rows are “implementation.” Sensor location is not implementation. It changes the meaning of the number. Valve authority is not implementation. It changes whether flow is adjustable by the person you named. Alarm text is not implementation. It changes whether a stop can be explained. Hold those inside the requirement. Leave chassis thickness, paint, and cable dress to design, unless cable dress can kink the hose or block the module you said must come out. The moment dress affects a function, it returns to the sheet.

## A meeting that does not waste the sheet

Take the sheet to the first vendor or shop meeting and refuse to start with the rendering. Walk the six functions. For each, ask three questions. How will you show this on the day. What will you do when the check instrument disagrees. Which cell do you want to weaken. The third question is useful. Vendors weaken cells for real reasons: cost, lead time, a sensor that will not fit. Those reasons can be accepted as limitations or rejected as scope cuts. They cannot be discovered after the metal exists, unless you like paying twice.

If the meeting can only discuss kilowatts, you are in the wrong meeting or you sent the wrong page. Kilowatts are one cell of the duty set, in the next chapter. They are not the requirement.

## Public sources for this chapter

A requirement cell may cite a public document. It may not be replaced by one. NVIDIA’s product page can support the sentence “the stand-in is liquid, not air,” because the public description of the GB200 NVL72 is a rack-scale liquid-cooled design. It cannot support “flow is adjustable” or “temperature is readable.” Those are your functions. ASHRAE titles can support the sentence “name the loop the unit sits on, and do not assume building water and rack water are one water.” They cannot be pasted in as the six functions. If a vendor’s proposal quotes a white paper instead of answering a do-not-ship cell, send it back. The white paper is a bibliography line. The cell is yours.

## Decisions to record

- The six functions, each with observed-where, evidence, and do-not-ship.
- The three interface lines, with fitting family and power left as citations or dated unknowns.
- Whether an air-cooled companion is in scope, on its own line.
- Who drafts, who signs scope, who owns the interface citation.
- The revision rule, including what counts as a waiver.


# 2. The duty it has to survive

A load bank can meet every function in the previous chapter and still be the wrong machine. Functions say it can be adjusted and read. Duty says what it must be able to become. Those are different. A laboratory heater with a flow meter can be adjusted and read. It still may not stand in for an NVL72-class rack, because the rack’s liquid problem is not “some heat, some water.” The change that matters is the flow regime on the rack side.

High rack-side flow is the point of this class of liquid cooling. The load bank has to be able to live in that regime, not in a gentler loop that happens to use the same word, coolant. A unit sized for a small temperature rise at a modest flow will look excellent on a bench and useless at the manifold, or the reverse: it will demand a temperature rise the rack will never show, and everyone will conclude the rack is “too cold” when the rack is simply moving more liquid.

This book will not publish the vendor’s current flow, pressure, or temperature window. Those figures belong to a document with a revision. Your duty sheet cites that document. When the revision changes, the sheet changes. The metal might not, and that is a project decision, not a fact this book can freeze.

## Heat is not a nameplate

Electrical power into the elements and heat into the liquid are not the same quantity. They are close when the unit is well built, steady, and not dumping heat into the room or into a mass that has not warmed up. They are not close during the first minutes of a step, or when a cabinet is open, or when a portion of the power is lost in drives and supplies that do not touch the liquid. If your acceptance treats nameplate kilowatts as heat into the loop, you will accept a unit that cannot do the thermal job, or you will reject a unit that can, because the first minutes looked short.

Write both numbers on the sheet, with different names. Commanded electrical power. Inferred heat into the liquid. The inference needs flow and both temperatures, which is why those readings are not optional ornaments. The inference also needs you to say whether you are in steady state. A step that has not been held is not a heat measurement. It is a transient. Transients matter, but they are a different row.

You do not need a published formula with borrowed constants to use this. You need the habit of asking, at every plateau: does the temperature rise, times the flow, tell a story that matches the electrical power within a band that does not embarrass the conclusion. If you cannot form that story, you are not yet allowed to say the load bank loaded the loop. You are allowed to say the contactors closed.

## The educational baseline sandbox: 120 kW virtual rack derivation

To ensure this book provides concrete numerical yardsticks without violating vendor non-disclosure or freezing a proprietary datasheet, we establish a non-proprietary educational reference model. (See Figure 07 for the complete first-principles derivation sheet).

Assume a baseline virtual AI rack operating in a secondary liquid loop under standard testing conditions:
- **Nominal Thermal Duty**: P_thermal = 120.0 kW
- **Secondary Coolant**: 25% Propylene Glycol / 75% Water by volume (PG25)
- **Coolant Physical Properties (@ 40°C mean bulk)**: Density ρ = 1025 kg/m³, Specific Heat C_p = 3.980 kJ/(kg·K)
- **Design Thermal Delta-T**: Supply T_supply = 35.0°C, Return T_return = 45.0°C (ΔT = 10.0 K)

From first-principles thermodynamics (P = ṁ · C_p · ΔT), the required mass flow rate is:
$$\dot{m} = \frac{120.0\,\text{kW}}{3.980\,\text{kJ/(kg}\cdot\text{K)} \times 10.0\,\text{K}} = 3.015\,\text{kg/s}$$

Converting mass flow to volumetric flow rate ($Q_v = \frac{\dot{m}}{\rho}$):
$$Q_v = \frac{3.015\,\text{kg/s}}{1025\,\text{kg/m}^3} \times 60 \times 1000 = \mathbf{176.5\,\text{L/min}} \quad (\approx 46.6\,\text{GPM})$$

Now perform the hydraulic pipe velocity verification. Across a standard DN32 sanitary stainless pipe (inner diameter d_i = 32.0 mm, cross-sectional area A = 8.04 × 10^{-4} m²):
$$v = \frac{Q_v}{A} = \frac{0.00294\,\text{m}^3\text{/s}}{8.04 \times 10^{-4}\,\text{m}^2} = \mathbf{2.45\,\text{m/s}}$$
This velocity sits safely below the standard 3.0 m/s fluid erosion threshold for stainless steel piping and EPDM hoses, preventing acoustic resonance, cavitation, and particulate wear.

Finally, establish the hydraulic resistance target. The stand-in must match the rack's pressure drop curve (ΔP = k · Q_v²). At the rated 176.5 L/min flow, nominal differential pressure is targeted at ΔP_nominal = 115 kPa (1.15 bar), with an allowable prototype acceptance band of ± 10% (103.5 kPa to 126.5 kPa).

With these exact sandbox equations, your project sheet has a mathematically closed baseline. If your actual cited interface specification later demands 140 kW at 190 LPM, you adjust the variables in daylight. The method of calculation remains identical.

## The set, not the list

Four liquid quantities and one electrical quantity travel together. Heat into the liquid. Flow. Differential pressure. Supply temperature. Return temperature. Electrical power sits beside them as the means, not as a substitute.

If any one is missing, the others can tell a false story that looks like engineering.

Heat without flow: you may be heating a trapped volume, a dead leg, or a unit that has begun to boil in a place you did not intend. The temperature will move. The movement will be frightening and uninformative.

Flow without temperatures: a high flow can mean the stand-in is realistic or that the heat is off. You cannot tell. Low flow can mean a realistic reduced step or a blockage. You cannot tell.

Temperatures without flow: a small rise can mean high flow, which may be what you wanted, or failed heaters, which is the opposite. A large rise can mean the rack-like condition or a hose on its way to a kink. The rise alone does not know.

Pressures without flow: you can see that the loop is stressed and not know whether you are at the duty flow or at a trickle through a half-closed valve. Stress at the wrong flow is not the rack’s resistance. It is an accident with a gauge.

Flow and temperatures without differential pressure: you can balance the heat and still present the CDU with a hydraulic surprise. The CDU will then move off the operating point you thought you were testing, and the later data book will try to explain a control reaction that began in your omission.

Electrical power without the liquid set: you can prove the feeders warmed and not prove the coolant did.

So the duty sheet is one operating point, written as a set, plus the range around it that acceptance must visit. A list of five unrelated wishes is how you get a unit that can reach each number on a different afternoon.

## What an operating point contains

For each quantity in the set, answer three questions only.

Why is it measured. If the answer is “the display had a spare channel,” delete it or demote it to optional. A quantity earns its place by changing a decision: hold the step, stop the step, or refuse to call the point valid.

Which side of the boundary is it measured on. Rack side, load-bank side, and CDU side are not interchangeable. A supply temperature at the CDU outlet has already been through a pump and a hose. A supply temperature at the load-bank inlet is the liquid the heaters see. Pick the side that matches the sentence you are trying to make true. Then, if the later test needs the other side, add it as a second point rather than reusing the name.

What false story a bad reading tells. Write the sentence. “A low temperature rise will be reported as high performance when the heaters are actually off.” That sentence is the reason the flow meter and the power reading have to sit next to the temperatures. If you cannot write a false story, you do not understand the point yet. Leave it marked unknown. Do not fill it with a plausible unit and a made-up accuracy.

## Nominal, steps, and overload

The duty point is the nominal stand-in: the set you mean when you say the unit can represent the rack at the condition you care about. Around it, acceptance visits a reduced step, a middle step, full, and zero. After those are clean, it visits a short overload whose level and dwell are defined on the acceptance sheet, not invented in the room.

Do not copy those levels from a prototype report you once saw. A percentage that was right for one element arrangement is a superstition for another. The rule is procedural. The sheet must name the levels and the dwells before the day. The levels must be fractions of a duty point you can cite, or values you explicitly accept responsibility for because no citation exists yet. Responsibility is allowed. Pretending the number came from a standard is not.

Dwell is part of the point. A flow you touched and left is not a flow you held. State the dwell in time, or state the criterion that ends the dwell: temperatures no longer changing in a way that would alter the heat story. The second form is harder to cheat and harder to write. Use it if you can say what “alter the heat story” means in the export. If you cannot, use a clock and be honest that the clock is a convenience.

Overload is not a second nameplate. It is a short visit above the rated set to see whether the unit stays stable and whether heat still leaves by the path you designed. It is not a license to publish a higher continuous rating. The limitations page should say the overload is a transient acceptance point, not a new nominal, unless you truly designed for continuous duty there. Most prototypes did not. Say so.

## High flow as a design driver

Why does flow regime change the machine, rather than merely changing a setpoint.

At higher flow, the same heat produces a smaller temperature rise. Sensors and records that were adequate for a large rise become arguments about noise. You may need the check method, the interval, and the dwell to be tighter, not because this book declares a new accuracy class, but because the story you are trying to tell got smaller. Write that risk on the sheet: “temperature rise at the duty flow may be small; do not accept the point on temperature alone.”

At higher flow, fittings, bends, and a half-closed valve dominate differential pressure. A unit that was “low pressure drop” at a gentle flow can become the dominant resistance at the rack flow, or it can cavitate, pull air, or collapse a hose that looked fine when empty. The liquid-path chapter is where you design for that. The duty chapter is where you admit it. Put “intended flow band” on the sheet even when the numbers are still a citation. A blank band is a reminder. A missing row is how the shop sizes for the heater and forgets the water.

At higher flow, maldistribution inside the unit matters more. Parallel paths that shared nicely at low flow will not share nicely when one path has a little extra hose. The heat-path chapter deals with modules and branches. Here, the duty consequence is: if you claim a single flow reading represents the unit, you must say that the internal paths are not separately loaded, or you must measure the branches you will separately load. A single meter on a header is a header meter. It is not a module meter.

None of this requires you to insert a liters-per-minute figure from a paper or a slide. It requires the duty sheet to treat flow as a driver of sensor choice, valve authority, and what “one reading” means. If your sheet has kilowatts in bold and flow in a footnote, you have built the gentle heater again, in prose.

## The window and the point

A specification window is a region: flows, temperatures, and pressures the rack side is allowed to see. An operating point is a place inside or on that region where you will sit. Acceptance visits several places. It does not “cover the window” by waving at it.

Pick the places for reasons. Nominal, because that is the claim. A reduced flow, because valve authority and meter behavior change there, and because some tests will ask for it. A high flow within the cited window, if nominal is not already there, because that is the regime you are afraid of. A supply temperature at the cool end and, if the window is wide, at a warm end, because density, viscosity, and heater surface temperature are not identical across the window. If you do not know whether the window is wide, the citation is unfinished. Do not invent a second temperature to look thorough.

Write a column called “why this place.” If the only answer is “to have more rows,” delete the row. Extra rows cost dwell time and create false failures.

## What changes when the revision changes

Interface specifications move. A field guide that embedded last year’s window would become a quiet lie. Your process has to be dull enough to survive that.

When a cited revision changes, someone rereads the duty set and marks each cell: still inside what we built, no longer inside, or unknown. Cells that are no longer inside do not auto-update. The unit does not grow a larger pipe because a PDF changed. You either accept a limitation (“this unit represents the previous window, not the current one”), or you modify the unit and re-accept the affected gates, or you stop claiming the stand-in. All three are honorable. Pretending the old acceptance still covers the new window is not.

Record the revision on the duty sheet itself, not in an email. The acceptance record cites the sheet revision. Two hops is enough to reconstruct history. Three hops, through a chat log, is how you lose.

## The loop you connect to on the day

Duty is about the unit. The unit cannot show duty if the loop on the day cannot absorb it. A bench loop with a small reservoir and a tired pump will overheat or run out of flow and you will condemn the prototype. Write, on the acceptance sheet, the minimum the temporary loop must provide: it must absorb the heat of the longest dwell, and it must be able to deliver the flow you intend to demand, at a pressure the unit is allowed to see. Those are setup requirements. They are not a second load bank. They stop you from running Gate 3 against a loop that made the test impossible.

If you do not know the temporary loop yet, mark it unknown with a date. Do not leave it implicit. Implicit loops are always assumed to be adequate, and they rarely are.

## Composite: the impressive nameplate

A shop builds a unit whose electrical nameplate is large. On the bench they run it at a modest flow because the bench pump is modest. Temperature rise is easy to see. Everyone relaxes. Months later the unit is asked to follow a rack-side flow that is several times the bench flow. Temperature rise shrinks into the noise of the sensors. Differential pressure across a restrictive internal path climbs. The same people say the rack specification is unrealistic. The unit was accepted against the wrong set. The nameplate did exactly what a nameplate does: it described the heaters, not the stand-in.

The fix is not a better adjective on the nameplate. The fix is a duty point written as a set, cited, and visited at that set before anyone calls the prototype done.

## Composite: the borrowed window

Another team pastes a table of flows and temperatures from a slide into the duty sheet and removes the slide’s title. The numbers are now “the standard.” A later revision of the real interface document moves a limit. The sheet still has the old numbers, and no one can say where they came from. Acceptance passes against the souvenir. The first real hookup fails a limit the souvenir no longer matches.

The fix is the citation column. Numbers without a title and revision are not a duty. They are a rumor. If you are not allowed to copy the numbers into a book, you are also not allowed to copy them into a sheet without the citation. The permission to use them on the project is not the same as the permission to detach them from their source.

## Electrical duty, briefly

The electrical feed must be able to support the highest step you will command, including the overload dwell if the overload is electrical and not only thermal. Record voltage and frequency as citations to what the hall, or the bench, will actually provide. Record whether the unit’s protection assumes a neutral, a ground, or a particular breaker behavior only so far as a wrong assumption would make the safe-state chapter false. Do not turn this into a power-system study. Do notice the common cheat: thermal acceptance run from a temporary feed the hall does not have. If the delivered unit needs a different feed, the power interface line is not accepted.

## Steady state, step, and trip

Give the duty sheet three kinds of rows, so people stop arguing about which kind a number is.

Steady rows are the set at a plateau, after the dwell criterion. Step rows are the command to move, and what must be true during the move: no trip, no stale data, flow not collapsing unless the step was a flow step. Trip rows are not duty in the sense of output. They are the conditions under which duty must end. Put a pointer to the safety chapter rather than inventing trip values here. If a trip value is in the cited specification, cite it. If it is your choice, label it as your choice.

This separation keeps overload from being used as a steady rating, and keeps a trip setpoint from being used as a performance target. Targets and limits are different directions. A unit that runs best at its trip point is a unit you do not understand.

## What NVIDIA publishes on the data-center site

Read on 11 October 2026 from https://www.nvidia.com/en-us/data-center/ and the product pages linked from it. These are NVIDIA’s pages. The sentences below are a short extract of configuration facts that bear on a load bank. They are not a copy of the pages, and they are not an interface specification.

The site is a catalog. It describes accelerated computing, AI factories, networking, and rack products. It does not, on the pages read for this draft, publish the coolant flow, supply temperature, differential pressure, or fitting family a load bank must meet. Those cells stay blank until the datasheet or the rack specification then in force fills them. Do not invent them from the catalog.

Two rack pages are the ones this book can use.

GB200 NVL72, product page https://www.nvidia.com/en-us/data-center/gb200-nvl72/. NVIDIA describes it as rack-scale and liquid-cooled. The published configuration is 36 Grace CPUs and 72 Blackwell GPUs, one NVLink domain. The same page’s specification table, which you should re-read rather than trust this sentence if the page has moved, lists 13.4 TB of HBM3E, 17 TB of LPDDR5X, 130 TB/s of NVLink bandwidth, and 2,592 Arm Neoverse V2 cores. A datasheet is linked from that page. Performance multiples against H100 are on the page. They are not duty. They do not enter a plateau.

GB300 NVL72, product page https://www.nvidia.com/en-us/data-center/gb300-nvl72/. NVIDIA describes it as fully liquid-cooled and rack-scale: 72 Blackwell Ultra GPUs and 36 Grace CPUs. The specification block on that page lists 130 TB/s NVLink bandwidth, 37 TB fast memory, 20 TB GPU memory, 17 TB LPDDR5X, and the same 2,592 Arm cores. A Blackwell Ultra datasheet is linked from the page. The 50x and 30x figures on that page are projected performance claims. They are not heat, flow, or pressure.

Vera Rubin NVL72 is listed on the same catalog as a later rack-scale product. Cite it only if that is the generation you are standing in for. Do not assume its liquid interface matches GB200 because the name still says NVL72.

What this does to the duty sheet is narrow. The stand-in is liquid, not air. The unit represents one rack of the generation you cite, not the building, not the network, and not the GPU’s FLOPS. Memory bandwidth and NVLink bandwidth are not coolant flow. A load bank that can match a published FLOPS number and cannot tell you flow and both temperatures has not met this chapter. Write the generation name and the page date on the duty header. Leave flow, temperatures, and differential pressure for the datasheet revision you are allowed to use.

Other links on the catalog, and why they stay out of the heat story: the data-center GPU line card, the qualified system catalog, and NVIDIA-Certified Systems, for identifying a server, not for sizing a hose. MLPerf, for workload benchmarks, not for a thermal plateau. Mission Control, for factory operations software, not for the local stop. Spectrum-X, Quantum InfiniBand, and BlueField, for the network, which this book does not accept. MGX, as a modular server reference, only if the interface owner says the rack you will mate to is an MGX liquid-cooled variant. DSX, as a cost-per-megawatt story, is not a kilowatt into your liquid.

## Public sources for this chapter

The duty set stays blank until a cited revision fills it. NVIDIA’s public page establishes the class: liquid-cooled, rack-scale, not a gentle air load. The datasheet linked from that page is the place interface numbers would live, if you are allowed to use them on the project. Do not copy marketing multiples from the page into a cell. A factor against an older platform is not a flow and not a temperature. ASHRAE thermal guidance, in whatever edition you are licensed to read, is where classes and recommended environments are defined. Those classes are not reprinted here. If your duty cites an ASHRAE class, the citation includes the edition, and the numeric window stays on the project sheet. ANSI/ASHRAE 90.4 is an energy standard for data centers. It does not set the load bank’s plateau. Do not let a hall energy claim migrate into this duty set.

## Decisions to record

- The nominal set: heat into the liquid, flow, differential pressure, supply temperature, return temperature, electrical power. Each cell cited or marked unknown.
- Why each place you will visit is on the sheet, including the overload dwell.
- Which side of the boundary each liquid quantity is read on.
- The false story each missing quantity would tell.
- What the temporary loop must absorb and deliver on acceptance day.
- The revision-change rule: limitation, modification, or stop the claim.


# 3. The liquid path

The liquid path is where a confident heater becomes a prototype that cannot be hooked up, cannot be isolated, or cannot be believed. Heat can be added in more than one way. Liquid only goes where you left it a path, and it only stays there if the joints, the valves, and the hose routing were treated as the design rather than as plumbing to be figured out at the end.

This chapter is a set of choices. It is not a parts list. Fitting families, sizes, and materials callouts come from the specification then in force and from the coolant you actually have. What this chapter insists on is the job each choice does, the failure it is meant to prevent, and the acceptance check that proves you did not skip it.

## Draw the boundary first

Before you sketch a pipe, draw the line where the load bank ends and the rest of the world begins. For this book, that line is the rack-side interface: the manifold, or the hose that mates to the manifold, depending on who owns the hose. The load bank does not include the CDU. It does not include the hall piping. It does not include a temporary bench loop, even if the prototype spends its first month bolted to one.

Write one sentence: “Delivered scope ends at X. The mating half of X is owned by Y.” If you cannot name X and Y, every later argument about a leak will be an argument about responsibility, which is a worse place to discover the boundary than a diagram.

Put the sentence on the one-line diagram. The diagram has boxes, arrows, and names. It does not have a site plan, a room number, or a vendor logo. It should be redrawable by a stranger from the prose in the delivery file. If it cannot be redrawn, it is a picture, not a diagram.

Name the streams. Supply into the load. Return out of the load. Any bypass that exists so flow can be trimmed without starving the CDU connection. Any drain or vent. If a stream does not have a name, someone will measure the wrong one and label it with the right word.

## Primary side and secondary side

Liquid-cooling conversations mix two loops until everyone is nodding at different machines. Separate them in the first paragraph of your diagram notes.

One side is the heat-rejection side: the side that ultimately dumps heat, often through a CDU’s heat exchanger to some other liquid or to air. The other side is the rack side: the liquid that would have gone through the IT equipment, and that your load bank is pretending to be. The names “primary” and “secondary” are used differently by different vendors. Do not inherit a vendor’s habit without writing your own glossary line. Pick “CDU-side” and “rack-side” if the inherited words are already confused in your project. Consistency inside your file beats fidelity to a slide.

The load bank in this book sits on the rack side of that boundary. It presents heat and resistance to whatever is supplying rack-side liquid. It is not a substitute for the CDU’s heat exchanger, pumps, or controls. If your prototype has its own pump, say so, and say whether that pump is only for bench acceptance or part of the delivered stand-in. A pump that quietly becomes “the” flow source will make every flow reading in the shop unrepresentative of a rack that expects to be fed.

If the project also needs a load on the CDU-side loop, that is a different requirement line and usually a different machine. Do not stretch this unit across both sides because the purchase order had one line item. Two duties on one chassis, unlabeled, is how a valve meant for isolation becomes a valve that starves the wrong loop.

Write, under the diagram: which side this unit occupies, what feeds it, and what it is not allowed to replace. Three sentences. If you need a page, you have not drawn the boundary. You have started a system description, which belongs in the project book.

## Isolation

Each external connection that can spill a loop needs a way to shut it off. A quick disconnect is a joint. It is sometimes also a valve. It is not, by itself, a maintenance plan. The first time you must remove a hose that is still full, you will learn whether you designed isolation or hoped for it.

Isolation has a place, a direction, and a visible state. Place: close enough to the point of spill that the trapped volume is small, and far enough from the joint that you can actually get a hand on it when the hose is fitted. Direction: you know which side stays live when it closes. Visible state: a person who did not build the unit can tell open from closed without a manual. If the state is invisible, acceptance treats it as unknown, and unknown is not open.

Two connections, supply and return, mean two isolation duties. A single valve in a shared location that does not exist is a common sketch. Do not let the sketch survive. Also isolate any spare port. A spare that cannot be shut is not a spare. It is a second leak.

Drains and vents are isolation problems in miniature. A drain that is a plug, with no valve and no captive cap, will be opened at the worst moment because it was the only way to empty the unit. A vent that cannot be closed will become an air leak or a spray. Write drain and vent as named devices with a closed state, or write that the unit is not meant to be drained except by breaking a joint, and accept that limitation in the file. The limitation is sometimes honest for a sealed module. It is rarely honest for a prototype you will service.

Acceptance for isolation is physical, not documentary. Close the valve. Confirm the downstream side can be opened without a continuous spill. Confirm the label matches the diagram. If you cannot do this without filling the entire hall loop, do it on the bench before the unit and the hall are inseparable. Gate 1 exists for this. Do not postpone it to a day when the loop is chemically treated and politically sensitive.

## One in service, one spare

A single external fitting is a single point of delay and a single point of damage. The pattern worth stealing from real load-bank specifications is not a size. It is the pattern: one connection in service, one held as spare, same duty, able to be brought into service without redesigning the manifold on the truck.

Say what spare means, because the word is cheap.

A capped port on the unit manifold, same family as the live port, isolated, labeled, and reachable. This is the minimum that deserves the word.

A second hose already fitted and capped at the far end. More ready, more able to kink, more able to be mistaken for the live hose. If you choose this, labels and caps are acceptance items, not accessories.

A spare fitting in a bag in a drawer. That is a spare part. It is not a spare connection. Do not write it on the diagram as if it were plumbed.

The spare must see the same duty if it is placed in service: same isolation, same instrument story, or a written limitation that the spare path is uninstrumented and therefore only a recovery path, not a test path. People will test on the spare if the live port is damaged. If the spare has no flow meter and no temperatures, they will do it anyway and the record will lie. Either instrument the spare path or write, in large letters, that a test on the spare path is not a valid acceptance and not a valid stand-in.

Who may change from live to spare. On the day, the default is: nobody, unless the acceptance sheet names the person and the retest that follows. Changing ports changes the hydraulic path. A quiet swap is a different unit.

## Hose workmanship

Soft hose is not a license to ignore routing. A hose that meets the fitting family and folds flat behind the chassis is a failed hose, even if it has never leaked. Kinks restrict flow, create a pressure drop you will blame on the rack, and fatigue the liner. Rub points wear through. A bend tighter than the hose can live with will look acceptable empty and wrong when pressurized.

Specify routing as a set of prohibitions and one positive statement. Prohibitions: no kink, no rub on an edge, no reliance on the connector to carry the hose’s weight, no loop that traps air at the high point you forgot, no run that blocks the module you said must come out. Positive statement: the hose length and path are fixed enough that two people will route it the same way. “Field fit” without a path is how every unit becomes a unique hydraulic accident.

Hose length is a design choice. Too short and the unit must sit in a place that conflicts with the rack. Too long and the spare loop becomes a heat exchanger and a trip hazard. Write a maximum unsupported length and a maximum total length as project numbers, or mark them unknown until the manifold location is known. Do not copy a length from another hall.

The elastomer, or metal, must be compatible with the coolant and with the temperature the duty sheet allows. Name the material class on the unit’s file and cite the coolant. Do not name a catalog hose from a previous job and assume the coolant is the same. Coolants are not interchangeable just because they are wet. If you do not know the coolant, the hose material cell stays unknown, and Gate 1 cannot close. That is correct. Shipping a hose of unknown compatibility is not a way to keep schedule.

Clamps and ferrules are part of the hose, not part of the decoration. A joint that depends on a clamp must have the clamp visible and of the type the hose maker requires. Acceptance includes a look, not a tug that damages the joint. If the joint is a type that should not be tugged, write the check as visual and as a pressure test, not as heroics.

Air in the hose is a measurement problem as well as a flow problem. A high point without a vent will collect air, the pump will sound wrong, and the flow meter will read a mixture. Walk the routed hose and mark high points. Either vent them or route them out. This is a Gate 1 and Gate 3 issue. It is cheaper on Gate 1.

## Interference

Static acceptance exists because drawings and chassis disagree in the real world. The check is practical. With hoses, valves, sensors, and connectors fitted, can a person reach every isolation device, close it, and remove a module without dismantling the loop. Can the unit sit at the distance from the manifold that the hose length assumes, without the enclosure striking the rack, the floor, or the door of the CDU. Does the display, if it has one, face the person who must read it, or does it face the wall the rendering never included.

Interference is not only metal-to-metal. It is hand-to-valve. A valve that meets the drawing and cannot be turned while the hose is on has failed. It is eye-to-label. A label that exists and cannot be read with the hose fitted has failed. It is tool-to-fastener. A module you said could be removed, which requires a driver that does not fit between the hose and the frame, has failed.

Do these checks empty, then again at pressure if the hose grows or stiffens when filled. Hoses change shape. A check done only on a CAD model is a wish. A check done only empty is incomplete. You do not need a hall to do the filled check. You need caps, a pump, and honesty.

Record interference as a list of reaches, not as “layout OK.” Reaches: supply isolation, return isolation, spare cap, drain, module release, power disconnect, alarm silence if it is local. Each is pass or fail. A narrative paragraph will hide the one reach that failed.

## What fittings are for: Danfoss FD83 vs. blade-level couplings

You will be asked to pick a fitting early, usually by being shown whatever quick disconnect was left over from a previous server build. Refuse that inheritance. Pick the hydraulic job, understand the scale of the interface, and then let the specification name the family.

In data center liquid cooling commissioning, people often confuse two completely different connection tiers:
1. **Blade-level couplings (such as OCP UQD02/04/08)**: Designed for low-flow server blades, compute trays, or blind-mate chassis nodes. They handle modest flows (typically 2 to 15 LPM per tray). They are compact, but their internal flow orifices present high restriction if forced to carry whole-rack volumes.
2. **Rack-level manifold test couplings (such as Danfoss FD83 series)**: In temporary testing and prototype validation of NVL72-class racks—where bulk flows reach 150 to 200+ LPM—the prevailing industry standard is the **Danfoss FD83 series dual-interlock full-flow quick disconnect** (commonly in 1-inch or 2-inch body sizes, such as FD83-2051).

The Danfoss FD83 series solves two catastrophic field failure modes through physical mechanics:
- **Mechanical dual interlock**: The coupling cannot be disconnected while internal fluid is pressurized or flow is engaged; and the internal ball valves cannot be opened until both halves are fully mated and locked with the mechanical pin. This eliminates accidental, high-pressure coolant release inside a live data hall.
- **Full-flow low pressure drop (C_v)**: Unlike spring-loaded poppet designs that choke at high velocities, the FD83 provides a straight-through flow profile with a high flow coefficient (C_v).

The fluid head loss across the load bank manifold, internal piping, and quick disconnect couplings is governed by the Darcy-Weisbach equation:

$$\Delta P = \left( \lambda \frac{L}{D} + \sum \zeta \right) \frac{\rho v^2}{2}$$

Where:
- ΔP is the total pressure drop across the load bank (Pa).
- λ is the Darcy friction factor.
- L is internal pipe length (m), and D is hydraulic diameter (m).
- $\sum \zeta$ is the sum of local resistance loss coefficients (quick disconnect couplings, 90° elbows, tees, and heater element bundles).
- ρ is the coolant fluid density (1020–1050 kg/m³ for water/glycol mixtures).
- v is the mean coolant velocity (m/s).

Across a pair of Danfoss FD83 couplings (C_v ≥ 12.5–15.0) at rated rack flow (176.5 L/min), coupling head loss is approximately:

$$\Delta P_{\text{couplings}} = \frac{\rho}{2} \left( \frac{Q_v}{C_v \times 1.156 \times 10^{-4}} \right)^2 \approx 28\text{--}35\,\text{kPa}$$

This preserves low overall circuit impedance, leaving the bulk of allowable pressure drop available for the modulating trim valve and heating chamber.

If someone hands you a blade-level UQD adapter hose to connect a 120kW whole-rack load bank, reject it at Gate 1. Choking a 180 LPM stream through an undersized coupling creates an artificial hydraulic pressure drop of hundreds of kilopascals, starves the heater core, induces pump cavitation in the CDU, and corrupts the entire rack resistance curve.

A clamped sanitary-style joint (such as DN32 Tri-clamp) solves a clean, inspectable, high-integrity internal connection that is not meant to be snapped daily. Its failure modes are an incompatible elastomer gasket, a clamp not seated uniformly, or a ferrule warped by overtightening. If you need daily make-and-break on the test floor, use Danfoss FD83 with tethered dust caps. If you need internal modularity, use sanitary clamps.

Isolation valves and modulating trim valves solve different problems. Do not combine them unlabeled. Isolation valves (full-port ball or butterfly) must provide zero leakage and visible handle status. Modulating trim valves (motorized linear TCV) must have sufficient valve authority across the entire operating window without needing to choke into a cavitation regime. (See Figure 02 for the full P&ID layout, including the relative placement of isolation, trim, and instruments).

## Pre-commissioning flushing and the 50-micron bypass strainer

Strainers and filters solve dirt. In liquid cooling commissioning, they also solve why a brand-new GPU cold plate in an adjacent production rack gets clogged with welding swarf.

A load bank is a nomadic test instrument. It travels between dirty construction sites, storage warehouses, and pristine commissioning data halls. If a load bank ships with uncleaned pipes, internal metal shavings, or microbiological slime, connecting it directly to a secondary CDU loop will inject that contamination straight into the secondary manifold.

The load bank must incorporate a dedicated pre-commissioning flushing bypass loop (see V-105 on the P&ID in Figure 02):
1. **End-capping at the shop**: Wetted pipes must be clean 304 or 316 stainless steel, chemically passivated, dried, and hermetically capped before leaving the factory.
2. **Two-stage flush before heat**: Prior to running Gate 3 heat runs on any facility loop, liquid must first circulate through the load bank’s internal 50-micron inline bypass strainer while the main heater core is isolated.
3. **Differential pressure check**: The bypass strainer must feature a differential pressure gauge or visual flag. If the strainer collects construction debris during the initial cold wash, clean it before opening the main heater elements.

If you omit the flushing bypass loop, loop cleanliness remains an unverified assumption. In a high-velocity NVL72 secondary loop, an unverified assumption is a fast way to foul a multimillion-dollar facility.

## Fill, vent, and the first liquid

The first fill is a designed procedure, not a folk skill. Write it as a sequence the acceptance sheet can point to. Where liquid enters. Which valve is open. Which vent is open. How you know the unit is full. How you know you did not trap air in the heater branch. What you do with the liquid you spill, in the sense of “there is a container,” not in the sense of a site environmental plan. The project book can hold the hall rules. This book only insists the prototype is not filled by forcing a connection and hoping.

A unit that cannot be filled without a special tool that is not in the delivery file is a unit that will be filled wrongly. Put the tool in the file, or change the vent.

Hot liquid and cold fill are different events. Filling with cold liquid and then heating is normal. Filling with liquid that is already at the top of the window, into a unit that has not been leak-tested at that temperature, is how gaskets surprise you. Leak-test at a pressure you cite, at a temperature that is not only ambient, if the duty window is hot. If you cannot do the hot leak test yet, write the limitation and do not claim the full window.

## Pressure, in the liquid sense

The duty chapter asked for differential pressure as a quantity. The liquid path must be able to survive the absolute pressures as well, including the case where a valve is closed and a pump elsewhere is not. A load bank that is happy as a flow-through device and bursts as a dead-head device is not finished. You do not have to publish a bar rating here. You have to ask: what is the highest pressure the cited loop can apply to a closed valve on this unit, and is every component in the trapped section rated for that, including the hose, the gauge, and the heater shell.

Dead-head is also a thermal event. Heat into a closed volume is how overtemperature and overpressure arrive together. The safe-state chapter will say heat must come off. The liquid chapter must not make a trapped volume the normal path. If a valve arrangement can trap the heater between two closed valves, interlock it or alarm it or remove that arrangement. “Operators will know” is not an interlock.

## Sensors in the liquid

Temperature and pressure sensors are part of the liquid path because their taps change the path. A boss, a tee, a thermowell, a long impulse line: each can leak, trap air, or read a pocket. Put taps on the diagram. Short impulse lines. High points vented. Thermowells in the stream, not in a stub that leaves the stream. A stub will read last hour’s temperature and you will tune to it.

Flow meters need upstream and downstream calm, or they need a type that does not, and you must know which you bought. A meter jammed against an elbow will be repeatable and wrong. Repeatable wrongness is the dangerous kind, because acceptance will “pass” the comparison once and then every later hour will share the bias. If you cannot provide the meter’s required straight length inside the chassis, relocate the meter or choose a different type before Gate 3. Do not calibrate the bias in and call it the rack.

Every tap needs isolation if removing the instrument would spill the loop, unless the instrument is welded and the limitation says it is not serviceable. Serviceable instruments that spill the loop will not be serviced. They will be left failed, and the failed reading will be used.

## What a vendor liquid-load specification actually contains

The working file has vendor specifications for liquid load units, one smaller and one larger. They are product documents, not a standard, and they are not reprinted here. What they contain, and what your sheet should therefore be able to say, is this.

The wetted pipe is a named metal, not “metal.” In those specifications it is a stainless grade, stated, not implied. Before the unit leaves, the inside of the pipe is cleaned and the ends are capped, so the first fill is not a flush of machine chips into someone else’s loop. If your unit cannot say what the pipe is, and cannot say that it shipped capped and clean, Gate 1 has nothing to look at.

The external joint is a family, with a default and a note that another family can be made. The default in a vendor document is not your mating family. Your mating family still comes from the rack specification then in force. The useful pattern is that the joint is named, and that a change of joint is a revision, not a hose-shop surprise.

Isolation sits at the ports. Flow can be indicated, not only inferred. A larger unit in that file is specified with one connection in service and one held ready, and with valves you can close without breaking the joint. That is the spare and isolation pattern already in this chapter, seen in a real specification rather than only as advice.

Each unit is run with power and with water before it is called finished, long enough that a cold leak and a hot joint have a chance to appear. Their text uses a run of at least half an hour. Use that as the shape of a factory line: water in, heat on, dwell, look, record. Do not copy their voltage, their clamp size, or their flow band into your duty cell. Those numbers belong to that product. Your cell cites your interface, or it stays blank.

A medium-voltage load bank manual for a generator test is also in the file. It is a different machine. It heats air, or a resistor stack, to load a generator. It does not stand in for a rack liquid loop. Do not borrow its wiring diagram to finish a liquid unit.

## Corrosion, dirt, and what you will not pretend to cover

Coolant chemistry can destroy a unit that passed a water test. This book does not become a chemistry manual. It does require the materials list, hose, seals, metals in the wetted path, to be checked against the coolant in the cited specification. The check is a row: materials listed, coolant cited, incompatibility none found by the person who owns the interface, date. If that person will not sign, you do not have compatibility. You have a hope.

Dirt is similar. A cleanliness requirement you cannot test is a slogan. Either specify a flush and a sample method you will actually run before Gate 3, or specify a strainer and an inspection, or write that cleanliness is assumed from the bench loop and is not a delivered claim. Assumed cleanliness must not be resold later as a finding about the hall.

## Composite: the spare that was a hole

A prototype drawing shows two ports. Only one is piped. The second is a boss with a plug, added so the drawing matches a sentence someone liked. At acceptance the plug is called the spare. It has no valve, no hose, and no path through the heat section. The sentence “one in service, one spare” is technically true and practically false. The fix is the definition earlier in this chapter. If it is not plumbed to the same duty, it is not the spare connection. Call it a plug, and stop taking credit.

## Composite: the hose that passed empty

Another unit is accepted in a shop with the hoses coiled on top, empty, because the manifold was not there. The coil looks neat. On site the hoses are forced down the side of the rack. One flattens. Flow collapses at the high end of the band. Temperatures rise. The heaters are blamed. The flattened hose is visible to anyone who looks, and invisible to anyone staring at the power display. Gate 1 with the routing you will actually use, repeated at pressure, would have caught it. A coil on a bench is not a routing.

## What design may decide, and what it may not

Design may choose the chassis, the exact bend, the brand of valve within the job you specified, and the way cables are dressed, provided dress does not create a kink or block a reach. Design may not delete isolation to save a fitting. Design may not convert the spare into a plug and keep the claim. Design may not move a sensor into a stub because the stream was crowded. Design may not add an adapter that changes the mating family and hide it in a note. Those are requirement changes. They go through the revision rule.

If a fabricator tells you the isolation valve will not fit, that is useful information. The answers are: change the envelope, change the valve geometry, or change the requirement in daylight and lose the claim you can no longer support. There is no fourth answer called “it will be fine.”

## Public sources for this chapter

Publishers do not agree on the words primary and secondary, and the words move between editions. This book keeps rack-side and CDU-side. Rack-side is the closed loop that would have served the IT. CDU-side is the building heat-rejection loop. A heat exchanger is the usual boundary, because building water and rack water are not assumed to be interchangeable in chemistry, dirt, or temperature. That is an engineering boundary, stated in this book’s words. The ASHRAE TC 9.9 liquid-cooling titles, the water-cooled server material, and the Datacom Encyclopedia are where you check the current published names and the current guidance on water quality and materials. Read the edition you are licensed to read. Do not paste its tables into the diagram notes. Write a one-line glossary: their word, your word, edition. If you skip the glossary, a fitting specified for one loop will be bought for the other.

Open Compute Project liquid-cooling specifications, if the interface owner has adopted one, are cited by version and used under that license. They do not override the rack specification then in force unless the interface owner says they are that specification.

## Decisions to record

- The boundary sentence and the one-line diagram, with streams named.
- Which side of the CDU boundary the unit occupies, and whether it includes a pump.
- Isolation devices, including spare, drain, and vent, with visible state.
- What “spare” means, and whether a test on the spare path is valid.
- Hose routing prohibitions, material class against cited coolant, and the reaches Gate 1 will touch.
- Fitting jobs, with families left as citations. Adapters drawn, not implied.
- The fill sequence, and the trapped-volume case you have designed out or interlocked.
- The materials-versus-coolant row, signed or explicitly open.


# 4. Heat path and modules

Heat is the product. The liquid path only carries it. Treat them as separate designs that must agree at the duty point. A beautiful manifold with a heater that can only be off or on is a valve assembly. A large heater with no honest path for the heat into the moving liquid is a room heater that happens to have fittings.

This chapter decides how heat is divided, how it is stepped, how a sudden increase works, how a module comes out, and how a fault stays local. It does not decide a module kilowatt map from any prototype you have seen. Those maps are project residue. The patterns are not.

## Where the heat has to go

Every watt you command has a destination. Into the liquid stream you are measuring. Into metal that will later give the heat back, which is storage, not delivery. Into the room, through the case. Into a pocket of liquid that is not in the measured flow. Acceptance cares about the first. The others are errors, delays, or losses. You do not need a calorimeter laboratory to respect the distinction. You need the habit, already stated in the duty chapter, of comparing electrical power with the heat story in the liquid after a dwell.

Design follows that habit. The heat-producing surface must see the stream you measure, not a side branch, not a tank that mixes slowly, not a plate that faces air on one side and a trickle on the other. If the geometry cannot put the surface in the stream, change the geometry before you argue about controls. Controls cannot push heat into a liquid that is not there.

Thermal mass is not free realism. A heavy block will make every step look slow and will make overload look safe for a while, because the metal is absorbing what the liquid has not taken. If your stand-in is supposed to present heat promptly, mass is a distortion. If your stand-in is supposed to resemble a rack’s thermal inertia, mass is a claim, and it must be written as a claim with a reason. Do not let mass happen because the element vendor sold a thick assembly. Write whether fast response or inertia is the goal. For a load bank whose job is to exercise a cooling chain, fast and measurable usually beats accidental inertia. Accidental inertia hides failed flow.

## Thermal power balance and fluid specific heat: PG25 vs. DI water

The fundamental thermodynamic truth of the load bank is the closed thermal power balance equation:

$$Q = \dot{m} \cdot C_p \cdot \Delta T = \rho \cdot Q_v \cdot C_p \cdot (T_{\text{return}} - T_{\text{supply}})$$

Where:
- Q is the thermal heat transferred into the liquid stream (kW).
- ṁ is the mass flow rate (kg/s), and Q_v is volumetric flow rate (m³/s or L/min).
- ρ is the coolant fluid density (kg/m³).
- C_p is the specific heat capacity (kJ/(kg·K)).
- ΔT = T_return - T_supply is the temperature rise across the load bank (K).

The physical properties of the coolant determine the flow regime required to absorb nominal power. In data center liquid cooling, secondary loops predominantly circulate either Propylene Glycol 25% by volume (PG25) or treated Deionized (DI) water:
- **PG25 Coolant (@ 40°C mean bulk)**: Density ρ = 1025 kg/m³, Specific Heat C_p = 3.980 kJ/(kg·K).
- **DI Water (@ 40°C mean bulk)**: Density ρ = 992 kg/m³, Specific Heat C_p = 4.179 kJ/(kg·K).

Because PG25 has an approximately 5% lower specific heat capacity than pure water, absorbing a 120.0 kW thermal load across a 10.0 K ΔT requires a mass flow rate of 3.015 kg/s (176.5 L/min for PG25) compared to 2.871 kg/s (172.2 L/min for DI water). 

If a test operator assumes pure water constants (4.18 kJ/(kg·K)) while circulating PG25, the calculated thermal heat will overestimate reality by ~5%, generating an artificial discrepancy in the electrical-to-thermal balance. Every calculation on the acceptance sheet must cite the specific fluid mixture and its temperature-dependent properties.

## Steps are plateaus, not a knob

You need stepped heat. Commissioning and acceptance both need to see the machine move through fractions of the duty point and sit there long enough to be believed. Name the plateaus on the sheet before anyone sizes contactors: a low step, a middle step, a high step, full, and zero. You may add one more if a real test needs it. You may not add ten because the controller has a percentage field.

Each plateau needs a definition that does not depend on the display’s mood. Prefer: this plateau is a commanded electrical power, and it is valid only when the liquid set is inside the band you cited for that plateau. If you have no bands yet, the plateau is still a commanded power held for the dwell, and the liquid set is recorded rather than judged. Recording without judging is acceptable early. Judging without recording is not. Calling a knob position a plateau is neither.

Dwell belongs to the plateau. State it. A dwell that ends when someone gets bored will be short on the day the truck is waiting and long when a demonstration is going well. Neither is a measurement.

The return to zero is a plateau of its own. Heat command at zero, flow still readable, temperatures coming down for a reason you can see. A unit that cannot sit at zero without being powered off entirely may still be acceptable, but then “zero” means “safe off,” and the sheet must say that a planned zero and an emergency stop are the same state. If they are the same, you cannot take a zero-load hydraulic reading without a special arrangement. Write that limitation or give yourself a true zero-heat state with pumps and valves still in the test condition.

## Sudden increase

Plateaus prove you can hold. A sudden increase proves you can move without a secret ramp that the operator cannot bypass. Cooling controls in the real test may be judged on how they react to a change. A load bank that only creeps will never present that change. Specify one increase, from a named plateau to a higher named plateau, with a command that is fast relative to the thermal response you care about. You do not have to publish a millisecond. You have to say “not a slow ramp,” and you have to say what slow means in your sheet: for example, the command reaches the new value before the liquid temperatures have finished moving. If the command itself takes as long as the thermal settling, you did not buy a sudden increase. You bought a second ramp.

The sudden increase is not an invitation to slam the unit into a trip for sport. The destination plateau must be one you are allowed to hold. If you want a pulse above rating, that is the overload visit, with a dwell and an exit, not an unnamed slam.

False compliance: a software slider with an animation, while the contactors stage on over a long stagger that nobody documented. Staging can be good electrical practice. Hidden staging is a ramp. Document the stage times. If the sum of the stage times is the thermal time scale, call it a ramp and stop calling it sudden.

Evidence: the export shows the command jumping, then the power, then the temperatures, on one timeline. If those three are in different files with unsynchronized clocks, you do not have evidence. You have three stories.

## Modules

Modules are how you get steps, redundancy, and service without a single element that can only be on or off. The rules that matter are service and fault containment. Brand does not matter. A kilowatt label from a previous unit does not matter.

A module should come out without moving its neighbors and without draining the entire manifold if you claimed that serviceability. If removal requires draining, say so, and put the drain procedure in the file. Hidden drain requirements are how modules are never removed and failed elements are left in the count. Acceptance includes a removal of one module, or a demonstrated equivalent if the module is behind a fitting you are allowed to break, done once, with the reaches from the liquid chapter still true afterward. If you reassemble and a reach is gone, the service demonstration failed.

A fault in one module should not become a fault in the loop. Open-element failure should remove that module’s heat, not short the feed to its neighbors. A leak at a module joint should be isolatable if you claimed isolation, or should be a declared “drain the unit” event if you did not. What you may not have is an undescribed third thing, where a leak forces a choice nobody wrote down while the heaters stay on.

The design bias is toward a safe state. Loss of control removes heat. It does not lock heat on. Loss of a module’s communication removes that module’s heat. It does not leave the last command latched unless the latch is a deliberate, local, visible state that acceptance has tested. Latched heat with a dead controller is a failure mode you must write a test for, or design out. Prefer design out.

How many modules. Enough to build the plateaus you named without depending on a single element for full load, unless you explicitly accept that a single element failure is a total loss of heat and you can still safely stop. Single-element full load is simpler and brittle. Several elements are more to wire and easier to step. Choose against the plateaus and the safe-state rule, not against a photo of someone else’s interior.

Balance among modules matters when they share a liquid path. If one module takes most of the flow and another takes little, equal electrical power is unequal surface temperature. The starved module trips or degrades while the header temperatures look fine. This is the maldistribution problem from the duty chapter, seen from the heat side. Either design the branches to share across the flow band, or measure the branches, or do not claim that header readings describe module health. A claim you cannot measure is a limitation. Write it. Do not discover it as a burnt smell.

## Grouping and what the later test must answer

One loop that represents a whole rack is simple. It is also blind to maldistribution inside the rack you are not actually testing. Several loops that represent groups of secondary paths tell you more and cost more valves, meters, and hoses. Pick against the question the later test must answer.

If the project book only needs “rack-side demand was present at the manifold,” one well-instrumented loop may be enough. Building six loops to feel serious is how budgets disappear into fittings. If the project must show that a manifold feeds more than one path, and that those paths can be loaded differently, the load bank has to present more than one path, with heat and flow authority on each path you will independently command. A manifold of dummy plugs is not a multi-path load. It is a costume.

Write the question in one sentence at the top of the heat-path section of your file. “This unit must let us command two different heats on two branches that share an inlet.” Or, “This unit is one branch, and any claim about rack internal distribution is out of scope.” Both are valid. The invalid state is three branches in the rendering and one heater in the chassis.

Each branch you will command independently needs the six functions, or a written subset. A branch with heat and no flow reading is a branch you will mis-tell stories about. If the subset drops a function, the drop is a limitation on that branch, and any test result from that branch inherits the limitation. Results do not outrank the sheet.

## Bypass, trim, and who is allowed to move flow

Heat and flow meet at authority. A load bank that can only reduce flow by closing the only path will fight the CDU, or will dead-head a pump, or will trip on temperature because the same valve that trimmed flow also trapped heat. Say, in prose, what is allowed to move.

A trim valve on the load bank, in series with the heat section, with a bypass around the heat section so total flow at the rack interface can stay high while heat-section flow is tempered. This is a real design, and it needs two flow stories or a clear statement that you only measure one of them. If you measure only total flow, you do not know the flow that touches the heaters. If you measure only heater flow, you do not know what the manifold sees. The duty set must say which flow is the stand-in flow. Preferably measure both if both can move.

A bypass that is fixed, not controlled, is a leak path for heat. It will make temperature rise look small. It is acceptable only if it is drawn, sized on purpose, and included in the heat story.

A request back to the CDU to change flow. Allowed as a project method. Not allowed as a hidden dependency of the prototype. If the unit cannot reach the flow band without a CDU command you do not own, the unit does not have adjustable flow. The CDU does. Put that in the limitations or change the unit.

No trim at all, flow set by the external loop, heat set by you. Also allowed, and often simpler, provided the external loop on acceptance day can actually set the flows, and provided you do not claim a flow adjustment the unit does not have. The requirements list in chapter 1 asked for adjustable flow. If you now decide adjustment lives outside the unit, revise that line. Do not leave both claims in force.

Write the authority sentence: “Flow at the interface is set by A. Flow through the heat section is set by B. Heat is set by C.” If A, B, and C are the same valve, say that, and accept the coupling as a limitation. Coupled authority means you cannot walk heat and flow independently. Some tests need to walk them independently. If yours does, one valve is the wrong design.

## Failure modes worth writing down

Full electrical power, little temperature rise. Either the flow is far above the point you think, or the heat is not in the liquid, or the temperature sensors are not in the stream. The response is not to add power. The response is to check the set: flow, sensor location, and whether a bypass is stealing the rise. Acceptance fails the plateau if the heat story does not match and nobody can explain the destination of the watts.

Temperature rise with collapsing flow. A blockage, a kink, a valve not where you think, a strainer you forgot, air. Heat should come off if flow collapses below the point you named as minimum for safe heat. That minimum is a protection, not a performance target. Name it or cite it. A unit that keeps full heat into a collapsing flow is climbing toward the overtemperature stop, and it may lose the race.

One module hot, neighbors idle, total power “correct.” Distribution inside the unit. Header readings will not see it unless a module sensor or a branch flow exists. If you have neither, you cannot claim module health. The failure mode then is: you will run this way for hours. The fix is a sensor or a limitation that forbids unattended full load. Prefer the sensor if full load is the product.

Trip with no alarm. You lose the test and the reason together. Already forbidden in the requirements. Repeated here because heat-path design often implements the trip in a contactor and the alarm in software that does not see the contactor. Wire the alarm to the thing that actually removed heat, or accept that the alarm is a rumor.

Heat on, command off. A welded contactor, a latched relay, a control power arrangement that back-feeds. This is the safe-state test. Command zero and kill control power separately. Both must end with heat off. If killing control power turns heat on, stop. That unit is not a prototype you are allowed to finish by writing a procedure. Change the circuit.

Slow leak of heat into the room. The liquid story almost matches, and the room gets hot, and someone “corrects” the heat balance with a factor. A factor can be an honest loss term if you measured it. A factor typed to make the spreadsheet close is fraud against yourself. Either measure case loss or keep the band wide enough that you are not pretending to a precision the case stole. Do not publish a fake efficiency.

Uneven steps. The middle plateau is not between low and high, because modules are unequal or because a stage failed and the controller still says the percentage. Evidence is measured power, not the percentage field. Put measured power in the export. A percentage with no watts is a request, not a result.

## Controls, only as far as heat requires

Control in this chapter has one job: make the plateaus and the sudden increase true, and make the safe state true. The next chapter will talk about data. Do not build a control system that needs the data chapter in order to turn heat off. Local, boring, and testable beats networked and clever for the stop path. The network may request a plateau. The network must not be the only thing holding the contactors open. If that sentence conflicts with a product your vendor likes, the product does not meet the requirement. Write the conflict down. Do not let a demo of a dashboard resolve it.

Manual mode matters. A person on the floor must be able to command zero without logging into anything. A local stop that only stops the display is not a stop. Label the local control with the plateaus you actually have, or with off and a request for remote. Unlabeled buttons become folklore.

Interlocks that belong here: no heat if flow is below the minimum you named, no heat if the isolation valves are closed, no heat if the liquid sensors required for protection are failed. Each interlock needs a behavior when the sensor that feeds it has failed. Failed flow sensor should remove heat, not bypass the interlock. A bypassed interlock is a jumper. Jumpers are not a mode. If maintenance needs a jumper, it is a controlled defeat, logged, heat inhibited or strictly limited, and impossible to leave in place without a visible tag. Acceptance tries to leave a defeat engaged and checks that the unit refuses to look normal.

## What not to draw

Do not put a fabrication drawing in the delivery file and call it the design basis. A drawing will freeze hole sizes and will not freeze the authority sentence. The authority sentence is more important. Do not publish a module map of electrical kilowatts copied from another unit. Do not publish a control schematic as a substitute for the safe-state test. Schematics can be wrong in the way that matters, which is the way wires actually run. The test is the authority. The schematic is a convenience if it matches the test.

Do not draw the CDU inside your heat path to make the picture look like a system. The moment the CDU is inside your drawing, people will assign you its failures. Keep the boundary.

## Composite: the percentage that lied

A controller offers one percent to one hundred. Acceptance sits at half because the script says fifty. Measured electrical power is nowhere near half of full, because half in the software is half the modules enabled, and two of those modules are failed open, and the software does not count watts. Liquid temperature rise agrees with the smaller power, not with the percentage. The unit is not necessarily unsafe. The plateau definition is wrong. Fix the definition to measured power, fix the failed modules, and stop writing scripts in percent until percent has a watt calibration you have checked.

## Composite: the fight with the feeder

A unit trims flow with the same valve that feeds the heaters, and has no bypass. At the high-flow end of the cited window the valve is nearly open and useless as a trim. At the low-flow end it is nearly closed and the heaters trip. The team adds a software ramp to “stabilize.” The ramp hides the fact that independent control of heat and flow was never possible. The authority sentence, written early, would have forced a bypass or a revision of the adjustable-flow claim. Software will not create a hydraulic path.

## Public sources for this chapter

NVIDIA’s public description puts the heat of this rack class in a liquid-cooled rack, not in an air-cooled chassis you can imitate with a room heater. That supports the grouping sentence: the unit stands in for rack-side heat. It does not support a module map, a kilowatt split, or a claim that your heater arrangement matches theirs. Do not open a datasheet and copy a power figure into the plateau list. The plateau list is measured power you will sit on, cited or chosen. ASHRAE material on IT equipment design and on cooling technologies can inform whether your mass and your response are a claim or an accident. Cite the title. Do not retell the chapter. The authority sentence remains yours. No white paper will write it for you.

## Decisions to record

- Where commanded heat is required to go, and whether thermal mass is a claim or an accident.
- The plateaus, the dwell, and the definition of a valid plateau.
- The sudden-increase test, distinct from a ramp and from overload.
- Module service and the fault that must stay local.
- The one-sentence question the grouping must answer.
- The authority sentence for interface flow, heat-section flow, and heat.
- The safe-state tests: command zero, and kill control power.
- Interlocks, and the behavior when their sensors fail.


# 5. Instruments, control, and the data exit

A load bank that cannot be read is a heater. A load bank that can be read only on its own door is a demonstration. The test you are building toward needs the same facts in a file as the person on the floor sees in the room. This chapter is about what is measured, where, how the readings share a clock, and what must be true of the exit path. It is not a register map. It is not a brand of monitoring software. Maps and brands rot. The duties do not.

## Two sets, or you cannot compare

On the unit, the minimum set is supply temperature, return temperature, supply pressure, return pressure, and flow. Those words match the duty set. If your diagram used different names, this is the moment to stop and make them match. Synonyms are how columns get swapped in the export.

On the rack side of the boundary, the same quantities need to exist as a comparison set, at least during acceptance and during any test where you will claim the stand-in behaved like the interface. People skip the second set because the unit already has sensors. Then every argument about a mismatch is unresolvable. The unit can be telling the truth about itself and lying about the manifold, because a hose, an adapter, or a mixing point sits between them.

The second set can be temporary instrumentation. Temporary is allowed. Impossible is not. The chassis, the hose routing, and the insulation must leave a place for a check probe and a check pressure tap, or you must have permanent rack-side points. Decide which. “We will figure out taps on the day” means you will not have them, and Gate 3 will be a local demonstration you over-interpret.

Write a column: unit point, comparison point, what difference is expected. Some difference is normal. A hose has loss. A sensor has bias. The column is not a demand that the numbers match to the last digit. It is a demand that you know which differences would change the story. A difference that changes the story is a stop until explained. An explained difference becomes a limitation or a correction you apply in public.

## Placement: Core immersion metrology versus dead-leg fraud

A sensor measures the thermodynamic microclimate of the exact spot where its sensing element sits, not the abstract stream in its software label. Supply temperature placed in a stagnant pipe stub measures the stub. Return temperature downstream of a bypass mix measures a mixture. (See Figure 03 for the detailed cutaway comparison of compliant core immersion versus dead-leg fraud).

To achieve valid metrology that survives mathematical scrutiny, four installation rules are non-negotiable:
1. **Core Stream Immersion ($1/3 \sim 1/2 D$)**: The thermowell tip must penetrate past the boundary layer and sit directly inside the high-velocity central core of the stream (between 35% and 50% of the pipe inner diameter). A shallow probe sitting flush with the pipe wall measures cold laminar boundary liquid and ambient metal conduction.
2. **Angle of Attack**: Angle the thermowell 45° upstream into the oncoming fluid flow. This maximizes convective heat transfer across the sheath, eliminates stagnant vortex wakes, and ensures rapid thermal response.
3. **Thermal Conductive Compound**: The annular gap between the RTD element and the inner thermowell sleeve must be packed with high-temperature thermal compound (zinc oxide/silicone grease). A dry thermowell creates an air-gap insulation barrier with a 30-second thermal lag, masking rapid transient spikes.
4. **Flush Deburred Static Pressure Taps**: Pressure taps for differential measurement (DPT) must be drilled perfectly perpendicular to the pipe axis, with inner edges completely deburred and polished flush. A tap drilled immediately downstream of a throttled butterfly valve or elbow sits in turbulent swirling eddies, converting dynamic velocity pressure into massive, fluctuating false static heads.

Protection sensors are not the same as recording sensors, even when they measure the same physical quantity. A protection sensor (such as a mechanical bimetal snap switch) must be fast, crude, fail-safe, and mounted directly on the heater element sheath. A recording sensor (such as a calibrated 4-wire Pt100 RTD) sits in the bulk stream to tell the true thermodynamic heat story.

## Industrial telemetry: Modbus-TCP, polling intervals, and quality flags

While the final acceptance package requires a flat CSV export for the stranger audit, modern data hall commissioning relies on automated supervisory platforms (such as Zabbix, DCIM, or PLC schedulers).

The load bank controller must expose a standardized, isolated telemetry interface (such as Modbus-TCP or Modbus-RTU over RS-485):
- **Discrete Coils**: Solenoid positions, heater contactor feedback, leak rope trip, E-stop circuit continuity.
- **Holding Registers**: Commanded kW, actual kW, supply temperature (0.01°C resolution), return temperature, flow rate (0.1 LPM resolution), supply pressure, return pressure.
- **Quality Bitmask**: A dedicated status register indicating sensor health. If a sensor wire breaks or a reading freezes, the controller must set the corresponding fault bit rather than echoing a stale value.

## Calibration tolerance classes and dual-sensor cross-checks

Metrology on acceptance day cannot rely on uncalibrated process gauges. Instruments must adhere to defined calibration tolerance classes:
1. **Temperature Sensors**: 4-wire Pt100 RTD elements conforming to IEC 60751 Class A (± 0.15°C tolerance at 0°C, ± 0.23°C at 40°C). Dual matched pairs must be calibrated together to ensure differential temperature measurement (ΔT) error remains ≤ 0.10 K.
2. **Flow Meters**: High-accuracy electromagnetic or Coriolis mass flow meters with factory-calibrated accuracy ≤ ± 0.5% of rate across the 50–250 L/min flow envelope. Vortex or turbine meters with ± 2.0% accuracy are acceptable only if straight-run piping requirements (10D upstream, 5D downstream) are strictly satisfied.
3. **Differential Pressure Transmitters (DPT)**: High-stability piezoresistive transmitters with ≤ ± 0.10% of calibrated span (e.g., ± 0.25 kPa on a 0–250 kPa span).

During Gate 2 and Gate 3, cross-checks between the unit's onboard sensors and the facility rack-side comparison probes must satisfy strict delta limits:
- **Temperature Cross-Check**: |T_unit - T_rack| ≤ 0.20 K.
- **Differential Temperature Delta**: |ΔT_unit - ΔT_rack| ≤ 0.15 K.
- **Differential Pressure Cross-Check**: |ΔP_unit - ΔP_rack| ≤ 5.0 kPa (after subtracting calibrated hose and coupling losses).
- **Flow Cross-Check**: |Q_unit - Q_rack| ≤ 1.0 L/min (or ≤ 1.0%).

Any variance exceeding these limits stops the gate until resolved. Never adjust sensor offsets in software to force arbitrary agreement.

## Clock and interval

The two sets and the electrical power must share a timeline. A temperature at one minute and a flow at four minutes are not a pair. You do not need a laboratory time service to meet this. You need one clock the export uses, a declared sample interval, and a way to see that a sample is missing rather than quietly repeated.

Missing versus repeated is the whole game. Many systems, when a read fails, hold the last value and keep stamping new times. The file looks dense. The process left. Any heat balance you compute from that file is fiction. The requirement is: a failed read is a failed read, marked, not painted over. If your platform cannot mark quality, do not use it as the acceptance record. Use something that can, even if it is humble, and demote the pretty platform to a display.

Declare the interval in the file. Faster is not always better. Faster than you can align is a way to fill disks and still mis-pair events. Slower than the sudden increase is a way to miss the only interesting moment. The interval must show the command jump and the plateau dwell with more than one sample on the dwell. If you have one sample on a dwell, you did not dwell in the record. You flickered.

Timestamp the command as well as the measurements. A record of temperatures with no record of what was requested is a weather log. You will not remember the request. The person who reviews the file next month was not in the room. The request is data.

## Four duties of the exit

Collect. The test platform can read the points without a person typing them off a panel. Typing is allowed as a backup for one gate, once, if the export path is broken and you are deciding whether to stop. It is not the design. If collection depends on a laptop that a single engineer must remember to start, the collection does not exist when that engineer is late. Start collection with the run, or make the run refuse to start. Prefer refuse.

Store. A run survives the end of the run. Power loss to the display does not erase the hour you just paid for. If storage is on the unit, say what happens when the unit’s storage fills: stop the test, overwrite oldest, or alarm and continue. Pick one. Overwrite without alarm is how evidence disappears from the front. Continuing with a full disk and no record is the same failure in slower motion.

Show. A person on the floor can see the live point and the alarm without the export. Floors are loud and bright. A tiny screen with a fault code is a show only if the code is in the file and the alarm is also a lamp or a line of plain words. Plain words beat codes. If you use codes, the code list is part of the delivery file, and an unknown code is itself an alarm condition, not a blank.

Export. The next book needs a file, not a photograph of a screen. The file has one row per time, or an equivalent that does not require a private tool to flatten. Columns have names, units, and a quality flag. A proprietary container that only one application can open is a hostage, not an export. You may keep a proprietary live protocol. You may not make it the only way out. Define the export as something a stranger can open in a ordinary table tool. If that sentence is painful, your architecture is showing off.

Identity of each point travels with the value. Unit of measure travels with the value. Timestamp travels with the value. Quality travels with the value. A documented failure travels with a stale point. Those four companions are the design principle. Everything else is implementation, and implementation may vary, and implementation does not get to drop a companion because the protocol makes it awkward.

## Valve position, leak, and other facts that change the story

If a valve can change the hydraulic story, its position is a point, not a decoration. At minimum the isolation valves and the trim or bypass valve, if they exist, need a state in the record when they are power-operated. Manually operated valves need a recorded check at the start of a run, because they will not update themselves. A run that begins without that check is not comparable to a run that begins with the valves elsewhere. Put the check on the acceptance sheet and on the later run sheet. This book only forces the acceptance version. The project book should steal it.

Leak or coolant detection belongs as an alarm if liquid leaving the path is a credible failure of this unit. It does not belong as a science project, and it does not belong as a substitute for isolation and for a person looking during Gate 1. A leak sensor that is not tested is a rumor. Test it the way the safety chapter says: a simulated input or a controlled wet test that does not soak the electrical section. Write the method. A method you cannot write is a sensor you do not have.

Level in a reservoir, if you have a reservoir, is the same kind of fact. A falling level with stable flow readings can mean a leak downstream of the meter or a deaeration event. Without level, you will misread both. If the unit has no reservoir, say so, and say where the expansion volume of the loop actually is. It is not nowhere.

Electrical power, voltage, and a current or a power reading are points, not just nameplate facts. The heat story needs power. A contactor auxiliary contact is a useful companion to power: command on and power at zero is an open element or a missed stage; command off and power above zero is the welded-contactor case. You do not need a power-quality study. You need enough electrical truth to know whether the heaters did what the heat command said.

## Alarms are sentences

An alarm must say what it is. Overtemperature, low flow, sensor fault, valve not in position, leak, storage full, export failed, control power lost: these are different events. A single red lamp is how acceptance becomes a debate about which fault was meant. Lamps may exist. They may not be the only text.

Each alarm has a source, a threshold or a discrete cause, a local indication, a record line, and an action. Action is one of: remove heat, stop flow authority, alert only, or inhibit start. Alert-only is acceptable for a storage warning and unacceptable for overtemperature. Write the action next to the name. If the action column is empty, the alarm is not specified.

Latched versus self-resetting is a choice. Protection alarms latch until a person resets them, so a trip is not erased by the condition going away. Informational alarms may reset. A protection that self-resets and then allows heat to return without a person is a heater that hunts through a fault. Do not build that unless you have a written reason and a limit on retries. Prefer latch and a local reset that does not require the network.

Alarm tests are part of acceptance, not part of the first real emergency. For each protection alarm, the sheet names the way you will cause it without destroying the unit. Simulated sensor. Controlled low flow with heat inhibited, then with a small heat, if that is safe. Open-door or jumper methods only if they do not bypass the very stop you are testing. If the only way to test overtemperature is to overheat the liquid past the limit, you have not designed a test, and you will skip it. Add a test input or accept that the protection is unproven. Unproven protection is a stop on the claim that the unit is safe to leave with heat available.

## Control duties, and no fifth duty

Control has four duties. Hold a setpoint that corresponds to a plateau. Step when asked, including the sudden increase. Remove heat on stop or on protection, including loss of control power. Leave a record of what it commanded and what it did. A control system that can do less is not finished. A control system that can also optimize a plant, forecast a price, or host a dashboard for visitors is out of scope. Extra scope that threatens the four duties is not a bonus. It is a risk. If the extra scope shares a processor with the stop path, you have coupled a toy to a protection. Separate them or delete the toy.

Remote command is allowed. Remote command is not the stop path. A local means to remove heat must work when the remote path is silent, wrong, or hostile. Hostile includes a stuck command to full load. The local stop overrides stuck remote command. Test that. A stop that politely asks the remote controller to stop is not a stop. It is a request.

Setpoint limits live in the controller and in the sheet. The controller should refuse a setpoint outside the duty you accepted, or outside a temporary override that is itself an alarmed mode. An open percentage field that can command beyond the tested plateaus will be used, in a hurry, beyond the tested plateaus. Refuse, or alarm and log, but do not be quiet.

Mode names should match the sheet. If the sheet says plateaus, the screen should not say “scenario B” unless the file defines scenario B as a plateau in watts. Undefined modes are how a unit ships with a demo mode that bypasses interlocks. Demo mode, if it exists, is heat-inhibited or it is not allowed to exist in the delivered software. Acceptance includes a hunt for heat that can be commanded with interlocks defeated. Ask the builder what modes exist. Then try to find one they did not mention. This is not hostility. It is how software ships.

## What you will not specify here

You will not specify a default network address. Addresses are commissioning facts. They go on the acceptance record as “identity as commissioned,” not into a book where they will be wrong and, worse, where they will be copied.

You will not specify a register map. The map is a project file. It must exist for your project if you use a bus, and it must match the points in this chapter, and it must be revision-controlled. It is not a design principle. The principle is the companions: identity, unit, time, quality. A map that delivers a number with none of those is a failed map even if the number is correct today.

You will not name a monitoring product. If the hall already has one, the collect duty can be satisfied by it, provided the quality and export duties are also satisfied. A product that can graph and cannot mark a stale point fails the exit, regardless of how common it is. Do not let familiarity substitute for the stale-data test.

You will not publish a point list from a site. Your point list is the functions in this chapter, plus any branch points your grouping sentence required, plus valve states. That is enough. A hundred extra points copied from a building design will bury the ones that can stop a bad heat story. Extra points are allowed after the minimum set is in the export and has been used in a real plateau. Not before.

## The command path that already exists

The working file has one page that is the control logic, and it is only one page. It is still the most concrete logic we have. Use it. Do not wait for a ladder diagram that is not in the file.

There are two sensor groups, and they are not optional duplicates. One group is the single load: supply temperature, return temperature, supply pressure, return pressure, flow. The other group is the rack side of the same boundary: the same five quantities. If you only build the first group, you can describe the heater. You cannot describe the stand-in. The page draws both. So does this chapter.

Above the sensors is a test platform with five jobs, in this order: collect, store, run a schedule, show, export. Collect is the read. Store is the file that outlives the screen. The schedule is a script, not a person clicking. Show is the live view. Export is what leaves the room. A platform that can show and cannot export has failed the page, even if the demo looked busy.

Two facts sit beside the temperatures because they change the story. Valve position, because a valve can be the hidden throttle. Leak or coolant detection, because a wet unit that still reports healthy flow is not healthy. They are alarms and records, not a research topic.

The bus on that page is Modbus, and the monitoring path is allowed to be Modbus or SNMP. That is a protocol family, not a register map and not an address. Do not publish a default address. Do not paste a site point list into the book. Do require that the points above can be read by the platform without a person typing them, and that a failed read is marked.

The command direction is the part people skip. A test task becomes a script. The script becomes a rack-level command. The rack-level command becomes the load bank’s on, off, and step. It does not become a suggestion on a local screen that someone may ignore. If the only way to change heat is a button the script cannot reach, you do not have the logic on that page. You have a heater with a laptop nearby.

Write this as six lines on the point list. Unit sensors. Rack-side sensors. Valve state. Leak state. Command echo, meaning what the script asked and what the unit did. Export. If any line is missing, the control logic is not implemented, however finished the enclosure looks.

## The stranger test for a file

Take an export from a bench run. Hand it to someone who was not there. Ask them to answer, without you: what was commanded, what heat did the liquid appear to receive, did any sample go stale, did any alarm fire, were the valves in the recorded state. If they cannot answer, the exit failed, even if you can answer from memory. Memory is not an export.

This test is the acceptance test for the data path. Do it on Gate 2 and again on a plateau in Gate 3. Gate 2 proves the points exist. Gate 3 proves they exist while heat and flow are moving. A data path that only works at idle is a data path that will be down during the only hour that matters.

## Composite: the last good value

A platform loses the flow meter for twenty minutes and repeats the last flow with fresh timestamps. Temperatures climb. The computed heat balance shows a bizarre efficiency. An engineer “corrects” the temperatures. The correction is famous for a week. The held flow is discovered later, or not at all. The fix is quality flags and a rule that a stale flow fails the plateau. The fix is not a better correction. Corrections on top of painted data are how false precision spreads.

## Composite: the door display

Another unit has a fine local display and an export that is a different set of names, updated at a different interval, missing power. The team uses the display for the acceptance conversation and files a screenshot. The screenshot becomes the record. Two months later the screenshot cannot support a heat story, and the export cannot either, and the unit “passed.” The stranger test would have failed in ten minutes. Screenshots are allowed as illustrations. They are not the export.

## Public sources for this chapter

Public documents will tell you that liquid-cooled IT is discussed in terms of flow, temperatures, and pressure. They will not give you a register map, and you should not build one by transcribing a figure. The minimum set in this chapter is the book’s own: both temperatures, both pressures, flow, on the unit and as a comparison at the boundary, plus electrical power. If a cited ASHRAE or NVIDIA document requires an additional quantity for the interface you are standing in for, add a row and cite the edition. Do not add a hundred points because a building guide had a hundred points. ASHRAE’s titled work on real-time energy measurements and on DCIM integration is about the hall’s data problem. It is the next book’s neighborhood. Here it only supports the export duties: time, unit, quality, and a file a stranger can open. Do not paste a point list from a sample chapter.

## Decisions to record

- Unit points and comparison points, with expected-difference notes.
- Sensor places on the diagram, including which sensor is allowed to remove heat.
- The interval, the clock, and the rule that a failed read is marked, not repeated.
- Collect, store, show, export, each with a do-not-ship condition.
- Alarm list with actions, latch behavior, and a non-destructive test method for each protection.
- The local stop that overrides a stuck remote command.
- A named person for the stranger test, and the file they will be handed.


# 6. Safety

Safety in this book is a list of stops, not a site emergency plan. The project book can hold phone numbers, egress, and who to call in a particular hall. This book holds the stops that must be true of the unit wherever it is plugged in, including a bench, including a truck dock, including a room where the network is a rumor.

A stop has a sensor or a discrete cause, an action that removes or contains the hazard, a local indication, a record, and a behavior when the thing that was supposed to detect the hazard has itself failed. If you cannot fill those five, you do not have a stop. You have a warning label.

The five stops this chapter requires by name are overtemperature, overpressure, leak, electrical fault of the kinds that set things on fire or shock a person, and the wrong valve. You may add others. You may not drop these and replace them with a single “system healthy” bit.

## Overtemperature and the Class-1 hardwired safety loop

The unit’s product is heat. The failure of that product is heat in the liquid, on a surface, or in a terminal that was not meant to be the heat sink. Overtemperature protection must remove heat without asking a person to notice a trend. Trends are for the data book. Stops are for hardware and for circuits that still work when the trend display has crashed.

In mission-critical load bank engineering, overtemperature safety must be split into two tiers:
1. **Class-2 Supervisory Software Trip**: The PLC or monitoring microcontroller reads calibrated Pt100 RTD values and software setpoints. If liquid temperature drifts high, it commands contactors open via Modbus or firmware logic.
2. **Class-1 Hardwired Fail-Safe Interlock (Firmware-Independent)**: (See Figure 04). A series electrical circuit powered directly from the 24VDC contactor coil supply, passing through:
 - A red latching mushroom E-Stop pushbutton on the front panel;
 - A mechanical bimetal snap-disc thermostat welded directly to the immersion heater vessel shell (tripping mechanically at 85°C);
 - A hardware mechanical low-flow differential pressure switch (opening if flow collapses below minimum 30 LPM);
 - A containment drip-tray leak detection relay contact.

If any of these physical devices opens, the main contactor coil de-energizes immediately (< 20 milliseconds), and internal spring returns force the high-voltage contacts open. This safety action occurs even if the PLC processor is completely frozen, firmware is in an infinite loop, or the operating system is locked in a kernel panic. Software cannot override this hardwired loop. Acceptance includes pulling one of these wires and proving the contactors drop.

## Condensation and dew point interlock

Liquid load banks operating in humid or tropical facilities face a reverse thermal hazard: condensation. 

When chilled liquid enters the secondary loop below the data hall dew point (T_dp), bare metal manifolds, uninsulated EPDM hoses, and quick disconnects instantly condense water from the air. In a high-density AI room, droplets dripping onto live 400V busbars or 54V power shelves cause catastrophic phase-to-phase arc flashes.

The safety architecture must include a hard dew point interlock:
- The controller monitors data hall ambient air temperature and relative humidity (RH) to compute real-time dew point (T_dp).
- **Safety Rule**: Supply temperature must maintain an operating margin of T_supply ≥ T_dp + 2.0 K.
- If secondary loop temperature falls toward the dew point envelope, the controller must sound an alarm and immediately close modulating cooling valves or stage on minimal trim heat. Liquid cooling tests must never allow a sweating machine.

## Overpressure

The loop the load bank can influence needs a limit that does not depend on the CDU being polite. If the only protection is “the CDU will catch it,” write that assumption in known limitations, in ink, and do not claim the unit is safe on a bench pump that has no such politeness. Bench pumps are where prototypes die, because the bench pump is often capable of more pressure than the hall loop, into a closed valve the hall loop would not have closed.

Name the highest pressure you believe the cited loop, and the bench loop, can apply. Compare that with the weakest wetted component: hose, gasket, gauge, heater shell, meter body, valve body. The weakest one is the rating that matters. A strong shell does not rescue a weak gauge. Gauges fail sharp. Put a gauge range and a gauge isolation valve on the diagram if a failed gauge can spray.

Relief is the honest design when a trapped section can be pressurized beyond that weakest rating. A relief path needs a destination: a tank, a return, a place that is not a person’s face and not an electrical enclosure. A relief that relieves onto the floor without a record is a leak you intended. It still needs an alarm or an inspection step after any event, because a relief that has lifted may not have reseated.

If you choose not to fit relief, because every pressure source is external and controlled, write the assumption and the administrative control: this unit is not to be connected to an unregulated source. Then make that sentence impossible to miss in the file a stranger gets. Administrative controls are weaker than relief. They are sometimes all you have. They are never a reason to skip the sentence.

Overpressure and heat interact in a closed volume. The heat-path chapter forbade trapped heaters between closed valves, or required an interlock. This chapter repeats the consequence: a relief device is not a substitute for heat in a trapped volume, because the liquid that leaves through the relief may be hot, and the element may still be dry-firing after the liquid has left. Interlock first. Relief second. Procedure third. Do not reverse that order because a relief valve was easier to buy than a valve-position switch.

Test the overpressure story carefully. You do not need to drive the unit to destruction. You need to show that the detecting device, if you have one, alarms at a simulated pressure, and that a relief, if you have one, has a certificate or a bench test from its maker that you have filed, and that the destination of the relief is the one on the diagram. A relief pointed at a changed panel, because the panel moved after the drawing, is a failed Gate 1 item. Look at where it points, with the enclosure closed, from the position a person would occupy.

## Leak

A leak is a liquid failure and sometimes an electrical failure, in that order of time and in the reverse order of severity if the liquid is conductive and reaches a live part. Design so liquid does not have a path into the electrical enclosure. Drip lips, separation, connectors that face down, no terminal blocks in the drip plane. These are design duties. They are also Gate 1 looks. A rendering will not show the path a drip actually takes. A cup of water, used deliberately on the outside of the liquid section while the electrical section is open and powered down, will show it. Do that before you mix electricity and coolant. It is a cheap test and it embarrasses drawings, which is what you want.

Detection, if fitted, must cause an action. Minimum action: remove heat and alarm locally. Better: also close what you can close, if closing does not trap a heater that is still hot. Think that sequence through. Close valves, then heat off, is the wrong order if closing traps heat. Heat off, then isolate, is usually the right order. Write the order.

A leak alarm that only exists on a screen in another room is a report. It is not a protection for the person standing next to the unit. Local indication has to work with the network dead. A lamp, a horn, a flag. Pick one that can be heard or seen in the room you will actually use. Then test it by simulation. A wet test on a sensor probe, done so the liquid cannot reach live parts, is better than a software bit if the sensor is the thing that will fail in service. Software bits do not get wet.

No leak sensor is an allowed limitation for a prototype that is never left alone and is used only on a bench with a person whose job is to watch. It is a poor limitation for a unit that will be left at a plateau while people look at a CDU. Match the limitation to the way the unit will be used. If the use changes, the limitation must be reopened. Limitations are not permanent gifts.

## Electrical: 2N dual feeders and dielectric withstand thresholds

Insulation and protective earth are acceptance items, not a paragraph in a manual no one opens. In industrial load bank commissioning, “the electrician said OK” is not a test record.

Two electrical standards govern Gate 2 acceptance:
1. **Insulation Resistance (Megger Test)**: Apply DC 1000V for 1 minute between the main power circuit and the grounded chassis frame. The measured insulation resistance must be ≥ 10 MΩ. Any lower resistance indicates moisture ingress, compromised conductor insulation, or internal coolant leakage.
2. **Dielectric Withstand Test (Hipot)**: Subject the main circuit to power-frequency 1.5 kV AC for 1 minute with zero dielectric breakdown, flashover, or trip.

Furthermore, mission-critical AI data centers utilize a **2N dual-feeder power architecture (Feed A and Feed B)**. Racks are dual-corded, with each feeder fed from independent upstream UPS and PDU lines. A prototype liquid load bank must mirror this dual-corded reality:
- **Feeder Separation**: Feeder A powers Heating Banks 1 & 2; Feeder B powers Heating Banks 3 & 4. Each feeder features its own lockable molded case circuit breaker (CB-101A and CB-101B).
- **Control Power Survival**: The internal 24VDC control power supply must be dual-fed via a diode-OR redundancy module. 
- **Single-Feed Loss Drop Test**: During Gate 3 testing at 100% load, operator intentionally trips Feeder A. The load bank must instantly shed Banks 1 & 2 without causing Feeder B to trip on overcurrent or inrush transient. Crucially, the control bus, PLC, flow meter, and temperature sensors must not suffer even a microsecond brownout. If losing one feeder reboots the controller or freezes the export, the unit fails 2N acceptance. (See Figure 04 for the dual-feeder and control bus schematic).

Conductive coolant and a leak into a terminal is the combined failure. The drip test and the earth test are how you cheapen that combination. Do not wait to “see if the coolant is really conductive.” Assume a leak can become a shock or a trip, and keep liquid and live parts apart. If a design cannot keep them apart, it is not finished.

Lockout matters for service. Module removal and any work that opens the electrical section need a way to make heat and unexpected motion impossible. A local disconnect, lockable, visible, is the usual answer. A software “service mode” is not a lockout. Acceptance includes opening the disconnect and confirming heat cannot be commanded remotely while it is open. Remote start that ignores a local disconnect is a failed unit, not a feature.

## Wrong valve

The spare port, the bypass, and the isolation valves will be found in the wrong state. This is not a slur on operators. It is a count of handles. Every handle will, at some point, be left where the last task needed it.

Label handles by function, in words a stranger can match to the one-line diagram. “V3” is not a function. “Return isolation” is a function. If you need both, use both, and make the function the large text. Labels that face the wall fail Gate 1. Labels that fall off fail Gate 1. Acceptance includes a hand on each valve and a comparison to the diagram, not a glance at a list.

Wrong valve is also an interlock problem where the valve can trap heat or dead-head a path you said was protected. Position switches on those valves are how the interlock becomes real. Without switches, the interlock is a procedure. Procedures are Gate checks and run checks. They are weaker than switches. If you rely on procedure, the acceptance sheet and the run sheet must both include the valve line, and a missed line is a failed start, not a coaching moment. Write that.

The spare brought into service without a retest is a wrong-valve event of a special kind. The hydraulic path changed and the record did not. The liquid chapter already said a swap requires a named person and a retest. Here the safety consequence: a spare path that is uninstrumented can put full heat through a path with no flow reading. Forbid heat on an uninstrumented spare, by procedure or by switch, or instrument it. Do not leave the combination available and unnamed.

## What stays out of this chapter

Phone numbers, room names, egress maps, chemical-handling plans for a particular hall, and medical advice. Those are real, and they are not properties of the load bank. Putting them here would make the book look complete and make the unit look specified when it is not. Point to the project book. Then check that your unit does not assume a response time that only one hall can provide. A stop that needs someone to arrive in one minute is not a stop on the unit. It is a hope about the building. Convert it into a stop on the unit, or write the dependency as a limitation that forbids unattended heat.

Fire suppression interfaces, if a building requires them, are a project interface. The unit’s contribution is a contact that means “heat is commanded” or “fault,” if the project needs it, tested like any other discrete. Do not pretend this book designs the suppression system.

## Composite: the polite CDU

A prototype is always tested downstream of a CDU that trips at a sensible pressure. The unit has no relief and no pressure switch. The limitations page never gets the sentence about unregulated sources. On a bench, a temporary pump and a closed isolation valve meet. The weakest gauge fails. Nobody is injured because the gauge happens to point at a panel. The panel is then redesigned, and the gauge is replaced with the same range, and the sentence is still missing. The fix is the sentence, the comparison with the bench source, and a relief or a pressure switch that does not need the CDU. The fix is not a new panel.

## Composite: the software limit

Overtemperature is a number in a controller. The contactor is driven by a different board that holds last state on loss of communication. The controller reboots during a sag and comes back slowly. The contactor stays in. The software limit is not in force for the minute that matters. The safe-state test, kill control power, and the separate test, kill the link between controller and contactor, would have shown it. Those tests are acceptance tests. They are boring. They are the chapter.

## Public sources for this chapter

Electrical control is two citations, not one copied article. The feed is governed by the premises code the hall adopted: NFPA 70, the National Electrical Code, in the United States, in the adopted edition, or the local adoption of IEC 60364 or the national wiring rules. The unit is governed by an equipment standard. IEC 60204-1, electrical equipment of machines, is the usual international reference for a heater with a control circuit and a disconnect. The mark the builder claims, if any, names the product-safety standard. Write both editions on the sheet. Do not transcribe code text into the gate. Transcribing a code is a copyright problem and a maintenance problem, because the adopted edition will move.

The behaviors this book requires are its own, and they are the ones the gates test. Lockable disconnect that remote command cannot override. Overcurrent that removes heat, with the control-supply state known. Protective earth tested. Loss of control power removes heat. Stop does not ask the network. Liquid does not track into live parts. Where the cited edition specifies a test method, use that method and cite it. Where it does not, write the method. Do not invent a clause number.

ASHRAE’s bulletin titled “Data Center Power Equipment Thermal Guidelines and Best Practices” is about the thermal environment of power equipment. Cite it if the project needs that subject. It is not the wiring code, and it is not extracted here.

## Decisions to record

- For each of the five stops: sensor or cause, action, local indication, record, failed-sensor behavior.
- Thresholds cited or labeled as your choice. No invented universal numbers.
- Non-destructive test method for each protection, written before the prototype is hot.
- Control power versus heater power, and the open-breaker test.
- Valve labels and which valves are procedure-only versus switched.
- The limitations that forbid unattended heat, if detection or relief is absent.
- Confirmation that hall emergency plans were not used as a substitute for a unit stop.


# 7. Accept the prototype

This is the chapter the rest of the book is for. An unaccepted prototype is a liability with a nameplate. A prototype accepted against a slideshow is the same liability, with better lighting.

Acceptance is a sequence of gates. The sequence is the method. Teams fail when they start the heat run because the truck is waiting, while a valve still cannot be reached, or they waive the data exit because the local display looked fine. The truck can wait. A load bank that leaks at the fitting does not get a heat run so the schedule can say the heat run happened. A heat run on a leaking unit is not evidence of duty. It is evidence that you were in a hurry.

Four gates, in order. Static and workmanship. Power and communications. Load steps. Overload. Do not start the next gate to save the day on a failed earlier one. Do not run them in parallel on the same unit to save an afternoon. Parallel gates hide the failure mode you most need, which is a unit that looks electrically alive and is hydraulically unfinished.

The sheet you walk in with is the sheet from the earlier chapters, revision marked, unknowns either filled or converted into explicit limitations. If material unknowns remain in a do-not-ship cell, you are not at acceptance. You are at a design review. Hold the review. Do not rename it acceptance to keep the date.

## Roles

Name four roles, even if two people hold all of them. The owner of the sheet, who may not quietly edit a stop condition during the day. The operator, who commands plateaus and is not the same person who built the contactor logic, if you can arrange that. The recorder, who writes what happened, including the boring passes. The stranger, who was not in the build and who will be handed the export. If your team is one person, the stranger still has to be someone else, even if only for an hour. Self-acceptance is how stale data survives.

Name who may waive a gate. The default is nobody on the day. A waiver is a revision of the sheet, signed by the sheet owner and by whoever signed scope, with a limitation added, and with the claim reduced to match. A waiver that keeps the claim and drops the evidence is not a waiver. It is a decision to ship a rumor. Write that sentence at the top of the sheet so it is in the room.

## Setup is not a gate, and it can still stop you

Before Gate 1, record the setup. What loop is connected. What it can absorb. What it can deliver. What feed is connected. Which revision of the sheet you are using. Which revision of the cited interface specification, if a citation is in play. The identity of the unit: a serial or a shop mark that will still mean something in a year. If the unit has no identity, give it one before you start. Acceptance of an anonymous chassis will be mis-filed onto its successor.

If the temporary loop cannot absorb the longest dwell or cannot deliver the flow you intend to demand, do not enter Gate 3. You may still do Gate 1 and Gate 2. Write “Gate 3 not started, loop inadequate” and stop. That sentence is a successful use of the method. It is not a failed prototype. A failed prototype is one you declared passed against an inadequate loop.

Photographs are allowed. They are not the record. The record is the sheet with pass, fail, or not-started on every line, signed, with the export attached for the gates that produce data. A photograph of a green lamp is a souvenir.

## Gate 1. Static and workmanship

Compare the physical object to the requirement sheet and to the P&ID diagram (Figure 02), not to a memory of a 3D CAD rendering. (See Figure 06 for the sequential gate state machine and the fail-closed barrier rules).

Walk the reaches and couplings:
- **Danfoss FD83 Quick Disconnect Verification**: Inspect both supply and return FD83 couplings. Verify that the mechanical dual interlock operates smoothly: with fluid unpressurized, the coupling must engage and snap the safety lock pin firmly into detent. Verify that the internal ball valve handle cannot be turned to "Open" while uncoupled, and that the sleeve cannot be retracted to "Disconnect" while the valve is open. A coupling with a bent lock pin, stuck sleeve, or scratched sealing face is an immediate Gate 1 fail.
- **Hose Routing & Bend Radius**: Verify that the EPDM/reinforced hoses maintain a minimum bend radius of R ≥ 6D under actual operating geometry. No kinks, no chafing against sheet metal edges, no mechanical hose weight suspended from the coupling neck, and no hose drape obstructing electrical enclosure access or module removal.
- **Pre-Commissioning Flushing Bypass**: Verify that the 50-micron inline bypass strainer (V-105 loop) is installed and piped. Perform an initial cold-water wash through the bypass; inspect the strainer basket for machining swarf or pipe scale before allowing liquid into the main heater core.
- **Hydrostatic Hold & Joint Leak Inspection**: Pressurize the unit to 1.5× rated working pressure (e.g. 9.0 bar cold) and hold for 30 minutes. Zero visible weep across all NPT/BSP threads, tri-clamp sanitary ferrules, and valve stems.
- **Drip Path Test**: With the electrical section powered down and cabinet open, pour a deliberate cup of water over the exterior of the liquid section. Verify that runoff drains completely into the bottom containment tray without tracking a single drop into the high-voltage electrical compartment. If liquid tracks into live enclosures, stop. The day ends as a mechanical redesign day.

Gate 1 fails closed. Anything you would otherwise discover with the loop full and the commissioning truck waiting outside is an automatic stop.

## Gate 2. Power, Megger testing, and telemetry

The feed matches the power interface line. Electrical testing must not rely on casual verbal assurances:
- **Megger Insulation Resistance**: Apply DC 1000V for 60 seconds between the main busbars and the chassis protective earth (PE). Measured resistance must be ≥ 10 MΩ. Record the exact value on the acceptance sheet.
- **Dielectric Withstand (Hipot)**: Subject the main circuits to power-frequency 1.5 kV AC for 1 minute with zero flashover or breakdown.
- **Hardwired E-Stop Circuit Trip**: Assert the manual E-Stop pushbutton and verify that the main power contactors drop open within 20 milliseconds by spring return. Verify that control power (24VDC) remains alive to maintain alarm logging.
- **Local Disconnect Interlock**: Open the main lockable disconnect switch. Attempt a remote software start command over Modbus. Verify that heat cannot be energized under any software override.

The unit can be found by the test platform under the identity commissioned today. That identity is written on the sheet. It is not in this book, and it is not a default you promised a vendor in a footnote. Points in the instrument chapter can be read: both temperatures, both pressures, flow, electrical power, valve states where valves are powered, alarms. Each has a unit, a timestamp, and a quality. A disagreed or missing point retries or alarms. It does not freeze the last good value and stamp a new time.

Prove the stale-data rule. Disconnect one sensor or stop one read, on purpose, for long enough that a lazy system would have repeated the value. The export must show a gap or a bad quality flag over that interval. If it shows a smooth continuation, the exit fails. This test is worth more than a dashboard review. Do it even if everyone is annoyed.

Local indication and remote indication tell the same story, or the difference is documented as a known limitation before you proceed. A limitation that says “display and export disagree and we do not know why” is not acceptable. A limitation that says “display is rounded to a coarser step than the export” can be acceptable if the stranger can still answer the questions. Run the stranger test here, on an idle export. Command nothing. Confirm the stranger can see that nothing was commanded, that quality is good, and that the points are the points on the diagram. If the stranger cannot map a column to a diagram name, fix the names. Do not teach the stranger a private dialect and call that a pass.

Alarms at idle: cause one informational alarm if you can do it safely, and one protection alarm by simulation. Confirm local indication, record line, and action. For the protection alarm, confirm heat cannot be commanded while it is latched, if that is the rule you wrote. Reset only from the place you specified. A reset that anyone can do remotely, with no local acknowledgement, will be used to clear a trip during a later run. If that is not what you wanted, you will learn it now.

Network loss while a stop is asserted. The stop remains. Heat stays off. The unit does not reboot into a default full load. Defaults to full load exist in this world because someone thought a demo should look alive. Hunt for that default. Power-cycle with the remote path silent. The resulting state is heat off, or heat off until a local person commands a plateau. Anything else fails.

Gate 2 pass: identity recorded, points live, stale data marked, stranger can read an idle file, protection alarm tested without destruction, local disconnect and network-loss behaviors match the sheet. Gate 2 fail: any of those missing. Do not proceed to heat in order to “see the points under load” if the points are already lying at idle. Load will not make a liar honest. It will make the lie expensive.

## Gate 3. Load steps

Enter only from a passed Gate 2 and an adequate loop. Start from the recorded valve line-up. Start the export first. If the export is not running, the step does not count. A step that happened in the room and not in the file did not happen.

The sequence is a shape, and the prototype plans in the working file already use one. Power on. Self-check, recorded, not a splash you believe. Initialize: heat still off, flow readable, no latched protection. Then sit at quarters of the duty: a quarter, a half, three quarters, full. Then zero. Then shut down. The record covers the whole path. An alarm that is not explained fails the path. This quarter sequence is a usable default when the sheet has no other citation. It is not a law. If your duty citation demands different steps, use those, and say why the quarters were not enough.

The same plans then make a separate visit above full, and come back to zero. Their paperwork uses a short step above the rated point. Do not copy their percentage into your sheet as an industry overload. Do copy the shape: name the level, name the dwell, record it, leave it. A visit you extend because it looks calm is no longer the visit on the sheet.

A liquid-system test procedure in the same file uses the load-bank controller to walk those steps while other people record the coolant distribution unit, on both sides of its heat exchanger, and look at electrical terminals with a thermal camera. That procedure is a later book. The requirement it puts on this unit is not. The controller must be able to hold each step long enough for those other readings to be taken, and the export must show that the step was the step they think they recorded. If the controller can only be nudged by hand, their procedure and your gate are both fiction.

The sequence continues. The sudden increase is inserted where the sheet says, between two plateaus, and is not a substitute for sitting on the destination plateau afterward. You still sit. The jump is not the dwell.

The 2N single-feed loss drop test is inserted at the 100% plateau. In a mission-critical 2N data center, power feeds fail. With the unit operating steadily at 100% duty, the operator manually trips the main circuit breaker on Feeder A (CB-101A). The load bank must immediately shed its assigned heater banks without delay. Feeder B must continue carrying its half-load without tripping its upstream breaker on transient inrush. Crucially, the internal 24VDC control power supply must ride through the transfer seamlessly: zero PLC reboot, zero dropped Modbus frames, zero clock reset, and no false latching of emergency shutdowns. If tripping one feed kills the data export or resets the controller, Gate 3 fails the power redundancy line.

At each plateau, the recorder logs start time, commanded power, and whether the liquid set is being judged or only recorded. If it is judged, the bands are the ones on the sheet, not new bands invented because the first plateau missed. Missing a band is a fail or a limitation, not a prompt to edit the band. The operator does not “nudge” a valve that the authority sentence said was fixed, unless the sheet allows the nudge and the nudge is recorded. Unrecorded nudges are how two plateaus become incomparable.

Alarms that appear must be explained in the record or the gate fails. Explained means: cause, whether the action matched the sheet, whether the plateau was invalid as a result. An alarm that clears itself and is not in the export is a failed alarm design, discovered late. Stop and fix the exit. Do not argue that the lamp only flickered.

The heat story at each judged plateau: electrical power and the liquid temperatures and flow should be tellable in one paragraph by the stranger, after the fact, without you. If the rise is small because flow is high, the paragraph should say that, and should say that temperature alone was not used to pass the point. If the rise and the power disagree enough to change the conclusion, the plateau fails until the destination of the watts is found. Bypass, loss to the room, sensor in a stub, stale flow: find which. Do not apply a factor.

Comparison points, if temporary, are fitted before the first plateau and left alone. Moving a probe between plateaus breaks the set. If a probe must move, that plateau is a different setup and is labeled as such. Do not average it into the others.

The sudden increase: the command reaches the new value on a time scale the sheet called sudden, the power follows, the export shows the order, no protection trips unless the destination was illegal. If a hidden stagger turns it into a ramp, write “ramp, not sudden” and fail the sudden-increase line until the stagger is documented and either accepted as a ramp or removed. Do not pass it because the final plateau was fine. The final plateau is a different line.

Return to zero and confirm heat is off while flow remains readable, if that is the design, or confirm the safe-off state if zero means off. Shut down. Export closed properly, file stored, file opened on a machine that did not run the test. The stranger test, again, on a file that contains plateaus. This is the real stranger test. The idle one was a rehearsal.

Gate 3 fails if a plateau cannot be held, if the record is incomplete, if stale data appears inside a dwell, if an alarm fired and is unexplained, if the sudden increase was a ramp you were not allowed to call sudden, or if the stranger cannot reconstruct the command and the heat story. Gate 3 does not fail because the temporary loop drifted, provided you wrote loop-drift as a setup limit and the unit’s own points were honest. If you cannot tell unit drift from loop drift, the comparison points are inadequate. That is a fail of the setup, and it invalidates the judged plateaus. Recorded-only plateaus may stand. Judged plateaus may not.

A unit that can only be off or full has not passed this gate, whatever the nameplate says. Do not accept a promise that steps will be added in software later. Software later is a different unit. Accept the unit in the room.

## Gate 4. Overload

Enter only after Gate 3 is clean. Overload on a unit that cannot hold its rated plateaus proves nothing except bravery. Define the level and the dwell on the sheet before the day, as a citation or as your choice, labeled. Define the exit: return to a named plateau or to zero, then shut down. Data still recorded. The overload is a visit, not a new rating.

You are looking for stability and for heat leaving by the path you designed. Stability means no trip, no oscillation that the sheet called unacceptable, no valve hunting if valves are powered, no stale data, no connector growing hot, no hose changing shape into a kink. Heat leaving by the designed path means the liquid story still explains the power, within the wider band you should have written for this short visit. If you wrote no band, you record and you do not claim a quantified pass. You may still fail the visit for a trip, a leak, a stale record, or a safe-state miss.

Watch the person, not only the screen. Overload is when a hose, a relief, or a smell will announce a design error the sensors are late to. Someone’s job is to look at the unit, not at the plot. Give them the authority to hit the local stop without a meeting. A culture that requires permission to stop an overload is a culture that will one day be late.

Then leave. Return to zero. Confirm latched alarms, if any, are understood. Confirm the unit does not now sit at a higher continuous command because someone liked the overload number. Reset any temporary override. A override left engaged is a failed gate even if the visit was pretty.

Do not copy a percentage from a prototype report and call it the industry overload. The rule in this book is smaller and stricter: the sheet must name the overload and the dwell, and a machine that cannot perform the named point does not ship as a machine that can. If you need to ship anyway, you ship with the overload claim removed, not with the claim and a story.

Gate 4 pass: named visit completed, exit completed, record complete, no unexplained alarm, no new leak, local stop proven if you used it or proven separately if you did not need it. Gate 4 fail: trip you cannot explain, heat that stayed on after command zero, data that went stale at the only moment that mattered, or a visit you extended because it was going well. Extending the dwell beyond the sheet is a different test. Do not rename it into a pass of the original.

## The overload stop, practiced

If Gate 4 never needs the local stop, you still practice it once, at a low plateau, before or after the visit. Command a plateau, then hit local stop, including while a remote command is asserting the plateau. Heat off. Alarm or indication as specified. Export shows the stop. Reset does not resume heat unless a person commands it again. This practice is not optional. Units that are never stopped are units whose stop path is a drawing.

Also practice loss of control power at a low plateau, once. The result matches the safe-state chapter. If you are afraid to do this, you are afraid of the design. Fix the design before Gate 4’s high visit. Fear is information.

## What you write on the day

Every line: pass, fail, or not started. Time. Initials. For a fail, one sentence of what was observed, not what was hoped. Attach the export file name and the identity of the machine that stored it. Note the sheet revision. Note any waiver by its own revision, not by a verbal aside. Note who the stranger was. Note the loop and the feed. Note anything that smelled, wept, or changed shape, even if a number did not catch it.

Do not write “as expected” as the only content of a line. Expected is the sheet. The line should say what was observed in a way a later reader can compare. “Held middle plateau for the dwell, export file X, stranger reconstructed command and rise” is a line. “OK” is not a line.

## After a fail

Fix, then repeat the failed line and every line the fix could have disturbed. A software fix repeats Gate 2’s stale-data test, not only the screen you were looking at. A hose fix repeats the reaches and the leak look. A sensor fix repeats the stranger test. Do not declare the unit accepted because the last fix felt small. Small fixes have large cousins.

If you cannot fix, reduce the claim or reject the unit. Reduced claim goes on the limitations page the same day, not in a follow-up mail. The acceptance record cites the reduced claim. A unit with a reduced claim can still be useful. A unit with a full claim and a reduced secret cannot.

## What pass looks like, and what it does not

Pass is boring. The points exist. The steps were sat. The record is complete. The alarms that fired are explained. The stops work with the network dead. The stranger can reconstruct the day. The limitations page matches what you actually saw, including “overload is not a new rating” and any sensor blind spot you still carry.

Pass does not look like enthusiasm. It does not look like a tour. It does not look like a single full-load photograph. It does not transfer to a second unit by resemblance. The second unit gets its own record. Twins are not the same unit until the gates say they are.

Pass of this prototype does not accept the hall, the CDU, or the IT rack. It accepts the stand-in, at the duty cited, within the limitations written. Anyone who uses the record to claim more is writing the project book without doing the project. That misuse is not a reason to weaken the gates. It is a reason to keep the claim sentence at the top of the record, in short words.

## Composite: the truck

The truck is at the dock. Gate 1 found a spare port that is only a plug, and a hose that kinks when routed to the real manifold position. Someone proposes to note both as commissioning items and run Gate 3 on the bench coil so the acceptance meeting can happen. The meeting would then accept a unit that has not been seen in its real routing, against a spare claim that is false. The method’s answer is dull. Fix the spare claim or the port. Route the hose as it will be used. Repeat the disturbed lines. The truck waits. The alternative is a record that will be used, later, to argue that the manifold “cannot take the flow,” when the manifold was never the thing that was kinked.

## Composite: the edited band

The middle plateau misses a temperature band by a small amount. The owner of the sheet, who is also the operator today, edits the band and continues. The export is fine. The story is fine. The revision rule is dead. Next month a different miss will be edited too, and the duty set will have migrated to whatever the unit can do, while the citation still names a window the unit no longer represents. The method’s answer: the miss is a fail or a waiver with a reduced claim. The person who edits and operates and signs is the reason the roles were split. If they cannot be split, the recorder at least writes “band edited during the run” in a sentence the stranger will see. Shame is a weak control. It is better than silence.

## Public sources for this chapter

A gate cites a document. It does not attach the document. On the acceptance header, the interface citation is the NVIDIA datasheet or the rack specification then in force, by title and revision, or it is unknown and Gate 3’s judged duty lines stay not started. The premises code edition and the equipment-standard edition sit on the Gate 2 header. An ASHRAE title sits on the bibliography if a materials or class cell depends on it, and the cell still holds your project’s value, not a pasted table. If someone arrives with a printed white paper and wants to initial a line by pointing at a paragraph, refuse. The line passes when the object meets the sheet. The paper is not the object. Chapter 19 is the rule if the argument continues.

## Decisions to record

- The four roles, and the waiver rule, before the day.
- Setup adequacy for the loop and the feed, or Gate 3 not started.
- Every Gate 1 reach and the fill, leak, and drip results.
- The stale-data proof and the stranger’s name.
- Plateau results tied to export file names, not to memory.
- Overload level, dwell, exit, and the practiced local stop.
- Limitations revised the same day as any reduced claim.


# 8. The file you must hand over

A delivered load bank without a file is a used appliance. The person who receives it cannot accept it, cannot operate it, cannot explain a bad hour, and cannot tell a later revision of the rack specification whether the unit still applies. They can turn it on. That is not delivery.

The file is short on purpose. Short means a stranger can find the claim, the stops, and the limitations in one sitting. Short does not mean missing. A thick file that hides the authority sentence in an appendix is a thin file plus a burden. Put the sentences that can stop a bad claim in the front. Put the test records behind them, labeled so the front page can point at a file name.

This chapter lists what is in the file and what is not. It is the packing list for the knowledge. The machine’s packing list is a project document. Do not merge them. A crate list and a duty set have different readers, and one of them will be thrown away when the crate is empty.

## Identity and revision

The first page names the unit. Shop mark or serial, and a description a person can match to the chassis without opening a drawing: roughly what it is, not a slogan. It names the file revision and the date. It names the sheet revisions that acceptance used. If the unit changes after acceptance, the file revision changes the same day. A changed unit with an unchanged file is an unaccepted unit that happens to have a history.

Two hops reconstruct history. The acceptance record cites the sheet revision. The sheet cites the interface specification by title and revision. You do not need a third hop through a mailbox. If a fact exists only in a mailbox, it is not in the file. Copy it in or stop relying on it.

The claim sentence sits under the identity. What this unit is allowed to represent. What it is not allowed to represent. The claim is the same sentence you wrote in the first sitting, updated by whatever the gates forced you to reduce. If the claim grew during the project, the gates that justify the growth are cited. Claims do not grow by adjective.

## The requirement sheet

Include the requirements list from the first technical chapter, revision marked, with the six functions and the three interface lines. Evidence cells and do-not-ship cells are filled. Unknowns that remain are dated and owned, and they are repeated on the limitations page so a reader who only reads limitations still sees them. A requirement that is “open” and a limitation that does not mention it will be missed. Say it twice, in those two places, and nowhere else in a contradictory form.

Include the revision rule and the waiver rule. A future reader needs to know how a cell was allowed to change. If a cell changed during acceptance, the waiver is attached, not summarized from memory. Attachments have names. “See email” is not a name.

## The duty set

Include the operating point as a set, each cell cited or labeled as the project’s own choice. Include the places acceptance visited and why. Include the overload as a visit, with the explicit statement that it is not a new continuous rating unless a gate actually established that, which it almost certainly did not.

Include the false-story sentences. They teach the next operator what not to conclude from a single pretty number. A file that only has numbers will be read as a score. The false stories turn it back into a measurement.

Include the temporary-loop minimums that were assumed at acceptance, so nobody confuses the bench loop’s capacity with the unit’s. A later hall loop that is weaker than the bench is a project problem. The file should make that comparison possible without calling you.

## The one-line diagram

Include the diagram a stranger can redraw. Boundary, streams, isolation, spare, trim or bypass if they exist, sensor places, relief destination if relief exists, and the authority sentence: who sets interface flow, who sets heat-section flow, who sets heat. If the diagram and the authority sentence disagree, the file is not ready. Do not ship a disagreement and call it detail.

The diagram does not include a site plan, a customer logo, a room number, or a photograph of a real manifold that would identify a place. Those belong to the project, if anywhere. The unit’s diagram should still make sense if the unit is moved.

## The point list

Functions, not registers. Each point: name as in the export, diagram location, unit of measure, whether it can remove heat, whether a stale value fails a plateau. Valve states included. Alarm names included, with actions. The export’s column headers match this list exactly. If they do not, Gate 2 was not really passed. Fix the headers or fix the list before you call the file delivered.

A register map, if your project uses a bus, can be an appendix for the people who must maintain the bus. It is not the point list. The point list is readable without the bus. If the map and the list disagree, the list and the export win, and the map is wrong. Say that in the appendix so a later technician does not “correct” the export to match a stale map.

## The acceptance record

Include the record from the gates: pass, fail, or not started on every line, times, identities, export file names, stranger’s conclusion, waiver identifiers, and the same-day limitations. Include failed attempts you fixed, and the repeat results. A record that starts at the final pass and omits the fail is advertising. The fail is how the next unit gets built faster. It is also how you remember which fix was load-bearing.

Include the practiced local stop and the control-power kill, not only the pretty plateaus. A reader who sees only plateaus will assume the stop path was never proven. Do not make them assume.

Store the export files with the record, or store a durable pointer that does not depend on one person’s laptop. If the pointer dies, the acceptance dies with it. A record that cites a file you cannot open is a story. Treat file storage as part of delivery, not as an IT favor.

## Known limitations

This page is not an apology. It is a boundary on use. Write limitations in the form: this unit does not, and therefore you must not. Examples of the form, generic: this unit does not measure branch flow, and therefore you must not claim module balance from the header. This unit’s overload visit is not a continuous rating, and therefore you must not command that level for a long run. This unit was leak-tested only at the temperature on the record, and therefore you must not claim the hot end of a window you did not test. This unit has no leak detection, and therefore you must not leave heat unattended.

Every limitation has an owner and a review date, even if the review date is “before any use beyond the bench.” Limitations without review dates become permanent by neglect, including the ones that were only true of the prototype for a month. If you clear a limitation by modification, you re-run the gates the modification touches and you remove the sentence. You do not leave the sentence and add a handwritten “fixed” that the next reader will not trust.

Limitations that forbid representation of the current interface revision, because the revision moved, stay until the unit is modified or the claim is dropped. Do not delete them because they are inconvenient in a meeting.

## The user note

Include a note that lets a stranger check each function against the file without a tour. The note is a procedure for a single plateau, a stop, and an export, written so that a person who did not build the unit can do those three things and recognize a bad result. It references the diagram and the point list. It does not introduce new setpoints that are not on the duty sheet. A user note that contains a second, unofficial duty is how the official duty decays.

The note includes how to shut down, how to kill control power, and what “safe” looks like afterward. It includes the fill and drain story, or the statement that the user does not drain. It includes the valve line-up. It does not include folklore: the kick that makes a valve seat, the menu no one documented, the laptop that must be present. If a kick is required, the unit failed acceptance. Do not enshrine the kick in the note.

If the only way to learn the machine is to have been in the room when it was built, you did not deliver it. You delivered a machine and retained the knowledge. That arrangement feels efficient until the person who retains the knowledge is elsewhere on the day the hose kinks. The file is how the unit survives that day.

## What you leave out

Leave out quotations, contracts, rental rates, attendance sheets, and shipping invoices. They decide whether a project happens. They do not decide what pass means, and they often contain names and commercial terms you have no business copying into a technical file that will be forwarded.

Leave out site drawings, point lists from a building, and photographs that identify a customer or a hall. The unit should be describable without them. If a mating detail cannot be described without a confidential drawing, cite the drawing’s title and revision and keep the drawing in the project system that is allowed to hold it. Do not paste it here to be helpful.

Leave out a second design narrative that contradicts the authority sentence. One story. If you like an alternative story, it is not in this file until it has replaced the first through the revision rule.

Leave out raw dumps from a controller that no one has mapped to the point list. Unmapped dumps look thorough and cannot answer the stranger’s questions. They will be forwarded as if they were evidence. Store them as debug material if you must, labeled debug, not labeled acceptance.

## The handoff

Handoff is a meeting in which the receiver uses the file, not a meeting in which you talk while they nod. They find the claim. They find a limitation and restate it. They point to the local stop on the unit and on the diagram. They open the export you archived and answer the stranger questions. They find the interface citation. If they cannot do one of those, the file is not handed over. Fix the file or teach the missing map, then make them do it. A signature without the exercise is a ceremony.

Record the handoff: who received, which file revision, which unit identity, what they were able to do without help. That record is the last page. It is also the first page of someone else’s responsibility. Make it match.

If you are both the builder and the receiver, the exercise still requires a second person for the stranger portion. One-person projects fail the file in private and discover the failure in public. Borrow the second person for an hour. It is cheaper than a wrong claim.

## Composite: the thick binder

A team delivers a binder with a rendering, a quote, a cable schedule, and a chapter of marketing descriptions from a component vendor. The authority sentence is absent. The acceptance record is a signature on the last page of the quote. Months later nobody can say whether the spare port was real. The binder was heavy. The file was empty. Weight is not completeness. The packing list in this chapter is the test. If a required item is missing, the binder does not compensate.

## Composite: the unofficial setpoint

The user note says the unit is “usually” run at a convenient command that is not on the duty sheet, because that command made a nice temperature rise on the bench. Operators follow the note. The duty sheet becomes decorative. The fix is to delete unofficial setpoints from the note, or to add them to the duty sheet through the revision rule and accept them. A secret operating point is an unaccepted operating point. It will be the one in use.

## Public sources for this chapter

The delivery file carries a bibliography, not a library. Each entry is title, organization, edition or revision, date read, and the cell it informed. NVIDIA product page and datasheet, if used. ASHRAE titles, if used. Code editions, if used. No PDF of a licensed handbook. No screenshot of a datasheet table. No water-quality table retyped “for convenience.” A reader who needs the table uses the edition the bibliography names, under the license they hold. ASHRAE’s own statement is that its publication content is not an input to an AI tool and that AI derivative works need written permission. A file that includes a model’s paraphrase of an ASHRAE chapter is the wrong file. Replace the paraphrase with the citation.

## Decisions to record

- File revision matches unit identity on the day of handoff.
- Claim sentence and limitations agree with the gates, including reduced claims.
- Export files open without the builder’s laptop.
- Receiver completed the handoff exercise without a tour.
- Out-of-scope commercial and site material was not pasted in to make the file look finished.


# 9. What this book will not be

A field guide fails in two directions. It can be so vague that no one can write a sheet from it. It can be so specific that it becomes a leaked project file with the names rubbed off. This book is trying to stay in the middle, and this chapter is the guardrail. If a draft chapter, including one of the earlier chapters in your hands, violates the guardrail, the chapter is wrong. Do not defend it because it sounds practical.

## It will not be a rewritten vendor specification

Rack documents, CDU manuals, and component data sheets have owners and revisions. They also have limits on what you may copy. Even when you may copy, a paraphrase that drags their numbers into a book freezes a revision you do not control. The next revision makes the book false, and readers will still quote it, because a book feels more stable than a PDF.

If a sentence only makes sense as a paraphrase of a manual, delete it. Cite the document by title and revision on your own sheet. Keep, in the book, the reason you need that citation: flow regime, mating family, coolant compatibility, pressure the loop can apply. The reason survives a revision. The stolen setpoint does not.

This rule is also how you stay clear of publishing someone else’s test limits as if you had derived them. You did not derive them. You read them. Reading is not authorship. Authorship here is the method: the set, the gates, the stops, the file.

## It will not be one site, promoted

Fitting families, unit counts, network addresses, module maps, hose lengths, and alarm thresholds from a project stay in the project. They were earned there, or borrowed there, under a duty and a coolant and a manifold that are not universal. Promoted into a book, they become a false standard. People will build to them because a book said so, and the book will have laundered a souvenir.

The book keeps patterns. Isolation with a visible state. A spare that is actually plumbed, or not called a spare. Hose routing proved at pressure in the position you will use. Stepped heat with a dwell and a measured watt, not a percentage folklore. Paired readings on the unit and at the comparison boundary. A data exit that marks stale values. Four gates in order. A local stop that does not ask the network. A file a stranger can use. Those patterns are the transferable part. If a sentence needs a project fact to be true, it is not transferable. Cut it or rewrite it as a check.

Composite scenes in this book are teaching scenes. Do not add a place, a customer, or a model number back into them when you reuse a checklist. If you recognize a scene, that means the failure is common. It does not mean the book documented your site, and it does not give you permission to document your site in the margin and forward the margin.

## It will not invent numbers

Where a figure would make the page look finished, and you do not have both a source and permission to publish it, write the check. Confirm flow, temperatures, differential pressure, and the mating family against the rack specification then in force, and write them on the duty sheet before acceptance. That sentence ages better than a borrowed setpoint, and it is the sentence an honest engineer can defend in a room where a vendor disagrees.

Inventing a “typical” number is still inventing. Typical is how folklore enters a table. If you need a worked example with digits for training, label every digit as fictitious and do not let the fictitious digit sit in a checklist cell where someone will copy it. This book mostly refuses the fictitious digit as well, because readers copy. The refusal is intentional. A blank with a citation column is harder to misuse than a plausible fake.

If a calculation needs a constant you cannot stand behind, do not print the calculation as if it were design data. Print the structure of the argument: heat, flow, and temperature rise move together; a missing one can imitate a healthy value of another. The structure is the lesson. The constant can live on the project sheet when the project has a source.

## It will not be a fabrication package

No hole sizes, no welding procedure, no torque table, no enclosure cut file. Those are real work, and they are the fabricator’s work, done against your sheet. If this book included them, two bad things would happen. Readers would treat them as universal. And readers would think the book had designed their unit, when it has only told them what the unit must be able to prove. Fabrication that cannot meet a gate is failed fabrication, even if it matches a drawing this book does not contain. Fabrication that meets the gates with a different internal arrangement is a success this book has no reason to forbid.

If you are the fabricator, use the book as the examiner’s questions, not as the shop drawing. If a question cannot be answered from your drawing, the drawing is incomplete in the way that matters, which is the way acceptance will notice.

## It will not be the data book or the project book

How to clean a record, how to compare a month of plateaus, how to tell a CDU oscillation from a load-bank valve hunt: that is the next book. This book stops at “the export must make those questions possible.” If you need the answers in order to accept the prototype, you have mixed the volumes. Acceptance uses the stranger test and the heat story on the day. It does not use a statistical method you have not written down. Do not pretend this volume taught the statistical method in a paragraph.

How to run a hall, how to staff a window, how to coordinate one NVL72 test with a live CDU and a customer: that is the book after. This volume tells you what the stand-in must be so that the later test is not limited by a toy. It does not schedule the later test. A sentence that starts “on the day of the hall test, call…” has wandered. Bring it back or cut it.

## It will not launder confidentiality

Project files that informed the method may be confidential, commercial, or simply not yours to publish. The method survived extraction. The identifiers did not come with it. Do not put them back in appendices “for completeness.” Completeness is the enemy of this chapter. A complete dump of a project is a leak with a table of contents. If a reader asks for the underlying site data, the answer is no. The answer is the sheet they must write for their own interface, cited to their own revision.

The same refusal applies to component manuals that are not public, and to test reports that name a customer. Cite what you are allowed to cite. Omit the rest. A gap in the story is better than a name that was never cleared.

## It will not pretend agreement is a standard

Two projects can both be competent and still specify different fitting families, different plateau fractions, and different overload dwells. This book does not resolve that difference by voting. It tells you to cite your source and to accept against your sheet. If two groups in your own company disagree, that disagreement is yours to close before Gate 3, not mine to close by sounding confident. Confidence without a revision is a tone. It is not a duty point.

When someone says “the standard load bank” and cannot name a revision, they are asking you to skip the sheet. Do not. There is no standard unit hiding in this book. There is a standard shape of work: write the job, cite the window, build only what the job requires, accept in four gates, hand over a file. Units that come out of that work will differ. That is success, not inconsistency.

## Kills

Some findings end the claim, or end the project, and should not be negotiated away in prose.

You cannot name the interface specification, and you still want a universal fitting and a universal flow. Kill the universality. Keep the method. Do not invent the missing specification to keep the chapter smooth.

The heat story cannot be formed, because flow or temperatures are absent, and you still want to say the unit loaded the loop. Kill the sentence. You may say the contactors closed. You may not say more.

Stale data is painted as live, and the vendor offers a screenshot instead of a fix. Kill the data-exit claim. Do not accept the unit “except for data” if the later books need data. A heater with a story is not the product.

The only stop path asks the network for permission. Kill the unattended claim, and do not ship a procedure as if it were a contactor. Fix the circuit or forbid the use.

A spare, a hose routing, or a module-service claim is false in the object, and the schedule wants a note instead of a fix. Kill the false claim or fix the object. A note that preserves the claim is a lie with a softer verb.

You need a stolen setpoint to make a chapter, a quote, or a gate look finished. Kill the page, not the pause. A blank you can explain is a professional object. A filled blank you cannot source is a defect.

If you hit a kill, say so in the file, in plain words, and stop the affected claim. Stopping is part of the method. A field guide that cannot tell you to stop is a sales sheet.

## What you should have when you close the book

You should have a requirements list and an acceptance sheet, blank where citation is still due, filled where you have authority, ugly in the way honest documents are ugly. You should have a one-line diagram and an authority sentence. You should have a limitations page that already contains the refusals, not only the hardware gaps. You should be able to explain, without numbers you do not own, why high rack-side flow changes the machine, why a single temperature is a mood, and why a gate that has not been written as a stop is not a gate.

If you have a rendering and a kilowatt figure and a sense that the software will be flexible, you have not finished. Go back to the six functions. They are still the start. Flexibility is what people write when the plateaus are unnamed. Name them, or admit the unit is off and full, and accept the consequences in the file.

The work after this book is not more introduction. It is the sheet, used on a real prototype, against a real revision, with the gates in order. The book cannot do that visit for you. It can only make the visit harder to fake. That is the whole offer.

## Public sources for this chapter

The kill list grows by one. If a sentence only works as a paraphrase of an ASHRAE publication, an NVIDIA datasheet, or a code article, the sentence is killed. The citation remains. ASHRAE has published a position that its intellectual property is not to be entered into AI tools or turned into AI derivative works without written permission. NVIDIA’s pages and datasheets are NVIDIA’s. Codes are the standards bodies’. A field guide that launders them is not more useful. It freezes a revision. Chapter 19 is the working rule. This chapter is the stop.


# 10. The two sheets, line by line

The early chapters told you to produce a requirements list and an acceptance sheet. This chapter sits with you while you do it. It does not fill the numbers. It fills the prompts, and it says what a weak answer looks like so you can reject your own first draft before a vendor does it for you.

Copy the headings into your own file. Leave the citation cells blank until you have a title and a revision. Do not paste this chapter into a purchase order. It is a tutor, not a specification. A purchase order that quotes a tutor is how a book accidentally becomes a contract.

## Header

Unit identity, or “unassigned” if the metal does not exist yet. File revision. Date. Sheet owner. Scope signer. Interface owner, who may be a role rather than a person in the room. Claim sentence, two clauses: represents, does not represent. Interface specification title and revision, or “unknown, due on” and a date. Coolant citation, same pattern. Electrical supply citation, same pattern.

A header without a due date on the unknowns is a header that plans to stay ignorant. Put the date. If the date slips, revise the header. Do not let the old date stand as decoration.

Weak header: “NVL72 load bank, various sites, standard coolant.” There is no standard coolant in this book. There is a citation you have not fetched.

## Row: adjustable flow

Statement: the operator named on the acceptance sheet can move flow across the band on the duty sheet and hold each declared flow point for the dwell, without rebuilding hose and without a private trick. Observed where: the path named in the authority sentence as the stand-in flow. Evidence: indicated flow and a check method, both recorded, at not fewer than two declared points. Do-not-ship if: command or handle moves and indicated flow does not, or indicated flow moves and will not hold, or only the person who built the unit can recover the point. Owner: sheet owner. Status: written, unknown, deferred, or cited.

Write the authority sentence under the row if it is short. If flow adjustment is outside the unit, this row must say so, and the limitations must forbid a claim of on-unit adjustment. Do not leave the row saying adjustable while the authority sentence says the CDU does it. That contradiction is a failed sheet, not a nuance.

Weak row: “flow control included.” Included where. Shown how. Failed how. If you cannot answer, the row is a brochure line. Delete the adjective and start again.

## Row: temperatures

Statement: supply and return temperature, as named on the diagram, are readable by a person in the room and by the export. Observed where: the taps on the diagram, not “in the system.” Evidence: both values in the export at the declared interval, with units and quality, and a check comparison that does not change the heat story or that is explained. Do-not-ship if: only one temperature exists, or the export can repeat a stale temperature with a fresh time, or the tap is in a stub that leaves the stream. Owner. Status.

Add a sub-line for which sensor, if either, is allowed to remove heat. If neither is allowed to remove heat, say which other sensor is. A temperature row with no path to a stop is a display row. Display rows do not satisfy the protection function. They can still exist. They must not be the only temperature story.

Weak row: “high-accuracy temperature.” Accuracy unnamed, location unnamed, stale-data behavior unnamed. High is not a specification. It is a mood.

## Row: flow readable

Statement: flow on the stand-in path is in the export at the same times as the temperatures. Observed where: meter location on the diagram, with installation assumptions written, including whether straight lengths are satisfied. Evidence: reading present, quality flagged, check method named at the duty point and at one reduced point. Do-not-ship if: the meter is on a bypass and labeled as heater flow, or the only “flow” is a pump curve inference you did not declare as a limitation. Owner. Status.

If you have more than one branch and you will command them independently, repeat the row per branch. A single row for a multi-branch claim is how one meter launders three paths.

Weak row: “flow meter, good brand.” Brand is not evidence. A good brand in a bad elbow is a bad reading.

## Row: pressure

Statement: pressures sufficient to form the differential pressure in the duty set are readable at the locations on the diagram. Observed where: high side and low side named. Evidence: both in the export with flow, or a differential device whose ports are drawn. Do-not-ship if: a single undirected gauge is the only pressure, or taps are valved off and still reporting. Owner. Status.

Add the absolute-pressure survival question as a sub-line, not as a performance target: weakest wetted component versus the highest source you will connect, including the bench. That sub-line connects this row to the overpressure stop. If it is blank, Gate 1 is not ready.

Weak row: “pressure monitoring.” Monitoring without a side is a word.

## Row: stepped heat

Statement: the unit can sit at the named plateaus, defined as measured electrical power unless you have explicitly defined them otherwise, for the named dwells, and can perform the sudden increase between the two plateaus you named. Observed where: power in the export, heat command in the export, liquid set in the export. Evidence: Gate 3 record. Do-not-ship if: the unit is only off or full, or percent does not correspond to measured power and you still script in percent, or the sudden increase is an undocumented stagger. Owner. Status.

List the plateaus here by name and by what kind of number they are: fraction of cited duty, or project choice. Do not list a dozen. If the list has an item no gate will sit on, delete it now. Unused plateaus become unofficial setpoints later, which is worse than not having them.

Weak row: “0–100% adjustable.” That row has never failed a unit and never will. It cannot fail a unit. Replace it.

## Row: overtemperature protection and alarm

Statement: overtemperature removes heat and latches an alarm that says overtemperature, locally, with the network dead. Observed where: the sensor you named, at the place you drew. Evidence: non-destructive test method named, to be run at Gate 2 and confirmed in spirit at a low plateau. Do-not-ship if: the only trip is silent, or the only alarm is a code with no words, or a failed sensor continues the last setpoint. Owner. Status.

Name the failed-sensor behavior in the row, not in a philosophy section. Philosophy sections are skipped on the day. Rows are not.

Weak row: “has protection.” All unsafe units have a slide that says this.

## Interface line: liquid

Statement: mating family per the cited specification, hose owner named, spare defined as plumbed or not claimed, isolation on supply, return, and spare. Observed where: the boundary on the diagram. Evidence: Gate 1 reaches and a mate-demate or joint inspection as appropriate to the family. Do-not-ship if: family does not match the citation, spare is a plug while claimed as a connection, or a hose kink is required to reach the manifold position. Owner: interface owner for the family, sheet owner for the routing. Status.

Leave the family blank rather than guessing from the last project. A blank is a question. A guess is a false part.

Weak line: “compatible with NVL72.” Compatible is the word vendors use when the family is unresolved. Make them name the family against the citation, or make yourself name it and own the risk in limitations.

## Interface line: power

Statement: delivered unit requires the supply you cited; acceptance feed is that supply or a written difference. Observed where: nameplate and the plug or hardwire point. Evidence: earth and insulation results per the rules you cited, local disconnect test, breaker-open test. Do-not-ship if: an adapter defeats earth, or acceptance ran on a feed you will not ship to and the difference is unwritten. Owner. Status.

Weak line: “standard power.” Name the citation. If the hall and the bench differ, the line is two lines. Do not average them.

## Interface line: air-cooled companion

Statement: either “not in scope” or a separate mini-sheet with steps, alarm, and power, explicitly not part of the liquid gates. Evidence: none, if not in scope. Do-not-ship if: the companion’s faults are used to waive a liquid gate, or liquid faults are waived because the air unit looked fine. Owner. Status.

Weak line: a blank that might mean out of scope or might mean forgotten. Write “not in scope” if that is the decision. Blanks on scope are how scope returns during acceptance as a surprise crate.

## Duty block

One nominal set. Columns: quantity, side of boundary, value or “cited, not copied here,” source title and revision, false story if missing, why the acceptance place exists. Rows: heat into the liquid, flow, differential pressure, supply temperature, return temperature, electrical power. Then a short list of other places: reduced, middle, full if full is not nominal, zero, overload visit. Each place has a dwell and a why.

Add a row for minimum flow for heat permitted. That row is a protection input, not a performance boast. If it is missing, the low-flow interlock has nothing to compare against.

Weak duty block: a single kilowatt number in bold, and five liquid cells marked TBD for six months. The kilowatt number will be remembered. The TBD will be forgotten. If the liquid cells are unknown, the kilowatt number is not a duty. Mark the whole set unknown rather than letting one cell look finished.

## Limitations block, started early

Open this block on the day you open the sheet, not after failure. Seed it with the refusals you already know: no universal fitting invented by this project, no overload-as-rating, no claim on CDU behavior, no claim on IT performance, no unattended heat if leak detection is absent. Add hardware limitations as you earn them. A limitations block that appears the night before the truck is a negotiation, not a record.

Each limitation: does not, therefore you must not, owner, review date. If you cannot write “therefore you must not,” the sentence is a worry, not a limitation. Worries go in a notebook. Limitations go in the file.

## Acceptance sheet header

Unit identity matching the requirements header. Requirements revision being used. Loop description and whether it meets the minimums. Feed description. Roles: sheet owner, operator, recorder, stranger. Waiver authority, written as a name or as “none on the day.” Export location. Date.

If the requirements revision on this header does not match the file you think you are using, stop. You are about to accept the wrong document. This happens when two people edited two copies. One copy wins, by the revision rule, before any valve is touched.

## Gate 1 lines

Write these as lines you can initial, not as a paragraph you can admire.

Diagram matches object in the streams named. Supply isolation reach, label, visible state. Return isolation, same. Spare matches definition. Drain and vent, or limitation already signed. Hose routing in the position of use, pressurized look, no kink, no rub. Fitting family matches citation, adapters drawn. Materials-versus-coolant row signed. Module removal and re-fit, or sealed-section limitation signed. Reaches repeated after re-fit. Labels readable with hoses on. Relief pointing, if fitted. Drip path does not enter electrical section. Fill procedure executed from the file with the author silent. Leak test at the cited condition, claim reduced if the condition was milder than the window. Valve line-up recorded.

Each line: pass, fail, not started. A line without a box will be skipped when you are tired. Boxes are the method.

Add a line: no do-not-ship cell was edited during this gate. That line protects the revision rule when everyone is standing up.

## Gate 2 lines

Feed matches, or difference written. Earth and insulation recorded against criteria. Local disconnect prevents remote heat. Breaker-open behavior matches the drawing. Identity commissioned, written here. Minimum points present with unit, time, quality. Stale-data proof performed, result attached. Stranger mapped columns to diagram at idle. One protection alarm by simulation, action and latch confirmed. Network-loss test, resulting state is heat off. Power-cycle with remote silent, resulting state is not default full load. Local and export do not disagree without a signed limitation.

If a line cannot be performed because the unit has no network, rewrite the line to the thing that exists, and limit the claim to local use. Do not mark a network line pass because there was nothing to fail. Not started, with a limitation, is the honest mark. Pass is a claim that a test happened.

## Gate 3 lines

Export started before the first command. Self-check recorded or “no self-check” already on the sheet. Ready state with heat off. Each plateau: command, measured power, dwell, heat story told or explicitly record-only, alarms explained. Sudden increase distinguished from ramp. Comparison probes unmoved during judged plateaus. Return to zero. Stranger reconstructed a plateau from the file without coaching. No band edited during the run, or waiver identifier written.

Include a line for the authority sentence: nobody trimmed a path that was supposed to be fixed, or trims were the ones allowed and were recorded. Unrecorded trims fail the gate even if the numbers look smooth. Smoothness is easy to buy with a hand on a valve and a quiet recorder.

## Gate 4 lines

Overload level and dwell are the ones on the sheet, not an extension. Exit to the named state completed. No new leak, no new kink, no stale data during the visit. Local stop practiced at a low plateau with remote command asserting. Control-power kill practiced at a low plateau. Override cleared afterward. Claim sentence still says the visit is not a continuous rating.

A line for the person whose job was to look at the unit rather than the plot: name them. If you cannot name them, the role was not filled. Do not leave it implicit that “everyone was watching.” Everyone was watching the screen. That is how hoses change shape off-camera.

## Close-out lines

Limitations page matches the gates, same day. Export opens on a machine that did not run the test. File revision bumped if the unit or the claim changed. Handoff exercise done, or explicitly not yet delivered. Second unit, if any, not declared accepted by resemblance.

The close-out is where people skip because the interesting part is over. The close-out is the delivery. A perfect Gate 4 with a missing export next month is a story you will not be able to retell. Initial the close-out with the same seriousness as the overload.

## How to use a failed line

Write the observation in one sentence. Write the disturbed lines you must repeat. Do not write the remedy as a pass. The remedy is a new attempt. Number the attempts. Attempt 1 fail, attempt 2 pass, on the same line, is a history. A single pass with the fail erased is a brochure. Keep both.

If the same line fails twice for different reasons, the design is talking to you. Two hose failures are not bad luck. They are a routing that is not fixed. Stop and change the routing requirement, or change the hardware, before a third attempt. Three attempts at the same line without a design change are how acceptance becomes a campaign to wear the recorder down.

## A fictitious walk-through, digits labeled false

Imagine a sheet where every numeric cell says “citation withheld, value not in this book.” The team still has to practice the motions. They mark nominal flow as cited. They mark a reduced flow as a project choice at “a fraction the sheet names,” without me telling you the fraction. They sit on it. The export shows a hold. The stranger says: command was the reduced plateau, flow held, temperatures moved in the direction heat would cause, quality stayed good. That sentence is a pass line and it contains no stolen number. If your real line cannot be written without a number you do not own, write the sentence and attach the number in your project file, not in a public example.

Practice that sentence once in your own words before the day. Teams who have never said a pass line out loud will write “OK” when the time comes. The sentence is a skill. The gates only create the occasion.

## Tabular Sheet 1: Liquid Load Bank Engineering Requirements

| Item / Function | Engineering Parameter & Target | Interface / Location | Verification Method | Do-Not-Ship Condition |
|---|---|---|---|---|
| Liquid Interface Coupling | Danfoss FD83-2051 (2" dual-interlock full-flow quick disconnect, C_v ≥ 12.5), female supply, male return | Rack manifold supply & return ports | Physical mating test & ball valve lockout inspection | Coupling lacks mechanical dual interlock, uses blade-level UQD adapter hose, or leaks during mate/demate |
| Nominal Thermal Duty | P_thermal = 120.0 kW into liquid stream (ΔT = 10.0 K, $35.0°C \to 45.0°C$) | Core electric heating bundle in fluid stream | Calibrated flow + RTD power balance: Q = ṁ C_p ΔT | Inferred thermal heat differs from electrical kW by > ± 3.0% at steady-state dwell |
| Flow Rate & Valve Authority | Q_v = 80.0–220.0 L/min (nominal 176.5 L/min for PG25); linear modulating TCV | Internal trim & bypass manifold | Electromagnetic / Coriolis flow meter | Indicated flow fails to hold setpoint within ± 2.0% or valve induces cavitation choke |
| Hydraulic Flow Resistance | ΔP_nominal = 115 kPa ± 10% (103.5–126.5 kPa) at 176.5 L/min rated flow | Inlet to outlet across FD83 couplings | Calibrated differential pressure transmitter (DPT) | Differential pressure deviates by > 10% from cited rack manifold resistance curve |
| Pre-Commissioning Flushing Bypass | 50-micron inline bypass strainer (V-105 loop) with differential pressure indicator | Full bypass loop isolating main heating vessel | 15-minute cold flush & basket particulate inspection | Bypass loop omitted, strainer > 50 μm, or strainer differential pressure unmonitored |
| Air-Cooled Companion Load | 15.0 kW sensible heat into data hall air (80:20 liquid-to-air heat split) | Top/rear chassis exhaust fan-coil elements | Thermal anemometer & air temperature sensors | Companion air heat omitted without written facility waiver, leaving CRAH unexercised |
| Dew Point Safety Margin | Supply temperature T_supply ≥ T_dp + 2.0 K (automated safety interlock) | Supply RTD cross-referenced with hall humidity/dew point | Automated modulating valve closure on dew point approach | Unit operates with coolant below dew point, causing condensation dripping onto equipment |
| Power Architecture | 2N Dual Feeder (Feed A and Feed B, 400V/480V 3-phase, lockable CB-101A/B) | Dual input power lugs and terminal block | Single-feed loss drop test during 100% full load | Tripping Feed A causes Feed B trip, or causes control PLC reboot / telemetry loss |
| Megger Insulation Resistance | DC 1000V applied for 60 seconds; insulation resistance R_iso ≥ 10 MΩ | Main 3-phase busbars to chassis PE frame | Calibrated DC Megohmmeter test | Measured insulation resistance < 10 MΩ, indicating coolant leakage or degraded dielectric |
| Dielectric Withstand (Hipot) | 1.5 kV AC power frequency applied for 60 seconds | Main circuits to chassis PE ground | Factory / bench calibrated Hipot tester | Any dielectric breakdown, sparkover, or current trip during 60-second dwell |
| Emergency Stop (E-Stop) | Hardwired trip dropping main contactors in ≤ 20 ms; 24VDC control logging remains alive | Local dual-channel mushroom pushbutton & remote loop | Contact opening oscilloscope timing test | Contactor drop exceeds 20 ms, or E-Stop kills 24VDC telemetry power |
| Industrial Telemetry & Export | Modbus-TCP / RTU holding registers & discrete coils; flat CSV export with quality bitmask | RJ45 Ethernet / RS-485 port and local storage | Stranger audit on flat CSV file with simulated sensor failure | Stale readings repeated with fresh timestamps; missing quality flags; proprietary raw files |

## Tabular Sheet 2: Liquid Load Bank Gate Acceptance Checklist

| Gate / Step | Inspection & Test Procedure | Engineering Criteria & Pass Limits | Recorded Field Measurement | Result | Witness Initial |
|---|---|---|---|---|---|
| Gate 1.1 | Danfoss FD83 coupling dual-interlock verification | Safety pin snaps into detent; ball valves locked closed when disconnected | [ Detent engaged / Valve lockout verified ] | Pass / Fail | [ ] |
| Gate 1.2 | Hose routing and minimum bend radius inspection | Minimum bend radius R ≥ 6D; zero kinks, rubs, or coupling neck strain | [ Measured radius: ___ mm (D = 32 mm) ] | Pass / Fail | [ ] |
| Gate 1.3 | Pre-commissioning flushing bypass & 50-micron strainer | 15-minute cold flush through V-105; basket clean of swarf, ΔP ≤ 10 kPa | [ Strainer clean / $ΔP = \_\_\_ kPa$ ] | Pass / Fail | [ ] |
| Gate 1.4 | Hydrostatic pressure hold & joint integrity | Cold hydrostatic hold at 1.5× rated pressure (9.0 bar) for 30 minutes | [ 30 min hold: 9.0 bar $\to$ ___ bar (0 leaks) ] | Pass / Fail | [ ] |
| Gate 1.5 | Drip path liquid-to-electrical isolation | 250 mL water poured over liquid section exterior with electrical doors open | [ Runoff to tray: 100% / Cabinet drops: 0 ] | Pass / Fail | [ ] |
| Gate 2.1 | Megger insulation resistance test | DC 1000V applied for 60 seconds between phases and chassis PE; R ≥ 10 MΩ | [ Measured $R_iso = \_\_\_ MΩ$ ] | Pass / Fail | [ ] |
| Gate 2.2 | Dielectric withstand (Hipot) test | 1.5 kV AC applied for 60 seconds between main power circuits and ground | [ Leakage current: ___ mA (0 breakdown) ] | Pass / Fail | [ ] |
| Gate 2.3 | Hardwired E-Stop contactor trip response | Assert mushroom pushbutton; main contactors drop in ≤ 20 ms; 24VDC alive | [ Trip time: ___ ms / PLC alive: Yes ] | Pass / Fail | [ ] |
| Gate 2.4 | Local disconnect lockout interlock | Open lockable CB-101; send remote Modbus start command; zero heater energization | [ Software override blocked: Verified ] | Pass / Fail | [ ] |
| Gate 2.5 | Modbus telemetry and stale-data proof | Disconnect flow sensor for 60s; controller marks quality bit bad; zero repeated stale value | [ Quality flag bad asserted: Verified ] | Pass / Fail | [ ] |
| Gate 2.6 | Stranger data audit at idle | Deliver idle CSV file to stranger; verify column headers, engineering units, clock | [ Stranger verified point list without assistance ] | Pass / Fail | [ ] |
| Gate 3.1 | Sequential load step plateaus (25%, 50%, 75%, 100%) | Hold 15-minute dwell at 30, 60, 90, 120 kW; thermal heat balance within ± 3.0% | [ 120 kW dwell: $Q_thermal = \_\_\_ kW$ ] | Pass / Fail | [ ] |
| Gate 3.2 | 2N single-feed loss drop test | At 120 kW load, trip Feeder A; Banks 1-2 shed instantly; Feed B & 24VDC hold | [ Feed B load stable / Zero PLC reboot ] | Pass / Fail | [ ] |
| Gate 3.3 | Sudden step response vs. hidden ramp | Step command 60 kW $\to$ 120 kW; instant command jump; thermal lag τ ≈ 45 s | [ Instant step verified / Zero stagger delay ] | Pass / Fail | [ ] |
| Gate 4.1 | Overload capacity stress dwell | Hold 135 kW (112.5% rated) for exactly 5 minutes; zero overtemp trip or hose bulge | [ 5-min dwell completed / Return to 0 kW ] | Pass / Fail | [ ] |
| Gate 4.2 | Final close-out and stranger data package audit | Complete CSV export delivered to stranger; thermal story reconstructed without author | [ Heat story reconstructed / All gates signed ] | Pass / Fail | [ ] |

## What the sheets are not

They are not a risk matrix with red and green icons. Color will be used to hide a fail inside a mostly green row. They are not a Gantt chart. Schedule does not pass a gate. They are not a vendor scorecard with weights. Weights are how a failed stale-data test becomes ten percent of a score and gets outvoted by paint. A do-not-ship cell is not outvoted. It stops the claim it belongs to.

If your organization requires a scorecard, attach it behind the sheets and do not let it edit them. If the scorecard and the sheet disagree, the sheet wins. Write that on the scorecard so the required process does not quietly become the real process.

## Public sources for this chapter

Citation cells on the sheet use the form in chapter 19: title, edition, date read, cell informed. A blank that says “see NVIDIA” fails the form. A blank that says “see ASHRAE” fails the form. The premises code and the equipment standard are two rows, not a single word, electrical. Do not paste a class table into the duty block to make it look finished.

## Decisions to record

- A requirements file with the rows in this chapter, blanks dated.
- An acceptance file with a box on every line, not a narrative in place of boxes.
- A rule that color, schedule, and weighted scores do not pass a failed line.
- One practiced pass sentence that contains no number you cannot cite.


# 11. Reading a proposal, and the bench you accept on

Most bad load banks begin as a plausible proposal and a convenient bench. The proposal answers a question you did not ask, in a unit you did not define. The bench makes that unit look successful by being unable to stress it. This chapter is how you read both before they harden into metal and habit.

## What a proposal is allowed to be

A proposal is a claim that a design will make your sheet true, plus a list of exceptions. It is not a replacement sheet. If you sent a vendor a rendering request instead of a sheet, you will get a rendering proposal. That is your fault. Send the sheet. Ask for exceptions in the form your limitations block already uses: we do not, therefore you must not. An exception written as “typical performance may vary” is not an exception. It is fog. Send it back.

Ask for the authority sentence in the vendor’s words. If they cannot say who sets flow and who sets heat, they do not have a design yet. They have a catalog item and a hope that your loop will cooperate. Catalog items can be the right answer. They still need the sentence. A catalog item that only works when an unnamed external valve is perfectly set is a component, not a load bank that meets the adjustable-flow row.

Ask where each sensor sits, in a sketch that uses your stream names. If their sketch uses a private vocabulary, make a translation table and attach it. Untranslated vocabulary is how their “outlet” becomes your “supply” in the export. Fix it on paper before it is fixed in a cable.

Ask for the stale-data behavior in one sentence. You are listening for “we repeat the last value.” That sentence is a fail of the exit, said early, which is a gift. Do not talk them out of admitting it. Write it as an exception and decide whether the project can fund the fix. If it cannot, decide whether you are buying a heater. Do not decide later, at Gate 2, when the metal is yours and the leverage is gone.

Ask for the stop path as a sketch of power, not as a software architecture diagram. Where does the contactor coil get its permission. What happens if that permission wire is cut. What happens if the controller reboots. Vendors who have a real stop path answer this without a workshop. Vendors who have a dashboard answer with a workshop and a promise. Prefer the boring answer.

Ask for module removal in a paragraph: what comes out, what stays full of liquid, what tool, what the neighbors do. “Modular design” is not a paragraph. It is an adjective. Adjectives do not pass Gate 1.

Ask which of your plateaus their hardware can actually sit on, in measured power, and which are software fiction. Ask what the sudden increase does in time relative to contactor staging. Ask them to mark any plateau they want you to drop. A vendor who wants a row dropped is negotiating scope. That is allowed. A vendor who says all rows are easy and discovers staging at Gate 3 is spending your acceptance as their development lab. You may still choose them. You will do it with your eyes open if you asked.

## Exceptions you should expect

Expect a request to treat the spare as a capped boss. Decide. If you agree, the claim changes. Do not agree verbally and leave the sheet saying spare connection.

Expect a request to skip rack-side comparison points because their sensors are “accurate enough.” Accuracy is not the issue. Location is the issue. Decline, or accept a limitation that forbids claims about the manifold as distinct from the unit.

Expect a request to demonstrate steps by a factory video. A video is not Gate 3. It can be a reason to visit. It cannot be a record. If distance is real, send the sheet and require the export from their factory run, then repeat the gates on your loop anyway. Factory loops are benches too. They have the same incentive to be gentle.

Expect a request to substitute a percent screen for measured power. Decline. Percent is a request. You are buying a result.

Expect a price that assumes a coolant, a fitting, and a flow you have not cited. Unpack the assumption. A price built on the wrong family is not a price. It is a later change order wearing a quote.

You do not need to be hostile. You do need the exceptions in writing before you award. An award that says “per proposal” without attaching the exception list has just accepted the fog. Attach the list. Mark each exception accepted, rejected, or accepted with a reduced claim. That marked list is part of your requirements revision on the day of award. It is not a side letter nobody will find.

## What you do not ask a vendor to invent

Do not ask them to tell you the rack’s current flow window if the interface owner should be citing it. They will guess, and the guess will enter the proposal as if it were your requirement, and you will accept against their guess. Give them the citation or tell them the cell is unknown and their design must show how it will be confirmed before Gate 3. A design that cannot wait for a citation is a design that has already frozen a souvenir.

Do not ask them to copy a point list from a building they once touched. You will inherit a hundred points and miss the five you need. Give them this book’s minimum set in your own names.

Do not ask them for a compliance matrix against a standard they cannot name by revision. Matrices against unnamed standards are green by default. Ask them which tests they will run, against which written criteria, and where the results will sit in your gate list. A test that does not map to a gate is optional theater. You may allow it. You may not let it replace a gate.

## The bench is a piece of test equipment

The temporary loop is not a neutral background. It is an instrument with biases. If it cannot absorb the heat of the longest dwell, every temperature will climb and you will condemn the unit or, worse, you will “finish early” and call the climb a pass. If it cannot deliver the flow band, you will accept at a gentle flow and discover the unit at the manifold. If it can deliver more pressure than the unit can survive into a closed valve, you will discover the weakest gauge.

Write bench minimums on the acceptance sheet before you build the bench, not after the bench happens to exist. Minimum heat absorption over the longest dwell, described as a capability, not as a brand of chiller. Minimum flow at the top of the band you intend to visit. Maximum pressure the bench can apply, compared with the unit’s weakest wetted component. A fill and vent path that does not depend on the unit’s own vents being perfect. A place for comparison probes. A feed that matches the power interface or a written difference.

If your bench cannot meet a minimum, you have three honest choices. Change the bench. Reduce the claim and accept only the band the bench can reach, with the limitation screaming. Delay Gate 3. There is no fourth choice called “it should be fine for a short test.” Short tests are how overload visits get done on inadequate sinks. The visit looks stable because it was brief. The file then implies a stability the sink was borrowing from its own thermal mass. Name the sink’s mass as a limitation or remove it from the story.

## Bench flow and the authority sentence

If the unit is not supposed to set flow, the bench must set flow, repeatably, and record what it set. A bench valve that only one technician can position is the same sin as a unit valve with no scale, just relocated. Record the bench valve state or, better, measure the flow and stop depending on the handle.

If the unit is supposed to set flow, the bench must not secretly set it too. A bench valve half closed, forgotten, will be “the unit cannot reach flow.” Start each gate from a recorded bench line-up. The line-up is part of setup. A bench with no line-up drawing is a bench that will change under you.

Pumps add heat. At high flow and low commanded heat, pump heat can be a large fraction of the liquid story. You will think the heaters are leaking watts into the liquid when the pump is the source. Either measure pump power and acknowledge it, or do not judge the heat story at a plateau where pump heat dominates. This is a bench problem wearing a unit costume. Write it down when you choose the low plateau. If the low plateau’s heat is comparable to expected pump heat, the low plateau is a bad place to judge and a fine place to record. Mark it record-only in advance, not after the numbers embarrass someone.

## Bench electrical habits

Temporary cables, temporary adapters, and temporary breakers are how earth gets defeated and how fault current becomes a fairy tale. If you must use them, they are part of the setup description, and they limit the electrical claim to “behaved on this temporary feed.” That limitation is often unacceptable for a delivered unit. Then the temporary feed is not an acceptance feed. It is a smoke test. Call it a smoke test. Do not file it as Gate 2.

A bench that cannot run the local-disconnect test and the control-power-kill test is not a bench. Those tests need no high flow. If you “cannot do them here,” you are saying the unit is already installed in a way that forbids proving the stop. That installation is early. Uninstall the obstacle. Prove the stop. Then install.

Shared feeds with other shop loads will sag when you step. A sag that trips the unit is not necessarily a unit defect, and a sag that the unit ignores is not necessarily a virtue. Record that the feed was shared, or do not share it during judged plateaus. Shared feeds are a fine way to weld. They are a poor way to accept.

## Factory acceptance versus your gates

A vendor’s factory test can be mapped onto your gates if you insist on the mapping in the purchase. Unmapped factory tests are ceremonies. Mapped factory tests still do not replace the gates on your loop, unless your loop is the factory and you have already decided the factory loop is the duty. For a rack-side stand-in, the factory rarely has your manifold position, your hose routing, or your comparison points. Use the factory for what it is good for: workmanship you would rather see fail before shipping, stale-data behavior, stop path, module removal. Use your gates for routing in position, duty set on a loop that meets the minimums, and the stranger test on the file you will actually keep.

Do not pay for a factory ceremony you will not witness and will not receive as data. If you cannot witness it, require the export and the line-by-line sheet, signed, with fails included. A certificate that says “passed FAT” is a souvenir. A sheet with lines is a record. You are allowed to require the record. If a vendor cannot produce it, believe them. They cannot produce it.

## Shipping and what it does to a pass

A unit that passed Gate 1 in one orientation may arrive with a hose rerouted by a person who needed it to fit a crate. The first act after delivery is not Gate 3. It is a repeat of the reaches, the valve line-up, and a leak look. Shipping is a disturbance. The disturbed-line rule applies to it. Teams that “already accepted it at the factory” skip this and start heat. They then interpret a kink as a site problem.

Write “post-ship repeat of Gate 1 reaches” into the project plan as a condition of using the factory record at all. If that repeat fails, the factory record is historical. It is not a description of the object now in the room. This is not an insult to the factory. Crates are persuasive. They persuade hoses into bad shapes.

## Second unit

If you will build more than one, the first accepted unit is not a type certificate. It is one identity with one file. The second unit gets the same gates. You may shorten a line only where you have a written reason that the line cannot differ between units, and even then a sample check is wiser than a skip. Hoses differ. Sensor placement differs. Software images differ. The assumption that the second unit is a copy is the assumption shipping departments make, and it is occasionally true. Acceptance does not rest on occasionally.

What you may reuse is the sheet, the diagram, and the lessons from the first unit’s fails. Update the sheet before the second unit’s Gate 1 if the first unit taught you that a row was untestable. Do not hand the builder the same untestable row and hope. That is how a known fail becomes a tradition.

Software images, if any, are part of identity. Record the image revision in the header next to the serial. Two chassis with two images are not the same design. A field update of the image repeats the Gate 2 tests the image can affect: stale data, default state on power-cycle, alarm text, stop path if the image is in that path. If the image is in the stop path, you have already violated the preference for a stop that does not depend on clever software. Repeating Gate 2 is the minimum apology. Removing the image from the stop path is the repair.

## Composite: the gentle bench

A bench pump cannot reach the cited high-flow end. The team accepts at the flow the pump can do, files a pass, and writes the duty cell from the citation anyway. The file now says the unit met a window the bench never applied. Months later the manifold test is “mysteriously” resistive. The unit was never a mystery. The bench was a smaller machine than the claim. The fix is the limitation that should have been written on the day: accepted only up to the flow the bench could deliver; high end of the cited window not visited; claim reduced. That sentence is annoying. It is also the only sentence that keeps the next test honest.

## Composite: the factory video

A vendor sends a video of a unit at full load, gauges in frame, no export, no identity, hose routed across an open floor. The purchase requires your gates. Someone still wants to skip Gate 3 because the video was “basically the same.” It was not the same unit in any sense the file can use, and it may not have been the same unit in the physical sense either. Videos do not have quality flags. Treat the video as marketing. Marketing is allowed to exist. It is not allowed to initial a line.

## Public sources for this chapter

A proposal that attaches a white paper has not answered the sheet. Ask which cell the paper is allowed to inform, and which edition. A factory test mapped to a code article is acceptable as a pointer to a test you will also run or witness. A factory test that consists of a pasted article is not your record. The bench feed still names the premises code edition, or the electrical claim stays limited to the temporary feed.

## Decisions to record

- Exception list from the proposal, each marked, attached to the awarded revision.
- Bench minimums written before Gate 3, with the heat-absorption and max-pressure lines filled or Gate 3 delayed.
- Factory tests mapped to gates or demoted to ceremony.
- Post-ship repeat of disturbed Gate 1 lines.
- Second-unit rule: own record, software image in the identity header.


# 12. Arguments you will have, and how to close them

Acceptance and design reviews fail socially before they fail technically. Someone needs the date. Someone trusts the display. Someone remembers a different project. This chapter is a set of arguments that recur, and a way to close each without inventing a number and without giving in to the schedule. Use it as a script only in the sense that the closing sentence is one you can say out loud. Do not use it as a way to win a room while the sheet stays false. The sheet is the close. The sentence only buys you the right to edit the sheet or to stop.

## “We have always used this fitting.”

The fitting in memory may be correct, and it may be a souvenir from a manifold that no longer exists. Close: the interface owner cites the specification then in force, by title and revision, and the family on the sheet matches that citation. Memory can nominate a candidate. It cannot pass Gate 1. If the cited family and the remembered family differ, the difference is a boundary problem with a date, not a compromise fitting that averages them. Adapters get drawn and get a pressure-drop story, or they are not used. There is no social version of an adapter, where everyone agrees not to mention it.

If there is no specification yet, the honest close is a blank and a due date, and a prototype that does not pretend to have passed the liquid interface line. You may still build heat and stops. You may not claim the stand-in.

## “Compatible with the rack.”

Compatibility is a conclusion, and only after a family, a hose, a routing, and a pressure story exist. As an opening claim it means nothing. Close: replace the word with the interface line filled or explicitly unknown. If a vendor will not replace the word, they do not have an exception list. They have a slogan. Do not award against a slogan. You will re-buy the interface later, at a worse time, with the rest of the unit already proud of itself.

## “The nameplate is the duty.”

The nameplate is the electrical promise the builder is willing to print. Duty is the set. Close: the duty block stands, and the nameplate is one cell, electrical power, still not identical to heat into the liquid. If the builder will only warrant the nameplate, write that as a limitation on the thermal claim and do not let the nameplate migrate into the flow cell. This argument often comes from a good faith belief that kilowatts are the hard part. In this class of rack they are not. Flow regime is the hard part. Say that, then point at the blank flow cell. A blank cell ends the argument faster than a lecture.

## “Temperature rise is small, so it is fine.”

Small rise is what high flow does to a given heat. It is also what failed heat does to a given flow. Close: the plateau is judged on the set, not on the rise alone. If the rise is inside the noise of the sensors, the plateau is record-only until the measurement can see it, or the sensors change, or the claim is reduced. Do not compliment a small rise. Compliments are how failed heaters pass. Ask for the power, the flow, and the quality flags. If those three cannot be said in one breath, you are not looking at a result. You are looking at a temperature.

## “The display matches, so the export can wait.”

It cannot wait if the product is a stand-in you will later analyze. Close: Gate 2’s stale-data line and the stranger test are do-not-ship for the data claim. You may ship a heater with a limitation that forbids use as a data source. You may not ship the claim and a promise to log later. Later logging arrives after the first controversy, which is the hour you needed the file. This argument is often made by the person who will not be present for the controversy. That is understandable. It is not a reason to weaken the gate. Write their name on the waiver if they force the point, and reduce the claim in the same edit. Make the reduction visible to the person who will run the later test. They are the one who pays.

## “We will add steps in software.”

Software can rearrange commands. It cannot create measured power you did not wire, and it cannot create a sudden increase if the contactors are staged by a hidden timer. Close: Gate 3 is about the object in the room. A later image is a later acceptance of the lines the image touches. If steps require a second delivery of hardware, say so now and split the purchase. Do not accept the first delivery as if it were the second. A payment milestone tied to “software complete” is a commercial fact. It is not a thermal fact. Keep it off the gate sheet.

## “One red lamp is simpler for operators.”

It is simpler, and it deletes the reason. Close: lamps may summarize. They may not replace words in the record. An operator who needs simplicity still needs the record to say overtemperature rather than fault, because the operator will not be the person explaining the hour next month. If the display is truly tiny, the words can live on the export and on a local legend plate that maps a code to a sentence. An unmapped code is a fail. Simplicity that cannot be expanded into a sentence is not simplicity. It is loss.

## “The CDU will protect it.”

Sometimes the CDU will. The bench will not. A future loop will not. Close: any protection that lives only in the CDU is a limitation, and it forbids unattended connection to other sources, and it does not pass the overpressure or low-flow stop on the unit. If the project accepts that limitation, write it in the form “does not, therefore you must not,” and make the bench comply. If the project cannot accept it, the stop has to move onto the unit. There is no middle where the CDU is “usually” there. Usually is not a sensor.

## “Factory already passed it.”

Mapped, witnessed or exported, line by line, the factory may have passed some lines. Close: post-ship repeat of disturbed lines, and your loop for any duty line the factory loop did not reach. A certificate is not a line. If the factory record omits fails, it is not a record. You do not need to accuse anyone of lying. You need the lines. Absence of lines is enough to rerun the gate. Rerunning is cheaper than a wrong claim in a hall.

## “The second unit is identical.”

Identity of design intent is not identity of the object. Close: the second unit gets a record. You may copy the sheet. You may not copy the initials. Software image revision is part of the header. If someone wants a skip, they can propose the skip as a limitation on the second unit’s claim, not as a resemblance. Few people will sign “we did not look.” That reluctance is the method working. Let it work. Do not help them by offering a “spot check” that has no lines. A spot check is a short gate, still with boxes.

## “The stranger does not understand the system.”

If the stranger cannot reconstruct the command and the heat story, the failure is the file or the export, not the stranger, unless you chose a stranger who cannot read a table. Choose someone who can read a table and who was not in the build. Do not choose someone who needs a tour, and do not choose someone so removed that they refuse the task. Close: fix names, units, and quality until a competent stranger can answer. Coaching during the test invalidates the test. If you hear yourself explaining a column, that column failed. Stop explaining. Rename it. Run the test again on the renamed file. The second run is the one that counts.

## “We edited the band because it was close.”

Close is a miss. Close: the miss is a fail or a waiver with a reduced claim, same day, new revision. Editing during the run is itself a failed line, the line that says the revision did not change in the hallway. You may write a new band before the next attempt, in daylight, with a reason, and accept against the new band. You may not pretend the old band was met. “Close” is how windows migrate until the citation is a decoration. If the band was arbitrary, admit it was arbitrary and replace it with a record-only plateau. Record-only is cleaner than a band you are willing to edit.

## “Overload went well, let’s call that the rating.”

A visit is not a rating. Close: the claim sentence stays as written unless you design a continuous duty and accept it with plateaus, dwells, and a heat story at that level, on a loop that can absorb it for a long dwell, not a short visit. If you want that, it is a new nominal, and Gate 3 must sit there. It is not a promotion you award at the end of Gate 4 because nothing burned. Nothing burned because you left. That is the point of a dwell limit. Respect it after the fact, not only during the minute it is running.

## “We need a number for the slide.”

Slides are how invented numbers escape. Close: the slide cites the specification, or it says the value is not yet cited, or it shows the shape of the set with the cells blank. A slide with a plausible number and no revision is a defect in the same family as a false duty cell. If communications staff need a number, give them the claim sentence instead. If they cannot use a sentence, the slide is the wrong medium for this project. Let the slide be ugly. Ugly slides get fewer false quotations.

## “The book said we could.”

This book said you could write a check, not that you could skip it. Close: point to the decision line, not to a mood. If a chapter and the sheet disagree, the sheet is yours and the chapter may be wrong. Fix the sheet in daylight, or fix your reading. Do not cite the book as authority for a fitting, a flow, or a waiver. The book is not an interface owner. It is not a waiver authority. Anyone waving the book at a do-not-ship cell has misunderstood the book. Read them the kill list. Then do what the sheet says.

## “Confidentiality prevents us from writing the duty.”

Confidentiality prevents you from publishing the duty in a book and from pasting it into a file that will be forwarded to people who should not have it. It does not prevent the interface owner from writing the duty on the project sheet that is allowed to hold it. Close: the project sheet gets the citation and the values, in the system that may hold them. This book’s public pages stay blank. Acceptance still uses the values. If even the project sheet cannot hold them, you cannot accept, because acceptance would have nothing to judge against except a rumor. Say that. A project that cannot write its own duty down cannot accept a stand-in. That is a project problem. Do not solve it by inventing a public number.

## “A small leak is normal on first heat.”

Weep at a joint is information. It is not a tradition. Close: Gate 1 leak line fails, the joint is repaired, the disturbed lines repeat. A small leak that appears only when hot is exactly the leak a cold test misses, which is why a hot claim requires a hot look. Normalizing it will train the next unit to weep. It will also train operators to stand next to a weep during overload, which is the wrong lesson sitting next to the electrical section. Fix the joint. If the joint cannot be fixed within the family you cited, the family or the installation has failed. Change it in daylight.

## “Air in the line will work itself out.”

Sometimes air leaves. Sometimes it sits in a high point and makes the flow meter lie for the entire gate. Close: vent as the fill procedure says, or fail the fill line. Do not start judged plateaus on a hopeful burp. A burp during a plateau invalidates the plateau. Record it as a disturbance, not as color. If the unit cannot be vented, that is a design miss from the liquid chapter. Go back. Do not compensate with a longer dwell. Longer dwells do not remove a trapped pocket. They only make the pocket traditional.

## “The operator nudged the valve, but the average looks right.”

Unrecorded authority changes break comparability. Close: the plateau fails the authority line. Repeat it from a recorded line-up. If the nudge was necessary, the authority sentence was wrong. Revise the sentence, then redesign or re-accept. Do not keep the sentence and the nudge. Averages hide the nudge and convince the next reader the path was stable. The next reader is who the file is for. Do not lie to them with a mean.

## How to stop a meeting that is eating the sheet

Read the do-not-ship cell that the meeting is trying to dissolve. Ask whether the speaker is waiving it. If yes, they sign, and the claim reduces in the same revision. If no, the cell stands, and the meeting can continue on other rows. If they will neither sign nor stand, the meeting is not a review. End it. Endless discussion is a waiver with extra steps and no signature. You do not have to be dramatic. You have to be willing to leave a row marked fail. A fail that is visible is a project still in contact with reality. A pass that is verbal is a project already writing its own legend.

Write the outcome before people stand up. Rows change only by revision. Actions get owners and dates. A meeting with no edited revision and no fail mark did not happen, technically, however long it felt. Send the revision or the fail list the same day. Next-day memory will soften every stop into a note. Same-day text is part of the method, not clerical fussiness.

## Arguments that should not be closed quickly

Some disagreements are real and should stay open, with a date, rather than being forced into a false pass. Whether the cited window’s high-flow end is achievable by this chassis is a real disagreement until a bench can apply it. Leave Gate 3’s high end not started. Whether a material is compatible with a coolant the interface owner has not named should stay open, and should block the materials row. Whether the stop path is independent of the controller should stay open until the kill test, and should block any unattended claim. Speed in those cases is how you buy a week and sell a month. An open row with a date is a professional object. Treat it as one.

## Public sources for this chapter

“The white paper says so” is not a close. The close is the edition, the cell, and whether the text may be copied. It may not. “ASHRAE requires this number” is not a close until the speaker can name the edition and is allowed to hold that number on the project sheet. Even then the number does not enter this book. “NVIDIA says thirty times” is a slogan. It does not fill a duty cell. Point the speaker at chapter 19 and return to the cell they were trying to dissolve.

## Decisions to record

- Which of these arguments is already active in your project, and which cell it is trying to dissolve.
- The close you will use, written as a sheet edit or a fail, not as a slogan.
- A same-day habit: revision or fail list before you leave the room.
- The rows you are explicitly leaving open, with dates, so openness is not confused with pass.


# 13. Owning the unit after the gates

Acceptance is a day. Ownership is the period in which the unit remains the thing the file describes. Most stand-ins drift. Hoses get rerouted, images get updated, limitations get forgotten, and a convenient plateau becomes the real duty. This chapter is how you keep the accepted object and the file the same object. It is still not the project book. It does not run the hall test. It keeps the tool honest until that book needs it.

## The unit is the file plus the metal

If the metal changes and the file does not, you do not have the accepted unit. You have a descendant. Descendants need gates on the lines the change disturbed. This sounds bureaucratic the first time and obvious the first time a hose swap explains a bad week. Write the rule where the operator can see it: no change without a mark, no mark without a disturbed-line decision. The mark can be a line in a log. The log is part of the file. A log that lives in a chat is not a log. Copy it or stop calling the chat the history.

Changes that always count as disturbances: hose replacement or reroute, fitting replacement, sensor replacement or relocation, valve replacement, software image change, contactor or protection-device replacement, relief replacement, coolant change, and any edit to a do-not-ship cell. Changes that often get waved through and should not: a “same” sensor from a different batch, a clamp of a different type, a longer hose that still “reaches,” a display that looks the same and logs differently. Sameness is a claim. Test it or do not claim it.

Changes that can be recorded without a full Gate 3: label replacement, documentation typos that do not alter a set point, a wheel or a handle that does not enter the wetted or protection path. Even those get a mark, because the habit matters. A team that marks nothing will mark nothing on the day the change was actually a disturbance.

## Storage and the next first fill

A unit that sits empty will collect dust in the fittings and will lose the valve line-up in people’s memory. Before storage, record the line-up and the image revision. Cap what the design says to cap. Do not invent a storage chemistry. Follow the coolant citation’s rules if the unit stays wet, and if you do not know them, do not store it wet and call that neutral. Wet storage of an unknown coolant is a materials experiment. Dry storage with open ports is a dirt experiment. Caps and a recorded state are the minimum.

The next use starts with Gate 1 reaches, not with a plateau. Storage is a disturbance you did not witness. Treat it like shipping. The operator who skips the look because “we only stored it for a month” is the operator who will explain a blocked meter as a CDU fault. A month is enough. A week is enough if the room was dirty. The look is cheap. The misdiagnosis is not.

## Unofficial plateaus

If operators discover a command that “works better” than the sheet, that command is either a new plateau or a bad habit. A new plateau needs a why, a dwell, a heat-story rule, and a revision. A bad habit needs to be removed from the user note if someone wrote it there, and removed from folklore if they did not. The way you detect folklore is to ask a new operator, without the builder present, what they usually run. If the answer is not on the sheet, the file has already lost. Update the sheet or correct the operator. Do not shrug. Shrugs are how the bench’s convenient rise becomes the project’s unofficial duty, and how the cited window becomes a poster.

Review this on the limitations review date. Ask what was commanded in the last real run, if a run has happened. Compare it to the sheet. A mismatch is a finding, even if the run “went well.” Went well is not a revision.

## Firmware and the stop path

If a software image can command heat, record its identity. If it can also hold the only permission to keep heat on, you have a design the safety chapter asked you not to ship. If you shipped it anyway, under a limitation, the limitation must say that an image change repeats the kill tests before heat is allowed. Do not “just update” a controller that sits in the stop path. That update is a new unit in the only sense that matters.

Prefer, still, to remove the image from the stop path. A contactor that needs a healthy operating system is a contactor that will be healthy in demos and absent in sags. Ownership includes the right to demand that modification even after acceptance, if the kill test was never really independent. If you discover late that the stop path depends on a boot sequence, stop unattended use the same day. Write the limitation. Schedule the circuit change. Do not wait for the next planned window. The window you need is the one before the next heat.

Keep a copy of the accepted image in the same place as the export archive. A unit that can be updated from a laptop that also contains three newer images will be updated from the wrong one. Identity includes a checksum or a vendor version string written on the header. If the vendor string is vague, ask for a build identifier before you accept. Vague strings are how two images share a name. Two images with one name will share a pass they did not both earn.

## Calibration and check methods

Sensors drift, and check methods drift. The acceptance comparison is a moment. Ownership decides whether that moment remains relevant. You do not need a metrology program dressed up as a science. You need a rule: before a run that will be used to claim the duty, the check method named on the sheet has been compared again, or the run is record-only, not judged. Record-only runs are allowed and useful. They must not be filed as confirmations of the window.

If a sensor is replaced, the comparison is not optional. The new sensor is a disturbance. It can be wrong in a new direction. The old bias, if you had characterized one, does not transfer. Delete inherited corrections when the sensor changes. Inherited corrections are a quiet way to manufacture accuracy. A correction is allowed if it is written, dated, and tied to a named comparison. A correction that lives in a spreadsheet nobody owns is a second, unofficial calibration. Delete it or adopt it in the file.

Flow meters that spent a year full of dirty liquid do not own last year’s acceptance. Inspect or compare. If you cannot, reduce the claim for that run. Say so at the start of the run, not in the conclusions. Conclusions are too late to relabel a judged plateau as record-only. The label is a setup decision.

## Coolant changes

A different coolant is a new materials row. Seals, hoses, and metals that were signed against the old citation are unsigned against the new one. Close the row again or do not fill. Mixing coolants because the barrel was handy is a materials experiment conducted inside your heaters. It is also a way to make leak detection and temperature sensors lie, if the properties changed. The duty set’s temperature meaning can survive. The compatibility signature cannot. Treat a coolant change like a fitting-family change: stop the claim, re-sign, or do not run judged heat.

If the cited specification changes coolant, the same rule applies even if the unit was happy. Happiness is not a signature. The interface owner signs again, or the limitations gain a sentence that the unit has not been reviewed against the new coolant and must not be filled with it.

## Who is allowed to command heat

Acceptance named an operator. Ownership must keep naming one, or name a role with a qualification that is more than “was in the room once.” The qualification is practical: can find the local stop, can read the valve line-up, can start the export before heat, can say the claim sentence and one limitation without opening the binder. If a person cannot do those, they may assist and they may not command. This is not a guild. It is a way to keep unofficial plateaus and skipped exports from being the night shift’s private culture.

Write the names or the role in the user note. Update them when people leave. A note that still names a person who left is a file that has started to rot. Rot in the user note is a leading indicator. The duty set is usually next.

## When the interface revision moves

The duty chapter already said: mark each cell still inside, no longer inside, or unknown. Ownership is the moment that rule either happens or is forgotten. Tie the review to the limitations review date and to any mail that announces a new revision. The announcement is not the review. The review is the marked cells. If nobody owns the announcement, you will hear about the new revision from a failed hookup. Assign the owner on the header now, while the old revision is still the one you accepted against.

If the new revision pulls a cell outside what you built, choose limitation, modification, or dropped claim. Do not choose “we will be careful.” Careful is not a cell. Modification reopens the gates the metal change touches. A new hose size is a liquid-path change. A new flow band may be a bench change and a Gate 3 change. A new temperature window may be a materials and relief change. Read the revision for what it disturbs. Do not read it only for the number that moved on the slide. Slides emphasize what the author found exciting. Your unit may be sensitive to a sentence the slide omitted. The owner reads the document, not the slide.

## Incidents

An incident, for this book, is any time heat stayed on when it should have come off, any leak, any relief lift, any stale-data episode that was used in a judged plateau, any shock or tripped breaker that is not understood, any hose that changed shape under pressure. Incidents are disturbances plus a lesson. The file gets a paragraph: what happened, which stop did or did not fire, what claim is reduced until a fix, which lines will be repeated. An incident that lives only in memory will be repeated as a story with the stop edited out. Write it down the same day, in the same tone as a failed gate. Calm prose. No blame paragraph. Blame paragraphs are how facts get negotiated away.

If the incident showed that a stop depends on the network, unattended heat ends until the circuit changes. Do not “monitor more carefully” as the repair. Monitoring is the thing that just failed to be a stop. The repair is a stop on the unit.

## Retirement

A unit that can no longer meet the claim should have the claim removed, not the unit quietly used for a lesser job without a new sentence. Lesser jobs are allowed. They are new claims, short ones: this unit may be used as a plumbing dummy with heat inhibited, or as a low-flow record-only source, or not at all. Leave the old acceptance in the file as history. Do not leave it in the header as if it still applies. People will find the header and ignore the history. Put the current claim in the first lines. Put the old claim under a superseded mark.

Scrapping or resale does not include handing over a file full of someone else’s site data. Strip the file to the unit’s own method and its own limitations, or hand over nothing but a warning that the unit is unaccepted. A file that travels with customer names and drawings is not a kindness to the next owner. It is a leak you chose at the end. The next owner needs the stops and the limitations if you give them anything. They do not need your project’s addresses.

## What ownership is not

It is not a reason to reopen the design every week. It is not a substitute for the hall-test book. It is not a calibration cult that never runs. It is a small set of habits that keep the gates from expiring in silence: mark changes, repeat disturbed lines, keep unofficial plateaus from becoming the duty, repeat the kill test when the stop path might have changed, read new interface revisions against the cells, write incidents the day they happen.

If you do only one of those, write incidents and mark hose changes. Those two prevent the worst lies. The others prevent the slow ones. A unit can fail by drama or by drift. The gates were for the day you could still see the drama coming. Ownership is for the drift.

## Composite: the helpful hose swap

A hose wears. A helpful person replaces it with a longer one from the wrong bin, routes it as best they can, and does not mark the log because the unit “is the same, just a new hose.” The next judged plateau shows a flow the sheet cannot explain. The CDU is blamed. The hose is the disturbance that the rule was written for. The fix after the fact is still the fix: stop the claim, look at the routing, compare materials to the coolant citation, repeat the reaches and the affected plateaus. The fix before the fact is a culture that treats a hose as part of the accepted object. Build that culture with the log, not with a speech. People follow a log that someone actually reads. Read it on the review date. A log nobody reads is a diary.

## Composite: the quiet image

A controller is updated “just for the display font” over a lunch. The font change shares an image with a change to default state after reboot. The next power sag returns the unit to a command. Nobody connects the sag to the lunch. The kill test, repeated because the image changed, would have connected them in five minutes, before the sag. Ownership is the decision to treat the lunch as a disturbance even when the person who brought the laptop is sure it was only a font. Their certainty is not a test. The test is the test.

## Public sources for this chapter

When a cited edition moves, the bibliography date moves with it. NVIDIA’s public generation name can change while your metal does not. ASHRAE editions and code editions move on their own calendars. Ownership is the review that marks each cell still inside, no longer inside, or unknown. You do not download the new PDF into a tool and ask it to update the book. You read the edition you are licensed to read, and you edit your sheet.

## Decisions to record

- The change log’s home, and the list of changes that always count as disturbances.
- The person who commands heat, and the four things they must be able to do.
- The image identifier in the header, and the rule that an image change repeats kill tests if the image can hold heat on.
- The owner of interface-revision review, and the date of the next limitations review.
- The current claim in the first lines, with superseded claims marked, not deleted.


# 14. One acceptance day, told in order

This chapter follows a single prototype through the four gates. The unit is fictional. The numbers are not supplied, because the point of the day is the order of the work, not a set of values you could copy. Where a real day would read a gauge, this day says “the sheet’s value” or “not the sheet’s value.” Fill yours from the citation. Do not fill this chapter’s blanks and then quote them.

The people are roles. The sheet owner is not the operator. The recorder writes sentences. The stranger is available in the afternoon and was not in the shop during the build. A fifth person, the builder, may answer questions and may not initial the do-not-ship lines. That separation is the whole social design of the day. If your day cannot staff it, you can still run the gates, and you should mark the role collision as a limitation on the independence of the record. Do not pretend the collision did not happen.

## The day before

The sheet revision is frozen. Unknowns that block a gate are either filled, dated past today and therefore blocking, or converted into limitations that reduce the claim. The bench minimums are written. The feed is the acceptance feed, or the difference is already a limitation and everyone has agreed the claim is reduced. The export path has been tried with a dummy run so that tomorrow’s first failure is not a missing cable. The builder has been told they will be asked to stay silent during the fill procedure. They have also been told that a fail is a line, not an insult. If you skip that conversation, the first fail becomes a quarrel, and the quarrel becomes an edit in the hallway.

The overload level and dwell are on the sheet already. They are not a discussion item for tomorrow morning. If someone intends to argue them, they argue today, in a revision, or they do not argue. The local stop is identified on the diagram so the person who must hit it does not search for it during a visit.

Print or freeze the line list. A line list that can still be edited by the same file the operator is using is a temptation. Freeze a copy. The live sheet can be revised only by the owner, between attempts, with a new revision mark. The frozen copy is what you walked in with. Keep it so the hallway edit has something to be compared against.

## Morning, before liquid

The recorder writes the header: identity, revisions, roles, loop, feed. The unit identity is read off the chassis, not off a memory. If the chassis has no mark, the day starts by making one, and the file header uses it. An unmarked chassis will be confused with its successor in the photographs people will take despite your warning that photographs are not the record.

Gate 1 begins empty of excuses and, at first, empty of liquid. Reaches first, because reaches do not require a fill and because a reach that fails should not be discovered after you have wet the floor. Supply isolation: hand on the handle, label readable, state matches the diagram, handle not blocked by the hose in the routing you will actually use. The routing is set now, not later. Someone will want to coil the hose for convenience and “route it properly at the end.” That is the composite failure from the liquid chapter, arriving on schedule. Refuse it. The position of use is the position of the check.

Return isolation, same treatment. Spare, compared with the definition rather than with the word spare. If the spare is a plug, the claim is already false or the definition was the plug. There is no third state discovered at 9 a.m. Drain and vent, or the signed limitation. The recorder does not write “OK.” The recorder writes “supply isolation reachable, label matches diagram, state visible, closed.” Sentences are slower. Sentences are the point.

Module removal. The builder may demonstrate once, then a person who is not the builder does it from the user note, or you learn the note is incomplete and you stop to write the missing step. Writing the missing step is allowed. Pretending you followed a note that does not contain the step is not. After reassembly, reaches again. A module that comes out only by disconnecting the hose you just proved is a module whose service claim must shrink. Shrink it now, in a limitation, before liquid. Do not shrink it after a heat run has made everyone reluctant to open the claim.

Labels, relief direction, drip path with the electrical section open and power confirmed absent. The drip test is undignified and short. A cup, the outside of the liquid section, a light. If liquid tracks into the electrical enclosure, the day ends as a design day. That is a successful outcome. It is not a ruined gate. The ruined version is to skip the cup because the enclosure looks tight, then to find the track during a leak, with power available in the neighborhood.

Fitting family against the citation, adapters on the diagram, materials row signed. If the materials row is unsigned because the coolant citation is missing, Gate 1 cannot close and Gate 3 cannot start. You may continue the dry reaches so the day is not wasted. You mark liquid lines not started. You do not “temporarily” sign the materials row to keep the schedule. A temporary signature is a signature. There is no such thing as a temporary pass.

## Fill

The author of the fill procedure is silent. The operator follows the file. Where the file is ambiguous, the operator stops and the ambiguity is written into the procedure before the step continues. This will feel slow if the builder is used to filling by feel. The slowness is the test. A procedure that only works with coaching is a procedure that will not survive the builder’s absence. You are buying that survival now, at the price of an hour.

High points vent. Air is not waved through. The flow meter, once the loop is running at a gentle condition with heat still off, is watched for a stable reading rather than a heroic one. Stability at zero heat is not a duty pass. It is a fill pass. If the reading hunts, you do not start Gate 3 later and hope. You find the air or the installation problem while heat is still off. Hunting flow with heat off is a gift. Hunting flow with heat on is an incident.

Leak look at the cited condition. Joints wiped dry first, so an old drip is not a new leak. Then the condition, then a look, then a look again after a wait the sheet names. A leak is a fail even if it is small, even if it is traditional, even if it is on a joint the builder says always weeps once. The repair happens, the disturbed reaches repeat, the leak look repeats. Attempt numbers are written. If the second attempt weeps at a different joint, you have a systematic problem, not a single bad ferrule. Stop and look at the material and the make-up method. Do not hunt joints one by one through the afternoon and call the last dry joint a pass of the series. The series failed until the method of make-up is something you can repeat.

Valve line-up recorded at the end of Gate 1, with heat still off. This is the baseline. The recorder reads it back. Someone else looks at the handles while they read. That second pair of eyes is cheap. Skipping it is how a diagram and a handle part company before the first plateau.

Gate 1 close: every line pass, fail, or not started. Fails either cleared by repeat or converted into limitations before anyone talks about power in a casual way. The sheet owner initials the close. The builder does not. If a fail remains and a limitation covers it, the claim sentence is read aloud and changed if the fail reduced it. Read it aloud. Silent claim edits are hallway edits.

## Power, still with heat inhibited if you can

Gate 2 starts with the feed. The recorder writes what is actually plugged in. If that differs from the sheet, stop and update the limitation or change the feed. Do not “note it later.” Later is how the wrong feed becomes the accepted feed.

Earth and insulation, criteria in hand, results written as results. Then the local disconnect test, before any high load, before any pride. Open the disconnect. Attempt a remote command of heat. Heat does not come on. If it comes on, the day is a design day again. Celebrate the find. Do not continue to plateaus. A unit that accepts remote heat with the local disconnect open is not a unit you load “just to see the thermals.” The thermals are not the emergency. The emergency is the command path you just proved unsafe.

Breaker-open behavior, control power sketch in hand. Then identity, points, quality. The stale-data proof is performed with a little cruelty and no apology. Disconnect a sensor or stop a read. Wait long enough that a lazy system would have painted. Collect the export. The stranger is not required for this look, but the recorder and the sheet owner are. If the file shows a smooth continuation, Gate 2 fails the exit. The builder may explain. The explanation does not pass the line. A fix, a new image, a new logger, then a repeat. If the fix is “we will ignore that channel,” the channel is removed from the point list and any duty that needed it is reduced. You do not ignore a channel and keep the duty.

Alarm by simulation. Words, not only a lamp. Latch. Local reset. Network loss while a stop is latched: heat stays off, alarm remains. Power-cycle with remote silent: the unit does not wake into heat. If it wakes into heat, that is the same class of fail as the disconnect test. Stop the day as a claim day. Continue only as a repair day.

The stranger’s idle test can happen here if the stranger is present. If the stranger comes after lunch, do not skip the test and do not substitute your own reading. Wait. Use the wait to repair anything Gate 2 already failed. Do not use the wait to start Gate 3. The order is the method. A gap in the schedule is not a hole in the order.

## Plateaus

Export confirmed running. Ready state, heat off, flow readable, no latched unexplained alarm. The first plateau is the low one, and it may be record-only if you decided pump heat would dominate the story. The operator commands it. The recorder writes the start time from the export’s clock, not from a wristwatch that was never compared. If the two clocks differ, the export clock wins and the wristwatch is retired from the record. Two clocks are how a sudden increase gets narrated in a different order than it happened.

Dwell means dwell. Nobody shortens it because the numbers “look stable early.” Early stability is a hypothesis. The dwell is the test of the hypothesis. If the sheet’s end condition is a heat story that has stopped changing, the recorder says when that condition was met and does not invent a tighter one to finish before lunch. If lunch is the real end condition, the sheet was dishonest. You are not required to be hungry. You are required not to edit the dwell to match your hunger.

At the judged plateau, the stranger’s questions are answered by the file after the dwell, not during it by the operator’s memory. Command, power, flow, both temperatures, quality, alarms. If a quality flag went bad and recovered, the plateau is suspect. Look at the gap. A gap inside the dwell fails the dwell unless the sheet explicitly allowed a defined gap, which it should not have. Fail the line. Repeat the plateau. Do not average across the gap.

The sudden increase is commanded only if the destination is a plateau you are allowed to hold. The recorder watches the order in the file: command, then power, then temperatures. If the order cannot be seen because the interval is too slow, the interval fails the evidence, and the sudden-increase line cannot pass. That is a sheet problem you should have caught in Gate 2. Catching it now still counts. Change the interval, repeat Gate 2’s relevant lines if the logger change can paint stale data, then repeat the increase. Logger changes are disturbances. They feel like “just a setting.” Settings that alter evidence are in the stop-adjacent family. Treat them with suspicion.

An alarm during a plateau stops the narration and starts a sentence: which alarm, what action, did heat come off if it should have, is the plateau invalid. If the alarm was spurious and the action was correct, the plateau still does not automatically pass. A spurious trip means you do not have a clean dwell. Repeat after the cause is fixed. If the cause is “unknown, cleared by reset,” you do not have a fix. You have a cleared lamp. The line stays failed. This is the moment teams cheat, because the lamp is quiet and the truck is loud. The recorder’s sentence is the defense. Write “reset without cause” and do not let the next line begin.

Return to zero. Confirm the zero you defined. Shut down only after the stranger has the file, or after the file is stored where the stranger can open it without your laptop. A file trapped on the operator’s machine is not yet a record. Copy it before you break the setup. Setups get broken by people tidying. Tidying is a disturbance. The copy is the defense.

## The visit above rating

Only if Gate 3’s judged lines passed. The person whose job is to look at the unit is named and is not the person watching the plot. The dwell is the sheet’s dwell. You do not extend it because it looks calm. Calm is not a new rating. The exit is performed even if everyone wants to “leave it there while we talk.” Talking while an overload continues is how a visit becomes an unaccepted continuous run. Exit first. Talk second.

Local stop practice, if not already done at a low plateau, is done before the visit, at a low plateau, with a remote command asserting. If you discover during practice that the stop only asks the controller politely, you do not proceed to the visit. The visit is not the place to learn that. Control-power kill, same logic. Fear of this test is a finding. Write it down and repair. Do not skip the test to keep morale. Morale is not a gate.

After the exit, overrides are checked cleared. The claim sentence is read again, aloud, including the clause that the visit is not a continuous rating. People will be proud. Pride is welcome. Pride does not edit the sentence. The recorder writes the visit as a visit. The word rating does not appear in the line except to say it was not established.

## Close of day

Limitations updated the same day. Export opened on another machine. Attempt history preserved. Frozen morning copy kept, so any hallway revision can be seen as a revision. Handoff exercise if the receiver is present. If the receiver is not present, the unit is not delivered, even if it passed. Passed and delivered are different. Write “accepted, not handed over” rather than letting a pass imply a handoff. The next person will assume the file is enough only if the exercise happened. Schedule the exercise. Do not let it fall off the end of the day because everyone is tired. Tired handoffs are how the unofficial plateau gets whispered at the door. Do the exercise or write not done.

The builder gets a copy of the fail list, including fails that were later repeated to a pass. That list is their best document. A thank-you with no list teaches the wrong lesson. You can be polite and still hand over the list. Politeness is not a pass.

## Where this day differs from yours

Your day may have a hot leak test the fictional day only points at. Your day may have a second branch. Your day may be unable to staff a stranger until tomorrow, in which case Gate 3’s stranger line stays not started and the unit is not fully accepted today. Partial days are allowed. Partial passes are not. A gate with a not-started line is not a passed gate. Say so in the header of the day’s record so a reader who only sees “Gate 3” in a status report does not invent a pass. Status reports are where not-started goes to become green. Deny them the green. Give them the words.

Your day may also include a commercial pressure this chapter cannot feel. The close remains the same. A failed line with a date for the repeat is a day that did its job. A passed line that was not run is a day that created work for the project book, the kind of work that shows up as a mystery at the manifold. You are allowed to disappoint a schedule. You are not allowed to lend it your initials.

## Public sources for this chapter

The frozen header on the morning of the day includes the editions, or the lines that depend on them are not started. Nobody reads a datasheet aloud as a substitute for a reach, a leak look, or a kill test. If a number from a public document is needed to judge a plateau, it was written on the project sheet before the day, from an edition the project may use. It is not looked up in the hallway and typed into the record from a phone.

## Decisions to record

- Whether your real day can staff the roles, and the limitation if it cannot.
- The frozen revision you will walk in with.
- The rule that a not-started line forbids calling the gate passed in any status report.
- The same-day list of fails, including those later repeated to pass, given to the builder.


# 15. Telling the heat story without a stolen constant

The duty chapter said electrical power and heat into the liquid are not the same quantity, and that a missing member of the set can imitate a healthy value of another. This chapter is the practice of saying that out loud, in sentences a recorder can write, without a universal formula and without a constant borrowed from a paper you are not allowed to freeze. The structure of the story is enough to run a gate. The project file may add a calculation when the interface owner has a source. The gate does not wait for a decorative equation.

## The story has a direction

Heat into the liquid moves from the elements into the stream you measured. The stream enters at the supply temperature and leaves at the return temperature, if you named those taps on the heater path and not on a bypass mix. Flow is the amount of stream. Power is the electrical claim that heat was available. A story that cannot name those four, plus quality, is not a short story. It is a different genre. It is a log of a contactor.

Direction matters because people reverse supply and return when a hose is flipped and the labels are not. A reversed pair makes heat look like a cooler. The first check at a low plateau, heat on purpose, is whether the temperature change has the sign the diagram predicts. If the sign is wrong, stop judging. Fix the names or the hose. Do not “take the absolute value” and continue. Absolute value is how a reversed installation passes and then poisons every later comparison with the rack side. The rack side will not share your absolute value. It will share the confusion.

Write the sign check as a Gate 3 line if it is not already implied by the heat story. Implied lines get skipped. A line that says “return is hotter than supply on the heater path, as the diagram defines those words” is a small line and it has caught real errors. Keep it.

## What “agrees” is allowed to mean

This book will not tell you a percentage within which power and the liquid story must match. A percentage without a measurement basis is a costume of rigor. What the gate may require is weaker and stricter: the recorder can say whether the liquid story and the power story point at the same conclusion, and can say what would change the conclusion.

Same conclusion means: heat is going into the measured stream at a level that is recognizably the plateau you commanded, not recognizably zero, and not recognizably some other plateau. If you commanded the middle and the liquid story looks like zero, they do not agree, whatever a future calculation might say about losses. If you commanded zero and the liquid story looks like the high plateau, they do not agree, and you may have a welded contactor or a mislabeled power channel. If you commanded the high plateau and the liquid story is in the right direction but you cannot tell high from middle, you do not have agreement. You have a measurement that cannot see the step. That is a fail of evidence, not a pass with a footnote.

Losses exist. Case heat, pump heat, a bypass, a transient into metal. They are reasons to widen what “recognizable” means, or to mark the plateau record-only. They are not reasons to declare agreement by adding a factor until the stories match. A factor typed after the dwell is a confession that the stories did not agree. Record the confession. Do not hide it in a cell called efficiency.

If the project later earns a real balance, with named loss terms and a comparison method, it may tighten “recognizable” into a band. The band lives on the project sheet, cited, and the gate uses it. Until that day, the word is recognizable, and the test is whether a stranger, told the plateau name, can see that name in the liquid story without being told a correction. If they need the correction, the correction is part of the claim and must be written before the dwell, not invented for the stranger’s comfort.

## Five stories that look like success

Power high, rise high, flow unread. This looks like a strong test. It is a heater in a box that might be full of liquid. Without flow you cannot tell a healthy high rise from a low-flow event that is about to trip, and you cannot tell the CDU anything about demand. The story is incomplete. The gate fails the flow line. The pretty temperatures do not outvote it.

Power high, rise small, flow high, quality good, sensors in the stream. This can be the high-flow regime doing what it does. It can also be a bypass mixing cold liquid into the return tap. The diagram decides which story you are allowed to tell. If the return tap is downstream of a mix, you are not measuring heater rise. You are measuring a mixture. Say the mixture story or move the tap. Do not call a mixture a heater rise because the number is convenient.

Power high, rise small, flow unread, display smiling. This is the dangerous cousin of the high-flow story. People who have heard that small rise means high flow will pass it. The close is the one in the arguments chapter: rise alone is not a flow measurement. Fail the line until flow is in the file.

Power low, rise high, flow low. Recognizable as a low-flow condition. If the command was high power, the stories disagree and the plateau fails. If the command was low power and flow was supposed to be high, they also disagree. The useful part is the disagreement. It points at a kink, a valve, a pump, or a meter, and it does so without a formula. Follow the disagreement. Do not average it with the next plateau.

Power high, rise high, flow high, differential pressure unread. The thermal story may be recognizable and the hydraulic stand-in still false. A gate that passes heat and ignores the pressure cell has accepted a different product than the one in the claim. If the claim includes “represents the rack-side resistance,” unread pressure fails it. If the claim was reduced to heat only, the file must say the resistance is not represented. Do not let a good thermal story silently restore the hydraulic claim.

## Four-quadrant time-series diagnostics

Beyond static averages, thermal and hydraulic evidence lives in the dynamic shape of time-series waveforms. (See Figure 05 for the four diagnostic signature quadrants).

When inspecting the exported test log, look for these four distinct archetypes:
1. **Quadrant A (Valid Plateau & Dwell)**: Commanded electrical power steps up sharply (e.g. 30kW -> 60kW -> 120kW). Flow remains stable. Return temperature rises with a smooth, physical exponential thermal lag (τ ≈ 45 s), eventually flattening into a horizontal plateau that holds for the entire 15-minute dwell. The closed thermodynamic heat balance (Q_thermal = ṁ C_p ΔT) matches commanded electrical power within ± 3%.
2. **Quadrant B (Stale Data Communication Fraud)**: The power step is commanded, but temperature and flow traces are rendered as mathematically perfect, flat lines with zero sensor variance (σ² = 0.000). In real physical loops, turbulent convection always produces minor micro-noise. A flat line indicates the telemetry buffer froze or firmware repeated cached readings with fabricated timestamps. This is an immediate Gate 2 and Gate 3 fail.
3. **Quadrant C (Internal Bypass Short-Circuit)**: 120 kW electrical power is confirmed, but the return temperature barely budges (ΔT rises by only 1.2 K instead of the expected 10.0 K). The inferred thermal heat into the liquid is only 14 kW, leaving 106 kW missing! This signature reveals that an internal bypass valve or baffle seal is blown: 85% of cold liquid is short-circuiting around the heating vessel.
4. **Quadrant D (Water Hammer & Valve Bounce Transient)**: A motorized modulating valve or solenoid closes too fast (< 1 second) without a deceleration ramp. Pressure spikes violently to 3.5× nominal operating head, inducing acoustic banging, cavitation slugs in the flow meter, and mechanical fatigue in hose ferrules. Modulating valves must be programmed with minimum 3-second stroke ramps.

## Transients are not plateaus

At the start of a step, metal and liquid that were cold take heat that has not yet appeared as a steady rise. The power is real. The rise is late. A judgment made in that window will say the heater is weak. The dwell exists so you do not judge in that window. If your dwell is shorter than the transient, you wrote a bad dwell. Lengthen it before the day, or mark the plateau record-only. Do not lengthen it on the day to chase a number, and do not shorten it to avoid the transient’s lesson. The lesson is that the unit has mass. If mass is not in the claim, the dwell has to be long enough to get past it. If mass is in the claim, you still need a steady region in which to see it. Either way the transient is not the place you initial.

The sudden increase is a transient on purpose. You judge it by order and by arrival at the destination plateau, not by a heat balance taken at the midpoint of the jump. Mid-jump balances are how people prove contradictions. Leave them to the data book. The acceptance question is only: did the command arrive as a step, and did the destination plateau then become recognizable. Two questions. Do not add a third because the plot is interesting.

## Quality flags inside the story

A story that uses a stale flow is a story about a painting. Before the recorder writes “recognizable,” the recorder looks at quality across the dwell. One bad sample may be a defined nuisance if the sheet allows it, which it should not, or a fail. A run of bad samples is a fail. A flag that never changes, on a system you have not tested with the stale-data proof, is not a comfort. It may mean the flag is decorative. Gate 2’s proof is what makes the flag meaningful here. If Gate 2 was skipped, you cannot use the flag as evidence, and you also cannot use the absence of flags as evidence that everything was live. Skipped Gate 2 collapses Gate 3’s heat story into a contactor log with extra columns. Say that when someone wants to “just run heat” because the thermocouples look alive. Alive on a screen is not quality in a file.

## Comparison points in the story

The unit story and the rack-side story are allowed to differ by the hose, the adapter, and the sensor bias you wrote down before the dwell. They are not allowed to differ by a surprise bypass. If the comparison rise and the unit rise lead to different plateau names, you do not pick the one that matches the command. You stop and explain the path between the taps. The explanation becomes a diagram correction or a fail. It does not become a preference for the friendlier sensor. Friendlier sensors are how claims migrate to the tap that behaves. The tap that behaves may not be the boundary you said you represented.

Write one sentence in the record: which tap is the stand-in tap for the claim. The other taps are witnesses. Witnesses can fail the claim if they contradict it. They cannot replace it because they are closer to the command. Closer to the command is exactly what a biased test looks like.

## What the recorder writes

A template, with no numbers in it. “Plateau name: as on the sheet. Command recorded. Measured power present or absent. Flow present or absent, quality good or not across the dwell. Supply and return named as on the diagram, sign of the difference correct or not. Story recognizable as this plateau, or not, or record-only as predeclared. Comparison tap agrees on the plateau name, or contradicts, or not fitted. Alarms: none, or explained. Stale samples: none inside the dwell. Authority: line-up unchanged, or disturbance noted and plateau invalid.”

That template is long. It is also one paragraph once the team has said it twice. Practice it on the dummy export the day before, the one with heat off, so the first time the recorder says it is not the first judged plateau. A first recital during a dwell becomes “OK” under pressure. Recite on the dummy. The dummy should produce “record-only, heat off, sign not applicable, quality good.” If the recorder cannot say that about a dummy, they will not say the real paragraph about a live plateau.

## What the stranger writes

The stranger does not use your template’s conclusions. The stranger gets the file and the diagram and writes their own sentence. You compare. If the sentences name the same plateau and the same holes, the exit passed. If the stranger names a different plateau, believe the stranger until you can show a naming bug in the file. If the stranger says the file cannot support a sentence, believe that even if you can support one from memory. Memory is not in the file. The fix is the file. This is the same stranger test as before, said here so the heat story does not become a private dialect the recorder shares with the operator. The stranger is the proof the dialect is public.

## When you are not allowed to tell the story

You are not allowed to tell it if flow or either temperature is missing on the heater path. You may say power was present. You may not say the loop was loaded. You are not allowed to tell it if quality is unproven because Gate 2’s stale-data line did not pass. You are not allowed to tell it during the transient and call that the plateau. You are not allowed to tell it on an uninstrumented spare path. You are not allowed to tell it at an unofficial command and then slide the official name over it. You are not allowed to tell it with a factor born after the dwell.

Those prohibitions are the kill list applied to prose. They will feel pedantic the first time the plot looks obvious. Obvious plots are the ones that launder a missing flow. Hold the prohibition. The data book can be clever later, on files that earned cleverness by being complete. Acceptance is not the place to be clever. It is the place to be unwilling to say more than the columns support.

## A bench note on pump heat, again, in story form

At a low command, the liquid story may be recognizable as heat even when the heaters are off, because the pump is the source. If you did not predeclare that plateau record-only, you will pass a heater that is not on, or you will fail a heater that is honestly small next to the pump. Predeclaration is the whole trick. Write, before the day, which plateaus are above pump heat in the story sense and which are not. If you do not know, the first heat-off run with flow on is not a waste. It is the measurement of the floor. Record the floor. Judge only above it. A floor discovered during a judged plateau invalidates that plateau and improves the next one. Mark the invalidation. Do not quietly reclassify after you have seen the answer and liked it. Reclassification after the answer is the band-edit failure in a new costume.

## Differential pressure as a story, not a number

You can tell a hydraulic story without publishing a resistance curve. At a held flow, the difference between the two pressure taps is either present and stable, or it is not. Present and stable supports “the path is the path we lined up.” Climbing during a dwell at constant command supports “something is blocking, heating, or the valve is moving.” Falling supports “something opened, or a pump changed, or a tap is leaking to atmosphere.” Unreadable supports nothing. The recorder’s hydraulic sentence is: stable, climbing, falling, or unreadable, at the lined-up flow. That sentence is enough to fail a kink that the thermal story has not yet registered, because pressure often moves before temperature becomes scary. Use it. A team that waits for temperature to confirm a hydraulic problem is a team that uses the overtemperature stop as a flow meter. That works, in the sense that it eventually trips. It is a bad instrument.

If the sheet has a cited band for the difference, you may also say inside or outside. If it does not, do not invent the band from today’s reading. Today’s reading can be the baseline for a later comparison. A baseline is not a retroactive specification. Label it baseline. The next unit does not inherit it as a limit unless you promote it through the revision rule with a reason that is more than “the first unit happened to do this.”

## Putting the story in the file

The delivery file’s user note includes the template paragraph and the prohibitions, in short form. An operator who was not at acceptance should be able to refuse a bad story without calling you. If the note only says “log the data,” they will log the data and tell the story anyway, in email, with a factor. The prohibitions belong in the note. They are use limits, like the limitations page. A heat story told against a prohibition is an incident of the documentation kind. Treat a published bad story as an incident if it leaves the project. Quiet bad stories in a notebook are coaching opportunities. Bad stories in a status report are how a reduced claim gets reversed in public. Correct them the same day, in the same channel, with the prohibition quoted. Speed matters more than tone. A late correction reads as a dispute. A same-day correction reads as the method.

## Public sources for this chapter

A heat story does not borrow a formula from a handbook to look finished. If the project has a licensed method for a balance, the method is cited on the project sheet and used there. This chapter’s words, recognizable and record-only, are the acceptance language. They do not become a fake ASHRAE calculation by adding a constant you saw once. NVIDIA’s public performance claims are not a heat story about your unit. They are claims about their rack, on their page, under their conditions.

## Decisions to record

- The sign-check line on Gate 3.
- Which plateaus are predeclared record-only because of pump heat or sensor noise.
- The recorder’s paragraph, practiced on a dummy export.
- The prohibitions copied into the user note, not left in this chapter alone.
- A rule that a baseline from unit one is not a limit for unit two unless revised on purpose.


# 16. A review you can run on someone else’s draft

You will be handed a design note, a quote, or a draft acceptance sheet and asked whether it is enough to build or to buy. This chapter is the pass you run before you answer. It is deliberately repetitive of the earlier chapters. Repetition here is the point. A review that trusts the author’s structure will miss the missing stop. A review that walks the same cells every time will not. Use it on your own sheet as well, a day after you wrote it, when the sentences have gone cold.

## First page

Find the claim sentence. If it is absent, stop the review and ask for it. Do not reconstruct it from the marketing paragraph. A reconstructed claim will be kinder than the sheet deserves. If the claim says the unit replaces a CDU, or accepts a hall, or proves IT gear, the claim is the wrong product. Say so in the first comment. Everything else is secondary until the claim shrinks to a rack-side thermal and hydraulic stand-in, or to something smaller that is honestly named.

Find the citation line. Title and revision, or a dated unknown. A draft that has values and no citation is not more complete than a draft that has blanks. It is less safe. Comment: source each value or remove it. Do not suggest a “typical” replacement. Typical is how you would become the author of a number you do not own.

Find the limitations block. If it is missing, the draft has not started. If it contains only commercial complaints, it is missing. Seed comments: unattended heat, overload-as-rating, comparison points, spare definition, image in the stop path. Ask which of those the design actually satisfies. The answers become limitations or gates. They do not become assurances in the reply mail.

## Six functions, hunting omissions

Search the draft for flow adjustment. If you find a valve mentioned only in a parts list, the function is not specified. Ask the authority sentence. If the sentence is missing, the draft is a parts pile. Do not help them by writing the sentence yourself in the margin and calling the review done. Make them write it. A sentence you wrote for them will not be the sentence they build.

Search for both temperatures and for the words that locate them. “Temperature sensor” without a stream name fails the review. Ask which sensor may remove heat, and what a failed sensor does. If the draft says the controller will decide, ask the kill test. Controllers do not answer kill tests. Circuits do.

Search for flow readable as distinct from flow adjustable. Drafts often specify a modulating valve and forget the meter, or specify a meter on the wrong path. Ask which path is the stand-in path. If there are branches, ask whether each commanded branch has a meter. A header meter with independent branch heat is a comment, not a quibble. It is a false story waiting for a date.

Search for pressure. Drafts love a single gauge. Ask for the two sides of the difference, or for an explicit reduction of the hydraulic claim. Do not let a gauge icon on a rendering close the cell.

Search for plateaus by name. If you find only a percentage range, the steps are unspecified. Ask for measured power in the export. Ask for the sudden increase as distinct from staging. If they say staging is the increase, ask them to call it a ramp and to stop using the other word. Vocabulary is a gate. Wrong vocabulary will be copied into the script.

Search for the alarm text. If the only word is fault, the protection row fails the review even if a contactor exists. Ask for the local indication with the network dead. Ask for the latch. These questions feel like software questions. They are stop questions. Keep asking them until the answer is a behavior, not a product name.

## Liquid path, hunting souvenirs

Look for a part number that is not tied to a citation. Comment: souvenir, remove or cite. Look for a spare that is not drawn through the heat section. Comment: plug, not spare, or draw it. Look for hose described as “field routed.” Comment: routing prohibitions and a pressurized look in the position of use, or accept that Gate 1 cannot pass at the factory. Look for a sensor boss described as “near” the outlet. Near is a stub until proven otherwise. Ask for the diagram.

Look for primary and secondary used without a glossary line. Ask which side the unit occupies. If the draft shows the unit between a chiller and a rack in a way that makes it the CDU, the claim has drifted. Point at the first page. Do not redraw their system for them. Make them delete the parts that are not in scope. Scope deletion is the reviewer’s kindness. Leaving the extra parts in is how they get built and then blamed on you.

## Heat path, hunting coupling

Find the authority sentence. If one valve sets heat and flow, look for a written coupling limitation. If it is absent, the draft claims independent control it does not have. Comment the limitation in the “does not, therefore you must not” form so they can paste it if they agree. If they do not agree, they owe a bypass or a second authority. Do not design the bypass in the review comment beyond the job it does. You are not their fabricator. You are the examiner.

Find module service. If the draft says modular and does not say whether the loop drains, comment the omission. A sealed module is allowed. An implied serviceable module that is actually sealed is a claim defect. Ask which one they mean. Make them pick before metal. After metal, picking is expensive, and people pick the story that matches the object rather than the need.

Find the safe-state tests. If they are absent, add them as gate lines in your comment, not as a suggestion. Command zero. Kill control power. Local disconnect versus remote command. A draft that cannot host those lines is not ready for a purchase that includes acceptance. It may be ready for a study. Label it a study so nobody schedules a truck.

## Data exit, hunting paint

Search for the words last value, hold, timeout, and quality. If none of them appear, ask the stale-data question directly. If the answer is a brand name, ask again. Brands are not behaviors. Search for the export format. If the only exit is a screen, the stranger test cannot be passed. Comment that. Search for default addresses and register tables copied from another job. Tell them to take those out of the design basis and put them in an appendix that does not lead. Maps that lead the document will be what gets built, and the functions will follow the map even when the map is the wrong dialect.

Search for alarm actions. A table of codes without actions is a decoder ring, not a protection design. Ask what each code does to heat. If they do not know, the code is not ready to ship inside the unit. It can remain a private debug list. Label it debug so it is not mistaken for the point list.

## Safety, hunting dependence

For each of the five stops, ask the five fillers: cause, action, local indication, record, failed-sensor behavior. A draft that answers three is not “mostly safe.” The two missing fillers are where the incident will live. Overpressure dependence on a CDU is a limitation or a device. Leak detection that is only a software point is a report. Electrical tests that are “to code” without being lines on the sheet will not be in the record. Wrong-valve interlocks that are procedures need to be on the run sheet and the acceptance sheet both. Comment the one that is missing. Do not accept “we have a culture of safety” as a filler. Culture is not a failed-sensor behavior.

## Acceptance sheet, hunting narrative

If the acceptance document is a paragraph, it is not a sheet. Ask for boxes. If the boxes exist, check that Gate 3 cannot be initialed while Gate 1 has a fail. Check that not-started is a real status. Check that the overload dwell is present before the day, in the draft, not as “to be agreed.” Agreed on the day means edited on the day. Check the stranger. If no stranger is named, the independence of the record is already limited. That limitation is acceptable only if written. It is not acceptable as an oversight you repair by being thorough yourself. Thorough authors are how independent checks get skipped.

Look at the waiver line. If anyone on the day may waive, the sheet will move. Comment a tighter rule. If the commercial owner must waive, say so, and say the claim reduces in the same edit. A waiver path that keeps the claim is a hole. Point at the hole. Do not be embarrassed to call it a hole. The word is accurate, and softer words will be used to keep the hole.

## File list, hunting souvenirs of a different kind

Ask which of the delivery items exist: claim, requirements, duty, diagram, point list, acceptance record, limitations, user note, export archive. A draft package that has a rendering and a quote has two items, neither of which is on the list. Say the list. Do not grade the rendering. Grading the rendering teaches the author that the rendering is the deliverable. Silence on the rendering, and comments on the list, teach the opposite.

If the package includes site names, addresses, or another project’s point list, tell them to remove those before the file circulates. That comment is not pedantry. It is the difference between a unit file and a leak. You can make it without repeating the confidential content in your comment. “Remove site identifiers” is enough. Do not quote the identifiers back to prove you saw them.

## How to write the review so it can be used

Number comments. Tie each to a cell or a missing cell. Do not write an essay that must be interpreted. “Flow row: no stand-in path named. Authority sentence missing. Cannot pass a review until both exist.” That is a comment. “Consider clarifying the flow philosophy in light of best practice” is not a comment. It is a way to avoid a fail. Reviews that avoid fails produce drafts that avoid gates. Be plain. Be specific. Be willing to say the draft is a study, not a build package.

Separate blocking comments from notes. A blocking comment is one that, if ignored, makes the claim false or the gate unrunnable. Notes are everything else. Authors will try to clear notes and declare the review closed. The rule is: blocking comments closed, or the claim reduced, or the review is not closed. Put that rule in the header of your review so it cannot be managed away in a tracker that counts comments as equal.

Do not insert stolen numbers as examples of what their blanks should contain. If you have the citation on your own desk, you may point at the title and revision. You may not copy the values into the review mail and create a second, unofficial duty. Mails get forwarded. Forwarded values become the standard you spent this book refusing to invent. Point. Do not paste.

## After the review

The author revises the sheet or accepts a reduced claim. You re-read the blocking comments only. Do not re-read the whole draft as if it were new, or you will move the goalposts with fresh taste. New blocking comments are allowed if the revision created a new hole. They are not allowed because you thought of a better sentence. Better sentences can wait for the next revision. Goalposts that move every review teach the author that the cells are not real. The cells are real. Your taste is not.

When the blocking comments are closed, say so in one line. Do not add a blessing of the design. You did not bless a design. You found no remaining blocker against the claim as now written. That sentence is narrower, and it is the only one you should sign. A blessing will be quoted as acceptance. You have not accepted a unit. You have accepted a sheet’s readiness to be used on a unit. The gates still have to happen to metal.

## Using this chapter on the day

The same pass works on the morning of acceptance, with the object instead of the draft. Claim still matches the metal. Citations still the ones in the header. Limitations still true of the hoses you can see. Six functions still have somewhere to live in the record. If the morning pass fails, the day is a repair day. Starting Gate 3 anyway is the review failure this chapter is for. The object does not outrank the sheet because it is heavy. Weight is not evidence. The sheet is the evidence of what you intended. The gates are the evidence of what you have. Both have to exist. Neither substitutes for the other.

## Public sources for this chapter

A blocking comment includes any pasted table, figure, or paragraph from ASHRAE, from an NVIDIA datasheet, or from a code. The remedy is a citation in the form chapter 19 requires, and deletion of the paste. Do not replace the paste with your own paraphrase of the same page. A paraphrase of a licensed table is how a review creates the derivative the policy forbids. Point. Do not retype.

## Decisions to record

- Blocking comments separated from notes, with a close rule that notes do not outvote blockers.
- A refusal to paste values into review mail.
- A one-line close that does not bless the design.
- The morning-of-acceptance pass, run before Gate 3, even if the sheet was reviewed last month.


# 17. Before metal, and when to stop

There is a period, after the sheet exists and before anyone orders a heater, when the project can still stop cheaply. This chapter is about that period. Teams waste it on renderings because renderings feel like progress and a blank citation feels like delay. The blank citation is the progress. The rendering is the delay, dressed up as a picture of a box you have not yet earned.

## The minimum package that justifies an order

You may order metal when the claim sentence is stable, the six functions have do-not-ship cells, the duty set is either cited or explicitly record-only with no fake values, the authority sentence is written, the stop path is sketched far enough to run the kill tests, and the acceptance lines exist as boxes. You may not order metal because a vendor has a slot on a production line and the slot feels scarce. Scarcity is a commercial fact. It does not fill a cell. If the slot will disappear, the honest choices are to miss the slot or to order only what the completed cells justify, with the rest as a later release. A partial order is a legitimate tool. A full order against a partial sheet is how the missing cells get designed by the factory, in their favor, while you are still looking for the interface revision.

Write the order so it points at the sheet revision, not at a conversation. “Per our discussion” is not a technical reference. The exception list is attached. Factory tests, if you are paying for them, are mapped to gate lines in the order, so a certificate cannot be substituted later. Delivery includes the file items, not only the crate. A crate that arrives without the point list and the user note is a partial delivery. Say that in the order, or you will be told the documents are a courtesy. They are not a courtesy. They are how the unit remains the accepted object. Courtesy documents arrive late and wrong. Contractual documents arrive with the revision you named.

## What you can build while a citation is open

You can build and accept the stop path, the export behavior, the module service, and the fill procedure. Those do not need the rack’s flow window. You cannot accept the duty claim, the fitting family, or the hose material. Mark the open items not started. A shop that is idle can still run Gate 2 on a bench feed you have described. A shop that is idle should not invent a fitting “so there is something to test.” Something to test is not a reason to freeze a souvenir into hardware. Caps and a clearly temporary adapter, labeled not the interface, are allowed if the label is physical, not a note in a drawer. A temporary adapter that looks like a finished port will be used as a finished port. Paint the temporary status on it. Ugly is useful.

If the open citation is the coolant, you do not fill the unit with a convenient fluid and call the materials row done. You may pressure-test with a fluid the builder declares, and you limit that test to “held pressure with this fluid,” not “compatible with the service coolant.” The limitation is written before the test, so the test report cannot grow a compatibility sentence in its conclusions. Reports grow such sentences when the header was vague. Make the header narrow.

## Stopping

Stopping is a result. A sheet whose interface citation will not exist before the hall test does not justify a load bank that claims to represent that interface. Buy a heater if you need heat. Do not buy a claim. A stop path that cannot be made independent of a reboot does not justify unattended plateaus. Run attended, or do not run. A bench that cannot reach the cited flow does not justify a pass at that flow. Reduce the claim or change the bench. These are the kills, applied to schedule. The schedule will call them delays. The file should call them stops. Use the shorter word in status reports so the longer story cannot be rounded up into “on track.”

A stop should name the cell, the person who owns the missing input, and the date you will look again. An open-ended stop is a sulk. A stop with a date is a plan. If the date passes and the input is still missing, the stop converts into a dropped claim, not into a waiver that pretends the input arrived. Waivers are for cells you have decided to live without. They are not for cells you hope will appear. Hope is not a revision.

## What “enough book” means

You do not need another chapter to start. You need the two sheets. If you are still reading in order and you have not opened a blank file for the requirements list, stop reading and open it. The later chapters will still be here. They are useless to a reader who has no sheet for them to press against. A team that finishes the book and starts a rendering has used the book as a delay. A team that finishes chapter 1 with a drafted row for each function has used it as a tool. Be the second team, even if the rows are ugly. Ugly rows can be reviewed. Empty taste cannot.

When you do start, keep the claim sentence where the status report can see it. Status reports like percentages. Give them a percentage of gate lines passed if you must, and give them the claim in the same line, so a high percentage cannot be quoted without the limitation that rides with it. A percentage without a claim is the weighted scorecard in a new suit. You already decided the scorecard does not outvote a failed cell. Do not let a dashboard do it instead.

The work is the sheet, the metal, the gates, and the file, kept the same object for as long as you use the unit. This book ends where that work starts. If the work produces a kill, write the kill and stop the claim. That sentence is the last method in the book, and the one most often skipped, because it does not look like progress. It is progress. A false claim removed is a finished piece of engineering. A false claim illustrated is not.

## Public sources for this chapter

You may order metal for the stop path and the export while a citation is open. You may not order a fitting family or a hose material against a white paper you have not read in a licensed copy, and you may not fill those cells with numbers a tool extracted from one. An open NVIDIA datasheet revision blocks the interface claim. An open code edition blocks the electrical claim. An open ASHRAE liquid-cooling title blocks any cell that pretends to have settled water quality or loop names. The rest of the unit can still be built as a study. Call it a study.


# 18. Read this twice

Some sentences in this book are easy to agree with and easy to skip when the day gets loud. They are collected here so you can read them again with the sheet open. If a sentence does not match a line on your sheet, add the line or drop the sentence from your project. Do not keep it as a belief.

The load bank stands in for rack-side heat and rack-side hydraulics. It does not stand in for the CDU, the hall, or the IT equipment. If a status line claims more, the status line is wrong, not the limit.

Six functions, or a written reduction: flow adjustable, both temperatures readable, flow readable, pressure readable, heat in steps, overtemperature that stops and alarms. A brochure that meets five has not met the sheet. Say which one is missing.

Duty is a set. Power without flow, flow without temperature, temperature without the sign of the difference, pressure without a named high side and low side: each of those is a false story with a familiar face. Pass the set or reduce the claim. Do not pass the familiar face.

High rack-side flow is the reason this unit is not a gentle heater. The book does not give you the flow. The citation does. A blank citation is not permission to write a plausible one.

Isolation has a visible state. A spare is plumbed to the same duty or it is not a spare. A hose is proven in the routing you will use, at pressure, not coiled on a bench. A fitting family comes from the specification then in force, not from the last project and not from this book.

Heat plateaus are measured power held for a dwell. Percent is a request. A sudden increase that is secretly a stagger is a ramp. Call it a ramp. Modules come out as the sheet says, or the sheet changes. Loss of control removes heat. Prove that by killing control power, not by reading a schematic.

The export marks stale data. A repeated last value with a fresh timestamp is a failed exit, even if the number is plausible. The stranger test is the proof. Coaching the stranger fails the proof.

Local stop overrides a stuck remote command. A stop that asks the network for permission is not a stop. Overtemperature, overpressure, leak, electrical fault, and the wrong valve each have a failed-sensor behavior. “The CDU will catch it” is a limitation, not a device.

Four gates, in order. A heat run does not repair a kink. A factory certificate does not repair a missing line. Not started is not a pass. A band edited in the hallway is a failed revision rule. An overload visit is not a new rating.

The file and the metal are the same object. A hose swap, an image change, a coolant change, and a new interface revision are disturbances. Repeat the lines they touch. An unofficial plateau is an unaccepted duty. Write incidents the same day.

No site name, no part number, no address, and no unpublished setpoint belongs in a public chapter or in a review mail that will be forwarded. Cite the document. Do not launder it.

If you need a stolen number to make the page look finished, the page is the defect. A blank you can explain is a finished professional object. A filled blank you cannot source is not.

When a kill appears, stop the claim. Stopping is the method. Progress that preserves a false claim is not progress. It is a rendering of progress, and this book has already declined to be that rendering.

Read the claim sentence on your sheet. If you cannot, you are not done with chapter 1, whatever chapter you think you are in. Go back and write it. Then come here again. The sentences will still be true, and they will finally have somewhere to land.

## A last pass over the sheet

Open the requirements list beside this page. For each sentence above, put a mark in the margin: on the sheet, reduced on purpose, or missing. Missing is the only mark that needs work tonight. Reduced on purpose is already a limitation, if you wrote the “therefore you must not.” If you reduced it only in your head, it is missing.

Count the Gate 3 lines that can be initialed while a Gate 1 fail is still open. The count should be zero. If it is not, the sheet allows the truck to outrank the hose. Fix the sheet before you fix the prose of the claim. A strong claim on a leaky procedure is how the claim gets attached to the wrong object.

Find every number on the sheet. Each one is either cited, labeled as your choice, or fictitious and therefore forbidden. Fictitious numbers enter when someone copies an example. This book tried not to give you one. If a number has no source, delete it today, not after the first review copies it into a second document. Second documents are where folklore becomes a requirement. You will not remember which copy was the joke.

Find every proper noun that is a place, a customer, or a product you do not have the right to publish. Remove them from any file that will leave the project system. The method does not need them. If a sentence collapses without them, the sentence was a souvenir. Replace it with the job the souvenir was doing: isolation, spare, step, stop, export.

Then close the book. The next useful hour is a blank acceptance line filled with a box, not another page of guidance. Guidance past this point is a way to avoid the box. You have enough guidance. The box is the work.

If you are the person who asked for a longer draft, use the length this way. Do not read it as a novel. Read chapter 1 and write the six rows. Read chapter 7 and turn each gate into boxes. Read chapter 9 before you paste anything from a project file into a public place. The middle chapters are what you open when a row is weak. A weak row is a row you cannot fail. Strengthen the fail, not the adjective.

Leave the later books alone until a stranger can reconstruct one plateau from your export. That is the hinge between this volume and the next. Without it, a data book would be a book about screenshots. With it, the next book has something to read. Do not start that book in the margin of this one. The margin is for the claim, the citation, and the limitation you are still avoiding. Write those three. Then stop.

One practical test before you put this draft down. Pick the page you like best. Delete every sentence that could not change a line on the sheet. If the page survives, it is doing work. If the page collapses, it was tone. Keep the pages that survive. The sheet is the only summary that matters, and it is not in this file until you write it.

If you only mark three lines tonight, mark these. The claim sentence does not mention a CDU, a hall, or a GPU. The duty cells are blank or cited, never remembered. Gate 3 cannot start while a hose, a spare, or a stop path is still a fail. Those three marks are the book in miniature. Everything else is how you keep them from being talked away.

When you come back to this draft, do not ask whether it sounds like a book. Ask whether a builder could fail a line with it. If the answer is no, the draft is still a speech. If the answer is yes, take that line onto your sheet and try it on the object you actually have, even if the object is only a sketch. A sketch that can fail is further along than a prototype that can only be admired. Admiration is the failure mode this chapter is here to interrupt. Fail something small, in writing, before you praise something large. That is the whole practice, repeated until it is boring. Boring is what you want. The interesting days are the ones where a stop did not work. Arrange the sheet so those days are visible, and the quiet days are dull on purpose. If you do nothing else with this draft, make one fail visible. A hidden fail is the same as a false pass, and a false pass is the only outcome this book is written to prevent. Put the fail on the sheet tonight, with the revision still frozen, so tomorrow cannot talk it into a note. A note is where fails go to become folklore. The sheet is where they stay fails until the metal or the claim changes in daylight. That is enough. Close the file. The next edit belongs on your sheet, not in this chapter. If the sheet is still empty, this draft has not been used yet, however long it is. Use it, or do not keep reading.

## Public sources for this chapter

Read this with the bibliography open. Every famous name on the sheet has an edition, or it is not yet a citation. NVIDIA’s public page may support “liquid-cooled rack.” It may not support a number. ASHRAE may be named. ASHRAE may not be pasted, digested, or rewritten by a tool. The wiring code and the equipment standard are two editions. A sheet that says “per code” has not finished Gate 2. A sheet that says “per ASHRAE” has not finished the materials row. Those two failures are enough to send you back, which is what this chapter is for.


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
