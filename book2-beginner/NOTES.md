# Book 2 Working Notes

## Key Decisions

- **Chapter 1**: Install + first website + GitHub Pages, all in one sitting.
  One arc: setup → create → share.

- **Chapter 2**: Python and C console apps. The "peak" of Chapter 2 is a
  complex project (roguelike dungeon or similar) that deliberately requires
  debugging through conversation. Teaches: "When Claude Gets It Wrong" —
  paste the error back, describe what's wrong, iterate.

- **Compiled vs interpreted**: Maze generator in C, then the same in Python.
  Don't tell Claude which algorithm to use — let it choose, then ask about
  alternatives. Left-hand wall rule for solving — it will fail on some mazes,
  which becomes a natural learning moment.

- **Things Claude can just DO don't need scripts**: File organising, disk
  analysis — just ask Claude directly. Python scripts are for things that
  justify being a program (games, tools you'd re-run, things that are
  interactive).

- **Open the code and look at it**: Throughout Chapter 2, encourage the reader
  to open the source files and look. Not to learn, just to see. Lose the fear.
  Then ask Claude to walk through it line by line. Progression: password
  generator (readable) → maze.c (alien) → Sudoku solver (the algorithm is
  20 lines).

- **Ask Claude which algorithm it used, then ask about alternatives**: This
  pattern recurs. Mazes, Sudoku, sorting — Claude picks one, reader explores
  after the fact. This is the collaborator model.

- **"After each project ask Claude how it enjoyed it"**: Recurring motif.
  Not a joke.

## Chapter 1 Example Projects — Single-Page Websites

### First project (guided)
- Personal link tree — the one everyone does first, shareable immediately

### Games (single HTML file — the reader builds ALL of these)
1. Snake — arrow keys, growing tail, score
2. Whack-a-mole — circles pop up, click them, timer + score
3. Memory card game — flip pairs, find matches
4. Breakout / brick breaker — paddle, ball, bricks, canvas animation
5. Hangman — guess the word, ASCII drawing builds with wrong guesses
6. Quiz — multiple choice, scoring, themed (reader picks topic)

---

## Chapter 2 Example Projects

### Python
- Password generator (simple, useful, one-shots)
- Text-based RPG / dungeon crawler (complex, will need debugging)
- Sudoku solver (animated backtracking in terminal)
- Game of Life (curses animation, load patterns from .txt files)
- Typing tutor (curses, real-time input, WPM scoring)
- ASCII art converter (pip install Pillow, takes image file as argument)
- Word ladder (needs dictionary file, BFS)
- Expense tracker / habit tracker (re-runnable tools)

### C (compiled vs interpreted)
- Maze generator + left-hand-wall solver (then same in Python for speed comparison)
- N-Queens — all solutions for N=8 instant, N=14+ shows C vs Python speed gap
- Knight's tour (Warnsdorff's rule vs brute force)

### "Just ask Claude" (no script needed)
- Organise my Downloads folder
- Show me what's using disk space
- Find duplicate files
- Batch rename photos

## Appendices

1. **Introduction to Unix** — drawn from cs_foundations_guide.md. Kernel,
   shell, filesystem, processes, essential commands.
2. **Windows Installation** — WSL setup, how Windows architecture differs
   from Unix, "still read the Unix appendix."
3. **Elementary Principles of Programming** — variables, types, conditionals,
   loops, functions, errors. Python examples. Concepts not mastery. "You don't
   need to memorise this. Claude writes the code. But understanding these
   concepts lets you read what Claude writes."
4. **GitHub, GitHub Pages, CI/CD, PR Reviews** — step by step, probably needs
   a skill to walk them through it.

## GitHub (Chapter 1, after first website)

**Naming matters. You can't change it later.**

- Your GitHub **username** is permanent. Choose carefully. Lowercase,
  professional-ish, something you'd put on a CV.
- **Repo names** are technically changeable but it breaks all your links
  and is annoying. Get it right first time. Lowercase, hyphenated,
  descriptive: `snake-game` not `project1` or `myGame`.
- Every repo MUST have:
  - A short description (the one-liner on GitHub, under the repo name)
  - A README.md (even a few sentences is fine — what is this, how to run it)

**The GitHub commit skill / checklist:**

