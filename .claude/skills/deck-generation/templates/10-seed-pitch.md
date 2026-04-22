<!-- TEMPLATE: 10-seed-pitch  CATEGORY: Executive / Pitch  USE WHEN: Pre-seed or seed fundraise — early-stage pitch covering problem, insight, solution, market, team, traction, ask  SLIDE COUNT: 10  PALETTE: Dark premium with purple accent (#0a0e14 bg, #d0d8e4 text, #ffffff headings, #a78bfa accent)  RENDER: marp --pptx 10-seed-pitch.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section { font-family: 'DM Sans', system-ui, sans-serif; background: #0a0e14; color: #d0d8e4; padding: 60px 80px; }
  h1 { font-family: 'DM Serif Display', Georgia, serif; color: #ffffff; letter-spacing: -0.5px; font-size: 2em; margin-bottom: 0.3em; }
  h2 { color: #a78bfa; font-size: 0.95em; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 1em; }
  strong { color: #ffffff; }
  em { color: #a78bfa; font-style: normal; }
  table { width: 100%; border-collapse: collapse; font-size: 0.88em; }
  th { background: #111820; color: #a78bfa; padding: 10px 16px; text-align: left; border-bottom: 2px solid #a78bfa; }
  td { padding: 10px 16px; border-bottom: 1px solid #1e2a38; color: #d0d8e4; }
  .big { font-size: 2.8em; font-weight: 700; color: #ffffff; display: block; line-height: 1.1; letter-spacing: -0.02em; }
  .label { font-size: 0.8em; color: #8899ac; text-transform: uppercase; letter-spacing: 0.06em; display: block; margin-top: 6px; }
  .pill { display: inline-block; background: #1a1228; border: 1px solid #a78bfa; color: #a78bfa; padding: 4px 14px; border-radius: 100px; font-size: 0.78em; margin-right: 8px; }
  .grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 36px; margin-top: 20px; }
  .grid3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 24px; }
  .card { background: #111820; border-left: 4px solid #a78bfa; padding: 20px 24px; border-radius: 4px; }
  .card-blue { background: #111820; border-left: 4px solid #3b9eff; padding: 20px 24px; border-radius: 4px; }
  .muted { color: #8899ac; font-size: 0.88em; }
  .stat { background: #111820; border: 1px solid #1e2a38; border-top: 3px solid #a78bfa; padding: 20px; border-radius: 4px; text-align: center; }
---

# Helix
## Seed Round &nbsp;|&nbsp; April 2026

**Prior authorization, solved.**

AI that tells clinicians which treatments will be approved — before they ask.

<span class="pill">Pre-Revenue &#8594; $142K MRR</span><span class="pill">Healthcare AI</span><span class="pill">Seed $3M</span>

<!-- Speaker notes:
This is a seed pitch. Seed investors buy the team and the insight, not the business — because at seed stage there is not enough business yet to buy. Open with the clearest possible statement of what Helix does: it predicts prior-auth approval before the clinician submits the request. That is a specific, demonstrable capability. Avoid the temptation to open with market size or problem statistics — seed investors hear those every day. Open with the behavior change you enable. We went from zero to $142K MRR in 14 months, which is unusually fast for healthcare enterprise software. That headline signals that the problem is real, the product works, and the sales motion is not blocked by the typical healthcare procurement friction. The seed round is $3M. We will use it to reach $500K MRR and Series A readiness — specifically, to prove that the land-expand motion works in three different health system archetypes (academic medical center, community hospital, independent physician group) before we scale the sales team. This deck is 10 slides and takes 18 minutes. We have left 12 minutes for questions.
-->

---

# The Problem

## PA Is the Number-One Reason Treatments Are Delayed

<div class="grid2">
  <div>
    <p><strong>3.4 billion</strong> PA requests per year in the US</p>
    <p><strong>13.4 hours/week</strong> of physician time lost to PA paperwork</p>
    <p><strong>47%</strong> of complex PA requests are denied on first submission</p>
    <p><strong>1 in 4 patients</strong> abandon care when PA takes &gt; 2 weeks</p>
  </div>
  <div class="card">
    <p style="margin:0; font-size:0.9em; line-height:1.9;">A cardiologist wants to prescribe a specialty drug.<br><br>
    She opens 3 systems to pull the patient history.<br>
    She fills out a 14-page payer form — by hand.<br>
    She faxes it. She waits 11 days. It is denied.<br>
    She appeals. She waits 7 more days.<br><br>
    The patient has moved on.</p>
  </div>
</div>

<!-- Speaker notes:
Seed pitches live or die on problem conviction. The cardiologist vignette on the right side of this slide is based on a real composite case from our first customer interview round — 40 clinicians across 8 health systems in September 2024. We use the narrative format because it is more memorable than the statistics alone, and because seed investors need to feel the problem in order to fund the solution. The four statistics on the left are all sourced — AMA 2025 administrative burden report, AHIP outcomes study, and CMS claims data. The 47% first-submission denial rate for complex cases is the most important number: it means that nearly half of all PA requests require a second submission or appeal, which doubles the labor and doubles the delay. Our insight — which the next slide explains — is that this denial rate is not random. It is predictable. And if it is predictable, it is preventable. The patient abandonment statistic (1 in 4 abandoning care after a 2-week delay) is the one that resonates most with clinician buyers. It is also the one that makes CFOs uncomfortable, because a patient who abandons care often returns later with a more expensive, more acute condition — the worst possible outcome for a health system operating under value-based contracts.
-->

---

# The Insight

## Denials Are Predictable — Therefore Preventable

<div class="card" style="margin-bottom: 28px;">
  <strong>Counterintuitive finding from our research:</strong><br>
  <span style="font-size:0.92em; line-height:1.8; display:block; margin-top:8px;">Payer denial decisions follow 94% reproducible patterns across diagnosis code, treatment type, and payer ID. A model trained on historical outcomes can predict approval probability with higher accuracy than a trained human reviewer — before the request is submitted.</span>
</div>

**What this unlocks:**
- Submit only requests with &gt; 85% approval probability as-is
- Pre-modify borderline requests with supporting documentation before first submission
- Flag likely denials for physician review before patient commitment to treatment

**Why nobody has done this:** The training data was locked inside individual health systems. We built the dataset access layer first.

<!-- Speaker notes:
The insight slide is the most important slide in a seed pitch. It is the moment where the investor either understands why you will win or does not. The insight is not "prior auth is broken" — that is the problem. The insight is that denials are statistically deterministic. Payers follow their own coverage policies. Those policies produce patterns. Those patterns are learnable. A model trained on 18 months of retrospective PA outcomes from a single health system can predict first-submission approval with 91% accuracy for that payer-diagnosis combination. A model trained across multiple health systems and multiple payers reaches 94% accuracy because it learns cross-payer patterns that individual health systems cannot see. The "why nobody has done this" answer is the moat explanation at seed stage: the training data was distributed across thousands of health systems, each with its own EHR and its own payer mix, each with no incentive to share. We built the data-sharing agreement infrastructure — standardized BAA language, FHIR-based data extraction, de-identification pipeline — before we built the model. That infrastructure is itself a barrier to replication. A competitor has to build what we built before they can even start training.
-->

---

# The Solution

## Helix — Predict, Pre-populate, Submit

<div class="grid3">
  <div class="stat">
    <em style="font-size:1.5em; font-weight:700;">Predict</em>
    <span class="label" style="margin-top:12px;">AI scores approval probability before submission. Clinician sees confidence level inline in their EHR.</span>
  </div>
  <div class="stat">
    <em style="font-size:1.5em; font-weight:700;">Pre-populate</em>
    <span class="label" style="margin-top:12px;">Helix pulls the correct payer form and fills it from EHR data automatically. Zero manual entry.</span>
  </div>
  <div class="stat">
    <em style="font-size:1.5em; font-weight:700;">Submit</em>
    <span class="label" style="margin-top:12px;">Submits via payer FHIR API or auto-fax. Tracks status. Flags denials for one-click appeal.</span>
  </div>
</div>

<div style="margin-top: 32px;">
  <strong>Integration model:</strong> Embedded panel inside Epic, Cerner, Meditech — no new login, no behavior change required<br>
  <strong>Data model:</strong> De-identified, aggregated; no PII leaves the customer VPC
</div>

<!-- Speaker notes:
The solution slide must answer three questions: what does it do, how does the user experience it, and why is it safe? The three-step framework — Predict, Pre-populate, Submit — maps directly to the three failure points in the current PA workflow: uncertainty about approval before submission, manual data entry from multiple sources, and manual tracking through a slow payer process. The integration model point is the most important for healthcare enterprise buyers: zero new login. Clinicians have an average of 11 different systems they log into during a shift. Adding a 12th system with a new credential produces abandonment rates above 70% in the first 30 days. Helix appears as a panel inside the EHR the clinician is already using. The data model point answers the compliance question before it is asked. In every discovery call, the first technical question from the health system IT team is "where does the patient data go?" The answer is: nowhere. The model runs inference inside the customer's Azure VPC. De-identified aggregate patterns are shared across customers to improve the model — the same model-as-a-service pattern used by Google Health's sepsis prediction model, which has been cleared by health system privacy officers at 40+ academic medical centers.
-->

---

# Market — Sized from the Bottom

## $4.8B Reachable in 36 Months

<div class="grid2">
  <div>
    <p><strong>Segment 1 — Health Systems</strong><br>
    6,090 US hospitals<br>
    Avg ACV: $72K<br>
    <em>Reachable: $438M</em></p>
    <p style="margin-top:20px;"><strong>Segment 2 — Physician Practices</strong><br>
    250,000+ independent practices (PA-heavy specialties)<br>
    Avg ACV: $18K<br>
    <em>Reachable: $4.5B</em></p>
  </div>
  <div class="card">
    <strong>Why this is conservative:</strong>
    <ul style="margin-top: 12px; font-size:0.88em; line-height:2;">
      <li>Does not include payer-side processing ($12B)</li>
      <li>Does not include denial appeal automation ($8B)</li>
      <li>Does not include international markets</li>
      <li>CMS mandate forces every payer to expose PA API — grows addressable base annually</li>
    </ul>
  </div>
</div>

<!-- Speaker notes:
Market size at seed stage should be expressed in terms of what you can actually reach with the capital you are raising, not the total theoretical addressable market. The $4.8B reachable market figure is the number of US hospitals and physician practices that do prior authorization and could adopt a SaaS tool, multiplied by our current ACV. It is bottoms-up, not top-down. The physician practice segment is 10x the hospital segment in account count but at lower ACV — it is the long tail that becomes economically attractive once we build a self-serve onboarding flow. With $3M in seed capital, we are not addressing the physician practice segment directly — we are proving the health system motion. The physician segment is the Series A story. The "why this is conservative" card is important because seed investors are often skeptical of healthcare TAM claims — the market is large but the distribution is hard. We show the conservative case and note that the expansion markets (payer-side, denial appeal, international) are real but not in our plan. That discipline signals financial maturity, which is rare at seed stage and builds investor confidence in our ability to allocate capital.
-->

---

# Why Us

## Three Unfair Advantages

<div class="grid3">
  <div class="card">
    <strong>Domain Depth</strong>
    <p style="font-size:0.85em; margin-top:8px; line-height:1.8;">CEO is a former CMIO. CMO wrote the CMS interoperability rules. We are not outsiders learning the industry — we are the industry building a tool for ourselves.</p>
  </div>
  <div class="card">
    <strong>Data Moat</strong>
    <p style="font-size:0.85em; margin-top:8px; line-height:1.8;">18M labeled PA outcomes across 7 payers and 22 states. Took 14 months to build. Every new customer adds 200K samples per year. The model improves; the barrier rises.</p>
  </div>
  <div class="card">
    <strong>Regulatory Tailwind</strong>
    <p style="font-size:0.85em; margin-top:8px; line-height:1.8;">CMS FHIR mandate (Jan 2026) forces payers to expose PA APIs. We designed Helix for this infrastructure from day one. Competitors designed for fax and portal scraping.</p>
  </div>
</div>

<!-- Speaker notes:
"Why us" is the team and insight slide combined. At seed stage, investors fund the team's unfair advantage — the reason this team can win where others cannot. Domain depth: the founding team includes a physician who ran prior authorization at a top-10 US health system, and a former CMS policy official who designed the very regulations that created the market we operate in. This is not "we did research on the healthcare market." This is "we lived this problem and then we built the infrastructure for it." Data moat: 18 million labeled outcomes is not a number you get by signing up for a data broker. It required 14 months of data-sharing agreements with 22 health systems, custom FHIR extraction pipelines, and a de-identification process cleared by three health system IRBs. A new entrant has to build the same infrastructure before they can collect their first training sample. Regulatory tailwind: most healthcare AI startups fight regulatory headwinds. We designed Helix around the CMS FHIR API mandate before it took effect, which means our architecture is the compliance-forward architecture. Competitors who built on portal scraping are now facing a retooling cost that we have already paid. The mandate is a forcing function that makes Helix's approach the only architecturally compliant one for new deployments.
-->

---

# Why Now

## The 18-Month Window

<div class="grid2">
  <div class="card">
    <strong>Market window opened Jan 2026</strong>
    <p style="font-size:0.88em; line-height:1.8; margin-top:8px;">CMS FHIR mandate live. Payers legally required to expose PA APIs. Health systems actively evaluating FHIR-native PA tools for the first time. Window will close in 12-18 months as incumbents retool.</p>
  </div>
  <div class="card">
    <strong>Clinical LLM capability crossed the threshold</strong>
    <p style="font-size:0.88em; line-height:1.8; margin-top:8px;">GPT-4-class reasoning + domain-specific fine-tuning = 94% PA prediction accuracy. Two years ago: 71%. One year ago: 84%. The capability curve crossed clinical utility in Q3 2025 and we were positioned for it.</p>
  </div>
</div>

<p style="margin-top: 24px; font-size: 0.92em;">&#9656; Health system CFO budgets for AI: <strong>$0 in 2022 &#8594; avg $1.4M earmarked in 2025</strong> (HIMSS survey). The buyer is ready.</p>

<!-- Speaker notes:
Why now answers the question every seed investor asks but rarely says out loud: "Why didn't someone build this 3 years ago, and why won't someone bigger build it tomorrow?" Three years ago: the CMS mandate did not exist, so payers had no obligation to expose PA data via API, making FHIR-native architectures impossible. The clinical LLM capability was at 71% accuracy — useful for consumer applications but not for clinical decision support, where the bar for AI assistance is "better than the best human." Tomorrow: yes, Epic could build this. Epic has the distribution and the EHR integration. But Epic has 18 months of AI development lag in clinical AI specifically, and their incentive structure favors interoperability fees over point solution competition. Our Epic App Orchard partnership is partly insurance: if Epic decides to compete, we become a preferred Epic AI partner rather than a target. The CFO budget point closes the "who pays" question that seed investors ask about enterprise healthcare. In 2022, health system CFOs did not have an AI line item in their budget. In 2025, the average health system has $1.4M earmarked for AI tools. Helix is not asking them to create a new budget category — we are competing for a budget that already exists.
-->

---

# Traction

## 14 Months — $142K MRR, 94 Health Systems

<div class="grid3">
  <div class="stat">
    <span class="big">$1.7M</span>
    <span class="label">ARR — Month 14</span>
  </div>
  <div class="stat">
    <span class="big">94</span>
    <span class="label">Active Health Systems</span>
  </div>
  <div class="stat">
    <span class="big">112%</span>
    <span class="label">Net Revenue Retention</span>
  </div>
</div>

<div style="margin-top: 28px;">

| Milestone | Date | Significance |
|---|---|---|
| First paying customer | Month 3 | 18 days from first demo to signed contract |
| 10 health systems | Month 7 | Validated repeatable sales motion |
| CMS interoperability audit | Month 12 | Zero findings — opens federal market |
| Dignity Health (7 hospitals, $180K ACV) | Month 14 | Largest single logo — Catholic health system entry point |

</div>

<!-- Speaker notes:
Traction at seed stage is proof that the problem is real and the product works for someone other than the founders. $1.7M ARR in 14 months is exceptional for healthcare enterprise SaaS — the median Series A healthcare SaaS company takes 22 months to reach this ARR level. Three data points matter more than the headline ARR number. First, 18 days from first demo to signed contract at our earliest customers. Healthcare enterprise sales cycles average 90-120 days. Our first four customers signed in under 30 days because the PA problem was so acute and our demo showed measurable, immediate results. Second, 112% Net Revenue Retention. This is not a vanity metric — it is the signal that clinicians use the product after they sign. Healthcare SaaS has chronic adoption problems; tools get signed and shelved. 112% NRR means our customers are adding seats faster than they churn. Third, the Dignity Health deal. Dignity is one of 15 Catholic health system networks with a shared procurement committee. A Dignity adoption creates a warm referral path to 46 additional hospitals in the same network. We treat the Dignity deal as a distribution event, not just a revenue event. Seed investors should understand that the $180K ACV is the visible part; the network value behind it is larger.
-->

---

# Business Model

## Simple, Scalable, Defensible

<div class="grid2">
  <div>
    <strong>How we charge:</strong>
    <ul style="line-height: 2.2; margin-top: 12px;">
      <li>Per-department subscription: $18K–$45K/year</li>
      <li>Implementation fee: $12K one-time</li>
      <li>Add-on: denial appeal module — $28K/year</li>
      <li>Annual contracts (2-year preferred, 1-year available)</li>
    </ul>
  </div>
  <div>
    <strong>Unit economics (current):</strong>
    <ul style="line-height: 2.2; margin-top: 12px;">
      <li>Gross margin: <em>73%</em></li>
      <li>CAC payback: <em>8.7 months</em></li>
      <li>LTV / CAC: <em>6.8x</em></li>
      <li>Average contract: <em>$72K ACV, 24 months</em></li>
    </ul>
  </div>
</div>

<div class="card-blue" style="margin-top: 28px;">
  <strong>Path to profitability:</strong> Breakeven at $4.2M ARR — a Q1 2027 event at current growth rate. Seed capital bridges us there with 8 months of buffer.
</div>

<!-- Speaker notes:
Seed-stage business model slides should prove three things: the price is defensible, the margin is real, and the path to profitability is visible. On price defensibility: $18K–$45K per department per year is 3-4x cheaper than the status quo — a full-time PA coordinator earns $52K/year and handles fewer requests than Helix processes in a month. The ROI story writes itself, and we have the cost savings analysis from 23 customers to support it. On margin: 73% gross margin is already at Series B-level SaaS margins, which is unusual for a company this early. The reason is our inference cost structure — we use a distilled clinical model that runs at 1/3 the compute cost of GPT-4-class inference, and we amortize it across 94 customers. As we scale, the per-customer inference cost drops further. On breakeven: $4.2M ARR is 2.5x our current ARR. At 22% month-over-month growth — our 6-month trailing average — we reach that in 6 months. We are targeting a more conservative 15% MoM for the next 12 months, which puts breakeven at Q1 2027. The seed capital we are raising provides runway to breakeven with 8 months of buffer — meaning we are not a "must raise Series A or die" company. That negotiating position changes the quality of Series A conversations.
-->

---

# The Ask

## $3M Seed — 18 Months to Series A Readiness

<div class="grid2">
  <div>
    <strong>Use of funds:</strong>
    <ul style="line-height: 2.2; margin-top: 12px; font-size: 0.92em;">
      <li>Engineering: 2 ML engineers, 1 backend — <em>40%</em></li>
      <li>Sales: 1 enterprise AE, 1 SDR — <em>28%</em></li>
      <li>Customer success and implementations — <em>18%</em></li>
      <li>G&A, legal, SOC 2 audit — <em>14%</em></li>
    </ul>
  </div>
  <div>
    <strong>18-month milestones:</strong>
    <ul style="line-height: 2.2; margin-top: 12px; font-size: 0.92em;">
      <li>&#8594; $500K MRR ($6M ARR)</li>
      <li>&#8594; 250 health systems live</li>
      <li>&#8594; Denial appeal module in 50+ customers</li>
      <li>&#8594; SOC 2 Type 2 certified</li>
      <li>&#8594; Series A raise at $40M–$50M pre-money</li>
    </ul>
  </div>
</div>

Connect us to two health system CMIOs in your portfolio before May 15 — that is the highest-leverage action you can take. We close this round by June 1.

<!-- Speaker notes:
The ask slide must be specific on three dimensions: how much, what for, and what it buys. We are asking for $3M — not $5M, not $2M. The $3M figure is sized to reach the specific milestones that make Helix Series A-fundable at a $40M-$50M pre-money valuation, with 8 months of buffer. The use-of-funds breakdown is 40% engineering, 28% sales — a 68% allocation to revenue-generating activities. Healthcare SaaS companies that over-invest in G&A at seed stage create cost structures that compress margins before they establish product-market fit. We have kept G&A to 14%. The milestones are the commitments we are making in exchange for the capital. $500K MRR is the Series A threshold for healthcare enterprise SaaS in the current market. 250 health systems proves the sales motion at scale. SOC 2 Type 2 certification is required by 80% of health system enterprise procurement offices — without it, we are blocked from federal and academic medical center accounts. The CTA is specific: two CMIO introductions before May 15. Every seed investor in healthcare has portfolio companies with health system relationships. A warm introduction from a trusted investor compresses our sales cycle from 105 days to under 30 days. That is not a courtesy ask — it is the single fastest path to the milestones we just committed to.
-->
