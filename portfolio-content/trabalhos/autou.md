# Experiência Profissional - AutoU (Startup de IA Aplicada)

## Sobre a AutoU

A **AutoU** é uma startup que constrói soluções de **IA aplicada** para empresas — visão computacional, agentes de IA, modelos preditivos e plataformas de dados — com projetos para clientes enterprise como **Saint-Gobain, Rocester, Oxiquímica e redes de varejo/combustíveis** (além de demos enterprise, como a de pré-venda para o Itaú e a construída para concorrer a edital da Libbs, ainda em andamento). O ambiente é acelerado, com alta exposição a clientes e foco em entrega com qualidade e ritmo veloz.

### Contexto de Atuação

- Projetos para empresas de grande porte, **todos em produção**
- Stack core: **Python (FastAPI, LangGraph)** no backend e **React 19 + Vite** no frontend
- Infraestrutura multi-cloud: **AWS** (EC2, S3, Lambda, DynamoDB), **Google Cloud** (Cloud Run, Cloud Run Jobs, Scheduler, Pub/Sub, VMs), **Azure**
- CI/CD e deploy: **GitHub Actions**, **Docker Compose**, deploy automatizado

## Experiências na Empresa

### Desenvolvedor Fullstack

*Período: Fevereiro 2026 - Atual | Remoto*

#### Visão Computacional em Produção 24/7 (rede de postos de combustível)

- Pipeline **YOLO rodando em edge** (PC no posto consumindo câmeras RTSP), eventos consolidados em **AWS (S3, Lambda, DynamoDB)**
- **Pipeline agêntico LangGraph + Gemini + RAG** para análise de ocorrências, insights e notificações por e-mail/WhatsApp
- **Loop de retraining**: feedback de falsos positivos dos usuários vira dataset de re-treino — o modelo melhora com o uso
- **Observabilidade implementada por mim**: Prometheus + Grafana em VM stateful própria, monitorando custo, uso e infraestrutura

#### Machine Learning e Previsão de Demanda (rede de autopeças)

- Algoritmo preditivo com **Prophet** (séries temporais) para previsão de demanda por produto/filial
- Recomendações de **compra, transferência entre filiais e produtos substitutos**, integradas ao **ERP Sankhya**
- Execução diária automatizada em produção

#### Plataforma de P&D com Otimização Bayesiana (indústria química)

- Plataforma de formulações com **BayBE** (framework open-source da Merck) para sugerir a próxima formulação a testar — menos ciclos físicos de estufa
- Agente de IA **"Colibri"** que gera e ajuda em fórmulas; chat científico com **RAG e governança de fontes** (whitelist/blacklist)
- **Observabilidade Grafana + Prometheus implementada por mim**: custo de IA, consumo e infraestrutura

#### Pipeline de Replicação de Savings (Saint-Gobain)

- **Cloud Run Jobs + Cloud Scheduler** com sincronização **idempotente por hash**, auditoria e rollback
- Backend FastAPI de administração; execução diária em produção

#### Assistente de Triagem SAC com IA (demo para edital da Libbs — projeto solo, edital em andamento)

- MVP full stack feito sozinho como demo para concorrer a edital da farmacêutica: chat público com **triagem por Gemini e fallback determinístico por regras**, transbordo humano, portal interno com timeline de tickets
- Uma aplicação servindo dois domínios (chat público + portal interno) — demo no ar; edital ainda em andamento

#### Catálogo Inteligente de Peças (Rocester — fundação do projeto)

- Participação na fundação: arquitetura com **camada de IA desacoplada** (inversão de dependência) e base do pipeline de **extração de PDFs com Gemini Vision**
- Score de confiança com reasoning por peça e **curadoria humana em massa**; **pgvector** para busca semântica — em produção

#### Site Institucional da AutoU (projeto solo)

- Site completo feito sozinho: frontend React otimizado para **SEO** (blog, cases), backend FastAPI de leads e **CMS próprio** — no ar em Azure

#### Plataforma B2B de Gestão de Pessoas (Aura Central — monorepo DDD)

- **Feature de notificações**: serviço dedicado consumindo eventos dos bounded contexts via Pub/Sub, sem acoplar domínios
- **Sistema de logs** da plataforma, dando visibilidade de operação em produção
- Trabalho dentro de arquitetura **DDD com 5 bounded contexts e database-per-service**

#### Frontend de Demo Enterprise (Itaú — em dupla)

- Interface pixel-perfect a partir de Figma com **mapas interativos (React 19 + Leaflet)**, sob prazo curto de pré-venda

#### Integrações Corporativas

- **ERP Sankhya/Microwork** via API: automação de relatórios, orçamentos e fluxos de vendas
- **Slack**: notificações em tempo real; **Outlook / Microsoft 365**: e-mails transacionais

**Tecnologias Utilizadas:**

- Python, FastAPI, LangGraph, Prophet, BayBE
- React 19, Vite, TypeScript
- LLMs (Gemini, Gemini Vision), RAG, pgvector, FAISS, YOLO
- AWS (EC2, S3, Lambda, DynamoDB), Google Cloud (Cloud Run, Cloud Run Jobs, Scheduler, Pub/Sub), Azure
- Prometheus, Grafana
- GitHub Actions, Docker, Docker Compose
- Sankhya/Microwork, Slack API, Microsoft 365 / Outlook

## Conquistas e Aprendizados

- **Todos os projetos em que atuei estão em produção** — de visão computacional 24/7 a pipelines diários de dados
- IA aplicada com juízo de engenharia: fallback determinístico, curadoria humana, governança de fontes e loop de retraining — nunca "IA porque sim"
- Observabilidade de produção (Prometheus/Grafana) implementada por iniciativa própria, incluindo monitoramento de **custo de IA**
- Exposição direta a clientes enterprise (Saint-Gobain) e a pré-venda/editais enterprise (demos para Itaú e para edital da Libbs) em ambiente de startup acelerada
- ML além de LLMs: séries temporais (Prophet), visão computacional (YOLO) e otimização Bayesiana (BayBE)
