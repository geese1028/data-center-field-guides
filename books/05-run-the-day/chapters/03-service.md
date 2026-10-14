# 3. The Service You Sold

Customers do not buy your diesel fuel tanks, your titanium plate heat exchangers, or your personal dedication. Customers buy an SLA: a mathematically defined service contract guaranteeing electrical availability, thermal delivery, and escalation timing. If you cannot cite the exact clause in the master service agreement, you are operating on hearsay.

```
+-----------------------------------------------------------------------------+
| SERVICE BOUNDARY MATRIX |
| |
| Contract Parameter Guaranteed Limit Measurement Source |
| ----------------------- ------------------------- --------------------- |
| AC Power Availability 99.999% (Five Nines) Active PDU Revenue Mtrs|
| Secondary Supply Temp 25.0°C to 32.0°C (W3/W4) CDU TCS Supply RTD Tree|
| Primary Chilled Water 12.0°C to 18.0°C FWS Header Flow/Temp |
| Air Temperature (Rack) 18.0°C to 27.0°C (ASHRAE) Cold Aisle Sensors (3h)|
| Incident Notice Clock <= 15 Minutes from T-0 Client Portal & Phone |
+-----------------------------------------------------------------------------+
```

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

```
+-------------------------------------------------------------------------+
| THE 15-MINUTE NOTIFICATION WINDOW |
| |
| T = 00:00 Alarms trigger on BMS/EPMS; trip detected |
| T + 05:00 Duty Manager verifies event; stabilizes safe state |
| T + 10:00 Draft incident notification: Symptom, Time, Impacted Halls |
| T + 14:00 Notification transmitted to client technical contacts |
| T + 15:00 Contractual SLA notification deadline expires |
+-------------------------------------------------------------------------+
```

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
