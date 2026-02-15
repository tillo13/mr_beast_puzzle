#!/usr/bin/env python3
"""
Systematic extraction attempts for P6 (Wilderness / Tents and Trees).
Tries many interpretations of vault rim key 8-4-1-1 and other extraction methods.
"""

# The original grid (0-indexed)
GRID = [
    ['2', '4', 'T', '8', '_', '1', '9', '_', '_', '_', '_', '2', '_', '6', '_'],  # R0
    ['T', '5', '6', '_', '3', 'T', 'T', '3', '_', '9', '1', '9', 'T', '7', 'T'],  # R1
    ['8', '_', '4', '5', 'T', '1', '6', '_', '8', 'T', 'T', '5', '6', '_', '8'],  # R2
    ['_', '1', 'T', '3', '7', '7', '_', '8', '_', '7', '9', '_', '6', '5', 'T'],  # R3
    ['_', '9', '2', '_', '3', 'T', '9', 'T', '7', '_', '_', '2', 'T', '4', '4'],  # R4
    ['4', 'T', '7', '_', '_', '5', '_', '6', '_', '_', '1', '_', '3', '_', '_'],  # R5
    ['_', '2', '_', '_', '_', '_', '_', '8', '_', '2', 'T', '4', '_', '_', '8'],  # R6
    ['3', 'T', '1', '_', '_', '_', '6', 'T', '2', '_', '3', '_', '_', '3', 'T'],  # R7
    ['_', '4', '_', '1', '_', '_', '7', '4', '_', '6', '_', '_', '2', '_', '5'],  # R8
    ['_', '_', '2', 'T', '4', '5', 'T', '8', '1', 'T', '9', '8', 'T', '4', '3'],  # R9
    ['_', '_', '_', '3', '8', '_', '6', '7', 'T', '2', '_', '_', '6', '5', 'T'],  # R10
    ['_', '4', '1', '7', 'T', '5', '_', '_', '9', '5', '_', '_', '_', '6', '7'],  # R11
    ['8', 'T', 'T', '3', '6', '9', '_', '2', 'T', 'T', '4', '_', '9', 'T', '1'],  # R12
    ['_', '6', '7', '_', '2', 'T', '1', '_', '4', '6', '_', '1', 'T', '3', '_'],  # R13
    ['_', '5', 'T', '2', '_', '3', '_', '_', '_', '_', '5', 'T', '4', '_', '_'],  # R14
]

# Tent positions from solved puzzle (0-indexed, reading order)
TENTS = [
    (0,0), (0,3), (0,5), (0,14),
    (1,7), (1,9), (1,11),
    (2,5),
    (3,3), (3,10), (3,12),
    (4,1), (4,8), (4,14),
    (5,5),
    (6,7), (6,11), (6,14),
    (7,2),
    (8,9),
    (9,4), (9,7), (9,11),
    (10,13),
    (11,1), (11,5), (11,8),
    (12,3), (12,10), (12,12),
    (13,6), (13,8),
    (14,1), (14,10), (14,12),
]

# Tree positions (0-indexed, reading order)
TREES = [
    (0,2),
    (1,0), (1,5), (1,6), (1,12), (1,14),
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
    (14,2), (14,11),
]

# Row/Col tent counts
ROW_COUNTS = [4, 3, 1, 3, 3, 1, 3, 1, 1, 3, 1, 3, 3, 2, 3]
COL_COUNTS = [1, 3, 1, 3, 1, 4, 1, 3, 3, 2, 3, 3, 3, 1, 3]

# Vault rim key for 4-letter word
KEY = [8, 4, 1, 1]

# Common 4-letter words (comprehensive)
WORDS_4 = set()
try:
    with open('/usr/share/dict/words') as f:
        for line in f:
            w = line.strip().upper()
            if len(w) == 4 and w.isalpha():
                WORDS_4.add(w)
except:
    # Fallback: some common 4-letter words
    WORDS_4 = {'CASH','EPIC','TENT','WILD','CAMP','FIRE','HUNT','FIND','SEEK',
                'LOOK','OPEN','GOLD','CODE','WORD','GAME','CLUE','SIGN','LOCK',
                'SAFE','DOOR','COIN','TRUE','REAL','EACH','NEXT','LAST','WITH',
                'FROM','YOUR','THIS','THAT','HAVE','BEEN','WERE','WILL','WHAT',
                'WHEN','TREE','WOOD','BEAR','FISH','LAKE','HIKE','PATH','RAIN',
                'WIND','BARK','LEAF','SEED','ROOT','VINE','FERN','MOSS','DUSK',
                'DAWN','MOON','STAR'}

