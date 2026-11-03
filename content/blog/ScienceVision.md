Title: ScienceVision: Can AI Observe and Reason Like a Scientist?
Date: 2026-10-30
Summary: ScienceVision is an interdisciplinary benchmark for scientific 3D understanding and reasoning. Its expert-level visual questions over native 3D objects test whether a model can obtain evidence from the object and reason from it. The best score is 0.53 out of 1.
HeaderImage: /static/sciencevision/assets/sciencevision-cover.jpg
Layout: sciencevision

<link rel="stylesheet" href="/static/sciencevision/styles/tokens.css?v=bb3701f1">
<link rel="stylesheet" href="/static/sciencevision/styles/article.css?v=3d8a6787">
<link rel="stylesheet" href="/static/sciencevision/styles/trajectory.css?v=b7672362">
<link rel="stylesheet" href="/static/sciencevision/styles/components.css?v=23e5bceb">
<link rel="stylesheet" href="/static/sciencevision/styles/viewer.css?v=62824a51">
<link rel="stylesheet" href="/static/sciencevision/styles/site.css?v=3e20dbd1">

<div class="sv-layout">

<article class="sv-article">

<section class="sv-hero" id="overview">
<p class="sv-eyebrow">ScienceVision</p>
<div class="sv-hero__grid">
<div class="sv-hero__copy">
<h1>Can AI Observe and Reason Like a Scientist?</h1>
<p class="sv-hero__lede">
ScienceVision is an interdisciplinary benchmark for scientific 3D understanding and reasoning. It
uses expert-level visual question answering over native 3D objects to test whether a model can
obtain the evidence it needs from the object itself and then reason from it. The best score is
0.53 out of 1, from GPT-6 Astra (Codex).
</p>
<div class="sv-hero__actions">
<a class="sv-action sv-action--primary" href="https://github.com/UniPat-AI/ScienceVision" target="_blank" rel="noopener"><svg class="sv-action__icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>Code &amp; tasks</a>
<a class="sv-action" href="https://huggingface.co/datasets/UnipatAI/ScienceVision" target="_blank" rel="noopener"><svg class="sv-action__icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12.025 1.13c-5.77 0-10.449 4.647-10.449 10.378 0 1.112.178 2.181.503 3.185.064-.222.203-.444.416-.577a.96.96 0 0 1 .524-.15c.293 0 .584.124.84.284.278.173.48.408.71.694.226.282.458.611.684.951v-.014c.017-.324.106-.622.264-.874s.403-.487.762-.543c.3-.047.596.06.787.203s.31.313.4.467c.15.257.212.468.233.542.01.026.653 1.552 1.657 2.54.616.605 1.01 1.223 1.082 1.912.055.537-.096 1.059-.38 1.572.637.121 1.294.187 1.967.187.657 0 1.298-.063 1.921-.178-.287-.517-.44-1.041-.384-1.581.07-.69.465-1.307 1.081-1.913 1.004-.987 1.647-2.513 1.657-2.539.021-.074.083-.285.233-.542.09-.154.208-.323.4-.467a1.08 1.08 0 0 1 .787-.203c.359.056.604.29.762.543s.247.55.265.874v.015c.225-.34.457-.67.683-.952.23-.286.432-.52.71-.694.257-.16.547-.284.84-.285a.97.97 0 0 1 .524.151c.228.143.373.388.43.625l.006.04a10.3 10.3 0 0 0 .534-3.273c0-5.731-4.678-10.378-10.449-10.378M8.327 6.583a1.5 1.5 0 0 1 .713.174 1.487 1.487 0 0 1 .617 2.013c-.183.343-.762-.214-1.102-.094-.38.134-.532.914-.917.71a1.487 1.487 0 0 1 .69-2.803m7.486 0a1.487 1.487 0 0 1 .689 2.803c-.385.204-.536-.576-.916-.71-.34-.12-.92.437-1.103.094a1.487 1.487 0 0 1 .617-2.013 1.5 1.5 0 0 1 .713-.174m-10.68 1.55a.96.96 0 1 1 0 1.921.96.96 0 0 1 0-1.92m13.838 0a.96.96 0 1 1 0 1.92.96.96 0 0 1 0-1.92M8.489 11.458c.588.01 1.965 1.157 3.572 1.164 1.607-.007 2.984-1.155 3.572-1.164.196-.003.305.12.305.454 0 .886-.424 2.328-1.563 3.202-.22-.756-1.396-1.366-1.63-1.32q-.011.001-.02.006l-.044.026-.01.008-.03.024q-.018.017-.035.036l-.032.04a1 1 0 0 0-.058.09l-.014.025q-.049.088-.11.19a1 1 0 0 1-.083.116 1.2 1.2 0 0 1-.173.18q-.035.029-.075.058a1.3 1.3 0 0 1-.251-.243 1 1 0 0 1-.076-.107c-.124-.193-.177-.363-.337-.444-.034-.016-.104-.008-.2.022q-.094.03-.216.087-.06.028-.125.063l-.13.074q-.067.04-.136.086a3 3 0 0 0-.135.096 3 3 0 0 0-.26.219 2 2 0 0 0-.12.121 2 2 0 0 0-.106.128l-.002.002a2 2 0 0 0-.09.132l-.001.001a1.2 1.2 0 0 0-.105.212q-.013.036-.024.073c-1.139-.875-1.563-2.317-1.563-3.203 0-.334.109-.457.305-.454m.836 10.354c.824-1.19.766-2.082-.365-3.194-1.13-1.112-1.789-2.738-1.789-2.738s-.246-.945-.806-.858-.97 1.499.202 2.362c1.173.864-.233 1.45-.685.64-.45-.812-1.683-2.896-2.322-3.295s-1.089-.175-.938.647 2.822 2.813 2.562 3.244-1.176-.506-1.176-.506-2.866-2.567-3.49-1.898.473 1.23 2.037 2.16c1.564.932 1.686 1.178 1.464 1.53s-3.675-2.511-4-1.297c-.323 1.214 3.524 1.567 3.287 2.405-.238.839-2.71-1.587-3.216-.642-.506.946 3.49 2.056 3.522 2.064 1.29.33 4.568 1.028 5.713-.624m5.349 0c-.824-1.19-.766-2.082.365-3.194 1.13-1.112 1.789-2.738 1.789-2.738s.246-.945.806-.858.97 1.499-.202 2.362c-1.173.864.233 1.45.685.64.451-.812 1.683-2.896 2.322-3.295s1.089-.175.938.647-2.822 2.813-2.562 3.244 1.176-.506 1.176-.506 2.866-2.567 3.49-1.898-.473 1.23-2.037 2.16c-1.564.932-1.686 1.178-1.464 1.53s3.675-2.511 4-1.297c.323 1.214-3.524 1.567-3.287 2.405.238.839 2.71-1.587 3.216-.642.506.946-3.49 2.056-3.522 2.064-1.29.33-4.568 1.028-5.713-.624"/></svg>Dataset</a>
<a class="sv-action" href="https://github.com/UniPat-AI/ScienceVision/blob/main/paper/sciencevision.pdf" target="_blank" rel="noopener"><svg class="sv-action__icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5.625 1.5c-1.036 0-1.875.84-1.875 1.875v17.25c0 1.035.84 1.875 1.875 1.875h12.75c1.035 0 1.875-.84 1.875-1.875V12.75A3.75 3.75 0 0 0 16.5 9h-1.875a1.875 1.875 0 0 1-1.875-1.875V5.25A3.75 3.75 0 0 0 9 1.5H5.625Z"/><path d="M12.971 1.816A5.23 5.23 0 0 1 14.25 5.25v1.875c0 .207.168.375.375.375h1.875a5.23 5.23 0 0 1 3.434 1.279 9.768 9.768 0 0 0-6.963-6.963Z"/></svg>Paper</a>
</div>
</div>
<figure class="sv-hero__figure">
<picture>
<source srcset="/static/sciencevision/assets/sciencevision-cover.webp" type="image/webp">
<img src="/static/sciencevision/assets/sciencevision-cover.jpg" width="760" height="760" alt="A robot at a laptop inspecting a 3D cube through a magnifying glass, ringed by panels showing a protein ribbon, a molecule, a brain scan, a gear assembly and a building frame.">
</picture>
</figure>
</div>

