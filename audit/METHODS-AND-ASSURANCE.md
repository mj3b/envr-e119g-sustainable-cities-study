# Revision record · methods, course depth and assurance

[Home](../README.md) / [Build status](../BUILD-STATUS.md) / Revision record

**Baseline:** v0.1.0 (`ff057b59199e571f7c24bc325626e1c4898fe603`). **Work date:** September 17–18, 2026. **Review type:** AI-assisted repository review; human source-fidelity approval remains pending.

## Problem and change

| Baseline problem | Revision | Inspect the result |
| :--- | :--- | :--- |
| “Bridges” grouped influences without a clear analytical operation | Moved practices into task, design, evidence and review stages | [Methodology](../METHODOLOGY.md), [translator comparison](APPLIED-TRANSLATOR-AUDIT.md) |
| Reading data existed but class syntheses were thin | Reconstructed arguments, comparison, lecture contribution, rival accounts and task cards | [Module 1](../modules/01-theories-sustainable-development/README.md) |
| Six places had uneven narrative presentation | Comparable candidate dossiers with evidence gaps, population denominators and advancement criteria | [Case discovery](../cases/README.md) |
| AI-use log recorded activity without an assurance system | Added responsibility, failure controls, evaluated automation and pending semantic review | [Governance](../governance/README.md) |
| Markdown hid useful distinctions in dense prose | Added concise orientation, purposeful tables, reading paths and selective diagrams | [Faculty guide](../docs/FACULTY-GUIDE.md) |
| Repository expansion risked distracting from the deadline | Built a focused evidence packet and 900-word argument architecture | [Assignment 1](../assignments/assignment-01/EVIDENCE-PACKET.md) |

## Review findings corrected

An independent agent review found that privacy checks originally omitted untracked files that the evaluation fingerprint included. The privacy scan now includes both tracked and non-ignored untracked paths. Receipt verification also reruns privacy checks because reachable history can change without a file-content change.

The review also found an overly broad missing-link exception for the generated receipt. The exception is now restricted to the exact receipt destination. Regression tests reproduce both failure modes. The live human-review register was not modified.

The first CI run exposed a roughly two-minute clock difference between the local evaluation timestamp and the CI runner. Automated receipt validation now permits a bounded five-minute skew, with a regression test rejecting a larger future timestamp. Source chronology and human-review timestamp checks are unchanged.

Normative questions were separated from empirical falsification: values require explicit reasons and contestation; observations alone cannot settle them. No named outside organization is presented as endorsing the method.

## Presentation verification

Representative Markdown pages were parsed and rendered entirely on the local computer with document network requests blocked. Inspected layout included methodology and a reading dossier; desktop and narrow-width checks found no whole-page horizontal overflow. The local stylesheet approximates GitHub conventions. It does not verify GitHub's actual renderer, theme differences or Mermaid execution. Temporary render files remain outside the repository.

## Preserved boundaries

Source originals and canonical claims were not rewritten for this revision. Six candidates remain unselected. Actual physical outcomes remain unknown where records are missing. Assignment preparation is separate from the still-paused draft. The user supplied personal context for the packet; no additional feelings, identity or accomplishments were invented.

The [AI-use log](../AI-USE-LOG.md) documents assistance and the [evaluation receipt](../governance/evaluation-results.json) records reproducible automated results. Neither is a human approval.
