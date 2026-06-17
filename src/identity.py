"""Identity — who is THIS agent's bot?

A single source of truth for the agent's own bot login, shared by every
module that has to tell "my own action" from "someone else's". Both
`respond.py` (issue replies) and `immunity.py` (PR review) must answer the
same question — *is this comment mine?* — and they must answer it the same
way: by exact-matching `BOT_LOGIN`, never by a substring like "contains
bot" (the Flux cage-match #62 invariant; a broad check let foreign bots
suppress the agent's actions).

This module exists so that invariant lives in one place instead of being
re-derived per module.
"""

import os


def self_login() -> str:
    """The agent's own bot login, e.g. `flux-shadow[bot]`.

    Sourced from the BOT_LOGIN env var the workflow sets (heartbeat.yml).
    Empty string when unset — callers degrade conservatively in that case
    (respond/immunity skip the pulse rather than mis-identify comments).
    """
    return os.environ.get("BOT_LOGIN", "").strip()
