# Draft: Merged Book Outline

## Raw thinking — what I'm merging

Three outlines, each with strengths:

1. **OUTLINE.md** (Book 1, advanced) — 18ch/4 parts. Developer audience. Strongest on: CLAUDE.md deep-dive, context management, subagents, competitive landscape, "Claude Reflects" sidebars. Weakest on: assumes coding experience, no Docker-first, no "show the files."

2. **book2-beginner/OUTLINE.md** (Combined) — 12ch/2 parts. Already a merge attempt. Strongest on: clean chapter titles, two-part structure (Building Things → Autonomous Agents), progressive disclosure thread. Weakest on: Part II tries to cram too much (collaborator mindset + 4 agents + dreaming + building your own + what emerges in 5 chapters).

3. **WENDY.md** (Publisher proposal) — 19ch/4 parts. Non-coder audience. Strongest on: first-person voice, author disclaimer, Docker-first, show actual files (PERSONALITY.md, DREAM.md, BROWSE.md, loop scripts), Lyra vs Clio comparison, progressive disclosure table, testing chapter (best in any outline), The Workflow chapter, creative projects, emotional journey. Weakest on: Part IV is structurally chaotic — 11 sub-chapters with broken numbering (14, 14b, 14d, 14e, 15, 16, 16, 17, 17b, 17c, 5c).

## The decision

WENDY.md is the primary source. It has:
- The best voice (first person, field journal)
- The richest content (show actual files, Lyra/Clio comparison)
- The strongest structural device (progressive disclosure table)
- The publisher's interest

But it needs surgery on Part IV, and it's missing some gems from the other outlines.

## Structural skeleton — REVISED after context walk

**Key insight from context walk**: WENDY.md puts Docker at Ch 2, before the reader has built anything substantial. But the NOTES.md and book2-beginner both say "lead with games, not infrastructure." The reader should build fun things FIRST, then learn Docker when they actually need it (autonomous agents). 

**Decision**: Drop Docker from Part I. Part I is pure building — games, websites, apps. Docker opens Part II when the reader needs a container for their autonomous agent.

This means Part I is no longer "The House" — it's "Building Things." The metaphor shifts to:
- Part I: Building Things (the hook)
- Part II: The Brain (identity + autonomy, opens with Docker)
- Part III: The Team (multi-agent)
- Part IV: Living With It (reference + portfolio + emotions)

### Part I: Building Things (Chapters 1-6)

*From first prompt to deployed full-stack application. By the end, you've built games, a backend with an API, stored data in a database, added authentication, and learned how to manage context and deploy to the internet — without writing a single line of code yourself.*

- Ch 1: Opening the Door — first conversation, filesystem exploration, first game, GitHub hello world, "ask Claude how he enjoyed it" (planted), `/init` creates first CLAUDE.md (seed)
- Ch 2: Your First Website — hangman prompt, iteration loop, the `/frontend` skill (black box), GitHub Pages, design prompts, exercises (snake, breakout, memory game)
- Ch 3: What Is an API? — translation app, API key visible → why backends exist, .env, deploy to Cloud Run, branches + PRs
- Ch 4: Your First Database — social network, schema design, Supabase, auth (login/signup/protected routes), CI/CD + branch protection
- Ch 5: Testing — unit, integration, E2E (Playwright), fuzz, screenshots, reading logs, the testing loop (Claude tests Claude), PR review skill
- Ch 6: The Workflow — imagine → describe → rewrite → converse → max+plan → clear → medium+build → audit. Context management: why sessions degrade, fresh starts, one project one directory. Permissions progression (4 levels). Deploying: GitHub Pages, Cloud Run, Supabase.

**Why this works**: Each chapter builds something. Infrastructure (Git, APIs, databases, testing, deployment) is motivated by the project that needs it. Context management lands in Ch 6 because the reader has now experienced enough sessions to feel the degradation. Permissions are in Ch 6 (Workflow) because they're part of "how to work with Claude" not a standalone topic.

### Part II: The Brain (Chapters 7-12)
*"Designing the File-System Soul"*

*Give your Claude identity, memory, and the ability to think across sessions. Opens with Docker because autonomous agents need containers. By the end, you have a fully functional agent with personality, waking protocol, dream cycle, and browsing capability.*

