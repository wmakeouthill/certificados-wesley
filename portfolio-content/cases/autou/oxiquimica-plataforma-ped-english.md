---
title: Colibri — R&D formulation platform with Bayesian optimization
client: Oxiquímica
category: autou
status: Production
stack: [FastAPI, React 19, Vertex AI, BayBE]
order: 5
---

# Case — Oxiquímica (R&D Formulation Platform with Bayesian Optimization)

**Type:** AutoU (client: Oxiquímica — chemical/fertilizer industry)
**Role:** Technical discovery, architecture and prototyping — translating a lab process into a software product; technical lead of project workstreams (team project), with direct client contact in weekly checkpoints and ad-hoc alignment sessions
**Status:** Live (in production)
**Stack (defined):** Python 3.13, FastAPI, React 19 + TypeScript, Vertex AI (Google Cloud), Gemini via `google-genai`, BayBE (Bayesian optimization, Merck's open-source project), RAG with source governance, PostgreSQL

> Confidentiality note: AutoU client project — validate what can be made public before exposing name/details.

## Context and problem

Oxiquímica's R&D lab develops formulations (fertilizers and the like) by trial and error: each iteration goes through a ~14-day greenhouse/climate-chamber cycle, and the knowledge of which combinations work lives in the analysts' heads. Many iterations mean months until a stable formula.

## Solution (designed product)

An R&D platform with a generative AI agent ("Colibri", Gemini via `google-genai`) that generates/assists formulas and reduces physical iterations:

- **Formulation Management Hub**: KPIs (success rate, average iterations), cards per formulation with stability probability and a countdown for the climate test
- **Reactive composition table**: autocomplete from the raw-materials database, auto-filled guaranteed content, suggested average purity (editable per batch) and **real-time computed guarantee** (`concentration × purity`) — computed on the front end and revalidated on the backend
- **Bayesian optimization with BayBE**: suggests the next formulation to test based on previous experiments — fewer greenhouse cycles to reach the target
- **Scientific chat with dual RAG**: answers by querying the internal knowledge base and web search with a **source whitelist/blacklist** (citation governance, every answer traceable to its origin)
- **Explicit formula versioning** (V0, V1... with author and status) and a process timeline (definition → AI analysis → climate chamber → opinion → approval)

## Technical work performed

- **In-depth study of BayBE** (Merck's framework) with my own versioned Python examples — feasibility validated before promising anything to the client
- **Full architecture documented** from the Figma prototype + designer comments, turning each comment into an executable specification (field-by-field behavior of the composition table)
- **Documented architecture decisions**: reactive calculation on the front end with backend revalidation as the source of truth; purity override per composition without changing the raw-material record; default-block policy for unlisted web sources
- Survey and cataloging of the client's material archive (general catalog and a detailed raw-materials map)
- **Observability with Grafana + Prometheus** implemented by me: monitoring of cost (AI usage), consumption and platform infrastructure

## Challenges and solutions

- **Complex scientific domain**: formulation chemistry translated into a domain model (guarantees, purities per batch, raw-material functions) validated with the designer and the client
- **Responsible AI**: in a confidential industrial environment, the web RAG has explicit source governance — recommendation to block by default
- **Prototype-driven discovery**: open questions documented and addressed with the client instead of silent assumptions

## Results and impact

- Modernization of the R&D process that already existed: a previously manual, trial-and-error flow became an automated platform with AI assistance and **stability recommendation via Bayesian optimization (BayBE)** — in production
- Lab knowledge captured in a queryable base (RAG) instead of tribal knowledge
- Greenhouse cycle tracked digitally with informed interruption

## Interview highlights (STAR summary)

- **S/T:** chemical R&D iterating by trial and error with 14-day physical cycles. **A:** I led the technical discovery — studied and validated BayBE (Bayesian optimization) with my own examples, wrote the FastAPI + React 19 + Vertex AI architecture from the Figma prototype, and specified the scientific RAG with source governance. **R:** architecture approved as the basis for the implementation plan, with AI feasibility validated before any promise to the client.
