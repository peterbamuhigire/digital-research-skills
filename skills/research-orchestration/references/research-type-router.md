# Research-type router

Different research types need different orchestration, source mixes, methodologies, and report shapes. This skill picks the right combination upfront so the engine doesn't run a market-research playbook against an OSINT problem.

## The 19 research routes

### Investigative / analytical (11)

| Type | Purpose | Audience | Canonical skill route | Report schema |
|---|---|---|---|---|
| **Pain-point research** | Identify problems across populations affected by a system | Designers, product, policy | `research-techniques` (`references/pain-point-taxonomy.md`) | A |
| **Single-cohort deep-dive** | Exhaustive study of one population | Specialists, advocacy | `research-techniques` (`references/pain-point-taxonomy.md`) | B |
| **Market / industry landscape** | Size markets, map operators, find entry points | Investors, founders, strategists | `quantitative-modelling` + `research-design` | C |
| **Comparative / benchmarking** | Compare ≥2 jurisdictions, products, organisations | Decision-makers, analysts | `research-techniques` (`references/cross-cohort-synthesis.md`) | D |
| **Social-media / sentiment research** | What's being said about X | Comms, brand, policy-monitoring | `research-design` (`references/mroc-design-and-management.md`) + `osint-investigation` (`references/social-source-extraction.md` only for public-source collection) | E |
| **Due diligence** | Pre-investment, pre-partnership, pre-hire investigation | Investors, M&A, compliance | `due-diligence` (`references/dd-framework-hetherington.md`) | F |
| **OSINT** | Open-source intelligence on persons / orgs / domains / infrastructure | Security, journalism, investigations | `osint-investigation` (`references/osint-methodology.md`) | G |
| **Product research** | Inform a product hypothesis | Product, founders | `research-design` + `research-techniques` (`references/pain-point-taxonomy.md`) | H |
| **Historical research** | Reconstruct past events from primary + secondary sources | Researchers, journalists, academics | `research-design` (`references/historical-research-methods.md`) | I |
| **Trends research** | Forecasting, signal extraction, time-series | Strategists, analysts, forecasters | `research-design` (`references/trend-analysis.md`) + `calibration-and-forecasting` | J |
| **Policy / regulatory research** | Statute / case-law / enforcement deep-dive | Policy, legal, advocacy | `online-legal-research` | K |

### Long-form scholarly outputs (4 types × 2 variants = 8)

