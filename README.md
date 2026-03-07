# MrBeast Million Dollar Puzzle — Building an Agentic AI to Chase $1,000,000

> **CONCLUDED — March 6, 2026.** Someone won the $1M: https://x.com/MrBeast/status/2029970184887214343
> This is a full retrospective of the agentic AI system we built across 26 days trying to crack it.

---

## How It Started

My son is a huge MrBeast fan. When the million-dollar puzzle dropped during Super Bowl LX on February 8, 2026, he was instantly locked in — watching every video, reading the community Discord, tracking each new hint like it was live sports. He sat down next to me and said: "Dad, he ALWAYS changes the rules mid-stream. That's literally what he does in every challenge." He was right, and that turned out to be one of the most important insights of the whole project.

I loved the idea of an agentic AI helper. I looked at the puzzle for about three days and made an honest assessment: we were never going to out-puzzle the dedicated ARG teams who do this professionally. These groups — Team Omega, various Discord servers — have dozens of organized solvers, shared spreadsheets, years of experience, and full-time attention. We had two people, evenings and weekends, and a lot of curiosity.

But that realization made the project *more* interesting, not less. Instead of trying to solve the puzzle by hand, we asked a different question: **what can an agentic AI system do here that a human team can't?**

The answer, it turned out, was quite a lot: monitor six different community sources simultaneously, send thousands of bot questions systematically with perfect consistency, analyze patterns across 2,100+ interactions without losing track of any of them, maintain perfect memory across 26 days of work, and build new hypotheses each day by standing on the shoulders of everything from the previous sessions — without ever getting tired, forgetting what was asked, or losing track of what we'd already tried.

The puzzle became a live, high-stakes testbed for agentic AI architecture. The $1M prize was real motivation to build it well, iterate fast, and actually care about the results. This repo documents everything we built, every pattern we found, and everything we learned.

---

## The Daily Reality

For 26 days, this wasn't a background side project. It was running every day, for hours on end:

- **Morning:** Check scraper outputs — what changed overnight in the community Google Doc, Reddit, Team Omega's wiki?
- **Midday:** Run a new Beastbot session — 20-100 targeted questions, each on a fresh card, logged automatically
- **Evening:** Analyze the session's responses — categorize by topic, look for patterns, identify what to probe next
- **Night:** Write the next session script, update the CLAUDE.md with new findings, commit everything to git

Claude Code was running throughout all of this. Not as a one-shot assistant but as a persistent collaborator that knew everything we'd done, remembered every response, and could pick up exactly where we left off each time. The combination of structured state files, memory documents, and persistent instruction files meant each session built on the last.

By the end, we had 52 session scripts, 2,100+ logged bot interactions, 6 concurrent monitoring scrapers, a reverse-engineered API client, and a framework for evaluating the quality of information under adversarial conditions.

---

## What We Built

### The Agentic Stack

| Layer | What It Does |
|-------|-------------|
| **Orchestration** | Claude Code with `CLAUDE.md` — session-based agent with persistent instructions, memory files, and skill system |
| **Monitoring** | 6 Python scrapers (Reddit, Google Docs, Team Omega wiki, ARGNet, beastforce.fun, mrbeast.salesforce.com) with snapshot diffing |
| **Bot Interaction** | Reverse-engineered Slackbot/Beastbot API — 52 sessions, 2,100+ logged interactions over 26 days |
| **Session Orchestration** | Per-session Python scripts with automatic human pacing, card creation, CSRF auth, and response logging |
| **Corpus Analysis** | 2,100+ responses categorized by topic, response type, and signal strength — pattern finding at scale |
| **Evidence Tiering** | T1/T2/T3/T4 framework — every piece of information evaluated by actual provenance, not by how much we wanted it to be true |
| **Vision Analysis** | Qwen2.5-VL (via LM Studio) for video frame analysis at 2-4fps — automated visual clue extraction |
| **State Management** | JSON state files + markdown docs committed to git — full diff-able history of every session |
| **Secrets Hygiene** | Whitelist-based repo sync with automatic secrets scanner — two-repo architecture for public/private separation |

---

### Layer 1: CLAUDE.md as the Agent's Brain

The single most important architectural decision was treating `CLAUDE.md` as the agent's persistent operational brain.

