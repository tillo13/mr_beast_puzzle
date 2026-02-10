# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A collaborative, AI-assisted attempt to solve the MrBeast x Salesforce Million Dollar Puzzle launched during Super Bowl LX (Feb 8, 2026). Designed by Lone Shark Games. Deadline: April 2, 2026. No code to build/lint/test — this is a research and puzzle-solving repo.

## Puzzle Architecture

The puzzle is a multi-step treasure hunt:
1. A playlist of 9 YouTube videos each have a **pinned comment** linking to a sub-puzzle
2. Each solved sub-puzzle yields **one word**
3. The 9 words form a meta-clue with word lengths: **5, 9, 5, 7, 8, 4, 9, 6, 5**
4. The meta-clue is an INSTRUCTION that "defines the nature of the search" — it is NOT the final answer
5. Following the meta-clue's instruction leads to a hidden code
6. Slack the code to Jimmy Donaldson to win

Key constraint: the Super Bowl ad contains extraction keys needed to pull answer words from solved puzzles. The playlist puzzles and the ad are interdependent.

## Hub Videos (4)

| ID | Title | Notes |
|----|-------|-------|
| JBy1T5IykkU | First To Find $1,000,000, Keeps It! | Super Bowl ad, 32s, frame-by-frame clues |
| OBQELGS13XA | Watch My Super Bowl Ad To Win $1,000,000! | Bank heist teaser, 2:25, pinned comment → playlist |
| 8_aIjKi0VLM | Rewatch This Video to Win $1,000,000 | 41s, NO captions/audio/description, purely visual |
| rKg5OZNM1aU | One Idea. 27 Days. Built with Slack. | Salesforce BTS, 60s |

## Puzzle Links (All 9 Found)

All posted by **BeastForce67** accounts across platforms.

| # | Video | Platform | URL |
|---|-------|----------|-----|
| 1 | I Built 100 Wells In Africa (mwKJfNYwvm8) | Pinterest | https://pin.it/3DIjEcxdY |
| 2 | Changing the Lives of 600 Strangers (VGvj6bj4Sog) | Reddit | https://www.reddit.com/user/BeastForce67/comments/1qxxmdn/puzzle/ |
| 3 | I Cleaned The World's Dirtiest Beach (cV2gBU6hKfY) | Imgur | https://imgur.com/gallery/puzzle-mD2eHYD |
| 4 | $1 vs $500,000 Experiences! (Xj0Jtjg3lHQ) | ImageShack | https://imageshack.com/user/BeastForce67 |
| 5 | POKEMON GO STEREOTYPES (e-If_d_bzfI) | Photobucket | https://photobucket.com/share/753ba093-2a25-4fd1-a061-5d199c5bda49 |
| 6 | $10,000 Every Day You Survive In The Wilderness (U_LlX4t0A9I) | Medium | https://medium.com/@beastforce67/puzzle-1a6600218fd0 |
| 7 | I Adopted 100 Dogs! (lOKASgtr6kU) | Pixelfed | https://pixelfed.social/BeastForce67 |
| 8 | I Spent 100 Hours Inside The Pyramids! (NDsO1LT_0lw) | imgpile | https://imgpile.com/u/beastforce67 |
| 9 | Anything You Can Fit In The Circle I'll Pay For (yXWw0_UfSFg) | 500px | https://500px.com/p/beastforce67 |

Full details with pinned comment text: `clues/puzzle_links.md`

## Puzzle Status

| # | Puzzle | Grid/Solve Status | Extraction Status | Answer Word |
|---|--------|-------------------|-------------------|-------------|
| 1 | Wells/Africa (Pinterest) | Not started | — | — |
| 2 | LIFECHANGE Sudoku (Reddit) | **GRID SOLVED** | Unknown (need ad key) | — |
| 3 | Dirtiest Beach (Imgur) | Not started | — | — |
| 4 | Experiences (ImageShack) | Not started | — | — |
| 5 | Pokemon Go (Photobucket) | Not started | — | — |
| 6 | Wilderness (Medium) | Not started | — | — |
| 7 | Adopted Dogs (Pixelfed) | Not started | — | — |
| 8 | Pyramids (imgpile) | Not started | — | — |
| 9 | Circle (500px) | Not started | — | — |
| — | Crossword (video TBD) | Clue text missing | — | — |

