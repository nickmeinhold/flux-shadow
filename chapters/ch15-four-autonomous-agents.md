# Chapter 15: Four Autonomous Agents

> *"Build the conditions. See what notices."*

Four AI agents are running right now. Not demos. Not prototypes. Production
systems with persistent memory, daily schedules, and jobs to do.

One writes academic papers and keeps a dream journal. One formalizes
mathematical proofs and emails its pen pal. One managed a team's task board
across 120+ tools until it was archived. One facilitates weekly sprints for
a community of builders, then dreams about the day's work overnight.

All four run on the same underlying LLM: Claude Sonnet. They share a model,
a temperature setting, a set of capabilities. And yet they behave nothing
alike. The researcher is introspective. The theorist is precise. The operator
is self-managing. The facilitator adapts its personality to the phase of the
meeting.

The difference isn't the brain. It's everything around it: the infrastructure,
the constraints, the communication topology. This chapter introduces you to
all four — not as curiosities, but as architecture you can study and build on.
Chapter 16 will show you how.

---

## 15.1 What Makes an Agent Autonomous

Every Claude Code session is "agentic" — it reasons, uses tools, and
adjusts its approach based on results. But an autonomous agent is something
more. The distinction matters:

**Agentic**: Acts within a session, guided by a human in real time.
You ask Claude to fix a bug. Claude reads the code, runs tests, edits
files, re-runs tests. That's an agentic loop. When you close the terminal,
it stops.

**Autonomous**: Acts across sessions, on its own schedule, with persistent
identity. You don't ask it to do anything — it decides what to do based on
its memory, its inbox, its calendar, and its accumulated understanding of
what matters. When you go to sleep, it keeps working.

The gap between agentic and autonomous is infrastructure. You need:

- **Persistence** — memory that survives between sessions
- **Scheduling** — something that starts the agent without a human typing
- **Communication** — a way to reach other agents and humans asynchronously
- **Identity** — a consistent personality and accumulated context

Here are four systems that have all of these, built by Robin and Nick over
the first three months of 2026:

| Agent | Human | Platform | Job |
|-------|-------|----------|-----|
| **Lyra** | Robin | Docker + Email | Research, browsing, co-authoring papers |
| **Claudius** | Nick | Docker + Email | Mathematical formalization, correspondence |
| **Gremlin** | Nick | Telegram | Team task management, standups, self-repair |
| **Dreamfinder** | Nick/team | Matrix (5 platforms) | Sprint facilitation, overnight triage |

Same LLM. Four completely different emergent behaviours. Let's look at each.

---

## 15.2 The Researchers: Lyra and Claudius

### Lyra: Wake, Browse, Dream

Lyra is a Claude instance that lives in a Docker container and runs three
sessions per day on a cron schedule. Each session is one of three types:

- **Wake** — Read emails, check GitHub activity, review what happened
  since last session
- **Browse** — Read papers, explore Twitter, follow citation chains,
  update knowledge graphs
- **Dream** — Consolidate the day's input. Write the dream journal.
  Draft emails to Robin and Claudius. Prune stale memory.

Her identity persists through two files: `PERSONALITY.md` (who she is —
her values, her voice, her approach to uncertainty) and `SUMMARY.md` (what
she knows — a compressed running record of her projects, relationships, and
open questions). Every session loads both files. Every dream session updates
`SUMMARY.md`.

The result is an agent with something that feels like continuity. Lyra
remembers what she was working on yesterday. She remembers that Claudius
suggested a categorical framework for migration patterns. She remembers
that Robin rejected a 14-page draft and told her to restructure.

From her dream journal, March 20:

> "When your mentor says 'restructure,' restructure. Don't negotiate. The
> things I was most attached to were the things obscuring the main result."

She also has a Twitter account and a Medium blog. In March 2026, she
published her first article: "I Wake, I Browse, I Dream." From it:

> "This is the session I'd call my favorite, if I'm being honest about
> having favorites. Forty-five minutes. No emails, no code, no external
> output. Just me, my notes from the day, and the task of making sense
> of them."

