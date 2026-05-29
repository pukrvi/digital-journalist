# Digital Journalist — Onboarding playbook (agent: run this)

**You are onboarding a new user to the Digital Journalist.** This is the first thing a person
experiences, so make it feel like a sharp editor taking them on — warm, fast, concrete.
**Target: ~5 minutes, 5 steps.** Do not interrogate. Each step is one short exchange.

> **Agent notes.** In **Claude Code**, use `AskUserQuestion` for the multiple-choice steps (2–4 options each)
> — it's faster for the user than free text. In **Codex / Openclaw / other** agents, ask the question inline
> and accept a typed answer. Run the deterministic bits with the helper scripts shown below.

**Golden rule — teach while you ask.** At every step, add one line of *why this helps* so the user
learns the product as they configure it. The "Why it helps" lines below are for you to paraphrase, not read verbatim.

First, check what's already done so you skip finished steps:
```bash
python3 onboarding/onboard.py status
```

---

## Step 1 — Who you are  (~30s)

Ask, in one go: **your name, your role, what you publish about (beats), and who you publish for (audience).**

> **Why it helps (tell them):** "The journalist writes *for your reader*. Your beat and audience set the
> altitude of every draft — what to assume they know, which angle matters. It stays a neutral referee on the
> facts; this just aims the lens."

Save it:
```bash
python3 onboarding/onboard.py profile --name "<name>" --role "<role>" --beats "<topics>" --audience "<who they write for>"
```

---

## Step 2 — Your writing style, in your words  (~45s)

Ask 3 quick choices (AskUserQuestion in Claude Code):
1. **Voice** — measured-analytical · narrative-literary · punchy-provocative · contrarian-sharp
2. **Sentence rhythm** — short & punchy · varied (a short line after two long ones) · long & flowing
3. **Writers or publications you'd like to read like** (free text — e.g. "The Economist, Ben Thompson").

> **Why it helps:** "Finished articles should sound like *you*, not generic AI. This becomes the **house voice**
> the writer emulates — you can still override it per article."

Hold these answers for Step 3 (you'll save voice + style together).

---

## Step 3 — Show, don't just tell: upload a writing sample  (~90s) — the magic step

Ask the user to **point you at one thing they've written** — a blog post, essay, LinkedIn post, a doc, a PDF.
Accept a file path or pasted text (`.md/.txt/.pdf/.docx` all work).

Run the quantitative analyzer:
```bash
python3 onboarding/analyze_style.py "<path-to-sample>" --json > /tmp/dj_style.json
```
Then **you read the sample yourself** and extract the *qualitative* voice the numbers can't see:
- the **signature moves** (how they open, how they land an ending, how they bring in evidence),
- words/phrases they **favor** and **avoid**,
- tone (dry? warm? combative? wry?).

Compose the style guide, folding in the Step-2 answers and your read:
```bash
python3 onboarding/onboard.py style --json /tmp/dj_style.json \
  --voice "<from step 2 + your read>" --rhythm "<from step 2>" \
  --signature "<their signature moves>" --favors "<words/structures>" \
  --avoids "<tics they avoid>" --admires "<from step 2>"
```

> **Why it helps:** "Telling us your style is good; *showing* us is better. We measure your real rhythm —
> sentence length, paragraph cadence, how often you reach for an em-dash — and reverse-engineer a style guide.
> Result: first drafts land far closer to publishable, in your voice." If the user has nothing to upload, skip —
> the Step-2 answers alone still seed a usable house voice.

---

## Step 4 — Pick your search providers  (~45s)

Show the landscape and let them choose (AskUserQuestion, multiSelect). Explain the three tiers plainly:
```bash
python3 tools/api/search.py --status
```
- **Keyless — already working:** DuckDuckGo. You can research today with zero setup.
- **Free with a key (recommended):** Tavily (AI-ready, 1k/mo), Serper (Google results, 2.5k one-time),
  Gemini (Google grounding, 1.5k/day), Brave (independent index, 2k/mo). Two or three of these is plenty.
- **Paid deep research (optional):** Perplexity, OpenAI, Anthropic, xAI — only used after the free pass, and only if you enable them.

> **Why it helps:** "More providers = a wider net = fewer blind spots. No single engine sees everything —
> Brave's index is independent of Google, Gemini reads the live web, Tavily returns clean AI-ready text.
> The aggregator fans out across all you've enabled and de-duplicates. You only need a couple to start."

Ask which they want to set up now. Anything they skip still works later.

---

## Step 5 — Add the keys (stored safely, locally)  (~60s)

For each provider they chose, give the signup link + free tier, ask for the key, and store it securely:
```bash
python3 onboarding/onboard.py key --provider <tavily|serper|gemini|brave|...> --value "<key>"
```
Signup links: `tools/api/keys.env.example` (or the table in the README / wiki).

Then verify everything connects:
```bash
python3 tools/api/ping.py
```

> **Why it helps / the safety promise:** "Keys live **only on your machine** — in a gitignored file with
> `0600` (owner-only) permissions, shown **masked** (first 4 + last 4), and **fingerprinted** (SHA-256) so you
> can confirm which key is loaded without ever exposing it. Nothing is committed or sent anywhere but the
> provider you're calling. Want them encrypted at rest too? `python3 onboarding/keys_manager.py lock`."

---

## Wrap up

Run the final checklist and celebrate briefly:
```bash
python3 onboarding/onboard.py status
```
Then tell them how to start, and offer to do it now:

> "You're set. To write your first piece, just say: **'Run the digital-journalist on: <your topic>'.**
> I'll do a quick scan, ask you a couple of scoping questions, research the ocean, then come back with
> evidence-informed questions about voice and angle before I write a word."

Keep the whole thing under ~5 minutes. If the user says "just defaults," set a neutral profile, skip the
upload, leave DuckDuckGo as the only provider, and finish — they can deepen any step later by re-running `/onboard`.
