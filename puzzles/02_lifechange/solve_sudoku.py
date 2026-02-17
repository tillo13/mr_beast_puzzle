#!/usr/bin/env python3
"""
solve_sudoku.py — Solve the LIFECHANGE Sudoku variant (Puzzle #2).
Letters L,I,F,E,C,H,A,N,G replace digits 1-9.
Also tries nearby alternate placements if main grid fails.
"""

LETTERS = ['L', 'I', 'F', 'E', 'C', 'H', 'A', 'N', 'G']
LETTER_TO_NUM = {ch: i+1 for i, ch in enumerate(LETTERS)}
NUM_TO_LETTER = {i+1: ch for i, ch in enumerate(LETTERS)}
NUM_TO_LETTER[0] = '.'

# Primary transcription from image
GRID_LETTERS = [
    ['.','L','.','.','.',  'N','.','G','.'],
    ['C','.','.','.',  'I','.','N','.','.'],
    ['.','.','I','.',  '.','L','.','F','.'],
    ['G','.','.','.',  'E','.','C','.','.'],
    ['.','H','.','.', '.','A','.','E','.'],
    ['F','.','.','.',  'N','.','I','.','.'],
    ['.','.','F','.',  '.','G','.','I','.'],
    ['N','.','.','.',  'L','.','A','.','.'],
    ['.','C','.','.', '.','H','.','N','.'],
]


def to_num_grid(letter_grid):
    return [[LETTER_TO_NUM.get(c, 0) for c in row] for row in letter_grid]


