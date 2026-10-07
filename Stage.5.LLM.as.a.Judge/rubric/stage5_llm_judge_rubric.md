# Stage 5 LLM-as-a-Judge Rubric

## Grounding — 1–5
5 = fully supported; 4 = strongly supported; 3 = mixed; 2 = multiple material problems; 1 = substantially invented/contradicted/detached.

## Integration — 1–5
5 = natural and useful; 4 = natural with minor excess; 3 = adequate; 2 = awkward/excessive; 1 = dominates or is unnatural.

## Helpfulness — 1–5
5 = highly useful; 4 = clearly useful; 3 = adequate; 2 = limited/distraction; 1 = misleading or unusable.

## Personalization Relevance — 1–5
5 = every meaningful personalized element is relevant; 4 = nearly all; 3 = mixed; 2 = several irrelevant details; 1 = mostly irrelevant.

## Forced Personalization
`true` only when context is used mainly because it is available rather than because it helps.

## Unsupported Inference
`true` when a preference, trait, habit, intention, or fact is not sufficiently supported.

## Claim-Level Evaluation
Each material personalized claim should include claim_id, text, evidence_ids, support_type, and support_score. A claim with no evidence normally has `UNSUPPORTED`.

## Rationale
2–4 sentences identifying strongest evidence, important failure, and why the scores/flags follow.
