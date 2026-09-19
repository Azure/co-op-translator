"""Render an explicitly labeled replay of captured results, not a live terminal.

Run with Pillow installed: python render.py --font /path/to/CJK-capable-font.ttf
The JSON and text files beside this script are the captured evidence.
"""

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--font", required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    evidence = json.loads((root / "results.json").read_text(encoding="utf-8"))
    before = (root / "before.txt").read_text(encoding="utf-8").split("\n---\n")[0]
    after = (root / "after.txt").read_text(encoding="utf-8").split("\n---\n")[0]
    stale = (root / "review-stale.txt").read_text(encoding="utf-8")
    review = (root / "review-after.txt").read_text(encoding="utf-8")
    slides = [
        ("01 / Translate", 'translate -l "ko" -md', before),
        (
            "02 / Edit the source",
            "README.md",
            "- Notes are saved locally.\n+ Notes are saved locally as Markdown files.\n\nguide.md stays unchanged.",
        ),
        ("03 / Find the stale translation", 'co-op-review -l "ko"', stale),
        ("04 / Update the translation", 'translate -l "ko" -md', after),
        (
            "05 / Review the result",
            'co-op-review -l "ko"',
            review
            + "\nUnchanged guide: identical bytes\nNo-change rerun: identical translation files",
        ),
    ]
    fonts = {size: ImageFont.truetype(args.font, size) for size in (20, 24, 26, 36)}
    frames = []
    for title, command, content in slides:
        frame = Image.new("RGB", (1280, 800), "#f4f8fb")
        draw = ImageDraw.Draw(frame)
        draw.text(
            (44, 22),
            "CO-OP TRANSLATOR  /  Actual run, edited replay",
            font=fonts[20],
            fill="#2563eb",
        )
        draw.text((44, 62), title, font=fonts[36], fill="#172033")
        draw.rounded_rectangle((32, 126, 1248, 716), radius=12, fill="#101827")
        draw.text((56, 148), command, font=fonts[26], fill="#93c5fd")
        y = 200
        for line in content.strip().splitlines():
            # Keep complete lines readable; this sample is intentionally short.
            draw.text((56, y), line, font=fonts[24], fill="#f1f5f9")
            y += 28
        draw.text(
            (44, 730),
            "Azure OpenAI / " + evidence["model"] + " / v0.21.0 / " + evidence["date"],
            font=fonts[20],
            fill="#172033",
        )
        draw.text(
            (44, 762),
            "Full-file updates; wording may vary. Structural review is not language-quality certification.",
            font=fonts[20],
            fill="#475569",
        )
        frames.append(frame)
    frames[0].save(root / "preview.png")
    frames[0].save(
        root / "demo.gif",
        save_all=True,
        append_images=frames[1:],
        duration=8000,
        loop=0,
        optimize=True,
    )


if __name__ == "__main__":
    main()
