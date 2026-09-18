# Quantitative claims with visible boundaries

[Home](../README.md) / [Cases](README.md) / Quantitative reasoning

A number becomes useful when its unit, period, system boundary, and evidentiary status match the question. The same value can describe a contractual threshold, installed capacity, a forecast, or an observation. Those meanings are not interchangeable.

## A reproducible scale check

MLGW’s [2025 update](https://www.mlgw.com/images/content/files/pdf/new/xAI%202025%20Update.pdf), pp. 1–2, reports initial grid service of 150 MW at Paul Lowery Road (`X-02`, `MEAS-MEM-CAP`). Actual annual electricity consumption is not supplied by that capacity statement.

For a hypothetical 365-day year:

```text
Annual energy = power × hours × assumed load factor
              = 150 MW × 8,760 h × assumed load factor
```

| Assumed load factor | Calculated annual grid energy | Interpretation |
| :--- | ---: | :--- |
| 0.50 | 657,000 MWh | Illustrative scenario |
| 0.75 | 985,500 MWh | Illustrative scenario |
| 1.00 | 1,314,000 MWh | Constant stated load throughout the year |

These assumptions are not a confidence interval or an estimate of utilization. They exclude on-site generation and the second site. Use actual interval demand and operating dates for an empirical energy total. The final row is recorded as `MEAS-MEM-SCALE`; it cannot be promoted to an observed outcome.

## Measurement distinctions

| Distinction | Required evidence |
| :--- | :--- |
| MW / MWh | Power observation and integration period |
| Water withdrawal / consumption | Intake, return flows, accounting definition, losses |
| Direct / upstream water | Separate facility cooling and electricity-supply boundaries |
| Absolute impact / intensity | Total activity as well as the denominator |
| Operational / embodied carbon | Boundary, lifetime allocation, inputs, emissions factors |
| Location-based / market-based electricity emissions | Separate accounting methods and applicable factors |
| Rate change / cost caused by a project | Tariffs, cost allocation, counterfactual, other system changes |
| Exposure / experienced harm | Spatial and temporal exposure plus appropriate outcome evidence |

## Arithmetic does not establish causation

For comparable observations, a percent change is `(later − baseline) / baseline × 100`; the baseline must be nonzero and boundaries must match. A falling intensity with rising activity can produce rising total demand. That arithmetic does not show that efficiency caused growth.

For water, preserve source, basin, season, consumption versus withdrawal, and return flow. A replenishment promise elsewhere or later is not automatically equivalent to restoring the same local resource. Test equivalence before netting quantities. For monetary comparisons, preserve price year, nominal versus real values, time horizon, and discount assumptions (`CD-05`).

Unknown values stay null. Sensitivity tables show dependence on stated assumptions; they cannot create missing measurements.
