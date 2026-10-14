# 20. The building is a class of risk, not a postcard

You will be walked past the neighborhood, the structure, the water tank, and the fuel store. Write the class. Do not write the tour.

Outside: what would matter is a hazard the contract assumes is absent, and whether you were shown evidence or only a view from the gate. A view is a view. It is not a study of flood, pollution, or a neighbor's store of fuel. If the engagement needs that study, it is a named report by someone whose job that is, cited, not reconstructed from the car park. You may write "no obvious incompatible use seen from the roads we were on" and stop. That sentence does not clear a flood map you did not read.

Structure and height are facts on a drawing you accept as current, or they are not in the opinion. Do not estimate them. A drawing you do not accept as as-built does not support a sentence about what was built.

Water and fuel are about duration when the utility stops. A tank either has a stated volume tied to a stated demand in a document, or you write "volume not tied to demand." You do not adopt their daily-consumption claim without the basis. A looped supply is a second path only if both sides are real and a document or a test says so. A diagram with two lines is not yet a second path.

Condensate and other water that can reach equipment is a path you can see. If it is routed away from the equipment, say you saw the route, not that it can never fail. If you did not enter the floor void, you did not see it. Unentered is not protected.

None of this is a design review. You are not issuing a code compliance certificate. You are saying which classes were evidenced, which were a view, and which were not entered.

## Site hydrology, flood plain elevations, and seismic envelopes

A facility that passes a curb tour may harbor catastrophic civil and environmental liabilities. The TDD audit must reconcile the physical site against certified civil hydrology and geotechnical surveys:

![Figure 09.3: Natural Hazard Hydrology, 500-Year Flood Elevation and Seismic Design](../figures/fig-03-natural-hazards-and-flood-plain-hydrology.png)

### 1. Civil hydrology and the 500-year Base Flood Elevation (BFE)

Commercial building codes often cite the 100-year flood plain (1.0% annual exceedance probability) as the regulatory baseline. For mission-critical data centers underwriting hundreds of millions of dollars in syndicated debt, the 100-year benchmark is completely unacceptable.

**The Golden Rule of Data Center Elevation**:
Under GB 50174 Class A and institutional infrastructure underwriting guidelines, all critical IT whitespace Finished Floor Levels (FFL) and essential mechanical/electrical plinths must be elevated at least 1.0 m–1.5 m above the certified **500-Year Base Flood Elevation (0.2% annual exceedance probability)**.

Furthermore, on-site stormwater management must be engineered to retain a 100-year, 24-hour storm event without relying on municipal storm sewers. Peak stormwater runoff rate (Q) is governed by the Rational Method:

$$Q = C \times I \times A$$

Where:
- Q is peak runoff rate (m³/s).
- C is the dimensionless runoff coefficient (0.85–0.95 for paved data center roofs, roadways, and transformer yards).
- I is rainfall intensity (mm/hr) for the 100-year design storm.
- A is total contributing catchment area (m²).

The auditor must inspect the on-site retention basin, weir discharge invert elevations, and backup diesel-driven stormwater sump pumps. If the site relies on gravity storm discharge into an off-site canal whose crest elevation exceeds the facility yard during storm surges, log a critical Tier 1 flood risk.

Sub-grade basements must be audited for hydrostatic uplift. Where the historical high water table rises above the basement slab elevation, verify dual-layer bentonite or elastomeric waterproofing membranes and continuous dewatering sump pits with emergency generator power backing.

### 2. Seismic design category and lateral component bracing

Under IBC / ASCE 7-22 and GB 50011, data centers are classified as Essential Facilities with a Component Importance Factor I_p = 1.5. In Seismic Design Categories (SDC) D, E, or F, or where Peak Ground Acceleration (PGA) exceeds 0.25g:
- Medium-voltage transformers, centrifugal chillers, cooling towers, and standby diesel generators must be anchored with certified seismic snubbers to prevent shear dislocation.
- Raised access floor pedestals must feature welded diagonal seismic strut bracing tied directly into the concrete structural subfloor.
- VRLA and lithium-ion battery racks must incorporate heavy-gauge steel side retainers and floor anchor plates tested to withstand horizontal lateral acceleration F_p = 0.4 · S_DS · I_p · W_p.

### 3. Perimeter hazard exclusion buffers

A technical due diligence site audit must verify mandatory geographical separation distances:
- **Commercial Airport Runways**: Minimum 8.0 km from the centerline of active commercial jet runways to avoid FAA Part 77 imaginary airspace penetration and high-frequency acoustic/vibration coupling.
- **Toxic / Chemical Hazmat Facilities**: Minimum 1.5 km buffer from chemical refineries, fertilizer storage, and toxic gas facilities to eliminate plume corrosion (H_2S, SO_2) or toxic evacuation zones.
- **Heavy Freight Rail Corridors**: Minimum 150 m setback to prevent low-frequency ground vibration transmission (<10 Hz) from inducing head crashes in rotating media or optical switch transceiver jitter.
- **Overhead High-Voltage Lines**: No high-voltage transmission lines (>110 kV) may traverse directly above the data hall whitespace footprint.

## Decisions to record

- Outside hazards: study cited, view only, or not looked at.
- Finished floor elevation verified ≥ 1.0 m above 500-year Base Flood Elevation (BFE).
- Stormwater retention basin volume verified against 100-year storm rational formula.
- Structural facts only from a drawing you accept. No estimates.
- Seismic restraint snubbers verified for heavy mechanical and battery plants.
- Water or fuel duration: tied to a demand in a document, or not tied.
- Voids and routes you did not enter, listed.
