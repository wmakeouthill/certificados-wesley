# Case — JGV (Previsão de Demanda e Recomendação de Estoque para Rede de Autopeças)

**Tipo:** AutoU (cliente: JGV — rede de autopeças multi-filial)
**Papel:** Desenvolvedor Full Stack / Eng. de dados aplicado — correção e evolução do pipeline preditivo e da API
**Status:** Em produção (execução diária automatizada)
**Stack:** Python, Prophet (séries temporais), Flask (API), PostgreSQL, ERP Sankhya (Oracle SQL via API), Bubble (frontend), feature flags, Docker, Google Cloud, PowerShell/CI de deploy

> Nota de confidencialidade: projeto de cliente da AutoU — validar o que pode ser público antes de expor nome/detalhes.

## Contexto e problema

Rede de autopeças com múltiplas filiais comprava e transferia estoque com base em intuição do comprador sobre o ERP Sankhya. Resultado: excesso de itens parados em uma filial e ruptura em outra, capital imobilizado e vendas perdidas — agravado pela complexidade de peças com **substitutos e similares** (comprar o item "original" quando o substituto já cobre a demanda).

## Solução

Pipeline batch diário de ponta a ponta + API de gestão de recomendações:

- **JGV_Prediction**: sincroniza produtos, estoque, movimentação, custos, filiais e substitutos do Sankhya; calcula os 7 atributos de classificação do negócio; roda **Prophet por produto/filial** para prever demanda; gera recomendações de **compra**, **transferência entre filiais** (atrás de feature flag) e resolução de **substitutos**; executa automaticamente em horário diário configurável.
- **JGV_API (Flask)**: expõe as recomendações para o frontend Bubble, com fluxos de criar/aceitar recomendação integrados de volta ao Sankhya (geração de pedidos), documentados por contrato para o API Connector do Bubble.

## Arquitetura e decisões técnicas

- **Lógica de compra defensiva**: `QtdTotal_f = max(demanda_prevista − estoque − pedidos_pendentes, 0)` — pedidos abertos "para chegar" são descontados fora do `fit()` do Prophet (não contaminam o modelo), e recomendações já aceitas no histórico são abatidas antes de gravar, evitando compra duplicada
- **Resolução de substitutos no ponto certo**: agregação de demanda entre item original e substitutos resolvida na etapa de recomendação (`substitutos_resolver`), com view SQL dedicada no Sankhya
- **Ponderação por cobertura de dados**: previsão ajustada pelos dias realmente cobertos no histórico (`total_days`), evitando superestimar produtos com histórico parcial
- **Feature flags** para features novas (transferência entre filiais) — rollout controlado em produção sem branch de deploy
- **Testes de cenário contra o ambiente cloud** (`test_cenarios_recomendacao_cloud.py` etc.) e comparação de schema dev/prod scriptada
- Integração Sankhya via queries batch documentadas (`BATCH_QUERY_SANKHYA.md`), com mapeamento completo do banco do ERP versionado

## Desafios e soluções

- **Bug crítico de transferências/estoque herdado**: investigado e corrigido com resumo executivo formal para o cliente (RESUMO_EXECUTIVO com PDF) — diagnóstico de queries, correção de schema e validação em produção
- **ERP como fonte de dados hostil**: schema Sankhya mapeado na unha (codtipoper, status de nota, pendências) e regras fiscais/comerciais convertidas em filtros SQL explícitos e documentados
- **Modelo que o negócio confia**: cada etapa do cálculo é reproduzível e documentada — o comprador consegue auditar por que o sistema recomendou X unidades

## Resultados e impacto

- Recomendações diárias automáticas de compra e transferência por filial, considerando substitutos [redução de ruptura/estoque parado A CONFIRMAR]
- Correção do fluxo de transferências eliminou pendências fantasma no ERP
- Comprador passou de planilha/intuição para fila de recomendações aceitáveis em um clique no front

## Destaques para entrevista (STAR resumido)

- **S/T:** rede de autopeças multi-filial com compra por intuição, itens substitutos ignorados e bug de transferências corrompendo pendências no ERP. **A:** evoluí o pipeline Prophet (ponderação por cobertura, desconto de pedidos pendentes fora do fit, resolução de substitutos), corrigi o fluxo de transferência com diagnóstico formal, e mantive a API Flask que serve as recomendações ao front Bubble integrado ao Sankhya. **R:** pipeline diário em produção gerando recomendações auditáveis de compra e transferência, com rollout por feature flag e confiança do cliente no número.
