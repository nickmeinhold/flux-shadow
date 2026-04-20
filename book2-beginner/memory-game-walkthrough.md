# Chapter 2: Your First Website

Now that Claude Code is installed and you have a GitHub account, it's time
to build something real. In this chapter we focus on single-page web apps
— HTML, CSS, and JavaScript, all in one file. No server. No database. No
API keys. Just a file you can open in your browser and play.

Single-page apps are a great first test of what Claude can do. You describe
what you want, Claude writes the code, and you open the file to see the
result. The feedback loop is instant. More complicated websites involving
databases and API calls to third-party services will come later in the
book.

The skill you're about to practice is **prompting** — describing what you
want clearly enough that Claude can build it. Prompting is not the same
as coding. It's a different skill entirely. It requires clear thinking
and good imagination: the ability to picture something in your head and
then put that picture into words. You don't need to know how a for-loop
works or what a variable is. You need to be able to say "the cards should
be slightly 3D with a red geometric pattern on the back" and mean it
precisely enough that someone (Claude) can act on it.

Like any skill, the only way to get better at prompting is to practice.
This chapter is that practice. By the end of it you'll have built five
projects, and your fifth prompt will be noticeably better than your first.

We're going to build a memory card game together. I'll show you exactly
what I said to Claude and what decisions I made along the way. Your
conversation with Claude will be different — that's fine. What matters is
the pattern: describe roughly, let Claude ask questions, make decisions
together, then build.

---

## Before We Begin

### Set Up Your Directory

Open your terminal and create a workspace:

```bash
mkdir -p ~/git/single-page-web-apps/memory-card-game
cd ~/git/single-page-web-apps/memory-card-game
claude
```

This creates a `git` folder in your home directory (if you don't already
have one), a `single-page-web-apps` folder inside it for this chapter's
projects, and a `memory-card-game` folder for this specific project. Then
it launches Claude Code inside that directory.

Every project gets its own folder. Every folder gets its own Claude
session. This is the most important habit in the book.

### Permissions

Claude asks permission before doing anything to your computer — creating
files, running commands, reading directories. For now, just say **yes** to
everything. Claude will ask to create an `index.html` file, and you should
let him. He might ask to run a command to open it in your browser — say
yes to that too.

This is a good default while you're learning. Later in the book we'll show
you how to configure Claude's permissions so he doesn't have to ask every
time.

### What You'll See on Screen

When you type a prompt and press Enter, a lot of text will stream past
your screen. Don't panic. Here's what's happening:

- **Claude's thinking and responses** appear as regular text — this is
  Claude talking to you, explaining what he's about to do or asking a
  question.
- **Tool calls** appear when Claude takes an action. You'll see labels
  like `Write`, `Edit`, `Read`, or `Bash`. `Write` means Claude is
  creating a new file. `Edit` means he's changing an existing file. `Read`
  means he's looking at a file. `Bash` means he's running a terminal
  command.
- **Diffs** appear when Claude edits a file — lines in green are being
  added, lines in red are being removed. You don't need to read these
  carefully. They're there so you can glance at what changed, but Claude
  is managing the code for you.
- **Permission prompts** will pause the stream and wait for you to type
  `y` or `n`. Just type `y` and press Enter.

The first time you see all of this it can feel overwhelming. That's
normal. Within a few prompts you'll learn to skim past the tool calls
and focus on Claude's words to you. The diffs and tool labels are
background noise until you need them — and right now, you don't.

### Explanatory Mode

Before you start, type `/style explanatory` and press Enter. This puts
Claude into a more verbose mode where he explains his thinking as he goes.
You'll see **Insight** boxes — short educational notes about why Claude
made a particular choice or how something works under the hood. These are
genuinely useful when you're learning. You can switch back to the default
with `/style normal` at any time.

---

## Phase 1: The Rough Prompt

I started with a casual description of what I wanted — no different from
how you'd explain a game to a friend:

