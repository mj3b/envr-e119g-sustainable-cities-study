# Following a Water Commitment as Conditions Change
## Public-source register and bounded study protocol

Prepared for Mark Banasihan, ENVR E-119g. Earlier AI-assisted source-discovery record: September 22, 2026. Imported as preparation history; external sources were not rechecked in the Class 2 integration. See [current evidence note](class-03-evidence-note.md) and [source-review update](../../audit/2026-09-22-class2-integration.md).

### Scope and status

This is an acquisition and quality-control plan for one provisional The Dalles water-commitment case. It is not a downloaded longitudinal dataset, a completed impact assessment, an independent validation, or a live data connection. No outreach, public-records request, API-key registration, or repository change was made.

The immediate research target is one assurance associated with the November 8, 2021 authorization of Resolution 21-028. Keep later communications and observations separate from evidence shown to have been available before that decision. The 2023 company profile, 2024 master-plan adoption, and 2025 conservation-plan record are later evidence leads.

The attached earlier concept memo proposes a much larger IDB study. Its 8–12-project sample, multilingual experiment, and field extension are outside this semester plan. Its unresolved citation placeholders must be replaced with verified original sources before reuse.

## 1. Source register

### DAL-S01. Original authorization and deliberation

**Source:** City of The Dalles, November 8, 2021 council minutes.

