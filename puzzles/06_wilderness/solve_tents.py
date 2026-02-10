#!/usr/bin/env python3
"""
Tents and Trees solver for MrBeast Puzzle #6 (Wilderness).

Rules:
1. Each tree gets exactly one tent placed horizontally or vertically adjacent
2. No two tents can touch each other (horizontally, vertically, or diagonally)
3. Row/column tent counts must match the given clues
"""

ROWS = 15
COLS = 15

# Grid: 'T' = tree, number or '_' = non-tree cell
# Transcribed from screenshot — row 0 is top, col 0 is left
GRID = [
    # Col: 0    1    2    3    4    5    6    7    8    9   10   11   12   13   14
    ['2', '4', 'T', '8', '_', '1', '9', '_', '_', '_', '_', '2', '_', '6', '_'],  # R01
    ['T', '5', '6', '_', '3', 'T', 'T', '3', '_', '9', '1', '9', 'T', '7', 'T'],  # R02
    ['8', '_', '4', '5', 'T', '1', '6', '_', '8', 'T', 'T', '5', '6', '_', '8'],  # R03
    ['_', '1', 'T', '3', '7', '7', '_', '8', '_', '7', '9', '_', '6', '5', 'T'],  # R04
    ['_', '9', '2', '_', '3', 'T', '9', 'T', '7', '_', '_', '2', 'T', '4', '4'],  # R05
    ['4', 'T', '7', '_', '_', '5', '_', '6', '_', '_', '1', '_', '3', '_', '_'],  # R06
    ['_', '2', '_', '_', '_', '_', '_', '8', '_', '2', 'T', '4', '_', '_', '8'],  # R07
    ['3', 'T', '1', '_', '_', '_', '6', 'T', '2', '_', '3', '_', '_', '3', 'T'],  # R08
    ['_', '4', '_', '1', '_', '_', '7', '4', '_', '6', '_', '_', '2', '_', '5'],  # R09
    ['_', '_', '2', 'T', '4', '5', 'T', '8', '1', 'T', '9', '8', 'T', '4', '3'],  # R10
    ['_', '_', '_', '3', '8', '_', '6', '7', 'T', '2', '_', '_', '6', '5', 'T'],  # R11
    ['_', '4', '1', '7', 'T', '5', '_', '_', '9', '5', '_', '_', '_', '6', '7'],  # R12
    ['8', 'T', 'T', '3', '6', '9', '_', '2', 'T', 'T', '4', '_', '9', 'T', '1'],  # R13
    ['_', '6', '7', '_', '2', 'T', '1', '_', '4', '6', '_', '1', 'T', '3', '_'],  # R14
    ['_', '5', 'T', '2', '_', '3', '_', '_', '_', '_', '5', 'T', '4', '_', '_'],  # R15
]

# Tent counts per row (right side clues, top to bottom)
ROW_COUNTS = [4, 3, 1, 3, 3, 1, 3, 1, 1, 3, 1, 3, 3, 2, 3]

# Tent counts per column (bottom clues, left to right)
COL_COUNTS = [1, 3, 1, 3, 1, 4, 1, 3, 3, 2, 3, 3, 3, 1, 3]

def get_trees():
    """Return list of (row, col) for all trees."""
    trees = []
    for r in range(ROWS):
        for c in range(COLS):
            if GRID[r][c] == 'T':
                trees.append((r, c))
    return trees

def get_adjacent(r, c):
    """Return list of (row, col) horizontally/vertically adjacent to (r,c)."""
    adj = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            adj.append((nr, nc))
    return adj

def get_neighbors_8(r, c):
    """Return all 8 neighbors (including diagonals)."""
    neighbors = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                neighbors.append((nr, nc))
    return neighbors

