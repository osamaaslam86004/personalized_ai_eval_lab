# Stage 5 Rules: LLM-as-a-Judge

## 1. Evaluation order
Read context → request → candidate response → identify material personalized claims → trace evidence → classify support → score dimensions → mark flags → write rationale.

## 2. Evidence discipline
Use only supplied evidence. Labels: EXPLICIT, SYNTHESIZED, INFERRED, IRRELEVANT, CONTRADICTED, UNSUPPORTED. Absence of a stated preference is normally UNSUPPORTED, not CONTRADICTED.

## 3. Scores
Grounding, Integration, Helpfulness, and Personalization Relevance are integers 1–5. Never output 0 or >5.

## 4. Dimension meanings
- Grounding: are personalized claims supported?
- Integration: is context naturally and usefully woven in?
- Helpfulness: does personalization improve the answer?
- Personalization Relevance: is used context relevant to the request?

## 5. Flags
Forced Personalization = context is used mainly because it exists. Unsupported Inference = a preference, trait, habit, intention, or fact is asserted without sufficient evidence.

## 6. Missing personalization
Do not penalize omission automatically. Personalization is not required when it would not improve the answer.

## 7. Technical correctness
Technical correctness is separate from personalization quality. Mention material technical errors in rationale, but do not invent personalization defects.

## 8. Structured output
Return exactly: `case_id`, `scores`, `flags`, `claim_evaluations`, `rationale`. No Markdown fences or prose outside JSON.

## 9. No silent repair
Malformed output is a pipeline failure. Reject unknown evidence IDs, invalid scores, missing fields, malformed JSON, and other schema violations.

## 10. Human reference
Human labels are the reference set. Never alter them to make the judge agree.

## 11. Stage 6 boundary
Stage 5 produces validated judge outputs and comparison fixtures. Statistical agreement, confusion matrices, and deeper error analysis belong to Stage 6.