Before every commit and push, the reader (or a skill) should verify:

1. **Right project → right repo.** You're pushing snake-game to snake-game,
   not accidentally to your link-tree repo. Check with `git remote -v`.
2. **README exists.** If there's no README, write one first. Even just:
   "Snake game built with Claude Code. Open index.html to play."
3. **Commit message makes sense.** The commit message (the short summary
   text that describes what changed) should be readable by a stranger.
   "Add snake game with score tracking and game over screen" — good.
   "stuff" — bad. "asdf" — very bad. This text is permanent and public.
4. **Nothing secret is being committed.** No API keys, no passwords, no
   personal data. Claude should check for this automatically.

We should build a simple skill or checklist prompt that walks the reader
through this every time until it becomes habit. Something like:

```
Before we push to GitHub, let's check:
- What repo are we pushing to? (show me `git remote -v`)
- Is there a README.md?
- Show me the commit message you're about to use.
- Are there any files that shouldn't be public?
```

**GitHub Pages:** After pushing, turn on GitHub Pages in repo settings.
The reader's website is now live at username.github.io/repo-name.
This is the payoff of Chapter 1 — "I made this and anyone can see it."

---

## Filesystem Organisation (introduce early, reinforce throughout)

The reader should organise their work like this:

```
~/claude-projects/
├── single-web/
│   ├── link-tree/
│   ├── snake/
│   ├── whack-a-mole/
│   ├── memory-game/
│   ├── breakout/
│   ├── hangman/
│   └── quiz/
├── console-python/
│   ├── password-gen/
│   ├── dungeon/
│   ├── sudoku/
│   ├── maze/
│   └── institute/        ← Chapter 3 game
└── console-c/
    ├── maze-c/
    └── nqueens/
```

**THE RULE: One project, one directory, one Claude session.**

Never re-use a Claude instance that has already done work on a different
project. Never work on two projects in the same conversation. When you
start a new project:

1. Open a new terminal (or exit Claude with /exit)
2. `mkdir` the new project directory
3. `cd` into it
4. `claude`

This is the first lesson in context management. Claude's context window is
finite. If you've been building Snake and then say "now make me Breakout,"
Claude is still thinking about Snake. The Breakout code will be worse
because Claude's attention is split.

A fresh directory + a fresh session = Claude's full attention on YOUR project.

This sounds fussy. It is the single most important habit in the book.
Chapter 8 explains why in depth, but start doing it now.

## First CLAUDE.md (Chapter 1, after first website)

As early as the first single-page website, have the reader run `/init`.
Claude generates a CLAUDE.md for the project. The reader opens it and
takes a quick look — just to see it, not to understand every line.

"This is a file Claude wrote for itself. It's instructions for the next
time Claude opens this project. We'll come back to this in Chapter 9,
but for now just know it exists."

Plant the seed early. Don't explain it yet.

## .env and API keys

Don't discuss .env or secrets in Chapter 1. Wait until API keys come up
naturally (probably Chapter 5 - Working with Data, or Chapter 7 - Full-Stack
Web App when they need a database password or external API key). Then
explain .env, .gitignore, and why secrets must never be committed.

---

## Setup Tips (Chapter 1)

- **Explanatory mode**: Tell reader to type `/config` and set output style
  to "explanatory" (or whatever the exact setting is). Claude explains what
  it's doing as it goes. Essential for a learning book.

- **Permissions**: Claude asks permission for everything by default. Options:
  - Say yes each time (safest, but tedious)
  - Configure in settings.json to allow specific tools (e.g. `bash *`)
  - Robin's approach: allow everything (`bash *`) — mention this is the
    "I trust Claude, just do it" option
  - Show the reader how to find and edit settings.json
  - Recommend a middle ground for beginners: allow file read/write and
    bash, but keep the prompts for destructive stuff (delete, git push)
  - Revisit this properly in Chapter 8 (context) or Chapter 9 (CLAUDE.md)

## Philosophy (woven throughout)

- Claude is a collaborator, not a tool
- You don't need to know how to code — you need to know what you want
- Claude works better when it's having fun
- The quality of your description determines the quality of the result
- Conversation IS debugging
- Start new sessions for new tasks
- Look at the code — you don't need to understand it, just lose the fear
