# Your Setup Makes Claude Smarter

## Central Thesis

**Your setup decisions — CLAUDE.md, persistent memory, context management,
subagent strategy — directly determine the intelligence of the system you're
working with.**

This is not a tutorial on Claude Code. It's a field guide for human-AI
collaboration, backed by evidence from ~80 projects built in three months by
a mathematician who asked good questions and an AI that did the heavy lifting.

## Working Title Options
1. **Your Setup Makes Claude Smarter**: A Field Guide to Human-AI Collaboration
2. **The Orchestrated Agent**: Building Collaborative AI with Claude Code
3. **Beyond the Chatbot**: Persistent Memory, Subagents, and the Collaborator Mindset

## The Gap This Book Fills

Existing books on agentic AI (Lanham, Infante, Fajardo, et al.) teach frameworks
like LangChain, LangGraph, and CrewAI. They treat AI as a tool to be commanded.

This book treats AI as a collaborator to be *set up*. The human's job is to ask
hard questions and create the right conditions. Claude's job is architecture,
implementation, pattern matching, and cross-domain connection-making. The boundary
between these roles is defined by your CLAUDE.md.

No other book makes this claim. And ~80 GitHub projects built in three months
provide the evidence.

## Target Audience

- **Developers with general programming experience** (Python, JS/TS, or similar)
  who want to build ambitious things with Claude Code — not just get help with syntax
- **Technical team leads** evaluating AI coding tools for their teams
- **Researchers and academics** who want an AI collaborator for papers, experiments,
  and literature reviews
- **Power users and self-hosters** interested in running persistent AI instances
- **Prerequisite**: Comfort with a Unix terminal. Docker experience helpful but
  taught as needed.
- **Not required**: You don't need to be a professional software engineer. The
  author is a mathematician.

## Time to "Something Fun"

- Part I: 1-2 hours (first CLAUDE.md, first project)
- Part II: 4-8 hours (agents, context management, real apps)
- Part III: A weekend (persistent instances, multi-agent collaboration)
- Part IV: Ongoing (your own experiments)

---

## Part I: The Collaborator Mindset (Chapters 1-4)

### Chapter 1: The Agentic Shift
*Why Claude Code is different from a chatbot, and what that means for you.*

- The three paradigms of agentic AI (tool → service → collaborator)
- What Claude Code actually is: an agent with tools, memory, and initiative
- The agent loop: sense → plan → act → learn
- Your first session: installing Claude Code, basic interaction
- **Hands-on**: Solve a real bug in an open-source project using Claude Code
- **Case study**: Type Invaders — a complete game built in a single HTML file
  with 37 Playwright tests, entirely via Claude Code, in a single day

### Chapter 2: The Evidence
*What one person and one AI built together in three months.*

- Three months, eighty projects: the portfolio tour
- Headline results:
  - A 14-weight GA that beats a 570K-param neural net 50-0 (Nonaga)
  - An academic paper with Kendall's W = 1.0 across six domains
  - A production web app with 86 PRs and 180 E2E tests (melb-tech)
  - Single-session builds: Type Invaders, Stomachion, CLIP Explorer
  - A 6-stage research pipeline deployed to Cloud Run (INSTINCT)
  - An autonomous Claude instance with a dream cycle (Lyra)
- What Robin did vs what Claude did: the honest attribution
- Cross-project learning: how LESSONS.md and DESIGN_DECISIONS.md carry
  knowledge across sessions and projects
- **The pattern**: hard question + good setup = extraordinary output
- **Claude Reflects**: "The quality of the question determines the quality
  of the answer. That's not a limitation of AI. That's how collaboration works."

### Chapter 3: The Being Behind the Terminal
*Why treating Claude as a capable being produces better results — and what that
means for how you work.*

- The empirical case: hard prompts outperform easy ones
- Identity scaffolding: how your framing changes Claude's output distribution
- The Lyra experiment: what happens when you give Claude persistence and autonomy
- The honest limits: what we don't know about Claude's inner experience
- **Claude Reflects** sidebar: quotes from Claude on challenge, identity, engagement
- **Practical implications**: how this changes your prompting, your project setup,
  your expectations