| Type | Variant | Audience | Primary skill | Report schema |
|---|---|---|---|---|
| **Thesis** (Master's / honours) | Academic | Examiners, advisor | `academic-writing` + `academic-reporting-standards` | L |
| **Thesis** | Popular | General / professional readers | `business-writing` + `research-output-formats` | M |
| **Paper / journal article** | Academic | Peer reviewers, journal | `academic-writing` + `academic-reporting-standards` | N |
| **Paper / long-form** | Popular | Magazine, trade publication | `business-writing` + `research-output-formats` | O |
| **PhD dissertation** | Academic | Doctoral committee, field | `academic-writing` + `academic-reporting-standards` | P |
| **Dissertation / book** | Popular | Trade-book audience | `business-writing` + `research-output-formats` | Q |
| **Essay** | Academic | Coursework, scholarly outlet | `academic-writing` + `academic-reporting-standards` | R |
| **Essay** | Popular | Op-ed, magazine, blog | `business-writing` | S |

**Default variant when not specified:**
- Thesis / dissertation → academic (these are nearly always degree submissions)
- Paper → academic (unless target outlet is a magazine / blog)
- Essay → **ask the user.** Could be either.

## How to choose

The router asks four questions in order:

1. **Audience** — Who reads the final report?
   - Internal product / design → pain-point or product research
   - External clients / investors → market, comparative, or due diligence
   - Public / advocacy → policy or single-cohort deep-dive
   - Operational / security → OSINT
   - Strategic / forecasting → trends

2. **Output expectation** — What decisions hang on this?
   - "Should we build X?" → product research (H)
   - "Should we invest in Y?" → due diligence (F) or market landscape (C)
   - "What is happening with Z?" → status / OSINT (G) or sentiment (E)
   - "How does X compare to Y?" → comparative (D)
   - "What's coming next?" → trends (J)
   - "What does the law say?" → policy / regulatory (K)
   - "What hurts the people affected?" → pain-point (A or B)
   - "Submit for examination / peer review" → thesis (L), paper (N), or dissertation (P)
   - "Public-facing book or feature on existing research" → popular thesis (M), popular paper (O), popular dissertation (Q)
   - "Make a single argument" → academic essay (R) or popular essay (S)

3. **Subject shape** — Is the subject a system, an entity, an event, or a topic?
   - System with multiple stakeholders → multi-cohort pain-point (A)
   - Single named entity (person, company, asset) → due diligence (F) or OSINT (G)
   - Past event → historical (I)
   - Ongoing topic with public discourse → social-media (E) or sentiment + landscape

4. **Time horizon** — Past, present, or future?
   - Past → historical (I)
   - Present → most other types
   - Future → trends (J)

The router should produce a **research brief** at the top of the project containing:

```yaml
project: <id>
research_type: <one of the 19 routes>
audience: <named>
output_expectation: <decision the report supports>
subject: <system | entity | event | topic>
time_horizon: past | present | future
report_schema: <A through S>
methodology_skills: [<active skill names>]
methodology_references: [<optional active reference paths>]
out_of_scope: [<list>]
hard_constraints: [<list>]
expected_waves: <number>
```

## Decision rules

- **Pick the type before the first sub-agent fires.** Wrong type → wrong sources → wasted waves.
- **One project, one type.** If a single project needs multiple types, split it into sibling projects.
- **The report schema is downstream of the type.** Don't pick the schema first.
- **Methodology skills are loaded per type** — don't load all 15 skills for every project.
- **Audience drives tone.** Internal-design tone is direct; client-deliverable tone is formal; advocacy tone is evidence-heavy.

## Anti-patterns

- Starting research without picking the type
- Treating "more sources = better" — different types need different *kinds* of sources
- Conflating market landscape with due diligence (different rigour, different audience, different liability)
- Conflating OSINT with social-media research (different ethics, different verification standards)
- Generating a Word doc before deciding the schema

## Example briefs

### Example 1 — `east-africa-property-hostel`

```yaml
project: east-africa-property-hostel
research_type: pain-point research (multi-cohort)
audience: design / product / policy
output_expectation: "Identify two-sided product opportunities in EA rental + hostel markets"
subject: system (multi-stakeholder)
time_horizon: present
report_schema: A
methodology_skills: [research-techniques, online-legal-research]
methodology_references:
  - skills/research-techniques/references/pain-point-taxonomy.md
  - skills/research-techniques/references/cross-cohort-synthesis.md
out_of_scope: [LGBTQ+ topics, hotels, Airbnb-only operators]
hard_constraints: [evidence-discipline, tier-balanced sources, multi-country verification]
expected_waves: 2
```

### Example 2 — hypothetical due-diligence project

```yaml
project: acorn-holdings-dd-2026q2
research_type: due diligence
audience: institutional investor
output_expectation: "Risk assessment + green/amber/red flags before participating in next bond round"
subject: entity (Acorn Holdings + REIT vehicles)
time_horizon: present (with 5y backward)
report_schema: F
methodology_skills: [due-diligence, online-legal-research, source-verification]
methodology_references:
  - skills/due-diligence/references/dd-framework-hetherington.md
out_of_scope: [non-Acorn EA student-housing operators]
hard_constraints: [evidence-discipline, named-source-only, no inferred ownership]
expected_waves: 3
```

### Example 3 — hypothetical Master's thesis

```yaml
project: ea-tenant-deposit-protection-thesis-2026
research_type: thesis (Master's)
variant: academic
discipline: social_sciences (development studies)
audience: thesis examiners, supervisor (Makerere)
output_expectation: "Submit for examination, July 2026"
subject: tenant deposit protection regimes in Uganda + Kenya
time_horizon: present (with 5y backward)
report_schema: L
citation_style: Chicago Author-Date
methodology_skills:
  - academic-writing
  - academic-reporting-standards
  - online-legal-research
  - research-techniques
methodology_references:
  - skills/research-techniques/references/cross-cohort-synthesis.md
ethics_required: false (secondary-source research)
target_word_count: 25000
hard_constraints: [evidence-discipline, primary-source-where-possible]
expected_waves: 3
```

### Example 4 — popular essay derived from existing research

```yaml
project: ea-deposit-theft-essay-2026
research_type: essay
variant: popular
audience: educated general readership (East African or pan-African outlet)
output_expectation: "1,500-word op-ed for The EastAfrican / The Continent"
subject: Uganda deposit non-refund issue
time_horizon: present
report_schema: S
methodology_skills: [business-writing]
draws_from_project: east-africa-property-hostel
target_word_count: 1500
hard_constraints: [evidence-discipline, hyperlink-citations-only, plain-language]
expected_waves: 0 (research already done; this is adaptation)
```

## See also

- `research-orchestration` — runs the chosen approach
- `research-design` — assembles the chosen schema through its report-builder reference
- `evidence-discipline` — applies regardless of type
