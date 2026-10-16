# 5. Change

Most catastrophic data center outages are not caused by lightning strikes, earthquakes, or manufacturer component defects. Most catastrophic outages are changes that were casually categorized as "routine maintenance."

| **CHANGE EXECUTION LIFECYCLE** |
| :--- |
| [T - 72h] Engineering Review: Risk assessment, single-point failure audit |
| ↓ |
| [T - 24h] Change Advisory Board (CAB) Sign-Off: Risk accepted in writing |
| ↓ |
| [T - 02h] Pre-Window Verification: Redundant plant 100% healthy, no alarms |
| ↓ |
| [T = 00h] Maintenance Window Opens: Abnormal state posted on shift board |
| ↓ |
| [T + Execution] Step-by-Step MOP Execution under Two-Person Rule |
| ↓ |
| [T + Verification] Functional Load Verification: Telemetry confirms service |
| ↓ |
| [T + Close] Post-Change Sign-Off: Abnormal state cleared, turnover updated |

## What Constitutes a Change

A change is any physical, electrical, mechanical, or logical action that alters:
- How the critical infrastructure fails under transient conditions.
- How the plant is operated, monitored, or controlled by technicians.
- The redundancy, capacity, or path configuration delivered to the customer.

Replacing an indicator LED with an identical factory part is maintenance, provided the task requires no electrical isolation and introduces no risk of control bus short-circuiting. Replacing a thermal-magnetic circuit breaker with one possessing a different trip curve, altering a variable frequency drive's acceleration ramp rate, modifying a Building Management System PID loop tuning parameter, or adjusting a CDU secondary loop temperature setpoint by even 0.5 K is a change.

Transferring critical server load from electrical Bus A to Bus B—even for twenty minutes—is a critical change. If an unexpected transient occurs on Bus B while Bus A is isolated, the entire facility drops. If an operational action prompts any debate over whether it constitutes maintenance or change, default immediately to treating it as a change.

## The Change Advisory Board and Risk Acceptance

Every change requires formal approval from the Change Advisory Board (CAB) prior to execution.

The CAB submission must document:
1. **The Operational Justification**: Why the change must occur. "The vendor technician was already on site for another job" is never an acceptable justification. Acceptable justifications are resolving a logged defect, accommodating contracted capacity expansion, or mitigating an identified safety vulnerability.
2. **The Operational Risk Level**: Classified according to potential customer impact:
 - **Level 1 (Critical)**: Intrusive work touching active power distribution or primary cooling loops serving production IT workloads. Requires executive operations director sign-off and mandatory customer notification.
 - **Level 2 (Major)**: Work on redundant (N+1) systems where failure of the surviving system during the window would result in customer impact.
 - **Level 3 (Minor)**: Non-intrusive work on auxiliary or support systems where physical and electrical separation guarantees zero service risk.
3. **The Risk Acceptor**: A named senior leader who possesses the contractual and financial authority to accept the risk of the change. The field technician holding the torque wrench is not the risk acceptor. If the named risk acceptor is unreachable, the maintenance window does not open.

## The Abnormal State Board

During the maintenance window, the facility enters a named, temporary **Abnormal Operating State**.

The exact nature of this abnormal state must be:
- Written prominently on the physical whiteboard in the central control room.
- Displayed on the digital Building Management System banner across all operator workstations.
- Recorded explicitly on the shift handover log.

| **CONTROL ROOM ABNORMAL STATE BOARD** |
| :--- |
| [ACTIVE IMPAIRMENT] Chiller CH-03 isolated for condenser overhaul |
| [SURVIVING REDUNDANCY] 3 of 4 chillers operating; redundancy = N+0 |
| [RISK] Loss of CH-01 or CH-02 triggers automatic load shedding |
| [WINDOW] 2026-10-14 10:00 to 14:00 UTC \| Risk Acceptor: J. Vance (VP) |
| [BACK-OUT DEADLINE] 13:00 UTC (If not re-assembled, abort and restore) |

An abnormal state that finishes in the physical sense (e.g., the mechanic tightens the final bolt) but is not formally cleared on the control room board and turnover log remains an open operational hazard. If an unexpected alarm occurs two hours later, the incoming shift will troubleshoot based on the assumption of a normal plant configuration, leading to erroneous switching decisions and cascading equipment trips.

## Pre-Window Verification and Back-Out Execution

Never initiate a change window based on the assumption that redundant systems are operational. Two hours prior to opening the window (T-2 h), the duty team must perform a comprehensive pre-window audit:
- Verify that all surviving redundant units (2N electrical feeders, N+1 chillers, standby generator sets) are online, running stably, and completely free of active or latent alarms.
- Confirm that no severe weather alerts (lightning storms, grid instability, extreme heat waves) are forecast during the execution window.
- Verify that external emergency service support (utility grid operators, fuel delivery vendors, specialized service contractors) is on standby.