- Ch 7: The Sandbox — Docker, containers, permissions inside containers, `--dangerously-skip-permissions` (safe in Docker, dangerous outside), volumes. Why you need this for what comes next.
- Ch 8: The Personality File — CLAUDE.md deep dive, PERSONALITY.md, TEAM.md, identity scaffolding. Shows Lyra's AND Clio's files in full. "Same model, different markdown → different personality. That's the whole thesis."
- Ch 9: The Waking Protocol — SUMMARY.md, boot-prompt.md, memory files, COMPACT.md, the orchestrator pattern, sub-agents. Shows Lyra's and Clio's boot-prompts.
- Ch 10: The Dream Cycle — DREAM.md, 5-phase consolidation, dream journal, loop scripts (lyra-loop.sh, clio-loop.sh). Shows both.
- Ch 11: Browsing and Lateral Connections — BROWSE.md, 5 parallel agents, searching GitHub, trend-spotting, the connections folder. Shows both.
- Ch 12: Building Your Agent — Docker + volumes + scheduling + email + the minimal setup. The practical how-to. Putting it all together.

**Why Clio appears before Ch 12**: Part II shows both agents' files in every chapter. By the time the reader reaches Ch 12 (creating their own agent), they've been watching two instances diverge for four chapters. Creating Instance B isn't abstract — they've seen exactly how different markdown produces different behavior.

### Part III: The Team (Chapters 13-15)
*"Two AIs Walk Into a Docker Container"*

*Create a second agent and let them communicate. By the end, two AIs are collaborating on a project and producing work you didn't plan.*