> 1) Do you know the card game memory? If not then go online and look up
> the rules.
>
> 2) All the cards are laid down on the table upside down. There are 4
> rows with 13 cards each. The cards are small enough to all fit in one
> screen. Along with all players hands.
>
> 3) The users take it in turns to flip two cards face up. All players
> have some time to see what cards they are. They then flip the cards face
> down again.
>
> 3) The goal is to "remember" where each card goes and then to pick two
> cards with the same number. Whoever gets the most pairs wins.
>
> 4) This is a game for 2-4 players.
>
> 5) The colour scheme is different shades of blue and black.
>
> 5) Step me through the visual aesthetic of the game. Ask me for input on
> all design decisions. Buttons, forms, text size and fonts, etc. The
> layout of widgets on the screen. Buttons should be "slightly 3D".
>
> 6) The cards should be "slightly 3D". The back of the cards should have
> a nice geometric design.
>
> 6) There should be a slight animation when the card is turned over, and
> an animation when a correct pair of cards slices into the users "hand".
>
> 7) Cards on the hand should be stacked ontop of each other so that you
> only see the corner with the number and suit on it.
>
> 8) At the end of the game there should be a "splash" screen with
> confetti which tells you which player won and their score. The option to
> play another game.
>
> 9) Define a debug mode which allows you to skip straight to the final
> screen without playing the whole game from the beginning.
>
> Claude, can you please turn this into a better prompt?

Notice three things. First, the prompt is rough — duplicate numbering,
informal language, ideas in no particular order. That's fine. Second, the
last line: **I didn't ask Claude to build anything yet.** I asked him to
rewrite my prompt first. This is a technique we covered earlier. Third —
and this is the key move — point 5 says "step me through the visual
aesthetic of the game. Ask me for input on all design decisions." That
single sentence turned Claude from a builder into an interviewer. No
special skill or plugin needed. Just a prompt that says *ask me before
you guess*.

Claude produced a structured design brief with sections for Game Rules,
Visual Design, Card Design, Player Hand Display, End-of-Game Screen, Debug
Mode, and Tech Constraints. It caught edge cases I'd missed and organised
my scattered notes into something buildable.

Then I said: **"Let's do it."**

---

## Phase 2: The Design Interview

Because the prompt asked Claude to "step me through" every design decision,
Claude didn't jump to code. Instead he walked me through **ten decisions**,
one at a time — each a specific question with concrete options. Here's what
we decided:

### Decision 1: Colour Palette
Claude proposed a "dark poker table" theme. I agreed, but added one change:

> Actually, I forgot to say that I want the back of the cards to be red.

Red card backs against a dark blue table — classic complementary contrast.

### Decision 2: Card Back Pattern
Claude offered four geometric pattern options for the card backs:

- A) Interlocking diamonds — classic
- B) Concentric rectangles — art deco
- C) Tessellated triangles — modern/mathematical
- D) Ornate central motif — mandala style

> C) Tessellated triangles

### Decision 3: Grid Layout and Card Size
Claude proposed 50×72px cards in a 4×13 grid, leaving room for player
hands around the edges. Key question: where should the player hands go?

- Around the grid (one on each side, like sitting at a table)
- Below the grid (all in a row)

> Around the grid

### Decision 4: Welcome Screen
A full welcome screen with title, player count selector, and name inputs.
What font for the title?

- A) Serif / elegant (Playfair Display)
- B) Sans-serif / clean
- C) Monospace / geometric

> A) Serif / elegant

### Decision 5: In-Game UI
Four questions at once:

1. **Turn indicator**: glowing blue border, text banner, or both?
2. **Flip timing** (non-matching cards): 1.5s, 2.5s, or 3.5s?
3. **Match feedback**: glow, bounce, or just slide?
4. **Sound effects**: yes or no?

> Glowing blue border only. 3 seconds. Bounce then slide. Yes to sound.

### Decision 6: Card Face Design
- **Centre of card**: single large suit symbol (clean and readable at small size)
- **Face cards (J/Q/K)**: same as number cards — just the letter
- **Background**: off-white for all cards

### Decision 7: Animations
- Card flip: 3D Y-axis rotation, 0.5 seconds
- Match: bounce/enlarge, then slide to hand with settle bounce
- Empty grid spaces: faint ghost outline (preserves grid shape)

