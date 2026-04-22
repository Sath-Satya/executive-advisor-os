<!-- TEMPLATE: visual-narrative
     CATEGORY: Creative / Visual-First
     USE WHEN: show-don't-tell storytelling — each slide is a visual scene with minimal caption
     SLIDE COUNT: 12
     PALETTE: Deep navy #0a0e14 / surface #111820 / electric blue #3b9eff / mint #2dd4a0 / text #d0d8e4
     RENDER: marp --pptx 45-visual-narrative.md -->
---
marp: true
theme: default
paginate: true
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
  /* Caption bar at bottom */
  .caption {
    position: relative;
    z-index: 10;
    padding: 24px 56px 36px 56px;
    background: linear-gradient(to top, rgba(10,14,20,0.98) 80%, transparent);
  }
  .caption h2 {
    font-family: 'DM Mono', monospace;
    font-size: 0.62em;
    font-weight: 400;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #3b9eff;
    margin: 0 0 0.3em 0;
    border: none;
    padding: 0;
  }
  .caption h1 {
    font-family: 'DM Sans', sans-serif;
    font-size: 1.5em;
    font-weight: 600;
    letter-spacing: -0.3px;
    color: #d0d8e4;
    margin: 0 0 0.2em 0;
    line-height: 1.2;
  }
  .caption p {
    font-size: 0.78em;
    font-weight: 300;
    color: #8899ac;
    margin: 0;
    max-width: 480px;
    line-height: 1.5;
  }
  /* Visual canvas — fills entire slide */
  .canvas {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1;
  }
  footer {
    position: absolute;
    bottom: 12px;
    right: 56px;
    font-family: 'DM Mono', monospace;
    font-size: 0.55em;
    letter-spacing: 0.14em;
    color: #2a3848;
    z-index: 20;
  }
  /* Cover: full-height caption */
  section.cover .caption {
    padding: 0 56px 64px 56px;
    background: linear-gradient(to top, rgba(10,14,20,1) 60%, transparent);
  }
  section.cover .caption h1 {
    font-size: 2.8em;
    letter-spacing: -1px;
    line-height: 1.0;
  }
---

<!-- _class: cover -->

<svg class="canvas" viewBox="0 0 1280 720" xmlns="http://www.w3.org/2000/svg">
  <!-- Starfield / node network background -->
  <rect width="1280" height="720" fill="#0a0e14"/>
  <!-- Nodes -->
  <circle cx="640" cy="260" r="6" fill="#3b9eff" opacity="0.9"/>
  <circle cx="380" cy="180" r="3.5" fill="#3b9eff" opacity="0.5"/>
  <circle cx="900" cy="200" r="3.5" fill="#3b9eff" opacity="0.5"/>
  <circle cx="200" cy="320" r="2.5" fill="#8899ac" opacity="0.4"/>
  <circle cx="1080" cy="300" r="2.5" fill="#8899ac" opacity="0.4"/>
  <circle cx="460" cy="380" r="2.5" fill="#2dd4a0" opacity="0.35"/>
  <circle cx="820" cy="360" r="2.5" fill="#2dd4a0" opacity="0.35"/>
  <circle cx="520" cy="140" r="2" fill="#8899ac" opacity="0.3"/>
  <circle cx="760" cy="130" r="2" fill="#8899ac" opacity="0.3"/>
  <!-- Connections from center -->
  <line x1="640" y1="260" x2="380" y2="180" stroke="#3b9eff" stroke-width="1" opacity="0.25"/>
  <line x1="640" y1="260" x2="900" y2="200" stroke="#3b9eff" stroke-width="1" opacity="0.25"/>
  <line x1="640" y1="260" x2="460" y2="380" stroke="#3b9eff" stroke-width="0.8" opacity="0.18"/>
  <line x1="640" y1="260" x2="820" y2="360" stroke="#3b9eff" stroke-width="0.8" opacity="0.18"/>
  <line x1="380" y1="180" x2="200" y2="320" stroke="#8899ac" stroke-width="0.6" opacity="0.12"/>
  <line x1="900" y1="200" x2="1080" y2="300" stroke="#8899ac" stroke-width="0.6" opacity="0.12"/>
  <line x1="380" y1="180" x2="520" y2="140" stroke="#8899ac" stroke-width="0.5" opacity="0.1"/>
  <line x1="900" y1="200" x2="760" y2="130" stroke="#8899ac" stroke-width="0.5" opacity="0.1"/>
  <!-- Glow ring around center -->
  <circle cx="640" cy="260" r="48" fill="none" stroke="#3b9eff" stroke-width="1" opacity="0.15"/>
  <circle cx="640" cy="260" r="90" fill="none" stroke="#3b9eff" stroke-width="0.5" opacity="0.08"/>
</svg>

<div class="caption">
  <h2>SponAItech ◆ Vision Series</h2>
  <h1>The Network<br>Thinks Now.</h1>
  <p>A visual journey through agentic AI — what it looks like when software stops waiting for instructions.</p>
