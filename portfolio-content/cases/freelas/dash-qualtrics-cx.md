---
title: Dashboard CX por jornada + MCP server Qualtrics
client: Cliente corporativo
category: freela
status: Produção
stack: [FastAPI, Angular, Gemini, Qualtrics]
order: 6
---
# Case — Dash Qualtrics (Dashboard de CX por Jornada + MCP Server)

**Tipo:** Freelance (cliente corporativo — área de Customer Experience)
**Papel:** Desenvolvedor Full Stack (autoria completa; inclui um MCP server em TypeScript)
**Status:** Em produção (VPS Oracle) + versão desktop portátil
**Stack:** Python, FastAPI, Angular, PostgreSQL/SQLite, Gemini (`google-genai`), JWT, Docker Compose, Nginx + Let's Encrypt, Oracle Cloud VPS, TypeScript (MCP server), Qualtrics API

## Contexto e problema

A área de CX do cliente coletava pesquisas no Qualtrics, mas a análise por jornada do cliente exigia exportações manuais e montagem de gráficos à mão. Os dashboards nativos não davam a visão consolidada por jornada nem um parecer qualitativo rápido sobre o que as respostas estavam dizendo.

## Solução

Duas frentes complementares:

1. **Dash Qualtrics** — dashboard web que sincroniza respostas via API do Qualtrics, consolida gráficos por jornada e inclui uma aba de **análise por IA (Gemini)** com "termômetro" e parecer sobre as perguntas. Login JWT e gestão básica de usuários.
2. **Qualtrics MCP Server (TypeScript)** — servidor MCP que expõe a API do Qualtrics como ferramentas para assistentes de IA, usado para diagnóstico de data models e construção assistida de dashboards CX (documentação de análises versionada no repo).

## Arquitetura e decisões técnicas

- **FastAPI + Angular + Postgres** em Docker Compose único (db, backend, frontend com Nginx fazendo proxy de `/api`)
- **Sincronização incremental** de respostas via API Qualtrics com token seguro no backend
- **Deploy automatizado em VPS Oracle** com um script: atualiza DNS dinâmico (DuckDNS), envia o projeto, publica em 80/443 e emite/renova certificado Let's Encrypt via Certbot
- **Versão desktop portátil para Windows** — decisão de produto notável: mesmo backend empacotado com Python embutido + SQLite, sem exigir Docker, Node ou permissão de admin; roda até de pendrive, com **auto-update via GitHub Releases** (`Atualizar.bat`). Um código, dois modos de distribuição (SaaS na VPS e pacote offline)
- **Hot reload em dev** com compose override, sem tocar no compose de produção

## Desafios e soluções

- **Cliente com restrições de TI** (sem Docker/admin nas máquinas locais): resolvido com o pacote desktop portátil SQLite — remoção total de fricção de instalação
- **Custo de infraestrutura**: VPS Oracle Always Free + DuckDNS + Certbot = HTTPS de produção com custo zero
- **Análise qualitativa em escala**: prompt engineering para o parecer da IA por jornada, com termômetro visual para leitura executiva rápida

## Resultados e impacto

- Visão por jornada disponível em tempo real, sem exportação manual do Qualtrics
- Parecer automático por IA encurtou o ciclo de leitura das pesquisas [tempo A CONFIRMAR]
- Distribuição dupla (web + desktop portátil) cobriu tanto a operação central quanto usuários com TI restrita

## Destaques para entrevista (STAR resumido)

- **S/T:** área de CX precisava de análise por jornada sobre dados do Qualtrics sem trabalho manual. **A:** construí dashboard FastAPI/Angular com sync via API, análise por Gemini, deploy automatizado com HTTPS em VPS Oracle e — para usuários sem Docker/admin — uma versão desktop portátil com Python embutido, SQLite e auto-update via GitHub Releases; complementei com um MCP server TypeScript para explorar a API do Qualtrics via IA. **R:** análise de CX contínua em produção com custo de infra zero e adoção sem fricção de TI.
