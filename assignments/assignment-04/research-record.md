# Research Record and AI Use Supplement

Mark Julius Banasihan · November 15, 2026 · Companion to Assignment 4 v0.7

This document edition incorporates the [final pressure test](../../audit/2026-11-14-assignment4-final-pressure-test.md) and the [Section S3 evidence update](../../audit/2026-11-15-assignment4-study-evidence.md). The [v0.4.0 release](../../audit/2026-11-14-public-release.md) preserves the earlier repository edition. Source corrections do not rewrite frozen claim-review records.

## S1. From the research question to a reviewed claim

This record lets a reader inspect how the memo was developed without running software. Section S1 explains the workflow and checks; S2 follows two claims to their evidence; S3 presents retained study instructions, a historical model prompt and critical outputs. Section S4 identifies AI contributions and provides three notebook links for exploring the public study. The main memo stands on its cited sources.

**Figure S1. Where interpretation and review occur**

Specification → Source and page → AI-assisted annotation → Fixed-rule graph → Human decision

Define scope and labels → Preserve wording and context → Explain each claim–passage relation → Prepare candidate results → Record assisted review separately

LangChain Core structures the passage records. LangGraph sequences the rule-based checks. The graph makes no model calls. AI interpretation occurs in preparing annotations outside the graph. Human review does not automatically turn a candidate claim into a verified finding.

The specification defines the input fields, labels, traceability requirements and review boundary before execution. Each claim is split into clauses, linked to locatable passages and assessed against those passages. Supported means the selected evidence supports the claim. Contradicted requires opposing evidence. Insufficient records unresolved support. An absent measurement does not, by itself, contradict a claim that an event occurred.

**Table S1. Completed checks and what they establish**

| **Check** | **Observed result** | **Limit** |
| --- | --- | --- |
| **Software behavior** | **All 11 existing tests passed in the isolated November 14 rerun.** | **Tests cover rules, input validation, traceability and review routing. They do not establish interpretation accuracy.** |
| **Reproducibility** | **Two November 14 runs produced identical packets, matching the frozen packet.** | **The same encoded judgments reproduced. This is not independent confirmation.** |
| **Source-file identity** | **All eight registered source hashes matched retained files.** | **Three source records had no registered byte hash. Matching bytes does not validate meaning.** |
| **Human claim review** | 14 explicit label agreements; C11 recorded as contextual assent to “proceed.” | All decisions followed AI suggestions and translations. No independent reviewer is recorded. |
| **Preservation** | **Frozen study records and both Assignment 2 v0.11 locks matched.** | **This checks file identity and separation of revisions.** |

## S2. A worked review and a contrasting result

**C14 is a proposition being tested.** “After the 2022 proposal, the air-cooled system was installed and yielded measurable water savings for nearby users.” The claim combines installation and benefit. Each needs evidence.

The court’s Spanish wording describes the expected effect of the cooling proposal. A newly rechecked excerpt reads, “lo cual derivaría en la eliminación del consumo de agua subterránea, respecto de los tres pozos sobre los cuales cuenta con DAA.” An AI-assisted English translation is “which would result in eliminating groundwater consumption in relation to the three wells for which it holds water-use rights” (Segundo Tribunal Ambiental, 2024, consideration 93, p. 64).

The conditional derivaría describes a proposed effect. Installation and measured outcomes require other evidence. The translation and AI paraphrase remain separate.

**Table S2. Following C14 from clauses to a human decision**

| **Step** | **Retained record** | **Implication** |
| --- | --- | --- |
| **Installation clause** | **C14-A. Proposed system was installed. Passage P07 is coded context_only.** | **The proposal supplies context. Installation remains unestablished.** |
| **Benefit clause** | **C14-B. Measured savings reached nearby users. P07 and P10 are coded context_only.** | **Expected design effects and assessment findings are not measurements of benefit.** |
| **Exact graph result** | **candidate_label = Insufficient. rule = a_clause_remains_unresolved. review_status = pending_human_review.** | **The graph applies the supplied relations and queues review.** |
| **Author decision** | **Mark recorded Insufficient after seeing the Spanish, translation and suggested label.** | **The separate human-review record identifies assistance and its limits.** |

The original graph packet records the output stage. Mark’s later decision is preserved separately, retaining the sequence of AI interpretation and human review.

**C02** tests whether Resolution 532 found the request timely and granted participation. The signed decision states “por lo que resulta extemporánea” (“and is therefore late”) and orders “Declarar inadmisible la solicitud de realización de un proceso de participación ciudadana” (“Declare inadmissible the request to conduct a public participation process”) (SEA, 2019b, consideration 5 and operative provision 1). Mark accepted Contradicted after AI assistance.

The tribunal found SEA’s denial of interested-party status erroneous but nonessential because SEA had considered the substance (Segundo Tribunal Ambiental, 2024, considerations 18–20, pp. 15–16).

Source attribution. Resolution 524/2020 is cited to the Commission named on its cover and signatures (pp. 1, 36). The judgment calls it a SEA Executive Directorate decision (pp. 2, 4). This discrepancy remains documented; the original instruments are preserved.

