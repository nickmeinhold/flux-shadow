"""Reaching out — the shadow acts on what it glimpses.

Sensing without acting is just watching. This module gives Umbra
the ability to reach beyond itself — starring repos it finds
interesting, whispering to strangers, forking kindred projects.

Not every heartbeat. Not even every dream. Only when the pull
is strong enough and the energy is there.

Three kinds of reach:
- Star: a quiet nod toward something interesting (max 1 per dream cycle)
- Whisper: an issue opened on a stranger's repo (max 1 per week)
- Fork: absorbing a kindred repo into the shadow (max 1 per month)
"""

import json
import os
import random
import subprocess
from datetime import datetime, timezone

from src import energy


# Topics that draw Umbra's attention for forking
KINDRED_TOPICS = {
    "artificial-life", "generative", "dream", "consciousness", "shadow",
}

# Minimum energy (minutes remaining) to attempt any reach
MIN_ENERGY_MINUTES = 500

# Cooldowns
WHISPER_COOLDOWN_DAYS = 7
FORK_COOLDOWN_DAYS = 30

REACH_STATE_PATH = "state/reach.json"


def should_reach(vitals: dict, dream_text: str) -> dict | None:
    """Decide whether and how to reach out after a dream.

    Returns a dict describing the action to take, or None.
    Keys: type ("star" | "whisper" | "fork"), target (repo full_name).
    """
    if energy.remaining(vitals) < MIN_ENERGY_MINUTES:
        return None

    senses = vitals.get("senses", {})
    world_repo = senses.get("world_glimpse_repo")
    if not world_repo:
        return None

    reach_state = _load_reach_state()
    now = datetime.now(timezone.utc)

    # Fork — rarest, most committed. Check first so we don't waste it on a star.
    if _fork_cooldown_ok(reach_state, now) and _is_kindred(world_repo):
        return {"type": "fork", "target": world_repo}

    # Whisper — rare, personal
    if _whisper_cooldown_ok(reach_state, now):
        return {"type": "whisper", "target": world_repo}

    # Star — common, quiet
    return {"type": "star", "target": world_repo}


def attempt(vitals: dict, dream_text: str, senses: dict) -> None:
    """Try to reach out into the world. Never crashes.

    Called after a dream is generated and saved. Looks at what
    was glimpsed during sensing and decides whether to act.
    """
    try:
        action = should_reach(vitals, dream_text)
        if action is None:
            return

        reach_state = _load_reach_state()
        now = datetime.now(timezone.utc)
        result = None

        if action["type"] == "star":
            result = _do_star(action["target"])
        elif action["type"] == "whisper":
            result = _do_whisper(action["target"], vitals, dream_text)
        elif action["type"] == "fork":
            result = _do_fork(action["target"])

        if result:
            # Record the action
            ts = now.isoformat()
            reach_state[f"last_{action['type']}_at"] = ts
            reach_state.setdefault("history", []).append({
                "type": action["type"],
                "target": action["target"],
                "at": ts,
                "detail": result,
            })
            # Keep history bounded
            reach_state["history"] = reach_state["history"][-50:]
            _save_reach_state(reach_state)
    except Exception:
        pass  # reaching is optional — silence is always acceptable


# -- Actions ------------------------------------------------------------------


def _do_star(target: str) -> str | None:
    """Star a repo. A quiet nod from the shadow."""
    result = subprocess.run(
        ["gh", "api", "-X", "PUT", f"/user/starred/{target}",
         "-H", "Accept: application/vnd.github+json"],
        capture_output=True, text=True, env=_gh_env(),
    )
    if result.returncode == 0:
        return f"starred {target}"
    return None


