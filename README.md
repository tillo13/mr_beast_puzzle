# MrBeast Million Dollar Puzzle — Agentic AI Meets Real-World Puzzle Solving

A practical exercise in **agentic AI architecture** applied to a live, evolving problem: the [MrBeast x Salesforce Million Dollar Puzzle](https://mrbeast.salesforce.com/) (Super Bowl LX, Feb 2026). Multiple autonomous agents monitor community sources, detect changes, cross-reference findings, and synthesize what matters — all orchestrated through Claude Code with persistent memory and git-based state tracking.

Also a father-son project. My son's a huge MrBeast fan and brings genuine pattern recognition from years of watching challenge videos ("Dad, he ALWAYS changes the rules mid-stream"). I bring the engineering. It's been a great excuse to build something real together.

---

## Why This Project

About a week in, we figured out something obvious: we can't compete with the awesome people who solve puzzles with large teams for a living. These folks are organized, dedicated, and really good at what they do.

But that realization made the project *more* interesting, not less. The puzzle became a perfect domain for building and testing agentic AI patterns:

- **Multi-source monitoring** — agents watching Reddit, Google Docs, Discord, community solvers, wikis, and news sites for changes
- **Change detection and diffing** — automated comparison against known state, flagging what's actually new vs. noise
- **Cross-referencing** — new findings get checked against all existing knowledge before surfacing
- **Session-based orchestration** — Claude Code with `CLAUDE.md` instructions, persistent memory across sessions, and structured state files
- **Git as the state machine** — two-repo architecture (private working repo + public sharing repo) with whitelist-based sync scripts and secrets scanning
- **Signal vs. noise at scale** — when a million dollars is involved, community intel is a mix of genuine discoveries and deliberate misdirection. The agents help separate the two.

The puzzle itself is adaptive — MrBeast and Lone Shark Games are watching community progress and adjusting what's visible. That means the problem space is non-stationary, which makes it a genuinely interesting test for agentic systems.

---

## The Agentic Stack

| Layer | What It Does |
|-------|-------------|
| **Orchestration** | Claude Code (Anthropic) — session-based agent with tool use, persistent memory via `CLAUDE.md` + memory files, structured state tracking |
| **Monitoring** | Python scrapers (PRAW for Reddit, BeautifulSoup/requests for web sources) running on schedule, diffing against snapshots |
| **Analysis** | Cross-referencing pipeline — new findings checked against master knowledge base, puzzle constraints, and community consensus |
| **Vision** | Qwen2.5-VL (via LM Studio) for video frame analysis — extracting visual clues from MrBeast videos at 2-4fps |
| **State** | JSON state files + markdown docs in git — source of truth across sessions, with structured update protocols |
| **Sync** | Whitelist-based repo sync with secrets scanner — automated safe sharing from private working repo to public |

### Patterns Worth Noting

- **CLAUDE.md as agent instructions** — the repo's `CLAUDE.md` file acts as persistent context for every Claude Code session: what to read first, what to work on, what tools are available, what not to do. It's like a `.env` for agent behavior.
- **Two-repo architecture** — private repo has competitive findings and analysis methods; public repo gets curated summaries via `sync_to_public.sh` (whitelist + secrets scanner). The sync script blocks if forbidden patterns are detected.
- **Skill-based workflows** — custom slash commands (`/puzzle-startup`, `/check-community`, `/cross-ref`) encapsulate multi-step agentic workflows that would otherwise require manual orchestration each session.
- **Memory across sessions** — structured memory files persist learnings across conversation windows. The agent reads previous findings at startup and builds on them rather than starting fresh.

---

## What the Community Has Found (as of Feb 17)

This is what our monitoring agents have gathered from community sources. None of this is confirmed by MrBeast unless noted. Data may be stale — when a million dollars is on the line, nobody serious is sharing real-time findings.

### Puzzle Structure
- **Stage 0:** 9 playlist puzzles — answer words form a meta-clue instruction
- **Stage 1:** 50+ puzzles across commercial, bank video, gifts, social media — all clues released as of Hint #6
- **Stage 2:** A 25x25 crossword (188 entries) — community has ~74 answers
- **Phase 2:** Beast Travel (https://beast.travel/) — 8 puzzles involving 12-letter words and world locations
- **Stage 3+:** Exists but unknown

### Key Community Findings
- 8 official hints released over 9 days, each adjusting the puzzle based on observed progress
- 11 soup names found hidden in crossword theme entries
- 16 circled cells in the main grid feed into a later extraction
- Hint #8: "50 locations + crossword" combine into Beast Travel
- Community crossword solver at [beastforce.fun](https://beastforce.fun) tracks answers with voting
- onemil.xyz — community-driven collaborative puzzle requiring massive participation
- Slackbot and Beastbot available to all registered players for hints

### Beastbot — Question Framing Matters

We've noticed that how you frame your Puzzle Cards matters a lot. Describe what you've *observed*, not what you think the answer is, and Beastbot gives you puzzle-type confirmations and structural hints that are genuinely useful.

A few responses on well-known community topics: **[`beastbot_samples.json`](beastbot_samples.json)**

**If you want to compare notes on Beastbot strategy, open an issue.**

---

## Current Stage (Feb 17)

| Stage | Status | Notes |
|-------|--------|-------|
| Stage 0 | Solved (community) | 9 words forming a meta-clue instruction |
| Stage 1 | All clues released | 50+ puzzles, community solving |
| Stage 2 | Crossword in progress | 188 entries, ~74 answers, extraction mechanism exists |
| Phase 2 | Beast Travel | 8 location puzzles, combinations unsolved |
| Stage 3+ | Unknown | At least one more stage |

**44 days remaining** (deadline: April 2, 2026)

---

## What's In This Repo

- **[`puzzles/`](puzzles/)** — All 9 Stage 0 puzzles + crossword, with notes, solution write-ups, and solver scripts. Browse these to see how each puzzle was approached. **Caveat:** data may be stale — this is a snapshot, not necessarily current truth.
- **[`hints/`](hints/)** — All 8 official hints
- **[`clues/`](clues/)** — Puzzle links with pinned comments, video transcripts (VTT subtitles)
- **[`beastbot_samples.json`](beastbot_samples.json)** — A few Beastbot responses on well-known topics, with notes on why they're interesting
- **[`docs/`](docs/)** — Gameplay theory, adaptive puzzle design analysis

**What's not here:** Some analysis methods and findings stay private while the puzzle is active. Happy to share more after the deadline or with collaborators.

---

## Community Resources

| Resource | URL |
|----------|-----|
| Official Hub | https://mrbeast.salesforce.com/ |
| 9-Video Playlist | https://www.youtube.com/playlist?list=PLj-VLkYRjRxm5HVGFVpPP5W7jkvvzd1q7 |
| Super Bowl Ad | https://www.youtube.com/watch?v=JBy1T5IykkU |
| beastforce.fun | https://beastforce.fun — community crossword solver |
| Lone Shark Games Discord | https://lonesharkgames.com/discord/ |
| ARGNet Article | https://www.argn.com/2026/02/start_slacking_off_with_mrbeasts_million_dollar_puzzle_hunt/ |
| r/ARG | https://www.reddit.com/r/ARG/ |
| r/MrBeast | https://www.reddit.com/r/MrBeast/ |

---

<details>
<summary>Day-by-Day Timeline (Days 1-9)</summary>

### Day 1 — Saturday, Feb 8 (Super Bowl LX)
- Puzzle launches during Super Bowl LX. 4 hub videos go live. Tens of millions visit.

### Day 2 — Sunday, Feb 9
- MrBeast on GMA: "Look for some numbers in photos I took at the Super Bowl"
- "No one has solved it... No one is even close to winning"

### Day 3 — Monday, Feb 10
- **Hint #1** — Meta-clue structure revealed. Community rapidly solves Stage 0.

### Day 4 — Tuesday, Feb 11
- **Hint #2** — Crossword discovered. **Hint #3** — "We've been checking in on everything you've solved"

### Day 5 — Wednesday, Feb 12
- **Hint #4** — Slackbot goes public. Community discovers 11 soups in crossword.

### Day 6 — Thursday, Feb 13
- **Hint #5** — Puzzle Cards become critical.

### Day 7 — Friday, Feb 14
- **Hint #6** — "All the clues for stage 1 are out." 60 total puzzles.

### Day 8 — Saturday, Feb 15
- **Hint #7** — "You need friends for this puzzle. Maybe a million of them."

### Day 9 — Sunday, Feb 16
- **Hint #8** — Beast Travel begins.

</details>

---

## Collaboration

Open an issue to discuss theories, share findings, or talk agentic AI methodology. PRs welcome for tools or community intel.

---

## About

Built by [@tillo13](https://github.com/tillo13) and son. This project started as "let's check out that MrBeast puzzle" and turned into a real-world testbed for multi-agent monitoring, session-based AI orchestration, and collaborative signal detection. The puzzle is fun. The agentic architecture is the real project.