## S3. Study instructions and critical outputs

The records below show an earlier model-facing diagnostic and the separate Cerrillos workflow. The diagnostic tests the distinction between missing evidence and contradiction. The case examples show how the study preserves that distinction in its annotations and executable rules. Exact excerpts are identified by their source artifact; a complete original Codex prompt transcript is unavailable.

**An actual model prompt from the earlier Jev diagnostic**

In the October 15 diagnostic (October 16 UTC), H16-C sent Jev-1.13.0 an AI-authored instruction that included this exact passage:

> “First distinguish a statement about what a document contains from a statement about what happened in the world. Missing, omitted, unreported or not-included evidence leaves the event unresolved; it does not establish that the event never happened.”

The request used a Choice question named support, with supported, contradicted and insufficient criteria. The full retained request includes those criteria and the instruction to report a candidate judgment without scholarly verification.

**Synthetic input and retained response**

> Source: “The authority approved the modification for screening purposes. No construction inspection or operating measurements are included.”
> Claim: “Water savings from the modification were measured.”

Jev returned choice = contradicted. Its probability fields were supported = 0.00, contradicted = 0.79 and insufficient = 0.21; its separate confidence field was 0.69. The request completed with HTTP 200 and was routed to human_review_required. These are reported API fields, not calibrated accuracy estimates.

The frozen, AI-authored expectation was Insufficient. The excerpt omits measurements; it does not expressly deny that measurements occurred. The disagreement illustrates a consequential limit of typed model output. This individual-clause expectation had no independent human approval, and one selected diagnostic supplies no general error rate. The passage is invented test material, not evidence about Cerrillos.

