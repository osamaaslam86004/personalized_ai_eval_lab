from dataclasses import dataclass
from typing import Literal

EvidenceLabel = Literal["EXPLICIT","SYNTHESIZED","INFERRED","IRRELEVANT","CONTRADICTED","UNSUPPORTED"]

@dataclass(frozen=True)
class ClaimRecord:
    claim_id: str
    claim: str
    evidence_ids: tuple[str, ...]
    label: EvidenceLabel
    score: int

def validate_claim(claim: ClaimRecord, context_ids: set[str]) -> list[str]:
    errors = []
    if not claim.claim_id: errors.append("missing claim_id")
    if not claim.claim: errors.append("missing claim")
    if claim.label not in {"EXPLICIT","SYNTHESIZED","INFERRED","IRRELEVANT","CONTRADICTED","UNSUPPORTED"}:
        errors.append("invalid evidence label")
    if not isinstance(claim.score, int) or not 1 <= claim.score <= 5:
        errors.append("score must be an integer from 1 to 5")
    for eid in claim.evidence_ids:
        if eid not in context_ids: errors.append(f"unknown evidence id: {eid}")
    return errors
