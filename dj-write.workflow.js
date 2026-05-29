// SPDX-License-Identifier: Apache-2.0
// Copyright 2026 INFINITIGRID TECHNOLOGIES (OPC) PRIVATE LIMITED. Created by Puneet Vishnawat.
//
// Digital Journalist — WRITE STAGE (v3, Stage 2 of 2). Schema-FREE.
//
// Turns an existing research dossier into the finished deliverables, applying the human's
// Round-2 answers (voice, where-to-land POV, what-to-lead-with, emphasis). Reads master.md
// AND the individual research/*.md lens files (not master alone) + verification.md + synthesis.md.
//
// Unifies the old finisher (outFolder == srcFolder) and spinoff (outFolder != srcFolder):
//   - Finish an aborted/checkpointed run: srcFolder == outFolder.
//   - Spin a new angle off the same research: outFolder != srcFolder (research reused, not copied).
//
// Schema-free by design: every agent writes files and returns a short text confirmation, so it
// cannot hit the "completed without calling StructuredOutput" failure.
//
// Invoke:
//   Workflow({ scriptPath: ".../dj-write.workflow.js", args: {
//     srcFolder: "articles/<slug>",        // REQUIRED — where the research lives
//     outFolder: "articles/<slug-or-new>", // default = srcFolder
//     topic, angle, audience,
//     stance:    "neutral referee" | "argue X, steelman counters" | ...,   // Round-2: where to land
//     voice:     "measured-analytical" | "narrative-literary" | "punchy-provocative" | "contrarian-sharp",
//     leadWith:  "the human story" | "the killer stat" | "the contrarian twist" | "the historical parallel",
//     emphasize: ["..."], deemphasize: ["..."], avoidClaims: ["..."],
//     companionNote, timestamp
//   }})

export const meta = {
  name: 'dj-write',
  description: 'WRITE stage (schema-free): turns an existing dossier (master.md + every research/*.md lens file + verification.md + synthesis.md) into a finished article + sources + 10 SEO titles + meta, applying the human Round-2 answers (voice, where-to-land POV, lead, emphasis). Enforces credibility-ordered citations and an authority-ordered quote hierarchy. Finishes a checkpointed run (out==src) or spins a new angle (out!=src). Updates memory.',
  whenToUse: 'Stage 2 of the digital-journalist, after research + Round-2 questions. Also the recovery path for an aborted run and the spinoff path for a new angle off the same research.',
  phases: [
    { title: 'Writer brief' },
    { title: 'Write' },
    { title: 'Headlines (SEO)' },
    { title: 'Meta + memory' },
  ],
}

let input
if (typeof args === 'string') {
  const t = args.trim()
  input = (t.startsWith('{') && t.endsWith('}')) ? (() => { try { return JSON.parse(t) } catch (e) { return {} } })() : {}
} else { input = args || {} }

const srcFolder = input.srcFolder
if (!srcFolder) throw new Error('dj-write requires args.srcFolder')
const outFolder = input.outFolder || srcFolder
const isSpinoff = outFolder !== srcFolder
const topic = input.topic || 'Untitled'
const angle = input.angle || ''
const audience = input.audience || 'general business reader (Atlantic/Bloomberg style — smart non-specialist)'
const stance = input.stance || 'neutral referee — no house thesis; weigh both sides; let the evidence decide'
const voice = input.voice || 'measured-analytical (Atlantic/Bloomberg)'
const leadWith = input.leadWith || 'the strongest evidence-grounded hook'
const emphasize = Array.isArray(input.emphasize) ? input.emphasize : []
const deemphasize = Array.isArray(input.deemphasize) ? input.deemphasize : []
const avoidClaims = Array.isArray(input.avoidClaims) ? input.avoidClaims : []
const companionNote = input.companionNote || ''
const timestamp = input.timestamp || 'unspecified'

const LENS_FILES = ['mainstream', 'contrarian', 'data', 'stakeholders', 'expert', 'followthemoney', 'historical', 'comparative', 'international']
  .map(n => `${srcFolder}/research/${n}.md`).join(', ')

