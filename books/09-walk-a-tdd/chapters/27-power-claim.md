# 27. How to read a power claim

They will show a single line, a capacity number, and a sentence about redundancy. You are not redrawing the line. You are testing whether the claim and the evidence are the same width.

Start with the claim, not the drawing. What must stay up for the performance they sell. The equipment in scope, or the whole building, or a named suite. If the claim does not say, the drawing cannot save it. A drawing of the whole site does not prove the suite, and a drawing of the suite does not prove the site.

Then the path. Two feeds, a generator, a battery, a second board: each is a name until a document says it was tested, or you saw the test. A brochure runtime is not the test. A single-line note that says N+1 is not the test. Spoken redundancy is not the test. Write tested, documented, or spoken. Only the first two may enter the opinion, and documented means you opened the record, not that they mentioned it.

Then the number. Design kilowatts, nameplate, and a measured load are three numbers. Do not add them. Do not put design in the operating cell because the meter was inconvenient. If the financing model uses a load the visit cannot see, say the model’s load is not your finding. Counsel and the model owner own that cell. You own whether a live point exists and whether you were shown it.

A utility application, a transformer rating, and an expansion still on paper are future path, not present path. Label future. A future path does not support a sentence about tonight’s equipment. If the equipment in scope is already installed, the path that feeds it now is the one that matters. The expansion may be a separate sentence, evidenced or not.

You do not copy the drawing into the report. You cite the revision you read, and you say whether you accept it as current. Floor and drawing disagree: neither supports a precise claim until they agree. You can still support a coarser one: a second path was not shown.

## Utility substation diversity: physical reality versus marketing claim

The most dangerous failure in data center due diligence is accepting a sales brochure's claim of "dual utility feeds" without auditing the physical underground routing:

![Figure 09.2: Utility Substation Diversity and Grid Dual-Feed Reality](../figures/fig-02-utility-substation-and-grid-diversity.png)

### 1. The pseudo-diverse single-bus trap

Developers frequently present two separate utility power bills or two meter accounts as evidence of redundancy. In reality, both medium-voltage feeders often originate from the same primary utility transmission substation, connected to the same high-voltage transformer bus section. 

Even worse, both medium-voltage cables are frequently pulled through the exact same underground duct bank or street utility manhole outside the campus gate. A single municipal excavator strike, vehicle collision with a riser pole, or manhole cable fire severs both feeds simultaneously, collapsing the entire data center onto standby generators.

### 2. True physical transmission grid diversity

Under Uptime Tier III / IV and GB 50174 Class A criteria, true electrical grid diversity requires:
- **Independent Transmission Substations**: Feeder A and Feeder B must originate from two distinct, geographically separate utility transmission substations (e.g. Substation North at 220 kV and Substation South at 110 kV), powered by separate grid transmission networks.
- **Geographically Diverse Cable Routing**: The two cable routes must follow independent rights-of-way separated by at least 1.5–2.5 km, with zero shared utility trenches, duct banks, bridges, or manholes.
- **Dual Campus Entry Vaults**: The two feeders must enter the data center property from opposite street boundaries, through concrete-encased duct banks terminating in independent, blast-separated medium-voltage electrical vaults located at least 20 m apart.

### 3. Electrical TDD audit checklist

When auditing the electrical single-line diagram and utility agreements, verify five hard technical parameters:
1. **Capacity Allocation Letter**: Inspect the utility's formal capacity reservation letter. Verify whether the capacity is **firm and uncurtailable** or subject to seasonal grid curtailment / clawback clauses. A utility application or pending permit is future capacity, not present capacity.
2. **N-1 Emergency Capacity Contingency**: Each utility feeder and primary transformer must be rated to carry 100% of the facility's maximum coincident peak load plus UPS battery recharge current (I_recharge ≈ 15%–20% of UPS rating) continuously under single-path N-1 operation:
 $$S_{\text{feeder}} \ge \frac{P_{\text{facility\_peak}} + P_{\text{recharge}}}{\text{PF}} \times 1.10$$
3. **Breaker Transfer Scheme and Latency**: Audit the medium-voltage bus-tie transfer logic. Is it an Automatic Transfer Switch (ATS) with open-transition break-before-make latency (2–10 seconds), or a closed-transition sync-check scheme? Confirm that UPS energy storage ride-through seamlessly bridges the transfer window without IT power disruption.
4. **Short-Circuit Withstand & Arc-Flash Hazard**: Verify that switchgear busbars and breakers have certified short-circuit withstand ratings (I_sc ≥ 40 kA or 65 kA) conforming to IEEE Std 141 short-circuit study results. Arc-flash warning labels must display incident energy levels (cal/cm²) dated within the last three years.
5. **Power Factor & Harmonic Distortion**: Reconcile utility revenue meters against facility BMS power meters. Verify power factor PF ≥ 0.95 and total harmonic voltage distortion THD_v ≤ 5.0% (IEEE 519) to prevent utility tariff surcharges or filter resonance trips.

## Decisions to record

- The power claim, in their words, before you open the drawing.
- True utility substation diversity verified via GIS route maps, or logged as "pseudo-diverse single bus."
- Firm capacity reservation letter verified, uncurtailable vs interruptible.
- Each named path: tested, documented, spoken, or future.
- N-1 single-feeder emergency capacity verified with battery recharge load.
- Design load kept out of the operating cell.
- Drawing revision cited, not pasted. Disagreement written.
