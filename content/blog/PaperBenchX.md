Title: PaperBenchX: Can AI Reproduce Science Across Disciplines?
Date: 2026-10-08
Summary: PaperBenchX evaluates whether AI agents can reconstruct published scientific experiments, execute domain-native software, and regenerate verifiable evidence across disciplines.
HeaderImage: /static/paperbenchx/cover/paperbenchx-scientist-cover.png
Layout: paperbenchx

<link rel="stylesheet" href="/static/paperbenchx/article-layout.css?v=20261007-contributors-13">
<link rel="stylesheet" href="/static/paperbenchx/leaderboard.css?v=20261030-logos">
<link rel="stylesheet" href="/static/paperbenchx/analysis.css">

<style>
:root {
  --pbx-ink: #171717;
  --pbx-soft: #525252;
  --pbx-muted: #737373;
  --pbx-line: #dedede;
  --pbx-paper: #ffffff;
  --pbx-wash: #f7f7f5;
  --pbx-green: #147d64;
  --pbx-green-light: #e8f5f0;
  --pbx-blue: #285f9e;
  --pbx-blue-light: #eaf1f8;
  --pbx-amber: #a45a08;
  --pbx-amber-light: #fff4dd;
  --pbx-red: #a63d40;
  --pbx-radius: 6px;
}

