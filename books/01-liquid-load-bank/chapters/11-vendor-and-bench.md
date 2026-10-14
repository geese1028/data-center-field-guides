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
