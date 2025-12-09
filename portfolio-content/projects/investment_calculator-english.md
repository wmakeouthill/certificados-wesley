# Investment Calculator

![Angular](https://img.shields.io/badge/Angular-18.0.0-red.svg)
![TypeScript](https://img.shields.io/badge/TypeScript-5.4.2-blue.svg)
![RxJS](https://img.shields.io/badge/RxJS-7.8.0-purple.svg)

## A complete investment calculator built with Angular

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit-brightgreen.svg)](https://your-demo-link.com)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black.svg)](https://github.com/your-username/investment-calculator)

---

## 📋 Overview

This project is an investment calculator built during Maximilian Schwarzmüller’s Angular course (Udemy). It demonstrates advanced Angular concepts, including signals, computed properties, reactive services, and template-driven forms. The tool calculates investment projections based on initial and annual deposits, expected return rate, and investment duration.

### ✨ Key Features

- **Investment Calculation:** Full compound-interest projection
- **Intuitive UI:** Simple, straightforward data entry form
- **Detailed Results:** Year-by-year table with invested amounts, interest, and total capital
- **Currency Formatting:** Values displayed in BRL currency format
- **Reactive Architecture:** Signals for reactive state management
- **Modern Design:** Elegant gradient interface with professional typography

---

## 🚀 Tech Stack

### Frontend

- **Angular 18.0.0** – Main framework
- **TypeScript 5.4.2** – Programming language
- **RxJS 7.8.0** – Reactive programming
- **Angular Forms** – Form handling
- **Angular Signals** – Reactive signals system

### Development Tooling

- **Angular CLI 18.0.0** – Command-line tools
- **Karma & Jasmine** – Testing framework
- **TypeScript Compiler** – Compilation and type checking

---

## 🏗️ Project Architecture

### Component Structure

```text
src/app/
├── app.component.*              # Root component
├── header/                      # Header with logo/title
│   ├── header.component.*       # Header component
├── user-input/                  # Input form
│   ├── user-input.component.*   # User input component
├── investment-results/          # Results display
│   ├── investment-results.component.* # Results component
├── investment.service.ts        # Calculation service
└── investment-input.model.ts    # Input data interface
```

### Data Models

#### InvestmentInput Interface

```typescript
export interface InvestmentInput {
  initialInvestment: number;
  duration: number;
  expectedReturn: number;
  annualInvestment: number;
}
```

#### Investment Result

```typescript
interface InvestmentResult {
  year: number;
  totalAmountInvested: number;
  interest: number;
  valueEndOfYear: number;
  annualInvestment: number;
  totalInterest: number;
}
```

---

## 🔧 Detailed Features

### 1. Input System

- **Initial Investment:** Starting amount
- **Annual Investment:** Extra amount invested each year
- **Expected Return:** Annual return rate (%)
- **Duration:** Years to calculate
- **Validation:** Numeric fields with sensible defaults

### 2. Financial Calculations

- **Compound Interest:** Correct compound calculations
- **Annual Projection:** Detailed year-by-year results
- **Capital Invested:** Total money invested over time
- **Total Interest:** Accumulated interest
- **Final Value:** Total investment value at the end

### 3. User Interface

- **Professional Design:** Dark gradient with elegant typography
- **Responsive Form:** Grouped inputs, clean layout
- **Results Table:** Clear display of calculated data
- **Currency Formatting:** Values in Brazilian Real (BRL)
- **Visual Feedback:** Message when there is no data to show

---

## 🛠️ Installation & Run

### Prerequisites

- Node.js (18 or higher)
- npm or yarn
- Angular CLI

### Setup Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/investment-calculator.git
   cd investment-calculator
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

1. **Landing:** Form with input fields
2. **Fill:** User enters investment values and parameters
3. **Calculate:** System processes data and computes projections
4. **Results:** Detailed year-by-year table
5. **Reset:** Form is cleared for new calculations

### Usage Example

- **Initial Investment:** R$ 10,000  
- **Annual Investment:** R$ 5,000  
- **Expected Return:** 8% per year  
- **Duration:** 10 years  

**Result:** Final value of ~R$ 95,000 with ~R$ 35,000 total interest.

---

## 🎯 Angular Concepts Demonstrated

### Signals and Reactivity

- **Angular Signals:** Modern reactive state system
- **Computed Properties:** Automatically calculated properties
- **Signal Updates:** Reactive state updates

### Services and Business Logic

- **InvestmentService:** Centralized calculations
- **Dependency Injection:** `inject()` and service pattern
- **Separation of Concerns:** UI-free business logic

### Template-driven Forms

- **Input Binding:** Template-driven forms with `[(ngModel)]`
- **Validation:** Required fields and sensible defaults
- **Form Events:** Submit and reset handling

### UI & UX

- **Professional Gradient:** Dark theme with good contrast
- **Responsive Layout:** Organized form and results table
- **Feedback:** Empty state messaging and clean typography

---

## 🔍 Technical Analysis

### Strengths

- ✅ **Clean Architecture:** Clear separation of concerns
- ✅ **Reactivity:** Signals and computed properties
- ✅ **Type Safety:** Strong typing with TypeScript
- ✅ **User Experience:** Professional UI and responsive layout
- ✅ **Persistence-ready:** Clear models for potential backend integration

### Future Improvements

- 🔄 **Backend Integration:** REST API for saving scenarios
- 🔄 **Authentication:** User accounts and saved profiles
- 🔄 **Unit Tests:** Broader test coverage
- 🔄 **PWA:** Turn into a Progressive Web App
- 🔄 **State Management:** NgRx for more complex flows

---

## 📚 Learnings

This project helped consolidate:

- **Angular Reactivity:** Signals and computed properties
- **TypeScript:** Strong typing and interfaces
- **Frontend Architecture:** Separation of concerns
- **Responsive Design:** Modern CSS and adaptive layouts
- **State Management:** Patterns for client-side data

---

### Built with ❤️ using Angular

Project created during the course “Angular - The Complete Guide” by Maximilian Schwarzmüller.
