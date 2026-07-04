# Índice de Cases Profissionais — Wesley de Carvalho

Cases criados a partir da análise dos workspaces reais (`D:\freela-workspace` e `D:\AutoU_workspace`) em 03/07/2026. Servem de fonte para: currículo, RAG do portfólio e a futura aba de **Projetos Profissionais** do site.

> Marcadores `[A CONFIRMAR]` indicam métricas que só o Wesley pode validar (volumes, prazos, percentuais). Cases de clientes AutoU têm nota de confidencialidade — validar o que pode ser exibido publicamente (nome do cliente vs. "grande banco", "farmacêutica nacional" etc.).

## Freelance (full cycle: proposta → produto → deploy; exceção: entre-pontos, atuação só no frontend)

| Case | Projeto | Stack núcleo | Status |
|---|---|---|---|
| [entre-pontos-integrador](freelas/entre-pontos-integrador.md) | Renovação visual e refatoração do frontend do integrador EDI logístico | Next.js 16 + React 19 + Tailwind 4 | Produção |
| [aog-dux-truck](freelas/aog-dux-truck.md) | Sistema de operação logística emergencial (AOG) | Java 21 + Spring Boot 3 Clean Arch + Angular 20 + Entra ID | Produção |
| [dux-logistics-workflow](freelas/dux-logistics-workflow.md) | Plataforma de workflow logístico/documental (substitui BPM Fluig-like) | Java + Spring + Angular + Postgres | Completo, em homologação |
| [dux-nf-automacao-fiscal](freelas/dux-nf-automacao-fiscal.md) | Automação de NF-e por e-mail com IA em camadas | FastAPI + React + MS Graph + Postgres | Produção |
| [whatsapp-bot-tickets-sol](freelas/whatsapp-bot-tickets-sol.md) | Sol — central omnichannel de atendimento TI (WhatsApp/Teams/web/e-mail) com IA, termômetro de satisfação e CRM integrado | FastAPI + Angular 20 + pgvector + Gemini + Evolution/Meta API | Produção |
| [dash-qualtrics-cx](freelas/dash-qualtrics-cx.md) | Dashboard CX por jornada + MCP server Qualtrics | FastAPI + Angular + Gemini + TS (MCP) | Produção |
| [gerador-de-cracha](freelas/gerador-de-cracha.md) | Gerador de crachás em lote (Supermercados Rio Sul) | Python + PyInstaller | Entregue |
| [notas-vue-spring](freelas/notas-vue-spring.md) | App de anotações + comparativo técnico Vue/React/Angular | Vue 3 + Spring Boot + SQLite | Estudo |
| [mercearia-rv](freelas/mercearia-rv.md) | Mercearia R&V — sistema desktop offline-first de estoque/vendas (PDV, caixa, fidelidade) | Java 21 + Spring Boot + Angular 20 + Electron + Postgres embarcado | Produção |
| [experimenta-ai-soneca](freelas/experimenta-ai-soneca.md) | Experimenta AI (Soneca) — POS de lanchonete com impressão ESC/POS + ecossistema delivery (rastreamento tempo real) | Java + Spring multi-module + Angular 17 + Electron + MySQL + Google Maps/OAuth | POS completo; delivery em homologação |

Não viraram case (sem implementação): `pricing-end` (só escopo em PDF) e `proposta comercial` (PPTXs de venda — mas evidenciam atuação comercial/pré-venda como freelancer, útil pro texto do currículo).

## AutoU (fev/2026 – atual, Desenvolvedor Full Stack)

