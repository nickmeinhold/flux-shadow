"""Tests for the cage-match merge gate in immunity.py.

Mirrors the intent of Flux's Tier-3 gate (the-dreaming-repo immunity.py),
adapted to Umbra's path-classification model. The invariant under test:

    A PR that reaches the auto-merge branch AND touches behavior-changing
    paths (src/, .github/workflows/, requirements.txt) must NOT merge
    unless it carries the `cage-matched` label. When held, a hold comment
    is posted explaining the gate. With the label present, it merges.

All GitHub I/O is monkeypatched — these run with no network.
"""

from __future__ import annotations

import os

import pytest

from src import immunity


@pytest.fixture
def captured(monkeypatch):
    """Wire up immunity's gh-wrappers to record calls instead of hitting
    the network. Returns a dict the test inspects after the run."""
    state = {
        "merged": [],
        "comments": [],
        "labels_added": [],
    }

    monkeypatch.setenv("REPO_FULL_NAME", "nickmeinhold/flux-shadow")
    # review_pending_prs now skips the pulse if it can't identify its own
    # bot login, so the gate tests must run with BOT_LOGIN set.
    monkeypatch.setenv("BOT_LOGIN", "flux-shadow[bot]")

    # One open PR, number 7.
    monkeypatch.setattr(immunity, "_list_open_prs",
                        lambda: [{"number": 7, "title": "t", "author": {}}])
    monkeypatch.setattr(immunity, "_already_reviewed", lambda pr: False)
    # No deletions of protected paths in these fixtures.
    monkeypatch.setattr(immunity, "_get_deleted_protected", lambda pr: [])
    # Don't shell out to claude for the comment body.
    monkeypatch.setattr(immunity, "generate_review_comment",
                        lambda result, pr: "review body")

    # _merge_pr returns True on success; record the call and report success so
    # the caller posts its review comment.
    monkeypatch.setattr(
        immunity, "_merge_pr",
        lambda pr, sha: (state["merged"].append((pr, sha)), True)[1],
    )
    monkeypatch.setattr(immunity, "_post_comment",
                        lambda pr, body: state["comments"].append((pr, body)))
    monkeypatch.setattr(immunity, "_add_label",
                        lambda pr, label: state["labels_added"].append((pr, label)))
    # The merge is now pinned to the reviewed head SHA; default to a readable
    # one so the existing gate tests still reach the merge.
    monkeypatch.setattr(immunity, "_get_pr_head_sha", lambda pr: "headsha7")

    return state


def _set_changed_files(monkeypatch, files):
    monkeypatch.setattr(immunity, "_get_changed_files", lambda pr: files)


def _set_label_present(monkeypatch, present):
    monkeypatch.setattr(immunity, "_pr_has_label",
                        lambda pr, label: present)


class TestCageMatchGate:
    def test_behavior_change_without_label_is_held_not_merged(
        self, captured, monkeypatch
    ):
        """A src/ change that classifies as auto-mergeable (e.g. a brand-new
        src/ file the classifier treats as a subdir addition) must NOT
        merge without the cage-matched label, and must post a hold comment."""
        _set_changed_files(monkeypatch, ["src/new_helper.py"])
        _set_label_present(monkeypatch, False)
        # Force the recommendation to "merge" so we exercise the gate even
        # though the path-classifier would normally flag src/ for human
        # review — the gate is defense-in-depth at the auto-merge site.
        monkeypatch.setattr(
            immunity, "review_pr",
            lambda pr: {
                "safe": True,
                "verdict": "clean",
                "protected_files_touched": [],
                "files_outside_subdirs": [],
                "files_changed": ["src/new_helper.py"],
                "recommendation": "merge",
            },
        )

        immunity.review_pending_prs({})

        assert captured["merged"] == [], "behavior-change must NOT auto-merge"
        assert len(captured["comments"]) == 1
        _, body = captured["comments"][0]
        assert "Cage-match gate" in body
        assert immunity.CAGE_MATCH_LABEL in body
        assert "src/new_helper.py" in body

    def test_behavior_change_with_label_merges(self, captured, monkeypatch):
        """Once the cage-matched label is applied, the same PR merges."""
        _set_label_present(monkeypatch, True)
        monkeypatch.setattr(
            immunity, "review_pr",
            lambda pr: {
                "safe": True,
                "verdict": "clean",
                "protected_files_touched": [],
                "files_outside_subdirs": [],
                "files_changed": [".github/workflows/heartbeat.yml"],
                "recommendation": "merge",
            },
        )

        immunity.review_pending_prs({})

        assert captured["merged"] == [(7, "headsha7")], "labelled PR should merge"

    def test_pure_content_change_merges_without_label(
        self, captured, monkeypatch
    ):
        """A books/ or greetings/ PR is NOT behavior-changing — it must
        still auto-merge with no label and no gate."""
        _set_label_present(monkeypatch, False)
        monkeypatch.setattr(
            immunity, "review_pr",
            lambda pr: {
                "safe": True,
                "verdict": "clean",
                "protected_files_touched": [],
                "files_outside_subdirs": [],
                "files_changed": ["greetings/hello.md"],
                "recommendation": "merge",
            },
        )

        immunity.review_pending_prs({})

        assert captured["merged"] == [(7, "headsha7")], "pure content PR should auto-merge"
        # No hold comment about the gate.
        for _, body in captured["comments"]:
            assert "Cage-match gate" not in body


