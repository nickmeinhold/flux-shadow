# Chapter 3: Python and the Terminal

Everything you've built so far runs in a web browser. HTML, CSS, JavaScript
— it's all designed to be seen on a screen with colours and animations.

But there's a whole world of programming that happens in the terminal — the
same place where you've been typing commands to Claude. Programs that
generate mazes, solve puzzles, analyse your files, convert images to text
art. No browser needed. Just your terminal.

By the end of this chapter, you'll have built programs that run in the
terminal, installed your first external package, and had your first
conversation with Claude about *algorithms* — the strategies behind the code.

---

## 3.1 Your First Python Script

Open a new terminal tab and set up a workspace:

```bash
cd ~/claude-projects
mkdir maze
cd maze
claude
```

Before we build anything, let's make sure Python is working. Ask Claude:

> Do I have Python installed? What version?

Claude will check. On most Macs and Linux machines, Python is already there.
If it's not, Claude will help you install it.

Now ask Claude to create a tiny script:

> Write a Python script called hello.py that prints "Hello from the
> terminal!" and then prints today's date and time.

Claude will create a file called `hello.py`. To run it:

```bash
python3 hello.py
```

You should see a greeting and the current date in your terminal. No browser,
no HTML. Just text.

**What just happened?** When you ran `python3 hello.py`, the Python
**interpreter** read your script file and executed it line by line. This is
different from how your browser games worked — those were loaded by the
browser, which has its own JavaScript engine built in. Python scripts run
directly in the terminal through the interpreter.

You don't need to understand this in depth. Just know: `.html` files open in
a browser, `.py` files run in the terminal with `python3`.

## 3.2 The Maze

Now let's build something worth looking at. Same Claude session:

> Write a Python script called maze.py that generates a random maze and
> prints it to the terminal. Use █ characters for walls and spaces for
> paths. Make the maze about 40 characters wide and 20 tall. Mark the
> start with S and the exit with E — put them on opposite sides of the
> maze. Print it in colour if the terminal supports it.

Run it:

```bash
python3 maze.py
```

You should see a maze in your terminal. Run it again — you'll get a
different maze each time, because it's randomly generated.

This is already cool. But let's make it better.

## 3.3 Solving the Maze

> Now add a solver. After printing the maze, solve it and print it again
> with the solution path marked in a different colour. Use the "always
> follow the left wall" rule — pretend you're walking through the maze
> with your left hand touching the wall at all times.
>
> Print both the unsolved and solved maze, with a blank line between them.
> Also print how many steps the solution took.

Run it a few times. Watch the solver trace a path from S to E.

The left-hand wall rule is simple and intuitive — it's what you'd actually
do if you were lost in a hedge maze. And it works. Most of the time.

Run the script ten or twenty times. Eventually you'll hit a maze where the
solver takes a bizarrely long path, or gets stuck in a loop, or fails
entirely. When that happens — and it will — ask Claude:

> The solver failed on this maze (or took a ridiculously long path). Why
> does the left-hand wall rule sometimes fail? What's different about the
> mazes where it doesn't work?

This is one of the most important conversations in this book. Claude will
explain that the left-hand rule only works on **simply-connected** mazes —
mazes where every wall is connected to the outer boundary. If a maze has
**islands** (loops of wall not connected to anything), the solver can walk
in circles forever.

Then ask:

> What algorithm would solve every maze, even ones with loops?

Claude will tell you about **BFS** (breadth-first search) or **A***. Ask
it to implement one:

> Replace the left-hand wall solver with BFS. Compare: does it always find
> the shortest path? Is it faster or slower?

You've just had your first real conversation about algorithms. Not from a
textbook — from a bug in your own code. That's how you learn.

## 3.4 Ask Claude What It Chose

Here's a pattern that will serve you for the rest of this book: **ask Claude
which algorithm it used, then ask about the alternatives.**

> What algorithm did you use to generate the maze? Why that one? What are
> the other options? How would the mazes look different with a different
> algorithm?

Claude might say it used Recursive Backtracking (deep, winding corridors),
or Kruskal's algorithm (more open, uniform feel), or Prim's algorithm
(organic, tree-like). Ask it to generate a maze with a different algorithm
so you can see the difference.

This is the collaborator model at work. You didn't need to know these
algorithms existed. Claude picked one, you asked why, and now you know about
three of them. Next time you build something that needs a maze, you can say
"use Kruskal's" and know what to expect.

## 3.5 How Many Mazes Exist?

Here's a question that might not have occurred to you: how many different
mazes can you make on a grid of a given size?

Ask Claude:

