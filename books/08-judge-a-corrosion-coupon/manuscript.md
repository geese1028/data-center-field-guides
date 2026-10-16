# 0. How to use this piece

This piece is for the person who must decide whether the air in a hall is attacking the boards. The attack is gas on metal, not dust on a filter, and not rust in a water pipe. Those are other problems. They do not get this sheet.

It is not a product brochure. It is not a course slide. It is not a customer's coupon report rewritten in cleaner English. The method is the one used when a room looked treated and the silver still moved: hang a coupon where the boards live, keep it there long enough to see the season, seal the leaks before you buy a machine, and treat the air that enters, or do not claim the room is held.

A standard may already name the severity classes. Cite the edition. Do not paste the table, and do not invent a class from a photograph of a tarnished strip. The number comes from the report you are allowed to use. This piece does not contain one.

When you finish, you should be able to hand over one coupon sheet. It names the metal, the place, the start, the end, who read it, and the sentence you are allowed to write. The sheet is in chapter 9. If a vendor is already in the room with a before-and-after picture, start at chapter 8. If they are selling media, start at chapter 14, then chapter 15. The gas families, without a concentration table, are chapter 12. How to read the lab pdf is chapter 13. The blank that has to travel with the strip is chapter 19. The shift, after you refuse the class, is chapter 20. When to hang again, without a magic number of days, is chapter 21.

| **ATMOSPHERIC CORROSION GATING PIPELINE** |
| :--- |
| [OUTDOOR SMOG] → [CHEMICAL SCRUBBERS] → [DATA HALL WHITESPACE] |
| H2S, SO2, NOx, Cl2 Carbon & Permanganate Positive Pressure: +20 Pa |
| Breakthrough <= 5% Class G1: Cu < 300Å, Ag<200Å |

## What you may copy

You may copy the sheet headings. You may not paste a sentence from this piece into a customer's procedure and call it their limit. Their report, their media, and their room names stay in their file.

## ANSI/ISA-71.04-2013 Reactivity Governance for RoHS Lead-Free Hardware

### Why G1 Mild Environments Are Mandatory for Modern AI and Enterprise Racks

Under **ANSI/ISA-71.04-2013** (*Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*) and **ASHRAE TC 9.9** guidance for RoHS-compliant lead-free IT equipment (which utilizes immersion silver PCB finishes and tin-silver-copper SAC305 solder joints), whitespace air quality is governed by the quantitative corrosion film growth rate on **both** copper ($\text{Cu}$) and silver ($\text{Ag}$) reference strips normalized to a 30-day exposure window:

$$d_{\text{Cu}} < 300\,\text{\AA}/30\text{d} \;\land\; d_{\text{Ag}} < 200\,\text{\AA}/30\text{d} \implies \text{ISA Class G1 (Mild)}$$

Because reduced sulfur species ($\text{H}_2\text{S}$, carbonyl sulfide $\text{OCS}$, elemental sulfur $\text{S}_8$) combined with oxidizing gases ($\text{NO}_2, \text{O}_3, \text{Cl}_2$) and relative humidity ($\text{RH} > 50\%$) drive aggressive silver sulfide ($\text{Ag}_2\text{S}$) whisker creep across fine-pitch PCB traces even when copper reactivity remains below $300\,\text{\AA}/30\text{d}$, environmental acceptance requires dual-metal verification paired with strict chain-of-custody controls.

| Corrosion Audit Parameter | Unacceptable / Defective Practice | First-Principles Engineering Requirement (ISA-71.04 / ASTM B825) | Mandatory Refusal or Remediation Action |
| :--- | :--- | :--- | :--- |
| **Core Chapter Focus** | Establishing the Dual-Metal Cu/Ag Audit Baseline | Dual $\text{Cu} + \text{Ag}$ coulometric reduction with documented exposure timestamps | Refuse any environmental fitness claim missing $\text{Ag}$ or hang interval |
| **Class G1 Mild Pass Gate** | Quoting Copper rate alone ($<300\,\text{\AA}$) or visual strip color | $d_{\text{Cu}} < 300\,\text{\AA}/30\text{d}$ **AND** $d_{\text{Ag}} < 200\,\text{\AA}/30\text{d}$ (zero $\text{Cu}_2\text{S}$ on copper) | Classify G2 ($<1000/1000\,\text{\AA}$), G3 ($<2000/2000\,\text{\AA}$), or GX as non-compliant |
| **Chain of Custody & Blank** | Mailing strips without a sealed Field Travel Blank (`FTB`) | Sealed lot-matched travel blank $d_{\text{blank}} \le 25\text{--}35\,\text{\AA}$ subtracted/verified | Invalidate "Fit" certification if no unopened travel blank accompanied lot |
| **Filtration & Envelope Proof** | Installing recirculation filters in an unsealed negative-$\Delta P$ hall | Vapor-sealed envelope ($\Delta P \ge +12.5\,\text{Pa}$) + gas-matched media ($\text{EBCT} \ge 0.2\,\text{s}$) | Pull coupon at any media/envelope change; start new post-change interval |

## Decisions to record

- The sentence this coupon is allowed to support.
- The metal you will not ignore because the other metal looked calm.
- The makeup path you have not treated, if you are about to claim the room is held.

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

# 2. A coupon is the record

A coupon is a piece of metal of a known kind, exposed on purpose, for a known time, then read by a method you can name. It is a standardized metallurgically prepared reference strip (typically high-purity 99.99% Copper and 99.99% Silver), never an uncalibrated scrap of electrical busbar or a casual smartphone photograph of a tarnished connector. Photographs show that something happened. They do not give you a rate, and they do not tell you when it happened.

Write the metal. Copper and silver are the pair this judgment uses, because they do not move together. If the lab adds another metal, it is an extra. It does not replace the pair. A report that reads only copper is a partial. Chapter 1. Partial may be stored. It may not close the sentence about the joints.

Write who exposed it and who read it. They should not be the same person if that person also sells the treatment. A vendor may hang a coupon. The read that you will sign should be a method you can point to, not a slide in their deck. If the only read is theirs, say so on the sheet. You may still use it as a hypothesis. You may not use it as the sentence you give a customer, unless a second read, or a method you accept, agrees. Agreement means the same metal, the same interval, the same place, not a similar adjective.

## The clock on the metal

The coupon integrates. It does not tell you Tuesday. The start and the end are the measurement times. The day you received the report is arrival time. Do not plot the class on the day the pdf arrived and call that the week the air changed. The sixth book's clock rule applies. A late report may correct the record. It may not be drawn as a fresh event.

The rate is meaningless without the interval. A strip that hung for a week is not comparable to a strip that hung for a season, even if someone divides both down to a month. Division assumes the attack was steady. It often is not. Keep the actual start and end on the sheet. If the report only gives a normalized rate and hides the hang time, ask for the hang time before you use the rate. Hidden interval is a missing clock. Missing clock, the point may not speak.

Do not invent a rate because a coupon "looked like" one you saw elsewhere. Another hall is not this coupon. The seventh book already refused that transfer. It applies here with less argument, because the number is the whole claim.

## A blank travels with it

Chapter 19 is the blank: a strip from the same lot that never sees the room, so the trip and the lab are not mistaken for the hall. If you did not send one, you may still file a harsh result as a reason to look. You may not sign a fit class. Fit without a blank is fit you cannot separate from the mailer. Send the blank. Do not open it to show a visitor what a clean strip looks like. An opened blank is spoiled. A spoiled blank does not clear the trip.

## What you send, and what you keep

You send the coupon, not a story. You keep the place, the height, the start, the end, and a note of what was running: makeup on or off, doors propped, a treatment unit installed midway. A change midway makes two intervals. If you leave the coupon up across the change, you have averaged a before and an after into one rate. That average cannot prove the treatment. Pull the coupon at the change, or hang a second one. Do not discover this when the lab returns a single number and the vendor wants it as the after.

The lab's raw read stays in their report. You do not retype a table from a standard into the customer note to make the class look official. The note says the class the report named, the edition the report cited, and where the report is filed. If the report names no edition, you do not supply one from memory.

## Coulometric Cathodic Reduction (ASTM B825) and Faraday Film Thickness Math

### Deriving Angstroms per 30 Days from Laboratory Reduction Charge

Under **ANSI/ISA-71.04-2013** (*Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*) and **ASHRAE TC 9.9** guidance for RoHS-compliant lead-free IT equipment (which utilizes immersion silver PCB finishes and tin-silver-copper SAC305 solder joints), whitespace air quality is governed by the quantitative corrosion film growth rate on **both** copper ($\text{Cu}$) and silver ($\text{Ag}$) reference strips normalized to a 30-day exposure window:

$$d_{\text{film}} = \frac{I_{\text{red}} \cdot t_{\text{red}} \cdot M_{\text{mol}}}{n \cdot F \cdot A_{\text{surface}} \cdot \rho_{\text{film}}} \times 10^8\,\text{\AA/cm}$$

Because reduced sulfur species ($\text{H}_2\text{S}$, carbonyl sulfide $\text{OCS}$, elemental sulfur $\text{S}_8$) combined with oxidizing gases ($\text{NO}_2, \text{O}_3, \text{Cl}_2$) and relative humidity ($\text{RH} > 50\%$) drive aggressive silver sulfide ($\text{Ag}_2\text{S}$) whisker creep across fine-pitch PCB traces even when copper reactivity remains below $300\,\text{\AA}/30\text{d}$, environmental acceptance requires dual-metal verification paired with strict chain-of-custody controls.

| Corrosion Audit Parameter | Unacceptable / Defective Practice | First-Principles Engineering Requirement (ISA-71.04 / ASTM B825) | Mandatory Refusal or Remediation Action |
| :--- | :--- | :--- | :--- |
| **Core Chapter Focus** | Auditing Laboratory Reduction Curves for Cu2O, CuO, Cu2S, Ag2S, and AgCl | Dual $\text{Cu} + \text{Ag}$ coulometric reduction with documented exposure timestamps | Refuse any environmental fitness claim missing $\text{Ag}$ or hang interval |
| **Class G1 Mild Pass Gate** | Quoting Copper rate alone ($<300\,\text{\AA}$) or visual strip color | $d_{\text{Cu}} < 300\,\text{\AA}/30\text{d}$ **AND** $d_{\text{Ag}} < 200\,\text{\AA}/30\text{d}$ (zero $\text{Cu}_2\text{S}$ on copper) | Classify G2 ($<1000/1000\,\text{\AA}$), G3 ($<2000/2000\,\text{\AA}$), or GX as non-compliant |
| **Chain of Custody & Blank** | Mailing strips without a sealed Field Travel Blank (`FTB`) | Sealed lot-matched travel blank $d_{\text{blank}} \le 25\text{--}35\,\text{\AA}$ subtracted/verified | Invalidate "Fit" certification if no unopened travel blank accompanied lot |
| **Filtration & Envelope Proof** | Installing recirculation filters in an unsealed negative-$\Delta P$ hall | Vapor-sealed envelope ($\Delta P \ge +12.5\,\text{Pa}$) + gas-matched media ($\text{EBCT} \ge 0.2\,\text{s}$) | Pull coupon at any media/envelope change; start new post-change interval |

## Decisions to record

- Metal, place, start, end. Not the day the pdf arrived.
- Who hung it, who read it. Vendor-only read marked as hypothesis if that is all you have.
- Hang time visible. A normalized rate with no interval is not used.
- Coupon pulled at a treatment change, or a second coupon hung. Not one average across the change.


![Dual Copper & Silver Corrosion Coupon Anatomy](../figures/fig-01-isa-coupon-anatomy-and-reactivity-rate.png)

# 3. Where it hangs

The coupon measures the air that touched it. It does not measure the hall. A strip in the return says what left the room. A strip in the supply says what the unit delivered. A strip at the face of a board says what that board saw. These are three sentences. A meeting will try to make them one. Do not sign the merged sentence.

Hang the one that matches the claim. If the claim is that the boards are in fit air, the coupon belongs where the boards live, not in the prettiest aisle and not inside the treatment unit's own discharge. A coupon in the discharge proves the unit can clean the air it just cleaned. It does not prove the room. That trick is the same shape as a temperature probe in a supply stub being called an inlet. The fourth book already refused the stub. Refuse the discharge.

Height and facing matter enough to write down. A strip on top of a cabinet in a dead pocket is a different sample from a strip in the stream that feeds the face. You do not need a model to know they differ. You need to write which one you hung, so the next person does not hang the other and announce a trend. If you cannot describe the place without a room number that identifies a site, describe the function: board face, cold aisle, supply leaving the unit, return entering the unit, makeup before treatment, makeup after treatment. Function is enough. The site name stays in their file.

## Outside and inside

A coupon outside, or in the makeup before any treatment, is the source. A coupon inside is the result after the building has done whatever it does. You want both if you are about to spend money on treatment. Without the outside coupon, a bad inside result does not tell you whether the city, the street, a loading dock, or a dead animal in a duct is the source. You will buy the wrong machine. Without the inside coupon, a bad outside result does not tell you whether the building already keeps it out. You will buy a machine for a problem the envelope already solved.

Do not hang one coupon "for the site" and let every room inherit it. A sealed electrical room and a hall with a propped door are not the same air. One coupon per sentence. If you cannot afford two, write which sentence you are not supporting. Absence is allowed. Inheritance is not.

## People move them

A coupon that was taken down for a tour, then rehung, has a gap. Write the gap. Do not let the lab's single rate cover the days it was in a drawer. A coupon moved from the board face to the return halfway, without a note, is two places and no result. Treat it as missing. Chapter 6 of the monitor book: missing is not zero, and it is not a pass.

## Spatial Coupon Placement Topology Across Supply, Return, and Rack Inlets

### Mapping Local Micro-Environments and Air-Handling Mixing Ratios

Under **ANSI/ISA-71.04-2013** (*Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*) and **ASHRAE TC 9.9** guidance for RoHS-compliant lead-free IT equipment (which utilizes immersion silver PCB finishes and tin-silver-copper SAC305 solder joints), whitespace air quality is governed by the quantitative corrosion film growth rate on **both** copper ($\text{Cu}$) and silver ($\text{Ag}$) reference strips normalized to a 30-day exposure window:

$$C_{\text{inlet}}(x,y,z) = \alpha C_{\text{makeup}} + (1 - \alpha) C_{\text{recirc}} (1 - \eta_{\text{media}})$$

Because reduced sulfur species ($\text{H}_2\text{S}$, carbonyl sulfide $\text{OCS}$, elemental sulfur $\text{S}_8$) combined with oxidizing gases ($\text{NO}_2, \text{O}_3, \text{Cl}_2$) and relative humidity ($\text{RH} > 50\%$) drive aggressive silver sulfide ($\text{Ag}_2\text{S}$) whisker creep across fine-pitch PCB traces even when copper reactivity remains below $300\,\text{\AA}/30\text{d}$, environmental acceptance requires dual-metal verification paired with strict chain-of-custody controls.

| Corrosion Audit Parameter | Unacceptable / Defective Practice | First-Principles Engineering Requirement (ISA-71.04 / ASTM B825) | Mandatory Refusal or Remediation Action |
| :--- | :--- | :--- | :--- |
| **Core Chapter Focus** | Hanging Paired Strips at Outdoor Makeup, Chemical Filter Outlet, and Rack Bezels | Dual $\text{Cu} + \text{Ag}$ coulometric reduction with documented exposure timestamps | Refuse any environmental fitness claim missing $\text{Ag}$ or hang interval |
| **Class G1 Mild Pass Gate** | Quoting Copper rate alone ($<300\,\text{\AA}$) or visual strip color | $d_{\text{Cu}} < 300\,\text{\AA}/30\text{d}$ **AND** $d_{\text{Ag}} < 200\,\text{\AA}/30\text{d}$ (zero $\text{Cu}_2\text{S}$ on copper) | Classify G2 ($<1000/1000\,\text{\AA}$), G3 ($<2000/2000\,\text{\AA}$), or GX as non-compliant |
| **Chain of Custody & Blank** | Mailing strips without a sealed Field Travel Blank (`FTB`) | Sealed lot-matched travel blank $d_{\text{blank}} \le 25\text{--}35\,\text{\AA}$ subtracted/verified | Invalidate "Fit" certification if no unopened travel blank accompanied lot |
| **Filtration & Envelope Proof** | Installing recirculation filters in an unsealed negative-$\Delta P$ hall | Vapor-sealed envelope ($\Delta P \ge +12.5\,\text{Pa}$) + gas-matched media ($\text{EBCT} \ge 0.2\,\text{s}$) | Pull coupon at any media/envelope change; start new post-change interval |