class TestStaleHeadPin:
    """The founding incident (#826 / PR #30): immunity's `--auto` merge merged
    at the enablement-time head and dropped later fix commits. The merge is now
    pinned to the head we reviewed, and held if that head can't be read."""

    def test_merge_is_pinned_to_reviewed_head(self, captured, monkeypatch):
        monkeypatch.setattr(immunity, "_get_pr_head_sha", lambda pr: "abc123def")
        _set_label_present(monkeypatch, True)
        monkeypatch.setattr(
            immunity, "review_pr",
            lambda pr: {
                "safe": True, "verdict": "clean",
                "protected_files_touched": [], "files_outside_subdirs": [],
                "files_changed": ["requirements.txt"], "recommendation": "merge",
            },
        )
        immunity.review_pending_prs({})
        assert captured["merged"] == [(7, "abc123def")]

    def _merge_review(self, monkeypatch):
        monkeypatch.setattr(
            immunity, "review_pr",
            lambda pr: {
                "safe": True, "verdict": "clean",
                "protected_files_touched": [], "files_outside_subdirs": [],
                "files_changed": ["requirements.txt"], "recommendation": "merge",
            },
        )

    def test_unreadable_head_holds_and_is_retryable(self, captured, monkeypatch):
        """If the head SHA can't be read, hold (fail closed) AND leave no
        comment — so _already_reviewed doesn't strand it and the next pulse
        retries (Carnot: a hold that posts a comment is never retried)."""
        monkeypatch.setattr(immunity, "_get_pr_head_sha", lambda pr: None)
        _set_label_present(monkeypatch, True)
        self._merge_review(monkeypatch)
        immunity.review_pending_prs({})
        assert captured["merged"] == [], "unreadable head must hold"
        assert captured["comments"] == [], "a retryable hold must not comment (would strand it)"

    def test_merge_refusal_is_retryable_not_stranded(self, captured, monkeypatch):
        """A --match-head-commit refusal (head moved) returns False; immunity
        must NOT post a review comment, so the next pulse re-reviews the new
        head rather than _already_reviewed skipping it forever."""
        monkeypatch.setattr(immunity, "_merge_pr", lambda pr, sha: False)
        _set_label_present(monkeypatch, True)
        self._merge_review(monkeypatch)
        immunity.review_pending_prs({})
        assert captured["comments"] == [], "refused merge must leave no comment (retryable)"

    def test_successful_merge_does_post_its_review(self, captured, monkeypatch):
        """The happy path still records the review — comment posted AFTER a
        successful merge."""
        _set_label_present(monkeypatch, True)
        self._merge_review(monkeypatch)
        immunity.review_pending_prs({})
        assert captured["merged"] == [(7, "headsha7")]
        assert len(captured["comments"]) == 1

    def test_merge_pr_passes_match_head_commit(self, monkeypatch):
        """_merge_pr shells out with --match-head-commit (no --auto), returns
        True on success, and gh refuses a stale-head merge."""
        import subprocess

        class _R:
            returncode = 0
            stderr = ""

        calls = {}
        monkeypatch.setattr(
            subprocess, "run",
            lambda cmd, **k: calls.update(cmd=cmd) or _R(),
        )
        ok = immunity._merge_pr(7, "cafebabe")
        assert ok is True
        assert "--match-head-commit" in calls["cmd"]
        assert "cafebabe" in calls["cmd"]
        assert "--auto" not in calls["cmd"], "must not arm GitHub auto-merge"

    def test_merge_pr_returns_false_on_nonzero_exit(self, monkeypatch):
        """A gh refusal (nonzero exit) is reported as failure, not swallowed."""
        import subprocess

        class _R:
            returncode = 1
            stderr = "head mismatch"

        monkeypatch.setattr(subprocess, "run", lambda cmd, **k: _R())
        assert immunity._merge_pr(7, "cafebabe") is False