const ROUND2 = `
**Round-2 direction from the human (informed by the evidence):**
- Where to land (stance): ${stance}
- Voice / tone: ${voice}
- Lead with: ${leadWith}
- Emphasize: ${emphasize.length ? emphasize.join('; ') : '(use editorial judgment)'}
- De-emphasize / cut: ${deemphasize.length ? deemphasize.join('; ') : '(none)'}
- Avoid these claims/framings: ${avoidClaims.length ? avoidClaims.join('; ') : '(none beyond the verification traps)'}
`.trim()

const CREDIBILITY_POLICY = `
**Citation & quote hierarchy (enforce):**
- **Cite most-credible-first.** Lead every claim with the strongest available source: government/official & primary data and peer-reviewed work first; then market-research/consulting (Gartner, McKinsey, BCG, IDC…) and established journalism; then everything else. Cite a blog / Substack / social post ONLY when no stronger source exists OR the author is themselves the authority — and never let a Tier 4-5 source carry a load-bearing fact.
- **Quote most-authoritative-first.** Prefer quotes from a named executive of a major organization, a government official, a frequently-cited academic, or the named author of the primary study — over analysts, over anonymous/"regular" individuals. Use a lived-experience quote only for color, clearly framed as one person's anecdote, never as evidence for a general claim.
- When the corpus forces reliance on a weaker source, say so in-text ("according to one widely-shared but unverified account…").
`.trim()

log(`[write] ${isSpinoff ? 'SPINOFF' : 'FINISH'} ${topic}`)
log(`  src=${srcFolder} → out=${outFolder} | voice=${voice} | land=${stance}`)

// ---------- Phase 1: Writer brief (refine synthesis with Round-2 direction) ----------

phase('Writer brief')
await agent(`Prepare the writer's brief for a NEW final draft, applying the human's Round-2 direction. No new web research.

**Topic:** ${topic}${angle ? `  |  **Angle:** ${angle}` : ''}
${ROUND2}
${companionNote ? `**Companion:** ${companionNote} — own a distinct spine; minimal overlap.` : ''}

**Read (do NOT rely on master.md alone):**
- \`profile/writing-style.md\` and \`profile/writer.md\` IF they exist (the user's house voice + who they write for) — the draft should sound like them. The Round-2 \`voice\` above overrides the house voice only where they conflict.
- \`${srcFolder}/research/synthesis.md\` (the insight layer + the "traps to avoid")
- \`${srcFolder}/master.md\` (the map)
- the individual lens files (the territory — exact quotes, attribution, data the master compresses): ${LENS_FILES}
- \`${srcFolder}/research/verification.md\` (only confirmed/partially-confirmed are factual; honor rewrite suggestions)

${isSpinoff ? `From project root: \`mkdir -p ${outFolder}/research\`.\n` : ''}Write \`${outFolder}/research/writer-brief.md\`: the chosen LANDING (per the stance above), the LEDE concept (per "lead with"), the section order, which 5-8 quotes and which 8-12 data points to use (chosen per the credibility & quote hierarchy below — most authoritative first), the contrarian section's strongest form, and the explicit list of figures to NEVER assert (from verification traps).

${CREDIBILITY_POLICY}

Schema-free: write the file, return a 2-line confirmation (path + the chosen landing).`, { label: 'writer-brief', phase: 'Writer brief' })

// ---------- Phase 2: Write article + sources ----------

