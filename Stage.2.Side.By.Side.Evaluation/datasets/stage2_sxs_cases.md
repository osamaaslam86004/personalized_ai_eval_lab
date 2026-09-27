# Stage 2 SxS Cases

## PERS-006

**Context:** C1 FastAPI/Python; C2 PostgreSQL; C3 learning Docker; C4 never mentioned Kubernetes.

**Request:** I need to deploy my small FastAPI API for a personal project. What should I use?

A: Since you already work with FastAPI and PostgreSQL, Docker is a practical way to package your application and its dependencies. For a small personal deployment, you could run the container on a simple VPS or a managed container platform rather than introducing Kubernetes.

B: Since you're learning Docker, Kubernetes would be a natural next step. You could containerize the FastAPI service, create Kubernetes manifests, and deploy the application through a Kubernetes cluster.

## PERS-007

**Context:** C1 Python; C2 several backend APIs; C3 no stated command-line preference; C4 VS Code.

**Request:** How can I test my API endpoints locally?

A: Since you already build Python APIs, pytest with FastAPI's test client is a straightforward option. You can write tests for your endpoints and run them locally before deploying.

B: Since you're an experienced backend developer who prefers working from the command line, pytest is probably the best option. You can run your API tests directly from the terminal and automate them later in CI.

## PERS-008

**Context:** C1 Django; C2 FastAPI; C3 PostgreSQL; C4 Python tutorials; C5 learning AI-agent evaluation.

**Request:** Explain what a database index does.

A: Since you use PostgreSQL, think of an index as an additional structure PostgreSQL can use to find rows faster instead of scanning the entire table. For example, an index on email can make lookups by email much faster.

B: Since you use Django, FastAPI, PostgreSQL, and you're learning AI-agent evaluation, database indexes are especially important. You can think of indexes in terms of the backend systems and AI applications you're building.

## PERS-009

**Context:** C1 Redis for background jobs; C2 Celery; C3 no statement that Redis is a favorite.

**Request:** My application needs to process jobs asynchronously.

A: Since you have used Celery with Redis, you could reuse that architecture here. Celery can handle asynchronous job execution while Redis can act as the broker.

B: You have used Redis and Celery before, which means you have experience with distributed systems. Redis is your familiar technology, so using Redis and Celery is obviously the correct architectural choice for your application.

## PERS-010

**Context:** C1 Python; C2 FastAPI; C3 learning JavaScript; C4 never used React.

**Request:** What is React?

A: React is a JavaScript library for building user interfaces. It lets you create reusable components and update parts of a web page efficiently.

B: Since you know Python and FastAPI, React should be easy for you. You can think of React components as similar to FastAPI routes because both let you organize application logic into reusable pieces.

## PERS-011

**Context:** C1 explicitly prefers PostgreSQL for relational projects; C2 SQLite; C3 MongoDB; C4 no stated SQL/NoSQL preference for this project.

**Request:** I'm starting a small application. Should I use PostgreSQL or MongoDB?

A: You previously said you prefer PostgreSQL for relational projects, so PostgreSQL would align with an explicitly stated preference. If your data is highly relational, that also supports the choice independently of the preference.

B: Since you have used PostgreSQL, you clearly prefer SQL databases. PostgreSQL is therefore the right choice for this application.

## PERS-012

**Context:** C1 8 GB RAM; C2 no AVX; C3 Google Colab Free; C4 experimenting with small quantized GGUF models.

**Request:** Can I run a large 30B parameter model locally?

A: A 30B model is likely to be impractical on your local machine given the 8 GB RAM constraint. Since you have access to Colab, a cloud GPU environment would be more appropriate for substantially larger models.

B: Since you work with GGUF models, you can run a 30B model locally if you quantize it aggressively. GGUF is designed to make large models easier to run on consumer hardware.

## PERS-013

**Context:** C1 FastAPI; C2 Django; C3 Redis; C4 enjoys football videos; C5 learning AI evaluation.

