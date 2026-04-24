# Three Projects: A Progressive Complexity Arc

Three projects that each introduce exactly one new architectural concept.

## Project 1: Music Visualizer (Chapter 2 territory)

**New concept**: None — pure HTML/CSS/JS, single file, no server, no persistence.

- Web Audio API's `AnalyserNode.getFrequencyData()` gives a live FFT of the audio stream
- Draw to `<canvas>` every frame using frequency data
- Start with bars, iterate toward particles/circles/shaders
- Deploy on GitHub Pages — single HTML file, no build step
- Visually striking with minimal code; immediate feedback loop

**Why this project**: It's the most visually appealing thing you can build with zero infrastructure. The reader sees something beautiful on screen within minutes.

## Project 2: Recipe App with AI (Chapter 3 territory)

**New concept**: External API call (LLM integration via GPT-4o-mini or similar).

- User types what's in their fridge, AI returns a recipe
- First attempt: API call from frontend — works, but key is exposed in browser console
- This is why backends exist: rebuild with a thin proxy (Node.js or Flask) that holds the API key
- `.env` file for the key, `.gitignore` to keep it out of GitHub
- Deploy backend to Cloud Run (free tier)

**Why this project**: The AI does 90% of the interesting work — you can't replace it with a lookup table. This is genuine AI integration, not a gimmick. Also teaches the reader the most common security mistake in frontend development.

## Project 3: Bookmarks App with Database (Chapter 4 territory)

**New concept**: Database persistence (SQLite or Supabase).

- Save URLs with a title and tags, search/filter by tag
- One table: `id`, `url`, `title`, `tags`, `created_at`
- Basic CRUD: add, list, search, delete
- The database IS the app — without persistence, there's nothing

**Why this project**: The simplest possible app that genuinely requires a database. No auth, no AI, no real-time — just storage and retrieval. Isolates the concept perfectly.

---

## Pedagogical Arc

| Project | Frontend | Backend | API | Database |
|---------|----------|---------|-----|----------|
| Music Visualizer | Yes | No | No | No |
| Recipe App | Yes | Yes (proxy) | Yes (LLM) | No |
| Bookmarks App | Yes | Yes | No | Yes |

Each chapter adds exactly one new layer. The reader never has to learn two new concepts at once.