def is_valid(grid, row, col, num):
    if num in grid[row]:
        return False
    if any(grid[r][col] == num for r in range(9)):
        return False
    br, bc = 3 * (row // 3), 3 * (col // 3)
    for r in range(br, br + 3):
        for c in range(bc, bc + 3):
            if grid[r][c] == num:
                return False
    return True


def check_initial_validity(grid):
    """Check if the given clues themselves are consistent."""
    errors = []
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                continue
            val = grid[r][c]
            grid[r][c] = 0  # temporarily remove to check
            if not is_valid(grid, r, c, val):
                errors.append((r, c, NUM_TO_LETTER[val]))
            grid[r][c] = val
    return errors


def solve(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                for num in range(1, 10):
                    if is_valid(grid, r, c, num):
                        grid[r][c] = num
                        if solve(grid):
                            return True
                        grid[r][c] = 0
                return False
    return True


def count_possibilities(grid):
    """For each empty cell, count how many values are possible."""
    info = []
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                possible = [n for n in range(1, 10) if is_valid(grid, r, c, n)]
                info.append((r, c, len(possible), [NUM_TO_LETTER[n] for n in possible]))
    return info


def print_grid(grid, label=""):
    if label:
        print(f"\n=== {label} ===")
    for i, row in enumerate(grid):
        if i % 3 == 0 and i > 0:
            print("------+-------+------")
        line = ""
        for j, val in enumerate(row):
            if j % 3 == 0 and j > 0:
                line += " | "
            ch = NUM_TO_LETTER.get(val, '.') if isinstance(val, int) else val
            line += f" {ch}"
        print(line)


def try_grid(letter_grid, label=""):
    """Try to solve a grid, return solved grid or None."""
    grid = to_num_grid(letter_grid)

    errors = check_initial_validity(grid)
    if errors:
        print(f"  {label}: Initial constraint violations at: {errors}")
        return None

    import copy
    g = copy.deepcopy(grid)
    if solve(g):
        print(f"  {label}: SOLVED!")
        return g
    else:
        print(f"  {label}: No solution (grid is unsolvable)")
        return None


def generate_variants(base_grid):
    """Try shifting each given letter left/right by 1 position."""
    import copy
    variants = []

    for r in range(9):
        for c in range(9):
            if base_grid[r][c] != '.':
                # Try shifting left
                if c > 0 and base_grid[r][c-1] == '.':
                    v = copy.deepcopy(base_grid)
                    v[r][c-1] = v[r][c]
                    v[r][c] = '.'
                    variants.append((v, f"R{r+1}C{c+1}({base_grid[r][c]}) -> C{c}"))
                # Try shifting right
                if c < 8 and base_grid[r][c+1] == '.':
                    v = copy.deepcopy(base_grid)
                    v[r][c+1] = v[r][c]
                    v[r][c] = '.'
                    variants.append((v, f"R{r+1}C{c+1}({base_grid[r][c]}) -> C{c+2}"))

    return variants


def main():
    print("LIFECHANGE Sudoku — Puzzle #2")
    print(f"Letters: {' '.join(LETTERS)}")

    print_grid(GRID_LETTERS, "GIVEN GRID (primary transcription)")

    # Try primary grid
    print("\n--- Attempting primary grid ---")
    result = try_grid(GRID_LETTERS, "Primary")

    if result:
        print_grid(result, "SOLVED")
    else:
        # Debug: show possibilities for primary grid
        grid = to_num_grid(GRID_LETTERS)
        poss = count_possibilities(grid)
        dead = [(r, c, n, p) for r, c, n, p in poss if n == 0]
        if dead:
            print(f"\n  Dead cells (0 possibilities): {[(f'R{r+1}C{c+1}', p) for r,c,n,p in dead]}")
        tight = [(r, c, n, p) for r, c, n, p in poss if 0 < n <= 2]
        if tight:
            print(f"  Tight cells (1-2 possibilities): {[(f'R{r+1}C{c+1}', p) for r,c,n,p in tight]}")

        # Try single-letter shifts
        print("\n--- Trying single-letter shifts ---")
        variants = generate_variants(GRID_LETTERS)
        print(f"  Generated {len(variants)} variants")

        solutions = []
        for v_grid, desc in variants:
            result = try_grid(v_grid, desc)
            if result:
                solutions.append((result, desc))

        if solutions:
            print(f"\n*** FOUND {len(solutions)} SOLUTION(S) via single shifts ***")
            for sol, desc in solutions:
                print(f"\nShift: {desc}")
                print_grid(sol, f"SOLVED (shift: {desc})")
                print("\nRows:")
                for i in range(9):
                    print(f"  Row {i+1}: {''.join(NUM_TO_LETTER[sol[i][c]] for c in range(9))}")
                print("Columns:")
                for c in range(9):
                    print(f"  Col {c+1}: {''.join(NUM_TO_LETTER[sol[r][c]] for r in range(9))}")
                print("Diagonals:")
                print(f"  Main:  {''.join(NUM_TO_LETTER[sol[i][i]] for i in range(9))}")
                print(f"  Anti:  {''.join(NUM_TO_LETTER[sol[i][8-i]] for i in range(9))}")
        else:
            # Try double shifts
            print("\n--- Trying double-letter shifts ---")
            count = 0
            for v1_grid, d1 in variants:
                v2s = generate_variants(v1_grid)
                for v2_grid, d2 in v2s:
                    result = try_grid(v2_grid, f"{d1} + {d2}")
                    if result:
                        solutions.append((result, f"{d1} + {d2}"))
                    count += 1
                    if count % 100 == 0:
                        print(f"  ... tried {count} double variants")

            if solutions:
                print(f"\n*** FOUND {len(solutions)} SOLUTION(S) via double shifts ***")
                for sol, desc in solutions:
                    print(f"\nShifts: {desc}")
                    print_grid(sol, f"SOLVED (shifts: {desc})")
                    print("\nRows:")
                    for i in range(9):
                        print(f"  Row {i+1}: {''.join(NUM_TO_LETTER[sol[i][c]] for c in range(9))}")
            else:
                print("\n  No solutions found with up to 2 shifts.")
                print("  The puzzle may need a completely different transcription.")


if __name__ == "__main__":
    main()