<div class="sv-stats">
<div class="sv-stat"><strong>250</strong><span>expert questions<br>50 per discipline</span></div>
<div class="sv-stat"><strong>5</strong><span>disciplines<br>22 subdomains</span></div>
<div class="sv-stat"><strong>&asymp;500 h</strong><span>expert annotation<br>66 experts &middot; 482.98 recorded hours</span></div>
<div class="sv-stat"><strong>0.53</strong><span>best mean answer score<br>GPT-6 Astra &middot; Harness &middot; 3D</span></div>
</div>
<p class="sv-note">
Best mean answer score at the 3D setting; values are the mean
<code class="sv-code" style="display:inline;padding:2px 5px">answer_score</code> on [0,1],
with ineligible trials counted zero.
</p>
</section>

<section class="sv-section" id="why">
<p class="sv-kicker">Why it is hard</p>
<h2>Visual observation in scientific research</h2>
<p>
Scientific discovery starts with observation. Galileo's telescope found the moons of Jupiter,
Hooke's microscope named the cell, and Rosalind Franklin's X-ray diffraction images showed the
DNA helix. A researcher has to notice what is anomalous in a three-dimensional field, work out
how it is assembled, and decide what to verify next. Models can now read papers, write code and
derive formulas, but interpreting visual evidence is a separate capability.
</p>
<p>
Scientific observation starts with finding the evidence needed to answer a question. A chemist
may have to reveal an occluded atom before tracing a bonded path; a radiologist has to locate a
lesion inside a volume. For a model, that means choosing what to inspect, obtaining the evidence,
and connecting it to the question. Occlusion, repeated components, and coordinate conventions
affect these observations and measurements. Research agents that generate hypotheses or run
computational experiments face the same demand.
</p>
<p>
ScienceVision evaluates scientific question answering through 250 tasks across five
disciplines. Each task pairs a 3D source with a domain question, a specified response
format, and a reference answer. The questions require models to use domain knowledge to
interpret geometric or topological evidence.
</p>

