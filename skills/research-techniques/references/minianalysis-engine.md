# Minianalysis engine

Abbott: *"a specific research question with a finite set of research acts done in a limited time."* The minianalysis is the smallest *unit of finished work* in a research project. It maps cleanly to one paragraph or one section in the final report.

## Four families of minianalysis

| Family | Output | Examples |
|---|---|---|
| **Timeline / biography / narrative** | Date-ordered chain of events | Timeline of Kenya Building Code 2024 from draft to enforcement; biography of Acorn Holdings 2010–2026 |
| **Categorisation & colligation** | Typology with named categories | Five categories of EA hostel-owner per ownership structure; six classes of tenant-discrimination pattern |
| **Numerical / quantitative** | Statistic, table, chart | KSh -26.8% depreciation impact on construction materials; deposit-non-refund rates by city |
| **Content analysis** | Theme distribution from a corpus | Top complaint themes from 100 Kenya Tribunal cases; sentiment in r/Kenya rental threads |

## Constraints

- **Maximum: one full-time week.** If it exceeds that, decompose further.
- **Single research question per minianalysis.** Not a cluster.
- **Stand-alone output.** Must read as a coherent paragraph or section without surrounding context.
- **Provenance-anchored.** Every claim cites its source. Failure here is treated as `evidence-discipline` violation.

## The establishment minianalysis

The first minianalysis on any project must answer: **"Is this puzzle real, and is it still puzzling?"**

If the establishment minianalysis returns "puzzle has already been solved" or "puzzle was misstated" — the project pivots. **Never proceed to deeper investment without a positive establishment verdict.**

Examples:
- For the EA deposit project: confirm the 80% non-refund stat against primary Daily Monitor source (Aug 2 2023). ✅ Established.
- For an Acorn DD project: confirm Acorn Holdings exists, is Kenyan, has ~20,000 beds. ✅ Established.

## Decision rules

- **Every research question gets a minianalysis.** Questions without one are unverified hopes.
- **Every minianalysis ends with a written paragraph.** Even a short one. Dragging unwritten findings into endphase causes blockage.
- **Just-in-time minianalyses in endphase** — small research acts driven entirely by the emerging text's needs.
- **Orphan-tolerant.** When the report's rhetorical structure changes, some completed minianalyses won't fit. Abandon them. Don't force them in.
- **Crosswalk visible.** Each minianalysis maps to a cell in the crosswalk matrix (research-question × source).

## Workflow

1. Sub-agent receives a research question + reading-mode hint
2. Conducts bounded ≤1-week investigation
3. Writes 1–3 paragraphs answering the question, with sources cited inline
4. Logs the minianalysis as a file: `projects/<project-id>/minianalyses/<id>-<short-title>.md`
5. Adds a row to the crosswalk matrix mapping question × sources used

## File structure

```
projects/<project-id>/minianalyses/
├── 001-establishment-deposit-nonrefund-rate.md
├── 002-uganda-lt-act-2022-section-26.md
├── 003-kenya-tribunal-case-volume-2024.md
└── ...
```

Each minianalysis file:
```markdown
# <id>: <title>
**Question:** <single research question>
**Type:** timeline | categorisation | numerical | content
**Status:** establishment | midphase | endphase | orphaned
**Sources:** [list]
**Findings:**
<1–3 paragraphs of finished prose>
**Crosswalk row:** <id> in matrix
```

## Anti-patterns

- Minianalyses without a written paragraph (just a "data dump")
- Minianalyses that exceed one week — they're really projects
- Skipping the establishment step — researches an illusory puzzle
- Treating completed minianalyses as immutable — they should orphan when the rhetorical structure shifts
- Dumping all minianalyses into the report verbatim — they need integration

## See also

- `research-design-document` — supplies the questions
- `crosswalk-matrix` — the matrix that minianalyses populate
- `reading-mode-router` — picks how to read sources within a minianalysis
- `provenance-anchored-notes` (roadmap) — note discipline beneath minianalyses
- `research-report-builder` — minianalyses are the building blocks of the final report
