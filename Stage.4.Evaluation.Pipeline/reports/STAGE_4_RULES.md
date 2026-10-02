# Stage 4 — Evaluation Pipeline Rules

1. Keep data separate from evaluation logic.
2. Give every case a unique stable ID.
3. Preserve raw system and evaluator outputs.
4. Validate records before computing metrics.
5. Every evidence ID must resolve to context in the same case.
6. Keep deterministic checks deterministic.
7. Never silently repair invalid scores or labels.
8. Distinguish pipeline failure from poor model quality.
9. Preserve run metadata: run_id, dataset_version, pipeline_version, timestamp.
10. Produce machine-readable JSON before human-readable summaries.

### Pipeline
Dataset
↓
Schema Validation
↓
Evaluation Input
↓
System/Candidate Response
↓
Evaluation Record
↓
Deterministic Validation
↓
Metric Computation
↓
Run Report

### Exercise
Implement the supplied fixtures without LLM-as-judge:
1. load
2. validate
3. create/load candidate output
4. create evaluation record
5. validate
6. calculate metrics
7. write JSON
8. write aggregate report
