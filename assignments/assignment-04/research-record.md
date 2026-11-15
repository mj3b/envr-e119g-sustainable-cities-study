# Research Record and AI Use Supplement

Mark Julius Banasihan · November 14, 2026 · Companion to Assignment 4 v0.4

Publication note: the November 14 release update changes navigation and publication status. The memo’s main argument and the reported earlier rerun results are retained. [Release audit](../../audit/2026-11-14-public-release.md) documents the separate repository checks.

## S1. From the research question to a reviewed claim

This record lets a reader inspect how the memo was developed without running software. Begin with Figure S1 and the checks below. Section S2 follows two claims to their evidence. Section S3 supplies selected prompts and retained outputs. Section S4 explains AI contributions and links to the wider record. The main memo stands on its cited sources. This supplement documents the work used to prepare it.

**Figure S1. Where interpretation and review occur**

Specification → Source and page → AI-assisted annotation → Fixed-rule graph → Human decision

Define scope and labels → Preserve wording and context → Explain each claim–passage relation → Prepare candidate results → Record assisted review separately

LangChain Core structures the passage records. LangGraph sequences the rule-based checks. The graph makes no model calls. AI interpretation occurs in preparing annotations outside the graph. Human review does not automatically turn a candidate claim into a verified finding.

The specification defines the input fields, labels, traceability requirements and review boundary before execution. Each claim is split into clauses, linked to locatable passages and assessed against those passages. Supported means the selected evidence supports the claim. Contradicted requires opposing evidence. Insufficient records unresolved support. An absent measurement does not, by itself, contradict a claim that an event occurred.

**Table S1. Completed checks and what they establish**

| Check | Observed result | Limit |
| --- | --- | --- |
| Software behavior | All 11 existing tests passed in the isolated November 14 rerun. | Tests cover rules, input validation, traceability and review routing. They do not establish interpretation accuracy. |
| Reproducibility | Two November 14 runs produced identical packets, matching the frozen packet. | The same encoded judgments reproduced. This is not independent confirmation. |
| Source-file identity | All eight registered source hashes matched retained files. | Three source records had no registered byte hash. Matching bytes does not validate meaning. |
| Human claim review | The record contains 14 explicit label agreements and C11 recorded as contextual assent to “proceed,” after AI suggestions and translations. | These are AI-assisted, nonblind decisions. No independent reviewer is recorded. |
| Preservation | Frozen study records and both Assignment 2 v0.11 locks matched. | This checks file identity and separation of revisions. |

## S2. A worked review and a contrasting result

**C14 is a proposition being tested.** “After the 2022 proposal, the air-cooled system was installed and yielded measurable water savings for nearby users.” The claim combines installation and benefit. Each needs evidence.

The court’s Spanish wording describes the expected effect of the cooling proposal. A newly rechecked excerpt reads, “lo cual derivaría en la eliminación del consumo de agua subterránea, respecto de los tres pozos sobre los cuales cuenta con DAA.” An AI-assisted English translation is “which would result in eliminating groundwater consumption in relation to the three wells for which it holds water-use rights” (Segundo Tribunal Ambiental, 2024, consideration 93, p. 64).

The conditional *derivaría* describes what the proposal would do. It does not establish what was installed or measured. The original passage remains distinct from its English translation and from the retained AI-authored paraphrase.

**Table S2. Following C14 from clauses to a human decision**

| Step | Retained record | Implication |
| --- | --- | --- |
| Installation clause | C14-A. Proposed system was installed. Passage P07 is coded context_only. | The proposal supplies context. Installation remains unestablished. |
| Benefit clause | C14-B. Measured savings reached nearby users. P07 and P10 are coded context_only. | Expected design effects and assessment findings are not measurements of benefit. |
| Exact graph result | candidate_label = Insufficient. rule = a_clause_remains_unresolved. review_status = pending_human_review. | The graph applies the supplied relations and queues review. |
| Author decision | Mark recorded Insufficient after seeing the Spanish, translation and suggested label. | The separate human-review record identifies assistance and its limits. |