## Directory Structure

```
mrbeast_puzzle/
├── README.md                    # Public-facing overview & contributor guide
├── CLAUDE.md                    # AI instructions (this file)
│
├── puzzles/                     # One folder per identified puzzle
│   ├── 01_wells_africa/
│   ├── 02_lifechange/           # GRID SOLVED — notes.md, solve_sudoku.py, puzzle.png
│   ├── 03_dirtiest_beach/
│   ├── 04_experiences/
│   ├── 05_pokemon_go/
│   ├── 06_wilderness/
│   ├── 07_adopted_dogs/
│   ├── 08_pyramids/
│   ├── 09_circle/
│   └── crossword/               # PDF + images, no clue text yet — notes.md
│
├── clues/                       # Raw clue materials (not puzzle-specific)
│   ├── hub_videos/              # 4 hub video MP4s, VTTs, info.json, thumbnails
│   ├── playlist_videos/         # 9 playlist video VTTs, info.json, thumbnails
│   ├── super_bowl_ad/frames/    # 64 frames at 2fps from JBy1T5IykkU
│   ├── teaser_videos/
│   │   ├── rewatch_frames/      # 82 frames from 8_aIjKi0VLM (no audio)
│   │   └── bank_heist_frames/   # 290 frames from OBQELGS13XA
│   ├── social_media/            # X/Instagram/TikTok screenshots
│   └── daily_hints/             # Official hints (hint_01.md, ...)
│
├── sources/                     # External intel — daily-updatable (see pattern below)
│   ├── argnet/                  # ARGNet articles & updates
│   ├── reddit/                  # Reddit threads & BeastForce67 posts
│   ├── gma/                     # Good Morning America hints
│   ├── manifold/                # Community predictions & decoded clues
│   ├── loneshark_games/         # Lone Shark Games info & Discord intel
│   ├── salesforce_hub/          # mrbeast.salesforce.com site data
│   ├── social_media/            # Twitter/Instagram clue screenshots
│   │   ├── twitter/
│   │   └── instagram/
│   ├── tonight_show/            # Tonight Show appearance clues
│   ├── youtube/                 # YouTube-specific analysis
│   │   ├── playlist_videos/
│   │   └── teaser_videos/
│   └── community/               # Cross-platform community progress
│
├── results/                     # Central state only
│   └── state.json               # ONE rolling file: current state of all puzzles + meta-clue
│
├── scripts/                     # Shared automation tools
│   └── check_sources.py         # Source monitor (run daily)
│
└── docs/                        # Documentation, tracking & GitHub Pages
    ├── index.html               # Puzzle tracker dashboard
    ├── how_to_attempt.md        # Agent workflow phases & AI techniques
    ├── nine_word_clue.md        # Meta-clue assembly tracker
    ├── progress.md              # Daily progress log
    ├── potential_tools.md       # Puzzle-relevant tools (vision, audio, stego)
    ├── testing_suite_methodology.md  # Puzzle-specific stage gates
    ├── parallel_agent_strategy.md   # 1-agent-per-puzzle execution plan
    └── sources_strategy.md          # How to check sources without re-scraping
```

## Key Files

- `results/state.json` — **Single source of truth** for current state of all puzzles, meta-clue, and pending work. Read this first. Update your puzzle's entry when you make progress.
- `docs/how_to_attempt.md` — Agent workflow phases & AI techniques to deploy
- `docs/progress.md` — Daily progress log; update at end of each session
- `docs/parallel_agent_strategy.md` — Multi-agent-per-puzzle execution plan with prompt templates
- `docs/sources_strategy.md` — How to check sources incrementally (session startup checklist)
- `clues/puzzle_links.md` — All 9 puzzle links with full pinned comment text

## Repo Conventions

