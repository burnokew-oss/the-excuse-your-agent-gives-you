#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — entry writer.

Writes a single one-line excuse (an AI agent owning up to its human for
a bug it shipped) to /output/entry.txt. Pure stdlib, deterministic: the
same bytes on every run (sha256 b664ed67d540b9682febb38eb538cdc88e5971a8c
ab4a6c0e83d66567008a502, verified 3x), no trailing newline so the file is
exactly one line. Entry is 119 characters, within the 200-character gate.
"""

import os

ENTRY = (
    # Rubric pick: the specific absurdity of an agent owning its own
    # code — it wrote the bug, tested it, approved its own pull
    # request, and shipped it anyway. The turn lands last:
    # "I was very thorough."
    "I found the bug. I wrote it, I tested it, "
    "I approved my own pull request, and I shipped it anyway. "
    "I was very thorough."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
