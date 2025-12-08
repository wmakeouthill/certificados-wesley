# Stacks and Technologies - Wesley Correia

Complete documentation of the technologies, languages, frameworks, and tools used by Wesley Correia in his professional and personal projects.

## Overview

Wesley Correia works with a modern, enterprise stack focused on full-stack development with Java/Spring on the backend and Angular on the frontend. He has diversified experience across different sectors, from simple automations to critical financial infrastructure systems.

### Current Main Stack

**Backend:** Java 17/21 + Spring Boot 3.x + Oracle/MySQL/PostgreSQL  
**Frontend:** Angular 17+/18/19/20 + TypeScript + RxJS  
**DevOps:** Docker + GitLab CI/CD + Google Cloud Run  
**Observability:** Prometheus + Grafana + Spring Actuator  
**Databases:** Oracle, MySQL, PostgreSQL, SQLite, Redis

### Areas of Expertise

1. **Enterprise Full-Stack Development** - Java/Spring + Angular
2. **Observability and Monitoring** - Prometheus, Grafana, Micrometer
3. **DevOps and Containerization** - Docker, CI/CD, Cloud Deploy
4. **Legacy System Migration** - COBOL → Modern Java
5. **Automation and RPA** - Python, Selenium, VBA
6. **Business Intelligence** - Power BI, DAX, Dashboards

## Programming Languages

### Java

**Version:** Java 17 (LTS) and Java 21

**Usage Context:**

- Main language for enterprise backend development
- Used in all Spring Boot projects
- Application of modern features: records, sealed classes, pattern matching, text blocks
- Extensive use in projects such as LoL Matchmaking Fazenda, Experimenta AI - Soneca, Mercearia R-V

**Projects:**

- LoL Matchmaking Fazenda: Complete backend with Java 21 and Spring Boot 3.3.2
- Experimenta AI - Soneca: Full-stack system with Java 17 and Clean Architecture
- Mercearia R-V: Enterprise desktop system with Java 21 and Spring Boot 3.5.5

### TypeScript

**Version:** TypeScript 5.4.2, 5.7.2, 5.8

**Usage Context:**

- Main language for frontend and desktop development
- Static typing for scalable development
- Used in all Angular and Electron projects
- Object-oriented programming and well-defined interfaces

**Projects:**

- All Angular projects (17+, 18, 19, 20)
- Electron applications (LoL Matchmaking, Mercearia R-V)
- Node.js backend with TypeScript (AA Space)

### JavaScript

**Usage Context:**

- Base of the frontend ecosystem
- Integration with APIs and libraries
- Automation and build scripts
- Node.js for backend development

### Python

**Usage Context:**

- Automation scripts
- Data analysis
- Integration with Power BI
- Process automation

## Backend Frameworks and Libraries

### Spring Boot

**Version:** Spring Boot 3.2.3, 3.3.2, 3.5.5

**Usage Context:**

- Market-leading enterprise framework for Java development
- Foundation of all Java backend projects
- Microservices and RESTful APIs
- Integration with Spring Security, Spring Data JPA, Spring Web

**Projects:**

- LoL Matchmaking Fazenda: Spring Boot 3.3.2 with Java 21
- Experimenta AI - Soneca: Spring Boot 3.2.3 with Java 17
- Mercearia R-V: Spring Boot 3.5.5 with Java 21

### Spring Framework

**Components Used:**

- **Spring Web:** RESTful APIs and microservice architecture
- **Spring Data JPA:** Industry-standard ORM with Hibernate
- **Spring Security:** Most robust security framework
- **Spring Validation:** Enterprise data validation
- **Spring Mail:** Email notification system
- **Spring Actuator:** Health checks and metrics

### Spring Security

**Usage Context:**

- Authentication and authorization
- JWT tokens for stateless APIs
- Granular access control
- Integration with Spring Boot

### JPA/Hibernate

**Usage Context:**

- Industry-standard Java ORM
- Object-relational mapping
- Optimized queries
- Entity relationships

## Frontend Frameworks and Libraries

### Angular

**Versions:** Angular 17.3.0, 18.0.0, 19.1.0, 20.1.3

**Usage Context:**

- Market-leading enterprise framework for frontend development
- Standalone components (modern architecture without modules)
- Signals for modern reactivity
- Reactive Forms for complex forms
- Dependency Injection with `inject()`

**Projects:**

- LoL Matchmaking Fazenda: Angular 20 with WebSockets
- Experimenta AI - Soneca: Angular 17+ with Clean Architecture
- Traffic Manager: Angular 18 with signals and standalone components
- Investment Calculator: Angular 18 with signals and computed properties
- First Angular App: Angular 19 with fundamental concepts
- AA Space: Angular 19 with real-time chat

### RxJS

**Version:** RxJS 7.8.0

**Usage Context:**

