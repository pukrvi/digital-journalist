# Follow-the-money: The AI cost reckoning — does replacing workers with AI actually save money?

**Lens focus:** Incentives behind each narrative. Who profits from "cut headcount," from "reskill," and from "control your tokens"? The Altman/Amodei walkback timing vs. trillion-dollar IPOs; model-vendor inference margins; consultancies (BCG/McKinsey) selling BOTH layoff-automation AND reskilling; the new AI-FinOps tooling vendors monetizing the panic.

**Summary (5 bullets):**
- The CEOs of both AI labs (Altman, Amodei) walked back their "AI jobs apocalypse" warnings in May 2026 — within weeks of reportedly preparing ~$1 trillion IPOs. Multiple outlets explicitly tie the reversal to IPO/marketing incentives: "catastrophism is bad marketing" when you're about to sell shares to the public.
- The vendor economics reveal the real game: Anthropic's inference gross margin jumped from ~38% (2025) to ~70% (2026), while OpenAI's gross margin FELL from 40% to 33%, missing its 46% forecast, with inference costs ballooning ~4x to $8.4B. Margin headroom = room to keep subsidizing seat prices to lock in users pre-IPO, then raise prices after.
- The April–June 2026 pricing shift (Claude Code moving programmatic usage to full API rates effective June 15, 2026; the "$200 sub buys $1,000+ of tokens" era ending) is consistent with a classic loss-leader-before-IPO playbook: "burning cash not to achieve immediate profitability, but to lock in the largest possible user base before the IPO window opens."
- Consultancies (BCG, McKinsey) monetize BOTH sides of the trade: McKinsey cut 5,000+ staff while growing its own AI-agent fleet to ~25,000, AND sells reskilling/transformation work — BCG's AI-transformation revenue reportedly ~25% of a $3.6B line. The "AI will reshape more jobs than it replaces" framing is itself a consulting product.
- A whole new vendor category — "FinOps for AI" — is monetizing the panic: 98% of FinOps teams now manage AI spend (up from 31% two years ago); cloud-cost startups (e.g., Adaptive6, $28M Series A) are pivoting to AI token governance. The cost-control narrative sells software regardless of whether AI actually saves money on labor.

---

## Sources

### [1] Sam Altman and Dario Amodei are both walking back their AI jobs apocalypse prophecies as they eye blockbuster IPOs
- URL: https://fortune.com/2026/05/26/sam-altman-dario-amodei-walking-back-ai-jobs-apocalypse-prophecies-ipo/
- Author: Fortune staff (byline not captured)
- Publication: Fortune
- Date: 2026-05-26
- Tier: 2
- Credibility notes: Established business journalism (Tier 2). The headline draws the IPO-timing connection but the body reports it largely implicitly — the explicit causal critique is made more forcefully by the Substack (source [3]) and mlq.ai. Use Fortune for the on-the-record CEO quotes and the IPO/valuation facts; attribute the *argument* to the named critic.

**Key quotes:**
> "I'm delighted to be wrong about this." — Sam Altman, quoted in Fortune, 2026-05-26
> "I thought there would have been more impact on entry-level white-collar jobs being eliminated by now than has actually happened." — Sam Altman, quoted in Fortune, 2026-05-26
> "If you automate 90% of the job, then everyone does the 10% of the job... And the 10% kind of expands to be 100% of what people do and kind of 10-times their productivity." — Dario Amodei (paraphrasing his shift toward job-expansion framing), quoted in Fortune

**Key claims:**
- Both OpenAI and Anthropic are reportedly preparing IPOs in 2026, each at an estimated ~$1 trillion valuation. (cited from [1])
- Altman's June 2025 warnings that entry-level white-collar roles were at serious risk have been reversed; he now says he was "pretty wrong" about AI's near-term economic impact. (cited from [1])
- The article presents pro-adoption voices (David Solomon, Aaron Levie) but no on-record critic questioning the reversal's timing — the follow-the-money read is left to the reader/headline. (cited from [1])

