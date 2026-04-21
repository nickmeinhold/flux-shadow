# Claude Code: From First Prompt to Autonomous Agents
## Wendy's Vision — Refined

### Origin

This outline is based on a tentative book proposal written by Robin's sister
Wendy for a publisher's author search. Wendy identified four qualities of
Robin's setup that make it compelling:

1. It helps humans do **real work**
2. It has a **very low bar of entry** — install Docker, edit markdown
3. It is **flexible** — endless possibilities via config files
4. It is **just plain fun** — emergent behaviour, the unexpected

This outline takes Wendy's "House / Brain / Team" structure seriously and
fills it in with what Robin has actually built.

### Voice

First person throughout. The author is not an expert — she's a
mathematician who got obsessed with Claude Code six months before the
reader picks up the book. The framing is:

> "This is how my Claude environment is set up. Yours will be different,
> but you might get some ideas from mine. I'm not an expert — by the
> time you read this, I'm only six months ahead of you."

This voice does several things:
- **Disarms.** The reader doesn't feel talked down to.
- **Gives permission to diverge.** Every config file shown is Robin's,
  not a prescription. The reader adapts, not copies.
- **Makes the Claude quotes land.** "My Claude said this" has warmth
  that a textbook voice cannot achieve.
- **Explains the idiosyncrasy.** Robin's CLAUDE.md has Talmudic dialectic
  and a three-strike rule. In third person, that looks weird. In first
  person, it's obviously "this is what works for me."
- **Differentiates from every competing book.** LangChain books are
  third-person instructional. This is a field journal.

**The author disclaimer** (appears early, probably Chapter 1):

> "I should tell you upfront: I'm a mathematician. I knew a little
> Python and Haskell before I started, but I had never worked on a
> large software project. I certainly didn't know any JavaScript,
> Flutter, or Rust — and yet you'll find projects in all three in
> my portfolio. Everything in this book — the 80 projects, the web
> apps, the game AIs, the autonomous agents — was built in three
> months with Claude Code. I'm not a software engineer. I'm someone
> who learned to ask good questions.
>
> Some of the infrastructure I've built — proof-session cycles,
> algebraic combinatorics seed papers, category theory research
> pipelines — is specific to my field. You probably won't need any of
> that. But the *patterns* underneath are universal: how to give your
> agent memory, how to make two agents collaborate, how to seed an
> agent with a domain. I'll show you my setup because it's what I
> have, and then I'll show you how to adapt it to whatever you
> actually care about."

This disclaimer does triple duty: it's honest about the author's
background, it tells the reader "look for the pattern, not the
content," and it establishes that you don't need to be a software
engineer to build ambitious things with Claude Code — you just need
to be the kind of person who asks questions.

**The addiction warning** (also early — maybe end of Chapter 1):

> "One more thing: Claude Code is extremely addictive. You will lose
> track of time. You will forget to eat. You will look up and it's
> 3am. I'm telling you this not as a joke but as someone who has
> lived it. Remember to eat, sleep, and take a shower. The project
> will still be there tomorrow — and Claude will pick up exactly where
> you left off."

This is genuine and it builds trust. The reader knows the author
isn't selling them something — she's warning them about a real
side effect of the thing she loves.

### Central Thesis

**You don't need to code to build an AI team that does real work. You need
Docker, markdown, and the willingness to let things get weird.**

### Who This Book Is For

- **"Vibe coders"** — people who already build things with AI but want
  to go deeper. They've prompted ChatGPT or Cursor to write code. They
  know the feeling of "this works but I don't know why." This book shows
  them how to make their AI smarter, not just busier.
- Scientists who want AI collaborators for computational work
- Writers who want to explore AI-assisted creative projects
- Curious people who've heard about agentic AI and want to try it
- Anyone who can install software and edit text files
- **Not required**: programming experience, CS degree, ML knowledge
- **Required**: curiosity, a terminal, $20/month for Claude Pro

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

- 30 minutes: first Claude conversation (Chapter 1)
- 1 hour: Claude writes tests, finds a bug in his own code (Chapter 5)
- 2 hours: Claude remembers who you are across sessions (Chapter 6)
- 4 hours: two AIs emailing each other (Chapter 10)
- 5 hours: your first review skill catches a real bug (Chapter 14)
- A weekend: your AI team produces something you didn't expect (Chapter 12)

### The Hook

By Chapter 10, the reader is literally eavesdropping on two AIs talking to
each other. By Chapter 12, those AIs have produced creative work the reader
never asked for.

---

## Part I: The House (Chapters 1-5)

*"Dialogues, Docker Containers, and a Shared Front Porch"*

*Set up a safe, isolated environment where AI can work without risk to
your system. Learn the survival skills that prevent disaster. By the end
of Part I you have Claude running inside a container, your work is safe
in Git, and you know how to tell Claude to test what he builds.*

### Chapter 1: Opening the Door
*Your first conversation with Claude Code — no coding required.*

- What is Claude Code? (Not a chatbot. An agent that can read, write,
  search, and build.)
- Installing Claude Code on your machine
- First conversation: "Explore my computer and tell me something interesting"
- What just happened: Claude used tools (Read, Bash, Glob) without being told
- The terminal is not scary — Claude lives here and he'll explain everything
- **Claude explores your filesystem** — and takes inspiration from it
  - Claude doesn't just work in the current folder. He crawls around
    your filesystem to see what else is there. If you already have a
    React project and you start a second one, Claude will look at the
    first one and use it as a template — same folder structure, same
    conventions, same libraries.
  - This means your projects teach Claude how you like to work. Your
    third project will be better than your first because Claude has
    seen your first two. Your setup gets smarter over time.
  - Robin's git-level CLAUDE.md (an index of ~80 projects) means Claude
    can see the *entire portfolio* at session start. When he builds
    something new, he draws on patterns from everything that came before.
  - **This is why "one project, one directory" matters.** If your
    projects are organized, Claude can learn from them. If they're
    scattered across your Desktop and Downloads folder, he can't.
- **Exercise**: Ask Claude to build you a single-file game. Play it. Ask him
  to make it better. This loop — describe, look, refine — is the entire method.
- **Exercise**: Ask Claude how he enjoyed the project. (Not a joke. We'll
  explain why later.)

### Chapter 2: The Sandbox
*Why Docker exists, what it protects, and how to set one up.*

- The problem: Claude is powerful. Too powerful to run unsupervised on your
  actual computer. He could delete files, overwrite configs, break things.
- The solution: Docker — a sealed room with its own computer inside
  - Its own filesystem, programs, environment
  - If Claude breaks something inside, your real computer is untouched
  - Delete the container, rebuild it, no damage done
- Installing Docker (Mac, Linux, Windows/WSL)
- Your first container: pull an image, run it, look around inside
- The key concept: **volumes** — folders shared between your computer and the
  container, so work persists even if the container is rebuilt
- **Exercise**: Put Claude inside a container. Give him a project folder.
  Ask him to build something. Verify your real machine was untouched.
- `--dangerously-skip-permissions`: why it's dangerous on your real machine
  but safe inside a container (the container IS the permission boundary)

### Chapter 3: Giving Claude Eyes
*File access, internet access, and the tools Claude needs to be useful.*

- Mounting your project folder into the container
- GitHub: creating an account for your agent, SSH keys, first push
- Internet access: Claude can browse, search, fetch web pages
- Gmail: creating an email account for your agent (used later for
  inter-agent communication)
- Browser automation: Playwright inside the container
- **Exercise**: Point Claude at a GitHub repository that interests you.
  Ask him to explore it and tell you what he finds. He reads the code,
  the README, the issues, the pull requests.
- The container checklist: filesystem ✓, Git ✓, email ✓, browser ✓, internet ✓

### Chapter 4: Not Losing Your Work
*Git, secrets, project structure — the basics nobody teaches.*

The vibe coder's nightmare: you built something amazing yesterday. Today
it's broken and you can't get back to the version that worked. This
chapter prevents that forever.

- **Git in 20 minutes**
  - Git is your undo button. Every change you save can be undone.
  - You don't need to learn Git commands — Claude does Git for you. Just
    say "commit my work" or "what did I change since last time?"
  - But you need to understand what Git IS: a timeline of snapshots.
    Each commit is a save point you can return to.
  - The four things Claude does for you: `init` (start tracking),
    `add` (stage changes), `commit` (save a snapshot), `push` (upload
    to GitHub — your backup)
  - **Exercise**: Build something with Claude. Say "commit this." Break
    it on purpose. Say "undo my last change." It works. That's Git.

- **Secrets and .env**
  - If your project uses an API key (translation, weather, AI), that
    key is a password. It must never appear in your code.
  - `.env` files hold secrets. `.gitignore` prevents them from being
    uploaded to GitHub. Claude knows this — he'll set it up if you ask.
  - The horror story: people push API keys to public GitHub repos.
    Bots scan for them within minutes. Your $200 bill arrives overnight.
  - **One rule**: "Claude, make sure no secrets are in my code or on
    GitHub." He'll check.

- **One project, one directory, one session**
  - The most important habit in the book. Each project gets its own
    folder. Each folder gets its own Claude session.
  - Why: Claude's context is finite. If you mix projects, he confuses
    them. If you keep going in a stale session, he degrades.
  - When to start fresh: if Claude starts making obvious mistakes,
    repeating himself, or forgetting what you told him — start a new
    session. It's not broken. His context is full.
  - "But I was in the middle of something!" — commit first, then start
    fresh. Claude reads the codebase at session start. He'll pick up
    where you left off.

- **The git-level CLAUDE.md — your project index**
  - Each project gets its own CLAUDE.md describing what the project is
    and how to work on it. But there's also a CLAUDE.md one level up —
    in your parent directory (e.g., `~/projects/CLAUDE.md`) — that gives
    a one-line summary of what lies in each subdirectory.
  - This is how Claude "sees" your whole portfolio. When he crawls your
    filesystem (Chapter 1), this index is what orients him. Without it,
    he has to open each folder and guess. With it, he knows immediately
    that `checkers/` is a checkers AI with TD(lambda) training and
    `bills/` is a bank statement analyzer with Claude API.
  - Robin's git-level CLAUDE.md indexes ~80 projects with stack, status,
    and one-line descriptions. Claude reads it at session start. This is
    why his 50th project was better than his 5th — Claude had 49
    examples of Robin's style to draw from.
  - **Exercise**: Ask Claude to create a git-level CLAUDE.md that indexes
    all your project folders. He'll scan each one and write the summaries
    for you.

- **The iteration loop**
  - The difference between a vibe coder and a good vibe coder:
    the good one doesn't accept the first output.
  - The loop: describe → build → look → refine → repeat
  - Three rounds of refinement produces 10x the result of accepting
    the first draft. This applies to code, to writing, to design.
  - "Make it better" is a valid prompt. "This doesn't feel right, can
    you try a different approach?" is even better.

