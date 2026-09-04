# ConvertX

Convert Anything. Understand Everything.

A frontend-only universal conversion and utility platform built with HTML5, modern ES modules, Tailwind CSS, browser APIs, LocalStorage, and a service worker.

## Run
Use a local static server (required for ES modules and service workers):

```bash
python -m http.server 5500
```

Open `http://localhost:5500/`.

## Architecture
UI pages call reusable modules for conversion, parsing, storage, formatting, sharing, search, theme, and tools. Unit definitions live in `data/unit-definitions.js`; adding a unit does not require changing the conversion engine.

## Features
- Universal converter with aliases, precision, details, copy, share and URL state
- Multi-unit converter and comparison
- Deterministic natural-language smart converter
- Safe expression calculator and unit-aware arithmetic
- Favorites/history/search/command palette/settings
- JSON, Base64, URL, timestamp, number-base, color, percentage, date and timezone tools
- Local-only data storage
- PWA manifest and versioned service worker
- Responsive accessible UI

## Adding a unit
Add a unit definition to the relevant category in `data/unit-definitions.js`. For linear units use `toBase`/`fromBase`; for offset units such as temperature use explicit functions.

## Keyboard shortcuts
- Ctrl/Cmd+K command palette
- Ctrl/Cmd+Shift+S swap units on converter pages
- Ctrl/Cmd+H history
- Ctrl/Cmd+D theme toggle
- Escape closes dialogs

## Privacy
Conversion values, history, favorites and settings stay in the browser. ConvertX has no backend.

## Security
No `eval()` or dynamic code execution is used. Imported data and URL parameters are validated before use.
