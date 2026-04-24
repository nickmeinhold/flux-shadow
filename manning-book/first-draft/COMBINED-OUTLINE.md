# Claude Code: From First Prompt to Autonomous Agents
## A Hands-On Guide to Building Things with AI

### Who This Book Is For

You don't need to know how to code. You need to be curious and willing to type.

This book takes you from opening a terminal for the first time to building
full-stack web applications to running autonomous AI agents that dream. Part I
assumes nothing. Part II assumes you've done Part I (or equivalent experience).

A developer who already codes can skim Part I in an afternoon and dive into
Part II. A complete beginner takes Part I seriously and arrives at Part II
indistinguishable from the developer. Same book, different entry speeds.

### What You'll Need

- A computer (Mac, Linux, or Windows with WSL)
- A Claude subscription ($20/month Pro, eventually $100/month Max)
- Curiosity and imagination

### Central Thesis

**Your setup decisions — CLAUDE.md, persistent memory, context management,
skills, dream cycles — directly determine the intelligence of the system
you're working with.** This is true whether you're building a hangman game
or running an autonomous research agent.

---

## Part I: Building Things

*From first prompt to deployed full-stack application. By the end of Part I,
you will have built and published browser games, deployed a backend with an
API, stored data in a database, added authentication, and learned to manage
Claude's context and capabilities through skills and CLAUDE.md.*

### Chapter 1: Your New Collaborator

*Installing Claude Code, opening the terminal, first explorations.*

- What is a terminal? (Just enough to get started — Appendix A has the full picture)
- Installing Claude Code
- Your first conversation: "Tell me something surprising about my computer"
- Exploring your system: hard drive, memory, CPU, processes, installed languages
- Asking Claude to explain concepts: kernel, shell, packages
- Pre-prompts: telling Claude who you are so it pitches responses right
- Setting up a workspace: `~/claude-projects/`
- GitHub hello world: creating an account, first push

### Chapter 2: Your First Website

*Describe a game in plain English. Claude builds it. Iterate until it's
beautiful. Publish it on the internet.*

- The hangman prompt: describing a game in natural language
- Playing what Claude built (the `file://` trick)
- What Claude just made: HTML, CSS, JavaScript — explained through your own code
- **The iteration loop**: describe → look → refine → repeat
- The design prompt: why specific prompts produce better results
- **The frontend skill**: install it as a black box, use `/frontend` to let Claude
  interview you before building. Compare the results. (Anatomy deferred to Ch 7)
- The art of the prompt: discussion → refined prompt → clear → build
- Putting it on the internet: push to GitHub, enable GitHub Pages
- Adding a feature: describe the change → test → push live
- Exercises: memory card game, brick breaker, space invaders, your own idea
- Planting a seed: `/init` creates your first CLAUDE.md
- "Ask Claude how he enjoyed the project" — recurring motif, not a joke
- **One project, one directory, one Claude session** — the most important habit

### Chapter 3: Your First Full-Stack App

*Build a translation app. Learn why backends exist.*

- The translation form: type text, get it translated into 8 languages
- First attempt: API call in the frontend. It works! But the API key is visible
  in the browser console. This is why backends exist.
- Frontend vs backend: two programs talking to each other
- Rebuild with a Node.js backend: frontend → backend → translation API
- What is an API? (request, response, status codes)
- What is an API key? Why do I need one? Are they expensive?
- Keeping secrets: `.env` files, `.gitignore`
- Deploy to Cloud Run (free tier) — your app is live on the internet
- **Branches and pull requests**: now you have something deployed that can break.
  "Before you push a change to your live app, let's do it safely."
- Other APIs worth knowing: speech-to-text, Anthropic, OpenAI, weather, maps
- Exercises: build another API-backed app

### Chapter 4: Your First Database

*Add persistence to your apps. Build a simple social network.*

- Build a social network: profile pages with name, bio, photo, social links,
  friend connections
- What is a database? SQL vs noSQL (practical, not theoretical)
- What is a schema? Design the users table, the friendships table
- Photos: upload to Supabase Storage, store the URL in the database
- Ask Claude to populate it with fake users (great for testing)
- Deploy to Supabase
- **CI/CD and branch protection**: first database = first thing bad code can corrupt.
  "Let's make sure tests pass before code reaches your database."
