# 1. The claim

A liquid cooling verification project fails during its first week when nobody writes down the exact sentence it is hired to prove. "The liquid cooling works" is not an engineering claim; it is an aspirational wish. An auditable claim sentence names the physical plant, the electrical and hydraulic duty the load bank simulates, the facility water supply boundary conditions, and the exact commercial decision the facility owner will make when the test pack is returned.

On the AI data hall projects from which this field guide is drawn, that commercial decision was whether the facility cooling infrastructure was legally and mechanically acceptable for IT deployment. It was not whether an accelerated compute chip would successfully run a distributed model training workload. It was not whether a prototype liquid load bank met manufacturing R&D standards. Those claims belong to other engineering scopes, other test benches, and other signatures.

```
+----------------------------------------------------------------------------------------------------+
| THE BOUNDARY OF THE CLAIM SENTENCE |
+------------------------------------+---------------------------------------------------------------+
| WHAT THE CLAIM LEGALLY PROVES | WHAT THE CLAIM CANNOT PROVE |
+------------------------------------+---------------------------------------------------------------+
| • CDU heat transfer at 1.2 MW duty | • Silicon compute efficiency or tensor performance |
| • Secondary pump N+1 failover speed| • Quick-disconnect long-term galvanic corrosion rates |
| • Manifold reverse-return balance | • Facility central chiller plant seasonal free-cooling PUE |
| • Enthalpy heat closure >= 97.0% | • Prototype load-bank heater element manufacturing durability|
| • 2N electrical feed transfer ride | • Facility building envelope structural wind-load compliance |
+------------------------------------+---------------------------------------------------------------+
```

## Formulating the project claim

Draft the sentence before you count load banks. The required machine count and electrical topology are consequences of the sentence, not its origin. If the claim is restricted to a single 1.2 MW in-row Coolant Distribution Unit (CDU) feeding ten 120 kW rack footprints, you do not deploy forty load banks across an entire row simply because the general contractor rented them for the month. If the claim encompasses the white space envelope—including the CRAH units or fan walls that capture the residual 15% to 20% convective air load escaped from the liquid cold plates—then the air-side thermal boundary must be explicitly stated in the claim sentence, or the test is structurally invalid.

In full facility commissioning, the Owner’s Project Requirements (OPR) is an exhaustive contractual volume. On a liquid cooling verification that commences after the facility structure and mechanical piping are already erected, you require that same governance distilled into a single, binding page:
1. What operational metrics must be demonstrated before production servers are cleared for delivery?
2. Which physical systems are inside the verification boundary?
3. Which plant systems are explicitly excluded?

If the owner already possesses an approved OPR page, audit it against the physical piping on the floor. Do not silently amend it in the margins of a field test script. If the owner lacks this document, the one-page claim is the prerequisite paper you draft and get signed in ink before uncrating a single tool. An unsigned claim guarantees that the final closeout meeting will degenerate into a dispute over what the testing party was compensated to demonstrate.

## Auditing the Basis of Design (BOD)

The Basis of Design (BOD) is the companion document. It articulates the engineering assumptions, heat transfer coefficients, and control logic intended to fulfill the owner's claim. You audit the BOD against the physical data hall as it stands, not against the preliminary design drawings.

You never average out the difference between drawing and installation. If the BOD specifies a DN150 reverse-return secondary header with 25% Propylene Glycol (PG25) fluid, and the as-built installation is a DN100 direct-return manifold charged with demineralized water and corrosion inhibitors, that discrepancy is not an acceptable "field adjustment." It is a critical design deviation that must be recorded on the claim cover before anyone plots a pump curve or declares the system "compliant."

What the verification cannot prove must sit on the same page as what it proves. It does not certify the server manufacturer's warranty. It does not accept the liquid load bank itself; that acceptance occurred under the factory protocols of Book 01, or it did not, and this verification will not quietly perform factory acceptance testing under the guise of site commissioning. It does not validate an unlisted quick disconnect coupling, an unverified biocidal chemistry, or a minimum flow floor that the project specification has failed to quantify. Those data cells remain blank until the test script cites the governing document. A blank cell is an intentional stop. An unverified number recalled from memory is a defect disguised as data.

Finally, the claim establishes the operational state of the hall:
- **Empty Hall Verification**: Conducted before any production IT hardware or live network fabric is energized in the room.
- **Maintenance Outage Window**: Conducted on an isolated loop during a scheduled facility shutdown.
- **Live Hall Proximity**: Conducted on a shared mechanical plant where adjacent rows support active production workloads.

A method statement written for an empty data hall that is applied to a live facility without explicit risk mitigation is an unapproved incident waiting to trigger a client outage. If the facility is live, the site's Standard Operating Procedures (SOPs) and Method of Procedure (MOP) protocols supersede this book, and their governing document numbers must head the claim sheet.

## Decisions to record before test start

- The signed project claim sentence, countersigned by Owner PE and Cx Lead.
- The physical equipment inventory within scope, and the list of excluded plant.
- The specific Basis of Design (BOD) revision audited, including all logged physical deviations.
- The concrete commercial decision the owner will make from the verified test pack.
- The operational state of the facility (empty, planned outage, or live data hall rules).
