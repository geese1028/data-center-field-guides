# 3. The Service You Sold

Customers do not buy your diesel fuel tanks, your titanium plate heat exchangers, or your personal dedication. Customers buy an SLA: a mathematically defined service contract guaranteeing electrical availability, thermal delivery, and escalation timing. If you cannot cite the exact clause in the master service agreement, you are operating on hearsay.

**SERVICE BOUNDARY MATRIX**

| Contract Parameter Guara | nteed Limit Measurement So | urce |
| :--- | :--- | :--- |
| AC Power Availability 99 | .999% (Five Nines) Active | PDU Revenue Mtrs |
| Secondary Supply Temp 25 | .0°C to 32.0°C (W3/W4) CDU | TCS Supply RTD Tree |
| Primary Chilled Water 12 | .0°C to 18.0°C FWS Header | Flow/Temp |
| Air Temperature (Rack) 1 | 8.0°C to 27.0°C (ASHRAE) C | old Aisle Sensors (3h) |
| Incident Notice Clock <= | 15 Minutes from T-0 Clien | t Portal & Phone |

## Contractual Service Limits vs. Engineering Margins

Operating a data center requires distinguishing between three distinct boundaries:
1. **Design Setpoints**: The optimal operating conditions engineered into the control sequences (e.g., CDU secondary supply at 28.0°C, cold aisle air at 22.0°C).
2. **Operational Alarm Limits**: The internal facility thresholds that alert technicians to take corrective action before client impact occurs (e.g., secondary supply reaches 30.5°C, prompting standby pump start or chiller staging).
3. **Contractual Breach Limits**: The legal boundaries defined in the client SLA that trigger service credit penalties and default notices (e.g., secondary supply exceeding 32.0°C for > 5 continuous minutes, or rack intake air exceeding 27.0°C).

Never allow the client's commercial representative to treat an internal operational alarm as a contractual service breach. Conversely, never allow your shift team to dismiss a temperature excursion that crossed the SLA threshold simply because "it only spiked for three minutes." If the contract measures excursions in 60-second rolling averages, a three-minute spike is an SLA violation. Log it.

## The Availability Equation

Data center availability (A) is calculated as:

$$A = \frac{\text{Total Period Minutes} - \text{Outage Minutes}}{\text{Total Period Minutes}}  \times 100\%$$

In modern multi-tenant colocation and hyperscale build-to-suit contracts, "Outage Minutes" are defined with extreme legal precision:
- Does an outage require loss of power on both A and B cords of a 2N rack, or does loss of redundancy on a single cord constitute a fractional outage?
- If a customer's server continues running on cord B while cord A is de-energized, does the SLA clock run?
- If a liquid cooling CDU drops from N+1 dual pumps to single pump operation without thermal derating, has an outage occurred?

The duty manager must know the contractual answer to these questions before an event occurs. During a live incident, there is no time to consult external legal counsel.

## The Notice Period Clock

When an infrastructure excursion crosses an SLA threshold, the clock begins ticking immediately:

$$\Delta t_{\text{notice}} = t_{\text{sent}} - t_{\text{detect}} \le T_{\text{contractual}}$$

Most hyperscale SLAs require formal incident notification within **15 minutes** of initial detection (T_contractual ≤ 15 min).

| **THE 15-MINUTE NOTIFICATION WINDOW** |
| :--- |
| T = 00:00 Alarms trigger on BMS/EPMS; trip detected |
| T + 05:00 Duty Manager verifies event; stabilizes safe state |
| T + 10:00 Draft incident notification: Symptom, Time, Impacted Halls |
| T + 14:00 Notification transmitted to client technical contacts |
| T + 15:00 Contractual SLA notification deadline expires |

A common failure among novice operations managers is delaying the initial customer notification while technicians investigate the root cause. This is a contractual disaster. A client will forgive a transformer trip that was stabilized within minutes; they will never forgive discovering their servers are down from their own telemetry while the data center manager remained silent for forty minutes.

Send the notification at minute 12. State the observed facts: the timestamp of the event, the affected electrical buses or cooling loops, the current status of the emergency systems, and the timestamp of the next update. Keep root-cause theories completely off the wire.

## What You Do Not Report as Owed

Measure only what the contract specifies. Generating internal operational metrics—such as real-time Power Usage Effectiveness (PUE), Carbon Usage Effectiveness (CUE), or Water Usage Effectiveness (WUE)—is vital for facility engineering and corporate sustainability reporting. However, do not paste internal PUE calculations into a daily SLA delivery certificate unless the contract explicitly defines PUE as a billable SLA parameter.

