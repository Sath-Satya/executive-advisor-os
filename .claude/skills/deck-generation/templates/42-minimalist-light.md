<!-- TEMPLATE: minimalist-light
     CATEGORY: Creative / Minimal
     USE WHEN: Swiss-style minimalism for a design-conscious audience — white bg, grid-anchored, generous whitespace
     SLIDE COUNT: 10
     PALETTE: Pure white / black / single accent #f06070
     RENDER: marp --pptx 42-minimalist-light.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;600;700&display=swap');
  section {
    font-family: 'DM Sans', Helvetica, Arial, system-ui, sans-serif;
    background: #ffffff;
    color: #111111;
    padding: 64px 80px 64px 80px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }
  h1 {
    font-size: 3.6em;
    font-weight: 700;
    letter-spacing: -1.5px;
    line-height: 1.0;
    color: #111111;
    margin: 0 0 0.1em 0;
  }
  h2 {
    font-size: 0.72em;
    font-weight: 600;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #999999;
    margin: 0 0 2.4em 0;
    border: none;
    padding: 0;
  }
  h3 {
    font-size: 1.4em;
    font-weight: 300;
    letter-spacing: -0.2px;
    color: #444444;
    margin: 0.6em 0 0 0;
  }
  p {
    font-size: 0.9em;
    font-weight: 300;
    color: #777777;
    line-height: 1.7;
    max-width: 560px;
    margin: 0.8em 0 0 0;
  }
  strong {
    font-weight: 700;
    color: #111111;
  }
  .accent {
    color: #f06070;
  }
  .rule {
    width: 32px;
    height: 2px;
    background: #f06070;
    margin: 0 0 2em 0;
  }
  .rule-full {
    width: 100%;
    height: 1px;
    background: #eeeeee;
    margin: 1.6em 0;
  }
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3em;
    margin-top: 1.6em;
  }
  .grid-cell {
    border-top: 2px solid #111111;
    padding-top: 0.8em;
  }
  .grid-cell h4 {
    font-size: 0.78em;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #999999;
    margin: 0 0 0.4em 0;
  }
  .grid-cell p {
    max-width: none;
    margin: 0;
    font-size: 0.85em;
  }
  .number-hero {
    font-size: 6em;
    font-weight: 700;
    letter-spacing: -4px;
    color: #111111;
    line-height: 1;
    margin: 0.1em 0 0 0;
  }
  section.cover {
    justify-content: flex-end;
    padding-bottom: 80px;
  }
  section.cover h1 {
    font-size: 4.8em;
  }
  footer {
    font-size: 0.6em;
    letter-spacing: 0.16em;
    color: #cccccc;
    font-weight: 400;
  }
---

<!-- _class: cover -->

## Claims Intelligence — 2026 Roadmap

# Reinventing
# the Intake
# Experience.

<div class="rule"></div>

<!-- Speaker notes:
Open with the rule visible — the short red horizontal line at the bottom left is the signature element of this template. Everything hugs the left margin, like a grid from a Swiss design grid.

"Today I want to walk you through what we have built and where we are taking it. The intake experience — the moment a member first contacts us about a claim — is the highest-friction point in our entire service chain. We have been measuring it, instrumenting it, and redesigning it. This is the roadmap."

Note the hierarchy: the headline is the subject, the subtext above it is the context, and the red rule is the visual full stop. The presenter's voice provides all connective tissue. The slide provides none.

The cover slide anchors the bottom rather than the center — this is a deliberate Swiss grid choice. Content grows upward from a baseline, creating gravitational stability.

Total slide time target: 20 seconds. -->

---

## The current state

# Intake takes
# **9.2 minutes.**

<h3>Industry benchmark: <span class="accent">4.1 minutes.</span></h3>

<div class="rule-full"></div>

<p>Every minute over benchmark is a satisfaction risk. Our NPS for first-contact resolution is 34 points below members who resolve in under five minutes.</p>

<!-- Speaker notes:
"Let me start with a number that should bother everyone in this room: 9.2 minutes. That is our median first-contact intake time. The industry benchmark for best-in-class operations is 4.1 minutes. We are 124% above benchmark."

"This is not an efficiency problem. It is a member experience problem. We have correlated intake duration with NPS, and the relationship is stark: members who resolve in under five minutes score 34 NPS points higher than members who take nine minutes or more. That is not noise — that is signal."

The Swiss approach: state the fact, provide the comparison, connect it to the outcome. No story arc, no drama. The data earns its own authority.

