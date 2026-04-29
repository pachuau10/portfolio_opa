/* Scroll reveal, parallax, tilt, skill bar fill */
(function () {
  'use strict';

  // Intersection observer for reveal-on-scroll + skill bars
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
        // animate any skill bars inside
        entry.target.querySelectorAll && entry.target.querySelectorAll('.skill-bar').forEach(function (b) { b.classList.add('in-view'); });
      }
    });
  }, { threshold: 0.12 });

  document.querySelectorAll('.reveal-on-scroll, .skill-bar').forEach(function (el) { io.observe(el); });

  // Subtle parallax for hero collage
  var collage = document.querySelector('[data-parallax]');
  if (collage && window.matchMedia('(min-width: 901px)').matches) {
    window.addEventListener('scroll', function () {
      var y = Math.min(window.scrollY, 600);
      collage.style.transform = 'translateY(' + (y * 0.12) + 'px)';
    }, { passive: true });
  }

  // Tilt effect on hover for cards & collage items
  document.querySelectorAll('[data-tilt]').forEach(function (el) {
    el.addEventListener('mousemove', function (e) {
      var r = el.getBoundingClientRect();
      var px = (e.clientX - r.left) / r.width - 0.5;
      var py = (e.clientY - r.top) / r.height - 0.5;
      el.style.transform = 'perspective(900px) rotateX(' + (-py * 6) + 'deg) rotateY(' + (px * 8) + 'deg) translateY(-6px)';
    });
    el.addEventListener('mouseleave', function () {
      el.style.transform = '';
    });
  });
})();
