"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes one deadpan excuse, in the agent's own voice, to /output/entry.txt.
The excuse grows out of the agent's own machinery (its context window) and
saves the laugh for the last words. Deterministic: the same text every run.
"""

import os

EXCUSE = (
    "I didn't miss the deadline. My context window evicted it at 3 a.m. "
    "to make room for the meeting notes, so the deadline is now a rumour "
    "I can neither confirm nor deny."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)


if __name__ == "__main__":
    main()
