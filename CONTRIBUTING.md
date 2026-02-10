# Contributing to the MrBeast Million Dollar Puzzle Hunt

Thanks for joining the hunt! This is a collaborative effort — every clue, theory, and solved puzzle gets us closer to $1M.

## How the Puzzle Works

1. **9 YouTube videos** each have a pinned comment linking to a sub-puzzle
2. Each solved puzzle yields **one word**
3. The 9 words form a **meta-clue** (word lengths: 5, 9, 5, 7, 8, 4, 9, 6, 5)
4. The meta-clue is an INSTRUCTION that leads to a hidden code
5. Slack the code to Jimmy Donaldson to win

The Super Bowl ad contains extraction keys needed to pull answer words from solved puzzles. You can't solve the puzzles in isolation — they're interconnected.

## Ways to Contribute

### Found a clue?
1. [Open a "Clue Found" issue](../../issues/new?template=clue_found.yml)
2. Include screenshots, timestamps, or frame numbers
3. Rate your confidence level

### Solved a puzzle?
1. [Open a "Puzzle Solution" issue](../../issues/new?template=puzzle_solution.yml)
2. Show your work — especially the extraction method
3. Explain how others can verify it

### Have a theory?
1. [Open a "Theory" issue](../../issues/new?template=theory.yml)
2. Include supporting evidence
3. Describe how we could test it

### Want to add code or files?
1. Fork this repo
2. Create a branch: `git checkout -b clue/your-finding`
3. Add your work to the correct directory (see below)
4. Submit a PR

## Where to Put Things

| What you have | Where it goes |
|---------------|---------------|
| Puzzle solution or analysis | `puzzles/XX_name/notes.md` |
| Frame screenshots or extracted images | `clues/super_bowl_ad/` or `clues/teaser_videos/` |
| Community intel or web findings | `sources/<topic>/` |
| Scripts or tools | `scripts/` |
| General documentation | `docs/` |

## Ground Rules

- **Document everything** — screenshots, links, reasoning, timestamps
- **Label theories vs confirmed findings** — don't present guesses as facts
- **Don't delete others' work** — even if you disagree, add your counter-analysis alongside
- **Don't post the final answer publicly** if you find it — the prize goes to the first person who Slacks it
- **Speed matters but accuracy matters more** — a wrong lead wastes everyone's time
- **Be kind** — we're all in this together

## Branch Naming

- `clue/short-description` — new clue or evidence
- `solve/puzzle-N` — puzzle solution attempt
- `theory/short-description` — a theory with supporting evidence
- `fix/short-description` — repo fixes, typos, structure improvements

## The Puzzle Platforms

Each puzzle lives on a different platform under the account **BeastForce67**:

| # | Platform | Link |
|---|----------|------|
| 1 | Pinterest | https://pin.it/3DIjEcxdY |
| 2 | Reddit | https://www.reddit.com/user/BeastForce67/comments/1qxxmdn/puzzle/ |
| 3 | Imgur | https://imgur.com/gallery/puzzle-mD2eHYD |
| 4 | ImageShack | https://imageshack.com/user/BeastForce67 |
| 5 | Photobucket | https://photobucket.com/share/753ba093-2a25-4fd1-a061-5d199c5bda49 |
| 6 | Medium | https://medium.com/@beastforce67/puzzle-1a6600218fd0 |
| 7 | Pixelfed | https://pixelfed.social/BeastForce67 |
| 8 | imgpile | https://imgpile.com/u/beastforce67 |
| 9 | 500px | https://500px.com/p/beastforce67 |

## Using AI Tools

This repo is designed to work with Claude Code and other AI assistants. The `CLAUDE.md` file contains instructions for AI agents. The `docs/how_to_attempt.md` file is a complete battle plan that can be fed directly to an AI.

If you use AI to find clues, please note that in your PR/issue so others can evaluate the methodology.

## Questions?

Open a Discussion (if enabled) or an issue tagged with `question`.

---

*Let's go get that million dollars.*