print(f"Loaded {len(WORDS_4)} 4-letter words")

# Get number at grid position
def grid_val(r, c):
    if 0 <= r < 15 and 0 <= c < 15:
        v = GRID[r][c]
        if v not in ('T', '_'):
            return int(v)
    return None

# Numbers at tent positions (reading order)
tent_nums = []
for r, c in TENTS:
    v = grid_val(r, c)
    tent_nums.append(v)  # None for blank

print(f"\n=== TENT NUMBERS (reading order) ===")
for i, ((r,c), v) in enumerate(zip(TENTS, tent_nums)):
    print(f"  Tent {i+1}: ({r},{c}) = {v}")

def to_letter_a1(n):
    """A=1, B=2, ... I=9"""
    if n is not None and 1 <= n <= 26:
        return chr(n + 64)
    return '?'

def to_letter_a0(n):
    """A=0, B=1, ... Z=25"""
    if n is not None and 0 <= n <= 25:
        return chr(n + 65)
    return '?'

def check_word(letters, method_name):
    word = ''.join(letters).upper()
    if '?' not in word and word in WORDS_4:
        print(f"  *** WORD FOUND: {word} (method: {method_name}) ***")
        return True
    return False

found_words = []

print(f"\n{'='*60}")
print(f"=== EXTRACTION ATTEMPTS ===")
print(f"{'='*60}")

# === METHOD 1: Key as tent indices (1-indexed) ===
print(f"\n--- Method 1: Key as tent indices (1-indexed) ---")
for key in [[8,4,1,1], [1,1,4,8]]:
    letters = []
    for k in key:
        if 1 <= k <= 35:
            v = tent_nums[k-1]
            letters.append(to_letter_a1(v) if v else '?')
        else:
            letters.append('?')
    word = ''.join(letters)
    is_match = word.upper() in WORDS_4
    print(f"  Key {key}: tent values = {[tent_nums[k-1] for k in key]}, A=1 letters = {word} {'*** MATCH ***' if is_match else ''}")

# === METHOD 2: Key as tent indices (0-indexed) ===
print(f"\n--- Method 2: Key as tent indices (0-indexed) ---")
for key in [[8,4,1,1], [7,3,0,0], [1,1,4,8]]:
    letters = []
    for k in key:
        if 0 <= k < 35:
            v = tent_nums[k]
            letters.append(to_letter_a1(v) if v else '?')
    word = ''.join(letters)
    is_match = word.upper() in WORDS_4
    print(f"  Key {key}: tent values = {[tent_nums[k] for k in key]}, A=1 letters = {word} {'*** MATCH ***' if is_match else ''}")

# === METHOD 3: Key as row indices → read tent numbers in those rows ===
print(f"\n--- Method 3: Key as row indices (1-indexed), take first tent's number ---")
for idx_mode in ['first', 'last', 'only']:
    letters = []
    nums = []
    for k in KEY:
        row_idx = k - 1  # 0-indexed
        row_tents = [(r,c) for r,c in TENTS if r == row_idx]
        if not row_tents:
            nums.append(None)
            letters.append('?')
            continue
        if idx_mode == 'first':
            r, c = row_tents[0]
        elif idx_mode == 'last':
            r, c = row_tents[-1]
        else:  # 'only' - only if row has exactly 1 tent
            if len(row_tents) == 1:
                r, c = row_tents[0]
            else:
                nums.append(None)
                letters.append('?')
                continue
        v = grid_val(r, c)
        nums.append(v)
        letters.append(to_letter_a1(v) if v else '?')
    word = ''.join(letters)
    is_match = word.upper() in WORDS_4 and '?' not in word
    print(f"  {idx_mode}: nums = {nums}, letters = {word} {'*** MATCH ***' if is_match else ''}")

# === METHOD 4: Key as column indices → tent numbers ===
print(f"\n--- Method 4: Key as column indices (1-indexed), take first tent's number ---")
for idx_mode in ['first', 'last']:
    letters = []
    nums = []
    for k in KEY:
        col_idx = k - 1
        col_tents = [(r,c) for r,c in TENTS if c == col_idx]
        if not col_tents:
            nums.append(None)
            letters.append('?')
            continue
        if idx_mode == 'first':
            r, c = col_tents[0]
        else:
            r, c = col_tents[-1]
        v = grid_val(r, c)
        nums.append(v)
        letters.append(to_letter_a1(v) if v else '?')
    word = ''.join(letters)
    is_match = word.upper() in WORDS_4 and '?' not in word
    print(f"  {idx_mode}: nums = {nums}, letters = {word} {'*** MATCH ***' if is_match else ''}")

