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

Each plateau needs an objective quantitative definition rather than relying on an uncalibrated front-panel status indicator. Prefer: this plateau is a commanded electrical power, and it is valid only when the liquid set is inside the band you cited for that plateau. If you have no bands yet, the plateau is still a commanded power held for the dwell, and the liquid set is recorded rather than judged. Recording without judging is acceptable early. Judging without recording is not. Calling a manual dial position a plateau is neither.

Dwell duration belongs to the plateau definition. Specify the minimum thermal stabilization dwell time in minutes (typically 15 to 30 minutes per step after $dT_{\text{return}}/dt < 0.1\,\text{K/min}$). A dwell that ends arbitrarily at the operator's discretion will be cut short when the delivery truck is waiting and extended only when a demonstration is going well. Neither is a repeatable measurement.

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
