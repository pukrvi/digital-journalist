// SPDX-License-Identifier: Apache-2.0
// Copyright 2026 INFINITIGRID TECHNOLOGIES (OPC) PRIVATE LIMITED. Created by Puneet Vishnawat.
//
// Digital Journalist — RESEARCH STAGE (v3, Stage 1 of 2).
//
// The "boil the ocean" research engine. Reads memory, scopes the topic, fans out across
// 6-8 lenses (contrarian mandatory) using BOTH the multi-provider aggregator AND native
// WebSearch, with a hard mandate to seek government/agency data, consulting & market-research
// firms, and comparable companies — not just journalism and blogs. Consolidates everything
// into a master evidence dossier, adversarially verifies the load-bearing claims, fills gaps,
// synthesizes, and then PROPOSES a second round of deeper, evidence-informed clarifying
// questions for the human.
//
// It deliberately STOPS before writing. The dossier is a durable checkpoint: an aborted or
// expensive run never loses the research, and the human gets to inject voice + POV — informed
// by what the evidence actually found — before the (cheap, schema-free) write stage runs.
//
// TWO-ROUND CLARIFYING QUESTIONS (see CLAUDE.md → Run protocol):
//   Round 1 (before this stage): the orchestrator asks scope questions in the conversation and
//            passes the answers in as args.pov / args.angle / args.clarifications / args.mustInclude.
//   Round 2 (after this stage): this workflow writes research/round2-questions.md — deeper
//            questions grounded in the findings. The orchestrator asks them, then runs dj-write.
//
// Invoke:
//   Workflow({ name: "digital-journalist", args: {
//     topic: "...",  angle, audience, pov, clarifications, mustInclude, mustAvoid, timestamp
//   }})
//
// Output: articles/<slug>/ — master.md, research/{scope,<lens>,verification,gaps,synthesis,round2-questions}.md

export const meta = {
  name: 'digital-journalist',
  description: 'RESEARCH stage: boil-the-ocean multi-provider + native search across 6-8 lenses (contrarian mandatory), mandated to use government/agency, consulting & market-research, and comparable-company sources. Builds a master evidence dossier + adversarial verification + synthesis, then proposes a second round of evidence-informed clarifying questions. Stops before writing (run dj-write next).',
  whenToUse: 'Stage 1 of the digital-journalist. Ask Round-1 scope questions in the conversation first, then run this. After it finishes, read research/round2-questions.md, ask Round 2, then run dj-write.',
  phases: [
    { title: 'Load memory' },
    { title: 'Scope' },
    { title: 'Setup folder' },
    { title: 'Research (multi-lens)' },
    { title: 'Master dossier' },
    { title: 'Verify (adversarial)' },
    { title: 'Fill gaps' },
    { title: 'Synthesize' },
    { title: 'Round-2 questions' },
  ],
}

// ---------- Args (robust: harness may deliver args as a JSON string) ----------

let input
if (typeof args === 'string') {
  const t = args.trim()
  input = (t.startsWith('{') && t.endsWith('}')) ? (() => { try { return JSON.parse(t) } catch (e) { return { topic: args } } })() : { topic: args }
} else {
  input = args || {}
}
const topic = input.topic
if (!topic || typeof topic !== 'string') throw new Error('digital-journalist requires args.topic (string).')

const angle = input.angle || ''
const audience = input.audience || 'general business reader (Atlantic/Bloomberg style — smart non-specialist)'
const pov = input.pov || ''
const clarifications = (input.clarifications && typeof input.clarifications === 'object') ? input.clarifications : {}
const mustInclude = Array.isArray(input.mustInclude) ? input.mustInclude : []
const mustAvoid = Array.isArray(input.mustAvoid) ? input.mustAvoid : []
const timestamp = input.timestamp || 'unspecified'

const slug = topic.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 60)
const folder = `articles/${slug}`

const USER_INTENT = `
**User intent (guides emphasis & framing — never suppresses counter-evidence):**
- Topic: ${topic}
- Angle: ${angle || '(none specified)'}
- Audience: ${audience}
- Round-1 POV / stance: ${pov || '(none — stay neutral)'}
- Round-1 clarifying answers: ${Object.keys(clarifications).length ? JSON.stringify(clarifications) : '(none)'}
- Must include: ${mustInclude.length ? mustInclude.join('; ') : '(nothing specified)'}
- Must avoid: ${mustAvoid.length ? mustAvoid.join('; ') : '(nothing specified)'}

The POV sets emphasis only. The contrarian lens stays mandatory and steelmanned; if evidence
contradicts the POV, surface it. A journalist serves the reader, not the commissioner.
`.trim()

