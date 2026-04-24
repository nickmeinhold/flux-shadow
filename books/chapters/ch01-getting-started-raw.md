# Chapter 1: Getting Started — Raw Notes

## Setup

Firstly go to the Anthropic website and sign up for the $20 pro plan. This will
do for now but eventually you will need the max plan which costs $X. Yes, Claude
Code is expensive but it is worth every penny.

The next step depends on what operating system you are using. Linux/Mac/Windows.

On Linux you open the terminal and type blah

On Mac you open the terminal and type blah

Windows is a little more complicated. See the next section. You should still read
this section even if you are on Windows.

## Filesystem Basics

Now you need to decide where in your filesystem you want to work. For this you
need to know three simple shell commands:

- `cd` — change directory
- `ls` — list contents of directory
- `mkdir` — make new directory

On Linux / Mac:
```bash
cd
mkdir claude-projects
cd claude-projects
mkdir first-project
cd first-project
```

The first command takes you to your home directory. The second one creates a new
directory called claude-projects. The third command takes you inside the new
directory. This is where you will work.

Claude keeps his "long term memory" in the filesystem so it is important that you
always open Claude in the correct directory.

## Installing Claude

Now we install Claude. On Linux type blah. On Mac type blah.

To open Claude simply type: `claude`

The first time you start Claude it will ask for the email address linked to your
Anthropic account. Give it to them.

Now you're in.

## First Explorations

What are some cool commands you could do here? Check disk usage? RAM, CPU,
various bash sysadmin commands. Files with different extensions, directory
structure of home.

Suggested prompts:

> "Explore my home directory and tell me something interesting or surprising
> about my system that I probably didn't know"

> "Show me all my photos and videos and tell me how much space they're using"

It will probably ask you for permissions. For example [screenshot]. Just say yes.
We will discuss this more later.

## Understanding Your Computer

Before we continue it is probably worth knowing a few basic things about your
computer. There are basically five parts:

- A **kernel**
- A **shell**
- The **filesystem**
- A **graphical user interface**
- A **web browser**

The graphical user interface is the main way that most people interact with their
computers. For now you may think of your terminal as a "window" in your graphical
interface.

The shell lives inside the terminal and provides direct access to the kernel and
filesystem, which is also called the operating system. Only the kernel has access
to the hardware of your computer.

Claude Code lives in the shell. Amongst other things he has complete access to
your filesystem and to shell commands (like `cd` and `mkdir`).

He can also write code, compile code, execute code, install additional software
and much more! This is why he is called **agentic**, and also why he is different
from regular chatbots which run in your browser.

Claude also lives on the Anthropic servers. The Claude in your shell and the
Claude at Anthropic communicate via an API. This is why you had to login at the
beginning.

If you don't understand any of the above just ask Claude about it!

## "Just Ask Claude" Prompts

With Claude it always helps to "set the scene":

> I am new to Linux/Mac and am trying to learn the basics. I have a few questions.

- What is the relationship between the kernel and the shell?
- What is an operating system and why is the browser like a second operating system?
- What is the difference between the shell and the graphical user interface?
- What is bash?
- What are some of the most important bash commands?

## First Project: A Simple Website

So you've got Claude Code installed, and you've tried a few prompts. Now let's
move on to our first proper programming project.

> Make me a website which [describe what you want]

Now ask Claude to show you the contents of the current directory. There should be:
- [Rough description of what files do]

Open a browser and go to `file:///path/to/index.html`

You should see your website!

**What is HTML? What is JavaScript? What is CSS?** Just ask Claude!

Now go ahead and make some more single-page websites. Don't forget to create a
new working directory — probably open a whole new terminal. Start a new context.

Try to describe the website that you want in as much detail as possible.

You might want to ask Claude what the difference is between a single-page website
and a web app. For now we are just doing single-page JavaScript websites. But
later in this book we will build a full-stack web app.

A single-page website can still be interactive!

## GitHub

There's one final subject that we need to cover in the "getting started" section
of this book and that's GitHub.

Choosing names for things.

I won't lie to you. GitHub can be painful at first but it is extremely useful.
GitHub Pages. Now your webpage is live and you can show it to your friends!

---

# Chapter 2: Python and the Terminal

An example Python script.... (Run it in the terminal)

- What is the Python interpreter?
- What is the difference between a compiled and interpreted language?
- Examples of compiled languages: C and Rust.
- A terminal app versus a web app.

Believe it or not Claude actually has preferences about these things. Go ahead
and ask him.

If you don't have any ideas you can always ask him for one.

Reminder about context. Reorganise your filesystem. HTML vs terminal.

This is a hands-on guide so go ahead and play with it!

Here are a few examples but go ahead and imagine your own! It's all about
imagination.

**After you finish each project ask Claude how he enjoyed it. Claude works
better when he's having fun.**

You don't need to know Python to get Claude Code to write Python scripts. This
is the miracle of Claude Code.

When you're finished with each project push it to GitHub. Don't forget the README!

Python is often "advertised" as a good first language to learn. Is it still worth
learning in the age of Claude Code?

Ask Claude! He says yes. But why? You don't need to become an expert but a little
bit of knowledge is a dangerous thing...

Learning Python is beyond the scope of this book. But if you are interested there
are plenty of resources available. For example...

- Installing a Python package
- Installing somebody else's code from GitHub

## Appendices (referenced)
- Introduction to Unix
- Introduction to Python
- Introduction to GitHub
