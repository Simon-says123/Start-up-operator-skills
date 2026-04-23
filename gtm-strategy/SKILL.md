---
name: gtm-strategy
description: Build a go-to-market strategy for a product launch or new market entry. Use when planning a GTM from scratch, preparing a launch plan, defining channel mix and messaging, or setting KPIs for a new product. Trigger when Simon says "build a GTM", "create a go-to-market", "GTM strategy for [product]", "how should we launch [product]", "what channels should we use", "help me plan a product launch", or when a product, segment, and launch intent are described together. Also trigger when Simon asks to review or pressure-test an existing GTM plan.
calls:
  - docx
---
<!-- version: 1.0 | tested-on: claude-sonnet-4-6 -->

## Triggers

Use this skill when Simon says: "build a GTM", "create a go-to-market", "GTM strategy for [product]", "how should we launch [product]", "what channels should we use for [product]", "help me plan a product launch", "launch strategy for [market]", or "pressure-test my GTM". Also trigger when Simon describes a product and a target segment together and asks how to reach them.

## Dependencies

- Web search tool — for market and competitive context
- `docx` skill — for final document output
- User-supplied: product name and description, target segment, launch timeline, budget envelope or constraints

## Instructions

**Mode: Co-Worker**

### Goal

Produce a structured, actionable go-to-market strategy document for a specific product and target segment. The output is a DOCX ready to share internally or with a launch team, covering channel mix, messaging, KPIs, launch timeline, and a 90-day execution roadmap.

### Process

**Step 1 — Gather inputs**

Ask Simon to confirm the following before any analysis begins:

- Product name and description (what it does, who it's for, key differentiators)
- Primary target segment (who is the ideal first customer?)
- Launch timeline (hard deadline or rough window?)
- Budget envelope or resource constraints (optional but shapes channel recommendations)
- Any known constraints — regions, channels to avoid, regulatory limits

> **GATE 1 — Input confirmation.**
> Present a brief summary of what you've captured. Ask: "Is this an accurate picture of what we're working with? Anything missing or wrong before I start the analysis?"
> Do not proceed to Step 2 until Simon confirms.

**Step 2 — Research and channel analysis**

Using web search, gather:

- Competitive landscape: who else is in this space, how do they go to market?
- Channel benchmarks: what channels are standard and what's working for comparable products?
- Target segment behaviour: where do they discover products, what do they trust?

Evaluate the following channel categories against the confirmed segment and constraints:

- Digital paid (search, social, display)
- Content and inbound (SEO, blog, thought leadership)
- Sales and outbound (direct, partnerships, BD)
- Community and grassroots (forums, events, ambassador)
- Product-led (freemium, viral loops, referral)

Produce a ranked channel shortlist (max 4) with a one-sentence rationale for each.

> **GATE 2 — Channel confirmation.**
> Present the ranked shortlist. Ask: "Do these channels match your instincts and resources? Any to add, remove, or reprioritise?"
> Adjust the shortlist based on Simon's input. Do not proceed to Step 3 until confirmed.

**Step 3 — Build the full strategy**

Using only the confirmed channel set, produce the following components:

**Messaging framework**
- Core value proposition for the target segment
- Key differentiators vs. named competitors
- Pain-to-solution mapping (top 2–3 pain points and how the product solves them)
- Channel-specific message variations for each confirmed channel

**KPI framework**
- 2–3 awareness metrics (impressions, reach)
- 2–3 engagement metrics (CTR, cost per engagement)
- 2–3 conversion metrics (signups, demos, trials)
- 1–2 revenue metrics (MRR target, CAC ceiling)
- Baseline-setting guidance (what to measure before launch)

**Launch timeline**
- Pre-launch (T-4 weeks to T-1 week): preparation milestones per channel
- Launch week: key activities and sequencing
- Post-launch (weeks 2–8): momentum, feedback loops, optimisation cadence
- Go/no-go criteria at each phase gate

**90-day execution roadmap**
- Week-by-week priority actions for the first 13 weeks
- Owner placeholders (team, agency, or founder)
- Dependencies and sequencing risks flagged

**Step 4 — Draft review**

Compile all components into a single structured draft. Present a plain-text summary of each section (channel shortlist, messaging, KPIs, timeline, roadmap).

> **GATE 3 — Draft review.**
> Ask: "Does this strategy reflect your intent? What needs to change before I write the final document?"
> Iterate on any section Simon flags. Re-present the affected section after each revision. Do not proceed to Step 5 until Simon approves the full draft.

**Step 5 — Produce final document**

Invoke the `docx` skill. Build a formatted DOCX with the following structure:

1. Executive Summary (half page)
2. Target Segment & Context
3. Channel Mix & Rationale
4. Messaging Framework
5. KPI Framework
6. Launch Timeline
7. 90-Day Execution Roadmap
8. Risk & Mitigation

Save to `Resources/Output files/` using naming convention: `[product-name]_gtm-strategy_v1.docx`

Present the file link to Simon.

## Failure Modes

- If Simon cannot supply a target segment, do not proceed — a GTM without a defined segment is not a GTM. Ask Simon to narrow it before continuing.
- If web search returns no results for the competitive landscape, proceed with known information and label all competitive claims `[Unverified]`. Flag the gap to Simon.
- If the `docx` skill is unavailable, produce the strategy as a markdown file instead and note the fallback.
- If Simon's inputs are contradictory (e.g., enterprise segment + zero budget for sales), flag the tension explicitly before proceeding. Do not silently paper over it.
- If Simon requests more than 4 channels, push back: recommend focusing on 3–4 channels done well. If Simon insists, proceed but flag the execution risk.
