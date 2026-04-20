# Example Prompts

Actual prompts the reader can paste into Claude Code. Each should produce a
complete, working project in a single shot.

Pick the ones that interest you. Skip the ones that don't. Claude works better
when you're having fun — and so do you.

---

## 1.1 — Personal Link Tree (Single-Page Website)

```
Make me a single-page personal website in one HTML file. My name is [YOUR NAME].
I want a clean, modern design with a profile photo placeholder (use a grey
circle with my initials), a short bio section, and a vertical list of links
to my social media. Use these links:

- GitHub: [your URL]
- LinkedIn: [your URL]
- Twitter: [your URL]
- Email: [your email]

Each link should be a rounded button with an icon or emoji. The colour scheme
should be dark background with light text. Make it look good on both mobile
and desktop. Add a subtle animation when the page loads — the buttons should
fade in one by one.
```

---

## 1.2 — Quiz (Single-Page Website)

```
Make me a single-page quiz game in one HTML file. The topic is "How well do
you know the solar system?" Include 10 multiple-choice questions with 4
options each. Make sure the questions range from easy ("Which planet is
closest to the Sun?") to hard ("What is the Great Red Spot?").

The design should be fun and colourful — space-themed with a dark background
and glowing text. Show one question at a time with a progress bar at the top.
When the user picks an answer, highlight it green if correct or red if wrong
and briefly show the right answer before moving on. At the end, show the
score with a message: 10/10 = "You're an astronaut!", 7-9 = "Mission
specialist!", 4-6 = "Cadet", 0-3 = "Ground control, we have a problem."

Add a "Play Again" button that shuffles the question order.
```

---

## 2.1 — Password Generator (Python Console App)

```
Write me a Python script called password_gen.py that generates strong
passwords. When I run it, it should ask me:

1. How long do you want the password? (default 16)
2. Include symbols? (y/n, default y)
3. Include numbers? (y/n, default y)
4. How many passwords to generate? (default 3)

Then print the passwords to the terminal, nicely formatted. Also rate each
password's strength (weak/medium/strong/very strong) based on length and
character variety.

Add a option to copy one of them to the clipboard. Keep it simple — one file,
no external packages beyond what comes with Python.
```

---

## 2.2 — Text-Based RPG (Python Console App)

*This one is deliberately too complex to one-shot perfectly. That's the point.
You'll learn how to debug through conversation.*

```
Write me a text-based RPG in Python called dungeon.py. The setting is a
procedurally generated dungeon — each playthrough is different.

The game should have:
- A 5x5 grid of rooms, randomly generated each game. Each room is one of:
  empty, monster, treasure, trap, shop, or the exit
- A player with HP (starts at 100), attack power, defence, gold, and an
  inventory that holds up to 5 items
- Combat: turn-based, the player can attack, use an item, or try to flee.
  Monsters have names, HP, and attack power. At least 5 monster types
  ranging from easy (rat) to hard (dragon)
- Items: health potions, strength potions, a shield, a magic sword, a
  skeleton key. Each does something different
- A shop room where you can buy items with gold
- Traps that deal damage but can be disarmed if you have high enough
  attack power
- A map command that shows which rooms you've visited (fog of war for
  the rest)
- The goal: find the exit and escape alive. Track the player's score
  based on monsters killed, gold collected, and rooms explored
- Permadeath: when you die, it's over. Show final stats.
- Save and load game to a JSON file

One file, no external packages. Make the text output atmospheric —
descriptions should feel like a real dungeon crawl.
```

---

# More Ideas: Single-Page Websites

The reader should pick 2-3 that appeal to them. Every one of these can be
built with a single prompt.

## 1.3 — Countdown Timer

```
Make me a single-page countdown timer in one HTML file. It counts down to
[DATE] with the label "[EVENT NAME]". Show days, hours, minutes, and seconds
all ticking in real time. Big bold numbers. When it reaches zero, show
confetti animation and a celebration message. Dark background, the numbers
should glow slightly. Make it look good on a phone — I want to keep it open
on my desk.
```

