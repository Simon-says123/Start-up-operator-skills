---
name: swot-analysis
description: Run a structured SWOT analysis for any product, business, startup, or strategic decision. Produces a formatted PDF with a four-quadrant SWOT matrix, SO/ST/WO/WT cross-reference insights, and 3–5 prioritised strategic recommendations. Use when doing a strategic review, competitive positioning assessment, market entry evaluation, or preparing for an investment or board discussion. Trigger when the user says "SWOT", "strengths and weaknesses", "strategic assessment", "analyse our position", "where are we exposed", "what are our competitive advantages", "internal vs external factors", or whenever a product, startup, or business is being evaluated and a structured strategic framework would add clarity — even if SWOT isn't named explicitly.
---
<!-- version: 1.0 | tested-on: claude-sonnet-4-6 -->

## Triggers

Use this skill when the user says: "run a SWOT", "do a SWOT analysis", "map our strengths and weaknesses", "strategic assessment", "analyse our position", "where are we exposed", or when evaluating a product, company, or initiative and a structured internal/external review would help. Also trigger when someone asks "what are our advantages", "what threats should we worry about", or shares a company or opportunity and asks for a strategic take.

## Dependencies

- PDF skill (for final output)
- Web search (optional — for market/competitive context if the user hasn't supplied it)

## Instructions

**Mode: Co-Worker**

### Goal

Produce a rigorous, context-specific SWOT analysis — four populated quadrants, a strategic cross-reference layer (SO/ST/WO/WT), and 3–5 prioritised recommendations — delivered as a formatted PDF. The value is in the cross-referencing and recommendations, not just the list of factors.

---

### Process

**Step 1 — Gather context**

Ask the user for the following. Request all at once; do not scatter into multiple messages.

1. What is the subject? (product, business unit, startup, initiative, market entry)
2. What is the purpose of this SWOT? (investment decision, product review, board prep, competitive response)
3. Internal context: capabilities, resources, team strengths, known constraints or gaps
4. External context: competitive landscape, market dynamics, regulatory environment, key trends
5. Any customer feedback, traction data, or usage signals (optional)
6. What time horizon matters? (current state vs. 12–24 months out)

> **GATE 1 — Input confirmation.**
> Once the user has responded, summarise back the subject and scope in two sentences. Ask: "Is this the right framing before I start the analysis?" Do not draft the SWOT until confirmed.

---

**Step 2 — Draft the SWOT quadrants**

For each quadrant, identify 5–7 items. Quality over quantity — drop weak items rather than pad to hit the count.

- **Strengths** (internal, positive): unique capabilities, brand, IP, team, distribution, cost position, customer relationships
- **Weaknesses** (internal, negative): resource gaps, skill deficits, high costs, weak market presence, dependency risks, legacy constraints
- **Opportunities** (external, positive): growing segments, market gaps, competitor weaknesses, regulatory tailwinds, technology shifts, partnership potential
- **Threats** (external, negative): emerging competitors, regulatory risk, technology disruption, economic headwinds, customer behaviour shifts, partner/supplier risk

Be specific to the subject — avoid generic items that would apply to any business. If web search would add useful competitive or market context, use it now.

> **GATE 2 — SWOT review.**
> Present the four quadrants in a clear table. Ask: "Does this look accurate? Anything to add, remove, or reframe before I build the strategic layer?" Revise based on feedback. Do not proceed to cross-referencing until the user is satisfied with the raw SWOT.

---

**Step 3 — Cross-reference analysis**

Map interactions across the four quadrants to surface strategic implications:

- **SO** (Strengths + Opportunities): Where can we lean in hardest? What strengths best position us to capture the biggest opportunities?
- **ST** (Strengths + Threats): Which strengths act as a buffer against the most dangerous threats?
- **WO** (Weaknesses + Opportunities): Which opportunities, if captured, would directly address key weaknesses?
- **WT** (Weaknesses + Threats): Where are we most exposed? What combinations of weakness and threat represent the highest risk?

Identify 2–3 insights per quadrant pair. Focus on the intersections that are most strategically significant — not every combination needs a finding.

---

**Step 4 — Develop strategic recommendations**

Produce 3–5 recommendations derived directly from the cross-reference analysis. Each recommendation must:

- Be action-oriented (what to do, not just what to consider)
- Map to a specific SO/ST/WO/WT insight
- Include a rationale in one sentence
- Carry a priority label: **High / Medium / Low**

Frame using the four strategic postures where useful:
- **Build**: double down on a strength to capture an opportunity
- **Defend**: shore up a weakness before a threat exploits it
- **Pivot**: use an opportunity to escape a weakness
- **Monitor**: watch a threat that isn't yet urgent

> **GATE 3 — Recommendations review.**
> Present the cross-reference insights and recommendations. Ask: "Do these recommendations land? Ready to produce the final document?" Revise if needed, then proceed to output.

---

**Step 5 — Produce the output document**

Invoke the PDF skill to produce a formatted PDF containing:

1. **Cover**: subject name, date, purpose statement
2. **SWOT matrix**: four-quadrant table, 5–7 items per quadrant
3. **Cross-reference analysis**: SO/ST/WO/WT insights in prose or structured table
4. **Strategic recommendations**: numbered, with rationale and priority label
5. **Appendix** (optional): notes on assumptions, data sources, or time horizon

Save to `Resources/Output files/` using the naming convention: `[subject]_swot-analysis_v1.pdf`

---

## Failure Modes

- If the user provides insufficient context at Gate 1, ask targeted follow-up questions rather than guessing. A SWOT built on thin context is worse than useless.
- If web search returns no useful competitive or market data, proceed with what the user has supplied and note the gap in the output.
- If the PDF skill is unavailable, produce the analysis as a structured markdown file and save as `[subject]_swot-analysis_v1.md` instead.
- If the user skips a gate without confirming, prompt once: "Just confirming — happy to proceed with this as the basis?" Do not skip the confirmation silently.
