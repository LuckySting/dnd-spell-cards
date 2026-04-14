#!/usr/bin/env python3
"""CLI tool to generate images via OpenAI DALL-E API."""

import argparse
import base64
import json
import os
import ssl
import sys
from pathlib import Path
import urllib.request


API_URL = "https://api.openai.com/v1/images/generations"
DEFAULT_MODEL = "dall-e-3"
DEFAULT_QUALITY = "standard"
IMAGES_DIR = Path(__file__).parents[3] / "img"


def generate_image(prompt: str, filename: str, *, model: str = DEFAULT_MODEL, quality: str = DEFAULT_QUALITY, size: str = "1024x1024") -> str:
    """Call OpenAI DALL-E API and save the generated image. Returns the file path."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    IMAGES_DIR.mkdir(exist_ok=True)

    payload = json.dumps({
        "model": model,
        "prompt": prompt,
        "quality": quality,
        "size": size,
        "response_format": "b64_json",
        "n": 1,
    }).encode()

    req = urllib.request.Request(
        API_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    try:
        with urllib.request.urlopen(req, context=ctx) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        print(f"API error {e.code}: {body}", file=sys.stderr)
        sys.exit(1)

    b64_data = data["data"][0]["b64_json"]
    image_bytes = base64.b64decode(b64_data)

    if not filename.endswith(".png"):
        filename = f"{filename}.png"
    filepath = IMAGES_DIR / filename
    filepath.write_bytes(image_bytes)

    return str(filepath)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate an image using OpenAI DALL-E API.")
    parser.add_argument("prompt", type=str, help="Text prompt describing the image to generate.")
    parser.add_argument("filename", type=str, help="Output filename (e.g. burning_hands or burning_hands.png)")
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL, help=f"Model to use (default: {DEFAULT_MODEL})")
    parser.add_argument("--quality", type=str, default=DEFAULT_QUALITY, help=f"Image quality (default: {DEFAULT_QUALITY})")
    parser.add_argument("--size", type=str, default="1024x1024", help="Image size (default: 1024x1024)")
    args = parser.parse_args()

    path = generate_image(args.prompt, args.filename, model=args.model, quality=args.quality, size=args.size)
    print(path)


if __name__ == "__main__":
    main()
