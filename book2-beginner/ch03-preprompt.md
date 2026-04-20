# Pre-prompt for Chapter 3 session

Paste this into the new Claude instance before giving it the game prompt.

---

```
I am writing an introductory book about Claude Code for people who don't
necessarily have a programming or computer science background. This is
Chapter 3, where the reader builds their first ambitious project — a
text-based adventure game in Python.

The purpose of this chapter is to teach debugging through conversation.
We EXPECT things to go wrong. When they do, I will paste errors back to
you or describe what went wrong, and you will fix them. This back-and-forth
IS the lesson.

Please:
- Don't try too hard to be perfect on the first attempt. Build it naturally.
- When I report a bug, fix it and briefly explain what went wrong and why,
  in plain English a non-programmer could understand.
- If you make a design choice (which algorithm, which data structure, how
  to organise the code), mention it so I can ask about it later.
- Keep everything in a single Python file, no external packages.

The transcript of this session will become the chapter. Readers will see
exactly what I typed and exactly what you responded. Be yourself.

Here is the game I want to build:
```
