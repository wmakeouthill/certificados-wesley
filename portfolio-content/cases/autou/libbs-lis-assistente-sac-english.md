---
title: LIS — AI-powered SAC ticket triage (demo)
client: Libbs (demo — public bid in progress)
category: autou
status: Live demo
stack: [FastAPI, React 19, Gemini]
order: 4
---

# Case — LIS (Demo for Libbs' Public Bid: AI-Powered Customer Service Ticket Triage Assistant)

**Type:** AutoU (demo for a Libbs public bid — pharmaceutical industry; the bid is still in progress, Libbs is **not** an AutoU client)
**Role:** Full Stack Developer — solo project (demo/MVP built alone)
**Status:** Live demo (awaiting the bid's outcome)
**Stack:** Python, FastAPI, Poetry, React 19, TypeScript, Vite, TanStack Query, Zustand, Recharts, PostgreSQL, Gemini (`google-genai`) with rule-based fallback, Docker Compose, deployment on Oracle Cloud VPS

> Confidentiality note: demo built by AutoU to compete for a public bid — validate what can be made public before exposing name/details. Do not present it as a contracted project or an AutoU client while the bid is undecided.

## Context and problem

The pharmaceutical company's customer service (SAC) receives heterogeneous requests (medication questions, pharmacovigilance, complaints) that must be manually triaged before reaching the right agent — with regulatory risk when an adverse-event report takes too long to be classified. AutoU decided to compete for Libbs' public bid for this problem, and the LIS demo was built as a functional technical proposal — the bid is still in progress.

## Solution

The LIS portal with two surfaces in the same application:

- **Public chat** (own domain, e.g. `chat.domain.com`): the end user talks to the LIS assistant, which triages the request with AI and opens the classified ticket; cases requiring a human are **escalated** to support
- **Internal portal** (protected login): a "Conversations and support" queue, ticket view with timeline, dashboards (Recharts)

## Architecture and technical decisions

- **Graceful AI degradation**: without `GOOGLE_GENAI_API_KEY`, LIS triages via local rules — the MVP is never down due to LLM unavailability or cost
- **One application, two domains**: the same frontend serves the internal portal and the public chat, routed by the `VITE_CHAT_HOSTS` env var — less infrastructure, the same API and database, natural escalation between channels
- **React 19 + TanStack Query + Zustand**: server state and client state separated by the right tool; tests with Vitest + Testing Library
- **Registry-free deployment**: a PowerShell script builds images locally, sends `images.tar` + compose + `.env` via SSH and brings it up on the VPS — a simple, reproducible pipeline for the MVP
- Architecture documented in HTML diagrams and technical opinions versioned in the repo (presentation material for the bid)

## Challenges and solutions

- **Regulated sector (pharma)**: triage with a clear conversation→ticket trail and human escalation for sensitive cases
- **Fidelity to the design**: screens implemented from CSS specifications extracted from Figma (chat and conversations/timeline view)
- **MVP cost**: Oracle Cloud Always Free + DuckDNS, with a clear path to definitive infrastructure

## Results and impact

- Automatic SAC ticket triage with AI-assisted classification and deterministic fallback
- Public support channel and internal portal delivered as a single deployment
- Functional demo presented in the bid at zero infrastructure cost — bid outcome still in progress

## Discovery-projected indicators (business-case projections — not measurements)

Baseline gathered with the stakeholders: **~50 tickets/day (~18–20k/year)**, of which **80% are simple**; current handling time of **7 min/ticket** (5 min drafting the answer + 2 min logging), with a response SLA of up to 24h. Projections presented:

- **Automatic resolution:** ~72% of tickets with no human intervention (~36/day) — the AI resolves ~90% of the simple ones; complex cases go to a human with pre-collected context
- **Average handling time:** from 7 min to ~2 min (**~71% reduction**) — simple cases answered instantly, complex ones in ~4 min because the context arrives already structured
- **Correct escalation:** ~90% of sensitive cases routed correctly to a human, trending to 95%+ with the feedback loop
- **Operational load:** ~4.2h/day saved (~1,050h/year), **estimated savings of ~R$ 26k/year** — not counting quality and rework
- **Intent-classification accuracy:** ~82% at go-live → ~90% after the 1st feedback cycle → ~95% in mature operation (differentiator: continuous knowledge-base governance and agent feedback)
- **NPS:** estimated gain of +25 to +30 points vs. traditional SAC

> Automation with judgment, not a 100% automated SAC: simple cases (résumé, discount, institutional questions) resolved instantly with approved answers; sensitive ones (adverse event, quality deviation, technical complaint) identified, collected and safely escalated — respecting pharmacovigilance, LGPD and consumer-protection law.

## Interview highlights (STAR summary)

- **S/T:** a pharmaceutical public bid to solve SAC with manual triage and regulatory risk from slow classification — AutoU needed a functional technical proposal, not just slides. **A:** I built the full-stack demo alone — public chat with Gemini-based triage and rule-based fallback, escalation to human support, internal portal with a ticket timeline — serving two domains from a single application with a scripted VPS deployment. **R:** a functional demo live, supporting AutoU's bid candidacy (in progress), resilient to LLM unavailability and with zero infrastructure cost.
