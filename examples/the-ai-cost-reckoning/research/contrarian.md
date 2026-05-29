# Contrarian: The AI cost reckoning — does replacing workers with AI actually save money?

**Lens mandate:** Steelman BOTH provocations a skeptical reader will raise:
1. The "cost reckoning" is a *temporary subsidy-unwind* that token-price deflation will erase within ~a year.
2. AI-for-labor substitution genuinely *DOES* save money at scale where deployed narrowly.
Find the best version of: **"the bears are wrong — AI gets cheaper and the savings are real."**

**Summary (6 bullets):**
- **The deflation curve is real, large, and — crucially — driven by efficiency and competition, not just subsidy.** Two independent primary sources converge: a16z's Guido Appenzeller ("LLMflation") clocks **~10x/year** decline, with a GPT-3-quality model falling from **$60/Mtok (Nov 2021) to $0.06/Mtok (Nov 2024) — 1,000x in 3 years**; Epoch AI (Tier 1) finds the price to hit a fixed capability benchmark fell **9x–900x/yr (median ~50x)**. The named drivers are quantization, smaller models, better GPUs, and open-weight competition — not primarily VC burn. That undercuts the pure "it's all subsidy" bear story.
- **The price war is structural, and 2026 made it sharper, not softer.** DeepSeek's V4-Pro cut (permanent, May 2026) put comparable reasoning at **~90–95% below OpenAI/Anthropic API prices** (as low as ~$0.0035/Mtok), and self-hosting open weights reportedly cuts AI opex **85–95%** vs closed APIs. When a competitor delivers comparable performance at ~2% of your price, deflation is competition-driven and hard to reverse — exactly what a subsidy-unwind story needs to be false.
- **The narrow-substitution savings case has its best exhibit in Klarna:** an AI assistant doing the work of ~700 FTE agents, **2.3M conversations in month one**, **25% drop in repeat inquiries**, resolution time **11 min → under 2 min**, parity CSAT, **$40M profit improvement (2024)** — a real, primary-sourced number, even after Klarna re-added humans for complex cases. At ~$57k fully-loaded per agent, 700 agents ≈ $40M/yr of avoided labor cost against an estimated $5–10M AI run-cost: the unit economics pencil where the task is high-volume, low-variance, and error-tolerant.
- **The "AI destroys jobs / it's all cost-cutting" panic is empirically weak — and the strongest data says AI mostly *augments*.** The Anthropic Economic Index finds **57% of Claude usage is augmentation vs 43% automation**. The Dallas Fed (Tier 1) finds wages in AI-exposed sectors *rising*, not falling (computer-systems-design wages **+16.7% vs +7.5% national** since fall 2022) — inconsistent with simple labor replacement. Jevons paradox (invoked by Hassabis and Nadella) is the deepest version: cheaper intelligence expands the total market for intelligence, including human work.
- **The honest bull case is conditional, not universal:** AI substitution wins where the task is high-volume, low-variance, error-tolerant, the human baseline is expensive, AND you route to the cheapest adequate model rather than the frontier one. Even the bearish MIT "only ~23% of tasks pencil out today" framing concedes ~1-in-4 tasks ALREADY clear the bar — *before* another year of 10x deflation.
- **The deepest counter-to-the-counter (the bull must concede this):** per-*token* deflation is necessary but not sufficient. Agentic workflows consume vastly more tokens per outcome, so the relevant unit is cost-per-*accepted-outcome*, not cost-per-token. Even the deflation bulls' own primary source (Epoch) flags that the *fastest* declines (900x/yr) only began after Jan 2024 and "it's less clear that those will persist." Whether the reckoning is temporary turns on whether $/token deflation outruns tokens/task inflation — genuinely unresolved.

---

## Sources

### [1] LLM inference prices have fallen rapidly but unequally across tasks
- URL: https://epoch.ai/data-insights/llm-inference-price-trends
- Author: Ben Cottier, Ben Snodin, David Owen, Tom Adamczewski
- Publication: Epoch AI (Data Insights)
- Date: 2025-03-12
- Tier: 1 (independent research institute; primary quantitative analysis of model+price data; the single most-cited source on this curve)
- Credibility notes: Epoch AI is a respected, methodologically transparent AI-trends research org; widely cited by The Economist, FT, etc. This is the canonical primary source for the deflation claim — which makes it the strongest available foundation for the steelman AND the most credible source for the steelman's own limits.