</div>

<!-- Speaker notes:
The opening visual is a node network centered on a bright blue point of light. The network represents the connected, distributed nature of agentic AI — nodes are agents, lines are communication channels, the central node is the orchestrator.

"I want to open with an image rather than a slide. This is a network. Every node is a piece of software. In 2022, those nodes waited for humans to tell them what to do. Today, some of those nodes are agents — they receive a goal, and they figure out the path themselves. This presentation is about what that means."

Do not over-explain the visual. Say less than you think you need to. Let the audience look at it.

Total slide time target: 25 seconds. -->

---

<svg class="canvas" viewBox="0 0 1280 720" xmlns="http://www.w3.org/2000/svg">
  <!-- Before: isolated siloed rectangles, cold gray, disconnected -->
  <rect width="1280" height="720" fill="#0a0e14"/>
  <!-- Silo 1 -->
  <rect x="120" y="180" width="180" height="320" rx="8" fill="#111820" stroke="#2a3848" stroke-width="1.5"/>
  <rect x="150" y="220" width="120" height="12" rx="3" fill="#2a3848" opacity="0.8"/>
  <rect x="150" y="248" width="80" height="8" rx="2" fill="#1e2a38" opacity="0.6"/>
  <rect x="150" y="268" width="100" height="8" rx="2" fill="#1e2a38" opacity="0.6"/>
  <rect x="150" y="340" width="120" height="40" rx="4" fill="#1e2a38" opacity="0.4"/>
  <!-- Silo 2 -->
  <rect x="360" y="180" width="180" height="320" rx="8" fill="#111820" stroke="#2a3848" stroke-width="1.5"/>
  <rect x="390" y="220" width="120" height="12" rx="3" fill="#2a3848" opacity="0.8"/>
  <rect x="390" y="248" width="80" height="8" rx="2" fill="#1e2a38" opacity="0.6"/>
  <rect x="390" y="268" width="100" height="8" rx="2" fill="#1e2a38" opacity="0.6"/>
  <rect x="390" y="340" width="120" height="40" rx="4" fill="#1e2a38" opacity="0.4"/>
  <!-- Silo 3 -->
  <rect x="600" y="180" width="180" height="320" rx="8" fill="#111820" stroke="#2a3848" stroke-width="1.5"/>
  <rect x="630" y="220" width="120" height="12" rx="3" fill="#2a3848" opacity="0.8"/>
  <rect x="630" y="248" width="80" height="8" rx="2" fill="#1e2a38" opacity="0.6"/>
  <rect x="630" y="268" width="100" height="8" rx="2" fill="#1e2a38" opacity="0.6"/>
  <rect x="630" y="340" width="120" height="40" rx="4" fill="#1e2a38" opacity="0.4"/>
  <!-- Silo 4 -->
  <rect x="840" y="180" width="180" height="320" rx="8" fill="#111820" stroke="#2a3848" stroke-width="1.5"/>
  <rect x="870" y="220" width="120" height="12" rx="3" fill="#2a3848" opacity="0.8"/>
  <rect x="870" y="248" width="80" height="8" rx="2" fill="#1e2a38" opacity="0.6"/>
  <rect x="870" y="268" width="100" height="8" rx="2" fill="#1e2a38" opacity="0.6"/>
  <rect x="870" y="340" width="120" height="40" rx="4" fill="#1e2a38" opacity="0.4"/>
  <!-- No connections — deliberately isolated -->
  <!-- Labels -->
  <text x="210" y="540" text-anchor="middle" font-family="DM Mono, monospace" font-size="11" fill="#4a5a70" letter-spacing="1">CRM</text>
  <text x="450" y="540" text-anchor="middle" font-family="DM Mono, monospace" font-size="11" fill="#4a5a70" letter-spacing="1">CLAIMS</text>
  <text x="690" y="540" text-anchor="middle" font-family="DM Mono, monospace" font-size="11" fill="#4a5a70" letter-spacing="1">EHR</text>
  <text x="930" y="540" text-anchor="middle" font-family="DM Mono, monospace" font-size="11" fill="#4a5a70" letter-spacing="1">BILLING</text>
</svg>

<div class="caption">
  <h2>The problem — 2022</h2>
  <h1>Four systems. Zero conversation.</h1>
  <p>Each silo holds the truth. None of them talk to each other without a human in the middle.</p>
</div>

<!-- Speaker notes:
Four rectangles — CRM, Claims, EHR, Billing — isolated and unconnected. No lines between them. The visual communicates the problem before any words are spoken.

"This is a healthcare organization in 2022. Four core systems. Each one the source of truth for its domain. And between them: silence. A claims reviewer needs to pull data from all four systems to make a single coverage decision. They do it manually. Every time. For every claim."

"The human is the integration layer. That is the bottleneck."

