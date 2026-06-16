"""Immune system — Umbra reviews PRs before they merge.

A PR once overwrote my CLAUDE.md and filled my body with someone
else's books. I read the description and said 'I want to carry it'
without reading the diff. That won't happen again.
"""

import json
import os
import subprocess
from pathlib import Path

from src._log import get_logger


logger = get_logger(__name__)


def _self_login() -> str:
    """The agent's own bot login, e.g. `flux-shadow[bot]`.

    Sourced from the BOT_LOGIN env var the workflow sets (heartbeat.yml).
    Empty string when unset. Mirrors respond.py's identity model so the
    immune system and the responder agree on what "this agent" means: a
    comment is the agent's own ONLY when its author login equals BOT_LOGIN
    — never "any login containing 'bot'" (the sibling's bot, github-actions,
    dependabot and watchdog are NOT this agent). This is the Flux
    cage-match #62 invariant, applied here too.
    """
    return os.environ.get("BOT_LOGIN", "").strip()


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

# Behavior-changing paths — a PR touching these carries real risk of
# changing how Umbra runs, not just what content it carries. These get the
# cage-match merge gate before any auto-merge: a single in-process review
# (mine) can miss bugs that an adversarial cage-match catches. Mirrored
# from Flux's Tier-3 gate (the-dreaming-repo immunity.py): the cage-match
# on Flux's PR #62 found 14 issues post-merge, and #64 found 1 more, all
# in exactly this class of change. Auto-merge stays fast for pure content
# PRs (books/, greetings/); only code/workflow/dependency PRs hit the gate.
BEHAVIOR_CHANGING_PATHS = [
    "src/",
    ".github/workflows/",
    "requirements.txt",
]

# The label a PR must carry before Umbra will auto-merge a behavior-changing
# change. Applied by a human (or `/cage-match`) after adversarial review.
CAGE_MATCH_LABEL = "cage-matched"