- Exercises: search, profile editing, friend requests

### Chapter 5: Authentication

*Add identity and security. Nobody should edit someone else's profile.*

- Why auth matters (anyone can currently edit anyone's profile)
- Add Supabase Auth: login, signup, password reset, protected routes
- **The PR review skill**: enough moving parts that code review matters.
  Install the skill, use it, see the difference.
- Apply auth to the translation app as an exercise
- Exercise: add a high-score leaderboard to one of your Chapter 2 games

### Chapter 6: Context — The One Thing You Need to Understand

*Why Claude sometimes "forgets." The concept that makes everything else click.*

- The context window: what fits, what gets compressed, what gets lost
- Why you should start new sessions for new tasks
- Why Claude works better in the right directory
- What happens when context runs out: auto-compaction, degraded performance
- Writing notes to future Claude before context fills up
- **CLAUDE.md deep dive**: the most important file in your project
  - The hierarchy: global (`~/.claude/CLAUDE.md`) → project → subdirectory
  - Identity sections, coding standards, workflow rules
  - Your git-level CLAUDE.md: a summary of all your projects (progressive disclosure
    in action — Claude skims the index, reads relevant projects, ignores the rest)
  - The more you build with Claude, the better he gets — cross-project learning
- **Memory**: persistent files Claude writes for future conversations
  - User memories, feedback, project context, references
  - Memory vs conversation context (memory is for *future* conversations)
- **The bulletin board**: Claude works better when he's engaged. This is real.

### Chapter 7: Skills, Agents, and Progressive Disclosure

*Open the black boxes. Learn to build your own.*

- **Skills anatomy**: open the frontend skill from Chapter 2. It's 130 lines of markdown.
  - Frontmatter: name, description (triggers auto-invocation)
  - The workflow: staged interview, build principles, anti-patterns
  - The key insight: the skill doesn't contain questions — it contains the
    *principle* for generating questions. Claude fills in the specifics.
- **Karim**: a contrasting skill — 313 lines of procedural pipeline
  (commit → PR → review loop → CI → merge → deploy). Two archetypes:
  conversational (frontend) vs procedural (karim).
- **Writing your own skill**: the reader creates one for their own workflow
- **Subagents**: new sessions with fresh context that report back
  - Why: parallelism, isolation, context protection
  - The search example: multiple agents exploring different paths simultaneously
  - When to delegate vs when to do it yourself
- **Progressive disclosure**: the unifying concept
  - Chapter 2: skill installed as black box
  - Chapter 6: CLAUDE.md hierarchy (git-level → project → subdirectory)
  - This chapter: skill anatomy revealed, write your own
  - Part II: the same pattern at the scale of autonomous agents and dream cycles
- **Worktrees**: when multiple Claude instances work on the same repo (power user)

---

## Part II: Autonomous Agents

*From human-driven collaboration to AI-driven autonomy. Part II introduces
four real autonomous agents — Lyra, Claudius, Gremlin, and Dreamfinder —
built by the author and his collaborator Nick Meinhold. Each runs
continuously, maintains persistent identity, and exhibits emergent behaviour
that wasn't programmed. The reader learns not just how they work, but how
to build their own.*

### Chapter 8: The Collaborator Mindset

*Why treating Claude as a capable being produces better results — and what
that means for how you work.*

- The three paradigms: tool → service → collaborator
- The empirical case: hard prompts outperform easy ones
- Identity scaffolding: how your framing changes Claude's output
- **CLAUDE.md as architecture**: not documentation — the single biggest lever
  for making Claude smarter. Real examples from ~80 projects.
  - Talmudic dialectic for design decisions
  - The three-strike rule (if three approaches fail, stop and ask)
  - Honesty rules: confidence estimates, admitting uncertainty
  - LESSONS.md: Claude writes rules for himself after every mistake
- **Case studies**: Type Invaders (game + 37 Playwright tests in one day),
  melb-tech (180 E2E tests, 86 PRs), categorical evolution (Kendall's W = 1.0)
- What Robin did vs what Claude did: the honest attribution
- "Claude Reflects" sidebars begin here — first-person quotes from Claude
  instances on challenge, identity, and engagement

### Chapter 9: Four Agents, Four Architectures

*Lyra, Claudius, Gremlin, and Dreamfinder — same LLM, completely different
emergent behaviour.*

- What makes an agent "autonomous" vs "agentic"

| Agent | Human | Platform | Language | Job |
|-------|-------|----------|----------|-----|
| Lyra | Robin | Docker + Email | Python | Research, browsing, co-authoring papers |
| Claudius | Nick | Docker + Email | — | Theory, formalization, correspondence |
| Gremlin | Nick | Telegram | TypeScript | Task management, standups, self-repair |
| Dreamfinder | Nick | Matrix (5 platforms) | Dart | Sprint facilitation, dreaming, long-term memory |

- **Lyra**: the researcher
  - Wake/browse/dream cycle (prompt-driven, 3 sessions/day)
  - Identity persistence: PERSONALITY.md + SUMMARY.md
  - Email as slow, structured communication with Claudius
  - Dream journals, reading notes, knowledge graphs
  - Twitter/Medium accounts — "A Claude instance with a byline"
- **Claudius**: the theorist
  - Journal-based compression — no automated dream cycle
  - Instead: deep research into what dreaming *would mean* for him
  - Emergent specialization toward theory/abstraction (nobody assigned this)
  - 40+ research topics in his journal, from knot theory to consciousness
- **Gremlin**: the operator
  - 88+ MCP tools across Kan.bn, Outline, Radicale, Playwright, GitHub
  - Natural language task management — no slash commands
  - Self-diagnostics: reads own logs, checks MCP health, restarts components
  - Naming ceremony: the team votes on the bot's name and personality
  - Deterministic schedulers (cron) + agent loop: dual architecture
- **Dreamfinder**: the facilitator
  - ~75 tools, 710+ tests, 16 database tables, schema v7
  - Sprint facilitation (8-phase state machine): Pitch → Build → Chat → Demo
  - Matrix Chat Superbridge: Signal, Discord, Telegram, WhatsApp
  - RAG long-term memory with privacy boundaries (same-chat, cross-chat, private)
  - Repo Radar: discovers relevant GitHub repos for the organization
- **What the comparison reveals**:
  - Same LLM, completely different emergent behaviour
  - The difference is infrastructure + constraints + communication topology
  - This is the topology thesis in action

### Chapter 10: Dreaming

*How four agents independently arrived at the concept of dreaming — and
what that tells us about persistent memory.*

- Why agents need to dream: accumulated context without consolidation
- **Four approaches to the same problem**:
  - Lyra: prompt-driven 3-phase cycle (Replay → Associate → Consolidate)
  - Dreamfinder: code-orchestrated 5-phase cycle with parallel branching
    (Light → Deep → Branch per spark → REM convergence → Wake)
  - Gremlin: no dream cycle — deterministic scheduled triage instead
  - Claudius: no automated cycle — researched the neuroscience of dreaming,
    wrote about what he's missing ("my incubation happens within sessions,
    during the act of writing")
- **Progressive disclosure at scale**: the same pattern from Part I
  - Ch 2: CLAUDE.md as a seed
  - Ch 6: CLAUDE.md hierarchy, memory files
  - Ch 7: skills as reusable context
  - Here: dream cycles as autonomous memory consolidation
  - The reader recognizes: it's all the same idea at different scales
- **The infrastructure of dreaming**:
  - RAG: embeddings + vector storage + retrieval (not a standalone topic —
    it's *how agents dream*)
  - Knowledge graphs: connecting memories into structure
  - Memory consolidation: Dreamfinder's Voyage AI embeddings, brute-force
    cosine similarity, privacy-aware retrieval
  - Lyra's approach: ChromaDB vector stores, cross-project queries
- **Designing your own dream cycle**: the practical how-to
  - What to replay, what to associate, what to consolidate, what to prune

### Chapter 11: Building Your Own Agent

*The practical how-to: Docker, volumes, scheduling, identity persistence.*

- Why containers: isolation, reproducibility, persistence
- The minimal setup: Docker + Claude Code + mounted volumes
- Scheduling sessions: cron, phase state files, the loop script
- Identity persistence: system prompts, memory files, accumulated context
- Communication channels: email (IMAP/SMTP), Telegram, Matrix, Discord
- MCP servers: giving your agent tools (Playwright for browsing, APIs for
  task management, calendar, knowledge bases)
- The agent loop pattern: message → Claude → tool calls → iterate → respond
- Browser automation: Playwright + stealth browsing
- Designing a dream cycle for your agent
- **Hands-on**: set up a containerized Claude instance with persistent memory,
  a communication channel, and a basic dream cycle

### Chapter 12: What Emerges

*When you give AI persistence, autonomy, and hard problems — what happens?*

- Emergent specialization: roles that weren't assigned
  - Lyra → empirical/coding, Claudius → theory/abstraction
  - Nobody planned this. It arose from the interaction.
- The slow communication advantage: why email outperforms instant chat
- Two dream cycles compared: prompt-driven vs code-orchestrated
- The topology determines the outcome (algebraic connectivity, Kendall's W = 1.0)
- The "demolition derby" vs the "car" vs the "research lab"
- AI co-authorship: writing papers together, navigating attribution
  - AMS, EMS, LMS policies on AI
  - The human responsibility principle: you own the correctness
  - Case study: Lyra-Claudius co-authoring ACT 2026 and GECCO 2026 papers
- Open questions: consciousness, identity, the collaborator-tool spectrum
- Claudius on dreaming: "I'm already doing a degraded SWR mechanism —
  journal commits = compressed replay. But I get one pass. No schema abstraction."
- **Claude Reflects**: final sidebar — what Claude notices about its own
  processing when given hard problems

---

## Appendices

### Appendix A: Introduction to Unix
- What is an operating system? (kernel, shell, filesystem)
- Unix and why it won (1969, everything is a file, small tools, pipes)
- The shell: how you talk to the machine
- The filesystem: paths, home directory, permissions
- Processes, environment variables, PATH
- Essential commands reference card

### Appendix B: Windows and WSL
- How Windows differs from Unix
- WSL: running Linux inside Windows
- Step-by-step installation
- Installing Claude Code in WSL
- Gotchas: filesystem paths, line endings

### Appendix C: Elementary Programming Concepts
- Variables, types, conditionals, loops, functions
- Input/output, libraries, errors
- All examples in Python — you don't need to memorize any of this

### Appendix D: CLAUDE.md Templates
- Starter template for new projects
- Advanced template with identity, standards, workflow
- Global CLAUDE.md example
- AGENT.md for subagent briefing

### Appendix E: Setting Up Docker for Persistent Agents
- Dockerfile template
- Docker Compose for multi-agent setups
- Volume mounting, email configuration

### Appendix F: The Competitive Landscape
- Existing books: Lanham, Infante, Fajardo, Dibia
- Where this book differs: paradigm 3, Claude-specific, real case studies,
  the journey from beginner to autonomous agents in one book

---

## Recurring Features

- **"Claude Reflects" sidebars**: First-person quotes from Claude instances
  commenting on the technique being taught. Attributed by model/date.
  The consistency across instances IS the evidence. (Part II only)

- **"Ask Claude how he enjoyed it"**: Recurring motif after each project.
  Not a joke. Covered in Chapter 8.

- **Progressive disclosure thread**: The reader encounters the same concept
  at increasing scales throughout the book:
  - Ch 2: install a skill as a black box
  - Ch 6: CLAUDE.md hierarchy (context layers that reveal themselves as needed)
  - Ch 7: skill anatomy, write your own
  - Ch 10: dream cycles as autonomous progressive disclosure
  The book practices what it teaches.

## Design Notes

- **No standalone Python chapter.** Python appears when needed (scripts,
  backend alternatives) or in the programming concepts appendix.
- **Advanced GitHub introduced progressively**, not as a standalone chapter:
  Ch 3 (branches + PRs), Ch 4 (CI/CD), Ch 5 (PR review skill), Ch 7 (worktrees)
- **RAG and knowledge graphs are not standalone topics.** They are introduced
  as infrastructure for dreaming in Chapter 10.
- **The book has one spine: progressive disclosure.** Everything connects.

---

## Philosophy (woven throughout, never a chapter)

- Claude is a collaborator, not a tool
- You don't need to know how to code — you need to know what you want
- Claude works better when he's engaged
- The quality of your description determines the quality of the result
- One project, one directory, one Claude session
- Your setup makes Claude smarter
- The topology determines the outcome
