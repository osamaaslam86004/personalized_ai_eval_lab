# Personalized AI Evaluation Lab

Purpose: prepare for an AI Quality Analyst (Personalization) role by practicing grounded, evidence-based evaluation of personalized responses.

## Stage 1 goal
Build human evaluation skill before automating evaluation.

Core dimensions:
- Grounding
- Integration
- Helpfulness
- Personalization relevance
- Forced personalization
- Unsupported inference
- Side-by-side (SxS) comparison
- Defensible rationale with evidence references

## Hardware strategy
Primary: local CPU-only environment, designed to work without AVX and with 8 GB RAM.
Secondary: Google Colab Free for occasional larger/batch experiments. Do not make Colab a dependency.

## Stage 1 workflow
1. Read a user context and conversation.
2. Inspect Response A and Response B.
3. Trace every personalized claim back to evidence.
4. Score Grounding, Integration, Helpfulness, and Relevance from 1-5.
5. Mark forced personalization and unsupported inference.
6. Select A, B, or Tie.
7. Write a 2-4 sentence evidence-based rationale.

## Files
- `rubric/personalization_rubric.md`: annotation rubric
- `datasets/stage1_cases.json`: calibration cases
- `src/schema.py`: Pydantic-compatible annotation schema
- `tests/test_cases.py`: basic dataset validation
- `reports/`: place evaluation reports here
