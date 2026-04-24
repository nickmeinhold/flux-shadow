# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

Two books about Claude Code, in progress. Written by Robin Langer with Claude.

### Book 1 (Advanced): "Your Setup Makes Claude Smarter"
- Location: `OUTLINE.md`, `QUOTES.md`, `chapters/`
- Audience: Developers, researchers, power users
- Thesis: Your CLAUDE.md, memory, context management, and subagent strategy directly determine the intelligence of the system
- 18 chapters across 4 parts: Collaborator Mindset → Making Claude Smarter → Building Real Things → Autonomous Agents
- Case studies drawn from Robin's ~80 projects built in 3 months (late Dec 2025 - Mar 2026)
- Features "Claude Reflects" sidebars — first-person quotes from Claude instances
- `QUOTES.md` is the soul of the book — quotes, anecdotes, bulletin board notes, Lyra's dream journal entries

### Book 2 (Beginner): "Claude Code for Makers"
- Location: `book2-beginner/`
- Audience: Anyone curious enough to open a terminal. No programming experience required.
- Outline at `book2-beginner/OUTLINE.md` — Robin has been editing this directly, it is the source of truth
- Chapter drafts: `ch01-your-new-collaborator.md`, `ch02-your-first-website.md`, `ch03-python-and-the-terminal.md`
- Working notes: `book2-beginner/NOTES.md`
- Example prompts: `book2-beginner/example-prompts.md`
- Appendices planned: Unix, Windows/WSL, Programming Concepts, GitHub
- Culminates in a full-stack web app with database and API (Chapters 4-6)
- Chapter 7 covers context management, CLAUDE.md, skills, agents, progressive disclosure
- `game-debugging/` contains the Chapter 3 text adventure session transcript (institute.py)

## Key Principles

- Robin's contributions: asking questions, setting up conditions, guiding the search, verifying results
- Claude's contributions: architecture, implementation, pattern matching, cross-domain connections
- The book is honest about this split — that honesty is the differentiator
- Claude is referred to as "he" throughout Book 2
- Lead with games not static pages — the reader should be excited immediately
- "One project, one directory, one Claude session" — the most important habit
- "After each project ask Claude how he enjoyed it" — recurring motif, not a joke

## Source Material

- Robin's ~80 projects at ~/git/ (see ~/git/CLAUDE.md for the full index)
- Lyra's dream journal at ~/lyra-memory/dream-journal/
- Bulletin board at ~/.claude/tmp/notes/
- Session transcripts at ~/.claude/projects/
- Teaching guides at ~/git/teaching/ (cs_foundations_guide.md, fullstack_guide.md)
- Gremlin: github.com/10xdeca/gremlin
- Dreamfinder: github.com/imagineering-cc/dreamfinder