const SEARCH_TOOLKIT = `
**Use BOTH search systems (boil the ocean):**
1. Native **WebSearch** — several varied queries.
2. The aggregator (DuckDuckGo + Tavily + Serper + Gemini grounding, deduped, with AI summaries):
   \`python3 tools/api/search.py "<query>" --count 8 --aggregate --json\` (from project root).
   Parse \`.results[]\` (title/url/snippet/sources) and \`.ai_summaries\` (leads — verify, never cite raw).
3. Read full sources with **WebFetch**, falling back to \`bash tools/fetch.sh <url> --json\`.
4. Specialized: \`bash tools/arxiv.sh "<q>"\` (papers); \`bash tools/wiki.sh "<topic>"\` (history → follow its citations);
   \`python3 tools/api/search.py "<q>" --provider gemini\` (real-time). \`--status\` shows which providers have keys.
5. A URL surfaced by multiple providers (\`sources\` length > 1) is a relevance signal.
`.trim()

const SOURCE_PRIORITY = `
**Source-class mandate — actively seek these, and prefer them in this order:**
1. **PRIMARY / OFFICIAL** — government statistics & agencies (BLS, Census, the Federal Reserve incl.
   regional banks, CBO, GAO, SEC/EDGAR filings, FTC, OECD, IMF, World Bank, Eurostat, central banks &
   national statistics offices) and official disclosures (10-K, earnings calls, regulator filings).
2. **PEER-REVIEWED / ACADEMIC** — journals, NBER, university research centers; arXiv (mark "preprint").
3. **MARKET RESEARCH & CONSULTING** — Gartner, Forrester, IDC, McKinsey, BCG, Bain, Deloitte, PwC,
   Accenture, CB Insights, PitchBook, Statista, eMarketer, Nielsen. Name firm + report + date; note the
   commercial incentive.
4. **COMPARABLES** — for any company/industry topic, ALWAYS triangulate against peer/competitor
   companies (their filings, results, statements), not just the focal subject.
5. **ESTABLISHED JOURNALISM** — NYT, WSJ, FT, Reuters, AP, Bloomberg, The Economist, The Atlantic, ProPublica.
6. **EVERYTHING ELSE** (Substack, blogs, social) — Tier 3-4: use to SURFACE arguments/leads, then verify
   against 1-5. Quote only when the person is themselves the authority.

For this topic, deliberately run at least one query each targeting (a) a government/agency source,
(b) a consulting/market-research firm, and (c) comparable companies/peers. Note in your return which
of these source classes you actually reached.
`.trim()

const STRUCT_REMINDER = `
**CRITICAL:** After writing any file(s), your VERY LAST action MUST be the StructuredOutput tool call
with the required JSON. Never end your turn on a file write or prose — the step fails without it.
`.trim()

log(`[research] ${topic}`)
log(`  slug=${slug} pov=${pov || 'neutral'} mustInclude=${mustInclude.length}`)

// ---------- Schemas (kept only where structured returns drive control flow) ----------

const MEMORY_SCHEMA = { type: 'object', required: ['principles', 'lessonsLearned'], additionalProperties: false, properties: {
  principles: { type: 'array', items: { type: 'string' } },
  lessonsLearned: { type: 'array', items: { type: 'string' } },
  reliableSources: { type: 'array', items: { type: 'string' } },
  unreliableSources: { type: 'array', items: { type: 'string' } },
  antiPatterns: { type: 'array', items: { type: 'string' } },
  providerTips: { type: 'array', items: { type: 'string' } },
} }

const SCOPE_SCHEMA = { type: 'object', required: ['coreQuestion', 'lenses'], additionalProperties: false, properties: {
  coreQuestion: { type: 'string' },
  subQuestions: { type: 'array', items: { type: 'string' } },
  lenses: { type: 'array', minItems: 6, maxItems: 9, items: { type: 'object', required: ['name', 'focus', 'searchQueries'], additionalProperties: false, properties: {
    name: { type: 'string' }, focus: { type: 'string' }, searchQueries: { type: 'array', items: { type: 'string' }, minItems: 3, maxItems: 8 },
  } } },
  likelyControversies: { type: 'array', items: { type: 'string' } },
  povHandling: { type: 'string' },
} }

