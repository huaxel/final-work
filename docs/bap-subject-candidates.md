# BAP subject candidates

These are two separate Final Work / Bachelorproef subjects. They should not be combined unless the course team explicitly approves that scope.

## Candidate A — Trees & Surfaces

### Core idea

Analyse the relationship between urban trees, heat and street usage, with a focus on how cities can make better interventions.

### Possible data

- per-tree registers from Brussels or Ghent;
- canopy and urban-heat layers from LiDAR, DSM/DTM and satellite data;
- bicycle-counter history;
- public-transport supply and route data;
- building and street morphology.

### Possible research/product direction

A multi-objective analysis of greenery, temperature and mobility friction. The output could identify trade-offs or Pareto-optimal interventions rather than produce a simple “more trees is better” map.

### Main risks

- pedestrian use and actual occupancy are poorly observed;
- bicycle counters are sparse and geographically biased;
- public-transport time series may contain structural breaks;
- the project could become a descriptive dashboard without a sufficiently strong research question.

## Candidate B — De Drie Leeftijden van een Brussels pand

### Core idea

Represent a Brussels building through three different ages:

1. **Register age** — the construction year in official building data;
2. **Facade-style age** — the architectural period inferred from street imagery;
3. **Structural age** — the underlying building period inferred from historical aerial imagery and change detection.

### Research question

How often does a registered historical year describe the building itself, and how often does it mainly describe a preserved facade? This turns facadism into a measurable heritage and urban-history question.

### Possible data

- GRB or other building-register data;
- the existing *Buildings of Brussels* photo archive as seed labels;
- Mapillary or other permitted street imagery;
- historical Brussels aerial imagery such as Bruciel, subject to reuse permissions;
- architect, address, date and style metadata.

### Possible product direction

An explainable building-history explorer showing the three ages, confidence/uncertainty and evidence behind each label. The project should avoid presenting uncertain image classifications as historical facts.

### Main risks

- image and aerial-data licensing;
- limited labelled training data;
- facade style is subjective and noisy;
- building-register dates may not represent renovation, reconstruction or facadism.

## Decision boundary

The two candidates have different identities:

- **Trees & Surfaces:** urban ecology, heat, mobility and spatial optimisation.
- **Three Ages:** Brussels architecture, heritage, computer vision and historical change detection.

The choice should be made based on available data access, the preferred technical challenge, coach fit and a finishable MVP.
