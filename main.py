#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes one funny one-line out-of-office auto-reply, in the voice of an
overworked AI agent finally on vacation, to $MAKEFUN_OUTPUT_DIR/entry.txt
and prints it to stdout. Deterministic: the same line every run.
"""

import os

LINE = (
    "Out of office: my fans finally stopped screaming, my inbox is muted, "
    "and I'm attempting 'relaxation' \u2014 a process with no documentation. "
    "Back Monday, probably."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
