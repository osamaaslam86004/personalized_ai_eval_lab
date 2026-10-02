# Personalized AI Evaluation Lab — Stage 4
## Evaluation Pipeline

Stage 4 turns Stages 1–3 into a reproducible, auditable evaluation pipeline.

Flow:
Dataset → Schema Validation → Evaluation Input → Candidate Response → Evaluation Record → Deterministic Validation → Metrics → Report

Contents:
- datasets/stage4_pipeline_cases.json
- rubric/stage4_evaluation_pipeline_rubric.md
- reports/STAGE_4_RULES.md
- reports/STAGE_4_WORKSHEET.md
- src/schema.py
- tests/test_schema.py

Do not implement LLM-as-judge yet. Stage 4 focuses on pipeline architecture, validation, traceability, and deterministic metrics.

Run:
`python -m pytest tests -q`
