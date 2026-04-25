---
name: source-verification
description: Use when ranking, triangulating, or auditing the credibility of sources in a research corpus. Defines a 5-tier credibility ladder, URL-liveness checks, fact triangulation rules, and quote-attribution discipline.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Source verification

Not all sources are equal. This skill tags every source with a credibility tier and enforces triangulation for high-impact claims.

## The 5-tier ladder

| Tier | Type | Examples | Use as |
|---|---|---|---|
| 1 | Peer-reviewed academic + official statistics | Wiley, SAGE, KNBS, World Bank | Primary, citable |
| 2 | Regulatory / institutional | KRA, URA, ULII, Kenyalaw, IRA, NEMA, university reports | Primary, citable |
| 3 | Established journalism with bylines | Daily Monitor, Daily Nation, The Standard, The Citizen, BBC, Reuters | Quotable, attribute clearly |
| 4 | Industry analyst / NGO | Cytonn, CrossBoundary, Hass Consult, CAHF, Hakijamii | Quotable with framing context |
| 5 | Social / blog / forum | Reddit, Twitter, Medium, TikTok, WhatsApp screenshots | Indicative themes only — never as sole source |

## Decision rules

- **High-impact claims need ≥2 tier-1/2 sources, OR 1 tier-1 + 1 tier-3.**
  - Headline statistics, court precedents, statutory citations
- **Quoted statistics get the source attached at point of citation**, not just in a bibliography
- **Tier 5 alone is never enough** — must be paired with a tier-1/2/3 corroborator
- **URL liveness** — verify before publishing. Dead links break trust faster than missing sources
- **Date-stamp every source** — laws and statistics rot
- **Distinguish primary from secondary attribution** — "Daily Nation reporting that KNBS found X" must cite the KNBS report, not just Daily Nation

## Triangulation patterns

When two sources disagree:

1. Prefer the **higher-tier** source
2. If tied, prefer the **more recent**
3. If still tied, prefer the **closer-to-source** (KNBS report > journalism quoting KNBS)
4. Document the disagreement in the report — don't silently pick one

## Quote-attribution discipline

Every direct quote needs:
- Speaker (or "an X resident") + role
- Outlet (if reported speech) OR direct citation (if primary)
- Date
- Source URL

Paraphrased / inferred quotes get marked as such. Never present a paraphrase as if it were a verbatim quote.

## Anti-patterns

- Citing a tier-5 source for a headline statistic
- Listing URLs at the bottom without binding them to specific claims
- Quoting "an expert" without naming, role, or outlet
- Treating Reddit consensus as evidence
- Linking to a paywalled source without flagging the paywall
- Citing search-engine snippets without verifying the underlying page

## See also

- `academic-source-mining` — feeds tier-1 sources
- `quote-extraction` — implements quote-attribution discipline
- `gap-analysis` — flags tier-imbalance in a corpus
