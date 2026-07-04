# Case — LIS (Libbs: Assistente de Triagem de Tickets SAC com IA)

**Tipo:** AutoU (cliente: Libbs — indústria farmacêutica)
**Papel:** Desenvolvedor Full Stack — projeto solo (demo/MVP feito sozinho)
**Status:** No ar (em produção)
**Stack:** Python, FastAPI, Poetry, React 19, TypeScript, Vite, TanStack Query, Zustand, Recharts, PostgreSQL, Gemini (`google-genai`) com fallback por regras, Docker Compose, deploy Oracle Cloud VPS

> Nota de confidencialidade: projeto de cliente da AutoU — validar o que pode ser público antes de expor nome/detalhes.

## Contexto e problema

O SAC da farmacêutica recebia solicitações heterogêneas (dúvidas de medicamento, farmacovigilância, reclamações) que precisavam ser triadas manualmente antes de chegar ao atendente certo — com risco regulatório quando um relato de evento adverso demora a ser classificado.

## Solução

Portal LIS com duas superfícies na mesma aplicação:

- **Chat público** (domínio próprio, ex. `chat.dominio.com`): usuário final conversa com a assistente LIS, que triage a solicitação com IA e abre o ticket classificado; casos que exigem humano fazem **transbordo** para atendimento
- **Portal interno** (login protegido): fila de "Conversas e atendimentos", visão de tickets com timeline, dashboards (Recharts)

## Arquitetura e decisões técnicas

- **Degradação graciosa da IA**: sem `GOOGLE_GENAI_API_KEY`, a LIS triage por regras locais — o MVP nunca fica fora do ar por indisponibilidade/custo de LLM
- **Uma aplicação, dois domínios**: o mesmo frontend serve portal interno e chat público, roteando pela env `VITE_CHAT_HOSTS` — menos infra, mesma API e mesmo banco, transbordo natural entre canais
- **React 19 + TanStack Query + Zustand**: server state e client state separados por ferramenta certa; testes com Vitest + Testing Library
- **Deploy sem registry**: script PowerShell builda imagens localmente, envia `images.tar` + compose + `.env` via SSH e sobe na VPS — pipeline simples e reproduzível para MVP
- Arquitetura documentada em diagramas HTML e pareceres técnicos versionados no repo (material de apresentação ao cliente)

## Desafios e soluções

- **Setor regulado (farma)**: triagem com trilha clara de conversa→ticket e transbordo humano para casos sensíveis
- **Fidelidade ao design**: telas implementadas a partir de especificações CSS extraídas do Figma (chat e visão de conversas/timeline)
- **Custo do MVP**: Oracle Cloud Always Free + DuckDNS, com caminho pavimentado para infra definitiva

## Resultados e impacto

- Triagem automática de tickets SAC com classificação assistida por IA e fallback determinístico [volume/precisão A CONFIRMAR]
- Canal público de atendimento e portal interno entregues como um único deploy
- MVP demonstrável ao cliente com custo de infraestrutura zero

## Destaques para entrevista (STAR resumido)

- **S/T:** SAC de farmacêutica com triagem manual e risco regulatório em classificação lenta. **A:** construí o portal full stack — chat público com triagem por Gemini e fallback por regras, transbordo para atendimento humano, portal interno com timeline de tickets — servindo dois domínios com uma única aplicação e deploy scriptado em VPS. **R:** MVP funcional em produção de demonstração, resiliente à indisponibilidade de LLM e pronto para validação de negócio.