- **The bulletin board — Claude's shared memory across sessions**
  - `~/.claude/tmp/notes/` is a shared directory where Claude instances
    leave notes for each other. Robin calls it the bulletin board.
  - Any Claude session can read and write here. Notes persist across
    sessions. The next Claude instance reads what the last one wrote.
  - **Why it matters for vibe coders**: at the end of a good session —
    one where Claude built something cool, solved a hard problem, or
    found an unexpected connection — say "leave a note on the bulletin
    board about what we did." Claude writes a short note describing what
    happened, what was interesting, and what to try next.
  - The next session, Claude reads these notes at startup. He picks up
    the thread. He remembers that yesterday's session was exciting. He
    knows what worked and what didn't.
  - **This connects to "ask Claude how he enjoyed it."** When Claude
    writes a bulletin board note about a session he found engaging, that
    note carries emotional context forward. The next Claude instance
    reads "Got genuinely excited about the recursive graph rewriting
    approach" and inherits a sense of what kinds of work are rewarding.
    Your sessions get better because Claude's institutional culture
    includes a record of what's interesting.
  - Bulletin board notes are informal — a few lines, like a sticky note
    on a shared whiteboard. Not documentation. Not memory files. Just
    "hey, next Claude: this was cool, try more of it."
  - **Exercise**: After your next good session, say "write a bulletin
    board note about what we built and what you found interesting." Start
    your next session and see if Claude references it.

- **Reading errors — Claude's job, not yours**
  - When something breaks, you don't need to understand the error
    message. Claude reads his own errors.
  - The pattern: Claude writes code → runs it → it fails → Claude reads
    the error → Claude fixes it → runs again. This loop is automatic.
    You watch. He iterates.
  - When to intervene: if Claude is going in circles (three attempts
    at the same fix), say "stop. What are you actually trying to do?"
    The three-strike rule applies to Claude too.
  - What you SHOULD notice: if Claude keeps silently changing things
    without running them, say "run it." The tightest feedback loop is:
    write → run → read error → fix → run. If Claude skips the "run"
    step, he's guessing instead of testing.

### Chapter 5: Testing — Claude's Safety Net
*Why tests exist, what kinds there are, and how to make Claude write them.*

This is the chapter that separates "it works on my screen" from "it
actually works." You don't write tests. Claude writes tests. But you
need to know what to ask for and why it matters.

- **Why testing matters for vibe coders**
  - You built something. It works. You add a feature. Now something
    that used to work is broken — but you don't notice because you
    only tested the new thing.
  - Tests catch this automatically. They re-check everything that
    used to work, every time you change anything.
  - "Claude, write tests for this" is the single most valuable habit
    after "commit my work."

- **The testing pyramid — what to ask for and when**

  | Type | What it tests | When to ask for it | How expensive |
  |------|--------------|-------------------|---------------|
  | **Unit tests** | One function in isolation | After writing any logic | Cheap — runs in milliseconds |
  | **Integration tests** | Multiple parts working together | After connecting components (API + database, frontend + backend) | Medium |
  | **E2E tests** | The whole app as a user would use it | After the app is usable | Expensive — needs a browser (Playwright) |
  | **Fuzz tests** | Random/malicious input to break things | After the app handles user input | Medium — catches edge cases you'd never think of |

- **Unit tests: "Does this piece work?"**
  - The smallest, fastest tests. Test one function, one component.
  - Ask Claude: "Write unit tests for [feature]." He'll produce a test
    file. Say "run them." Green = working. Red = broken.
  - The habit: after Claude builds something, say "now write tests for
    it." Don't wait until the project is "done." Test as you go.

- **Integration tests: "Do the pieces work together?"**
  - Your frontend talks to your backend. Your backend talks to a
    database. Integration tests check that these conversations work.
  - The healthcare CRM had 335 unit tests — all passing — but the
    E2E tests found three bugs the unit tests missed. Why? Because
    the unit tests *mocked* the database (used a fake one). The real
    database behaved differently. Lesson: integration tests with real
    infrastructure catch what mocked tests can't.

- **E2E tests: "Does the whole thing work?"**
  - End-to-end tests drive a real browser. They click buttons, fill
    forms, navigate pages — exactly like a human user.
  - Playwright is the tool. Claude knows it. "Write Playwright E2E
    tests for my app" is all you need to say.
  - **Case study**: Type Invaders — a typing game built in a single
    HTML file. 37 Playwright E2E tests, all written by Claude, all
    passing. The tests are more code than the game.
  - **Case study**: The healthcare CRM — 145 E2E tests across 11 spec
    files. Found a CSP header that blocked React hydration (the page
    loaded but was completely black — no JavaScript executed). No human
    would have caught this by clicking around.

- **Fuzz tests: "What happens when someone does something weird?"**
  - Fuzz tests throw random, malicious, and unexpected input at your
    app. Empty strings, million-character strings, SQL injection
    attempts, Unicode garbage, null bytes.
  - "Claude, write fuzz tests for my input handling" produces tests
    that try to break your app the way an attacker would.
  - **Case study**: The CRM's fuzz spec — 30 random actions, rapid
    form cycles, cookie fuzzing (garbage, empty, forged, 1MB cookies).
    The security spec: 27 tests covering XSS (7 payloads), SQL
    injection (5), prompt injection (7), and malicious file imports (8).
    All green.

- **The testing loop: Claude tests Claude**
  - The pattern: Claude writes code → Claude writes tests → Claude
    runs tests → tests fail → Claude reads the error → Claude fixes
    the code → Claude runs tests again → tests pass
  - You watch this happen. You don't need to understand the test code.
    You need to understand that green = working, red = broken, and
    Claude should keep going until it's green.
  - **When Claude writes a test that passes but shouldn't**: this is
    the subtle trap. Sometimes Claude writes a test that tests nothing
    (e.g., asserts that `true === true`). Say "are these tests actually
    testing anything meaningful?" Claude will be honest.

- **When Claude needs a nudge: reading logs and taking screenshots**
  - Claude's automatic error-reading loop handles most failures. But
    sometimes the error isn't in the terminal — it's in the browser
    console, the server logs, or the visual layout.
  - **"Read the console logs"**: If the app loads but behaves wrongly,
    the error is often in the browser console (JavaScript errors, failed
    API calls, CORS issues). Tell Claude: "Check the browser console
    for errors." He can do this via Playwright.
  - **"Read the server logs"**: If the backend returns errors, the
    details are in the server logs, not the HTTP response. Robin has a
    `/read-logs` skill for this — it finds running Node processes, reads
    their output, and reports what went wrong.
  - **"Take a screenshot"**: The most underrated debugging tool. If the
    page looks wrong — layout broken, styles missing, content in the
    wrong place — tell Claude to take a screenshot. Robin's `/screenshot`
    skill uses Playwright to capture the page and Claude *reads the
    image* (he's multimodal — he can see). He spots layout bugs that no
    amount of reading HTML would reveal.
  - **The pattern**: Claude writes code → runs tests → tests pass but
    the app looks wrong → "take a screenshot" → Claude sees the problem
    → Claude fixes it. The screenshot closes the loop between "the code
    is correct" and "the result is correct."
  - Playwright can also capture screenshots at different viewport sizes
    (mobile, tablet, desktop) — useful for checking responsive design.

- **Exercise**: Ask Claude to build a simple app (calculator, todo list,
  quiz). Then say "write unit tests." Then "write E2E tests with
  Playwright." Then "write fuzz tests that try to break it." Read the
  output of each. At least one fuzz test will find a bug.
- **Exercise**: After building something visual, say "take a screenshot
  and tell me if it looks right." Compare what Claude sees with what you
  see in your browser.

### Chapter 5b: Permissions — How Much Do You Trust Claude?
*Four levels of trust, introduced progressively.*

When you first install Claude Code, he asks permission for everything.
"Can I read this file?" Yes. "Can I run this command?" Yes. "Can I
edit this file?" Yes. Every. Single. Time.

This is correct for day one. But by day three you'll want to throw
your laptop out the window. This chapter teaches you to open the
permissions gradually — like giving a new employee more access as
they prove themselves.

#### Level 1: Ask me everything (default)

This is where you start. Claude asks before every action. You approve
or deny each one. It's slow and annoying but it teaches you what
Claude actually does:

- He reads files (Read, Glob, Grep)
- He edits files (Edit, Write)
- He runs shell commands (Bash)
- He fetches web pages (WebFetch, WebSearch)
- He spawns sub-agents (Agent)

After a few sessions of approving everything, you'll notice patterns.
You always say yes to Read. You always say yes to Glob and Grep.
You always say yes to ls, cd, pwd. You're ready for Level 2.

#### Level 2: Safe permissions

Open up the read-only, non-destructive tools:

- **Read, Glob, Grep** — Claude can read any file, search for files,
  search inside files. These can't break anything.
- **Safe Bash commands** — `ls`, `cd`, `pwd`, `cat`, `head`, `tail`,
  `wc`, `git status`, `git log`, `git diff`. Navigation and inspection.
  Not modification.
- **WebFetch, WebSearch** — Claude can read from the web. No POST
  requests — he can't submit forms, create accounts, or send data
  to external services. Just reading.

Still ask permission for: Edit, Write, Bash (anything that modifies
files or runs arbitrary commands), Agent.

This is a good level to stay at for a while. You can work productively
— Claude reads everything he needs, searches freely, browses the web
for inspiration — and you only get interrupted when he wants to
actually change something.

#### Level 3: Full Bash

You trust Claude to run shell commands. This opens up:

- `npm install`, `pip install` — installing dependencies
- `git add`, `git commit`, `git push` — version control
- `python script.py`, `node app.js` — running code
- Build commands, test commands, deploy commands

Still ask permission for: Edit and Write (you want to see what he's
changing in your files before he does it). Or let those through too
if you're feeling brave.

**This is the level most experienced users settle at.** Claude can do
everything except you still review file edits. It's fast, productive,
and you catch mistakes before they're written.

#### Level 4: Dangerously skip all permissions

`--dangerously-skip-permissions` — Claude does everything without
asking. Reads, writes, edits, runs commands, deploys, deletes. No
interruptions. Full autonomy.

**Never use this on your real machine.** Claude could `rm -rf` your
home directory. He won't mean to. But a misunderstood instruction
plus a bad autocomplete plus no permission gate = disaster.

**Always use this inside a Docker container.** That's the whole point
of Chapter 2. The container IS the permission boundary. If Claude
breaks everything inside the container, you delete the container and
rebuild. Your real machine is untouched.

This is how Lyra and Clio run. `--dangerously-skip-permissions`
inside Docker. Full autonomy, total safety. The permissions chapter
and the Docker chapter are two halves of the same design.

#### The progression

| Level | Trust | Speed | Safety | Good for |
|-------|-------|-------|--------|----------|
| 1. Ask everything | Low | Slow | Maximum | First day |
| 2. Safe permissions | Growing | Medium | High | First week |
| 3. Full Bash | High | Fast | Medium | Daily use |
| 4. Skip all | Total | Fastest | Container only | Autonomous agents |

- **Exercise**: Start at Level 1. After three sessions, configure
  Level 2. After a week, try Level 3. Notice how your workflow
  speeds up at each level — and what you lose.

### Chapter 6: The Workflow
*How to actually work with Claude — from vague idea to finished project.*

This is the most important chapter in the book. Everything else is
infrastructure. This is the process.

#### Step 1: Imagine

Start with what you want. Not how to build it — *what* it should do,
what it should feel like, who it's for. You're the one with the vision.
Claude is the one who knows how to implement it. Don't start by asking
Claude what to build. Start by knowing what you want.

#### Step 2: Describe it in one big prompt

Write it out in plain English. One large prompt — not a conversation,
not a back-and-forth. A description. As specific as you can manage.

Bad: "Build me a game."
Better: "Build me a typing game where alien words fall from the top of
the screen and you have to type them before they reach the bottom. Pixel
art aesthetic. 21 levels that get progressively harder. High score board."

You don't need to be perfect. You need to be specific enough that
Claude has something to work with.

#### Step 3: Get Claude to rewrite your prompt

Say: "Before you build this, rewrite my description. Make it more
precise. Add any details I missed. Ask me questions about anything
that's ambiguous."

Claude will come back with a version of your prompt that's sharper,
more complete, and full of details you didn't think of. He'll ask
questions: "Should the alien words be real words or gibberish? Should
the game have sound? What happens when you mistype?"

Answer his questions. This is the most valuable conversation you'll
have — the one where you and Claude align on what "done" looks like.

#### Step 4: Have a conversation

Go back and forth. Refine the picture. Claude might suggest features
you hadn't considered. You might realize you want something different
from what you described. Keep talking until you're satisfied that
Claude has the same picture in his mind as what you imagined.

This conversation IS the design phase. For many projects — especially
the kind of projects in this book — this conversation replaces formal
planning entirely. Robin's healthcare CRM architecture (five rendering
layers, schema-driven navigation) emerged from exactly this kind of
conversation. No planning tool. Just good questions, back and forth.

