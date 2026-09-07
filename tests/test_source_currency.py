import json
import copy
import subprocess
import sys
from datetime import date
from pathlib import Path

import pytest

from scripts.validate_source_currency import validate_manifest


ROOT = Path(__file__).resolve().parents[1]


def test_source_currency_fixture_passes():
    path = ROOT / "tests" / "fixtures" / "source-currency.json"
    assert validate_manifest(path, date(2026, 8, 6)) == []


def test_overdue_current_source_blocks(tmp_path):
    path = ROOT / "tests" / "fixtures" / "source-currency.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["sources"][0]["review_after"] = "2026-08-05"
    temp = tmp_path / "source-currency-overdue.json"
    temp.write_text(json.dumps(data), encoding="utf-8")
    assert any("overdue" in item for item in validate_manifest(temp, date(2026, 8, 6)))


@pytest.fixture
def manifest():
    return json.loads((ROOT / 'tests/fixtures/source-currency.json').read_text(encoding='utf-8'))


def check(tmp_path, data):
    path = tmp_path / 'manifest.json'
    path.write_text(json.dumps(data), encoding='utf-8')
    return validate_manifest(path, date(2026, 8, 6))


@pytest.mark.parametrize('root', [None, [], '', 1, True])
def test_nonobject_roots_fail(tmp_path, root):
    assert check(tmp_path, root) == ['manifest must be an object']


@pytest.mark.parametrize('value', [None, {}, '', 1, True])
@pytest.mark.parametrize('field', ['sources', 'claims'])
def test_collections_require_lists(tmp_path, manifest, field, value):
    manifest[field] = value
    assert any(f'{field} must be a' in item for item in check(tmp_path, manifest))


def test_empty_or_missing_sources_fail(tmp_path):
    for data in ({}, {'sources': []}):
        assert check(tmp_path, data) == ['sources must be a nonempty list']


@pytest.mark.parametrize('collection', ['sources', 'claims'])
@pytest.mark.parametrize('row', [None, [], 'text', 1, True])
def test_collection_rows_require_objects(tmp_path, manifest, collection, row):
    manifest[collection] = [row]
    assert any('entries must be objects' in item for item in check(tmp_path, manifest))


@pytest.mark.parametrize('collection', ['sources', 'claims'])
@pytest.mark.parametrize('value', [None, '', ' \t', 1, True, [], {}])
def test_identifiers_are_nonempty_strings(tmp_path, manifest, collection, value):
    manifest[collection][0]['id'] = value
    assert any('id must be a nonempty string' in item for item in check(tmp_path, manifest))


@pytest.mark.parametrize('collection', ['sources', 'claims'])
def test_missing_and_duplicate_identifiers_fail(tmp_path, manifest, collection):
    duplicate = copy.deepcopy(manifest[collection][0])
    manifest[collection].append(duplicate)
    assert any('duplicate' in item for item in check(tmp_path, manifest))
    manifest[collection].pop()
    del manifest[collection][0]['id']
    assert any('id must be a nonempty string' in item for item in check(tmp_path, manifest))


@pytest.mark.parametrize('value', [None, '', 'false', 0, 1, [], {}])
def test_currentness_flag_requires_boolean(tmp_path, manifest, value):
    manifest['claims'][0]['requires_currentness'] = value
    assert any('must be boolean' in item for item in check(tmp_path, manifest))


@pytest.mark.parametrize('field', ['requires_currentness', 'source_ids'])
def test_missing_claim_fields_fail(tmp_path, manifest, field):
    del manifest['claims'][0][field]
    assert any(field in item for item in check(tmp_path, manifest))


@pytest.mark.parametrize('value', [None, '', 'src-current-001', {}, True, 1])
def test_claim_source_ids_require_list(tmp_path, manifest, value):
    manifest['claims'][0]['source_ids'] = value
    assert any('source_ids must be a list' in item for item in check(tmp_path, manifest))


@pytest.mark.parametrize('value', [None, '', ' ', True, 1, [], {}])
def test_claim_source_ids_are_typed(tmp_path, manifest, value):
    manifest['claims'][0]['source_ids'] = [value]
    assert any('entries must be nonempty strings' in item for item in check(tmp_path, manifest))


def test_claim_sources_are_nonempty_known_and_unique(tmp_path, manifest):
    for ids, expected in (([], 'nonempty source_ids'), (['missing'], 'unknown source'),
                          (['src-current-001'] * 2, 'duplicate source id')):
        manifest['claims'][0]['source_ids'] = ids
        assert any(expected in item for item in check(tmp_path, manifest))


