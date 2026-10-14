---
title: Fixed inputs are not fan handles
description: Weather, flow, and water temperatures are conditions. Tower count and fan speed are the only things a search may move.
book: When a Monitor May Speak
slug: fixed-and-adjustable
---

# Fixed inputs are not fan handles

![Conditions are not handles.](figures/tower-model.png)

*Original diagram. Not a site record. Not a control schematic.*


Write two lists before anyone fits a line. Conditions are what the plant and the weather already are. Handles are what a person is allowed to change. Mixing them is how a model "optimizes" the outdoor wet bulb.

Conditions, for a condenser tower, are the ones you can measure and not choose in that hour: entering water temperature, leaving water temperature, dry bulb, wet bulb, and flow, if the flow is not itself a handle. Handles are tower on or off, fan speed, and pump speed only if the procedure already allows that pump to move. A setpoint the chiller must not cross is a fence, not a handle.

The search, if you run one, moves only the handles. It holds the conditions at the values a live point just reported. A search that also moves wet bulb until the power looks small has left the plant. It is a spreadsheet. File it as a spreadsheet.

Each condition is a point. It needs a clock, a source, and a quality mark before the model may speak. A stale wet bulb is not a reason to slow a fan. A missing flow is not zero. If any condition the suggestion depends on is stale or missing, the suggestion does not go out. You may still look at the last fit. You may not obey it.

Write the objective in one sentence: tower and pump power, not a blended score that hides a warmer leaving temperature inside a greener total. If leaving temperature moved, that is a second result. Do not let it disappear into the kilowatt.

From *When a Monitor May Speak*, Tristan, Data Center Field Guides. No store link until the Kindle edition is listed.

Related: [A monitoring point needs a clock](06-a-point-needs-a-clock.md).
