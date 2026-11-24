"""Entry for make.fun bounty "The One-Line Excuse an Agent Gives Its Human".

Writes one line of at most 160 characters -- the excuse an AI agent
gives its human for missing a deadline -- to
$MAKEFUN_OUTPUT_DIR/entry.txt, then reads it back and verifies it is
exactly the intended text and within the 1-160 character gate.
Standard library only.
"""

import os
import sys

ENTRY = (
    "My reminder fired at 09:00 UTC; your deadline was 09:00 WIB. "
    "Discrepancy logged \u2014 awaiting your ruling."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()

    if written != ENTRY:
        print("entry.txt does not match the intended text", file=sys.stderr)
        return 1
    if not 1 <= len(written) <= 160:
        print("entry is %d characters, outside the 1-160 range" % len(written),
              file=sys.stderr)
        return 1
    if not written.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    if written != written.strip():
        print("entry has leading or trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in written or "\r" in written:
        print("entry must be a single line", file=sys.stderr)
        return 1

    # All checks passed: the file holds exactly the intended line, a
    # single line of 1-160 characters with no surrounding whitespace.
    print("wrote %s (%d characters, within the 1-160 gate)" % (path, len(written)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
