# Sources: The AI Cost Reckoning — Does Replacing Workers With AI Actually Save Money?

Deduplicated, numbered, grouped by source-quality tier. Each entry notes the research lens(es) it came from in the master dossier and, where relevant, the article citation number `[n]` it backs. Sources recurring across lenses are merged.

**Empirical backbone:** The article's load-bearing facts (the pricing shift, the agentic-token mechanism, the no-ROI-correlation finding, the developer-slowdown trial) are Tier 1. The "AI doesn't pay" anecdotes and the inflation/FinOps dollar figures skew Tier 2–3 (contemporaneous reporting, vendor research, paywalled scoops via relays) and are flagged in the article accordingly.

---

## Tier 1 — Anchor (peer-reviewed, government, official primary data, first-party docs)

1. **GitHub Blog — "GitHub Copilot is moving to usage-based billing"** — Mario Rodriguez (CPO), 2026-04-27. https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/ (per-credit value: GitHub Docs, https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing) — *lenses: mainstream, data, follow-the-money* · article **[2]**

2. **Stanford Digital Economy Lab — "How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks"** — Bai, Huang, Wang, Sun, Mihalcea, Brynjolfsson, Pentland & Pei, arXiv:2604.22750, 2026-04 (preprint, not yet peer-reviewed). https://arxiv.org/abs/2604.22750 · Pei quote via https://digitaleconomy.stanford.edu/news/how-are-ai-agents-spending-your-tokens/ — *lenses: data, expert* · article **[8]**

3. **Gartner press release — "Autonomous Business and AI Layoffs May Create Budget Room but Do Not Deliver Returns"** — Helen Poitevin (Distinguished VP Analyst), 2026-05-05 (survey n=350, $1B+ revenue, fielded Q3 2025). https://www.gartner.com/en/newsroom/press-releases/2026-05-05-gartner-says-autonomous-business-and-artificial-intelligence-layoffs-may-create-budget-room-but-do-not-deliver-returns — *lenses: data, expert, follow-the-money* · article **[11]**

4. **METR — "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity"** — Becker, Rush, Barnes & Rein, 2025-07-10; arXiv:2507.09089 (RCT, n=16, 246 tasks; −19%, 95% CI +2% to +39%). https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ · follow-up https://metr.org/blog/2026-02-24-uplift-update/ — *lens: comparative* · article **[12]**

5. **Epoch AI — "LLM inference price trends"** — Cottier, Snodin, Owen & Adamczewski, 2025-03-12 (9x–900x/yr at fixed capability; median ~50x). https://epoch.ai/data-insights/llm-inference-price-trends — *lenses: contrarian, data* · article **[5]**

6. **Stanford HAI — "2025 AI Index Report"** — Maslej et al., 2025-04 (GPT-3.5-class $20.00 → ~$0.07/Mtok ≈ 280x in ~18 mo). https://hai.stanford.edu/ai-index/2025-ai-index-report — *lens: data* · article **[6]**

7. **Federal Reserve Bank of Dallas — "AI is simultaneously aiding and replacing workers"** — 2026-02-24 (computer-systems-design wages +16.7% vs +7.5% national since fall 2022). https://www.dallasfed.org/research/economics/2026/0224 — *lens: contrarian* · article **[17]**

8. **Forrester press release — "Forrester's Impact of AI on Jobs Forecast"** — J.P. Gownder, 2026-01-13 ("over half" of AI-attributed layoffs forecast to reverse; "AI washing"). https://www.forrester.com/press-newsroom/forrester-impact-ai-jobs-forecast/ — *lenses: expert, follow-the-money* · article **[16]** (rehire-survey range via HR Executive, Tier 2, #19)

9. **Daron Acemoglu — "The Simple Macroeconomics of AI"** — NBER Working Paper w32487 / *Economic Policy*, 2024/2025 (~1.1–1.6% GDP over a decade). https://www.nber.org/papers/w32487 — *lens: expert* · article **[19]**

10. **FinOps Foundation — "FinOps for AI Overview" + State of FinOps 2026** — 2025–2026 (98% of members manage AI spend, up from 31% in 2024; n≈1,192). https://www.finops.org/wg/finops-for-ai-overview/ · data https://data.finops.org/ — *lenses: expert, follow-the-money, historical* · article **[24]**

*(Additional Tier-1 sources in the dossier not directly cited in this article — MIT FutureTech vision-automation cost study; GSA OIG RPA audit; IMF WP 2025/043 and ILO Philippines labor studies — informed the analysis but did not carry a specific in-text claim here.)*

---

## Tier 2 — Strong (established journalism / major-firm research)

