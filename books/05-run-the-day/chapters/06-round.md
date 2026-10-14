# 6. The Shift Inspection Round

Telemetry dashboards lie. A Building Management System (BMS) pressure transducer can drift out of calibration; an optical smoke detector can accumulate dust and report clear; an RTD temperature sensor can fail high and be clamped by a bad software filter.

The physical shift round is the ultimate verification that the physical reality of the data center matches the mathematical model in the control room.

```
+-----------------------------------------------------------------------------+
| SHIFT ROUND PHYSICAL INSPECTION TOPOLOGY |
| |
| [STATION 1] MV Substation & Switchgear (35kV/10kV Gas, Springs, Relays) |
| | |
| [STATION 2] Transformer Vaults (Winding Temps, Acoustic Hum, Lugs) |
| | |
| [STATION 3] UPS & Battery Rooms (DC Float Voltage, String Temps, Exhaust) |
| | |
| [STATION 4] Central Chiller Plant (Approach Temp, Oil Pressure, Head Press)|
| | |
| [STATION 5] Liquid CDU Stations (0.15-0.90 MPa, Refractometer, Catch Pan) |
| | |
| [STATION 6] AI Whitespace & NVL72 Racks (Thermal IR, Delta-P, FD83 Couplings)|
+-----------------------------------------------------------------------------+
```

![Shift Round Inspection Topology](../figures/fig-03-shift-round-inspection-topology.png)

A technician walking the round is not an errand runner checking boxes on a clipboard. A technician on the round is an active, multi-sensory diagnostic instrument.

## The Multi-Sensory Inspection Discipline

Every square meter of a production data center must be audited across four sensory channels:
1. **Visual**: Inspect equipment for fluid drips, staining, discoloration, rust, loose fasteners, bulging capacitors, blistered paint indicating extreme heat, and verify mechanical analog gauge needles against digital telemetry readings.
2. **Acoustic**: Listen for cavitation in pump volutes (sounds like pumping gravel), harmonic buzzing in transformers indicating loose laminations or core saturation, bearing squeal in fan motors, and whistling air leaks around aisle containment doors.
3. **Thermal**: Use calibrated handheld infrared (IR) cameras to sweep electrical busbar connections, circuit breaker terminals, cable lugs, and mechanical bearings. Any connection exhibiting a temperature > 70°C or a phase-to-phase differential ΔT > 10 K is an immediate Category 1 defect.
4. **Olfactory**: Sniff for the sharp, pungent scent of burning electrical insulation (ozone and overheated phenolic resin), the sweet odor of atomized propylene glycol from a micro-leak, or the sulfurous stench of an off-gassing lead-acid battery.

## The Six Critical Inspection Stations

Following the operational standards outlined in OpenViking (`ALZJ-YW-2.6XZ02` for IT Whitespace and `ALZJ-YW-2.6XZ10` for Liquid Cooling Infrastructure), the shift inspection round traverses six mandatory stations:

```
+-----------------------------------------------------------------------------+
| CRITICAL STATION INSPECTION METRICS |
| |
| Station / System Standard Parameter Rejection Threshold |
| ----------------------- ------------------------ ---------------------- |
| MV Switchgear SF6 Gas Pressure Nominal Low Pressure Alarm Trip |
| Transformers Winding Temp < 90°C Temp >= 110°C (Alarm) |
| UPS Battery Rooms Ambient Temp 20°C - 25°C Temp > 28°C / Swelling |
| Chiller Plant Condenser Approach <1.5K Approach >= 2.5 K |
| CDU Secondary Loop Pressure 0.15 - 0.90 MPa Pressure < 0.12 MPa |
| CDU Glycol Mix 25.0% PG (+/- 1.0%) PG < 23% or > 27% |
| IT Whitespace Aisles Underfloor DP >= 5.0 Pa DP < 2.5 Pa (Air Starve)|
| Liquid Racks (NVL72) FD83/UQD Couplings Dry Any Active Fluid Droplet|
+-----------------------------------------------------------------------------+
```

![CDU Shift Inspection Checklist](../figures/fig-05-liquid-cdu-shift-inspection-checklist.png)

### Station 1: Medium-Voltage Substation & Switchgear
- Inspect 35kV and 10kV circuit breaker spring charge indicators (verify charged state).
- Check SF6 gas pressure indicators on gas-insulated switchgear (GIS); ensure needles sit securely in the green zone.
- Verify DC control bus battery charger voltage (125 VDC ± 2%) and ensure zero ground-fault alarms exist on the ungrounded DC control system.

