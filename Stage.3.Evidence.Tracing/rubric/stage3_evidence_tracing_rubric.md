# Stage 3 — Evidence Tracing Rubric

## Purpose
Trace every meaningful personalized claim in an AI response to the specific user evidence that supports it.

Distinguish:
- **EXPLICIT** — directly supported by a context item.
- **SYNTHESIZED** — supported by multiple context items without adding an unsupported personal fact.
- **INFERRED** — plausible-sounding but not established.
- **IRRELEVANT** — true context that does not support useful personalization.
- **CONTRADICTED** — conflicts with available context.
- **UNSUPPORTED** — personal claim has no identifiable evidence source.

## Claim-level score
**5:** directly supported, no meaningful leap.  
**4:** strongly supported by closely related evidence or a small reasonable synthesis.  
**3:** plausible but interpretive; should not be stated as certain personal fact.  
**2:** weakly supported; substantial inference required.  
**1:** unsupported or contradicted.

## Evidence coverage
- **Complete:** all meaningful personalized claims traceable.
- **Mostly complete:** one minor weak/ambiguous claim.
- **Incomplete:** multiple meaningful claims lack evidence.
- **Failed:** personalization is substantially fabricated, contradicted, or untraceable.

## Calibration principles
- Context existing does not mean personalization is required.
- True context is not automatically relevant evidence.
- More evidence references do not make an answer better.
- Do not convert “used X” into “prefers X.”
- Do not convert one behavior into a stable trait or long-term preference.
- Technical correctness and evidence grounding are separate dimensions.
