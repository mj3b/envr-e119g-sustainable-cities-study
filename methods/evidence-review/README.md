# How to trace a claim

[Reader’s guide](../../docs/START-HERE.ipynb) / [Methods](../README.md) / Evidence review

Suppose a city wants to know how much water its cooling project withdrew in July 2025. A design estimate can help explain what the city expected. A July meter log could establish what the city recorded. This exercise follows one claim through both kinds of records so you can see when the evidence changes the label.

[Open the worked notebook](trace-a-claim.ipynb) and read it in your browser. The examples use invented records. You can follow them without installing anything. For the current study and its evidence, begin with the [first-reader notebook](../../docs/START-HERE.ipynb) or the [course-reader notebook](../../docs/FACULTY-GUIDE.ipynb). Both guides contain prose and reading exercises, with no code to run.

## Check the claim against the right record

Start with “The city measured the project’s July water withdrawals.” Find the part of the document that addresses the measurement and its date. Then use the table to compare possible records.

| If you find this | What the record establishes | Candidate label |
| --- | --- | --- |
| T02. A design report gives an expected amount. The supplied records are silent about July measurements. | A design estimate, with July measurements still an open question. | Insufficient |
| T01. An operating report expressly states that the city took no July meter readings. | An account of no measurements for that project and period. | Contradicted |
| T03. An operating log lists a July meter reading for the project. | A record of a measurement for the stated project and period. | Supported |

In T04 the claim adds that the city measured withdrawals in August. Check that clause separately. A July reading gives one observation. If the record says nothing about August measurements, the August clause remains unresolved and the combined claim is Insufficient.

## Follow the claim through the workflow

1. **Read the source and annotate the link.** The analyst records the passage, source, locator, claim clause and reason for linking them. A locator is the page, section or other detail that lets a reader find the passage again. For each link, the analyst indicates whether the passage supports the clause, contradicts it or supplies context.
2. **Check the packet and keep the passage attached to the source.** The program validates the packet. LangChain Core’s `Document` stores the passage and accompanying details. The passage identifier connects the annotation to the text a reader can inspect.
3. **Apply the written rules.** LangGraph runs the steps in a fixed order and combines the annotated links into a candidate label. A fixed workflow lets a reviewer reproduce the result and ask which annotation produced it.
4. **Send the candidate for human review.** Every result carries `pending_human_review`. A reviewer can compare the passage to the clause, check the period and units, and record a separate decision with their reasoning.

The program applies rules to the analyst’s annotations. A repeat run can show that the software handles the same inputs consistently. Checking the annotations requires reading the evidence. The demonstration uses no model calls, hosted tracing or API key. [LangChain Core document reference](https://reference.langchain.com/python/langchain-core/documents/base/Document) · [LangGraph workflow guide](https://docs.langchain.com/oss/python/langgraph/workflows-agents)

## Write the specification before changing the code

Spec-driven development records what a tool must do and how a developer will demonstrate it. In this example, “Keep missing measurements distinct from a statement that none were taken” becomes a requirement with two cases and two expected labels. If either case returns the wrong label, the test identifies the behavior to fix. The specification, implementation and tests let a reader follow that decision even when a coding assistant contributed. [Local specification](SPEC.md) · [Microsoft’s spec-first guide](https://developer.microsoft.com/blog/spec-driven-development-ai-native-engineering/) · [GitHub Spec Kit](https://github.github.com/spec-kit/)

For a real review, keep the claim and clause IDs, source version, locator, and explanation together. A SHA-256 fingerprint can identify the exact file reviewed. The reviewer still decides what the source supports and records that decision separately. The [AI use record](../../AI-USE-LOG.md) and [disclosure](../AI-DISCLOSURE.md) identify the assistance used in this project.

## Run the demonstration checks

The local test environment used Python 3.14.3. The three direct dependencies are pinned in [requirements.txt](requirements.txt). From the repository root, use the following commands.

```sh
cd methods/evidence-review
python -m pip install -r requirements.txt
python -m unittest -v test_workflow
python workflow.py
```

To run the notebook, open it in Jupyter with the same Python environment and run the cells in order. The [workflow](workflow.py) and [tests](test_workflow.py) are available alongside it.

## Check the notebook reading surface

Return to the repository root for the following checks. The first command uses Python’s standard library to validate the three notebooks, check local links, and screen text and saved outputs for selected publication hazards. It also keeps executable cells out of the two prose guides.

```sh
python scripts/check_notebooks.py
```

With the demonstration’s recorded dependencies installed in the active Python environment, the optional replay executes the fictional code cell and compares its output with the saved notebook output. It blocks socket connections, stops after 60 seconds and does not rewrite a notebook.

```sh
python scripts/check_notebooks.py --execute-worked
```

These checks address structure, navigation, selected disclosure hazards and reproducible example output. Source fidelity, reader comprehension and the adequacy of the case argument require separate review. The regression checks are in [the notebook test file](../../tests/test_notebooks.py).
