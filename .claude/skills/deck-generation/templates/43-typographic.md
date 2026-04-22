<!-- TEMPLATE: typographic
     CATEGORY: Creative / Design-Forward
     USE WHEN: typography IS the design — letterforms carry meaning, size contrast is the hierarchy
     SLIDE COUNT: 10
     PALETTE: Cream #f7f4ef / ink #1c1a18 / warm gray #9a9590
     RENDER: marp --pptx 43-typographic.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Mono:wght@400;500&family=DM+Sans:wght@300;400;700&display=swap');
  section {
    font-family: 'DM Sans', system-ui, sans-serif;
    background: #f7f4ef;
    color: #1c1a18;
    padding: 56px 80px;
    overflow: hidden;
  }
  /* Typographic hero: DM Serif Display italic at extreme scale */
  h1 {
    font-family: 'DM Serif Display', Georgia, serif;
    font-style: italic;
    font-size: 5.8em;
    letter-spacing: -3px;
    line-height: 0.9;
    color: #1c1a18;
    margin: 0;
  }
  /* Meta label: DM Mono small caps feel */
  h2 {
    font-family: 'DM Mono', monospace;
    font-size: 0.68em;
    font-weight: 400;
    letter-spacing: 0.24em;
    text-transform: uppercase;
    color: #9a9590;
    margin: 0 0 1.2em 0;
    border: none;
    padding: 0;
  }
  /* Secondary display: DM Serif non-italic */
  h3 {
    font-family: 'DM Serif Display', Georgia, serif;
    font-size: 2.4em;
    font-style: normal;
    letter-spacing: -1px;
    color: #1c1a18;
    margin: 0.2em 0 0 0;
  }
  /* Body: DM Sans light */
  p {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.88em;
    font-weight: 300;
    color: #6b6560;
    line-height: 1.75;
    max-width: 540px;
    margin: 0.8em 0 0 0;
  }
  /* Mono annotation: for stats and callouts */
  .mono {
    font-family: 'DM Mono', monospace;
    font-size: 0.72em;
    color: #9a9590;
    letter-spacing: 0.12em;
  }
  /* Giant letter — single character as visual */
  .letterform {
    font-family: 'DM Serif Display', Georgia, serif;
    font-style: italic;
    font-size: 22em;
    line-height: 0.85;
    color: rgba(28,26,24,0.07);
    position: absolute;
    right: -0.1em;
    top: -0.15em;
    pointer-events: none;
    letter-spacing: -10px;
  }
  /* Pull quote: large DM Serif, centered, spanning full width */
  .pullquote {
    font-family: 'DM Serif Display', Georgia, serif;
    font-style: italic;
    font-size: 2.2em;
    letter-spacing: -0.5px;
    line-height: 1.2;
    color: #1c1a18;
    text-align: center;
    padding: 0 4em;
    margin: auto 0;
  }
  /* Size contrast pair */
  .size-pair {
    display: flex;
    align-items: baseline;
    gap: 0.3em;
    margin-top: 0.4em;
  }
  .size-big {
    font-family: 'DM Serif Display', serif;
    font-style: italic;
    font-size: 4em;
    letter-spacing: -2px;
    line-height: 1;
  }
  .size-small {
    font-family: 'DM Mono', monospace;
    font-size: 0.72em;
    color: #9a9590;
    letter-spacing: 0.12em;
    text-transform: uppercase;
  }
  footer {
    font-family: 'DM Mono', monospace;
    font-size: 0.6em;
    letter-spacing: 0.18em;
    color: #c8c4be;
  }
---

## SponAItech ◆ Thought Leadership Series

# Why We
# Bet on
# *Agents.*

<!-- Speaker notes:
The opening slide places the italic serif at maximum scale. The word "Agents" is italicized in the Markdown via the asterisks, which in this template's h1 style renders as DM Serif Display italic. The tilt of the letterform creates forward motion.

"This is a presentation about a bet. A specific bet, made at a specific moment, with specific evidence. I want to tell you what the bet is, why we made it, and what has happened since."

Typography note for adaptation: the h1 on this slide is deliberately line-broken at three lines to create a stacked effect. Do not let it reflow to a single line — use manual line breaks if needed.

The background ghosts (`.letterform`) would show on rendered slides as a nearly-invisible oversized italic letter. In Marp rendering, position:absolute may not work — in that case, the effect is removed gracefully and the slide remains clean. Consider it a progressive enhancement.

Total slide time target: 20 seconds. -->

---

## The moment

<div class="pullquote">"Every ten years, there is a moment where the underlying substrate of software changes. We are in that moment."</div>

<p class="mono" style="text-align:center; margin-top:1.6em;">— SponAItech strategy memo, Q4 2024</p>

