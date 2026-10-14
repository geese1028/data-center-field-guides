---
title: A model cannot learn a fan speed it never saw
description: If the towers only ran one way, a fit has no evidence for the speeds a search will propose.
book: When a Monitor May Speak
slug: model-cannot-learn-a-speed-it-never-saw
---

# A model cannot learn a fan speed it never saw

![Unseen speeds are a guess.](figures/tower-model.png)

*Original diagram. Not a site record. Not a control schematic.*


A fit learns the plant it was shown. If the towers spent the archive at one fan speed, and two towers always on, the archive does not contain the other speeds. A search that then proposes those speeds is guessing. Label the guess. Do not call it an optimum.

Ask, before the fit, whether the handles actually moved. On and off. More than one speed. More than one tower count. A historian that is flat on the handle is not a training set for that handle. You may still fit the conditions you do have, and say what the plant did. You may not search a space the points never visited and treat the bottom of the curve as a recommendation.

Partial data is allowed if the sheet says partial. "We have some speeds, not all" is a limit. Hidden partial is the same defect as a score that drops a stale input and stays confident. Show which speeds were present. A proposal outside that set does not page, and it does not go to the BMS as a setpoint.

Do not fill the missing speeds with a simulator you have not checked against a walked or metered hour. A simulator that agrees with the one speed you ran has not been checked. Agreement on the only point you have is not a validation.

If you need the missing speeds, that is a test, with a method approved before the tools, a back-out, and a live power point. It is not a notebook loop. The model waits until that test exists. It does not invent the hour.

From *When a Monitor May Speak*, Tristan, Data Center Field Guides. No store link until the Kindle edition is listed.

Related: [A failed poll is a gap](02-a-failed-poll-is-a-gap.md).
