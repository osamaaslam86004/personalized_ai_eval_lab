# Stage 4 — Evaluation Pipeline Rubric

## Purpose
Convert the human evaluation methodology into a reproducible pipeline.

Core flow:
**Dataset → Test Case → System Response → Evaluation Record → Validation → Metrics → Report**

### 1. Dataset integrity
5 = schema-valid, versioned, complete, stable IDs.
4 = minor metadata issue.
3 = usable but inconsistent.
2 = substantial ambiguity.
1 = cannot reliably execute.

### 2. Evaluation-record integrity
Every record should preserve case ID, dataset version, context, request, response, claims, evidence IDs, labels, scores, rationale, and metadata.

5 = complete and traceable.
4 = one minor omission.
3 = usable but loses some traceability.
2 = major fields missing.
1 = not auditable.

### 3. Deterministic validation
Use code for required fields, enums, score ranges, evidence IDs, unique IDs, rationale presence, and aggregation consistency.

### 4. Reproducibility
Record run ID, dataset version, pipeline version, timestamp, and evaluator/model configuration when applicable.

### 5. Failure handling
Explicitly represent invalid input, malformed output, missing evidence, schema violations, and runtime failures. Never silently turn failures into passing scores.

### 6. Reporting
Separate case-level results, aggregate metrics, validation errors, and run metadata.

## Stage 4 principle
**The pipeline preserves evaluation truth; it does not manufacture it.**
