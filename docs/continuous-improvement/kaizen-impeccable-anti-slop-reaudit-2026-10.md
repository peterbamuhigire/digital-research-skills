# Kaizen Re-audit: Impeccable-Derived Anti-Slop Overlay (AS1-AS7)

**Re-audit of:** [`kaizen-impeccable-anti-slop-2026-09-03.md`](kaizen-impeccable-anti-slop-2026-09-03.md) (due 2026-10-03)
**Opened:** 2026-09-29, ahead of the due date, under my-10-kaizen M10-09-T14 (BL-09a)
**Source record:** [`impeccable-slop-source-record-2026-09-29.md`](impeccable-slop-source-record-2026-09-29.md) (Impeccable at commit `114ea1d`)
**Owner:** Digital Research Engine maintainer. The design engine owns the detector.
**Status:** measured re-audit complete. The retain/adjust decision below was taken by the orchestrator under Peter's delegated authority on 29 Sep 2026. Phase acceptance (independent review and design CI run) is pending.

## What changed since 2026-09-03

The overlay defined `cli` and `browser` evidence modes, but no Chwezi command sat behind them. M10-09
built `chwezi-slop` in `design-system-skills/tools/slop-detector/`: 49 registry rules (42 static,
7 browser), each keyed to one AS check, each with an authority record, a severity, a tier and a
flag/pass fixture pair. This re-audit uses that detector's output as `MEASURED` evidence of
pattern presence. Taste, prevalence and machine-authorship claims remain `NOT_ASSESSED`.

Registry `tools/slop-detector/rules/registry.json`, SHA-256
`750eaf523fda9be3de2dd783d793498a035ec7a66c16323cfd89310dafd66cd0`. Node v24.8.0, Python 3.13.7,
Playwright 1.61.1 (locked in a scratch consuming project, not in any engine repository).

## AS coverage matrix

| AS | Executable rules (block / warning / advisory) | Tiers | Evidence modes available | Rules |
|---|---|---|---|---|
| AS1 default choices | 11 (3 / 4 / 4) | immediate, deep | `cli` | banned-primary-font, conditional-source-sans-primary, flat-type-hierarchy, heading-wide-tracking, body-wide-tracking, italic-serif-display, ai-beige-ground, pure-black-body-text, design-system-font, design-system-color, design-system-font-size |
| AS2 unearned authority | 4 (0 / 4 / 0) | deep | `cli` | decorative-side-stripe, hero-eyebrow-chip, kicker-above-heading, numbered-section-labels |
| AS3 flattened hierarchy | 4 (0 / 2 / 2) | deep | `cli` | nested-cards, identical-three-column-feature-grid, thin-border-wide-shadow, design-system-radius |
| AS4 attention without value | 11 (5 / 4 / 2) | immediate, deep | `cli` | gradient-text, purple-blue-gradient, neon-glow, glassmorphism, radial-halo, stripes-or-grid-background, bounce-easing, pulsing-dot, blinking-cursor, marquee, missing-reduced-motion |
| AS5 placeholder material | 1 (0 / 1 / 0) | deep | `cli` | placeholder-image-host. Generic or shape-assembled imagery stays `NOT_ASSESSED` (needs visual judgement). |
| AS6 copy tells | 0 built in | n/a | `NOT_ASSESSED` in design | Digital Research owns written-copy slop (ME1-ME7). Copy rules load as a data-only `--extra-rules` pack over DRE or website phrase lists; wiring lands in M10-11. The pack mechanism is tested (`registry.test.mjs`). |
| AS7 concealed delivery debt | 18 (2 / 13 / 3) | immediate, deep, browser | `cli`, `browser` | body-leading-tight, body-leading-loose, extreme-negative-tracking, justified-body-text, tiny-text, all-caps-body, line-length, skipped-heading, gray-on-color, broken-local-image, focus-indicator-removed, horizontal-overflow, clipped-positioned-child, text-occlusion, content-hidden-at-rest, script-error, low-contrast-computed, first-viewport-column-overflow |

