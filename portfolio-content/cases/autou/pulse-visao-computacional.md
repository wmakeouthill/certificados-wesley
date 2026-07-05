---
title: Pulse — Conformidade de postos com visão computacional
client: Rede São Roque
category: autou
status: Produção
stack: [YOLO, FastAPI, LangGraph, Gemini, AWS]
order: 2
---

# Case — Pulse (Conformidade de Postos de Combustível com Visão Computacional)

**Tipo:** AutoU (cliente: Rede São Roque — rede de postos de combustível)
**Papel:** Desenvolvedor Full Stack / IA — pipeline de visão computacional, backend, deploy e observabilidade; liderança técnica de frentes do projeto (em equipe), com contato direto com o cliente em pontos semanais e alinhamentos pontuais
**Status:** Em produção (edge agent 24/7 nos postos)
**Stack:** Python, YOLO (detecção), FastAPI, React, PostgreSQL, LangGraph + Gemini (pipeline agêntico), RAG, AWS (S3, Lambda, DynamoDB), Google Cloud (2 VMs), RTSP stream-worker, Prometheus + Grafana, Caddy, Docker Compose, Roboflow + Google Colab (retraining)

> Nota de confidencialidade: projeto de cliente da AutoU — validar o que pode ser público antes de expor nome/detalhes.

## Contexto e problema

Rede de postos precisava fiscalizar conformidade visual das unidades (manchas de óleo, lixo, cabos expostos, EPIs) — hoje dependente de visitas presenciais e fotos esporádicas. Sem detecção contínua, problemas ficavam dias sem tratativa e a gerência não tinha visão consolidada.

## Solução

Sistema de monitoramento contínuo com ciclo completo de melhoria do modelo:

- **Edge Agent (PC no posto)**: consome câmeras via RTSP, roda YOLO 24/7, valida detecções e faz upload dos eventos
- **Backend cloud**: armazena eventos e fotos (S3, retenção 1 ano; DynamoDB para eventos/feedback), API REST com fluxos de `resolve`, `false-positive` e dashboard
- **Pipeline agêntico (LangGraph + Gemini + RAG)**: análise das ocorrências, geração de insights e tratativas, integração com fluxo de e-mail/WhatsApp para notificação
- **Dashboard React**: gerência aprova/resolve ocorrências e marca falsos positivos
- **Loop de retraining**: feedback dos usuários vira dataset (script de coleta), re-treino em Colab com Roboflow, novo modelo volta ao edge — o sistema melhora com o uso

## Arquitetura e decisões técnicas

- **Edge + cloud híbrido**: inferência YOLO no posto (largura de banda e latência mínimas — sobe evento, não vídeo), consolidação e IA generativa na nuvem
- **Multi-cloud pragmático**: AWS para armazenamento/eventos (S3/Lambda/DynamoDB), GCP para aplicação (deploy em 2 VMs com papéis separados — app e stateful/observabilidade)
- **Stream-worker dedicado** para captura RTSP desacoplada do backend — decisão arquitetural de captura: consumo direto do DVR Intelbras já existente no posto via RTSP, com **porta externa segura configurada via NAT no DVR do cliente** — aproveitando o hardware de câmeras que o posto já tinha, sem custo de equipamento novo
- **Observabilidade de verdade (implementada por mim)**: Prometheus + Grafana em VM stateful própria — monitoramento de custos e orçamento computacional, uso e infraestrutura — com snapshots e plano de deploy versionado
- **Otimização do pipeline agêntico** documentada e executada (`PLANO_OTIMIZACAO_PIPELINE_AGENTICO.md`) — custo e latência de LLM controlados
- **Cache global** planejado/implementado para reduzir reprocessamento (`plano-cache-global.md`)
- Migração single-shot documentada, seeds de RAG versionadas, scripts de sync local→GCP/EC2

## Desafios e soluções

- **Falsos positivos corroendo confiança**: botão de false-positive no dashboard alimenta diretamente o dataset de re-treino — feedback do usuário virou ativo de ML
- **Infra 24/7 com custo controlado**: separação app/stateful em VMs distintas, retenção definida (fotos 1 ano) e edge fazendo o trabalho pesado de inferência
- **Operação real (posto de gasolina)**: setup reproduzível por scripts PowerShell/bash para instalar estações novas (`push-stations.ps1`)

## Resultados e impacto

- Detecção contínua 24/7 em produção substituindo fiscalização presencial esporádica — piloto no ar com **2 postos monitorados** e expansão prevista para os **~50 postos da rede**
- Ciclo de melhoria contínua do modelo com dados reais da operação
- Gerência com dashboard consolidado de ocorrências, tratativas e falsos positivos

## Destaques para entrevista (STAR resumido)

- **S/T:** rede de postos sem monitoramento contínuo de conformidade visual. **A:** participei da construção do sistema edge-to-cloud — captura via RTSP direto do DVR Intelbras do cliente (porta externa segura via NAT), YOLO rodando no posto, eventos em AWS, pipeline agêntico LangGraph+Gemini com RAG para análise e notificações, dashboard React, observabilidade Prometheus/Grafana com controle de custo/orçamento computacional e loop de retraining alimentado pelo feedback dos usuários. **R:** sistema em produção detectando ocorrências 24/7, com modelo que melhora continuamente e operação de deploy reproduzível em GCP.