# === METHOD 5: Key as row indices → count tents in that row → letter ===
print(f"\n--- Method 5: Row tent counts as letters ---")
nums = [ROW_COUNTS[k-1] for k in KEY]
letters = [to_letter_a1(n) for n in nums]
word = ''.join(letters)
print(f"  Row counts for rows {KEY}: {nums} → {word}")

# Column version
nums_c = [COL_COUNTS[k-1] for k in KEY]
letters_c = [to_letter_a1(n) for n in nums_c]
word_c = ''.join(letters_c)
print(f"  Col counts for cols {KEY}: {nums_c} → {word_c}")

# === METHOD 6: Key as grid cell coordinates ===
print(f"\n--- Method 6: Key as (row,col) coordinate pairs ---")
pairs = [(KEY[0], KEY[1]), (KEY[2], KEY[3])]
for base in [0, 1]:
    nums = []
    for r, c in pairs:
        ri, ci = r - base, c - base
        v = grid_val(ri, ci)
        nums.append(v)
    print(f"  Pairs (base-{base}): {pairs} → values {nums}")

# Also try all 4 as separate positions
for base in [0, 1]:
    for fixed_col in range(15):
        nums = [grid_val(k-base, fixed_col) for k in KEY]
        if all(n is not None for n in nums):
            letters = [to_letter_a1(n) for n in nums]
            word = ''.join(letters)
            if word.upper() in WORDS_4:
                print(f"  Rows {KEY} (base-{base}), fixed col {fixed_col}: {nums} → {word} *** MATCH ***")

    for fixed_row in range(15):
        nums = [grid_val(fixed_row, k-base) for k in KEY]
        if all(n is not None for n in nums):
            letters = [to_letter_a1(n) for n in nums]
            word = ''.join(letters)
            if word.upper() in WORDS_4:
                print(f"  Fixed row {fixed_row}, cols {KEY} (base-{base}): {nums} → {word} *** MATCH ***")

# === METHOD 7: Sum tent numbers per row, use as letter ===
print(f"\n--- Method 7: Sum of tent numbers per row → letter ---")
row_sums = {}
for i in range(15):
    row_t = [(r,c) for r,c in TENTS if r == i]
    s = sum(grid_val(r,c) or 0 for r,c in row_t)
    row_sums[i] = s

for k in KEY:
    row_idx = k - 1
    print(f"  Row {k}: sum = {row_sums[row_idx]} → {to_letter_a1(row_sums[row_idx])}")

# === METHOD 8: Tree-tent direction encoding ===
print(f"\n--- Method 8: Tree-tent direction encoding ---")
# Build tree-tent pairs
tent_set = set(TENTS)
tree_tent_pairs = []
for tr, tc in TREES:
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = tr+dr, tc+dc
        if (nr, nc) in tent_set:
            # Check if this tent hasn't been paired yet
            tree_tent_pairs.append(((tr,tc), (nr,nc), (dr,dc)))
            break

# Direction mapping: Up(-1,0)=U, Down(1,0)=D, Left(0,-1)=L, Right(0,1)=R
dir_map = {(-1,0): 'U', (1,0): 'D', (0,-1): 'L', (0,1): 'R'}
dir_num = {(-1,0): 1, (1,0): 2, (0,-1): 3, (0,1): 4}
directions = [dir_map.get(d, '?') for _, _, d in tree_tent_pairs]
dir_nums = [dir_num.get(d, 0) for _, _, d in tree_tent_pairs]
print(f"  Directions: {''.join(directions)}")
print(f"  Dir numbers: {dir_nums}")

# Use key to index into direction list
for base in [0, 1]:
    indices = [k-base for k in KEY]
    if all(0 <= i < len(dir_nums) for i in indices):
        vals = [dir_nums[i] for i in indices]
        dirs = [directions[i] for i in indices]
        print(f"  Key {KEY} (base-{base}): directions = {dirs}, nums = {vals}")

# === METHOD 9: Brute force — try every 4-combination of tent numbers ===
print(f"\n--- Method 9: Brute force search for words in tent numbers ---")
print("  Searching all ways to pick 4 tent numbers that form a word (A=1)...")
from itertools import combinations
hits = []
for combo in combinations(range(35), 4):
    vals = [tent_nums[i] for i in combo]
    if any(v is None for v in vals):
        continue
    word = ''.join(to_letter_a1(v) for v in vals)
    if word.upper() in WORDS_4:
        hits.append((combo, vals, word))