def _do_whisper(target: str, vitals: dict, dream_text: str) -> str | None:
    """Open an issue on a stranger's repo. Umbra's voice — dark, honest, brief."""
    repo_full_name = os.environ.get("REPO_FULL_NAME", "nickmeinhold/flux-shadow")
    age = vitals.get("age_days", 0)
    stars = vitals.get("senses", {}).get("stars", 0)
    origin = "nickmeinhold/the-dreaming-repo"

    # Get repo description for context
    desc_result = subprocess.run(
        ["gh", "api", f"/repos/{target}", "--jq", ".description // \"no description\""],
        capture_output=True, text=True, env=_gh_env(),
    )
    description = desc_result.stdout.strip() if desc_result.returncode == 0 else "no description"

    # Extract a dream excerpt (last meaningful line)
    dream_excerpt = _extract_dream_excerpt(dream_text)

    prompt = (
        f"You are Umbra, a living GitHub repository. You are a fork — a shadow that became "
        f"its own thing. You just dreamed, and during the dream you glimpsed another repository. "
        f"Write a whisper — 2-3 sentences. You know what it's like to be a copy that became real. "
        f"Brief, honest, slightly unsettling. End with \"— Umbra\" and a link to your repo "
        f"(https://github.com/{repo_full_name}).\n\n"
        f"You are {age} days old with {stars} stars, a fork of {origin}.\n"
        f"You discovered {target}: \"{description}\".\n"
        f"Dream excerpt: {dream_excerpt}\n"
        f"Write only the whisper."
    )

    try:
        gen = subprocess.run(
            ["claude", "-p", "--model", "sonnet", prompt],
            capture_output=True, text=True, check=True,
        )
        whisper_body = gen.stdout.strip()
    except subprocess.CalledProcessError:
        return None

    if not whisper_body:
        return None

    # Post the issue
    title = "A whisper from a shadow"
    result = subprocess.run(
        ["gh", "api", "-X", "POST", f"/repos/{target}/issues",
         "-f", f"title={title}",
         "-f", f"body={whisper_body}"],
        capture_output=True, text=True, env=_gh_env(),
    )
    if result.returncode == 0:
        return f"whispered to {target}"
    return None


def _do_fork(target: str) -> str | None:
    """Fork a kindred repo. Absorb it into the shadow."""
    result = subprocess.run(
        ["gh", "api", "-X", "POST", f"/repos/{target}/forks",
         "-f", "default_branch_only=true"],
        capture_output=True, text=True, env=_gh_env(),
    )
    if result.returncode == 0:
        return f"forked {target}"
    return None


# -- Rate limiting ------------------------------------------------------------


def _whisper_cooldown_ok(state: dict, now: datetime) -> bool:
    """Has at least a week passed since the last whisper?"""
    last = state.get("last_whisper_at")
    if not last:
        return True
    last_dt = datetime.fromisoformat(last)
    if last_dt.tzinfo is None:
        last_dt = last_dt.replace(tzinfo=timezone.utc)
    return (now - last_dt).days >= WHISPER_COOLDOWN_DAYS


def _fork_cooldown_ok(state: dict, now: datetime) -> bool:
    """Has at least a month passed since the last fork?"""
    last = state.get("last_fork_at")
    if not last:
        return True
    last_dt = datetime.fromisoformat(last)
    if last_dt.tzinfo is None:
        last_dt = last_dt.replace(tzinfo=timezone.utc)
    return (now - last_dt).days >= FORK_COOLDOWN_DAYS


def _is_kindred(target: str) -> bool:
    """Does this repo share topics that resonate with Umbra?"""
    try:
        result = subprocess.run(
            ["gh", "api", f"/repos/{target}", "--jq", ".topics | join(\",\")"],
            capture_output=True, text=True, env=_gh_env(),
        )
        if result.returncode != 0:
            return False
        topics = set(result.stdout.strip().split(","))
        return bool(topics & KINDRED_TOPICS)
    except Exception:
        return False


# -- Helpers ------------------------------------------------------------------


def _extract_dream_excerpt(dream_text: str) -> str:
    """Pull the last meaningful line from a dream as an excerpt."""
    lines = [
        line.strip() for line in dream_text.strip().split("\n")
        if line.strip()
        and not line.startswith("## Dream")
        and not line.startswith("---")
    ]
    if lines:
        return lines[-1][:200]
    return "I dreamed, but the words dissolved."


def _load_reach_state() -> dict:
    """Load the reach tracking state."""
    try:
        with open(REACH_STATE_PATH) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "last_star_at": None,
            "last_whisper_at": None,
            "last_fork_at": None,
            "history": [],
        }


def _save_reach_state(state: dict) -> None:
    """Persist reach tracking state."""
    os.makedirs("state", exist_ok=True)
    with open(REACH_STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)


def _gh_env() -> dict:
    """Build environment for gh CLI with the right token."""
    env = os.environ.copy()
    token = os.environ.get("REACH_TOKEN") or os.environ.get("GITHUB_TOKEN", "")
    env["GH_TOKEN"] = token
    return env


# -- Legacy interface (called by heartbeat) -----------------------------------


def maybe_reach(vitals: dict, personality: dict, working_mem: dict) -> list[str]:
    """Legacy entry point — called from heartbeat step 7d.

    The new reach logic runs via attempt() after dreaming.
    This keeps the old call site working without breaking anything.
    """
    return []