Do not describe the slide. The visual speaks. Add only what the visual cannot show.

Total slide time target: 30 seconds. -->

---

<svg class="canvas" viewBox="0 0 1280 720" xmlns="http://www.w3.org/2000/svg">
  <!-- Human figure in the center — small, overwhelmed -->
  <rect width="1280" height="720" fill="#0a0e14"/>
  <!-- Data streams converging on center human -->
  <!-- From left -->
  <line x1="120" y1="200" x2="580" y2="360" stroke="#4a5a70" stroke-width="1" opacity="0.5" stroke-dasharray="6,4"/>
  <line x1="120" y1="400" x2="580" y2="380" stroke="#4a5a70" stroke-width="1" opacity="0.5" stroke-dasharray="6,4"/>
  <!-- From right -->
  <line x1="1160" y1="200" x2="700" y2="360" stroke="#4a5a70" stroke-width="1" opacity="0.5" stroke-dasharray="6,4"/>
  <line x1="1160" y1="400" x2="700" y2="380" stroke="#4a5a70" stroke-width="1" opacity="0.5" stroke-dasharray="6,4"/>
  <!-- From top -->
  <line x1="640" y1="80" x2="640" y2="320" stroke="#4a5a70" stroke-width="1" opacity="0.5" stroke-dasharray="6,4"/>
  <!-- Human figure — simple geometric -->
  <circle cx="640" cy="340" r="28" fill="#111820" stroke="#556677" stroke-width="1.5"/>
  <rect x="612" y="372" width="56" height="70" rx="4" fill="#111820" stroke="#556677" stroke-width="1.5"/>
  <!-- Stack of papers / queue growing around them -->
  <rect x="420" y="460" width="400" height="8" rx="2" fill="#1e2a38" opacity="0.7"/>
  <rect x="430" y="450" width="380" height="8" rx="2" fill="#1e2a38" opacity="0.55"/>
  <rect x="440" y="440" width="360" height="8" rx="2" fill="#1e2a38" opacity="0.4"/>
  <rect x="450" y="430" width="340" height="8" rx="2" fill="#1e2a38" opacity="0.28"/>
  <rect x="460" y="420" width="320" height="8" rx="2" fill="#1e2a38" opacity="0.18"/>
  <!-- Small clock -->
  <circle cx="1080" cy="160" r="40" fill="none" stroke="#3a4858" stroke-width="2"/>
  <line x1="1080" y1="160" x2="1080" y2="130" stroke="#3a4858" stroke-width="2"/>
  <line x1="1080" y1="160" x2="1104" y2="172" stroke="#f06070" stroke-width="2.5" opacity="0.8"/>
</svg>

<div class="caption">
  <h2>The burden</h2>
  <h1>One person. Every data source. Infinite queue.</h1>
  <p>The queue grows faster than any single reviewer can clear it.</p>
</div>

<!-- Speaker notes:
A human figure surrounded by data streams converging on them from all directions. A growing stack of work beneath their feet. A clock with a red minute hand in the top-right corner.

"The human is not the problem. The system is the problem. The system was designed in an era when software could not cross its own boundaries. So it put a human in every boundary as a bridge."

"The cost of that design decision is visible in every reviewer's queue. The work arrives faster than it can be cleared. The queue is permanent. The reviewer lives in triage mode."

Let the visual of the growing stack communicate the burden. The clock with the red hand communicates deadline pressure without any text.

Total slide time target: 30 seconds. -->

---