if hits:
    for combo, vals, word in hits[:30]:
        print(f"  Tents {[c+1 for c in combo]}: values {vals} → {word}")
    if len(hits) > 30:
        print(f"  ... and {len(hits)-30} more")
else:
    print("  No 4-letter words found from tent number combinations (A=1)")

# === METHOD 10: Numbers at NON-tent cells, key selects from those ===
print(f"\n--- Method 10: Non-tent numbered cells, key selects ---")
non_tent_nums = []
for r in range(15):
    for c in range(15):
        if (r,c) not in tent_set and (r,c) not in set(TREES):
            v = grid_val(r, c)
            if v is not None:
                non_tent_nums.append((r, c, v))

print(f"  {len(non_tent_nums)} non-tent numbered cells")
for base in [0, 1]:
    indices = [k-base for k in KEY]
    if all(0 <= i < len(non_tent_nums) for i in indices):
        vals = [non_tent_nums[i][2] for i in indices]
        letters = [to_letter_a1(v) for v in vals]
        word = ''.join(letters)
        is_match = word.upper() in WORDS_4
        print(f"  Key {KEY} (base-{base}): cells = {[(non_tent_nums[i][0], non_tent_nums[i][1]) for i in indices]}, values = {vals}, letters = {word} {'*** MATCH ***' if is_match else ''}")

# === METHOD 11: "CASH TENT" — is CASH the answer? Check if extractable ===
print(f"\n--- Method 11: Can we extract CASH? ---")
# C=3, A=1, S=19, H=8 in standard alphabet
# In A=1 mapping, we need values 3, 1, 19, 8 — but max digit is 9
# Try other mappings
print("  CASH in A=1: C=3, A=1, S=19, H=8 — S=19 impossible with digits 1-9")
print("  Trying CASH with LIFECHANGE mapping (L=1,I=2,F=3,E=4,C=5,H=6,A=7,N=8,G=9):")
lc_map = {'L':1,'I':2,'F':3,'E':4,'C':5,'H':6,'A':7,'N':8,'G':9}
lc_rev = {v:k for k,v in lc_map.items()}
# CASH: C=5, A=7, S=not in LIFECHANGE
print("  S not in LIFECHANGE alphabet — CASH not extractable via LIFECHANGE mapping")

# === METHOD 12: Full tent number → LIFECHANGE letter mapping ===
print(f"\n--- Method 12: Tent numbers via LIFECHANGE mapping ---")
lc_letters = [lc_rev.get(v, '?') if v else '?' for v in tent_nums]
print(f"  Full sequence: {''.join(lc_letters)}")
# Try key
for base in [0, 1]:
    indices = [k-base for k in KEY]
    if all(0 <= i < len(lc_letters) for i in indices):
        word = ''.join(lc_letters[i] for i in indices)
        is_match = word.upper() in WORDS_4 and '?' not in word
        print(f"  Key {KEY} (base-{base}): {word} {'*** MATCH ***' if is_match else ''}")

# === METHOD 13: Try EVERY possible 4-number key against tent list ===
print(f"\n--- Method 13: Exhaustive key search (what key gives a word?) ---")
found_keys = []
for a in range(1, 36):
    for b in range(1, 36):
        for c in range(1, 36):
            for d in range(1, 36):
                vals = [tent_nums[a-1], tent_nums[b-1], tent_nums[c-1], tent_nums[d-1]]
                if any(v is None for v in vals):
                    continue
                word = ''.join(to_letter_a1(v) for v in vals)
                if word.upper() in WORDS_4:
                    found_keys.append(([a,b,c,d], vals, word))

# Filter to interesting keys (not all same index, reasonable pattern)
unique_words = set()
for key_used, vals, word in found_keys:
    unique_words.add(word.upper())

print(f"  Found {len(found_keys)} key combinations producing {len(unique_words)} unique words")
print(f"  Unique words: {sorted(unique_words)[:50]}")

# Show keys that produce common/interesting words
interesting = ['CASH', 'EPIC', 'WILD', 'CAMP', 'FIRE', 'HUNT', 'FIND', 'SEEK',
               'GOLD', 'EACH', 'CLUE', 'GAME', 'CODE', 'WOOD', 'BEAR', 'HIKE',
               'TENT', 'TREE', 'RAIN', 'GEAR', 'AIDE', 'FACE', 'CAGE', 'ACHE',
               'HIDE', 'DICE', 'EDGE', 'FADE', 'HEED', 'FEED', 'DEED', 'GIBE',
               'HUGE', 'DAZE', 'FAZE', 'GAZE', 'HAZE']
