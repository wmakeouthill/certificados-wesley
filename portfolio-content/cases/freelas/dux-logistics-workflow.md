---
title: Dux Workflow — Plataforma de workflow logístico e documental
client: Dux Logistics
category: freela
status: Homologação
stack: [Java, Spring Boot, Angular, PostgreSQL]
order: 3
gallery: dux-logistics
---
# Case — Dux Logistics MVP (Plataforma de Workflow Logístico e Documental)

**Tipo:** Freelance (cliente: Dux Logistics)
**Papel:** Desenvolvedor Full Stack e responsável por produto/arquitetura
**Status:** Completo, em homologação com o cliente
**Stack:** Java, Spring Boot, Angular, PostgreSQL, Docker Compose, deploy em VPS Oracle Cloud

## Contexto e problema

O cliente operava processos logísticos e documentais em uma plataforma BPM corporativa cara e genérica (estilo TOTVS Fluig): abertura de solicitações, filas de tratativa por grupo, aprovações em etapas, anexos e SLAs. O objetivo era substituir isso por um produto próprio, enxuto e especializado no domínio logístico — sem pagar o custo (financeiro e de complexidade) de um BPM genérico.

## Solução

Produto web corporativo de workflow operacional para logística, projetado a partir de engenharia reversa das telas do sistema legado:

- Abertura de solicitações com formulários por tipo (schema controlado, não editor livre)
- Caixa de tarefas individual e por grupo, com tratativa, encaminhamento, devolução e reatribuição
- Aprovação em uma ou múltiplas etapas, workflow parametrizável por tipo de solicitação
- Gestão de documentos, anexos e checklist documental
- Timeline completa da solicitação (auditoria e trilha de alterações)
- Dashboard operacional com indicadores de atraso, prazo e volume; filtros, exportação e operações em lote
- Cadastros organizacionais (empresa, unidade, departamento, grupos) e operacionais (clientes, tipos de documento, prioridades)
- Notificações in-app e por e-mail

## Arquitetura e decisões técnicas

- **Decisão de produto explícita**: workflow parametrizável por etapas, regras, grupos e SLA — sem BPMN aberto nem low-code genérico. Escopo controlado = MVP viável para um dev solo.
- **Formulários dinâmicos com schema controlado**: campos configuráveis por tipo de solicitação com componentes padronizados, evitando a armadilha do "form builder" ilimitado.
- **Java + Spring Boot no backend e Angular no frontend**, seguindo guia de regras de desenvolvimento próprio versionado no repo (padrões de código, testes e contrato de API).
- **PostgreSQL** com modelagem para trilha de auditoria por solicitação.
- **Docker Compose** para dev e produção, com compose específico para deploy em VPS Oracle Cloud (custo de infra ~zero no free tier).
- Plano de otimizações de JVM/queries versionado e aplicado (`PLANO-OTIMIZACOES-JAVA.md`).

## Desafios e soluções

- **Levantar requisitos sem acesso ao sistema original**: requisitos inferidos de prints reais da operação, validados com o cliente e documentados em plano de produto detalhado antes de codar.
- **Equilibrar "produto completo" vs. "clone de Fluig"**: trade-offs documentados; tudo que era genérico demais ficou fora do MVP em favor de profundidade no domínio logístico.
- **Operar como freelancer full cycle**: da proposta comercial (PPTX de venda) ao deploy na VPS, passando por produto, UX, arquitetura e código.

## Resultados e impacto

- Substituição de licença BPM corporativa por produto próprio especializado — desenvolvimento concluído, em homologação aguardando a desativação do sistema legado para entrar no ar e integrar a operação
- Processos com rastreabilidade completa e SLAs visíveis para gestão
- Base parametrizável que permite ao cliente criar novos tipos de solicitação sem desenvolvimento

## Destaques para entrevista (STAR resumido)

- **S/T:** cliente queria sair de um BPM genérico caro para um produto próprio de workflow logístico. **A:** fiz o discovery por engenharia reversa de prints, escrevi o plano de produto com trade-offs explícitos (parametrizável sim, low-code não), e construí o MVP full stack em Java/Spring + Angular com deploy em VPS Oracle. **R:** MVP funcional cobrindo abertura, filas, aprovações, documentos e dashboard, com custo de infraestrutura próximo de zero.
