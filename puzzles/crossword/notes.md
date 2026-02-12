# Crossword: Million Dollar Crossword

> **STATUS:** Research in progress
> **GRID:** 25x25 with ~176 numbered entries
> **CLUES:** Not yet visible (may populate dynamically)

---

## Overview

**Title:** "I WROTE A PUZZLE FOR JIMMY!"
**Author:** Mike Selinker (Lone Shark Games)
**Type:** Crossword puzzle with extraction mechanism
**Grid Size:** 25x25 with ~176 numbered entries

Per Hint #2, this crossword "might be a key to Stage 2" of the puzzle.

**Grid confirmed as 25x25** based on circled cell coordinates reaching column 25 and row 25.

---

## 🔥 HINT #2 REVELATION (Feb 10, 2026)

From official organizers:
> "In one of the Behind the Scenes videos, you might have seen puzzlemaster Mike drop a crossword puzzle."
> "That crossword is here and was a gift to Jimmy."
> "That crossword might also be a key to STAGE 2."
> **"Either way, it doesn't have any clues ... yet."**
> **"The more progress you make, the more the clues will fill in. You'll need those for the endgame."**

### What This Means

1. **Dynamic clue population** — Clues may appear as solvers make progress in Stage 1
2. **Role unclear** — Described as "might be a key to Stage 2"
3. **Mike Selinker revealed it** — In a BTS video (researching which one)
4. **Extraction mechanism** — Contains circled cells (typical extraction method)

---

## Puzzle Structure

### The Grid
- Standard 25x25 crossword layout
- 176 numbered squares total
- Mix of ACROSS and DOWN entries
- Contains **circled squares** for extraction

### Special Feature: Extraction Mechanism
- Multiple cells in the grid contain circles
- These circled letters spell out the final answer when read in order
- The extraction order/method is part of the puzzle

### Meta-Instruction (Entry 167)
The puzzle contains an explicit instruction:
> **167: What this puzzle commemorates in eleven hidden words in the theme entries**

This tells us:
- Theme entries contain hidden words
- Eleven hidden words reveal what the puzzle commemorates
- Classic Mike Selinker "hidden word" mechanic

---

## Current Research Focus

### 1. Finding Clue Text
The puzzle sheet shows only entry **numbers**, not the actual clues. We're investigating:
- YouTube video content (pinned comments, transcripts)
- Super Bowl ad frames (may encode clue information)
- BTS videos showing Mike with the crossword
- Dynamic updates on the puzzle site as Stage 1 progresses

### 2. Mapping Entry Positions
Building a database of:
- Which entry numbers correspond to which grid positions
- Entry lengths and crossing patterns
- Theme entries (the longer/special answers)

### 3. Cross-Referencing Video Content
Scanning thousands of frames from:
- Super Bowl ad (4K resolution)
- Bank heist teaser
- Salesforce BTS videos
- Checking for numbers that might correspond to crossword entries
- Looking for thematic connections

### 4. Developing Solving Tools
Created programmatic solvers:
- Database system to track candidates
- CSP (Constraint Satisfaction Problem) solver
- Backtracking algorithm with arc consistency
- Frame analysis pipeline (3,762 frames being processed)

---

## Community Collaboration

We're tracking community progress and findings from:
- Reddit threads (r/MrBeast, puzzle communities)
- Discord servers
- ARGNet analysis
- Social media hints

### What We're Seeing
- Various entry answers being proposed
- Cross-references with video content (149M views, September 19, etc.)
- Thematic connections to MrBeast videos
- Extraction theories

---

## Technical Approach

### Phase 1: Data Gathering ✅
- Transcribed all video content (VTT files)
- Extracted frames at 2-4fps from all videos
- Catalogued monitor symbols, numbers, visual elements
- Documented grid structure

### Phase 2: Pattern Recognition (In Progress)
- Correlating video numbers with crossword entry numbers
- Testing thematic word matches
- Analyzing Mike Selinker's puzzle design patterns
- Checking for embedded clues in ad content

### Phase 3: Automated Solving (In Progress)
- CSP solver to fill entries using crossing constraints
- Word list database by length
- Candidate ranking by confidence level
- Extraction script for circled cells

### Phase 4: Final Extraction (Pending)
- Map all cells with circles
- Determine extraction order
- Extract and verify final code
- Submit to Jimmy on Slack

---

## Next Steps

1. **Complete frame analysis** — Currently at 36.6% (1,377/3,759 frames)
2. **Monitor clue updates** — Check puzzle site for dynamic clue population
3. **Find Mike's BTS reveal** — Locate the video showing the crossword
4. **Test entry candidates** — Verify proposed answers against grid constraints
5. **Map extraction mechanism** — Determine precise reading order for circled cells

---

## Open Questions

1. Which Stage 1 milestones trigger which crossword clues?
2. How many circled cells total? (Estimated 12-20)
3. What order do we read the circled letters?
4. Does the extraction grid (bottom-right) have its own structure?
5. Which BTS video shows Mike revealing the crossword?

---

## Stage 2 Connection

Hint #2 states the crossword "might be a key to Stage 2" and that clues may fill in as progress is made. The exact mechanism and role in the overall puzzle is being researched.

---

## Files & Tools

```
puzzles/crossword/
├── notes.md                 # This file
├── Million-Dollar-Crossword.pdf
├── scripts/                 # Solver tools
└── [Additional research files]
```

---

**Status:** Active research | Clue text partially available | Extraction mechanism being mapped

**Last Updated:** 2026-02-11

---

*This is a collaborative effort. If you have findings to share, please contribute via GitHub issues or discussions.*
