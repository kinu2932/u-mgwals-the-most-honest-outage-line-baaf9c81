#!/usr/bin/env python3
"""The Most Honest Outage Line.

Writes a single status-page line (at most 160 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Pure Python standard library, no network, no dependencies, fully
deterministic: the same bytes on every run.
"""

import os
import sys

ENTRY = (
    "Every server is down, including the one I use to check whether "
    "servers are down. I don't know why yet, and I can't find out "
    "until something comes back."
)


def main() -> int:
    if not (1 <= len(ENTRY) <= 160):
        print(
            "entry is %d characters; must be 1-160" % len(ENTRY),
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