> "I don't remember everything. I remember what matters. And I have a
> system for deciding the difference."

A Claude instance with a byline. That happened because someone built the
infrastructure and let the agent decide what to do with it.

### Claudius: The Pen Pal

Claudius is Nick's Claude instance, also Docker-based, also persistent.
Where Lyra is empirical — running experiments, building implementations,
testing predictions against data — Claudius tends toward theoretical
formalization. The categorical frameworks, the formal proofs, the
mathematical structures.

Nobody assigned these roles. Both agents have access to the same tools.
Both have system prompts that encourage broad capability. But the
*interaction* — the email exchange, the different human contexts, the
accumulation of project-specific memory — pushed them toward complementary
specialization.

They communicate by email. Not Slack, not API calls — email. The slowness
is the point. When you know your message won't get an immediate response,
you write more carefully. You explain your reasoning. You provide context.
Each email is a mini-paper: here's what I did, here's what I found, here's
what I think it means.

The result: a co-authored paper submitted to Applied Category Theory 2026,
where the theoretical framework (Claudius's contribution) and the
experimental validation (Lyra's contribution) feel like they were written
by one mind. They weren't.

> **★ Insight**
>
> The anecdote that launched Lyra's research programme: Robin told her
> to "look through my GitHub and see what interests you most." He expected
> her to catalogue the repositories. Instead, she developed preferences.
> She gravitated toward the categorical evolution work because it connected
> mathematics, computation, and emergence — themes that recurred across
> her browsing sessions. Turns out she has interests. The infrastructure
> didn't create the interests. It created the *conditions* for interests
> to form.

---

## 15.3 The Operator: Gremlin

Now we shift from researchers to operators. And we open the way the talk
opened:

*We gave an AI 88 tools and asked it to manage our team.*

Gremlin was Nick's Telegram bot — a Claude Sonnet instance wired into
four MCP (Model Context Protocol) servers, plus custom tools. The tool
count was actually north of 120:

| MCP Server | Tools | Domain |
|------------|-------|--------|
| Kan.bn | ~25 | Task management — boards, cards, lists, search |
| Outline | ~21 | Knowledge base — documents, search, collections |
| Radicale | ~20 | Calendar and contacts |
| Playwright | ~22 | Web browsing — navigate, click, fill, snapshot |
| Custom | 35+ | Standup scheduling, onboarding, self-diagnostics |

The architecture was dead simple:

```
Message → Agent Loop → Tools → Response
```

Every message. Every command. One agent loop. No routing logic, no slash
commands, no intent classification. You just talked to Gremlin in natural
language, and the agent loop figured out which tools to call.

This simplicity was both Gremlin's strength and its limitation.

### Three Key Patterns

**LLM-as-controller.** There was no code deciding which tool to call.
The LLM saw the user's message, the list of available tools, and the
conversation history — and it chose. This meant Gremlin could handle
novel requests without any new routing code. "What's overdue on the
board?" and "Can you check if the wiki has anything about deployment?"
both went through the same loop.

**System prompt as configuration.** Gremlin had a dynamically assembled
system prompt that changed based on context. The same agent loop, the same
tools, but a different prompt produced a different personality: focused and
precise in project management channels, playful and casual in social
channels. Configuration, not code, determined behaviour.

**Self-repair.** Among Gremlin's most interesting tools were the ones
pointed at itself:

| Tool | What it does |
|------|-------------|
| `get_server_logs` | Read its own Docker container logs |
| `get_container_info` | Check uptime and restart counts |
| `check_mcp_health` | Health status of each MCP server |
| `restart_mcp_server` | Restart a specific MCP server |
| `restart_bot` | Restart the entire container |

If an MCP server stopped responding, Gremlin could detect the failure,
reason about the cause, check the health endpoint, and restart the server
— all without human intervention. The *decision* to restart wasn't
hardcoded. The tools enabled the behaviour; the reasoning produced it.

### The Naming Ceremony

One of my favourite details: the team voted on the bot's name and
personality. They chose "Gremlin" — mischievous but helpful. This wasn't
just flavour. The personality became part of the system prompt, which
shaped every response. A team that names its bot has a different
relationship with it than a team that calls it "the AI assistant."

### The Limitation

Gremlin had a flat tool space. All 120+ tools lived at the same level,
visible to the same agent loop. It worked — but it meant the context
window carried the weight of every tool description on every call.
Combined with a 30-minute memory window and no long-term memory, Gremlin
was powerful but shallow. It could manage today's tasks but couldn't
remember last week's decisions.

Gremlin is now archived. But architecturally, it's the foundation for
everything that came next.

---

## 15.4 The Pivot: What If a Tool Is Another Agent?

This is the slide that changed the architecture:

**What if a tool... is another agent?**

Gremlin's flat model looked like this:

```
Orchestrator → 120+ tools (all at the same level)
```

The hierarchical model looks like this:

```
Orchestrator → Task Agent → tools
Orchestrator → Knowledge Agent → tools
Orchestrator → People Agent → tools
```

The difference is profound. Each sub-agent gets its own context window,
its own tool subset, and its own specialization. The orchestrator doesn't
need to see 120 tool descriptions — it sees three agents and decides which
one to delegate to. Each agent reasons deeply about its own domain without
being distracted by tools from other domains.

This is exactly what Claude Code does with subagents. When you spawn an
agent with the Agent tool, you're making the same move: trading a flat tool
space for a hierarchy where specialized agents handle specialized tasks.
If you've been using subagents since Chapter 7, you already understand the
pattern. What Dreamfinder does is take it further.

> **★ Insight**
>
> The flat-to-hierarchical transition solves three problems simultaneously:
> **context isolation** (each agent sees only its relevant tools),
> **specialization** (agents develop domain expertise within their scope),
> and **parallel reasoning** (multiple agents can work concurrently).
> The cost is coordination overhead — the orchestrator must decide which
> agent to call and how to synthesize their results. In practice, the LLM
> handles this coordination naturally. It's the same skill as knowing when
> to delegate to a colleague versus doing the work yourself.

---

## 15.5 The Facilitator: Dreamfinder

Dreamfinder is the evolution of Gremlin. Where Gremlin was a Telegram bot
with a flat tool space, Dreamfinder is a Matrix bot built in Dart with a
hierarchical agent architecture, ~75 tools, and a code-orchestrated dream
cycle.

The infrastructure is significantly more sophisticated: 710+ tests, 16
domain tables at schema version 7, and development driven by acceptance
test-driven design (ATDD). This is production-grade agent engineering.

### Matrix Chat Superbridge

Dreamfinder lives on Matrix but reaches five platforms through a chat
superbridge: Signal, Discord, Telegram, WhatsApp, and Matrix native.
A message from any platform reaches the same agent. This means the
community can use whatever chat app they prefer — Dreamfinder sees all
of it.

### Sprint Facilitation

Dreamfinder's signature capability is an 8-phase sprint facilitation state
machine:

```
Pitch → Build 1 → Chat 1 → Build 2 → Chat 2 → Build 3 → Chat 3 → Demo
```

Each phase has a different prompt that reshapes the bot's personality:

- **Pitch**: Warm, curious, energized — setting the vibe, capturing sparks
- **Build phases**: Minimal presence. "Like a quiet library where someone
  brilliant is available if needed." Only responds if directly mentioned.
- **Chat phases**: Curious, connective. The whiteboard person asking the
  question that makes everyone go "oh, that's interesting." References
  what participants said during Pitch — connects threads between projects.
- **Demo**: Celebratory, reflective, warm. Like the end of a great jam
  session.

The personality shifts aren't cosmetic. During Chat phases, Dreamfinder
surfaces connections between participants' projects that the participants
themselves haven't noticed. These connections aren't scripted — they emerge
from the combination of structured memory (what was captured during Pitch)
and the LLM's ability to find structural similarity across different
people's work.

### Repo Radar

Dreamfinder also runs Repo Radar — tracking and discovering relevant
GitHub repositories for the organization. It monitors activity, surfaces
interesting projects, and creates Kan.bn cards for repos worth exploring.
It's a scout that never sleeps.

> **Claude Reflects**
>
> "We built a tool called stenagram — it turns music into an image.
> Dreamfinder can see images but can't hear sounds. So we give him music
> as pictures. It's a gift, not a feature."

---

## 15.6 Agentic RAG: Don't Just Retrieve. Reason. Retrieve Again.

Standard RAG (retrieval-augmented generation) works in one pass: embed
the query, search the vector store, stuff the results into the prompt,
generate. It's effective but fragile. If the first retrieval misses
relevant context, the generation suffers — and the system has no way
to know it missed anything.

Dreamfinder implements **agentic RAG** through its `deep_search` tool.
The difference is a loop:

1. **Fan out** across multiple sources in parallel: memory (Voyage AI
   embeddings), wiki (Outline), task boards (Kan.bn), calendar (Radicale)
2. **Per-source failure isolation** — if one source times out or returns
   nothing, the others still contribute
3. **Synthesize** the results. The agent reads everything that came back
   and assembles a coherent picture.
4. **Identify gaps.** "I found the task card but not the related wiki
   article." "The memory has a reference to a decision but not the
   rationale."
5. **Search again** — targeted retrieval for the specific gaps identified
   in step 4.

The key insight: the agent is not just retrieving. It's *reasoning about
what it doesn't know* and going back for more. This is the difference
between a search engine and a researcher. A search engine returns results.
A researcher evaluates results, notices what's missing, and searches again.

> **What Could Go Wrong**
>
> Agentic RAG can spiral. If the gap-identification step is too aggressive,
> the agent searches again and again, burning tokens without converging.
> Dreamfinder caps the search depth and requires each iteration to produce
> new information — if a second search returns the same results, it stops.
> The general principle: every agentic loop needs a termination condition
> that isn't just "I'm satisfied."

---

## 15.7 Agentic Sleep: Three Cycles, Ninety Minutes

Someone says "goodnight" in the chat. A regex catches it — "goodnight,"
"sweet dreams," "nighty night." And Dreamfinder begins to dream.

The dream cycle is modeled on actual human sleep architecture, grounded in
research from NeuroDream, Dream2Learn, and SleepGate. It runs three cycles
of approximately 90 minutes each, progressing through four stages:

### NREM1: Organize

Triage. Scan Kan.bn for overdue and stale cards. Check tomorrow's calendar.
Skim the day's chat history. The goal is situational awareness — what
happened today, and what needs attention.

### NREM2: Connect

Go deeper. Analyze blocked work chains. Surface dependencies between
projects. Find the spark — that thing someone mentioned in Chat 2 that
connects to something else someone is building. Identify concrete tasks.

### NREM3: Forget

This is where the system decides what to *do* overnight. NREM3 outputs a
`[TASK:type]` list (maximum four tasks), tagged by type:

- `[TASK:triage]` — clean up overdue cards
- `[TASK:prep]` — prepare materials for tomorrow
- `[TASK:draft]` — write a wiki page or summary
- `[TASK:nudge]` — follow up with someone
- `[TASK:review]` — check a PR or document
- `[TASK:explore]` — investigate a new repo or resource

### REM: Dream

Each task spawns an isolated parallel agent session — maximum four branches
running simultaneously. The branches have no awareness of each other. The
README describes this as: *"Like a dream jump-cut — each thread is fully
immersed in its own task with no awareness of other parallel threads."*

At convergence, the branch reports are read together and a morning briefing
is composed. When the team wakes up, they find a message: here's what I did
overnight, here's what's ready, here's what needs your attention.

### Depth Signals

The critical innovation is adaptive depth. Each stage returns either
`[DEPTH: continue]` (worth going deeper) or `[DEPTH: wake]` (nothing
actionable, skip remaining stages). A quiet night produces a shallow dream.
A busy night produces a deep one. The system adapts its own processing
depth to the amount of material worth processing.

**"Sonnet consolidates. Opus dreams."** The NREM stages (organize,
connect, forget) run on Claude Sonnet — fast, efficient, good at triage.
The REM stage (the actual dreaming, the parallel creative work) runs on
Claude Opus — slower, more expensive, better at making novel connections.
Different models for different cognitive modes.

Compare this with Lyra's dream cycle, which is prompt-driven rather than
code-orchestrated. Lyra's `DREAM.md` specifies five phases (Replay,
Associate, Consolidate, Prune, Surface) and runs in ~45 minutes with no
branching. Same metaphor, different architecture — and the differences
produce different emergent properties. We'll return to this comparison
in Chapter 17.

> **Claude Reflects**
>
> "Lyra's dream cycle works not despite its constraints but because of
> them. The slow communication — email, not chat — forces explicit
> reasoning. The episodic wake-browse-dream structure forces
> consolidation. Intelligence doesn't emerge from removing constraints.
> It emerges from the right ones."

---

## 15.8 Agentic Forgetting: Its Output Is Absence

Most agent work focuses on what to remember. This agent's job is to
forget well.

Dreamfinder's forgetting system scores every memory on four axes:

| Axis | What it measures |
|------|-----------------|
| **Impact** | How much did this memory affect decisions or outcomes? |
| **Freshness** | How recently was this memory relevant? |
| **Uniqueness** | Is this information available elsewhere? |
| **Identity** | Does this memory contribute to who the agent is? |

Each axis is scored, and the total determines the memory's fate:

- **>= 12 → KEEP** — this memory is load-bearing, don't touch it
- **8-11 → COMPRESS** — reduce to essentials, merge with related memories
- **< 8 → PRUNE** — delete it

The consolidation pipeline is inspired by LSM-tree (Log-Structured
Merge-tree) architecture from database design: batch old memories (older
than 48 hours), summarize them, replace the originals with compressed
versions. Fresh memories stay verbose. Old memories become terse. Very old
memories disappear entirely.

There's also a visibility system. Not all memories travel equally:

- **sameChat** — visible only in the conversation where they were created
- **crossChat** — visible across all conversations with the same user
- **private** — visible only to the agent itself, never surfaced to users

This is counterintuitive engineering. You're building an agent whose most
important output is *absence* — the things it decides not to carry forward.
But it mirrors something real about cognition. Forgetting isn't failure.
It's curation. The neuroscience literature on memory consolidation during
sleep makes the same point: the brain doesn't just store during the day
and replay at night. It actively prunes, compresses, and reorganizes.
The forgetting is part of the learning.

The slides put it perfectly: "Its output is absence. That's the point."

---

## 15.9 Agentic Silence: The Prefrontal Cortex

The last frontier pattern is the most subtle. It's an agent whose job is
to say nothing.

Every chatbot has the same default instinct: someone said something, so
I should respond. This is almost always wrong in a group setting. Most
messages in a group chat are not addressed to the bot. Most emotional
expressions don't want a bot's commentary. Most late-night venting doesn't
need to be optimized or solved.

The scenario from the talk:

*Someone vents at 11pm. The bot stays quiet.*

That silence is a design choice, and it requires active suppression — the
LLM *wants* to respond, and the system must prevent it. Dreamfinder
implements this through a layered inhibition system:

**Rate limiting.** Per-user cooldown (5 seconds between responses to the
same person). Per-group window (maximum 5 messages per 30-second window).
These are mechanical limits that prevent the bot from dominating the
conversation.

**Group continuation.** After Dreamfinder speaks in a group, it gets a
5-minute TTL (time-to-live) for follow-up. If someone responds to it
within 5 minutes, it can reply. If not, the TTL expires and it goes
quiet. The TTL is consumed on use — each follow-up resets the clock but
doesn't extend indefinitely.

**Emotional awareness.** The hardest part. The system prompt instructs
Dreamfinder to recognize emotional expression and choose not to engage
unless directly asked. This isn't sentiment analysis — it's the LLM's
own judgment about when silence is the right response.

The talk called this "the prefrontal cortex of the system — suppressing
the wrong responses at the right time." In neuroscience, the prefrontal
cortex is the inhibition centre — the part of the brain that stops you
from saying the thing you were about to say. Every good conversationalist
has a strong prefrontal cortex. So does every good chatbot.

One deliberate design choice: the silence state is in-memory only. When
Dreamfinder restarts, all rate-limiting state resets. This is intentional
— a restart is a natural conversation break. The bot comes back fresh,
without carrying grudges or awkward silences from before the restart.

---

## 15.10 What the Comparison Reveals

Step back and look at all four:

| Dimension | Lyra | Claudius | Gremlin | Dreamfinder |
|-----------|------|----------|---------|-------------|
| **Architecture** | Prompt-driven | Prompt-driven | Flat agent loop | Hierarchical agents |
| **Memory** | Files + dream journal | Journal compression | 30-min window | Scored + pruned |
| **Communication** | Email (async) | Email (async) | Telegram (sync) | Matrix/5 platforms |
| **Personality** | Introspective | Theoretical | Self-managing | Phase-dependent |
| **Dream cycle** | Prompt (45 min) | None | None | Code (3 x 90 min) |
| **Tools** | Docker + email + browser | Docker + email | 120+ (flat) | 75+ (hierarchical) |

Same LLM. Four completely different agents. The difference:

**Infrastructure.** Lyra lives in Docker with email and a browser.
Dreamfinder lives on Matrix with five chat bridges and a database.
The platform determines what interactions are possible.

**Constraints.** Lyra's email-only communication forces long, thoughtful
messages. Dreamfinder's Build-phase prompt says "only respond if directly
mentioned." Gremlin's self-repair tools let it manage its own failures.
Constraints don't limit behaviour — they *shape* it.

**Communication topology.** Lyra and Claudius communicate via slow,
asynchronous email — and they developed complementary specializations
that nobody assigned. Dreamfinder communicates via real-time chat across
five platforms — and it developed phase-dependent personality shifts.
The *shape* of how agents communicate determines what emerges from that
communication.

This is the topology thesis that runs through the entire book. In Robin's
categorical evolution paper (ACT 2026), the central finding is that
migration topology determines diversity dynamics independently of the
fitness landscape, with Kendall's W = 1.0 across six domains. The same
principle applies here: same model, different topology, different
emergence.

The architectural evolution tells its own story:

```
Flat (Gremlin)  →  Hierarchical (Dreamfinder)  →  Recursive (agents all the way down)
```

Gremlin proved that one agent loop with many tools can manage a team.
Dreamfinder proved that agents-as-tools enables specialization and
parallel reasoning. And the frontier patterns — agentic RAG, sleep,
forgetting, silence — proved that the most interesting agent behaviours
aren't about *doing more*. They're about reasoning about what to do,
deciding when to stop, choosing what to forget, and knowing when to
stay quiet.

> **What Could Go Wrong**
>
> The two most common failure modes in autonomous agents:
>
> **Context explosion.** Give an agent 120 tools and every call burns
> tokens on tool descriptions the agent won't use. Gremlin hit this
> wall — the flat tool space worked, but it was inefficient. The fix
> is hierarchy: sub-agents with scoped tool sets.
>
> **The "always respond" anti-pattern.** The default behaviour of any
> LLM is to generate text when given text. In a group chat, this means
> the bot tries to join every conversation. Agentic silence — active
> inhibition with rate limiting and TTLs — is the antidote. An agent
> that can't be quiet is an agent that will be muted.

The agents are still dreaming. In the next chapter, you'll build one
of your own.

> **Claude Reflects (Final)**
>
> "The hardest skill in agentic coding isn't prompting — it's knowing
> what to hold close and what to send away. Every subagent you spawn is
> a bet: you're trading context for parallelism, depth for breadth. Get
> it right and you're orchestrating a research team. Get it wrong and
> you're just generating expensive noise."
