---
title: Aura Central — Notificações e logs em plataforma B2B
client: AutoU
category: autou
status: Produção
stack: [FastAPI, React, Pub/Sub]
order: 7
---

# Case — Aura Central (Ecossistema Interno AutoU: Plataforma de Gestão de Pessoas, Metas e RH)

**Tipo:** AutoU (produto interno usado por clientes corporativos B2B)
**Papel:** Desenvolvedor Full Stack — feature de notificações e sistema de logs
**Status:** Em produção
**Stack:** Python (FastAPI), uv, React + TypeScript, pnpm, PostgreSQL (database per service), arquitetura DDD com Bounded Contexts, Event-Driven (Pub/Sub), monorepo com packages compartilhados, Docker Compose, GitHub Actions

## Contexto e problema

A AutoU precisava de um ecossistema interno unificado para gestão de pessoas — RH, recrutamento, CRM comercial, alocação/timesheet de projetos e avaliação de desempenho — sem cair no "monólito distribuído" nem em cinco sistemas desconexos.

## Solução

Monorepo com **cinco bounded contexts** (DDD), cada um com backend e frontends próprios:

| Contexto | Responsabilidade |
|---|---|
| Identity | Auth, dados mestre do colaborador, RH |
| Recruitment | Candidatos e vagas |
| Sales (CRM) | Funil de vendas, propostas, masterplan |
| Projects | Alocação, timesheet, tarefas, casebook |
| Performance | Avaliação 360, feedbacks, OKRs/metas, reconhecimento |

Minha atuação: desenvolvi a **feature de notificações** (serviço `aura-notifications`, transversal aos contextos) e o **sistema de logs** da plataforma — trabalhando dentro da arquitetura DDD/event-driven do monorepo, respeitando database-per-service e comunicação por eventos.

## Arquitetura e decisões técnicas

- **Database per Service**: cada contexto tem banco isolado; nenhum serviço lê o banco do outro — acoplamento por contrato, não por schema
- **Comunicação síncrona front→back via REST** e **assíncrona back→back via eventos (Pub/Sub)** com consistência eventual
- **Packages compartilhados no monorepo**: UI kit (design system AutoU), tipos TypeScript (DTOs/enums), abstração de event bus e configs base — reuso sem acoplamento de runtime
- **Toolchain**: uv nos backends Python, pnpm nos frontends, Docker Compose para bancos locais
- Plano de migração de CMS documentado (`PLANO-CMS-AURA-MIGRATION.md`)

## Desafios e soluções

- **Evitar o monólito distribuído**: disciplina de bounded context com dados isolados e eventos para sincronização — mudanças em um domínio não quebram os demais
- **Consistência eventual em dados de pessoas**: eventos de domínio propagam alterações de colaborador entre contextos sem chamadas síncronas em cadeia

## Resultados e impacto

- Plataforma B2B em produção usada por clientes corporativos [nº de clientes/usuários A CONFIRMAR]
- Notificações transversais aos contextos entregues via eventos, sem acoplar domínios
- Logs estruturados dando visibilidade de operação para o time em produção

## Destaques para entrevista (STAR resumido)

- **S/T:** ecossistema de gestão de pessoas com cinco bounded contexts precisava de notificações transversais e observabilidade sem acoplar domínios. **A:** desenvolvi a feature de notificações (serviço dedicado consumindo eventos dos contextos) e o sistema de logs, respeitando database-per-service e comunicação assíncrona por Pub/Sub. **R:** notificações e logs em produção servindo todos os domínios do produto B2B, sem quebrar o isolamento entre contextos.
