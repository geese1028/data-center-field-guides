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
