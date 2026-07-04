# Case — AutoU Website (Site Institucional com SEO e Captura de Leads)

**Tipo:** AutoU (produto interno — presença digital da empresa)
**Papel:** Desenvolvedor Full Stack — projeto solo (site completo, incluindo CMS)
**Status:** No ar (em produção)
**Stack:** Vite + React + TypeScript, FastAPI + Pydantic, PostgreSQL (instância Aura), CMS próprio para artigos/cases, SSG/ISR para SEO, Microsoft Graph (app registrado no Azure) para recepção de e-mails, Docker Compose, Microsoft Azure, Nginx

## Contexto e problema

O site institucional da AutoU precisava ser reconstruído com foco em SEO (blog, cases de sucesso, indexação), captura de leads integrada ao ecossistema interno e caminho evolutivo para CMS — sem prender a empresa a plataforma de terceiros.

## Solução

Monorepo com frontend público otimizado para SEO, backend enxuto e CMS — construído por mim de ponta a ponta:

- **Frontend**: site público com blog e cases (`/blog`, `/cases` com paginação e slugs), conteúdo consumido por camada de serviços desacoplada (`getBlogPosts`, `getCases`)
- **CMS de conteúdo**: gestão de artigos e cases de sucesso implementada (plano `PLANO-CMS-ARTIGOS-CASES`), permitindo ao time publicar sem depender de dev
- **Backend FastAPI**: API de leads (+ health), persistência no Postgres do ecossistema Aura, e-mail transacional apenas para o time interno
- **Integração de e-mail → funil CRM**: recepção de e-mails via **Microsoft Graph** (app registrado no Azure) com registro automático no funil do CRM — contato que chega por e-mail entra no mesmo funil dos leads capturados pelo site
- **Estratégia de render por tipo de conteúdo**: SSG para institucional/MDX, ISR quando entrar CMS, SSR só se necessário — decisão documentada em ADR
- **SEO operacional**: guia de indexação, plano de SEO/SSR/cache e ajustes de design a partir do Figma versionados no repo

## Decisões técnicas notáveis

- **Camada de conteúdo desacoplada**: contrato de acesso a conteúdo definido antes do CMS — as páginas não mudaram quando o conteúdo migrou de MDX local para o CMS
- **Deploy em Azure na infra Aura** (decisão explícita de sair da Vercel), com Docker Compose local e CI em GitHub Actions
- Arquitetura frontend feature-based com atomic design; backend em módulos DDD-light

## Resultados e impacto (esperados)

- Site institucional com blog/cases indexáveis alimentando o funil de vendas [métricas de SEO/leads A CONFIRMAR]
- Leads integrados diretamente ao Postgres do ecossistema interno (CRM Aura)
- E-mails recebidos registrados automaticamente no funil do CRM (via Microsoft Graph), sem triagem manual de caixa de entrada [volume A CONFIRMAR]

## Destaques para entrevista (STAR resumido)

- **S/T:** site institucional precisava de SEO forte, blog/cases e captura de leads sem dependência de plataforma de terceiros. **A:** trabalhei no monorepo Vite/React + FastAPI com camada de conteúdo desacoplada (MDX→CMS sem reescrita), estratégia SSG/ISR documentada em ADR, deploy em Azure e integração de e-mail via Microsoft Graph (app registrado no Azure) alimentando o funil do CRM. **R:** arquitetura pronta para escalar conteúdo e captar leads por dois canais — formulário do site e e-mails recebidos — integrados ao funil do CRM interno.
