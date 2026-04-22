<!-- TEMPLATE: google-slides
     CATEGORY: Creative / Modern
     USE WHEN: modern product-demo feel — white bg, colorful category strips, friendly and approachable
     SLIDE COUNT: 10
     PALETTE: White #fff / category strip colors (blue #4285f4, red #ea4335, yellow #fbbc04, green #34a853) / text #202124
     RENDER: marp --pptx 47-google-slides.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&display=swap');
  section {
    font-family: 'DM Sans', 'Google Sans', system-ui, sans-serif;
    background: #ffffff;
    color: #202124;
    padding: 0;
    display: flex;
    flex-direction: column;
  }
  /* Category strip at top */
  .strip {
    width: 100%;
    height: 8px;
    flex-shrink: 0;
  }
  .strip-blue { background: #4285f4; }
  .strip-red { background: #ea4335; }
  .strip-yellow { background: #fbbc04; }
  .strip-green { background: #34a853; }
  .strip-multi {
    background: linear-gradient(90deg, #4285f4 25%, #ea4335 25% 50%, #fbbc04 50% 75%, #34a853 75%);
  }
  /* Slide body */
  .body {
    flex: 1;
    padding: 40px 72px 40px 72px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  h1 {
    font-size: 2.5em;
    font-weight: 600;
    letter-spacing: -0.5px;
    line-height: 1.15;
    color: #202124;
    margin: 0 0 0.2em 0;
  }
  h2 {
    font-size: 0.72em;
    font-weight: 500;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #5f6368;
    margin: 0 0 0.6em 0;
    border: none;
    padding: 0;
  }
  h3 {
    font-size: 1.2em;
    font-weight: 400;
    color: #3c4043;
    margin: 0.4em 0 0 0;
    line-height: 1.4;
  }
  p {
    font-size: 0.88em;
    font-weight: 300;
    color: #5f6368;
    line-height: 1.65;
    margin: 0.5em 0 0 0;
    max-width: 640px;
  }
  strong { font-weight: 600; color: #202124; }
  /* Feature card grid */
  .card-row {
    display: flex;
    gap: 20px;
    margin-top: 1.4em;
  }
  .card {
    flex: 1;
    background: #f8f9fa;
    border-radius: 12px;
    padding: 1.2em 1.4em;
    border: 1px solid #e8eaed;
  }
  .card-icon {
    width: 36px;
    height: 36px;
    border-radius: 8px;
    margin-bottom: 0.6em;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.1em;
    color: white;
    font-weight: 600;
  }
  .card-icon.blue { background: #4285f4; }
  .card-icon.red { background: #ea4335; }
  .card-icon.yellow { background: #fbbc04; color: #202124; }
  .card-icon.green { background: #34a853; }
  .card h4 {
    font-size: 0.9em;
    font-weight: 600;
    color: #202124;
    margin: 0 0 0.3em 0;
  }
  .card p {
    font-size: 0.8em;
    margin: 0;
    max-width: none;
  }
  /* Stat callout */
  .stat-row {
    display: flex;
    gap: 2em;
    margin-top: 1.4em;
  }
  .stat {
    display: flex;
    flex-direction: column;
  }
  .stat-num {
    font-size: 3em;
    font-weight: 700;
    letter-spacing: -2px;
    line-height: 1;
    color: #4285f4;
  }
  .stat-num.red { color: #ea4335; }
  .stat-num.green { color: #34a853; }
  .stat-num.yellow { color: #fbbc04; }
  .stat-desc {
    font-size: 0.82em;
    color: #5f6368;
    margin-top: 0.2em;
  }
  /* Cover specifics */
  section.cover .body {
    justify-content: flex-start;
    padding-top: 56px;
  }
  section.cover h1 {
    font-size: 3.2em;
    max-width: 700px;
  }
  /* Illustration area */
  .illus {
    position: absolute;
    right: 72px;
    top: 50%;
    transform: translateY(-50%);
  }
  footer {
    font-size: 0.58em;
    letter-spacing: 0.1em;
    color: #bdc1c6;
    position: absolute;
    bottom: 14px;
    right: 72px;
  }
---

<!-- _class: cover -->

<div class="strip strip-multi"></div>
<div class="body">
  <h2>SponAItech ◆ Product Overview</h2>
  <h1>Agentic AI for Healthcare Operations</h1>
  <p>From claims processing to member engagement — AI that works alongside your team, not against it.</p>

  <svg width="340" height="200" viewBox="0 0 340 200" style="margin-top:1.6em;" xmlns="http://www.w3.org/2000/svg">
    <!-- Friendly illustration: abstract workflow with colored dots and lines -->
    <circle cx="40" cy="100" r="28" fill="#e8f0fe" stroke="#4285f4" stroke-width="2"/>
    <text x="40" y="106" text-anchor="middle" font-family="DM Sans" font-size="12" fill="#4285f4" font-weight="600">IN</text>
    <line x1="68" y1="100" x2="120" y2="100" stroke="#e8eaed" stroke-width="2"/>
    <rect x="120" y="72" width="100" height="56" rx="10" fill="#fce8e6" stroke="#ea4335" stroke-width="2"/>
    <text x="170" y="103" text-anchor="middle" font-family="DM Sans" font-size="11" fill="#ea4335" font-weight="500">AGENT</text>
    <line x1="220" y1="100" x2="272" y2="100" stroke="#e8eaed" stroke-width="2"/>
    <circle cx="300" cy="100" r="28" fill="#e6f4ea" stroke="#34a853" stroke-width="2"/>
    <text x="300" y="106" text-anchor="middle" font-family="DM Sans" font-size="12" fill="#34a853" font-weight="600">OUT</text>
    <!-- Decorative dots -->
    <circle cx="170" cy="32" r="6" fill="#fbbc04" opacity="0.7"/>
    <circle cx="200" cy="168" r="6" fill="#4285f4" opacity="0.5"/>
    <circle cx="80" cy="48" r="4" fill="#34a853" opacity="0.4"/>
    <circle cx="260" cy="152" r="4" fill="#ea4335" opacity="0.4"/>
  </svg>
</div>

<!-- Speaker notes:
Open with the multi-color strip at the top — this is the signature element of this template. The four-color strip (blue/red/yellow/green) signals: we are in Google Slides territory — approachable, modern, product-focused.

"Welcome. Today we are going to walk through how SponAItech is using agentic AI to transform healthcare operations — specifically, how we are taking the most friction-heavy workflows in your organization and removing the human bottlenecks from the parts that do not need humans."

The SVG illustration shows a simple workflow: input node → agent box → output node. It is the conceptual skeleton of the entire presentation, rendered in the four brand colors. Friendly, legible, not intimidating.

Total slide time target: 20 seconds. -->

---

<div class="strip strip-blue"></div>
<div class="body">
  <h2>The challenge</h2>
  <h1>Healthcare operations run on manual workflows that were never meant to scale.</h1>
  <p>Claims intake, eligibility verification, prior authorization, member routing — each workflow was designed for a different era. AI changes the equation.</p>
</div>

<!-- Speaker notes:
Blue strip = challenge/problem framing.

"Healthcare operations are built on manual workflows that were designed for a world where software could not cross its own boundaries. Every major workflow — claims intake, eligibility checks, prior auth — requires a human to bridge between systems."

"These workflows were not badly designed. They were designed for their era. But that era ended when large language models and agentic frameworks made it possible for software to reason, connect, and act across system boundaries."

"We are at the beginning of a very fast transition."

The blue strip on this slide signals: this is the "challenge" category. The color coding is consistent throughout — blue for context/challenge, red for problems/risks, yellow for insights/numbers, green for solutions/wins.

Total slide time target: 30 seconds. -->

---

<div class="strip strip-red"></div>
<div class="body">
  <h2>The cost of the status quo</h2>
  <h1>What manual workflows cost you every day.</h1>

  <div class="stat-row">
    <div class="stat">
      <span class="stat-num red">9.2</span>
      <span class="stat-desc">minutes per claim intake</span>
    </div>
    <div class="stat">
      <span class="stat-num red">73%</span>
      <span class="stat-desc">of claims without AI review</span>
    </div>
    <div class="stat">
      <span class="stat-num red">$340M</span>
      <span class="stat-desc">annual leakage estimate</span>
    </div>
  </div>

  <p style="margin-top:1.2em;">These are not industry averages. These are metrics from health plans the size of yours.</p>
</div>

<!-- Speaker notes:
Red strip = risk/cost framing. Three red stat callouts communicate urgency without drama.

"Let me put three numbers on the screen. Nine-point-two minutes per claim intake — that is 124% above benchmark. 73% of claims processed without AI-assisted clinical review — that is your exposure surface. And $340 million in annual leakage for a plan your size — that is a calculated figure, not an estimate."

"These are the costs of the status quo. They are not unusual — they are the baseline for organizations that have not yet deployed agentic automation. What is unusual is that there is now a clear, proven path to closing each of these gaps."

Red callout numbers on white background with red top strip creates alarm without aggression. The numbers speak — the presenter adds context.

Total slide time target: 35 seconds. -->

---

<div class="strip strip-green"></div>
<div class="body">
  <h2>The solution</h2>
  <h1>Four capabilities. One platform.</h1>

  <div class="card-row">
    <div class="card">
      <div class="card-icon blue">1</div>
      <h4>Claims Intelligence</h4>
      <p>Secondary code detection at 94% accuracy. 22-second decision time.</p>
    </div>
    <div class="card">
      <div class="card-icon red">2</div>
      <h4>Intake Automation</h4>
      <p>Pre-populated member context before the agent speaks. 4.3-min target.</p>
    </div>
    <div class="card">
      <div class="card-icon yellow">3</div>
      <h4>Eligibility Verification</h4>
      <p>Real-time cross-system eligibility check. No manual lookup required.</p>
    </div>
    <div class="card">
      <div class="card-icon green">4</div>
      <h4>Prior Auth Routing</h4>
      <p>Clinical criteria matching and auto-routing. 60% reduction in cycle time.</p>
    </div>
  </div>
</div>

<!-- Speaker notes:
Green strip = solution framing. Four cards, each with a color-coded number icon.

"The platform we have built has four core capabilities."

"One: Claims Intelligence — the secondary code detector that finds $244 million in leakage."

"Two: Intake Automation — the AI co-pilot that reduces first-contact time from 9.2 to 4.3 minutes."

"Three: Eligibility Verification — real-time, cross-system, no manual lookup."

"Four: Prior Auth Routing — clinical criteria matching that routes to the right reviewer automatically."

"These four capabilities are independent — you can start with one and add the others over time. But they compound when deployed together: the data from claims intelligence improves the intake model; the eligibility verification feeds the prior auth routing."

The card layout is the Google Slides signature — rectangular cards with rounded corners, small icon, headline, short description. Friendly and scannable.

Total slide time target: 45 seconds. -->

---

<div class="strip strip-yellow"></div>
<div class="body">
  <h2>The results</h2>
  <h1>What our clients are seeing.</h1>

  <div class="stat-row">
    <div class="stat">
      <span class="stat-num">83%</span>
      <span class="stat-desc">throughput improvement</span>
    </div>
    <div class="stat">
      <span class="stat-num green">273x</span>
      <span class="stat-desc">year-one ROI</span>
    </div>
    <div class="stat">
      <span class="stat-num">30</span>
      <span class="stat-desc">days to production</span>
    </div>
  </div>

  <svg width="520" height="60" viewBox="0 0 520 60" style="margin-top:1.4em;" xmlns="http://www.w3.org/2000/svg">
    <!-- Simple horizontal timeline -->
    <line x1="20" y1="30" x2="500" y2="30" stroke="#e8eaed" stroke-width="2"/>
    <circle cx="20" cy="30" r="8" fill="#4285f4"/>
    <circle cx="180" cy="30" r="8" fill="#fbbc04"/>
    <circle cx="340" cy="30" r="8" fill="#34a853"/>
    <circle cx="500" cy="30" r="8" fill="#34a853" opacity="0.6"/>
    <text x="20" y="52" text-anchor="middle" font-family="DM Sans" font-size="10" fill="#5f6368">Day 1</text>
    <text x="180" y="52" text-anchor="middle" font-family="DM Sans" font-size="10" fill="#5f6368">Day 10</text>
    <text x="340" y="52" text-anchor="middle" font-family="DM Sans" font-size="10" fill="#5f6368">Day 30</text>
    <text x="500" y="52" text-anchor="middle" font-family="DM Sans" font-size="10" fill="#5f6368">Day 90</text>
    <text x="20" y="16" text-anchor="middle" font-family="DM Sans" font-size="9" fill="#4285f4">Start</text>
    <text x="180" y="16" text-anchor="middle" font-family="DM Sans" font-size="9" fill="#fbbc04">Config</text>
    <text x="340" y="16" text-anchor="middle" font-family="DM Sans" font-size="9" fill="#34a853">Live</text>
    <text x="500" y="16" text-anchor="middle" font-family="DM Sans" font-size="9" fill="#34a853">Iterate</text>
  </svg>
</div>

<!-- Speaker notes:
Yellow strip = insights/results framing. The yellow strip is the data reveal strip in this template.

"Let me share what we are actually seeing across our client portfolio."

"83% throughput improvement — median across five enterprise clients, measured end-to-end."

"273x year-one ROI — at current model accuracy, before any fine-tuning."

"30 days to production — average time from contract to first live agent decision."

"The timeline at the bottom shows what those 90 days look like: Day 1 kickoff, Day 10 configuration complete, Day 30 first live decision, Day 90 first iteration based on real production data."

"No 18-month implementation program. No big-bang rollout. 30 days to live. Then iterate."

The colored timeline SVG reinforces the brand color system: blue (start) → yellow (config/caution) → green (live) → green-faded (ongoing). The colors carry semantic meaning across the deck.

Total slide time target: 40 seconds. -->

---

<div class="strip strip-blue"></div>
<div class="body">
  <h2>How it works</h2>
  <h1>Three steps. No custom development.</h1>

  <div class="card-row" style="margin-top:1.6em;">
    <div class="card">
      <div class="card-icon blue">&#9312;</div>
      <h4>Connect</h4>
      <p>Point Orion at your claims system, EHR, and eligibility database. Standard connectors — no custom integration code.</p>
    </div>
    <div class="card">
      <div class="card-icon blue" style="background:#2a6dd9;">&#9313;</div>
      <h4>Calibrate</h4>
      <p>The model trains on your historical claims data. 8 weeks. No data leaves your environment.</p>
    </div>
    <div class="card">
      <div class="card-icon blue" style="background:#1a5cc8;">&#9314;</div>
      <h4>Deploy</h4>
      <p>Shadow mode first — AI runs parallel, reviewers validate. Full production when you are confident.</p>
    </div>
  </div>
</div>

<!-- Speaker notes:
"Three steps. Connect — we use standard connectors for Epic, Salesforce Health Cloud, Availity, and the major claims platforms. No custom integration code written by your team."

"Calibrate — eight weeks for the model to learn your claims patterns, your provider network's coding habits, and your specific clinical rule set. No data leaves your environment — the model trains inside your Azure or AWS tenant."

"Deploy — shadow mode first. The AI makes decisions in parallel with your reviewers. Every AI decision is compared to the human decision. When concordance is above 92%, you switch to production. Most clients hit that threshold in week 4 of shadow mode."

"Three steps. No drama. No custom development."

The three-card layout with a gradient of blue shades (lighter blue → medium blue → darker blue) creates visual progression — each card is a step, and the color gets richer as you advance.

Total slide time target: 40 seconds. -->

---

<div class="strip strip-green"></div>
<div class="body">
  <h2>Security and compliance</h2>
  <h1>HIPAA-ready from day one.</h1>

  <div class="card-row">
    <div class="card">
      <div class="card-icon green">&#10003;</div>
      <h4>Data stays with you</h4>
      <p>Models train inside your cloud environment. We never see your member data.</p>
    </div>
    <div class="card">
      <div class="card-icon green">&#10003;</div>
      <h4>Full audit trail</h4>
      <p>Every AI decision is logged with the reasoning, the data sources, and the timestamp. Audit-ready.</p>
    </div>
    <div class="card">
      <div class="card-icon green">&#10003;</div>
      <h4>Human override</h4>
      <p>Every AI decision can be overridden by a reviewer. The system never locks out human judgment.</p>
    </div>
  </div>
</div>

<!-- Speaker notes:
"Security is not an afterthought in healthcare AI — it is the precondition for everything else. Let me address the three questions your compliance team will ask."

"Data stays with you: the Orion model trains inside your Azure or AWS tenant. We use your compute, your storage, your network boundary. We never have access to your member data."

"Full audit trail: every AI decision — every single one — is logged with the reasoning, the data sources queried, the rule applied, and the timestamp. Your auditors can pull any decision from any point in time and see exactly how Orion reached it."

"Human override: no AI decision is ever final until a human confirms it. The reviewer can override any Orion recommendation with a single click, and the override is logged as training signal for the next model iteration."

Green strip = validation/confirmation. Three green checkmark cards signal: these concerns are addressed, these risks are mitigated.

Total slide time target: 40 seconds. -->

---

<div class="strip strip-yellow"></div>
<div class="body">
  <h2>The investment</h2>
  <h1>$840K for Phases 1 and 2.</h1>

  <svg width="580" height="130" viewBox="0 0 580 130" style="margin-top:1.2em;" xmlns="http://www.w3.org/2000/svg">
    <!-- Cost vs benefit bar comparison -->
    <!-- Investment bar -->
    <rect x="0" y="20" width="40" height="80" rx="4" fill="#fbbc04"/>
    <text x="20" y="116" text-anchor="middle" font-family="DM Sans" font-size="10" fill="#5f6368">Cost</text>
    <text x="20" y="14" text-anchor="middle" font-family="DM Sans" font-size="11" fill="#fbbc04" font-weight="600">$840K</text>
    <!-- Gap label -->
    <text x="310" y="65" text-anchor="middle" font-family="DM Sans" font-size="11" fill="#5f6368" font-style="italic">273x</text>
    <line x1="50" y1="60" x2="230" y2="60" stroke="#e8eaed" stroke-width="1" stroke-dasharray="4,3"/>
    <!-- Return bar -->
    <rect x="230" y="0" width="350" height="100" rx="4" fill="#34a853"/>
    <text x="405" y="116" text-anchor="middle" font-family="DM Sans" font-size="10" fill="#5f6368">Year 1 Recovery</text>
    <text x="405" y="88" text-anchor="middle" font-family="DM Sans" font-size="14" fill="white" font-weight="600">$230M</text>
  </svg>

  <p>All data from live deployments. Guarantee: if year-one ROI falls below projection, engagement extends at no cost.</p>
</div>

<!-- Speaker notes:
"The investment is $840,000 for Phases 1 and 2 — calibration and shadow deployment. Everything is included: model training, integration, change management support, reviewer training."

"The visualization makes the point I cannot make in words: the cost bar and the return bar are not on the same scale. The investment is $840,000. The year-one recovery at current model performance is $230 million."

"273 times. Same order of magnitude as the ROI on cloud infrastructure in the early 2010s."

"We stand behind this projection with a guarantee: if year-one recovery falls below what we project before contract signature, we extend the engagement at no additional cost until we achieve it."

The bar chart SVG creates a dramatic visual imbalance — the cost bar is tiny (40px wide) and the recovery bar is massive (350px wide). The proportions are accurate to the numbers and the asymmetry communicates the ROI instantly.

Total slide time target: 40 seconds. -->

---

<div class="strip strip-multi"></div>
<div class="body">
  <h2>Let's talk</h2>
  <h1>Ready to deploy your first agent?</h1>

  <div class="card-row" style="margin-top:1.6em; max-width:560px;">
    <div class="card" style="text-align:center; background:#f8f9fa;">
      <svg width="40" height="40" viewBox="0 0 40 40" style="margin-bottom:0.4em;" xmlns="http://www.w3.org/2000/svg">
        <circle cx="20" cy="20" r="20" fill="#e8f0fe"/>
        <text x="20" y="26" text-anchor="middle" font-family="DM Sans" font-size="16" fill="#4285f4">&#9990;</text>
      </svg>
      <h4>Book a 30-min call</h4>
      <p>Walk through your highest-friction workflow with our team.</p>
    </div>
    <div class="card" style="text-align:center; background:#f8f9fa;">
      <svg width="40" height="40" viewBox="0 0 40 40" style="margin-bottom:0.4em;" xmlns="http://www.w3.org/2000/svg">
        <circle cx="20" cy="20" r="20" fill="#e6f4ea"/>
        <text x="20" y="26" text-anchor="middle" font-family="DM Sans" font-size="16" fill="#34a853">&#9654;</text>
      </svg>
      <h4>See a live demo</h4>
      <p>Orion processing real (de-identified) claims in real time.</p>
    </div>
  </div>

  <p style="margin-top:1.4em;"><strong>sponaitech.com</strong> &nbsp;·&nbsp; sathiyaraj.t@gmail.com</p>
</div>

<!-- Speaker notes:
The closing slide uses the multi-color strip — the same as the opening — to bookend the presentation.

"We have two ways to take the next step."

"One: a 30-minute call with our solutions team. You bring your highest-friction workflow, we walk through how Orion would handle it, and we give you a specific ROI projection — no charge, no commitment."

"Two: a live demo. We will run Orion on de-identified claims from an organization your size, in real time. You can see the 22-second decision cycle, the explanation engine, and the flagging logic — on actual healthcare data."

"Either way, we start with your problem, not our product."

The two call-to-action cards match the Google Slides aesthetic: simple icons, clear labels, short descriptions. The multi-color closing strip signals: we have come full circle.

Total slide time target: 30 seconds, then open Q&A. -->