<div class="sv-contrib">
<div>
<strong>A cross-discipline 3D benchmark</strong>
<span>250 expert questions across architecture, biology, chemistry, mechanical CAD and
medical imaging, covering 22 subdomains. Each pairs a 3D source with a domain question
and a structured reference answer; some connect target identification under occlusion to
topological or geometric reasoning.</span>
</div>
<div>
<strong>An MCP inspection environment shaped by expert workflow</strong>
<span>View control, target isolation, slice browsing and scientific measurement, with the
available operations varying by viewer. The agent chooses what to inspect and obtains the
evidence itself rather than receiving a fixed rendering.</span>
</div>
<div>
<strong>Three access settings, one answer contract</strong>
<span>Source-only 3D, 3D with MCP inspection tools, and a 2D rendered-image control are
evaluated on the same question set. Scores are reported by setting and discipline, with
the run and scoring limits stated.</span>
</div>
<div>
<strong>Deterministic, component-level scoring across domains</strong>
<span>Reference answers and predefined rules verify each answer component separately, then
aggregate by setting and discipline. The same scoring method is used for every setting, so
the settings remain comparable.</span>
</div>
</div>
</section>

<section class="sv-section" id="inspect">
<p class="sv-kicker">Hands on</p>
<h2>Inspect the source yourself</h2>
<p class="sv-lede">
ScienceVision spans five disciplines whose native 3D sources span several formats. The
five samples below cover five of them: a protein is an mmCIF file, a crystal is a CIF
with unit-cell symmetry, a CT study is a NIfTI volume, a CAD assembly is a STEP file,
and a building is glTF. This page brings those formats into one interface and opens
each in the viewer its discipline uses &mdash; Mol* for structures, NiiVue for volumes,
OCCT for STEP, three.js for glTF.
</p>
<p>
Choose a discipline and inspect the source directly: orbit, zoom, section, read the unit
cell, or switch the CT between a 3D render and orthogonal slices. This is active visual
inspection &mdash; the reader chooses what to expose and how to look at it, rather than
reading a fixed rendering. These are the expert-facing viewers, not the evaluation
harness; nothing is uploaded, nothing is saved, and the page does not score your
inspection. Each viewer loads only when you open it; the medical volume is the heaviest
at about 61 MB, so its first view can take a few seconds.
</p>

<figure class="sv-live" data-live-viewer>
<div class="sv-live__brief">
<p class="sv-live__domain" data-domain></p>
<p class="sv-live__caption" data-caption></p>
<p class="sv-live__task" data-task></p>
<details class="sv-live__question">
<summary>Question</summary>
<div class="sv-live__question-body" data-question></div>
</details>
</div>
<div class="sv-live__tabs" data-tabs role="tablist" aria-label="Discipline"></div>
<div class="sv-live__stage" data-stage id="sv-live-stage" role="tabpanel">
<div class="sv-live__poster" data-poster>
<img data-poster-img src="/static/sciencevision/assets/traj/arch-rhl-access-al116-m07-ramp-run-between-decks/017.jpg" alt="Isometric view of the ramp model with slope and run measurements overlaid.">
<button class="sv-live__load" data-load type="button">Load interactive view</button>
</div>
<p class="sv-live__status" data-status hidden></p>
<iframe class="sv-live__frame" data-frame title="ScienceVision 3D viewer" loading="lazy" allow="fullscreen" hidden></iframe>
</div>
<div class="sv-live__bar">
<div class="sv-live__actions">
<button class="sv-live__action" data-fullscreen type="button">Full screen</button>
</div>
</div>
<figcaption>
The assets are the original task files. The viewer applications are the ScienceVision
inspection interfaces; a recorded expert session for each task is shown in the section
below. Viewer libraries: Mol* (MIT), NiiVue (BSD-2-Clause), three.js (MIT),
occt-import-js (LGPL-2.1).
</figcaption>
</figure>
<noscript>
<p class="sv-note">The interactive viewer needs JavaScript. The static preview and the recorded inspections below remain available.</p>
</noscript>
</section>

