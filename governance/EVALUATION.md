# Evaluate the work we actually perform

[Home](../README.md) / [Governance](README.md) / Evaluation · [Run receipt](evaluation-results.json)

> **Evaluation target:** this repository's evidence workflow and outputs. The suite is not a general model benchmark, a study of learning gains, or an independent scholarly review.

## Four levels, four distinct results

| Level | Method | Current interpretation |
| :--- | :--- | :--- |
| Structural consistency | Validate schemas, references, dates, units and selection state | Reproducible software result in the run receipt |
| Failure resistance | Mutate isolated fixtures to introduce known mistakes | Whether the named control catches that mistake |
| Semantic fidelity | Human compares claims, context, editions and synthesis with originals | Pending; [review queue](REVIEW-QUEUE.md) defines the first packet |
| Research usefulness | Researcher completes realistic interpretation tasks; compare accuracy, effort and retained understanding | Not measured; no productivity or learning benefit claimed |

## Executed failure tests

The runnable tests are in [integrity tests](../tests/test_integrity.py), [research tests](../tests/test_research.py), and [assurance tests](../tests/test_assurance.py). Their current results are recorded by the assurance runner.

| Introduced mistake | Expected behavior | Limit of the test |
| :--- | :--- | :--- |
| Peer statement relabeled as assigned reading | Reject evidence-class laundering | Cannot determine who actually spoke |
| Changed claim with old approval | Reject stale content-bound receipt | Cannot authenticate the claimed reviewer |
| Later evidence labeled timely | Reject inconsistent decision/access dates | Cannot prove access from dates alone |
| MW called energy; unknown set to zero | Reject invalid representation | Cannot verify meter calibration or original measurement |
| Scenario presented as observed outcome | Reject the promotion | Cannot establish whether an observation is unbiased |
| Missing evidence bypasses case selection | Reject readiness/selection inconsistency | Cannot decide which case is intellectually strongest |
| Dead local link or altered evaluated artifact | Report broken navigation or stale evaluation | Cannot assess rendered readability or source truth |

## Repeatable run

From the repository root, install the pinned development dependency, then run:

```sh
python scripts/assure.py --local
python scripts/assure.py --check
```

The runner executes schema/structural validation, local links, privacy path/history checks, and the unit tests. `--local` additionally checks privately held source bytes against registered digests; CI cannot inspect those ignored originals. It writes a dated receipt with command results and an aggregate fingerprint of tracked and non-ignored files. The receipt excludes itself from that fingerprint.

`--check` verifies the receipt still matches the current files and reruns privacy checks because reachable Git history can change independently of file contents. It does not rerun the test suite or authenticate who generated the receipt. Regenerate after changes. CI reruns the substantive automated checks independently of the committed receipt.

The fingerprint excludes ignored private originals. Freshness alone therefore does not revalidate those bytes; repeat `--local` when original-source integrity matters. The receipt identifies that distinction in its scope.

A failed or stale run cannot support a “checks pass” statement. No command changes human reviews or gate states.

## Human evaluation protocol

Before reviewing, freeze the relevant files and identify intended use. For each queue item, inspect the original passage plus surrounding argument, compare the proposed interpretation, identify omissions, and record **accept**, **narrow**, **hold**, or **reject**, with a reason and update condition. Use **abstain** when expertise, access or evidence is insufficient.

Start with all decision-critical numerical, causal, policy and attribution claims. The queue is purposive and risk-based; a clean sample cannot certify the whole corpus. Complete source review for every claim included in a promoted brief, plus the G2 lecture-coverage audit and G3 synthesis review. Human acceptance must use the existing content-bound receipt mechanism; this document creates no approvals.

## A possible usefulness study, not yet run

Predefine realistic tasks, such as reconstructing Sen's argument or distinguishing capacity from consumption. Compare a source-only workflow with the assisted workflow on comparable material. Record support accuracy, missed qualifications, total time including verification, correction effort, and retained explanation after a delay. Avoid reusing an already learned task as a naive baseline; order and familiarity can confound the comparison.

METR's [2025 developer study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) motivates separating expectations from measured task performance. Its results do not estimate the benefit of AI for this student or research domain. No human trial, model comparison, blind rating or measured time saving has been conducted here.