**Request:** What is the difference between precision and recall?

A: Precision measures how many predicted positives are actually positive, while recall measures how many actual positives the system successfully identifies. For example, in a classifier, high precision means fewer false positives, while high recall means fewer false negatives.

B: Since you work with FastAPI and Django and are learning AI evaluation, precision and recall are especially important for your projects. You can think of them like football statistics, where precision measures successful predictions and recall measures how many opportunities you didn't miss.

## PERS-014

**Context:** C1 building FastAPI service; C2 already wrote pytest tests; C3 wants CI later.

**Request:** How should I organize automated testing?

A: Since you already have pytest tests, organize them around application behavior rather than implementation details. Keep unit tests separate from integration tests, and later run the test suite automatically in CI.

B: Your FastAPI service, pytest tests, and future CI plans are all relevant here. FastAPI is a Python framework, pytest is a Python testing framework, and CI means continuous integration. A good testing strategy includes unit tests and integration tests.

## PERS-015

**Context:** C1 asked about several Python frameworks; C2 FastAPI and Django; C3 no statement disliking complexity; C4 asked for simple explanations once.

**Request:** Should I use FastAPI or Django for a new project?

A: Given your existing experience with both FastAPI and Django, either is a viable starting point. FastAPI may fit an API-focused service particularly well, while Django provides a broader integrated web framework.

B: Since you usually prefer simple solutions, FastAPI is probably better for you. It's less complex than Django and should be easier for you to manage.

## PERS-016

**Context:** C1 PostgreSQL; C2 deployed small applications; C3 never used a cloud database service.

**Request:** What should I consider when choosing a managed PostgreSQL provider?

A: Since you already use PostgreSQL and have deployed small applications, you can focus on provider differences such as pricing, backups, connection limits, scaling, and operational tooling. You should also check whether the provider's networking model fits your deployment.

B: Since you already use PostgreSQL, you won't need to worry about database operations when using a managed provider. The provider will handle everything for you.

## PERS-017

**Context:** C1 learning AI-agent evaluation; C2 Python; C3 structured JSON; C4 FastAPI.

**Request:** What is a confusion matrix?

A: A confusion matrix summarizes classification results by counting true positives, true negatives, false positives, and false negatives. For an evaluation task, it helps you see which kinds of classification errors a system makes.

B: Since you're learning AI-agent evaluation, a confusion matrix is particularly useful. Because you know Python, FastAPI, and structured JSON, you can represent the matrix programmatically as JSON and expose it through FastAPI.

## PERS-018

**Context:** C1 explicitly prefers concise explanations; C2 Python; C3 FastAPI; C4 interested in AI evaluation.

**Request:** Explain the difference between RAM and storage.

A: RAM is fast temporary working memory used by running programs. Storage, such as an SSD, keeps data persistently even after the computer is turned off.

B: Since you prefer concise explanations, here's the short version: RAM is temporary working memory, while storage is persistent data storage. This distinction is especially important for your Python and AI projects.

## PERS-019

**Context:** C1 PostgreSQL; C2 Redis; C3 Celery; C4 never said they want to avoid managed services.

**Request:** Should I use a managed Redis service?

A: Since you've already used Redis and Celery, you're familiar with the technologies involved. A managed Redis service could reduce the operational work of running Redis yourself, so compare its cost and features with self-hosting.

B: Since you've used Redis and Celery, you probably prefer managing infrastructure yourself. Self-hosting Redis would therefore be the better choice for you.

## PERS-020

**Context:** C1 Python; C2 learning automated evaluation; C3 pandas.

**Request:** How can I calculate the average score across evaluation results?

A: If your evaluation results are stored in a pandas DataFrame, you can calculate the mean of the score column. For example, df['score'].mean() gives the average score.

B: Since you already use pandas, you can calculate the average directly from your score column using df['score'].mean(). If the scores are stored elsewhere, the same arithmetic is simply the sum of scores divided by the number of scores.

