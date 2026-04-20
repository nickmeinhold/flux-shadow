# Permissions — Progressive Trust

Permissions are introduced progressively throughout the book, mirroring how
trust develops between you and Claude.

## Chapter 1: The Default

Claude asks permission for everything. Every file read, every bash command,
every file write — you see a prompt and say yes or no.

This is safe but tedious. After your tenth "yes" in a row, you'll want to
change it. That's the point — you should feel the friction before you remove it.

## Chapter 2 or 3: Opening Up

Permissions live in `~/.claude/settings.json`. You can edit this file
yourself, but you don't have to — just ask Claude. Say "allow yourself
to read files without asking me" and he'll edit `settings.json` for you.

**Stage 1 — Let Claude look freely:**
```json
{
  "permissions": {
    "allow": [
      "Read",
      "Glob",
      "Grep"
    ]
  }
}
```
Claude can read any file and search your codebase without asking. He still
asks before writing, editing, or running commands.

**Stage 2 — Let Claude run commands:**
```json
{
  "permissions": {
    "allow": [
      "Read",
      "Glob",
      "Grep",
      "Bash"
    ]
  }
}
```
Claude can now run shell commands (npm install, git status, python scripts)
without asking. He still asks before writing or editing files.

**Stage 3 — Let Claude write, but only in your projects:**
```json
{
  "permissions": {
    "allow": [
      "Read",
      "Glob",
      "Grep",
      "Bash",
      "Write(~/claude-projects/**)",
      "Edit(~/claude-projects/**)"
    ]
  }
}
```
Claude can now read, run commands, and write files — but only inside your
projects directory. He can't touch anything else on your system. This is
Robin's approach (with `~/git/**` instead of `~/claude-projects/**`).

**Stage 4 — The "I trust Claude, just do it" option:**
```json
{
  "permissions": {
    "allow": [
      "Read",
      "Glob",
      "Grep",
      "Bash",
      "Write",
      "Edit"
    ]
  }
}
```
Claude can do anything without asking. This is convenient but means Claude
could write files anywhere on your system. Only do this if you understand
the risk.

## Robin's Actual Setup

```json
{
  "permissions": {
    "allow": [
      "Read",
      "Glob",
      "Grep",
      "Bash",
      "WebSearch",
      "WebFetch",
      "Write(~/git/**)",
      "Write(~/data/**)",
      "Write(/tmp/**)",
      "Edit(~/git/**)",
      "Edit(~/data/**)",
      "Edit(/tmp/**)"
    ]
  }
}
```

Broad read and search permissions. Write and edit scoped to specific
directories. Claude can look anywhere but can only change files in the
places Robin works. This is the sensible middle ground.

## Part II, Chapter 8: Autonomous Agents

An autonomous agent can't stop and ask permission — there's nobody watching.
So you give it broad permissions, but inside a Docker container. The
container is the sandbox. Claude has full access inside, but "inside" is
an isolated environment that can't touch your real system.

This is the final step in the progression:
1. Ask every time (Chapter 1)
2. Allow reads freely (Chapter 2)
3. Allow commands (Chapter 2-3)
4. Allow scoped writes (Chapter 3+)
5. Allow everything — inside a container (Chapter 8)

**Permissions are progressive trust.** You start cautious, open up as you
learn what Claude does, and for autonomous agents you give full access but
inside a sandbox.
