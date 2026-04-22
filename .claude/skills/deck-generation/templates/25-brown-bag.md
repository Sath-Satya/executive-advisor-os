<!-- TEMPLATE: brown-bag
     CATEGORY: Technical
     USE WHEN: running an internal team knowledge-sharing session over lunch
     SLIDE COUNT: 8
     PALETTE: Clean light dev
     RENDER: marp --pptx 25-brown-bag.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'DM Sans', 'Segoe UI', system-ui, sans-serif;
    background: #ffffff;
    color: #1c1a18;
    padding: 48px 60px;
  }
  h1 {
    font-family: 'DM Mono', 'Cascadia Code', monospace;
    color: #0e1b2e;
    letter-spacing: -0.3px;
    font-size: 1.75em;
    border-bottom: 2px solid #e8edf2;
    padding-bottom: 12px;
    margin-bottom: 22px;
  }
  h2 { color: #3b9eff; font-size: 1.2em; margin-top: 0; }
  h3 { color: #8899ac; font-size: 0.9em; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; }
  p, li { color: #2c3340; line-height: 1.65; }
  strong { color: #0e1b2e; }
  em { color: #3b9eff; font-style: normal; font-weight: 600; }
  code {
    font-family: 'DM Mono', 'Cascadia Code', monospace;
    background: #f0f4f8;
    padding: 2px 6px;
    border-radius: 3px;
    color: #5a4fcf;
    font-size: 0.9em;
    border: 1px solid #dde3ea;
  }
  pre {
    background: #f0f4f8;
    padding: 16px 20px;
    border-left: 3px solid #3b9eff;
    border-radius: 0 4px 4px 0;
    border: 1px solid #dde3ea;
  }
  pre code { background: transparent; padding: 0; color: #1c1a18; border: none; font-size: 0.9em; }
  table { width: 100%; border-collapse: collapse; font-size: 0.9em; }
  th { background: #f0f4f8; color: #0e1b2e; padding: 10px 14px; text-align: left; border-bottom: 2px solid #dde3ea; font-family: 'DM Mono', monospace; }
  td { padding: 9px 14px; border-bottom: 1px solid #e8edf2; color: #2c3340; }
  tr:nth-child(even) td { background: #f7fafc; }
  blockquote { border-left: 3px solid #3b9eff; padding: 8px 16px; background: #f0f4f8; margin: 16px 0; border-radius: 0 4px 4px 0; }
  blockquote p { color: #0e1b2e; margin: 0; font-style: italic; }
  section.title { justify-content: center; background: #0e1b2e; }
  section.title h1 { color: #ffffff; border-bottom-color: #1a2e48; font-size: 2.2em; }
  section.title h2 { color: #3b9eff; font-size: 1.1em; }
  section.title p { color: #8899ac; font-size: 0.9em; }
---
<!-- _class: title -->

# [Topic Name]
## What It Is, Why It Matters, and When to Use It

[Presenter Name] · [Team] · [Date]
_Brown bag — 40 min including Q&A_

<!-- SPEAKER NOTES — Slide 1: Title
Brown bags are informal — you can open with a question to gauge the room ("How many of you have heard of X?"). The 40-minute format typically means 25 minutes of content and 15 minutes of Q&A. If your topic is unfamiliar to most of the room, budget more time for concept intro. If most people have context, you can spend more time on pitfalls and when-to-use. State the norms: "I will stop for questions at any time — this is a conversation, not a lecture." Set up the room informally: people eating lunch should feel comfortable, not like they are in a formal presentation. Keep the energy light.
-->

---

# 1 — Topic Overview

## What Are We Talking About?

[Topic Name] is **[one-sentence definition that a non-expert can follow]**.

**Core idea in three points:**
- [First principle — what problem does it solve?]
- [Second principle — how does it work at a high level?]
- [Third principle — what makes it different from the obvious alternative?]

**Analogies that work:**
- [Analogy 1 — relates to something the team already knows]
- [Analogy 2 — everyday-world comparison]

> "[A memorable one-line summary that your audience can repeat to a colleague]"

<!-- SPEAKER NOTES — Slide 2: Topic Overview
The one-sentence definition is the hardest sentence to write for a brown bag. Test it on someone outside the team before presenting — if they can repeat it back, it works. The three core points should be genuinely distinct — avoid restating the same idea three ways. The analogies section is important for mixed-experience rooms: pick analogies based on the lowest-context person you expect to attend. The pull-quote should be memorable enough that people repeat it in conversations later — that is the brown bag's primary value, spreading ideas peer-to-peer after the session.
-->

---

# 2 — Why It Matters to Us

## Connection to Our Work

**Where we encounter this today (whether we know it or not):**
- [Scenario 1 — specific example from current codebase or workflow]
- [Scenario 2 — place where not knowing this has caused a problem]
- [Scenario 3 — upcoming project or feature where this will matter]

**Without understanding [topic]:**
- We build workarounds that are slower and harder to maintain
- We miss opportunities to use existing platform capabilities
- We reinvent solutions the ecosystem already provides

<!-- SPEAKER NOTES — Slide 3: Why It Matters
This slide is the most important for engagement. Connecting the topic to something the team actually works on converts abstract knowledge into immediately applicable skills. Be specific — "this is exactly what we did in [project name] when we ran into [problem]" is more powerful than a generic example. If you have a war story about not knowing this topic and paying for it, this is where to tell it. Keep the "without understanding" bullets neutral — this is not criticism of past decisions, it is framing for why the knowledge is valuable going forward.
-->

---

# 3 — Core Concepts

## The Mental Model

```
[Visual representation — ASCII diagram, state machine, or flow]

Example:
[Input] → [Transform A] → [Transform B] → [Output]
               ↑ config            ↑ config
```

**Key terms (use these consistently):**

| Term | Definition | Common Misuse |
|---|---|---|
| [Term 1] | [precise definition] | [how people misuse or confuse it] |
| [Term 2] | [precise definition] | [common synonym that means something different] |
| [Term 3] | [precise definition] | [anti-pattern it is often confused with] |

<!-- SPEAKER NOTES — Slide 4: Core Concepts
The mental model diagram is worth more than a paragraph of text. Spend time on it — even a simple ASCII diagram anchors the concept visually. The terminology table is particularly valuable: it establishes shared vocabulary that prevents miscommunication in code reviews and design discussions. If "Term 2" is a word that has different meanings in different contexts (e.g., "stream" means something different in Java, Kafka, and Unix), call that out explicitly. This slide often generates the most questions — build in extra time or be prepared to go deeper here.
-->

---

# 4 — Hands-On Example

## What It Looks Like in Practice

**Scenario:** [Brief, realistic scenario from our domain]

```python
# Before — common pattern without [topic]
[show the naive or typical approach]
[3-5 lines of code]

# After — applying [topic]
[show the improved approach]
[3-5 lines of code]
```

**What changed:**
- [Change 1 — what it does differently and why that matters]
- [Change 2 — the trade-off accepted]

<!-- SPEAKER NOTES — Slide 5: Hands-On Example
The before/after code structure is the single most effective learning format for engineers. Keep both versions short — 5 lines each maximum. If the real-world example requires more context, extract the essential pattern and note that the full example is in the linked repo. The "what changed" bullets should explicitly name the trade-off accepted — no technique is free, and acknowledging the trade-off builds credibility. If you have a live demo or a REPL link, this is the slide to switch to it. Live demos in brown bags are usually appreciated — the informal setting makes failures funny rather than embarrassing.
-->

---

# 5 — Pitfalls

## What to Watch Out For

**Pitfall 1 — [Name]**
[Description of the mistake and how it manifests]
→ Fix: [specific remediation]

**Pitfall 2 — [Name]**
[Description of the mistake and how it manifests]
→ Fix: [specific remediation]

**Pitfall 3 — [Name]**
[Description of the mistake — the "obvious" approach that fails at scale]
→ Fix: [specific remediation]

> Rule of thumb: "[A memorable heuristic that prevents the most common mistake]"

<!-- SPEAKER NOTES — Slide 6: Pitfalls
Pitfalls are often the most valuable part of a brown bag because they capture hard-won knowledge that is not in the documentation. Try to have at least one pitfall from personal experience — "I did this once and here is what happened" is more memorable than abstract warnings. The rule of thumb at the bottom should be short enough to put in a comment or a code review response. If any of these pitfalls has caused a real incident on the team, say so (without blaming individuals) — it contextualizes the severity of the warning.
-->

---

# 6 — When to Use It

## Decision Guide

**Use [topic] when:**
- ✓ [Condition 1 — clearest positive signal]
- ✓ [Condition 2 — secondary positive signal]
- ✓ [Condition 3 — scale or complexity threshold]

**Do NOT use [topic] when:**
- ✗ [Condition 1 — simpler alternative exists and is sufficient]
- ✗ [Condition 2 — operational overhead not justified by use case]
- ✗ [Condition 3 — team does not yet have the required prerequisite knowledge]

**The simplest heuristic:** [One sentence decision rule — easier to remember than a full decision tree]

<!-- SPEAKER NOTES — Slide 7: When to Use It
This slide prevents over-engineering, which is the most common failure mode after a brown bag. People learn a new tool and immediately want to apply it everywhere. The "do not use" conditions are as important as the "use" conditions. The simplest heuristic at the bottom should be the answer to "should I use this?" for 80% of cases. If someone asks "what about [edge case]?", the answer is often "that falls into the operator judgment zone — start with the heuristic and escalate to a design review if the tradeoffs are unclear."
-->

---

# 7 — Q&A Prompts

## Let's Discuss

**Seed questions to get the conversation started:**
- "Have you encountered a problem this week that [topic] might have helped with?"
- "What would need to be true for us to adopt this in [Project X]?"
- "What's the biggest risk you see in applying this on our team?"

**Further reading if you want to go deeper:**
- [Authoritative doc/RFC/paper — primary source]
- [Best practical tutorial — what to do next Monday]
- [Real-world case study — company blog post or conference talk]

**Repo / demo:** `[link]`

<!-- SPEAKER NOTES — Slide 8: Q&A Prompts (final)
Seed questions are critical for getting Q&A started in a room that is eating lunch — people are less likely to raise hands when their hands are occupied. Pick the seed question that is most likely to generate useful discussion given what you know about the team. The "what would need to be true for us to adopt this" question is particularly productive — it surfaces real adoption blockers that you can address in follow-up. The three reading levels (authoritative, practical, case study) serve different learners. The "what to do next Monday" tutorial reference is the most valuable for engineers who want to act immediately. End the session by asking if anyone wants to pair on applying this to a real task in the next sprint — direct application cements learning.
-->
