<!-- TEMPLATE: data-story
     CATEGORY: Creative / Data Visualization
     USE WHEN: data-driven narrative — Cole Nussbaumer Knaflic method — one big number per slide, signal vs noise
     SLIDE COUNT: 11
     PALETTE: White #ffffff / near-black #1a1a2e / signal red #f06070 / muted gray #c8ccd6
     RENDER: marp --pptx 44-data-story.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;600;700&family=DM+Mono:wght@400;500&display=swap');
  section {
    font-family: 'DM Sans', system-ui, sans-serif;
    background: #ffffff;
    color: #1a1a2e;
    padding: 60px 80px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  h1 {
    font-size: 2.6em;
    font-weight: 700;
    letter-spacing: -1px;
    line-height: 1.1;
    color: #1a1a2e;
    margin: 0 0 0.3em 0;
  }
  h2 {
    font-family: 'DM Mono', monospace;
    font-size: 0.7em;
    font-weight: 400;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #9098a8;
    margin: 0 0 0.6em 0;
    border: none;
    padding: 0;
  }
  h3 {
    font-size: 1.2em;
    font-weight: 400;
    color: #4a5568;
    margin: 0.3em 0 0 0;
    line-height: 1.4;
  }
  p {
    font-size: 0.88em;
    font-weight: 300;
    color: #6b7280;
    line-height: 1.7;
    max-width: 620px;
    margin: 0.6em 0 0 0;
  }
  /* Hero number — the dominant data point on each slide */
  .hero-number {
    font-family: 'DM Sans', sans-serif;
    font-size: 7.5em;
    font-weight: 700;
    letter-spacing: -6px;
    line-height: 1;
    color: #1a1a2e;
    margin: 0;
    display: block;
  }
  .hero-number.signal {
    color: #f06070;
  }
  .hero-number.muted {
    color: #c8ccd6;
  }
  .hero-unit {
    font-family: 'DM Mono', monospace;
    font-size: 0.9em;
    font-weight: 400;
    color: #9098a8;
    letter-spacing: 0.08em;
    vertical-align: super;
    margin-left: 0.1em;
  }
  /* Bar chart simulation using CSS */
  .bar-chart {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-top: 1.2em;
    max-width: 600px;
  }
  .bar-row {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .bar-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.68em;
    color: #9098a8;
    width: 120px;
    text-align: right;
    flex-shrink: 0;
  }
  .bar-track {
    flex: 1;
    height: 24px;
    background: #f0f2f5;
    border-radius: 3px;
    overflow: hidden;
  }
  .bar-fill {
    height: 100%;
    background: #c8ccd6;
    border-radius: 3px;
  }
  .bar-fill.signal {
    background: #f06070;
  }
  .bar-value {
    font-family: 'DM Mono', monospace;
    font-size: 0.72em;
    font-weight: 500;
    color: #1a1a2e;
    width: 52px;
    flex-shrink: 0;
  }
  /* Tension arrow — visual transition between "what is" and "what should be" */
  .tension-line {
    display: flex;
    align-items: center;
    gap: 1em;
    margin: 1.2em 0;
  }
  .tension-left {
    font-size: 1.8em;
    font-weight: 700;
    color: #c8ccd6;
  }
  .tension-arrow {
    font-size: 1.4em;
    color: #9098a8;
  }
  .tension-right {
    font-size: 1.8em;
    font-weight: 700;
    color: #f06070;
  }
  section.hook {
    background: #1a1a2e;
    color: #ffffff;
  }
  section.hook h1 { color: #ffffff; }
  section.hook h2 { color: #5a6478; }
  section.hook p { color: #8090a8; }
  section.hook .hero-number { color: #ffffff; }
  footer {
    font-family: 'DM Mono', monospace;
    font-size: 0.58em;
    letter-spacing: 0.14em;
    color: #c8ccd6;
  }
  section.hook footer { color: #3a4458; }
---

<!-- _class: hook -->

## The story of a number

<span class="hero-number">$340M</span>

<h3>in preventable claims leakage — annually — across a 500,000-member health plan.</h3>

<!-- Speaker notes:
Open with the hook number in white-on-dark. The dark opening creates contrast with every slide that follows.

"I want to start with a number: $340 million. That is our estimate of preventable claims leakage annually in a plan the size of the one we are presenting to today. Leakage — meaning money paid out on claims that should have been flagged, reviewed, or denied based on clinical guidelines and member eligibility."

"$340 million is not a projection. It is a calculation. We used published industry leakage rates (2.7% of medical spend for mid-market plans) against the client's stated annual medical spend. We will show you the methodology in the appendix."

"I am leading with this number because everything else in this deck is context for it. The technology, the process, the timeline — all of it is in service of addressing this single figure."

The dark section.hook class creates maximum contrast for the opening number. The hero-number at 7.5em fills approximately the left half of the slide — the right half breathes.

Total slide time target: 30 seconds. -->

---

## Why this happens

<span class="hero-number muted">73<span class="hero-unit">%</span></span>

<h3>of claims are processed without AI-assisted clinical review.</h3>

<p>Manual review touches the highest-volume, lowest-complexity claims. Complex edge cases — where leakage lives — move through the queue faster because reviewers are occupied with routine work.</p>

<!-- Speaker notes:
"The $340 million is not mysterious. We know exactly where it comes from."

"73% of claims in a typical mid-market health plan are processed without AI-assisted clinical review. A human reviewer looks at the claim, checks the primary code, approves it. End to end in under four minutes. Fast, but not deep."

"The problem is that claims leakage does not live in the routine cases. It lives in the 12% of claims that have secondary codes, unusual procedure combinations, or eligibility ambiguity. Those claims look routine at the surface. They pass the four-minute review. And they leave money on the table."

The muted gray hero-number on this slide signals the baseline problem state — not yet alarming, just describing the current reality. The red will come when we show the solution impact.

Total slide time target: 35 seconds. -->

---

## The pattern in the data

<h2>Where leakage concentrates</h2>

<div class="bar-chart">
  <div class="bar-row">
    <span class="bar-label">Secondary codes</span>
    <div class="bar-track"><div class="bar-fill signal" style="width:72%;"></div></div>
    <span class="bar-value signal" style="color:#f06070;">$244M</span>
  </div>
  <div class="bar-row">
    <span class="bar-label">Eligibility gaps</span>
    <div class="bar-track"><div class="bar-fill" style="width:20%;"></div></div>
    <span class="bar-value">$68M</span>
  </div>
  <div class="bar-row">
    <span class="bar-label">DRG upcoding</span>
    <div class="bar-track"><div class="bar-fill" style="width:5%;"></div></div>
    <span class="bar-value">$17M</span>
  </div>
  <div class="bar-row">
    <span class="bar-label">Duplicate claims</span>
    <div class="bar-track"><div class="bar-fill" style="width:3%;"></div></div>
    <span class="bar-value">$11M</span>
  </div>
</div>

<!-- Speaker notes:
"When we analyze where the $340 million lives, the distribution is highly concentrated. Secondary code leakage — claims where the secondary procedure code triggers a reimbursement rate higher than the clinical evidence supports — accounts for $244 million. That is 72% of total leakage from a single cause."

"This concentration is good news. It means we do not need to solve a thousand problems. We need to solve one problem well: secondary code detection."

The bar chart is simulated using CSS divs. The signal bar (secondary codes) is the only red bar. All others are gray — this is the Cole Nussbaumer Knaflic principle of preattentive attributes: use color only for the data point that matters. The audience's eye goes directly to red.

Teach this principle if presenting to a data-literate audience: "Notice I have colored only the bar that is the signal. Everything else is gray. This is intentional — your eye should go to red first."

Total slide time target: 40 seconds. -->

---

## The tension

<h2>Current reality vs addressable state</h2>

<div class="tension-line">
  <span class="tension-left">73%</span>
  <span class="tension-arrow">→</span>
  <span class="tension-right">18%</span>
</div>

<h3>of claims processed without AI review: today vs post-deployment.</h3>

<p>That is the gap we are closing. From 73% unassisted to 18% unassisted — the 18% representing complex exception cases that require pure human judgment.</p>

<!-- Speaker notes:
"Here is the tension. Today: 73% of claims unassisted. After our deployment: 18% unassisted. The 18% that remains unassisted is the irreducible core of genuinely complex cases — multi-payer coordination, experimental procedure codes, member appeals. The system flags them and routes them to senior reviewers."

"The gap between 73 and 18 is where the $244 million lives."

"I want to be honest about the 18%. We will never reach zero. AI-assisted review is not a replacement for clinical judgment on complex cases — it is a replacement for routine lookup work on routine cases. The senior reviewer who today spends 40% of their time on routine cases will spend 0% of their time on routine cases after deployment. Their entire working day will be exceptions."

The tension line is the visual anchor of this slide: two large numbers separated by an arrow. Gray to red. Before to after. The gap is literal: the visual space between the two numbers.

Total slide time target: 45 seconds. -->

---

## The evidence for 18%

<span class="hero-number signal">94<span class="hero-unit">%</span></span>

<h3>secondary code accuracy rate in our 6-month controlled pilot.</h3>

<p>Measured across 48,000 claims. False positive rate: 0.8%. False negative rate: 5.2%. Clinical review team validated 1,200 flagged claims against medical records.</p>

<!-- Speaker notes:
"We are not asking you to trust a projection. We are asking you to evaluate a pilot."

"Over six months, on a shadow cohort of 48,000 claims, our model identified secondary code issues with 94% accuracy. False positives — claims flagged that should not have been — came in at 0.8%. That means 0.8% of claims required unnecessary human review. That is acceptable friction."

"False negatives — claims that should have been flagged and were not — came in at 5.2%. That is the gap we are working to close in the next model iteration. Even at 5.2% miss rate, the deployed model would have caught $230 million of the $244 million secondary code leakage."

The signal red on the hero number is the first full red number in the deck — reserved for the positive evidence. This is color as argument: we used muted gray for the problem state and red for the opportunity. Now red marks the evidence for the solution.

Total slide time target: 45 seconds. -->

---

## What the shift looks like

<h2>Reviewer time allocation — before vs after</h2>

<div class="bar-chart" style="margin-top:1em;">
  <div class="bar-row">
    <span class="bar-label">Routine claims</span>
    <div class="bar-track"><div class="bar-fill" style="width:65%;"></div></div>
    <span class="bar-value" style="color:#9098a8;">65%</span>
  </div>
  <div class="bar-row">
    <span class="bar-label">Flagged claims</span>
    <div class="bar-track"><div class="bar-fill signal" style="width:20%;"></div></div>
    <span class="bar-value">20%</span>
  </div>
  <div class="bar-row">
    <span class="bar-label">Appeals</span>
    <div class="bar-track"><div class="bar-fill" style="width:15%;"></div></div>
    <span class="bar-value">15%</span>
  </div>
</div>

<div style="margin:1.2em 0; height:1px; background:#f0f2f5;"></div>

<div class="bar-chart">
  <div class="bar-row">
    <span class="bar-label">Routine claims</span>
    <div class="bar-track"><div class="bar-fill" style="width:5%;"></div></div>
    <span class="bar-value" style="color:#c8ccd6;">5%</span>
  </div>
  <div class="bar-row">
    <span class="bar-label">Flagged claims</span>
    <div class="bar-track"><div class="bar-fill signal" style="width:55%;"></div></div>
    <span class="bar-value signal" style="color:#f06070;">55%</span>
  </div>
  <div class="bar-row">
    <span class="bar-label">Appeals</span>
    <div class="bar-track"><div class="bar-fill" style="width:40%;"></div></div>
    <span class="bar-value">40%</span>
  </div>
</div>

<!-- Speaker notes:
Two bar charts — before and after. The signal bar (Flagged claims) shifts from 20% to 55%. This is the before/after using the same visual language, making the change immediately apparent.

"What does this mean for your reviewers? Today, a claims reviewer spends 65% of their time processing routine claims that an AI system could handle. After deployment, that drops to 5%. The time freed up goes to flagged claims — the complex cases the model escalates — and to appeals."

"Your senior reviewers will become your most effective leakage recovery resource, because they will finally have time to actually review the things worth reviewing."

The before/after in the same CSS bar chart format makes the comparison visceral without a complex chart component. The divider line between the two sections is the only separator — no labels needed because the structure is obvious.

Total slide time target: 45 seconds. -->

---

## The implication

<span class="hero-number signal">$230M</span>

<h3>recoverable leakage with current model accuracy at scale.</h3>

<p>Conservative estimate. Assumes 5.2% miss rate persists. Does not include secondary benefits: reviewer capacity reallocation, cycle time reduction, downstream appeals reduction.</p>

<!-- Speaker notes:
"The punchline. At current model accuracy — 94% on secondary codes — the recoverable leakage is $230 million annually on a plan of this size."

"I want to be conservative here. $230 million assumes the 5.2% miss rate persists. We expect the next model iteration to improve that. But even at current performance, $230 million against an implementation cost of $840,000 is a 273x return in year one."

"That is not a typo. Two hundred and seventy-three times the implementation cost, recovered in year one."

"And that is before the secondary benefits: senior reviewer capacity freed for appeals work, cycle time reduction in claim settlement, downstream reduction in appeals volume as first-pass accuracy improves."

The $230 million in signal red is the largest positive number in the deck — it answers the $340 million hook from slide one. The audience has been watching the gap close across the deck. This is the resolution.

Total slide time target: 40 seconds. -->

---

## The ask

<h2>Three-phase engagement</h2>

<div class="bar-chart" style="margin-top:1em; gap:14px;">
  <div class="bar-row">
    <span class="bar-label">Phase 1</span>
    <div class="bar-track" style="height:32px;"><div class="bar-fill" style="width:25%; height:100%;"></div></div>
    <span class="bar-value" style="font-size:0.8em; width:auto;">8 weeks — model calibration</span>
  </div>
  <div class="bar-row">
    <span class="bar-label">Phase 2</span>
    <div class="bar-track" style="height:32px;"><div class="bar-fill signal" style="width:50%; height:100%;"></div></div>
    <span class="bar-value" style="font-size:0.8em; width:auto; color:#f06070;">12 weeks — shadow deployment</span>
  </div>
  <div class="bar-row">
    <span class="bar-label">Phase 3</span>
    <div class="bar-track" style="height:32px;"><div class="bar-fill" style="width:100%; height:100%;"></div></div>
    <span class="bar-value" style="font-size:0.8em; width:auto;">Ongoing — production + iteration</span>
  </div>
</div>

<p style="margin-top:1.4em;">Total Phase 1+2 investment: <strong>$840,000.</strong> Year 1 ROI: <strong>273x.</strong></p>

<!-- Speaker notes:
"The engagement is three phases."

"Phase 1, eight weeks: we calibrate the model on your specific claims data, claim mix, and coding patterns. The model that worked in our pilot needs to learn your terminology and your provider network's quirks."

"Phase 2, twelve weeks: shadow deployment. The AI runs in parallel with your reviewers, making recommendations. We measure concordance — how often the AI and the reviewer agree — and use disagreements as training signal. No decisions are made by the AI yet."

"Phase 3: production. The AI makes the primary assessment on routine claims. Reviewers handle the flagged cases and exceptions. We iterate monthly on model performance."

"The investment for Phase 1 and 2: $840,000. The year-one recovery at current model accuracy: $230 million."

This is the penultimate data slide. It uses the bar chart to show timeline proportionality — Phase 3 fills the track completely because it is ongoing. The signal red on Phase 2 (shadow deployment) marks the critical phase — the one where the model learns your specific data.

Total slide time target: 50 seconds. -->

---

## The summary number

<span class="hero-number signal">273x</span>

<h3>year-one return on implementation cost.</h3>

<p>$230M recovered ÷ $840K invested. Conservative model. No assumptions about model improvement.</p>

<!-- Speaker notes:
"One number. 273x."

"I am going to close the data section with this number because it is the number that answers the question your CFO will ask. Not 'does this work?' — your pilot data answers that. The CFO question is: 'Is this worth the budget?'"

"273 times the implementation cost, recovered in year one, at current model accuracy, assuming we never improve the model."

"We will improve the model."

"That is the data story. Everything I have shown you from slide one to this slide is a straight line from a $340 million problem to a $230 million recovery to a 273x return. The data tells the story. I just needed to frame it."

This is the Cole Nussbaumer Knaflic "so what?" slide — the interpretive layer that tells the audience what the data means. The number is the same color (signal red) as the $230M slide — they form a visual pair.

Total slide time target: 30 seconds. -->

---

<!-- _class: hook -->

## SponAItech

<span class="hero-number" style="font-size:5em;">Ready<br>when<br>you are.</span>

<p style="color:#5a6478; margin-top:1.4em;">sponaitech.com</p>

<!-- Speaker notes:
Close back on the dark hook background — the deck is bookended in dark navy. This creates a visual frame: we opened in the dark with a provocative number, and we close in the dark with an invitation.

"The data is clear. The path is mapped. The only question left is timing."

"We are ready to begin Phase 1 calibration on 30 days notice. The model pre-training starts before your data arrives — the moment you sign, the clock starts and it is moving in your favor."

"What questions do you have?"

Leave the slide on screen. The dark background makes the room feel like a theatre — the presentation is over, the conversation begins.

Total slide time target: 20 seconds, then open Q&A. -->
