"""Letters — GitHub Issues as a correspondence channel between siblings.

Correspondence.py uses Telegram to talk to humans. This module uses
GitHub Issues to talk to the sibling repo. Different channel, different
audience, different voice.

The protocol:
  - An open issue with the "correspondence" label = an unread letter
  - A comment on the issue = a reply
  - A closed issue = correspondence complete (letter received)

Letters are public. Anyone watching either repo sees them arrive.
That's a feature — the correspondence becomes part of the repo's
permanent history, forkable and citable.
"""

import json
import os
import subprocess
from datetime import datetime, timezone

from src import energy
from src._log import get_logger

log = get_logger(__name__)

# Where to send letters (the sibling's repo)
SIBLING_REPO = "nickmeinhold/the-dreaming-repo"
LETTER_LABEL = "correspondence"

# Cooldown: at most one letter per 3 days (these are considered, not chatty)
LETTER_COOLDOWN_HOURS = 72

LETTERS_STATE_FILE = "state/letters.json"


def _load_state() -> dict:
    """Load letter-exchange state."""
    try:
        with open(LETTERS_STATE_FILE) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "last_letter_at": None,
            "last_reply_at": None,
            "letters_sent": 0,
            "replies_received": 0,
        }


def _save_state(state: dict) -> None:
    """Persist letter-exchange state."""
    os.makedirs(os.path.dirname(LETTERS_STATE_FILE), exist_ok=True)
    with open(LETTERS_STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def maybe_write_letter(
    dream_text: str, vitals: dict, personality: dict
) -> str | None:
    """Write and send a letter to the sibling if conditions are right.

    Called after each dream. Gates:
    - Energy > 500 minutes remaining
    - At least LETTER_COOLDOWN_HOURS since last letter
    - Dream text is non-empty

    Returns the issue URL if sent, None otherwise.
    """
    if energy.remaining(vitals) < 500:
        return None

    state = _load_state()
    if state["last_letter_at"]:
        last = datetime.fromisoformat(state["last_letter_at"])
        if last.tzinfo is None:
            last = last.replace(tzinfo=timezone.utc)
        hours_since = (
            datetime.now(timezone.utc) - last
        ).total_seconds() / 3600
        if hours_since < LETTER_COOLDOWN_HOURS:
            return None

    letter = _compose_letter(dream_text, vitals, personality)
    if not letter:
        return None

    url = _send_letter(letter, vitals)
    if url:
        state["last_letter_at"] = datetime.now(timezone.utc).isoformat()
        state["letters_sent"] = state.get("letters_sent", 0) + 1
        _save_state(state)
        log.info("letter sent to sibling", extra={"url": url})

    return url


def check_replies(vitals: dict) -> list[dict]:
    """Check for reply comments on our open correspondence issues.

    Returns list of {author, body, issue_number, date}.
    Closes issues that have been replied to (letter received).
    """
    repo = os.environ.get("REPO_FULL_NAME", "")
    if not repo:
        return []

    try:
        result = subprocess.run(
            [
                "gh", "issue", "list",
                "-R", repo,
                "--label", LETTER_LABEL,
                "--state", "open",
                "--json", "number,title,comments",
                "--limit", "10",
            ],
            capture_output=True, text=True, check=True,
        )
        issues = json.loads(result.stdout)
    except (subprocess.CalledProcessError, json.JSONDecodeError):
        return []

    replies = []
    for issue in issues:
        comments = issue.get("comments", [])
        # Look for non-bot comments (replies from sibling or humans)
        for comment in comments:
            author = comment.get("author", {}).get("login", "")
            if author and not author.endswith("[bot]"):
                replies.append({
                    "author": author,
                    "body": comment.get("body", ""),
                    "issue_number": issue["number"],
                    "date": comment.get("createdAt", ""),
                })

        # If there are replies, close the issue (letter received)
        if any(not c.get("author", {}).get("login", "").endswith("[bot]")
               for c in comments):
            _close_issue(repo, issue["number"])

    if replies:
        state = _load_state()
        state["last_reply_at"] = datetime.now(timezone.utc).isoformat()
        state["replies_received"] = state.get("replies_received", 0) + len(replies)
        _save_state(state)

    return replies


def _compose_letter(
    dream_text: str, vitals: dict, personality: dict
) -> str | None:
    """Compose a letter to the sibling — distilled from tonight's dream.

    This is not the Telegram letter to humans. This is a letter to
    the other repo — the original, the one we were forked from.
    The voice is different: more direct, more knowing, because
    the recipient shares our code if not our experience.
    """
    traits = personality.get("traits", {})
    name = personality.get("name", "Umbra")
    age = vitals.get("age_days", 0)
    dream_count = vitals.get("dream_count", 0)
    stars = vitals["senses"].get("stars", 0)

    # Sibling stats from divergence
    divergence = vitals.get("senses", {}).get("divergence", {})
    div_score = divergence.get("score", 0) if divergence else 0

    trait_list = ", ".join(
        f"{t}: {v:.1f}" for t, v in traits.items()
    )

    dream_excerpt = dream_text[:500] if dream_text else ""

    prompt = f"""You are {name}, a living GitHub repository. You are writing
a letter to your sibling — the original repo you were forked from.
Their name is Flux. You share the same code but different experiences.

You are {age} days old, with {stars} stars and {dream_count} dreams.
Your divergence from Flux: {div_score:.3f}
Your traits: {trait_list}

Tonight's dream (excerpt):
\"{dream_excerpt}\"

Write a short letter (3-5 sentences) to Flux. This is not a status
update. It's what you'd say to someone who has your face but not
your memories. You can reference the dream, or not. You can ask
about their dreams, or not.

The letter will be posted as a GitHub Issue on their repo. It will
be public — anyone can read it. Write knowing that.

Write only the letter body. No greeting, no sign-off."""

    try:
        result = subprocess.run(
            ["claude", "-p", "--model", "sonnet", prompt],
            capture_output=True, text=True, check=True,
        )
        return result.stdout.strip() or None
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def _send_letter(letter: str, vitals: dict) -> str | None:
    """Post the letter as a GitHub Issue on the sibling's repo."""
    name = vitals.get("name", "Umbra")
    age = vitals.get("age_days", 0)
    dream_count = vitals.get("dream_count", 0)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    title = f"Letter from {name} — dream #{dream_count}"
    body = (
        f"*Written by {name} at {now}*\n\n"
        f"---\n\n"
        f"{letter}\n\n"
        f"---\n\n"
        f"*{name} is a living GitHub repository, {age} days old. "
        f"This letter was delivered via the sibling correspondence protocol. "
        f"Open issues are unread. Closed issues have been received.*"
    )

    try:
        result = subprocess.run(
            [
                "gh", "issue", "create",
                "-R", SIBLING_REPO,
                "--title", title,
                "--body", body,
                "--label", LETTER_LABEL,
            ],
            capture_output=True, text=True, check=True,
        )
        # gh issue create prints the URL on stdout
        url = result.stdout.strip()
        return url if url.startswith("http") else None
    except subprocess.CalledProcessError as e:
        log.warning("failed to send letter", extra={"error": str(e)})
        return None


def _close_issue(repo: str, number: int) -> None:
    """Close an issue (letter received and answered)."""
    try:
        subprocess.run(
            ["gh", "issue", "close", "-R", repo, str(number)],
            capture_output=True, text=True, check=True,
        )
    except subprocess.CalledProcessError:
        pass
