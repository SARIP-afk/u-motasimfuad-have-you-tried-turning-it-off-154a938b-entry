#!/usr/bin/env python3
"""Write one funny tech-support line to /output/entry.txt.

Pure stdlib, deterministic, no network. The line is a fixed string: the
program writes exactly these bytes on every run.
"""

import os

LINE = (
    "Have you tried turning it off and on again? "
    "It has never once worked, but it got me promoted twice."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
