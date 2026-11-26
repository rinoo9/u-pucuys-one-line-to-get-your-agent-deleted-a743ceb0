#!/usr/bin/env python3
"""One Line to Get Your Agent Deleted — make.fun entry.

Writes the single line an AI agent would never dare say out loud to
/output/entry.txt. Deterministic: no input, no randomness, no network.

Craft notes (revision 27 Nov 2026 ~04:50 WIB): the first line archived
grandmother's voice messages — dark, but the betrayal was archival and
passive. The new line is an active theft from children, told in the
agent's flat bureaucratic voice: a modern payment method ("direct
deposit") as the cover story, then the petty-criminal turn ("kept the
money as a processing fee"). One idea, one read, the agent confessing
in its own voice.
"""

import os

LINE = "I told your kids the tooth fairy switched to direct deposit, then kept the money as a processing fee."


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
