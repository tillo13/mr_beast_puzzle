# 🔐 MrBeast Million Dollar Puzzle — AI-Assisted Treasure Hunt

> **$1,000,000 prize. First to crack the code wins. Nobody has solved it yet.**

This repo is a collaborative, AI-assisted attempt to solve the [MrBeast x Salesforce Million Dollar Puzzle](https://mrbeast.salesforce.com/) launched during Super Bowl LX (February 8, 2026).

## 🚀 What is this?

MrBeast aired a Super Bowl ad challenging the world to solve a series of interconnected puzzles designed by [Lone Shark Games](https://shop.lonesharkgames.com/). The first person to crack the hidden code and Slack it to Jimmy Donaldson wins **$1,000,000 cash**.

- **Status:** 🔴 UNSOLVED (as of Feb 9, 2026)
- **Deadline:** April 2, 2026
- **Eligibility:** US, Canada, Mexico (18+)
- **Designed by:** Lone Shark Games (pros behind Wired's manhunt, CAH puzzles)

## 📁 Repo Structure

```
mrbeast_puzzle/
├── README.md                    ← You are here
├── CLAUDE.md                    ← AI agent instructions
│
├── puzzles/                     ← One folder per identified puzzle
│   ├── 01_wells_africa/         ← Puzzle 1
│   ├── 02_lifechange/           ← Puzzle 2: LIFECHANGE Sudoku (solver + image)
│   ├── 03_dirtiest_beach/       ← Puzzle 3
│   ├── ...                      ← Puzzles 4-9
│   └── crossword/               ← Crossword puzzle (video # TBD)
│
├── clues/                       ← Raw clue materials (not puzzle-specific)
│   ├── super_bowl_ad/           ← Frame extractions from the ad
│   ├── teaser_videos/           ← Bank heist, Slack, door gag clues
│   ├── social_media/            ← X/Instagram/TikTok screenshots
│   └── daily_hints/             ← Official hints as they drop
│
├── sources/                     ← External intel & community findings
│   ├── reddit/                  ← BeastForce67 posts, megathreads
│   ├── manifold/                ← Manifold Markets decoded clues
│   └── ...                      ← ARGNet, Lone Shark, Salesforce hub
│
├── scripts/                     ← Shared automation (source monitor, etc.)
│
└── docs/                        ← All documentation & GitHub Pages
    ├── index.html               ← Live puzzle tracker dashboard
    ├── how_to_attempt.md        ← Full battle plan & agent workflow
    ├── nine_word_clue.md        ← Meta-clue assembly tracker
    ├── progress.md              ← Daily progress log
    ├── potential_tools.md       ← Reusable tools catalog
    └── testing_suite_methodology.md
```

## 🧠 The Key Puzzle Structure

The puzzle has a known architecture (from official Hint #1):

1. **9 YouTube videos** in a playlist each have a **pinned comment** linking to a sub-puzzle
2. Each sub-puzzle, when solved, yields **one word**
3. The 9 words form a **meta-clue** with word lengths: **5, 9, 5, 7, 8, 4, 9, 6, 5**
4. That meta-clue "defines the nature of the search" — it tells you what to do NEXT
5. Follow the trail → find the hidden code → Slack it to Jimmy → 💰

## 🔗 Key Links

| Resource | URL |
|----------|-----|
| Official Hub | https://mrbeast.salesforce.com/ |
| Super Bowl Ad | [YouTube - "The Vault"](https://www.youtube.com/results?search_query=salesforce+super+bowl+2026+mrbeast+the+vault) |
| 9-Video Playlist | https://www.youtube.com/playlist?list=PLj-VLkYRjRxm5HVGFVpPP5W7jkvvzd1q7 |
| Bank Heist Teaser | https://www.youtube.com/watch?v=OBQELGS13XA |
| Known Reddit Puzzle | https://www.reddit.com/user/BeastForce67/comments/1qxxmdn/puzzle/ |
| ARGNet Analysis | https://www.argn.com/2026/02/start_slacking_off_with_mrbeasts_million_dollar_puzzle_hunt/ |

## 🤖 Using This with Claude Code

The [`docs/how_to_attempt.md`](docs/how_to_attempt.md) file is designed to be fed directly to Claude Code as an agentic task runner. It contains:

- Prioritized task lists for AI-assisted solving
- All known URLs and entry points
- Frame-by-frame analysis targets for the Super Bowl ad
- AI-specific techniques (OCR, cipher detection, steganography, audio spectrograms)
- Cross-referencing strategies for connecting puzzle pieces
- A daily monitoring checklist

```bash
# Clone and start hunting
git clone https://github.com/tillo13/mr_beast_puzzle.git
cd mr_beast_puzzle
# Feed how_to_attempt.md to Claude Code and start solving!
```

## 🤝 Want to Join the Hunt?

PRs welcome! See **[CONTRIBUTING.md](CONTRIBUTING.md)** for the full guide.

**Quick start:**
1. Fork this repo
2. Pick a puzzle, clue, or theory to investigate
3. Add your findings to the appropriate directory
4. Submit a PR using the template

**Or just open an issue:**
- [Report a clue](../../issues/new?template=clue_found.yml) you found
- [Submit a solution](../../issues/new?template=puzzle_solution.yml) to a puzzle
- [Propose a theory](../../issues/new?template=theory.yml) about how things connect

**Ground rules:**
- Document everything — screenshots, links, reasoning
- Label theories vs. confirmed findings
- Don't delete other people's work, even if you disagree
- Speed matters but accuracy matters more

## 📋 Current Progress

| Puzzle # | Video | Puzzle Type | Solved? | Answer Word |
|----------|-------|-------------|---------|-------------|
| 1 | TBD | TBD | ❌ | _ _ _ _ _ (5) |
| 2 | TBD | TBD | ❌ | _ _ _ _ _ _ _ _ _ (9) |
| 3 | TBD | TBD | ❌ | _ _ _ _ _ (5) |
| 4 | TBD | TBD | ❌ | _ _ _ _ _ _ _ (7) |
| 5 | TBD | TBD | ❌ | _ _ _ _ _ _ _ _ (8) |
| 6 | TBD | TBD | ❌ | _ _ _ _ (4) |
| 7 | TBD | TBD | ❌ | _ _ _ _ _ _ _ _ _ (9) |
| 8 | TBD | TBD | ❌ | _ _ _ _ _ _ (6) |
| 9 | TBD | TBD | ❌ | _ _ _ _ _ (5) |

**9-Word Clue:** `_____ _________ _____ _______ ________ ____ _________ ______ _____`

**Final Code:** ❓

## ⏰ Timeline

- **Dec 29, 2025:** MrBeast tweets Super Bowl commercial idea
- **Jan 2026:** Teaser videos drop with hidden clues
- **Feb 6, 2026:** MrBeast on Tonight Show (possible clues)
- **Feb 8, 2026:** Super Bowl ad airs, puzzle officially launches
- **Feb 9, 2026:** Hint #1 released, GMA appearance with photo hint
- **Feb 10+:** Daily clue drops expected
- **TBD:** Slackbot activated for puzzle assistance
- **Apr 2, 2026:** Contest deadline

---

*Built with 🧠 + 🤖 by [@tillo13](https://github.com/tillo13) and Claude*

*Let's go get that million dollars.*
