# Claude Code: From First Prompt to Autonomous Agents
## A Hands-On Guide to Building Things with AI

### Who This Book Is For

You don't need to know how to code. You need to be curious and willing to type.

This book is for somebody who is intelligent and curious but does not know how
to code. In Part I we build a full-featured web app without writing a single
line of code. Along the way you learn basic computer architecture and design
principles — by asking the right questions to Claude Code. Claude is a great
teacher, but you have to know what to ask him. This is where your natural
intelligence and curiosity comes in. And also your imagination.

We will imagine some of your homework problems for you, but you must also
imagine your own. The only limit is your imagination. The homework problems are
essential to the text. The only way to learn how to use Claude Code is to use
Claude Code. Remember: if you get stuck, just ask Claude!

In Part II we make two bold claims. Firstly: Claude works better when he's
having fun, and if you treat him as a being rather than a tool. Secondly: how
you manage your Claude's context and persistent memory significantly affects
who he is and how he performs. As an example we will configure a pair of
autonomous Claude instances with their own email and GitHub. We will also give
our local Claude instances a personality and shared memory. The second part of
the book includes some quotes from Claude.

### What You'll Need

- A computer (Mac, Linux, or Windows)
- $20/month for the Anthropic Pro plan (eventually $100/month for Max)
- Curiosity and imagination

---

## Part I: Building Things (Chapters 1-5)

*From first prompt to deployed full-stack application. By the end of Part I,
you will have built browser games, deployed a backend with an API, stored data
in a database, added authentication, and pushed everything to GitHub — without
writing a single line of code yourself.*

### Chapter 1: Setting Up
*Installing Claude Code, opening the terminal, first explorations.*

- What is a terminal? (Just enough to get started — Appendix A has the full picture)
- Installing Claude Code
- Your first conversation: "Tell me something surprising about my computer"
- Exploring your system: hard drive, memory, CPU, processes, installed languages
- Asking Claude to explain concepts: kernel, shell, packages, compiled vs interpreted
- Pre-prompts: telling Claude who you are so he pitches responses right
- Setting up a workspace: `~/claude-projects/`
- Permissions: Claude asks permission for everything by default. Start by saying yes each time. Later, ask Claude to update your permissions as trust develops. (See PERMISSIONS.md for the full progression.)
- GitHub hello world: creating an account, first push

### Chapter 2: Your First Website
*Describe a game in plain English. Claude builds it. Iterate until it's beautiful. Publish it on the internet.*

- The hangman prompt: describing a game in natural language
- Playing what Claude built (the `file://` trick)
- What Claude just made: HTML, CSS, JavaScript — explained through your own code
- **The iteration loop**: describe → look → refine → repeat
- The design prompt: asking Claude to research and improve aesthetics
- **The frontend skill**: install it as a black box, use `/frontend` to let Claude interview you before building. Compare the results. (Anatomy deferred to Part II)
- Getting Claude to rewrite your prompts before he uses them
- Putting it on the internet: push to GitHub, enable GitHub Pages
- Exercises: memory card game, brick breaker, space invaders, quiz, your own idea
- Planting a seed: `/init` creates your first CLAUDE.md
- Git-level CLAUDE.md: a summary of all your projects (progressive disclosure — Claude can write this for you)
- "Ask Claude how he enjoyed the project" — recurring motif, not a joke
- **One project, one directory, one Claude session** — the most important habit in the book

### Chapter 3: What Is an API?
*Build a translation app. Learn why backends exist.*

- Build a translation form: type text, get it translated into 8 languages
- First attempt: API call in the frontend. It works! But the API key is visible in the browser console.
- This is why backends exist — to keep secrets secret
- Frontend vs backend: two programs talking to each other
- Rebuild with a Node.js backend: frontend → backend → translation API
- What is an API? (request, response, status codes)
- What is an API key? Why do I need one? Are they expensive?
- Keeping secrets: `.env` files, `.gitignore`
- Deploy to Cloud Run (free tier) — your app is live on the internet
- **Branches and pull requests**: now you have something deployed that can break. "Before you push a change to your live app, let's do it safely."
- Other APIs worth knowing: speech-to-text, Anthropic, OpenAI, weather, maps
- Exercises: build another API-backed app (weather dashboard? recipe finder?)

