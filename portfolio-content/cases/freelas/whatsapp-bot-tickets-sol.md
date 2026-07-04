---
title: Sol — Central omnichannel de atendimento de TI com IA
client: Cliente corporativo
category: freela
status: Produção
stack: [FastAPI, Angular 20, pgvector, Gemini]
order: 5
---
# Case — Sol (Central Omnichannel de Atendimento de TI com IA e CRM)

**Tipo:** Freelance (cliente corporativo — atendimento de TI interno)
**Papel:** Desenvolvedor Full Stack (autoria completa: produto, backend, frontend, IA, infra e deploy)
**Status:** Em produção (com ambiente de homologação separado)
**Stack:** Python 3.11, FastAPI, SQLAlchemy async, Alembic, Angular 20 (standalone + Signals, TypeScript strict), PostgreSQL 16 + pgvector, Redis, Evolution API / Meta WhatsApp Cloud API, Microsoft Teams app, e-mail (mensagens), Gemini (`google-genai`) com migração planejada p/ Vertex AI, Docker Compose, deploy em VPS + Google Cloud

## Contexto e problema

A equipe de TI do cliente recebia solicitações de suporte de forma dispersa (WhatsApp pessoal, e-mail, boca a boca), sem fila, sem histórico e sem priorização. Era preciso estruturar o atendimento nos canais que os usuários já usam — sem forçar ninguém a aprender um portal novo — e dar à gestão visibilidade real sobre qualidade e volume de atendimento.

## Solução

Central de atendimento **omnichannel** com IA, gestão completa e CRM integrado:

- **Atendimento multicanal**: tickets tratados por **WhatsApp, Microsoft Teams, plataforma web e e-mail** (por mensagens) — mesma fila, mesmo histórico, independente do canal de entrada
- **Bot de triagem com IA (Gemini)**: conversa naturalmente com o usuário, entende o problema, classifica e abre o chamado com os dados certos; conversas livres também são suportadas; fallback por regras locais quando o LLM está indisponível
- **Painel completo de gestão de tickets (Angular 20)**: filas, conversas em tempo real, timeline por ticket, dashboards gerenciais — tudo relacionado ao ciclo de vida do chamado em um lugar
- **Termômetro de atendimento e satisfação**: análise por IA com **amostragem das conversas**, gerando parecer por setor e insights acionáveis para a gestão
- **Relatórios automatizados** de operação e qualidade de atendimento
- **Módulo de CRM integrado**: campanhas e recepção de contatos via WhatsApp na mesma plataforma — atendimento e relacionamento no mesmo dado
- **Busca semântica com pgvector**: histórico e conhecimento indexados por embeddings para apoiar a triagem

## Arquitetura e decisões técnicas

- **FastAPI assíncrono** com SQLAlchemy async e Alembic; qualidade travada com pytest, Ruff e mypy
- **Angular 20 standalone com Signals e SCSS puro**, TypeScript strict — reatividade fina no painel de conversas em tempo real
- **Camada de canais isolada**: WhatsApp (Evolution API no MVP, com migração planejada para a Meta Cloud API oficial), Teams app e e-mail plugam no mesmo domínio de tickets — adicionar canal não reescreve o negócio
- **PostgreSQL 16 + pgvector** para dados operacionais e embeddings no mesmo banco (menos infra, transações únicas); **Redis** para estado de conversa e cache
- **Análises de qualidade por amostragem**: em vez de processar 100% das conversas com LLM (custo proibitivo), amostragem estatística gera o termômetro de satisfação e os pareceres por setor com custo controlado
- **Dois ambientes**: produção e homologação com scripts de deploy separados (`deploy.ps1`, `deploy-homolog.ps1`, `vps-setup*.sh`) — pipeline reproduzível de build local → tar → VPS
- **Segurança**: SQL Server externo integrado com usuário/role restrita; segredos fora do versionamento

## Desafios e soluções

- **Unificar canais heterogêneos** (WhatsApp, Teams, e-mail, web) num único fluxo de tickets: abstração de canal no domínio, com identidade do usuário resolvida entre canais
- **IA que não pode travar a operação**: triagem degrada graciosamente para regras locais quando o LLM está indisponível
- **Medir qualidade sem custo explosivo de LLM**: termômetro por amostragem de conversas com parecer por setor
- **Datas, fusos e ordenação de mensagens em conversas assíncronas**: tratados como planos específicos de correção com testes
- **Evolução visual**: repaginação de UI planejada e executada com design system próprio

## Resultados e impacto

- Chamados de TI passam a nascer estruturados de qualquer canal (WhatsApp, Teams, e-mail, web), com fila e histórico unificados [volume A CONFIRMAR]
- Gestão com visão de qualidade: termômetro de satisfação, pareceres por setor e relatórios automáticos — antes não existia medição nenhuma
- CRM integrado transforma o mesmo canal de suporte em canal de campanhas e captação de contatos
- Operação com ambiente de homologação, migrações versionadas e typing/lint estritos — manutenível por terceiros

## Destaques para entrevista (STAR resumido)

- **S/T:** TI corporativa sem canal estruturado de chamados nem medição de qualidade de atendimento. **A:** construí sozinho a central omnichannel — triagem com Gemini e fallback por regras, painel Angular 20 de gestão completa, termômetro de satisfação por amostragem de conversas com parecer por setor, relatórios automatizados e módulo de CRM para campanhas via WhatsApp — sobre uma camada de canais isolada (WhatsApp, Teams, e-mail, web). **R:** atendimento estruturado e medido em produção nos canais que os usuários já usavam, com custo de IA controlado por amostragem e dois ambientes de deploy.