Every AS row names at least one executable rule, except AS6, which is `NOT_ASSESSED` in the
design engine for the ownership reason stated. Severity ladder: `block` needs a WCAG criterion,
an engine doctrine line or a dated house ruling. Rules with only AI-tool evidence are `advisory`
and never fail a run.

## Detector runs

All outputs are in `chwezi-engine-agents/docs/operations/m10-kaizen-evidence/M10-09/`.

| Target | Command (from the target repo) | Files | Findings after review (block / warning / advisory) | Waived | Output |
|---|---|---|---|---|---|
| Design fixtures | `node tools/slop-detector/cli.mjs --json tests/fixtures/slop` | 84 | Every flag fixture reports its rule; no pass fixture reports anything | 0 | `fixtures-run.json` |
| Design `skills/` and `examples/` | `… --json --tier deep skills examples` | 623 | 0 / 8 / 0 | 9 | `engine-self-scan.json` |
| Design, wider (adds `templates/`, `doctrine/`, `governance/`) | `… --json --tier deep skills examples templates doctrine governance` | 642 | 0 / 8 / 0 | 9 | `engine-self-scan-wide.json` |
| Website `fixtures/website-kaizen` | `node <design>/tools/slop-detector/cli.mjs --json fixtures/website-kaizen` | 3 | 0 / 1 / 0 | 0 | `website-kaizen-scan.json` |
| Website `skills/` (read-only) | `… --json skills` | 489 | 4 / 1 / 3 | 0 | `website-skills-scan.json` |
| Dev `skills/frontend-ux/` (read-only; no `examples/` folders exist, so every file was scanned) | `… --json skills/frontend-ux` | 77 | 0 / 1 / 0 | 0 | `dev-frontend-ux-scan.json` |
| Browser acceptance fixtures | `… --tier browser …/failed-reveal-and-clipped-tooltip.html …/clean.html` | 2 pages x 2 viewports | `content-hidden-at-rest` and `clipped-positioned-child` fire on the failed-reveal page; none fire on `clean.html` | 0 | `browser-acceptance.json` |
| Browser, cross-engine | `… --tier browser <website-kaizen> <design examples/kraal…/index.html>` | 3 pages | 0 findings; one remote Google Fonts request was blocked by the local-only rule | 0 | `browser-cross-engine-scan.json` |

### Review of findings (true or false positive)

- **Design self-scan: 8 findings, all true positives on review.**
  - 2 × `kicker-above-heading` (a layout example and the Kraal dashboard heading).
  - 1 × `tiny-text` (an 11 px healthcare table label).
  - 1 × `skipped-heading` (h1 to h3 in a dark-mode snippet).
  - 4 × `missing-reduced-motion` (sector templates with no reduced-motion path).
  - The one `block` finding in the engine's own templates, `bounce-easing` from an `animate-bounce` scroll arrow in the education template, was remediated in this phase.
- **Waivers issued: 9 findings across 4 files.**
  - 2 status-encoding side stripes in the healthcare examples, under the Option A ruling.
  - 6 findings inside 2 deliberate before-state counter-examples: the typography audit and the before/after UI example. These are quoted slop the example then fixes.
  - Every waiver has a "<who>: <evidence>" reason.
- **False-positive rate: 0 of 8 unwaived design findings after review, against a target of 5 % or less.**
  - Development tuning is recorded honestly: the first self-scan returned 111 findings, most of them false positives. Examples were card parts such as `card-header` read as nested cards, pull quotes, drop caps, email preheader hiding text, colour-only transitions, `img { outline: none }` resets, a documented `--font-system` fallback token, neutral tree-guide borders, text typed in capitals, lead and display-size text, JS hook classes (`animate-on-scroll`) and a baseline-grid debug overlay.
  - Each class was fixed in the rule and pinned by a pass fixture where practical. Precision on unseen code remains `NOT_ASSESSED` beyond these corpora.
