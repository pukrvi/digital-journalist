# Master Dossier: The AI cost reckoning — does replacing workers with AI actually save money?

**Topic:** The AI cost reckoning: does replacing workers with AI actually save money?
**Angle:** The economics of AI-for-labor substitution — unit costs, token/usage-based pricing, and whether the savings math actually holds once flat-rate subsidies end. Unifies three framings: (a) AI costs bursting the cheap-replacement bubble, (b) job-apocalypse fears, (c) AI-as-workflow-optimizer saving millions.
**Audience:** General business reader (Atlantic/Bloomberg style — smart non-specialist).
**Stance:** Neutral referee — no house thesis; weigh both sides; let the evidence decide.
**Timestamp:** 2026-05-29
**Companion piece note:** The SAME dossier feeds a second article on the "AI job apocalypse" fear — the labor/jobs dimension is researched broadly here, not only the cost angle.

*Consolidated from 8 research lenses (mainstream, contrarian, data, stakeholders, expert, follow-the-money, historical, comparative) + the commissioning seed LinkedIn post. Every entry carries a source. Sources appearing in multiple lenses are deduplicated below with all lenses noted.*

---

## 1. Executive synthesis (holistic knowledge)

1. **All three named seed claims are confirmed in substance, but the headline dollar/adoption figures are contaminated by aggregation drift.** (a) Microsoft is winding down internal Claude Code licenses in its Experiences + Devices division by June 30, 2026, redirecting engineers to GitHub Copilot CLI — a *standardization/competitive* move (Anthropic models remain available *through* Copilot CLI), not a verdict that "Claude Code didn't save money." (b) Uber exhausted its entire 2026 AI *coding-tools* budget in four months, with President & COO Andrew Macdonald publicly questioning the ROI. (c) GitHub Copilot moves to usage-based "AI Credits" on June 1, 2026 — confirmed by GitHub's own blog and docs. **CRITICAL UNRESOLVED CONFLICT inside this dossier:** the lenses disagree on whether the "~5,000 engineers / 32%→84% adoption / $150–$2,000 per engineer/month / CTO burned $1,200 in a 2-hr demo / ~70% AI code" cluster is verified. See §6 and the per-source notes — treat these figures as **contested**.

2. **The pricing shift is real and the vendors' own language confirms the "cloud-infra, not SaaS" mechanism.** GitHub's stated rationale — "a quick chat question and a multi-hour autonomous coding session can cost the user the same amount… the current premium request model is no longer sustainable" — is first-party confirmation that coding agents bill like metered compute. Stanford's Digital Economy Lab supplies the academic "why": agentic coding consumes up to ~1000x more tokens than chat, varies up to 30x run-to-run on identical tasks, and models cannot predict their own token spend (correlation ≤0.39).

3. **The deflation counter-argument is strong, large, and partly structural — not purely subsidy.** Three independent sources converge on ~1–3 orders of magnitude/year of per-token price decline at fixed capability: Epoch AI (9x–900x/yr, median ~50x), a16z's "LLMflation" (~10x/yr; GPT-3-class $60→$0.06/Mtok = 1,000x in 3 yrs), and Stanford HAI's AI Index (GPT-3.5-class $20→$0.07/Mtok ≈ 280x). DeepSeek's permanent V4-Pro cut (~90–95% below OpenAI/Anthropic) is framed by named analysts as "an efficiency gain being passed through… permanent rather than promotional." This is the strongest case that the reckoning is temporary.

4. **But per-token deflation is necessary, not sufficient — the relevant unit is cost-per-accepted-outcome.** Tokens-consumed-per-task is exploding faster, in places, than price is falling; the model-token invoice is reportedly only 20–40% of true all-in AI cost (the rest is orchestration, retries, idle compute, oversight, incident response). Net direction of cost-per-useful-outcome is genuinely workflow-dependent — the honest answer is "it depends," which the article must own rather than dodge.

5. **The ROI evidence cuts against the cheap-replacement thesis on BOTH sides.** Gartner (n=350 execs at $1B+ firms, Q3 2025): ~80% cut workforce after AI, with **no correlation** between layoffs and ROI; "people amplification" beats replacement. MIT NANDA: ~95% of enterprise GenAI pilots show no measurable P&L return — though this stat is methodologically contested (named critic Paul Roetzer: "not a viable, statistically valid thing"). Forrester forecasts >half of AI-attributed layoffs get quietly reversed and names "AI washing." Two rival research firms (Gartner, Forrester) plus a Nobel economist (Acemoglu, ~1.1–1.6% GDP over a decade) independently land on "augment, don't replace."

6. **The narrow-substitution savings case is real but conditional.** Klarna's AI assistant did the work of ~700 FTE agents (2.3M conversations month one, $40M estimated 2024 profit improvement) — then Klarna re-added humans for complex cases by May 2025 ("lower quality," CEO admitted). JPMorgan attaches ~$1.5B in AI "business value." The pattern across every sector: substitution wins for high-volume, low-variance, error-tolerant tasks where the human baseline is expensive AND you route to the cheapest adequate model; it backfires on variable, high-context, reputationally-loaded work. The winning endpoint is hybrid — and the human layer you can't remove is what undercuts pure unit-cost claims.

7. **Follow-the-money: every narrative has a paid beneficiary, which should discount all of them.** Both AI-lab CEOs (Altman, Amodei) walked back their "jobs apocalypse" warnings in mid-2026 within weeks of reportedly preparing ~$900B–$1T IPOs ("catastrophism is bad prospectus material"). Consultancies (BCG ~$3.6B/25% of revenue from AI; McKinsey) sell BOTH layoff-automation AND reskilling. A whole "FinOps for AI" vendor class (CloudZero $56M Series C; FinOps Foundation reports 98% of teams now manage AI spend, up from 31% in 2024) monetizes the cost panic itself. Nvidia (Huang/Catanzaro) sells the compute and argues heavy token spend is correct ("a $500k engineer should burn ~$250k/yr in tokens").

8. **History says this is a recognizable pattern, not a novelty — and the precedent cuts both ways.** The "cheap-then-metered" arc is the default trajectory of every compute utility (AWS 2006 → cloud FinOps 2019); AI-FinOps is that arc one layer up, in fast-forward. The offshoring precedent (advertised ~80% savings, realized ~20% after hidden costs) is the template for AI's "hidden cost stack." The ATM/teller fable (automation grew teller jobs — until ~2010, when mobile reversed it) warns against extrapolating early augmentation. Carlota Perez (installation-vs-deployment) and the Solow Productivity Paradox both support the steelman that "no measured ROI yet" may be diffusion lag, not proof the savings aren't real.

---

## 2. The spectrum of views

