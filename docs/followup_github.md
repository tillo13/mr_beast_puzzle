# GitHub Followup Tasks

Things to do when you're ready. Nothing here is urgent — the repo works fine as-is. These are "nice to have" features that unlock when you flip certain switches.

## Already Done

- [x] Git repo initialized and pushed to `tillo13/mr_beast_puzzle` (private)
- [x] 20 puzzle-specific labels created on GitHub
- [x] 10 repo topics set for discoverability (mrbeast, puzzle, arg, etc.)
- [x] Repo description set
- [x] 3 GitHub Actions workflows ready (daily source monitor, Pages deploy, auto-label issues)
- [x] 8 setup scripts in `tools/github/` (all documented and repeatable)
- [x] Issue templates for Clue Found, Puzzle Solution, Theory
- [x] PR template, CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md
- [x] CODEOWNERS assigns @tillo13 as reviewer

## When You Want GitHub Pages (Live Dashboard)

The puzzle tracker at `docs/index.html` can be a live website. Requires the repo to be **public** (free plan limitation).

```
1. Go to https://github.com/tillo13/mr_beast_puzzle/settings
2. Scroll to "Danger Zone" → Change visibility → Make public
3. Go to Settings > Pages
4. Source: "GitHub Actions" (the workflow is already set up)
5. Wait ~1 min for the action to run
6. Dashboard live at: https://tillo13.github.io/mr_beast_puzzle
```

Or stay private and just open `docs/index.html` locally in your browser — it works standalone.

## When You Want the Project Board (Kanban)

A visual board with cards for each puzzle, draggable between columns (Todo → In Progress → Done).

```bash
# First, add the required auth scope (one-time):
gh auth refresh -s project,read:project

# Then run the setup script:
bash tools/github/setup_project.sh

# View your board:
# https://github.com/users/tillo13/projects/<number>
```

## When You Want Discussions

A built-in forum on your repo for theories, Q&A, and community chat. Like a mini-Reddit but you control it.

```
1. Go to https://github.com/tillo13/mr_beast_puzzle/settings
2. Scroll to "Features"
3. Check "Discussions"
4. Then run: bash tools/github/setup_discussions.sh
```

## When You Want Branch Protection

Require pull request reviews before merging to main. Good if other people are contributing. Skip this while it's just you.

```bash
bash tools/github/setup_branch_protection.sh
```

## When You Hit a Milestone

Create a release to mark progress (like a save point).

```bash
# After solving a puzzle:
bash tools/github/create_release.sh v0.2.0 "Puzzle 3 solved + extraction method found"

# After assembling the meta-clue:
bash tools/github/create_release.sh v0.9.0 "9-word meta-clue assembled"

# After winning:
bash tools/github/create_release.sh v1.0.0 "We won a million dollars"
```

## Daily Routine (Optional)

Check if any puzzle sources have changed:

```bash
# Run manually:
bash tools/github/daily_check.sh

# Or let GitHub Actions handle it:
# The daily_sources.yml workflow runs at 8am PT automatically.
# If it detects changes, it creates an issue automatically.
```

## What Each GitHub Feature Teaches

| Feature | What it is | Why it's useful here |
|---------|-----------|---------------------|
| **Pages** | Free website from your repo | Live puzzle tracker anyone can see |
| **Actions** | Automated tasks that run on events | Daily source checks, auto-labeling |
| **Projects** | Kanban board (like Trello) | Visual puzzle progress tracking |
| **Discussions** | Built-in forum | Community theories without Reddit drama |
| **Issues** | Bug/task tracker with templates | Structured clue/solution reporting |
| **PRs** | Code review workflow | Review contributions before merging |
| **Labels** | Color-coded tags on issues | Filter by puzzle, status, or type |
| **Releases** | Versioned snapshots with notes | Mark milestones, generate changelogs |
| **Topics** | Repo tags for search | People searching "mrbeast puzzle" find you |
| **CODEOWNERS** | Auto-assign reviewers | You get notified on all PRs |
| **Branch protection** | Require reviews to merge | Keep main branch clean |

## Quick Reference: All Setup Scripts

All in `tools/github/` — run from repo root:

| Script | What it does |
|--------|-------------|
| `setup_labels.sh` | Creates 20 labels (already done) |
| `setup_topics.sh` | Sets repo topics + description (already done) |
| `setup_discussions.sh` | Creates Discussion categories |
| `setup_project.sh` | Creates kanban board with puzzle cards |
| `setup_branch_protection.sh` | Protects main branch |
| `create_release.sh` | Tags + creates a release |
| `sync_puzzle_status.py` | Updates dashboard from puzzle notes |
| `daily_check.sh` | Runs source monitor + commits |
