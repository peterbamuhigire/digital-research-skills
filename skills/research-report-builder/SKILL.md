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

The project type determines the chapter sequence. Pick the best match.

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

- `professional-word-output` — the rendering engine
- `python-document-generation` — alternative pure-Python pipeline
- `markdown-lint-cleanup` — pre-render cleanup
- `pain-point-taxonomy` — supplies tables
- `cross-cohort-synthesis` — supplies the synthesis chapter
- `source-verification` — supplies the tiered bibliography
