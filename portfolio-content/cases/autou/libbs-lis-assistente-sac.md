---
title: LIS — Triagem de tickets SAC com IA (demo)
client: Libbs (demo — edital em andamento)
category: autou
status: Demo no ar
stack: [FastAPI, React 19, Gemini]
order: 4
---

# Case — LIS (demo para edital da Libbs: Assistente de Triagem de Tickets SAC com IA)

**Tipo:** AutoU (demo para edital da Libbs — indústria farmacêutica; edital ainda em andamento, a Libbs **não é cliente** da AutoU)
**Papel:** Desenvolvedor Full Stack — projeto solo (demo/MVP feito sozinho)
**Status:** Demo no ar (aguardando resultado do edital)
**Stack:** Python, FastAPI, Poetry, React 19, TypeScript, Vite, TanStack Query, Zustand, Recharts, PostgreSQL, Gemini (`google-genai`) com fallback por regras, Docker Compose, deploy Oracle Cloud VPS

> Nota de confidencialidade: demo construída pela AutoU para concorrer a edital — validar o que pode ser público antes de expor nome/detalhes. Não apresentar como projeto contratado ou cliente da AutoU enquanto o edital não for decidido.

## Contexto e problema

O SAC da farmacêutica recebe solicitações heterogêneas (dúvidas de medicamento, farmacovigilância, reclamações) que precisam ser triadas manualmente antes de chegar ao atendente certo — com risco regulatório quando um relato de evento adverso demora a ser classificado. A AutoU decidiu concorrer ao edital da Libbs para esse problema, e a demo LIS foi construída como proposta técnica funcional — o edital segue em andamento.

## Solução

Portal LIS com duas superfícies na mesma aplicação:

- **Chat público** (domínio próprio, ex. `chat.dominio.com`): usuário final conversa com a assistente LIS, que triage a solicitação com IA e abre o ticket classificado; casos que exigem humano fazem **transbordo** para atendimento
- **Portal interno** (login protegido): fila de "Conversas e atendimentos", visão de tickets com timeline, dashboards (Recharts)

## Arquitetura e decisões técnicas

- **Degradação graciosa da IA**: sem `GOOGLE_GENAI_API_KEY`, a LIS triage por regras locais — o MVP nunca fica fora do ar por indisponibilidade/custo de LLM
- **Uma aplicação, dois domínios**: o mesmo frontend serve portal interno e chat público, roteando pela env `VITE_CHAT_HOSTS` — menos infra, mesma API e mesmo banco, transbordo natural entre canais
- **React 19 + TanStack Query + Zustand**: server state e client state separados por ferramenta certa; testes com Vitest + Testing Library
- **Deploy sem registry**: script PowerShell builda imagens localmente, envia `images.tar` + compose + `.env` via SSH e sobe na VPS — pipeline simples e reproduzível para MVP
- Arquitetura documentada em diagramas HTML e pareceres técnicos versionados no repo (material de apresentação para o edital)

## Desafios e soluções

- **Setor regulado (farma)**: triagem com trilha clara de conversa→ticket e transbordo humano para casos sensíveis
- **Fidelidade ao design**: telas implementadas a partir de especificações CSS extraídas do Figma (chat e visão de conversas/timeline)
- **Custo do MVP**: Oracle Cloud Always Free + DuckDNS, com caminho pavimentado para infra definitiva

## Resultados e impacto

- Triagem automática de tickets SAC com classificação assistida por IA e fallback determinístico
- Canal público de atendimento e portal interno entregues como um único deploy
- Demo funcional apresentada no edital com custo de infraestrutura zero — resultado do edital ainda em andamento

## Indicadores projetados no discovery (projeções do business case — não medições)

Base de referência levantada com os stakeholders: **~50 chamados/dia (~18–20 mil/ano)**, sendo **80% simples**; tempo atual de **7 min/chamado** (5 de formulação de resposta + 2 de tabulação), com prazo de resposta de até 24h. Projeções apresentadas:

- **Resolução automática:** ~72% dos chamados sem intervenção humana (~36/dia) — a IA resolve ~90% dos simples; os complexos seguem para humano com contexto pré-coletado
- **Tempo médio de atendimento:** de 7 min para ~2 min (**redução de ~71%**) — simples respondidos na hora, complexos em ~4 min porque o contexto já chega estruturado
- **Escalonamento correto:** ~90% dos casos sensíveis direcionados certo ao humano, tendendo a 95%+ com o ciclo de feedback
- **Carga operacional:** ~4,2h/dia economizadas (~1.050h/ano), **economia estimada de ~R$ 26 mil/ano** — sem contar qualidade e retrabalho
- **Acurácia da classificação de intenção:** ~82% no go-live → ~90% após o 1º ciclo de feedback → ~95% na operação madura (diferencial: governança contínua da base de conhecimento e feedback dos atendentes)
- **NPS:** ganho estimado de +25 a +30 pontos vs. SAC tradicional

> Automação com critério, não SAC 100% automatizado: simples (currículo, desconto, dúvida institucional) resolvidos na hora com respostas aprovadas; sensíveis (evento adverso, desvio de qualidade, reclamação técnica) identificados, coletados e transbordados com segurança — respeitando farmacovigilância, LGPD e CDC.

## Destaques para entrevista (STAR resumido)

- **S/T:** edital de farmacêutica para resolver SAC com triagem manual e risco regulatório em classificação lenta — a AutoU precisava de uma proposta técnica funcional, não só slides. **A:** construí sozinho a demo full stack — chat público com triagem por Gemini e fallback por regras, transbordo para atendimento humano, portal interno com timeline de tickets — servindo dois domínios com uma única aplicação e deploy scriptado em VPS. **R:** demo funcional no ar sustentando a candidatura da AutoU no edital (em andamento), resiliente à indisponibilidade de LLM e com custo de infra zero.
