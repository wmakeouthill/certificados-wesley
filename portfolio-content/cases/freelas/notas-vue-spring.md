---
title: App de anotações + comparativo Vue/React/Angular
category: freela
status: Estudo
stack: [Vue 3, Spring Boot, SQLite]
order: 8
---
# Case — App de Anotações Vue 3 + Spring Boot (estudo/avaliação técnica)

**Tipo:** Projeto de avaliação/estudo técnico (freela-workspace)
**Papel:** Desenvolvedor Full Stack
**Status:** Concluído (escopo de demonstração)
**Stack:** Vue 3 (Composition API, Vite, TypeScript), Java 21, Spring Boot (Web + Data JPA), SQLite, Docker Compose (incl. compose de testes)

## Contexto

Projeto para demonstrar domínio de um terceiro framework frontend (Vue 3) além do dia a dia com Angular e React, implementando uma aplicação de anotações/dashboard completa com backend Java.

## O que foi construído

- Frontend Vue 3 com Composition API, `<script setup>` e TypeScript, buildado com Vite
- Backend Spring Boot (Java 21) com Spring Data JPA sobre SQLite (dialeto community)
- Docker Compose para app e para suíte de testes (Dockerfiles separados de teste)
- **Documento técnico comparativo Vue vs. React vs. Angular** cobrindo modelo mental, reatividade (Proxies vs. imutabilidade/VDOM vs. Signals/Zone.js), estado global e trade-offs — com justificativa fundamentada da escolha do Vue para o caso

## Por que este case importa

Não é o tamanho do projeto, é a evidência de **versatilidade entre os três grandes frameworks**: o comparativo demonstra entendimento dos mecanismos internos de reatividade e renderização de cada um — o tipo de profundidade que diferencia "usa framework" de "entende framework".

## Destaques para entrevista

- Capaz de justificar escolha de framework por mecanismo (fine-grained reactivity vs. reconciliation vs. change detection), não por preferência
- Mesmo padrão de qualidade dos projetos grandes: TypeScript, containerização e testes desde o início
