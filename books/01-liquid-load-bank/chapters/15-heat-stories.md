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