<section class="sv-section" id="recorded-inspections">
<p class="sv-kicker">How the work is done</p>
<h2>The reference inspection, recorded</h2>
<p class="sv-lede">
The tools in ScienceVision are modelled on how a domain expert works a 3D source: orbit
until the target is visible, isolate it from what surrounds it, cut away what is in front,
switch how the structure is drawn, then measure what matters. Those inspections were
captured operation by operation, so the workflow can be watched rather than described.
</p>
<p>
Five play below, one per discipline, chosen to show how differently the work divides. One
inspection is almost all camera moves; another is almost all selecting and hiding; another
reads a unit cell and lets symmetry show how the packing repeats. The bar under the viewer
is the complete operation record, coloured by the kind of operation; click any step to jump
to it, or use the discipline buttons to move between them.
</p>

<figure class="sv-cinema" data-cinema>
<div class="sv-cinema__body">
<div class="sv-cinema__stage">
<img data-frame src="" alt="">
</div>
<div class="sv-cinema__panel">
<p class="sv-cinema__domain" data-domain></p>
<p class="sv-cinema__caption" data-caption></p>
<div class="sv-cinema__readout">
<p class="sv-cinema__fn" data-fn></p>
<p class="sv-cinema__param" data-param></p>
</div>
<p class="sv-cinema__mix" data-mix></p>
<p class="sv-cinema__task" data-task></p>
</div>
</div>

<ol class="sv-cinema__strip" data-strip></ol>

<div class="sv-cinema__bar">
<button class="sv-cinema__btn" type="button" data-act="toggle">Play</button>
<button class="sv-cinema__btn" type="button" data-act="prev" aria-label="Previous step">&lsaquo;</button>
<button class="sv-cinema__btn" type="button" data-act="next" aria-label="Next step">&rsaquo;</button>
<span class="sv-cinema__counter" data-counter></span>
<div class="sv-cinema__tabs" data-tabs></div>
</div>

<p class="sv-cinema__legend">
<span><i class="cls-measure"></i>measurement</span>
<span><i class="cls-select"></i>selection &amp; display</span>
<span><i class="cls-section"></i>section</span>
<span><i class="cls-view"></i>camera</span>
</p>

<figcaption>
Reference inspection trajectories recorded through the source viewer. A step record
documents what was done; it does not establish expert certification, a required tool
set, or a minimum reasoning length.
</figcaption>
</figure>

<p class="sv-note">
All 250 questions carry a recorded inspection, running to 62 operations, and every one
was captured keyframe by keyframe, which is what makes the replay above possible. The
proportion of operations that are measurements, selections, sections or camera moves
differs sharply by discipline; counts are shown per trajectory in the timeline.
</p>
</section>



<section class="sv-section" id="benchmark">
<p class="sv-kicker">Task anatomy</p>
<h2>What one question contains</h2>
<p class="sv-lede">
Each task pairs a source artifact with a domain question and specifies the answer format
to return. The response is evaluated against a structured reference answer.
</p>

<div class="sv-steps">
<div class="sv-step">
<span class="sv-step__num">01</span>
<h3>Source artifact</h3>
<p>
A molecular coordinate file (XYZ or CIF), a CT volume (NIfTI), or a CAD or building
model. The question concerns the supplied object, not a description of it.
</p>
</div>
<div class="sv-step">
<span class="sv-step__num">02</span>
<h3>Question</h3>
<p>
Identifies the target or explains how to locate it, and states units, coordinate
conventions, or inspection conditions where they are specified.
</p>
</div>
<div class="sv-step">
<span class="sv-step__num">03</span>
<h3>Answer contract</h3>
<p>
The question's own contract sets the output structure. Many ask for JSON fields;
others ask for a single word or category.
</p>
</div>
<div class="sv-step">
<span class="sv-step__num">04</span>
<h3>Reference answer</h3>
<p>
The evaluator's target for comparison. Code and tool calls are intermediate means of
obtaining evidence, not the requested result. The released task tree also includes the
reference solution under <code>oracles/&lt;task_id&gt;/solution/</code>, whose
<code>solution.sh</code> runs the task's oracle program; in the Harbor task format this
is the oracle solution, a reference implementation rather than a model output
(paper App. A.5; task tree <code>oracles/</code>).
</p>
</div>
</div>

