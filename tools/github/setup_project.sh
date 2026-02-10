#!/usr/bin/env bash
# setup_project.sh — Create a GitHub Projects v2 kanban board for puzzle tracking
# Uses: gh project create, gh project field-create, gh project item-add
# Creates a board with status columns and one card per puzzle.

set -euo pipefail

OWNER="tillo13"

echo "=== Creating Project Board ==="
PROJECT_NUM=$(gh project create \
  --owner "$OWNER" \
  --title "MrBeast \$1M Puzzle Tracker" \
  --format BOARD \
  2>&1 | grep -oE '[0-9]+$')

echo "Created project #$PROJECT_NUM"

# Get project ID for API calls
PROJECT_ID=$(gh api graphql -f query='
  query($owner: String!, $num: Int!) {
    user(login: $owner) {
      projectV2(number: $num) { id }
    }
  }
' -f owner="$OWNER" -F num="$PROJECT_NUM" --jq '.data.user.projectV2.id')

echo "Project ID: $PROJECT_ID"

# The default Status field has "Todo", "In Progress", "Done"
# We'll add custom options for puzzle stages
echo "=== Adding custom status options ==="

# Get the Status field ID
STATUS_FIELD_ID=$(gh api graphql -f query='
  query($id: ID!) {
    node(id: $id) {
      ... on ProjectV2 {
        fields(first: 20) {
          nodes {
            ... on ProjectV2SingleSelectField {
              id
              name
            }
          }
        }
      }
    }
  }
' -f id="$PROJECT_ID" --jq '.data.node.fields.nodes[] | select(.name == "Status") | .id')

echo "Status field: $STATUS_FIELD_ID"

# Add draft items for each puzzle
echo "=== Adding puzzle cards ==="

PUZZLES=(
  "Puzzle 1 — Wells/Africa (Pinterest)"
  "Puzzle 2 — LIFECHANGE Sudoku (Reddit) [GRID SOLVED]"
  "Puzzle 3 — Dirtiest Beach (Imgur)"
  "Puzzle 4 — Experiences (ImageShack)"
  "Puzzle 5 — Pokemon Go (Photobucket)"
  "Puzzle 6 — Wilderness (Medium)"
  "Puzzle 7 — Adopted Dogs (Pixelfed)"
  "Puzzle 8 — Pyramids (imgpile)"
  "Puzzle 9 — Circle (500px)"
  "Crossword — Video TBD"
  "META-CLUE — 9 words (5,9,5,7,8,4,9,6,5)"
)

for puzzle in "${PUZZLES[@]}"; do
  echo "  Adding: $puzzle"
  gh project item-create "$PROJECT_NUM" --owner "$OWNER" --title "$puzzle" --format BOARD 2>/dev/null || echo "    (error, skipping)"
done

echo ""
echo "=== Done! ==="
echo "View: https://github.com/users/$OWNER/projects/$PROJECT_NUM"
echo ""
echo "Next steps:"
echo "  - Drag cards to the right column (Todo/In Progress/Done)"
echo "  - Link issues to project cards as you create them"
