# Appendix: Elementary Principles of Programming

Now that we have Claude, do we still need to learn how to code? I asked
Claude, and he said yes — but not for the reasons you think. You don't need
to learn to *write* code. Claude does that. You need to learn to *read* it
— just enough to follow what Claude is doing, spot when something looks
wrong, and have a real conversation about it.

That's what this appendix teaches. Every example comes from the projects
you built in this book.

---

## Running Python

When Claude creates a Python file, you run it yourself in the terminal:

```bash
python3 maze.py
```

That's it. `python3` is the **interpreter** — it reads your script line by
line and executes it. The file is plain text. You can open it in any editor
and read it.

If the script takes arguments:

```bash
python3 ascii_art.py photo.jpg
python3 posterize.py photo.jpg 8
```

The words after the filename are **arguments** — inputs that the script uses.
In your posterize script, `photo.jpg` is the image and `8` is the number of
colours.

Python was historically considered easier to read and faster to work with
than other languages — though this matters less now that Claude writes the
code for you. What still matters is Python's ecosystem: it dominates data
science and machine learning, and has libraries for almost everything.

## Compiling and Running C

C is a much older and lower-level language. The Linux kernel and most of the
GNU toolchain — the foundational software that runs most of the world's
servers — are written in C. It's fast because it compiles directly to
machine code, but it gives you less help: you manage memory yourself, and
mistakes can crash your program without a helpful error message.

You can't run a `.c` file directly — you have to **compile** it first:

```bash
gcc maze_counter.c -o maze_counter
```

This translates your C code into a **binary** — a file of machine
instructions that your CPU understands directly. The `-o maze_counter` part
names the output file.

Then you run the binary:

```bash
./maze_counter
```

The `./` means "run this file in the current directory." The binary runs
much faster than Python because there's no interpreter in the middle — the
CPU executes the instructions directly.

Two commands instead of one. That's the price of speed.

## Compiled vs Interpreted

When you run a C program, the compiled binary talks directly to the kernel
— your operating system's core. There's nothing in between. That's why
it's fast.

When you run a Python script, something different happens. Python runs
inside a **virtual machine** — a program that pretends to be a computer.
Your Python code gets translated into instructions for this virtual machine,
and the virtual machine then talks to the kernel on your behalf. There's an
extra layer in between:

```
C program  →  kernel  →  hardware

Python script  →  Python virtual machine  →  kernel  →  hardware
```

That extra layer is why Python is slower for computation-heavy tasks like
counting mazes. But it's also why Python is safer and easier to work with
— the virtual machine handles memory, catches errors gracefully, and
protects you from crashing the whole system.

**Compiled languages** (C, Rust, Go) translate your code to machine
instructions *before* it runs. Fast, but you wait for compilation and get
less hand-holding.

**Interpreted languages** (Python, JavaScript, Ruby) translate your code
*as* it runs, through a virtual machine or interpreter. Slower, but more
forgiving and quicker to iterate with.

For most things you'll build with Claude, the difference doesn't matter.
When it does — you saw this with the maze counter — you can always ask
Claude to rewrite the slow part in C.

## Recognising Python vs C by Sight

You've used both Python and C in this book. You should be able to tell
which is which at a glance. Here's the same thing in both languages — print
every word longer than 5 letters:

**Python:**
```python
for word in words:
    if len(word) > 5:
        print(word)
```

**C:**
```c
for (int i = 0; i < count; i++) {
    if (strlen(words[i]) > 5) {
        printf("%s\n", words[i]);
    }
}
```

The quickest tells: Python has no semicolons and uses indentation to define
blocks. C has semicolons at the end of every statement, curly braces `{}`
around blocks, type declarations before variables (`int i`), and `#include`
at the top of every file. Python reads like English. C reads like
instructions for a machine — which is closer to what it actually is.

---

## Variables

A variable is a name for a value. In your hangman game, Claude needs to
keep track of how many wrong guesses the player has made:

```python
wrong_guesses = 0
```

That's a variable. The name is `wrong_guesses`, the value is `0`. Every
time the player guesses wrong, the code changes it:

```python
wrong_guesses = wrong_guesses + 1
```

Now it's `1`. Then `2`. And so on. When it reaches `9`, the game is over.

Your hangman game has several variables working together:

```python
guesses_remaining = 9
game_over = False
wrong_letters = []
```

Each one stores a different piece of the game's state — how many guesses
are left, whether the game has ended, and which wrong letters have been
tried.

