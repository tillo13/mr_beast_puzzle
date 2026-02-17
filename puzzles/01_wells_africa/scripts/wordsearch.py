#!/usr/bin/env python3
"""
Comprehensive multi-directional word search for MrBeast Puzzle #1 (Wells/Africa).

Grid: 9x9 with 15 water drops (wildcards).
Searches all 8 directions for:
  1. Specific clue candidate answers
  2. Specific partial patterns (HOOD, DAM, HOOVER, etc.)
  3. All English words of length 4+ from /usr/share/dict/words

Outputs results to scratch_wordsearch.md
"""

import os
import re
from collections import defaultdict

# ── THE GRID ──────────────────────────────────────────────────────────────────
grid = [
    ['M', '.', 'R', 'A', 'Y', '.', 'C', 'O', 'N'],
    ['U', 'A', 'N', 'L', '.', 'C', 'S', 'T', 'I'],
    ['.', 'H', 'D', '.', 'O', 'A', 'I', 'D', 'A'],
    ['N', 'D', 'T', 'R', 'W', 'O', '.', 'R', 'R'],
    ['N', 'E', 'W', 'P', 'E', 'N', 'A', 'E', 'T'],
    ['.', 'C', '.', 'I', 'I', 'V', 'I', 'N', '.'],
    ['P', 'E', 'D', 'B', 'N', 'S', '.', '.', 'C'],
    ['Y', '.', 'O', 'H', '.', 'K', 'W', 'C', '.'],
    ['T', 'R', 'O', 'R', 'D', 'K', '.', 'S', 'C'],
]

ROWS = len(grid)
COLS = len(grid[0])

# 8 directions: (row_delta, col_delta)
DIRECTIONS = {
    'RIGHT':      (0, 1),
    'LEFT':       (0, -1),
    'DOWN':       (1, 0),
    'UP':         (-1, 0),
    'DOWN_RIGHT': (1, 1),
    'DOWN_LEFT':  (1, -1),
    'UP_RIGHT':   (-1, 1),
    'UP_LEFT':    (-1, -1),
}

# ── CLUE CANDIDATES ──────────────────────────────────────────────────────────
clue_candidates = {
    '1. A cold noise?': [
        'ACHOO', 'SNEEZE', 'WHEEZE', 'COUGH', 'SNIFFLE', 'BRRR', 'SHIVER',
    ],
    '2. A natural disaster': [
        'STORM', 'TORNADO', 'DROUGHT', 'FLOOD', 'QUAKE', 'TREMOR', 'TWISTER',
        'TYPHOON', 'BLIZZARD', 'CYCLONE',
    ],
    '3. MrBeast went to one in Greenville, NC': [
        'SCHOOL', 'CHURCH', 'LIBRARY', 'STORE', 'RESTAURANT', 'COLLEGE',
        'UNIVERSITY', 'ARCADE', 'CINEMA', 'MUSEUM', 'DINER', 'ARENA',
    ],
    '4. Deceive': [
        'TRICK', 'DUPE', 'CHEAT', 'SWINDLE', 'CON', 'HOAX', 'DELUDE',
        'MISLEAD', 'LIE', 'DECEIVE', 'OUTWIT', 'BETRAY', 'DEFRAUD', 'HOODWINK',
    ],
    '5. Rats! (2 wds.)': [
        'OHNO', 'DARNIT', 'OHRATS', 'NOWAY', 'GOODGRIEF', 'OHSHOOT', 'OHWELL', 'OHGEE',
    ],
    '6. A certain Midwesterner': [
        'IOWAN', 'OHIOAN', 'HOOSIER', 'KANSAN',
    ],
    '7. A child\'s toy (2 wds., Hyph.)': [
        'YOYO', 'TOPTOP', 'POPGUN', 'TINCAN', 'TOPHAT', 'NERFGUN', 'RUBIKS',
    ],
    '8. Upset': [
        'IRATE', 'ANGRY', 'RILED', 'VEXED', 'MAD', 'UPSET', 'CROSS', 'IRKED',
        'PEEVED', 'ANNOYED', 'TICKED',
    ],
    '9. An item you can buy in MrBeast\'s store': [
        'HOODIE', 'TSHIRT', 'HAT', 'SHIRT', 'PANTS', 'CANDY', 'CAP', 'SNACK',
        'CHOCOLATE',
    ],
    '10. A US landmark (2 wds.)': [
        'HOOVERDAM', 'MOUNTRUSHMORE', 'GOLDGATE', 'LIBERTYBELL', 'RUBYFALLS',
        'PIKEPLACE', 'ARCHWAY', 'OLDWELL', 'ROCKCITY',
    ],
    '11. A type of boat': [
        'CANOE', 'KAYAK', 'SKIFF', 'YACHT', 'SLOOP', 'DINGHY', 'BARGE',
        'SCOW', 'PUNT', 'ARK', 'DHOW', 'CATBOAT', 'ROWBOAT',
    ],
    '12. A literary outlaw (2 wds.)': [
        'ROBINHOOD', 'ROBIN', 'HOOD', 'JESSEJAMES', 'BILLYKID', 'CAPTAINHOOK', 'ZORRO',
    ],
    '13. What you might say when you finish!': [
        'DONE', 'WELLDONE', 'HURRAY', 'YIPPEE', 'EUREKA', 'TADAA', 'VOILA',
        'FINISH', 'ATLAST', 'HOORAY', 'WAHOO', 'YESSS', 'FINALLY', 'BINGO',
    ],
}

