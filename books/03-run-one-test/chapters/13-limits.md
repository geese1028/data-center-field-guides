# 13. What this project does not own

This book will inevitably be misused by individuals who attempt to expand it into an exhaustive encyclopedia of all liquid cooling engineering. Establish clear professional boundaries here.

A commissioning verification project maintains legal and engineering authority only when its boundaries are sharply defined. Expanding a verification scope into adjacent engineering disciplines on the fly produces flawed testing, diluted accountability, and severe contractual disputes.

**EXPLICIT NEGATIVE SCOPE BOUNDARIES**

| WHAT THIS PROJECT VERIFIES | WHAT THIS PROJECT CANNOT AND DOES NOT OWN |
| :--- | :--- |
| • Simulated thermal heat transfer | • Book 01 Scope: Load-bank design, R&D, and manufacturing QA |
| • Secondary pump curve baseline | • Book 02 Scope: Telemetry math, anomaly detection algorithms |
| • 2N electrical feed transfer ride | • Facility Design: Architectural, structural, MEP engineering |
| • Multi-rack manifold flow balance | • Silicon Performance: GPU compute, memory bus, AI workload |
| • CDU local autonomous safety loops | • Metallurgy & Chemistry: Water corrosion, biocide (Book 08) |
| • Physical hardware alarm trips | • Next Data Hall: Extrapolated universal building code rules |

## The Dedicated Boundaries

### 1. It Does Not Own the Load Bank Design (Book 01)
This verification assumes that the liquid load bank deployed on the floor has already undergone full factory acceptance testing, chassis isolation verification, and flow bench characterization under the disciplines of Book 01. If the load bank arrives on site as an unverified prototype with leaking internal braze joints or unstable SCR controllers, the Commissioning Lead must refuse to connect it. A site commissioning campaign must never be converted into an ad-hoc equipment R&D laboratory.

### 2. It Does Not Own the Telemetry Interpretation (Book 02)
This verification logs raw physical measurements and witnessed timestamps. The algorithmic reconciliation of the flash report, changepoint analysis (FLOC/Focus), and the statistical validation of data integrity belong to the disciplines of Book 02. A stable-looking thermal curve on a BMS monitor is not an accepted pass until the raw data files pass rigorous variance and quality-bitmask audits. Conversely, the field testing team must not invent alternative, lenient acceptance criteria on site simply because client executives are observing the test.

### 3. It Does Not Own Facility MEP Design
The verification team verifies the physical plant against the approved Basis of Design. If the plant fails to maintain secondary supply temperature because the central chiller plant was undersized, or because the secondary header diameter causes excessive frictional head loss, that failure is an installation deviation or design deficiency. The verification team documents the physical performance in ink; they do not redesign the facility piping on site or issue comforting statements that the installation is "close enough."

### 4. It Does Not Own Fluid Chemistry and Metallurgy (Book 08)
The verification team audits basic fluid parameters (refractometer glycol concentration ± 0.5%, turbidity, and initial pH) as prerequisites for testing. They do not certify long-term metallurgical compatibility, galvanic corrosion rates between copper cold plates and aluminum manifolds, or biocide degradation curves. Those long-term chemical verifications belong to the disciplines of Book 08.

### 5. It Does Not Own the Silicon Compute Infrastructure
A liquid load bank simulates the bulk electrical dissipation and hydraulic pressure drop of an accelerated compute rack (such as an NVL72 footprint). It does not contain silicon microprocessors, optical transceivers, or NVLink network fabrics. A load bank that operates stably under a 120 kW thermal step has proven that the cooling loop can extract 120 kW of heat; it has not proven that a production compute rack will boot, train a large neural network, or avoid silicon thermal throttling.

### 6. It Does Not Own the Next Data Hall
The procedural workflow established in this book—the sequence of twelve products, the six-level hierarchy, the five functional roles, and the seven master sheets—can be applied universally across mission-critical facilities. However, the specific numerical parameters (the exact kW steps, dwell durations, flow tolerances, and maximum operating temperatures) are unique to the specific contract in force. Copying numerical values from this data hall into a different facility without independent engineering analysis turns this field guide into an unverified copy-paste exercise.

## Decisions to record before test start

- The load-bank factory acceptance certificate reference (Book 01), or formal refusal to connect.
- The formal data audit procedure adopted from Book 02.
- The explicit list of excluded engineering disciplines, documented on the claim sheet and reaffirmed in the final report.