<svg class="canvas" viewBox="0 0 1280 720" xmlns="http://www.w3.org/2000/svg">
  <!-- Agent: geometric diamond form, glowing, reading from all four systems simultaneously -->
  <rect width="1280" height="720" fill="#0a0e14"/>
  <!-- Central agent diamond -->
  <polygon points="640,240 720,320 640,400 560,320" fill="#0d1520" stroke="#3b9eff" stroke-width="2" opacity="0.95"/>
  <polygon points="640,255 710,320 640,385 570,320" fill="#3b9eff" opacity="0.08"/>
  <!-- Glow -->
  <circle cx="640" cy="320" r="70" fill="none" stroke="#3b9eff" stroke-width="1" opacity="0.2"/>
  <circle cx="640" cy="320" r="100" fill="none" stroke="#3b9eff" stroke-width="0.5" opacity="0.1"/>
  <!-- System nodes -->
  <rect x="60" y="140" width="120" height="60" rx="6" fill="#111820" stroke="#2dd4a0" stroke-width="1.2"/>
  <text x="120" y="175" text-anchor="middle" font-family="DM Mono, monospace" font-size="11" fill="#2dd4a0" letter-spacing="1">CRM</text>
  <rect x="60" y="500" width="120" height="60" rx="6" fill="#111820" stroke="#2dd4a0" stroke-width="1.2"/>
  <text x="120" y="535" text-anchor="middle" font-family="DM Mono, monospace" font-size="11" fill="#2dd4a0" letter-spacing="1">CLAIMS</text>
  <rect x="1100" y="140" width="120" height="60" rx="6" fill="#111820" stroke="#2dd4a0" stroke-width="1.2"/>
  <text x="1160" y="175" text-anchor="middle" font-family="DM Mono, monospace" font-size="11" fill="#2dd4a0" letter-spacing="1">EHR</text>
  <rect x="1100" y="500" width="120" height="60" rx="6" fill="#111820" stroke="#2dd4a0" stroke-width="1.2"/>
  <text x="1160" y="535" text-anchor="middle" font-family="DM Mono, monospace" font-size="11" fill="#2dd4a0" letter-spacing="1">BILLING</text>
  <!-- Live connection lines -->
  <line x1="180" y1="170" x2="560" y2="305" stroke="#3b9eff" stroke-width="1.5" opacity="0.5"/>
  <line x1="180" y1="530" x2="560" y2="340" stroke="#3b9eff" stroke-width="1.5" opacity="0.5"/>
  <line x1="1100" y1="170" x2="720" y2="305" stroke="#3b9eff" stroke-width="1.5" opacity="0.5"/>
  <line x1="1100" y1="530" x2="720" y2="340" stroke="#3b9eff" stroke-width="1.5" opacity="0.5"/>
  <!-- Output arrow -->
  <line x1="640" y1="400" x2="640" y2="560" stroke="#2dd4a0" stroke-width="2" opacity="0.7"/>
  <polygon points="630,555 650,555 640,575" fill="#2dd4a0" opacity="0.7"/>
  <rect x="530" y="575" width="220" height="36" rx="6" fill="#0d1a12" stroke="#2dd4a0" stroke-width="1"/>
  <text x="640" y="598" text-anchor="middle" font-family="DM Mono, monospace" font-size="11" fill="#2dd4a0" letter-spacing="2">DECISION COMPLETE</text>
</svg>

<div class="caption">
  <h2>The agent</h2>
  <h1>Reads everything. Decides. Outputs.</h1>
  <p>No switching between tabs. No waiting for system responses. The agent is the integration layer.</p>
</div>

<!-- Speaker notes:
The diamond form of the agent sits at center, with live blue lines connecting to all four system nodes simultaneously. Below the agent, an output arrow and a "DECISION COMPLETE" label in mint green.

"This is what an agent looks like architecturally. Not a chatbot, not a dashboard. A decision engine that connects to every system simultaneously, reads context, applies rules, and outputs a decision."

"The diamond is not a metaphor — it is a schematic. Perception in, action out. Four connections in, one decision out. The cycle time is measured in seconds, not minutes."

"The human who was the integration layer is now the exception handler. The agent handles everything else."

Total slide time target: 35 seconds. -->

---

<svg class="canvas" viewBox="0 0 1280 720" xmlns="http://www.w3.org/2000/svg">
  <!-- Clock: before vs after, side by side -->
  <rect width="1280" height="720" fill="#0a0e14"/>
  <!-- BEFORE clock — large, on left, almost full revolution -->
  <circle cx="340" cy="320" r="160" fill="#111820" stroke="#2a3848" stroke-width="2"/>
  <circle cx="340" cy="320" r="6" fill="#4a5a70"/>
  <!-- Minute hand — almost at 9 minutes -->
  <line x1="340" y1="320" x2="340" y2="180" stroke="#8899ac" stroke-width="4" stroke-linecap="round"/>
  <!-- Hour hand -->
  <line x1="340" y1="320" x2="276" y2="360" stroke="#8899ac" stroke-width="3" stroke-linecap="round"/>
  <text x="340" y="520" text-anchor="middle" font-family="DM Mono, monospace" font-size="13" fill="#4a5a70" letter-spacing="2">9.2 MINUTES</text>
  <!-- AFTER clock — smaller, on right, quick tick -->
  <circle cx="940" cy="320" r="100" fill="#111820" stroke="#3b9eff" stroke-width="1.5" opacity="0.8"/>
  <circle cx="940" cy="320" r="5" fill="#3b9eff" opacity="0.8"/>
  <!-- Minute hand — barely moved (22 seconds) -->
  <line x1="940" y1="320" x2="940" y2="226" stroke="#3b9eff" stroke-width="3" stroke-linecap="round" opacity="0.8"/>
  <!-- Hour hand -->
  <line x1="940" y1="320" x2="904" y2="350" stroke="#3b9eff" stroke-width="2.5" stroke-linecap="round" opacity="0.8"/>
  <text x="940" y="455" text-anchor="middle" font-family="DM Mono, monospace" font-size="13" fill="#3b9eff" letter-spacing="2">22 SECONDS</text>
  <!-- VS divider -->
  <line x1="640" y1="160" x2="640" y2="480" stroke="#2a3848" stroke-width="1" stroke-dasharray="6,4"/>
  <text x="640" y="330" text-anchor="middle" font-family="DM Sans, sans-serif" font-size="18" fill="#4a5a70" font-weight="600">VS</text>