# Extra specific patterns to search
extra_patterns = ['HOOD', 'DAM', 'HOOVER', 'ROBIN', 'TRAIN', 'WINK', 'RAIN',
                  'WELL', 'WELLS', 'WATER', 'AFRICA', 'BEAST', 'PENNY', 'PENNE',
                  'NEWPENAET', 'REPENT', 'PENNATE', 'WEAPON', 'IRATE', 'TROWEL',
                  'DROWN', 'CROWD', 'SWORD', 'TOWER', 'POWER', 'OWNER', 'NEWER',
                  'ROWBOAT', 'CANOE', 'KAYAK', 'SKIFF', 'SCOW', 'PUNT',
                  'DHOW', 'CORKED', 'DOCKS', 'STOCK', 'STORK', 'CORDS',
                  'CIVIC', 'VINCI', 'SPEND', 'BENDS', 'WHOCK', 'HOCKEY',
                  'AIDA', 'AHEAD', 'OHNO', 'IOWAN', 'YOYO', 'CON', 'TRICK',
                  'DUPE', 'LIE', 'PEON', 'OPEN', 'NOPE', 'PENT', 'WENT',
                  'WEPT', 'NEAP', 'PANE', 'PEAT', 'PAWN', 'PEWN', 'ANEW',
                  'INWARD', 'ONWARD', 'UPWARD', 'DOWNWARD',
                  'ACE', 'VINE', 'DIVINE', 'DRIVEN', 'RIVEN',
                  'OWN', 'OWE', 'AWE', 'EWE', 'ORE', 'DRONE', 'HONE',
                  'WREN', 'HEWN', 'DAWN', 'DRAWN', 'PRAWN', 'SPAWN',
                  'WORD', 'WORK', 'WORLD', 'CORD', 'LORD', 'FORD',
                  'COIN', 'JOIN', 'VOID', 'AVID', 'AMID',
                  'RIND', 'BIND', 'KIND', 'MIND', 'WIND', 'FIND',
                  'PEDAL', 'PEDANT', 'PEDESTRIAN',
                  'SNIDE', 'PRIDE', 'BRIDE', 'STRIDE', 'TRIDENT',
                  'OVERDO', 'REDO', 'UNDO', 'INDOOR',
                  'ORCID', 'ORCHID', 'TORRID',
                  'SINK', 'RINK', 'DRINK', 'THINK', 'BRINK',
                  'COIN', 'GROIN', 'LOIN',
                  ]


def extract_line(r, c, dr, dc, max_len=9):
    """Extract characters along a direction from (r,c), up to max_len or grid edge.
    Returns list of (row, col, char) tuples."""
    cells = []
    cr, cc = r, c
    while 0 <= cr < ROWS and 0 <= cc < COLS and len(cells) < max_len:
        cells.append((cr, cc, grid[cr][cc]))
        cr += dr
        cc += dc
    return cells