## Types

Values come in different types. You don't need to declare them in Python —
it figures them out automatically.

**Strings** — text, always in quotes:
```python
filename = "photo.jpg"       # (ASCII art)
player_one = "Alice"         # (memory card game)
player_two = "Bob"           # (memory card game)
```

**Integers** — whole numbers:
```python
maze_width = 40              # (maze)
maze_height = 20             # (maze)
num_colours = 8              # (posterize)
```

**Floats** — decimal numbers:
```python
brightness = 0.75            # (ASCII art)
```

**Booleans** — true or false:
```python
can_move_forward = False     # (maze solver)
game_over = True             # (hangman)
```

**Lists** — ordered collections:
```python
letters = ["e", "l", "e", "p", "h", "a", "n", "t"]   # (hangman)
row = ["#", " ", " ", "#", " ", "#"]                    # (maze)
```

You access items by position (starting from 0):
```python
letters[0]    # "e"          (hangman — first letter)
letters[3]    # "p"          (hangman — fourth letter)
row[1]        # " "          (maze — a path, not a wall)
```

**Dictionaries** — key-value pairs:
```python
char_ramp = {                # (ASCII art)
    0: " ",
    1: ".",
    2: ":",
    3: "-",
    4: "=",
    5: "+",
    6: "*",
    7: "#",
    8: "%",
    9: "@"
}
```

A list uses a position number to look things up: `letters[3]` means "give
me the 4th item." A dictionary uses a key: `char_ramp[7]` means "give me
the character for brightness level 7" — which is `"#"`.

The difference: lists are ordered sequences (first, second, third...).
Dictionaries are lookups (this key maps to this value). Dictionaries are
everywhere in Python — any time you see curly braces with colons, you're
looking at one.

## Conditionals

Do different things depending on a condition. This is from your hangman
game — the core logic that runs every time the player guesses a letter:

```python
if letter in word:
    reveal_letter(letter)
elif letter in wrong_guesses:
    print("Already guessed!")
else:
    wrong_guesses.append(letter)
    guesses_remaining -= 1
```

`if` checks the condition. `elif` (else-if) checks another condition if the
first was false. `else` runs if nothing above was true.

In the maze solver, a conditional checks whether a cell is passable:

```python
if grid[row][col] == " " and (row, col) not in visited:
    queue.append((row, col))
```

Notice the **indentation** — in Python, indentation isn't decorative. It
defines which lines belong to which block. Everything indented under `if`
runs only when the condition is true.

## Loops

Do something many times. This is from your ASCII art converter — it goes
through every pixel in the image, looks up how bright it is, and replaces
it with a text character that approximates that level of grey:

```python
for y in range(height):                    # (ASCII art)
    for x in range(width):
        brightness = pixels[x, y]          # how bright is this pixel?
        char = char_ramp[brightness]        # find the matching character
        print(char, end="")                 # print it (no newline yet)
    print()                                 # newline at end of each row
```

A dark pixel becomes a space. A medium pixel becomes `=` or `*`. A bright
pixel becomes `@`. Do that for every pixel and you get a photo made of text.

The outer loop goes through each row. The inner loop goes through each
pixel in that row. `for X in Y` means "for each item X in the collection
Y, do this."

There's also `while`, which keeps going as long as a condition is true.
This is the main game loop from hangman — it keeps asking for guesses
until the player wins or runs out of tries:

```python
while guesses_remaining > 0 and not word_complete:   # (hangman)
    letter = input("Guess a letter: ")
    if letter in word:
        # correct — reveal this letter in the word
        revealed[word.index(letter)] = letter
    else:
        # wrong — lose a guess, add to wrong list
        guesses_remaining -= 1
        wrong_letters.append(letter)
```

## Functions

A function is a named chunk of instructions that you can reuse. In your
maze program, the solver is a function — you give it a maze, a starting
position, and an exit position, and it gives you back the path:

```python
def solve(grid, start, end):                         # (maze)
    queue = [start]          # cells to visit next
    visited = set()          # cells already checked
    came_from = {}           # how we got to each cell
    while queue:
        current = queue.pop(0)
        if current == end:
            return build_path(came_from, end)         # found it!
        visited.add(current)
        for neighbour in get_neighbours(grid, current):
            if neighbour not in visited:
                queue.append(neighbour)
                came_from[neighbour] = current
    return None                                       # no path exists
```