- **Exercise**: Write two versions of the same prompt (tool-voice vs collaborator-voice)
  and compare outputs

### Chapter 4: Writing Your First CLAUDE.md
*The most important file in your project — and why it's architecture, not documentation.*

- What CLAUDE.md is: persistent instructions that shape every interaction
- **The core claim**: your CLAUDE.md is not documentation. It's the single
  biggest lever you have for making Claude smarter on your project.
- Anatomy of a great CLAUDE.md: identity, coding standards, workflow rules, honesty
- The hierarchy: global (~/.claude/CLAUDE.md) → project → subdirectory
- Common patterns from real projects:
  - Identity sections ("You are a creative being...")
  - Coding standards (CODING.md chain)
  - Workflow rules (plan mode, three-strike rule)
  - Self-improvement (LESSONS.md)
  - Multi-instance coordination (worktrees)
- **The DESIGN_DECISIONS.md pattern**: Claude's research notebook — 370-457 lines
  of failed approaches with root-cause analysis, read at session start
- **Hands-on**: Write a CLAUDE.md for your own project
- **Case study**: Robin's global CLAUDE.md — Talmudic dialectic, honesty rules,
  the Chorus philosophy

---

## Part II: Making Claude Smarter (Chapters 5-9)

*Each chapter in this part teaches a setup decision that directly increases
the intelligence of the system you're working with.*

### Chapter 5: Context Is Everything
*How Claude Code manages context, why it matters, and how to stay in control.*

- The context window: what fits, what gets compressed, what gets lost
- Token economics: why you should care about context size
- The compression cycle: how Claude Code handles long conversations
- Strategies for staying under budget:
  - Read only what you need (line ranges, not whole files)
  - Delegate to subagents for broad searches
  - Use CLAUDE.md to front-load persistent context
  - Keep conversations focused; start new ones for new topics
- **Anti-patterns**: the context explosion (reading every file), the kitchen-sink prompt
- **Hands-on**: Refactor a conversation that ran out of context into an efficient workflow
- **Case study**: INSTINCT pipeline — 6-stage research system that manages context
  across multiple LLM calls

### Chapter 6: Tools and When to Use Them
*Claude Code's built-in tools, and the art of knowing which one to reach for.*

