# 🌌 AA Space — Real-Time Community Platform

## 🚀 Overview

**AA Space** is a complete community and real-time communication platform built with a modern full-stack architecture. It provides a safe environment to share experiences, with an advanced chat system, interactive forum, and user management, all integrated into a responsive web experience.

### 🎯 Key Features

- **Complete Chat System:** Private and group conversations with advanced control
- **Interactive Forum:** Posts, comments, and likes system
- **User Management:** Customizable profiles with image uploads
- **Real-Time Communication:** WebSockets with Socket.IO
- **Modern Interface:** Responsive design with Angular 19
- **Robust Backend:** RESTful API with Node.js and Express

## 🏗️ System Architecture

```mermaid
%%{title: "Arquitetura Geral do AA_Space"}%%
graph TB
    A[Angular 19 Frontend] --> B[Node.js + Express Backend]
    B --> C[SQLite Database]
    B --> D[Socket.IO Server]
    D --> A
    
    subgraph "Frontend"
        A
        E[Chat System]
        F[Forum System]
        G[User Management]
    end
    
    subgraph "Backend"
        B
        C
        D
        H[JWT Authentication]
        I[TypeORM]
    end
```

## 🔄 Real-Time Communication Flows

### Hybrid Chat System (Private + Group)

```mermaid
%%{title: "Chat em Tempo Real com WebSockets"}%%
sequenceDiagram
    participant U1 as User 1
    participant U2 as User 2
    participant F as Frontend
    participant B as Backend
    participant S as Socket.IO
    participant DB as SQLite
    
    Note over U1,DB: Private Chat
    
    U1->>F: Sends message to User 2
    F->>S: socket.emit('send_message', data)
    S->>B: Process message
    B->>DB: Save message in DB
    DB-->>B: Message saved (ID: 123)
    B->>S: socket.to(roomId).emit('new_message', message)
    S->>F: Receives new message
    F->>U1: Updates interface
    F->>U2: Updates interface (if online)
    
    Note over U1,DB: Group Chat
    
    U1->>F: Sends message in group
    F->>S: socket.emit('send_group_message', data)
    S->>B: Process group message
    B->>DB: Save group message
    DB-->>B: Message saved
    B->>S: socket.to(groupRoomId).emit('new_group_message', message)
    S->>F: Broadcast to everyone in group
    F->>U1: Updates interface
    F->>U2: Updates interface
    F->>U3: Updates interface (other members)
```

### Interactive Forum System

```mermaid
%%{title: "Fluxo do Sistema de Fórum com Interações"}%%
sequenceDiagram
    participant U as User
    participant F as Frontend
    participant B as Backend
    participant DB as SQLite
    participant WS as WebSocket
    
    Note over U,WS: Post Creation
    
    U->>F: Creates new post
    F->>B: POST /api/posts
    B->>B: Validate data + authentication
    B->>DB: INSERT INTO posts
    DB-->>B: Post created (ID: 456)
    B->>WS: Broadcast new post
    WS->>F: All users receive notification
    F->>U: Confirmation + post visible
    
    Note over U,WS: Like System
    
    U->>F: Clicks "Like" on post
    F->>B: POST /api/posts/456/like
    B->>DB: Check if already liked
    alt Already liked
        DB-->>B: Remove like
        B->>DB: DELETE FROM likes
    else Not liked
        DB-->>B: Add like
        B->>DB: INSERT INTO likes
    end
    DB-->>B: Operation completed
    B->>WS: Broadcast likes update
    WS->>F: Update counter in real time
    
    Note over U,WS: Real-Time Comments
    
    U->>F: Adds comment
    F->>B: POST /api/posts/456/comments
    B->>DB: Save comment
    DB-->>B: Comment saved
    B->>WS: Broadcast new comment
    WS->>F: Everyone sees the comment instantly
```

## 🔐 Authentication and Sessions

### JWT Flow with Refresh Tokens

```mermaid
%%{title: "Sistema de Autenticação JWT com Refresh Tokens"}%%
sequenceDiagram
    participant U as User
    participant F as Frontend
    participant B as Backend
    participant DB as SQLite
    
    Note over U,DB: Initial Login
    
    U->>F: Enter credentials
    F->>B: POST /api/auth/login
    B->>B: Validate credentials
    B->>DB: SELECT user WHERE email/password
    DB-->>B: User found
    B->>B: Generate JWT access token (15min)
    B->>B: Generate refresh token (7 days)
    B->>DB: Save refresh token
    DB-->>B: Token saved
    B-->>F: {accessToken, refreshToken, user}
    F->>F: Store tokens in localStorage
    
    Note over U,DB: Authenticated Requests
    
    F->>B: GET /api/profile (with access token)
    B->>B: Verify JWT
    alt Token valid
        B-->>F: Profile data
    else Token expired
        B-->>F: 401 Unauthorized
        F->>B: POST /api/auth/refresh (with refresh token)
        B->>DB: Verify refresh token
        DB-->>B: Token valid
        B->>B: Generate new access token
        B-->>F: New access token
        F->>B: GET /api/profile (with new token)
        B-->>F: Profile data
    end
    
    Note over U,DB: Logout
    
    U->>F: Clicks logout
    F->>B: POST /api/auth/logout
    B->>DB: Remove refresh token
    DB-->>B: Token removed
    B-->>F: Logout confirmed
    F->>F: Clear localStorage
```

