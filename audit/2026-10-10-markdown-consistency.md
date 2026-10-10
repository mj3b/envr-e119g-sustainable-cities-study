# Markdown consistency and AI-record audit

[Home](../README.md) / Audit · [Complete file inventory](2026-10-10-markdown-inventory.json) · [AI-use log](../AI-USE-LOG.md)

This audit covers all **121 Markdown files** in the tracked snapshot at `62ac291605b791511c4178493da3bd767bf481c0`, the `v0.3.0-review.1` checkpoint. The snapshot was obtained from GitHub Actions artifact `11651609935`; its archive SHA-256 is `be8780cb0b90d3cbe49469c83b8390b1a0f9deb88b3d20f86f6a5be425b22477`.

Python decoded and screened every Markdown file for selected naming, authority, privacy, case-selection, AI-system and version/count patterns. **52 files** triggered at least one pattern. These are review candidates, not 52 confirmed errors. AI review focused on the flagged passages, current entry pages and documents changed in this increment. The inventory provides a disposition for every baseline path.

## Corrections selected

The root AI-use log contained September narrative and an October pointer but lacked a current narrative account. It now links historical work to the October task records and the present editorial update. A system register distinguishes model use, supplied outputs, prepared tools and deterministic execution. Existing activity objects and the September narrative are retained unchanged.

Live citation, governance and continuity pages still contained private-repository language. Several current navigation pages also retained open-case or Assignment 1 instructions. Those operational statements are aligned with the owner’s public-sharing decision and narrowed Cerrillos review-draft scope. Earlier discovery results, assignment prose and source-closure conclusions are preserved as historical or protected records.

The writing page and active links now use Mark’s personal standard title. The provenance page retains the source packet’s original name and identifies the limits of its reconstructed teaching material. There is no global replacement of historical source names.

## Changed baseline Markdown pages

| File | Maintenance decision |
| :--- | :--- |
| `AGENTS.md` | Adds ongoing AI-record and documentation-audit maintenance to operating rules. |
| `AI-USE-LOG.md` | Adds October continuity, systems and current editorial activity; preserves the existing September narrative verbatim from Session record onward. |
| `BUILD-STATUS.md` | Adds a dated current status panel while preserving the full historical build narrative. |
| `CITATION-POLICY.md` | Removes an obsolete private-repository statement; raw-source restrictions remain. |
| `COURSE-MAP.md` | Adds session-crosswalk and coverage limits without replacing syllabus data or claiming unperformed reading analysis. |
| `MEMORY.md` | Separates current operational instructions from dated Assignment 1 preferences and obsolete case/drafting directions. |
| `METHODOLOGY.md` | Renames active writing influence and preserves source provenance. |
| `README.md` | Adds stable writing, audit and release paths without implying scholarly approval. |
| `assignments/README.md` | Updates the current assignment-navigation status without revising archived syllabus formats. |
| `assignments/assignment-01/README.md` | Adds a dated/current-state boundary to historical material; original analysis retained below the annotation. |
| `assignments/assignment-02/ai-method-notes.md` | Adds a dated/current-state boundary to historical material; original analysis retained below the annotation. |
| `assignments/assignment-02/editorial-and-integration.md` | Adds a dated/current-state boundary to historical material; original analysis retained below the annotation. |
| `audit/2026-10-09-assignment2-update.md` | Adds a dated/current-state boundary to historical material; original analysis retained below the annotation. |
| `cases/README.md` | Adds a dated/current-state boundary to historical material; original analysis retained below the annotation. |
| `docs/FACULTY-GUIDE.md` | Updates reader route and current scope to Cerrillos, with AI and editorial provenance links; course-theory statements retained. |
| `governance/AI-GOVERNANCE.md` | Links actual system roles and updates authorization without changing human gates. |
| `methods/AI-DISCLOSURE.md` | Reconciles the disclosure page with the expanded root log and system register. |
| `modules/01-theories-sustainable-development/class-01-economic-social-development/north-1994/argument-map.md` | Clarifies the date scope of an instructional case-selection reference; theory and claim records unchanged. |
| `modules/01-theories-sustainable-development/class-01-economic-social-development/sen-2000/argument-map.md` | Clarifies the date scope of an instructional case-selection reference; theory and claim records unchanged. |
| `modules/01-theories-sustainable-development/class-01-economic-social-development/synthesis/urban-application.md` | Clarifies historical scope of a generic course application without changing its concepts. |
| `modules/01-theories-sustainable-development/class-02-environmental-sustainability/costanza-daly-1992/argument-map.md` | Clarifies the date scope of an instructional case-selection reference; theory and claim records unchanged. |
| `modules/01-theories-sustainable-development/class-02-environmental-sustainability/ostrom-2009/argument-map.md` | Clarifies the date scope of an instructional case-selection reference; theory and claim records unchanged. |
| `standards/DELIVERABLES.md` | Renames the active editorial cross-reference. |
| `standards/INFLUENCES.md` | Replaces active course-labelled influence with the current standard while retaining source lineage. |
| `standards/MARKDOWN.md` | Renames the active writing link while preserving its stable path. |
| `standards/WRITING.md` | Replaces course-labelled public title with Mark’s writing and register system; extends grammar, evidence, register, revision and AI attribution rules without rebranding source teaching as original doctrine. |
| `study/RESEARCH-AGENDA.md` | Adds a dated/current-state boundary to historical material; original analysis retained below the annotation. |
| `study/RESEARCH-POSITIONING.md` | Adds a dated/current-state boundary to historical material; original analysis retained below the annotation. |

## Evidence and history held fixed

Assignment 2 review draft v0.1, its review notes and source-check record, the source-closure report and ledger, canonical claims and source registry, live review receipts, and the current research question are hash-checked against the input snapshot. This update makes no new finding about the case. The `ACT01`–`ACT08` objects retain their exact field values, including original spelling; the current coverage text explains their scope rather than silently repairing historical metadata.

The September AI-use narrative beginning at `## Session record` is preserved byte-for-byte. Human review is never inferred from an AI-authored disposition, a passing test, a release or permission to maintain the repository.

## Repeatable check and limits

From the repository root, run:

```sh
python scripts/markdown_audit.py
python scripts/publication_check.py
python scripts/assure.py
python scripts/assure.py --check
```

The first command emits a fresh JSON inventory to standard output. Save it outside the repository or give a committed audit a clear date and scope. Read each flag in context. Correct live instructions; date or annotate historical records; leave exact sources and protected exports unchanged.

For each AI-assisted documentation change, update the root log and task record. Update the systems register when a provider’s role changes. Record checks that actually ran and failures that remain. Regenerate the stored receipt after edits, then inspect CI for the exact PR head before merge. A release needs its own verified tag, commit and successful post-merge check.

The audit does not establish that every unflagged paragraph is current, every historical claim is true, or every publication right is resolved. It does not verify external links or rendered page layout. Local testing uses a reconstructed snapshot history because direct Git cloning failed on name resolution; remote CI supplies reachable-history checking. Scholarly review remains separate.
