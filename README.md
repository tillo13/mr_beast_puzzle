## What This Is

I wanted to stress-test GitHub's full toolchain and collaboration potential, and give Claude Code agents some fun things to to to try to max the Claude Max plan. The [MrBeast x Salesforce Million Dollar Puzzle](https://mrbeast.salesforce.com/) (Super Bowl LX, Feb 2026) turned out to be a pretty good use case:

- **Time-bounded** — hard deadline of April 2, 2026
- **Multi-faceted** — 9 sub-puzzles across different platforms, each requiring different techniques
- **Naturally collaborative** — designed so no single person (or Agent stack?) can solve everything alone
- **AI-friendly** — perfect for testing Claude Code and other AI-assisted workflows
- **Real stakes** — there's a $1M prize, which keeps things interesting

The puzzle itself is a multi-step treasure hunt designed by [Lone Shark Games](https://shop.lonesharkgames.com/): 9 YouTube videos link to 9 sub-puzzles, each yielding a word. The 9 words form an instruction that leads to a hidden code. First to Slack the code to MrBeast wins.

## Why GitHub?

The puzzle community is **everywhere** — Reddit threads, Discord servers, ARGNet articles, Twitter/X posts, YouTube comments, TikTok breakdowns — and none of it is centralized. Findings get buried in comment threads, theories get lost across platforms, and there's no single place to track what's been solved, what's been tried, and what's still open.

GitHub solves this naturally:

- **Everything in one place** — puzzle images, solver scripts, analysis notes, community intel, all version-controlled
- **Structure without overhead** — Issues for clues, PRs for solutions, Projects for tracking status across 9 puzzles
- **Built-in collaboration** — fork it, open a PR, leave a comment — no Discord invites or Reddit accounts needed
- **Persistence** — nothing gets buried in a chat scroll; every finding is filed and searchable
- **AI-native** — `CLAUDE.md` gives AI agents full project context; Claude Code can read the repo and contribute directly

This puzzle is scattered across 9 different platforms by design. A GitHub repo is the right tool to pull it all together.

## The GitHub Experiment

This repo uses (or plans to use) the following GitHub features as the **sole project infrastructure**:

| Feature | How It's Used |
|---------|---------------|
| **Issues + Templates** | Clue reports, puzzle solutions, theory proposals — all structured with YAML templates |
| **Pull Requests** | All findings submitted as PRs with review workflows |
| **GitHub Pages** | Live puzzle tracker dashboard at `docs/index.html` |
| **Discussions** | Open-ended brainstorming and strategy talk |
| **Projects** | Kanban board tracking puzzle status across all 9 sub-puzzles |
| **Actions** | Automated source monitoring, daily hint checks |
| **CLAUDE.md** | AI agent instructions — Claude Code reads this file for context |
| **Branch strategy** | `clue/`, `solve/`, `theory/` prefixed branches for organized contributions |

The goal is to see how far GitHub alone can take a fast-moving, multi-person research + problem-solving effort, while pushing Claude Agents locally. Currently debating putting multiple agents on one puzzle versus multiple agents across ALL puzzles, leaning towards the prior.

## Repo Structure

```
mrbeast_puzzle/
├── puzzles/                     # One folder per sub-puzzle (images, solvers, notes)
│   ├── 01_wells_africa/
│   ├── 02_lifechange/           # Sudoku variant — grid solved
│   ├── ...
│   └── 09_circle/
│
├── clues/                       # Raw materials + cross-cutting references
│   ├── super_bowl_ad/           # Ad frames, vault crops, braille crops
│   ├── teaser_videos/           # Rewatch + bank heist frames
│   ├── puzzle_links.md          # All 9 puzzle URLs + pinned comments
│   └── daily_hints/
│
├── sources/                     # External intel (Reddit, ARGNet, community findings)
├── scripts/                     # Automation (source monitors, etc.)
├── results/                     # Just state.json — single source of truth
└── docs/                        # GitHub Pages dashboard + strategy docs
```

## Getting Started

We'd encourage you to start from the source — half the fun is the scavenger hunt itself:

1. Start at the [9-video playlist](https://www.youtube.com/playlist?list=PLj-VLkYRjRxm5HVGFVpPP5W7jkvvzd1q7)
2. Find the **pinned comment** on each video (posted by BeastForce67 accounts)
3. Follow each link to the puzzle on its platform (Pinterest, Reddit, Imgur, Medium, etc.)

That said, all the analysis, solver code, and strategy is right here in the repo — dig around as much as you want. The puzzle URLs are documented in [`clues/puzzle_links.md`](clues/puzzle_links.md).

## Current Puzzle Status

| # | Puzzle | Platform | Status |
|---|--------|----------|--------|
| 1 | Wells/Africa | Pinterest | Solving — drop-quote/crossword clues |
| 2 | LIFECHANGE Sudoku | Reddit | **Grid solved** — extraction unknown |
| 3 | Dirtiest Beach | Imgur | Solving — TV show identification |
| 4 | Experiences | ImageShack | Solving — location/stencil word |
| 5 | Pokemon Go | Photobucket | Solving — cage/crossword grid |
| 6 | Wilderness | Medium | **Grid solved** — Tents & Trees, unique solution found |
| 7 | Adopted Dogs | Pixelfed | Solving — 100-dog visual grid |
| 8 | Pyramids | imgpile | Not started |
| 9 | Circle | 500px | Not started |

### Super Bowl Ad Analysis
| Element | Status |
|---------|--------|
| QR code | **Decoded** → `mrbeast.salesforce.com/bts` |
| Slack emojis | **Identified** — camel, dinosaur, coin, anchor, tent |
| Control room monitors | 9 symbols catalogued, mapping to puzzles unknown |
| Vault rim numbers | Partially read — need MrBeast's Super Bowl photos |
| Braille on blast door | Not decoded |

## Want to Collaborate?

This is an open experiment on two fronts — **the puzzle** and **GitHub as a project platform**. Either angle is a valid reason to jump in.

- Found a clue the community missed? Open an issue.
- Have a better way to use GitHub Actions for this? Open a PR.
- Want to fork it and run your own AI agents against the puzzles? Go for it.
- Downloaded puzzle images and solved something? Share your analysis (not the images) as a PR.

See **[CONTRIBUTING.md](CONTRIBUTING.md)** for structure and conventions.

## Key Links

| Resource | URL |
|----------|-----|
| Official Hub | https://mrbeast.salesforce.com/ |
| 9-Video Playlist | https://www.youtube.com/playlist?list=PLj-VLkYRjRxm5HVGFVpPP5W7jkvvzd1q7 |
| ARGNet Analysis | https://www.argn.com/2026/02/start_slacking_off_with_mrbeasts_million_dollar_puzzle_hunt/ |
| Puzzle Links | [clues/puzzle_links.md](clues/puzzle_links.md) |

## Timeline

- **Feb 8, 2026:** Super Bowl ad airs, puzzle launches
- **Feb 9, 2026:** Hint #1 released (9-word clue structure)
- **Feb 10+:** Daily clue drops expected
- **Apr 2, 2026:** Contest deadline

---

*Built by [@tillo13](https://github.com/tillo13) with Claude Code — experimenting with GitHub as a full project platform.*
