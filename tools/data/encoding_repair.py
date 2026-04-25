"""Encoding repair — charset detection + mojibake fix + BOM strip.

Walker's gap closed: every text file the engine ingests passes through this
before pandas. Common failure modes: BOM in column header, latin-1
mis-decoded as UTF-8 producing 'Ã©' for 'é', mixed encodings within one file.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass(slots=True)
class RepairReport:
    detected_encoding: str
    confidence: float
    bom_stripped: bool
    mojibake_fixes: int
    final_encoding: str = "utf-8"


def repair_encoding(
    file_path: str | Path, *,
    output_path: Optional[str | Path] = None,
    fix_mojibake: bool = True,
) -> RepairReport:
    """Detect encoding, repair mojibake, write clean UTF-8.

    Lazy-imports charset-normalizer and ftfy.

    If output_path is None, overwrites in place after backup to .bak.
    """
    file_path = Path(file_path)
    raw = file_path.read_bytes()

    # 1. Detect encoding
    try:
        from charset_normalizer import from_bytes
        results = from_bytes(raw)
        if results:
            best = results.best()
            detected = best.encoding or "utf-8"
            confidence = float(best.chaos) if best.chaos is not None else 0.0
            confidence = 1.0 - min(confidence, 1.0)
        else:
            detected, confidence = "utf-8", 0.5
    except ImportError:
        detected, confidence = "utf-8", 0.5

    # 2. Decode
    try:
        text = raw.decode(detected)
    except (UnicodeDecodeError, LookupError):
        text = raw.decode("utf-8", errors="replace")

    # 3. BOM strip
    bom_stripped = False
    if text.startswith("﻿"):
        text = text.lstrip("﻿")
        bom_stripped = True

    # 4. Mojibake fix
    mojibake_fixes = 0
    if fix_mojibake:
        try:
            from ftfy import fix_text
            fixed = fix_text(text)
            mojibake_fixes = sum(1 for a, b in zip(text, fixed) if a != b)
            text = fixed
        except ImportError:
            pass

    # 5. Write clean UTF-8
    if output_path is None:
        output_path = file_path
        # Backup original
        backup = file_path.with_suffix(file_path.suffix + ".bak")
        if not backup.exists():
            backup.write_bytes(raw)
    output_path = Path(output_path)
    output_path.write_text(text, encoding="utf-8")

    return RepairReport(
        detected_encoding=detected,
        confidence=confidence,
        bom_stripped=bom_stripped,
        mojibake_fixes=mojibake_fixes,
        final_encoding="utf-8",
    )
