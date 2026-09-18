# AI governance and research assurance

[Home](../README.md) / Governance · [Methodology](../METHODOLOGY.md) · [AI use record](../AI-USE-LOG.md)

> **AI can assist analysis; it cannot supply its own human approval.** Automated consistency checks, substantive source review, and permission to submit are separate decisions.

| Start here | Purpose |
| :--- | :--- |
| [AI governance](AI-GOVERNANCE.md) | Roles, permitted work, failure controls and correction procedure |
| [Evaluation](EVALUATION.md) | What is tested, how results are recorded, and what remains unevaluated |
| [Human review queue](REVIEW-QUEUE.md) | Concrete high-consequence interpretations awaiting source adjudication |
| [Automated run receipt](evaluation-results.json) | Machine-readable results bound to the evaluated repository files |
| [AI use log](../AI-USE-LOG.md) | Assistance actually used, retained outputs and unresolved human review |

## Three different assurance questions

| Question | Evidence | Decision-maker |
| :--- | :--- | :--- |
| Are the records internally consistent? | Schema/reference checks, failure tests, links, privacy-path checks | Software reports the result; researcher investigates failures |
| Does the source support the interpretation? | Passage-level review, context, edition, qualifications and competing readings | Mark or an identified human reviewer |
| May this be used for the intended purpose? | Assignment policy, scope of review, unresolved limits, actual AI disclosure | Mark; course staff determine course expectations |

A passing test suite covers specified failure modes. It is not a measurement of AI truthfulness or a certification of research quality. All current human fidelity gates remain pending.
