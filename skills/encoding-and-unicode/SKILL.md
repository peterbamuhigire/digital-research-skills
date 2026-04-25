---
name: encoding-and-unicode
description: Use whenever a text file enters the engine — detect charset, strip BOM, repair mojibake, write canonical UTF-8. Walker's gap closed via charset-normalizer + ftfy. Backed by tools/data/encoding_repair.py.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Encoding and Unicode

Walker's *Python Data Cleaning Cookbook* notes encoding only in passing. Modern web-scraped data is full of:

- BOM-prefixed CSV column headers (`﻿` in `﻿name`)
- Latin-1 mis-decoded as UTF-8 (mojibake — `Ã©` for `é`)
- Mixed encodings within one file
- `chardet`'s outdated detection

This skill makes the engine charset-safe at the boundary.

## The pipeline

```
raw bytes  →  charset-normalizer detect  →  decode  →  strip BOM  →  ftfy fix mojibake  →  UTF-8 output
```

```python
from tools.data import repair_encoding

report = repair_encoding(
    "messy.csv",
    output_path="clean.csv",  # optional; in-place if None (with .bak backup)
    fix_mojibake=True,
)

print(report.detected_encoding)    # e.g. "windows-1252"
print(report.confidence)            # 0.0-1.0
print(report.bom_stripped)
print(report.mojibake_fixes)        # number of characters fixed
```

## Common patterns

### Detect-then-decide
```python
from charset_normalizer import from_path
results = from_path("file.csv").best()
if results.encoding != "utf-8":
    # log the discovery; convert
    ...
```

### Mojibake fix at column level
```python
import ftfy
df["name"] = df["name"].apply(lambda s: ftfy.fix_text(s) if isinstance(s, str) else s)
```

### BOM-aware read
```python
df = pd.read_csv("file.csv", encoding="utf-8-sig")  # strips BOM if present
```

## Decision rules

- **Run `repair_encoding` first**, then `pd.read_csv` on the clean file
- **Prefer `charset-normalizer` over legacy `chardet`** (faster, MIT, more accurate)
- **Always backup** before in-place repair (`.bak` file)
- **Log the detected encoding** in the cleaning manifest
- **Default to UTF-8 on output** — the engine's canonical form

## Anti-patterns

- Trusting `pd.read_csv`'s auto-detection
- Suppressing `UnicodeDecodeError` with `errors='replace'` and shipping
- Mixing encodings within a single project's data tree
- Treating mojibake as "weird characters" rather than fixable
- Forgetting BOMs (silent first-column-name corruption)

## See also

- `tools/data/encoding_repair.py` — implementation
- `data-cleaning-pandas` — encoding repair is step 1
- `data-quality-assessment` — encoding issues lower validity score
