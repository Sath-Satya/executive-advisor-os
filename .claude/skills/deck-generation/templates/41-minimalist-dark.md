<!-- TEMPLATE: minimalist-dark
     CATEGORY: Creative / Minimal
     USE WHEN: you want radical minimalism — one idea per slide, ultra-tight design, maximum impact through restraint
     SLIDE COUNT: 10
     PALETTE: Pure black / white / single accent #3b9eff
     RENDER: marp --pptx 41-minimalist-dark.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;700&display=swap');
  section {
    font-family: 'DM Sans', system-ui, sans-serif;
    background: #000000;
    color: #ffffff;
    padding: 72px 96px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  h1 {
    font-size: 5.2em;
    font-weight: 700;
    letter-spacing: -3px;
    line-height: 0.92;
    color: #ffffff;
    margin: 0;
  }
  h2 {
    font-size: 1em;
    font-weight: 300;
    letter-spacing: 0.28em;
    text-transform: uppercase;
    color: #555555;
    margin: 0 0 1.6em 0;
  }
  h3 {
    font-size: 2em;
    font-weight: 300;
    letter-spacing: -0.5px;
    color: #cccccc;
    margin: 0.4em 0 0 0;
  }
  p {
    font-size: 1em;
    font-weight: 300;
    color: #666666;
    letter-spacing: 0.04em;
    margin: 0.8em 0 0 0;
  }
  .accent {
    color: #3b9eff;
  }
  .accent-line {
    width: 48px;
    height: 3px;
    background: #3b9eff;
    margin: 2em 0 0 0;
  }
  section.lead {
    justify-content: flex-end;
    padding-bottom: 96px;
  }
  section.lead h1 {
    font-size: 7em;
  }
  section.invert {
    background: #3b9eff;
    color: #000000;
  }
  section.invert h1 {
    color: #000000;
  }
  section.invert h2 {
    color: rgba(0,0,0,0.5);
  }
  footer {
    font-size: 0.65em;
    letter-spacing: 0.18em;
    color: #333333;
    font-weight: 300;
  }
  section.invert footer {
    color: rgba(0,0,0,0.4);
  }
---

<!-- _class: lead -->
## SponAItech

# The&nbsp;Agents
# Are&nbsp;Here.

<!-- Speaker notes:
Open in silence. Let the slide breathe for five full seconds before you speak.

"We are at an inflection point. Not in the PowerPoint sense — in the real sense. The kind of inflection where the curve actually bends. The agents we built ten months ago looked like demos. The agents we're shipping today look like products. The agents we'll ship next year will look like infrastructure."

Pause. Say nothing else. Advance.

This opening slide exists to create a single feeling: inevitability. The type is large because the idea is large. The black is absolute because there is no ambiguity. The blue accent line does not appear on this slide — that comes later, when the argument needs proof. Here, we just establish stakes.

Total slide time target: 20 seconds. -->

---

## The problem

# Humans
# bottleneck
# everything.

<div class="accent-line"></div>

<!-- Speaker notes:
"Every workflow I have studied in the past two years has the same failure mode. A human being is in the middle of a process that does not require a human being. Reviewing an intake form. Routing a ticket. Reformatting a report. These are not decisions — they are transactions. And we are paying human decision-making wages for transaction work."

Let that land. Do not explain it further. The audience already feels this in their organizations — you are naming their frustration, not diagnosing it.

The accent line at the bottom is the only non-monochrome element on this slide. It signals: this is the end of the problem section. Something is about to change.

Total slide time target: 25 seconds. -->

---

## What we shipped

# <span class="accent">47</span>
# agents.

<div class="accent-line"></div>

<!-- Speaker notes:
"In Q1 alone, we deployed forty-seven production agents across five enterprise clients. Not prototypes. Not sandboxes. Production — meaning they touch real data, they execute real transactions, and a human reviews the exceptions, not the outputs."

Hold on 47. Let the number do the work.

"Each agent replaced on average 3.2 hours of daily manual effort per knowledge worker affected. Across the portfolio that is eleven full-time equivalents of capacity unlocked — without a single headcount reduction. We added capacity. The humans did harder things."

The number must be your number — replace 47 with actual deployment count before presenting. Never use a fictional number in a live client context.

Total slide time target: 35 seconds. -->

---

## The model

# Build.
# Measure.
# Repeat.

<!-- Speaker notes:
"Three words that sound like a startup platitude. Let me tell you what they actually mean in the context of agentic systems."

"Build: we scope to one workflow, one agent, one measurable outcome. Not a platform. Not a vision. One thing that works."

"Measure: we define success before we write a line of code. Cycle time. Error rate. Throughput. If we cannot measure it, we do not build it."

"Repeat: once the first agent proves the pattern, we replicate it. The second agent takes 40% less time to deploy. The third takes 60% less. The framework compounds."

This is the only slide with three sequential concepts. It earns that privilege because each word is a genuine stage — not a bullet list dressed up as drama.

Total slide time target: 40 seconds. -->

---

<!-- _class: invert -->

# One
# workflow.

<!-- Speaker notes:
This is the pivot slide. The blue background signals a shift in register — we are moving from describing the method to issuing an invitation.

"We are not proposing a transformation program. We are proposing that you identify one workflow — one — where a human being spends more than two hours per day doing something a well-designed agent could do in two minutes. That is the entry point."

"In our experience, every organization has at least a dozen of these workflows. Most have hundreds. But you do not start with hundreds. You start with one."

The inversion to blue-on-black creates maximum contrast. This slide should feel like a key change in a piece of music — same tempo, different key, everything suddenly feels different.

Total slide time target: 30 seconds. -->

---

## The evidence

# <span class="accent">83%</span>
# faster.

<p>Average throughput gain across Q1 deployments.</p>

<!-- Speaker notes:
"83%. That is not a projection — that is a measured median across our Q1 cohort. Some workflows improved by 60%. One improved by 99.4%, because the entire workflow was automatable and the human had been doing it manually for four years out of habit."

"We define faster as: time from trigger event to completed output, measured end-to-end including exception handling. Not theoretical throughput — actual wall-clock time reduction."

The percentage must be rendered large because the claim is large and the evidence is specific. The gray subtext grounds it with the qualifier — it is not a cherry-picked number.

Replace with your actual measured figure before presenting. If you do not have a measurement, do not use this slide.

Total slide time target: 30 seconds. -->

---

## The risk of waiting

# Every day
# is a cost.

<div class="accent-line"></div>

<!-- Speaker notes:
"I want to spend 30 seconds on the cost of inaction, because this is usually the conversation that does not happen. We talk about the cost of the project — the budget, the timeline, the change management. We rarely talk about the cost of not doing the project."

"If the workflow we are targeting costs you three hours of human time per day, and an agent can do it in four minutes — that is 2 hours and 56 minutes of daily waste, compounding. Over a year, across a team of ten people running this workflow, that is 7,300 hours. That is 3.5 full-time equivalents. That is real money."

"Every day you do not act is a day you are choosing to pay for that inefficiency."

Pause. Advance without explanation.

Total slide time target: 40 seconds. -->

---

## The ask

# Three
# months.
# One agent.

<!-- Speaker notes:
"Here is what we are proposing. A three-month engagement. One workflow. One agent. Fully instrumented, fully measured, fully yours at the end."

"At the end of month one: the workflow is mapped and the success metrics are agreed."
"At the end of month two: the agent is in staging, running parallel to the human workflow."
"At the end of month three: the agent is in production, the human is doing something harder, and you have a deployment pattern you can replicate across your organization."

"No multi-year roadmap. No transformation theatre. Three months. One agent. Prove the pattern."

This is the most important slide in the deck structurally. It converts everything before it into a concrete ask. The three-line rhythm reinforces the three-month structure.

Total slide time target: 45 seconds. -->

---

## SponAItech

# <span class="accent">Yes</span>
# or no?

<!-- Speaker notes:
"I am going to close with a binary. Not because I am being dramatic — because the decision genuinely is binary. Either you believe that agentic automation will reshape how your organization operates in the next 24 months, or you do not."

"If you believe it, the question is only when and with whom. We are arguing it should be now and with us — because we have the production deployments, the measurement framework, and the pattern to replicate."

"If you do not believe it — let us talk about that. I would rather have that conversation than leave the room with a polite maybe."

Hold eye contact. Do not add to this. The yes or no is literal — wait for the response.

This slide deliberately uses the accent color for "Yes" only. "Or no?" is white. We know which answer we want.

Total slide time target: 20 seconds, then silence. -->

---

<!-- _class: lead -->

## sponaitech.com

# Let's
# build.

<!-- Speaker notes:
Leave this slide on screen during any Q&A or follow-up conversation. It is a closing frame — it does not require narration.

If you must say something: "Thank you for the time. We are ready when you are."

The website in the h2 position is the only contact information needed. A phone number or email would break the minimalism — the website leads to everything.

Design note: the em-dash in "Let's" is intentional punctuation, not decoration. It contracts "let us" — an invitation to collaborate, not a command.

Total slide time target: 0. This is the ambient slide. -->
