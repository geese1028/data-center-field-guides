# 2. People on Shift

A data center does not run on software telemetry. It runs on the competence, licensing, and physical discipline of the technicians walking the plant floors. If you do not know the exact qualifications of the people holding the master keys, you do not control the plant.

```
+-----------------------------------------------------------------------------+
| SHIFT QUALIFICATION & GATING MATRIX |
| |
| Role Certifications Required Authorized Scope |
| ------------------ ---------------------------- ----------------------- |
| Duty Manager CDFOM / Operations License Overall SLA & Permits |
| Lead Electrician High-Voltage (HV/LV) License Switchgear, Transformers |
| Cooling Specialist Refrigeration / HVAC License Chillers, CDUs, Glycol |
| Shift Technician Data Center Facilities Cert Rounds, Telemetry, Logs |
| Escort / Safety OSHA 30 / First Aid / CPR Vendor Supervision, LOTO |
+-----------------------------------------------------------------------------+
```

## Licensing and Statutory Requirements

In high-density AI data centers housing megawatt-scale liquid cooling and multi-megavolt-ampere electrical substations, generic facility technicians are an existential liability. Operational tasks require statutory certification:
- **Electrical Operations**: Any switching, racking, or live testing on medium-voltage (10kV/35kV) or low-voltage (400V/480V) switchgear must be performed exclusively by certified high-voltage/low-voltage electricians holding valid governmental licenses.
- **Cooling & Chemical Operations**: Operating centrifugal chillers, industrial cooling towers, and primary/secondary pumping stations requires licensed refrigeration technicians certified in pressurized refrigerant handling and industrial water treatment.

Per OpenViking operational guidelines (`ALZJ-YW-2.6XZ10`), liquid cooling operations involving secondary distribution units (CDUs), primary facility water systems (FWS), and rack-level manifolds require verified technical training on chemical biocides, glycol concentration measurement, and leak containment protocols.

If a technician on shift lacks the statutory license for high-voltage switching, their name may not appear on an electrical switching ticket. If an unlicensed contractor is found with an open panel door, work stops immediately.

## The Two-Person Rule

No critical switching operation, high-voltage racking, or valve isolation on a primary cooling loop may ever be performed by a solo technician.

The two-person rule requires:
1. **The Performer**: The certified technician holding the approved Method of Procedure (MOP) who physically touches the control switch, breaker handle, or isolation valve.
2. **The Checker**: An equally qualified technician standing immediately behind the performer, holding the printed procedure, reading each step aloud, verifying equipment tags (e.g., confirming breaker label `SWG-01-4A` matches the ticket before racking), and maintaining emergency stop awareness.

The checker's sole duty during the operation is verification and safety. If the performer begins reaching for the wrong breaker handle or turns a valve in the wrong sequence, the checker possesses absolute authority to halt the operation instantly.

```
+-------------------------------------------------------------------------+
| THE TWO-PERSON RULE |
| |
| +------------------+ +------------------+ |
| | THE CHECKER | | THE PERFORMER | |
| | Holds MOP sheet | | Touches switch | |
| | Reads step loud | ----------> | Points to label | |
| | Verifies tag ID | | Executes action | |
| | Has Stop Power | | Reports status | |
| +------------------+ +------------------+ |
+-------------------------------------------------------------------------+
```

## Stop Work Authority (SWA)

Every individual entering the facility—from the senior operations director to an apprentice cable puller—possesses full, unconditional Stop Work Authority.

Stop Work Authority is triggered whenever:
- Physical conditions in the room diverge from the assumptions in the written MOP.
- An unexpected alarm sounds on the Building Management System (BMS) or Electrical Power Monitoring System (EPMS).
- Water droplets, fluid pooling, or abnormal chemical odors are detected near electrical equipment.
- A required safety barricade, personal protective equipment (PPE), or Lockout/Tagout (LOTO) lock is missing or compromised.
- An operator experiences confusion or uncertainty regarding the next procedural step.

When Stop Work is invoked:
1. Equipment is immediately placed into the nearest stable, safe state defined in the procedure.
2. Tools are set down; no further valves or switches are moved.
3. The duty manager is summoned to the work location.
4. Work resumes only after the ambiguity is resolved and documented in writing on the permit.

No technician or contractor may ever be reprimanded, penalized, or questioned for invoking Stop Work in good faith. A facility culture where technicians hesitate to call Stop Work because of schedule pressure is a facility waiting for a multi-megawatt blackout.

## The 30-Minute Joint Walkthrough

Never execute a shift handover sitting behind desks in the control room. A handover completed over coffee is an abdication of duty.

The incoming duty manager and outgoing duty manager must complete a mandatory 30-minute joint physical walkthrough of the six critical facility zones before signing the Day Sheet:
1. **Medium-Voltage Substation**: Inspect 35kV/10kV switchgear, breaker spring charge indicators, SF6 gas pressure gauges, and battery charger status.
2. **Transformer Vaults**: Inspect dry-type/oil-filled transformer winding temperatures (ensure T < 90°C), cooling fan operation, and listen for abnormal acoustic harmonics.
3. **UPS & Battery Rooms**: Verify DC bus float voltages, individual string temperatures (T < 25°C), inspect for battery post corrosion or swelling, and verify hydrogen exhaust fan airflow.
4. **Central Chiller & Pumping Plant**: Check chiller approach temperatures (ΔT_approach ≤ 1.5 K), condenser head pressures, variable frequency drive (VFD) frequencies, and acoustic vibration.
5. **CDU Liquid Stations**: Verify primary/secondary pressures (0.15 - 0.90 MPa), pump differential pressures (ΔP < 1.0 bar), expansion tank fluid levels, and inspect catch basins for moisture.
6. **AI Whitespace Halls**: Walk hot and cold aisles, inspect power distribution units (PDUs) for thermal hotspots, verify tile differential pressure (ΔP ≥ 5 Pa), and check quick-disconnect couplings (FD83/UQD) for weeping.

Both managers must walk the entire path side-by-side. If the outgoing manager refuses to walk the floor, the incoming manager assumes all plant equipment is in an unverified state and notes the refusal on the turnover log.

## Decisions to Record

- Names of all on-shift personnel, their verified license numbers, and expiration dates.
- Confirmation that high-voltage and critical fluid operations adhere to the two-person rule.
- Any invocation of Stop Work Authority during the shift, detailing the cause and resolution.
- Completed 30-minute joint physical walkthrough signed by both incoming and outgoing managers.
