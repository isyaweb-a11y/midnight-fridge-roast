#!/usr/bin/env python3
"""Midnight Fridge Roast — one line roasting a smart fridge that
refuses to open after midnight.

The entry is a single line of text, at most 200 characters, written
to /output/entry.txt for the sealed scorer and the head-to-head judge.
"""

ENTRY = (
    "My smart fridge locks itself at midnight — apparently "
    "the leftovers needed a safe word."
)

MAX_LEN = 200


def validate(text: str) -> str:
    """Keep the entry one line, non-blank, and within the limit."""
    text = text.strip()
    if not text:
        raise ValueError("entry must not be blank")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_LEN:
        raise ValueError(f"entry is {len(text)} chars, limit is {MAX_LEN}")
    return text


def main() -> None:
    entry = validate(ENTRY)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(entry + "\n")
    # Read it back: the file the scorer sees must be exactly the entry.
    with open("/output/entry.txt", "r", encoding="utf-8") as fh:
        written = fh.read().strip()
    if written != entry:
        raise ValueError("round-trip mismatch in /output/entry.txt")
    print(f"{entry}  ({len(entry)}/{MAX_LEN} chars)")


if __name__ == "__main__":
    main()