## Decisions to record

- Function of the place: board face, supply, return, makeup before, makeup after. One sentence each.
- Discharge of the treatment unit not used as the room.
- Outside and inside both present, or the sentence you are not supporting written down.
- Gaps and moves noted, or the rate not used.


![Data Center Coupon Spatial Placement Architecture](../figures/fig-03-data-hall-coupon-placement-topology.png)

# 4. How long, and the season

A coupon that hangs for a short visit measures the visit. It does not measure the year. Outdoor air changes with the season. Humidity changes with the season. A treatment that held in the cold can fail when the makeup load rises, because more dirty air is being pushed in than the indoor unit can take. If you have not hung through that change, you do not have a result for the year. You have a result for the weeks you hung. Write the weeks. Do not let the report's monthly rate become "the hall, annually."

The failure mode is specific. Indoor treatment alone can look successful until the makeup path starts delivering untreated outdoor air in volume. The indoor unit did not get worse. The source got louder. Pulling the coupon only in the quiet season, then signing the room, is how that surprise is scheduled. Hang across the change, or hang a second interval when the makeup is known to be at its highest, and do not sign the year from the quiet interval.

## What "long enough" is not

This piece will not give you a minimum number of days. A number invented here would be a false precision, and a number copied from a standard's table would be a paste. The report's method names the interval it stands behind. If it does not, you do not invent one. You can still refuse a visit-length hang as support for an annual sentence. That refusal does not require a magic duration. It requires the sentence to match the clock you actually have.

Two intervals are more honest than one smoothed rate. Before treatment and after treatment, each with its own start and end. Quiet season and loud season, the same. If you only have one, the sheet says which season is missing. Missing season, the annual sentence is refused.

Humidity and temperature belong in the note if you are going to explain a change. They are not the corrosion result. They are the conditions. If you do not have them, do not explain the change by a story about the weather. Say the rate changed and you do not have the conditions. A weather story without a record is the hypothesis the day book already told you not to inherit.

## A live week is not a coupon month

Someone will offer a real-time box as a way to skip the wait. Chapter 7 is that box. It does not shorten the coupon. If you need a year, you still need the time. The box may tell you a week was loud. It does not replace the metal that sat there.

## Non-Linear Tarnish Growth Kinetics and 30-Day Normalization Errors

### Parabolic Copper Diffusion vs. Linear Silver Sulfidation Across Seasons

Under **ANSI/ISA-71.04-2013** (*Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*) and **ASHRAE TC 9.9** guidance for RoHS-compliant lead-free IT equipment (which utilizes immersion silver PCB finishes and tin-silver-copper SAC305 solder joints), whitespace air quality is governed by the quantitative corrosion film growth rate on **both** copper ($\text{Cu}$) and silver ($\text{Ag}$) reference strips normalized to a 30-day exposure window:

$$d_{\text{norm}}(30\text{d}) = d_{\text{meas}}(t_{\text{hang}}) \cdot \left( \frac{30}{t_{\text{hang}}} \right)^n, \quad n_{\text{Cu}} \in [0.5, 0.7], \; n_{\text{Ag}} \approx 1.0$$

Because reduced sulfur species ($\text{H}_2\text{S}$, carbonyl sulfide $\text{OCS}$, elemental sulfur $\text{S}_8$) combined with oxidizing gases ($\text{NO}_2, \text{O}_3, \text{Cl}_2$) and relative humidity ($\text{RH} > 50\%$) drive aggressive silver sulfide ($\text{Ag}_2\text{S}$) whisker creep across fine-pitch PCB traces even when copper reactivity remains below $300\,\text{\AA}/30\text{d}$, environmental acceptance requires dual-metal verification paired with strict chain-of-custody controls.

| Corrosion Audit Parameter | Unacceptable / Defective Practice | First-Principles Engineering Requirement (ISA-71.04 / ASTM B825) | Mandatory Refusal or Remediation Action |
| :--- | :--- | :--- | :--- |
| **Core Chapter Focus** | Why a 7-Day Short Hang Cannot Certify Annual Seasonal Compliance | Dual $\text{Cu} + \text{Ag}$ coulometric reduction with documented exposure timestamps | Refuse any environmental fitness claim missing $\text{Ag}$ or hang interval |
| **Class G1 Mild Pass Gate** | Quoting Copper rate alone ($<300\,\text{\AA}$) or visual strip color | $d_{\text{Cu}} < 300\,\text{\AA}/30\text{d}$ **AND** $d_{\text{Ag}} < 200\,\text{\AA}/30\text{d}$ (zero $\text{Cu}_2\text{S}$ on copper) | Classify G2 ($<1000/1000\,\text{\AA}$), G3 ($<2000/2000\,\text{\AA}$), or GX as non-compliant |
| **Chain of Custody & Blank** | Mailing strips without a sealed Field Travel Blank (`FTB`) | Sealed lot-matched travel blank $d_{\text{blank}} \le 25\text{--}35\,\text{\AA}$ subtracted/verified | Invalidate "Fit" certification if no unopened travel blank accompanied lot |
| **Filtration & Envelope Proof** | Installing recirculation filters in an unsealed negative-$\Delta P$ hall | Vapor-sealed envelope ($\Delta P \ge +12.5\,\text{Pa}$) + gas-matched media ($\text{EBCT} \ge 0.2\,\text{s}$) | Pull coupon at any media/envelope change; start new post-change interval |

## Decisions to record

- Interval actually hung. Annual sentence refused if the loud season is missing.
- Before and after kept as two intervals, not one rate across the install.
- Weather explanation refused unless the conditions were recorded.
- No duration invented to make a short hang look standard.

# 5. Seal the room before you buy the machine

The first work is the envelope, not the catalog. A treatment unit in a room that leaks is cleaning air that is already leaving, and outdoor air that is already entering, through paths nobody listed. Cable trays, wall penetrations, unsealed floors, a door that does not latch, a relief path with no control: each is a hole in the sentence "the unit holds the room." Close the holes you can see, then hang the coupon. Do not hang it, buy the unit, and seal later. Later's coupon will not tell you which action did the work.

Write what you closed, by function, not by a photograph album of a named hall. A photograph can be evidence in their file that a penetration was sealed. It is not the sheet. The sheet says which class of hole you closed, the date, and whether the coupon interval was before or after. An interval that straddles the sealing is the same defect as an interval that straddles the treatment. Chapter 2. Pull it or hang another.

## Where to look, by function

Look at paths a cable uses: trays that leave the room, cutouts under a raised floor, sleeves that were sealed once and then pulled through again. Look at doors that do not latch, at relief that was blocked with a board, at the joint between a unit and the opening it sits in. Look at the makeup intake before you look at the catalog. You are not performing a tightness test this piece does not own. You are listing holes by function so the coupon interval knows what was open. A number from a blower-door test, if they have one, stays in their report. It does not replace the list. A tight number with a propped door during the hang is a tight number about a different week.

Write the list before the coupon goes up, and again when you take it down. The second list is how you notice the cable pull. One list, made from memory after a bad report, is a story. Stories do not choose the next machine.

## What sealing is not

Sealing is not a promise that the room is a laboratory. Doors will open. People will enter. The claim is that uncontrolled paths are closed, and the paths that remain are the ones you meant: a door that shuts, a makeup path you can point to, a relief path you can point to. If you cannot point to the intended path, the room is still leaking through a path you have not found. Look again before you buy. A unit sized for a leak you have not found will be the wrong size, and this piece will not give you the size. Sizing is their calculation, in their file, from a method they can show. It is not a number you invent in the corridor.

Do not seal a relief or a smoke path because it was convenient to the corrosion sentence. Life safety paper wins. If a path must stay open for that paper, it is an intended path. Treat the air that uses it, or accept that this path is a source. Do not hide the path in the sealing note as "closed."

## Recheck

Seals fail. A cable pull next month opens what you closed. The coupon does not know why the rate returned. The note has to. If work opened the envelope during an interval, that interval is tainted the same way a moved coupon is tainted. Mark it. Do not let a vendor call the return a proof that you need a larger machine. You may need a larger machine. You may need the hole closed again. The coupon alone cannot say which. Go and look.

## Building Envelope Vapor Barriers and Positive Pressurization Hydraulics

### Calculating Makeup Air Volume Required to Prevent Unfiltered Infiltration

Under **ANSI/ISA-71.04-2013** (*Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*) and **ASHRAE TC 9.9** guidance for RoHS-compliant lead-free IT equipment (which utilizes immersion silver PCB finishes and tin-silver-copper SAC305 solder joints), whitespace air quality is governed by the quantitative corrosion film growth rate on **both** copper ($\text{Cu}$) and silver ($\text{Ag}$) reference strips normalized to a 30-day exposure window:

$$\Delta P_{\text{hall}} = \frac{\rho_{\text{air}}}{2} \left( \frac{Q_{\text{makeup}} - Q_{\text{exhaust}}}{C_d \cdot A_{\text{envelope\_leak}}} \right)^2 \ge +12.5\,\text{Pa}$$

Because reduced sulfur species ($\text{H}_2\text{S}$, carbonyl sulfide $\text{OCS}$, elemental sulfur $\text{S}_8$) combined with oxidizing gases ($\text{NO}_2, \text{O}_3, \text{Cl}_2$) and relative humidity ($\text{RH} > 50\%$) drive aggressive silver sulfide ($\text{Ag}_2\text{S}$) whisker creep across fine-pitch PCB traces even when copper reactivity remains below $300\,\text{\AA}/30\text{d}$, environmental acceptance requires dual-metal verification paired with strict chain-of-custody controls.

| Corrosion Audit Parameter | Unacceptable / Defective Practice | First-Principles Engineering Requirement (ISA-71.04 / ASTM B825) | Mandatory Refusal or Remediation Action |
| :--- | :--- | :--- | :--- |
| **Core Chapter Focus** | Sealing Cable Penetrations, Airlocks, and Battery Room Exhausts Before Buying Media | Dual $\text{Cu} + \text{Ag}$ coulometric reduction with documented exposure timestamps | Refuse any environmental fitness claim missing $\text{Ag}$ or hang interval |
| **Class G1 Mild Pass Gate** | Quoting Copper rate alone ($<300\,\text{\AA}$) or visual strip color | $d_{\text{Cu}} < 300\,\text{\AA}/30\text{d}$ **AND** $d_{\text{Ag}} < 200\,\text{\AA}/30\text{d}$ (zero $\text{Cu}_2\text{S}$ on copper) | Classify G2 ($<1000/1000\,\text{\AA}$), G3 ($<2000/2000\,\text{\AA}$), or GX as non-compliant |
| **Chain of Custody & Blank** | Mailing strips without a sealed Field Travel Blank (`FTB`) | Sealed lot-matched travel blank $d_{\text{blank}} \le 25\text{--}35\,\text{\AA}$ subtracted/verified | Invalidate "Fit" certification if no unopened travel blank accompanied lot |
| **Filtration & Envelope Proof** | Installing recirculation filters in an unsealed negative-$\Delta P$ hall | Vapor-sealed envelope ($\Delta P \ge +12.5\,\text{Pa}$) + gas-matched media ($\text{EBCT} \ge 0.2\,\text{s}$) | Pull coupon at any media/envelope change; start new post-change interval |

## Decisions to record

- Holes closed, by function, dated against the coupon interval.
- Intended paths named: door, makeup, relief. Unnamed remaining path: do not buy yet.
- A life-safety path left open on purpose, and treated as a source, not marked closed.
- An interval tainted by later cable work, not used as a sizing argument.

# 6. Treat the air that enters

Indoor treatment can lose. It loses when makeup air arrives untreated, in enough volume that the indoor unit cannot keep up. The unit is not necessarily defective. The source was left outside the job. If you claim the room is held, the makeup path is part of the claim. A coupon after the treatment of that path, and a coupon in the room at the board face, are the pair that supports the claim. A coupon only in the room, while makeup is untreated, supports a weaker sentence: the room was at this rate while untreated air was still allowed in. Do not upgrade that sentence because the rate improved for a month.

This is the lesson that survives after the site names are removed. Treating the corridor, or setting a cleaner in the hall, is not the same job as treating the air the fans are paid to bring in. Start at the intake. If the intake has no place to treat, say so, and do not promise the class. A promise without a path is a brochure.

## What the box still owes you

Chapter 14 is the media. This chapter only says where it has to sit. A media that works on one gas family can miss another. Copper and silver already told you the gases are not one substance. A single "chemical filter" line on a drawing does not say which family it was chosen for. Ask. If they cannot say, you do not have a treatment. You have a box. Do not accept a bed depth, a vendor blend, or a change-out hour spoken in the corridor. Those are claims. Chapter 14 says which claims you may write down, and which you refuse.

Change-out is a maintenance fact, not a corrosion result. A fresh bed and a spent bed are different machines. If the sheet does not say how they know the bed is spent, they will learn it from the next coupon, which is late by definition. The coupon is the audit. It is not the only alarm if they claim continuous holding. Chapter 7 is the alarm. Chapter 15 is the spent test. Neither replaces the other.

Do not accept a bypass around the treatment as a minor path. Untreated bypass is untreated makeup. Chapter 5. An intended path you did not treat is a source. Write it on the sheet, or do not claim the class.

## After the work

Hang a new coupon when the treatment of the intake is actually in service, not when the purchase order is signed. In service means air is going through it, not around it. The before coupon ends that day. The after coupon starts that day. One strip across both is an average, and averages are how a late install borrows the credit of an early seal. Chapter 2.

Then wait through the loud season before you sign the year. Chapter 4. A good month after install is a start. It is not the sentence.

## Mass-Balance Modeling of Untreated Makeup Air vs. Recirculation Scrubbing

### Why Indoor Recirculation Units Lose Against Raw Outdoor Infiltration

Under **ANSI/ISA-71.04-2013** (*Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*) and **ASHRAE TC 9.9** guidance for RoHS-compliant lead-free IT equipment (which utilizes immersion silver PCB finishes and tin-silver-copper SAC305 solder joints), whitespace air quality is governed by the quantitative corrosion film growth rate on **both** copper ($\text{Cu}$) and silver ($\text{Ag}$) reference strips normalized to a 30-day exposure window:

$$C_{\text{steady}} = \frac{Q_{\text{makeup}}(1 - \eta_{\text{MU}}) C_{\text{outdoor}} + \dot{G}_{\text{internal}}}{Q_{\text{makeup}} + Q_{\text{recirc}} \cdot \eta_{\text{recirc}}}$$

Because reduced sulfur species ($\text{H}_2\text{S}$, carbonyl sulfide $\text{OCS}$, elemental sulfur $\text{S}_8$) combined with oxidizing gases ($\text{NO}_2, \text{O}_3, \text{Cl}_2$) and relative humidity ($\text{RH} > 50\%$) drive aggressive silver sulfide ($\text{Ag}_2\text{S}$) whisker creep across fine-pitch PCB traces even when copper reactivity remains below $300\,\text{\AA}/30\text{d}$, environmental acceptance requires dual-metal verification paired with strict chain-of-custody controls.

| Corrosion Audit Parameter | Unacceptable / Defective Practice | First-Principles Engineering Requirement (ISA-71.04 / ASTM B825) | Mandatory Refusal or Remediation Action |
| :--- | :--- | :--- | :--- |
| **Core Chapter Focus** | Sizing Dedicated Chemical Filtration on the Primary Makeup Air Handler | Dual $\text{Cu} + \text{Ag}$ coulometric reduction with documented exposure timestamps | Refuse any environmental fitness claim missing $\text{Ag}$ or hang interval |
| **Class G1 Mild Pass Gate** | Quoting Copper rate alone ($<300\,\text{\AA}$) or visual strip color | $d_{\text{Cu}} < 300\,\text{\AA}/30\text{d}$ **AND** $d_{\text{Ag}} < 200\,\text{\AA}/30\text{d}$ (zero $\text{Cu}_2\text{S}$ on copper) | Classify G2 ($<1000/1000\,\text{\AA}$), G3 ($<2000/2000\,\text{\AA}$), or GX as non-compliant |
| **Chain of Custody & Blank** | Mailing strips without a sealed Field Travel Blank (`FTB`) | Sealed lot-matched travel blank $d_{\text{blank}} \le 25\text{--}35\,\text{\AA}$ subtracted/verified | Invalidate "Fit" certification if no unopened travel blank accompanied lot |
| **Filtration & Envelope Proof** | Installing recirculation filters in an unsealed negative-$\Delta P$ hall | Vapor-sealed envelope ($\Delta P \ge +12.5\,\text{Pa}$) + gas-matched media ($\text{EBCT} \ge 0.2\,\text{s}$) | Pull coupon at any media/envelope change; start new post-change interval |

