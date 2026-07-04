---
title: Mercearia R&V — Offline-first desktop POS
client: Mercearia R&V
category: freela
status: Production
stack: [Java 21, Spring Boot, Angular 20, Electron]
order: 9
gallery: mercearia-r-v
---
# Case — Mercearia R&V (Desktop Inventory and Sales Management System)

**Type:** In-house product for a real client (retail — grocery store)
**Role:** Full Stack Developer — full authorship (product, installer and support)
**Status:** In production (daily use in the grocery store's operation)
**Stack:** Java 21 + Spring Boot 3.5, Angular 20 + Angular Material, Electron 27 + TypeScript, embedded PostgreSQL, Liquibase, JWT (Spring Security), OpenHTMLToPDF/PDFBox, Chart.js, electron-builder + NSIS

## Context and problem

A neighborhood grocery store needed inventory, sales and cash-register management — but with no server, no SaaS subscription fee and no dependence on stable internet. Market systems were either too expensive for the business's size or required infrastructure the client didn't have.

## Solution

An **offline-first** desktop application that embeds the entire enterprise stack in a single Windows installer:

- **Complete POS**: cart, discounts, multiple payment methods (cash, card, PIX), exchanges and returns
- **Cash register management**: opening/closing with movement control
- **Audited inventory**: low-stock alerts, movement history, product image upload
- **Customers and loyalty**: registration, purchase history, points system
- **Reports**: Chart.js dashboards and server-side PDF generation (receipts and reports) with OpenHTMLToPDF

## Architecture and technical decisions

- **Embedded PostgreSQL + bundled JDK in the NSIS installer**: the client installs a single `.exe` and has an enterprise-grade relational database running locally — zero external dependency, zero subscription fee
- **Electron orchestrates the lifecycle**: splash screen, Spring Boot backend startup as a child process, health check before releasing the UI, clean process shutdown
- **Liquibase for schema versioning**: system updates migrate the client's database automatically, with no manual intervention
- **JWT even in a local app**: user profiles (owner vs. employee) with real authorization, not just hiding a button
- **Structured logs persisted to file**: viable remote support — the client sends the log, I diagnose without going on-site

## Challenges and solutions

- **Non-technical user as operator**: single installer, automatic startup of all services and a health check — if something doesn't come up, the UI warns instead of opening broken
- **Reliability without DevOps**: local database backups and automatic schema migration on every update
- **Modest hardware**: stack tuned to run on a typical counter machine

## Results and impact

- System in production running the grocery store's day-to-day operations (sales, cash register, inventory) [time in production / sales volume TO CONFIRM]
- Zero recurring cost for the client — no server, no subscription
- Complete product cycle: requirements gathering with the client → development → installer → operation and support

## Interview highlights (STAR summary)

- **S/T:** the grocery store needed sales/inventory management with no infrastructure, no stable internet and no recurring cost. **A:** I built an offline-first desktop app alone — Electron orchestrating an embedded Spring Boot and PostgreSQL in a single NSIS installer, with POS, cash register, audited inventory, loyalty and PDF reports, Liquibase for automatic schema migration and file logs for remote support. **R:** system in production in daily use by the business, with zero recurring cost and updates with no on-site technical intervention.
