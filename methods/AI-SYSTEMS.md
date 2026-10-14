# AI systems and research tools: contribution register

[AI-use log](../AI-USE-LOG.md) · [Detailed disclosure](AI-DISCLOSURE.md) · [Task-level records](ai-activity.json)

This register describes use in this research repository. It separates direct model assistance, author-supplied outputs, prepared tools, and deterministic execution. A product mentioned in a discussion has not necessarily been used. The record covers known activity through this writing and documentation update; missing historical traces remain missing.

| System or tool | Recorded role | Use status and evidentiary limit |
| :--- | :--- | :--- |
| ChatGPT, OpenAI | Candidate analysis and prose, source-retrieval assistance, English paraphrase, editorial critique, code and documentation | Direct assistance in the recorded October work and this revision. Exact backend deployment identifiers, token usage, and costs were not exposed as auditable results. AI-authored judgments remain reviewable candidates. |
| Codex, OpenAI | Earlier repository engineering and Assignment 1 drafting/checking | Use reported in the dated September log. This entry neither reruns that work nor relabels the current connected-tool session as a separate Codex execution. |
| Perplexity | Editorial critique and framework suggestions supplied by Mark | Historical supplied output was used in Assignment 1 revisions. No direct Perplexity call occurred in this update. A supplied critique is not an independent source check. |
| Otter.ai exports | Supplied lecture transcripts and summaries | Input artifacts, not a transcription service invoked in this update. Transcript wording, speaker identity and summary coverage retain their recorded limits. No audio was inspected here. |
| TypeSafe Jev | Optional claim-support diagnostic adapter and synthetic test setup | Prepared and off by default. Zero live Jev calls are recorded for this study through this update. Synthetic fixtures and mock responses are test data, not empirical evaluation results. |
| Research-to-Decision Translator | Source-to-claim, bounded-task, evaluation and human-decision record pattern | Adaptation of an existing repository pattern. The upstream runtime was not installed or executed here. It is workflow infrastructure, not another model or an independent reviewer. |
| Claude and SciSpace | Previously discussed possible tools | No use recorded for the documented memo work or this update. This is a statement about available records, not Mark’s use of those products elsewhere. |
| Python, Git, GitHub connector and GitHub Actions | Hashing, comparison, serialization, inventory, tests, repository operations and release packaging | Deterministic execution where specified. AI may author the code and interpret results; the executed checks themselves do not make scholarly judgments. |

## Recording rules

Each new use identifies the task, input and output versions, system/provider, access channel, source locators where relevant, exact model identifier when exposed, settings when known, retained and rejected contributions, performed checks, failures, and human-review status. Record unavailable fields as unknown rather than reconstructing them.

For an author-supplied model response, record both the provider named by the author and that the output was supplied rather than invoked here. For a tool prepared but unused, record preparation separately from execution. State the scope of a zero-use claim and update it when live use occurs.

“Checked” requires a named activity and scope: a script matched hashes; the assistant compared a claim with a supplied passage; or a named human reviewed the identified version. Agreement among models is a diagnostic result, not source independence. An AI-written check cannot be recorded as Mark’s personal verification.

No fieldwork, interviews, community consultation, environmental measurements, course submission, or human scholarly approval occurred in this writing update. Existing research evidence and its limits remain unchanged. Public sharing requires its own review under the [publication policy](../governance/PUBLICATION.md).

## Visitor-edition update

The visitor-facing README and guide were AI-authored in ChatGPT. Web retrieval supplied the bounded original-judgment and METR-method checks recorded in the visitor audit; web retrieval is an access channel, not an independent reviewer. Python generated record counts and documentation checks. These additions are documented in `ACT13`–`ACT15` in the [activity record](ai-activity.json).

No additional model provider was invoked, no live Jev evaluation occurred, and the upstream Translator was not executed in this increment. The [measurement protocol](MEASUREMENT.md) specifies future comparisons without reporting them as performed experiments.

## Regular public-checkpoint publication

For `v0.3.0`, ChatGPT authored release and onboarding prose and repository-operation instructions. Python, Git, the GitHub connector and GitHub Actions supplied the documented deterministic checks and delivery operations. Web retrieval was limited to official GitHub release documentation. This is a continuation of the existing tool roles; no additional model provider was invoked.

`ACT16` and `ACT17` in the [activity record](ai-activity.json) preserve the baseline and execution boundaries. No auditable backend deployment ID, token total or cost was returned for these tasks. Human scholarly acceptance remains separately recorded. Jev and the upstream Translator were unused in this publication step.

## Course-reading execution update, 14 October 2026

The earlier Translator entries above describe earlier increments. In this increment, its pinned source was retrieved and five original validation scripts ran over eleven AI-authored candidate source packs: 55 completed schema checks. The upstream provider-backed agent runloop was not invoked. Translator is deterministic workflow software in this exercise, not an additional model or an independent scientific reviewer. Python checked each uploaded PDF hash; ChatGPT read source text and selected images and authored the candidates. The [receipt](../research/course-readings/translator-execution.json) and [execution explanation](../research/course-readings/TRANSLATOR.md) define exactly what occurred. Human review remains pending.

## Additional execution after interrupted transfer

ACT21 adds a repeat 55-check structural run and eleven original upstream PDF-intake commands. The intake CLI uses `pdftotext` and writes templates; it does not call an AI model. North yielded an empty extraction and remains visually read. Raw PDFs, full extractions and generic CLI templates stay outside public Git. The [completion record](../research/course-readings/completion-checks.json) gives counts, hashes and failures. No provider-backed agent loop, live Jev call or human gate ran.
