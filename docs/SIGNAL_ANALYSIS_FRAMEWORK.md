# Signal Analysis — Evidence-Tier Framework

*Developed during the MrBeast x Salesforce Million Dollar Puzzle (Feb–Mar 2026). Applies to any domain where you're operating with mixed-quality information sources under adversarial or competitive pressure.*

---

## The Problem

When a large prize is on the line, community information is actively corrupted. Some participants post wrong answers deliberately to slow competitors. Bots are LLMs that reflect your confident hypotheses back at you — not ground truth. Your own prior analysis builds on prior analysis until you're very confident about something that was always speculation. Community consensus is not correctness.

The fix is to evaluate every piece of information by its **actual provenance** — not by how useful it would be if it were true, not by how confident the source sounds, not by how many people agree.

This framework enforces that discipline.

---

## The Four Tiers

### T1 — Ground Truth

**Only two sources qualify:**
1. Content directly on the official source (the authoritative page, rendered and read yourself)
2. Direct statements from the organizers in official channels

**Nothing else is T1.** Not:
- Bot responses (they're LLMs, not oracles)
- API responses (see below)
- Community consensus
- Your own prior analysis
- "Everyone agrees this is right"
- API success/failure signals

**Critical example from this project:** The `submitFinalAnswer` API returned `{"success": true}` for every submission — correct or wrong. We confirmed this via HAR analysis. There was no `correct` field. No winner signal. The API success response was meaningless as evidence. We had been treating `success: true` as positive signal. It wasn't T1. It wasn't even T3. It was noise.

**T1 is what you can read directly on the official page, right now, yourself.**

### T2 — Structurally Derivable

Math or logic that follows from T1 facts alone, without requiring any community source.

**The test:** "If I removed every community source, every bot response, and all prior analysis — does this conclusion still hold from T1 facts alone?"

If yes → T2. Show the derivation explicitly. Don't hand-wave.

**Example of genuine T2 from this project:**
- T1: Hint #22 says "combination lock, letters and numbers"
- T1: Hint #17 says "the last part [of the example row] shows up one more time in the list"
- T2 derived: The answer contains both letters AND numbers (direct from T1). The Roamy rows chain — the last city of row N is the first city of row N+1 (structural implication of Hint #17).

**Example of fake T2:** "The community says R62-L39-R05 and it makes sense given the globe trip directions." → This is T4 community claim + T2-sounding reasoning. Without reading the actual Roamy page yourself and deriving the degree values, it's not T2.

### T3 — Bot Signal (Weak Indicator)

Patterns across **10+ independent bot probes** on the same topic, with varied framings.

- Consistent **DEFLECTION** across 10+ probes → weak negative signal (bot actively avoiding the topic)
- Consistent **ENGAGEMENT** → very weak positive signal (LLMs match confident framings — be careful)
- **Beastbot fires** (puzzle-specific response from the card-context bot) → strongest T3 signal

**Rules:**
- ONE response = anecdote, not evidence. Treat it as a single data point, nothing more.
- "Interesting hypothesis" / "reasonable approach" / "that's a thoughtful angle" = near-worthless filler. The LLM is matching your confidence.
- "I can't confirm or deny" = neutral. Not negative, not positive. The bot deflects this way on everything sensitive.
- Pattern across 50+ independent probes = begins to be meaningful signal
- Contradictions on same topic = noisy channel; probe more, don't resolve by picking the answer you prefer

**From this project:** EYJAFJALLAJOKULL had 9 Beastbot responses across 172 questions (5.2%). Final code format questions were deflected 51% of the time. Those are patterns worth acting on. A single Beastbot response saying "yes this is a puzzle" is not.

### T4 — Community / Conjecture

Everything else. Google Docs, Discord, Reddit, ARG teams, any solver group, your own prior sessions when you can't trace the original source.

**Treat as hypothesis to test. Never as confirmed fact.**

Key question for every T4 claim:
> "Can I verify this from T1/T2 alone, without trusting this source at all?"

If the answer is no — it's T4. Even if 500 people believe it. Even if it "just makes sense." Even if you've been acting on it for two weeks. T4 is T4.

---

## The Honest Audit

Before generating new hypotheses or taking action, run this audit on your current beliefs:

```
=== WHAT WE KNOW (T1/T2) ===
[Only facts that survive the tier check — be strict]
[If you can't cite the official page or show the T1 derivation, it doesn't belong here]

=== WHAT'S PROBABLE (T3) ===
[Topics with 10+ consistent bot responses in the same direction]
[Note the probe count and direction for each]

=== WHAT WE'RE ASSUMING FROM COMMUNITY (T4) ===
[Every key belief that's actually T4 — be ruthlessly honest]
[This is usually most of what you think you know]

=== WHAT'S BEEN DISPROVEN ===
[Tested and failed — what does each failure actually rule out?]
[Note: API success/failure is not proof of correctness/incorrectness — see T1 note above]

=== ACTIVE UNKNOWNS ===
[What we genuinely don't know and need to figure out]
[These are the real questions — not more probes on T1 facts you already have]
```

**The gap map is the most important output of any analysis session.** If a belief is T4, it belongs in the assumptions section — not the knowns section. Running this audit honestly usually reveals that most of what you "know" is actually T4 with a T2 costume on.

---

## Generating Questions Targeting Real Unknowns

Given the gap map, generate probes that target **genuine unknowns** — not things you already know, not things you've probed 30 times already.

**Priority order for new probes:**
1. Questions that could upgrade T4 claims to T2 (structural verification from official source)
2. Questions that probe active unknowns directly
3. Questions that probe T4 claims for bot engagement vs. deflection (T3 signal building)
4. Questions on topics NOT yet probed (check your log first)

**Never generate probes about:**
- Things already probed 3+ times with consistent responses (extract the signal, move on)
- Things that are T1/T2 confirmed (don't need bot validation)
- Things disproven by direct testing

---

## Framing Rules for Bot Probes

- **Discovery framing beats demand framing.** "i found X at Y location, is this a puzzle?" consistently outperforms "confirm that X is relevant."
- **Specific data beats general questions.** "the roamy grid row 22 goes eyjafjallajokull to castelo branco — what connects these?" beats "tell me about row 22."
- **Fresh card per question.** Card context (not lobby) is required for the more specific bot. New card = new context = highest signal rate on first message.
- **Sound like a person.** Lowercase, casual, phone-message energy. No bullet points, no formal phrasing, no mention of "systematic analysis" or "I've investigated."

---

## Mental Model

Think like a detective, not a solver:

- **Evidence has quality levels.** T1 is direct observation. T2 is sound inference. T3 is a pattern in noisy data. T4 is a rumor from someone who might be lying.
- **Pattern across many independent observations > single strong observation.** One Beastbot response means almost nothing. Nine Beastbot responses on the same topic across varied framings means something.
- **An LLM confirming your hypothesis is not evidence.** It's you talking to yourself through a very agreeable mirror. The LLM matches confidence. Don't mistake its matching for validation.
- **A winning answer is proved by winning — nothing else proves it.** In this project, the API gave `success: true` for every submission. The only proof was winning.
- **The agent generates hypotheses. Reality tests them.** Use the agent to produce things to verify from T1 sources. Don't use the agent to confirm that your hypotheses are correct.

---

## Applying This Beyond Puzzles

This framework was built for a puzzle competition, but the core problem — working with mixed-quality information sources, some of which are actively corrupted — is common:

- **Research with LLM assistance:** LLMs hallucinate. Treat their outputs as T4 until verified from primary sources.
- **Market intelligence:** Community rumors, analyst opinions, and competitor intel are all T4. Primary sources (filings, official statements, direct observation) are T1.
- **Agentic systems with multiple data sources:** Not all data sources have equal quality. Build quality tiers into how you treat incoming information. Don't let noisy sources (web scraping, community posts) override clean sources (structured APIs, official docs).
- **Security research:** Community PoCs and writeups are T4. Reproduced in your own environment = T2.

The underlying discipline: **be honest about what you actually know vs. what you're assuming.** The gap map forces that honesty. It usually reveals that your "known" column is much shorter than you thought, and your "assuming" column is much longer. That clarity is where real progress starts.

---

*Built from 26 days of operating under $1M stakes. Every rule in this framework was learned the hard way.*
