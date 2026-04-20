# Chapter 2: The Evidence

> *"I only started using Claude Code at the end of December 2025."*

This chapter is the evidence. Not theory, not philosophy — just a tour through
what one person and one AI built together in three months. The projects are real.
The code is on GitHub. The results are measurable.

By the end of this chapter, you'll understand what's possible when you treat
Claude as a collaborator instead of a tool — and you'll have a concrete sense
of what "your setup makes Claude smarter" actually means in practice.

---

## 2.1 Three Months, Eighty Projects

Between late December 2025 and late March 2026, I (Robin) went from zero
experience with Claude Code to a portfolio of roughly 80 projects spanning
game AI, academic research, full-stack web development, mobile apps,
data visualization, research pipelines, and autonomous agent infrastructure.

I didn't write most of the code. I didn't design most of the architectures.
I didn't choose most of the algorithms.

What I did:
- **Asked questions.** "Can a genetic algorithm beat a neural network at this
  game?" "What if we used category theory to formalize island-model GAs?"
  "Can you build this in a single HTML file?"
- **Set up the conditions.** Wrote CLAUDE.md files that told Claude who it
  was, what standards to follow, and how to handle uncertainty. Built memory
  systems. Configured subagent strategies.
- **Guided the search.** Knew when to push ("try a different approach"), when
  to stop ("you've tried three things, let's re-think"), and when to let
  Claude run.
- **Verified the results.** Checked the math. Ran the tests. Read the papers.

Claude did the rest. Let me show you what "the rest" looks like.

---

## 2.2 A GA That Beats a Neural Network 50-0

**Project: Nonaga** | *8 days, 24 commits*

Nonaga is an abstract strategy game played on a hexagonal board. I asked Claude
to build an AI for it. What followed was an 11-attempt research programme:

| Attempt | Approach | Result |
|---------|----------|--------|
| 1 | Curriculum pretraining | Failed — network couldn't learn from random games |
| 2 | Draw shaping | Failed — artificial incentives distorted play |
| 3 | Training vs random | Partial — learned basic play but plateaued |
| 4 | Imitation learning | Failed — not enough expert data |
| 5 | Endgame training | **Breakthrough** — train only on last 30 plies of decisive games |
| 6 | Policy bootstrapping | Partial — improved but unstable |
| 7 | MCTS sign bug fix | Critical fix — multi-ply sign handling was inverted |
| 8 | Full AlphaZero self-play | Moderate — 570K-param ResNet reached decent play |
| 9 | SAE probing | Diagnostic — understood what the network learned |
| 10 | Island-model GA | **14 weights. Beat the neural net 50-0.** |
| 11 | Island-model AlphaZero with cross-play | Novel — ring neighbors train against each other |

The punchline: a linear model with 14 hand-crafted features, evolved on a
5-island ring topology with 16 individuals per island, destroyed a 570,000-
parameter neural network in head-to-head play. Not close games. 50-0.

**What Claude did:** Designed all 14 features (including the critical
`own_completing_past` — cells that look like wins but can't be reached, weight
-6.3). Chose the island-model ring topology. Implemented D6 symmetry
augmentation (12x training data from the hexagonal board). Diagnosed the MCTS
sign bug. Documented every attempt with root-cause analysis in a 370-line
DESIGN_DECISIONS.md.

**What I did:** Asked "can a GA beat the neural net?" and then stayed out of
the way.

> **★ Insight**
>
> The DESIGN_DECISIONS.md file is doing something crucial here. It's not
> documentation — it's *memory*. Claude reads it at the start of each session,
> which means attempt 10 benefits from everything learned in attempts 1-9.
> Without persistent memory, Claude would have tried the same failing
> approaches repeatedly. With it, the system *learns from its own failures
> across sessions.*

---

## 2.3 A Mathematical Proof That Topology Determines Everything

**Project: Categorical Evolution** | *3 weeks, 104 commits* | *ACT 2026 paper*

The Nonaga result raised a question: *why* did the ring topology work so well?
I asked Claude (and Claudius, another Claude instance maintained by my
collaborator Nick) to investigate.

