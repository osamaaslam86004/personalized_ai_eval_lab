# Stage 3 — Evidence Tracing Rules

For every case:

1. Read the complete context.
2. Read the request.
3. Read the AI response.
4. Identify every meaningful personalized claim.
5. Assign claim IDs: C1, C2, C3...
6. Trace each claim to the smallest relevant evidence source(s).
7. Label it EXPLICIT, SYNTHESIZED, INFERRED, IRRELEVANT, CONTRADICTED, or UNSUPPORTED.
8. Score support 1–5.
9. Assess overall evidence coverage.
10. Write a 2–4 sentence evidence-based rationale.

### What counts as a personalized claim?
Statements about what the user uses, prefers, knows, has experienced, is learning, wants, usually does, or is likely to choose.

### Evidence discipline
Use the **smallest sufficient evidence set**. Do not reward context dumping.

Example:
- “You use FastAPI.” → trace to C1.
- “You prefer FastAPI.” → unsupported unless preference is explicitly established.

### Contradictions
If context says the user has never used React and the response says “since you already use React,” mark the claim CONTRADICTED.

### Output
For each case provide:

| Claim ID | Personalized claim | Evidence ID(s) | Label | Score |
|---|---|---|---|---|

Then:
- Coverage: Complete / Mostly complete / Incomplete / Failed
- Rationale: 2–4 sentences

Do not use overall answer quality as a substitute for evidence tracing.
