# Case — Rocester (Catálogo Digital Inteligente de Peças Industriais)

**Tipo:** AutoU (cliente: Rocester — peças industriais)
**Papel:** Desenvolvedor Full Stack / IA — participação na fundação do projeto (arquitetura e base funcional inicial)
**Status:** No ar (em produção); evoluções em roadmap
**Stack:** Python, FastAPI, React + TypeScript, PostgreSQL (pgvector habilitado), Gemini Vision (extração de PDF), JWT com roles, Docker Compose, ReportLab (roadmap), full-text search (RAG)

> Nota de confidencialidade: projeto de cliente da AutoU — validar o que pode ser público antes de expor nome/detalhes.

## Contexto e problema

Os vendedores da Rocester consultavam catálogos de peças em PDFs escaneados de fornecedores: achar uma peça, conferir código OEM e montar orçamento era lento e sujeito a erro. Digitalizar os catálogos manualmente era inviável pelo volume.

## Solução

Plataforma que transforma PDFs de catálogo em base de dados pesquisável com IA:

- **Pipeline de ingestão de PDFs com Gemini Vision**: upload do catálogo → extração estruturada de peças (código, OEM, descrição, categoria, equipamento) com `temperature=0.1`, JSON mode e retries
- **Score de confiança por peça (0.0–1.0) com reasoning textual**: peças extraídas entram como pendentes; painel de revisão com **ações em massa** (aprovar/reprovar) para curadoria humana eficiente
- **Busca e filtros** por código, OEM, descrição, categoria e equipamento
- **Orçamentos**: carrinho, código automático (`ORC-AAMM-XXXX`), histórico
- **Assistente IA (chat)**: sugestão de peças por texto livre com RAG sobre o catálogo real

## Arquitetura e decisões técnicas

- **Inversão de dependência na camada de IA**: o domínio não conhece o provedor LLM — trocar Gemini por outro modelo não toca o negócio (documentado na arquitetura do README)
- **Ciclo de vida explícito da peça**: extraída → pendente de revisão → aprovada/reprovada — IA propõe, humano dispõe; o catálogo público só contém dados curados
- **Extração com controles anti-alucinação**: temperatura baixa, saída JSON estrita, retries e score de confiança com justificativa por item
- **JWT com roles** (`admin` / `seller`): vendedor consulta e orça; admin importa e cura
- **pgvector já habilitado** no banco para evolução de busca semântica por embeddings (roadmap documentado, incluindo processamento assíncrono da ingestão e export de orçamento em PDF)
- Proposta técnico-comercial e plano de projeto versionados junto ao código

## Desafios e soluções

- **PDFs heterogêneos de fornecedores** (tabelas, imagens, layouts variados): Vision multimodal + revisão humana em massa equilibram automação e precisão
- **Confiança do vendedor no dado**: score + reasoning por peça tornam o "quão certo a IA está" visível, não escondido

## Resultados e impacto

- Catálogos em PDF viram base pesquisável sem digitação manual [nº de peças/catálogos A CONFIRMAR]
- Orçamento montado no mesmo fluxo da busca — menos alternância de ferramenta para o vendedor
- Curadoria em massa reduz o custo humano de validar a extração da IA

## Destaques para entrevista (STAR resumido)

- **S/T:** vendedores dependiam de PDFs escaneados para achar peças e montar orçamentos. **A:** participei da fundação da plataforma — arquitetura com camada de IA desacoplada por inversão de dependência e base funcional do pipeline de extração via Gemini Vision (JSON mode, score de confiança com reasoning), painel de revisão com bulk actions, orçamentos e assistente RAG. **R:** fundação sólida transformando catálogo estático em dado estruturado curado, com caminho claro para busca vetorial (pgvector já provisionado).
