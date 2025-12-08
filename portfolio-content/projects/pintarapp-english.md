# 🎨 PintarApp — SVG Coloring App for Android

## 🚀 Overview

**PintarApp** is an SVG coloring app built with React Native, designed to work 100% offline on Android. The codebase emphasizes clean separation, strong typing, and decoupled components, prepared for ads and a premium tier.

### 🎯 Value Proposition

- **SVG coloring** with touch interactions
- **Offline-first** experience
- **Clean architecture** with well-defined layers
- **TypeScript-first** codebase
- **Monetization-ready** (ads/premium)

## 🏗️ Tech Stack

### Mobile (React Native 0.76)

- TypeScript
- `react-native-svg` + transformer
- Safe Area Context
- Hooks + reducers for immutable state

### Architecture

- `@/*` alias for short imports (Babel/TS)
- Feature-based structure
- Clean Code and testability

## 📁 Structure

```text
src/
  app/            # composition root
  core/           # design system, utilities
  features/
    coloring/     # domain (components, hooks, state)
  types/          # global declarations (e.g., SVG)
assets/svgs/      # bundled vectors inside APK
```

## 🎯 Current Features

- **ColoringScreen**: header, painting surface, toolbox
- **SvgColoringSurface**: tap-to-fill, eraser, touch-friendly controls
- **ColorPalette**: horizontal swatches, visual selection, custom colors
- **Toolbox**: switch tools, reset drawing
- **State mgmt**: `useColoringSession` hook + pure reducer, ready for persistence

## 🚀 Install & Run

Prereqs: Node 18+, Android Studio/SDK, emulator or device.

```bash
npm install
npm start          # start Metro
npm run android    # install/run on device or emulator
# optional (macOS): npm run ios

npm run lint
npm run test
npm run typecheck
```

### Configure Android emulator as tablet

1. Open Android Studio → AVD Manager → create tablet device (API 33+).
2. Start emulator and run `npm run android`.

## 🔮 Next Steps

- AsyncStorage/SQLite persistence
- Import external SVGs + page library
- Advanced tools (zoom/pan, brush, eyedropper)
- Monetization (AdMob, premium)
- Sharing, gamification, achievements

## 🛠️ Skills Demonstrated

React Native, TypeScript, SVG manipulation, hooks/reducers, offline-first UX, feature-based architecture, strong typing.

---
Built with ❤️ for Android, with clean architecture and offline-first focus.
