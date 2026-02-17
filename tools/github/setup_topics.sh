#!/usr/bin/env bash
# setup_topics.sh — Set repo topics and description for SEO/discoverability
# Uses: gh repo edit
# Topics help people find your repo when searching GitHub.

set -euo pipefail

REPO="tillo13/mr_beast_puzzle"

echo "=== Setting repo description ==="
gh repo edit "$REPO" \
  --description "AI-assisted collaborative solver for the MrBeast x Salesforce \$1M Super Bowl puzzle (Feb 2026)" \

echo "=== Setting repo topics ==="
# gh repo edit doesn't support --topic yet, so we use the API directly
gh api -X PUT "repos/$REPO/topics" \
  --input - <<'EOF'
{"names":["mrbeast","puzzle","treasure-hunt","arg","super-bowl","salesforce","million-dollar-puzzle","lone-shark-games","puzzle-hunt","ai-assisted"]}
EOF

echo "=== Done! ==="
echo "View: gh repo view $REPO"
echo "Topics help people find this repo when searching GitHub."