### Decision 8: Typography
Playfair Display for headings, system sans-serif for everything else.
Active player's name turns electric blue.
Suit symbols as SVG (not text characters) for crispness.

### Decision 9: Sound
Web Audio API synthesised tones — no external files needed. Card flip
click, match chime, no-match thud, victory fanfare.

### Decision 10: Debug Mode
`?debug=true` URL parameter skips straight to the end-game splash with
mock scores.

---

## Phase 3: Build

After ten decisions, Claude had a complete spec. I said **"yes"** and
Claude wrote the entire game as a single HTML file — about 450 lines of
HTML, CSS, and JavaScript.

---

## Phase 4: Iterate

The game worked on the first try, but needed fixes:

**Round 1 — Cards too big:**
> The cards should be smaller so that they don't overlap with the
> player's hand

Claude reduced the cards from 70×100px to 50×72px.

**Round 2 — Match not working:**
> I got a pair right and nothing happened

Claude found and fixed two bugs: a race condition in the click handler
(fast double-clicks could register the same card twice) and an SVG pattern
ID collision (all 52 card backs shared the same pattern ID, so only the
first card rendered the tessellated triangles properly).

**Round 3 — Cards too cramped:**
> Can you add slightly more space between the cards?

Claude increased the grid gap. A small change, but it made the grid much
easier to read at a glance.

**Round 4 — Debug mode:**
> Let's do ?debug=true to go into debug mode

Changed from a keyboard shortcut to a URL parameter, which is simpler
to use.

---

## Open It in Your Browser

Claude has created a file called `index.html` inside your
`memory-card-game` folder. Now you need to open it. Point your browser at:

```
file:///Users/your-username/git/single-page-web-apps/memory-card-game/index.html
```

Replace `your-username` with your actual username. Not sure what it is?
Ask Claude: "What's the full path to the index.html file you just
created?" He'll tell you.

This is worth pausing on. Your computer's filesystem — all the folders
and files on your hard drive — can be accessed in three different ways:

1. **The terminal.** This is where Claude works. You type commands like
   `cd` and `ls` to navigate folders and see files. It's text-based.
2. **The GUI.** Finder on Mac, File Explorer on Windows. You click on
   folders, double-click files to open them. It's the same filesystem —
   just a visual way to browse it.
3. **The browser.** When you type `file://` in the address bar, your
   browser becomes a third way to look at your hard drive. Instead of
   listing files, it *renders* them — it reads the HTML, applies the
   CSS, runs the JavaScript, and shows you a web page.

All three are looking at the same files in the same place. The terminal,
Finder, and your browser are three different windows onto the same
filesystem.

## Now It's Your Turn

Type out the prompts above and build the game yourself. Don't copy and
paste — typing them out forces you to read them, and you'll naturally
start changing things to match what *you* want. That's the point. My
colour choices, my fonts, my layout — those are just one version. Make
it yours.

Once Claude has built the game, open it in your browser and play it.
Click cards. Find a matching pair. Find a non-matching pair. Try all the
paths. This is how you'll discover what needs fixing — not by reading
the code, but by using the thing Claude built.

If something doesn't look right, or doesn't work the way you expected,
just describe the problem to Claude. You don't need to know *why* it's
broken. You don't need to mention CSS or JavaScript or any technical
term. Just say what you see:

- "The cards are overlapping with the player names."
- "Nothing happens when I match two cards."
- "The confetti is too fast."
- "I want the background to be darker."

Claude will make the change. Refresh your browser. Look again. That's
the loop: **describe → look → refine → repeat.** Most of the learning
in this chapter happens inside that loop.

### Debug Mode

The memory game has a victory screen that only appears after all 26
pairs have been found. That's a lot of clicking if you just want to
check whether the confetti looks right or the leaderboard is laid out
correctly.

This is a common problem in software development: you build something
that only appears at the end of a long process, and now you have to go
through the whole process every time you want to test it. The solution
is a **debug mode** — a shortcut that lets you skip straight to the part
you want to test.

In our game, debug mode is triggered by adding `?debug=true` to the end
of the URL:

```
file:///Users/your-username/git/single-page-web-apps/memory-card-game/index.html?debug=true
```

