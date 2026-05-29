# The AI Cost Reckoning: Does Replacing Workers With AI Actually Save Money?

*Per-token prices are collapsing and AI bills are still going up. The reason explains why "AI is cheaper than a worker" turns out to depend entirely on the job.*

Four months into 2026, Uber had already spent its entire annual budget for AI coding tools [1]. Engineers had taken to Anthropic's Claude Code and Cursor with the enthusiasm of converts, and the meter ran faster than anyone had modeled. Then the company's president and chief operating officer, Andrew Macdonald, went on the *Rapid Response* podcast and, asked whether all that usage was translating into shipped product, answered plainly:

> "That link is not there yet." — Andrew Macdonald, President & COO, Uber, *Rapid Response* (via Fortune), 2026-05-26 [1]

Macdonald wasn't disputing that his engineers were busy. He was disputing that anyone could prove the busyness was worth it. "Maybe implicitly there's more that is getting shipped," he said, "but it's very hard to draw a line between one of those stats and 'Okay now we're actually producing like 25% more useful consumer features'" [1]. A company that had bet heavily on AI for labor was asking where the money went.

That question is now being asked across corporate finance, and the timing is not coincidental. The premise underpinning three years of AI enthusiasm — that software could do knowledge work for a fraction of a salary — rested on a pricing model being dismantled in real time. On June 1, 2026, GitHub stops charging a flat subscription for its Copilot coding assistant and starts billing by the token, like cloud compute [2]. The claim that AI is cheaper than the worker it replaces was always a bet that the bill would stay small. The bill is no longer staying small.

So were the savings ever real, or merely subsidized? The honest answer is neither a clean yes nor a clean no: the math holds for a narrow band of work and quietly falls apart everywhere else.

## The pricing model flipped from flat fee to metered compute

Start with the mechanism, the most solid fact in the story and a first-party one. For three years, AI coding tools sold like software: a fixed monthly fee, all you can eat. That model is ending. GitHub Copilot is replacing its "premium request" allowance with usage-based "GitHub AI Credits" — one credit costs a cent, and credits drain as you consume tokens, billed on input, output, and cached tokens at each model's published API rates [2].

The company's own explanation is the cleanest statement of the problem anywhere in the corpus. In the announcement, GitHub Chief Product Officer Mario Rodriguez wrote that the flat model is "no longer sustainable," for a reason that should worry any CFO who budgeted AI as a SaaS line item:

> "Today, a quick chat question and a multi-hour autonomous coding session can cost the user the same amount. GitHub has absorbed much of the escalating inference cost behind that usage, but the current premium request model is no longer sustainable." — Mario Rodriguez, Chief Product Officer, GitHub, 2026-04-27 [2]

That is a vendor admitting it has been eating the difference — and the pricing change hands it to the customer. Developers noticed; a complaint headlined by *Visual Studio Magazine* was blunt: "You will get less, but pay the same price" [3].

The shift is not unique to GitHub — it is a whole industry moving from selling a product to selling a utility. Sam Altman has been explicit: "We see a future where intelligence is a utility, like electricity or water, and people buy it from us on a meter" [4]. A meter rewards the seller when you use more, which changes the arithmetic of replacing a salaried human with software whose cost climbs with every task you hand it.

## The deflation is real — but so is the consumption explosion

Here is where the story gets genuinely difficult, because two true facts point in opposite directions.

The first: the price of AI is falling at a rate almost without precedent in computing. Epoch AI, a research nonprofit that tracks model economics, found that for a fixed level of capability, inference prices have fallen between 9-fold and 900-fold per year, with a median around 50-fold [5]. Stanford's AI Index put it in human terms: running a GPT-3.5-class model fell from $20.00 per million tokens to about $0.07 in roughly eighteen months — a drop of about 280 times, or 99.7% [6]. This is not purely venture-capital generosity; analysts attribute it to genuine engineering — better chips, smaller models, open-weight competition. When the Chinese lab DeepSeek slashed prices on its V4-Pro model, Sanchit Vir Gogia of Greyhound Research told *InfoWorld* the cut was structural, not a loss-leader:

> "It is not a discount. It is an efficiency gain being passed through… This is why the price cut is permanent rather than promotional." — Sanchit Vir Gogia, CEO, Greyhound Research (via InfoWorld), 2026-05-25 [7]

