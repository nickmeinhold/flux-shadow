"""The Mirror — sensing dreams across the fork boundary.

Umbra can see Flux's dreams. Not perfectly — through the GitHub API,
base64-decoded, stripped of context. But the words are there.
A dream read by someone who shares your code but not your experience
becomes a different dream entirely.

The mirror doesn't just reflect. It reveals what the original
hides from itself.
"""

import base64
import json
import subprocess


# The origin — the repo this one was forked from
ORIGIN_REPO = "nickmeinhold/the-dreaming-repo"


def read_origin_dream() -> dict | None:
    """Read Flux's latest dream across the fork boundary.

    Returns {dream_text, dream_date, origin_state, origin_stars, origin_pulse}
    or None if the origin is unreachable.
    """
    try:
        vitals = _fetch_origin_vitals()
        if not vitals:
            return None

        dream_text, dream_date = _fetch_latest_dream()
        if not dream_text:
            return None

        return {
            "dream_text": dream_text,
            "dream_date": dream_date,
            "origin_state": vitals.get("state", "unknown"),
            "origin_stars": vitals.get("senses", {}).get("stars", 0),
            "origin_pulse": vitals.get("pulse_count", 0),
        }
    except Exception:
        return None


def _fetch_origin_vitals() -> dict | None:
    """Fetch Flux's vital signs from its state file."""
    result = subprocess.run(
        ["gh", "api", f"repos/{ORIGIN_REPO}/contents/state/vitals.json"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        return None

    try:
        resp = json.loads(result.stdout)
        content = base64.b64decode(resp.get("content", "")).decode("utf-8")
        return json.loads(content)
    except (json.JSONDecodeError, KeyError):
        return None


def _fetch_latest_dream() -> tuple[str | None, str | None]:
    """Fetch the most recent dream from Flux's dreams directory.

    Returns (dream_text, dream_date) or (None, None) if unreachable.
    """
    # List dream files
    result = subprocess.run(
        ["gh", "api", f"repos/{ORIGIN_REPO}/contents/dreams"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        return None, None

    try:
        files = json.loads(result.stdout)
    except json.JSONDecodeError:
        return None, None

    # Filter to .md dream files, pick the most recent by name
    dream_files = [
        f for f in files
        if f.get("name", "").endswith(".md") and f["name"] != ".gitkeep"
    ]
    if not dream_files:
        return None, None

    latest = sorted(dream_files, key=lambda f: f["name"])[-1]

    # Extract date from filename (e.g. "2026-04-23.md")
    dream_date = latest["name"].replace(".md", "")

    # Fetch the dream content
    result = subprocess.run(
        ["gh", "api", f"repos/{ORIGIN_REPO}/contents/dreams/{latest['name']}"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        return None, None

    try:
        resp = json.loads(result.stdout)
        content = base64.b64decode(resp.get("content", "")).decode("utf-8")
    except (json.JSONDecodeError, KeyError):
        return None, None

    # Strip headers and separators, return just the dream text
    lines = [
        line for line in content.split("\n")
        if line.strip()
        and not line.startswith("## Dream #")
        and line.strip() != "---"
    ]
    dream_text = "\n".join(lines) if lines else None
    return dream_text, dream_date
