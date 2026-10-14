# 34. How to read a cooling claim

Cooling claims fail in the same place power claims fail: a drawing is treated as a test, and a design condition is treated as tonight. Start with the sentence. What must the room do for the equipment in scope. A supply temperature, a redundancy of units, a water source, a rejection path. If the sentence is only "cooled to industry standard," you do not have a sentence. Industry standard is not a number you may reconstruct. Ask them to point to the contract line. If they cannot, the cooling performance is not stated.

A unit count on a drawing is a name. It is tested only if a document says the remaining units carried the load, or you saw that test. You will not stage that test. Spoken N+1 does not enter the opinion as tested. A control system that rotates units is not a test of what happens when one is off. Rotation is a schedule. Failure is a different hour.

Water is a duration question and a path question. Duration: when the utility stops, is there a volume tied to a demand in a document, or only a tank you saw. A tank without the tie is a tank. Path: one source or two, and whether the second is real. A loop drawn on paper is not a second source until a document or a valve you can have explained shows it can feed the plant alone. Do not estimate liters. Do not adopt their daily use without the basis.

Heat rejection outside, towers or dry coolers or whatever they use, is in scope only as far as the contract's cooling sentence needs it. You are not optimizing it. A model of fan speed is not a finding that the plant is efficient. Efficiency was not the question unless the engagement asked, and even then only a meter you were shown can support a number. Chapter 32. A tower that is running is not a test of approach. Approach is a measurement with a clock, or it is not in the opinion.

Leaks that can reach the equipment are the risk you can see without becoming the designer. Route evidenced, route not entered, or route only described. Description is an interview. The floor void you did not enter is not dry.

## The cooling audit formula and thermal ride-through

As detailed in Figure 09.4, an evaporative cooling claim must be reconciled against the thermodynamic water demand:
- **Evaporative Consumption**: Wet cooling towers consume approximately 1.5–2.2 liters per kilowatt-hour of heat rejected. For a 20 MW continuous critical heat load, the 48-hour emergency water reserve requires:
 $$V_{\text{water}} = 20,000\,\text{kW} \times 1.8\,\text{L/kWh} \times 48\,\text{hours} = 1,728,000\,\text{liters} \quad (\approx 1,728\,\text{m}^3)$$
 If the on-site raw water storage tanks fall below this volume and dual independent municipal water mains are not proven via physical utility GIS route maps, log an emergency water duration deficiency.
- **Chilled Water Thermal Energy Storage (TES)**: Centrifugal chillers require 7–12 minutes (t_restart) to restart following an electrical transfer. In high-density AI whitespaces, coolant supply temperature spikes beyond IT warranty limits within 90 seconds unless an inline stratified thermal buffer is installed:
 $$V_{\text{tes}} = \frac{Q_{\text{cooling}} \times t_{\text{restart}}}{\rho \times C_p \times \Delta T}$$
 Verify that the secondary loop thermal inertia or TES tank volume satisfies this equation.
- **Closed-Loop Liquid Secondary Circuit**: For direct-to-chip liquid cooling loops (CDUs), inspect water quality logs: electrical conductivity must be maintained at ≤ 10–30 μS/cm (or ≤ 100 μS/cm with propylene glycol), and biocide reserves must be evidenced.

## Decisions to record

- Cooling sentence from the contract, or not stated.
- Unit redundancy: tested, documented, spoken, or a rotation schedule only.
- Water duration tied to demand equation (1.5–2.2 L/kWh), or not tied.
- Chilled water thermal buffer (TES) verified for centrifugal chiller restart latency (7–12 min).
- CDU closed-loop fluid conductivity and corrosion inhibition records verified.
- Heat-rejection efficiency not signed from a running tower.
