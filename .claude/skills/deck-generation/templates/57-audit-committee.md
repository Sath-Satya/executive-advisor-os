<!-- TEMPLATE: audit-committee
     CATEGORY: Finance
     USE WHEN: quarterly audit committee update to board
     SLIDE COUNT: 11
     PALETTE: Executive cream with dark navy accents (formal)
     RENDER: marp --pptx 57-audit-committee.md -->

---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  :root {
    --cream: #f7f4ef;
    --navy: #0e1b2e;
    --dark-navy: #071320;
    --gold: #b8965a;
    --muted: #5a6a7a;
    --rule: #c8bfb0;
    --green: #1f6e4c;
    --red: #b02a2a;
    --amber: #b57000;
  }
  section {
    background: var(--cream);
    color: var(--navy);
    font-family: 'Segoe UI', system-ui, sans-serif;
    padding: 48px 60px;
    border-top: 5px solid var(--dark-navy);
  }
  h1 {
    font-size: 1.80rem; font-weight: 700; color: var(--dark-navy);
    letter-spacing: -0.3px; border-bottom: 2px solid var(--gold);
    padding-bottom: 8px; margin-bottom: 20px;
  }
  h2 { font-size: 1.15rem; font-weight: 600; color: var(--muted); margin-bottom: 12px; text-transform: uppercase; letter-spacing: 0.5px; }
  ul { margin: 0; padding-left: 1.4em; }
  li { margin-bottom: 9px; font-size: 0.97rem; line-height: 1.55; }
  table { width: 100%; border-collapse: collapse; font-size: 0.88rem; margin-top: 10px; }
  th { background: var(--dark-navy); color: var(--cream); padding: 7px 11px; text-align: left; font-weight: 600; }
  td { padding: 6px 11px; border-bottom: 1px solid var(--rule); }
  tr:nth-child(even) td { background: #ede9e0; }
  .label {
    display: inline-block; background: var(--dark-navy); color: var(--cream);
    font-size: 0.68rem; font-weight: 700; letter-spacing: 1.2px;
    text-transform: uppercase; padding: 3px 10px; border-radius: 2px; margin-bottom: 12px;
  }
  .status-green { color: var(--green); font-weight: 700; }
  .status-red { color: var(--red); font-weight: 700; }
  .status-amber { color: var(--amber); font-weight: 700; }
  .finding-box {
    border-left: 4px solid var(--gold); background: white;
    padding: 12px 16px; margin-bottom: 10px; border-radius: 0 6px 6px 0;
    font-size: 0.93rem;
  }
  .finding-box .severity {
    font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px;
    margin-bottom: 4px;
  }
  .sev-high { color: var(--red); }
  .sev-med { color: var(--amber); }
  .sev-low { color: var(--green); }
  section.cover {
    background: var(--dark-navy); color: var(--cream);
    display: flex; flex-direction: column; justify-content: center;
    border-top: none;
  }
  section.cover h1 { color: var(--cream); border-color: var(--gold); font-size: 2.2rem; }
  section.cover .sub { color: var(--gold); font-size: 1.0rem; margin-top: 8px; }
  section.cover .meta { color: #8899ac; font-size: 0.85rem; margin-top: 24px; line-height: 1.8; }
  section.close {
    background: var(--dark-navy); color: var(--cream); border-top: none;
    display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;
  }
  section.close h1 { color: var(--gold); border: none; font-size: 1.9rem; }
  section.close p { color: #8899ac; font-size: 0.92rem; line-height: 1.7; }
---

<!-- _class: cover -->

<div class="label">Audit Committee — Q3 2026 Update</div>

# Northwind Capital — Audit Committee Report

<div class="sub">Quarterly Update: Internal Controls, External Audit, Risk, and Compliance</div>
<div class="meta">
  November 5, 2026 &nbsp;|&nbsp; Audit Committee of the Board of Directors<br>
  Presenter: Margaret Wu, Chief Audit Executive<br>
  Attendees: Audit Committee Chair, 3 Independent Directors, CFO, General Counsel, External Auditor (EY)
</div>

<!-- Presenter notes: Good afternoon, committee members. This is the Q3 2026 Audit Committee update, covering internal controls, the external audit status, the risk register, compliance matters, fraud risk, IT controls, findings, remediation status, and auditor independence. All materials presented today are subject to attorney-client privilege where applicable and should be treated as confidential board communications. The format follows our charter-mandated quarterly update structure. We have 90 minutes allocated: 60 minutes for prepared remarks across the eleven agenda items, 30 minutes for committee questions. External auditors from EY are present for agenda items 3, 5, and 10. I will indicate when EY will speak. The committee has received the pre-read materials including the complete internal audit reports for Q3. Today I will cover highlights and exceptions, not a full recitation of the reports. Please refer to the pre-reads for underlying detail. -->

---

# Agenda

<div class="label">Today's Topics</div>

| # | Topic | Presenter | Time |
|---|---|---|---|
| 1 | Internal Controls Status | CAE | 8 min |
| 2 | External Auditor Update | EY | 8 min |
| 3 | Risk Register Review | CAE | 10 min |
| 4 | Compliance Matters | General Counsel | 8 min |
| 5 | Fraud Risk Assessment | CAE | 6 min |
| 6 | IT Controls | CIO | 8 min |
| 7 | Findings Summary | CAE | 6 min |
| 8 | Remediation Status | CAE | 6 min |
| 9 | Auditor Independence | EY | 4 min |
| 10 | Committee Q&amp;A | All | 30 min |

<!-- Presenter notes: The agenda follows the structure required by Section 3.2 of our Audit Committee Charter and is consistent with the format we have used for the past three years. Today's meeting has three presenters: the Chief Audit Executive for the majority of items, EY for the external audit update and independence confirmation, and the CIO for IT controls. The General Counsel will briefly address the compliance matters section. Timing is approximate. If any committee member wishes to spend more time on a particular topic, please signal and we will adjust. The most time-sensitive item is the External Auditor Update (Item 2) because EY needs to leave by 3:30 PM for a client commitment. Committee Chair, please let me know if you would prefer to front-load the EY items. The pre-read materials distributed Monday included: Q3 internal audit report, risk register update, IT controls assessment, and EY's Q3 status letter. Assuming committee members have reviewed these, I will present highlights and exceptions only today. -->

---

# Internal Controls Status — Q3 2026

<div class="label">SOX 404 and Internal Control Environment</div>

| Control Area | Q3 Status | Open Deficiencies | Notes |
|---|---|---|---|
| Financial Close &amp; Reporting | <span class="status-green">Effective</span> | 0 | 5-day close maintained; 3 new controls implemented |
| Revenue Recognition | <span class="status-amber">Remediation in Progress</span> | 1 Significant Deficiency | Advisory fee calculation; see Findings slide |
| Expenditure &amp; AP | <span class="status-green">Effective</span> | 0 | PCard controls enhanced in Q2 |
| Payroll &amp; HR | <span class="status-green">Effective</span> | 0 | Compensation audit clean |
| Treasury &amp; Cash | <span class="status-green">Effective</span> | 0 | New T-bill investment controls tested |
| IT General Controls | <span class="status-amber">Partial</span> | 1 Deficiency | Access review; detail in IT Controls slide |

Overall assessment: **No Material Weaknesses.** 2 items in remediation; expected remediation by December 31.

<!-- Presenter notes: The internal control environment is generally sound with no material weaknesses to report as of September 30, 2026. This is the 14th consecutive quarter without a material weakness since I joined as CAE in 2023. There are two items requiring committee attention. First, the revenue recognition significant deficiency: our internal audit team identified that advisory fees for complex multi-tranche transactions were being recognized under a manual calculation process that lacked secondary review controls. This is not a GAAP error — we reviewed the specific transactions and revenue was recognized correctly — but the absence of a secondary review creates the risk of future errors. We are implementing an automated fee calculation workflow in the Salesforce FSC platform, which will be live in January 2027 and will resolve this deficiency. In the interim, we have implemented a manual compensating control requiring CFO review of all fees over $500K before recognition. Second, the IT access review deficiency: I will let the CIO address this in detail in the IT Controls section. The bottom line is that EY has reviewed both items and concurs with management's classification as significant deficiency and deficiency respectively (not material weaknesses) and with the proposed remediation timelines. -->

---

# External Auditor Update — EY

<div class="label">Q3 Interim Audit Status and Q4 Planning</div>

| Phase | Status | Issues Identified | Notes |
|---|---|---|---|
| Q3 Review (SAS 100) | <span class="status-green">Complete</span> | None | Review letter issued October 28 |
| Interim Testing (SOX) | <span class="status-green">Complete</span> | 1 observation | Revenue recognition (management aware) |
| Year-End Audit Planning | <span class="status-amber">In Progress</span> | — | Scoping complete; fieldwork begins Nov. 15 |
| 10-Q Filing | <span class="status-green">On Track</span> | — | Target: November 14, 2026 |

EY audit opinion: "Nothing came to our attention suggesting the interim financial statements are not fairly presented in all material respects" (full text in board pre-read, Tab 3).

<!-- Presenter notes: I will turn it over to the EY engagement partner to present this section. EY, please go ahead. [EY presents.] Thank you. To summarize for the committee record: EY's Q3 review is complete with a clean SAS 100 review conclusion. The one interim observation regarding revenue recognition is consistent with management's own significant deficiency identification and does not represent an incremental finding — EY and internal audit identified the same control gap through independent processes, which actually increases our confidence in the internal audit function's effectiveness. Year-end audit planning is in progress; EY will begin fieldwork November 15 and expects to complete the audit by February 5, 2027, in time for our February 12 earnings release. The audit scope includes all three business segments and has been expanded this year to include additional testing of the Salesforce FSC implementation controls given the system change in progress. EY will request committee pre-approval for any audit scope changes that may arise during fieldwork. The 10-Q filing remains on track for November 14. -->

---

# Risk Register — Top 10 Risks

<div class="label">Enterprise Risk Profile — September 30, 2026</div>

| Rank | Risk | Likelihood | Impact | Trend | Owner |
|---|---|---|---|---|---|
| 1 | Revenue concentration (top 3 segments) | Medium | High | &#x2192; Stable | CEO |
| 2 | Key person — Head of Capital Markets | Medium | High | &#x25B2; Elevated | CEO |
| 3 | Technology transition (Salesforce FSC) | Medium | Medium | &#x25B2; New |  CIO |
| 4 | Credit quality — 2 watch-list facilities | Low-Med | Medium | &#x25B2; Elevated | CCO |
| 5 | Regulatory change — financial services | Low | High | &#x2192; Stable | GC |
| 6 | Cybersecurity — third-party vendor | Low | High | &#x2192; Stable | CIO |
| 7 | Interest rate sensitivity (Lending NIM) | Medium | Medium | &#x25B2; Elevated | CFO |
| 8 | Atlanta office ramp failure | Medium | Medium | &#x2192; Stable | CRO |
| 9 | Fraud — advisory fee manipulation | Low | High | &#x2192; Stable | CAE |
| 10 | Talent market — advisor retention | Medium | Medium | &#x2192; Stable | CHRO |

Two risks elevated since Q2: Key Person (Rank 2) and Credit Quality (Rank 4).

<!-- Presenter notes: The risk register is reviewed quarterly by the executive team and presented to the audit committee for oversight. I will focus on the two risks that have been elevated since the Q2 update. Rank 2 — Key Person risk — was elevated from Low-Medium to Medium in October following the retention situation with our Head of Capital Markets that the CFO mentioned in the finance committee briefing earlier today. The audit committee should be aware of this risk at a high level; the CFO and CEO are managing the retention actively. Risk Rank 4 — Credit Quality — was elevated when two Lending facilities were placed on the watch list in Q3. The CCO will provide a brief update after this presentation. The two facilities involve total outstanding balances of $18.4M and are not currently in default; they are on the watch list due to covenant tightness (both within 10% of threshold). Reserve methodology remains appropriate; no impairment charge is required at Q3. For the remaining risks, I would highlight Rank 6 (cybersecurity — third-party vendor) as a standing watch item given the Salesforce FSC implementation: we are introducing a new major vendor relationship, and our third-party risk management process has been enhanced to assess Salesforce's SOC 2 Type II controls. The SOC 2 report is on file and was reviewed by internal audit in Q3 with no material exceptions identified. -->

---

# Compliance Matters

<div class="label">Regulatory and Legal Update</div>

- **SEC Regulation Best Interest (Reg BI):** Annual compliance review complete; no deficiencies identified; documentation practices rated satisfactory by independent compliance consultant
- **Anti-Money Laundering (AML):** Q3 SAR filings: 0 (consistent with prior quarters); enhanced customer due diligence applied to 3 new Wealth Management clients as per policy
- **Employment law:** 1 EEOC inquiry received October 2026 (details shared with committee chair under privilege); General Counsel assessing; no material financial exposure anticipated
- **Data privacy (CCPA/GDPR):** Quarterly assessment clean; 2 data subject requests received and resolved within required timeframes

No pending litigation requiring financial statement disclosure beyond existing disclosures.

<!-- Presenter notes: I will hand this section to the General Counsel for a brief verbal update, then return for the remainder of the deck. [GC presents.] To summarize: from a legal and compliance perspective, Q3 was relatively clean. The Reg BI review is the most important recurring compliance obligation given our advisory business model, and the independent consultant's satisfactory rating is a meaningful endorsement. The EEOC inquiry is the only new development: the General Counsel has assessed the claim and believes the likelihood of material liability is low based on facts and documentation. We will disclose as required if assessment changes. The AML program continues to function as designed; the zero SAR quarter is consistent with our client profile and is not suggestive of underreporting — we have rigorous screening processes. The three enhanced due diligence clients were all approved after extended review; two were new Wealth Management clients with complex ownership structures, and one was a Capital Markets client with international connections requiring additional OFAC screening. All three were cleared. Data privacy compliance is managed by our privacy officer and has been consistently clean. No new state privacy law requirements became effective in Q3 that require program changes. -->

---

# Fraud Risk Assessment

<div class="label">Annual Fraud Risk Program Update</div>

- **Fraud risk assessment** refreshed annually per COSO framework; Q3 2026 assessment complete with no new high-risk areas identified
- **Highest residual fraud risks:** Advisory fee manipulation (Rank 9), expense reimbursement fraud (below top 10), employee payroll fraud (below top 10)
- **Controls effectiveness:** All three high-risk areas have effective preventive and detective controls in place; compensating controls added for advisory fee calculation pending Salesforce FSC go-live
- **Anonymous hotline:** 4 calls received in 2026 YTD; 3 resolved as non-fraudulent (2 HR matters, 1 vendor dispute); 1 under investigation (see confidential memo distributed to committee chair)

No fraud losses recorded in 2026.

<!-- Presenter notes: The fraud risk assessment is a required annual activity under our audit committee charter and the COSO 2013 internal control framework. The assessment is conducted by internal audit with input from management and reviewed by the audit committee. No new high-risk fraud areas were identified in the 2026 assessment. The most relevant fraud risk for Northwind Capital is advisory fee manipulation — this is industry-specific and relates to the potential for advisors or finance staff to manipulate fee calculations in complex multi-tranche transactions. This risk is why the revenue recognition significant deficiency is particularly important to remediate: the absence of a secondary review on fee calculations creates an opportunity for manipulation. Our compensating controls include CFO review of all fees over $500K and independent reconciliation of deal economics to fee invoices by a Finance analyst not in the advisory chain. Regarding the anonymous hotline: there is one matter currently under investigation that I have addressed in a confidential memo to the audit committee chair. I am not in a position to discuss this in the full meeting, but the committee chair is aware of the facts and the investigation timeline. The remaining three calls were employment-related matters (two handled by HR) and a vendor dispute resolved through contract review. No financial losses are associated with any of the 2026 hotline matters to date. -->

---

# IT Controls Assessment

<div class="label">Technology Risk and General Controls</div>

- **Access management:** Quarterly user access review identified 12 accounts with excessive permissions; 10 remediated; 2 pending (target: November 30) — classified as **control deficiency** (not significant)
- **Change management:** All production system changes in Q3 followed approved change control process; 0 unauthorized changes detected
- **Backup and recovery:** Monthly disaster recovery test completed September 2026; recovery time objective (RTO) of 4 hours met
- **Salesforce FSC pre-go-live assessment:** SOC 2 Type II reviewed; access control design approved; data migration plan reviewed; no go/no-go issues identified

<!-- Presenter notes: The CIO will address this section briefly, then I will take back control. [CIO presents.] The access management deficiency warrants committee explanation. During our Q3 quarterly user access review, internal audit identified 12 user accounts with access rights beyond what their role requires — a standard "least privilege" violation. Ten of these have been remediated (access removed). Two accounts belong to contractors whose system access is being renegotiated as part of contract renewals; access will be reduced by November 30. This is classified as a control deficiency (the lowest severity level) because the accounts have not been used inappropriately — we have log evidence showing these accounts have not accessed the sensitive data their permissions would allow. However, the existence of excess permissions is a control gap regardless of usage. This is the second consecutive quarter with an access management finding; the CIO has committed to implementing automated access provisioning that will prevent this class of deficiency going forward. The Salesforce FSC pre-go-live assessment result is important: internal audit reviewed the implementation plan and found no go/no-go issues. The data migration approach, access control design, and SOC 2 coverage are all adequate. We are ready to proceed to go-live in January. -->

---

# Findings Summary — Q3 2026

<div class="label">Internal Audit Findings</div>

<div class="finding-box">
  <div class="severity sev-high">Significant Deficiency — Revenue Recognition</div>
  Advisory fee calculation for multi-tranche transactions lacks automated secondary review control. Manual compensating control implemented October 2026. Permanent fix: Salesforce FSC automated fee calculation, target January 31, 2027.
</div>

<div class="finding-box">
  <div class="severity sev-med">Control Deficiency — IT Access Management</div>
  12 user accounts with excess permissions identified in Q3 quarterly review. 10 remediated; 2 pending contractor renewal. Target: November 30, 2026.
</div>

<div class="finding-box">
  <div class="severity sev-low">Observation — Expense Report Timeliness</div>
  14% of expense reports submitted more than 30 days after travel dates; policy requires 15 days. No financial impact. Reminder communication sent October 15; monitoring in Q4.
</div>

No material weaknesses. Total open findings: 2 deficiencies, 1 observation. Prior quarter: 3 deficiencies, 2 observations. Trend improving.

<!-- Presenter notes: The findings summary presents all open findings from the Q3 audit cycle. Total open items have declined from 5 in Q2 to 3 in Q3, reflecting effective remediation of prior-period findings. The two significant findings — the revenue recognition significant deficiency and the IT access deficiency — have been discussed in prior slides. I want to draw the committee's attention to the improving trend: in 2024 we had 8 open findings on average across quarters; in 2025 we averaged 5; in 2026 YTD we are averaging 3.5. This trajectory reflects the investment the company has made in internal audit resources and control infrastructure over the past three years. The expense report observation is a policy compliance matter, not a financial control failure — we found no cases of unauthorized or fraudulent expenses. The issue is simply timeliness: 14% of expense reports were submitted late. We have sent a company-wide reminder and are monitoring compliance in Q4. If the rate does not improve to below 5% in Q4, we will propose a policy change to require manager approval before expenses are reimbursable (currently, late submission has no practical consequence). EY has reviewed all three findings and concurs with management's severity classifications and proposed remediation timelines. -->

---

# Remediation Status — Open Items

<div class="label">Prior Findings — Remediation Tracking</div>

| Finding | Period Opened | Target Close | Status | Evidence |
|---|---|---|---|---|
| Revenue recognition — secondary review | Q3 2026 | Jan 31, 2027 | <span class="status-amber">In Progress</span> | Compensating control active; SF FSC on track |
| IT access — excess permissions | Q3 2026 | Nov 30, 2026 | <span class="status-amber">In Progress</span> | 10 of 12 remediated; 2 pending |
| Expense report timeliness | Q3 2026 | Q4 2026 | <span class="status-amber">In Progress</span> | Reminder sent; monitoring |
| Vendor contract review backlog | Q2 2026 | Oct 31, 2026 | <span class="status-green">Closed</span> | 47 contracts reviewed; 3 renewed |
| Segregation of duties — AP | Q1 2026 | Sep 30, 2026 | <span class="status-green">Closed</span> | Role redesign implemented; tested effective |

2 of 5 prior-period findings closed on time. No findings older than 9 months remain open.

<!-- Presenter notes: The remediation tracking table provides the committee with visibility into all open and recently closed findings. Two items closed in Q3 as planned. The vendor contract review backlog was opened in Q2 when we found 47 contracts had lapsed without renewal review — all 47 have now been reviewed and 3 were renewed with updated terms. The segregation of duties finding in Accounts Payable was remediated through a role redesign that separated invoice approval from payment processing; we tested the redesigned controls in Q3 and confirmed they are operating effectively. The committee should note that our finding remediation rate in 2026 is 94% on-time (32 findings due for closure in 2026 YTD; 30 closed on time, 2 with approved extensions). This compares favorably to our 2025 on-time rate of 81% and reflects stronger accountability and tracking in the internal audit function. The two items receiving approved extensions are the IT access contractor accounts (waiting on contract negotiations outside internal audit's control) and the revenue recognition finding (permanent fix is technology-dependent with a known January 2027 timeline). For the three current open items, I will provide a written status update to the committee chair by December 5, prior to the Q4 meeting. -->

---

# Auditor Independence and Non-Audit Services

<div class="label">EY Independence Confirmation — 2026</div>

| Service Type | FY 2026 Fees | Pre-Approved | Independence Impact |
|---|---|---|---|
| Audit (annual) | $620,000 | Yes | None — audit services |
| Audit-related (SOX, quarterly reviews) | $185,000 | Yes | None — audit-related |
| Tax compliance | $48,000 | Yes | None — routine compliance |
| Advisory / consulting | $0 | N/A | N/A |
| **Total EY Fees** | **$853,000** | | |

EY Engagement Partner confirms: no independence-impairing relationships between EY and Northwind Capital or any related party as of November 5, 2026.

<!-- Presenter notes: I will turn the floor to EY for the independence confirmation. [EY engagement partner presents.] For the committee record: EY has confirmed their independence as required by SEC Rule 2-01 and PCAOB AS 1005. There are no non-audit advisory or consulting engagements. Total FY 2026 EY fees are $853,000, within the board-approved budget of $875,000. Audit fees of $620,000 are flat versus prior year; the incremental SOX testing scope related to the Salesforce FSC implementation was absorbed within the existing engagement budget. Tax fees of $48,000 relate to routine federal and state compliance filings only. The committee should note that our policy prohibits EY from performing any advisory or consulting services; this is more restrictive than the SEC rules require and reflects our commitment to audit independence. EY's lead engagement partner rotates every 5 years; the current partner has served 3 years. The concurring review partner rotates every 7 years; current partner in year 2. Both rotation schedules are compliant with PCAOB and SEC requirements. EY will distribute their formal independence letter to the committee chair by November 12. The committee is required to discuss independence with EY at least annually; this discussion satisfies that requirement. -->

---

<!-- _class: close -->

# Audit Committee Meeting — Q3 2026 Complete

**Action Items from Today's Meeting**

1. Management to provide written remediation updates by December 5, 2026
2. General Counsel to update committee chair on EEOC inquiry by November 30
3. CAE to provide confidential investigation update to committee chair by November 20
4. EY to distribute formal independence letter by November 12

Next Audit Committee Meeting: February 4, 2027 (Q4 2026 and Year-End Audit)

<!-- Presenter notes: This concludes the prepared remarks portion of the audit committee update. We have four specific action items arising from today's meeting, all assigned to specific owners and deadlines. Before we open Q&A, I want to remind the committee that the management representation letters for the Q3 10-Q require signatures by November 12 — CFO and CEO signature pages are in Tab 9 of the board materials. A 30-minute Q&A session is available. The committee may wish to hold an executive session with EY without management present — this is a standing option under our charter and can be arranged now or after Q&A. Similarly, the committee has the option to meet with the CAE without management present, which I recommend annually. Committee Chair, please advise on whether you wish to hold executive sessions today, and in what order. The next audit committee meeting is scheduled for February 4, 2027, which is one week before the Q4 earnings release, consistent with our practice of committee review before public reporting. At that meeting, we will cover the full-year audit results, year-end financial statement review, and the external audit opinion. Thank you for your attention and engagement today. -->
