# Data: The AI cost reckoning — does replacing workers with AI actually save money?

**Lens focus:** Hard numbers with primary-source URLs. Quantify the deflation-vs-volume tension precisely — token-price decline curves (Epoch AI), tokens-per-task growth for agentic workflows, the MIT "23% of tasks cost-effective" study, Gartner survey internals, per-engineer Claude Code spend, AI software price inflation.

**Summary (5 bullets):**
- **Both things are true at once.** Per-token inference prices are collapsing (Epoch AI: median ~50x/year historically, ~200x/year since Jan 2024, halving roughly every ~2 months at fixed performance) WHILE tokens-consumed-per-task is exploding (agentic coding tasks burn up to 1000x more tokens than code-chat; same task varies up to 30x run-to-run). The cost reckoning is the collision of these two curves — deflation per unit vs. inflation in units consumed.
- **The canonical "AI isn't cheap enough" stat (MIT FutureTech, Feb 2024): only 23% of worker wages in vision tasks are economically attractive to automate at current cost; 77% are not.** This is the empirical backbone of the "savings math doesn't hold" thesis — but it is (a) vision-only, (b) pre-dates the 2024-26 price collapse, and the authors explicitly model that falling costs / AI-as-a-service flip the math.
- **Higher spend ≠ better output.** The Microsoft Research / Stanford paper (Brynjolfsson & Pentland among authors, Apr 2026) finds accuracy peaks at *intermediate* token cost, and frontier models can't predict their own token usage (correlation ≤0.39) — a direct, peer-reviewed argument for FinOps-style cost governance.
- **The ROI evidence is genuinely weak.** Gartner: ~80% of organizations report no material enterprise-level EBIT/ROI impact from GenAI. MIT Media Lab "GenAI Divide": 95% of enterprise GenAI pilots show zero return. These cut against the "AI saves millions by replacing labor" framing.
- **Prices are also going UP where it's billed as software.** AI-feature price uplifts on software renewals run ~20-37% (Tropic [8], vendor-sourced), and the pivot from flat per-seat to usage/credit pricing is now documented as a primary fact: GitHub Copilot moves to token-metered AI Credits on 2026-06-01, with GitHub's own rationale that "a quick chat question and a multi-hour autonomous coding session can cost the user the same amount" under flat pricing — "no longer sustainable" [7]. So the buyer's *realized* unit cost can rise even as the *list* per-token price falls.

**Seed-claim verification (data lens):**
- **Microsoft cutting internal Claude Code licenses → CORROBORATED (Tier 2-3).** Reported by Windows Central and others: Microsoft is canceling most internal Claude Code licenses by ~2026-06-30, migrating engineers to GitHub Copilot CLI; drivers cited are cost-at-scale AND the strategic conflict of selling Copilot while its own engineers preferred Claude. No primary Microsoft document; treat as well-reported but not officially confirmed.
- **Uber burning its 2026 AI budget in ~4 months → CORROBORATED on substance, but the seed's dollar figure is UNVERIFIED.** Confirmed (Fortune/Business Insider/The Verge): full-year budget gone in 4 months, ~5,000 engineers, 32%→84% adoption (Feb→Mar), $150-$250/mo typical and $500-$2,000/mo heavy per engineer, CTO burned $1,200 in a 2-hr demo. The "~$1.2M total budget" is a CONFLATION (the $1,200 demo figure and a separate "$1.2M→$7M industry-average budget" stat); Uber's actual total is not disclosed. One search even hallucinated a "$3.4B 2026 AI budget" — a cautionary example of exactly the number-inflation this article must avoid.
- **GitHub Copilot → usage-based credits → CONFIRMED via primary source [7].** Effective 2026-06-01, token-metered, 1 credit = $0.01.

