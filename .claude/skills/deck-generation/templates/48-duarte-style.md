<!-- TEMPLATE: duarte-style
     CATEGORY: Creative / Narrative
     USE WHEN: Nancy Duarte "Resonate" method — oscillating what-is vs what-could-be, building to a call to action
     SLIDE COUNT: 12
     PALETTE: Cream #f9f6f0 / navy #0e1b2e / gold #b8965a / contrast highlight #e8f0fd
     RENDER: marp --pptx 48-duarte-style.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;600&display=swap');
  section {
    font-family: 'DM Sans', system-ui, sans-serif;
    background: #f9f6f0;
    color: #0e1b2e;
    padding: 60px 80px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  h1 {
    font-family: 'DM Serif Display', Georgia, serif;
    font-size: 2.8em;
    font-style: italic;
    letter-spacing: -0.5px;
    line-height: 1.05;
    color: #0e1b2e;
    margin: 0 0 0.2em 0;
  }
  h2 {
    font-size: 0.7em;
    font-weight: 600;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    margin: 0 0 0.8em 0;
    border: none;
    padding: 0;
  }
  h2.is { color: #8a7a6a; }
  h2.could { color: #b8965a; }
  h2.call { color: #0e1b2e; }
  h3 {
    font-size: 1.15em;
    font-weight: 300;
    color: #4a5568;
    margin: 0.5em 0 0 0;
    line-height: 1.5;
  }
  p {
    font-size: 0.88em;
    font-weight: 300;
    color: #6b6560;
    line-height: 1.75;
    max-width: 640px;
    margin: 0.6em 0 0 0;
  }
  strong { font-weight: 600; color: #0e1b2e; }
  /* IS slides — cream palette, muted, "ordinary world" */
  section.is {
    background: #f9f6f0;
  }
  section.is h1 { color: #3a3530; }
  /* COULD slides — elevated, slight blue tint, "new world" */
  section.could {
    background: #e8f0fd;
  }
  section.could h1 { color: #0e1b2e; font-style: normal; }
  section.could h2.could { color: #1a56b0; }
  section.could h3 { color: #1e3a6a; }
  section.could p { color: #3a5080; }
  /* CALL slide — gold accent, summit moment */
  section.call {
    background: #0e1b2e;
    color: #f9f6f0;
  }
  section.call h1 { color: #b8965a; font-style: normal; font-size: 3.4em; }
  section.call h2.call { color: #5a6888; }
  section.call h3 { color: #d0c4b0; }
  section.call p { color: #8a9ab8; }
  /* Opening: split emphasis */
  .contrast-pair {
    display: flex;
    gap: 3em;
    margin-top: 1.4em;
  }
  .contrast-left {
    border-left: 3px solid #c8bfb0;
    padding-left: 1.2em;
    flex: 1;
  }
  .contrast-right {
    border-left: 3px solid #b8965a;
    padding-left: 1.2em;
    flex: 1;
  }
  .contrast-left h4, .contrast-right h4 {
    font-size: 0.68em;
    font-weight: 600;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    margin: 0 0 0.4em 0;
  }
  .contrast-left h4 { color: #8a7a6a; }
  .contrast-right h4 { color: #b8965a; }
  .contrast-left p, .contrast-right p {
    font-size: 0.88em;
    max-width: none;
  }
  /* Gold rule */
  .gold-rule {
    width: 40px;
    height: 3px;
    background: #b8965a;
    margin: 0 0 1.6em 0;
  }
  /* Open eye / quote block */
  .big-quote {
    font-family: 'DM Serif Display', serif;
    font-style: italic;
    font-size: 2em;
    letter-spacing: -0.3px;
    line-height: 1.2;
    color: #0e1b2e;
    border-left: 4px solid #b8965a;
    padding-left: 1em;
    margin: 0.8em 0 0 0;
  }
  section.could .big-quote { color: #0e1b2e; border-left-color: #1a56b0; }
  section.call .big-quote { color: #b8965a; border-left-color: #b8965a; }
  footer {
    font-size: 0.6em;
    letter-spacing: 0.14em;
    color: #c8bfb0;
  }
  section.call footer { color: #3a4858; }
  section.could footer { color: #8090b8; }
---

## The Call to Action

<div class="gold-rule"></div>

<h1>The Cost of Routine.</h1>
<h3>A presentation to the Molina Healthcare Leadership Team on the case for agentic claims automation.</h3>

<!-- Speaker notes:
This is the Duarte "Resonate" structure. The opening slide is neither "what is" nor "what could be" — it is the frame. It names the tension before the first oscillation begins.

"The title of this presentation is: The Cost of Routine. We are going to spend the next 25 minutes examining what it costs your organization — in dollars, in capacity, and in opportunity — to run routine workflows with people who were hired to do something harder."

"This is not a technology pitch. It is a strategic argument. And like all strategic arguments, it has a structure: what is, what could be, what is, what could be — until the gap between those two states becomes impossible to ignore. Then the call to action."

"Let's begin."

Duarte opening principle: do not start with the solution. Start with the audience in their current world — the "ordinary world." The gold rule and serif italic headline set the tone: thoughtful, serious, credible.

Total slide time target: 25 seconds. -->

---

<!-- _class: is -->

## What is ◆ The Ordinary World

<div class="gold-rule" style="background:#c8bfb0;"></div>

<h1>A claims reviewer's day, exactly as it is.</h1>

<p>40-60 claims per shift. Each one requiring four system lookups, one eligibility check, and one coding verification. Every step manual. Every step repeated.</p>

<!-- Speaker notes:
First "what is" slide. Cream palette, muted gray rule. The ordinary world.

"Let me describe a claims reviewer's day — not as we wish it were, but as it actually is."

"She starts at 8am. She opens her queue: 52 claims. Each claim requires her to pull the member record from Salesforce, check eligibility in Availity, verify the procedure code against the clinical guidelines, and cross-reference any secondary codes. Then she makes a decision and documents it."

"She does this 52 times. The fastest claims take 6 minutes. The complex ones take 15. Her day is completely consumed by lookup and verification work."

"She was hired for her clinical judgment. She spends 80% of her day on data retrieval."

The muted, cream-on-cream palette communicates the dullness of the ordinary world. No drama. No color. This is the world as it is — and it is not exciting.

Total slide time target: 35 seconds. -->

---

<!-- _class: could -->

## What could be ◆ The New World

<h1>What if her day looked different?</h1>

<div class="big-quote">She arrives. Her queue is pre-analyzed. Every claim has a recommended decision with a plain-language explanation. She reviews, confirms, and handles the three claims that need her actual judgment.</div>

<!-- Speaker notes:
First "what could be" slide. Blue-tinted background. The possible world.

"What if her day started differently? The queue is still 52 claims. But when she opens it, 49 of them have a recommended decision from the AI system, with an explanation she can read and verify in 15 seconds. She confirms 49 in 12 minutes."

"She spends the remaining 5 hours on the three claims that actually need her clinical expertise: the multi-system coordination dispute, the member appeal with incomplete documentation, the DRG reclassification request."

"Her job has transformed. She is no longer a data retrieval system. She is a clinical decision-maker."

The "could be" slide uses a block quote — the Duarte "picture the future" technique. The quote is vivid and specific, not abstract. The audience should see the scene.

Total slide time target: 35 seconds. -->

---

<!-- _class: is -->

## What is ◆ The Ordinary World

<div class="gold-rule" style="background:#c8bfb0;"></div>

<h1>The queue grows faster than it can be cleared.</h1>

<div class="contrast-pair">
  <div class="contrast-left">
    <h4>Today</h4>
    <p>3.2-day average claim backlog. 73% of claims processed without AI assistance. $340M in estimated annual leakage.</p>
  </div>
  <div class="contrast-right">
    <h4>The implication</h4>
    <p>Backlog is not a staffing problem. It is a design problem. Adding reviewers does not fix a workflow designed for a different era.</p>
  </div>
</div>

<!-- Speaker notes:
Second "what is" slide. Back to the ordinary world — now with data.

"The queue grows faster than it can be cleared. This is not a performance issue with your reviewers — it is a math issue with the workflow design."

"At current throughput, the median claim backlog is 3.2 days. Industry best-in-class is same-day for routine claims and 48 hours for complex claims. You are 3x the benchmark on routine claims."

"Adding reviewers improves throughput linearly — each new reviewer adds their individual capacity. But the problem is not capacity. The problem is that each reviewer is spending 80% of their time on work that does not require a human. Adding humans to do human work in a human-speed system is not a solution."

"The solution is to change what humans are doing."

The contrast pair (today vs implication) uses the Duarte technique of placing the "what is" on the left (muted border) and the reframe on the right (gold border). The audience sees both simultaneously: the fact and its meaning.

Total slide time target: 40 seconds. -->

---

<!-- _class: could -->

## What could be ◆ The New World

<h1>The backlog disappears.</h1>

<h3>Because 80% of your claim volume is routine — and routine is exactly what AI does best.</h3>

<div class="contrast-pair" style="margin-top:1.4em;">
  <div class="contrast-right" style="border-left-color:#1a56b0;">
    <h4 style="color:#1a56b0;">Routine claims</h4>
    <p style="color:#3a5080;">Processed by AI in 22 seconds. Reviewed by human in 15 seconds. Done.</p>
  </div>
  <div class="contrast-right" style="border-left-color:#1a56b0;">
    <h4 style="color:#1a56b0;">Complex claims</h4>
    <p style="color:#3a5080;">Flagged by AI, routed to senior reviewer with full context pre-loaded. Human judgment where it counts.</p>
  </div>
</div>

<!-- Speaker notes:
Second "what could be" slide. The oscillation is building — the audience has now seen the problem twice and the possibility twice. The tension is accumulating.

"The backlog disappears. Not because you hired more people — because you removed the lookup work from the workflow entirely."

"Routine claims — 80% of your volume — are processed by AI in 22 seconds and confirmed by a reviewer in 15 seconds. Total: 37 seconds per claim. Compare that to your current 9.2 minutes."

"Complex claims are flagged immediately and routed to your most experienced reviewers — with the full member context, the clinical guideline comparison, and the secondary code analysis pre-loaded. The reviewer's first action is a clinical judgment, not a data lookup."

"The backlog does not shrink. It disappears."

The two-column layout in the "could" blue tint creates symmetry between the solution's two modes — routine and complex. Both are solved, differently.

Total slide time target: 40 seconds. -->

---

<!-- _class: is -->

## What is ◆ The Ordinary World

<div class="gold-rule" style="background:#c8bfb0;"></div>

<h1>$340 million leaves every year. Quietly.</h1>

<p>Secondary code leakage is invisible in a manual review workflow. The reviewer sees the primary code, verifies it, approves. The secondary code with the inflated reimbursement rate passes through unexamined.</p>

<div class="big-quote" style="font-size:1.3em; color:#3a3530; border-left-color:#c8bfb0;">$244 million of that $340 million lives in secondary codes alone.</div>

<!-- Speaker notes:
Third "what is" slide. The stakes escalate — we move from inefficiency to financial loss.

"I want to name the third dimension of the ordinary world: money leaving the organization quietly."

"Secondary code leakage is invisible in a manual review workflow. Your reviewers are trained to verify the primary code. The primary code — the main procedure — is almost always correct. It is the secondary codes, the modifier codes, the unbundling patterns, that create reimbursement inflation."

"A manual reviewer checking 52 claims per shift does not have the time or the pattern-recognition to catch secondary code anomalies. They are not missing something obvious — they are missing something that requires comparing this claim to 4.2 million other claims to identify as an outlier."

"The AI does not get tired. It compares every claim to every other claim. It finds the pattern."

The quote block makes the $244 million figure visceral — not a statistic, but a reality that sits in the room with the audience.

Total slide time target: 40 seconds. -->

---

<!-- _class: could -->

## What could be ◆ The New World

<h1>$230 million recovered. Year one.</h1>

<h3>At current model accuracy — 94% on secondary codes — the recoverable leakage is $230 million annually.</h3>

<p>That is what the ordinary world is costing you every year you do not act. Not as a projection — as a calculation based on your plan size, your claim mix, and our measured detection accuracy.</p>

<!-- Speaker notes:
Third "what could be" slide. The oscillation reaches its peak tension. The gap between "what is" and "what could be" is now $230 million, and the audience feels it.

"This is the number that changes the conversation."

"$230 million recovered in year one. At current model accuracy — 94% — without any fine-tuning on your specific claims data. With fine-tuning, which we complete during the calibration phase, the model typically reaches 96-97% accuracy on your specific coding patterns."

"This is not a projection built on assumptions. It is a calculation: your annual medical spend, multiplied by the published secondary code leakage rate for your plan type, multiplied by our measured detection accuracy. Every variable is either a known quantity or a measured result."

"I want to pause here and let that number sit."

Pause for 5 seconds.

"$230 million. Every year. Starting in year one."

This is the Duarte "starburst" moment — where "what could be" is stated at maximum specificity and the audience cannot avoid feeling the gap.

Total slide time target: 45 seconds including pause. -->

---

<!-- _class: is -->

## What is ◆ The Ordinary World

<div class="gold-rule" style="background:#c8bfb0;"></div>

<h1>The risk of waiting is compounding.</h1>

<div class="contrast-pair">
  <div class="contrast-left">
    <h4>Every quarter of inaction</h4>
    <p>$57.5M in unrecovered leakage. Widening gap between your reviewers' capacity and your claim volume growth. Competitors building the AI advantage.</p>
  </div>
  <div class="contrast-right">
    <h4>The compounding factor</h4>
    <p>Organizations that deploy agentic infrastructure early develop operational knowledge that late movers cannot buy. The second adopter starts 18 months behind.</p>
  </div>
</div>

<!-- Speaker notes:
Fourth "what is" — this one is the urgency slide. The ordinary world is not static — it is getting worse.

"The cost of inaction is not constant. It is compounding."

"Every quarter without AI-assisted review: $57.5 million in unrecovered leakage. Measured quarterly, that is one number. Measured over the deployment timeline — the 20 weeks from decision to production — that is $115 million that leaves between now and the day the system goes live."

"But the financial cost is the smaller part of the compounding risk. The larger part is organizational knowledge. Organizations that deploy agentic infrastructure now — this year — will have 18 months of production learning before organizations that wait until next year even start. That 18 months of data, of model refinement, of workflow adaptation — that is a structural advantage. It cannot be purchased. It has to be earned."

"The ordinary world does not stay still while you decide."

Fourth "what is" is the final warning before the call to action. Duarte structure: the audience must feel the urgency of the ordinary world at its sharpest before the call to action lands.

Total slide time target: 45 seconds. -->

---

<!-- _class: could -->

## What could be ◆ The New World

<h1>You decide to lead.</h1>

<h3>Not because you had perfect information. Because you had enough information and the will to act.</h3>

<div class="big-quote" style="font-size:1.2em; color:#0e1b2e; border-left-color:#1a56b0;">The organizations that will define healthcare operations in 2030 are making deployment decisions today.</div>

<!-- Speaker notes:
Final "what could be" — the aspirational frame. Not about the technology anymore. About the decision.

"I want to close the oscillation here. Not with another number. With a statement about what kind of organization you want to be."

"The question we are asking is not: do you believe AI works? You have the pilot data. You have the accuracy numbers. You have the ROI calculation. The question is whether you believe that acting now — with uncertainty, with imperfect information, with the discomfort of a new thing — is the right choice."

"The organizations that will define the next decade of healthcare operations are not waiting for certainty. They are acting with enough evidence to justify the risk."

"This is that moment."

Pause. Long pause. Then advance to the call to action.

Total slide time target: 35 seconds including pause. -->

---

<!-- _class: call -->

## The Call to Action

<h1>Decide today.</h1>

<h3 style="color:#d0c4b0; margin-top:0.6em;">Not this quarter. Not next month. Today — because the $230 million does not wait.</h3>

<div class="big-quote" style="font-size:1.1em; margin-top:1em;">We are proposing a three-phase engagement. Sign before the end of this month. Production in 30 days. ROI measured in 12 months. If we fall short, we work for free until we hit the target.</div>

<!-- Speaker notes:
The call to action is the summit of the Duarte oscillation — the highest "what could be" moment, stated as a directive. The dark navy background signals: we have left the ordinary world entirely. The gold text on navy is the most vivid color contrast in the deck.

"Decide today."

"Not because I am pressuring you. Because the math is simple: every day of indecision is $940,000 in unrecovered leakage. 30 days to make the decision and sign the contract is $28 million."

"We are proposing a three-phase engagement. If you sign this month, we have your environment provisioned in 10 business days. Model calibration starts immediately. Production in 30 days."

"And we back it with a guarantee: if year-one recovery falls below our projection, we work for free until we achieve it. We put that in the contract."

"The call to action is simple: yes or no. And I want to hear it in this meeting."

The Duarte CTA structure: restate the ask, provide the deadline, provide the consequence of inaction, provide the guarantee. Then stop talking.

Total slide time target: 50 seconds. -->

---

## Appendix ◆ Methodology

<div class="gold-rule"></div>

<h1>How we calculated $230 million.</h1>

<div class="contrast-pair">
  <div class="contrast-left">
    <h4>Input variables</h4>
    <p>Annual medical spend (client-provided). Secondary code leakage rate: 2.7% (industry benchmark, AHIP 2024). Plan size: 500,000 members.</p>
  </div>
  <div class="contrast-right">
    <h4>Model performance</h4>
    <p>94% accuracy on secondary code detection (measured: 48,000 pilot claims). False negative rate: 5.2%. Recovery calculation: leakage pool × detection rate.</p>
  </div>
</div>

<p style="margin-top:1.2em; font-size:0.8em;">Full methodology and raw pilot data available on request. Statistical analysis conducted by SponAItech research team. Reviewed by external actuarial consultant.</p>

<!-- Speaker notes:
The appendix slide is part of the Duarte methodology — after the call to action, provide the CFO slide. This is for the finance and compliance members of the audience who need to validate the number before it becomes a decision.

"For those of you who want to see the methodology — and you should — here it is."

"The leakage estimate uses the AHIP 2024 published secondary code leakage rate of 2.7% of medical spend. Applied to your plan's annual medical spend, that gives us the total leakage pool. The recovery figure is the leakage pool multiplied by our measured detection accuracy of 94%, minus the 5.2% miss rate."

"If you want the full actuarial review, we have it. If you want to run your own analysis on the pilot data — de-identified — we will provide it."

"We have nothing to hide in the methodology. The number is real."

This slide does not appear in the main deck flow — it is referenced in conversation as available. If the audience asks to see the math, flip to this slide.

Total slide time target: on-demand. -->

---

<!-- _class: call -->

## SponAItech

<h1>Thank you.</h1>

<h3 style="color:#8a9ab8; margin-top:0.6em;">sponaitech.com &nbsp;·&nbsp; sathiyaraj.t@gmail.com</h3>

<!-- Speaker notes:
The closing "call" slide holds the navy background. We do not return to cream — the audience should carry the call-to-action energy out of the room, not settle back into the ordinary world.

"Thank you. We are available for questions — and for a decision."

Leave on screen. The gold "Thank you" on navy is the final image. It carries the same weight as the call to action — we are still in the "what could be" space. The presentation ends in the future, not the past.

Total slide time target: 0. Ambient. -->
