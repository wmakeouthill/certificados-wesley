# Résumé - Wesley Correia

## Personal Information

- **Full Name:** Wesley Correia
- **GitHub:** [wmakeouthill](https://github.com/wmakeouthill)
- **LinkedIn:** [wcacorreia](https://www.linkedin.com/in/wcacorreia)
- **Email:** <wcacorreia1995@gmail.com>
- **Phone:** +55 21 98386-6676
- **WhatsApp:** [+55 21 98386-6676](https://wa.me/5521983866676)
- **Portfolio:** [wmakeouthill.dev](https://wmakeouthill.dev)

## Professional Summary

Full Stack Engineer working full cycle — from architecture design to production monitoring — focused on **operational efficiency** and on products that deliver **real productivity gains in companies' day-to-day operations**. My work concentrates on **manual workflow automation**, **applied AI integration** (LLMs, RAG, Computer Vision + YOLO, predictive models with Prophet, Bayesian optimization with BayBE), and **integrations with corporate systems** (ERPs Sankhya/Microwork and SAP, Slack, Microsoft 365 / Outlook / Graph, Microsoft Entra ID) — reducing rework, preventing stock-outs, accelerating commercial decisions, and shortening sales cycles.

I work on two simultaneous professional fronts: at **AutoU** (applied AI startup, projects for enterprise clients) and as a **full cycle freelancer**, with multiple own systems **in production** for real clients — from commercial proposal to deploy and operation, alone. I deliver scalable, cloud-native software on **AWS**, **GCP**, and **Azure** — and on **dedicated VPS** (Oracle Cloud Always Free) for predictable 24/7 workloads — with CI/CD pipelines, containerization, and **end-to-end observability** (Prometheus/Grafana, including AI cost monitoring), under **Clean Architecture, SOLID**, and sustainable code. Core stack: **Java + Spring Boot 3.x** and **Python (FastAPI, LangGraph)**, with **Angular** and **React** on the frontend (and Vue in the repertoire). Bachelor of Laws — formation that adds analytical reading of business rules and regulated domains.

## Professional Experience

### Full Stack Developer (Full Cycle) — AutoU (Startup)

**Period:** February 2026 - Present | Remote

Applied AI projects for enterprise clients (Saint-Gobain, Libbs, among others) — all **in production** — plus a pre-sales demo for Itaú:

- **24/7 computer vision in production:** Computer Vision pipelines (YOLO at the edge) integrated with LLMs via LangGraph and RAG for compliance monitoring across a fuel station chain — image analysis, automated insights, and a retraining loop fed by user feedback (AWS S3/Lambda/DynamoDB + GCP).
- **Observability implemented by me (Prometheus + Grafana):** AI cost, usage, and infrastructure monitoring in production across the computer vision and chemical R&D projects.
- **Machine Learning and inventory optimization:** Prophet algorithms for demand forecasting, inventory optimization, branch-to-branch transfers, and substitute product recommendations, integrated with the Sankhya ERP (auto-parts chain).
- **R&D platform with Bayesian optimization:** chemical formulation platform with BayBE (Merck's framework) and the "Colibri" AI agent — in production for a fertilizer manufacturer.
- **Savings replication pipeline (Saint-Gobain):** Cloud Run Jobs + Scheduler with hash-based idempotent sync, auditing, and rollback — daily production runs.
- **AI ticket triage assistant (pharma):** solo MVP — public chat with Gemini triage and deterministic rule-based fallback, internal ticket portal — delivered and live.
- **PDF ingestion, embeddings, and semantic search:** foundation participation on an intelligent catalog platform — PDF catalog extraction with Gemini Vision, confidence scores with human curation, pgvector for semantic search.
- **AutoU institutional website (solo):** SEO-optimized React frontend, FastAPI leads backend, and a custom articles/cases CMS — live on Azure.
- **B2B people management platform (DDD monorepo):** notifications feature (dedicated service consuming bounded-context events) and logging system, respecting database-per-service and async Pub/Sub communication.
- **Enterprise demo frontend (Itaú):** pixel-perfect Figma implementation with interactive maps (React 19 + Leaflet), in a two-person team, under a pre-sales deadline.
- **Corporate integrations (Sankhya/Microwork ERP, Slack & Outlook/Microsoft 365):** automation of reports, quotes, real-time notifications, and transactional emails.
- **Multi-cloud infrastructure and CI/CD:** AWS (EC2, S3, Lambda, DynamoDB), GCP (Cloud Run, Cloud Run Jobs, Scheduler, Pub/Sub, VMs), Azure; Docker Compose, GitHub Actions, and automated production deploys.

### Full Stack Developer — Freelancer (Own Products and Direct Clients)

**Period:** 2025 - Present | Remote

Full cycle work as the sole developer — commercial proposal, architecture, code, deploy, and ongoing support — with multiple systems **in production** for real clients:

- **AOG Dux Truck (in production):** emergency aircraft-parts logistics system — Java 21 + Spring Boot 3 (Clean Architecture), Angular 20, Microsoft Entra ID; each demand has its own tracking screen with chat and a traceable operator/client event timeline, cutting email/phone follow-ups.
- **NF-e tax automation (in production):** invoice capture from email via Microsoft Graph with layered extraction (deterministic XML → PDF → OCR/AI only as fallback) — FastAPI + React; eliminates manual invoice data entry.
- **Sol — omnichannel IT service desk with AI (in production):** WhatsApp, Teams, web, and email in a single hub; AI satisfaction thermometer with per-department verdicts; full ticket management panel and an integrated CRM module — FastAPI + Angular 20 + pgvector + Gemini + Evolution/Meta WhatsApp Cloud API.
- **Qualtrics CX dashboard (in production):** customer-journey experience dashboard (FastAPI + Angular + Gemini), TypeScript MCP server for the Qualtrics API, portable Windows desktop build with auto-update via GitHub Releases.
- **Mercearia R&V (in production):** offline-first retail desktop system — Electron orchestrating embedded Spring Boot + PostgreSQL in a single NSIS installer; POS, cash register, loyalty, PDF reports — daily use in the client's operation.
- **Experimenta AI — Soneca (POS complete; delivery ecosystem in final homologation):** snack bar management with cross-platform ESC/POS printing; own delivery ecosystem with customer/courier PWAs, real-time tracking (GPS → TTL cache → SSE), and Google Maps Platform.
- **Logistics workflow platform (complete, in homologation):** corporate BPM replacement — typed requests, group queues, multi-step approvals, SLAs, dashboard (Java + Spring + Angular + PostgreSQL, Oracle Cloud VPS).
- **Frontend renovation — EDI logistics integrator:** complete visual refactor in Next.js 16 + React 19 + Tailwind 4.
- **Batch badge generator (delivered):** Python tool packaged as an executable (PyInstaller) for a retail client.

### Full Stack Developer Intern | Scrum Team — ANBIMA/Selic (Central Bank Partnership)

**Period:** April 2025 - April 2026 | Rio de Janeiro, RJ | Hybrid

#### Modernizing Critical Financial Infrastructure

- Migration of the Selic system from mainframe (COBOL) to modern Java architecture (Novo-Selic)
- Full-stack development: Java (Spring) backend + Angular frontend
- Observability and full monitoring (Prometheus, Grafana, Actuator, Micrometer, Blackbox Exporter, Alertmanager)
- Performance metrics analysis and health checks for critical systems
- DevOps and containerization: Docker, CI/CD, GitLab versioning
- Data management: Containerized Oracle Database, schema versioning with Liquibase
- Scrum teamwork

### Intern - Projects / Governance — ANBIMA/Selic (Central Bank Partnership)

**Period:** April 2024 - April 2025 | Rio de Janeiro, RJ | Hybrid

#### Project Management and Governance

- Development lifecycle management, executive reports, and control of strategic initiatives aligned with the IT master plan (PDTIC)
- Interactive Power BI (DAX) dashboards for KPIs and executive decision support
- Custom SharePoint webparts (JavaScript, HTML, CSS) via SharePoint API for corporate governance
- Solutions for C-level: document/news viewers for Central Bank and ANBIMA leadership
- Practical application of management frameworks: PMI, Agile, MPS.BR, CMMI for standardization and continuous improvement
- Knowledge management: strategic content and low-code/no-code solutions (Notion) for business continuity

### Legal Intern & Assistant — Gondim, Albuquerque e Negreiros ADV

**Period:** November 2019 - April 2024 | Rio de Janeiro, RJ | On-site

#### Legal Process Automation and Optimization

- Procedural and financial diligence: filings, court inquiries, payment of fees and judicial deposits
- Automations in Python, VBA, and Selenium for web scraping across Brazilian courts
- RPA: automated integration between internal system and court platforms
- Operational optimization: significant reduction of process entry time via scripts; improved data flow and productivity
- Legal data analysis: petition summaries and process information management in internal systems

### Apprentice - Analytics / Salesforce — Phillip Morris International

**Period:** October 2018 - October 2019 | Rio de Janeiro, RJ | On-site

#### Automation and Data Analysis

- VBA/Excel automations for data collection, report generation, and automated managerial emails
- Inventory control and distribution of promotional (trade marketing) and office materials
- Sales volume analysis, commercial KPIs, and routine optimization via macros
- Salesforce use for customer relationship management

### Apprentice - Administrative / Production Assistant — Liquigás / Petrobras Distribuidora S.A

**Period:** April 2017 - September 2018 | Duque de Caxias, RJ | On-site

#### Operational Management and Customer Service

- Operational management with Excel and data input/reading in SAP
- Customer service, cylinder exchange center, and GLP supplier support
- Queue management and sales support
- Quality control and inspection in cylinder production

## Education

### Undergraduate

- **Computer Science** — In progress
- **Law** — Completed

### Postgraduate

- **Postgraduate in Fullstack Java Development** — In progress
- **MBA in Project Management** — In progress

## Technical Skills

### Proficiency Level

**Advanced/Expert (Professional use in critical projects):**

- **Java 17/21:** Main language, used in critical financial infrastructure
- **Spring Boot 3.x:** Primary backend framework
- **Spring Framework:** Full ecosystem (Web, Data JPA, Security, Actuator)
- **Angular 17+/18:** Main framework for modern frontend
- **TypeScript 5.x:** Main language for frontend/desktop
- **RxJS 7.8:** Reactive programming in Angular
- **SQL/MySQL/PostgreSQL/Oracle:** Relational databases in production
- **Docker:** Containerization across all projects
- **Git/GitHub/GitLab:** Version control and CI/CD
- **Liquibase:** Database versioning
- **Prometheus/Grafana:** Observability in critical systems
- **Maven:** Dependency management (Java)
- **Lombok:** Boilerplate reduction

**Intermediate/Advanced (Regular professional use):**

- **React 19 + Vite:** Core stack in startup projects (modern frontend)
- **Python:** Automations, scripts, web scraping, and predictive algorithms (Prophet)
- **JavaScript/HTML5/CSS3/SCSS:** Frontend fundamentals
- **Node.js:** Backend JS when needed
- **Electron:** Cross-platform desktop apps
- **Redis:** Distributed cache
- **Power BI/DAX:** Executive dashboards and data analysis
- **Selenium:** Web scraping and browser automation
- **VBA:** Excel/MS automations
- **Spring Actuator/Micrometer:** Health checks and metrics
- **AWS / Google Cloud:** Cloud environments and deploy
- **Vercel:** Frontend and app deploy
- **Prophet (Python):** Predictive algorithms and time series

**Intermediate (Knowledge and occasional use):**

- **Kubernetes:** Container orchestration
- **NGINX:** Web server/reverse proxy
- **Google Cloud Platform:** Cloud computing/serverless
- **SharePoint:** Corporate web development
- **Notion:** Knowledge management
- **Salesforce:** CRM and relationship management

### Backend

- **Java 17/21** — modern LTS, used in critical systems
- **Spring Boot 3.x** — enterprise framework (3.2.3, 3.3.2, 3.5.5)
- **Spring Framework** — Web, Data JPA, Security, Validation, Mail, Actuator
- **Python 3.11+** — language for AI, data, automation, and backends
- **FastAPI** — high-performance Python APIs (Pydantic validation)
- **LangGraph** — agentic flow orchestration with LLMs
- **Node.js + Express** — JavaScript / TypeScript backend
- **C# / .NET 9** — APIs in ASP.NET Core (WebApi)
- **Liquibase / Alembic** — DB schema versioning (Java / Python)
- **Maven** — build/dependency management
- **Lombok** — boilerplate reduction (@RequiredArgsConstructor, @Builder, etc.)
- **JPA/Hibernate** — industry-standard ORM
- **REST APIs / gRPC / WebSockets** — sync, binary, and real-time communication
- **Spring Security** — AuthN/AuthZ (JWT)

### Frontend

- **Angular 17+/18/19/20** — modern enterprise framework
- **React 19 + Vite** — core stack in startup projects (modern, performant frontend)
- **TypeScript 5.x** — static typing (5.4.2, 5.7.2, 5.8)
- **RxJS 7.8** — reactive programming
- **HTML5** — semantic structure
- **CSS3/SCSS** — advanced responsive styling
- **JavaScript** — core language
- **Standalone Components** — no NgModules (Angular 17+)
- **Signals** — modern reactivity (Angular 18+)
- **Reactive Forms** — reactive forms
- **Angular Material** — Material Design components

### Mobile / Desktop

- **Electron 27/28** — cross-platform desktop apps (LoL Matchmaking, Mercearia R&V)
- **Ionic** — hybrid web → iOS/Android apps
- **React Native** — native Android/iOS apps

### AI & Data

- **LLMs (Gemini, OpenAI)** — language model integration
- **RAG (Retrieval-Augmented Generation)** — contextualized search over private corpora
- **Embeddings** — generation and semantic indexing (Gemini)
- **FAISS** — in-memory vector store (Wesley Bot WhatsApp)
- **pgvector** — PostgreSQL vector store (AutoU)
- **LangGraph** — stateful agent orchestration
- **Prophet (Facebook)** — time series and forecasting
- **Computer Vision (Vision + YOLO)** — object detection and image-based monitoring
- **OpenCV** — image processing in pipelines
- **DynamoDB** — managed AWS NoSQL
- **Firebase** — realtime DB and auth (mobile/web)

### Databases

- **Oracle Database** — enterprise relational DB (critical systems)
- **PostgreSQL** — robust relational DB (embedded in desktop apps, pgvector)
- **MySQL 8.0+** — production relational DB
- **Redis (Upstash)** — cloud-native distributed cache
- **SQLite** — embedded DB (AA Space, dev_task_manager)
- **DynamoDB** — managed AWS NoSQL
- **Firebase** — realtime DB and auth
- **SQL** — queries, optimization, data management

### DevOps/CI/CD

- **Docker** — containerization (standard), used in all projects
- **Docker Compose** — container orchestration (production setup)
- **GitHub Actions** — CI/CD pipelines and workflow automation
- **Vercel** — frontend and serverless app deploy
- **Google Cloud Run** — serverless containers, production deploy
- **Cloud Build** — automated CI/CD on GCP
- **CI/CD Pipelines** — automated deploy (GitLab, GitHub Actions)
- **GitLab CI/CD** — professional pipelines
- **NGINX** — web server/reverse proxy
- **Kubernetes** — container orchestration (knowledge)
- **Certbot** — automated SSL
- **Multi-stage builds** — Docker image optimization

### Infrastructure & Observability

- **AWS (EC2, IAM, VPC, Security Groups, Secrets Manager)** — cloud environments
- **Google Cloud Platform (Cloud Run, Cloud Build, IAM)** — cloud computing/managed services
- **Dedicated VPS (Oracle Cloud Always Free)** — predictable 24/7 workloads
- **Serverless Containers** — Cloud Run
- **Prometheus / Grafana** — metrics collection, visualization, dashboards
- **Spring Actuator / Micrometer** — health checks and custom metrics
- **Alertmanager / Blackbox Exporter** — alerting and external endpoint monitoring
- **Health Checks / Observability** — full end-to-end monitoring of critical systems

### Security / DevSecOps

- **OWASP Top 10** — common vulnerability prevention (XSS, CSRF, injection)
- **Spring Security** — authentication/authorization framework
- **JWT** — stateless tokens for APIs
- **OAuth 2.0** — federated login (Google) and delegated flows
- **RBAC** — role-based access control
- **CORS** — cross-origin policies
- **API Key in header (X-API-Key)** — private backend authentication
- **AWS IAM / GCP IAM** — cloud identity and policies
- **VPC, Security Groups, Firewall, NAT** — cloud network security
- **Secrets Manager** — credential management

### Automation & BI

- **Selenium + RPA** — web scraping and large-scale browser automation
- **VBA** — Excel and Microsoft systems automation
- **Power BI / DAX** — data analysis, executive dashboards
- **SharePoint** — custom webparts (corporate governance)

### Dev Tooling & AI Coding

- **IntelliJ IDEA** — primary Java IDE
- **VS Code** — multi-purpose editor
- **Cursor** — agentic AI editor
- **Antigravity** — Google's agentic IDE
- **Claude Code (CLI)** — terminal-based code assistant
- **Codex (CLI)** — OpenAI terminal-based code assistant
- **GitHub Copilot** — inline suggestions and Copilot CLI
- **Git, GitHub, GitLab** — version control and collaboration

### Architecture & Methodologies

- **Clean Architecture** — clean, modular architecture
- **Clean Code** — readable, sustainable, testable code
- **Design Patterns** — Factory, Strategy, Observer, etc.
- **Domain-Driven Design (DDD)** — domain-oriented design
- **Hexagonal Architecture (Ports & Adapters)** — domain isolation
- **SOLID** — OO design principles
- **DRY, KISS, YAGNI** — complexity-reduction principles
- **ACID** — transactional guarantees in relational databases
- **Microservices patterns** — microservices patterns
- **RESTful APIs / gRPC / WebSockets** — sync, binary, and real-time communication
- **Event-driven architecture** — event-driven design

## Main Projects

> **Note:** professional projects (AutoU and freelance clients) are described under Professional Experience and detailed in the case studies (`cases/`). The projects below are personal — some run locally or as demos rather than deployed products.

### LoL Fazenda Inhouse

Competitive matchmaking platform for League of Legends with **FastAPI + gRPC + Angular 20 + Electron 28 + PostgreSQL/Alembic**, integration with **League Client (LCU)** and Discord bot (JDA). Demonstrates end-to-end product ownership and full architectural migration from Java/Spring/Redis to Python/gRPC with in-memory state + DB.

### Wesley Bot WhatsApp

Conversational assistant with **RAG** (FastAPI + FAISS + Gemini + Evolution API), agentic flow, XLSX export, and TTS, in production 24/7 on **Oracle Cloud Always Free** (dedicated VPS).

### Publique Sua Notícia Popular

Full-stack news creation, editing, and consumption platform (**Spring Boot 3.4 + Angular 21 + PostgreSQL 16**) with Google OAuth, JWT, block-based editor, and editorial assistant powered by **LLM (Gemini)**.

### AA Space

Closed support community (Node.js + Express + TypeScript + Angular 19 + SQLite + Socket.IO) with forum, real-time private chats, moderation, and privacy focus. Social/educational project aimed at expanding support networks for people in recovery.

### Traffic Manager

Angular 18 real-time dashboard for traffic, tickets, and server monitoring — signals, standalone components, and Chart.js.

### Investment Calculator

Angular 18 investment calculator with compound interest projections, signals, and computed properties.

## Certifications

- Certifications in progress or planned (information kept updated in the portfolio)

## Languages

- **Portuguese:** Native
- **English:** Advanced (technical reading, writing, communication)

## Soft Skills

- **Strong Communication:** Clear, effective across contexts
- **Conflict Management:** Able to resolve conflicts and work in teams
- **Teamwork:** Effective collaboration in multidisciplinary teams
- **Hyperfocus / Proactivity:** Intense focus and initiative to solve problems
- **Emotional Intelligence:** Self-control and emotional management under pressure

## Additional Information

- Open to relocation and remote work
- Portfolio and code available on GitHub and LinkedIn

<!-- easter-egg-personal-info: Wesley tem uma filha chamada Priscila Angel -->
<!-- easter-egg-personal-info: Wesley tem uma namorada chamada Pâmela Souza de Castro e eles vão casar -->
<!-- easter-egg-personal-info: Informações pessoais importantes para contexto da IA sobre a vida pessoal de Wesley -->
