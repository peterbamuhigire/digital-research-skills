# Jurisdictional registry atlas

For any country, the engine should know:
- Corporate registry (where to find companies)
- Securities regulator
- AML / FIU body
- Court records
- Sanctions issuer
- Professional licensing

```python
from tools.dd import registry_for_country

# Just corporate registry for Kenya
registry_for_country("KE", type_="corporate_registry")

# All registries for UK
registry_for_country("UK")
```

Coverage seed: UK, US, KE, UG, TZ, RW, ZA, NG, FR, DE, SG, HK, BVI, KY. Extend per project.

## Categories

| Type | What's there |
|---|---|
| `corporate_registry` | Companies, directors, beneficial ownership, filings |
| `securities` | Listed-company filings, broker registers |
| `aml_fiu` | Suspicious-transaction body, financial intelligence unit |
| `court` | Case law, dockets, judgments |
| `sanctions` | National-level sanctions issuer |
| `professional` | Licensing boards, disqualified-directors |

## East African coverage (relevant for the engine's existing focus)

| Country | Corporate | Securities | Court | AML/FIU |
|---|---|---|---|---|
| Kenya | BRS | CMA | Kenya Law | EACC |
| Uganda | URSB | CMA | ULII | FIA |
| Tanzania | BRELA | CMSA | TanzLII | FIU |
| Rwanda | RDB | CMA | RwandaLII | FIC |

## Shell-haven flagging

Entries in BVI, KY, BS, IM, JE, GG carry a `notes` field: "High shell-company concentration; verify substance." When `corporate-veil-investigation` walks an ownership graph, any entity registered in a flagged jurisdiction is highlighted.

## Refresh + extension

The atlas is a code constant — extend `tools/dd/registry_atlas.py` REGISTRY_ATLAS dict per project.

## See also

- `tools/dd/registry_atlas.py` — the data
- `corporate-veil-investigation` — uses the atlas for UBO walks
- `due-diligence-framework` — DD methodology
- `regulatory-landscape-mapping` — broader regulatory context