<p class="sv-note" style="margin-top:18px">Three answer contracts from the set:</p>
<div class="sv-settings">
<div class="sv-setting">
<span class="sv-setting__tag">chemistry</span>
<code class="sv-code">{"sp_count": 2, "sp2_count": 6, "sp3_count": 1}</code>
<p style="margin-top:10px">
Classify every heavy atom by hybridization from its bonding and local geometry, then
count each category.
</p>
</div>
<div class="sv-setting">
<span class="sv-setting__tag">medical imaging</span>
<code class="sv-code">{"point_vox": [77, 105, 120]}</code>
<p style="margin-top:10px">
A voxel inside a lesion. The prompt fixes array shape, axis order, voxel size, and
zero-based integer indices.
</p>
</div>
<div class="sv-setting">
<span class="sv-setting__tag">mechanical CAD</span>
<code class="sv-code">{"answer": "asymmetric"}</code>
<p style="margin-top:10px">
The question asks for one word, <em>symmetric</em> or <em>asymmetric</em>. The JSON
wrapper is the normalised record, not the question's own format.
</p>
</div>
</div>

<p class="sv-note" style="margin-top:16px">
Atom identities can also be nested objects carrying <code>chain_id</code>,
<code>residue_name</code>, <code>residue_number</code>, <code>atom_name</code> and
<code>element</code>. Field counts describe output structure, not dependent
subquestions or reasoning steps.
</p>
</section>

<section class="sv-section" id="access">
<p class="sv-kicker">Access settings</p>
<h2>Two ways to obtain the evidence, and a 2D control</h2>
<p class="sv-lede">
The same 250 questions are posed under two access settings. What changes is not the
question or the scoring, but what the solver is given. A third condition supplies only
rendered images, and serves as a control against which the two settings are read.
</p>

<div class="sv-settings" data-settings>
<div class="sv-setting">
<span class="sv-setting__tag">Harness &middot; 3D</span>
<h3>Source access</h3>
<p>
A coding agent analyses the source artifact programmatically. It can read coordinates
or other source data and write code to identify objects, compute measurements, or
test geometric relationships.
</p>
</div>
<div class="sv-setting">
<span class="sv-setting__tag">Harness &middot; 3D + MCP</span>
<h3>Source access with inspection tools</h3>
<p>
The same source access, plus human-oriented interfaces: change views, isolate
structures, inspect slices, measure geometry. The operations are modelled on expert
inspection, and are available to the agent as tools.
</p>
</div>
<div class="sv-setting">
<span class="sv-setting__tag">Harness &middot; 2D</span>
<h3>Fixed-view control</h3>
<p>
Only rendered images accompany the question, so evidence has to come from them and
the solver cannot compute from the source. The condition varies the camera plan and
the number of views. The aligned plan looks along canonical directions; the orbit
plan spaces views evenly around the horizontal circle at a fixed elevation. One,
three, six and twelve views of each plan were tested, and six aligned views, the
setting used in the comparison below, was the best of them in a GPT-6-Astra run
under Codex. Medical tasks pair each volume render with a slice, so a six-view
manifest contains twelve image files: six renders and six slices (paper §5).
</p>
</div>
</div>

<p class="sv-note" style="margin-top:16px">
Direct artifact access still tests visual exploration of the scientific object: the
model must locate and interpret the task-relevant spatial evidence. What the score does
not show is the route. The model may compute from source geometry in code rather than
observe the object in a scientific application, and access to source data or tools does
not by itself establish that the required evidence was acquired through a viewer.
</p>
</section>

<section class="sv-section" id="leaderboard">
<p class="sv-kicker">Model comparison</p>
<h2>How the models compare</h2>
<p class="sv-lede">
Twelve models were run over the same 250 questions under the two 3D access settings.
Both share a metric and a scale, so they are charted together and answer whether the
inspection tools help. The 2D control uses the same metric on a fixed-view rendering and gets its own chart.
</p>

<div data-leaderboard></div>

<p>
<strong>The questions are hard.</strong> The highest discipline cell is 0.65, and the
best overall mean is 0.53.
</p>

<p>
<strong>The models separate.</strong> They run from 0.53 down to 0.16, and under both 3D
settings every closed-source model stays above every open-source one.
</p>

<p>
<strong>The disciplines differ.</strong> Mechanical CAD, medical imaging and architecture
have the lowest floors, with their weakest models below 0.10. Chemistry and biology stay
flat and high: no model falls below 0.24 there, and biology holds the highest discipline
cell in the set (0.65).
</p>