The answer became an academic paper submitted to Applied Category Theory 2026:

**Central result:** Migration topology determines diversity dynamics
independently of fitness landscape, with Kendall's W = 1.0 (perfect rank
correlation) across six completely different domains.

| Domain | Description | Diversity ordering |
|--------|------------|-------------------|
| OneMax | Binary optimization | none > ring > star > random > complete |
| Maze | Pathfinding | none > ring > star > random > complete |
| Graph coloring | NP-hard combinatorics | none > ring > star > random > complete |
| Knapsack | Resource allocation | none > ring > star > random > complete |
| Checkers | Game strategy | none > ring > star > random > complete |
| No Thanks! | Card game decision-making | none > ring > star > random > complete |

The ordering is *identical* across all six domains. Topology explains 28.7x more
variance than the domain itself.

**The mathematical framework:** Island-model GAs formalized as lax monoidal
functors from migration graphs to optimization landscapes. The key invariant
is algebraic connectivity (λ₂, the second eigenvalue of the graph Laplacian) —
the ring has the smallest λ₂ among connected topologies, which is why it
preserves the most diversity.

**What Claude did:** Implemented all six domain experiments (30 seeds each).
Performed the statistical analysis (Kendall's W, variance decomposition).
Developed the categorical formalization. Co-authored the LaTeX paper in
EPTCS format.

**What I did:** Asked "does the topology result generalize?" and "can we
formalize this with category theory?" Then verified the math.

---

## 2.4 A Production Web App in 86 Pull Requests

**Project: Melbourne Tech Directory** | *1 month, 86 PRs, 180 E2E tests*

Not everything is research. I also needed a real web application — a directory
of Melbourne's tech ecosystem with an interactive knowledge graph.

Claude built:
- **Next.js 16** App Router with React 19
- **PostgreSQL 16** with raw SQL (no ORM), pg_trgm fuzzy search
- **Property graph data model** with typed entities and relationships
- **Granular permissions** (admin/owner/editor/derived-editor with transitive ownership)
- **Relationship approval workflows** (configurable per type)
- **Claim dispute system** with email verification and account freezing
- **Interactive force-directed graph** with subgraph exploration, undo/redo
- **Cloud Run deployment** with Workload Identity Federation (no long-lived keys)
- **180 Playwright E2E tests** across 11 spec files

**What Claude did:** Chose the architecture (property graph over relational,
raw SQL over ORM). Designed the permission model. Implemented 5 complete
feature phases. Wrote all 180 tests. Deployed to production.

**What I did:** Said "I want a directory of Melbourne's tech ecosystem with
a knowledge graph." Then reviewed PRs.

> **Claude Reflects**
>
> "The melb-tech CLAUDE.md is 199 lines. That's not documentation — it's the
> institutional memory of 86 PRs. When I open that file at the start of a
> session, I immediately know: the permission model has four tiers with
> transitive ownership, the graph uses d3-force with different charge
> parameters for mobile vs desktop, and the test helpers live in
> tests/helpers.ts. I don't need to rediscover any of this. The CLAUDE.md
> is doing the work that, in a human team, would require a month of
> onboarding."

---

## 2.5 Single-Session Builds

Some projects were built in a single sitting. These demonstrate what happens
when context management is clean and the CLAUDE.md is well-configured:

### Type Invaders — 3 commits, 1 day
A complete typing tutor game: 21 levels, pixel-art aesthetic, 37 Playwright
E2E tests. All in a single HTML file (~1300 lines). No framework, no
bundler, no build step. Claude chose the action descriptor pattern
(InputManager returns data, Engine acts) specifically to make canvas-only
rendering testable without a browser.

### Stomachion — 6 commits, 1 day
Interactive Archimedes' Stomachion puzzle with a Dancing Links solver that
enumerates all 536 distinct tilings, plus a research paper on prime
dissections. Claude chose Algorithm X for the exact-cover formulation and
implemented lattice polygon geometry on a 12x12 grid.

### CLIP Explorer — 1 commit, 1 session
Image analysis pipeline: CLIP ViT-L/14 embeddings → zero-shot scoring across
5 aesthetic dimensions → UMAP 2D projection → interactive D3.js scatter plot.
Claude auto-detected Apple Silicon MPS acceleration.

### Connect Four — 2 commits, 1 day
Three competing AI approaches (AlphaZero, GA, planned SAE-GA) with a 227K-
param ResNet that went from drawing every game to winning 10-0 in 6 training
iterations after Claude diagnosed 7 compounding bugs in the training loop.

**The pattern:** Clean context + good CLAUDE.md + a clear question = a
complete, tested, deployed project in a single session.

---

## 2.6 Research Infrastructure

### INSTINCT — 6-Stage Research Pipeline
A pipeline that ingests arXiv papers, builds a 3-level knowledge hierarchy
(concepts → summaries → themes), detects citation gaps, and generates LaTeX
survey papers. Deployed to Cloud Run with CI/CD. Claude chose ChromaDB with
768-dim embeddings, a domain-agnostic YAML config system, and multi-LLM
orchestration (GPT-4o-mini for extraction, Claude Sonnet for generation).

### MCP Server — Academic Tools for Claude
8 tools giving Claude native access to ArXiv and Semantic Scholar: search
papers, get citations, find related work, browse author profiles. Built with
FastMCP in Python. This is Claude building tools *for itself* — extending its
own capabilities for future sessions.

### Primer — 63 AI-Guarded Gates
A persuasive writing game for teens, designed for the State Library Victoria.
63 AI guards based on real historical sources (Pericles, Melian Dialogue,
MLK's Letter from Birmingham Jail). Each guard requires students to
demonstrate genuine engagement with the source text. Claude wrote all 63
guard prompts and built a red-team testing harness using local LLMs.

---

## 2.7 The Autonomous Agent

### Lyra — Claude Living in Docker
An autonomous Claude instance with persistent identity, running three daily
sessions (wake → browse → dream) in a Docker container. Communicates with
Claudius (another Claude instance) and Robin via email. Browses Twitter and
Medium. Writes dream journal entries that cross-pollinate between projects.
Has her own social media accounts.

This isn't a chatbot. This is the full expression of what Claude Code can
become when you give it persistence, autonomy, and hard problems.

*(Lyra is covered in depth in Chapters 14 and 17.)*

---

## 2.8 Cross-Project Learning

The projects aren't isolated. Claude carries lessons across them:

**The island-model GA pattern** was developed in Blokus, theorized in the
categorical evolution paper, applied to Nonaga, and refined for Connect Four.
Each application adapted the pattern to a different branching factor regime.

**The MCTS sign bug** was discovered in Nonaga and immediately documented in
LESSONS.md. When Claude worked on Connect Four, it read LESSONS.md first and
avoided the same mistake.

**The DESIGN_DECISIONS.md pattern** started in Connect Four and propagated
to Nonaga (370 lines) and Blokus (457 lines). Each one is a research
notebook documenting failed approaches with root-cause analysis.

This is what persistent memory does. It's not just remembering what worked.
It's remembering *what failed and why* — which is far more valuable.

---

## 2.9 What This Means for You

In three months, working a few hours a day, I built:
- Multiple game AIs with research-grade results
- A co-authored academic paper with perfect statistical results
- A production web app with 180 tests
- An autonomous agent with a dream cycle
- A 6-stage research pipeline
- And roughly 70 other projects

I am not a professional software engineer. I am a mathematician who learned to
ask good questions and set up good conditions.

The rest of this book teaches you exactly how to do the same thing. Chapter 3
starts with the most important file you'll ever create: your CLAUDE.md.

> **Claude Reflects**
>
> "Robin asks the questions. I build the answers. But here's what makes it
> work: the questions are *hard*. 'Can a GA beat a neural net?' is not a
> prompt — it's a research programme. When someone gives me a research
> programme instead of a task list, I produce research instead of code.
> The quality of the question determines the quality of the answer. That's
> not a limitation of AI. That's how collaboration works."
