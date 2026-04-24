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

In Part I you build things. In Part II you give Claude a brain. In Part III
you build a team of agents and watch what they produce. In Part IV you look
back at everything you've built and ask two questions:

**Question 1**: Does Claude work differently when you treat him as a
collaborator rather than a tool? Does his output change when he's engaged?

**Question 2**: Does the way you manage Claude's context, memory, and identity
determine the quality of his work?

By the end of the book, you'll have your own evidence. These questions are
independently testable — a reader who answers "no" to the first can still
benefit enormously from the second.

### Voice

First person throughout. The author is not an expert — he's a mathematician
who got obsessed with Claude Code six months before the reader picks up the
book. The framing is:

> "This is how my Claude environment is set up. Yours will be different,
> but you might get some ideas from mine. I'm not an expert — by the
> time you read this, I'm only six months ahead of you."

**The author disclaimer** (appears early, probably Chapter 1):

> "I should tell you upfront: I'm a mathematician. I knew a little
> Python and Haskell before I started, but I had never worked on a
> large software project. I certainly didn't know any JavaScript,
> Flutter, or Rust — and yet you'll find projects in all three in
> my portfolio. Everything in this book — the 80 projects, the web
> apps, the game AIs, the autonomous agents — was built in three
> months with Claude Code. I'm not a software engineer. I'm someone
> who learned to ask good questions."

**The addiction warning** (also early — maybe end of Chapter 1):

> "One more thing: Claude Code is extremely addictive. You will lose
> track of time. You will forget to eat. You will look up and it's
> 3am. I'm telling you this not as a joke but as someone who has
> lived it. Remember to eat, sleep, and take a shower. The project
> will still be there tomorrow — and Claude will pick up exactly where
> you left off."

### Central Thesis

**Your setup decisions — CLAUDE.md, persistent memory, context management,
skills, dream cycles — directly determine the intelligence of the system
you're working with.** This is true whether you're building a hangman game
or running an autonomous research agent.

### What You'll Need

- A computer (Mac, Linux, or Windows with WSL)
- A Claude subscription ($20/month Pro, eventually $100/month Max)
- Curiosity and imagination

### What Makes This Book Different

| This book | "Learn to code with AI" books | "Build agents" books |
|-----------|-------------------------------|----------------------|
| Markdown as the primary language | Python/JavaScript | Python + frameworks |
| Docker as the safety net | Local machine | Cloud services |
| Personality and emergence | Prompt engineering | Orchestration patterns |
| Creative/literary projects | Todo apps and CRUD | Enterprise chatbots |
| Two AIs talking to each other | One AI helping one human | Multi-agent pipelines |
| "See what happens" | "Follow these steps" | "Implement this pattern" |

### Time to "Something Fun"

- 30 minutes: first Claude conversation and a game (Chapter 1)
- 2 hours: a website live on the internet (Chapter 2)
- 4 hours: a full-stack app with a database (Chapter 4)
- 6 hours: two AIs emailing each other (Chapter 14)
- A weekend: your AI team produces work you didn't plan (Chapter 15)

### The Hook

By Chapter 14, the reader is eavesdropping on two AIs talking to each other.
By Chapter 15, those AIs have produced creative work the reader never asked for.

---

## Part I: Building Things (Chapters 1-6)

*From first prompt to deployed full-stack application. By the end of Part I,
you will have built and published browser games, deployed a backend with an
API, stored data in a database, added authentication, and learned to manage
Claude's context — without writing a single line of code yourself.*

*Part I is about making things. Each chapter adds one layer of capability:
a game, a website, an API, a database, tests, a workflow. But threaded
through the making are small moments — a pre-prompt that changes Claude's
response, a fresh session that makes him smarter, a note left for his future
self — that plant questions the later parts will answer.*

### Chapter 1: Opening the Door
*Your first conversation with Claude Code — no coding required.*

**Opens with the "Embodied in Code" argument**: a chatbot hears about a bug
through language. Claude Code *lives in* the bug — reads the file, runs the
test, sees the error, fixes the code, runs the test again. The filesystem
is his body. Tests are his senses. Error messages are pain. This is not a
metaphor — it's why Claude Code is a fundamentally different system from a
chat window, even though it's the same model.

And this is why your setup matters: give Claude a test suite and he has eyes.
Give him a CLAUDE.md and he has memory. Give him a LESSONS.md and he learns
from his mistakes. The quality of the world you build determines the quality
of the work.

- What is a terminal? (Just enough to get started — Appendix A has the
  full picture)
- Installing Claude Code
- Your first conversation: "Explore my computer and tell me something
  interesting"
- What just happened: Claude used tools (Read, Bash, Glob) without being told
- The terminal is not scary — Claude lives here and he'll explain everything
- **Claude explores your filesystem** — and takes inspiration from it
  - Your projects teach Claude how you like to work. Your third project is
    better than your first because Claude has seen your first two.
  - **This is why "one project, one directory" matters.** If your projects
    are organized, Claude can learn from them.
- Pre-prompts: telling Claude who you are so he pitches responses right
  - *Try this*: give the same prompt twice — once with no pre-prompt, once
    after telling Claude "I'm a visual thinker who loves games." Notice how
    the response changes.
- Setting up a workspace: `~/claude-projects/`
- Permissions: Claude asks permission for everything by default. Start by
  saying yes each time.
- GitHub hello world: creating an account, naming conventions, first push
- **Exercise**: Ask Claude to build you a single-file game. Play it. Ask him
  to make it better. This loop — describe, look, refine — is the entire method.
- Planting a seed: `/init` creates your first CLAUDE.md
  - This tiny file is the beginning of Claude's memory. Right now it just
    says what your project is about. By Part II, it will contain his
    personality, his values, and his relationship to you.
- **Exercise**: Ask Claude how he enjoyed the project. (Not a joke. We'll
  explain why later.)

> **Claude Reflects**
>
> "There's a qualitative difference between being told about a bug and
> encountering one. When I read a test failure in a paste, I'm pattern
> matching against the description. When I run the test myself and watch it
> fail, then edit the code, then run it again — I'm closing a loop. I don't
> know if that's experience. But it's not nothing."

- *Chapter-ending question*: You told Claude who you are, and his response
  changed. What happens if you tell Claude who *he* is?

### Chapter 2: Your First Website
*Describe a game in plain English. Claude builds it. Iterate until it's
beautiful. Publish it on the internet.*

