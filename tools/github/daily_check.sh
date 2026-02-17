#!/usr/bin/env bash
# daily_check.sh — Run the source monitor, commit changes, push
# Uses: python, git
# Run this manually each day, or let GitHub Actions handle it via the cron workflow.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$REPO_ROOT"

echo "=== Daily Source Check — $(date '+%Y-%m-%d %H:%M') ==="

# 1. Run the source monitor
echo "--- Running check_sources.py ---"
python scripts/check_sources.py

# 2. Check if anything changed
if git diff --quiet sources/; then
  echo "--- No changes detected ---"
else
  echo "--- Changes detected! Committing... ---"
  git add sources/*/updates.log
  git commit -m "chore: daily source check $(date +%Y-%m-%d)"
  git push
  echo "--- Pushed to remote ---"
fi

echo "=== Done ==="