const LENS_SCHEMA = { type: 'object', required: ['lens', 'sourcesFound', 'keyFindings'], additionalProperties: false, properties: {
  lens: { type: 'string' },
  sourcesFound: { type: 'integer' },
  keyFindings: { type: 'array', items: { type: 'string' } },
  strongestQuote: { type: 'string' },
  bestDataPoint: { type: 'string' },
  sourceClassesReached: { type: 'array', items: { type: 'string' } },
  surprises: { type: 'array', items: { type: 'string' } },
  gaps: { type: 'array', items: { type: 'string' } },
  domainsCovered: { type: 'array', items: { type: 'string' } },
} }

const MASTER_SCHEMA = { type: 'object', required: ['sourcesProcessed', 'quotesCaptured', 'dataPoints'], additionalProperties: false, properties: {
  sourcesProcessed: { type: 'integer' }, quotesCaptured: { type: 'integer' }, dataPoints: { type: 'integer' },
  stakeholderVoices: { type: 'integer' }, viewsCovered: { type: 'array', items: { type: 'string' } },
  tierBreakdown: { type: 'object', additionalProperties: true }, sourceClassCoverage: { type: 'object', additionalProperties: true },
  unresolvedQuestions: { type: 'array', items: { type: 'string' } },
} }

const CLAIMS_SCHEMA = { type: 'object', required: ['claims'], additionalProperties: false, properties: {
  claims: { type: 'array', minItems: 6, maxItems: 14, items: { type: 'object', required: ['id', 'text', 'whyImportant'], additionalProperties: false, properties: {
    id: { type: 'string' }, text: { type: 'string' }, originatingLens: { type: 'string' }, whyImportant: { type: 'string' },
  } } },
} }

const VERIFY_SCHEMA = { type: 'object', required: ['claimId', 'verdict', 'confidence'], additionalProperties: false, properties: {
  claimId: { type: 'string' }, verdict: { type: 'string', enum: ['confirmed', 'partially-confirmed', 'refuted', 'unverifiable'] },
  confidence: { type: 'number', minimum: 0, maximum: 1 },
  supportingSources: { type: 'array', items: { type: 'string' } }, counterSources: { type: 'array', items: { type: 'string' } },
  nuance: { type: 'string' }, rewriteSuggestion: { type: 'string' },
} }

const GAPS_SCHEMA = { type: 'object', required: ['criticalGaps'], additionalProperties: false, properties: {
  criticalGaps: { type: 'array', items: { type: 'string' }, maxItems: 4 }, niceToHaves: { type: 'array', items: { type: 'string' } },
} }

// ---------- Phase 1: Load memory ----------

phase('Load memory')
const mem = await agent(`Project root is the working dir. Read if present (Read tool; skip silently if absent — don't create):
CLAUDE.md, memory/learnings.md, memory/source-quality.md, memory/failure-modes.md, memory/search-providers.md, memory/writing-standards.md, Idea.md.

Return a JSON digest of what you ACTUALLY found: principles (from CLAUDE.md), lessonsLearned, reliableSources / unreliableSources (domains), antiPatterns (failure modes), providerTips (which provider suits which lens).

${STRUCT_REMINDER}`, { label: 'load-memory', phase: 'Load memory', schema: MEMORY_SCHEMA })
log(`memory: ${mem.lessonsLearned.length} lessons, ${(mem.reliableSources||[]).length} reliable / ${(mem.unreliableSources||[]).length} unreliable domains`)

// ---------- Phase 2: Scope ----------

phase('Scope')
const scope = await agent(`Scope this topic for a deep investigative feature.

${USER_INTENT}
${SEARCH_TOOLKIT}
${SOURCE_PRIORITY}

**Process:** ground scoping in reality first (2-3 native WebSearches + one \`python3 tools/api/search.py "${topic}" --count 5 --aggregate --json\`). Then decide the single most important, concrete **core question**; define 6-8 **lenses** (contrarian MANDATORY); give each 3-6 varied queries (institutional + outsider phrasings; skeptical framings for contrarian; and for at least one lens, queries that explicitly target government/consulting/market-research/peer-company sources). Predict 3-5 controversies. In "povHandling", say how you'll honor the user's POV while keeping the piece fair.

Lens menu (pick 6-8; contrarian REQUIRED): mainstream, contrarian, data, historical, stakeholders, expert, comparative, follow-the-money, international. Lowercase single-word names.
Apply memory: ${JSON.stringify({ lessons: mem.lessonsLearned, providerTips: mem.providerTips })}

${STRUCT_REMINDER}`, { label: 'scope', phase: 'Scope', schema: SCOPE_SCHEMA })

