# Public-checkpoint publication audit

[Home](../README.md) / Audit · [Release scope](../docs/releases/v0.3.0.md) · [AI activity](../methods/ai-activity.json)

## Scope and baseline

The owner authorized `v0.3.0` as a regular public checkpoint and asked that new researchers and professional readers have an accessible entry route. This update concerns release status, navigation and disclosure. It performs no new case analysis.

The baseline is commit `0e12b7c6570d27174e25fb9727d85b271d1d32db`, root tree `183554b9fcec24bc9f4c0103480bdfa24c942546`. The mounted GitHub Actions artifact `11657390235` matched its official SHA-256, `e74a2cab09e36e4fa93a3910ab78692e67a33ab54f4b560ef2d7ebf703e54953`. Extracted file modes and bytes reproduced the exact root tree. Direct cloning failed on name resolution; local tests use reconstructed snapshot history. Full reachable-history checks must run remotely.

## Documentation screen and editorial decisions

Python decoded and screened every one of the baseline's **134 Markdown files** using `scripts/markdown_audit.py`. **53 files** triggered one or more maintenance patterns. These are candidates for contextual review. The complete screen can be reproduced from the pinned baseline; its UTF-8 JSON output SHA-256 is `82b9e50143b16734a3bedd840433cd34e9aeaec455ba51350498ac431044c6ad`.

AI read the current repository instructions, methodology, research-integrity and writing standards, entry pages, citation policy, release index and AI records. A focused search examined prerelease and version references. Historical release descriptions and research text remain as dated evidence. Current entry links, the release index and work status now lead to the regular checkpoint. The first-visit route gives new readers an order of reading without requiring software execution.

| Files | Disposition |
| :--- | :--- |
| `README.md`, `docs/START-HERE.md` | Keep the public research narrative; add limited onboarding and fixed-version links |
| `docs/releases/README.md`, `BUILD-STATUS.md` | Separate regular publication from research review; retain earlier history |
| `CITATION-POLICY.md` | Add checkpoint attribution without replacing original-source citations |
| `AI-USE-LOG.md`, `methods/AI-SYSTEMS.md`, `methods/ai-activity.json` | Add this task's contributions; preserve prior narrative and activity objects |
| `docs/releases/v0.3.0.md`, this audit | New publication scope and traceable maintenance record |
| `governance/evaluation-results.json` | Regenerate from executed checks; never fabricate a passing receipt |

All other baseline Markdown files retain their bytes. This is a documentation-consistency screen with targeted editorial reading, not a full scholarly rereading, independent usability study or semantic publication-rights audit.

## Research and history held fixed

The nine protected research hashes in the [visitor-edition inventory](2026-10-10-public-readme-inventory.json) remain binding for this change. They cover the current research decision, Assignment 2 draft and notes, its source-check register, preserved source-closure report and ledger, canonical claims and sources, and human-review receipts. Prior `ACT01` through `ACT15` objects retain every value; removing the newly inserted section from the AI-use log reproduces the prior file.

Earlier tags and release descriptions are preserved. Cleanup may remove only the newly merged publication branch after checking for unmerged work. Unrelated branches are outside this change. Source-access limitations, the exact non-claims and **B. GO — NARROWED COURT/INSTRUMENT QUESTION** remain unchanged.

## Verification and publication boundary

The delivery verifies expected input and output hashes, checks preserved research, runs the publication and assurance suite, and regenerates the actual receipt. Exact-head PR CI must pass before merge. Successful post-merge CI is required before creating the regular `v0.3.0` release with `draft=false`, `prerelease=false` and `make_latest=true`. The final GitHub publication record supplies the target commit and check identifiers; this audit alone is not a delivery receipt.

The release body uses tag-pinned file links. Its status note explicitly preserves peer-review, faculty-endorsement, source-verification and environmental-outcome limits. Official GitHub [release API documentation](https://docs.github.com/en/rest/releases/releases#create-a-release) and [release-link guidance](https://docs.github.com/en/repositories/releasing-projects-on-github/linking-to-releases) were consulted for these mechanics. No scientific source was added or revalidated.

Automated checks do not assess the substantive research argument. GitHub rendering, external-source availability and independent audience comprehension are not certified by this update. Human scholarly review remains pending; no live Jev call, upstream Translator execution or assignment submission occurred.