def match_word_on_line(word, cells):
    """Check if `word` matches the beginning of `cells`.
    '.' in the grid is a wildcard matching any letter.
    Returns (matched, path_info) where path_info lists each cell.
    """
    if len(word) > len(cells):
        return False, []
    path = []
    for i, ch in enumerate(word):
        r, c, grid_ch = cells[i]
        if grid_ch == '.':
            path.append((r, c, ch, True))   # wildcard: filled with word's letter
        elif grid_ch == ch:
            path.append((r, c, ch, False))   # exact match
        else:
            return False, []
    return True, path


def search_word(word):
    """Search for `word` in all 8 directions from every cell.
    Returns list of (direction_name, path) for each match found.
    """
    word = word.upper()
    results = []
    for dir_name, (dr, dc) in DIRECTIONS.items():
        for r in range(ROWS):
            for c in range(COLS):
                cells = extract_line(r, c, dr, dc, len(word))
                matched, path = match_word_on_line(word, cells)
                if matched:
                    results.append((dir_name, path))
    return results


def format_path(path):
    """Format a path as a readable string."""
    parts = []
    wildcards = []
    for r, c, ch, is_wild in path:
        marker = '*' if is_wild else ''
        parts.append(f"R{r+1}C{c+1}={ch}{marker}")
        if is_wild:
            wildcards.append(f"R{r+1}C{c+1}")
    path_str = ' -> '.join(parts)
    wild_count = sum(1 for _, _, _, w in path if w)
    wild_str = f" [wildcards: {', '.join(wildcards)}]" if wildcards else " [all visible]"
    return path_str + wild_str, wild_count


def load_dictionary(min_len=4, max_len=9):
    """Load English words from /usr/share/dict/words."""
    words = set()
    dict_path = '/usr/share/dict/words'
    if not os.path.exists(dict_path):
        print(f"WARNING: {dict_path} not found. Skipping general word search.")
        return words
    with open(dict_path, 'r') as f:
        for line in f:
            w = line.strip().upper()
            if min_len <= len(w) <= max_len and w.isalpha():
                words.add(w)
    print(f"Loaded {len(words)} dictionary words (length {min_len}-{max_len})")
    return words


# ──────────────────────────────────────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────────────────────────────────────

output_lines = []

def out(text=""):
    output_lines.append(text)
    print(text)


out("# Puzzle #1 Word Search Results")
out()
out("Grid (. = wildcard/water drop):")
out("```")
out("       C1  C2  C3  C4  C5  C6  C7  C8  C9")
for i, row in enumerate(grid):
    cells = '  '.join(f" {ch}" if ch != '.' else ' .' for ch in row)
    out(f"Row {i+1}: {cells}")
out("```")
out()

# ── SECTION 1: Clue-specific candidate search ────────────────────────────────
out("## Section 1: Clue Candidate Matches")
out()

total_clue_matches = 0
for clue, candidates in clue_candidates.items():
    out(f"### {clue}")
    found_any = False
    for word in candidates:
        results = search_word(word)
        if results:
            found_any = True
            total_clue_matches += len(results)
            for dir_name, path in results:
                path_str, wild_count = format_path(path)
                out(f"  **{word}** ({len(word)} letters) — {dir_name} — wildcards: {wild_count}")
                out(f"    Path: {path_str}")
    if not found_any:
        out("  (no matches)")
    out()

out(f"**Total clue candidate matches: {total_clue_matches}**")
out()

# ── SECTION 2: Extra specific patterns ────────────────────────────────────────
out("## Section 2: Specific Pattern Matches")
out()

for word in extra_patterns:
    results = search_word(word)
    if results:
        for dir_name, path in results:
            path_str, wild_count = format_path(path)
            out(f"**{word}** ({len(word)}) — {dir_name} — wildcards: {wild_count}")
            out(f"  Path: {path_str}")
        out()

# ── SECTION 3: General dictionary word search ─────────────────────────────────
out("## Section 3: General Dictionary Word Search (4+ letters)")
out()

dictionary = load_dictionary(min_len=4, max_len=9)

# For efficiency, pre-extract all lines in all directions and search
all_found = {}  # word -> [(dir_name, path, wild_count)]

