# Codex model-policy review: GPT-6 Luna

**Decision date:** 2026-09-25
**Runtime scope:** Codex only. Claude model selection and permissions are unchanged.
**Authorization:** Peter explicitly authorized replacement of the GPT-5 Luna pins with GPT-6 Luna on 2026-09-25.

## Evidence and scope

- The official [OpenAI models catalog](https://developers.openai.com/api/docs/models) identifies `gpt-6-luna` and positions it for cost-sensitive, high-volume work. It lists input/output API prices of $0.10/$0.50 per million tokens, versus $0.20/$1.20 on the [GPT-5.6 Luna model page](https://developers.openai.com/api/docs/models/gpt-5.6-luna) as checked on this date.
- The official [GPT-6 Luna model page](https://developers.openai.com/api/docs/models/gpt-6-luna) lists `high` reasoning support, a 1.05M-token context window, and a 128K-token maximum output.
- The official [ChatGPT Work and Codex availability page](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex) says GPT-6 Luna is a Work/Codex model, with availability dependent on plan, workspace settings, and rollout access.
- The installed Codex CLI `debug models` catalogue on this machine, inspected 2026-09-25, contains `gpt-6-luna` as a selectable listed model and includes `high` reasoning. A fresh `codex exec --ephemeral --model gpt-6-luna` invocation then completed successfully on 2026-09-25, confirming access for this CLI/account context at that time; workspace or entitlement changes may alter future availability.

## Task fit and tradeoffs

The existing policy uses Luna for the root/orchestrator, reviewer, and bounded execution roles, all at high reasoning. GPT-6 Luna supports that reasoning level and OpenAI positions it for efficient, focused work, so the role assignment transfers without changing scope or reasoning effort. Published token pricing is lower than the checked GPT-5.6 Luna pricing.

No controlled quality or latency comparison for this engine's representative work was available in the sources reviewed. Treat quality and latency deltas as **NOT_ASSESSED**; the change is authorized and matches the user's selected family, but this record does not claim GPT-6 Luna is better on those measures. Account/workspace entitlement remains **NOT_ASSESSED** until a new session successfully starts with the model.

## Decision and limits

- **Change:** set Codex root, reviewer, execution-role templates, engine policies, and managed Codex configuration to `gpt-6-luna` with high reasoning.
- **Retain:** `gpt-6-astra` only as an explicit user-selected exception where its additional capability is wanted; do not change Claude settings.
- **Do not infer:** changing files does not switch an already-running session. The explicit fresh CLI invocation succeeded; new Codex sessions use the persisted selection unless a profile or session override applies.
- **Re-review:** by 2026-10-25, or earlier if OpenAI changes the model catalog, Codex availability, or the user's workload needs.

## Evidence record

| Claim | Source | Access/verification | Support | Uncertainty |
|---|---|---|---|---|
| GPT-6 Luna ID, positioning, listed price, reasoning and limits; GPT-5.6 Luna API pricing | Official OpenAI model catalog and model pages; source IDs in the central currentness register | 2026-09-25 | Verified for published facts | Provider positioning is not an independent task benchmark; latency and comparative quality are NOT_ASSESSED |
| GPT-6 Luna is offered for Codex subject to plan/workspace/rollout | Official ChatGPT Work and Codex page; source ID in central register | 2026-09-25 | Verified for stated availability conditions | Entitlement can vary by plan/workspace and can change over time |
| Local Codex CLI lists `gpt-6-luna` with high reasoning and a fresh CLI invocation succeeds | `codex debug models` and `codex exec --ephemeral --model gpt-6-luna` local runtime observations | 2026-09-25 | Observed; explicit invocation completed successfully | Confirms this CLI/account context at test time, not every future profile or session |