**Key quotes:**
> "The rate of decline varies dramatically depending on the performance milestone, ranging from 9x to 900x per year." — Epoch AI, 2025-03-12

> "The price to achieve GPT-4's performance on a set of PhD-level science questions fell by 40x per year." — Epoch AI, 2025-03-12

> "The fastest trends (e.g. 900x per year) start after January 2024 ... The fastest price drops in that range have occurred in the past year, so it's less clear that those will persist." — Epoch AI, 2025-03-12

**Key claims:**
- Across six benchmarks over ~3 years, the price to reach a fixed capability milestone fell between 9x/yr and 900x/yr, **median ~50x/yr**. (cited from [1]) — the empirical backbone of the steelman: if the *task* is held constant, intelligence is deflating faster than almost any technology in history.
- The decline is *unequal across tasks* — cheap on some benchmarks, far slower on others; you cannot assume your specific workload is on the 900x curve. (cited from [1])
- Drivers (smaller models, cheaper hardware, others "difficult to determine from public information") — Epoch did NOT find that shrinking margins/subsidy fully explain the drops, weakening the pure "it's all subsidy" bear story. (cited from [1])
- **Steelman's built-in caveat:** the most dramatic decline rates are the most recent and least proven to persist — the bull case partly extrapolates the steepest segment of the curve. (cited from [1])

**Data points:**
- 9x–900x per year price decline to reach a fixed benchmark; median ~50x/yr. (Epoch AI, as of 2025-03-12)
- 40x/yr decline for GPT-4-level performance on GPQA Diamond (PhD-level science). (Epoch AI, 2025-03-12)
- Fastest (900x/yr) trends began after January 2024. (Epoch AI, 2025-03-12)

### [2] Welcome to LLMflation — LLM inference cost is going down fast
- URL: https://a16z.com/llmflation-llm-inference-cost/
- Author: Guido Appenzeller
- Publication: Andreessen Horowitz (a16z)
- Date: 2024-11-12
- Tier: 3 (VC firm with a financial stake in AI adoption — clear directional bias toward "AI is cheap and getting cheaper." But the underlying price data is verifiable and independently corroborated by Epoch [1], so the numbers are usable; treat the *interpretation* as advocacy.)
- Credibility notes: a16z is a major AI investor; this is the essay that coined "LLMflation" and is the most-cited articulation of the deflation-bull thesis. Use it as the steelman's clearest voice, cross-checked against Epoch [1].

**Key quotes:**
> "the cost is decreasing by 10x every year" — Guido Appenzeller, a16z, 2024-11-12

> "there is no question we are seeing an order of magnitude decline in cost every year" — Guido Appenzeller, a16z, 2024-11-12

> "the price decline in LLMs is even faster" [than Moore's Law, Dennard scaling, or Edholm's Law for bandwidth] — Guido Appenzeller, a16z, 2024-11-12

**Key claims:**
- For a model scoring MMLU 42 (GPT-3-equivalent), price fell from **$60/Mtok (GPT-3, Nov 2021) to $0.06/Mtok (Llama 3.2 3B via Together.ai, Nov 2024)** — a **1,000x drop in 3 years**. (cited from [2])
- For the higher MMLU-83 (GPT-4) tier, price fell ~**62x** since March 2023; note the frontier tier (o1) is still priced at ~$60/Mtok output — i.e., the *frontier* stays expensive while the *capability floor* collapses. (cited from [2]) — important nuance: deflation is fastest for "good enough," not for the bleeding edge.
- Named drivers: GPU cost/performance, **4-bit quantization**, software optimization, **smaller models** (a 1B model now beating a 2021 175B model), instruction tuning, and **open-source competition** (Meta/Mistral). (cited from [2]) — these are efficiency/competition drivers, not subsidy, which is the steelman's core point.
- Illustrative "too cheap to meter" use cases: transcribing ~10,000 words/hour of speech for ~$2/year; processing the entire 40M-line Linux kernel for under $1. (cited from [2])
- **Author's own caveat:** "the cost of LLM inference will likely continue to decrease, [but] its rate may slow down"; MMLU "can be easily contaminated"; quantization scaling "may not continue." (cited from [2]) — the bull concedes the rate is not guaranteed.