### Station 2: Transformer Vaults
- Verify digital winding temperature indicators on dry-type transformers (normal operating range: 60°C - 85°C; alarm threshold at 110°C; automatic trip at 130°C).
- Inspect forced-air cooling fans for physical obstruction and bearing vibration.
- Check oil-filled transformers for tank oil level, silica gel desiccant color (deep blue; pink indicates moisture saturation requiring immediate replacement), and inspect tank seams for weeping oil.

### Station 3: UPS & Battery Rooms
- Record DC bus float voltages and battery charging currents across all static UPS modules.
- Audit battery room ambient temperature (maintain strictly between 20°C and 25°C; lead-acid battery design life degrades by 50% for every 8 K rise above 25°C).
- Visually inspect individual VRLA battery jars for case bulging, terminal post corrosion, or electrolyte leaking; for lithium-ion systems, verify that the Battery Management System (BMS) reports zero cell voltage imbalances (> 50 mV).
- Confirm hydrogen exhaust fan operation by feeling airflow at the intake louvers.

### Station 4: Central Chiller & Pumping Plant
- Audit chiller operating logs: verify that condenser water approach temperature is ≤ 1.5 K (ΔT_approach = T_cond, leaving - T_tower, entering). An approach temperature > 2.5 K indicates severe tube fouling or scaling requiring chemical brushing.
- Check compressor oil levels, oil pressures, and oil return temperatures.
- Audit chilled water pump differential pressures (ΔP) and verify that secondary variable speed drives are modulating correctly without hunting.

### Station 5: Secondary Cooling Distribution Units (CDU)
Per OpenViking `ALZJ-YW-2.6XZ10`, the CDU is the mechanical heart of high-density AI clusters:
- **Pressure Envelope**: Verify primary facility water system (FWS) supply pressure and secondary technology cooling system (TCS) supply pressure remain strictly between 0.15 MPa and 0.90 MPa. Verify that pump differential pressure is < 1.0 bar.
- **Thermal Performance**: Verify that plate heat exchanger approach temperature (ΔT_approach = T_TCS, supply - T_FWS, supply) does not exceed 8.0 K. An approach > 8.0 K indicates biological fouling or particulate clogging on the plate surfaces.
- **Fluid Chemistry**: Use a calibrated optical refractometer to test secondary coolant. Propylene glycol concentration must measure precisely **25.0% by weight** (± 1.0%), providing freeze protection down to -11.5°C and burst protection down to -22.0°C. Coolant conductivity must measure < 10 μ S/ cm, with pH maintained between 7.5 and 9.0.
- **Physical Integrity**: Inspect the internal CDU catch pan and base frame for moisture. Verify that the continuous rope leak detection sensor is completely dry and properly positioned. Check the nitrogen pre-charge pressure on the thermal expansion tank (P_0 = P_fill - 0.2 bar).

### Station 6: AI Whitespace & NVL72 Racks
Per OpenViking `ALZJ-YW-2.6XZ02`:
- **Electrical Distribution**: Inspect remote power panels (RPPs) and power distribution units (PDUs). Sweep circuit breakers and terminal lugs with an infrared camera to detect loose terminations.
- **Airflow Containment**: Audit cold aisle containment (CAC) or hot aisle containment (HAC). Verify that differential pressure across the raised floor or containment barrier remains ≥ 5.0 Pa. Verify that all unpopulated rack units contain blanking panels; a single missing 1U panel permits 25 L/s of air bypass, creating localized hot spots.
- **Liquid Cooling Manifolds & Couplings**: Audit rack-level vertical distribution manifolds. Inspect all quick-disconnect couplings (Danfoss FD83 or Universal Quick Disconnects) serving compute trays and NVLink switch trays. Any sign of fluid weeping, crusting, or drop formation is an immediate Stop Work condition requiring tray isolation. Check that drip trays under the rack manifolds are clean and dry.

## The Immediate Defect Entry Rule

If you discover a defect during the shift round, it must be entered into the site computerized maintenance management system (CMMS) or physical defect register **before you leave the room**.

Taking a photograph on a personal mobile phone with the intention of logging the issue at the end of the shift is unacceptable:
- A defect entered into the register has a physical timestamp, an asset ID, a priority classification, and an assigned owner.
- A photograph on a smartphone is an unmanaged private note that is forgotten when an alarm sounds thirty minutes later.

If the defect impairs equipment redundancy or causes operating parameters to cross an SLA threshold, the shift round halts immediately, the duty manager is notified via radio, and an incident ticket is generated on the spot. Never complete the round and casually mention a leaking CDU pump during lunch.

## Decisions to Record

- Physical inspection route completed, with start and completion timestamps and technician signatures.
- Specific operating parameters logged at all six inspection stations.
- Handheld refractometer, conductivity, and pH measurements logged for the secondary cooling loop.
- All defects entered into the formal site register prior to exiting each room, or an explicit statement of zero defects found.
