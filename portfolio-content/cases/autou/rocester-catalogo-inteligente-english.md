---
title: AI-powered parts catalog with PDF ingestion
client: Rocester
category: autou
status: Production
stack: [FastAPI, React, Gemini Vision, pgvector]
order: 6
gallery: rocester
---

# Case — Rocester (Intelligent Digital Catalog of Industrial Parts)

**Type:** AutoU (client: Rocester — industrial parts)
**Role:** Full Stack / AI Developer — involved in founding the project (architecture and initial functional base)
**Status:** Live (in production); further evolution on the roadmap
**Stack:** Python, FastAPI, React + TypeScript, PostgreSQL (pgvector enabled), Gemini Vision (PDF extraction), JWT with roles, Docker Compose, ReportLab (roadmap), full-text search (RAG)

> Confidentiality note: AutoU client project — validate what can be made public before exposing name/details.

## Context and problem

Rocester's salespeople looked up parts catalogs in scanned supplier PDFs: finding a part, checking the OEM code and putting together a quote was slow and error-prone. Digitizing the catalogs manually was unfeasible given the volume.

## Solution

A platform that turns catalog PDFs into an AI-searchable database:

- **PDF ingestion pipeline with Gemini Vision**: catalog upload → structured part extraction (code, OEM, description, category, equipment) with `temperature=0.1`, JSON mode and retries
- **Confidence score per part (0.0–1.0) with textual reasoning**: extracted parts enter as pending; a review panel with **bulk actions** (approve/reject) for efficient human curation
- **Search and filters** by code, OEM, description, category and equipment
- **Quotes**: cart, automatic code (`ORC-AAMM-XXXX`), history
- **AI assistant (chat)**: free-text part suggestions with RAG over the real catalog

## Architecture and technical decisions

- **Dependency inversion in the AI layer**: the domain doesn't know the LLM provider — swapping Gemini for another model doesn't touch the business logic (documented in the README architecture)
- **Explicit part lifecycle**: extracted → pending review → approved/rejected — AI proposes, human disposes; the public catalog only contains curated data
- **Extraction with anti-hallucination controls**: low temperature, strict JSON output, retries and a confidence score with a justification per item
- **JWT with roles** (`admin` / `seller`): sellers search and quote; admins import and curate
- **pgvector already enabled** in the database for evolving toward semantic search via embeddings (documented roadmap, including asynchronous ingestion processing and PDF quote export)
- Technical-commercial proposal and project plan versioned alongside the code

## Challenges and solutions

- **Heterogeneous supplier PDFs** (tables, images, varying layouts): multimodal Vision + bulk human review balance automation and accuracy
- **Seller trust in the data**: score + reasoning per part make "how sure is the AI" visible instead of hidden

## Results and impact

- PDF catalogs become a searchable base with no manual data entry
- Quotes assembled in the same flow as the search — less tool-switching for the seller
- Bulk curation reduces the human cost of validating AI extraction

## Interview highlights (STAR summary)

- **S/T:** salespeople depended on scanned PDFs to find parts and put together quotes. **A:** I took part in founding the platform — architecture with an AI layer decoupled via dependency inversion, and the functional base of the extraction pipeline via Gemini Vision (JSON mode, confidence score with reasoning), a review panel with bulk actions, quotes and a RAG assistant. **R:** a solid foundation turning a static catalog into structured, curated data, with a clear path to vector search (pgvector already provisioned).
