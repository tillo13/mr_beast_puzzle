# Puzzle-Solving Stage Gates

> Verification gates to prevent lost work across sessions and multi-agent tasks.
> Adapted from stage-gate QA methodology for research/puzzle-solving repos.

## Core Rule

Every phase produces artifacts. Every artifact gets verified before advancing. Nothing advances past a gate until checks pass.

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  STAGE N    │────>│  TEST GATE   │────>│  STAGE N+1  │
│  (AI works) │     │  (verify)    │     │  (AI works)  │
└─────────────┘     └──────────────┘     └─────────────┘
                         │
                    FAIL │
                         v
                    Fix before
                    continuing
```

---

## Gate 1: State File Integrity

**Rule:** `results/state.json` must always be valid and current.

```bash
#!/bin/bash
# verify_state.sh
PASS=0; FAIL=0

if [ -f "results/state.json" ]; then
  python3 -c "import json; d=json.load(open('results/state.json')); assert 'puzzles' in d; assert 'meta_clue' in d; assert 'pending' in d" 2>/dev/null
  if [ $? -eq 0 ]; then ((PASS++)); echo "  OK: state.json is valid with required keys"
  else ((FAIL++)); echo "  FAIL: state.json missing required keys (puzzles, meta_clue, pending)"; fi
else
  ((FAIL++)); echo "  FAIL: results/state.json does not exist"
fi

echo "STATE FILE GATE: $PASS passed, $FAIL failed"
[ $FAIL -eq 0 ] && echo "CLEAR" || echo "FIX BEFORE CONTINUING"
```

---

## Gate 2: Puzzle Solution Verification

**Rule:** Before moving to the next puzzle, verify solutions are on disk.

```bash
#!/bin/bash
# verify_puzzle_solutions.sh
PASS=0; FAIL=0

for dir in puzzles/*/; do
  puzzle=$(basename "$dir")
  file_count=$(find "$dir" -type f | wc -l | tr -d ' ')
  if [ "$file_count" -gt 0 ]; then
    ((PASS++)); echo "  OK: $puzzle has $file_count file(s)"
  else
    echo "  INFO: $puzzle is empty (not started)"
  fi
done

# Check that any solved puzzle has a notes.md with real content
for notes in puzzles/*/notes.md; do
  if [ -f "$notes" ]; then
    size=$(wc -c < "$notes" | tr -d ' ')
    if [ "$size" -gt 50 ]; then
      ((PASS++)); echo "  OK: $notes has content ($size bytes)"
    else
      ((FAIL++)); echo "  FAIL: $notes exists but is nearly empty"
    fi
  fi
done

echo "PUZZLE SOLUTIONS GATE: $PASS passed, $FAIL failed"
[ $FAIL -eq 0 ] && echo "CLEAR" || echo "FIX BEFORE CONTINUING"
```

---

## Gate 3: Session Handoff

**Rule:** `results/state.json` and `docs/progress.md` must be current before ending a session.

```python
# verify_session_handoff.py
import json, os, sys

STATE = "results/state.json"
PROGRESS = "docs/progress.md"

if not os.path.exists(STATE):
    print("FAIL: results/state.json missing"); sys.exit(1)
if not os.path.exists(PROGRESS):
    print("FAIL: docs/progress.md missing"); sys.exit(1)

data = json.load(open(STATE))
for key in ["last_updated", "last_session", "puzzles", "pending"]:
    if key not in data:
        print(f"FAIL: Missing key '{key}' in state.json"); sys.exit(1)

solved = sum(1 for p in data["puzzles"].values() if p.get("grid_solved"))
words = sum(1 for w in data["meta_clue"]["words"] if w is not None)

print(f"Last session: {data['last_session']}")
print(f"Puzzles with grids solved: {solved}/10")
print(f"Answer words extracted: {words}/9")
print(f"Pending items: {len(data['pending'])}")
print("SESSION HANDOFF GATE: CLEAR")
```

---

## Gate 4: Pre-Launch Check for Parallel Agents

**Rule:** Before launching the 1-agent-per-puzzle swarm, verify prerequisites.

```bash
#!/bin/bash
# verify_parallel_launch.sh
PASS=0; FAIL=0

# Shared context file exists
if [ -f "puzzles/shared_context.md" ]; then
  size=$(wc -c < "puzzles/shared_context.md" | tr -d ' ')
  if [ "$size" -gt 100 ]; then
    ((PASS++)); echo "  OK: shared_context.md has content"
  else
    ((FAIL++)); echo "  FAIL: shared_context.md is too small — extraction keys missing?"
  fi
else
  ((FAIL++)); echo "  FAIL: puzzles/shared_context.md does not exist"
fi

# All 9 puzzle directories exist
for i in 01_wells_africa 02_lifechange 03_dirtiest_beach 04_experiences 05_pokemon_go 06_wilderness 07_adopted_dogs 08_pyramids 09_circle; do
  if [ -d "puzzles/$i" ]; then
    ((PASS++))
  else
    ((FAIL++)); echo "  FAIL: puzzles/$i directory missing"
  fi
done

echo "PARALLEL LAUNCH GATE: $PASS passed, $FAIL failed"
[ $FAIL -eq 0 ] && echo "CLEAR TO LAUNCH" || echo "FIX BEFORE LAUNCHING"
```

---

## When to Run Each Gate

| Gate | When |
|------|------|
| State File | After any agent updates results/state.json |
| Puzzle Solution | Before moving from one puzzle to the next |
| Session Handoff | End of every work session |
| Parallel Launch | Before launching the 9-agent swarm |