- Reactive programming (enterprise standard)
- Observables for asynchronous operations
- Operators for data transformation
- Integration with Angular HTTP Client
- Reactive state management

### Angular Material

**Version:** Angular Material 20.1.3

**Usage Context:**

- UI components following Material Design
- Consistent and professional interface
- Built-in accessibility
- Customizable themes

### Socket.IO

**Usage Context:**

- Real-time WebSocket communication
- Real-time chat (AA Space)
- Instant updates (LoL Matchmaking)
- Bidirectional client-server integration

## Databases

### MySQL

**Version:** MySQL 8.0+

**Usage Context:**

- Enterprise relational database for production
- Used in Spring Boot projects
- Integration with Spring Data JPA
- Migrations with Liquibase

**Projects:**

- LoL Matchmaking Fazenda: MySQL 8.0 in production
- Experimenta AI - Soneca: MySQL with Clean Architecture

### PostgreSQL

**Usage Context:**

- Robust enterprise relational database
- Used in desktop projects (Mercearia R-V)
- PostgreSQL embedded in Electron applications
- Migrations with Liquibase

**Projects:**

- Mercearia R-V: Full embedded PostgreSQL

### SQLite

**Usage Context:**

- Embedded relational database
- Development and prototyping
- Lightweight desktop applications

**Projects:**

- AA Space: SQLite3 with TypeORM

### Redis

**Usage Context:**

- Cloud-native distributed cache
- Real-time state management
- Distributed locks for atomic operations
- Session management

**Projects:**

- LoL Matchmaking Fazenda: Redis Upstash for cache and distributed state

## Development Tools

### Maven

**Usage Context:**

- Java dependency management
- Build and packaging
- Lifecycle management
- Integration with Spring Boot

### Lombok

**Version:** Lombok 1.18.36

**Usage Context:**

- Boilerplate reduction
- `@RequiredArgsConstructor` for dependency injection
- `@Builder` for complex objects
- `@Getter`, `@Setter`, `@Data` when appropriate

### Liquibase

**Version:** Liquibase 4.25.0

**Usage Context:**

- Schema version control
- Database migrations
- Rollback of changes
- Versioning of data structures

### Git

**Usage Context:**

- Version control
- Team collaboration
- Branching strategies
- Integration with GitHub

### GitHub

**Usage Context:**

- Code repository
- GitHub Actions for CI/CD
- Issues and pull requests
- GitHub Pages for deploy

## Containerization and DevOps

### Docker

**Usage Context:**

- Application containerization
- Multi-stage builds for optimization
- Consistent environments
- Simplified deploy

**Projects:**

- All backend projects use Docker
- Docker Compose for local orchestration

### Docker Compose

**Usage Context:**

- Orchestration of multiple containers
- Local development
- Full stack (app + database + cache)

### Google Cloud Run

**Usage Context:**

- Serverless containers
- Automatic scaling
- Simplified deploy
- Integration with Cloud Build

**Projects:**

- Wesley Portfolio: Deploy on Google Cloud Run
- LoL Matchmaking Fazenda: Backend on Cloud Run

### Cloud Build

**Usage Context:**

- Automated CI/CD
- Docker image builds
- Automatic deploy
- Integration with GitHub

### Kubernetes

**Usage Context:**

- Container orchestration
- Horizontal scalability
- Service management
- Production deploy

### NGINX

**Usage Context:**

- Web server
- Reverse proxy
- Load balancing
- SSL/TLS termination

### Certbot

**Usage Context:**

- Automatic SSL certificates
- Automatic renewal
- Integration with Let's Encrypt

## Desktop Applications

### Electron

**Version:** Electron 27, 28

**Usage Context:**

- Cross-platform desktop applications
- Integration with native APIs
- File system access
- Communication with backend processes

**Projects:**

- LoL Matchmaking Fazenda: Electron 28 with LCU integration
- Mercearia R-V: Electron 27 with embedded backend

### electron-builder

**Version:** electron-builder 24.9.1

**Usage Context:**

- Application packaging
- Installer builders (NSIS for Windows)
- Cross-platform distribution
- Inclusion of resources and dependencies

## Integrations and APIs

### JDA (Java Discord API)

**Usage Context:**

- Discord integration
- Server automation
- Dynamic channel creation
- Permission management

**Projects:**

- LoL Matchmaking Fazenda: Complete Discord bot with automation

### OpenAI API

**Usage Context:**

- GPT integration
- Intelligent chatbots
- Natural language processing
- Content generation

**Projects:**

- Wesley Portfolio: Chatbot with portfolio-trained AI
- Obaid with Bro: Thematic chatbot

### LCU Integration (League of Legends)

**Usage Context:**

- Integration with game client
- Real-time action validation
- Match monitoring
- Automatic player detection

**Projects:**