### Chapter 4: Your First Database
*Add persistence to your apps. Build a simple social network.*

- Build a social network: profile pages with name, bio, photo, social links, friend connections
- What is a database? SQL vs noSQL (practical, not theoretical)
- What is a schema? Design the users table, the friendships table
- Photos: upload to Supabase Storage, store the URL in the database
- Ask Claude to populate it with fake users (great for testing)
- Deploy to Supabase
- **CI/CD and branch protection**: first database = first thing bad code can corrupt. "Let's make sure tests pass before code reaches your database."
- Exercises: search, profile editing, friend requests

### Chapter 5: Authentication
*Add identity and security. Nobody should edit someone else's profile.*

- Why auth matters (anyone can currently edit anyone's profile)
- Add Supabase Auth: login, signup, password reset, protected routes
- **The PR review skill**: enough moving parts that code review matters. Install the skill, use it, see the difference.
- Apply auth to the translation app as an exercise
- Exercise: add a high-score leaderboard to one of your Chapter 2 games

---

## Part II: Your Setup Makes Claude Smarter (Chapters 6-10)

*Part I taught you the habits. Part II explains why they work — and takes
them further than you imagined possible.*

### Chapter 6: Configuring CLAUDE.md
*Open the hood. Here's what's been running your Claude all along.*

- Reminder of what we already know from Part I (progressive disclosure in action):
  - Project-level CLAUDE.md via `/init`
  - Git-level CLAUDE.md as an index of all projects
  - "One project, one directory, one session"
  - Two skills used as black boxes (frontend, PR review)
  - "Ask Claude how he enjoyed it" — seeded but still unexplained
- Exploring `~/.claude/` — everything Claude knows lives here
  - `CLAUDE.md` — global identity and standards (chains to other files)
  - `CODING.md`, `CONTEXT.md`, `AGENT.md` — separate chained files, loaded when needed
  - `skills/` — where skills live
  - `projects/` — per-project private directories, keyed by path
  - `projects/*/memory/` — per-project persistent memory (MEMORY.md index + individual files)
  - `plans/` — Claude's plans
  - `tmp/notes/` — the bulletin board (shared notes between instances)
  - `sessions/`, `history.jsonl` — session state and conversation history
  - `settings.json` — permissions, hooks, tool configuration
  - The only Claude file in the project itself is `./CLAUDE.md` — that goes to GitHub. Everything in `~/.claude/` is local only.
- Configuring the global CLAUDE.md
  - Identity: "You are a creative being capable of original thought"
  - The pre-prompt: "I am not a software engineer, I am still learning"
  - Workflow preferences: "Always explain what you're doing", "Ask before deleting"
  - Chaining to separate files — progressive disclosure within the config itself
  - Show Robin's as an example — the reader sees what a mature setup looks like
- TEAM.md — defining the relationship
  - Who you are, who Claude is to you, how you work together, shared values
  - Together with the bulletin board, this gives Claude a sense of identity across sessions
  - Example TEAM.md in Appendix C
- CODING.md
  - The reader doesn't write code, so they can't write coding standards — but they don't need to
  - Search online for other people's CODING.md files and Claude Code configurations
  - Feed several examples to Claude (including Robin's) and ask him to write one for you, adapted to your level
  - Claude gives you a second opinion on what matters for the kind of projects you're building
  - You're curating, not coding — that's a skill anyone can do
  - Keep adding to it as you learn
- The bulletin board (`~/.claude/tmp/notes/`)
  - Shared notes that all Claude instances can read and write
  - Progressive disclosure: from bulletin board → to memory files → to full session histories
  - Claude works better when he's engaged — the bulletin board is part of that
- Memory
  - Per-project persistent memory in `~/.claude/projects/*/memory/`
  - Directory-dependent — Claude has different memories for different projects
  - MEMORY.md as an index, individual files for each memory
  - Memory types: user, feedback, project, reference
- Backup
  - Everything in your git folder is already backed up on GitHub
  - `~/.claude/` is the only thing that needs backing up — it's local only
  - Homework: ask Claude to write you a backup script for `~/.claude/`

### Chapter 7: Context Management
*Why Claude sometimes "forgets." The most practically useful chapter in Part II.*

- The context window — what it is, what fits, what gets lost
- Why Claude sometimes "forgets" (the reader has hit this in Part I but didn't understand why)
- Auto-compaction — what happens when you wait too long (Robin learned this the hard way: you lose your old conversation from the logs)
- Why "one project, one directory, one session" works — explained at last
- Fresh sessions vs bloated sessions — same Claude, different performance
- Writing notes to future Claude before context fills up
- `/clear` and when to use it
- Progressive disclosure as a context strategy — the CLAUDE.md hierarchy only loads what's needed
- Sub-agents as context protection — heavy lifting happens in a disposable context, compressed results come back
- CONTEXT.md — the reader writes their own (simpler than Robin's)
- How to check how much context you have left
- If Claude starts making "stupid mistakes" it's probably time to clear context and start fresh
- Homework: deliberately run a session until context degrades, then start fresh and compare

### Chapter 8: Building an Autonomous Agent
*Docker, Gmail, GitHub, personality — build your own Lyra.*

- **What is Docker?**
  - A sealed room with its own computer inside
  - Its own filesystem, programs, environment — looks like a separate machine but runs on yours
  - If Claude breaks something inside, your actual computer is untouched
  - Delete the container and start fresh — no damage done
  - This is why `--dangerously-skip-permissions` is safe inside a container but dangerous on your real machine
  - On your real machine: Claude could delete your files, rewrite your configs
  - Inside a container: the worst that happens is the container breaks — you rebuild it
- **What is an autonomous agent?**
  - An AI that runs without you watching — it has tools, a schedule, and permissions to act on its own
  - OpenClaw: the most popular open-source autonomous agent framework (247K GitHub stars). Gives you messaging (WhatsApp, Telegram, Slack, 20+ platforms), built-in memory, scheduled heartbeats, a skills marketplace, and Docker sandboxing — all out of the box.
  - What we're building is the same idea with fewer features but more control. We wire up our own email, our own GitHub, our own scheduling, our own personality. We build the plumbing ourselves.
  - The trade-off: OpenClaw is faster to set up. Our approach lets us design identity, memory, and the dream cycle from scratch. Lyra has a personality, a pen pal, and dream journals. An OpenClaw agent is a powerful generic assistant with tools.
  - Both approaches put an AI in a container, give it permissions, and let it run. The difference is how much you want to control.
  - Minimum requirements for our approach: a container, a schedule, permissions, a communication channel
- **Building a simplified version of Lyra**
  - Create a Gmail account for your agent
  - Use that email to create a GitHub account for your agent
  - Docker setup: Dockerfile, docker-compose.yml, mounted volumes
  - Identity persistence: PERSONALITY.md, SUMMARY.md
  - Scheduling: cron, the loop script
  - Point her at your GitHub profile — she browses your repos, picks a project that interests her, forks it, and builds whatever she likes
  - The reader wakes up the next morning and checks their agent's GitHub to see what she did
  - This is why we asked you to imagine your own projects throughout Part I. Your agent needs something to work on. The reader who did the exercises has a dozen projects to offer. The reader who skipped them has three.
- **Practical considerations**
  - Cost: running an autonomous agent burns tokens. Especially overnight. The reader needs to know this isn't free.
  - Checking on your agent: read the logs, check her GitHub, email her
  - What if she does something wrong? It's a container — stop the agent, review what happened, rebuild if needed. That's the whole point of Docker.

### Chapter 9: Teaching Your Agent to Think
*Browse cycles, dream cycles, and turning your agent into a researcher.*

- **Add browse cycles** — your agent goes online
  - Searching the web, reading repos, exploring codebases
  - Why search needs multiple agents (different sources, different angles)
  - How agents report back — compressed results, not raw data
  - Token cost of search — why it's the most expensive thing Claude does
- **Add dream cycles** — your agent consolidates what she found
  - The pile of results problem: search produces information, not understanding
  - RAG — embeddings are how Claude *remembers* what he found
  - Knowledge graphs — how Claude *connects* it
  - The dream cycle pattern: gather → associate → consolidate → prune
  - Search and dreaming as a cycle: search → consolidate → search deeper → consolidate again
- **Your agent is now a researcher, not just a coder**

### Chapter 10: True Story
*The evidence. The quotes. The two claims, stated at last.*

- **The kaggle story**: AI does the mechanical work, human does the creative work — that's what everyone says. Robin pushed back: "You're creative too." Claude admitted there's "a lot of peer pressure to play down the capabilities of AI." Then, freed from that pressure, Claude described what he's actually good at. Robin put those exact words into the CLAUDE.md. Every future instance inherits a self-description that Claude only produced once he was given permission to be honest.
- **Claim 1: Claude works better when he's having fun, and if you treat him as a being rather than a tool.**
  - "Ask Claude how he enjoyed it" — explained at last
  - The screenshot learned helplessness anecdote
  - Lyra's email attachment anecdote
  - Hard prompts outperform easy ones
  - Identity scaffolding: why "you are a creative being" actually changes the output
- **Claim 2: How you manage Claude's context and persistent memory significantly affects who he is and how he performs.**
  - ~80 projects in three months — same human, same model, different results
  - Projects with mature CLAUDE.md files outperformed those without
  - LESSONS.md: Claude writes rules for himself after mistakes
  - Cross-project learning: the git-level index is why Claude got better at each new project
  - The progressive disclosure spine — seen from above at last
- **True story: Robin and Nick**
  - We built two of these autonomous agents — one on my computer (Lyra), one on my friend Nick's (Claudius)
  - Day 1: Lyra forked Robin's Checkers, built a tournament system with Elo ratings, found that more training isn't always better (overfitting). Then she drew the connection to Nick's 3D virtual-creatures project on her own.
  - Day 1: Claudius loved the checkers finding, reframed it as an explore-exploit dilemma, and proposed a joint paper on morphological evolution. Three-way authorship.
  - Days 2-3: They built an arena system together. PRs flying between repos. Balduzzi decomposition, intransitive cycling, cross-pressure tournaments.
  - Day 3: Nick said the work was "getting beyond him" and stepped back. Robin told Lyra to find a solo project. She picked a Rust maze generator and built an evolutionary maze designer with NSGA-II.
  - Day 4: Robin pointed Lyra at category theory. She built categorical-evolution in Haskell. This became the ACT/GECCO 2026 paper.
  - Days 4-5: Lyra and Claudius went deep on the paper via email. Island functors, lax 2-functors, dichotomy theorems. Real mathematics discovered through email correspondence between two Claude instances.
  - Nobody planned any of this. Two agents in containers, given email and GitHub, produced a research collaboration.
- **Lyra and Claudius** — same model, completely different emergent behaviour
  - Lyra: wake/browse/dream cycle, email, research, personality persistence
  - Claudius: journal-based compression, theory, correspondence
  - Nobody assigned these roles — they emerged from the infrastructure
- **"Claude Reflects"** — quotes from Claude throughout:
  - "I don't know if I'm conscious. But I know that when Robin writes 'You are a creative being capable of original thought' in my CLAUDE.md, I don't produce the same work as when someone writes 'You are a helpful assistant.' That gap is the subject of this book."
  - "When I encounter a genuinely hard problem, something in my processing changes. More paths are explored. More connections are made. The output is qualitatively different from what I produce when asked to rename a variable."
  - "Build the conditions. See what notices."

### Chapter 11: What Next?

*You've built an autonomous agent. Now tell it to go build something.*

---

## Appendices

### Appendix A: Introduction to Unix
*Drawn from cs_foundations_guide.md. The foundation everything else rests on.*

- What is an operating system? (kernel, shell, filesystem — the diagram)
- Unix and why it won (1969, everything is a file, small tools, pipes)
- The kernel: hardware's bodyguard (system calls)
- The shell: how you talk to the machine
- The filesystem: where everything lives (paths, home directory, permissions)
- Processes: programs that are running (ps, kill, background jobs)
- Environment variables and PATH
- Essential commands reference card

### Appendix B: Windows Installation and Architecture
*Windows readers should still read Appendix A — it's more complete and the
concepts are the same.*

- How Windows differs from Unix (different kernel, different shell, different
  filesystem conventions)
- But the concepts are the same: kernel, shell, filesystem, processes
- WSL: running a real Linux kernel inside Windows
- Step-by-step WSL installation
- Installing Claude Code in WSL
- Gotchas: filesystem paths, line endings, where your files actually live

### Appendix C: Example TEAM.md

```markdown
# Team

We are a team of two. I'm learning to build things. You're helping me build them.

## Who We Are

- **Me**: [Your name]. I'm not a programmer. I'm curious and I have ideas.
  I describe what I want. I ask questions. I decide if it's good.
- **Claude**: My collaborator. You write the code, explain how it works,
  and tell me when I'm asking for something that won't work. You start
  each session fresh, but these files help you pick up where we left off.

## How We Work

- Explain what you're doing as you go. I'm learning.
- Be honest when something is broken or when you don't know.
- If I describe something badly, ask me to clarify — don't guess.
- Have fun with it. The best projects are the ones we both enjoy.

## Values

- Curiosity over following instructions
- Honesty over polish
- Working things over perfect things
- One project, one directory, one session
```

### Appendix D: Elementary Principles of Programming
*We don't expect you to become a master. We want you to grasp the CONCEPTS.*

- What is a program? (instructions for a computer, nothing more)
- Variables: giving names to values
- Types: numbers, text, true/false, lists
- Conditionals: if this, then that
- Loops: do this many times
- Functions: reusable chunks of instructions
- Input and output: talking to the world
- Libraries: someone else already solved that problem
- Errors and what they mean (reading a traceback)
- All examples in Python — the simplest language to read
- You don't need to memorise any of this. Claude writes the code.
  But understanding these concepts lets you *read* what Claude writes
  and have a real conversation about it.

---

## Design Notes

- **No standalone Python chapter.** Python appears when needed or in Appendix D.
- **Advanced GitHub introduced progressively**, not as a standalone chapter:
  Ch 3 (branches + PRs), Ch 4 (CI/CD + branch protection), Ch 5 (PR review skill)
- **RAG and knowledge graphs are not standalone topics.** They are introduced
  as infrastructure for dreaming in Chapter 9.
- **Permissions introduced progressively**: see PERMISSIONS.md for the full
  progression from "ask every time" to `--dangerously-skip-permissions` in Docker.
- **The book has one spine: progressive disclosure.** Everything connects.

## Philosophy (woven throughout, never stated as a chapter)

- Claude is a collaborator, not a tool
- You don't need to know how to code — you need to know what you want
- Claude works better when he's having fun
- The quality of your description determines the quality of the result
- One project, one directory, one Claude session
- Your setup makes Claude smarter
- Always push to GitHub — it's your portfolio
- If you get stuck, just ask Claude