<p class="sv-note">
<strong>Metric and coverage.</strong> Values are the mean
<code class="sv-code" style="display:inline;padding:2px 5px">answer_score</code> on [0,1],
with ineligible trials counted zero. The two 3D settings average up to three runs per
question and then the 250 questions; Gemini's carried-over segment has two runs. The 2D
control uses the same metric over three runs; Hunyuan-4 has three questions with two
runs. All 250 questions are covered. The 2D control is drawn on its own axis, so compare its order with the 3D
charts, not its bar lengths.
</p>
<p class="sv-note">
<strong>Harness.</strong> The two GPT-family models were run in a Codex harness on all
250 questions and in all three settings; the other ten in Claude Code. A GPT row
therefore measures a different scaffold, not only a different model. Run under Claude
Code instead, GPT-6 Astra scores 0.440 on Harness &middot; 3D and 0.426 on Harness &middot; 3D + MCP, and GPT-6.1 Sol
0.419 and 0.416, seven to ten points below their Codex rows.
</p>
<p class="sv-note">
<strong>Harness cross-check.</strong> Under Codex, Claude Fable 5.1 scores 0.507 on
Harness &middot; 3D and 0.535 on Harness &middot; 3D + MCP, versus 0.462 and 0.463 under Claude Code;
Claude Opus 5.5 scores 0.545 and 0.532 under Codex versus 0.454 and 0.434 under Claude Code.
The two Claude Codex rows were run on the current 250-task package at high reasoning
effort, while the other rows splice the archived runs with the rerun tasks, so these
gaps also include task-version and effort differences; they are not a controlled
harness-only comparison.
</p>
<p class="sv-note">
<strong>Sources and drift.</strong> Each score splices a carried-over segment with a
re-run segment, and six models take their re-run segment from a separate evaluation
service. Runs were measured on different days and model aliases carry no version, so a
difference here can mix a change of run with a change of model version.
</p>
<p class="sv-note">
Equal coverage does not establish a controlled comparison.
</p>
</section>

<section class="sv-section" id="related">
<p class="sv-kicker">Related work</p>
<h2>Where this sits</h2>
<p class="sv-lede">
Earlier benchmarks already cover parts of this ground. The difference is the combination:
several disciplines at once, evidence the solver selects from a 3D source, and answers
checked independently against task-specific reference values.
</p>

<div data-comparison></div>

<p class="sv-note">
A mark records what a benchmark reports, not how well it does it. <strong>QA focus</strong>
means task families centre on questions about the input, including author-classified
object-description prompts; <em>partial</em> denotes QA alongside visualisation or
data-processing workflow outcomes. <strong>Cross-domain
science</strong> covers multiple scientific fields, not object categories. <strong>Visual
interaction</strong> includes agent-selected views, slices, crops or rendered prediction
feedback. <strong>Static-image QA</strong> is a separately reported fixed-image QA setting.
<strong>Deterministic scoring</strong> is a tick for rule-based formal grading without a
language-model judge, <em>partial</em> for mixed rule-based and language-model grading, and
a cross for language-model-only grading; annotation, evaluated agents and shadow
diagnostics are excluded. ScienceVision retains separate verdicts for independently
evaluated answer components, identifying which subquestions fail.
</p>

<p>
SciVisAgentBench is the only other cross-domain entry here, and both benchmarks put 3D
scientific data behind the agent. Its cases are visualisation tasks carried out in
established software, each admitting a single specified outcome and anchored by a
ground-truth artifact, usually the reference visualisation. Scoring combines
expert-authored rubrics, model judges, image-similarity metrics and rule-based checks,
with its question tasks scored as discrete single-answer checks. ScienceVision centres on
expert-level scientific understanding and reasoning: a question asks what is true of the
object (how many parts, which class, where, how far apart), and answering it means
applying the scientific knowledge and conventions needed to interpret the object, not
just producing a correct rendering. Answers are scored component by component against a
task-specific reference, without a model judge. In one benchmark the graded product is
the visualisation; in the other it is the conclusion about the object, with the
visualisation only one of the evidence routes under comparison.
</p>

<p>
Anthropic's
<a href="https://www.anthropic.com/claude-opus-5-5-system-card" target="_blank" rel="noopener">Claude Opus 5.5 System Card</a>
also reports science evaluations, including CT and MRI medical imaging. The direction overlaps,
but the scope differs: ScienceVision covers native scientific 3D objects more broadly, asking
whether a model can gather evidence from such an object and reason from it.
</p>
</section>

<section class="sv-section" id="coverage">
<p class="sv-kicker">The set</p>
<h2>What the 250 questions cover</h2>
<p class="sv-lede">
Five disciplines, 50 questions each, spread over 22 sub-domains, four or five per
discipline, and never an even split. Bucket size runs from 4 questions to 25, with a
median of 10.
</p>

<div class="sv-compose" data-coverage></div>

<p class="sv-note" style="margin-top:16px">
How concentrated a discipline is varies: its largest bucket takes 28% of biology, 32% of
architecture, 40% of mechanical CAD, 42% of chemistry and 50% of medical imaging, where
lesion pointing alone accounts for 25 of the 50. Sub-domain labels describe task
categories rather than mutually exclusive cognitive abilities, and equal discipline
counts do not imply uniform coverage of task types within a discipline.
</p>