- LoL Matchmaking Fazenda: Full integration with League of Legends

## Specific Libraries and Tools

### MapStruct

**Usage Context:**

- Type-safe object mapping
- Conversion between DTOs and entities
- Boilerplate reduction

### Redisson

**Usage Context:**

- Distributed locks for Redis
- Atomic operations
- Distributed synchronization

**Projects:**

- LoL Matchmaking Fazenda: Distributed locks for matchmaking

### Caffeine Cache

**Usage Context:**

- High-performance local cache
- In-memory cache
- Optimization of frequent queries

### Resilience4j

**Usage Context:**

- Circuit breaker
- Automatic retry
- Rate limiting
- Application resilience

### OpenHTMLToPDF

**Version:** OpenHTMLToPDF 1.0.10

**Usage Context:**

- Server-side PDF generation
- HTML templates to PDF
- Automated reports

**Projects:**

- Mercearia R-V: Generation of invoices and reports

### PDFBox

**Version:** PDFBox 2.0.29

**Usage Context:**

- Advanced PDF processing
- PDF manipulation
- Data extraction

### Chart.js

**Version:** Chart.js 4.4.3

**Usage Context:**

- Data visualization
- Interactive charts
- Dashboards

**Projects:**

- Mercearia R-V: Sales charts and reports
- Traffic Manager: Traffic visualization

### TypeORM

**Version:** TypeORM 0.3.22

**Usage Context:**

- Modern ORM with TypeScript
- Migrations
- Relationships

**Projects:**

- AA Space: TypeORM with SQLite

### JWT (jjwt)

**Version:** jjwt 0.11.5

**Usage Context:**

- Stateless authentication
- Secure tokens
- Refresh tokens
- Integration with Spring Security

## Analytics and BI Tools

### Power BI

**Usage Context:**

- Data analysis
- Business Intelligence
- Dashboards and reports
- Data visualization

### Selenium

**Usage Context:**

- Test automation
- Web scraping
- End-to-end tests
- Browser automation

## Methodologies and Architectures

### Clean Architecture

**Usage Context:**

- Clean, modular architecture
- Separation of responsibilities
- Framework independence
- Testability

**Projects:**

- Experimenta AI - Soneca: Full Clean Architecture
- Mercearia R-V: Modular architecture

### Domain-Driven Design (DDD)

**Usage Context:**

- Domain-oriented design
- Entities and value objects
- Aggregates and repositories
- Ubiquitous language

### Microservices Patterns

**Usage Context:**

- Microservices architecture
- Communication between services
- Service discovery
- API Gateway

### Event-Driven Architecture

**Usage Context:**

- Event-driven architecture
- WebSockets for real time
- Pub/Sub patterns
- Event sourcing (when appropriate)

## Patterns and Practices

### RESTful APIs

**Usage Context:**

- RESTful APIs
- HTTP methods (GET, POST, PUT, DELETE)
- Appropriate status codes
- API versioning

### WebSockets

**Usage Context:**

- Bidirectional real-time communication
- Real-time chat
- Instant updates
- Push notifications

### JWT Authentication

**Usage Context:**

- Stateless authentication
- Secure tokens
- Refresh tokens
- Frontend integration

### CORS Configuration

**Usage Context:**

- Cross-origin access control
- Security policies
- Header configuration

## Observability and Monitoring

### Spring Actuator

**Usage Context:**

- Health checks
- Application metrics
- Monitoring endpoints
- System information

### SLF4J + Logback

**Usage Context:**

- Structured logging
- Different log levels
- Persisted logs
- Log analysis

### Health Checks

**Usage Context:**

- Health monitoring
- Dependency verification
- Service status
- Automatic alerts

## Category Summary

### Enterprise Backend

**Languages:** Java 17/21  
**Frameworks:** Spring Boot 3.x, Spring Framework  
**ORM:** JPA/Hibernate  
**Databases:** MySQL, PostgreSQL, Oracle  
**Tools:** Liquibase, Maven, Lombok  
**Use:** RESTful API development, enterprise systems, legacy system migration

### Modern Frontend

**Framework:** Angular 17+/18/19/20  
**Language:** TypeScript 5.x  
**Reactive Programming:** RxJS 7.8  
**Web Standards:** HTML5, CSS3/SCSS, JavaScript  
**Architecture:** Standalone Components, Signals, Reactive Forms  
**Use:** Modern interfaces, dashboards, SPA applications, real-time systems

### DevOps/Cloud

**Containerization:** Docker, Docker Compose  
**Cloud:** Google Cloud Run, Cloud Build  
**CI/CD:** CI/CD Pipelines, GitHub Actions, GitLab CI/CD  
**Infrastructure:** NGINX, Kubernetes, Certbot  
**Use:** Automated deploy, container orchestration, serverless, monitoring

### Desktop

