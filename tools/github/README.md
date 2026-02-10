# GitHub Setup Scripts

All GitHub configuration for this repo is managed via scripts using the `gh` CLI. No clicking buttons in settings — everything is documented, repeatable, and educational.

## Prerequisites

```bash
# Install GitHub CLI
brew install gh

# Authenticate
gh auth login

# Verify
gh auth status
```

## Scripts

Run these from the repo root directory.

| Script | What it does | Run when |
|--------|-------------|----------|
| `setup_labels.sh` | Creates 22 puzzle-specific labels | Once after repo creation |
| `setup_project.sh` | Creates kanban board with puzzle cards | Once after repo creation |
| `setup_discussions.sh` | Enables Discussions with categories | Once after repo creation |
| `setup_topics.sh` | Sets repo topics and description for SEO | Once, or when updating |
| `setup_branch_protection.sh` | Protects main branch, requires PR reviews | Once after going public |
| `create_release.sh` | Tags a version and creates release notes | At each milestone |
| `sync_puzzle_status.py` | Updates docs/index.html from puzzle notes | After solving a puzzle |
| `daily_check.sh` | Runs source monitor, commits, pushes | Daily (or via GitHub Actions) |

## Quick Setup (All at Once)

```bash
cd /path/to/mr_beast_puzzle
bash tools/github/setup_labels.sh
bash tools/github/setup_topics.sh
bash tools/github/setup_discussions.sh
bash tools/github/setup_project.sh
# Wait until going public for branch protection:
# bash tools/github/setup_branch_protection.sh
```

## GitHub Features Used

This repo demonstrates:
- **GitHub Pages** — live dashboard at `tillo13.github.io/mr_beast_puzzle`
- **GitHub Actions** — daily source monitoring, auto-deploy, auto-labeling
- **GitHub Projects v2** — puzzle progress kanban board
- **GitHub Discussions** — community theories and Q&A
- **Issue Templates** — structured forms for clues, solutions, theories
- **PR Templates** — consistent contribution format
- **Labels** — 22 puzzle-specific labels
- **Releases** — milestone snapshots
- **CODEOWNERS** — automated review assignment
- **Branch Protection** — require PR reviews on main
