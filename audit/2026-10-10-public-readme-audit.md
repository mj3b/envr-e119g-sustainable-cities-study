# Public README and research-navigation audit

[Home](../README.md) / Audit · [Complete inventory](2026-10-10-public-readme-inventory.json) · [Source checks](2026-10-10-visitor-source-checks.json)

## Scope and starting point

The starting point is commit `981440ccd0cc204e591ebf6dc1d5e4480e3f96db`, release `v0.3.0-review.2`. The checked GitHub Actions artifact contains 221 tracked files, including **125 Markdown files and 19 README files**. Its SHA-256 is `ab64ec78d889eb063e201d307461b907c84b9f8034f543199b4eb05019461cd2`.

All baseline Markdown bytes were decoded and screened for the existing documentation patterns. **46 files** triggered at least one pattern. A match is a review candidate, not a confirmed error. The inventory records a disposition and inspection scope for every baseline Markdown path. AI editorial review concentrated on current entry pages, changed pages and relevant flagged passages; this was not a full factual rereading of the repository.

## Editorial decisions

The root README previously led with repository administration. The revision leads with the public problem and explains why environmental claims require different evidence at design, authorization and outcome stages. It gives non-specialists a short route into the case and draft while preserving access to technical records.

The reader's guide connects research practices to specific artifacts for potential employers and collaborators. It does not attribute every AI-assisted operation to Mark or imply that pending review has occurred.

Current indexes connect research, methods and Assignment 2. Earlier case discovery is clearly historical. The archive is logical: older files remain at stable paths, with their existing text and evidence classifications. The preceding README versions are also preserved in the tagged baseline. No file is physically relocated or deleted.

The quantitative addition comprises local method specifications and a deterministic census of named records. Missing water-demand inputs and the absence of a timed AI-productivity comparison remain explicit. Equations do not supply observations. Historical claim labels are never recoded by the counting script.

## Evidence and history held fixed

Protected research files retain their exact baseline SHA-256 values. These include the current question, Assignment 2 draft and verification notes, draft inspection register, historical source-closure report and ledger, canonical claim/source records, and human reviews.

All previous activity objects remain unchanged. The root AI-use log receives one new section before its existing coverage section; prior text is retained. Build history remains intact inside a collapsed historical section at its original path.

The separate source-check record identifies the limited original-judgment passage inspection and official METR method reading used for the public explanation. It neither resolves an underlying technical dependency nor changes a scholarly verdict.

## Visual and execution checks

The root README was visually inspected in local HTML at desktop width 1,200 pixels and mobile width 390 pixels. The reader's guide was visually inspected at desktop width. All four generated preview layouts had no page-level horizontal overflow. Tables can scroll within their containers where needed.

These previews used Mistune and installed Chromium with network requests blocked. They do not certify actual GitHub rendering, external-link availability, or mathematical typesetting. The initial default Playwright browser was unavailable; the installed Chromium executable supplied the local rendering route.

The first container call returned a client error. A later attempt to read the public Git remote failed on name resolution. Preparation used the mounted artifact after matching its digest to GitHub's record and checking the live main ref. Local Git history is a snapshot reconstruction; remote CI must inspect full reachable history.

## Reproduce the checks

```sh
python scripts/markdown_audit.py
python scripts/research_progress.py --check
python scripts/publication_check.py
python scripts/assure.py --check
python scripts/assure.py
```

The actual receipt records executed checks. Exact-head PR CI and post-merge CI must pass before the working-review release is published. Neither an automated result nor repository-maintenance authorization supplies human scholarly approval.