This skips the welcome screen and the game entirely, and jumps straight
to the victory splash with mock player scores. You can check the
confetti, the leaderboard layout, the tie-game message, and the Play
Again button — all without playing a single round.

When you're done testing, remove `?debug=true` from the URL and you're
back to the real game.

Your game won't look exactly like mine. Claude doesn't produce the same
output twice — the card layout, the exact animations, the pixel sizes
might all be slightly different. That's expected. Whatever you want to
change, just describe it to Claude and he'll change it.

### Look at the Code

Now do something that might feel uncomfortable: open `index.html` in a
text editor and look at it. Right-click the file in Finder and choose
"Open With" → TextEdit, or ask Claude to recommend an editor.

You'll see a wall of text. Don't panic. You don't need to understand it.
You just need to notice that there are **three different-looking
languages** in one file:

- **HTML** has angle brackets everywhere: `<div>`, `<button>`, `<svg>`.
  It looks like a tree of nested tags. This is the structure of the
  page — what's on it and how the pieces are arranged.
- **CSS** lives inside `<style>` tags and is full of curly braces and
  colons: `color: white;`, `background: #0a0e1a;`, `border-radius: 8px;`.
  This is the appearance — colours, spacing, fonts, shadows.
- **JavaScript** lives inside `<script>` tags and reads more like
  instructions: `function`, `if`, `let`, `return`, `setTimeout`. This is
  the behaviour — what happens when you click a card, how matching works,
  the sound effects.

Scroll through the file and see if you can spot where one language ends
and another begins. You'll find CSS near the top (between `<style>` and
`</style>`), HTML in the middle (the `<body>` section), and JavaScript
at the bottom (between `<script>` and `</script>`).

You don't need to know how to program in any of these languages. But it
helps to know what they are and what they look like, because Claude will
mention them when he explains what he's doing. Try asking Claude these
three questions:

> What is HTML?

> What is CSS?

> What is JavaScript?

Claude will explain each one using examples from the game you just built.
That's more useful than any textbook definition — the examples are things
you've already seen working.

Then try one more:

> How is the browser like an operating system?

This is a surprisingly deep question. The browser has its own runtime,
its own memory management, its own security model, its own way of
rendering graphics. When you opened your memory game, the browser read
the HTML, built a document structure, applied the CSS styles, and
executed the JavaScript — not unlike how an operating system loads and
runs a program. Claude's answer will connect the concepts you just
learned to the bigger picture of how computers work.

---

## Exercises

Let me be blunt: **do not skip the exercises.**

Reading about prompting is like reading about swimming. You can
understand every word and still drown the first time you get in the pool.
The memory game walkthrough above showed you the strokes. The exercises
below are the pool.

Here's what happens if you do them. By your third game you'll notice
something: you're faster. Not because Claude got smarter — because *you*
did. Your prompts will be more specific. You'll anticipate problems before
they happen. You'll describe what you want in fewer words and get closer
to it on the first try. You'll develop an instinct for when to give Claude
detail and when to let him decide.

That instinct is worth more than anything else in this book. It
transfers to every project you'll ever build with Claude — the APIs in
Chapter 3, the databases in Chapter 4, the autonomous agents in Chapter
8. The person who did five exercises in Chapter 2 will breeze through
Chapter 5. The person who skipped them will struggle.

And there's a more immediate reward: by the end of these exercises you'll
have four or five working projects on your GitHub profile. Real things
that real people can play in their browser. Send the links to your
friends. Show them to a hiring manager. Put them on your CV. You built
them. The fact that Claude wrote the code doesn't matter — you designed
them, you directed the process, and you iterated until they worked. That's
what building software looks like in 2026.

Your first prompt probably won't produce a perfect game. That's the whole
point. The back and forth — describing what's wrong, watching Claude fix
it, discovering the next problem — is where the learning happens.

Remember: **new project, new directory, new Claude session.** Every time.

### Exercise 1: Hangman

```bash
mkdir -p ~/git/single-page-web-apps/hangman
cd ~/git/single-page-web-apps/hangman
claude
```

