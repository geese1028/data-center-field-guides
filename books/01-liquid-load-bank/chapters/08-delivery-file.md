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