def solve():
    trees = get_trees()
    num_trees = len(trees)
    print(f"Found {num_trees} trees")

    # For each tree, find valid tent positions (adjacent non-tree cells)
    tree_options = []
    for r, c in trees:
        options = []
        for nr, nc in get_adjacent(r, c):
            if GRID[nr][nc] != 'T':
                options.append((nr, nc))
        tree_options.append(options)
        if not options:
            print(f"ERROR: Tree at ({r},{c}) has no valid tent positions!")
            return

    # Print tree options for debugging
    for i, ((r, c), opts) in enumerate(zip(trees, tree_options)):
        print(f"Tree {i} at ({r},{c}): {len(opts)} options -> {opts}")

    # Solve using backtracking with constraint checking
    tent_placement = [None] * num_trees  # tent_placement[i] = (r,c) for tree i's tent
    tent_set = set()  # set of current tent positions

    row_counts = [0] * ROWS
    col_counts = [0] * COLS

    solutions = []

    def is_valid_tent(r, c):
        """Check if placing a tent at (r,c) is valid given current placements."""
        # Check row/col count limits
        if row_counts[r] >= ROW_COUNTS[r]:
            return False
        if col_counts[c] >= COL_COUNTS[c]:
            return False
        # Check no adjacent tent (8-directional)
        for nr, nc in get_neighbors_8(r, c):
            if (nr, nc) in tent_set:
                return False
        return True

    def can_still_satisfy_counts(tree_idx):
        """Quick check: can remaining trees still satisfy row/col counts?"""
        # Check if any row/col is already over the limit
        for r in range(ROWS):
            if row_counts[r] > ROW_COUNTS[r]:
                return False
        for c in range(COLS):
            if col_counts[c] > COL_COUNTS[c]:
                return False
        return True

    def backtrack(idx):
        if len(solutions) >= 10:  # Stop after finding 10 solutions
            return
        if idx == num_trees:
            # Check all row/col counts are exactly met
            if row_counts == ROW_COUNTS and col_counts == list(COL_COUNTS):
                solution = list(tent_placement)
                solutions.append(solution)
                print(f"\nSOLUTION {len(solutions)} FOUND!")
                print_solution(solution)
            return

        tr, tc = trees[idx]
        for tent_r, tent_c in tree_options[idx]:
            if (tent_r, tent_c) in tent_set:
                continue  # Already occupied by another tent
            if not is_valid_tent(tent_r, tent_c):
                continue

            # Place tent
            tent_placement[idx] = (tent_r, tent_c)
            tent_set.add((tent_r, tent_c))
            row_counts[tent_r] += 1
            col_counts[tent_c] += 1

            if can_still_satisfy_counts(idx + 1):
                backtrack(idx + 1)

            # Remove tent
            tent_placement[idx] = None
            tent_set.remove((tent_r, tent_c))
            row_counts[tent_r] -= 1
            col_counts[tent_c] -= 1

    backtrack(0)

    if not solutions:
        print("\nNo solution found! Grid transcription may have errors.")
    else:
        print(f"\nFound {len(solutions)} solution(s)")
        for i, sol in enumerate(solutions):
            print(f"\n=== Solution {i+1} ===")
            print_solution(sol)
            extract_answer(sol)

def print_solution(solution):
    """Print the grid with tents marked as 'X'."""
    display = [row[:] for row in GRID]
    for tent_r, tent_c in solution:
        display[tent_r][tent_c] = 'X'

    print("     " + "  ".join(f"{c:2d}" for c in range(COLS)))
    for r in range(ROWS):
        row_str = "  ".join(f"{display[r][c]:>2}" for c in range(COLS))
        print(f"R{r+1:02d}: {row_str}  | {ROW_COUNTS[r]}")
    print("     " + "  ".join(f"{c:2d}" for c in COL_COUNTS))

def extract_answer(solution):
    """Try various extraction methods on the solution."""
    print("\n--- Extraction attempts ---")

    # Method 1: Numbers at tent positions
    tent_numbers = []
    for tent_r, tent_c in solution:
        cell = GRID[tent_r][tent_c]
        if cell != '_' and cell != 'T':
            tent_numbers.append((tent_r, tent_c, cell))
        else:
            tent_numbers.append((tent_r, tent_c, '_'))

    print(f"\nNumbers at tent positions:")
    for r, c, val in tent_numbers:
        print(f"  Tent at ({r},{c}): {val}")

    nums_only = [v for _, _, v in tent_numbers if v != '_']
    print(f"Numeric values at tent sites: {nums_only}")
    if nums_only:
        # Try as letter indices (A=1)
        try:
            letters = [chr(int(n) + 64) for n in nums_only]
            print(f"As A=1 letters: {''.join(letters)}")
        except:
            pass

    # Method 2: Numbers in cells NOT occupied by tents (grass numbers)
    # This might be less useful with 35 tents in 225 cells

    # Method 3: Count something about the tent positions
    print(f"\nTent positions (row, col):")
    for i, (r, c) in enumerate(solution):
        print(f"  Tree {i}: tent at ({r},{c})")

if __name__ == "__main__":
    solve()
