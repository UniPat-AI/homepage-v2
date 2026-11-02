/* Pause the glass layers outside the viewport and when the tab is hidden. */
(function () {
    var visuals = document.querySelectorAll('[data-ots-optic]');
    var visible = new Set();
    function update() {
        visuals.forEach(function (el) {
            el.classList.toggle('is-moving', visible.has(el) && !document.hidden);
        });
    }
    var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) visible.add(entry.target);
            else visible.delete(entry.target);
        });
        update();
    });
    visuals.forEach(function (el) { observer.observe(el); });
    document.addEventListener('visibilitychange', update);
})();
