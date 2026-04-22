<!-- TEMPLATE: pecha-kucha
     CATEGORY: Creative / Timed
     USE WHEN: Pecha Kucha format — exactly 20 slides x 20 seconds = 6:40 total. Each slide visual-forward, notes ≤60 words
     SLIDE COUNT: 20
     PALETTE: Deep navy #0a0e14 / electric blue #3b9eff / mint #2dd4a0 / amber #f0a050 / text #d0d8e4
     RENDER: marp --pptx 50-pecha-kucha.md -->
---
marp: true
theme: default
paginate: false
size: 16:9
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;600&family=DM+Mono:wght@400&display=swap');
  section {
    font-family: 'DM Sans', system-ui, sans-serif;
    background: #0a0e14;
    color: #d0d8e4;
    padding: 0;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
  }
  /* Visual area — fills top 75% of slide */
  .visual {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 75%;
    z-index: 1;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  /* Caption bar — fixed bottom 25% */
  .caption {
    position: relative;
    z-index: 10;
    height: 25%;
    padding: 0 56px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    background: rgba(10,14,20,0.96);
    border-top: 1px solid #1e2a38;
  }
  .caption h2 {
    font-family: 'DM Mono', monospace;
    font-size: 0.58em;
    font-weight: 400;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #3b9eff;
    margin: 0 0 0.2em 0;
    border: none;
    padding: 0;
  }
  .caption h1 {
    font-size: 1.3em;
    font-weight: 600;
    letter-spacing: -0.2px;
    color: #d0d8e4;
    margin: 0;
    line-height: 1.2;
  }
  .caption p {
    font-size: 0.75em;
    font-weight: 300;
    color: #8899ac;
    margin: 0.2em 0 0 0;
    line-height: 1.4;
  }
  /* Timer ghost — top-right corner, very subtle */
  .timer {
    position: absolute;
    top: 14px;
    right: 20px;
    font-family: 'DM Mono', monospace;
    font-size: 0.55em;
    color: rgba(59,158,255,0.2);
    letter-spacing: 0.1em;
    z-index: 20;
  }
---

<div class="visual">
<svg width="1280" height="540" viewBox="0 0 1280 540" xmlns="http://www.w3.org/2000/svg">
  <!-- Slide 01: Network constellation — the opening image -->
  <rect width="1280" height="540" fill="#0a0e14"/>
  <circle cx="640" cy="270" r="10" fill="#3b9eff" opacity="0.95"/>
  <circle cx="640" cy="270" r="60" fill="none" stroke="#3b9eff" stroke-width="0.8" opacity="0.15"/>
  <circle cx="640" cy="270" r="120" fill="none" stroke="#3b9eff" stroke-width="0.5" opacity="0.08"/>
  <!-- Constellation nodes -->
  <circle cx="400" cy="160" r="4" fill="#3b9eff" opacity="0.6"/>
  <circle cx="880" cy="160" r="4" fill="#3b9eff" opacity="0.6"/>
  <circle cx="280" cy="340" r="3" fill="#2dd4a0" opacity="0.5"/>
  <circle cx="1000" cy="340" r="3" fill="#2dd4a0" opacity="0.5"/>
  <circle cx="520" cy="420" r="3" fill="#8899ac" opacity="0.4"/>
  <circle cx="760" cy="420" r="3" fill="#8899ac" opacity="0.4"/>
  <circle cx="200" cy="220" r="2.5" fill="#8899ac" opacity="0.3"/>
  <circle cx="1080" cy="220" r="2.5" fill="#8899ac" opacity="0.3"/>
  <!-- Lines -->
  <line x1="640" y1="270" x2="400" y2="160" stroke="#3b9eff" stroke-width="1" opacity="0.3"/>
  <line x1="640" y1="270" x2="880" y2="160" stroke="#3b9eff" stroke-width="1" opacity="0.3"/>
  <line x1="640" y1="270" x2="280" y2="340" stroke="#2dd4a0" stroke-width="0.8" opacity="0.25"/>
  <line x1="640" y1="270" x2="1000" y2="340" stroke="#2dd4a0" stroke-width="0.8" opacity="0.25"/>
  <line x1="400" y1="160" x2="200" y2="220" stroke="#8899ac" stroke-width="0.5" opacity="0.15"/>
  <line x1="880" y1="160" x2="1080" y2="220" stroke="#8899ac" stroke-width="0.5" opacity="0.15"/>
</svg>
</div>

<div class="visual" style="z-index:2; pointer-events:none;">
<span style="font-family:'DM Sans',sans-serif; font-size:0.7em; letter-spacing:0.3em; color:rgba(59,158,255,0.4); text-transform:uppercase; position:absolute; top:32px; left:56px;">Pecha Kucha 20×20</span>
</div>

<div class="caption">
  <h2>01 / 20 ◆ SponAItech</h2>
  <h1>The network that thinks.</h1>
  <p>Why we bet everything on agentic AI — and what happened next.</p>
</div>

<!-- Speaker notes [20 sec / ≤60 words]:
An agent is not a chatbot. It is software that receives a goal and figures out the path. This constellation — every node connected, every connection live — is what agentic infrastructure looks like at scale. Tonight I will tell you what it took to build it, and why we would do it again. -->

---

<div class="visual">
<svg width="1280" height="540" viewBox="0 0 1280 540" xmlns="http://www.w3.org/2000/svg">
  <!-- Slide 02: Clock face — time pressure -->
  <rect width="1280" height="540" fill="#0a0e14"/>
  <circle cx="640" cy="270" r="200" fill="#111820" stroke="#2a3848" stroke-width="2"/>
  <circle cx="640" cy="270" r="8" fill="#3b9eff"/>
  <!-- Minute hand — pointing to 9 minutes (270deg = almost full) -->
  <line x1="640" y1="270" x2="640" y2="90" stroke="#d0d8e4" stroke-width="5" stroke-linecap="round" opacity="0.9"/>
  <!-- Hour hand -->
  <line x1="640" y1="270" x2="506" y2="350" stroke="#d0d8e4" stroke-width="4" stroke-linecap="round" opacity="0.6"/>
  <!-- Clock ticks -->
  <line x1="640" y1="76" x2="640" y2="94" stroke="#3a4858" stroke-width="2"/>
  <line x1="640" y1="448" x2="640" y2="466" stroke="#3a4858" stroke-width="2"/>
  <line x1="446" y1="270" x2="464" y2="270" stroke="#3a4858" stroke-width="2"/>
  <line x1="816" y1="270" x2="834" y2="270" stroke="#3a4858" stroke-width="2"/>
  <!-- 9.2 min label -->
  <text x="640" y="315" text-anchor="middle" font-family="DM Mono, monospace" font-size="22" fill="#3b9eff" letter-spacing="2">9.2 MIN</text>
</svg>
</div>

<div class="caption">
  <h2>02 / 20 ◆ The baseline</h2>
  <h1>A claim that takes 9.2 minutes.</h1>
  <p>Per claim. 52 claims per shift. Every reviewer. Every day.</p>
</div>

<!-- Speaker notes [20 sec / ≤60 words]:
Nine minutes and twelve seconds. That is the median time to process one insurance claim at the organizations we work with. 52 claims per shift. One reviewer. Multiply that out — it is a beautiful number until you understand what it means: 80% of that time is data retrieval, not judgment. -->

---

<div class="visual">
<svg width="1280" height="540" viewBox="0 0 1280 540" xmlns="http://www.w3.org/2000/svg">
  <!-- Slide 03: Four silos — isolated rectangles -->
  <rect width="1280" height="540" fill="#0a0e14"/>
  <rect x="140" y="120" width="160" height="260" rx="8" fill="#111820" stroke="#2a3848" stroke-width="1.5"/>
  <rect x="380" y="120" width="160" height="260" rx="8" fill="#111820" stroke="#2a3848" stroke-width="1.5"/>
  <rect x="620" y="120" width="160" height="260" rx="8" fill="#111820" stroke="#2a3848" stroke-width="1.5"/>
  <rect x="860" y="120" width="160" height="260" rx="8" fill="#111820" stroke="#2a3848" stroke-width="1.5"/>
  <!-- Blank lines in each silo -->
  <rect x="168" y="160" width="104" height="8" rx="2" fill="#2a3848" opacity="0.6"/>
  <rect x="168" y="180" width="80" height="6" rx="2" fill="#2a3848" opacity="0.4"/>
  <rect x="408" y="160" width="104" height="8" rx="2" fill="#2a3848" opacity="0.6"/>
  <rect x="408" y="180" width="80" height="6" rx="2" fill="#2a3848" opacity="0.4"/>
  <rect x="648" y="160" width="104" height="8" rx="2" fill="#2a3848" opacity="0.6"/>
  <rect x="648" y="180" width="80" height="6" rx="2" fill="#2a3848" opacity="0.4"/>
  <rect x="888" y="160" width="104" height="8" rx="2" fill="#2a3848" opacity="0.6"/>
  <rect x="888" y="180" width="80" height="6" rx="2" fill="#2a3848" opacity="0.4"/>
  <!-- Labels -->
  <text x="220" y="412" text-anchor="middle" font-family="DM Mono, monospace" font-size="11" fill="#4a5a70" letter-spacing="1">CRM</text>
  <text x="460" y="412" text-anchor="middle" font-family="DM Mono, monospace" font-size="11" fill="#4a5a70" letter-spacing="1">CLAIMS</text>
  <text x="700" y="412" text-anchor="middle" font-family="DM Mono, monospace" font-size="11" fill="#4a5a70" letter-spacing="1">EHR</text>
  <text x="940" y="412" text-anchor="middle" font-family="DM Mono, monospace" font-size="11" fill="#4a5a70" letter-spacing="1">BILLING</text>
  <!-- No connections — isolation is the point -->
</svg>
</div>

<div class="caption">
  <h2>03 / 20 ◆ The architecture problem</h2>
  <h1>Four systems. Zero connections.</h1>
  <p>The human is the integration layer — and that is the bottleneck.</p>
</div>

<!-- Speaker notes [20 sec / ≤60 words]:
CRM. Claims. EHR. Billing. Four systems, each the source of truth for its domain. None connected. The reviewer opens each one manually, retrieves the data, reconciles it in her head, makes a decision. She is not doing clinical work. She is doing data plumbing. Every minute of it. -->

---

<div class="visual">
<svg width="1280" height="540" viewBox="0 0 1280 540" xmlns="http://www.w3.org/2000/svg">
  <!-- Slide 04: Stack of paper — the queue -->
  <rect width="1280" height="540" fill="#0a0e14"/>
  <!-- Stacked document layers, growing upward -->
  <rect x="340" y="400" width="600" height="10" rx="2" fill="#2a3848" opacity="0.9"/>
  <rect x="350" y="388" width="580" height="10" rx="2" fill="#2a3848" opacity="0.75"/>
  <rect x="360" y="376" width="560" height="10" rx="2" fill="#2a3848" opacity="0.62"/>
  <rect x="370" y="364" width="540" height="10" rx="2" fill="#2a3848" opacity="0.50"/>
  <rect x="380" y="352" width="520" height="10" rx="2" fill="#2a3848" opacity="0.40"/>
  <rect x="390" y="340" width="500" height="10" rx="2" fill="#1e2a38" opacity="0.32"/>
  <rect x="400" y="328" width="480" height="10" rx="2" fill="#1e2a38" opacity="0.25"/>
  <rect x="410" y="316" width="460" height="10" rx="2" fill="#1e2a38" opacity="0.18"/>
  <rect x="420" y="304" width="440" height="10" rx="2" fill="#1e2a38" opacity="0.13"/>
  <rect x="430" y="292" width="420" height="10" rx="2" fill="#1e2a38" opacity="0.09"/>
  <!-- "52 CLAIMS" label at top of stack -->
  <text x="640" y="268" text-anchor="middle" font-family="DM Mono, monospace" font-size="14" fill="#f0a050" letter-spacing="3">52 CLAIMS</text>
  <text x="640" y="290" text-anchor="middle" font-family="DM Mono, monospace" font-size="11" fill="#4a5a70" letter-spacing="2">IN QUEUE</text>
  <!-- Arrow pointing down at the stack, pressure -->
  <line x1="640" y1="180" x2="640" y2="250" stroke="#f0a050" stroke-width="2" opacity="0.6"/>
  <polygon points="632,245 648,245 640,260" fill="#f0a050" opacity="0.6"/>
</svg>
</div>

<div class="caption">
  <h2>04 / 20 ◆ The queue problem</h2>
  <h1>It grows faster than it clears.</h1>
  <p>Not a staffing problem. A workflow design problem.</p>
</div>

<!-- Speaker notes [20 sec / ≤60 words]:
The queue is permanent. Not because reviewers are slow — because claim volume outpaces human throughput by design. Adding headcount buys linear capacity in an exponential problem. The queue does not clear. It reorganizes. The answer is not more humans doing human-speed work. It is redesigning what humans do. -->

---

<div class="visual">
<svg width="1280" height="540" viewBox="0 0 1280 540" xmlns="http://www.w3.org/2000/svg">
  <!-- Slide 05: Diamond agent shape, glowing, central -->
  <rect width="1280" height="540" fill="#0a0e14"/>
  <polygon points="640,140 780,270 640,400 500,270" fill="#0d1520" stroke="#3b9eff" stroke-width="2.5"/>
  <polygon points="640,160 760,270 640,380 520,270" fill="#3b9eff" opacity="0.1"/>
  <circle cx="640" cy="270" r="90" fill="none" stroke="#3b9eff" stroke-width="0.8" opacity="0.2"/>
  <circle cx="640" cy="270" r="140" fill="none" stroke="#3b9eff" stroke-width="0.4" opacity="0.1"/>
  <!-- "AGENT" label inside diamond -->
  <text x="640" y="278" text-anchor="middle" font-family="DM Mono, monospace" font-size="16" fill="#3b9eff" letter-spacing="4">AGENT</text>
</svg>
</div>

<div class="caption">
  <h2>05 / 20 ◆ The solution</h2>
  <h1>The agent is the integration layer.</h1>
  <p>It queries everything simultaneously. It does not wait.</p>
</div>

<!-- Speaker notes [20 sec / ≤60 words]:
The agent replaces the human as the bridge between systems. Not because humans are expendable — because that bridge work is mechanical, not judgmental. The agent queries four systems in parallel, assembles context in milliseconds, applies clinical rules, outputs a decision. The human reviews, confirms, moves to the next. -->

---

<div class="visual">
<svg width="1280" height="540" viewBox="0 0 1280 540" xmlns="http://www.w3.org/2000/svg">
  <!-- Slide 06: Split timer before/after -->
  <rect width="1280" height="540" fill="#0a0e14"/>
  <!-- Left: BEFORE -->
  <text x="320" y="200" text-anchor="middle" font-family="DM Mono, monospace" font-size="12" fill="#4a5a70" letter-spacing="2">BEFORE</text>
  <text x="320" y="310" text-anchor="middle" font-family="DM Sans, sans-serif" font-size="80" fill="#8899ac" font-weight="700" letter-spacing="-4">9.2</text>
  <text x="320" y="360" text-anchor="middle" font-family="DM Mono, monospace" font-size="12" fill="#4a5a70" letter-spacing="2">MINUTES</text>
  <!-- Divider -->
  <line x1="640" y1="100" x2="640" y2="440" stroke="#1e2a38" stroke-width="1.5"/>
  <!-- Right: AFTER -->
  <text x="960" y="200" text-anchor="middle" font-family="DM Mono, monospace" font-size="12" fill="#3b9eff" letter-spacing="2">AFTER</text>
  <text x="960" y="310" text-anchor="middle" font-family="DM Sans, sans-serif" font-size="80" fill="#3b9eff" font-weight="700" letter-spacing="-4">22</text>
  <text x="960" y="360" text-anchor="middle" font-family="DM Mono, monospace" font-size="12" fill="#3b9eff" letter-spacing="2">SECONDS</text>
</svg>
</div>

<div class="caption">
  <h2>06 / 20 ◆ The result</h2>
  <h1>96% faster. Same decision. Same data.</h1>
  <p>The bottleneck was never the thinking. It was the lookup.</p>
</div>

<!-- Speaker notes [20 sec / ≤60 words]:
Nine minutes and twelve seconds. Twenty-two seconds. Not a 10% improvement. A 96% reduction. Same four systems queried. Same clinical rules applied. Same output generated. The agent eliminates sequential lookup. Parallel queries collapse the timeline. The thinking time — the actual judgment — was always just seconds. -->

---

<div class="visual">
<svg width="1280" height="540" viewBox="0 0 1280 540" xmlns="http://www.w3.org/2000/svg">
  <!-- Slide 07: $340M large number on dark -->
  <rect width="1280" height="540" fill="#0a0e14"/>
  <text x="640" y="320" text-anchor="middle" font-family="DM Sans, sans-serif" font-size="130" fill="#1e2a38" font-weight="700" letter-spacing="-8">$340M</text>
  <text x="640" y="320" text-anchor="middle" font-family="DM Sans, sans-serif" font-size="130" fill="#f0a050" font-weight="700" letter-spacing="-8" opacity="0.9">$340M</text>
</svg>
</div>

<div class="caption">
  <h2>07 / 20 ◆ The cost of inaction</h2>
  <h1>Annual leakage. Leaving. Quietly.</h1>
  <p>Secondary code errors invisible to manual review.</p>
</div>

<!-- Speaker notes [20 sec / ≤60 words]:
$340 million. Annual leakage — money paid on claims that should have been flagged, modified, or denied. Not fraud. Coding errors, modifier anomalies, secondary code inflation. Invisible in manual review because catching them requires comparing each claim to millions of historical patterns. No human does that at 52 claims per shift. -->

---

<div class="visual">
<svg width="1280" height="540" viewBox="0 0 1280 540" xmlns="http://www.w3.org/2000/svg">
  <!-- Slide 08: Pie chart — 72% concentrated in secondary codes -->
  <rect width="1280" height="540" fill="#0a0e14"/>
  <!-- Pie: 72% amber (secondary codes), 28% gray -->
  <!-- SVG arc math for 72%: 360 * 0.72 = 259.2 degrees -->
  <!-- Start at top (270 deg = -90 deg), sweep 259.2 deg clockwise -->
  <path d="M 640 270 L 640 70 A 200 200 0 1 1 290.3 388.4 Z" fill="#f0a050" opacity="0.85"/>
  <path d="M 640 270 L 290.3 388.4 A 200 200 0 0 1 640 70 Z" fill="#1e2a38" opacity="0.8"/>
  <!-- Labels -->
  <text x="700" y="240" font-family="DM Mono, monospace" font-size="22" fill="#f0a050" font-weight="500">72%</text>
  <text x="710" y="262" font-family="DM Mono, monospace" font-size="11" fill="#f0a050" opacity="0.7">Secondary codes</text>
  <text x="460" y="390" font-family="DM Mono, monospace" font-size="11" fill="#4a5a70">28% other</text>
</svg>
</div>

<div class="caption">
  <h2>08 / 20 ◆ Concentration</h2>
  <h1>72% of leakage. One cause.</h1>
  <p>Secondary code errors: $244M of the $340M total.</p>
</div>

<!-- Speaker notes [20 sec / ≤60 words]:
Leakage is not evenly distributed. 72% — $244 million — lives in one place: secondary procedure codes. This concentration is good news. It means one model, tuned to one problem, captures three-quarters of the recoverable value. We do not need to solve everything. We need to solve secondary codes. -->

---

<div class="visual">
<svg width="1280" height="540" viewBox="0 0 1280 540" xmlns="http://www.w3.org/2000/svg">
  <!-- Slide 09: 94% accuracy gauge -->
  <rect width="1280" height="540" fill="#0a0e14"/>
  <!-- Semi-circle gauge -->
  <path d="M 240 350 A 400 400 0 0 1 1040 350" fill="none" stroke="#1e2a38" stroke-width="40" stroke-linecap="round"/>
  <!-- 94% fill: 94% of 180 degrees = 169.2 degrees -->
  <path d="M 240 350 A 400 400 0 0 1 1008 302" fill="none" stroke="#2dd4a0" stroke-width="40" stroke-linecap="round"/>
  <!-- Needle -->
  <line x1="640" y1="350" x2="1008" y2="302" stroke="#ffffff" stroke-width="3" stroke-linecap="round" opacity="0.6"/>
  <circle cx="640" cy="350" r="14" fill="#2dd4a0"/>
  <!-- Percentage label -->
  <text x="640" y="230" text-anchor="middle" font-family="DM Sans, sans-serif" font-size="90" fill="#2dd4a0" font-weight="700" letter-spacing="-5">94%</text>
  <text x="640" y="270" text-anchor="middle" font-family="DM Mono, monospace" font-size="12" fill="#4a5a70" letter-spacing="3">ACCURACY</text>
</svg>
</div>

<div class="caption">
  <h2>09 / 20 ◆ The model</h2>
  <h1>94% on secondary code detection.</h1>
  <p>Measured on 48,000 pilot claims the model had never seen.</p>
</div>

<!-- Speaker notes [20 sec / ≤60 words]:
Not trained accuracy. Test accuracy. 48,000 claims the model had never encountered. 94% correct identification of secondary code anomalies. False positive rate 0.8% — minimal unnecessary review. False negative rate 5.2% — the gap we are closing. 94% on first deployment. Industry baseline: 68% for rule-based systems. -->

---

<div class="visual">
<svg width="1280" height="540" viewBox="0 0 1280 540" xmlns="http://www.w3.org/2000/svg">
  <!-- Slide 10: Explanation text block — the explainability feature -->
  <rect width="1280" height="540" fill="#0a0e14"/>
  <!-- Document card -->
  <rect x="240" y="80" width="800" height="340" rx="12" fill="#111820" stroke="#2a3848" stroke-width="1.5"/>
  <!-- Header bar -->
  <rect x="240" y="80" width="800" height="48" rx="12" fill="#1e2a38"/>
  <rect x="240" y="108" width="800" height="20" fill="#1e2a38"/>
  <text x="280" y="112" font-family="DM Mono, monospace" font-size="11" fill="#3b9eff" letter-spacing="2">DECISION EXPLANATION</text>
  <!-- Content lines (simulated text) -->
  <text x="280" y="172" font-family="DM Sans, sans-serif" font-size="13" fill="#d0d8e4">Claim flagged: secondary code 27447 appears with primary</text>
  <text x="280" y="195" font-family="DM Sans, sans-serif" font-size="13" fill="#d0d8e4">diagnosis that does not meet CMS criteria for bilateral</text>
  <text x="280" y="218" font-family="DM Sans, sans-serif" font-size="13" fill="#d0d8e4">knee replacement (effective Jan 2025 guideline update).</text>
  <line x1="280" y1="238" x2="960" y2="238" stroke="#1e2a38" stroke-width="1"/>
  <text x="280" y="266" font-family="DM Mono, monospace" font-size="11" fill="#4a5a70" letter-spacing="1">RECOMMENDED ACTION</text>
  <text x="280" y="290" font-family="DM Sans, sans-serif" font-size="13" fill="#2dd4a0">Request clinical documentation before approval.</text>
  <!-- Action buttons -->
  <rect x="280" y="330" width="120" height="32" rx="6" fill="#2dd4a0" opacity="0.9"/>
  <text x="340" y="351" text-anchor="middle" font-family="DM Sans, sans-serif" font-size="11" fill="#0a0e14" font-weight="600">CONFIRM</text>
  <rect x="420" y="330" width="120" height="32" rx="6" fill="#1e2a38" stroke="#3a4858" stroke-width="1"/>
  <text x="480" y="351" text-anchor="middle" font-family="DM Sans, sans-serif" font-size="11" fill="#8899ac">OVERRIDE</text>
</svg>
</div>

<div class="caption">
  <h2>10 / 20 ◆ Explainability</h2>
  <h1>Not a score. A reason.</h1>
  <p>Every decision includes a plain-language explanation the reviewer can read, verify, and act on.</p>
</div>

<!-- Speaker notes [20 sec / ≤60 words]:
AI black boxes fail in healthcare compliance. Every Orion decision includes a plain-language explanation: why it was flagged, which guideline applies, what action to take. The reviewer reads it in eight seconds. Agrees, or overrides with documentation. The audit trail is complete. Explainability is the architecture, not a feature. -->

---

<div class="visual">
<svg width="1280" height="540" viewBox="0 0 1280 540" xmlns="http://www.w3.org/2000/svg">
  <!-- Slide 11: 30-day calendar grid -->
  <rect width="1280" height="540" fill="#0a0e14"/>
  <!-- Calendar grid 5 cols x 6 rows -->
  <!-- Row labels -->
  <text x="260" y="130" text-anchor="middle" font-family="DM Mono, monospace" font-size="10" fill="#4a5a70">MON</text>
  <text x="380" y="130" text-anchor="middle" font-family="DM Mono, monospace" font-size="10" fill="#4a5a70">TUE</text>
  <text x="500" y="130" text-anchor="middle" font-family="DM Mono, monospace" font-size="10" fill="#4a5a70">WED</text>
  <text x="620" y="130" text-anchor="middle" font-family="DM Mono, monospace" font-size="10" fill="#4a5a70">THU</text>
  <text x="740" y="130" text-anchor="middle" font-family="DM Mono, monospace" font-size="10" fill="#4a5a70">FRI</text>
  <!-- Week 1 -->
  <rect x="220" y="140" width="80" height="52" rx="4" fill="#1e2a38" stroke="#2a3848" stroke-width="1"/>
  <text x="260" y="172" text-anchor="middle" font-family="DM Sans" font-size="18" fill="#3b9eff" font-weight="600">1</text>
  <text x="260" y="186" text-anchor="middle" font-family="DM Mono" font-size="8" fill="#3b9eff" letter-spacing="1">START</text>
  <rect x="340" y="140" width="80" height="52" rx="4" fill="#111820" stroke="#1e2a38" stroke-width="1"/>
  <text x="380" y="172" text-anchor="middle" font-family="DM Sans" font-size="18" fill="#4a5a70" font-weight="600">2</text>
  <rect x="460" y="140" width="80" height="52" rx="4" fill="#111820" stroke="#1e2a38" stroke-width="1"/>
  <text x="500" y="172" text-anchor="middle" font-family="DM Sans" font-size="18" fill="#4a5a70" font-weight="600">3</text>
  <rect x="580" y="140" width="80" height="52" rx="4" fill="#111820" stroke="#1e2a38" stroke-width="1"/>
  <text x="620" y="172" text-anchor="middle" font-family="DM Sans" font-size="18" fill="#4a5a70" font-weight="600">4</text>
  <rect x="700" y="140" width="80" height="52" rx="4" fill="#1e2a38" stroke="#2a3848" stroke-width="1"/>
  <text x="740" y="172" text-anchor="middle" font-family="DM Sans" font-size="18" fill="#8899ac" font-weight="600">5</text>
  <text x="740" y="186" text-anchor="middle" font-family="DM Mono" font-size="8" fill="#8899ac" letter-spacing="1">SETUP</text>
  <!-- Weeks 2-4 abbreviated -->
  <!-- Day 10 highlighted -->
  <rect x="340" y="204" width="80" height="52" rx="4" fill="#1e2a38" stroke="#2a3848" stroke-width="1"/>
  <text x="380" y="236" text-anchor="middle" font-family="DM Sans" font-size="18" fill="#f0a050" font-weight="600">10</text>
  <text x="380" y="250" text-anchor="middle" font-family="DM Mono" font-size="8" fill="#f0a050" letter-spacing="1">CONFIG</text>
  <!-- Other week 2 -->
  <rect x="220" y="204" width="80" height="52" rx="4" fill="#111820" stroke="#1e2a38" stroke-width="1"/>
  <text x="260" y="236" text-anchor="middle" font-family="DM Sans" font-size="18" fill="#4a5a70" font-weight="600">8</text>
  <rect x="460" y="204" width="80" height="52" rx="4" fill="#111820" stroke="#1e2a38" stroke-width="1"/>
  <text x="500" y="236" text-anchor="middle" font-family="DM Sans" font-size="18" fill="#4a5a70" font-weight="600">11</text>
  <rect x="580" y="204" width="80" height="52" rx="4" fill="#111820" stroke="#1e2a38" stroke-width="1"/>
  <text x="620" y="236" text-anchor="middle" font-family="DM Sans" font-size="18" fill="#4a5a70" font-weight="600">12</text>
  <rect x="700" y="204" width="80" height="52" rx="4" fill="#111820" stroke="#1e2a38" stroke-width="1"/>
  <text x="740" y="236" text-anchor="middle" font-family="DM Sans" font-size="18" fill="#4a5a70" font-weight="600">13</text>
  <!-- Day 30 highlighted -->
  <rect x="460" y="336" width="80" height="52" rx="4" fill="#1e2a38" stroke="#2dd4a0" stroke-width="2"/>
  <text x="500" y="368" text-anchor="middle" font-family="DM Sans" font-size="18" fill="#2dd4a0" font-weight="600">30</text>
  <text x="500" y="382" text-anchor="middle" font-family="DM Mono" font-size="8" fill="#2dd4a0" letter-spacing="1">LIVE</text>
  <!-- Other day 30 week boxes minimal -->
  <rect x="220" y="336" width="80" height="52" rx="4" fill="#111820" stroke="#1e2a38" stroke-width="1"/>
  <text x="260" y="368" text-anchor="middle" font-family="DM Sans" font-size="18" fill="#4a5a70" font-weight="600">28</text>
  <rect x="340" y="336" width="80" height="52" rx="4" fill="#111820" stroke="#1e2a38" stroke-width="1"/>
  <text x="380" y="368" text-anchor="middle" font-family="DM Sans" font-size="18" fill="#4a5a70" font-weight="600">29</text>
  <rect x="580" y="336" width="80" height="52" rx="4" fill="#111820" stroke="#1e2a38" stroke-width="1"/>
  <text x="620" y="368" text-anchor="middle" font-family="DM Sans" font-size="18" fill="#4a5a70" font-weight="600">31</text>
  <!-- Week 3 row abbreviated -->
  <rect x="220" y="270" width="80" height="52" rx="4" fill="#111820" stroke="#1e2a38" stroke-width="1"/>
  <text x="260" y="300" text-anchor="middle" font-family="DM Sans" font-size="18" fill="#4a5a70" font-weight="600">15</text>
  <rect x="340" y="270" width="80" height="52" rx="4" fill="#111820" stroke="#1e2a38" stroke-width="1"/>
  <text x="380" y="300" text-anchor="middle" font-family="DM Sans" font-size="18" fill="#4a5a70" font-weight="600">16</text>
  <rect x="460" y="270" width="80" height="52" rx="4" fill="#111820" stroke="#1e2a38" stroke-width="1"/>
  <text x="500" y="300" text-anchor="middle" font-family="DM Sans" font-size="18" fill="#4a5a70" font-weight="600">17</text>
  <rect x="580" y="270" width="80" height="52" rx="4" fill="#111820" stroke="#1e2a38" stroke-width="1"/>
  <text x="620" y="300" text-anchor="middle" font-family="DM Sans" font-size="18" fill="#4a5a70" font-weight="600">18</text>
  <rect x="700" y="270" width="80" height="52" rx="4" fill="#111820" stroke="#1e2a38" stroke-width="1"/>
  <text x="740" y="300" text-anchor="middle" font-family="DM Sans" font-size="18" fill="#4a5a70" font-weight="600">19</text>
</svg>
</div>

<div class="caption">
  <h2>11 / 20 ◆ The timeline</h2>
  <h1>Day 1 to Day 30: production.</h1>
  <p>No 18-month program. Sign Monday. Live by end of month.</p>
</div>

<!-- Speaker notes [20 sec / ≤60 words]:
Day 1: kickoff, environment provisioned. Day 10: model calibration begins using your historical data. Day 30: first live production decision. We have achieved this across all five clients. Fastest: 18 days. Longest: 32. Median: 28. Thirty days is the promise. We have never broken it. -->

---

<div class="visual">
<svg width="1280" height="540" viewBox="0 0 1280 540" xmlns="http://www.w3.org/2000/svg">
  <!-- Slide 12: Lock icon — data stays with you -->
  <rect width="1280" height="540" fill="#0a0e14"/>
  <!-- Lock body -->
  <rect x="480" y="240" width="320" height="240" rx="20" fill="#111820" stroke="#2dd4a0" stroke-width="2.5"/>
  <!-- Lock shackle -->
  <path d="M 540 240 L 540 160 A 100 100 0 0 1 740 160 L 740 240" fill="none" stroke="#2dd4a0" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Keyhole -->
  <circle cx="640" cy="340" r="28" fill="#1e2a38" stroke="#2dd4a0" stroke-width="1.5"/>
  <rect x="628" y="350" width="24" height="40" rx="4" fill="#1e2a38" stroke="#2dd4a0" stroke-width="1.5"/>
  <!-- "YOUR CLOUD" label -->
  <text x="640" y="445" text-anchor="middle" font-family="DM Mono, monospace" font-size="13" fill="#2dd4a0" letter-spacing="3">YOUR CLOUD</text>
  <text x="640" y="465" text-anchor="middle" font-family="DM Mono, monospace" font-size="11" fill="#4a5a70" letter-spacing="2">WE NEVER SEE THE DATA</text>
</svg>
</div>

<div class="caption">
  <h2>12 / 20 ◆ Security</h2>
  <h1>Your data. Your cloud. Your model.</h1>
  <p>HIPAA-ready by architecture, not by configuration.</p>
</div>

<!-- Speaker notes [20 sec / ≤60 words]:
The model trains inside your Azure or AWS tenant. SponAItech has zero access to your member data. We supply the architecture and the methodology. You supply the compute and the data. The trained model weights are yours. If we disappeared tomorrow, the system continues running. Data sovereignty is non-negotiable. -->

---

<div class="visual">
<svg width="1280" height="540" viewBox="0 0 1280 540" xmlns="http://www.w3.org/2000/svg">
  <!-- Slide 13: Fleet of agents — 47 diamonds -->
  <rect width="1280" height="540" fill="#0a0e14"/>
  <!-- 47 small diamonds in a grid pattern -->
  <!-- Row 1: 9 diamonds -->
  <polygon points="100,130 120,155 100,180 80,155" fill="#0d1520" stroke="#3b9eff" stroke-width="1.2" opacity="0.85"/>
  <polygon points="230,130 250,155 230,180 210,155" fill="#0d1520" stroke="#3b9eff" stroke-width="1.2" opacity="0.85"/>
  <polygon points="360,130 380,155 360,180 340,155" fill="#0d1520" stroke="#3b9eff" stroke-width="1.2" opacity="0.85"/>
  <polygon points="490,130 510,155 490,180 470,155" fill="#0d1520" stroke="#3b9eff" stroke-width="1.2" opacity="0.85"/>
  <polygon points="620,130 640,155 620,180 600,155" fill="#0d1520" stroke="#3b9eff" stroke-width="1.2" opacity="0.85"/>
  <polygon points="750,130 770,155 750,180 730,155" fill="#0d1520" stroke="#3b9eff" stroke-width="1.2" opacity="0.85"/>
  <polygon points="880,130 900,155 880,180 860,155" fill="#0d1520" stroke="#3b9eff" stroke-width="1.2" opacity="0.85"/>
  <polygon points="1010,130 1030,155 1010,180 990,155" fill="#0d1520" stroke="#3b9eff" stroke-width="1.2" opacity="0.85"/>
  <polygon points="1140,130 1160,155 1140,180 1120,155" fill="#0d1520" stroke="#3b9eff" stroke-width="1.2" opacity="0.85"/>
  <!-- Row 2: 9 diamonds -->
  <polygon points="100,230 120,255 100,280 80,255" fill="#0d1520" stroke="#2dd4a0" stroke-width="1.2" opacity="0.75"/>
  <polygon points="230,230 250,255 230,280 210,255" fill="#0d1520" stroke="#2dd4a0" stroke-width="1.2" opacity="0.75"/>
  <polygon points="360,230 380,255 360,280 340,255" fill="#0d1520" stroke="#2dd4a0" stroke-width="1.2" opacity="0.75"/>
  <polygon points="490,230 510,255 490,280 470,255" fill="#0d1520" stroke="#2dd4a0" stroke-width="1.2" opacity="0.75"/>
  <polygon points="620,230 640,255 620,280 600,255" fill="#0d1520" stroke="#2dd4a0" stroke-width="1.2" opacity="0.75"/>
  <polygon points="750,230 770,255 750,280 730,255" fill="#0d1520" stroke="#2dd4a0" stroke-width="1.2" opacity="0.75"/>
  <polygon points="880,230 900,255 880,280 860,255" fill="#0d1520" stroke="#2dd4a0" stroke-width="1.2" opacity="0.75"/>
  <polygon points="1010,230 1030,255 1010,280 990,255" fill="#0d1520" stroke="#2dd4a0" stroke-width="1.2" opacity="0.75"/>
  <polygon points="1140,230 1160,255 1140,280 1120,255" fill="#0d1520" stroke="#2dd4a0" stroke-width="1.2" opacity="0.75"/>
  <!-- Row 3: 9 diamonds -->
  <polygon points="100,330 120,355 100,380 80,355" fill="#0d1520" stroke="#8899ac" stroke-width="1" opacity="0.55"/>
  <polygon points="230,330 250,355 230,380 210,355" fill="#0d1520" stroke="#8899ac" stroke-width="1" opacity="0.55"/>
  <polygon points="360,330 380,355 360,380 340,355" fill="#0d1520" stroke="#8899ac" stroke-width="1" opacity="0.55"/>
  <polygon points="490,330 510,355 490,380 470,355" fill="#0d1520" stroke="#8899ac" stroke-width="1" opacity="0.55"/>
  <polygon points="620,330 640,355 620,380 600,355" fill="#0d1520" stroke="#8899ac" stroke-width="1" opacity="0.55"/>
  <polygon points="750,330 770,355 750,380 730,355" fill="#0d1520" stroke="#8899ac" stroke-width="1" opacity="0.55"/>
  <polygon points="880,330 900,355 880,380 860,355" fill="#0d1520" stroke="#8899ac" stroke-width="1" opacity="0.55"/>
  <polygon points="1010,330 1030,355 1010,380 990,355" fill="#0d1520" stroke="#8899ac" stroke-width="1" opacity="0.55"/>
  <polygon points="1140,330 1160,355 1140,380 1120,355" fill="#0d1520" stroke="#8899ac" stroke-width="1" opacity="0.55"/>
  <!-- Row 4: 9 diamonds -->
  <polygon points="100,430 120,455 100,480 80,455" fill="#0d1520" stroke="#4a5a70" stroke-width="0.8" opacity="0.4"/>
  <polygon points="230,430 250,455 230,480 210,455" fill="#0d1520" stroke="#4a5a70" stroke-width="0.8" opacity="0.4"/>
  <polygon points="360,430 380,455 360,480 340,455" fill="#0d1520" stroke="#4a5a70" stroke-width="0.8" opacity="0.4"/>
  <polygon points="490,430 510,455 490,480 470,455" fill="#0d1520" stroke="#4a5a70" stroke-width="0.8" opacity="0.4"/>
  <polygon points="620,430 640,455 620,480 600,455" fill="#0d1520" stroke="#4a5a70" stroke-width="0.8" opacity="0.4"/>
  <!-- Label -->
  <text x="640" y="90" text-anchor="middle" font-family="DM Mono, monospace" font-size="13" fill="#3b9eff" letter-spacing="4">47 AGENTS</text>
</svg>
</div>

<div class="caption">
  <h2>13 / 20 ◆ Scale</h2>
  <h1>47 in production. Right now.</h1>
  <p>Blue: claims. Green: intake. Gray: newer deployments, still calibrating.</p>
</div>

<!-- Speaker notes [20 sec / ≤60 words]:
This is not a pipeline. This is the current state. 47 agents deployed across five enterprise clients, processing decisions simultaneously as we speak. Blue agents: claims review. Green: member intake. Gray: newer deployments still in calibration. Every row is a new deployment cohort. The fleet compounds each quarter. -->

---

<div class="visual">
<svg width="1280" height="540" viewBox="0 0 1280 540" xmlns="http://www.w3.org/2000/svg">
  <!-- Slide 14: ROI visual — tiny cost bar vs giant return bar -->
  <rect width="1280" height="540" fill="#0a0e14"/>
  <!-- Cost bar - tiny, left -->
  <rect x="180" y="200" width="60" height="280" rx="4" fill="#f0a050" opacity="0.8"/>
  <text x="210" y="185" text-anchor="middle" font-family="DM Mono, monospace" font-size="11" fill="#f0a050" letter-spacing="1">$840K</text>
  <text x="210" y="500" text-anchor="middle" font-family="DM Mono, monospace" font-size="10" fill="#4a5a70">COST</text>
  <!-- Return bar - massive, right -->
  <rect x="400" y="80" width="700" height="400" rx="4" fill="#2dd4a0" opacity="0.8"/>
  <text x="750" y="65" text-anchor="middle" font-family="DM Mono, monospace" font-size="11" fill="#2dd4a0" letter-spacing="2">$230M RECOVERED</text>
  <text x="750" y="300" text-anchor="middle" font-family="DM Sans, sans-serif" font-size="70" fill="rgba(0,0,0,0.4)" font-weight="700">273x</text>
  <text x="750" y="500" text-anchor="middle" font-family="DM Mono, monospace" font-size="10" fill="#4a5a70">YEAR 1 RECOVERY</text>
</svg>
</div>

<div class="caption">
  <h2>14 / 20 ◆ Return</h2>
  <h1>273x year-one return on implementation.</h1>
  <p>$840K invested. $230M recovered. Conservative model.</p>
</div>

<!-- Speaker notes [20 sec / ≤60 words]:
$840,000 implementation cost. $230 million year-one recovery. 273 times the investment. The bars are proportionally accurate — I did not scale them for drama. The real numbers produce this visual. That is what a 273x return looks like. It does not fit on a normal axis. -->

---

<div class="visual">
<svg width="1280" height="540" viewBox="0 0 1280 540" xmlns="http://www.w3.org/2000/svg">
  <!-- Slide 15: Compounding curve — capacity over time -->
  <rect width="1280" height="540" fill="#0a0e14"/>
  <line x1="120" y1="460" x2="1160" y2="460" stroke="#1e2a38" stroke-width="1.5"/>
  <line x1="120" y1="100" x2="120" y2="460" stroke="#1e2a38" stroke-width="1.5"/>
  <!-- Flat headcount line -->
  <line x1="120" y1="340" x2="1160" y2="330" stroke="#2a3848" stroke-width="2" stroke-dasharray="8,5"/>
  <!-- Rising capacity curve -->
  <polyline points="120,340 260,328 400,308 520,278 640,238 760,192 880,152 1000,122 1120,100" fill="none" stroke="#3b9eff" stroke-width="3"/>
  <!-- Shaded area -->
  <polygon points="120,340 260,328 400,308 520,278 640,238 760,192 880,152 1000,122 1120,100 1120,330 1000,330 880,330 760,330 640,330 520,330 400,330 260,330 120,340" fill="#3b9eff" opacity="0.06"/>
  <!-- Key data points -->
  <circle cx="400" cy="308" r="5" fill="#3b9eff" opacity="0.8"/>
  <circle cx="640" cy="238" r="5" fill="#3b9eff" opacity="0.8"/>
  <circle cx="880" cy="152" r="6" fill="#2dd4a0" opacity="0.9"/>
  <circle cx="1120" cy="100" r="7" fill="#2dd4a0"/>
  <!-- Labels -->
  <text x="280" y="450" text-anchor="middle" font-family="DM Mono, monospace" font-size="9" fill="#4a5a70">Q1</text>
  <text x="520" y="450" text-anchor="middle" font-family="DM Mono, monospace" font-size="9" fill="#4a5a70">Q2</text>
  <text x="760" y="450" text-anchor="middle" font-family="DM Mono, monospace" font-size="9" fill="#4a5a70">Q3</text>
  <text x="1000" y="450" text-anchor="middle" font-family="DM Mono, monospace" font-size="9" fill="#4a5a70">Q4</text>
  <text x="900" y="145" font-family="DM Mono, monospace" font-size="10" fill="#3b9eff">CAPACITY</text>
  <text x="900" y="322" font-family="DM Mono, monospace" font-size="10" fill="#4a5a70">HEADCOUNT</text>
</svg>
</div>

<div class="caption">
  <h2>15 / 20 ◆ The compound effect</h2>
  <h1>Capacity grows. Headcount flat.</h1>
  <p>The gap between the lines is the value of the deployment.</p>
</div>

<!-- Speaker notes [20 sec / ≤60 words]:
Capacity (blue curve) grows. Headcount (gray dash) stays flat. The shaded area between them — that is the value created by the deployment. By Q4, capacity is at 2.4x the Q1 baseline on identical headcount. The compound effect: each new agent benefits from infrastructure previous agents established. Faster, cheaper, every cohort. -->

---

<div class="visual">
<svg width="1280" height="540" viewBox="0 0 1280 540" xmlns="http://www.w3.org/2000/svg">
  <!-- Slide 16: Three phases — horizontal lanes -->
  <rect width="1280" height="540" fill="#0a0e14"/>
  <!-- Phase 1 -->
  <rect x="80" y="120" width="320" height="80" rx="8" fill="#111820" stroke="#3b9eff" stroke-width="1.5"/>
  <text x="240" y="152" text-anchor="middle" font-family="DM Mono, monospace" font-size="12" fill="#3b9eff" letter-spacing="2">PHASE 1 — 8 WEEKS</text>
  <text x="240" y="176" text-anchor="middle" font-family="DM Sans, sans-serif" font-size="13" fill="#8899ac">Model Calibration</text>
  <!-- Arrow 1→2 -->
  <line x1="400" y1="160" x2="480" y2="160" stroke="#2a3848" stroke-width="2"/>
  <polygon points="476,154 492,160 476,166" fill="#2a3848"/>
  <!-- Phase 2 -->
  <rect x="480" y="120" width="320" height="80" rx="8" fill="#111820" stroke="#f0a050" stroke-width="1.5"/>
  <text x="640" y="152" text-anchor="middle" font-family="DM Mono, monospace" font-size="12" fill="#f0a050" letter-spacing="2">PHASE 2 — 12 WEEKS</text>
  <text x="640" y="176" text-anchor="middle" font-family="DM Sans, sans-serif" font-size="13" fill="#8899ac">Shadow Deployment</text>
  <!-- Arrow 2→3 -->
  <line x1="800" y1="160" x2="880" y2="160" stroke="#2a3848" stroke-width="2"/>
  <polygon points="876,154 892,160 876,166" fill="#2a3848"/>
  <!-- Phase 3 -->
  <rect x="880" y="120" width="320" height="80" rx="8" fill="#111820" stroke="#2dd4a0" stroke-width="1.5"/>
  <text x="1040" y="152" text-anchor="middle" font-family="DM Mono, monospace" font-size="12" fill="#2dd4a0" letter-spacing="2">PHASE 3 — ONGOING</text>
  <text x="1040" y="176" text-anchor="middle" font-family="DM Sans, sans-serif" font-size="13" fill="#8899ac">Production + Iteration</text>
  <!-- Bottom detail -->
  <line x1="80" y1="300" x2="1200" y2="300" stroke="#1e2a38" stroke-width="1"/>
  <text x="240" y="340" text-anchor="middle" font-family="DM Mono, monospace" font-size="10" fill="#4a5a70">$0 live cost</text>
  <text x="640" y="340" text-anchor="middle" font-family="DM Mono, monospace" font-size="10" fill="#f0a050">Model learns your data</text>
  <text x="1040" y="340" text-anchor="middle" font-family="DM Mono, monospace" font-size="10" fill="#2dd4a0">ROI clock starts</text>
  <!-- Guarantee badge -->
  <rect x="400" y="390" width="480" height="60" rx="8" fill="#0d1a12" stroke="#2dd4a0" stroke-width="1"/>
  <text x="640" y="420" text-anchor="middle" font-family="DM Mono, monospace" font-size="11" fill="#2dd4a0" letter-spacing="2">GUARANTEE</text>
  <text x="640" y="440" text-anchor="middle" font-family="DM Sans, sans-serif" font-size="11" fill="#8899ac">Miss ROI projection → extend at no cost</text>
</svg>
</div>

<div class="caption">
  <h2>16 / 20 ◆ The engagement</h2>
  <h1>Three phases. One guarantee.</h1>
  <p>Miss the ROI projection — we extend at no cost until you hit it.</p>
</div>

<!-- Speaker notes [20 sec / ≤60 words]:
Phase 1: calibrate the model on your data. 8 weeks. Phase 2: shadow deployment — AI runs parallel, we measure concordance, we build trust. 12 weeks. Phase 3: production. ROI clock starts. If we miss the projection — and we have not — we extend until we hit it. In writing. -->

---

<div class="visual">
<svg width="1280" height="540" viewBox="0 0 1280 540" xmlns="http://www.w3.org/2000/svg">
  <!-- Slide 17: Daily cost of waiting — countdown/dollar burn -->
  <rect width="1280" height="540" fill="#0a0e14"/>
  <!-- Burning dollar visual — large $ with amber glow -->
  <text x="640" y="320" text-anchor="middle" font-family="DM Sans, sans-serif" font-size="160" fill="#1e2a10" font-weight="700">$</text>
  <text x="640" y="320" text-anchor="middle" font-family="DM Sans, sans-serif" font-size="160" fill="#f0a050" font-weight="700" opacity="0.85">$</text>
  <!-- Glow ring -->
  <circle cx="640" cy="260" r="120" fill="none" stroke="#f0a050" stroke-width="1" opacity="0.12"/>
  <!-- Per-day label -->
  <text x="640" y="420" text-anchor="middle" font-family="DM Mono, monospace" font-size="18" fill="#f0a050" letter-spacing="3">$940,000 / DAY</text>
  <text x="640" y="450" text-anchor="middle" font-family="DM Mono, monospace" font-size="12" fill="#4a5a70" letter-spacing="2">COST OF INACTION</text>
</svg>
</div>

<div class="caption">
  <h2>17 / 20 ◆ The urgency</h2>
  <h1>Every day of delay costs $940,000.</h1>
  <p>$340M annual leakage ÷ 365 days. Unrecovered. Every day.</p>
</div>

<!-- Speaker notes [20 sec / ≤60 words]:
$340 million annual leakage divided by 365 days is $931,507 per day, rounded to $940,000. That is the daily cost of the status quo. Every day between now and a signed contract is real money — not projected money, not model money. Real leakage, leaving today, recoverable tomorrow. -->

---

<div class="visual">
<svg width="1280" height="540" viewBox="0 0 1280 540" xmlns="http://www.w3.org/2000/svg">
  <!-- Slide 18: Horizon line — looking forward -->
  <rect width="1280" height="540" fill="#0a0e14"/>
  <defs>
    <linearGradient id="pk-horizon" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e14"/>
      <stop offset="55%" stop-color="#0a0e14"/>
      <stop offset="100%" stop-color="#0d1828"/>
    </linearGradient>
    <linearGradient id="pk-glow" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#3b9eff" stop-opacity="0"/>
      <stop offset="50%" stop-color="#3b9eff" stop-opacity="0.14"/>
      <stop offset="100%" stop-color="#3b9eff" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect width="1280" height="540" fill="url(#pk-horizon)"/>
  <line x1="0" y1="300" x2="1280" y2="300" stroke="#3b9eff" stroke-width="1" opacity="0.4"/>
  <rect x="0" y="230" width="1280" height="140" fill="url(#pk-glow)"/>
  <line x1="640" y1="300" x2="0" y2="540" stroke="#1e2a38" stroke-width="1.2" opacity="0.4"/>
  <line x1="640" y1="300" x2="1280" y2="540" stroke="#1e2a38" stroke-width="1.2" opacity="0.4"/>
  <circle cx="640" cy="300" r="6" fill="#3b9eff" opacity="1"/>
  <circle cx="640" cy="300" r="30" fill="none" stroke="#3b9eff" stroke-width="0.8" opacity="0.2"/>
  <!-- 2027 label -->
  <text x="640" y="200" text-anchor="middle" font-family="DM Mono, monospace" font-size="14" fill="#3b9eff" letter-spacing="4" opacity="0.7">2027</text>
  <text x="640" y="225" text-anchor="middle" font-family="DM Sans, sans-serif" font-size="13" fill="#4a5a70">Agents as infrastructure</text>
</svg>
</div>

<div class="caption">
  <h2>18 / 20 ◆ The horizon</h2>
  <h1>2027: agents are infrastructure.</h1>
  <p>The same way cloud became default — not optional.</p>
</div>

<!-- Speaker notes [20 sec / ≤60 words]:
By 2027, organizations that deployed agentic infrastructure in 2025 will have three years of production learning that late movers cannot buy. The horizon is not distant. Two years. The organizations at the vanishing point today will define what healthcare operations looks like on the other side. -->

---

<div class="visual">
<svg width="1280" height="540" viewBox="0 0 1280 540" xmlns="http://www.w3.org/2000/svg">
  <!-- Slide 19: Single node — begin -->
  <rect width="1280" height="540" fill="#0a0e14"/>
  <circle cx="640" cy="270" r="120" fill="none" stroke="#3b9eff" stroke-width="0.5" opacity="0.08"/>
  <circle cx="640" cy="270" r="60" fill="none" stroke="#3b9eff" stroke-width="0.8" opacity="0.14"/>
  <circle cx="640" cy="270" r="12" fill="#3b9eff" opacity="1"/>
  <circle cx="640" cy="270" r="28" fill="#3b9eff" opacity="0.15"/>
  <!-- "ONE NODE" label below -->
  <text x="640" y="360" text-anchor="middle" font-family="DM Mono, monospace" font-size="13" fill="#3b9eff" letter-spacing="4" opacity="0.7">ONE NODE</text>
  <text x="640" y="382" text-anchor="middle" font-family="DM Mono, monospace" font-size="11" fill="#4a5a70" letter-spacing="3">ONE WORKFLOW</text>
  <text x="640" y="404" text-anchor="middle" font-family="DM Mono, monospace" font-size="11" fill="#4a5a70" letter-spacing="3">ONE AGENT</text>
</svg>
</div>

<div class="caption">
  <h2>19 / 20 ◆ The ask</h2>
  <h1>Start with one node.</h1>
  <p>One workflow. One agent. 30 days. Then expand.</p>
</div>

<!-- Speaker notes [20 sec / ≤60 words]:
We are not asking for a transformation program. We are asking for one workflow. The highest-friction workflow in your organization — the one a reviewer mentions when you ask what they wish could be automated. Start there. One agent. 30 days. Prove the pattern. Then expand. -->

---

<div class="visual">
<svg width="1280" height="540" viewBox="0 0 1280 540" xmlns="http://www.w3.org/2000/svg">
  <!-- Slide 20: The network again — full circle closing -->
  <rect width="1280" height="540" fill="#0a0e14"/>
  <circle cx="640" cy="270" r="10" fill="#3b9eff" opacity="0.95"/>
  <circle cx="640" cy="270" r="65" fill="none" stroke="#3b9eff" stroke-width="1" opacity="0.18"/>
  <circle cx="640" cy="270" r="130" fill="none" stroke="#3b9eff" stroke-width="0.5" opacity="0.1"/>
  <circle cx="400" cy="160" r="5" fill="#3b9eff" opacity="0.7"/>
  <circle cx="880" cy="160" r="5" fill="#3b9eff" opacity="0.7"/>
  <circle cx="280" cy="340" r="4" fill="#2dd4a0" opacity="0.6"/>
  <circle cx="1000" cy="340" r="4" fill="#2dd4a0" opacity="0.6"/>
  <circle cx="520" cy="420" r="3.5" fill="#8899ac" opacity="0.5"/>
  <circle cx="760" cy="420" r="3.5" fill="#8899ac" opacity="0.5"/>
  <circle cx="200" cy="220" r="3" fill="#8899ac" opacity="0.4"/>
  <circle cx="1080" cy="220" r="3" fill="#8899ac" opacity="0.4"/>
  <line x1="640" y1="270" x2="400" y2="160" stroke="#3b9eff" stroke-width="1.2" opacity="0.35"/>
  <line x1="640" y1="270" x2="880" y2="160" stroke="#3b9eff" stroke-width="1.2" opacity="0.35"/>
  <line x1="640" y1="270" x2="280" y2="340" stroke="#2dd4a0" stroke-width="1" opacity="0.3"/>
  <line x1="640" y1="270" x2="1000" y2="340" stroke="#2dd4a0" stroke-width="1" opacity="0.3"/>
  <line x1="400" y1="160" x2="200" y2="220" stroke="#8899ac" stroke-width="0.6" opacity="0.18"/>
  <line x1="880" y1="160" x2="1080" y2="220" stroke="#8899ac" stroke-width="0.6" opacity="0.18"/>
  <!-- sponaitech.com subtle -->
  <text x="640" y="78" text-anchor="middle" font-family="DM Mono, monospace" font-size="11" fill="rgba(59,158,255,0.3)" letter-spacing="4">SPONAITECH.COM</text>
</svg>
</div>

<div class="caption">
  <h2>20 / 20 ◆ SponAItech</h2>
  <h1>The network is ready. Are you?</h1>
  <p>sponaitech.com &nbsp;·&nbsp; sathiyaraj.t@gmail.com</p>
</div>

<!-- Speaker notes [20 sec / ≤60 words]:
We opened with a network. We close with the same network — but now you know what every node represents. Every agent. Every workflow. Every recovered dollar. The network is ready. The framework is proven. The only question left is whether you are ready to add your node. Thank you. -->
