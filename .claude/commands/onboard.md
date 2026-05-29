---
description: Onboard a new user to the Digital Journalist (5 quick steps, ~5 min)
---

Run the onboarding playbook at `onboarding/onboard.md`.

Follow it exactly: 5 steps (who you are → writing style → upload a sample to extrapolate style →
choose search providers → add API keys), each with a one-line "why this helps." Use `AskUserQuestion`
for the multiple-choice steps. Start by running `python3 onboarding/onboard.py status` to skip anything
already configured. Keep it under ~5 minutes; if the user wants defaults, set a neutral profile and finish.
