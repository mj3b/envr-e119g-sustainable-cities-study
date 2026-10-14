# Translator execution: what ran and what remains human

[Home](../../README.md) / [Course readings](README.md) / Translator execution

Eleven supplied PDFs were tied to source-specific candidate packs. Their original bytes were SHA-256 checked locally, and the pinned upstream Translator's original scripts completed **55 schema-validator invocations: five per pack, all passing**. The [unaltered execution receipt](translator-execution.json) records commands, outputs, exit codes, input hashes, artifact hashes, runtime versions and the observed timestamps.

That statement has a narrow meaning. ChatGPT assisted the reading and authored the candidate interpretations. Python serialized those candidates. Translator's validation scripts checked their structure. Translator did not independently read the PDFs, verify the scientific claims, approve the memo or execute its provider-backed agent loop. The source descriptions and use recommendations remain subject to Mark's review.

## Upstream version and executed steps

The source was retrieved at commit `4e5d742378dd2fecbafd525eeb9754c975b83aa0` from [Research-to-Decision Translator](https://github.com/node-and-norm/applied-ai-research-translator/tree/4e5d742378dd2fecbafd525eeb9754c975b83aa0). The original archive came from GitHub Actions run `38497671805`; its digest and the script/schema hashes were checked. [Pinned file hashes](upstream-files.json) make the actual executed files identifiable.

| Original upstream script | What the run checked |
| :--- | :--- |
| `validate_pack.sh` | `agent_spec.json` only; its name does not imply validation of every pack file |
| `validate_claims.sh` | Candidate `claims.json` structure |
| `validate_tasks.sh` | Bounded `tasks.json` structure |
| `validate_run_input.sh` | The serialized candidate input record |
| `validate_run_output.sh` | The serialized candidate mapping output |

Each generated pack also contains an evaluation-plan object, a README and a short source-anchor text file. That anchor contains a limited quotation, not the article. Full PDFs and extracted article text stay outside public Git history. The committed source cards and runner reproduce the pack contents; the receipt identifies every output by hash.

The theoretical and normative readings require a further distinction: a check of whether a card faithfully describes Sen or North does not experimentally validate their theory. The candidate task tests source-description fidelity and appropriate use. It does not disguise a normative principle as an empirical effect.

## Deliberately unexecuted steps

The upstream `runloop/run_t_c02.py` is a particular provider-backed classification example with an interactive human gate. It is not a general PDF-ingestion command. It was inspected but not invoked. No provider key was requested or supplied; no API-backed Translator classification or live Jev evaluation occurred. No `human_gate.json` or final `decision_summary.json` was fabricated.

The safety-policy intake script was not invoked for these urban-course source-use records. This is a bounded extension of the artifact workflow to course readings, not a claim that every AI-safety workflow or governance gate has been completed. Upstream compatibility is demonstrated only for the five validated artifact types at the pinned revision.

All candidate output records use `status: ok` to mean that the mapping object was produced. Every human-review state remains pending. A successful structure check is not acceptance for submission or a new finding about the case.

## Reproduce the completed scope

Use a checkout of the exact upstream commit and a directory containing the eleven original files with the filenames in the source cards. Run from this study repository:

```sh
python scripts/run_course_translator.py \
  --translator-root /path/to/applied-ai-research-translator \
  --source-dir /path/to/original-course-pdfs \
  --output /path/to/new-run-directory
```

The runner requires `jsonschema`, verifies the listed upstream file hashes, checks every source hash before starting, refuses to overwrite an existing output directory, and records each original validation command. Its bounded parallelism changes execution scheduling, not the validators or their input content.

A public reader without the course files may reproduce the structural checks only:

```sh
python scripts/run_course_translator.py \
  --translator-root /path/to/applied-ai-research-translator \
  --structures-only \
  --output /path/to/another-new-directory
```

That mode explicitly records that original PDF bytes were not checked. It cannot be used to claim original-source access. The original `translator-execution.json` must remain unchanged; a subsequent run gets a new receipt.

## Retrieval and execution failures preserved

Direct container Git access failed on DNS resolution; the connected GitHub tools and a previously retrieved, hash-checked archive supplied the code. The archive's checksum list initially referred to a directory prefix absent from the unpacked location; checking the same files by basename resolved that path issue, and both archive hashes matched. No integrity mismatch was observed.

Two sequential validation attempts exceeded their tool execution time limits before producing a terminal receipt. Their partial output directories were retained separately and were not counted as completed runs. The final bounded-parallel run completed all 55 checks and produced the cited receipt. This records completion of a retry, not retrospective success for the interrupted attempts.

McConnell's publisher HTML was read separately. Attempts to obtain its local PDF bytes and page screenshots failed; the source was not inserted into this eleven-PDF run. The Module III Canvas links likewise do not count as downloaded or processed PDFs.

See [source cards](source-cards.json), [assignment relevance](ASSIGNMENT-02-RELEVANCE.md), and [the AI-use log](../../AI-USE-LOG.md). Repository delivery, source interpretation and scholarly approval remain separate events.

## Completion after the transfer interruption

The [additional observed checks](completion-checks.json) distinguish a repeat schema-validation run from a separate run of the original PDF-intake CLI. All 55 validators passed again, and all 88 candidate-artifact hashes matched the earlier receipt. The unchanged upstream `src/translator/cli.py` also ran on each original PDF outside public Git. It copied the files, invoked `pdftotext`, and created unreviewed templates. Ten extractions contained text; North's contained none. Neither result measures understanding or establishes source fidelity.

The CLI templates are deliberately kept out of the public candidate packs: their default agent language and empty bibliographic fields do not represent this course study. The existing source cards remain the AI-authored, source-located interpretation layer. A scan that produces no text requires visual reading; no OCR was performed here. The code hash is in [PDF-intake provenance](pdf-intake-code.json).

To reproduce intake for one file from the pinned Translator checkout, set `PYTHONPATH=src` and run `python -m translator.cli make-pack --title "Reading title" --out /path/outside/public-repo --pdf /path/to/original.pdf`. The command copies the PDF: keep its output outside public Git. The completion packet retains exact per-file commands and outputs without distributing the PDFs or extracted articles.
