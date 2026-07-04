---
title: AOG Dux Truck — Operação logística emergencial
client: Dux Logistics
category: freela
status: Produção
stack: [Java 21, Spring Boot 3, Angular 20, Entra ID]
order: 2
gallery: dux-logistics
---
# Case — AOG Dux Truck (Sistema de Operação Logística Emergencial)

**Tipo:** Freelance (cliente: Dux Logistics)
**Papel:** Desenvolvedor Full Stack (autoria completa: backend, frontend, autenticação corporativa, deploy)
**Status:** Em produção
**Stack:** Java 21, Spring Boot 3, Clean Architecture, Angular 20+ (standalone + Signals), PostgreSQL, Microsoft Entra ID (OAuth2/OIDC), JWT, Docker Compose, Nginx (SSE)

## Contexto e problema

Operações AOG (Aircraft On Ground — transporte emergencial de peças críticas) exigem fluxo operacional rígido, rastreável e com prazos agressivos. O cliente operava o fluxo definido em BPMN (`AOG - PADRÃO.bpmn`) de forma manual/planilhada, sem controle de transições de status, sem histórico auditável e sem portal para os clientes finais acompanharem suas demandas.

## Solução

Sistema operacional web que implementa o fluxo AOG completo como máquina de estados auditável, com dois públicos:

- **Operação interna**: login corporativo via Microsoft Entra ID, escopos de acesso por operador, telas por etapa do fluxo, gestão de usuários e clientes.
- **Portal externo de clientes**: login próprio (JWT independente) onde cada cliente enxerga somente as próprias demandas e seus status no fluxo.

Cada demanda tem sua **tela de acompanhamento própria**, compartilhada entre operação e cliente:

- **Chat de conversação dentro da demanda**: problemas específicos daquela demanda são resolvidos ali mesmo, com contexto — sem e-mail paralelo
- **Troca de comentários** entre operador e cliente vinculada à demanda
- **Timeline de eventos rastreável**: toda transição de status, comentário e interação fica registrada em ordem cronológica, visível para os dois lados

Funcionalidades-chave adicionais: onboarding automático de usuários Entra como "pendentes" até ativação por admin, bootstrap de primeiro admin por variável de ambiente, sincronização de foto via Microsoft Graph, atualizações em tempo real (SSE), gestão de escopos por tela.

## Arquitetura e decisões técnicas

- **Clean Architecture no backend**: domínio 100% livre de Spring/JPA; toda transição de status passa por um `StatusTransicaoService` central e gera `HistoricoStatus` — o fluxo BPMN vira invariante de domínio, impossível de burlar por atalho de CRUD.
- **Dupla autenticação isolada**: Entra ID (OIDC) para operadores e emissor JWT próprio para clientes externos, com TTL e issuer configuráveis — superfícies de ataque separadas.
- **Angular 20 com Signals e standalone components**: reatividade fina sem NgModules, com proxy para o backend em dev.
- **Server-Sent Events atrás de Nginx** para atualização em tempo real das filas operacionais.
- **Planos executados de otimização**: cache e performance (`PLANO_OTIMIZACAO_CACHE_PERFORMANCE`), refresh token, otimizações de Docker/JVM para runtime enxuto.
- Docker Compose para stack completa local (front, API, Postgres) e deploy scriptado (PowerShell).

## Desafios e soluções

- **Fluxo de negócio complexo e não-linear**: modelado como máquina de estados no domínio, com transições válidas explícitas — bugs de "status impossível" eliminados por construção.
- **Convivência de dois modelos de identidade** (corporativa e externa) sem vazamento de dados entre eles: separação por perfil, escopo e query — cliente externo nunca acessa dados de outro cliente.
- **Time-to-market de freelance**: entrega incremental guiada por backlog e planos de implementação versionados no repositório.

## Resultados e impacto

- Fluxo AOG saiu de controle manual para sistema auditável com histórico completo de cada demanda
- Cobranças por e-mail/telefone reduzidas: cliente acompanha cada demanda em tela própria e resolve dúvidas pelo chat da demanda, com comentários e timeline de eventos rastreável para os dois lados
- Comunicação centralizada no contexto certo: a conversa fica anexada à demanda, não espalhada em threads de e-mail
- Governança de acesso: nenhum usuário entra com permissões sem ativação explícita de admin

## Destaques para entrevista (STAR resumido)

- **S/T:** cliente de logística emergencial precisava digitalizar um fluxo BPMN crítico com auditoria e portal de clientes. **A:** construí sozinho o sistema em Java 21/Spring Boot 3 com Clean Architecture (domínio puro, máquina de estados central) e Angular 20 com Signals, integrando Microsoft Entra ID para a operação e JWT próprio para o portal externo — com tela de acompanhamento por demanda incluindo chat, comentários e timeline de eventos compartilhada entre operador e cliente. **R:** operação rastreável de ponta a ponta em produção, comunicação centralizada no contexto de cada demanda (menos cobranças por e-mail/telefone) e histórico auditável de toda transição.
