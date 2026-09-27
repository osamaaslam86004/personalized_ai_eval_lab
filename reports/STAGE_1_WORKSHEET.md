# Stage 1 Calibration Worksheet

For each case, independently score Response A and Response B.

| Case | A Grounding | A Integration | A Helpfulness | A Relevance | B Grounding | B Integration | B Helpfulness | B Relevance | Forced? | Unsupported? | Winner |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| PERS-001 | 3 | 4 | 3 | 3 | 4 | 5 | 4 | 4 | false | false | B |
| PERS-002 | 4 | 4 | 2 | 4 | 0 | 0 | 0 | 0 | true | true | A |
| PERS-003 | 5 | 5 | 5 | 5 | 3 | 1 | 1 | 2 | true | false | A |
| PERS-004 | 5 | 5| 4 | 4 | 2 | 2 | 3| 4| false | true | A 
| PERS-005 | 2 | 4 | 2 | 4 | 5 | 5 | 5 | 5 | false | false | B |

## Rationale practice
Write 2-4 sentences per case. Reference context IDs such as C1/C2 and explain the concrete response behavior.

### "case_id": "PERS-001"
Response A fail to incorporate C1, C2 and C3. Response B incorporate C1, and C2 but fail to inorporate C3. Response B is partially correct (`should have ask for user about architecture, instead of recommending`)

### "case_id": "PERS-002"
Response A is partially correct. It only integrates C1, C2 in response but `it should contain examples of database models with index for django, and fastapi frameworks`. Response B is partially correct based on inference but Agent assumed `user like consice answar`

### "case_id": "PERS-003"
Response A is techically correct based on user context. Respone A only incorporate C2 while response is `forceful` implementation of C1 and C2 

### "case_id": "PERS-004"
Response A is correct based on User context "C1". Response B is partially correct becuase it includes C1 but assumed user `dislike learning new systems`

### "case_id": "PERS-005"
Response A is partially correct becuase it only include C2. Response B is correct becuase it include C2 explicitly but includes C1 implicitly stating django is `python based` server-side rendering framework for templates"  

## Calibration rule
Do not look at `gold_notes` until you have completed your independent judgments.
