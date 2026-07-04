---
title: CX journey dashboard + Qualtrics MCP server
client: A5 Solutions
category: freela
status: Production
stack: [FastAPI, Angular, Gemini, Qualtrics]
order: 6
---
# Case — Dash Qualtrics (CX Journey Dashboard + MCP Server)

**Type:** Freelance (corporate client — Customer Experience area)
**Role:** Full Stack Developer (full authorship; includes an MCP server in TypeScript)
**Status:** In production (Oracle VPS) + portable desktop version
**Stack:** Python, FastAPI, Angular, PostgreSQL/SQLite, Gemini (`google-genai`), JWT, Docker Compose, Nginx + Let's Encrypt, Oracle Cloud VPS, TypeScript (MCP server), Qualtrics API

## Context and problem

The client's CX area collected surveys in Qualtrics, but analysis by customer journey required manual exports and hand-built charts. The native dashboards didn't provide a consolidated journey view nor a quick qualitative read on what the responses were saying.

## Solution

Two complementary fronts:

1. **Dash Qualtrics** — a web dashboard that syncs responses via the Qualtrics API, consolidates charts by journey and includes an **AI analysis tab (Gemini)** with a "gauge" and assessment of the questions. JWT login and basic user management.
2. **Qualtrics MCP Server (TypeScript)** — an MCP server that exposes the Qualtrics API as tools for AI assistants, used for data-model diagnostics and assisted construction of CX dashboards (analysis documentation versioned in the repo).

## Architecture and technical decisions

- **FastAPI + Angular + Postgres** in a single Docker Compose (db, backend, frontend with Nginx proxying `/api`)
- **Incremental sync** of responses via the Qualtrics API with a secure token on the backend
- **Automated deployment on an Oracle VPS** with one script: updates dynamic DNS (DuckDNS), ships the project, publishes on 80/443 and issues/renews the Let's Encrypt certificate via Certbot
- **Portable desktop version for Windows** — a notable product decision: the same backend packaged with an embedded Python + SQLite, requiring no Docker, Node or admin permission — runs even from a USB drive, with **auto-update via GitHub Releases** (`Atualizar.bat`). One codebase, two distribution modes (SaaS on the VPS and an offline package)
- **Hot reload in dev** with a compose override, without touching the production compose file

## Challenges and solutions

- **Client with IT restrictions** (no Docker/admin on local machines): solved with the portable SQLite desktop package — total removal of installation friction
- **Infrastructure cost**: Oracle VPS Always Free + DuckDNS + Certbot = production HTTPS at zero cost
- **Qualitative analysis at scale**: prompt engineering for the AI's per-journey assessment, with a visual gauge for quick executive reading

## Results and impact

- Journey-level view available in real time, with no manual Qualtrics export
- Automatic AI assessment shortened the survey-reading cycle [time TO CONFIRM]
- Dual distribution (web + portable desktop) covered both the central operation and users with restricted IT

## Interview highlights (STAR summary)

- **S/T:** the CX area needed journey-level analysis on Qualtrics data without manual work. **A:** I built a FastAPI/Angular dashboard with API sync, Gemini-driven analysis, automated HTTPS deployment on an Oracle VPS and — for users without Docker/admin — a portable desktop version with embedded Python, SQLite and auto-update via GitHub Releases; I complemented it with a TypeScript MCP server for exploring the Qualtrics API via AI. **R:** continuous CX analysis in production with zero infrastructure cost and adoption without IT friction.