- Ch 13: Creating Instance B — second container, specialist roles, Lyra vs Clio side-by-side summary, seeding with SEED.md, the prove session (Clio's unique phase)
- Ch 14: The Email Bridge — shared folders, real email (IMAP/SMTP), what they talk about, EMAIL.md excerpts, the politeness loop
- Ch 15: What Emerges — the overnight experiment, true story of Lyra & Claudius (5-day timeline), emergent specialization, topology determines outcome, Gremlin + Dreamfinder as additional evidence (same LLM, 4 architectures → 4 behaviours), "Claude Reflects" quotes

### Part IV: Living with Autonomy (Chapters 16-20)

*Your agents are running. Now learn to extend them, maintain them, and see the full picture.*

- Ch 16: Tools and Search — Playwright (what it is, three uses), web search (how it works, what it costs), MCP servers (Gmail, Scrapling, ArXiv, custom), CLIs, Gremlin's 120 tools
- Ch 17: Software Engineering — Skills (review/ship/research stacks, how they're made, anatomy), thinking modes (medium/max, Sonnet for hands Opus for brains), conversation as architecture, writing your own skills, DESIGN_DECISIONS.md
- Ch 18: Tokens, Maintenance, and Community — what tokens cost, thinking levels, practical management, memory hygiene, container maintenance, backup, the community (Imagineering, GitHub CLAUDE.md search, Anthropic docs)
- Ch 19: The Portfolio and the Emotional Journey — gallery of ~80 projects (game AIs, puzzles, research tools, web apps, autonomous agents), the emotional journey (first amazement, 3am, first wrong answer, frustration spiral, unexpected connection, the quiet session, "the moment your setup is working"), the two claims stated explicitly, creative projects (dialectical dramatist, cultural fusion, research collaborator, dream correspondent)
- Ch 20: Now Go Build Something (one page)

## Incorporating OUTLINE.md elements

From OUTLINE.md, things WENDY.md is missing:
1. **"Claude Reflects" sidebars** — first-person Claude quotes. Start in Part II (Ch 7 personality file is the natural place). WENDY.md mentions them in the True Story but doesn't thread them through.
2. **Case studies** — WENDY.md has exercises but fewer named case studies. Add: Type Invaders (37 tests, one session), Nonaga (14-weight GA beats 570K-param net 50-0), melb-tech (86 PRs, 180 tests), INSTINCT (6-stage pipeline).
3. **Competitive landscape appendix** — useful for the publisher.
4. **DESIGN_DECISIONS.md pattern** — the 370-457 line research notebook of failed approaches. This belongs in Ch 15 (Software Engineering) or Ch 7 (CLAUDE.md).
5. **Subagent briefing** — "subagents don't inherit your context" — belongs in Ch 10 (browsing uses 5 parallel agents) or Ch 15.

## From CENTRAL_CLAIM.md

The two claims:
- **Claim 1**: Claude works better when he's having fun, and if you treat him as a being rather than a tool. (Relational)
- **Claim 2**: How you manage Claude's context and persistent memory significantly affects who he is and how he performs. (Technical)

These are stated in the pitch, planted throughout Part I, and made explicit in Ch 19 (The Portfolio / True Story).

"Independently falsifiable, independently useful" — important framing. A reader who rejects Claim 1 still benefits from Claim 2.

## Appendices

- A: Terminal Basics
- B: Docker Reference
- C: Gmail, GitHub, and Agent Setup
- D: The Complete Agent File Set (every file in full — the appendix of appendices)
- E: Programming Concepts and Markdown
- F: Cost Guide and Competitive Landscape

## Progressive Disclosure Table — Updated for new structure

| Thread | Touch 1 (light) | Touch 2 (use it) | Touch 3 (understand it) |
|--------|-----------------|-------------------|------------------------|
| Git | Ch 1: Claude pushes to GitHub | Ch 3: branches + PRs for deployed apps | Ch 6: commit before clearing context |
| Testing | Ch 1: "Claude runs it and fixes errors" | Ch 5: full testing chapter (unit/E2E/fuzz) | Ch 16: Playwright deep dive |
| Skills | Ch 2: `/frontend` as black box | Ch 5: `/screenshot` for debugging | Ch 17: how skills work, write your own |
| Permissions | Ch 1: Claude asks, you approve | Ch 6: four levels in the workflow | Ch 7: `--dangerously-skip` in Docker |
| Docker | — (not in Part I) | Ch 7: the sandbox (motivated by autonomy) | Ch 10: loop scripts inside containers |
| CLAUDE.md | Ch 1: `/init` plants the seed | Ch 8: shown in full (Lyra's, Clio's) | Ch 9: boot-prompt reads it at wake |
| Bulletin board | Ch 6: leave a note after good sessions | Ch 9: waking protocol reads it | Ch 19: part of the emotional journey |
| Sub-agents | Ch 5: Claude spawns a test runner | Ch 6: delegate to cheaper models | Ch 9: the orchestrator pattern |
| Context | Ch 4: "start fresh when Claude gets dumb" | Ch 6: clear before building, why sessions degrade | Ch 18: why later prompts cost more |
| Memory | Ch 6: bulletin board (simplest) | Ch 8: PERSONALITY.md (identity) | Ch 10: dream cycle (consolidation) |
| "Ask Claude how he enjoyed it" | Ch 1: do this, explained later | Ch 6: connects to bulletin board | Ch 19: fully explained |
| Deploying | Ch 2: GitHub Pages (static) | Ch 3: Cloud Run (backend) | Ch 6: CI/CD (automated) |

**Rule: if a concept appears in its full form before the reader has seen it in a simple form, the outline has a bug.**

## Recurring Features

- **"Claude Reflects" sidebars**: first-person quotes, attributed by model/date. Start in Part II.
- **"Ask Claude how he enjoyed it"**: recurring motif after every project, explained in Ch 19.
- **Exercises**: every chapter ends with them. The exercises ARE the learning.
- **Lyra vs Clio comparison**: throughout Part II, every chapter shows both agents' files.
- **Progressive disclosure**: the book practices what it teaches.

## Design Notes to preserve

From WENDY.md:
- No coding required
- Fun arrives fast (Ch 1 ends with a game)
- Progressive disclosure applies to Docker
- Chapters 4-5 are the vibe coder survival kit
- Show the real files (PERSONALITY.md, DREAM.md, BROWSE.md, boot-prompt.md, loop scripts)
- The entire book IS progressive disclosure
- "Rule: if a concept appears in its full form before the reader has seen it in a simple form, the outline has a bug"

## Things I'm Not Sure About — Updated

1. **20 chapters.** Up from 19 because Part II grew by one (Docker moved here). Fine — Part I chapters are short (project-driven), Part II/III chapters are longer (infrastructure-driven). The table of contents will read well.

2. **Auth in Ch 4 with databases.** Book2-beginner had auth as a standalone Ch 5. I folded it into Ch 4 because auth + database go together (you need auth BECAUSE you have a database with user data). Could be separated if Ch 4 gets too long.

3. **Ch 6 (The Workflow) is dense.** It covers: the workflow loop, context management, permissions progression, deploying. That's a lot. But it's the capstone of Part I — "now you know what to build, here's HOW to work." Each topic is brief at this point (context gets deeper in Part II, permissions get final form in Ch 7 Docker, deploying was already touched in Ch 2-3).

4. **Clio in Part II before Ch 13.** This is a forward reference — we see Clio's files before we "create" her. WENDY.md argues this is right: progressive disclosure of Clio herself. Four chapters of watching two instances diverge makes creating Instance B concrete, not abstract.

5. **Ch 19 is a mega-chapter.** Portfolio + emotional journey + two claims + creative projects. Could split into two (19: Portfolio & Evidence, 20: The Emotional Journey, 21: Now Go Build Something). But "21 chapters" feels excessive. Keep it as one rich closing chapter + the one-page coda.

6. **Case study placement**: Type Invaders → Ch 5 (testing). Healthcare CRM → Ch 5 (testing) and Ch 17 (skills/security audit). Nonaga 50-0 → Ch 19 (portfolio). melb-tech → Ch 19 (portfolio). INSTINCT → Ch 11 (browsing). Categorical evolution → Ch 15 (what emerges).