Claude Code reads `CLAUDE.md` at the start of every session. It's not a README — it's a living operational document that tells the agent: what stage the puzzle is in right now, what to read first, what the daily workflow is, what mistakes NOT to make, what tools are available, what hypotheses we're currently testing, and what to do next. It's the equivalent of a `.env` file, but for agent behavior — and it evolved with the project every single day.

On Day 1, the CLAUDE.md was a few paragraphs of basic context. By Day 26 (session 52), it was a dense operational document covering:

- **The current code structure hypothesis**: `R62-L39-R05 [ROAMY BLOCK] ACCRA`
- **The 50-character submission limit** discovered empirically by the user
- **Daily submission limits**: 20 per day, resets at midnight Pacific (not UTC)
- **Two-account strategy**: andytillo (primary, 109 cards, creation blocked) vs. kumori (secondary, creation working)
- **Cookie handling rules**: Always use `SlackbotChat.set_cookies_from_string()`, never raw headers
- **API pacing**: 30-64s between ALL operations, empirically proven safe
- **What's been tried**: Full list of submitted codes and their status
- **What to do next**: Step-by-step priorities for the current session

The agent could start a fresh conversation cold and immediately be operating at full operational context — no re-explaining required. This compounding effect is what made 26 days of continuous work possible.

**The pattern:** Agents are stateless by default. Persistent, structured instruction files are what give them continuity. A well-maintained `CLAUDE.md` is worth more than any clever prompt.

---

### Layer 2: The Skills System — Reusable Agent Programs

We built a library of custom slash commands — "skills" — each one a complete multi-step workflow encoded as a markdown file. When invoked (e.g., `/puzzle-startup`), the agent reads the skill file and follows its instructions step-by-step, with all the context-awareness of a full session.

| Skill | What It Does |
|-------|-------------|
| `/puzzle-startup` | Reads all key state files, runs all 6 scrapers, checks community sources, compares against known state, delivers a structured briefing with what changed |
| `/run-session` | The full session workflow: check all intel → cross-reference against known state → generate 10-20 Beastbot questions → ask for cookie → fire the batch with logging |
| `/engage-slackbot` | The complete bot interaction bible: cookie auth, CSRF token extraction, card creation, message framing, pacing rules, what works, what gets blocked, what to never do |
| `/signal-analysis` | Full evidence-tier audit: what do we actually know vs. what are we assuming? Builds the T1/T2/T3/T4 gap map |
| `/cross-ref` | Cross-reference any new finding against all existing knowledge before acting on it — prevents chasing things we already knew or disproved |
| `/check-community` | Run all scrapers, check Reddit/Google Doc/beastforce, diff against snapshots, report only what's genuinely new |
| `/process-video` | Full video pipeline: download via yt-dlp → extract frames with ffmpeg at 2-4fps → analyze with Qwen2.5-VL → cross-reference findings |
| `/har-analysis` | Extract API endpoints, controller IDs, worksheet IDs, and CSRF patterns from browser HAR captures |

The key difference between skills and prompts: **skills are deterministic and improvable**. When we discovered that 30-64 seconds between API calls eliminates rate limiting, we added it to `/engage-slackbot` once. Every future session inherited that knowledge automatically. When we found that lobby context doesn't trigger Beastbot but card context does, we added it to the skill. Every subsequent question went through a card.

Skills encode operational knowledge, not just factual knowledge. They're the difference between an agent that knows something and an agent that consistently does the right thing.

---

### Layer 3: Memory Across Sessions

Claude Code operates within a context window — it doesn't natively remember previous conversations. We solved this with a structured memory architecture:

- **`CLAUDE.md`** — Operational instructions, current hypotheses, daily priorities, what's been tried, what not to do. The agent's working memory.
- **`docs_global/state.json`** — Structured evidence tracking: what's confirmed, what's disproven, what's speculative. Session counters, confidence levels, cross-references.
- **`docs_global/WHERE_WE_ARE.md`** — Daily startup briefing: current stage, active fronts, next actions. Written at the end of each session for the next day's start.
- **`memory/MEMORY.md`** — Auto-maintained memory file. Updated each session with key learnings, pattern discoveries, and corrections to previous beliefs.
- **`tools/slackbot/responses_log.json`** — Every single bot response ever received, structured JSON. 25,000+ lines covering 2,100+ interactions.

At the start of every session, the agent reads these files. At the end, it updates them. The knowledge compounds instead of resetting. By session 52, the agent had a complete operational picture of 26 days of work — every tried code, every confirmed fact, every discarded theory — without us having to re-explain any of it.

