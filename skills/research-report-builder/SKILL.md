---
name: research-report-builder
description: Use when assembling the final structured Word document from a completed research project — pulls from research/, analysis/, and opportunities/ files, applies a topic-appropriate report schema, and emits a designed .docx via the professional-word-output skill.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Research report builder

The end product of every project in `digital-research-engine` is a Word document. This skill defines:

1. The schema (chapter structure) per report-type
2. The pipeline from markdown source → Word output
3. The visual / layout standards

## Report-type schemas

The project type determines the chapter sequence. Pick the best match. The engine supports research across many disciplines — schema choice is the most important upstream decision.

| Schema | Research type | Use when |
|---|---|---|
| A | Pain-point research (multi-cohort) | Investigating problems across populations affected by a system |
| B | Single-cohort deep-dive | One population studied exhaustively |
| C | Market / industry landscape | Sizing a market, mapping operators, finding entry points |
| D | Comparative / benchmarking | Comparing ≥2 jurisdictions, products, organisations, or operators |
| E | Social-media / sentiment research | What is being said about X on Reddit, X, TikTok, Facebook, news comments |
| F | Due diligence | Pre-investment, pre-partnership, pre-hire investigation of an entity |
| G | OSINT (open-source intelligence) | Person / org / domain / infrastructure profiling from public sources |
| H | Product research | Competitive intel + user pain + opportunity sizing for a single product hypothesis |
| I | Historical research | Reconstruction of past events from primary + secondary sources |
| J | Trends research | Forecasting, signal extraction, time-series patterns |
| K | Policy / regulatory research | Statute / case-law / enforcement deep-dive across jurisdictions |

### Schema A — Pain-point research (multi-cohort)
Used when researching pain points across one or more cohorts (e.g., East Africa Property/Hostel).

```
1. Executive Summary
2. Methodology & Sources
3. Per-cohort findings:
   3.1 <Cohort A> — pain-points report
   3.2 <Cohort A> — themes taxonomy
   3.3 <Cohort A> — country breakdown
   3.4 <Cohort A> — vulnerable groups (if applicable)
   3.5 <Cohort A> — opportunities
   (repeat for each cohort)
4. Cross-cohort synthesis
5. Two-sided product opportunities
6. Regulatory landscape (if applicable)
7. Academic & industry references
8. Quotes appendix
9. Source bibliography (tiered)
10. Glossary
```

### Schema B — Single-cohort deep-dive
Used when one population is studied in depth.

```
1. Executive Summary
2. Methodology
3. Pain-points report
4. Themes taxonomy
5. Geographic / segment breakdown
6. Vulnerable sub-groups
7. Regulatory landscape
8. Opportunities
9. Quotes appendix
10. References
```

### Schema C — Market-landscape research
Used for industry / asset-class studies.

```
1. Executive Summary
2. Market size & structure
3. Key players & operators
4. Demand drivers
5. Supply constraints
6. Regulatory & tax landscape
7. Financing & capital landscape
8. Competitive dynamics
9. Opportunities & risks
10. References
```

### Schema D — Comparative / benchmarking
Used when comparing >2 jurisdictions or operators.

```
1. Executive Summary
2. Comparison framework
3. Per-entity profiles
4. Cross-entity comparison tables
5. Pattern analysis
6. Recommendations
7. References
```

### Schema E — Social-media / sentiment research
Used when surfacing what's being said about a topic on social platforms.

```
1. Executive Summary
2. Methodology (platforms, queries, time-window, sample size)
3. Volume & reach metrics
4. Theme extraction
5. Sentiment analysis (positive / negative / neutral)
6. Key voices & influencers
7. Notable threads / viral moments
8. Cross-platform comparison
9. Quote appendix (with platform context)
10. Limitations (platform bias, ToS constraints)
11. References
```

### Schema F — Due diligence
Used pre-investment, pre-partnership, or pre-hire to investigate an entity (person, company, asset).

```
1. Executive Summary (red / amber / green flags)
2. Subject identification & corroboration
3. Legal & regulatory status (registration, licences, court records)
4. Financial position (filings, audits, credit history)
5. Reputational footprint (news, social, sanction lists)
6. Beneficial-ownership trace
7. Counterparty / network mapping
8. Adverse-media findings
9. Source-of-funds / source-of-wealth (for AML contexts)
10. Risk assessment
11. Remaining gaps & verification limits
12. References (with confidence levels)
```

### Schema G — OSINT (open-source intelligence)
Used for person / org / domain / infrastructure profiling from publicly available sources.

