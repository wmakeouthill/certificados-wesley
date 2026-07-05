---
title: Experimenta AI — Full restaurant management + delivery
client: Soneca
category: freela
status: Production
stack: [Java, Spring Boot, Angular 17, Electron, MySQL]
order: 10
gallery: experimenta-ai---soneca
---
# Case — Experimenta AI (Soneca): Restaurant Management + Delivery Ecosystem

**Type:** In-house product for a real client (food service — snack bar)
**Role:** Full Stack Developer — full authorship (desktop POS + delivery platform)
**Status:** Full restaurant management **in production** (counter, table ordering via QR code, self-service kiosk); delivery ecosystem built (Java 17 + Angular 20+), currently deactivated
**Stack:** Java 17 + Spring Boot 3.2 (Maven multi-module, Clean Architecture), Angular 17+ for management and Angular 20+ for delivery (Standalone Components), Electron (POS + print server), MySQL 8 + Liquibase, ESC/POS thermal printing, Google Maps Platform (Directions/Geocoding/Places), Google OAuth, SSE, PWA, Docker Compose

## Context and problem

A snack bar needed to move from paper/WhatsApp to an organized operation: counter orders with printed receipts, a manageable menu, and later an expansion into its own delivery — without paying marketplace fees (iFood and similar) or losing the direct relationship with the client.

## Solution

A two-phase ecosystem built on the same Clean Architecture foundation:

**Phase 1 — Full restaurant management (in production):**
- Order, menu, customer and authentication management in an Electron desktop app
- **Table ordering via QR code** and a **self-service kiosk**, in addition to the counter flow — multiple order channels converging into the same operation
- **ESC/POS receipt printing** via an Electron print server: support for Windows Spooler, direct USB, CUPS (Linux) and network printers — tested with EPSON TM-T20 and DARUMA DR-800

**Phase 2 — Delivery (built with Java 17 + Angular 20+; currently deactivated):**
- **Customer app (PWA)**: menu, ordering, addresses with Google Places autocomplete, favorites/reorder, status timeline and **real-time courier tracking on the map**
- **Courier app (PWA)**: self-registration via a public link with admin approval, Google OAuth login, Kanban of own deliveries, GPS position reporting
- **Manager panel**: management of delivery orders and couriers

## Architecture and technical decisions

- **Maven multi-module with Clean Architecture**: modules by domain (orders, menu, customers, authentication, printing) — delivery was born as a module extension, not a fork
- **High-frequency tracking without overloading the database**: courier positions cached in a `ConcurrentHashMap` with TTL, decoupled writes via asynchronous events (the HTTP connection returns immediately) and **broadcast via Server-Sent Events** — the customer sees the courier move without polling
- **Hybrid authentication**: internal JWT for admin/staff; Google OAuth exchanged for a session JWT with distinct claims for customer and courier
- **Location privacy**: the customer only accesses the position of their designated courier, and only while the order is "out for delivery"
- **Mobile-first PWA**: customer and courier install it as an app with no app store
- **MySQL + Liquibase, Docker Compose** for reproducible dev and deployment

## Challenges and solutions

- **Heterogeneous printing hardware**: an in-house ESC/POS conversion layer in the Electron print server abstracting spooler/USB/CUPS per platform
- **Cheap real time**: SSE + in-memory cache instead of full-duplex WebSocket and per-coordinate database writes — simple, and sufficient for the case
- **Operation by non-technical staff**: counter flows designed for service speed (order → printed receipt in seconds)

## Results and impact

- Full restaurant management **in production for ~3 months**, handling around **R$ 300k/month in sales** — counter (order→receipt in seconds), table ordering via QR code and self-service kiosk
- Own delivery platform built (Java 17 + Angular 20+) — a direct channel with no marketplace fee; currently deactivated, ready for reactivation whenever the client wants
- Proven modular foundation: delivery reused domain, authentication and menu from phase 1

## Interview highlights (STAR summary)

- **S/T:** a paper-based snack bar wanted organized orders with printed receipts and, later, its own delivery with no marketplace fees. **A:** I built the complete ecosystem — a desktop POS with a cross-platform ESC/POS print server, table ordering via QR code, a self-service kiosk, and the delivery extension with PWAs for customer and courier, real-time tracking (GPS → TTL cache → SSE), hybrid Google OAuth and a multi-module Clean Architecture that let delivery be born as an extension. **R:** end-to-end restaurant management in production (counter, table and kiosk) handling ~R$ 300k/month in sales, and an own delivery platform built (Java 17 + Angular 20+), currently deactivated and ready for reactivation.
