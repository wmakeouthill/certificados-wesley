---
title: Notes app + Vue/React/Angular comparison
category: freela
status: Study
stack: [Vue 3, Spring Boot, SQLite]
order: 8
---
# Case — Vue 3 + Spring Boot Notes App (technical study/evaluation)

**Type:** Technical evaluation/study project (freela-workspace)
**Role:** Full Stack Developer
**Status:** Completed (demonstration scope)
**Stack:** Vue 3 (Composition API, Vite, TypeScript), Java 21, Spring Boot (Web + Data JPA), SQLite, Docker Compose (incl. test compose)

## Context

A project to demonstrate mastery of a third frontend framework (Vue 3) beyond day-to-day work with Angular and React, implementing a complete notes/dashboard application with a Java backend.

## What was built

- Vue 3 frontend with the Composition API, `<script setup>` and TypeScript, built with Vite
- Spring Boot backend (Java 21) with Spring Data JPA over SQLite (community dialect)
- Docker Compose for the app and for the test suite (separate test Dockerfiles)
- **Technical comparison document: Vue vs. React vs. Angular** covering mental model, reactivity (Proxies vs. immutability/VDOM vs. Signals/Zone.js), global state and trade-offs — with a well-founded justification for choosing Vue for this case

## Why this case matters

It's not the size of the project, it's evidence of **versatility across the three major frameworks**: the comparison demonstrates understanding of each one's internal reactivity and rendering mechanisms — the kind of depth that distinguishes "uses a framework" from "understands a framework".

## Interview highlights

- Able to justify a framework choice by mechanism (fine-grained reactivity vs. reconciliation vs. change detection), not by preference
- Same quality standard as the larger projects: TypeScript, containerization and tests from the start