[Original minutes PDF](https://ompnetwork.s3-us-west-2.amazonaws.com/sites/312/documents/cc_2021-11-08_council_minutes.pdf?jYfO_44rHBJuOFVzCoOJEEfTLBPitWPC=)

**Inspected:** Relevant passages on printed pages 4–6.

**Use:** Identify the authorization, documented assurances, references to supporting studies, and named counterparties. Search Moraine Industries LLC and Design LLC as well as Google and Resolution 21-028.

**Limit:** Minutes are not the executed agreement or proof of environmental performance. Reconcile the recorded 3.8 and 3.9 million gallons/day figures against their underlying definitions before calculation. Avoid redistributing incidental personal contact information in attached public correspondence.

**Next acquisition:** Executed agreement, exhibits, amendments, referenced studies, and evidence of their availability at the decision date.

### DAL-S02. Municipal archive

[City digital archives and search instructions](https://www.thedalles.gov/department/city_clerk/digital_archives_public_document_search.php)

**Inspected:** Landing page and search guidance. No complete case search exported.

**Access:** Public ORMS search and linked documents. Select jurisdiction “The Dalles, City of.” “Any Word” searches title/notes; “Document Content” searches text in searchable documents. Record both routes, aliases, dates, and results. A bookmarked search reruns against the current archive; preserve the actual retrieved files separately.

**Use:** Council packets, minutes, budgets, audited financial statements, resolutions, and records linking obligations to later decisions.

**Limit:** An incomplete archive or failed search cannot establish that a document or action never existed. The city provides a separate public-records request route; none was used here.

### DAL-S03. Water-system planning records

[Water Master Plan landing page](https://www.thedalles.gov/department/public_works/master_plans/water_master_plan.php)

[2025 Water Management and Conservation Plan record](https://ormswd2.synergydcs.com/ORMSCMSearchDEQ/Search/RecordViewer.aspx?uri=7066258)

**Inspected:** City landing page and conservation-plan record title. The city identifies December 9, 2024 as the master-plan adoption date. The linked full master-plan PDF could not be retrieved in this pass; the conservation-plan viewer did not expose its full text.

**Use:** Acquire technical assumptions, demand scenarios, source descriptions, infrastructure schedules, financing, and any conservation/review provisions actually contained in the plans.

**Limit:** Do not attribute contents to an unread plan. A later plan can test continuity of assumptions but cannot establish what the 2021 decision-makers knew. The city's explanatory FAQ includes its view that major replacement projects address aging infrastructure; test this explanation against dated capital plans and financial records.

### DAL-S04. Oregon water rights

[Water Right Research Query](https://apps.wrd.state.or.us/apps/wr/wrinfo/)

**Inspected:** Public query interface; no case-specific rights selected.

**Access:** Search by name, location, stream, application, permit, certificate, or transfer identifier.

**Use:** Establish which rights, transfers, authorized uses, and conditions relate to the infrastructure and sources under study.

**Limit:** A legal authorization is a different object from a measured withdrawal, customer delivery, or reliably available supply. Interpret individual conditions only after inspecting the instrument.

### DAL-S05. Oregon reported water use

[Water Use Reporting guidance](https://www.oregon.gov/owrd/programs/waterrights/reporting/wur/pages/default.aspx)

[Public Water Use Query](https://apps.wrd.state.or.us/apps/wr/wateruse_query/)

**Inspected:** Reporting guidance and query/export interface. No local data series downloaded or checked.

**Access:** Query water user, diversion/facility, water right, or geography; the interface offers text and spreadsheet export options. Keep calendar-year and water-year selections explicit.

**Use:** Seek observations corresponding to the selected rights and physical sources. Identify measured versus estimated reports.

**Limit:** The agency explains that reporting coverage is incomplete and values may be measured or estimated. Geographic totals are not a census of all use. Source withdrawals may differ from facility deliveries; establish the measurement point before comparing them.

### DAL-S06. Groundwater observations and well metadata

[Oregon groundwater-monitoring guidance](https://www.oregon.gov/owrd/programs/GWWL/GW/Pages/GWMonitoring.aspx)

[Groundwater Information System](https://apps.wrd.state.or.us/apps/gw/gw_info/gw_info_report/Default.aspx)

**Inspected:** Guidance and database description. No well selected or time series extracted.

**Access:** Public site query, mapping interface, and linked well-report database.

**Use:** Identify potentially relevant wells, water-level measurements, well construction, location uncertainty, and available links to rights.

**Limit:** Coverage and quality vary; some integrations are described as planned. Select a monitoring well through a documented hydrogeological relationship, not proximity alone. Preserve depth, measuring datum, pumping/static status where supplied, collection method, and quality qualifications.

### DAL-S07. USGS observations

[USGS Water Data APIs](https://api.waterdata.usgs.gov/)

**Inspected:** API catalog and metadata endpoints; no study-specific station selected or observational query validated.

**Access:** Documented REST services for monitoring locations, time-series metadata, daily values, continuous values, and water-quality services. Confirm current service authentication/rate terms before deployment.

**Use:** First examine station location, measured parameter, units, and period of record. Retrieve observations only after establishing relevance to the case's water source or process.

**Limit:** A nearby streamgage is not automatically evidence about the relevant municipal source or aquifer. Preserve provisional/revised flags, gaps, and aggregation methods. Do not substitute Columbia River flow for a local source without a defensible connection.

### DAL-S08. Drinking-water quality and service geography

[The Dalles water-supply page and report links](https://www.thedalles.gov/department/public_works/public_works_divisions/water_supply___treatment.php)

[Oregon Your Water system-record target](https://yourwater.oregon.gov/inventory.php?pwsno=00869)

**Inspected:** City page identifying public water system 41-00869 and links to current/past quality reports, a service map, and OHA results. The selected OHA record failed to load in this pass; linked map and report contents were not verified here.

**Use:** Acquire quality records and source descriptions; verify which customers and service area the data cover.

**Limit:** The city explicitly distinguishes its utility from Chenowith Water PUD. Quality-compliance information cannot establish all dimensions of service continuity, affordability, or source sustainability.

### DAL-S09. Company assertions and reported quantities

[Google, April 2023 water profile for The Dalles](https://www.gstatic.com/gumdrop/sustainability/2023-data-center-water-profile-the-dalles.pdf)

[Google Oregon data-center location page](https://datacenters.google/locations/oregon/)

**Inspected:** Two-page 2023 profile, including its diagram. Other linked corporate reports have not been audited here.

**Use:** Record dated company assertions, project phase descriptions, definitions, and numerical claims as a source to test.

**Limit:** Corporate provenance stays visible. A planned benefit is not an achieved result. The April 2023 publication is subsequent communication, not evidence available at the November 2021 vote. Clarify relationships among campuses, older infrastructure, new construction, rights transfers, and storage projects before joining records. Do not infer an AI-workload share.

### DAL-S10. Household context and utility finance

[ACS five-year data and API guidance](https://www.census.gov/data/developers/data-sets/acs-5year.html)

[Municipal budgets and audited statements gateway](https://www.thedalles.gov/department/city_clerk/digital_archives_public_document_search.php)

**Inspected:** Census documentation and municipal archive links. No local estimates, tariff schedules, or account records acquired.

**Access:** ACS web/download options or API. The inspected Census documentation says all data API queries now require a key. No key was requested. Municipal documents require their own archive search.

**Use:** Seek appropriate poverty, income, tenure, population, and housing estimates; pair them with acquired rate schedules and financial records for bounded distributional questions.

**Limit:** Retain margins of error, variable universes, geography versions, and multi-year periods. Census geography is not a utility customer list. A modeled water bill divided by an income scenario is an illustration, not an observed household burden. A rate change alone cannot identify the commitment's causal effect on costs.

### DAL-S11. Weather and drought context

[NOAA Climate Data Online API documentation](https://www.ncei.noaa.gov/cdo-web/webservices/v2)

[U.S. Drought Monitor downloads](https://droughtmonitor.unl.edu/DmData/DataDownload.aspx)

**Inspected:** Access documentation and download page. No local station series or drought-area file acquired.

**Access:** NOAA CDO v2 uses a token and returns JSON; documented limits are five requests per second and 10,000 per day. The Drought Monitor provides downloadable statistics and map data. No token registration occurred.

**Use:** Describe weather and drought conditions relevant to a prespecified period and water source.

**Limit:** Choose station elevation, distance, coverage, and watershed relevance explicitly. A county drought category cannot measure the selected aquifer's condition or establish anthropogenic attribution for an event.

### DAL-S12. Watershed boundaries

[USGS Watershed Boundary Dataset](https://www.usgs.gov/national-hydrography/watershed-boundary-dataset)

**Inspected:** Official description; no geometry downloaded.

**Use:** Delineate surface-drainage context alongside the verified municipal/service-area boundary.

**Limit:** Surface drainage, groundwater connectivity, utility distribution, and legal jurisdiction require different representations. Record layer date, scale, geographic reference system, and the reason it answers the question. Mapping is optional if it adds no material insight.

## 2. Minimum protocol before inference

The following requirements are proposed for this study, not institutional endorsements or formal grading criteria.

### Define one question and its permissible answer

Working question: What evidence supported the selected supply assurance, what later observations bear on its continuing adequacy, and which institution could reconsider the commitment?

The core product is documentary reconstruction. A causal effect estimate requires additional identification. Documentary clarity, ecological adequacy, household outcomes, and economic benefits remain distinct assessment dimensions.

### Freeze the relevant dates

Record approval, execution, effective date, document creation, public release, retrieval, and measurement interval separately. Use a fixed review cutoff. End quantitative comparisons at the latest complete and comparable reporting period; label partial periods. Record evidence that an actor actually received a document rather than inferring receipt from publication alone.

### Specify competing explanations

Examine whether added infrastructure improved supply; whether demand or source conditions changed; whether observed costs reflect pre-existing asset replacement; whether another management instrument supplied the review mechanism; and whether missing public records prevent reconstruction. For each explanation, specify the observation that would support or weaken it.

### Adopt a retrieval stopping rule

Search the defined repositories using documented identifiers, aliases, dates, and content-search options. Follow references to material exhibits and studies. Record unavailable, unsearched, inaccessible, superseded, and located-but-unreviewed items separately. When a material gap remains, narrow the conclusion. Do not broaden the project simply to find available numbers.

### Protect source and measurement meaning

Maintain a data dictionary for quantity, unit, measurement point, period, facility, population, definition, provenance, and uncertainty. Keep rights, capacity, withdrawals, deliveries, consumption, return flow, and storage changes distinct. Distinguish a forecast, target, analytical threshold, and documented action trigger. A trigger requires an identified response provision; a number alone does not establish one.

### Handle sources as sources

An agency record is primary evidence of the agency's record or observation, subject to its qualifications. A corporate publication is primary evidence of the company's representation. Public testimony establishes a documented account, not population prevalence. Repeated publications based on one measurement share provenance; count the originating observation rather than the number of webpages.

### Document solo quality checks

Verify every substantive quoted, numerical, causal, and attribution claim used in the final argument against the original passage or dataset. Check calculations separately and preserve transformation steps. Revisit selected coding after a delay and record changes as within-researcher consistency checks. AI agreement is not independent validation. Refer to the resulting evidence as researcher-checked.

### Keep affected people and ecological constraints visible

Public secondary data can support bounded household or service findings when the population, measures, and coverage are adequate. Lack of a local partner is not an automatic prohibition on such analysis. Direct claims about experiences absent from the data remain unresolved. Distinguish service continuation from ecological sustainability, and avoid treating citywide averages as the experience of every group.

### Preserve privacy and research materials

Retain original documents privately with retrieval metadata and file hashes where feasible. Keep extracted text and corrected tables separate from originals. Use public excerpts or permitted derived data for sharing; omit incidental personal contact details and all NDA-covered materials. Record source-use restrictions and disclose AI contributions accurately.

## 3. Proposed data structure

Use the existing repository schema where possible; this is a conceptual crosswalk, not a request to build duplicate systems.

| Research object | Minimum content |
| --- | --- |
| Source | Identifier, originator, URL, document version, relevant dates, retrieval status, use limits, original-file location, hash when acquired |
| Entity/location | Name and aliases, institution/facility/well identifier, geographic boundary, evidence for each match, applicable dates |
| Claim | Exact passage and locator, speaker/author, date, proposition, conditions, evidence class, researcher interpretation, review status |
| Measurement | Value, unit, definition, measurement point, period, scope, source, estimation/observation status, quality flags, transformation |
| Event | Decision or observation date, actor, authority, action, related evidence, record of implementation or unresolved gap |
| Finding | Supported interpretation, alternative explanation, limitations, source links, next discriminating check, condition for revision |

## 4. First completed research packet

Start with one claim from the authorization discussion and follow it as far as the accessible records allow. Produce its timeline, source-linked interpretation, and an explicit account of any missing executed terms or supporting evidence. Add one defensible quantitative comparison or one boundary map only after it answers a defined question.

Completion means another reader can locate the evidence, reproduce the transformation, distinguish the observation from the inference, and identify what could change the finding. It does not require a particular positive or negative conclusion about the commitment.

## 5. Research-practice references

[MIT Libraries: Documentation and metadata](https://libraries.mit.edu/data-management/store/documentation/)

[Harvard Biomedical Data Management: Data dictionary](https://datamanagement.hms.harvard.edu/collect-analyze/documentation-metadata/data-dictionary)

These sources support documenting research materials, variable meanings, provenance, changes, and AI use. They are useful practices to adopt; they are not a certification of this study or the course's grading rubric.