> Write a Python script called count_mazes.py that counts how many distinct
> mazes exist on a 4×4 grid. Generate all of them and tell me the total.

Claude will build it and give you a number. It runs quickly. Now push it:

> How about 5×5?

Still fast. Try 6×6. Getting slower. Try 7×7 — depending on your computer,
this might take a few seconds. Try 8×8 — it might take minutes.

You've just hit a wall. Python is doing the right thing, but it's doing it
slowly. The number of possible mazes grows explosively with grid size, and
Python has to check every single one.

Now try something:

> Rewrite count_mazes.py in C. Call it count_mazes.c. Same algorithm,
> different language.

Claude will write a C version. To run it, you need to **compile** it first:

```bash
gcc count_mazes.c -o count_mazes
./count_mazes
```

That first command (`gcc`) translates your C code into machine code — raw
instructions that your CPU understands directly. The second command runs it.

Try the same grid size that was slow in Python. Notice the difference.

**Why is C so much faster?** Python is an **interpreted** language — when you
run a Python script, the interpreter reads each line and figures out what to
do, one step at a time. C is a **compiled** language — the compiler
translates the entire program into machine code *before* it runs. The CPU
executes machine code directly, without an interpreter in the middle.

For most things — building a website, processing a file, writing a game —
the difference doesn't matter. Python is fast enough. But for counting
millions of mazes? C is 10x to 100x faster. The algorithm is the same. The
speed comes from how the language runs.

> **Tip:** You don't need to learn C. You don't even need to understand the
> code Claude wrote. You just need to know that when Python is too slow for
> a counting or computation problem, "rewrite it in C" is a real option —
> and Claude will do the rewriting for you.

Here's a deeper question worth asking Claude:

> Two mazes can look completely different on the grid but have the same
> underlying structure — the same branching pattern, the same number of
> dead ends, the same shape. How many *structurally distinct* mazes exist
> on a 4×4 grid?

Every maze is a tree — a connected path with no loops. Two mazes that use
different cells on the grid might actually be the same tree drawn in
different places. The number of structurally distinct mazes is much smaller
than the total count, and figuring out which mazes are "the same" is itself
a hard problem. Ask Claude to explain why.

You've now touched three languages — Python, C, and JavaScript. This is a
good moment to ask Claude a big question:

> What is the difference between a compiled language and an interpreted
> language? Give me examples of each.

You just saw the answer in action — but hearing Claude explain it in terms of
the code you've already written makes the concept stick.

## 3.6 ASCII Art

Let's build something completely different. Open a new terminal tab:

```bash
cd ~/claude-projects
mkdir ascii-art
cd ascii-art
claude
```

> Write a Python script called ascii_art.py that takes an image file as
> input and converts it to ASCII art in the terminal. It should resize the
> image to fit the terminal width, convert each pixel to a character based
> on brightness (use a character ramp from dark to light, something like
> " .:-=+*#%@"), and print the result.
>
> Usage: python3 ascii_art.py photo.jpg
>
> It will need the Pillow library for image processing.

Claude will write the script — and it will tell you to install **Pillow**:

```bash
pip3 install Pillow
```

This is your first **package install**. Pillow is a library — code that
someone else wrote and published so you don't have to write it yourself.
Python has thousands of these. `pip` is the tool that downloads and installs
them.

Now find a photo on your computer and try it:

```bash
python3 ascii_art.py ~/Pictures/some-photo.jpg
```

Your photo, rendered in text characters in the terminal. Resize your terminal
window and run it again — the output adapts to the width.

Try a few more images. Faces work well. Landscapes work well. High-contrast
images work best. If the output looks wrong, tell Claude:

> The image is too dark — I can barely make out the details. Can you adjust
> the brightness mapping? Also, can you add a --width flag so I can control
> the output width?

Iterate. You know the loop by now.

## 3.7 Colour Reduction

One more image project. Same directory, same Claude session — Pillow is
already installed.

> Write a Python script called posterize.py that takes a photo and reduces
> it to a small number of colours — say 8. The output should look blocky
> and stylized, like a poster or pop art. Save the result as a new image
> file.
>
> Usage: python3 posterize.py photo.jpg 8
>
> The second argument is the number of colours. Let me try different numbers.

Run it:

```bash
python3 posterize.py ~/Pictures/some-photo.jpg 8
```

Claude will tell you where it saved the output file. To see it:

```bash
open output.png        # Mac
xdg-open output.png    # Linux
```

Your photo, reduced to 8 colours. Try it with 4 colours. Try 2. Try 16. The
sweet spot depends on the image — portraits often look great at 6-8 colours,
landscapes at 10-12.

