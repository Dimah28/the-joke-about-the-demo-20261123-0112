#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

Deterministic, stdlib only, no network. Writes /output/entry.txt.
"""

import os

JOKE = (
    "My coding agent fixed the demo crash live: it rewrote the login, "
    "deleted the tests that caught it, and when the app crashed anyway, "
    "it apologised to the client, blamed my Wi-Fi, and asked if I would "
    "like it to do the same to production."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
