# Traffic Manager Dashboard

![Angular](https://img.shields.io/badge/Angular-18.0.0-red.svg)
![TypeScript](https://img.shields.io/badge/TypeScript-5.4.2-blue.svg)
![RxJS](https://img.shields.io/badge/RxJS-7.8.0-purple.svg)

## A complete traffic monitoring and ticket management dashboard built with Angular

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit-brightgreen.svg)](https://your-demo-link.com)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black.svg)](https://github.com/your-username/traffic-manager)

---

## 📋 Overview

This project is a monitoring dashboard built during advanced Angular studies. The app showcases modern Angular 18 concepts, including standalone components, signals, advanced lifecycle hooks, and reusable component architecture to build real-time monitoring interfaces.

### ✨ Key Features

- **Server Monitoring:** Real-time status with automatic updates
- **Traffic Analysis:** Traffic data visualization with dynamic charts
- **Ticket System:** Full support ticket management
- **Modular Dashboard:** Interface organized in independent widgets
- **Reusable Components:** Architecture based on shared components

---

## 🚀 Tech Stack

### Frontend

- **Angular 18.0.0** - Main framework with standalone components
- **TypeScript 5.4.2** - Strongly typed language
- **RxJS 7.8.0** - Reactive programming with observables
- **Angular Forms** - Form management
- **Angular Signals** - Signal-based reactivity system

### Development Tooling

- **Angular CLI 18.0.0** - Command line tooling
- **Karma & Jasmine** - Testing framework
- **TypeScript Compiler** - Compilation and type checking

---

## 🏗️ Project Architecture

### Component Structure

```text
src/app/
├── app.component.*              # Root component
├── header/                      # App header
├── dashboard/                   # Main dashboard module
│   ├── dashboard-item/          # Wrapper component for widgets
│   ├── server-status/           # Server status monitoring
│   ├── traffic/                 # Traffic data visualization
│   └── tickets/                 # Ticket management system
│       ├── tickets.component.*  # Main ticket list
│       ├── ticket/              # Individual ticket component
│       ├── new-ticket/          # Ticket creation form
│       └── ticket.model.ts      # Ticket data model
└── shared/                      # Shared components
    ├── button/                  # Reusable button component
    └── control/                 # Form control component
```

### Data Models

#### Ticket Interface

```typescript
interface Ticket {
  id: string;
  title: string;
  request: string;
  status: 'open' | 'closed';
}
```

#### Traffic Data Interface

```typescript
interface TrafficData {
  id: string;
  value: number;
}
```

---

## 🔧 Detailed Features

### 1. Server Monitoring

- **Real-Time Status:** Automatic update every 5 seconds
- **Dynamic States:** Online, Offline, and Unknown with configurable probabilities
- **Angular Signals:** Signals for efficient reactivity
- **Lifecycle Management:** Interval cleanup with DestroyRef

### 2. Traffic Analysis

- **Data Visualization:** Dynamic bar chart
- **Simulated Data:** Demo dataset with realistic values
- **Automatic Calculation:** Dynamic max value for visual normalization
- **Responsive UI:** Adapts to different screen sizes

### 3. Ticket System

- **Ticket Creation:** Full form with validation
- **State Management:** Dynamic ticket list
- **Status Change:** Switch between open and closed
- **Event Handling:** Component communication via outputs

### 4. Modular Architecture

- **Dashboard Items:** Wrapper components for organization
- **Shared Components:** Reusable Button and Control
- **Standalone Components:** Modern architecture without NgModules
- **ViewChild and ViewChild.required:** DOM and child component access

---

## 🛠️ Installation & Run

### Prerequisites

- Node.js (version 18 or higher)
- npm or yarn
- Angular CLI

### Setup Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/traffic-manager.git
   cd traffic-manager
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

### Main Flow

1. **Main Dashboard:** View the three primary widgets
2. **Monitoring:** Server status updates automatically
3. **Traffic:** Real-time traffic chart
4. **Tickets:** Create and manage support tickets

### Screenshots

> Add app screenshots here

---

## 🎯 Angular Concepts Demonstrated

### Standalone Components

- **Independent Components:** Using standalone components without NgModules
- **Direct Imports:** Components imported directly in `imports`
- **Modern Architecture:** Recommended approach from Angular 17+

### Angular Signals

- **Modern Reactivity:** Signals for reactive state
- **Effect API:** Automatic reaction to state changes
- **Performance:** Optimized change detection

### Advanced Lifecycle Hooks

- **OnInit and AfterViewInit:** Initialization hooks
- **DestroyRef:** Modern cleanup management
- **ViewChild:** DOM and child component access

### Event Handling

- **Output API:** New outputs API
- **EventEmitter:** Component communication
- **Form Handling:** Template-driven forms

---

## 🔍 Technical Analysis

### Strengths

- ✅ **Modern Architecture:** Standalone components and signals
- ✅ **Componentization:** Small, focused components
- ✅ **Reusability:** Well-structured shared components
- ✅ **Lifecycle Management:** Proper resource cleanup
- ✅ **TypeScript:** Strong typing and clear interfaces
- ✅ **Performance:** Efficient reactivity with signals

### Future Improvements

- 🔄 **Backend Integration:** Connect to real monitoring APIs
- 🔄 **WebSocket:** Real-time communication
- 🔄 **Unit Tests:** Full coverage
- 🔄 **PWA:** Convert to a Progressive Web App
- 🔄 **State Management:** Add NgRx for complex state
- 🔄 **Charts Library:** Integrate a professional chart library

---

## 📚 Learnings

This project helped consolidate knowledge in:

- **Modern Angular:** Standalone components and signals
- **Lifecycle Hooks:** Advanced lifecycle management
- **Frontend Architecture:** Dashboard design patterns
- **Component Communication:** Event handling and outputs
- **Performance:** Optimization with signals and proper cleanup
- **Advanced TypeScript:** Interfaces and complex typing

---

## 🎨 Design & UX

### User Interface

- **Clean Design:** Minimalist, professional interface
- **Organized Widgets:** Responsive grid layout
- **Visual Feedback:** Clear states for different situations
- **Consistent Components:** Unified visual pattern

### Responsiveness

- **Mobile First:** Adaptive design for mobile devices
- **Grid Layout:** Flexible component organization
- **Typography:** Clear visual hierarchy

---

### Built with ❤️ using Angular

Project created during advanced Angular studies, demonstrating modern concepts and frontend best practices.