If that were the whole picture, Macdonald's budget problem would be temporary. But there is a second fact, and it cuts the other way: the price of a *token* is collapsing while the number of tokens a task *consumes* is exploding. In a study of agentic coding — where a model works autonomously through a problem rather than answering one question — Longju Bai and colleagues at Stanford's Digital Economy Lab found that on a standard software-engineering benchmark, agentic workflows burned up to roughly 1,000 times more tokens than ordinary code chat or reasoning [8]. Worse for anyone trying to budget: token use on the *same task* varied by up to 30 times run to run, and the models could not predict their own consumption — a best-case correlation of about 0.39 — while systematically underestimating the true cost [8]. The lab's framing is unsparing:

> "Agents are not capable of predicting their own token costs. This is the fundamental bottleneck for result-based pricing for agents." — Jiaxin Pei, Stanford Digital Economy Lab, 2026-05-05 [8]

Cheaper tokens, in other words, do not guarantee a cheaper outcome; they can produce a more expensive one. *Fortune*, surveying the same dynamic, drew the conclusion the whole debate rests on: "with a token-based pricing system, the work gets more expensive with more use and better efficiency" [9]. Efficiency invites more autonomous use, and autonomous use eats tokens faster than the price falls. Which blade of the scissors wins is not a matter of opinion — it is a matter of which workflow you are running.

## The layoffs don't track the returns

Set the bill aside, then, and look only at the bottom line. Companies have cut staff and credited AI. Did the savings show up? Not where you would expect. In the third quarter of 2025, Gartner surveyed 350 executives at companies with more than $1 billion in revenue, all piloting or deploying AI automation. About 80% reported workforce reductions tied to AI. But when Gartner sorted firms by the returns they were getting, the layoff rates barely moved between the winners and the losers. Helen Poitevin, a Distinguished VP Analyst at Gartner, put it without hedging:

> "There's no connection or correlation between people who are achieving ROI and layoffs." — Helen Poitevin, Distinguished VP Analyst, Gartner (via Computerworld), 2026 [10]

This is correlational, self-reported, single-vendor data, limited to large firms already committed to AI — not causal proof that cutting staff destroys value. But it shows the firms capturing real returns are not, on the whole, the ones cutting the most people. Poitevin's reading is that the returns come from a different move: "Organizations that improve ROI are not those that eliminate the need for people, but those that amplify them" [11].

The discomfort deepens when you ask whether AI even saves time for the people still using it. In a randomized controlled trial published in July 2025, the research group METR had 16 experienced open-source developers complete 246 real tasks on their own mature codebases — work where an expert should know exactly where AI helps. With early-2025 AI tools available, they took 19% *longer* (a wide confidence interval of +2% to +39%) [12]. The startling part is what they believed. They had forecast a 24% speedup; afterward, having been slowed down, they still believed AI had sped them up by about 20% [12]. The people best positioned to judge were confidently wrong about their own productivity.

METR's authors limit the claim — it covers experienced developers on complex, familiar code, the hardest case for AI, and a later follow-up suggested newer tools likely help more [12]. It is not a verdict on all software work. But it punctures the assumption that the gain is so self-evident it need not be measured. At Uber, Macdonald was asking for exactly that measurement and not finding it.

## Where it genuinely saves millions — and where that breaks

None of this means AI never pays. It means the wins are specific — and the clearest one is also the clearest cautionary tale.

In February 2024, the buy-now-pay-later company Klarna announced that its AI customer-service assistant had, in its first month, handled 2.3 million conversations — about two-thirds of chat volume — and was doing "the equivalent work of 700 full-time agents" [13]. It cut average resolution time from 11 minutes to under two, drove a 25% drop in repeat inquiries, and matched human agents on customer satisfaction. Klarna estimated it would improve profit by $40 million in 2024 [13]. These describe exactly the work AI substitution is built for: high volume, low variance, error-tolerant, with an expensive human baseline.

But the figures come from Klarna's own press release, were never independently audited, and describe cost the company says it *avoided* — hiring it skipped during a growth phase — not realized savings or layoffs reconciled to actuals [13]. And the story did not end there. By May 2025, CEO Sebastian Siemiatkowski had begun re-adding human agents, telling Bloomberg that making cost the dominant factor had produced "lower quality" support [14]. He reframed the strategy in terms that would have sounded heretical a year earlier:

> "Really, investing in the quality of human support is the way of the future for us." — Sebastian Siemiatkowski, CEO, Klarna (via Entrepreneur), 2025-05-09 [14]

The reversal, too, has limits: Klarna insists it remains "AI-first," and the re-added humans are a small pilot of remote freelance agents, not a restoration of the 700 roles [14]. The honest reading is not "AI failed at Klarna." It is that the same case proves both halves of the argument at once — substitution genuinely cleared the cheap, repetitive work, and genuinely buckled on the complex, reputation-sensitive work. The savings and the limits are the same story.

