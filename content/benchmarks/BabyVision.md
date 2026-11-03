Title: BabyVision
Date: 2026-01-12
Rank: 🏆 Qwen3.8-Max: 91.3%
Domain: Visual Reasoning
Summary: A benchmark for visual reasoning that challenges frontier MLLMs yet 3-year-olds can solve.
HeaderImage: /static/images/babyvision/baby_logo2.png

<style>
/* ============================================
   BabyVision Benchmarks Styles
   ============================================ */

.bv-lb-hero {
    text-align: center;
    padding: 40px 0 30px;
    margin-bottom: 30px;
}

.bv-lb-hero h1 {
    font-size: 2.2em;
    margin-bottom: 12px;
    color: var(--text, #0f172a);
}

.bv-lb-hero .subtitle {
    font-size: 1.1em;
    color: var(--muted, #6b7280);
    max-width: 700px;
    margin: 0 auto 24px;
    line-height: 1.6;
}

.bv-lb-links {
    display: flex;
    justify-content: center;
    gap: 16px;
    flex-wrap: wrap;
    margin-top: 20px;
}

.bv-lb-link {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 20px;
    border: 1px solid var(--border, #e5e7eb);
    border-radius: 8px;
    font-size: 14px;
    font-weight: 600;
    transition: all 0.2s ease;
    text-decoration: none !important;
}

.bv-lb-link:hover {
    background: var(--pill, #f1f5f9);
    border-color: var(--accent, #111827);
    text-decoration: none !important;
}

.bv-lb-link svg {
    width: 18px;
    height: 18px;
}

/* ============================================
   Interactive Timeline Chart - Dark Theme
   ============================================ */

.bv-chart-container {
    margin: 40px 0;
    padding: 20px;
    background: #0a0a0a;
    border-radius: 12px;
    border: 1px solid #222;
}

.bv-chart-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
    flex-wrap: wrap;
    gap: 12px;
    padding: 0 8px;
}

.bv-chart-title {
    font-size: 1.1em;
    font-weight: 600;
    margin: 0;
    color: #ffffff;
}

.bv-chart-legend {
    display: flex;
    gap: 16px;
    font-size: 12px;
    flex-wrap: wrap;
}

.bv-legend-item {
    display: flex;
    align-items: center;
    gap: 6px;
    color: #888;
}

.bv-legend-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
}

.bv-legend-dot.open { background: #1e93ff; }
.bv-legend-dot.closed { background: #ff841c; }
.bv-legend-dot.human { background: #4ecc30; }

.bv-legend-line {
    width: 16px;
    height: 2px;
    background: repeating-linear-gradient(90deg, #4ecc30 0, #4ecc30 4px, transparent 4px, transparent 8px);
}

/* Chart Area - Dark Background */
.bv-chart-area {
    position: relative;
    width: 100%;
    height: 520px;
    background: #000;
    border-radius: 8px;
    overflow: visible;
}

.bv-chart-grid {
    position: absolute;
    inset: 45px 60px 55px 65px;
}

/* Y-Axis */
.bv-y-axis {
    position: absolute;
    left: 0;
    top: 45px;
    bottom: 55px;
    width: 65px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding-right: 10px;
}

.bv-y-label {
    font-size: 12px;
    color: #666;
    text-align: right;
    transform: translateY(50%);
}

.bv-y-title {
    position: absolute;
    left: 6px;
    top: 50%;
    transform: rotate(-90deg) translateX(-50%);
    transform-origin: left center;
    font-size: 12px;
    font-weight: 500;
    color: #777;
    white-space: nowrap;
}

/* X-Axis */
.bv-x-axis {
    position: absolute;
    left: 65px;
    right: 60px;
    bottom: 0;
    height: 55px;
    display: flex;
    justify-content: space-between;
    padding-top: 10px;
}

.bv-x-label {
    font-size: 12px;
    color: #666;
    text-align: center;
}

.bv-x-title {
    position: absolute;
    bottom: 6px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 12px;
    font-weight: 500;
    color: #777;
}

/* Grid Lines - Subtle */
.bv-grid-lines {
    position: absolute;
    inset: 0;
}

.bv-grid-line-h {
    position: absolute;
    left: 0;
    right: 0;
    height: 1px;
    background: #1a1a1a;
}

.bv-grid-line-v {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 1px;
    background: #1a1a1a;
}

/* Release Date Vertical Line */
.bv-release-line {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 0;
    border-left: 2px dashed #ef4444;
    z-index: 5;
    opacity: 0.7;
}

.bv-release-label {
    position: absolute;
    top: -22px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 12px;
    font-weight: 600;
    color: #ef4444;
    background: rgba(0,0,0,0.85);
    padding: 3px 8px;
    border-radius: 4px;
    white-space: nowrap;
}

/* Human Baseline */
.bv-human-line {
    position: absolute;
    left: 0;
    right: 0;
    height: 0;
    border-top: 2px dashed #4ecc30;
    z-index: 5;
    opacity: 0.7;
}

.bv-human-label {
    position: absolute;
    right: 10px;
    top: -22px;
    font-size: 12px;
    font-weight: 600;
    color: #4ecc30;
    background: rgba(0,0,0,0.85);
    padding: 3px 8px;
    border-radius: 4px;
}

/* Data Points - Small Circles with Labels */
.bv-data-point {
    position: absolute;
    transform: translate(-50%, -50%);
    z-index: 10;
    cursor: pointer;
}

.bv-data-point:hover {
    z-index: 20;
}

.bv-data-point:hover .bv-point-marker {
    transform: scale(1.4);
    box-shadow: 0 0 14px currentColor;
}

.bv-data-point:hover .bv-point-tooltip {
    opacity: 1;
    visibility: visible;
    transform: translateY(-10px);
}

.bv-point-marker {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
    box-shadow: 0 0 8px currentColor;
}

.bv-point-marker.open {
    background: #1e93ff;
    color: #1e93ff;
}
.bv-point-marker.closed {
    background: #ff841c;
    color: #ff841c;
}

/* Model Name Label - Always Visible */
.bv-point-name {
    position: absolute;
    font-size: 11px;
    font-weight: 500;
    line-height: 1;
    color: #bbb;
    white-space: nowrap;
    pointer-events: none;
    text-shadow: 0 1px 3px rgba(0,0,0,0.9);
}

/* Tooltip on Hover */
.bv-point-tooltip {
    position: absolute;
    bottom: calc(100% + 12px);
    left: 50%;
    transform: translateX(-50%) translateY(0);
    background: rgba(30, 30, 30, 0.95);
    color: #fff;
    padding: 8px 12px;
    border-radius: 6px;
    font-size: 11px;
    white-space: nowrap;
    opacity: 0;
    visibility: hidden;
    pointer-events: none;
    transition: all 0.15s ease;
    border: 1px solid #333;
    z-index: 100;
}

.bv-point-tooltip::after {
    content: '';
    position: absolute;
    top: 100%;
    left: 50%;
    transform: translateX(-50%);
    border: 5px solid transparent;
    border-top-color: rgba(30, 30, 30, 0.95);
}

.bv-point-tooltip-name {
    font-weight: 600;
    margin-bottom: 3px;
    color: #fff;
}

.bv-point-tooltip-info {
    font-size: 10px;
    color: #999;
}

.bv-point-tooltip-score {
    font-size: 13px;
    font-weight: 700;
    margin-top: 4px;
}

.bv-point-tooltip-score.open { color: #1e93ff; }
.bv-point-tooltip-score.closed { color: #ff841c; }

/* Chart Caption */
.bv-chart-caption {
    text-align: center;
    font-size: 11px;
    color: #666;
    margin-top: 12px;
    line-height: 1.5;
}

/* Stats Cards */
.bv-lb-stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 16px;
    margin: 30px 0;
}

.bv-lb-stat-card {
    padding: 20px;
    border: 1px solid var(--border, #e5e7eb);
    border-radius: 12px;
    text-align: center;
    background: var(--bg, #ffffff);
}

.bv-lb-stat-value {
    font-size: 2em;
    font-weight: 700;
    color: var(--text, #0f172a);
    margin-bottom: 4px;
}

.bv-lb-stat-label {
    font-size: 13px;
    color: var(--muted, #6b7280);
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Sample Distribution */
.bv-lb-distribution {
    margin: 40px 0;
    padding: 24px;
    border: 1px solid var(--border, #e5e7eb);
    border-radius: 16px;
}

.bv-lb-distribution h2 {
    margin-bottom: 20px;
}

.bv-lb-category-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
}

.bv-lb-category {
    padding: 16px;
    background: var(--pill, #f1f5f9);
    border-radius: 10px;
    border-left: 4px solid;
}

.bv-lb-category.discrimination { border-left-color: #3b82f6; }
.bv-lb-category.tracking { border-left-color: #8b5cf6; }
.bv-lb-category.spatial { border-left-color: #22c55e; }
.bv-lb-category.pattern { border-left-color: #f59e0b; }

.bv-lb-category-title {
    font-weight: 700;
    margin-bottom: 8px;
}

.bv-lb-category-count {
    font-size: 1.5em;
    font-weight: 700;
    color: var(--muted, #6b7280);
}

.bv-lb-category-types {
    font-size: 12px;
    color: var(--muted, #6b7280);
    margin-top: 8px;
}

/* Benchmarks Table */
.bv-lb-table-section {
    margin: 40px 0;
}

.bv-lb-table-section h2 {
    margin-bottom: 20px;
}

.bv-lb-table-wrapper {
    overflow-x: auto;
    border: 1px solid var(--border, #e5e7eb);
    border-radius: 12px;
}

.bv-lb-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
}

.bv-lb-table thead {
    background: var(--pill, #f1f5f9);
}

.bv-lb-table th {
    padding: 14px 16px;
    text-align: left;
    font-weight: 700;
    border-bottom: 2px solid var(--border, #e5e7eb);
    white-space: nowrap;
}

.bv-lb-table td {
    padding: 12px 16px;
    border-bottom: 1px solid var(--border, #e5e7eb);
}

.bv-lb-table tbody tr:hover {
    background: var(--pill, #f1f5f9);
}

.bv-lb-table tbody tr:last-child td {
    border-bottom: none;
}

.bv-lb-rank {
    font-weight: 700;
    width: 50px;
}

.bv-lb-rank-1 { color: #fbbf24; }
.bv-lb-rank-2 { color: #9ca3af; }
.bv-lb-rank-3 { color: #d97706; }

.bv-lb-model-name {
    font-weight: 600;
}

.bv-lb-model-type {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 600;
    margin-left: 8px;
}

.bv-lb-type-open { background: #dbeafe; color: #1d4ed8; }
.bv-lb-type-closed { background: #ede9fe; color: #7c3aed; }
.bv-lb-type-human { background: #dcfce7; color: #16a34a; }

.bv-lb-score {
    font-weight: 700;
    font-size: 15px;
}

.bv-lb-bar {
    height: 8px;
    background: var(--border, #e5e7eb);
    border-radius: 4px;
    overflow: hidden;
    min-width: 100px;
}

.bv-lb-bar-fill {
    height: 100%;
    border-radius: 4px;
    transition: width 0.3s ease;
}

.bv-lb-bar-open { background: #3b82f6; }
.bv-lb-bar-closed { background: #ff841c; }
.bv-lb-bar-human { background: #22c55e; }

/* Detailed Results Section */
.bv-lb-detailed {
    margin: 40px 0;
    padding: 24px;
    border: 1px solid var(--border, #e5e7eb);
    border-radius: 16px;
}

.bv-lb-detailed h2 {
    margin-bottom: 8px;
}

.bv-lb-detailed-note {
    font-size: 13px;
    color: var(--muted, #6b7280);
    margin-bottom: 20px;
}

/* About Section */
.bv-lb-about {
    margin: 40px 0;
    padding: 24px;
    background: linear-gradient(135deg, #f0f9ff 0%, #faf5ff 100%);
    border-radius: 16px;
    border: 1px solid var(--border, #e5e7eb);
}

.bv-lb-about h2 {
    margin-bottom: 16px;
}

.bv-lb-about p {
    color: var(--muted, #6b7280);
    line-height: 1.7;
}

/* Footer Links */
.bv-lb-footer {
    margin: 40px 0 20px;
    text-align: center;
    padding: 24px;
    border-top: 1px solid var(--border, #e5e7eb);
}

.bv-lb-footer p {
    color: var(--muted, #6b7280);
    font-size: 13px;
}

/* ============================================
   Mobile Responsive Styles
   ============================================ */

/* Tablet breakpoint */
@media (max-width: 992px) {
    .bv-lb-hero { padding: 30px 0 20px; }
    .bv-lb-hero h1 { font-size: 1.9em; }
    .bv-lb-stats { grid-template-columns: repeat(2, 1fr); gap: 12px; }
    .bv-lb-category-grid { grid-template-columns: repeat(2, 1fr); }
}

/* Mobile breakpoint */
@media (max-width: 768px) {
    /* Hero Section */
    .bv-lb-hero { padding: 20px 0 15px; margin-bottom: 20px; }
    .bv-lb-hero h1 { font-size: 1.5em; line-height: 1.3; }
    .bv-lb-hero .subtitle { font-size: 0.95em; padding: 0 10px; }

    /* Links */
    .bv-lb-links {
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: center;
        gap: 8px;
    }
    .bv-lb-link {
        padding: 8px 14px;
        font-size: 12px;
        gap: 5px;
    }
    .bv-lb-link svg { width: 14px; height: 14px; }

    /* Stats Cards */
    .bv-lb-stats {
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
        margin: 20px 0;
    }
    .bv-lb-stat-card { padding: 14px 10px; }
    .bv-lb-stat-value { font-size: 1.5em; }
    .bv-lb-stat-label { font-size: 10px; letter-spacing: 0.5px; }

    /* Chart Container */
    .bv-chart-container {
        padding: 12px;
        margin: 25px 0;
        border-radius: 10px;
    }
    .bv-chart-header {
        flex-direction: column;
        align-items: flex-start;
        gap: 10px;
        margin-bottom: 12px;
    }
    .bv-chart-title { font-size: 1em; }
    .bv-chart-legend {
        gap: 12px;
        font-size: 10px;
    }
    .bv-legend-dot { width: 6px; height: 6px; }

    /* Chart Area - Optimized for Mobile */
    .bv-chart-area {
        height: 300px;
        overflow: visible;
    }
    .bv-chart-grid { inset: 30px 15px 35px 35px; }
    .bv-y-axis {
        width: 35px;
        top: 30px;
        bottom: 35px;
    }
    .bv-y-label { font-size: 8px; }
    .bv-y-title { font-size: 8px; left: 2px; }
    .bv-x-axis {
        left: 35px;
        right: 15px;
        height: 35px;
        padding-top: 6px;
    }
    .bv-x-label { font-size: 7px; }
    .bv-x-title { font-size: 8px; bottom: 2px; }

    /* Data Points - Smaller on Mobile */
    /* Keep the right-most labels inside the chart on narrow screens */
    .bv-point-name .bv-pn-suffix { display: none; }
    .bv-point-name.bv-pn-tight { left: auto !important; right: 8px !important; }
    .bv-point-marker { width: 8px; height: 8px; }
    .bv-point-name {
        font-size: 6px;
        display: block; /* Keep labels visible on mobile */
    }
    .bv-human-label { font-size: 8px; padding: 1px 4px; }
    .bv-release-label { font-size: 8px; padding: 1px 4px; }

    /* Tooltip adjustments for touch */
    .bv-point-tooltip {
        font-size: 10px;
        padding: 6px 10px;
    }
    .bv-point-tooltip-name { font-size: 11px; }
    .bv-point-tooltip-info { font-size: 9px; }
    .bv-point-tooltip-score { font-size: 12px; }

    .bv-chart-caption { font-size: 10px; margin-top: 10px; }

    /* Category Grid */
    .bv-lb-category-grid { grid-template-columns: 1fr; gap: 12px; }
    .bv-lb-category { padding: 12px; }
    .bv-lb-category-title { font-size: 14px; }
    .bv-lb-category-count { font-size: 1.2em; }
    .bv-lb-category-types { font-size: 11px; }

    /* Distribution Section */
    .bv-lb-distribution { padding: 16px; margin: 25px 0; }
    .bv-lb-distribution h2 { font-size: 1.2em; margin-bottom: 15px; }

    /* Table - Critical for Mobile */
    .bv-lb-table-section { margin: 25px 0; }
    .bv-lb-table-section h2 { font-size: 1.2em; margin-bottom: 15px; }
    .bv-lb-table-wrapper {
        border-radius: 8px;
        -webkit-overflow-scrolling: touch; /* Smooth scroll on iOS */
    }
    .bv-lb-table {
        font-size: 11px;
        min-width: 600px; /* Allow horizontal scroll */
    }
    .bv-lb-table th {
        padding: 10px 8px;
        font-size: 10px;
        position: sticky;
        top: 0;
        background: var(--pill, #f1f5f9);
    }
    .bv-lb-table td { padding: 8px; }
    .bv-lb-rank { width: 35px; }
    .bv-lb-model-name { font-size: 11px; }
    .bv-lb-model-type {
        font-size: 8px;
        padding: 1px 5px;
        margin-left: 4px;
    }
    .bv-lb-score { font-size: 12px; }
    .bv-lb-bar { min-width: 60px; height: 6px; }

    /* About/Citation Section */
    .bv-lb-about {
        padding: 16px;
        margin: 25px 0;
        border-radius: 12px;
    }
    .bv-lb-about h2 { font-size: 1.1em; margin-bottom: 12px; }
    .bv-lb-about p { font-size: 13px; line-height: 1.6; }
    .bv-lb-about pre {
        font-size: 9px;
        padding: 12px;
        line-height: 1.4;
    }

    /* Footer */
    .bv-lb-footer {
        padding: 16px;
        margin: 25px 0 10px;
    }
    .bv-lb-footer p { font-size: 11px; }
}

/* Small phone breakpoint */
@media (max-width: 480px) {
    .bv-lb-hero h1 { font-size: 1.3em; }
    .bv-lb-hero .subtitle { font-size: 0.85em; }

    .bv-lb-links { gap: 6px; }
    .bv-lb-link {
        padding: 6px 10px;
        font-size: 11px;
    }

    .bv-lb-stats { gap: 8px; }
    .bv-lb-stat-card { padding: 12px 8px; }
    .bv-lb-stat-value { font-size: 1.3em; }
    .bv-lb-stat-label { font-size: 9px; }

    .bv-chart-area { height: 280px; }
    .bv-chart-grid { inset: 25px 10px 30px 30px; }
    .bv-y-axis { width: 30px; top: 25px; bottom: 30px; }
    .bv-x-axis { left: 30px; right: 10px; height: 30px; }
    .bv-point-marker { width: 6px; height: 6px; }
    .bv-point-name { font-size: 5px; } /* Smaller but still visible */

    .bv-lb-table { font-size: 10px; min-width: 550px; }
    .bv-lb-table th { padding: 8px 6px; font-size: 9px; }
    .bv-lb-table td { padding: 6px; }

    .bv-lb-about pre { font-size: 8px; padding: 10px; }
}

/* Touch-friendly interactions */
@media (hover: none) and (pointer: coarse) {
    /* Make data points larger touch targets on touch devices */
    .bv-data-point {
        padding: 8px;
        margin: -8px;
    }

    .bv-point-marker {
        width: 10px;
        height: 10px;
    }

    /* Ensure labels are visible on touch devices */
    .bv-point-name {
        display: block;
        font-size: 7px;
    }

    /* Show tooltip on tap (via :active) */
    .bv-data-point:active .bv-point-tooltip {
        opacity: 1;
        visibility: visible;
        transform: translateY(-8px);
    }

    /* Larger touch targets for links */
    .bv-lb-link {
        min-height: 44px;
        display: inline-flex;
        align-items: center;
    }

    /* Scroll hint for tables */
    .bv-lb-table-wrapper::after {
        content: '';
        position: absolute;
        right: 0;
        top: 0;
        bottom: 0;
        width: 30px;
        background: linear-gradient(to right, transparent, rgba(0,0,0,0.05));
        pointer-events: none;
    }
    .bv-lb-table-wrapper {
        position: relative;
    }
}

/* Landscape phone orientation */
@media (max-width: 768px) and (orientation: landscape) {
    .bv-chart-area { height: 250px; }
    .bv-lb-hero { padding: 15px 0 10px; }
    .bv-lb-stats { grid-template-columns: repeat(4, 1fr); }
}
</style>


<!-- Key Statistics -->
<!-- <div class="bv-lb-stats">
    <div class="bv-lb-stat-card">
        <div class="bv-lb-stat-value">94.1%</div>
        <div class="bv-lb-stat-label">Human Performance</div>
    </div>
    <div class="bv-lb-stat-card">
        <div class="bv-lb-stat-value">49.7%</div>
        <div class="bv-lb-stat-label">Best AI Model</div>
    </div>
    <div class="bv-lb-stat-card">
        <div class="bv-lb-stat-value">44.4%</div>
        <div class="bv-lb-stat-label">Gap to Human</div>
    </div>
    <div class="bv-lb-stat-card">
        <div class="bv-lb-stat-value">22</div>
        <div class="bv-lb-stat-label">Task Types</div>
    </div>
</div> -->

<!-- Interactive Timeline Chart -->
<div class="bv-chart-container">
    <div class="bv-chart-header">
        <h2 class="bv-chart-title">BabyVision Performance Timeline</h2>
        <div class="bv-chart-legend">
            <div class="bv-legend-item">
                <div class="bv-legend-dot open"></div>
                <span>Open</span>
            </div>
            <div class="bv-legend-item">
                <div class="bv-legend-dot closed"></div>
                <span>Proprietary</span>
            </div>
            <div class="bv-legend-item">
                <div class="bv-legend-line"></div>
                <span>Human (94.1%)</span>
            </div>
        </div>
    </div>

    <div class="bv-chart-area" id="bv-timeline-chart">
        <!-- Y-Axis -->
        <div class="bv-y-title">Performance (%)</div>
        <div class="bv-y-axis">
            <div class="bv-y-label">100</div>
            <div class="bv-y-label">80</div>
            <div class="bv-y-label">60</div>
            <div class="bv-y-label">40</div>
            <div class="bv-y-label">20</div>
            <div class="bv-y-label">0</div>
        </div>

        <!-- X-Axis -->
        <div class="bv-x-axis">
            <div class="bv-x-label">Apr 2025</div>
            <div class="bv-x-label">Jun 2025</div>
            <div class="bv-x-label">Aug 2025</div>
            <div class="bv-x-label">Oct 2025</div>
            <div class="bv-x-label">Dec 2025</div>
            <div class="bv-x-label">Feb 2026</div>
            <div class="bv-x-label">Apr 2026</div>
            <div class="bv-x-label">Jun 2026</div>
            <div class="bv-x-label">Aug 2026</div>
            <div class="bv-x-label">Oct 2026</div>
        </div>
        <div class="bv-x-title">Release Date</div>

        <!-- Chart Grid -->
        <div class="bv-chart-grid">
            <!-- Grid Lines -->
            <div class="bv-grid-lines">
                <div class="bv-grid-line-h" style="top: 0%"></div>
                <div class="bv-grid-line-h" style="top: 20%"></div>
                <div class="bv-grid-line-h" style="top: 40%"></div>
                <div class="bv-grid-line-h" style="top: 60%"></div>
                <div class="bv-grid-line-h" style="top: 80%"></div>
                <div class="bv-grid-line-h" style="top: 100%"></div>
                <div class="bv-grid-line-v" style="left: 0%"></div>
                <div class="bv-grid-line-v" style="left: 25%"></div>
                <div class="bv-grid-line-v" style="left: 50%"></div>
                <div class="bv-grid-line-v" style="left: 75%"></div>
                <div class="bv-grid-line-v" style="left: 100%"></div>
            </div>

            <!-- Human Baseline Line -->
            <div class="bv-human-line" style="top: 5.9%">
                <span class="bv-human-label">Human 94.1%</span>
            </div>

            <!-- Leaderboard Release Date Line -->
            <div class="bv-release-line" style="left: 52.2%">
                <span class="bv-release-label">Leaderboard Release</span>
            </div>

            <!-- Data Points with small circles and text labels -->

            <!-- KimiVL-A3B: Apr 10, 12.4% -->
            <div class="bv-data-point" style="left: 1.6%; top: 87.6%">
                <div class="bv-point-marker open"></div>
                <span class="bv-point-name" style="left: 14px; top: 5px;">Kimi-VL</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">KimiVL-A3B</div>
                    <div class="bv-point-tooltip-info">Moonshot AI · Apr 10, 2025</div>
                    <div class="bv-point-tooltip-score open">12.4%</div>
                </div>
            </div>

            <!-- Kimi-K2.5: Jan 27, 36.5% -->
            <div class="bv-data-point" style="left: 54.9%; top: 63.5%">
                <div class="bv-point-marker open"></div>
                <span class="bv-point-name" style="left: 14px; top: -3px;">Kimi K2.5</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">Kimi-K2.5</div>
                    <div class="bv-point-tooltip-info">Moonshot AI · Jan 27, 2026</div>
                    <div class="bv-point-tooltip-score open">36.5%</div>
                </div>
            </div>

            <!-- MimoVL-7B-RL: Apr 23, 15.1% -->
            <div class="bv-data-point" style="left: 4.0%; top: 84.9%">
                <div class="bv-point-marker open"></div>
                <span class="bv-point-name" style="left: 14px; top: -3px;">MiMo-VL</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">MimoVL-7B-RL</div>
                    <div class="bv-point-tooltip-info">Xiaomi · Apr 23, 2025</div>
                    <div class="bv-point-tooltip-score open">15.1%</div>
                </div>
            </div>

            <!-- Grok-4: Jul 9, 16.2% -->
            <div class="bv-data-point" style="left: 18.1%; top: 83.8%">
                <div class="bv-point-marker closed"></div>
                <span class="bv-point-name" style="left: 14px; top: -15px;">Grok 4</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">Grok-4</div>
                    <div class="bv-point-tooltip-info">xAI · Jul 9, 2025</div>
                    <div class="bv-point-tooltip-score closed">16.2%</div>
                </div>
            </div>

            <!-- Step3: Jul 31, 14.7% -->
            <div class="bv-data-point" style="left: 22.1%; top: 85.3%">
                <div class="bv-point-marker open"></div>
                <span class="bv-point-name" style="left: 14px; top: -3px;">Step3</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">Step3</div>
                    <div class="bv-point-tooltip-info">StepFun · Jul 31, 2025</div>
                    <div class="bv-point-tooltip-score open">14.7%</div>
                </div>
            </div>

            <!-- InternVL3.5-241B: Aug 26, 19.2% -->
            <div class="bv-data-point" style="left: 26.8%; top: 80.8%">
                <div class="bv-point-marker open"></div>
                <span class="bv-point-name" style="left: 14px; top: 14px;">InternVL3.5</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">InternVL3.5-241B</div>
                    <div class="bv-point-tooltip-info">OpenGVLab · Aug 26, 2025</div>
                    <div class="bv-point-tooltip-score open">19.2%</div>
                </div>
            </div>

            <!-- Qwen3VL-235B-Thinking: Sep 23, 22.2% -->
            <div class="bv-data-point" style="left: 31.9%; top: 77.8%">
                <div class="bv-point-marker open"></div>
                <span class="bv-point-name" style="left: 14px; top: -3px;">Qwen3-VL</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">Qwen3VL-235B-Thinking</div>
                    <div class="bv-point-tooltip-info">Alibaba · Sep 23, 2025</div>
                    <div class="bv-point-tooltip-score open">22.2%</div>
                </div>
            </div>

            <!-- Qwen3-VL-Plus: Sep 23, 19.2% -->
            <div class="bv-data-point" style="left: 31.9%; top: 80.8%">
                <div class="bv-point-marker closed"></div>
                <span class="bv-point-name" style="left: 14px; top: -3px;">Qwen3-VL-Plus</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">Qwen3-VL-Plus</div>
                    <div class="bv-point-tooltip-info">Alibaba · Sep 23, 2025</div>
                    <div class="bv-point-tooltip-score closed">19.2%</div>
                </div>
            </div>

            <!-- Gemini3-Pro-Preview: Nov 18, 49.7% -->
            <div class="bv-data-point" style="left: 42.2%; top: 50.3%">
                <div class="bv-point-marker closed"></div>
                <span class="bv-point-name" style="left: 14px; top: -3px;">Gemini 3 Pro</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">Gemini-3.0-Pro</div>
                    <div class="bv-point-tooltip-info">Google · Nov 18, 2025</div>
                    <div class="bv-point-tooltip-score closed">49.7%</div>
                </div>
            </div>

            <!-- Claude-4.5-Opus: Nov 24, 14.2% -->
            <div class="bv-data-point" style="left: 43.2%; top: 85.8%">
                <div class="bv-point-marker closed"></div>
                <span class="bv-point-name" style="left: 14px; top: 14px; line-height: 1;">Claude Opus 4.5</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">Claude-4.5-Opus</div>
                    <div class="bv-point-tooltip-info">Anthropic · Nov 24, 2025</div>
                    <div class="bv-point-tooltip-score closed">14.2%</div>
                </div>
            </div>

            <!-- GLM4.6V: Dec 8, 17.6% -->
            <div class="bv-data-point" style="left: 45.8%; top: 82.4%">
                <div class="bv-point-marker open"></div>
                <span class="bv-point-name" style="left: 14px; top: -3px; line-height: 1;">GLM-4.6V</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">GLM4.6V</div>
                    <div class="bv-point-tooltip-info">Zhipu AI · Dec 8, 2025</div>
                    <div class="bv-point-tooltip-score open">17.6%</div>
                </div>
            </div>

            <!-- GPT-5.2: Dec 11, 34.4% -->
            <div class="bv-data-point" style="left: 46.4%; top: 65.6%">
                <div class="bv-point-marker closed"></div>
                <span class="bv-point-name" style="right: 14px; top: -3px; left: auto;">GPT-5.2</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">GPT-5.2</div>
                    <div class="bv-point-tooltip-info">OpenAI · Dec 11, 2025</div>
                    <div class="bv-point-tooltip-score closed">34.4%</div>
                </div>
            </div>

            <!-- Seed-1.8: Dec 18, 30.2% -->
            <div class="bv-data-point" style="left: 47.6%; top: 69.8%">
                <div class="bv-point-marker closed"></div>
                <span class="bv-point-name" style="right: 14px; top: -3px; left: auto;">Seed 1.8</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">Seed-1.8</div>
                    <div class="bv-point-tooltip-info">ByteDance · Dec 18, 2025</div>
                    <div class="bv-point-tooltip-score closed">30.2%</div>
                </div>
            </div>

            <!-- Claude-Opus-4.6: Feb 5, 14.8% -->
            <div class="bv-data-point" style="left: 56.6%; top: 85.2%">
                <div class="bv-point-marker closed"></div>
                <span class="bv-point-name" style="left: 14px; top: -14px; line-height: 1;">Claude Opus 4.6</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">Claude-Opus-4.6</div>
                    <div class="bv-point-tooltip-info">Anthropic · Feb 5, 2026</div>
                    <div class="bv-point-tooltip-score closed">14.8%</div>
                </div>
            </div>

            <!-- Seed-2.0: Feb 14, 60.6% -->
            <div class="bv-data-point" style="left: 58.2%; top: 39.4%">
                <div class="bv-point-marker closed"></div>
                <span class="bv-point-name" style="left: 14px; top: -3px;">Seed 2.0 Pro</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">Seed-2.0 (high)</div>
                    <div class="bv-point-tooltip-info">ByteDance · Feb 14, 2026</div>
                    <div class="bv-point-tooltip-score closed">60.6%</div>
                </div>
            </div>

            <!-- Qwen3.5-397B-A17B: Feb 16, 43.3% -->
            <div class="bv-data-point" style="left: 58.6%; top: 56.7%">
                <div class="bv-point-marker open"></div>
                <span class="bv-point-name" style="left: 14px; top: -3px;">Qwen3.5</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">Qwen3.5-397B-A17B</div>
                    <div class="bv-point-tooltip-info">Alibaba · Feb 16, 2026</div>
                    <div class="bv-point-tooltip-score open">43.3%</div>
                </div>
            </div>

            <!-- Gemini-3.1-Pro: Feb 23, 51.6% -->
            <div class="bv-data-point" style="left: 59.9%; top: 48.4%">
                <div class="bv-point-marker closed"></div>
                <span class="bv-point-name" style="left: 14px; top: -15px;">Gemini 3.1 Pro</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">Gemini-3.1-Pro</div>
                    <div class="bv-point-tooltip-info">Google · Feb 23, 2026</div>
                    <div class="bv-point-tooltip-score closed">51.6%</div>
                </div>
            </div>

            <!-- GPT-5.4 (xhigh): Mar 5, 49.7% -->
            <div class="bv-data-point" style="left: 61.7%; top: 50.3%">
                <div class="bv-point-marker closed"></div>
                <span class="bv-point-name" style="left: 14px; top: -3px;">GPT-5.4</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">GPT-5.4 (xhigh)</div>
                    <div class="bv-point-tooltip-info">OpenAI · Mar 5, 2026</div>
                    <div class="bv-point-tooltip-score closed">49.7%</div>
                </div>
            </div>

            <!-- GPT-5.5 (xhigh): Apr 23, 2026, 83.6% -->
            <div class="bv-data-point" style="left: 70.6%; top: 16.4%">
                <div class="bv-point-marker closed"></div>
                <span class="bv-point-name" style="right: 14px; top: -3px; left: auto;">GPT-5.5</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">GPT-5.5 (xhigh) (with tools)</div>
                    <div class="bv-point-tooltip-info">OpenAI · Apr 23, 2026</div>
                    <div class="bv-point-tooltip-score closed">83.6%</div>
                </div>
            </div>

            <!-- Claude-Opus-4.8 (max): May 28, 2026, 81.2% -->
            <div class="bv-data-point" style="left: 77.0%; top: 18.8%">
                <div class="bv-point-marker closed"></div>
                <span class="bv-point-name" style="right: 14px; top: 6px; left: auto;">Claude Opus 4.8</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">Claude-Opus-4.8 (max) (with tools)</div>
                    <div class="bv-point-tooltip-info">Anthropic · May 28, 2026</div>
                    <div class="bv-point-tooltip-score closed">81.2%</div>
                </div>
            </div>

            <!-- Qwen3.7-Plus (with tools): Jun 2, 2026, 70.4% -->
            <div class="bv-data-point" style="left: 77.9%; top: 29.6%">
                <div class="bv-point-marker closed"></div>
                <span class="bv-point-name" style="left: 14px; top: 4px;">Qwen3.7-Plus</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">Qwen3.7-Plus (with tools)</div>
                    <div class="bv-point-tooltip-info">Alibaba · Jun 2, 2026</div>
                    <div class="bv-point-tooltip-score closed">70.4%</div>
                </div>
            </div>

            <!-- Seed-2.1-Pro: Jun 23, 2026, 73.7% -->
            <div class="bv-data-point" style="left: 81.8%; top: 26.3%">
                <div class="bv-point-marker closed"></div>
                <span class="bv-point-name" style="right: 14px; top: 1px; left: auto;">Seed 2.1 Pro</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">Seed-2.1-Pro</div>
                    <div class="bv-point-tooltip-info">ByteDance · Jun 23, 2026</div>
                    <div class="bv-point-tooltip-score closed">73.7%</div>
                </div>
            </div>

            <!-- Muse Spark 1.1 (with tools): Jul 9, 2026, 76.3% -->
            <div class="bv-data-point" style="left: 84.7%; top: 23.7%">
                <div class="bv-point-marker closed"></div>
                <span class="bv-point-name" style="right: 14px; top: -3px; left: auto;">Muse Spark 1.1</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">Muse Spark 1.1 (with tools)</div>
                    <div class="bv-point-tooltip-info">Meta · Jul 9, 2026</div>
                    <div class="bv-point-tooltip-score closed">76.3%</div>
                </div>
            </div>

            <!-- Kimi-K2.6 (with tools): Apr 21, 2026, 68.5% -->
            <div class="bv-data-point" style="left: 70.3%; top: 31.5%">
                <div class="bv-point-marker open"></div>
                <span class="bv-point-name" style="right: 14px; top: -3px; left: auto;">Kimi K2.6</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">Kimi-K2.6 (with tools)</div>
                    <div class="bv-point-tooltip-info">Moonshot AI · Apr 21, 2026</div>
                    <div class="bv-point-tooltip-score open">68.5%</div>
                </div>
            </div>

            <!-- Fable 5 (max) (with tools): Jun 9, 2026, 90.5% -->
            <div class="bv-data-point" style="left: 79.2%; top: 9.5%">
                <div class="bv-point-marker closed"></div>
                <span class="bv-point-name" style="right: 14px; top: -3px; left: auto; line-height: 1;">Fable 5</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">Fable 5 (max) (with tools)</div>
                    <div class="bv-point-tooltip-info">Anthropic &middot; Jun 9, 2026</div>
                    <div class="bv-point-tooltip-score closed">90.5%</div>
                </div>
            </div>

            <!-- GPT-5.6 Sol (max) (with tools): Jun 26, 2026, 88.9% -->
            <div class="bv-data-point" style="left: 82.3%; top: 11.1%">
                <div class="bv-point-marker closed"></div>
                <span class="bv-point-name" style="right: 14px; top: 8px; left: auto; line-height: 1;">GPT-5.6 Sol</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">GPT-5.6 Sol (max) (with tools)</div>
                    <div class="bv-point-tooltip-info">OpenAI &middot; Jun 26, 2026</div>
                    <div class="bv-point-tooltip-score closed">88.9%</div>
                </div>
            </div>

            <!-- Kimi K3 (with Python tools): Jul 14, 2026, 85.7% -->
            <div class="bv-data-point" style="left: 85.6%; top: 14.3%">
                <div class="bv-point-marker open"></div>
                <span class="bv-point-name" style="right: 14px; top: 10px; left: auto; line-height: 1;">Kimi K3</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">Kimi K3 (with Python tools)</div>
                    <div class="bv-point-tooltip-info">Moonshot AI &middot; Jul 14, 2026</div>
                    <div class="bv-point-tooltip-score open">85.7%</div>
                </div>
            </div>

            <!-- Qwen3.8 (with tools): Aug 3, 2026, 91.3% -->
            <div class="bv-data-point" style="left: 89.2%; top: 8.7%">
                <div class="bv-point-marker open"></div>
                <span class="bv-point-name bv-pn-tight" style="left: 14px; top: 0;">Qwen3.8-Max<span class="bv-pn-suffix"> w tool</span></span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">Qwen3.8-Max (with tools)</div>
                    <div class="bv-point-tooltip-info">Alibaba &middot; Aug 3, 2026</div>
                    <div class="bv-point-tooltip-score open">91.3%</div>
                </div>
            </div>

            <!-- Qwen3.8: Aug 3, 2026, 82.0% -->
            <div class="bv-data-point" style="left: 89.2%; top: 18.0%">
                <div class="bv-point-marker open"></div>
                <span class="bv-point-name bv-pn-tight" style="left: 14px; top: -3px;">Qwen3.8-Max</span>
                <div class="bv-point-tooltip">
                    <div class="bv-point-tooltip-name">Qwen3.8-Max</div>
                    <div class="bv-point-tooltip-info">Alibaba &middot; Aug 3, 2026</div>
                    <div class="bv-point-tooltip-score open">82.0%</div>
                </div>
            </div>
        </div>
    </div>

    <p class="bv-chart-caption">
        Hover over data points for details. Blue = Open, Orange = Proprietary. Dashed line = Human baseline (94.1%).
    </p>
</div>


<div class="bv-lb-hero">
    <p class="subtitle">
        Can MLLMs See Like a 3-Year-Old?
    </p>
    <div class="bv-lb-links">
        <a href="/blog/BabyVision" class="bv-lb-link">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M19 5v14H5V5h14m0-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-4.86 8.86l-3 3.87L9 13.14 6 17h12l-3.86-5.14z"/></svg>
            Blog
        </a>
        <a href="https://www.arxiv.org/abs/2601.06521" class="bv-lb-link" target="_blank">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>
            Paper
        </a>
        <a href="https://github.com/UniPat-AI/BabyVision" class="bv-lb-link" target="_blank">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
            GitHub
        </a>
        <a href="https://huggingface.co/collections/UnipatAI/babyvision" class="bv-lb-link" target="_blank">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>
            Dataset
        </a>
        
    </div>
</div>



<!-- Benchmarks Table -->
<div class="bv-lb-table-section">
    <h2>BabyVision Leaderboard</h2>
    <div class="bv-lb-table-wrapper">
        <table class="bv-lb-table">
            <thead>
                <tr>
                    <th>Rank</th>
                    <th>Model</th>
                    <th>Type</th>
                    <th>Company</th>
                    <th>Release Date</th>
                    <th>Score</th>
                    <th>Progress</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="bv-lb-rank">-</td>
                    <td class="bv-lb-model-name">Human<span class="bv-lb-model-type bv-lb-type-human">BASELINE</span></td>
                    <td>Human</td>
                    <td>-</td>
                    <td>-</td>
                    <td class="bv-lb-score">94.1%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-human" style="width: 94.1%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank bv-lb-rank-1">1</td>
                    <td class="bv-lb-model-name">Qwen3.8-Max (with tools)</td>
                    <td>Open</td>
                    <td>Alibaba</td>
                    <td>Aug 3, 2026</td>
                    <td class="bv-lb-score">91.3%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-open" style="width: 91.3%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank bv-lb-rank-2">2</td>
                    <td class="bv-lb-model-name">Fable 5 (max) (with tools)</td>
                    <td>Proprietary</td>
                    <td>Anthropic</td>
                    <td>Jun 9, 2026</td>
                    <td class="bv-lb-score">90.5%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-closed" style="width: 90.5%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank bv-lb-rank-3">3</td>
                    <td class="bv-lb-model-name">GPT-5.6 Sol (max) (with tools)</td>
                    <td>Proprietary</td>
                    <td>OpenAI</td>
                    <td>Jun 26, 2026</td>
                    <td class="bv-lb-score">88.9%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-closed" style="width: 88.9%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank">4</td>
                    <td class="bv-lb-model-name">Kimi K3 (with Python tools)</td>
                    <td>Open</td>
                    <td>Moonshot AI</td>
                    <td>Jul 14, 2026</td>
                    <td class="bv-lb-score">85.7%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-open" style="width: 85.7%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank">5</td>
                    <td class="bv-lb-model-name">GPT-5.5 (xhigh) (with tools)</td>
                    <td>Proprietary</td>
                    <td>OpenAI</td>
                    <td>Apr 23, 2026</td>
                    <td class="bv-lb-score">83.6%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-closed" style="width: 83.6%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank">6</td>
                    <td class="bv-lb-model-name">Qwen3.8-Max</td>
                    <td>Open</td>
                    <td>Alibaba</td>
                    <td>Aug 3, 2026</td>
                    <td class="bv-lb-score">82.0%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-open" style="width: 82.0%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank">7</td>
                    <td class="bv-lb-model-name">Claude-Opus-4.8 (max) (with tools)</td>
                    <td>Proprietary</td>
                    <td>Anthropic</td>
                    <td>May 28, 2026</td>
                    <td class="bv-lb-score">81.2%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-closed" style="width: 81.2%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank">8</td>
                    <td class="bv-lb-model-name">Muse Spark 1.1 (with tools)</td>
                    <td>Proprietary</td>
                    <td>Meta</td>
                    <td>Jul 9, 2026</td>
                    <td class="bv-lb-score">76.3%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-closed" style="width: 76.3%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank">9</td>
                    <td class="bv-lb-model-name">Seed-2.1-Pro</td>
                    <td>Proprietary</td>
                    <td>ByteDance</td>
                    <td>Jun 23, 2026</td>
                    <td class="bv-lb-score">73.7%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-closed" style="width: 73.7%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank">10</td>
                    <td class="bv-lb-model-name">Qwen3.7-Plus (with tools)</td>
                    <td>Proprietary</td>
                    <td>Alibaba</td>
                    <td>Jun 2, 2026</td>
                    <td class="bv-lb-score">70.4%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-closed" style="width: 70.4%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank">11</td>
                    <td class="bv-lb-model-name">Kimi-K2.6 (with tools)</td>
                    <td>Open</td>
                    <td>Moonshot AI</td>
                    <td>Apr 21, 2026</td>
                    <td class="bv-lb-score">68.5%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-open" style="width: 68.5%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank">12</td>
                    <td class="bv-lb-model-name">Seed-2.0-Pro (high)</td>
                    <td>Proprietary</td>
                    <td>ByteDance</td>
                    <td>Feb 14, 2026</td>
                    <td class="bv-lb-score">60.6%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-closed" style="width: 60.6%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank">13</td>
                    <td class="bv-lb-model-name">Gemini-3.1-Pro</td>
                    <td>Proprietary</td>
                    <td>Google</td>
                    <td>Feb 23, 2026</td>
                    <td class="bv-lb-score">51.6%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-closed" style="width: 51.6%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank">14</td>
                    <td class="bv-lb-model-name">Gemini-3.0-Pro</td>
                    <td>Proprietary</td>
                    <td>Google</td>
                    <td>Nov 18, 2025</td>
                    <td class="bv-lb-score">49.7%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-closed" style="width: 49.7%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank">15</td>
                    <td class="bv-lb-model-name">GPT-5.4 (xhigh)</td>
                    <td>Proprietary</td>
                    <td>OpenAI</td>
                    <td>Mar 5, 2026</td>
                    <td class="bv-lb-score">49.7%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-closed" style="width: 49.7%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank">16</td>
                    <td class="bv-lb-model-name">Qwen3.5-397B-A17B</td>
                    <td>Open</td>
                    <td>Alibaba</td>
                    <td>Feb 16, 2026</td>
                    <td class="bv-lb-score">43.3%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-open" style="width: 43.3%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank">17</td>
                    <td class="bv-lb-model-name">Kimi-K2.5</td>
                    <td>Open</td>
                    <td>Moonshot AI</td>
                    <td>Jan 27, 2026</td>
                    <td class="bv-lb-score">36.5%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-open" style="width: 36.5%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank">18</td>
                    <td class="bv-lb-model-name">GPT-5.2</td>
                    <td>Proprietary</td>
                    <td>OpenAI</td>
                    <td>Dec 11, 2025</td>
                    <td class="bv-lb-score">34.4%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-closed" style="width: 34.4%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank">19</td>
                    <td class="bv-lb-model-name">Seed-1.8</td>
                    <td>Proprietary</td>
                    <td>ByteDance</td>
                    <td>Dec 18, 2025</td>
                    <td class="bv-lb-score">30.2%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-closed" style="width: 30.2%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank">20</td>
                    <td class="bv-lb-model-name">Qwen3VL-235B-Thinking</td>
                    <td>Open</td>
                    <td>Alibaba</td>
                    <td>Sep 23, 2025</td>
                    <td class="bv-lb-score">22.2%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-open" style="width: 22.2%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank">21</td>
                    <td class="bv-lb-model-name">InternVL3.5-241B</td>
                    <td>Open</td>
                    <td>OpenGVLab</td>
                    <td>Aug 26, 2025</td>
                    <td class="bv-lb-score">19.2%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-open" style="width: 19.2%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank">22</td>
                    <td class="bv-lb-model-name">Qwen3-VL-Plus</td>
                    <td>Proprietary</td>
                    <td>Alibaba</td>
                    <td>Sep 23, 2025</td>
                    <td class="bv-lb-score">19.2%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-closed" style="width: 19.2%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank">23</td>
                    <td class="bv-lb-model-name">GLM4.6V</td>
                    <td>Open</td>
                    <td>Zhipu AI</td>
                    <td>Dec 8, 2025</td>
                    <td class="bv-lb-score">17.6%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-open" style="width: 17.6%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank">24</td>
                    <td class="bv-lb-model-name">Grok-4</td>
                    <td>Proprietary</td>
                    <td>xAI</td>
                    <td>Jul 9, 2025</td>
                    <td class="bv-lb-score">16.2%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-closed" style="width: 16.2%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank">25</td>
                    <td class="bv-lb-model-name">MimoVL-7B-RL</td>
                    <td>Open</td>
                    <td>Xiaomi</td>
                    <td>Apr 23, 2025</td>
                    <td class="bv-lb-score">15.1%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-open" style="width: 15.1%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank">26</td>
                    <td class="bv-lb-model-name">Claude-Opus-4.6</td>
                    <td>Proprietary</td>
                    <td>Anthropic</td>
                    <td>Feb 5, 2026</td>
                    <td class="bv-lb-score">14.8%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-closed" style="width: 14.8%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank">27</td>
                    <td class="bv-lb-model-name">Step3</td>
                    <td>Open</td>
                    <td>StepFun</td>
                    <td>Jul 31, 2025</td>
                    <td class="bv-lb-score">14.7%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-open" style="width: 14.7%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank">28</td>
                    <td class="bv-lb-model-name">Claude-4.5-Opus</td>
                    <td>Proprietary</td>
                    <td>Anthropic</td>
                    <td>Nov 24, 2025</td>
                    <td class="bv-lb-score">14.2%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-closed" style="width: 14.2%"></div></div></td>
                </tr>
                <tr>
                    <td class="bv-lb-rank">29</td>
                    <td class="bv-lb-model-name">KimiVL-A3B</td>
                    <td>Open</td>
                    <td>Moonshot AI</td>
                    <td>Apr 10, 2025</td>
                    <td class="bv-lb-score">12.4%</td>
                    <td><div class="bv-lb-bar"><div class="bv-lb-bar-fill bv-lb-bar-open" style="width: 12.4%"></div></div></td>
                </tr>
            </tbody>
        </table>
    </div>
</div>



<!-- Citation -->
<div class="bv-lb-about" style="background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);">
    <h2>Citation</h2>
    <p>For details of BabyVision, please read our paper. If you find it useful in your research, please kindly cite:</p>
    <pre style="background: #1e293b; color: #e2e8f0; padding: 16px; border-radius: 8px; overflow-x: auto; font-size: 12px;">
@misc{chen2026babyvisionvisualreasoninglanguage,
      title={BabyVision: Visual Reasoning Beyond Language}, 
      author={Liang Chen and Weichu Xie and Yiyan Liang and Hongfeng He and Hans Zhao and Zhibo Yang and Zhiqi Huang and Haoning Wu and Haoyu Lu and Y. charles and Yiping Bao and Yuantao Fan and Guopeng Li and Haiyang Shen and Xuanzhong Chen and Wendong Xu and Shuzheng Si and Zefan Cai and Wenhao Chai and Ziqi Huang and Fangfu Liu and Tianyu Liu and Baobao Chang and Xiaobo Hu and Kaiyuan Chen and Yixin Ren and Yang Liu and Yuan Gong and Kuan Li},
      year={2026},
      eprint={2601.06521},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2601.06521}, 
} </pre>
</div>

<!-- Footer -->
<div class="bv-lb-footer">
    <p>
        Last updated: Aug. 3, 2026 |
        <a href="mailto:contact@unipat.ai">Contact us and submit your model results</a> 
    </p>
</div>
