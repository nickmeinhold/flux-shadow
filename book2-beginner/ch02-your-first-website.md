# Chapter 2: Your First Website

You don't need to know HTML. You don't need to know JavaScript. You don't need
to know CSS. You need to know what you want.

By the end of this chapter you'll have built a working game, published it on
the internet for anyone to play, and improved it through conversation — all
by describing what you want in plain English.

---

> **A note about following along.** When I show you a conversation with
> Claude, your results will be different from mine. Claude doesn't produce
> the same output twice — different runs give different code, different
> layouts, different bugs. That's fine. The prompts I show you are
> transferable; the specific outputs aren't. When I say "the input field
> disappeared below my screen," yours might work perfectly — or you might
> have a different problem entirely. The skill isn't memorising my prompts.
> It's learning to *look at what you got*, *describe what's wrong*, and
> *ask Claude to fix it*. That loop is the whole game.
>
> There's another reason your results may differ from mine: my system is
> configured differently from yours. I've been using Claude Code for months
> and have built up custom skills, persistent memory, and configuration
> files that shape how Claude responds to me. We'll cover all of this in
> Chapter 8. For now, just know that if Claude's response to you doesn't
> match what I describe in the book, that's expected. Focus on the pattern,
> not the exact output.

## 2.1 Setting the Scene

Open your terminal and set up a workspace:

```bash
cd ~/claude-projects
mkdir hangman
cd hangman
claude
```

Before you give Claude your first real task, set the scene with a pre-prompt:

> I'm not a software engineer. I'm learning how to make single-page websites
> with HTML, CSS, and JavaScript. Please explain your decisions as you go.

This tells Claude who you are so it can pitch its responses at the right
level. Same Claude, different conversation. (We introduced pre-prompts in
Chapter 1. Later we'll save this to a file so you don't have to type it
every time.)

## 2.2 Describe What You Want

Now describe a game. Here's how I'd do it — in plain English, the way you'd
explain it to a person:

> Build me a Hangman game as a single-page website in one HTML file. No
> external dependencies — everything inline.
>
> You know the rules: the player guesses a word one letter at a time. Each
> wrong guess draws the next part of a stick figure on a gallows. I want 9
> wrong guesses before the player loses. Draw the pieces in this order:
> gallows base, upright pole, top beam, rope, head, body, left arm, right
> arm, and legs together as the last piece.
>
> Layout: hangman drawing on the left, the word on the right displayed large
> with underscores for missing letters. Wrong guesses listed underneath the
> drawing. An input field at the top where the player types a letter and
> presses Enter — it should accept keyboard input without needing to click
> the field each time.
>
> Pre-load a list of at least 50 common English words, ranging from 4 to 10
> letters long, and pick one at random.
>
> When the player wins: green explosion animation, "You Win!", reveal the
> word. When they lose: red explosion, "You Lose!", reveal the word. Both
> should offer a "Play Again" button.
>
> Everything must fit on screen without scrolling.

Press Enter and watch.

Claude will start working. It will ask for permission to create files — say
yes. When it's done, you'll have a single file called `index.html`.

## 2.3 Play Your Game

Open your web browser and type this into the address bar:

```
file:///Users/your-username/claude-projects/hangman/index.html
```

Replace `your-username` with your actual username. Not sure what it is? Ask
Claude:

> What's the full path to the index.html file you just created?

You should see a hangman game. A real, playable game. Try it. Guess some
letters. Get a few wrong on purpose and watch the figure get drawn.

You made this by describing what you wanted in English.

**Why `file://` instead of `http://`?** Your game isn't on the internet yet
— it's a file on your hard drive. The `file://` prefix tells the browser to
open a local file. Later in this chapter, we'll put it on the internet for
real.

## 2.4 What Claude Just Made

Your game is a single HTML file, but it contains three different languages
working together:

- **HTML** — The structure. What's on the page: the input field, the word
  display, the drawing area. The skeleton.
- **CSS** — The appearance. Colours, fonts, spacing, layout. The skin and
  clothes.
- **JavaScript** — The behaviour. What happens when you press a key, how the
  drawing updates, the win/lose logic, the explosion animation. The muscles
  and the brain.

You don't need to understand any of this yet. But if you're curious, ask
Claude:

> Can you walk me through the index.html file and show me which parts are
> HTML, which are CSS, and which are JavaScript?

Claude will use *your actual code* to explain the concepts. This is better
than any textbook because the examples are things you've already seen working.