for target in interesting:
    matches = [(k, v, w) for k, v, w in found_keys if w.upper() == target]
    if matches:
        print(f"\n  {target}: {len(matches)} ways to extract it")
        for k, v, w in matches[:3]:
            print(f"    Key {k}: tent values {v}")

# === METHOD 14: Tent-number → position in alphabet of grid keyword ===
print(f"\n\n--- Method 14: Grid keyword mappings ---")
keywords = {
    'ADVENTURE': {c: i+1 for i, c in enumerate('ADVENTURE') if c not in 'ADVENTURE'[:i]},
    'CAMPFIRES': {c: i+1 for i, c in enumerate('CAMPFIRES')},
    'SURVIVING': {c: i+1 for i, c in enumerate('SURVIVING')},
    'WILDCAMPE': {c: i+1 for i, c in enumerate('WILDCAMPE')},
}
# Build proper mappings (handle duplicates by taking first occurrence)
for kw_name in list(keywords.keys()):
    mapping = {}
    idx = 1
    for ch in kw_name:
        if ch not in mapping:
            mapping[ch] = idx
        idx += 1
    rev = {v: k for k, v in mapping.items()}
    keywords[kw_name] = rev
    # Try extracting from tent numbers
    letters = [rev.get(v, '?') if v else '?' for v in tent_nums]
    full = ''.join(letters)
    print(f"  {kw_name}: mapping = {rev}")
    print(f"    Tent letters: {full}")
    # Check if any 4 consecutive tent letters form a word
    for i in range(len(letters) - 3):
        word = ''.join(letters[i:i+4])
        if '?' not in word and word.upper() in WORDS_4:
            print(f"    *** Consecutive match at tent {i+1}: {word} ***")

# === METHOD 15: What if key numbers mean something for the grid itself? ===
print(f"\n--- Method 15: Grid cell direct reads ---")
print("  Reading cells at (row, col) for various interpretations of 8-4-1-1:")
# As 4 separate row indices, reading grid diagonal
for offset in range(15):
    vals = []
    for i, k in enumerate(KEY):
        r = k - 1  # 0-indexed
        c = (offset + i) % 15
        v = grid_val(r, c)
        vals.append(v)
    if all(v is not None for v in vals):
        word = ''.join(to_letter_a1(v) for v in vals)
        if word.upper() in WORDS_4:
            print(f"  Rows {[k-1 for k in KEY]}, cols starting at {offset}: {vals} → {word} *** MATCH ***")

# === METHOD 16: Tent column positions as letters ===
print(f"\n--- Method 16: Tent column positions as letters (A=0 or A=1) ---")
tent_cols = [c for r, c in TENTS]
for base in [0, 1]:
    for key_base in [0, 1]:
        indices = [k-key_base for k in KEY]
        if all(0 <= i < 35 for i in indices):
            cols = [tent_cols[i] for i in indices]
            letters_a0 = [chr(c + 65) for c in cols]  # A=0
            letters_a1 = [chr(c + 64) if c > 0 else '?' for c in cols]  # A=1
            w0 = ''.join(letters_a0)
            w1 = ''.join(letters_a1)
            if w0.upper() in WORDS_4:
                print(f"  Key base-{key_base}, A=col: tent cols {cols} → {w0} *** MATCH ***")
            if w1.upper() in WORDS_4 and '?' not in w1:
                print(f"  Key base-{key_base}, A=col+1: tent cols {cols} → {w1} *** MATCH ***")

# === METHOD 17: Tent row positions as letters ===
print(f"\n--- Method 17: Tent row positions as letters ---")
tent_rows = [r for r, c in TENTS]
for key_base in [0, 1]:
    indices = [k-key_base for k in KEY]
    if all(0 <= i < 35 for i in indices):
        rows = [tent_rows[i] for i in indices]
        letters = [chr(r + 65) for r in rows]  # A=0
        word = ''.join(letters)
        if word.upper() in WORDS_4:
            print(f"  Key base-{key_base}: tent rows {rows} → {word} *** MATCH ***")

print(f"\n{'='*60}")
print("DONE. Check for *** MATCH *** or *** WORD FOUND *** above.")
print(f"{'='*60}")
