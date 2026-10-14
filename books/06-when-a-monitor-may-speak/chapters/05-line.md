# 5. The Line, the Dwell, the Flap

Drawing an alarm threshold as a single, knife-edge mathematical line on an analog data stream is an engineering design failure.

An analog sensor operating in an industrial environment is naturally subject to electrical noise, thermal turbulence, and pump pressure pulsations. If a high-temperature alarm threshold is set at exactly 30.0°C without filtering, a fluid stream fluctuating between 29.99°C and 30.01°C will cross the threshold twenty times a minute.

This phenomenon—known as **alarm chattering or flapping**—floods the control room console, triggers hundreds of automated text messages, induces acute alarm fatigue, and trains operators to ignore sirens.

```
+-----------------------------------------------------------------------------+
| ANALOG THRESHOLDING ARCHITECTURE |
| |
| [HIGH-HIGH (HH)] Trip / EOP Line (e.g. 40.0°C) - Immediate Auto Action |
| |
| [HIGH ALARM (H)] SLA Warning Line (e.g. 32.0°C) |
| ^ |
| | HYSTERESIS DEADBAND ZONE (Delta-H = 2.0 K) |
| v Point must fall below 30.0°C before alarm clears |
| [RESET LINE] -------------------------------------------------- |
| |
| [NOMINAL] Normal Operating Setpoint (e.g. 25.0°C) |
| |
| [LOW ALARM (L)] Condensation Risk Line (e.g. 18.0°C) |
+-----------------------------------------------------------------------------+
```

![Thresholding Dynamics: Deadband Hysteresis and Dwell Filtering](../figures/fig-02-threshold-deadband-and-dwell-filter.png)

To prevent alarm chatter, every analog monitoring point must implement three mathematical filtering layers:
1. **Hysteresis Deadbands (Δ_deadband)**
2. **Continuous Dwell Time Windows (t_dwell)**
3. **Anti-Flap Quarantine Envelopes (N_flap)**

## The Mathematics of Hysteresis Deadbands

An alarm threshold must possess distinct activation and deactivation boundaries.

For a High Alarm condition (T_high):
- **Activation Rule**: The alarm state transitions from `NORMAL` to `ALARM` only when the measured value exceeds the upper threshold:

$$V(t) \ge T_{\text{high}}$$

- **Deactivation (Reset) Rule**: The alarm state does not return to `NORMAL` when the value dips back below T_high. The alarm remains latched until the value drops below the threshold minus the hysteresis deadband:

$$V(t) \le T_{\text{high}} - \Delta_{\text{deadband}}$$

Where:
- Δ_deadband is the configured hysteresis offset (typically 1.0 K to 2.0 K for temperature loops, and 0.2 bar to 0.5 bar for hydraulic loops).

If the High Alarm is configured at 32.0°C with a deadband of 2.0 K, the alarm triggers when temperature reaches 32.0°C. As the cooling system responds and temperature recedes to 31.5°C, the alarm **stays active**. It clears only when the temperature drops cleanly below 30.0°C (32.0 - 2.0). Hysteresis completely eliminates boundary oscillation.

## The Continuous Dwell Window

A physical parameter must demonstrate that an excursion is sustained, rather than a momentary electrical glitch or transient hydraulic wave, before waking an engineer:

$$\text{Trigger Condition}: \quad \forall t \in [t_0, \, t_0 + t_{\text{dwell}}], \quad V(t) \ge T_{\text{high}}$$

Where:
- t_dwell is the continuous dwell duration.

The value of t_dwell must be carefully matched to the physical thermal and mechanical inertia of the monitored system:
- **Secondary Cooling Fluid Temperature**: t_dwell = 10.0 s to 15.0 s. A 2-second fluid temperature spike caused by a sensor electrical blip does not threaten GPU silicon; a 15-second sustained excursion indicates true heat exchanger starvation.
- **Underfloor Air Plenum Static Differential Pressure**: t_dwell = 10.0 s. A momentary air pressure dip caused by an operator opening a containment door for four seconds must not sound a low-pressure alarm.
- **Electrical Bus Under-Voltage**: t_dwell = 0.1 s to 0.5 s (100 to 500 ms). Electrical systems possess virtually zero thermal inertia; an undervoltage condition exceeding a few cycles requires immediate protective reaction.

If a point crosses an alarm threshold and recedes prior to satisfying t_dwell, the event is archived as a transient log entry; it does not sound an audible horn or dispatch an automated page.

## The Anti-Flap Quarantine Engine

Even with deadbands and dwell delays, a severely degraded sensor—such as an RTD with a loose terminal screw vibrating against a pump frame—can oscillate violently across wide boundaries.

The monitoring engine must implement an automated **Anti-Flap Quarantine Algorithm**:

$$\text{If } N_{\text{transitions}} \ge N_{\text{flap\_max}} \quad \text{within rolling window } W_{\text{flap}}, \quad \text{engage FLAPPING\_LATCH}$$

Standard operational parameters:
- Maximum transitions allowed: $N_{\text{flap\_max}} = 4$ transitions (`NORMAL` \leftrightarrow `ALARM`).
- Rolling evaluation window: W_flap = 10 minutes.

When a point trips the anti-flap limit:
1. The point transitions into the `FLAPPING_LATCH` state.
2. Control room audible horns, automated SMS gateways, and client SLA portals for this specific point are **instantly muted**.
3. A single, high-priority **"Sensor Flap Defect"** is dispatched to the shift technician's maintenance queue: *"Point CDU-02-T_sup quarantined for excessive state oscillation. Physical wire inspection required."*
4. The analog telemetry values continue logging to disk at full resolution for diagnostic analysis.
5. The point remains quarantined until a technician physically inspects the device and a manager executes a manual unlatch command, or until the sensor demonstrates 60 continuous minutes of zero-alarm stability.

Anti-flap quarantine protects the sanity of operational personnel while maintaining complete technical accountability.

## Decisions to Record

- The explicit numerical deadband (Δ_deadband) assigned to every analog alarm threshold.
- The continuous dwell duration (t_dwell) configured per subsystem, justified by thermal/electrical physics.
- The active anti-flap quarantine limits ($N_{\text{flap\_max}} = 4$ in 10 min) enforced on the SCADA server.
- The registry of all points currently held in anti-flap quarantine, with assigned technician names.
