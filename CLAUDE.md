# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Printable D&D 5e spell cards — a single-page static HTML app (`spells.html`) with no build system or dependencies. Open `spells.html` directly in a browser to view/develop.

## Architecture

- **spells.html** — the entire application: CSS, HTML, and JavaScript in one file
  - Spell data is a JS array of objects (`spells`), each with `name`, `level`, `school`, `castTime`, `range`, `components`, `duration`, `cls` (class), and `desc` (HTML)
  - Cards are generated at runtime from this array and inserted into `#cards`
  - Three character classes supported: `paladin`, `warlock`, `wizard` — each with a class-specific card frame image and name color
- **templates/** — card frame background images (`frame_paladin.png`, `frame_warlock.png`, `frame_wizard.png`)
- **img/** — spell illustration assets

## Key Design Details

- Cards are sized to standard poker card dimensions (63mm x 88mm) for printing
- Print layout uses `@media print` to hide UI controls and arrange cards on A4 sheets
- Font sizes use `clamp()` for responsive scaling between screen and print
- Class filtering is done client-side by toggling `.hidden` on card elements
