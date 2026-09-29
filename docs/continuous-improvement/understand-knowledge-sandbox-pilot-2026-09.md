# Understand Anything `/understand-knowledge` sandbox pilot — decision record

| Field | Value |
|---|---|
| Record ID | UA-14 (my-10-kaizen phase M10-13, task T04) |
| Date | 29 September 2026 |
| Tool | Understand Anything (MIT, https://github.com/Egonex-AI/Understand-Anything), inspected at commit `b05cc3b20990afca537b4fc0a49b4d7fbdc65bb0` |
| Proposed subject | A copy of `projects/example-market-landscape/` (synthetic; 35 files, 7,010 bytes; `_registry/claims.yaml` 1 claim, `_registry/synthesis-map.yaml` 1 row), outside `C:\wamp64\www` |
| Status | **NOT_ASSESSED — not run** |
| Verdict | **No adoption.** The line of enquiry stays closed until a re-entry condition below is met. |
| Decided by | Orchestrator under Peter Bamuhigire's delegated authority, 29 Sep 2026 |

## Why the pilot was not run

The pilot's only purpose is to measure what `/understand-knowledge` adds to this engine's own registers. Every measure it needs (graph nodes, edges, implicit-claim edges) is produced by model calls inside the plugin's agents, and the phase's first measure is the token cost of those calls. Peter's standing zero-spend rule for this Kaizen (29 Sep 2026: no paid API calls or model-executed runs) therefore rules the run out: the pilot cannot be carried out without spending. Install alone would measure nothing, so the plugin was not installed either.

The phase file's own value gate names this as the credible, cheap option: skip the run, record `NOT_ASSESSED`, and the engine loses nothing.

## Measures

| Measure | Result |
|---|---|
| Installed version or commit | NOT_ASSESSED — not installed (zero-spend rule) |
| Tokens used by one `/understand-knowledge` run | NOT_ASSESSED — not run (zero-spend rule) |
| Run time | NOT_ASSESSED — not run |
| Graph node count | NOT_ASSESSED — not run |
| Graph edge count | NOT_ASSESSED — not run |
| Implicit-claim edges not already in `_registry/claims.yaml` or `synthesis-map.yaml` | NOT_ASSESSED — not run |
| Reviewer judgement of edge usefulness | NOT_ASSESSED — nothing to judge |

## Safety evidence (before and after)

No sandbox was created, no plugin was installed and no hook was enabled. SHA-256 values taken at the start and end of the M10-13 session:

| Item | Before | After |
|---|---|---|
| `~/.claude/settings.json` | `110aee8a69f4422ef742fd357bdf74e1aa1b5f46c26457a22d336941aa90a4be` | identical |
| `~/.claude/CLAUDE.md` | `70965424868e929d1ef026d8339906cfae88ab6a2d1d840e52b476c54bd0c866` | identical |
| `git status --porcelain` of this engine | `39479f022eafe20dd93eb9dde083d5985f615bf70dcf0bbb4eff0107c0c36a0c` (one pre-existing modification by another phase: `scripts/routing_smoke_test.py`) | only this record and the T05 scan record are new; the other modification was committed by its own phase during the session |

Because nothing was installed, there is nothing to uninstall and no sandbox to quarantine.

## Constraints any future run must keep

These restate the M10-00 disposition D2 (UA-01) and the M10-13 protocol; they are not new rules.

- Marketplace install at a pinned version, `autoUpdate` off, hooks not enabled; never `curl | bash` or `iwr | iex`.
- A copy of a synthetic project only, outside `C:\wamp64\www`; no client material; the live engine is never converted to the wiki layout and gains no wikilinks.
- Never on the same repository as Graphify.
- Token spend logged from the session usage report; uninstall and quarantine (not delete) the sandbox at the end.

## Re-entry condition

Re-open only when **both** hold: Peter lifts the zero-spend rule for this pilot and approves the install explicitly; and the UA-01 reversal trigger is met (a pinned, reviewed release without the confirmation-suppressing hook text and self-executing agents). Adoption would additionally need at least one implicit-claim edge judged useful and a per-project token cost that Peter records as acceptable. Given the evidence in the Understand Anything repository report (§5.6: the engine's projects lack the index and wikilink layout the parser expects), the expected outcome of a future run remains reject.

## Evidence

- Phase file: `my-10-kaizen/03-phases/M10-13-cross-engine-extensions.md`, task M10-13-T04 and §6 value gate.
- Disposition: `chwezi-engine-agents/docs/operations/third-party-tool-dispositions-2026-09-29.md`, D2.
- Executor evidence: `chwezi-engine-agents/docs/operations/m10-kaizen-evidence/M10-13/`.
