/* Renders the results explorer, sub-domain coverage, and the two distributions from
   window.SV_BENCHMARK (see scripts/build_web_data.py). */

(function () {
  "use strict";

  var data = window.SV_BENCHMARK;
  if (!data) return;

  // Series colours run by vendor: two greys for the OpenAI models, orange for Anthropic.
  var SERIES = ["openai-a", "openai-b", "anthropic"];
  // The tallest reported value is 0.55; the extra headroom keeps value labels off the top edge.
  var Y_MAX = 0.66;
  var TICKS = [0.6, 0.45, 0.3, 0.15, 0];

  // Display names for the access settings; the keys stay as they appear in the data.
  var SETTING_NAME = {
    "cc-3d": "Harness · 3D",
    "cc-mcp": "Harness · 3D + MCP",
    "cc-2d-6": "Harness · 2D (6 views)"
  };

  function settingName(key) {
    return SETTING_NAME[key] || key;
  }

  function settingShort(key) {
    return settingName(key).replace(/^Harness · /, "");
  }

  var DOMAIN_PREFIX = {
    architecture: "arch_",
    biology: "bio_",
    chemistry: "chem_",
    "mechanical-cad": "cad_",
    medical: "med_"
  };

  function humanise(slug, domain) {
    var prefix = DOMAIN_PREFIX[domain] || "";
    var body = slug.indexOf(prefix) === 0 ? slug.slice(prefix.length) : slug;
    var words = body.replace(/_/g, " ");
    return words.charAt(0).toUpperCase() + words.slice(1);
  }

  // Touch screens have no hover; a tap fires the same mouseover, so only the wording changes.
  var POINTING = window.matchMedia && matchMedia("(hover: none)").matches ? "tap" : "hover";

  function hint(target) {
    return POINTING + " a " + target + " for the reported value";
  }

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined) node.textContent = text;
    return node;
  }

  function fmt(value) {
    return value.toFixed(3);
  }

  var SVG_NS = "http://www.w3.org/2000/svg";

  function vendorMark(vendor, className) {
    var logos = window.SV_VENDOR_LOGOS || {};
    var mark = logos[vendor];
    if (!mark) return null;
    var svg = document.createElementNS(SVG_NS, "svg");
    svg.setAttribute("viewBox", mark.viewBox);
    svg.setAttribute("aria-hidden", "true");
    svg.setAttribute("class", className);
    if (mark.path) {
      var path = document.createElementNS(SVG_NS, "path");
      path.setAttribute("d", mark.path);
      svg.appendChild(path);
      return svg;
    }
    // Vendors Simple Icons does not carry get a letterform chip: the mark is filled with
    // the vendor colour, and the initial is knocked out of it.
    var chip = document.createElementNS(SVG_NS, "rect");
    chip.setAttribute("x", "1.5");
    chip.setAttribute("y", "1.5");
    chip.setAttribute("width", "21");
    chip.setAttribute("height", "21");
    chip.setAttribute("rx", "4.5");
    svg.appendChild(chip);
    var initial = document.createElementNS(SVG_NS, "text");
    initial.setAttribute("x", "12");
    initial.setAttribute("y", "17");
    initial.setAttribute("text-anchor", "middle");
    initial.setAttribute("font-size", "14");
    initial.setAttribute("font-weight", "700");
    initial.setAttribute("fill", "#fff");
    initial.textContent = mark.text;
    svg.appendChild(initial);
    return svg;
  }

  /* ---------- results explorer ---------- */

  var explorer = document.querySelector("[data-explorer]");
  var setting = "cc-mcp";

  function renderExplorer() {
    if (!explorer) return;
    explorer.textContent = "";

    var head = el("div", "sv-chart__head");
    var titles = el("div");
    titles.appendChild(el("h3", null, "Mean answer score by discipline and access setting"));
    var current = data.settings.filter(function (s) { return s.key === setting; })[0];
    titles.appendChild(el("p", null, current.note));
    head.appendChild(titles);

    var seg = el("div", "sv-seg");
    seg.setAttribute("role", "group");
    seg.setAttribute("aria-label", "Access setting");
    data.settings.forEach(function (item) {
      var button = el("button", null, item.key);
      button.type = "button";
      button.title = item.label;
      button.setAttribute("aria-pressed", item.key === setting ? "true" : "false");
      button.addEventListener("click", function () {
        setting = item.key;
        renderExplorer();
      });
      seg.appendChild(button);
    });
    head.appendChild(seg);
    explorer.appendChild(head);

    var plot = el("div", "sv-plot");
    var axis = el("div", "sv-plot__axis");
    TICKS.forEach(function (tick) {
      var label = el("span", null, tick.toFixed(2));
      label.style.bottom = (tick / Y_MAX * 100) + "%";
      axis.appendChild(label);
    });
    plot.appendChild(axis);

    var area = el("div", "sv-plot__area");
    var groups = data.domains.concat([{ key: "ALL", label: "Overall" }]);

    groups.forEach(function (domain) {
      var group = el("div", "sv-group");
      var bars = el("div", "sv-group__bars");

      data.models.forEach(function (model, index) {
        var value = (data.results[setting][model.key] || {})[domain.key];

        if (value === null || value === undefined) {
          var gap = el("div", "sv-bar sv-bar--none");
          gap.title = "not reported";
          bars.appendChild(gap);
          return;
        }

        var bar = el("div", "sv-bar sv-bar--" + SERIES[index]);
        bar.style.setProperty("--h", (value / Y_MAX * 100) + "%");
        bar.setAttribute("role", "img");
        bar.setAttribute("aria-label",
          model.label + ", " + domain.label + ", " + fmt(value));
        bar.dataset.value = fmt(value);
        bar.dataset.label = model.label + " · " + domain.label;
        bar.appendChild(el("span", "sv-bar__value", value.toFixed(2)));
        bars.appendChild(bar);
      });

      group.appendChild(bars);
      var name = el("span", "sv-group__label" + (domain.key === "ALL" ? " is-overall" : ""),
        domain.label);
      group.appendChild(name);
      area.appendChild(group);
    });

    TICKS.forEach(function (tick) {
      var line = el("div", "sv-gridline");
      line.style.bottom = (tick / Y_MAX * 100) + "%";
      area.appendChild(line);
    });
    plot.appendChild(area);
    explorer.appendChild(plot);

    var foot = el("div", "sv-chart__foot");
    var legend = el("div", "sv-chart__legend");
    data.models.forEach(function (model, index) {
      var item = el("span");
      var mark = vendorMark(model.vendor, SERIES[index]);
      if (mark) item.appendChild(mark);
      item.appendChild(document.createTextNode(model.label + " · " + model.harness));
      legend.appendChild(item);
    });
    foot.appendChild(legend);
    var readout = el("p", "sv-chart__readout", hint("bar"));
    readout.setAttribute("data-readout", "");
    foot.appendChild(readout);
    explorer.appendChild(foot);

    area.addEventListener("mouseover", function (event) {
      var bar = event.target.closest(".sv-bar:not(.sv-bar--none)");
      if (!bar) return;
      area.classList.add("is-dim");
      Array.prototype.forEach.call(area.querySelectorAll(".sv-bar"), function (other) {
        other.classList.toggle("is-on", other === bar);
      });
      readout.textContent = bar.dataset.label + " · " + bar.dataset.value;
    });

    area.addEventListener("mouseleave", function () {
      area.classList.remove("is-dim");
      Array.prototype.forEach.call(area.querySelectorAll(".sv-bar"), function (other) {
        other.classList.remove("is-on");
      });
      readout.textContent = hint("bar");
    });
  }

  /* ---------- related-work comparison ---------- */

  var MARK_GLYPH = { yes: "✓", no: "×", na: "—" };
  var MARK_WORD = {
    yes: "reported", no: "not reported", partial: "partial", na: "not applicable"
  };

  function renderComparison() {
    var host = document.querySelector("[data-comparison]");
    if (!host || !data.comparison) return;
    var source = data.comparison;

    var table = el("table", "sv-compare");
    var head = el("thead");
    var headRow = el("tr");
    var corner = el("th", null, "Benchmark");
    corner.setAttribute("scope", "col");
    headRow.appendChild(corner);
    source.columns.forEach(function (name) {
      var th = el("th", null, name);
      th.setAttribute("scope", "col");
      headRow.appendChild(th);
    });
    head.appendChild(headRow);
    table.appendChild(head);

    var body = el("tbody");
    source.rows.forEach(function (row) {
      var tr = el("tr", row.ours ? "is-ours" : null);
      var th = el("th", null, row.name);
      th.setAttribute("scope", "row");
      tr.appendChild(th);

      row.marks.forEach(function (mark, index) {
        var td = el("td", mark);
        var visible = mark === "partial"
          ? el("span", "sv-partial", "partial")
          : el("span", null, MARK_GLYPH[mark]);
        visible.setAttribute("aria-hidden", "true");
        td.appendChild(visible);
        td.appendChild(el("span", "sv-sr",
          MARK_WORD[mark] + ": " + source.columns[index]));
        tr.appendChild(td);
      });
      body.appendChild(tr);
    });
    table.appendChild(body);

    // The table scrolls inside its own box on narrow screens; the caption stays outside it
    // so it wraps to the column instead of travelling with the table.
    var figure = el("figure", "sv-compare-figure");
    var scroller = el("div", "sv-scroll");
    scroller.appendChild(table);
    figure.appendChild(scroller);
    figure.appendChild(el("figcaption", "sv-compare__caption",
      "Comparison of benchmark objectives and settings reported in the cited papers."));
    host.appendChild(figure);
  }

  /* ---------- sub-domain coverage ---------- */

  var SEGMENTS = 5;

  function segmentColour(index) {
    return "var(--sv-seg-" + ((index % SEGMENTS) + 1) + ")";
  }

  function renderCoverage() {
    var host = document.querySelector("[data-coverage]");
    if (!host) return;

    data.domains.forEach(function (domain) {
      var items = data.subdomains
        .filter(function (s) { return s.domain === domain.key; })
        .sort(function (a, b) { return b.n - a.n; });
      var total = items.reduce(function (sum, s) { return sum + s.n; }, 0);

      var row = el("div", "sv-compose__row");

      var head = el("div", "sv-compose__head");
      head.appendChild(el("span", "sv-compose__name", domain.label));
      head.appendChild(el("span", "sv-compose__total", total + " questions"));
      row.appendChild(head);

      var bar = el("div", "sv-compose__bar");
      var keys = el("div", "sv-compose__keys");

      items.forEach(function (s, index) {
        var label = humanise(s.name, s.domain);

        var seg = el("div", "sv-compose__seg");
        seg.style.width = (s.n / total * 100) + "%";
        seg.style.background = segmentColour(index);
        seg.title = label + " · " + s.n;
        bar.appendChild(seg);

        var key = el("span", "sv-compose__key");
        var chip = el("i");
        chip.style.background = segmentColour(index);
        key.appendChild(chip);
        key.appendChild(document.createTextNode(label + " "));
        key.appendChild(el("b", null, String(s.n)));
        key.title = domain.label + " · " + s.name;
        keys.appendChild(key);
      });

      row.appendChild(bar);
      row.appendChild(keys);
      host.appendChild(row);
    });
  }

  /* ---------- model comparison ---------- */

  // The six-view axis covers half the range: it is a different metric, so the three charts
  // share a shape, not a scale.
  var LB_AXIS = {
    "cc-3d": { max: 0.6, ticks: [0, 0.1, 0.2, 0.3, 0.4, 0.5] },
    "cc-mcp": { max: 0.6, ticks: [0, 0.1, 0.2, 0.3, 0.4, 0.5] },
    "cc-2d-6": { max: 0.325, ticks: [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3] }
  };
  function fmt4(value) { return value.toFixed(4); }

  // Keyed on the data attribute rather than a class, so the matrix cells can carry the same
  // hover behaviour without inheriting the .sv-bar box that the column charts need.
  function lbReadout(area, readout) {
    var hot = "[data-value]";
    area.addEventListener("mouseover", function (event) {
      var bar = event.target.closest(hot);
      if (!bar || !area.contains(bar)) return;
      area.classList.add("is-dim");
      Array.prototype.forEach.call(area.querySelectorAll(hot), function (other) {
        other.classList.toggle("is-on", other === bar);
      });
      readout.textContent = bar.dataset.label + " · " + bar.dataset.value;
    });
    area.addEventListener("mouseleave", function () {
      area.classList.remove("is-dim");
      Array.prototype.forEach.call(area.querySelectorAll(hot), function (other) {
        other.classList.remove("is-on");
      });
      readout.textContent = hint("bar");
    });
  }

  // One chart per axis, not per setting: the two 3D settings share a metric and a scale, so
  // pairing them answers "does the tool interface help" directly. The six-view column is a
  // different metric and stays on its own.
  var LB_CHARTS = [
    { keys: ["cc-3d", "cc-mcp"], axis: "cc-3d" },
    // The six-view chart carries one bar per model against a shorter axis, so it does not
    // need the column the paired chart does.
    { keys: ["cc-2d-6"], axis: "cc-2d-6", narrow: true }
  ];

  function lbChart(lb, spec) {
    var settings = spec.keys.map(function (key) {
      var match = lb.settings.filter(function (s) { return s.key === key; })[0];
      if (!match) throw new Error("unknown setting " + key);
      return match;
    });
    var scale = LB_AXIS[spec.axis];
    if (!scale) throw new Error("no axis for " + spec.axis);

    // A model needs every setting in the chart; the six-view column is missing two of them.
    var rows = lb.models.filter(function (model) {
      return settings.every(function (s) { return model.settings[s.key]; });
    }).sort(function (a, b) {
      return b.settings[settings[0].key].mean - a.settings[settings[0].key].mean;
    });

    var chart = el("div", "sv-chart sv-lb__chart" + (spec.narrow ? " sv-lb__chart--narrow" : ""));

    var head = el("div", "sv-chart__head");
    var titles = el("div");
    var names = settings.map(function (s) { return settingName(s.key); });
    var title = names.length > 1
      ? names[0] + " vs " + settings.slice(1).map(function (s) { return settingShort(s.key); }).join(" vs ")
      : names[0];
    titles.appendChild(el("h3", null, title + " · " + settings[0].metric));
    titles.appendChild(el("p", null, settings.map(function (s) {
      return settingShort(s.key) + ". " + s.note;
    }).join(" ")));
    head.appendChild(titles);
    chart.appendChild(head);

    var plot = el("div", "sv-plot");
    var axis = el("div", "sv-plot__axis");
    scale.ticks.forEach(function (tick) {
      var label = el("span", null, tick.toFixed(2));
      label.style.bottom = (tick / scale.max * 100) + "%";
      axis.appendChild(label);
    });
    plot.appendChild(axis);

    var area = el("div", "sv-plot__area");
    rows.forEach(function (model) {
      var group = el("div", "sv-group");
      var bars = el("div", "sv-group__bars");

      settings.forEach(function (setting, index) {
        var cell = model.settings[setting.key];
        var bar = el("div", "sv-bar sv-bar--" + model.vendor + (index ? " is-alt" : ""));
        bar.style.setProperty("--h", (cell.mean / scale.max * 100) + "%");
        bar.setAttribute("role", "img");
        bar.setAttribute("aria-label",
          model.label + ", " + settingName(setting.key) + ", " + fmt4(cell.mean));
        bar.dataset.value = fmt4(cell.mean);
        bar.dataset.label = model.label + " · " + settingName(setting.key);
        bar.appendChild(el("span", "sv-bar__value", cell.mean.toFixed(2)));
        bars.appendChild(bar);
      });
      group.appendChild(bars);

      var name = el("span", "sv-lb__label");
      var mark = vendorMark(model.vendor, "sv-mark sv-mark--" + model.vendor);
      if (mark) name.appendChild(mark);
      name.appendChild(el("span", null, model.label));
      group.appendChild(name);
      area.appendChild(group);
    });

    scale.ticks.forEach(function (tick) {
      var line = el("div", "sv-gridline");
      line.style.bottom = (tick / scale.max * 100) + "%";
      area.appendChild(line);
    });
    plot.appendChild(area);
    chart.appendChild(plot);

    var foot = el("div", "sv-chart__foot");
    var legend = el("div", "sv-chart__legend");
    if (settings.length > 1) {
      // Only the pairing needs a key: the vendor mark under each name already carries the
      // colour, so a nine-entry vendor legend would repeat what the row labels say.
      settings.forEach(function (setting, index) {
        var item = el("span");
        item.appendChild(el("i", "sv-lb__swatch" + (index ? " is-alt" : "")));
        item.appendChild(document.createTextNode(settingName(setting.key)));
        legend.appendChild(item);
      });
    }
    foot.appendChild(legend);
    var readout = el("p", "sv-chart__readout", hint("bar"));
    foot.appendChild(readout);
    chart.appendChild(foot);

    lbReadout(area, readout);
    return chart;
  }

  /* One row per model, one column per discipline, each column on its own scale. A column
     asks "which model is ahead in this discipline"; it does not compare disciplines, whose
     questions are not on a common axis. Drawn from the same arms as the charts above. */
  function lbDomainMatrix(lb, domains) {
    var setting = lb.settings.filter(function (s) { return s.key === "cc-3d"; })[0];
    if (!setting) throw new Error("no cc-3d setting for the per-domain matrix");

    var rows = lb.models.filter(function (model) {
      return model.settings["cc-3d"] && model.settings["cc-3d"].byDomain;
    });
    var maxima = domains.map(function (domain) {
      return rows.reduce(function (best, model) {
        return Math.max(best, model.settings["cc-3d"].byDomain[domain.key]);
      }, 0);
    });

    var chart = el("div", "sv-chart sv-lb__chart sv-lb__matrix");

    var head = el("div", "sv-chart__head");
    var titles = el("div");
    titles.appendChild(el("h3", null, "Per-domain " + setting.metric + " · " + settingName(setting.key)));
    titles.appendChild(el("p", null,
      "The eight architecture replacements lift Architecture into Mechanical CAD's tier; " +
      "the five medical replacements lift Medical imaging off the floor. Each column carries " +
      "its own scale, whose maximum sits under the discipline name, so bar length compares " +
      "models within a discipline and not disciplines with each other."));
    head.appendChild(titles);
    chart.appendChild(head);

    // Five columns cannot share a phone's width, so the grid scrolls in its own box with
    // the model names pinned.
    var matrix = el("div", "sv-matrix sv-scroll");
    var grid = el("div", "sv-matrix__grid");
    matrix.appendChild(grid);

    var headRow = el("div", "sv-matrix__head");
    headRow.appendChild(el("span", null, "Model"));
    domains.forEach(function (domain, index) {
      var cell = el("span", null, domain.label);
      cell.appendChild(el("em", null, "max " + maxima[index].toFixed(3)));
      headRow.appendChild(cell);
    });
    grid.appendChild(headRow);

    rows.forEach(function (model) {
      var row = el("div", "sv-matrix__row");

      var name = el("div", "sv-matrix__name");
      var mark = vendorMark(model.vendor, "sv-mark sv-mark--" + model.vendor);
      if (mark) name.appendChild(mark);
      name.appendChild(el("span", null, model.label));
      row.appendChild(name);

      domains.forEach(function (domain, index) {
        var value = model.settings["cc-3d"].byDomain[domain.key];
        var cell = el("div", "sv-matrix__cell");
        cell.dataset.label = model.label + " · " + domain.label;
        cell.dataset.value = fmt4(value);
        cell.setAttribute("role", "img");
        cell.setAttribute("aria-label", cell.dataset.label + ", " + cell.dataset.value);

        var track = el("div", "sv-matrix__track");
        // The vendor modifier sits on the fill, not the cell: some of them paint a
        // background as well as declaring the colour, which would flood the whole grid cell.
        var fill = el("div", "sv-matrix__fill sv-bar--" + model.vendor);
        fill.style.width = (value / maxima[index] * 100) + "%";
        track.appendChild(fill);
        cell.appendChild(track);
        cell.appendChild(el("span", "sv-matrix__val", value.toFixed(3)));
        row.appendChild(cell);
      });
      grid.appendChild(row);
    });
    chart.appendChild(matrix);

    var foot = el("div", "sv-chart__foot");
    foot.appendChild(el("div", "sv-chart__legend"));
    var readout = el("p", "sv-chart__readout", hint("cell"));
    foot.appendChild(readout);
    chart.appendChild(foot);
    lbReadout(chart, readout);

    return chart;
  }

  function renderLeaderboard() {
    var host = document.querySelector("[data-leaderboard]");
    if (!host || !data.leaderboard) return;
    var lb = data.leaderboard;

    LB_CHARTS.forEach(function (spec) { host.appendChild(lbChart(lb, spec)); });
    host.appendChild(lbDomainMatrix(lb, data.domains));
  }

  renderExplorer();
  renderLeaderboard();
  renderComparison();
  renderCoverage();
})();
