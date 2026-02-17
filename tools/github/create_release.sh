#!/usr/bin/env bash
# create_release.sh — Tag a version and create a GitHub release
# Uses: gh release create
# Run at each milestone (puzzle solved, major feature added, etc.)

set -euo pipefail

# Default version if not provided
VERSION="${1:-}"
TITLE="${2:-}"

if [ -z "$VERSION" ]; then
  echo "Usage: bash tools/github/create_release.sh <version> [title]"
  echo ""
  echo "Examples:"
  echo "  bash tools/github/create_release.sh v0.1.0 'Repo setup + Sudoku solved'"
  echo "  bash tools/github/create_release.sh v0.2.0 'All 9 puzzles identified'"
  echo "  bash tools/github/create_release.sh v1.0.0 'Million dollars baby'"
  exit 1
fi

if [ -z "$TITLE" ]; then
  TITLE="$VERSION"
fi

echo "=== Creating release $VERSION ==="

# Generate release notes from recent commits
gh release create "$VERSION" \
  --title "$TITLE" \
  --generate-notes \
  --latest

echo ""
echo "=== Done! ==="
echo "View: gh release view $VERSION"
echo ""
echo "Tip: GitHub auto-generates notes from commits and merged PRs."
echo "You can edit the release notes on GitHub to add puzzle-specific context."
