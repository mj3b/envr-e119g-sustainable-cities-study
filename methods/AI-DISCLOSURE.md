# AI-use disclosure and contribution record

A generic statement that AI helped is insufficient for this notebook. Report assistance at the task and artifact level. Detailed records belong here; a short, accurate disclosure belongs in the assignment, subject to its instructions.

## What to record

Each activity identifies the task; tool/provider and resolved model/version when exposed; date; source IDs and pages; prompt text or its honest availability status; input/output hashes when obtainable; relevant settings; what was generated or changed; retained/rejected output; performed checks and who performed them; human-review status; and remaining uncertainty. Public prompts must be redacted when they contain restricted material. Record the redaction and retain the original separately when permitted.

Do not reconstruct unavailable historical prompts, token usage, costs, model versions, or human actions from memory. Set them to null with an explanation. Hidden model reasoning is neither required nor treated as auditable source evidence; record observable inputs, outputs, decisions, and tests.

## Current contribution boundaries

| Stage | AI role | Separate human responsibility |
| :--- | :--- | :--- |
| Exploration and case narrowing | Proposed questions, comparisons, objections, and candidate scope | Owner chose the case and authorized the narrowed inquiry |
| Source retrieval | Located URLs, read returned text, inspected identified page images, recorded failures | Check that cited originals support material submitted claims |
| Interpretation and drafting | Candidate legal paraphrases, analytical applications, draft prose | Accept, revise, or reject the argument and verify legal/linguistic meaning |
| Repository engineering | Authored code/docs, file hashing, schema and consistency tests | Review publication scope; do not confuse merge with scholarly approval |
| Translator | Workflow adaptation and example review card | Approve the bounded task and any claim-use decision |
| Jev | Protocol and optional runner only; no live results in this study | Review reference labels and approve a budgeted live pilot before results are used |
| Empirical fieldwork | None performed in this drafting session | Interviews, measurements, and community consultation cannot be implied |

Source access performed by the assistant must not be described as a human double-check. Conversely, deterministic hash or schema computation is not model judgment, even when AI authored the code or invoked it. Model-generated prose and analysis remain AI-assisted work until the author has reviewed them; editing does not erase that history.

[Activity records](ai-activity.json) distinguish contemporaneous activity from inherited source-closure reports. The [AI-use log](../AI-USE-LOG.md) adds current session records while retaining earlier narrative. The [system register](AI-SYSTEMS.md) records whether a tool was directly used, supplied through its output, prepared, or unused. Unknown historical coverage remains unknown.
