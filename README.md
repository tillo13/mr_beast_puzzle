# MrBeast Million Dollar Puzzle — Monitoring the Meta-Game

**The community has solved most puzzles. That's not the endgame.**

This repo documents an AI-assisted approach to the [MrBeast x Salesforce Million Dollar Puzzle](https://mrbeast.salesforce.com/) (Super Bowl LX, Feb 2026) — but the real insight isn't in the puzzle solutions, it's in **understanding how MrBeast builds the puzzle in real-time**.

---

## 📅 2026-02-12 8am Update: What If It's All Noise So Far?

**That's a MrBeast calling card move, right?**

Here's the theory: What if EVERYTHING we've been analyzing (vault rims, monitor symbols, calendar dates, dollar bill sequences) is mostly decorative noise designed to drive engagement and video replays? Not fraud — the $1M is real — but MrBeast is **making it up as he goes** based on community progress, just like he does in challenge videos.

**Context:** My son and I are working on this together — he's a huge MrBeast fan, I love puzzles and Salesforce/Slack tech. We didn't think much of the Super Bowl ad at first, but he caught it again the next day and we got to work. **The "pivot theory" is his.** He watches every MrBeast challenge video and kept pointing out *"Dad, he ALWAYS changes the rules. Remember the circle challenge? The hotel video?"* When Hint #3 dropped with "adjusting what you can see," he called it: **MrBeast is pivoting the puzzle in real-time.**

His pattern recognition (YouTuber behavior, game mechanics) + my technical analysis (Salesforce/Slack platform knowledge) = this repo's approach.

### A Few Thoughts Why:

**1. He literally told us in Hint #3:**
> "We've been checking in on everything you've solved... We've seen a whole lot of stuff get crushed by giant groups of solvers. **So it's time to start adjusting what you can see.**"

"Adjusting what you can see" = **pivoting the puzzle NOW**, not revealing pre-baked content.

**2. It's his MO:**
- "Last To Leave Circle" → Changed rules 3x mid-stream
- "$1 vs $500K Hotel" → Extended from 24h to 3 days
- He ALWAYS announces "new rule!" based on how it's going

**3. Three hints in three days = rapid iteration:**
- Feb 9: Hint #1 (community not finding meta-clue)
- Feb 10: Hint #2 (community solved 9 words too fast)
- Feb 11: Hint #3 (add 40 puzzles + Stage structure)

That's sprint planning, not hint releases.

**4. Community has all 9 answers — but NO WINNER:**
If the puzzle was fully designed on Feb 8, someone would've won by now. Instead, the crossword (Stage 2 gate) has clues "populating as you progress" = being written NOW.

**5. What matters shifts dynamically:**
- Today's noise (vault rim) could be tomorrow's signal if community latches onto it
- MrBeast's watching what trends → incorporates into Stage 3
- **We're CO-CREATING the puzzle** by exploring interesting paths

### What This Means:

The real puzzle isn't "solve the clues" — it's **"understand MrBeast's design process and position yourself for the pivots."**

Most people are grinding vault rim positions. Smarter play: watch for Hint #4, monitor crossword clue population, track what's trending on Reddit/Discord (that's what MrBeast's team is watching).


## 🎮 The Core Insight: Adaptive Puzzle Design

**MrBeast doesn't have the full puzzle pre-baked. He's building it dynamically based on community progress.**

### Evidence from Hint #3 (Feb 11):

> **"On Reddit, Slack, Discord, and anywhere else public that you've been working, we've been checking in on everything you've solved."**
>
> **"We've seen a whole lot of stuff get crushed by giant groups of solvers."**
>
> **"So it's time to start adjusting what you can see."**

That last line is the key: **"adjusting what you can see."** MrBeast explicitly announced he's pivoting the puzzle based on community velocity. This is his MO from challenge videos — he announces rule changes mid-stream, adapts based on how contestants/audience react, and optimizes for entertainment.

**Three hints in three days** (Feb 9-11) = rapid iteration based on observed community progress. The community solved all 9 Stage 0 puzzles in 3 days (probably expected to take 2-3 weeks), so MrBeast added 40+ "gift puzzles," revealed a Stage 0/1/2/3+ structure, and gated progress with a crossword.

### Why This Matters:

- **Signal vs noise is dynamic** — Today's decorative detail could become tomorrow's puzzle mechanism if community latches onto it
- **Trending discoveries influence future stages** — MrBeast's watching what goes viral on Reddit/Discord
- **Crossword clues are populating dynamically** — Not all pre-written on Feb 8
- **The puzzle is being CO-CREATED** by the community's exploration patterns

This isn't fraud — the $1M is real, someone will win by April 2. But the path to winning is being written NOW, not predetermined.

---

## 🤖 The Agentic AI Approach (Our Strategy)

**We're not manually clicking through Reddit threads and Discord channels — we're building an agentic monitoring system.**

Using **multiple LLMs** (Claude Sonnet, Qwen Vision, Llama3 via LMStudio/Ollama) and **agentic orchestration tools** (n8n workflows, LangChain, investigating CrewAI/LlamaIndex patterns), we've automated the heavy lifting:

### How It Works:
- **Agents constantly monitor** community sources (Reddit, Discord, Google Doc, MrBeast socials, puzzle site)
- **LLM parsers analyze** new content: "Signal or noise? Pivot or chatter?"
- **Pattern detection** flags: new hints, crossword clue population, MrBeast language shifts, community breakthroughs
- **We zoom in** when agents surface valid hits — automation handles the noise, we handle the signal

### Why Agentic AI?

**Most solvers:** Manually refreshing 10 tabs, scrolling threads, clicking through posts
**Us:** Agentic system watches 24/7, alerts on high-priority developments

This aligns with **Salesforce's Agentforce vision** — investigating if Agentforce patterns apply here, but primarily using local LLM orchestration (lower latency, full control, no API costs).

**Personal angle:** Building expertise in agentic AI workflows — applicable beyond puzzles to any signal-detection problem in noisy environments.

---

## 🔍 What This Repo Does

Instead of grinding every puzzle detail, this project focuses on:

1. **Agentic monitoring** — Automated agents watch for MrBeast's pivots, community trends, crossword updates
2. **Platform expertise** — Understanding Salesforce/Slack architecture (Agentforce, SFDC patterns, API endpoints)
3. **Technical infrastructure** — Frame extraction, video analysis pipelines, data aggregation
4. **Meta-game analysis** — Understanding MrBeast's design patterns from his challenge videos
5. **Local LLM orchestration** — Multi-agent systems sorting signal from noise

### Why Platform Knowledge Matters:

**MrBeast explicitly said the Salesforce/Slack platform IS part of the puzzle:**

> "Salesforce's AI agent Slackbot will eventually be activated to help people 'solve certain parts of the puzzle,' with users able to ask it questions to help 'point [people] in the right direction.'" — [ARGNet](https://www.argn.com/2026/02/start_slacking_off_with_mrbeasts_million_dollar_puzzle_hunt/)

Based on this, we've found some interesting endpoint data worth exploring. Having a good grasp on SFDC/Slack in general has given us a few tips/tricks/thoughts we're investigating.

The final submission is via **Slack to MrBeast** — not a web form, not email, but Slack. The platform isn't just hosting the puzzle, **it's part of the mechanism**.

### Technical Capabilities Demonstrated:

- **Salesforce/Slack platform expertise** — Understanding SFDC and Slack APIs and endpoints has been pretty interesting...
- **Automated video analysis** — Frame extraction at 2fps/4fps, Qwen vision LLM for frame-by-frame analysis
- **Data aggregation** — Pulling clues from Reddit, Discord, Google Docs, community PDFs
- **Systematic documentation** — Structured state tracking, findings index, answer keys

### The Angle:

Most solvers are brute-forcing puzzles. This repo explores **strategic positioning** — watching for shifts, understanding when to commit energy, and recognizing what matters vs what's noise. Plus: **deep platform knowledge** others don't have.

---

## 🌐 Community Resources (Where the Real Work Is)

The community has crushed most puzzles. If you want answers, check these sources:

- **Community Google Doc:** https://bris.kr/qo (collaborative crossword solving, confirmed answers)
- **"The Mr. Beast Files" PDF:** 102+ page community compilation (all 9 puzzle solutions, location theories)
- **Reddit:**
  - [r/ARG Discussion Thread](https://www.reddit.com/r/ARG/)
  - [r/MrBeast Puzzle Megathread](https://www.reddit.com/r/MrBeast/)
- **Discord:**
  - [Lone Shark Games Server](https://lonesharkgames.com/discord/)
  - Various puzzle-solving community servers
- **ARGNet:** [Start Slacking Off with MrBeast's Million Dollar Puzzle Hunt](https://www.argn.com/2026/02/start_slacking_off_with_mrbeasts_million_dollar_puzzle_hunt/)
- **YouTube:** Community solving videos and livestreams

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
2. **"Gift puzzles" discovery** — MrBeast gave gifts to friends with embedded puzzles
3. **Watching for Hint #4** — Next pivot signal (probably drops by Feb 15-18 if progress stalls)
4. **Community trend analysis** — What discoveries are going viral? (MrBeast's watching same sources)

---

## 🧠 Why It's Still Fun (Even With Answers Out There)

This puzzle is like a **real-world escape room**:
- Someone might post the solution online
- But figuring out HOW they got there is the fun part
- And in this case, the "how" is still being written

The interesting challenge isn't "what's the answer" — it's:
- **When does noise become signal?** (Vault rim analysis, monitor symbols, elephant codes)
- **What will MrBeast activate next?** (Stage 3 mechanics)
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
- **Platform exploration:** SFDC and Slack familiarity

### Analysis:
- **Community intel synthesis:** What's trending across platforms
- **Pivot detection:** Tracking MrBeast's adaptations via hints
- **Meta-game theory:** How MrBeast designs challenges (from his videos)

### What's NOT Here:
- **Deep platform findings:** Years of Salesforce/Slack experience has revealed some interesting patterns — some competitive advantages stay private
- **Over-committed theories:** Not burning energy on unconfirmed extraction methods
- **Noise documentation:** Only high-signal findings (we don't document every frame detail)

---

## 🤝 Want to Collaborate?

This repo is part of the collaborative spirit encouraged by the organizers. Here's how to connect:

- **Open an issue** — Share a finding, discuss theories, or ask about methodology
- **Open a PR** — Contribute tools, analysis, or community intel
- **Fork and experiment** — Run your own AI agents using `CLAUDE.md` for context

### Collaboration Philosophy:

- **High-visibility discoveries influence the puzzle** — Trending = what MrBeast leans into
- **Share public findings** — Vault rim patterns, monitor symbols, crossword progress
- **Platform expertise helps** — Salesforce/Slack background useful for sorting signal from noise
- **Contribute to community resources** — Google Doc, Reddit threads, Discord

---

## 🔧 Technical Stack

### Agentic AI Infrastructure:
- **Local LLM Orchestration** — Claude Sonnet 4.5, Qwen Vision, Llama3 (via LMStudio/Ollama), LocalAI
- **Agentic Frameworks** — Investigating: LangChain, CrewAI, LlamaIndex, AutoGPT patterns for multi-agent coordination
- **Workflow Automation** — n8n for agent orchestration, exploring Prefect/Airflow for scheduled monitoring
- **Automated Monitoring** — Agents watching Reddit, Discord, Google Doc, puzzle site, MrBeast socials
- **Signal Processing** — LLM-based classification: "Is this a pivot? A hint? Community breakthrough? Or noise?"
- **Pattern Detection** — Agents flag: MrBeast pivot language, crossword clue population, trending theories

### Platform Expertise:
- **Salesforce/Slack** — Understanding SFDC and Slack APIs and endpoints has been pretty interesting...
- **Agentforce Investigation** — Exploring if Agentforce patterns apply to puzzle monitoring

### Video Analysis:
- **yt-dlp** — Video downloads (4K when available)
- **ffmpeg** — Frame extraction at 2fps/4fps
- **Qwen Vision LLM** — Frame-by-frame analysis

### Techniques:
- **Agentic workflows** — Automation handles noise, humans handle signal
- **Platform-native exploration** — Using SFDC/Slack architecture knowledge to find structure
- **Structured state management** — Single source of truth across sessions
- **Real-time pivot detection** — Agents alert when MrBeast adapts puzzle

---

## 📋 Key Links

| Resource | URL |
|----------|-----|
| Official Hub | https://mrbeast.salesforce.com/ |
| 9-Video Playlist | https://www.youtube.com/playlist?list=PLj-VLkYRjRxm5HVGFVpPP5W7jkvvzd1q7 |
| Super Bowl Ad | https://www.youtube.com/watch?v=JBy1T5IykkU |
| Community Google Doc | https://bris.kr/qo |
| Lone Shark Games Discord | https://lonesharkgames.com/discord/ |
| ARGNet Article | https://www.argn.com/2026/02/start_slacking_off_with_mrbeasts_million_dollar_puzzle_hunt/ |
| r/ARG Subreddit | https://www.reddit.com/r/ARG/ |
| r/MrBeast Subreddit | https://www.reddit.com/r/MrBeast/ |
| Official Hints | [hints/](hints/) |
| All Puzzle Links | [clues/puzzle_links.md](clues/puzzle_links.md) |

---

## 🎬 The MrBeast MO Pattern

Understanding this puzzle requires understanding how MrBeast runs challenges:

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

**This repo isn't about having the answers. It's about understanding the game — and using agentic AI to watch it in real-time.**

**The Differentiator:**
- **Most solvers:** Manually grinding puzzles, refreshing Reddit threads, scrolling Discord
- **This approach:** Agentic AI system monitors 24/7, surfaces high-priority signals, lets us zoom in on what matters

**What We're Actually Doing:**
- Community has most puzzle solutions → Check Google Doc / PDF
- We're watching the **meta-game** → Automated monitoring for MrBeast's pivots
- Agentic workflows → Automation handles noise, we handle signal
- Platform knowledge → SFDC/Slack understanding reveals structure
- Strategic positioning → Commit energy when agents flag valid hits

**This isn't just puzzle-solving — it's building agentic AI expertise applicable to any signal-detection problem in noisy environments.**

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

Built by [@tillo13](https://github.com/tillo13) — an experiment in **agentic AI workflows**:
- Multi-agent monitoring systems (LangChain, CrewAI, n8n orchestration)
- Local LLM coordination (Claude, Qwen, Llama3, Ollama, LocalAI)
- Signal detection in noisy environments
- Automated intelligence synthesis
- Meta-game analysis and adaptive strategy
- Salesforce/Slack platform patterns (Agentforce investigation)

**Portfolio piece demonstrating:**
- **Agentic AI stack** — LangChain, n8n, CrewAI, LlamaIndex, AutoGPT patterns
- **Local LLM orchestration** — Claude Sonnet, Qwen Vision, Llama3 (LMStudio/Ollama/LocalAI)
- **Workflow automation** — n8n, Prefect, Airflow for scheduled agent monitoring
- **Salesforce/Agentforce alignment** — Investigating agentic workflow patterns for SFDC ecosystem
- **Signal vs noise** — Automated detection in high-volume data streams
- **Platform architecture** — SFDC/Slack API understanding
- **Systems thinking** — Automation handles monitoring, humans handle insights

---

*"So it's time to start adjusting what you can see."* — Hint #3
