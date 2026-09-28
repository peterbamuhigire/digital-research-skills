# Model-currentness review: GPT-6 Luna policy

**Review date:** 2026-09-28  
**Scope:** Codex model-policy pins for Kaizen, orchestration, review, and execution  
**Decision:** Retain `gpt-6-luna` with high reasoning as the default; retain `gpt-6-astra` only when Peter explicitly selects it. Do not promote `gpt-6-sol` without representative task evidence.

## Current-source check

The official [OpenAI model catalogue](https://developers.openai.com/api/docs/models) lists GPT-6 Astra (`gpt-6-astra`), GPT-6 Sol (`gpt-6-sol`), and GPT-6 Luna (`gpt-6-luna`). The [API changelog](https://developers.openai.com/api/docs/changelog), checked on this date, shows a 2026-09-25 image-encoding fix for GPT-6 Sol and Luna and their 2026-09-22 release; it shows no later model release. The fix is relevant to image-input workflows and does not establish a quality or latency change for this text-focused policy review.

The official [Codex and ChatGPT Work release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) state that Sol and Luna are available in Work and Codex, subject to plan and workspace settings. On this device, `codex debug models` listed Astra, Sol, and Luna with visibility `list`; Luna included `high` reasoning. A fresh `codex exec --ephemeral --model gpt-6-luna -c model_reasoning_effort=high` invocation succeeded under the installed Codex CLI (v0.156.0) and returned the requested response. This verifies the local CLI/account context on the review date; it does not prove entitlement in other profiles or the identity of an already-running root session.

## Task fit and trade-offs

OpenAI describes Luna as its efficient model for focused, high-volume tasks and lists `high` reasoning support on the [Luna model page](https://developers.openai.com/api/docs/models/gpt-6-luna). Its [model-selection guide](https://developers.openai.com/api/docs/guides/model-selection) places Luna on focused edits and scoped problem solving, Sol on everyday coding and judgment, and Astra on more demanding analysis and complex deliverables. This is provider guidance, not an independent comparison on Peter's Kaizen workload.

The published standard, short-context API rates are USD 0.10 input / USD 0.50 output per million tokens for Luna, USD 2 / USD 10 for Sol, and USD 10 / USD 50 for Astra, according to the [current model catalogue](https://developers.openai.com/api/docs/models). API rates do not establish Codex subscription or account cost. No controlled quality, latency, or task-cost comparison for Peter's representative engineering and cross-engine workload was available; those measures remain **NOT_ASSESSED**. The successful CLI response establishes availability only, not output quality.

## Decision and review cadence

Retain the user's existing Luna/high default. Do not change provider or reasoning effort on the basis of release recency or vendor positioning alone. Keep Astra as an explicit user-selected exception and do not change Claude settings. The image-encoding fix warrants evaluation when a future Kaizen task materially depends on model image input; no image benchmark was run in this review.

Check official releases and the active runtime/account catalogue on every Kaizen operation. Reuse this fuller task-fit comparison for up to three months only while those checks find no relevant release or catalogue change. Run a new comparison sooner after a relevant release, a proposed policy change, or an availability problem. Current active root-session model identity, subscription cost, and comparative quality/latency remain **NOT_ASSESSED**.

## Source register

All sources were opened or queried on 2026-09-28. Official OpenAI documentation is primary for OpenAI's model IDs, published capabilities, prices, release history, and stated availability; it is not independent evidence of comparative model quality.

| Source ID | Source and scope | Publication/version date | Access and verification | Freshness and review date |
|---|---|---|---|---|
| S01 | [OpenAI API model catalogue](https://developers.openai.com/api/docs/models): public model IDs, provider descriptions and listed standard API rates | Live catalogue; no page revision date shown | Accessed and page content checked 2026-09-28 | Time-sensitive; check every Kaizen cycle; full review by 2026-12-28 |
| S02 | [GPT-6 Luna model page](https://developers.openai.com/api/docs/models/gpt-6-luna): reasoning support, limits, and Luna details | Live page; no page revision date shown | Accessed and page content checked 2026-09-28 | Time-sensitive; scope limited to published API documentation; full review by 2026-12-28 |
| S03 | [GPT-6 Sol model page](https://developers.openai.com/api/docs/models/gpt-6-sol): Sol identity and published capabilities | Live page; no page revision date shown | Accessed and page content checked 2026-09-28 | Time-sensitive; scope limited to published API documentation; full review by 2026-12-28 |
| S04 | [GPT-6 Astra model page](https://developers.openai.com/api/docs/models/gpt-6-astra): Astra identity and published capabilities | Live page; no page revision date shown | Accessed and page content checked 2026-09-28 | Time-sensitive; scope limited to published API documentation; full review by 2026-12-28 |
| S05 | [OpenAI model-selection guide](https://developers.openai.com/api/docs/guides/model-selection): provider task-fit guidance | Live guide; no page revision date shown | Accessed and page content checked 2026-09-28 | Time-sensitive vendor guidance; not a benchmark; full review by 2026-12-28 |
| S06 | [OpenAI API changelog](https://developers.openai.com/api/docs/changelog): dated model release and image-encoding entries | Latest relevant entries dated 2026-09-25 and 2026-09-22 | Accessed and entries checked 2026-09-28 | Time-sensitive; check every Kaizen cycle; full review by 2026-12-28 |
| S07 | [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes): Work/Codex model availability conditions | Relevant entry dated 2026-09-22 | Accessed and entry checked 2026-09-28 | Time-sensitive; actual access depends on plan/workspace; full review by 2026-12-28 |
| R01 | Local `codex debug models` output on this device | Runtime catalogue observed 2026-09-28 | Queried 2026-09-28 | Local visibility only; listing does not by itself prove entitlement; retest by 2026-12-28 or sooner on policy/availability trigger |
| R02 | Local `codex exec --ephemeral --model gpt-6-luna -c model_reasoning_effort=high` | Codex CLI v0.156.0; invocation observed 2026-09-28 | Exit 0 and expected response observed 2026-09-28 | Confirms that invocation in this CLI/account context only; retest by 2026-12-28 or sooner on policy/availability trigger |
| R03 | `python -X utf8 .codex/ensure_model_policy.py --runtime codex --check` in `chwezi-dev-engine` | Configuration observed 2026-09-28 | Output `PASS` on 2026-09-28 | Checks persisted configuration; does not identify a running root session; recheck by 2026-12-28 or sooner on policy/availability trigger |

## Claim register

| Claim ID | Claim | Source IDs and tier | Access/verification | Freshness, support and uncertainty | Confidence / owner |
|---|---|---|---|---|---|
| M01 | The public catalogue lists GPT-6 Astra, Sol, and Luna; Luna supports high reasoning | S01-S04, tier 1 official primary documentation | 2026-09-28 | Time-sensitive; supported for the pages checked | High for published facts / Codex policy owner |
| M02 | The 2026-09-25 image-encoding fix applies to GPT-6 Sol and Luna; those models were released 2026-09-22 | S06, tier 1 official primary documentation | 2026-09-28 | Supported for dated changelog entries; task impact outside image input is unassessed | High for release record / Codex policy owner |
| M03 | Luna appears in this device's Codex catalogue with high reasoning and executed successfully in this CLI/account context | R01-R02, direct local runtime observations | 2026-09-28 | Supported for this local context only; other profiles/workspaces and the already-running root session are unassessed | High for observed local result / Codex policy owner |
| M04 | Luna/high remains the default; Astra remains user-selected only; Sol is not promoted by this review | S01-S05, tier 1 vendor documentation; R02 confirms availability, not quality | 2026-09-28 | Decision preserves the user-authorised policy; vendor positioning is not independent task-fit evidence | Moderate decision confidence; comparative quality is unassessed / Peter retains policy authority |
| M05 | No measured quality, latency, or Codex subscription-cost comparison supports changing the default | No source; no representative benchmark or account-cost data available | Checked 2026-09-28 | `NOT_ASSESSED`; API prices are not Codex subscription prices | Not assessed / Codex policy owner |