<div class="sv-stats" style="margin-top:26px">
<div class="sv-stat">
<strong>107</strong>
<span>of 250 tasks ask more than one question (multiple answer fields); the remaining
143 declare a single field</span>
</div>
<div class="sv-stat">
<strong>8.63</strong>
<span>operations per reference inspection on average, up to 62, across all 250
questions</span>
</div>
<div class="sv-stat">
<strong>173</strong>
<span>of 250 delivered tool records call at least one tool</span>
</div>
<div class="sv-stat">
<strong>16%</strong>
<span>numeric-only answers that also show a measuring-tool call</span>
</div>
</div>

<p class="sv-note" style="margin-top:20px">
These describe the delivered records. A step count does not establish a complete
demonstration, expert certification, a required tool set, or a minimum reasoning length,
and the 16% is an operational statistic rather than a claim about which tasks intrinsically
require measurement.
</p>
</section>

<section class="sv-section" id="cases">
<p class="sv-kicker">Task examples</p>
<h2>Three questions and what they demand</h2>
<p class="sv-lede">
These describe questions in the current set, rather than inferring model behaviour from
final scores.
</p>

<div class="sv-cases">
<div class="sv-case">
<p class="sv-case__domain">Chemistry</p>
<h3>Occluded atoms and bonded paths</h3>
<p>
Identify an almost fully occluded atom and a partially occluded heavy atom in the
initial view, then find the shortest bonded path between them and the minimum
absolute dihedral angle along it.
</p>
<dl>
<dt>task</dt>
<dd>sv-chem-chem_conformation-0002</dd>
<dt>reference</dt>
<dd>[21, 8, 9, 3, 2] · 3 intermediate · 64.49°</dd>
</dl>
</div>

<div class="sv-case">
<p class="sv-case__domain">Architecture</p>
<h3>Continuity, extents and units</h3>
<p>
A continuous member spans two or more storeys without interruption. Count them, give
the shortest and longest extents, and say whether any is discontinuous.
</p>
<dl>
<dt>task</dt>
<dd>arch-anzj-align-a07</dd>
<dt>reference</dt>
<dd>4 members · 12,000 mm and 12,200 mm · none discontinuous</dd>
</dl>
</div>

<div class="sv-case">
<p class="sv-case__domain">Mechanical CAD</p>
<h3>Repeated and hidden instances</h3>
<p>
Count instances of one component design, where identical shapes are marked as separate
instances by colour and some are hidden behind other components.
</p>
<dl>
<dt>task</dt>
<dd>hard-011</dd>
<dt>reference</dt>
<dd>14 instances</dd>
</dl>
</div>
</div>

<p>
The architecture question specifies millimetres in a Z-up source frame and metres in a
Y-up viewer frame, so a correct answer depends on converting coordinates and units
consistently. In the CAD task the final count alone cannot show whether a model identified
the correct part, observed all instances, or obtained the number from source data.
</p>
</section>

<section class="sv-section" id="limits">
<p class="sv-kicker">Limits</p>
<h2>What the scores do not settle</h2>
<p class="sv-lede">
Several limitations bear on how the scores should be read.
</p>

<div class="sv-callout">
<p>
<strong>Independent answer-component scores identify which subquestions fail.</strong>
These verdicts do not by themselves verify the evidence used or establish whether an
error came from observation or reasoning.
</p>
</div>

<p>
Three biology tasks require camera behaviour in an interactive viewer that the report says
was absent from the Codex evaluation system. For one model, repairing missing biology
comparators changed 11 of 12 trials across six tasks from zero to full score without
changing the answers; a further 13 trials across seven tasks did not parse into the
required answer fields. Cross-model comparisons therefore reflect the model, the execution
system and the scoring pipeline together.
</p>

<p>
Of the 250 delivered MCP trajectories, 173 include at least one tool call and 83 include a
measuring-tool call. The intersection of numeric-only answers with observed
measuring-tool calls holds 40 tasks, or 16%.
</p>
<p class="sv-note">
Scores are reported as evaluated, and do not show that every historical run has been
independently replayed. Rebuilding the aggregate tables reproduces the summary figures on
this page, not a replay of the original evaluation.
</p>
</section>

<section class="sv-section" id="construction">
<p class="sv-kicker">Construction</p>
<h2>From candidate questions to expert review</h2>
<p class="sv-lede">
Automation and experts build the questions together. Neither side works alone, and
each review pass feeds the next draft.
</p>
<p>
Automated checks first match an asset to a task and confirm that the object can actually
be inspected, then draft candidate questions and screen them against rules before
packaging each one with its assets. Experts then review the questions, inspect the 3D
evidence themselves, and record reference answers and the route they took to reach them.
Records that fail quality review go back for revision, by hand or by an agent, and are
checked again before export.
</p>

