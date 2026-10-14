# 11. A Path Is Not a Cause

When an operational incident occurs, human beings experience an overwhelming psychological urge to connect data points into a narrative.

The monitoring screen displays five red icons:
1. `09:14:00` - Outside air wet-bulb temperature reached 28.5°C.
2. `09:14:05` - Chiller CH-02 compressor power surged to 450 kW.
3. `09:14:12` - Secondary CDU supply fluid temperature crept to 31.8°C.
4. `09:14:18` - An electrical feeder circuit breaker tripped on Bus B.
5. `09:14:25` - A technician badged through the security door of Switchgear Room 2.

The human mind immediately constructs a story:
> *"The hot outside weather overloaded the chiller, which caused the CDU temperature to rise, which pulled too much power and tripped the circuit breaker right when the technician opened the door."*

This is the narrative fallacy in operational engineering. It confuses temporal proximity and physical topology with physical causation.

```
+-----------------------------------------------------------------------------+
| CAUSALITY VS. TOPOLOGY |
| |
| PHYSICAL TOPOLOGY (The Path) --> Physical wires, pipes, and buses |
| Tells you what COULD interact |
| |
| TEMPORAL SEQUENCE (The Clock) --> Order of millisecond arrival |
| Tells you what happened FIRST |
| |
| ENGINEERING FORENSICS (The Cause) --> Conservation of energy, metallurgy, |
| electrical protective relay targets |
| Tells you WHY it happened |
+-----------------------------------------------------------------------------+
```

A physical path (the electrical busway, the chilled water piping header, the network cable) tells you where energy and data are capable of flowing. It does not prove that a specific energy transfer caused a failure.

## The Three Tests of Physical Causation

Before an operational review or Root Cause Analysis (RCA) may declare that Event A caused Event B, the hypothesis must pass **The Three Laws of Forensic Causation**:

### Law 1: The Strict Temporal Precedence Law
Event A must precede Event B in true, synchronized source measurement time (t_meas):

$$t_{\text{meas}}(A) < t_{\text{meas}}(B)$$

If Event A occurred at `09:14:18.045 UTC` and Event B occurred at `09:14:18.012 UTC`, Event A cannot be the cause of Event B, regardless of how neatly it fits a narrative. Verify time synchronization via PTP/IRIG-B before asserting temporal precedence.

### Law 2: The Physical Energy Transfer Mechanism
There must exist an unbroken, verifiable physical mechanism governed by the laws of thermodynamics, fluid mechanics, or electromagnetism capable of transmitting sufficient energy to induce the observed failure:
- If a breaker tripped on instantaneous magnetic overcurrent (I > 5000 A), there must exist evidence of a dead short-circuit or massive mechanical seizure. An ambient temperature increase of 0.5 K cannot induce an instantaneous magnetic trip on a 4000A breaker.
- If a pump cavitated, there must exist physical evidence that net positive suction head available ( NPSH_a) dropped below net positive suction head required ( NPSH_r). Saying the pump cavitated because *"the water was warm"* without checking the suction pressure transducer is unverified speculation.

### Law 3: Protective Relay Target Confirmation
In electrical systems, modern microprocessor-based protective relays (e.g., Schweitzer Engineering Laboratories, GE Multilin) latch explicit **Protective Relay Elements (Targets)** into non-volatile memory when commanding a trip:
- Element `50P` = Instantaneous Phase Overcurrent.
- Element `51N` = Time-Delay Neutral Ground Fault.
- Element `87T` = Transformer Differential Current Mismatch.
- Element `27` = Under-Voltage Drop.

If the protective relay latched element `51N` (Ground Fault), the cause was a breakdown of electrical insulation to earth (e.g., water ingress into a conduit or a pinched cable lug). Asserting that the breaker tripped because of *"overload from the chiller"* (Element `51P`) directly contradicts the physical relay target. The relay target is the hard evidence; the engineer's narrative is a story.

## Labeling Hypotheses in the Operations Log

During a live incident investigation, intermediate working theories are necessary to direct troubleshooting. However, every unverified theory must be rigorously labeled in the site logbook:

```
+-------------------------------------------------------------------------+
| LOGBOOK FORENSIC DISCIPLINE |
| |
| [PERMITTED FACTUAL LOG ENTRY] |
| "09:14:18.045 UTC: Breaker SWG-02-4B tripped. Relay 87T target latched.|
| Winding resistance test shows Phase B to ground resistance = 0.2 ohms. |
| CONCLUSION: Phase B internal transformer winding breakdown to earth." |
| |
| [PROHIBITED SPECULATIVE LOG ENTRY] |
| "Chiller CH-02 probably pulled too much juice because it was hot out |
| and tripped the breaker. We reset it and hope it holds." |
+-------------------------------------------------------------------------+
```

An unverified hypothesis that is written into an operational turnover report without the word **"HYPOTHESIS"** prominently stamped on it will be inherited by the morning executive meeting as an established physical fact.

Once a false narrative enters executive slide decks, it takes weeks of contentious debate to dislodge, wasting hundreds of engineering hours solving an imaginary problem while the real physical defect—a compromised cable termination or a leaking pipe seal—remains unaddressed in the whitespace.

## Decisions to Record

- The immutable distinction between physical topological paths and verified root causes.
- The mandatory extraction and recording of microprocessor relay target codes prior to any breaker reset.
- The strict requirement that all working theories be formally labeled as `HYPOTHESIS` until verified.
- The physical energy balance calculations required to substantiate any forensic RCA claim.
