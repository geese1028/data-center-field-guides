---
title: A baseline is not a fault
description: A detector that draws a band around history has not found an incident. The band width is a choice. Do not erase the points first.
book: When a Monitor May Speak
slug: a-baseline-is-not-a-fault
---

# A baseline is not a fault

![A band around history is not a fault.](figures/stale.png)

*Original diagram. Not a site record.*


Big-data detection, in the work this series will actually defend, is a band around recent history. The band moves as the history moves. A point outside the band is a candidate alert. It is not an incident, and it is not a root cause. The screen still needs a clock, a quality mark, and a person who may promote the alert. A cleverer band does not skip that.

Two choices are made before the night, and they are not physics. How wide the band is. Whether last week's spikes are replaced before the band is drawn. A wider band pages less. A narrower band pages more. Neither width is a severity. Replacing spikes before you draw the band teaches the band that the spikes were normal, or erases the only evidence you had. If you replace, write that you replaced, and do not call the cleaned series the raw plant. Raw stays recoverable. Clean lives in another column.

Season and hour belong in the band only if you can say so in one sentence a stranger can check. "It knows weekly seasonality" is a vendor sentence. Your sentence is: which clock, how much history, what happens when the history is shorter than the method requires. If the method needs two days and you have one, you do not have a baseline. You have a gap. Do not invent the second day.

A detector that retunes itself when the plant is in a maintenance window will learn the window as normal. Mark the window first, the way the monitor book already requires. Points inside the window may be stored. They do not train the band you will trust on Monday, unless you meant them to.

No accuracy rate. No product name. No parameter table from a manual. If your site uses a named detector, the weights and the switches stay in the site file. This note only refuses the pen.

From *When a Monitor May Speak*, Tristan, Data Center Field Guides. No store link until the Kindle edition is listed.

Related: [A green tile can be stale](06-stale-is-not-green.md).