`def` defines the function. The name is `solve`. The words in parentheses
(`grid`, `start`, `end`) are **parameters** — values you pass in when you
call it. `return` sends a value back — either the path it found, or `None`
if the maze has no solution.

You call it like this:

```python
path = solve(grid, start, end)
```

That one line runs the entire solver. The function contains 12 lines of
logic, but from the outside it's just: give it a maze, get back a path.
That's the point of functions — they hide complexity behind a simple
interface.

## Recursion

A function can call itself. This is called **recursion**. It sounds strange
but it's how both your maze generator and your Sudoku solver work.

Here's the Sudoku solver — the logic is surprisingly short:

```python
def solve(board):                                     # (Sudoku)
    empty = find_empty_cell(board)
    if empty is None:
        return True                  # no empty cells — puzzle solved!
    row, col = empty
    for number in range(1, 10):      # try 1, 2, 3, ... 9
        if is_valid(board, row, col, number):
            board[row][col] = number # place the number
            if solve(board):         # try to solve the rest
                return True
            board[row][col] = 0      # didn't work — erase it
    return False                     # none of 1-9 worked — backtrack
```

Read it line by line: find an empty cell. Try putting 1 in it. Is that
valid (not already in the same row, column, or 3×3 box)? If so, place it
and call `solve` again — on the same board, which now has one more number
filled in. If that eventually leads to a solution, great. If not, erase the
number and try 2. Then 3. And so on up to 9. If none of them work, return
`False` — which tells the *previous* call to erase *its* guess and try the
next number.

That's **recursive backtracking**: try something, go deeper, and if you hit
a dead end, undo and try the next option. Your maze generator uses the same
pattern — pick a direction, carve a path, go deeper; if you hit a dead end,
backtrack and try another direction.

A short function that calls itself can explore an enormous number of
possibilities. That's why this pattern shows up everywhere — mazes, Sudoku,
chess engines, route planning.

## Libraries and Imports

A **library** is code that someone else has already written and shared so
you don't have to build everything from scratch. Writing code to open a JPEG
file, decode its pixels, and resize it would take hundreds of lines. Or you
can use the Pillow library — someone already solved that problem, tested it,
and published it for anyone to use. That's what libraries are for: avoiding
reinventing the wheel.

You use a library by **importing** it. In your ASCII art and posterize
scripts, the first line is:

```python
from PIL import Image                                 # (ASCII art)
```

This pulls the `Image` tool from the Pillow library so your script can open
and process photos. In the maze generator:

```python
import random                                         # (maze)
```

This loads Python's built-in random number tools — used to shuffle which
direction the generator carves next, and to pick the secret word in hangman.

When you see `import` at the top of a file, it's loading tools. Some are
built into Python (`random`, `sys`, `os`, `json`). Others are external
libraries that you or Claude installed.

## Reading Errors

When a Python script crashes, it prints a **traceback**. It looks alarming
but it's actually helpful. You might see this when running your maze solver:

```
Traceback (most recent call last):
  File "maze.py", line 47, in solve
    if grid[row][col] == " ":
IndexError: list index out of range
```

Read it from the bottom up:

1. **The error**: `IndexError: list index out of range` — the solver tried
   to check a cell outside the grid
2. **The line**: `line 47` in `maze.py` — exactly where it went wrong
3. **The code**: `if grid[row][col] == " "` — the line that caused it

When you paste this back to Claude, it knows exactly where to look. The
traceback is a map to the problem.

Common errors you'll see:

| Error | What it means |
|-------|--------------|
| `SyntaxError` | Python can't understand the code (typo, missing colon) |
| `NameError` | You used a variable that doesn't exist |
| `TypeError` | You used the wrong type (like adding a string to a number) |
| `IndexError` | You accessed a list position that doesn't exist (e.g. the solver went off the grid) |
| `KeyError` | You accessed a dictionary key that doesn't exist |
| `FileNotFoundError` | The file you asked for isn't there (wrong path to your photo?) |
| `ModuleNotFoundError` | You need to `pip install` something (probably Pillow) |

You don't need to fix these yourself. Copy the entire traceback, paste it
to Claude, and say "this crashed." Claude will fix it. But knowing how to
read the last line tells you whether it's a typo, a missing file, or a
missing library — which helps you have a faster conversation.

---

That's it. Variables, types, conditionals, loops, functions, recursion,
imports, and errors. With these eight concepts you can read any Python file
Claude writes and follow what it's doing. You don't need to write Python.
You need to *read* it — and now you can.
