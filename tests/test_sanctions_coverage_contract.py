import json

from tools.sanctions.screen import screen_name


def test_empty_cache_is_failed_not_clean_no_hit(tmp_path):
    result = screen_name("SYNTHETIC SUBJECT", cache_dir=tmp_path)
    assert result.total_hits == 0
    assert result.coverage_state == "failed"
    assert result.sources_attempted == 0
    assert result.source_errors


def test_valid_empty_source_is_complete_no_hit(tmp_path):
    (tmp_path / "empty.json").write_text("[]", encoding="utf-8")
    result = screen_name("SYNTHETIC SUBJECT", cache_dir=tmp_path)
    assert result.total_hits == 0
    assert result.coverage_state == "complete"
    assert result.sources_loaded == 1
    assert result.source_errors == []


def test_corrupt_source_is_failed_and_preserves_error(tmp_path):
    (tmp_path / "broken.json").write_text("{not-json", encoding="utf-8")
    result = screen_name("SYNTHETIC SUBJECT", cache_dir=tmp_path)
    assert result.coverage_state == "failed"
    assert result.total_hits == 0
    assert "broken.json" in result.source_errors[0]


def test_mixed_sources_are_partial(tmp_path):
    (tmp_path / "valid.json").write_text(json.dumps([{"name": "OTHER"}]), encoding="utf-8")
    (tmp_path / "broken.json").write_text("not-json", encoding="utf-8")
    result = screen_name("SYNTHETIC SUBJECT", cache_dir=tmp_path)
    assert result.coverage_state == "partial"
    assert result.sources_attempted == 2
    assert result.sources_loaded == 1