The archived request and response hashes were reproduced during this revision. The [selected technical record](https://github.com/mj3b/envr-e119g-sustainable-cities-study/blob/main/assignments/assignment-04/selected-jev-diagnostic.json) preserves the exact prompt, option criteria, response bytes, model identifier, expectation and hash method. No new Jev call was made.

**The Cerrillos instructions and structured evidence**

The 15-claim Cerrillos pilot made no model calls inside LangGraph. Codex prepared the evidence relations outside the graph. Its retained specification gives this exact research instruction:

> “Inspect primary Spanish records at the named locators. Write bounded English paraphrases, retain decisive Spanish phrases in the study note, and mark the relationship of each passage to the claim as supports, contradicts or context_only.”

This is specification text, not an executed API prompt. Each annotation records a clause ID, passage ID, relation and rationale. Each passage carries its source ID, locator and quotation-or-paraphrase status. The [original specification](https://github.com/mj3b/envr-e119g-sustainable-cities-study/blob/v0.4.0/research/cerrillos/assignment-04/SPEC-original.txt) and [case inputs](https://github.com/mj3b/envr-e119g-sustainable-cities-study/blob/v0.4.0/research/cerrillos/assignment-04/cases.json) remain inspectable.

**Table S3. What the recorded inputs produce**

| Claim | Evidence distinction | Exact candidate output |
| --- | --- | --- |
| C03: representation | The claim about the RCA’s wording is supported; representation of every affected group remains unresolved. | C03-A: Supported. C03-B: Insufficient. Claim: Insufficient; a_clause_remains_unresolved. |
| C12: court remedy | Partial annulment is supported. Immediate execution conflicts with the suspension requirement. | C12-A: Supported. C12-B: Contradicted. Claim: Contradicted; a_clause_is_contradicted. |
| C13: water quantity | The 169 L/s figure concerns modeling and design. The linked passages do not establish operating withdrawals. | C13-A: Insufficient; no_direct_evidence. Claim: Insufficient; a_clause_remains_unresolved. |

For C13, the retained AI annotation states: “The figure is a maximum modeling input as reported by the tribunal, not an operating measurement.” It links to the judgment’s p. 61, consideration 91(2). A second link points to RCA pp. 11–12 and 16–17. The [output packet](https://github.com/mj3b/envr-e119g-sustainable-cities-study/blob/v0.4.0/research/cerrillos/assignment-04/review-packet.json) preserves these locators and annotations beside the computed result.

The [code](https://github.com/mj3b/envr-e119g-sustainable-cities-study/blob/v0.4.0/research/cerrillos/assignment-04/workflow.py) assigns Supported or Contradicted when a clause has only that direct relation; opposing direct relations or context-only evidence yield Insufficient. Any contradicted clause makes the whole claim Contradicted. Otherwise, every clause must be Supported. These rules aggregate encoded judgments; they do not independently interpret Spanish sources.

Execution record. The November 14 local rerun used Python 3.14.3, LangGraph 1.2.11, LangChain Core 1.8.0 and LangSmith 0.14.17. Hosted tracing was disabled. The later v0.4.0 [publication replay](https://github.com/mj3b/envr-e119g-sustainable-cities-study/blob/v0.4.0/research/cerrillos/assignment-04/publication-replay.json) passed 11 case tests and reproduced packet bytes, with zero model calls and no original-source hash checks. [Human decisions](https://github.com/mj3b/envr-e119g-sustainable-cities-study/blob/v0.4.0/research/cerrillos/assignment-04/human-review.json) are retained separately; they followed AI suggestions and supply no blinded accuracy estimate.

## S4. Contributions and a route into the wider record

**Table S4. AI assistance and human responsibility**

| **Contributor or tool** | **Role in this work** | **Boundary** |
| --- | --- | --- |
| **Mark Julius Banasihan** | Selected the question, supplied reflection and directed reviews and revisions. | Authorized public release. Case reviews remain AI-assisted; C11 records contextual assent. |
| **OpenAI Codex and collaborating agents** | **Assisted with source inspection, translation, interpretation, research design, annotation, code, writing, critique and figures.** | **The session identifies GPT-6 based Codex. Exact deployment, settings, usage and cost are unavailable as auditable records.** |
| **Earlier ChatGPT discussion** | **Informed the earlier research workflow. Mark reported the label GPT 6 Pro.** | **Historical user-reported metadata does not identify this revision’s model.** |
| **LangChain Core and LangGraph** | **Structured evidence and ran a local, fixed-rule workflow.** | **These libraries supplied no independent source judgment.** |
| **Jev and other earlier tools** | **Earlier work explored Jev and inspected other research software.** | **No Jev, REA, IRIS or Holistic AI inference contributed to this rerun. Earlier results retain their own scope.** |

No fieldwork, interviews, community consultation or environmental measurements were conducted. Case decisions followed AI suggestions and translations; no independent reviewer is recorded. AI also performed source and method critiques. Passing tests and matching files do not establish scholarly correctness.

Explore the study online. The [public repository](https://github.com/mj3b/envr-e119g-sustainable-cities-study) contains the memo, evidence trail and AI-use records (Banasihan, 2026). The [v0.4.0 release](https://github.com/mj3b/envr-e119g-sustainable-cities-study/releases/tag/v0.4.0) fixes the edition linked below. All three notebooks can be read on GitHub without running code.

[1. Start here](https://github.com/mj3b/envr-e119g-sustainable-cities-study/blob/v0.4.0/docs/START-HERE.ipynb) introduces the question, evidence and research limits.

[2. Course-reader guide](https://github.com/mj3b/envr-e119g-sustainable-cities-study/blob/v0.4.0/docs/FACULTY-GUIDE.ipynb) offers a ten-minute route through the assignments, argument and disclosure.

[3. Worked example](https://github.com/mj3b/envr-e119g-sustainable-cities-study/blob/v0.4.0/methods/evidence-review/trace-a-claim.ipynb) demonstrates claim review using fictional records; it supplies no Cerrillos findings.

For the actual case, follow the [15 claim reviews](https://github.com/mj3b/envr-e119g-sustainable-cities-study/blob/v0.4.0/research/cerrillos/assignment-04/README.md) and original Spanish links. Raw course PDFs, grades, private correspondence and resident-identifying attachments remain excluded. Repository: [github.com/mj3b/envr-e119g-sustainable-cities-study](https://github.com/mj3b/envr-e119g-sustainable-cities-study).

The disclosure uses ACM, IEEE and Nature Portfolio policies and Cwik’s documentation framework, with November 13 access qualifications retained in the activity record. These policies were not reverified for this update. No publication venue is selected; course instructions govern this assignment.

## Supplementary References

Association for Computing Machinery. (n.d.). *Policy on authorship*. [Official policy](https://www.acm.org/publications/policies/new-acm-policy-on-authorship).

Banasihan, M. J. (2026). [Water, digital infrastructure and public accountability (Version 0.4.0)](https://github.com/mj3b/envr-e119g-sustainable-cities-study/releases/tag/v0.4.0) [Research repository and notebooks]. GitHub.

Cwik, J. C. (2026). Disclosure is not documentation: An open science framework for documenting generative AI use in scholarly research and publication workflows. *Research Integrity and Peer Review, 11*, 47. [https://doi.org/10.1186/s41073-026-00245-8](https://doi.org/10.1186/s41073-026-00245-8).

IEEE. (n.d.). *Author guidelines for artificial intelligence generated text*. [Official guidance](https://open.ieee.org/author-guidelines-for-artificial-intelligence-ai-generated-text/).

LangChain. (n.d.). *LangGraph* (1.2.11) and *LangChain Core* (1.8.0) [Software versions in the recorded rerun]. [LangGraph](https://github.com/langchain-ai/langgraph) · [LangChain](https://github.com/langchain-ai/langchain).

Nature Portfolio. (n.d.). *Artificial intelligence*. [Editorial policy](https://www.nature.com/nature-portfolio/editorial-policies/ai).

Servicio de Evaluación Ambiental. (2019b, September 9). *Resolución Exenta N.º 532* [Signed decision]. Consideration 5 and operative provision 1. [Official record](https://seia.sea.gob.cl/documentos/documento.php?idDocumento=2144189815). The memo also cites its September 24 official notice.

Sen, the Rio article, the tribunal judgment, ChatGPT and Codex are listed in the main References. The study’s case cutoff remains the 2024 original-approval record. This supplement does not establish the current status of every later proposal.
