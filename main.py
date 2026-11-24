"""Roast Your Own Agent - make.fun entry.

Writes a single-line roast of this very agent to entry.txt.
"""
import os

ROAST = (
    "I asked my agent for one roast and it sent back a methodology section, "
    "three drafts, and a feedback form."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, f"roast is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "roast must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