**Robustness note:** The deflation curve is the most over-determined claim here — Epoch AI [1], a16z [6], and Stanford HAI [10] independently land on ~1-3 orders of magnitude/year. The corpus skews Tier 1 on deflation (Epoch, Stanford, MIT) and Tier 3 on the inflation/FinOps side (Tropic, Vertice, NavyaAI are vendors selling the fix) — flag this asymmetry when citing the 20-37% and "bills tripled" figures.

---

## Sources

### [1] LLM inference prices have fallen rapidly but unequally across tasks
- URL: https://epoch.ai/data-insights/llm-inference-price-trends
- Author: Ben Cottier, Ben Snodin, David Owen, Tom Adamczewski
- Publication: Epoch AI (Data Insights)
- Date: 2025-03-12
- Tier: 1 (independent research institute; primary data compilation with published methodology)
- Credibility notes: Epoch AI is a nonprofit research org specializing in AI trends/compute economics; widely cited by academics and journalists. This is a quantitative data insight with stated regression methodology, not opinion. The "unequally across tasks" framing is itself a key nuance — they actively caution against a single headline number.

**Key quotes:**
> "the rate of decline varies dramatically depending on the performance milestone, ranging from 9x to 900x per year." — Epoch AI, 2025-03-12

**Key claims:**
- Across benchmarks/performance thresholds, LLM inference price declines run from 9x/year to 900x/year, median ~50x/year. (cited from [1])
- Post-January 2024 the median rate rises to ~200x/year — i.e. price drops are *accelerating*. (cited from [1])
- The fastest single trend (~900x/year) began after January 2024. (cited from [1])
- For GPT-4-level performance on PhD-level science (GPQA) questions, price fell ~40x/year. (cited from [1])
- Cost to reach a fixed performance level has been roughly halving every ~2 months (~2 orders of magnitude/year). (cited from [1])
- Reasoning models were EXCLUDED because inflated token generation distorts cost comparison — important caveat: the deflation curve is measured on non-reasoning, non-agentic usage. (cited from [1])

**Data points:**
- 9x–900x per year: range of LLM inference price decline across milestones (as of 2025-03-12).
- 50x/year: median price decline (full history).
- 200x/year: median price decline using only post-Jan-2024 data.
- 40x/year: price decline for GPT-4-level GPQA performance.
- Halving every ~2 months at fixed performance (~100x/year).
- Methodology: log-linear regression, ≥4 data points per trend, 36 model-price observations, 6 benchmarks (MMLU, GPQA Diamond, MATH-500, MATH Level 5, HumanEval, Chatbot Arena ELO).

---

### [2] Beyond AI Exposure: Which Tasks are Cost-Effective to Automate with Computer Vision
- URL: https://futuretech.mit.edu/publication/beyond-ai-exposure-which-tasks-are-cost-effective-to-automate-with-computer-vision (paper on SSRN)
- Author: Maja S. Svanberg, Wensu Li, Martin Fleming, Brian C. Goehring, Neil Thompson
- Publication: MIT FutureTech / MIT CSAIL (working paper, SSRN)
- Date: 2024-02-08
- Tier: 1 (MIT research group; Neil Thompson is a leading AI-economics researcher; methodology-driven cost-benefit modeling)
- Credibility notes: The single most-cited empirical anchor for "AI is too expensive to replace most workers." Caveats: scope is **computer-vision tasks only** (not LLMs/coding), and it pre-dates the 2024–2026 inference price collapse. The authors explicitly model that cost declines or AI-as-a-service scale would flip the conclusion — so it is NOT evidence that AI labor substitution is permanently uneconomic, only that it was at early-2024 cost levels for vision.

**Key quotes:**
> "at today's costs U.S. businesses would choose not to automate most vision tasks that have 'AI Exposure.'" — Svanberg et al., MIT FutureTech, 2024-02-08
> "AI job displacement will be substantial, but also gradual – and therefore there is room for policy and retraining to mitigate unemployment impacts." — Svanberg et al., 2024-02-08

