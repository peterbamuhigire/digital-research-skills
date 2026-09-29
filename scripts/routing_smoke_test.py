#!/usr/bin/env python3
"""Run lexical top-three routing checks against active skill contracts.

Lexical proxy; not live routing (see addyosmani/agent-skills issue #620).

M10-03 additions:
- precision@1 and precision@3 are printed; ``--min-rank1 <pct>`` fails below the ratchet floor;
- owned negatives (top-level ``negatives`` in the fixture file): the negative's skill must not rank
  first with a non-zero score, and its ``owner`` must rank strictly above it with a non-zero score.
  An owner written ``<engine-id>/<skill>`` is NOT_ASSESSED here and is evaluated in union mode by
  chwezi-engine-agents. Owner-outranks-self rule adapted from addyosmani/agent-skills (MIT,
  https://github.com/addyosmani/agent-skills, commit 2686b62), ``scripts/run-evals.js``; paraphrased;
- ``--lint-fixtures``: a prompt must not contain its expected slug as a phrase, and its word-trigram
  overlap with the expected description must stay below 0.6.
"""

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
    parser.add_argument("--min-rank1", type=float, default=None, help="Fail when precision@1 (percent) is below this floor.")
    parser.add_argument("--lint-fixtures", action="store_true", help="Fail on slug-bearing or description-copying prompts.")
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


def read_descriptions() -> dict[str, str]:
    descriptions: dict[str, str] = {}
    for path in sorted((ROOT / "skills").rglob("SKILL.md")):
        if EXCLUDED in path.resolve().parents:
            continue
        raw = path.read_text(encoding="utf-8", errors="replace")
        match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?", raw, re.S)
        if match:
            frontmatter = yaml.safe_load(match.group(1)) or {}
            descriptions[str(frontmatter.get("name", path.parent.name))] = str(frontmatter.get("description", ""))
    return descriptions


def check_negative(negative: dict, catalogue: dict[str, Counter[str]]) -> tuple[str, str]:
    """Return (status, message); status is PASS, FAIL or NOT_ASSESSED."""
    skill, owner = negative["skill"], negative.get("owner")
    if owner and "/" in owner:
        return "NOT_ASSESSED", f"cross-engine owner {owner} is checked in union mode"
    if skill not in catalogue:
        return "FAIL", f"negative skill {skill} is not active"
    ranking = rank(negative["prompt"], catalogue)
    order = [name for name, _ in ranking]
    scores = dict(ranking)
    if order[0] == skill and scores[skill] > 0:
        return "FAIL", f"{skill} ranks first ({scores[skill]:.2f})"
    if not owner:
        return "PASS", "skill is not rank 1"
    if owner not in catalogue:
        return "FAIL", f"owner {owner} is not active"
    if scores[owner] <= 0 or order.index(owner) >= order.index(skill):
        return "FAIL", f"owner {owner} (rank {order.index(owner) + 1}) does not outrank {skill} (rank {order.index(skill) + 1})"
    return "PASS", "owner outranks skill"


def _normalise(text: str) -> str:
    return " " + re.sub(r"[^a-z0-9]+", " ", text.lower()).strip() + " "


def _trigrams(text: str) -> set[tuple[str, ...]]:
    words = re.findall(r"[a-z0-9]+", text.lower())
    return {tuple(words[index : index + 3]) for index in range(len(words) - 2)}


def lint_prompt(prompt: str, slug: str, description: str, limit: float = 0.6) -> list[str]:
    findings = []
    phrase = re.sub(r"^\d+-", "", slug.lower()).replace("-", " ").strip()
    if phrase and f" {phrase} " in _normalise(prompt):
        findings.append(f"slug-in-prompt '{phrase}'")
    grams = _trigrams(prompt)
    if grams:
        overlap = len(grams & _trigrams(description)) / len(grams)
        if overlap >= limit:
            findings.append(f"description-copy trigram overlap {overlap:.2f}")
    return findings


def main() -> int:
    args = parse_args()
    fixture_path = args.fixtures if args.fixtures.is_absolute() else ROOT / args.fixtures
    fixture_data = json.loads(fixture_path.read_text(encoding="utf-8"))
    catalogue = read_catalogue()
    top_k = int(fixture_data.get("top_k", 3))
    threshold = float(fixture_data.get("threshold", 1.0))
    results = []
    rank1 = 0
    for fixture in fixture_data["fixtures"]:
        ranking = rank(fixture["prompt"], catalogue)
        top = [name for name, _ in ranking[:top_k]]
        rank1 += ranking[0][0] == fixture["expected"]
        expected_pass = fixture["expected"] in top
        forbidden_at_one = bool(fixture.get("forbidden")) and ranking[0][0] in fixture["forbidden"]
        passed = expected_pass and not forbidden_at_one
        results.append({"id": fixture["id"], "passed": passed, "expected": fixture["expected"], "top": ranking[:top_k]})
    passed_count = sum(item["passed"] for item in results)
    total = len(results)
    precision = passed_count / total if total else 0.0
    p_at_1 = 100.0 * rank1 / total if total else 0.0
    p_at_3 = 100.0 * sum(item["expected"] in [name for name, _ in item["top"]] for item in results) / total if total else 0.0
    print(f"routing-smoke-test: {passed_count}/{total} top-{top_k} precision={precision:.3f} threshold={threshold:.3f} (lexical proxy; not live routing)")
    print(f"- precision@1: {rank1}/{total} ({p_at_1:.1f}%)")
    print(f"- precision@3: {p_at_3:.1f}%")
    extra_failures: list[str] = []
    outcome: Counter[str] = Counter()
    negatives = fixture_data.get("negatives", [])
    for negative in negatives:
        status, message = check_negative(negative, catalogue)
        outcome[status] += 1
        if status == "FAIL":
            extra_failures.append(f"negative {negative.get('id', negative['skill'])}: {message}")
        elif status == "NOT_ASSESSED" and args.details:
            print(f"- NOT_ASSESSED negative {negative.get('id')}: {message}")
    owned = sum(1 for negative in negatives if negative.get("owner"))
    print(f"- owned negatives: {owned} (pass {outcome['PASS']}, fail {outcome['FAIL']}, not assessed {outcome['NOT_ASSESSED']})")
    if args.min_rank1 is not None:
        print(f"- rank-1 floor: {args.min_rank1:.1f}%")
        if p_at_1 < args.min_rank1:
            extra_failures.append(f"precision@1 {p_at_1:.1f}% is below the ratchet floor {args.min_rank1:.1f}%")
    if args.lint_fixtures:
        descriptions = read_descriptions()
        lint_findings = [
            f"{fixture['id']}: {finding}"
            for fixture in fixture_data["fixtures"]
            for finding in lint_prompt(fixture["prompt"], fixture["expected"], descriptions.get(fixture["expected"], ""))
        ]
        print(f"- fixture lint findings: {len(lint_findings)}")
        extra_failures.extend(f"lint {item}" for item in lint_findings)
    if args.details or precision < threshold:
        for result in results:
            marker = "PASS" if result["passed"] else "FAIL"
            print(f"- {marker} {result['id']}: expected={result['expected']} top={result['top']}")
    for failure in extra_failures:
        print(f"ERROR: {failure}")
    ok = precision >= threshold and all(item["passed"] for item in results) and not extra_failures
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