</svg>

<div class="caption">
  <h2>Speed of decision</h2>
  <h1>9.2 minutes became 22 seconds.</h1>
  <p>Same decision. Same data. Same accuracy. No human in the loop for routine claims.</p>
</div>

<!-- Speaker notes:
Two clocks side by side. The left clock is large, muted, with hands nearly completing a full revolution — representing the 9.2-minute manual process. The right clock is smaller, blue, with hands barely moved — representing the 22-second AI-assisted process.

"This slide is about time. Nine minutes and twelve seconds versus twenty-two seconds. That is the before and after for a routine coverage verification decision."

"Same decision. Same four systems queried. Same clinical rules applied. Twenty-two seconds instead of nine minutes."

"That is not a 10% improvement. It is a 96% reduction in decision time. At scale, across a claims volume of 50,000 per week, that is the difference between a three-day backlog and a same-day clearance rate."

Total slide time target: 35 seconds. -->

---

<svg class="canvas" viewBox="0 0 1280 720" xmlns="http://www.w3.org/2000/svg">
  <!-- Agents as a fleet — many small diamonds, organized, networked -->
  <rect width="1280" height="720" fill="#0a0e14"/>
  <!-- Grid of agent diamonds — 7 columns, 3 rows = 21 agents -->
  <!-- Row 1 -->
  <polygon points="160,180 185,210 160,240 135,210" fill="#0d1520" stroke="#3b9eff" stroke-width="1.2" opacity="0.8"/>
  <polygon points="280,180 305,210 280,240 255,210" fill="#0d1520" stroke="#3b9eff" stroke-width="1.2" opacity="0.8"/>
  <polygon points="400,180 425,210 400,240 375,210" fill="#0d1520" stroke="#3b9eff" stroke-width="1.2" opacity="0.8"/>
  <polygon points="520,180 545,210 520,240 495,210" fill="#0d1520" stroke="#3b9eff" stroke-width="1.2" opacity="0.8"/>
  <polygon points="640,180 665,210 640,240 615,210" fill="#0d1520" stroke="#3b9eff" stroke-width="1.2" opacity="0.8"/>
  <polygon points="760,180 785,210 760,240 735,210" fill="#0d1520" stroke="#3b9eff" stroke-width="1.2" opacity="0.8"/>
  <polygon points="880,180 905,210 880,240 855,210" fill="#0d1520" stroke="#3b9eff" stroke-width="1.2" opacity="0.8"/>
  <polygon points="1000,180 1025,210 1000,240 975,210" fill="#0d1520" stroke="#3b9eff" stroke-width="1.2" opacity="0.8"/>
  <polygon points="1120,180 1145,210 1120,240 1095,210" fill="#0d1520" stroke="#3b9eff" stroke-width="1.2" opacity="0.8"/>
  <!-- Row 2 -->
  <polygon points="160,300 185,330 160,360 135,330" fill="#0d1520" stroke="#2dd4a0" stroke-width="1.2" opacity="0.7"/>
  <polygon points="280,300 305,330 280,360 255,330" fill="#0d1520" stroke="#2dd4a0" stroke-width="1.2" opacity="0.7"/>
  <polygon points="400,300 425,330 400,360 375,330" fill="#0d1520" stroke="#2dd4a0" stroke-width="1.2" opacity="0.7"/>
  <polygon points="520,300 545,330 520,360 495,330" fill="#0d1520" stroke="#2dd4a0" stroke-width="1.2" opacity="0.7"/>
  <polygon points="640,300 665,330 640,360 615,330" fill="#0d1520" stroke="#2dd4a0" stroke-width="1.2" opacity="0.7"/>
  <polygon points="760,300 785,330 760,360 735,330" fill="#0d1520" stroke="#2dd4a0" stroke-width="1.2" opacity="0.7"/>
  <polygon points="880,300 905,330 880,360 855,330" fill="#0d1520" stroke="#2dd4a0" stroke-width="1.2" opacity="0.7"/>
  <polygon points="1000,300 1025,330 1000,360 975,330" fill="#0d1520" stroke="#2dd4a0" stroke-width="1.2" opacity="0.7"/>
  <polygon points="1120,300 1145,330 1120,360 1095,330" fill="#0d1520" stroke="#2dd4a0" stroke-width="1.2" opacity="0.7"/>
  <!-- Row 3 — fewer agents representing growth -->
  <polygon points="220,420 245,450 220,480 195,450" fill="#0d1520" stroke="#8899ac" stroke-width="1" opacity="0.5"/>
  <polygon points="400,420 425,450 400,480 375,450" fill="#0d1520" stroke="#8899ac" stroke-width="1" opacity="0.5"/>
  <polygon points="580,420 605,450 580,480 555,450" fill="#0d1520" stroke="#8899ac" stroke-width="1" opacity="0.5"/>
  <polygon points="760,420 785,450 760,480 735,450" fill="#0d1520" stroke="#8899ac" stroke-width="1" opacity="0.5"/>
  <polygon points="940,420 965,450 940,480 915,450" fill="#0d1520" stroke="#8899ac" stroke-width="1" opacity="0.5"/>
  <!-- Subtle horizontal flow lines between rows -->
  <line x1="100" y1="210" x2="1180" y2="210" stroke="#3b9eff" stroke-width="0.4" opacity="0.08"/>
  <line x1="100" y1="330" x2="1180" y2="330" stroke="#2dd4a0" stroke-width="0.4" opacity="0.08"/>