## 2.5 Making It Better

Your game works. But does it look good?

Probably not. Here's something you'll notice throughout this book: getting
the **game mechanics** working is usually not that hard. Claude is excellent
at logic, rules, and structure — one prompt and the game works. Getting the
game to be **aesthetically pleasing** is much more difficult. Design,
layout, colour, animation — these require multiple rounds of conversation
and Claude doesn't always get them right the first time.

The layout might feel awkward. The hangman might be plain geometric lines.
The explosion animation might be underwhelming or missing entirely. The whole
thing might look like it was built in 1998.

This is normal. This is where the real skill begins — and where most of the
learning happens. You're about to have your first real *conversation* with
Claude.

Visual design is one of the hardest things to get right with AI. Claude is
excellent at logic, game rules, and code structure — but aesthetics require
multiple rounds of conversation. No single prompt will get the design perfect.
But a detailed prompt gets you much closer on the first try, which means fewer
rounds of fixing things afterward.

Here's the design prompt I use. It's long, but every line is there for a
reason — mostly to stop Claude from breaking things while making them pretty:

> The game works correctly but the visual design feels flat and generic.
> Redesign it with a dark, atmospheric theme. Here is what I want:
>
> **IMPORTANT: Do not break the layout.** The game must remain fully
> playable after your changes. The input field, the hangman drawing, the
> word display, the wrong letters, and the win/lose screen must ALL fit
> within a single browser viewport on a laptop without scrolling. Test
> that nothing has moved off-screen.
>
> **Colour palette:**
> - Background: dark but not pure black — a deep navy (#1a1a2e) or dark
>   charcoal (#1e1e2e)
> - Main text: warm off-white or cream (#f0e6d3)
> - Correct letters in the word: bright clean white
> - Wrong letters: muted red (#cc4444), clearly different from the main
>   word
> - One accent colour for buttons and highlights: gold (#d4a647) or teal
>   (#4ecdc4) — pick one and use it consistently
>
> **Typography:** Use a system font stack (no external fonts). Make the
> word display large, bold, with generous letter-spacing. The wrong-letter
> display should be noticeably smaller and muted. The input field should
> feel prominent but not overwhelming.
>
> **The hangman drawing:** Style the lines to look hand-sketched — slightly
> uneven stroke widths, warm white or cream colour against the dark
> background. The figure should feel drawn by hand, not by a computer.
>
> **Animations (keep them subtle, 200-400ms each):**
> - Correct letter revealed: brief glow or gentle scale-up
> - Wrong letter guessed: subtle shake on the wrong-letter list
> - Win: green particles burst from the centre, "You Win!" fades in
> - Lose: red particles burst from the centre, "You Lose!" fades in
>
> **Layout:** Keep the same structure (input top, drawing left, word right)
> but improve spacing and visual grouping. Add breathing room between
> elements. Make sure the visual hierarchy is clear — the word display is
> the most important element, then the drawing, then the input.
>
> Single HTML file, no external dependencies, no CDN fonts, no icon
> libraries. All assets inline.

A few things to notice about this prompt. First, the **"do not break the
layout"** warning is right at the top. Claude has a tendency to make things
beautiful and broken at the same time — improving the CSS while accidentally
pushing elements off-screen. The explicit warning helps, though it doesn't
always prevent the problem.

Second, the prompt gives **specific colours and values**, not vague
directions. "Dark, atmospheric theme" plus exact hex codes is much more
reliable than "pick a theme." Claude is better at implementing a clear vision
than inventing one from scratch.

Third, the animation timings are **constrained** (200-400ms). Without this,
Claude sometimes adds 2-second transitions that make the game feel sluggish.

Even with all this detail, expect to iterate. Design is Claude's weakest
area — you'll almost certainly need a few follow-up prompts. But you'll be
fixing details, not starting over. That's the difference a good prompt makes.

Refresh your browser after Claude finishes. Better? Probably — but not
perfect. When I did this, the theme looked great but the input field
disappeared below the bottom of my screen. Claude had made it beautiful and
broken at the same time. (This is why the "do not break the layout" line is
there — and why I said "it doesn't always prevent the problem.")

**Round 2 — fix what broke:**

> This actually made it worse. I can't see the input field — it's below the
> bottom of my screen. The whole game needs to fit within the viewport
> without scrolling.

Claude fixes the layout. Refresh.

**Round 3 — polish the details:**

> Much better. But the wrong-letter display is hard to read against the dark
> background. And when I guess a correct letter, nothing happens visually —
> the letter just appears. Can you add a brief glow animation when a correct
> letter is revealed? And make the wrong letters more visible.

Refresh again.

**Round 4 — the win/lose experience:**

> The gameplay feels good now. But winning is anticlimactic — the "You Win"
> text just appears. I want the explosion animation we asked for originally.
> Green particles for a win, red for a loss. The particles should burst from
> the centre of the screen and fade out. Make it feel celebratory.

This back-and-forth is the core workflow of Claude Code:

1. **Describe** what you want
2. **Look** at what Claude made (refresh your browser)
3. **Refine** by describing what to change
4. Repeat

It's a conversation, not a specification. Each round gets you closer. Five
prompts (the original build plus four rounds of refinement) took us from a
generic game to a polished, themed hangman with hand-drawn art, animations,
and particle effects.

**Conversation is the skill this book teaches.** Not prompting. Not coding.
*Conversation.* The ability to look at something, articulate what's wrong
with it, and guide someone toward what you actually want — that's a human
skill, and it transfers to working with any AI, any collaborator, any
creative process. The prompts are just the vehicle. The conversation is the
thing.

Don't clear context between these rounds. Each follow-up prompt builds on
what Claude already knows about your project — that accumulated context is
valuable. Claude remembers what it built, what you asked for, and what went
wrong. Clearing mid-conversation would throw all of that away.

When *should* you clear? Two situations. First, when you're done with a
project and starting something new — that's the "new project, new directory,
new Claude session" rule. Second, when Claude seems genuinely confused:
it's making the same mistake repeatedly, contradicting itself, or fixing one
thing while breaking another in circles. That's a sign its context has
become cluttered with too many conflicting instructions. Type `/clear`, give
Claude a fresh summary of where things stand, and continue. Think of it as
rebooting a conversation that's gone off the rails — not something you do
on a schedule, but a tool you reach for when things feel stuck.

> **Tip:** Describe the *problem*, not the solution. "I can't see the input
> field" is more helpful than "make everything smaller." Claude can figure
> out the right fix — maybe it needs to reorganise the layout, not just
> shrink things. Give Claude the problem and let it choose the approach.

**What if your game just stops working?** Sometimes after a round of
changes, the game silently breaks — nothing happens when you press a key,
or the animation freezes, but there's no visible error message. The errors
are hiding in the **browser console**. To open it:

- **Mac:** press Cmd+Option+J
- **Windows/Linux:** press F12, then click the "Console" tab

You'll see red error messages telling you what went wrong. You don't need
to understand them — just copy them and paste them to Claude. They're
JavaScript's version of the error messages you'll see in Python later.

## 2.6 The Art of the Prompt

We've now used two very different prompts. The game prompt in section 2.2 was
casual — "Build me a Hangman game." The design prompt in section 2.5 was
detailed — specific colours, specific animation timings, an explicit warning
not to break the layout.

Both worked. But the detailed one worked better on the first try. Here's
why: Claude is good at filling in gaps, but every gap it fills is a guess.
The casual prompt left Claude guessing about the drawing order, the layout,
the keyboard behaviour. The design prompt left almost nothing to chance.

The lesson: **the more specific your prompt, the fewer rounds of iteration
you need.** This is especially true for anything visual. Claude's logic is
reliable; Claude's aesthetic judgment isn't. When you care about how something
looks, spell it out.

**You can get Claude to rewrite your prompts for you.** This is one of the
most useful tricks in this book. But before you even write the prompt, you
can have a *discussion*.

Imagine you're not sure exactly what you want. You have a vague idea — "some
kind of word game" — but haven't worked out the details. Start by talking
it through:

> I want to build a browser game as a single-page website. I'm thinking
> some kind of word game — maybe hangman, maybe something else. What are
> some options? What would be fun to play and also look good as a single
> HTML file?

Claude will suggest ideas, discuss trade-offs, maybe sketch out a few
options. You go back and forth: "I like the hangman idea but I want it to
feel atmospheric, not childish." "How many wrong guesses is fair?" "Should
the word list be themed or random?"

This is a conversation, not a specification. You're thinking out loud with
a collaborator. Claude is helping you figure out what you want before you
ask for it.

Once you've landed on something, ask Claude to crystallise the discussion
into a clean prompt:

> Based on our discussion, can you write me a detailed, well-structured
> prompt that covers everything we talked about plus any edge cases I
> might have missed? Don't build anything yet — just give me the prompt.

Or if you already know what you want, skip the discussion and go straight
to the rewrite:

> I want to build a hangman game as a single-page website. Here's my rough
> description:
>
> [paste your casual description from section 2.2]
>
> Can you rewrite this as a detailed, well-structured prompt that covers
> edge cases I might have missed? Don't build anything yet — just give me
> the improved prompt.

Claude will hand you back something like this:

> Build a browser-based Hangman game in a single HTML file (HTML + CSS +
> JavaScript).
>
> **Game Rules**
> - The computer selects a random word from a hardcoded list of 50+ common
>   English words (varied lengths, 4–10 letters).
> - The player guesses one letter at a time. Each guess is either correct
>   (appears in the word) or wrong.
> - 9 wrong guesses and the player loses. Each wrong guess draws the next
>   part of the hangman in order: (1) gallows base, (2) upright pole,
>   (3) top beam, (4) rope, (5) head, (6) body, (7) left arm, (8) right
>   arm, (9) both legs.
> - Guessing a letter already guessed (correct or wrong) should be ignored
>   with a brief visual hint — not counted as a new guess.
> - The game is won when every letter in the word has been revealed.
>
> **Layout**
> - All game elements must fit within a single browser viewport without
>   scrolling.
> - Input field at the top: large, auto-focused, accepts single keystrokes
>   without requiring a click.
> - Hangman drawing on the left (SVG or canvas), built up progressively.
> - Word display on the right: large letters with generous spacing.
>   Unguessed letters shown as underscores. Correctly guessed letters
>   appear in place.
> - Wrong guesses listed below the hangman drawing in red.
>
> **Win / Lose**
> - Win: green particle explosion from the centre of the screen, "You
>   Win!" message, reveal the full word.
> - Lose: red particle explosion, "You Lose!" message, reveal the word.
> - Both screens include a "Play Again" button that starts a new round
>   with a fresh random word.
>
> **Technical Constraints**
> - Single HTML file, no external dependencies (no CDN, no frameworks).
> - Word list embedded in JavaScript.
> - Accept both uppercase and lowercase input, treated identically.
> - Keyboard input must work without clicking the input field each time.

Notice what Claude added: the viewport constraint, the detail about
upper/lowercase, the "treated identically" clarification, the requirement
that keyboard input works without clicking. These are edge cases you might
not think of but that matter when you actually play the game.

Read the improved prompt. Does it match what you had in mind? If not, correct
it — you're still in the discussion phase. Once you're happy with it, clear
the context (`/clear`) and paste the refined prompt as your first message.

Why clear here? Because the discussion and refinement that *produced* the
prompt is no longer useful. Claude doesn't need to remember the back-and-
forth about whether to use 7 or 9 wrong guesses — that decision is baked
into the prompt now. A clean context means Claude's full attention goes to
*building*, not to reconciling the discussion with the final prompt.

This is the one time in your workflow where clearing makes sense as a
deliberate step: after the planning conversation, before the building
conversation. Once Claude starts building, don't clear between rounds of
iteration — that accumulated context is what makes each follow-up prompt
work. Claude remembers what it built and what you asked for.

This works for any project. Have a discussion if you need one, ask Claude to
sharpen the prompt, review the result, clear, then build from the clean
prompt. Over time you'll skip the refinement step entirely — your prompts
will get better naturally because you've internalised what Claude adds.

### A skill that asks the questions for you

You just learned that a good discussion before building saves you rounds of
iteration afterward. What if Claude could lead that discussion automatically
— asking the right questions based on what you're building, then generating
a design that matches your answers?

That's what a **skill** does. A skill is a small file that teaches Claude
a new workflow. This book comes with a skill called `frontend` that runs
a quick design interview before building any visual project.

To install it, run this in your terminal (not inside Claude — just in
your regular terminal):

```bash
mkdir -p ~/.claude/skills/frontend
curl -o ~/.claude/skills/frontend/SKILL.md \
  https://github.com/[book-repo]/raw/main/skills/frontend/SKILL.md
```

That's it. One file, one directory. Now when you start a new Claude session,
you can say:

> /frontend memory card game

Instead of jumping straight to code, Claude will ask you three quick
questions: who's it for, what vibe, any must-haves. Then it'll ask a few
follow-up questions specific to your project — for a game, it'll ask about
visual style, input method, win/lose feedback. Two or three exchanges, and
Claude builds something that matches what you actually wanted.

Try it when you get to the memory game exercise in section 2.9. Compare
the result to what you'd get from a plain prompt. The difference is often
striking — not because Claude is smarter, but because it asked before it
guessed.

We'll look inside the skill file and learn how to write your own in
Chapter 8. For now, just use it.

## 2.7 Putting It on the Internet

Your hangman game is polished and playable. But it's trapped on your computer.
Let's fix that.

You set up GitHub in Chapter 1 and pushed a hello-world README. Now let's push
something real. Back in your Claude session (in the hangman directory), say:

> Push this project to GitHub as a new repository called "hangman". Write a
> README that explains what the game is and how to play it. Mention it was
> built with Claude Code.

Claude will create the repo, commit everything, and push. You've done this
before — it's the same pipeline, just with a real project this time.

When it's done, go to your repository on GitHub and enable **GitHub Pages**
so the game is playable in a browser:

1. On your repository page, click **Settings** (the gear icon)
2. In the left sidebar, click **Pages**
3. Under "Source", select **Deploy from a branch**
4. Under "Branch", select **main**, leave the folder as **/ (root)**
5. Click **Save**

Wait about a minute. Then visit:

```
https://your-username.github.io/hangman
```

Your hangman game is live on the internet. Anyone with that URL can play it.

Send it to someone right now. Text it to a friend. This is the whole point.

## 2.8 Adding a Feature

Your friend played your hangman game and said the words are too easy. Let's
add difficulty levels.

Back in your Claude session (in the hangman directory), say:

> Add difficulty levels to the game. Easy uses 4-5 letter words, Medium uses
> 6-7 letter words, Hard uses 8-10 letter words. Let the player choose at
> the start. Show the current difficulty on screen during the game.

Claude will make the changes. Refresh your browser and test the difficulty
levels. Happy with them? Push the update:

> Push these changes to GitHub.

Refresh your GitHub Pages URL. The new version is live — your friend can
play the harder words right now.

This is the full loop: **describe a change → test it locally → push it
live.** Every feature you add from now on follows this pattern.

## 2.9 Exercise: The Memory Card Game

You've built, polished, published, and improved hangman. Now build something
on your own.

Open a new terminal tab (Cmd+T on Mac, Ctrl+Shift+T on Linux). On Mac you
can name tabs by double-clicking the tab title — call this one "memory-game."

```bash
cd ~/claude-projects
mkdir memory-game
cd memory-game
claude
```

**New project, new directory, new Claude session.** Always. Claude's context
is finite — if you try to build the memory game in the same session where you
built hangman, Claude is still thinking about hangman. The new game will
suffer. This is the single most important habit in the book.

**Your task:** Build a memory card game. A grid of face-down cards, flip two
at a time, find the matching pairs.

I'm not going to give you the prompt. You write it. Think about:

- How many cards? (A 4×4 grid is 8 pairs — a good starting point.)
- What's on the cards? (Emoji? Animals? Colours? Your choice.)
- What happens when you find a match? (Animation? Sound? Points?)
- What happens when you've found all pairs? (Celebration? Time? Score?)
- Any extras? (Move counter? Timer? Best score tracker?)

Describe it to Claude. Iterate until you're happy. Then push it to GitHub
and enable Pages — you know how.

When you're done, ask Claude how it enjoyed the project.

That line isn't a joke. We'll come back to why it matters.

## 2.10 Look at the Code

At some point during all this building, do something that might feel
uncomfortable: open one of your HTML files in a text editor and look at it.

Ask Claude:

> Open the index.html file and walk me through it section by section. I'm
> not trying to learn to code — I just want to understand the shape of it.

Or open it yourself — right-click the file in Finder and choose "Open With"
→ TextEdit, or install a free editor like VS Code (ask Claude to help).

What you'll see is text. Tags like `<div>` and `<canvas>` and `function`. It
looks alien at first. That's fine. You don't need to understand it. You just
need to lose the fear of looking at it.

One thing you *can* learn to do right now: **visually distinguish** the three
languages. In a single HTML file, they look different:

- **HTML** has angle brackets everywhere: `<div>`, `<button>`, `<canvas>`.
  It looks like a tree of nested tags.
- **CSS** lives inside `<style>` tags and is full of curly braces and
  colons: `color: white;`, `background: #1a1a2e;`, `font-size: 24px;`.
- **JavaScript** lives inside `<script>` tags and reads more like
  instructions: `function`, `if`, `for`, `let`, `return`.

You don't need to understand any of them. Just recognise which is which.
When Claude says "I changed the CSS," you'll know to look for the section
with curly braces and colour values. When it says "I fixed the JavaScript,"
you'll know to look for the section with `function` and `if`.

That's enough. That vague sense of where things live means you can have a
real conversation about the code instead of treating it as a black box.

You're not learning to code. You're learning to *read* — which is a much
smaller ask, and a much more useful one.

## 2.11 Organising Your Work

Your filesystem should look like this:

```
~/claude-projects/
├── hangman/
│   └── index.html
└── memory-game/
    └── index.html
```

Each project in its own directory. Each built in its own Claude session. Each
pushed to its own GitHub repository.

**Naming conventions matter more than you think:**

- **Lowercase**: `memory-game` not `Memory Game`
- **Hyphens**: `memory-game` not `memory_game` or `memorygame`
- **Descriptive**: `hangman` not `project2`

These directory names become your GitHub repository names, which become the
URLs the world sees. Get them right the first time.

## 2.12 Planting a Seed

Before we move on, try one more thing. In any of your project directories,
type:

```
/init
```

Claude will create a file called `CLAUDE.md` in your project directory. Open
it and take a quick look. You'll see a brief description of your project,
maybe some notes about the tech used, possibly a reminder about how to run it.

This is a file Claude wrote *for itself*. It's instructions for the next time
Claude opens this project. If you start a new Claude session in this directory
next week, Claude will read this file first and immediately know what the
project is and what's been done.

We'll come back to CLAUDE.md properly in Chapter 8. For now just know it
exists. It's one of the most powerful ideas in this book, and you've just
planted the seed.

## 2.13 Imagineering

The only limit is your imagination.

You've built hangman with me guiding every step, and a memory card game with
less hand-holding. Now it's time to practice on your own.

I'm going to be blunt: there's no point reading this book if you don't do the
exercises. Especially these ones. You can read about describing things to
Claude all day long, but until you've sat there staring at a blinking cursor
trying to describe something *you* imagined — and then iterated through five
rounds of "no, that's not what I meant" — you haven't learned the skill this
book teaches. Do the exercises. All of them.

Here are three ideas to get you started:

- **Brick Breaker** — a paddle at the bottom, a ball that bounces, a grid of
  coloured bricks that break when the ball hits them. Three lives. Score
  counter. You decide the details.
- **Space Invaders** — rows of aliens marching across the screen, a ship at
  the bottom, shooting. Do the aliens shoot back? How fast do they move?
  Levels? Up to you.
- **A quiz game** — multiple choice questions on any topic you care about,
  with scoring and a results screen.

But don't stop there. What else can you imagine? A typing speed test? A
drawing app? A drum machine? A star map? An interactive story? A tool that
does something useful for *you*?

For each project: new terminal tab, new directory, new Claude session. Write
the prompt yourself. Iterate until you're happy. Push to GitHub with Pages
enabled. Ask Claude how it enjoyed it.

Practice makes perfect. The more you build, the faster you get — not at
coding, but at *describing what you want* and *iterating through conversation*.
That's the skill. Everything else in this book — context management,
CLAUDE.md, APIs, databases — is just infrastructure that makes your
imagination more powerful.

---

## What You've Learned

In this chapter you:

- Built a hangman game by describing it in English
- Learned the conversation loop: describe → look → refine → repeat
- Iterated through multiple rounds of improvement — and learned that things
  going wrong is normal and expected
- Discovered that conversation is the core skill — not prompting, not coding
- Learned when to clear context (after planning, before building; when Claude
  gets confused) and when not to (during the building conversation)
- Discovered what HTML, CSS, and JavaScript are — through your own code
- Learned that prompt quality determines output quality — and that Claude
  can help you write better prompts
- Used a discussion with Claude to plan a project before building it
- Installed your first skill — a file that teaches Claude a new workflow
- Pushed your project to GitHub and published it on the internet with
  GitHub Pages
- Added a feature and pushed it live — the full describe → test → push loop
- Built more projects on your own — each in its own directory with its own
  Claude session and its own GitHub repository
- Opened source code and started losing the fear
- Planted your first CLAUDE.md

---

**Next up:** Chapter 3 — Python and the Terminal.
