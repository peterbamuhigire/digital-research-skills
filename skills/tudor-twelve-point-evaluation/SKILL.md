---
name: tudor-twelve-point-evaluation
description: Use to evaluate media, journalism, and analyst sources beyond the 5-tier credibility ladder. Twelve-criterion rubric covering recency, relevancy, authority, completeness, accuracy, clarity, verifiability, statistical validity, internal consistency, external consistency, context, comparative quality. From Robin Rowland citing Dean Tudor.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Tudor's twelve-point evaluation

Where `source-verification` tiers a source by class and `five-term-source-doubt` situates a primary document, Tudor's rubric scores any source — especially journalism, analyst reports, and grey literature — across twelve dimensions. From Dean Tudor via Robin Rowland's *Creative Guide to Research*.

## The twelve criteria

| # | Criterion | Test question |
|---|---|---|
| 1 | **Recency** | When was the source produced? Has the situation changed since? |
| 2 | **Relevancy** | Does it address the specific question, or only adjacent topics? |
| 3 | **Authority** | Is the author / outlet recognised in the domain? |
| 4 | **Completeness** | Does it cover the topic in full, or only one angle? |
| 5 | **Accuracy** | Are the facts checkable? Have they been checked? |
| 6 | **Clarity** | Is the argument well-structured, or muddled? |
| 7 | **Verifiability** | Are sources, methods, data accessible? |
| 8 | **Statistical validity** | If quantitative — sample size, methodology, error bars |
| 9 | **Internal consistency** | Do statements within the source agree with each other? |
| 10 | **External consistency** | Does it agree with other sources on shared facts? |
| 11 | **Context** | Is the situational background provided, or assumed? |
| 12 | **Comparative quality** | How does it compare to peer sources on the same topic? |

## Three optional criteria for financial / business sources

Rowland adds:

- **Understandability** — is the financial information accessible to non-specialists?
- **Reliability / representational faithfulness** — does the report represent what it claims?
- **Comparability** — can it be benchmarked against industry / peer entities?

## Scoring

Each criterion: 0 (fail) / 1 (weak) / 2 (acceptable) / 3 (strong). Out of 36 (or 45 with financial extensions).

Recommended thresholds:
- **≥30/36** — promotable to Tier 3 in `source-verification` even if originally Tier 4
- **20–29** — usable with explicit caveats
- **<20** — quote selectively; do not anchor major claims on it
- **Any single criterion = 0** — flag the entire source for re-evaluation

## Decision rules

- **Apply to every analyst report, NGO report, journalism investigation** before citing it as a primary anchor.
- **Don't apply to peer-reviewed academic sources** — they have their own review process.
- **Don't apply to user-generated content** — Tier 5 doesn't get this treatment; it's flagged separately.
- **Document the score per criterion**, not just the total. The pattern of weakness matters.
- **Re-score periodically.** Recency erodes; external consistency may shift as new sources emerge.

## Worked example — Cytonn Q1 2026 Markets report

| Criterion | Score | Note |
|---|---|---|
| Recency | 3 | Published 18 Jan 2026, covers Q3 2025 |
| Relevancy | 3 | Explicit residential coverage |
| Authority | 3 | Established Kenyan analyst |
| Completeness | 2 | Some segments thinly covered |
| Accuracy | 2 | Spot-checks pass; methodology not always disclosed |
| Clarity | 3 | Good prose, clear tables |
| Verifiability | 1 | Methodology box thin |
| Statistical validity | 2 | Sample sizes per neighbourhood not disclosed |
| Internal consistency | 3 | No contradictions found |
| External consistency | 3 | Aligns with Hass Consult, KNBS |
| Context | 2 | Macro context light |
| Comparative quality | 3 | Best-in-class for KE residential |
| **Total** | **30/36** | Promote to upper Tier 3 with note that methodology disclosure is weak |

## Anti-patterns

- Single-number tier-only scoring without per-criterion breakdown
- Applying to peer-reviewed academic — they're already vetted
- Forgetting Internal vs External consistency are different (a source can be self-consistent while being externally wrong)
- Scoring once and never updating
- Citing strong-on-some-criteria sources as if strong on all

## See also

- `source-verification` — tier ladder this rubric refines
- `five-term-source-doubt` — for primary documents specifically
- `evidence-discipline` — the umbrella discipline
- `gap-analysis` — low-scoring criteria are real gaps