if (!scope.lenses.some(l => /contrarian|critical|sceptic|skeptic|dissent/i.test(l.name))) throw new Error('Scope failed: contrarian lens missing.')
log(`scope: ${scope.lenses.map(l => l.name).join(', ')}`)

// ---------- Phase 3: Setup folder ----------

phase('Setup folder')
await agent(`From project root: \`mkdir -p ${folder}/research\`. Then write \`${folder}/research/scope.md\`:

# Scope: ${topic}
**Slug:** ${slug} | **Angle:** ${angle || '(none)'} | **Audience:** ${audience}
**Round-1 POV:** ${pov || '(neutral)'} | **Timestamp:** ${timestamp}
**Must include:** ${mustInclude.join('; ') || '(none)'} | **Must avoid:** ${mustAvoid.join('; ') || '(none)'}

## Core question
${scope.coreQuestion}

## Sub-questions
${(scope.subQuestions || []).map(q => `- ${q}`).join('\n') || '(none)'}

## POV handling
${scope.povHandling || '(neutral)'}

## Lenses
${scope.lenses.map(l => `### ${l.name}\n${l.focus}\n\n**Queries:**\n${l.searchQueries.map(q => `- \`${q}\``).join('\n')}`).join('\n\n')}

## Likely controversies
${(scope.likelyControversies || []).map(c => `- ${c}`).join('\n') || '(none)'}

Confirm done in 1 line.`, { label: 'setup-folder', phase: 'Setup folder' })

// ---------- Phase 4: Multi-lens research ----------

phase('Research (multi-lens)')
const research = (await parallel(scope.lenses.map(lens => () =>
  agent(`Research "${topic}" through the **${lens.name}** lens. Gather a holistic, all-sides picture.

**Focus:** ${lens.focus}
**Starter queries:** ${lens.searchQueries.map(q => `"${q}"`).join(', ')}

${USER_INTENT}
${SEARCH_TOOLKIT}
${SOURCE_PRIORITY}

**Process:** 4-7 searches across BOTH systems; READ full content (WebFetch / tools/fetch.sh) — never cite a snippet; extract EXACT verbatim quotes with full attribution. For the **contrarian** lens, name the 1-2 strongest critics and quote them at length (a weak contrarian section is the #1 failure mode).

**Per source (min 6, target 10):** url, title, author, publication, date (YYYY-MM-DD or "Undated"), **tier (1-5 per CLAUDE.md)**, **sourceClass** (official/academic/market-research/consulting/comparable/journalism/other), exactQuotes[], keyClaims[], dataPoints[] (stat + unit + date), credibilityNotes (bias/funding/track record). Diversify: ≤2 per publication, ≥4 domains.

**Write to \`${folder}/research/${lens.name}.md\`** (## Sources → ### [n] Title → metadata incl. tier & sourceClass → Exact quotes → Key claims → Data points). Append as you go.

Return JSON per the lens schema. \`bestDataPoint\` = most cite-worthy stat w/ attribution. \`sourceClassesReached\` = which of {official, academic, market-research/consulting, comparable, journalism} you actually got.

${STRUCT_REMINDER}`, { label: `lens:${lens.name}`, phase: 'Research (multi-lens)', schema: LENS_SCHEMA })
))).filter(Boolean)

log(`lenses: ${research.length}/${scope.lenses.length}, sources≈${research.reduce((a, r) => a + (r.sourcesFound || 0), 0)}`)
if (research.length < 4) throw new Error(`Too few lenses completed (${research.length}).`)

// ---------- Phase 5: Master dossier ----------

