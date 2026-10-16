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
