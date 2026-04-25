---
name: knowledge-lifecycle-pipeline
description: Use to model every research artefact as a state machine moving through eight lifecycle stages. Each stage has its own issues, support mechanisms, and value contribution. The single most important framework from Bryan Bergeron's Essentials of Knowledge Management.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Knowledge lifecycle pipeline

Bergeron: every knowledge artefact moves through eight interrelated stages. Treating them implicitly causes deferred-translation rot, format-migration failure, and lost institutional memory. Treating them explicitly turns research into a *manageable asset*.

## The eight stages

1. **Creation / acquisition** — original capture (sub-agent finds; user-uploaded; primary-source extract)
2. **Modification** — editing, refinement, integration with other artefacts
3. **Use** — quoted, cited, applied to a decision, included in a report
4. **Archiving** — long-term storage with retrieval metadata
5. **Transfer** — moved across systems, projects, or owners
6. **Translation / repurposing** — converted to a new format / audience / language
7. **Access** — retrieved by future users / agents
8. **Disposal** — retired when superseded or no longer useful

A **tracking function** runs in parallel — knowing where each artefact is in the pipeline.

## Six issue-axes per stage

For every stage, evaluate:

| Axis | Question |
|---|---|
| **Economics** | What does this stage cost? What's its value contribution? |
| **Accessibility** | Who can reach the artefact at this stage? |
| **Intellectual property** | Who owns it; what licensing applies; can we resell / repurpose? |
| **Information** | Format, naming, reversibility, versioning |
| **Infrastructure** | Storage, backup, search index, redundancy |
| **Management** | Who is responsible? When? With what KPIs? |

## Five support mechanisms

For any stage:

1. **Technology** — tools, software, hardware
2. **Standards** — file formats, naming conventions, taxonomies
3. **Knowledge workers** — analysts, researchers, sub-agents
4. **Management** — accountability, prioritisation
5. **Librarian** — the under-appreciated keystone; owns artefact across full lifecycle

## Decision rules

- **Every research artefact has a current stage.** The crosswalk should reflect it.
- **Translation / repurposing is the highest-value-multiplier stage.** A finding becomes a report; the report becomes a slide deck; the deck becomes an op-ed; the op-ed becomes a thesis chapter. Same insight, four products.
- **Disposal is a real stage.** Stale claims should be retired explicitly, not allowed to silently rot.
- **Format migration is mandatory.** Files become unreadable as software evolves; the librarian role plans this.
- **Tracking function ≠ optional.** Without it, artefacts drift unmanaged.

## Where each stage lives in the engine

| Stage | Engine artefact / skill |
|---|---|
| Creation / acquisition | Sub-agent dispatch; primary source capture |
| Modification | `minianalysis-engine` writes; `evidence-discipline` checks |
| Use | Cited in `research-report-builder` outputs |
| Archiving | Project file tree; git history |
| Transfer | Cross-project linking; export to client deliverable |
| Translation / repurposing | Schema-A → Schema-O (popular essay) reuse |
| Access | Future projects' `crosswalk-matrix` looking up prior work |
| Disposal | `EVIDENCE-AUDIT.md` mark-stale items |

## The Incremental Value Curve (Bergeron's Exhibit 7.6)

Value contribution by stage, roughly:
- Creation / Acquisition — sharp rise
- Modification — flat
- Use — rise
- Archiving — flat
- **Translation / Repurposing — second sharp rise** (highest monetisation moment)
- Access — rise
- Disposal — decay

**Implication:** the engine should optimise for repurposing. Reports should be designed knowing they'll spawn essays, decks, and theses.

## Anti-patterns

- Treating archiving as the end (it's the middle)
- No format migration plan — files become unreadable
- No disposal stage — stale claims persist as if current
- No translation / repurposing — finding lives once and dies
- No tracking function — artefacts drift without management
- Treating librarian role as overhead (it's where institutional memory lives)

## Monetisation

Bergeron's monetisable patterns map onto stages:

- **Sell the audit** — a knowledge audit (lifecycle inventory) at fixed price
- **Repurposing premium** — same insight, multiple formats, multiple price points
- **Subscription access** — Stage 7 monetised
- **Knowledge escrow** — premium tier reserves access to certain stages

## See also

- `research-design-document` — defines the project; lifecycle applies to the project's outputs
- `crosswalk-matrix` — operational view of artefacts in flight
- `research-report-builder` — Stage-3 + Stage-6 productisation
- `evidence-discipline` — gates Stage-1 quality
- `research-monetisation-playbook` (roadmap) — full monetisation framework
