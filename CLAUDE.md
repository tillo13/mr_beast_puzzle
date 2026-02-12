# CLAUDE.md

## REPO TYPE: PUBLIC

This repo is **PUBLIC** on GitHub. **NEVER** write answer words, extraction methods, slackbot findings, or competitive advantages here. All sensitive work happens in the private repo.

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

## Directory Structure

```
mrbeast_puzzle/
├── README.md                    # Public overview & collaboration invite
├── CLAUDE.md                    # AI instructions (this file)
├── puzzles/                     # Per-puzzle folders with notes
├── clues/                       # Puzzle links, video transcripts, hints
│   ├── puzzle_links.md
│   ├── daily_hints/
│   ├── hub_videos/              # VTTs + metadata
│   └── playlist_videos/         # VTTs + metadata
├── sources/                     # External intel tracking
├── scripts/                     # Reusable tools
├── docs/                        # Methodology & strategy docs
└── tools/github/                # GitHub automation
```

## Important Entry Points

- Official hub: https://mrbeast.salesforce.com/
- 9-video playlist: https://www.youtube.com/playlist?list=PLj-VLkYRjRxm5HVGFVpPP5W7jkvvzd1q7
- Super Bowl ad: https://www.youtube.com/watch?v=JBy1T5IykkU
- Bank heist teaser: https://www.youtube.com/watch?v=OBQELGS13XA
- Rewatch video (visual-only): https://www.youtube.com/watch?v=8_aIjKi0VLM
- ARGNet analysis: https://www.argn.com/2026/02/start_slacking_off_with_mrbeasts_million_dollar_puzzle_hunt/
- Lone Shark Games Discord: https://lonesharkgames.com/discord/

## Known Red Herrings

- "Red Herring Bank" name in teaser video
- Acrostic in teaser that spells "this means nothing I just wanted to waste your time lol"
- However, even red herring scenes contain real clues (barcode, calendars) — stay thorough
