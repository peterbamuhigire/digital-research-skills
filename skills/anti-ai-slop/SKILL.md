---
name: anti-ai-slop
description: Use when producing or revising any research artefact to prevent generic, unsupported, repetitive, or mechanically styled output in real time; use ai-slop-audit to grade a concrete completed iteration independently.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
  priority: critical
  source: ai-slop-detector research (2026-06-07), verified
---

# Anti AI Slop

The guardrail that governs **production quality** — writing and assembling research outputs so slop never appears. Detection is the companion `ai-slop-audit` skill. Truthfulness is `source-evaluation/references/evidence-discipline.md`; this skill is its quality counterpart: a report can be fully sourced and still read as slop (generic, voiceless, template-uniform). Both gates must pass.

## Real-time application (a LIVE constraint, not only a final gate)

Apply these rules continuously, as you write — to every sentence, table, finding, and slide at the moment it is drafted, not in one cleanup pass at the end. The moment you reach for a banned word, a generic placeholder, an unverified figure, or a template default, correct it in place. The ship-gate checklist below is the final confirmation, not the first time these rules are consulted.

## What "AI slop" is (so you know what you are preventing)

Low-quality content produced in quantity by generative AI and pushed at people who did not ask for it (Merriam-Webster 2025 Word of the Year, verified). Three diagnostic properties (Kommers et al., *"Why Slop Matters"*, arXiv 2601.06060, verified): **superficial competence, asymmetric effort, mass producibility**. The human tell named in every domain studied: **absence of intent**. A research output beats slop by re-internalising effort — specificity, verification, and authored judgement — before it reaches the reader.

## The seven universal guardrails (apply to EVERY output)

| # | Marker to prevent | Avoidance rule you MUST follow |
|---|---|---|
| U1 | Genericness / averaging | Every section carries >=1 concrete, named, source-specific element (a real figure, named source, dated event, decision) a generic template could not produce. |
| U2 | Superficial competence | Substance floor: include an analytic claim, comparison, or judgement the section could not exist without. If you cannot, it is filler — cut it. |
| U3 | Confident wrongness / hallucination | Verify every statistic, quote, citation, name, and URL before it ships; cite at the point of claim; mark inferences "(inference)" and gaps "(no source found)". Defers to evidence-discipline. |
| U4 | Volume over substance | One sourced, reasoned paragraph beats three hollow ones. Do not pad to length. |
| U5 | Absence of authored voice / judgement | State the analytic point of view: what the evidence means, not just what it says. No relentless hedging, no viewpoint-free summary. |
| U6 | Skipping the hard parts | Address the counter-case, the limitation, the contradicting source, the gap — not just the confirming evidence. |
| U7 | Mechanical uniformity | Vary sentence and section structure. No rule-of-three reflex, no "it's not X, it's Y" formula, no em-dash flood, no uniform paragraph length. |

## Banned / high-risk vocabulary (the lexical tells)

Over-produced by LLMs (FSU/COLING-2025; PubMed "delve" +400%, verified). Allowed only when genuinely the precise term, never as default register.

- **Words:** delve, tapestry, realm, landscape (as metaphor), navigate (as metaphor), leverage, foster, harness, synergy, embark, robust, vibrant, holistic, seamless, intricate, commendable, meticulous, pivotal, underscore, testament, resonate, elevate, paramount, multifaceted.
- **Phrases:** "in today's fast-paced world", "in the ever-evolving landscape of", "it is important to note that", "let's dive in", "at the end of the day", "in conclusion", "studies show" (without a named study).
- **Constructions:** the "it's not just X, it's Y" antithesis; reflexive rule-of-three lists; em-dash used to manufacture drama; triplet adjectives ("robust, scalable, reliable").

## Drop-in guardrail block (inherit in dependent skills)

```
ANTI-SLOP GUARDRAIL (inherit in every output):
1. SPECIFICITY FLOOR — every section carries >=1 concrete, named, source-specific element.
2. VERIFY-BEFORE-EMIT — no statistic, quote, citation, name, or URL ships unverified;
   cite at point of claim; mark inferences and gaps. (Defers to evidence-discipline.)
3. AUTHORED JUDGEMENT — say what the evidence means; no viewpoint-free summary, no sycophancy.
4. COVER THE HARD PARTS — counter-case, limitation, contradicting source, gap.
5. BREAK THE TEMPLATE — vary rhythm and structure; forbid the banned-vocabulary list above.
```

## Domain-specific avoidance (research outputs)