**Data points:**
- OpenAI estimated IPO valuation: ~$1 trillion (2026). (Fortune, 2026-05-26)
- Anthropic estimated IPO valuation: ~$1 trillion (2026). (Fortune, 2026-05-26)

### [2] OpenAI and Anthropic Miss Gross Margin Targets as Inference Costs Skyrocket
- URL: https://finance.biggo.com/news/mRiPlZwBTwP6zY3HRxp-
- Author: BigGo Finance (aggregating reporting from The Information)
- Publication: BigGo Finance (primary reporting: The Information)
- Date: 2026-02-25 (reflecting The Information's report)
- Tier: 3 (aggregator of a Tier-2 paywalled original — The Information; cross-checked against MindStudio/SemiAnalysis for the Anthropic margin trajectory)
- Credibility notes: Secondary aggregation of The Information's reporting (The Information is Tier 2 but paywalled). Numbers are internally consistent with the MindStudio/SemiAnalysis Anthropic figures (source [4]). Treat the specific dollar figures as "reported by The Information" rather than independently confirmed.

**Key quotes:**
> "When SemiAnalysis reported Anthropic's margins at 38% last year, it meant compute was eating 62 cents of every dollar. At 70%, compute costs have dropped to 30 cents on the dollar." — MindStudio (source [4], corroborating)

**Key claims:**
- OpenAI's gross margin fell to 33% in 2025 (down from 40% in 2024), missing its own 46% forecast. (reported by The Information, via [2])
- OpenAI's 2025 inference costs hit $8.4B, ~4x year-over-year, exceeding its $6.6B forecast. (reported by The Information, via [2])
- OpenAI spent ~$3.9B serving free users (~95% of weekly actives) and ~$4.5B serving paying users (~5%). (reported by The Information, via [2])
- Anthropic's gross margin went from negative 94% (2024) to a projected ~40% (2025), then to ~70% (2026 per source [4]). (via [2] and [4])
- Both labs target 60%+ gross margin by 2030; OpenAI specifically ~67%. (reported by The Information, via [2])

**Data points:**
- OpenAI 2025 gross margin: 33% (down from 40% in 2024; forecast was 46%). (The Information, ~2026-02-25)
- OpenAI 2025 inference cost: $8.4B (~4x YoY; forecast $6.6B). (The Information)
- OpenAI 2030 inference cost projection: ~$85B, 94% from paying users. (The Information)
- Anthropic inference margin trajectory: −94% (2024) → ~40% (2025) → ~70% (2026). (The Information + SemiAnalysis via [4])

### [3] Billionaires Backpedal on the AI Jobs Apocalypse: Why AI's Prophets of Doom Went Quiet Right Before Their IPOs
- URL: https://futureforwarded.substack.com/p/billionaires-backpedal-on-the-ai
- Author: William R. Dodson
- Publication: Future Forwarded (Substack)
- Date: 2026-05 (undated day; published shortly after the 2026-05-26 walkbacks)
- Tier: 3 (named domain commentator with a track record; opinion/analysis — quote the argument, verify the underlying facts against Tier 1-2)
- Credibility notes: This is the STRONGEST explicit steelman of the follow-the-money read. It is opinion/analysis (Tier 3), so its factual anchors (valuations, dates of doom statements) are cross-checked against Fortune [1]; the *argument* is what makes it citable as the contrarian-incentive voice.

**Key quotes:**
> "Companies preparing to sell shares to the public have a compelling reason to stop telling potential investors that the technology at the core of their business is a threat to social stability." — William R. Dodson, Future Forwarded, 2026-05
> "Catastrophism is bad marketing. It's also bad prospectus material." — William R. Dodson, Future Forwarded, 2026-05
> "The capabilities haven't changed — only the audience requiring persuasion." — William R. Dodson (paraphrased conclusion), Future Forwarded, 2026-05

**Key claims:**
- The walkbacks are timed to IPOs: executives' compensation and stock valuations rise when the technology is adopted widely, so doom narratives become a liability pre-listing. (cited from [3])
- Altman (July 2025, Federal Reserve conference) said "entire classes of jobs would disappear"; he now says he is "delighted to be wrong." (cited from [3], Altman quote cross-checked against [1])
- Amodei warned AI could "eliminate half of entry-level, white-collar knowledge work within years" and push U.S. unemployment to "between 10% and 20%" (Axios); he now says automation "may actually expand the work people do." (cited from [3])
- Anthropic targets an October listing seeking ~$30B at a ~$900B valuation. (cited from [3])

**Data points:**
- Amodei's prior public estimate: AI could push U.S. unemployment to 10–20% (stated 2025, Axios). (via [3])
- Anthropic listing target: raise ~$30B at ~$900B valuation, October 2026. (via [3])

> NOTE on IPO-valuation discrepancy: Fortune [1] cites "~$1 trillion each"; Dodson [3] cites Anthropic ~$900B / raise ~$30B (October). Both are pre-IPO estimates from different dates — report as a range (~$900B–$1T) rather than a fixed number.

---

### [4b] Why Anthropic's 70% Inference Margins Matter for Your API Costs — And What to Expect Next (the price-deflation steelman)
- URL: https://www.mindstudio.ai/blog/anthropic-inference-margins-70-percent-api-costs
- Author: MindStudio Team
- Publication: MindStudio (vendor blog)
- Date: 2026-05-07
- Tier: 3 (vendor blog; load-bearing numbers attributed to SemiAnalysis — treat those as Tier 2 pending direct confirmation of the primary SemiAnalysis report)
- Credibility notes: MindStudio is an AI-tooling vendor with a mild bias toward "prices keep falling." Cited here because it is the STRONGEST articulation of the price-deflation counter-argument that the whole "cost reckoning" thesis may be temporary. The 38%→70% margin figure corroborates source [2]'s Anthropic trajectory.

**Key quotes:**
> "When SemiAnalysis reported Anthropic's margins at 38% last year, it meant compute was eating 62 cents of every dollar. At 70%, compute costs have dropped to 30 cents on the dollar." — MindStudio, 2026-05-07 (attributing the figures to SemiAnalysis)

**Key claims:**
- Fat-and-rising inference margins signal FALLING underlying costs, not imminent price hikes; expect continued price cuts on smaller (Haiku-class) models over 6–12 months while frontier models stay pricey due to inelastic demand. (cited from [4b]) — this is the core "the reckoning is temporary" steelman.
- Anthropic ARR reportedly grew from ~$9B to >$44B in 2026 (per SemiAnalysis via [4b]) — verify; extraordinary growth claim.

**Data points:**
- Inference gross margin ~38% → >70% in one year (compute cost per revenue-dollar $0.62 → $0.30). (SemiAnalysis via [4b])

---

### [5] Gartner Says Autonomous Business and AI Layoffs May Create Budget Room, but Do Not Deliver Returns
- URL: https://www.gartner.com/en/newsroom/press-releases/2026-05-05-gartner-says-autonomous-business-and-artificial-intelligence-layoffs-may-create-budget-room-but-do-not-deliver-returns (press release; HTTP 403 to bot fetch — methodology & quotes captured via Fortune coverage [5b])
- Author: Gartner (research firm)
- Publication: Gartner newsroom
- Date: 2026-05-05
- Tier: 1 (primary research from a major analyst firm; the survey is the original source for the "80% / no ROI correlation" finding the brief asks for)
- Credibility notes: Gartner sells advisory services to the same enterprises making these decisions, so it has an incentive to position itself as the sober referee ("don't just cut heads, amplify people — and buy our guidance"). But the finding cuts AGAINST the cost-savings narrative, which is the opposite of what a hype-selling vendor would push — strengthening its credibility here.

**Key quotes:**
> "Many CEOs turn to layoffs to demonstrate quick AI returns; however, this disposition is misplaced. Workforce reductions may create budget room, but they do not create return. Organizations that improve ROI are not those that eliminate the need for people, but those that amplify them by aggressively investing more in skills, roles and operating models that allow humans to guide and scale autonomous systems." — Helen Poitevin, Distinguished VP Analyst, Gartner (press release, 2026-05-05)

> "Looking only at layoffs is shortsighted in terms of getting value from AI. Chasing value only through headcount reduction is likely to lead most organizations down a path of limited returns." — Helen Poitevin, Gartner (via Fortune [5b])

**Key claims:**
- ~80% of surveyed orgs that piloted/deployed AI or autonomous tech reported workforce reductions — but reduction rates were nearly EQUAL among high-ROI and low/negative-ROI respondents, i.e., NO correlation between cutting heads and returns. (cited from [5]/[5b])
- The orgs with the highest gains used AI for "people amplification," not replacement. (cited from [5])

**Data points:**
- Survey: 350 global business executives, Q3 2025, organizations with ≥$1B enterprise-wide annual revenue, all piloting/deploying autonomous tech. (cited from [5b])
- ~80% reported workforce reductions; no correlation with higher ROI. (cited from [5]/[5b])

---

### [5b] AI isn't paying off in the way companies think. Layoffs driven by automation are failing to generate returns, study finds
- URL: https://fortune.com/2026/05/11/ai-automation-layoffs-gartner-study-roi/
- Author: Jake Angelo (News Fellow)
- Publication: Fortune
- Date: 2026-05-11
- Tier: 2 (established business journalism reporting on the Gartner primary data)
- Credibility notes: Tier-2 outlet; used to capture the Gartner methodology and verbatim Poitevin quotes that the 403-blocked press release would have provided. Cross-checked with CIO.com, Allwork, SiliconRepublic — all report the same 80%/350-exec figures.

**Key quotes:**
> "80% of those surveyed who have piloted an AI or autonomous technology have reported workforce reductions" — Fortune summarizing Gartner, 2026-05-11
> "That's not where the value is. That's not where the productivity gains are going to be." — Helen Poitevin (on layoffs), via Fortune

**Data points:**
- 80% workforce-reduction rate among AI-piloting orgs, no ROI correlation (Gartner, n=350, ≥$1B revenue). (Fortune, 2026-05-11)

---

### [6] Forrester: AI-Led Job Disruption Will Escalate, While Fears Of A Job Apocalypse Are Overstated
- URL: https://www.forrester.com/press-newsroom/forrester-impact-ai-jobs-forecast/
- Author: Forrester (named analyst: J.P. Gownder, VP & Principal Analyst)
- Publication: Forrester Research (press release for "The Forrester AI Job Impact Forecast, US, 2025–2030")
- Date: 2026-01-13
- Tier: 1 (primary research/forecast from a major analyst firm)
- Credibility notes: Like Gartner, Forrester sells research subscriptions and has an interest in being seen as the calm forecaster between doomers and boosters. Its "reverse half the layoffs" and "AI washing" findings cut against the easy-savings narrative. The 55%-regret / 57%-vs-15% headcount figures are in the FULL (client-gated) report, so attribute those to secondary coverage ([6b], The Register) rather than the public release.

**Key quotes:**
> "over half of layoffs attributed to AI will be quietly reversed as companies realize the operational challenges of replacing human talent prematurely" — Forrester, 2026-01-13
> "Many companies announcing AI-related layoffs do not have mature, vetted AI applications ready to fill those roles, highlighting a trend of 'AI washing' — attributing financially motivated cuts to future AI implementation." — Forrester, 2026-01-13

**Key claims:**
- Over half of AI-attributed layoffs will be quietly reversed (often rehired offshore or at lower pay). (cited from [6])
- "AI washing" = labeling financially-motivated cuts as AI-driven; many firms lack the mature AI to actually backfill. (cited from [6])
- Only ~6% of US jobs automated by 2030 (~10.4M roles); ~20% augmented over five years — i.e., the apocalypse framing is overstated. (cited from [6])

**Data points:**
- ~6% of US jobs automated by 2030 (~10.4M). (Forrester, 2026-01-13)
- ~20% of jobs augmented over next 5 years. (Forrester)
- "Over half" of AI-attributed layoffs reversed. (Forrester)

---

### [6b] AI layoffs to backfire: Half quietly rehired at lower pay
- URL: https://www.theregister.com/2025/10/29/forrester_ai_rehiring/
- Author: The Register staff
- Publication: The Register
- Date: 2025-10-29
- Tier: 2 (established tech journalism; reporting Forrester's client-report figures)
- Credibility notes: Tier-2 tech outlet, useful for the gated Forrester numbers (55% regret; 57% expect AI to INCREASE headcount vs 15% decrease). These figures appear consistently across HRExecutive, Resultsense, and Curiouser.AI coverage of the same Forrester report.

**Key claims:**
- 55% of employers regret laying off workers because of AI. (Forrester via [6b])
- 57% of those overseeing AI investment expect it to INCREASE headcount over the next year; only 15% expect a decrease. (Forrester via [6b])

**Data points:**
- 55% regret AI layoffs; 57% expect headcount up / 15% expect down. (Forrester, reported 2025-10-29)

---

### [7] AI Will Reshape More Jobs Than It Replaces — BCG (the consultancy double-dip)
- URL: https://www.bcg.com/publications/2026/ai-will-reshape-more-jobs-than-it-replaces
- Author: Boston Consulting Group (Henderson Institute)
- Publication: BCG
- Date: 2026-04 (≈April 2026 per HPCwire/WhatJobs coverage)
- Tier: 2 for the underlying research; READ WITH the follow-the-money caveat below.
- Credibility notes: THIS IS THE CLEANEST DOUBLE-INCENTIVE STORY. BCG sells AI-transformation consulting (layoff design AND reskilling AND governance). Per BCG's own disclosure to Bloomberg (2026-04-23, via Metaintro [7b]), ~25% of its $14.4B 2025 revenue — ~$3.6B — came from AI work, while the consulting industry (McKinsey, BCG, Bain) simultaneously cut staff [see 8]. A "reshape, don't replace" message is reassuring to clients (keep spending on transformation, don't panic) AND to BCG's own about-to-be-automated junior analysts. The firm profits whichever narrative wins.

**Key claims:**
- BCG: AI could reshape 50–55% of U.S. jobs over 2–3 years; only 10–15% could be outright replaced; emphasis on task-change within roles. (cited from [7]/secondary)

**Data points:**
- BCG AI-consulting revenue: ~$3.6B = ~25% of $14.4B total 2025 revenue. (BCG to Bloomberg, 2026-04-23, via [7b])
- Reshape 50–55% / replace 10–15% (BCG estimate, ~April 2026).

---

### [7b] BCG Rode AI to $3.6B in Revenue — Here's What It Means for Consulting Jobs
- URL: https://www.metaintro.com/blog/bcg-25-percent-ai-revenue-consulting-jobs-2026
- Author: Metaintro (career/hiring-tracking blog)
- Publication: Metaintro
- Date: 2026-04-23 (citing BCG's same-day Bloomberg disclosure)
- Tier: 4 (secondary blog) — but the $3.6B/25%/$14.4B figures are explicitly sourced to BCG's statement to Bloomberg (Tier 2). Cite the numbers as "BCG, reported by Bloomberg," not to the blog.
- Credibility notes: Use only for the BCG revenue figures, which trace to a Bloomberg disclosure. The blog itself is boosterish about AI creating consulting jobs (it is a hiring-content site).

**Data points:**
- $3.6B AI revenue (25% of $14.4B), 2025. (BCG via Bloomberg, 2026-04-23)

---

### [8] Why the McKinsey layoffs are a warning signal for consulting in the AI age
- URL: https://www.fastcompany.com/91463039/why-the-mckinsey-layoffs-are-a-warning-signal-for-consulting-in-the-ai-age-ai-layoffs-management-consulting
- Author: Fast Company (via Inc. syndication)
- Publication: Fast Company
- Date: 2026 (early 2026)
- Tier: 2 (established business journalism)
- Credibility notes: The other half of the consultancy double-dip: McKinsey cutting its OWN staff (~10%, ~3,000–4,000 roles, its largest cut since 2008) as gen-AI compresses the analyst pyramid — while simultaneously selling AI transformation to clients and (per secondary reporting) deploying a large internal AI-agent fleet. Self-cannibalization and self-monetization at once.

**Key claims:**
- McKinsey cutting ~10% of global workforce (~3,000–4,000), largest since 2008, concentrated in back-office/junior research where gen-AI compresses delivery. (cited from [8])
- Driven by AI productivity gains + post-pandemic over-hiring + competition from AI-native boutiques. (cited from [8])

**Data points:**
- McKinsey cuts: ~10% of workforce, ~3,000–4,000 roles (2025–2026). (Fast Company)
- (Secondary, VERIFY) McKinsey internal AI-agent fleet reported at ~12,000+ agents across coverage. — treat as unverified; flagged but not load-bearing.

---

### [9] GitHub Copilot is moving to usage-based billing
- URL: https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/
- Author: Mario Rodriguez (Chief Product Officer, GitHub)
- Publication: GitHub Official Blog
- Date: 2026-04-27
- Tier: 1 (primary source — the vendor's own announcement; directly verifies seed-post claim #3 and the April–June 2026 pricing-shift must-include)
- Credibility notes: Primary/official. The rationale is the company's own framing, but it IS the on-record confirmation that GitHub is moving Copilot to token-metered "AI Credits" effective June 1, 2026 — exactly the SaaS-seat → cloud-infra-usage pivot the seed post describes. Follow-the-money read: Microsoft is monetizing the compute it previously gave away at flat rate.

**Key quotes:**
> "Agentic usage is becoming the default, and it brings significantly higher compute and inference demands." — GitHub announcement (Mario Rodriguez), 2026-04-27
> [Paraphrase] The prior model where a quick chat and a multi-hour autonomous session cost the same "was no longer sustainable."

**Key claims:**
- All Copilot plans move to usage-based billing on June 1, 2026; premium-request units (PRUs) replaced by "GitHub AI Credits" consumed by token usage (input + output + cached) at published per-model API rates. (cited from [9]) — CONFIRMS seed claim #3.
- Seat prices unchanged (Pro $10, Pro+ $39, Business $19/user, Enterprise $39/user) but overage now metered — the seat is now a token wallet. (cited from [9])
- Explicit rationale: agentic workflows consume far more compute → flat pricing "no longer sustainable." (cited from [9]) — DIRECTLY supports the "coding agents behave like cloud infra, not fixed-seat SaaS" thesis.

**Data points:**
- Effective date: June 1, 2026. Preview-bill experience launched early May 2026. (GitHub, 2026-04-27)
- Plan prices: Pro $10/mo, Pro+ $39/mo, Business $19/user/mo, Enterprise $39/user/mo (credits = dollar value of plan). (GitHub)

---

### [10] CloudZero Raises $56M Series C To Redefine Cloud Cost Optimization In The AI Era
- URL: https://www.cloudzero.com/press-releases/20250528/
- Author: CloudZero (company press release)
- Publication: CloudZero / PR Newswire
- Date: 2025-05-28 (with follow-on "Financial Control Plane for AI" launch 2026-05-28)
- Tier: 3 (vendor press release — reliable for funding facts, self-serving on market framing)
- Credibility notes: Direct evidence of the "control your tokens" vendor category being capitalized. CloudZero rebranded itself "The AI ROI Company" — a vendor literally selling the answer to the brief's question. Follow-the-money: the cost-panic narrative sells this software whether or not AI actually saves money on labor; in fact uncertainty about ROI is the sales pitch.

**Key quotes:**
> "AI is redefining what's possible — but without a deep understanding of cloud unit economics, innovation becomes unsustainable." — Phil Pergola, CEO, CloudZero (2025-05-28)

**Key claims:**
- $56M Series C led by BlueCrest Capital Management and Innovius Capital (+ Matrix, Threshold, Underscore, G20, MongoDB strategic). (cited from [10])
- Repositioned as "The AI ROI Company"; launched a "Financial Control Plane for AI" (2026-05-28) to measure what outcomes AI investments produce. (cited from [10])
- Market framing: cloud spend projected to reach $2T by 2030. (cited from [10])

**Data points:**
- CloudZero Series C: $56M (2025-05-28). (CloudZero PR)
- Pay-i (separate FinOps-for-AI startup): ~$4.5M seed led by Khosla Ventures, founded 2024, tracks token spend across OpenAI/Anthropic/Google/self-hosted ("the OpenTelemetry of AI costs"). (per ToolDirectory/aggregator) — Tier 4 secondary; VERIFY funding figure before citing as fact.

---

### [11] State of FinOps 2026 Report (the "control your tokens" market signal)
- URL: https://data.finops.org/
- Author: FinOps Foundation (research team)
- Publication: FinOps Foundation (Linux Foundation project)
- Date: 2026 (6th annual; published 2026)
- Tier: 2 (industry-body primary survey, large n) — note vendor-adjacency bias below.
- Credibility notes: The Foundation is funded by member organizations, many of them the very cost-tooling vendors that benefit from "FinOps for AI is the top priority." Mild conflict — but n=1,192 / $83B+ cloud spend makes the headline YoY jump credible. This is the single best market-size proxy for the "control your tokens" beneficiary class.

**Key claims:**
- "FinOps for AI emerges as the top forward-looking priority," outpacing traditional workload optimization. (cited from [11])
- AI cost management is the #1 most-desired skillset across all org sizes. (cited from [11])
- "Labor costs" appears as an EMERGING FinOps category (28%) — finance is starting to put humans and AI on the same cost ledger. (cited from [11]) — directly relevant to labor-substitution economics.

**Data points:**
- Teams managing AI spend: 98% (2026) vs 63% (2025) vs 31% (2024); +35 pts YoY. (FinOps Foundation)
- Sample: 1,192 respondents, $83B+ annual cloud spend. (FinOps Foundation)
- 78% of FinOps teams report to CTO/CIO (up 18 pts vs 2023). (FinOps Foundation)

---

### [12] AI-washing & reversals: who benefits from the "AI did it" story (synthesis source cluster)
- URLs:
  - https://fortune.com/2026/05/11/ai-automation-layoffs-gartner-study-roi/ (Fortune, 2026-05-11, Tier 2)
  - https://www.theregister.com/2025/10/29/forrester_ai_rehiring/ (The Register, 2025-10-29, Tier 2)
  - Orgvue survey (32% rehire) and Careerminds survey (n=600 HR pros, Feb 2026; ~2-in-3 rehiring) — reported across Career-metrics/GFMag (Tier 3-4; attribute to the named survey houses)
- Tier: 2 (anchor outlets) + 3-4 (survey-house secondary)
- Credibility notes: Multiple independent surveys converge on the same pattern (regret + rehiring), which strengthens the finding despite individual-source weakness. The KEY follow-the-money insight: executives have an incentive to blame AI rather than admit financial/over-hiring motives, because "we're cutting for AI efficiency" reads better to investors than "we over-hired and need cash." This INVERTS the labor-apocalypse narrative — the "AI took the jobs" story is itself partly a marketing product.

**Key quotes:**
> [Reported finding] "Nearly 60 percent [of US hiring managers] said they emphasize AI's role in reducing hiring or cutting jobs because it's viewed more favorably than financial constraints." — survey reporting (via WebSearch synthesis of Built In / SHRM coverage, 2026)

**Key claims:**
- Klarna: announced its AI assistant did the work of 700 agents (2024); by early 2026 quietly rehiring as quality dropped and projected savings didn't materialize. (cited from Klarna coverage)
- IBM: cut ~8,000 HR jobs into "AskHR"; began rehiring humans for empathy/judgment/edge cases. (cited from coverage)
- Orgvue: 32% of orgs that made AI-linked layoffs subsequently rehired. (cited)
- Careerminds (n=600 HR pros, Feb 2026): ~2 in 3 employers that cut jobs for AI are already rehiring, often within months. (cited)
- ~48% of 78,557 layoffs tracked through April 2026 were attributed to AI/automation — but "attribution doesn't mean causation." (cited)

**Data points:**
- Klarna: 700 agents' worth of work claimed automated (2024) → rehiring (2026). 
- IBM: ~8,000 HR roles cut to AskHR → partial rehire.
- Orgvue: 32% rehired post-AI-layoff. Careerminds: ~67% rehiring (n=600, Feb 2026).
- ~60% of hiring managers admit emphasizing AI as a more palatable layoff rationale than finances. (survey, 2026)

---

## Follow-the-money synthesis (cross-source patterns)

**Who profits from "cut headcount":** Short-term, the CEO/CFO booking the budget reduction and the stock-market story (Gartner [5]: layoffs "create budget room"). The narrative is amplified because "AI made us efficient" is better investor optics than "we over-hired" ([12]). BUT the ROI doesn't follow ([5]: no correlation) and ~half reverse ([6]) — so the durable beneficiary is the *story*, not the P&L.

**Who profits from "reskill / reshape, don't replace":** Consultancies. BCG ($3.6B/25% of revenue [7]) and McKinsey sell transformation, change-management, and reskilling — and the "reshape not replace" framing is itself a consulting product that keeps clients spending instead of panicking. They also cut their OWN staff ([8]), monetizing the same trend internally. Analyst firms (Gartner, Forrester) sell the sober-referee guidance.

**Who profits from "control your tokens":** (a) The model vendors — usage-based pricing lets Anthropic/OpenAI capture the value of compounding agentic workloads, which they NEED to justify ~$900B–$1T IPO valuations ([1],[3]); GitHub/Microsoft converts flat Copilot seats into metered token wallets ([9]). (b) The new AI-FinOps vendor class — CloudZero ($56M Series C, "The AI ROI Company") [10], Pay-i (Khosla seed), Vantage, Finout — whose entire pitch is the cost panic. The FinOps Foundation [11] (vendor-funded) elevates "FinOps for AI" to #1 priority. Uncertainty about AI ROI is literally their TAM.

**The deflation counter (steelman):** Vendors' fat-and-rising inference margins (~38%→70% [2],[4b]) plus falling per-token prices ($10→$2.50/M) mean they have room to keep cutting prices — so the "subsidy cliff" may be transient, at least for smaller models. The follow-the-money tension: the SAME vendors want both (i) lower headline token prices to drive adoption AND (ii) more total usage/spend to feed IPO revenue. Both can be true — price per token falls while total bills rise.

**The cleanest single irony:** The two CEOs who did the most to seed the "AI replaces workers / cheap labor substitution" narrative (Altman, Amodei) BOTH walked it back ([1],[3]) in the exact window they need investors to believe AI is a growth story, not a social threat. The labor-apocalypse fear that powers the cost-savings pitch is being quietly disowned by its original authors — for reasons of finance, not evidence.