def test_noncurrent_claims_still_validate_shape(tmp_path, manifest):
    manifest['claims'][0]['requires_currentness'] = False
    manifest['claims'][0]['source_ids'] = []
    assert check(tmp_path, manifest) == []
    manifest['claims'][0]['source_ids'] = 'bad'
    assert check(tmp_path, manifest)


def test_optional_empty_claims_pass(tmp_path, manifest):
    manifest['claims'] = []
    assert check(tmp_path, manifest) == []
    del manifest['claims']
    assert check(tmp_path, manifest) == []


@pytest.mark.parametrize('field', ['accessed', 'verified_at'])
def test_future_observation_dates_fail(tmp_path, manifest, field):
    manifest['sources'][0][field] = '2026-08-07'
    assert any(f'{field} is in the future' in item for item in check(tmp_path, manifest))


def test_equal_day_boundaries_pass(tmp_path, manifest):
    for field in ('accessed', 'verified_at', 'review_after'):
        manifest['sources'][0][field] = '2026-08-06'
    assert check(tmp_path, manifest) == []


@pytest.mark.parametrize('field,value,expected', [
    ('verified_at', '2026-07-31', 'precedes accessed'),
    ('review_after', '2026-08-01', 'precedes verified_at'),
    ('accessed', '2026-02-30', 'not ISO date'),
    ('verified_at', True, 'required as ISO date'),
    ('publication_date', 'invalid', 'not ISO date'),
    ('freshness_class', {}, 'unsupported freshness_class'),
    ('freshness_class', 'historical', 'not currentness-qualified'),
])
def test_existing_date_and_freshness_controls(tmp_path, manifest, field, value, expected):
    manifest['sources'][0][field] = value
    assert any(expected in item for item in check(tmp_path, manifest))


def test_current_source_requires_publication_metadata(tmp_path, manifest):
    del manifest['sources'][0]['publication_date']
    assert any('requires publication_date' in item for item in check(tmp_path, manifest))


def test_context_bound_source_requires_dated_scope(tmp_path, manifest):
    source = manifest['sources'][0]
    source['freshness_class'] = 'context-bound'
    source['scope'] = 'Synthetic catalogue taxonomy at the observed snapshot only.'
    source['as_of'] = '2026-08-01'
    del source['publication_date']
    assert check(tmp_path, manifest) == []
    del source['as_of']
    assert any('requires publication_date' in item for item in check(tmp_path, manifest))


@pytest.mark.parametrize('scope', [None, '', ' ', [], {}, True, 42])
def test_context_bound_source_rejects_missing_scope(tmp_path, manifest, scope):
    manifest['sources'][0].update(freshness_class='context-bound', scope=scope)
    assert any('context-bound source requires nonempty scope' in item
               for item in check(tmp_path, manifest))


def test_context_bound_source_cannot_bypass_review_window(tmp_path, manifest):
    manifest['sources'][0].update(freshness_class='context-bound', scope='Fixture only',
                                  review_after='2026-08-05')
    assert any('overdue' in item for item in check(tmp_path, manifest))


@pytest.mark.parametrize('payload', [b'\xff', b'{invalid json'])
def test_encoding_and_json_fail_cleanly(tmp_path, payload):
    path = tmp_path / 'invalid.json'
    path.write_bytes(payload)
    assert validate_manifest(path)[0].startswith('cannot read manifest:')
    result = subprocess.run([sys.executable, '-B', '-X', 'utf8',
                             str(ROOT / 'scripts/validate_source_currency.py'), str(path)],
                            capture_output=True, text=True, encoding='utf-8')
    assert result.returncode == 1
    assert '[FAIL] cannot read manifest:' in result.stdout
    assert 'Traceback' not in result.stderr


def test_missing_file_fails_cleanly(tmp_path):
    assert validate_manifest(tmp_path / 'missing.json')[0].startswith('cannot read manifest:')


def test_cli_pass_is_noncertifying_and_read_only(tmp_path, manifest):
    path = tmp_path / 'manifest.json'
    path.write_text(json.dumps(manifest), encoding='utf-8')
    before = path.read_bytes()
    result = subprocess.run([sys.executable, '-B', '-X', 'utf8',
                             str(ROOT / 'scripts/validate_source_currency.py'), str(path),
                             '--as-of', '2026-08-06'],
                            capture_output=True, text=True, encoding='utf-8')
    assert result.returncode == 0
    assert 'PASS: metadata/date checks only; claim support NOT ASSESSED' in result.stdout
    assert path.read_bytes() == before