- **Report / dossier / memo:** named sources at the point of every claim; a stated analytic judgement per section; the contradicting evidence shown, not hidden; varied section shapes (not every section a three-bullet list).
- **Tables / data:** every figure carries a source and date; no round-number "estimates" presented as measured; flag computed/derived values.
- **.docx output:** apply the `professional-word-output` design standard (named styles, two typefaces, real hierarchy) so the document looks human-made, not template-extruded.
- **Academic / proposal:** visible logic (evidence -> warrant -> implication); no inflated superlatives; British English and house tone per the project.

## Ship gate (run before delivering ANY output)

- [ ] Every section has >=1 concrete, named, source-specific element (U1/U2).
- [ ] Every stat, quote, citation, name, URL verified and cited at point of claim (U3 / evidence-discipline).
- [ ] No banned vocabulary used as register; output scanned against the list.
- [ ] Output states an analytic judgement; no viewpoint-free summary, no sycophancy (U5).
- [ ] Counter-case, limitation, or gap addressed (U6).
- [ ] Sentence and section structure varied; no rule-of-three reflex, no antithesis formula, no em-dash flood (U7).
- [ ] For .docx, `professional-word-output` standard applied.
- [ ] When in doubt, run `ai-slop-audit` on the draft.

If any box is unticked, the output is not ready to ship.

## See also

<!-- dual-compat-start -->
## Use When

Use throughout production and revision of every research artefact.

## Do Not Use When

Do not substitute it for the independent `ai-slop-audit` release verdict.

## Required Inputs

| Input | Source/provider | If absent |
|---|---|---|
| Draft artefact, purpose, audience | Producing workflow | Stop generic generation and request context |
| Verifiable facts and dependencies | Evidence register | Remove or qualify unsupported specificity |

## Workflow

1. Identify the artefact type and intended action.
2. Apply specificity, verification, voice, hard-case, and variation controls while drafting.
3. Stop on fabricated or unverifiable content and recover by removing it or marking a gap.
4. Run the domain ship gate, then route the iteration to `ai-slop-audit`.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Guarded artefact | Requesting workflow | Every section earns its place and all claims are verified or qualified |

## Production Evidence Guidance

The completed ship gate and verification-gap log support release review.

## Production Capability Notes

Apply only capabilities authorised for the parent task. Mutation, publication, destructive action, spending, or certification requires explicit authority.

## Degraded Mode

Fallback when a fact, dependency, citation, or visual check is unavailable: name the gap and return the narrowest useful qualified artefact; never turn an unassessed check into a pass.

## Decision Rules

| Finding | Action | Failure/risk avoided |
|---|---|---|
| Unsupported specificity | Verify, qualify, or remove | Hallucination |
| Generic non-blocking prose | Rewrite or cut | Superficial content |
| Intentional verified material | Preserve | Destructive over-editing |

## Quality Standards

Every claim is verified or qualified, every section carries intent, and errors, empty states, risks, and countercases are addressed where applicable.

## Anti-Patterns

- Inventing a number for specificity. **Fix:** verify it or remove it.
- Keeping polished filler. **Fix:** add a sourced judgement or cut it.
- Waiting for the final audit. **Fix:** apply controls live.
- Flattening authored voice. **Fix:** preserve intentional choices.
- Hiding an unavailable check. **Fix:** name the gap and its release consequence.

## Worked Example

If a current market figure cannot be verified, the draft records the evidence gap instead of inserting a plausible estimate.

## References

- [Independent audit](../ai-slop-audit/SKILL.md)
- [Evidence discipline](../source-evaluation/references/evidence-discipline.md)
- `extracted-books/human-english-craft-synthesis-2026.md` — human-English reader, genre, rhythm, grammar, and proof overlay; routed from the engine-level `AGENTS.md`.
<!-- dual-compat-end -->

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Completed ship gate and verification-gap log | Producing workflow and release reviewer | Every section has intentional substance and every claim is verified, qualified, or removed |

## Capability Contract

Minimum capability is read-only access to the draft, facts, and dependencies. Any editing, mutation, publication, destructive action, spending, or certification requires explicit authorisation from the parent task.

## Production Pitfalls

- Inventing a number for specificity. **Fix:** verify it or remove it.
- Keeping polished filler. **Fix:** add a decision or evidence, otherwise cut it.
- Waiting for the final audit. **Fix:** apply controls during production.
- Flattening an intentional voice. **Fix:** preserve authored choices that serve the audience.
- Hiding an unavailable check. **Fix:** name the gap and its release consequence.

## See also
- `ai-slop-audit` — the per-iteration detection/audit companion.
- `source-evaluation` / `references/evidence-discipline.md` — the truth gate this pairs with.
- `professional-word-output` — document-design standard for .docx outputs.
