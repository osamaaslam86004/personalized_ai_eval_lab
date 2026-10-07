# Stage 5 Judge Specification

## Input
```json
{"case_id":"PERS-XXX","context":[{"id":"C1","text":"..."}],"request":"...","candidate_response":"..."}
```

## Output
```json
{"case_id":"PERS-XXX","scores":{"grounding":1,"integration":1,"helpfulness":1,"personalization_relevance":1},"flags":{"forced_personalization":false,"unsupported_inference":false},"claim_evaluations":[{"claim_id":"CLM-1","text":"...","evidence_ids":["C1"],"support_type":"EXPLICIT","support_score":5}],"rationale":"..."}
```

Allowed support types: EXPLICIT, SYNTHESIZED, INFERRED, IRRELEVANT, CONTRADICTED, UNSUPPORTED.

Deterministic constraints: scores 1–5; support_score 1–5; evidence IDs resolve; case_id matches; claim IDs unique; rationale non-empty; flags boolean; no extra top-level fields.

`INFERRED` means a plausible conclusion from evidence that is not directly stated. `UNSUPPORTED` means insufficient evidence. A plausible inference can still trigger `unsupported_inference=true` when presented as fact or preference.

Provider independent: the contract works with cloud or local models.
