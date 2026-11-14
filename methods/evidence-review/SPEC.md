# Specification for the evidence review demonstration

[Reader’s guide](../../docs/START-HERE.md) / [Evidence review](README.md) / Specification

A reader should be able to reproduce why a candidate label appeared and trace it to the passage and annotation that produced it. This specification covers a local teaching example using fictional water records. The public research record and the locked Assignment 2 memo sit outside the demonstration.

## Inputs and outputs

A packet contains the claim, its checkable clauses, the relevant passages and the analyst’s evidence links. Each link names a passage and gives an evidence relation and reason. The passage record gives the source and a locator. A valid output preserves the connection between claim, clause, passage and locator and places each candidate in a human review queue. A malformed packet should stop with a validation error.

## Requirements and acceptance checks

| ID | Requirement | Acceptance check |
| --- | --- | --- |
| ER-01 | Validate packet structure and passage references before evaluating evidence. | An invalid packet or an unknown passage reference stops the run. See `test_unknown_fields_and_relations_are_rejected` and `test_unknown_source_and_passage_are_rejected`. |
| ER-02 | Preserve the source and locator with the passage and its annotation. | A reader can follow a candidate result back to the exact passage. See `test_traceability_and_no_promotion`. |
| ER-03 | Treat silence and direct contradiction differently. | T02’s design estimate yields Insufficient for the July measurement claim. T01’s explicit statement of no July measurements yields Contradicted. See `test_case_set_replays_with_all_claims_pending`. |
| ER-04 | Match the evidence to the clause’s scope. | T03’s July measurement supports the July measurement claim. T04’s July passage, tagged as context for August, leaves the August clause Insufficient. See `test_case_set_replays_with_all_claims_pending`. |
| ER-05 | Apply the rule to each clause before giving a combined candidate. | T04’s supported July measurement clause paired with an unresolved August clause yields Insufficient for the combined claim. A clause with an unopposed direct contradiction yields Contradicted for the combined claim. See `test_compound_rules`. |
| ER-06 | Keep the workflow local and preserve the human handoff. | Replaying identical inputs produces identical results. Each result remains `pending_human_review`. The graph runs without a model call or hosted tracing. See `test_runtime_stays_local_and_disables_tracing` and `test_case_set_replays_with_all_claims_pending`. |

The analyst sets each evidence relation and explains it. For a clause, direct support alone yields Supported, direct contradiction alone yields Contradicted, and context alone or conflicting direct relations yields Insufficient. For a claim with several clauses, a Contradicted clause takes precedence. Supported requires support for every clause. Other combinations yield Insufficient.

## Plan and implementation

Validate the packet. Prepare a LangChain Core `Document` for each passage with its source and locator. Use LangGraph to run the validation, document preparation and candidate assessment steps in order. Produce the pending review result with the passage and clause information needed to check it. The teaching example provides no approval or publishing operation.

Compare the [cases](cases.json), [implementation](workflow.py) and [software tests](test_workflow.py) with the requirements before making a change. The [notebook](trace-a-claim.ipynb) lets a reader compare the cases without tracing the implementation. Run the checks described in the [guide](README.md) after any change to the cases or rules. Record the command, result and tested version.

## Limits a reviewer needs to know

Software can reproduce the result implied by the annotations. Judgments about source completeness, interpretation and policy effectiveness require their own evidence and review. A researcher should check actor, date, event, measurement and source version before relying on any claim. Two records can describe the same event, so count independent evidence only when their underlying sources are independent.

The teaching cases show how the labels work. Measuring model accuracy or assessing a real facility would require a different evidence set. Changes to a source or clause require a new evidence review and a dated explanation of the change.

## Template for the next specification

| Before implementation | Record |
| --- | --- |
| Define the task | The reader’s question, permitted inputs, output and human decision. |
| Set the boundary | The records in scope, privacy rules and conditions that should stop a run. |
| Write an acceptance check | One concrete requirement ID, a case that exercises it and the expected result. Include a failure case. |
| Map the work | Which workflow step implements each requirement and which test exercises it. |
| Record the run and handoff | Versions, commands, results, AI assistance and the human review still required. |

[Spec-first engineering guidance](https://developer.microsoft.com/blog/spec-driven-development-ai-native-engineering/) · [Research integrity protocol](../RESEARCH-INTEGRITY.md) · [AI disclosure](../AI-DISCLOSURE.md)