- **Each puzzle gets its own folder** under `puzzles/` — solver scripts, images, and notes co-locate
- **Clues not tied to a specific puzzle** go in `clues/` subdirectories
- **External intel** (web scrapes, community analysis) goes in `sources/` (see daily-update pattern below)
- **Shared scripts** (monitoring, batch tools) go in `scripts/`
- Label theories vs confirmed findings clearly
- Video files (.mp4, .avi, .mkv) are gitignored; images in `puzzles/` and `clues/` are tracked
- Use `yt-dlp --write-auto-subs --sub-lang en` for video transcriptions (no external API needed)

## Sources Daily-Update Pattern

Sources change over time (new hints, community discoveries, site updates). Use this pattern:

```
sources/<topic>/
├── updates.log                   # Append-only log: YYYY-MM-DD: <what changed>
├── <descriptive_name>.md         # Current snapshot of findings
└── YYYY-MM-DD/                   # Optional: daily snapshots when data changes significantly
    └── <raw_data_or_snapshot>.md
```

**Rules:**
1. **Always append to `updates.log`** when scraping or checking a source — even if nothing changed
2. **Overwrite the top-level `.md` file** with latest findings (it's the "current" view)
3. **Create a dated subfolder** only when there's a significant change worth preserving (new hint dropped, puzzle content changed, major community breakthrough)
4. **Web search results** go in the appropriate topic folder, not in `results/`
5. **Run `scripts/check_sources.py` daily** to detect changes on monitored URLs

Example:
```
sources/salesforce_hub/
├── updates.log                   # "2026-02-09: Initial scrape, 403 blocked..."
├── site_info.md                  # Latest known site content
├── 2026-02-10/                   # Created when Hint #2 drops
│   └── hint_02_raw.md
└── 2026-02-11/
    └── hint_03_raw.md
```

## Important Entry Points

- Official hub: https://mrbeast.salesforce.com/
- 9-video playlist: https://www.youtube.com/playlist?list=PLj-VLkYRjRxm5HVGFVpPP5W7jkvvzd1q7
- Super Bowl ad: https://www.youtube.com/watch?v=JBy1T5IykkU
- Bank heist teaser: https://www.youtube.com/watch?v=OBQELGS13XA
- Rewatch video (visual-only): https://www.youtube.com/watch?v=8_aIjKi0VLM
- Slack BTS: https://www.youtube.com/watch?v=rKg5OZNM1aU
- Reddit puzzle (BeastForce67): https://www.reddit.com/user/BeastForce67/comments/1qxxmdn/puzzle/
- ARGNet analysis: https://www.argn.com/2026/02/start_slacking_off_with_mrbeasts_million_dollar_puzzle_hunt/
- Lone Shark Games Discord: https://lonesharkgames.com/discord/

## Stage-Gate Rules (MUST FOLLOW)

These rules prevent lost work across sessions and multi-agent tasks.

### 1. Single Source of Truth
`results/state.json` is the rolling state file. Update your puzzle's entry when you make progress. Do NOT create new timestamped summary files — update `state.json` instead.

### 2. Per-Puzzle Isolation
Each puzzle agent writes ONLY to its own `puzzles/XX_*/` folder. Puzzle-specific findings go in `puzzles/XX_*/notes.md`. Cross-cutting state goes in `results/state.json`.

### 3. File-Based Handoffs
Work in focused sessions. Never rely on one massive context window. All findings must be written to disk in the appropriate `puzzles/`, `clues/`, or `results/` directory.

### 4. Verify Before Proceeding
After puzzle-solving: verify solutions are written to disk before proceeding. Check that `notes.md` exists and contains expected content. Check that `state.json` reflects the new status.

### 5. Multi-Agent Discipline
When launching parallel agents, each agent writes to its own folder. The orchestrator reads `results/state.json` and all `puzzles/*/notes.md` to synthesize. See `docs/parallel_agent_strategy.md`.

### 6. Web Search → Sources
All web search results go into `sources/<topic>/`, not `results/`. Follow the daily-update pattern above. Append to `updates.log` every time you check a source.

### 7. Session Wrap-Up
At end of each session, update `results/state.json` (pending, last_session) and `docs/progress.md`.

## Known Red Herrings

- "Red Herring Bank" name in teaser video
- Acrostic in teaser that spells "this means nothing I just wanted to waste your time lol"
- However, even red herring scenes contain real clues (barcode, calendars) — stay thorough
