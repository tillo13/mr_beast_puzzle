#!/usr/bin/env python3
"""
sync_puzzle_status.py — Read puzzle notes and update docs/index.html progress table.

Scans puzzles/*/notes.md for status indicators and updates the puzzle table
in docs/index.html so the GitHub Pages dashboard stays current.

Usage:
    python tools/github/sync_puzzle_status.py
"""

import os
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PUZZLES_DIR = os.path.join(REPO_ROOT, "puzzles")
INDEX_HTML = os.path.join(REPO_ROOT, "docs", "index.html")

PUZZLE_FOLDERS = [
    ("01_wells_africa", "1"),
    ("02_lifechange", "2"),
    ("03_dirtiest_beach", "3"),
    ("04_experiences", "4"),
    ("05_pokemon_go", "5"),
    ("06_wilderness", "6"),
    ("07_adopted_dogs", "7"),
    ("08_pyramids", "8"),
    ("09_circle", "9"),
]


def get_puzzle_status(folder):
    """Read notes.md and determine puzzle status."""
    notes_path = os.path.join(PUZZLES_DIR, folder, "notes.md")
    if not os.path.exists(notes_path):
        return {"status": "TODO", "puzzle_type": "TBD", "word": None}

    with open(notes_path) as f:
        content = f.read()

    result = {"status": "WIP", "puzzle_type": "TBD", "word": None}

    # Detect puzzle type
    type_match = re.search(r"\*\*Puzzle type:\*\*\s*(.+)", content)
    if type_match:
        result["puzzle_type"] = type_match.group(1).strip()

    # Detect status
    if "GRID SOLVED" in content.upper() or "SOLVED" in content.upper():
        result["status"] = "WIP"  # Grid solved but extraction unknown
    if "ANSWER:" in content.upper() or "ANSWER WORD:" in content.upper():
        answer_match = re.search(r"(?:answer|answer word):\s*\*?\*?(\w+)", content, re.IGNORECASE)
        if answer_match:
            result["word"] = answer_match.group(1)
            result["status"] = "DONE"

    return result


def main():
    print("=== Syncing puzzle status ===")

    statuses = {}
    for folder, num in PUZZLE_FOLDERS:
        status = get_puzzle_status(folder)
        statuses[num] = status
        badge = status["status"]
        word = status["word"] or "—"
        print(f"  Puzzle {num}: {badge} | Type: {status['puzzle_type']} | Word: {word}")

    # Count solved
    solved = sum(1 for s in statuses.values() if s["status"] == "DONE")
    print(f"\n  {solved}/9 words found")

    if not os.path.exists(INDEX_HTML):
        print(f"  WARNING: {INDEX_HTML} not found. Skipping HTML update.")
        return

    print(f"\n  To update docs/index.html, edit the puzzle table manually or")
    print(f"  extend this script with HTML rewriting logic.")
    print(f"\n=== Done ===")


if __name__ == "__main__":
    main()
