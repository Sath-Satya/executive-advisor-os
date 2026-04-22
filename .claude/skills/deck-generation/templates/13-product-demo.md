<!-- TEMPLATE: product-demo
     CATEGORY: Sales / Demo
     USE WHEN: live product demonstration to prospect, discovery call follow-up, or recorded demo
     SLIDE COUNT: 8
     PALETTE: Clean light
     RENDER: marp --pptx 13-product-demo.md -->
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
    padding: 48px 64px;
  }
  h1 {
    font-family: 'DM Serif Display', 'Georgia', serif;
    color: #1c1a18;
    letter-spacing: -0.4px;
    font-size: 2.2em;
    line-height: 1.15;
    margin-bottom: 0.3em;
  }
  h2 {
    color: #3b9eff;
    font-size: 0.9em;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 1em;
  }
  h3 {
    color: #1c1a18;
    font-size: 1.05em;
    font-weight: 700;
    margin-bottom: 0.4em;
  }
  strong { color: #3b9eff; }
  em { color: #8899ac; font-style: normal; }
  ul { list-style: none; padding: 0; }
  ul li::before { content: "• "; color: #3b9eff; }
  ul li { margin-bottom: 0.55em; font-size: 1.02em; line-height: 1.5; }
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.92em;
  }
  th {
    background: #f4f6f8;
    color: #8899ac;
    padding: 10px 16px;
    text-align: left;
    font-weight: 700;
    letter-spacing: 0.06em;
    font-size: 0.82em;
    text-transform: uppercase;
    border-bottom: 2px solid #e0e6ed;
  }
  td { padding: 10px 16px; border-bottom: 1px solid #f0f2f5; color: #1c1a18; }
  tr:last-child td { border-bottom: none; }
  .screen-placeholder {
    background: #f4f6f8;
    border: 2px dashed #d0d8e4;
    border-radius: 10px;
    padding: 32px;
    text-align: center;
    color: #8899ac;
    font-size: 0.95em;
    font-style: italic;
    margin-top: 1em;
  }
  section::after { color: #c0cad4; font-size: 0.75em; }
---

## Product Demo

# Helix — See the Workflow End to End

Welcome to Helix. In the next 20 minutes, you will see:
- How Helix connects to your EHR in under 60 seconds
- A live prior-authorization from chart to submission
- The appeals workflow — fully automated

*Demo environment: sandbox data, HIPAA-compliant*

<!-- Speaker notes:
Set expectations at the start of every demo. Tell them exactly what they are going to see and how long it will take. This removes the "are we almost done?" anxiety and primes them to look for the right things. The "20 minutes" commitment is a respect signal — you are not going to waste their time. If this is a recorded demo rather than live, replace the opening with: "You are watching a pre-recorded walkthrough of our sandbox environment. Every action you see is real product, not a mockup." Never apologize for using sandbox data — state it matter-of-factly as a security and compliance practice. If the prospect has shared sample data (de-identified), say so: "We have pre-loaded de-identified records from your team to make this relevant." Start the demo with energy — you are about to save them three hours a day.
-->

---

## The Pain We Are Solving

# Your Team Spends 3 Hours Daily on Forms — Helix Eliminates That

**Today's workflow:**
- Physician identifies procedure &nbsp;▸&nbsp; locates PA requirement &nbsp;▸&nbsp; pulls clinical notes
- Manually fills payer form &nbsp;▸&nbsp; submits via fax or portal &nbsp;▸&nbsp; waits 11 days

**After Helix:**
- Physician identifies procedure &nbsp;▸&nbsp; Helix surfaces PA status instantly
- Physician reviews AI-generated submission in 22 seconds &nbsp;▸&nbsp; approves &nbsp;▸&nbsp; done

<!-- Speaker notes:
Anchor the demo in their reality before you show anything technical. If you did a discovery call, reference what they told you: "You mentioned that your cardiology department has two full-time staff dedicated to PA. That's what we're going to eliminate today." The before/after structure is deliberate — it maps the current pain to the specific moment in the demo where it disappears. If you do not have discovery data, use the generic numbers (3 hours, 11 days, 22 seconds) — they are provocative enough to hold attention. Keep this slide under 90 seconds. The prospect came for the demo, not the setup. Use this slide only if there are skeptics in the room who need to be reminded why the problem matters. If you are demoing to a physician champion who already bought in, skip forward: "You know the pain — let's skip to the solution."
-->

---

## Demo — Connect and Configure

# Step 1 — Helix Connects to Your EHR in Under 60 Seconds

*[SCREEN: EHR integration setup — OAuth FHIR connection flow]*

- One-click FHIR R4 OAuth — no API keys, no IT tickets
- Helix requests **read-only** access to the PA-relevant data fields
- Configuration is **per department** — cardiology can be live before radiology starts

<div class="screen-placeholder">Replace with live screen share or annotated screenshot of the connection flow</div>

<!-- Speaker notes:
The integration setup is the first "wow" moment in the demo because it addresses the prospect's biggest fear: "How long will this take our IT team?" The answer is: IT does not need to be in the room. You are using a standard FHIR R4 OAuth handshake that every modern EHR supports. If the EHR is Epic, say: "Epic's App Orchard certification means Helix has already passed Epic's security review. Your Epic admin can approve this in minutes." If it is Cerner, say: "We are a Cerner SMART on FHIR partner — same process." Show the actual OAuth flow — do not just describe it. Click through it in real time. The per-department configuration point is important for enterprise prospects: "Cardiology goes live this week. Radiology follows in two weeks. You do not need to do a hospital-wide rollout to start realizing value."
-->

---

## Demo — Live Prior Authorization

# Step 2 — From Chart to Submitted in 22 Seconds

*[SCREEN: Epic chart open — Helix sidebar visible — PA trigger event]*

- Helix sidebar appears automatically when a PA-required order is placed
- Clinical notes, labs, and imaging are **pre-populated** — no copy-paste
- One-click review &nbsp;▸&nbsp; one-click submit &nbsp;▸&nbsp; confirmation with tracking number

<div class="screen-placeholder">Replace with live screen share or annotated screenshot of the 22-second PA submission flow</div>

<!-- Speaker notes:
This is the core demo moment. Slow down here. Do not rush the 22-second flow — let the prospect watch every step. Narrate what is happening in the background: "Helix is reading Dr. Johnson's note from this morning's visit. It's mapping the diagnosis code to Aetna's criteria set for MRI lumbar spine. It's found three supporting evidence elements in the chart. It's now composing the submission." Then stop. Let them read the pre-populated form on screen. Then: "The physician looks at this, sees it's complete and accurate, and clicks approve. That's the 22 seconds." Count it if you want to make it real. The emotional moment is when the confirmation number appears: "Previously, this physician would have waited 11 days to know if this submitted successfully. The confirmation is instant." Pause. Let that land. If the demo environment is slow, have a recorded backup ready.
-->

---

## Demo — Appeals Workflow

# Step 3 — Helix Fights Denials So Physicians Don't Have To

*[SCREEN: Denial notification — Helix auto-generates appeal letter — submission]*

- Denial triggers automatic **evidence package assembly**
- Helix cites patient record, clinical guidelines, and payer policy in one document
- Appeal submitted within **4 minutes** of denial &nbsp;|&nbsp; win rate: **73%**

<div class="screen-placeholder">Replace with live screen share or annotated screenshot of the auto-appeals generation flow</div>

<!-- Speaker notes:
The appeals flow is the differentiator that no competitor has fully closed. Demo it even if the prospect did not ask about it — it is the "we did not know we needed this" feature that generates the most interest. Walk through the evidence package: "Helix has found the relevant section of Aetna's clinical criteria document. It has matched it to the specific evidence in this patient's record — the ejection fraction measurement from the echocardiogram. It has pre-written the appeal letter citing all of it." Then: "The physician's assistant reviews, clicks submit. Four minutes from denial to appeal." The 73% win rate is your close signal: "We win 73% of the appeals we file. The industry average for manual appeals is 42%. The difference is that Helix never forgets a piece of evidence and never writes a weak argument." If the prospect has experienced painful denial reversals, this is where they will start asking "when can we start?"
-->

---

## Before and After — By the Numbers

| Metric | Before Helix | After Helix | Change |
|---|---|---|---|
| Time per PA submission | 14 minutes | 22 seconds | **-98%** |
| Days to approval | 11 days avg | 3 days avg | **-73%** |
| First-pass denial rate | 17% | 6% | **-65%** |
| Appeals win rate | 42% manual | 73% Helix | **+74%** |
| Staff time on PA (weekly) | 120 hours | 18 hours | **-85%** |

*Based on 11 live deployments, March 2026 data*

<!-- Speaker notes:
Numbers close deals. This table is the ROI summary that the economic buyer — CFO, VP Operations, CMO — will use to justify the purchase internally. Walk through each row but spend the most time on the last one: "120 hours to 18 hours per week. That is two full-time staff equivalents. Whether you redeploy them or reduce hiring, that is a tangible cost impact. At a fully-loaded cost of $75,000 per staff equivalent, Helix pays for itself in under 4 months." If your specific prospect has shared their current PA volume, customize this table before the demo. Replace "120 hours" with their number. Nothing is more persuasive than seeing their own data reflected back with Helix's impact applied. Always include the source footnote: "based on live deployments, current data" — it signals these are not modeled projections.
-->

---

## Pricing

# Simple, Transparent, No Surprises

| Tier | What's Included | Price |
|---|---|---|
| **Starter** | Up to 500 PA/month, 1 department, email support | $4,800/mo |
| **Growth** | Unlimited PA, 3 departments, analytics dashboard | $9,500/mo |
| **Enterprise** | Unlimited PA, all departments, dedicated CS, SLA 99.9% | Custom |

*No setup fees &nbsp;|&nbsp; No per-seat licenses &nbsp;|&nbsp; 30-day onboarding guarantee*

ROI at Growth tier: typical payback in **under 90 days**

<!-- Speaker notes:
Introduce pricing only after the prospect has seen the value — never before. The table structure is simple on purpose: three tiers, clear differentiation, no hidden complexity. The "no setup fees, no per-seat licenses" footnote addresses the two most common objections before they are raised. The 30-day onboarding guarantee is a risk reversal: "If you are not live and processing PA within 30 days of signing, we extend your first month at no charge." That guarantee has never been exercised — we have been under 30 days on every deployment. Present it as confidence, not desperation. On the Enterprise row: "For your size, we would typically quote $17K–$22K per month depending on PA volume and department count. I will send a tailored proposal today." Never make them feel like they are the first person you are quoting. Reference a comparable customer: "Mercy Health, similar size, is at $19K/month and has had 14-month payback."
-->

---

## Next Steps

# Three Things to Do Before Friday

1. **Share PA volume data** — 90-day sample &nbsp;▸&nbsp; we model your specific ROI (2 hours)
2. **Schedule IT intro call** — 30 minutes with your Epic admin to confirm FHIR access (30 min)
3. **Pilot agreement** — 60-day paid pilot at $0 risk: full refund if targets not met

**We will have a custom ROI model and pilot agreement in your inbox by tomorrow 5 PM.**

*Contact: sarah.chen@helix.health &nbsp;|&nbsp; (415) 555-0192*

<!-- Speaker notes:
The next steps slide converts the demo from a conversation into a project. Each action item is numbered, has a specific deliverable, and has a time estimate — this signals respect for their calendar. Action 1 is the most important: if they share PA volume data, you can send a customized ROI model with their numbers. That document will be circulated internally. Never leave a demo without a specific commitment: "Can you send me the PA volume report by Wednesday? Even an aggregate from your billing system works." If they say yes, send a follow-up email within 2 hours of the call with exactly what you asked for and the format you need. The pilot structure — 60-day, paid, full refund if targets not met — removes the risk objection. "We are not asking you to trust us. We are asking you to measure us." If they push back on the pilot fee: "The pilot fee converts to your first month's subscription. There is no sunk cost." Close with your contact information visible — do not make them dig for it.
-->
