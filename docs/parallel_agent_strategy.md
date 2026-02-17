# Parallel Agent Strategy

## Lessons Learned (the hard way)

1. **Agents die.** Every agent from session 2 ran out of context without saving notes. All work was lost.
2. **Save incrementally, not at the end.** If an agent writes findings to disk after every discovery, a context blowout becomes a checkpoint instead of a total loss.
3. **Multiple agents on one puzzle > one agent per puzzle.** Focused collaboration beats shallow coverage. One deep solve is worth more than 9 shallow attempts.
4. **Each agent needs its own file.** Concurrent agents writing to the same file clobber each other.

## Strategy: Multi-Agent Per Puzzle

Instead of spreading 9 agents across 9 puzzles, concentrate multiple agents on ONE puzzle at a time. Each agent attacks a different angle. When that puzzle is cracked, move on.

### File Structure

```
puzzles/XX_name/
├── puzzle.png              # shared input (read-only for agents)
├── scratch_clues.md        # Agent A: crossword/clue solving
├── scratch_grid.md         # Agent B: grid transcription & structure
├── scratch_community.md    # Agent C: web research & community intel
├── scratch_quote.md        # Agent D: quote/phrase guessing
├── scratch_extraction.md   # Agent E: extraction method testing
└── notes.md                # FINAL merged result (orchestrator writes)
```

Agent file names should reflect the agent's **role**, not a number. Pick from the role list or invent one that fits.

### Per-Agent Prompt Template

```
You are solving puzzle #{N} of the MrBeast Million Dollar Puzzle.
Your role: {ROLE} (e.g., "crossword clue solver", "grid transcriber", "community researcher")

YOUR PUZZLE:
- Video: {video_title} ({video_id})
- Platform: {platform}
- Meta-clue position: word #{N} of 9 (expected length: {X} letters)
- Puzzle image: puzzles/{folder}/puzzle.png

YOUR TASK:
1. Read puzzles/shared_context.md for extraction keys from the Super Bowl ad
2. Read puzzles/{folder}/puzzle.png (the puzzle image)
3. Focus on your role: {ROLE_SPECIFIC_INSTRUCTIONS}
4. Write your answer word candidate if you find one

CRITICAL — INCREMENTAL SAVING:
- Write findings to puzzles/{folder}/scratch_{role}.md AFTER EVERY DISCOVERY
- Do NOT wait until the end. Append new sections as you go.
- If you run out of context, another agent will pick up from this file.
- Use clear headers: ## Clue 1, ## Grid Row 3, ## Theory: XYZ, etc.
- Mark confidence levels: CONFIRMED, LIKELY, GUESS, UNVERIFIED

RULES:
- ONLY write to puzzles/{folder}/ — do not touch other puzzle folders
- ONLY write to your scratch file: scratch_{role}.md
- Do NOT write to notes.md (the orchestrator does that)
- Read CLAUDE.md for repo conventions
```

### Role Templates

Pick 3-5 of these per puzzle depending on puzzle type:

| Role | File | What it does |
|------|------|-------------|
| **clues** | `scratch_clues.md` | Solve crossword clues, word puzzles, trivia questions |
| **grid** | `scratch_grid.md` | Transcribe the visual grid, identify structure, map positions |
| **community** | `scratch_community.md` | Web search for community solutions, Reddit/Discord intel |
| **quote** | `scratch_quote.md` | Guess the quote/phrase from partial letters, thematic hints |
| **extraction** | `scratch_extraction.md` | Test extraction methods using Super Bowl ad keys |
| **visual** | `scratch_visual.md` | Analyze images for hidden details, steganography, colors |
| **logic** | `scratch_logic.md` | Constraint solving (sudoku, tents, cages, etc.) |
| **research** | `scratch_research.md` | Look up references, identify TV shows/songs/places |

### Agent Count Per Puzzle Type

| Puzzle Type | Recommended Agents | Roles |
|-------------|-------------------|-------|
| Crossword / drop-quote | 4 | clues, grid, quote, community |
| Sudoku / logic grid | 3 | grid, logic, extraction |
| Visual identification | 3 | visual, research, community |
| Word puzzle / cipher | 3 | grid, clues, extraction |

## Orchestrator Role

The orchestrator (human or main agent window) does NOT solve — it coordinates:

1. **Before launch:** Write `puzzles/shared_context.md` with all known extraction keys
2. **Launch agents** with role-specific prompts (stagger by ~30s if rate-limited)
3. **Monitor scratch files** — check `puzzles/XX_*/scratch_*.md` periodically
4. **When agents finish (or die):** Read all scratch files, merge into `notes.md`
5. **Cross-reference** findings between puzzles for extraction clues
6. **Update** `results/state.json` with puzzle status
7. **Decide next puzzle** to attack with the multi-agent approach

### Merging Scratch Files into notes.md

```
# Puzzle #N — {Name}

## Source
(from shared_context.md)

## Puzzle Type
(from scratch_grid.md)

## Grid / Structure
(from scratch_grid.md)

## Clue Solutions
(from scratch_clues.md)

## Community Intel
(from scratch_community.md)

## Extraction
(from scratch_extraction.md)

## Answer Word
(merged conclusion)

## Status
- [ ] Grid transcribed
- [ ] Clues solved
- [ ] Grid solved
- [ ] Extraction method found
- [ ] Answer word extracted
```

## Word Length Constraints

| Position | Word Length | Assigned Puzzle |
|----------|-----------|-----------------|
| 1 | 5 letters | #1 Wells/Africa |
| 2 | 9 letters | #2 LIFECHANGE Sudoku |
| 3 | 5 letters | #3 Dirtiest Beach |
| 4 | 7 letters | #4 Experiences |
| 5 | 8 letters | #5 Pokemon Go |
| 6 | 4 letters | #6 Wilderness |
| 7 | 9 letters | #7 Adopted Dogs |
| 8 | 6 letters | #8 Pyramids |
| 9 | 5 letters | #9 Circle |

**Note:** Playlist order = meta-clue order is assumed but unconfirmed.

## Execution Checklist

- [x] Super Bowl ad frame analysis complete
- [x] Rewatch video analysis complete
- [x] `puzzles/shared_context.md` written with extraction keys
- [ ] Pick puzzle to focus on
- [ ] Launch 3-5 agents with role-specific prompts
- [ ] Monitor scratch files during execution
- [ ] Merge results into notes.md when agents complete
- [ ] Update state.json
- [ ] Repeat for next puzzle
