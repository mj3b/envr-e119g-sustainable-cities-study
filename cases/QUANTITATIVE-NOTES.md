# Quantitative evidence that can be reconstructed

[Home](../README.md) / [Cases](README.md) / Quantitative reasoning

> **A number needs a definition before it needs a chart.** Record whether it is an observation, reported figure, contractual threshold, forecast, or illustrative scenario. Unknown values remain null.

## Minimum record for a usable quantity

| Field | Question it must answer |
| :--- | :--- |
| Value and unit | What is counted or measured? Is this power, energy, volume, flow, currency, or a rate? |
| Evidence status | Was it directly observed, reported by a party, modeled, promised, or assumed? |
| Period | Which dates, interval length, operating hours, and baseline apply? |
| System boundary | Which facility, meter, service territory, basin, population, or process is included? |
| Denominator | Per what activity, person, household, account, unit of output, or time interval? |
| Provenance | Which source, locator, version, and transformation produced the value? |
| Comparability | Did definitions, equipment, coverage, prices, or boundaries change between observations? |
| Uncertainty and missingness | What is unknown, estimated, censored, incomplete, or sensitive to an assumption? |

These fields support review. They do not turn a reported quantity into an independent measurement.

## Worked scale check · Memphis electricity

MLGW's [2025 update](https://www.mlgw.com/images/content/files/pdf/new/xAI%202025%20Update.pdf), pp. 1–2, reports initial grid service of 150 MW at Paul Lowery Road (`X-02`, `MEAS-MEM-CAP`). Actual annual electricity consumption is not supplied by that capacity statement.

For a hypothetical 365-day year:

```text
Annual energy = power × hours × assumed load factor
              = 150 MW × 8,760 h × assumed load factor
```

| Assumed load factor | Calculated annual grid energy | Status |
| :--- | ---: | :--- |
| 0.50 | 657,000 MWh | Illustrative scenario |
| 0.75 | 985,500 MWh | Illustrative scenario |
| 1.00 | 1,314,000 MWh | Constant stated load throughout the hypothetical year |

The rows are assumption sensitivity, not a confidence interval or a utilization estimate. They exclude on-site generation and the second site. Actual interval demand, operating dates, and missing intervals are needed for an empirical total. `MEAS-MEM-SCALE` records the final scenario; it cannot become an observed outcome.

## Keep the quantity attached to its meaning

| Distinction | Evidence required | Error to detect |
| :--- | :--- | :--- |
| MW / MWh | Power observations and integration period | Treating capacity as consumed energy |
| Water withdrawal / consumption | Intake, return flows, accounting definition, and losses | Labeling every withdrawn gallon as consumed |
| Water right / actual use | Legal allocation plus separate operating observations | Using an entitlement as a meter reading |
| Direct / upstream water | Facility cooling and electricity-supply boundaries | Combining incompatible periods or double-counting |
| Absolute impact / intensity | Total activity and the functional denominator | Presenting lower intensity as proof of lower total impact |
| Operational / embodied carbon | Scope, lifetime allocation, inputs, and emissions factors | Hiding allocation assumptions in a single total |
| Location-based / market-based emissions | Separate accounting methods and applicable factors | Combining methods as if they measure the same quantity |
| Rate change / project-caused cost | Tariffs, allocation, usage, other system changes, and a comparison | Assigning every bill change to the project |
| Exposure / experienced harm | Spatial and temporal exposure plus outcome evidence | Inferring harm from distance or demographics alone |

The Dalles' 3.8/3.9 million-gallons-per-day discrepancy remains a definition or source-reconciliation problem (`CASE-DAL-03`). Averaging the values would conceal the unresolved issue.

## Population denominators are part of the argument

| Proposed measure | Numerator and denominator to specify | Qualification |
| :--- | :--- | :--- |
| Share of a group within a study boundary | Group population / total population in the same geography and period | Preserve estimate uncertainty and geographic mismatch |
| Household energy burden | Household annual energy expenditure / the same household's annual income | Specify treatment of zero or missing income and which expenditures are included |
| Service-event frequency | Qualifying events / defined observation period or opportunities | Missing observations cannot be treated as no event |
| Participation | Recorded participants relative to a justified eligible population, only if known | A hearing attendance count does not establish representativeness or influence |

Keep households, accounts, residents, and submissions distinct. Disaggregate when the data and question support it; do not manufacture precision from sparse or incompatible records. The candidate dossiers define intended acquisition, not completed population analysis.

## Comparison before causal explanation

For comparable observations, percent change is `(later − baseline) / baseline × 100`. A zero baseline makes that expression undefined. A changed definition or boundary can make a technically correct percentage misleading.

| Check | Practical consequence |
| :--- | :--- |
| Baseline chosen before inspecting the desired result | Record why the period is representative and retain inconvenient observations |
| Same boundary and seasonal basis | Do not compare different meters, basins, project versions, or seasons without adjustment and explanation |
| Rival drivers examined | Workload, weather, other users, fuel prices, and infrastructure changes can explain movement independently of governance |
| Appropriate uncertainty stated | Assumption ranges, measurement uncertainty, and uncertainty about causation are different claims |
| Outcome distinguished from commitment | Authorization, construction, or a promise does not establish the intended social or ecological effect |

For water, preserve source, basin, season, withdrawal/consumption definition, and return flow. A replenishment promise elsewhere or later cannot be netted against local use without establishing equivalence. For money, preserve price year, nominal/real basis, horizon, and discount assumptions (`CD-05`).

A falling intensity alongside rising activity can produce rising total demand. That arithmetic does not show that efficiency caused growth. A sensitivity table can expose assumptions; it cannot supply absent measurements or establish a causal effect.
