# Test Suite Methodology: Gate Every Stage Before Moving Forward

*Inspired by helk1d's "13 no-bs lessons" + community TDD discussion, adapted for Andy's workflow.*

---

## Core Philosophy

The AI writes code. You own the tests. Tests are the product — code is disposable.

Never let AI write both the implementation AND the tests that validate it. That proves nothing. You design what "correct" looks like. AI figures out how to get there. Automated gates prevent bad output from surviving.

Every stage of building produces an artifact. Every artifact gets a test harness before the next stage begins. If the harness fails, the AI rewrites the code — not the tests.

---

## The Stage-Gate Pattern

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  STAGE N    │────▶│  TEST GATE   │────▶│  STAGE N+1  │
│  (AI builds)│     │  (You own)   │     │  (AI builds) │
└─────────────┘     └──────────────┘     └─────────────┘
                         │
                    FAIL │
                         ▼
                    AI rewrites
                    Stage N code
                    (tests don't change)
```

The rule: **nothing advances past a gate until every test passes.** The AI can retry as many times as it needs. The tests are frozen unless YOU decide the spec changed.

---

## Stage 0: Foundation & Project Setup

**What's produced:** Directory structure, dependencies, config files, CLAUDE.md/AGENTS.md

**Test harness:**

```bash
# foundation_gate.sh — run before writing any feature code

#!/bin/bash
PASS=0
FAIL=0

# 1. Required files exist
for f in app.py requirements.txt app.yaml .gitignore CLAUDE.md; do
  if [ -f "$f" ]; then ((PASS++)); else echo "MISSING: $f"; ((FAIL++)); fi
done

# 2. Dependencies install cleanly
pip install -r requirements.txt --dry-run > /dev/null 2>&1
if [ $? -eq 0 ]; then ((PASS++)); else echo "FAIL: requirements.txt broken"; ((FAIL++)); fi

# 3. App imports without errors
python -c "import app" 2>/dev/null
if [ $? -eq 0 ]; then ((PASS++)); else echo "FAIL: app.py won't import"; ((FAIL++)); fi

# 4. No secrets in repo
if grep -r "sk-" . --include="*.py" --include="*.yaml" | grep -v ".gitignore"; then
  echo "FAIL: secrets found in code"; ((FAIL++))
else ((PASS++)); fi

# 5. Directory structure matches spec
for d in templates static utilities; do
  if [ -d "$d" ]; then ((PASS++)); else echo "MISSING DIR: $d"; ((FAIL++)); fi
done

echo "========================"
echo "FOUNDATION GATE: $PASS passed, $FAIL failed"
[ $FAIL -eq 0 ] && echo "✅ CLEAR TO PROCEED" || echo "❌ FIX BEFORE CONTINUING"
```

**Why this matters:** This is helk1d's Point 1 — the first few thousand lines determine everything. If the foundation is wrong, every AI-generated file after this replicates the wrong patterns.

---

## Stage 1: Database Schema & Data Layer

**What's produced:** Schema SQL, postgres_utils.py (or sqlite_utils.py), migration files

**Test harness:**

```python
# test_data_layer.py

import sys
sys.path.append('.')

TESTS_PASSED = 0
TESTS_FAILED = 0

def test(name, condition):
    global TESTS_PASSED, TESTS_FAILED
    if condition:
        TESTS_PASSED += 1
        print(f"  ✅ {name}")
    else:
        TESTS_FAILED += 1
        print(f"  ❌ {name}")

print("DATA LAYER GATE")
print("=" * 50)

# 1. Utils module imports
try:
    from utilities.postgres_utils import get_db_connection
    test("postgres_utils imports", True)
except Exception as e:
    test(f"postgres_utils imports ({e})", False)

# 2. Connection works
try:
    conn = get_db_connection()
    test("database connection", conn is not None)
    conn.close()
except Exception as e:
    test(f"database connection ({e})", False)

# 3. Required tables exist
REQUIRED_TABLES = ["users", "sessions"]  # customize per project
try:
    conn = get_db_connection()
    cur = conn.cursor()
    for table in REQUIRED_TABLES:
        cur.execute(f"SELECT 1 FROM information_schema.tables WHERE table_name='{table}'")
        test(f"table '{table}' exists", cur.fetchone() is not None)
    conn.close()
except Exception as e:
    test(f"table check ({e})", False)

# 4. CRUD operations work (use a test record, clean up after)
try:
    conn = get_db_connection()
    cur = conn.cursor()
    # INSERT
    cur.execute("INSERT INTO users (name, email) VALUES ('__TEST__', '__test@test.com__') RETURNING id")
    test_id = cur.fetchone()[0]
    test("INSERT works", test_id is not None)
    # SELECT
    cur.execute("SELECT name FROM users WHERE id = %s", (test_id,))
    test("SELECT works", cur.fetchone()[0] == '__TEST__')
    # DELETE (cleanup)
    cur.execute("DELETE FROM users WHERE id = %s", (test_id,))
    conn.commit()
    test("DELETE cleanup", True)
    conn.close()
except Exception as e:
    test(f"CRUD operations ({e})", False)

# 5. No raw SQL in app.py (should all be in utils)
with open("app.py", "r") as f:
    content = f.read()
    has_raw_sql = "SELECT " in content or "INSERT " in content or "UPDATE " in content
    test("no raw SQL in app.py (should be in utils)", not has_raw_sql)

print("=" * 50)
print(f"DATA LAYER GATE: {TESTS_PASSED} passed, {TESTS_FAILED} failed")
if TESTS_FAILED == 0:
    print("✅ CLEAR TO PROCEED")
else:
    print("❌ FIX BEFORE CONTINUING")
```

**Why this matters:** helk1d's Point 6 — database schema decisions can't be done by a one-liner prompt. Lock the schema down with tests before building features on top of it.

---

## Stage 2: Core Routes & API Endpoints

**What's produced:** Flask routes, API endpoints, template rendering

**Test harness:**

```python
# test_routes.py

import sys
sys.path.append('.')
from app import app

TESTS_PASSED = 0
TESTS_FAILED = 0

def test(name, condition):
    global TESTS_PASSED, TESTS_FAILED
    if condition:
        TESTS_PASSED += 1
        print(f"  ✅ {name}")
    else:
        TESTS_FAILED += 1
        print(f"  ❌ {name}")

print("ROUTES GATE")
print("=" * 50)

client = app.test_client()

# 1. Landing page loads
resp = client.get("/")
test("GET / returns 200", resp.status_code == 200)
test("GET / has content", len(resp.data) > 100)

# 2. All defined routes respond (no 500s)
EXPECTED_ROUTES = ["/", "/about", "/api/health"]  # customize per project
for route in EXPECTED_ROUTES:
    resp = client.get(route)
    test(f"GET {route} not 500", resp.status_code != 500)

# 3. Health check endpoint
resp = client.get("/api/health")
test("health endpoint returns JSON", resp.content_type == "application/json")

# 4. 404 handling works (not a raw error)
resp = client.get("/nonexistent-page-xyz")
test("404 handled gracefully", resp.status_code == 404)

# 5. No debug mode in production config
test("DEBUG is False", not app.config.get("DEBUG", False))

# 6. Secret key is set (not default)
test("SECRET_KEY is set", app.config.get("SECRET_KEY") not in [None, "", "dev", "change-me"])

print("=" * 50)
print(f"ROUTES GATE: {TESTS_PASSED} passed, {TESTS_FAILED} failed")
if TESTS_FAILED == 0:
    print("✅ CLEAR TO PROCEED")
else:
    print("❌ FIX BEFORE CONTINUING")
```

---

## Stage 3: External Integrations (APIs, Secrets, Third-Party)

**What's produced:** API client code, secrets_utils.py, external service connections

**Test harness:**

```python
# test_integrations.py

import os
import sys
sys.path.append('.')

TESTS_PASSED = 0
TESTS_FAILED = 0

def test(name, condition):
    global TESTS_PASSED, TESTS_FAILED
    if condition:
        TESTS_PASSED += 1
        print(f"  ✅ {name}")
    else:
        TESTS_FAILED += 1
        print(f"  ❌ {name}")

print("INTEGRATIONS GATE")
print("=" * 50)

# 1. Secrets load without exposing values
try:
    from utilities.secrets_utils import get_secret
    test("secrets_utils imports", True)
except Exception as e:
    test(f"secrets_utils imports ({e})", False)

# 2. Required secrets are accessible
REQUIRED_SECRETS = ["DATABASE_URL"]  # customize per project
for secret_name in REQUIRED_SECRETS:
    try:
        val = get_secret(secret_name)
        test(f"secret '{secret_name}' accessible", val is not None and len(val) > 0)
        # Verify it's not hardcoded in any .py file
        import glob
        for pyfile in glob.glob("**/*.py", recursive=True):
            if "venv" in pyfile or "__pycache__" in pyfile:
                continue
            with open(pyfile) as f:
                if val in f.read():
                    test(f"secret '{secret_name}' NOT hardcoded in {pyfile}", False)
    except Exception as e:
        test(f"secret '{secret_name}' ({e})", False)

# 3. External API connectivity (dry-run / ping only)
import requests
EXTERNAL_ENDPOINTS = {
    "GCP Secret Manager": "https://secretmanager.googleapis.com/",
    # "Replicate": "https://api.replicate.com/v1",
    # "Shelly Cloud": "https://shelly-xx-eu.shelly.cloud",
}
for name, url in EXTERNAL_ENDPOINTS.items():
    try:
        resp = requests.head(url, timeout=5)
        test(f"{name} reachable", resp.status_code < 500)
    except Exception as e:
        test(f"{name} reachable ({e})", False)

# 4. No API keys in git-tracked files
import subprocess
result = subprocess.run(
    ["git", "log", "--all", "-p", "--", "*.py", "*.yaml", "*.json"],
    capture_output=True, text=True, timeout=30
)
sensitive_patterns = ["sk-", "AKIA", "-----BEGIN PRIVATE KEY"]
for pattern in sensitive_patterns:
    test(f"no '{pattern}' in git history", pattern not in result.stdout)

print("=" * 50)
print(f"INTEGRATIONS GATE: {TESTS_PASSED} passed, {TESTS_FAILED} failed")
if TESTS_FAILED == 0:
    print("✅ CLEAR TO PROCEED")
else:
    print("❌ FIX BEFORE CONTINUING")
```

**Why this matters:** helk1d's Point 11 — AI doesn't optimize for security by default. This gate catches leaked secrets, broken connections, and hardcoded credentials before they hit production.

---

## Stage 4: Frontend & Templates

**What's produced:** HTML templates, static files, CSS/JS

**Test harness:**

```python
# test_frontend.py

import sys, os, re
sys.path.append('.')
from app import app

TESTS_PASSED = 0
TESTS_FAILED = 0

def test(name, condition):
    global TESTS_PASSED, TESTS_FAILED
    if condition:
        TESTS_PASSED += 1
        print(f"  ✅ {name}")
    else:
        TESTS_FAILED += 1
        print(f"  ❌ {name}")

print("FRONTEND GATE")
print("=" * 50)

client = app.test_client()

# 1. Every template referenced in app.py exists
with open("app.py") as f:
    content = f.read()
templates_referenced = re.findall(r'render_template\(["\']([^"\']+)', content)
for tmpl in templates_referenced:
    test(f"template '{tmpl}' exists", os.path.exists(f"templates/{tmpl}"))

# 2. No broken static file references in templates
for tmpl in templates_referenced:
    path = f"templates/{tmpl}"
    if os.path.exists(path):
        with open(path) as f:
            html = f.read()
        static_refs = re.findall(r'url_for\(["\']static["\'],\s*filename=["\']([^"\']+)', html)
        for ref in static_refs:
            test(f"  static/{ref} exists (in {tmpl})", os.path.exists(f"static/{ref}"))

# 3. Key pages render without Jinja errors
KEY_PAGES = ["/"]  # customize
for page in KEY_PAGES:
    try:
        resp = client.get(page)
        test(f"GET {page} renders cleanly", resp.status_code == 200)
        # Check for common Jinja error signatures in response
        test(f"GET {page} no Jinja errors", b"UndefinedError" not in resp.data)
    except Exception as e:
        test(f"GET {page} ({e})", False)

# 4. No inline secrets in templates
for tmpl in templates_referenced:
    path = f"templates/{tmpl}"
    if os.path.exists(path):
        with open(path) as f:
            html = f.read()
        test(f"no API keys in {tmpl}", "sk-" not in html and "AKIA" not in html)

print("=" * 50)
print(f"FRONTEND GATE: {TESTS_PASSED} passed, {TESTS_FAILED} failed")
if TESTS_FAILED == 0:
    print("✅ CLEAR TO PROCEED")
else:
    print("❌ FIX BEFORE CONTINUING")
```

---

## Stage 5: Deployment Pipeline

**What's produced:** app.yaml, gcloud_deploy.py, git_push.sh

**Test harness:**

```bash
# test_deploy_gate.sh — run BEFORE actual deployment

#!/bin/bash
PASS=0
FAIL=0

check() {
  if [ $? -eq 0 ]; then ((PASS++)); echo "  ✅ $1"; 
  else ((FAIL++)); echo "  ❌ $1"; fi
}

echo "DEPLOYMENT GATE"
echo "=================================================="

# 1. app.yaml is valid
python -c "import yaml; yaml.safe_load(open('app.yaml'))" 2>/dev/null
check "app.yaml parses as valid YAML"

# 2. runtime is set
grep -q "runtime:" app.yaml
check "runtime specified in app.yaml"

# 3. requirements.txt matches what's installed
pip freeze > /tmp/frozen.txt
while IFS= read -r line; do
  pkg=$(echo "$line" | cut -d'=' -f1 | tr '[:upper:]' '[:lower:]')
  grep -qi "$pkg" /tmp/frozen.txt
  check "requirement '$pkg' is installed"
done < <(grep -v "^#" requirements.txt | grep -v "^$")

# 4. No venv in deployment (would be huge)
if grep -q "venv" .gcloudignore 2>/dev/null || ! [ -d "venv" ]; then
  ((PASS++)); echo "  ✅ venv excluded from deploy"
else
  ((FAIL++)); echo "  ❌ venv would be deployed (add to .gcloudignore)"
fi

# 5. gcloud CLI available
gcloud --version > /dev/null 2>&1
check "gcloud CLI installed"

# 6. Correct GCP project
EXPECTED_PROJECT="your-project-id"  # customize
CURRENT=$(gcloud config get-value project 2>/dev/null)
if [ "$CURRENT" = "$EXPECTED_PROJECT" ]; then
  ((PASS++)); echo "  ✅ correct GCP project ($CURRENT)"
else
  ((FAIL++)); echo "  ❌ wrong GCP project (got $CURRENT, expected $EXPECTED_PROJECT)"
fi

# 7. App starts locally without crashing
timeout 5 python -c "
from app import app
with app.test_client() as c:
    r = c.get('/')
    exit(0 if r.status_code == 200 else 1)
" 2>/dev/null
check "app starts and serves locally"

# 8. No debug/dev settings in production config
! grep -q "DEBUG.*True" app.py
check "DEBUG not set to True"

echo "=================================================="
echo "DEPLOYMENT GATE: $PASS passed, $FAIL failed"
[ $FAIL -eq 0 ] && echo "✅ CLEAR TO DEPLOY" || echo "❌ FIX BEFORE DEPLOYING"
```

**Why this matters:** You've been bitten by this — the venv getting deployed (1137 files instead of 9), wrong GCP project, missing requirements. This gate catches all of that before `gcloud app deploy` runs.

---

## Stage 6: Post-Deploy Smoke Test

**What's produced:** Live app on App Engine

**Test harness:**

```python
# test_smoke.py — run AFTER deployment

import requests
import sys

APP_URL = "https://your-app.uc.r.appspot.com"  # customize
TESTS_PASSED = 0
TESTS_FAILED = 0

def test(name, condition):
    global TESTS_PASSED, TESTS_FAILED
    if condition:
        TESTS_PASSED += 1
        print(f"  ✅ {name}")
    else:
        TESTS_FAILED += 1
        print(f"  ❌ {name}")

print(f"SMOKE TEST: {APP_URL}")
print("=" * 50)

# 1. Site is up
try:
    resp = requests.get(APP_URL, timeout=10)
    test("site returns 200", resp.status_code == 200)
    test("response has content", len(resp.text) > 100)
    test("no error page", "Internal Server Error" not in resp.text)
except Exception as e:
    test(f"site reachable ({e})", False)

# 2. HTTPS enforced
try:
    resp = requests.get(APP_URL.replace("https://", "http://"), timeout=10, allow_redirects=False)
    test("HTTP redirects to HTTPS", resp.status_code in [301, 302])
except:
    test("HTTP redirect check", True)  # may not apply on App Engine

# 3. Health endpoint
try:
    resp = requests.get(f"{APP_URL}/api/health", timeout=10)
    test("health endpoint live", resp.status_code == 200)
except Exception as e:
    test(f"health endpoint ({e})", False)

# 4. Database connectivity (via health or a known endpoint)
try:
    resp = requests.get(f"{APP_URL}/api/health", timeout=10)
    data = resp.json()
    test("database connected", data.get("db") == "ok" or resp.status_code == 200)
except:
    test("database check (no health endpoint?)", False)

# 5. No sensitive info exposed
try:
    resp = requests.get(APP_URL, timeout=10)
    test("no stack traces in response", "Traceback" not in resp.text)
    test("no debug info exposed", "FLASK_ENV" not in resp.text)
except:
    pass

print("=" * 50)
print(f"SMOKE TEST: {TESTS_PASSED} passed, {TESTS_FAILED} failed")
if TESTS_FAILED == 0:
    print("✅ DEPLOY VERIFIED")
else:
    print("⚠️  ISSUES FOUND — check logs: gcloud app logs tail -s default")
```

---

## The Master Gate Runner

```bash
# run_all_gates.sh — full pipeline check

#!/bin/bash
echo "╔══════════════════════════════════════════╗"
echo "║     FULL STAGE-GATE TEST PIPELINE        ║"
echo "╚══════════════════════════════════════════╝"
echo ""

STAGE=0
run_gate() {
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "  STAGE $STAGE: $1"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    eval "$2"
    if [ $? -ne 0 ]; then
        echo ""
        echo "🛑 PIPELINE STOPPED AT STAGE $STAGE: $1"
        echo "   Fix failures above before continuing."
        exit 1
    fi
    ((STAGE++))
}

run_gate "Foundation"       "bash tests/foundation_gate.sh"
run_gate "Data Layer"       "python tests/test_data_layer.py"
run_gate "Routes"           "python tests/test_routes.py"
run_gate "Integrations"     "python tests/test_integrations.py"
run_gate "Frontend"         "python tests/test_frontend.py"
run_gate "Deploy Readiness" "bash tests/test_deploy_gate.sh"

echo ""
echo "╔══════════════════════════════════════════╗"
echo "║     ✅ ALL GATES PASSED                  ║"
echo "║     Safe to deploy.                      ║"
echo "╚══════════════════════════════════════════╝"
```

---

## For Non-Web Projects (ComfyUI, Image Gen, Video Pipelines)

The same stage-gate pattern applies, just different gates:

| Stage | What's Produced | Gate Checks |
|-------|----------------|-------------|
| 0. Setup | Python script, model paths, config | Models exist on disk, imports work, VRAM check |
| 1. Single run | One image/video output | Output file exists, expected dimensions, not corrupted |
| 2. Parameter sweep | Batch outputs at different settings | All combinations complete, timing logged, no OOM |
| 3. Quality check | Human review of outputs | Outputs match expected style (manual gate) |
| 4. Pipeline integration | End-to-end workflow | Full pipeline runs unattended, logs clean |

Example — your ComfyUI stress test harness was already doing this:

```python
# This IS a stage gate — you just didn't call it that
if not tester.run_quick_validation_test():
    print("❌ Validation test failed - stopping here")
    print("💡 Fix the validation issues before running full test suite")
    return False

# Only proceed to full suite if validation passes
print("🚀 Starting full tests...")
success = tester.run_all_tests(max_workers=MAX_WORKERS)
```

---

## Rules for Working with AI Under This System

1. **You write the test. AI writes the code.** Never the reverse.

2. **Tests are frozen once written.** AI cannot modify tests without your explicit approval and a written justification.

3. **Every stage produces a gate script.** No stage is "too small" for a test. If it produces a file, that file gets checked.

4. **Gates run automatically.** Put them in git hooks, CI/CD, or at minimum a single `run_all_gates.sh` you execute before every deploy.

5. **Failures are information.** When a gate fails, that's the AI's problem to solve. Your job is to read the failure message and decide if the test is wrong (rare) or the code is wrong (common).

6. **Git diff review is the final human gate.** Even after all automated gates pass, review the diff for semantic correctness. The AI might use `created_at` as a fallback for `birth_date` — tests won't catch that, but you will.

7. **One doc per feature, one gate per stage.** Don't let documentation sprawl. If you can't describe the feature and its tests in one file, the feature is too big.

---

## Quick-Start Checklist for a New Project

- [ ] Create `tests/` directory
- [ ] Write `foundation_gate.sh` FIRST (before any feature code)
- [ ] Add `test_data_layer.py` when database is introduced
- [ ] Add `test_routes.py` when first route is written
- [ ] Add `test_integrations.py` when first external API is connected
- [ ] Add `test_frontend.py` when templates exist
- [ ] Add `test_deploy_gate.sh` before first deployment
- [ ] Add `test_smoke.py` after first deployment
- [ ] Wire into `run_all_gates.sh`
- [ ] Add to CLAUDE.md: "Run `bash run_all_gates.sh` before any deploy"

---

## Puzzle-Solving Stage Gates (MrBeast Puzzle Specific)

The same stage-gate pattern applies to research/puzzle-solving repos. Every phase produces artifacts. Every artifact gets verified before advancing.

### Gate: Multi-Agent Results Persistence

**Rule:** After any multi-agent task, save results to `results/summary.json` before doing anything else.

```bash
# verify_agent_results.sh
#!/bin/bash
PASS=0; FAIL=0

# Results file exists and is valid JSON
if [ -f "results/summary.json" ]; then
  python3 -c "import json; json.load(open('results/summary.json'))" 2>/dev/null
  if [ $? -eq 0 ]; then ((PASS++)); echo "  OK: results/summary.json is valid JSON"
  else ((FAIL++)); echo "  FAIL: results/summary.json is invalid JSON"; fi
else
  ((FAIL++)); echo "  FAIL: results/summary.json missing"
fi

echo "AGENT RESULTS GATE: $PASS passed, $FAIL failed"
[ $FAIL -eq 0 ] && echo "CLEAR" || echo "FIX BEFORE CONTINUING"
```

### Gate: Puzzle Solution Verification

**Rule:** Before moving to the next puzzle or restructuring, verify solutions are on disk.

```bash
# verify_puzzle_solutions.sh
#!/bin/bash
PASS=0; FAIL=0

for dir in puzzles/*/; do
  puzzle=$(basename "$dir")
  # Check if puzzle has any content (not just empty dir)
  file_count=$(find "$dir" -type f | wc -l | tr -d ' ')
  if [ "$file_count" -gt 0 ]; then
    ((PASS++)); echo "  OK: $puzzle has $file_count file(s)"
  else
    echo "  INFO: $puzzle is empty (not started)"
  fi
done

# Check that any solved puzzle has a notes.md with findings
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

### Gate: Session Handoff

**Rule:** At end of each session, `results/summary.json` must be updated. Next session reads it first.

```python
# verify_session_handoff.py
import json, os, sys
from datetime import datetime

SUMMARY = "results/summary.json"

if not os.path.exists(SUMMARY):
    print("FAIL: No session summary found. Run a session first.")
    sys.exit(1)

data = json.load(open(SUMMARY))
required_keys = ["last_updated", "accomplished", "files_modified", "pending"]

for key in required_keys:
    if key not in data:
        print(f"FAIL: Missing required key '{key}' in summary.json")
        sys.exit(1)

print(f"Last session: {data['last_updated']}")
print(f"Accomplished: {len(data['accomplished'])} items")
print(f"Files modified: {len(data['files_modified'])} files")
print(f"Pending: {len(data['pending'])} items")
print("SESSION HANDOFF GATE: CLEAR")
```

---

*Last updated: February 2026*