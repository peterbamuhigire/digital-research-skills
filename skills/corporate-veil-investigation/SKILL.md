---
name: corporate-veil-investigation
description: Use to investigate corporate ownership structures, shell-company networks, and beneficial-owner trace. Combines registry walks, Whois clustering, foreign-extension classification, and offshore-leak corpora. Backed by tools/dd/ubo.py + foreign_extensions + registry_atlas.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Corporate-veil investigation

Hetherington: walk *up* (parent), walk *down* (subsidiaries), then cross to *related parties* via shared officers/addresses/phones. Surface shell signals.

## The four-pillar UBO trace

### 1. Walk parent (up the tree)
- D&B Global Family Tree → LexisNexis Corporate Affiliations → Orbis → Sayari (precedence)
- Confirm with secretary-of-state filings (`tools.dd.registry_for_country`)
- Look for **foreign-company tag** (e.g., a Kenya business legally incorporated in BVI)

### 2. Walk subsidiaries (down the tree)
- Same registries, downward link
- Note **franchise vs subsidiary** distinction (different liability propagation)

### 3. Cross to related parties
- Shared officers across entities → red flag
- Shared registered address → shell signal
- Shared phone number → shell signal
- Shared registered agent → shell signal
- Property records cross-check at the registered address (co-tenants)

### 4. Foreign-extension classification
Use `tools.dd.foreign_extension_for(name)` to detect jurisdiction from suffix:

```python
from tools.dd import foreign_extension_for

foreign_extension_for("BugCo Sp. z.o.o.")
# → [{"country": "PL", "type": "Spółka z ograniczoną odpowiedzialnością — private LLC"}]

foreign_extension_for("Acme AVV")
# → [{"country": "AW", "type": "Aruba Vrijgestelde Vennootschap — Aruba exempt company"}]
```

## Standard workflow

```python
from tools.dd import trace_ubo, find_shared_officers, find_shared_addresses
from tools.registry.companies_house import fetch_parent, fetch_subsidiaries, fetch_officers

# UBO walk
graph = trace_ubo(
    seed_entity_id="01234567",
    seed_name="Acme Holdings Ltd",
    fetch_parent=fetch_parent,
    fetch_subsidiaries=fetch_subsidiaries,
    fetch_officers=fetch_officers,
    max_depth_up=5,
    max_depth_down=3,
)

# Render as Mermaid for the DD report
print(graph.to_mermaid())

# Cross-graph related-party detection
shared_off = find_shared_officers([graph_acme, graph_other])
shared_addr = find_shared_addresses([graph_acme, graph_other])
```

## Shell-company red flags (Hetherington's catalogue)

| Signal | Why it matters |
|---|---|
| Registration in tax-haven address (Road Town BVI, Camana Bay, Wickhams Cay) | Operations probably elsewhere |
| "c/o trust company" in registered-address line | Indirect control |
| HQ in UAE / Ireland / Switzerland for activity that doesn't justify it | Tax-arbitrage cover |
| Virtual / one-day-suite leases | No real substance |
| Website registrant ≠ named principals | Identity mismatch |
| Multiple unrelated companies sharing one address | Shell ring |
| WHOIS / corporate filing mismatch | Corporate fiction |
| Foreign-currency capital with mostly bearer shares (Aruba AVV, Uruguay SAFI) | Anonymity preference |
| No annual-report filings where required | Compliance avoidance |
| Sudden directory-of-affiliations gap | Restructure to obscure |

## Cross-jurisdictional notes

- **China**: Hetherington's Phase-2 OSINT can be **criminal**. Capvision raid (2023), Peter Humphrey / Yu Yingzeng prosecution. Engage China-licensed counsel before any boots-on-ground move.
- **BVI / Cayman / Bahamas**: shell concentration; verify substance, not just registration
- **East Africa**: KE BRS, UG URSB, TZ BRELA, RW RDB — see `tools/dd/registry_atlas.py`
- **MENA**: registry searches often only return local-language form; transliterate company names into Arabic before re-querying

## Anti-patterns

- Treating registration jurisdiction = operating jurisdiction
- Stopping at the first parent (walk to root)
- Ignoring shared-officer / shared-address signals — that's where shell rings hide
- Using only WHOIS — registries also matter
- Missing the foreign-extension hint on company-name alone

## Sources

- `tools/dd/ubo.py` — graph walker
- `tools/dd/foreign_extensions.py` — name-suffix → jurisdiction
- `tools/dd/registry_atlas.py` — per-country registries (UK, US, KE, UG, TZ, RW, ZA, NG, FR, DE, SG, HK, BVI, KY, ...)
- `tools/registry/` — registry-specific adapters (Companies House, EDGAR, ...) — roadmap

## See also

- `due-diligence-framework`
- `due-diligence-report-architecture` — feeds the corporate body sections
- `sanctions-pep-screening` — apply to every entity in the graph
- `adverse-media-investigation` — apply to every entity in the graph
