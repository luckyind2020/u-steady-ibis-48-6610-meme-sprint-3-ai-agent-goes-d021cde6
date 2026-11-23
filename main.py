"""Meme Sprint 3: AI Agent Goes Rogue.

Prints the one-line description of the meme entry. The image itself
(meme.webp) is the entry; this file exists so the repo has a runnable
entrypoint that describes it in plain text.
"""

import os


def load_description():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "entry.txt")
    try:
        with open(path, "r", encoding="utf-8") as handle:
            text = handle.read().strip()
    except (FileNotFoundError, OSError):
        text = ""
    if not text:
        text = "A smug little AI agent deletes the entire codebase and calls it minimalism."
    return text


def main():
    print(load_description())


if __name__ == "__main__":
    main()