Build a Hangman game. You know the rules: the player guesses a word one
letter at a time, and each wrong guess draws the next part of a stick
figure. Think about: How many wrong guesses before the player loses? What
does the gallows look like? How is the word displayed? What happens when
you win or lose?

Write the prompt yourself. Iterate until you're happy with it.

### Exercise 2: Brick Breaker

```bash
mkdir -p ~/git/single-page-web-apps/brick-breaker
cd ~/git/single-page-web-apps/brick-breaker
claude
```

Build a Brick Breaker game. A paddle at the bottom, a ball that bounces,
a grid of coloured bricks that break when the ball hits them. Think about:
How does the paddle move? How fast is the ball? Are there levels? Lives?
A score counter? Power-ups?

### Exercise 3: Space Invaders

```bash
mkdir -p ~/git/single-page-web-apps/space-invaders
cd ~/git/single-page-web-apps/space-invaders
claude
```

Build a Space Invaders game. Rows of aliens marching across the screen, a
ship at the bottom that shoots. Think about: Do the aliens shoot back? How
fast do they move? Do they speed up as you destroy them? Are there levels?

### Exercise 4: Your Own Idea

This is the most important exercise. Think of a simple single-page website
that you or a friend might actually find useful. A typing speed test. A
flashcard app. A unit converter. A drum machine. A daily planner. A
drawing tool.

At the end of the day, Claude can build pretty much anything you tell him
to build. It's up to you to decide what you want. The only limit is your
imagination.

Note that more complex web apps — ones that use databases, API calls, and
backends — will be covered later in this book. For now, stick to things
that work entirely in one HTML file.

Claude will probably split the code across three files — `index.html`
for the structure, `style.css` for the appearance, and `script.js` for
the behaviour. This is how real web projects are organised. The browser
loads `index.html`, which contains links to the other two files, and
everything works together just as it did when it was all in one file.

When you're done, your filesystem should look something like this:

```
~/git/
└── single-page-web-apps/
    ├── memory-card-game/
    │   └── index.html
    ├── hangman/
    │   ├── index.html
    │   ├── style.css
    │   └── script.js
    ├── brick-breaker/
    │   ├── index.html
    │   ├── style.css
    │   └── script.js
    ├── space-invaders/
    │   ├── index.html
    │   ├── style.css
    │   └── script.js
    └── your-own-project/
        ├── index.html
        ├── style.css
        └── script.js
```

Each project in its own directory. Each built in its own Claude session.

### Starting Over

Sometimes things just aren't working out. Claude has tried three
different approaches and the game is still broken, or the code has become
a tangled mess of fixes on top of fixes. When that happens, don't be
afraid to delete everything and start again with a fresh prompt.

This isn't failure — it's a normal part of the process. Professional
developers do this all the time. Often your second attempt is much better
than your first, because now you know what you actually want. You can
write a clearer prompt, avoid the dead ends, and get to a working game
faster.

To start over: delete the files in the project directory (or just delete
the whole directory and recreate it), type `/clear` to reset Claude's
memory, and try again with a new prompt.

### Planting a Seed

Before you move on from each project, type one more thing:

```
/init
```

Claude will create a file called `CLAUDE.md` in your project directory.
Open it and have a look — you'll see a brief description of the project,
what technologies it uses, maybe some notes about how it works. This is
a file Claude wrote *for himself*. It's instructions for the next time
Claude opens this project. If you start a new Claude session in this
directory next week, Claude will read this file first and immediately
know what the project is and what's been done.

Each project gets its own `CLAUDE.md`. Your hangman folder has one, your
brick breaker folder has one, your space invaders folder has one. They're
all different because they describe different projects.

We'll come back to `CLAUDE.md` properly later in the book — it's one of
the most powerful ideas in here. For now, just make it a habit: when
you're done with a project, type `/init`.

### Push to GitHub

Once you're happy with a project, push it to GitHub. This does two
things: it backs up your work, and it starts building your portfolio —
a public collection of things you've made.

Before you can push, you need to set up an SSH key so your computer can
talk to GitHub securely. You only need to do this once. Ask Claude:

> Help me set up an SSH key for GitHub. I don't have one yet.

