# Sustainable Cities: evidence and research record

ENVR E-119g · Mark Julius Banasihan · Working research notebook

This repository records course study, source access, analytical revisions, and Assignment 2 preparation. It became public by the owner's explicit choice on October 9, 2026. Public availability, automated checks, and course permission to use AI do not constitute faculty endorsement or scholarly approval.

## Start with the current inquiry

[Current Cerrillos question](research/CURRENT.md) · [Assignment 2 review draft](assignments/assignment-02/review-draft-v01.md) · [Draft verification notes](assignments/assignment-02/review-notes-v01.md)

The source-closure decision remains **B. GO — NARROWED COURT/INSTRUMENT QUESTION**. The current inquiry concerns the legal treatment of environmental screening and authorization in the Cerrillos Data Center proceedings. It does not establish AI-specific demand, implemented savings, or environmental recovery.

## Inspect how the work was produced

[Research-integrity protocol](methods/RESEARCH-INTEGRITY.md) explains the source-to-claim chain, counterevidence, version limits, human review, and correction procedure. [AI-use disclosure](methods/AI-DISCLOSURE.md) distinguishes actual assistance, historical reports, planned tools, and work still requiring human verification. [Activity records](methods/ai-activity.json) are machine-readable. The [AI systems register](methods/AI-SYSTEMS.md) distinguishes direct assistance, supplied outputs, prepared tools, and deterministic execution.

The [Translator adaptation](methods/TRANSLATOR-BRIDGE.md) structures reviewable tasks. The [optional Jev experiment](experiments/jev/README.md) prepares a claim-support test; no live Jev evaluation has been performed for this study. Neither is a theory of urban development or an authority to close evidence gaps.

## Writing and documentation

[Mark’s writing rules and voice registers](standards/WRITING.md) define sentence, argument, evidence, and audience practices. [Editorial provenance](standards/WRITING-PROVENANCE.md) records the supplied reconstruction and its gaps. The [Markdown audit](audit/2026-10-10-markdown-consistency.md) separates current corrections from historical records retained unchanged.

[Writing and AI-records release scope](docs/releases/v0.3.0-review.2.md) documents this increment. Research status remains a working review record.

## Evidence and preservation

[Historical source-closure report](research/cerrillos/history/ENVR_E119g_Cerrillos_Source_Closure_Sprint.md) · [Unchanged historical ledger](research/cerrillos/history/ENVR_E119g_Cerrillos_Source_Closure_Ledger.json) · [Current inspection record](research/cerrillos/draft-source-checks.json) · [Artifact preservation index](research/preservation-index.json)

The two historical source-closure files retain their exact bytes. Their original confidence labels remain historical assessments. The current inspection record identifies precisely which original passages were revisited for the draft. The remaining earlier exports are inventoried and retained in the owner's separate archive pending item-level public-sharing review. Fingerprinting a file does not publish its contents or make it an original source.

## Course record and boundaries

[Course map](COURSE-MAP.md) · [Course-session correction](research/course-session-crosswalk.json) · [Existing methodology](METHODOLOGY.md) · [AI-use log and history](AI-USE-LOG.md) · [Public-sharing policy](governance/PUBLICATION.md)

Older documents preserve earlier case choices, private-storage rules, and preparation-only restrictions. The dated current decision supersedes those instructions prospectively; historical findings are not silently rewritten. The original course assignment prompt must be checked before submission. Raw readings, recordings, transcripts, private correspondence, and credentials stay outside Git.

## Checks

```sh
python -m pip install -r requirements-dev.txt
python scripts/publication_check.py
python scripts/assure.py
python scripts/assure.py --check
```

These checks test structure, content consistency, path/history restrictions, and local links. They cannot certify the truth of a claim, the adequacy of a legal interpretation, public-sharing rights, or substantive human review. G1–G3 and claim approvals remain human-controlled.