## 1.4 — Recipe Card Collection

```
Make me a single-page recipe website in one HTML file. Include 6 recipes
for simple pasta dishes. Each recipe should be a card with the dish name,
a cooking time, difficulty rating (1-3 stars), ingredients list, and
step-by-step instructions. The cards should be in a grid that's 3 columns
on desktop, 1 column on mobile. Add a search bar at the top that filters
recipes as you type. Warm colour scheme — creams, terracotta, olive green.
Make it feel like a handwritten cookbook.
```

## 1.5 — Flashcards

```
Make me a single-page flashcard app in one HTML file. The topic is basic
Spanish vocabulary — include 20 common words with their English translations.
Show one card at a time. Click the card to flip it and reveal the answer.
Buttons for "Got it" and "Didn't know" — the ones you didn't know come back
more often. Show progress: "12/20 learned." Clean, minimal design. Make the
card flip with a smooth 3D animation.
```

## 1.6 — Pomodoro Timer

```
Make me a single-page Pomodoro timer in one HTML file. 25 minutes of work,
5 minutes of break, every 4th break is 15 minutes. Big circular progress
ring that fills up as time passes. Show which session you're on (e.g.
"Work 3/4"). Play a gentle sound when the timer finishes (use the Web
Audio API to generate a tone — no external files). Buttons: Start, Pause,
Skip. Track how many pomodoros you've completed today. Minimal design,
easy on the eyes — this will be open all day.
```

## 1.7 — Decision Maker

```
Make me a single-page "decision wheel" in one HTML file. I type in options
(like restaurant names or movie choices), and it shows them on a colourful
spinning wheel. When I click "Spin", the wheel spins with realistic
deceleration and lands on a random choice. Add a satisfying click sound
as it passes each option. Let me add and remove options. Make it fun —
bright colours, the wheel should feel physical.
```

## 1.8 — Personal Dashboard

```
Make me a single-page personal dashboard in one HTML file. It should show:
- Current time and date (big and prominent)
- Today's weather for [YOUR CITY] (use a free weather API, or just show
  a placeholder if the API needs a key)
- A "quote of the day" section (hardcode 30 good quotes and pick one
  based on the date)
- A simple to-do list that saves to localStorage so it persists between
  page refreshes
- A "focus mode" button that hides everything except the time and to-do list

Dark theme. Grid layout. Make it feel like a command centre.
```

---

# More Ideas: Python Console Apps

Pick 2-3 that sound useful to you. These all run in your terminal.

## 2.3 — Maze Generator and Solver (C — compiled vs interpreted)

*This teaches compiled vs interpreted languages. Same problem, two languages,
wildly different speed. Don't tell Claude which algorithm to use — let it choose.
Then ask it about the alternatives afterward.*

```
Write me a C program called maze.c that generates a random maze, prints it
to the terminal using █ for walls and spaces for paths, then solves it
using the "always follow the left wall" rule and shows the solution path
with dots. The maze should be about 40 wide and 20 tall. Tell me how long
generation and solving each took.
```

*After it works:*

```
Now write the same thing in Python as maze.py. Same output. I want to
compare the speed.
```

*Then explore:*

```
What algorithm did you use to generate the maze? What other options are
there? Can you show me a maze generated with a different algorithm so I
can see the difference?
```

*The left-hand rule will work on most mazes. Eventually the reader will hit
one where it fails or takes a silly path. That's when they ask why — and
learn about simply-connected mazes, loops, and better algorithms like BFS
and A*. Don't spoil this. Let it happen naturally.*

---

## 2.4 — Disk Space Analyser

