---
title: Dux Workflow — Logistics & document workflow platform
client: Dux Logistics
category: freela
status: UAT
stack: [Java, Spring Boot, Angular, PostgreSQL]
order: 3
gallery: dux-logistics
---
# Case — Dux Logistics MVP (Logistics & Document Workflow Platform)

**Type:** Freelance (client: Dux Logistics)
**Role:** Full Stack Developer and product/architecture owner
**Status:** Complete, in UAT with the client
**Stack:** Java, Spring Boot, Angular, PostgreSQL, Docker Compose, deployed on an Oracle Cloud VPS

## Context and problem

The client ran logistics and document processes on an expensive, generic corporate BPM platform (TOTVS Fluig-style): request creation, group handling queues, staged approvals, attachments and SLAs. The goal was to replace it with a lean, in-house product specialized in the logistics domain — without paying the cost (financial and complexity) of a generic BPM.

## Solution

A corporate web product for logistics operational workflow, designed by reverse-engineering the legacy system's screens:

- Request creation with per-type forms (controlled schema, not a free-form editor)
- Individual and group task inbox, with handling, forwarding, return and reassignment
- Single or multi-stage approval, workflow parameterizable by request type
- Document, attachment and document checklist management
- Complete request timeline (audit trail and change history)
- Operational dashboard with delay, deadline and volume indicators; filters, export and batch operations
- Organizational records (company, unit, department, groups) and operational records (clients, document types, priorities)
- In-app and e-mail notifications

## Architecture and technical decisions

- **Explicit product decision**: workflow parameterizable by stages, rules, groups and SLA — no open BPMN and no generic low-code. Controlled scope = a viable MVP for a solo developer.
- **Dynamic forms with a controlled schema**: fields configurable per request type with standardized components, avoiding the trap of an unbounded "form builder".
- **Java + Spring Boot on the backend and Angular on the frontend**, following an in-house development rules guide versioned in the repo (code standards, tests and API contract).
- **PostgreSQL** with modeling for a per-request audit trail.
- **Docker Compose** for dev and production, with a specific compose file for deployment on an Oracle Cloud VPS (near-zero infrastructure cost on the free tier).
- JVM/query optimization plan versioned and applied (`PLANO-OTIMIZACOES-JAVA.md`).

## Challenges and solutions

- **Gathering requirements without access to the original system**: requirements inferred from real screenshots of the operation, validated with the client and documented in a detailed product plan before coding.
- **Balancing "complete product" vs. "Fluig clone"**: trade-offs documented; anything too generic was left out of the MVP in favor of depth in the logistics domain.
- **Operating as a full-cycle freelancer**: from the commercial proposal (sales PPTX) to the VPS deployment, covering product, UX, architecture and code.

## Results and impact

- Replacement of a corporate BPM license with a specialized in-house product [savings TO CONFIRM]
- Processes with full traceability and SLAs visible to management
- Parameterizable foundation that lets the client create new request types without development work

## Interview highlights (STAR summary)

- **S/T:** the client wanted to move away from an expensive generic BPM to an in-house logistics workflow product. **A:** I did discovery by reverse-engineering screenshots, wrote the product plan with explicit trade-offs (parameterizable yes, low-code no), and built the full-stack MVP in Java/Spring + Angular with deployment on an Oracle VPS. **R:** functional MVP covering request creation, queues, approvals, documents and dashboard, with infrastructure cost near zero.