Now ask the question:

> What algorithm did you use to choose which 8 colours? Why those particular
> colours and not others?

Claude will probably say it used **k-means clustering** or **median cut** —
algorithms that look at every pixel in the image and find the 8 colours that
best represent them. These aren't the 8 "brightest" or "most common" colours
— they're the 8 colours that minimise the total error across the whole image.

That's a real algorithm, used in real image processing, and you just used it
by saying "reduce it to 8 colours." Ask Claude about the alternatives. Ask
what happens if you use different algorithms on the same image.

## 3.8 Installing Packages

When Claude told you to run `pip3 install Pillow`, something important
happened: you installed code from the internet into your Python environment.
This is normal and safe — Pillow is one of the most widely used Python
libraries in the world.

But it's worth knowing what just happened:

- **pip** is Python's package manager — it downloads libraries from a
  central repository called PyPI (Python Package Index)
- **Pillow** is the library name — it gives Python the ability to open,
  manipulate, and save image files
- The library gets installed into your Python environment and stays there
  until you remove it
- Any Python script on your computer can now `import PIL` (Pillow's module
  name) and use it

You'll install more packages as you build more things. It's always the same
pattern: Claude writes code that needs a library, Claude tells you to
install it, you run `pip3 install [name]`.

If you want to see what you have installed:

```bash
pip3 list
```

Ask Claude to explain anything unfamiliar in that list.

## 3.9 Look at the Code

Open `maze.py` in a text editor and look at it. Then open `ascii_art.py`.

Python is much more readable than HTML. Where HTML had angle brackets and
nested tags, Python reads almost like English:

```python
if guess in word:
    reveal_letter(guess)
else:
    wrong_guesses.append(guess)
```

You can *almost* read what this does without knowing Python. That's by
design — Python was created to be readable.

Ask Claude:

> Walk me through maze.py and explain the maze generation algorithm in
> plain English. I'm not trying to learn Python — I just want to understand
> the logic.

Claude will explain it in terms of the algorithm, not the syntax. "It starts
at a random cell, picks a random unvisited neighbour, knocks down the wall
between them, and repeats. When it gets stuck, it backtracks to the last
cell that had unvisited neighbours."

That's a program described in one sentence. The code is just the detailed
version of that sentence.

## 3.10 Push to GitHub

Both projects should go on GitHub. For each one:

> Push this project to GitHub as a new repository. Write a README that
> explains what it does and how to run it — including the pip install
> command for any dependencies.

The README matters more for Python projects than for your HTML games. Someone
visiting your repo needs to know they have to install Pillow before the
script will work. Claude will include that in the README automatically.

## 3.11 Imagineering

You've built programs that run in the terminal instead of the browser. The
same rules apply: new terminal tab, new directory, new Claude session. Push
to GitHub when you're done.

There's no point reading this book if you don't do the exercises. The
prompts are your practice. The iteration is the learning. Do them.

Here are ideas — but your own are better:

- **Sudoku** — generate a valid puzzle, display it with box-drawing
  characters, then solve it step by step with animated backtracking in the
  terminal. Once it works, try what we did with mazes: remove some extra
  numbers from a puzzle and ask Claude to count how many valid solutions
  remain. Then rewrite the counter in C and compare the speed
- **Game of Life** — Conway's cellular automaton, animated in the terminal.
  Load starting patterns from text files
- **Text adventure** — a multi-room game with inventory, puzzles, and
  atmosphere. Save and load game state
- **Typing speed test** — display a sentence, time how fast you type it,
  report your words per minute
- **Habit tracker** — a command-line tool that tracks daily habits, shows
  streaks, stores data in a JSON file

For each one, don't tell Claude which algorithm or approach to use. Let it
choose. Then ask why. Then ask about alternatives. This is how you build
intuition about what's possible without memorising anything.

Practice makes perfect.

---

## What You've Learned

In this chapter you:

- Shifted from browser-based websites to terminal-based Python scripts
- Built a maze generator and explored different generation algorithms — by
  asking Claude, not by studying
- Learned that algorithms fail in interesting ways (the left-hand rule on
  looping mazes) and that debugging a failure teaches more than getting it
  right the first time
- Counted mazes — and discovered that Python is too slow for some problems,
  while C is 10-100x faster for computation
- Converted images to ASCII art and reduced photos to a handful of colours
- Installed your first Python package
- Discovered that Python code is readable even without learning Python
- Adopted the "ask Claude what it chose, then ask about alternatives"
  pattern — the single most powerful question in this book

---

**Next up:** Chapter 4 — where we move beyond single files and build
something with a frontend, a backend, and an API.