Other large numbers survive scrutiny better precisely because they are not framed as headcount replacement. JPMorgan attaches roughly $1.5 billion in "business value" to its AI deployments [13] — a figure that, like the durable wins generally, comes from amplifying a workforce, not deleting one.

## The bull case, fairly stated: deflation plus amplification

The strongest counterargument to the "reckoning" framing is not weak, and it deserves its best advocates. It comes in two parts.

The first is the deflation case pushed to its conclusion: per-token prices fall one to three orders of magnitude a year for structural reasons, so today's cost panic is a snapshot of the most expensive moment AI will ever have. Satya Nadella and others invoke the Jevons paradox — as a resource gets cheaper, total consumption rises, but per-unit economics keep improving [15]. Runaway bills, on this view, are falling prices working as designed. Even Epoch, the source bulls lean on hardest, adds the caveat that keeps this honest: the fastest declines "start after January 2024," and "it's less clear that those will persist" [5].

The second part is the augmentation case, with unusually strong, ideologically diverse backing. Gartner's own conclusion is that the returns come from amplifying workers, not replacing them. Forrester forecasts that more than half of layoffs attributed to AI will be "quietly reversed," and names the pattern driving the cuts — "AI washing," blaming financially motivated layoffs on capabilities that don't yet exist [16]. The Federal Reserve Bank of Dallas, with no product to sell, found something hard to square with simple replacement: wages in the most AI-exposed white-collar fields are *rising*, with pay in computer-systems design up 16.7% since the fall of 2022 against 7.5% nationally [17]. Its framing splits the difference precisely: AI "can substitute for entry-level workers… and at the same time complement experienced workers" [17]. Anthropic's own usage data agrees — 57% augmentation versus 43% automation [18] — and the Nobel laureate Daron Acemoglu, the most prominent academic skeptic, estimates AI will lift GDP a "nontrivial, but modest" 1.1% to 1.6% over a decade [19]. A real effect, not a labor apocalypse.

Put together, the bull case is coherent: wait out the price curve, deploy AI to amplify workers rather than fire them, and the economics work. The evidence genuinely leans this way — but conditionally. Every one of these sources describes the *average* across many workflows, and the average hides the fact that substitution does win, decisively, in the narrow band where the work is repetitive and the human baseline is costly. The bull case and the Klarna case are both true. They are describing different jobs.

## The real unit of measurement, and who profits from the confusion

Stack the evidence and a single idea falls out that no source states cleanly: the unit that matters is neither the price of a token nor the cost of a headcount, but the cost per *accepted outcome* — the all-in price of one piece of work a human actually approves and ships.

That unit explains everything else. It explains why GitHub had to start metering: a quick question and a multi-hour agent run produce wildly different outcome costs at the same flat price [2]. It explains the observation that haunts the FinOps literature — Nikhil Mungel of InfoWorld watched "two customers with the same licenses generate a 10X difference in inference and tool costs because one had standardized workflows and the other lived in exceptions" [20]. And it explains Gartner's no-correlation finding: the firms cutting heads were optimizing the wrong variable. The model invoice, by vendor estimates that should be read as directional, is only a fifth to two-fifths of the true cost of an AI workflow — the rest is orchestration, retries, oversight, and the human who checks the work [21]. The direction is not in dispute: the human layer you cannot remove is what makes the substitution work, and what the cheap-replacement pitch leaves off the invoice.

Which raises the follow-the-money question. The answer is bracing: nearly every story in this debate has a paid beneficiary, so all deserve a discount. "Cut headcount" flatters a CEO's investor narrative. "Reskill, don't replace" sells consulting — Boston Consulting Group books roughly $3.6 billion, about a quarter of its revenue, from AI work [22]. "Buy more tokens" serves the model vendors. And "control your tokens" has minted an AI-FinOps vendor class: CloudZero raised $56 million and rebranded as "The AI ROI Company," while the FinOps Foundation reports 98% of its members now manage AI spending, up from 31% in 2024 [23][24]. Even the chip makers argue the spending is correct — Nvidia's Jensen Huang said a $500,000 engineer who doesn't burn $250,000 a year in tokens would leave him "deeply alarmed" [25]. The cost panic itself is now a market: the FinOps mandate framing this debate is real and rational, and it is also being sold.

## What we don't know

