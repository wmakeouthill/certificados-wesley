---
title: AOG Dux Truck — Emergency logistics operations system
client: Dux Logistics
category: freela
status: Production
stack: [Java 21, Spring Boot 3, Angular 20, Entra ID]
order: 2
gallery: dux-logistics
---
# Case — AOG Dux Truck (Emergency Logistics Operations System)

**Type:** Freelance (client: Dux Logistics)
**Role:** Full Stack Developer (full authorship: backend, frontend, corporate authentication, deployment)
**Status:** In production
**Stack:** Java 21, Spring Boot 3, Clean Architecture, Angular 20+ (standalone + Signals), PostgreSQL, Microsoft Entra ID (OAuth2/OIDC), JWT, Docker Compose, Nginx (SSE)

## Context and problem

AOG (Aircraft On Ground — emergency transport of critical parts) operations require a rigid, traceable operational flow with aggressive deadlines. The client ran the flow defined in BPMN (`AOG - PADRÃO.bpmn`) manually via spreadsheet, with no control over status transitions, no auditable history and no portal for end clients to track their requests.

## Solution

A web operational system that implements the full AOG flow as an auditable state machine, with two audiences:

- **Internal operation**: corporate login via Microsoft Entra ID, per-operator access scopes, screens per flow stage, user and client management.
- **External client portal**: its own login (independent JWT) where each client sees only its own requests and their status in the flow.

Each request has its own **tracking screen**, shared between operation and client:

- **In-request conversation chat**: issues specific to that request are resolved right there, with context — no parallel e-mail thread
- **Comment exchange** between operator and client tied to the request
- **Traceable event timeline**: every status transition, comment and interaction is recorded chronologically, visible to both sides

Additional key features: automatic onboarding of Entra users as "pending" until admin activation, first-admin bootstrap via environment variable, photo sync via Microsoft Graph, real-time updates (SSE), per-screen scope management.

## Architecture and technical decisions

- **Clean Architecture in the backend**: domain 100% free of Spring/JPA; every status transition goes through a central `StatusTransicaoService` and generates a `HistoricoStatus` record — the BPMN flow becomes a domain invariant, impossible to bypass with a CRUD shortcut.
- **Dual, isolated authentication**: Entra ID (OIDC) for operators and a proprietary JWT issuer for external clients, with configurable TTL and issuer — separate attack surfaces.
- **Angular 20 with Signals and standalone components**: fine-grained reactivity without NgModules, with a proxy to the backend in dev.
- **Server-Sent Events behind Nginx** for real-time updates of operational queues.
- **Executed optimization plans**: cache and performance (`PLANO_OTIMIZACAO_CACHE_PERFORMANCE`), refresh token, Docker/JVM optimizations for a lean runtime.
- Docker Compose for the full local stack (frontend, API, Postgres) and scripted deployment (PowerShell).

## Challenges and solutions

- **Complex, non-linear business flow**: modeled as a domain state machine with explicit valid transitions — "impossible status" bugs eliminated by construction.
- **Coexistence of two identity models** (corporate and external) without data leakage between them: separation by profile, scope and query — an external client never accesses another client's data.
- **Freelance time-to-market**: incremental delivery guided by a backlog and implementation plans versioned in the repository.

## Results and impact

- The AOG flow moved from manual control to an auditable system with a complete history for every request
- Reduced e-mail/phone follow-ups: the client tracks each request on its own screen and resolves questions via the request's chat, with comments and a traceable event timeline visible to both sides
- Communication centralized in the right context: the conversation stays attached to the request, not scattered across e-mail threads
- Access governance: no user gains permissions without explicit admin activation

## Interview highlights (STAR summary)

- **S/T:** an emergency logistics client needed to digitize a critical BPMN flow with auditing and a client portal. **A:** I built the system alone in Java 21/Spring Boot 3 with Clean Architecture (pure domain, central state machine) and Angular 20 with Signals, integrating Microsoft Entra ID for the operation and a proprietary JWT for the external portal — with a per-request tracking screen including chat, comments and an event timeline shared between operator and client. **R:** end-to-end traceable operation in production, communication centralized in the context of each request (fewer e-mail/phone follow-ups) and an auditable history of every transition.
