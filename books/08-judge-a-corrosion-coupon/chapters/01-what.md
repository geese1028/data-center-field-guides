# 1. What you are judging

You are judging whether gases in the air are consuming metal on the equipment, fast enough that you are not willing to call the room fit for the boards you intend to run. You are not judging cleanliness in the housekeeping sense. A room can be swept and still be corrosive. A room can look hazy and not be the problem this sheet is for.

The metal that matters changed when boards stopped using the old leaded finish. Immersion silver, and solders of tin, copper, and silver, put silver where the joint is. Silver is not a decoration. It is a path. Gases that attack silver can open a joint while the copper in the same room still looks acceptable. A pass on copper alone is not a pass. Write both metals, or write that you did not measure silver and you will not claim the joints.

This is not the corrosion of a steel pipe in a water loop. Iron in a chilled-water report does not tell you about the air at a board. Do not staple those reports together and call them one trend. Different metal, different path, different sheet.

Smell is not a measurement. A nose adapts, and many of the gases that matter do not announce themselves at the concentration that hurts a joint. A particle counter is not a measurement of this problem either. Particles and gases travel together often enough that people mix the sentences. A filter that catches dust has not necessarily caught the gas. If the only instrument in the pack is a particle counter, you do not have a corrosion result. You have a dust result. File it on a different line.

## What this is not

A shorted board has many causes. Dust, moisture, a bad joint from the day it was made, a scratch, a cleaner someone sprayed. Gas corrosion is one cause, and only after the coupon says the air could do it. Do not use this sheet to close a failure investigation. The coupon does not identify which joint failed, and it does not date the failure. If a board failed in the interval, write that as a separate fact, with its own owner. Mixing them is how a bad hang becomes a vendor's fault, or a real air problem becomes a manufacturing story. Leave both open until each has its own evidence.

Do not import a water-treatment trend, a particle count, or a temperature map to fill a missing silver strip. Adjacent measurements are conditions or other problems. They are not a substitute metal. If the only reason you believe the air is fit is that the room is cool and the floor is clean, you believe a different sheet. Say so. Do not sign this one.

## What a result is allowed to mean

![ISA-71.04-2013 Environmental Severity Classification Matrix](../figures/fig-02-isa-71-04-severity-classification-matrix.png)


A coupon result supports one sentence: over this interval, at this place, this metal reacted at the rate the report states, and the report's method names a class or it does not. It does not support "the hall is safe," "the city is dirty," or "the boards will fail by a date." Failure dates are not in the coupon. If someone offers one, label it a guess. Guesses do not go in the sentence.

A class name without the report's method is a word. You may not carry it onto a slide as if you had measured it. Cite the standard's title and edition when the report cites them. Do not reconstruct the class from memory of a table. If you do not have the report, you do not have the class.

## Electrochemical Creep Corrosion on Immersion Silver (ImAg) and SAC305 Solder

### Why Copper Coupons Alone Fail to Detect Reduced-Sulfur Attack on Silver

Under **ANSI/ISA-71.04-2013** (*Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*) and **ASHRAE TC 9.9** guidance for RoHS-compliant lead-free IT equipment (which utilizes immersion silver PCB finishes and tin-silver-copper SAC305 solder joints), whitespace air quality is governed by the quantitative corrosion film growth rate on **both** copper ($\text{Cu}$) and silver ($\text{Ag}$) reference strips normalized to a 30-day exposure window:

$$2\text{Ag} + \text{H}_2\text{S} + \frac{1}{2}\text{O}_2 \xrightarrow{\text{RH}} \text{Ag}_2\text{S} + \text{H}_2\text{O}$$

Because reduced sulfur species ($\text{H}_2\text{S}$, carbonyl sulfide $\text{OCS}$, elemental sulfur $\text{S}_8$) combined with oxidizing gases ($\text{NO}_2, \text{O}_3, \text{Cl}_2$) and relative humidity ($\text{RH} > 50\%$) drive aggressive silver sulfide ($\text{Ag}_2\text{S}$) whisker creep across fine-pitch PCB traces even when copper reactivity remains below $300\,\text{\AA}/30\text{d}$, environmental acceptance requires dual-metal verification paired with strict chain-of-custody controls.

| Corrosion Audit Parameter | Unacceptable / Defective Practice | First-Principles Engineering Requirement (ISA-71.04 / ASTM B825) | Mandatory Refusal or Remediation Action |
| :--- | :--- | :--- | :--- |
| **Core Chapter Focus** | Separating Gas-Phase Reactivity from Particulate Dust and Water Loops | Dual $\text{Cu} + \text{Ag}$ coulometric reduction with documented exposure timestamps | Refuse any environmental fitness claim missing $\text{Ag}$ or hang interval |
| **Class G1 Mild Pass Gate** | Quoting Copper rate alone ($<300\,\text{\AA}$) or visual strip color | $d_{\text{Cu}} < 300\,\text{\AA}/30\text{d}$ **AND** $d_{\text{Ag}} < 200\,\text{\AA}/30\text{d}$ (zero $\text{Cu}_2\text{S}$ on copper) | Classify G2 ($<1000/1000\,\text{\AA}$), G3 ($<2000/2000\,\text{\AA}$), or GX as non-compliant |
| **Chain of Custody & Blank** | Mailing strips without a sealed Field Travel Blank (`FTB`) | Sealed lot-matched travel blank $d_{\text{blank}} \le 25\text{--}35\,\text{\AA}$ subtracted/verified | Invalidate "Fit" certification if no unopened travel blank accompanied lot |
| **Filtration & Envelope Proof** | Installing recirculation filters in an unsealed negative-$\Delta P$ hall | Vapor-sealed envelope ($\Delta P \ge +12.5\,\text{Pa}$) + gas-matched media ($\text{EBCT} \ge 0.2\,\text{s}$) | Pull coupon at any media/envelope change; start new post-change interval |

## Decisions to record

- Gas on board metal, not pipe water, not housekeeping dust.
- Copper and silver both named, or silver explicitly not measured and not claimed.
- The one sentence this result may support. No failure date.
