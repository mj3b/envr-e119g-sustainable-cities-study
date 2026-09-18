# Research objects: an inspectable chain of reasoning

[Home](../README.md) / [Cases](README.md) / Research objects

The [canonical register](research-objects.json) contains 44 objects across 12 types. Each has a stable ID, candidate links, supporting claim/source IDs, limitations, and human-review status. These are our authored research structures; their evidence remains in the six-class source and claim registries.

| Object | Required analytical work |
| :--- | :--- |
| Research question | Boundary, question type, answerability, revision condition |
| Hypothesis | Mechanism, prediction, disconfirmation, rival, proposed test |
| Assumption | What is assumed, how to test it, consequence of failure |
| Actor | Role, attributed position, tentative incentive, population boundary |
| Authority | Actor, action, jurisdiction, instrument and limits |
| Decision | Date, authority, action, evidence, alternatives, unresolved points |
| Timeline event | Event date, precision, decision relationship and evidence |
| Decision-time evidence | Event/publication/access dates, actor, locator and access basis |
| Measurement | Value/status, units, period, boundary, baseline, method, uncertainty |
| Contradiction | Competing assertions, comparability, resolution test and consequence |
| Alternative | Contemporaneous or analyst origin, feasibility and tradeoff |
| Outcome | Output/outcome distinction, observations, comparison and causal limit |

## Temporal discipline

Event date, publication date, and availability to a decision-maker are separate fields. A later summary may establish that an earlier action was reported. It cannot establish which evidence was available before that action. Unknown dates remain null. A private document may precede public release, so publication date alone cannot establish institutional access.

Validation rejects claims of decision-time availability without a dated decision and timely access evidence. It checks typed references and ownership, MW/MWh distinctions, unknown values, measurement cycles, and unsupported promotion of scenarios into observations. Human review uses content-bound receipts and remains pending.

## A small workflow

Add a question and the minimum objects needed to test it. Cite the existing canonical claim where possible. Register a new source and locator when the assertion is new. Create a contradiction when records disagree. Close an uncertainty only with a reason and evidence; retain the old interpretation in version history.

The [JSON Schema](../schemas/research_objects.schema.json) is the contract; [research checks](../scripts/research_checks.py) enforce relationships the schema cannot express. The readable briefs supply interpretation. No database or application service is required.

<details>
<summary><strong>Current object catalog</strong></summary>

| ID | Type | Question or record |
| :--- | :--- | :--- |
| `RQ-01` | research question | Evidence at urban commitment |
| `H-01` | hypothesis | Monitoring turns conditions into observable corrections |
| `H-02` | hypothesis | Changed operations explain apparent improvement |
| `ASM-01` | assumption | Comparable boundaries across time |
| `ASM-02` | assumption | Public availability is distinct from institutional access |
| `ACT-GA-PSC` | actor | Georgia Public Service Commission |
| `ACT-HI-COMMITTEES` | actor | Senate Energy/Intergovernmental Affairs and Agriculture/Environment committees |
| `ACT-TVA` | actor | TVA Board of Directors |
| `ACT-MLGW` | actor | Memphis Light, Gas and Water |
| `ACT-LOUDOUN-BOS` | actor | Loudoun Board of Supervisors |
| `ACT-DAL-COUNCIL` | actor | The Dalles City Council |
| `ACT-DAL-MANAGER` | actor | The Dalles City Manager |
| `ACT-DAL-PARTIES` | actor | Moraine Industries LLC and Design LLC |
| `ACT-DAL-PUBLIC` | actor | Residents contributing public comments |
| `ACT-TUC-COUNCIL` | actor | Tucson Mayor and Council |
| `ACT-PIMA` | actor | Pima County government |
| `AUTH-GA` | authority | Large-load rule authority |
| `DEC-GA` | decision | Large-load rule |
| `AUTH-HI` | authority | SCR95 SD1 recommendation authority |
| `DEC-HI` | decision | SCR95 SD1 recommendation |
| `AUTH-MEM` | authority | Initial Paul Lowery grid-service request authority |
| `DEC-MEM` | decision | Initial Paul Lowery grid-service request |
| `AUTH-LOU` | authority | County land-use amendments authority |
| `DEC-LOU` | decision | County land-use amendments |
| `AUTH-DAL` | authority | Infrastructure agreement execution authorization authority |
| `DEC-DAL` | decision | Infrastructure agreement execution authorization |
| `AUTH-TUC` | authority | City review of proposed Project Blue agreement authority |
| `DEC-TUC` | decision | City review of proposed Project Blue agreement |
| `RQ-DAL` | research question | Supply assurance and public scrutiny |
| `EV-DAL-PUBLIC` | decision evidence | Public disclosure concern before the vote |
| `EV-DAL-ASSURANCE` | decision evidence | Water-supply assurance in deliberation |
| `EV-MEM-LATER` | decision evidence | Retrospective utility account |
| `TL-DAL-01` | timeline event | Public letter predates authorization. |
| `TL-DAL-02` | timeline event | Council authorization vote. |
| `TL-TUC-01` | timeline event | City draft released |
| `TL-PIMA-01` | timeline event | Later county closing preparation |
| `MEAS-MEM-CAP` | measurement | Reported initial service capacity |
| `MEAS-MEM-SCALE` | measurement | Capacity-to-energy scale calculation |
| `MEAS-DAL-GAP` | measurement | Comparable water consumption series needed |
| `CON-DAL-01` | contradiction | Water-rights figures need reconciliation |
| `ALT-DAL-DEFER` | alternative | Defer until evidence can be examined |
| `ALT-DAL-PHASE` | alternative | Phase service with measurable conditions |
| `OUT-DAL-01` | outcome | Post-agreement water outcome remains unknown |
| `OUT-DAL-OUTPUT` | outcome | Authorization is an output |

</details>
