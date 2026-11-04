/* Article navigation only. The retired benchmark and public trace UI are absent. */
(function () {
  'use strict';
  const root = document.querySelector('.sle-blog');
  const toc = root?.querySelector('.sle-toc');
  if (!toc) return;
  const links = [...toc.querySelectorAll('a[href^="#"]')];
  const targets = links.map(link => document.getElementById(link.hash.slice(1))).filter(Boolean);
  const article = root.querySelector('.sle-story');
  const progress = toc.querySelector('progress');
  let scheduled = false;
  function update() {
    scheduled = false;
    let active = targets[0];
    const readingLine = Math.max(160, innerHeight * 0.25);
    targets.forEach(section => { if (section.getBoundingClientRect().top <= readingLine) active = section; });
    links.forEach(link => {
      if (active && link.hash === '#' + active.id) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
    if (article && progress) {
      const rect = article.getBoundingClientRect();
      progress.value = Math.round(Math.max(0, Math.min(100, -rect.top / Math.max(1, rect.height - innerHeight) * 100)));
    }
  }
  const schedule = () => {
    if (!scheduled) { scheduled = true; requestAnimationFrame(update); }
  };
  window.addEventListener('scroll', schedule, {passive: true});
  window.addEventListener('resize', schedule, {passive: true});
  update();
})();
