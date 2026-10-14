---
title: Do not train a tower model on a stopped plant
description: Hours when tower or pump power is zero are shutdown, not an efficient setpoint. Take them out before the fit.
book: When a Monitor May Speak
slug: do-not-train-on-a-stopped-plant
---

# Do not train a tower model on a stopped plant

![Shutdown hours are not an efficient setpoint.](figures/tower-checks.png)

*Original diagram. Not a site record.*


A historian will contain hours when the condenser plant is off. Pump power is zero. Tower power is zero. Leaving water sits wherever the pipes left it. If those hours stay in the fit, the model learns that the cheapest way to run is not to run. That is true and useless. It is not an operating point.

Mark shutdown before you fit. The mark is a rule you can read: total pump power at zero, or total tower power at zero, or a plant-off state you already write on the day sheet. Do not invent the mark after the curve looks strange. Do not delete the hours from the archive. Delete them from the training set, and keep the count. A fit that cannot say how many hours it refused has hidden its sample.

A short stop inside a longer run is the same defect, smaller. A fan that coasts for ten minutes is not a speed you may recommend. If the interval is shorter than the poll you trust, it is a gap, not a sample. Chapter of the file book already said a failed poll is a gap. A zero that means "off" is a different gap. Label which zero you mean. Off is not a measurement of a running tower.

After the cut, look at what remains. If the remaining hours are one season, one tower count, and one fan speed, you still do not have a search space. You have a description of how the plant was left. Say that. Do not proceed to an optimizer because the notebook ran.

From *When a Monitor May Speak*, Tristan, Data Center Field Guides. No store link until the Kindle edition is listed.

Related: [A model cannot learn a fan speed it never saw](06c-model-cannot-learn-a-speed-it-never-saw.md).
