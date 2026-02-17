#!/usr/bin/env bash
# setup_labels.sh — Create all puzzle-specific labels on the GitHub repo
# Uses: gh label create
# Run once after repo creation. Safe to re-run (skips existing labels).

set -euo pipefail

echo "=== Setting up labels ==="

# Puzzle-specific labels (blue)
gh label create "puzzle-1" --color "1d76db" --description "Puzzle 1: Wells/Africa (Pinterest)" --force
gh label create "puzzle-2" --color "1d76db" --description "Puzzle 2: LIFECHANGE Sudoku (Reddit)" --force
gh label create "puzzle-3" --color "1d76db" --description "Puzzle 3: Dirtiest Beach (Imgur)" --force
gh label create "puzzle-4" --color "1d76db" --description "Puzzle 4: Experiences (ImageShack)" --force
gh label create "puzzle-5" --color "1d76db" --description "Puzzle 5: Pokemon Go (Photobucket)" --force
gh label create "puzzle-6" --color "1d76db" --description "Puzzle 6: Wilderness (Medium)" --force
gh label create "puzzle-7" --color "1d76db" --description "Puzzle 7: Adopted Dogs (Pixelfed)" --force
gh label create "puzzle-8" --color "1d76db" --description "Puzzle 8: Pyramids (imgpile)" --force
gh label create "puzzle-9" --color "1d76db" --description "Puzzle 9: Circle (500px)" --force

# Special puzzle labels
gh label create "crossword" --color "5319e7" --description "The crossword puzzle" --force
gh label create "super-bowl-ad" --color "e99695" --description "Clues from the Super Bowl ad" --force
gh label create "meta-clue" --color "d93f0b" --description "9-word meta-clue assembly" --force

# Status labels
gh label create "clue" --color "0e8a16" --description "A discovered clue or piece of evidence" --force
gh label create "solution" --color "006b75" --description "A proposed puzzle solution" --force
gh label create "theory" --color "fbca04" --description "An unverified theory or hypothesis" --force
gh label create "confirmed" --color "0e8a16" --description "Verified and confirmed finding" --force
gh label create "red-herring" --color "b60205" --description "Confirmed red herring / dead end" --force
gh label create "needs-verification" --color "c5def5" --description "Needs someone else to verify" --force
gh label create "extraction-method" --color "d4c5f9" --description "How to extract answer from solved puzzle" --force
gh label create "question" --color "cc317c" --description "Question about the puzzle or repo" --force

echo "=== Done! Created 20 labels ==="
echo "View them: gh label list"
