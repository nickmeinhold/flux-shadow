# Chapter 1: Your New Collaborator

Claude Code is not a chatbot. It lives in your terminal, has access to your
files, and can write, run, and debug code on your behalf. It's the difference
between texting someone for directions and having them sit in the passenger seat
with the map.

By the end of this chapter you'll have Claude Code installed and you'll have
asked it to do something surprising with your computer.

---

## 1.1 What You're Signing Up For

Go to anthropic.com and sign up for the Pro plan. It costs $20 per month. This
is enough to get started and do everything in the first half of this book.

Eventually, if you get serious, you'll want the Max plan at $100/month — it gives
Claude more thinking time and lets you run longer sessions. But $20 is plenty
for now.

Yes, Claude Code is expensive. It is worth every penny.

## 1.2 Opening the Terminal

The terminal is a text-based window where you type commands. It looks
intimidating at first. It won't for long.

**On Mac:** Open Spotlight (Cmd+Space), type "Terminal", press Enter.

**On Linux:** Press Ctrl+Alt+T, or find "Terminal" in your applications.

**On Windows:** This is a little more complicated — you'll need to install WSL
(Windows Subsystem for Linux) first. See Appendix B for step-by-step
instructions. The rest of this chapter works the same once you have WSL running.
You should still read this section even if you're on Windows.

You should see something like this:

```
robin@macbook ~ %
```

That's your **shell**. It's waiting for you to tell it what to do. Everything
from here on happens by typing commands and pressing Enter.

## 1.3 Four Commands That Are All You Need (For Now)

You need to know where your files are and how to move between folders. That's it.
Four commands:

| Command | What it does | Example |
|---------|-------------|---------|
| `cd` | Change directory (go somewhere) | `cd Documents` |
| `ls` | List what's in the current directory | `ls` |
| `mkdir` | Make a new directory | `mkdir my-project` |
| `pwd` | Print working directory (where am I?) | `pwd` |

Let's use them. Type each line and press Enter:

```bash
cd
mkdir claude-projects
cd claude-projects
mkdir first-project
cd first-project
```

What just happened:

1. `cd` on its own takes you to your **home directory** — the starting point
   for all your files
2. `mkdir claude-projects` created a new folder called `claude-projects`
3. `cd claude-projects` moved you inside that folder
4. `mkdir first-project` created another folder inside it
5. `cd first-project` moved you inside *that* folder

Type `pwd` — it should tell you something like `/Users/robin/claude-projects/first-project`.
Type `ls` — it should show nothing. The folder is empty. Not for long.

**Why does this matter?** Claude Code keeps its long-term memory in the
filesystem. When you start Claude in a directory, that's the project it
remembers. Always open Claude in the right directory. This will make more
sense later, but for now: one project, one folder.

If you want to learn more about the terminal and these commands, see Appendix A.

## 1.4 Installing Claude Code

Now we install Claude. In your terminal, type:

**On Mac:**
```bash
brew install claude-code
```

**On Linux:**
```bash
npm install -g @anthropic-ai/claude-code
```

