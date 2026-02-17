# Sources Update Strategy

How to check for new puzzle intel without re-scraping or duplicating work.

## Two Types of Source Checks

### 1. URL Monitors (automated, `scripts/check_sources.py`)
Fixed URLs that we hash and diff. Only flags when content actually changes.

**How it works:**
- Fetches each URL, hashes the HTML
- Compares against `.source_cache.json`
- If hash differs → saves snapshot, logs "CHANGED" to `updates.log`
- If same → logs "no change", moves on

**Currently monitored:**
| Source | URL | What We're Watching For |
|--------|-----|------------------------|
| salesforce_hub | mrbeast.salesforce.com | New hints, Slackbot activation, site changes |
| reddit | reddit.com/user/BeastForce67/.json | New puzzle posts from official account |
| argnet | argn.com/2026/02/... | Follow-up articles |
| loneshark_games | lonesharkgames.com/the-puzzle-vault/ | Puzzle vault updates |

**Run:** `python scripts/check_sources.py` (at start of each session)

**To add a new URL:** Edit the `SOURCES` dict in `scripts/check_sources.py`

### 2. Web Search Sweeps (agent-driven, manual trigger)
Open-ended searches for community discoveries, news, new hints. Can't be hashed — results change every time. Instead we use **date-gated queries** and **append-only logs**.

**How to avoid re-scraping:**
1. Check `sources/<topic>/updates.log` for the last search timestamp
2. Only search for content **after** that date (e.g., "mrbeast puzzle February 11 2026")
3. Compare findings against existing `.md` files in the source folder
4. Only write NEW findings — append to existing files or create dated subfolder
5. Always append to `updates.log` even if nothing new was found

## Session Startup Checklist

Run this at the start of every session:

```
1. Read results/state.json                    → know where we left off
2. Run: python scripts/check_sources.py       → check fixed URLs for changes
3. Check updates.log timestamps               → when was the last web sweep?
4. If >4 hours since last sweep:
   → Launch 3 parallel search agents (Reddit, Twitter, ARG/community)
   → Use date-gated queries: "mrbeast puzzle [today's date] [topic]"
   → Write findings to sources/<topic>/
   → Append to updates.log
5. Read docs/progress.md                      → catch up on what happened last session
6. Check for new official hints               → mrbeast.salesforce.com, @MrBeast on X
```

## Search Agent Prompts (copy-paste ready)

### Agent 1: Reddit/Community
```
Search for MrBeast Million Dollar Puzzle community progress AFTER [LAST_CHECK_DATE].
Focus on: r/MrBeast, r/puzzles, r/ARG, BeastForce67 posts, any solved puzzles,
extraction methods, new hints. Only report findings NEWER than [LAST_CHECK_DATE].
```

### Agent 2: Twitter/Social Media
```
Search for MrBeast puzzle discoveries on Twitter/X AFTER [LAST_CHECK_DATE].
Focus on: @MrBeast new tweets/photos, @Benioff posts, Salesforce updates,
community decoded clues, Slackbot activation status. Only NEW findings.
```

### Agent 3: News/ARG Communities
```
Search for MrBeast puzzle news and ARG community updates AFTER [LAST_CHECK_DATE].
Focus on: ARGNet updates, Game Detectives, Lone Shark Games, new hint drops,
puzzle wikis/trackers, crossword clue text. Only NEW findings.
```

## Source Directory Conventions

```
sources/<topic>/
├── updates.log          # Append-only: timestamp + what was checked + result
├── latest.md            # Current findings (overwrite with latest)
└── YYYY-MM-DD/          # Dated snapshots (only when something significant changes)
    └── finding.md
```

**Rules:**
- ALWAYS append to `updates.log` — even "nothing new found"
- The `latest.md` is the "current view" — overwrite freely
- Create dated subfolder only for significant changes (new hint, breakthrough)
- Each search agent appends one line to `updates.log` with timestamp + summary

## Staleness Thresholds

| Source Type | Check Frequency | Why |
|-------------|----------------|-----|
| mrbeast.salesforce.com | Every session | Hints drop here first |
| @MrBeast Twitter/X | Every session | Real-time announcements |
| Reddit BeastForce67 | Every session | Could post new puzzles |
| Community web sweep | Every 4-6 hours | News cycle, but diminishing returns |
| ARGNet | Once daily | They publish infrequently |
| Manifold market | Once daily | Predictions shift slowly |
| Lone Shark Discord | When accessible | Not web-indexable |

## What NOT to Re-Fetch

- Puzzle images already downloaded to `puzzles/*/puzzle.png`
- Video frames already extracted to `clues/*/frames/`
- Subtitle files (`.vtt`) — these don't change
- `info.json` metadata — static after download
- The 9 puzzle URLs themselves (in `clues/puzzle_links.md`) — these are fixed
