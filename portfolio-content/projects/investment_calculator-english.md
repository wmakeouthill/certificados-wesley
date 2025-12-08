# Investment Calculator

![Angular](https://img.shields.io/badge/Angular-18.0.0-red.svg)
![TypeScript](https://img.shields.io/badge/TypeScript-5.4.2-blue.svg)
![RxJS](https://img.shields.io/badge/RxJS-7.8.0-purple.svg)

## A full compound-interest calculator built with Angular

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit-brightgreen.svg)](https://your-demo-link.com)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black.svg)](https://github.com/your-username/investment-calculator)

---

## 📋 Overview

Built during Maximilian Schwarzmüller's Angular course (Udemy). Demonstrates signals, computed properties, reactive services, and template-driven forms to project investments over time.

### ✨ Features

- **Investment projection** with compound interest
- **Simple input UI** for initial/annual deposits, expected return, duration
- **Detailed yearly table**: investment, interest, total capital
- **Currency formatting** (BRL in the sample)
- **Reactive architecture** using Angular Signals
- **Modern UI** with gradient and polished typography

---

## 🚀 Tech

### Frontend

- Angular 18.0.0
- TypeScript 5.4.2
- RxJS 7.8.0
- Angular Forms + Signals

### Dev Tooling

- Angular CLI 18.0.0
- Karma & Jasmine
- TypeScript compiler

---

## 🏗️ Architecture

```text
src/app/
├── app.component.*
├── header/
│   └── header.component.*
├── user-input/
│   └── user-input.component.*
├── investment-results/
│   └── investment-results.component.*
├── investment.service.ts
└── investment-input.model.ts
```

### Data Models

```typescript
export interface InvestmentInput {
  initialInvestment: number;
  duration: number;
  expectedReturn: number;
  annualInvestment: number;
}

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

## 🔧 Details

### Input System

- Initial investment, annual contribution, expected return (%), duration (years)
- Numeric validation with sensible defaults

### Financial Calculations

- Compound interest per year
- Annual projection with total invested, interest, final value
- Total interest and capital tracking

### UI

- Professional dark gradient theme
- Responsive form layout
- Result table with currency formatting
- Empty state messaging

---

## 🛠️ Install & Run

Prereqs: Node 18+, npm/yarn, Angular CLI

```bash
git clone https://github.com/your-username/investment-calculator.git
cd investment-calculator
npm install
npm start   # http://localhost:4200
```

Scripts:

```bash
npm start
npm run build
npm test
npm run watch
```

---

## 📱 Demo Flow

1) Fill the form with investment params
2) Submit to compute projections
3) View year-by-year table
4) Reset and try new scenarios

Example:

- Initial: R$ 10,000
- Annual: R$ 5,000
- Return: 8%/year
- Duration: 10 years
→ Final ≈ R$ 95,000 with ~R$ 35,000 interest.

---

## 🎯 Angular Concepts

- Signals + computed properties
- Standalone components
- Service-centered business logic
- Template-driven forms with `[(ngModel)]`
- Modern control flow (`@if`, `@for`)

---

## 📚 Learnings

Modern Angular reactivity (Signals), clean separation of business logic in services, and financial math with TypeScript. Built with ❤️ using Angular.
