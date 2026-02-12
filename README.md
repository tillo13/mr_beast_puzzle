# MrBeast Million Dollar Puzzle — Monitoring the Meta-Game

**The community has solved most puzzles. That's not the endgame.**

This repo documents an AI-assisted approach to the [MrBeast x Salesforce Million Dollar Puzzle](https://mrbeast.salesforce.com/) (Super Bowl LX, Feb 2026) — but the real insight isn't in the puzzle solutions, it's in **understanding how Jimmy builds the puzzle in real-time**.

---

## 🎮 The Core Insight: Adaptive Puzzle Design

**Jimmy doesn't have the full puzzle pre-baked. He's building it dynamically based on community progress.**

### Evidence from Hint #3 (Feb 11):

> **"On Reddit, Slack, Discord, and anywhere else public that you've been working, we've been checking in on everything you've solved."**
>
> **"We've seen a whole lot of stuff get crushed by giant groups of solvers."**
>
> **"So it's time to start adjusting what you can see."**

That last line is the key: **"adjusting what you can see."** Jimmy explicitly announced he's pivoting the puzzle based on community velocity. This is his MO from challenge videos — he announces rule changes mid-stream, adapts based on how contestants/audience react, and optimizes for entertainment.

**Three hints in three days** (Feb 9-11) = rapid iteration based on observed community progress. The community solved all 9 Stage 0 puzzles in 3 days (probably expected to take 2-3 weeks), so Jimmy added 40+ "gift puzzles," revealed a Stage 0/1/2/3+ structure, and gated progress with a crossword.

### Why This Matters:

- **Signal vs noise is dynamic** — Today's decorative detail could become tomorrow's puzzle mechanism if community latches onto it
- **Trending discoveries influence future stages** — Jimmy's watching what goes viral on Reddit/Discord
- **Crossword clues are populating dynamically** — Not all pre-written on Feb 8
- **The puzzle is being CO-CREATED** by the community's exploration patterns

This isn't fraud — the $1M is real, someone will win by April 2. But the path to winning is being written NOW, not predetermined.

---

## 🔍 What This Repo Does

Instead of grinding every puzzle detail, this project focuses on:

1. **Monitoring for pivots** — What signals indicate Jimmy's adapting the puzzle?
2. **Technical infrastructure** — Frame extraction, video analysis pipelines, data aggregation
3. **Meta-game analysis** — Understanding Jimmy's design patterns from his challenge videos
4. **Community intel synthesis** — Tracking what's trending across platforms

### Technical Capabilities Demonstrated:

- **Automated video analysis** — Frame extraction at 2fps/4fps, Qwen vision LLM for frame-by-frame analysis
- **Data aggregation** — Pulling clues from Reddit, Discord, Google Docs, community PDFs
- **HAR file analysis** — Discovered hidden API endpoints (Slackbot, Vault, Insights) not visible in web UI
- **Systematic documentation** — Structured state tracking, findings index, answer keys

### The Angle:

Most solvers are brute-forcing puzzles. This repo explores **strategic positioning** — watching for shifts, understanding when to commit energy, and recognizing what matters vs what's noise.

---

## 🌐 Community Resources (Where the Real Work Is)

The community has crushed most puzzles. If you want answers, check these sources:

- **Community Google Doc:** https://bris.kr/qo (collaborative crossword solving, confirmed answers)
- **"The Mr. Beast Files" PDF:** 102+ page community compilation (all 9 puzzle solutions, location theories)
- **Reddit Megathread:** r/ARG and r/MrBeast puzzle discussions
- **Discord:** Lone Shark Games server

### What the Community Has Solved (as of Feb 11):

All 9 Stage 0 puzzle answers are known:
- **EVERY** (Wells in Africa)
- **CHALLENGE** (Life Change Sudoku)
- **LEADS** (Dirtiest Beach)
- **TOWARDS** (Experiences)
- **LOCATION** (Pokemon GO)
- **NAME** (Wilderness)
- **SOMEWHERE** (Adopted Dogs)
- **AROUND** (Pyramids)
- **WORLD** (Circle)

**Meta-clue:** "EVERY CHALLENGE LEADS TOWARDS [A] LOCATION NAME SOMEWHERE AROUND [THE] WORLD"

But this is an **instruction**, not the final answer. The real puzzle is figuring out what location, and what code to submit.

---

## 🎯 Current Stage (as of Feb 11)

### Stage Structure (per Hint #3):

- ✅ **Stage 0:** 9 playlist puzzles → established answer type
- 🔄 **Stage 1:** 50 total puzzles (site + Inside the Beast video + social + gifts)
- 🔥 **Stage 2:** Crossword (25×25 grid, 176 entries, clues populating dynamically)
- ⬜ **Stage 3+:** Unknown (at least one more stage exists)

### Where Effort Should Focus:

1. **Crossword clue population** — Monitor for new clues appearing
2. **"Gift puzzles" discovery** — Jimmy gave gifts to friends with embedded puzzles
3. **Watching for Hint #4** — Next pivot signal (probably drops by Feb 15-18 if progress stalls)
4. **Community trend analysis** — What discoveries are going viral? (Jimmy's watching same sources)

---

## 🧠 Why It's Still Fun (Even With Answers Out There)

This puzzle is like a **real-world escape room**:
- Someone might post the solution online
- But figuring out HOW they got there is the fun part
- And in this case, the "how" is still being written

The interesting challenge isn't "what's the answer" — it's:
- **When does noise become signal?** (Vault rim analysis, monitor symbols, elephant codes)
- **What will Jimmy activate next?** (Stage 3 mechanics)
- **How do trending discoveries influence puzzle design?** (Co-creation)

This is a **meta-puzzle about puzzle design itself.**

---

## 📊 What's Shared Here

This repo contains:

### Documentation:
- **Official hints:** [`hints/`](hints/) — Hint #1, #2, #3 full text
- **Puzzle links:** [`clues/puzzle_links.md`](clues/puzzle_links.md) — All 9 platforms with pinned comments
- **Video transcripts:** VTT subtitles for Super Bowl ad, bank heist, rewatch, playlist videos

### Tools:
- **Video analysis scripts:** Frame extraction, Qwen vision LLM integration
- **Source monitoring:** Automated tracking of Reddit, Discord, community docs
- **HAR analysis tools:** API endpoint discovery

### Analysis:
- **Community intel synthesis:** What's trending across platforms
- **Pivot detection:** Tracking Jimmy's adaptations via hints
- **Meta-game theory:** How Jimmy designs challenges (from his videos)

### What's NOT Here:
- **Private competitive advantages:** Slackbot hidden API details, unique discoveries
- **Over-committed theories:** Not burning energy on unconfirmed extraction methods
- **Noise documentation:** Only high-signal findings (we don't document every frame detail)

---

## 🤝 Want to Collaborate?

This repo is part of the collaborative spirit encouraged by the organizers. Here's how to connect:

- **Open an issue** — Share a finding, discuss theories, or ask about methodology
- **Open a PR** — Contribute tools, analysis, or community intel
- **Fork and experiment** — Run your own AI agents with Claude Code using `CLAUDE.md`

### Collaboration Philosophy:

- **High-visibility discoveries influence the puzzle** — Trending = what Jimmy leans into
- **Share public findings** — Vault rim patterns, monitor symbols, crossword progress
- **Keep private advantages** — Hidden API access, unique infrastructure
- **Contribute to community resources** — Google Doc, Reddit threads, Discord

---

## 🔧 Technical Stack

### Infrastructure:
- **Claude Code** (Sonnet 4.5) — Primary AI agent
- **Qwen Vision LLM** — Frame-by-frame video analysis
- **yt-dlp** — Video downloads (4K when available)
- **ffmpeg** — Frame extraction at 2fps/4fps
- **HAR file capture** — API endpoint discovery

### Techniques:
- **Parallel agent strategy** — Multiple angles on same problem
- **Structured state management** — Single source of truth across sessions
- **Community intel synthesis** — Aggregating across platforms
- **Pivot detection** — Monitoring hints for adaptation signals

---

## 📋 Key Links

| Resource | URL |
|----------|-----|
| Official Hub | https://mrbeast.salesforce.com/ |
| 9-Video Playlist | https://www.youtube.com/playlist?list=PLj-VLkYRjRxm5HVGFVpPP5W7jkvvzd1q7 |
| Super Bowl Ad | https://www.youtube.com/watch?v=JBy1T5IykkU |
| Community Google Doc | https://bris.kr/qo |
| Official Hints | [hints/](hints/) |
| All Puzzle Links | [clues/puzzle_links.md](clues/puzzle_links.md) |

---

## 🎬 The Jimmy MO Pattern

Understanding this puzzle requires understanding how Jimmy runs challenges:

### From His Videos:
- **"Last To Leave Circle"** → Changed rules 3x mid-stream ("new rule!", "we're moving inside")
- **"$1 vs $500K Hotel"** → Extended from 24h to 3 days based on how it was going
- **"100 People in Circle"** → Evolved from elimination to voting to challenge rounds

### Applied to Puzzle:
- **Day 3:** Community solved too fast → **Hint #3 adds 40 puzzles + Stage structure**
- **Future:** Crossword clues populate based on what community already found
- **Stage 3:** Mechanics will incorporate whatever discoveries trend (vault rim? symbols?)

**He told us explicitly:** "So it's time to start adjusting what you can see."

---

## 🎯 Bottom Line

**This repo isn't about having the answers. It's about understanding the game.**

- Community has most puzzle solutions → Check Google Doc / PDF
- This repo focuses on the **meta-game** → Monitoring shifts, watching for pivots
- Technical infrastructure → Video analysis, data aggregation, API discovery
- Strategic positioning → When to commit energy, what to document, how to influence

**The differentiator:** Most solvers are grinding puzzles. This project watches Jimmy's design process in real-time and adapts strategy accordingly.

---

## 📈 Timeline

- **Feb 8, 2026:** Super Bowl ad airs, puzzle launches
- **Feb 9, 2026:** Hint #1 (9-word structure) → Community not finding meta-clue fast enough
- **Feb 10, 2026:** Hint #2 (crossword revealed) → Community solved 9 words too fast
- **Feb 11, 2026:** Hint #3 (Stage 0/1/2/3+ structure, 50 puzzles) → **Explicit adaptation announced**
- **Feb 12+:** Monitoring for Hint #4 and crossword clue population
- **Apr 2, 2026:** Contest deadline

---

## 🚀 About

Built by [@tillo13](https://github.com/tillo13) with Claude Code — an experiment in:
- AI-assisted puzzle solving
- Meta-game analysis
- Understanding adaptive game design
- Technical infrastructure for data aggregation

**Portfolio piece demonstrating:** Systems thinking, video analysis pipelines, community intelligence synthesis, strategic positioning, and Claude Code agent coordination.

---

*"So it's time to start adjusting what you can see."* — Hint #3