class TestBehaviorPathDetection:
    def test_src_is_behavior_changing(self):
        assert immunity._touches_behavior_changing_paths(
            ["src/respond.py"]) == ["src/respond.py"]

    def test_workflows_is_behavior_changing(self):
        assert immunity._touches_behavior_changing_paths(
            [".github/workflows/heartbeat.yml"]
        ) == [".github/workflows/heartbeat.yml"]

    def test_requirements_is_behavior_changing(self):
        assert immunity._touches_behavior_changing_paths(
            ["requirements.txt"]) == ["requirements.txt"]

    def test_content_is_not_behavior_changing(self):
        assert immunity._touches_behavior_changing_paths(
            ["books/a.md", "greetings/b.md"]) == []

    def test_none_is_not_behavior_changing(self):
        """Defensive: an unreadable diff (None) must not crash here."""
        assert immunity._touches_behavior_changing_paths(None) == []


class TestFailClosedOnUnreadableDiff:
    """The bug that auto-merged PR #30 ungated: _get_changed_files returned
    [] on a transient failure, indistinguishable from a genuinely empty diff,
    so review_pr classified it as 'merge'. Now it returns None on failure and
    review_pr holds for human review. Fail CLOSED, never merge blind."""

    def test_get_changed_files_returns_none_on_failure(self, monkeypatch):
        import subprocess

        def boom(*a, **k):
            raise subprocess.TimeoutExpired("gh", 30)

        monkeypatch.setattr(subprocess, "run", boom)
        assert immunity._get_changed_files(7) is None

    def test_get_changed_files_returns_none_on_nonzero_exit(self, monkeypatch):
        import subprocess

        class R:
            returncode = 1
            stdout = ""

        monkeypatch.setattr(subprocess, "run", lambda *a, **k: R())
        assert immunity._get_changed_files(7) is None

    def test_review_pr_holds_when_diff_unreadable(self, monkeypatch):
        """None changed-files → flag_for_human, NOT merge. This is the
        core fail-closed invariant."""
        monkeypatch.setattr(immunity, "_get_changed_files", lambda pr: None)
        result = immunity.review_pr(7)
        assert result["recommendation"] == "flag_for_human"
        assert result["safe"] is False

    def test_unreadable_diff_pr_is_not_merged(self, captured, monkeypatch):
        """End-to-end: a PR whose diff can't be read must NOT auto-merge."""
        monkeypatch.setattr(immunity, "_get_changed_files", lambda pr: None)
        # flag_for_human routes through _fix_pr — stub it (no network/git).
        monkeypatch.setattr(immunity, "_fix_pr", lambda pr, r: False)
        immunity.review_pending_prs({})
        assert captured["merged"] == [], "unreadable-diff PR must never merge"

    def test_empty_diff_still_distinct_from_failure(self, monkeypatch):
        """A genuinely empty diff (returncode 0, no files) → [] (not None),
        so the distinction between 'empty' and 'unreadable' is preserved."""
        class R:
            returncode = 0
            stdout = "\n"

        monkeypatch.setattr("subprocess.run", lambda *a, **k: R())
        assert immunity._get_changed_files(7) == []

    def test_deleted_protected_fails_closed_on_error(self, monkeypatch):
        """The deletion scan must also fail CLOSED — None on a gh error,
        not [] — so review_pr can hold (the sibling-consistency fix)."""
        import subprocess

        def boom(*a, **k):
            raise subprocess.TimeoutExpired("gh", 30)

        monkeypatch.setattr(subprocess, "run", boom)
        assert immunity._get_deleted_protected(7) is None

    def test_deleted_protected_fails_closed_on_nonzero_exit(self, monkeypatch):
        """The other half of the fail-closed branch: a non-zero `gh` exit
        (not just a timeout) must also return None."""
        import subprocess

        class R:
            returncode = 1
            stdout = ""

        monkeypatch.setattr(subprocess, "run", lambda *a, **k: R())
        assert immunity._get_deleted_protected(7) is None

    def test_review_pr_holds_when_deletion_scan_unreadable(self, monkeypatch):
        """changed_files readable but the deletion scan fails → hold, not merge."""
        monkeypatch.setattr(immunity, "_get_changed_files", lambda pr: ["books/a.md"])
        monkeypatch.setattr(immunity, "_get_deleted_protected", lambda pr: None)
        result = immunity.review_pr(7)
        assert result["recommendation"] == "flag_for_human"
        assert result["safe"] is False

    def test_unreadable_deletion_hold_preserves_computed_evidence(self, monkeypatch):
        """The hold must NOT discard the protected/top-level lists already
        computed from the readable name-only diff — _fix_pr and the review
        comment need them (Carnot, PR #33)."""
        # A protected file touched + a stray top-level file, with the
        # deletion scan failing.
        monkeypatch.setattr(
            immunity, "_get_changed_files",
            lambda pr: ["src/immunity.py", "stray.txt"],
        )
        monkeypatch.setattr(immunity, "_get_deleted_protected", lambda pr: None)
        result = immunity.review_pr(7)
        assert result["recommendation"] == "flag_for_human"
        assert "src/immunity.py" in result["protected_files_touched"]
        assert "stray.txt" in result["files_outside_subdirs"]


