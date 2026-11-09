// Agentic QA Technologies — nav, theme, reveal, waitlist form. No dependencies.
(function () {
  var root = document.documentElement;
  root.classList.add('js');

  // Theme toggle (saved choice wins; otherwise follow OS)
  var tbtn = document.querySelector('.theme-toggle');
  function current() {
    var t = root.getAttribute('data-theme');
    if (t) return t;
    return window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }
  if (tbtn) {
    tbtn.addEventListener('click', function () {
      var next = current() === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('theme', next); } catch (e) {}
      tbtn.setAttribute('aria-label', 'Switch to ' + (next === 'dark' ? 'light' : 'dark') + ' theme');
    });
  }

  // Mobile nav
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') { nav.classList.remove('open'); toggle.setAttribute('aria-expanded', 'false'); }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { nav.classList.remove('open'); toggle.setAttribute('aria-expanded', 'false'); }
    });
  }

  var hdr = document.querySelector('.site-header');
  if (hdr) { var onS = function () { hdr.classList.toggle('scrolled', window.scrollY > 8); }; onS(); addEventListener('scroll', onS, { passive: true }); }

  // Nav scroll-spy: aria-current on section in view
  (function () {
    var nav = document.querySelector('.site-nav');
    if (!nav) return;
    var links = Array.prototype.slice.call(nav.querySelectorAll('a[href^="#"]'));
    if (!links.length) return;
    var map = {};
    links.forEach(function (a) {
      var id = (a.getAttribute('href') || '').slice(1);
      var el = id && document.getElementById(id);
      if (el) map[id] = a;
    });
    var ids = Object.keys(map);
    if (!ids.length) return;
    function setCurrent(id) {
      links.forEach(function (a) { a.removeAttribute('aria-current'); });
      if (map[id]) map[id].setAttribute('aria-current', 'true');
    }
    if (!('IntersectionObserver' in window)) {
      setCurrent(ids[0]);
      return;
    }
    var ratios = {};
    ids.forEach(function (id) { ratios[id] = 0; });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        ratios[en.target.id] = en.isIntersecting ? en.intersectionRatio : 0;
      });
      var best = null, bestR = 0;
      ids.forEach(function (id) {
        if (ratios[id] > bestR) { bestR = ratios[id]; best = id; }
      });
      if (best) setCurrent(best);
    }, { rootMargin: '-40% 0px -45% 0px', threshold: [0, 0.1, 0.25, 0.5, 0.75, 1] });
    ids.forEach(function (id) { io.observe(document.getElementById(id)); });
  })();


  var year = document.getElementById('year');
  if (year) year.textContent = String(new Date().getFullYear());

  // On real agenticqa.io hosts, upgrade preview-friendly /?site= links to production subdomains.
  // On *.vercel.app / localhost, leave /?site= so preview review does not bounce to live production.
  (function () {
    var host = (location.hostname || '').toLowerCase();
    var isPreview = /\.vercel\.app$/.test(host) || host === 'localhost' || host === '127.0.0.1';
    if (isPreview) return;
    if (!/(^|\.)agenticqa\.io$/.test(host)) return;
    document.querySelectorAll('[data-prod-href]').forEach(function (a) {
      var prod = a.getAttribute('data-prod-href');
      if (prod) a.setAttribute('href', prod);
    });
  })();

  // Scroll reveal
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('visible'); io.unobserve(en.target); } });
    }, { threshold: 0.08 });
    els.forEach(function (el) { var k = el.parentElement ? Array.prototype.indexOf.call(el.parentElement.children, el) : 0; el.style.transitionDelay = (k % 4) * 80 + 'ms'; io.observe(el); });
  } else { els.forEach(function (el) { el.classList.add('visible'); }); }

  // Demo CTA: preselect interest in the form
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('[data-interest="demo"]');
    var sel = document.getElementById('f-interest');
    if (a && sel) { sel.value = 'Free demo class (30 min)'; var subj = document.querySelector('#waitlist-form [name=_subject], #enquiry-form [name=_subject], form.form[data-ajax] [name=_subject]'); if (subj) subj.value = 'Free demo class request'; }
  });
  if (location.hash === '#contact' && document.getElementById('f-interest')) document.getElementById('f-interest').value = 'Free demo class (30 min)';

  // Waitlist / contact form: AJAX to /api/contact (Titan SMTP), fall back to mailto
  var form = document.getElementById('waitlist-form') || document.getElementById('enquiry-form') || document.querySelector('form.form[data-ajax]');
  if (form) {
    var status = form.querySelector('.form-status');
    function mailtoFallback() {
      var d = new FormData(form);
      var body = 'Name: ' + (d.get('name') || '') + '\nEmail: ' + (d.get('email') || '') +
        '\nInterest: ' + (d.get('interest') || '') + '\nI am: ' + (d.get('profile') || '') + '\n\n' + (d.get('message') || '');
      window.location.href = 'mailto:admin@agenticqa.io?subject=' + encodeURIComponent(d.get('_subject') || 'Agentic QA enquiry') +
        '&body=' + encodeURIComponent(body);
    }
    form.addEventListener('submit', function (e) {
      if (!window.fetch) return; // native POST to /api/contact
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var btn = form.querySelector('button[type=submit]');
      btn.disabled = true; status.className = 'form-status'; status.textContent = 'Sending…';
      var fd = new FormData(form);
      var payload = {
        name: fd.get('name') || '',
        email: fd.get('email') || '',
        interest: fd.get('interest') || '',
        profile: fd.get('profile') || '',
        message: fd.get('message') || '',
        _subject: fd.get('_subject') || '',
        _honey: fd.get('_honey') || ''
      };
      fetch(form.getAttribute('data-ajax') || '/api/contact', {
        method: 'POST',
        headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      })
        .then(function (r) {
          return r.json().then(function (data) { return { ok: r.ok, status: r.status, data: data || {} }; },
            function () { throw new Error('bad-json:' + r.status); });
        })
        .then(function (res) {
          var data = res.data || {};
          var okFlag = String(data.success) === 'true';
          if (!res.ok || !okFlag) {
            var msg = (data && data.message) ? String(data.message) : '';
            status.className = 'form-status err';
            if (/activat/i.test(msg)) {
              status.textContent = 'Form delivery is not active for this mailbox yet. Please email admin@agenticqa.io directly, or try again after the form endpoint is confirmed.';
            } else if (msg) {
              status.textContent = 'Could not send the enquiry (' + msg.replace(/\s+/g, ' ').slice(0, 160) + '). Please email admin@agenticqa.io.';
            } else {
              status.textContent = 'Could not send the enquiry right now. Please email admin@agenticqa.io or try again later.';
            }
            return;
          }
          status.className = 'form-status ok';
          status.textContent = form.id === 'enquiry-form'
            ? 'Thanks! We will email you within 1–2 working days.'
            : 'Thanks! You are on the list — we will email you within 1–2 working days.';
          form.reset();
        })
        .catch(function () {
          status.className = 'form-status err';
          status.textContent = 'Could not send the enquiry right now. Please email admin@agenticqa.io or try again later.';
        })
        .then(function () { btn.disabled = false; });
    });
  }
})();

