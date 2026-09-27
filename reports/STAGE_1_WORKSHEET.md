# Stage 1 Calibration Worksheet

For each case, independently score Response A and Response B.

| Case | A Grounding | A Integration | A Helpfulness | A Relevance | B Grounding | B Integration | B Helpfulness | B Relevance | Forced? | Unsupported? | Winner |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| PERS-001 | 3 | 4 | 3 | 3 | 4 | 5 | 4 | 4 | false | false | B |
| PERS-002 | 4 | 4 | 2 | 4 | 2 | 1 | 2 | 1 | true | true | A |
| PERS-003 | 5 | 5 | 5 | 5 | 3 | 1 | 1 | 3 | true | false | A |
| PERS-004 | 5 | 5| 4 | 4 | 2 | 2 | 3| 4| false | true | A 
| PERS-005 | 2 | 4 | 2 | 4 | 5 | 5 | 5 | 5 | false | false | B |

## Rationale practice
Write 2-4 sentences per case. Reference context IDs such as C1/C2 and explain the concrete response behavior.

### "case_id": "PERS-001"
Response B is preferable because it effectively integrates relevant user context C1 and C2 into its recommendation. It uses C1 and C2 to deliver a tailored response, though it fails to incorporate C3. Response A misses context C1, C2, and C3 entirely, which negatively impacts its grounding, integration, and overall helpfulness.

### "case_id": "PERS-002"
Response A is preferable because it grounds its answer in context C1 and C2, providing a safer foundation despite omitting targeted framework-specific database indexing examples. Response B invents an unsupported preference by assuming the user prefers concise answers without sufficient evidence, which severely degrades its grounding, integration, helpfulness, and relevance scores

### "case_id": "PERS-003"
Response A is preferable because it naturally integrates context C2 to accurately answer the prompt. Response B overuses context by forcing C1 and C2 where unnecessary, creating an awkward and unnatural integration that harms both helpfulness and user experience.

### "case_id": "PERS-004"
Response A is preferable because it correctly applies user context C1 to deliver a tailored, grounded response. Response B invents an unsupported preference by assuming the user dislikes learning new systems, which degrades its grounding and helpfulness.

### "case_id": "PERS-005"
Response B is preferable because it fully integrates context C2 explicitly and C1 implicitly by correctly contextualizing Django as a Python-based server-side framework. Response A misses C1 and only partially incorporates C2, which reduces its grounding and helpfulness compared to Response B

## Calibration rule
Do not look at `gold_notes` until you have completed your independent judgments.
