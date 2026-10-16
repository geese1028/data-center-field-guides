# 7. A drawing is not a capacity

The number they want in the capacity cell has a source, a date, and a unit, or it does not go in the cell. A nameplate, a design kilowatt, a redundancy graphic, and a tier picture are not that number. The fifth book already said what the cell is for. This chapter says you do not sign a handover that fills the cell from the drawing because the measured point was inconvenient.

Redundancy is a design claim. It is not a measured spare. N+1 on a slide does not tell you what you can still serve if one machine is down tonight. If the signature says the redundancy is proved, ask which test showed the remaining capacity, on a valid file, with the failed machine actually out. If that test is not in the pack, the redundancy sentence is refused. You may still note the design claim as a design claim, in a different sentence, so nobody pretends you ignored the drawing. Noting is not signing.

## What you refuse

A single number for the hall that adds design and measured loads. They are not the same series. Plotting them on one line is the defect. Signing the sum is the same defect with your name.

A capacity that depends on a setpoint you have not seen held. If the cooling capacity assumes a supply temperature the verification never held, the capacity is a condition, not a result. Write the condition, or refuse the number. Do not write the number and hope the setpoint is close.

A future IT load offered as present capacity. The load that is not installed is not a measurement. It may be a plan. Plans do not go in the used cell, and they do not go in the available cell unless the method that produced "available" is written and you can operate to it. If you cannot explain the method in one sentence, the available cell stays blank.

A PUE, or any ratio of the building, offered as proof the hall is efficient enough to accept. This book does not own that ratio. A ratio is not a handover test. If the contract requires one, the contract's method is cited by title in their file, not reconstructed here. You still do not sign a ratio you did not see computed from points that were live.

## What you may accept

You may accept a blank cell. Blank is honest. It is better than a design number that will be quoted for a year. Write why it is blank: measured point missing, stale, or never in the claim.

You may accept a measured value with its time, its source path, and the sentence it supports, if the sixth book's quality mark is live. One feed, one number. Do not let them roll feeds into a hall total in the meeting unless the roll-up is already a calculated point with its inputs written. A total invented on a whiteboard is a new calculation. It does not get a pen in this hour.

## Proving Nameplate vs. Derated N+1/2N Operational Capacity

### Accounting for Ambient Wet-Bulb Extremes and Harmonic Derating

In institutional data center project delivery, the transition from construction and commissioning (ASHRAE Guideline 0 / Guideline 202 Levels 1 through 5) to live 24/7 operations is governed by measurable engineering gates rather than schedule milestones. Whenever a handover package asks the receiving operations lead to certify a plant attribute, that attribute must satisfy the quantitative gating relationship:

$$P_{\text{deliverable}} = \min\left(0.45 S_{\text{2N\_bus}}, \, Q_{\text{cooling}}(T_{\text{wb, 99.6\%}})\right)$$

If any supporting evidence file, witnessed test script, or as-built redline verification falls outside its acceptance corridor, the operations representative must either issue a formal **Notice of Handover Refusal** or execute a narrow **Conditional Acceptance with 200% Retainage Escrow** that explicitly bounds the permitted operating envelope until the defect is cured and re-tested.

| Handover Audit Dimension | Contractor / Project Team Submission | Operations Gatekeeper Verification Protocol | Mandatory Refusal or Escrow Action |
| :--- | :--- | :--- | :--- |
| **Primary Governance Focus** | Leaving the Capacity Cell Blank When Only Design Drawings Exist | Independent line-by-line audit against Volumes 01–06 criteria | Strike unsupported words from certificate before signing |
| **Quantitative Proof Standard** | Summary pass/fail cover sheet or verbal assurance | Raw 1-second telemetry CSV, signed witness sheet, and field walk | Classify missing proof as Category A/B defect on Refusal Sheet |
| **Financial & Operational Lever** | Request for 100% milestone release and full load | Enforce $200\%$ retainage holdback ($E = 2.0 \times C_{\text{fix}}$) and load cap | Hold plant at zero or derated load until remediation passes |
| **Post-Meeting Custody Rule** | Unfettered contractor access to finish open work | Transition space to Operations LOTO; require approved MOP per fix | Deny unescorted access; log all post-handover interventions |

## Decisions to record

- Capacity cell: measured and live, or blank. Design written beside it, not inside it.
- Redundancy sentence refused unless a test showed the remaining capacity.
- The ratio you did not sign.
- The whiteboard total you did not accept.