The stored graph status remains pending because the original output is preserved. Mark’s subsequent decision is recorded separately. Overwriting the candidate output would hide the order in which the judgment was made.

**C02 illustrates contradiction.** Its tested proposition says Resolution 532 found the request timely and granted formal participation. The signed decision instead states that it was late, “por lo que resulta extemporánea,” and orders “Declarar inadmisible la solicitud de realización de un proceso de participación ciudadana.” These mean “and is therefore late” and “Declare inadmissible the request to conduct a public participation process” (SEA, 2019b, consideration 5 and operative provision 1, signed resolution). The graph returned Contradicted, and Mark accepted that label after AI assistance. Opposing evidence supports this result. C14’s missing installation and outcome evidence supports Insufficient.

The tribunal found SEA’s denial of interested-party status erroneous but nonessential because SEA had considered the substance (Segundo Tribunal Ambiental, 2024, considerations 18–20, pp. 15–16).

## S3. Selected prompts and critical outputs

The following are verbatim excerpts of user messages recoverable from this conversation, compiled retrospectively for this revision. They are not a complete contemporaneous prompt log. Historical prompt_summary fields in the activity record are summaries. The graph itself receives structured case data and has no language-model prompt.

**Author’s drafting instruction**

“The 2019 filing stood out to me. It made me ask what happens to residents’ water concerns after the agency rules their request late. Let’s use that to draft the Assignment 4 memo. Keep Assignment 2 v0.11 unchanged.”

The first two sentences appear in Section 1 of the revised memo. Codex developed the subsequent argument and prose for Mark’s review. This distinguishes the author’s supplied reflection from AI-assisted elaboration.

**Author’s request to review C14**

“I agree, C13 is Insufficient. Record it as AI-assisted human review, then show me C14 with the original Spanish, an English translation, and your suggested label. Keep Assignment 2 v0.11 unchanged.”

**Retained AI-authored annotation for C14-A**

“The tribunal describes a proposed change, without evidence of installation.”

This exact rationale is stored in the case data. It is an AI interpretation of the passage, not a quotation from the court. The exact deterministic output fields appear in Table S2. The earlier private archive retains the complete case, source locator, paraphrase, output and later decision objects for C02 and C14; the public claim-review record supplies the selected trace.

**Author’s subsequent decision**

“I agree, C14 is Insufficient. Record it as AI-assisted human review, then show me C15 with the original Spanish, an English translation, and your suggested label. Keep Assignment 2 v0.11 unchanged.”

The sequence exposes a limitation. Mark saw the model’s proposed label before deciding. Agreement cannot be used as a blinded accuracy estimate or calibration result. No complete original assistant response or provider-level prompt chain is claimed from these selected records.

**Rerun environment.** The v0.3 verification completed November 15 at 02:26 UTC (November 14 in Georgia): Python 3.14.3, LangGraph 1.2.11, LangChain Core 1.8.0 and LangSmith 0.14.17. Dependencies passed; hosted tracing was disabled; the graph made no model or Jev calls. Its receipt preserves commands, output and hashes. Results were carried forward for the v0.4 writing revision. A separate [public-release replay](../../research/cerrillos/assignment-04/publication-replay.json) now records tests and replay of the unchanged case annotations. It does not repeat the original-source checks or change human decisions.

**Revision decisions.** After Mark reported difficulty following v0.3, this revision foregrounded learning, replaced abstract arrows with a timeline and worked register entry, and kept software details here. Earlier checks confirmed rendering; reader comprehension remained unestablished. No new environmental findings or human source-review decisions are claimed.

## S4. Contributions and a route into the wider record

**Table S3. AI assistance and human responsibility**