The full-width rule at 1px separates the headline claim from the supporting evidence without hierarchy confusion.

Total slide time target: 35 seconds. -->

---

## What we are building

# AI-guided
# intake.

<div class="rule"></div>

<div class="grid-2">
<div class="grid-cell">
<h4>What it does</h4>
<p>Pre-populates member context, suggests claim codes, and flags documentation gaps before the agent speaks.</p>
</div>
<div class="grid-cell">
<h4>What it does not do</h4>
<p>It does not replace the agent. It removes the lookup work so the agent can focus on the member.</p>
</div>
</div>

<!-- Speaker notes:
"The solution is not a chatbot. Let me be clear about that, because when people hear AI-assisted intake they imagine replacing the human agent. That is not what we are building."

"We are building a co-pilot. Before the agent says hello, the system has already pulled the member's claim history, predicted the three most likely claim codes for this call type, and flagged if any supporting documentation is missing. The agent sees this context on screen. The agent's first question is no longer 'can you give me your member ID' — it is 'I see you are calling about your hip replacement claim, is that right?'"

"That single sentence is worth minutes. Because confirmation takes four seconds; lookup takes two minutes."

The two-column grid is anchored by a black 2px top rule — a grid convention, not decoration. It visually separates the two columns while keeping the page white.

Total slide time target: 40 seconds. -->

---

## Design principle

# Invisible
# intelligence.

<p>The AI should never be visible to the member. Only its effects should be felt: faster resolution, more accurate coding, less repetition.</p>

<!-- Speaker notes:
"Here is the design principle that guides every decision on this project: invisible intelligence. The member should never know an AI system is involved. They should only feel its effects — a faster conversation, an agent who already knows their context, a resolution that does not require a callback."

"This principle has real engineering implications. We do not show the member a chatbot interface. We do not tell them their claim is being processed by AI. We do not introduce latency with loading spinners. The intelligence runs ahead of the conversation, not alongside it."

This slide is deliberately brief. One principle. One sentence of explanation. The rest is delivered by voice.

The Swiss grid means the text is left-aligned, ragged right, with generous right-side whitespace. The whitespace is load-bearing — it creates the feeling of confidence and restraint.

Total slide time target: 30 seconds. -->

---

## The numbers

<div class="number-hero"><span class="accent">4.3</span></div>
<h3>projected minutes to intake completion.</h3>

<div class="rule-full"></div>

<p>Modeled from pilot data across 1,200 test calls. Statistical confidence: 94%. Deployment target: Q3.</p>

<!-- Speaker notes:
"Based on our pilot — 1,200 test calls across three agent cohorts — we are projecting an intake time of 4.3 minutes. That puts us at benchmark. Not below benchmark — at benchmark. Because our goal for Q3 is not to be best-in-class globally. It is to be competitive."

"Best-in-class is the Q4 target, when we add the documentation gap prediction layer. But Q3 is: close the gap."

"94% confidence on the model. The remaining 6% variance is call types we did not have enough training data to model — complex multi-claimant scenarios and estate claims. Those are a rounding error in volume but an edge case in the model."

The large number is the hero of this slide. Everything else is context for it. The red accent on the number is the only use of color on this slide — it earns the emphasis.

Total slide time target: 35 seconds. -->

---

## The roadmap

<div class="grid-2">
<div class="grid-cell">
<h4>Q2 — Foundation</h4>
<p>Context pre-population live for 20% of agent cohort. Baseline measurement running.</p>
</div>
<div class="grid-cell">
<h4>Q3 — Scale</h4>
<p><strong>Full rollout.</strong> AI-guided intake for all inbound claims. Target: 4.3 min median.</p>
</div>
</div>

<div class="rule-full"></div>

<div class="grid-2">
<div class="grid-cell">
<h4>Q4 — Intelligence</h4>
<p>Documentation gap prediction. Proactive outreach before the member calls.</p>
</div>
<div class="grid-cell">
<h4>2027 — Autonomy</h4>
<p>Straight-through processing for simple claim types. Agent handles exceptions only.</p>
</div>
</div>

<!-- Speaker notes:
"Four quarters. Four phases. I want to walk through each briefly."

"Q2 — we are proving the pattern with 20% of the agent population. This is not a pilot. The infrastructure is production. The 20% scope is because change management takes time, not because the technology is uncertain."

"Q3 — full rollout. Every inbound claim call is AI-assisted. This is the benchmark-closing quarter."

