---
title: Colibri — P&D de formulações com otimização Bayesiana
client: Oxiquímica
category: autou
status: Produção
stack: [FastAPI, React 19, Vertex AI, BayBE]
order: 5
---

# Case — Oxiquímica (Plataforma de P&D de Formulações com Otimização Bayesiana)

**Tipo:** AutoU (cliente: Oxiquímica — indústria química/fertilizantes)
**Papel:** Discovery técnico, arquitetura e prototipagem — tradução de processo de laboratório em produto de software; liderança técnica de frentes do projeto (em equipe), com contato direto com o cliente em pontos semanais e alinhamentos pontuais
**Status:** No ar (em produção)
**Stack (definida):** Python 3.13, FastAPI, React 19 + TypeScript, Vertex AI (Google Cloud), Gemini via `google-genai`, BayBE (otimização Bayesiana, open-source da Merck), RAG com governança de fontes, PostgreSQL

> Nota de confidencialidade: projeto de cliente da AutoU — validar o que pode ser público antes de expor nome/detalhes.

## Contexto e problema

O laboratório de P&D da Oxiquímica desenvolve formulações (fertilizantes e afins) por tentativa e erro: cada iteração passa por ciclo de estufa/câmara climática de ~14 dias, e o conhecimento de quais combinações funcionam vive na cabeça dos analistas. Muitas iterações = meses até uma fórmula estável.

## Solução (produto desenhado)

Plataforma de P&D com agente de IA generativa ("Colibri", Gemini via `google-genai`) que gera/ajuda em fórmulas e reduz iterações físicas:

- **Hub de Gestão de Formulações**: KPIs (taxa de sucesso, iterações médias), cards por formulação com probabilidade de estabilidade e contagem regressiva do teste climático
- **Tabela de composição reativa**: autocomplete do banco de matérias-primas, garantia atendida auto-preenchida, pureza média sugerida (editável por lote) e **garantia calculada em tempo real** (`concentração × pureza`) — calculada no front e revalidada no backend
- **Otimização Bayesiana com BayBE**: sugestão da próxima formulação a testar com base nos experimentos anteriores — menos ciclos de estufa até a meta
- **Chat Científico com RAG duplo**: responde consultando a base interna de conhecimento e pesquisa web com **whitelist/blacklist de fontes** (governança de citações, cada resposta rastreável à origem)
- **Versionamento explícito de fórmulas** (V0, V1... com autor e status) e linha do tempo do processo (definição → análise IA → câmara climática → parecer → aprovação)

## Trabalho técnico realizado

- **Estudo aprofundado do BayBE** (framework da Merck) com exemplos Python próprios versionados — validação de viabilidade antes de prometer ao cliente
- **Arquitetura completa documentada** a partir do protótipo Figma + comentários do designer, transformando cada comentário em especificação executável (comportamento campo a campo da tabela de composição)
- **Decisões de arquitetura registradas**: cálculo reativo no front com revalidação no backend como fonte de verdade; override de pureza por composição sem alterar o cadastro da MP; política default de bloqueio para fontes web não listadas
- Levantamento e catalogação do acervo de materiais do cliente (catálogo geral e mapa detalhado de matérias-primas)
- **Observabilidade com Grafana + Prometheus** implementada por mim: monitoramento de custo (uso de IA), consumo e infraestrutura da plataforma

## Desafios e soluções

- **Domínio científico complexo**: química de formulações traduzida em modelo de domínio (garantias, purezas por lote, funções de MP) validado com o designer e o cliente
- **IA com responsabilidade**: em ambiente industrial confidencial, o RAG web tem governança explícita de fontes — recomendação de bloquear por padrão
- **Discovery guiado por protótipo**: dúvidas abertas documentadas e endereçadas ao cliente em vez de suposições silenciosas

## Resultados e impacto

- Modernização do processo de P&D que já existia: fluxo antes manual/tentativa-e-erro virou plataforma automatizada com assistência de IA e **recomendação de estabilidade via otimização Bayesiana (BayBE)** — em produção
- Conhecimento de laboratório capturado em base consultável (RAG) em vez de conhecimento tribal
- Ciclo de estufa acompanhado digitalmente com interrupção informada

## Destaques para entrevista (STAR resumido)

- **S/T:** P&D químico iterando por tentativa e erro com ciclos físicos de 14 dias. **A:** conduzi o discovery técnico — estudei e validei o BayBE (otimização Bayesiana) com exemplos próprios, escrevi a arquitetura FastAPI + React 19 + Vertex AI a partir do protótipo Figma, e especifiquei o RAG científico com governança de fontes. **R:** arquitetura aprovada como base do plano de implementação, com viabilidade de IA validada antes de qualquer promessa ao cliente.