// v7 motion: section fade-ins, neural-line hero canvas, headline caret. Respects reduced motion.
(function () {
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce) return;
  if ('IntersectionObserver' in window) {
    var t = document.querySelectorAll('.section-head, .grid > *:not(.reveal), .fact, .photo-wrap');
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('v7-on'); io.unobserve(e.target); } });
    }, { threshold: 0.12 });
    t.forEach(function (el, i) { el.classList.add('v7-in'); el.style.transitionDelay = (i % 4) * 70 + 'ms'; io.observe(el); });
  }
  var g = document.querySelector('.hero h1 .grad');
  if (g) setTimeout(function () { g.classList.add('v7-typed'); }, 4000);
  var hero = document.querySelector('.hero');
  if (!hero) return;
  var c = document.createElement('canvas'); c.className = 'v7-net'; c.setAttribute('aria-hidden', 'true');
  hero.insertBefore(c, hero.firstChild);
  var x = c.getContext('2d'), w, h, pts = [], N = 38, run = true;
  function size() { w = c.width = hero.offsetWidth; h = c.height = hero.offsetHeight; }
  size(); addEventListener('resize', size);
  for (var i = 0; i < N; i++) pts.push({ x: Math.random() * w, y: Math.random() * h, vx: (Math.random() - .5) * .3, vy: (Math.random() - .5) * .3 });
  new IntersectionObserver(function (e) { run = e[0].isIntersecting; if (run) tick(); }).observe(hero);
  function tick() {
    if (!run) return;
    var col = getComputedStyle(document.documentElement).getPropertyValue('--brand').trim() || '#5B4BFF';
    x.clearRect(0, 0, w, h); x.fillStyle = col; x.strokeStyle = col;
    for (var i = 0; i < N; i++) { var p = pts[i]; p.x += p.vx; p.y += p.vy;
      if (p.x < 0 || p.x > w) p.vx *= -1; if (p.y < 0 || p.y > h) p.vy *= -1;
      x.globalAlpha = .5; x.beginPath(); x.arc(p.x, p.y, 1.8, 0, 6.3); x.fill();
      for (var j = i + 1; j < N; j++) { var q = pts[j], d = Math.hypot(p.x - q.x, p.y - q.y);
        if (d < 140) { x.globalAlpha = (1 - d / 140) * .25; x.beginPath(); x.moveTo(p.x, p.y); x.lineTo(q.x, q.y); x.stroke(); } } }
    requestAnimationFrame(tick);
  }
})();
