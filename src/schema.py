from dataclasses import dataclass, field
from typing import Literal


@dataclass
class Evaluation:
    case_id: str
    grounding: int
    integration: int
    helpfulness: int
    personalization_relevance: int
    forced_personalization: bool
    unsupported_inference: bool
    winner: Literal["A", "B", "Tie"]
    evidence_refs: list[str] = field(default_factory=list)
    rationale: str = ""

    def validate(self) -> None:
        for name in (
            "grounding",
            "integration",
            "helpfulness",
            "personalization_relevance",
        ):
            value = getattr(self, name)
            if value < 1 or value > 5:
                raise ValueError(f"{name} must be between 1 and 5")
        if self.winner not in {"A", "B", "Tie"}:
            raise ValueError("winner must be A, B, or Tie")
        if len(self.rationale.strip()) < 20:
            raise ValueError("rationale is too short to be defensible")
