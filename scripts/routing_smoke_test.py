#!/usr/bin/env python3
"""Run lexical top-three routing checks against active skill contracts."""

from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURES = ROOT / "tests" / "skill-engine" / "routing-fixtures.json"
EXCLUDED = (ROOT / "skills" / "proposal-skills").resolve()
TOKEN_RE = re.compile(r"[a-z0-9]+")
STOP = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "in", "into", "is", "it",
    "of", "on", "or", "that", "the", "this", "to", "use", "when", "with", "without", "while",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixtures", type=Path, default=DEFAULT_FIXTURES)
    parser.add_argument("--details", action="store_true")
    return parser.parse_args()


def tokens(text: str) -> list[str]:
    values = []
    for token in TOKEN_RE.findall(text.casefold()):
        if token in STOP or len(token) < 3:
            continue
        for suffix in ("isation", "ization", "ments", "ment", "ings", "ing", "ies", "ed", "s"):
            if token.endswith(suffix) and len(token) - len(suffix) >= 4:
                token = token[: -len(suffix)]
                break
        values.append(token)
    return values


def read_catalogue() -> dict[str, Counter[str]]:
    catalogue: dict[str, Counter[str]] = {}
    for path in sorted((ROOT / "skills").rglob("SKILL.md")):
        if EXCLUDED in path.resolve().parents:
            continue
        raw = path.read_text(encoding="utf-8", errors="replace")
        match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?", raw, re.S)
        if not match:
            continue
        frontmatter = yaml.safe_load(match.group(1)) or {}
        name = frontmatter.get("name", path.parent.name)
        body = raw[match.end() :]
        use_match = re.search(r"^##\s+Use When\s*$([\s\S]*?)(?=^##\s|\Z)", body, re.M | re.I)
        use_when = use_match.group(1) if use_match else ""
        title = re.search(r"^#\s+(.+)$", body, re.M)
        weighted = Counter(tokens(str(frontmatter.get("description", ""))))
        weighted.update({key: value * 2 for key, value in Counter(tokens(use_when)).items()})
        weighted.update({key: value * 3 for key, value in Counter(tokens(name.replace("-", " "))).items()})
        if title:
            weighted.update({key: value * 2 for key, value in Counter(tokens(title.group(1))).items()})
        catalogue[name] = weighted
    return catalogue


def rank(prompt: str, catalogue: dict[str, Counter[str]]) -> list[tuple[str, float]]:
    query = Counter(tokens(prompt))
    document_frequency = Counter()
    for term in query:
        document_frequency[term] = sum(term in document for document in catalogue.values())
    scored = []
    for name, document in catalogue.items():
        score = 0.0
        for term, query_count in query.items():
            if term not in document:
                continue
            inverse = math.log((len(catalogue) + 1) / (document_frequency[term] + 1)) + 1
            score += query_count * document[term] * inverse
        scored.append((name, round(score, 4)))
    return sorted(scored, key=lambda item: (-item[1], item[0]))


def main() -> int:
    args = parse_args()
    fixture_path = args.fixtures if args.fixtures.is_absolute() else ROOT / args.fixtures
    fixture_data = json.loads(fixture_path.read_text(encoding="utf-8"))
    catalogue = read_catalogue()
    top_k = int(fixture_data.get("top_k", 3))
    threshold = float(fixture_data.get("threshold", 1.0))
    results = []
    for fixture in fixture_data["fixtures"]:
        ranking = rank(fixture["prompt"], catalogue)
        top = [name for name, _ in ranking[:top_k]]
        expected_pass = fixture["expected"] in top
        forbidden_at_one = bool(fixture.get("forbidden")) and ranking[0][0] in fixture["forbidden"]
        passed = expected_pass and not forbidden_at_one
        results.append({"id": fixture["id"], "passed": passed, "expected": fixture["expected"], "top": ranking[:top_k]})
    passed_count = sum(item["passed"] for item in results)
    precision = passed_count / len(results) if results else 0.0
    print(f"routing-smoke-test: {passed_count}/{len(results)} top-{top_k} precision={precision:.3f} threshold={threshold:.3f}")
    if args.details or precision < threshold:
        for result in results:
            marker = "PASS" if result["passed"] else "FAIL"
            print(f"- {marker} {result['id']}: expected={result['expected']} top={result['top']}")
    return 0 if precision >= threshold and all(item["passed"] for item in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
