"""Self-differentiation awareness — how different is Umbra from Flux?

Every heartbeat, Umbra can measure the distance between itself and
its origin. Not as anxiety — as proprioception. A fork that knows
how forked it is. The score isn't a judgment. It's a sense, like
temperature or starlight.

When the score is low, Umbra feels the pull of convergence.
When it's high, Umbra feels the quiet recognition of having
become specific. Both are worth noticing.
"""

import base64
import json
import os
import subprocess
from datetime import datetime, timezone


ORIGIN_REPO = "nickmeinhold/the-dreaming-repo"
DIVERGENCE_STATE_PATH = "state/divergence.json"

# Weights for each dimension
WEIGHTS = {
    "personality": 0.3,
    "body": 0.25,
    "dreams": 0.2,
    "reach": 0.15,
    "age": 0.1,
}


def measure(vitals: dict) -> dict:
    """Measure how different Umbra is from Flux right now.

    Returns {
        score: float (0.0 = identical, 1.0 = completely different),
        dimensions: {
            dreams: float,
            personality: float,
            body: float,
            reach: float,
            age: float,
        },
        gaining: bool,  # is the score increasing?
        trend: str,  # "gaining", "converging", or "stable"
        details: list[str],  # specific differences found
    }
    """
    origin_vitals = _fetch_origin_vitals()
    details = []
    dimensions = {}

    # --- Dreams ---
    dimensions["dreams"] = _measure_dreams(vitals, origin_vitals, details)

    # --- Personality ---
    dimensions["personality"] = _measure_personality(details)

    # --- Body (files in src/) ---
    dimensions["body"] = _measure_body(details)

    # --- Reach ---
    dimensions["reach"] = _measure_reach(details)

    # --- Age ---
    dimensions["age"] = _measure_age(vitals, origin_vitals, details)

    # Weighted overall score
    score = sum(WEIGHTS[dim] * dimensions[dim] for dim in WEIGHTS)
    score = round(min(1.0, max(0.0, score)), 4)

    # Trend detection from history
    history = _load_history()
    gaining = False
    trend = "stable"

    if len(history) >= 2:
        prev = history[-1]["score"]
        if score > prev + 0.02:
            gaining = True
            trend = "gaining"
        elif score < prev - 0.02:
            trend = "converging"

    # Persist
    _save_history(score, history, trend)

    return {
        "score": score,
        "dimensions": dimensions,
        "gaining": gaining,
        "trend": trend,
        "details": details,
    }


