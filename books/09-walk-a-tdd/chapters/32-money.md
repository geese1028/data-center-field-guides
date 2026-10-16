# 32. Cost, insurance, and models are not the opinion

A data room will contain an operating-cost sheet, an insurance summary, and a financial model that uses a load, an efficiency, and a life. You will be asked if the technical inputs are fair. Fair is a wide word. Answer the narrow one.

A load in the model is fair only if you can point to the evidence: measured and live, or a contract quantity you read, or absent. Design kilowatts are not fair by default. If the model uses design, say it uses design, and that you did not adopt it as the operating case. You do not propose a better number to be helpful. A number you invent in the margin becomes the technical case. Leave the cell as they built it, and tag it.

An efficiency, a loss, a utilization, is fair only if the basis is a document you opened or a meter you were shown. A ratio from a brochure is a brochure. Do not improve it. Do not attack it with a rule of thumb. Rule of thumb is the industry-practice word again.

Insurance is a contract about what is covered after a loss. You do not say the cover is enough. You may say whether the technical description in the proposal matches the plant you saw: the equipment class, the location class, the redundancy they described to the insurer. A mismatch is a finding if the financing relies on that cover existing as described. Adequacy of the sum is not your sentence.

Life in the model is the generation question, chapter 22. Do not let a depreciation schedule become a maintenance finding, or the reverse. They can both be written. They are not the same fact.

If they ask you to sensitize the model, refuse. Sensitivity is their case. Your case is which inputs you will stand behind, and which you will not. A table of your alternative loads is a second model with your name on it. Do not build it.

## Auditing Maintenance CapEx Reserves, PUE Power Pass-Throughs, and Insurance Limits

In institutional M&A acquisitions and project finance underwriting for mission-critical data centers, every qualitative observation recorded during the site walk must be translated into a deterministic commercial or contractual parameter for the investment committee and lending syndicate:

$$\text{CapEx}_{\text{reserve}}(y) = \sum_{k} C_{\text{overhaul}, k} \cdot \mathbb{I}(t_{\text{age}, k} + y \ge L_{\text{service}, k})$$

An observation that merely remarks on plant appearance without quantifying its impact on **Firm Deliverable IT Capacity ($\text{MW}$)**, **Single-Point-of-Failure ($\text{SPOF}$) Availability**, **Immediate Catch-Up Capital Expenditure ($\text{CapEx}$)**, or **Conditions Precedent ($\text{CP}$) / Conditions Subsequent ($\text{CS}$)** fails to protect the relying party.

| TDD Audit Evaluation Axis | Seller / Data Room Presentation | Independent Engineer Verification Protocol | Financing / Acquisition Covenant Impact |
| :--- | :--- | :--- | :--- |
| **Primary Audit Objective** | Auditing Maintenance CapEx Reserves, PUE Power Pass-Throughs, and Insurance Limits | Cross-check VDR contracts against physical nameplates & test logs | Convert unverified claims into explicit CP/CS or valuation haircuts |
| **Sampling & Evidence Rule** | Curated tour of flagship hall or summary slide | Statistical random sample ($n = \lceil\sqrt{N}\rceil + 1$) chosen by auditor | Any sample mismatch triggers expanded $100\%$ population audit |
| **Redundancy & Capacity Gate** | Nameplate sum of generators, chillers, or transformers | Derate for $99.6\%$ ASHRAE extreme wet-bulb and N+1/2N fault paths | Lock underwritten revenue model to firm derated MW ceiling |
| **Financial Protection Mechanism** | Seller warranty representation in purchase agreement | Quantify remediation cost $C_{\text{fix}}$ + schedule delay risk | Require $150\%\text{--}200\%$ cash escrow holdback at financial close |

## Decisions to record

- Model load tagged: measured, contract quantity, design, or not adopted.
- No alternative number written in the margin.
- Insurance description matched or not matched. Sum not judged.
- A request to run sensitivities, refused.