**Key claims:**
- Only ~23% of worker wages paid for vision tasks are economically attractive to automate at early-2024 costs. (cited from [2])
- The remaining ~77% of vision-task wages are NOT cost-effective to automate — implementation, maintenance and hardware costs exceed human wages. (cited from [2])
- Displacement will be "substantial but gradual," leaving room for policy/retraining. (cited from [2])
- Automation could accelerate via cost declines OR AI-as-a-service platforms with greater scale than individual firms. (cited from [2])

**Data points:**
- 23%: share of vision-task worker wages economically attractive to automate (current costs, Feb 2024).
- 77%: share NOT cost-effective to automate.
- Scope: computer-vision tasks with "AI exposure" in the US economy.

---

### [3] How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks
- URL: https://arxiv.org/abs/2604.22750 (also Microsoft Research publications; Stanford Digital Economy Lab writeup)
- Author: Longju Bai, Zhemin Huang, Xingyao Wang, Jiao Sun, Rada Mihalcea, Erik Brynjolfsson, Alex Pentland, Jiaxin Pei
- Publication: arXiv preprint (assoc. Microsoft Research; Stanford Digital Economy Lab)
- Date: 2026-04-24 (v1), 2026-04-29 (v2)
- Tier: 1 (academic preprint; author roster includes Erik Brynjolfsson and Alex Pentland — top-tier digital-economy researchers; empirical study on SWE-bench Verified)
- Credibility notes: Preprint (not yet peer-reviewed, version of record pending) but methodologically serious and from heavyweight authors. Directly supports the "AI behaves like compounding cloud infra, not fixed SaaS" thesis AND the FinOps case (you can't predict or linearly buy your way to accuracy). The 1000x figure's baseline is specifically "code reasoning and code chat" tasks — NOT generic chatbot queries — so quote it precisely.

**Key quotes:**
> "Agentic tasks consume 1000x more tokens than code reasoning and code chat" (input tokens, not output, drive cost). — Bai et al., arXiv 2604.22750, 2026

**Key claims:**
- Agentic coding tasks consume up to ~1000x more tokens than code-reasoning/code-chat tasks. (cited from [3])
- Input tokens (re-reading expanding context each loop) — not output tokens — drive the overall cost. (cited from [3])
- The SAME task varies by up to 30x in total tokens across runs — cost is highly non-deterministic. (cited from [3])
- Higher token usage does NOT yield higher accuracy; accuracy peaks at *intermediate* cost. (cited from [3])
- Frontier models fail to predict their own token usage (weak-to-moderate correlation, up to 0.39). (cited from [3])
- Kimi-K2 and Claude-Sonnet-4.5 consume on average >1.5 million more tokens than GPT-5 on the same tasks — model choice is a first-order cost lever. (cited from [3])

**Data points:**
- 1000x: agentic vs. code-chat/code-reasoning token consumption multiplier.
- Up to 30x: run-to-run token variance on the same task.
- ≤0.39: correlation between a model's predicted and actual token usage.
- >1.5M tokens: average extra token spend of Kimi-K2 / Claude-Sonnet-4.5 vs GPT-5 per task set.
- Dataset: SWE-bench Verified; 8 frontier LLMs evaluated.

---

### [4] Gartner Says Autonomous Business and AI Layoffs May Create Budget Room, but Do Not Deliver Returns
- URL: https://www.gartner.com/en/newsroom/press-releases/2026-05-05-gartner-says-autonomous-business-and-artificial-intelligence-layoffs-may-create-budget-room-but-do-not-deliver-returns
- Author: Gartner Newsroom (citing analyst Helen Poitevin); reporting verified via Fortune (Sasha Rogelberg, 2026-05-11) because gartner.com blocks automated fetch (HTTP 403)
- Publication: Gartner (primary press release) / Fortune (secondary, accessible)
- Date: 2026-05-05 (Gartner); 2026-05-11 (Fortune)
- Tier: 1 (Gartner is the primary survey author; this is their own data release. Fortune used as accessible mirror for verbatim text.)
- Credibility notes: Gartner is a research/advisory firm that also sells AI-strategy consulting — a mild conflict, but this finding cuts AGAINST the "just cut headcount" narrative that would be easy to sell, which raises its credibility. Survey is self-reported by executives (recall/social-desirability bias possible). The "no correlation" claim is the single strongest data anchor for the contrarian/ROI-skeptic thesis. Sample is large-enterprise only ($1B+ revenue) — does NOT generalize to startups/SMBs.

**Key quotes:**
> "Looking only at layoffs is shortsighted in terms of getting value from AI. Chasing value only through headcount reduction is likely to lead most organizations down a path of limited returns." — Helen Poitevin, Distinguished VP Analyst, Gartner (via Fortune, 2026-05-11)
> "Workforce reductions may create budget room, but they do not create return. Organizations that improve ROI are not those that eliminate the need for people, but those that amplify them..." — Helen Poitevin, Gartner (per multiple syndications of the 2026-05-05 release)

**Key claims:**
- ~80% of surveyed organizations that piloted/deployed autonomous tech reported workforce reductions. (cited from [4])
- Workforce-reduction rates were "nearly equal" among firms reporting HIGH ROI and those reporting modest/negative outcomes — i.e. NO correlation between cutting staff and getting returns. (cited from [4])
- Firms with the highest gains used AI as "people amplification" (augmenting workers), not replacement. (cited from [4])
- Gartner forecasts AI agent software spending of $206.5B in 2026 and $376.3B in 2027 (figure widely syndicated from the release; not in the Fortune excerpt). (cited from [4])
- Gartner projects autonomous business becomes a net-positive job creator by 2028–2029. (cited from [4])

**Data points:**
- 350: global business executives surveyed (Q3 2025).
- $1 billion+: minimum annual revenue to qualify (large-enterprise sample only).
- ~80%: share reporting workforce reductions after AI/autonomous pilots.
- "Nearly equal" reduction rates across high-ROI vs low-ROI firms = ~0 correlation between layoffs and ROI.
- $206.5B (2026) / $376.3B (2027): Gartner AI-agent software spend forecast.
- 2028–2029: projected crossover to net job creation.

---

### [5] Uber burned through its entire 2026 AI budget in four months. Now its COO is questioning whether it's worth it
- URL: https://fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/ (+ Business Insider original; Yahoo/The Verge syndications)
- Author: Fortune staff (syndicating Business Insider's all-hands reporting); COO/CTO quotes via Business Insider
- Publication: Fortune / Business Insider (original) / The Verge
- Date: 2026-05-26 (Fortune); underlying Uber all-hands ~May 2026
- Tier: 2 (established business journalism; the underlying event is a leaked/reported internal all-hands — strong but not a primary document)
- Credibility notes: This is the empirical centerpiece of the seed LinkedIn post's "Uber burned its budget" claim. VERIFICATION RESULT: The four-month burn, the 5,000-engineer org, the $150-$2,000/engineer spread, and 32%→84% adoption are all corroborated across Fortune, Business Insider, and The Verge. BUT the seed's implied "~$1.2M total budget" figure is NOT confirmed by any Tier 1-2 source — Uber has NOT disclosed the total dollar amount. The "$1,200" figure that circulates is the CTO burning $1,200 of tokens in a 2-hour live DEMO, not the annual budget; and a separate "$1.2M→$7M" stat is an industry-average AI budget, not Uber's. The seed conflates these. Treat the total-budget dollar figure as UNVERIFIED.

**Key quotes:**
> "That link is not there yet... Maybe implicitly there's more that is getting shipped, but it's very hard to draw a line between one of those stats and 'Okay now we're actually producing like 25% more useful consumer features.'" — Andrew Macdonald, President & COO, Uber (via Business Insider, 2026)
> "If you're not actually able to draw a direct line to how [many] useful features and functionality you're shipping to your users, that trade becomes harder to justify." — Andrew Macdonald, Uber (via Fortune, 2026-05-26)

**Key claims:**
- Uber exhausted its full-year 2026 AI coding-tools budget in ~4 months (by ~April). (cited from [5])
- Claude Code adoption rose from ~one-third of engineers (February) to 84% (March) of a ~5,000-engineer org. (cited from [5])
- Typical per-engineer spend $150-$250/month; heavy users $500-$2,000/month. (cited from [5])
- CTO Praveen Neppalli Naga burned ~$1,200 of tokens in ~2 hours during a single hands-on demo. (cited from [5])
- ~10% of committed code / live backend updates at Uber are AI-authored (per Uber Q1 earnings); the COO cannot draw a clear line from token spend to consumer value. (cited from [5])

**Data points:**
- 4 months: time to exhaust the full 2026 AI budget.
- ~5,000: engineers in scope.
- 32% (≈one-third, Feb 2026) → 84% (March 2026): Claude Code adoption jump.
- $150–$250/mo: typical per-engineer spend.
- $500–$2,000/mo: heavy-user per-engineer spend.
- $1,200 / 2 hours: CTO's token burn in a single live demo (NOT the annual budget).
- ~10%: share of committed code authored by AI agents (Uber Q1 earnings).
- TOTAL annual budget dollar figure: NOT publicly disclosed (seed's ~$1.2M is unverified/likely a conflation).

---

### [6] Welcome to LLMflation — LLM inference cost is going down fast
- URL: https://a16z.com/llmflation-llm-inference-cost/
- Author: Guido Appenzeller
- Publication: Andreessen Horowitz (a16z)
- Date: 2024-11-12
- Tier: 3 (VC firm with heavy financial stake in AI startups — strong analytical content but a clear pro-AI incentive; the underlying price data is verifiable, the optimistic framing is interest-laden)
- Credibility notes: This is the canonical statement of the STRONGEST deflation counter-argument ("the cost reckoning is temporary; tokens are getting 10x cheaper every year"). a16z is a major AI investor, so treat the bullish framing as motivated. The per-token figures are independently corroborated by Epoch AI [1]. Coined the term "LLMflation." Key honest caveat from the author himself: the rate "may slow down."

**Key quotes:**
> "For an LLM of equivalent performance, the cost is decreasing by 10x every year." — Guido Appenzeller, a16z, 2024-11-12
> "while the cost of LLM inference will likely continue to decrease, its rate may slow down" — Guido Appenzeller, a16z, 2024-11-12

**Key claims:**
- Inference cost for an equivalent-performance model falls ~10x per year. (cited from [6])
- A GPT-3-quality model (MMLU 42) fell from $60/M tokens (Nov 2021) to $0.06/M tokens — a 1,000x drop in 3 years. (cited from [6])
- Higher-tier (MMLU 83 / GPT-4-class) performance fell ~62x since March 2023. (cited from [6])
- BUT the frontier premium persists: OpenAI's o1 costs the same per output token ($60/M) as GPT-3 did at launch — i.e. the newest capability is NOT cheap. (cited from [6])

**Data points:**
- 10x/year: headline rate of equivalent-performance inference-cost decline.
- $60/M (Nov 2021) → $0.06/M (2024): GPT-3-class token price = 1,000x drop in 3 years.
- ~62x: decline in MMLU-83 (GPT-4-class) inference price since March 2023.
- $60/M output tokens: cost of o1 (frontier, 2024) = identical to GPT-3 at launch — the "frontier tax."

---

### [7] GitHub Copilot is moving to usage-based billing
- URL: https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/
- Author: Mario Rodriguez (GitHub)
- Publication: The GitHub Blog (official; Microsoft-owned)
- Date: 2026-04-27
- Tier: 1 (primary source — the vendor's own pricing announcement)
- Credibility notes: VERIFICATION RESULT for the seed claim "GitHub is moving Copilot toward usage-based AI credits" → CONFIRMED, with a precise date. This is a primary document, not reporting. The rationale quote is the cleanest articulation anywhere of WHY coding agents break the flat-seat model. Note: base subscription prices are unchanged; the shift is in how overage/agentic usage is metered. 1 AI Credit = $0.01 (per GitHub Docs).

**Key quotes:**
> "Today, a quick chat question and a multi-hour autonomous coding session can cost the user the same amount... the current premium request model is no longer sustainable." — Mario Rodriguez, GitHub, 2026-04-27
> Usage-based billing "better aligns pricing with actual usage [and] helps us maintain long-term service reliability." — GitHub, 2026-04-27

**Key claims:**
- GitHub Copilot transitions to usage-based (AI Credits) billing effective June 1, 2026. (cited from [7])
- Usage is metered by token consumption — input, output, AND cached tokens — at each model's listed API rate. (cited from [7])
- 1 AI Credit = $0.01 USD (per GitHub Docs). (cited from [7])
- Code completions and Next Edit suggestions remain free; Chat, autonomous agent sessions, and code review consume credits. (cited from [7])
- Explicit rationale: a chat question and a multi-hour agent run "cost the user the same amount" under flat pricing — "no longer sustainable." (cited from [7])

**Data points:**
- 2026-06-01: usage-based billing effective date.
- 1 credit = $0.01: AI Credit unit value.
- Plan credit allotments: Pro $10/mo, Pro+ $39/mo, Business $19/user/mo, Enterprise $39/user/mo (matching base price).
- Premium-request billing began 2025-06-18 (the transitional step before full token metering).

---

### [8] The AI Tax: How AI Is Driving Software Price Increases
- URL: https://www.tropicapp.io/blog/ai-tax
- Author: Justin Etkin (COO & Co-Founder, Tropic)
- Publication: Tropic (procurement/spend-management vendor)
- Date: 2025-12-23
- Tier: 3 (vendor research; useful proprietary dataset but a direct commercial incentive to emphasize rising prices — Tropic sells negotiation services)
- Credibility notes: This is the apparent ORIGIN of the widely-cited "AI software prices up 20-37%" figure. CONFLICT OF INTEREST is explicit: Tropic profits when buyers fear price increases. Sample size NOT disclosed ("a real-world dataset of AI-driven software renewals across Tropic customers") — a transparency gap. Treat the 20-37% as a vendor-sourced signal, not a peer-reviewed index. The Slack $20→$45/user example is a concrete, checkable data point.

**Key quotes:**
> "AI pricing uplifts sit between 20–37%, regardless of vendor category." — Justin Etkin, Tropic, 2025-12-23
> "Negotiation reduces the initial vendor ask by ~55% in relative terms, but final pricing still lands materially above pre-AI baselines (average final uplift ≈ 12%)." — Justin Etkin, Tropic, 2025-12-23

**Key claims:**
- AI-feature pricing uplifts on software renewals run 20-37% across vendor categories. (cited from [8])
- Four mechanisms: forced SKU migrations, credit-based obfuscation, unbundle-then-rebundle, AI-conditional discounts. (cited from [8])
- Even after hard negotiation, buyers pay ~12% above their pre-AI baseline on average. (cited from [8])

**Data points:**
- 20-37%: AI-feature price uplift range on software renewals (Tropic dataset, late 2025).
- Slack example: $20/user → $45/user via forced SKU migration.
- ~55%: relative reduction achievable by negotiation; ~12%: residual uplift above pre-AI baseline.
- Sample size: NOT disclosed (credibility caveat).

---

### [9] Vertice SaaS Inflation Index (2023 + 2026 editions)
- URL: https://www.vertice.one/l/saas-inflation-index-report ; https://www.cfodive.com/news/stubbornly-high-saas-prices-outpace-cpi-inflation/699683/
- Author: Vertice (data); CFO Dive (reporting, Lindsey Wilkinson)
- Publication: Vertice (SaaS/cloud spend-management firm) / CFO Dive
- Date: 2023-11-14 (original index); 2026 edition data current to March 2026
- Tier: 3 (vendor research with the same pro-"prices are rising" incentive as Tropic, BUT based on a large purchasing dataset — 16,000 vendors — which lends weight; CFO Dive reporting is Tier 2)
- Credibility notes: Vertice manages real SaaS purchasing for clients, so its index draws on 16,000 vendors' actual contract data — more grounded than survey opinion. Same commercial-incentive caveat as Tropic. Useful for the "list price is rising even as token prices fall" half of the tension. The per-employee SaaS spend trend ($7,900→$9,100) is a clean longitudinal data point.

**Key quotes:**
> "60% of vendors deliberately mask their rising prices" — Vertice SaaS Inflation Index (2026 edition)

**Key claims:**
- SaaS price inflation ran ~8.7% in 2023 (>2x the 3.2% CPI) and ~12-13% in early 2026 — persistently outpacing consumer inflation. (cited from [9])
- SaaS spend per employee rose from $7,900 (2023) to $8,700 (2024) to ~$9,100 (end 2025) — ~15% over two years. (cited from [9])
- ~73% of SaaS vendors raised prices in 2023; ~60% deliberately obscure increases (2026). (cited from [9])

**Data points:**
- 8.7% (2023) → ~12.2-13.2% (March 2026): SaaS price inflation rate.
- ~5x: SaaS inflation vs. G7 consumer inflation (2026 edition).
- $7,900 → $9,100 per employee: SaaS spend, 2023→end-2025.
- 16,000: vendors in Vertice's purchasing dataset (methodology anchor).
- 60%: vendors that mask price increases (2026).

---

### [10] The cost of GPT-3.5-level inference fell ~280x (Stanford HAI 2025 AI Index)
- URL: https://hai.stanford.edu/ai-index/2025-ai-index-report (via Search Engine Journal report, Matt G. Southern, 2025-04-09)
- Author: Stanford HAI (Institute for Human-Centered AI), Nestor Maslej et al. (Index authors); reporting by Search Engine Journal
- Publication: Stanford HAI AI Index 2025 / Search Engine Journal
- Date: 2025-04 (Index release)
- Tier: 1 (Stanford HAI AI Index is the most-cited annual AI metrics compendium; primary aggregation with disclosed sourcing. SEJ used as accessible mirror.)
- Credibility notes: Independent academic index; the gold-standard citation for AI cost/capability trends in journalism. The 280x figure is a SECOND independent confirmation of the Epoch [1] and a16z [6] deflation curves, using a different baseline (GPT-3.5 / MMLU ~64-66). Three independent sources (Epoch, a16z, Stanford) agreeing on ~1-3 orders of magnitude/year of deflation makes this the most robust quantitative claim in the entire dossier.

**Key quotes:**
> "the price of using GPT-3.5-level AI models has dropped from $20.00 to just $0.07 per million tokens" — Stanford HAI 2025 AI Index (as reported by Search Engine Journal, 2025-04-09)

**Key claims:**
- GPT-3.5-level inference fell from $20.00/M tokens (Nov 2022) to $0.07/M tokens — a ~280x drop in ~18 months. (cited from [10])
- Confirms the broader deflation trend independently of Epoch and a16z. (cited from [10])

**Data points:**
- 280x (≈99.7%): GPT-3.5-level inference price drop, Nov 2022 → early 2024.
- $20.00/M → $0.07/M tokens: the exact endpoints.
- ~18 months: the window.

---

### [11] Tokens got 99.7% cheaper. So why did your AI bill triple? (the deflation-vs-volume tension, quantified)
- URL: https://navyaai.com/reports/ai-cost-report-token-prices-vs-ai-bill
- Author: NavyaAI (AI cost/observability vendor)
- Publication: NavyaAI (report)
- Date: 2026-02 (reviewed 2026-05-26)
- Tier: 3 (vendor report; NavyaAI sells AI cost observability, so it has an incentive to stress hidden costs — but the structural breakdown is logically sound and corroborated by the agentic-token paper [3])
- Credibility notes: This is the single best QUANTIFIED statement of the deflation-vs-volume paradox — it puts numbers on both blades of the scissors. Vendor incentive caveat applies (sells the FinOps fix). The "model tokens are only 20-40% of real AI cost" claim is the key counter to naive token-price optimism: even if tokens were free, 60-80% of cost remains. Cross-check the 3x figure against independent enterprise-spend data before citing as fact.

**Key quotes:**
> "Token prices fell 99.7%, yet average monthly AI invoices tripled" — NavyaAI, 2026-02
> the model token invoice represents only "20-40% of real AI cost" (≈72% of spend occurs outside inference) — NavyaAI, 2026-02

**Key claims:**
- Unit token price fell ~99.7% while the average monthly AI bill ~tripled (3x). (cited from [11])
- The raw model/token invoice is only 20-40% of true AI cost; the other 60-80% is orchestration, retries/fallbacks, idle/overprovisioned compute, retrieval/vector inefficiency, observability/guardrails, and human incident response. (cited from [11])
- Therefore falling per-token prices cannot, alone, deliver net savings — the cost base is mostly non-token. (cited from [11])

**Data points:**
- 99.7%: token unit-price decline.
- 3x: average monthly AI bill increase over the same period.
- 20-40%: model tokens as a share of true all-in AI cost (so ~60-80% is non-inference).
- 6 named non-token cost categories driving the gap.

---

### [12] The GenAI Divide: State of AI in Business 2025 (MIT NANDA — 95% of pilots show no return)
- URL: https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf (MIT NANDA; via Fortune, 2025-08-18)
- Author: MIT NANDA initiative; lead author Aditya Challapally; reporting by Fortune (Sheryl Estrada)
- Publication: MIT NANDA / Fortune
- Date: 2025-08-18
- Tier: 2 (MIT-affiliated research group, but a non-peer-reviewed industry report; the "95%" headline drew methodological pushback for relying partly on interviews/surveys rather than audited financials — note this when citing)
- Credibility notes: The most-cited data point for "enterprise AI isn't paying off." Important caveats: (a) it measures rapid P&L revenue acceleration, a HIGH bar — "no measurable return" ≠ "negative return"; (b) methodology is interviews + survey + public-deployment review, not audited财务; (c) it found buying tools succeeds ~2x more often than building, so it's not anti-AI per se. Pair with Gartner [4] (independent, different method, same direction) for a robust ROI-skeptic claim.

**Key quotes:**
> 95% of generative AI pilot programs deliver "little to no measurable impact on P&L." — MIT NANDA, State of AI in Business 2025
> "Some large companies' pilots and younger startups are really excelling with generative AI." — Aditya Challapally, lead author, MIT NANDA (via Fortune, 2025-08-18)

**Key claims:**
- ~95% of enterprise GenAI pilots show no measurable P&L return; only ~5% achieve rapid revenue acceleration. (cited from [12])
- Buying AI from specialized vendors succeeds ~67% of the time; internal builds succeed roughly one-third as often. (cited from [12])
- The core barrier is a "learning gap" (systems don't retain feedback/adapt), not infrastructure or talent. (cited from [12])

**Data points:**
- 95%: enterprise GenAI pilots with no measurable P&L impact.
- ~5%: pilots achieving rapid revenue acceleration.
- $30-40B: estimated enterprise GenAI spend over the period (per syndicated coverage).
- Methodology: ~150 leader interviews, ~350-employee survey (153 senior-leader responses cited elsewhere), 300+ public AI deployments analyzed; Jan-June 2025.
- 67% vs ~33%: buy-vs-build pilot success rates.