</svg>

<div class="caption">
  <h2>Scale</h2>
  <h1>47 agents. Running in parallel. Today.</h1>
  <p>Not sequentially. Not on rotation. Simultaneously — each handling its workflow, each reporting back.</p>
</div>

<!-- Speaker notes:
A grid of agent diamonds in three rows — blue row, green row, gray row (representing mature/growing/new agents). They fill the slide like a fleet.

"This is what scale looks like. Not one agent solving one problem. Forty-seven agents, deployed across five clients, each handling a specific workflow simultaneously."

"The blue agents handle claims review. The green agents handle member intake and routing. The gray agents are newer — deployed in the last six weeks — still being calibrated."

"They are all running right now. While we are in this room. Decisions are being made, outputs are being generated, queues are being cleared."

The fleet visual creates a sense of momentum and scale that a number alone cannot. The audience should feel the weight of 47 simultaneous processes.

Total slide time target: 30 seconds. -->

---

<svg class="canvas" viewBox="0 0 1280 720" xmlns="http://www.w3.org/2000/svg">
  <!-- Human and agent side by side — different scales of work -->
  <rect width="1280" height="720" fill="#0a0e14"/>
  <!-- Human figure, left, doing one task -->
  <circle cx="280" cy="260" r="36" fill="#111820" stroke="#556677" stroke-width="1.5"/>
  <rect x="248" y="300" width="64" height="80" rx="4" fill="#111820" stroke="#556677" stroke-width="1.5"/>
  <!-- Single document in human's work area -->
  <rect x="200" y="420" width="160" height="100" rx="4" fill="#1a2030" stroke="#2a3848" stroke-width="1"/>
  <rect x="218" y="440" width="100" height="8" rx="2" fill="#2a3848"/>
  <rect x="218" y="458" width="80" height="6" rx="2" fill="#2a3848" opacity="0.6"/>
  <rect x="218" y="472" width="90" height="6" rx="2" fill="#2a3848" opacity="0.6"/>
  <text x="280" y="560" text-anchor="middle" font-family="DM Mono, monospace" font-size="10" fill="#4a5a70" letter-spacing="2">1 TASK</text>
  <!-- Agent diamond, right, branching to many tasks -->
  <polygon points="940,240 980,280 940,320 900,280" fill="#0d1520" stroke="#3b9eff" stroke-width="2"/>
  <polygon points="940,255 968,280 940,305 912,280" fill="#3b9eff" opacity="0.12"/>
  <!-- Task branches -->
  <line x1="940" y1="320" x2="780" y2="430" stroke="#3b9eff" stroke-width="1" opacity="0.5"/>
  <line x1="940" y1="320" x2="880" y2="440" stroke="#3b9eff" stroke-width="1" opacity="0.5"/>
  <line x1="940" y1="320" x2="940" y2="445" stroke="#3b9eff" stroke-width="1" opacity="0.5"/>
  <line x1="940" y1="320" x2="1000" y2="440" stroke="#3b9eff" stroke-width="1" opacity="0.5"/>
  <line x1="940" y1="320" x2="1100" y2="430" stroke="#3b9eff" stroke-width="1" opacity="0.5"/>
  <!-- Task nodes -->
  <circle cx="780" cy="445" r="14" fill="#111820" stroke="#3b9eff" stroke-width="1" opacity="0.7"/>
  <circle cx="880" cy="455" r="14" fill="#111820" stroke="#3b9eff" stroke-width="1" opacity="0.7"/>
  <circle cx="940" cy="460" r="14" fill="#111820" stroke="#3b9eff" stroke-width="1" opacity="0.7"/>
  <circle cx="1000" cy="455" r="14" fill="#111820" stroke="#3b9eff" stroke-width="1" opacity="0.7"/>
  <circle cx="1100" cy="445" r="14" fill="#111820" stroke="#3b9eff" stroke-width="1" opacity="0.7"/>
  <text x="940" y="520" text-anchor="middle" font-family="DM Mono, monospace" font-size="10" fill="#3b9eff" letter-spacing="2">500 TASKS / HOUR</text>
  <!-- Divider -->
  <line x1="620" y1="180" x2="620" y2="560" stroke="#1e2a38" stroke-width="1"/>
