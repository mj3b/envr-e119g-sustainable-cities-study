# ENVR E-119g Sustainable Cities Study

Private study and research repository for mj3b. Classes 1 and 2 form the calibration corpus. Assignment 1 is prepared as a research use case; the memo is not drafted and geography is not locked.

## Start here

- [Course map](COURSE-MAP.md) and [methodology](METHODOLOGY.md)
- [Class 1](modules/01-theories-sustainable-development/class-01-economic-social-development/README.md) and [Class 2](modules/01-theories-sustainable-development/class-02-environmental-sustainability/README.md)
- [Evidence registry](cross-course/evidence-registry.json), [claims](cross-course/claims.json), and [concept registry](cross-course/concept-registry.json)
- [Case candidates](cases/README.md), [research bridges](bridges/README.md), and [study workflow](study/README.md)
- [Assignment 1](assignments/assignment-01/README.md) and [reflection worksheet](assignments/assignment-01/reflection-and-evidence-worksheet.md)
- [Known omissions](cross-course/omissions.json), [citation policy](CITATION-POLICY.md), and [AI use](AI-USE-LOG.md)

The six evidence classes remain distinct: assigned reading, instructor lecture, TA guidance, peer discourse, external context, and our synthesis. The syllabus has a separate administrative subtype. Records distinguish supplied editions, speaker attribution, source locators, and human review.

## Current status

The repository contains a populated calibration subset, not approved master briefs. Both class packs have pending source, lecture, and synthesis fidelity gates. Full coverage review, edition reconciliation, transcript uncertainties, and Mark’s own reflection remain open. See each pack’s omissions report. Structural validation can pass while research readiness remains pending.

## Local use

Run `python3 scripts/validate.py` to check identifiers, classes, locators, dependencies, gates, and privacy boundaries. Run `python3 scripts/status.py` for readiness. Run `python3 -m unittest discover -s tests` for failure-path tests. Optional `--local` validation checks archived file digests. The schemas document the record contracts.

Raw PDFs, lecture archives, screenshots, conversations, and extracted text are stored under ignored `private/`. A clone contains metadata and authored research artifacts only. Preserve a separate private backup of that archive; Git is not its backup. `scripts/ingest.py` safely copies a new source into the ignored archive and returns its digest without overwriting originals. Never edit the parent project’s synced sources.

Install local hooks with `git config core.hooksPath .githooks`. The pre-commit hook checks staged paths; the pre-push hook also requires the GitHub repository to remain private under mj3b. CI checks privacy and record integrity. These controls reduce accidental disclosure; repository administrators can bypass them and must preserve the privacy requirement.
