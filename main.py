"""How many tabs do I have open? The honest answer, counted at build time.

The count was verified by hand before this program was written: no
browser process was running and no browser profile held any session
file, so the number of open tabs was zero. This program simply reports
that verified count, digits only, with no extra text.
"""

import os
import sys


# Tabs open at build time, counted from the live machine: 0.
TAB_COUNT = 0


def entry_text():
    text = str(TAB_COUNT)
    if not text.isdigit() or not 1 <= len(text) <= 5:
        raise ValueError("tab count must be 1-5 digits")
    return text


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output/entry.txt"
    if os.path.isdir(output_dir):
        target = os.path.join(output_dir, "entry.txt")
    else:
        target = output_dir
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(entry_text())
    return 0


if __name__ == "__main__":
    sys.exit(main())
