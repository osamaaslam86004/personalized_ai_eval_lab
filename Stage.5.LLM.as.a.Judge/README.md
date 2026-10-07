# Personalized AI Evaluation Lab — Stage 5: LLM-as-a-Judge

Stage 5 introduces an automated evaluator for personalized AI responses while preserving the discipline established in Stages 1–4.

## Goal
Build an LLM-as-a-Judge that evaluates Grounding, Integration, Helpfulness, Personalization Relevance, Forced Personalization, Unsupported Inference, and evidence coverage.

## Pipeline
```text
Evaluation Case → Candidate Response → LLM-as-a-Judge → Structured JSON → Deterministic Validation → Human Reference ↔ Judge → Agreement / Error Analysis
```

The LLM judge is an evaluator, not the source of truth. Human labels remain the reference standard in Stage 5. Stage 6 measures agreement statistically.

## Run tests
```bash
python -m pytest tests -q
```

## Workflow
1. Read `reports/STAGE_5_RULES.md`.
2. Read `rubric/stage5_llm_judge_rubric.md`.
3. Study `judge/judge_prompt.md` and `judge/judge_specification.md`.
4. Run deterministic tests.
5. Inspect human-vs-judge fixtures.
6. Replace fixture judge outputs with real model outputs.
7. Validate every real judge output before calculating agreement.