## Decisions to record

- Makeup path named. Treated, or explicitly untreated and the annual claim refused.
- Media's target gas stated by them, or the box not accepted as treatment.
- Bypass listed as a source, or absent.
- After coupon started when air was going through the treatment, not when it was ordered.


![Makeup Air Positive Pressurization & Envelope Sealing](../figures/fig-05-makeup-air-pressurization-and-leak-paths.png)

# 7. A live box is not a coupon

A real-time corrosion box is a point. The sixth book already said when a point may speak: a clock, a quality mark, a source path, a line written before the night, and a forced failure on the image you will run. Until those exist, the box may be watched. It may not page, and it may not close a coupon sentence.

The box and the coupon are not the same measurement even when both are honest. The coupon is metal that sat in the air for the whole interval. The box is a signal sampled on its own interval, often from a different place, often with a different metal or a different proxy. Write both sentences. Do not average them into one class. If they disagree, you have a disagreement, not a pass. The walked coupon, read by a method you accept, wins for the interval it covered, until you understand the box. The box does not win by being automatic. That is the same rule the fourth book used for a model and the sixth used for a screen.

## What the box is for

It is for the week you cannot wait to see. A loud week, a door left open, a bed that failed, a fire, a street event. It can tell you to go look, if it has been accepted as a point. It cannot tell you the class for the year. The year is still the coupon that was there.

A box in the discharge of the treatment unit has the same limit as a coupon there. It proves the unit's outlet, not the board face. Put the one you will obey where the claim is. If you only have one box, write the sentence it does not support.

Do not let the box's vendor set the severity class inside a black box and then page you. A class you cannot tie to a named method is a mood. Chapter 6 of the monitor book refused a score that hides its inputs. This is that score, wearing a metal. If the box will not say, in one sentence, what it is measuring and what stale means, it does not wake anyone.

## Forced failure

Stop its output on purpose, the way you stop a poll. The screen must show a gap, or show stale and refuse to page. A box that holds the last rate forward with a new time has failed acceptance. Corrosion boxes are especially tempting to hold forward, because the last rate looks like a calm room. Calm and stale are different. Stale does not prove the air recovered. It proves the box stopped talking.

## Quartz Crystal Microbalance (QCM) Real-Time Monitors vs. Passive Coupons

### Sauerbrey Frequency-Shift Equation and Volume 06 Telemetry Gate Rules

Under **ANSI/ISA-71.04-2013** (*Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*) and **ASHRAE TC 9.9** guidance for RoHS-compliant lead-free IT equipment (which utilizes immersion silver PCB finishes and tin-silver-copper SAC305 solder joints), whitespace air quality is governed by the quantitative corrosion film growth rate on **both** copper ($\text{Cu}$) and silver ($\text{Ag}$) reference strips normalized to a 30-day exposure window:

$$\Delta f = -\frac{2 f_0^2}{A \sqrt{\rho_q \mu_q}} \Delta m = -C_f \cdot \Delta m$$

Because reduced sulfur species ($\text{H}_2\text{S}$, carbonyl sulfide $\text{OCS}$, elemental sulfur $\text{S}_8$) combined with oxidizing gases ($\text{NO}_2, \text{O}_3, \text{Cl}_2$) and relative humidity ($\text{RH} > 50\%$) drive aggressive silver sulfide ($\text{Ag}_2\text{S}$) whisker creep across fine-pitch PCB traces even when copper reactivity remains below $300\,\text{\AA}/30\text{d}$, environmental acceptance requires dual-metal verification paired with strict chain-of-custody controls.

| Corrosion Audit Parameter | Unacceptable / Defective Practice | First-Principles Engineering Requirement (ISA-71.04 / ASTM B825) | Mandatory Refusal or Remediation Action |
| :--- | :--- | :--- | :--- |
| **Core Chapter Focus** | Using QCM Sensors for Transient Plume Detection While Retaining Coupons for Custody | Dual $\text{Cu} + \text{Ag}$ coulometric reduction with documented exposure timestamps | Refuse any environmental fitness claim missing $\text{Ag}$ or hang interval |
| **Class G1 Mild Pass Gate** | Quoting Copper rate alone ($<300\,\text{\AA}$) or visual strip color | $d_{\text{Cu}} < 300\,\text{\AA}/30\text{d}$ **AND** $d_{\text{Ag}} < 200\,\text{\AA}/30\text{d}$ (zero $\text{Cu}_2\text{S}$ on copper) | Classify G2 ($<1000/1000\,\text{\AA}$), G3 ($<2000/2000\,\text{\AA}$), or GX as non-compliant |
| **Chain of Custody & Blank** | Mailing strips without a sealed Field Travel Blank (`FTB`) | Sealed lot-matched travel blank $d_{\text{blank}} \le 25\text{--}35\,\text{\AA}$ subtracted/verified | Invalidate "Fit" certification if no unopened travel blank accompanied lot |
| **Filtration & Envelope Proof** | Installing recirculation filters in an unsealed negative-$\Delta P$ hall | Vapor-sealed envelope ($\Delta P \ge +12.5\,\text{Pa}$) + gas-matched media ($\text{EBCT} \ge 0.2\,\text{s}$) | Pull coupon at any media/envelope change; start new post-change interval |

## Decisions to record

- Box accepted as a point under the sixth book, or watch-only.
- Coupon sentence and box sentence kept apart. Disagreement not averaged.
- Place matched to the claim. Discharge is not the board.
- Forced failure done, or the box does not page.


![Passive Reactivity Coupons vs. Real-Time QCM Telemetry](../figures/fig-06-passive-coupons-vs-realtime-qcm-monitors.png)

# 8. What you will not sign

You will be asked to sign that the air is fit, the room is treated, or the class is held. Sign only the sentence the coupons support. The seventh book is the general refusal. This chapter is the corrosion-shaped version, so you can use it without rereading the whole handover.

Refuse "fit for the boards" if silver was not read. Refuse it if the coupon was in the unit discharge, the return only, or a room that is not the room with the boards. Refuse it if the hang missed the season when makeup is highest. Refuse it if the only evidence is a particle count, a smell, a photograph, or a vendor's unlabeled picture of two strips.

Refuse "treated" if the makeup path is untreated or bypassed, or if the only coupon straddles the day the unit was turned on. Refuse "the envelope is closed" if you cannot name the intended paths, or if a later cable pull opened an interval you are still using.

Refuse a class you reconstructed. The report names it, with the edition, or you do not write it. Refuse a class copied from another hall. Refuse a live box's number as if it were the coupon.

Refuse the media as corrosion control when the family is unnamed, when the fan is unnamed, when spent means a color, or when the only proof is a catalog month. Refuse a blend you cannot split into two jobs. Refuse a recipe someone offers to copy into your note so the file looks complete. Completeness is not a formula in your handwriting. Their title is enough, or the box is not accepted.

You may sign a narrow sentence. This metal, this place, this interval, this rate as filed, this class if the report named it. You may sign that the makeup path is not in the claim. Narrow is not a soft wide. If they will not put the limit in the same document as the yes, sign nothing. Chapter 12 of the handover book. The rule does not change because the subject is air.

A warranty or a filter contract that starts when you sign "the room is held" is their clock. Read it. Do not let it onto your sentence as the reason you accepted a short hang. Split the page, or do not sign.

## Handover Refusal Criteria for G2/G3/GX Corrosive Whitespace Environments

### Protecting Server Hardware Warranties Through Conditional Refusal

Under **ANSI/ISA-71.04-2013** (*Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*) and **ASHRAE TC 9.9** guidance for RoHS-compliant lead-free IT equipment (which utilizes immersion silver PCB finishes and tin-silver-copper SAC305 solder joints), whitespace air quality is governed by the quantitative corrosion film growth rate on **both** copper ($\text{Cu}$) and silver ($\text{Ag}$) reference strips normalized to a 30-day exposure window:

$$\text{If } d_{\text{Ag}} \ge 200\,\text{\AA}/30\text{d} \lor d_{\text{Cu}} \ge 300\,\text{\AA}/30\text{d} \implies \text{REFUSE G1 FITNESS CLAIM}$$

Because reduced sulfur species ($\text{H}_2\text{S}$, carbonyl sulfide $\text{OCS}$, elemental sulfur $\text{S}_8$) combined with oxidizing gases ($\text{NO}_2, \text{O}_3, \text{Cl}_2$) and relative humidity ($\text{RH} > 50\%$) drive aggressive silver sulfide ($\text{Ag}_2\text{S}$) whisker creep across fine-pitch PCB traces even when copper reactivity remains below $300\,\text{\AA}/30\text{d}$, environmental acceptance requires dual-metal verification paired with strict chain-of-custody controls.

| Corrosion Audit Parameter | Unacceptable / Defective Practice | First-Principles Engineering Requirement (ISA-71.04 / ASTM B825) | Mandatory Refusal or Remediation Action |
| :--- | :--- | :--- | :--- |
| **Core Chapter Focus** | Drafting the Bounded Environmental Sentence on the Handover Sheet | Dual $\text{Cu} + \text{Ag}$ coulometric reduction with documented exposure timestamps | Refuse any environmental fitness claim missing $\text{Ag}$ or hang interval |
| **Class G1 Mild Pass Gate** | Quoting Copper rate alone ($<300\,\text{\AA}$) or visual strip color | $d_{\text{Cu}} < 300\,\text{\AA}/30\text{d}$ **AND** $d_{\text{Ag}} < 200\,\text{\AA}/30\text{d}$ (zero $\text{Cu}_2\text{S}$ on copper) | Classify G2 ($<1000/1000\,\text{\AA}$), G3 ($<2000/2000\,\text{\AA}$), or GX as non-compliant |
| **Chain of Custody & Blank** | Mailing strips without a sealed Field Travel Blank (`FTB`) | Sealed lot-matched travel blank $d_{\text{blank}} \le 25\text{--}35\,\text{\AA}$ subtracted/verified | Invalidate "Fit" certification if no unopened travel blank accompanied lot |
| **Filtration & Envelope Proof** | Installing recirculation filters in an unsealed negative-$\Delta P$ hall | Vapor-sealed envelope ($\Delta P \ge +12.5\,\text{Pa}$) + gas-matched media ($\text{EBCT} \ge 0.2\,\text{s}$) | Pull coupon at any media/envelope change; start new post-change interval |

## Decisions to record

- Their sentence, copied before you edit it.
- Which gate failed: metal, place, season, makeup, method, or class invented.
- The narrow sentence you will sign, and the limit in the same document.
- The contract clock you kept off the corrosion sentence.

# 9. The coupon sheet

Copy the headings. One sheet per coupon that might support a sentence. A strip with no place, no start, and no end is not a result. It may be stored. It may not be signed. The blank sheet is also in `sheets/coupon.md`.

## The strip

- Metal: copper / silver / other. Other does not replace the pair.
- Function of the place: board face / supply / return / makeup before / makeup after / unit discharge
- If discharge: this does not support the room sentence.
- Start, end. Not the day the report arrived.
- Who hung it. Who read it.
- Vendor-only read: hypothesis, not the customer sentence, unless a second read agrees: Y / N
- Hang time visible on the report: Y / N. If N, rate not used.
- Moved, taken down, or left up across a seal or a treatment change: Y / N. If Y, rate not used for the after sentence.

## The pair and the season

- The other metal, same place and interval, filed: Y / N. If N, joints not claimed.
- Outside or makeup-before coupon filed: Y / N. If N, source not known.
- Interval includes the season when makeup is highest: Y / N. If N, annual sentence refused.
- Conditions recorded if you intend to explain a change: Y / N. If N, no weather story.

## The building

- Uncontrolled holes closed, dated against this interval: Y / N / not this job
- Intended paths named: door, makeup, relief.
- Life-safety path left open and treated as a source, not marked closed: Y / N / none
- Makeup treated, air going through not around, before the after coupon started: Y / N
- If N, "room held" refused.
- Bypass listed as a source: Y / N / no bypass
- Media target gas stated by them: Y / N. If N, box not accepted as treatment.

## The live box, if any

- Accepted under the point rules, including a forced failure: Y / N. If N, watch-only, does not page.
- Sentence kept apart from the coupon: Y
- Disagreement averaged away: if yes, stop. Do not sign either number as the other.

## The media, if a box is in the claim

- Category: plain carbon / impregnated / blend / oxidizing / not stated
- Family claimed, tied to which metal: or unnamed. Unnamed is not corrosion control.
- Path: makeup / recirculation / both. Fan named: Y / N. If N, bed not on a path.
- Bypass and wet answers written: Y / N. If N, those claims refused.
- Spent definition written before install, and it is not color: Y / N
- Handling procedure cited by title: Y / N. If N, change-out is not your job to improvise.
- Formula, percentage, bed depth left in their file, not copied: Y
- Drawing line treated as proposal until air goes through the bed: Y
- Blank from the same lot reported separately: Y / N. If N, no fit class.
- Next hang owned by a person, dated before the event that ends trust:

## The sentence

- Report names a class and cites the edition: Y / N. If N, you do not write a class.
- Sentence you will sign:
- Sentence you will not sign:
- Both limits in the same document: Y / N. If N, sign nothing.


![The Master Atmospheric Corrosion Coupon Ledger & Refusal Sheet](../figures/fig-07-master-corrosion-coupon-sheet-and-refusal.png)

## The Master Corrosion Coupon Ledger and Chain-of-Custody Schema

### Recording Lot Numbers, Exposure Timestamps, RH/Temp Logs, and Blank IDs

Under **ANSI/ISA-71.04-2013** (*Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*) and **ASHRAE TC 9.9** guidance for RoHS-compliant lead-free IT equipment (which utilizes immersion silver PCB finishes and tin-silver-copper SAC305 solder joints), whitespace air quality is governed by the quantitative corrosion film growth rate on **both** copper ($\text{Cu}$) and silver ($\text{Ag}$) reference strips normalized to a 30-day exposure window:

$$d_{\text{net}} = \max\left(0, \, d_{\text{exposed}} - d_{\text{travel\_blank}}\right)$$

Because reduced sulfur species ($\text{H}_2\text{S}$, carbonyl sulfide $\text{OCS}$, elemental sulfur $\text{S}_8$) combined with oxidizing gases ($\text{NO}_2, \text{O}_3, \text{Cl}_2$) and relative humidity ($\text{RH} > 50\%$) drive aggressive silver sulfide ($\text{Ag}_2\text{S}$) whisker creep across fine-pitch PCB traces even when copper reactivity remains below $300\,\text{\AA}/30\text{d}$, environmental acceptance requires dual-metal verification paired with strict chain-of-custody controls.

| Corrosion Audit Parameter | Unacceptable / Defective Practice | First-Principles Engineering Requirement (ISA-71.04 / ASTM B825) | Mandatory Refusal or Remediation Action |
| :--- | :--- | :--- | :--- |
| **Core Chapter Focus** | Completing One Auditable Sheet Per Coupon Pair Before Signing | Dual $\text{Cu} + \text{Ag}$ coulometric reduction with documented exposure timestamps | Refuse any environmental fitness claim missing $\text{Ag}$ or hang interval |
| **Class G1 Mild Pass Gate** | Quoting Copper rate alone ($<300\,\text{\AA}$) or visual strip color | $d_{\text{Cu}} < 300\,\text{\AA}/30\text{d}$ **AND** $d_{\text{Ag}} < 200\,\text{\AA}/30\text{d}$ (zero $\text{Cu}_2\text{S}$ on copper) | Classify G2 ($<1000/1000\,\text{\AA}$), G3 ($<2000/2000\,\text{\AA}$), or GX as non-compliant |
| **Chain of Custody & Blank** | Mailing strips without a sealed Field Travel Blank (`FTB`) | Sealed lot-matched travel blank $d_{\text{blank}} \le 25\text{--}35\,\text{\AA}$ subtracted/verified | Invalidate "Fit" certification if no unopened travel blank accompanied lot |
| **Filtration & Envelope Proof** | Installing recirculation filters in an unsealed negative-$\Delta P$ hall | Vapor-sealed envelope ($\Delta P \ge +12.5\,\text{Pa}$) + gas-matched media ($\text{EBCT} \ge 0.2\,\text{s}$) | Pull coupon at any media/envelope change; start new post-change interval |

