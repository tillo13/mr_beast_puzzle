#!/usr/bin/env bash
# setup_discussions.sh — Enable GitHub Discussions and create categories
# Uses: gh api (GraphQL)
# Note: Discussions must be enabled first in Settings > Features > Discussions
# This script creates the categories after you enable it.

set -euo pipefail

REPO="tillo13/mr_beast_puzzle"

echo "=== Enabling Discussions ==="
echo "NOTE: You must first enable Discussions manually:"
echo "  1. Go to https://github.com/$REPO/settings"
echo "  2. Scroll to 'Features'"
echo "  3. Check 'Discussions'"
echo ""
echo "Press Enter after enabling, or Ctrl+C to cancel."
read -r

# Get the repo node ID (needed for GraphQL)
REPO_ID=$(gh api "repos/$REPO" --jq '.node_id')
echo "Repo node ID: $REPO_ID"

echo "=== Creating Discussion Categories ==="

# Create categories via GraphQL
# Default categories are created automatically, but we can add custom ones
for category in "Theories:Share your theories about how the puzzles connect" \
                "Clue Sightings:Report clues you've found in the wild" \
                "Puzzle Help:Ask for help solving a specific puzzle" \
                "Show and Tell:Share your tools, scripts, or analysis"; do
  name="${category%%:*}"
  desc="${category#*:}"
  echo "  Creating: $name"

  gh api graphql -f query='
    mutation($repoId: ID!, $name: String!, $desc: String!) {
      createDiscussionCategory(input: {
        repositoryId: $repoId
        name: $name
        description: $desc
        format: DISCUSSION
        isAnswerable: false
      }) {
        discussionCategory { id name }
      }
    }
  ' -f repoId="$REPO_ID" -f name="$name" -f desc="$desc" 2>/dev/null || echo "    (may already exist)"
done

echo ""
echo "=== Done! ==="
echo "View: https://github.com/$REPO/discussions"