<figure class="sv-figure">
<img src="/static/sciencevision/assets/pipeline.png?v=7e7763b8" width="960" height="392" alt="Construction pipeline. Automated asset checks, candidate construction, rule screening and packaging produce a candidate bundle. Experts review and edit the questions, inspect the 3D evidence, record a reference answer and the route taken, and run quality review. Failed records return for revision and rechecking, by hand or by agent, before export.">
<figcaption>
Automated construction with expert-guided revision, from candidate bundles through
quality review to export.
</figcaption>
</figure>
</section>

<section class="sv-section" id="next">
<p class="sv-kicker">Outlook</p>
<h2>Where this goes next</h2>
<p>Finding the evidence a question needs, and turning it into a checkable answer, is one of the
capabilities scientific work asks of a model. ScienceVision makes it measurable on
cross-disciplinary 3D tasks, with inspection tools drawn from expert workflow and answers checked
against task-specific references. Expert knowledge and one annotation platform are what hold the
question, the inspection and the verification together.</p>
<p>Next we will widen the set of disciplines the benchmark covers, and explore extending the
evaluation to real production settings.</p>
</section>
<section class="sv-section" id="contributors">
<p class="sv-kicker">Contributors</p>
<h2>Who built it</h2>
<p class="sv-lede">
The expert roles were staffed across all five disciplines and coordinated through one
annotation platform, so all five were built and checked the same way rather than
separately and combined afterwards.
</p>
<p>That pool spans all five disciplines: 66 people, with 482.98 hours of recorded working time
between them: 74 in biology, 113.33 in chemistry, 103 in medical imaging, 115.65 in mechanical CAD
and 77 in architecture. The hours cover question writing, revision, reference-answer annotation
and review.</p>

<dl class="sv-people">
<div><dt>Core contributor</dt>
<dd>Tianyi Ma<sup>1,*</sup>, Jing Gu<sup>2,*</sup>, Haozhe Zhao<sup>1,&#8225;</sup>,
Liang Chen<sup>1,&#8225;</sup>, Yunfan Zhang<sup>1</sup>,
Haijun Su<sup>2</sup>, Jialong Wu<sup>1</sup>, Le Xue<sup>2</sup>,
Arnav Das<sup>2</sup>, Dustin Tran<sup>2</sup>, Yinfei Yang<sup>2</sup>,
Andrew Dai<sup>2,&#8224;</sup>, Kuan Li<sup>1,&#8224;</sup></dd></div>
<div><dt>Contributors</dt>
<dd>Liangkun He<sup>1</sup>, Zihao Guo<sup>1</sup>, Xiang Gong<sup>1</sup>,
Yutao Zhou<sup>1</sup>, Jiarui Sun<sup>1</sup>, Chengda Wu<sup>1</sup>,
Zhao Zhang<sup>1</sup>, Qianhui Yang<sup>1</sup>, Zhenji Kang<sup>1</sup>,
Yi Shen<sup>1</sup>, Wenda Wang<sup>2</sup></dd></div>
</dl>

<p class="sv-note">
<sup>1</sup> UniPat AI. <sup>2</sup> Elorian AI.
<sup>*</sup> Equal contribution. <sup>&#8225;</sup> Project leader.
<sup>&#8224;</sup> Corresponding author.
</p>
</section>

</article>

<aside class="sv-rail">
<p class="sv-rail__title">On this page</p>
<ol>
<li><a href="#why">Visual observation in scientific research</a></li>
<li><a href="#inspect">Inspect the source yourself</a></li>
<li><a href="#recorded-inspections">The reference inspection, recorded</a></li>
<li><a href="#benchmark">What one question contains</a></li>
<li><a href="#access">Two ways to obtain the evidence, and a 2D control</a></li>
<li><a href="#leaderboard">How the models compare</a></li>
<li><a href="#related">Where this sits</a></li>
<li><a href="#coverage">What the 250 questions cover</a></li>
<li><a href="#cases">Three questions and what they demand</a></li>
<li><a href="#limits">What the scores do not settle</a></li>
<li><a href="#next">Where this goes next</a></li>
<li><a href="#construction">From candidate questions to expert review</a></li>
<li><a href="#contributors">Who built it</a></li>
</ol>
</aside>

</div>

<script defer src="/static/sciencevision/data/trajectories.js?v=13a83b72"></script>
<script defer src="/static/sciencevision/data/benchmark.js?v=e77dc041"></script>
<script defer src="/static/sciencevision/js/vendor-logos.js?v=646de54c"></script>
<script defer src="/static/sciencevision/js/trajectory.js?v=548d147e"></script>
<script defer src="/static/sciencevision/js/benchmark.js?v=ceeaf43a"></script>
<script defer src="/static/sciencevision/data/viewer-cases.js?v=215b28bd"></script>
<script defer src="/static/sciencevision/js/viewer.js?v=6a03bc18"></script>
