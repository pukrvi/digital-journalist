# Failure Modes

Mistakes encountered in past runs and how to avoid them. Updated at the end of every run. Read at the start of every run as part of memory load.

## Seed failure modes (pre-first-run)

### Source monoculture
**Symptom:** 60%+ of citations come from one or two publications.
**Why it happens:** The first 5 search results dominate research because they appear in every lens's query.
**How to avoid:** During scoping, list the publications already represented. Bias subsequent lens queries away from those.

### Quote without source
**Symptom:** "Studies show…" or "Experts say…" appears in the draft without an inline citation.
**Why it happens:** A finding is paraphrased before the source URL is captured.
**How to avoid:** Every research file MUST attach a numbered source to every claim before any synthesis runs.

### Strawman contrarian
**Symptom:** The "contrarian" section presents a weak version of the counter-argument that's easy to refute.
**Why it happens:** The agent searched for "<topic> criticism" but didn't read the most articulate critic.
**How to avoid:** Name the strongest contrarian by name. Read their most-cited piece. Quote them at length.

### Stale data
**Symptom:** Citing 2018 statistics for a 2026 article without flagging the date.
**Why it happens:** Search results don't always surface most-recent data first.
**How to avoid:** During verification, every statistic gets a date stamp. If older than 3 years, search for a more recent version or annotate "as of <year>."

### Verifier capture
**Symptom:** Adversarial verification confirms everything because the verifier didn't actually search for refutation.
**Why it happens:** Confirmation bias — the verifier reads the original source and agrees.
**How to avoid:** Verification agents are prompted to default to "refuted=true" unless independent evidence appears. Counter-search must be explicit.

### Padding
**Symptom:** Article exceeds 3000 words with low insight density per paragraph.
**Why it happens:** Length is mistaken for thoroughness.
**How to avoid:** Cut every paragraph that doesn't deliver a fact, quote, or synthesis the reader didn't have. If a section can be deleted without losing insight, delete it.

### Burying weak areas
**Symptom:** The article reads as confident when the underlying research is thin in places.
**Why it happens:** Pressure to deliver a strong narrative.
**How to avoid:** Mandatory "What we don't know" section near the end of every article. Synthesis phase explicitly identifies weak areas.

---

## Run-discovered failure modes

### Args delivered as JSON string, not object
**Symptom:** The workflow ran with a mangled slug (`topic-...`) and every arg except the topic silently dropped — angle, audience, and timestamp never took effect. (run: the-ai-cost-reckoning)
**Why it happens:** The Workflow harness passed `args` as a JSON-encoded *string*, but the workflow's entry guard `typeof args === 'string' ? { topic: args } : args` treated the entire JSON blob as the topic string, so the whole `{"topic": "...", "angle": "...", ...}` payload became the topic and no other field was ever read.
**How to avoid:** Parse a JSON-looking string with `JSON.parse` *before* falling back to bare-topic. Fix shipped: try `JSON.parse(args)` when `typeof args === 'string'`, and only treat it as a bare topic if parsing fails or yields a non-object. Lesson: always JSON.parse string args defensively — never assume a string arg is the topic.

### Big-output schema agent skipped StructuredOutput
**Symptom:** The write/synthesis agent wrote its output file successfully, then ended its turn *without* calling StructuredOutput — aborting the whole run after ~2 hours of completed research. (run: the-ai-cost-reckoning)
**Why it happens:** On a very large file-writing phase, the agent treated the file write as the deliverable and ended without emitting the required structured return, so the orchestrator saw a missing StructuredOutput and failed the step even though the work was done and on disk.
**How to avoid:** Two mitigations shipped. (1) Add an explicit "your final action MUST be a StructuredOutput call" reminder to every heavy schema agent's prompt. (2) Provide a schema-FREE finisher (dj-finisher) that recovers an aborted run by reading the salvaged artifacts and finalizing metadata/memory without needing a structured return. Lesson: for very large file-writing phases, prefer schema-free agents (write file + confirm) or split the file-write step from the structured-return step so a heavy write can't swallow the required final call.