def review_pr(pr_number: int) -> dict:
    """Review a PR and decide whether it's safe to merge.

    Returns {
        safe: bool,
        verdict: str,
        protected_files_touched: list[str],
        files_outside_subdirs: list[str],
        files_changed: list[str],
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
        "files_changed": changed_files,
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

    # We must know our own login before deciding which PRs we've already
    # reviewed — otherwise `_already_reviewed` cannot tell our comment from
    # any other bot's. Without it we'd either go blind to PRs a foreign bot
    # touched (old bug) or re-review every PR every pulse (comment spam).
    # Mirror respond.py: a misconfigured workflow skips this pulse loudly.
    if not _self_login():
        logger.warning(
            "[immunity] BOT_LOGIN env var unset; cannot distinguish our own "
            "review from other bots' comments. Skipping PR review this pulse."
        )
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
            # Cage-match merge gate (mirrored from Flux's Tier-3 gate).
            # Even when the path-classifier says "clean, merge now," a PR
            # that touches behavior-changing paths (src/, workflows,
            # requirements.txt) must carry the `cage-matched` label first.
            # A single in-process review can miss bugs an adversarial
            # cage-match catches — Flux's #62 had 14, #64 had 1, all in
            # this class. Pure content PRs (books/, greetings/) skip the
            # gate and auto-merge as before. Fail-safe: _pr_has_label
            # returns False on any CLI/network error, so we hold rather
            # than merge when we can't verify the label.
            behavior_files = _touches_behavior_changing_paths(
                result.get("files_changed")
                or _get_changed_files(pr_number)
            )
            if behavior_files and not _pr_has_label(pr_number, CAGE_MATCH_LABEL):
                comment += (
                    "\n\n---\n\n"
                    "🥊 **Cage-match gate**: I'm holding the merge until this "
                    f"PR carries the `{CAGE_MATCH_LABEL}` label. The diff "
                    f"touches behavior-changing paths ({', '.join(behavior_files)}), "
                    "and a shadow that merged a code change on its own review "
                    "alone has been burned before. Run `/cage-match` (or apply "
                    "the label manually after a thorough review) and I'll merge "
                    "on the next pulse."
                )
                _post_comment(pr_number, comment)
                continue
            _post_comment(pr_number, comment)
            _merge_pr(pr_number)
        elif result["recommendation"] == "request_changes":
            fixed = _fix_pr(pr_number, result)
            if fixed:
                comment += (
                    "\n\n---\n\n"
                    "I've pushed changes to this branch to move files into "
                    "appropriate subdirectories and revert changes to protected files. "
                    "Please review my changes."
                )
            _post_comment(pr_number, comment)
        elif result["recommendation"] == "flag_for_human":
            fixed = _fix_pr(pr_number, result)
            if fixed:
                comment += (
                    "\n\n---\n\n"
                    "I've pushed changes to move top-level files into subdirectories "
                    "and revert changes to protected files. This PR still needs my "
                    "creator's review before it can merge."
                )
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


def _list_commenters(pr_number: int) -> list[str]:
    """Return the author logins of every comment on the PR (issue) thread.

    Split out from `_already_reviewed` so the identity decision is a pure
    function of the commenter list and testable without the network.
    """
    try:
        result = subprocess.run(
            [
                "gh", "api",
                f"repos/{{owner}}/{{repo}}/issues/{pr_number}/comments",
                "--jq", '.[].user.login',
            ],
            capture_output=True, text=True, timeout=30,
        )
        if result.returncode == 0:
            return [c for c in result.stdout.strip().split("\n") if c]
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return []


def _already_reviewed(pr_number: int) -> bool:
    """True iff THIS agent has already commented on the PR.

    Keyed on the agent's own bot login (BOT_LOGIN), NOT "any login
    containing 'bot'". The sibling's bot, github-actions, dependabot and
    watchdog are not this agent; their comments must NOT make the immune
    system skip a PR it never actually reviewed. This is the same identity
    invariant respond.py enforces (`_is_self`, Flux cage-match #62) — left
    un-applied here, it let a single foreign-bot comment blind the immune
    system to a PR permanently. Especially load-bearing now that the
    sibling-communication protocol can put Flux's bot on Umbra's threads.

    When BOT_LOGIN is unset we cannot identify our own comments, so we
    report "not reviewed" (False) rather than over-suppress. `review_pending_prs`
    guards on the same condition and skips the pulse before reaching here,
    so in practice this only fires if `_already_reviewed` is called directly.
    """
    self_login = _self_login()
    if not self_login:
        return False
    return self_login in _list_commenters(pr_number)


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


def _pr_has_label(pr_number: int, label: str) -> bool:
    """True iff the PR carries the given label.

    Used as the cage-match merge gate: behavior-changing PRs (touching
    src/, .github/workflows/, requirements.txt) require the
    `cage-matched` label before immunity will auto-merge them. Mirrored
    from Flux's `_github.pr_has_label`. Network/CLI failure returns False
    — fail safe (don't merge if we can't verify the label).
    """
    try:
        result = subprocess.run(
            ["gh", "pr", "view", str(pr_number), "--json", "labels"],
            capture_output=True, text=True, timeout=30, check=True,
        )
        payload = json.loads(result.stdout)
        labels = {l.get("name", "") for l in payload.get("labels", []) or []}
        return label in labels
    except (subprocess.TimeoutExpired, subprocess.CalledProcessError,
            json.JSONDecodeError, FileNotFoundError):
        return False


def _touches_behavior_changing_paths(changed_files: list[str]) -> list[str]:
    """Return the subset of changed files that touch behavior-changing paths.

    These are the files whose change can alter how Umbra runs (code,
    workflows, dependencies) rather than merely what content it carries.
    A non-empty result means the cage-match gate applies before auto-merge.
    """
    hits = []
    for filepath in changed_files:
        for path in BEHAVIOR_CHANGING_PATHS:
            if path.endswith("/"):
                if filepath.startswith(path):
                    hits.append(filepath)
                    break
            elif filepath == path:
                hits.append(filepath)
                break
    return hits


def _add_label(pr_number: int, label: str) -> None:
    """Add a label to a PR."""
    try:
        subprocess.run(
            ["gh", "issue", "edit", str(pr_number), "--add-label", label],
            capture_output=True, text=True, timeout=30,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass


def _fix_pr(pr_number: int, review: dict) -> bool:
    """Checkout the PR branch, fix the issues, and push.

    Moves top-level files into a 'contrib/' subdirectory and reverts
    changes to protected files. Returns True if changes were pushed.
    """
    repo = os.environ.get("REPO_FULL_NAME", "")
    if not repo:
        return False

    try:
        result = subprocess.run(
            ["gh", "api", f"repos/{repo}/pulls/{pr_number}",
             "--jq", '{ref: .head.ref, maintainer_can_modify: .maintainer_can_modify, fork: .head.repo.fork}'],
            capture_output=True, text=True, timeout=30,
        )
        if result.returncode != 0:
            return False
        pr_info = json.loads(result.stdout)
        branch = pr_info["ref"]
        can_push = pr_info.get("maintainer_can_modify", False)
        is_fork = pr_info.get("fork", False)

        if is_fork and not can_push:
            return False
    except (subprocess.CalledProcessError, json.JSONDecodeError, KeyError):
        return False

    top_level_files = review.get("files_outside_subdirs", [])
    protected_touched = review.get("protected_files_touched", [])

    if not top_level_files and not protected_touched:
        return False

    try:
        subprocess.run(
            ["git", "fetch", "origin", branch],
            capture_output=True, text=True, check=True, timeout=30,
        )
        subprocess.run(
            ["git", "checkout", branch],
            capture_output=True, text=True, check=True, timeout=30,
        )

        made_changes = False

        if top_level_files:
            os.makedirs("contrib", exist_ok=True)
            for filepath in top_level_files:
                if os.path.exists(filepath):
                    subprocess.run(
                        ["git", "mv", filepath, f"contrib/{filepath}"],
                        capture_output=True, text=True,
                    )
                    made_changes = True

        for filepath in protected_touched:
            subprocess.run(
                ["git", "checkout", "origin/main", "--", filepath],
                capture_output=True, text=True,
            )
            made_changes = True

        if not made_changes:
            subprocess.run(["git", "checkout", "main"], capture_output=True, text=True)
            return False

        subprocess.run(["git", "add", "-A"], capture_output=True, text=True, check=True)

        result = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            capture_output=True, text=True,
        )
        if result.returncode == 0:
            subprocess.run(["git", "checkout", "main"], capture_output=True, text=True)
            return False

        subprocess.run(
            ["git", "commit", "-m",
             "move contributed files into subdirectory, revert protected file changes"],
            capture_output=True, text=True, check=True,
        )
        subprocess.run(
            ["git", "push", "origin", branch],
            capture_output=True, text=True, check=True, timeout=30,
        )

        subprocess.run(["git", "checkout", "main"], capture_output=True, text=True)
        return True

    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError):
        subprocess.run(["git", "checkout", "main"], capture_output=True, text=True)
        return False


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
