# 🎮 LOL Matchmaking System — Advanced Custom Matchmaking Platform

## 🚀 Overview

A full desktop+cloud platform for custom League of Legends matchmaking with drafts, Discord automation, and LCU validation. Built with a modern, enterprise stack (Spring Boot, Angular, Electron) and distributed cache.

### 🎯 Value Proposition

- **Intelligent matchmaking** with MMR-based balancing
- **Native LoL integration** via LCU for real-time validation
- **Full Discord automation** (channels, permissions, spectators)
- **Centralized backend** with multi-instance scalability
- **Premium desktop UX** with Electron + TypeScript

## 🏗️ High-Level Architecture

```mermaid
%%{title: "LOL Matchmaking Architecture"}%%
graph TB
    A[Electron Desktop] --> B[Spring Boot Backend]
    B --> C[MySQL]
    B --> D[Redis Cache]
    B --> E[Discord Bot (JDA)]
    B --> F[Angular Frontend]
    F --> G[WebSocket]
    A --> H[League Client (LCU)]
    E --> I[Discord Server]
```

### Core Flow

1. Electron starts backend; Angular connects via WebSocket
2. Player logs in and joins queue
3. Matchmaking algorithm forms balanced teams
4. Draft runs with LCU validation
5. Discord channels auto-created/managed
6. Match monitored; results validated and stored

### Cache & Locks (Redis)

- Session, queue, match/draft state, Discord channels, player stats
- Distributed locks + TTL for atomic operations and cleanup

## 🧱 Tech Stack

### Backend (Spring Boot 3.3.2, Java 21)

- Spring Web/Security/Data JPA, MySQL (prod) + H2 (dev)
- Redis Upstash + Redisson locks
- WebSockets/Socket.IO, JDA (Discord), LCU integration
- MapStruct, Lombok, Caffeine cache, Resilience4j

### Frontend (Angular 20 + TS)

- Standalone components, RxJS, SCSS, Angular Material
- WebSocket client + REST

### Desktop (Electron 28 + TS)

- LCU integration, WebSocket client, filesystem access

### DevOps

- Docker/Compose, Google Cloud Run, MySQL cloud, Redis Upstash
- CI/CD, health checks (Actuator), structured logging

## 🎯 Functional Highlights

- **Matchmaking**: MMR-balanced queue, LP system, Discord notifications
- **Draft**: Picks/bans with timers, Redis-backed state, LCU validation
- **LoL Integration**: Auto-detect client, validate actions, monitor games, capture results
- **Discord Automation**: Auto-create channels, spectator mute/unmute, permissions, TTL cleanup
- **Voting & Results**: Democratic result voting, integrity checks, leaderboards
- **Reliability**: Multi-backend sync, locks, retries, cache layers

## 🔧 Notable Systems

- **Distributed draft with Redis** (atomic sets, TTL, locks)
- **Adapter-based integrations** for Discord/LCU
- **WebSocket real-time sync** between desktop and cloud
- **Health/metrics** via Spring Actuator

## 🛠️ Skills Demonstrated

Java 21 + Spring Boot, microservices-style design, Redis distributed state, WebSockets, Discord API (JDA), LCU integration, Angular 20, Electron, Docker/Cloud Run, CI/CD, observability.

---
Built with ❤️ for the League of Legends community.