Every MOP must include an unambiguous **Back-Out Deadline**. The back-out deadline is the absolute point in time during the maintenance window beyond which work must halt and the plant must be restored to its baseline configuration, regardless of progress. If a six-hour maintenance window has a two-hour restoration sequence, the back-out deadline is reached precisely four hours into the window (T+4 h). If the new component is not fully commissioned by that minute, the technician must execute the back-out procedure. Never allow a contractor to negotiate for "just thirty more minutes" while the maintenance window expires.

## Technical Verification vs. Commercial Completion

A change is not closed when the vendor packs their toolboxes, hands over an invoice, and departs the security gate. A change is closed only when the facility manager completes rigorous technical verification against the baseline SLA:
- The modified equipment has been energized and operated under live thermal and electrical load for a minimum dwell period (typically 30 to 60 minutes).
- Telemetry confirms that operating temperatures, pressures, vibration signatures, and electrical phase balances match pre-change specifications.
- All alarms that were disabled or muted during the procedure have been re-enabled and functionally verified via loop testing.
- The Sequence of Events (SOE) recorder confirms that no unrecorded transient spikes or ground faults were introduced during switching.

If technical verification cannot be completed satisfactorily, the change is formally classified as **Paused with Active Defect**, an incident ticket is generated, and the system is placed under active continuous monitoring with an assigned engineer.

## Decisions to Record

- Full registry of today's executed changes, detailing old parameter values and new parameter values.
- Name and title of the formal risk acceptor for each change ticket.
- Exact start and close timestamps for each maintenance window.
- Recorded abnormal states posted on the control room board and shift handover.
- Formal technical verification signed off under live load conditions.

## Quantitative Change Window Budgeting and Point of No Return (PONR) Governance

Every maintenance window ($T_{\text{window}}$) authorized on a live data center plant must be mathematically budgeted so that worst-case rollback completes before the customer's authorized maintenance window expires. A change window is governed by the deterministic cutoff timestamp ($t_{\text{cutoff}}$):

$$T_{\text{window}} \ge t_{\text{LOTO}} + t_{\text{work}} + t_{\text{dwell}} + t_{\text{rollback}} + t_{\text{margin}}$$

$$t_{\text{cutoff}} = T_{\text{window\_end}} - \left( t_{\text{rollback}} + t_{\text{dwell}} \right)$$

For example, during a $4.0$-hour ($240$-minute) night-shift window (`00:00` to `04:00`) where post-work thermal and electrical stabilization dwell requires $t_{\text{dwell}} = 30\,\text{minutes}$ and full multi-breaker rollback requires $t_{\text{rollback}} = 45\,\text{minutes}$, the hard abort clock is **`02:45`** ($t_{\text{cutoff}} = 04:00 - 1\,\text{h}\,15\,\text{m}$). If forward execution has not passed its verification check by `02:45:00`, the Shift Manager must call a mandatory stop and initiate rollback while 75 minutes remain in the authorized window.

| Change Window Phase | Time Allocation (4.0h Window) | Primary Engineering Activity | Gatekeeper Rule |
| :--- | :--- | :--- | :--- |
| **Phase 1: Pre-Check & Mask** | `00:00 - 00:20` ($20\,\text{min}$) | Tailboard read-back, surviving bus load check ($\le 45\%$), BMS window mask | Refuse start if surviving path load $> 45\%$ or active alarm exists |
| **Phase 2: LOTO & Isolation** | `00:20 - 00:50` ($30\,\text{min}$) | Synchronized bypass transfer, breaker racking, Live-Dead-Live check | Any unexpected relay flag triggers immediate Pre-PONR rollback |
| **Phase 3: Invasive Work** | `00:50 - 02:45` ($115\,\text{min}$) | Physical component replacement, torque checks, Megger/Hipot test | **Hard Abort Clock (`02:45`)**: Must finish before $t_{\text{cutoff}}$ |
| **Phase 4: Restoration & Dwell** | `02:45 - 03:45` ($60\,\text{min}$) | LOTO removal, phase-sync re-transfer, 30-min steady-state dwell | Unmask BMS points only after quality flag `0x00` Good is verified |

## Simultaneous Maintenance Exclusions Across Redundant A/B Trains

Under no circumstances may a Shift Manager issue concurrent work permits that touch both Bus A and Bus B (or both Primary Chilled Water Loop A and Loop B) within the same shift window—even if one task is labeled a "non-invasive visual inspection" or "panel filter cleaning." Opening a cabinet door on Train B while Train A is locked out on maintenance bypass violates physical fault compartmentalization: a dropped flashlight or bumped terminal strip in Train B immediately drops the entire facility.