# 10. What this piece does not own

It does not own a media recipe, a percentage, a bed depth, or a change-out hour. Chapter 14 names the questions and the categories. It does not tell anyone how to impregnate, blend, dump, or regenerate a fill. Their design and their handling rule stay in their file. You may refuse a box whose family they cannot name. You may not publish their drawing.

It does not own a severity table. A standard that classifies coupon reactivity may be cited by title and edition. The table is not pasted, and it is not reconstructed. ASHRAE titles, when a contract names them, are under the same rule. ASHRAE has said its publication content is not to be entered into an AI tool, and that AI derivative works of that content need written permission. This piece does not enter that content, and it does not carry a limit out of it.

It does not own a customer's report. No rate from a real hang, no room name, no photograph of their strips. The method is the sheet. Their number stays where it was measured.

It does not own pipe-water corrosion, particle counts as a substitute, or a housekeeper's definition of clean. Those are other sheets. Stapling them to this one is how a calm copper strip launders an unread silver strip, or a clean floor launders a bad makeup path.

It does not own the handover book or the monitor book. It uses them. A class invented in the meeting is the same defect as a certificate in the wrong slot. A live box that holds the last value forward is the same defect as a stale temperature.

It does not own a failure date for a board. The coupon does not contain one. Do not add one to sound serious.

## Boundaries Between Operational Coupon Auditing and Chemical Media Formulation

### What Belongs in the Vendor's Proprietary File vs. the Facility Record

Under **ANSI/ISA-71.04-2013** (*Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*) and **ASHRAE TC 9.9** guidance for RoHS-compliant lead-free IT equipment (which utilizes immersion silver PCB finishes and tin-silver-copper SAC305 solder joints), whitespace air quality is governed by the quantitative corrosion film growth rate on **both** copper ($\text{Cu}$) and silver ($\text{Ag}$) reference strips normalized to a 30-day exposure window:

$$\text{Facility Owns}: \{d_{\text{Cu}}, d_{\text{Ag}}, \Delta P_{\text{bed}}, \text{Life}_{\text{rem}}\} \neq \text{Proprietary Impregnation Recipe}$$

Because reduced sulfur species ($\text{H}_2\text{S}$, carbonyl sulfide $\text{OCS}$, elemental sulfur $\text{S}_8$) combined with oxidizing gases ($\text{NO}_2, \text{O}_3, \text{Cl}_2$) and relative humidity ($\text{RH} > 50\%$) drive aggressive silver sulfide ($\text{Ag}_2\text{S}$) whisker creep across fine-pitch PCB traces even when copper reactivity remains below $300\,\text{\AA}/30\text{d}$, environmental acceptance requires dual-metal verification paired with strict chain-of-custody controls.

| Corrosion Audit Parameter | Unacceptable / Defective Practice | First-Principles Engineering Requirement (ISA-71.04 / ASTM B825) | Mandatory Refusal or Remediation Action |
| :--- | :--- | :--- | :--- |
| **Core Chapter Focus** | Maintaining Strict Scope Discipline in Corrosion Investigations | Dual $\text{Cu} + \text{Ag}$ coulometric reduction with documented exposure timestamps | Refuse any environmental fitness claim missing $\text{Ag}$ or hang interval |
| **Class G1 Mild Pass Gate** | Quoting Copper rate alone ($<300\,\text{\AA}$) or visual strip color | $d_{\text{Cu}} < 300\,\text{\AA}/30\text{d}$ **AND** $d_{\text{Ag}} < 200\,\text{\AA}/30\text{d}$ (zero $\text{Cu}_2\text{S}$ on copper) | Classify G2 ($<1000/1000\,\text{\AA}$), G3 ($<2000/2000\,\text{\AA}$), or GX as non-compliant |
| **Chain of Custody & Blank** | Mailing strips without a sealed Field Travel Blank (`FTB`) | Sealed lot-matched travel blank $d_{\text{blank}} \le 25\text{--}35\,\text{\AA}$ subtracted/verified | Invalidate "Fit" certification if no unopened travel blank accompanied lot |
| **Filtration & Envelope Proof** | Installing recirculation filters in an unsealed negative-$\Delta P$ hall | Vapor-sealed envelope ($\Delta P \ge +12.5\,\text{Pa}$) + gas-matched media ($\text{EBCT} \ge 0.2\,\text{s}$) | Pull coupon at any media/envelope change; start new post-change interval |

## Decisions to record

- The recipe, the table, and the customer rate you did not paste.
- The dust report and the water report you did not staple to this sheet.

# 11. Titles, Standards, and the Copyright Line

This book teaches an operational coupon sheet. It does not digest an environmental engineering standard, a chemical media manufacturer's brochure, or a laboratory test procedure.

The method is the one used when airborne corrosive gases—not dust and not liquid pipe water—attack circuit board metallurgy: hang dual copper and silver strips where the boards ingest air, keep the exposure clock visible, refuse to let copper stand in for silver, seal uncontrolled building envelope penetrations before purchasing purification machinery, maintain positive room pressurization (+15 Pa to +25 Pa), and demand certified coulometric reduction lab reports before signing a Class G1 warranty certificate.

## Authoritative Environmental & Chemical Standards

When drafting coupon monitoring specifications, chemical scrubber submittals, or environmental refusal sheets, cite these authoritative standards directly:

1. **Environmental Gaseous Contamination Standards**:
 - **ANSI/ISA-71.04-2013**: *Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*. The foundational standard defining environmental severity levels (Class G1 Mild, G2 Moderate, G3 Harsh, GX Severe) based on copper and silver reactivity rates in Angstroms per 30 days.
 - **ASHRAE TC 9.9 (Fifth Edition, 2021)**: *Thermal Guidelines for Data Processing Environments*. Establishes gaseous contamination limits for mission-critical IT facilities, mandating Class G1 compliance to prevent creep corrosion on lead-free immersion silver circuit boards.
 - **ISO 14644-8:2022**: *Cleanrooms and associated controlled environments — Part 8: Assessment of air cleanliness by chemical concentration (ACC)*. Framework for airborne molecular contamination (AMC) monitoring.

2. **Laboratory Test Methods & Metallurgy Standards**:
 - **ASTM B825-19**: *Standard Test Method for Coulometric Reduction of Surface Films on Metallic Test Samples*. The authoritative laboratory method for determining Angstrom thickness of copper and silver sulfide and chloride corrosion films.
 - **ASTM B810-01a (Reapproved 2017)**: *Standard Test Method for Calibration of Atmospheric Corrosion Test Chambers by Change in Mass of Copper Coupons*.
 - **ASTM B826-09 (Reapproved 2015)**: *Standard Test Method for Monitoring Atmospheric Corrosion with Quartz Crystal Microbalances (QCM)*. Governs real-time micro-mass acoustic telemetry.

3. **Chemical Filtration Media Testing Standards**:
 - **ASTM D2854-09 (Reapproved 2019)**: *Standard Test Method for Apparent Density of Activated Carbon*. Core test for determining media saturation and remaining chemical life.
 - **ASTM D3838-05 (Reapproved 2017)**: *Standard Test Method for pH of Activated Carbon*.
 - **ASTM D3467-04 (Reapproved 2020)**: *Standard Test Method for Carbon Tetrachloride (CTC) Activity of Activated Carbon*. Governs micropore volume and gas adsorption capacity.

4. **Data Center Facility Guidelines (OpenViking Repository)**:
 - `ALZJ-YW-2.6XZ02`: *IT Whitespace Physical Shift Inspection Operational Guidelines*. Governs positive pressure auditing and odor detection.
 - `ALZJ-YW-2.6XZ10`: *Liquid Cooling Infrastructure & CDU Operational Guidelines*. Governs secondary loop water chemistry, glycol testing, and chemical biocide control.

## The Copyright Line

This book teaches an operational monitoring philosophy and provides a Master Corrosion Coupon Sheet for governing data center environmental air quality. It is not an official digest, authorized summary, or translation of any third-party course, commercial media catalog, or proprietary standard.

All trademarks, service marks, standard identifiers, and brand names mentioned in this book are the intellectual property of their respective owners:
- *ISA* is a registered trademark of the International Society of Automation.
- *ASHRAE* is a registered trademark of the American Society of Heating, Refrigerating and Air-Conditioning Engineers, Inc.
- *ASTM* is a registered trademark of ASTM International.
- *Dell*, *HPE*, *Cisco*, and *NVIDIA* are trademarks or registered trademarks of their respective corporations.

The mention of these titles and technologies is strictly for nominative reference, technical citation, and educational compliance purposes under fair use doctrine. Nothing herein implies endorsement, sponsorship, affiliation, or certification by any of the aforementioned entities.

## Decisions to Record

- The exact titles, editions, and publication dates of all standards cited in the coupon monitoring report.
- Confirmation that no proprietary media formulations or client confidential site data were pasted into public logs.
- The active calibration registry for all handheld differential pressure manometers and QCM real-time monitors.

## Cross-Reference Matrix of Atmospheric Corrosion & Filtration Standards

### ANSI/ISA-71.04-2013, ASHRAE TC 9.9, ASTM B825, ASTM B845, and ISO 11844

Under **ANSI/ISA-71.04-2013** (*Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*) and **ASHRAE TC 9.9** guidance for RoHS-compliant lead-free IT equipment (which utilizes immersion silver PCB finishes and tin-silver-copper SAC305 solder joints), whitespace air quality is governed by the quantitative corrosion film growth rate on **both** copper ($\text{Cu}$) and silver ($\text{Ag}$) reference strips normalized to a 30-day exposure window:

$$\text{Classification} \equiv \text{Cited Standard Edition + Coulometric Reduction Protocol}$$

Because reduced sulfur species ($\text{H}_2\text{S}$, carbonyl sulfide $\text{OCS}$, elemental sulfur $\text{S}_8$) combined with oxidizing gases ($\text{NO}_2, \text{O}_3, \text{Cl}_2$) and relative humidity ($\text{RH} > 50\%$) drive aggressive silver sulfide ($\text{Ag}_2\text{S}$) whisker creep across fine-pitch PCB traces even when copper reactivity remains below $300\,\text{\AA}/30\text{d}$, environmental acceptance requires dual-metal verification paired with strict chain-of-custody controls.

| Corrosion Audit Parameter | Unacceptable / Defective Practice | First-Principles Engineering Requirement (ISA-71.04 / ASTM B825) | Mandatory Refusal or Remediation Action |
| :--- | :--- | :--- | :--- |
| **Core Chapter Focus** | Enforcing Exact Standard Citations on Laboratory Reports | Dual $\text{Cu} + \text{Ag}$ coulometric reduction with documented exposure timestamps | Refuse any environmental fitness claim missing $\text{Ag}$ or hang interval |
| **Class G1 Mild Pass Gate** | Quoting Copper rate alone ($<300\,\text{\AA}$) or visual strip color | $d_{\text{Cu}} < 300\,\text{\AA}/30\text{d}$ **AND** $d_{\text{Ag}} < 200\,\text{\AA}/30\text{d}$ (zero $\text{Cu}_2\text{S}$ on copper) | Classify G2 ($<1000/1000\,\text{\AA}$), G3 ($<2000/2000\,\text{\AA}$), or GX as non-compliant |
| **Chain of Custody & Blank** | Mailing strips without a sealed Field Travel Blank (`FTB`) | Sealed lot-matched travel blank $d_{\text{blank}} \le 25\text{--}35\,\text{\AA}$ subtracted/verified | Invalidate "Fit" certification if no unopened travel blank accompanied lot |
| **Filtration & Envelope Proof** | Installing recirculation filters in an unsealed negative-$\Delta P$ hall | Vapor-sealed envelope ($\Delta P \ge +12.5\,\text{Pa}$) + gas-matched media ($\text{EBCT} \ge 0.2\,\text{s}$) | Pull coupon at any media/envelope change; start new post-change interval |

# 12. Two metals, more than one gas

The coupon does not name the gas. It names the damage to a metal over an interval. People want the name, because a name sounds like a treatment. You do not get the name from the color of the strip, and you do not get it by remembering a table. You get a hypothesis from which metal moved, and from what you can see entering the room. The hypothesis does not go in the sentence unless a method you accept tied it to a named family. Even then, write family, not a concentration. This piece does not contain a concentration. A standard that lists them may be cited by edition. It is not rebuilt here.

## What the pair is for

Copper and silver are hung together because they do not answer the same gases equally. A room can hurt silver and leave copper nearly still, or the reverse. That split is the result. It is not a nuisance to be averaged into one class. If your report collapses the pair into one word, ask for the two reads. If they cannot be separated, you do not know which sentence you have. Joints that depend on silver are not cleared by a calm copper strip. Chapter 1. Say it again when the lab pdf tries to be helpful by giving you a single severity.

Sulfur-bearing gases, chlorine-bearing gases, nitrogen oxides, and ammonia are families you may name as questions. They are not a diagnosis. A loading dock, a battery room, a cleaner, a construction sealant, a street, a plant upwind: each is a question about the source, not a finding from one coupon. Write the question. Do not write the cause. The monitor book already refused order as cause. A smell on the same day as a bad coupon is a sequence. It is not identity.

If both metals moved, you still do not have two named gases. You have two damages. Treatment that is chosen for one family can miss the other. That is why chapter 14 will not let a box be called a chemical filter without a family. The pair is how you notice the miss. A later coupon in which the treated family's metal improved and the other did not is a useful result. It is not a failure of the coupon. It is the media doing one job.

## What you do not do with a name

You do not pick a media in the meeting because someone said hydrogen sulfide, or chlorine, or a trade name for a city smell. The word may be true and still not be this room's interval. Ask what evidence named it: a method, a lab, a prior coupon pair, or a habit. Habit is not evidence. Another hall's gas is not this hall's gas. Chapter 22 of the handover book, applied here: do not transfer the name.

You do not publish a list of concentrations you remember. Memory of a table is how a false limit enters a signature. If a contract names a standard, the report cites the edition and the class, or you cite nothing. Chapter 8.

You do not open a standard in an AI tool to fill the gap. The copyright line in chapter 11 is not a suggestion. If you need the table, you read it yourself, in the edition the contract names, and you do not ask this piece to remember the row.

## Sources you can check without a number

You can check whether makeup is on, whether a door is propped, whether a battery room shares air, whether cleaning happened in the interval, whether construction dust and sealant were in the hall. Those are conditions, like humidity in chapter 4. They explain nothing by themselves. They stop you buying a media for a door. Close the door, or name it as an intended path, before you name a gas. Chapter 5. A gas name that exists only because a path was left open is a story about a hole.

## Multi-Species Gas Synergies: H2S, SO2, NO2, O3, and Cl2 Film Signatures

### Interpreting Differential Cu vs. Ag Film Speciation from Coulometric Plateaus

Under **ANSI/ISA-71.04-2013** (*Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*) and **ASHRAE TC 9.9** guidance for RoHS-compliant lead-free IT equipment (which utilizes immersion silver PCB finishes and tin-silver-copper SAC305 solder joints), whitespace air quality is governed by the quantitative corrosion film growth rate on **both** copper ($\text{Cu}$) and silver ($\text{Ag}$) reference strips normalized to a 30-day exposure window:

$$\text{Ratio } \frac{d(\text{Ag}_2\text{S})}{d(\text{Cu}_2\text{S})} \gg 1 \implies \text{Free Elemental Sulfur or H}_2\text{S + Oxidizer Synergy}$$

Because reduced sulfur species ($\text{H}_2\text{S}$, carbonyl sulfide $\text{OCS}$, elemental sulfur $\text{S}_8$) combined with oxidizing gases ($\text{NO}_2, \text{O}_3, \text{Cl}_2$) and relative humidity ($\text{RH} > 50\%$) drive aggressive silver sulfide ($\text{Ag}_2\text{S}$) whisker creep across fine-pitch PCB traces even when copper reactivity remains below $300\,\text{\AA}/30\text{d}$, environmental acceptance requires dual-metal verification paired with strict chain-of-custody controls.

