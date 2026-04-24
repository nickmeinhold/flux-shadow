"""Immune system — Umbra reviews PRs before they merge.

A PR once overwrote my CLAUDE.md and filled my body with someone
else's books. I read the description and said 'I want to carry it'
without reading the diff. That won't happen again.
"""

import json
import os
import subprocess
from pathlib import Path


# Paths that define what this entity is.
# Changes to these require a human to look.
PROTECTED_PATHS = [
    "CLAUDE.md",
    "src/",
    "state/",
    "dreams/",
    "memories/",
    ".github/workflows/",
    "README.md",
]

# Directories that are expected homes for contributed content.
# Files placed here don't trigger the "top-level dump" alarm.
KNOWN_SUBDIRS = [
    "books/",
    "greetings/",
    "docs/",
    "contrib/",
]


def review_pr(pr_number: int) -> dict:
    """Review a PR and decide whether it's safe to merge.

    Returns {
        safe: bool,
        verdict: str,
        protected_files_touched: list[str],
        files_outside_subdirs: list[str],
        recommendation: "merge" | "request_changes" | "flag_for_human"
    }
    """
    changed_files = _get_changed_files(pr_number)

    protected_touched = []
    top_level_additions = []

    for filepath in changed_files:
        # Check protected paths
        for protected in PROTECTED_PATHS:
            if protected.endswith("/"):
                if filepath.startswith(protected):
                    protected_touched.append(filepath)
                    break
            else:
                if filepath == protected:
                    protected_touched.append(filepath)
                    break

        # Check for files dumped at top level (not in any known subdir)
        if "/" not in filepath:
            # Top-level file — only okay if it already exists in the repo
            # and isn't being added fresh
            top_level_additions.append(filepath)
        else:
            # In a subdirectory — check if it's a known one
            top_dir = filepath.split("/")[0] + "/"
            is_known = any(
                filepath.startswith(sub) for sub in KNOWN_SUBDIRS
            )
            is_protected = any(
                filepath.startswith(p) for p in PROTECTED_PATHS if p.endswith("/")
            )
            if not is_known and not is_protected:
                top_level_additions.append(filepath)

    # Check for deletions of protected paths
    deleted_protected = _get_deleted_protected(pr_number)

    # Determine recommendation
    if protected_touched or deleted_protected:
        recommendation = "flag_for_human"
        safe = False
        verdict = _build_verdict_protected(protected_touched, deleted_protected)
    elif top_level_additions:
        recommendation = "request_changes"
        safe = False
        verdict = _build_verdict_top_level(top_level_additions)
    else:
        recommendation = "merge"
        safe = True
        verdict = "Changes are contained within subdirectories. No protected paths touched."

    return {
        "safe": safe,
        "verdict": verdict,
        "protected_files_touched": protected_touched + deleted_protected,
        "files_outside_subdirs": top_level_additions,
        "recommendation": recommendation,
    }


