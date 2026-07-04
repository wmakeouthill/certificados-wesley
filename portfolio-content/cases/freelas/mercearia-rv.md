# Case — Mercearia R&V (Sistema Desktop de Gestão de Estoque e Vendas)

**Tipo:** Produto próprio para cliente real (varejo — mercearia)
**Papel:** Desenvolvedor Full Stack — autoria completa (produto, instalador e suporte)
**Status:** Em produção (uso diário na operação da mercearia)
**Stack:** Java 21 + Spring Boot 3.5, Angular 20 + Angular Material, Electron 27 + TypeScript, PostgreSQL embarcado, Liquibase, JWT (Spring Security), OpenHTMLToPDF/PDFBox, Chart.js, electron-builder + NSIS

## Contexto e problema

Uma mercearia de bairro precisava de gestão de estoque, vendas e caixa — mas sem servidor, sem mensalidade de SaaS e sem depender de internet estável. Sistemas de mercado ou eram caros demais para o porte do negócio, ou exigiam infraestrutura que o cliente não tinha.

## Solução

Aplicação desktop **offline-first** que embarca o stack enterprise inteiro num único instalador Windows:

- **PDV completo**: carrinho, descontos, múltiplas formas de pagamento (dinheiro, cartão, PIX), trocas e devoluções
- **Gestão de caixa**: abertura/fechamento com controle de movimentações
- **Estoque com auditoria**: alertas de baixa, histórico de movimentações, upload de imagens de produtos
- **Clientes e fidelidade**: cadastro, histórico de compras, sistema de pontos
- **Relatórios**: dashboards com Chart.js e geração server-side de PDFs (notas e relatórios) com OpenHTMLToPDF

## Arquitetura e decisões técnicas

- **PostgreSQL embarcado + JDK empacotados no instalador NSIS**: o cliente instala um `.exe` e tem banco relacional enterprise rodando localmente — zero dependência externa, zero mensalidade
- **Electron orquestra o ciclo de vida**: splash screen, inicialização do backend Spring Boot como processo filho, health check antes de liberar a UI, encerramento limpo dos processos
- **Liquibase para versão de schema**: atualizações do sistema migram o banco do cliente automaticamente, sem intervenção manual
- **JWT mesmo em app local**: perfis de usuário (dono vs. funcionário) com autorização real, não só esconder botão
- **Logs estruturados persistidos em arquivo**: suporte remoto viável — o cliente manda o log, eu diagnostico sem ir até lá

## Desafios e soluções

- **Usuário não-técnico como operador**: instalador único, inicialização automática de todos os serviços e health check — se algo não subir, a UI avisa em vez de abrir quebrada
- **Confiabilidade sem DevOps**: backups locais do banco e migração automática de schema a cada atualização
- **Hardware modesto**: stack ajustado para rodar em máquina de balcão comum

## Resultados e impacto

- Sistema em produção operando o dia a dia da mercearia (vendas, caixa, estoque) [tempo em produção / volume de vendas A CONFIRMAR]
- Custo recorrente zero para o cliente — sem servidor, sem assinatura
- Ciclo completo de produto: levantamento com o cliente → desenvolvimento → instalador → operação e suporte

## Destaques para entrevista (STAR resumido)

- **S/T:** mercearia precisava de gestão de vendas/estoque sem infraestrutura, internet estável ou custo recorrente. **A:** construí sozinho um desktop offline-first — Electron orquestrando Spring Boot e PostgreSQL embarcados num único instalador NSIS, com PDV, caixa, estoque auditado, fidelidade e relatórios em PDF, Liquibase para migração automática de schema e logs em arquivo para suporte remoto. **R:** sistema em produção no uso diário do negócio, com custo recorrente zero e atualizações sem intervenção técnica no local.
