# Task Management System

![Angular](https://img.shields.io/badge/Angular-19.1.0-red.svg)
![TypeScript](https://img.shields.io/badge/TypeScript-5.7.2-blue.svg)
![RxJS](https://img.shields.io/badge/RxJS-7.8.0-purple.svg)

## A complete task manager built with Angular

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit-brightgreen.svg)](https://your-demo-link.com)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black.svg)](https://github.com/your-username/first-angular-app)

---

## 📋 Overview

Project created during Maximilian Schwarzmüller's Angular course (Udemy). It showcases core Angular concepts: components, services, reactive forms, routing, and state handling.

### ✨ Features

- **User selection**: Switch between users with an intuitive UI
- **Task CRUD**: Create, view, delete custom tasks
- **Local persistence**: Automatic storage via browser localStorage
- **Responsive UI**: Modern design for multiple screen sizes
- **Componentization**: Modular, reusable components

---

## 🚀 Tech

### Frontend

- Angular 19.1.0
- TypeScript 5.7.2
- RxJS 7.8.0
- Angular Forms & Router

### Dev Tooling

- Angular CLI 19.1.7
- Karma & Jasmine
- TypeScript compiler

---

## 🏗️ Project Architecture

### Component Structure

```text
src/app/
├── app.component.*
├── header/
├── user/
├── tasks/
│   ├── tasks.component.*
│   ├── task/
│   ├── new-task/
│   └── tasks.service.ts
├── shared/
│   └── card/
└── dummy-users.ts
```

### Data Models

```typescript
interface User {
  id: string;
  avatar: string;
  name: string;
}

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

### 1. Users

- Visual selection with avatar + name
- Active user highlight
- Mocked user base for demo

### 2. Tasks

- Create tasks with a full form
- List tasks for the selected user
- Mark/remove tasks
- Persist to localStorage

### 3. UI/UX

- Modern, intuitive design
- Reusable cards
- Responsive layout
- Loading/interaction feedback

---

## 🛠️ Install & Run

### Prereqs

- Node.js 18+
- npm or yarn
- Angular CLI

### Steps

1) Clone

```bash
git clone https://github.com/your-username/first-angular-app.git
cd first-angular-app
```

2) Install

```bash
npm install
```

3) Dev server

```bash
npm start
# http://localhost:4200
```

### Scripts

```bash
npm start        # dev server
npm run build    # production build
npm test         # unit tests
npm run watch    # build watch
```

---

## 📱 Demo Flow

1) Landing: list of users
2) Pick a user to see their tasks
3) Add/view/remove tasks
4) Data persists across sessions

---

## 🎯 Angular Concepts

- Standalone components
- Template syntax, new control flow (`@if`, `@for`)
- Services + `inject()` DI
- Template-driven forms & validation
- Local state + shared service state

---

## 🔍 Technical Notes

**Strengths**: clear architecture, strong typing, reusable components, local persistence, responsive UI.  
**Next**: real backend integration, auth, fuller tests, PWA, NgRx for complex state.

---

## 📚 Learnings

Consolidated fundamentals of Angular, TypeScript, frontend architecture, responsive design, and state patterns. Built with ❤️ using Angular.
