# Future Proof Project

## Basic Info

- [ECTS fiche](https://bamaflexweb.ehb.be/BMFUIDetailxOLOD.aspx?a=170139&b=5&c=1)
- **Jaar**: Derde Bachelor (E27)
- **Semester**: 1 (enkel aangeboden in semester 1)
- **Studiepunten**: 5
- **Uren**: 134 (4 coaching + 40 leer- en evaluatietijd + 90 projectwerk)
- **Docent**: Weemaels Steve
- **Taal**: Nederlands
- **Examen**: portfolio 100% (januari; 2e kans augustus)
- Niet tolereerbaar onder 8/20

## Beschrijving ECTS

De student krijgt in dit OLOD de kans om te excelleren op basis van een **zelfgekozen voorstel** (bv. kenniscentrum, werkveld, eigen voorstel, etc). De student argumenteert m.b.v. een pitch:

- de *definition of done*
- de eigen ambities
- de economische of maatschappelijke meerwaarde

Indien dit voorstel goedgekeurd wordt gaat de student van start met de uitvoering van het project.

## Doelstellingen

- D1: Levenslang leren en experiment
- D2: Zichzelf ontplooien en definiëren van ambities
- D3: Economische of maatschappelijke waardecreatie

## Status — brainstorm ronde 5 (sept 2026)

**Geselecteerd (ronde 5, 2026-09-17): De Vier Prijzen van Brussel** — convergentieanalyse van vier waarderingsregimes voor dezelfde woningen, uitgewerkt tot pitch-draft (zie onder). Het Trees/surfaces-platform (ex-Belgium from above, verrijkt met Ignacio's feedback) verhuist naar de BAP-backlog. De eerdere selectie (Municipal Budget Stress Lab) is geparkeerd.

## Idee-funnel — wat er gevallen is en waarom

Nuttig voor de pitch: toont selectiviteit, niet willekeur.

- **Energy ROI / Carte Solaire-achtige tools**: bestaan al → geen added value.
- **Budget stress lab**: te niche-publiek, te weinig ML-diepte.
- **Straatnamen, babynamen, Villo!, vogels**: descriptief — faalt de *pandas-test*: een journalist heeft hier geen data scientist voor nodig.
- **Belpex spike-forecasting**: sterk leerproject, maar publieke meerwaarde zwak — Belgische facturen zijn fees/taxes-gedomineerd (die kritiek werd zelf een concept: kandidaat 4).
- **Belgium from above & Good Move audit**: sterk, gehouden als fallback (zie Geparkeerd).

## Kandidaat 1 — De Vier Prijzen van Brussel ⭐⭐⭐⭐⭐ (leading)

### Kernvraag

> Vier systemen beweren dezelfde realiteit te beschrijven: de **marktvraagprijs** (Immoweb), de **wettelijke referentiehuur** (loyers.brussels), de **fiscale waarde** (kadastraal inkomen / intern AVM) en de **reële transactieprijs**. Waar, wanneer en waarom wijken ze af — en wat zegt die afwijking over wet, markt en fiscus?

### Waarom nú (de moordhoek)

- Sinds **1 mei 2025** is de Brusselse *loyer de référence* bindend: een huur >20% boven de referentie is **vermoedelijk misbruik**, afdwingbaar via de vredeschutter. Voor zover publiek in kaart gebracht: nog niemand heeft gemapt **waar de markt boven de wettelijke vork zit**.
- De referentieformules zijn **openbaar en auditeerbaar** ("Équations et variables additionnelles" op loyers.brussels) — een wettelijk regime dat je als data scientist volledig kunt reproduceren.
- Kadastrale waarden dateren in essentie van 1975: de kloof fiscus↔markt is een **fiscal-equity-kwestie** (grondslag van de onroerende voorheffing).

**Bronnen:** [loyers.brussels — formules](https://loyers.brussels/equations-et-variables-additionnelles) · [Droits Quotidiens — loyer de référence](https://www.droitsquotidiens.be/fr/question/quest-ce-que-le-loyer-de-reference-bruxelles) · [RTBF — bindend sinds mei 2025](https://www.rtbf.be/article/vers-la-fin-des-loyers-abusifs-a-bruxelles-la-region-adopte-un-outil-de-lutte-contraignant-11528592) · [Statbel — vastgoedverkopen per statistische sector, open](https://statbel.fgov.be/en/open-data/real-estate-sales-according-nature-property-deed-sale-statistical-sectors-nis7-and-nis9)

### De vier regimes

1. **Markt (vraagprijs)** — Immoweb-listings (huren én kopen); scraping of bestaande datasets.
2. **Wet (referentiehuur)** — publieke vergelijkingen van loyers.brussels, herberekenbaar per pandprofiel.
3. **Fiscaal (kadastraal/AVM)** — ⚠️ werkdata: uitsluitend via formele toestemming of in professionele context; de FPP-ruggengraat moet zonder kunnen.
4. **Realiteit (transacties)** — Statbel-microdata via onderzoeksaanvraag (via EHB-begeleider — student kan dit niet solo), of open fallback: Fednot-barometer per postcode + Statbel-open-data per statistische sector.

### Onderzoeksvragen

- **Q1 (publiek)**: waar overschrijdt de markt de wettelijke vork met >20% — de *vermoed-misbruik-kaart*? Wat voorspelt de kloof (buurt, oppervlakte, energieprestatie)?
- **Q2 (beleid)**: is de wettelijke referentie gekalibreerd op de marktrealiteit, en waar niet?
- **Q3 (fiscaal)**: hoe verhoudt de fiscale waarde zich tot de markt — wie is over- of onderbelast? (conditioneel op regime 3)
- **Q4 (markt)**: vraagprijs vs transactieprijs — de overpricing-kaart (conditioneel op microdata).
- **Q5 (causaal)**: heeft de soft cap — >20% boven de referentie = vermoedelijk misbruik, sinds 1 mei 2025 — de vraagsprijzen bewogen? **Event study rond 1 mei 2025** met behandeldifferentiatie per afstand-tot-de-cap: panden die vóór de invoering boven de vork zaten zijn gebonden (behandeld), eronder controle; zestien maanden naperiode beschikbaar. **Datavereiste**: vraagprijzen vóór mei 2025 — historische listing-archieven of werkdata (uitsluitend via governance-routes); eigen archivering vanaf dag 1 dekt enkel de naperiode. Let op anticipatie (aankondiging ver voor inwerkingtreding) en generieke markttrend. **Degradatie**: zonder vóór-data → cross-sectionele bindingsanalyse (aandeel listings boven de vork + gesimuleerde "waar zou de cap bijten"-kaart).

### ML-kern (wat het model dóét)

- Hedonische modellen per regime (GBM + SHAP) + **divergentie-modellering**: wat verklaart de kloof tussen regimes?
- Data engineering: een unified property record over vier bronnen met verschillende schema's en granulariteit.
- De deliverable is géén prijsvoorspeller maar een **afwijkingsanalyse met onzekerheid** — de pandas-test wordt ruim gehaald.

### DoD (90-uurs projectspoor)

1. Reproduceerbare pipeline: minstens regimes 1–2 volledig open; regime 4 indien de microdata-aanvraag slaagt.
2. Divergentie-rapport + interactieve verkenner (buurtkaart, voorbeeldpanden, uitlegbaar).
3. Eerlijk methodologisch verslag: representativiteit van vraagprijsdata, beperkingen, wat níet kan.
4. Stretch: artikelopzet voor lokale krant (BRUZZ/De Standaard-stijl).

### Data-governance — ontwerpeis nr. 1

- **Geen werkdata zonder formele, expliciete toestemming.** Doelbinding (GDPR) en het fiscale beroepsgeheim gelden persoonlijk; anonimiseren/aggregeren lost dat niet automatisch op.
- **Route A — Statbel *microdata for research***: aanvraag via de hogeschool (niet solo), confidentiality agreement, output uitsluitend anoniem/geaggregeerd. **Dag 1 versturen — de looptijd is het risico.**
- **Route B — Fednot**: statistisch/wetenschappelijk hergebruik voorzien; aanvraag via legal/analytical departments.
- **Route C (optioneel)**: vergelijking met het interne AVM uitsluitend met expliciete autorisatie van de administratie, liefst in professionele context; zonder autorisatie vervalt Q3 naar aggregaat-proxy.
- Architectuurprincipe: **elk regime is een plug-in**; geen enkel regime mag het project kunnen blokkeren.

### Risico's
- Immoweb-scraping (ToS) → bestaande datasets als alternatief; vraagprijs ≠ transactieprijs is zélf een bevinding, mits eerlijk gerapporteerd.
- Microdata-looptijd → open fallback klaarzetten (postcode-/sectorniveau).
- Scope: één stad (Brussel); eerst huren, dan kopen.

### Portfolio-fit

Fiscaal domein (beroepsvoorsprong) × housing × toegepaste ML × data-journalisme. Pitch-in-one: *"vier prijzen voor één dak — waar wijken wet, markt en fiscus af?"* Past exact op de ECTS-vragen (definition of done, ambities, maatschappelijke meerwaarde).

## Kandidaat 2 — Open pensioen-microsimulator (P1)

> Wat krijg *jij*? Een transparant open model tegenover de black-box officiële simulatoren.

- **Model doet**: cohort-microsimulatie — Statbel-bevolkingsprojecties + wettelijke pensioenparameters → vervangingsratio's per carrièreprofiel onder scenario's (pensioenleeftijd, indexatie, hervormingen) met onzekerheidsbanden.
- **Data**: alles open (Statbel-projecties, pensioenstatistieken, wetteksten).
- **Publieke inzet**: perennial top-3-zorg; de budget-stress-lab-instinct, maar voor het getal dat elke burger persoonlijk vreest.
- **Methode-familie**: demografie + simulatie + onzekerheid — nieuw voor jou, speelt wel minder op je ML-sterkte.
- **Risico**: actuariële vereenvoudiging moet transparant zijn — wat ook precies het punt is.

## Kandidaat 3 — DIY Belgische prijsindex (P2)

> Niemand vertrouwt de officiële inflatie. Bouw de onafhankelijke tegenhanger.

- **Model doet**: dagelijkse scrapes van online supermarkten → **product-matching over tijd en ketens heen** (harde entity-resolution-ML) → matched-model prijsindices (echte CPI-methodologie) → vergelijking met Statbel per categorie; stretch: gepersonaliseerde mandjesexplorer ("jouw inflatie").
- **Precedent**: MIT Billion Prices Project — bewezen publieke waarde, nooit open gerepliceerd voor België.
- **Publieke inzet**: inflatie = topzorg; "jouw inflatie hangt af van jouw mandje".
- **Risico's**: scraping-robustheid (sites wijzigen), online-assortimentsbias.

## Kandidaat 4 — Anatomie van de Belgische elektriciteitsrekening (#4p)

> Waarom is mijn factuur €X? — en welk deel ervan is zelfs maar beïnvloedbaar?

- **Model doet**: factuurdecompositie per profiel (vast vs dynamisch tarief vs zon+batterij) onder echte Belpex-historiek: commodity / netwerktarieven / heffingen / btw; scenario-simulator met onzekerheid. Het forecasting-leerdoel (spike-classificatie) blijft behouden als commodity-module.
- **Data**: publiek (VREG/BRUGEL-tariefbladen, Belpex/Elexys, Elia open data).
- **Publieke inzet**: hoog — antwoord op de vraag die iedereen stelt; de eigen kritiek op Belpex-optimisatie ("fees & taxes domineren") wordt hier de bevinding zelf.
- **Risico**: dicht bij het energy-dashboard-wereldje; origineel genoeg mits de decompositie centraal staat.

## BAP-backlog — Trees & Surfaces (ex-Belgium from above, ronde 5)

Platformconcept voor de Bachelorproef (meer domeinen, meer tijd), verrijkt met Ignacio's feedback (2026-09-17):

- **Per-boom-registers (verifieerd)**: Gent *Locaties bomen Gent* — **68.240 bomen** via ODS-API (`data.stad.gent/api/explore/v2.1/catalog/datasets/locaties-bomen-gent/records`), velden: straatnaam, **aanlegjaar** (schaars gevuld), sortiment/soort, hoogte, diameter, stamomtrek, beheerfase, eigenaar + geometrie; Brussel: *arbres-bomen-vbx-be-bm* + Bruxelles Mobilité-bomen + opmerkelijke bomen.
- **Overige geverifieerde lagen**: canopy/heat op 1m (LiDAR 2021 + DSM/DTM + Landsat/Sentinel); **fietsentellers met historiek sinds 2018** (bike API `request=history`); STIB GTFS + real-time wachttijden (aanbod ✅, bezetting ❌); terrassen enkel via stedenbouwkundige vergunningsdatasets (partieel); voetgangersstromen ❌ niet open.
- **Ignacio's optimalisatielaag**: bomen × temperatuur × straargebruik → multi-objective Pareto-fronten (groen vs mobiliteitsfrictie); haalbaar op canopy/heat × fietsdata × PT-aanbod; bezetting/voetgangers blijven proxies.
- **Confunders**: elektrische-busovergang (routewijzigingen, grotere vloot, capex) = structurele breuk in OV-tijdreeksen — expliciet behandelen.
- **Gent-editie extra's**: GRB bevat bouwjaarlabels (era-datering van bebouwing); Gentse open-datacultuur.
- **Friki-laag (Ignacio, 2026-09-17)**: *computational Jane Jacobs* — CV-classificatie modernistisch vs traditioneel (Brussels hook: 'brusselization'/Manhattan-torens) × niet-gemotoriseerd verkeer. Bottleneck: gebruiksmeting (fietsentellers = vaste punten, kleine n; voetgangers ❌). Ontwerp dat overleeft: vorm-features per tellerlocatie (+ steden combineren voor n) → gemeten gebruik voorspellen; CV = feature-extractor. **Morfologie-shortcut**: 'toren-in-park' meetbaar uit LiDAR+footprints (hoogte, bedekkingsgraad, setback, blokgrootte) zonder fotolabels; facade-CNN (Mapillary, klein handgelabeld set; GRB-bouwjaar 1958–1975 als validatie) als visuele friki-laag erbovenop.
- **De Drie Leeftijden van een Brussels pand (2026-09-17, na Ignacio's facadisme-kritiek)**: Ignacio's label-noise-probleem ("bouwjaar 1905" = vaak enkel één bewaarde muur, facadisme) omdraaien tot onderzoeksvraag: reconstrueer per pand *drie leeftijden* — **registersjaar** (GRB-bouwjaar, Flanders), **gevelstijljaar** (straatbeeld-CNN), **structureel tijdperk** (Bruciel multi-epoch luchtfoto's 1930s→nu: change detection achter de gevel — 'barrabasadas' zichtbaar van boven). Output: **gekwantificeerd facadisme in Brussel** (welk aandeel '1905' is eigenlijk een masker?) — erfgoedbeleidsdebat in cijfers, én eerlijke era-labels voor het hele platform. Zaadlabels: eigen fotoarchief *Buildings of Brussels* (Tumblr + Instagram; adres + architect + datum + stijl per post, art nouveau → brutalisme) + Mapillary voor schaal. ⚠️ To verify: Bruciel-hergebruikslicentie voor bulkverwerking (interactief gebruik is vrij; download/onderzoek vraagt mogelijk toestemming).

## Geparkeerd — fallbacks, te heractiveren

- **Good Move-causale audit** — auto-tellers: publieke API live-only; historiek in de Irma-databank bestaat per officiële metadata → formele aanvraag uitstaand. **Fietsentellerhistoriek sinds 2018** biedt deels substituut (fietsstromen vóór/na circulatieplannen). Fallbacks: IRCELINE (decennia), Statbel ongevallen (geogecodeerd), prospectief ontwerp.
- **Municipal Budget Stress Lab** — geparkeerd, zie archief hieronder.
- **Energy model audit** — blijft privaat- of BAP-materiaal.

## Archief — eerdere brainstormronde (fantasy/data-sentinel/agent-eval-lijnen)

Bronnen: juegosmineros/nursultan (eigen platform, echte gebruikers, eigen data), project-atom (werkervaring), *Essential Math for Data Science*.

Ideëen A–F hieronder blijven sterke BAP-kandidaten (met name B: Data Integrity Sentinel en de Agent Eval Harness); de uitgewerkte pitch-drafts staan onderaan dit document.

### Gearchiveerde domeinshortlist — ronde 1

The FPP does not need to use fantasy sports. A stronger direction may be **decision intelligence for real systems**:

### 1. Energy model audit and operational optimization ⭐⭐⭐⭐

The Carte Solaire report already covers roof potential, production, household consumption, self-consumption, CO₂, installation cost, green certificates, bill gains, net gains, financing options and discounted payback. A new ROI calculator would therefore add little.

The credible gap is the **closed loop between prediction and reality**:

- **Option A — model audit**: compare the Carte Solaire estimate with measured production, consumption and financial outcomes from `~/projects/energy-dashboard/`; quantify which assumptions drive the error and how uncertainty should be reported.
- **Option B — operational optimization**: use solar forecasts, electricity prices and household demand to evaluate forecast-aware appliance scheduling; compare actual or simulated savings against simple baselines.

- **DoD**: reproducible evaluation pipeline + clearly defined baselines + error/savings analysis + report/dashboard
- **Data**: own data only after removing private details; publish synthetic or aggregated examples
- **Scope**: one installation, one evaluation question, no replacement for Carte Solaire
- **Portfolio**: empirical validation, time-series reasoning, financial modelling and applied decision support

### 2. Public Transport Reliability Intelligence ⭐⭐⭐

Estimate delay or disruption risk for selected routes or connections, then show the impact on passengers. Use a temporal baseline, walk-forward evaluation and a small dashboard. The scope is one network and one prediction target—not a full journey planner.

### 3. Municipal Budget Stress Lab ⭐⭐⭐⭐ — geparkeerd (ronde 5)

OpenBudgets is mainly a procurement and subsidy transparency portal, not a complete municipal-budget simulator. The FPP can use the official Brussels local-authority budget/account compilations as its base and add a transparent **what-if and resilience layer**: can a municipality absorb energy-price shocks, inflation, wage pressure or reduced revenue while preserving services and planned investment?

- **Question**: which budget categories and assumptions determine when a municipality becomes financially stressed?
- **Data**: official Brussels municipal budgets/accounts; OpenBudgets procurement and subsidy data can be supplementary context
- **Scenarios**: baseline continuation; energy-cost shock; inflation/wage shock; revenue decline; combined stress case
- **DoD**: cleaned reproducible budget model + scenario engine + sensitivity analysis + decision-oriented report/dashboard
- **Evaluation**: reproduce historical totals within a documented tolerance, compare scenarios, identify the variables with the greatest effect and report uncertainty
- **Scope**: one municipality or a small comparable set, a limited number of budget categories, no political recommendations and no claim to predict the future
- **Portfolio**: data modelling, forecasting/scenario analysis, financial reasoning, visual communication and responsible interpretation

**Sources:** [Brussels municipal budgets and accounts](https://pouvoirs-locaux.brussels/mise-a-jour-juillet-2026-comptes-et-budgets-communes-bruxelloises-service-ordinaire) · [OpenBudgets](https://openbudgets.be.brussels/)

### 4. Company Financial Health Signals ⭐⭐

Use public company accounts to identify unusual changes in liquidity, margins or debt. Keep it descriptive and research-oriented—no investment recommendations. The main risk is finding a clean, comparable dataset.

**Best first candidate:** Building Energy Retrofit Prioritizer. It combines energy, buildings, urban planning, finance and applied ML while producing a meaningful visual result.

### A. Draft/Points Intelligence — ML-forecasting voor juegosmineros ⭐

Spelerspunt-voorspellingen per speelronde met onzekerheid, vertaald naar captain/transfer-advies in de UI.

- **Data**: al voorhanden via de ingester (spelerstatistieken, fixtures, historieke punten)
- **DoD**: model dat een naive baseline (gemiddelde laatste 3 speelronden) verslaat in backtest + calibratiecheck + deployed widget in één game (feature flag)
- **Portfolio**: ⭐⭐⭐ volledige stack — pipeline → model → deployment → UI → evaluatie, met echte gebruikers
- **Wiskundeboek**: direct toepasbaar (regressie, kansverdelingen, calibratie)
- **BAP-lijn**: uitbreiden naar opponent modeling, per-positie modellen, explainability (SHAP), userevaluatie
- Scope voor FPP: één competitie, één adviesfeature — rest is BAP

### B. Data Integrity Sentinel — betrouwbare data voor publieke analytics ⭐⭐⭐

Stille fouten in data pipelines detecteren vóór ze analyses, rapporten of modellen beïnvloeden. Gebruik uitsluitend open of synthetische data, bijvoorbeeld een publiek administratief datasetje met meerdere tabellen en periodieke updates.

- **Checks**: schemawijzigingen, versheid, ontbrekende waarden, duplicaten, domeinregels, referentiële integriteit en distributieverschuivingen
- **DoD**: herhaalbare pipeline + minstens zes foutklassen + fault-injection tests + reliability report/dashboard
- **Meetbaar**: detecteert minstens 90% van 20 geïnjecteerde incidenten en rapporteert de false-alarm-rate
- **Portfolio**: data engineering, data management, kwaliteitscontrole, observability en verantwoord gebruik van data
- **Scope**: één dataset, één CLI/report of dashboard, geen productieplatform

### C. Active-learning entity matching (project-atom-lijn, synthetische data)

Hoeveel label-inspanning bespaart active learning t.o.v. random sampling op de matching-lib?

- **DoD**: benchmark op synthetische data met leercurves + rapport
- **Portfolio**: ⭐⭐⭐ voor data-rollen, onderzoekser van vorm (stevige BAP-kandidaat)
- Voorwaarde: akkoord werkgever; géén echte belastingdata

### D. Live draft-assistant

Waardecurves per positie + scarcity-model tijdens de draft (draft-setup-2026 bestaat al).
- Overlapt sterk met A — kan de UI-gefacesiede uitloper zijn

### E. Explainable match reports (LLM-agent)
Gegronde na-match analyses genereren voor fantasyspelers. Leuk, maar "definition of done" lastig hard te maken.

> [!tip] Strategie (ronde 5): **De Vier Prijzen van Brussel** is geselecteerd als FPP-richting — wettig en actueel (referentiehuur bindend sinds 1 mei 2025), publiek, dicht bij de fiscale beroepservaring. De pitch-draft staat in dit document; de Trees/surfaces-platformversie is BAP-backlog. Data-governance (geen werkdata zonder formele toestemming) blijft ontwerpeis nr. 1.

> ⚠️ Geen gevoelige gegevens (geen contribuabel-/cliëntdata) — zie SECURITY.md project-atom

## Pitch draft — De Vier Prijzen van Brussel (geselecteerd FPP)

**Categorie**: eigen voorstel (fiscaal × housing × data-journalisme)

### Situatie

Brussel heeft sinds **1 mei 2025** een bindende *loyer de référence*: een huur die meer dan 20% boven de wettelijke referentiehuur ligt, wordt **vermoedelijk misbruik** en is afdwingbaar voor de vredeschutter. De referentie is een **openbaar, auditeerbaar algoritme**: sinds de arrêtés van 30 juni en 6 oktober 2022 (Moniteur 19.10.2022) geen grid met 7 wijkgroepen meer, maar **8 vergelijkingen per woningtype** over de **statistische sectoren** (moeilijkheidsindex −2…+4), met €-correcties voor PEB, garage, tweede badkamer e.d.; in **januari 2026 geïndexeerd** op de gezondheidsindex (aug 2021 → dec 2025, k = 136,69/112,74 = 1,21244).

Tegelijk beweren **vier waarderingswerelden** de waarde van hetzelfde goed te kennen: de **marktvraagprijs** (Immoweb), de **wettelijke referentiehuur**, de **fiscale waarde** (kadastraal inkomen / intern AVM) en de **reële transactieprijs** (notariële akten). Niemand heeft hun onderlinge afwijking systematisch in kaart gebracht — terwijl die afwijking bepaalt of de nieuwe wet bijt, wie fiscaal over- of onderbelast is, en waar vraagprijzen losstaan van de werkelijkheid.

### Frontrun — wat er al bewezen is (dag 1–2, vóór de semesterklok)

Het project is geen plan meer; de kern is **gebouwd en geverifieerd** (repo `~/projects/four-prices`, 63 tests groen, 21 commits):

- **De wet is code.** De gepubliceerde vergelijkingen + indexatie zijn geïmplementeerd; adres → statistische sector → index werkt end-to-end (de officiële IRISnet-dienst + de 724-sectoren-GeoJSON van de calculator zelf).
- **De wet zoals berekend is óók code — en ze wijkt af.** De officiële calculator bleek een server-side API; 50+ gevalideerde sondes reconstructeerden zijn werkelijke raster **tot op de euro**. Bevinding: de bijkomende variabelen (PEB, garage, indexcoëfficiënt) volgen de wettelijke indexatie **exact** (× 1,21244), maar de **typekern is stilzwijgend heringeschat** — gepubliceerde wet × k vs. bedienende calculator:

  | type (repr. opp.) | gepubliceerd × k | bedienend | verschil |
  | --- | --- | --- | --- |
  | studio 30 m² | 641 € | 758 € | **+18,2%** |
  | apt 1 ch 55 m² | 802 € | 926 € | +15,5% |
  | apt 2 ch 75 m² | 964 € | 1095 € | +13,5% |
  | huis 4+ 160 m² | 1571 € | 1727 € | +9,9% |

  — het grootste gat bij de **goedkoopste segmenten**, waar de wet het hardst moet bijten. Zes gedocumenteerde variabelen blijken bovendien in de calculator géén effect te hebben, en de antwoordband is [70%, 120%] — niet de gedocumenteerde ±10%-vork.
- **Data-assets binnen**: officiële index-xlsx (650 sectoren), 724-sectoren-geometrie, Statbel-transacties 2013–2024 (499.838 aggregaten), alles reproduceerbaar via `make fetch-*`; `make map` levert de joinbare sectorlaag (SVG + CSV) en `make explorer` een standalone demo; de SLRB-vraag is als e-mail klaar (met cijfers).

Dit is het project in het klein: **de wet zoals gepubliceerd vs. de wet zoals berekend** — een vijfde divergentiepaar naast de vier prijzen.

### Voorstel

Een **convergentieanalyse**: één unified property record over de regimes, hedonische modellen per regime (GBM + SHAP), en als eigenlijk product de **divergentie- en causale analyse** (Q1–Q5, zie kandidaat 1 hierboven — incl. de event study naar het effect van de soft cap sinds 1 mei 2025).

### Definition of done

1. ~~Reproduceerbare pipeline met regimes 1–2 volledig open: marktvraagprijzen + de wettelijke referentie **hergerekend vanuit de gepubliceerde formules en gevalideerd tegen de officiële simulator** op loyers.brussels~~ ✅ **frontrun klaar** — inclusief de gereconstrueerde bedienende raster (validatie tot op de euro)
2. De **vermoed-misbruik-kaart**: aandeel en locatie van vraagprijzen >20% boven de referentie, per buurt en pandprofiel, met onzekerheid
3. Divergentie-rapport + interactieve explorer (kaart + pandprofiel-lookup + uitleg)
4. Methodologisch verslag: representativiteit van vraagprijsdata, beperkingen, wat níet kan — eerlijkheid als kwaliteitseis
5. Stretch (conditioneel): Q5-event-study, Q3/Q4 indien microdata/autorisatie beschikbaar

### Eigen ambities

- De fiscale beroepservaring omzetten in een **publiek, reproduceerbaar artifact** — het tegengestelde van black-box simulatoren
- Eerlijke ML centraal: onzekerheidsbanden, uitlegbaarheid (SHAP), expliciete aannames
- Data-journalistische ambitie: output die een lokale krant ongewijzigd kan overnemen

### Meerwaarde

- **Maatschappelijk**: eerste open mapping van waar de nieuwe huurwet bijt; inzicht in fiscale over-/onderwaardering van woningen
- **Economisch**: huurders kunnen vraagprijzen toetsen; eigenaars/makelaars krijgen referentiepunten; de regio krijgt een evaluatie-instrument voor haar eigen wet
- **Educatief**: reproduceerbare methodologie (code + data + rapport) als voorbeeldproject

### Scope & planning (±90u)

| Weken | Fase |
| ----- | ---- |
| 1–2 | ~~Governance dag 1: Statbel-aanvraag via EHB-begeleider; eigen listing-archivering starten; wettelijke formule implementeren + validatie~~ **frontrun voltooid** (formule + validatie + bedienende raster + adresresolutie + Statbel-transacties); resterend: mails verzenden, scraping-bron beslissen |
| 3–5 | Unified property record + hedonische modellen regimes 1–2 |
| 6–8 | Divergentieanalyse: misbruikkaart, Q1–Q2, explorer-prototype |
| 9–11 | Conditionele modules: Q5 event study (of bindings-degradatie), Q3/Q4 indien beschikbaar |
| 12–13 | Rapport, artikelopzet, portfolio write-up |

### Risico's & mitigatie

- **Vraagprijsdata vóór mei 2025** (voor Q5) → historische archieven/onderzoeksdatasets; werkdata uitsluitend via governance-routes; anders Q5 naar cross-sectionele bindingsanalyse
- **Scraping/ToS** → bestaande datasets + eigen archivering vanaf dag 1
- **Microdata-looptijd** → open fallback (Fednot per postcode, Statbel per statistische sector)
- **Scope creep** → plug-in architectuur: elk regime onafhankelijk; huren eerst, kopen later
- **Gevoeligheid** → geen individuele pandidentificatie in publieke outputs; buurt-/profielniveau

## Pitch draft — Matchday Intelligence (idee A — archief)

**Categorie**: eigen voorstel

### Situatie

juegosmineros draait twee fantasycompetities (nursultan + beyoglu) met echte gebruikers en een eigen data-ingester. Spelers nemen hun captain- en transferbeslissingen op gevoel — het platform heeft de data, maar geen voorspellende laag.

### Voorstel

Een forecasting-service die per speelronde de te verwachten punten per speler voorspelt **met onzekerheid**, vertaald naar een captain-/transfer-advieswidget in één game (achter feature flag).

### Definition of done

1. Backtest-harness over de beschikbare historische speelronden (walk-forward), waarin het model **twee naive baselines verslaat** (gemiddelde laatste 3 speelronden; seizoensgemiddelde) op MAE
2. **Calibratiecheck**: voorspelde intervallen bevatten de werkelijke punten op het beloofde niveau (reliability diagram in het rapport)
3. Advieswidget **live in productie** in één game, achter feature flag
4. **Evaluatierapport**: methodologie, resultaten, beperkingen, eerlijke faalanalyse

### Eigen ambities

- De volledige ML-lifecycle beheersen op een systeem dat ik zelf bezit: data → model → deployment → evaluatie
- Wat ik lees (*Essential Math for Data Science*) en volg (Data Science, Machine Learning) direct toepassen: regressie, kansverdelingen, calibratie
- Een portfolio-stuk bouwen dat aantoonbaar in productie draait bij echte gebruikers — fundament voor de groeps-BAP

### Meerwaarde

- **Economisch**: eigen platform met echte gebruikers — retention- en engagementfeature; maakt de competitie sportiever en de games aantrekkelijker
- **Maatschappelijk/educatief**: transparante toepassing van toegepaste ML (het rapport legt uit *waarom* het model iets voorspelt), bruikbaar als voorbeeld voor medestudenten

### Scope & planning (±90u)

| Weken | Fase |
| ----- | ---- |
| 1-2 | Data-audit ingester + backtest-harness + baselines |
| 3-5 | Eerste model (regressie/GBM) per competitie |
| 6-8 | Onzekerheid + calibratie |
| 9-11 | API + widget + feature flag + monitoring (sentinel-mindset) |
| 12-13 | Evaluatierapport + portfolio write-up |

### Risico's & mitigatie

- **Te weinig historische data** → start met de competitie met de langste geschiedenis; zonodig openbare voetbaldata bijvoegen
- **Scope creep** → één competitie, één adviesfeature; de rest is BAP-materiaal
- **Tijdstekort** (job + 4 vakken) → harde fallback binnen de DoD: backtest + kalibratie + rapport tellen, widget is de stretch

## Pitch draft — Agent Eval Harness (idee F — archief)

**Categorie**: werkveld + eigen voorstel (geïnspireerd op project-atom, domeinagnostisch gebouwd op synthetische data)

### Situatie

Op het werk draaien LLM-agents productieworkflows (matching, validatie, verrijking) met human review in de lus. Agents zijn niet-deterministisch en de pijplijn verandert voortdurend (prompts, modellen, tools) — elke wijziging is een gok, regressies vallen pas op tijdens menselijke review. Bestaande tooling (promptfoo, DeepEval, LangSmith, Braintrust) dekt algemene cases af, maar **multi-step agent-workflows met human-review-checkpoints** zijn net het zwakst gedekte gebied.

### Voorstel

Een open-source **evaluatieharness voor multi-step agent-workflows**: golden test cases (synthetisch), een runner (geversioneerd, herhaalbaar), scorers (programmatisch + rubric/LLM-as-judge), en regressie-diffing tussen runs — geïntegreerd in CI. Gedemonstreerd op één agent-workflow, herïmplementeerd op synthetische data.

### Definition of done

1. Golden set van ≥50 synthetische cases met verwachte uitkomsten, inclusief edge cases
2. Runner + scorers: outcome-scoring (programmatisch) én rubric-scoring (LLM-as-judge, met calibratiecheck)
3. De suite detecteert **≥90% van 20+ geïnjecteerde regressies** (subtiel verslechterde prompts, gewisselde tools, gedegradeerde retrieval), met gemeten false-alarm-rate
4. Regressierapport dat twee pijplijn-versies diff't, draaiend in CI
5. Publieke repo + eerlijk rapport (wat het vangt, wat het mist)

### Eigen ambities

- Mijn professionele voorsprong (agents bouwen op het werk) omzetten in een streng, publiek artifact
- Evaluatiemethodologie beheersen — het actuele frontier-probleem van AI engineering
- Inspecteerbaar portfolio op GitHub, als tegenhanger van het vertrouwelijke werk op het werk

### Meerwaarde

- **Economisch**: agents in productie falen stil; eval-tooling vangt regressies vóór deployment en verlaagt review-kosten
- **Maatschappelijk**: betrouwbare AI bij publieke administraties; transparante, herbruikbare methodologie

### Scope & planning (±90u)

| Weken | Fase |
| ----- | ---- |
| 1-2 | Taakdefinitie + ontwerp golden set (synthetisch) |
| 3-5 | Runner + programmatische scorers + baseline runs |
| 6-8 | Rubric/LLM-as-judge + calibratie + regressie-diffing |
| 9-11 | Geïnjecteerde-regressie-experiment (de 90%-demo) + CI-integratie |
| 12-13 | Rapport + open-source release (README, docs) |

### Risico's & mitigatie

- **Vertrouwelijkheid werkgever** → domeinagnostisch op synthetische data; eventueel sign-off voor framing
- **LLM-as-judge instabiel** → inter-run variantie meten, calibratie rapporteren; DoD-floor zonder rubric
- **Tijdstekort** → fallback: outcome-only scoring, kleinere golden set
- **"Wiel opnieuw uitvinden"** → positioneren als niche (agent-workflows + review-checkpoints), vergelijking met bestaande tools in het rapport

### Frontrun-verificatie (2026-09-17) — de open ruggengraat is 100% geverifieerd

| Component | Status | Bron |
| --------- | ------ | ---- |
| Wettelijke formule | ✅ alle coëfficiënten publiek — `loyer = (0.1758082 + 1.0207648×(A + B/opp) + 0.2490667 [état=2] + 1.042853 [état=3] − 0.6455585×index) × opp + attributen`; A/B-constanten per 8 woontypes; attribuutcorrecties exact in € (2e badkamer +88.55, garage +40.11/st, berging +0.71, geen cv −18.68, geen thermoregeling −16.87, geen recreatieruimte −15.76, PEB A +164.16 … G −21.89) | [loyers.brussels — équations](https://loyers.brussels/equations-et-variables-additionnelles) |
| Indice synthétique de difficulté | ✅ downloadbaar per statistische sector (.xls), −2 tot +4 | [loyers.brussels — à propos](https://loyers.brussels/a-propos-des-loyers-de-reference) |
| Wettelijke basis nieuwe regime | ✅ gepubliceerd 19.10.2022 (numac 2022033354) | [Moniteur belge](https://www.ejustice.just.fgov.be/cgi/article_body.pl?caller=summary&language=fr&numac=2022033354&pub_date=2022-10-19) + [base légale](https://loyers.brussels/base-legale) |
| Buurtgeometrie | ✅ Monitoring des Quartiers-wijken: SHP/GeoJSON/GPKG + WFS | [opendata.brussels](https://opendata.brussels.be/explore/dataset/quartiers-du-monitoring-des-quartiers-ibsa-perspective-rbc/) |
| Transactie-fallback (regime 4) | ✅ Statbel NIS9: **prijzen per statistische sector** — Q10/Q25/Q50/Q75/Q90 in € per pandtype (drempel ≥16 transacties) — veel rijker dan postcode | [Statbel open data](https://statbel.fgov.be/en/open-data/real-estate-sales-according-nature-property-deed-sale-statistical-sectors-nis9) |
| Vóór-mei-2025 vraagsprijzen (Q5) | ✅ route gevonden — VUB-researchportaal: IMMOWEB-dataset vanaf jan. 2015 (EPC, bouwjaar, prijs, kenmerken); aanvraag bij VUB nodig | [VUB research portal](https://researchportal.vub.be/en/datasets/immoweb/) |
| Validatiedoel | openbare simulator op loyers.brussels (iframe-tool) | [loyers.brussels](https://loyers.brussels/) |

**Prior art om te kennen (en te overtreffen)**: IJHMA-paper *Predictability of Belgian residential real estate rents using tree-based ML models and IML techniques* (boommodellen op Belgische huren) — bevestigt dat de bijdrage niet 'een hedonisch model bestaat' is, maar de **multi-regime divergentie + causaliteit**. Precies onze framing.

**Dag-1 checklist (definitief)**
1. Wettelijke formule implementeren (constanten + index-xls + attributen) en valideren tegen de loyers.brussels-simulator op ~20 pandprofielen
2. Eigen listing-archivering starten (vult MAL/DAS/FPP naperiode)
3. EHB-begeleider: Statbel-microdata-aanvraag versturen (looptijd = risico)
4. VUB e-mailen voor de IMMOWEB-dataset 2015+ (Q5 pre-periode)
5. Docentengesprekken: Weemaels (pitch) → Hambrouck (DAM) → MAL-docent → DAS-docent (eigen case?)

## Werkstuk-synergie S1 (2026-09-17)

Eén domein, vier beoordelingslenzen — mits expliciet verklaard en goedgekeurd per docent:

| Vak | Gewicht | Lens op De Vier Prijzen | Te verifiëren |
| ---- | ------- | ------------------------ | -------------- |
| FPP | 100% portfolio | het hele project (pitch-draft klaar) | goedkeuring Weemaels |
| DAM | 100% werkstuk | **datalaag**: relationeel model van de vier regimes (pandprofiel, buurt, listing, referentiehuurberekening, fiscale/venale aggregaten) + NoSQL-documentstore voor rauwe listings (referencing vs embedding), views, indexen, security/PII-veilig ontwerp | Hambrouck: domeinkeuze + overlapregeling |
| MAL | 50% werkstuk | **modellaag**: hedonische regressie (regularized linear vs boom-ensembles), classificatievariant ("overschrijdt deze listing de vork van +20%?"), calibratie, bias-variance, SHAP | MAL-docent: vrijheid datasetkeuze |
| DAS | 50% werkstuk | **pijplijnlaag**: scrape → cleaning van incomplete & contaminated listings → model → website-explorer + ethische reflectie (D9) | ⚠️ fiche zegt "data supplied by companies" — vragen of eigen realistische case mag |

Patroon: zelfde domein, verschillend competentiebewijs per vak (schema vs model vs pipeline vs geheel) — geen zelf-plagiaat mits expliciet verklaard. Limit-stop: weigert een docent, dan valt dat vak terug op zijn eigen case; de FPP-ruggengraat verandert niet.

## Planning

| Fase | Wat | Deadline |
| ---- | --- | -------- |
| Voorstel uitwerken + pitch |   |         |
| Goedkeuring coach |   |         |
| Uitvoering project |   |         |
| Portfolio afwerken |   | januari  |

## Links

- [[FPP_productnote]] — operationele productnota (productvorm, MoSCoW, milestones & gates, bronnenregister, beslissingslog)
- [[FIN_planning]] — projectidee kan uitgroeien tot final work
