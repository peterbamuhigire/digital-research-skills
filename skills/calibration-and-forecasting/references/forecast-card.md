# Forecast Card

Use this card for any forecast that must be tracked, updated, or scored.

## Template

| Field | Requirement |
|---|---|
| Forecast ID | Stable identifier, e.g. `F-2026-001` |
| Question | Resolvable event question, not a theme |
| Event definition | Observable threshold that settles the forecast |
| Scope | Entity, geography, population, market, or cohort |
| Horizon | Exact date or event deadline |
| Resolution source | Source or evidence class that will settle the outcome |
| Base rate | Reference class and source |
| Current probability | Numeric probability or band |
| Verbal term | Kent/ODNI-compatible term if used |
| Source confidence | Separate from event probability |
| Rationale | Evidence, mechanism, and constraints |
| Alternatives | Rival pathways or outcomes |
| Update triggers | Evidence that raises, lowers, or retires the forecast |
| Owner | Analyst or wave responsible |
| Status | open, updated, resolved, retired |

## Update Record

| Date | Prior | New | Trigger evidence | Direction | Note |
|---|---:|---:|---|---|---|
| YYYY-MM-DD | 0.40 | 0.55 | Source IDs | up | Short explanation |

## Resolution Record

| Field | Requirement |
|---|---|
| Outcome | happened, did not happen, partial, unresolvable |
| Resolution date | Date settled |
| Resolution source | Source ID and locator |
| Score | Use the project's chosen scoring rule |
| Lesson | What changed in future forecasting practice |