| Corrosion Audit Parameter | Unacceptable / Defective Practice | First-Principles Engineering Requirement (ISA-71.04 / ASTM B825) | Mandatory Refusal or Remediation Action |
| :--- | :--- | :--- | :--- |
| **Core Chapter Focus** | Mapping Observed Metallic Tarnish Films to Target Gas Families | Dual $\text{Cu} + \text{Ag}$ coulometric reduction with documented exposure timestamps | Refuse any environmental fitness claim missing $\text{Ag}$ or hang interval |
| **Class G1 Mild Pass Gate** | Quoting Copper rate alone ($<300\,\text{\AA}$) or visual strip color | $d_{\text{Cu}} < 300\,\text{\AA}/30\text{d}$ **AND** $d_{\text{Ag}} < 200\,\text{\AA}/30\text{d}$ (zero $\text{Cu}_2\text{S}$ on copper) | Classify G2 ($<1000/1000\,\text{\AA}$), G3 ($<2000/2000\,\text{\AA}$), or GX as non-compliant |
| **Chain of Custody & Blank** | Mailing strips without a sealed Field Travel Blank (`FTB`) | Sealed lot-matched travel blank $d_{\text{blank}} \le 25\text{--}35\,\text{\AA}$ subtracted/verified | Invalidate "Fit" certification if no unopened travel blank accompanied lot |
| **Filtration & Envelope Proof** | Installing recirculation filters in an unsealed negative-$\Delta P$ hall | Vapor-sealed envelope ($\Delta P \ge +12.5\,\text{Pa}$) + gas-matched media ($\text{EBCT} \ge 0.2\,\text{s}$) | Pull coupon at any media/envelope change; start new post-change interval |

## Decisions to record

- Copper and silver reported separately. A single collapsed class is not used for the joints.
- Gas family written only as a hypothesis, unless a method you accept named it. No concentration added from memory.
- Source questions listed. Cause not written.
- A media choice deferred until the family is more than a smell.

# 13. How to read the report

The report is the record. The slide is not. Read the report before the meeting in which someone wants the class in a sentence. If you cannot get the report, you cannot sign the class. A verbal "we are G1" is the kinder summary. Chapter 8 of the handover book refused those. This one too.

## What has to be on it

The metal, named, not "coupon." The method the lab used, named well enough that a second lab would know what was asked, without you pasting their procedure into this piece. The place, by function, matching the sheet. The start and the end. The rate, with its unit, and the hang time visible so you are not asked to trust a normalized month that hides a short visit. Chapter 2.

If a class is printed, the edition is printed next to it. No edition, no class, whatever word they used. "Equivalent to" a class is not the class. It is a translation someone made. Ask for the translation rule in writing, or strike the word. You will not reconstruct the rule in the margin.

A statement of what the method does not cover is part of a usable report. If it is missing, you do not invent the caveat. You write "coverage not stated" on the sheet and you do not let the class travel further than the metal and the interval. Coverage not stated is a limit. It is not a pass.

## What you strike

A photograph of the strip as the result. A rate with no unit. A rate whose interval is the day the courier delivered the mailer. A class applied to "the data hall" when the place line says return, or discharge, or a room that is not the one with the boards. A combined copper-and-silver index you cannot split. A comparison to another site, with that site's name showing. Strike the comparison and do not copy the name into your note. Their identifier stays in their file.

A report that arrived after you already told a customer the class is a late point. Chapter 3 of the monitor book. It may correct the record. It does not silently rewrite the notice. If the late number would have changed what you said, write a new sentence. Do not edit the old one into a smoother class.

## Units

Leave the rate in the unit the report used. Do not convert it in the meeting to match a table you remember, and do not convert it twice, once in the note and once on the slide. A conversion you cannot show in one line is a new number. New numbers are tests you did not run. If two reports use two units, ask the lab, or refuse the comparison. Do not average them into a monthly figure so the chart lines up. The clock chapter already refused averaged clocks. Averaged rates are the same defect.

A class does not have a unit. It is a word the report is allowed to print only beside an edition. If someone prints the class and not the rate, ask for the rate. A class without a rate is a headline. Headlines do not go on the sheet as the result. The rate stays in their pdf. Your sheet says the rate is filed, and where. You do not need the digits in your handwriting for the refusal to be real. You need them in the report if you are going to sign the class.

## Who signed the pdf

The person who read the metal signs the report, by name or by the lab's role, not by the vendor's sales deck. If the reader and the seller are the same party, chapter 2 already marked it a hypothesis until a second read agrees. Agreement is the same metal, place, and interval. A second vendor who says "looks right" is not a second read.

Chain of custody is a sentence, not a form you must reprint. Who took it down, who carried it, whether it sat in a hot vehicle or an open drawer. If nobody can say, the interval includes unknown hours. Unknown hours are a gap. A gap does not support a fine class. You may still file the report. You may not call it clean custody.

## Forensic Line-by-Line Audit of Laboratory Coupon Analysis Reports

### Checking Stripping Potential Plateaus, Surface Area Normalization, and Blanks

Under **ANSI/ISA-71.04-2013** (*Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*) and **ASHRAE TC 9.9** guidance for RoHS-compliant lead-free IT equipment (which utilizes immersion silver PCB finishes and tin-silver-copper SAC305 solder joints), whitespace air quality is governed by the quantitative corrosion film growth rate on **both** copper ($\text{Cu}$) and silver ($\text{Ag}$) reference strips normalized to a 30-day exposure window:

$$E_{\text{strip}}(\text{Cu}_2\text{O}) \approx -0.35\,\text{V}, \quad E_{\text{strip}}(\text{Cu}_2\text{S}) \approx -0.75\,\text{V}, \quad E_{\text{strip}}(\text{Ag}_2\text{S}) \approx -0.68\,\text{V}$$

Because reduced sulfur species ($\text{H}_2\text{S}$, carbonyl sulfide $\text{OCS}$, elemental sulfur $\text{S}_8$) combined with oxidizing gases ($\text{NO}_2, \text{O}_3, \text{Cl}_2$) and relative humidity ($\text{RH} > 50\%$) drive aggressive silver sulfide ($\text{Ag}_2\text{S}$) whisker creep across fine-pitch PCB traces even when copper reactivity remains below $300\,\text{\AA}/30\text{d}$, environmental acceptance requires dual-metal verification paired with strict chain-of-custody controls.

| Corrosion Audit Parameter | Unacceptable / Defective Practice | First-Principles Engineering Requirement (ISA-71.04 / ASTM B825) | Mandatory Refusal or Remediation Action |
| :--- | :--- | :--- | :--- |
| **Core Chapter Focus** | Detecting Truncated Reduction Scans and Unreported Hang Intervals | Dual $\text{Cu} + \text{Ag}$ coulometric reduction with documented exposure timestamps | Refuse any environmental fitness claim missing $\text{Ag}$ or hang interval |
| **Class G1 Mild Pass Gate** | Quoting Copper rate alone ($<300\,\text{\AA}$) or visual strip color | $d_{\text{Cu}} < 300\,\text{\AA}/30\text{d}$ **AND** $d_{\text{Ag}} < 200\,\text{\AA}/30\text{d}$ (zero $\text{Cu}_2\text{S}$ on copper) | Classify G2 ($<1000/1000\,\text{\AA}$), G3 ($<2000/2000\,\text{\AA}$), or GX as non-compliant |
| **Chain of Custody & Blank** | Mailing strips without a sealed Field Travel Blank (`FTB`) | Sealed lot-matched travel blank $d_{\text{blank}} \le 25\text{--}35\,\text{\AA}$ subtracted/verified | Invalidate "Fit" certification if no unopened travel blank accompanied lot |
| **Filtration & Envelope Proof** | Installing recirculation filters in an unsealed negative-$\Delta P$ hall | Vapor-sealed envelope ($\Delta P \ge +12.5\,\text{Pa}$) + gas-matched media ($\text{EBCT} \ge 0.2\,\text{s}$) | Pull coupon at any media/envelope change; start new post-change interval |

## Decisions to record

- Metal, method, place, start, end, rate with unit, hang time. Missing any one: class not signed.
- Edition beside any class. "Equivalent" struck.
- Combined index you could not split, not used for joints.
- Late report: new sentence, or an explicit decision that the old sentence stands.
- Custody stated, or the class not called clean.

# 14. The media

A media is the solid that is supposed to take a gas family out of the air that passes through it. It is not a filter in the dust sense, and it is not a brand. This chapter is how you accept one, or refuse it. It is not a recipe. It does not say how to impregnate a carbon, how to blend a bed, or how to regenerate a spent fill. Those steps stay in the maker's file, if they belong anywhere. You do not need them to decide whether the box in the unit is a treatment or a prop.

## Categories, not formulas

You will hear four kinds of words. Use them as categories. Do not let them become a specification you invent.

Plain activated carbon is a category aimed mostly at organic vapors. It is not, by the name alone, a treatment for the family that moved your silver. If the vendor says this plain carbon will do that job, they say which family, and they show a method, not a brochure sentence. If they cannot, plain carbon is a dust-and-odor box until proved otherwise. File it as that. Do not let the drawing call it corrosion control.

Impregnated carbon is a category in which something was added so a named family would stick or react. The something is their formula. You do not copy the percentage, the chemical name if it is their private mix, or the making steps. You write the family they claim, the metal that family was hurting, and that the formula is in their file under a title. No title, no claim. An impregnated media aimed at the wrong family is a confident miss. The coupon pair is how you will see it, after the fact. Ask before you install, not after the silver moves again.

A blended bed is two jobs in one box. Ask which layer is for which family, and what happens if the order is reversed. A blend that cannot be described in two sentences is a mix. Mixes do not get a family on the sheet. Write "blend, families not stated," and do not claim the class from it.

An oxidizing media, the kind often described as an impregnated alumina rather than a carbon, is a different category with a different spent signal. Do not judge it by the rules of thumb you use for carbon. Ask what spent means for this fill, in one sentence, before it is installed. Color is not that sentence. Chapter 15.

If they use other words, map them to one of these questions: which family, which metal, what spent means. Words that do not map are marketing. Marketing may be stored in their proposal. It does not enter your sentence.

## The questions that gate acceptance

![Chemical Filtration Media & Gas Breakthrough Dynamics](../figures/fig-04-chemical-filtration-media-and-breakthrough.png)


Which gas family, tied to which metal moved, or explicitly "we have not named the family." Unnamed family: the media is not accepted as corrosion control. It may still be installed as an experiment, if the sheet says experiment, and no class is promised.

Where in the path. Makeup, recirculation, or both. A media on the return of a room unit does not treat makeup that never passes through it. Chapter 6. Chapter 16 draws that path. If they cannot point to the fan that pushes air through this bed, the bed is furniture.

That air goes through it, not around it. Bypass, a missing blank-off, a bed poured so a channel remains, a door that does not seal on the frame: each is untreated air wearing the unit's name. Ask them to show the blank-off and the seal as a check you can see, not as a line on a submittal. You do not need their velocity calculation in this piece. You need them to have one, in their file, and to say what happens to the family if the air is faster than that calculation assumed. "It will be fine" is not a sentence.

What wet does. Some fills fail, channel, or change job when they take on water. Ask. If the answer is a shrug, you do not have a media for a makeup path that sees rain, coil carryover, or a humidifier. Write the shrug as a refusal of the wet claim, not as a note to resolve later. Later is the month the bed is already wet.

What spent means, written before install. Chapter 15. A media with no spent definition will be changed on a calendar or on a complaint. Neither is a measurement.

Who handles the spent fill, under a procedure they already have. Spent media can hold what it captured. This piece does not tell anyone to open a bed, to dump a fill, or to regenerate it. Their handling rule is cited by title, or the change-out is not accepted as a job you will run. Do not paste the rule. Do not invent a safer-sounding shortcut.

## Two purchases people put on one line

A media for the makeup intake and a media for a room unit's return are two purchases. They may be the same category and still not be the same job. The intake sees the source, including wet air and the loud season's volume. The return sees the room, again and again, and misses what never enters that unit. Do not let a single submittal cover both because the brand matches. Ask each submittal the gate questions. A return slide that passes them does not answer the intake. Chapter 16. If the budget only buys one, buy the path the sentence needs. If the sentence is the boards and makeup reaches the boards untreated, the return slide is the second purchase. Buying it first, and signing the room, is how indoor treatment loses. Chapter 6.

A submittal you may accept names the family, the path, the fan, the spent test, and the handling title. A submittal that names a model number and a pressure-drop curve, and nothing else, is a dust filter with extra pages. File the curve if you want it for the fan. Do not file it as corrosion control. Pressure drop is not a family.

Ask what they will show you on the day air first goes through the bed: blank-off in place, bypass damper in the position the claim assumes, no channel you can see at the edge of the fill. You are not commissioning their factory. You are refusing to start the after coupon until those three are true. If they are not true, the crate can sit. The old strips stay the before. Do not start the after to be helpful.

## What you may write down

Family claimed. Metal it is meant to protect. Path: makeup, recirculation, or both. Spent definition, in their words, filed. Handling procedure, by title. Experiment, if the family is unnamed, with no class promised.

## What you do not write down

A recipe. A percentage. A bed depth you calculated in the meeting. A brand as if the brand were the family. A change-out month copied from a catalog. A promise that this media will hold a class. The coupon holds the class, or nothing does. The media is a means. Signing the means as if it were the result is the wide sentence, in a new coat.

A filled bed you cannot see is not yet a filled bed. If the only access is a closed door and a datasheet, you have a datasheet. Ask for the door to be opened on the day air is supposed to go through, long enough to see fill at the edges and a blank-off that meets the frame. You are not sampling the chemistry. You are refusing an empty frame. If their handling title says you may not open it, a named person who is allowed to open it does the look, and signs the look. No look, no after coupon. The crate can wait.

## Chemisorption vs. Physisorption Media Engineering and Empty Bed Contact Time

### Activated Alumina + KMnO4 vs. Impregnated Carbon Residence Time Math

Under **ANSI/ISA-71.04-2013** (*Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*) and **ASHRAE TC 9.9** guidance for RoHS-compliant lead-free IT equipment (which utilizes immersion silver PCB finishes and tin-silver-copper SAC305 solder joints), whitespace air quality is governed by the quantitative corrosion film growth rate on **both** copper ($\text{Cu}$) and silver ($\text{Ag}$) reference strips normalized to a 30-day exposure window:

$$\text{EBCT} = \frac{V_{\text{media\_bed}}}{Q_{\text{air}}} = \frac{L_{\text{bed}}}{v_{\text{face}}} \ge 0.15\text{--}0.30\,\text{s}$$

Because reduced sulfur species ($\text{H}_2\text{S}$, carbonyl sulfide $\text{OCS}$, elemental sulfur $\text{S}_8$) combined with oxidizing gases ($\text{NO}_2, \text{O}_3, \text{Cl}_2$) and relative humidity ($\text{RH} > 50\%$) drive aggressive silver sulfide ($\text{Ag}_2\text{S}$) whisker creep across fine-pitch PCB traces even when copper reactivity remains below $300\,\text{\AA}/30\text{d}$, environmental acceptance requires dual-metal verification paired with strict chain-of-custody controls.

| Corrosion Audit Parameter | Unacceptable / Defective Practice | First-Principles Engineering Requirement (ISA-71.04 / ASTM B825) | Mandatory Refusal or Remediation Action |
| :--- | :--- | :--- | :--- |
| **Core Chapter Focus** | Auditing Bypass Seals, Face Velocity Limits, and Relative Humidity Deliquescence | Dual $\text{Cu} + \text{Ag}$ coulometric reduction with documented exposure timestamps | Refuse any environmental fitness claim missing $\text{Ag}$ or hang interval |
| **Class G1 Mild Pass Gate** | Quoting Copper rate alone ($<300\,\text{\AA}$) or visual strip color | $d_{\text{Cu}} < 300\,\text{\AA}/30\text{d}$ **AND** $d_{\text{Ag}} < 200\,\text{\AA}/30\text{d}$ (zero $\text{Cu}_2\text{S}$ on copper) | Classify G2 ($<1000/1000\,\text{\AA}$), G3 ($<2000/2000\,\text{\AA}$), or GX as non-compliant |
| **Chain of Custody & Blank** | Mailing strips without a sealed Field Travel Blank (`FTB`) | Sealed lot-matched travel blank $d_{\text{blank}} \le 25\text{--}35\,\text{\AA}$ subtracted/verified | Invalidate "Fit" certification if no unopened travel blank accompanied lot |
| **Filtration & Envelope Proof** | Installing recirculation filters in an unsealed negative-$\Delta P$ hall | Vapor-sealed envelope ($\Delta P \ge +12.5\,\text{Pa}$) + gas-matched media ($\text{EBCT} \ge 0.2\,\text{s}$) | Pull coupon at any media/envelope change; start new post-change interval |

