# D&D Spell Cards

Printable D&D 5e spell cards — a single-page static HTML app with no build system or dependencies. Open `spells.html` directly in a browser to view and print.

Cards are sized to standard poker card dimensions (63mm x 88mm) and print on A4 sheets.

## Generating Spell Images

This project includes a Claude Code skill (`.claude/skills/generate-image/`) for generating spell illustrations via the OpenAI DALL-E API.

**Requirements:** Set the `OPENAI_API_KEY` environment variable.

**Usage:** Ask Claude Code to generate a spell image — it will craft a style-appropriate prompt based on the spell's class (paladin/warlock/wizard) and save the result to `img/`.

## TODO

- [ ] Change template for warlock and wizard spells
- [ ] Improve card text readability