The strongest claims here rest on solid ground: the pricing shift is GitHub's own documentation; the agentic-token mechanism is a Stanford preprint; the no-correlation finding and the developer-slowdown trial are independent and replicable. But the emotional center of the "AI doesn't pay" story is built on softer material, and honesty requires saying so.

The widely circulated specifics often don't survive a click. The viral figure of a single Meta engineer spending $500,000 a month traces to one anonymous social-media post and should not be repeated as fact — even though the underlying leaderboard is real: Meta's "Claudeonomics" dashboard tracked roughly 85,000 employees consuming about 60 trillion tokens in thirty days before the company shut it down [26]. The claim that "Microsoft dropped Claude Code because it was too expensive" inverts the reporting: Microsoft is standardizing its Experiences + Devices division on GitHub Copilot CLI, Claude models remain available *through* that tool, and its own engineers reportedly *preferred* Claude Code [27]. The much-cited MIT finding that 95% of corporate AI pilots show no measurable return is self-described as "directionally accurate" and has been challenged by named academics; it should never stand alone [28]. And the dollar figures degrade as they travel — the genuine $1,200 a single Uber demo consumed becomes, through careless aggregation, a "$1.2M" budget that exists in no primary source. Hype numbers don't just mislead; they compound.

Two larger questions stay open. Whether falling prices will outrun rising consumption over the next two years is workflow-specific and genuinely unresolved. And no single audited dataset shows what share of AI-attributed layoffs actually reversed; Forrester's "over half" is a forecast, Klarna is one company, and rehire surveys range wildly, from 29% to two-thirds [16]. Anyone who tells you the reckoning is settled, in either direction, is selling something.

## The reckoning is real. The verdict isn't binary.

Macdonald's problem at Uber was never that AI is worthless. It was that he couldn't draw a line from the meter to the money. That is the reckoning in one sentence: the era of not having to ask is over, and the bill arrives whether or not the line gets drawn.

Where the line can be drawn — high-volume, low-variance, error-tolerant work routed to the cheapest model that's good enough — AI saves real money, and Klarna's first act proved it. Where it can't, the savings evaporate into oversight, exceptions, and the experienced human who turns out slower with the tool but still signs off on the work. The technology didn't change between Klarna's first act and its second. The job did. The companies that win the next phase won't be the ones that spent the most on tokens or cut the most jobs. They'll be the ones that work out, workflow by unglamorous workflow, which of their work the meter can actually do — and keep the humans on the rest.

---

## Sources

[1] Uber burned through its 2026 AI budget in four months — Jake Angelo, Fortune, 2026-05-26. https://fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/

[2] GitHub Copilot is moving to usage-based billing — Mario Rodriguez, GitHub Blog, 2026-04-27. https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/ (per-credit value per GitHub Docs: https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing)

[3] Devs sound off on usage-based Copilot pricing change: "You will get less, but pay the same price" — Visual Studio Magazine, 2026-04-27. https://visualstudiomagazine.com/articles/2026/04/27/devs-sound-off-on-usage-based-copilot-pricing-change-you-will-get-less-but-pay-the-same-price.aspx

[4] "People will buy intelligence from us on a meter": Sam Altman — Tom's Guide, 2026-03. https://www.tomsguide.com/ai/people-will-buy-intelligence-from-us-on-a-meter-chatgpts-ceo-sam-altman-has-critics-worried-with-his-ai-vision

[5] LLM inference price trends — Cottier, Snodin, Owen & Adamczewski, Epoch AI, 2025-03-12. https://epoch.ai/data-insights/llm-inference-price-trends

[6] 2025 AI Index Report — Maslej et al., Stanford HAI, 2025-04. https://hai.stanford.edu/ai-index/2025-ai-index-report

[7] DeepSeek's steep V4-Pro price cut escalates AI pricing war — InfoWorld, 2026-05-25. https://www.infoworld.com/article/4176709/deepseeks-steep-v4-pro-price-cut-escalates-ai-pricing-war.html

[8] How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks — Bai, Huang, Wang, Sun, Mihalcea, Brynjolfsson, Pentland & Pei, Stanford Digital Economy Lab, arXiv:2604.22750, 2026-04. https://arxiv.org/abs/2604.22750 (Pei quote via https://digitaleconomy.stanford.edu/news/how-are-ai-agents-spending-your-tokens/)

[9] Microsoft and AI's real cost problem — Jake Angelo, Fortune, 2026-05-22. https://fortune.com/2026/05/22/microsoft-ai-cost-problem-tokens-agents/

[10] AI-led job cuts don't always mean stronger ROI (Gartner) — Computerworld, 2026-05. https://www.computerworld.com/article/4167140/ai-led-job-cuts-dont-always-mean-stronger-roi-gartner.html