### Mainstream / establishment
**Claim:** By mid-2026 the business press converged on "the AI subsidy era is ending and AI-for-labor may cost more than the labor it replaces" (Fortune's May 22 headline: *"Using the tech is more expensive than paying human employees"*). The flat-fee→token shift is now consensus, not contrarian.
**Holders:** Fortune (Jake Angelo), Tom's Hardware, Tom's Guide, Visual Studio Magazine; GitHub itself (first-party).
**Strongest evidence:** GitHub's own first-party rationale for metering ("no longer sustainable"); on-record executive doubt (Uber's Macdonald, Nvidia's Catanzaro); the pricing change is a documented fact with a date (June 1, 2026).
**Weakest point:** The same mainstream coverage already carries the deflation counter-curve (Gartner: ~90% cheaper inference by 2030) and the demand-explosion curve (Goldman: 24× tokens by 2030) side by side — so even the honest mainstream position is "net direction depends on the workflow," not a settled verdict. The most viral figures (Uber per-engineer cluster) degraded through aggregation.

### Contrarian / dissenting (steelmanned — mandatory lens)
**Claim:** The bears are wrong on two fronts: (1) the "cost reckoning" is a temporary subsidy-unwind that token-price deflation will erase; (2) AI-for-labor substitution genuinely DOES save money where deployed narrowly.
**Holders:** a16z (Guido Appenzeller, "LLMflation"); analysts Sanchit Vir Gogia / Neil Shah / Amit Jaju (on DeepSeek); Satya Nadella & Demis Hassabis (Jevons paradox); Bain, JPMorgan; Klarna's original launch data.
**Strongest evidence:** Three independent sources confirm ~1–3 orders of magnitude/year deflation at fixed capability, driven by quantization, smaller models, better GPUs, and open-weight competition (NOT primarily VC burn). DeepSeek's cut is "permanent rather than promotional." Klarna's ~700-FTE-equivalent + $40M and JPMorgan's ~$1.5B are real, large, primary-sourced numbers. The Dallas Fed (Tier 1) finds wages *rising* in AI-exposed sectors — inconsistent with simple replacement. Anthropic Economic Index: 57% augmentation vs 43% automation.
**Weakest point:** The bull must concede that per-*token* deflation ≠ per-*outcome* deflation; agentic workflows consume vastly more tokens, and ~60–80% of true AI cost is non-token. Even Epoch flags that the fastest declines (900x/yr) only began after Jan 2024 and "it's less clear that those will persist." Klarna itself reversed. Klarna/JPMorgan figures blend cost-avoidance + revenue uplift, not net-of-AI-cost savings.

### Data / empirical
**Claim:** Both things are true at once — per-token prices collapse WHILE tokens-per-task explode. The canonical "not cheap enough" anchor (MIT FutureTech: only 23% of vision-task wages economically attractive to automate) predates the price collapse and is vision-only. ROI evidence is genuinely weak (Gartner ~80%/no-correlation; MIT NANDA 95% no return). Prices also rise where billed as software (AI uplifts 20–37%).
**Holders:** Epoch AI, MIT FutureTech (Thompson et al.), Stanford Digital Economy Lab (Brynjolfsson/Pentland/Pei), Gartner, Stanford HAI, MIT NANDA; vendor-sourced inflation data (Tropic, Vertice, NavyaAI).
**Strongest evidence:** The deflation curve is over-determined (Epoch + a16z + Stanford HAI agree). The Stanford agentic-token paper is peer-grade and supplies the causal mechanism (1000x, 30x variance, ≤0.39 self-prediction).
**Weakest point:** The corpus skews Tier 1 on deflation but Tier 3 (vendors selling the fix) on the inflation/FinOps side — the 20–37% and "bills tripled 3x" figures are vendor-sourced with undisclosed sample sizes. MIT NANDA's 95% measures a high bar (rapid P&L acceleration) and is methodologically contested.

### Stakeholders (lived experience)
**Claim:** The economics are felt as (a) "tokenmaxxing" leaderboard pressure (a Goodhart's-Law metric failure), (b) shock individual/team bills, (c) the "boomerang" rehiring of laid-off workers, and (d) CFOs blind-sided by surprise invoices their tools don't even watch.
**Holders:** Gergely Orosz (Pragmatic Engineer), Fortune, FT/Tom's Hardware, Meta CTO Bosworth, Brian Merchant (displaced-worker voices), Klarna CEO, HR Executive, Finout/CFO.com.
**Strongest evidence:** Meta's "Claudeonomics" leaderboard (85,000 employees, 60.2T tokens/30 days, top user ~281B tokens) is corroborated by Fortune + The Information; the $6,000-overnight-loop and $30,141 Bedrock incidents are concrete; Klarna's reversal is on-record.
**Weakest point:** The most lurid figures (one Meta engineer "$500K/month / ~300B tokens"; "low-usage employees faced layoff risk") are single-sourced to one X user and must be treated as unverified. Displaced-worker testimonies (Merchant) are labor-sympathetic and mostly anonymized.

### Expert (named analysts & academics)
**Claim:** The near-term payoff is real but modest, and headcount-cutting is NOT where the ROI is. "AI FinOps" is a real named discipline. The productivity-positive/budget-negative paradox has credible voices on both sides.
**Holders:** Gartner (Helen Poitevin), Forrester (J.P. Gownder), Stanford (Pei/Brynjolfsson/Pentland), Daron Acemoglu (MIT, Nobel), FinOps Foundation, Nvidia (Huang/Catanzaro), Paul Roetzer (critic of the 95% stat), BCG Henderson Institute.
**Strongest evidence:** Two commercial rivals (Gartner, Forrester) plus a Nobel academic independently converge on "amplify, don't replace." Stanford supplies the causal cost mechanism. The FinOps Foundation's "FinOps for AI" framework (named enterprise practitioners) proves the discipline is institutional, not a buzzword.
**Weakest point:** Conflict-of-interest map is dense — Gartner/Forrester sell advisory (favor "transform, don't just cut"); Nvidia sells compute (favors heavy spend); FinOps/cost vendors dramatize cost risk; Acemoglu is openly AI-skeptical (steelman counter: Goldman's 7%/$7T). The doom data (MIT 95%) is contested.

### Follow-the-money (incentives)
**Claim:** Every narrative has a paid beneficiary. "Cut headcount" benefits the CEO's investor story; "reskill/reshape" benefits consultancies; "control your tokens" benefits model vendors (needing IPO revenue) AND the new AI-FinOps vendor class. The Altman/Amodei walkback timing tracks IPO incentives, not new evidence.
**Holders:** Fortune, Future Forwarded (Dodson), The Information (via aggregators), MindStudio/SemiAnalysis, BCG, McKinsey/Fast Company, CloudZero, FinOps Foundation.
**Strongest evidence:** Vendor inference margins (Anthropic ~38%→70%; OpenAI fell 40%→33% as inference hit $8.4B) show headroom to keep subsidizing pre-IPO then raise prices. BCG's ~$3.6B AI revenue and McKinsey's ~10% cuts document the consultancy double-dip. 98% of FinOps teams now manage AI spend (up from 31% in 2024).
**Weakest point:** Timing/incentive correlation is suggestive, not proof of insincerity; the walkbacks could be genuine updating on evidence. Margin figures trace to paywalled The Information via aggregators (Tier 3). IPO valuations are pre-listing estimates spanning ~$900B–$1T.

### Historical (precedent & path-dependence)
**Claim:** The "cheap-then-metered" arc, the offshoring "hidden cost" gap, the ATM/teller fable, RPA's unsubstantiated savings, and the Solow/Perez frameworks all show this is a recognizable pattern — and the precedents cut both ways.
**Holders:** James Bessen (ATM/teller), GSA Inspector General (RPA audit), EY (RPA failure rates), Stephanie Overby/CIO.com (offshoring), Carlota Perez, Robert Solow/Brookings, FinOps Foundation, Marc Andreessen + Altman (AI-washing).
**Strongest evidence:** The GSA OIG audit is a Tier-1 government finding that a flagship automation program's claimed "240,000 hours saved" was "inaccurate and unreliable" because it never tracked bot costs — a near-perfect rhyme with Gartner's "no correlation." The offshoring 80%→20% gap is the template for AI's hidden-cost stack. AWS→FinOps lineage is documented by the discipline's own body.
**Weakest point:** Several anchor quotes (Bessen IMF, AEI, Flexera) were 403-blocked and captured via secondary extracts — flagged for verbatim re-check. The ATM analogy is time-bounded (reversed post-2010). Perez/Solow support BOTH a "this is normal shakeout" read AND a "payoff was delayed and uneven" caution.

### Comparative (sector-by-sector + international)
**Claim:** Substitution succeeds/fails along ONE axis — task variability/exception density. The winning endpoint is hybrid (the expensive part). AI-FinOps is cloud-FinOps in fast-forward. And "AI is cheaper than a worker" is implicitly a *Western-wage* claim.
**Holders:** METR (RCT), CodeRabbit (+ The Register), Klarna, InfoWorld (Mungel), IMF & ILO (Philippines), IBPAP/Inquirer, FinOps Foundation, WorkfxAI/CMSWire (sector stats).
**Strongest evidence:** The METR RCT (Tier 1) found experienced devs 19% *slower* with AI while believing they were 20% faster — the single most important "does it actually save money" counter-data point. CodeRabbit (cross-confirmed): AI PRs carry ~1.7x more issues. IMF/ILO show the Philippines (most AI-exposed economy by sector) saw +4% BPO employment in 2025 — "flesh beats AI economics" where labor is cheap.
**Weakest point:** Several sector percentages come from vendor compilations (Tier 4) used only directionally. The METR result is explicitly narrow (experienced OSS devs on mature repos) and the authors caution against over-generalizing. Some BPO layoff tallies attributed to "AI" are AI-washing candidates.

---

## 3. Quote bank (grouped by theme; exact verbatim)

### A. The mainstream "AI costs more than employees" thesis
> "the cost of adoption is proving a stubborn bottleneck. These developments also suggest that the economics of replacing or augmenting human labor with AI may be more complicated than some early forecasts originally implied." — Jake Angelo, Fortune, 2026-05-22 [tier 2] (https://fortune.com/2026/05/22/microsoft-ai-cost-problem-tokens-agents/)

> "For my team, the cost of compute is far beyond the costs of the employees." — Bryan Catanzaro, VP of Applied Deep Learning Research, Nvidia, quoted in Fortune, 2026-05-22 [tier 2] (https://fortune.com/2026/05/22/microsoft-ai-cost-problem-tokens-agents/) [also via Tom's Hardware, 2026-04-30]

> "Chief Product Officers (CPOs) should not confuse the deflation of commodity tokens with the democratization of frontier reasoning." — Gartner, quoted in Fortune, 2026-05-22 [tier 2] (https://fortune.com/2026/05/22/microsoft-ai-cost-problem-tokens-agents/)

> "with a token-based pricing system, the work gets more expensive with more use and better efficiency… cheaper tokens won't translate to cheaper enterprise AI because agentic models require far more tokens per task." — Fortune, 2026-05-22 [tier 2] (https://fortune.com/2026/05/22/microsoft-ai-cost-problem-tokens-agents/)

### B. The pricing shift — vendors' own framing ("cloud-infra, not SaaS")
> "Agentic usage is becoming the default, and it brings significantly higher compute and inference demands." — Mario Rodriguez, Chief Product Officer, GitHub Blog, 2026-04-27 [tier 1] (https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)

> "Today, a quick chat question and a multi-hour autonomous coding session can cost the user the same amount. GitHub has absorbed much of the escalating inference cost behind that usage, but the current premium request model is no longer sustainable." — GitHub Blog (Mario Rodriguez), 2026-04-27 [tier 1] (https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)

> "Starting June 1, premium request units (PRUs) will be replaced by GitHub AI Credits. Credits will be consumed based on token usage, including input, output, and cached tokens, according to the published API rates for each model." — GitHub Blog, 2026-04-27 [tier 1] (https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)

> "We see a future where intelligence is a utility, like electricity or water, and people buy it from us on a meter." — Sam Altman, OpenAI CEO, BlackRock 2026 Infrastructure Summit, Washington D.C., 2026-03-11 [tier 3] (https://www.tomsguide.com/ai/people-will-buy-intelligence-from-us-on-a-meter-chatgpts-ceo-sam-altman-has-critics-worried-with-his-ai-vision)

> "You will get less, but pay the same price." — developer reaction to GitHub Copilot usage-based billing, headlined by Visual Studio Magazine, 2026-04-27 [tier 3] (https://visualstudiomagazine.com/articles/2026/04/27/devs-sound-off-on-usage-based-copilot-pricing-change-you-will-get-less-but-pay-the-same-price.aspx)

> "request-based billing was easier to understand because developers could predict how much work they could get from a plan before hitting limits… token-based billing makes usage harder to predict because a request's cost depends on the prompt, tools, files, model and output." — summarized developer concerns, GitHub Community thread #192948 / Visual Studio Magazine, 2026 [tier 3]

### C. The Uber ROI doubt (the buyer-side skepticism)
> "That link is not there yet." — Andrew Macdonald, President & COO, Uber, on the connection between AI tool usage stats and useful output, via Fortune, 2026-05-26 [tier 2] (https://fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/)

> "Maybe implicitly there's more that is getting shipped, but it's very hard to draw a line between one of those stats and 'Okay now we're actually producing like 25% more useful consumer features.'" — Andrew Macdonald, Uber, 2026-05-26 [tier 2] (https://fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/)

> "If you're not actually able to draw a direct line to how [many] useful features and functionality you're shipping to your users, that trade becomes harder to justify." — Andrew Macdonald, Uber, 2026-05-26 [tier 2] (https://fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/)

### D. The bull case — deflation is real and structural
> "The rate of decline varies dramatically depending on the performance milestone, ranging from 9x to 900x per year." — Epoch AI, 2025-03-12 [tier 1] (https://epoch.ai/data-insights/llm-inference-price-trends)

> "The fastest trends (e.g. 900x per year) start after January 2024 ... The fastest price drops in that range have occurred in the past year, so it's less clear that those will persist." — Epoch AI, 2025-03-12 [tier 1] (https://epoch.ai/data-insights/llm-inference-price-trends)

> "For an LLM of equivalent performance, the cost is decreasing by 10x every year." — Guido Appenzeller, a16z, 2024-11-12 [tier 3] (https://a16z.com/llmflation-llm-inference-cost/)

> "while the cost of LLM inference will likely continue to decrease, its rate may slow down" — Guido Appenzeller, a16z, 2024-11-12 [tier 3] (https://a16z.com/llmflation-llm-inference-cost/)

> "It is not a discount. It is an efficiency gain being passed through... V4-Pro was engineered to cut the cost of long-context inference... This is why the price cut is permanent rather than promotional." — Sanchit Vir Gogia, Greyhound Research, in InfoWorld, 2026-05-25 [tier 2] (https://www.infoworld.com/article/4176709/deepseeks-steep-v4-pro-price-cut-escalates-ai-pricing-war.html)

> "high-margin, high-consumption token pricing models from Anthropic and OpenAI are becoming harder to justify for many enterprise workloads." — Neil Shah, Counterpoint Research, in InfoWorld, 2026-05-25 [tier 2] (https://www.infoworld.com/article/4176709/deepseeks-steep-v4-pro-price-cut-escalates-ai-pricing-war.html)

> "If a CIO can host DeepSeek V4-Pro on their own infrastructure, inference costs drop dramatically, and many projects that were previously uneconomical at scale become viable." — Amit Jaju, Ankura Consulting, in InfoWorld, 2026-05-25 [tier 2] (https://www.infoworld.com/article/4176709/deepseeks-steep-v4-pro-price-cut-escalates-ai-pricing-war.html)

> "Jevons paradox strikes again! As AI gets more efficient and accessible, we will see its use skyrocket, turning it into a commodity we just can't get enough of." — Satya Nadella, CEO, Microsoft, 2025-01-27 (X) [tier 4 for tweet / tier 2 for GeekWire context] (https://x.com/satyanadella/status/1883753899255046301)

> "When SemiAnalysis reported Anthropic's margins at 38% last year, it meant compute was eating 62 cents of every dollar. At 70%, compute costs have dropped to 30 cents on the dollar." — MindStudio, 2026-05-07 (attributing figures to SemiAnalysis) [tier 3] (https://www.mindstudio.ai/blog/anthropic-inference-margins-70-percent-api-costs)

### E. The bull case — narrow substitution savings are real
> "The AI assistant has had 2.3 million conversations, two-thirds of Klarna's customer service chats... It is doing the equivalent work of 700 full-time agents... It is on par with human agents in regard to customer satisfaction score... leading to a 25% drop in repeat inquiries... Customers now resolve their errands in less than 2 mins compared to 11 mins previously... It's estimated to drive a $40 million USD in profit improvement to Klarna in 2024." — Klarna press release, 2024-02-27 [tier 4 interpretation / tier-2-equiv raw figures] (https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/)

> "The returns to frontier intelligence are extremely high... Customers see that, and then they invest really heavily in more tokens with the newer models." — Krishna Rao, CFO, Anthropic, via CFO.com, 2026-05-28 [tier 2] (https://www.cfo.com/news/claude-finance-price-pricing-raises-new-budgeting-questions-for-cfo/821266/)

> "If that $500,000 engineer did not consume at least $250,000 worth of tokens, I am going to be deeply alarmed." — Jensen Huang, CEO, Nvidia, GTC 2026 (All-In Podcast), reported 2026-03-20 [tier 2] (https://www.cnbc.com/2026/03/20/nvidia-ai-agents-tokens-human-workers-engineer-jobs-unemployment-jensen-huang.html)

> "Companies now monitor when—not if—the use of AI will generate value across the board." — Bain & Company, July 2024 [tier 2-3] (https://www.bain.com/insights/ai-in-financial-services-survey-shows-productivity-gains-across-the-board/)

### F. The ROI skeptic case (cuts against cheap-replacement)
> "There's no connection or correlation between people who are achieving ROI and layoffs." — Helen Poitevin, Distinguished VP Analyst, Gartner, via Computerworld, 2026-05 [tier 2] (https://www.computerworld.com/article/4167140/ai-led-job-cuts-dont-always-mean-stronger-roi-gartner.html)

> "Workforce reductions may create budget room, but they do not create return. Organizations that improve ROI are not those that eliminate the need for people, but those that amplify them by aggressively investing more in skills, roles and operating models that allow humans to guide and scale autonomous systems." — Helen Poitevin, Gartner press release, 2026-05-05 [tier 1] (https://www.gartner.com/en/newsroom/press-releases/2026-05-05-gartner-says-autonomous-business-and-artificial-intelligence-layoffs-may-create-budget-room-but-do-not-deliver-returns)

> "Looking only at layoffs is shortsighted in terms of getting value from AI. Chasing value only through headcount reduction is likely to lead most organizations down a path of limited returns." — Helen Poitevin, Gartner, via Fortune, 2026-05-11 [tier 2] (https://fortune.com/2026/05/11/ai-automation-layoffs-gartner-study-roi/)

> "AI is not leading to a jobs apocalypse, but it's unleashing job chaos, changing the shape of what people do." — Helen Poitevin, Gartner, via Computerworld, 2026-05 [tier 2] (https://www.computerworld.com/article/4167140/ai-led-job-cuts-dont-always-mean-stronger-roi-gartner.html)

> 95% of generative AI pilot programs deliver "little to no measurable impact on P&L." — MIT NANDA, *State of AI in Business 2025*, 2025-08-18 [tier 2] (https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf)

> "Please don't put any weight into this study. This is not a viable, statistically valid thing." — Paul Roetzer, CEO, Marketing AI Institute, on the MIT 95% stat, 2025-08-26 [tier 3] (https://www.marketingaiinstitute.com/blog/mit-study-ai-pilots)

> AI will have a "nontrivial, but modest" effect on GDP over the next decade. — Daron Acemoglu, MIT (2024 Nobel laureate), as summarized by MIT Sloan / MIT Technology Review [tier 1] (https://www.nber.org/papers/w32487)

### G. The unit-economics / FinOps mechanism (why bills run away)
> "Agents are not capable of predicting their own token costs. This is the fundamental bottleneck for result-based pricing for agents." — Jiaxin Pei, Stanford Digital Economy Lab, 2026-05-05 [tier 1] (https://digitaleconomy.stanford.edu/news/how-are-ai-agents-spending-your-tokens/)

> "Agentic tasks consume 1000x more tokens than code reasoning and code chat" — Bai et al., arXiv 2604.22750 (Stanford Digital Economy Lab / Microsoft Research), 2026 [tier 1] (https://arxiv.org/abs/2604.22750)

> "Ship an AI agent without loop limits and cost guardrails, and your cloud bill becomes the real product demo." — Nikhil Mungel, InfoWorld, 2026-03-02 [tier 2] (https://www.infoworld.com/article/4138748/finops-for-agents-loop-limits-tool-call-caps-and-the-new-unit-economics-of-agentic-saas.html)

> "In agentic SaaS, cost is a reliability metric. Loop limits and tool-call caps protect your margin." — Nikhil Mungel, InfoWorld, 2026-03-02 [tier 2] (https://www.infoworld.com/article/4138748/finops-for-agents-loop-limits-tool-call-caps-and-the-new-unit-economics-of-agentic-saas.html)

> "I have watched two customers with the same licenses generate a 10X difference in inference and tool costs because one had standardized workflows and the other lived in exceptions." — Nikhil Mungel, InfoWorld, 2026-03-02 [tier 2] (https://www.infoworld.com/article/4138748/finops-for-agents-loop-limits-tool-call-caps-and-the-new-unit-economics-of-agentic-saas.html)

> "Token prices fell 99.7%, yet average monthly AI invoices tripled" — NavyaAI, 2026-02 [tier 3] (https://navyaai.com/reports/ai-cost-report-token-prices-vs-ai-bill)

> "Regularly track and review AI costs and usage, set quotas, tag resources, and optimize GPU allocation to tightly control AI spending. Train teams on FinOps best practices for AI and align real-time financial monitoring to business outcomes for continuous improvement." — FinOps Foundation, "FinOps for AI Overview," 2025–2026 [tier 1-2] (https://www.finops.org/wg/finops-for-ai-overview/)

> "headcount-based chargeback distorts the cost signal because individual developers consume agent capacity at materially different rates." — Finout, 2026-04-27 [tier 3] (https://www.finout.io/blog/finops-for-ai-agents-a-four-step-allocation-framework)

### H. Tokenmaxxing (Goodhart's-Law stakeholder voices)
> "I am conscious of not wanting to be seen as 'uses too little AI,' and I'm not ashamed to say I need to do tokenmaxxing to do this." — anonymous Microsoft engineer, via Gergely Orosz, The Pragmatic Engineer, 2026-04-23 [tier 3] (https://blog.pragmaticengineer.com/the-pulse-tokenmaxxing-as-a-weird-new-trend/)

> "Ask AI questions about the code already in the documentation... I could use 'readthedocs,' but then my token numbers would be lower." — anonymous Microsoft engineer, via The Pragmatic Engineer, 2026-04-23 [tier 3] (https://blog.pragmaticengineer.com/the-pulse-tokenmaxxing-as-a-weird-new-trend/)

> "Default to always using the agent, even when I know I could do the work by hand much faster." — anonymous Microsoft engineer, via The Pragmatic Engineer, 2026-04-23 [tier 3] (https://blog.pragmaticengineer.com/the-pulse-tokenmaxxing-as-a-weird-new-trend/)

> "the equivalent of his salary in tokens, but he's '5x to 10x more productive.' ... It's like, this is easy money. Keep doing it. No limit." — Andrew Bosworth, CTO, Meta, describing his top engineer's token spend, via Fortune, 2026-04-09 [tier 2] (https://fortune.com/2026/04/09/meta-killed-employee-ai-token-dashboard/)

> "so much pressure to use these tools" / "perverse incentives" — anonymous Amazon workers, via FT/Tom's Hardware, 2026-05-12 [tier 2] (https://www.tomshardware.com/tech-industry/big-tech/big-tech-has-a-tokenmaxxing-habit)

### I. The reversal / boomerang (human face of the ROI reckoning)
> "From a brand perspective, a company perspective, I just think it's so critical that you are clear to your customer that there will always be a human if you want." — Sebastian Siemiatkowski, CEO, Klarna, via Entrepreneur/Bloomberg, 2025-05-09 [tier 2-3] (https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396)

> "Really, investing in the quality of human support is the way of the future for us." — Sebastian Siemiatkowski, Klarna, via Entrepreneur, 2025-05-09 [tier 2-3] (https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396)

> "When we ask if they have a mature, vetted AI app ready to fill in those jobs, 9 out of 10 times, the answer is no — and they haven't even started." — J.P. Gownder, VP & Principal Analyst, Forrester, via HR Executive, 2026-04-21 [tier 2] (https://hrexecutive.com/as-ai-layoff-regret-surges-will-boomerang-employees-make-a-comeback/)

> "over half of layoffs attributed to AI will be quietly reversed as companies realize the operational challenges of replacing human talent prematurely" — Forrester, 2026-01-13 [tier 1] (https://www.forrester.com/press-newsroom/forrester-impact-ai-jobs-forecast/)

> "Many companies announcing AI-related layoffs do not have mature, vetted AI applications ready to fill those roles, highlighting a trend of 'AI washing' — attributing financially motivated cuts to future AI implementation." — Forrester, 2026-01-13 [tier 1] (https://www.forrester.com/press-newsroom/forrester-impact-ai-jobs-forecast/)

> "I was forced to use AI until the day I was laid off." — anonymous corporate content copywriter, via Brian Merchant, Blood in the Machine, 2025-12-12 [tier 3] (https://www.bloodinthemachine.com/p/i-was-forced-to-use-ai-until-the)

> "I was actually let go the week before Thanksgiving now that the AI was good enough." — Jacques Reulet II, former head of support operations who had trained the chatbots that replaced his team, via Blood in the Machine, 2025-12-12 [tier 3] (https://www.bloodinthemachine.com/p/i-was-forced-to-use-ai-until-the)

> "At our peak... we went from making something like $600,000 a year and employing 8 people... To making less than $10K in 2025." — Marcus Wiesner, business copywriter / agency owner, via Blood in the Machine, 2025-12-12 [tier 3] (https://www.bloodinthemachine.com/p/i-was-forced-to-use-ai-until-the)

### J. Follow-the-money — the walkback and AI-washing
> "I'm delighted to be wrong about this." — Sam Altman, OpenAI CEO, quoted in Fortune, 2026-05-26 [tier 2] (https://fortune.com/2026/05/26/sam-altman-dario-amodei-walking-back-ai-jobs-apocalypse-prophecies-ipo/)

> "I thought there would have been more impact on entry-level white-collar jobs being eliminated by now than has actually happened." — Sam Altman, quoted in Fortune, 2026-05-26 [tier 2] (https://fortune.com/2026/05/26/sam-altman-dario-amodei-walking-back-ai-jobs-apocalypse-prophecies-ipo/)

> "Companies preparing to sell shares to the public have a compelling reason to stop telling potential investors that the technology at the core of their business is a threat to social stability." — William R. Dodson, Future Forwarded, 2026-05 [tier 3] (https://futureforwarded.substack.com/p/billionaires-backpedal-on-the-ai)

> "Catastrophism is bad marketing. It's also bad prospectus material." — William R. Dodson, Future Forwarded, 2026-05 [tier 3] (https://futureforwarded.substack.com/p/billionaires-backpedal-on-the-ai)

> "This entire labor displacement thing is 100% incorrect. It's completely wrong." — Marc Andreessen, 20VC podcast, via a16z, 2026 [tier 4] (https://x.com/a16z/status/2038760847473009083)

> "Now they all have the silver bullet excuse: Ah, it's AI." — Marc Andreessen, reported by Fortune, 2026-03-31 [tier 2] (https://fortune.com/2026/03/31/marc-andreessen-ai-layoffs-silver-bullet-excuse-overhiring/)

> [Reported survey finding] "Nearly 60 percent [of US hiring managers] said they emphasize AI's role in reducing hiring or cutting jobs because it's viewed more favorably than financial constraints." — survey reporting via Built In / SHRM coverage, 2026 [tier 3-4]

> "AI is redefining what's possible — but without a deep understanding of cloud unit economics, innovation becomes unsustainable." — Phil Pergola, CEO, CloudZero, 2025-05-28 [tier 3] (https://www.cloudzero.com/press-releases/20250528/)

### K. The labor/jobs dimension (for the companion piece)
> "Early data on employment and wages in AI-affected industries suggest it may be doing both [automating and augmenting]." — Federal Reserve Bank of Dallas, 2026-02-24 [tier 1] (https://www.dallasfed.org/research/economics/2026/0224)

> "AI can substitute for entry-level workers—new graduates with book-learning but no experience—and at the same time complement experienced workers, who have tacit knowledge that cannot be replicated by AI." — Dallas Fed, 2026-02-24 [tier 1] (https://www.dallasfed.org/research/economics/2026/0224)

> "We may not be heading for an imminent AI job apocalypse, but how organizations handle AI today will define more than just their future success... treating AI not as a replacement for human talent but as a tool to enhance it." — J.P. Gownder, Forrester, 2026-01-13 [tier 1] (https://www.forrester.com/press-newsroom/forrester-impact-ai-jobs-forecast/)

> "The augmentation of existing roles and the creation of new ones will proceed rapidly, but full job replacement by AI will progress more slowly." — BCG Henderson Institute, 2026-04 [tier 2] (https://www.bcg.com/publications/2026/ai-will-reshape-more-jobs-than-it-replaces)

> "exposure does not equate necessarily to full job replacement but rather the automation of tasks within occupations." — Phu Huynh, ILO, 2026-02-05 [tier 1] (https://www.ilo.org/publications/generative-ai-and-jobs-philippines-labour-market-exposure-and-policy)

### L. The comparative keystone — felt vs measured productivity
> "When developers are allowed to use AI tools, they take 19% longer to complete issues." — Becker, Rush, Barnes & Rein, METR, 2025-07-10 [tier 1] (https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)

> "developers expected AI to speed them up by 24%" … "they still believed AI had sped them up by 20%" [despite the actual 19% slowdown]. — METR, 2025-07-10 [tier 1] (https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)

### M. Historical precedent — automation savings that didn't materialize
> "GSA's assertion ... that its RPA program reclaimed more than 240,000 work hours annually was inaccurate and unreliable." — GSA Office of Inspector General, 2023-11-30 [tier 1] (https://www.gsaig.gov/content/gsas-robotic-process-automation-program-lacks-evidence-support-claimed-savings)

> "GSA is not tracking the costs associated with its bots, which precludes GSA from determining whether the bots are generating cost savings and a return on investment." — GSA OIG, 2023-11-30 [tier 1] (https://www.gsaig.gov/content/gsas-robotic-process-automation-program-lacks-evidence-support-claimed-savings)

> "No one saves 80 percent by shipping IT work to India or any other country. Few can save even half that." — Stephanie Overby, CIO.com, 2003-09-01 [tier 2] (https://www.cio.com/article/267239/the-hidden-costs-of-offshore-outsourcing.html)

> "Someone working for $10,000 a year in Hyderabad can end up costing an American company four to eight times that amount." — Hank Zupnick, CIO, GE Real Estate, in CIO.com, 2003-09-01 [tier 2] (https://www.cio.com/article/267239/the-hidden-costs-of-offshore-outsourcing.html)

> "You can see the computer age everywhere but in the productivity statistics." — Robert Solow, 1987, quoted by Brookings, 1999-03 [tier 2] (https://www.brookings.edu/articles/the-solow-productivity-paradox-what-do-computers-do-to-productivity/)

> "The average bank branch in an urban area required about 21 tellers. That was cut because of the ATM machine to about 13 tellers. But that meant it was cheaper to operate a branch... demand for bank tellers increased." — James Bessen, quoted by AEI, c.2016 [tier 3, flagged for verbatim re-check] (https://www.aei.org/economics/what-atms-bank-tellers-rise-robots-and-jobs/)

> "We do not, contrary to what some claim, have 'more bank tellers today than we did when the ATM was created': we in fact have far fewer. The story might have been true in 2000 or 2005, but it hasn't been true for years." — David Oks, c.2023-24 [tier 3, flagged for verbatim re-check] (https://davidoks.blog/p/why-the-atm-didnt-kill-bank-teller)

---

## 4. Fact & data ledger

*Unit, "as of" date, source, tier. Items older than 3 years from the 2026-05-29 timestamp are flagged ⚠OLD (pre-2023-05).*

| Fact / figure | Value | As of | Source | Tier |
|---|---|---|---|---|
| **Pricing shift** | | | | |
| GitHub Copilot → usage-based "AI Credits" effective date | June 1, 2026 | 2026-04-27 | GitHub Blog/Docs | 1 |
| GitHub AI Credit unit value | 1 credit = $0.01 USD | 2026 | GitHub Docs (secondary-confirmed) | 1 |
| GitHub Copilot plan prices (unchanged) | Pro $10/mo; Pro+ $39/mo; Business $19/user/mo; Enterprise $39/user/mo | 2026 | GitHub Blog | 1 |
| GitHub premium-request billing began (transitional step) | 2025-06-18 | 2026 | GitHub Blog | 1 |
| Microsoft Claude Code internal wind-down deadline | June 30, 2026 (also MS FY-end) | 2026-05-15 | Windows Central / The Verge (Tom Warren) | 2-3 |
| Microsoft opened internal Claude Code access | ~Dec 2025 (~6 mo prior) | 2026-05 | Fortune / Windows Central | 2-3 |
| Claude Code programmatic usage → full API rates | effective June 15, 2026 | 2026 | follow-the-money lens | 2-3 |
| **Deflation curve (per-token)** | | | | |
| LLM inference price decline at fixed capability | 9x–900x/yr; median ~50x | 2025-03-12 | Epoch AI | 1 |
| Median decline using only post-Jan-2024 data | ~200x/yr (halving ~every 2 mo) | 2025-03-12 | Epoch AI | 1 |
| GPT-4-level decline on GPQA (PhD science) | ~40x/yr | 2025-03-12 | Epoch AI | 1 |
| GPT-3-class (MMLU 42) price | $60/Mtok (Nov 2021) → $0.06/Mtok (Nov 2024) = 1,000x ⚠ endpoints span old→recent | 2024-11-12 | a16z (Appenzeller) | 3 |
| GPT-4-class (MMLU 83) decline since Mar 2023 | ~62x | 2024-11-12 | a16z | 3 |
| Frontier "tax": o1 output price | ~$60/Mtok (= GPT-3 launch price) | 2024-11-12 | a16z | 3 |
| GPT-3.5-class (MMLU ~64-66) price | $20.00/Mtok → $0.07/Mtok ≈ 280x (~99.7%) in ~18 mo | 2025-04 | Stanford HAI AI Index 2025 | 1 |
| DeepSeek V4-Pro permanent price cut | 75% cut; ~$0.87/Mtok output; ~$0.0036/Mtok cached input | 2026-05-25 | InfoWorld | 2 |
| DeepSeek V4-Pro vs OpenAI/Anthropic | ~90–95% cheaper | 2026-05 | cross-referenced (Silicon Canals/AIWeekly) | 3 |
| Self-hosting open weights vs closed APIs (opex) | ~85–95% cheaper (VERIFY) | 2026-05 | secondary tech blogs | 3-4 |
| **Token-volume explosion (the other blade)** | | | | |
| Agentic coding vs code-chat/reasoning token use | up to ~1000x more | 2026-04 | Stanford Digital Economy Lab (Bai et al., arXiv 2604.22750) | 1 |
| Run-to-run token variance, same task | up to 30x | 2026-04 | Stanford Digital Economy Lab | 1 |
| Model self-prediction of own token usage | correlation ≤0.39 | 2026-04 | Stanford Digital Economy Lab | 1 |
| Kimi-K2 / Claude-Sonnet-4.5 vs GPT-5 on same tasks | >1.5M more tokens avg | 2026-04 | Stanford Digital Economy Lab | 1 |
| Model-token invoice as share of true AI cost | only 20-40% (so ~60-80% non-token) | 2026-02 | NavyaAI | 3 |
| Token prices fell / avg monthly AI bill | -99.7% / ~3x (tripled) | 2026-02 | NavyaAI | 3 |
| Goldman Sachs token-demand forecast | 24× by 2030 (~120 quadrillion tokens/mo) | 2026-05 | Fortune / Tom's Hardware | 2 |
| Gartner inference cost (1T-param LLM) by 2030 | ~90% cheaper vs 2025 | 2026-05 | Fortune (citing Gartner) | 2 |
| **The MIT cost-effectiveness anchor** | | | | |
| Vision-task worker wages economically attractive to automate (early-2024 cost) | 23% (77% NOT) | 2024-02-08 | MIT FutureTech (Svanberg/Thompson et al.) | 1 |
| **ROI evidence** | | | | |
| Orgs cutting workforce after AI pilot, with NO ROI correlation | ~80% | Q3 2025 (rel. 2026-05-05) | Gartner (n=350, $1B+ rev) | 1 |
| Gartner AI-agent software spend forecast | $206.5B (2026); $376.3B (2027) | 2026-05 | Gartner | 1 |
| Gartner projected crossover to net job creation | 2028–2029 | 2026-05 | Gartner | 1 |
| Enterprise GenAI pilots with no measurable P&L return | ~95% (only ~5% rapid revenue) | 2025-08-18 | MIT NANDA (contested) | 2 |
| MIT NANDA buy-vs-build pilot success | 67% buy vs ~33% build | 2025-08-18 | MIT NANDA | 2 |
| MIT NANDA methodology | ~52 interviews + ~300 public initiatives; 6-mo ROI window | 2025-08 | per Roetzer/Marketing AI Institute | 3 |
| Estimated enterprise GenAI spend (NANDA period) | $30-40B | 2025 | MIT NANDA (syndicated) | 2 |
| BCG: companies that are "AI leaders" | only 5%; 60% minimal/no value | 2025 | BCG via Mavvrik | 3 (verify) |
| Forbes: execs reporting ≥20% ROI uplift | <1% (53% report 1-5%) | 2025 | Forbes via Mavvrik | 3 (verify) |
| Acemoglu: AI GDP boost over 10 yrs | ~1.1-1.6% (~0.05%/yr TFP); ~5% of tasks automatable | 2024/2025 | Acemoglu, NBER w32487 / Economic Policy | 1 |
| Steelman counter: Goldman GDP boost | ~7% / ~$7 trillion over 10 yrs | 2024 | Goldman Sachs (via AEI) | 2 |
| **Bull-case savings exhibits** | | | | |
| Klarna AI = FTE-agent equivalent | ~700 agents | 2024-02-27 | Klarna press release | 4 interp / 2-equiv raw |
| Klarna AI conversations month one | 2.3M (~two-thirds / ~75% of chats) | 2024-02-27 | Klarna | 4/2-equiv |
| Klarna resolution time | 11 min → <2 min; 25% drop in repeat inquiries; CSAT parity | 2024-02-27 | Klarna | 4/2-equiv |
| Klarna estimated 2024 profit improvement | $40M | 2024-02-27 | Klarna | 4/2-equiv |
| Klarna markets / languages | 23 markets, 24/7, 35+ languages | 2024-02-27 | Klarna | 4/2-equiv |
| Klarna headcount during AI freeze | ~4,487 → ~3,500 (~22% fall); freeze >12 mo | 2025-05-09 | Entrepreneur | 2-3 |
| JPMorgan AI-attributed business value | ~$1.5B (projected $1.5-2.0B) | 2025-05-05 | Reuters (COO Daniel Pinto) | 2 |
| Bain: avg productivity gain across AI uses | ~20%; +26% completed coding tasks (RCT) | Jul 2024 | Bain (n=109 US FS firms) | 2-3 |
| Bain: avg 2024 AI spend at $5B+ firms | $22.1M (~270 FTE engaged) | Jul 2024 | Bain | 2-3 |
| **Labor / augmentation data** | | | | |
| Claude usage: augmentation vs automation | 57% augment / 43% automate | 2025-02-10 | Anthropic Economic Index | 3 |
| Occupations using AI for ≥75% / ≥25% of tasks | ~4% / ~36% | 2025-02-10 | Anthropic Economic Index | 3 |
| Computer & Mathematical share of Claude convos | 37.2% | 2025-02-10 | Anthropic Economic Index | 3 |
| Dallas Fed: computer-systems-design wages vs national since fall 2022 | +16.7% vs +7.5% | 2026-02-24 | Dallas Fed (BLS data) | 1 |
| Dallas Fed: employment in 10% most AI-exposed sectors | -1%; computer systems design -5% | 2026-02-24 | Dallas Fed | 1 |
| Forrester: US jobs automated by 2030 | ~6% (~10.4M roles); ~20% augmented over 5 yrs | 2026-01-13 | Forrester | 1 |
| Forrester: AI-attributed layoffs reversed | "over half" | 2026-01-13 | Forrester | 1 |
| Forrester: employers regretting AI layoffs | 55% | 2025-10-29 | Forrester via The Register | 2 |
| Forrester: AI-investment leads expecting headcount UP vs DOWN | 57% up / 15% down | 2025-10-29 | Forrester via The Register | 2 |
| BCG: US jobs reshaped vs eliminated | 50-55% reshaped; 10-15% (~16-25M) eliminated within 5 yrs | 2026-04 | BCG Henderson Institute (165M jobs, 1,500 roles) | 2 |
| Robert Half: companies that laid off then rehired post-AI | ~29% | 2026-04-21 | via HR Executive | 2 |
| Careerminds: HR pros rehiring AI-laid-off staff | ~two-thirds (n=600, Feb 2026) | 2026 | via HR Executive / GFMag | 2-3 |
| Orgvue: orgs that rehired post-AI-layoff | 32% | 2026 | via follow-the-money cluster | 3 |
| Layoffs attributed to AI (measured year) | 49,135 (≈ prior-year total); ~48% of 78,557 tracked through Apr 2026 | 2026 | Fortune / coverage | 2 |
| Great Place to Work adoption-perception gap | 82% exec / 48% mgr / 38% IC say "company provides AI tools" (n≈4,000, 25 countries) | 2026 | via Fortune | 2 |
| **CFO / FinOps market signals** | | | | |
| Gartner Q4 2025 CFO survey: cost optimization rank | #1 urgent action; 56% top-5 2026 priority | Q4 2025 | Gartner via Mavvrik | 3 (verify) |
| CFOs confident they can achieve meaningful AI outcomes | only 36% | Q4 2025 | Gartner via Mavvrik | 3 (verify) |
| FinOps teams managing AI spend | 98% (2026) vs 63% (2025) vs 31% (2024) | 2026 | FinOps Foundation (n=1,192, $83B+ spend) | 2 |
| FinOps "labor costs" as emerging category | 28% | 2026 | FinOps Foundation | 2 |
| **Vendor economics / IPO incentives** | | | | |
| OpenAI 2025 gross margin | 33% (down from 40% in 2024; forecast 46%) | ~2026-02 | The Information (via aggregator) | 3 |
| OpenAI 2025 inference cost | $8.4B (~4x YoY; forecast $6.6B) | ~2026-02 | The Information | 3 |
| OpenAI free vs paying user serving cost | ~$3.9B free (~95% of actives) / ~$4.5B paying (~5%) | ~2026-02 | The Information | 3 |
| Anthropic inference gross margin trajectory | -94% (2024) → ~40% (2025) → ~70% (2026) | 2026-05 | The Information / SemiAnalysis (via MindStudio) | 3 |
| OpenAI / Anthropic est. IPO valuation | ~$900B–$1T each (range across sources/dates) | 2026-05 | Fortune / Future Forwarded | 2-3 |
| Anthropic listing target (one estimate) | ~$30B raise at ~$900B, October 2026 | 2026-05 | Future Forwarded (Dodson) | 3 |
| BCG AI-consulting revenue | ~$3.6B = ~25% of $14.4B 2025 revenue | 2026-04-23 | BCG to Bloomberg (via Metaintro) | 2 |
| McKinsey workforce cut | ~10% (~3,000-4,000 roles), largest since 2008 | 2025-26 | Fast Company | 2 |
| CloudZero Series C | $56M (repositioned "The AI ROI Company") | 2025-05-28 | CloudZero PR | 3 |
| Combined 2026 capex (AMZN/MSFT/GOOG/META) | $650-700B (2027 projections >$1T) | 2026-05-12 | FT/Tom's Hardware | 2 |
| Nvidia: $500k engineer should burn in tokens/yr | ~$250k (~50% of salary) | 2026-03-20 | Huang, GTC 2026 (CNBC) | 2 |
| **Stakeholder bills / leaderboards** | | | | |
| Meta "Claudeonomics" leaderboard | 85,000+ employees; 60.2T tokens/30 days; ~$900M list (~$100M+ post-discount) | 2026-04 | Pragmatic Engineer / Fortune | 2-3 |
| Meta top single token user | ~281B tokens/mo (~$1.4M+ at Opus 4.6 rates) | 2026-04-09 | Fortune | 2 |
| Amazon weekly-AI-usage requirement | 80%+ of developers | 2026-05-12 | FT/Tom's Hardware | 2 |
| Overnight looping-agent bill (Reddit dev) | ~$6,000 | 2026 | MakeUseOf | 3 |
| Surprise Bedrock invoice (+ silent Activate credits) | $30,141.33 + $8,026.54 | 2026-05 | The Register via Finout | 2-3 |
| Gemini bill via compromised key | $0 → $10,000 in 30 min | 2026-05 | The Register via Finout | 2-3 |
| Google auto-escalated spend cap (past $1,000 lifetime) | to $100,000 | 2026-05 | The Register via Finout | 2-3 |
| Reddit dev Claude Code spend | ~$3,000/month | 2026 | stakeholders lens (Reddit, Tier 4) | 4 |
| CONTESTED: single Meta engineer token spend | ~$500K/mo / ~300B tokens | 2026-05-28 | IBTimes (one X user @sheiyuo) | 4 UNVERIFIED |
| **Comparative / sector** | | | | |
| METR RCT: experienced-dev speed with AI | -19% (slower) vs +20% perceived faster | 2025-07-10 | METR (16 devs, 246 issues, repos 22k+ stars) | 1 |
| CodeRabbit: issues in AI vs human PRs | 10.83 vs 6.45 ≈ 1.7x (n=470 PRs) | 2025-12-17 | CodeRabbit / The Register | 2-3 |
| CodeRabbit: AI-code defect skew | security up to 2.74x; performance ~8x; readability 3x; logic +75% | 2025-12-17 | CodeRabbit / The Register | 2-3 |
| InfoWorld: cost spread, identical licenses | 10x (workflow standardization vs exceptions) | 2026-03-02 | InfoWorld (Mungel) | 2 |
| AI coding tools market | ~$7.37B (2025); Copilot ~42%, Cursor ~18% | 2025 | getpanto compilation | 4 (verify) |
| Call center: AI cost-per-resolution | <$1; 65-90% unit-cost cut | 2026 | CMSWire/Pylon | 3 |
| Support queries resolved without humans | 65% (2025) vs 52% (2023) | 2026 | CMSWire | 3 |
| Companies abandoning most AI initiatives | 42% (2025) vs 17% (2024) | 2025 | CMSWire (verify primary) | 3 |
| Call centers fully operationalizing AI | only ~25% | 2026 | CMSWire | 3 |
| GenAI assist lift on resolution rate (newer agents) | +14-15% | 2026 | CMSWire (Brynjolfsson/Li/Raymond echo) | 3 |
| Marketers using AI / struggling with brand voice | 85% / 81% | 2026-03-04 | WorkfxAI compilation | 4 (directional) |
| AI vs human guideline adherence / emotional resonance | 87% vs 73% / AI = 68% of human | 2026-03-04 | WorkfxAI | 4 |
| Readers who can't distinguish AI from human content | 84% (blind tests) | 2026-03-04 | WorkfxAI | 4 |
| Philippines: workers highly AI-exposed / also complementary | ~1/3 exposed; ~60% of those complementary | 2025-02-21 | IMF WP 2025/043 | 1 |
| Philippines: jobs GenAI-exposed / at highest displacement risk | 12.7M (>25%) exposed; only 3.6% high-risk | 2026-02-05 | ILO (Huynh) | 1 |
| Philippines IT-BPM 2025 actuals | +4% employment (vs ~3% global); ~80k net new jobs; >$40B export rev | 2025 | IBPAP / Inquirer | 2 |
| Philippines BPO firms using AI for productivity | 67% | 2025 | IBPAP / Inquirer | 2 |
| **Historical precedents** | | | | |
| GSA RPA claimed savings (unsubstantiated) | "more than 240,000 work hours annually" — "inaccurate and unreliable" | 2023-11-30 | GSA OIG | 1 |
| EY: RPA projects that failed | 30-50% | 2019/2024 ⚠OLD (2019) | EY via Raconteur/ActiveBatch | 3-4 |
| RPA projects never scaling beyond 10 bots | >50% (>70% plateaued <50 bots) | 2024 | via Xenith | 3-4 |
| Offshoring: advertised vs realized savings | ~80% advertised (5:1 wage gap) vs ~20% realized | 2003-09-01 ⚠OLD | CIO.com (Overby) | 2 |
| ATM/teller: tellers per urban branch | ~21 → ~13 | 1980s-2010 ⚠OLD | Bessen via AEI | 2-3 |
| ATM era: US teller employment | ~500k → ~600k (rose); +100k since 2000; reversed post-~2010 | 1980s-2025 ⚠OLD base | Bessen/MacCarthy; Oks (reversal) | 2-3 |
| US ATMs installed | ~400,000 | 1980s-2010 ⚠OLD | Bessen/AEI | 2-3 |
| Dot-com fiber: miles laid / still dark 2005 / price fall | 80M+ miles / ~85% dark / ~90% price drop | 1990s-2005 ⚠OLD | BoxCars AI (Tabrez Syed) | 3 |
| Global Crossing Q4 2001 loss | $3.4B on $793M revenue | 2001 ⚠OLD | BoxCars AI | 3 |
| SaaS firms on usage/hybrid pricing | ~45% (2024) → ~85% of leaders / ~61% hybrid (2025) | 2024-25 | Flexera | 3 |
| SaaS price inflation | ~8.7% (2023) → ~12-13% (Mar 2026) | 2023-2026 | Vertice / CFO Dive | 3 / 2 |
| SaaS spend per employee | $7,900 (2023) → $8,700 (2024) → ~$9,100 (end 2025) | 2023-2025 | Vertice | 3 |
| SaaS vendors masking price increases | ~60% | 2026 | Vertice (n=16,000 vendors) | 3 |
| AI software price uplift on renewals | 20-37% (residual ~12% after negotiation) | 2025-12-23 | Tropic (sample undisclosed) | 3 |
| Tropic Slack example | $20/user → $45/user (forced SKU migration) | 2025-12 | Tropic | 3 |
| AWS launch | S3 2006-03-14; EC2 Aug 2006 | 2006 ⚠OLD | Wikipedia/TechCrunch | 2-3 |
| AWS revenue trajectory | $17.46B (2017) → $46B (2020) → $128.7B (2025, $45.6B op income) | 2025 | Wikipedia | 2-3 |
| FinOps Foundation founded | Feb 2019; joined Linux Foundation 2020; 12,000+ members / 3,500+ companies | 2019-2026 ⚠OLD founding | FinOps Foundation | 1-2 |
| GenAI VC funding 2023 / revenue | $21.8B (5x, 426 deals) / ~$3B revenue | 2023 ⚠OLD | BoxCars AI | 3 |
| Andreessen: companies overstaffed by | ~25-75% | 2026-03-31 | Fortune | 2 |

**Note on ⚠OLD flags:** All historical-precedent rows are *intentionally* old — they are cited as precedent/analogy, not as current measurement. None of the *load-bearing current* claims (pricing shift, deflation, ROI surveys, sector data) rely on pre-2023 figures except the a16z deflation endpoints (which span Nov-2021→Nov-2024 and are corroborated by 2025 sources).

---

## 5. Stakeholder voices (first-person, those directly affected)

**Engineers under tokenmaxxing pressure (defensive, job-security behavior):** Anonymous Microsoft/Salesforce/Meta engineers (via Gergely Orosz) describe a Goodhart's-Law failure — running wasteful agents, querying AI about docs they already have, prototyping throwaway projects, and defaulting to agents when hand-coding is faster, purely to avoid *looking* like low AI users on leaderboards managers can see. One: *"I am conscious of not wanting to be seen as 'uses too little AI'… I need to do tokenmaxxing."* Amazon workers (via FT): *"so much pressure to use these tools," "perverse incentives."*

**Management's counter-stance (token spend as self-justifying):** Meta CTO Andrew Bosworth on his top engineer spending ~his salary in tokens: *"this is easy money. Keep doing it. No limit."* Nvidia's Huang: a $500k engineer who doesn't burn ~$250k in tokens is alarming. This is the live collision the seed post predicted — adoption-maximizing managers vs budget-predictability finance.

**CFOs / FinOps teams (the "finance feels it first" claim, partly corroborated):** Surprise invoices their native tools don't even watch ($30,141 Bedrock; $10k Gemini in 30 min). Uber's COO frames the objection precisely as *attribution*, not sticker price: *"That link is not there yet."* Anthropic's CFO counters that customers *voluntarily* buy more tokens because "the returns to frontier intelligence are extremely high."

**Individual engineers hit by runaway bills:** The cleanest primary-traceable story is the ~$6,000 overnight looping-agent bill (delayed dashboard, no live spend counter). Reddit devs report ~$3,000/month. (The viral "$500K/month single Meta engineer" is single-sourced and unverified.)

**The "boomerang" / displaced-then-rehired worker (human face of the ROI reckoning):** Klarna re-added humans after its AI pivot produced "lower quality" support. Displaced copywriters (via Brian Merchant) describe being *"forced to use AI until the day I was laid off"* and the "dig your own grave" pattern (Jacques Reulet II trained the chatbots that replaced him). One agency: ~$600k/yr and 8 staff → <$10k in 2025. These voices anchor the companion jobs-apocalypse article; note the labor disruption (2022-23) ran *ahead* of the 2026 cost disruption.

**International / offshore workers (the wage-contrast control group):** Philippine BPO — the most AI-exposed sector — nonetheless added jobs in 2025 (+4%, ~80k net new), with AI deployed as augmentation; "flesh beats AI economics" where labor is cheap. The displacement concentrates on the young, urban, college-educated, female services middle class (IMF/ILO).

---

## 6. Open questions / unresolved

1. **INTERNAL DOSSIER CONFLICT — the Uber per-engineer figures.** `mainstream.md` flags the cluster "5,000 engineers / 32%→84% adoption / $150–$2,000 per engineer/month / CTO burned $1,200 in a 2-hr demo / ~70% AI code" as **aggregation drift** NOT present in the Fortune primary (which gives only ~10% of committed code from autonomous agents, per CEO Khosrowshahi, and no per-engineer dollar figure; the "$1.3M/month" belongs to a *3-person OpenAI team*). But `data.md`, `stakeholders.md`, and `expert.md` treat the same cluster as **corroborated across Fortune/Business Insider/The Verge** (attributing the $1,200 demo and 32%→84% to Uber CTO Praveen Neppalli Naga via a leaked all-hands). **These cannot both be right.** The original-reporting trail runs to The Information (paywalled) and a possibly-leaked Uber all-hands. For the article: state only what the accessible Fortune primary confirms (4-month coding-tools-budget burn; ~10% AI code; COO ROI doubt) as fact; present the engineer-count/adoption/per-head spread as *reported but not confirmed in the accessible primary*; flag the total-budget dollar figure (the seed's "~$1.2M") as a conflation. **This is the single most important thing to resolve in verification.**

2. **Net direction of cost-per-useful-outcome.** Per-token prices fall ~1-3 orders of magnitude/year; tokens-per-task rise up to ~1000x for agentic work; ~60-80% of true AI cost is non-token. Whether the net unit cost of a *useful outcome* is rising or falling is genuinely workflow-dependent and unresolved — and a skeptic can accuse either side of cherry-picking the curve that fits. The honest answer ("it depends") risks sounding like a dodge.

3. **Is the reckoning temporary (deflation) or structural (compounding usage)?** The strongest steelman (Epoch + DeepSeek + competition-driven, permanent cuts) says temporary; the strongest counter (Stanford's 1000x + frontier re-pricing + non-token cost base) says structural-for-now. Epoch itself notes the fastest declines only began Jan 2024 and may not persist. No source resolves it.

4. **Reversals: measured fact or forecast/anecdote?** Forrester's "over half reversed" is a *forecast*; Klarna is *n=1*; the rehire surveys (Robert Half 29%, Careerminds ~67%, Orgvue 32%) vary widely and rely on self-report. There is no completed, audited cohort showing what share of AI-attributed layoffs actually reversed. Survivorship/selection bias plagues the vivid rehiring stories.

5. **How much is "AI washing" vs genuine automation?** Andreessen and Altman both say companies blame AI for cuts they'd make anyway (~60% of hiring managers admit AI is a more palatable rationale than "we over-hired"); but attributing layoffs to "cover stories" asserts motive without proof, while taking corporate AI claims at face value risks repeating PR. Largely inferential — cannot be cleanly settled.

6. **Does the MIT NANDA "95% fail" stat survive scrutiny?** Contested by named critic Roetzer (52 interviews, 6-month window, ignores efficiency/churn gains). Gartner's independent "no correlation" finding points the same direction with different method — but the headline 95% should never be cited as settled fact.

7. **Vendor-margin claims rest on paywalled reporting.** The Anthropic 38%→70% and OpenAI 40%→33%/$8.4B figures trace to The Information via aggregators; SemiAnalysis is the underlying primary but not directly confirmed in this corpus. Treat as "reported by The Information."

8. **Self-prediction undermines the very pricing model vendors are adopting.** Stanford shows agents can't predict their own token costs (≤0.39), which makes *result/outcome-based* pricing fragile — yet usage-based credits are the industry's chosen direction. Unresolved tension in where pricing settles.

9. **Verbatim integrity of several historical quotes.** Bessen (IMF/AEI), Oks, Flexera, and parts of the GSA OIG and AWS-history quotes were captured via secondary extracts after 403 blocks — flagged for verbatim re-confirmation before publication.

10. **The long-run equilibrium is unknowable from early data.** The ATM/teller precedent (augmentation grew jobs for ~25 years, then mobile reversed it) and Solow/Perez both warn that early augmentation signals and "no ROI yet" readings are poor predictors of the mature-technology endpoint.

---

## 7. Source index (deduplicated, grouped by tier, with originating lens[es])

**Dedup note:** Sources recurring across lenses are merged into one entry below with all lenses listed. Counts reflect *unique* sources. The Gartner 2026-05-05 release + its Fortune mirror (2026-05-11) appear in data, expert, and follow-the-money; the GitHub Blog appears in mainstream, data, and follow-the-money; Klarna press release / Entrepreneur reversal / METR / FinOps Foundation each span multiple lenses — all consolidated.

### Tier 1 (anchor: peer-reviewed, government, official primary data)
1. **Epoch AI — LLM inference price trends** (Cottier/Snodin/Owen/Adamczewski, 2025-03-12). https://epoch.ai/data-insights/llm-inference-price-trends — *lenses: contrarian, data*
2. **GitHub Blog — Copilot moving to usage-based billing** (Mario Rodriguez, 2026-04-27). https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/ — *lenses: mainstream, data, follow-the-money*
3. **GitHub Docs — Usage-based billing / Copilot requests** (2026). https://docs.github.com/en/copilot/concepts/billing/copilot-requests — *lens: mainstream*
4. **MIT FutureTech — Beyond AI Exposure: cost-effective vision automation** (Svanberg/Li/Fleming/Goehring/Thompson, 2024-02-08). https://futuretech.mit.edu/publication/beyond-ai-exposure-which-tasks-are-cost-effective-to-automate-with-computer-vision — *lens: data*
5. **Stanford Digital Economy Lab — How Do AI Agents Spend Your Money?** (Bai/Pei/Brynjolfsson/Pentland et al., arXiv 2604.22750, 2026-04). https://arxiv.org/abs/2604.22750 / https://digitaleconomy.stanford.edu/news/how-are-ai-agents-spending-your-tokens/ — *lenses: data, expert*
6. **Gartner — Autonomous Business and AI Layoffs… Do Not Deliver Returns** (Helen Poitevin, 2026-05-05). https://www.gartner.com/en/newsroom/press-releases/2026-05-05-gartner-says-autonomous-business-and-artificial-intelligence-layoffs-may-create-budget-room-but-do-not-deliver-returns — *lenses: data, expert, follow-the-money*
7. **Stanford HAI — 2025 AI Index** (Maslej et al., 2025-04; GPT-3.5 ~280x). https://hai.stanford.edu/ai-index/2025-ai-index-report — *lens: data*
8. **Federal Reserve Bank of Dallas — AI is simultaneously aiding and replacing workers** (2026-02-24). https://www.dallasfed.org/research/economics/2026/0224 — *lens: contrarian*
9. **Forrester — AI-Led Job Disruption… Job Apocalypse Overstated** (J.P. Gownder, 2026-01-13). https://www.forrester.com/press-newsroom/forrester-impact-ai-jobs-forecast/ — *lenses: expert, follow-the-money*
10. **Daron Acemoglu — The Simple Macroeconomics of AI** (NBER w32487 / Economic Policy, 2024/2025). https://www.nber.org/papers/w32487 — *lens: expert*
11. **FinOps Foundation — FinOps for AI Overview** (Eubanks/Barney/Lam et al., 2025-26). https://www.finops.org/wg/finops-for-ai-overview/ — *lens: expert* (related: State of FinOps 2026 https://data.finops.org/ — *follow-the-money*; What is FinOps / About — *historical, comparative*)
12. **METR — Measuring the Impact of Early-2025 AI on Experienced OSS Developer Productivity** (Becker/Rush/Barnes/Rein, 2025-07-10; arXiv 2507.09089). https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ — *lens: comparative*
13. **GSA Office of Inspector General — RPA Program Lacks Evidence to Support Claimed Savings** (2023-11-30). https://www.gsaig.gov/content/gsas-robotic-process-automation-program-lacks-evidence-support-claimed-savings — *lens: historical*
14. **IMF Working Paper 2025/043 — AI and the Philippine Labor Market** (Cucio/Hennig, 2025-02-21). https://www.imf.org/en/publications/wp/issues/2025/02/21/artificial-intelligence-and-the-philippine-labor-market-mapping-occupational-exposure-and-562171 — *lens: comparative*
15. **ILO — Generative AI and jobs in the Philippines** (Phu Huynh, 2026-02-05). https://www.ilo.org/publications/generative-ai-and-jobs-philippines-labour-market-exposure-and-policy — *lens: comparative*

### Tier 2 (strong: established journalism / major-firm research)
16. **Fortune — Microsoft… AI's real cost problem** (Jake Angelo, 2026-05-22). https://fortune.com/2026/05/22/microsoft-ai-cost-problem-tokens-agents/ — *lens: mainstream*
17. **Fortune — Uber burned through its 2026 AI budget in four months** (Jake Angelo, 2026-05-26). https://fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/ — *lenses: mainstream, data*
18. **Fortune — AI-driven layoffs aren't generating returns (Gartner study)** (2026-05-11). https://fortune.com/2026/05/11/ai-automation-layoffs-gartner-study-roi/ — *lenses: expert, follow-the-money* (accessible mirror of #6)
19. **Fortune — Altman & Amodei walking back AI jobs apocalypse… IPOs** (2026-05-26). https://fortune.com/2026/05/26/sam-altman-dario-amodei-walking-back-ai-jobs-apocalypse-prophecies-ipo/ — *lens: follow-the-money*
20. **Fortune — Meta killed employee AI token dashboard** (Jacqueline Munis, 2026-04-09). https://fortune.com/2026/04/09/meta-killed-employee-ai-token-dashboard/ — *lens: stakeholders*
21. **Fortune — Marc Andreessen "silver bullet excuse" for layoffs** (2026-03-31). https://fortune.com/2026/03/31/marc-andreessen-ai-layoffs-silver-bullet-excuse-overhiring/ — *lens: historical*
22. **Computerworld — AI-led job cuts don't always mean stronger ROI (Gartner)** (2026-05). https://www.computerworld.com/article/4167140/ai-led-job-cuts-dont-always-mean-stronger-roi-gartner.html — *lens: expert*
23. **InfoWorld — DeepSeek V4-Pro price cut escalates AI pricing war** (2026-05-25). https://www.infoworld.com/article/4176709/deepseeks-steep-v4-pro-price-cut-escalates-ai-pricing-war.html — *lens: contrarian*
24. **InfoWorld — FinOps for agents: loop limits, tool-call caps** (Nikhil Mungel, 2026-03-02). https://www.infoworld.com/article/4138748/finops-for-agents-loop-limits-tool-call-caps-and-the-new-unit-economics-of-agentic-saas.html — *lens: comparative*
25. **Reuters — JPMorgan ~$1.5B AI value** (Daniel Pinto, 2025-05-05). (syndicated) — *lens: contrarian*
26. **Bain & Company — AI in Financial Services Survey** (Mehta/Salomon/Alves/Barth, Jul 2024). https://www.bain.com/insights/ai-in-financial-services-survey-shows-productivity-gains-across-the-board/ — *lens: contrarian*
27. **MIT NANDA — The GenAI Divide: State of AI in Business 2025** (Challapally, 2025-08-18; via Fortune). https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf — *lens: data*
28. **BCG Henderson Institute — AI Will Reshape More Jobs Than It Replaces** (2026-04). https://www.bcg.com/publications/2026/ai-will-reshape-more-jobs-than-it-replaces — *lenses: expert, follow-the-money*
29. **Tom's Hardware — AI costs begin to bite (Goldman 24×); Uber & Microsoft** (Jon Martindale, 2026-05-27). https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-costs-begin-to-bite-as-agents-may-increase-token-demand-by-24-times-says-goldman-sachs-report-uber-and-microsoft-among-companies-feeling-the-bite-of-tokenized-billing — *lens: mainstream*
30. **Tom's Hardware — Talent over tokens: models more expensive to run** (Jon Martindale, 2026-04-30). https://www.tomshardware.com/tech-industry/artificial-intelligence/talent-over-tokens-ai-models-are-becoming-more-expensive-to-run... — *lens: expert*
31. **Tom's Hardware — Big Tech's tokenmaxxing habit (relaying FT)** (Luke James, 2026-05-12). https://www.tomshardware.com/tech-industry/big-tech/big-tech-has-a-tokenmaxxing-habit — *lens: stakeholders*
32. **CNBC — Nvidia's Huang pitches AI tokens on top of salary** (2026-03-20). https://www.cnbc.com/2026/03/20/nvidia-ai-agents-tokens-human-workers-engineer-jobs-unemployment-jensen-huang.html — *lens: expert*
33. **CFO.com — Claude pricing raises new budgeting questions for CFOs** (Adam Zaki, 2026-05-28). https://www.cfo.com/news/claude-finance-price-pricing-raises-new-budgeting-questions-for-cfo/821266/ — *lens: stakeholders*
34. **HR Executive — As AI layoff regret surges, will boomerang employees return?** (2026-04-21). https://hrexecutive.com/as-ai-layoff-regret-surges-will-boomerang-employees-make-a-comeback/ — *lens: stakeholders*
35. **The Register — AI layoffs to backfire: half quietly rehired** (2025-10-29). https://www.theregister.com/2025/10/29/forrester_ai_rehiring/ — *lens: follow-the-money*
36. **Entrepreneur — Klarna hiring CS agents after AI couldn't cut it** (Sherin Shibu, 2025-05-09). https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396 — *lenses: stakeholders, comparative*
37. **Fast Company — Why the McKinsey layoffs are a warning for consulting** (2026). https://www.fastcompany.com/91463039/why-the-mckinsey-layoffs-are-a-warning-signal-for-consulting-in-the-ai-age... — *lens: follow-the-money*
38. **CIO.com — The hidden costs of offshore outsourcing** (Stephanie Overby, 2003-09-01) ⚠OLD. https://www.cio.com/article/267239/the-hidden-costs-of-offshore-outsourcing.html — *lens: historical*
39. **Brookings — The Solow Productivity Paradox** (1999-03, quoting Solow 1987) ⚠OLD. https://www.brookings.edu/articles/the-solow-productivity-paradox-what-do-computers-do-to-productivity/ — *lens: historical*
40. **CodeRabbit — State of AI vs Human Code Generation** + The Register/Help Net Security coverage (2025-12-17). https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report / https://www.theregister.com/2025/12/17/ai_code_bugs/ — *lens: comparative*
41. **Philippine Daily Inquirer — IT-BPM industry outpaced global growth in 2025** (IBPAP data). https://business.inquirer.net/567026/it-bpm-industry-in-ph-outpaced-global-growth-in-2025 — *lens: comparative*
42. **IMF Finance & Development — Toil and Technology** (James Bessen, 2015-03) ⚠OLD. https://www.imf.org/external/pubs/ft/fandd/2015/03/bessen.htm — *lens: historical*
43. **Carlota Perez — Technological Revolutions and Financial Capital** (2002 book; Wikipedia summary) ⚠OLD. https://en.wikipedia.org/wiki/Technological_Revolutions_and_Financial_Capital — *lens: historical*
44. **CFO Dive — Stubbornly high SaaS prices outpace CPI (Vertice index)** (Lindsey Wilkinson). https://www.cfodive.com/news/stubbornly-high-saas-prices-outpace-cpi-inflation/699683/ — *lens: data*

### Tier 3 (useful, verify: expert Substacks, vendor research, trade/enthusiast outlets)
45. **a16z — Welcome to LLMflation** (Guido Appenzeller, 2024-11-12). https://a16z.com/llmflation-llm-inference-cost/ — *lenses: contrarian, data*
46. **Anthropic Economic Index** (2025-02-10). https://www.anthropic.com/research/the-anthropic-economic-index — *lens: contrarian*
47. **Klarna press release — AI assistant handles two-thirds of CS chats** (2024-02-27). https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/ — *lens: contrarian* (raw figures Tier-2-equiv; interpretation Tier 4)
48. **The Pragmatic Engineer — Tokenmaxxing as a weird new trend** (Gergely Orosz, 2026-04-23). https://blog.pragmaticengineer.com/the-pulse-tokenmaxxing-as-a-weird-new-trend/ — *lens: stakeholders*
49. **Windows Central — Microsoft cancels Claude Code licenses** (Kevin Okemwa, 2026-05-15; attributes to The Verge/Tom Warren). https://www.windowscentral.com/microsoft/microsoft-cancels-claude-code-licenses... — *lens: mainstream*
50. **Tom's Guide — Altman "intelligence on a meter"** (2026-03). https://www.tomsguide.com/ai/people-will-buy-intelligence-from-us-on-a-meter... — *lens: mainstream*
51. **Visual Studio Magazine — Devs sound off on usage-based Copilot pricing** (2026-04-27). https://visualstudiomagazine.com/articles/2026/04/27/devs-sound-off-on-usage-based-copilot-pricing-change... — *lens: mainstream*
52. **Tropic — The AI Tax** (Justin Etkin, 2025-12-23). https://www.tropicapp.io/blog/ai-tax — *lens: data*
53. **Vertice — SaaS Inflation Index** (2023 + 2026). https://www.vertice.one/l/saas-inflation-index-report — *lens: data*
54. **NavyaAI — Tokens got 99.7% cheaper, why did your bill triple?** (2026-02). https://navyaai.com/reports/ai-cost-report-token-prices-vs-ai-bill — *lens: data*
55. **MindStudio — Why Anthropic's 70% inference margins matter** (2026-05-07; SemiAnalysis figures). https://www.mindstudio.ai/blog/anthropic-inference-margins-70-percent-api-costs — *lens: follow-the-money*
56. **BigGo Finance — OpenAI/Anthropic miss gross-margin targets (The Information)** (2026-02-25). https://finance.biggo.com/news/mRiPlZwBTwP6zY3HRxp- — *lens: follow-the-money*
57. **Future Forwarded (Substack) — Billionaires Backpedal on the AI Jobs Apocalypse** (William R. Dodson, 2026-05). https://futureforwarded.substack.com/p/billionaires-backpedal-on-the-ai — *lens: follow-the-money*
58. **Finout — What AI cost disasters teach FinOps teams** (2026, relaying The Register). https://www.finout.io/blog/what-the-latest-ai-cost-disasters-are-teaching-finops-teams-5-lessons-from-the-trenches — *lens: stakeholders*
59. **Finout — FinOps for AI Agents: four-step allocation framework** (2026-04-27). https://www.finout.io/blog/finops-for-ai-agents-a-four-step-allocation-framework — *lens: comparative*
60. **MakeUseOf — Claude Code running overnight cost $6,000** (2026). https://www.makeuseof.com/someone-left-claude-code-running-overnight-and-it-cost-6000/ — *lens: stakeholders*
61. **Blood in the Machine (Substack) — "Forced to use AI until the day I was laid off"** (Brian Merchant, 2025-12-12). https://www.bloodinthemachine.com/p/i-was-forced-to-use-ai-until-the — *lens: stakeholders*
62. **Marketing AI Institute — That Viral MIT 95% Study? Don't Believe the Hype** (Kaput/Roetzer, 2025-08-26). https://www.marketingaiinstitute.com/blog/mit-study-ai-pilots — *lens: expert*
63. **Mavvrik — AI Cost Statistics 2026** (aggregates Gartner Q4-2025 CFO survey, BCG, Forbes). https://www.mavvrik.ai/blog/ai-cost-statistics-2026/ — *lens: expert* (use for the third-party stats it cites; verify each)
64. **CloudZero — $56M Series C / "The AI ROI Company"** (2025-05-28). https://www.cloudzero.com/press-releases/20250528/ — *lens: follow-the-money*
65. **BoxCars AI (Substack) — AI infra boom echoes the telco frenzy** (Tabrez Syed, 2024-04-04). https://blog.boxcars.ai/p/making-it-up-in-volume-how-the-ai — *lens: historical*
66. **Flexera — From seats to consumption (SaaS pricing)** (2024-25). https://www.flexera.com/blog/saas-management/from-seats-to-consumption-why-saas-pricing-has-entered-its-hybrid-era/ — *lens: historical*
67. **David Oks (Substack) — Why ATMs didn't kill teller jobs, but the iPhone did** (c.2023-24). https://davidoks.blog/p/why-the-atm-didnt-kill-bank-teller — *lens: historical*
68. **AEI — What ATMs & Bank Tellers Reveal About 'Rise of the Robots'** (Pethokoukis, c.2016) ⚠OLD. https://www.aei.org/economics/what-atms-bank-tellers-rise-robots-and-jobs/ — *lens: historical*
69. **Medium — Automation Often Creates Jobs, Just Ask Bank Tellers** (Mark MacCarthy, c.2020-21). https://medium.com/@maccartm/automation-often-creates-jobs-just-ask-bank-tellers-ebd16acf3632 — *lens: historical*
70. **ActiveBatch / Raconteur — Why RPA Fails** (EY 30-50% figure; Neil MacLean) (2019/2024). https://www.advsyscon.com/blog/why-rpa-fails-robotic-process-automation/ ; https://www.raconteur.net/technology/rpa-failures — *lens: historical*
71. **Wikipedia / TechCrunch — AWS history & metered-utility framing** (Andy Jassy). https://en.wikipedia.org/wiki/Amazon_Web_Services ; https://techcrunch.com/2016/07/02/andy-jassys-brief-history-of-the-genesis-of-aws/ — *lens: historical*
72. **getpanto.ai — AI coding assistant statistics** (compilation; surfaces METR + CodeRabbit + market-share). https://www.getpanto.ai/blog/ai-coding-assistant-statistics — *lens: comparative* (compilation Tier 4; points to Tier-1 primaries)
73. **WorkfxAI — AI Content Tools vs Human Writers (brand voice)** (2026-03-04). https://blogs.workfx.ai/2026/03/04/ai-content-tools-vs-human-writers-brand-voice-consistency-comparison-2026/ — *lens: comparative* (directional only)
74. **CMSWire — 16 call-center statistics** (2026). https://www.cmswire.com/contact-center/16-important-call-center-statistics-to-know-about/ — *lens: comparative*
75. **MLQ.ai — Klarna CEO admits AI cuts went too far (Bloomberg)** (2025-05). https://mlq.ai/news/klarna-ceo-admits-aggressive-ai-job-cuts-went-too-far-starts-hiring-again-after-us-ipo/ — *lens: comparative*

### Tier 4 (signal, not citation: social, single-source, partisan — surface arguments, verify factual claims)
76. **Seed input — commissioning author's LinkedIn post** (provenance: the commissioner; the four named claims to verify). `articles/the-ai-cost-reckoning-does-replacing-workers-with-ai-actuall/research/_seed_linkedin_post.md` — *lens: seed*
77. **X / GeekWire — Nadella "Jevons paradox" tweet** (2025-01-27; GeekWire context Tier 2). https://x.com/satyanadella/status/1883753899255046301 — *lens: contrarian*
78. **a16z / 20VC — Andreessen "100% incorrect" labor-displacement clip** (2026). https://x.com/a16z/status/2038760847473009083 — *lens: historical*
79. **Tech in Asia (LinkedIn) — "Call center apocalypse fails as flesh beats AI economics"** (2025). https://www.linkedin.com/posts/tech-in-asia_call-center-apocalypse-fails-as-flesh-beats-activity-7357341486587236352-53u6 — *lens: comparative* (Tech in Asia Tier 3 at source; layoff tally VERIFY)
80. **Metaintro — BCG $3.6B / 25% AI revenue** (2026-04-23; figures trace to BCG/Bloomberg). https://www.metaintro.com/blog/bcg-25-percent-ai-revenue-consulting-jobs-2026 — *lens: follow-the-money* (cite figures as "BCG via Bloomberg")
81. **HR/rehire survey cluster** — Robert Half, Careerminds (n=600), Orgvue (32%), Great Place to Work — reported via HR Executive/GFMag/Built In/SHRM. — *lenses: stakeholders, follow-the-money* (attribute to named survey houses)

### Tier 5 (avoid / do NOT cite — documented only as drift example)
82. **AI Weekly — "Uber Exhausts AI Budget as Claude Code Hits 84%"** (2026-05-26). https://aiweekly.co/alerts/uber-exhausts-ai-budget-as-claude-code-hits-84 — *lens: mainstream* — **DO NOT CITE.** Documented as the aggregation-drift vector that imported the "5,000 engineers / 32%→84% / 70% AI code / $500-$2,000" cluster and a fabricated "CTO Praveen Neppalli Naga confirmed" attribution not in the Fortune primary. See Open Question #1.
83. **IBTimes UK — "Meta Engineer Burned $500K a Month on AI Tokens"** (Brian Yalung, 2026-05-28). https://www.ibtimes.co.uk/meta-ai-transition-layoffs-claudenomics-1799390 — *lens: stakeholders* — **CONTESTED, do not cite as fact.** Headline figure traces to one X user (@sheiyuo); IBTimes hedges "reportedly/allegedly."

---

**Dossier coverage:** 8 research lenses + seed, consolidated to ~83 unique sources (≈15 Tier 1, ≈29 Tier 2, ≈31 Tier 3, ≈6 Tier 4, 2 Tier 5). The empirical backbone is unusually strong on the Tier-1 side: deflation (Epoch, Stanford HAI), the agentic-token mechanism (Stanford Digital Economy Lab), the ROI-skeptic finding (Gartner), the augmentation signal (Dallas Fed, Forrester), the felt-vs-measured productivity keystone (METR RCT), the automation-savings audit (GSA OIG), and the international labor data (IMF, ILO). The inflation/FinOps-cost side and the vendor-margin/IPO side skew Tier 3 (vendors selling the fix; paywalled reporting via aggregators) and are flagged accordingly throughout.