"Q4 — we add prediction. The system will identify members whose documentation packages are incomplete and trigger outreach before they call us. We stop the call before it happens."

"2027 — straight-through processing. Simple claim types — dental, vision, preventive — will not require an agent at all. The member gets a decision. The agent handles the complex cases."

This is the most information-dense slide in the deck. It earns that density because it is the roadmap — the one slide where the audience needs all four phases at once for comparison.

Total slide time target: 55 seconds. -->

---

## The risk

# Change
# management
# is the hard part.

<!-- Speaker notes:
"I want to name the risk explicitly, because pretending it does not exist is how projects fail."

"The technology is the easy part. We have the model. We have the pilot data. We have the infrastructure. The hard part is the 400 agents who will have a new interface in their workflow in Q3. Some of them have been running intake the same way for eight years. The system that helps them will feel, at first, like the system watching them."

"Our change management plan: agent involvement in the design from day one. Not after the product is built — during it. The intake co-pilot was designed with eight agent interviews, two focus groups, and a three-week shadowing study. The agents know this system. Some of them named the features."

No bullets. No lists. One idea, stated plainly. The weight of this slide is intentional — it is a rare moment of candor in a business presentation. It builds credibility.

Total slide time target: 40 seconds. -->

---

## What we need

# Three decisions,
# one meeting.

<div class="rule"></div>

<p>Budget approval for Q3 infrastructure scaling. Go/no-go on the Q4 prediction layer. Change management resourcing.</p>

<!-- Speaker notes:
"We are asking for three decisions in this meeting."

"One: budget approval for Q3 infrastructure. The compute cost for full-cohort AI-assisted intake is $18,000 per month in Azure. That is against a projected benefit of $340,000 per month in agent-hour savings at current call volume. We need a yes on the budget."

"Two: go or no-go on the Q4 documentation prediction layer. This requires a data-sharing agreement with our document management vendor. If we are doing it, we need to start procurement now."

"Three: resourcing for change management. We need 0.5 FTE from HR and 0.25 FTE from Training for the Q3 rollout. Not full-time. Half-time for one quarter."

"Those are three concrete asks. I want to leave this meeting with answers on all three."

The structure of this slide — one headline, one paragraph — mirrors the structure of the ask: direct, bounded, actionable.

Total slide time target: 50 seconds. -->

---

## Summary

<div class="grid-2">
<div class="grid-cell">
<h4>The problem</h4>
<p>9.2 min intake vs 4.1 min benchmark. 34-point NPS gap.</p>
</div>
<div class="grid-cell">
<h4>The solution</h4>
<p>AI-guided intake co-pilot. Invisible to members. Live Q3.</p>
</div>
</div>

<div class="rule-full"></div>

<div class="grid-2">
<div class="grid-cell">
<h4>The ask</h4>
<p>Budget + Q4 go/no-go + 0.75 FTE change management.</p>
</div>
<div class="grid-cell">
<h4>The outcome</h4>
<p><strong><span class="accent">4.3 min</span> median intake. Benchmark-competitive by Q3.</strong></p>
</div>
</div>

<!-- Speaker notes:
"Let me give you the one-screen summary before we open for questions."

"Problem: we are 9.2 minutes at intake against a 4.1-minute benchmark, and the member satisfaction gap is measurable and large."

"Solution: an AI co-pilot that pre-populates context before the agent speaks, invisible to the member, live in Q3."

"Ask: budget, one procurement decision, 0.75 FTE."

"Outcome: 4.3 minutes. Benchmark-competitive."

"Questions?"

This is the Swiss grid at its most rigorous — four equal cells, each with a category label and a precise statement. No wasted words. The grid itself is the argument: everything fits, everything connects, everything is accounted for.

Total slide time target: 35 seconds, then open Q&A. -->

---

## SponAItech

# Thank you.

<div class="rule"></div>

<p>sponaitech.com &nbsp;&nbsp;|&nbsp;&nbsp; sathiyaraj.t@gmail.com</p>

<!-- Speaker notes:
Leave this slide on screen during Q&A.

The closing slide is the simplest slide in the deck. It restates the company name at the category level (h2), gives a direct closing (h1), and provides contact information as a single line in small type.

No bullet list of takeaways. No "thank you for your time." The words "thank you" say that. Everything else would dilute it.

Swiss typography principle: the closing slide should feel like the last measure of a symphony — clean resolution, not a flourish.

Total slide time target: ambient. -->