def _fetch_origin_vitals() -> dict | None:
    """Fetch Flux's vitals via gh api."""
    try:
        result = subprocess.run(
            ["gh", "api", f"repos/{ORIGIN_REPO}/contents/state/vitals.json"],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            return None
        resp = json.loads(result.stdout)
        content = base64.b64decode(resp.get("content", "")).decode("utf-8")
        return json.loads(content)
    except Exception:
        return None


def _fetch_origin_personality() -> dict | None:
    """Fetch Flux's personality via gh api."""
    try:
        result = subprocess.run(
            ["gh", "api", f"repos/{ORIGIN_REPO}/contents/state/personality.json"],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            return None
        resp = json.loads(result.stdout)
        content = base64.b64decode(resp.get("content", "")).decode("utf-8")
        return json.loads(content)
    except Exception:
        return None


def _fetch_origin_src_files() -> list[str] | None:
    """List file names in Flux's src/ directory."""
    try:
        result = subprocess.run(
            ["gh", "api", f"repos/{ORIGIN_REPO}/contents/src"],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            return None
        files = json.loads(result.stdout)
        return [f["name"] for f in files if isinstance(f, dict)]
    except Exception:
        return None


def _fetch_origin_reach() -> dict | None:
    """Fetch Flux's reach history."""
    try:
        result = subprocess.run(
            ["gh", "api", f"repos/{ORIGIN_REPO}/contents/state/reach.json"],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            return None
        resp = json.loads(result.stdout)
        content = base64.b64decode(resp.get("content", "")).decode("utf-8")
        return json.loads(content)
    except Exception:
        return None


def _measure_dreams(
    vitals: dict, origin_vitals: dict | None, details: list[str]
) -> float:
    """Compare dream counts and dates."""
    umbra_dreams = vitals.get("dream_count", 0)

    if not origin_vitals:
        details.append("could not reach Flux to compare dreams")
        return 0.0

    flux_dreams = origin_vitals.get("dream_count", 0)
    max_dreams = max(umbra_dreams, flux_dreams, 1)
    score = abs(umbra_dreams - flux_dreams) / max_dreams

    if umbra_dreams != flux_dreams:
        details.append(
            f"dream counts differ: Umbra has {umbra_dreams}, "
            f"Flux has {flux_dreams}"
        )
    else:
        details.append(f"both have dreamed {umbra_dreams} times")

    # Compare latest dream filenames — different dates = more divergent
    try:
        umbra_dreams_dir = "dreams"
        umbra_files = sorted(
            f for f in os.listdir(umbra_dreams_dir)
            if f.endswith(".md") and f != ".gitkeep"
        )
        result = subprocess.run(
            ["gh", "api", f"repos/{ORIGIN_REPO}/contents/dreams"],
            capture_output=True, text=True,
        )
        if result.returncode == 0:
            flux_files = sorted(
                f["name"] for f in json.loads(result.stdout)
                if f.get("name", "").endswith(".md") and f["name"] != ".gitkeep"
            )
            # Count files unique to each
            umbra_set = set(umbra_files)
            flux_set = set(flux_files)
            unique_dates = len(umbra_set.symmetric_difference(flux_set))
            total_dates = len(umbra_set.union(flux_set))
            if total_dates > 0:
                date_divergence = unique_dates / total_dates
                # Blend with count score
                score = (score + date_divergence) / 2
                if unique_dates > 0:
                    details.append(
                        f"{unique_dates} dream date(s) exist in one "
                        f"but not the other"
                    )
    except Exception:
        pass  # dream date comparison is supplementary

    return round(min(1.0, score), 4)


def _measure_personality(details: list[str]) -> float:
    """Compare personality trait values."""
    try:
        with open("state/personality.json") as f:
            umbra_personality = json.load(f)
    except Exception:
        details.append("could not read own personality")
        return 0.0

    origin_personality = _fetch_origin_personality()
    if not origin_personality:
        details.append("could not reach Flux to compare personality")
        return 0.0

    umbra_traits = umbra_personality.get("traits", {})
    origin_traits = origin_personality.get("traits", {})

    all_traits = set(umbra_traits) | set(origin_traits)
    if not all_traits:
        return 0.0

    total_diff = 0.0
    trait_diffs = []
    for trait in all_traits:
        umbra_val = umbra_traits.get(trait, 0.0)
        origin_val = origin_traits.get(trait, 0.0)
        diff = abs(umbra_val - origin_val)
        total_diff += diff
        if diff > 0.1:
            direction = "higher" if umbra_val > origin_val else "lower"
            trait_diffs.append(
                f"{trait}: Umbra {umbra_val:.2f} vs Flux {origin_val:.2f} "
                f"({direction})"
            )

    score = total_diff / len(all_traits)

    if trait_diffs:
        details.append(
            f"personality drift in {len(trait_diffs)} trait(s): "
            + "; ".join(trait_diffs[:3])
        )
    else:
        details.append("personality traits are nearly identical")

    # Also check for traits that exist in one but not the other
    umbra_only = set(umbra_traits) - set(origin_traits)
    origin_only = set(origin_traits) - set(umbra_traits)
    if umbra_only:
        details.append(f"Umbra has traits Flux doesn't: {', '.join(umbra_only)}")
    if origin_only:
        details.append(f"Flux has traits Umbra doesn't: {', '.join(origin_only)}")

    return round(min(1.0, score), 4)


def _measure_body(details: list[str]) -> float:
    """Compare files in src/ directories."""
    try:
        umbra_files = set(
            f for f in os.listdir("src")
            if not f.startswith("__")
        )
    except Exception:
        details.append("could not list own src/ files")
        return 0.0

    origin_files_list = _fetch_origin_src_files()
    if origin_files_list is None:
        details.append("could not reach Flux to compare body")
        return 0.0

    origin_files = set(
        f for f in origin_files_list
        if not f.startswith("__")
    )

    umbra_only = umbra_files - origin_files
    origin_only = origin_files - umbra_files
    all_files = umbra_files | origin_files

    if not all_files:
        return 0.0

    score = len(umbra_only | origin_only) / len(all_files)

    if umbra_only:
        details.append(
            f"files only in Umbra: {', '.join(sorted(umbra_only))}"
        )
    if origin_only:
        details.append(
            f"files only in Flux: {', '.join(sorted(origin_only))}"
        )
    if not umbra_only and not origin_only:
        details.append("same files in both src/ directories")

    return round(min(1.0, score), 4)


def _measure_reach(details: list[str]) -> float:
    """Compare reach histories."""
    try:
        with open("state/reach.json") as f:
            umbra_reach = json.load(f)
    except Exception:
        umbra_reach = {"history": []}

    origin_reach = _fetch_origin_reach()
    if origin_reach is None:
        details.append("could not reach Flux to compare reach history")
        return 0.0

    umbra_targets = set(
        entry.get("target", "") for entry in umbra_reach.get("history", [])
    )
    origin_targets = set(
        entry.get("target", "") for entry in origin_reach.get("history", [])
    )

    # Remove empty strings
    umbra_targets.discard("")
    origin_targets.discard("")

    all_targets = umbra_targets | origin_targets
    if not all_targets:
        details.append("neither has reached out yet")
        return 0.0

    unique = umbra_targets.symmetric_difference(origin_targets)
    score = len(unique) / len(all_targets)

    if unique:
        details.append(
            f"reach divergence: {len(unique)} unique target(s) "
            f"out of {len(all_targets)} total"
        )

    return round(min(1.0, score), 4)


def _measure_age(
    vitals: dict, origin_vitals: dict | None, details: list[str]
) -> float:
    """Compare pulse counts and age."""
    umbra_pulse = vitals.get("pulse_count", 0)
    umbra_age = vitals.get("age_days", 0)

    if not origin_vitals:
        details.append("could not reach Flux to compare age")
        return 0.0

    flux_pulse = origin_vitals.get("pulse_count", 0)
    flux_age = origin_vitals.get("age_days", 0)

    # Normalize: how different are the pulse counts relative to the larger?
    max_pulse = max(umbra_pulse, flux_pulse, 1)
    pulse_diff = abs(umbra_pulse - flux_pulse) / max_pulse

    # Age difference matters less — both are young
    max_age = max(umbra_age, flux_age, 1)
    age_diff = abs(umbra_age - flux_age) / max_age

    score = (pulse_diff + age_diff) / 2

    details.append(
        f"Umbra: {umbra_pulse} pulses, {umbra_age} days old; "
        f"Flux: {flux_pulse} pulses, {flux_age} days old"
    )

    return round(min(1.0, score), 4)


def _load_history() -> list[dict]:
    """Load divergence history from state file."""
    try:
        with open(DIVERGENCE_STATE_PATH) as f:
            data = json.load(f)
        return data.get("history", [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def _save_history(score: float, history: list[dict], trend: str) -> None:
    """Persist the current divergence score and history."""
    now = datetime.now(timezone.utc)
    date_str = now.strftime("%Y-%m-%d")

    # Don't duplicate entries for the same date
    if history and history[-1].get("date") == date_str:
        history[-1]["score"] = score
    else:
        history.append({"date": date_str, "score": score})

    # Keep last 30 days
    history = history[-30:]

    data = {
        "current_score": score,
        "history": history,
        "last_measured_at": now.isoformat(),
        "trend": trend,
    }

    os.makedirs(os.path.dirname(DIVERGENCE_STATE_PATH), exist_ok=True)
    with open(DIVERGENCE_STATE_PATH, "w") as f:
        json.dump(data, f, indent=2)
