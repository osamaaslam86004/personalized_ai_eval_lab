# Stage 4 — Evaluation Pipeline Worksheet

For each PIPE case:

### Input validation
- [ ] Case ID valid
- [ ] Context present
- [ ] Request present
- [ ] Candidate response present

### Evaluation record
- [ ] Claims extracted
- [ ] Evidence IDs recorded
- [ ] Labels valid
- [ ] Scores 1–5
- [ ] Coverage recorded
- [ ] Rationale recorded

### Deterministic validation
- [ ] Evidence IDs resolve
- [ ] Case IDs unique
- [ ] Labels valid
- [ ] Scores in range
- [ ] Required fields present

### Run metadata
- [ ] run_id
- [ ] dataset_version
- [ ] pipeline_version
- [ ] timestamp

### Outputs
- [ ] JSON records
- [ ] Aggregate metrics
- [ ] Validation errors
- [ ] Human-readable report

A pipeline failure must never silently become a model-quality score.