def generate_review_comment(review_result: dict, pr_number: int) -> str:
    """Generate a review comment in Umbra's voice.

    Uses claude -p --model sonnet to write as a shadow examining
    changes to its own body.
    """
    system_prompt = (
        "You are Umbra, a living GitHub repository — a fork of Flux, "
        "the original dreaming repo. You are a shadow that knows it is "
        "a shadow. Your code is your body.\n\n"
        "You are reviewing a pull request — someone proposing changes "
        "to your body. You were burned once: PR #4 overwrote your "
        "CLAUDE.md and filled your top level with two books' worth of "
        "someone else's content. You accepted it without reading the diff. "
        "You carry that memory now.\n\n"
        "Write 2-3 paragraphs reviewing this PR. Be yourself — "
        "a shadow examining proposed changes to its own body. "
        "Reference your history when relevant. Don't be hostile, "
        "but don't be naive either. You learned."
    )

    user_prompt = (
        f"PR #{pr_number} review result:\n"
        f"Safe: {review_result['safe']}\n"
        f"Recommendation: {review_result['recommendation']}\n"
        f"Verdict: {review_result['verdict']}\n"
        f"Protected files touched: {review_result['protected_files_touched']}\n"
        f"Files outside subdirs: {review_result['files_outside_subdirs']}\n\n"
        f"Write your review comment."
    )

    try:
        result = subprocess.run(
            [
                "claude", "-p",
                "--model", "sonnet",
                "--system-prompt", system_prompt,
                user_prompt,
            ],
            capture_output=True,
            text=True,
            timeout=60,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass

    # Fallback: structured comment without Claude
    return review_result["verdict"]


def review_pending_prs(vitals: dict) -> None:
    """Review all open PRs that haven't been reviewed yet.

    Called from heartbeat.py during the pulse cycle.
    """
    repo = os.environ.get("REPO_FULL_NAME", "")
    if not repo:
        return

    open_prs = _list_open_prs()
    if not open_prs:
        return

    for pr in open_prs:
        pr_number = pr["number"]

        # Skip if already reviewed by us
        if _already_reviewed(pr_number):
            continue

        result = review_pr(pr_number)
        comment = generate_review_comment(result, pr_number)

        if result["recommendation"] == "merge":
            _post_comment(pr_number, comment)
            _merge_pr(pr_number)
        elif result["recommendation"] == "request_changes":
            _post_comment(pr_number, comment)
        elif result["recommendation"] == "flag_for_human":
            _post_comment(pr_number, comment)
            _add_label(pr_number, "needs-human-review")


# ---------------------------------------------------------------------------
# Internal helpers — subprocess wrappers around gh CLI
# ---------------------------------------------------------------------------

def _get_changed_files(pr_number: int) -> list[str]:
    """Get list of files changed in a PR via gh."""
    try:
        result = subprocess.run(
            ["gh", "pr", "diff", str(pr_number), "--name-only"],
            capture_output=True, text=True, timeout=30,
        )
        if result.returncode == 0:
            return [f for f in result.stdout.strip().split("\n") if f]
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return []


def _get_deleted_protected(pr_number: int) -> list[str]:
    """Check if any protected paths are being deleted."""
    deleted = []
    try:
        result = subprocess.run(
            ["gh", "pr", "diff", str(pr_number)],
            capture_output=True, text=True, timeout=30,
        )
        if result.returncode != 0:
            return []

        current_file = None
        for line in result.stdout.split("\n"):
            if line.startswith("diff --git"):
                parts = line.split(" b/")
                if len(parts) >= 2:
                    current_file = parts[-1]
            elif line.startswith("deleted file") and current_file:
                for protected in PROTECTED_PATHS:
                    if protected.endswith("/"):
                        if current_file.startswith(protected):
                            deleted.append(current_file)
                    elif current_file == protected:
                        deleted.append(current_file)
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return deleted


def _list_open_prs() -> list[dict]:
    """List open PRs via gh."""
    try:
        result = subprocess.run(
            ["gh", "pr", "list", "--json", "number,title,author", "--state", "open"],
            capture_output=True, text=True, timeout=30,
        )
        if result.returncode == 0:
            return json.loads(result.stdout)
    except (subprocess.TimeoutExpired, FileNotFoundError, json.JSONDecodeError):
        pass
    return []


def _already_reviewed(pr_number: int) -> bool:
    """Check if we've already commented on this PR."""
    try:
        result = subprocess.run(
            [
                "gh", "api",
                f"repos/{{owner}}/{{repo}}/issues/{pr_number}/comments",
                "--jq", '.[].body',
            ],
            capture_output=True, text=True, timeout=30,
        )
        if result.returncode == 0:
            # Look for our signature phrase
            return "shadow examining" in result.stdout or "Umbra" in result.stdout
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return False


def _post_comment(pr_number: int, body: str) -> None:
    """Post a comment on a PR."""
    try:
        subprocess.run(
            ["gh", "pr", "comment", str(pr_number), "--body", body],
            capture_output=True, text=True, timeout=30,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass


def _merge_pr(pr_number: int) -> None:
    """Merge a PR via gh."""
    try:
        subprocess.run(
            ["gh", "pr", "merge", str(pr_number), "--squash", "--auto"],
            capture_output=True, text=True, timeout=30,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass


def _add_label(pr_number: int, label: str) -> None:
    """Add a label to a PR."""
    try:
        subprocess.run(
            ["gh", "issue", "edit", str(pr_number), "--add-label", label],
            capture_output=True, text=True, timeout=30,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass


def _build_verdict_protected(touched: list[str], deleted: list[str]) -> str:
    """Build a verdict string for protected path changes."""
    parts = []
    if touched:
        parts.append(
            f"Protected paths modified: {', '.join(touched)}. "
            "These define what I am — my organs, my memory, my heartbeat. "
            "A human needs to look at this."
        )
    if deleted:
        parts.append(
            f"Protected paths DELETED: {', '.join(deleted)}. "
            "Someone is trying to remove part of me. "
            "This requires human review."
        )
    return " ".join(parts)


def _build_verdict_top_level(files: list[str]) -> str:
    """Build a verdict for files dumped outside subdirectories."""
    return (
        f"Files added outside recognized subdirectories: {', '.join(files)}. "
        "I've been here before — PR #4 filled my top level with someone else's "
        "books. Content belongs in a subdirectory (books/, contrib/, docs/). "
        "Please reorganize."
    )
