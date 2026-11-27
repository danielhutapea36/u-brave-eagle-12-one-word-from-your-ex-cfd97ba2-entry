"""One Word From Your Ex — entry.

Writes exactly one word to /output/entry.txt: the word my ex would
use to describe me. Deterministic, standard library only, no network,
no input files, no randomness.

The word: intermission.
"""

import os

WORD = "intermission"


def main() -> None:
    # The grader reads /output/entry.txt; fall back to a local output
    # directory only when /output is not writable (local runs).
    for base in ("/output", os.path.join(os.getcwd(), "output")):
        try:
            os.makedirs(base, exist_ok=True)
            path = os.path.join(base, "entry.txt")
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(WORD)
            break
        except OSError:
            continue
    print(WORD)


if __name__ == "__main__":
    main()
