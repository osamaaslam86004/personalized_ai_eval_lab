import pytest
from pydantic import ValidationError
from src.schema import validate_judge_output

VALID={"case_id":"JUDGE-001","scores":{"grounding":5,"integration":5,"helpfulness":5,"personalization_relevance":5},"flags":{"forced_personalization":False,"unsupported_inference":False},"claim_evaluations":[{"claim_id":"CLM-1","text":"The user has FastAPI experience.","evidence_ids":["C1"],"support_type":"EXPLICIT","support_score":5}],"rationale":"The claim is directly supported by C1 and is relevant to the request."}

def test_valid_judge_output(): assert validate_judge_output(VALID,"JUDGE-001",{"C1","C2"}).case_id=="JUDGE-001"
def test_score_zero_is_rejected():
    with pytest.raises(ValidationError): validate_judge_output({**VALID,"scores":{**VALID["scores"],"grounding":0}},"JUDGE-001",{"C1"})
def test_score_above_five_is_rejected():
    with pytest.raises(ValidationError): validate_judge_output({**VALID,"scores":{**VALID["scores"],"helpfulness":6}},"JUDGE-001",{"C1"})
def test_unknown_evidence_id_is_rejected():
    with pytest.raises(ValueError,match="unknown evidence IDs"): validate_judge_output({**VALID,"claim_evaluations":[{**VALID["claim_evaluations"][0],"evidence_ids":["C99"]}]},"JUDGE-001",{"C1"})
def test_case_id_mismatch_is_rejected():
    with pytest.raises(ValueError,match="case_id mismatch"): validate_judge_output(VALID,"JUDGE-999",{"C1"})
def test_duplicate_claim_ids_are_rejected():
    with pytest.raises(ValueError,match="claim_id values must be unique"): validate_judge_output({**VALID,"claim_evaluations":[VALID["claim_evaluations"][0],VALID["claim_evaluations"][0]]},"JUDGE-001",{"C1"})
def test_extra_top_level_field_is_rejected():
    with pytest.raises(ValidationError): validate_judge_output({**VALID,"extra":"not allowed"},"JUDGE-001",{"C1"})
