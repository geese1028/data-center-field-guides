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
