# Task Management System

![Angular](https://img.shields.io/badge/Angular-19.1.0-red.svg)
![TypeScript](https://img.shields.io/badge/TypeScript-5.7.2-blue.svg)
![RxJS](https://img.shields.io/badge/RxJS-7.8.0-purple.svg)

## A complete task manager built with Angular

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit-brightgreen.svg)](https://your-demo-link.com)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black.svg)](https://github.com/your-username/first-angular-app)

---

## 📋 Overview

This project is a task management system built during Maximilian Schwarzmüller’s Angular course on Udemy. It showcases core Angular fundamentals: components, services, reactive forms, routing, and state handling.

### ✨ Key Features

- **User Selection:** Intuitive UI to switch between users
- **Task Management:** Create, view, and remove custom tasks
- **Local Persistence:** Data automatically stored in browser localStorage
- **Responsive UI:** Modern design adaptable to different devices
- **Componentization:** Modular architecture with reusable components

---

## 🚀 Tech Stack

### Frontend

- **Angular 19.1.0** – Main framework
- **TypeScript 5.7.2** – Programming language
- **RxJS 7.8.0** – Reactive programming
- **Angular Forms** – Form handling
- **Angular Router** – Navigation between components

### Development Tooling

- **Angular CLI 19.1.7** – Command-line tools
- **Karma & Jasmine** – Testing framework
- **TypeScript Compiler** – Compilation and type checking

---

## 🏗️ Project Architecture

### Component Structure

```text
src/app/
├── app.component.*          # Root component
├── header/                  # App header
├── user/                    # User selection component
├── tasks/                   # Task management module
│   ├── tasks.component.*    # Main task list
│   ├── task/                # Individual task component
│   ├── new-task/            # Task creation form
│   └── tasks.service.ts     # Data service
├── shared/                  # Shared components
│   └── card/                # Reusable card component
└── dummy-users.ts           # Mock user data
```

### Data Models

#### User Interface

```typescript
interface User {
  id: string;
  avatar: string;
  name: string;
}
```

#### Task Interface

```typescript
interface Task {
  id: string;
  userId: string;
  title: string;
  summary: string;
  dueDate: string;
}
```

---

## 🔧 Detailed Functionality

### 1. User System

- **Visual Selection:** Interface with user avatars and names
- **Active State:** Visual highlight of the selected user
- **Mock Data:** Predefined user base for demo

### 2. Task Management

- **Creation:** Full form to add tasks
- **Viewing:** Organized list for the selected user
- **Removal:** Mark tasks as done/remove
- **Persistence:** Auto-save to localStorage

### 3. User Interface

- **Modern Design:** Clean, intuitive UI
- **Reusable Components:** Standardized task cards
- **Responsiveness:** Adapts to different screen sizes
- **Visual Feedback:** Loading/interaction states

---

## 🛠️ Installation & Run

### Prerequisites

- Node.js (18 or higher)
- npm or yarn
- Angular CLI

### Installation Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/first-angular-app.git
   cd first-angular-app
   ```

2. **Install dependencies**

   ```bash
   npm install
   ```

3. **Run the development server**

   ```bash
   npm start
   ```

4. **Access the app**

   ```text
   http://localhost:4200
   ```

### Available Scripts

```bash
# Development server
npm start

# Production build
npm run build

# Run tests
npm test

# Build with watch mode
npm run watch
```

---

## 📱 Demo

### Main App Flow

1. **Landing:** List of available users
2. **Selection:** Click a user to view their tasks
3. **Management:** Add, view, or remove tasks
4. **Persistence:** Data kept across sessions

### Screenshots

> Add app screenshots here

---

## 🎯 Angular Concepts Demonstrated

### Components and Templates

- **Standalone Components:** Using independent components
- **Template Syntax:** Interpolation, property binding, event binding
- **Control Flow:** New `@if`, `@for` syntax (Angular 17+)

### Services and Dependency Injection

- **TasksService:** Centralized data service
- **Dependency Injection:** Using the `inject()` function
- **Singleton Pattern:** Service available app-wide

### Forms

- **Template-driven Forms:** Template-based forms
- **Two-way Data Binding:** Bidirectional data sync
- **Form Validation:** Basic field validation

### State Management

- **Local State:** State managed in components
- **Service State:** Shared state via services
- **LocalStorage:** Client-side persistence

---

## 🔍 Technical Analysis

### Strengths

- ✅ **Clean Architecture:** Clear separation of concerns
- ✅ **Componentization:** Small, focused components
- ✅ **TypeScript:** Strong typing and well-defined interfaces
- ✅ **Reusability:** Shared components (Card)
- ✅ **Persistence:** Data kept between sessions

### Future Improvements

- 🔄 **Backend Integration:** Connect to a REST API
- 🔄 **Authentication:** Login and authorization
- 🔄 **Unit Tests:** Full test coverage
- 🔄 **PWA:** Turn into a Progressive Web App
- 🔄 **State Management:** Add NgRx for complex state

---

## 📚 Learnings

This project was key to consolidating knowledge in:

- **Angular Fundamentals:** Components, services, dependency injection
- **TypeScript:** Interfaces, types, OOP
- **Frontend Architecture:** Design patterns and code organization
- **Responsive Development:** Modern CSS and adaptive layouts
- **State Management:** Patterns for data sharing

---

### Built with ❤️ using Angular

Project created during the course “Angular - The Complete Guide” by Maximilian Schwarzmüller.