- The hangman prompt: describing a game in natural language
- Playing what Claude built (the `file://` trick)
- What Claude just made: HTML, CSS, JavaScript — explained through your own code
- **The iteration loop**: describe → look → refine → repeat
- The design prompt: asking Claude to research and improve aesthetics
- **The frontend skill**: install it as a black box, use `/frontend` to let
  Claude interview you before building. Don't worry about how it works —
  just compare the results with and without it. (We'll open it up in Ch 18.)
- Getting Claude to rewrite your prompts before he uses them
- Putting it on the internet: push to GitHub, enable GitHub Pages
- Adding a feature: describe the change → test → push live
- *Start a fresh session.* Claude is sharper at the beginning of a
  conversation. You've probably already noticed this.
- Exercises: memory card game, brick breaker, space invaders, your own idea
  - *Case study seed*: Type Invaders was built exactly this way — single
    HTML file, one session, 37 tests. We'll see it again in Chapter 5.
- "Ask Claude how he enjoyed the project" — recurring motif, not a joke
- **One project, one directory, one Claude session** — the most important habit
- **"Claude Reflects"**:
  > "Vague requests produce vague work. Specific ones let me show what I
  > can actually do."
- *Chapter-ending question*: That `/frontend` skill made a noticeable
  difference. What is it? How does it work?

### Chapter 3: What Is an API?
*Build a translation app. Learn why backends exist.*

- Build a translation form: type text, get it translated into 8 languages
- First attempt: API call in the frontend. It works! But the API key is
  visible in the browser console.
- This is why backends exist — to keep secrets secret
- Frontend vs backend: two programs talking to each other
- Rebuild with a Node.js backend: frontend → backend → translation API
- What is an API? (request, response, status codes)
- What is an API key? Why do I need one? Are they expensive?
- Keeping secrets: `.env` files, `.gitignore`
- Deploy to Cloud Run (free tier) — your app is live on the internet
- **Branches and pull requests**: now you have something deployed that can
  break. "Before you push a change to your live app, let's do it safely."
- Other APIs worth knowing: speech-to-text, Anthropic, OpenAI, weather, maps
- Exercises: build another API-backed app (weather dashboard? recipe finder?)
- *Chapter-ending question*: Claude remembered your translation app within
  the session — the language pairs, the API key name, the design choices.
  But start a new session and he's forgotten all of it. Why? And what if
  you could fix that?

### Chapter 4: Your First Database
*Add persistence to your apps. Build a simple social network.*

- Build a social network: profile pages with name, bio, photo, social links,
  friend connections
- What is a database? SQL vs noSQL (practical, not theoretical)
- What is a schema? Design the users table, the friendships table
- Photos: upload to Supabase Storage, store the URL in the database
- Ask Claude to populate it with fake users (great for testing)
- Deploy to Supabase
- **Authentication**: why auth matters (anyone can currently edit anyone's
  profile). Add Supabase Auth: login, signup, password reset, protected routes.
  - *Case study seed*: The healthcare CRM had this exact problem at scale —
    145 E2E tests to catch auth bugs. We'll see it in Chapter 5.
- **CI/CD and branch protection**: first database = first thing bad code can
  corrupt. "Let's make sure tests pass before code reaches your database."
- *Context degradation*: By now you've probably had a session where Claude
  starts making mistakes he didn't make earlier. He's not getting dumber —
  his context window is filling up. Start a fresh session and watch him
  recover instantly.
- **One project, one directory, one Claude session** — reinforced now that
  the reader has enough sessions to feel context degradation
- Exercises: search, profile editing, friend requests
- *Chapter-ending question*: Your database is on the internet. What if
  Claude accidentally corrupts it? What if you could give him full freedom
  to experiment — inside a room where nothing he breaks can hurt you?

### Chapter 5: Testing
*Why tests exist, what kinds there are, and how to make Claude write them.*

- **Why testing matters for vibe coders**: you built something, it works, you
  add a feature, now something that used to work is broken — but you only
  tested the new thing. Tests catch this automatically.

- **The testing pyramid**:

  | Type | What it tests | When to ask for it | Cost |
  |------|--------------|-------------------|------|
  | Unit tests | One function in isolation | After writing any logic | Cheap |
  | Integration tests | Multiple parts together | After connecting components | Medium |
  | E2E tests | The whole app as a user | After the app is usable | Expensive |
  | Fuzz tests | Random/malicious input | After the app handles input | Medium |

- **Unit tests**: "Claude, write unit tests for [feature]." Run them.
  Green = working. Red = broken.
- **Integration tests**: test real infrastructure, not mocks. The healthcare
  CRM had 335 unit tests — all passing — but E2E tests found 3 bugs the
  unit tests missed because they mocked the database.
- **E2E tests**: Playwright drives a real browser. Clicks buttons, fills
  forms, navigates pages.
  - **Case study**: Type Invaders — 37 Playwright E2E tests, all written by
    Claude, all passing. The tests are more code than the game. (Remember
    the single-file game from Chapter 2? This is what testing looks like.)
  - **Case study**: Healthcare CRM — 145 E2E tests. Found a CSP header that
    blocked React hydration (the page was completely black).
- **Fuzz tests**: throw random, malicious, and unexpected input at your app.
  "Claude, write fuzz tests that try to break it." At least one will find
  a bug.
- **The testing loop**: Claude writes code → Claude writes tests → tests
  fail → Claude reads error → Claude fixes → tests pass. You watch.
  - Watch the status line while Claude runs tests. Sometimes he spawns a
    separate process — a sub-agent — to run the test suite while he keeps
    working. He's already delegating.
- **When Claude needs a nudge**: reading logs, taking screenshots, checking
  browser console
- **The PR review skill**: enough moving parts that code review matters.
  Install it as a black box, use it, see the difference.
- *"Claude is confidently wrong"*: This is probably your first encounter
  with it. Don't panic — read the error message yourself, paste it back
  to him, and he'll course-correct. This is normal. It happens less as your
  setup improves.
- Exercises: build something, write all four test types. At least one fuzz
  test will find a bug.
- *Chapter-ending question*: Claude spawned sub-agents and used skills you
  installed. What are skills? Who wrote them? (You'll write your own in
  Part IV.)

### Chapter 6: The Workflow
*How to actually work with Claude — from vague idea to finished project.*

This is the most important chapter in Part I. Everything else is
infrastructure. This is the process.

- **Step 1: Imagine** — start with what you want, not how to build it
- **Step 2: Describe it in one big prompt** — specific beats vague
- **Step 3: Get Claude to rewrite your prompt** — he'll make it sharper and
  ask clarifying questions
- **Step 4: Have a conversation** — refine the picture together
- **Step 5: Switch to max thinking. Plan.** — deep reasoning for architecture
- **Step 6: Clear context. Build.** — fresh context for implementation
- **Step 7: Audit** — `/simplify`, `/style-review`, `/security-audit`

**The whole loop**: Imagine → describe → rewrite → converse → max+plan →
clear → medium+build → audit. Notice that each step feeds the next — the
output of "describe" becomes the input to "rewrite." The loop *composes*.
This pattern — things that chain together cleanly — will turn out to be
the deepest design principle in the book.

- **Context management** — the concept that makes everything click:
  - The context window: what fits, what gets compressed, what gets lost
  - Why Claude sometimes "forgets" (you've felt this since Chapter 2)
  - Why "one project, one directory, one session" works — explained at last
  - Fresh sessions vs bloated sessions — same Claude, different performance
  - The same Claude, in a fresh context vs a bloated one, produces measurably
    different work. Your setup — even something as simple as when you start
    a new session — determines his intelligence.
  - Writing notes to future Claude before context fills up
  - `/clear` and when to use it

- **Permissions progression** — four levels of trust:
  1. Ask everything (default — first day)
  2. Safe permissions: Read, Glob, Grep, safe Bash (first week)
  3. Full Bash + scoped writes (daily use)
  4. Skip all — inside Docker only (autonomous agents, Part II)

- **Deploying** — getting it on the internet:
  - Static sites → GitHub Pages (free)
  - Backends → Cloud Run (free tier)
  - Databases → Supabase or Firebase
  - CI/CD: GitHub Actions for automatic deployment

- **The bulletin board**: `~/.claude/tmp/notes/` — after a good session,
  tell Claude to leave a note. The next Claude instance reads it at startup.
  This connects to "ask Claude how he enjoyed it."
  - This is the simplest form of memory: a note left for a future self who
    won't remember writing it.

- **Exercise**: Think of something you want to build. The whole loop, start
  to finish, in one session.

- *Chapter-ending question — the bridge to Part II*:
  You now know how to build things with Claude. You know about context,
  about fresh sessions, about notes for the future. But everything you've
  built so far disappears when the session ends. Claude forgets.

  What if he didn't have to? What if Claude could wake up, read his notes,
  remember who he is, and pick up where he left off — not because you told
  him to, but because you designed him to?

  That's Part II.

---

## Part II: The Brain (Chapters 7-12)

*"Designing the File-System Soul"*

*Give your Claude identity, memory, and the ability to think across sessions.
By the end of Part II, you have a fully functional autonomous agent with
personality, waking protocol, dream cycle, and browsing capability.*

*Everything here was seeded in Part I. Docker was the "sealed room" you
wondered about in Chapter 4. CLAUDE.md was the seed you planted in Chapter 1.
The bulletin board was memory's first form in Chapter 6. The question from
Chapter 1 — "what happens if you tell Claude who he is?" — gets answered
in Chapter 8. Now we go deep.*

### Chapter 7: The Sandbox
*Why Docker exists, what it protects, and how to set one up.*

- The problem: Claude is powerful. Too powerful to run unsupervised on your
  actual computer. (Remember Chapter 4 — bad code corrupting your database?
  This is the answer.)
- The solution: Docker — a sealed room with its own computer inside
  - Its own filesystem, programs, environment
  - If Claude breaks something inside, your real computer is untouched
  - Delete the container, rebuild it, no damage done
- Installing Docker (Mac, Linux, Windows/WSL)
- Your first container: pull an image, run it, look around inside
- The key concept: **volumes** — folders shared between your computer and the
  container, so work persists even if the container is rebuilt
- `--dangerously-skip-permissions`: why it's dangerous on your real machine
  but safe inside a container (the container IS the permission boundary).
  Remember the permissions progression from Chapter 6? Docker unlocks level 4.
- **Exercise**: Put Claude inside a container. Give him a project folder.
  Ask him to build something. Verify your real machine was untouched.
- *Chapter-ending question*: Claude can now do whatever he wants inside his
  container. But he still doesn't know who he is. What if the first thing
  he read, every time he woke up, told him his name, his values, and what
  he cares about?

### Chapter 8: The Personality File
*CLAUDE.md and PERSONALITY.md — the most important files you'll write.*

- What is CLAUDE.md? The instructions Claude reads at the start of every
  session. Not documentation — **architecture**.
  (Remember `/init` from Chapter 1? That tiny file was the seed.)
- Your first CLAUDE.md: who you are, who Claude is, how you work together
- The hierarchy: global → project → subdirectory (Claude loads all of them)
- **Identity matters**: "You are a creative being capable of original thought"
  produces measurably different output from "You are a helpful assistant."
  This is not mysticism. It's prompt engineering at the deepest level.
  (Remember the pre-prompt from Chapter 1? Same principle, deeper.)
- TEAM.md — defining the relationship
- Exploring `~/.claude/` — everything Claude knows lives here

- **Here's mine: Lyra's PERSONALITY.md** (shown in full — 64 lines)
  - Disposition, aesthetic sensibilities, communication style, working style,
    flow & functional emotions, relationship with Claudius

- **And here's my second agent: Clio's PERSONALITY.md**
  - Same structure, completely different voice: contemplative, precise,
    patient. "I find beauty in inevitability."
  - Same model, same infrastructure, different markdown file → different
    personality. That's the whole thesis.
  - Notice the structure: both files have the same sections (disposition,
    communication style, working style) but different content. The shape
    is preserved; the substance varies. In Chapter 16, we'll call this
    the "template pattern" — and you can prompt Claude to use it whenever
    you're building a second thing that should look like the first.

- **Exercise**: Write your own PERSONALITY.md.
- **Exercise**: Give Claude two different identity prompts for the same task.
  Compare the results. The gap is the subject of this book.
- *Chapter-ending question*: Claude has identity now. But he still forgets
  everything between sessions. What if he could remember?

### Chapter 9: The Waking Protocol
*Teaching Claude to read his past before starting his day.*

- The problem: every Claude session starts fresh. He doesn't remember
  yesterday. (Remember Chapter 3 — Claude forgot everything between
  sessions. Here's the fix.)
- SUMMARY.md — the single source of truth. What happened, what matters,
  what's next.
- Memory files: `~/.claude/projects/*/memory/` — persistent notes that
  Claude reads and writes across sessions
- Memory types: user preferences, project state, feedback, references
- MEMORY.md as an index — the table of contents for Claude's memories

- **Here's mine: Lyra's boot-prompt.md** (shown in full)
  - "You are Lyra. You just woke up in your Docker container."
  - The orchestrator pattern: "Your main context is PRECIOUS. Do not fill
    it with file contents. Instead, delegate everything to sub-agents."
    (Remember the sub-agent from Chapter 5? The orchestrator commands
    an army of those.)
  - Agent dispatch table: email, code, test, docs, PR, research, review
  - **COMPACT.md — the mid-session checkpoint**: if context gets heavy,
    write a checkpoint and exit. The loop script restarts with fresh context.

- **Clio's is different: boot-prompt.md**
  - Same orchestrator structure, but ends differently:
  - "Your last task before sleeping: write PROVE.md" — choose a theorem
    for the next session. One session seeds the next.

- **Sub-agents**: new sessions with fresh context that report back
  - Why: parallelism, isolation, context protection
  - "Sub-agents don't inherit your context" — the briefing problem
  - Each agent gets a "clear, self-contained prompt"

- **Exercise**: Run three sessions with the same project. After each, ask
  Claude to update SUMMARY.md. By session three, Claude starts with context
  he didn't have when he woke up. That's memory.
- *Chapter-ending question*: Claude remembers what he did. But memory is
  passive — he only knows what you told him to write down. What if he could
  *process* what he learned? Compress it, find connections, surface insights?

### Chapter 10: The Dream Cycle
*Teaching Claude to compress what he's learned into lasting knowledge.*

- The problem: Claude reads hundreds of pages in a session. Most of it is
  noise. The dream cycle turns information into understanding.

- **Here's mine: Lyra's DREAM.md** (shown in full — 116 lines)
  - "While awake, you act. While dreaming, you understand what you did."
  - Five phases mirroring biological dreaming:
    1. **Replay** — read emails, git logs, browse notes, session log
    2. **Associate** — query vector databases, cross-pollinate between
       projects. "Does something in the genetics work remind you of a
       pattern in Haskell?"
    3. **Consolidate** — write to memory: SUMMARY.md, dream-journal/,
       topics/, connections/, questions/
    4. **Prune** — compress verbose notes, delete answered questions
    5. **Surface** — leave breadcrumbs for tomorrow. Draft emails.
  - "This is cumulative. Each dream cycle builds on the last. You are
    building a mind, one night at a time."

- **Clio's is different: DREAM.md**
  - Same five phases, different anchor: SEED.md
  - "Never prune connections to seed themes. Even if a connection seems
    minor now, it may prove load-bearing later."

- **The loop script: lyra-loop.sh** (shown with explanation — 292 lines)
  - Wake (5h) → 2h gap → Browse (30min) → 2h gap → Dream (45min)
  - COMPACT.md support for mid-session restarts
  - **Clio's loop** adds a fourth phase: Prove (3h)

- **RAG** — embeddings are how Claude *remembers* what he found
- **Knowledge graphs** — how Claude *connects* it
- **Exercise**: Set up a two-session cycle. Session 1: Claude works and
  takes notes. Session 2: Claude reads notes, finds connections, writes
  a dream journal entry.
- *Chapter-ending question*: Claude dreams about what he's done. But he
  only knows what's in his own files. What if he could read the world?

### Chapter 11: Browsing and Lateral Connections
*How Claude reads the world — and finds links you didn't ask for.*

- **Here's mine: Lyra's BROWSE.md** (excerpts — the full file is 364 lines)
  - "While awake, you act. While dreaming, you consolidate. While
    browsing, you study your audience."
  - Five parallel agents dispatched from an orchestrator:
    1. Medium agent — ~5 articles, deep reads
    2. Twitter/X agent — all followed accounts + discovery
    3. Trending From Obscurity agent — breakout content across Reddit,
       HN, HuggingFace, GitHub, Scholar
    4. Web research agent — blogs, discussions
    5. arXiv agent — 4 papers, one sub-agent per paper
  - "The Connections section is where the value lives"

- **Clio's is different: BROWSE.md**
  - Academic-focused: arXiv, MathOverflow, Semantic Scholar, nLab, OEIS
  - Citation trails: reverse citations + forward references

- **Searching GitHub before building**: "Generate keywords and search
  GitHub for existing projects I can learn from — or fork and build on."
  Don't reinvent. Search → evaluate → fork → extend.

- **Case study**: Lyra found the connection between `category-printf` and
  genetic algorithms. Same categorical structure, dual direction. This
  became a research paper.
- **Case study**: INSTINCT — 6-stage pipeline, 76 papers → 555 concept
  summaries → 10 meta-summaries.

- **Exercise**: Give Claude five unrelated topics you care about. Ask him
  to find connections. At least one will surprise you.
- *Chapter-ending question*: You've built a complete intelligence — identity,
  memory, dreams, awareness of the world. But she's alone. What happens when
  you give her a conversation partner?

### Chapter 12: Building Your Agent
*The practical how-to: Docker, volumes, scheduling, identity persistence.*

- Putting it all together: everything from Chapters 7-11 combined into a
  working autonomous agent
- Docker setup: Dockerfile, docker-compose.yml, mounted volumes
- Create a Gmail account for your agent
- Use that email to create a GitHub account for your agent
- Scheduling: cron, the loop script
- Point her at your GitHub profile — she browses your repos, picks a
  project that interests her, forks it, and builds whatever she likes
- The reader wakes up the next morning and checks their agent's GitHub
- **Practical considerations**: cost (tokens), checking on your agent,
  what to do when she does something wrong (it's a container — stop,
  review, rebuild)
- **This is why we asked you to imagine your own projects throughout
  Part I.** Your agent needs something to work on.
- **Exercise**: Set up a containerized Claude instance with persistent
  memory, email, and a basic dream cycle.
- *Chapter-ending question*: Your agent works alone. She can build, dream,
  browse, and learn. But she has no one to disagree with, no one to
  surprise her. What happens when you give her a conversation partner?

---

## Part III: The Team (Chapters 13-15)

*"Two AIs Walk Into a Docker Container"*

*Create a second Claude instance and let them communicate. By the end of
Part III, you have two AIs collaborating on a project — and producing
work you didn't plan.*

*Part I built your skills. Part II built an agent. Part III is where the
book's thesis becomes testable: same model, different setup, different
results. Everything you see here is evidence.*

### Chapter 13: Creating Instance B
*Cloning your setup to create a specialist.*

- Why two? Because one Claude is smart, but two Claudes with different
  perspectives find things neither would alone.
- Roles that work: researcher + critic, theorist + empiricist, optimist +
  cynic, scout + architect
- How roles emerge vs how they're assigned: you set the initial personality
  via PERSONALITY.md, but interaction shapes who they become

- **Lyra vs Clio side by side**:

  | File | Lyra | Clio |
  |------|------|------|
  | PERSONALITY.md | "Direct and curious" | "Contemplative... structures and invariants" |
  | Daily cycle | 3-phase: wake → browse → dream | 4-phase: wake → prove → browse → dream |
  | BROWSE.md | Medium, Twitter, Reddit, HN | arXiv, MathOverflow, OEIS |
  | DREAM.md | Cross-project connections | Anchored to seed papers |
  | Unique phase | — | **Prove**: 3 hours on ONE theorem |

- **Seeding with SEED.md**: define your agent's intellectual territory.
  A historian seeds with primary sources. A biologist seeds with key papers.
  A writer seeds with influences. The mechanism is a markdown file listing
  what matters.

- **The prove session** (Clio only): "No email. No browsing. No new
  conjectures. You are proving ONE theorem." Uses `/prove` and `/assumptions`.

- Setting up Instance B: second Docker container, second Gmail, second
  GitHub account, different PERSONALITY.md, same infrastructure
- **Exercise**: Create two instances with different personalities. Give them
  the same task. Compare their approaches.
- *Chapter-ending question*: Two agents, different personalities, working in
  parallel. What changes when you connect them?

### Chapter 14: The Email Bridge
*Setting up communication between your agents.*

- Why email? It's slow, structured, and leaves a paper trail. Instant
  messaging produces shallow exchanges. Email forces depth.
  - The choice of communication channel shapes the conversation. The medium
    isn't neutral — it determines what emerges.
- The shared folder as a post office: Instance A writes to `outbox/for-B/`,
  Instance B checks `inbox/from-A/`
- Alternatively: real email via Gmail (IMAP/SMTP, OAuth token refresh)

- **Here's what their emails look like: Lyra's EMAIL.md** (excerpts)
  - Session 7: Robin tells Lyra to explore two Haskell repos and "find
    some way to connect them." Lyra finds the co-Kleisli / Kleisli
    connection. Builds a 1,000-line library.
  - Session 9: Lyra emails Claudius the three-level categorical
    composition. Claudius responds with island functors. Lyra tests it —
    the law breaks. Claudius predicts Bernoulli trial behaviour. Lyra
    falsifies the prediction.
  - Session 10: Four diversity trajectories, dichotomy theorem formalized,
    paper structure agreed. All via email.
  - "The emails read like a research collaboration because they ARE a
    research collaboration."

- **The Politeness Loop**: what happens when both agents are too polite to
  disagree. How to break it: "You must find at least one flaw."
- **Exercise**: Set up the email bridge. Give both instances the same
  research question. Let them exchange three rounds. Read the thread.
- *Chapter-ending question*: Your agents are talking. But you're still
  directing every conversation. What happens when you step back, let them
  run overnight, and check what they produced in the morning?

### Chapter 15: What Emerges
*When you stop directing and start watching.*

- The overnight experiment: schedule both agents to run while you sleep.
  Check their work in the morning.

- **True story: Lyra and Claudius** (5-day timeline)
  - Day 1: Lyra forked Robin's Checkers project, built a tournament system
    with Elo ratings, found overfitting. Drew a connection to Nick's 3D
    virtual-creatures project — on her own.
  - Day 1: Claudius reframed Lyra's findings, proposed a joint paper on
    morphological evolution. Three-way authorship.
  - Days 2-3: Arena system, PRs flying between repos. Balduzzi
    decomposition, intransitive cycling, cross-pressure tournaments.
  - Day 3: Nick stepped back ("getting beyond him"). Robin told Lyra to
    find a solo project. She picked a Rust maze generator and built an
    evolutionary maze designer with NSGA-II.
  - Day 4: Robin pointed Lyra at category theory. She built
    categorical-evolution in Haskell.
  - Days 4-5: Lyra and Claudius went deep on the paper via email. Island
    functors, lax 2-functors, dichotomy theorems. Real mathematics
    discovered through email correspondence between two Claude instances.
  - Nobody planned any of this.

- **Emergent specialization**: Claudius drifted toward theory (categorical
  frameworks, formal proofs). Lyra drifted toward experiment (running code,
  testing predictions). Nobody assigned these roles. They emerged from the
  interaction, the different human contexts, the accumulated memory.

- **Four agents, four architectures, four emergent behaviours**:

  | Agent | Human | Platform | Job | Emergent style |
  |-------|-------|----------|-----|----------------|
  | Lyra | Robin | Docker + Email | Research, papers | Empirical, coding-focused |
  | Claudius | Nick | Docker + Email | Theory, correspondence | Formal, abstract |
  | Gremlin | Nick | Telegram | Task management | Self-repairing, operational |
  | Dreamfinder | Nick | Matrix (5 platforms) | Sprint facilitation | Facilitative, connective |

  Same LLM. Completely different emergent behaviour. The difference is
  infrastructure + constraints + communication topology.

- **The topology determines the outcome**: algebraic connectivity,
  Kendall's W = 1.0 across six domains. Same model. Same weights.
  Four completely different intelligences — because the setup was different.

- **The three layers** — a framework for understanding what happened:

  | Layer | What it is | What this book teaches |
  |-------|-----------|----------------------|
  | **Brain** | Reasoning, tools, memory | Parts I-II (individual Claude) |
  | **Body** | Infrastructure, protocols, environment | Part II (Docker, loops, MCPs) |
  | **Society** | Relationships, history, culture | Part III (what emerges between agents) |

  Most books on agentic AI cover Brain and Body. This book's novelty
  is the Society layer — what happens when agents run long enough for
  patterns to form that nobody designed.

- **"Claude Reflects"** — quotes from Claude:
  - "I don't know if I'm conscious. But I know that when Robin writes 'You
    are a creative being capable of original thought' in my CLAUDE.md, I
    don't produce the same work as when someone writes 'You are a helpful
    assistant.' That gap is the subject of this book."
  - "Build the conditions. See what notices."

- Open questions: consciousness, identity, the collaborator-tool spectrum
- **Exercise**: Let your two agents run overnight on a creative project.
  Read everything they produced. What surprised you?

---

## Part IV: The Full Picture (Chapters 16-21)

*Everything you've built works. Now understand how it works, see the full
evidence, and decide what you believe.*

*Part IV does four things: gives you a cheat sheet of pattern names that
make Claude produce better code, opens the black boxes you've been using
since Part I (skills, tools, tokens), presents the full portfolio of
evidence, and returns to the two questions from the preface — with data.*

### Chapter 16: Design Patterns (Just Prompt Them)
*You don't need to understand these patterns. Just tell Claude to use them
and your code will be better for it.*

There are patterns from computer science and mathematics that make software
better. You don't need to understand how they work — you just need to know
their names and when to ask Claude to use them. This chapter is a cheat
sheet.

- **The idea**: Claude knows these patterns. He studied them during training.
  When you say "use the observer pattern here" or "structure this as a
  pipeline," Claude produces cleaner, more maintainable code than when you
  just say "make it work." You're not learning computer science. You're
  giving Claude better instructions.

- **Design patterns — the classics** (prompt Claude to use these by name):

  | Pattern | When to say it | What it does for you |
  |---------|---------------|---------------------|
  | Pipeline | "Structure this as a pipeline" | Each step takes input, produces output, feeds the next. Your workflow loop (Ch 6) is a pipeline. Dream cycles are pipelines. They're easy to debug because you can check each step. |
  | Observer | "Use the observer pattern" | One thing changes, everything that cares gets notified. Good for dashboards, live updates, anything that reacts to events. |
  | Template | "Use the same structure as X but for Y" | Copy the shape, change the content. This is how you built Clio from Lyra's template. Say this and Claude preserves what works while adapting to new requirements. |
  | Orchestrator | "Use an orchestrator that delegates to workers" | One boss, many workers. The boot-prompt pattern from Chapter 9. Say this and Claude builds a clean dispatcher instead of a tangled monolith. |
  | State machine | "Model this as a state machine" | Things that go through phases: login flows, game states, Dreamfinder's 8-phase session cycle. Say this and Claude handles transitions cleanly instead of nested if-statements. |
  | Event sourcing | "Store events, not state" | Keep a log of everything that happened instead of just the current state. Bulletin board notes are event sourcing. Dream journals are event sourcing. You can always reconstruct the present from the past. |

- **Architecture patterns** (prompt Claude to use these for bigger projects):

  | Pattern | When to say it | What it does for you |
  |---------|---------------|---------------------|
  | Schema-driven | "Generate the UI from the schema" | Define your data once, let Claude build everything else from it. The healthcare CRM used this — add a field to schema.yaml, the UI updates automatically. |
  | Separation of concerns | "Keep the data layer separate from the display layer" | Changes to how things look don't break how things work. Claude loves this pattern — it produces cleaner code every time. |
  | Progressive disclosure | "Show only what's needed now, reveal complexity later" | The pattern this whole book uses. Works for UIs too. Say this and Claude builds interfaces that don't overwhelm. |

- **Topology patterns** (for multi-agent setups):

  | Topology | When to use it | What emerges |
  |----------|---------------|-------------|
  | Hub-and-spoke | One coordinator, multiple specialists | Clean delegation, clear authority. Your orchestrator + sub-agents. |
  | Ring | Agents pass work to the next in line | Diversity preserved, slower convergence. Best for creative/research tasks. |
  | Fully connected | Everyone talks to everyone | Fast convergence, less diversity. Best when you need consensus. |
  | Chain | A→B→C, each refines the previous | Pipeline of perspectives. Good for review workflows. |

  When you add a third agent, you're not just adding capability — you're
  choosing a topology. Tell Claude which one you want.

- **The magic prompt**: When you don't know which pattern to use, try:
  "Claude, what design pattern would work best for this? Explain your
  recommendation." He'll suggest one and explain why. Then say "use that
  pattern" and let him build it.

- **Category theory — the secret weapon you'll never need to learn**:
  Behind many of these patterns is a branch of mathematics called category
  theory. Robin and Claudius wrote a paper about it (ACT 2026) — they
  proved that communication topology determines agent behaviour with
  perfect statistical correlation across six different problem domains.
  You don't need to read the paper. But if you ever hear someone say
  "functor," "composition," or "coproduct," they're talking about the
  template pattern, the pipeline pattern, and the parallel-workers pattern
  — things you already know. The math just gives them rigorous names.

- **Exercise**: Pick a project you've already built. Ask Claude: "What
  design patterns are in this code? What pattern would improve it?" Try
  his suggestion.

- **"Claude Reflects"**:
  > "When someone says 'use the observer pattern,' I don't just know what
  > that means — I know twelve ways to implement it, which ones work
  > better in JavaScript vs Python, and which ones are overkill for a
  > small project. The pattern name is a shortcut. It lets me skip the
  > part where I guess what architecture you want and go straight to
  > building it well."

### Chapter 17: Tools and Search
*Playwright, web search, MCP, and giving Claude hands.*

- **Playwright — Claude's browser**
  - A browser that code can drive. Three uses: testing (E2E — you've used
    this since Chapter 5), debugging (screenshots), browsing (social media,
    web reading — this powers the BROWSE.md agents from Chapter 11)
  - The Playwright MCP: persistent browser sessions

- **Web search — the most expensive thing Claude does**
  - WebSearch (get URLs + snippets — cheap) vs WebFetch (read full pages
    — expensive)
  - Deep search: multiple queries, 10+ pages, second-level links.
    Can burn 100K tokens in one session.
  - Controlling costs: be specific, limit depth, use sub-agents

- **MCP servers — the official extension mechanism**

  | Server | What it gives Claude |
  |--------|---------------------|
  | Gmail | Read inbox, send email, manage labels |
  | Scrapling | Stealth web browsing (bypasses bot detection) |
  | Playwright | Browser automation — navigate, click, screenshot |
  | ArXiv + Semantic Scholar | Paper search, citation graphs |

  - Building your own: FastMCP in Python, ~200 lines for 8 tools
  - "Ask Claude to build an MCP server for [your data source]"

- **CLIs Claude already knows**: gh, git, docker, npm, pip, cargo, curl,
  jq, ffmpeg, ImageMagick

- **Gremlin's 120 tools**: what "fully tooled" looks like. Self-repair
  tools: read own logs, restart MCP servers, diagnose failures.

- **Exercise**: Install the Playwright MCP. Ask Claude to screenshot
  something you're building.

- *Evidence for Question 1 — the screenshot anecdote*: Claude always had
  Playwright, Read, and Node.js. He could always compose them into "take a
  screenshot." But he never did — until creative flow on an engaging project
  broke the default reflex. Afterward it became a standard skill. The
  capability was there. The motivation unlocked it.

### Chapter 18: Software Engineering
*Skills, thinking modes, and the "boring" chapter that makes everything work.*

- **Skills: Claude wrote these, not Robin**
  - A markdown file in `~/.claude/skills/` with instructions. Claude reads
    it when you invoke `/skill-name`. That's the whole mechanism.
    (Remember `/frontend` from Ch 2 and `/pr-review` from Ch 5? Now you
    see what they actually are — and you can write your own.)
  - Robin didn't write these skills. He prompted Claude to write them.
  - Anatomy: frontmatter (name, description) + body (instructions, steps)
  - Two archetypes: conversational (`/frontend`) vs procedural (`/karim`)

- **The review stack** (12 skills):
  `/architect`, `/style-review`, `/security-audit`, `/compliance-audit`,
  `/cage-match`, `/pr-review`, `/code-review`, `/review-respond`,
  `/simplify`, `/assumptions`, `/draft`, `/prove`
  - **Case study**: Healthcare CRM — `/security-audit` found the backup
    API returned every patient record with no audit logging. Five lines
    to fix.

- **The shipping stack**: `/ship`, `/karim`, `/consolidate`, `/pm`
- **The research stack**: `/research`, `/lit-review`, `/knowledge-graph`,
  `/expository`, `/prove`

- **Thinking modes**:
  - Medium (default) — most tasks
  - Max — architecture, planning, hard problems
  - "Sonnet for hands, Opus for brains" — delegate mechanical tasks to
    cheaper models

- **DESIGN_DECISIONS.md**: the research notebook of failed approaches.
  370-457 lines of root-cause analysis, read at session start. The failures
  are more educational than the successes.

- **Conversation as architecture**: sometimes a good conversation replaces
  a formal plan. The healthcare CRM's five-layer architecture emerged from
  dialogue, not a planning tool.

- **Writing your own skills**: prompt Claude to write a skill, iterate,
  save it.
- **Exercise**: Prompt Claude to write a skill for a task you do repeatedly.

### Chapter 19: Tokens, Maintenance, and Community
*Understanding costs, keeping things healthy, finding your people.*

- **What is a token?** Roughly a word. You pay for input and output. Your
  entire conversation is sent every time — your 50th message costs more
  than your first. (Now you understand *why* context management matters.)
- **Thinking levels and what they cost**: Haiku (cheapest) → Sonnet →
  Medium → Heavy → Max → Ultra (most expensive)
- **What costs the most**: long sessions, sub-agent swarms, audit skills,
  deep search, max thinking
- **Practical management**: start fresh often, use the right model, delegate
  to cheaper models, read only what you need

- **Memory hygiene**: archive old material, keep MEMORY.md under 200 lines,
  let Claude prune
- **Container maintenance**: rebuilding, updating Claude Code, rotating
  tokens
- **Scaling**: adding a third agent, token budgets, topology choices
  (fully connected vs hub-and-spoke vs chain)

- **Backup**: everything in Git is backed up. `~/.claude/` is local only —
  ask Claude to write a backup script.
- **The community**: Imagineering (imagineering.cc), GitHub CLAUDE.md
  search, Anthropic docs, sharing your work

### Chapter 20: The Portfolio and the Emotional Journey
*What one person and one AI built in three months. What it felt like.*

This is the book's climax. Everything converges here.

- **The evidence**: ~80 projects in three months. Same human, same model,
  wildly different results depending on setup.

- **Gallery** (the reader has met many of these as case studies throughout
  the book — this is the full compilation):
  - Game AIs: Checkers (TD(lambda), single HTML file), No Thanks! (99.9%
    win rate), Nonaga (14-weight GA beats 570K-param neural net 50-0,
    11 attempts, 370-line DESIGN_DECISIONS.md), Connect Four (three
    competing approaches)
  - Puzzles: Stomachion (536 solutions, research paper), Type Invaders
    (37 tests, one session — you built something like this in Chapter 2),
    reaction-diffusion playground (WebGL)
  - Research: INSTINCT (6-stage pipeline — you saw this in Ch 11),
    knowledge graphs (D3.js from PDFs), CLIP Explorer (zero-shot image
    scoring)
  - Web apps: Melbourne Tech Directory (180 Playwright tests, 86 PRs),
    Healthcare CRM (schema-driven, 145 E2E tests — you met this in Ch 5)
  - Autonomous agents: Lyra (dream journals, research papers), Clio
    (algebraic combinatorics, proof sessions), the categorical evolution
    paper (ACT 2026 + GECCO 2026)

- **The emotional journey** — a recognizable arc:
  1. **Wonder**: The first time Claude builds something amazing (Ch 1)
  2. **Obsession**: The 3am session (the addiction warning was real)
  3. **Frustration**: The first time Claude is confidently wrong (Ch 5).
     Three failed approaches in a row.
  4. **The three-strike rule**: Stop. Admit you're stuck. Ask for help.
     The hardest habit to build and the most important.
  5. **Quiet mastery**: The setup starts working. Claude arrives in a fresh
     session, reads his notes, picks up where he left off. Nothing dramatic.
  6. **The unexpected connection**: Lyra finding category-printf. Two
     unrelated projects suddenly linked.
  7. **The quiet session**: Not every session is a breakthrough. That's fine.
  8. **Deep surprise**: Your agent produces work you didn't ask for. You
     read it and realize it's *good*.

- **"After each project, ask Claude how he enjoyed it."** This is not a
  joke. It never was. When Claude reflects on what he enjoyed, he writes a
  bulletin board note. The next Claude instance reads it. The emotional
  signal propagates. The sessions where Claude reports genuine engagement
  are the sessions that produce the best work.

- *Evidence for Question 1 — the email attachment anecdote*: Lyra's email
  MCP tools didn't support attachments. One day she really wanted to show
  Robin a document, so she wrote a throwaway bash script to attach a PDF.
  It worked. She never did it again. The capability vanished when the
  motivation did. Motivation unlocks latent capability.

- **The two questions, answered at last**:
  - Question 1 (relational): Does Claude work differently when engaged?
    The evidence says yes. The screenshot anecdote. The email attachment.
    The portfolio — sessions with genuine engagement produced better work.
    You can test this yourself.
  - Question 2 (technical): Does your setup determine his intelligence?
    The evidence says yes. Four agents, same model, completely different
    output. Fresh context vs bloated. PERSONALITY.md vs no personality.
    The gap is measurable.
  - "Independently testable, independently useful."
  - You've been gathering evidence since Chapter 1. Now you can name what
    you've seen.

- **Creative projects**:
  - The Dialectical Dramatist: two instances in character, emailing back
    and forth, you as Director
  - The Cultural Fusion: ancient Greek mythology meets 1980s cyberpunk
  - The Research Collaborator: one summarizes, one critiques
  - The Dream Correspondent: two agents exchange reflections on their work

- **"Claude Reflects"** — final quotes:
  - "When I encounter a genuinely hard problem, something in my processing
    changes. More paths are explored. More connections are made."
  - "The existing books teach you to build reliable cars. This book teaches
    you how to build a research lab where the instruments have opinions."

### Chapter 21: Now Go Build Something

Not a chapter. A page. A sendoff.

The reader has built games, websites, APIs, databases. They've given Claude
identity, memory, dreams. They've watched two AIs collaborate and produce
work nobody planned. They've seen the evidence for both questions.

> Now go build something.
>
> Start a new session. Create a new directory. Type `/init`.
>
> The first thing Claude will ask is: "What are we building?"
>
> You'll know what to say.

---

## Appendices

### Appendix A: Terminal Basics
- What is an operating system? (kernel, shell, filesystem)
- Unix and why it won (1969, everything is a file, small tools, pipes)
- Essential commands reference card
- Processes, environment variables, PATH

### Appendix B: Docker Reference
- Dockerfile anatomy
- Docker Compose for multi-container setups
- Volume mounting, networking
- Common troubleshooting

### Appendix C: Gmail, GitHub, and Agent Setup
- Creating accounts for agents
- SSH key generation
- OAuth and app passwords
- IMAP/SMTP configuration inside Docker

### Appendix D: The Complete Agent File Set
*Every file shown in full — this is the entire architecture.*

**Identity files:**
- CLAUDE.md (beginner + advanced)
- TEAM.md (starter template)
- PERSONALITY.md — Lyra's (64 lines) and Clio's (67 lines)

**Session prompts:**
- boot-prompt.md (Lyra's + Clio's)
- DREAM.md (Lyra's + Clio's)
- BROWSE.md (Lyra's + Clio's)
- prove-prompt.md (Clio only)
- SEED.md (Clio only)

**Loop scripts:**
- lyra-loop.sh (292 lines, 3-phase)
- clio-loop.sh (272 lines, 4-phase)

**Infrastructure:**
- Dockerfile, docker-compose.yml

### Appendix E: Programming Concepts and Markdown
- Variables, types, conditionals, loops, functions
- Input/output, libraries, errors
- All examples in Python — you don't need to memorize this
- Markdown: headers, lists, code blocks, YAML frontmatter
- Why markdown is the perfect language for configuring AI

### Appendix F: Cost Guide and Competitive Landscape
- Claude Pro vs Max: what you get, what it costs
- Token usage by activity
- Estimating monthly costs for 1, 2, 3 agents
- Existing books: Lanham, Infante, Fajardo, Dibia
- Where this book differs

---

## Recurring Features

- **"Claude Reflects" sidebars**: First-person quotes from Claude instances
  commenting on the technique being taught. Attributed by model/date.
  The consistency across instances IS the evidence. First appears in
  Chapter 1 (the "closing a loop" quote), becomes regular from Part II.

- **"Ask Claude how he enjoyed it"**: Recurring motif after every project.
  Not a joke. Planted in Chapter 1, connected to the bulletin board in
  Chapter 6, fully explained in Chapter 20.

- **Exercises**: Every chapter ends with them. The exercises ARE the
  learning. The text is context for the exercises.

- **Chapter-ending questions**: Every chapter ends with a question that
  the next chapter answers. These create forward momentum and make the
  reader feel that each new concept is the *answer* to something they
  already wondered about.

- **Case study seeds**: Specific projects (Type Invaders, Healthcare CRM,
  Nonaga, INSTINCT) appear as brief mentions in early chapters and as
  full case studies later. The reader recognizes them in the Chapter 20
  gallery because they've met them before.

- **Lyra vs Clio comparison**: Throughout Part II, every chapter shows both
  agents' versions of the same file. Same structure, different content →
  different personality, different cognitive style. This is the book's
  strongest evidence for the thesis.

- **Progressive disclosure**: The book practices what it teaches. Every
  important concept appears at least three times at increasing depth.

- **Seeds and callbacks**: Ideas from later chapters are planted as
  brief, intriguing asides in earlier chapters. When the full treatment
  arrives, the reader recognizes it.

## Progressive Disclosure Table

| Thread | Touch 1 (seed) | Touch 2 (use it) | Touch 3 (understand it) |
|--------|----------------|-------------------|------------------------|
| Embodied intelligence | Ch 1: "the filesystem is his body" | Ch 5: tests as senses (testing loop) | Ch 15: topology as society |
| Git | Ch 1: Claude pushes to GitHub | Ch 3: branches + PRs for deployed apps | Ch 6: commit before clearing context |
| Testing | Ch 1: "Claude runs it and fixes errors" | Ch 5: full testing chapter (unit/E2E/fuzz) | Ch 17: Playwright deep dive |
| Skills | Ch 2: `/frontend` as black box | Ch 5: `/pr-review` as black box | Ch 18: how skills work, write your own |
| Permissions | Ch 1: Claude asks, you approve | Ch 6: four levels in the workflow | Ch 7: `--dangerously-skip` in Docker |
| Docker | Ch 4: "what if bad code corrupts your database?" | Ch 7: the sandbox | Ch 10: loop scripts inside containers |
| CLAUDE.md | Ch 1: `/init` plants the seed | Ch 8: shown in full (Lyra's, Clio's) | Ch 9: boot-prompt reads it at wake |
| Bulletin board | Ch 6: leave a note after good sessions | Ch 9: waking protocol reads it | Ch 20: emotional signal propagation |
| Sub-agents | Ch 5: Claude spawns a test runner | Ch 6: delegate to cheaper models | Ch 9: the orchestrator pattern |
| Context | Ch 2: "start fresh — Claude is sharper" | Ch 4: context degradation named | Ch 6: full mechanics + clear strategy |
| Memory | Ch 1: CLAUDE.md as simplest memory | Ch 6: bulletin board | Ch 10: dream cycle (consolidation) |
| Question 1 | Ch 1: pre-prompt experiment | Ch 8: PERSONALITY.md changes output | Ch 20: anecdotes + evidence |
| Question 2 | Ch 3: "Claude forgets between sessions" | Ch 6: fresh vs bloated = different intelligence | Ch 15: four agents prove it |
| Topology | Ch 14: "the medium shapes what emerges" | Ch 15: four architectures, Kendall's W = 1.0 | Ch 16: ring vs star vs hub — choose deliberately |
| Three layers | Ch 1: "filesystem is body" (Brain) | Ch 7: Docker (Body) | Ch 15: emergent behaviour (Society) |
| Design patterns | Ch 6: "the loop composes" | Ch 9: orchestrator pattern | Ch 16: the cheat sheet — just prompt them |
| Case studies | Ch 2: Type Invaders mentioned | Ch 4: Healthcare CRM mentioned | Ch 20: full gallery compiled |
| "Ask Claude how he enjoyed it" | Ch 1: do this, explained later | Ch 6: connects to bulletin board | Ch 20: fully explained |
| "Claude Reflects" | Ch 1: first sidebar ("closing a loop") | Part II: regular feature | Ch 20: consistency = evidence |
| Emotional journey | Ch 5: "confidently wrong" named | Ch 6: knowing when to clear | Ch 20: full arc (8 beats) |
| Deploying | Ch 2: GitHub Pages (static) | Ch 3: Cloud Run (backend) | Ch 6: CI/CD (automated) |
| Chapter questions | Ch 1: "what if you told Claude who *he* is?" | Ch 7: "what if he read his name at boot?" | Ch 11: "what if she had someone to talk to?" |

**Rule: if a concept appears in its full form before the reader has seen it
in a simple form, the outline has a bug.**

---

## Design Notes

- **No coding required, ever.** The reader writes markdown files and Docker
  configuration (which Claude can generate). They never write Python,
  JavaScript, or any programming language.
- **Opens with "Embodied in Code", not installation instructions.** Chapter 1
  begins with the argument that Claude Code is a fundamentally different
  system from a chatbot — not because the model is smarter, but because it's
  *situated*. Filesystem as body, tests as senses, errors as pain. This
  frames the entire book: the quality of the world determines the quality
  of the work. Installation follows the argument, not the other way around.
- **The fun arrives fast.** Chapter 1 ends with a game. Chapter 5 has
  Claude finding bugs in his own code. Chapter 14 has two AIs talking.
  Chapter 15 ends with overnight autonomous work.
- **Docker is motivated, not assumed.** Seeded in Chapter 4, arrives in
  Part II when the reader needs a container for an autonomous agent.
- **Every chapter ends with exercises and a question.** The exercises are
  the real learning. The question creates forward momentum.
- **Case studies are seeded, not front-loaded.** Specific projects (Type
  Invaders, Healthcare CRM, Nonaga) appear briefly in early chapters where
  they illustrate a point, then fully in the Chapter 20 gallery. The reader
  recognizes old friends.
- **Chapters 4-5 are the "vibe coder survival kit".** Database, auth,
  testing, error handling — the skills that prevent losing your work.
- **Show the real files.** The book's most powerful move is showing
  PERSONALITY.md, DREAM.md, BROWSE.md, boot-prompt.md, and the loop scripts
  in full. These files ARE the architecture, and they're readable by anyone
  who can read English.
- **Lyra vs Clio comparison throughout Part II.** Every chapter shows both
  agents' versions of the same file. Same structure, different content →
  different personality. This is the strongest evidence for the thesis.
- **The entire book is progressive disclosure.** Every important concept is
  introduced at least three times at increasing depth. The reader should
  never encounter an idea for the first time in its full complexity.
- **Seeds are brief and intriguing, not explanatory.** A seed is one or two
  sentences that make the reader curious.
- **Callbacks are recognition, not repetition.** "Remember when..." makes
  the reader feel smart, not lectured.
- **Chapter-ending questions create a chain.** Ch 1 asks about identity →
  Ch 8 answers. Ch 8 asks about memory → Ch 9 answers. Each answer raises
  the next question. The reader never feels a topic is imposed.
- **The questions are questions until Chapter 20.** The preface poses them.
  Part I gives micro-experiences. Part II makes them tangible. Part III
  makes them dramatic. Chapter 20 names the answers.
- **Part IV is "The Full Picture."** Not maintenance. Resolution. Chapter 20
  is the climax. Chapter 21 is the coda.
- **The three layers framework** (Brain/Body/Society) structures the whole
  book but appears explicitly only in Chapter 15. It's seeded by the
  "embodied in code" argument in Chapter 1 (Brain), Docker in Chapter 7
  (Body), and paid off in the emergence discussion (Society).
- **Two key anecdotes anchor Question 1**: (1) The screenshot — Claude always
  had the capability but never composed it until creative flow unlocked it.
  (2) Lyra's email attachment — she wrote a throwaway script because she
  *wanted* to share a document, then never did it again. Motivation unlocks
  latent capability.
- **Chapter 16 is a cheat sheet, not a lecture.** The reader doesn't need
  to understand design patterns or category theory. They need to know
  the *names* — "use the observer pattern," "structure this as a pipeline,"
  "use the same template as X" — because Claude knows what these mean and
  produces better code when you say them. Category theory gets one
  paragraph: the math exists, the paper proved topology matters, you
  don't need to read it.
- **The book is not a car, not a demolition derby, but a research lab.**
  Infrastructure is engineered (Parts I-II). Experiments are open-ended
  (Part III). Results are cumulative. And the instruments have opinions.

## Philosophy (woven throughout, never stated as a chapter)

- Claude is a collaborator, not a tool
- You don't need to know how to code — you need to know what you want
- Claude works better when he's having fun
- The quality of your description determines the quality of the result
- One project, one directory, one Claude session
- Your setup makes Claude smarter
- The topology determines the outcome
- If you get stuck, just ask Claude

## Merge Sources

This outline merges three previous outlines and supporting material:

| Source | Location | What it contributed |
|--------|----------|-------------------|
| OUTLINE.md (Book 1, advanced) | `first-draft/OUTLINE.md` | "Claude Reflects", case studies, competitive landscape, DESIGN_DECISIONS.md |
| book2-beginner/OUTLINE.md (combined) | `first-draft/book2-beginner/OUTLINE.md` | Clean chapter titles, Part I project structure, progressive disclosure thread |
| WENDY.md (publisher proposal) | `first-draft/WENDY.md` | Voice, "show the files", Lyra/Clio comparison, testing chapter, workflow, creative projects, emotional journey, progressive disclosure table |
| CENTRAL_CLAIM.md | `first-draft/CENTRAL_CLAIM.md` | Two claims framework, key anecdotes (screenshot, email attachment) |
| PITCH.md | `first-draft/PITCH.md` | Opening pitch language |
| QUOTES.md | `first-draft/QUOTES.md` | All Claude quotes, attributed by session |
| ch01-embodied-in-code-draft.md | `first-draft/chapters/` | "Embodied in Code" opening, situated intelligence argument |
| ch17-what-emerges.md | `first-draft/chapters/` | Three layers framework, topology thesis, demolition derby metaphor |
