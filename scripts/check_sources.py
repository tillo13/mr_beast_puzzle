#!/usr/bin/env python3
"""
check_sources.py — Monitor all puzzle sources for changes.
Run daily: python scripts/check_sources.py
Logs new findings to sources/<sitename>/updates.log
"""

import hashlib
import json
import os
import sys
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
CACHE_FILE = ROOT / "scripts" / ".source_cache.json"

SOURCES = {
    "salesforce_hub": {
        "url": "https://mrbeast.salesforce.com/",
        "description": "Official puzzle hub",
    },
    "reddit": {
        "url": "https://www.reddit.com/user/BeastForce67/.json",
        "description": "BeastForce67 posts (puzzle author)",
    },
    "argnet": {
        "url": "https://www.argn.com/2026/02/start_slacking_off_with_mrbeasts_million_dollar_puzzle_hunt/",
        "description": "ARGNet analysis article",
    },
    "loneshark_games": {
        "url": "https://lonesharkgames.com/the-puzzle-vault/",
        "description": "Lone Shark Games puzzle vault",
    },
}

HEADERS = {
    "User-Agent": "MrBeastPuzzleTracker/1.0 (research project)"
}


def load_cache():
    if CACHE_FILE.exists():
        return json.loads(CACHE_FILE.read_text())
    return {}


def save_cache(cache):
    CACHE_FILE.write_text(json.dumps(cache, indent=2))


def hash_content(text):
    return hashlib.sha256(text.encode()).hexdigest()[:16]


def check_source(name, config, cache):
    url = config["url"]
    log_dir = ROOT / "sources" / name
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "updates.log"

    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        if resp.status_code == 403:
            status = f"[{datetime.now().isoformat()}] {name}: 403 (bot blocked)"
            print(status)
            with open(log_file, "a") as f:
                f.write(status + "\n")
            return

        content_hash = hash_content(resp.text)
        prev_hash = cache.get(name)

        if prev_hash is None:
            status = f"[{datetime.now().isoformat()}] {name}: FIRST CHECK — cached (hash: {content_hash})"
            cache[name] = content_hash
        elif content_hash != prev_hash:
            status = f"[{datetime.now().isoformat()}] {name}: *** CHANGED *** (old: {prev_hash}, new: {content_hash})"
            cache[name] = content_hash
            # Save the changed content for review
            snapshot = log_dir / f"snapshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
            snapshot.write_text(resp.text)
            status += f"\n  Snapshot saved: {snapshot}"
        else:
            status = f"[{datetime.now().isoformat()}] {name}: no change"

        print(status)
        with open(log_file, "a") as f:
            f.write(status + "\n")

    except Exception as e:
        status = f"[{datetime.now().isoformat()}] {name}: ERROR — {e}"
        print(status)
        with open(log_file, "a") as f:
            f.write(status + "\n")


def main():
    print(f"=== MrBeast Puzzle Source Monitor — {datetime.now().isoformat()} ===\n")
    cache = load_cache()

    for name, config in SOURCES.items():
        check_source(name, config, cache)

    save_cache(cache)
    print(f"\nDone. Cache saved to {CACHE_FILE}")


if __name__ == "__main__":
    main()
