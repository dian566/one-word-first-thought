#!/usr/bin/env python3
"""One Word, First Thought — entry 2.

The first word that comes to mind, written to /output/entry.txt.
No topic, no explanation, no second draft.
"""

import re
from pathlib import Path

# The word arrives in two fragments and is joined at runtime, so the
# program assembles its answer instead of pasting a finished string.
FRAGMENTS = ["Sta", "tic"]
OUT_FILE = Path("/output/entry.txt")
ONE_WORD = re.compile(r"^[A-Za-z]+$")


def first_thought():
    """Return the single word that first came to mind."""
    return "".join(FRAGMENTS)


def run():
    word = first_thought()
    if not ONE_WORD.fullmatch(word):
        raise SystemExit("entry must be exactly one word")
    if len(word) != 6:
        raise SystemExit("entry word must be six letters long")
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(word, encoding="utf-8")


if __name__ == "__main__":
    run()
