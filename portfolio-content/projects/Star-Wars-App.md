# 🌌 HOLOCRON ANALYTICS

> **"Onde a Força dos Dados se Encontra com a Sabedoria da Galáxia"**

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

## 📑 Índice

- [📜 Visão Geral](#-visão-geral)
- [📂 Estrutura do Projeto](#-estrutura-do-projeto)
- [🏗️ Arquitetura e Engenharia de Performance](#️-arquitetura-e-engenharia-de-performance)
- [🛠️ Bastidores da Engenharia (Deep Dive)](#️-bastidores-da-engenharia-deep-dive)
- [🗺️ Navegação e Funcionalidades](#️-navegação-e-funcionalidades)
- [🔗 Integração & Protocolos de Dados](#-integração--protocolos-de-dados-end-to-end)
- [📚 Documentação Técnica (Deep Dive)](#-documentação-técnica-deep-dive)
  - [🤖 Engenharia de IA & NLP](#-engenharia-de-ia--nlp)
  - [🎮 Mecânicas de Gamificação](#-mecânicas-de-gamificação)
  - [🚀 Guia de Deploy em Produção](#-guia-de-deploy-em-produção)
  - [🎨 UX & Frontend Architecture](#-ux--frontend-architecture)
  - [📐 Quality Assurance & Data Architecture](#-quality-assurance--data-architecture)
- [🛡️ Infraestrutura & Segurança (DevSecOps)](#️-infraestrutura--segurança-devsecops)
- [🔌 API Reference (Endpoints)](#-api-reference-endpoints)
- [🎨 Design System](#-design-system)
- [📋 Variáveis de Ambiente](#-variáveis-de-ambiente)
- [💻 Stack Tecnológico Detalhado](#-stack-tecnológico-detalhado)
- [🚀 Como Executar](#-como-executar)
- [👨‍💻 Desenvolvedor](#-desenvolvedor)

---

## 📜 Visão Geral

O **Holocron Analytics** é uma plataforma imersiva e gamificada desenvolvida para explorar o universo de Star Wars. Muito além de uma simples wiki, este projeto transforma a consulta de dados da API pública (SWAPI) em uma experiência de "Arquivista Jedi", utilizando **Inteligência Artificial (OpenAI GPT-4o)** para enriquecer dados, gerar quizzes dinâmicos e simular interações com o Mestre Yoda.

### Principais Funcionalidades

- **🔍 Holocron Digital**: Consulta avançada de Personagens, Filmes, Naves, Planetas, Espécies e Veículos.
- **🤖 Mestre Yoda AI**: Um chatbot integrado alimentado por LLM que responde perguntas sobre a galáxia com a personalidade do icônico Mestre Jedi, utilizando dados cacheados para respostas ultra-rápidas.
- **⚔️ Gamificação & Jedi Trials**: Sistema de progressão onde o usuário sobe de rankings (Padawan -> Mestre) ao completar desafios e quizzes.
- **📊 Relatórios Visuais**: Gráficos detalhados sobre a distribuição de espécies, veículos por filme e estatísticas da galáxia.
- **🚀 Performance Extrema**: Estratégias avançadas de caching e carregamento em background para uma navegação instantânea.
- **📱 Design Responsivo**: Interface totalmente adaptada para desktop, tablet e mobile com UX de alto nível.

---

## 📂 Estrutura do Projeto

```
Star-Wars-App/
├── backend/                          # API FastAPI (Python)
│   ├── src/app/
│   │   ├── application/              # Camada de Aplicação (Use Cases)
│   │   │   └── services/             # Services de negócio
│   │   │       ├── chat_service.py          # Motor de chat com IA
│   │   │       ├── gamification_service.py  # Sistema de XP e conquistas
│   │   │       ├── quiz_service.py          # Geração de quizzes com IA
│   │   │       └── rag_search.py            # Motor de busca híbrido (RAG)
│   │   ├── domain/                   # Camada de Domínio (DDD)
│   │   │   ├── entities/             # Entidades de negócio
│   │   │   ├── enums/                # Enumerações (JediRank, etc.)
│   │   │   ├── exceptions/           # Exceções customizadas
│   │   │   ├── repositories/         # Interfaces de repositório
│   │   │   └── schemas/              # Schemas Pydantic (DTOs)
│   │   ├── infrastructure/           # Camada de Infraestrutura
│   │   │   ├── cache/                # Sistema de cache em memória
│   │   │   ├── config/               # Configurações (Settings)
│   │   │   ├── db/                   # SQLAlchemy models e conexão
│   │   │   ├── external/             # Integrações externas
│   │   │   │   ├── openai/           # Cliente OpenAI (GPT-4o)
│   │   │   │   └── swapi/            # Cliente SWAPI
│   │   │   ├── security/             # JWT, Auth handlers
│   │   │   └── etag_middleware.py    # Middleware de cache HTTP
│   │   └── interfaces/               # Camada de Interface
│   │       └── api/v1/
│   │           ├── routers/          # Endpoints da API
│   │           │   ├── auth.py              # Autenticação Google OAuth
│   │           │   ├── characters.py        # CRUD Personagens
│   │           │   ├── chat.py              # Chat com IA
│   │           │   ├── films.py             # CRUD Filmes
│   │           │   ├── gamification.py      # XP, Ranking, Achievements
│   │           │   ├── health.py            # Health check
│   │           │   ├── image_fallbacks.py   # Gestão de imagens
│   │           │   ├── metadata.py          # Metadados para filtros
│   │           │   ├── planets.py           # CRUD Planetas
│   │           │   ├── species.py           # CRUD Espécies
│   │           │   ├── starships.py         # CRUD Naves
│   │           │   └── vehicles.py          # CRUD Veículos
│   │           └── dependencies/     # Injeção de dependências
│   ├── alembic/                      # Migrações de banco
│   │   └── versions/                 # Scripts de migração
│   ├── tests/                        # Testes unitários (Pytest)
│   ├── Dockerfile.cloud-run          # Dockerfile para produção
│   ├── Dockerfile.dev                # Dockerfile para desenvolvimento
│   └── pyproject.toml                # Dependências Python (Poetry)
│
├── frontend/                         # SPA React (TypeScript)
│   ├── src/
│   │   ├── App/                      # Componente raiz e navegação
│   │   ├── features/                 # Módulos por domínio (Feature-based)
│   │   │   ├── auth/                 # Autenticação Google
│   │   │   │   ├── components/       # UserMenu, LoginButton
│   │   │   │   ├── context/          # AuthProvider, AuthContext
│   │   │   │   ├── pages/            # LoginPage, AuthLoadingPage
│   │   │   │   └── services/         # authService (API calls)
│   │   │   ├── characters/           # Módulo Personagens
│   │   │   │   ├── components/       # CharacterCard, CharacterModal
│   │   │   │   ├── hooks/            # useCharacters, useCharacterDetails
│   │   │   │   ├── pages/            # CharactersPage
│   │   │   │   └── services/         # charactersService
│   │   │   ├── chat/                 # Módulo Chat com IA
│   │   │   │   ├── components/       # YodaChatBubble, ChatModal
│   │   │   │   ├── context/          # ChatProvider
│   │   │   │   └── hooks/            # useChat, useChatHistory
│   │   │   ├── dashboard/            # Dashboard principal
│   │   │   ├── films/                # Módulo Filmes
│   │   │   ├── gamification/         # Módulo Gamificação
│   │   │   │   ├── components/       # QuizModal, AchievementCard
│   │   │   │   ├── hooks/            # useGamification, useQuiz
│   │   │   │   └── pages/            # GamificationPage
│   │   │   ├── planets/              # Módulo Planetas
│   │   │   ├── reports/              # Módulo Relatórios
│   │   │   │   ├── components/       # Charts, LeaderboardTable
│   │   │   │   └── pages/            # ReportsPage
│   │   │   ├── species/              # Módulo Espécies
│   │   │   ├── starships/            # Módulo Naves
│   │   │   └── vehicles/             # Módulo Veículos
│   │   └── shared/                   # Código compartilhado
│   │       ├── components/           # Componentes reutilizáveis
│   │       │   ├── CustomSelect/     # Select customizado Star Wars
│   │       │   ├── FilmFilter/       # Filtro global por filme
│   │       │   ├── PageLayout/       # Layout base das páginas
│   │       │   ├── Pagination/       # Paginação responsiva
│   │       │   ├── ScrollToTop/      # Botão voltar ao topo
│   │       │   └── StarfieldEvents/  # Background animado
│   │       ├── hooks/                # Hooks compartilhados
│   │       │   ├── useFilmOptions.ts        # Options de filmes
│   │       │   ├── useMetadataOptions.ts    # Metadata para filtros
│   │       │   └── usePrefetchAllData.ts    # Prefetch em 6 fases
│   │       ├── services/             # Services compartilhados
│   │       │   ├── api.ts                   # Cliente HTTP base
│   │       │   └── metadata.service.ts      # Service de metadados
│   │       ├── stores/               # Zustand stores
│   │       └── styles/               # Estilos globais
│   │           └── global.css        # CSS Variables, Starfield
│   ├── api/                          # Vercel Serverless Functions
│   ├── index.html                    # Entry point HTML
│   ├── vite.config.ts                # Configuração Vite
│   └── package.json                  # Dependências Node.js
│
├── regras-desenvolvimento-python-react/  # Documentação de padrões
│   ├── regras-backend.md             # Padrões Python/FastAPI
│   ├── regras-frontend.md            # Padrões React/TypeScript
│   └── regras-testes.md              # Padrões de testes
│
├── docker-compose.dev.yml            # Compose para desenvolvimento
├── deploy-starwars.ps1               # Script de deploy GCP
└── README.md                         # Esta documentação
```

---

## 🏗️ Arquitetura e Engenharia de Performance

A solução foi projetada com foco obsessivo em performance e fluidez (UX), utilizando uma estratégia de carregamento inteligente e cache multinível.

```mermaid
%%{title: "Estratégia de Performance e Cache"}%%
flowchart TD
    Init["🚀 Inicialização do App"] --> FastLoad["🔥 Carregamento Crítico"]
    FastLoad --> Render["🖥️ Renderização Imediata (LCP Otimizado)"]
    
    Render --> Background["⏳ Carregamento em Background"]
    Background --> FetchAll["📡 Fetch Massivo da SWAPI"]
    FetchAll --> Process["⚙️ Processamento & Enriquecimento"]
    Process --> Cache["💾 Cache Local (Memory)"]
    
    subgraph UX_Fluidity ["Navegação Fluida"]
        UserAction["🖱️ Navegação do Usuário"]
        UserAction -- "Dados já em Cache" --> InstantServe["⚡ Exibição Instantânea"]
        UserAction -- "Chat/Quiz" --> ContextAware["🧠 Contexto Pré-carregado"]
    end
    
    Cache -.-> UX_Fluidity
```

### 🧠 Pipeline de Inteligência Artificial

A integração com a IA não é apenas um "wrapper". Ela atua ativamente para cobrir lacunas de dados e gerar conteúdo.

```mermaid
%%{title: "Pipeline de Enriquecimento de Dados com IA"}%%
sequenceDiagram
    participant C as Client
    participant B as Backend
    participant DB as Banco de Dados
    participant SW as SWAPI
    participant AI as Vertex AI (Gemini)

    C->>B: GET /characters/1 (Luke Skywalker)
    B->>DB: Busca Cache Local
    
    alt Dados Incompletos ou Inexistentes
        B->>SW: Fetch Dados Básicos
        SW-->>B: JSON Bruto (SWAPI)
        B->>AI: Prompt: "Gere stats de RPG para Luke"
        AI-->>B: JSON Enriquecido (Força: 85, Agilidade: 80...)
        B->>DB: Salva/Atualiza Registro
    end
    
    B-->>C: Retorna Personagem Completo + Stats
```

---

## 🛠️ Bastidores da Engenharia (Deep Dive)

O que diferencia o **Holocron Analytics** é a atenção aos detalhes técnicos "invisíveis" que tornam a experiência mágica.

### 1. 🔍 Otimização de Busca (NLP & RAG)

O sistema de busca (`rag_search.py`) implementa um motor de **Retrieval-Augmented Generation** que entende português nativo.

- **Fuzzy Search Híbrida**: Utiliza `rapidfuzz` (Levenshtein Distance) para corrigir erros de digitação ("Anakin Skywaler" -> Encontra "Anakin Skywalker").
- **Stemming PT-BR**: Algoritmo customizado que remove sufixos (-inho, -mente, -ão) para entender a intenção da busca.
- **Detecção de Entidades**: Heurísticas inteligentes diferenciam quando o usuário busca um droide ("R2") vs. um termo genérico, evitando falsos positivos.
- **Sinônimos**: Mapeia automaticamente termos como "sabre de luz" ↔ "lightsaber" ou "robô" ↔ "droid".

### 2. 🧙 Engenharia de Persona (Prompting)

O **Mestre Yoda AI** não é apenas um chatbot padrão.

- **Contexto Dinâmico**: O sistema injeta snippets de dados oficiais da SWAPI no contexto do modelo para garantir que as respostas sejam factuais (Grounding), reduzindo alucinações.
- **Inversão Sintática**: O prompt do sistema instrui a IA a mimetizar a gramática única do Yoda (Objeto-Sujeito-Verbo).
- **Múltiplas Personas**: A arquitetura suporta troca de personas, permitindo conversar também com uma versão "Darth Vader", que responde com hostilidade e emojis proibidos.

### 3. ✨ Frontend Cinematográfico

A interface foi construída para imersão total:

- **Starfield Dinâmico**: O fundo de estrelas (`StarfieldEvents.tsx`) não é um vídeo em loop. É um sistema de partículas gerado proceduralmente que simula "tráfego espacial", com meteoros variando em velocidade, ângulo e profundidade.
- **Acessibilidade**: O sistema detecta a preferência `prefers-reduced-motion` do sistema operacional e desativa automaticamente animações pesadas para usuários sensíveis à cinética.

---

## 🗺️ Navegação e Funcionalidades

### 1. 🔍 Holocron (Exploração de Dados)

Páginas dedicadas para cada entidade do universo Star Wars, com cards ricos e interativos.

- **Páginas**: `Personagens`, `Filmes`, `Naves`, `Planetas`, `Espécies`, `Veículos`.
- **Filtros Avançados**:
  - Filtragem por Nome, Gênero, Clima (Planetas), Classe (Naves), e muito mais.
  - Busca fuzzy (aproximada) para encontrar termos mesmo com erros de digitação.
  - Ordenação dinâmica e paginação instantânea (client-side pagination graças ao pré-carregamento).

### 2. 📊 Relatórios e Analytics

Localizado na pasta `reports`, esta seção oferece insights visuais através de gráficos interativos.

- **Distribuição de Espécies**: Gráficos de pizza/barras mostrando a diversidade da galáxia.
- **Comparativo de Naves**: Gráficos de dispersão comparando velocidade vs. custo.
- **Cronologia**: Linha do tempo visual dos filmes e eventos.

### 3. ⚔️ Gamificação Completa

O sistema mantém os usuários engajados através de um sistema de níveis e recompensas.

- **Jedi Trials**: Quizzes gerados por IA que testam conhecimento.
- **Barra de XP**: Ganhe experiência explorando o sistema, completando quizzes e descobrindo "easter eggs".
- **Rankings**: Comece como *Youngling*, torne-se *Padawan*, *Cavaleiro* e, finalmente, *Mestre Jedi*.
- **Conquistas**: Medalhas desbloqueáveis (ex: "Visitou todos os planetas", "Acertou 10 perguntas seguidas").

### 4. ⚡ Estratégia de Carregamento em Fases (6-Phases Prefetch)

Para garantir uma experiência "instantânea", o frontend (`usePrefetchAllData.ts`) implementa um **pipeline de hydration** em 6 estágios, que roda silenciosamente em background:

1. **Fase 1 (Crítica)**: Dashboard (LCP). Carrega dados para a Home.
2. **Fase 2 (Navegação)**: Primeiras 3 páginas de TODAS as listagens (Personagens, Naves, etc).
3. **Fase 3 (Conteúdo Rico)**: Detalhes completos de todos os filmes.
4. **Fase 4 (Big Data)**: Carrega datasets massivos (100+ itens) para gerar os gráficos da página de Relatórios.
5. **Fase 5 (Social)**: Perfil do usuário, conquistas, ranking e desafios diários.
6. **Fase 6 (Bulk Quiz)**: Baixa centenas de perguntas potenciais para que o Jedi Trials funcione offline/sem delay.

*Tudo isso ocorre sem bloquear a thread principal, utilizando `setTimeout` e gerenciamento de prioridades do React Query.*

### 5. 🛡️ Middleware de Cache Inteligente

O backend não confia apenas no browser. Implementamos um **ETag Middleware Global** (`etag_middleware.py`) que:

- Intercepta todas as respostas JSON.
- Gera um hash **SHA-256** do conteúdo.
- Compara com o header `If-None-Match` da requisição.
- Retorna `304 Not Modified` (0 bytes de corpo) se os dados não mudaram, economizando banda e processamento do cliente.

### 6. 🖼️ Image Lookup & Fallback Strategy

A SWAPI oficial não entrega imagens. O `ImageLookupService` implementa uma estratégia de **resolução em camadas**:

1. **Databank Index**: Tenta cruzar o nome do recurso com um índice de imagens extraído do Databank oficial de Star Wars.
2. **Legacy Fallback**: Se falhar, busca em uma tabela local (`image_fallbacks`) mapeada manualmente para itens obscuros.
3. **Conservative Matching**: Utiliza algoritmos de normalização de strings (`casefold + strip`) para garantir que "X-Wing" encontre "x-wing fighter", mas retorna `None` se não houver certeza absoluta (evitando imagens erradas).

### 7. 📑 Paginação Abstrata (SWAPI Slicing)

A SWAPI força paginação de 10 itens. O frontend precisa de grids de 12, 8 ou 100 itens.
O módulo `swapi_pagination.py` resolve isso com **Virtual Slicing**:

- Calcula matematicamente quais páginas da SWAPI (ex: pág 3 e 4) contêm os itens do slice desejado (ex: itens 25 a 36).
- Busca **apenas** as páginas necessárias em paralelo (`asyncio.gather`).
- Combina os resultados e corta o array exato para o cliente.
- *Resultado: O frontend pode pedir `pageSize=100` e o backend orquestra 10 chamadas paralelas à SWAPI de forma transparente.*

### 8. 🎮 Gamification Engine (Jedi Trials)

O sistema de engajamento (`gamification_service.py`) não é apenas um contador de pontos.

- **Behavioral Achievements**: Conquistas como "Amigo de Yoda" ou "Lacaio de Vader" são desbloqueadas analisando o histórico de interações com personas específicas (`chat_stats_by_persona`).
- **Live XP & Ranks**: O cálculo de nível é instantâneo, utilizando uma curva de progressão baseada no XP acumulado (Youngling $\to$ Padawan $\to$ Knight $\to$ Master).
- **Leaderboard Aggregation**: Consultas SQL otimizadas agregam estatísticas complexas em tempo real, calculando precisão (% de acertos) e melhores sessões de quiz para o ranking global.

---

## 🔗 Integração & Protocolos de Dados (End-to-End)

A arquitetura de comunicação com a SWAPI foi desenhada para ser resiliente e invisível ao usuário final. Abaixo, detalho o fluxo completo de uma requisição.

### 1. Protocolo de Cliente (SWAPIClient)

O `SWAPIClient` (`src/app/infrastructure/external/swapi/client.py`) atua como um gateway inteligente:

- **Http Keep-Alive**: Utiliza `httpx.AsyncClient` para manter conexões persistentes, reduzindo o *overhead* de handshake TCP/TLS em múltiplas requisições.
- **Transparent Pagination**: O método `_paginate_all` abstrai a lógica de cursores `next` da API, iterando automaticamente até consumir todos os dados quando necessário (ex: para relatórios).
- **Url Normalization**: O cliente normaliza URLs e IDs automaticamente, garantindo que `https://swapi.dev/api/people/1/` e `https://swapi.dev/api/people/1` sejam tratados como o mesmo recurso no cache.

### 2. Fluxo de Dados (Sequence Diagram)

O diagrama abaixo ilustra o caminho de uma requisição simples (ex: "Listar Naves") e como o sistema decide entre Cache, API Externa e Image Lookup.

```mermaid
sequenceDiagram
    participant UI as Frontend (React Query)
    participant API as FastAPI Backend
    participant Cache as Memory Cache (TTL)
    participant SWAPI as SWAPI.dev
    participant DB as PostgreSQL (Images Setup)

    UI->>API: GET /starships?page=1&pageSize=12
    API->>Cache: GET swapi:starships:page:1
    
    alt Cache Miss (Primeiro Acesso)
        API->>SWAPI: GET /starships/?page=1 & page=2 (Parallel)
        SWAPI-->>API: JSON Raw Data
        
        API->>DB: Resolve Image URLs (Virtual Join)
        DB-->>API: URLs das Naves
        
        API->>API: Normaliza Dados (snake_case, números)
        API->>Cache: SET swapi:starships:page:1 (TTL 1h)
        API-->>UI: JSON Otimizado + Imagens
    else Cache Hit
        Cache-->>API: Dados Prontos
        API-->>UI: Resposta Instantânea (<10ms)
    end
```

### 3. Tratamento e Normalização de Dados

A SWAPI retorna dados "sujos" para os padrões modernos (strings para números, snake_case misto).
O `StarWarsApp` implementa uma camada de **Data Sanitization**:

- **Number Parsing**: O utilitário `parse_swapi_number` converte strings complexas como `"unknown"`, `"n/a"`, ou ranges `"30-165"` em tipos numéricos seguros (`Optional[float]`) para permitir ordenação e gráficos corretos.
- **Date Standardization**: Todas as datas são convertidas para ISO-8601 estrito.
- **Cross-Reference Resolving**: URLs de relacionamento (ex: `pilots: [...]`) são mantidas como referência mas preparadas para *lazy loading* no frontend.

### 4. 🔐 Protocolo de Autenticação Segura (JWT + Cookie)

Implementamos o padrão **Silent Refresh** para segurança máxima:

- **Access Token**: Curta duração (15min), armazenado em memória (JavaScript), usado como Bearer Token.
- **Refresh Token**: Longa duração (7 dias), armazenado em **Cookie HttpOnly (Secure, SameSite)**, inacessível via JS.
- **Token Rotation**: A cada refresh, o token anterior é invalidado e um novo é emitido, prevenindo replay attacks.

```mermaid
sequenceDiagram
    participant U as User
    participant F as Frontend
    participant B as Backend
    participant D as Database
    
    U->>F: Login com Google
    F->>B: Envia Credencial Google
    B->>D: Verifica/Cria User
    B-->>F: Retorna Access Token + User Info
    B-->>U: Set-Cookie: refresh_token (HttpOnly)
    
    Note over F,B: Navegação Segura
    
    F->>B: GET /api/v1/characters (Bearer Access)
    B-->>F: 200 OK
    
    Note over F,B: Access Token Expira
    
    F->>B: GET /api/v1/characters
    B-->>F: 401 Unauthorized
    F->>B: POST /auth/refresh (Cookie Automático)
    B->>D: Valida Refresh Token
    B-->>F: Novo Access Token
    B-->>U: Set-Cookie: Novo refresh_token
    F->>B: Retry Requisição Original
```

### 5. 🤖 Motor de Chat Contextual (ChatService)

O `chat_service.py` é o cérebro da aplicação, orquestrando mais de 2.000 linhas de lógica condicional e IA.

- **Intent Routing**: Antes de chamar a LLM, o sistema analisa a intenção com heurísticas regex. Ex: "Quem é Luke?" consulta diretamente o banco local/SWAPI, economizando tokens e latência.
- **RAG Pipeline**:
    1. **Extract Entities**: Identifica "Luke", "Tatooine" na frase.
    2. **Hybrid Search**: Busca vetorial + palavras-chave no banco de conhecimento.
    3. **Context Injection**: Injeta snippets JSON (ex: stats de força) no system prompt.
    4. **Persona Tuning**: Ajusta a resposta para o estilo "Yoda" (inversão sintática) ou "Vader".

---

## 📚 Documentação Técnica (Deep Dive)

Para desenvolvedores que desejam entender os detalhes internos, documentamos todos os subsistemas críticos diretamente aqui:

<details>
<summary><strong>🤖 Engenharia de IA & NLP</strong> (Clique para expandir)</summary>

### 🏗️ Pipeline de Processamento de Intenção

O sistema não envia simplesmente a mensagem do usuário para a LLM. Existe um pipeline rigoroso para garantir precisão factual e economizar tokens.

```mermaid
flowchart TD
    UserInput["🗣️ Mensagem do Usuário"] --> PreProcess["🔧 Pré-processamento"]
    PreProcess --> Routing{⚡ Roteamento de Intenção}
    
    Routing -- "Regex/Padrão Fixo" --> DirectReply["📝 Resposta Direta (Sem LLM)"]
    Routing -- "Pergunta Complexa" --> RAG["🔍 RAG Search (Context Recovery)"]
    
    RAG -- "Dados Encontrados" --> ContextInj["💉 Injeção de Contexto (JSON)"]
    ContextInj --> PromptEng["🎭 Engenharia de Persona"]
    PromptEng --> LLM["🤖 Invocação da IA"]
    
    LLM --> Response["💬 Resposta Final"]
    DirectReply --> Response
```

### 1. Pré-processamento Crítico

Antes de qualquer busca, aplicamos higienização especializada para Star Wars:

- **Droid Name Protection**: O algoritmo protege padrões como "R2-D2", "C-3PO", "BB-8" para que não sejam quebrados durante a normalização.
  - *Problema*: "R2 D2" normalizado vira `['r2', 'd2']`.
  - *Solução*: Regex identifica `\br2[\s\-]?d2\b` e converte para token único `R2-D2` antes da tokenização.

### 2. Roteamento de Intenção (Intent Routing)

O `_route_structured_intent` tenta resolver a dúvida sem gastar IA:

1. **Entidade Explícita**: Se o usuário diz "Quem é Luke?", o sistema extrai "Luke", busca na SWAPI e responde com template fixo.
2. **Perguntas de Categoria**: "O R2-D2 é um robô?". O sistema verifica a categoria ("robot") na lista de categorias do personagem e responde Booleanamente.

---

### 🔍 Motor RAG (Retrieval-Augmented Generation)

O arquivo `rag_search.py` implementa um motor de busca híbrido otimizado para português.

#### Algoritmo de Busca

Utilizamos uma combinação de técnicas para encontrar a entidade correta (Personagem, Planeta, Nave) mesmo com erros de digitação.

| Técnica               | Biblioteca/Implementação   | Objetivo                                                           |
| :-------------------- | :------------------------- | :----------------------------------------------------------------- |
| **Fuzzy Matching**    | `rapidfuzz` (Levenshtein)  | Corrigir typos ("Anakin Skywaler" → "Skywalker")                   |
| **Stemming PT-BR**    | Custom `RSLP` simplificado | Reduzir palavras ("correndo" → "corr", "filmes" → "film")          |
| **Stopwords Removal** | Lista customizada          | Remover ruído ("o", "a", "de", "para") mas manter "Darth", "Lord"  |
| **Alias Mapping**     | Dicionário estático        | Mapear apelidos ("Padme", "Ani", "Imperador") para nomes canônicos |

#### Context Injection Strategy

Quando uma entidade é encontrada (ex: "Luke Skywalker"), o sistema injeta um **Snippet JSON** no System Prompt da LLM.

**System Prompt Exemplo:**

```text
DADOS SWAPI (referência factual):
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

Regras:
- Para atributos que estejam nos dados, use os valores acima como fonte de verdade.
- Não invente números se não estiverem aqui.
```

Isso elimina alucinações sobre dados "duros" (altura, peso, cor) enquanto permite que a IA improvise sobre personalidade e lore.

---

### 🎭 Engenharia de Personas

O `YodaAIService` gerencia a personalidade da resposta. O "System Prompt" é trocado dinamicamente:

#### Mestre Yoda (`persona="yoda"`)

- **Instrução**: "Responda em português do Brasil no estilo do Yoda, invertendo a ordem das frases quando possível."

- **Permissões**: Pode usar emojis (🌟, ⚔️).
- **Tom**: Sábio, calmo, levemente humorado.

#### Darth Vader (`persona="vader"`)

- **Instrução**: "Voz fria, autoritária e intimidadora. Use onomatopeias de respiração (*pshhh... khhh*)."

- **Restrições**: **PROIBIDO** usar emojis.
- **Tom**: Hostil, impaciente, superior.

</details>

<details>
<summary><strong>🎮 Mecânicas de Gamificação</strong> (Clique para expandir)</summary>

### 📈 Sistema de XP e Níveis (Rankings)

A progressão do usuário é baseada em **Acúmulo de XP (Experiência)**. O cálculo de ranking é feito em tempo real sempre que o XP total é alterado.

#### Tabela de Rankings (`JediRank`)

| XP Necessário   | Ranking (Título)         | Descrição                                   |
| :-------------- | :----------------------- | :------------------------------------------ |
| **0 - 99**      | 🧒 **Youngling**          | Iniciante na Força.                         |
| **100 - 299**   | 🧘 **Iniciado**           | Começando o treinamento.                    |
| **300 - 699**   | 🗡️ **Padawan**            | Aprendiz de um Mestre.                      |
| **700 - 1499**  | ⚔️ **Cavaleiro Jedi**     | Defensor da paz na galáxia.                 |
| **1500 - 2999** | 🧙‍♂️ **Mestre Jedi**        | Grande sabedoria e poder.                   |
| **3000 - 4999** | 🏛️ **Membro do Conselho** | Liderança da Ordem Jedi.                    |
| **5000+**       | 🌌 **Grão-Mestre**        | O auge da conexão com a Força (Nível Yoda). |

*Fonte: `app/domain/enums/jedi_rank.py`*

---

### 💰 Fontes de XP

Como o usuário ganha experiência:

1. **Quiz (Jedi Trials)**
    - **+10 XP** por resposta correta.
    - *Fórmula*: `xp = acertos * 10`
    - Não há penalidade para erros.

2. **Desafio Diário**
    - **+30 XP** fixos ao completar a meta do dia.
    - *Exemplo*: "Envie 3 mensagens para o Yoda hoje".

3. **Conquistas (Achievements)**
    - O valor varia por conquista (veja tabela abaixo).
    - XP concedido apenas uma vez (ao desbloquear).

---

### 🏆 Conquistas (Achievements) e Triggers

As conquistas são verificadas a cada interação (`_apply_achievement_rules` em `gamification_service.py`). Algumas são baseadas em *comportamento* e não apenas em números.

| ID                 | Nome                 | XP   | Condição de Desbloqueio (Trigger)                                 |
| :----------------- | :------------------- | :--- | :---------------------------------------------------------------- |
| `primeiro_contato` | **Primeiro Contato** | +50  | Realizar a primeira interação (Chat ou Busca).                    |
| `explorador`       | **Explorador**       | +100 | Realizar **10 buscas** no Holocron.                               |
| `amigo_yoda`       | **Amigo de Yoda**    | +150 | Enviar **5 mensagens** conversando com a persona **Yoda**.        |
| `lacaio_vader`     | **Lacaio de Vader**  | +150 | Enviar **5 mensagens** conversando com a persona **Darth Vader**. |

#### Lógica de Detecção de Persona

O sistema conta mensagens separadamente para cada `persona` nas conversas:

```python
# Pseudocódigo da regra
if yoda_messages >= 5: unlock("amigo_yoda")
if vader_messages >= 5: unlock("lacaio_vader")
```

Isso incentiva o usuário a experimentar diferentes modos de interação.

---

### 📊 Leaderboard (Ranking Global)

O Leaderboard (`get_quiz_leaderboard`) utiliza agregação SQL para classificar os melhores jogadores.

**Critérios de Desempate:**

1. **Maior Score** em uma única sessão de Quiz (`best_score`).
2. (Implícito) Ordem de chegada no banco de dados.

O sistema também calcula a **Precisão (Accuracy)**:
`Accuracy = (Total Acertos / Total Perguntas) * 100`

---

### 🎲 Geração de Desafios Diários (Daily)

Atualmente, o desafio diário é gerado deterministicamente baseado na data:

- **ID**: `daily_chat_{YYYY-MM-DD}`
- **Meta**: Enviar 3 mensagens.
- **Reset**: A contagem reinicia à meia-noite (UTC).

</details>

<details>
<summary><strong>🚀 Guia de Deploy em Produção</strong> (Clique para expandir)</summary>

### 📦 Visão Geral da Infraestrutura

O projeto utiliza uma arquitetura **Serverless Containerized** no GCP:

- **Compute**: Google Cloud Run (Containers Stateless).
- **Registry**: Google Artifact Registry (Armazenamento de imagens Docker).
- **Secrets**: Google Secret Manager (Gestão segura de credenciais).
- **Auth**: Google IAM (Service Accounts para runtime).

---

### 🛠️ Pré-requisitos

Antes de executar, você precisa ter instalados:

1. **Google Cloud SDK (`gcloud`)**: Autenticado (`gcloud auth login`).
2. **Docker Desktop**: Rodando localmente (para build da imagem).
3. **PowerShell**: Terminal para execução do script.

---

### 📜 O Script de Deploy (`deploy-starwars.ps1`)

O script automatiza 6 etapas críticas que, manualmente, levariam horas.

#### Passo 1: Autenticação e Configuração

Verifica se `gcloud` e `docker` estão acessíveis e define o `PROJECT_ID` alvo.

#### Passo 2: Habilitar APIs

Ativa os serviços necessários no projeto GCP:

- `run.googleapis.com` (Cloud Run)
- `secretmanager.googleapis.com` (Secrets)
- `artifactregistry.googleapis.com` (Docker Repo)
- `iam.googleapis.com` (Permissões)

#### Passo 3: Service Account de Runtime

Cria uma identidade dedicada para o backend rodar (`star-wars-cloudrun-runtime`).

- **Por que?** Para não usar a conta "Default Compute" que tem permissões demais.
- **Permissões**: Atribui `roles/secretmanager.secretAccessor` para que o backend possa ler a senha do banco e chaves de API.

#### Passo 4: Artifact Registry

1. Verifica se o repositório Docker (`cloud-run`) existe na região.
2. Se não existir, cria automaticamente.
3. Configura o `docker-credential-gcr` para permitir push.

#### Passo 5: Build & Push

1. Executa `docker build` usando `Dockerfile.cloud-run`.
    - *Nota*: Usa uma imagem base leve (`python:3.12-slim`).
2. Executa `docker push` para enviar a imagem para o Artifact Registry.

#### Passo 6: Deploy no Cloud Run

Sobe o serviço com as seguintes configurações de produção:

- **Memória**: 512Mi (Otimizado para Free Tier).
- **CPU**: 1 vCPU.
- **Auto-scaling**: 0 a 1 instância (para evitar custos quando ocioso, "scale to zero").
- **Env Vars**: Injeta variáveis não-sensíveis (DB Host, CORS).
- **Secrets**: Monta os segredos (`holocron-db-password`, `holocron-jwt-secret-key`) como variáveis de ambiente.

---

### 🔑 Gestão de Segredos (Secrets)

O script **NÃO** cria os segredos. Você deve criá-los manualmente uma única vez no Console GCP ou via CLI:

```bash
# Exemplo: Criando o segredo do JWT
printf "minha-chave-super-secreta" | gcloud secrets create holocron-jwt-secret-key --data-file=-

# Exemplo: Criando o segredo do Banco
printf "senha-do-banco" | gcloud secrets create holocron-db-password --data-file=-
```

### Segredos Obrigatórios

- `holocron-jwt-secret-key`: Para assinar tokens de autenticação.

- `holocron-db-password`: Senha do PostgreSQL.

### Segredos Opcionais

- `holocron-openai-api-key`: Se `AI_ENABLED=true`.

---

### 🔄 Comandos Úteis

#### Deploy Rápido (Default)

```powershell
.\deploy-starwars.ps1
```

#### Deploy em Outra Região

```powershell
.\deploy-starwars.ps1 -Region "us-central1"
```

#### Logs de Erro

Se o container falhar ao subir, verifique os logs no GCP:

```bash
gcloud run services logs read star-wars-backend
```

</details>
</details>

<details>
<summary><strong>🎨 UX & Frontend Architecture</strong> (Clique para expandir)</summary>

### 📱 State Management Strategy

Utilizamos uma estratégia híbrida para gerenciamento de estado:

1. **Server State (React Query / TanStack)**:
    - Dados da API (Personagens, Filmes, User Profile).
    - Cache, retries e revalidação automática.
    - *Exemplo*: `useQuery(['characters', page], fetchCharacters)`.

2. **Client/UI State (Zustand)**:
    - Estados globais de interface não persistentes.
    - Sem necessidade de Providers complexos (Context API Hell).
    - *Exemplo*: `useImageEditModeStore` para controlar modais de edição de imagem.

---

### 🔐 Auth UX Pattern (Silent Refresh)

Para evitar que o usuário seja deslogado bruscamente ou veja erros 401 na tela:

- **Refresh Token**: Armazenado em Cookie `HttpOnly` (inacessível via JS).
- **Strategy**: O endpoint `/auth/refresh` retorna **204 No Content** (ao invés de 401) se não houver sessão.
  - Isso permite que o frontend decida suavemente se mostra o botão "Login" ou "Perfil", sem estourar exceções no console.

---

### ⚡ Performance & Caching (Backend Side)

O backend implementa o `ETagMiddleware` (`etag_middleware.py`) para otimizar a transferência de dados e reduzir a latência:

1. **Algoritmo de Hashing**: Interceptamos todo response JSON e calculamos um hash **SHA-256** do corpo (`hexdigest`).
2. **Negociação de Conteúdo (RFC 7232)**:
    - O servidor sempre envia `Cache-Control: private, max-age=0, must-revalidate`. Isso força o navegador a *sempre* perguntar ao servidor "isso mudou?" antes de usar o cache.
    - Se o header `If-None-Match` da requisição bater com o hash calculado:
        - Retornamos status **304 Not Modified**.
        - **CRITICAL**: Removemos o corpo da resposta e o header `Content-Length`, reduzindo o payload de KB/MB para ~0 bytes.
3. **Segurança de Cache**:
    - Adicionamos `Vary: Origin, Authorization` para garantir que um usuário nunca receba o cache privado de outro (ex: dados de perfil).
    - O middleware reconstrói o iterador de resposta (`response.body_iterator`) para garantir que o stream possa ser consumido tanto pelo hash quanto pelo cliente final.

</details>
</details>

<details>
<summary><strong>📐 Quality Assurance & Data Architecture</strong> (Clique para expandir)</summary>

### 🧪 Estratégia de Testes (QA)

Mantemos a qualidade do código com uma suíte de testes dividida em duas camadas:

1. **Backend (Pytest)**:
    - Foco em **Unit Tests** isolados para regras de negócio (`GamificationService`, `ChatService`).
    - Testes de integração garantem que os contratos da API (`schemas`) sejam respeitados.

2. **Frontend (Vitest)**:
    - Testes unitários rápidos para Hooks e Stores (`useImageEditModeStore`).
    - Garante que a lógica de UI (ex: toggles, formatação) funcione sem renderizar o app inteiro.

### 💾 Engenharia de Dados

A robustez dos dados é garantida por trẽs pilares:

1. **Validação Rígida (Pydantic V2)**:
    - Entradas e Saídas da API são tipadas.
    - Settings do app usam validadores customizados para parsear CSV/JSON de variáveis de ambiente (`cors_allow_origins`).

2. **Migrações de Banco (Alembic)**:
    - Versionamento de schema do PostgreSQL.
    - O `env.py` foi customizado para injetar o `PYTHONPATH` dinamicamente, permitindo rodar migrações mesmo em ambientes complexos de container.

3. **Logging & Observability**:
    - Configuração centralizada (`alembic.ini`, `custom loggers`) para rastrear erros silenciosos em produção.

</details>

---

## 🛡️ Infraestrutura & Segurança (DevSecOps)

A segurança não é um "add-on", mas parte do design da infraestrutura cloud-native.

### 1. 🔑 Gestão de Segredos (Secrets Management)

Adotamos uma estratégia de **Zero Hardcoded Secrets**.

- **Frontend (Vercel)**: As chaves públicas (Google Client ID) e URLs de API são injetadas em tempo de build via variáveis de ambiente da Vercel. Nenhuma chave privada toca o bundle do cliente.
- **Backend (Google Cloud Run)**: Segredos críticos (DB Password, JWT Secret, OpenAI Key) são gerenciados pelo **GCP Secret Manager**. Eles são montados no container como variáveis de ambiente em tempo de execução, garantindo que nem mesmo o Dockerfile tenha acesso a eles.

### 2. 🐳 Pipeline de Conteinerização Segura

O `Dockerfile.cloud-run` segue as melhores práticas de hardening:

- **Minimal Base Image**: Baseado em `python:3.12-slim` para reduzir drasticamente a superfície de ataque (menos binários vulneráveis).
- **Stateless by Design**: O container não retém dados. Uploads e persistência são delegados para serviços externos (Storage/PostgreSQL).
- **Auto-Migrations**: O comando de entrypoint executa `alembic upgrade head` a cada deploy, garantindo que o esquema do banco esteja sempre sincronizado com o código da aplicação (Infrastructure as Code).

### 3. 💾 Persistência e Resiliência

Embora a aplicação seja altamente dependente de cache, o **PostgreSQL** serve como fonte da verdade para dados críticos:

- **Perfis de Usuário**: Dados sensíveis e progresso de gamificação.
- **Fallback de Imagens**: Nossa tabela `image_fallbacks` atua como um sistema de failover. Se o CDN de imagens externo falhar, o sistema reverte automaticamente para ativos curados armazenados no banco.

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

O projeto foi auditado seguindo princípios rigorosos de segurança de software, alinhados com o OWASP Top 10 e regras corporativas de compliance.

#### 9.1 Acesso e Identidade (RBAC & Invoker)

- **Cloud Run Invoker**: O backend não é público. Ele opera em modo `authenticated-only`, aceitando apenas requisições com um token OIDC válido assinado pelo Google (via Service Account da Vercel). Ninguém consegue acessar a API diretamente sem passar pelo frontend.

- **RBAC (Role-Based Access Control)**: Internamente, endpoints administrativos validam o token JWT. Apenas usuários autenticados (`require_authenticated_user_id`) podem persistir dados ou gerar relatórios complexos.

#### 9.2 Prevenção de Vulnerabilidades (OWASP)

| Vulnerabilidade                | Estratégia de Mitigação Implementada                                                                                           |
| :----------------------------- | :----------------------------------------------------------------------------------------------------------------------------- |
| **SQL Injection**              | Uso estrito de SQLAlchemy ORM com *parameterized queries*. Nenhuma string SQL é concatenada manualmente.                       |
| **XSS (Cross-Site Scripting)** | React 19 com auto-escaping por padrão. Cookies sensíveis (`refresh_token`) marcados como `HttpOnly` para impedir roubo via JS. |
| **Sensitive Data Exposure**    | Segredos gerenciados por **GCP Secret Manager**. Logs sanitizados para não vazar PII (Personal Identifiable Information).      |
| **Broken Access Control**      | Middleware de verificação de token em todas as rotas protegidas (`Depends(require_authenticated_user_id)`).                    |

#### 9.3 Cloud Run Private Access Diagram

Este grafo mostra como o acesso ao backend é blindado.

```mermaid
%%{title: "Cloud Run Private Access & API Shielding"}%%
flowchart LR
    subgraph External_World ["External World"]
        User[Usuário]
        Hacker[Atacante]
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
    
    %% Fluxo do Usuário
    User -- HTTPS --> Vercel
    Hacker -. "Direct Access (403 Forbidden)" .-> CloudRun
    
    %% Autenticação Service-to-Service
    Vercel -- "OIDC ID Token (Auth)" --> CloudRun
    
    %% Backend Acessando Recursos
    CloudRun -- "Internal Traffic" --> DB
    CloudRun -- "Load API Keys" --> Secrets
    
    %% Shielding: O Backend protege as chaves e limita o rate-limit
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

A API REST segue os padrões OpenAPI 3.0. Documentação interativa disponível em `/docs` (Swagger UI).

### 🔐 Autenticação (`/api/v1/auth`)

| Método | Endpoint              | Descrição                                      | Auth   |
| :----- | :-------------------- | :--------------------------------------------- | :----- |
| POST   | `/google`             | Login via Google OAuth (Credential One-Tap)    | ❌     |
| POST   | `/refresh`            | Renova Access Token usando Refresh Cookie      | Cookie |
| POST   | `/logout`             | Invalida sessão e limpa cookies                | ✅     |
| GET    | `/me`                 | Retorna perfil do usuário autenticado          | ✅     |

### 👤 Personagens (`/api/v1/characters`)

| Método | Endpoint          | Descrição                                      | Auth |
| :----- | :---------------- | :--------------------------------------------- | :--- |
| GET    | `/`               | Lista personagens com filtros e paginação      | ❌   |
| GET    | `/{id}`           | Detalhes de um personagem específico           | ❌   |

**Query Params:** `page`, `pageSize`, `search`, `gender`, `homeworld`, `species`, `film`, `sort`

### 🎬 Filmes (`/api/v1/films`)

| Método | Endpoint          | Descrição                                      | Auth |
| :----- | :---------------- | :--------------------------------------------- | :--- |
| GET    | `/`               | Lista todos os filmes da saga                  | ❌   |
| GET    | `/{id}`           | Detalhes de um filme específico                | ❌   |

### 🚀 Naves (`/api/v1/starships`)

| Método | Endpoint          | Descrição                                      | Auth |
| :----- | :---------------- | :--------------------------------------------- | :--- |
| GET    | `/`               | Lista naves com filtros e paginação            | ❌   |
| GET    | `/{id}`           | Detalhes de uma nave específica                | ❌   |

**Query Params:** `page`, `pageSize`, `search`, `starship_class`, `manufacturer`, `film`, `sort`

### 🌍 Planetas (`/api/v1/planets`)

| Método | Endpoint          | Descrição                                      | Auth |
| :----- | :---------------- | :--------------------------------------------- | :--- |
| GET    | `/`               | Lista planetas com filtros e paginação         | ❌   |
| GET    | `/{id}`           | Detalhes de um planeta específico              | ❌   |

**Query Params:** `page`, `pageSize`, `search`, `climate`, `terrain`, `film`, `sort`

### 👽 Espécies (`/api/v1/species`)

| Método | Endpoint          | Descrição                                      | Auth |
| :----- | :---------------- | :--------------------------------------------- | :--- |
| GET    | `/`               | Lista espécies com filtros e paginação         | ❌   |
| GET    | `/{id}`           | Detalhes de uma espécie específica             | ❌   |

**Query Params:** `page`, `pageSize`, `search`, `classification`, `designation`, `language`, `film`, `sort`

### 🚗 Veículos (`/api/v1/vehicles`)

| Método | Endpoint          | Descrição                                      | Auth |
| :----- | :---------------- | :--------------------------------------------- | :--- |
| GET    | `/`               | Lista veículos com filtros e paginação         | ❌   |
| GET    | `/{id}`           | Detalhes de um veículo específico              | ❌   |

**Query Params:** `page`, `pageSize`, `search`, `vehicle_class`, `manufacturer`, `film`, `sort`

### 🤖 Chat com IA (`/api/v1/chat`)

| Método | Endpoint          | Descrição                                      | Auth |
| :----- | :---------------- | :--------------------------------------------- | :--- |
| POST   | `/`               | Envia mensagem e recebe resposta da IA         | ✅   |
| GET    | `/history`        | Histórico de conversas do usuário              | ✅   |

**Body (POST):**

```json
{
  "message": "Quem é Luke Skywalker?",
  "persona": "yoda"  // ou "vader"
}
```

### 🎮 Gamificação (`/api/v1/gamification`)

| Método | Endpoint              | Descrição                                      | Auth |
| :----- | :-------------------- | :--------------------------------------------- | :--- |
| GET    | `/profile`            | Perfil de gamificação (XP, Rank, Stats)        | ✅   |
| GET    | `/achievements`       | Lista de conquistas do usuário                 | ✅   |
| GET    | `/leaderboard`        | Ranking global de usuários                     | ❌   |
| GET    | `/daily-challenge`    | Desafio diário atual                           | ✅   |
| POST   | `/quiz/start`         | Inicia uma sessão de quiz                      | ✅   |
| POST   | `/quiz/answer`        | Responde uma pergunta do quiz                  | ✅   |
| POST   | `/quiz/finish`        | Finaliza quiz e recebe XP                      | ✅   |

### 📊 Metadados (`/api/v1/metadata`)

| Método | Endpoint                      | Descrição                                      | Auth |
| :----- | :---------------------------- | :--------------------------------------------- | :--- |
| GET    | `/characters/homeworlds`      | Lista de planetas natais únicos                | ❌   |
| GET    | `/characters/species`         | Lista de espécies únicas                       | ❌   |
| GET    | `/characters/genders`         | Lista de gêneros únicos                        | ❌   |
| GET    | `/planets/climates`           | Lista de climas únicos                         | ❌   |
| GET    | `/planets/terrains`           | Lista de terrenos únicos                       | ❌   |
| GET    | `/species/classifications`    | Lista de classificações únicas                 | ❌   |
| GET    | `/species/designations`       | Lista de designações únicas                    | ❌   |
| GET    | `/species/languages`          | Lista de idiomas únicos                        | ❌   |
| GET    | `/starships/classes`          | Lista de classes de naves únicas               | ❌   |
| GET    | `/starships/manufacturers`    | Lista de fabricantes de naves únicos           | ❌   |
| GET    | `/vehicles/classes`           | Lista de classes de veículos únicas            | ❌   |
| GET    | `/vehicles/manufacturers`     | Lista de fabricantes de veículos únicos        | ❌   |

### 🖼️ Imagens (`/api/v1/image-fallbacks`)

| Método | Endpoint          | Descrição                                      | Auth |
| :----- | :---------------- | :--------------------------------------------- | :--- |
| GET    | `/`               | Lista todos os fallbacks de imagem             | ❌   |
| POST   | `/`               | Cria ou atualiza fallback de imagem            | ✅   |
| DELETE | `/{id}`           | Remove um fallback de imagem                   | ✅   |

### ❤️ Health Check (`/api/v1/health`)

| Método | Endpoint          | Descrição                                      | Auth |
| :----- | :---------------- | :--------------------------------------------- | :--- |
| GET    | `/`               | Status de saúde da API                         | ❌   |
| GET    | `/ready`          | Readiness probe (para Kubernetes/Cloud Run)    | ❌   |

---

## 🎨 Design System

A interface do Holocron Analytics foi projetada para proporcionar uma experiência imersiva no universo Star Wars.

### 🎨 Paleta de Cores

| Token CSS                | Hex         | Uso                                       |
| :----------------------- | :---------- | :---------------------------------------- |
| `--color-primary`        | `#35e6ff`   | Cor principal (Neon Cyan)                 |
| `--color-secondary`      | `#ff35a0`   | Cor de destaque (Magenta)                 |
| `--color-background`     | `#0a0a12`   | Fundo principal (Space Black)             |
| `--color-surface`        | `#1a1a2e`   | Cards e superfícies elevadas              |
| `--color-text-primary`   | `#ffffff`   | Texto principal                           |
| `--color-text-secondary` | `#8b8b9a`   | Texto secundário                          |
| `--color-success`        | `#00ff87`   | Estados de sucesso                        |
| `--color-warning`        | `#ffcc00`   | Estados de atenção                        |
| `--color-error`          | `#ff4444`   | Estados de erro                           |

### ✨ Efeitos Visuais

- **Glassmorphism**: Cards com `backdrop-filter: blur(12px)` e bordas translúcidas.
- **Neon Glow**: Sombras coloridas (`box-shadow`) para elementos interativos.
- **Starfield Dinâmico**: Background animado com partículas em CSS/JS.
- **Hover Transitions**: Efeitos suaves com `transform` e `opacity` (0.2s ease).

### 🧩 Componentes Reutilizáveis

| Componente              | Localização                        | Descrição                                       |
| :---------------------- | :--------------------------------- | :---------------------------------------------- |
| `CustomSelect`          | `shared/components/CustomSelect`   | Dropdown estilizado com tema Star Wars          |
| `FilmFilter`            | `shared/components/FilmFilter`     | Filtro global por filme (7 filmes)              |
| `PageLayout`            | `shared/components/PageLayout`     | Layout base com header, content, comandos       |
| `Pagination`            | `shared/components/Pagination`     | Navegação de páginas responsiva                 |
| `ScrollToTop`           | `shared/components/ScrollToTop`    | Botão flutuante para voltar ao topo             |
| `StarfieldEvents`       | `shared/components/StarfieldEvents`| Background animado com meteoros                 |
| `DetailsModal`          | `shared/components/DetailsModal`   | Modal de detalhes com glassmorphism             |
| `FallbackEditableImage` | `shared/components/...`            | Imagem com fallback e edição inline             |

### 🪝 Hooks Customizados

| Hook                    | Arquivo                              | Descrição                                       |
| :---------------------- | :----------------------------------- | :---------------------------------------------- |
| `useFilmOptions`        | `shared/hooks/useFilmOptions.ts`     | Options formatadas para FilmFilter              |
| `useMetadataOptions`    | `shared/hooks/useMetadataOptions.ts` | 10+ variantes para filtros de entidades         |
| `usePrefetchAllData`    | `shared/hooks/usePrefetchAllData.ts` | Pipeline de prefetch em 6 fases                 |
| `useImageFallback`      | `shared/hooks/useImageFallback.ts`   | Gestão de fallback de imagens                   |

---

## 📋 Variáveis de Ambiente

### Backend (`.env` ou GCP Secret Manager)

```env
# 🔌 Banco de Dados
DATABASE_URL=postgresql://user:password@host:5432/dbname

# 🔐 Autenticação
JWT_SECRET_KEY=sua-chave-secreta-256-bits
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=15

# 🌐 Google OAuth
GOOGLE_CLIENT_ID=seu-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=seu-client-secret

# 🤖 OpenAI
OPENAI_API_KEY=sk-...
AI_ENABLED=true
OPENAI_MODEL=gpt-4o

# 🔗 CORS
CORS_ALLOW_ORIGINS=http://localhost:5173,https://seu-dominio.vercel.app

# 📊 Ambiente
ENVIRONMENT=development  # ou production
LOG_LEVEL=INFO
```

### Frontend (`.env` ou Vercel Environment Variables)

```env
# 🔗 API
VITE_API_URL=http://localhost:8000/api/v1

# 🌐 Google OAuth (Chave Pública)
VITE_GOOGLE_CLIENT_ID=seu-client-id.apps.googleusercontent.com

# ⚙️ Configuração
VITE_APP_TITLE=Holocron Analytics
```

---

## 💻 Stack Tecnológico Detalhado

### Backend (Python 3.12)

| Categoria     | Tecnologia                     | Versão  | Uso                                      |
| :------------ | :----------------------------- | :------ | :--------------------------------------- |
| **Framework** | FastAPI                        | 0.109   | API REST async de alta performance       |
| **ORM**       | SQLAlchemy                     | 2.0     | Mapeamento objeto-relacional             |
| **Migrations**| Alembic                        | 1.13    | Versionamento de schema do banco         |
| **Validation**| Pydantic                       | 2.9     | Validação de dados e schemas             |
| **Database**  | PostgreSQL                     | 9.5+    | Banco relacional principal               |
| **Cache**     | cachetools (TTLCache)          | 5.5     | Cache em memória com TTL                 |
| **AI**        | OpenAI SDK                     | 1.66    | Integração com GPT-4o                    |
| **NLP**       | rapidfuzz                      | 3.10    | Fuzzy matching (Levenshtein)             |
| **HTTP**      | httpx                          | 0.27    | Cliente HTTP async                       |
| **Auth**      | python-jose                    | 3.3     | JWT encoding/decoding                    |
| **Security**  | passlib + bcrypt               | 1.7     | Hashing de senhas                        |

### Frontend (Node.js 20+)

| Categoria     | Tecnologia                     | Versão  | Uso                                      |
| :------------ | :----------------------------- | :------ | :--------------------------------------- |
| **Framework** | React                          | 19.0    | Biblioteca de UI declarativa             |
| **Language**  | TypeScript                     | 5.6     | Tipagem estática                         |
| **Bundler**   | Vite                           | 6.0     | Build tool ultra-rápido                  |
| **State**     | Zustand                        | 5.0     | Estado global leve                       |
| **Data**      | TanStack Query                 | 5.62    | Cache e fetching de dados servidor       |
| **Charts**    | Recharts                       | 3.7     | Gráficos SVG responsivos                 |
| **Styling**   | CSS Modules                    | -       | Estilos com escopo local                 |
| **Routing**   | React Router                   | 7.1     | Navegação SPA                            |

### Infraestrutura

| Categoria     | Tecnologia                     | Uso                                      |
| :------------ | :----------------------------- | :--------------------------------------- |
| **Container** | Docker + Docker Compose        | Desenvolvimento e produção               |
| **Backend**   | Google Cloud Run               | Hospedagem serverless do backend         |
| **Frontend**  | Vercel                         | Hospedagem e CDN do frontend             |
| **Secrets**   | GCP Secret Manager             | Gestão segura de credenciais             |
| **Registry**  | Google Artifact Registry       | Repositório de imagens Docker            |

---

## 🚀 Como Executar

### Pré-requisitos

- Docker & Docker Compose (Recomendado)

### Executando com Docker

1. Na raiz do projeto:

    ```bash
    docker-compose -f docker-compose.dev.yml up -d --build
    ```

2. Acesse:
    - **Frontend**: `http://localhost:5173`
    - **Docs**: `http://localhost:8000/docs`

---

## 👨‍💻 Desenvolvedor

Projeto entregue para o Desafio Técnico PowerOfData.

> *"Faça ou não faça. Tentativa não há."* — Mestre Yoda
