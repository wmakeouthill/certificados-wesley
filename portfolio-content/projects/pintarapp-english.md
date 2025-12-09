# 🎨 PintarApp — SVG Painting App for Android

## 🚀 Overview

**PintarApp** is an SVG painting app built with React Native, designed to run 100% offline on Android. The focus is on a clean codebase from day one: well-separated layers, strong typing, and decoupled components. The app is prepared to evolve with ads and a premium version.

### 🎯 Value Proposition

- **SVG Painting:** Apply colors to SVG vectors
- **100% Offline:** Full functionality without connectivity
- **Clean Architecture:** Well-separated layers and decoupled components
- **TypeScript:** Strong typing across the codebase
- **Monetization-ready:** Base prepared for ads and premium tier

## 🏗️ Tech Stack

### Mobile (React Native)

- **React Native 0.76** – Cross-platform mobile framework
- **TypeScript** – Static typing for safer development
- **react-native-svg** – SVG rendering and manipulation
- **react-native-svg-transformer** – SVG vector loading
- **Safe Area Context** – Safe area handling
- **Hooks and Reducers** – Immutable state management

### Architecture

- **`@/*` alias** – Short imports configured in Babel/TS
- **Feature-based Structure** – Organized by feature
- **Clean Code** – Separation of concerns
- **Testability** – Decoupled components

## 📁 Project Structure

```text
src/
  app/            # Composition root (App, providers)
  core/           # Design system and generic utilities
  features/
    coloring/     # Painting domain (components, hooks, state)
  types/          # Global declarations (e.g., SVG)
assets/svgs/      # Local vectors bundled in the APK
```

Each feature keeps its own data, models, hooks, components, and reducers to favor cohesion and testability.

## 🎯 Current Features

### 1. Painting Screen (`ColoringScreen`)

- **Header:** Navigation interface
- **Painting Screen:** Main work area
- **Toolbox:** Painting tools

### 2. SVG Painting Surface (`SvgColoringSurface`)

- **Color Application:** Via `Path.onPress`
- **Fill Tool:** Bucket fill simulation
- **Eraser Tool:** Remove colors
- **Touch Interaction:** Controls optimized for touch

### 3. Color Palette (`ColorPalette`)

- **Horizontal List:** Color swatches
- **Visual Selection:** Intuitive interface
- **Custom Colors:** Support for custom palettes

### 4. Toolbox

- **Tool Switching:** Fill and erase
- **Reset Drawing:** Full clear
- **Intuitive Controls:** Touch-friendly UI

### 5. State Management

- **`useColoringSession` hook:** Session-scoped state
- **Pure Reducer (`coloringReducer`):** Immutable state logic
- **Local Persistence:** Prepared for AsyncStorage/SQLite

## 🚀 Installation & Run

### Prerequisites

- **Node 18+** — JavaScript runtime
- **Android Studio + SDKs** — Android environment configured
- **Android Emulator or Device** — To run the app

### Installation

```bash
npm install
```

### Run

```bash
# Start Metro bundler
npm start

# In another terminal, install/run on device or emulator
npm run android

# Optional: run on iOS (macOS)
npm run ios
```

### Code Quality

```bash
npm run lint       # Lint check
npm run test       # Run tests
npm run typecheck  # TypeScript type checking
```

### Configure Android Emulator as Tablet

The app is configured in `AndroidManifest.xml` to support tablets with large screens (`largeScreens` and `xlargeScreens`). To create a tablet emulator:

1. Open Android Studio
2. Go to AVD Manager
3. Create a new virtual device in **Tablets**
4. Choose a system image (API 33+ recommended)
5. Start the emulator and run `npm run android`

## 🔮 Next Steps Suggested

### Future Features

- **Local Persistence:** AsyncStorage/SQLite to save sessions
- **SVG Import:** Import external SVGs and build a page library
- **Advanced Tools:** Zoom/pan, brush, eyedropper
- **Monetization:** AdMob integration and premium no-ads version

### Product Evolution

- **Page Library:** Collection of SVGs to color
- **Sharing:** Export and share artwork
- **Gamification:** Achievements and challenges
- **Premium Version:** Remove ads and add exclusive features

## 🛠️ Technical Skills Demonstrated

### Mobile Development

- **React Native 0.76** – Modern mobile framework
- **TypeScript** – Static typing
- **SVG Manipulation** – Rendering and interaction with vectors
- **State Management** – Hooks and reducers for immutable state

### Architecture & Design

- **Feature-based Architecture** – Domain organization
- **Clean Code** – Separation of responsibilities
- **Component Design** – Decoupled, reusable components
- **Type Safety** – TypeScript throughout the code

### Mobile UX

- **Touch Interactions** – Optimized for touch
- **Offline-first** – Works without connectivity
- **Tablet Support** – Large-screen support
- **Performance** – Optimized for mobile devices

## 📝 Conclusion

**PintarApp** showcases mobile development skills with React Native, focusing on clean architecture, strong typing, and an optimized user experience for Android. The foundation is ready to evolve while maintaining Clean Code and separation of concerns.

---

## Built with ❤️

SVG painting app for Android, focused on clean architecture and offline-first experience.
