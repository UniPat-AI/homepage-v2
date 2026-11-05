Title: UniPat Fellows: Investing $15 Million to Reshape How Science Is Done
Date: 2026-11-04
Summary: UniPat Fellows brings scientific research and model development into the same feedback loop. Fellows work alongside our researchers and engineers to tackle important problems that AI still can’t solve—but should.
HeaderImage: /static/images/fellows/cover-standard-1200.jpg
Layout: feature

<style>
.markdown:has(.fw4) { max-width: 100%; }
.paper .container:has(.fw4) { width: min(1180px, 100% - 48px); }
.fw4 {
  --ink: #12141c; --soft: #3f4553; --muted: #6b7280; --line: #e3e7ef; --wash: #eceff5; --card: #fff;
  --ember: #ff5a24; --ember-ink: #c2410c; --ember-wash: #fbeee6; --teal: #0f6d70; --teal-wash: #e4f1ef;
  --head: var(--sans); --body: var(--sans); --label: var(--mono);
  --top: 80px;
  color: var(--ink); font-family: var(--body);
}
.fw4 h1, .fw4 h2, .fw4 h3 { margin: 0; color: var(--ink); }
:where(.fw4) p { margin: 0; }
.fw4 a { text-decoration: none; }
.fw4 a:hover { text-decoration: none; }

