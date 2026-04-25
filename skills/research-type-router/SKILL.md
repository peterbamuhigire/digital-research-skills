---
name: research-type-router
description: Use FIRST when starting any new research project — maps user intent to a research type, selects the orchestration approach, the methodology skills to load, and the report schema. Upstream of research-orchestration.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
  priority: high
---

# Research-type router

Different research types need different orchestration, source mixes, methodologies, and report shapes. This skill picks the right combination upfront so the engine doesn't run a market-research playbook against an OSINT problem.

## The 11 research types

| Type | Purpose | Audience | Primary skill | Report schema |
|---|---|---|---|---|
| **Pain-point research** | Identify problems across populations affected by a system | Designers, product, policy | `pain-point-taxonomy` | A |
| **Single-cohort deep-dive** | Exhaustive study of one population | Specialists, advocacy | `pain-point-taxonomy` | B |
| **Market / industry landscape** | Size markets, map operators, find entry points | Investors, founders, strategists | `academic-source-mining` + industry data | C |
| **Comparative / benchmarking** | Compare ≥2 jurisdictions, products, organisations | Decision-makers, analysts | `cross-cohort-synthesis` | D |
| **Social-media / sentiment research** | What's being said about X | Comms, brand, policy-monitoring | `social-source-extraction` | E |
| **Due diligence** | Pre-investment, pre-partnership, pre-hire investigation | Investors, M&A, compliance | `due-diligence-framework` | F |
| **OSINT** | Open-source intelligence on persons / orgs / domains / infrastructure | Security, journalism, investigations | `osint-methodology` | G |
| **Product research** | Inform a product hypothesis | Product, founders | `pain-point-taxonomy` + market | H |
| **Historical research** | Reconstruct past events from primary + secondary sources | Researchers, journalists, academics | `historical-research-methods` | I |
| **Trends research** | Forecasting, signal extraction, time-series | Strategists, analysts, forecasters | `trend-analysis` | J |
| **Policy / regulatory research** | Statute / case-law / enforcement deep-dive | Policy, legal, advocacy | `regulatory-landscape-mapping` | K |

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
research_type: <one of the 11>
audience: <named>
output_expectation: <decision the report supports>
subject: <system | entity | event | topic>
time_horizon: past | present | future
report_schema: <A through K>
methodology_skills: [<list>]
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
methodology_skills: [pain-point-taxonomy, regulatory-landscape-mapping, cross-cohort-synthesis]
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
methodology_skills: [due-diligence-framework, regulatory-landscape-mapping, source-verification]
out_of_scope: [non-Acorn EA student-housing operators]
hard_constraints: [evidence-discipline, named-source-only, no inferred ownership]
expected_waves: 3
```

## See also

- `research-orchestration` — runs the chosen approach
- `research-report-builder` — emits the chosen schema
- `evidence-discipline` — applies regardless of type
