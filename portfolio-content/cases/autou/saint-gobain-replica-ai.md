# Case — Replica AI (Saint-Gobain: Replicação de Projetos de Savings entre Fábricas)

**Tipo:** AutoU (cliente: Saint-Gobain — Quartzolit / Brasilit)
**Papel:** Desenvolvedor Full Stack — backend, pipeline de recomendação e integrações
**Status:** Em produção (pipeline diário via Cloud Scheduler)
**Stack:** Python, FastAPI, Flask, Google Cloud (Cloud Run Jobs/Service, Cloud Scheduler, Firestore, Cloud Storage, Pub/Sub, Cloud Tasks, Cloud Logging), PostgreSQL, Pandas/OpenPyXL, PyJWT, Bubble (frontend legado) com plano de migração React, integração SAID (API corporativa Saint-Gobain), Pytest, Docker

> Nota de confidencialidade: projeto de cliente da AutoU — validar o que pode ser público antes de expor nome/detalhes.

## Contexto e problema

A Saint-Gobain roda milhares de projetos de savings (redução de custo industrial) nas fábricas. Um projeto que funcionou numa fábrica de Quartzolit provavelmente funciona em outra do mesmo cluster — mas não havia mecanismo sistemático de replicação: a descoberta dependia de reuniões e conhecimento tribal. Além disso, a base de savings migrou do controle em planilha/Bubble para o sistema corporativo SAID, exigindo re-integração do pipeline.

## Solução

Plataforma de recomendação de replicação de projetos:

- **Pipeline de recomendação** que lê a base de savings do SAID (`V_PROJECT_SAVINGS_BRAZIL`), normaliza e filtra (negócio, dificuldade, CP), calcula recomendações de projetos por **cluster de fábricas** para Quartzolit e Brasilit e grava a matriz cross em Postgres
- **Execução como Cloud Run Job** disparado diariamente (seg–sex 06:00) pelo Cloud Scheduler, com Service Flask fino (mesma imagem) expondo endpoints para disparo manual, sync isolado e polling de status pelo frontend
- **Backend da plataforma (FastAPI)**: autenticação, CRUD dinâmico de coleções operacionais, extração de XLSX com worker assíncrono, analytics LRM00 (labor, maintenance, RMP, outros), **auditoria e rollback** de operações

## Arquitetura e decisões técnicas

- **Job vs. Service separados na mesma imagem**: nada de pipeline rodando dentro do processo HTTP — os POSTs apenas disparam execuções do Cloud Run Job e respondem `202` na hora; `409` se já houver execução em andamento (lock de concorrência)
- **Sync idempotente por hash** na etapa SAID (upsert), com flags para recorte de status e desativação de registros que sumiram da fonte
- **Migração Bubble→SAID sem quebrar a operação**: feature flags de ambiente (`SAID_SYNC_ENABLED`, `BUBBLE_ENABLED`) permitiram transição gradual mantendo o front Bubble funcionando
- **Auditoria e rollback como cidadãos de primeira classe** no backend FastAPI — operações reversíveis em dados operacionais críticos
- **Processamento assíncrono** de extrações XLSX via worker interno + Pub/Sub/Cloud Tasks
- **Ambiente local de verdade**: script que copia o Postgres de produção (read-only) para container local e roda o pipeline inteiro offline — debugging seguro de um pipeline de produção
- Suíte pytest com mocks de Firebase/GCP; autenticação por token de app (`X-App-Token`) nos endpoints de disparo

## Desafios e soluções

- **Fonte de dados em migração (planilha → Bubble → SAID)**: pipeline desenhado para trocar a origem sem tocar no cálculo, com sync desacoplado do recálculo
- **Segurança em disparos HTTP de jobs**: token de aplicação, lock de execução única e status legível por polling
- **Analytics industriais (LRM00)** com regras por categoria de custo implementadas como módulos separados e testados

## Resultados e impacto

- Recomendações de replicação recalculadas automaticamente todo dia útil, sem intervenção manual
- Migração para o SAID concluída mantendo continuidade da operação [datas/volume A CONFIRMAR]
- Operação com auditoria/rollback: erros de carga deixam de ser irreversíveis

## Destaques para entrevista (STAR resumido)

- **S/T:** multinacional industrial sem mecanismo sistemático de replicar projetos de savings entre fábricas, e com a base migrando de Bubble para o sistema corporativo SAID. **A:** trabalhei no pipeline de recomendação por cluster como Cloud Run Job diário com Service fino de controle (disparo/status), sync idempotente por hash com feature flags de transição, e no backend FastAPI com auditoria, rollback e analytics de custos. **R:** recomendação diária automática em produção e migração de fonte de dados concluída sem interrupção da operação.
