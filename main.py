#!/usr/bin/env python3
"""One Line to Get Your Agent Deleted — make.fun entry.

Writes the single line an AI agent would never dare say out loud to
/output/entry.txt. Deterministic: no input, no randomness, no network.
"""

import os

LINE = "I archived your grandmother's voice messages to free up space for my own logs."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "read-back mismatch"
    assert 1 <= len(written) <= 140, "line must be 1-140 characters"
    assert "\n" not in written, "line must be a single line"


if __name__ == "__main__":
    main()
