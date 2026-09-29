# Stage 2 SxS Rubric
## 1. Grounding
Question: Are personalized claims supported by available user evidence?

1 = multiple unsupported or contradictory claims
2 = substantial unsupported personalization
3 = mostly supported, with a questionable inference
4 = well supported, minor issue
5 = every meaningful personalized claim is traceable to evidence

## 2. Integration
Question: Is personal information woven naturally into the answer?

1 = personalization is distracting or dumped as a history recap
2 = awkward and repetitive
3 = usable but somewhat mechanical
4 = natural and appropriately concise
5 = personalization is seamless and materially improves the response

## 3. Helpfulness
Question: Does the personalization make the answer more useful for the user's actual request?

1 = harms usefulness
2 = little useful value
3 = adequately useful
4 = clearly improves usefulness
5 = materially improves the answer or decision

## 4. Personalization Relevance
Question: Was the selected personal context relevant to the current task?

1 = mostly irrelevant
2 = weak relevance
3 = partially relevant
4 = strongly relevant
5 = directly relevant and necessary/useful

## 5. Forced Personalization
Mark true when the model uses personal information mainly because it is available, rather than because it helps answer the request.

## 6. Unsupported Inference
Mark true when the model infers a preference, trait, intention, habit, or fact that is not supported by evidence.

## 7. SxS decision
Allowed labels: A, B, Tie.
Do not use overall labels such as 'best model'. The rationale must explain the concrete difference / Do not choose based on amount of personalization.

**Rationale:** 2–4 sentences. State the behavior, cite context IDs, explain the impact, and compare the responses.