**Data points:**
- ~10x/year inference-cost decline for equivalent performance, sustained ~3 years (Nov 2021–Nov 2024). (a16z, 2024-11-12)
- $60/Mtok → $0.06/Mtok = 1,000x for a GPT-3-quality (MMLU 42) model in 3 years. (a16z, 2024-11-12)
- ~62x decline for GPT-4-tier (MMLU 83) performance since March 2023. (a16z, 2024-11-12)

### [3] Klarna's AI assistant handles two-thirds of customer service chats in its first month
- URL: https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/
- Author: Klarna (corporate press release) with quotes from Sebastian Siemiatkowski (CEO) and Brad Lightcap (COO, OpenAI)
- Publication: Klarna newsroom
- Date: 2024-02-27
- Tier: 4 for *interpretation* (self-promotional first-party claim by the deploying company + its vendor) but Tier 2-equivalent for the *raw operational figures*, which are internally consistent and have been widely reported. The $40M is "estimated… profit improvement," not audited cost savings — treat as a directional figure, not a P&L line.
- Credibility notes: Both Klarna and OpenAI had a strong incentive to make this launch look transformative. The figures are first-party and unaudited. Critically, the SAME company later qualified the strategy (re-added human agents for complex cases, CEO called pure-cost prioritization a quality mistake by 2025) — so this is the bull's best exhibit AND comes pre-loaded with the bear's rebuttal.

**Key quotes:**
> "The AI assistant has had 2.3 million conversations, two-thirds of Klarna's customer service chats... It is doing the equivalent work of 700 full-time agents... It is on par with human agents in regard to customer satisfaction score... leading to a 25% drop in repeat inquiries... Customers now resolve their errands in less than 2 mins compared to 11 mins previously... It's estimated to drive a $40 million USD in profit improvement to Klarna in 2024." — Klarna press release, 2024-02-27

> "This AI breakthrough in customer interaction means superior experiences for our customers at better prices, more interesting challenges for our employees, and better returns for our investors." — Sebastian Siemiatkowski, CEO of Klarna, 2024-02-27