[11] Gartner Says Autonomous Business and AI Layoffs May Create Budget Room but Do Not Deliver Returns — Helen Poitevin, Gartner press release, 2026-05-05. https://www.gartner.com/en/newsroom/press-releases/2026-05-05-gartner-says-autonomous-business-and-artificial-intelligence-layoffs-may-create-budget-room-but-do-not-deliver-returns

[12] Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity — Becker, Rush, Barnes & Rein, METR, 2025-07-10; arXiv:2507.09089. https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ (follow-up: https://metr.org/blog/2026-02-24-uplift-update/)

[13] Klarna AI assistant handles two-thirds of customer service chats in its first month — Klarna press release, 2024-02-27. https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/ (JPMorgan ~$1.5B AI value: Reuters, COO Daniel Pinto, 2025-05-05)

[14] Klarna CEO reverses course by hiring more humans, not AI — Sherin Shibu, Entrepreneur, 2025-05-09. https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396 (reversal also reported by Bloomberg, 2025-05-08: https://www.bloomberg.com/news/articles/2025-05-08/klarna-turns-from-ai-to-real-person-customer-service)

[15] Satya Nadella on the Jevons paradox — X, 2025-01-27 (GeekWire context). https://x.com/satyanadella/status/1883753899255046301

[16] Forrester: AI-Led Job Disruption Will Be Significant, but the Job Apocalypse Is Overstated — J.P. Gownder, Forrester press release, 2026-01-13. https://www.forrester.com/press-newsroom/forrester-impact-ai-jobs-forecast/ (rehire-survey range via HR Executive, 2026-04-21: https://hrexecutive.com/as-ai-layoff-regret-surges-will-boomerang-employees-make-a-comeback/)

[17] AI is simultaneously aiding and replacing workers — Federal Reserve Bank of Dallas, 2026-02-24. https://www.dallasfed.org/research/economics/2026/0224

[18] The Anthropic Economic Index — Anthropic, 2025-02-10. https://www.anthropic.com/research/the-anthropic-economic-index

[19] The Simple Macroeconomics of AI — Daron Acemoglu, NBER Working Paper w32487 / Economic Policy, 2024/2025. https://www.nber.org/papers/w32487

[20] FinOps for agents: loop limits, tool-call caps, and the new unit economics of agentic SaaS — Nikhil Mungel, InfoWorld, 2026-03-02. https://www.infoworld.com/article/4138748/finops-for-agents-loop-limits-tool-call-caps-and-the-new-unit-economics-of-agentic-saas.html

[21] Tokens got 99.7% cheaper — why did your AI bill triple? — NavyaAI, 2026-02. https://navyaai.com/reports/ai-cost-report-token-prices-vs-ai-bill (vendor-sourced; directional only)

[22] BCG ~$3.6B / ~25% of revenue from AI — BCG to Bloomberg (via Metaintro), 2026-04-23. https://www.metaintro.com/blog/bcg-25-percent-ai-revenue-consulting-jobs-2026

[23] CloudZero $56M Series C — "The AI ROI Company" — CloudZero press release, 2025-05-28. https://www.cloudzero.com/press-releases/20250528/

[24] FinOps for AI Overview / State of FinOps 2026 — FinOps Foundation, 2025–2026. https://www.finops.org/wg/finops-for-ai-overview/ (membership/spend data: https://data.finops.org/)

[25] Nvidia's Jensen Huang on AI tokens on top of salary — CNBC, 2026-03-20. https://www.cnbc.com/2026/03/20/nvidia-ai-agents-tokens-human-workers-engineer-jobs-unemployment-jensen-huang.html

[26] Meta killed its employee AI token dashboard — Fortune, 2026-04-09. https://fortune.com/2026/04/09/meta-killed-employee-ai-token-dashboard/ (the "$500K/month single engineer" figure traces to one X user and is NOT corroborated — IBTimes UK, 2026-05-28, hedged)

[27] Microsoft is discontinuing Claude Code internally (Notepad) — Tom Warren, The Verge, 2026-05. https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad (standardization on Copilot CLI, not a cost verdict; engineers reportedly preferred Claude Code)

[28] The GenAI Divide: State of AI in Business 2025 — MIT NANDA (Challapally), 2025-08-18 (via Fortune). https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf (contested — Roetzer, Marketing AI Institute, 2025-08-26: https://www.marketingaiinstitute.com/blog/mit-study-ai-pilots; Wharton's Kevin Werbach independently questions the figure)
