# Crosswalk matrix

Abbott: *"By developing this matrix of questions across sources, you have broken the large research project up into smaller, more feasible pieces — the minianalyses."* The crosswalk turns "I'm doing research on X" into "I have N questions and M sources; here are the NM possible cells; here's which ones I've populated and which are gaps."

## Shape

Rows = research questions (from `research-design-document`).
Columns = sources / source-types.
Cells = either a minianalysis ID, "not relevant", "gap", or "in progress".

```
                    | Source A | Source B | Source C | Source D |
RQ 1 (deposit rate) | MA-001   | MA-002   | gap      | NR       |
RQ 2 (UG L&T § 26)  | MA-003   | gap      | MA-004   | NR       |
RQ 3 (case volume)  | gap      | NR       | MA-005   | MA-006   |
```

## What the cells encode

| Cell | Meaning |
|---|---|
| `MA-NNN` | Populated — minianalysis written |
| `gap` | Source should answer this; we haven't reached it |
| `NR` | Not relevant — this source doesn't speak to this question |
| `WIP` | In progress |
| `orphan` | Was populated; rhetorical structure changed; abandoned |

## Decision rules

- **Live document, not snapshot.** Updated whenever a minianalysis lands or a source is added.
- **Gaps drive next-wave dispatch.** The crosswalk *is* the work queue.
- **NR is a real cell value.** "Not relevant" is information; don't leave it blank.
- **Visualise as a table** — ASCII for markdown, real table for Word output.
- **Ratio of populated to total cells** is a project-progress metric; track it.
- **Orphaned cells are not failures.** When the report's rhetorical structure changes (per `research-report-builder`), some completed work no longer fits. Mark orphan; don't force it.
- **Crosswalk pairs with chronology** for time-bounded projects (see `chronology-construction`).

## File location

`projects/<project-id>/CROSSWALK.md`

Format suggestion:

```markdown
# Crosswalk — <project>

Last updated: YYYY-MM-DD

## Matrix
| RQ | Source A | Source B | ... |
|---|---|---|---|
| 1: <question> | MA-001 | gap | ... |
| 2: <question> | MA-003 | NR | ... |

## Legend
- MA-NNN: link to minianalysis
- gap: open work
- NR: not relevant
- WIP: in progress
- orphan: completed but no longer fits report

## Progress
Populated: 12 / 28 = 43%
Gaps remaining: 11
WIP: 3
NR (closed): 2
Orphaned: 0

## Open gaps prioritised
1. RQ 3 × Source A — high value, easy
2. ...
```

## Workflow

1. After research-design-document is stable, populate the empty matrix (rows from RQs, columns from candidate sources).
2. Mark obvious NR cells immediately — saves work.
3. Each minianalysis adds an `MA-NNN` to its cell.
4. Sub-agent dispatch picks an open gap and works it.
5. Synthesis (`cross-cohort-synthesis`) reads the crosswalk to find patterns across rows or columns.

## Anti-patterns

- Empty crosswalk that never gets populated — treat its absence as project-management failure
- Crosswalk without source-side discipline (vague column labels) — collapses to noise
- Filling cells without writing the underlying minianalysis — false completion
- Treating orphans as wasted work — they're evidence the project evolved
- Hidden crosswalk — keep it visible; sub-agents need to see what's already covered

## See also

- `research-design-document` — supplies rows
- `minianalysis-engine` — populates cells
- `gap-analysis` — works the open-gap queue
- `cross-cohort-synthesis` — reads the matrix for patterns
- `chronology-construction` — companion for time-bounded projects
