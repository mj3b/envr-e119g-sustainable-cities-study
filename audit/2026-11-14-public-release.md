# Public notebook edition: scope and checks

[Home](../README.md) · [Release notes](../docs/releases/v0.4.0.md) · [AI activity](../methods/ai-activity.json)

The owner authorized public release, merge and branch cleanup on November 14, 2026. The follow-up clarified that the course-reader guide and starting guide should become Jupyter notebooks while the worked notebook should remain. This release implements that direction and publishes the current Assignment 4 research record with its limitations visible.

## What changed

The starting guide and course-reader guide are prose notebooks with navigation and reading exercises. Their former Markdown addresses remain as short pointers. The worked notebook remains byte-identical to the prior published example. It contains fictional evidence and does not supply findings about Cerrillos.

The public Assignment 4 memo preserves the v0.4 text before the AI disclosure exactly. Publication wording and links are updated, and the disclosure clarifies C11’s recorded contextual assent. The supplement retains the distinction between the original pilot and a later memo-verification run. Its selected prompt quotations are retrospective excerpts, not a complete provider-level prompt log.

The public case record preserves original candidate assessments and later AI-assisted author decisions separately. Fourteen decisions record explicit label agreement; C11 records assent inferred from “proceed” after the proposed next step. No record is promoted to automatic verification or an independent accuracy label. The current documentation removes stale requests for publication approval. Frozen outputs and dated historical records retain their original state and explanatory context.

The architecture guide maps the supplied enterprise AI checklist to actual repository components. LangGraph runs a fixed sequence over supplied annotations, and LangChain Core holds passage records. There is no deployed multi-agent service, retrieval database, web API or resident response register. The proposed register remains a research proposal. The workflow and release badges report software checks and publication versions only.

## Source and publication review

PR #21 added a bounded Module IV reading review. Codex rechecked the six private PDF identities and cited sections. The interpretations retain their modeled/observed, air/surface-temperature, source-edition and transferability limits. The earlier relevance decisions remain development history; the current short memo prioritizes Sen and the Rio study. This was AI source inspection, not independent human review or dataset replication.

The publication pass inspected added prose, notebook cells and outputs, the selected case JSON, citation metadata and workflow code. No raw course PDFs, lecture files, grades, instructor correspondence, resident identities or credentials are added. The [content manifest](2026-11-14-publication-manifest.json) binds the selected files to their publication basis and byte hashes. Historical content beyond this change receives existing automated path and limited pattern checks; this release does not certify every historical sentence or third-party right.

## Completed local checks

| Check | Result and scope |
| :--- | :--- |
| Repository tests | 105 tests passed before final assurance; the current receipt records the final full result. Tests include notebook structure, navigation and failure cases. |
| Teaching workflow | All 11 workflow tests passed. They check fixed rules and traceability, not source interpretation. |
| Notebook validation | Official nbformat validation passed for all three notebooks. The fictional code cell reproduced its saved output with socket connections blocked. No notebook was rewritten by replay. |
| Cerrillos replay | All 11 retained case-workflow tests passed and the local packet matched the original bytes. The [separate replay receipt](../research/cerrillos/assignment-04/publication-replay.json) records the environment. Portable CI comparison excludes only Python-version metadata. |
| Source review | Six Module IV PDF hashes matched their retained identities; selected passages and locators were rechecked by AI. |
| Assignment 2 | The final Markdown SHA-256 remains `0b94552fcf6bab438d39dded715587822d4186cdc932cd3670e6a0a0e23d2938`. The existing protected-record tests preserve the source-closure verdict and earlier research records. |
| Assignment 4 argument | Text before the AI disclosure matches the retained v0.4 original. Its SHA-256 is `3042b9f7cbabd91f8cde61d5d3ce40ee66b73fa0bc90559f10a551c50f3c66f9`. The release does not revise the argument. |
| Worked notebook | SHA-256 remains `d91706c2adb5d0ae5ff78672304595c12e5df7acf6079a8c2325f071b048efa3`. |
| Publication and links | Limited publication scanning, local path checks, notebook output checks and the repository assurance suite identify their actual scope in the stored receipt. |

The new notebook tests exposed an escaped-newline credential-scanning gap. The checker now scans decoded notebook strings, and a regression test exercises that failure. An existing navigation test initially expected the retired Markdown guide; it was updated to the notebook route. PR #21’s earlier CI failed because its saved assurance receipt was stale. The final edited tree receives a fresh receipt before publication.

The [assurance receipt](../governance/evaluation-results.json) records commands, results and content hashes. Its timestamp uses UTC; the task date above follows the author’s Georgia date. Reader comprehension and independent scholarly validity are not software test outcomes.

## Repository operations and provenance

The release started from remote main `7af4ef2`. The existing PR #21 source commit was merged into a clean managed worktree; older local checkouts with uncommitted work were left intact. PR #21 is expanded to cover this edition so the original commit remains in the merged history. [Pull request](https://github.com/mj3b/envr-e119g-sustainable-cities-study/pull/21) · [Automated checks](https://github.com/mj3b/envr-e119g-sustainable-cities-study/actions/workflows/validate.yml) · [Release](https://github.com/mj3b/envr-e119g-sustainable-cities-study/releases/tag/v0.4.0)

The live GitHub records establish merge, check and publication outcomes. Only integrated remote branches are eligible for cleanup. Old release tags and local uncommitted work remain preserved. Publication does not submit coursework, grant source redistribution rights or establish a measured public benefit.

## AI contribution and retained instruction

Codex and collaborating Codex agents inspected sources and repository state, authored prose and code, performed AI review and prepared release operations. The session identifies GPT-6 based Codex; an exact deployed snapshot is unavailable. Python, Git, notebook execution and CI perform the specified deterministic operations. The graphs invoke no model or Jev service in this release. No private source content is sent to a hosted tracing service.

The clarification retained in the conversation was: “Yes—convert both guides to notebooks and keep the worked notebook.” The owner also explicitly authorized merges, cleanup and release publication. These are publication instructions, not a record of independent scholarly review. ACT29 documents the current contribution without rewriting earlier activity objects.