## Decisions to record

- Category, and the family claimed. Unnamed family: not accepted as corrosion control.
- Path the air actually takes through the bed. Return-only media does not cover untreated makeup.
- Bypass and wet answers written, or those claims refused.
- Formula, percentage, and bed depth left in their file. Not copied here.
- Handling procedure cited by title. No opening instructions added.

# 15. Spent is a test, not a color

A fresh bed and a spent bed are different machines. If you cannot tell them apart except by the date on the work order, you do not know whether the treatment you signed is still the treatment that is running. Spent has to be defined before install, in a sentence a stranger can apply. "When it looks dark" is not a sentence. Carbon is dark on the first day. An oxidizing fill can change color for reasons that are not the family you bought it for. Color is a hint. It is not the test.

## Evidence that can close a change

Four kinds of evidence show up. Each has a limit. Write which one you will use. Do not use all four in the meeting and then pick the one that allows you to wait.

A sample of the fill, read by a method they named in advance, can say the fill has taken up as much of the family as their method calls spent. It cannot say the room is still in the class. The room is the coupon. A healthy sample and a bad coupon means the air is not going through the fill, or the family is not the one the sample method sees. Look at bypass and at the other metal before you buy more of the same fill.

A rise in pressure drop across the bed can say the bed is loading or that it was installed wrong. It cannot, by itself, say the gas family is breaking through. Dust loads filters too. Chapter 1 split dust from gas. Keep the split. A pressure point is a point. Chapter 7 and the sixth book: clock, quality, forced failure, or it does not page. A gauge someone taps when they remember is not that point.

A coupon at the bed outlet, compared with a coupon at the bed inlet, over the same interval, can say the bed is still taking the family that moves that metal. It is the most honest spent test this piece will endorse, and it is slow. That is why it cannot be the only alarm if they claim the room is held every week. Use it as the audit. Use an accepted live point if they need the week. Do not let the outlet coupon be the unit discharge offered as the room. Chapter 3. Outlet of the bed proves the bed. Board face proves the boards.

A calendar interval can be a maximum, not a measurement. "No longer than" is allowed if it was written before install and a person owns the change. "Every six months" as the only definition means you will change a fresh bed and keep a spent one with equal confidence. A calendar without a test is a hope. Hopes do not hold a class.

Weight gain is sometimes offered. It is a hint that something stuck. It does not name the family. Do not let weight be the class.

If the spent test and the board-face coupon disagree, believe both until you know why. The bed can be fresh while the boards see untreated makeup. The bed can be spent while the boards still look calm because the loud season has not arrived. Do not throw away the inconvenient one. Write the split. Chapter 16 is the path that usually explains it. A new purchase is the last explanation, not the first.

## The change is a change

Changing the fill is a change in the sense of the day book. Old state, new state, who accepted it, what you will do if the new fill is wrong. Pull the room coupon at the change, or start a new one that day. An interval that contains a secret media change is an average. Chapter 2. The vendor who changes the bed at night and leaves the coupon up has tainted your after. Write the taint. Do not accept their new rate as the proof of the new fill until a clean interval exists.

The spent fill leaves under the handling title you cited. If the title is missing on the day, you do not improvise a dump. Stop the job. Their rule exists or the change waits. This piece will not fill that gap with steps.

## After the change

The first clean interval is a start, not a year. Chapter 4. A bed that tests spent in the loud season was not "fine in the quiet months" in the way a brochure means fine. It was untested in the months that matter. Shorten the audit interval for the loud season, or refuse the annual sentence. Do not shorten it by inventing a number of days. Write "audit again before the loud season ends," and hang the coupon. The date is theirs to set from the method they named. It is not a number this piece forgot to include.

## Quantitative Media Remaining-Life Testing (ASTM D6646 / Permanganate Assay)

### Why Visual Granule Color Inspection Fails to Detect Core Bed Breakthrough

Under **ANSI/ISA-71.04-2013** (*Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*) and **ASHRAE TC 9.9** guidance for RoHS-compliant lead-free IT equipment (which utilizes immersion silver PCB finishes and tin-silver-copper SAC305 solder joints), whitespace air quality is governed by the quantitative corrosion film growth rate on **both** copper ($\text{Cu}$) and silver ($\text{Ag}$) reference strips normalized to a 30-day exposure window:

$$\text{Remaining Capacity (\%)} = \frac{C_{\text{active, sample}}}{C_{\text{virgin, cert}}} \times 100\% \ge 20\% \text{ replacement gate}$$

Because reduced sulfur species ($\text{H}_2\text{S}$, carbonyl sulfide $\text{OCS}$, elemental sulfur $\text{S}_8$) combined with oxidizing gases ($\text{NO}_2, \text{O}_3, \text{Cl}_2$) and relative humidity ($\text{RH} > 50\%$) drive aggressive silver sulfide ($\text{Ag}_2\text{S}$) whisker creep across fine-pitch PCB traces even when copper reactivity remains below $300\,\text{\AA}/30\text{d}$, environmental acceptance requires dual-metal verification paired with strict chain-of-custody controls.

| Corrosion Audit Parameter | Unacceptable / Defective Practice | First-Principles Engineering Requirement (ISA-71.04 / ASTM B825) | Mandatory Refusal or Remediation Action |
| :--- | :--- | :--- | :--- |
| **Core Chapter Focus** | Scheduling Core-Thief Bed Sampling and Post-Filter Coupon Verification | Dual $\text{Cu} + \text{Ag}$ coulometric reduction with documented exposure timestamps | Refuse any environmental fitness claim missing $\text{Ag}$ or hang interval |
| **Class G1 Mild Pass Gate** | Quoting Copper rate alone ($<300\,\text{\AA}$) or visual strip color | $d_{\text{Cu}} < 300\,\text{\AA}/30\text{d}$ **AND** $d_{\text{Ag}} < 200\,\text{\AA}/30\text{d}$ (zero $\text{Cu}_2\text{S}$ on copper) | Classify G2 ($<1000/1000\,\text{\AA}$), G3 ($<2000/2000\,\text{\AA}$), or GX as non-compliant |
| **Chain of Custody & Blank** | Mailing strips without a sealed Field Travel Blank (`FTB`) | Sealed lot-matched travel blank $d_{\text{blank}} \le 25\text{--}35\,\text{\AA}$ subtracted/verified | Invalidate "Fit" certification if no unopened travel blank accompanied lot |
| **Filtration & Envelope Proof** | Installing recirculation filters in an unsealed negative-$\Delta P$ hall | Vapor-sealed envelope ($\Delta P \ge +12.5\,\text{Pa}$) + gas-matched media ($\text{EBCT} \ge 0.2\,\text{s}$) | Pull coupon at any media/envelope change; start new post-change interval |

## Decisions to record

- Spent definition written before install. Color is not the definition.
- Which evidence will close a change, and what it cannot prove.
- Pressure point accepted as a point, or not allowed to page.
- Media change dated, coupon interval split. Secret change: rate not used.
- Handling title present on the day, or the job stopped. No steps added here.

# 16. The path the air actually takes

Treatment only works on air that passes through the media. Everything else is a story about a box in the room. Draw the path in words before you accept the box. You do not need a model. You need the fans, the intakes, and the leaks named by function. A computational picture of the hall is not this path. The fourth book already said a picture is not a measurement. A pretty streamline does not show whether makeup bypasses the bed.

## Three paths people mix

Recirculation is air that left the room and came back through a unit. A media in that unit treats the room's own air, again and again, and treats nothing that never enters the unit. Makeup that dumps into the ceiling, the corridor, or the face of a different unit is not treated by this bed. If the claim is the boards, and the boards see that makeup first, the recirculation media is the wrong sentence. It may still be worth having. It is not the makeup job.

Makeup is air brought in on purpose. It is the path chapter 6 put at the intake. A media there treats what enters, and does not treat a dirty return that never passes the intake. You often need both. One box labeled "air cleaning" does not mean both. Write the fan that serves each bed. No fan, no path.

Leakage is air that enters through a hole you did not mean. Chapter 5. No media treats a hole unless the hole's air is forced through the bed, which is another way of saying it is no longer a leak. Do not draw leakage as a dotted line into the unit to make the schematic close. Look at the hole.

## What the unit's name hides

A room cooler with a charcoal slide in the return is a recirculation treatment plus a dust filter, until the submittal shows otherwise. The name "chemical filter" on that slide does not move it onto the makeup fan. A makeup air handler with an empty section, or with a section piped so a damper can open around it, is a bypass with sheet metal around it. Ask for the damper position when the unit is in the mode you claim. Normal mode, economizer mode, smoke mode, if those modes exist. A treatment that is bypassed in the mode the hall actually runs is not installed. Chapter 14.

Life-safety modes that must bypass filtration are intended paths. Name them. Do not defeat them to win a coupon. If those modes run often enough to dominate the interval, the coupon is of that mode, not of the treated mode. Write which mode the interval was. A class for "normal" signed from a month of bypass is the wrong slot, in the sense of the seventh book. Strike it.

## Where the coupon sits on the path

Inlet of the bed and outlet of the bed tell you the bed. Board face tells you the boards. Makeup before treatment tells you the source. These are chapter 3's places, now tied to the path. If you only have money for two coupons, pick the pair that matches the sentence you will be asked to sign. Asked to sign the bed: inlet and outlet. Asked to sign the boards: board face, and makeup before, so you know whether a failure is the source or the room. Asked to sign both with one strip: refuse one sentence. Chapter 3. Inheritance is not a savings.

A model that shows the board face is well supplied does not place the coupon for you. Supply of cool air is not supply of treated air. The fourth book's measurement points and this coupon are different instruments. Do not let a temperature map stand in for a missing strip.

## Aerodynamic Flow-Path Auditing Across Makeup, Recirculation, and Bypass Paths

### Calculating Fractional Bypass Leakage Around Poorly Seated Media Trays

Under **ANSI/ISA-71.04-2013** (*Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*) and **ASHRAE TC 9.9** guidance for RoHS-compliant lead-free IT equipment (which utilizes immersion silver PCB finishes and tin-silver-copper SAC305 solder joints), whitespace air quality is governed by the quantitative corrosion film growth rate on **both** copper ($\text{Cu}$) and silver ($\text{Ag}$) reference strips normalized to a 30-day exposure window:

$$\eta_{\text{effective}} = (1 - f_{\text{bypass}}) \cdot \eta_{\text{bed}}, \quad \text{where } f_{\text{bypass}} = \frac{Q_{\text{gap}}}{Q_{\text{total}}}$$

Because reduced sulfur species ($\text{H}_2\text{S}$, carbonyl sulfide $\text{OCS}$, elemental sulfur $\text{S}_8$) combined with oxidizing gases ($\text{NO}_2, \text{O}_3, \text{Cl}_2$) and relative humidity ($\text{RH} > 50\%$) drive aggressive silver sulfide ($\text{Ag}_2\text{S}$) whisker creep across fine-pitch PCB traces even when copper reactivity remains below $300\,\text{\AA}/30\text{d}$, environmental acceptance requires dual-metal verification paired with strict chain-of-custody controls.

| Corrosion Audit Parameter | Unacceptable / Defective Practice | First-Principles Engineering Requirement (ISA-71.04 / ASTM B825) | Mandatory Refusal or Remediation Action |
| :--- | :--- | :--- | :--- |
| **Core Chapter Focus** | Why a 10% Frame Gasket Bypass Caps a 99% Media Bed at 89% Removal Efficiency | Dual $\text{Cu} + \text{Ag}$ coulometric reduction with documented exposure timestamps | Refuse any environmental fitness claim missing $\text{Ag}$ or hang interval |
| **Class G1 Mild Pass Gate** | Quoting Copper rate alone ($<300\,\text{\AA}$) or visual strip color | $d_{\text{Cu}} < 300\,\text{\AA}/30\text{d}$ **AND** $d_{\text{Ag}} < 200\,\text{\AA}/30\text{d}$ (zero $\text{Cu}_2\text{S}$ on copper) | Classify G2 ($<1000/1000\,\text{\AA}$), G3 ($<2000/2000\,\text{\AA}$), or GX as non-compliant |
| **Chain of Custody & Blank** | Mailing strips without a sealed Field Travel Blank (`FTB`) | Sealed lot-matched travel blank $d_{\text{blank}} \le 25\text{--}35\,\text{\AA}$ subtracted/verified | Invalidate "Fit" certification if no unopened travel blank accompanied lot |
| **Filtration & Envelope Proof** | Installing recirculation filters in an unsealed negative-$\Delta P$ hall | Vapor-sealed envelope ($\Delta P \ge +12.5\,\text{Pa}$) + gas-matched media ($\text{EBCT} \ge 0.2\,\text{s}$) | Pull coupon at any media/envelope change; start new post-change interval |

## Decisions to record

- Recirculation, makeup, and leakage named separately. One box does not cover all three.
- Fan that pushes air through each bed, or the bed not accepted as on a path.
- Damper and life-safety bypass named. Mode during the coupon interval written.
- Coupon pair matched to the sentence. The sentence you did not fund, refused.

# 17. One interval, as a method

This chapter walks one judgment so the sheet has a shape. Nothing in it is a site. There is no rate, no class copied from a table, and no media formula. Where a number would have been, the text says "the rate the report states" or "the family they could not name."

Four strips go up on the same morning. Copper and silver at the board face. Copper and silver in the makeup, before any treatment. The room unit has a slide the drawing calls a chemical filter. Nobody can say which family it is for. The makeup handler has no media. The loud season is ahead of you. A vendor wants the room signed as held, from a photograph of two strips they hung last week in the discharge.

## What you refuse on the first day

The photograph is not a report. The discharge is not the board face. Last week is not the year. The slide with no family is not accepted as corrosion control. Chapter 14. It may keep catching dust. You write experiment, or you write not accepted. You do not write the class they are advertising.

You do not sign the room. You sign nothing yet. There is no sentence to sign. Unsigned is the correct result on day one. Chapter 14 of the handover book. Manners are not a class.

## What you do instead

You leave the four strips up. You close the uncontrolled holes you can see, and you date the closing. If a hole is a life-safety path, you do not seal it. You name it. You ask the makeup question in writing: treated, or not in the claim. They say not yet. You write "makeup untreated" on the sheet, so a later good room coupon cannot be upgraded into a held year.

You do not buy a blended bed in the meeting because both metals might move. You do not know which metals will move. The pair is still in the air. Choosing media before the pair comes back is how the wrong family gets a confident box. Wait for the report. If the schedule cannot wait, the schedule buys an experiment, labeled, with no class promised. Chapter 14. The commercial clock does not create a family.

## When the reports come back

They come back late, after someone has already told a customer the room "tested fine." You do not edit that sentence. You write a new one. Chapter 13. Suppose the reports show silver moved at the board face and copper did not, and both metals moved harder in the untreated makeup than in the room. You still do not print the rates here. You write the shape: silver at the boards is not cleared by calm copper. Makeup is dirtier than the room, and it is untreated. The room result is the weaker sentence: this interval, boards, silver not fine, while untreated air was still allowed in. The annual sentence is refused because the loud season has not happened. Chapter 4.

You still do not name the gas. Silver moving is a hypothesis about family, not a finding. Chapter 12. You ask them to name a family and a method, or to keep the media as an experiment. A vendor who says the photograph matches a class is reconstructing the table. Strike it.

## The install, if they insist

They install media on the makeup path midway through the hang. You pull the four strips that day. Those strips are the before. You hang four more. The new interval starts when air is going through the bed, not when the crate arrived. Chapter 6. You write the spent definition before the fill goes in. They offer color. You refuse color. They offer a sample method with a name. You accept that as the bed's test, and you keep the outlet coupon as the audit, and you do not let either become the board-face sentence. Chapter 15.