/* 2 · Applications banner stays in the article flow so it never covers content. */
/* Background gradients share the banner's rounded edge without a separate blurred layer. */
.fw4-banner { position: relative; display: flex; align-items: center; gap: 18px; min-height: 64px; margin: 0 0 30px; padding: 10px 10px 10px 22px; border-radius: 16px;
  background: radial-gradient(ellipse 48% 180% at 100% 100%, rgba(255, 90, 36, .48), rgba(255, 90, 36, 0)), radial-gradient(ellipse 32% 160% at 60% 100%, rgba(15, 109, 112, .45), rgba(15, 109, 112, 0)), var(--ink);
  color: #edeff5; overflow: hidden; box-shadow: 0 18px 40px -24px rgba(18, 20, 28, .7); }
.fw4-banner-text { display: flex; flex-wrap: wrap; align-items: center; gap: 6px 14px; min-width: 0; flex: 1; font-family: var(--label); font-size: 12px; letter-spacing: .14em; text-transform: uppercase; }
.fw4-banner-text strong { display: inline-flex; align-items: center; gap: 12px; color: #fff; font-weight: 600; }
.fw4-banner-text strong::before { content: ""; flex: none; width: 8px; height: 8px; border-radius: 50%; background: var(--ember); box-shadow: 0 0 0 4px rgba(255, 90, 36, .22); animation: fw4-pulse 2.4s ease-in-out infinite; }
.fw4-banner-text span { color: #a9aec0; padding-left: 14px; border-left: 1px solid rgba(221, 227, 241, .22); }
@keyframes fw4-pulse { 50% { box-shadow: 0 0 0 9px rgba(255, 90, 36, 0); } }
.fw4-banner-cta { flex: none; display: inline-flex; align-items: center; gap: 10px; padding: 12px 22px; border-radius: 10px; background: var(--ember); color: var(--ink) !important; font-family: var(--label); font-size: 13px; font-weight: 700; letter-spacing: .14em; transition: background .2s ease, transform .2s ease; }
.fw4-banner-cta:hover { background: #ff7a4a; transform: translateY(-1px); }
.fw4-banner-cta:focus-visible { outline: 2px solid #fff; outline-offset: 3px; }
.fw4-banner-cta span { transition: transform .2s ease; }
.fw4-banner-cta:hover span { transform: translateX(3px); }

/* Hero */
.fw4-hero { display: grid; grid-template-columns: minmax(0, 1.2fr) minmax(0, 1fr); gap: 52px; align-items: center; padding: 8px 0 40px; }
.fw4-hero h1 { margin: 0 0 20px; font-family: var(--head); font-size: clamp(32px, 4.2vw, 50px); font-weight: 600; line-height: 1.08; letter-spacing: -.035em; text-wrap: balance; }
.fw4-hero h1 span { color: var(--ember-ink); }
.fw4-abstract { font-size: 19px; line-height: 1.6; color: var(--soft); }
.fw4-actions { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 28px; }
.fw4-btn { display: inline-flex; align-items: center; gap: 8px; padding: 12px 20px; border-radius: 10px; font-family: var(--label); font-size: 12px; font-weight: 600; letter-spacing: .04em; border: 1px solid var(--ink); transition: transform .2s ease, background .2s ease, color .2s ease, border-color .2s ease; }
.fw4-btn:hover { transform: translateY(-1px); }
.fw4-btn.is-primary { background: var(--ink); color: #fff !important; }
.fw4-btn.is-primary:hover { background: var(--ember-ink); border-color: var(--ember-ink); }
.fw4-btn.is-ghost { color: var(--ink) !important; background: #fff; border-color: #cfd5e1; }
.fw4-btn.is-ghost:hover { border-color: var(--ink); }
.fw4-cover { position: relative; aspect-ratio: 1; margin: 0; border-radius: 20px; overflow: hidden; background: #0a0b10; box-shadow: 0 34px 70px -34px rgba(194, 65, 12, .55); }
.fw4-cover img { width: 100%; height: 100%; object-fit: contain; display: block; border-radius: 0 !important; }
.fw4-facts { display: grid; grid-template-columns: repeat(4, 1fr); margin: 0; border: 1px solid var(--line); border-radius: 16px; background: rgba(255, 255, 255, .8); }
.fw4-facts div { padding: 18px 22px; }
.fw4-facts div + div { border-left: 1px solid var(--line); }
.fw4-facts dt { font-family: var(--label); font-size: 10.5px; letter-spacing: .14em; text-transform: uppercase; color: var(--muted); }
.fw4-facts dd { margin: 8px 0 0; font-size: 24px; line-height: 1.15; font-weight: 600; letter-spacing: -.02em; }
.fw4-facts dd small { display: block; margin-top: 4px; font-size: 13px; font-weight: 400; letter-spacing: 0; color: var(--muted); }

/* Main column + rail */
.fw4-main { display: grid; grid-template-columns: minmax(0, 1fr) 280px; gap: 56px; margin-top: 72px; }
.fw4-sec { padding-bottom: 72px; scroll-margin-top: calc(var(--top) + 30px); }
.fw4-eyebrow { font-family: var(--label); font-size: 11px; letter-spacing: .16em; text-transform: uppercase; color: var(--ember-ink); margin-bottom: 12px !important; }
.fw4 h2 { font-family: var(--head); font-size: 30px; font-weight: 600; line-height: 1.2; letter-spacing: -.025em; margin-bottom: 22px; text-wrap: balance; }
.fw4-prose { font-size: 18px; line-height: 1.72; color: #2a2f3c; }
.fw4-prose p + p { margin-top: 1em; }
.fw4-prose strong { color: var(--ink); }

/* 3 · Bridge: what each side brings and may need, joined by the shared Fellows band */
.fw4-bridge { margin: 34px 0; border: 1px solid var(--line); border-radius: 20px; background: var(--card); overflow: hidden; }
.fw4-bridge-sides { display: grid; grid-template-columns: 1fr 1fr; padding: 32px 0 30px; }
.fw4-side { display: flex; flex-direction: column; padding: 2px 34px; }
.fw4-side + .fw4-side { border-left: 1px solid var(--line); }
.fw4-side-tag { display: flex; align-items: center; gap: 12px; margin-bottom: 22px !important; font-family: var(--label); font-size: 11.5px; font-weight: 600; letter-spacing: .12em; text-transform: uppercase; color: var(--ink); }
.fw4-side-tag::before { content: ""; width: 18px; height: 2px; background: var(--ember-ink); }
.fw4-side h3 { margin-bottom: 16px; font-family: var(--head); font-size: clamp(30px, 3.4vw, 40px); font-weight: 600; line-height: 1.08; letter-spacing: -.035em; }
.fw4-side-lead { font-size: 17px; line-height: 1.6; color: var(--soft); }
.fw4-side-need { margin-top: auto; padding-top: 18px; border-top: 1px solid var(--line); font-size: 16px; line-height: 1.6; color: var(--soft); }
.fw4-side-need span { display: block; margin-bottom: 8px; font-family: var(--label); font-size: 10.5px; letter-spacing: .14em; text-transform: uppercase; color: var(--muted); }
.fw4-side-body { flex: 1; display: flex; flex-direction: column; gap: 26px; }
.fw4-bridge-joint { padding: 24px 34px 26px; border-top: 1px solid var(--line); background: #f7f3ee; }
.fw4-bridge-joint strong { display: block; margin-bottom: 6px; font-family: var(--label); font-size: 15px; font-weight: 500; letter-spacing: .08em; text-transform: uppercase; color: var(--ember-ink); }
.fw4-bridge-joint p { font-size: 18px; line-height: 1.5; color: var(--soft); }

/* How it works */
.fw4-steps { list-style: none; margin: 28px 0; padding: 0; counter-reset: step; }
.fw4-steps li { position: relative; display: grid; grid-template-columns: 48px minmax(0, 1fr); gap: 14px; padding: 18px 0; border-top: 1px solid var(--line); font-size: 16.5px; line-height: 1.6; color: var(--soft); }
.fw4-steps li::before { counter-increment: step; content: counter(step, decimal-leading-zero); font-family: var(--label); font-size: 12px; font-weight: 600; color: var(--ember-ink); padding-top: 3px; }
.fw4-steps li:last-child::after { content: "↺ repeat"; position: absolute; right: 0; bottom: 18px; font-family: var(--label); font-size: 10.5px; color: var(--teal); }
.fw4-steps b { color: var(--ink); font-weight: 600; }

/* 4 · Domain chips */
.fw4-chips { display: flex; flex-wrap: wrap; align-items: center; gap: 8px; margin: 20px 0 0; padding: 0; list-style: none; }
.fw4-chips li { margin: 0; padding: 6px 13px; border-radius: 999px; background: var(--teal-wash); color: var(--teal); font-family: var(--label); font-size: 11.5px; line-height: 1.4; white-space: nowrap; }
/* the ellipsis hangs off the last chip so the two always wrap together */
.fw4-chips li.is-last { position: relative; margin-right: 24px; }
.fw4-chips li.is-last::after { content: "…"; position: absolute; left: calc(100% + 7px); top: 50%; transform: translateY(-58%); font-size: 16px; font-weight: 700; color: var(--teal); }

/* 6 · Cases: a 5/7 bento so wider cards carry the longer write-ups; subgrid aligns each row */
.fw4-cases { display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 16px; }
.fw4-case { grid-column: span 5; grid-row: span 4; display: grid; grid-template-rows: subgrid; row-gap: 0; align-content: start; padding: 24px 24px 26px; border: 1px solid var(--line); border-radius: 16px; background: var(--card); transition: border-color .2s ease, transform .2s ease, box-shadow .2s ease; }
.fw4-case:nth-child(even) { grid-column: span 7; }
.fw4-case:hover { border-color: #efb79e; transform: translateY(-2px); box-shadow: 0 18px 34px -26px rgba(194, 65, 12, .5); }
.fw4-case svg { width: 40px; height: 40px; color: var(--ember-ink); margin-bottom: 18px; }
.fw4-case h3 { align-self: end; font-family: var(--head); font-size: 19px; font-weight: 600; line-height: 1.25; letter-spacing: -.015em; margin-bottom: 6px; }
.fw4-case-who { font-family: var(--label); font-size: 10.5px; letter-spacing: .06em; color: var(--muted); margin-bottom: 14px !important; padding-bottom: 14px; border-bottom: 1px solid var(--line); }
.fw4-case p:last-child { font-size: 15.5px; line-height: 1.62; color: var(--soft); }

/* 5 · Fit */
.fw4-two { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; }
.fw4-two h2 { position: relative; padding-left: 16px; font-size: 26px; }
.fw4-two h2::before { content: ""; position: absolute; left: 0; top: .18em; bottom: .14em; width: 3px; border-radius: 2px; background: var(--ember); }
.fw4-checks { list-style: none; margin: 0; padding: 0; font-size: 17px; line-height: 1.55; color: #2a2f3c; }
.fw4-checks li { position: relative; margin: 0; padding: 11px 0 11px 32px; }
.fw4-checks li::before { content: ""; position: absolute; left: 0; top: 15px; width: 18px; height: 18px; border-radius: 50%; background: var(--teal-wash) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M4.5 8.2l2.2 2.2 4.8-4.8' fill='none' stroke='%230f6d70' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center / 16px no-repeat; }

/* Formats */
.fw4-ways { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 18px; }
.fw4-way { padding: 26px; border-radius: 16px; border: 1px solid var(--line); background: var(--card); }
.fw4-way.is-dark { background: var(--ink); color: #e5e7eb; border-color: var(--ink); }
.fw4-way.is-dark h3 { color: #fff; }
.fw4-way-tag { font-family: var(--label); font-size: 10.5px; letter-spacing: .14em; text-transform: uppercase; color: var(--ember-ink); margin-bottom: 14px !important; }
.fw4-way.is-dark .fw4-way-tag { color: #ff8a5a; }
.fw4-way h3 { font-size: 20px; font-weight: 600; letter-spacing: -.015em; margin-bottom: 10px; }
.fw4-way p:last-child { font-size: 16px; line-height: 1.6; }
.fw4-way:not(.is-dark) p:last-child { color: var(--soft); }

/* Rail */
.fw4-rail { position: sticky; top: calc(var(--top) + 26px); align-self: start; }
.fw4-card { padding: 24px; border-radius: 18px; background: var(--ink); color: #e5e7eb; position: relative; overflow: hidden; }
.fw4-card::before { content: ""; position: absolute; width: 340px; height: 90px; left: -60px; bottom: -10px; background: linear-gradient(90deg, #0f6d70, #ff5a24 60%, #ff9a5a); filter: blur(40px); opacity: .5; transform: rotate(-28deg); }
.fw4-card > * { position: relative; }
.fw4-card h2 { color: #fff; font-size: 20px; margin-bottom: 6px; }
.fw4-card-mail { font-family: var(--label); font-size: 12px; color: #ffb48f; margin-bottom: 18px !important; word-break: break-all; }
.fw4-card ol { margin: 0 0 22px; padding: 0; list-style: none; counter-reset: c; font-size: 14px; line-height: 1.5; }
.fw4-card li { position: relative; margin: 0; padding: 10px 0 10px 28px; border-top: 1px solid rgba(255, 255, 255, .12); }
.fw4-card li::before { counter-increment: c; content: counter(c); position: absolute; left: 0; top: 11px; width: 18px; height: 18px; border-radius: 50%; border: 1px solid rgba(255, 255, 255, .35); font-family: var(--label); font-size: 9px; line-height: 17px; text-align: center; color: #fff; }
.fw4-card li small { display: block; margin-top: 3px; color: #9ca3af; font-size: 12.5px; }
.fw4-card .fw4-btn { width: 100%; justify-content: center; background: #fff; color: var(--ink) !important; border-color: #fff; }
.fw4-card .fw4-btn:hover { background: #ffe3d6; }
.fw4-rail-nav { margin-top: 18px; padding: 0 4px; font-family: var(--label); font-size: 11px; }
.fw4-rail-nav a { display: block; margin: 0; padding: 6px 0; color: var(--muted) !important; }
.fw4-rail-nav a:hover { color: var(--ink) !important; }

/* Closing */
.fw4-final { padding: 44px 32px; border-radius: 20px; background: var(--wash); text-align: center; }
.fw4-final p:first-child { font-family: var(--label); font-size: 11px; letter-spacing: .16em; text-transform: uppercase; color: var(--muted); margin-bottom: 16px; }
.fw4-final blockquote { margin: 0 auto 26px; padding: 0; border: 0; max-width: 600px; font-size: clamp(24px, 3vw, 32px); font-weight: 500; line-height: 1.3; letter-spacing: -.02em; color: var(--ink); }
.fw4-final blockquote span { color: var(--ember-ink); }

@media (max-width: 960px) {
  .fw4-main { grid-template-columns: 1fr; }
  .fw4-rail { position: static; order: -1; }
  .fw4-rail-nav { display: none; }
  .fw4-facts { grid-template-columns: 1fr 1fr; }
  .fw4-facts div:nth-child(3) { border-left: 0; }
  .fw4-facts div:nth-child(n+3) { border-top: 1px solid var(--line); }
}
@media (max-width: 720px) {
  .fw4-banner { min-height: 0; flex-wrap: wrap; gap: 14px; padding: 16px; }
  .fw4-banner-text { flex-direction: column; align-items: flex-start; gap: 8px; font-size: 11px; }
  .fw4-banner-text span { padding: 0 0 0 20px; border: 0; }
  .fw4-banner-cta { width: 100%; justify-content: center; }
  .fw4-hero { grid-template-columns: 1fr; gap: 30px; }
  .fw4-cover { max-width: 460px; }
  .fw4 h2 { font-size: 26px; }
  .fw4-two, .fw4-ways { grid-template-columns: 1fr; }
  .fw4-two { gap: 8px; }
  .fw4-two > div + div { margin-top: 40px; }
  .fw4-cases { grid-template-columns: 1fr; }
  .fw4-case, .fw4-case:nth-child(even) { grid-column: auto; grid-row: auto; display: flex; flex-direction: column; }
  .fw4-case h3 { align-self: auto; }
  .fw4-bridge-sides { grid-template-columns: 1fr; padding: 0; }
  .fw4-side { padding: 26px 22px; }
  .fw4-side + .fw4-side { border-left: 0; border-top: 1px solid var(--line); }
  .fw4-bridge-joint { padding: 22px; }
  .fw4-final { padding: 30px 20px; }
}
@media (max-width: 380px) {
  .fw4-facts { grid-template-columns: 1fr; }
  .fw4-facts div + div { border-left: 0; border-top: 1px solid var(--line); }
  .fw4-hero h1 { font-size: 30px; }
}
@media (prefers-reduced-motion: reduce) {
  .fw4 *, .fw4 *::before, .fw4 *::after { animation: none !important; transition: none !important; }
}
</style>

<div class="fw4">
<aside class="fw4-banner" aria-label="Applications open">
<p class="fw4-banner-text"><strong>Applications open</strong><span>UniPat AI Exploration Lab</span></p>
<a class="fw4-banner-cta" href="mailto:fellows@unipat.ai?subject=UniPat%20Fellows%20Application">APPLY <span aria-hidden="true">→</span></a>
</aside>
<header class="fw4-hero">
<div>
<h1>UniPat Fellows: Investing <span>$15 Million</span> to Reshape How Science Is Done</h1>
<p class="fw4-abstract">UniPat Fellows brings scientific research and model development into the same feedback loop. Fellows work alongside our researchers and engineers to tackle important problems that AI still can’t solve—but should.</p>
<div class="fw4-actions">
<a class="fw4-btn is-primary" href="mailto:fellows@unipat.ai?subject=UniPat%20Fellows%20Application">Apply now <span aria-hidden="true">→</span></a>
<a class="fw4-btn is-ghost" href="#exploring">See what Fellows explore</a>
</div>
</div>
<figure class="fw4-cover"><img src="/static/images/fellows/cover-standard-1200.jpg" srcset="/static/images/fellows/cover-standard-640.jpg 640w, /static/images/fellows/cover-standard-1200.jpg 1200w" sizes="(max-width: 720px) min(460px, 100vw - 48px), 460px" alt="UniPat Fellows cover: a lens magnifying a beam of orange light" width="1200" height="1200" fetchpriority="high"></figure>
</header>
<dl class="fw4-facts">
<div><dt>Investment</dt><dd>$15M<small>over the next year</small></dd></div>
<div><dt>API credits</dt><dd>$75K<small>frontier-model access</small></dd></div>
<div><dt>Formats</dt><dd>2 ways<small>full-time or project-based</small></dd></div>
<div><dt>Work mode</dt><dd>Onsite / Remote<small>flexible options</small></dd></div>
</dl>
<div class="fw4-main">
<div>
<section class="fw4-sec" id="why">
<p class="fw4-eyebrow">Why Fellows</p>
<h2>Bridging Science and AI, Starting with Questions That Matter</h2>
<div class="fw4-prose">
<p>Across disciplines, researchers see opportunities for AI to advance their work. Yet domain researchers and AI teams often work separately, with limited opportunities for sustained collaboration.</p>
</div>
<div class="fw4-bridge">
<div class="fw4-bridge-sides">
<article class="fw4-side">
<p class="fw4-side-tag">Domain researchers</p>
<h3>Questions<br>that matter.</h3>
<div class="fw4-side-body">
<p class="fw4-side-lead">Know how to frame research problems and judge the results.</p>
<p class="fw4-side-need"><span>May need</span>Dedicated AI research and engineering support.</p>
</div>
</article>
<article class="fw4-side">
<p class="fw4-side-tag">AI teams</p>
<h3>Models<br>and tools.</h3>
<div class="fw4-side-body">
<p class="fw4-side-lead">Bring expertise in AI research and engineering.</p>
<p class="fw4-side-need"><span>May need</span>Domain knowledge to define tasks and validate results.</p>
</div>
</article>
</div>
<div class="fw4-bridge-joint"><strong>UniPat Fellows</strong><p>Working together on shared research problems.</p></div>
</div>
<div class="fw4-prose">
<p>We’re launching <strong>UniPat Fellows</strong> at the UniPat AI Exploration Lab to bring domain researchers and AI teams together around shared research problems.</p>
<p>Fellows bring hard questions and deep domain expertise. Our researchers and engineers work alongside them to turn those questions into tasks for evaluating and training models. As models improve, they can help Fellows advance the research that inspired those tasks.</p>
<p>UniPat AI will invest $15 million over the next year in this effort. Inspired by Bell Labs’ approach to collaborative research, we provide models, compute, and experimental support so researchers can pursue difficult questions together.</p>
</div>
</section>
<section class="fw4-sec" id="how">
<p class="fw4-eyebrow">The process</p>
<h2>How Fellows Work</h2>
<div class="fw4-prose"><p>Each Fellow starts with a problem from their own research. Together, we identify tasks that still depend on expert researchers and explore what it would take for AI to perform them reliably.</p></div>
<ol class="fw4-steps">
<li><span><b>Benchmarks</b> establish a baseline for model performance and reveal where models fall short.</span></li>
<li><span><b>Interactive environments</b> give models access to specialized tools and simulations, with real-world feedback guiding their next steps.</span></li>
<li><span><b>Training.</b> The resulting tasks and feedback provide the basis for model training.</span></li>
<li><span><b>Evaluation.</b> Subsequent evaluations assess whether model performance on these research tasks has improved.</span></li>
</ol>
<div class="fw4-prose"><p>Our scope spans physics, chemistry, biology, medicine, materials, chip design, and beyond. What matters is whether the problem is important—and whether progress can be tested against observable results.</p></div>
<ul class="fw4-chips" aria-label="Research domains"><li>Physics</li><li>Chemistry</li><li>Biology</li><li>Medicine</li><li>Materials</li><li class="is-last">Chip design</li></ul>
</section>
<section class="fw4-sec" id="exploring">
<p class="fw4-eyebrow">Current work</p>
<h2>What Fellows Are Exploring</h2>
<div class="fw4-cases">
<article class="fw4-case">
<svg viewBox="0 0 44 44" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="4" y="15" width="36" height="14" rx="2"/><path d="M4 22c4-5 8 5 12 0s8 5 12 0 8 5 12 0"/></svg>
<h3>Optical chip design</h3>
<p class="fw4-case-who">Peking University · Physics</p>
<p>A Fellow from Peking University with a background in physics is exploring automated optical chip design. Models use electromagnetic simulation tools to work toward design objectives, analyze optical fields and device responses, and refine their designs based on simulation feedback.</p>
</article>
<article class="fw4-case">
<svg viewBox="0 0 44 44" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><path d="M22 40V24M22 24 10 8M22 24 34 8M16 16l-6 4M28 16l6 4"/><circle cx="10" cy="8" r="2.5"/><circle cx="34" cy="8" r="2.5"/></svg>
<h3>Antibody design &amp; engineering</h3>
<p class="fw4-case-who">Peking University · Pharmacy</p>
<p>A Fellow working in pharmaceutical research at Peking University is investigating automated antibody design and engineering. Models draw on sequence, structural, and experimental data to propose mutations, then use wet-lab feedback to guide the next round of experiments. The research examines whether AI can participate meaningfully in a continuous cycle of design, experimentation, feedback, and redesign.</p>
</article>
<article class="fw4-case">
<svg viewBox="0 0 44 44" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="6" y="6" width="32" height="32" rx="2"/><rect x="12" y="12" width="9" height="9"/><rect x="25" y="12" width="7" height="14"/><rect x="12" y="25" width="9" height="7"/><path d="M21 16.5h4M16.5 21v4"/></svg>
<h3>Chip layout design</h3>
<p class="fw4-case-who">UCLA · Chip design</p>
<p>A Fellow from UCLA is exploring automated chip layout design. Models operate professional design tools to generate and modify layouts under complex constraints, using verification and simulation feedback to improve their work.</p>
</article>
<article class="fw4-case">
<svg viewBox="0 0 44 44" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><path d="M5 38h34M5 38V6"/><path d="M8 32c6 0 8-20 14-20s8 14 14 14" stroke-dasharray="2 3"/><circle cx="22" cy="12" r="2.5"/></svg>
<h3>Probabilistic forecasting</h3>
<p class="fw4-case-who">Prediction markets</p>
<p>Other researchers are exploring probabilistic forecasting, including questions drawn from prediction markets. Forecasts are made before outcomes are known and evaluated as events unfold. Across many resolved events, researchers can assess whether models identify useful signals in noisy information and produce reliable, well-calibrated forecasts.</p>
</article>
</div>
</section>
<section class="fw4-sec" id="fit">
<div class="fw4-two">
<div>
<h2>Who We’re Looking For</h2>
<ul class="fw4-checks">
<li>Deep expertise, exceptional talent, or distinctive research taste in your field</li>
<li>Belief in AI’s potential to substantially advance your discipline</li>
<li>AI as an integral part of your research or work</li>
</ul>
</div>
<div>
<h2>What We Provide</h2>
<ul class="fw4-checks">
<li>Close collaboration with our research and engineering teams.</li>
<li>Frontier-model API credits valued at $75,000.</li>
<li>Compute, specialized data, access to domain experts, and research tools.</li>
<li>Competitive compensation.</li>
</ul>
</div>
</div>
</section>
<section class="fw4-sec" id="join">
<p class="fw4-eyebrow">Formats</p>
<h2>Two Ways to Join</h2>
<div class="fw4-ways">
<div class="fw4-way is-dark"><p class="fw4-way-tag">Long-term</p><h3>Full-time Fellow</h3><p>Join UniPat AI to pursue long-term research and real-world applications.</p></div>
<div class="fw4-way"><p class="fw4-way-tag">3 months or longer</p><h3>Project-based Fellow</h3><p>Work with us on a project for three months or longer while continuing your academic or professional commitments.</p></div>
</div>
</section>
<section class="fw4-final" id="apply">
<p>The question that starts every Fellowship</p>
<blockquote>“What is a problem in your field that AI <span>still can’t solve, but should?</span>”</blockquote>
<a class="fw4-btn is-primary" href="mailto:fellows@unipat.ai?subject=UniPat%20Fellows%20Application">Email fellows@unipat.ai <span aria-hidden="true">→</span></a>
</section>
</div>
<aside class="fw4-rail">
<div class="fw4-card">
<h2>How to Apply</h2>
<p class="fw4-card-mail">fellows@unipat.ai</p>
<ol>
<li>Your CV.</li>
<li>1–2 selected projects or publications.<small>If you have used AI in your research or projects, please include examples.</small></li>
<li>The one problem you’d pursue over the next three months—and why.<small>What is a problem in your field that AI still can’t solve, but should?</small></li>
</ol>
<a class="fw4-btn" href="mailto:fellows@unipat.ai?subject=UniPat%20Fellows%20Application">Apply via email →</a>
</div>
<nav class="fw4-rail-nav" aria-label="On this page">
<a href="#why">Why Fellows</a>
<a href="#how">How Fellows work</a>
<a href="#exploring">What Fellows explore</a>
<a href="#fit">Who &amp; what we provide</a>
<a href="#join">Two ways to join</a>
</nav>
</aside>
</div>
</div>