for dir_name, (dr, dc) in DIRECTIONS.items():
    for r in range(ROWS):
        for c in range(COLS):
            cells = extract_line(r, c, dr, dc, 9)
            # Try matching every dictionary word against this line
            # Optimization: build the string and check substrings
            line_str = ''.join(ch for _, _, ch in cells)
            line_len = len(cells)

            # For each starting position in this line, try words of various lengths
            for start in range(line_len):
                sub_cells = cells[start:]
                for word_len in range(4, len(sub_cells) + 1):
                    # Build the candidate string (with wildcards as regex)
                    candidate_cells = sub_cells[:word_len]
                    # Check all dictionary words — but this is O(dict * positions) which is slow
                    # Instead, for each position, extract possible strings and look up
                    pass

# Better approach: for each line in the grid, extract all possible substrings
# and check against dictionary
out("### Method: Extract all lines, check against dictionary")
out()

all_found = defaultdict(list)  # word -> [(dir_name, start_r, start_c, path, wild_count)]

for dir_name, (dr, dc) in DIRECTIONS.items():
    # Generate all starting points for this direction
    starts = set()
    for r in range(ROWS):
        for c in range(COLS):
            starts.add((r, c))

    for sr, sc in starts:
        cells = extract_line(sr, sc, dr, dc, 9)
        if len(cells) < 4:
            continue

        # For each substring of length 4-9
        for start_idx in range(len(cells)):
            for end_idx in range(start_idx + 4, min(start_idx + 10, len(cells) + 1)):
                sub = cells[start_idx:end_idx]
                word_len = len(sub)

                # Build a regex pattern from the cells (. = any letter)
                pattern_chars = []
                for _, _, ch in sub:
                    if ch == '.':
                        pattern_chars.append('.')
                    else:
                        pattern_chars.append(ch)
                pattern = ''.join(pattern_chars)

                # If no wildcards, just look up directly
                if '.' not in pattern:
                    if pattern in dictionary:
                        _, path = match_word_on_line(pattern, sub)
                        _, wc = format_path(path)
                        all_found[pattern].append((dir_name, sub[0][0], sub[0][1], path, wc))
                else:
                    # With wildcards, need to check all words of this length
                    regex = re.compile('^' + pattern + '$')
                    for w in dictionary:
                        if len(w) == word_len and regex.match(w):
                            matched, path = match_word_on_line(w, sub)
                            if matched:
                                _, wc = format_path(path)
                                all_found[w].append((dir_name, sub[0][0], sub[0][1], path, wc))

# Deduplicate results (same word, same starting cell, same direction)
deduped = defaultdict(list)
for word, matches in all_found.items():
    seen = set()
    for dir_name, sr, sc, path, wc in matches:
        key = (dir_name, sr, sc)
        if key not in seen:
            seen.add(key)
            deduped[word].append((dir_name, sr, sc, path, wc))

# Sort by length (longest first), then alphabetically
sorted_words = sorted(deduped.keys(), key=lambda w: (-len(w), w))

out(f"Found **{len(sorted_words)}** unique dictionary words (4+ letters)")
out()

# Report by length group
for length in range(9, 3, -1):
    words_of_len = [w for w in sorted_words if len(w) == length]
    if not words_of_len:
        continue
    out(f"### {length}-letter words ({len(words_of_len)} found)")
    out()
    for word in words_of_len:
        for dir_name, sr, sc, path, wc in deduped[word]:
            path_str, _ = format_path(path)
            out(f"- **{word}** — {dir_name} — wildcards: {wc}")
            out(f"  {path_str}")
    out()

# ── SECTION 4: Words crossing drop positions ──────────────────────────────────
out("## Section 4: Words That Cross Drop Positions")
out()

drop_positions = set()
for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == '.':
            drop_positions.add((r, c))

out(f"Drop positions: {sorted(drop_positions)}")
out()

# Find all found words that have at least one wildcard (crossing a drop)
out("### Words requiring wildcards (crossing drops)")
out()

wildcard_words = []
for word in sorted_words:
    for dir_name, sr, sc, path, wc in deduped[word]:
        if wc > 0:
            wildcard_words.append((word, dir_name, sr, sc, path, wc))

# Sort by word length desc, then wildcard count asc (fewer wildcards = more constrained)
wildcard_words.sort(key=lambda x: (-len(x[0]), x[5], x[0]))

