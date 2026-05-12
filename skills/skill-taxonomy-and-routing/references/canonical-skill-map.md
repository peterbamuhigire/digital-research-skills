# Canonical Skill Map

## Decision Rules

| Question | If yes | If no |
|---|---|---|
| Is this a repeatable workflow with its own inputs and outputs? | Top-level skill | Reference file |
| Does it need independent triggering? | Top-level skill | Reference file |
| Is it only a checklist inside another workflow? | Reference file | Consider skill |
| Is it named by routers as an execution step? | Top-level skill or router fix | Leave local |

## Alias Register Pattern

| Alias | Canonical target | Action |
|---|---|---|
| source verification | `source-verification` | Keep as top-level verifier |
| gap analysis | `research-techniques` reference | Do not create unless workflow grows |
| cross-cohort synthesis | `research-techniques` reference | Keep orchestrator-owned |
