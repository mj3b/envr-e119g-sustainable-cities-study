# Measurement: what a number can establish

[Home](../README.md) / [Methods](README.md) / Measurement · [Reproducible record snapshot](../research/progress.json)

Status: administrative record counts can be computed now. The engineering comparison and AI-productivity measures below are prospective specifications. They introduce no new Cerrillos result or urban theory.

## A useful lesson from METR

METR's [2025 developer study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) compared task completion with AI allowed and disallowed, while distinguishing participants' expectations from recorded performance. Its [time-horizon method](https://metr.org/time-horizons/) defines success relative to a task distribution, a human-duration baseline and a stated reliability level. The horizon is neither an agent's runtime nor a measure of every kind of work.

The local adaptation is to define the unit, comparator, success condition and limits before reporting a result. The equations below are ordinary accounting and comparison devices selected for this repository. They are not METR metrics, validated instruments, or a replication of METR's experiments. METR's software-task results supply no estimate of water demand or research productivity here. [Inspection record](../audit/2026-10-10-visitor-source-checks.json).

## What can be counted now

Run:

```sh
python scripts/research_progress.py
python scripts/research_progress.py --check
```

The first command prints deterministic JSON; the second compares it with the committed snapshot. Two input files define the populations. SHA-256 values identify their exact versions.

The historical source-closure ledger contains **44 entries**: 24 closed, 7 qualified, 6 blocked, 4 locator-only and 3 discarded. These are inherited classifications across a mixed set of access, documentary and analytical claims. They are not independent observations of environmental performance or current human approvals.

The separate draft register contains **4 legal-claim entries**, each marked qualified with human review pending, and **5 uninspected original-record dependencies**. The four entries overlap conceptually with historical work; do not add the two claim counts as though they formed a deduplicated sample.

These are complete counts of the named files, so sampling confidence intervals would have no useful interpretation. The counts remain sensitive to how an entry is defined, split or merged. Changing the question or ledger version changes the denominator.

## A projected water-demand comparison

For strictly comparable design cases:

$$
r_{\mathrm{design}} = 1 - \frac{Q_{\mathrm{revised}}}{Q_{\mathrm{baseline}}}
$$

Here, each `Q` is projected groundwater demand for the same service, period and system boundary, expressed in the same unit. Require `Q_baseline > 0`. The ratio is dimensionless; multiply by 100 to express a percentage. Preserve the absolute difference and both original values alongside any percentage.

A positive value denotes lower projected demand in that comparison. It cannot establish installation, operating savings, aquifer response or net environmental benefit. A negative value is possible and must remain visible. A water right or pump capacity cannot substitute for a demand forecast. A flow rate cannot become annual consumption without supported operating assumptions.

For Cerrillos, the required original technical inputs remain uninspected in the [current record](../research/cerrillos/draft-source-checks.json). The result is **unavailable**, not zero. No values are inserted into this equation in this release.

## Evidence coverage needs a fixed population

For a dated, explicitly enumerated set of material claims:

$$
C_{\mathrm{review}} = \frac{N_{\mathrm{source\text{-}matched\ and\ human\text{-}accepted}}}{N_{\mathrm{material\ claims}}}
$$

The numerator must count only claims in the denominator whose exact wording is supported by inspected original passages and accepted in a current, content-bound human review. Report the count of pending, disputed and unsupported claims beside the fraction. Where a justified claim is based on a secondary source, report that evidence class separately rather than silently treating it as original-source support.

This fraction tracks completion of a specified review procedure. It is not the probability the paper is true, a sustainability score, or a replacement for a decisive missing record. One missing material source can block a conclusion even when most claims are reviewed. Scope changes require a new denominator and an explanation; deleting difficult claims cannot be described as improved research validity.

A complete material-claim population and matching human-review records have not been established for this public-facing update. **No study-wide coverage percentage is reported.**

## Measuring AI assistance would require another study

A proposed effort comparison would use:

$$
r_{\mathrm{effort}} = 1 - \frac{\overline{T}_{\mathrm{AI\text{-}assisted}}}{\overline{T}_{\mathrm{comparison}}}
$$

`T` is human labor time in minutes for a predefined task, including source preparation, prompting, verification, correction and delivery. Those activities must be timed without overlap. Track tool runtime and elapsed waiting separately; they may overlap with human work. The comparator needs the same task population and quality requirements, with its workflow specified in advance.

A positive value would describe lower observed mean effort for that comparison. A causal claim would additionally need a defensible assignment and analysis design, with expertise, task difficulty, learning, failed attempts and incomplete tasks addressed. Report success and error outcomes alongside time. Never calculate gains only from successful AI-assisted tasks while retaining failures in the comparison group.

No comparable timed task sample, independent reference review or validated Jev study exists in this record. Therefore AI speedup, error reduction, cost savings and evaluator accuracy are **unmeasured**. Completed repository tests measure specified code and record properties only.

## Reporting rules

Every numerical statement records its source, version, locator, value, unit, period, denominator, comparison and observation type. Preserve conflicting definitions and uncertain dates. Report missing inputs explicitly. Prefer a small set of interpretable measures to a composite score that hides incompatible evidence.

The next empirical extension should be chosen because the necessary data can answer the research question, not because an equation makes the repository look more technical.
