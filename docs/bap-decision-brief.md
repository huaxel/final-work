# BAP decision brief

Use [`bap-approval-checklist.md`](bap-approval-checklist.md) to turn this comparison into a coach/promotor decision.

The Final Work/BAP subject is still open. The two candidates are intentionally kept separate.

## Shared course requirements

Either subject should demonstrate:

- a concrete stakeholder problem;
- a realistic definition of done;
- analysis before implementation;
- a working or demonstrable product;
- documentation of decisions, testing, feedback and individual growth;
- ethical, privacy-aware and technically defensible choices.

## Candidate A — Trees & Surfaces

**Question:** where can urban tree placement reduce heat while preserving or improving street usability?

**Core MVP:** combine one city's tree register with one heat/canopy layer and one street-use proxy, then produce an explainable spatial analysis for a defined intervention question.

**Strong competencies:** data integration, spatial analysis, research, modelling, visual communication and value creation for urban stakeholders.

**Main uncertainty:** street usage is only partially observed. The project must not present bicycle counters or public-transport supply as a complete measure of pedestrian use.

**Safe fallback:** one city, one heat metric, one mobility proxy, descriptive/optimisation analysis and a transparent limitation report.

**Stretch:** Pareto-front analysis of greenery, heat and mobility trade-offs.

## Candidate B — De Drie Leeftijden van een Brussels pand

**Question:** how often does a building's registered construction year differ from its visible facade period and its structural historical period?

**Core MVP:** build a small, curated dataset of Brussels buildings with register metadata, facade-style labels and historical-image evidence, then demonstrate an explainable three-age explorer.

**Strong competencies:** data modelling, computer vision, historical research, uncertainty communication, heritage value creation and product design.

**Main uncertainty:** imagery licensing and the cost of creating reliable labels. Facade style must be treated as an uncertain classification, not as objective fact.

**Safe fallback:** a curated case-study dataset with transparent manual labels and a reproducible feature/annotation workflow; no claim of city-wide classification.

**Stretch:** change detection over multiple historical aerial-image epochs and city-wide scaling.

## Comparison

| Criterion | Trees & Surfaces | Three Ages |
|---|---|---|
| Core domain | urban ecology, heat, mobility | architecture, heritage, computer vision |
| Main data risk | sparse/incomplete usage measures | imagery rights and label quality |
| MVP shape | spatial analysis and map | curated dataset and explorer |
| Technical identity | GIS/data integration/optimisation | CV/data modelling/historical change |
| Personal archive advantage | open-data research | Buildings of Brussels archive |
| Safest fallback | one city and one proxy | curated case-study set |
| Main scope trap | becoming a descriptive dashboard | overpromising automated classification |

## Decision rule

Choose the subject for which a defensible MVP can be built with data that is actually accessible during the analysis phase. Treat the broader platform and city-wide automation as future work, not as prerequisites for passing the BAP.

## Prototype evidence update

The feasibility spikes now provide stronger evidence than the initial product sketches:

- **Trees & Surfaces:** 100 managed-tree points are joined to a real WBGT raster pixel and nearest bicycle-counter distance. The working MVP question is which observed tree areas combine relatively high heat-stress values with counter proximity for follow-up analysis. The interface supports a transparent exploratory signal; the counter join remains a spatial proxy, now supplemented by a measured-flow context (nearest-counter mean flow for one week, 97/100 trees) full per-point source traceability, complete core-join auditing and three explicitly named measured-flow gaps. A versioned stakeholder proposal and provenance-safe review worksheet are ready, with no response recorded yet.
- **Three Ages:** 34 real Grand Place records are available, with a six-record source-linked pilot and an explicit annotation protocol. All six register claims carry explicit `proxy` dates: three traced from Wikidata inception claims to Brussels heritage register records (one recorded disagreement) and three from direct Brussels architectural-inventory reconstruction dates. Three aligned ortho epochs (BruCiel 1930–1935 and 1996 under CC0; 2022 open data), five 1941–1942 KIK-IRPA facade previews (CC BY 4.0), an exact-case 1878 British Library engraving for La Balance (no known copyright restrictions) and its 2011 Wikimedia Commons comparison photograph (CC BY-SA 3.0) are committed. Historical facade and structural source access is now demonstrated. Eighteen aligned case crops and separate facade, structural and register worksheets make the remaining decisions reviewable without converting evidence into claims; human decisions and the La Balance address crosswalk remain pending.

## Recommendation for the approval conversation

Prefer **Three Ages** if reviewer capacity, identity mapping and register-year semantics can be confirmed before the analysis phase. Historical facade and structural source access now support the bounded MVP and its stronger uncertainty/product story.

Keep **Trees & Surfaces** as the fallback if the Three Ages review workflow cannot be staffed or its evidence semantics are rejected. Its safe MVP is a descriptive analysis of one city, one heat measure and one explicitly labelled mobility proxy—not a city-wide planting optimiser.

### Go/no-go checks

1. Confirm the stakeholder and decision question for the chosen subject.
2. For Three Ages, confirm the City `Grand-Place 24` to heritage `Rue de la Colline 24` identity mapping, review the 1878/2011 facade pair and 1930–1935/2022 structural comparison, and confirm that the official inventory reconstruction dates meet the intended register-year semantics.
3. For Trees & Surfaces, use the committed measured-flow context to decide whether counter proximity stays the ranking proxy or a flow-based alternative replaces it.
4. Freeze the MVP after the chosen subject passes its data-access check; treat automation and city-wide scaling as stretch work.
