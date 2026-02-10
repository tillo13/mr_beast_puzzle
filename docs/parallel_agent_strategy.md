# Parallel Agent Strategy: 1 Agent Per Puzzle

## Concept

Launch 9 Claude Code agents (CLI or VS Code windows), each laser-focused on one sub-puzzle. Each agent writes only to its own `puzzles/XX_*/` folder. A 10th "orchestrator" agent (or human) reads all 9 outputs and assembles the meta-clue.

## Prerequisites (before launching)

These should be done first — the per-puzzle agents need this shared context:

1. **Super Bowl ad frame analysis** — MUST complete first. The ad likely contains extraction keys needed to pull answer words from solved grids. Without these, agents can solve puzzle grids but can't extract the final word.
2. **Rewatch video analysis** — may contain additional extraction clues.
3. **Hint #2 (and any subsequent hints)** — could unlock entire puzzle categories.
4. **Shared context file** — write a `puzzles/shared_context.md` with all known extraction keys, ad symbols, and hints so each agent can reference it.

## Agent Assignments

| Agent | Puzzle | Folder | URL | Platform |
|-------|--------|--------|-----|----------|
| 1 | Wells/Africa | `puzzles/01_wells_africa/` | https://pin.it/3DIjEcxdY | Pinterest |
| 2 | LIFECHANGE Sudoku | `puzzles/02_lifechange/` | reddit.com/user/BeastForce67/.../puzzle/ | Reddit |
| 3 | Dirtiest Beach | `puzzles/03_dirtiest_beach/` | https://imgur.com/gallery/puzzle-mD2eHYD | Imgur |
| 4 | Experiences | `puzzles/04_experiences/` | https://imageshack.com/user/BeastForce67 | ImageShack |
| 5 | Pokemon Go | `puzzles/05_pokemon_go/` | photobucket.com/share/753ba093-... | Photobucket |
| 6 | Wilderness | `puzzles/06_wilderness/` | medium.com/@beastforce67/puzzle-... | Medium |
| 7 | Adopted Dogs | `puzzles/07_adopted_dogs/` | https://pixelfed.social/BeastForce67 | Pixelfed |
| 8 | Pyramids | `puzzles/08_pyramids/` | https://imgpile.com/u/beastforce67 | imgpile |
| 9 | Circle | `puzzles/09_circle/` | https://500px.com/p/beastforce67 | 500px |

## Per-Agent Prompt Template

Each agent gets a focused prompt like:

```
You are solving puzzle #{N} of the MrBeast Million Dollar Puzzle.

YOUR PUZZLE:
- Video: {video_title} ({video_id})
- Puzzle URL: {url}
- Platform: {platform}
- Meta-clue position: word #{N} of 9 (word length pattern: 5,9,5,7,8,4,9,6,5)
- Your answer word should be {X} letters long

YOUR TASK:
1. Fetch the puzzle URL and download/analyze all images
2. Identify the puzzle type (sudoku, crossword, cipher, steganography, etc.)
3. Solve the puzzle grid/mechanism
4. Read puzzles/shared_context.md for extraction keys from the Super Bowl ad
5. Apply the extraction method to get your answer word
6. Write ALL findings to puzzles/{folder}/notes.md

RULES:
- ONLY write to puzzles/{folder}/ — do not touch other puzzle folders
- Save images you download to puzzles/{folder}/
- Write notes.md with: puzzle type, solve process, grid solution, extraction attempt, answer word (or best candidates)
- If you can't extract the final word, document what you solved and what's missing
- Update your puzzle's entry in results/state.json when done (status, puzzle_type, grid_solved, answer_word)
- Read CLAUDE.md for repo conventions
```

## Word Length Constraints

Use these to validate answer words:

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

**Note:** We don't actually know which video maps to which meta-clue position. The mapping above assumes playlist order = meta-clue order, but this is unconfirmed. Agents should just focus on extracting their answer word — the ordering gets figured out during assembly.

## Practical Constraints

### Rate Limits
- 9 simultaneous agents all making API calls will likely hit rate limits
- **Mitigation:** Stagger launches by ~30 seconds, or run in two batches (5 then 4)
- Image-heavy puzzles (Pinterest, Imgur, Photobucket, imgpile) will use more tokens than text-based ones (Medium, Reddit)

### File Conflicts
- Each agent writes ONLY to its own folder — no conflicts
- `puzzles/shared_context.md` is READ-ONLY for puzzle agents (written by orchestrator before launch)

### When an Agent Gets Stuck
- It should document what it figured out and what's blocking it in `notes.md`
- The orchestrator can then cross-reference with other agents' findings
- Some puzzles may be unsolvable without info from other puzzles (the "interconnected" design)

## Orchestrator Role (10th agent or human)

After all 9 agents finish:

1. Read `results/state.json` — check which puzzles have answer words vs. are stuck
2. Read all 9 `puzzles/*/notes.md` files for detailed findings
3. Cross-reference stuck agents with findings from other puzzles
4. Update `results/state.json` meta_clue.words array with extracted words
5. Attempt meta-clue assembly: `_____ _________ _____ _______ ________ ____ _________ ______ _____`
6. Validate: does the assembled phrase read as an INSTRUCTION?
7. Follow the instruction to find the hidden code

## Estimated Resource Usage

- ~9 agent sessions running ~10-30 min each
- Token-heavy for image analysis puzzles
- Best run during off-peak hours if rate limits are a concern
- Total cost depends on puzzle complexity — budget for ~$5-15 across all 9

## When to Execute

- [ ] Super Bowl ad frame analysis complete → extraction keys documented
- [ ] Rewatch video analysis complete → additional clues documented
- [ ] All hints checked and incorporated
- [ ] `puzzles/shared_context.md` written with all known keys/clues
- [ ] Rate limit headroom confirmed

Then launch all 9.