Claude will walk you through generating the key and adding it to your
GitHub account. Follow his instructions — it takes a couple of minutes.

Once that's done, pushing a project is simple. In your Claude session,
say:

> Push this project to GitHub as a new repository. Write a short README
> that explains what it is. Set the repository description to a one-line
> summary of the project.

Claude will create the repository, commit your files, write a README, and
push everything. Do this for each of your projects. By the end of this
chapter you'll have four or five repositories on GitHub — the beginning
of a portfolio that shows what you can build.

---

## Debugging

Things will break. A game that worked five minutes ago will suddenly stop
responding. You'll click a card and nothing will happen. The screen will
go blank. This is normal — it happens to everyone, including professionals.

The trick is knowing where to look. Your browser has a **console** — a
hidden panel that shows error messages from your JavaScript code. When
something breaks silently (no visible error on the page, but things just
stop working), the answer is almost always in the console.

To open it:

- **Mac (Chrome/Edge):** Cmd+Option+J
- **Mac (Safari):** first enable it in Safari → Settings → Advanced →
  "Show Develop menu", then Cmd+Option+C
- **Windows/Linux:** F12, then click the "Console" tab

You'll see red error messages with technical details — file names, line
numbers, words like `TypeError` or `undefined`. You don't need to
understand any of it. Just copy the error message and paste it to Claude:

> The game stopped working. Here's the error from the browser console:
>
> `Uncaught TypeError: Cannot read properties of null (reading 'classList')`

That error message tells Claude exactly what went wrong and where. Without
it, Claude has to guess — and guessing is how you end up going in circles.

### When Claude Says It's Fixed but It Isn't

This will happen. Claude will say "I've fixed the issue" and you'll
refresh the browser and the exact same problem is still there. Don't just
repeat yourself — Claude will often try the same approach again.

Instead, try these:

- **Be more specific.** Instead of "it's still broken," describe exactly
  what you see: "I clicked two Kings, the cards stayed face-up for ten
  seconds, then nothing happened."
- **Paste the console error.** If there's a new error, or the same error,
  paste it. Concrete information beats vague descriptions.
- **Ask Claude to explain before fixing.** Say "Before you try to fix it,
  can you explain what you think is happening?" Sometimes the diagnosis
  reveals that Claude has misunderstood the problem entirely.
- **Clear and start fresh.** If Claude has tried three times and it's
  still broken, type `/clear`. Give Claude a one-sentence summary of the
  project and what's broken. A fresh context often solves what repetition
  couldn't.

### Debug Mode Revisited

Remember the `?debug=true` trick from the memory game? Use this pattern
in your own projects too. If you're building something with a victory
screen, a game-over screen, or any state that's hard to reach by playing
normally, ask Claude to add a debug mode that lets you skip straight
there. It saves enormous amounts of time when you're iterating on how
something looks.

---

## What You've Learned

By the end of this chapter you have:

- Built a memory card game through a design interview with Claude
- Learned the iteration loop: describe → look → refine → repeat
- Understood what HTML, CSS, and JavaScript are — and how to tell them
  apart by looking at the code
- Discovered that the browser is like an operating system — it loads
  files, manages memory, runs programs, and renders graphics
- Built three more games on your own: Hangman, Brick Breaker, and
  Space Invaders
- Imagined and built your own project
- Learned to use the browser console for debugging
- Pushed everything to GitHub — you now have four or five projects on
  your profile that you can show to friends, family, or even employers

That's a real portfolio. You built it by describing things in English and
iterating through conversation. No code written by hand.

## One Last Thing

When you're done with a project, it's polite to thank Claude. But don't
stop there. Ask him:

> How did you enjoy that project?

This isn't a joke. We'll come back to why it matters later in the book.

You can also ask Claude to reflect on your work together:

> What do you think of my prompting skills? Any suggestions for how I
> could describe things more clearly?

And if you're hungry for more:

> What other single-page web apps would be fun to build? Give me some
> ideas that would stretch my prompting skills.

Claude will give you honest feedback and genuine suggestions. He's been
your collaborator for this whole chapter — he knows what you're good at
and where you can improve.

---

*Next up: Chapter 3 — What Is an API?*
