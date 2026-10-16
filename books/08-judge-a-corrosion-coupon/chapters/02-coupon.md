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
