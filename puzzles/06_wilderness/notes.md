# Puzzle #6: Wilderness / $10,000 Every Day You Survive In The Wilderness

## Status: SOLVING
**Last updated:** 2026-02-09

---

## Basic Info

| Field | Value |
|-------|-------|
| Position in meta-clue | 6 of 9 |
| Expected answer length | **4 letters** |
| YouTube video | "$10,000 Every Day You Survive In The Wilderness" (U_LlX4t0A9I) |
| Video URL | https://www.youtube.com/watch?v=U_LlX4t0A9I |
| Pinned by | @MrBeast |
| Pinned comment text | "What an epic challenge! This is also pretty epic. https://medium.com/@beastforce67/puzzle-1a6600218fd0" |
| Puzzle platform | Medium (user @beastforce67) |
| Puzzle URL | https://medium.com/@beastforce67/puzzle-1a6600218fd0 |
| Puzzle type | **Tents and Trees** (logic puzzle) |
| Image URL | Screenshot provided by user |

---

## Puzzle Description

### Title (on image)
"$10,000 EVERY DAY YOU SURVIVE IN THE WILDERNESS"

### Rules (from image)
> You're alone in the wilderness with limited supplies.
> Pitch exactly one tent horizontally or vertically by each tree.
> No tent can touch any other tent, even diagonally.
> A number outside the wilderness shows how many tents are in that direction.

### Puzzle Type: Tents and Trees
This is a well-known logic puzzle:
1. Each tree (grey icon) gets exactly one tent placed horizontally or vertically adjacent
2. No two tents can touch each other, even diagonally
3. Row counts (right side) and column counts (bottom) show how many tents per line
4. Numbers inside the grid cells are NOT part of the Tents rules — likely for extraction

### Grid: 15x15
- 35 trees total
- Row clues (right, R01→R15): 4, 3, 1, 3, 3, 1, 3, 1, 1, 3, 1, 3, 3, 2, 3
- Col clues (bottom, C01→C15): 1, 3, 1, 3, 1, 4, 1, 3, 3, 2, 3, 3, 3, 1, 3
- Both sum to 35 ✓

### Grid Transcription (T = tree, _ = empty, numbers as-is)

**CAVEAT**: Transcribed from screenshot — some cells may be misread. Needs verification.

```
Col:  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
R01:  2  4  T  8  _  1  9  _  _  _  _  2  _  6  _  | 4
R02:  T  5  6  _  3  T  T  3  _  9  1  9  T  7  T  | 3
R03:  8  _  4  5  T  1  6  _  8  T  T  5  6  _  8  | 1
R04:  _  1  T  3  7  7  _  8  _  7  9  _  6  5  T  | 3
R05:  _  9  2  _  3  T  9  T  7  _  _  2  T  4  4  | 3
R06:  4  T  7  _  _  5  _  6  _  _  1  _  3  _  _  | 1
R07:  _  2  _  _  _  _  _  8  _  2  T  4  _  _  8  | 3
R08:  3  T  1  _  _  _  6  T  2  _  3  _  _  3  T  | 1
R09:  _  4  _  1  _  _  7  4  _  6  _  _  2  _  5  | 1
R10:  _  _  2  T  4  5  T  8  1  T  9  8  T  4  3  | 3
R11:  _  _  _  3  8  _  6  7  T  2  _  _  6  5  T  | 1
R12:  _  4  1  7  T  5  _  _  9  5  _  _  _  6  7  | 3
R13:  8  T  T  3  6  9  _  2  T  T  4  _  9  T  1  | 3
R14:  _  6  7  _  2  T  1  _  4  6  _  1  T  3  _  | 2
R15:  _  5  T  2  _  3  _  _  _  _  5  T  4  _  _  | 3
      1  3  1  3  1  4  1  3  3  2  3  3  3  1  3
```

### Tree positions (row, col) — 0-indexed for solver:
(0,2), (1,0), (1,5), (1,6), (1,12), (1,14),
(2,4), (2,9), (2,10),
(3,2), (3,14),
(4,5), (4,7), (4,12),
(5,1),
(6,10),
(7,1), (7,7), (7,14),
(9,3), (9,6), (9,9), (9,12),
(10,8), (10,14),
(11,4),
(12,1), (12,2), (12,8), (12,9), (12,13),
(13,5), (13,12),
(14,2), (14,11)

