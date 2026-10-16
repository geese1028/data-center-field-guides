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
