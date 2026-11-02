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

  var year = document.getElementById('year');
  if (year) year.textContent = String(new Date().getFullYear());

  // Scroll reveal
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('visible'); io.unobserve(en.target); } });
    }, { threshold: 0.08 });
    els.forEach(function (el) { io.observe(el); });
  } else { els.forEach(function (el) { el.classList.add('visible'); }); }

  // Waitlist / contact form: AJAX to formsubmit.co, fall back to mailto
  var form = document.getElementById('waitlist-form');
  if (form) {
    var status = form.querySelector('.form-status');
    function mailtoFallback() {
      var d = new FormData(form);
      var body = 'Name: ' + (d.get('name') || '') + '\nEmail: ' + (d.get('email') || '') +
        '\nI am: ' + (d.get('profile') || '') + '\n\n' + (d.get('message') || '');
      window.location.href = 'mailto:ganesh@agenticqa.io?subject=' + encodeURIComponent(d.get('_subject') || 'Agentic QA enquiry') +
        '&body=' + encodeURIComponent(body);
    }
    form.addEventListener('submit', function (e) {
      if (!window.fetch) return; // native POST to formsubmit.co
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var btn = form.querySelector('button[type=submit]');
      btn.disabled = true; status.className = 'form-status'; status.textContent = 'Sending…';
      fetch(form.getAttribute('data-ajax'), { method: 'POST', headers: { 'Accept': 'application/json' }, body: new FormData(form) })
        .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
        .then(function () {
          status.className = 'form-status ok';
          status.textContent = 'Thanks! You are on the list — we will email you within 1–2 working days.';
          form.reset();
        })
        .catch(function () {
          status.className = 'form-status err';
          status.textContent = 'Could not send from the page — opening your email app instead.';
          mailtoFallback();
        })
        .then(function () { btn.disabled = false; });
    });
  }
})();
