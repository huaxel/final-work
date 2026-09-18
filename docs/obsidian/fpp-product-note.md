---
tags: [fpp, productnota, brussel, housing]
status: pre-fase — pitch nog niet goedgekeurd
created: 2026-09-17
---

# De Vier Prijzen van Brussel — Productnota

**Productvorm**: data-product (unified property record) + divergentie-analyse + interactieve explorer
**Context**: EHB Future Proof Project, coach Weemaels, 90u projectspoor
**Code**: `~/projects/four-prices` — 63 tests groen: gepubliceerde wet + indexatie k=1,21244, bedienend raster, adresresolutie, R1 JSONL-archief, Statbel R4-loader, coverage-audit, kaart-APA en standalone explorer; R3 blijft governance-verzegeld, listingcollector blijft ToS-afhankelijk
**Zwaartekracht**: pitch & onderzoeksvragen in [[FPP_planning]] · werkstuk-synergie in [[FPP_planning]] · dataverificaties in [[FPP_planning]]

## 1. One-liner

> Vier waarderingsregimes — **marktvraagprijs, wettelijke referentiehuur, fiscale waarde, reële transactieprijs** — beweren hetzelfde pand te kennen. Dit product reconstrueert ze alle vier open en reproduceerbaar, meet waar ze uit elkaar lopen, en maakt die divergentie doorzoekbaar per buurt.

## 2. Probleem & publiek

**Probleem.** Sinds 1 mei 2025 is de Brusselse referentiehuur bindend recht: >20% boven de referentie = *vermoedelijk misbruik*, afdwingbaar voor de vredeschutter. Maar niemand kan publiek antwoorden op de eerste-ordevragen: waar zit de markt boven de wettelijke vork? Is de vork zelf goed gekalibreerd? En hoe verhoudt de fiscale waarde zich tot de werkelijkheid — wie is over- of onderbelast?

**Gebruikers.**

| Gebruiker | Vraag | Productdeel |
| --------- | ------ | ------------ |
| Huurders | "Is mijn huur juridisch toetsbaar?" | Explorer: pandprofiel → referentie + vork |
| Eigenaars/makelaars | "Welke prijs is verdedigbaar?" | Zelfde lookup, andere lezing |
| Beleid (SLRB/regio) | "Blijft de kalibratie correct na invoering?" | Q2-kalibratieanalyse |
| Journalisten | "Waar bijt de nieuwe wet?" | Misbruikkaart + artikelopzet |

## 3. Wat we bouwen — drie productlagen

### L1 — Datalaag: de unified property record

Pandprofiel-centrisch record (type, oppervlakte, staat, PEB, sector/wijk, kenmerken). Elk regime is een **plug-in** die hetzelfde profiel naar een eigen prijs wereld-transformeert:

| Plug-in | Input | Output | Validatie | Status |
| ------- | ----- | ------ | --------- | ------ |
| R1 Markt | listings (Immoweb, eigen archief) | vraagsprijzen + attributen | kwaliteitsaudit volledigheid | ✅ start dag 1 |
| R2 Wet | gepubliceerde formules + index-xls | referentiehuur + vork per profiel | officiële simulator op ~20 profielen | ✅ 100% implementeerbaar geverifieerd |
| R3 Fiscus | kadastraal/AVM | fiscale waarde | — | ⚠️ uitsluitend via governance-route |
| R4 Realiteit | Statbel NIS9 (fallback), microdata (indien) | transactieprijs-percentielen per sector | representativiteitscheck | ✅ loader + filters / ⚠️ microdata |

### L2 — Analyselfaag

Hedonische modellen per regime (GBM + SHAP), divergentiefeatures per profiel/buurt (markt − wet, markt − realiteit, …), en de onderzoeksvragen Q1–Q5 uit [[FPP_planning]]: misbruikkaart, kalibratie, fiscale equity (conditioneel), overpricing (conditioneel), soft-cap event study (conditioneel op VUB-dataset).

### L3 — Presentatielaag

Interactieve explorer (kaart + pandprofiel-lookup), methodologisch verslag (eerlijkheid als kwaliteitseis), artikelopzet voor lokale krant.

## 4. Scope — MoSCoW

- **MUST**: R2-formule geïmplementeerd + gevalideerd · R1-archivering lopend · Q1-misbruikkaart · explorer-prototype · methodologisch verslag
- **SHOULD**: Q2-kalibratie · NIS9-koppeling (R4-fallback) · VUB-dataset → Q5
- **COULD**: microdata (Q4) · AVM-vergelijking (Q3, alleen met autorisatie) · Fednot per postcode
- **WON'T** (dit semester): koopmarkt als hoofdspoor · productiescraper · juridisch advies · andere steden

