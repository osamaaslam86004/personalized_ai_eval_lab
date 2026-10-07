from typing import Literal
from pydantic import BaseModel, ConfigDict, Field

SupportType = Literal["EXPLICIT","SYNTHESIZED","INFERRED","IRRELEVANT","CONTRADICTED","UNSUPPORTED"]

class Scores(BaseModel):
    model_config = ConfigDict(extra="forbid")
    grounding: int = Field(ge=1, le=5)
    integration: int = Field(ge=1, le=5)
    helpfulness: int = Field(ge=1, le=5)
    personalization_relevance: int = Field(ge=1, le=5)

class Flags(BaseModel):
    model_config = ConfigDict(extra="forbid")
    forced_personalization: bool
    unsupported_inference: bool

class ClaimEvaluation(BaseModel):
    model_config = ConfigDict(extra="forbid")
    claim_id: str = Field(min_length=1)
    text: str = Field(min_length=1)
    evidence_ids: list[str]
    support_type: SupportType
    support_score: int = Field(ge=1, le=5)

class JudgeOutput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    case_id: str = Field(min_length=1)
    scores: Scores
    flags: Flags
    claim_evaluations: list[ClaimEvaluation]
    rationale: str = Field(min_length=1)

def validate_judge_output(payload: dict, expected_case_id: str, valid_evidence_ids: set[str]) -> JudgeOutput:
    result = JudgeOutput.model_validate(payload)
    if result.case_id != expected_case_id:
        raise ValueError(f"case_id mismatch: expected {expected_case_id}, got {result.case_id}")
    claim_ids = [c.claim_id for c in result.claim_evaluations]
    if len(claim_ids) != len(set(claim_ids)):
        raise ValueError("claim_id values must be unique")
    unknown = sorted({e for c in result.claim_evaluations for e in c.evidence_ids if e not in valid_evidence_ids})
    if unknown:
        raise ValueError(f"unknown evidence IDs: {unknown}")
    return result
