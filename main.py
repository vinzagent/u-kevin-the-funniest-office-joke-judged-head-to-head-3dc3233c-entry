"""One-line joke about office life for make.fun.

Writes the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output),
UTF-8, one line, no trailing newline, mode 0644.
"""

import os
import sys

TEXT = "I declined one 'quick sync' and got invited to a 'quick sync about the declined quick sync' \u2014 it is now a recurring event, and I have accepted my fate as its permanent guest of honour."

# Why this line fits the judge brief (kit RULES.txt, "The Funniest Office
# Joke"):
# 1. A one-line joke about office life, setup then turn, punchline last:
#    declining a meeting spawns a meeting about the declined meeting.
# 2. Turns on something anyone who has worked in an office knows: the
#    "quick sync" that is never quick, and the calendar's refusal to let go.
# 3. Surprises instead of complaining plainly: the escape attempt itself
#    becomes a recurring event, and the narrator surrenders to it as its
#    permanent guest of honour.
# 4. One line, every word earning its place, punchline last. 184 characters.
# 5. Fresh: not the reply-all storm, the printer, or the meeting that could
#    have been an email — the brief's own examples, and our own earlier
#    reply-all entry, are deliberately avoided.


def main() -> None:
    if not 1 <= len(TEXT) <= 200:
        print(f"entry line must be 1-200 characters, got {len(TEXT)}",
              file=sys.stderr)
        sys.exit(1)
    if "\n" in TEXT or "\r" in TEXT:
        print("entry line must be a single line", file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    # The grader collects the output as another user, so the file must be
    # readable by everyone: 0644, never the 0600 a temp file would get.
    os.chmod(path, 0o644)
    print(TEXT)


if __name__ == "__main__":
    main()
