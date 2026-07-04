---
title: Automação fiscal de NF-e por e-mail com IA
client: Dux Logistics
category: freela
status: Produção
stack: [FastAPI, React, MS Graph, PostgreSQL]
order: 4
---
# Case — Dux NF (Automação de Notas Fiscais por E-mail com IA)

**Tipo:** Freelance (cliente: Dux Logistics — operação de coleta em concessionárias Fiat/Citroën, contexto Stellantis)
**Papel:** Desenvolvedor Full Stack (autoria completa)
**Status:** Em produção
**Stack:** Python, FastAPI, React + TypeScript + Vite, PostgreSQL, Microsoft Graph API (Outlook/M365), IA para extração (fallback OCR/LLM), Docker Compose, deploy Hostinger/Oracle Cloud

## Contexto e problema

A operação logística recebia dezenas de notas fiscais (XML e PDF) por e-mail e alimentava manualmente uma planilha operacional de controle de demanda usada com a Stellantis. Processo lento, sujeito a erro de digitação e sem auditoria — e a planilha tinha fórmulas e validações que não podiam ser quebradas.

## Solução

Pipeline de ponta a ponta que monitora a caixa Outlook/Microsoft 365 via Microsoft Graph, captura anexos de NF, extrai os dados e preenche a planilha operacional automaticamente — com painel administrativo para operação, fila de falhas e configuração.

Estratégia de extração em camadas (custo e confiabilidade):

1. **XML de NF-e** — parsing determinístico (fonte primária, custo zero de IA)
2. **PDF texto** — parsing determinístico quando possível
3. **OCR/IA** — somente quando XML ausente/inválido e PDF não parseável

Dashboard operacional com recortes de qualidade e custo: total recebido, sucesso por XML, sucesso sem IA, processadas com IA/OCR, falhas com motivo e ação de reprocessamento manual.

## Arquitetura e decisões técnicas

- **FastAPI + worker assíncrono leve** (agendamento simples, sem fila distribuída no MVP — decisão consciente de simplicidade operacional)
- **Microsoft Graph** para leitura da caixa monitorada, com pasta e parâmetros configuráveis pelo próprio front
- **Preenchimento de planilha não-destrutivo**: insere linhas sem quebrar fórmulas, validações e colunas fora do alvo — incluindo backfill auditado com backup prévio (`backup_pre_backfill.sql`)
- **Anexos arquivados em diretório controlado** para auditoria e reprocessamento
- **PostgreSQL** para trilha completa de processamento (o que entrou, como foi extraído, o que falhou e por quê)
- **Plano de fallback de IA documentado** (`plano-fallback-ia-extracao-nf.md`): IA como último recurso, com métricas separadas no dashboard para controlar custo
- Segredos exclusivamente no backend; front nunca vê token/client secret
- React + TypeScript + Vite no painel; Docker Compose com variantes para Hostinger, Oracle e ngrok (demo)

## Desafios e soluções

- **Confiabilidade acima de "mágica de IA"**: hierarquia determinístico-primeiro tornou o custo de IA marginal e a taxa de acerto auditável por recorte no dashboard.
- **Planilha viva compartilhada com o cliente final**: escrita cirúrgica preservando o artefato que a operação já usava — adoção sem mudança de hábito.
- **Regras de negócio da operação** (CNPJ da concessionária → ponto de coleta): implementadas como enriquecimento automático dos dados extraídos.

## Resultados e impacto

- Eliminou digitação manual de NFs na planilha operacional [volume/dia A CONFIRMAR]
- Auditoria completa: toda NF processada tem origem, método de extração e resultado registrados
- Custo de IA controlado: maioria dos documentos resolvida por parsing determinístico [percentual A CONFIRMAR no dashboard]

## Destaques para entrevista (STAR resumido)

- **S/T:** operação logística alimentava planilha de demanda Stellantis manualmente a partir de NFs recebidas por e-mail. **A:** construí pipeline FastAPI + Graph API com extração em camadas (XML determinístico → PDF → IA/OCR como fallback), preenchimento não-destrutivo da planilha e painel com fila de falhas. **R:** processo automatizado de ponta a ponta em produção, com auditoria completa e uso de IA apenas onde necessário — controlando custo e mantendo confiança da operação.
