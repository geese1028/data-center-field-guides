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
