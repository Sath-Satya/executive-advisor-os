<!-- TEMPLATE: tech-talk
     CATEGORY: Technical
     USE WHEN: delivering a conference-style technical talk to a developer audience
     SLIDE COUNT: 10
     PALETTE: Dark premium
     RENDER: marp --pptx 24-tech-talk.md -->
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'DM Sans', 'Segoe UI', system-ui, sans-serif;
    background: #0a0e14;
    color: #d0d8e4;
    padding: 56px 72px;
  }
  h1 {
    font-family: 'DM Mono', 'Cascadia Code', monospace;
    color: #ffffff;
    letter-spacing: -0.5px;
    font-size: 2em;
    margin-bottom: 20px;
    line-height: 1.2;
  }
  h2 { color: #a78bfa; font-size: 1.25em; margin-top: 0; font-weight: 500; }
  h3 { color: #556677; font-size: 0.9em; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; }
  p, li { color: #d0d8e4; line-height: 1.7; font-size: 1.05em; }
  strong { color: #ffffff; }
  em { color: #a78bfa; font-style: normal; font-weight: 600; }
  code {
    font-family: 'DM Mono', 'Cascadia Code', monospace;
    background: #0d1117;
    padding: 2px 6px;
    border-radius: 3px;
    color: #a78bfa;
    font-size: 0.9em;
  }
  pre {
    background: #0d1117;
    padding: 20px 24px;
    border-left: 3px solid #a78bfa;
    border-radius: 0 6px 6px 0;
  }
  pre code { background: transparent; padding: 0; color: #d0d8e4; font-size: 0.95em; }
  blockquote { border-left: 3px solid #a78bfa; padding: 10px 20px; background: #0d1117; margin: 16px 0; border-radius: 0 6px 6px 0; }
  blockquote p { color: #a78bfa; margin: 0; font-style: italic; font-size: 1.1em; }
  table { width: 100%; border-collapse: collapse; font-size: 0.9em; }
  th { background: #0d1117; color: #a78bfa; padding: 10px 14px; text-align: left; border-bottom: 2px solid #1a2535; }
  td { padding: 9px 14px; border-bottom: 1px solid #1a2535; color: #d0d8e4; }
  section.title { justify-content: center; text-align: center; }
  section.title h1 { font-size: 2.6em; color: #ffffff; margin-bottom: 12px; }
  section.title h2 { color: #a78bfa; font-size: 1.15em; font-weight: 400; margin-bottom: 32px; }
  section.title p { color: #556677; font-size: 0.9em; }
  section.section-break { justify-content: center; text-align: center; background: #0d1117; }
  section.section-break h1 { font-size: 3em; color: #a78bfa; border: none; }
  section.section-break h2 { color: #556677; font-size: 1em; }
---
<!-- _class: title -->

# [Talk Title]
## [One-Line Conference Pitch — What the Audience Will Walk Away Knowing]

[Your Name] · [Company / Role]
[Conference Name] · [Date]

<!-- SPEAKER NOTES — Slide 1: Title
Your title slide is the first impression. The main title should be punchy and concrete — avoid abstractions. Conference talks that perform well on title alone tend to be specific: "How We Cut P99 Latency by 80% Without Rewriting Our Stack" beats "Performance at Scale." Your one-line pitch should complete the sentence: "By the end of this talk, you will know how to..." The audience has already scanned the schedule and chosen your talk — reaffirm that choice in the first 30 seconds by stating exactly what they will get. Include your social handle or GitHub if you want post-talk engagement. If this is a recorded talk, do not start speaking until the title is on screen and the host has introduced you.
-->

---

# The Hook

## A Problem Every Developer Knows

> "Our service was fast in staging. In production, under 10x load, it fell apart."

Everyone who has shipped a distributed system has lived this story. The failure mode is always the same: what you tested was not what ran in production. What you measured was not what users experienced.

**This talk is about closing that gap.**

Three concrete techniques. Works on your stack today. No rewrites required.

<!-- SPEAKER NOTES — Slide 2: The Hook
The hook slide must earn the audience's attention within 90 seconds. The pull-quote is a universal experience — nodding in the audience is your signal it landed. Follow it with an explicit promise: "three concrete techniques, works on your stack today, no rewrites." This is the conference talk contract. The audience should know within the first two slides what they are getting and whether they should stay or switch rooms. Be honest about scope — if the techniques require a specific stack or version, say so now rather than at the end when someone tries to apply it and it does not work. Pause after the pull-quote and make eye contact with the front rows before continuing. The silence makes the quote land.
-->

---

# The Problem

## What Observability Gaps Actually Cost

At scale, there are three categories of failure that are invisible until they cascade:

- **Latency hotspots** — P50 looks fine; P99 is killing retention
- **Partial failures** — 3% of requests silently degrade; aggregate SLO still passes
- **Configuration drift** — staging and production diverge; you find out during an incident

The root problem: **you are measuring averages in a world of percentiles.**

```
P50: 120 ms  ←  "Service is healthy" (your dashboard)
P95: 890 ms  ←  1 in 20 users is frustrated
P99: 4,200 ms ←  1 in 100 users is leaving
```

<!-- SPEAKER NOTES — Slide 3: The Problem
The three-category framing is memorable and sticky. Walk through each one with a single sentence before going to the code block. The code block with P50/P95/P99 numbers is the most concrete thing on this slide — let it breathe. Point to the P99 number and say "that is the user who just decided never to come back." This makes an abstract metric concrete and personal. The "averages in a world of percentiles" line is the thesis of the problem — it should be memorable enough to repeat. If you have your own production numbers, use them instead of these placeholders — real data from your system is always more compelling than hypothetical examples.
-->

---

# The Insight

## The Percentile Illusion

```python
# What you think you are measuring
avg_latency = sum(latencies) / len(latencies)

# What actually describes user experience
p99_latency = np.percentile(latencies, 99)
```

**The fundamental shift:** stop asking "is the service healthy?" — ask "what is the worst experience a real user is having right now?"

- **Histograms, not averages** — use `prometheus_client.Histogram` with explicit buckets
- **Exemplars** — attach trace IDs to histogram observations to find the slow requests
- **Red Method** — Rate, Errors, Duration (per endpoint, per percentile)

<!-- SPEAKER NOTES — Slide 4: The Insight
The code block is intentionally simple — the contrast between two lines of Python is the insight. Walk slowly through both lines and ask the audience which one they see in their dashboards. In most rooms, the answer is the top one. The "what is the worst experience a real user is having right now?" reframe is the key mental model shift. The three bullets are actionable immediately — your audience can go home and implement the first one today. For the Exemplars bullet, briefly explain that exemplars attach a trace ID to a specific histogram observation so that when you see a P99 spike, you can jump directly to the trace that caused it. This is the "find the slow request" capability that histogram averages cannot provide.
-->

---

# The Approach — Part 1

## Instrumentation That Tells the Truth

```python
from prometheus_client import Histogram

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'Request latency by endpoint and method',
    ['endpoint', 'method', 'status'],
    buckets=[0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0]
)

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    duration = time.perf_counter() - start
    REQUEST_LATENCY.labels(
        endpoint=request.url.path,
        method=request.method,
        status=response.status_code
    ).observe(duration)
    return response
```

**Key decisions:** explicit buckets (not defaults), per-endpoint labels, `perf_counter` not `time`.

<!-- SPEAKER NOTES — Slide 5: Deep Dive 1
The code slide should be dense enough to be useful but not so dense it becomes a wall. This example is self-contained and copy-pasteable — that is intentional. Walk through the three "key decisions" at the bottom: explicit buckets matter because the default Prometheus buckets (0.005, 0.01, 0.025...) do not cover the 1–10 second range where real user pain happens; per-endpoint labels let you drill down to the specific route that is slow; perf_counter has microsecond resolution while time.time() can be system-call dependent. Mention that this middleware adds ~0.1 ms overhead per request — for most services, this is acceptable. If someone asks about high-traffic services (>10k RPS), mention the sampling approach in Part 2. Have a live demo ready if the conference setup allows it.
-->

---

# The Approach — Part 2

## From Metrics to Root Cause — in 3 Queries

```promql
# 1. Is there a latency regression in the last hour?
histogram_quantile(0.99,
  rate(http_request_duration_seconds_bucket[5m])
) > 1.0

# 2. Which endpoint is responsible?
topk(3,
  histogram_quantile(0.99,
    sum by (endpoint) (rate(http_request_duration_seconds_bucket[5m]))
  )
)

# 3. Has it always been slow, or did it just change?
histogram_quantile(0.99,
  rate(http_request_duration_seconds_bucket[1h])
)
offset 1d
```

→ From "something is slow" to "this endpoint, since 14:07" in under 2 minutes.

<!-- SPEAKER NOTES — Slide 6: Deep Dive 2
Three PromQL queries is the right depth for a conference talk — more feels like a tutorial, fewer feels underspecified. Walk through each query and its diagnostic purpose. Query 1 is the alert condition — you would put this in Alertmanager with threshold 1.0. Query 2 is the drill-down — `topk(3)` shows the three worst offenders by P99. Query 3 is the regression detector — the `offset 1d` comparison tells you whether this is a new problem or chronic. The closing line "from 'something is slow' to 'this endpoint, since 14:07' in under 2 minutes" is your value proposition restated as a time savings. Pause here and let the audience absorb the three queries. If time permits, show these running against a live Grafana dashboard — visual impact in a conference setting is significant.
-->

---

# Results

## What This Looks Like in Practice

| Before | After |
|---|---|
| Metric: avg latency = 180 ms | Metric: P99 = 4.2 s on `/api/v1/claims/adjudicate` |
| Alert: "service degraded" | Alert: "P99 > 1 s on claims adjudication, started 14:07" |
| MTTR: 3.5 hours (hunt for root cause) | MTTR: 22 minutes (instrument → query → trace) |
| On-call experience: stressful, guesswork | On-call experience: systematic, tool-guided |

**Measured over 6 months, 3 production incidents:**
- MTTR reduced from avg 3.5 h → 28 min
- P99 regressions detected in < 5 min (vs. customer report)
- Zero P0 incidents from undetected latency drift post-implementation

<!-- SPEAKER NOTES — Slide 7: Results
Results slides must have real numbers. If you do not have production data from your own system, be honest about that and use benchmark data from a well-known reference. The before/after table format is highly effective for conference audiences because it makes the value concrete and comparable. The MTTR reduction from 3.5 hours to 28 minutes is the single most compelling number — it translates to reduced on-call burden, reduced SLA penalties, and better sleep for engineers. Walk through the bottom three bullets quickly — these are the compounding benefits over time. If someone asks "how long did the instrumentation take?", the honest answer is one sprint for a moderately complex service — frame that against 6 months of saved incident time.
-->

---

# Lessons

## What Generalized Across the Team

- **Observability is a product feature**, not infrastructure — it needs an owner and a roadmap
- **Start with the three instruments**: histograms (latency), counters (error rate), gauges (resource utilization)
- **Agree on alert SLOs before writing alert rules** — alerting without an SLO is noise generation
- **Teach your on-call rotation to read dashboards** — instrumentation is useless without fluency

> The biggest lesson: our staging environment had perfect metrics. Our production environment had averages. We fixed production first.

<!-- SPEAKER NOTES — Slide 8: Lessons
Lessons slides give the audience takeaways that generalize beyond your specific system. The four bullets should be memorable and actionable. "Observability is a product feature" is a mindset shift — it means the team should have a dedicated engineer (or rotation) responsible for observability health, not treating it as a side task. The pull-quote at the bottom is the talk's punchline — it subverts the expectation that staging should mirror production. In most organizations, the reverse is true and nobody talks about it. End on this quote with a brief pause. It tends to get a knowing laugh from experienced engineers in the audience.
-->

---

# Code and Resources

## Take These Home

**Reference implementation (MIT licensed):**
```
github.com/[your-org]/[repo-name]
```

**What is in the repo:**
- FastAPI middleware with histogram instrumentation
- Grafana dashboard JSON (import and use today)
- 10 PromQL queries for common debugging scenarios
- Runbook template: "How to investigate a P99 spike"

**Further reading:**
- Brendan Gregg — "Systems Performance" (latency histograms, Ch. 2)
- Cindy Sridharan — "Distributed Systems Observability" (O'Reilly, free online)
- SRE Book Ch. 6 — Monitoring Distributed Systems

<!-- SPEAKER NOTES — Slide 9: Code and Resources
Always give the audience something they can use immediately after the talk. The GitHub repo should be ready and public before you go on stage — test the link. The Grafana dashboard import JSON is the highest-value artifact in the repo: it means someone can have a working dashboard within 10 minutes of their first instrumented service. The PromQL query library is the second most valuable. Include both in the README as copy-pasteable blocks, not just in the dashboard JSON. The three book recommendations are classics — any serious engineer on observability should have read Brendan Gregg. Mention them briefly rather than reading them out. If you are livestreamed, read the GitHub URL slowly and clearly — people will try to type it in real time.
-->

---

# Thank You

## [Your Name] — [Company]

**Contact:**
- GitHub: `@[handle]`
- LinkedIn: `[profile-url]`
- [Conference handle]: `@[handle]`

**Slides and repo:** `github.com/[org]/[repo]`

**Questions?**

<!-- SPEAKER NOTES — Slide 10: Thanks and Contact (final)
Leave this slide up during the full Q&A period — it should be the last thing on screen when people are leaving the room so they can photograph your contact details. Have the GitHub URL large enough to read from the back row. During Q&A: acknowledge good questions before answering; if a question is too specific for the room, offer to continue the conversation in the hallway. Prepare three questions to ask yourself in case the Q&A starts slowly: "One question I get asked a lot is..." This avoids awkward silence. If time runs out, offer to answer remaining questions via Twitter/GitHub issues. Thank the conference organizers and A/V team verbally before leaving the stage.
-->
