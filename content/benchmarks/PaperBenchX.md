Title: PaperBenchX
Date: 2026-10-08
Rank: GPT-6-Astra / Full 13.98%
Domain: AI4SCI
Summary: 93 paper-reproduction tasks across 12 research areas, scored through clean replay and evidence-backed scientific rubrics.
HeaderImage: /static/paperbenchx/cover/paperbenchx-scientist-cover.png

<link rel="stylesheet" href="/static/css/paperbenchx-benchmark.css?v=20261007">
<div class="pbxb">
<div class="pbxb-hero">
<div class="pbxb-kicker">PaperBenchX / Scientific reproduction</div>
<h2>Can AI agents reproduce published scientific results?</h2>
<p>PaperBenchX evaluates whether research agents can reconstruct experiments from papers, operate domain-native scientific software, and regenerate evidence that supports the original claims. The benchmark contains 93 tasks across 12 research areas and six scientific domains.</p>
<div class="pbxb-links">
<a href="/blog/PaperBenchX">Read the blog</a>
<a href="/benchmarks/PaperBenchX" class="primary">Leaderboard</a>
<a href="https://github.com/UniPat-AI/PaperBenchX" target="_blank" rel="noopener noreferrer">Code &amp; tasks</a>
<a href="https://arxiv.org/pdf/2610.39744" target="_blank" rel="noopener noreferrer">Paper</a>
</div>
</div>

<div class="pbxb-highlights">
<div class="pbxb-highlight"><strong>13.98%</strong><span>Top Full rate / 13 of 93 tasks</span></div>
<div class="pbxb-highlight"><strong>59.08%</strong><span>Top Partial score / GPT-6-Astra</span></div>
<div class="pbxb-highlight"><strong>3,168</strong><span>Scorable criteria / 12 research areas</span></div>
</div>

<h3>Overall results</h3>
<p class="pbxb-section-intro"><strong>Full</strong> is the percentage of tasks scoring strictly above 90%. <strong>Partial</strong> averages rubric credit over the fixed 93-task set. Stage scores show where credit is earned across Modeling, Execution, and Validation; average turns describe interaction effort. Each rubric item is evaluated by either a deterministic check or an LLM judge. Items requiring scientific judgment use <strong>GPT-5.6-Sol</strong> as the shared judge across all agent configurations.</p>

<div class="pbxb-table-wrap" role="region" aria-label="PaperBenchX overall results" tabindex="0">
<table class="pbxb-table">
<thead><tr><th scope="col">Agent</th><th scope="col">Full (%)</th><th scope="col">Partial (%)</th><th scope="col">Modeling</th><th scope="col">Execution</th><th scope="col">Validation</th><th scope="col">Avg turns</th></tr></thead>
<tbody>
<tr><td class="pbxb-model">GPT-6-Astra <span>(Codex)</span></td><td class="pbxb-best">13.98</td><td class="pbxb-best">59.08</td><td class="pbxb-best">72.72</td><td>69.35</td><td class="pbxb-best">52.76</td><td>348.7</td></tr>
<tr><td class="pbxb-model">Fable 5.1</td><td>12.90</td><td>58.17</td><td>71.00</td><td>69.92</td><td>51.06</td><td>113.0</td></tr>
<tr><td class="pbxb-model">Fable 5</td><td>11.83</td><td>57.96</td><td>72.13</td><td>68.99</td><td>50.39</td><td class="pbxb-efficient">112.0</td></tr>
<tr><td class="pbxb-model">GPT-5.6-Sol <span>(Codex)</span></td><td>9.68</td><td>55.07</td><td>69.85</td><td class="pbxb-best">71.23</td><td>45.29</td><td>237.8</td></tr>
<tr><td class="pbxb-model">Opus 5</td><td>7.53</td><td>52.52</td><td>66.99</td><td>67.16</td><td>47.76</td><td>259.2</td></tr>
<tr><td class="pbxb-model">Kimi-K3</td><td>7.53</td><td>49.24</td><td>62.40</td><td>60.70</td><td>42.32</td><td>185.9</td></tr>
<tr><td class="pbxb-model">Qwen3.8-Max</td><td>5.38</td><td>46.76</td><td>64.41</td><td>61.02</td><td>41.65</td><td>234.4</td></tr>
<tr><td class="pbxb-model">DeepSeek-V4.1-Flash</td><td>7.53</td><td>45.47</td><td>59.87</td><td>57.51</td><td>41.13</td><td>372.6</td></tr>
<tr><td class="pbxb-model">GLM-5.3</td><td>7.53</td><td>40.78</td><td>51.11</td><td>51.85</td><td>37.06</td><td>290.8</td></tr>
<tr><td class="pbxb-model">HY3</td><td>2.15</td><td>27.53</td><td>36.83</td><td>40.59</td><td>19.67</td><td>197.4</td></tr>
</tbody>
</table>
</div>

<div class="pbxb-takeaway"><strong>What the results show.</strong> The leading system earns substantial partial credit but fully reproduces only 13 of 93 tasks. Modeling and execution are stronger than validation across the cohort, showing that running scientific software is not enough: agents must also produce replayable evidence that supports the intended scientific claim.</div>

<div class="pbxb-footer">PaperBenchX / <a href="/blog/PaperBenchX">Read the methodology and analysis</a></div>
</div>
