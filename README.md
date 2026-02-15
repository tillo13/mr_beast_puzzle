# MrBeast Million Dollar Puzzle — A Father-Son AI Project

My son and I are working on the [MrBeast x Salesforce Million Dollar Puzzle](https://mrbeast.salesforce.com/) together — he's a huge MrBeast fan, I enjoy puzzles and have some background in Salesforce/Slack. We didn't think much of the Super Bowl ad at first, but he caught it again the next day and we got to work.

This has turned into a genuinely fun project for us. He brings the pattern recognition from years of watching MrBeast challenge videos ("Dad, he ALWAYS changes the rules mid-stream"), and I bring the technical side — AI tools, GitHub repos, Salesforce platform knowledge. It's a good excuse to spend time together and learn things along the way.

This repo is our public workspace. We use AI (Claude, Qwen Vision, local LLMs) to help with analysis, monitoring, and documentation. It's a practical exercise in agentic AI workflows applied to a real problem, and we're sharing what we can in case it's useful to other solvers.

---

## 📅 Progress Updates

### Feb 14 — Six hints in, crossword is the gate

47 days remain until the April 2 deadline. The organizers have been releasing daily hints, and the puzzle structure is now fairly clear:

- **Hint #4 (Feb 12):** Slackbot announced to all players. A second AI called "Beastbot" lives inside Puzzle Cards.
- **Hint #5 (Feb 13):** Card submissions confirmed working.
- **Hint #6 (Feb 14):** All stage 1 clues are now released. 60 total puzzles across multiple categories (commercial, bank video, gifts, YouTube shorts, site/social, Lone Shark social).

Community progress on the crossword:
- 48 of 188 clues revealed so far, ~69 answers filled collaboratively
- 11 soup names found hidden in theme entries (STEW, TAGINE, BROTH, RAMEN, UDON, MISO, CURRY, PHO, GUMBO, STOCK, SOUP) — the crossword commemorates Super Bowl Sunday with a "SOUPERBOWLSUNDAY" pun
- A mini crossword of the 11 interlocking soups is printed on the PDF
- 16 circled cells in the main grid likely feed into a later stage

### Feb 12 — The adaptive puzzle theory

My son pointed out something that keeps proving true: MrBeast runs this puzzle the same way he runs challenge videos. He watches community progress and adjusts. Hint #3 said it directly: "So it's time to start adjusting what you can see."

Three hints in three days (Feb 9-11), then three more (Feb 12-14). That's iteration based on observed progress, not a pre-planned schedule. The community solved all 9 Stage 0 puzzles in about 3 days, which was probably faster than expected — so the organizers added structure (stages), new puzzle categories (gifts), and a crossword gate.


## 🎮 Adaptive Puzzle Design

One observation that's held up across 6 hints: the puzzle appears to be evolving based on community progress. Hint #3 said it directly:

> "We've been checking in on everything you've solved... So it's time to start adjusting what you can see."

This matters practically — what's noise today could become a real mechanism tomorrow if the community latches onto it. The crossword clues have been populating over time (went from 1 revealed clue to 48 in a few days), and new puzzle categories keep appearing.

---

## 🤖 How We Use AI

We use AI tools to help with the heavy lifting — monitoring community sources, analyzing video frames, tracking crossword progress, and keeping organized documentation across sessions. The tools:

- **Claude** (Anthropic) — Primary analysis, code generation, puzzle-solving assistance
- **Qwen Vision** (via LM Studio) — Frame-by-frame video analysis for visual clues
- **Local LLMs** (Ollama/LM Studio) — Lower-latency tasks, change detection
- **GitHub** — Version control, state tracking across sessions, collaboration

This is a practical exercise in using AI tools on a real problem. It's also been a good way to learn about agentic workflows, Salesforce/Slack APIs, and collaborative puzzle-solving with my son.

---

## 🔍 What This Repo Contains

- **Community monitoring** — Tracking crossword progress, new hints, community discoveries
- **Video analysis** — Frame extraction (ffmpeg at 2-4fps), vision LLM analysis of visual clues
- **Platform exploration** — The puzzle runs on Salesforce with a Slack submission mechanism. Some Salesforce/Slack knowledge has been useful.
- **Structured documentation** — State tracking across sessions, organized findings

The Salesforce/Slack platform is explicitly part of the puzzle — the final submission goes via Slack to MrBeast, and an AI Slackbot is available to help solvers. Per [ARGNet](https://www.argn.com/2026/02/start_slacking_off_with_mrbeasts_million_dollar_puzzle_hunt/): "Salesforce's AI agent Slackbot will eventually be activated to help people solve certain parts of the puzzle."

---

## 🎯 Current Stage (as of Feb 14)

### Stage Structure (per Hints #3, #6):

- ✅ **Stage 0:** 9 playlist puzzles — answer type established (words, not locations per Hint #6)
- ✅ **Stage 1:** 60 total puzzles — all clues now released
- 🔥 **Stage 2:** Crossword (25x25 grid, 188 entries, 48 clues revealed, ~69 community answers)
- ⬜ **Stage 3+:** Unknown (at least one more stage exists)

### Community-Solved Stage 0 Answers:

All 9 words are known: **EVERY CHALLENGE LEADS TOWARDS LOCATION NAME SOMEWHERE AROUND WORLD**

This forms an instruction, not the final answer. The actual answer is a code derived through the crossword extraction mechanism.

---

## 📂 What's In This Repo

- Official hints ([`hints/`](hints/) — #1 through #6)
- All 9 puzzle links with pinned comments ([`clues/puzzle_links.md`](clues/puzzle_links.md))
- Video transcripts (VTT subtitles for Super Bowl ad, bank heist, rewatch, playlist videos)
- Video analysis scripts (frame extraction, vision LLM integration)
- Source monitoring tools

**Not included:** Extraction analysis, solver scripts, Slackbot logs, and some competitive findings stay private while the puzzle is active. Happy to share more after the deadline or with collaborators.

---

## 🌐 Community Resources

The community has been great. Key sources if you're working on this:

- **Reddit:** [r/ARG](https://www.reddit.com/r/ARG/), [r/MrBeast](https://www.reddit.com/r/MrBeast/)
- **Discord:** [Lone Shark Games Server](https://lonesharkgames.com/discord/)
- **ARGNet:** [Start Slacking Off with MrBeast's Million Dollar Puzzle Hunt](https://www.argn.com/2026/02/start_slacking_off_with_mrbeasts_million_dollar_puzzle_hunt/)
- **beastforce.fun** — Community crossword solver with voting

---

## 📋 Key Links

| Resource | URL |
|----------|-----|
| Official Hub | https://mrbeast.salesforce.com/ |
| 9-Video Playlist | https://www.youtube.com/playlist?list=PLj-VLkYRjRxm5HVGFVpPP5W7jkvvzd1q7 |
| Super Bowl Ad | https://www.youtube.com/watch?v=JBy1T5IykkU |
| Lone Shark Games Discord | https://lonesharkgames.com/discord/ |
| ARGNet Article | https://www.argn.com/2026/02/start_slacking_off_with_mrbeasts_million_dollar_puzzle_hunt/ |
| r/ARG Subreddit | https://www.reddit.com/r/ARG/ |
| r/MrBeast Subreddit | https://www.reddit.com/r/MrBeast/ |
| Official Hints | [hints/](hints/) |
| All Puzzle Links | [clues/puzzle_links.md](clues/puzzle_links.md) |

---

## 📈 Timeline

- **Feb 8, 2026:** Super Bowl ad airs, puzzle launches
- **Feb 9:** Hint #1 — 9-word meta-clue structure revealed
- **Feb 10:** Hint #2 — Crossword revealed, monitor-bank mapping
- **Feb 11:** Hint #3 — Stage structure (0/1/2/3+), 50+ puzzles, "adjusting what you can see"
- **Feb 12:** Hint #4 — Slackbot publicly announced, Beastbot revealed
- **Feb 13:** Hint #5 — Card submissions working
- **Feb 14:** Hint #6 — All stage 1 clues released, 60 total puzzles, Puzzle Cards are "a key to what happens next"
- **Apr 2, 2026:** Contest deadline

---

## 🤝 Collaboration

Open an issue if you want to discuss theories, share findings, or talk methodology. PRs welcome for tools or community intel. This is meant to be a fun project — we're enjoying the process regardless of the outcome.

---

## 🚀 About

Built by [@tillo13](https://github.com/tillo13) and son. A father-son project combining:
- AI-assisted puzzle solving (Claude, Qwen Vision, local LLMs)
- Salesforce/Slack platform exploration
- GitHub-based state tracking and documentation
- Video frame analysis and community monitoring

We're learning a lot about agentic AI workflows, collaborative puzzle-solving, and how MrBeast designs challenges. It's been a great project to work on together.

---

*"So it's time to start adjusting what you can see."* — Hint #3
