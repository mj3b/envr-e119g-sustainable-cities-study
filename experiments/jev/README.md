# Optional Jev claim-support pilot

Status: protocol, request builder, and synthetic contract tests only. **Zero live Jev evaluations for this study.** This is not a prerequisite for Assignment 2.

Jev is TypeSafe AI's hosted model for typed questions and structured answers. Official documentation inspected October 9, 2026: [introduction](https://docs.typesafe.ai/introduction), [API quickstart](https://docs.typesafe.ai/introduction/quickstart), and [confidence](https://docs.typesafe.ai/confidence). Use the official API endpoint only. Similarly named independent gateways are not treated as TypeSafe.

## Task and limits

Given one bounded claim and a supplied passage, classify the passage's support as `supported`, `contradicted`, or `insufficient`. This is a proposed use, not a demonstrated capability. Jev does not retrieve missing originals, decide the correct legal interpretation, establish source authenticity, determine ecological benefit, or approve the memo. A deterministic missing-evidence check runs before any provider call. Every result remains advisory.

TypeSafe's Choice confidence is a transformation of the probability distribution; it is not an independently established probability that a research claim is true. Preserve the complete distribution and resolved model identifier. Evaluate errors on this task before describing calibration or utility. No threshold in this scaffold grants claim acceptance.

## Prospective pilot

Start with the 12 [synthetic fixture cases](fixtures.json). Their reference labels are AI-authored and **not human-approved ground truth**. A human must correct/freeze labels before live use. Then prepare a separate small set of source-bound examples, withholding expected labels from all model inputs. Define the split and analysis before running those examples. TAE's Jev experiments are a separate study; their results are not imported as validity evidence here.

Include projection-versus-observation, screening-versus-authorization, missing-source, attribution, negation, temporal, and quantity-type contrasts. Test a claim with a consequential word changed and a meaning-preserving paraphrase. Compare against a simple deterministic missingness/type-check baseline. All judges should receive the same bounded evidence; agreement is not independent source corroboration.

Report counts and denominators: unsupported claims labeled supported / all truly unsupported claims; supported predictions that are wrong / all supported predictions; abstentions / eligible items; support agreement; mutation consistency; errors by kind; and recorded latency/cost when available. With a small pilot, report descriptive results, not a general calibration claim. Zero observed errors is not proof of zero risk. Blind model labels from the reference reviewer where feasible; disagreements remain visible and require adjudication.

## Run without a provider

```sh
python experiments/jev/runner.py --mode prepare --out private/jev-prepared.json
python experiments/jev/runner.py --mode mock --out private/jev-mock.json
```

Mock responses are fabricated software fixtures. They must never be reported as Jev measurements.

Live mode requires an explicit network flag, a budget cap in call count, reviewed/frozen reference labels, and `TYPESAFE_API_KEY` in a secure local environment. Do not put keys in chat or Git. It is disabled in CI. The runner uses Python's standard library; no provider SDK or model weights were installed. The live adapter has not been tested against the provider.
