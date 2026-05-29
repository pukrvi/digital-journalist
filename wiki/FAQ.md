# FAQ

**Do I need API keys to start?**
No. DuckDuckGo is keyless and works immediately. Adding a couple of free keys (Tavily, Serper, Gemini, Brave)
widens the net — onboarding Step 5, or `python3 onboarding/keys_manager.py set <provider> <key>`.

**Which agents does it work with?**
Claude Code, OpenAI Codex, Openclaw, and similar. Claude Code gets the `/onboard` command and named workflow;
others read [AGENTS.md](../AGENTS.md) and run the playbook/scripts directly.

**Is it free to run?**
Search can be entirely free (a full article used a rounding-error of the free tiers). Your agent's own model
usage (Claude/GPT) is the real cost. Paid search providers are opt-in (`ALLOW_PAID=1`).

**Does it take a side?**
By default it's a **neutral referee** — it weighs the evidence and steelmans the contrarian view. In Round 2
you can ask it to take the side the evidence favors or to foreground a specific tension. Your POV guides
emphasis; it never suppresses counter-evidence.

**Why two stages and two rounds of questions?**
Research is ~80% of the cost and best treated as a durable checkpoint. The second round of questions is
*evidence-informed* — you choose voice and angle after seeing what the research actually found. See
[Architecture](Architecture.md).

**Will the article sound like generic AI?**
Not if you complete onboarding Step 3 — it learns your voice from a sample you wrote and emulates it. The
house style also bans the usual AI-slop tells.

**How does it avoid hallucinated/viral "facts"?**
Adversarial verification: it tries to *refute* the load-bearing claims before writing, defaulting to
"refuted" when independent support is weak. See [Writing & Sources](Writing-and-Sources.md).

**A run failed — did I lose the research?**
No. Research is written to disk as it goes. Re-run Stage 2 (`dj-write`) pointed at the article folder to
finish from the checkpoint.

**Can I write multiple articles from one research run?**
Yes — run `dj-write` with `outFolder` ≠ `srcFolder` to spin a new angle off the same dossier, no re-research.

**Where do my keys and profile go? Are they committed?**
Local only, and gitignored. Keys in `tools/api/keys.env` (`0600`, masked, fingerprinted); profile in
`profile/*.md`. See [Security](Security.md).

**How do I update the wiki on GitHub?**
Copy `wiki/*.md` into your repo's GitHub Wiki (clone `<repo>.wiki.git`), or just let the README link to them
in-repo — both render on GitHub.