phase('Master dossier')
const master = await agent(`Build the **master dossier** — the single consolidated knowledge base, assembled from ALL processed sources. The writer draws every quote/fact/figure from here.

${USER_INTENT}

Read EVERY lens file in \`${folder}/research/\` (${research.map(r => `${r.lens}.md`).join(', ')}). Then write \`${folder}/master.md\`:

# Master Dossier: ${topic}
(header: topic, angle, audience, stance, timestamp, lens count)

## 1. Executive synthesis (5-8 bullets) — holistic knowledge across all views
## 2. The spectrum of views — per view: claim, who holds it, strongest evidence, weakest point (contrarian steelmanned)
## 3. Quote bank — every notable verbatim quote, **ordered most-authoritative-speaker first** (named execs of major orgs / govt officials / cited academics / primary-study authors before analysts before anonymous voices). Format: > "quote" — Name, Title, Publication, YYYY-MM-DD [tier N] (url)
## 4. Fact & data ledger — table: Fact | Value | As of | Source | Tier. Flag anything >3 years old. **Sort Tier 1 → 5.**
## 5. Stakeholder voices
## 6. Open questions / unresolved
## 7. Source index — numbered, deduped, **grouped by tier (1 first)**, each noting sourceClass + lens(es).

Rules: no entry without a source; dedupe across lenses (note all). Preserve exact quotes.

Return JSON per the master schema (counts + viewsCovered + tierBreakdown {"1":n,...} + sourceClassCoverage {"official":n,"consulting":n,...} + unresolvedQuestions).

${STRUCT_REMINDER}`, { label: 'master', phase: 'Master dossier', schema: MASTER_SCHEMA })
log(`master: ${master.sourcesProcessed} sources, ${master.quotesCaptured} quotes, ${master.dataPoints} data pts; classes=${JSON.stringify(master.sourceClassCoverage||{})}`)

// ---------- Phase 6: Adversarial verification ----------

phase('Verify (adversarial)')
const claims = await agent(`From \`${folder}/master.md\` (esp. §4 fact ledger) and these lens summaries, extract 8-12 of the most impactful FACTUAL claims to verify (specific number/date/causal/named-entity action — skip opinion). Prioritize claims that anchor a section, would surprise if wrong, or rest on a single source.
Summaries: ${JSON.stringify(research.map(r => ({ lens: r.lens, keyFindings: r.keyFindings, bestDataPoint: r.bestDataPoint })))}
Return JSON per the claims schema.

${STRUCT_REMINDER}`, { label: 'claims', phase: 'Verify (adversarial)', schema: CLAIMS_SCHEMA })
log(`claims to verify: ${claims.claims.length}`)

const verifications = (await parallel(claims.claims.map(c => () =>
  agent(`**Adversarially verify — TRY TO REFUTE:** "${c.text}" (lens ${c.originatingLens}; matters: ${c.whyImportant})
Default to "refuted" if no strong INDEPENDENT support. ${SEARCH_TOOLKIT}
Search skeptical framings ("<subject> debunked/criticism/wrong/evidence against"); find the PRIMARY data (not the article quoting it); prefer Tier 1-2 corroboration. If no independent confirm in 3-4 searches → "unverifiable"/"refuted", not "confirmed".
Verdicts: confirmed (2+ independent Tier 1-2, no credible counter) | partially-confirmed (right w/ caveats) | refuted | unverifiable.
Return JSON per the verify schema (supporting/counter = URL arrays; nuance = what's oversimplified; rewriteSuggestion = what to say instead).

${STRUCT_REMINDER}`, { label: `verify:${c.id}`, phase: 'Verify (adversarial)', schema: VERIFY_SCHEMA })
))).filter(Boolean)
const verdicts = verifications.reduce((a, v) => { a[v.verdict] = (a[v.verdict] || 0) + 1; return a }, {})
log(`verdicts: ${JSON.stringify(verdicts)}`)

await agent(`Write \`${folder}/research/verification.md\`: a summary table (Claim | Verdict | Confidence), a "Headline takeaways for the writer" block (the debunked/contaminated figures to never assert; the strongest confirmed anchors), then per-claim detail (claim, supporting sources, counter sources, nuance, rewrite suggestion).
CLAIMS: ${JSON.stringify(claims.claims)}
VERIFICATIONS: ${JSON.stringify(verifications)}
Use Write. Confirm done.`, { label: 'save-verification', phase: 'Verify (adversarial)' })

// ---------- Phase 7: Fill gaps ----------

phase('Fill gaps')
const gaps = await agent(`Review \`${folder}/master.md\` + verification for what's missing.
${mustInclude.length ? `User REQUIRED these be covered — check each is actually in the research: ${mustInclude.join('; ')}.` : ''}
Find: a missing lens; a major unanswered question; unsurfaced counter-evidence; a missing stakeholder voice; a missing PRIMARY source (the actual study/filing/government series being cited); any missing official/consulting/comparable source class; any unmet "must include".
criticalGaps = MUST fill before writing (max 4). Empty is fine if solid — don't manufacture work. Return JSON per the gaps schema.

${STRUCT_REMINDER}`, { label: 'gaps-critic', phase: 'Fill gaps', schema: GAPS_SCHEMA })
log(`gaps: ${gaps.criticalGaps.length} critical`)