## 🛠️ Tech Stack

### Frontend

- **Angular 19** – Enterprise framework with TypeScript 5.7
- **RxJS 7.8** – Reactive programming
- **Socket.IO Client** – WebSocket communication
- **CSS3** – Responsive, modern interface

### Backend

- **Node.js** – Server-side JavaScript runtime
- **Express.js 4.18** – Web framework
- **TypeScript 5.8** – Static typing
- **Socket.IO 4.8** – WebSocket server

### Database

- **SQLite3** – Embedded relational database
- **TypeORM 0.3.22** – Modern ORM with TypeScript
- **Migrations** – Schema versioning

### Security & Auth

- **JWT** – Secure tokens for auth
- **bcrypt** – Password hashing
- **CORS** – Cross-origin access control
- **Input Validation** – Robust data validation

### DevOps & Development

- **TypeScript Compiler** – Type-safe compilation
- **ts-node** – TS execution in development
- **nodemon** – Hot reload
- **Concurrently** – Parallel process execution

## 🎯 Technical Features

### 1. Advanced Chat System

- **Private Chats:** One-to-one with persistent history
- **Group Chat:** Multiple participants with custom avatars
- **Real Time:** Instant WebSocket communication
- **Message Status:** Delivery/read in real time
- **Participant Management:** Add/remove users

### 2. Forum System

- **Posts and Comments:** Full interaction system
- **Like System:** For posts and comments
- **Real-Time Updates:** Instant notifications
- **Content Moderation:** Admin controls

### 3. User Management

- **JWT Auth:** Stateless, secure system
- **Image Upload:** Profile photos and group avatars
- **Contact Info:** Email and phone
- **Roles:** Admins and regular users

### 4. File Upload & Management

- **File Validation:** Allowed types and sizes
- **Local Storage:** File system integration
- **Image Processing:** Automatic optimization

#### Upload Flow with Validation

```mermaid
%%{title: "Sistema de Upload com Validação e Processamento"}%%
sequenceDiagram
    participant U as User
    participant F as Frontend
    participant B as Backend
    participant FS as File System
    participant DB as SQLite
    
    Note over U,DB: Profile Image Upload
    
    U->>F: Selects profile image
    F->>B: POST /api/upload/profile (multipart/form-data)
    B->>B: Validate mimetype/size
    alt Invalid file
        B-->>F: 400 Bad Request
    else Valid file
        B->>FS: Save file locally
        FS-->>B: Path saved (e.g., uploads/profile/abc.png)
        B->>DB: UPDATE users SET avatarPath = ...
        DB-->>B: Avatar updated
        B-->>F: 200 OK (avatar URL)
    end
```

## 🔒 Reliability, Performance, and Monitoring

### Reliability

- **Atomic Operations:** Transactions via TypeORM
- **Error Handling:** Centralized middleware
- **Retries & Timeouts:** Socket reconnection strategies

### Performance

- **WebSockets:** Real-time, low-latency communication
- **Indexed Queries:** Optimized SQLite queries
- **Resource Optimization:** Lightweight stack (SQLite + Node)

### Monitoring

- **Logs:** Structured logging
- **Health Checks:** Basic readiness checks for API
- **Metrics (suggested):** Integrate with a lightweight metrics tool if needed

## 🧭 Product Flows & UX

### 1. Onboarding & Auth

- Login, token storage, automatic refresh, logout flow

### 2. Chat (Private/Group)

- Send/receive in real time, message status, room management

### 3. Forum

- Create/edit/delete posts, comments, likes, moderation

### 4. Profiles

- Edit profile, upload avatar, contact info

### 5. Notifications

- Real-time updates for new posts, likes, comments, messages

## 🚀 Build & Run (Suggested)

```bash
# Backend
npm install
npm run dev   # nodemon + ts-node

# Frontend
cd frontend
npm install
npm start     # Angular dev server
```

## 🛠️ Skills Demonstrated

- Full-stack TypeScript (Angular + Node/Express)
- WebSockets with Socket.IO
- JWT auth + refresh tokens
- File upload with validation/processing
- ORM (TypeORM) with migrations
- Reactive frontend (RxJS) and modern Angular

---

## Built with ❤️ for real-time, community-driven experiences
