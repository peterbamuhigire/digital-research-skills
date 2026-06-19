---
name: ai-slop-audit
description: Analyse, evaluate, and audit any artefact for AI slop and grade it. Runs after EACH major iteration of research work (a drafted section, a completed cohort, a synthesis, a generated .docx) and auto-runs whenever the user asks to analyse, review, evaluate, audit, critique, score, or "de-slop" any report, dossier, document, app, website, business plan, SRS, proposal, blog post, image, or codebase — or asks "does this look AI-generated?". Produces a graded slop report — per-marker findings with severity, evidence, and a concrete fix. Pairs with anti-ai-slop (real-time prevention).
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
  priority: high
  source: ai-slop-detector research (2026-06-07), verified
---

# AI Slop Audit

The detector. Given any artefact, it decides how strongly it reads as AI slop, names exactly why, and says how to fix each finding. Prevention is the companion `anti-ai-slop` skill; truthfulness is `source-evaluation`.

## When this runs

**Cadence — run after EACH major iteration of work on the project at hand.** This is the default mode: when a meaningful unit is completed — a drafted report section, a finished cohort, a synthesis pass, a generated .docx, a significant revision — audit what was just produced before moving on. Log the verdict. If the verdict is **F (Blocked)**, do not progress to the next iteration until the blocking findings are fixed. Treat it like a test suite that runs at every checkpoint.

**Also auto-run on request:** when the user asks to analyse, review, evaluate, audit, critique, score, or de-slop any report, dossier, document, website, app, business plan, SRS/spec, proposal, blog/article, social post, image/video, or codebase — or asks "is this AI slop / does this look AI-generated?".

**Also run as the final gate** before delivering any engine output or building the final .docx.

The companion `anti-ai-slop` runs continuously *during* writing; this audit runs *at each checkpoint* to catch what slipped through.

## What slop is (the yardstick)

Low-quality content produced in quantity by AI and pushed at people who did not ask for it (Merriam-Webster 2025 Word of the Year, verified). Three diagnostic properties (Kommers et al., arXiv 2601.06060, verified): **superficial competence, asymmetric effort, mass producibility**. The human tell: **absence of intent**.

## Audit method — layered, cheapest first

### Step 1 — Identify artefact type and load the right checklist
Map the artefact to one or more domains: research report/document (written EN/FR), UI/UX, app/product, image/video, code. A project (website, app, dossier) usually spans several — audit each layer.

### Step 2 — Automated gates ([auto], machine-checkable) — any hit is hard evidence
Run every applicable check; a hit on a blocking marker ([BLOCK]) fails the artefact outright.

**Written content / reports**
- [auto] Focal-word density — delve/tapestry/realm/navigate/underscore/pivotal/intricate/leverage etc. >2 per 500 words.
- [auto] Em-dash density >1 per paragraph; reflexive rule-of-three; "it's not X, it's Y" repetition; uniform 15-25-word sentences (low burstiness).
- [auto] Transition clichés ("in today's fast-paced world", "let's dive in", "in conclusion").
- [auto] Mechanical formatting: Title-Case headers, excess bold, decorative emoji, leftover tool markup ("oaicite", "contentReference").
- [BLOCK] [auto] Broken/fake citations: dead URLs, invalid DOI/ISBN, fabricated stats, "studies show" with no named study, source missing at point of claim.

**UI/UX**
- [auto] Indigo/purple-gradient default (HSL 250-280deg, sat 70%+); Inter/Roboto/Poppins-only; uniform border-radius; glassmorphism; gradient text; shadcn coloured card-border.
- [BLOCK] [auto] Body/dark-mode contrast <4.5:1 (WCAG fail); missing states (error/empty/loading/focus/disabled).

**Code**
- [BLOCK] [auto] Hallucinated/uninstallable imports & packages (slopsquatting) — resolve every dependency against its registry.
- [BLOCK] [auto] Hardcoded secrets; SQL by string interpolation; innerHTML = userInput (XSS); insecure defaults.
- [auto] Placeholder stubs/TODO/NotImplementedError in shipped code; dead code; duplication; bare-except; tautological tests (assert true).

**Image/video**
- [auto] Missing/contradictory C2PA provenance; SynthID absence (Google-only — absence != authentic); ELA/JPEG-forensics anomalies.

### Step 3 — Structural score ([auto]) -> 0-100 "genericness"
Combine burstiness, focal-word density, duplication, and template-similarity into one genericness score. Higher = more slop-like. Report the score and its drivers.

### Step 4 — Human-judgement review ([human]) — the checklist no tool replaces
- [human] **Substance:** what does this assert/decide that required real work? If nothing — slop.
- [human] **Intent / authored judgement:** is there a stated analytic point of view, or viewpoint-free summary?
- [human] **Specificity:** real named sources, figures, dated events — or generic placeholders?
- [human] **Hard parts:** counter-case, limitation, contradicting source, gap addressed?
- [human] **Domain-specific:**
  - *Research report/dossier:* claims sourced at point of use; analytic judgement per section; gaps marked, not filled with plausible filler.
  - *Business plan:* fabricated market stats, generic TAM/SAM filler, no authored strategy.
  - *SRS/spec:* vague requirements, placeholder "Challenges and Future Prospects" sections, missing edge/error specs, hallucinated APIs.
  - *Proposal/EoI:* inflated superlatives, hollow analogies, unverifiable claims, no visible logic.
  - *Blog/social:* engagement-bait, no lived experience, clichés, AI-sheen imagery.

## Scoring & verdict

| Grade | Meaning | Trigger |
|---|---|---|
| A — Clean | No blocking hits; low genericness; substance & judgement present | ship |
| B — Minor slop | A few automated hits, no blockers | fix listed items |
| C — Slopy | Multiple hits or weak substance/judgement | rework before ship |
| F — Blocked | Any [BLOCK] (hallucinated fact/citation/package, secret, WCAG fail, missing states) OR no substance | do not ship |

## Output format (the audit report)

```
# AI Slop Audit — <artefact> — <date>
Verdict: <A/B/C/F>   Genericness: <0-100>
Artefact type(s): <...>

## Blocking findings ([BLOCK]) — must fix
- [marker] <finding> · evidence: <quote/line/URL/colour/region> · fix: <action>

## Slop findings (by severity)
- [marker] <finding> · evidence: <...> · fix: <...>

## What's good (keep in the fix)
- <substantive, specific, authored elements worth keeping>

## Recommended next step
- <rework / targeted fixes / ship>
```

## Discipline (the audit itself must not hallucinate)
- Every finding cites concrete evidence from the artefact (a quote, line number, colour value, region, URL). No evidence, no finding.
- Do not invent a flaw to pad the report. "This artefact is clean" is a valid, wanted verdict.
- Mark inferences "(inference)".

## See also
- `anti-ai-slop` — real-time prevention companion.
- `source-evaluation` — the truth/credibility gate.
- `professional-word-output` — apply when the audited artefact is a .docx.