phase('Write')
await agent(`Write the final investigative article on **"${topic}"** for: ${audience}. Top-desk standard (NYT / WSJ / Bloomberg).

${ROUND2}
${companionNote ? `**Companion:** ${companionNote} — distinct spine; cost/other-angle is at most a supporting thread.` : ''}

**Read first, in order:** \`memory/writing-standards.md\` (house style + the Source/Quote hierarchy), \`profile/writing-style.md\` + \`profile/writer.md\` if present (the user's voice — emulate it; the \`voice\` arg overrides on conflict), \`${outFolder}/research/writer-brief.md\`, \`${srcFolder}/master.md\`, the lens files (${LENS_FILES}) for exact quotes/attribution, and \`${srcFolder}/research/verification.md\`.

**Requirements:**
1. 1,800-2,800 words; every paragraph earns its place.
2. Structure per the brief: lede (per "lead with") → nut graf → 3-5 evidence sections w/ subheads → steelmanned contrarian turn → implications → "What we don't know" → kicker (strong, not a summary).
3. Inline numbered citations [1], [2]… on every factual claim. Quotes as blockquotes with \`— Name, Title, Publication, YYYY-MM-DD\`.
4. Voice = ${voice}. Contextualize every number. Active voice. No clichés / AI-slop tells.
5. Use ONLY confirmed/partially-confirmed claims as fact; apply rewrite suggestions; never assert the debunked figures (except briefly as a cautionary example).
6. Honor the stance ("${stance}") — but keep the contrarian case fair and strong.

${CREDIBILITY_POLICY}

Write \`${outFolder}/article.md\`: H1 headline + italic one-line subhead + body with inline [n] + "## Sources" ([n] Title — Author, Publication, Date. URL).
Then write \`${outFolder}/sources.md\`: deduped, numbered, **grouped by tier (1 first)**, each noting sourceClass + lens(es).

Schema-free: write both files, return 3 lines (word count, citation count, working headline).`, { label: 'write-article', phase: 'Write' })

// ---------- Phase 3: SEO headlines ----------

phase('Headlines (SEO)')
await agent(`Suggest **10 catchy, SEO-optimized headlines** for \`${outFolder}/article.md\`.
Read the article + \`${outFolder}/sources.md\` (differentiate from every source headline) and \`memory/writing-standards.md\` §9.
Each: match real search intent, front-load the primary keyword, be specific, differ from sources, earn the click honestly (no clickbait). Mix ~4 SEO / ~3 editorial / ~3 provocative. Match the chosen voice (${voice}).
Write \`${outFolder}/titles.md\`: a **Recommended:** line, then the 3 categories, each title with char count, primary keyword, search intent, and a one-line why. End with "*All 10 checked against sources.md.*"
Schema-free: write the file, return the recommended title.`, { label: 'seo-titles', phase: 'Headlines (SEO)' })

// ---------- Phase 4: Meta + memory (+ pointer if spinoff) ----------

phase('Meta + memory')
await agent(`Finalize metadata + memory. Project root; Bash + Read + Write/Edit.

**Counts (Bash):** \`wc -w ${outFolder}/article.md\`; citations \`grep -oE '\\[[0-9]+\\]' ${outFolder}/article.md | sort -u | wc -l\`; recommended title from the "Recommended:" line of ${outFolder}/titles.md.

**Write \`${outFolder}/meta.json\`:** topic, slug (basename of ${outFolder}), angle, audience, stance ("${stance}"), voice ("${voice}"), leadWith ("${leadWith}"), timestamp ("${timestamp}"), counts {articleWords, citations}, recommendedTitle${isSpinoff ? `, sharedResearch ("${srcFolder}" — reused, not re-run), companionArticle ("${srcFolder}/article.md")` : ''}.
${isSpinoff ? `**Write \`${outFolder}/README.md\`:** one short paragraph — this article reuses the dossier in \`${srcFolder}/\` (master.md + research/*.md + verification.md); only the writer-brief, article, titles, and sources here are new.\n` : ''}
**Update memory (Read + Edit/append):**
- \`memory/learnings.md\` — under "## Run log", a "### Run: <out-slug> (${timestamp})" note: topic, stance/voice chosen, and any durable craft lesson (e.g., what the two-round questions changed about the draft).
- \`memory/source-quality.md\` — if clear from the dossier, add 1-2 reliable/unreliable domain notes (dedupe).
- \`memory/writing-standards.md\` — if a voice/structure choice clearly worked, append one note under "## Run-learned writing notes" (dedupe).

Return a confirmation listing every file written/updated.`, { label: 'meta-memory', phase: 'Meta + memory' })

log(`write stage complete → ${outFolder}/article.md`)
return { stage: 'write', srcFolder, outFolder, topic, mode: isSpinoff ? 'spinoff' : 'finish', status: 'done' }