11. **Fortune — "Uber burned through its 2026 AI budget in four months"** — Jake Angelo, 2026-05-26 (Macdonald "not there yet"; ~10% committed code from autonomous agents per Khosrowshahi; Uber's real $1,200 demo figure; NO per-engineer dollar figure). https://fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/ — *lenses: mainstream, data* · article **[1]**

12. **Fortune — "Microsoft and AI's real cost problem"** — Jake Angelo, 2026-05-22 ("the work gets more expensive with more use and better efficiency"). https://fortune.com/2026/05/22/microsoft-ai-cost-problem-tokens-agents/ — *lens: mainstream* · article **[9]**

13. **Computerworld — "AI-led job cuts don't always mean stronger ROI"** — 2026-05 (origin of the verbatim Poitevin "no connection or correlation" quote). https://www.computerworld.com/article/4167140/ai-led-job-cuts-dont-always-mean-stronger-roi-gartner.html — *lens: expert* · article **[10]**

14. **InfoWorld — "DeepSeek's steep V4-Pro price cut escalates AI pricing war"** — 2026-05-25 (Gogia: "permanent rather than promotional"). https://www.infoworld.com/article/4176709/deepseeks-steep-v4-pro-price-cut-escalates-ai-pricing-war.html — *lens: contrarian* · article **[7]**

15. **InfoWorld — "FinOps for agents: loop limits, tool-call caps, and the new unit economics of agentic SaaS"** — Nikhil Mungel, 2026-03-02 ("two customers with the same licenses generate a 10X difference… one had standardized workflows and the other lived in exceptions"). https://www.infoworld.com/article/4138748/finops-for-agents-loop-limits-tool-call-caps-and-the-new-unit-economics-of-agentic-saas.html — *lens: comparative* · article **[20]**

16. **Klarna press release — "Klarna AI assistant handles two-thirds of customer service chats in its first month"** — 2024-02-27 (self-interested; ~700-FTE equivalent, 2.3M conversations, $40M estimated 2024 profit improvement — never independently audited). https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/ — *lens: contrarian* (raw figures Tier-2-equivalent; promotional interpretation Tier 4) · article **[13]** (JPMorgan ~$1.5B AI value via Reuters/COO Daniel Pinto, 2025-05-05, also cited at **[13]**)

17. **Entrepreneur — "Klarna CEO reverses course by hiring more humans, not AI"** — Sherin Shibu, 2025-05-09 (Siemiatkowski: "investing in the quality of human support is the way of the future"). https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396 (reversal also reported by Bloomberg, 2025-05-08: https://www.bloomberg.com/news/articles/2025-05-08/klarna-turns-from-ai-to-real-person-customer-service) — *lenses: stakeholders, comparative* · article **[14]**

18. **CNBC — "Nvidia's Jensen Huang on AI tokens and engineer salaries"** — 2026-03-20 ("$500,000 engineer… $250,000 worth of tokens… deeply alarmed"). https://www.cnbc.com/2026/03/20/nvidia-ai-agents-tokens-human-workers-engineer-jobs-unemployment-jensen-huang.html — *lens: expert* · article **[25]**

19. **HR Executive — "As AI layoff regret surges, will boomerang employees make a comeback?"** — 2026-04-21 (rehire-survey range: Robert Half ~29%, Careerminds ~two-thirds). https://hrexecutive.com/as-ai-layoff-regret-surges-will-boomerang-employees-make-a-comeback/ — *lens: stakeholders* · supports article **[16]** (rehire range)

20. **Fortune — "Meta killed its employee AI token dashboard"** — 2026-04-09 ("Claudeonomics" leaderboard: ~85,000 employees, ~60 trillion tokens/30 days, top user ~281B, shut ~April 8, 2026). https://fortune.com/2026/04/09/meta-killed-employee-ai-token-dashboard/ — *lens: stakeholders* · article **[26]**

21. **The Verge ("Notepad") — Microsoft discontinuing Claude Code internally** — Tom Warren, 2026-05 (EVP Rajesh Jha memo; E+D division; standardization on Copilot CLI; engineers preferred Claude Code). https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad — *lens: mainstream* · article **[27]** *(primary not directly fetchable for this user agent; verified via independent relays incl. Windows Central, WinBuzzer — confidence capped accordingly)*

22. **MIT NANDA — "The GenAI Divide: State of AI in Business 2025"** — Challapally, 2025-08-18 (the "~95% no measurable P&L" figure; self-described "directionally accurate," methodology contested). https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf (via Fortune, 2025-08-18) — *lens: data* · article **[28]**

---

## Tier 3 — Useful, verify (expert Substacks, vendor research, trade/enthusiast outlets)

23. **Tom's Guide — "People will buy intelligence from us on a meter": Sam Altman** — 2026-03 (BlackRock Infrastructure Summit). https://www.tomsguide.com/ai/people-will-buy-intelligence-from-us-on-a-meter-chatgpts-ceo-sam-altman-has-critics-worried-with-his-ai-vision — *lens: mainstream* · article **[4]**

24. **Visual Studio Magazine — "Devs sound off on usage-based Copilot pricing change: 'You will get less, but pay the same price'"** — 2026-04-27. https://visualstudiomagazine.com/articles/2026/04/27/devs-sound-off-on-usage-based-copilot-pricing-change-you-will-get-less-but-pay-the-same-price.aspx — *lens: mainstream* · article **[3]**

25. **NavyaAI — "Tokens got 99.7% cheaper — why did your AI bill triple?"** — 2026-02 (vendor-sourced; model invoice ~20–40% of true cost; sample size undisclosed — directional only). https://navyaai.com/reports/ai-cost-report-token-prices-vs-ai-bill — *lens: data* · article **[21]**

26. **Marketing AI Institute — "That Viral MIT 95% Study? Don't Believe the Hype"** — Kaput/Roetzer, 2025-08-26 (verbatim Roetzer rebuttal: "not a viable, statistically valid thing"; Wharton's Kevin Werbach independently questions the figure). https://www.marketingaiinstitute.com/blog/mit-study-ai-pilots — *lens: expert* · supports article **[28]**

27. **CloudZero press release — $56M Series C, "The AI ROI Company"** — 2025-05-28. https://www.cloudzero.com/press-releases/20250528/ — *lens: follow-the-money* · article **[23]**

28. **Anthropic Economic Index** — 2025-02-10 (57% augmentation vs 43% automation). https://www.anthropic.com/research/the-anthropic-economic-index — *lens: contrarian* · article **[18]** *(first-party usage data; treated as Tier 3 given vendor incentive)*

29. **Metaintro — "BCG: ~25% of revenue from AI" (figures trace to BCG/Bloomberg)** — 2026-04-23 (~$3.6B / ~25% of $14.4B 2025 revenue). https://www.metaintro.com/blog/bcg-25-percent-ai-revenue-consulting-jobs-2026 — *lens: follow-the-money* · article **[22]** *(cite figure as "BCG via Bloomberg")*

---

## Tier 4 — Signal, not citation (social, single-source; surface arguments, verify factual claims)

30. **X / GeekWire — Satya Nadella "Jevons paradox" post** — 2025-01-27 (GeekWire context Tier 2). https://x.com/satyanadella/status/1883753899255046301 — *lens: contrarian* · article **[15]** *(used for the named argument, not a factual claim)*

31. **Seed input — commissioning author's LinkedIn post** — provenance: the commissioner; the framing ("subsidy era ending / FinOps mandatory") and the three named claims the article tests. `research/_seed_linkedin_post.md` — *lens: seed*

---

## Tier 5 — Avoid / do NOT cite (documented only as aggregation-drift examples)

- **AI Weekly — "Uber Exhausts AI Budget as Claude Code Hits 84%"**, 2026-05-26. https://aiweekly.co/alerts/uber-exhausts-ai-budget-as-claude-code-hits-84 — **NOT CITED.** Aggregation-drift vector: imported the contested per-engineer cluster and mis-captioned it as Fortune-origin. The underlying cluster (84% adoption, $500–$2,000/engineer, CTO's $1,200 demo, ~70% AI code) is *real reporting from The Information's paywalled scoop*, not a fabrication — but is not in the fetchable Fortune primary, so the article does not assert it.

- **IBTimes UK — "Meta Engineer Burned $500K a Month on AI Tokens"**, Brian Yalung, 2026-05-28. https://www.ibtimes.co.uk/meta-ai-transition-layoffs-claudenomics-1799390 — **CONTESTED, not cited as fact.** The $500K/month per-engineer figure traces to one X user (@sheiyuo); IBTimes hedges ("roughly," "according to"). The article references it only inside the "What we don't know" section as an example of how hype figures degrade.

---

**Dedup / provenance notes:**
- The Gartner findings appear across data, expert, and follow-the-money lenses; consolidated to the 2026-05-05 release (#3) with the verbatim quote attributed to Computerworld (#13).
- The GitHub Blog (#1) spans mainstream, data, and follow-the-money.
- Klarna's launch claims (#16) and the reversal (#17) are deliberately kept as two entries — the article uses both halves to make the same point.
- **The Verge (#21) and The Information (the origin of the contested Uber and Meta clusters) could not be fetched directly** for this user agent / paywall; their contents were verified via independent relays, which is why the corresponding article claims are framed as "reported" and the debunked dollar figures are quarantined in the "What we don't know" section.