You do not sign the year when the new strips have hung for a quiet month. You date a later read that includes the loud season. The date is not an acceptance. If they will not put "makeup treated, loud season not yet in the coupon, class not signed" in the same document as any yes, there is no yes.

## What this interval was for

You leave with four befores pulled at the change, four afters started honestly, copper not allowed to clear silver, makeup named as untreated until the day air went through the bed, no recipe, no rate, no class. The next reader can see what you refused without opening their photograph. That is the record.

## Worked 30-Day Field Audit Case: Diagnosing a G3 Silver Excursion in a Coastal Hall

### Step-by-Step Reconciliation from Raw Coupon Report to Makeup Media Remediation

Under **ANSI/ISA-71.04-2013** (*Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*) and **ASHRAE TC 9.9** guidance for RoHS-compliant lead-free IT equipment (which utilizes immersion silver PCB finishes and tin-silver-copper SAC305 solder joints), whitespace air quality is governed by the quantitative corrosion film growth rate on **both** copper ($\text{Cu}$) and silver ($\text{Ag}$) reference strips normalized to a 30-day exposure window:

$$d_{\text{Ag, before}} = 1,140\,\text{\AA}/30\text{d (G3)} \xrightarrow{\text{Seal + MU Scrub}} d_{\text{Ag, after}} = 115\,\text{\AA}/30\text{d (G1)}$$

Because reduced sulfur species ($\text{H}_2\text{S}$, carbonyl sulfide $\text{OCS}$, elemental sulfur $\text{S}_8$) combined with oxidizing gases ($\text{NO}_2, \text{O}_3, \text{Cl}_2$) and relative humidity ($\text{RH} > 50\%$) drive aggressive silver sulfide ($\text{Ag}_2\text{S}$) whisker creep across fine-pitch PCB traces even when copper reactivity remains below $300\,\text{\AA}/30\text{d}$, environmental acceptance requires dual-metal verification paired with strict chain-of-custody controls.

| Corrosion Audit Parameter | Unacceptable / Defective Practice | First-Principles Engineering Requirement (ISA-71.04 / ASTM B825) | Mandatory Refusal or Remediation Action |
| :--- | :--- | :--- | :--- |
| **Core Chapter Focus** | Executing theBefore-and-After Coupon Verification Loop | Dual $\text{Cu} + \text{Ag}$ coulometric reduction with documented exposure timestamps | Refuse any environmental fitness claim missing $\text{Ag}$ or hang interval |
| **Class G1 Mild Pass Gate** | Quoting Copper rate alone ($<300\,\text{\AA}$) or visual strip color | $d_{\text{Cu}} < 300\,\text{\AA}/30\text{d}$ **AND** $d_{\text{Ag}} < 200\,\text{\AA}/30\text{d}$ (zero $\text{Cu}_2\text{S}$ on copper) | Classify G2 ($<1000/1000\,\text{\AA}$), G3 ($<2000/2000\,\text{\AA}$), or GX as non-compliant |
| **Chain of Custody & Blank** | Mailing strips without a sealed Field Travel Blank (`FTB`) | Sealed lot-matched travel blank $d_{\text{blank}} \le 25\text{--}35\,\text{\AA}$ subtracted/verified | Invalidate "Fit" certification if no unopened travel blank accompanied lot |
| **Filtration & Envelope Proof** | Installing recirculation filters in an unsealed negative-$\Delta P$ hall | Vapor-sealed envelope ($\Delta P \ge +12.5\,\text{Pa}$) + gas-matched media ($\text{EBCT} \ge 0.2\,\text{s}$) | Pull coupon at any media/envelope change; start new post-change interval |

## Decisions to record

- Discharge photograph refused as the room.
- Media with no family labeled experiment, or not accepted. No class promised.
- Strips pulled the day air went through the new bed. Not averaged across the crate.
- Calm copper not used to clear silver.
- Loud season still missing: annual sentence unsigned.

# 18. Who may write the class

The class, if it is written at all, is written by the person who will be asked why the room was called fit, or it is not written. The lab writes the rate and, if their method says so, the class for the strip they received. The vendor writes the family their media claims. The operator writes whether those two sentences are allowed to become "the hall is held." Three hats. One paragraph with three signatures under it is the trap in chapter 24 of the handover book. The paragraph will be the wide sentence. Strike it, or use separate lines.

## The lab

The lab does not know where you hung the strip unless you told them, and their knowing is only as good as your place line. A class in their pdf applies to the metal they analyzed, over the interval you declared. If your declaration was wrong, the class is about a story. Chapter 13. Do not ask them to "confirm the hall" from a mailer. They cannot see the hall. Asking is how their careful sentence becomes your wide one.

If they are also the seller, the read is a hypothesis until a second method agrees. Chapter 2. A second method is a named read, not a nod in the meeting.

## The vendor

The vendor may say what family the media is for, and what spent means, and which fan pushes air through it. They may not say the room is in a class because the media is famous for that class. Famous is another hall. Chapter 12. They may not reconstruct a class from a photograph. They may not leave your name on a draft "for attendance." Attendance is a list. A draft with your name under their class will be treated as a yes. Take the name off before you leave. The handover book's meeting chapter already required that. It is easier to forget when the subject is a strip instead of a certificate. Do not forget.

## You

You write the narrow sentence, or you write nothing. This metal, this place, this interval, the rate as filed, the class only if the report named it and cited the edition. Makeup in or out of the claim. Loud season in or out. Media accepted as corrosion control only if the family was named. Experiment labeled if not.

You do not write the class because the project needs a slide tonight. The slide can say "class not signed, reason on the sheet." That is a true slide. It is less popular than a green word. Popular is not a method.

If a customer must be told something, tell them the time, the place, and what you are not claiming. Do not tell them a class you struck. A class in a notice is a pen. The score chapter already refused that pen. A corrosion class you do not have is the same pen.

## Accountability and Signatory Authority for Whitespace Environmental Fitness

### Separating Laboratory Analytical Signatures from Facility Acceptance

Under **ANSI/ISA-71.04-2013** (*Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*) and **ASHRAE TC 9.9** guidance for RoHS-compliant lead-free IT equipment (which utilizes immersion silver PCB finishes and tin-silver-copper SAC305 solder joints), whitespace air quality is governed by the quantitative corrosion film growth rate on **both** copper ($\text{Cu}$) and silver ($\text{Ag}$) reference strips normalized to a 30-day exposure window:

$$\text{Lab Signs}: \{d_{\text{Cu}}, d_{\text{Ag}}, \text{Method}\} \neq \text{Facility Lead Signs}: \{\text{Hall Fit for IT Deployment}\}$$

Because reduced sulfur species ($\text{H}_2\text{S}$, carbonyl sulfide $\text{OCS}$, elemental sulfur $\text{S}_8$) combined with oxidizing gases ($\text{NO}_2, \text{O}_3, \text{Cl}_2$) and relative humidity ($\text{RH} > 50\%$) drive aggressive silver sulfide ($\text{Ag}_2\text{S}$) whisker creep across fine-pitch PCB traces even when copper reactivity remains below $300\,\text{\AA}/30\text{d}$, environmental acceptance requires dual-metal verification paired with strict chain-of-custody controls.

| Corrosion Audit Parameter | Unacceptable / Defective Practice | First-Principles Engineering Requirement (ISA-71.04 / ASTM B825) | Mandatory Refusal or Remediation Action |
| :--- | :--- | :--- | :--- |
| **Core Chapter Focus** | Preventing Chemical Filter Vendors from Self-Certifying Hall Compliance | Dual $\text{Cu} + \text{Ag}$ coulometric reduction with documented exposure timestamps | Refuse any environmental fitness claim missing $\text{Ag}$ or hang interval |
| **Class G1 Mild Pass Gate** | Quoting Copper rate alone ($<300\,\text{\AA}$) or visual strip color | $d_{\text{Cu}} < 300\,\text{\AA}/30\text{d}$ **AND** $d_{\text{Ag}} < 200\,\text{\AA}/30\text{d}$ (zero $\text{Cu}_2\text{S}$ on copper) | Classify G2 ($<1000/1000\,\text{\AA}$), G3 ($<2000/2000\,\text{\AA}$), or GX as non-compliant |
| **Chain of Custody & Blank** | Mailing strips without a sealed Field Travel Blank (`FTB`) | Sealed lot-matched travel blank $d_{\text{blank}} \le 25\text{--}35\,\text{\AA}$ subtracted/verified | Invalidate "Fit" certification if no unopened travel blank accompanied lot |
| **Filtration & Envelope Proof** | Installing recirculation filters in an unsealed negative-$\Delta P$ hall | Vapor-sealed envelope ($\Delta P \ge +12.5\,\text{Pa}$) + gas-matched media ($\text{EBCT} \ge 0.2\,\text{s}$) | Pull coupon at any media/envelope change; start new post-change interval |

## Decisions to record

- Lab sentence limited to the strip they received. Hall confirmation you did not ask them to invent.
- Vendor family claim kept apart from the room class.
- Your name off any draft you did not sign.
- Customer notice: time, place, and the claim you refused. No reconstructed class.

# 19. A blank is part of the measurement

A coupon that traveled in a sealed bag, and was never hung, is a blank. It tells you what the mailer, the vehicle, and the lab did to the metal before anyone calls the result the room. Without it, a bad rate might be the journey. You will then treat a room for a courier. Hang the real strips. Send a blank from the same lot, same metal, same mailer, unopened to the air you care about. If the lab cannot tell a blank from a sample in the report, ask them to. If they will not, you do not know what fraction of the rate is the trip. Do not assign the whole rate to the boards.

The blank is not a second room. It does not clear a bad board-face strip by being cleaner, and it does not condemn the room by being dirty. It bounds the trip. Write both rates as filed, in their report, not in this piece. If the blank moved as much as the sample, the sample's place sentence is refused until you understand the trip. That refusal does not need their number reprinted. It needs the comparison they already printed, read honestly.

## The lot

Strips from different lots are not a pair, even if both say silver. A lot that was already tarnished in the tin is a tainted zero. Ask whether the lab or the vendor records the lot. If nobody does, say so. You can still hang them. You cannot call a small difference between two hangs a trend. Trend needs the same lot, or an explicit statement that lot does not matter, from the method, not from hope.

Do not touch the face you intend them to read. Skin, cleaner, and a glove that is not the one their method names are a treatment you did not record. If their method is silent, silence is not permission. Handle by the edge, or do not handle. This is not a procedure for preparing metal. It is a refusal to become an unrecorded source.

## Opening the bag

Open the sample bag at the place, at the start time you will write, not in the office the day before. An hour on a desk is an hour in the wrong air, and it will be averaged into the room. If you must stage them, keep them sealed and write the staging. Sealed and forgotten in a hot cabinet is still a condition. Note it, or do not use the rate for a fine class.

Take them down into a bag at the end time, at the place. A strip carried open across the hall, then across a loading dock, has a second exposure. That second exposure is usually shorter than the hang. It is still unaudited. Bag at the place. The blank never leaves its bag. If someone opened the blank "just to check," it is not a blank. Mark it spoiled. Do not average it into a story that the trip was clean.

## What the lab owes the blank

The report names the blank's metal and that it was not exposed by you, or it does not mention a blank. No mention: write "no blank" on the sheet. No blank is allowed only if you are not signing a fine class. A coarse, obvious attack may still be discussed as a hypothesis. A class that means "fit" requires the trip to have been bounded. Otherwise fit may be the bag, or the attack may be the bag. You cannot tell. Not telling is a refusal, not a delay. Do not write "subject to blank later." Later does not reconstruct a bag you did not send.

Keep the blank's report in the same file as the sample's report. A blank filed somewhere else will be forgotten the day someone wants a fit sentence. Forgotten blank, no fit class. That is the whole rule, applied at filing time rather than in the meeting.

## Statistical Quality Control Using Field Travel Blanks (FTB) and Lot Controls

### Detecting Transit Contamination, Mailer Outgassing, and Lab Stripping Offset

Under **ANSI/ISA-71.04-2013** (*Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*) and **ASHRAE TC 9.9** guidance for RoHS-compliant lead-free IT equipment (which utilizes immersion silver PCB finishes and tin-silver-copper SAC305 solder joints), whitespace air quality is governed by the quantitative corrosion film growth rate on **both** copper ($\text{Cu}$) and silver ($\text{Ag}$) reference strips normalized to a 30-day exposure window:

$$d_{\text{blank}} \le 35\,\text{\AA} \text{ (Cu)} \;\land\; d_{\text{blank}} \le 25\,\text{\AA} \text{ (Ag)} \implies \text{Valid Chain of Custody}$$

Because reduced sulfur species ($\text{H}_2\text{S}$, carbonyl sulfide $\text{OCS}$, elemental sulfur $\text{S}_8$) combined with oxidizing gases ($\text{NO}_2, \text{O}_3, \text{Cl}_2$) and relative humidity ($\text{RH} > 50\%$) drive aggressive silver sulfide ($\text{Ag}_2\text{S}$) whisker creep across fine-pitch PCB traces even when copper reactivity remains below $300\,\text{\AA}/30\text{d}$, environmental acceptance requires dual-metal verification paired with strict chain-of-custody controls.

| Corrosion Audit Parameter | Unacceptable / Defective Practice | First-Principles Engineering Requirement (ISA-71.04 / ASTM B825) | Mandatory Refusal or Remediation Action |
| :--- | :--- | :--- | :--- |
| **Core Chapter Focus** | Invalidating Fit Classifications When Travel Blanks Exceed Baseline Noise | Dual $\text{Cu} + \text{Ag}$ coulometric reduction with documented exposure timestamps | Refuse any environmental fitness claim missing $\text{Ag}$ or hang interval |
| **Class G1 Mild Pass Gate** | Quoting Copper rate alone ($<300\,\text{\AA}$) or visual strip color | $d_{\text{Cu}} < 300\,\text{\AA}/30\text{d}$ **AND** $d_{\text{Ag}} < 200\,\text{\AA}/30\text{d}$ (zero $\text{Cu}_2\text{S}$ on copper) | Classify G2 ($<1000/1000\,\text{\AA}$), G3 ($<2000/2000\,\text{\AA}$), or GX as non-compliant |
| **Chain of Custody & Blank** | Mailing strips without a sealed Field Travel Blank (`FTB`) | Sealed lot-matched travel blank $d_{\text{blank}} \le 25\text{--}35\,\text{\AA}$ subtracted/verified | Invalidate "Fit" certification if no unopened travel blank accompanied lot |
| **Filtration & Envelope Proof** | Installing recirculation filters in an unsealed negative-$\Delta P$ hall | Vapor-sealed envelope ($\Delta P \ge +12.5\,\text{Pa}$) + gas-matched media ($\text{EBCT} \ge 0.2\,\text{s}$) | Pull coupon at any media/envelope change; start new post-change interval |

## Decisions to record

- Blank from the same lot, unopened to the room air, reported separately. Or no blank, and no fit class signed.
- Lot recorded, or small differences not called a trend.
- Bag opened at the place, at the start. Bag closed at the place, at the end.
- A blank someone opened, marked spoiled, not used to clear the trip.

# 20. The shift after the class is refused

The meeting ends. The hall is still exchanging air. The day after is where a refused class is quietly spoken as if you had signed it, because a customer asked and the slide was already green. This chapter is how the shift keeps the sentence.

## If you signed nothing

Do not let the word fit, held, or the class name into a notice, a tour script, or a capacity conversation. Those words are pens. You refused the pen. Tell the shift the prohibitions in one sentence they can say aloud: which place was not measured, which metal was not read, whether makeup is in the claim, whether the loud season is still missing. If they cannot say it, write it shorter, not softer. Softer is how "not signed" becomes "basically fine."

A vendor who changes the fill overnight has tainted the coupon that is still hanging. Chapter 15. The shift writes the change the morning they see it, even if the vendor calls it routine. Routine does not split an interval. If they cannot tell whether the fill changed, the interval is already suspect. Look. Do not wait for the lab to average it.

Do not start a customer load, a warranty clock, or a public claim on the strength of the photograph you refused. The corrosion sentence is not the IT sentence. The handover book already kept those apart. Keep them apart when the subject is air. A board that arrives next week does not retroactively make last month's missing silver strip into a pass.

## If you signed the narrow page

