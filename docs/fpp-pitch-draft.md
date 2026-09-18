# FPP pitch draft — De Vier Prijzen van Brussel

> **Status:** working draft based on the existing FPP brainstorming; not yet approved as the FPP subject.

## Project title

**De Vier Prijzen van Brussel** — an explainable data product that compares four valuation regimes for Brussels housing.

## Why this project?

As a lawyer working with Brussels fiscal matters and as a computer-science student, I want to combine legal reasoning, public data and applied software engineering in one inspectable project. The project turns a legal and societal question into a reproducible technical artefact rather than another opaque price prediction tool.

## Problem

The same dwelling can be described by several systems:

1. the market asking price;
2. the legal reference rent;
3. the fiscal value;
4. the real transaction price.

These systems do not necessarily agree. Since the Brussels reference-rent regime became binding, it is useful to understand where market prices exceed the legal reference band and how the different regimes diverge.

## Intended users and value

- **Tenants:** understand the legal reference for a property profile.
- **Owners and agents:** obtain a transparent reference point for pricing.
- **Policy stakeholders:** evaluate whether the reference-rent model remains calibrated.
- **Journalists and researchers:** explore geographic and property-profile patterns.

The public value is a transparent, reproducible way to investigate housing affordability and the operation of a legal policy. The project does not provide individual legal advice or investment recommendations.

## Proposed solution

Build a data product with three layers:

1. **Unified property record** — common representation of property type, size, location, energy performance and other attributes.
2. **Regime plug-ins** — independently calculate or load each valuation regime, so restricted data cannot block the core project.
3. **Explorer and analysis** — neighbourhood-level maps, property-profile lookups, divergence measures, uncertainty and a methodological report.

## Definition of done

The project is done when it delivers:

- a reproducible pipeline for the open legal reference-rent regime;
- a documented market/listing or approved public-data input;
- a neighbourhood-level analysis of properties exceeding the legal reference band;
- an interactive explorer or equivalent static demonstrator;
- documented assumptions, data limitations, privacy boundaries and validation results;
- a final report explaining what the data can and cannot establish.

Optional modules include historical event-study analysis, transaction microdata and fiscal-value comparison. None is required for the core MVP.

## Technical direction

Possible components:

- Python data pipeline and validation tests;
- relational model for canonical entities and analytical views;
- append-only raw-data archive with provenance;
- statistical or tree-based models for explainable divergence analysis;
- map and profile explorer;
- reproducible local execution and documentation.

The final stack will be chosen after confirming the course requirements and available data.

## Scope and safeguards

### Core scope

- Brussels only;
- rental market first;
- legal reference-rent regime plus one approved market/public-data source;
- neighbourhood/profile-level output;
- no individual property identification in public outputs.

### Explicit non-goals

- no legal advice;
- no production scraping before terms and permissions are assessed;
- no confidential fiscal or employer data;
- no dependency on restricted microdata;
- no claim that asking price equals transaction price;
- no expansion to other cities during the core project.

## Competencies demonstrated

The project can provide evidence of planning, requirements analysis, data modelling, implementation, integration, research, critical problem-solving, professional communication, privacy/security awareness, value creation and ethical interpretation.

The evidence should be maintained throughout the project in a decision log, risk register, test results, feedback log, contribution log and individual reflection.

## Risks and fallback

- **Historical or market data unavailable:** use approved public data or a cross-sectional analysis.
- **Restricted transaction/fiscal data unavailable:** treat those regimes as documented future extensions.
- **Terms-of-service limitations:** use an approved dataset or an explicitly documented archive.
- **Scope expansion:** keep each valuation regime optional and preserve the rental MVP.

## Proposed analysis-phase plan

| Phase | Output |
|---|---|
| Weeks 1–3 | approved problem statement, users, data-governance boundaries and team roles |
| Week 4 | introduction page, definition of done and realistic project plan |
| Weeks 5–8 | data model, source audit, legal/formula analysis, validation and prototype |
| Weeks 9–12 | divergence analysis, explorer design and technical documentation |
| Before the pitch | tested MVP, limitations report, competence evidence and presentation |

## Decisions to confirm with the course team

- whether this FPP direction should later inform a separate Final Work subject;
- acceptable project/team format and bootcamp planning;
- coach/promotor and relevant technical coaches;
- permitted datasets and overlap with DAM, DAS and MAL coursework;
- whether the core project should include a real external stakeholder.