<!-- Speaker notes:
This slide is a pull quote — the entire slide IS the quote. No other information.

"I wrote this in our internal strategy memo eighteen months ago. At the time, it felt like a provocation. Today it feels like a statement of fact."

"The substrate shift I was describing: from deterministic software — code that does exactly what you tell it to do — to probabilistic software — systems that reason, infer, and act. Agents are the practical expression of that shift."

The quote is set in DM Serif Display italic at 2.2em, padded on both sides to create breathing room. The attribution is in DM Mono, small, at the bottom center. The contrast in scale between the quote and the attribution mirrors the contrast in authority.

Allow 8 full seconds of silence after reading the quote. Let the audience sit with it before moving on.

Total slide time target: 35 seconds including silence. -->

---

## The bet

<h1 style="font-size:7.5em; line-height:0.85;">Agents<br>first.</h1>

<p class="mono" style="margin-top:1.4em;">Not AI features. Not chatbots. Not copilots.<br>Autonomous agents that complete workflows end-to-end.</p>

<!-- Speaker notes:
"When we say agents-first, we mean a very specific thing. We do not mean adding a chat interface to an existing product. We do not mean a large language model that suggests the next word. We mean a system that can receive a task, reason about it, take actions across multiple systems, and deliver a completed output — without a human in the loop for the routine steps."

"This is a meaningfully harder technical problem than the chatbot problem. And it is a meaningfully larger business opportunity than the chatbot opportunity."

The oversized h1 at 7.5em creates near-full-bleed typography. "Agents" fills the left two-thirds of the slide. "first." is the kicker — smaller in implied weight because it is a continuation of the same line, but equal in typographic measure.

Total slide time target: 35 seconds. -->

---

## The evidence

<div class="size-pair">
<span class="size-big">47</span>
<span class="size-small">production deployments<br>in Q1 alone.</span>
</div>

<div class="size-pair" style="margin-top:0.6em;">
<span class="size-big">83%</span>
<span class="size-small">average throughput<br>improvement measured.</span>
</div>

<div class="size-pair" style="margin-top:0.6em;">
<span class="size-big">11</span>
<span class="size-small">FTE equivalents of<br>capacity unlocked.</span>
</div>

<!-- Speaker notes:
Three data points. Each rendered as a size-contrast pair: the number in DM Serif Display italic at 4em, the label in DM Mono at 0.72em. The scale difference is roughly 5.5x — enough to make the number a headline and the label a footnote, on the same line.

"Let me give you the evidence for the bet. Forty-seven production deployments in Q1 — not demos, not sandboxes, production. 83% average throughput improvement across those deployments — measured, not modeled. Eleven FTE equivalents of capacity unlocked — meaning the humans who were doing that work are now doing something harder."

"This is the quarter where agentic deployment stopped being a research project and became a production practice."

The stacked three-pair layout creates visual rhythm. The eye reads: big number → label → next big number → label → next. This is faster than bullets and more impactful than a chart.

Total slide time target: 40 seconds. -->

---

## The architecture

## *Three layers.*

<h3>Perception ◆ Reasoning ◆ Action</h3>

<p>Every agent we build operates on the same substrate: it perceives context, it reasons about what to do, and it takes action. The complexity lives inside each layer — not in the orchestration.</p>

<!-- Speaker notes:
"I want to spend a minute on architecture, because the design decisions here are the source of the performance numbers."

"Every agent we build has three layers. Perception: what does the agent know about the world right now? This is context ingestion — pulling member data, claim status, document state, conversation history. Reasoning: given what the agent knows, what should it do? This is where the language model sits — not as a chatbot, but as a decision engine. Action: what does the agent actually do? This is where it writes to systems, sends messages, flags exceptions."

"The reason our agents perform is that we have invested heavily in the perception layer. Most teams under-invest here and then over-spend on prompt engineering to compensate for weak context. We do it the other way."

The three-part h3 uses a diamond character ◆ as a separator — a typographic convention that reads as enumeration without the visual weight of bullets.

Total slide time target: 45 seconds. -->

---

## The human role

<div class="pullquote">"The agent handles the transaction. The human handles the exception — which is the only part worth a human's attention."</div>

<!-- Speaker notes:
"I get this question in every client conversation: what happens to the people? Let me answer it directly."

"In every deployment we have done, the human role has changed but not disappeared. The agent handles the routine transaction — the lookup, the routing, the code matching, the status update. The human handles the exception — the ambiguous case, the member in distress, the multi-system conflict that requires judgment."

"And here is the important point: exceptions are the only part of the job that required a human's attention in the first place. We have just removed the scaffolding work so that the human can spend 100% of their time on the 20% of cases that actually need them."

