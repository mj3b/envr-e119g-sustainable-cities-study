# Assignment 4 study instructions and output evidence

[Home](../README.md) / Audit · [Research supplement](../assignments/assignment-04/research-record.md) · [Selected diagnostic](../assignments/assignment-04/selected-jev-diagnostic.json)

The owner asked to remove the author's drafting instruction and repetitive label agreements from Section S3, and replace them with technical evidence from the study. Document v0.7 makes that change while retaining the memo argument, main references and formatting from v0.6. The [prior source review](2026-11-14-assignment4-final-pressure-test.md) remains the record of that earlier correction pass.

## Selected records and their scope

Section S3 now distinguishes an executed model prompt from the written instructions for the fixed-rule Cerrillos graph.

The selected H16-C diagnostic is one historical synthetic case, rubric v0.2, option order 0, from run `20261016T034529738234Z`. That timestamp falls on October 15 in Georgia and October 16 UTC. The record contains the exact Jev-1.13.0 request, its full instructions and criteria, typed response, original response bytes, recorded route and HTTP status. Jev returned `contradicted`; the frozen AI-authored expectation was `insufficient`. The individual-clause expectation was not independently approved by a human. This disagreement illustrates a limitation without supplying an independent accuracy estimate, calibration result or Cerrillos observation. No new provider call was made.

The public selection contains synthetic AI-authored source and claim text, instructions, returned fields and provenance. It excludes the other historical cases, raw course material, resident identifiers, correspondence, credentials and private host paths. The original private archive remains unchanged. Source-file hashes and record-selection fields permit comparison with that archive; they do not establish semantic validity.

The request digest was reproduced from UTF-8 `json.dumps(request, ensure_ascii=False)` with default separators and preserved insertion order. The stored response bytes were decoded and hashed, and their parsed value matched the retained response object. The selected public file records the exact methods and original digests.

| Record | SHA-256 |
| :--- | :--- |
| Selected diagnostic and provenance | `42649a184aeeaa7db8f3829567e443abca45c3035f152432bf766153de8d6f2a` |
| Original serialized request | `697d4145ade9d0f177be2b924ab024feed6351c868653e45753b6595ae0ea64f` |
| Original response bytes | `d5521664dbc44de9a025aa5e2977011156d0340175b8006f065c88dbbc1ef80f` |

The Cerrillos half quotes the retained [specification](../research/cerrillos/assignment-04/SPEC-original.txt), explains the annotation fields and shows the recorded C03, C12 and C13 clause results. These extend S2's existing C14 and C02 examples. The table values were compared with the frozen case data and output packet; the prose describing aggregation was checked against the preserved implementation. The original specification is identified as specification text. It is not presented as an executed model prompt. Complete original Codex provider prompt transcripts are unavailable and were not reconstructed.

The section links the case inputs, code, output packet, separate human decisions and publication replay. The current graph's zero-model-call boundary is preserved. No new source interpretation or human label was added to the frozen case records. The update explains retained annotations rather than revalidating the underlying Spanish instruments.

## Document checks

The first five pages, including the main memo and its references, retain identical extracted text. The corresponding Word body elements are unchanged. The body therefore retains 1,353 editable words, or 1,380 including timeline labels; disclosure, references and supplement remain outside that count. Section S3 occupies two pages in the eleven-page document. All eleven pages were visually inspected after the final edit.

The Word styles, section settings, headers, footers and images retain their original package bytes. Only the main document part, its hyperlink relationships and core description changed. Existing notebook links and the new technical links are present as PDF annotations. The supplement's date and version, introductory route and subsequent table number were updated to match the new content. The author's contribution remains disclosed in S4; removing the drafting quotation does not erase that role.

| Final artifact | SHA-256 |
| :--- | :--- |
| Assignment 4 v0.7 Word | `dff4d17b99a6b3adbeb299fb23f8bed8851beb35e7d6df984c37ded84beccbaf` |
| Assignment 4 v0.7 PDF | `a48a41bcd551c0fda747168939085233475953da57d59247f009d3406f48a1d3` |

Assignment 2's canonical v0.11 digest remains `0b94552fcf6bab438d39dded715587822d4186cdc932cd3670e6a0a0e23d2938`. The narrowed research verdict and historical claim-review files remain unchanged. No course submission occurred.

## AI and publication record

Codex and collaborating agents selected the record, compared exact excerpts and outputs, wrote the revised explanation, edited the documents and inspected the pages. The session identifies GPT-6 based Codex; the exact deployment snapshot is unavailable. These activities are recorded in ACT32 in the [AI activity log](../methods/ai-activity.json), with a corresponding [system-register note](../methods/AI-SYSTEMS.md). They are not independent human scholarly review.

The [item-level publication record](2026-11-15-assignment4-study-evidence-publication.json) records the new authored files and the selected synthetic request/response. The [assurance receipt](../governance/evaluation-results.json) records repository checks separately. The Markdown inventory flags were reviewed in the context of current instructions; historical wording and literal output fields remain historical records. Document binaries and production materials remain outside public Git.