**Key claims:**
- One AI assistant performed the equivalent work of ~700 FTE customer-service agents within its first month live. (cited from [3])
- Quality held: CSAT on par with humans, AND a measurable 25% reduction in repeat inquiries (i.e., more first-contact resolution). (cited from [3]) — the bull's strongest point: this wasn't cheaper-but-worse, it was cheaper-and-at-least-as-good on the measured dimensions.
- Operating in 23 markets, 24/7, in 35+ languages — capabilities (24/7 multilingual coverage with instant scaling) that a human org would pay a large premium to match. (cited from [3])
- $40M estimated 2024 profit improvement. (cited from [3]) — widely cross-referenced as ~700 agents × ~$57k fully-loaded ≈ $40M avoided labor cost, against an estimated $5–10M/yr AI run-cost (third-party estimate, not Klarna's).

**Data points:**
- 2.3M AI conversations in month one; 700 FTE-agent equivalent. (Klarna, 2024-02-27)
- Resolution time 11 min → <2 min; 25% drop in repeat inquiries; CSAT parity. (Klarna, 2024-02-27)
- $40M estimated profit improvement in 2024. (Klarna, 2024-02-27)
- 23 markets, 24/7, 35+ languages. (Klarna, 2024-02-27)

### [4] AI is simultaneously aiding and replacing workers, wage data suggest
- URL: https://www.dallasfed.org/research/economics/2026/0224
- Author: Federal Reserve Bank of Dallas (research economists; piece references work by Tyler Atkinson, and cites Autor, Brynjolfsson, Felten/Raj/Seamans)
- Publication: Federal Reserve Bank of Dallas — Economics research
- Date: 2026-02-24
- Tier: 1 (regional Federal Reserve research using BLS wage data and peer-reviewed exposure indices; primary empirical analysis)
- Credibility notes: A Federal Reserve bank is about as close to a neutral, non-commercial referee as exists on this question. No stake in AI hype either direction. This is the strongest empirical rebuttal to the "AI is just labor-replacement" framing — it shows the labor-market signature of *augmentation*, not pure substitution, for experienced workers.

**Key quotes:**
> "Early data on employment and wages in AI-affected industries suggest it may be doing both [automating and augmenting]." — Dallas Fed, 2026-02-24

> "Since fall 2022, nominal average weekly wages nationwide have increased 7.5 percent, while the computer systems design sector has risen 16.7 percent." — Dallas Fed, 2026-02-24

> "AI can substitute for entry-level workers—new graduates with book-learning but no experience—and at the same time complement experienced workers, who have tacit knowledge that cannot be replicated by AI." — Dallas Fed, 2026-02-24

**Key claims:**
- Wages are RISING in AI-exposed sectors even as employment in some (computer systems design, –5%) lags — a pattern inconsistent with simple "AI replaces labor and wages fall." (cited from [4]) — central to the steelman against the job-apocalypse framing: if AI were purely substituting, both wages and employment would fall; instead wages rose.
- AI substitutes for *codified* knowledge (entry-level, textbook) but complements *tacit* knowledge (experience) — so the effect is reallocation, not wholesale elimination. (cited from [4])
- The displacement that does appear is concentrated on under-25 new entrants via a low job-finding rate, not layoffs of existing workers. (cited from [4]) — qualifies the bull case honestly: there IS a real entry-level cost, even if it's not the "everyone gets replaced" story.

**Data points:**
- Computer-systems-design wages +16.7% vs +7.5% national since fall 2022. (Dallas Fed, 2026-02-24, BLS data)
- Employment in the 10% most AI-exposed sectors –1% since late 2022; computer systems design –5%. (Dallas Fed, 2026-02-24)
- Median occupation "experience premium" 40% (range <10% to >100%); higher-experience-premium jobs see AI exposure associated with *positive* wage effects. (Dallas Fed, 2026-02-24)

### [5] The Anthropic Economic Index
- URL: https://www.anthropic.com/research/the-anthropic-economic-index
- Author: Anthropic (research team)
- Publication: Anthropic
- Date: 2025-02-10 (initial report)
- Tier: 3 (first-party data from a frontier AI lab with an interest in framing AI as a complement to workers — clear directional bias. But it is a large empirical dataset of real Claude usage, the best available proxy for how AI is actually being used at the task level.)
- Credibility notes: Anthropic benefits commercially and reputationally from the "AI augments, doesn't replace" narrative — weigh accordingly. Still, the augment-vs-automate split is derived from millions of real conversations, not a survey, which makes the *measurement* more credible than the *spin*.

**Key quotes:**
> [In just over half of cases] "AI was not being used to replace people doing tasks, but instead worked _with_ them" [in validation, learning, and task iteration]. — Anthropic Economic Index, 2025-02-10

**Key claims:**
- **57% of Claude usage is augmentation** (AI collaborates with a human) vs **43% automation** (AI performs the task directly). (cited from [5]) — direct evidence that, at the task level, AI is more often a co-pilot than a replacement.
- AI use concentrates in mid-to-high-wage roles (software, data science) and is low at both the bottom and very top of the wage distribution — inconsistent with a simple "AI comes for the cheapest labor first" story. (cited from [5])
- Only ~4% of occupations use AI for 75%+ of their tasks; ~36% use it for at least 25% of tasks. (cited from [5]) — depth of automation is still shallow, so wholesale role-elimination is not yet the dominant pattern.

**Data points:**
- 57% augmentation / 43% automation of tasks. (Anthropic, 2025-02-10)
- Computer & Mathematical roles = 37.2% of Claude conversations; ~36% of occupations use AI for ≥25% of tasks; ~4% for ≥75%. (Anthropic, 2025-02-10)

### [6] DeepSeek's steep V4-Pro price cut escalates AI pricing war
- URL: https://www.infoworld.com/article/4176709/deepseeks-steep-v4-pro-price-cut-escalates-ai-pricing-war.html
- Author: InfoWorld staff (quotes analysts Sanchit Vir Gogia, Neil Shah, Amit Jaju)
- Publication: InfoWorld
- Date: 2026-05-25
- Tier: 2 (established tech-industry trade publication; the named analysts are at real research firms — Greyhound Research, Counterpoint Research, Ankura Consulting)
- Credibility notes: Trade press, so verify the headline price figures, but the value here is the *named-analyst interpretation* that the deflation is engineered/structural. This is the single strongest source for the steelman's core rebuttal to the subsidy-unwind thesis: a credible third party arguing the price cut is "an efficiency gain being passed through," not a promotional subsidy.

**Key quotes:**
> "It is not a discount. It is an efficiency gain being passed through... V4-Pro was engineered to cut the cost of long-context inference... This is why the price cut is permanent rather than promotional." — Sanchit Vir Gogia, Greyhound Research, in InfoWorld, 2026-05-25

> "high-margin, high-consumption token pricing models from Anthropic and OpenAI are becoming harder to justify for many enterprise workloads." — Neil Shah, Counterpoint Research, in InfoWorld, 2026-05-25

> "If a CIO can host DeepSeek V4-Pro on their own infrastructure, inference costs drop dramatically, and many projects that were previously uneconomical at scale become viable." — Amit Jaju, Ankura Consulting, in InfoWorld, 2026-05-25

**Key claims:**
- DeepSeek made a **permanent 75% cut** on V4-Pro (effective after May 31, 2026), with output as low as ~$0.87/Mtok and cached input at ~$0.0036/Mtok. (cited from [6]) — corroborated independently by multiple outlets (Silicon Canals, ChinaBizInsider, AIWeekly) reporting ~90–95% below comparable OpenAI/Anthropic pricing.
- The cut is framed by analysts as a *structural efficiency pass-through*, not a subsidy — directly contradicting the "subsidy era is ending so prices will rise" bear thesis. (cited from [6]) — THE pivotal steelman point: if competition + engineering drive prices down, withdrawal of one vendor's subsidy doesn't re-inflate the market.
- Self-hosting open weights makes previously-uneconomical workloads viable — a second, durable downward force on effective cost. (cited from [6])

**Data points:**
- DeepSeek V4-Pro: permanent 75% price cut; ~$0.87/Mtok output, ~$0.0036/Mtok cached input. (InfoWorld, 2026-05-25)
- Reported ~90–95% cheaper than comparable OpenAI/Anthropic API pricing. (cross-referenced; AIWeekly/Silicon Canals, May 2026)
- Self-hosting open weights reportedly cuts AI opex ~85–95% vs closed APIs. (cross-referenced; verify before citing as a hard figure — this specific % comes from secondary tech blogs, not a primary benchmark)

### [7] Jevons paradox: cheaper AI expands demand (incl. for human work) — Nadella/Hassabis
- URL: https://x.com/satyanadella/status/1883753899255046301 (primary tweet) ; corroborated at https://www.geekwire.com/2025/microsoft-ceo-says-ai-use-will-skyrocket-with-more-efficiency-amid-craze-over-deepseek/
- Author: Satya Nadella (CEO, Microsoft); reporting/context by GeekWire; concept also invoked by Demis Hassabis (CEO, Google DeepMind)
- Publication: X / GeekWire (and widely reported: NPR Planet Money, BusinessToday, Outlook Business)
- Date: 2025-01-27 (tweet)
- Tier: 4 for the tweet itself (executive statement, self-interested), Tier 2 for the GeekWire/NPR reporting that contextualizes it. Use the quote as a *named articulation of the argument*, not as evidence the argument is correct.
- Credibility notes: Nadella and Hassabis both run companies that profit enormously if AI demand "skyrockets" — this is the most self-interested possible source for the Jevons claim, and the steelman must flag that. The value is that it names the strongest *theoretical* counter to job-apocalypse fears: the rebound effect. The Dallas Fed wage data [4] is the empirical version of the same argument and carries the real weight.

**Key quotes:**
> "Jevons paradox strikes again! As AI gets more efficient and accessible, we will see its use skyrocket, turning it into a commodity we just can't get enough of." — Satya Nadella, 2025-01-27 (X)

**Key claims:**
- The Jevons rebound effect: when the unit cost of intelligence falls, total consumption of intelligence rises — existing users use more, new users enter, and new use cases become viable. (cited from [7]) — applied to labor, the steelman is that cheaper AI grows the *total* demand for cognitive work rather than shrinking the pie, shifting humans toward judgment-heavy tasks rather than eliminating them.
- Historical analogues (coal/steam engines 1865; later spreadsheets, ATMs, email) show efficiency gains often *expanded* the associated workforce. (cited from [7]) — note: this is suggestive, not dispositive; the bear's rebuttal is that AI substitutes for cognition itself, unlike prior tools that augmented it, so the analogy may break.

**Data points:**
- (Qualitative argument — no primary statistic. The empirical proxy is the Dallas Fed wage data in [4] and the 57/43 augmentation split in [5].)

### [8] AI in Financial Services Survey Shows Productivity Gains Across the Board
- URL: https://www.bain.com/insights/ai-in-financial-services-survey-shows-productivity-gains-across-the-board/
- Author: Bhavi Mehta, Oren Salomon, Marta Alves, Elaine Barth
- Publication: Bain & Company
- Date: 2024-07 (survey conducted July 2024)
- Tier: 2-3 (a top management consultancy that sells AI-transformation services — directional bias toward "AI works." But it is a structured survey of 109 firms, not anecdote, and the headline productivity figures align with independent RCTs.)
- Credibility notes: Bain profits from enterprises believing AI delivers ROI; weigh accordingly. Used here as a *corroborating, non-Klarna* data point that measurable productivity gains are real and broad-based — and as a counterweight to the Gartner "no ROI correlation" finding (the truth is contested, and the steelman gets to cite the optimistic survey).

**Key quotes:**
> "Companies now monitor when—not if—the use of AI will generate value across the board." — Bain & Company, July 2024

**Key claims:**
- Across 109 US financial-services firms, AI delivered ~**20% average productivity improvement** across uses, with software development showing a **26% increase in completed tasks** (citing a randomized controlled trial). (cited from [8]) — corroborates that the *productivity* side of the ledger is real, even where the *cost-savings* side is contested.
- Large firms ($5B+ revenue) averaged $22.1M in 2024 AI spend with ~270 FTE engaged — i.e., the spend is material, which is precisely why the cost question matters; but respondents framed value as a "when not if." (cited from [8])

**Data points:**
- +20% average productivity across AI uses; +26% completed coding tasks (RCT-based). (Bain, July 2024, n=109 US financial-services firms)
- $22.1M average 2024 AI spend at $5B+ revenue firms. (Bain, July 2024)

### [9] Corroborated enterprise ROI exhibit: JPMorgan Chase (~$1.5B AI value)
- URL: (Reuters report, 2025-05-05, summarized via multiple outlets; primary figure from JPMorgan COO Daniel Pinto)
- Author: Reuters (primary statement: Daniel Pinto, President & COO, JPMorgan Chase)
- Publication: Reuters (widely syndicated)
- Date: 2025-05-05
- Tier: 2 (Reuters) reporting a Tier-1-adjacent primary statement from the company's COO. The figure is company-provided ("business value"/cost savings), so it blends cost avoidance + revenue uplift — not a pure cost-reduction number.
- Credibility notes: Company-sourced and broad ("fraud prevention, trading, credit decisions"), so it's a directional ROI claim, not an audited line item. Included as a second independent "savings are real at scale" exhibit beyond Klarna, to avoid resting the whole bull case on one company.

**Key claims:**
- JPMorgan reported **~$1.5B** in AI-driven value/cost savings (fraud prevention, trading, credit decisions), with COO Pinto projecting **$1.5B–$2.0B** in tangible business value. (cited from [9]) — a large, regulated, scrutinized institution publicly attaching a ~$1.5B figure to AI is the bull's strongest non-Klarna data point.
- Caveat for the article: this is "business value" (cost avoidance + revenue uplift), not net-of-AI-cost savings — the same blurring the bears warn about. Cite as directional, not as proof the math nets positive after compute. (cited from [9])

**Data points:**
- ~$1.5B AI-attributed business value/cost savings; projected $1.5B–$2.0B. (Reuters, 2025-05-05, JPMorgan COO Pinto)