"That is not a headcount reduction story. That is a job quality improvement story."

This is the second pull quote slide. The context note: pull quotes should be used at most twice in a deck. Each use should carry weight — a statement worth stopping for.

Total slide time target: 40 seconds. -->

---

## The pattern

## *Build once.*

<h1 style="font-size:3.2em;">Replicate
everywhere.</h1>

<p>The first agent in any organization takes 8 weeks. The second takes 4. By the fifth, the pattern is institutional. The framework compounds.</p>

<!-- Speaker notes:
"The business model for agentic deployment is not a project business. It is a compounding business."

"The first agent takes eight weeks. Not because the technology is slow — because the organizational readiness work takes time. Mapping the workflow, getting data access, training the model on domain terminology, running the parallel test period."

"The second agent takes four weeks. The workflow mapping methodology is established. Data access patterns are known. The parallel test process is repeatable."

"By the fifth agent, the organization has an internal deployment pattern. They can start building agents themselves, with us in a governance role. The framework compounds."

"This is why we structure our engagements with a framework fee, not a per-agent fee. We are not selling you agents — we are selling you the ability to build agents."

The "Build once / Replicate everywhere" layout uses h2 for the italic lead-in and h1 for the continuation. The size contrast creates a two-beat rhythm: small italic whisper → large serif declaration.

Total slide time target: 45 seconds. -->

---

## The timeline

<h2 style="margin-bottom:0.4em;">Where we were</h2>
<h1 style="font-size:2em; margin:0; line-height:1.1;">Promising demos.</h1>

<div style="margin: 1.4em 0; width: 100%; height: 2px; background: #1c1a18; opacity: 0.12;"></div>

<h2 style="margin-bottom:0.4em;">Where we are</h2>
<h1 style="font-size:2em; margin:0; line-height:1.1;">Production deployments.</h1>

<div style="margin: 1.4em 0; width: 100%; height: 2px; background: #1c1a18; opacity: 0.12;"></div>

<h2 style="margin-bottom:0.4em;">Where we are going</h2>
<h1 style="font-size:2em; font-style:italic; margin:0; line-height:1.1; font-family:'DM Serif Display', serif;">Infrastructure.</h1>

<!-- Speaker notes:
"Three sentences about where we stand."

"Eighteen months ago: promising demos. Everyone was impressed. No one was in production."

"Today: production deployments. Forty-seven of them. With measurement."

"Next year: infrastructure. The same way cloud moved from 'interesting experiment' to 'how we run everything' — agentic automation is moving from 'we have some agents' to 'agents are the operating system of the organization.'"

The three-section structure is separated by hairline rules (2px, 12% opacity) rather than whitespace alone. This creates section breaks that read as timeline markers without using bullets or chevrons.

The final item — "Infrastructure." — is set in italic serif to mark it as a prediction rather than a fact. Small but intentional typographic signal.

Total slide time target: 35 seconds. -->

---

## The invitation

<h1 style="font-size:6em; letter-spacing:-4px; line-height:0.88;">One call.<br>One workflow.<br>One agent.</h1>

<!-- Speaker notes:
"Here is the invitation. One call to identify your highest-friction workflow. One workflow to target for the first agent. One agent built, measured, and handed back to you in 90 days."

"If it does not work, we will tell you before we take your money. The measurement framework is agreed before the engagement starts. If we cannot project a 40% throughput improvement or better on the identified workflow, we do not take the engagement."

"That is how confident we are in the pattern."

Pause.

"Call us."

The h1 at 6em creates three-line vertical fill similar to the opening slide. The closing slide deliberately echoes the opening typographic scale — a bookend. The content has moved from question (Why We Bet on Agents) to answer (One agent. Now.) but the letterform treatment is the same.

Total slide time target: 30 seconds, then ambient. -->

---

<!-- _paginate: false -->

## sponaitech.com

<h1 style="font-family:'DM Serif Display',serif; font-style:italic; font-size:8em; letter-spacing:-5px; line-height:0.85; margin:0; color:#1c1a18;">Thank<br>you.</h1>

<p class="mono" style="margin-top:2em;">sathiyaraj.t@gmail.com</p>

<!-- Speaker notes:
The closing slide removes pagination (_paginate: false) to keep the final frame clean.

"Thank you" in italic DM Serif Display at 8em is the largest type in the entire deck. It earns that scale because it is the final statement — not a functional slide but an emotional one. The audience should feel the weight of the thanks.

Leave on screen. Say nothing else.

Design note: the closing slide breaking the pagination rule is intentional. The final frame is not a slide — it is a pause. Removing the page number reinforces that the formal presentation is over. What follows is conversation.

Total slide time target: ambient. -->