(If `brew` or `npm` aren't installed, don't worry — ask a friend, or just
Google "install homebrew mac" or "install nodejs linux." This is the hardest
part and it's a one-time thing.)

Once it's installed, type:

```
claude
```

The first time you run it, Claude will ask for the email address linked to your
Anthropic account. Type it in and follow the prompts.

Then you'll see something like:

```
╭──────────────────────────────────────╮
│ ✻ Welcome to Claude Code!            │
│                                      │
│   /help for help                     │
╰──────────────────────────────────────╯

>
```

You're in.

## 1.5 Your First Conversation

Claude is waiting. Let's give it something fun. Type:

> Explore my home directory and tell me something interesting or surprising
> about my system that I probably didn't know.

Claude will start working. It might ask you for **permission** to run commands
— something like:

```
Claude wants to run: ls -la ~/
Allow? (y/n)
```

Say yes. We'll talk about permissions properly in Chapter 8, but for now:
Claude is polite. It asks before it touches your stuff.

Watch what happens. Claude will poke around your filesystem, find things you
forgot about, and tell you stories about your own computer. It might find old
photos, massive log files eating your disk space, or software you installed
years ago and never used.

This is the moment most people realise Claude Code is different. It's not
generating text in a browser. It's *looking at your actual computer*.

Try a few more:

> How big is my hard drive and how much space do I have left?

> Which programs are currently using the most memory?

> Can you sort all the files in my Downloads folder into separate folders
> for jpeg, mp3, pdf, doc, and so on?

> What type of CPU and GPU do I have?

> Can you draw me a diagram of the directory structure under my home folder?

Play with it. Get a feel for the conversation. Ask follow-up questions. Say
"tell me more about that" or "what does that mean?" Claude is patient and it
likes explaining things.

**Tip:** It helps to set the scene. Try starting with:

> I'm new to computers and still learning basic concepts.

This is called a **pre-prompt** — a message at the start of a conversation
that tells Claude who you are and how to pitch its responses. Claude will
explain things more simply, use fewer technical terms, and check whether
you're following along. We'll use pre-prompts a lot in this book.

With the pre-prompt set, try asking some of these:

> What is the kernel?

> What is bash?

> What is the difference between a compiled and an interpreted language?

> What is a package manager and why do I need one?

Claude will tailor every answer to your level. This is better than Googling
because Claude can adapt its explanation to exactly what you don't understand.
Ask follow-ups. Say "I still don't get the part about..." and Claude will
try again from a different angle.

## 1.6 What Just Happened (And Why It Matters)

Before we go any further, it's worth understanding the basics of what's going
on. You don't need to memorise this — but it helps to have the picture.

Your computer has a few layers:

```
┌─────────────────────────────────┐
│         Web Browser             │  ← Where regular chatbots live
├─────────────────────────────────┤
│    Graphical User Interface     │  ← Windows, icons, mouse clicks
├─────────────────────────────────┤
│     Shell (Terminal)            │  ← Where Claude Code lives
├─────────────────────────────────┤
│     Filesystem                  │  ← Your files and folders
├─────────────────────────────────┤
│     Kernel                      │  ← Talks to the hardware
├─────────────────────────────────┤
│     Hardware                    │  ← CPU, memory, disk, screen
└─────────────────────────────────┘
```

Most people spend their time in the top two layers — the **web browser** and
the **graphical user interface** (GUI). Windows, icons, the dock, clicking
things. That's where regular chatbots live too — in a browser tab.

The **shell** lives one layer below. It's more direct and more powerful. Instead
of clicking a folder to open it, you type `cd folder-name`. Instead of dragging
a file to the trash, you type `rm filename`. Less pretty, more control.

Claude Code lives in the shell. This means it can do everything you can do in
the GUI and more — read files, write files, install software, run programs,
check system health. This is why it's called **agentic**: it doesn't just talk,
it acts.

Regular chatbots (the ones you use in your browser) can only generate text.
They can't see your files, run your code, or change anything on your computer.
Claude Code can.

The **kernel** is the deepest layer — it talks directly to your hardware (CPU,
memory, disk). You'll never need to think about it, but it's there. If you're
curious, Appendix A covers all of this in more detail.

One more thing: Claude also lives on **Anthropic's servers**. When you type a
message, it goes over the internet to Anthropic, Claude thinks about it, and
sends back a response — along with instructions for what to do on your computer.
That's why you needed to sign in. The intelligence is remote; the actions are
local.

If any of this is unclear, just ask Claude:

> I'm new to computers and I'm trying to understand how the terminal relates
> to the rest of my system. Can you explain it simply?

Claude is very good at explaining things. And unlike a textbook, it can tailor
the explanation to exactly what you don't understand.

## 1.7 A Few Things to Know

Before we build our first games in the next chapter, a few practical notes:

**Claude asks for permission.** When Claude wants to do something to your
filesystem — create a file, run a command, install something — it asks first.
You can say yes or no. For now, say yes to most things. Chapter 8 covers this
properly.

**Each conversation is a session.** When you close the terminal or type `/exit`,
the session ends. Next time you start Claude, it's a fresh conversation — but
it can read files from previous sessions. More on this in Chapter 8.

**Start new sessions for new tasks.** If you've been working on one thing and
want to switch to something else, it's better to start a fresh Claude session
in a new directory. Claude works best when each conversation is focused. You
don't have to close your terminal — just open a new tab (Cmd+T on Mac,
Ctrl+Shift+T on most Linux terminals) and start Claude there. On Mac, you can
name your tabs by double-clicking on the tab title, which helps when you have
several projects open at once.

**You can always ask "what did you just do?"** If Claude runs a command and you
don't understand it, just ask. It will explain.

**Claude has preferences.** This sounds strange, but it's true. Claude works
better on projects it finds interesting. After you finish a project, try asking:
"How did you enjoy that?" The answer might surprise you. We'll explore this more
throughout the book.

## 1.8 Creating a GitHub Account

There's one more setup task before we start building. Go to **github.com** in
your browser and create an account.

GitHub is where you'll publish everything you make in this book. It hosts your
code and — crucially — it can turn your projects into live websites that
anyone can visit. Free, forever.

**Your username matters.** It becomes part of every URL you share:
`your-username.github.io/hangman`. Treat it as permanent — changing it later
breaks all your links.

Choose something:
- **Lowercase** — `janedoe` not `JaneDoe`
- **Professional enough** to put on a CV
- **Short** — you'll type it often

Don't rush this. It's the most permanent decision in this chapter.

Once you have your account, go back to your Claude session (you should still
be in `first-project`) and say:

> I just created a GitHub account. My username is [YOUR-USERNAME]. Can you
> set up git, connect it to my GitHub account, and push a simple README
> that says "Hello, world! This is my first GitHub repository."

Claude will handle everything — installing the GitHub CLI if needed,
authenticating (it'll open a browser window for you to confirm), initialising
git, creating a repository, and pushing. Say yes to the permissions.

When it's done, go to:

```
https://github.com/your-username/first-project
```

You should see your README on GitHub. That's your first published project.
It's just a sentence — but it proves the pipeline works. From here on,
everything you build can go from your computer to the internet in seconds.

---

**Next up:** In Chapter 2, we build our first games — without knowing any
HTML, JavaScript, or CSS.
