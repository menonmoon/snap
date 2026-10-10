#!/usr/bin/env python3
"""Generate transparent-background PNG assets for lenses with the OpenAI image API.

Usage:
    export OPENAI_API_KEY=...            # never commit the key
    python3 tools/generate_assets.py lenses/mustache-beanie/prompts.json

Each manifest is a JSON list of {"file": "name.png", "prompt": "..."} entries.
PNGs are written to <manifest folder>/Assets/Textures/, the folder Lens Studio
imports from. Existing files are skipped. Only the standard library is required.
"""
import base64
import json
import os
import sys
import urllib.request
from pathlib import Path

API_URL = "https://api.openai.com/v1/images/generations"
MODEL = "gpt-image-1"
STYLE = (
    "Single isolated object, centered, front-facing, clean cut-out edges, "
    "no background, no border, no outline, no glow, no drop shadow, no text."
)


def generate(prompt: str, out_path: Path, api_key: str) -> None:
    body = json.dumps({
        "model": MODEL,
        "prompt": f"{prompt} {STYLE}",
        "size": "1024x1024",
        "background": "transparent",
        "output_format": "png",
        "quality": "medium",
        "n": 1,
    }).encode()
    req = urllib.request.Request(
        API_URL,
        data=body,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=300) as resp:
        payload = json.load(resp)
    out_path.write_bytes(base64.b64decode(payload["data"][0]["b64_json"]))
    print(f"wrote {out_path}")


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("OPENAI_API_KEY is not set", file=sys.stderr)
        return 2
    manifest = Path(sys.argv[1]).resolve()
    out_dir = manifest.parent / "Assets" / "Textures"
    out_dir.mkdir(parents=True, exist_ok=True)
    for item in json.loads(manifest.read_text()):
        out_path = out_dir / item["file"]
        if out_path.exists():
            print(f"skip existing {out_path}")
            continue
        generate(item["prompt"], out_path, api_key)
    return 0


if __name__ == "__main__":
    sys.exit(main())
