# Onboarding

A ~5-minute, LLM-native flow. Your agent runs the playbook ([`onboarding/onboard.md`](../onboarding/onboard.md))
conversationally; helper scripts do the file writes and secure storage so steps are idempotent.

**Start it:**
- Claude Code: `/onboard`
- Any agent: "run `onboarding/onboard.md`"
- Check progress anytime: `python3 onboarding/onboard.py status`

## The five steps

| Step | You provide | Why it helps |
|------|-------------|--------------|
| **1. Who you are** | name, role, beats, audience | The journalist writes *for your reader* — this sets the altitude of every draft. |
| **2. Writing style** | voice, sentence rhythm, writers you admire | Becomes the **house voice** the writer emulates, so drafts sound like you. |
| **3. Upload a sample** | a file/text you wrote | We *measure* your real style (sentence length, cadence, punctuation tics) and reverse-engineer a style guide — drafts land closer to publishable. |
| **4. Pick providers** | which search APIs to enable | More providers = wider net = fewer blind spots. DuckDuckGo works now; a couple of free keys go a long way. |
| **5. Add keys** | API keys for the chosen providers | Stored locally only, masked, fingerprinted, gitignored. Nothing leaves your machine. |

## What it produces

- `profile/writer.md` — read by the research stage (relevance/altitude).
- `profile/writing-style.md` — read by the write stage (your voice). Includes a measured fingerprint from
  your uploaded sample. Override per-article with the `voice` arg.
- Keys saved to `tools/api/keys.env` (see [Security](Security.md)).

Both profile files are **gitignored** — they're yours.

## Doing it manually

```bash
python3 onboarding/onboard.py profile --name "Ada" --role "Founder" --beats "AI, fintech" --audience "operators"
python3 onboarding/analyze_style.py my-essay.md --json > /tmp/style.json
python3 onboarding/onboard.py style --json /tmp/style.json --voice "measured-analytical" --rhythm "varied"
python3 onboarding/onboard.py key --provider tavily --value "tvly-..."
python3 onboarding/onboard.py status
```

## Minimal path

Say "just defaults" and the agent sets a neutral profile, skips the sample, leaves DuckDuckGo as the only
provider, and finishes. Re-run `/onboard` anytime to deepen any step.
