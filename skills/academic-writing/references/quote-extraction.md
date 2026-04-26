# Quote extraction

Reports without quotes feel abstract. Reports with badly attributed quotes feel dishonest. This skill standardises the middle path.

## Three classes of quote

| Class | Definition | Use as |
|---|---|---|
| **Primary** | Speaker's actual words, attributed to them in the source | Quotable verbatim |
| **Secondary** | Reported speech in journalism — "she said X" | Quotable with "via [outlet]" framing |
| **Paraphrased** | Synthesised summary of position | Mark explicitly: "(paraphrased)" |
| **Inferred** | Implied from data / behaviour | Never quote — describe instead |

## Attribution structure

Every primary quote stored in a `quotes.md` file gets:

```markdown
> "Verbatim text exactly as it appeared in the source."
— Speaker name (or "an X resident") + role
[Outlet or direct citation], date
```

Example:

```markdown
> "80% of tenants have never gotten a refund of their security deposit..."
— Daily Monitor Uganda investigation
[Daily Monitor](https://...), August 2023
```

## Decision rules

- **Quote the data, not the journalist.** If a stat appears in a journalism piece, attribute the stat to its underlying source where possible.
- **Verbatim or nothing.** If you can't reproduce the exact words, use indirect speech.
- **Date every quote.** Statistics rot; sentiment dates; legal frames change.
- **Anonymise where the source did** — "a Mathare resident" rather than inventing a name.
- **Translate carefully.** If the source is in Swahili, Luganda, or French, include both the original and the translation, marked as such.
- **No fabrication.** Never invent a quote to illustrate a pattern. If no quote exists, say so.

## Anti-patterns

- "An expert said..." with no name
- Stitching together two non-adjacent sentences as one quote
- Removing context that changes meaning
- Quoting a paraphrase as if it were primary
- Using ellipses to hide qualifying clauses
- Quoting Reddit comments as primary tenant voice without acknowledging the platform-bias

## Output target

`<cohort>/research/quotes.md` organised by theme, with attribution as above. Each quote should be retrievable by theme key for downstream `research-report-builder` use.

## See also

- `source-verification` — credibility tiers underpin which quotes are quotable
- `social-source-extraction` — Reddit / X / TikTok quote pipelines
- `research-report-builder` — consumes `quotes.md` for pull-quotes in Word output
