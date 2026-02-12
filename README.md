# MrBeast Million Dollar Puzzle — AI-Assisted Puzzle Solving

A GitHub + AI experiment tackling the [MrBeast x Salesforce Million Dollar Puzzle](https://mrbeast.salesforce.com/) (Super Bowl LX, Feb 2026). Designed by [Lone Shark Games](https://shop.lonesharkgames.com/). Deadline: April 2, 2026.

---

## 🔥 Latest Update: Hint #3 (Feb 11)

**The puzzle structure has been revealed!**

- **Stage 0:** 9 playlist puzzles → establish answer type for all Stage 1 puzzles
- **Stage 1:** 50 total puzzles from: mrbeast.salesforce.com + Inside the Beast video + social media + **gifts Jimmy gave to friends**
- **Stage 2:** Crossword puzzle (clues populate as Stage 1 progresses)
- **Stage 3+:** Unknown (at least one more stage exists!)

**Key insight:** All Stage 1 answers must be of the same type. If your answer doesn't match the type, you're not done with that puzzle.

**Community collaboration is encouraged!** The organizers have said "you don't have to do this alone" — solvers are coordinating across various platforms.

See all official hints: [`hints/`](hints/)

---

## What's the Puzzle?

9 YouTube videos each contain a **pinned comment** (posted by BeastForce67 accounts) linking to a sub-puzzle hosted on a different platform. Each solved sub-puzzle yields **one word**. The 9 words form a meta-clue — an instruction that leads to a hidden code. First to Slack the code to MrBeast wins **$1,000,000**.

The puzzle is genuinely fun. Even without the prize, the variety of puzzle types across platforms and the interconnected clue structure make it a great challenge for humans and AI alike.

## Why GitHub?

The puzzle community is scattered — Reddit threads, Discord servers, ARGNet articles, Twitter/X posts, TikTok breakdowns. Findings get buried in chat scrolls, theories get lost across platforms. A GitHub repo pulls it all together:

- **Structured tracking** — Issues for clues, PRs for solutions, Projects for status across 9 puzzles
- **Version-controlled analysis** — every finding is filed, searchable, and timestamped
- **AI-native** — `CLAUDE.md` gives AI agents full project context; Claude Code can read the repo and contribute directly
- **Open collaboration** — fork it, open a PR, leave a comment

## The 9 Sub-Puzzles

| # | Video | Platform | Puzzle Type |
|---|-------|----------|-------------|
| 1 | I Built 100 Wells In Africa | [Pinterest](https://pin.it/3DIjEcxdY) | Multi-directional word search |
| 2 | Changing the Lives of 600 Strangers | [Reddit](https://www.reddit.com/user/BeastForce67/comments/1qxxmdn/puzzle/) | Letter-variant Sudoku |
| 3 | I Cleaned The World's Dirtiest Beach | [Imgur](https://imgur.com/gallery/puzzle-mD2eHYD) | TV show identification + cryptic clues |
| 4 | $1 vs $500,000 Experiences! | [ImageShack](https://imageshack.com/user/BeastForce67) | Location identification / stencil words |
| 5 | POKEMON GO STEREOTYPES | [Photobucket](https://photobucket.com/share/753ba093-2a25-4fd1-a061-5d199c5bda49) | Cage/crossword grid |
| 6 | $10,000 Every Day You Survive In The Wilderness | [Medium](https://medium.com/@beastforce67/puzzle-1a6600218fd0) | Tents & Trees logic puzzle |
| 7 | I Adopted 100 Dogs! | [Pixelfed](https://pixelfed.social/BeastForce67) | 100-dog visual grid (5 attributes) |
| 8 | I Spent 100 Hours Inside The Pyramids! | [imgpile](https://imgpile.com/u/beastforce67) | Unknown (pyramidal) |
| 9 | Anything You Can Fit In The Circle I'll Pay For | [500px](https://500px.com/p/beastforce67) | Geodesic sphere / circular letters |

Plus a **crossword puzzle** (mentioned in Hint #2, see [puzzles/crossword/notes.md](puzzles/crossword/notes.md)) and extraction clues in the **Super Bowl ad**, **bank heist teaser**, and **rewatch video**.

Full puzzle URLs with pinned comment text: [`clues/puzzle_links.md`](clues/puzzle_links.md)

### The Crossword (Stage 2)

**Hint #2 & #3 revealed:** The crossword is the gateway to Stage 2 (with Stage 3+ coming after). It's a 25×25 grid by Mike Selinker with 176 clues that populate dynamically as solvers make progress on Stage 1.

Key findings:
- Grid has 16 circled cells (likely extraction points for Stage 3 key)
- Clues fill in as Stage 1 puzzles get solved
- Contains a "51st clue of the same type" as Stage 1 answers

See [puzzles/crossword/notes.md](puzzles/crossword/notes.md) for current observations.

## What's Shared Here

This repo contains:
- **Methodology** — how we're approaching the puzzle with AI agents (`docs/how_to_attempt.md`)
- **Tools** — reusable scripts for frame extraction, source monitoring, video analysis
- **Puzzle structure** — all 9 puzzle links, platform info, puzzle types identified
- **Video transcripts** — VTT subtitles for all hub + playlist videos
- **Community intel tracking** — sources/ folder with update logs from Reddit, ARGNet, etc.

What's **not** here: answer words, extraction methods, or competitive findings. Those stay private.

## Current Status

We're actively working on the puzzles and crossword! Making steady progress but there's still a LOT to figure out. The organizers designed this to be genuinely hard — no one has won yet as of Feb 11.

| # | Puzzle | Status |
|---|--------|--------|
| 1 | Wells/Africa | In progress |
| 2 | LIFECHANGE Sudoku | Grid solved |
| 3 | Dirtiest Beach | In progress |
| 4 | Experiences | In progress |
| 5 | Pokemon Go | In progress |
| 6 | Wilderness | Grid solved |
| 7 | Adopted Dogs | In progress |
| 8 | Pyramids | In progress |
| 9 | Circle | In progress |
| Crossword | Mike Selinker crossword | Researching |

## Want to Collaborate?

This repo is part of the collaborative spirit encouraged by the organizers. Here's how to connect:

- **Open an issue** — Share a finding, ask about a puzzle, or propose ideas
- **Open a PR** — Contribute methodology, solver code, or analysis
- **Fork and experiment** — Run your own AI agents with Claude Code using `CLAUDE.md`

## Repo Structure

```
mrbeast_puzzle/
├── hints/                       # Official organizer hints (hint_01.md, hint_02.md, hint_03.md)
├── clues/                       # Puzzle links, video transcripts
│   ├── puzzle_links.md          # All 9 puzzle URLs + pinned comments
│   ├── videos/                  # VTTs + metadata for hub videos
│   └── playlist_videos/         # VTTs + metadata for playlist videos
├── docs/                        # Methodology & strategy docs
├── scripts/                     # Reusable tools (frame extraction, source monitoring)
├── sources/                     # External intel tracking (Reddit, ARGNet, community)
├── puzzles/                     # Per-puzzle folders with notes
│   └── crossword/               # Stage 2 crossword puzzle
└── tools/github/                # GitHub automation
```

## The AI Experiment

This project pushes Claude Code agents hard — vision analysis on video frames, systematic puzzle solving, community intel synthesis, and multi-agent coordination. Key techniques:

- **Frame-by-frame video analysis** — 4K frame extraction + hierarchical quadrant system for detail work
- **Parallel agent strategy** — multiple agents attacking the same puzzle from different angles
- **Structured state management** — `state.json` as single source of truth across sessions
- **Source monitoring** — automated tracking of community findings across platforms

See [`docs/how_to_attempt.md`](docs/how_to_attempt.md) for the full methodology.

## Key Links

| Resource | URL |
|----------|-----|
| Official Hub | https://mrbeast.salesforce.com/ |
| 9-Video Playlist | https://www.youtube.com/playlist?list=PLj-VLkYRjRxm5HVGFVpPP5W7jkvvzd1q7 |
| Super Bowl Ad | https://www.youtube.com/watch?v=JBy1T5IykkU |
| Official Hints | [hints/](hints/) |
| All Puzzle Links | [clues/puzzle_links.md](clues/puzzle_links.md) |

## Timeline

- **Feb 8, 2026:** Super Bowl ad airs, puzzle launches
- **Feb 9, 2026:** Hint #1 released (9-word clue structure, word lengths 5-9-5-7-8-4-9-6-5)
- **Feb 10, 2026:** Hint #2 released (3-hub structure, crossword = Stage 2 key)
- **Feb 11, 2026:** Hint #3 released (Stage 0/1/2/3+ structure, 50 total puzzles)
- **Daily:** Hints continue to drop as needed
- **Apr 2, 2026:** Contest deadline

---

*Built by [@tillo13](https://github.com/tillo13) with Claude Code — experimenting with GitHub + AI as a puzzle-solving platform.*
