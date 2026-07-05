---
title: Entre Pontos — Frontend renewal of the EDI logistics integrator
client: Entre Pontos
category: freela
status: Production
stack: [Next.js 16, React 19, Tailwind 4]
order: 1
---
# Case — Entre Pontos Integrador (Frontend Visual Renewal of an EDI Platform)

**Type:** Freelance (client: carrier / Simpress-ESL operation)
**Role:** Frontend Developer — visual renewal and refactoring of the integrator's frontend
**Status:** Delivered
**Stack:** Next.js 16, React 19, TypeScript, Tailwind CSS 4, Vitest, pnpm (existing backend: Fastify + Prisma + PostgreSQL)

## Context and problem

The operation's EDI integrator (PROCEDA/OCOREN/DOCCOB pipeline: ingestion via FTP/e-mail, layout transformation and output delivery) already worked, but the operational interface hadn't kept pace: dated visuals, confusing information hierarchy and inefficient reading of failures/status for the operators who monitor the pipeline all day.

## Solution

Complete visual renewal with a frontend refactor in Next.js 16 + React 19 + Tailwind CSS 4, guided by design documentation created specifically for the project:

- **Documented product language** (operational glossary: Outputs, Deliveries, Configuration Clients, Pipeline Profiles) — the UI started speaking the operation's language, with forbidden/preferred terms defined per concept
- **Explicit design principles** (PRODUCT.md/DESIGN.md): operational signal above decoration, failures/status/next steps immediately readable, information density as a work tool — a declared anti-reference to generic SaaS dashboards
- Refactoring of the main flows: pipeline monitoring, failure detail/investigation and reprocessing/resending in the same flow, with enough context to act

## Technical decisions

- **Next.js 16 + React 19** with Tailwind CSS 4 and TypeScript; tests with Vitest
- Sober, functional design system defined before the code (brand personality, anti-references and principles versioned in the repo) — a visual refactor done with judgment, not just "make it pretty"
- Visual validation assisted by Playwright during the redesign (comparative screenshots)

## Results and impact

- Modernized operational interface while keeping the existing backend and flows intact
- Faster reading of pipeline state and failure investigation for the operator — client feedback: the rebranding "came out excellent"
- Documented design foundation that keeps consistency across future UI evolutions

## Interview highlights (STAR summary)

- **S/T:** functional EDI integrator, but with a dated frontend that hindered operational readability. **A:** I led the visual renewal by refactoring the frontend in Next.js 16/React 19/Tailwind 4, first defining a product glossary and versioned design principles, prioritizing failure readability and useful information density. **R:** operation with a modern interface and objective pipeline reading, with no functional regression — and with a documented design foundation for the future.