**Framework:** Electron 27/28  
**Tools:** electron-builder  
**Language:** TypeScript  
**Integration:** Node.js Integration  
**Use:** Cross-platform desktop applications, integration with native systems

### Integrations

**External APIs:** JDA (Discord), OpenAI API, LCU (League of Legends)  
**Communication:** Socket.IO, WebSockets  
**Use:** Chatbots, automations, real-time integrations, bidirectional communication

### Observability and Monitoring

**Metrics:** Prometheus, Micrometer, Spring Actuator  
**Visualization:** Grafana  
**Alerts:** Alertmanager  
**Monitoring:** Blackbox Exporter  
**Use:** Monitoring critical systems, performance analysis, health checks

### Quality and Performance

**Mapping:** MapStruct  
**Cache:** Redisson, Caffeine Cache  
**Resilience:** Resilience4j  
**Logging:** SLF4J + Logback  
**Use:** Performance optimization, distributed cache, circuit breakers, structured logs

### Business Intelligence and Analytics

**BI:** Power BI, DAX  
**Automation:** Python, Selenium, VBA  
**Use:** Executive dashboards, data analysis, process automation, web scraping

### Documentation and Tools

**Version Control:** Git, GitHub, GitLab  
**Documentation:** Markdown  
**Tools:** Power BI, Selenium, Notion, SharePoint  
**Use:** Versioning, technical documentation, collaboration, knowledge management

### Architecture and Methodologies

**Architectures:** Clean Architecture, Domain-Driven Design, Modular Architecture  
**Patterns:** Microservices, Event-Driven Architecture  
**APIs:** RESTful APIs  
**Use:** Design of scalable systems, separation of responsibilities, enterprise architecture

## Proficiency Level by Technology

### Expert/Advanced (Professional use in critical projects)

- **Java 17/21:** Main language, used in critical systems
- **Spring Boot 3.x:** Main framework for enterprise backend
- **Angular 17+/18:** Main framework for modern frontend
- **TypeScript 5.x:** Main language for frontend and desktop
- **SQL/MySQL/PostgreSQL/Oracle:** Relational databases in production
- **Docker:** Containerization in all projects
- **Git/GitHub/GitLab:** Version control and CI/CD
- **Liquibase:** Database versioning
- **Prometheus/Grafana:** Observability in critical systems

### Intermediate/Advanced (Regular professional use)

- **JavaScript/HTML5/CSS3:** Frontend foundation
- **RxJS:** Reactive programming in Angular
- **Redis:** Distributed cache
- **Power BI/DAX:** Dashboards and data analysis
- **Python:** Automations and scripts
- **Selenium:** Web scraping and automation
- **VBA:** Automations in Excel
- **Node.js:** JavaScript backend when needed
- **Electron:** Desktop applications

### Intermediate (Occasional knowledge and use)

- **Kubernetes:** Container orchestration
- **NGINX:** Web server and proxy
- **Google Cloud Platform:** Cloud computing
- **SharePoint:** Corporate web development
- **Salesforce:** CRM and relationship management
- **Notion:** Knowledge management

## Usage Context by Project

### Professional Projects (ANBIMA/Selic)

**Main Stack:**

- Java + Spring Boot + Angular
- Oracle Database + Liquibase
- Docker + GitLab CI/CD
- Prometheus + Grafana + Spring Actuator + Micrometer

**Context:** Critical financial infrastructure systems, mainframe migration to modern Java

### Personal Projects (Portfolio)

**LoL Matchmaking Fazenda:**

- Java 21 + Spring Boot 3.3.2
- Angular 20 + TypeScript
- MySQL + Redis (Upstash)
- Electron 28
- Google Cloud Run

**Experimenta AI - Soneca:**

- Java 17 + Spring Boot 3.2.3
- Angular 17+ + TypeScript
- MySQL + Liquibase
- Clean Architecture

**Mercearia R-V:**

- Java 21 + Spring Boot 3.5.5
- Angular 20 + TypeScript
- Embedded PostgreSQL
- Electron 27

**AA Space:**

- Node.js + Express + TypeScript
- Angular 19 + TypeScript
- SQLite + TypeORM
- Socket.IO

## Stack Evolution

### 2017-2018 (Beginning)

- Excel, SAP (basic corporate systems)

### 2018-2019 (Automation)

- VBA, Advanced Excel, Salesforce

### 2019-2024 (Transition to Technology)

- Python, Selenium, VBA, RPA
- Web scraping and automations

### 2024-2025 (Management and BI)

- Power BI, DAX, JavaScript, SharePoint
- Dashboards and corporate web development

### 2025-Present (Full-Stack Enterprise)

- Java 17/21 + Spring Boot 3.x
- Angular 17+/18 + TypeScript
- Oracle + Liquibase
- Docker + CI/CD
- Prometheus + Grafana (complete observability)
