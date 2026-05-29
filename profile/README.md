# profile/

Your identity and writing voice, learned once during onboarding and read by the journalist on every run.

| File | Written by | Read by | Purpose |
|------|-----------|---------|---------|
| `writer.md` | onboarding Step 1 | research stage (scope) | Who you are, your beat, your audience — sets the *altitude* of every draft |
| `writing-style.md` | onboarding Steps 2–3 | write stage (`dj-write`) | Your **house voice** — emulated unless a per-article `voice` arg overrides it |

Both are **gitignored** (they're yours, not the repo's). Templates live here as `*.template.md`.

Generate them by running onboarding:
- **Claude Code:** `/onboard`
- **Any agent:** "run `onboarding/onboard.md`"
- Check status anytime: `python3 onboarding/onboard.py status`

> The journalist stays a **neutral referee on the facts** regardless of your profile. These files shape
> *relevance and voice* — what to foreground for your reader and how the prose should sound — never the verdict.