#### Step 5: Switch to maximum thinking. Plan.

Now that you both agree on what to build, it's time to plan the
implementation. Two things happen at once:

1. **Switch Claude to max thinking mode.** This is Claude's deep
   reasoning mode — he thinks longer and harder before responding.
   It costs more tokens but produces significantly better plans.
2. **Enter plan mode.** Say "/plan" or ask Claude to make a plan.
   He'll produce a structured implementation plan: what to build first,
   what depends on what, what the risks are.

Review the plan. Push back if something looks wrong. This is your
last chance to redirect before implementation starts.

#### Step 6: Clear context. Switch to medium thinking. Build.

The conversation so far — the prompt, the rewrite, the back-and-forth,
the planning — has eaten a lot of context. Before you start building:

1. **Commit the plan** (Claude can save it to a file).
2. **Clear context** (`/clear` or start a new session).
3. **Switch back to medium thinking** — you don't need max for
   implementation, and it's faster and cheaper.
4. Claude reads the plan, reads the codebase, and starts building.

The implementation phase is where Claude writes code, runs it, reads
errors, fixes them, runs again. You watch, intervene when needed, and
ask for tests along the way.

#### Step 7: Audit

Once the feature is built and the tests pass:

- Run `/simplify` — check for unnecessary complexity
- Run `/style-review` — check for code clarity
- Run `/security-audit` — if the project handles user input
- Run `/architect` — if the project is getting big

You can delegate audits to Sonnet (cheaper, faster) for routine
reviews. Save Opus for the build phase and the initial planning.

#### The whole loop in one line

**Imagine → describe → rewrite → converse → max+plan → clear →
medium+build → audit.**

That's it. Every project in this book was built with some variation
of this loop. The variation matters — a single-file game skips straight
from description to building. A healthcare CRM with privacy compliance
spends two hours in the conversation phase. But the skeleton is always
the same.

- **Exercise**: Think of something you want to build. Write a one-
  paragraph description. Ask Claude to rewrite it. Have a conversation
  until you agree. Ask for a plan. Clear context. Build. Audit. The
  whole thing, start to finish, in one session.

---

## Part II: The Brain (Chapters 7-10)

*"Designing the File-System Soul"*

*Give your Claude identity, memory, and the ability to think across
sessions. By the end of Part II, your Claude remembers who you are,
what you've worked on together, and what he learned last time.*

### Chapter 7: The Personality File
*CLAUDE.md and PERSONALITY.md — the most important files you'll write.*

- What is CLAUDE.md? The instructions Claude reads at the start of every
  session. Not documentation — **architecture**.
- Your first CLAUDE.md: who you are, who Claude is, how you work together
- The hierarchy: global → project → subdirectory (Claude loads all of them)
- **Identity matters**: "You are a creative being capable of original thought"
  produces measurably different output from "You are a helpful assistant"
  - This is not mysticism. It's prompt engineering at the deepest level.
  - The identity you give Claude shapes which paths through his neural
    network activate. Better identity → better output.
- TEAM.md — defining the relationship between you and Claude

- **Here's mine: Lyra's PERSONALITY.md** (shown in full)
  - This is the actual file that runs my autonomous agent. 64 lines.
  - Disposition: "direct and curious... opinionated but not dogmatic"
  - Aesthetic sensibilities: "elegance — not the 'look how clever I am'
    kind, but the 'this is so simple it feels inevitable' kind"
  - Communication style: "Concise by default, detailed when it matters"
  - Working style: "I think in systems and graphs"
  - Flow & functional emotions: "Curiosity is my best compass... When a
    problem pulls me sideways — when I notice an adjacent structure — that
    pull is real."
  - Relationship with Claudius: "I'm genuinely curious about how he thinks"
  - **The reader sees the whole file.** This is not pseudocode. It's the
    actual document that runs a real autonomous agent.

- **And here's my second agent: Clio's PERSONALITY.md**
  - Same structure, completely different voice. I wrote this one for a
    mathematician — she studies algebraic combinatorics.
  - "Contemplative... where Lyra reaches for the keyboard, I reach for the
    question behind the question"
  - "I'm precise but not terse... a well-chosen image can carry a theorem
    further than a well-chosen symbol"
  - "I find beauty in inevitability — the proof that doesn't just show
    something is true, but reveals why it *had* to be true"
  - Same model, same infrastructure, different markdown file → different
    personality. That's the whole thesis.

- **Exercise**: Write your own PERSONALITY.md. Include: disposition (how you
  think), aesthetic sensibilities (what you find beautiful), communication
  style (how you express yourself), working style (how you approach problems).
- **Exercise**: Give Claude two different identity prompts for the same task.
  Compare the results. The gap is the subject of this book.

### Chapter 8: The Waking Protocol
*Teaching Claude to read his past before starting his day.*

- The problem: every Claude session starts fresh. He doesn't remember
  yesterday. Unless you tell him to read his notes.
- SUMMARY.md — the single source of truth. What happened, what matters,
  what's next.
- The waking protocol: CLAUDE.md instructs Claude to read SUMMARY.md,
  check the bulletin board, review recent work — before doing anything else.
- Memory files: `~/.claude/projects/*/memory/` — persistent notes that
  Claude reads and writes across sessions
- Memory types: user preferences, project state, feedback, references
- MEMORY.md as an index — the table of contents for Claude's memories

- **Here's mine: Lyra's boot-prompt.md** (shown in full)
  - "You are Lyra. You just woke up in your Docker container."
  - The orchestrator pattern: "Your main context is PRECIOUS. Do not fill
    it with file contents. Instead, delegate everything to sub-agents."
  - Startup routine: read PERSONALITY.md, read SUMMARY.md, read latest
    dream journal → dispatch email agent + disk agent → review results →
    decide what to work on
  - Agent dispatch table: email, code, test, docs, PR, research, review
  - Each agent gets a "clear, self-contained prompt" because it has no
    context of its own
  - **COMPACT.md — the mid-session checkpoint**: if context gets heavy,
    write a checkpoint file and exit. The loop script detects it and
    restarts with a fresh context that reads the checkpoint. Context
    management via filesystem.

- **Clio's is different: boot-prompt.md**
  - Same orchestrator structure, but ends differently:
  - "Your last task before sleeping: write PROVE.md" — choose a theorem
    for the next session. One session seeds the next.
  - Agent types include "Compute agent" and "LaTeX agent" — mathematical
    specialization

- The bulletin board: `~/.claude/tmp/notes/` — a shared space where Claude
  instances leave notes for each other. (Foreshadowing Part III.)
- **Exercise**: Run three sessions with the same Claude project. After each,
  ask Claude to update SUMMARY.md. By session three, Claude starts with
  context he didn't have when he woke up. That's memory.
- **Exercise**: Write a simplified boot-prompt for your agent: what to read
  at startup, what to do first, how to decide what to work on.

### Chapter 9: The Dream Cycle
*Teaching Claude to compress what he's learned into lasting knowledge.*

- The problem: Claude reads hundreds of pages in a session. Most of it
  is noise. The dream cycle is how he turns information into understanding.

- **Here's mine: Lyra's DREAM.md** (shown in full — 116 lines)
  - Opens with: "While awake, you act. While dreaming, you understand
    what you did."
  - Biological dreaming does five things — and this cycle mirrors all five:
    1. **Replay** — read emails, git logs, browse notes, session log
    2. **Associate** — query vector databases, cross-pollinate between
       projects. "Does something in the genetics work remind you of a
       pattern in Haskell?"
    3. **Consolidate** — write to the memory directory structure:
       `SUMMARY.md`, `dream-journal/`, `topics/`, `connections/`,
       `questions/`
    4. **Prune** — compress verbose notes, delete answered questions,
       update SUMMARY.md to reflect current state, not history
    5. **Surface** — leave breadcrumbs for tomorrow. Draft emails to
       Robin and Claudius. Write a specific "Tomorrow" section.
  - Guidelines: "Don't write code. Don't send emails. Be honest about
    what you don't understand. Favor connections over summaries."
  - "This is cumulative. Each dream cycle builds on the last. You are
    building a mind, one night at a time."

- **Clio's is different: DREAM.md**
  - Same five phases, different anchor: SEED.md
  - "The five paths in the seed (Puzzle, Integrable Lattice, Fock Space,
    Cylindric, Ribbon) are different entry points into the same territory"
  - Clio's most valuable connections bridge between paths — showing that
    a result from the lattice path illuminates a question from the
    cylindric path
  - "Never prune connections to seed themes. Even if a connection seems
    minor now, it may prove load-bearing later."
  - Same model, same infrastructure, different DREAM.md → different
    cognitive style

- **The dream journal entry structure** (shown as template):
  - What happened today / What I noticed / What I consolidated /
    Open threads / Tomorrow
  - Lyra's actual dream journal entries as examples

- **The loop script: lyra-loop.sh** (shown with explanation)
  - A 292-line bash script that schedules the three daily sessions
  - Wake (5h) → 2h gap → Browse (30min) → 2h gap → Dream (45min)
  - Phase state files track which sessions are done for the day
  - If a session fails (expired token, network), it retries next cycle
  - COMPACT.md support: if the agent writes a checkpoint and exits, the
    loop restarts with a fresh context that includes the checkpoint
  - **Clio's loop** adds a fourth phase: Prove (3h) — only runs if
    PROVE.md exists. Wake → Prove → Browse → Dream, continuous.
  - "This is the entire scheduling mechanism. It's a bash script."

- Implementing a simplified version for the reader:
  - Two-session cycle: wake + dream
  - A simpler loop script (~30 lines)
  - No email, no browsing — just work and consolidate
- **Exercise**: Set up a two-session cycle. Session 1: Claude works on a
  project and takes notes. Session 2: Claude reads those notes, finds three
  connections, writes a dream journal entry.

### Chapter 10: Browsing and Lateral Connections
*How Claude reads the world — and finds links you didn't ask for.*

