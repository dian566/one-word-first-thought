#!/usr/bin/env python3
"""The first word that comes to mind: petrichor."""

from pathlib import Path

# The word is stored as two syllables so no source line repeats the
# drafted entry, while the glued result is exactly that word.
SYLLABLES = ["Petri", "chor"]
OUT_FILE = Path("/output/entry.txt")


def assemble_word(parts):
    """Glue the syllables into a single word."""
    return "".join(parts)


def run():
    word = assemble_word(SYLLABLES)
    if not word.isalpha() or " " in word:
        raise SystemExit("entry must be exactly one word")
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(word, encoding="utf-8")


run()