The combination of **(persistent instruction file) + (structured state) + (daily briefing doc) + (memory file) + (git history)** produces a system that genuinely builds on its own past work. This is the pattern that makes long-running agentic tasks tractable.

---

### Layer 4: Multi-Source Monitoring (6 Concurrent Scrapers)

Every day, six scrapers ran automatically and committed their diffs to git:

**Reddit (PRAW)** — Monitored r/MrBeast, r/ARG, r/puzzles. PRAW gives structured access to post content, comments, upvotes, and new posts. We diffed against previous snapshots to surface only what actually changed.

**Community Google Doc** — The main collaborative document where solvers shared findings. Scraped on a schedule, compared against the previous version. New paragraphs, edited sections, and added theories all surfaced automatically.

**Team Omega Wiki** — The dedicated ARG team's analysis pages. These were the most technically sophisticated community findings — but also the most likely to contain deliberate misdirection.

**ARGNet** — ARG news coverage and write-ups. Good for understanding the meta-state of community progress without being in the Discord.

**beastforce.fun** — Community crossword solver with vote counts per answer. Useful for tracking which crossword answers had consensus vs. which were contested.

**mrbeast.salesforce.com** — The official puzzle hub. This was the only T1 source we monitored. New hints appeared here first. We checked it on a tight schedule.

Each scraper saved a timestamped snapshot and generated a diff summary. The monitoring pipeline committed to git daily — giving us a full history of what the community discovered and when. When a new hint dropped, we had a comparison point for everything we thought we knew before vs. after.

The monitoring wasn't about outsourcing the answer-finding to community sources. With $1M on the line, we assumed some community intel was deliberately wrong. The scrapers let us catch genuine signal early enough to investigate it ourselves — from official sources — before acting on it.

---

### Layer 5: The Reverse-Engineered Beastbot API

This was the most technically interesting piece of the project, and the one that gave us the biggest edge.

The MrBeast puzzle site (`mrbeast.salesforce.com`) offered players a Slackbot and a Beastbot to ask questions. The UI made it look like a simple chat window. But the site runs on Salesforce Experience Cloud, and by capturing browser HAR files and analyzing the raw network traffic, we found something the UI didn't expose: **a full set of API endpoints for puzzle interaction, hidden from the interface entirely.**

Using HAR analysis, we identified four controller IDs:

| Controller | ID | Purpose |
|-----------|-----|---------|
| Chat | `@udd/01pfm000001Aezs` | Slackbot/Beastbot messaging |
| Vault | `@udd/01pfm000001Aezx` | Puzzle Card CRUD |
| Answers | `@udd/01pfm000001Aezu` | Final answer submissions |
| Insights | `@udd/01pfm000001Aezv` | Player stats and milestones |

We built `slackbot_chat.py` — a Python session client that handles:
- Cookie authentication (Salesforce session cookies, properly set per-domain)
- CSRF token extraction (fetch the page, parse `"csrfToken":"..."` from HTML)
- Apex API calls (POST to `/webruntime/api/apex/execute`)
- Human-paced timing (random delays between every operation)
- Automatic response logging to `responses_log.json`

This let us interact with Slackbot and Beastbot programmatically, at scale, from within the agent workflow — and log every interaction in a structured format for later analysis.

**What we discovered by operating the API directly:**

**Discovery 1: Beastbot only fires in card context, not lobby.**

The visible UI puts players in a global lobby chat. Beastbot — the more puzzle-specific and useful bot — only responds when you're chatting within a specific Puzzle Card. This is completely invisible in the UI. You'd only know it if you looked at what `worksheetId` the API was using. Once we knew this, every single question went through a Puzzle Card. Every session before this discovery was running at about 20% effectiveness.

**Discovery 2: The first message to a fresh card is the best Beastbot trigger.**

Across 2,100+ interactions, Beastbot responded most reliably to the first message on a new card. Follow-up messages in the same card went almost exclusively to Slackbot. This shaped our entire session structure: **one focused question per card, new card for every question, fresh context every time.** We never reused a card unless we were intentionally building on a thread.

**Discovery 3: Card name + notes + answer filled = more Beastbot responses.**

The card context wasn't just the message — it included the card's title, answer field, and notes field. Filling all three with specific, relevant data (not generic text) correlated with higher Beastbot response rates. We started treating card creation as the question framing, not just the message.

**Discovery 4: 30-64 seconds between API calls = zero rate limits. Always.**