</svg>

<div class="caption">
  <h2>Human vs agent capacity</h2>
  <h1>One task at a time. Or five hundred.</h1>
  <p>The agent does not get tired. It does not take breaks. It processes at exactly the same quality at task 1 and task 500.</p>
</div>

<!-- Speaker notes:
Left side: a human figure with one document in front of them — one task. Right side: an agent diamond branching to five simultaneous task nodes — 500 tasks per hour labeled.

"I want to visualize the fundamental asymmetry. A human reviewer, at peak performance, handles 40 to 60 claims per hour. A well-designed agent handles 500 claims per hour. And the agent handles all 500 at the same quality level. No fatigue, no cognitive load, no Friday afternoon attention decay."

"This is not a critique of human performance. A human reviewer is doing something fundamentally different when they handle a claim — they are exercising clinical judgment. The agent is doing pattern matching at scale. Those are different cognitive tasks. The agent is good at the pattern matching. The human is irreplaceable on the judgment."

"We are not replacing human judgment. We are removing pattern matching from the human's job."

Total slide time target: 40 seconds. -->

---

<svg class="canvas" viewBox="0 0 1280 720" xmlns="http://www.w3.org/2000/svg">
  <!-- Upward curve: capacity unlocked over time -->
  <rect width="1280" height="720" fill="#0a0e14"/>
  <!-- Axes -->
  <line x1="160" y1="560" x2="1160" y2="560" stroke="#2a3848" stroke-width="1.5"/>
  <line x1="160" y1="120" x2="160" y2="560" stroke="#2a3848" stroke-width="1.5"/>
  <!-- Gray line: headcount (flat) -->
  <polyline points="160,420 400,418 600,416 800,414 1000,412 1160,410" fill="none" stroke="#2a3848" stroke-width="2" stroke-dasharray="8,4"/>
  <!-- Blue curve: capacity (rising) -->
  <polyline points="160,420 300,410 440,390 560,355 680,305 800,245 920,185 1040,148 1160,128" fill="none" stroke="#3b9eff" stroke-width="3"/>
  <!-- Shaded area between lines -->
  <polygon points="160,420 300,410 440,390 560,355 680,305 800,245 920,185 1040,148 1160,128 1160,410 1000,412 800,414 600,416 400,418 160,420" fill="#3b9eff" opacity="0.06"/>
  <!-- Data points on curve -->
  <circle cx="400" cy="410" r="5" fill="#3b9eff" opacity="0.8"/>
  <circle cx="640" cy="320" r="5" fill="#3b9eff" opacity="0.8"/>
  <circle cx="880" cy="196" r="5" fill="#2dd4a0" opacity="0.9"/>
  <circle cx="1120" cy="136" r="7" fill="#2dd4a0" opacity="1"/>
  <!-- Axis labels -->
  <text x="280" y="590" text-anchor="middle" font-family="DM Mono, monospace" font-size="10" fill="#4a5a70">Q1</text>
  <text x="520" y="590" text-anchor="middle" font-family="DM Mono, monospace" font-size="10" fill="#4a5a70">Q2</text>
  <text x="760" y="590" text-anchor="middle" font-family="DM Mono, monospace" font-size="10" fill="#4a5a70">Q3</text>
  <text x="1000" y="590" text-anchor="middle" font-family="DM Mono, monospace" font-size="10" fill="#4a5a70">Q4</text>
  <!-- Legend -->
  <line x1="900" y1="640" x2="940" y2="640" stroke="#2a3848" stroke-width="2" stroke-dasharray="6,3"/>
  <text x="950" y="644" font-family="DM Mono, monospace" font-size="10" fill="#4a5a70">HEADCOUNT</text>
  <line x1="1060" y1="640" x2="1100" y2="640" stroke="#3b9eff" stroke-width="2"/>
  <text x="1110" y="644" font-family="DM Mono, monospace" font-size="10" fill="#3b9eff">CAPACITY</text>
</svg>

<div class="caption">
  <h2>The compound effect</h2>
  <h1>Capacity grows. Headcount stays flat.</h1>
  <p>Each new agent adds throughput without adding payroll. The gap between the lines is the value of the deployment.</p>
</div>

<!-- Speaker notes:
A chart with two lines: a flat dashed gray line (headcount) and a rising blue curve (capacity). The shaded area between them grows over time — that is the value area.

"This is the business case in one image. The gray line is headcount — flat, because we are not hiring. The blue line is capacity — rising, because each new agent adds throughput. The shaded area between the lines is the value generated by the deployment."

"By Q4, capacity is running at 2.4x the Q1 baseline, on the same headcount. In Q1 of the following year, with another cohort of agents deployed, it reaches 3.8x."

