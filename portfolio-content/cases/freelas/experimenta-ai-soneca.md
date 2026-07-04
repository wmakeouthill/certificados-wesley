# Case — Experimenta AI (Soneca): Gestão de Lanchonete + Ecossistema de Delivery

**Tipo:** Produto próprio para cliente real (food service — lanchonete)
**Papel:** Desenvolvedor Full Stack — autoria completa (POS desktop + plataforma de delivery)
**Status:** POS de balcão completo; ecossistema delivery em homologação final para entrar no ar
**Stack:** Java 17 + Spring Boot 3.2 (Maven multi-module, Clean Architecture), Angular 17+ (Standalone Components), Electron (POS + print server), MySQL 8 + Liquibase, impressão térmica ESC/POS, Google Maps Platform (Directions/Geocoding/Places), Google OAuth, SSE, PWA, Docker Compose

## Contexto e problema

Uma lanchonete precisava sair do papel/WhatsApp para uma operação organizada: pedidos de balcão com cupom impresso, cardápio gerenciável, e depois expandir para delivery próprio — sem pagar as taxas de marketplace (iFood e afins) nem perder a relação direta com o cliente.

## Solução

Ecossistema em duas fases sobre a mesma base Clean Architecture:

**Fase 1 — POS de balcão (completo):**
- Gestão de pedidos, cardápio, clientes e autenticação em app desktop Electron
- **Impressão de cupons ESC/POS** via print server no Electron: suporte a Windows Spooler, USB direto, CUPS (Linux) e impressoras de rede — testado com EPSON TM-T20 e DARUMA DR-800

**Fase 2 — Delivery (em homologação para ir ao ar):**
- **App do cliente (PWA)**: cardápio, pedido, endereços com autocomplete do Google Places, favoritos/re-pedido, timeline de status e **rastreamento do motoboy em tempo real no mapa**
- **App do motoboy (PWA)**: auto-cadastro por link público com aprovação do admin, login Google OAuth, Kanban das próprias entregas, envio de posição GPS
- **Painel do gestor**: gestão de pedidos delivery e de motoboys

## Arquitetura e decisões técnicas

- **Maven multi-module com Clean Architecture**: módulos por domínio (pedidos, cardápio, clientes, autenticação, impressão) — o delivery nasceu como extensão de módulos, não como fork
- **Rastreamento de alta frequência sem sobrecarregar o banco**: posições dos motoboys em cache `ConcurrentHashMap` com TTL, escrita desacoplada por eventos assíncronos (a conexão HTTP libera imediato) e **broadcast via Server-Sent Events** — o cliente vê o motoboy se mover sem polling
- **Autenticação híbrida**: JWT interno para admin/funcionários; OAuth Google trocado por JWT de sessão com claims distintas para cliente e motoboy
- **Privacidade de localização**: cliente só acessa a posição do motoboy designado, e apenas enquanto o pedido está "saiu para entrega"
- **PWA mobile-first**: cliente e motoboy instalam como app sem loja de aplicativos
- **MySQL + Liquibase, Docker Compose** para dev e deploy reproduzíveis

## Desafios e soluções

- **Hardware de impressão heterogêneo**: camada de conversão ESC/POS própria no print server Electron abstraindo spooler/USB/CUPS por plataforma
- **Tempo real barato**: SSE + cache em memória em vez de WebSocket full-duplex e escrita em banco por coordenada — simples, e suficiente para o caso
- **Operação por não-técnicos**: fluxos de balcão desenhados para velocidade de atendimento (pedido → cupom impresso em segundos)

## Resultados e impacto

- POS de balcão completo operando o fluxo pedido→cupom da lanchonete [tempo de uso A CONFIRMAR]
- Plataforma de delivery própria em homologação final — canal direto sem taxa de marketplace
- Base modular comprovada: o delivery reusou domínio, autenticação e cardápio da fase 1

## Destaques para entrevista (STAR resumido)

- **S/T:** lanchonete operando no papel queria pedidos organizados com cupom impresso e, depois, delivery próprio sem taxas de marketplace. **A:** construí o ecossistema completo — POS desktop com print server ESC/POS multiplataforma, e a extensão de delivery com PWAs para cliente e motoboy, rastreamento em tempo real (GPS → cache TTL → SSE), OAuth Google híbrido e Clean Architecture multi-module que permitiu o delivery nascer como extensão. **R:** balcão informatizado de ponta a ponta e plataforma de delivery própria em homologação final para produção.
