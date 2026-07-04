---
title: AI-powered invoice (NF-e) email automation
client: Dux Logistics
category: freela
status: Production
stack: [FastAPI, React, MS Graph, PostgreSQL]
order: 4
gallery: dux-logistics
---
# Case — Dux NF (AI-Powered Invoice Automation via E-mail)

**Type:** Freelance (client: Dux Logistics — pickup operation at Fiat/Citroën dealerships, Stellantis context)
**Role:** Full Stack Developer (full authorship)
**Status:** In production
**Stack:** Python, FastAPI, React + TypeScript + Vite, PostgreSQL, Microsoft Graph API (Outlook/M365), AI for extraction (OCR/LLM fallback), Docker Compose, deployment on Hostinger/Oracle Cloud

## Context and problem

The logistics operation received dozens of invoices (XML and PDF) by e-mail and manually fed an operational demand-control spreadsheet used with Stellantis. The process was slow, prone to typing errors and lacked auditing — and the spreadsheet had formulas and validations that couldn't be broken.

## Solution

An end-to-end pipeline that monitors the Outlook/Microsoft 365 mailbox via Microsoft Graph, captures invoice attachments, extracts the data and automatically fills in the operational spreadsheet — with an admin panel for operations, a failure queue and configuration.

Layered extraction strategy (cost and reliability):

1. **NF-e XML** — deterministic parsing (primary source, zero AI cost)
2. **PDF text** — deterministic parsing when possible
3. **OCR/AI** — only when XML is missing/invalid and the PDF isn't parseable

Operational dashboard with quality and cost breakdowns: total received, success via XML, success without AI, processed with AI/OCR, failures with reason and manual reprocessing action.

## Architecture and technical decisions

- **FastAPI + a lightweight async worker** (simple scheduling, no distributed queue in the MVP — a conscious decision for operational simplicity)
- **Microsoft Graph** to read the monitored mailbox, with folder and parameters configurable from the frontend itself
- **Non-destructive spreadsheet writing**: inserts rows without breaking formulas, validations or out-of-scope columns — including an audited backfill with a prior backup (`backup_pre_backfill.sql`)
- **Attachments archived in a controlled directory** for auditing and reprocessing
- **PostgreSQL** for a complete processing trail (what came in, how it was extracted, what failed and why)
- **Documented AI fallback plan** (`plano-fallback-ia-extracao-nf.md`): AI as a last resort, with separate metrics on the dashboard to control cost
- Secrets exclusively on the backend; the frontend never sees the token/client secret
- React + TypeScript + Vite for the panel; Docker Compose with variants for Hostinger, Oracle and ngrok (demo)

## Challenges and solutions

- **Reliability over "AI magic"**: a deterministic-first hierarchy made AI cost marginal and the success rate auditable per breakdown on the dashboard.
- **Live spreadsheet shared with the end client**: surgical writes preserving the artifact the operation already used — adoption without a change in habits.
- **Operational business rules** (dealership CNPJ → pickup point): implemented as automatic enrichment of the extracted data.

## Results and impact

- Eliminated manual invoice entry into the operational spreadsheet [volume/day TO CONFIRM]
- Full auditing: every processed invoice has its origin, extraction method and result recorded
- Controlled AI cost: most documents resolved via deterministic parsing [percentage TO CONFIRM on the dashboard]

## Interview highlights (STAR summary)

- **S/T:** the logistics operation manually fed the Stellantis demand spreadsheet from invoices received by e-mail. **A:** I built a FastAPI + Graph API pipeline with layered extraction (deterministic XML → PDF → AI/OCR as fallback), non-destructive spreadsheet writing and a panel with a failure queue. **R:** end-to-end automated process in production, with full auditing and AI used only where necessary — controlling cost and maintaining the operation's trust.