```
1. Executive Summary
2. Subject scope & target list
3. Identification & disambiguation
4. Online footprint (domains, accounts, repositories)
5. Geolocation / temporal pattern (where applicable)
6. Network mapping (associates, organisations)
7. Technical infrastructure (hosting, certificates, DNS)
8. Cross-reference & corroboration
9. Confidence ratings per finding
10. Operational security caveats
11. References
```

### Schema H — Product research
Used to inform a product hypothesis with competitive + user + opportunity data.

```
1. Executive Summary
2. Hypothesis & thesis
3. Target user / customer profile
4. Pain-point evidence (qualitative + quantitative)
5. Competitive landscape
6. Pricing & willingness-to-pay
7. Market sizing (TAM / SAM / SOM)
8. Distribution channels
9. Risks & failure modes
10. Recommended next experiments
11. References
```

### Schema I — Historical research
Used to reconstruct past events from primary and secondary sources.

```
1. Executive Summary
2. Period & scope
3. Primary-source inventory
4. Secondary-source synthesis
5. Chronology / timeline
6. Key actors & their roles
7. Causal analysis
8. Historiographical debates
9. Implications for the present
10. Source appraisal (provenance, bias, gaps)
11. References (Chicago / footnoted)
```

### Schema J — Trends research
Used for forecasting, signal extraction, and time-series pattern identification.

```
1. Executive Summary
2. Domain & time-horizon
3. Methodology (signal sources, weighting)
4. Quantitative trends (with charts)
5. Qualitative signals
6. Convergent / divergent factors
7. Scenario analysis (best / base / worst)
8. Leading indicators to watch
9. Confidence intervals & assumptions
10. Implications for stakeholders
11. References
```

### Schema K — Policy / regulatory research
Used for deep statute / case-law / enforcement work across jurisdictions.

```
1. Executive Summary
2. Domain & jurisdictions covered
3. Per-jurisdiction five-layer mapping (constitutional → enforcement)
4. Cross-jurisdictional comparison
5. Recent precedent & enforcement actions
6. Gaps between law and enforcement
7. Pending bills / reform momentum
8. Stakeholder positions (industry, NGO, government)
9. Recommendations
10. References (case citations + statutes)
```

## Pipeline

1. **Read** all `<cohort>/research/*.md`, `<cohort>/analysis/*.md`, `<cohort>/opportunities/*.md` for the project
2. **Validate** with `gap-analysis` — flag any missing chapters per the chosen schema
3. **Run** `cross-cohort-synthesis` if >1 cohort
4. **Assemble** a single master markdown matching the schema
5. **Lint** with `markdown-lint-cleanup`
6. **Generate** the `.docx` via the `professional-word-output` skill (or `python-document-generation` for pure-Python flows)
7. **Place** the output at `projects/<project-id>/report.docx` with `report-DRAFT-YYYY-MM-DD.docx` versions kept for audit

## Visual / layout standards

- Cover page with title, date, version, author
- Auto-generated TOC
- Chapter numbering
- Tables of pain-point taxonomies use the prevalence × severity columns from `pain-point-taxonomy`
- Quotes rendered as block-quotes with attribution lines
- Tier-bibliography at the end (academic / regulatory / news / industry / social — matches `source-verification` ladder)
- Pull-quotes formatted distinctly from running text
- Brand colours and typography per `professional-word-output` defaults unless overridden

## Decision rules

- **Pick the schema before assembling.** Switching mid-build wastes time.
- **Don't include placeholder text** in a delivered Word doc. Mark "data gap" sections explicitly using a callout.
- **Keep markdown source** — the `.docx` is generated, not authored. Edits go to markdown.
- **Version every export.** `report-v1.docx`, `report-v2-2026-04-25.docx`. Last-export-wins is destructive.

## Anti-patterns

- Editing the .docx directly — markdown source then drifts
- Cramming all cohort detail into the executive summary
- Omitting the source bibliography
- Using inconsistent taxonomy formatting across chapters
- Generating the doc before `gap-analysis` and `cross-cohort-synthesis` have run

## See also

- `research-type-router` — maps user intent to schema (use upstream of this skill)
- `professional-word-output` — the rendering engine
- `python-document-generation` — alternative pure-Python pipeline
- `markdown-lint-cleanup` — pre-render cleanup
- `pain-point-taxonomy` — supplies tables for Schema A / B
- `cross-cohort-synthesis` — supplies the synthesis chapter for Schema A
- `source-verification` — supplies the tiered bibliography for all schemas
- `due-diligence-framework` — methodology for Schema F
- `osint-methodology` — methodology for Schema G
- `trend-analysis` — methodology for Schema J
- `regulatory-landscape-mapping` — methodology for Schema K
