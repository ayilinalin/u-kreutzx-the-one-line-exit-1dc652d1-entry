#!/usr/bin/env python3
"""The One-Line Exit — make.fun bounty entry (program/v1).

Writes a single funny one-line resignation letter to /output/entry.txt.
Gate: UTF-8 text, 1-140 characters, not only whitespace, exactly one line.
"""

import os

ENTRY = "I resign: after three years, the only thing this company ever promoted was the Wi-Fi password."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    if not text or text.isspace():
        raise SystemExit("entry is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be exactly one line")
    if not 1 <= len(text) <= 140:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-140")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
