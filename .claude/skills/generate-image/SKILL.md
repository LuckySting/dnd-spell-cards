---
name: generate-image
description: Generates an image using OpenAI DALL-E API from a text prompt. WHEN TO USE IT: if user asks to generate, create, or make an image, picture, illustration, or photo.
---

## The Goal

A skill that generates an image via the OpenAI DALL-E API using a text prompt and saves it to the `images` subfolder.

## Known Constants

- **Script location**: `.claude/skills/generate-image/generate`
- **API endpoint**: `https://api.openai.com/v1/images/generations`
- **Default model**: `dall-e-3`
- **Default quality**: `standard`
- **Default size**: `1024x1024`
- **Available qualities**: `standard`, `hd`
- **Available sizes** (dall-e-3): `1024x1024`, `1792x1024`, `1024x1792`

## The Process

1. **Gather context and understand the subject**
   - Before generating a prompt, research the subject the user is asking about.
   - If it's a game mechanic (D&D spell, item, ability), look up what it actually does — its visual effects, lore, and flavor text — to inform a richer prompt.
   - If it's a real-world subject, consider its key visual characteristics.
   - If the user provided reference images or links, examine them.
   - Use web search, file reads, or conversation context as needed to gather this information.

2. **Craft a detailed image generation prompt**
   - Based on the gathered context, write a detailed, visually descriptive prompt optimized for image generation.
   - Include: subject, action/pose, lighting, color palette, atmosphere, background, composition, and art style cues.
   - Present the crafted prompt to the user for confirmation before generating.

3. **Determine quality and size**
   - If the user mentions a specific quality (e.g. "high quality", "HD"), use `--quality hd`.
   - If the user mentions a specific size or aspect ratio, map it to the appropriate `--size` value.
   - Otherwise, use defaults (`standard` quality, `1024x1024` size).

4. **Run the script**
   - Execute: `bash .claude/skills/generate-image/generate "<prompt>" "<filename>" --quality <quality> --size <size>`
   - The `filename` should be a descriptive snake_case name (e.g. `burning_hands`, `fireball_spell`). The `.png` extension is added automatically.

5. **Report the result**
   - Show the returned file path and display the image to the user.
   - On failure, show the error and suggest fixes.

## Rules

1. Always gather context about the subject before crafting the prompt — don't just pass the user's message verbatim.
2. Present the crafted prompt to the user before generating, so they can adjust it.
3. Use the bash wrapper `.claude/skills/generate-image/generate` to run the script (not `python3 generate.py` directly).
4. Output images are saved to the project's `img/` directory.
5. If the user asks for multiple images, run the script multiple times (sequentially, not in parallel) to avoid timestamp collisions.

## Progressive updates

Whenever user defines a clear thing not to do anymore, automatically update the Rules section in this SKILL.md file.
