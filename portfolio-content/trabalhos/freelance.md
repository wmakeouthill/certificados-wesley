# Experiência Profissional - Freelancer Full Cycle (Produtos Próprios e Clientes Diretos)

## Sobre a Atuação

Desde 2025, atuo em paralelo como **freelancer full cycle**: proposta comercial → discovery → arquitetura → código → deploy → operação e suporte, como **único desenvolvedor**. Não são projetos de estudo — são sistemas **em produção**, operando o dia a dia de clientes reais, com contrato, prazo e suporte.

*Período: 2025 - Atual | Remoto*

## Sistemas em Produção

### AOG Dux Truck — Operação Logística Emergencial (em produção)

- Sistema para operação AOG (aviation on ground) — logística emergencial de peças
- **Java 21 + Spring Boot 3 em Clean Architecture**, **Angular 20**, autenticação **Microsoft Entra ID**
- Cada demanda tem **tela de acompanhamento própria com chat**, comentários operador/cliente e **timeline de eventos rastreável** — reduzindo cobranças por e-mail/telefone

### Automação Fiscal de NF-e (em produção)

- Captura de notas fiscais por e-mail via **Microsoft Graph** com **extração em camadas**: XML determinístico → PDF → OCR/IA apenas como fallback
- **FastAPI + React**; elimina digitação manual de notas no fluxo fiscal do cliente

### Sol — Central Omnichannel de Atendimento TI com IA (em produção)

- Atendimento por **WhatsApp, Teams, plataforma web e e-mail** em uma central única
- **Termômetro de satisfação** por amostragem de conversas com IA, gerando pareceres por setor e insights
- Painel completo de gestão de tickets, relatórios automatizados e **módulo de CRM integrado** (campanhas + captação de contatos por WhatsApp)
- **FastAPI + Angular 20 + pgvector + Gemini + Evolution/Meta WhatsApp Cloud API**

### Dashboard CX Qualtrics (em produção)

- Dashboard de experiência do cliente por jornada — **FastAPI + Angular + Gemini**
- **MCP server em TypeScript** para a API do Qualtrics
- Build desktop portátil Windows (Python + SQLite embarcados) com **auto-update via GitHub Releases**

### Mercearia R&V — Varejo Offline-First (em produção)

- Sistema desktop de estoque/vendas/PDV: **Electron orquestrando Spring Boot + PostgreSQL embarcados** num único instalador NSIS
- PDV, caixa, fidelidade, relatórios em PDF; **uso diário na operação do cliente com custo recorrente zero**

### Experimenta AI — Soneca (POS completo; delivery em homologação)

- Gestão de lanchonete com **impressão de cupons ESC/POS multiplataforma** (Windows Spooler, USB direto, CUPS)
- Ecossistema de **delivery próprio**: PWAs de cliente e motoboy, **rastreamento em tempo real** (GPS → cache TTL → Server-Sent Events), Google Maps Platform e OAuth Google
- **Java + Spring Boot multi-module (Clean Architecture) + Angular 17 + MySQL**

## Em Homologação / Entregas Pontuais

### Plataforma de Workflow Logístico (completa, em homologação)

- Substitui BPM corporativo estilo TOTVS Fluig: solicitações por tipo, filas por grupo, aprovações multi-etapa, documentos, SLAs e dashboard
- **Java + Spring + Angular + PostgreSQL**, deploy em VPS Oracle Cloud

### Renovação de Frontend — Integrador EDI Logístico

- Refatoração visual completa do frontend em **Next.js 16 + React 19 + Tailwind 4**

### Gerador de Crachás em Lote (entregue)

- Ferramenta Python empacotada em executável (PyInstaller) para Supermercados Rio Sul, com calibração por preview no navegador

## O Que Esta Experiência Comprova

- **Full cycle de verdade**: da proposta comercial (incluindo PPTX de venda) à operação em produção
- **Poliglota**: Java/Spring Clean Architecture, Python/FastAPI, Node, e os três grandes frontends (Angular, React, Vue)
- **Integrações corporativas**: Microsoft Entra ID, Microsoft Graph, Evolution API / Meta WhatsApp Cloud API, Teams, Qualtrics
- **Engenharia de custo**: VPS Oracle Cloud Always Free, apps desktop com banco embarcado — infraestrutura certa para o porte de cada cliente
- **Produtos que ficam no ar**: clientes operando diariamente nos sistemas, com suporte e evolução contínua
