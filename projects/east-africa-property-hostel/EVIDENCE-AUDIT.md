# Evidence Audit — east-africa-property-hostel

Running log of caught hallucinations, citation drift, fabricated content, and corrections. Per the engine's `evidence-discipline` skill.

## Log format

```markdown
## YYYY-MM-DD
- Source agent / wave: <which sub-agent / which wave>
- Fabricated content: "<the exact text>"
- Caught by: <human reviewer | spot-check | URL-fetch | source-grep>
- Action: <strike | flag | replace | source-found>
- Lesson: <what to change in the next prompt>
```

## Open items requiring verification (before final Word export)

- **"~90% single-women rejection rate"** — single source (Medium / Daily Nation synthesis). Independent verification needed before publishing as a hard statistic. Currently flagged in `tenants/research/pain-points-report.md` as needing verification.
- **"~95% of EA rental stock is non-accessible to PWDs"** — described as "estimate" in `tenants/analysis/vulnerable-groups.md`; source not anchored. Either find the underlying survey or downgrade to "(inference)".
- **"~50,000–100,000 informal Somali tenants in Nairobi"** — range claim from "synthesised from UNHCR Kenya & UN-Habitat". Locate the specific UNHCR / UN-Habitat document that supplies the range; if not findable, mark as inference.
- **All Reddit findings in `landlords/` and `tenants/`** — sub-agent flagged that real-time scraping was constrained by ToS and only "consolidated themes" were captured. No verbatim Reddit quotes in any project file. Confirm none have leaked in.
- **Acorn Holdings FY'25 financials (KSh 1.52bn profit, 20,000 beds)** — verify against Acorn's NSE filings or annual report rather than relying on the agent's summary.
- **Kenyatta U Africa Integras PPP "stalled"** — agent flagged "no 2024–25 completion updates found." Re-search for confirmation before stating "stalled" definitively.
- **Tribunal Case E007 of 2024 and Muhanda v LP Holdings 2025** — verify on kenyalaw.org. Both cases were cited but not URL-confirmed.
- **"Komakech & 7 Ors v Ayaa & Anor 2018"** — verify on ULII.

## Closed items

(none yet — first audit pending)

## Process

Before generating any final Word report:

1. Walk this list top to bottom
2. For each open item, attempt verification with `WebFetch` against primary source
3. Move resolved items to "Closed items" with the verification URL
4. For items that **cannot** be verified, do one of:
   - Mark with `(inference)` or `(estimated)` in the source markdown file
   - Strike from the report and remove from the corpus
   - Convert to a "gap — no source found" finding

This list grows over the project's lifetime. Every Wave-2 spot-check or human review can add new items. **Never** quietly remove an item without recording the resolution.