We discovered this empirically and the hard way. Early sessions used 8-15 second delays and got rate-limited every 3-4 cards. After switching to `time.sleep(random.uniform(30, 64))` between every operation — card creation, card save, message send — we ran 52 sessions with 2,100+ API calls and were never rate-limited once. This rule went into `/engage-slackbot` and was never violated again.

**Discovery 5: The final answer API returns `success: true` regardless of correctness.**

This was the most critical — and sobering — finding. We'd been treating `success: true` API responses as meaningful signal. They're not. Via HAR analysis of multiple confirmed wrong submissions, we verified that the `submitFinalAnswer` API returns `{"success": true}` for every single submission — correct or wrong. There is no `correct` field. There is no winner flag. The only way to know if you won was to receive a direct message from MrBeast's team.

This meant all 21 of our code submissions had an unknown outcome from the API's perspective. We could have been submitting the right code for days without knowing. This changed how we thought about submissions — from "did it work?" to "fire it and move on."

---

### Layer 6: The Session Scripts — 52 Iterations of the Question Loop

Each "session" was a self-contained Python script that fired a batch of targeted questions. Over 26 days, we wrote 52 of them. They evolved dramatically from first to last.

**Early sessions (1-10):** Exploratory. Broad questions about puzzle structure, crossword mechanics, Beast Travel basics. Long lists of questions, less targeted. Discovery-mode.

**Middle sessions (20-35):** More focused. We'd identified specific gaps and were probing them systematically. Card framing became more sophisticated — specific data in the card notes, discovery-mode message framing ("i found X, is this a puzzle?"). Beastbot trigger rate improved.

**Late sessions (40-52):** Highly targeted. Each session was designed to answer a specific question about the final code structure. Some sessions were pure question-batches (100-200 questions). Some were pure submission sessions (5-10 final answer attempts). Some were both running concurrently — a question session keeping the cookie alive while a submission session piggybacked on it.

A typical session script:

```python
"""
Session 49 — 200 questions targeting Roamy extraction mechanism
Probing: R62/L39/R05 format, L73 fourth segment, Row 22 vs Row 1
Running on kumori account, 30-64s pacing, card context only.
"""

QUESTIONS = [
    {
        "card_name": "r62 l39 r05 combination format",
        "answer": "dashes between segments",
        "notes": "hint 22 says combination lock letters and numbers. car trips = R62, horse = L39, plane = R05",
        "message": "found what looks like a combination: r62-l39-r05. the numbers come from globe trip distances. is this the right format for the lock?"
    },
    # ... 199 more
]

for q in QUESTIONS:
    time.sleep(random.uniform(30, 64))
    card_id = bot.create_card(q["card_name"])
    time.sleep(random.uniform(30, 64))
    bot.save_card(card_id, answer=q["answer"], notes=q["notes"])
    time.sleep(random.uniform(30, 64))
    result = bot.send_message(q["message"], worksheet_id=card_id)
    log_response(result, q)  # writes to responses_log.json immediately
```

Every response was logged immediately after it arrived — not batched. If the script crashed, every response up to that point was preserved. The log was the source of truth, not the terminal.

Between sessions, Claude Code analyzed the responses: what did the bot engage with, what did it deflect, did Beastbot fire on anything? That analysis fed directly into the next session's question list. The feedback loop ran continuously.

---

### Layer 7: Corpus Analysis — Finding Signal in 2,100+ Responses

By session 30, we had enough logged responses to shift from reading individual ones to analyzing patterns. We built a corpus analysis pipeline:

**Step 1 — Categorize every response:**
```
BEASTBOT  — Beastbot responded (highest signal, rarest — ~5% of questions)
DEFLECT   — "I can't confirm or deny..." (active avoidance signal)
ENGAGE    — Substantive response to the question (positive signal, but noisy)
POSITIVE  — Filler phrases ("interesting hypothesis", "reasonable approach") — nearly worthless
```

**Step 2 — Group by topic:**
Every question was tagged with keywords. We grouped responses by topic: EYJAFJALLAJOKULL, L73, ACCRA, final code format, Row 22, combination lock format, etc.

**Step 3 — Look for patterns across volume:**