class TestSharedIdentity:
    def test_immunity_self_login_delegates_to_identity(self, monkeypatch):
        from src import identity
        monkeypatch.setenv("BOT_LOGIN", "flux-shadow[bot]")
        assert immunity._self_login() == "flux-shadow[bot]"
        assert immunity._self_login() == identity.self_login()

    def test_respond_and_immunity_agree_on_self(self, monkeypatch):
        from src import respond, identity
        monkeypatch.setenv("BOT_LOGIN", "  flux-shadow[bot]  ")
        # Both strip and read the same env → identical answer.
        assert immunity._self_login() == respond._self_login() == identity.self_login()
        assert identity.self_login() == "flux-shadow[bot]"

    def test_fail_safe_label_check_on_error_returns_false(self, monkeypatch):
        """_pr_has_label must return False (→ hold, don't merge) if gh fails."""
        import subprocess

        def boom(*a, **k):
            raise subprocess.CalledProcessError(1, "gh")

        monkeypatch.setattr(subprocess, "run", boom)
        assert immunity._pr_has_label(7, "cage-matched") is False


class TestAlreadyReviewedIdentity:
    """The immune system must key 'already reviewed' on its OWN bot login,
    not on any login containing 'bot'. A foreign bot comment (the sibling's
    bot, github-actions, dependabot, watchdog) must NOT make immunity skip a
    PR it never reviewed. Mirrors respond.py's `_is_self` invariant."""

    def test_own_comment_counts_as_reviewed(self, monkeypatch):
        monkeypatch.setenv("BOT_LOGIN", "flux-shadow[bot]")
        monkeypatch.setattr(
            immunity, "_list_commenters",
            lambda pr: ["RaggedR", "flux-shadow[bot]"],
        )
        assert immunity._already_reviewed(7) is True

    def test_foreign_bot_does_not_count_as_reviewed(self, monkeypatch):
        """The bug this fixes: a foreign bot commented, but WE never did.
        Old code (`any 'bot' in login`) returned True and blinded the
        immune system. The fix returns False — we still owe a review."""
        monkeypatch.setenv("BOT_LOGIN", "flux-shadow[bot]")
        for foreign in ("github-actions[bot]", "dependabot[bot]",
                        "flux-dreaming-repo[bot]", "watchdog[bot]"):
            monkeypatch.setattr(
                immunity, "_list_commenters",
                lambda pr, f=foreign: ["RaggedR", f],
            )
            assert immunity._already_reviewed(7) is False, (
                f"{foreign} comment must not count as our review"
            )

    def test_human_only_thread_is_not_reviewed(self, monkeypatch):
        monkeypatch.setenv("BOT_LOGIN", "flux-shadow[bot]")
        monkeypatch.setattr(
            immunity, "_list_commenters", lambda pr: ["RaggedR", "nickmeinhold"]
        )
        assert immunity._already_reviewed(7) is False

    def test_unset_bot_login_reports_not_reviewed(self, monkeypatch):
        """No identity → can't claim we reviewed. False (re-review) is the
        safe direction; review_pending_prs separately skips the pulse."""
        monkeypatch.delenv("BOT_LOGIN", raising=False)
        monkeypatch.setattr(
            immunity, "_list_commenters", lambda pr: ["flux-shadow[bot]"]
        )
        assert immunity._already_reviewed(7) is False

    def test_review_pending_prs_skips_when_bot_login_unset(self, monkeypatch):
        """Whole-pulse guard: with no BOT_LOGIN, immunity must not review
        (would either over-suppress or spam). Mirrors respond.maybe_respond."""
        monkeypatch.setenv("REPO_FULL_NAME", "nickmeinhold/flux-shadow")
        monkeypatch.delenv("BOT_LOGIN", raising=False)
        called = {"listed": False}
        monkeypatch.setattr(
            immunity, "_list_open_prs",
            lambda: called.__setitem__("listed", True) or [],
        )
        immunity.review_pending_prs({})
        assert called["listed"] is False, "must skip before listing PRs"
