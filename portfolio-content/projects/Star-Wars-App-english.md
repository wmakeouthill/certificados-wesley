# 🌌 HOLOCRON ANALYTICS

> **"Where the Force of Data Meets the Wisdom of the Galaxy"**

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-5.6-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-9.5-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=for-the-badge&logo=openai&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-Frontend-000000?style=for-the-badge&logo=vercel&logoColor=white)
![GCP](https://img.shields.io/badge/Google_Cloud-Cloud_Run-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)

---

## 📑 Table of Contents

- [📜 Overview](#-overview)
- [📂 Project Structure](#-project-structure)
- [🏗️ Architecture and Performance Engineering](#️-architecture-and-performance-engineering)
- [🛠️ Engineering Behind the Scenes (Deep Dive)](#️-engineering-behind-the-scenes-deep-dive)
- [🗺️ Navigation and Features](#️-navigation-and-features)
- [🔗 Integration & Data Protocols (End-to-End)](#-integration--data-protocols-end-to-end)
- [📚 Technical Documentation (Deep Dive)](#-technical-documentation-deep-dive)
  - [🤖 AI & NLP Engineering](#-ai--nlp-engineering)
  - [🎮 Gamification Mechanics](#-gamification-mechanics)
  - [🚀 Production Deploy Guide](#-production-deploy-guide)
  - [🎨 UX & Frontend Architecture](#-ux--frontend-architecture)
  - [📐 Quality Assurance & Data Architecture](#-quality-assurance--data-architecture)
- [🛡️ Infrastructure & Security (DevSecOps)](#️-infrastructure--security-devsecops)
- [🔌 API Reference (Endpoints)](#-api-reference-endpoints)
- [🎨 Design System](#-design-system)
- [📋 Environment Variables](#-environment-variables)
- [💻 Detailed Tech Stack](#-detailed-tech-stack)
- [🚀 How to Run](#-how-to-run)
- [👨‍💻 Developer](#-developer)

---

## 📜 Overview

**Holocron Analytics** is an immersive and gamified platform built to explore the Star Wars universe. Far beyond a simple wiki, this project turns querying data from the public API (SWAPI) into a “Jedi Archivist” experience, using **Artificial Intelligence (OpenAI GPT-4o)** to enrich data, generate dynamic quizzes, and simulate interactions with Master Yoda.

### Key Features

- **🔍 Digital Holocron**: Advanced lookup for Characters, Films, Starships, Planets, Species, and Vehicles.
- **🤖 Master Yoda AI**: An integrated LLM-powered chatbot that answers questions about the galaxy with the iconic Jedi Master’s personality, using cached data for ultra-fast responses.
- **⚔️ Gamification & Jedi Trials**: A progression system where users climb ranks (Padawan -> Master) by completing challenges and quizzes.
- **📊 Visual Reports**: Detailed charts on species distribution, vehicles per film, and galaxy statistics.
- **🚀 Extreme Performance**: Advanced caching and background-loading strategies for instant navigation.
- **📱 Responsive Design**: Fully adaptive UI for desktop, tablet, and mobile with high-end UX.

---

## 📂 Project Structure

```
Star-Wars-App/
├── backend/                          # FastAPI API (Python)
│   ├── src/app/
│   │   ├── application/              # Application Layer (Use Cases)
│   │   │   └── services/             # Business services
│   │   │       ├── chat_service.py          # AI chat engine
│   │   │       ├── gamification_service.py  # XP and achievements system
│   │   │       ├── quiz_service.py          # AI quiz generation
│   │   │       └── rag_search.py            # Hybrid search engine (RAG)
│   │   ├── domain/                   # Domain Layer (DDD)
│   │   │   ├── entities/             # Business entities
│   │   │   ├── enums/                # Enumerations (JediRank, etc.)
│   │   │   ├── exceptions/           # Custom exceptions
│   │   │   ├── repositories/         # Repository interfaces
│   │   │   └── schemas/              # Pydantic schemas (DTOs)
│   │   ├── infrastructure/           # Infrastructure Layer
│   │   │   ├── cache/                # In-memory cache system
│   │   │   ├── config/               # Settings/config
│   │   │   ├── db/                   # SQLAlchemy models and connection
│   │   │   ├── external/             # External integrations
│   │   │   │   ├── openai/           # OpenAI client (GPT-4o)
│   │   │   │   └── swapi/            # SWAPI client
│   │   │   ├── security/             # JWT, auth handlers
│   │   │   └── etag_middleware.py    # HTTP cache middleware
│   │   └── interfaces/               # Interface Layer
│   │       └── api/v1/
│   │           ├── routers/          # API endpoints
│   │           │   ├── auth.py              # Google OAuth authentication
│   │           │   ├── characters.py        # Characters CRUD
│   │           │   ├── chat.py              # AI chat
│   │           │   ├── films.py             # Films CRUD
│   │           │   ├── gamification.py      # XP, Rank, Achievements
│   │           │   ├── health.py            # Health check
│   │           │   ├── image_fallbacks.py   # Image management
│   │           │   ├── metadata.py          # Metadata for filters
│   │           │   ├── planets.py           # Planets CRUD
│   │           │   ├── species.py           # Species CRUD
│   │           │   ├── starships.py         # Starships CRUD
│   │           │   └── vehicles.py          # Vehicles CRUD
│   │           └── dependencies/     # Dependency injection
│   ├── alembic/                      # DB migrations
│   │   └── versions/                 # Migration scripts
│   ├── tests/                        # Unit tests (Pytest)
│   ├── Dockerfile.cloud-run          # Production Dockerfile
│   ├── Dockerfile.dev                # Development Dockerfile
│   └── pyproject.toml                # Python deps (Poetry)
│
├── frontend/                         # React SPA (TypeScript)
│   ├── src/
│   │   ├── App/                      # Root component and navigation
│   │   ├── features/                 # Domain modules (Feature-based)
│   │   │   ├── auth/                 # Google authentication
│   │   │   │   ├── components/       # UserMenu, LoginButton
│   │   │   │   ├── context/          # AuthProvider, AuthContext
│   │   │   │   ├── pages/            # LoginPage, AuthLoadingPage
│   │   │   │   └── services/         # authService (API calls)
│   │   │   ├── characters/           # Characters module
│   │   │   │   ├── components/       # CharacterCard, CharacterModal
│   │   │   │   ├── hooks/            # useCharacters, useCharacterDetails
│   │   │   │   ├── pages/            # CharactersPage
│   │   │   │   └── services/         # charactersService
│   │   │   ├── chat/                 # AI Chat module
│   │   │   │   ├── components/       # YodaChatBubble, ChatModal
│   │   │   │   ├── context/          # ChatProvider
│   │   │   │   └── hooks/            # useChat, useChatHistory
│   │   │   ├── dashboard/            # Main dashboard
│   │   │   ├── films/                # Films module
│   │   │   ├── gamification/         # Gamification module
│   │   │   │   ├── components/       # QuizModal, AchievementCard
│   │   │   │   ├── hooks/            # useGamification, useQuiz
│   │   │   │   └── pages/            # GamificationPage
│   │   │   ├── planets/              # Planets module
│   │   │   ├── reports/              # Reports module
│   │   │   │   ├── components/       # Charts, LeaderboardTable
│   │   │   │   └── pages/            # ReportsPage
│   │   │   ├── species/              # Species module
│   │   │   ├── starships/            # Starships module
│   │   │   └── vehicles/             # Vehicles module
│   │   └── shared/                   # Shared code
│   │       ├── components/           # Reusable components
│   │       │   ├── CustomSelect/     # Custom Star Wars select
│   │       │   ├── FilmFilter/       # Global film filter
│   │       │   ├── PageLayout/       # Base page layout
│   │       │   ├── Pagination/       # Responsive pagination
│   │       │   ├── ScrollToTop/      # Back-to-top button
│   │       │   └── StarfieldEvents/  # Animated background
│   │       ├── hooks/                # Shared hooks
│   │       │   ├── useFilmOptions.ts        # Film options
│   │       │   ├── useMetadataOptions.ts    # Metadata for filters
│   │       │   └── usePrefetchAllData.ts    # 6-phase prefetch
│   │       ├── services/             # Shared services
│   │       │   ├── api.ts                   # Base HTTP client
│   │       │   └── metadata.service.ts      # Metadata service
│   │       ├── stores/               # Zustand stores
│   │       └── styles/               # Global styles
│   │           └── global.css        # CSS Variables, Starfield
│   ├── api/                          # Vercel Serverless Functions
│   ├── index.html                    # HTML entry point
│   ├── vite.config.ts                # Vite config
│   └── package.json                  # Node.js dependencies
│
├── regras-desenvolvimento-python-react/  # Standards documentation
│   ├── regras-backend.md             # Python/FastAPI standards
│   ├── regras-frontend.md            # React/TypeScript standards
│   └── regras-testes.md              # Testing standards
│
├── docker-compose.dev.yml            # Development compose
├── deploy-starwars.ps1               # GCP deploy script
└── README.md                         # This documentation
```

---

## 🏗️ Architecture and Performance Engineering

The solution was designed with an obsessive focus on performance and fluid UX, using an intelligent loading strategy and multi-level caching.

```mermaid
%%{title: "Performance and Cache Strategy"}%%
flowchart TD
    Init["🚀 App Initialization"] --> FastLoad["🔥 Critical Load"]
    FastLoad --> Render["🖥️ Immediate Render (Optimized LCP)"]
    
    Render --> Background["⏳ Background Loading"]
    Background --> FetchAll["📡 Massive Fetch from SWAPI"]
    FetchAll --> Process["⚙️ Processing & Enrichment"]
    Process --> Cache["💾 Local Cache (Memory)"]
    
    subgraph UX_Fluidity ["Smooth Navigation"]
        UserAction["🖱️ User Navigation"]
        UserAction -- "Data already in Cache" --> InstantServe["⚡ Instant Display"]
        UserAction -- "Chat/Quiz" --> ContextAware["🧠 Preloaded Context"]
    end
    
    Cache -.-> UX_Fluidity
```

### 🧠 Artificial Intelligence Pipeline

The AI integration is not just a “wrapper”. It actively fills data gaps and generates content.

```mermaid
%%{title: "AI Data Enrichment Pipeline"}%%
sequenceDiagram
    participant C as Client
    participant B as Backend
    participant DB as Database
    participant SW as SWAPI
    participant AI as Vertex AI (Gemini)

    C->>B: GET /characters/1 (Luke Skywalker)
    B->>DB: Lookup Local Cache
    
    alt Incomplete or Missing Data
        B->>SW: Fetch Basic Data
        SW-->>B: Raw JSON (SWAPI)
        B->>AI: Prompt: "Generate RPG stats for Luke"
        AI-->>B: Enriched JSON (Force: 85, Agility: 80...)
        B->>DB: Save/Update Record
    end
    
    B-->>C: Return Full Character + Stats
```

---

## 🛠️ Engineering Behind the Scenes (Deep Dive)

What sets **Holocron Analytics** apart is the attention to “invisible” technical details that make the experience magical.

### 1. 🔍 Search Optimization (NLP & RAG)

The search system (`rag_search.py`) implements a **Retrieval-Augmented Generation** engine that understands native Portuguese.

- **Hybrid Fuzzy Search**: Uses `rapidfuzz` (Levenshtein Distance) to correct typos ("Anakin Skywaler" -> Finds "Anakin Skywalker").
- **PT-BR Stemming**: A custom algorithm that removes suffixes (-inho, -mente, -ão) to understand search intent.
- **Entity Detection**: Smart heuristics distinguish when the user searches for a droid ("R2") vs. a generic term, avoiding false positives.
- **Synonyms**: Automatically maps terms like "sabre de luz" ↔ "lightsaber" or "robô" ↔ "droid".

### 2. 🧙 Persona Engineering (Prompting)

**Master Yoda AI** is not just a standard chatbot.

- **Dynamic Context**: The system injects official SWAPI data snippets into the model context to keep answers factual (Grounding), reducing hallucinations.
- **Syntactic Inversion**: The system prompt instructs the AI to mimic Yoda’s unique grammar (Object-Subject-Verb).
- **Multiple Personas**: The architecture supports persona switching, also enabling a "Darth Vader" persona that responds with hostility and forbidden emojis.

### 3. ✨ Cinematic Frontend

The UI was built for total immersion:

- **Dynamic Starfield**: The star background (`StarfieldEvents.tsx`) is not a looping video. It’s a procedurally-generated particle system simulating “space traffic”, with meteors varying in speed, angle, and depth.
- **Accessibility**: The system detects the OS `prefers-reduced-motion` preference and automatically disables heavy animations for motion-sensitive users.

---

## 🗺️ Navigation and Features

### 1. 🔍 Holocron (Data Exploration)

Dedicated pages for each Star Wars entity, with rich, interactive cards.

- **Pages**: `Characters`, `Films`, `Starships`, `Planets`, `Species`, `Vehicles`.
- **Advanced Filters**:
  - Filter by Name, Gender, Climate (Planets), Class (Starships), and more.
  - Fuzzy (approximate) search to find terms even with typos.
  - Dynamic sorting and instant pagination (client-side pagination thanks to preloading).

### 2. 📊 Reports and Analytics

Located in the `reports` folder, this section provides visual insights through interactive charts.

- **Species Distribution**: Pie/bar charts showing the diversity of the galaxy.
- **Starship Comparison**: Scatter plots comparing speed vs. cost.
- **Timeline**: Visual timeline of films and events.

### 3. ⚔️ Full Gamification

The system keeps users engaged through a levels and rewards system.

- **Jedi Trials**: AI-generated quizzes that test knowledge.
- **XP Bar**: Earn experience by exploring the system, completing quizzes, and discovering “easter eggs”.
- **Rankings**: Start as *Youngling*, become *Initiate*, *Padawan*, *Knight*, and finally *Jedi Master*.
- **Achievements**: Unlockable badges (e.g., "Visited all planets", "Answered 10 questions in a row").

### 4. ⚡ Phased Loading Strategy (6-Phases Prefetch)

To ensure an “instant” experience, the frontend (`usePrefetchAllData.ts`) implements a 6-stage **hydration pipeline** that runs silently in the background:

1. **Phase 1 (Critical)**: Dashboard (LCP). Loads data for Home.
2. **Phase 2 (Navigation)**: First 3 pages of ALL listings (Characters, Starships, etc).
3. **Phase 3 (Rich Content)**: Full details of all films.
4. **Phase 4 (Big Data)**: Loads massive datasets (100+ items) to generate the Reports charts.
5. **Phase 5 (Social)**: User profile, achievements, leaderboard, and daily challenges.
6. **Phase 6 (Bulk Quiz)**: Downloads hundreds of potential questions so Jedi Trials works offline/without delay.

*All of this happens without blocking the main thread, using `setTimeout` and React Query priority management.*

### 5. 🛡️ Intelligent Cache Middleware

The backend does not rely only on the browser. We implemented a **Global ETag Middleware** (`etag_middleware.py`) that:

- Intercepts all JSON responses.
- Generates a **SHA-256** hash of the content.
- Compares it with the request’s `If-None-Match` header.
- Returns `304 Not Modified` (0 bytes body) if data hasn’t changed, saving bandwidth and client processing.

### 6. 🖼️ Image Lookup & Fallback Strategy

SWAPI does not provide images. `ImageLookupService` implements a **layered resolution strategy**:

1. **Databank Index**: Tries to match the resource name against an image index extracted from the official Star Wars Databank.
2. **Legacy Fallback**: If it fails, it looks up a local table (`image_fallbacks`) manually mapped for obscure items.
3. **Conservative Matching**: Uses string normalization algorithms (`casefold + strip`) to ensure "X-Wing" matches "x-wing fighter", but returns `None` if there’s no absolute certainty (avoiding wrong images).

### 7. 📑 Abstract Pagination (SWAPI Slicing)

SWAPI enforces pagination of 10 items. The frontend needs grids of 12, 8, or 100 items.
The `swapi_pagination.py` module solves this with **Virtual Slicing**:

- Mathematically computes which SWAPI pages (e.g., page 3 and 4) contain the desired slice (e.g., items 25 to 36).
- Fetches **only** the required pages in parallel (`asyncio.gather`).
- Combines results and slices the exact array for the client.
- *Result: The frontend can request `pageSize=100` and the backend transparently orchestrates 10 parallel SWAPI calls.*

### 8. 🎮 Gamification Engine (Jedi Trials)

The engagement system (`gamification_service.py`) is not just a points counter.

- **Behavioral Achievements**: Achievements like "Friend of Yoda" or "Vader’s Minion" are unlocked by analyzing interaction history with specific personas (`chat_stats_by_persona`).
- **Live XP & Ranks**: Level calculation is instant, using a progression curve based on cumulative XP (Youngling $\to$ Padawan $\to$ Knight $\to$ Master).
- **Leaderboard Aggregation**: Optimized SQL queries aggregate complex statistics in real time, computing accuracy (% correct) and best quiz sessions for the global leaderboard.

---

## 🔗 Integration & Data Protocols (End-to-End)

The SWAPI communication architecture was designed to be resilient and invisible to the end user. Below is the full request flow.

### 1. Client Protocol (SWAPIClient)

`SWAPIClient` (`src/app/infrastructure/external/swapi/client.py`) acts as an intelligent gateway:

- **HTTP Keep-Alive**: Uses `httpx.AsyncClient` to keep persistent connections, reducing TCP/TLS handshake *overhead* across multiple requests.
- **Transparent Pagination**: `_paginate_all` abstracts the API `next` cursor logic, automatically iterating until it consumes all data when needed (e.g., for reports).
- **URL Normalization**: The client normalizes URLs and IDs automatically, ensuring `https://swapi.dev/api/people/1/` and `https://swapi.dev/api/people/1` are treated as the same cache resource.

### 2. Data Flow (Sequence Diagram)

The diagram below illustrates the path of a simple request (e.g., "List Starships") and how the system chooses between Cache, External API, and Image Lookup.

```mermaid
sequenceDiagram
    participant UI as Frontend (React Query)
    participant API as FastAPI Backend
    participant Cache as Memory Cache (TTL)
    participant SWAPI as SWAPI.dev
    participant DB as PostgreSQL (Images Setup)

    UI->>API: GET /starships?page=1&pageSize=12
    API->>Cache: GET swapi:starships:page:1
    
    alt Cache Miss (First Access)
        API->>SWAPI: GET /starships/?page=1 & page=2 (Parallel)
        SWAPI-->>API: JSON Raw Data
        
        API->>DB: Resolve Image URLs (Virtual Join)
        DB-->>API: Starship URLs
        
        API->>API: Normalize Data (snake_case, numbers)
        API->>Cache: SET swapi:starships:page:1 (TTL 1h)
        API-->>UI: Optimized JSON + Images
    else Cache Hit
        Cache-->>API: Ready Data
        API-->>UI: Instant Response (<10ms)
    end
```

### 3. Data Handling and Normalization

SWAPI returns “dirty” data by modern standards (strings for numbers, mixed snake_case).
`StarWarsApp` implements a **Data Sanitization** layer:

- **Number Parsing**: `parse_swapi_number` converts complex strings like `"unknown"`, `"n/a"`, or ranges `"30-165"` into safe numeric types (`Optional[float]`) to enable correct sorting and charts.
- **Date Standardization**: All dates are converted to strict ISO-8601.
- **Cross-Reference Resolving**: Relationship URLs (e.g., `pilots: [...]`) are kept as references but prepared for *lazy loading* in the frontend.

### 4. 🔐 Secure Authentication Protocol (JWT + Cookie)

We implemented the **Silent Refresh** pattern for maximum security:

- **Access Token**: Short-lived (15min), stored in memory (JavaScript), used as a Bearer Token.
- **Refresh Token**: Long-lived (7 days), stored in an **HttpOnly Cookie (Secure, SameSite)**, inaccessible via JS.
- **Token Rotation**: On each refresh, the previous token is invalidated and a new one is issued, preventing replay attacks.

```mermaid
sequenceDiagram
    participant U as User
    participant F as Frontend
    participant B as Backend
    participant D as Database
    
    U->>F: Login with Google
    F->>B: Send Google Credential
    B->>D: Verify/Create User
    B-->>F: Return Access Token + User Info
    B-->>U: Set-Cookie: refresh_token (HttpOnly)
    
    Note over F,B: Secure Navigation
    
    F->>B: GET /api/v1/characters (Bearer Access)
    B-->>F: 200 OK
    
    Note over F,B: Access Token Expires
    
    F->>B: GET /api/v1/characters
    B-->>F: 401 Unauthorized
    F->>B: POST /auth/refresh (Automatic Cookie)
    B->>D: Validate Refresh Token
    B-->>F: New Access Token
    B-->>U: Set-Cookie: New refresh_token
    F->>B: Retry Original Request
```

### 5. 🤖 Context-Aware Chat Engine (ChatService)

`chat_service.py` is the brain of the application, orchestrating over 2,000 lines of conditional logic and AI.

- **Intent Routing**: Before calling the LLM, the system analyzes intent with regex heuristics. Example: "Who is Luke?" queries the local DB/SWAPI directly, saving tokens and latency.
- **RAG Pipeline**:
    1. **Extract Entities**: Identifies "Luke", "Tatooine" in the sentence.
    2. **Hybrid Search**: Vector + keyword search in the knowledge base.
    3. **Context Injection**: Injects JSON snippets (e.g., force stats) into the system prompt.
    4. **Persona Tuning**: Adjusts the response to the "Yoda" style (syntactic inversion) or "Vader".

---

## 📚 Technical Documentation (Deep Dive)

For developers who want to understand internal details, we document all critical subsystems directly here:

<details>
<summary><strong>🤖 AI & NLP Engineering</strong> (Click to expand)</summary>

### 🏗️ Intent Processing Pipeline

The system does not simply send the user’s message to the LLM. There is a strict pipeline to ensure factual accuracy and save tokens.

```mermaid
flowchart TD
    UserInput["🗣️ User Message"] --> PreProcess["🔧 Pre-processing"]
    PreProcess --> Routing{⚡ Intent Routing}
    
    Routing -- "Regex/Fixed Pattern" --> DirectReply["📝 Direct Reply (No LLM)"]
    Routing -- "Complex Question" --> RAG["🔍 RAG Search (Context Recovery)"]
    
    RAG -- "Data Found" --> ContextInj["💉 Context Injection (JSON)"]
    ContextInj --> PromptEng["🎭 Persona Engineering"]
    PromptEng --> LLM["🤖 AI Invocation"]
    
    LLM --> Response["💬 Final Answer"]
    DirectReply --> Response
```

### 1. Critical Pre-processing

Before any search, we apply Star Wars-specific sanitization:

- **Droid Name Protection**: The algorithm protects patterns like "R2-D2", "C-3PO", "BB-8" so they are not broken during normalization.
  - *Problem*: Normalizing "R2 D2" becomes `['r2', 'd2']`.
  - *Solution*: Regex identifies `\br2[\s\-]?d2\b` and converts it to a single token `R2-D2` before tokenization.

### 2. Intent Routing (Intent Routing)

`_route_structured_intent` tries to resolve the request without spending AI:

1. **Explicit Entity**: If the user says "Who is Luke?", the system extracts "Luke", fetches from SWAPI, and responds with a fixed template.
2. **Category Questions**: "Is R2-D2 a robot?". The system checks the character’s category ("robot") and answers as a boolean.

---

### 🔍 RAG Engine (Retrieval-Augmented Generation)

The `rag_search.py` file implements a hybrid search engine optimized for Portuguese.

#### Search Algorithm

We use a combination of techniques to find the correct entity (Character, Planet, Starship) even with typos.

| Technique              | Library/Implementation        | Goal                                                                     |
| :--------------------- | :---------------------------- | :----------------------------------------------------------------------- |
| **Fuzzy Matching**     | `rapidfuzz` (Levenshtein)     | Fix typos ("Anakin Skywaler" → "Skywalker")                              |
| **PT-BR Stemming**     | Custom simplified `RSLP`      | Reduce words ("correndo" → "corr", "filmes" → "film")                    |
| **Stopwords Removal**  | Custom list                   | Remove noise ("o", "a", "de", "para") but keep "Darth", "Lord"           |
| **Alias Mapping**      | Static dictionary             | Map nicknames ("Padme", "Ani", "Imperador") to canonical names           |

#### Context Injection Strategy

When an entity is found (e.g., "Luke Skywalker"), the system injects a **JSON Snippet** into the LLM System Prompt.

**Example System Prompt:**

```text
SWAPI DATA (factual reference):
{
  "name": "Luke Skywalker",
  "height": "172",
  "mass": "77",
  "hair_color": "blond",
  "skin_color": "fair",
  "eye_color": "blue",
  "birth_year": "19BBY",
  "gender": "male"
}

Rules:
- For attributes present in the data, use the values above as the source of truth.
- Do not invent numbers if they are not here.
```

This removes hallucinations about “hard” data (height, weight, colors) while allowing the AI to improvise about personality and lore.

---

### 🎭 Persona Engineering

`YodaAIService` manages response personality. The System Prompt is swapped dynamically:

#### Master Yoda (`persona="yoda"`)

- **Instruction**: "Answer in Brazilian Portuguese in Yoda’s style, inverting sentence order when possible."

- **Permissions**: Can use emojis (🌟, ⚔️).
- **Tone**: Wise, calm, lightly humorous.

#### Darth Vader (`persona="vader"`)

- **Instruction**: "Cold, authoritative, intimidating voice. Use breathing onomatopoeia (*pshhh... khhh*)."

- **Restrictions**: **FORBIDDEN** to use emojis.
- **Tone**: Hostile, impatient, superior.

</details>

<details>
<summary><strong>🎮 Gamification Mechanics</strong> (Click to expand)</summary>

### 📈 XP and Level System (Rankings)

User progression is based on **Accumulated XP (Experience)**. Rank calculation is done in real time whenever total XP changes.

#### Rankings Table (`JediRank`)

| Required XP      | Rank (Title)               | Description                                              |
| :--------------- | :------------------------- | :------------------------------------------------------- |
| **0 - 99**       | 🧒 **Youngling**           | Beginner in the Force.                                   |
| **100 - 299**    | 🧘 **Initiate**            | Starting training.                                       |
| **300 - 699**    | 🗡️ **Padawan**             | Apprentice to a Master.                                  |
| **700 - 1499**   | ⚔️ **Jedi Knight**         | Defender of peace in the galaxy.                         |
| **1500 - 2999**  | 🧙‍♂️ **Jedi Master**        | Great wisdom and power.                                  |
| **3000 - 4999**  | 🏛️ **Council Member**      | Leadership of the Jedi Order.                            |
| **5000+**        | 🌌 **Grand Master**        | Peak Force connection (Yoda level).                      |

*Source: `app/domain/enums/jedi_rank.py`*

---

### 💰 XP Sources

How the user earns experience:

1. **Quiz (Jedi Trials)**
    - **+10 XP** per correct answer.
    - *Formula*: `xp = correct * 10`
    - There is no penalty for mistakes.

2. **Daily Challenge**
    - **+30 XP** fixed upon completing the day’s goal.
    - *Example*: "Send 3 messages to Yoda today".

3. **Achievements**
    - Value varies by achievement (see table below).
    - XP is granted only once (when unlocked).

---

### 🏆 Achievements and Triggers

Achievements are checked on each interaction (`_apply_achievement_rules` in `gamification_service.py`). Some are based on *behavior* and not only numbers.

| ID                 | Name                 | XP   | Unlock Condition (Trigger)                                     |
| :----------------- | :------------------- | :--- | :------------------------------------------------------------- |
| `primeiro_contato` | **First Contact**    | +50  | Perform the first interaction (Chat or Search).                |
| `explorador`       | **Explorer**         | +100 | Perform **10 searches** in the Holocron.                       |
| `amigo_yoda`       | **Friend of Yoda**   | +150 | Send **5 messages** talking with the **Yoda** persona.         |
| `lacaio_vader`     | **Vader’s Minion**   | +150 | Send **5 messages** talking with the **Darth Vader** persona.  |

#### Persona Detection Logic

The system counts messages separately for each `persona` in conversations:

```python
# Rule pseudocode
if yoda_messages >= 5: unlock("amigo_yoda")
if vader_messages >= 5: unlock("lacaio_vader")
```

This encourages the user to try different interaction modes.

---

### 📊 Leaderboard (Global Ranking)

The Leaderboard (`get_quiz_leaderboard`) uses SQL aggregation to rank the best players.

**Tie-break criteria:**

1. **Highest score** in a single Quiz session (`best_score`).
2. (Implicit) Order of insertion in the database.

The system also computes **Accuracy**:
`Accuracy = (Total Correct / Total Questions) * 100`

---

### 🎲 Daily Challenge Generation

Currently, the daily challenge is generated deterministically based on the date:

- **ID**: `daily_chat_{YYYY-MM-DD}`
- **Goal**: Send 3 messages.
- **Reset**: The count resets at midnight (UTC).

</details>

<details>
<summary><strong>🚀 Production Deploy Guide</strong> (Click to expand)</summary>

### 📦 Infrastructure Overview

The project uses a **Serverless Containerized** architecture on GCP:

- **Compute**: Google Cloud Run (Stateless Containers).
- **Registry**: Google Artifact Registry (Docker image storage).
- **Secrets**: Google Secret Manager (Secure credential management).
- **Auth**: Google IAM (Service Accounts for runtime).

---

### 🛠️ Prerequisites

Before running, you need the following installed:

1. **Google Cloud SDK (`gcloud`)**: Authenticated (`gcloud auth login`).
2. **Docker Desktop**: Running locally (for image build).
3. **PowerShell**: Terminal for running the script.

---

### 📜 Deploy Script (`deploy-starwars.ps1`)

The script automates 6 critical steps that would take hours manually.

#### Step 1: Authentication and Setup

Checks whether `gcloud` and `docker` are available and defines the target `PROJECT_ID`.

#### Step 2: Enable APIs

Enables the required services in the GCP project:

- `run.googleapis.com` (Cloud Run)
- `secretmanager.googleapis.com` (Secrets)
- `artifactregistry.googleapis.com` (Docker Repo)
- `iam.googleapis.com` (Permissions)

#### Step 3: Runtime Service Account

Creates a dedicated identity for the backend runtime (`star-wars-cloudrun-runtime`).

- **Why?** To avoid using the “Default Compute” account which has excessive permissions.
- **Permissions**: Grants `roles/secretmanager.secretAccessor` so the backend can read the DB password and API keys.

#### Step 4: Artifact Registry

1. Checks whether the Docker repo (`cloud-run`) exists in the region.
2. If it doesn’t, creates it automatically.
3. Configures `docker-credential-gcr` to allow push.

#### Step 5: Build & Push

1. Runs `docker build` using `Dockerfile.cloud-run`.
    - *Note*: Uses a lightweight base image (`python:3.12-slim`).
2. Runs `docker push` to upload the image to Artifact Registry.

#### Step 6: Deploy to Cloud Run

Deploys the service with the following production settings:

- **Memory**: 512Mi (Optimized for Free Tier).
- **CPU**: 1 vCPU.
- **Auto-scaling**: 0 to 1 instance (avoid costs when idle, “scale to zero”).
- **Env Vars**: Injects non-sensitive variables (DB Host, CORS).
- **Secrets**: Mounts secrets (`holocron-db-password`, `holocron-jwt-secret-key`) as environment variables.

---

### 🔑 Secrets Management

The script does **NOT** create secrets. You must create them manually once in the GCP Console or via CLI:

```bash
# Example: Creating the JWT secret
printf "my-super-secret-key" | gcloud secrets create holocron-jwt-secret-key --data-file=-

# Example: Creating the DB secret
printf "db-password" | gcloud secrets create holocron-db-password --data-file=-
```

### Required Secrets

- `holocron-jwt-secret-key`: To sign auth tokens.

- `holocron-db-password`: PostgreSQL password.

### Optional Secrets

- `holocron-openai-api-key`: If `AI_ENABLED=true`.

---

### 🔄 Useful Commands

#### Quick Deploy (Default)

```powershell
.\deploy-starwars.ps1
```

#### Deploy to Another Region

```powershell
.\deploy-starwars.ps1 -Region "us-central1"
```

#### Error Logs

If the container fails to start, check logs in GCP:

```bash
gcloud run services logs read star-wars-backend
```

</details>
</details>

<details>
<summary><strong>🎨 UX & Frontend Architecture</strong> (Click to expand)</summary>

### 📱 State Management Strategy

We use a hybrid strategy for state management:

1. **Server State (React Query / TanStack)**:
    - API data (Characters, Films, User Profile).
    - Cache, retries, and automatic revalidation.
    - *Example*: `useQuery(['characters', page], fetchCharacters)`.

2. **Client/UI State (Zustand)**:
    - Non-persistent global UI state.
    - No need for complex Providers (Context API Hell).
    - *Example*: `useImageEditModeStore` to control image editing modals.

---

### 🔐 Auth UX Pattern (Silent Refresh)

To avoid abruptly logging the user out or showing 401 errors on screen:

- **Refresh Token**: Stored in an `HttpOnly` Cookie (inaccessible via JS).
- **Strategy**: The `/auth/refresh` endpoint returns **204 No Content** (instead of 401) when there is no session.
  - This lets the frontend smoothly decide whether to show “Login” or “Profile” without throwing exceptions in the console.

---

### ⚡ Performance & Caching (Backend Side)

The backend implements `ETagMiddleware` (`etag_middleware.py`) to optimize data transfer and reduce latency:

1. **Hashing Algorithm**: We intercept every JSON response and compute a **SHA-256** hash of the body (`hexdigest`).
2. **Content Negotiation (RFC 7232)**:
    - The server always sends `Cache-Control: private, max-age=0, must-revalidate`. This forces the browser to *always* ask the server “did this change?” before using cache.
    - If the request `If-None-Match` header matches the computed hash:
        - We return **304 Not Modified**.
        - **CRITICAL**: We remove the response body and the `Content-Length` header, reducing the payload from KB/MB to ~0 bytes.
3. **Cache Security**:
    - We add `Vary: Origin, Authorization` to ensure one user never receives another user’s private cache (e.g., profile data).
    - The middleware reconstructs the response iterator (`response.body_iterator`) to ensure the stream can be consumed both for hashing and by the final client.

</details>
</details>

<details>
<summary><strong>📐 Quality Assurance & Data Architecture</strong> (Click to expand)</summary>

### 🧪 Testing Strategy (QA)

We maintain code quality with a test suite split into two layers:

1. **Backend (Pytest)**:
    - Focus on isolated **Unit Tests** for business rules (`GamificationService`, `ChatService`).
    - Integration tests ensure API contracts (`schemas`) are respected.

2. **Frontend (Vitest)**:
    - Fast unit tests for Hooks and Stores (`useImageEditModeStore`).
    - Ensures UI logic (e.g., toggles, formatting) works without rendering the entire app.

### 💾 Data Engineering

Data robustness is guaranteed by three pillars:

1. **Strict Validation (Pydantic V2)**:
    - API inputs and outputs are typed.
    - App settings use custom validators to parse CSV/JSON from environment variables (`cors_allow_origins`).

2. **Database Migrations (Alembic)**:
    - PostgreSQL schema versioning.
    - `env.py` was customized to inject `PYTHONPATH` dynamically, enabling migrations even in complex container environments.

3. **Logging & Observability**:
    - Centralized configuration (`alembic.ini`, `custom loggers`) to trace silent production errors.

</details>

---

## 🛡️ Infrastructure & Security (DevSecOps)

Security is not an “add-on”, but part of the cloud-native infrastructure design.

### 1. 🔑 Secrets Management

We adopted a **Zero Hardcoded Secrets** strategy.

- **Frontend (Vercel)**: Public keys (Google Client ID) and API URLs are injected at build time via Vercel environment variables. No private key ever touches the client bundle.
- **Backend (Google Cloud Run)**: Critical secrets (DB Password, JWT Secret, OpenAI Key) are managed by **GCP Secret Manager**. They are mounted into the container as runtime environment variables, ensuring not even the Dockerfile can access them.

### 2. 🐳 Secure Containerization Pipeline

`Dockerfile.cloud-run` follows hardening best practices:

- **Minimal Base Image**: Based on `python:3.12-slim` to drastically reduce the attack surface (fewer vulnerable binaries).
- **Stateless by Design**: The container retains no data. Uploads and persistence are delegated to external services (Storage/PostgreSQL).
- **Auto-Migrations**: The entrypoint runs `alembic upgrade head` on every deploy, ensuring the DB schema stays synchronized with application code (Infrastructure as Code).

### 3. 💾 Persistence and Resilience

Although the application heavily relies on cache, **PostgreSQL** is the source of truth for critical data:

- **User Profiles**: Sensitive data and gamification progress.
- **Image Fallbacks**: Our `image_fallbacks` table acts as a failover system. If the external image CDN fails, the system automatically falls back to curated assets stored in the database.

```mermaid
graph TD
    subgraph "Public Zone (Vercel)"
        Frontend[React SPA]
    end
    
    subgraph "Private Zone (Google Cloud Platform)"
        LB[Load Balancer HTTPS]
        
        subgraph "Cloud Run (Auto-Scaling)"
            API[FastAPI Container]
        end
        
        Secret[GCP Secret Manager]
        DB[(PostgreSQL)]
        Vertex[Vertex AI]
    end
    
    Frontend -- "Bearer JWT (TLS 1.3)" --> LB
    LB --> API
    
    API -- "Env Vars Injection" --> Secret
    API -- "SQLAlchemy (Connection Pool)" --> DB
    API -- "IAM Credentials" --> Vertex
    
    style Secret fill:#f9f,stroke:#333
    style DB fill:#ccf,stroke:#333
```

---

### 9. 🛡️ Compliance & Security Standards (RBAC & OWASP)

The project was audited following strict software security principles, aligned with the OWASP Top 10 and corporate compliance rules.

#### 9.1 Access and Identity (RBAC & Invoker)

- **Cloud Run Invoker**: The backend is not public. It runs in `authenticated-only` mode, accepting only requests with a valid Google-signed OIDC token (via Vercel Service Account). No one can access the API directly without going through the frontend.

- **RBAC (Role-Based Access Control)**: Internally, administrative endpoints validate the JWT token. Only authenticated users (`require_authenticated_user_id`) can persist data or generate complex reports.

#### 9.2 Vulnerability Prevention (OWASP)

| Vulnerability                     | Implemented Mitigation Strategy                                                                                                 |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| **SQL Injection**                 | Strict use of SQLAlchemy ORM with *parameterized queries*. No SQL string is manually concatenated.                               |
| **XSS (Cross-Site Scripting)**    | React 19 with default auto-escaping. Sensitive cookies (`refresh_token`) marked `HttpOnly` to prevent JS theft.                |
| **Sensitive Data Exposure**       | Secrets managed by **GCP Secret Manager**. Logs sanitized to avoid leaking PII (Personal Identifiable Information).            |
| **Broken Access Control**         | Token verification middleware on all protected routes (`Depends(require_authenticated_user_id)`).                              |

#### 9.3 Cloud Run Private Access Diagram

This graph shows how backend access is locked down.

```mermaid
%%{title: "Cloud Run Private Access & API Shielding"}%%
flowchart LR
    subgraph External_World ["External World"]
        User[User]
        Hacker[Attacker]
    end
    
    subgraph Security_Perimeter ["Security Perimeter (Google Auth)"]
        Vercel["Vercel Frontend"]
    end
    
    subgraph Private_Zone ["Private Zone (Secure Backend)"]
        CloudRun["Cloud Run Backend"]
        DB[("PostgreSQL")]
        Secrets["Secret Manager"]
    end
    
    subgraph Shielded_APIs ["External APIs (Shielded)"]
        SWAPI["SWAPI (Data)"]
        AI["OpenAI / Vertex AI"]
    end
    
    %% User flow
    User -- HTTPS --> Vercel
    Hacker -. "Direct Access (403 Forbidden)" .-> CloudRun
    
    %% Service-to-service auth
    Vercel -- "OIDC ID Token (Auth)" --> CloudRun
    
    %% Backend accessing resources
    CloudRun -- "Internal Traffic" --> DB
    CloudRun -- "Load API Keys" --> Secrets
    
    %% Shielding: backend protects keys and rate-limits
    CloudRun -- "Proxied Request" --> SWAPI
    CloudRun -- "Secure Context" --> AI
    
    %% Styling
    style Vercel fill:#000,color:#fff
    style CloudRun fill:#4285F4,color:#fff
    style Hacker stroke:red,stroke-width:2px,stroke-dasharray: 5 5
    style Secrets fill:#FFEB3B,color:#000
```

---

## 🔌 API Reference (Endpoints)

The REST API follows OpenAPI 3.0 standards. Interactive documentation is available at `/docs` (Swagger UI).

### 🔐 Authentication (`/api/v1/auth`)

| Method | Endpoint              | Description                                  | Auth   |
| :----- | :-------------------- | :------------------------------------------- | :----- |
| POST   | `/google`             | Login via Google OAuth (Credential One-Tap)  | ❌     |
| POST   | `/refresh`            | Refresh Access Token using Refresh Cookie    | Cookie |
| POST   | `/logout`             | Invalidate session and clear cookies         | ✅     |
| GET    | `/me`                 | Return authenticated user profile            | ✅     |

### 👤 Characters (`/api/v1/characters`)

| Method | Endpoint          | Description                                  | Auth |
| :----- | :---------------- | :------------------------------------------- | :--- |
| GET    | `/`               | List characters with filters and pagination  | ❌   |
| GET    | `/{id}`           | Details for a specific character             | ❌   |

**Query Params:** `page`, `pageSize`, `search`, `gender`, `homeworld`, `species`, `film`, `sort`

### 🎬 Films (`/api/v1/films`)

| Method | Endpoint          | Description                                  | Auth |
| :----- | :---------------- | :------------------------------------------- | :--- |
| GET    | `/`               | List all films in the saga                   | ❌   |
| GET    | `/{id}`           | Details for a specific film                  | ❌   |

### 🚀 Starships (`/api/v1/starships`)

| Method | Endpoint          | Description                                  | Auth |
| :----- | :---------------- | :------------------------------------------- | :--- |
| GET    | `/`               | List starships with filters and pagination   | ❌   |
| GET    | `/{id}`           | Details for a specific starship              | ❌   |

**Query Params:** `page`, `pageSize`, `search`, `starship_class`, `manufacturer`, `film`, `sort`

### 🌍 Planets (`/api/v1/planets`)

| Method | Endpoint          | Description                                  | Auth |
| :----- | :---------------- | :------------------------------------------- | :--- |
| GET    | `/`               | List planets with filters and pagination     | ❌   |
| GET    | `/{id}`           | Details for a specific planet                | ❌   |

**Query Params:** `page`, `pageSize`, `search`, `climate`, `terrain`, `film`, `sort`

### 👽 Species (`/api/v1/species`)

| Method | Endpoint          | Description                                  | Auth |
| :----- | :---------------- | :------------------------------------------- | :--- |
| GET    | `/`               | List species with filters and pagination     | ❌   |
| GET    | `/{id}`           | Details for a specific species               | ❌   |

**Query Params:** `page`, `pageSize`, `search`, `classification`, `designation`, `language`, `film`, `sort`

### 🚗 Vehicles (`/api/v1/vehicles`)

| Method | Endpoint          | Description                                  | Auth |
| :----- | :---------------- | :------------------------------------------- | :--- |
| GET    | `/`               | List vehicles with filters and pagination    | ❌   |
| GET    | `/{id}`           | Details for a specific vehicle               | ❌   |

**Query Params:** `page`, `pageSize`, `search`, `vehicle_class`, `manufacturer`, `film`, `sort`

### 🤖 AI Chat (`/api/v1/chat`)

| Method | Endpoint          | Description                                  | Auth |
| :----- | :---------------- | :------------------------------------------- | :--- |
| POST   | `/`               | Send message and receive AI response         | ✅   |
| GET    | `/history`        | User conversation history                    | ✅   |

**Body (POST):**

```json
{
  "message": "Who is Luke Skywalker?",
  "persona": "yoda"  // or "vader"
}
```

### 🎮 Gamification (`/api/v1/gamification`)

| Method | Endpoint              | Description                                  | Auth |
| :----- | :-------------------- | :------------------------------------------- | :--- |
| GET    | `/profile`            | Gamification profile (XP, Rank, Stats)       | ✅   |
| GET    | `/achievements`       | List user achievements                       | ✅   |
| GET    | `/leaderboard`        | Global users leaderboard                      | ❌   |
| GET    | `/daily-challenge`    | Current daily challenge                       | ✅   |
| POST   | `/quiz/start`         | Start a quiz session                          | ✅   |
| POST   | `/quiz/answer`        | Answer a quiz question                        | ✅   |
| POST   | `/quiz/finish`        | Finish quiz and receive XP                    | ✅   |

### 📊 Metadata (`/api/v1/metadata`)

| Method | Endpoint                      | Description                                  | Auth |
| :----- | :---------------------------- | :------------------------------------------- | :--- |
| GET    | `/characters/homeworlds`      | List unique homeworlds                       | ❌   |
| GET    | `/characters/species`         | List unique species                           | ❌   |
| GET    | `/characters/genders`         | List unique genders                           | ❌   |
| GET    | `/planets/climates`           | List unique climates                          | ❌   |
| GET    | `/planets/terrains`           | List unique terrains                          | ❌   |
| GET    | `/species/classifications`    | List unique classifications                   | ❌   |
| GET    | `/species/designations`       | List unique designations                      | ❌   |
| GET    | `/species/languages`          | List unique languages                         | ❌   |
| GET    | `/starships/classes`          | List unique starship classes                  | ❌   |
| GET    | `/starships/manufacturers`    | List unique starship manufacturers            | ❌   |
| GET    | `/vehicles/classes`           | List unique vehicle classes                   | ❌   |
| GET    | `/vehicles/manufacturers`     | List unique vehicle manufacturers             | ❌   |

### 🖼️ Images (`/api/v1/image-fallbacks`)

| Method | Endpoint          | Description                                  | Auth |
| :----- | :---------------- | :------------------------------------------- | :--- |
| GET    | `/`               | List all image fallbacks                      | ❌   |
| POST   | `/`               | Create or update an image fallback            | ✅   |
| DELETE | `/{id}`           | Remove an image fallback                      | ✅   |

### ❤️ Health Check (`/api/v1/health`)

| Method | Endpoint          | Description                                  | Auth |
| :----- | :---------------- | :------------------------------------------- | :--- |
| GET    | `/`               | API health status                             | ❌   |
| GET    | `/ready`          | Readiness probe (for Kubernetes/Cloud Run)    | ❌   |

---

## 🎨 Design System

The Holocron Analytics UI was designed to deliver an immersive Star Wars experience.

### 🎨 Color Palette

| CSS Token                 | Hex         | Usage                                    |
| :------------------------ | :---------- | :--------------------------------------- |
| `--color-primary`         | `#35e6ff`   | Primary color (Neon Cyan)                |
| `--color-secondary`       | `#ff35a0`   | Accent color (Magenta)                   |
| `--color-background`      | `#0a0a12`   | Main background (Space Black)            |
| `--color-surface`         | `#1a1a2e`   | Cards and elevated surfaces              |
| `--color-text-primary`    | `#ffffff`   | Primary text                             |
| `--color-text-secondary`  | `#8b8b9a`   | Secondary text                           |
| `--color-success`         | `#00ff87`   | Success states                           |
| `--color-warning`         | `#ffcc00`   | Warning states                           |
| `--color-error`           | `#ff4444`   | Error states                             |

### ✨ Visual Effects

- **Glassmorphism**: Cards with `backdrop-filter: blur(12px)` and translucent borders.
- **Neon Glow**: Colored shadows (`box-shadow`) for interactive elements.
- **Dynamic Starfield**: Animated background with CSS/JS particles.
- **Hover Transitions**: Smooth effects with `transform` and `opacity` (0.2s ease).

### 🧩 Reusable Components

| Component               | Location                           | Description                                       |
| :---------------------- | :--------------------------------- | :------------------------------------------------ |
| `CustomSelect`          | `shared/components/CustomSelect`   | Styled dropdown with Star Wars theme              |
| `FilmFilter`            | `shared/components/FilmFilter`     | Global film filter (7 films)                      |
| `PageLayout`            | `shared/components/PageLayout`     | Base layout with header, content, commands        |
| `Pagination`            | `shared/components/Pagination`     | Responsive page navigation                         |
| `ScrollToTop`           | `shared/components/ScrollToTop`    | Floating button to scroll back to top             |
| `StarfieldEvents`       | `shared/components/StarfieldEvents`| Animated background with meteors                  |
| `DetailsModal`          | `shared/components/DetailsModal`   | Details modal with glassmorphism                  |
| `FallbackEditableImage` | `shared/components/...`            | Image with fallback and inline editing            |

### 🪝 Custom Hooks

| Hook                  | File                                 | Description                                       |
| :-------------------- | :----------------------------------- | :------------------------------------------------ |
| `useFilmOptions`      | `shared/hooks/useFilmOptions.ts`     | Formatted options for FilmFilter                  |
| `useMetadataOptions`  | `shared/hooks/useMetadataOptions.ts` | 10+ variants for entity filters                   |
| `usePrefetchAllData`  | `shared/hooks/usePrefetchAllData.ts` | 6-phase prefetch pipeline                         |
| `useImageFallback`    | `shared/hooks/useImageFallback.ts`   | Image fallback management                         |

---

## 📋 Environment Variables

### Backend (`.env` or GCP Secret Manager)

```env
# 🔌 Database
DATABASE_URL=postgresql://user:password@host:5432/dbname

# 🔐 Authentication
JWT_SECRET_KEY=your-256-bit-secret-key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=15

# 🌐 Google OAuth
GOOGLE_CLIENT_ID=your-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-client-secret

# 🤖 OpenAI
OPENAI_API_KEY=sk-...
AI_ENABLED=true
OPENAI_MODEL=gpt-4o

# 🔗 CORS
CORS_ALLOW_ORIGINS=http://localhost:5173,https://your-domain.vercel.app

# 📊 Environment
ENVIRONMENT=development  # or production
LOG_LEVEL=INFO
```

### Frontend (`.env` or Vercel Environment Variables)

```env
# 🔗 API
VITE_API_URL=http://localhost:8000/api/v1

# 🌐 Google OAuth (Public Key)
VITE_GOOGLE_CLIENT_ID=your-client-id.apps.googleusercontent.com

# ⚙️ Configuration
VITE_APP_TITLE=Holocron Analytics
```

---

## 💻 Detailed Tech Stack

### Backend (Python 3.12)

| Category        | Technology                    | Version | Usage                                   |
| :-------------- | :---------------------------- | :------ | :-------------------------------------- |
| **Framework**   | FastAPI                       | 0.109   | High-performance async REST API         |
| **ORM**         | SQLAlchemy                    | 2.0     | Object-relational mapping               |
| **Migrations**  | Alembic                       | 1.13    | DB schema versioning                    |
| **Validation**  | Pydantic                      | 2.9     | Data validation and schemas             |
| **Database**    | PostgreSQL                    | 9.5+    | Primary relational database             |
| **Cache**       | cachetools (TTLCache)         | 5.5     | In-memory cache with TTL                |
| **AI**          | OpenAI SDK                    | 1.66    | GPT-4o integration                      |
| **NLP**         | rapidfuzz                     | 3.10    | Fuzzy matching (Levenshtein)            |
| **HTTP**        | httpx                         | 0.27    | Async HTTP client                       |
| **Auth**        | python-jose                   | 3.3     | JWT encoding/decoding                   |
| **Security**    | passlib + bcrypt              | 1.7     | Password hashing                        |

### Frontend (Node.js 20+)

| Category        | Technology                    | Version | Usage                                   |
| :-------------- | :---------------------------- | :------ | :-------------------------------------- |
| **Framework**   | React                         | 19.0    | Declarative UI library                  |
| **Language**    | TypeScript                    | 5.6     | Static typing                           |
| **Bundler**     | Vite                          | 6.0     | Ultra-fast build tool                   |
| **State**       | Zustand                       | 5.0     | Lightweight global state                |
| **Data**        | TanStack Query                | 5.62    | Server data fetching and cache          |
| **Charts**      | Recharts                      | 3.7     | Responsive SVG charts                   |
| **Styling**     | CSS Modules                   | -       | Locally scoped styles                   |
| **Routing**     | React Router                  | 7.1     | SPA navigation                          |

### Infrastructure

| Category        | Technology                    | Usage                                   |
| :-------------- | :---------------------------- | :-------------------------------------- |
| **Container**   | Docker + Docker Compose       | Development and production              |
| **Backend**     | Google Cloud Run              | Serverless backend hosting              |
| **Frontend**    | Vercel                        | Frontend hosting and CDN                |
| **Secrets**     | GCP Secret Manager            | Secure credential management            |
| **Registry**    | Google Artifact Registry      | Docker image repository                 |

---

## 🚀 How to Run

### Prerequisites

- Docker & Docker Compose (Recommended)

### Running with Docker

1. At the project root:

    ```bash
    docker-compose -f docker-compose.dev.yml up -d --build
    ```

2. Access:
    - **Frontend**: `http://localhost:5173`
    - **Docs**: `http://localhost:8000/docs`

---

## 👨‍💻 Developer

Project delivered for the PowerOfData Technical Challenge.

> *"Do or do not. There is no try."* — Master Yoda
