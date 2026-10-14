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
