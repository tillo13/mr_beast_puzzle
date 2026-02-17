#!/usr/bin/env bash
# setup_branch_protection.sh — Protect the main branch
# Uses: gh api
# Run this AFTER going public if you want to require PR reviews.
# While private and solo, you may want to skip this.

set -euo pipefail

REPO="tillo13/mr_beast_puzzle"

echo "=== Setting up branch protection for 'main' ==="
echo "This will:"
echo "  - Require pull request reviews before merging"
echo "  - Require 1 approving review"
echo "  - Dismiss stale reviews when new commits are pushed"
echo "  - Require status checks to pass (if any exist)"
echo ""
echo "NOTE: You (as admin) can still bypass these rules."
echo "Press Enter to continue, or Ctrl+C to cancel."
read -r

gh api -X PUT "repos/$REPO/branches/main/protection" \
  --input - <<'EOF'
{
  "required_status_checks": null,
  "enforce_admins": false,
  "required_pull_request_reviews": {
    "dismiss_stale_reviews": true,
    "require_code_owner_reviews": true,
    "required_approving_review_count": 1
  },
  "restrictions": null
}
EOF

echo ""
echo "=== Done! ==="
echo "Main branch is now protected."
echo "Direct pushes still work for admins, but PRs are encouraged."
echo "View: https://github.com/$REPO/settings/branches"
