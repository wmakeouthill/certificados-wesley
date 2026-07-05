---
title: Pulse — Gas station compliance with computer vision
client: Rede São Roque
category: autou
status: Production
stack: [YOLO, FastAPI, LangGraph, Gemini, AWS]
order: 2
---

# Case — Pulse (Gas Station Compliance with Computer Vision)

**Type:** AutoU (client: Rede São Roque — gas station chain)
**Role:** Full Stack / AI Developer — computer vision pipeline, backend, deployment and observability; technical lead of project workstreams (team project), with direct client contact in weekly checkpoints and ad-hoc alignment sessions
**Status:** In production (edge agent 24/7 at the stations)
**Stack:** Python, YOLO (detection), FastAPI, React, PostgreSQL, LangGraph + Gemini via `google-genai` (agentic pipeline), RAG, AWS (S3, Lambda, DynamoDB), Google Cloud (2 VMs), RTSP stream-worker, Prometheus + Grafana, Caddy, Docker Compose, Roboflow + Google Colab (retraining)

> Confidentiality note: AutoU client project — validate what can be made public before exposing name/details.

## Context and problem

The gas station chain needed to inspect visual compliance of its units (oil stains, litter, exposed cables, PPE) — currently dependent on on-site visits and sporadic photos. Without continuous detection, issues went untreated for days and management had no consolidated view.

## Solution

A continuous monitoring system with a full model-improvement cycle:

- **Edge Agent (PC at the station)**: consumes cameras via RTSP, runs YOLO 24/7, validates detections and uploads events
- **Cloud backend**: stores events and photos (S3, 1-year retention; DynamoDB for events/feedback), REST API with `resolve`, `false-positive` flows and dashboard
- **Agentic pipeline (LangGraph + Gemini via `google-genai` + RAG)**: analysis of detected occurrences and insight generation with GenAI, remediation steps, integration with an e-mail/WhatsApp flow for notification
- **React dashboard**: management approves/resolves occurrences and flags false positives
- **Retraining loop**: user feedback becomes a dataset (collection script), retraining in Colab with Roboflow, new model goes back to the edge — the system improves with use

## Architecture and technical decisions

- **Hybrid edge + cloud**: YOLO inference at the station (minimal bandwidth and latency — uploads an event, not video), consolidation and generative AI in the cloud
- **Pragmatic multi-cloud**: AWS for storage/events (S3/Lambda/DynamoDB), GCP for the application (deployed on 2 VMs with separate roles — app and stateful/observability)
- **Dedicated stream-worker** for RTSP capture decoupled from the backend — capture architecture decision: direct consumption of the station's existing Intelbras DVR via RTSP, with a **secure external port configured via NAT on the client's DVR** — reusing the camera hardware the station already had, with no new equipment cost
- **Real observability (implemented by me)**: Prometheus + Grafana on its own stateful VM — cost and compute budget monitoring, usage and infrastructure — with versioned snapshots and deployment plan
- **Agentic pipeline optimization** documented and executed (`PLANO_OTIMIZACAO_PIPELINE_AGENTICO.md`) — controlled LLM cost and latency
- **Global cache** planned/implemented to reduce reprocessing (`plano-cache-global.md`)
- Documented single-shot migration, versioned RAG seeds, local→GCP/EC2 sync scripts

## Challenges and solutions

- **False positives eroding trust**: a false-positive button on the dashboard feeds directly into the retraining dataset — user feedback became an ML asset
- **24/7 infrastructure with controlled cost**: separation of app/stateful into distinct VMs, defined retention (photos 1 year) and the edge doing the heavy inference work
- **Real-world operation (gas stations)**: reproducible setup via PowerShell/bash scripts to install new stations (`push-stations.ps1`)

## Results and impact

- Continuous 24/7 detection in production replacing sporadic on-site inspection — pilot live with **2 stations monitored** and planned expansion to the chain's **~50 stations**
- Continuous model-improvement cycle with real operational data
- Management with a consolidated dashboard of occurrences, remediation and false positives

## Interview highlights (STAR summary)

- **S/T:** a gas station chain with no continuous monitoring of visual compliance. **A:** I took part in building the edge-to-cloud system — capture via RTSP straight from the client's Intelbras DVR (secure external port via NAT), YOLO running at the station, events in AWS, LangGraph+Gemini agentic pipeline with RAG for analysis and notifications, React dashboard, Prometheus/Grafana observability with cost/compute-budget control and a retraining loop fed by user feedback. **R:** a production system detecting occurrences 24/7, with a model that keeps improving and a reproducible deployment operation on GCP.
