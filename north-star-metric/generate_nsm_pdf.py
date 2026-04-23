#!/usr/bin/env python3
"""Generate North Star Metric PDF for designer marketplace."""

import os
import subprocess
import sys
from datetime import date

# Ensure weasyprint is available
try:
    from weasyprint import HTML
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "weasyprint", "--break-system-packages"], check=True)
    from weasyprint import HTML

TODAY = date.today().strftime("%d %B %Y")

HTML_CONTENT = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 16px;
    color: #222;
    background: #fff;
    margin: 40px;
  }}

  /* ── HEADER ── */
  .header {{
    background: #1B2A4A;
    color: #fff;
    padding: 40px 44px 32px;
    border-radius: 6px;
    margin-bottom: 32px;
  }}
  .header h1 {{
    font-size: 28px;
    font-weight: 700;
    letter-spacing: -0.5px;
    margin-bottom: 6px;
  }}
  .header .subtitle {{
    font-size: 15px;
    color: #A8BBDA;
    font-weight: 400;
  }}

  /* ── SECTION HEADINGS ── */
  .section-heading {{
    font-size: 20px;
    font-weight: 700;
    color: #1B2A4A;
    margin-top: 36px;
    margin-bottom: 14px;
    padding-bottom: 6px;
    border-bottom: 2px solid #E8ECF2;
  }}

  /* ── BUSINESS GAME BADGE ── */
  .game-row {{
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 8px;
  }}
  .game-badge {{
    display: inline-block;
    background: #F5A623;
    color: #fff;
    font-weight: 700;
    font-size: 13px;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 6px 16px;
    border-radius: 20px;
  }}
  .game-rationale {{
    font-size: 15px;
    color: #444;
    line-height: 1.5;
  }}

  /* ── NSM HERO ── */
  .nsm-hero {{
    text-align: center;
    background: #F7F8FA;
    border: 2px solid #1B2A4A;
    border-radius: 8px;
    padding: 36px 40px 28px;
    margin: 16px 0 12px;
  }}
  .nsm-label {{
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #888;
    margin-bottom: 12px;
  }}
  .nsm-title {{
    font-size: 38px;
    font-weight: 700;
    color: #1B2A4A;
    line-height: 1.2;
    border-bottom: 4px solid #F5A623;
    display: inline-block;
    padding-bottom: 6px;
    margin-bottom: 20px;
  }}
  .nsm-rationale {{
    font-size: 15px;
    color: #444;
    line-height: 1.65;
    max-width: 640px;
    margin: 0 auto;
  }}

  /* ── CRITERIA TABLE ── */
  table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
    margin-top: 8px;
  }}
  thead tr {{
    background: #1B2A4A;
    color: #fff;
  }}
  thead th {{
    padding: 10px 14px;
    text-align: left;
    font-weight: 600;
  }}
  tbody tr:nth-child(odd)  {{ background: #F7F8FA; }}
  tbody tr:nth-child(even) {{ background: #ffffff; }}
  tbody td {{
    padding: 10px 14px;
    vertical-align: top;
    color: #333;
    line-height: 1.4;
  }}
  .check {{ color: #27AE60; font-weight: 700; }}
  .cross {{ color: #E74C3C; font-weight: 700; }}

  /* ── INPUT METRIC CARDS ── */
  .cards {{
    display: block;
    margin-top: 8px;
  }}
  .card {{
    background: #F7F8FA;
    border-left: 5px solid #F5A623;
    border-radius: 4px;
    padding: 18px 20px;
    margin-bottom: 14px;
  }}
  .card-name {{
    font-size: 16px;
    font-weight: 700;
    color: #1B2A4A;
    margin-bottom: 6px;
  }}
  .card-row {{
    font-size: 14px;
    color: #444;
    margin-bottom: 4px;
    line-height: 1.5;
  }}
  .card-row strong {{
    color: #1B2A4A;
    font-weight: 600;
  }}

  /* ── FOOTER ── */
  .footer {{
    margin-top: 40px;
    text-align: right;
    font-size: 12px;
    color: #AAA;
    border-top: 1px solid #E8ECF2;
    padding-top: 10px;
  }}
</style>
</head>
<body>

<!-- 1. HEADER -->
<div class="header">
  <h1>UX Designer Marketplace</h1>
  <div class="subtitle">North Star Metric Framework</div>
</div>

<!-- 2. BUSINESS GAME -->
<div class="section-heading">Business Game Classification</div>
<div class="game-row">
  <span class="game-badge">Transaction</span>
</div>
<p class="game-rationale">
  This platform creates value at the moment a design project is completed and payment is exchanged —
  the classic Transaction game — with a secondary Productivity dimension for designers managing their pipeline.
</p>

<!-- 3. NORTH STAR METRIC -->
<div class="section-heading">North Star Metric</div>
<div class="nsm-hero">
  <div class="nsm-label">North Star Metric</div>
  <div class="nsm-title">Projects Successfully Completed per Month</div>
  <p class="nsm-rationale">
    A "successfully completed project" is one where a startup receives and accepts delivered design work
    and the designer is paid. This single metric captures value for both sides of the marketplace: startups
    get the great design they came for; designers earn income; and the platform earns its 18% commission.
    It is a direct leading indicator of GMV and future revenue, reflects the mission ("make great design
    accessible to every startup"), and can be influenced by every function — product, growth, supply quality,
    and operations. Unlike GMV alone, it cannot be inflated by high-value but stalled projects, and unlike
    "projects posted" it confirms actual value delivery.
  </p>
</div>

<!-- 4. CRITERIA VALIDATION -->
<div class="section-heading">Criteria Validation</div>
<table>
  <thead>
    <tr>
      <th style="width:26%">Criterion</th>
      <th style="width:7%">Met?</th>
      <th>Justification</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Easy to Understand</td>
      <td class="check">✓</td>
      <td>Any team member can explain it: a completed project means a startup got its design and a designer was paid.</td>
    </tr>
    <tr>
      <td>Customer-Centric</td>
      <td class="check">✓</td>
      <td>Completion requires value delivery to the startup (the primary customer); it is not an internal activity metric.</td>
    </tr>
    <tr>
      <td>Sustainable Value</td>
      <td class="check">✓</td>
      <td>Recurring completions signal habitual use by startups and repeat earnings for designers, not one-off spikes.</td>
    </tr>
    <tr>
      <td>Vision Alignment</td>
      <td class="check">✓</td>
      <td>Each completed project is a concrete instance of great design becoming accessible to a startup — the mission in action.</td>
    </tr>
    <tr>
      <td>Quantitative</td>
      <td class="check">✓</td>
      <td>Countable integer per month; easily tracked in any data warehouse or ops dashboard.</td>
    </tr>
    <tr>
      <td>Actionable</td>
      <td class="check">✓</td>
      <td>Product can reduce friction, marketing can drive brief volume, ops can improve matching — all directly move completions.</td>
    </tr>
    <tr>
      <td>Leading Indicator</td>
      <td class="check">✓</td>
      <td>Monthly completions × average project value × 18% predicts near-term revenue; growth in completions precedes GMV growth.</td>
    </tr>
  </tbody>
</table>

<!-- 5. METRICS CONSTELLATION -->
<div class="section-heading">Metrics Constellation</div>
<div class="cards">

  <div class="card">
    <div class="card-name">1. Brief-to-Application Rate</div>
    <div class="card-row"><strong>What it measures:</strong> The share of posted briefs that receive at least one designer application within 48 hours.</div>
    <div class="card-row"><strong>How it drives the NSM:</strong> No applications = no match = no completion. A healthy application rate is the first gate to any completed project.</div>
    <div class="card-row"><strong>How to move it:</strong> Improve brief quality prompts, expand active designer supply, optimise notification and brief-discovery algorithms.</div>
  </div>

  <div class="card">
    <div class="card-name">2. Match-to-Kickoff Rate</div>
    <div class="card-row"><strong>What it measures:</strong> The share of startup–designer matches (accepted applications) that result in a project actually starting within 7 days.</div>
    <div class="card-row"><strong>How it drives the NSM:</strong> Matches that stall before kickoff never complete; reducing drop-off here directly lifts monthly completions.</div>
    <div class="card-row"><strong>How to move it:</strong> Streamline contract and payment setup, send automated kickoff nudges, surface clear next-step prompts post-match.</div>
  </div>

  <div class="card">
    <div class="card-name">3. Project Completion Rate</div>
    <div class="card-row"><strong>What it measures:</strong> The share of started projects that reach successful delivery and acceptance (no abandonment or dispute).</div>
    <div class="card-row"><strong>How it drives the NSM:</strong> This is the final conversion step; improving it has a 1-to-1 impact on the NSM.</div>
    <div class="card-row"><strong>How to move it:</strong> Provide milestone tracking tools, mediation support for disputes, designer vetting, and expectation-setting during onboarding.</div>
  </div>

  <div class="card">
    <div class="card-name">4. Active Designer Supply (Monthly)</div>
    <div class="card-row"><strong>What it measures:</strong> Number of designers who applied to at least one brief in the past 30 days.</div>
    <div class="card-row"><strong>How it drives the NSM:</strong> Thin supply causes unanswered briefs and slow matches; adequate supply is a prerequisite for completion volume.</div>
    <div class="card-row"><strong>How to move it:</strong> Designer acquisition campaigns, referral incentives, community building, and reducing time-to-first-earning for new designers.</div>
  </div>

  <div class="card">
    <div class="card-name">5. Startup Repeat-Brief Rate</div>
    <div class="card-row"><strong>What it measures:</strong> Share of startups that post a second brief within 60 days of completing their first project.</div>
    <div class="card-row"><strong>How it drives the NSM:</strong> Repeat customers compound monthly completions without additional acquisition cost, driving sustainable NSM growth.</div>
    <div class="card-row"><strong>How to move it:</strong> Post-project follow-up, satisfaction surveys, showcasing next-phase design needs, and loyalty discounts or credits.</div>
  </div>

</div>

<!-- 6. FOOTER -->
<div class="footer">Generated {TODAY} &nbsp;|&nbsp; North Star Metric Framework &nbsp;|&nbsp; UX Designer Marketplace</div>

</body>
</html>"""

# Output paths
paths = [
    "/Users/simonhuber/Documents/Claude workspace/Resources/Output files/designer-marketplace-north-star-metric_v1.pdf",
    "/Users/simonhuber/Library/Application Support/Claude/local-agent-mode-sessions/b7219776-2e00-4f54-a8a4-249ce28c97b2/baa53458-63d2-4ec5-88a8-3b38e4f1fe7e/local_96258873-fd4e-4156-ab9b-1959636816e6/outputs/north-star-metric-workspace/iteration-1/eval-2-marketplace/with_skill/outputs/north-star-metric.pdf",
]

# Create directories
for path in paths:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    print(f"Directory ensured: {os.path.dirname(path)}")

# Generate PDFs
html_obj = HTML(string=HTML_CONTENT)
for path in paths:
    html_obj.write_pdf(path)
    size = os.path.getsize(path)
    print(f"PDF written: {path} ({size:,} bytes)")

print("Done.")
