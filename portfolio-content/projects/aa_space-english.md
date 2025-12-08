# 🌌 AA Space — Real-Time Community Platform

## 🚀 Overview

**AA Space** is a complete community and real-time communication platform built with a modern full-stack architecture. The solution provides a safe environment to share experiences, with an advanced chat system, interactive forum, and user management— all integrated into a responsive web experience.

### 🎯 Key Features

- **Complete Chat System:** Private and group conversations with advanced control
- **Interactive Forum:** Posts, comments, and like system
- **User Management:** Customizable profiles with image uploads
- **Real-Time Communication:** Via WebSockets with Socket.IO
- **Modern Interface:** Responsive design with Angular 19
- **Robust Backend:** RESTful API with Node.js and Express

## 🏗️ System Architecture

```mermaid
%%{title: "AA_Space General Architecture"}%%
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
%%{title: "Real-Time Chat with WebSockets"}%%
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
%%{title: "Forum Flow with Interactions"}%%
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
    WS->>F: Everyone sees comment instantly
```

## 🔐 Authentication and Sessions

### JWT Flow with Refresh Tokens

```mermaid
%%{title: "JWT Authentication System with Refresh Tokens"}%%
sequenceDiagram
    participant U as User
    participant F as Frontend
    participant B as Backend
    participant DB as SQLite
    
    Note over U,DB: Initial Login
    
    U->>F: Enters credentials
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

- **Angular 19** - Enterprise framework with TypeScript 5.7
- **RxJS 7.8** - Reactive programming
- **Socket.IO Client** - WebSocket communication
- **CSS3** - Responsive, modern interface

### Backend

- **Node.js** - Server-side JavaScript runtime
- **Express.js 4.18** - Web framework
- **TypeScript 5.8** - Static typing
- **Socket.IO 4.8** - WebSocket server

### Database

- **SQLite3** - Embedded relational database
- **TypeORM 0.3.22** - Modern ORM with TypeScript
- **Migrations** - Schema version control

### Security & Authentication

- **JWT** - Secure tokens for authentication
- **bcrypt** - Password hashing
- **CORS** - Cross-origin access control
- **Input Validation** - Robust data validation

### DevOps & Development

- **TypeScript Compiler** - Type-safe compilation
- **ts-node** - TypeScript execution in development
- **nodemon** - Hot reload
- **Concurrently** - Parallel process execution

## 🎯 Technical Features

### 1. Advanced Chat System

- **Private Conversations:** One-to-one with persistent history
- **Group Chat:** Multiple participants with customizable avatars
- **Real Time:** Instant communication via WebSockets
- **Message Status:** Delivery and read receipts in real time
- **Participant Management:** Add/remove users

### 2. Forum System

- **Posts and Comments:** Complete interaction system
- **Like System:** For posts and comments
- **Real-Time Updates:** Instant notifications
- **Content Moderation:** Administrative control

### 3. User Management

- **JWT Authentication:** Secure stateless system
- **Image Upload:** Profile pictures and group avatars
- **Contact Information:** Email and phone
- **Role System:** Admins and regular users

### 4. File Upload and Management

- **File Validation:** Allowed types and sizes
- **Local Storage:** Integration with file system
- **Image Processing:** Automatic optimization

#### Upload Flow with Validation

```mermaid
%%{title: "Upload System with Validation and Processing"}%%
sequenceDiagram
    participant U as User
    participant F as Frontend
    participant B as Backend
    participant FS as File System
    participant DB as SQLite
    
    Note over U,DB: Profile Image Upload
    
    U->>F: Selects image file
    F->>F: Client-side validation (type, size)
    F->>B: POST /api/upload/profile-image (multipart/form-data)
    B->>B: Validation middleware
    alt Valid file
        B->>FS: Save temporary file
        FS-->>B: File saved
        B->>B: Process image (resize, optimize)
        B->>FS: Save optimized version
        FS-->>B: Processed image saved
        B->>DB: UPDATE user SET profile_image = filename
        DB-->>B: Database updated
        B-->>F: {success: true, imageUrl: '/uploads/profile_123.jpg'}
        F->>F: Update interface with new image
    else Invalid file
        B-->>F: {error: 'File type not allowed'}
        F->>U: Show validation error
    end
    
    Note over U,DB: Group Avatar Upload
    
    U->>F: Selects group avatar
    F->>B: POST /api/upload/group-avatar
    B->>FS: Save group avatar
    FS-->>B: Avatar saved
    B->>DB: UPDATE groups SET avatar = filename
    DB-->>B: Group updated
    B->>B: Broadcast to group members
    B-->>F: Avatar updated
    F->>F: Update group interface
```

## 🔧 Technical Implementations

### WebSocket Communication

```typescript
// Socket.IO server
io.on('connection', (socket) => {
  socket.on('join_room', (roomId) => {
    socket.join(roomId);
  });
  
  socket.on('send_message', (data) => {
    io.to(data.roomId).emit('new_message', data);
  });
});
```

### TypeORM Entities

```typescript
@Entity()
export class User {
  @PrimaryGeneratedColumn()
  id: number;
  
  @Column({ unique: true })
  username: string;
  
  @OneToMany(() => ChatMessage, message => message.sender)
  messages: ChatMessage[];
}
```

### JWT Authentication

```typescript
// Authentication middleware
const authenticateToken = (req, res, next) => {
  const token = req.headers['authorization'];
  if (!token) return res.sendStatus(401);
  
  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) return res.sendStatus(403);
    req.user = user;
    next();
  });
};
```

## 📊 Technical Differentials

### Implemented Innovations

1. **Hybrid chat system** with private and group conversations
2. **WebSocket integration** for real-time communication
3. **Full TypeScript architecture** with static typing
4. **Upload system** with security validation
5. **Responsive interface** adaptable to all devices

### Skills Demonstrated

- **Full-stack Development** with Angular and Node.js
- **Real-time Communication** with WebSockets
- **TypeScript** on frontend and backend
- **Modern ORM** with TypeORM
- **Secure Authentication** with JWT
- **Component Architecture** with Angular
- **Reactive Programming** with RxJS
- **Database Versioning** control

## 🚀 Final Result

**AA Space** demonstrates advanced capability in:

- **Modern Full-stack Development**
- **Real-Time Communication** with WebSockets
- **TypeScript Architecture** with type safety
- **Complex Chat Systems**
- **User Management** and authentication
- **Responsive and modern Interface**

A complete solution that brings together modern market technologies to create a robust and scalable community experience.
