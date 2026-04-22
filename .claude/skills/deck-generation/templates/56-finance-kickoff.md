<!-- TEMPLATE: finance-kickoff
     CATEGORY: Finance
     USE WHEN: annual finance team kickoff meeting — year-in-review + year-ahead planning
     SLIDE COUNT: 10
     PALETTE: Warm corporate
     RENDER: marp --pptx 56-finance-kickoff.md -->

---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  :root {
    --warm: #faf7f2;
    --navy: #0e1b2e;
    --amber: #f0a050;
    --muted: #5a6a7a;
    --rule: #e0d8cc;
    --green: #2a7d5f;
    --blue: #2c6fad;
  }
  section {
    background: var(--warm);
    color: var(--navy);
    font-family: 'Segoe UI', system-ui, sans-serif;
    padding: 50px 62px;
  }
  h1 {
    font-size: 1.85rem; font-weight: 700; color: var(--navy);
    letter-spacing: -0.3px; border-bottom: 3px solid var(--amber);
    padding-bottom: 9px; margin-bottom: 22px;
  }
  h2 { font-size: 1.2rem; font-weight: 600; color: var(--amber); margin-bottom: 12px; }
  ul { margin: 0; padding-left: 1.4em; }
  li { margin-bottom: 10px; font-size: 1.0rem; line-height: 1.55; }
  table { width: 100%; border-collapse: collapse; font-size: 0.92rem; margin-top: 10px; }
  th { background: var(--navy); color: var(--warm); padding: 7px 11px; text-align: left; }
  td { padding: 6px 11px; border-bottom: 1px solid var(--rule); }
  tr:nth-child(even) td { background: #f0ebe2; }
  .label {
    display: inline-block; background: var(--amber); color: var(--warm);
    font-size: 0.68rem; font-weight: 700; letter-spacing: 1px;
    text-transform: uppercase; padding: 2px 9px; border-radius: 3px; margin-bottom: 10px;
  }
  .win-card {
    background: white; border-left: 4px solid var(--amber); border-radius: 6px;
    padding: 14px 18px; margin-bottom: 12px; font-size: 0.96rem;
  }
  .win-card strong { color: var(--navy); }
  .goal-row { display: flex; gap: 18px; margin-top: 16px; }
  .goal {
    flex: 1; background: var(--navy); color: white;
    border-radius: 8px; padding: 16px 20px;
    border-top: 4px solid var(--amber);
  }
  .goal .title { font-size: 0.88rem; font-weight: 700; color: var(--amber); margin-bottom: 8px; }
  .goal .desc { font-size: 0.84rem; color: #c0cfd8; line-height: 1.4; }
  section.cover {
    background: var(--navy); color: white;
    display: flex; flex-direction: column; justify-content: center;
  }
  section.cover h1 { color: white; border-color: var(--amber); font-size: 2.2rem; }
  section.cover .sub { color: var(--amber); font-size: 1.0rem; margin-top: 8px; }
  section.cover .meta { color: #8899ac; font-size: 0.85rem; margin-top: 20px; }
  section.theme {
    background: var(--amber); color: var(--navy);
    display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;
  }
  section.theme h1 { color: var(--navy); border: none; font-size: 2.4rem; letter-spacing: -0.5px; }
  section.theme p { font-size: 1.1rem; color: #3a2800; max-width: 700px; }
  section.close { background: var(--navy); color: white; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; }
  section.close h1 { color: var(--amber); border: none; font-size: 2.0rem; }
  section.close p { color: #8899ac; font-size: 1.0rem; }
---

<!-- _class: cover -->

<div class="label">Finance Team Annual Kickoff — 2027</div>

# Northwind Capital Finance Team
## 2026 in Review &amp; 2027 Roadmap

<div class="sub">Building the Finance function that earns a seat at the strategy table</div>
<div class="meta">January 9, 2027 &nbsp;|&nbsp; Finance All-Hands &nbsp;|&nbsp; New York + Remote</div>

<!-- Presenter notes: Good morning, everyone — happy new year and welcome to our 2027 Finance Team Kickoff. Thank you for traveling in or joining remotely; I know January kickoffs compete with a lot, so I appreciate the commitment. We have two hours together today. The agenda follows our annual format: look back at 2026 — what we achieved and what we learned — then look ahead to 2027 with our theme, goals, priorities, and how we want to work together. This is not a budget review (you have all seen the AOP). This is a team meeting about who we are as a Finance function and what we want to be known for inside Northwind Capital. I want this to be interactive — please use the chat or raise your hand to add context, push back on my framing, or share perspective. This deck is internal-only. We have 28 people in this room/call today — the full Finance and Accounting team. Let us get started. -->

---

# 2026 — The Year in Numbers

<div class="label">What We Achieved</div>

<div class="goal-row">
  <div class="goal">
    <div class="title">Revenue</div>
    <div class="desc">$187.2M actual vs. $185M plan — third consecutive year of revenue beat</div>
  </div>
  <div class="goal">
    <div class="title">EBITDA</div>
    <div class="desc">$27.8M — 14.8% margin, up 190 bps YoY; operating leverage is real</div>
  </div>
  <div class="goal">
    <div class="title">Cash</div>
    <div class="desc">$49.8M in liquidity; debt-free Q3; record free cash flow $19.6M</div>
  </div>
  <div class="goal">
    <div class="title">Close Cycle</div>
    <div class="desc">Monthly close reduced from 8 days to 5 days — Finance team achievement</div>
  </div>
</div>

Every financial KPI met or exceeded in 2026. That is a team result — not a CFO result.

<!-- Presenter notes: I want to start with the numbers because they matter and because the team deserves to see them in context. These are not just company results — they reflect the quality of our financial infrastructure. We can close in 5 days because the accounting team built a close process that works. We can report 18 KPIs to the board in real time because our FP&A team built the models and dashboards to support it. We can navigate Q3 preliminary results and a CFO board briefing on the same day because our team has built the analytical muscle and processes to do both simultaneously. I am proud of every one of these numbers, but I am most proud of the close cycle improvement. Going from 8 days to 5 days in one year — without adding headcount — is a genuine operational achievement that directly affects every business decision in this company. The CEO mentions it to me regularly. It matters. Before we move on, I want to give the floor to the Controller to highlight one or two specific contributors to the close improvement — this should be a team celebration moment, not a management talking point. -->

---

# 2026 Wins — What We Built

<div class="label">Capabilities Delivered by Finance This Year</div>

<div class="win-card"><strong>Pipeline Forecasting Model</strong> — Built bottoms-up Capital Markets forecast that predicted Q3 revenue within 2.1%; adopted by CEO for investor guidance calibration</div>
<div class="win-card"><strong>Board Reporting Automation</strong> — Automated board package production saving 3 days/quarter of FP&A time; zero manual errors in H2</div>
<div class="win-card"><strong>Revenue Leakage Audit</strong> — Identified $1.4M in systematic underbilling; directly drove the Salesforce FSC investment decision; Finance team initiated the fix</div>

The revenue leakage audit was the single most impactful Finance initiative in 2026. It changed a technology investment decision at the executive level.

<!-- Presenter notes: I want to highlight three specific wins because they illustrate what Finance can do when we go beyond reporting and into analysis. The pipeline forecasting model is a good example of FP&A doing what FP&A should do — building a model that helps leadership make better decisions, not just reporting what happened. When our model predicted Q3 revenue within 2.1% of actuals, the CEO started sharing the model's outputs with the board. That is Finance earning credibility by being right. The board reporting automation is a quality-of-life win for the team but also a credibility win with the board — they noticed immediately when the board package became cleaner, faster, and error-free. The revenue leakage audit deserves special recognition. David Chen in our FP&A team identified the pattern during a routine billing reconciliation in Q1 — he flagged it, the Controller escalated it, and we ended up presenting a $1.4M finding to the CFO that directly changed a $2.8M investment decision. That is the Finance team acting as a strategic partner, not a back-office function. David, if you are on the call, thank you. This is exactly the mindset I want the whole team to bring to 2027. -->

---

# 2026 Lessons — What We Would Do Differently

<div class="label">Honest Retrospective</div>

- **Forecast communication lag:** Our models were accurate but we communicated updates to business leaders 2–3 weeks late in Q2; by then, decisions had already been made with stale data — we need faster forecasting cycles
- **Segment CFO partnership:** Finance is too reactive with Lending; we wait for them to ask rather than proactively delivering insight — this cost us visibility into the Q2 covenant watch-list situation
- **Onboarding gap:** Two new team members in H1 felt undertrained on our planning tools for 60+ days; our onboarding process needs to be rebuilt to match team growth

Not failures — these are the specific things we are fixing in 2027.

<!-- Presenter notes: I want to spend real time on this slide because the lessons are more important than the wins for what we build next. On forecast communication: our internal data shows that we updated our rolling forecast models on average every 3 weeks in 2026, but we communicated updates to business leaders in writing only monthly, in the FP&A review deck. In Q2, the CRO made a hiring decision with an outdated revenue assumption because we had not communicated a material forecast change for 3 weeks. We need a faster communication cadence — not more meetings, but a weekly one-page executive summary when there is a material change to the forecast. On segment partnership: the Lending situation in Q2 was a miss. Two facilities were approaching covenant thresholds and Finance did not know until the CCO disclosed it in a meeting. We should have been proactively monitoring covenant compliance monthly and flagging emerging risks. We are implementing a monthly Lending credit dashboard in Q1 2027. On onboarding: this one is on me. I approved three hires in H1 without building the onboarding infrastructure to support them. Our two H1 hires, Jennifer and Raj, both told me in their 90-day reviews that they felt lost on our planning tools for the first two months. We are building a structured 30-60-90 Finance onboarding program before any Q1 2027 hires start. -->

---

<!-- _class: theme -->

# 2027 Theme — "Finance as the Early Warning System"

We are not the scorekeepers. We are the radar.

Our job in 2027 is to surface risks and opportunities before they become headlines, give business leaders the insights they need to make better decisions faster, and make Northwind's financial infrastructure match the caliber of the company we are becoming.

<!-- Presenter notes: Every year I give the Finance team a theme — a short phrase that captures what we are optimizing for as a function. Last year's theme was "Close Quality and Speed," which drove the 5-day close achievement. This year's theme is "Finance as the Early Warning System." Let me explain what I mean. In 2026, we built great financial infrastructure — close processes, models, automation. That foundation is now in place. In 2027, I want us to use that foundation to become the people who see things coming before they happen. The revenue leakage audit David did in Q1 is the perfect example: he found a $1.4M problem before anyone else did, because he was looking for it. I want that instinct institutionalized across the whole team. The "radar" metaphor is intentional. Radar does not respond to the storm — it sees the storm forming and gives you time to act. Finance in 2027 should be the radar for Northwind Capital's leadership team. This theme shapes everything that follows: our goals, our priorities, our capabilities investments, and how we structure our work. When you are deciding whether something is a Finance responsibility, ask: "Does this help us see things earlier?" If yes, prioritize it. -->

---

# 2027 Goals — The Four Outcomes We Own

<div class="label">Finance Function Goals</div>

| # | Goal | Measure of Success | Owner |
|---|---|---|---|
| 1 | Weekly forecast signal to business leaders | Distributed every Monday by 9 AM; adopted by 3+ segment leads | FP&A Lead |
| 2 | Proactive credit monitoring dashboard | Covenant breach risk flagged ≥30 days in advance, 100% of facilities | Controller |
| 3 | Salesforce FSC financial data quality | Zero billing errors post-go-live; revenue recognition lag &lt;24hrs | Finance Ops |
| 4 | Finance team NPS (internal) | Score ≥70 from business partners in H2 2027 survey | CFO |

These four goals, delivered, will change how this company views its Finance function.

<!-- Presenter notes: These four goals are the specific outcomes I am committing the Finance team to in 2027. They are not activities — they are measurable outcomes with clear success definitions. Goal 1 addresses the forecast communication problem we identified in 2026. The weekly signal does not need to be comprehensive — it should be one page, four numbers, and any material changes with a brief explanation. The measure of success is not that we send it; it is that business leaders actually use it. I will ask the segment leads in Q2 whether the weekly signal is influencing their decisions. Goal 2 addresses the Lending visibility gap. The credit monitoring dashboard will pull facility balances, covenant ratios, and trend data weekly from our loan management system. Any facility approaching 90% of a covenant threshold triggers an automatic alert to the Controller and CFO. Goal 3 is the technology goal — the Salesforce FSC go-live in January will create a period of transition risk for revenue recognition. Our job is to ensure that the transition does not create billing errors or recognition delays. Zero errors and 24-hour recognition lag is the target. Goal 4 may surprise you — measuring Finance's NPS with internal partners is new. But if we are going to claim we are strategic partners, we should be willing to be measured by the people we serve. I will survey segment leads and the executive team in Q3 and share the results with the full team. -->

---

# Team Priorities — What We Focus On

<div class="label">How We Allocate Capacity in 2027</div>

| Priority | Q1 Focus | Q2–Q3 Focus | Q4 Focus |
|---|---|---|---|
| Salesforce FSC transition | Go-live support; data validation | Productivity monitoring; benefit tracking | Year-end reporting on new platform |
| Forecast infrastructure | Weekly signal process design | Refine based on adoption feedback | AOP 2028 modeling |
| Lending credit monitoring | Dashboard build | Full deployment | Quarterly review with CCO |
| Onboarding program | Build 30-60-90 framework | First use with Q1 hires | Refine based on feedback |

- No new Finance initiatives in H1 until core priorities are stabilized
- FP&A: 60% forward-looking analysis, 40% historical reporting (shift from current 40/60)
- Accounting: close quality is non-negotiable; 5-day close maintained through platform transition

<!-- Presenter notes: The quarterly priority table gives each part of the Finance team clarity on what to focus on each quarter. I want to be direct about one constraint: we are not taking on new Finance initiatives in H1 until the Salesforce FSC transition is stable. The transition is a significant operational risk, and I want the team fully focused on making it succeed. I know there are several interesting projects on the backlog — the private credit fund financial modeling, the M&A due diligence framework, the treasury risk dashboard. Those are good ideas and we will get to them. But they are H2 priorities at earliest. The FP&A capacity rebalancing is important: today we spend about 40% of FP&A time on forward-looking analysis (models, forecasts, scenario planning) and 60% on historical reporting (actuals, variance commentary, board packages). I want to flip that ratio by end of year. The automation we built in 2026 should enable this — the board package now takes 30% less time to produce, and that time should flow into analytical work. For the accounting team: the 5-day close must be maintained through the Salesforce FSC transition. This is not negotiable. If the transition creates close risks, escalate immediately rather than trying to solve it silently. -->

---

# Capabilities We Are Building in 2027

<div class="label">Skills and Systems Investment</div>

- **FP&A analytics upgrade** — Snowflake data warehouse go-live Q1; Power BI dashboards for all three segments by Q2; eliminates manual data pulls
- **Credit monitoring tooling** — Custom Salesforce dashboard for covenant tracking; built in Q1 alongside FSC go-live
- **Finance team training** — All FP&A analysts complete Power BI certification by Q2; all accounting staff complete Salesforce FSC certification by March 31
- **Structured onboarding** — 30-60-90 program covering tools, processes, and stakeholder relationships; first cohort: Q1 hires

<!-- Presenter notes: The capabilities investments align directly with our four goals. The Snowflake data warehouse migration is the infrastructure foundation for the weekly forecast signal and the credit monitoring dashboard — both rely on real-time data that today requires manual extraction. The Power BI dashboard investment is the interface layer: once we have Snowflake as the data source and Power BI as the visualization layer, the FP&A team can serve real-time insights to business leaders without rebuilding reports from scratch each time. On training: I am requiring Power BI certification for all FP&A analysts because it is becoming the standard tool for financial analysis at Northwind, and I want the team to be skilled rather than self-taught. The Salesforce FSC certification for accounting staff is equally important — we are going to depend on this platform for revenue recognition, and the team needs to understand it deeply, not just use it superficially. The onboarding program is a team investment: I am asking our most experienced team members to contribute to the 30-60-90 curriculum. Julia Reyes will lead the onboarding program design; please support her when she reaches out in February. Building this program is an investment in team quality that pays dividends for years. -->

---

# How We Work — Finance Team Operating Principles

<div class="label">Our Norms and Rituals</div>

- **Weekly Finance signal** — Monday 9 AM ET; CFO distributes; FP&A owns the draft by Friday noon
- **Monthly FP&A review** — 2nd Tuesday of the month; segment finance leads attend; Finance team prepares, does not just present
- **Quarterly retrospective** — Last Friday of each quarter; Finance team only; wins, lessons, and process changes
- **"Radar" standard** — When bringing an issue to the CFO, bring it with a timeline ("this will become a problem by X"), not just a description

<!-- Presenter notes: The operating principles slide captures the four behavioral norms I want the Finance team to internalize in 2027. The weekly Finance signal is a new ritual — the FP&A team owns the draft and submits to my office by Friday noon so I can review and distribute Monday morning. This requires a discipline change: FP&A needs to have a working view of the current week's forecast ready by Thursday. I know that is a tighter cadence than we are used to. If Friday noon is not achievable in Q1, we will adjust — but let us try to hit it from week one. The monthly FP&A review cadence has been in place since 2024 and works well. The refinement I am adding: the Finance team should come to that meeting having already identified the most important insights, not waiting for the business leaders to ask the right questions. Prepare to lead the conversation, not just answer it. The quarterly retrospective is new — patterned on what software engineering teams call a sprint retrospective. The last Friday of each quarter, the Finance team meets for 90 minutes to discuss: what went well, what did not, and what we are changing. No business leaders, no presentations. Just the team. The "radar" standard applies to how we communicate risks to the CFO: when you bring me a problem, tell me when it will become material if not addressed, not just that it exists. "The Drew facility is at 88% of the covenant" is a description. "The Drew facility will breach in 6 weeks if revenue does not recover" is radar. That is what I need from the team. -->

---

<!-- _class: close -->

# 2027 Starts Now

**The Finance team that built a 5-day close in 2026**
**will build the early warning system in 2027.**

Questions and open discussion: 10:00 AM – 10:30 AM ET

Team lunch: 12:00 PM at Gramercy Tavern (NYC) / $50 DoorDash credit (Remote)

<!-- Presenter notes: I want to close with the same message I opened with: everything we accomplished in 2026 was a team result. The $187M revenue, the debt-free balance sheet, the 5-day close, the revenue leakage audit — all of it happened because this team showed up and did the work. I am proud to be your CFO and I am genuinely excited about what we can build together in 2027. The theme of Finance as the Early Warning System is not just a slogan — it is an invitation to be more than a reporting function. Radar operators are not passive; they are active, vigilant, and they sound the alarm before it is too late. That is who I want us to be for Northwind Capital. Before we go to Q&A, I want to hear from the team. What did I miss in the 2026 review? What are you most excited about in 2027? What do you need from me that I am not currently providing? This is the right room and the right moment to have that conversation. I am opening the floor now — NYC, please raise hands; remote, please use the chat. We have 30 minutes before we break for the segment deep dives. -->
