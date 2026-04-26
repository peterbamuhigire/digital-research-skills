# Evidence custody discipline

McMahon: every PI / investigator must maintain a court-ready chain of custody for any item that may be used as evidence. Without it, the evidence is inadmissible regardless of probative value.

## Six-step evidence procedure

| Step | Action |
|---|---|
| 1. **Protect** | Secure scene; prevent contamination |
| 2. **Collect** | Use gloves; minimise handling; photograph in situ first |
| 3. **Identify** | Mark solid objects ≥1 cubic inch with investigator's initials |
| 4. **Preserve** | Sealed container with case#, date, time, name, location, signature, witness names |
| 5. **Transmit** | Logged transfer with from/to/date/time/signature |
| 6. **Dispose** | Logged final destination (court, return to owner, destruction) |

## Three-factor admissibility test

For physical evidence to be admissible:

1. **Properly identified** — investigator can point to it and say "this is the X I collected at Y on Z"
2. **Chain-of-custody continuity proven** — every transfer documented; no gaps
3. **Competency proven** — material AND relevant to the case

## The chain-of-custody ledger

Every transfer logged with:
- Timestamp
- From party (name + role + signature)
- To party
- Location
- Purpose ("collection" | "transport" | "analysis" | "storage" | "court")
- Sealed container y/n + seal ID
- Notes

The engine's `tools.pi.ChainOfCustody` is **append-only** with hash-chained entries to prevent post-hoc tampering.

## Standard usage

```python
from tools.pi import ChainOfCustody, CustodyTransfer
from datetime import datetime

coc = ChainOfCustody(
    case_id="2026-001",
    evidence_id="EV-001",
    description="USB drive seized from suspect's vehicle",
    collected_at=datetime(2026, 4, 25, 10, 30),
    collected_by="Investigator Smith #C-1234",
    collected_location="2300 Main St parking lot",
)

# Each transfer is logged
coc.append(CustodyTransfer(
    timestamp=datetime(2026, 4, 25, 11, 15),
    from_party="Investigator Smith #C-1234",
    to_party="Forensic lab — analyst Jones #L-5678",
    location="ABC Forensics, 100 Lab Way",
    purpose="analysis",
    sealed_container=True,
    seal_id="SEAL-2026-04-25-001",
))

# Court-ready affidavit
coc.to_affidavit("custody-affidavit-EV-001.docx")

# Verify integrity
assert coc.verify_integrity()
```

## Anti-patterns

- "We always do it that way" — undocumented practice = inadmissible
- Single-investigator collection without witness
- Transfers without sealed container
- Marking too-small objects (use sealed container instead)
- Gaps in the ledger (any unaccounted period invalidates the chain)
- Post-hoc edits to the ledger (use append-only)
- Missing investigator signatures
- No witness names on the seal

## Marking conventions

- Solid objects ≥1 cubic inch: investigator's initials directly on the item
- Smaller items / liquids / documents: sealed container with the markings
- Container markings (mandatory): case#, date, time, investigator name, location, signature, witness names

## See also

- `tools/pi/chain_of_custody.py` — implementation
- `pi-report-writing` — chain-of-custody affidavit goes in as exhibit
- `court-testimony-preparation` — how to introduce evidence on the stand
- `evidence-discipline` — engine-wide rule above this one