| Case | Cliente/Produto | Stack núcleo | Status |
|---|---|---|---|
| [jgv-previsao-demanda](autou/jgv-previsao-demanda.md) | JGV — previsão de demanda e recomendação de estoque (autopeças) | Python + Prophet + Flask + Sankhya + Postgres | Produção |
| [pulse-visao-computacional](autou/pulse-visao-computacional.md) | Rede São Roque — conformidade de postos com visão computacional | YOLO + FastAPI + LangGraph/Gemini + AWS + GCP | Produção |
| [saint-gobain-replica-ai](autou/saint-gobain-replica-ai.md) | Saint-Gobain — replicação de projetos de savings entre fábricas | FastAPI + Cloud Run Jobs + Firestore/GCS/PubSub | Produção |
| [libbs-lis-assistente-sac](autou/libbs-lis-assistente-sac.md) | Libbs — triagem de tickets SAC com IA (demo para edital em andamento) | FastAPI + React 19 + Gemini c/ fallback | Demo no ar (edital em andamento) |
| [oxiquimica-plataforma-ped](autou/oxiquimica-plataforma-ped.md) | Oxiquímica — P&D de formulações com otimização Bayesiana (BayBE) | FastAPI + React 19 + Vertex AI + BayBE | Produção |
| [rocester-catalogo-inteligente](autou/rocester-catalogo-inteligente.md) | Rocester — catálogo de peças com ingestão de PDF por IA | FastAPI + React + Gemini Vision + pgvector | Produção |
| [aura-central-autou](autou/aura-central-autou.md) | Aura Central — feature de notificações e logs em plataforma B2B (monorepo DDD) | FastAPI + React + eventos + database-per-service | Produção |
| [autou-website](autou/autou-website.md) | Site institucional AutoU (SEO, blog/cases, leads, CMS) — solo | React + FastAPI + CMS próprio + Azure | No ar |
| [itau-demo](autou/itau-demo.md) | Demo de pré-venda para Itaú (mapas Leaflet) | React 19 + Tailwind 4 + Leaflet | Entregue |

Não viraram case: `bubble-mcp` (repositório de terceiros — nocoderoi — usado como ferramenta; citar como experiência com MCP, não como autoria), `pdi-autou`/`pdi-autou-des` (plano de desenvolvimento individual, não é projeto).

## Leitura transversal (matéria-prima pro currículo)

Padrões que se repetem e sustentam o posicionamento de **Engenheiro Full Stack experiente com especialização em IA aplicada**:

1. **Full cycle real**: proposta comercial → discovery → arquitetura → código → deploy → operação, em dezenas de projetos, sozinho (freelas) e em time (AutoU)
2. **Poliglota comprovado**: Java/Spring (Clean Architecture), Python/FastAPI (async), Node/Fastify, e os três frontends (Angular 20 Signals, React 18/19, Vue 3) — com comparativo técnico escrito
3. **IA aplicada com juízo de engenharia**: IA como fallback (Dux NF), com fallback (LIS), com curadoria humana (Rocester), com governança de fontes (Oxiquímica), com loop de retraining (Pulse) — nunca "IA porque sim"
4. **Multi-cloud operacional**: AWS (S3/Lambda/DynamoDB), GCP (Cloud Run Jobs, Scheduler, Pub/Sub, VMs), Azure (Entra ID, Graph), Oracle Cloud (VPS free tier para MVPs de custo zero)
5. **Clientes enterprise**: Saint-Gobain — exposição direta em ambiente de startup acelerada (Itaú foi demo de pré-venda e Libbs é demo para edital ainda em andamento — nenhum dos dois é cliente; os clientes exibidos no site da AutoU incluem L'Oréal, Stellantis, Nestlé, B3, PRIO, Petrobras, Embraer etc., mas o Wesley só cita nos materiais os que ele atendeu diretamente)
6. **Dados e ML clássico além de LLM**: Prophet (séries temporais), YOLO (visão), BayBE (otimização Bayesiana), pgvector/FAISS (embeddings)

## Próximas fases (combinadas)

1. ✅ Cases criados (esta pasta)
2. ✅ Validação do Wesley: statuses confirmados (AutoU todos no ar; NF/AOG no ar; workflow em homologação; Mercearia em produção; Soneca em homologação final) — métricas `[A CONFIRMAR]` e anonimização ainda pendentes
3. ✅ Currículo (`Curriculo-Wesley-Pleno.html` + PDF), markdowns de RAG (`CURRICULO.md`, `STACKS.md`, `trabalhos/`, versões -english) atualizados em 03/07/2026
4. ⬜ Refatorar seção de projetos do portfólio: aba **Profissionais** (destaque, alimentada por estes cases) + aba **Pessoais** (atual)
