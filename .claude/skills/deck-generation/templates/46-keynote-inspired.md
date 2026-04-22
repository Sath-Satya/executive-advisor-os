<!-- TEMPLATE: keynote-inspired
     CATEGORY: Creative / Product
     USE WHEN: Apple keynote aesthetic — product launches, capability reveals, one-idea-per-slide drama
     SLIDE COUNT: 10
     PALETTE: Pure black #000 / white / single accent #3b9eff
     RENDER: marp --pptx 46-keynote-inspired.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,300;0,400;0,600;0,700;1,300&display=swap');
  section {
    font-family: 'DM Sans', -apple-system, Helvetica, Arial, sans-serif;
    background: #000000;
    color: #ffffff;
    padding: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  h1 {
    font-size: 4.2em;
    font-weight: 700;
    letter-spacing: -2px;
    line-height: 1.0;
    color: #ffffff;
    margin: 0;
    max-width: 900px;
  }
  h2 {
    font-size: 0.85em;
    font-weight: 400;
    letter-spacing: 0.08em;
    color: #888888;
    margin: 0 0 0.8em 0;
    border: none;
    padding: 0;
    text-transform: none;
  }
  h3 {
    font-size: 1.6em;
    font-weight: 300;
    letter-spacing: -0.3px;
    color: #cccccc;
    margin: 0.5em 0 0 0;
    font-style: italic;
  }
  p {
    font-size: 1.05em;
    font-weight: 300;
    color: #888888;
    margin: 0.6em 0 0 0;
    max-width: 680px;
    line-height: 1.5;
  }
  .product-name {
    font-size: 5.5em;
    font-weight: 700;
    letter-spacing: -3px;
    color: #3b9eff;
    display: block;
    line-height: 1;
  }
  .tagline {
    font-size: 1.5em;
    font-weight: 300;
    font-style: italic;
    color: #aaaaaa;
    margin-top: 0.4em;
    display: block;
    letter-spacing: -0.2px;
  }
  .stat-hero {
    display: block;
    font-size: 7em;
    font-weight: 700;
    letter-spacing: -5px;
    line-height: 1;
    color: #ffffff;
    margin: 0;
  }
  .stat-label {
    display: block;
    font-size: 1.2em;
    font-weight: 300;
    color: #666666;
    margin-top: 0.3em;
    letter-spacing: 0.04em;
  }
  .reveal-cue {
    display: inline-block;
    border: 1px solid #333333;
    border-radius: 4px;
    padding: 0.2em 0.8em;
    font-size: 0.65em;
    font-weight: 400;
    letter-spacing: 0.14em;
    color: #444444;
    text-transform: uppercase;
    margin-top: 2em;
  }
  .one-more-thing {
    font-size: 2.8em;
    font-weight: 300;
    font-style: italic;
    color: #888888;
    display: block;
    margin-bottom: 0.2em;
  }
  footer {
    position: absolute;
    bottom: 20px;
    right: 40px;
    font-size: 0.58em;
    letter-spacing: 0.12em;
    color: #333333;
  }
---

<span class="product-name">Orion</span>
<span class="tagline">The claims intelligence platform.</span>

<!-- Speaker notes:
Open with the product name in blue — the only color on this slide. Say nothing for three full seconds.

"Today, we are introducing Orion."

Pause. Do not explain what it is. Let the name land.

"Orion is the claims intelligence platform we have been building for the past eighteen months. It is the most sophisticated claims processing system we have ever built. And it is shipping today."

[click] — next slide reveals what it does.

Apple keynote principle: the product name earns its own slide. The explanation comes after. This ordering creates anticipation — the audience hears the name before they understand it, which means they are leaning forward.

The blue product name on pure black is the signature visual of this template. Every product reveal uses this format.

Total slide time target: 15 seconds + pause. -->

---

<span class="stat-hero">22</span>
<span class="stat-label">seconds to process a claim.</span>

<!-- Speaker notes:
[click] from the previous slide.

"22 seconds."

Let the number sit alone for five seconds.

"That is the median time for Orion to process a routine claim from trigger to decision. End to end. Including querying four systems, applying clinical rules, checking eligibility, and generating the output."

"The previous record for a software-assisted claim was four minutes. We cut that by 91%."

Pause.

[click] — advance.

Apple keynote number slides follow this formula: enormous number, small label, enormous silence. The presenter does not rush. The number earns the silence.

Do not add context on this slide. The context slide comes next.

Total slide time target: 30 seconds including silence. -->

---

<h2>And it just works.</h2>
<h1>Zero configuration.<br>Production in 30 days.</h1>

<!-- Speaker notes:
"Here is what we said to every enterprise customer who evaluated Orion: it will be in production in 30 days. No 6-month implementation project. No data lake migration. No custom development."

"Zero configuration. You connect it to your claims system, your EHR, and your eligibility database. Orion does the rest."

[click] — "We have proven this across five enterprise clients. The fastest was 18 days. The slowest was 32. The average is 28. That is what we mean by zero configuration."

"We did not simplify Orion by removing capability. We built a product that earns its complexity internally and presents simplicity externally."

The "And it just works" echo of the Steve Jobs phrasing is intentional — it is a recognizable signal of this template's design language. It tells the audience: this is a product presentation, not a consulting pitch.

Total slide time target: 35 seconds. -->

---

<h1>The world's most accurate<br>secondary code detector.</h1>
<h3>94% on the first model. Improving every quarter.</h3>

<!-- Speaker notes:
"Every claims platform has a leakage detection feature. Ours is different — not by degree, but in kind."

"Orion was trained on 4.2 million historical claims across twelve health plan clients. The secondary code detection model — the capability that catches incorrect upcoding — performs at 94% accuracy on claims it has never seen before."

[click] — "To put that in context: the best rule-based systems in the market today perform at 68%. Our nearest AI-based competitor is at 79%. We are at 94%. And because Orion learns from every claim it processes, that number improves every quarter."

"We do not call it the best secondary code detector in the world lightly. We tested it against every published benchmark we could find. It is the best."

The superlative headline is an Apple keynote hallmark — but it must be earned with evidence. The h3 provides the qualifier: "94% on the first model." The claim is specific, not hyperbolic.

Total slide time target: 40 seconds. -->

---

<h2>The missing piece.</h2>
<h1>Explainable decisions.</h1>
<p>Every Orion decision includes a plain-language explanation. Not a confidence score — a reason. One that your reviewers can read, agree with, and act on.</p>

<!-- Speaker notes:
"Every AI claims system before Orion has the same problem: it is a black box. It tells you what to do, but not why. Your reviewer approves or denies based on a recommendation they cannot interrogate. That is a compliance risk. It is an auditor risk. And it is a trust problem."

"Orion solves this with what we call Transparent Decisions. Every claim output includes a plain-language explanation: 'This claim was flagged because the secondary procedure code 27447 appears with a primary diagnosis that does not meet clinical criteria for bilateral knee replacement per CMS guidelines effective January 2025. Recommended action: request clinical documentation before approval.'"

"Your reviewer reads that in eight seconds. They understand it. They can act on it. They can override it with documentation. The audit trail is complete."

"Explainability is not a feature we added. It is the architecture. Orion reasons in language because language is how decisions are communicated."

The "missing piece" framing is a classic Jobs positioning: we identified what every competitor was missing, and we built the solution.

Total slide time target: 50 seconds. -->

---

<span class="product-name" style="font-size:3.8em; color:#2dd4a0;">Orion&nbsp;Mobile</span>
<span class="tagline">Your claims intelligence — everywhere.</span>

<!-- Speaker notes:
"One more thing."

Pause.

"We know that claims leadership is not always at a desk. Your VP of Claims Operations is on a flight. Your Medical Director is between patient rounds. Your compliance team is at a conference."

[click] — "Today we are also introducing Orion Mobile. The full intelligence of the Orion platform — available on iOS and Android."

"Orion Mobile is not a reporting dashboard. It is the complete decision engine in your pocket. You can review flagged claims, approve exceptions, interrogate the explanation for any decision, and override with documentation — from anywhere."

"It syncs in real time. It is built on the same infrastructure as the enterprise platform. It has the same security posture. And it is launching in App Store and Google Play today."

The new product on this slide uses the mint green (#2dd4a0) instead of blue — differentiating it visually from the primary product while staying within the palette. This is the Jobs "one more thing" structural reveal.

Total slide time target: 35 seconds. -->

---

<h1>We believe the future of<br>claims is autonomous.</h1>
<h3>Assisted today. Supervised tomorrow. Autonomous next year.</h3>

<!-- Speaker notes:
"I want to spend 60 seconds on where we are going. Because Orion today is the foundation, not the destination."

"Today: assisted. Every Orion decision is reviewed by a human. The system recommends; the human approves. This is the right starting point — it builds trust, it generates training data, it establishes the audit trail."

"Tomorrow: supervised. Routine claims — the 80% that are straightforward — are processed straight through. Humans review the flagged 20%. The system runs autonomously on the known patterns; humans apply judgment to the unknowns."

"Next year: autonomous. Orion processes claims end-to-end, from submission to payment, without a human decision for routine cases. Humans are the exception handlers, the model trainers, the policy setters. The system is the operator."

"This is not a prediction. This is the roadmap we have committed to — with specific milestones, specific accuracy thresholds, and specific customer commitments attached to each stage."

This slide is the vision statement — the moment where the product story expands from 'this is what we built' to 'this is where we are going.' The three-tier statement (assisted / supervised / autonomous) maps directly to the product roadmap.

Total slide time target: 55 seconds. -->

---

<h2>Available today.</h2>
<span class="stat-hero" style="font-size:4.8em;">$840K</span>
<span class="stat-label">Phase 1 + 2 implementation. 273x first-year ROI.</span>

<!-- Speaker notes:
"Orion is available today. If you sign before the end of this month, we will have your environment provisioned and model calibration started within 10 business days."

"The implementation investment for Phase 1 and Phase 2 is $840,000. That is model calibration, shadow deployment, change management support, and full integration with your existing systems."

"At current model performance — before any fine-tuning on your specific claims data — the projected first-year recovery is $230 million in prevented leakage on a plan your size. That is a 273x return on implementation cost."

"We stand behind that projection. If we do not achieve the projected ROI within 12 months of Phase 3 launch, we will extend the contract at no cost until we do. That is in writing."

The price-on-slide approach is unusual in enterprise software pitches but effective in the keynote format. It communicates confidence. It removes the "ask the sales team" ambiguity. It treats the audience as capable of evaluating the business case directly.

Total slide time target: 40 seconds. -->

---

<h1>SponAItech.</h1>
<h3>Agentforce for the enterprise. Built in the real world.</h3>

<!-- Speaker notes:
"SponAItech. We are an AI consulting company, but that does not capture what we actually do. We build production AI systems for healthcare organizations — systems that are live, measured, and improving every quarter."

"Orion is our flagship product. It is the result of 18 months of development, 4.2 million training claims, and deployment experience with five enterprise clients."

"We do not build demos. We build infrastructure."

"If you are ready to talk about implementation, my team is available today. We have reserved capacity for three new implementation starts before the end of the quarter."

[click] — final slide.

This slide is the brand moment — the presenter says the company name, not as a logo but as a statement. "SponAItech" is spoken with the weight of everything that has come before it.

Total slide time target: 25 seconds. -->

---

<h1>Thank you.</h1>
<p style="margin-top:1em; font-size:0.85em; color:#555555;">sponaitech.com</p>

<!-- Speaker notes:
Leave this slide up for Q&A.

"Thank you."

Two words. Nothing else. The Apple keynote closing is always brief — the product has done the talking.

If you must add: "We would love to continue the conversation. My team will be in the room for the next two hours."

Then stop talking.

The white "Thank you" on black is the final image the audience carries with them. It should be the cleanest slide in the deck — and it is.

Total slide time target: 0. Ambient. -->
