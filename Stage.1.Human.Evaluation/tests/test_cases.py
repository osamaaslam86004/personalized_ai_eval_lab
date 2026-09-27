import json
from pathlib import Path


CASES = Path(__file__).parents[1] / "datasets" / "stage1_cases.json"


def test_stage1_cases_are_well_formed():
    cases = json.loads(CASES.read_text())
    assert len(cases) == 5
    for case in cases:
        for key in ("case_id", "user_context", "conversation", "response_a", "response_b"):
            assert key in case
        assert case["response_a"] != case["response_b"]
        assert case["user_context"]
