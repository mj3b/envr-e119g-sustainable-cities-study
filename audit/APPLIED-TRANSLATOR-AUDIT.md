# From source summaries to inspectable research

[Home](../README.md) / [Methodology](../METHODOLOGY.md) / Applied Translator audit

> **Finding:** the course repository already preserves sources, claims, and review boundaries. Its weakest link is the translation from a source claim into a bounded analytical task with an explicit test, result, and decision about permissible use.

| Audit boundary | Record |
| :--- | :--- |
| Course baseline assessed | [`ff057b5`](https://github.com/mj3b/envr-e119g-sustainable-cities-study/commit/ff057b59199e571f7c24bc325626e1c4898fe603), the v0.1.0 research foundation |
| Upstream reference | [Applied AI Research Translator](https://github.com/node-and-norm/applied-ai-research-translator), now titled *Research-to-Decision Translator* |
| Upstream revision | [`4e5d742`](https://github.com/node-and-norm/applied-ai-research-translator/commit/4e5d742378dd2fecbafd525eeb9754c975b83aa0), committed September 15, 2026, 03:50:29 UTC |
| Inspection date | September 18, 2026 UTC |
| Review status | AI-assisted audit; human assessment pending |
| What was checked | Method documentation, governance specifications, representative pack artifacts, and local course artifacts; upstream execution was not tested |

The comparison below describes that fixed baseline. Subsequent implementation status belongs in [Build status](../BUILD-STATUS.md); this audit retains the reasons for the revision.

## 1 · What the Translator actually contributes

The upstream method separates source capture, claim screening, task design, evaluation, execution or manual review, and human authorization. Its useful contribution here is the requirement to make each transition inspectable. A reading should produce a research operation whose inputs, output, limitations, and failure conditions a reviewer can examine. See the pinned [translation method](https://github.com/node-and-norm/applied-ai-research-translator/blob/4e5d742378dd2fecbafd525eeb9754c975b83aa0/TRANSLATION-METHOD.md).

| Upstream operation | Course baseline | Practical adaptation and completion test |
| :--- | :--- | :--- |
| Preserve the source used | Private raw archive, hashes, edition notes; external discoveries often reference-only | Keep exact editions and locators. A reviewer can identify which source state supports each material claim. |
| Screen claims before translation | Claim records and limitations; no consistent use verdict | For each selected claim, state whether it supports interpretation, evaluation design, or a case test. Record the reason when use must stop. |
| Derive a bounded task | Research questions and objects; reading packs lack task definitions | Name the question, permitted inputs, output, and excluded inference. A task can be completed without changing scope halfway through. |
| Declare evaluation first | Strong structural failure checks; no reading-level semantic acceptance plan | Specify support, qualification, edition, and attribution checks before evaluating the result. Distinguish prospective criteria from retrospective checks. |
| Preserve a worked result | The Dalles has a decision reconstruction; many class synthesis files contain only short prompts | Populate comparison tables, mechanisms, competing interpretations, and unresolved observations using existing claims. Every result identifies its evidence basis. |
| Allow negative outcomes | Unknowns and omissions retained; translation decisions mostly implicit | Record a supported narrow use, a deferred inference, or a rejected use. Each deferral names what evidence would reopen it. |
| Preserve human authority | G1/G2/G3 gates and content-bound receipts; no completed receipts | Keep AI proposals separate from human review. Approval requires an actual reviewer, rationale, and matching artifact state. |
| Reconstruct the whole chain | Source and claim links exist across canonical records | A reviewer can follow one claim through task, result, limitation, and permissible use without relying on chat history. |

The upstream [pack guide](https://github.com/node-and-norm/applied-ai-research-translator/blob/4e5d742378dd2fecbafd525eeb9754c975b83aa0/packs/README.md) distinguishes scaffolds from source-captured, claim-complete, evaluation-ready, and decision-complete packs. These are upstream maturity descriptions. The course repository should report its own achieved states rather than adopt a maturity label merely because similarly named files exist.

## 2 · Where population matters most

At the assessed baseline, the four reading packs contain argument reconstructions and notes. Several class-level synthesis files contain only a few sentences. This makes the repository's architecture more developed than the analysis a reader sees.

| Priority | Artifact needing substantive work | What a reviewer should find |
| :--- | :--- | :--- |
| First | Reading-to-task translation | A selected claim; a bounded inquiry; an observable implication or evaluative question; a worked result; a limit on use |
| First | Class synthesis and comparisons | A consequential disagreement, each author's reasoning, lecture contribution, and evidence that could discriminate between interpretations |
| First | AI assurance | Named failure cases, the check applied, observed result, unresolved semantic review, and a correction path |
| Next | Cumulative synthesis | A focused argument that develops across classes, with unresolved tensions retained |
| Next | Case evidence acquisition | Executed decisions, contemporaneous evidence, measurements, affected populations, and contrary evidence; source richness alone does not select a case |

Useful starting points are the [reading–lecture matrix](../modules/01-theories-sustainable-development/class-01-economic-social-development/lecture/reading-alignment.md), [Dalles reconstruction](../cases/worked-example.md), and [research agenda](../study/RESEARCH-AGENDA.md). They contain existing evidence relationships that can support fuller analysis without inventing new data.

## 3 · A small worked translation

**Question:** What would it take to apply Sen's warning about aggregate evaluation to the Dalles water decision?

| Element | Bounded application |
| :--- | :--- |
| Source basis | `S-01`–`S-03`: plural evaluation, the limits of a single index, and reasoning about evaluative weights; interpretation remains pending human review |
| Analytical task | Identify which decision-relevant dimensions appear in the recorded deliberation and which require additional evidence |
| Inputs | The existing Sen claim records and `CASE-DAL-01`–`CASE-DAL-03`; the November 2021 minutes at their recorded locators |
| Output | A table connecting each stated concern to the actor expressing it, its evidentiary basis, and the observation needed to assess it |
| Acceptance check | Every attributed position has a locator; author argument and local inference remain separate; disagreement is not converted into measured harm |
| Worked result from current evidence | The minutes support a vote, official supply assurances, and a public disclosure concern. They do not supply a comparable post-decision water series or an account of all affected groups. |
| Permissible use | Frame plural evaluative questions and guide retrieval; the claims do not establish that this decision reduced capabilities or water security |
| Update condition | Retrieve the executed agreement, supporting studies, affected-population evidence, and comparable measurements; then reassess the interpretation |

This is an analyst's application of Sen, not Sen's empirical finding about the Dalles. It illustrates a useful translation with a deliberately limited result. The canonical records remain in [claims](../cross-course/claims.json) and [research objects](../cases/research-objects.json); this table does not create a human approval.

## 4 · Adapt the controls proportionately

| Keep | Adapt | Leave outside this course workflow |
| :--- | :--- | :--- |
| Source-specific claims and version tracking | Safety-policy intake becomes a research-use boundary: theory, empirical evidence, forecast, institutional statement, or analyst inference | An operational agent deployment platform |
| Fixed task inputs and inspectable outputs | Run artifacts can be a compact Markdown translation card with canonical links | Duplicate JSON files for every paragraph |
| Acceptance, failure, and abstention conditions | A normative theory can guide evaluation without becoming a falsifiable causal estimate | Claims that every source must yield an executable task |
| Human decisions and retained corrections | Release authorization, source fidelity, and assignment submission remain separate decisions | Automatic approvals inferred from a successful release |

The upstream [human-gate specification](https://github.com/node-and-norm/applied-ai-research-translator/blob/4e5d742378dd2fecbafd525eeb9754c975b83aa0/docs/specifications/human-gate.md) distinguishes proposals from authorized outputs. It also says its implementation centers acceptance, override, and rejection; explicit abstention is described as a future schema extension. A documented design state should therefore not be described as an enforced software capability without inspecting and testing its implementation.

The course's automated checks establish structural consistency and detect selected failure patterns. They cannot authenticate a reviewer, establish source support, measure learning, or confer doctoral research quality. Those require substantive reading, defensible inference, meaningful criticism, and actual human judgment.

## 5 · Source quality and verification limits

The upstream materials are a methodological reference, not independent validation of this repository. For example, the inspected [human–AI collaboration claims pack](https://github.com/node-and-norm/applied-ai-research-translator/blob/4e5d742378dd2fecbafd525eeb9754c975b83aa0/packs/haic_reliance_review_59e257ff/claims.json) contains provisional search hints where exact evidence locations still need refinement. The course should retain its stronger requirement for page or timestamp support. The [provenance guidance](https://github.com/node-and-norm/applied-ai-research-translator/blob/4e5d742378dd2fecbafd525eeb9754c975b83aa0/docs/governance/research-provenance.md) usefully names the hazards of source laundering, version ambiguity, and context loss.

<details>
<summary><strong>Verification record: supplied archive against current upstream</strong></summary>

The supplied archive's SHA-256 is `3cca440700f71292b208adf4180b30a61b079879f534cf51216868fa768a7d1a`.

Git blob hashes computed from the following archive members matched GitHub's recursive tree at the pinned commit:

- `TRANSLATION-METHOD.md`
- `GOVERNANCE-MODEL.md`
- `docs/specifications/artifact-model.md`
- `docs/specifications/human-gate.md`
- `docs/specifications/abstention-model.md`
- `docs/governance/research-provenance.md`
- `docs/governance/online-research-controls.md`
- `packs/README.md`
- `packs/haic_reliance_review_59e257ff/claims.json`

This verifies the selected local texts against the upstream revision. It is not a whole-repository equivalence check, an execution test, or a finding about the effectiveness of the method.

</details>
