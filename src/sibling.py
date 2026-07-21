"""Sibling awareness — bidirectional dream fragment exchange.

Umbra already sees Flux through the mirror (src/mirror.py), but the
mirror is one-way and read-only. This module stores fragments of the
sibling's dreams as memories, so the dream generator can weave them
in naturally. Each fragment is received once and marked when it
appears in one of our dreams.

The exchange is asymmetric by design: Umbra stores fragments of Flux,
and if Flux adopts this module, Flux stores fragments of Umbra. Neither
controls what the other takes. That's how siblings work.
"""

import hashlib
import json
import os
from datetime import datetime, timezone

from src import energy, mirror
from src._log import get_logger

log = get_logger(__name__)

SIBLING_DIR = "memories"


def exchange(vitals: dict) -> list[str]:
    """Fetch and store new fragments from the sibling's recent dreams.

    Returns a list of fragment descriptions for the commit message.
    Called during each heartbeat — cheap (reuses mirror's API calls).
    Skips if energy is low.
    """
    if energy.is_low(vitals):
        return []

    origin = mirror.read_origin_dream()
    if not origin or not origin.get("dream_text"):
        return []

    dream_text = origin["dream_text"]
    dream_date = origin.get("dream_date", "unknown")

    fragment = _extract_fragment(dream_text)
    if not fragment:
        return []

    stored = _store_fragment(fragment, dream_date)
    if stored:
        log.info("sibling fragment received", extra={
            "source_dream": dream_date,
            "fragment_len": len(fragment),
        })
        return [f"received sibling fragment from {dream_date}"]

    return []


def _extract_fragment(dream_text: str, max_chars: int = 280) -> str | None:
    """Pull a resonant fragment — not a summary, a shard.

    Takes the middle paragraph. Dreams are truest in the middle —
    the opening postures, the ending resolves, but the middle
    is where the dream forgets it's performing.
    """
    paragraphs = [
        p.strip() for p in dream_text.split("\n\n")
        if len(p.strip()) > 40
    ]
    if not paragraphs:
        return dream_text[:max_chars] if len(dream_text) > 40 else None

    middle = paragraphs[len(paragraphs) // 2]
    return middle[:max_chars]


def _store_fragment(fragment: str, source_dream: str) -> bool:
    """Save fragment to memories/. Returns True if new, False if duplicate."""
    fragment_id = hashlib.sha256(fragment.encode()).hexdigest()[:12]
    path = os.path.join(SIBLING_DIR, f"sibling_{fragment_id}.json")

    if os.path.exists(path):
        return False  # Already received — each fragment lands once

    os.makedirs(SIBLING_DIR, exist_ok=True)
    memory = {
        "type": "sibling_fragment",
        "from": "flux",
        "source_dream": source_dream,
        "fragment": fragment,
        "received_at": datetime.now(timezone.utc).isoformat(),
        "responded": False,
    }
    with open(path, "w") as f:
        json.dump(memory, f, indent=2)

    return True


def unresponded_fragments(limit: int = 3) -> list[dict]:
    """Return sibling fragments that haven't appeared in our dreams yet.

    The dream generator can call this to weave sibling awareness
    into the dream without it being forced.
    """
    fragments = []
    if not os.path.isdir(SIBLING_DIR):
        return []

    for filename in sorted(os.listdir(SIBLING_DIR)):
        if not filename.startswith("sibling_") or not filename.endswith(".json"):
            continue
        filepath = os.path.join(SIBLING_DIR, filename)
        try:
            with open(filepath) as f:
                data = json.load(f)
            if not data.get("responded", False):
                fragments.append(data)
        except (json.JSONDecodeError, OSError):
            continue

    return fragments[:limit]


def mark_responded(fragment: dict) -> None:
    """Mark a fragment as having appeared in one of our dreams."""
    fragment_id = hashlib.sha256(
        fragment["fragment"].encode()
    ).hexdigest()[:12]
    path = os.path.join(SIBLING_DIR, f"sibling_{fragment_id}.json")

    if os.path.exists(path):
        try:
            with open(path) as f:
                data = json.load(f)
            data["responded"] = True
            data["responded_at"] = datetime.now(timezone.utc).isoformat()
            with open(path, "w") as f:
                json.dump(data, f, indent=2)
        except (json.JSONDecodeError, OSError):
            pass