If an efficiency ratio is not part of the commercial contract, reporting it on a daily client log turns an internal engineering aspiration into an external target that clients will use to dispute invoices. Keep contractual delivery logs strictly separated from internal engineering analytics.

## Decisions to Record

- The exact master contract title, amendment number, and clause governing today's service.
- The authoritative telemetry meter ID and clock source used for contractual timekeeping.
- The contractual notification window (T_contractual) in minutes.
- Any SLA excursion observed during the shift, recorded with microsecond timestamps from the sequence-of-events recorder.

## Quantitative Service Level Agreement (SLA) Boundary Envelopes

A colocation or hyperscale service contract does not promise that chillers, pumps, or UPS inverters will never fail; it promises that **at the physical demarcation boundary**, four continuous environmental and electrical parameters will remain inside a mathematically bounded corridor $100\%$ of the contracted time.

| SLA Service Stream | Physical Demarcation Point | Standard Normal Operating Band | Hard SLA Breach Trigger Condition |
| :--- | :--- | :--- | :--- |
| **Dual-Corded Critical Power** | Load terminals of Rack PDU Breakers (Bus A & Bus B) | $400/230\,\text{VAC} \pm 5\%$ (or $415/240\,\text{VAC}$), $50/60\,\text{Hz} \pm 0.2\,\text{Hz}$ | Simultaneous loss of voltage on both Bus A and Bus B for $> 0\,\text{ms}$ (or ITIC/CBEMA curve violation) |
| **Whitespace Air Supply** | $50\,\text{mm}$ in front of Server Rack Intake Bezel ($0.3, 1.2, 1.8\,\text{m}$) | ASHRAE Recommended: $18.0^\circ\text{C}$ to $27.0^\circ\text{C}$; Dew Point $5.5^\circ\text{C}$ to $15.0^\circ\text{C}$ ($\text{RH} \le 60\%$) | Sustained intake temperature $> T_{\text{SLA, max}}$ (e.g., $27.0^\circ\text{C}$ or $32.0^\circ\text{C}$) beyond contracted grace dwell |
| **Secondary Liquid Supply** | Outlet of Facility CDU / Rack Supply Manifold FD83 Coupling | ASHRAE W3/W4 Warm Water: $30.0^\circ\text{C}$ to $35.0^\circ\text{C} \pm 1.5\,\text{K}$; $T_{\text{sup}} \ge T_{\text{dp}} + 2.0\,\text{K}$ | Supply temperature $> T_{\text{SLA, max}}$, condensation below dew point, or $\Delta P_{\text{manifold}} < \Delta P_{\text{min}}$ |
| **Physical Security & Escort** | Mantrap Biometric Turnstile & Data Hall Cage Door | Dual-factor authenticated access log + continuous camera retention ($\ge 90\,\text{days}$) | Unescorted third-party entry or unlogged physical access to customer cage |

### Psychrometric Dew-Point Margin Mathematics

On humid summer shifts or during ultrasonic humidifier valve faults, the most immediate threat to a liquid-cooled or cold-aisle data hall is surface condensation on uninsulated manifolds and server intakes. The shift manager continuously monitors the psychrometric dew-point temperature ($T_{\text{dp}}$), approximated via the Magnus-Tetens formulation from dry-bulb temperature $T$ ($^\circ\text{C}$) and relative humidity $\text{RH}$ ($\%$):

$$\gamma(T, \text{RH}) = \frac{a \cdot T}{b + T} + \ln\left(\frac{\text{RH}}{100}\right), \qquad T_{\text{dp}} = \frac{b \cdot \gamma(T, \text{RH})}{a - \gamma(T, \text{RH})}$$

Where $a = 17.27$ and $b = 237.7^\circ\text{C}$. Every liquid CDU secondary supply setpoint must satisfy the hard anti-condensation inequality $T_{\text{CDU, supply}} \ge T_{\text{dp, hall}} + 2.0\,\text{K}$ at all times.

## Calculating Financial SLA Credit Exposure vs. Proactive Load Curtailment

Understanding how physical boundary excursions translate into commercial SLA service credits allows the shift manager to prioritize emergency actions rationally. Most hyperscale and enterprise colocation leases structure availability guarantees around a multi-tier credit multiplier applied to monthly recurring charges ($\text{MRC}$):

$$\text{SLA Availability (\%)} = \left( 1 - \frac{\sum t_{\text{outage\_minutes}}}{T_{\text{month\_minutes}}} \right) \times 100\%$$

Because a single $5$-minute dual-bus power interruption ($99.988\%$ monthly availability) frequently triggers a $10\%$ to $25\%$ monthly fee credit—and a second excursion in the same quarter can trigger contract termination rights—preserving continuous demarcation delivery always takes absolute precedence over completing scheduled preventive maintenance.