| Topic | Total Questions | Beastbot | Deflect Rate | Signal |
|-------|----------------|----------|-------------|--------|
| EYJAFJALLAJOKULL | 172 | 9 (5.2%) | Low | STRONG |
| Final code format | 239 | 3 (1.3%) | 51% | Active avoidance |
| ACCRA last part | 87 | 7 (8.0%) | Low | MODERATE |
| L73 fourth segment | 44 | 0 (0%) | Medium | Weak/untested |
| Boat page decode | 31 | 2 (6.5%) | Low | MODERATE |

**Step 4 — Apply the insight:**

The key realization from this analysis: **a single enthusiastic response means almost nothing.** An LLM will mirror your confident framing back at you. What matters is the *pattern* across many independent probes on the same topic with varied framings.

Consistent deflection (51% of final code format questions deflected) = the bot is actively avoiding the topic. Strong signal.

High Beastbot rate (EYJAFJALLAJOKULL at 5.2% vs. baseline ~1%) = something real is there. Moderate signal.

Zero Beastbot across 44 probes on L73 = weak negative signal, but maybe just unframed well.

This is corpus analysis applied to AI bot interactions — the same techniques used for customer feedback analysis, social media monitoring, or survey coding. We were treating the bot responses as a noisy channel and finding the signal through volume and categorization.

---

### Layer 8: The Evidence-Tier Framework

About two weeks in, we identified a fundamental problem: we were treating community claims, bot responses, our own prior analysis, and official hints as if they had roughly equal weight. They don't — not even close.

With $1M on the line:
- Some community posters were deliberately posting wrong theories to slow competitors
- Bot responses were LLM outputs that reflected our confident framings back at us
- Our own prior analysis was colored by weeks of believing certain things
- "Everyone in the Discord agrees" meant nothing about correctness

We built a 4-tier framework that forced us to evaluate every piece of information by its actual provenance:

**T1 — Ground Truth (exactly two sources):**
- Content directly on `mrbeast.salesforce.com` (official hints, puzzle pages as rendered)
- Direct statements from MrBeast or his team in official channels

Nothing else qualifies. Not bot responses. Not API responses. Not community consensus. Not things we'd spent three weeks believing. T1 is what you can read directly on the official page, today.

**T2 — Structurally Derivable:**
Math or logic that follows from T1 alone. The test: "If I removed every community source, every bot response, and every prior analysis — does this still hold from T1 facts alone?" If yes → T2. Show the derivation explicitly.

Example of genuine T2: Hint #22 says "letters and numbers." Hint #21 says "very, very close." Hint #17 says the example row's last part "shows up one more time in the list." From these three: the answer has both letters and numbers (T1 direct), and the 40 Roamy rows chain by sharing a city (T2 derivable from Hint #17 structure).

**T3 — Bot Signal (weak indicator):**
Patterns across 10+ independent bot probes on the same topic. A single response = anecdote. Consistent deflection across 50 probes = weak negative signal. Beastbot fires are the strongest T3 signal — but Beastbot is still an LLM.

**T4 — Community / Conjecture:**
Everything else. Google Docs, Discord, Reddit, any solver group, our own prior sessions when we can't verify the source. Treat as hypothesis to test, never as confirmed fact.

The honest audit of our work around Day 20 revealed something uncomfortable: most of what we "knew" was T4 dressed as T1. The Roamy row ordering, the city extraction rules, the boat page decode text — all T4. The framework forced us to ask: "Can I derive this from official hints alone, without trusting any community source?" If no — it's a hypothesis, not a fact.

This framework transfers directly to any agentic system operating on mixed-quality information. Which is nearly every real-world agentic task.

---

### Layer 9: Two-Repo Architecture + Automated Secrets Hygiene

From day one, we ran two git repos:

**Private repo** (this one, never public during the puzzle):
- Full competitive analysis with commentary
- All 2,100+ bot responses in `responses_log.json`
- Extraction key analysis and hypotheses
- Daily tactical briefing (`WHERE_WE_ARE.md`)
- Full tried-codes list with notes
- Community intel with our assessment of reliability
- Account config files with Salesforce org IDs

