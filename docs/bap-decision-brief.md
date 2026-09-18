# BAP decision brief

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
