---
title: AutoU institutional website — SEO, blog, leads and custom CMS
client: AutoU
category: autou
status: Live
stack: [React, FastAPI, Azure]
order: 8
---

# Case — AutoU Website (Institutional Website with SEO and Lead Capture)

**Type:** AutoU (internal product — the company's digital presence)
**Role:** Full Stack Developer — solo project (the entire website, including the CMS)
**Status:** Live (in production)
**Stack:** Vite + React + TypeScript, FastAPI + Pydantic, PostgreSQL (Aura instance), custom CMS for articles/cases, SSG/ISR for SEO, Microsoft Graph (app registered in Azure) for receiving e-mails, Docker Compose, Microsoft Azure, Nginx

## Context and problem

AutoU's institutional website needed to be rebuilt with a focus on SEO (blog, success cases, indexing), lead capture integrated with the internal ecosystem, and an evolutionary path toward a CMS — without locking the company into a third-party platform.

## Solution

A monorepo with a public, SEO-optimized frontend, a lean backend and a CMS — built by me end to end:

- **Frontend**: a public site with a blog and cases (`/blog`, `/cases` with pagination and slugs), content consumed through a decoupled service layer (`getBlogPosts`, `getCases`)
- **Content CMS**: article and success-case management implemented (`PLANO-CMS-ARTIGOS-CASES` plan), letting the team publish without depending on a developer
- **FastAPI backend**: leads API (+ health), persistence in the Aura ecosystem's Postgres, transactional e-mail for the internal team only
- **E-mail → CRM funnel integration**: e-mail reception via **Microsoft Graph** (app registered in Azure) with automatic registration in the CRM funnel — a contact arriving by e-mail enters the same funnel as leads captured through the site
- **Rendering strategy per content type**: SSG for institutional/MDX content, ISR once the CMS is in place, SSR only if necessary — decision documented in an ADR
- **Operational SEO**: indexing guide, SEO/SSR/cache plan and design adjustments from Figma versioned in the repo

## Notable technical decisions

- **Decoupled content layer**: a content-access contract defined before the CMS existed — pages didn't change when content migrated from local MDX to the CMS
- **Deployment on Azure on the Aura infrastructure** (an explicit decision to move away from Vercel), with local Docker Compose and CI on GitHub Actions
- Feature-based frontend architecture with atomic design; backend in DDD-light modules

## Results and impact

- Institutional website with indexable blog/cases feeding the sales funnel — significant daily traffic and recurring lead generation (internal company figures)
- Leads integrated directly into the internal ecosystem's Postgres (Aura CRM)
- E-mails received automatically registered in the CRM funnel (via Microsoft Graph), with no manual inbox triage

## Interview highlights (STAR summary)

- **S/T:** the institutional website needed strong SEO, a blog/cases and lead capture with no dependency on a third-party platform. **A:** I worked on the Vite/React + FastAPI monorepo with a decoupled content layer (MDX→CMS with no rewrite), an SSG/ISR strategy documented in an ADR, Azure deployment and e-mail integration via Microsoft Graph (app registered in Azure) feeding the CRM funnel. **R:** an architecture ready to scale content and capture leads through two channels — the site's form and incoming e-mails — integrated into the internal CRM funnel.
