import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from src.schema import ClaimRecord, validate_claim


def test_valid_claim():
    assert (
        validate_claim(
            ClaimRecord("C1", "You use FastAPI", ("C1",), "EXPLICIT", 5), {"C1"}
        )
        == []
    )


def test_unknown_evidence_is_rejected():
    c = ClaimRecord("C1", "You use FastAPI", ("C9",), "EXPLICIT", 5)
    assert "unknown evidence id: C9" in validate_claim(c, {"C1"})


def test_out_of_range_score_is_rejected():
    c = ClaimRecord("C1", "You use FastAPI", ("C1",), "EXPLICIT", 7)
    assert "score must be an integer from 1 to 5" in validate_claim(c, {"C1"})