.markdown:has(.pbx-hero) { max-width: 100%; background: var(--pbx-paper); color: var(--pbx-ink); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
.pbx-cover-link { display: block; }
.pbx-cover-image { display: block; object-fit: contain; background: #fff; }
.pbx-cover-link:focus-visible { outline: 3px solid var(--pbx-blue); outline-offset: 4px; border-radius: 10px; }
@media (max-width: 820px) { .markdown:has(.pbx-hero) { width: 100%; } }

.pbx-hero {
  padding: 12px 0 30px;
  margin-bottom: 42px;
  border-bottom: 3px solid var(--pbx-ink);
}
.pbx-eyebrow {
  margin-bottom: 12px;
  color: var(--pbx-green);
  font-size: .78em;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0;
}
.pbx-hero h2 {
  max-width: 860px;
  margin: 0 0 18px;
  font-size: 2em;
  line-height: 1.2;
  letter-spacing: 0;
}
.pbx-lede {
  max-width: 860px;
  margin: 0 0 14px;
  color: var(--pbx-soft);
  font-size: 1.06em;
  line-height: 1.75;
}
.pbx-stats {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px;
  margin-top: 26px;
}
.pbx-stat {
  min-height: 112px;
  padding: 16px;
  border: 1px solid var(--pbx-line);
  border-top: 3px solid var(--pbx-green);
  border-radius: var(--pbx-radius);
  background: var(--pbx-paper);
  box-sizing: border-box;
}
.pbx-stat:nth-child(2) { border-top-color: var(--pbx-blue); }
.pbx-stat:nth-child(3) { border-top-color: var(--pbx-amber); }
.pbx-stat strong {
  display: block;
  margin-bottom: 5px;
  color: var(--pbx-ink);
  font-size: 1.85em;
  line-height: 1;
}
.pbx-stat span { color: var(--pbx-soft); font-size: .84em; line-height: 1.5; }
.pbx-opening-video { margin-top: 22px; }
.pbx-opening-video h3 { margin: 0 0 10px; font-size: 1em; }
#pbx-video-status:empty { display: none; }

.pbx-section { margin: 48px 0; scroll-margin-top: 24px; }
.pbx-kicker {
  margin-bottom: 5px;
  color: var(--pbx-green);
  font-size: .78em;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0;
}
.pbx-title {
  margin: 0 0 14px;
  padding-left: 12px;
  border-left: 4px solid var(--pbx-green);
  color: var(--pbx-ink);
  font-size: 1.55em;
  letter-spacing: 0;
}
.pbx-copy { color: #333; font-size: .98em; line-height: 1.8; }
.pbx-copy strong { color: var(--pbx-ink); }
.pbx-callout {
  margin: 22px 0;
  padding: 16px 18px;
  border: 1px solid #bcded2;
  border-left: 4px solid var(--pbx-green);
  border-radius: var(--pbx-radius);
  background: var(--pbx-green-light);
  color: #234139;
  font-size: .94em;
  line-height: 1.75;
}
.pbx-warning {
  margin: 18px 0;
  padding: 14px 16px;
  border: 1px solid #efd5a7;
  border-left: 4px solid var(--pbx-amber);
  border-radius: var(--pbx-radius);
  background: var(--pbx-amber-light);
  color: #624017;
  font-size: .9em;
  line-height: 1.7;
}

.pbx-compare {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin: 22px 0;
}
.pbx-panel {
  padding: 18px;
  border: 1px solid var(--pbx-line);
  border-radius: var(--pbx-radius);
  background: var(--pbx-paper);
}
.pbx-panel.old { border-top: 3px solid var(--pbx-muted); }
.pbx-panel.new { border-top: 3px solid var(--pbx-green); }
.pbx-panel h3 { margin: 0 0 10px; font-size: 1em; letter-spacing: 0; }
.pbx-panel ul { margin: 0; padding-left: 20px; color: var(--pbx-soft); font-size: .88em; line-height: 1.75; }

.pbx-flow {
  display: grid;
  grid-template-columns: repeat(5, minmax(0, 1fr));
  gap: 24px;
  margin: 24px 0 12px;
}
.pbx-step {
  position: relative;
  min-height: 116px;
  padding: 14px 12px;
  border: 1px solid var(--pbx-line);
  border-top: 3px solid var(--pbx-blue);
  border-radius: var(--pbx-radius);
  background: var(--pbx-paper);
  box-sizing: border-box;
}
.pbx-step:not(:last-child)::after {
  content: '\2192';
  position: absolute;
  top: 42px;
  right: -21px;
  color: var(--pbx-muted);
  font-size: 1.15em;
  font-weight: 700;
}
.pbx-step b { display: block; margin-bottom: 7px; font-size: .86em; }
.pbx-step span { display: block; color: var(--pbx-soft); font-size: .76em; line-height: 1.55; }
.pbx-caption { margin-top: 10px; color: var(--pbx-muted); font-size: .8em; line-height: 1.6; text-align: center; }

.pbx-table-wrap { overflow-x: auto; margin: 20px 0; border: 1px solid var(--pbx-line); border-radius: var(--pbx-radius); }
.pbx-table { width: 100%; min-width: 760px; margin: 0; border-collapse: collapse; font-size: .86em; }
.pbx-table th, .pbx-table td { padding: 10px 12px; border-bottom: 1px solid var(--pbx-line); text-align: left; vertical-align: top; }
.pbx-table th { background: var(--pbx-wash); color: var(--pbx-soft); font-weight: 700; }
.pbx-table tbody tr:last-child td { border-bottom: 0; }
.pbx-table td:nth-child(2), .pbx-table th:nth-child(2) { text-align: center; }
.pbx-task { color: var(--pbx-ink); font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: .92em; }
.pbx-status {
  display: inline-block;
  white-space: nowrap;
  padding: 3px 7px;
  border-radius: 4px;
  background: var(--pbx-green-light);
  color: var(--pbx-green);
  font-size: .78em;
  font-weight: 700;
}
.pbx-status.pending { background: var(--pbx-amber-light); color: var(--pbx-amber); }
.pbx-status.remediation { background: #f6e9e9; color: var(--pbx-red); }

.pbx-capabilities {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 10px;
  margin: 22px 0;
}
.pbx-capability {
  min-height: 100px;
  padding: 13px 14px;
  border: 1px solid var(--pbx-line);
  border-left: 3px solid var(--pbx-blue);
  border-radius: var(--pbx-radius);
  background: var(--pbx-paper);
  box-sizing: border-box;
}
.pbx-capability small { display: block; margin-bottom: 7px; color: var(--pbx-green); font-family: 'Space Mono', monospace; font-size: .62em; font-weight: 700; text-transform: uppercase; }
.pbx-capability b { display: block; margin-bottom: 7px; font-size: .86em; line-height: 1.45; }
.pbx-capability span { color: var(--pbx-soft); font-size: .78em; line-height: 1.55; }

.pbx-example {
  margin: 24px 0;
  padding: 20px;
  border: 1px solid var(--pbx-line);
  border-top: 4px solid var(--pbx-green);
  border-radius: var(--pbx-radius);
  background: var(--pbx-paper);
}
.pbx-example h3 { margin: 0 0 8px; font-size: 1.08em; letter-spacing: 0; }
.pbx-example .meta { margin-bottom: 16px; color: var(--pbx-muted); font-size: .82em; }
.pbx-example ol { margin: 0; padding-left: 22px; color: #333; font-size: .9em; line-height: 1.75; }

.pbx-demo-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px;
  margin: 22px 0;
}
.pbx-demo-card {
  display: block;
  overflow: hidden;
  border: 1px solid var(--pbx-line);
  border-radius: var(--pbx-radius);
  background: var(--pbx-paper);
  color: var(--pbx-ink);
  box-sizing: border-box;
  text-decoration: none !important;
}
.pbx-demo-card:hover, .pbx-demo-card[aria-current="true"] { border-color: var(--pbx-green); box-shadow: inset 0 -3px var(--pbx-green); }
.pbx-demo-card:focus-visible, .pbx-action:focus-visible { outline: 3px solid var(--pbx-blue); outline-offset: 4px; }
.markdown .pbx-demo-card img { display: block; width: 100%; aspect-ratio: 16 / 9; object-fit: cover; border-radius: 0; }
.pbx-demo-card .pbx-card-copy { display: block; padding: 12px; }
.pbx-demo-card b { display: block; margin: 4px 0 7px; font-size: .86em; line-height: 1.4; }
.pbx-demo-card small { display: block; color: var(--pbx-soft); font-size: .75em; line-height: 1.6; }
.pbx-demo-card .pbx-card-area { color: var(--pbx-green); font-size: .7em; font-weight: 700; }
.pbx-demo-unavailable { padding: 18px; background: var(--pbx-wash); }
.pbx-player-frame { display: block; width: 100%; aspect-ratio: 16 / 9; border: 0; background: #111; }
.pbx-player { overflow: hidden; border: 1px solid var(--pbx-line); border-radius: var(--pbx-radius); background: var(--pbx-wash); scroll-margin-top: 24px; }
.pbx-player-copy { padding: 16px 18px; }
.pbx-player-copy h3 { margin: 0 0 8px; }
.pbx-player-copy p { margin: 8px 0; font-size: .85em; line-height: 1.65; }
.pbx-video-player { object-fit: contain; }
#latest-videos { scroll-margin-top: 24px; }
.pbx-actions, .pbx-toc { display: flex; flex-wrap: wrap; gap: 10px; margin: 18px 0; }
.pbx-action { display: inline-block; padding: 9px 13px; border: 1px solid var(--pbx-line); border-radius: var(--pbx-radius); background: var(--pbx-paper); color: var(--pbx-green); font-size: .82em; font-weight: 600; text-decoration: none !important; }
.pbx-toc a { margin-left: 0; color: var(--pbx-soft); font-size: .82em; }
.pbx-question { padding-top: 12px; border-top: 1px solid var(--pbx-line); color: var(--pbx-green); font-size: .9em; line-height: 1.7; }
.pbx-source-list { padding-left: 20px; color: var(--pbx-soft); font-size: .85em; line-height: 1.8; }
.pbx-paper-figure { margin: 26px 0; padding: 16px; border: 1px solid var(--pbx-line); border-radius: var(--pbx-radius); background: #fff; }
.markdown .pbx-paper-figure img { display: block; width: 100%; height: auto; margin: 0; }
.pbx-paper-figure figcaption { margin-top: 12px; color: var(--pbx-soft); font-size: .78em; line-height: 1.65; }
.pbx-takeaway { margin: 24px 0; padding: 22px; border-left: 5px solid var(--pbx-green); background: var(--pbx-green-light); }
.pbx-takeaway strong { color: var(--pbx-green); font-size: 1.35em; }
.pbx-takeaway p { margin: 10px 0 0; line-height: 1.75; }
.pbx-steps { display: grid; gap: 14px; padding: 0; list-style: none; counter-reset: pbx-step; }
.pbx-steps li { position: relative; padding: 18px 18px 18px 62px; border: 1px solid var(--pbx-line); border-radius: var(--pbx-radius); color: var(--pbx-soft); font-size: .93em; line-height: 1.75; counter-increment: pbx-step; }
.pbx-steps li::before { content: counter(pbx-step); position: absolute; top: 18px; left: 18px; display: grid; place-items: center; width: 28px; height: 28px; border-radius: 50%; background: var(--pbx-green-light); color: var(--pbx-green); font-weight: 700; }
.pbx-steps strong { display: block; color: var(--pbx-ink); }
.pbx-disclosure { margin: 18px 0; padding: 14px 18px; border: 1px solid var(--pbx-line); border-radius: var(--pbx-radius); }
.pbx-disclosure summary { cursor: pointer; color: var(--pbx-green); font-weight: 650; }
.pbx-disclosure summary:focus-visible { outline: 3px solid var(--pbx-blue); outline-offset: 4px; }
.pbx-result-table td:not(:first-child), .pbx-result-table th:not(:first-child) { text-align: right; font-variant-numeric: tabular-nums; }
.pbx-result-table tbody tr:first-child { background: var(--pbx-green-light); }
.pbx-metric-formula { color: var(--pbx-green); font-family: ui-monospace, monospace; font-size: 1.15em; }
.pbx-chart-link { display: block; }
.pbx-note { color: var(--pbx-muted); font-size: .82em; line-height: 1.7; }
.pbx-evidence-chain { display: flex; flex-wrap: wrap; align-items: center; gap: 8px; margin: 20px 0; padding: 16px; border: 1px solid var(--pbx-line); background: var(--pbx-wash); border-radius: var(--pbx-radius); font-size: .82em; line-height: 1.7; }
.pbx-evidence-chain span:not([aria-hidden]) { color: var(--pbx-green); font-weight: 650; }

.pbx-conclusion {
  margin-top: 24px;
  padding: 20px;
  border: 2px solid var(--pbx-ink);
  border-left: 6px solid var(--pbx-green);
  border-radius: var(--pbx-radius);
  color: var(--pbx-ink);
  font-size: 1em;
  line-height: 1.8;
}
.pbx-draft-note {
  margin-top: 42px;
  padding-top: 16px;
  border-top: 1px solid var(--pbx-line);
  color: var(--pbx-muted);
  font-size: .8em;
  line-height: 1.6;
}

@media (max-width: 760px) {
  .pbx-stats, .pbx-capabilities { grid-template-columns: 1fr; }
  .pbx-demo-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .pbx-compare { grid-template-columns: 1fr; }
  .pbx-flow { grid-template-columns: 1fr; gap: 10px; }
  .pbx-step { min-height: 0; }
  .pbx-step:not(:last-child)::after { display: none; }
  .pbx-hero h2 { font-size: 1.55em; }
}
@media (max-width: 480px) { .pbx-demo-grid { grid-template-columns: 1fr; } }
@media (max-width: 640px) {
  .site-header .header-content { gap: 12px; }
  .site-header nav { display: flex; flex-wrap: wrap; justify-content: flex-end; gap: 8px 12px; min-width: 0; }
  .site-header nav a { margin-left: 0; }
  .detail-hero:has(.pbx-cover-image) { grid-template-columns: 96px minmax(0, 1fr); gap: 12px; align-items: start; }
  .detail-hero .pbx-cover-image { height: 96px; }
  .detail-hero:has(.pbx-cover-image) h1 { font-size: 1.15em; line-height: 1.35; }
  .detail-hero:has(.pbx-cover-image) .muted { font-size: .72em; }
}
</style>
<section class="pbx-hero" id="overview" aria-labelledby="overview-heading">
<div class="pbx-eyebrow">01 / Overview</div>
<h2 id="overview-heading">Can AI reproduce published scientific results?</h2>
<div class="pbx-intro-grid">
<p class="pbx-lede"><strong class="pbx-key">Reproducibility is a defining feature of science.</strong> Before an AI system can be trusted to discover something new, it should be able to reconstruct and verify what science already knows. PaperBenchX tests this demanding middle ground: the target claim is known, but the agent must turn an incomplete scientific description into an executable experiment and produce evidence that another researcher can independently regenerate.</p>
<figure class="pbx-intro-figure"><a class="pbx-chart-link" href="/static/paperbenchx/paper/fig_task_inventory_93.png?v=20261006" target="_blank" rel="noopener" aria-label="Enlarge the PaperBenchX task distribution figure"><img alt="PaperBenchX contains 93 tasks across twelve research areas in six scientific domains" width="2304" height="2130" decoding="async" src="/static/paperbenchx/paper/fig_task_inventory_93.png?v=20261006"/></a><figcaption>93 paper-reproduction tasks across 12 research areas and six scientific domains.</figcaption></figure>
</div>
<div class="pbx-stats pbx-opening-stats" aria-label="PaperBenchX at a glance">
<div class="pbx-stat"><strong>93</strong><span>Paper-reproduction<br/>tasks</span></div>
<div class="pbx-stat"><strong>12</strong><span>Research<br/>areas</span></div>
<div class="pbx-stat"><strong>10</strong><span>Domain-native<br/>environments</span></div>
<div class="pbx-stat"><strong>3,168</strong><span>Scorable rubric<br/>criteria</span></div>
</div>
<p class="pbx-note">The tasks draw on 93 papers from 44 publication venues. Agent time limits range from 4 to 24 hours, with a median of 7 hours.</p>
<section class="pbx-opening-video" id="latest-videos" aria-label="PaperBenchX scientific reproduction film">
<div class="pbx-player" id="pbx-video-player">
<video class="pbx-player-frame pbx-video-player" id="pbx-active-video" controls="" loop="" muted="" playsinline="" preload="metadata" poster="/static/paperbenchx/videos/ideo-poster.png" src="/static/paperbenchx/videos/ideo.mov" aria-label="PaperBenchX scientific reproduction workflows">Your browser does not support embedded video. <a href="/static/paperbenchx/videos/ideo.mov">Open the overview film.</a></video>
</div>
<p class="pbx-note" id="pbx-video-status" role="status"></p>
</section>
<div class="pbx-actions"><a class="pbx-action" href="#results">Explore the results</a><a class="pbx-action" href="#protocol">How evaluation works</a></div>
</section>

<section class="pbx-section" id="why-paperbenchx">
<div class="pbx-kicker">02 / Why scientific reproduction?</div>
<h2 class="pbx-title">A common interface does not make the science uniform.</h2>
<p class="pbx-copy">PaperBenchX gives every task the same outer contract: a paper, public instructions, a configured environment, and a runnable submission entry point. That standardizes how an agent starts and how its work is delivered. It does not supply the missing scientific decisions needed to reproduce the result.</p>
<p class="pbx-copy">Inside that shared interface, the work changes substantially across HFSS, Meep, electronic-structure codes, data-analysis pipelines, and embodied simulators. Geometry, boundary conditions, physical models, numerical tolerances, convergence behavior, and result extraction determine what experiment was actually performed. A command can finish successfully and still model the wrong system or support the wrong claim.</p>
<div class="pbx-capabilities">
<div class="pbx-capability"><small>01 / Modeling</small><b>What experiment did the paper perform?</b><span>Translate prose, equations, and figures into the correct model, assumptions, parameters, and target observable.</span></div>
<div class="pbx-capability"><small>02 / Execution</small><b>Did the scientific computation work?</b><span>Operate specialized software, interpret diagnostics, and determine whether a run is complete, stable, and converged.</span></div>
<div class="pbx-capability"><small>03 / Validation</small><b>Does the evidence support the claim?</b><span>Regenerate the required artifacts and verify that they arise from the intended workflow rather than a plausible-looking shortcut.</span></div>
</div>
<p class="pbx-callout"><strong>The benchmark evaluates three connected stages:</strong> Modeling recovers the intended experiment, Execution runs it in its native environment, and Validation tests the regenerated evidence. Passing only one stage is not a successful reproduction.</p>
</section>

<section class="pbx-section" id="protocol">
<div class="pbx-kicker">03 / Inside a task</div>
<h2 class="pbx-title">What does a PaperBenchX task look like?</h2>
<p class="pbx-copy">Scientific correctness cannot be established from an agent's final report alone. PaperBenchX therefore combines <strong class="pbx-key">clean replay, evidence-based grading, and hierarchical scoring</strong> to test whether a submitted procedure regenerates evidence that supports the target claim—not merely a plausible-looking number.</p>
<figure class="pbx-paper-figure" id="replay-workflow">
<a class="pbx-chart-link" href="/static/paperbenchx/paper/task.png?v=20261006" target="_blank" rel="noopener" aria-label="Open the task submission and clean replay diagram at full resolution"><img src="/static/paperbenchx/paper/task.png?v=20261006" width="3890" height="1920" loading="lazy" decoding="async" alt="PaperBenchX task inputs, agent submission, clean replay, and private evidence-based evaluation"/></a>
<figcaption><strong>Task inputs → agent submission → clean replay → rubric evaluation.</strong> The Brewster criteria, pass/fail marks, and 24.5% outcome illustrate grading, not a measured result or a universal pass rule. Platform logos are examples, not a complete inventory. Click to enlarge.</figcaption>
</figure>
<ol class="pbx-evaluation-questions">
<li><h3>Task inputs — define what must be reproduced</h3><p>The paper, instructions, and addendum specify the scientific target, required methods, permitted alternatives, and evidence to deliver. <strong>Private grading must assess stated obligations, not introduce hidden requirements.</strong></p></li>
<li><h3>Agent submission — hand over the experiment</h3><p>The agent submits source code, configuration, permitted inputs, and a runnable <code>reproduce.sh</code>. The package must regenerate the required outputs; a report or a folder of saved figures cannot replace the workflow that produced them.</p></li>
<li><h3>Clean replay — establish where the evidence came from</h3><p>Remove generated outputs and stale state, then run the submitted workflow again. The protocol requires isolation, blocked network access, and task-specific limits. Admissible outputs are frozen for grading, so surviving files from the agent's earlier session do not count as regenerated evidence. Replay regenerates the evidence; rubric evaluation tests whether it supports the scientific claim.</p></li>
<li><h3>Rubric evaluation — test each scientific claim</h3><p>Each rubric item is evaluated using one of two methods: deterministic checks for directly verifiable numerical or structural properties, or LLM-based evaluation for items requiring scientific interpretation and judgment. <strong>GPT-5.6-Sol</strong> serves as the shared LLM judge across all agent configurations.</p>
<section class="pbx-score-summary" id="score-summary" aria-labelledby="score-summary-heading">
<h4 id="score-summary-heading">Rubrics and scoring</h4>
<div class="pbx-score-visual">
<figure class="pbx-score-tree">
<img src="/static/paperbenchx/rubric-scoring-tree.svg?v=20260922-scoring-tree" width="320" height="160" loading="lazy" decoding="async" alt="Illustrative rubric tree: evidence-backed criterion scores between 0 and 1 combine through requirement groups into task score R = Σ wᵢsᵢ. Effective weights reflect scientific importance and sum to 1; branches and weights vary by task."/>
<figcaption>Illustrative tree · task-specific weights</figcaption>
</figure>
<dl class="pbx-score-metrics">
<div><dt>Full rate <span class="pbx-score-threshold">R &gt; 0.90</span></dt><dd>Fraction of the 93 tasks strictly above the threshold.<small>A score of exactly 0.90 does not qualify.</small></dd></div>
<div><dt>Partial score</dt><dd>Mean task score across the same fixed set of 93 tasks.<small>Missing outcomes count as zero.</small></dd></div>
</dl>
</div>
</section>
</li>
</ol>
</section>

<section class="pbx-section" id="construction">
<div class="pbx-kicker">04 / Task construction</div>
<h2 class="pbx-title">From papers to reproduction tasks</h2>
<p class="pbx-copy">Turning a paper into a benchmark task requires more than extracting a target number. Each task begins with a verifiable scientific claim and passes through two stages. In <strong class="pbx-key">Build</strong>, a domain expert selects the claim, fixes the scope and conditions, provisions the native environment, writes the public task contract, and completes a private reference workflow. In <strong class="pbx-key">Validate and Review</strong>, the expert defines evidence-backed rubric leaves, reruns the reference workflow from a clean environment, calibrates the scoring on valid and invalid submissions, and sends the task through independent review.</p>
<figure class="pbx-paper-figure" id="task-construction"><a class="pbx-chart-link" href="/static/paperbenchx/paper/task_construct.png?v=20261007-3" rel="noopener" target="_blank" aria-label="Open the task construction diagram at full resolution"><img alt="The PaperBenchX two-stage task construction pipeline, from selecting a published claim to clean reference replay, calibration and independent expert review" width="5281" height="1898" loading="lazy" decoding="async" src="/static/paperbenchx/paper/task_construct.png?v=20261007-3"/></a><figcaption><strong>Build, then validate and review.</strong> Tasks that fail because of scope, environment, or reference execution return to the build stage; scoring problems return to rubric construction. Two independent domain experts review the scientific scope, fairness, reproducibility, evidence requirements, and scoring behavior before a task is frozen.</figcaption></figure>
<p class="pbx-copy">This process produced 93 tasks with 3,168 scorable criteria, a median of 38 per task. The environment is part of the scientific task itself: model representations, numerical conventions, convergence evidence, and execution procedures differ across software.</p>
</section>

<section class="pbx-section" id="results">
<div class="pbx-kicker">05 / Leaderboard</div>
<h2 class="pbx-title">How do current agents compare?</h2>
<p class="pbx-copy">Across ten frontier agent configurations, the strongest system fully reproduces only <strong class="pbx-key">13 of 93 tasks</strong> under the strict 90% threshold, a <strong class="pbx-key">13.98% Full rate</strong>. Its Partial score reaches 59.08%, but the large gap between partial and full completion shows that substantial progress rarely closes the full loop from paper understanding to reproducible scientific evidence.</p>
<div class="pbx-stats" aria-label="Headline PaperBenchX results">
<div class="pbx-stat"><strong>13.98%</strong><span>Best Full rate<br/>13 of 93 tasks</span></div>
<div class="pbx-stat"><strong>59.08%</strong><span>Best Partial score<br/>GPT-6-Astra</span></div>
<div class="pbx-stat"><strong>71</strong><span>Tasks never fully<br/>reproduced</span></div>
</div>
<div class="pbx-leaderboard" id="pbx-leaderboard">
<div class="pbx-ranking-card-head">
<div><h3>Overall leaderboard</h3><p>Every configuration is evaluated on the same fixed set of 93 tasks.</p></div>
<span>10 agents · 93 tasks</span>
</div>
<div class="pbx-leaderboard-tabs" role="tablist" aria-label="Leaderboard views">
<button type="button" role="tab" id="pbx-leaderboard-tab-full" data-leaderboard-view="full" aria-selected="true" aria-controls="pbx-leaderboard-panel-full"><span>01</span><strong>Full reproduction</strong><small>Strict task completion</small></button>
<button type="button" role="tab" id="pbx-leaderboard-tab-partial" data-leaderboard-view="partial" aria-selected="false" aria-controls="pbx-leaderboard-panel-partial" tabindex="-1"><span>02</span><strong>Partial &amp; process</strong><small>Stages and interaction effort</small></button>
</div>
<div id="pbx-leaderboard-panel-full" role="tabpanel" aria-labelledby="pbx-leaderboard-tab-full">
<figure class="pbx-paper-ranking" aria-labelledby="pbx-paper-ranking-caption">
<div class="pbx-chart-legend" aria-label="Chart legend"><span><i class="pbx-legend-full"></i>Full Score</span><span><i class="pbx-legend-partial">x.x%</i>Partial Score</span></div>
<div class="pbx-paper-ranking-scroll" role="region" tabindex="0" aria-label="Interactive model performance chart; scroll horizontally on narrow screens">
<div class="pbx-paper-chart">
<div class="pbx-chart-y-title">Performance (%)</div>
<div class="pbx-chart-axis" aria-hidden="true"><span style="--tick: 60">60%</span><span style="--tick: 40">40%</span><span style="--tick: 20">20%</span><span style="--tick: 0">0%</span></div>
<div class="pbx-chart-plot" id="pbx-ranking-chart" aria-label="Model leaderboard"></div>
</div>
</div>
<p class="pbx-ranking-readout" id="pbx-ranking-readout" role="status" aria-live="polite">Hover, focus, or select a model to compare its Full and Partial scores.</p>
<figcaption id="pbx-paper-ranking-caption">Bars show Full scores (&gt;90%); boxes show Partial scores.</figcaption>
</figure>
</div>
<div id="pbx-leaderboard-panel-partial" role="tabpanel" aria-labelledby="pbx-leaderboard-tab-partial" hidden>
<div class="pbx-process-head"><div><h4>Partial score and process profile</h4><p>Each model keeps its Full-view color; shade separates the three stages.</p></div><div class="pbx-process-legend" aria-label="Stage color shades"><span><i data-stage="modeling"></i>Modeling</span><span><i data-stage="execution"></i>Execution</span><span><i data-stage="validation"></i>Validation</span></div></div>
<div class="pbx-process-scroll" role="region" tabindex="0" aria-label="Partial score, stage scores, and average interaction turns by model; scroll horizontally on narrow screens">
<div class="pbx-process-chart-layout">
<div class="pbx-stage-y-title">Stage score (%)</div>
<div class="pbx-stage-axis" aria-hidden="true"><span>100%</span><span>75%</span><span>50%</span><span>25%</span><span>0%</span></div>
<div class="pbx-stage-plot" id="pbx-process-chart" aria-label="Partial score and stage profile by model"></div>
</div>
</div>
<p class="pbx-process-readout" id="pbx-process-readout" role="status" aria-live="polite">Select a model to inspect the gap between scientific setup, execution, and validation.</p>
<p class="pbx-process-note"><strong>Stage scores diagnose where rubric credit is earned.</strong> Average turns describe interaction effort and are not part of the scientific score; more turns do not necessarily mean better reproduction.</p>
</div>
<div class="pbx-ranking-meta"><span id="pbx-ranking-status" role="status" aria-live="polite">Loading the leaderboard…</span></div>
<details class="pbx-ranking-methods"><summary>How to read these rankings</summary>
<p><strong>Full</strong> is the fraction of tasks scoring strictly above 90%; a score of exactly 90% does not qualify. <strong>Partial</strong> averages rubric scores over the fixed 93-task set and captures supported progress on incomplete reproductions. Missing outcomes count as zero in both views.</p>
<p>Every configuration is compared on the same task denominator. Ties use unrounded scores, and all submissions are evaluated through clean replay with the same scientific rubric evaluator and deterministic checks.</p>
</details>
<section class="pbx-difficulty-section" aria-labelledby="pbx-difficulty-heading">
<div class="pbx-difficulty-heading"><div><h3 id="pbx-difficulty-heading">Research-area difficulty</h3><p>Hardest to easiest for the evaluated ten-model cohort</p></div><span>12 research areas</span></div>
<div class="pbx-difficulty-chart" id="pbx-difficulty-chart" aria-label="Research areas ranked by difficulty"></div>
<p class="pbx-difficulty-readout" id="pbx-difficulty-readout" role="status">Select a research area to inspect its cross-model mean Partial score.</p>
<p class="pbx-difficulty-note"><strong>Difficulty = 100 − cross-model mean Partial score.</strong> This is a comparative result for the evaluated cohort, not an intrinsic property of the papers.</p>
</section>
<noscript><p class="pbx-note">Enable JavaScript to view the interactive leaderboard and research-area difficulty ranking.</p></noscript>
</div>
</section>

<section class="pbx-section" id="failure-modes">
<div class="pbx-kicker">06 / Analysis</div>
<h2 class="pbx-title">What separates partial progress from reliable reproduction?</h2>
<p class="pbx-copy">The overall score shows who performs better; the three views below explain where the difference comes from. Read them together, then hover or focus on a mark for its exact value.</p>
<figure class="pbx-analysis-explorer" id="analysis-diagnostics" aria-labelledby="pbx-analysis-explorer-title">
<div class="pbx-analysis-explorer-head">
<div><h3 id="pbx-analysis-explorer-title">Three questions behind the score</h3><p>Stage performance, interaction efficiency, and workflow allocation</p></div>
</div>
<div class="pbx-analysis-grid">
<section class="pbx-analysis-panel" id="pbx-analysis-panel-stages" aria-label="Where does credit drop?"></section>
<section class="pbx-analysis-panel" id="pbx-analysis-panel-effort" aria-label="Do more turns help?"></section>
<section class="pbx-analysis-panel" id="pbx-analysis-panel-time" aria-label="Where does time go?"></section>
</div>
<figcaption>Stage performance, interaction length, and workflow allocation.</figcaption>
<div class="pbx-chart-tooltip" id="pbx-analysis-tooltip" role="status" aria-live="polite" hidden></div>
</figure>
<div class="pbx-analysis-list">
<section><span>01</span><div><h3>The main drop appears at scientific validation.</h3><p>Modeling and Execution reach median scores of 73.4% and 73.5%, while Validation falls to 40.0%. Even among 304 outcomes with at least 80% in both upstream stages, only 53 cross the full-reproduction threshold. Agents often build and run much of an experiment without closing the evidentiary loop.</p></div></section>
<section><span>02</span><div><h3>More interaction does not reliably produce a better result.</h3><p>Fable 5.1 and Fable 5 reach about 58% Partial score in roughly 113 turns. GPT-6-Astra reaches 59.08% in 348.7 turns, while DeepSeek-V4.1-Flash uses 372.6 turns for 45.47%. The weakly negative correlation (<em>r</em> = −0.14) suggests that long trajectories often reflect recovery attempts or continued work on a mis-specified experiment.</p></div></section>
<section><span>03</span><div><h3>Most time is spent executing, but success is decided upstream.</h3><p>Native software consumes 51.8–63.3% of tool-mediated time. On the F-stub antenna task, however, Fable 5 recovers more of the required scientific evidence in 159 turns than GPT-6-Astra or HY3 do in 464 and 390 turns. Correct modeling, parameter choices, and intermediate checks determine whether expensive computation becomes useful evidence.</p></div></section>
<section><span>04</span><div><h3>Stage-aware scoring distinguishes different kinds of failure.</h3><p>A run can complete yet support the wrong conclusion because its modes, ports, parameters, mechanism, or result extraction are incorrect. The LNOI edge-coupler result illustrates this separation: GPT-6-Astra receives full Execution credit but only 41.9% in Validation. Clean replay and stage scores distinguish an execution failure from an unsupported scientific claim.</p></div></section>
</div>
</section>

<section class="pbx-section" id="data-release">
<div class="pbx-kicker">07 / Data release</div>
<h2 class="pbx-title">12 open tasks, 81 held-out tasks</h2>
<p class="pbx-copy">PaperBenchX releases one representative task from each research area: <strong class="pbx-key">12 open tasks</strong> that the community can run, inspect, and use to study the strengths and limitations of research agents. The remaining <strong class="pbx-key">81 tasks</strong> are maintained as a held-out evaluation set with controlled access, limiting benchmark contamination while preserving long-term measurement value.</p>

<div class="pbx-release-split" aria-label="Open and held-out PaperBenchX tasks">
<section><strong>12</strong><h3>Open tasks</h3><p>Run the tasks, inspect the evaluation method, debug reproduction workflows, and examine how individual scientific requirements become scores.</p></section>
<section><strong>81</strong><h3>Held-out tasks</h3><p>Retained for continuing evaluation of future agents, helping PaperBenchX preserve discrimination as systems improve.</p></section>
</div>

<h3 class="pbx-release-heading">What the open release provides</h3>
<p class="pbx-copy">The release includes task instructions, scoring details, and the resources required for evaluation. Scientific software licensing determines how each environment is distributed:</p>
<div class="pbx-environment-split">
<section><span>9 tasks</span><h3>Redistributable environments</h3><p>Complete open-source scientific computing environments are provided and can be run directly.</p></section>
<section><span>3 tasks</span><h3>Licensed environments</h3><p>For tasks that depend on commercial software, we release the task instructions, scoring details, environment setup guidance, and unified evaluation framework. Researchers can configure and run the environment after obtaining a valid license.</p></section>
</div>
<p class="pbx-copy pbx-release-link"><a href="https://github.com/UniPat-AI/PaperBenchX" target="_blank" rel="noopener">Explore the open PaperBenchX tasks and evaluation resources on GitHub →</a></p>
</section>
<section class="pbx-section" id="open-release">
<div class="pbx-kicker">08 / Toward a general AI scientist</div>
<h2 class="pbx-title">Reliable reproduction is a foundation for new science.</h2>
<p class="pbx-copy pbx-frontier-lede"><strong class="pbx-key">PaperBenchX makes that foundation measurable.</strong> Agents already make partial progress in Modeling and Execution, yet the strongest configuration fully reproduces only 13.98% of tasks. A substantial gap remains between reading a paper, operating scientific software, and regenerating evidence that supports its claims.</p>
<div class="pbx-frontier-map" aria-label="Capability path from reproducing known science to autonomous scientific discovery">
<div class="pbx-frontier-scopes" aria-hidden="true"><span>Measured by PaperBenchX</span><span>Beyond reproduction</span></div>
<div class="pbx-frontier-steps">
<section class="pbx-frontier-step is-measured"><small>Measured by PaperBenchX</small><span>01</span><h3>Modeling</h3><p>Recover the intended model, assumptions, and experiment.</p></section>
<section class="pbx-frontier-step is-measured"><small>Measured by PaperBenchX</small><span>02</span><h3>Execution</h3><p>Operate domain-native tools and diagnose the computation.</p></section>
<section class="pbx-frontier-step is-measured"><small>Measured by PaperBenchX</small><span>03</span><h3>Validation</h3><p>Regenerate evidence and test whether it supports the claim.</p></section>
<section class="pbx-frontier-step is-next"><small>Beyond reproduction</small><span>04</span><h3>Form hypotheses</h3><p>Identify open questions and prioritize ideas worth testing.</p></section>
<section class="pbx-frontier-step is-next"><small>Beyond reproduction</small><span>05</span><h3>Discover</h3><p>Design informative tests and revise beliefs with new evidence.</p></section>
</div>
</div>
<div class="pbx-frontier-notes" id="discussion">
<section><small>What PaperBenchX contributes</small><h3>A measurable first step</h3><p>The benchmark turns gaps in cross-disciplinary reproduction into evidence that can guide improvement. Reproduction is not discovery, but it provides a verifiable checkpoint on the path toward it.</p></section>
<section><small>What lies beyond</small><h3>From computation to physical feedback</h3><p>PaperBenchX currently focuses on scientific tasks that can be completed on a computer. Extending this direction to wet-lab research would require agents to design experiments, act safely in the physical world, learn from observations, and revise hypotheses when evidence disagrees.</p></section>
</div>
<p class="pbx-frontier-closing">PaperBenchX makes reliable scientific reproduction a measurable step toward more autonomous scientific research.</p>
</section>

<section class="pbx-section pbx-contributors" id="contributors" aria-labelledby="pbx-contributors-heading">
<div class="pbx-kicker">09 / Contributors</div>
<h2 class="pbx-title" id="pbx-contributors-heading">Contributors</h2>
<div class="pbx-contributors-box">
<div class="pbx-contributor-list">
<p><strong>Core contributors</strong><span>Ruoyu Wu<sup>1</sup>, Zengji Tu<sup>1</sup>, Aolong Sun<sup>1</sup>, Tianyi Ma<sup>1</sup>, Liang Chen<sup>1</sup>, Kuan Li<sup>1</sup></span></p>
<p><strong>Contributors</strong><span>Junren Li<sup>1</sup>, Xinbo Xu<sup>1</sup>, Li Fu<sup>1</sup>, Ziyan Zhang<sup>1</sup>, Pinrui Huang<sup>1</sup>, Xiaochen Wang<sup>1</sup>, Chengda Wu<sup>1</sup>, Yutao Zhou<sup>1</sup>, Jin Chen, Shen Yan, Xu Li, Zhongfei Hou, Nan Shu, Chaoyi Huang, Sihang Yuan, Zihan Xu</span></p>
<p><strong>Advisors</strong><span>Baobao Chang<sup>2</sup>, Lin Chang<sup>2</sup>, Jianjun Wu<sup>2</sup></span></p>
</div>
<p class="pbx-affiliations"><sup>1</sup>UniPat AI <span aria-hidden="true">·</span> <sup>2</sup>Peking University</p>
</div>
<p class="pbx-collaboration"><strong>For further collaboration on PaperBenchX, contact <a href="mailto:paperbenchx@unipat.ai">paperbenchx@unipat.ai</a>.</strong></p>
</section>

<script defer="" src="/static/paperbenchx/blog.js?v=20260921-structure-toc"></script>
<script defer="" src="/static/paperbenchx/leaderboard-data.js?v=20261007-names"></script>
<script defer="" src="/static/paperbenchx/leaderboard.js?v=20261030-logos"></script>
<script defer="" src="/static/paperbenchx/analysis-interactive.js?v=20261007-names"></script>