| Contributor or tool | Role in this work | Boundary |
| --- | --- | --- |
| Mark Julius Banasihan | Selected the question, supplied reflection, directed revisions and contributed 15 recorded case decisions, including C11’s contextual assent. | Authorized public release of this research record; no course submission is recorded. |
| OpenAI Codex and collaborating agents | Assisted with source inspection, translation, interpretation, research design, annotation, code, writing, critique and figures. | The session identifies GPT-6 based Codex. Exact deployment, settings, usage and cost are unavailable as auditable records. |
| Earlier ChatGPT discussion | Informed the earlier research workflow. Mark reported the label GPT 6 Pro. | Historical user-reported metadata does not identify this revision’s model. |
| LangChain Core and LangGraph | Structured evidence and ran a local, fixed-rule workflow. | These libraries supplied no independent source judgment. |
| Jev and other earlier tools | Earlier work explored Jev and inspected other research software. | No Jev, REA, IRIS or Holistic AI inference contributed to this rerun. Earlier results retain their own scope. |

No fieldwork, interviews, community consultation or environmental measurements were conducted for this memo. The author’s reviews cover selected claims after AI assistance. The source and method critiques performed during this revision were AI reviews. Neither matching files nor successful tests establishes scholarly correctness.

The public repository offers a [course-reader guide](https://github.com/mj3b/envr-e119g-sustainable-cities-study/blob/main/docs/FACULTY-GUIDE.ipynb), a [plain-language starting page](https://github.com/mj3b/envr-e119g-sustainable-cities-study/blob/main/docs/START-HERE.ipynb), and a [worked notebook](https://github.com/mj3b/envr-e119g-sustainable-cities-study/blob/main/methods/evidence-review/trace-a-claim.ipynb). The notebook’s demonstration is fictional. The [Cerrillos claim-review record](../../research/cerrillos/assignment-04/README.md) publishes a bounded view of the 15 case reviews with source locators and provenance. The memo and this supplement are released for public review under the author’s November 14 authorization. Course submission and independent scholarly review remain separately recorded.

The private companion archive retains the earlier verification receipt and selected prompt/output records. The public case record identifies its selection and redaction scope. Raw course PDFs, grades and instructor correspondence are excluded. The original Spanish records remain available through the memo’s references.

The retained disclosure guidance draws separately on ACM, IEEE and Nature Portfolio policies and on Cwik’s documentation framework. Their November 13 access qualifications remain in the activity record. Policies were not newly reverified for this revision. No publication venue is selected. The guidance supports recording substantive assistance and actual review; it does not certify compliance with every venue. Course instructions govern this assignment.

## Supplementary References

Association for Computing Machinery. (n.d.). *Policy on authorship*. [Official policy](https://www.acm.org/publications/policies/new-acm-policy-on-authorship).

Cwik, J. C. (2026). Disclosure is not documentation: An open science framework for documenting generative AI use in scholarly research and publication workflows. *Research Integrity and Peer Review, 11*, 47. [https://doi.org/10.1186/s41073-026-00245-8](https://doi.org/10.1186/s41073-026-00245-8).

IEEE. (n.d.). *Author guidelines for artificial intelligence generated text*. [Official guidance](https://open.ieee.org/author-guidelines-for-artificial-intelligence-ai-generated-text/).

LangChain. (n.d.). *LangGraph* (1.2.11) and *LangChain Core* (1.8.0) [Software versions in the recorded rerun]. [LangGraph](https://github.com/langchain-ai/langgraph) · [LangChain](https://github.com/langchain-ai/langchain).

Nature Portfolio. (n.d.). *Artificial intelligence*. [Editorial policy](https://www.nature.com/nature-portfolio/editorial-policies/ai).

Servicio de Evaluación Ambiental. (2019b, September 9). *Resolución Exenta N.º 532* [Signed decision]. Consideration 5 and operative provision 1. [Official record](https://seia.sea.gob.cl/documentos/documento.php?idDocumento=2144189815). The memo also cites its September 24 official notice.

Sen, the Rio article, the tribunal judgment and OpenAI Codex are listed in the main References. The study’s case cutoff remains the 2024 original-approval record. This supplement does not establish the current status of every later proposal.
