---
name: digital-research-engine
description: Use when routing evidence-disciplined research across intake, source evaluation, web search, OSINT, due diligence, academic review, policy research, synthesis, verification, and final deliverables.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Digital Research Engine Router

This router turns a user request into the minimum skill stack required to produce research that is traceable, well-reasoned, and release-ready. It is the entrypoint for the engine, not a replacement for sub-skills.

## Non-negotiable foundation

Always load these before research work:

1. `skills/source-evaluation/SKILL.md`
2. `skills/source-evaluation/references/evidence-discipline.md`
3. `skills/anti-ai-slop/SKILL.md`

4. `docs/continuous-improvement/portfolio-kaizen-standard-2026-08.md` for every engine or
   research-product audit, improvement plan, or book-study integration.

All engines may route here for current-source verification. This engine also audits its own
research outputs: use `skills/00-meta-initialization/references/kaizen-engine-and-product-audit.md`,
publish the current audit at a maximum of 65/100, and produce a remediation plan targeting 95/100.

Every sub-agent prompt must include the hard-constraint clause from `evidence-discipline.md` verbatim.

## Route by user intent

| User intent | Primary skill | Companion skills |
|---|---|---|
| Start or scope a research project | `skills/00-meta-initialization/SKILL.md` | `skills/research-orchestration/SKILL.md`, `skills/research-design/SKILL.md` |
| Plan waves, cohorts, or work allocation | `skills/research-orchestration/SKILL.md` | `skills/agentic-research-operations/SKILL.md` |
| Search strategy, query design, source discovery | `skills/research-techniques/SKILL.md` | `skills/web-scraping-foundations/SKILL.md` |
| Source credibility and evidence discipline | `skills/source-evaluation/SKILL.md` | `skills/source-verification/SKILL.md` |
| Verify URLs, quotes, statistics, archives, citations | `skills/source-verification/SKILL.md` | `tools/verification/source_verifier.py` |
| OSINT or public-record investigation | `skills/osint-investigation/SKILL.md` | `skills/due-diligence/SKILL.md`, `skills/source-evaluation/SKILL.md` |
| Corporate due diligence | `skills/due-diligence/SKILL.md` | `skills/online-legal-research/SKILL.md`, `skills/data-quality-pipeline/SKILL.md` |
| Primary research interviews or field evidence | `skills/primary-research/SKILL.md` | `skills/research-design/SKILL.md` |
| Data discovery or dataset analysis | `skills/dataset-discovery-and-analysis/SKILL.md` | `skills/data-quality-pipeline/SKILL.md`, `tools/reports/citation_density_dashboard.py` |
| Academic paper, thesis, dissertation, systematic review | `skills/academic-reporting-standards/SKILL.md` | `skills/academic-writing/SKILL.md`, `docs/source-registers/research-standards-register.md` |
| Forward-looking judgment, scenario, warning, risk call | `skills/analytic-tradecraft/SKILL.md` | `skills/calibration-and-forecasting/SKILL.md`, `skills/peer-review-loop/SKILL.md` |
| Executive memo, board brief, consulting report | `skills/executive-communication/SKILL.md` | `skills/critical-reasoning-and-argument/SKILL.md` |
| Final report or proposal craft | `skills/report-and-proposal-craft/SKILL.md` | `skills/research-output-formats/SKILL.md`, `skills/professional-word-output/SKILL.md` |
| Word, PDF, Excel, or rendered deliverable | `skills/python-document-generation/SKILL.md` | `skills/professional-word-output/SKILL.md`, design-system-skills engine |
| Skill authoring or engine extension | `skills/skill-writing/SKILL.md` | `skills/skill-composition-standards/SKILL.md` |
| Engine or product improvement audit | `skills/00-meta-initialization/references/kaizen-engine-and-product-audit.md` | `skills/source-evaluation/SKILL.md`, `skills/source-verification/SKILL.md` |

## Running example

Use `docs/world-class-exemplars/running-example.md` as the shared example across sub-skills: a Chwezi Core Systems research engagement on informal cross-border trade digitisation in East Africa. It includes executive, academic, OSINT, data, and policy variants without relying on invented statistics.

## Standard operating sequence

1. Intake: define audience, decision, research type, output family, risk level, and stop conditions.
2. Evidence: load source-evaluation and evidence-discipline; assign source tiers at collection time.
3. Design: choose method, cohorts, search plan, and data needs.
4. Collection: run waves; log sources, search strings, exclusions, and unresolved gaps.
5. Verification: run source-verification and the verifier tool before synthesis.
6. Reasoning: run critical-reasoning and analytic-tradecraft where claims, judgments, or recommendations appear.
7. Synthesis: build the claim graph, answer-first message, and evidence pack.
8. Output: use the format skill matching the deliverable and apply anti-slop gates.
9. Release: run quality gates, citation density dashboard, reviewer notes, and final manifest.

## Stop conditions

Stop and ask for clarification when the request lacks the decision/audience, asks for private surveillance, asks for fabricated or unsourced claims, requires current legal/regulatory facts that cannot be verified, or asks to publish a claim whose source trail fails verification.

## See also

- `docs/skill-authoring-standard.md`
- `docs/pathing-model-engine-vs-projects.md`
- `docs/quality-gates/release-blocking-gates.md`
- `docs/source-registers/research-standards-register.md`
- `templates/research-evidence-pack-template.md`
- `examples/research-types/README.md`
