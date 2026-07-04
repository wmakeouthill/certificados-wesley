# Currículo - Wesley de Carvalho Augusto Correia

## Informações Pessoais

- **Nome Completo:** Wesley de Carvalho Augusto Correia
- **GitHub:** [wmakeouthill](https://github.com/wmakeouthill)
- **LinkedIn:** [wcacorreia](https://www.linkedin.com/in/wcacorreia)
- **Email:** <wcacorreia1995@gmail.com>
- **Telefone:** +55 21 98386-6676
- **WhatsApp:** [+55 21 98386-6676](https://wa.me/5521983866676)
- **Portfólio:** [wmakeouthill.dev](https://wmakeouthill.dev)

## Resumo Profissional

Engenheiro Full Stack atuando do desenho da arquitetura ao monitoramento em produção, com foco em **eficiência operacional** e em produtos que geram **ganho real de produtividade no dia a dia das empresas**. Concentro a atuação em **automação de fluxos manuais**, **integração de IA aplicada** (LLMs, RAG, Visão Computacional + YOLO, modelos preditivos com Prophet, otimização Bayesiana com BayBE) e **integrações com sistemas corporativos** (ERPs Sankhya/Microwork e SAP, Slack, Microsoft 365 / Outlook / Graph, Microsoft Entra ID) — reduzindo retrabalho, evitando ruptura de estoque, acelerando decisão comercial e encurtando ciclos de venda.

Atuo em duas frentes profissionais simultâneas: na **AutoU** (startup de IA aplicada, projetos para clientes enterprise) e como **freelancer full cycle**, com múltiplos sistemas próprios **em produção** para clientes reais — da proposta comercial ao deploy e operação, sozinho. Entrego software escalável e cloud-native em **AWS**, **GCP** e **Azure** — e em **VPS dedicada** (Oracle Cloud Always Free) para cargas previsíveis 24/7 — com pipelines de CI/CD, containerização e **observabilidade ponta a ponta** (Prometheus/Grafana, incluindo monitoramento de custo de IA), sob **Clean Architecture, SOLID** e código sustentável. Stack core: **Java + Spring Boot 3.x** e **Python (FastAPI, LangGraph)**, com **Angular** e **React** no front (e Vue no repertório). Bacharel em Direito — base que agrega leitura analítica de regras de negócio e domínios regulatórios.

## Experiência Profissional

### Desenvolvedor FullStack (Full Cycle) - AutoU

*Período: Fev 2026 - Presente | Remoto*

Projetos de IA aplicada para clientes enterprise (Saint-Gobain, entre outros) — todos **em produção** — além de demos enterprise: pré-venda para o Itaú e edital em andamento para a Libbs:

- **Visão computacional em produção 24/7:** pipelines de Visão Computacional (YOLO em edge) integrados a LLMs via LangGraph e RAG para monitoramento de conformidade em rede de postos — análise de imagens, insights automatizados e loop de retraining alimentado por feedback dos usuários (AWS S3/Lambda/DynamoDB + GCP).
- **Observabilidade implementada por mim (Prometheus + Grafana):** monitoramento de custo de IA, consumo e infraestrutura em produção nos projetos de visão computacional e P&D químico.
- **Machine Learning e otimização de estoque:** algoritmos com Prophet para predição de demanda, otimização de estoque, transferências entre filiais e sugestão de produtos substitutos, integrados ao ERP Sankhya (rede de autopeças).
- **Plataforma de P&D com otimização Bayesiana:** plataforma de formulações químicas com BayBE (framework da Merck) e agente de IA "Colibri" — em produção para indústria de fertilizantes.
- **Pipeline de replicação de projetos de savings (Saint-Gobain):** Cloud Run Jobs + Scheduler com sincronização idempotente por hash, auditoria e rollback — execução diária em produção.
- **Assistente de triagem SAC com IA (demo para edital de farmacêutica, em andamento):** MVP solo — chat público com triagem por Gemini e fallback determinístico por regras, portal interno de tickets — no ar como demonstração.
- **Ingestão de PDF, embeddings e busca semântica:** participação na fundação de plataforma de catálogo inteligente — extração de catálogos PDF com Gemini Vision, score de confiança com curadoria humana, pgvector para busca semântica.
- **Site institucional da AutoU (solo):** frontend React otimizado para SEO, backend FastAPI de leads e CMS próprio de artigos/cases — no ar em Azure.
- **Plataforma B2B de gestão de pessoas (monorepo DDD):** feature de notificações (serviço dedicado consumindo eventos dos bounded contexts) e sistema de logs, respeitando database-per-service e comunicação assíncrona por Pub/Sub.
- **Frontend de demo enterprise (Itaú):** interface pixel-perfect a partir de Figma com mapas interativos (React 19 + Leaflet), em dupla, sob prazo de pré-venda.
- **Integrações corporativas (ERP Sankhya/Microwork, Slack & Outlook/Microsoft 365):** automação de relatórios, orçamentos, notificações em tempo real e e-mails transacionais.
- **Infraestrutura multi-cloud e CI/CD:** AWS (EC2, S3, Lambda, DynamoDB), GCP (Cloud Run, Cloud Run Jobs, Scheduler, Pub/Sub, VMs), Azure; Docker Compose, GitHub Actions e deploy automatizado em produção.

### Desenvolvedor Full Stack - Freelancer (Produtos Próprios e Clientes Diretos)

*Período: 2025 - Presente | Remoto*

Atuação **full cycle real**: proposta comercial → discovery → arquitetura → código → deploy → operação e suporte, como único desenvolvedor. Sistemas **em produção**:

- **AOG Dux Truck (em produção):** sistema de operação logística emergencial (aviation on ground) — Java 21 + Spring Boot 3 em Clean Architecture, Angular 20, autenticação Microsoft Entra ID. Cada demanda tem tela de acompanhamento própria com chat, comentários operador/cliente e timeline de eventos rastreável — reduzindo cobranças por e-mail/telefone.
- **Automação fiscal de NF-e (em produção):** captura de notas por e-mail (Microsoft Graph) com extração em camadas — XML determinístico → PDF → OCR/IA como fallback — FastAPI + React, eliminando digitação manual de notas.
- **Sol — Central omnichannel de atendimento TI com IA (em produção):** atendimento por WhatsApp, Teams, plataforma web e e-mail; relatórios automatizados, termômetro de satisfação por amostragem de conversas com pareceres por setor, painel completo de gestão de tickets e módulo de CRM integrado para campanhas — FastAPI + Angular 20 + pgvector + Gemini + Evolution/Meta API.
- **Dashboard CX Qualtrics (em produção):** dashboard de experiência do cliente por jornada (FastAPI + Angular + Gemini) + MCP server TypeScript para Qualtrics; build desktop portátil Windows com auto-update via GitHub Releases.
- **Plataforma de workflow logístico (completa, em homologação):** substitui BPM corporativo estilo Fluig — solicitações, filas por grupo, aprovações multi-etapa, documentos e SLAs — Java + Spring + Angular.
- **Mercearia R&V (em produção):** sistema desktop offline-first de estoque/vendas/PDV — Electron orquestrando Spring Boot + PostgreSQL embarcados em instalador único NSIS; uso diário na operação do cliente com custo recorrente zero.
- **Experimenta AI — Soneca (POS completo; delivery em homologação):** gestão de lanchonete com impressão de cupons ESC/POS multiplataforma + ecossistema de delivery próprio com PWAs de cliente e motoboy, rastreamento em tempo real (GPS → SSE) e Google Maps/OAuth.
- **Renovação de frontend de integrador EDI logístico:** refatoração visual completa em Next.js 16 + React 19 + Tailwind 4.
- **Gerador de crachás em lote:** ferramenta Python empacotada em executável para cliente de varejo (Supermercados Rio Sul).

### Estagiário - Backend / FullStack / ScrumTeam - Anbima / Selic (Banco Central)

*Período: Abr 2025 - Abr 2026 | Rio de Janeiro, RJ | Híbrido*

- **Modernização de infraestrutura financeira / sistema crítico:** migração Selic mainframe (COBOL) para arquitetura Java (Novo-Selic).
- **Observabilidade e monitoramento:** implementação de stack completa (Prometheus, Grafana, Actuator, Micrometer, Blackbox Exporter, Alertmanager), para análise de métricas de performance e healthcheck.
- **Desenvolvimento full stack:** Java (Spring) Backend + Angular Frontend.
- **DevOps e containerização:** Docker, CI/CD, versionamento de branches com GitLab para colaboração e práticas de deployment automatizado.
- **Gestão de dados:** Oracle (Containerizado) Database (SQL), versionamento de schemas com Liquibase / Scripts SQL.

### Estagiário - Projetos / Governança - Anbima / Selic (Banco Central)

*Período: Abr 2024 - Abr 2025 | Rio de Janeiro, RJ | Híbrido*

- **Gestão de Projetos:** ciclo de desenvolvimento de artefatos, relatórios executivos e controle de iniciativas estratégicas alinhadas ao PDTIC.
- **Business Intelligence:** criação de dashboards Power BI (DAX) interativos para visualização de KPIs e suporte à tomada de decisão executiva.
- **Desenvolvimento web:** webparts customizados SharePoint (JavaScript, HTML, CSS) integrados via SharePoint API para governança corporativa.
- **Soluções para C-level:** expositores de documentos e notícias institucionais para chefia do Banco Central e ANBIMA.
- **Frameworks de gestão:** aplicação prática de PMI, Agile, MPS.BR e CMMI para padronização e melhoria contínua de procedimentos e processos.
- **Gestão do conhecimento:** elaboração de conteúdos estratégicos e soluções low-code/no-code (Notion), para continuidade do negócio.

### Estagiário & Assistente Jurídico - Gondim, Albuquerque e Negreiros ADV

*Período: Nov 2019 - Abr 2024 | Rio de Janeiro, RJ | Presencial*

- **Diligências processuais e financeiras:** protocolos, questionamentos forenses, pagamentos de custas e depósitos judiciais, controle de pagamentos entre cliente-escritório e obrigações processuais.
- **Automação de processos:** desenvolvimento em Python, VBA e Selenium para web scraping de dados de diversos tribunais do Brasil + RPA: integração automatizada entre sistema interno e plataformas judiciais.
- **Otimização operacional:** redução do tempo de cadastro processual via scripts, melhorando fluxo de dados e produtividade.
- **Análise de dados jurídicos:** resumos de petições e gestão de informações processuais em sistemas internos.

### Aprendiz - Analytics / SalesForce - Phillip Morris Internacional

*Período: Out 2018 - Out 2019 | Rio de Janeiro, RJ | Presencial*

- **Automação VBA/Excel:** automações VBA/Excel para coleta automatizada de dados, geração de relatórios e envio email gerencial.
- **Controle de estoque:** gerenciei controle de estoque e distribuição de materiais promocionais (trade marketing) e de escritório.
- **Análise de vendas:** realizei análises de volume de vendas, KPIs comerciais e otimização de rotinas administrativas via macros.

### Aprendiz - Auxiliar Administrativo / Produção - Liquigás / Petrobras Distribuidora S.A

*Período: Abr 2017 - Set 2018 | Duque de Caxias, RJ | Presencial*

- **Gestão operacional:** atuei com Excel na gestão operacional. Input e leitura de dados no SAP.
- **Atendimento e apoio:** atendimento a clientes, ao centro de destrocas de botijões e fornecedor de GLP. Apoio na gestão de filas e suporte aos vendedores.
- **Controle de qualidade:** controle de qualidade e fiscalização na produção de botijões.

## Formação Acadêmica

### Graduação

- **Ciências da Computação** - 2024 a 2027 (Em andamento) - Faculdade GRAN
- **Direito** - 2018 a 2022 (Concluído) - Centro Universitário Unigama

### Pós-Graduação

- **Full Stack Java Developer** - 2025 a 2026 (Concluído) - Faculdade FACINT
- **Gestão de Projetos** - 2025 (Em andamento) - Centro Universitário Unigama

## Habilidades Técnicas

### Nível de Proficiência

**Avançado/Expert (Uso Profissional em Projetos Críticos):**

- **Java 17/21:** Linguagem principal, uso em sistemas críticos de infraestrutura financeira
- **Spring Boot 3.x:** Framework principal para backend enterprise
- **Spring Framework:** Ecossistema completo (Web, Data JPA, Security, Actuator)
- **Angular 17+/18:** Framework principal para frontend moderno
- **TypeScript 5.x:** Linguagem principal para frontend e desktop
- **RxJS 7.8:** Programação reativa em Angular
- **SQL/MySQL/PostgreSQL/Oracle:** Bancos relacionais em produção
- **Docker:** Containerização em todos os projetos
- **Git/GitHub/GitLab:** Controle de versão e CI/CD
- **Liquibase:** Versionamento de banco de dados
- **Prometheus/Grafana:** Observabilidade em sistemas críticos
- **Maven:** Gerenciamento de dependências Java
- **Lombok:** Redução de boilerplate

**Intermediário/Avançado (Uso Profissional Regular):**

- **React 19 + Vite:** Stack core em projetos de startup (frontend moderno)
- **Python:** Automações, scripts, web scraping e algoritmos preditivos (Prophet)
- **JavaScript/HTML5/CSS3/SCSS:** Base do frontend
- **Node.js:** Backend JavaScript quando necessário
- **Electron:** Aplicações desktop multiplataforma
- **Redis:** Cache distribuído
- **Power BI/DAX:** Dashboards e análise de dados executivos
- **Selenium:** Web scraping e automação de navegadores
- **VBA:** Automações em Excel e sistemas Microsoft
- **Spring Actuator/Micrometer:** Health checks e métricas
- **AWS / Google Cloud:** Ambientes cloud e deploy
- **Vercel:** Deploy de frontend e aplicações
- **Prophet (Python):** Algoritmos preditivos e séries temporais

**Intermediário (Conhecimento e Uso Ocasional):**

- **Kubernetes:** Orquestração de containers
- **NGINX:** Servidor web e proxy reverso
- **Google Cloud Platform:** Cloud computing e serverless
- **SharePoint:** Desenvolvimento web corporativo
- **Notion:** Gestão de conhecimento
- **Salesforce:** CRM e gestão de relacionamento

### Backend

- **Java 17/21** - Linguagem principal com recursos modernos (LTS), uso em sistemas críticos
- **Spring Boot 3.x** - Framework enterprise líder de mercado (3.2.3, 3.3.2, 3.5.5)
- **Spring Framework** - Ecossistema completo (Web, Data JPA, Security, Validation, Mail, Actuator)
- **Python 3.11+** - Linguagem para IA, dados, automação e backends
- **FastAPI** - APIs Python de alta performance (validação via Pydantic)
- **LangGraph** - Orquestração de fluxos agênticos com LLMs
- **Node.js + Express** - Backend JavaScript / TypeScript
- **C# / .NET 9** - APIs em ASP.NET Core (WebApi)
- **Liquibase / Alembic** - Versionamento de schema de banco (Java / Python)
- **Maven** - Gerenciamento de dependências e build
- **Lombok** - Redução de boilerplate (@RequiredArgsConstructor, @Builder, etc.)
- **JPA/Hibernate** - ORM padrão da indústria
- **REST APIs** - Arquitetura de comunicação padrão
- **gRPC** - Comunicação binária de alta performance (LoL Fazenda Inhouse)
- **Spring Security** - Autenticação e autorização (JWT)

### Frontend

- **Angular 17+/18/19/20** - Framework enterprise líder de mercado, versões modernas
- **React 19 + Vite** - Stack core em projetos de startup (frontend moderno e performático)
- **TypeScript 5.x** - Tipagem estática para desenvolvimento escalável (5.4.2, 5.7.2, 5.8)
- **RxJS 7.8** - Programação reativa (padrão enterprise)
- **HTML5** - Estrutura semântica moderna
- **CSS3/SCSS** - Estilização avançada e responsiva
- **JavaScript** - Linguagem base do frontend
- **Standalone Components** - Arquitetura moderna sem módulos (Angular 17+)
- **Signals** - Sistema de reatividade moderno (Angular 18+)
- **Reactive Forms** - Formulários reativos
- **Angular Material** - Componentes UI seguindo Material Design

### Mobile / Desktop

- **Electron 27/28** - Aplicações desktop multiplataforma (LoL Matchmaking, Mercearia R&V)
- **Ionic** - Apps híbridos web → iOS/Android
- **React Native** - Apps nativos Android/iOS

### IA & Dados

- **LLMs (Gemini, OpenAI)** - Integração com modelos de linguagem
- **RAG (Retrieval-Augmented Generation)** - Busca contextualizada em corpus próprio
- **Embeddings** - Geração e indexação semântica (Gemini)
- **FAISS** - Vector store em memória (Wesley Bot WhatsApp)
- **pgvector** - Vector store em PostgreSQL (AutoU)
- **LangGraph** - Orquestração de agentes com fluxo de estado
- **Prophet (Facebook)** - Séries temporais e predição
- **Visão Computacional (Vision + YOLO)** - Detecção de objetos e monitoramento por imagem
- **OpenCV** - Processamento de imagem em pipelines
- **DynamoDB** - NoSQL gerenciado AWS
- **Firebase** - Banco realtime e auth (mobile/web)

### Bancos de Dados

- **Oracle Database** - Banco relacional enterprise (sistemas críticos)
- **PostgreSQL** - Banco relacional robusto (embarcado em aplicações desktop, pgvector)
- **MySQL 8.0+** - Banco relacional enterprise em produção
- **Redis (Upstash)** - Cache distribuído cloud-native
- **SQLite** - Banco embarcado (AA Space, dev_task_manager)
- **DynamoDB** - NoSQL gerenciado AWS
- **Firebase** - Banco realtime e auth
- **SQL** - Consultas, otimização e gestão de dados

### DevOps/CI/CD

- **Docker** - Containerização (padrão da indústria), uso em todos os projetos
- **Docker Compose** - Orquestração de containers (configuração em produção)
- **GitHub Actions** - Pipelines de CI/CD e automação de workflows
- **Vercel** - Deploy de frontend e aplicações serverless
- **Google Cloud Run** - Serverless containers, deploy em produção
- **Cloud Build** - CI/CD automatizado no Google Cloud
- **CI/CD Pipelines** - Deploy automatizado (GitLab, GitHub Actions)
- **GitLab CI/CD** - Pipelines de CI/CD em projetos profissionais
- **NGINX** - Servidor web e proxy reverso
- **Kubernetes** - Orquestração de containers (conhecimento)
- **Certbot** - Certificados SSL automáticos
- **Multi-stage builds** - Otimização de imagens Docker

### Infraestrutura e Observabilidade

- **AWS (EC2, IAM, VPC, Security Groups, Secrets Manager)** - Ambientes cloud
- **Google Cloud Platform (Cloud Run, Cloud Build, IAM)** - Cloud computing e serviços gerenciados
- **VPS dedicada (Oracle Cloud Always Free)** - Cargas previsíveis 24/7
- **Serverless Containers** - Arquitetura serverless (Cloud Run)
- **Prometheus / Grafana** - Coleta, visualização e dashboards de métricas
- **Spring Actuator / Micrometer** - Health checks e métricas customizadas
- **Alertmanager / Blackbox Exporter** - Alertas e monitoramento de endpoints externos
- **Health Checks / Observabilidade** - Monitoramento ponta a ponta de sistemas críticos

### Segurança / DevSecOps

- **OWASP Top 10** - Prevenção de vulnerabilidades comuns (XSS, CSRF, injection)
- **Spring Security** - Framework de autenticação/autorização
- **JWT** - Tokens stateless para APIs
- **OAuth 2.0** - Login federado (Google) e fluxos delegados
- **RBAC** - Controle de acesso baseado em papéis
- **CORS** - Políticas de origem cruzada
- **API Key em header (X-API-Key)** - Autenticação de backends privados
- **AWS IAM / GCP IAM** - Identidades, papéis e políticas em cloud
- **VPC, Security Groups, Firewall, NAT** - Segurança de rede em cloud
- **Secrets Manager** - Gestão de credenciais

### Automação & BI

- **Selenium + RPA** - Web scraping e automação de navegadores em larga escala
- **VBA** - Automações em Excel e sistemas Microsoft
- **Power BI / DAX** - Análise de dados, dashboards executivos
- **SharePoint** - Webparts customizados (governança corporativa)

### Dev Tooling & AI Coding

- **IntelliJ IDEA** - IDE principal Java
- **VS Code** - Editor multiuso
- **Cursor** - Editor com IA agêntica
- **Antigravity** - IDE agêntica do Google
- **Claude Code (CLI)** - Assistente de código via terminal
- **Codex (CLI)** - Assistente de código OpenAI via terminal
- **GitHub Copilot** - Sugestões inline e Copilot CLI
- **Git, GitHub, GitLab** - Versionamento e colaboração

### Arquitetura e Metodologias

- **Clean Architecture** - Arquitetura limpa e modular
- **Clean Code** - Código legível, sustentável e testável
- **Design Patterns** - Padrões de projeto (Factory, Strategy, Observer, etc.)
- **Domain-Driven Design (DDD)** - Design orientado a domínio
- **Hexagonal Architecture (Ports & Adapters)** - Isolamento do domínio
- **SOLID** - Princípios de design orientado a objetos
- **DRY, KISS, YAGNI** - Princípios de redução de complexidade
- **ACID** - Garantias transacionais em bancos relacionais
- **Microservices patterns** - Padrões de microserviços
- **RESTful APIs / gRPC / WebSockets** - Comunicação síncrona, binária e em tempo real
- **Event-driven architecture** - Arquitetura orientada a eventos

## Projetos Principais

> Os projetos profissionais (freelance e AutoU) estão detalhados na seção de Experiência Profissional e nos cases em `portfolio-content/cases/`. Abaixo, os principais projetos pessoais — que complementam o repertório técnico.

### LoL Fazenda Inhouse

Plataforma de matchmaking competitivo para League of Legends com **FastAPI + gRPC + Angular 20 + Electron 28 + PostgreSQL/Alembic**, integração com **League Client (LCU)** e bot Discord (JDA). Demonstra ownership de produto end-to-end e migração arquitetural completa de Java/Spring/Redis para Python/gRPC com estado em memória + DB.

### Wesley Bot WhatsApp

Assistente conversacional com **RAG** (FastAPI + FAISS + Gemini + Evolution API), fluxo agêntico, exportação para XLSX e TTS, em produção 24/7 em **Oracle Cloud Always Free** (VPS dedicada).

### Publique Sua Notícia Popular

Plataforma full-stack para criação, edição e consumo de notícias (**Spring Boot 3.4 + Angular 21 + PostgreSQL 16**) com OAuth Google, JWT, editor em blocos e assistente editorial baseado em **LLM (Gemini)**.

### AA Space

Comunidade fechada de apoio (Node.js + Express + TypeScript + Angular 19 + SQLite + Socket.IO) com fórum, chats privados em tempo real, moderação e foco em privacidade. Projeto social/educacional para ampliar rede de apoio a pessoas em recuperação.

### Traffic Manager

Dashboard Angular 18 em tempo real para tráfego, tickets e monitoramento de servidores — signals, standalone components e Chart.js.

### Investment Calculator

Calculadora de investimentos em Angular 18 com projeções de juros compostos, signals e computed properties.

## Certificações

- Certificações em andamento ou planejadas (informações atualizadas no portfólio)

## Idiomas

- **Português:** Nativo
- **Inglês:** Avançado (leitura técnica, escrita e comunicação)

## Soft Skills

- **Boa Comunicação:** Comunicação clara e eficaz em diferentes contextos
- **Gestão de Conflitos:** Habilidade para resolver conflitos e trabalhar em equipe
- **Trabalho em Equipe:** Colaboração efetiva em equipes multidisciplinares
- **Hiperfoco / Proatividade:** Foco intenso em tarefas e iniciativa para resolver problemas
- **Inteligência Emocional:** Autocontrole e gestão emocional em situações de pressão
- **Autodidata:** Capacidade de aprender rapidamente novas tecnologias e conceitos
- **Adaptado a Metodologias Ágeis:** Experiência com Scrum, Agile, PMI, MPS.BR, CMMI
- **Análise e Solução de Problemas:** Identificação de gargalos e criação de soluções eficientes
- **Versatilidade:** Adaptação a diferentes contextos (grandes corporações ou ambientes dinâmicos)

## Diferenciais

- **Aprendizado Contínuo:** Sempre em busca de novos conhecimentos e tecnologias
- **Projetos Práticos:** Portfólio diversificado com projetos reais e funcionais
- **Arquitetura Moderna:** Experiência com Clean Architecture e DDD
- **Full-Stack:** Domínio completo do ciclo de desenvolvimento (Backend + Frontend + DevOps)
- **DevOps:** Experiência com deploy, CI/CD e infraestrutura cloud
- **Qualidade de Código:** Foco em código limpo, testável e manutenível
- **Experiência Diversificada:** Trabalhou em setores variados (jurídico, tabaco, energia, financeiro)
- **Automação:** Histórico comprovado de criação de automações que geram eficiência mensurável
- **Sistemas Críticos:** Experiência em sistemas de alta criticidade (infraestrutura financeira)
- **Metodologias Ágeis:** Trabalho em equipes Scrum e aplicação de frameworks de gestão (PMI, Agile, MPS.BR, CMMI)
- **Observabilidade:** Implementação completa de monitoramento e métricas em sistemas críticos
- **Migração de Sistemas:** Experiência em migração de sistemas legados (COBOL → Java moderno)

## Trajetória Profissional

### Evolução da Carreira

**2017-2018:** Início profissional em ambiente corporativo (Liquigás/Petrobras)

- Primeira experiência com sistemas ERP (SAP)
- Desenvolvimento de habilidades organizacionais e de atendimento

**2018-2019:** Primeira experiência em automação (Phillip Morris)

- Desenvolvimento de habilidades em VBA e Excel avançado
- Introdução a análise de dados e KPIs
- Experiência com Salesforce (CRM)

**2019-2024:** Transição para tecnologia através de automações (Escritório de Advocacia)

- Desenvolvimento de habilidades em Python, Selenium e RPA
- Aplicação prática de tecnologia para resolver problemas reais
- Redução significativa de tempo em processos através de automações

**2024-2025:** Gestão de projetos e governança (ANBIMA/Selic)

- Desenvolvimento de dashboards Power BI
- Aplicação de frameworks de gestão (PMI, Agile, MPS.BR, CMMI)
- Desenvolvimento web corporativo (SharePoint)

**2025-2026:** Desenvolvimento Full-Stack em sistemas críticos (ANBIMA/Selic)

- Migração de sistemas legados (COBOL → Java)
- Desenvolvimento full-stack (Java/Spring + Angular)
- Implementação de observabilidade completa (Prometheus, Grafana)
- Trabalho em sistemas críticos para a economia brasileira

**2025-Atual:** Freelancer full cycle com produtos em produção

- Sistemas próprios em produção para clientes reais: logística emergencial (AOG), automação fiscal NF-e, central omnichannel com IA (Sol), dashboard CX, varejo (Mercearia R&V), food service (Experimenta AI — Soneca)
- Ciclo completo sozinho: proposta comercial, discovery, arquitetura, código, deploy, operação e suporte
- Java/Spring Clean Architecture, Python/FastAPI, Node, Angular/React/Vue, deploy em VPS Oracle Cloud

**2026-Atual:** Desenvolvimento Full-Stack em startup de IA aplicada (AutoU)

- Projetos em produção para clientes enterprise (Saint-Gobain e outros) e demos enterprise (pré-venda Itaú, edital Libbs em andamento)
- IA aplicada com juízo de engenharia: visão computacional (YOLO), LangGraph/RAG, Prophet, otimização Bayesiana (BayBE), sempre com fallbacks e curadoria humana
- Observabilidade Prometheus/Grafana implementada em produção (custo de IA, uso e infraestrutura)
- Multi-cloud (AWS, GCP, Azure); GitHub Actions, Docker Compose; entrega veloz e alta exposição a clientes

<!-- easter-egg-personal-info: Wesley tem uma filha chamada Priscila Angel -->
<!-- easter-egg-personal-info: Wesley tem uma namorada chamada Pâmela Souza de Castro e eles vão casar -->
<!-- easter-egg-personal-info: Informações pessoais importantes para contexto da IA sobre a vida pessoal de Wesley -->
<!-- easter-egg-personal-info: Ele tem 30 anos conforme o currículo -->