```
Write me a Python script called diskcheck.py that shows me what's using
space on my computer. It should:

1. Scan my home directory
2. Show the top 20 biggest folders with their sizes in human-readable
   format (GB, MB)
3. Show a simple bar chart using just text characters: ████████░░ 4.2 GB
4. Warn me about any folders over 10 GB
5. Show total used vs available disk space

One file, no external packages. Make the output colourful using ANSI
escape codes.
```

## 2.4 — Batch File Renamer

```
Write me a Python script called rename.py that helps me rename lots of
files at once. It should:

1. Ask me for a folder path
2. Show me all the files in that folder
3. Ask me what pattern to apply. Options:
   - Add a prefix (e.g. "holiday_" → holiday_IMG001.jpg)
   - Add a date prefix (e.g. 2026-03-30_IMG001.jpg)
   - Sequential numbering (e.g. 001.jpg, 002.jpg, 003.jpg)
   - Replace text (e.g. replace "IMG" with "photo")
   - Lowercase everything
4. Show me a preview of the old name → new name for every file
5. Ask "Proceed? (y/n)" before doing anything

One file, no external packages.
```

## 2.5 — Expense Tracker

```
Write me a Python script called expenses.py that tracks my daily spending.
It should:

1. When I run it with no arguments: show a summary of this month's spending
   by category with totals
2. When I run it with: python expenses.py add 45.50 groceries "weekly shop"
   it adds an expense with amount, category, and description
3. Store everything in a simple CSV file called expenses.csv
4. Categories should be auto-detected from what I've used before
5. Show a simple monthly bar chart in the terminal using text characters

One file, no external packages beyond what comes with Python.
```

## 2.6 — Weather in Your Terminal

```
Write me a Python script called weather.py that shows the weather in my
terminal. Use the free wttr.in API (it needs no API key — just make a
request to wttr.in/[city]?format=j1).

When I run: python weather.py Melbourne

It should show:
- Current temperature and "feels like"
- Weather description (sunny, cloudy, raining)
- Wind speed and direction
- Humidity
- A 3-day forecast with highs and lows

Format it nicely with colours and maybe a simple ASCII art sun/cloud/rain.
One file, the only package needed is requests (tell me how to install it).
```

## 2.7 — Text Adventure Game

```
Write me a Python text adventure game called adventure.py. The setting is
a haunted mansion with 8 rooms. Each room has a description, items you
can pick up, and exits to other rooms. Include:

- An inventory system (pick up, drop, use items)
- A locked door that needs a key found elsewhere
- A simple puzzle (e.g. arrange items on a shelf in the right order)
- A win condition and a lose condition
- Atmospheric descriptions — make it creepy

The game state should be a dictionary so it's easy to understand.
Print a simple map when the player types "map". One file, no external
packages.
```

## 2.8 — Habit Tracker

```
Write me a Python script called habits.py that tracks daily habits.
It should:

1. Let me define habits: python habits.py add "exercise" "read" "meditate"
2. Let me check off today's habits: python habits.py done exercise
3. Show a weekly view with checkmarks:

            Mon  Tue  Wed  Thu  Fri  Sat  Sun
   exercise  ✓    ✓    ✗    ✓    ✓    ✗    -
   read      ✓    ✓    ✓    ✓    ✗    ✗    -
   meditate  ✗    ✓    ✓    ✓    ✓    ✗    -

4. Show streaks: "exercise: 2 day streak (best: 5)"
5. Store everything in a JSON file

One file, no external packages.
```

## 2.9 — Duplicate Photo Finder

```
Write me a Python script called dupes.py that finds duplicate photos on
my computer. It should:

1. Ask me for a folder to scan (default ~/Pictures)
2. Scan all image files recursively (jpg, png, heic, webp)
3. Find duplicates by comparing file hashes (not just names — the same
   photo might have different names)
4. Group the duplicates and show me:
   "Found 7 sets of duplicates using 2.3 GB of wasted space"
5. For each set, show the file paths and ask if I want to keep the
   first one and delete the rest, or skip

Be careful — ask before deleting anything. One file, no external packages.
```