for word, dir_name, sr, sc, path, wc in wildcard_words:
    path_str, _ = format_path(path)
    out(f"- **{word}** ({len(word)} letters, {wc} wildcards) — {dir_name}")
    out(f"  {path_str}")

out()

# ── SECTION 5: Drop letter implications ──────────────────────────────────────
out("## Section 5: What Letters Could Fill Each Drop?")
out()

# For each drop, collect all words that cross it and what letter they imply
drop_letters = defaultdict(set)  # (r,c) -> set of (letter, word, direction)

for word in sorted_words:
    for dir_name, sr, sc, path, wc in deduped[word]:
        if wc > 0:
            for r, c, ch, is_wild in path:
                if is_wild:
                    drop_letters[(r, c)].add((ch, word, dir_name))

for (r, c) in sorted(drop_positions):
    implied = drop_letters.get((r, c), set())
    if implied:
        letters_only = sorted(set(ch for ch, _, _ in implied))
        out(f"**R{r+1}C{c+1}** — possible letters: {', '.join(letters_only)}")
        for ch, word, dir_name in sorted(implied, key=lambda x: (-len(x[1]), x[1])):
            out(f"  - {ch} ← {word} ({dir_name})")
    else:
        out(f"**R{r+1}C{c+1}** — no dictionary words cross this drop")
    out()

# ── SECTION 6: Summary of clue-matching words ────────────────────────────────
out("## Section 6: Summary — Best Clue-Word Matches Found in Grid")
out()

# Manually compile from the clue search above + notable dictionary finds
out("(See Section 1 for full clue-candidate results and Section 3 for dictionary matches.)")
out()
out("### Cross-reference: Dictionary words that might match clues")
out()

# Thematic words that could match clues
thematic_check = {
    'Cold noise': ['ACHOO', 'COUGH', 'SNEEZE', 'WHEEZE', 'SNIFFLE'],
    'Natural disaster': ['STORM', 'FLOOD', 'QUAKE', 'TREMOR', 'DROUGHT', 'TORNADO', 'CYCLONE'],
    'Place in Greenville NC': ['SCHOOL', 'CHURCH', 'STORE', 'ARENA', 'MUSEUM', 'TRAIN'],
    'Deceive': ['TRICK', 'DUPE', 'CON', 'LIE', 'HOAX', 'CHEAT', 'SWINDLE', 'HOODWINK'],
    'Rats! (2 wds)': ['OHNO', 'DARNIT', 'OHRATS'],
    'Midwesterner': ['IOWAN', 'OHIOAN', 'HOOSIER', 'KANSAN'],
    'Child toy (hyph)': ['YOYO'],
    'Upset': ['IRATE', 'ANGRY', 'RILED', 'VEXED', 'MAD', 'IRKED', 'CROSS'],
    'MrBeast store item': ['HOODIE', 'SHIRT', 'HAT', 'CANDY', 'CAP', 'SNACK'],
    'US landmark (2 wds)': ['HOOVERDAM'],
    'Type of boat': ['CANOE', 'KAYAK', 'SKIFF', 'YACHT', 'SLOOP', 'BARGE', 'SCOW', 'PUNT', 'ARK', 'DHOW'],
    'Literary outlaw (2 wds)': ['ROBIN', 'HOOD', 'ROBINHOOD', 'ZORRO'],
    'What you say when finished': ['DONE', 'HURRAY', 'EUREKA', 'VOILA', 'HOORAY', 'BINGO'],
}

for category, words in thematic_check.items():
    found_in_grid = []
    for word in words:
        results = search_word(word)
        if results:
            for dir_name, path in results:
                _, wc = format_path(path)
                found_in_grid.append((word, dir_name, wc, path))
    if found_in_grid:
        out(f"**{category}:**")
        for word, dir_name, wc, path in found_in_grid:
            path_str, _ = format_path(path)
            out(f"  - {word} — {dir_name} (wildcards: {wc})")
            out(f"    {path_str}")
        out()

# ── Write output ──────────────────────────────────────────────────────────────
output_path = '/Users/at/Desktop/code/other/mrbeast_puzzle/puzzles/01_wells_africa/scratch_wordsearch.md'
with open(output_path, 'w') as f:
    f.write('\n'.join(output_lines) + '\n')

print(f"\n\nResults written to {output_path}")
print(f"Total lines: {len(output_lines)}")
