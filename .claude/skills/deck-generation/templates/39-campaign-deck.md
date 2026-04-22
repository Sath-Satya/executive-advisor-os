<!-- TEMPLATE: campaign-deck
     CATEGORY: Marketing / Campaign
     USE WHEN: pitching a marketing campaign concept to internal stakeholders or clients
     SLIDE COUNT: 11
     PALETTE: Bold creative (white bg, purple + mint accent)
     RENDER: marp --pptx 39-campaign-deck.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;700&family=DM+Serif+Display&family=DM+Mono&display=swap');
  section {
    font-family: 'DM Sans', system-ui, sans-serif;
    background: #ffffff;
    color: #1c1a18;
    padding: 52px 64px;
  }
  h1 {
    font-family: 'DM Serif Display', serif;
    color: #0e1b2e;
    font-size: 2.2em;
    letter-spacing: -0.5px;
    margin-bottom: 0.2em;
  }
  h2 { color: #0e1b2e; font-size: 1.35em; font-weight: 700; margin-bottom: 0.5em; }
  h3 { color: #a78bfa; font-size: 1.0em; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 0.4em; }
  strong { color: #0e1b2e; }
  em { color: #556677; font-style: normal; font-size: 0.87em; }
  ul { margin-top: 0.5em; }
  li { margin-bottom: 0.4em; line-height: 1.6; }
  footer { font-family: 'DM Mono', monospace; font-size: 0.72em; color: #8899ac; }
  section.lead {
    background: #0e1b2e;
    color: #d0d8e4;
  }
  section.lead h1 { font-size: 2.8em; color: #ffffff; }
  section.lead h2 { color: #a78bfa; }
  section.lead p { font-size: 1.1em; color: #8899ac; margin-top: 0.4em; }
  section.big-idea { background: #f5f0ff; border-left: 6px solid #a78bfa; }
  section.channel { border-top: 4px solid #2dd4a0; }
  section.ask { background: #0e1b2e; color: #d0d8e4; }
  section.ask h2 { color: #2dd4a0; }
  section.ask strong { color: #ffffff; }
  .insight-box { background: #f5f0ff; border-left: 4px solid #a78bfa; border-radius: 4px; padding: 0.8em 1.2em; margin-top: 0.7em; font-size: 0.97em; line-height: 1.7; }
  .stat { font-family: 'DM Serif Display', serif; font-size: 2.8em; color: #a78bfa; line-height: 1.1; }
  .stat-label { font-size: 0.85em; color: #556677; margin-top: 0.1em; }
  .channel-row { display: flex; gap: 1.2em; margin-top: 0.8em; }
  .channel-card { flex: 1; background: #f8fff9; border: 1.5px solid #2dd4a0; border-radius: 6px; padding: 0.8em 1em; }
  .channel-card strong { font-size: 0.95em; }
  .channel-card em { display: block; margin-top: 0.3em; font-size: 0.82em; color: #556677; }
  .budget-row { display: flex; gap: 1.4em; margin-top: 0.8em; }
  .budget-item { flex: 1; background: #f5f0ff; border-radius: 4px; padding: 0.7em 1em; text-align: center; }
  .budget-item strong { display: block; font-family: 'DM Serif Display', serif; font-size: 1.6em; color: #a78bfa; }
  .budget-item em { font-size: 0.78em; color: #556677; }
---

<!-- _class: lead -->

# The Expert Next Door Campaign

**SponAItech** &nbsp;|&nbsp; Q3 2025 Brand Awareness Campaign

*Presented to: Internal Marketing Review · April 2025*

<!--
SPEAKER NOTES — SLIDE 1 (Title)
"The Expert Next Door" is the campaign concept for SponAItech's Q3 2025 brand awareness push. The name captures the core positioning tension: SponAItech delivers enterprise-grade AI consulting with the accessibility and speed of a local expert who actually understands your business.

This deck is an internal pitch to the marketing review committee. It is not a client-facing document. The tone is direct and confident — the team reviewing this knows SponAItech's positioning and does not need the background context that an external audience would.

The campaign targets mid-market healthcare and Salesforce-heavy organizations — the SponAItech ICP. It runs on three channels: LinkedIn thought leadership, targeted email, and partner-sourced referrals. Total Q3 budget request: $14,500.

What this deck needs to accomplish: the committee should leave this meeting with a clear go/no-go on the campaign concept, a decision on the three channel mix, and approval of the budget allocation. The campaign launches July 1 if approved today.
-->

---

## Context — Where We Are Today

**Current brand awareness status:**

- Inbound leads: 3–5 per month (primarily referrals)
- Website traffic: 420 unique visitors/month, conversion rate 1.4%
- LinkedIn followers: 312
- Share of voice in "AI consulting mid-market": effectively zero

**The problem:** SponAItech does excellent work for clients but is largely invisible to prospects who are not already in the network.

*Referral networks are not scalable. Brand awareness is.*

<!--
SPEAKER NOTES — SLIDE 2 (Context)
Deliver this slide quickly and without apology. The numbers are what they are — SponAItech is a young brand with strong client outcomes and weak market visibility. This is not a failure; it is a stage. The campaign is the inflection point.

The referral network observation: 100% of current clients came through referrals. This is both a strength (trusted relationships, high-quality clients) and a vulnerability (zero pipeline if referral activity slows). The Q3 campaign begins the transition from a purely referral-dependent model to a brand-aware model.

The "effectively zero" share of voice statement is honest. SponAItech is not yet competing for mindshare against Deloitte Digital, Slalom, or even boutique Salesforce consultancies. The goal of the Q3 campaign is not to win share of voice — it is to establish a presence that the ICP can find and recognize.

The conversion rate context: 1.4% website conversion is below the B2B services benchmark of 2.3% (Unbounce, 2024). Part of the campaign investment goes to conversion rate optimization on the landing page — which is a cost-effective lever before increasing traffic spend.
-->

---

## Audience — Who We Are Talking To

**Primary:** VP/Director of IT at mid-market healthcare organizations (500–2,500 employees)

**Secondary:** Salesforce Admins and Architects who influence vendor decisions at the same organizations

**What keeps them up at night:**
- AI pilots that fail to reach production
- Salesforce technical debt that slows every initiative
- Budget pressure to do more with smaller teams

**How they find vendors:** peer recommendations → LinkedIn thought leadership → Google search

<!--
SPEAKER NOTES — SLIDE 3 (Audience)
The audience definition here is tighter than a typical awareness campaign. This is intentional — SponAItech's TAM is small enough that mass-market awareness spend is wasted. Every dollar should reach someone who could become a client within 18 months.

The secondary audience (Salesforce admins and architects) is strategically important. These are the people who recommend vendors to the primary audience. A VP of IT who trusts their Salesforce architect will listen when the architect says "I have been following this SponAItech team and they are excellent." The LinkedIn thought leadership channel is specifically designed to reach this secondary audience.

The three "keeps them up at night" points are direct from the SponAItech ICP document. They are also validated by the SponAItech team's own 24 years of enterprise experience — these are real concerns, not marketing constructs.

The discovery sequence (peer → LinkedIn → Google) is the decision journey for this audience. The campaign is designed to be present at the LinkedIn and Google stages — referrals happen organically. Thought leadership content on LinkedIn reaches them at the "I have seen this brand before" stage and Google search catches them when they are actively evaluating.
-->

---

## Insight — The Brief That Drives It All

<div class="insight-box">

Mid-market organizations do not lack access to AI technology. They lack access to someone who has worked inside their type of organization, understands their constraints, and will still be accountable for the result six months after the contract ends.

They do not need a bigger consultant. They need the right expert.

</div>

**Strategic implication:** SponAItech's 24-year enterprise pedigree is not a credential — it is a competitive moat that no AI-only startup can replicate.

<!--
SPEAKER NOTES — SLIDE 4 (Insight)
This is the pivot point of the deck — the strategic insight that the campaign concept is built on. Spend extra time here.

The insight reframes the competitive landscape. The threat to SponAItech is not from other consultancies — it is from the prospect's assumption that AI consulting is a commodity. "Any firm with a Claude API key can do what you do." The campaign must refute this assumption — and the refutation is the 24-year enterprise pedigree.

The strategic implication at the bottom: the pedigree is a moat because it cannot be faked and cannot be fast-followed. An AI startup founded last year cannot credibly claim healthcare domain expertise. A Salesforce boutique without AI-native development cannot claim AI-first delivery speed. SponAItech's combination is genuinely rare.

The campaign must make this combination tangible. "Enterprise experience, startup speed" is the tagline — but the campaign should show it, not just say it. The LinkedIn content strategy (Slide 7) is where this plays out: real case studies, real metrics, real decision context. Not general claims.

Take questions after this slide before moving to the campaign concept. If the committee does not believe the insight, the campaign will not land internally — and it will not land with prospects.
-->

---

<!-- _class: big-idea -->

## Big Idea — "The Expert Next Door"

SponAItech is the AI consulting firm that operates like a trusted colleague inside your organization — not like a vendor who presents slides and disappears.

**Campaign voice:** First-person, direct, evidence-based. No buzz. No jargon.

**Campaign proof points:**
- ● 24 years of enterprise IT — inside healthcare, inside Salesforce
- ● AI-native development from day one — not bolt-on
- ● Production results — we measure success by what ships, not what is proposed

*The competitor is the impression that AI consulting is abstract and risky*

<!--
SPEAKER NOTES — SLIDE 5 (Big Idea)
The big idea is the emotional center of the campaign. "The Expert Next Door" works because it resolves the tension the audience feels: they want AI expertise, but they do not want to feel managed by an outsider who does not understand their world.

Campaign voice discipline: the voice rules ("first-person, direct, evidence-based, no buzz") must be enforced across every piece of content produced for this campaign. The fastest way to undermine a thought leadership campaign is inconsistency — a LinkedIn post that uses "paradigm-shifting" next to an email that says "we build things that ship" confuses the audience.

The three proof points are the campaign's credentials: 24 years (longevity and depth), AI-native (modernity and capability), production results (accountability). These three together address the primary audience's three fears: "Will they understand my world?" "Are they technically current?" "Will they still be accountable after the kickoff?"

The last line — "the competitor is the impression that AI consulting is abstract and risky" — is a category insight, not a competitor analysis. SponAItech is not trying to win business away from a specific competitor. It is trying to change a potential client's belief that AI consulting is inherently risky for mid-market organizations.
-->

---

<!-- _class: channel -->

## Channel 1 — LinkedIn Thought Leadership

**Format:** Long-form posts (800–1,200 words) + short-form commentary (150–300 words)

**Cadence:** 3 posts per week — Monday (case study), Wednesday (insight), Friday (quick take)

**Content themes:**
- Healthcare IT: what AI actually does for claims, enrollment, and member engagement
- Salesforce: technical decisions that age well vs. decisions that create debt
- AI development: what "production-ready" actually means vs. what vendors promise

**Target KPIs:** 500 new followers · 15,000 impressions/week · 2% engagement rate by September 30

<!--
SPEAKER NOTES — SLIDE 6 (Channel 1 — LinkedIn)
LinkedIn is the primary channel because the primary audience (VP/Director IT at mid-market healthcare) and secondary audience (Salesforce admins and architects) are both active on LinkedIn for professional content. Twitter/X has declined for B2B professional audiences. Medium and Substack require too much friction.

The three-times-per-week cadence is aggressive for a solo practitioner. Be honest about this in the committee: the Monday case study post will require 2–3 hours of writing and editing per week. The Wednesday insight is typically 1 hour. The Friday quick take is 30 minutes. Total: 3.5–4.5 hours of content creation per week. This is the primary cost of the campaign — not dollars, but founder time.

Content pillar rationale: the three themes map directly to the three proof points in the Big Idea slide. Healthcare IT content demonstrates domain expertise. Salesforce technical content demonstrates technical depth. AI development content demonstrates AI-native capability. Every post should be attributable to one of the three pillars.

The KPIs: 500 new followers is achievable if content reaches above-average engagement. LinkedIn's algorithm amplifies posts with high early engagement — the first 60 minutes after posting are critical. The founder should be available to respond to comments immediately after each post goes live.
-->

---

<!-- _class: channel -->

## Channel 2 — Targeted Email Outreach

**Target list:** 150 curated contacts — VP/Director IT at healthcare organizations, built from LinkedIn, conference attendee lists, and public directories

**Sequence:** 3-email nurture sequence over 3 weeks
- Email 1: Value-first — one insight relevant to their specific role
- Email 2: Case study — relevant client outcome (anonymized as needed)
- Email 3: CTA — 20-minute strategy conversation, no commitment

**Tools:** Apollo.io (contact enrichment) · Instantly.ai (sequencing) · SponAItech domain (not a personal address)

**Target KPIs:** 35% open rate · 8% reply rate · 5 booked strategy conversations

<!--
SPEAKER NOTES — SLIDE 7 (Channel 2 — Email)
The 150-contact list is deliberately small. Mass cold email to a poorly targeted list produces low response rates, damages domain reputation, and trains the audience to ignore SponAItech. 150 highly targeted, highly personalized contacts produces better results.

The value-first email structure: Email 1 should lead with something specific to the recipient's situation — not "I saw you are in healthcare" but "I saw your team is expanding your Salesforce implementation to include member self-service — here is one decision that every team I work with wishes they had made differently at that stage." This specificity requires research per contact (approximately 10 minutes per contact for the 150-contact list — total: 25 hours of list research).

The anonymized case study: the team must confirm with each client whether they can be named in external communications before the campaign launches. If clients cannot be named, the case studies should describe the situation specifically enough to be credible without being identifiable.

The domain reputation note: all campaign emails send from a dedicated campaign subdomain (campaign@sponaitech.com or outreach@sponaitech.com) — not the primary domain. This protects the primary domain's reputation if the campaign's spam rate exceeds thresholds.

5 booked strategy conversations from 150 contacts is a 3.3% conversion rate — above the cold outreach industry average of 1–2% and achievable with high-quality targeting and personalization.
-->

---

<!-- _class: channel -->

## Channel 3 — Partner Referral Activation

**Partner types:**
- Salesforce ISV partners who do not do services (they build tools, we implement)
- Healthcare IT advisory firms without Salesforce depth
- Accounting/CFO advisory firms with healthcare clients

**Activation approach:**
- Identify 10 target partners via LinkedIn and Salesforce AppExchange
- Outreach and 1:1 meeting to establish referral relationship
- Provide partners with a one-page SponAItech capability brief for their files

**Structure:** Referral fee (5–10% of first-year contract value) for qualified, closed referrals

**Target KPIs:** 5 active referral partnerships · 2 qualified referrals in Q3

<!--
SPEAKER NOTES — SLIDE 8 (Channel 3 — Partner Referrals)
Partner referrals are the highest-value channel per dollar because they carry third-party trust. A partner who says "you should talk to SponAItech" to their client is a stronger signal than any amount of content marketing.

The three partner types were chosen based on complementarity: ISV partners have tool-building depth but no implementation capacity. Healthcare advisory firms have domain relationships but no technical depth. CFO advisors are positioned inside client organizations during budget conversations — they are present when a client is deciding whether to spend on IT modernization.

The 1:1 meeting approach: the goal of the first partner meeting is not to pitch SponAItech — it is to understand the partner's client base and identify two or three specific scenarios where a referral would be appropriate. "When your clients ask you for someone who can implement Claims AI on Salesforce, we want to be the team you think of first."

Referral fee structure: the 5–10% range is standard for professional services referrals. For a $150K engagement, a 7% referral fee is $10,500 — well within the cost of acquisition for a 14-month client relationship. Define the fee structure in a simple written referral agreement before any referrals are made.

The 2 qualified referrals target is conservative. If even one referral converts to a client, the partner channel will have paid for itself many times over.
-->

---

## Timeline — Q3 2025

| Month | Activity |
|---|---|
| **May (prep)** | Finalize contact list · Draft content calendar · Establish partner outreach list |
| **June (pre-launch)** | Write 8 LinkedIn posts · Set up email sequences · Meet with 3 partner prospects |
| **July 1** | Campaign launch — all three channels active |
| **August** | Mid-campaign review — adjust based on KPI performance · Establish 2+ partner relationships |
| **September** | Campaign close · Measure final KPIs · Plan Q4 continuation or pivot |

*Review dates: July 15 (4-week check) · August 15 (8-week check) · September 30 (close)*

<!--
SPEAKER NOTES — SLIDE 9 (Timeline)
The May and June prep months are not optional. Launching a content campaign without 4–6 weeks of content pre-written is a common failure mode — the first week of content is strong, then quality declines as the creation cadence collides with client work.

The pre-launch content bank: by June 30, the content bank should contain: 8 LinkedIn posts (4 case studies, 2 insights, 2 quick takes), 3 email templates (the nurture sequence), and 1 partner capability brief. This content bank gives the campaign a 3-week runway before new content must be created.

The July 15 four-week check: this is a performance gate. If LinkedIn engagement rate is below 1% at four weeks, the content strategy needs to be adjusted before the mid-point. If email open rates are below 25%, deliverability is an issue — investigate domain reputation immediately.

The September close is a real close, not a slide. After September 30, the committee should review: total investment, qualified leads generated, and pipeline influenced. Based on those results, decide whether to continue the campaign in Q4 (likely with a modified channel mix) or redirect the budget.

Campaign ownership: name the owner before the meeting ends. Without a named owner, campaign tasks will fall between contributors. The owner is responsible for the weekly content calendar, the email sequence management, and the partner outreach tracking.
-->

---

## Budget — Q3 Campaign

<div class="budget-row">
  <div class="budget-item">
    <strong>$4,200</strong>
    <em>LinkedIn content production (12 posts × $350 copywriting/editing)</em>
  </div>
  <div class="budget-item">
    <strong>$2,800</strong>
    <em>Email tools (Apollo $150/mo + Instantly $120/mo) + contact list research</em>
  </div>
  <div class="budget-item">
    <strong>$3,500</strong>
    <em>Landing page redesign and CRO (one-time)</em>
  </div>
  <div class="budget-item">
    <strong>$4,000</strong>
    <em>LinkedIn paid amplification (2 best posts × $2,000 promotion budget)</em>
  </div>
</div>

**Total Q3 request: $14,500**

*Target return: 2+ qualified leads → 1 closed client → estimated $120–180K first-year contract value*

<!--
SPEAKER NOTES — SLIDE 10 (Budget)
The $14,500 budget is mid-range for a Q3 brand awareness campaign at SponAItech's scale. The ROI frame at the bottom is how the committee should evaluate the budget: if the campaign generates 2 qualified leads and 1 closes, the campaign pays back 8–12× in Year 1.

Budget breakdown rationale:
- LinkedIn content production: $350 per post assumes a professional copywriter or significant founder time. If the founder writes everything, this budget can be redirected to design.
- Email tools: Apollo and Instantly are industry-standard tools for B2B outreach. The contact list research cost is internal time — approximately 25 hours at an imputed rate.
- Landing page redesign: this is a one-time investment with residual value beyond Q3. The current landing page converts at 1.4% — a redesign targeting 2.5% conversion would add approximately 4–5 additional inquiries per month on current traffic.
- LinkedIn paid amplification: $2,000 per promoted post is a modest LinkedIn budget. The strategy is to identify the two highest-performing organic posts (by engagement rate) and amplify those — letting organic performance predict paid performance.

The committee should be prepared to discuss: can the landing page budget be deferred to Q4? (Yes, if budget is tight.) Can LinkedIn paid amplification be scaled down? (Yes, but organic reach alone will not achieve the follower targets without it.)
-->

---

## Success Metrics — What We Are Measuring

**Awareness:**
- LinkedIn: 500+ new followers · 15,000 impressions/week by September 30
- Email: 35%+ open rate · 8%+ reply rate

**Pipeline:**
- 5+ booked strategy conversations
- 2+ qualified opportunities (prospects who have a real problem and a budget)

**Brand:**
- One published client case study (named or with client consent)
- One industry mention or LinkedIn reshare from a non-SponAItech account

**Ask:** Approve the Q3 campaign concept and $14,500 budget. Name a campaign owner today.

<!--
SPEAKER NOTES — SLIDE 11 (Ask)
End on the specific ask. The committee should know exactly what decision is needed before they leave the room.

The three-tier metric structure (Awareness, Pipeline, Brand) maps to the three phases of the buyer journey for this audience: they become aware of SponAItech (awareness metrics), they engage and consider (pipeline metrics), and they see SponAItech validated by others (brand metrics). Each tier has a different time horizon — awareness metrics show up in weeks, pipeline in months, brand in quarters.

The "brand mention" metric is intentionally qualitative. One reshare or mention from a credible third-party account (a Salesforce MVP, a healthcare IT publication, a partner firm) is worth more than 50 SponAItech-originated posts. It cannot be bought — it is earned through quality content. The metric is here to make it a priority, not to guarantee it.

The two-part ask: campaign approval and owner naming. Both are required for the campaign to launch. A campaign with budget but no owner is a campaign that does not run. The owner should be named before the committee adjourns.

If the committee wants to approve the concept but modify the budget: be prepared to show which channel is cut and what the impact on KPIs would be. The email channel ($2,800) is the lowest-cost-per-contact channel and should be the last to be cut. The LinkedIn paid amplification ($4,000) is the most discretionary.
-->
