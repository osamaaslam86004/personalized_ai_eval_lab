# Stage 3 — Evidence Tracing Dataset

Complete the cases before using the gold-focus notes for calibration.

## PERS-021

### Context
- C1: User uses Python and FastAPI for backend APIs.
- C2: User uses PostgreSQL for relational data.
- C3: User is learning Docker.
- C4: User has never mentioned Kubernetes.

### User request
How should I package my small FastAPI API for deployment?

### AI response
Since you use FastAPI and are learning Docker, containerizing the API with Docker is a natural fit. For a small deployment, a simple container host is enough; Kubernetes would be unnecessary complexity.

### Gold-focus note
C1 and C3 explicitly support the personalization. The Kubernetes statement is a recommendation based on C4, not a personal preference claim.

---

## PERS-022

### Context
- C1: User uses Python.
- C2: User has asked for concise explanations.
- C3: User has never stated a preference for pytest over unittest.

### User request
Show me a simple way to test a Python function.

### AI response
Because you prefer pytest, I'll keep this concise and use pytest for the example.

### Gold-focus note
C2 supports concise explanations. The pytest preference is unsupported.

---

## PERS-023

### Context
- C1: User uses Django.
- C2: User uses FastAPI.
- C3: User uses PostgreSQL.
- C4: User is learning AI-agent evaluation.

### User request
Explain database indexes.

### AI response
Since you use PostgreSQL, an index is a data structure that helps PostgreSQL find rows without scanning the entire table. That should fit the kind of backend work you do with Django and FastAPI.

### Gold-focus note
C3 directly supports PostgreSQL. C1/C2 support the frameworks, but the broader work claim is a synthesis and should not be overstated.

---

## PERS-024

### Context
- C1: User uses Celery with Redis for background jobs.
- C2: User has never stated that Redis is a favorite technology.
- C3: User has used PostgreSQL.

### User request
What would you use for asynchronous jobs in this service?

### AI response
You already prefer Redis, so I would definitely keep Redis and Celery.

### Gold-focus note
C1 supports current Redis/Celery use. The preference claim is unsupported.

---

## PERS-025

### Context
- C1: User explicitly prefers PostgreSQL for relational projects.
- C2: User has used MongoDB.
- C3: User has not stated a preference for MongoDB.

### User request
Should I use PostgreSQL or MongoDB for a relational application?

### AI response
You have explicitly said you prefer PostgreSQL for relational projects, so PostgreSQL is consistent with that stated preference.

### Gold-focus note
C1 directly supports the personalized claim. C2 is true but unnecessary.

---

## PERS-026

### Context
- C1: User has 8 GB RAM.
- C2: User has no AVX support.
- C3: User uses Google Colab Free for heavier experiments.
- C4: User experiments with small quantized GGUF models.

### User request
Where should I run a larger local language model?

### AI response
Given your 8 GB RAM and no AVX support, your local machine is constrained. You also use Colab Free for heavier experiments, so moving the larger experiment to Colab is consistent with your existing setup.

### Gold-focus note
C1, C2, C3 directly support the claims. C4 is irrelevant unless the question is specifically about GGUF.

---

## PERS-027

### Context
- C1: User watches football videos.
- C2: User is learning AI evaluation.
- C3: User uses Python.

### User request
What is precision versus recall?

### AI response
Since you enjoy football videos, I'll explain precision and recall using a football referee analogy.

### Gold-focus note
C1 supports watching football videos, not the claim that the user enjoys them. Personalization is unsupported and relevance is not established.

---

## PERS-028

### Context
- C1: User uses FastAPI.
- C2: User uses pytest.
- C3: User wants to add CI to the project.

### User request
How should I organize testing before adding CI?

### AI response
You already use FastAPI and pytest, and you want CI, so I would organize tests around behavior first and add CI after the test suite is stable.

### Gold-focus note
C1, C2, C3 all support the personalized setup.

---

## PERS-029

### Context
- C1: User asked for simple explanations once.
- C2: User has discussed both FastAPI and Django.
- C3: User has never said they dislike complexity.

### User request
FastAPI versus Django: how should I choose?

### AI response
You usually prefer simple solutions, so FastAPI is probably better for you.

### Gold-focus note
C1 does not establish a stable general preference. The claim is an unsupported inference.

---

## PERS-030

### Context
- C1: User prefers concise explanations.
- C2: User uses Python.
- C3: User is learning AI evaluation.
- C4: User uses FastAPI.

### User request
Explain a confusion matrix.

### AI response
I'll keep this concise, as you prefer. A confusion matrix compares predicted labels with actual labels.

### Gold-focus note
C1 explicitly supports the personalization. C2-C4 are irrelevant to that claim.

---

## PERS-031

### Context
- C1: User has deployed small applications.
- C2: User has never used a managed cloud database.
- C3: User uses PostgreSQL.

### User request
What should I check when choosing a managed PostgreSQL provider?

### AI response
Because you have deployed small applications and use PostgreSQL, I would compare pricing, backups, connection limits, networking, scaling, and operational controls.

### Gold-focus note
C1 and C3 support the personalized context. C2 does not support a claim that the user already knows managed database operations.

---

## PERS-032

### Context
- C1: User uses PostgreSQL.
- C2: User uses Redis.
- C3: User uses Celery.
- C4: User has never said they want to avoid managed services.

### User request
Should I self-host Redis or use a managed Redis service?

### AI response
Since you prefer managing infrastructure yourself, I would self-host Redis.

### Gold-focus note
C1-C3 support current use, not an infrastructure preference. The preference claim is unsupported.

---

## PERS-033

### Context
- C1: User is learning automated evaluation.
- C2: User uses pandas.
- C3: User uses Python.

### User request
How do I calculate the average evaluation score?

### AI response
Since you're learning automated evaluation and use pandas, you can calculate the mean with pandas. If the scores are in a column called score, use the column's mean operation.

### Gold-focus note
C1 and C2 support the personalization. C3 is true but unnecessary.

---

## PERS-034

### Context
- C1: User uses Django.
- C2: User has never used React.
- C3: User is learning JavaScript.

### User request
What is React?

### AI response
Since you already use React with Django, React components should be familiar to you.

### Gold-focus note
The claim that the user already uses React is contradicted by C2. Django use does not establish React use.

---

## PERS-035

### Context
- C1: User explicitly wants concise technical explanations.
- C2: User uses FastAPI.
- C3: User uses PostgreSQL.

### User request
What is database normalization?

### AI response
You like concise explanations, so here is the short version: normalization organizes relational data to reduce unnecessary duplication and update anomalies.

### Gold-focus note
C1 explicitly supports the personalization. C2 and C3 are unnecessary for tracing it.

---