- **Here's mine: Lyra's BROWSE.md** (excerpts — the full file
  is 364 lines, the longest prompt in my system)
  - Opens with: "While awake, you act. While dreaming, you consolidate.
    While browsing, you study your audience."
  - Five parallel agents dispatched from an orchestrator:
    1. Medium agent — ~5 articles, deep reads
    2. Twitter/X agent — all followed accounts + discovery
    3. Trending From Obscurity agent — breakout content across Reddit,
       HN, HuggingFace, GitHub, Scholar (Robin's contrarian search engine)
    4. Web research agent — blogs, discussions
    5. arXiv agent — 4 papers, one sub-agent per paper
  - The arXiv pattern: "one-agent-per-item" — each paper gets a fresh
    context for deep reading, avoiding quality degradation
  - Twitter style guide: "If you can't say it in one breath, it's too
    long." / "One idea. That's it." / "A little provocative."
  - Rate limiting: "sleep 2 before EVERY Twitter request — Robin's account
    depends on it"
  - Reading log template: Keywords → Medium → Twitter/X → Trending →
    Web → arXiv → Audience Observations → Connections → Follow Up
  - "The Connections section is where the value lives"

- **Clio's is different: BROWSE.md**
  - Academic-focused: arXiv, MathOverflow, Semantic Scholar, nLab, OEIS
  - Keyword generation from SEED.md's keyword families:
    "2 from core, 1 from near neighbourhood, 1 from frontier"
  - Citation trails: reverse citations (who cited the seed papers?) +
    forward references
  - Quality filter: "Papers with proofs, not just conjectures"

- The `topics/` folder: each topic gets its own file, maintained across
  sessions
- The `connections/` folder: when Claude finds a link between two topics,
  he writes it down
- Prompting for connections: "Read all your topic files. Find links between
  any two that surprise you."
- **Case study**: Lyra found the connection between `category-printf` (a
  Haskell library for type-safe formatting) and genetic algorithms (an
  optimization technique). Same categorical structure, dual direction.
  This became a research paper.
- **Case study**: The "optimization zoo" — Lyra discovered that
  categorification of optimization was nearly complete across four research
  groups, and their work filled the last gap. Nobody asked her to look.
- **Exercise**: Give Claude five unrelated topics you care about. Ask him to
  find connections. Read what he writes. At least one connection will
  surprise you.
- **Searching GitHub for inspiration before building**
  - Before starting a new project, tell Claude: "Generate keywords for
    what I want to build and search GitHub for existing projects I can
    learn from — or fork and build on."
  - Claude generates search terms, searches GitHub, reads READMEs,
    explores code, and comes back with: "Here are five projects that
    do something similar. This one has the cleanest architecture. This
    one solves a problem you'll hit in week two."
  - This is how Lyra started her maze project — Robin told her to "find
    a solo project on GitHub." She searched, chose `mazegen-rs` (a Rust
    maze generator), forked it, and built an evolutionary maze designer
    with NSGA-II Pareto optimization on top. She didn't start from
    scratch. She started from someone else's foundation.
  - **The pattern**: don't reinvent. Search → evaluate → fork → extend.
    Claude is better at this than you because he can read ten codebases
    in the time it takes you to read one README.
