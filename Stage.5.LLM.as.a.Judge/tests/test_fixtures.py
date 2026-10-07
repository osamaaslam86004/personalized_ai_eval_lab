import json
from pathlib import Path
from src.schema import validate_judge_output
ROOT=Path(__file__).resolve().parents[1]

def test_human_vs_judge_fixture_is_well_formed():
    data=json.loads((ROOT/"fixtures/human_vs_judge_fixtures.json").read_text())
    assert len(data["comparisons"])==5

def test_calibration_dataset_has_unique_case_ids():
    data=json.loads((ROOT/"datasets/stage5_judge_calibration.json").read_text())
    ids=[c["case_id"] for c in data["cases"]]
    assert len(ids)==len(set(ids))

def test_fixture_judge_records_pass_schema():
    data=json.loads((ROOT/"fixtures/human_vs_judge_fixtures.json").read_text())
    for item in data["comparisons"]:
        j=item["judge"]
        validate_judge_output({"case_id":item["case_id"],"scores":{k:j[k] for k in ["grounding","integration","helpfulness","personalization_relevance"]},"flags":{"forced_personalization":j["forced_personalization"],"unsupported_inference":j["unsupported_inference"]},"claim_evaluations":[],"rationale":"Fixture judge output used for deterministic comparison testing."},item["case_id"],set())
