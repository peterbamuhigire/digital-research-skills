# Discipline router

Different disciplines have different research grammars. Searching humanities like sciences misses everything. This skill picks the strategy template before any sub-agent fires.

## The six discipline templates

### Sciences (physics, chemistry, biology, engineering)
- **Title words are content-rich** — keyword search alone often works
- **Citations matter intensely** — publish-or-perish, tenure
- **Brachiation is high-yield** — citation graph is dense and fast-moving
- **Currency matters** — 5-year-old work is often superseded
- **Subject headings less essential** than in medicine
- **Top sources:** Web of Science, Scopus, ScienceDirect, arXiv (preprints), discipline-specific (IEEE Xplore for engineering)
- **Default operator stack:** title + keyword; date-bounded last 5 years

### Medicine (clinical, biomedical)
- **MeSH (controlled vocabulary) is dominant** — auto-explode, major-topic flag, subheadings
- **Indexers always pick most-specific term** — search the broad term won't catch articles indexed only at the narrow term unless explode is on
- **Vancouver citation style** typical
- **Currency very important** for clinical practice; less for foundational physiology
- **Top sources:** PubMed (free), MEDLINE (Ovid / EBSCO / others), Cochrane Library (systematic reviews), ClinicalTrials.gov
- **Default operator stack:** MeSH heading + AND + clinical filter

### Social sciences (sociology, education, psychology, economics, political science)
- **Strong thesauri** — ERIC thesaurus, PsycINFO thesaurus
- **Hierarchical broader/narrower/related terms** — use the thesaurus to map concept space
- **Grey literature matters** — reports, working papers, dissertations
- **Citation chasing yields more than in pure sciences**
- **Top sources:** ERIC (free), PsycINFO, JSTOR, SSRN (preprints), Google Scholar
- **Default operator stack:** thesaurus term + AND + age-group / methodology filter

### Humanities (history, philosophy, literature, religious studies, art)
- **Indexers only assign a term if explicitly mentioned** — over-specifying produces zero hits
- **Cited-reference searching now valuable** even though the field used to resist it
- **Subject Language vs Language of Publication** are distinct fields
- **Older book-length sources matter** — long after currency-decay in sciences
- **Top sources:** MLA International Bibliography, Project MUSE, JSTOR, America: History and Life, ATLA Religion Database
- **Default operator stack:** keyword + author + period; broad keyword often beats over-specified field

### Numerical / statistical
- **Publication date and content-coverage date are different fields** — Statistical Insight covers data 1700–2090 even though publications run 1973+
- **Don't date-filter early** — find any source first, see what data range it carries
- **Use Basic search** — Advanced search is often *worse* for statistics
- **Top sources:** ProQuest Statistical Insight, Census, BLS, World Bank, IMF, OECD, Statista, KNBS for Kenya, UBOS for Uganda
- **Default operator stack:** topic + geographic + don't-filter-by-date initially

### Law
- **Statute / case-law / regulation are distinct corpora** with different search semantics
- **Citation format itself encodes jurisdiction** (e.g., `[2025] KEBPRT 425`)
- **Currency varies** — old cases still binding; old statutes often repealed
- **Top sources:** Kenyalaw.org (KE), ULII (UG), TanzLII (TZ), RwandaLII (RW), CommonLII for shared content; Westlaw / LexisNexis for paid
- **Default operator stack:** citation lookup OR jurisdiction-bounded keyword + parties

## Decision rules

- **Pick the discipline first.** Don't issue queries before this routing decision.
- **Use the discipline's own controlled vocabulary** when one exists. Free, more powerful than keyword.
- **Combine sources within discipline** — index overlap is partial.
- **Don't import strategies across disciplines** — humanities indexing rules will fail in medicine and vice versa.
- **Multi-discipline projects** need multi-discipline routers, one strategy per cohort.

## Anti-patterns

- One-strategy-fits-all queries
- Date-filtering humanities early (loses book-length sources)
- Keyword-only searches in medicine (misses MeSH precision)
- Treating Google Scholar as comprehensive (Bell: "complete black box in terms of content")
- Skipping the discipline thesaurus and hand-rolling synonym lists

## East African discipline-specific anchors

- **Sciences in EA:** WoS, Scopus, AJOL (African Journals Online)
- **Medicine in EA:** PubMed, AfricanIndexMedicus (AIM)
- **Social sciences:** ERIC, IDS Sussex, AERC, Africa Portal, JSTOR's Africa collection
- **Humanities:** MLA, JSTOR, university repositories (Makerere Dissertations, UoN e-Repository, UDSM)
- **Numerical:** KNBS, UBOS, NBS-Tanzania, NISR-Rwanda, World Bank Open Data
- **Law:** Kenyalaw, ULII, TanzLII, RwandaLII

## See also

- `pearl-growing-iteration` — how to iterate within the chosen discipline
- `web-search-operator-grammar` — the operator layer
- `academic-source-mining` — discipline-specific repositories
- `regulatory-landscape-mapping` — for the law branch