## 5. Milestones & gates (13 weken, ±90u)

| Weken | Mijlpaal | Gate | Fallback |
| ----- | -------- | ---- | -------- |
| 1–2 | Formule + validatie; archivering start; governance-mails (Statbel via coach, VUB, docenten) | ≤2% afwijking op 20 simulatorprofielen | interpretatiekeuzes documenteren |
| 3–5 | Unified record + R1-dataset | n ≥ 500 bruikbare listings | n verlagen, buurtaggregatie |
| 6–8 | Q1 + Q2 + explorer-prototype | demo begrijpelijk voor 2 buitenstaanders | kaart-APA's als statisch artefact |
| 9–11 | Conditionele modules (Q5 / bindingsanalyse; Q3/Q4 indien) | — | Q5 → bindingsanalyse; Q3/Q4 → weglaten |
| 12–13 | Rapport + artikelopzet + portfolio | inleverklaar | — |

## 6. Bronnenregister (geverifieerd 2026-09-17)

| Bron | Wat | Status |
| ---- | --- | ------ |
| [loyers.brussels — équations](https://loyers.brussels/equations-et-variables-additionnelles) | alle formulecoëfficiënten + attribuutcorrecties in € | ✅ |
| loyers.brussels — indice synthétique de difficulté (.xls per statistische sector, −2 tot +4) | formule-input | ✅ downloadbaar |
| [Moniteur 19.10.2022, numac 2022033354](https://www.ejustice.just.fgov.be/cgi/article_body.pl?caller=summary&language=fr&numac=2022033354&pub_date=2022-10-19) | wettelijke basis nieuw regime | ✅ |
| Arrêté 10.11.2017 + erratum (`~/projects/fpp-ideas/29_1.pdf`) | historische grid: GQ1–7, medianen ±10%, attributen, PEB | ✅ geëxtraheerd |
| [Monitoring des Quartiers-wijken](https://opendata.brussels.be/explore/dataset/quartiers-du-monitoring-des-quartiers-ibsa-perspective-rbc/) | buurtgeometrie (GeoJSON/SHP/WFS) | ✅ |
| [Statbel NIS9 vastgoedverkopen](https://statbel.fgov.be/en/open-data/real-estate-sales-according-nature-property-deed-sale-statistical-sectors-nis9) | prijspercentielen Q10–Q90 per statistische sector (≥16 transacties) | ✅ |
| [VUB IMMOWEB-dataset](https://researchportal.vub.be/en/datasets/immoweb/) | listings vanaf jan. 2015 (EPC, bouwjaar, prijs) | ⚠️ aan te vragen |
| Statbel *microdata for research* | transactie-microdata | ⚠️ via EHB-begeleider, looptijd = risico |
| Fednot-barometer | prijzen per postcode | ⚠️ te halen |
| Eigen listing-archief | naperiode R1 + dirty-data-case DAS | 🟡 start dag 1 |

## 7. Governance — ontwerpeis nr. 1

- **Geen werkdata zonder expliciete, formele toestemming.** Anonimiseren lost doelbinding niet op.
- Routes: A) Statbel microdata via hogeschool · B) Fednot legal/analytical · C) intern AVM uitsluitend met autorisatie, anders vervalt Q3 naar aggregaat.
- Publieke outputs uitsluitend op buurt-/profielniveau; geen pandidentificatie.
- Alles reproduceerbaar: open repo, gedocumenteerde interpretatiekeuzes (juridische precisie = voordeel, geen bijzaak).

## 8. Risico-register (top 5)

| # | Risico | Mitigatie |
| - | ------ | --------- |
| 1 | Vóór-mei-2025-data ontbreekt voor Q5 | VUB-route; anders cross-sectionele bindingsanalyse |
| 2 | Scraping/ToS | eigen archief vanaf dag 1 + bestaande datasets; vraagprijs≠transactie is zélf een bevinding |
| 3 | Microdata-looptijd | NIS9-fallback is al analysis-grade |
| 4 | Formule-interpretatie (wettelijke ambiguïteit) | simulatorvalidatie + expliciete keuzelog |
| 5 | Scope creep | plug-in architectuur; WON'T-lijst; huren eerst |

## 9. Beslissingslog

- **2026-09-17** — Richting gelockt na 5 brainstormrondes (idee-funnel in [[FPP_planning]]); Trees & Surfaces-platform → BAP-backlog.
- **2026-09-17** — Q5 toegevoegd: soft-cap event study (behandeldifferentiatie = afstand tot de vork).
- **2026-09-17** — Open ruggengraat 100% geverifieerd (bronnenregister §6); productnota aangemaakt als operationeel document.
- Open — coach-goedkeuring pitch; docentenakkoord werkstuk-synergie (DAM/MAL/DAS).

## 10. Glossary

- **Referentiehuur / loyer de référence** — wettelijk berekende vergelijkingshuur; >20% erboven = vermoedelijk misbruik (sinds 1 mei 2025).
- **Indice synthétique de difficulté** — buurtindex (−2 tot +4), formule-input, downloadbaar per statistische sector.
- **Statistische sector (NIS9)** — kleinste Belgische statistiekeenheid; koppelpunt tussen adressen, index en Statbel-prijzen.
- **Vork** — ±-band rond de referentie; juridisch relevant op +20%.
- **Facadisme** — buiten scope (BAP-backlog: *De Drie Leeftijden van een Brussels pand*).

## 11. Volgende acties

1. ~~Formule implementeren + valideren~~ ✅ **gedaan (2026-09-17)**: 63 tests groen; officiële calculator-API gevonden en gecsondeerd (31 probes in `data/validation/api_probes.jsonl`), bedienend raster tot op de euro gereconstrueerd; indexatie k=1,21244 ingevuld en fingerprint bevestigd
2. ~~Adres-validatieflow van de wizard namaken~~ ✅ **gedaan (2026-09-17)**: IRISnet-geocoding + officiële 724-sector-GeoJSON werken lokaal als `four_prices.lookup`; geometrie → INSSEC → index is testbaar. **Datagap gevonden:** de geometrie heeft 724 sectoren, de beschikbare officiële index-xlsx 650; ontbrekende indexen worden expliciet `None`, nooit geïmputeerd.
3. ~~Statbel NIS9-fallback laden~~ ✅ **gedaan (2026-09-17)**: `TF_IMMO_SECTOR.zip` lokaal geladen; 499.838 aggregaten, 2013–2024, sector × jaar × type, met expliciete `None` voor onderdrukte percentielen (<16 geldige prijzen). Filterlaag klaar voor R4.
4. **Day-2 follow-up:** één browser-sessie-spotcheck, actuele base légale/arrêté controleren en de 724↔650-indexgap aan SLRB voorleggen
5. ~~Eigen listing-archivering opzetten~~ ✅ **gedaan (2026-09-17)**: append-only JSONL met typed roundtrip, sector/index-koppeling en `rent_gap` (R1 × R2); géén scraper zolang bron/ToS niet beslist is.
6. ~~Coach Weemaels: pitch + Statbel-aanvraag via EHB~~ **pitch-draft geactualiseerd (2026-09-17)**: `FPP_planning.md` §"Pitch draft" bevat nu de correcte wetsbasis (2022-vergelijkingen, jan-2026-indexatie) én de frontrun-bevindingen met de per-type divergentietabel (+9,9% … +18,2%) — klaar om te pitchen; de mails (SLRB/VUB/Statbel) staan klaar in `docs/email_drafts.md`
7. VUB e-mailen i.v.m. IMMOWEB-dataset 2015+
8. Docentengesprekken: Hambrouck (DAM) → MAL → DAS (eigen case?)

### Beslissingslog (aanvulling 2026-09-17, day-1 frontrun)

- **Bevinding**: de bedienende calculator wijkt **structureel** af van de gepubliceerde vergelijkingen — geen enkele schaalfactor verklaart de prijzen (impliciete factoren 1.28–1.44 per type/oppervlak); zes gepubliceerde bijkomende variabelen (dubbel glas, 2e badkamer, cv, thermoregulering, recreatieruimte, berging) hebben **geen effect** in de API; antwoordband = [70%, 120%].
- **Day-2: draadformaat gekraakt** — de wizard stuurt de sectorcode in dubbele accolades (`{{21016A922}}`); met dat formaat resolut de API de **exacte moeilijkheidsindex** (komt tot op 8 decimalen overeen met het officiële xlsx) en bewegen de prijzen mee: indexcoëfficiënt ≈ **−0,78 €/m²** (gepubliceerd: −0,6456). Bijkomende anomalie: ongevalideerde adressen gaven soms andere prijzen dan gevalideerde (huis 4+: 1881 vs 2080 — verschil exact de PEB-A-correctie).
- **Framing**: dit ís het project in het klein — *de wet zoals gepubliceerd vs de wet zoals berekend* is een vijfde divergentiepaar naast de vier prijzen.
- **Day-2 vingerafdruk (2026-09-17, afrondend)**: het bedienende raster volledig gereconstrueerd (`operating_grid.py`) — per-type kern (α/β, zie README-tabel), bouwjaar-increment +0,962 €/m² (tweekstandenmodel), indexcoëfficiënt −0,7821, PEB/garage-tabellen. Validatie: **bedienend raster = officiële calculator tot op de euro** (residu 0,0 op alle profielen), terwijl de gepubliceerde wet met 28–44% afwijkt. Vingerafdruk ×1,2103 op PEB/garage/index (indexatie jan 2026) maar níet op de typekern → vermoeden van een hergeschatte, ongepubliceerde kern. Dit is nu een runbaar artefact: vijf regimes in code.
- **Indexatiefactor ingevuld en kwantitatief bevestigd (2026-09-17)**: k = 136,69/112,74 = **1,21244** (gezondheidsindex dec 2025/aug 2021, basis 2013=100). `INDEXATION_FACTOR` actief; de vingerafdruk-test (`TestPrescribedIndexation`) bewijst dat de bijkomende-variabelenblok van de calculator exact gepubliceerd × k volgt (PEB tot op de euro, garage en indexcoëfficiënt binnen meetruis), terwijl de typekern en het jaarincrement (0,962 ≠ 1,0429×k) dat níet doen. **Het residuele verschil gepubliceerd×k vs. bedienend = +13 à +15%** — puur de hergeschatte kern. De SLRB-vraag in `docs/email_drafts.md` is nu met cijfers ondubbelzinnig.
- **Cross-regime laag (2026-09-17)**: listing-archief × wettelijke referentie × expliciet gekozen Statbel NIS9-aggregaat is runbaar (`analysis/compare.py`). Verkoopmediaan blijft context; er wordt geen maandhuur/verkoopprijs-ratio verzonnen (verschillende eenheden; Statbel-type wordt niet uit slaapkamers afgeleid).
- **Coverage-audit (2026-09-17)**: de drie officiële bronnen zijn niet dezelfde vintage: 724 geometriesectoren, 650 indexrijen, 643 geometry/index-matches, 81 geometriesectoren zonder indexrij; 663 geometriesectoren komen voor in Statbel (499.838 aggregaten, 2013–2024). `analysis/coverage.py` reproduceert deze tellingen.
- **Shared data contract (2026-09-17)**: `projects/four-prices/docs/data_dictionary.md` + `listing_record.schema.json` leggen de DAM-entiteiten, DAS-null/suppressieregels, MAL-features en FPP-provenance vast zonder scraperafhankelijkheid.
- **Archive quality-audit (2026-09-17)**: `python -m four_prices.analysis.archive_quality <archief>` scant een JSONL-archief niet-destructief: ongeldige regels, duplicaat-snapshots en records zonder sectorjoin worden geteld met regelnummers — de DAS dirty-data-instrument.
- **Kaart-APA v0 (2026-09-17)**: `make map` genereert een zelfstandige SVG-choropleth én joinbare CSV van de bedienende referentiehuur per statistische sector voor een standaardappartement (75 m², bouwjaar 1995). 643 sectoren berekend, 81 zonder indexrij expliciet grijs; tooltips/CSV tonen index, referentie, band, gepubliceerd × k en de procentuele divergentie. Dit is de lawful half van de misbruikkaart; listings worden later als tweede laag toegevoegd.
- **Explorer v0 (2026-09-18)**: `make explorer` genereert een standalone HTML-demo zonder CDN of netwerkcalls. Een buitenstaander kan type, oppervlakte, bouwjaar, PEB en weergave (gepubliceerd × k / bedienend / 120%-drempel) wisselen en per sector de drie waarden inspecteren. Dit is het week-6/8-demo-criterium in miniatuur, zonder de listingcollector te vervroegen.
- **R4 suppression-profiel (2026-09-18)**: `make transactions-profile` toont dat Statbel in 2024 apartmenten (B015) medianen publiceert voor 38,3% van de Brussels geometry-rijen, maar B001 slechts 0,8%, B002 0% en B00A 1,0%. R4 kan dus robuust als apartment-contextlaag; huispercentielen zijn niet voldoende beschikbaar voor een brede kaart zonder extra microdata. De explorer toont per aangeklikte sector nu ook die laatste B015-observatie, inclusief onderdrukking.
- **Open**: (1) één browser-sessie-spotcheck, (2) actueel arrêté via base légale (JS-gerenderd; Moniteur-check), (3) de vraag aan de SLRB.

---

Links: [[FPP_planning]] · [[DAM_planning]] · [[DAS_planning]] · [[MAL_planning]] · [[S1_preparation]] · [[FIN_planning]]