- **Cross-engine: all true positives against design doctrine. Nothing was edited in those engines.**
  - Website: `glassmorphism` × 2 in `skills/build/design-system/liquid-glass-effects.md`, which conflicts with the design no-ship boundary and is for M10-11 to resolve. Also `banned-primary-font` (DM Sans, newly banned on 29 Sep) and an overshooting `cubic-bezier` in `references/legacy-guidance.md`, 1 reduced-motion finding and 3 advisory findings.
  - Website Kaizen fixture: 1 cream-ground warning.
  - Dev: 1 `text-black` body paragraph in `tailwind-css/SKILL.md`.

## 12/12 adapter check

`python -X utf8 scripts/validate_machine_error_gate.py` fails as committed. The reason is one
stale path: the `digital-research` target still points at `C:/wamp64/www/digital-research-skills/…`,
the engine's name before it was renamed. With that single path rewritten in a scratch copy of the
fixture, the gate reports `PASS (identifier presence only)` for all 12 engines and every ME1-ME7
and AS1-AS7 identifier. Semantic, editorial and visual verification remain `NOT ASSESSED`.

Result: **12/12 adapters present, measured with one stale fixture path.** The fixture
correction (`tests/fixtures/machine-error-gate-baseline.json`, `digital-research-skills` to
`digital-research-engine`) is an open item for the DRE owner. It was not edited here because
other executors were working in this repository.

## Measures against the 2026-09-03 targets

| Measure | Target | Result | Evidence class |
|---|---|---|---|
| AS1-AS7 coverage | 12/12 registered engine adapters | 12/12 present (one stale fixture path to fix) | `MEASURED` (identifier presence) |
| Pressure fixture | One observable case per AS check plus functional exceptions | 42 static and 7 browser flag/pass pairs. Exceptions are pinned by pass fixtures: status side stripe, blockquote, `--font-system`, streaming caret, nav chrome blur, live status dot | `MEASURED` |
| Native gates | No new validator or routing failures | Design `validate_engine` 101/101 plus the slop registry floors; routing smoke passes; pytest 108 passed; Node suites pass | `MEASURED` |
| Evidence discipline | No universal-prevalence claim; unsupported visual judgement stays `NOT_ASSESSED` | Detector findings claim only that a pattern is present. AS5 imagery taste and AS6 copy are `NOT_ASSESSED` in design. Browser rules without a locked Playwright report `NOT_ASSESSED`, never a pass | `MEASURED` |
| Stop condition | No adapter suppresses required repetition, accessibility, safety, traceability or legally operative wording | Not triggered. Status encodings, focus replacements, reduced-motion blocks and streaming carets are explicit exceptions | `HEURISTIC` (review) |

## Decision

**Retain** AS1-AS7 as a scoped overlay. **Adjust** it by adding the `cli` and `browser`
evidence modes, now backed by `chwezi-slop`. Impeccable stays optional and source-bound. It is
not installed, not a dependency, and its catalogue is not a blacklist. Its rule ideas are
paraphrased with attribution (Apache-2.0, commit `114ea1d`), and its font lists are evidence for
bans only. The decision was taken by the orchestrator under Peter's delegated authority on
29 Sep 2026. Peter's exact-diff ratification of the doctrine-class items (severity ladder,
waiver format, side-stripe option, watchlist decisions) is recorded as pending at phase
acceptance.

## Open items

1. Fix the stale `digital-research-skills` path in `tests/fixtures/machine-error-gate-baseline.json` (DRE owner).
2. Website M10-11: resolve the `liquid-glass-effects.md` glassmorphism conflict and the DM Sans and bounce findings in `legacy-guidance.md`, then wire `slop-scan.sh` to the frozen CLI contract and load AS6 as a data pack.
3. Design follow-up: add reduced-motion variants to the four sector templates flagged by `missing-reduced-motion`.
4. The design CI run URL is `NOT_ASSESSED` until the orchestrator pushes. The browser tier is not in CI (it needs a locked Playwright), so it stays a local, recorded run.
5. Next re-audit: 2026-12-29, together with the quarterly check of Impeccable's registry (61 rules at `114ea1d`).
