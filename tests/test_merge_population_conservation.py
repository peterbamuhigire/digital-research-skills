import pandas as pd

from tools.data.checkmerge import check_merge


def test_inner_join_reports_input_keys_discarded():
    merged, report = check_merge(
        pd.DataFrame({"id": [1, 2], "value": [10, 20]}),
        pd.DataFrame({"id": [1], "label": ["one"]}),
        on="id", how="inner", validate="one_to_one",
    )
    assert len(merged) == 1
    assert report.left_only == 0  # output indicator has no discarded row
    assert report.left_input_only == 1
    assert report.input_key_overlap == 1
    assert any("distinct left keys DROPPED" in w for w in report.warnings)


def test_left_join_can_pass_when_population_is_declared():
    _, report = check_merge(
        pd.DataFrame({"id": [1, 2]}),
        pd.DataFrame({"id": [1]}),
        on="id", how="left", validate="one_to_one",
    )
    assert report.left_input_only == 1
    assert report.right_input_only == 0
    assert report.passes(max_left_only_rate=1.0)
