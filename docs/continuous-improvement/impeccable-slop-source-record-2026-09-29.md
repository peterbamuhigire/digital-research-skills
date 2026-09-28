# Source Record: Impeccable Repository (refresh of the 2026-09-03 slop-catalogue record)

Supersedes [`impeccable-slop-source-record-2026-09-03.md`](impeccable-slop-source-record-2026-09-03.md),
which was taken from the web page alone, listed no commit and fell due for review on 2026-10-03.
Kaizen task: my-10-kaizen M10-01-T14 (IM-05).

| Field | Value |
|---|---|
| `source_id` | `impeccable-repo-114ea1d-2026-09-29` |
| Supersedes | `impeccable-slop-page-2026-09-03` |
| Repository | https://github.com/pbakaus/impeccable (default branch `main`) |
| Commit reviewed | `114ea1d3838fca73b253af45f873b9c4f5f213c8` (committed 2026-09-28T17:12:18Z; HEAD of `main` when checked on 2026-09-29) |
| Licence | Apache-2.0 (GitHub API `license.spdx_id`); `NOTICE.md` carries an MIT attribution for the iOS and Android references |
| Publisher/author | Paul Bakaus (repository owner; LICENSE "Copyright 2025 Paul Bakaus") |
| Companion page | https://impeccable.style/slop/ (re-read 2026-09-29: "61 detector rules and 6 patterns for design review") |
| Source tier | Tier 1 for Impeccable's own detector taxonomy and doctrine; not independent evidence of prevalence or of machine authorship |
| Access date | 2026-09-29 |
| Freshness class | `context-bound` (the rule registry grew from 59 to 61 rules between 17 Aug and 28 Sep 2026) |
| Scope | Deterministic detector rules, LLM-only design-review patterns, skill doctrine and reference layout at the pinned commit |
| Owner | Digital Research Engine maintainer |
| Review date | 2026-12-29, or earlier before any dependency, command or universal-standard claim is introduced, or when an Impeccable skill release changes the rule registry |

## What was verified at `114ea1d`

| Claim | Status | Evidence |
|---|---|---|
| 61 registered detector rules | `supported` | `crates/foundation/src/registry.rs` at the pinned commit: 61 unique rule ids (fetched through the GitHub contents API, 2026-09-29). `docs/CLI-CONTRACT.md` still says 59; the registry is the authority. |
| 6 LLM-only design-review patterns | `supported` | impeccable.style/slop states "61 detector rules and 6 patterns for design review" (2026-09-29). |
| v4 removed the brand/product register | `supported` | Repository `CLAUDE.md` "Modes": four per-surface modes (Persuade, Operate, Read, Experience) replace the register axis; `reference/brand.md` and `reference/product.md` no longer exist. |
| v4 removed the per-domain references | `supported` | Repository `CLAUDE.md`: "Do not reintroduce per-domain reference files." Removed files include `typography.md`, `color-and-contrast.md`, `spatial-design.md`, `motion-design.md`, `interaction-design.md`, `responsive-design.md` and `ux-writing.md`; their content was folded into the command references and `craft-floor.md`. The `skill/reference/` listing at the pinned commit confirms their absence. |
| Every listed pattern is machine-generated or always defective | `not supported` | The page itself calls a finding "a reason to look closer". The record supports a scoped review overlay, not a blanket style ban. |

No detector was installed or executed; precision and recall remain `NOT_ASSESSED`. No independent
evaluation of the detector was found.

## Consequences for the portfolio

- Citation form for Impeccable-derived material: "Impeccable (Paul Bakaus), Apache-2.0,
  https://github.com/pbakaus/impeccable, commit 114ea1d (reviewed 2026-09-29)". Ideas are
  paraphrased; no Impeccable source text or code is copied.
- Citations updated on 2026-09-29 (every "(Bakaus, 2025)" citation in the engines):
  - design `skills/00-cross-cutting-ops-qa-a11y/design-audit/SKILL.md`;
  - design `skills/04-web-and-ui-design/ai-output-design/references/ai-slop-prevention/entrypoint.md`;
  - design `skills/08-motion-and-interaction/motion-design/SKILL.md` (`superseded-upstream`);
  - dev `skills/frontend-ux/tailwind-css/references/responsive-design/entrypoint.md` (`superseded-upstream`);
  - dev `skills/frontend-ux/ux-content-strategy/references/ux-writing/entrypoint.md` (`superseded-upstream`).
- `superseded-upstream` means the Impeccable reference the citation names was removed in v4. The
  Chwezi text remains Peter's paraphrase and is retained as house guidance.
- Design authority rule: Impeccable is evidence for bans only. Positive typeface or design
  approvals must trace to a human authority.
- The 61-rule registry at this commit is the rule-source pin for the M10-09 deterministic detector.

## Extracted evidence groups (unchanged from 2026-09-03, now pinned to the commit)

- Visual convergence: default palettes and typefaces, decorative gradients and glows, glass
  surfaces, side-tab borders, nested or identical cards, icon tiles, hero labels and metrics,
  monotonous spacing.
- Copy convergence: redundant labels, buzzword clusters, repeated dash cadence, manufactured
  aphorisms, theatrical framing.
- Interaction and delivery quality: decorative motion, fake cursors, marquees, missing or generic
  imagery, invisible content, contrast failures, cramped or overflowing content, heading and text
  legibility defects.
