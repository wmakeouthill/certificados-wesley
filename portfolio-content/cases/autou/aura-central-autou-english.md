---
title: Aura Central — Notifications & logs in a B2B platform
client: AutoU
category: autou
status: Production
stack: [FastAPI, React, Pub/Sub]
order: 7
---

# Case — Aura Central (AutoU's Internal Ecosystem: People, Goals and HR Management Platform)

**Type:** AutoU (internal product used by B2B corporate clients)
**Role:** Full Stack Developer — notifications feature and logging system
**Status:** In production
**Stack:** Python (FastAPI), uv, React + TypeScript, pnpm, PostgreSQL (database per service), DDD architecture with Bounded Contexts, Event-Driven (Pub/Sub), monorepo with shared packages, Docker Compose, GitHub Actions

## Context and problem

AutoU needed a unified internal ecosystem for people management — HR, recruitment, commercial CRM, project allocation/timesheet and performance evaluation — without falling into a "distributed monolith" or five disconnected systems.

## Solution

A monorepo with **five bounded contexts** (DDD), each with its own backend and frontends:

| Context | Responsibility |
|---|---|
| Identity | Auth, employee master data, HR |
| Recruitment | Candidates and job openings |
| Sales (CRM) | Sales funnel, proposals, masterplan |
| Projects | Allocation, timesheet, tasks, casebook |
| Performance | 360 evaluation, feedback, OKRs/goals, recognition |

My contribution: I developed the **notifications feature** (the `aura-notifications` service, cross-cutting across contexts) and the platform's **logging system** — working within the monorepo's DDD/event-driven architecture, respecting database-per-service and event-based communication.

## Architecture and technical decisions

- **Database per Service**: each context has an isolated database; no service reads another's database — coupling by contract, not by schema
- **Synchronous front→back communication via REST** and **asynchronous back→back via events (Pub/Sub)** with eventual consistency
- **Shared packages in the monorepo**: UI kit (AutoU design system), TypeScript types (DTOs/enums), event-bus abstraction and base configs — reuse without runtime coupling
- **Toolchain**: uv on Python backends, pnpm on frontends, Docker Compose for local databases
- Documented CMS migration plan (`PLANO-CMS-AURA-MIGRATION.md`)

## Challenges and solutions

- **Avoiding the distributed monolith**: bounded-context discipline with isolated data and events for synchronization — changes in one domain don't break the others
- **Eventual consistency in people data**: domain events propagate employee changes across contexts without chained synchronous calls

## Results and impact

- B2B platform in production used by corporate clients [number of clients/users TO CONFIRM]
- Cross-context notifications delivered via events, without coupling domains
- Structured logs giving the team operational visibility in production

## Interview highlights (STAR summary)

- **S/T:** a people-management ecosystem with five bounded contexts needed cross-cutting notifications and observability without coupling domains. **A:** I developed the notifications feature (a dedicated service consuming events from the contexts) and the logging system, respecting database-per-service and asynchronous Pub/Sub communication. **R:** notifications and logs in production serving every domain of the B2B product, without breaking the isolation between contexts.
