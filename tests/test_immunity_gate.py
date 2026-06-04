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

    # One open PR, number 7.
    monkeypatch.setattr(immunity, "_list_open_prs",
                        lambda: [{"number": 7, "title": "t", "author": {}}])
    monkeypatch.setattr(immunity, "_already_reviewed", lambda pr: False)
    # No deletions of protected paths in these fixtures.
    monkeypatch.setattr(immunity, "_get_deleted_protected", lambda pr: [])
    # Don't shell out to claude for the comment body.
    monkeypatch.setattr(immunity, "generate_review_comment",
                        lambda result, pr: "review body")

    monkeypatch.setattr(immunity, "_merge_pr",
                        lambda pr: state["merged"].append(pr))
    monkeypatch.setattr(immunity, "_post_comment",
                        lambda pr, body: state["comments"].append((pr, body)))
    monkeypatch.setattr(immunity, "_add_label",
                        lambda pr, label: state["labels_added"].append((pr, label)))

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

        assert captured["merged"] == [7], "labelled PR should merge"

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

        assert captured["merged"] == [7], "pure content PR should auto-merge"
        # No hold comment about the gate.
        for _, body in captured["comments"]:
            assert "Cage-match gate" not in body


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

    def test_fail_safe_label_check_on_error_returns_false(self, monkeypatch):
        """_pr_has_label must return False (→ hold, don't merge) if gh fails."""
        import subprocess

        def boom(*a, **k):
            raise subprocess.CalledProcessError(1, "gh")

        monkeypatch.setattr(subprocess, "run", boom)
        assert immunity._pr_has_label(7, "cage-matched") is False
