/* Main interactions: cursor, header, mobile nav, loader */
(function () {
  'use strict';

  // Loader
  window.addEventListener('load', function () {
    setTimeout(function () {
      var loader = document.getElementById('loader');
      if (loader) loader.classList.add('hidden');
      document.body.classList.add('loaded');
    }, 1600);
  });

  // Custom cursor (desktop only)
  if (window.matchMedia('(min-width: 901px)').matches) {
    var cursor = document.getElementById('cursor');
    var dot = document.getElementById('cursorDot');
    var x = 0, y = 0, tx = 0, ty = 0;

    document.addEventListener('mousemove', function (e) { tx = e.clientX; ty = e.clientY; if (dot) { dot.style.left = tx + 'px'; dot.style.top = ty + 'px'; } });

    function loop() {
      x += (tx - x) * 0.18;
      y += (ty - y) * 0.18;
      if (cursor) { cursor.style.left = x + 'px'; cursor.style.top = y + 'px'; }
      requestAnimationFrame(loop);
    }
    loop();

    document.querySelectorAll('a, button, .gallery-card, .collage-item, .about-img-frame, .about-img-card, input, textarea').forEach(function (el) {
      el.addEventListener('mouseenter', function () { cursor && cursor.classList.add('is-hover'); });
      el.addEventListener('mouseleave', function () { cursor && cursor.classList.remove('is-hover'); });
    });
  }

  // Header scroll state
  var header = document.getElementById('siteHeader');
  function onScroll() {
    if (!header) return;
    if (window.scrollY > 60) header.classList.add('scrolled');
    else header.classList.remove('scrolled');
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mobile nav — toggles the <nav id="siteNav"> overlay
  var toggle = document.getElementById('navToggle');
  var nav = document.getElementById('siteNav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      toggle.classList.toggle('open');
      nav.classList.toggle('open');
    });
    nav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        toggle.classList.remove('open');
        nav.classList.remove('open');
      });
    });
  }
})();