"""M10-03 tests: owned negatives, rank-1 ratchet and fixture lint for the research routing smoke test."""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "routing_smoke_test.py"
SPEC = importlib.util.spec_from_file_location("dre_routing", SCRIPT)
ROUTING = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ROUTING)
FIXTURES = ROOT / "tests" / "skill-engine" / "routing-fixtures.json"


def _run(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, "-X", "utf8", str(SCRIPT), *args], capture_output=True, text=True, encoding="utf-8")


def test_live_fixtures_pass_with_floor_and_lint():
    result = _run("--min-rank1", "84", "--lint-fixtures")
    assert result.returncode == 0, result.stdout
    assert "owned negatives:" in result.stdout


def test_floor_above_measured_fails():
    result = _run("--min-rank1", "100")
    assert result.returncode == 1
    assert "below the ratchet floor" in result.stdout


def test_owner_ranked_below_self_fails(tmp_path):
    data = json.loads(FIXTURES.read_text(encoding="utf-8"))
    data["negatives"] = [{"id": "seeded", "skill": "anti-ai-slop", "prompt": "Apply live anti-slop controls while I write the human-facing research deliverable.", "owner": "ai-slop-audit"}]
    path = tmp_path / "fixtures.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    result = _run("--fixtures", str(path))
    assert result.returncode == 1
    assert "negative seeded" in result.stdout


def test_cross_engine_owner_is_not_assessed():
    status, _ = ROUTING.check_negative({"skill": "validation-contract", "prompt": "Prepare the release evidence bundle", "owner": "chwezi-dev-engine/validation-contract"}, ROUTING.read_catalogue())
    assert status == "NOT_ASSESSED"


def test_lint_detects_slug_and_description_copy():
    assert ROUTING.lint_prompt("Run the due diligence now", "due-diligence", "")
    assert ROUTING.lint_prompt("Use 02-primary-research here", "02-primary-research", "")
    assert ROUTING.lint_prompt("profiling cleaning merging data", "x", "Use when profiling cleaning merging data")
    assert ROUTING.lint_prompt("Check who really owns the target", "due-diligence", "Use when conducting due diligence") == []
