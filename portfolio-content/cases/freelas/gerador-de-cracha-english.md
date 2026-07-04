---
title: Batch badge generator
client: Supermercados Rio Sul
category: freela
status: Delivered
stack: [Python, PyInstaller]
order: 7
---
# Case — Badge Generator (Supermercados Rio Sul)

**Type:** Freelance (client: Supermercados Rio Sul)
**Role:** Developer (full authorship)
**Status:** Delivered and in use
**Stack:** Python (Pillow), local HTTP preview server, PyInstaller (.exe distribution), HTML/JS (interactive preview)

## Context and problem

The supermarket's HR department generated employee badges manually in a graphics editor: positioning photo, name and role one by one, with inconsistent results and hours spent on each batch of new hires.

## Solution

A batch badge-generation tool: HR drops the photos into a folder, adjusts positions once in an **interactive browser preview** (a local server that renders the layout in real time and saves the coordinates to `positions.json`) and generates all standardized badges at once.

## Technical decisions

- **Distributed as a Windows executable (PyInstaller)** with a build script (`criar_exe.bat`) — the client doesn't need Python installed; I also included a "how to use without Python" guide
- **Visual configuration, not code**: an HTML preview with position adjustments persisted to JSON — HR calibrates the template on their own whenever the badge layout changes
- **Batch processing with Pillow**: photos normalized and composited onto the template with consistent typography

## Results and impact

- Badge generation went from a manual per-employee task to batch processing of an entire folder
- A self-sufficient tool for non-technical users: no installation, no dependencies, visual calibration

## Interview highlights (STAR summary)

- **S/T:** HR spent hours assembling badges one by one in a graphics editor. **A:** I delivered a Python tool packaged as an .exe with an interactive browser preview for calibrating the layout and batch generation. **R:** the process reduced to "drop photos in the folder and click", operable by a user with no technical knowledge.
