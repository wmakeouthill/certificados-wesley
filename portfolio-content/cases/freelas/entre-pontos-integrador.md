---
title: Entre Pontos — Renovação do frontend do integrador EDI logístico
client: Entre Pontos
category: freela
status: Produção
stack: [Next.js 16, React 19, Tailwind 4]
order: 1
---
# Case — Entre Pontos Integrador (Renovação Visual do Frontend de Plataforma EDI)

**Tipo:** Freelance (cliente: transportadora / operação Simpress-ESL)
**Papel:** Desenvolvedor Frontend — renovação visual e refatoração do frontend do integrador
**Status:** Entregue
**Stack:** Next.js 16, React 19, TypeScript, Tailwind CSS 4, Vitest, pnpm (backend existente: Fastify + Prisma + PostgreSQL)

## Contexto e problema

O integrador EDI da operação (pipeline PROCEDA/OCOREN/DOCCOB: ingestão por FTP/e-mail, transformação de layouts e entrega de outputs) já funcionava, mas a interface operacional não acompanhava: visual datado, hierarquia de informação confusa e leitura de falhas/status pouco eficiente para os operadores que monitoram o pipeline o dia inteiro.

## Solução

Renovação visual completa com refatoração do frontend em Next.js 16 + React 19 + Tailwind CSS 4, guiada por documentação de design própria criada para o projeto:

- **Linguagem de produto documentada** (glossário operacional: Outputs, Entregas, Configuration Clients, Pipeline Profiles) — a UI passou a falar a língua da operação, com termos proibidos/preferidos definidos por conceito
- **Princípios de design explícitos** (PRODUCT.md/DESIGN.md): sinal operacional acima de decoração, falhas/status/próximos passos imediatamente legíveis, densidade de informação como ferramenta de trabalho — anti-referência declarada a dashboards SaaS genéricos
- Refatoração dos fluxos principais: monitoramento do pipeline, detalhe/investigação de falhas e reprocessamento/reenvio no mesmo fluxo, com contexto suficiente para agir

## Decisões técnicas

- **Next.js 16 + React 19** com Tailwind CSS 4 e TypeScript; testes com Vitest
- Design system sóbrio e funcional definido antes do código (brand personality, anti-referências e princípios versionados no repo) — refatoração visual com critério, não "deixar bonito"
- Validação visual assistida por Playwright durante o redesign (screenshots comparativos)

## Resultados e impacto

- Interface operacional modernizada mantendo o backend e os fluxos existentes intactos
- Leitura de estado do pipeline e investigação de falhas mais rápidas para o operador [feedback A CONFIRMAR]
- Base de design documentada que mantém consistência em evoluções futuras da UI

## Destaques para entrevista (STAR resumido)

- **S/T:** integrador EDI funcional, mas com frontend datado que dificultava a leitura operacional. **A:** conduzi a renovação visual refatorando o frontend em Next.js 16/React 19/Tailwind 4, definindo antes glossário de produto e princípios de design versionados, priorizando legibilidade de falhas e densidade útil de informação. **R:** operação com interface moderna e leitura objetiva do pipeline, sem regressão funcional — e com fundação de design documentada para o futuro.
