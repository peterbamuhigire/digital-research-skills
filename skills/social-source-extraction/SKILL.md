---
name: social-source-extraction
description: Use when surfacing social-platform voices (Reddit, X, Facebook groups, TikTok comments, WhatsApp) for a research project. Defines methodology, tooling, ToS limits, and the Tier-5-with-corroboration discipline.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Social source extraction

Social platforms carry the freshest, most candid voice on a research domain — and the most platform-bias and noise. This skill defines how to mine them responsibly.

## Platforms & methods

| Platform | Method | Notes |
|---|---|---|
| Reddit | PRAW (Python Reddit API Wrapper) with OAuth | Free, rate-limited ~60 req/min; respect ToS |
| Reddit (paid) | Apify Reddit Scraper | Paid; bypasses some rate limits |
| Reddit archives | Pushshift | Largely deprecated post-2023 |
| Reddit (last resort) | Search-engine indexed snippets | Theme-level only, no quote extraction |
| X / Twitter | API v2 (paid tiers) | Free tier severely limited |
| X (last resort) | Search-engine indexed snippets | Theme-level only |
| Facebook public groups | Manual login | Closed groups inaccessible |
| TikTok | Comment scraping via Apify or manual | Comment sections are gold; not bulk-searchable |
| YouTube | Comment API + manual | Long-form content useful |
| WhatsApp / Telegram | Voluntary screenshot submission only | Closed; ToS-protected |

## Decision rules

- **Tier 5 alone is never enough.** Corroborate with at least one Tier 1/2/3 source.
- **Always note the platform** in attribution — "an r/Kenya commenter" not "a tenant".
- **Quote conservatively.** Social posts are public but written casually; treat speakers with dignity.
- **Anonymise where the user expects privacy** — don't surface usernames in reports unless they are clearly public-figure accounts.
- **Document the method used** — which scraping tool, what auth, what date — so the result is reproducible.
- **Acknowledge platform bias.** Reddit skews English-speaking, urban, internet-connected. Twitter skews political. TikTok skews young. None is representative.

## Reddit-specific reference (PRAW path)

```python
import praw
reddit = praw.Reddit(
    client_id="...",
    client_secret="...",
    user_agent="research-engine/1.0"
)
for sub in ["Uganda", "Kenya", "Tanzania", "Rwanda"]:
    for post in reddit.subreddit(sub).search("landlord", time_filter="year", limit=100):
        # extract post.title, post.selftext, post.url, post.score, post.num_comments
        for comment in post.comments.list():
            # extract comment.body, comment.author, comment.created_utc
            ...
```

This is the canonical East-African-tenant / landlord research method when verbatim quotes are needed.

## Apify Reddit Scraper (paid alternative)

When PRAW rate limits become blocking:
- [Apify Reddit Scraper](https://apify.com/trudax/reddit-scraper)
- Define keyword + subreddit list + time window
- Returns JSON of posts + comments

## Output target

`<cohort>/research/social-corpus.md` (when generated) with each entry tagged:

```markdown
> "Verbatim social post text"
— u/<username if public-figure>, [r/Kenya](https://...) | <date>
**Platform context:** Reddit r/Kenya; <post score / context>
**Corroborated by:** [Daily Nation 2024](...) — same finding
```

## Anti-patterns

- Treating Reddit consensus as evidence
- Quoting a commenter without naming the platform
- Surfacing usernames of non-public-figure tenants in a final report
- Using social posts as the sole source for a statistic
- Ignoring platform bias in synthesis

## See also

- `source-verification` — Tier-5 corroboration discipline
- `quote-extraction` — attribution rules apply
- `gap-analysis` — Reddit gaps are usually search gaps, not structural