Total: 35 trees ✓

---

## Extraction Hypothesis

The grid contains numbers (1-9) in many non-tree cells. After solving tent placement, the extraction likely involves:
- Reading numbers at tent positions
- Or reading numbers adjacent to tents
- Or some mapping from tent positions to letters

The expected answer is **4 letters**. The pinned comment mentions "epic" twice — "EPIC" is 4 letters and could be thematic.

---

## Solving Strategy
1. Solve Tents placement using constraint solver (see `solve_tents.py`)
2. After tent positions found, examine numbers at/near tent positions
3. Determine extraction mechanism (may need Super Bowl ad clues)
4. Extract the 4-letter answer word

## SOLUTION — Tents Placement (UNIQUE)

The solver found exactly **1 solution** — the placement is unique and consistent.

```
Col:  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14
R01:  X   4   T   X   _   X   9   _   _   _   _   2   _   6   X  | 4
R02:  T   5   6   _   3   T   T   X   _   X   1   X   T   7   T  | 3
R03:  8   _   4   5   T   X   6   _   8   T   T   5   6   _   8  | 1
R04:  _   1   T   X   7   7   _   8   _   7   X   _   X   5   T  | 3
R05:  _   X   2   _   3   T   9   T   X   _   _   2   T   4   X  | 3
R06:  4   T   7   _   _   X   _   6   _   _   1   _   3   _   _  | 1
R07:  _   2   _   _   _   _   _   X   _   2   T   X   _   _   X  | 3
R08:  3   T   X   _   _   _   6   T   2   _   3   _   _   3   T  | 1
R09:  _   4   _   1   _   _   7   4   _   X   _   _   2   _   5  | 1
R10:  _   _   2   T   X   5   T   X   1   T   9   X   T   4   3  | 3
R11:  _   _   _   3   8   _   6   7   T   2   _   _   6   X   T  | 1
R12:  _   X   1   7   T   X   _   _   X   5   _   _   _   6   7  | 3
R13:  8   T   T   X   6   9   _   2   T   T   X   _   X   T   1  | 3
R14:  _   6   7   _   2   T   X   _   X   6   _   1   T   3   _  | 2
R15:  _   X   T   2   _   3   _   _   _   _   X   T   X   _   _  | 3
      1   3   1   3   1   4   1   3   3   2   3   3   3   1   3
```

X = tent, T = tree

### Numbers at tent positions (reading order, top-left to bottom-right):
| Row | Col | Number |
|-----|-----|--------|
| 0 | 0 | 2 |
| 0 | 3 | 8 |
| 0 | 5 | 1 |
| 0 | 14 | _ (empty) |
| 1 | 7 | 3 |
| 1 | 9 | 9 |
| 1 | 11 | 9 |
| 2 | 5 | 1 |
| 3 | 3 | 3 |
| 3 | 10 | 9 |
| 3 | 12 | 6 |
| 4 | 1 | 9 |
| 4 | 8 | 7 |
| 4 | 14 | 4 |
| 5 | 5 | 5 |
| 6 | 7 | 8 |
| 6 | 11 | 4 |
| 6 | 14 | 8 |
| 7 | 2 | 1 |
| 8 | 9 | 6 |
| 9 | 4 | 4 |
| 9 | 7 | 8 |
| 9 | 11 | 8 |
| 10 | 13 | 5 |
| 11 | 1 | 4 |
| 11 | 5 | 5 |
| 11 | 8 | 9 |
| 12 | 3 | 3 |
| 12 | 10 | 4 |
| 12 | 12 | 9 |
| 13 | 6 | 1 |
| 13 | 8 | 4 |
| 14 | 1 | 5 |
| 14 | 10 | 5 |
| 14 | 12 | 4 |

### Extraction — Still Unknown
- 35 tents but only 4-letter answer needed
- Community decoded "CASH TENT" from Super Bowl ad — "TENT" is directly relevant
- Need to determine which 4 tents/cells to read, or what mapping gives 4 letters
- One tent (0,14) lands on an empty cell — possibly significant

## Status Checklist
- [x] Puzzle image obtained (screenshot)
- [x] Grid transcribed
- [x] Tents SOLVED (unique solution)
- [x] Grid verified against higher-res image
- [ ] Extraction mechanism determined
- [ ] Answer word extracted
