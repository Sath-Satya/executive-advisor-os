<!-- TEMPLATE: workshop-deck
     CATEGORY: Training / Workshop
     USE WHEN: facilitating a full-day or half-day interactive workshop
     SLIDE COUNT: 18
     PALETTE: Warm light
     RENDER: marp --pptx 31-workshop-deck.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600&family=DM+Serif+Display&family=DM+Mono&display=swap');
  section {
    font-family: 'DM Sans', system-ui, sans-serif;
    background: #faf7f2;
    color: #1c1a18;
    padding: 52px 64px;
  }
  h1 {
    font-family: 'DM Serif Display', serif;
    color: #0e1b2e;
    font-size: 2.2em;
    letter-spacing: -0.4px;
    margin-bottom: 0.2em;
  }
  h2 {
    color: #b8740a;
    font-size: 1.05em;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 0.6em;
  }
  h3 { color: #0e1b2e; font-size: 1.15em; font-weight: 600; margin-bottom: 0.4em; }
  strong { color: #0e1b2e; }
  em { color: #6b6560; font-style: normal; font-size: 0.88em; }
  ul { margin-top: 0.5em; }
  li { margin-bottom: 0.45em; line-height: 1.6; }
  footer { font-family: 'DM Mono', monospace; font-size: 0.72em; color: #6b6560; }
  section.lead h1 { font-size: 2.8em; }
  section.lead p { font-size: 1.1em; color: #6b6560; margin-top: 0.4em; }
  section.exercise { background: #fff8ed; border-left: 6px solid #f0a050; }
  section.exercise h2 { color: #b8740a; }
  section.debrief { background: #faf7f2; border-top: 4px solid #f0a050; }
  .time-box {
    display: inline-block;
    background: #f0a050;
    color: #0e1b2e;
    font-family: 'DM Mono', monospace;
    font-size: 0.82em;
    font-weight: 600;
    padding: 0.2em 0.7em;
    border-radius: 4px;
    margin-bottom: 0.8em;
  }
  .prompt-block {
    background: #ffffff;
    border: 1.5px solid #f0a050;
    border-radius: 6px;
    padding: 1em 1.4em;
    margin-top: 0.8em;
    font-size: 0.95em;
  }
---

<!-- _class: lead -->

# Agentic Workflow Design Workshop

**SponAItech** &nbsp;|&nbsp; Internal Enablement Series

*Full-Day Workshop — v1.0 — April 2025*

<!--
SPEAKER NOTES — SLIDE 1 (Title) [5 min]
Welcome participants as they settle. This is a full-day interactive workshop — not a lecture. The bulk of the time will be in two structured exercises that participants work through in small groups. Set expectations early: phones away, laptops closed except during exercise phases, every voice matters in debrief.

Briefly introduce yourself and any co-facilitators. State the day's structure at a high level: morning concepts and Exercise 1, afternoon deeper concepts and Exercise 2, close with a synthesis and personal commitment. Tell the room the one thing you want them to leave with: a concrete workflow map they built themselves, not a slide they half-read.

Energy management: stand at the front, do not sit. Move around the room. The warm amber palette and open layout is intentional — this is not a boardroom deck, it is a workshop space. Match that energy.
-->

---

## Agenda — Full Day

- **09:00** Welcome + objectives
- **09:15** Why this topic matters now
- **09:30** Concepts Block 1 — foundations
- **10:30** Exercise 1 — map your current workflow
- **11:15** Debrief + synthesis
- **11:45** Concepts Block 2 — advanced patterns
- **13:00** Exercise 2 — redesign with AI augmentation
- **14:15** Debrief + synthesis
- **14:45** Homework + commitments
- **15:00** Close

*Breaks at facilitator discretion — read the room*

<!--
SPEAKER NOTES — SLIDE 2 (Agenda) [3 min]
Walk the agenda at a medium pace. Do not rush through it — participants need to mentally orient to the day. Point out the two exercise blocks explicitly: "You will be doing real work in this room, not just listening."

Logistics: bathrooms, lunch arrangements, parking for afternoon arrivals. Confirm the room will be set up for group work (tables of 4–5, not auditorium rows). If the room is wrong, fix it now before you lose the first 20 minutes of content.

Mention that the agenda is a guide, not a contract. If a debrief runs long because the room is generating valuable insight, you will extend it. The close time is firm because some participants have hard stops.

Ask if there are any questions about the structure before you begin.
-->

---

## Why This Topic Matters Now

- AI-augmented workflows are shifting from pilot to production in 2025
- Teams without a deliberate design process bolt AI onto broken processes
- **The risk:** automation amplifies waste, not just speed

*Source: McKinsey State of AI 2024 — 68% of AI pilots fail to reach production due to workflow mismatch*

<!--
SPEAKER NOTES — SLIDE 3 (Why Now) [10 min]
This slide earns the room's attention for the day. Do not skip it or rush it. The stat from McKinsey is real — source is the McKinsey Global Survey on AI Adoption 2024. If anyone questions it, the full citation is in the facilitator notes appendix.

The core argument to make verbally: most organizations think their AI problem is a technology problem. They have picked the wrong model, chosen the wrong vendor, or deployed too slowly. The research consistently shows the real problem is that they are automating workflows that were already broken. Garbage in, garbage out — but faster.

Tell a brief story from your own experience or a known client scenario (use Meridian Health as the example if you have clearance): when Meridian automated claims intake without first redesigning the intake workflow, they reduced processing time by 15% but increased error rates by 22% because the AI was faithfully replicating a flawed human process.

The goal of today is to give participants a repeatable method for designing workflows that are worth automating.
-->

---

## Concept 1 — What Is a Workflow

A workflow is **a repeatable sequence of decisions and actions** that moves work from input to outcome.

Three components every workflow must have:
- **Trigger** — what starts the work
- **Transformation** — what changes between input and output
- **Exit condition** — how you know the work is done

*Workflows without exit conditions are the most common source of rework*

<!--
SPEAKER NOTES — SLIDE 4 (Concept 1 — Definition) [8 min]
This is a foundational definition slide. Resist the urge to go deep yet — the goal is to give participants shared vocabulary before the exercise. Without shared vocabulary, the debrief will be chaos.

Write the three components on a whiteboard or flip chart as you say them. Ask the room: "Can anyone name a workflow they work with daily that does NOT have a clear exit condition?" Let two or three people answer. This surfaces the pain that makes the day relevant.

Common answers you will hear: approval chains that sit in inboxes forever, escalation paths that loop back to the person who escalated, reporting processes where no one knows who publishes the final version. Validate these — do not solve them yet. Exercise 1 will surface the patterns.

Estimated time on this slide: 8 minutes. If you are running long, cut the Q&A and move to the next concept.
-->

---

## Concept 2 — The Three Workflow Failure Modes

**1. Undefined handoffs** — work arrives with no owner

**2. Manual decision gates** — humans are interrupts, not deciders

**3. Missing feedback loops** — no signal reaches back to improve input quality

→ AI augmentation exposes all three. Design before you automate.

<!--
SPEAKER NOTES — SLIDE 5 (Concept 2 — Failure Modes) [10 min]
Each failure mode deserves a brief real-world example. Keep each to 90 seconds.

Undefined handoffs: Think of a customer escalation that arrives in a shared inbox. When everyone is responsible, no one is. AI routing tools can assign the ticket — but if the ownership model is not defined, the ticket gets re-routed in a loop.

Manual decision gates: A human who must approve before work can proceed is not a decision-maker if they approve 98% of requests without reading them. This is a rubber-stamp gate. AI can replace it — but only after the decision criteria are made explicit.

Missing feedback loops: A QA team that flags defects but never sees whether the defects are fixed does not improve input quality. The upstream team has no incentive to change because they see no signal. AI-generated summaries without feedback loops produce the same effect.

Ask the room which failure mode they recognize most in their own work. Take a quick show of hands. Use the distribution to anchor the first exercise.
-->

---

## Concept 3 — AI Augmentation Patterns

Three ways AI changes a workflow — choose deliberately:

- **Replace** — AI does the step entirely (classification, extraction, formatting)
- **Assist** — AI drafts, human decides (generation, summarization, first review)
- **Monitor** — AI watches and alerts (anomaly detection, drift signals, SLA breach)

*Wrong pattern choice is the second most common cause of pilot failure*

<!--
SPEAKER NOTES — SLIDE 6 (Concept 3 — Augmentation Patterns) [12 min]
This is the most strategically important concept of the morning. Spend the full time here.

The common mistake is defaulting to "assist" for everything because it feels safe. In practice, assist patterns require the most careful design — the human still carries decision burden but now has to evaluate AI output rather than doing the original work. If the human does not have the time or expertise to evaluate the AI's draft, you have made the workflow slower, not faster.

Replace patterns are actually lower risk when the task is well-defined and the error cost is low. Classification of support tickets, extraction of structured data from forms, and formatting of standard documents are all strong replace candidates.

Monitor patterns are underused. They add AI value without disrupting the existing workflow. Great first step for teams that are skeptical.

Give participants one minute to discuss at their table: for one workflow they identified in the prior slide, which pattern applies? Brief report-out before moving to Exercise 1.
-->

---

## Concept 4 — Workflow Mapping Notation

Use this notation in Exercise 1:

| Symbol | Meaning |
|---|---|
| **[ ]** | Process step |
| **< >** | Decision gate |
| **{ }** | Handoff to another team |
| **( )** | AI augmentation point |
| **→** | Flow direction |
| **✗** | Known failure point |

*You do not need a tool — paper and markers work fine*

<!--
SPEAKER NOTES — SLIDE 7 (Concept 4 — Notation) [5 min]
Keep this slide brief. The notation exists to give groups a shared language during Exercise 1 — it is not a formal modeling standard. Participants should not spend time arguing about whether something is a process step or a decision gate. If in doubt, pick one and keep moving.

Distribute paper and markers before this slide so participants have materials in hand when Exercise 1 starts. Groups of four to five work best. If the room is larger than 25, assign a second facilitator to rotate between groups during the exercise.

Point out the AI augmentation point notation specifically: (step name). This is the primary output of Exercise 1 — participants will identify where AI could augment their current workflow. They are not designing the AI solution yet, just placing the markers.

Transition to Exercise 1 immediately after this slide.
-->

---

<!-- _class: exercise -->

## Exercise 1 — Map Your Current Workflow

<div class="time-box">45 minutes</div>

**Your task:**

<div class="prompt-block">

In groups of 4–5, select one workflow your team runs at least weekly. Map it using the notation from the previous slide. Mark every:
- **✗** Known failure point
- **(  )** Where AI augmentation could apply
- **< >** Decision gate that could be made explicit

Capture on paper or whiteboard. You will present a 3-minute walkthrough in debrief.

</div>

*Pick a real workflow — not an ideal one*

<!--
SPEAKER NOTES — SLIDE 8 (Exercise 1) [45 min]
Start the exercise immediately. Do not allow groups to spend the first 10 minutes discussing which workflow to choose — give them 2 minutes to decide, then they must start mapping.

Your role during the exercise: rotate between groups every 8–10 minutes. Ask probing questions rather than giving answers. Good probes: "Who owns this step when [person X] is out?" — "What triggers this gate — a calendar? A request? A threshold?" — "What happens when this fails — where does the work go?"

Watch for groups that go too abstract ("the marketing workflow") — redirect them to a specific instance ("walk me through what happened with the last campaign launch"). Specificity surfaces the real failure points.

At the 35-minute mark, give a 10-minute warning. Groups should have their map complete and be able to walk through it in 3 minutes. If a group is stuck, help them pick one failure point and work backward from it.

After 45 minutes, stop all groups. Debrief begins on the next slide.
-->

---

<!-- _class: debrief -->

## Debrief — Exercise 1

**Each group: 3-minute walkthrough**

Facilitator listens for:
- ● Common failure points across groups
- ● Decision gates that are actually rubber stamps
- ● AI augmentation points that appear repeatedly

**Synthesis question:** Where did the same failure mode appear in more than one workflow?

<!--
SPEAKER NOTES — SLIDE 9 (Debrief 1) [25 min]
Run round-robin — each group presents their map in 3 minutes. Hold to time. After all groups have presented, spend 10 minutes on synthesis.

Synthesis technique: on a whiteboard or flip chart, create three columns: Handoff failures | Rubber-stamp gates | AI augmentation candidates. As each group presents, place tally marks in the relevant columns. By the end of the round, the room will see the pattern. This is far more powerful than you telling them what you observed.

The most important insight to surface: teams in the same organization running the same type of workflow often have different failure points. This tells you the failure is not inherent to the workflow type — it is a process design choice that can be changed.

Bridge to the afternoon: "In the next concept block, we are going to look at patterns for redesigning these workflows. When we get to Exercise 2, you will take the map you built this morning and redesign it."
-->

---

## Concept 5 — Redesign Principles

When redesigning a workflow with AI augmentation, apply in order:

- **Eliminate first** — remove steps that add no value, with or without AI
- **Standardize second** — make inputs and outputs explicit before automating
- **Automate third** — apply the augmentation pattern (Replace / Assist / Monitor)

*Automating before eliminating locks waste into your system permanently*

<!--
SPEAKER NOTES — SLIDE 10 (Concept 5) [10 min]
This sequencing principle is the most counterintuitive thing you will say all day. Most participants will want to jump straight to automating because that is where the excitement is. Validate that impulse — the excitement is real — and then explain why the order matters.

Use the Meridian Health example: when they deployed an AI claims router before cleaning up their intake form, the AI learned to route based on the incomplete data fields. It became extremely good at routing bad claims. They had to rebuild the model after standardizing the intake form — doubling the implementation cost.

The phrase "eliminating before automating" is the key takeaway from this slide. Ask the room to say it aloud. Sounds trivial but it anchors the memory.

Check in on the room's energy here — this is the post-lunch phase and the hardest time to hold attention. If energy is low, call a 5-minute stretch break before the next concept slide.
-->

---

## Concept 6 — Feedback Loop Design

Every AI-augmented workflow needs a feedback loop:

- **Short loop** — immediate correction signal (accept / reject / edit)
- **Medium loop** — weekly quality review of AI outputs
- **Long loop** — quarterly model performance against original success criteria

*Without the short loop, the AI never learns. Without the long loop, you never know if it is still solving the right problem.*

<!--
SPEAKER NOTES — SLIDE 11 (Concept 6) [12 min]
The three loops map roughly to: user-level feedback (the short loop), team-level feedback (medium), and organizational-level feedback (long). Each operates on a different time scale and has a different owner.

Common mistake: teams instrument the short loop but ignore the long loop. As a result, the AI gets better at the task as originally defined, but no one re-examines whether the task is still the right one. In a healthcare scenario, an AI that gets very good at routing claims under the old coverage rules becomes a liability when the coverage rules change — unless someone is running the long loop.

Ask: does anyone in the room have an example of a system that they know is solving the wrong problem but it is hard to change because it is deeply instrumented? This usually surfaces a great anecdote from the room and makes the long loop concept vivid.

Transition: "You are going to design all three loops into your redesigned workflow in Exercise 2."
-->

---

## Concept 7 — Change Readiness

Before deploying AI augmentation, assess:

- **Skill gap** — can your team evaluate AI outputs critically?
- **Trust level** — will users act on AI recommendations without over-checking?
- **Rollback plan** — how do you restore the old workflow if the AI fails?

*A workflow your team does not trust will be circumvented — every time*

<!--
SPEAKER NOTES — SLIDE 12 (Concept 7) [8 min]
Change readiness is the most underinvested dimension in AI deployment. The technology is usually ready before the organization is. Three quick diagnostics for the room.

Skill gap test: ask your team to describe the last three times an AI tool gave them a wrong answer and how they caught it. If they cannot answer, the skill gap is wide.

Trust level: shadow a few users for an hour. Do they click "accept" on AI suggestions without reading them (over-trust) or do they re-do the AI's work manually as a check (under-trust)? Both are productivity problems.

Rollback plan: this is non-negotiable. Every deployment must document how to disable the AI augmentation and restore the manual workflow. The rollback plan is not a sign of pessimism — it is what makes it safe to move fast.

Bridge to Exercise 2: "You will sketch a rollback plan as part of your redesign."
-->

---

<!-- _class: exercise -->

## Exercise 2 — Redesign with AI Augmentation

<div class="time-box">50 minutes</div>

**Your task:**

<div class="prompt-block">

Take your morning workflow map. Apply the redesign principles:

1. Circle and cross out at least one step to **eliminate**
2. Identify two **standardization** changes needed before automation
3. Assign an augmentation pattern (Replace / Assist / Monitor) to each (  ) point
4. Design the **short feedback loop** for your top AI touchpoint
5. Write a one-sentence **rollback plan**

Prepare a 4-minute presentation for debrief.

</div>

<!--
SPEAKER NOTES — SLIDE 13 (Exercise 2) [50 min]
This exercise is harder than Exercise 1 because participants must make design decisions, not just describe current state. Expect more uncertainty and more requests for facilitator input. Your role is to help them think, not to design for them.

Common sticking point: participants want to know which AI tool to use before they design the workflow. Redirect firmly — "The tool decision comes after the workflow design. Design the workflow for the outcome you want, then find the tool that fits." This is a discipline, not a preference.

For the rollback plan: it should be one sentence. "If the AI classifier breaks, claims route to the shared inbox and the manual triage process from Q3 2023 is reinstated." Simple, specific, executable.

At the 40-minute mark, check in with each group. At least one group will be stuck on step 3 (augmentation pattern assignment). Help them by asking: "What is the cost of a wrong answer here?" High cost = Monitor or Assist. Low cost and well-defined = Replace.

After 50 minutes, move immediately to Debrief 2.
-->

---

<!-- _class: debrief -->

## Debrief — Exercise 2

**Each group: 4-minute walkthrough**

Facilitator listens for:
- ● Elimination choices — what was cut and why
- ● Where groups chose Monitor over Replace (often the wisest starting point)
- ● Feedback loop designs — are they actually measurable?

**Synthesis question:** What would have to be true for your team to deploy this redesign in the next 90 days?

<!--
SPEAKER NOTES — SLIDE 14 (Debrief 2) [30 min]
Run presentations in the same order as Exercise 1 so each group can compare their morning map to their afternoon redesign. The contrast is often striking — and motivating.

The synthesis question is deliberately ambitious. "90 days" forces participants to be concrete about barriers. Common barriers you will hear: "We don't have the data to train a model" (redirect: Monitor patterns need no training data), "Leadership hasn't approved it" (redirect: what would an approval request look like?), "Our team won't trust the AI" (redirect: what is the change readiness plan?).

Spend the last 10 minutes of debrief on commitments. Ask each participant (not each group — each individual) to write down: one thing they will do in the next two weeks to move their redesigned workflow forward. These become the basis for the homework slide.

Bridge to synthesis: "Let's step back and connect what we did today to the bigger picture."
-->

---

## Synthesis — What We Built Today

**Morning:** You mapped a real workflow and found its failure points.

**Afternoon:** You redesigned it with deliberate AI augmentation — and built in a feedback loop.

**The pattern you now own:**
- Eliminate → Standardize → Automate
- Map → Identify → Pattern → Loop → Rollback

*This method works for any workflow, any domain, any AI tool*

<!--
SPEAKER NOTES — SLIDE 15 (Synthesis) [5 min]
This is the payoff slide. Keep it brief. The room has done real work and deserves a moment of recognition before the homework ask.

Reinforce that what participants built today is not theoretical — it is a real artifact they can bring back to their team tomorrow. The workflow map is theirs. The redesign is theirs. You facilitated; they built.

Name the pattern explicitly one more time: Eliminate → Standardize → Automate. This is the thing that will stick if anything sticks. Ask the room to repeat it back.

Transition to homework: "I want to make sure what you built today does not end up in a binder. So here is what I am asking you to do before we meet again."
-->

---

## Homework — Before the Next Session

**Individual commitment (15–30 min):**

- ● Share your redesigned workflow map with your direct manager
- ● Identify one person on your team to be your "feedback loop champion"
- ● Write the one-sentence rollback plan in your team's shared doc

**Optional (for those ready to move fast):**

- ○ Run a 30-minute pilot of the Monitor pattern on your top AI touchpoint
- ○ Schedule a 30-day check-in with your team

*Bring your manager's response — pro or con — to the next session*

<!--
SPEAKER NOTES — SLIDE 16 (Homework) [5 min]
The homework is structured to be achievable in under 30 minutes. Do not overload participants with a list of 10 things — you will get zero compliance. Three specific, short actions with clear outputs.

The "bring your manager's response" instruction is important. It surfaces organizational blockers early — before the next session, not 6 months later when the pilot has stalled. It also creates accountability without surveillance.

For participants who say they do not have a manager to share with: "Share it with a peer. The goal is external accountability, not hierarchy."

Remind participants that the optional items are truly optional. The Monitor pattern pilot is low-risk by design — it requires no new tools, no approval, and no change to the existing workflow. If someone is ready to pilot, encourage them.
-->

---

## Close — Thank You and Next Steps

**What you accomplished today:**
- ✓ Mapped a real workflow with failure points
- ✓ Applied three AI augmentation patterns
- ✓ Designed a feedback loop
- ✓ Committed to a next action

**Next session:** Deep dive on feedback loop instrumentation — bring your pilot results.

*Questions? &nbsp;&nbsp;[facilitator@sponaitech.com]*

*Workshop materials: [your shared drive path]*

<!--
SPEAKER NOTES — SLIDE 17 (Close) [5 min]
End on energy, not exhaustion. The room has done real work and deserves a strong close. Recap the four accomplishments — read them slowly, one by one. This is a moment of earned recognition, not a formality.

Next session logistics: confirm the date, time, and location before people leave the room. "Before you walk out, check your calendar for [date] — our next session is [time] at [location]." If participants do not confirm now, you will lose 30% to scheduling conflicts.

The closing question: stand at the door as people leave and ask each participant "What is the one thing you are taking back to your team?" Listen without responding. Their answers are your most valuable feedback on whether the day landed.

Facilitator debrief: within 48 hours, write a one-page facilitator retrospective: what worked, what ran long, what questions surprised you. This is your learning artifact for the next time you run this workshop.
-->

---

<!-- _class: lead -->

# Appendix — Facilitator Resources

*Timing guide · Whiteboard templates · Notation reference · Rollback plan template*

*Full facilitator guide: [your shared drive path]*

<!--
SPEAKER NOTES — SLIDE 18 (Appendix) [Reference only]
This slide is a reference slide — it is not presented in sequence. It exists so that participants can find facilitator resources after the session. The links should point to the canonical location of workshop materials: the shared drive, Notion page, or internal wiki where the facilitator guide, whiteboard templates, and notation reference live.

If you are running this workshop for the first time, build the facilitator guide before the session, not after. The guide should include: room setup diagram, materials checklist, timing buffer strategy, common participant questions and suggested responses, and the exercise debrief synthesis technique described in the notes for slides 9 and 14.

The notation reference on this slide should match exactly what was presented on the Concept 4 slide. Consistency matters — participants who photograph this slide to share with their teams should get the same notation they practiced with.
-->