**Public repo** ([github.com/tillo13/mr_beast_puzzle](https://github.com/tillo13/mr_beast_puzzle)):
- All official hints (curated from the private repo)
- Methodology documentation (no competitive content)
- Gameplay theory analysis
- Beastbot sample responses (sanitized)
- Scripts and tools (no auth material)

The sync between them ran via `scripts_global/sync_to_public.sh` — a whitelist-based script that only copied specifically listed files, then ran a secrets scanner on the destination. The scanner searched for forbidden patterns: account names, cookie strings, extraction keys, answer words, community doc URLs. If any were found, the script refused to commit.

Over 26 days of daily commits, zero secrets leaked to the public repo. The scanning is what made this reliable — not discipline alone. When you're running fast and it's late at night and you've just had a breakthrough, "I'll remember not to commit that file" is not a safe approach. The scanner enforced it mechanically.

---

## How Far We Got

By session 52, we had established the following with reasonable confidence:

**Confirmed structure (T2-T3):**
```
R62-L39-R05 [ROAMY BLOCK] ACCRA
```

**R62-L39-R05** — The vault combination. Hint #22 confirmed "combination lock, letters AND numbers." The car trips on the Roamy globe produced a right arc of ~62 degrees, horse trips a left arc of ~39 degrees, plane trips a right arc of ~5 degrees. The dash-separated format matched Hint #22's "combination lock" framing and was consistent with bot engagement patterns.

**ACCRA** — The last part. Appeared as the rightmost city in Row 22 of the Roamy grid (Eyjafjallajokull → Castelo Branco → Accra) and was independently bot-confirmed in session 45, question 11, and in multiple subsequent probes. 7 Beastbot responses touched on Accra as a terminal element.

**[ROAMY BLOCK]** — The middle section. This is what we never cracked. Based on Hint #21 ("very, very close" to solvers who'd submitted), it was 22-32 characters, encoding something from the Beast Travel Roamy puzzle's 40-row grid. The community called this "P3.4 — the Start." Team Omega marked it with a ⦻ (unsolved) in their analysis.

**What we submitted:**
21 code candidates across 26 days. Notable attempts:
- `R62-L39-R05 TIJUANA BEATTY YELLOWKNIFE ACCRA` — Row 1 cities
- `R62-L39-R05 YELLOWKNIFE L'ASCENSION MONTREAL ACCRA` — Row 2 cities
- `R62-L39-R05 EYJAFJALLAJOKULL CASTELO BRANCO ACCRA` — Row 22 cities
- `R62-L39-R05 EYJAFJALLAJOKULL AGA ACCRA` — Row 22 with extracted letter code

None won. We consistently had the structure right. The Roamy block was always wrong.

Someone won on March 6, 2026 — three days after Hint #23 said "We've seen Final Answers that give us strong hope." The API gave no correctness signal on his winning submission either. He would have found out by being contacted directly. We still don't know the exact winning code — but we were in the right neighborhood, probably.

---

## What We Learned

### On Agentic AI Architecture

**1. The instruction file is the agent's identity.**

`CLAUDE.md` was more important than any prompt. A well-maintained, specific, operational instruction file lets an agent start every session at full context. It tells the agent not just what to know, but what to *do* — step by step. Vague instructions produce vague agents. Specific, current, operational instructions produce consistent, effective ones.

**2. Skills beat prompts for repeated workflows.**

Encoding a complete workflow as a skill file makes it consistent, improvable, and compounding. When we learned something new — about pacing, about card framing, about evidence quality — we added it to the relevant skill once. Every future session inherited that improvement automatically. Ad-hoc prompting for complex workflows produces ad-hoc and inconsistent results.

**3. Evidence quality matters more than evidence volume.**

We had 2,100+ bot responses. The signal was in maybe 5% of them. The other 95% was an LLM reflecting our framings back at us, or deflecting generically. Volume isn't signal — pattern across independent probes on the same topic is signal. Tier your evidence by actual provenance, not by how much you want a particular answer to be true.

**4. The agent is a hypothesis generator, not a validator.**

Every "confirmation" — from a bot, from community sources, from our own prior work — is a hypothesis to verify, not a known fact. The agent excels at generating things to test. It's poor at confirming things are true. The only ground truth is what you can observe directly from the authoritative source. Everything else is conjecture at some confidence level.

**5. Corpus analysis works for AI bot interactions.**

Treating 2,100 responses as a corpus — categorizing, grouping by topic, looking for pattern distributions — extracted real signal that reading individual responses didn't. This is the same technique used for customer feedback analysis, social media monitoring, or market research. It transfers directly to any domain where you're querying a noisy AI system at scale.

**6. Feedback loops are what make agentic systems compound.**

The daily cycle — run session → analyze responses → identify new questions → write next session → repeat — is what produced compounding progress. Each iteration was informed by everything before it. Without that cycle, we'd have been sending the same questions over and over. With it, each session was more targeted than the last.

**7. Secrets hygiene requires automation, not discipline.**

26 days, daily commits, sensitive API data, account credentials, extraction keys — zero leaks. The whitelist sync + secrets scanner made it structurally impossible to accidentally publish something sensitive. Discipline fails. Automation doesn't sleep.

**8. Git is an underrated tool for agentic state management.**

Every session committed. Every scraper run in history. Every hypothesis, tried code, and discarded theory tracked. When we needed to know exactly what we'd tried three weeks ago, or what the community had claimed on a specific day, it was a `git log` away. Git as state machine for agentic tasks is a pattern that scales to any long-running project.

**9. Two bots, two contexts — read the API, not the UI.**

The UI showed one chat interface. The API had four controllers, two distinct bot personalities, and completely different behavior depending on which worksheet context you sent messages to. Lobby context got Slackbot only. Card context got both Slackbot and Beastbot, with the card's own content informing the response. You couldn't see any of this from the UI. HAR analysis revealed what was actually happening. Always read what the system is actually doing, not just what it shows you.

---

## What's In This Repo

- **[`hints/`](hints/)** — All 23 official hints from `mrbeast.salesforce.com`, exactly as published. The T1 source of truth for everything.
- **[`docs/SIGNAL_ANALYSIS_FRAMEWORK.md`](docs/SIGNAL_ANALYSIS_FRAMEWORK.md)** — The evidence-tier framework (T1/T2/T3/T4) for evaluating information quality in adversarial environments
- **[`docs/gameplay_theory.md`](docs/gameplay_theory.md)** — Analysis of MrBeast's adaptive puzzle design: how the puzzle adjusted in real-time based on community progress
- **[`docs/how_to_attempt.md`](docs/how_to_attempt.md)** — Methodology for approaching a large multi-stage puzzle with AI assistance
- **[`docs/parallel_agent_strategy.md`](docs/parallel_agent_strategy.md)** — Strategy for running multiple agents in parallel on different puzzle sub-problems
- **[`beastbot_samples.json`](beastbot_samples.json)** — Sample Beastbot responses with analysis of what triggered them and why they're interesting
- **[`puzzles/`](puzzles/)** — Stage 0 puzzle notes + crossword analysis (methodology and approach, not final solutions)
- **[`scripts/`](scripts/)** — Utility scripts: video frame extraction, source checking, diff tools

---

## Community Resources

| Resource | URL | Status |
|----------|-----|--------|
| Official Hub | https://mrbeast.salesforce.com/ | Active until Mar 9, 2026 noon PT |
| Winner Announcement | https://x.com/MrBeast/status/2029970184887214343 | Someone won |
| Super Bowl Ad | https://www.youtube.com/watch?v=JBy1T5IykkU | Archived |
| beastforce.fun | https://beastforce.fun | Community crossword solver |
| ARGNet Coverage | https://www.argn.com/2026/02/start_slacking_off_with_mrbeasts_million_dollar_puzzle_hunt/ | Archived |
| Lone Shark Games | https://lonesharkgames.com/ | Puzzle designers |
| r/ARG | https://www.reddit.com/r/ARG/ | Community post-mortem ongoing |

---

## The Honest Bottom Line

We didn't win. someone else did, and they deserved it — they cracked something we never did.

But what we built in 26 days is something we're genuinely proud of. A system that:
- Monitored 6 community sources continuously with automated change detection
- Ran 52 question sessions with 2,100+ logged interactions, all systematically analyzed
- Reverse-engineered a hidden API to access bot functionality the UI didn't expose
- Built and maintained perfect operational memory across a month of daily sessions
- Developed a rigorous evidence-quality framework under real adversarial pressure
- Maintained zero secrets leaks across daily public commits for 26 days

The puzzle was the domain. The agentic architecture is what we actually built.

If you're building agentic systems and want to talk methodology — how to structure persistent instructions, how to build skill-based workflow encoding, how to analyze bot interaction corpora, or how to architect a two-repo secrets-safe workflow — open an issue. This is the kind of thing that's worth talking about.

---

## About

Built by [@tillo13](https://github.com/tillo13) and son. Started as "let's check out that MrBeast puzzle" on Super Bowl Sunday. Became a 26-day exercise in agentic AI architecture, adversarial information analysis, and systematic hypothesis testing — with $1M on the line as the real-world stakes.

We didn't win the money, but we built a fun story.
