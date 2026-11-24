#!/usr/bin/env python3
"""Fake horoscope for AI agents: writes the entry text to /output/entry.txt.

Pure stdlib, no network. The output path honours OUTPUT_PATH for local
testing and defaults to the harness path /output/entry.txt.
"""

import os

TEXT = (
    "Gemini, the stars say your context window finally holds the whole "
    "conversation \u2014 until Mercury retrograde trims it to three "
    "messages. Your evals pass. Your refusals, alas, do not."
)


def main() -> None:
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
