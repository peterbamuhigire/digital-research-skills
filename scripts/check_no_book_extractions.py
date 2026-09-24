"""Fail if book-extraction folders exist or any text file links into one.

Book extractions, summaries and chapter notes must never be stored in this repository
(copyright). Knowledge enters only as paraphrased, task-oriented skill references.
Governance text may name the banned folders; it may not point at a file inside them.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANNED_DIRS = ("extracted-books", "book-extractions", "docs/book-study")
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "projects", "runs"}
TEXT_SUFFIXES = {".md", ".txt", ".yaml", ".yml", ".json", ".py", ".js", ".toml", ".html"}
# A path into a banned folder: folder name followed by "/" and at least one filename character.
LINK_RE = re.compile(r"(?<![\w-])(?:extracted-books|book-extractions|book-study)[/\\][\w.-]")
SELF = Path(__file__).resolve()


def candidate_files() -> list[Path]:
    """Tracked plus untracked-but-not-ignored files; falls back to a filtered walk."""
    try:
        out = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout
        return [ROOT / line for line in out.splitlines() if line]
    except (OSError, subprocess.CalledProcessError):
        return [
            p for p in ROOT.rglob("*")
            if not any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts)
        ]


def main() -> int:
    failures: list[str] = []
    for rel in BANNED_DIRS:
        if (ROOT / rel).exists():
            failures.append(f"banned folder exists: {rel}/")
    for path in candidate_files():
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES or path.resolve() == SELF:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            if LINK_RE.search(line):
                failures.append(f"{path.relative_to(ROOT).as_posix()}:{lineno}: links into a book-extraction folder")
    if failures:
        print("no-book-extractions: FAIL")
        for item in failures:
            print(" -", item)
        return 1
    print("no-book-extractions: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