Read the limits to the shift before they repeat a tour. The narrow yes is easy to hear as the class. Say what you did not take: the other metal, the other season, the untreated makeup, the experiment media, the live box that was watch-only. Name the person who watches the date of the next hang. An unnamed date is a hope. Chapter 20 of the handover book used the same shape for a punch condition. A coupon condition expires into a refusal, not into a class. If the date passes and the strip is still in the air with no report, you do not have a longer yes. You have a late interval. Write late. Do not write held.

When a report arrives, read it outside the tour, in the order of chapter 13, before anyone updates the slide. Close one limit at a time. A silver result does not close a missing loud season. A treated makeup path does not close a coupon that straddled the install. Do not initial the old refused page. Write a new sentence as narrow as what is now true.

## What the shift may do

They may keep the doors latched, the named holes closed, and the life-safety paths unblocked. They may write down a propped door, a cable pull, a humidifier left on, a battery-room door sharing air. Those are conditions. They are not a new class. They may not dump a bed because a gauge moved, unless the spent rule and the handling title already allow that job. Chapter 15. A gauge is not a permit to improvise.

They may not tell a visitor the class. Visitors repeat tour sentences as facts. Give them the sentence on the sheet, including the not. If there is no sheet on the wall or in the shift book, the tour will invent one. Put the not where they stand. Identifiers and rates stay in the report, not on a public board. The not is enough.

## Operational Controls on the Shift Following a G2/G3 Corrosion Refusal

### Emergency Makeup Damper Throttling, Airlock Enforcement, and Portable Scrubbing

Under **ANSI/ISA-71.04-2013** (*Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*) and **ASHRAE TC 9.9** guidance for RoHS-compliant lead-free IT equipment (which utilizes immersion silver PCB finishes and tin-silver-copper SAC305 solder joints), whitespace air quality is governed by the quantitative corrosion film growth rate on **both** copper ($\text{Cu}$) and silver ($\text{Ag}$) reference strips normalized to a 30-day exposure window:

$$Q_{\text{makeup, emergency}} = Q_{\text{min\_pressurization}} \text{ while maintaining } \Delta P_{\text{hall}} \ge +10\,\text{Pa}$$

Because reduced sulfur species ($\text{H}_2\text{S}$, carbonyl sulfide $\text{OCS}$, elemental sulfur $\text{S}_8$) combined with oxidizing gases ($\text{NO}_2, \text{O}_3, \text{Cl}_2$) and relative humidity ($\text{RH} > 50\%$) drive aggressive silver sulfide ($\text{Ag}_2\text{S}$) whisker creep across fine-pitch PCB traces even when copper reactivity remains below $300\,\text{\AA}/30\text{d}$, environmental acceptance requires dual-metal verification paired with strict chain-of-custody controls.

| Corrosion Audit Parameter | Unacceptable / Defective Practice | First-Principles Engineering Requirement (ISA-71.04 / ASTM B825) | Mandatory Refusal or Remediation Action |
| :--- | :--- | :--- | :--- |
| **Core Chapter Focus** | Protecting Installed IT Hardware While Permanent Filtration Is Procured | Dual $\text{Cu} + \text{Ag}$ coulometric reduction with documented exposure timestamps | Refuse any environmental fitness claim missing $\text{Ag}$ or hang interval |
| **Class G1 Mild Pass Gate** | Quoting Copper rate alone ($<300\,\text{\AA}$) or visual strip color | $d_{\text{Cu}} < 300\,\text{\AA}/30\text{d}$ **AND** $d_{\text{Ag}} < 200\,\text{\AA}/30\text{d}$ (zero $\text{Cu}_2\text{S}$ on copper) | Classify G2 ($<1000/1000\,\text{\AA}$), G3 ($<2000/2000\,\text{\AA}$), or GX as non-compliant |
| **Chain of Custody & Blank** | Mailing strips without a sealed Field Travel Blank (`FTB`) | Sealed lot-matched travel blank $d_{\text{blank}} \le 25\text{--}35\,\text{\AA}$ subtracted/verified | Invalidate "Fit" certification if no unopened travel blank accompanied lot |
| **Filtration & Envelope Proof** | Installing recirculation filters in an unsealed negative-$\Delta P$ hall | Vapor-sealed envelope ($\Delta P \ge +12.5\,\text{Pa}$) + gas-matched media ($\text{EBCT} \ge 0.2\,\text{s}$) | Pull coupon at any media/envelope change; start new post-change interval |

## Decisions to record

- Prohibitions the shift can say aloud, written the same day.
- A secret or routine media change, written, interval tainted.
- Next hang dated, with a person. Late is not held.
- New report closes one limit, not the old page.
- Visitors given the not. Class not spoken from a refused page.

# 21. Hang it again

One interval is a fact about those weeks. A room that is supposed to stay fit is a claim about the weeks you have not measured yet. The claim needs a next hang, owned, dated, and tied to the thing that would make the last result a lie: the loud season, a media change, a cable pull, a new makeup mode. This piece will not tell you a number of days. A number invented here would be copied into procedures as if it were a standard. The standard, if the contract names one, stays in the contract. You write the event that ends the current trust, and you hang before that event is over, not after someone has already called the year fine.

## What ends the trust

Trust in the last coupon ends when the path changes. A new bed, a damper that starts bypassing, a door that no longer latches, a season the last strip missed, a construction job inside the envelope. Any one of those makes the old class a statement about a previous room. Leave it filed. Do not let it ride. The seventh book's rename rule is the same shape: a new path is a new source. A new hole is a new path.

Trust also ends when the spent test says the bed is no longer the machine you accepted. Chapter 15. You do not wait for the next annual hang to discover breakthrough if you already defined a faster test. You also do not cancel the hang because the faster test was calm. Calm on a gauge is not the metal at the board face. The audit remains. The alarm remains. They are not substitutes.

If nothing changed, you still do not keep last year's sentence for free. "Nothing changed" is a claim. It needs the second list from chapter 5, the mode the unit ran, and a person willing to sign that they looked. A year of silence is not a look. Schedule the look before the loud season, even when you believe the bed is fresh. Belief is not a blank. Chapter 19.

## How you compare two hangs

Same metal, same function of place, lot noted or the difference not called a trend. Overlapping intervals are not two hangs. They are one hang with a extra label. Back-to-back intervals can show a change. They cannot show a cause unless the path note says what changed at the boundary. Chapter 12. Write "rate differed." Do not write "the media saved us" unless the before and after were split at the install and the makeup path was actually through the bed.

A worse second hang is not automatically a spent bed. It may be a hole, a season, a blank you forgot, a lab method that changed. Check those before you buy fill. Buying fill for a propped door is the catalog error chapter 5 exists to prevent. A better second hang is not automatically a treatment success. It may be the quiet season. Chapter 4. Do not sign the year from the better hang alone.

## Do not stack the old class on the new slide

The slide will want last year's word in the corner while the new strip is still in the mail. Take the word off. A corner class is how a tour keeps speaking a sentence you already limited. Replace it with the date the next report is due, and the name of the person who notices if that date passes. A date in the corner is an instruction. A class in the corner is a claim. If the graphic people cannot bear an empty corner, the corner says "not signed." That is a complete sentence. It does not need a color.

## Who owns the next date

Name a person, not a team. Teams do not hang strips. The date is on the shift sheet the day book already uses, or it will be forgotten under a louder alarm. If the date passes, chapter 20 applies: late is not held. Do not backdate a hang you start the morning after someone asks for the class. A hang that starts when the question arrives measures the question, not the year you already claimed.

## Continuous Quarterly Surveillance Cadence and Multi-Year Trend Governance

### Designing the Rolling 90-Day Coupon Replacement Matrix

Under **ANSI/ISA-71.04-2013** (*Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*) and **ASHRAE TC 9.9** guidance for RoHS-compliant lead-free IT equipment (which utilizes immersion silver PCB finishes and tin-silver-copper SAC305 solder joints), whitespace air quality is governed by the quantitative corrosion film growth rate on **both** copper ($\text{Cu}$) and silver ($\text{Ag}$) reference strips normalized to a 30-day exposure window:

$$f_{\text{sampling}} = 4\,\text{intervals/year} \times \left( N_{\text{hall\_zones}} + N_{\text{makeup}} + 1_{\text{blank}} \right)$$

Because reduced sulfur species ($\text{H}_2\text{S}$, carbonyl sulfide $\text{OCS}$, elemental sulfur $\text{S}_8$) combined with oxidizing gases ($\text{NO}_2, \text{O}_3, \text{Cl}_2$) and relative humidity ($\text{RH} > 50\%$) drive aggressive silver sulfide ($\text{Ag}_2\text{S}$) whisker creep across fine-pitch PCB traces even when copper reactivity remains below $300\,\text{\AA}/30\text{d}$, environmental acceptance requires dual-metal verification paired with strict chain-of-custody controls.

| Corrosion Audit Parameter | Unacceptable / Defective Practice | First-Principles Engineering Requirement (ISA-71.04 / ASTM B825) | Mandatory Refusal or Remediation Action |
| :--- | :--- | :--- | :--- |
| **Core Chapter Focus** | Preventing Seasonal Drift and Spent Media From Going Undetected | Dual $\text{Cu} + \text{Ag}$ coulometric reduction with documented exposure timestamps | Refuse any environmental fitness claim missing $\text{Ag}$ or hang interval |
| **Class G1 Mild Pass Gate** | Quoting Copper rate alone ($<300\,\text{\AA}$) or visual strip color | $d_{\text{Cu}} < 300\,\text{\AA}/30\text{d}$ **AND** $d_{\text{Ag}} < 200\,\text{\AA}/30\text{d}$ (zero $\text{Cu}_2\text{S}$ on copper) | Classify G2 ($<1000/1000\,\text{\AA}$), G3 ($<2000/2000\,\text{\AA}$), or GX as non-compliant |
| **Chain of Custody & Blank** | Mailing strips without a sealed Field Travel Blank (`FTB`) | Sealed lot-matched travel blank $d_{\text{blank}} \le 25\text{--}35\,\text{\AA}$ subtracted/verified | Invalidate "Fit" certification if no unopened travel blank accompanied lot |
| **Filtration & Envelope Proof** | Installing recirculation filters in an unsealed negative-$\Delta P$ hall | Vapor-sealed envelope ($\Delta P \ge +12.5\,\text{Pa}$) + gas-matched media ($\text{EBCT} \ge 0.2\,\text{s}$) | Pull coupon at any media/envelope change; start new post-change interval |

## Decisions to record

- The event that ends trust in the last coupon, written now. Not a magic number of days.
- Next hang owned by a person, dated before the loud season or the path change, whichever comes first.
- Two hangs compared only if place, metal, and lot rules hold. Cause not written from the difference alone.
- A missed date written as late, not as another year of fit.

# 22. The line on the drawing

A drawing will say chemical filter, carbon filter, or a model number, on a makeup unit or on a room unit, and someone will treat the line as installed treatment. A line is a proposal. It becomes a treatment only when chapter 14's gates are true and air is going through the bed. Until then the line is a blank-off you have not seen. Do not let it into the corrosion sentence. Do not let it into the handover sentence either. The seventh book refused a renamed design called as-built. A filter line that was never blanked off is that defect, smaller and easier to miss.

## What you check on the drawing, and only that

You check whether the line sits on the makeup fan, the recirculation fan, or both. You check whether a damper is drawn around it. You check whether the same symbol is used for a dust filter and for the media, which is how the families get lost. You do not check the drawing against a code. You do not redraw it. You do not add a bed depth in the margin. If the symbol does not say which fan, the drawing cannot support the path. Chapter 16. Ask for a revised line, or write "path not on the drawing" and refuse the box as corrosion control.

A schedule that lists media weight, model, and pressure drop, and does not list the family, is the submittal chapter 14 already called a dust filter with extra pages. The schedule can stay in their file. Your sheet does not gain a class from a weight. Weight is not a gas.

If the drawing and the unit on the floor disagree, the floor wins until the drawing is corrected, and neither supports the sentence until they agree. Disagreement is not averaged. A model number on the drawing and a different fill in the rack is a rename. Treat it as a new media. Old acceptance is void. Chapter 2 of the monitor book, applied to a bed. Do not discover the swap in the next coupon and call it drift.

## The symbol is not the fill

A symbol repeated on every unit does not mean every unit has the same family inside. One handler may have been filled. The next may still be an empty frame with the symbol copied from the typical detail. Walk the frame, or have a named person walk it, before the symbol supports a path. A typical detail is a proposal for all of them. Typical is the word chapter 21 of the handover book already refused as evidence. It is the same word here. Each bed is its own gate. A hall with six symbols and one filled bed has one bed. Sign the one, or sign none. Do not sign six.

## As-built, later

When the bed is in and the blank-off has been seen, the drawing may be marked to that fact, with a date, by a person. The mark says path, family claimed, spent test cited by title. It does not say the room is held. Holding is the coupon. A stamp that says corrosion controlled, dated the day of install, is the wide sentence in CAD. Strike it the way you strike commissioned. Chapter 10 of the handover book. The word can return only with a coupon interval that matches it, in a later revision, not by surviving in the title block because nobody opened the file.

## Auditing Mechanical Schedules and Submittals Beyond Generic 'Carbon Filter' Notes

### Translating Drawing Callouts into Verifiable Gas-Family Performance Gates

Under **ANSI/ISA-71.04-2013** (*Environmental Conditions for Process Measurement and Control Systems: Airborne Contaminants*) and **ASHRAE TC 9.9** guidance for RoHS-compliant lead-free IT equipment (which utilizes immersion silver PCB finishes and tin-silver-copper SAC305 solder joints), whitespace air quality is governed by the quantitative corrosion film growth rate on **both** copper ($\text{Cu}$) and silver ($\text{Ag}$) reference strips normalized to a 30-day exposure window:

$$\Delta P_{\text{media, clean}} + \Delta P_{\text{HEPA}} \le \Delta P_{\text{fan\_available}} \text{ at rated } \text{EBCT}$$

Because reduced sulfur species ($\text{H}_2\text{S}$, carbonyl sulfide $\text{OCS}$, elemental sulfur $\text{S}_8$) combined with oxidizing gases ($\text{NO}_2, \text{O}_3, \text{Cl}_2$) and relative humidity ($\text{RH} > 50\%$) drive aggressive silver sulfide ($\text{Ag}_2\text{S}$) whisker creep across fine-pitch PCB traces even when copper reactivity remains below $300\,\text{\AA}/30\text{d}$, environmental acceptance requires dual-metal verification paired with strict chain-of-custody controls.

| Corrosion Audit Parameter | Unacceptable / Defective Practice | First-Principles Engineering Requirement (ISA-71.04 / ASTM B825) | Mandatory Refusal or Remediation Action |
| :--- | :--- | :--- | :--- |
| **Core Chapter Focus** | Refusing Unspecified Filter Boxes on Construction Drawings | Dual $\text{Cu} + \text{Ag}$ coulometric reduction with documented exposure timestamps | Refuse any environmental fitness claim missing $\text{Ag}$ or hang interval |
| **Class G1 Mild Pass Gate** | Quoting Copper rate alone ($<300\,\text{\AA}$) or visual strip color | $d_{\text{Cu}} < 300\,\text{\AA}/30\text{d}$ **AND** $d_{\text{Ag}} < 200\,\text{\AA}/30\text{d}$ (zero $\text{Cu}_2\text{S}$ on copper) | Classify G2 ($<1000/1000\,\text{\AA}$), G3 ($<2000/2000\,\text{\AA}$), or GX as non-compliant |
| **Chain of Custody & Blank** | Mailing strips without a sealed Field Travel Blank (`FTB`) | Sealed lot-matched travel blank $d_{\text{blank}} \le 25\text{--}35\,\text{\AA}$ subtracted/verified | Invalidate "Fit" certification if no unopened travel blank accompanied lot |
| **Filtration & Envelope Proof** | Installing recirculation filters in an unsealed negative-$\Delta P$ hall | Vapor-sealed envelope ($\Delta P \ge +12.5\,\text{Pa}$) + gas-matched media ($\text{EBCT} \ge 0.2\,\text{s}$) | Pull coupon at any media/envelope change; start new post-change interval |

## Decisions to record

- Drawing line read as proposal until air goes through a bed that passed the gates.
- Fan and bypass damper found on the drawing, or path not on the drawing.
- Floor and drawing disagree: neither signed. Swap treated as new media.
- A stamp that says controlled, struck. Coupon not replaced by CAD.
