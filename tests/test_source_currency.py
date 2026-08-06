import json
from datetime import date
from pathlib import Path

from scripts.validate_source_currency import validate_manifest


ROOT = Path(__file__).resolve().parents[1]


def test_source_currency_fixture_passes():
    path = ROOT / "tests" / "fixtures" / "source-currency.json"
    assert validate_manifest(path, date(2026, 8, 6)) == []


def test_overdue_current_source_blocks():
    path = ROOT / "tests" / "fixtures" / "source-currency.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["sources"][0]["review_after"] = "2026-08-05"
    temp = ROOT / "tests" / "fixtures" / "source-currency-overdue.json"
    temp.write_text(json.dumps(data), encoding="utf-8")
    try:
        assert any("overdue" in item for item in validate_manifest(temp, date(2026, 8, 6)))
    finally:
        temp.unlink()
