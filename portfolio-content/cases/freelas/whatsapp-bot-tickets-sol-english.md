---
title: Sol — Omnichannel IT service desk with AI
client: Cliente corporativo
category: freela
status: Production
stack: [FastAPI, Angular 20, pgvector, Gemini]
order: 5
---
# Case — Sol (Omnichannel IT Service Desk with AI and CRM)

**Type:** Freelance (corporate client — internal IT support)
**Role:** Full Stack Developer (full authorship: product, backend, frontend, AI, infrastructure and deployment)
**Status:** In production (with a separate UAT environment)
**Stack:** Python 3.11, FastAPI, async SQLAlchemy, Alembic, Angular 20 (standalone + Signals, strict TypeScript), PostgreSQL 16 + pgvector, Redis, Evolution API / Meta WhatsApp Cloud API, Microsoft Teams app, e-mail (messages), Gemini (`google-genai`) with a planned migration to Vertex AI, Docker Compose, deployment on a VPS + Google Cloud

## Context and problem

The client's IT team received support requests in a scattered way (personal WhatsApp, e-mail, word of mouth), with no queue, no history and no prioritization. Support needed to be structured across the channels users already use — without forcing anyone to learn a new portal — and give management real visibility into service quality and volume.

## Solution

An **omnichannel** service desk with AI, complete management and integrated CRM:

- **Multichannel support**: tickets handled via **WhatsApp, Microsoft Teams, a web platform and e-mail** (by messages) — same queue, same history, regardless of the incoming channel
- **AI triage bot (Gemini)**: converses naturally with the user, understands the problem, classifies it and opens the ticket with the right data; free-form conversations are also supported; fallback to local rules when the LLM is unavailable
- **Complete ticket management panel (Angular 20)**: queues, real-time conversations, per-ticket timeline, management dashboards — everything related to the ticket's lifecycle in one place
- **Service and satisfaction gauge**: AI-driven analysis with **conversation sampling**, generating a per-department assessment and actionable insights for management
- **Automated reports** on service operation and quality
- **Integrated CRM module**: campaigns and contact intake via WhatsApp on the same platform — service and relationship on the same data
- **Semantic search with pgvector**: history and knowledge indexed by embeddings to support triage

## Architecture and technical decisions

- **Async FastAPI** with async SQLAlchemy and Alembic; quality locked in with pytest, Ruff and mypy
- **Angular 20 standalone with Signals and pure SCSS**, strict TypeScript — fine-grained reactivity in the real-time conversation panel
- **Isolated channel layer**: WhatsApp (Evolution API in the MVP, with a planned migration to the official Meta Cloud API), Teams app and e-mail plug into the same ticket domain — adding a channel doesn't rewrite the business logic
- **PostgreSQL 16 + pgvector** for operational data and embeddings in the same database (less infrastructure, single transactions); **Redis** for conversation state and cache
- **Sampled quality analysis**: instead of processing 100% of conversations with an LLM (prohibitive cost), statistical sampling generates the satisfaction gauge and per-department assessments at a controlled cost
- **Two environments**: production and UAT with separate deployment scripts (`deploy.ps1`, `deploy-homolog.ps1`, `vps-setup*.sh`) — a reproducible pipeline from local build → tar → VPS
- **Security**: external SQL Server integrated with a restricted user/role; secrets kept out of version control

## Challenges and solutions

- **Unifying heterogeneous channels** (WhatsApp, Teams, e-mail, web) into a single ticket flow: a channel abstraction in the domain, with user identity resolved across channels
- **AI that can't block operations**: triage gracefully degrades to local rules when the LLM is unavailable
- **Measuring quality without explosive LLM cost**: gauge based on conversation sampling with per-department assessment
- **Dates, time zones and message ordering in asynchronous conversations**: handled as specific fix plans with tests
- **Visual evolution**: UI overhaul planned and executed with an in-house design system

## Results and impact

- IT tickets now originate structured from any channel (WhatsApp, Teams, e-mail, web), with a unified queue and history [volume TO CONFIRM]
- Management gains quality visibility: satisfaction gauge, per-department assessments and automated reports — previously there was no measurement at all
- Integrated CRM turns the same support channel into a campaign and contact-capture channel
- Operation with a UAT environment, versioned migrations and strict typing/lint — maintainable by third parties

## Interview highlights (STAR summary)

- **S/T:** corporate IT with no structured ticket channel and no service quality measurement. **A:** I built the omnichannel service desk alone — triage with Gemini and rule-based fallback, a complete management panel in Angular 20, a satisfaction gauge based on conversation sampling with per-department assessment, automated reports and a CRM module for WhatsApp campaigns — on top of an isolated channel layer (WhatsApp, Teams, e-mail, web). **R:** structured, measured support in production across the channels users already used, with AI cost controlled via sampling and two deployment environments.