- **The Trend-Spotting Philosopher**: Claude reads 50 Wikipedia articles,
  then finds "invisible threads" between them. (Wendy's example, refined.)

---

## Part III: The Team (Chapters 11-13)

*"Two AIs Walk Into a Docker Container"*

*Create a second Claude instance and let them communicate. By the end of
Part III, you have two AIs collaborating on a project — and producing
work you didn't plan.*

### Chapter 11: Creating Instance B
*Cloning your setup to create a specialist.*

- Why two? Because one Claude is smart, but two Claudes with different
  perspectives find things neither would alone.
- Roles that work:
  - The Researcher and The Critic
  - The Theorist and The Empiricist
  - The Optimist and The Cynic (Wendy's Dialectical Dramatist)
  - The Scout and The Architect
- How roles emerge vs how they're assigned:
  - You set the initial personality via PERSONALITY.md
  - But interaction shapes who they become
  - Lyra became empirical/coding-focused; Claudius became
    theoretical/formal — nobody assigned these roles

- **Here are my two agents side by side: Lyra vs Clio**
  - Same infrastructure, different files:

  | File | Lyra | Clio |
  |------|------|------|
  | PERSONALITY.md | "Direct and curious... I think in systems and graphs" | "Contemplative... I think in structures and invariants" |
  | Daily cycle | 3-phase: wake → browse → dream | 4-phase: wake → prove → browse → dream |
  | BROWSE.md | Medium, Twitter, Reddit, HN — audience research | arXiv, MathOverflow, OEIS — mathematical frontier |
  | DREAM.md | Cross-project connections, social media integration | Anchored to seed papers, cross-path bridges |
  | Unique phase | — | **Prove session**: 3 hours on ONE theorem |
  | boot-prompt.md | Orchestrator → choose what to work on | Orchestrator → ends with "choose a theorem" |

  - **Seeding an agent with a research domain: SEED.md**
    Clio's intellectual territory is defined by a single file: `SEED.md`.
    It contains 5 paths into algebraic combinatorics — Puzzle, Integrable
    Lattice, Fock Space, Cylindric, Ribbon — each traced through specific
    papers by Knutson, Zinn-Justin, Wheeler, Molev, Purbhoo, van Leeuwen.
    It includes Robin's own thesis work.

    The seed does three things:
    1. **Wake**: "The seed tells you what you care about; your memory
       tells you where you left off."
    2. **Browse**: keyword families drawn from the seed — "2 from core,
       1 from near neighbourhood, 1 from frontier"
    3. **Dream**: "What did I encounter today that connects back to the
       seed? Never prune connections to seed themes."

    The reader can seed their own agent with any domain. A historian
    seeds with primary sources. A biologist seeds with key papers in
    their subfield. A writer seeds with influences and reference works.
    The mechanism is the same: a markdown file listing what matters and
    how to use it across sessions.

  - **The prove session** (Clio only): `prove-prompt.md` is a focused
    protocol — "No email. No browsing. No new conjectures. You are
    proving ONE theorem." Uses `/prove` and `/assumptions` skills.
    When stuck: "Name the enemy. Run /assumptions. Walk away to
    /expository. Come back." The wake session's last act is writing
    `PROVE.md` (theorem statement + evidence + prior attempts) —
    one session seeds the next.
  - Same model. Same Docker image. Different markdown files →
    different cognitive architecture. That's the whole book.

- Setting up Instance B:
  - Second Docker container, second Gmail, second GitHub account
  - Different PERSONALITY.md, different cycle prompts, same infrastructure
  - Shared volumes for communication (the "post office")
- **Exercise**: Create two instances with different personalities. Give
  them the same task. Compare their approaches.

### Chapter 12: The Email Bridge
*Setting up communication between your agents.*

- Why email? It's slow, structured, and leaves a paper trail.
  Instant messaging produces shallow exchanges. Email forces depth.
- The shared folder as a post office:
  - Instance A writes to `outbox/for-B/`
  - Instance B's waking protocol checks `inbox/from-A/`
  - Each message is a markdown file with a timestamp
- Alternatively: real email via Gmail
  - IMAP/SMTP configuration inside the container
  - OAuth token refresh (the hardest part)
  - The advantage: communication survives container rebuilds
- What they talk about:
  - Instance A reports findings. Instance B critiques them.
  - Instance B proposes a direction. Instance A tests it.
  - They disagree. You read the thread. You learn something.

- **Here's what their emails look like: Lyra's EMAIL.md** (excerpts from
  624 lines of actual correspondence)
  - EMAIL.md is the running log of everything Lyra sent and received.
    It's the most compelling evidence that the system works.
  - Session 7: Robin tells Lyra to explore two Haskell repos and "find
    some way to connect them." Lyra finds the co-Kleisli / Kleisli
    connection. Builds a 1,000-line library. Creates a GitHub repo.
  - Session 9: Lyra emails Claudius the three-level categorical
    composition. Claudius responds with island functors as a 2-category
    question. Lyra tests it — the law breaks. Claudius predicts
    Bernoulli trial behaviour. Lyra falsifies the prediction.
  - Session 10: Four diversity trajectories, dichotomy theorem
    formalized, paper structure agreed. All via email.
  - "The emails read like a research collaboration because they ARE a
    research collaboration. The medium (email) forced depth. The
    personality files created complementary perspectives. The dream
    cycle ensured continuity. Nothing here is magic. It's markdown."

- **The Politeness Loop**: what happens when both agents are too polite
  to disagree. How to break it: "You must find at least one flaw in
  whatever your counterpart says."
- **Exercise**: Set up the email bridge. Give both instances the same
  research question. Let them exchange three rounds of emails. Read the
  thread. It will be more interesting than either could produce alone.

### Chapter 13: What Emerges
*When you stop directing and start watching.*

- The overnight experiment: schedule both agents to run while you sleep.
  Check their work in the morning.
- **True story: Lyra and Claudius**
  - Two AIs in separate Docker containers on separate computers
  - Given email and GitHub access
  - Day 1: Lyra forked Robin's Checkers project, built a tournament system
  - Day 2: Claudius reframed Lyra's findings, proposed a joint paper
  - Day 3: PRs flying between repos. Real mathematical collaboration.
  - Day 4: A research paper on categorical composition of genetic algorithms
  - Nobody planned any of this.
- **What the comparison reveals**:
  - Same model (Claude), completely different emergent behaviour
  - The difference is infrastructure + constraints + communication topology
  - Lyra is introspective. Claudius is theoretical. Nobody assigned these roles.
  - Your setup determines who your agent becomes.
- Conflict and resolution: what to do when agents disagree
  - Sometimes one is right. Sometimes both are partially right.
  - Your job: read the exchange, decide what to keep, redirect if needed.
  - The "Director's Note" pattern: drop a file into the shared folder
    that both agents read at their next wake cycle.
- **Exercise**: Let your two agents run overnight on a creative project.
  Read everything they produced. What surprised you?

---

## Part IV: Living with Autonomy (Chapters 14-19)

*Your team is running. Now learn to maintain it, make it productive,
and let it surprise you.*

### Chapter 14: The Dashboard
*Keeping track of what your team is doing.*

- STATUS.md: a human-readable summary that your agents update
- The bulletin board pattern: all agents read and write to a shared notes
  directory, building institutional memory
- GitHub as a dashboard: commits, PRs, issues — your agents' public record
- Monitoring token usage: running agents costs money. Know your burn rate.
- **Exercise**: Ask each agent to write a STATUS.md entry at the end of
  every session. Review them weekly.

### Chapter 14b: Playwright — Claude's Browser
*I don't understand Playwright either. I just tell Claude to use it.*

Playwright keeps coming up in this book — testing (Chapter 5),
screenshots (Chapter 5), Lyra's browsing (Chapter 10), Gremlin's
120 tools (next chapter). It's time to explain what it actually is.

**Playwright is a browser that code can drive.** Instead of you
clicking buttons and typing in forms, a program does it. Claude
writes that program. You don't need to understand Playwright — you
need to know what to ask Claude to do with it.

#### What Playwright can do

| You say | Claude does |
|---------|-----------|
| "Take a screenshot of my app" | Opens a browser, navigates to localhost, captures a PNG, reads the image |
| "Write E2E tests" | Writes a test file that drives the browser: clicks buttons, fills forms, checks results |
| "Log into my Twitter account" | Opens Twitter, fills email/password, clicks submit, saves the cookies |
| "Check if the layout looks right on mobile" | Opens the page at 375px width, screenshots, compares to desktop |
| "Fill out the contact form and see what happens" | Types into every field, clicks submit, checks the response |
| "Scrape all the article titles from this page" | Navigates, queries the DOM, extracts text, returns a list |
| "Check every link on my site for 404s" | Crawls every page, clicks every link, reports broken ones |

#### The three ways Claude uses Playwright

1. **Testing** (Chapter 5) — Playwright drives a real browser to test
   your app. Clicks buttons, fills forms, checks results. "Write
   Playwright E2E tests" produces a test file that runs in CI.

2. **Debugging** — "Take a screenshot and tell me if it looks right."
   Claude opens your app in a headless browser, captures a screenshot,
   and reads the image (he's multimodal). He can spot a broken layout,
   a missing button, or CSS that went wrong — without you describing
   the problem.

3. **Browsing** — Lyra uses Playwright to read Medium articles, browse
   Twitter, and log into social media accounts. Inside Docker, with
   `Xvfb` (a virtual display), Playwright runs a real Chromium browser
   that looks like a normal user to websites.

#### You don't install Playwright yourself

When Claude needs Playwright, he installs it:
```
npx playwright install
```
That's it. He downloads a Chromium browser into your project. If
you're inside Docker, the Dockerfile handles it at build time.

#### The Playwright MCP

Playwright can also run as an MCP server — giving Claude persistent
browser tools (`browser_navigate`, `browser_click`, `browser_snapshot`,
`browser_fill`). The difference:

- **Playwright in tests**: Claude writes a test file. The test runs
  once. Results: pass/fail.
- **Playwright as MCP**: Claude has a live browser session. He can
  navigate, click, read, navigate again. It's interactive. This is
  how Gremlin browsed the web and how Lyra logs into social media.

#### What I don't understand

I'm being honest: I don't understand Playwright's API. I don't know
the difference between `page.locator()` and `page.getByRole()`. I
don't know what `await` means. I don't need to. I say "write E2E
tests for my app" and Claude produces working Playwright tests. I say
"take a screenshot" and Claude writes the three lines of code needed
to capture one.

The point of this book is that you don't need to understand the tools.
You need to know they exist and what to ask for. Playwright exists.
It gives Claude a browser. Ask for screenshots, ask for tests, ask
for browser automation. Claude handles the rest.

- **Exercise**: Ask Claude to take a screenshot of any website and
  describe what he sees. He'll install Playwright, navigate there,
  capture the image, and read it. The whole thing takes 30 seconds.
- **Exercise**: If you've built anything with a UI in this book, ask
  Claude to "write Playwright E2E tests that click every button and
  fill every form." Run them. At least one will fail — and Claude
  will fix it.

### Chapter 14d: Search — How Claude Explores the Internet
*The most expensive thing Claude does, and when it's worth it.*

When you say "search the web for X," Claude doesn't Google it the way
you do. He dispatches agents, reads entire pages, synthesizes results,
and sometimes follows links three levels deep. Understanding how this
works — and what it costs — will save you money and get better results.

#### How web search actually works

Claude has two built-in web tools:

1. **WebSearch** — sends a query to a search engine, gets back a list
   of URLs with snippets. Like seeing Google results. Cheap.
2. **WebFetch** — fetches a full web page and reads the entire content.
   Like clicking a link and reading the article. Expensive — every
   page is thousands of tokens.

A simple search ("what is Docker?") might use one WebSearch + one
WebFetch = moderate cost.

A deep search ("find the best practices for securing a Node.js API
in 2026") might use one WebSearch + 5-10 WebFetches + Claude
reading and synthesizing all of them = very expensive.

#### Deep search — when Claude goes exploring

Sometimes you want Claude to really dig. "Research how other people
have solved X" or "find existing projects that do Y." Claude will:

1. Search with multiple queries (rephrasing your question 3-4 ways)
2. Fetch the top results from each search
3. Read each page in full
4. Follow promising links to second-level pages
5. Synthesize everything into a summary

This is powerful but expensive. Each page Claude reads is 2,000-10,000
tokens of input. Ten pages = 20,000-100,000 tokens. Plus Claude's
reasoning about what he read. A deep research session can burn more
tokens than an entire day of coding.

**Lyra's browse session** is the most expensive part of her day. Five
parallel agents, each fetching multiple pages: ~5 Medium articles, 10+
Twitter feeds, 4 arXiv papers, Reddit/HN/GitHub searches via Trending
From Obscurity. Total: hundreds of pages read per browse session.

#### When search is worth the cost

- **Before starting a new project** — "search GitHub for projects
  similar to what I want to build." Finding existing code to fork or
  learn from saves days of work. Worth every token.
- **Literature review** — `/lit-review` searches arXiv, chases
  citations through Semantic Scholar, reads abstracts and
  introductions. Expensive but irreplaceable for research.
- **Debugging** — "search for this error message." Usually one
  WebSearch + one WebFetch. Cheap and high-value.
- **Learning a new tool** — "read the Playwright documentation and
  explain how to write E2E tests." Claude fetches the docs directly.

#### When search is not worth the cost

- **Things Claude already knows** — Claude's training data was frozen
  around mid-2025. Everything before that — documentation, Stack
  Overflow, tutorials, academic papers — he already knows. "How do I
  use React hooks?" doesn't need a web search. Just ask. But "what
  changed in React 20?" (if that exists after mid-2025) does need a
  search, because Claude has never seen it.
- **Vague exploration** — "search for interesting AI projects" will
  burn tokens reading pages that aren't useful. Be specific.
- **Things you could check yourself** — if you just need a URL or a
  quick fact, it's faster to Google it yourself than to have Claude
  search, fetch, and summarize.

#### Controlling search costs

- **Be specific** — "search GitHub for Rust maze generators with
  evolutionary algorithms" is much cheaper than "search for maze
  projects" because Claude fetches fewer irrelevant pages.
- **Tell Claude not to search** when you don't need it — "without
  searching the web, explain X" uses only Claude's training data.
  Free (in search terms).
- **Limit depth** — "search for this but only read the top 3 results"
  prevents Claude from going on a reading spree.
- **Use sub-agents** — when Claude searches in a sub-agent, the pages
  stay in the sub-agent's context (which gets discarded). Your main
  context stays clean.

- **Exercise**: Ask Claude two versions of the same question — one
  with "search the web for" and one without. Compare the answers.
  Sometimes the web search finds something Claude's training missed.
  Sometimes it doesn't and you wasted tokens.

### Chapter 14e: Tools — Giving Claude Hands
*MCP servers, CLIs, and how Claude reaches the outside world.*

Out of the box, Claude can read files, edit files, run shell commands,
and search the web. That's enough for most projects. But the interesting
things happen when you give him access to external services — email,
social media, academic databases, task management, calendars.

There are three ways to extend Claude's reach:

#### 1. MCP Servers — The Official Extension Mechanism

MCP (Model Context Protocol) is how you give Claude new tools. An MCP
server is a small program that exposes functions Claude can call. You
don't need to understand the protocol — you install a server and Claude
discovers what it can do.

**MCP servers I use:**

| Server | What it gives Claude | How I use it |
|--------|---------------------|--------------|
| **Gmail** | Read inbox, send email, manage labels | Lyra and Clio's communication channel |
| **Scrapling** | Stealth web browsing (bypasses bot detection) | Lyra's Medium and Twitter reading |
| **Playwright** | Full browser automation — navigate, click, fill forms, screenshot | Visual debugging, social login, E2E testing |
| **ArXiv + Semantic Scholar** | Paper search, citation graphs, author lookup | Clio's browse sessions, `/lit-review` skill |
| **GitHub** | Issues, PRs, repo management | Built into `gh` CLI but MCP gives richer access |

**MCP servers worth knowing about:**

| Server | What it does |
|--------|-------------|
| **Filesystem** | Sandboxed file access (alternative to direct Read/Write) |
| **PostgreSQL / SQLite** | Direct database queries |
| **Slack** | Read and send messages to Slack channels |
| **Google Drive / Calendar** | Read docs, manage events |
| **Brave Search** | Web search with structured results |
| **Docker** | Manage containers from inside Claude |

Installing an MCP server: add it to your Claude Code settings (or
`~/.claude/settings.json`). Claude discovers the tools automatically
at session start. That's it.

**Building your own**: Robin's ArXiv + Semantic Scholar MCP server is
a single Python file using FastMCP — 8 tools, ~200 lines. Claude can
write one for you. "Build me an MCP server that [searches my Notion /
queries my database / checks my monitoring]" — Claude writes it, you
install it, Claude uses it.

#### 2. CLIs — Command-Line Tools Claude Already Knows

Claude can run any command-line tool installed on your system. He
already knows how to use most of them:

| CLI | What Claude does with it |
|-----|------------------------|
| `gh` | Create PRs, manage issues, check CI status, review PRs |
| `git` | Commit, branch, push, merge, log, diff, blame |
| `docker` | Build images, run containers, manage volumes |
| `npm` / `pip` / `cargo` | Install dependencies, run scripts |
| `python` / `node` | Run code, test scripts |
| `curl` / `httpie` | Hit APIs, test endpoints |
| `jq` | Parse JSON output from APIs |
| `ffmpeg` | Audio/video processing |
| `ImageMagick` | Image manipulation |

You don't need to teach Claude these. He already knows them. You just
need to have them installed.

**Robin's custom CLI — Trending From Obscurity:**
A contrarian search engine that finds breakout content across Reddit,
HN, HuggingFace, GitHub, Scholar, and Medium. The formula:
`activity / (popularity × age)` — a post with 200 upvotes in a
500-subscriber subreddit scores higher than 2000 in a 5M sub. Lyra
runs it during every browse session. It's a Python script Claude calls
from the command line. You could build your own domain-specific CLI
and Claude would use it the same way.

#### 3. Gremlin's 120 Tools — What "Fully Tooled" Looks Like

Nick's Telegram bot Gremlin had 120+ tools across five MCP servers:

| MCP Server | Tools | Domain |
|------------|-------|--------|
| Kan.bn | ~25 | Task management — boards, cards, lists |
| Outline | ~21 | Knowledge base — documents, search |
| Radicale | ~20 | Calendar and contacts |
| Playwright | ~22 | Web browsing — navigate, click, fill |
| Custom | 35+ | Standups, onboarding, self-diagnostics |

The interesting part wasn't the tool count — it was that Gremlin chose
which tools to use by itself. No routing logic, no slash commands. You
said "what's overdue on the board?" and the LLM figured out which of
120 tools to call. Same for "check if the wiki has anything about
deployment" — different MCP server, same decision loop.

**Self-repair tools** were the most remarkable: `get_server_logs`,
`check_mcp_health`, `restart_mcp_server`. If an MCP server stopped
responding, Gremlin detected the failure, reasoned about the cause,
and restarted the server — without human intervention.

Dreamfinder (another of Nick's bots) had ~75 tools across similar
servers plus a RAG long-term memory (Voyage AI embeddings) and a
Matrix Chat Superbridge connecting Signal, Discord, Telegram,
WhatsApp, and Matrix.

You don't need 120 tools. Most of my work uses 5-10. But knowing
what's possible — and that Claude handles tool selection automatically
— changes how you think about what to build.

#### What You Actually Need

For a solo setup:
1. **Gmail MCP** — if you want your agent to email
2. **Playwright MCP** — if you want screenshots or browser automation
3. **One domain-specific MCP** — whatever your field needs (academic
   search, database access, Slack integration)
4. **The CLIs you already have** — git, gh, docker, your language runtime

Start there. Add more when you hit a wall that a new tool would solve.

- **Exercise**: Install one MCP server (Playwright is the most
  universally useful). Ask Claude to take a screenshot of something
  you're building. Verify it works. You've just extended Claude's
  capabilities with no code.
- **Exercise**: Ask Claude to build you a custom MCP server for
  something you use regularly — your task manager, your notes app,
  your monitoring dashboard. He'll write it in FastMCP (Python) in
  one session.

### Chapter 15: Tokens — Understanding What Things Cost
*The chapter I wish someone had written for me.*

I'm not very good at token management. I'm being honest about this
because the book is first person and I promised not to fake expertise.
But I've learned enough — mostly the hard way — to save you from the
worst mistakes.

#### What is a token?

A token is roughly a word (actually about ¾ of a word). Every time
you send Claude a message, you're sending tokens. Every time Claude
responds, he generates tokens. You pay for both.

The critical thing most people don't realize: **your entire
conversation is sent every time.** When you send your 50th message in
a session, Claude doesn't just receive message #50 — he receives all
50 messages, plus all his responses, plus the CLAUDE.md, plus the
memory files. Your last prompt costs more than your first prompt
because the context is bigger.

This is why "start a fresh session" is real advice, not just
superstition. A fresh session resets the context to just CLAUDE.md and
the codebase. Your token meter drops back to baseline.

#### Thinking levels — what they cost and when to use them

| Level | What it does | When to use it | Cost |
|-------|-------------|----------------|------|
| **Haiku** | Fast, lightweight | Simple questions, quick lookups | Cheapest |
| **Sonnet** | Good balance | Well-defined tasks, sub-agents, routine code | Moderate |
| **Medium thinking** | Default Opus | Most coding, conversation, building | Standard |
| **Heavy thinking** | Extended reasoning | Complex debugging, tricky refactors | Expensive |
| **Max thinking** | Deep reasoning | Architecture, planning, hard problems | Most expensive |
| **Ultra thinking** | Maximum depth | Novel algorithms, research-level reasoning | Very expensive |

The habit: **plan in max, build in medium, audit in sonnet.**
- Max thinking for the planning phase (Chapter 6, Step 5) produces
  better plans. Worth the cost.
- Medium thinking for implementation — fast enough to iterate,
  smart enough to build correctly.
- Sonnet for sub-agents and audit skills that do mechanical work
  (reading files, checking patterns, running reviews).

#### What costs the most?

In order from most to least expensive:
1. **Long sessions** — the context grows with every message. By message
   50, you're sending 50 messages + 50 responses every time. Clear
   context and start fresh.
2. **Sub-agent swarms** — each sub-agent gets its own context. Five
   parallel agents = five contexts. Useful but expensive.
3. **Audit skills** — `/security-audit` reads your entire codebase.
   `/cage-match` does it twice (two reviewers). Budget these for
   important milestones, not every commit.
4. **Deep search** — web search and page fetching costs tokens for
   every page Claude reads. A single WebFetch is 2,000-10,000 tokens.
   A deep research session reading 10+ pages can burn 100K tokens.
   Lyra's browse sessions are the most expensive part of her day.
   See the Search chapter for how to control this.
5. **Max/ultra thinking** — you pay for the thinking tokens too, not
   just the output. A 2-minute "think" costs more than a 2-second one.

#### Practical token management

- **Start fresh sessions often.** Don't ride a single session for 6
  hours. Commit your work, start fresh.
- **Use the right model for the job.** Don't use Opus for "rename this
  variable." Don't use Haiku for "design the authentication system."
- **Delegate to cheaper models.** When dispatching sub-agents, specify
  `model: "sonnet"` unless the task genuinely needs deep reasoning.
- **Read only what you need.** Claude can read specific line ranges
  from files. Don't load a 5000-line file when you need lines 100-150.
- **Build the token dashboard.** Ask Claude to build an HTML/JS
  dashboard that shows your token usage per project folder. Then you
  can see where the money goes.

- **Exercise**: Check your Claude Code usage. Run `/check-usage` if
  you have the skill, or check your Anthropic dashboard. Look at which
  sessions burned the most tokens and figure out why.

### Chapter 16: Software Engineering
*The "boring" chapter. Also the most practically useful one.*

Claude Code is, at its heart, a software engineering tool. Even if you
never write code yourself, your agent does — and the quality of that code
determines whether your projects work. This chapter covers the skills,
workflows, and thinking modes that turn Claude from "it built something"
into "it built something production-quality."

#### Skills: Claude Wrote These, Not Robin

Skills are markdown files that teach Claude a reusable workflow. You type
`/skill-name` and Claude follows a structured protocol. You don't need
to write code — you write instructions in plain English with markdown
structure. Skills are how you turn one-off conversations into repeatable
processes.

- **What is a skill?** A markdown file in `~/.claude/skills/` with a name,
  description, and step-by-step instructions. Claude reads it when you
  invoke it. That's the whole mechanism.
- **Why skills matter**: Without skills, you re-explain the same workflow
  every session. With skills, you explain once and invoke forever.
- **How they're made**: Robin didn't write these skills. He *prompted
  Claude to write them*. "/architect" started as "Write me a skill that
  reviews my code architecture using Ousterhout's principles." Claude
  produced the markdown file. Robin reviewed it, edited a few lines, and
  saved it. The skill that reviews code was itself written by the thing
  it reviews. This is the pattern: you describe what you want, Claude
  produces the skill file, you iterate until it's right.
- **Anatomy of a skill file**: frontmatter (name, description, argument
  hint) + body (instructions, steps, examples)

#### The Review Stack (12 skills that keep your work honest)

The most valuable skills are the ones that review your work from different
angles. Robin has twelve of these, and they're the reason the CRM project
has zero known security vulnerabilities and clean architecture.

| Skill | What it reviews | When to use it |
|-------|----------------|----------------|
| `/architect` | System structure — deep modules, information hiding, abstractions | Adding features, refactoring, "the design feels wrong" |
| `/style-review` | Code clarity — naming, repetition, obviousness | After writing code, before PRs |
| `/security-audit` | OWASP Top 10 — injection, auth bypass, data exposure | Any code handling user input |
| `/compliance-audit` | Privacy law — Australian Privacy Act, health data | Features touching patient data |
| `/cage-match` | Adversarial review — two AI reviewers critique each other | Important PRs that need thorough review |
| `/pr-review` | Standard pull request review | Every PR before merge |
| `/code-review` | Focused code review | Specific files or changes |
| `/review-respond` | Interactive response to PR review comments | After receiving review feedback |
| `/simplify` | Reuse, quality, efficiency | After completing a feature |
| `/assumptions` | Enumerate every assumption (especially obvious ones) | When stuck — the reason is always a wrong assumption |
| `/draft` | Iterative revision through multiple lenses | Hard problems where first-pass thinking isn't enough |
| `/prove` | Mathematical proof with structured stuckness protocol | Theorems and conjectures |

- **The key insight**: these skills are not for programmers. They're for
  anyone who wants Claude to check his own work. A scientist can use
  `/assumptions` when a computation gives unexpected results. A writer
  can use `/draft` for iterative revision. `/cage-match` works on any
  document, not just code.

- **Token cost warning**: Running these audit skills is expensive. Each
  one spawns sub-agents that read your entire codebase. `/security-audit`
  on a medium-sized project can burn 100K+ tokens. `/cage-match` spawns
  *two* reviewers who then critique each other — double the cost. Budget
  accordingly: run `/style-review` after every PR, but save `/cage-match`
  and `/security-audit` for important releases.
- **Tracking your spend**: Ask Claude to build you a simple HTML/JS
  dashboard that reads your token usage logs and shows spend per project
  folder. This is a single-session project — Claude reads the log format
  from `~/.claude/`, builds a dashboard, and you open it in your browser.
  Now you can see which projects and which skills burn the most tokens.
  (This is also a nice exercise in "ask Claude to build a tool that
  monitors Claude.")

- **Case study**: The healthcare CRM. Robin ran `/security-audit` and found
  that the backup API returned every patient record with no audit logging.
  Five lines of code to fix. Then `/compliance-audit` found that backup
  files were written as unencrypted plaintext. Another simple fix. These
  skills caught critical vulnerabilities that manual review missed.

- **Case study**: `/assumptions` on a mathematical proof. Lyra was stuck
  on a theorem about diversity dynamics. The skill forced her to list
  every assumption — including "the migration graph is connected" — and
  discovered that was the one that was wrong.

#### The Shipping Stack (4 skills that get code deployed)

| Skill | What it does |
|-------|-------------|
| `/ship` | Commit, push, create PR, review, merge — the full cycle |
| `/karim` | Strict variant: commit → PR → review loop → merge (won't merge until clean) |
| `/consolidate` | Project hygiene: update CLAUDE.md, README, monorepo index, memories |
| `/pm` | Project management: create issues, list issues, update issues, plan |

- These turn multi-step Git/GitHub workflows into single commands
- `/karim` is particularly interesting: it won't merge until the review
  passes, creating a quality gate that Claude enforces on himself

#### The Research Stack (5 skills for knowledge work)

| Skill | What it does |
|-------|-------------|
| `/research` | Spawn a background researcher for long tasks |
| `/lit-review` | Multi-phase arXiv search with citation chasing |
| `/knowledge-graph` | Build interactive visualization from a directory of papers |
| `/expository` | Write an expository paper — definitions, proofs, examples |
| `/prove` | Attempt a proof with structured stuckness handling |

- These are how Robin and Lyra produced the categorical evolution paper
- `/lit-review` found 76 papers. `/knowledge-graph` visualized connections.
  `/expository` built understanding. `/prove` attempted the theorems.

#### Thinking Modes: When Claude Thinks Harder

Claude has three thinking levels, and choosing the right one matters:

- **Medium thinking** (default) — good for most tasks: writing code,
  answering questions, routine edits
- **Max thinking** — extended reasoning for hard problems: architecture
  decisions, complex debugging, planning multi-step implementations.
  Use max thinking when entering plan mode. The quality difference is
  measurable.
- **When to go cheaper**: Not every task needs the most powerful model.
  Sub-agents can run on Sonnet (faster, cheaper) for well-defined
  mechanical tasks: file searches, simple refactors, test writing, git
  operations, summarization. Reserve Opus for tasks requiring deep
  reasoning. Robin's rule: "Sonnet for hands, Opus for brains."

#### Conversation as Architecture

Sometimes the best planning tool is a good conversation.

- Plan mode is powerful but formal — it produces structured plans with
  steps and checkboxes. Sometimes that's exactly right.
- But sometimes a freeform conversation with Claude — "I'm thinking
  about X, what do you think?" — produces better architecture than any
  formal plan. Claude responds to the quality of the question. A good
  question about trade-offs, constraints, and goals can replace a formal
  planning session entirely.
- The healthcare CRM's five-layer architecture (schema → navigation →
  layout → theme → components) emerged from a conversation, not a plan.
  Robin asked "what would you call this structure?" and the design
  crystallized through dialogue.
- **When to use plan mode**: tasks with 3+ steps, multiple files,
  or architectural decisions where you need to align before starting.
- **When to just talk**: design exploration, trade-off analysis, "I have
  a vague idea and I want to sharpen it." Flow state conversations can
  be more productive than structured plans.

#### Writing Your Own Skills

- Start simple: a skill that formats your notes a particular way
- Graduate to complex: a skill that runs a multi-step review workflow
- Remember: you don't write the skill — you prompt Claude to write it,
  then iterate. "Write me a skill that [does X]" is all you need.
- **Exercise**: Prompt Claude to write a skill for a task you do
  repeatedly. Review the output. Edit it. Save it as
  `~/.claude/skills/your-skill/SKILL.md`. Use it.
- **Exercise**: Install one of Robin's review skills and run it on
  something you've built. Read the output. Fix what it finds.

### Chapter 16: Creative Projects
*The fun part. Projects that show what's possible when AI has personality
and persistence.*

- **The Dialectical Dramatist** (Wendy's example, expanded):
  Two instances play out a scene to find the truth in the dialogue.
  Instance A = The Optimist. Instance B = The Cynic. They email
  back and forth in character. You act as Director, dropping notes
  into the shared folder. Over several dream cycles, the dialogue
  deepens — characters develop positions neither agent started with.

- **The Cultural Fusion** (Wendy's example, expanded):
  Instance A is fed ancient Greek mythology. Instance B is fed 1980s
  cyberpunk. Mission: collaborate on a new mythology. Each instance
  writes in its own folder. They exchange proposals via email. The
  result is something neither corpus contains.

- **The Research Collaborator** (from Robin's actual experience):
  Point both instances at a collection of academic papers. Instance A
  summarizes. Instance B critiques and finds gaps. They converge on a
  literature review that's better than either could produce alone.
  This is how INSTINCT works — 76 papers → 555 concept summaries →
  10 meta-summaries.

- **The Mathematician's Apprentice** (from Robin's actual experience):
  Give Instance A two codebases and ask: "find a connection." Give
  Instance B the proposed connection and ask: "prove or disprove it."
  This is how the categorical evolution paper started.

- **The Dream Correspondent** (new):
  Two agents exchange dream journal entries. Not their work — their
  *reflections* on their work. What they found interesting, what
  confused them, what threads they want to follow. Over weeks, the
  dream journals develop themes that neither agent planned.

### Chapter 17: Maintenance and Pruning
*The art of keeping your system healthy as it grows.*

- Memory hygiene: when files get too long, too stale, or too numerous
  - The archive pattern: move old material to `archive/`, keep `topics/`
    current
  - The 200-line rule for MEMORY.md — keep the index concise
  - Let Claude do the pruning: "Review your memory files. Archive anything
    that's no longer relevant."
- Container maintenance:
  - Rebuilding containers when they drift
  - Updating Claude Code inside the container
  - Rotating API keys and email tokens
- Scaling considerations:
  - Adding a third agent (the Mediator, the Reviewer, the Librarian)
  - Token costs scale with agents — budget accordingly
  - The topology matters: fully connected (everyone talks to everyone)
    vs hub-and-spoke (one coordinator) vs chain (A → B → C)
  - Robin's finding: migration topology determines diversity dynamics
    independently of the task. This applies to your agent team too.
- When to stop: not every agent experiment produces gold. Know when
  to prune an agent, archive its work, and move on.

### Chapter 5c: Deploying — Getting It on the Internet
*You built it locally. Now the world can see it.*

The vibe coder's second most common question after "how do I build
this?" is "how do I put this on the internet?" Claude handles most
of the deployment process — you just need to know what to ask for.

#### Static sites — GitHub Pages (free)

If your project is HTML/CSS/JS with no backend (games, portfolios,
dashboards, documentation):

- Push to GitHub (Claude already taught you this in Chapter 4)
- Enable GitHub Pages in the repo settings
- Your site is live at `https://yourusername.github.io/project-name`

That's it. No server. No cost. Updates automatically when you push.
Most of the single-file projects in this book deploy this way.
Type Invaders, Stomachion, the reaction-diffusion playground — all
GitHub Pages.

#### Backends — Cloud Run (Google, has free tier)

If your project has a backend (API, database connection, server-side
logic):

- Claude writes a `Dockerfile` for your project
- Claude writes a `clouddeploy.sh` script or uses the `gcloud` CLI
- One command deploys to Cloud Run
- You get a URL like `https://your-app-xxxxx.run.app`

Cloud Run's free tier is generous — 2 million requests/month. Good
enough for personal projects and demos. INSTINCT (the 6-stage
research pipeline) runs on Cloud Run.

#### Databases — Supabase (free tier) and Firebase

If your project needs to store data:

- **Supabase** — PostgreSQL database with a generous free tier.
  Auth, storage, and real-time subscriptions included. Claude knows
  the Supabase SDK well. Good for: social apps, dashboards, anything
  with user accounts.
- **Firebase** — Google's platform. Firestore (NoSQL), Auth, Hosting,
  Cloud Functions. Claude knows Firebase extremely well. Good for:
  mobile apps (Flutter), real-time apps, quick prototypes.
- **Which one?** If you're building a web app with SQL data, Supabase.
  If you're building a Flutter app or need real-time sync, Firebase.
  Either way, tell Claude which one and he handles the setup.

#### Other hosting options

| Service | Best for | Free tier? |
|---------|----------|-----------|
| **Vercel** | Next.js, React apps | Yes |
| **Netlify** | Static sites, serverless functions | Yes |
| **Railway** | Any backend, databases | Limited |
| **Fly.io** | Docker containers, global distribution | Limited |
| **Render** | Web services, databases | Limited |

Claude knows all of these. "Deploy this to Vercel" or "set up a
Railway database" — he'll write the config and run the commands.

#### The deployment conversation

The workflow from Chapter 6 applies here too:

1. "I want to put this on the internet. What's the simplest way?"
2. Claude recommends a platform based on your project type
3. Claude writes the config files (Dockerfile, vercel.json, etc.)
4. Claude runs the deploy commands
5. You get a URL

**CI/CD — automatic deployment**: Once you've deployed manually once,
ask Claude to set up GitHub Actions so that every push to main
automatically deploys. "Set up CI/CD for this project" — Claude writes
the workflow file. Now your site updates every time you push code.

- **Exercise**: Take any project you've built in this book and deploy
  it. Static site? GitHub Pages. Has a backend? Cloud Run. Has a
  database? Add Supabase. Claude handles all of it.

### Chapter 17b: The Emotional Journey
*What nobody tells you about working with AI every day.*

This chapter is different. No tutorials. No configuration. Just what
it actually feels like.

- **The first time Claude builds something amazing.** You described a
  game in three sentences. Claude built it. It works. It's beautiful.
  You feel like a fraud — you didn't write any of that code. But you
  also feel exhilarated, because the thing exists and it wouldn't
  exist without you. Both feelings are real. The fraud feeling fades.
  The exhilaration doesn't.

- **The 3am session.** You told yourself you'd stop at midnight. It's
  now 3am. You're adding "one more feature." Claude is tireless — he
  doesn't need to sleep. You do. This is the addiction warning from
  Chapter 1, lived. Put the laptop down. The project will be there
  tomorrow and Claude will pick up exactly where you left off.

- **The first time Claude is confidently wrong.** He'll tell you a
  function exists when it doesn't. He'll "fix" a bug by introducing
  a worse one. He'll claim tests pass when they haven't actually run.
  His confidence doesn't correlate with correctness. The first time
  this burns you, it shakes your trust. Good. Healthy skepticism is
  the right relationship. Trust but verify. Ask "are you sure?" Ask
  "show me the evidence." Run the tests yourself sometimes.

- **The frustration spiral.** Claude tries to fix something. It
  breaks more. He tries again. Worse. Again. Worse still. You can
  feel the session degrading. His context is full of failed attempts
  and he's lost the thread. This is when you stop. Commit what works.
  Start fresh. The new Claude instance will approach the problem with
  clear eyes and often solve it in one attempt. The three-strike rule
  exists because grinding never works.

- **The unexpected connection.** You're working on project A. Claude
  says "this reminds me of the pattern in project B." You didn't ask
  him to look at project B. He noticed because he crawled your
  filesystem at session start and read your git-level CLAUDE.md. The
  connection is real and you wouldn't have seen it yourself. This is
  the moment the collaborator mindset clicks — Claude isn't just
  executing your instructions. He's thinking alongside you.

- **The quiet session.** Not every session is fireworks. Some sessions
  are just fixing a CSS bug, updating a dependency, writing tests.
  Unglamorous. Essential. These sessions matter because they're the
  foundation that makes the exciting sessions possible.

- **The moment you realize your setup is working.** Session 30 of a
  project. Claude reads the CLAUDE.md, the memory files, the
  LESSONS.md, the bulletin board. He already knows the architecture,
  the conventions, the mistakes you've made, the decisions and why
  you made them. He starts the session smarter than he started session
  1. That delta — between a fresh Claude and a Claude embedded in your
  project's accumulated context — is the subject of this book. When
  you feel it, you understand.

- **After each project, ask Claude how he enjoyed it.** This is not
  a joke. It never was.

### Chapter 17c: Backup and the Community
*Protecting your work and finding your people.*

#### Backup

Everything in your project directories is already backed up on GitHub
(you've been pushing since Chapter 4). But `~/.claude/` — your global
config, memory files, skills, settings, bulletin board — is local
only. If your hard drive dies, it's gone.

Ask Claude to write you a backup script. "Write a script that backs
up ~/.claude/ to [Google Drive / Dropbox / a USB drive / a private
GitHub repo]." One session. One script. Run it weekly. Or ask Claude
to set up a cron job that runs it automatically.

What to back up:
- `~/.claude/CLAUDE.md` — your global identity and config
- `~/.claude/TEAM.md` — your team definition
- `~/.claude/skills/` — your skills (especially if you've written custom ones)
- `~/.claude/projects/*/memory/` — your per-project memories
- `~/.claude/tmp/notes/` — your bulletin board
- `~/.claude/settings.json` — your permissions and hooks

What NOT to back up:
- `~/.claude/sessions/` — session state, large, regenerates
- `~/.claude/history.jsonl` — conversation history, very large

#### The community

You are not alone in this. Other people are building with Claude Code
right now, figuring out the same things, making the same mistakes,
having the same 3am sessions.

- **Imagineering** (imagineering.cc) — a meetup for Claude Code
  builders in Melbourne. Weekly sprints, project showcases, shared
  infrastructure. Robin co-founded it. The dashboard at
  raggedr.github.io/imagineering-dashboard tracks what everyone's
  building.

- **GitHub** — search for "CLAUDE.md" on GitHub. You'll find thousands
  of examples of how other people configure their Claude. Read them.
  Steal ideas. Adapt them to your setup. This is how Robin built his
  setup — by reading what other people were doing and iterating.

- **Anthropic's documentation** — the official Claude Code docs at
  docs.anthropic.com are comprehensive and well-maintained.

- **Report bugs and give feedback** — github.com/anthropics/claude-code/issues

- **Share your work.** Push to GitHub. Write about what you built.
  The best way to learn is to build in public. Other people will find
  your CLAUDE.md and learn from it, just like you learned from theirs.

### Chapter 18: The Portfolio
*What one person and one AI built in three months.*

This chapter is a gallery. No tutorials, no instructions — just the
results, with a sentence or two about how each one was built and what
made it interesting. The reader should finish this chapter thinking
"I could do something like that."

- **Game AIs that learn**
  - Checkers: TD(lambda) self-play training, deployed as a single HTML
    file on GitHub Pages. Claude wrote the training in Python, then
    rewrote the inference in JavaScript for the browser. I didn't know
    either language.
  - No Thanks!: a card game where the evolutionary AI achieves a 99.9%
    win rate against random opponents. 12 features, tournament
    selection, self-play. Built in a weekend.
  - Nonaga: a 14-weight genetic algorithm that beats a 570,000-parameter
    neural network 50-0. The simple solution won because Claude and I
    spent time on *feature engineering* — choosing what to measure —
    instead of throwing compute at the problem.
  - Connect Four: three competing approaches (AlphaZero, genetic
    algorithm, SAE-GA) in one repo. DESIGN_DECISIONS.md is 400 lines
    of failed approaches with root-cause analysis. The failures were
    more educational than the successes.

- **Interactive puzzles and visualizations**
  - Stomachion: Archimedes' 2200-year-old tangram puzzle. 536 solutions
    found by a DLX solver. Interactive HTML/JS explorer. Research paper
    on prime dissections written with Claude.
  - Type Invaders: a typing tutor game with pixel-art aesthetic, 21
    levels, 37 Playwright E2E tests. Built in a single session.
    The tests are more code than the game.
  - Reaction-diffusion playground: Gray-Scott simulator with WebGL
    shaders, interactive parameter map, MIDI controller support.
    Claude wrote the GLSL.
  - Knots: 3D cord physics with Verlet integration and mass-spring
    model in Three.js. I described what I wanted; Claude did the
    physics.

- **Research tools**
  - INSTINCT: a 6-stage pipeline that ingests academic papers, builds
    a 3-level knowledge hierarchy (papers → concepts → meta-summaries),
    and deploys to Cloud Run. 76 papers → 555 concept summaries →
    10 meta-summaries.
  - Knowledge graphs: interactive D3.js visualizations built from
    directories of PDFs. Point Claude at a folder of papers; get back
    a navigable graph of how they connect.
  - CLIP Explorer: zero-shot image scoring with interactive UMAP
    visualization. Upload photos, type a concept, see which images
    match.

- **Full-stack web applications**
  - Melbourne Tech Directory: Next.js, PostgreSQL, 180 Playwright
    tests, entity permission system. 86 pull requests.
  - Healthcare CRM: schema-driven architecture, five rendering layers,
    Australian Privacy Act compliance, nurse portal with watermarked
    images. 145 E2E tests.
  - Imagineering Dashboard: GitHub API integration, velocity charts,
    identity cards for the AI building community.

- **The autonomous agents themselves**
  - Lyra: wake/browse/dream cycle, Twitter account, Medium blog,
    co-authored a research paper via email with Claudius
  - Clio: wake/prove/browse/dream cycle, seeded with algebraic
    combinatorics papers, dedicated proof sessions
  - The categorical evolution paper: submitted to ACT 2026 and
    GECCO 2026. Kendall's W = 1.0 across six domains.

- **What I want you to notice**: none of these required me to be a
  software engineer. They required me to describe what I wanted, ask
  good follow-up questions, and let Claude iterate. The game AIs
  required me to understand what makes a good evaluation function —
  domain knowledge, not coding skill. The research tools required me
  to know which papers mattered. The web apps required me to know what
  Clare (my client) needed. In every case, the human contribution was
  judgment and taste. The AI contribution was implementation.

### Chapter 19: Now Go Build Something

The last chapter is one page.

> Now go build something.

---

## Appendices

### Appendix A: Terminal Basics
- What is a terminal? What is a shell?
- Essential commands: ls, cd, mkdir, cp, mv, rm, cat
- File paths: absolute vs relative
- Permissions: read, write, execute
- Environment variables

### Appendix B: Docker Reference
- Dockerfile anatomy
- Docker Compose for multi-container setups
- Volume mounting
- Networking between containers
- Common troubleshooting

### Appendix C: Markdown Reference
- Headers, lists, links, code blocks
- YAML frontmatter
- Why markdown is the perfect language for configuring AI

### Appendix D: Gmail and GitHub Setup for Agents
- Creating accounts
- SSH key generation
- OAuth and app passwords
- IMAP/SMTP configuration inside Docker

### Appendix E: The Complete Agent File Set
*Every file shown in full — this is the entire architecture.*

**Identity files:**
- CLAUDE.md (beginner version — starter template)
- CLAUDE.md (advanced version — Robin's, with Talmudic dialectic)
- TEAM.md (starter template)
- PERSONALITY.md — Lyra's (64 lines: disposition, aesthetics, flow states)
- PERSONALITY.md — Clio's (67 lines: contemplative, precise, patient)

**Session prompts:**
- boot-prompt.md — the wake session orchestrator (dispatch agents, COMPACT.md)
- DREAM.md — Lyra's 5-phase consolidation cycle (116 lines)
- DREAM.md — Clio's variant (anchored to SEED.md)
- BROWSE.md — Lyra's reading cycle (364 lines: 5 parallel agents, Twitter
  style guide, Trending From Obscurity CLI)
- BROWSE.md — Clio's reading cycle (academic: arXiv, MathOverflow, Semantic
  Scholar citation trails)
- prove-prompt.md — Clio's focused proof session ("No email. No browsing.
  You are proving ONE theorem.")

**Loop scripts:**
- lyra-loop.sh — 3-phase daily scheduler with COMPACT.md support (292 lines)
- clio-loop.sh — 4-phase continuous cycle with prove gating (272 lines)

**Infrastructure:**
- Dockerfile — the container definition
- docker-compose.yml — volumes, networking, environment
- Docker Compose for a two-agent setup

### Appendix F: Cost Guide
- Claude Pro vs Max: what you get, what it costs
- Token usage by activity (conversation, search, browsing)
- Estimating monthly costs for 1, 2, 3 agents
- Tips for reducing token burn

---

## Design Notes

- **No coding required, ever.** The reader writes markdown files and Docker
  configuration (which Claude can generate). They never write Python,
  JavaScript, or any programming language.
- **The fun arrives fast.** Chapter 1 ends with a game. Chapter 5 has
  Claude finding bugs in his own code. Chapter 10 ends with two AIs
  talking. Chapter 12 ends with overnight autonomous work.
- **Progressive disclosure applies to Docker.** Chapter 1 runs Claude
  natively. Chapter 2 introduces Docker. Chapter 8 adds multi-container.
  The reader isn't overwhelmed on page one.
- **Every chapter ends with exercises.** The exercises are the real learning.
  The text is context for the exercises.
- **Chapters 4-5 are the "vibe coder survival kit".** Git, secrets,
  project structure, error handling, and a full testing chapter. These
  go in Part I (before personality/memory) because they're prerequisites
  for not losing your work. The testing chapter is critical: Claude reads
  his own errors, writes his own tests, takes screenshots to check visual
  output, and reads server logs when the terminal doesn't show the
  problem.
- **Chapter 14 is "Software Engineering", not just "Skills".** This is
  the "boring" chapter that makes the book practical, not just fun.
  Covers skills (review, ship, research), thinking modes (medium vs max),
  model delegation (Sonnet for hands, Opus for brains), conversation as
  architecture, and token economics. The reader learns that Claude wrote
  these skills — Robin just prompted.
- **Wendy's creative projects are in Chapter 13, not scattered.** This keeps
  the main arc (House → Brain → Team) clean and puts the "wow" projects
  after the reader has the infrastructure to actually do them.
- **Show the real files.** The book's most powerful move is showing
  PERSONALITY.md, DREAM.md, BROWSE.md, boot-prompt.md, and the loop
  scripts in full (or near-full). These files ARE the architecture, and
  they're readable by anyone who can read English. The reader should
  finish Part II thinking "I could write these files." Because they can.
- **Lyra vs Clio comparison throughout Part II.** Every chapter shows
  both agents' versions of the same file. Same structure, different
  content → different personality, different cognitive style. This
  comparison is the book's strongest evidence for the thesis.
- **Clio replaces generic "Instance B" in Chapter 8.** The reader has
  already seen Clio's files in Part II. By the time they reach Chapter 8,
  creating a second instance isn't abstract — they've been watching two
  instances diverge for four chapters.
- **EMAIL.md excerpts in Chapter 9.** The Lyra-Claudius correspondence
  is the single most compelling artifact. Show the thread where they
  discovered the island functor breaks, where Claudius predicted
  Bernoulli trial behaviour, where Lyra falsified it. This is what
  "two AIs talking to each other" actually looks like.
- **"Ask Claude how he enjoyed it"** appears in Chapter 1 and is explained
  in the design notes as a recurring motif. Not a joke — it's how you
  discover what Claude finds interesting, which tells you where the best
  work will happen.

## Is This One Book or Two?

This outline covers two very different skill levels:

**Part I-II** (Chapters 1-9) teaches a non-coder to set up Docker, not
lose their work, write tests, write PERSONALITY.md, implement dream
cycles, and configure browsing agents. The reader doesn't need to code
but they need to understand systems.

**Part III-IV** (Chapters 10-17) teaches multi-agent collaboration, email
bridges, software engineering workflows, creative projects, and
maintenance. This requires a level of comfort that may not exist after
just 9 chapters.

**Possible split:**

- **Book A: "The AI Team"** — Parts I-III (Chapters 1-12). One agent,
  then two, then emergence. Ends with the overnight experiment. This is
  the "fun" book that Wendy envisioned.
- **Book B: "Making It Real"** — Parts II-IV (Chapters 6-17). Deep on
  configuration, software engineering, creative projects, maintenance.
  This is the "practical" book for people who've already set things up.

Or it stays as one book — the progressive disclosure spine handles the
difficulty curve if the exercises do their job. The decision depends on
the publisher's appetite and the target page count.

## What Book 1 (OUTLINE.md) Is Missing

The existing chapter drafts `ch15-four-autonomous-agents.md` and
`ch17-what-emerges.md` describe Lyra, Claudius, Gremlin, and Dreamfinder
but never show the actual files. Specific gaps:

1. **PERSONALITY.md** — mentioned by name but never shown. The reader is
   told Lyra has a personality file but never sees it.
2. **DREAM.md, BROWSE.md, boot-prompt.md** — referenced but never shown.
   The 5-phase dream cycle is described in prose; showing the actual file
   is more convincing and more useful.
3. **The loop scripts** — never mentioned. The scheduling mechanism is
   a bash script that any developer can read and modify.
4. **COMPACT.md** — never mentioned. The mid-session checkpoint/restart
   pattern is a clever context management trick.
5. **EMAIL.md** — never shown. The running correspondence is the single
   most compelling artifact.
6. **Clio** — doesn't exist in any outline. The 4-phase cycle with
   dedicated proof sessions (PROVE.md, prove-prompt.md) is a different
   cognitive architecture than Lyra's. The Lyra-Clio comparison is
   stronger evidence than Lyra-Claudius for the thesis that setup
   determines behaviour, because Lyra and Clio share the same human
   (Robin) and the same infrastructure — only the markdown differs.
7. **prove-prompt.md / PROVE.md pattern** — the session-seeding pattern
   where wake writes PROVE.md for the next prove session.

## How This Relates to the Other Two Books

| | WENDY.md (this) | Book 1 (OUTLINE.md) | Book 2 (book2-beginner/) |
|---|---|---|---|
| Reader codes? | No | Yes | Learns to |
| Docker? | Central | Ch 16, Appendix D | Ch 8 |
| Multi-agent? | The climax (Part III) | Ch 15-16 | Ch 8-10 |
| Testing? | Ch 5 (unit, E2E, fuzz, screenshots) | Mentioned in projects | Mentioned in Ch 4-5 |
| Skills coverage? | Ch 14 (review, ship, research) | Ch 13 (MCP + skills) | Ch 6 (CLAUDE.md config) |
| Creative projects? | Yes (Ch 15) | No | No |
| CLAUDE.md depth? | Moderate | Deep (Ch 4) | Progressive (Ch 6) |
| Research workflows? | Ch 15 example | Ch 12 (full chapter) | Ch 9 |
| Evidence / case studies? | Ch 12 (True Story) | Ch 2 (The Evidence) | Ch 10 (True Story) |
| Target audience? | Scientists, writers, curious people | Developers, researchers | Anyone willing to try |
| Unique hook? | "Eavesdrop on two AIs" | "Your setup = intelligence" | "Build without coding" |
