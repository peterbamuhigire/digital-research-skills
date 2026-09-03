---
name: ai-slop-audit
description: Use when auditing a concrete artefact for AI slop after a major iteration or before release, with evidence-backed findings, fixes, genericness score, and A/B/C/F verdict; use anti-ai-slop during production rather than for retrospective grading.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
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

#### Machine-error review (human-evidence required)

- [ME1] Compare adjacent units for repeated meaning, not only repeated words; cite both units and the missing delta.
- [ME2] Identify decorative symmetry, antithesis, or evenly shaped lists that do not express a real distinction.
- [ME3] Mark explanation that continues after the reader can act or decide.
- [ME4] Mark significance language that exceeds the evidence, scale, or consequence.
- [ME5] Mark examples that could be moved to another context unchanged; require a traceable replacement or removal.
- [ME6] Count repeated rhetorical devices and report the recurrence that makes them mannerisms.
- [ME7] Mark paragraphs with no claim, warrant, evidence, comparison, implication, or decision.

Do not issue a semantic finding from a keyword count alone. If the context or reviewer cannot
establish the meaning delta, record `NOT_ASSESSED`.

#### Impeccable-derived overlay review

For visual or interface artefacts, review AS1-AS7 and record the evidence mode (`cli`, `browser`,
`llm_only`, or `human_review`). Treat purple gradients, glassmorphism, neon glow, AI-beige defaults,
decorative editorial scaffolding, and decorative motion as blocking visual findings unless a
functional state, accessibility need, data encoding, or approved design-system reason is recorded.
For non-visual artefacts, mark visual checks `not_applicable`; unavailable render or browser evidence
is `NOT_ASSESSED`.

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

## Machine-error findings
- <ME1-ME7> <unit> · evidence: <affected units or recurrence> · delta: <what is missing> · action: <keep/merge/cut/rewrite/not_assessed>

## Anti-slop overlay findings
- <AS1-AS7> <unit> · evidence mode: <cli/browser/llm_only/human_review> · task value or exception: <...> · action: <keep/reduce/remove/rewrite/not_applicable/not_assessed>

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

<!-- dual-compat-start -->
## Use When

Use after a concrete iteration exists and before release.

## Do Not Use When

Do not use to generate the artefact or edit it without separate remediation authority.

## Inputs

| Input | Source/provider | If absent |
|---|---|---|
| Concrete artefact, purpose, audience | Requester or workspace | Stop; no artefact means no auditable evidence |
| Applicable source, dependency, render, or state evidence | Owner and available tools | Mark unavailable checks `not assessed` |

## Audit Core Method

1. Classify the artefact and applicable checks.
2. Run machine-checkable gates before judgment checks.
3. Cite exact evidence for each finding and stop on any blocking marker.
4. Grade consistently; name unavailable checks rather than passing them.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Graded audit report | Author or release owner | Every finding has location, severity, evidence, fix, and unassessed checks |

## Audit Evidence Guidance

The audit report, check results, and evidence locations support the verdict.

## Capability Contract

Default to read-only. Editing, publication, destructive action, spending, and certification require separate explicit authority.

## Degraded Mode

Report inaccessible checks as `not assessed`; do not lower risk, invent findings, or issue a clean verdict that depends on them.

## Decision Rules

| Evidence | Action | Failure/risk avoided |
|---|---|---|
| Blocking factual, security, citation, or accessibility defect | Grade F and block | Harmful release |
| Supported non-blocking marker | Grade B or C and prescribe fix | Vague critique |
| No supported finding | Preserve clean verdict | Invented debt |

## Audit Quality Notes

Verdicts follow evidence, not preference, and unavailable checks remain visible.

## Audit Pitfalls

- Reporting an “AI feel”; cite a marker.
- Inventing flaws to fill sections; allow a clean audit.
- Editing during diagnosis; request authority.
- Treating inaccessible checks as passes; mark them.
- Removing authored specificity; list what to preserve.

## Audit Scenario

An inaccessible rendered page is marked `not assessed`; text-only findings do not imply a visual pass.

## References

- [Production-time prevention](../anti-ai-slop/SKILL.md)
<!-- dual-compat-end -->

## Workflow

1. Classify the artefact and list every applicable machine and judgment check.
2. Run objective checks first and preserve exact locations for each hit.
3. Stop and grade F when a blocking defect is supported by evidence.
4. Recover unavailable checks by marking them `not assessed`; retry when the required artefact or tool becomes available.
5. Assign the verdict from the evidence and preserve authored material that should survive remediation.

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Audit report and check log | Author and release owner | Every finding has an exact location, severity, supporting evidence, and concrete correction |

## Quality Standards

Every verdict agrees with its blocking markers, every finding cites observable evidence, and every unavailable check remains explicitly unassessed.

## Anti-Patterns

- Reporting an undefined “AI feel.” **Fix:** cite the exact marker and location.
- Inventing defects to fill the report. **Fix:** allow a clean verdict when evidence supports it.
- Editing during diagnosis. **Fix:** request separate remediation authority.
- Passing an inaccessible check. **Fix:** mark it `not assessed`.
- Removing useful authored specificity. **Fix:** identify material that remediation must preserve.

## Worked Example

If a document page cannot be rendered, the audit marks visual checks unassessed while still reporting separately evidenced citation and prose findings.

## See also
- `anti-ai-slop` — real-time prevention companion.
- `source-evaluation` — the truth/credibility gate.
- `professional-word-output` — apply when the audited artefact is a .docx.