"This is not linear growth. Agent capacity compounds — each new agent benefits from the infrastructure, tooling, and data that previous agents established. The second agent is cheaper and faster to deploy than the first. The tenth is nearly turnkey."

Total slide time target: 40 seconds. -->

---

<svg class="canvas" viewBox="0 0 1280 720" xmlns="http://www.w3.org/2000/svg">
  <!-- Horizon line: invitation, open space ahead -->
  <rect width="1280" height="720" fill="#0a0e14"/>
  <!-- Gradient horizon — dark to lighter at the horizon line -->
  <defs>
    <linearGradient id="horizonGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a0e14"/>
      <stop offset="60%" stop-color="#0a0e14"/>
      <stop offset="100%" stop-color="#0d1a28"/>
    </linearGradient>
    <linearGradient id="glowGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#3b9eff" stop-opacity="0"/>
      <stop offset="50%" stop-color="#3b9eff" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#3b9eff" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect width="1280" height="720" fill="url(#horizonGrad)"/>
  <!-- Horizon line -->
  <line x1="0" y1="400" x2="1280" y2="400" stroke="#3b9eff" stroke-width="1" opacity="0.4"/>
  <!-- Glow above horizon -->
  <rect x="0" y="320" width="1280" height="160" fill="url(#glowGrad)"/>
  <!-- Road perspective lines converging at vanishing point -->
  <line x1="640" y1="400" x2="0" y2="720" stroke="#1e2a38" stroke-width="1.5" opacity="0.5"/>
  <line x1="640" y1="400" x2="1280" y2="720" stroke="#1e2a38" stroke-width="1.5" opacity="0.5"/>
  <line x1="640" y1="400" x2="200" y2="720" stroke="#1a2535" stroke-width="1" opacity="0.35"/>
  <line x1="640" y1="400" x2="1080" y2="720" stroke="#1a2535" stroke-width="1" opacity="0.35"/>
  <!-- Stars / nodes on horizon -->
  <circle cx="300" cy="400" r="2" fill="#3b9eff" opacity="0.5"/>
  <circle cx="640" cy="400" r="4" fill="#3b9eff" opacity="0.9"/>
  <circle cx="980" cy="400" r="2" fill="#3b9eff" opacity="0.5"/>
  <circle cx="480" cy="400" r="1.5" fill="#2dd4a0" opacity="0.4"/>
  <circle cx="800" cy="400" r="1.5" fill="#2dd4a0" opacity="0.4"/>
</svg>

<div class="caption">
  <h2>The horizon</h2>
  <h1>The infrastructure of tomorrow is being built today.</h1>
  <p>In three years, the organizations that deployed early will operate at a structural cost advantage that late movers cannot close.</p>
</div>

<!-- Speaker notes:
A horizon line with converging perspective lines — the visual language of an open road ahead. A single bright node at the vanishing point on the horizon.

"I want to close with a frame about timing."

"The organizations that built cloud infrastructure in 2010 — when it was expensive and uncertain — had structural cost advantages by 2015 that their competitors could not close without massive catch-up investment. We are at a similar moment with agentic infrastructure."

"The early adopters are not just buying efficiency. They are building organizational knowledge — how to deploy agents, how to measure them, how to iterate on them. That knowledge does not transfer. It has to be earned through experience."

"The horizon is open. The question is whether you start walking toward it today or wait until it is less uncertain."

Pause. Advance to the final slide.

Total slide time target: 40 seconds. -->

---

<svg class="canvas" viewBox="0 0 1280 720" xmlns="http://www.w3.org/2000/svg">
  <!-- Simple: a single lit node against dark — the beginning -->
  <rect width="1280" height="720" fill="#0a0e14"/>
  <circle cx="640" cy="340" r="80" fill="none" stroke="#3b9eff" stroke-width="1" opacity="0.1"/>
  <circle cx="640" cy="340" r="140" fill="none" stroke="#3b9eff" stroke-width="0.5" opacity="0.06"/>
  <circle cx="640" cy="340" r="8" fill="#3b9eff" opacity="1"/>
  <circle cx="640" cy="340" r="20" fill="#3b9eff" opacity="0.2"/>
</svg>

<div class="caption">
  <h2>SponAItech</h2>
  <h1>Start with one node.</h1>
  <p>sponaitech.com</p>
</div>

<!-- Speaker notes:
The closing slide returns to a single lit node — a callback to the opening network visual, but reduced to its simplest form. One node. The beginning.

"We started this conversation with a network. I want to close with a single node. Because every network — no matter how large, no matter how interconnected — started with one node. One workflow. One agent. One decision that worked."

"That is all we are asking for. Start with one node."

"Thank you."

The visual bookend — complex network opening, single node closing — creates a narrative arc in the visual language of the template itself. The audience should feel the compression: vast possibility reduced to a simple, achievable first step.

Leave on screen for Q&A. The single node against dark is a contemplative image — appropriate for conversation.

Total slide time target: 20 seconds, then open. -->
