<!-- TEMPLATE: takahashi-method
     CATEGORY: Creative / Rapid-Fire
     USE WHEN: Takahashi method — one giant word per slide, rapid pacing, 2-3 seconds per slide, notes carry all narrative
     SLIDE COUNT: 20
     PALETTE: White #ffffff / black #000000 (pure — zero decoration)
     RENDER: marp --pptx 49-takahashi-method.md -->
---
marp: true
theme: default
paginate: false
size: 16:9
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@700;900&display=swap');
  section {
    font-family: 'DM Sans', system-ui, -apple-system, Helvetica, Arial, sans-serif;
    background: #ffffff;
    color: #000000;
    padding: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  /* THE word — fills the screen */
  h1 {
    font-size: 12em;
    font-weight: 900;
    letter-spacing: -8px;
    line-height: 0.88;
    color: #000000;
    margin: 0;
    padding: 0 0.1em;
    word-break: break-word;
    hyphens: manual;
  }
  /* Two-word slide: slightly smaller to fit */
  h1.two {
    font-size: 7.5em;
    letter-spacing: -5px;
    line-height: 0.9;
  }
  /* Three-word / phrase slide */
  h1.three {
    font-size: 5em;
    letter-spacing: -3px;
    line-height: 0.95;
  }
  /* Inverted — black bg, white text — for key pivots */
  section.pivot {
    background: #000000;
  }
  section.pivot h1 {
    color: #ffffff;
  }
  /* No footer, no decoration */
---

# Agents.

<!-- Speaker notes:
Slide 1. The single word "Agents." with a period. 2 seconds. Advance.

Spoken narrative: "Agents. That is the subject of the next six minutes and forty seconds. Not AI in general. Not machine learning. Agents. Software that receives a goal and figures out how to achieve it."

Takahashi principle: the word is the entire slide. The audience reads it in one heartbeat. You advance before they can over-read it. The period is intentional — it is a statement, not a question.

Total slide time target: 3 seconds. -->

---

# Now.

<!-- Speaker notes:
Slide 2. "Now." — present tense. 2 seconds. Advance.

Spoken narrative: "Not in three years. Not when the technology matures. Now. Agents are in production today. At enterprise scale. Doing real work. Making real decisions."

The period again. Every slide in the Takahashi method uses a period or no punctuation. Questions are rare and deliberate.

Total slide time target: 2 seconds. -->

---

# <span class="two">Not<br>a demo.</span>

<!-- Speaker notes:
Slide 3. "Not a demo." — two lines. 3 seconds.

Spoken narrative: "I want to say this clearly upfront: everything I am about to tell you is from production deployments. Real clients. Real claims. Real data. Not a demo environment. Not a sandbox. Production."

The "not" creates contrast — it addresses the assumption the audience is carrying. Many AI presentations are demos. This one is about what actually works.

Total slide time target: 3 seconds. -->

---

<!-- _class: pivot -->

# 47.

<!-- Speaker notes:
Slide 4. Black background pivot. "47." — a number. 2 seconds.

Spoken narrative: "Forty-seven agents deployed in Q1. Across five enterprise healthcare clients. Each one processing real claims, real member data, real decisions. Forty-seven. In one quarter."

The black background pivot marks a shift in register — we are moving from framing to evidence. The audience knows that when the background inverts, something important is being said.

Total slide time target: 2 seconds. -->

---

# Production.

<!-- Speaker notes:
Slide 5. Back to white. "Production." — reiterates the theme.

Spoken narrative: "All forty-seven in production. Not pilot. Not proof of concept. Production. Meaning the agent's output is the actual output. Meaning a human reviews exceptions, not every decision. Meaning the system is trusted enough to run without training wheels."

Total slide time target: 2 seconds. -->

---

# <span class="two">9.2<br>minutes.</span>

<!-- Speaker notes:
Slide 6. The baseline number. Two lines. 3 seconds.

Spoken narrative: "Here is where we started. 9.2 minutes — median time for a claims intake at the organizations we work with. 9.2 minutes per claim. Across tens of thousands of claims per week. The math on that is brutal."

Total slide time target: 3 seconds. -->

---

# <span class="two">22<br>seconds.</span>

<!-- Speaker notes:
Slide 7. The after number. Immediate contrast with slide 6. 3 seconds.

Spoken narrative: "Here is where we end up. 22 seconds. Same claim. Same data sources. Same decision output. 22 seconds instead of 9 minutes and 12 seconds. That is a 96% reduction in decision time. Not a 20% efficiency gain. 96%."

The contrast between slide 6 and slide 7 is the Takahashi method's most powerful tool: two sequential slides that tell a before/after story in six seconds combined. The audience experiences the difference viscerally.

Total slide time target: 3 seconds. -->

---

<!-- _class: pivot -->

# Why?

<!-- Speaker notes:
Slide 8. Black pivot. "Why?" — a rare question in the Takahashi method. 2 seconds.

Spoken narrative: "Why is it 22 seconds? Not because we have faster hardware. Because we changed what the system is doing. A human reviewer retrieves data sequentially — opens CRM, opens eligibility, opens EHR, opens claims system. One at a time. An agent queries all four systems simultaneously. The bottleneck is not thinking time. It is lookup time. We eliminated the lookup."

Total slide time target: 2 seconds. -->

---

# Parallel.

<!-- Speaker notes:
Slide 9. The answer to "Why?" — "Parallel." 2 seconds.

Spoken narrative: "Parallel. That is the word. The agent does not wait. It sends four queries simultaneously, receives four responses simultaneously, and reasons on the combined context. No switching. No waiting. No one system blocking the next."

Total slide time target: 2 seconds. -->

---

# <span class="three">No human<br>in the loop.</span>

<!-- Speaker notes:
Slide 10. Three-word phrase at smaller size. 4 seconds.

Spoken narrative: "For routine decisions — the 80% of claims that are standard — there is no human in the loop between trigger and output. The agent receives the claim, queries the systems, applies the rules, generates the decision, and writes the output. Start to finish. 22 seconds. The human reviews the output, confirms it, and moves on. The human is a quality check, not a bottleneck."

This slide is longer than the others because "no human in the loop" is a statement that requires immediate context. Do not advance until you have given the audience the qualification.

Total slide time target: 4 seconds. -->

---

<!-- _class: pivot -->

# $340M.

<!-- Speaker notes:
Slide 11. Black pivot. The leakage number. 3 seconds.

Spoken narrative: "What is the cost of not having those 22 seconds? $340 million. That is the annual leakage estimate for a health plan the size of the ones we work with. Money paid out on claims that should have been flagged, reviewed, or denied. Walking out the door. Every year."

Total slide time target: 3 seconds. -->

---

# Invisible.

<!-- Speaker notes:
Slide 12. White. "Invisible." 2 seconds.

Spoken narrative: "The leakage is invisible in a manual workflow. The reviewer checks the primary code — it is correct. They approve. The secondary code with the inflated modifier passes through unexamined. Not because the reviewer is bad at their job. Because no human, reviewing 52 claims per shift, can cross-reference every secondary code against 4 million historical claims to find the anomaly."

Total slide time target: 2 seconds. -->

---

# <span class="two">94%<br>accuracy.</span>

<!-- Speaker notes:
Slide 13. The detection number. 3 seconds.

Spoken narrative: "The model detects secondary code anomalies with 94% accuracy. Measured across 48,000 pilot claims. Not trained on — tested on. New claims the model had never seen. 94%."

Total slide time target: 3 seconds. -->

---

# <span class="two">$230M<br>recovered.</span>

<!-- Speaker notes:
Slide 14. The recovery number. 3 seconds.

Spoken narrative: "$230 million recoverable in year one. At 94% detection accuracy. Conservative. Does not include the model improvement that happens during the calibration phase. Does not include the downstream reduction in appeals as first-pass accuracy improves."

Total slide time target: 3 seconds. -->

---

<!-- _class: pivot -->

# 273x.

<!-- Speaker notes:
Slide 15. Black pivot. The ROI number. 3 seconds.

Spoken narrative: "The implementation cost is $840,000 for phases one and two. $230 million recovered. That is 273 times the implementation cost. In year one. Without model improvement. That number gets better every year."

Total slide time target: 3 seconds. -->

---

# 30 days.

<!-- Speaker notes:
Slide 16. White. "30 days." 2 seconds.

Spoken narrative: "Time from contract signature to first production decision: 30 days. We have done it in 18. We have never taken more than 32. The median is 28. No 18-month implementation program. No custom development. 30 days."

Total slide time target: 2 seconds. -->

---

# <span class="three">You own<br>the model.</span>

<!-- Speaker notes:
Slide 17. Three-word phrase. 4 seconds.

Spoken narrative: "One concern I hear in every conversation: what if you go away? Here is the answer: you own the model. The model trains inside your cloud environment. The weights, the architecture, the fine-tuning data — all of it is in your tenant. If SponAItech disappeared tomorrow, your model continues running. We do not host anything you depend on."

Total slide time target: 4 seconds. -->

---

<!-- _class: pivot -->

# Decide.

<!-- Speaker notes:
Slide 18. Black pivot. The call to action word. 3 seconds.

Spoken narrative: "Decide. That is the call to action. Not 'consider.' Not 'explore.' Decide. Because every day between now and a signed contract is $940,000 in unrecovered leakage. The math does not wait for the decision. The decision has a cost."

Total slide time target: 3 seconds. -->

---

# Today.

<!-- Speaker notes:
Slide 19. White. "Today." — the time pressure.

Spoken narrative: "Today. We have capacity for three new implementation starts before end of quarter. Each one gets dedicated calibration resources, dedicated change management support, and a dedicated ROI guarantee: if you do not hit the projected recovery in 12 months, we extend at no cost until you do."

Total slide time target: 2 seconds. -->

---

<!-- _class: pivot -->

# <span class="three">Thank<br>you.</span>

<!-- Speaker notes:
Slide 20. Black. Final slide. The closing. 3 seconds then ambient.

"Thank you."

In the Takahashi method, the closing is the simplest slide — two words, black background, white text, the same giant scale as every other slide. No company name here. No website. No contact information. Those go on a leave-behind.

The final image the audience sees is "Thank you." in white on black. Large. Unmissable.

Leave on screen for Q&A or conversation. The black background makes the room feel like a theatre has gone dark — the show is over, but you are still here.

Total slide time target: 3 seconds, then ambient. -->
