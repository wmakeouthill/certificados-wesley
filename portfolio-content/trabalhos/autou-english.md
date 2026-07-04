# Professional Experience - AutoU (Applied AI Startup)

## About AutoU

**AutoU** is a startup building **applied AI** solutions for companies — computer vision, AI agents, predictive models, and data platforms — with projects for enterprise clients such as **Saint-Gobain, Rocester, Oxiquímica, and retail/fuel chains** (plus enterprise demos, such as the pre-sales demo built for Itaú and the demo built to compete in an ongoing Libbs bid/RFP). The environment is fast-paced, with high client exposure and a focus on quality delivery at high velocity.

### Work Context

- Projects for large enterprises, **all in production**
- Core stack: **Python (FastAPI, LangGraph)** in the backend and **React 19 + Vite** in the frontend
- Multi-cloud infrastructure: **AWS** (EC2, S3, Lambda, DynamoDB), **Google Cloud** (Cloud Run, Cloud Run Jobs, Scheduler, Pub/Sub, VMs), **Azure**
- CI/CD and deploy: **GitHub Actions**, **Docker Compose**, automated deployments

## Experience at the Company

### Fullstack Developer

*Period: February 2026 - Present | Remote*

#### 24/7 Computer Vision in Production (fuel station chain)

- **YOLO pipeline running at the edge** (on-site PC consuming RTSP cameras), events consolidated in **AWS (S3, Lambda, DynamoDB)**
- **Agentic pipeline with LangGraph + Gemini + RAG** for incident analysis, insights, and email/WhatsApp notifications
- **Retraining loop**: user false-positive feedback becomes retraining dataset — the model improves with use
- **Observability implemented by me**: Prometheus + Grafana on a dedicated stateful VM, monitoring cost, usage, and infrastructure

#### Machine Learning and Demand Forecasting (auto-parts chain)

- Predictive algorithm with **Prophet** (time series) for per-product/per-branch demand forecasting
- **Purchase, inter-branch transfer, and substitute product recommendations**, integrated with the **Sankhya ERP**
- Automated daily execution in production

#### R&D Platform with Bayesian Optimization (chemical industry)

- Formulation platform using **BayBE** (Merck's open-source framework) to suggest the next formulation to test — fewer physical greenhouse cycles
- AI agent **"Colibri"** that generates and assists with formulas; scientific chat with **RAG and source governance** (whitelist/blacklist)
- **Grafana + Prometheus observability implemented by me**: AI cost, consumption, and infrastructure

#### Savings Replication Pipeline (Saint-Gobain)

- **Cloud Run Jobs + Cloud Scheduler** with **hash-based idempotent synchronization**, auditing, and rollback
- FastAPI admin backend; daily execution in production

#### AI Ticket Triage Assistant (demo for an ongoing Libbs bid/RFP — solo project)

- Full-stack MVP built alone as a demo to compete in the pharma company's bid: public chat with **Gemini-powered triage and deterministic rule-based fallback**, human handoff, internal portal with ticket timeline
- One application serving two domains (public chat + internal portal) — demo live; bid still in progress

#### Intelligent Parts Catalog (Rocester — project foundation)

- Foundation participation: architecture with a **decoupled AI layer** (dependency inversion) and the base of the **PDF extraction pipeline with Gemini Vision**
- Per-part confidence score with reasoning and **bulk human curation**; **pgvector** for semantic search — in production

#### AutoU Institutional Website (solo project)

- Complete site built alone: SEO-optimized React frontend (blog, cases), FastAPI leads backend, and a **custom CMS** — live on Azure
- **Email integration via Microsoft Graph** (Azure app registration): incoming emails are automatically recorded in the **CRM funnel**, in the same flow as leads captured through the site

#### B2B People Management Platform (Aura Central — DDD monorepo)

- **Notifications feature**: dedicated service consuming bounded-context events via Pub/Sub, without coupling domains
- **Platform logging system**, providing operational visibility in production
- Work within a **DDD architecture with 5 bounded contexts and database-per-service**

#### Enterprise Demo Frontend (Itaú — two-person team)

- Pixel-perfect interface from Figma with **interactive maps (React 19 + Leaflet)**, under a short pre-sales deadline

#### Corporate Integrations

- **Sankhya/Microwork ERP** via API: automation of reports, quotes, and sales flows
- **Slack**: real-time notifications; **Outlook / Microsoft 365**: transactional emails

**Technologies Used:**

- Python, FastAPI, LangGraph, Prophet, BayBE
- React 19, Vite, TypeScript
- LLMs (Gemini, Gemini Vision), RAG, pgvector, FAISS, YOLO
- AWS (EC2, S3, Lambda, DynamoDB), Google Cloud (Cloud Run, Cloud Run Jobs, Scheduler, Pub/Sub), Azure
- Prometheus, Grafana
- GitHub Actions, Docker, Docker Compose
- Sankhya/Microwork, Slack API, Microsoft 365 / Outlook

## Achievements and Learnings

- **Every project I worked on is in production** — from 24/7 computer vision to daily data pipelines
- Applied AI with engineering judgment: deterministic fallbacks, human curation, source governance, and retraining loops — never "AI for AI's sake"
- Production observability (Prometheus/Grafana) implemented on my own initiative, including **AI cost monitoring**
- Direct exposure to enterprise clients (Saint-Gobain) and enterprise pre-sales/bids (Itaú demo and Libbs bid demo) in a fast-paced startup environment
- ML beyond LLMs: time series (Prophet), computer vision (YOLO), and Bayesian optimization (BayBE)
