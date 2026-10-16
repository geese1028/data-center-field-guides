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