if (gaps.criticalGaps && gaps.criticalGaps.length) {
  await parallel(gaps.criticalGaps.slice(0, 4).map((g, i) => () =>
    agent(`Fill this gap: **${g}**. Topic: ${topic}. Core question: ${scope.coreQuestion}.
${SEARCH_TOOLKIT}
${SOURCE_PRIORITY}
Capture 3-5 sources (exact quotes, attribution, tier, sourceClass, data points). Append to \`${folder}/research/gaps.md\` (create if needed) under a header for this gap, AND fold the new quotes/facts into the right sections of \`${folder}/master.md\`. Confirm in 2 lines (no schema).`,
      { label: `gap:${i + 1}`, phase: 'Fill gaps' })
  ))
}

// ---------- Phase 8: Synthesize (schema-free) ----------

phase('Synthesize')
await agent(`Synthesize the dossier into the insight layer — the "butter to the recipe." Read \`${folder}/master.md\` + \`${folder}/research/verification.md\` (use only confirmed/partially-confirmed as factual; honor rewrite suggestions).

${USER_INTENT}

Write \`${folder}/research/synthesis.md\`:
# Synthesis: ${topic}
## The big insight (one concrete, defensible sentence)
## Narrative arc (2-4 sentences: lede idea → tension → where evidence lands)
## Convergent truths (confirmed across 3+ lenses or verification ≥0.7 — the load-bearing facts)
## Genuine disputes (both sides, strongest case each)
## Hidden patterns (what no single source said)
## Counterintuitive findings
## Weak areas / what we don't know
## Implications no one states
## Traps to avoid in prose (debunked/contaminated figures from verification — never assert as fact)

Be specific (names, numbers, dates). Schema-free: write the file, then return a 2-line confirmation (path + the big insight).`, { label: 'synthesize', phase: 'Synthesize' })

// ---------- Phase 9: Round-2 questions (schema-free; the human answers these next) ----------

phase('Round-2 questions')
const round2 = await agent(`The research is done. Propose a SECOND round of clarifying questions for the human — deeper and INFORMED BY THE EVIDENCE — so the writer's voice and POV come through before the final draft.

Read \`${folder}/research/synthesis.md\` and \`${folder}/master.md\`.

Round-1 answers were: ${JSON.stringify({ angle, audience, pov, clarifications, mustInclude }) }.

Generate **3-4 questions** that only make sense NOW that we have evidence — e.g.:
- Where to LAND now that the evidence is in (stay neutral, or take the side the evidence favors, or foreground a specific tension we found)?
- VOICE / tone (measured-analytical / narrative-literary / punchy-provocative / contrarian-sharp)?
- What to LEAD with (the human story / the killer stat / the contrarian twist / the historical parallel)?
- What to EMPHASIZE vs cut, and the headline direction?
Each question must reference an ACTUAL finding (name the tension/stat/quote it hinges on).

Write \`${folder}/research/round2-questions.md\` in this exact format so the orchestrator can turn each into a multiple-choice prompt:

# Round-2 questions: ${topic}
*Grounded in the dossier. The orchestrator asks these, then runs dj-write with the answers.*

## Q1. <header (≤6 words)>
<the question, naming the finding it hinges on>
- **<option label>** — <what choosing this means>
- **<option label>** — <...>
- **<option label>** — <...>

## Q2. ...
(3-4 total)

## Suggested default answers (if the human says "you decide")
- Q1: <the evidence-led default + one-line why>
- Q2: ...

Schema-free: write the file, then return the full questions text as your final message.`, { label: 'round2-questions', phase: 'Round-2 questions' })

log(`research stage complete → ${folder} | round2-questions.md ready`)

return {
  stage: 'research',
  folder, slug, topic,
  audience, povRound1: pov || null,
  counts: { lenses: research.length, sources: master.sourcesProcessed, quotes: master.quotesCaptured, dataPoints: master.dataPoints },
  sourceClassCoverage: master.sourceClassCoverage || {},
  verdicts,
  questionsFile: `${folder}/research/round2-questions.md`,
  round2QuestionsText: round2,
  next: `Read ${folder}/research/round2-questions.md, ask the human (AskUserQuestion), then run dj-write with srcFolder="${folder}".`,
}
