#!/usr/bin/env python3
"""Write the excuse entry to entry.txt.

Entry for make.fun's "The Excuse That Almost Works": a hurried text
to the boss - the flat's boiler died, the plumber only has today, and
the sender is stood in two inches of water in their socks. Boring,
specific and mundane, which is exactly why a tired manager would
almost believe it.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "sorry, flat's boiler died, plumber only has today, I'm stood in two inches of water in my socks"
TEXT = LINE + "\n"
MAX_CHARS = 140
MAX_WORDS = 20


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be a single line")
    words = body.split()
    if len(words) > MAX_WORDS:
        raise ValueError("entry exceeds the word limit")
    if body != body.strip() or "  " in body:
        raise ValueError("entry must be clean single-spaced text")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