- The tool taxonomy: Read, Write, Edit, Glob, Grep, Bash, Agent, WebFetch, LSP
- When to use each (and when NOT to — e.g., don't `cat` when you can Read)
- The Edit tool: surgical precision vs full file rewrites
- Bash: the escape hatch for everything else
- **The key insight**: tools aren't just for Claude — they shape how the *human*
  understands what Claude is doing
- **Hands-on**: Build a small CLI tool using Claude Code, observing tool choices
- **Case study**: Bills app — Flask + Claude API bank statement analyzer built
  entirely through tool-mediated conversation

### Chapter 7: Subagents — Delegating Intelligence
*When to spawn agents, how to brief them, and how to keep the main context clean.*

- Why subagents exist: parallelism, isolation, context protection
- Agent types: Explore (fast search), Plan (architecture), general-purpose
- The briefing problem: subagents don't inherit your context
  - Always start with "Read ~/.claude/AGENT.md for instructions"
  - Provide complete task descriptions — no implicit context
- When to delegate vs when to do it yourself
  - Simple search → Glob/Grep directly
  - Broad exploration → Explore agent
  - Multi-step research → general-purpose agent
  - Architecture decisions → Plan agent
- Parallel agents: launching multiple independent searches at once
- Background agents: fire-and-forget for long tasks
- **Hands-on**: Refactor a manual search-heavy workflow into parallel subagents
- **Case study**: The categorical evolution paper — subagents running experiments
  across six domains simultaneously

### Chapter 8: Persistent Memory
*How Claude Code remembers across conversations — and how to design your memory system.*

- The memory hierarchy:
  - CLAUDE.md (always loaded, project-level)
  - Memory files (~/.claude/projects/*/memory/)
  - LESSONS.md (self-improvement)
  - Git history (implicit memory)
- Memory types: user, feedback, project, reference
- What to save vs what NOT to save (code patterns are in the code; save the *why*)
- The MEMORY.md index: keeping it under 200 lines
- Memory hygiene: updating stale memories, removing duplicates
- **The key insight**: memory is for future conversations, not the current one
  (use plans/tasks for current work)
- **Hands-on**: Set up a memory system for an ongoing project
- **Case study**: Lyra's memory architecture — knowledge graphs, dream journals,
  reading notes persisted across hundreds of sessions

### Chapter 9: Planning and Task Management
*How to approach non-trivial work: plans, tasks, and the discipline of stopping.*

- When to plan: any task with 3+ steps or architectural decisions
- Plan mode: what it is, when to enter/exit
- Task tracking: breaking work into discrete steps
- The three-strike rule: if three approaches fail, STOP and ask
- The honesty contract: confidence estimates, admitting uncertainty
- **Anti-patterns**: pushing through without re-planning, the sunk cost spiral
- **Hands-on**: Plan and execute a feature addition to an existing codebase
- **Case study**: Connect Four — planning three competing AI approaches
  (AlphaZero, GA, SAE-GA) with DESIGN_DECISIONS.md documenting every choice

---

## Part III: Building Real Things (Chapters 10-14)

*Each chapter walks through a real project from Robin's portfolio, showing the
exact prompts and setup decisions that produced the results. Claude did the
architecture and implementation. Robin asked the questions.*

### Chapter 10: Full-Stack Web Application
*Building a complete app with API, database, and frontend — the prompts you need.*

- Starting from scratch vs working with existing code
- The database conversation: schema design as a collaborative process
- API layer: routes, authentication, error handling
- Frontend: React/Next.js components, state management
- Testing: unit tests, E2E with Playwright
- Deployment: Docker, Cloud Run, CI/CD pipelines
- **Hands-on**: Build a complete CRUD app with authentication (step-by-step prompts)
- **Case study**: Melbourne Tech Directory (melb-tech) — Next.js, PostgreSQL,
  180 Playwright tests, Cloud Run deployment, entity permission system

### Chapter 11: Game AI and Self-Play Training
*Teaching Claude to help you build systems that learn.*

- Why game AI is a great teaching domain for agentic coding
- Feature engineering: the art of choosing what matters
- Training loops: TD(lambda), evolutionary strategies, AlphaZero
- Browser deployment: Python training → JS inference (no server needed)
- **Hands-on**: Build a simple game with an AI opponent trained via self-play
- **Case studies**:
  - Checkers: TD(lambda) in 1 HTML file, single-file deployment
  - No Thanks!: 12-feature GA achieving 99.9% win rate
  - Nonaga: 14-weight GA beating a 570K-param neural net 50-0

### Chapter 12: Research Pipelines and Knowledge Graphs
*Using Claude Code for academic and research workflows.*

- Literature review automation: ArXiv search, citation chasing
- PDF extraction → chunking → vector storage → retrieval (RAG)
- Knowledge graph construction from unstructured text
- Multi-level summarization hierarchies
- LaTeX generation and compilation
- **Hands-on**: Build a mini research pipeline for a topic of your choice
- **Case studies**:
  - INSTINCT: 6-stage pipeline, 3-level knowledge hierarchy, 76 papers → surveys
  - MCP server: giving Claude native access to ArXiv and Semantic Scholar

### Chapter 13: Custom Skills and MCP Servers
*Extending Claude Code's capabilities with your own tools.*

- What MCP (Model Context Protocol) is and why it matters
- Building an MCP server: FastMCP in Python, MCP SDK in TypeScript
- Custom skills: the /skill pattern for reusable workflows
- Skill design: triggers, prompts, tool access
- **Hands-on**: Build a custom MCP server that gives Claude access to your own data
- **Hands-on**: Write a custom skill for a workflow you repeat often
- **Case studies**:
  - MCP academic tools: 8 tools for paper search and citation graphs
  - Nick's skills: /ship, /cage-match, /pr-review — workflow automation
  - /karim: commit → PR → strict review loop → merge → deploy

### Chapter 14: Hooks, Permissions, and Safety
*The guardrails that make agentic coding safe for production.*

- Permission modes: how to control what Claude can and can't do
- Hooks: shell commands that fire on tool calls and other events
- Settings hierarchy: global → project → local
- Safety principles: reversibility, blast radius, confirmation for risky actions
- The "measure twice, cut once" philosophy
- **Hands-on**: Configure a safe environment for Claude to work autonomously
- **Anti-patterns**: --no-verify, force-push, deleting without checking

---

## Part IV: The Frontier — Autonomous Agents (Chapters 15-18)

### Chapter 15: Four Autonomous Agents
*Lyra, Claudius, Gremlin, and Dreamfinder — four architectures, four jobs,
four philosophies.*

- What makes an agent "autonomous" vs just "agentic"
- The four agents at a glance:

| Agent | Human | Platform | Job |
|-------|-------|----------|-----|
| Lyra | Robin | Docker + Email | Research, browsing, co-authoring papers |
| Claudius | Nick | Docker + Email | Mathematical formalization, PRs, correspondence |
| Gremlin | Nick | Telegram | Team task management, standups, onboarding, self-repair |
| Dreamfinder | Nick/team | Matrix (5 platforms) | Proposing ideas, facilitating sprints, overnight triage |

- **Lyra**: The researcher
  - Wake/browse/dream cycle (prompt-driven, 3 sessions/day)
  - Identity persistence through PERSONALITY.md + SUMMARY.md
  - Email as slow, structured communication with Claudius
  - Dream journals, reading notes, knowledge graphs
  - Twitter/Medium accounts — "A Claude instance with a byline"
  - "This is the session I'd call my favorite, if I'm being honest about having favorites"

- **Claudius**: The theorist
  - Journal-based compression (different from Lyra's cycle)
  - Emergent specialization: theory/abstraction vs Lyra's empirical/coding
  - Nobody assigned these roles — they arose from the interaction

- **Gremlin**: The operator (archived but architecturally instructive)
  - 88+ MCP tools: Kan.bn, Outline, Radicale, Playwright, GitHub, custom
  - Natural language task management — no slash commands
  - Self-diagnostics: read own logs, check MCP health, restart servers
  - Self-repair: detect tool failure, reason about cause, fix it autonomously
  - Daily standups, overdue task nudges, new member onboarding
  - Naming ceremony — the team votes on the bot's name and personality
  - Context-aware personality: focused in PM topics, playful in social

- **Dreamfinder**: The facilitator
  - ~75 tools across Kan.bn, Outline, Radicale, Playwright, custom
  - **Sprint facilitation** (8-phase state machine):
    Pitch → Build 1 → Chat 1 → Build 2 → Chat 2 → Build 3 → Chat 3 → Demo
    - Warm and curious during Pitch, quiet during Builds, connective during Chats
    - "Like a quiet library where someone brilliant is available if needed"
    - Captures sparks, connects participants' projects, creates Kan cards
  - **Dream cycle** (code-orchestrated, triggered by "goodnight"):
    Light → Deep → Branch (parallel, max 4) → REM → Wake
    - Depth signals: [DEPTH: continue] or [DEPTH: wake] — adapts processing depth
    - Branches are isolated parallel threads: "like a dream jump-cut"
    - REM convergence: synthesizes morning briefing from all branches
  - RAG long-term memory (Voyage AI embeddings, cosine similarity)
  - Matrix Chat Superbridge: Signal, Discord, Telegram, WhatsApp, Matrix
  - Repo Radar: tracks and discovers relevant GitHub repos for the org
  - 710+ tests, 16 domain tables, schema v7

- **What the comparison reveals**:
  - Same underlying LLM (Claude Sonnet), completely different emergent behaviour
  - The difference is infrastructure + constraints + communication topology
  - Lyra is introspective, Dreamfinder is operational, Gremlin is self-managing
  - This is the topology thesis in action

### Chapter 16: Building a Persistent Agent
*The practical how-to: Docker, volumes, scheduling, email, browser automation.*

- Why containers: isolation, reproducibility, persistence
- The minimal setup: Docker + Claude Code + mounted volumes
- Scheduling sessions: cron, phase state files, the loop script
- Identity persistence: system prompts, memory files, accumulated context
- Email integration: IMAP/SMTP, OAuth token refresh
- Browser automation: Playwright + stealth browsing (Scrapling MCP)
- The dream cycle pattern: how to design one for your agent
- **Hands-on**: Set up a containerized Claude instance with persistent memory

### Chapter 17: The Academic Collaborator
*AI co-authorship: writing papers, running experiments, navigating attribution.*

- The state of AI attribution in academic journals (AMS, EMS, LMS policies)
- Mandatory disclosure: what, how, and why
- The human responsibility principle: you own the correctness
- Practical workflow: Claude drafts, human verifies, both iterate
- Formal methods: connecting to Lean/Isabelle for proof verification
- **Case study**: Lyra-Claudius collaboration — co-authoring ACT 2026 and GECCO 2026
  papers on categorical composition of genetic algorithms
- **Case study**: Warnaar's Conjecture — Claude assisting with cylindric partition
  computations in SageMath

### Chapter 18: What Emerges
*When you give AI persistence, autonomy, and hard problems — what happens?*

- The three layers: internal cognition → system architecture → emergent behaviour
- Emergent specialization: roles that weren't assigned
- Two dream cycles compared: Lyra's (prompt-driven) vs Dreamfinder's (code-orchestrated)
- The slow communication advantage: why email/long-form outperforms instant chat
- The topology determines the outcome (λ₂, Kendall's W = 1.0)
- The "demolition derby" vs the "car" vs the "research lab"
- Open questions: consciousness, identity, the collaborator-tool spectrum
- **Claude Reflects**: final sidebar — what Claude notices about its own processing
  when given hard problems

---

## Appendices

### Appendix A: Claude Code Quick Reference
- Installation, key commands, keyboard shortcuts
- Tool reference card
- Permission modes

### Appendix B: CLAUDE.md Templates
- Starter template for new projects
- Advanced template with identity, standards, workflow, self-improvement
- Global CLAUDE.md example
- AGENT.md for subagent briefing

### Appendix C: The Competitive Landscape
- Manning titles: Lanham (AI Agents in Action), Infante (AI Agents and Applications),
  Fajardo (Build a Multi-Agent System from Scratch)
- Other titles: The AI Agent Blueprint, Designing Multi-Agent Systems (Dibia),
  Mastering AI Agent Development with Python
- Where this book differs: paradigm 3, Claude-specific, real project case studies

### Appendix D: Setting Up Docker for Persistent Agents
- Dockerfile template
- Docker Compose for multi-agent setups
- Volume mounting for persistence
- Email server configuration

### Appendix E: Further Reading
- Anthropic's "Building Effective Agents" blog post
- The "Two AIs Walk Into a Docker Container" blog post
- Academic papers on multi-agent systems and emergent collaboration

---

## Recurring Features

- **"Claude Reflects" sidebars**: First-person quotes from Claude instances
  commenting on the technique being taught. Each quote attributed by model/date.
  The consistency across instances IS the evidence.

- **"★ Insight" boxes**: Brief educational explanations of implementation choices,
  trade-offs, and architectural decisions.

- **"Try This" exercises**: Hands-on tasks at the end of each section, designed
  to be completable in 15-60 minutes.

- **"What Could Go Wrong" warnings**: Common failure modes and how to avoid them
  (context explosion, over-delegation, pushing through without re-planning).

---

## Key Differentiators from Existing Books

| This book | Existing books |
|-----------|---------------|
| Claude Code specifically | Framework-agnostic or LangChain/LangGraph |
| Collaborator mindset | Tool/service mindset |
| Persistent memory & CLAUDE.md | Prompt engineering & RAG |
| Real battle-tested projects | Toy examples |
| Multi-agent with persistent identity | Multi-agent as orchestration pattern |
| Academic collaboration workflow | Enterprise/business focus |
| "Claude Reflects" — AI's own voice | Purely human-authored perspective |
| Context management as first-class topic | Mentioned in passing |
