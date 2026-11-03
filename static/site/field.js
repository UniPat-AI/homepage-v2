/* UniPat particle field — one canvas shared by every page.
   Each [data-scene] element names the shape the particles assemble into while it is
   centred on screen, plus where the shape sits:
     data-shape  mark | sphere | plane | ring | bars | helix | gate | dust | image
     data-src    image URL when data-shape="image" (falls back to the mark)
     data-tint   optional particle colour for an image (otherwise sampled colours)
     data-detail "fine" preserves small points in a point-cloud reference image
     data-fx/fy  centre as a fraction of the viewport (desktop; mobile is centred)
     data-fs     scale        data-fa  opacity
   Particle positions are handed to the next page through sessionStorage, so the
   field flows from one page's shape into the next instead of starting over. */
(function () {
    var cv = document.getElementById('field');
    if (!cv) return;
    var ctx = cv.getContext('2d');
    var MARK = new Path2D(cv.dataset.mark), VB = 425.2;
    var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
    var dpr = Math.min(devicePixelRatio || 1, 2), W, H, N, P = [], T = [], META = [], mouse = { x: -1e4, y: -1e4 };
    var PAL = ['#dde3f1', '#dde3f1', '#a3b2d8', '#a3b2d8', '#c2b7ee', '#ecd9a6', '#9fd6b8'];
    var KEY = 'unipat:field';
    var cover = document.querySelector('[data-field-cover]');

    function rnd(seed) { var s = seed; return function () { s = (s * 16807) % 2147483647; return (s - 1) / 2147483646; }; }

    // ---- shapes, in a unit space roughly [-1, 1] ----
    var markPts = null;
    function sampleMark(n) {
        if (!markPts) {
            var S = 300, off = document.createElement('canvas'); off.width = off.height = S;
            var o = off.getContext('2d', { willReadFrequently: true }), sc = S / VB;
            o.setTransform(sc, 0, 0, sc, 0, 0); o.fillStyle = '#fff'; o.fill(MARK);
            var d = o.getImageData(0, 0, S, S).data; markPts = [];
            for (var y = 0; y < S; y += 2) for (var x = 0; x < S; x += 2) if (d[(y * S + x) * 4 + 3] > 128) markPts.push([x / S * 2 - 1, y / S * 2 - 1]);
        }
        var out = [];
        for (var i = 0; i < n; i++) { var p = markPts[(Math.random() * markPts.length) | 0]; out.push({ x: p[0] + (Math.random() - .5) * .01, y: p[1] + (Math.random() - .5) * .01, z: (Math.random() - .5) * .08 }); }
        return out;
    }
    function sphere(n) {
        var out = [], g = Math.PI * (3 - Math.sqrt(5));
        for (var i = 0; i < n; i++) { var y = 1 - i / (n - 1) * 2, r = Math.sqrt(1 - y * y), th = g * i; out.push({ x: Math.cos(th) * r * .92, y: y * .92, z: Math.sin(th) * r * .92 }); }
        return out;
    }
    function plane(n) {
        var cols = Math.ceil(Math.sqrt(n * 1.6)), rows = Math.ceil(n / cols), out = [];
        for (var i = 0; i < n; i++) { var c = i % cols, r = (i / cols) | 0; out.push({ x: c / (cols - 1) * 2.2 - 1.1, y: 0, z: r / (rows - 1) * 2 - 1 }); }
        return out;
    }
    function ring(n) {
        var k = Math.floor(n * .62), a = sampleMark(k);
        a.forEach(function (p) { p.x *= .62; p.y *= .62; });
        for (var i = k; i < n; i++) { var th = Math.random() * 6.283, rr = .95 + (Math.random() - .5) * .06; a.push({ x: Math.cos(th) * rr, y: Math.sin(th) * rr * .34, z: Math.sin(th) * .4 }); }
        return a;
    }
    // a leaderboard: one column per benchmark, rising from a shared floor
    function bars(n) {
        var hs = [.95, 1.35, .7, 1.6, 1.15, .82, 1.45, 1.05], B = hs.length, out = [], R = rnd(7);
        var floor = n * .12 | 0;
        for (var i = 0; i < n - floor; i++) {
            var b = i % B, h = hs[b], x0 = (b / (B - 1)) * 1.9 - .95;
            var face = R();
            var u = (R() - .5) * .15, v = (R() - .5) * .15;
            // hug the column's edges so it reads as a solid prism
            if (face < .5) u = (u > 0 ? .075 : -.075); else v = (v > 0 ? .075 : -.075);
            out.push({ x: x0 + u, y: .8 - R() * h, z: v });
        }
        for (var j = 0; j < floor; j++) out.push({ x: (R() - .5) * 2.2, y: .8, z: (R() - .5) * .7 });
        return out;
    }
    // shared knowledge: a double helix with rungs
    function helix(n) {
        var out = [], R = rnd(11), rungs = n * .18 | 0;
        for (var i = 0; i < n - rungs; i++) {
            var t = R(), th = t * Math.PI * 5, s = i % 2 ? Math.PI : 0;
            out.push({ x: Math.cos(th + s) * .42 + (R() - .5) * .03, y: t * 2 - 1, z: Math.sin(th + s) * .42 });
        }
        for (var j = 0; j < rungs; j++) {
            var k = ((R() * 24) | 0) / 24, a = k * Math.PI * 5, m = R() * 2 - 1;
            out.push({ x: Math.cos(a) * .42 * m, y: k * 2 - 1, z: Math.sin(a) * .42 * m });
        }
        return out;
    }
    // off-the-shelf data: two facing dot-matrix panels with lit inner edges, rays fanning outward
    function gate(n) {
        var out = [], R = rnd(23), edge = n * .18 | 0, panel = n * .5 | 0;
        var RAYS = [[-.3, -.56], [-.2, -.4], [-.08, -.2], [.08, .2], [.2, .4], [.3, .56]];
        for (var i = 0; i < n; i++) {
            var s = i % 2 ? 1 : -1, x, y, z, c;
            if (i < edge) {
                // the bright hinge: a tight column of dots on each inner edge
                x = .06 + R() * .012; y = Math.round((R() * 2 - 1) * 30) / 30 * .34; z = 0; c = R() < .1 ? '#ecd9a6' : '#f6f7fb';
            } else if (i < edge + panel) {
                // the panel recedes from the hinge: thinner and shorter toward its far edge
                var u = Math.round(Math.pow(R(), 1.6) * 22) / 22, h = .34 - u * .1;
                x = .08 + u * .5; y = Math.round((R() * 2 - 1) * 26) / 26 * h; z = u * .25; c = R() < .6 ? '#dde3f1' : '#a3b2d8';
            } else {
                var ray = RAYS[(R() * RAYS.length) | 0], t = Math.pow(R(), .8);
                x = .14 + t * .74 + (R() - .5) * .03; y = ray[0] + (ray[1] - ray[0]) * t + (R() - .5) * .03 * (1 + t); z = t * .2; c = R() < .05 ? '#ecd9a6' : '#a9aec0';
            }
            out.push({ x: s * x, y: y, z: z + (R() - .5) * .02, c: c });
        }
        return out;
    }
    function dust(n) {
        var out = [];
        for (var i = 0; i < n; i++) out.push({ x: (Math.random() - .5) * 3.2, y: (Math.random() - .5) * 2, z: (Math.random() - .5) * 1.5 });
        return out;
    }
    var FLAGS = { mark: { sway: 1 }, ring: { sway: 1 }, gate: { sway: .7 }, image: { sway: .4 }, sphere: { spin: 1 }, bars: { swing: 1, yaw: -.42, tilt: .3 }, helix: { spin: 1 }, plane: { spin: 1, wave: 1 }, dust: { drift: 1 } };
    var MAKE = { mark: sampleMark, sphere: sphere, plane: plane, ring: ring, bars: bars, helix: helix, gate: gate, dust: dust, image: sampleMark };

    // a cover image re-drawn in particles: keep pixels that stand out from the background
    function sampleImage(src, n, done, tint, detail) {
        var img = new Image(); img.crossOrigin = 'anonymous'; img.decoding = 'async';
        img.onload = function () {
            try {
                var S = detail === 'fine' ? 480 : 180, ar = img.naturalWidth / img.naturalHeight, w = ar >= 1 ? S : Math.round(S * ar), h = ar >= 1 ? Math.round(S / ar) : S;
                var off = document.createElement('canvas'); off.width = w; off.height = h;
                var o = off.getContext('2d', { willReadFrequently: true }); o.drawImage(img, 0, 0, w, h);
                var d = o.getImageData(0, 0, w, h).data;
                function px(x, y) { var i = (y * w + x) * 4; return [d[i], d[i + 1], d[i + 2], d[i + 3]]; }
                var cs = [px(1, 1), px(w - 2, 1), px(1, h - 2), px(w - 2, h - 2)], bg = [0, 1, 2].map(function (c) { return (cs[0][c] + cs[1][c] + cs[2][c] + cs[3][c]) / 4; });
                var pts = [], sc = 2 / Math.max(w, h);
                for (var y = 0; y < h; y++) for (var x = 0; x < w; x++) {
                    var p = px(x, y); if (p[3] < 128) continue;
                    var dist = Math.abs(p[0] - bg[0]) + Math.abs(p[1] - bg[1]) + Math.abs(p[2] - bg[2]);
                    if (dist < 70) continue;
                    // lift dark pixels toward the mist tone so they read on the night background
                    var l = (p[0] * .3 + p[1] * .59 + p[2] * .11) / 255, m = Math.max(.25, .7 - l);
                    pts.push({ x: (x - w / 2) * sc, y: (y - h / 2) * sc, c: 'rgb(' + [0, 1, 2].map(function (c) { return Math.round(p[c] * (1 - m) + [221, 227, 241][c] * m); }) + ')' });
                }
                if (pts.length < 400) return;
                var out = [];
                for (var i = 0; i < n; i++) { var q = pts[(Math.random() * pts.length) | 0]; out.push({ x: q.x * .95 + (Math.random() - .5) * .012, y: q.y * .95 + (Math.random() - .5) * .012, z: (Math.random() - .5) * .06, c: tint || q.c }); }
                done(out);
            } catch (e) { /* cross-origin image without CORS: keep the mark */ }
        };
        img.src = src;
    }

    var sections = Array.prototype.slice.call(document.querySelectorAll('[data-scene]'));
    var scenes = sections.map(function (s) {
        var d = s.dataset;
        return { shape: d.shape || 'mark', src: d.src, tint: d.tint, detail: d.detail, fx: +(d.fx || .7), fy: +(d.fy || .5), fs: +(d.fs || 1), fa: d.fa === undefined ? 1 : +d.fa };
    });
    if (!scenes.length) scenes = [{ shape: 'mark', fx: .5, fy: .5, fs: 1, fa: 1 }];

    function restore() {
        try {
            var s = JSON.parse(sessionStorage.getItem(KEY) || 'null');
            sessionStorage.removeItem(KEY);
            if (!s || Date.now() - s.t > 8000 || s.p.length !== N * 2) return false;
            var fx = W / s.w, fy = H / s.h;
            for (var i = 0; i < N; i++) { P[i].x = s.p[i * 2] * fx; P[i].y = s.p[i * 2 + 1] * fy; }
            return true;
        } catch (e) { return false; }
    }
    function save() {
        try {
            var arr = new Array(N * 2);
            for (var i = 0; i < N; i++) { arr[i * 2] = Math.round(P[i].x); arr[i * 2 + 1] = Math.round(P[i].y); }
            sessionStorage.setItem(KEY, JSON.stringify({ t: Date.now(), w: W, h: H, p: arr }));
        } catch (e) {}
    }

    var restored = false;
    function build() {
        W = innerWidth; H = innerHeight;
        cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        var nN = W < 700 ? 1300 : 2200;
        if (nN === N) return;
        N = nN; P = [];
        for (var i = 0; i < N; i++) P.push({ x: Math.random() * W, y: Math.random() * H, vx: 0, vy: 0, c: PAL[(Math.random() * PAL.length) | 0], s: Math.random() < .12 ? 2.2 : 1.3, seed: Math.random() });
        T = scenes.map(function (sc) { return MAKE[sc.shape] ? MAKE[sc.shape](N) : sampleMark(N); });
        META = scenes.map(function (sc) { return FLAGS[sc.shape] || FLAGS.mark; });
        scenes.forEach(function (sc, idx) {
            if (sc.shape === 'image' && sc.src) sampleImage(sc.src, N, function (pts) { if (pts.length !== N) return; T[idx] = pts; if (reduce) settle(); }, sc.tint, sc.detail);
        });
        restored = restore() || restored;
    }

    var dots = Array.prototype.slice.call(document.querySelectorAll('.scenes a'));
    function sceneProgress() {
        if (sections.length < 2) return 0;
        var mid = innerHeight / 2, centers = sections.map(function (s) { var r = s.getBoundingClientRect(); return r.top + r.height / 2; });
        if (mid <= centers[0]) return 0;
        for (var i = 0; i < centers.length - 1; i++) if (mid < centers[i + 1]) return i + (mid - centers[i]) / (centers[i + 1] - centers[i]);
        return centers.length - 1;
    }
    function ease(k) { return k < .5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2; }
    function mix(a, b, k) { return a + (b - a) * k; }

    var t0 = performance.now(), rotY = 0, tilt = { x: 0, y: 0 }, running = true;
    function frame(now) {
        if (running && !reduce) requestAnimationFrame(frame);
        if (document.hidden) return;
        // the reading surface fully covers the field: skip drawing
        if (cover && cover.getBoundingClientRect().top <= 0) { cv.style.visibility = 'hidden'; return; }
        cv.style.visibility = '';
        var t = (now - t0) / 1000;
        var sp = sceneProgress(), a = Math.floor(sp), b = Math.min(T.length - 1, a + 1), k = ease(sp - a);
        dots.forEach(function (d, i) { d.classList.toggle('on', Math.round(sp) === i); });
        var A0 = scenes[a], B0 = scenes[b], MA = META[a], MB = META[b];

        ctx.globalCompositeOperation = 'source-over';
        ctx.fillStyle = 'rgba(10,11,16,.32)'; ctx.fillRect(0, 0, W, H);
        ctx.globalCompositeOperation = 'lighter';

        var mobile = W < 900;
        // on phones the copy sits at the bottom of each scene, so the shape moves into the space above it
        var cx = mobile ? W * .5 : W * mix(A0.fx, B0.fx, k), cy = H * Math.min(mix(A0.fy, B0.fy, k), mobile ? .24 : 1);
        var S = Math.min(mobile ? W * .32 : W * .24, H * (mobile ? .2 : .36)) * mix(A0.fs, B0.fs, k), alpha = mix(A0.fa, B0.fa, k);
        rotY += reduce ? 0 : .0035;
        tilt.x += ((mouse.y > -1e3 ? (mouse.y / H - .5) : 0) * .5 - tilt.x) * .04;
        tilt.y += ((mouse.x > -1e3 ? (mouse.x / W - .5) : 0) * .7 - tilt.y) * .04;

        var spinW = (MA.spin || 0) * (1 - k) + (MB.spin || 0) * k, swayW = (MA.sway || 0) * (1 - k) + (MB.sway || 0) * k;
        var waveW = (MA.wave || 0) * (1 - k) + (MB.wave || 0) * k, driftW = (MA.drift || 0) * (1 - k) + (MB.drift || 0) * k;
        var swingW = (MA.swing || 0) * (1 - k) + (MB.swing || 0) * k, yaw = (MA.yaw || 0) * (1 - k) + (MB.yaw || 0) * k;
        var ry = tilt.y + rotY * spinW + Math.sin(t * .3) * (.12 * swayW + .38 * swingW) + yaw;
        var rx = tilt.x + .55 * waveW + ((MA.tilt || 0) * (1 - k) + (MB.tilt || 0) * k);
        var cyr = Math.cos(ry), syr = Math.sin(ry), cxr = Math.cos(rx), sxr = Math.sin(rx);

        for (var i = 0; i < N; i++) {
            var p = P[i], A = T[a][i], B = T[b][i];
            var tx = A.x + (B.x - A.x) * k, ty = A.y + (B.y - A.y) * k, tz = A.z + (B.z - A.z) * k;
            if (waveW) ty += waveW * (.22 * Math.sin(tx * 3.2 + t * 1.2) * Math.cos(tz * 2.4 - t * .8) + .08);
            if (driftW) { tx += driftW * Math.sin(t * .2 + p.seed * 40) * .12; ty += driftW * Math.cos(t * .17 + p.seed * 30) * .1; }
            var x1 = tx * cyr + tz * syr, z1 = -tx * syr + tz * cyr;
            var y1 = ty * cxr - z1 * sxr, z2 = ty * sxr + z1 * cxr;
            var persp = 2.6 / (2.6 + z2), gx = cx + x1 * S * persp, gy = cy + y1 * S * persp;

            p.vx += (gx - p.x) * .055; p.vy += (gy - p.y) * .055;
            var dx = p.x - mouse.x, dy = p.y - mouse.y, d2 = dx * dx + dy * dy;
            if (d2 < 14400) { var f = (1 - Math.sqrt(d2) / 120) * 2.2; p.vx += dx * f * .04; p.vy += dy * f * .04; }
            p.vx *= .78; p.vy *= .78; p.x += p.vx; p.y += p.vy;

            var depth = Math.max(.25, Math.min(1, persp - .35));
            ctx.globalAlpha = alpha * depth * (.55 + .45 * Math.sin(t * 2 + p.seed * 20));
            ctx.fillStyle = (k < .5 ? A.c : B.c) || p.c;
            ctx.fillRect(p.x, p.y, p.s * persp, p.s * persp);
        }
        ctx.globalAlpha = 1;
    }

    addEventListener('pointermove', function (e) { mouse.x = e.clientX; mouse.y = e.clientY; }, { passive: true });
    document.addEventListener('pointerleave', function () { mouse.x = mouse.y = -1e4; });
    var rt; addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(build, 150); });
    addEventListener('pagehide', save);
    addEventListener('pageshow', function (e) { if (e.persisted && reduce) frame(performance.now()); });
    if (reduce) addEventListener('scroll', function () { requestAnimationFrame(frame); }, { passive: true });

    // with reduced motion there is no animation loop: settle into the shape in one go
    function settle() { for (var w = 0; w < 120; w++) frame(performance.now()); }
    build();
    if (reduce) settle();
    else requestAnimationFrame(frame);
    if (restored) document.documentElement.classList.add('field-continued');
})();
