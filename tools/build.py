#!/usr/bin/env python3
"""Generates hub + site pages from shared header/footer templates. Run: python3 tools/build.py"""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HUB = "https://agenticqa.io"
SITES = {
 "ai": ("https://ai.agenticqa.io", "AI for Business"),
 "aiengineering": ("https://aiengineering.agenticqa.io", "AI Engineering"),
 "neetjee": ("https://neetjee.agenticqa.io", "NEET Prep"),
 "playwrightai": ("https://playwrightai.agenticqa.io", "Playwright + AI"),
}
SUN = '<svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg><svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
MENU = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'

def page(title, desc, canonical, nav, cta, body, tag="", accent="neural", cta_href="#contact"):
    navhtml = "\n      ".join(f'<a href="{h}">{t}</a>' for h, t in nav)
    tagh = f' <span class="site-tag">{tag}</span>' if tag else ""
    return f'''<!DOCTYPE html>
<html lang="en" data-accent="{accent}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">
  <meta name="theme-color" content="#5B4BFF">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Agentic QA Technologies">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="https://agenticqa.io/assets/brand/og-image.png">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" type="image/svg+xml" href="/assets/brand/icon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/brand/favicon-32.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/assets/brand/apple-touch-icon.png">
  <script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.setAttribute('data-theme',t)}}catch(e){{}}</script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/styles.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="./" aria-label="Agentic QA Technologies — {tag or 'home'}"><img class="logo-l" src="/assets/brand/logo.svg" alt="Agentic QA Technologies" width="150" height="40"><img class="logo-d" src="/assets/brand/logo-dark.svg" alt="" aria-hidden="true" width="150" height="40">{tagh}</a>
    <nav class="site-nav" id="site-nav" aria-label="Primary">
      {navhtml}
    </nav>
    <a class="btn btn-primary btn-sm hdr-cta" href="{cta_href}">{cta}</a>
    <button class="icon-btn theme-toggle" type="button" aria-label="Toggle dark mode">{SUN}</button>
    <button class="icon-btn nav-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="site-nav">{MENU}</button>
  </div>
</header>
<main id="main">
{body}
</main>
<footer>
  <div class="wrap">
    <div class="foot">
      <div>
        <a class="brand brand-foot" href="{HUB}/" aria-label="Agentic QA Technologies home"><img class="logo-l" src="/assets/brand/logo.svg" alt="Agentic QA Technologies" width="220" height="58" loading="lazy"><img class="logo-d" src="/assets/brand/logo-dark.svg" alt="" aria-hidden="true" width="220" height="58" loading="lazy"></a>
        <p class="brand-tag">AI automation, AI engineering and learning</p>
      </div>
      <div><h4>Sites</h4><ul><li><a href="{HUB}/" data-prod-href="{HUB}/">Agentic QA home</a></li><li><a href="/?site=ai" data-prod-href="{SITES['ai'][0]}/" data-site="ai">AI for Business</a></li><li><a href="/?site=aiengineering" data-prod-href="{SITES['aiengineering'][0]}/" data-site="aiengineering">AI Engineering</a></li><li><a href="/?site=neetjee" data-prod-href="{SITES['neetjee'][0]}/" data-site="neetjee">NEET Prep</a></li><li><a href="/?site=playwrightai" data-prod-href="{SITES['playwrightai'][0]}/" data-site="playwrightai">Playwright + AI</a></li></ul></div>
      <div><h4>Company</h4><ul><li><a href="{HUB}/#about">About</a></li><li><a href="{HUB}/privacy.html">Privacy</a></li></ul></div>
      <div><h4>Connect</h4><ul><li><a href="tel:+919663434422">+91 96634 34422</a></li><li><a href="https://wa.me/919663434422" rel="noopener">WhatsApp</a></li><li><a href="mailto:admin@agenticqa.io">admin@agenticqa.io</a></li><li><a href="https://www.youtube.com/@AgenticQA" rel="noopener">YouTube @AgenticQA</a></li><li><a href="https://www.linkedin.com/in/ganesan-sivaraman/" rel="noopener">LinkedIn</a></li></ul></div>
    </div>
    <p class="copy">© <span id="year">2026</span> Agentic QA Technologies LLP · LLPIN: <span style="white-space:nowrap">ACV-7177</span> · Registered in Puducherry, India</p>
  </div>
</footer>
<script src="/assets/js/site.js?v=20261106m1" defer></script>
</body>
</html>
'''

def contact(eyebrow, heading, text, subject, interests, profiles, button, sid="waitlist"):
    opts = "".join(f"<option>{o}</option>" for o in interests)
    pro = "".join(f"<option>{o}</option>" for o in profiles)
    s = subject.replace(" ", "%20")
    return f'''<section id="{sid}" class="alt">
  <div class="wrap contact" id="contact">
    <div>
      <span class="eyebrow">{eyebrow}</span>
      <h2>{heading}</h2>
      <p class="muted">{text}</p>
      <ul class="links">
        <li><a href="tel:+919663434422">☎ +91 96634 34422</a> · <a href="https://wa.me/919663434422" rel="noopener">WhatsApp</a></li>
        <li><a href="mailto:admin@agenticqa.io?subject={s}">✉ admin@agenticqa.io</a></li>
        <li><a href="https://www.youtube.com/@AgenticQA" rel="noopener">▶ YouTube — @AgenticQA</a></li>
      </ul>
    </div>
    <form class="form" id="{sid}-form" action="/api/contact" data-ajax="/api/contact" method="POST" novalidate>
      <input type="hidden" name="_subject" value="{subject}">
      <input type="hidden" name="_template" value="table">
      <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
      <div class="row2">
        <div class="field"><label for="f-name">Name</label><input id="f-name" name="name" autocomplete="name" required></div>
        <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
      </div>
      <div class="field"><label for="f-interest">I'm interested in</label><select id="f-interest" name="interest">{opts}</select></div>
      <div class="field"><label for="f-profile">I am…</label><select id="f-profile" name="profile">{pro}</select></div>
      <div class="field"><label for="f-msg">Anything we should know? <span class="muted">(optional)</span></label><textarea id="f-msg" name="message" rows="4"></textarea></div>
      <button class="btn btn-primary" type="submit" style="width:100%">{button}</button>
      <p class="form-status" role="status" aria-live="polite"></p>
      <p class="form-note">We only use your details to reply to you. See our <a href="{HUB}/privacy.html">privacy policy</a>.</p>
    </form>
  </div>
</section>'''

IC = {
 "agent":'<rect x="5" y="7" width="14" height="11" rx="3"/><path d="M12 3v4M9 12h.01M15 12h.01M9.5 15h5"/>',
 "flow":'<circle cx="6" cy="6" r="2.5"/><circle cx="18" cy="18" r="2.5"/><path d="M8.5 6H14a4 4 0 0 1 4 4v5.5M6 8.5V15a3 3 0 0 0 3 3h6.5"/>',
 "check":'<path d="M4 12.5l5 5L20 6.5"/>',
 "gauge":'<path d="M4 16a8 8 0 1 1 16 0"/><path d="M12 16l4-5"/>',
 "doc":'<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5M10 13h6M10 17h6"/>',
 "people":'<circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M15 14.5c3 0 6 1.8 6 5"/>',
 "code":'<path d="M8 8l-4 4 4 4M16 8l4 4-4 4M13.5 5l-3 14"/>',
 "db":'<ellipse cx="12" cy="6" rx="7" ry="2.6"/><path d="M5 6v12c0 1.4 3.1 2.6 7 2.6s7-1.2 7-2.6V6M5 12c0 1.4 3.1 2.6 7 2.6s7-1.2 7-2.6"/>',
 "leaf":'<path d="M5 19C5 10 11 5 20 4c0 9-5 15-14 15z"/><path d="M5 19l8-8"/>',
 "flask":'<path d="M9 3h6M10 3v6L4.5 18.5A1.8 1.8 0 0 0 6 21h12a1.8 1.8 0 0 0 1.5-2.5L14 9V3"/><path d="M7 15h10"/>',
 "atom":'<circle cx="12" cy="12" r="1.6"/><ellipse cx="12" cy="12" rx="9" ry="3.6"/><ellipse cx="12" cy="12" rx="9" ry="3.6" transform="rotate(60 12 12)"/><ellipse cx="12" cy="12" rx="9" ry="3.6" transform="rotate(120 12 12)"/>',
 "clock":'<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
 "chart":'<path d="M4 20V4M4 20h16M8 16v-4M12 16V8M16 16v-6"/>',
 "bug":'<rect x="7" y="8" width="10" height="12" rx="5"/><path d="M12 8v12M4 13h3M17 13h3M5 8l2.5 2M19 8l-2.5 2M9 5l1.5 2M15 5l-1.5 2"/>',
 "layers":'<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
 "spark":'<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M19 16l.8 2.2L22 19l-2.2.8L19 22l-.8-2.2L16 19l2.2-.8z"/>',
 "rocket":'<path d="M5 15c-1 1-1.5 4-1.5 4s3-.5 4-1.5M14 4c3-1 6-1 6-1s0 3-1 6l-6 6-5-5z"/><circle cx="15" cy="9" r="1.5"/>',
 "pc":'<rect x="3" y="4.5" width="18" height="12" rx="2"/><path d="M8 20h8M12 16.5V20"/>',
 "book":'<path d="M4 5.5C6.5 4 9.5 4 12 5.5 14.5 4 17.5 4 20 5.5V19c-2.5-1.5-5.5-1.5-8 0-2.5-1.5-5.5-1.5-8 0z"/><path d="M12 5.5V19"/>',
}
def ico(k): return f'<span class="ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{IC[k]}</svg></span>'
def cards(items, cls="g3", icons=None):
    return f'<div class="grid {cls}">' + "".join(f'<article class="card reveal">{ico(icons[i]) if icons else ""}<h3>{it[0]}</h3><p class="muted">{it[1]}</p></article>' for i, it in enumerate(items)) + "</div>"
def ticks(items, cls="g2"):
    return f'<div class="grid {cls} tick-cards">' + "".join(f'<div class="tick reveal"><span aria-hidden="true">✓</span>{t}</div>' for t in items) + "</div>"

def head(eyebrow, h2, lede=""):
    l = f'<p class="lede">{lede}</p>' if lede else ""
    return f'<div class="section-head"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2>{l}</div>'

import random as _r
def _art(seed):
    r=_r.Random(seed); pts=[(r.randint(40,520),r.randint(30,420)) for _ in range(16)]
    ln="".join(f'<line x1="{a[0]}" y1="{a[1]}" x2="{c[0]}" y2="{c[1]}"/>' for i,a in enumerate(pts) for c in pts[i+1:i+3])
    cs="".join(f'<circle cx="{x}" cy="{y}" r="{r.choice([3,4,5,7])}"/>' for x,y in pts)
    return f'<svg class="ai-art" viewBox="0 0 560 450" aria-hidden="true" focusable="false"><g>{ln}</g><g>{cs}</g></svg>'
# ---- Hero illustrations (inline SVG; styled via CSS classes; decorative) ----
def _svg(inner, label):
    return f'<figure class="hero-visual" aria-hidden="true"><svg class="hv" viewBox="0 0 480 400" focusable="false" role="presentation"><defs><linearGradient id="hvg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" class="hv-s1"/><stop offset="1" class="hv-s2"/></linearGradient></defs>{inner}</svg><figcaption class="hv-cap">{label}</figcaption></figure>'
def _node(x, y, w, h, t, sub="", hot=False, d=0):
    s = f'<text class="hv-sub" x="{x+16}" y="{y+h-14}">{sub}</text>' if sub else ""
    return f'<g class="hv-node{" hot" if hot else ""}" style="--d:{d}s"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14"/><text class="hv-t" x="{x+16}" y="{y+(26 if sub else h/2+5)}">{t}</text>{s}</g>'
def _wire(d, delay=0):
    return f'<path class="hv-wire" d="{d}" style="--d:{delay}s"/>'
def hero_art(kind):
    if kind == "hub":
        nodes = [(240,64,"AI for Business"),(410,200,"AI Engineering"),(240,336,"NEET Prep"),(70,200,"Playwright + AI")]
        rings = '<circle class="hv-ring r1" cx="240" cy="200" r="136"/><circle class="hv-ring r2" cx="240" cy="200" r="92"/>'
        wires = "".join(_wire(f"M240 200 L{x} {y}", i*.4) for i,(x,y,_) in enumerate(nodes))
        dots = "".join(f'<g class="hv-orb" style="--d:{i*.5}s"><circle cx="{x}" cy="{y}" r="30"/><text class="hv-t c" x="{x}" y="{y+(52 if y>=200 else -42)}" text-anchor="middle">{t}</text></g>' for i,(x,y,t) in enumerate(nodes))
        icons = '<path class="hv-ico" d="M232 58h16M240 50v16"/><path class="hv-ico" d="M398 200l8-8 8 8-8 8z"/><circle class="hv-ico" cx="240" cy="336" r="9"/><path class="hv-ico" d="M60 196l8 8 14-14"/>'
        core = '<g class="hv-core"><circle cx="240" cy="200" r="54"/><text x="240" y="208" text-anchor="middle">AQ</text></g>'
        return _svg(rings + wires + dots + icons + core, "One company · four focused sites")
    if kind == "ai":
        inner = (_node(20,40,140,56,"Inbox &amp; tickets","inputs",d=0)+_node(20,172,140,56,"Docs &amp; CRM","company data",d=.2)+_node(20,304,140,56,"Workflows","manual today",d=.4)
          + _wire("M160 68 C210 68 200 200 240 200",0)+_wire("M160 200 L240 200",.3)+_wire("M160 332 C210 332 200 200 240 200",.6)
          + '<g class="hv-core sq"><rect x="240" y="150" width="110" height="100" rx="22"/><text x="295" y="196" text-anchor="middle">Agent</text><text class="hv-sub2" x="295" y="218" text-anchor="middle">tools · MCP</text></g>'
          + _wire("M350 200 L380 200",.9)
          + _node(380,110,90,56,"Eval ✓","guardrails",True,.6)+_node(380,234,90,56,"Human","checkpoint",d=.8)
          + _wire("M425 166 L425 234",1.2))
        return _svg(inner, "Agents with evaluation and human checkpoints")
    if kind == "ae":
        vec = "".join(f'<circle class="hv-vec" cx="{250+ (i%6)*16}" cy="{150+(i//6)*16}" r="4" style="--d:{(i%7)*.25}s"/>' for i in range(30))
        inner = (_node(16,40,130,56,"Documents","ingest")+_node(16,172,130,56,"Chunks","split + overlap",d=.2)
          + _wire("M81 96 L81 172",0)+_wire("M146 200 L234 200",.3)
          + '<rect class="hv-panel" x="234" y="130" width="112" height="104" rx="16"/>' + vec + '<text class="hv-sub" x="244" y="254">vector store</text>'
          + _wire("M346 182 L376 182",.6)
          + _node(376,40,94,56,"Retrieve","rerank",d=.3)+_node(376,154,94,56,"LLM","+ tools",True,.5)+_node(376,268,94,56,"Answer","citations",d=.7)
          + _wire("M423 96 L423 154",.9)+_wire("M423 210 L423 268",1.2)
          + _node(16,304,200,56,"Eval harness","golden set · regression gate",d=.9) + _wire("M216 332 L376 300",1.5))
        return _svg(inner, "Retrieval-augmented generation, end to end")
    if kind == "neet":
        subj = [(120,120,"Biology"),(360,120,"Chemistry"),(240,300,"Physics")]
        inner = "".join(f'<g class="hv-orb" style="--d:{i*.6}s"><circle cx="{x}" cy="{y}" r="58"/><text class="hv-t c" x="{x}" y="{y+5}" text-anchor="middle">{t}</text></g>' for i,(x,y,t) in enumerate(subj))
        inner = _wire("M120 120 L360 120",0)+_wire("M360 120 L240 300",.4)+_wire("M240 300 L120 120",.8) + inner
        bars = "".join(f'<rect class="hv-bar" x="196" y="{176+i*16}" width="{w}" height="8" rx="4" style="--d:{i*.3}s"/>' for i,w in enumerate([88,64,76]))
        inner += '<rect class="hv-panel" x="180" y="160" width="120" height="72" rx="14"/>' + bars
        return _svg(inner, "NCERT-aligned plan across all three subjects")
    return ""

def write(rel, html):
    import re as _re
    p = os.path.join(ROOT, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write(html)

# ---------------- HUB ----------------
hub_cards = [
 ("ai", "AI for Business", "Custom AI agents, automation consulting and AI-native QA for companies. We scope your workflows, build agents that fit your stack, and evaluate them before they reach users."),
 ("aiengineering", "AI Engineering", "The builder track: LLMs, retrieval-augmented generation, vector databases, agents and MCP, evaluation and fine-tuning — with in-house projects as working examples."),
 ("neetjee", "NEET Prep (CatalystAI)", "CatalystAI-powered NEET preparation: NCERT-aligned subject maps, mock tests and personalised study plans with doubt-solving support."),
 ("playwrightai", "Playwright + AI", "Playwright test automation with AI-assisted testing — tutorials, hands-on labs and Playwright MCP, for testers and teams moving into AI-era automation."),
]
HUB_ICO = {
 "ai": '<path d="M12 3v3M12 18v3M3 12h3M18 12h3"/><rect x="7" y="7" width="10" height="10" rx="3"/><circle cx="12" cy="12" r="1.6"/>',
 "aiengineering": '<ellipse cx="12" cy="6" rx="7" ry="2.6"/><path d="M5 6v6c0 1.4 3.1 2.6 7 2.6s7-1.2 7-2.6V6M5 12v6c0 1.4 3.1 2.6 7 2.6s7-1.2 7-2.6v-6"/>',
 "neetjee": '<path d="M4 6.5C6.5 5 9.5 5 12 6.5 14.5 5 17.5 5 20 6.5V19c-2.5-1.5-5.5-1.5-8 0-2.5-1.5-5.5-1.5-8 0z"/><path d="M12 6.5V19"/>',
 "playwrightai": '<rect x="3" y="4.5" width="18" height="15" rx="2.5"/><path d="M3 9h18M7.5 14l2 2 4-4"/>',
}
cardhtml = '<div class="hub-cards">' + "".join(
 f'<a class="hub-card reveal" href="/?site={k}" data-prod-href="{SITES[k][0]}/" data-site="{k}" data-accent-card="{k}"><span class="hc-ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{HUB_ICO[k]}</svg></span><span class="host">{SITES[k][0][8:]}</span><h3>{t}</h3><p>{d}</p><span class="go">Visit site <span aria-hidden="true">→</span></span></a>' for k, t, d in hub_cards) + "</div>"
PROJ = [("ResumeGenieAI.webp","ResumeGenie AI","ResumeGenie AI dashboard","LLM feedback with structured critique"),
 ("StudyMateAI.webp","StudyMate AI","StudyMate AI interface","Retrieval over large PDFs, with citations"),
 ("FeedBack_Pulse.webp","FeedbackPulse AI","FeedbackPulse sentiment dashboard","Sentiment and theme clustering"),
 ("MeetingMind_AI_.webp","MeetingMind AI","MeetingMind AI screen","Summaries and action items")]
def proj_strip():
    return '<div class="proj-strip">' + "".join(f'<figure class="pshot reveal"><div class="pframe"><span class="pbar" aria-hidden="true"><i></i><i></i><i></i></span><img src="/assets/img/{f}" alt="{a}" width="1200" height="660" loading="lazy" decoding="async"></div><figcaption><b>{t}</b><span>{d}</span></figcaption></figure>' for f,t,a,d in PROJ) + "</div>"
hub_body = f'''<section class="hero" id="company">
  <div class="wrap hero-grid"><div class="hero-copy">
    <span class="pill"><span class="dot" aria-hidden="true"></span>Agentic QA Technologies LLP</span>
    <h1>AI-native quality engineering and <span class="grad">AI agents for real-world teams.</span></h1>
    <p class="lede">Agentic QA Technologies LLP is a Bengaluru-based AI and automation engineering company. We build AI-native quality engineering solutions, custom AI agents and evaluation pipelines for companies — and run structured programmes that develop industry-ready AI and automation skills.</p>
    <div class="cta-row"><a class="btn btn-primary" href="#about">About the company</a><a class="btn btn-ghost" href="#contact">Talk to us</a></div>
</div>
  {hero_art("hub")}
  </div>
</section>
<div class="trust-band"><div class="wrap"><ul><li><b>LLP</b><span>Registered · LLPIN ACV-7177</span></li><li><b>4</b><span>Focused sites</span></li><li><b>4</b><span>In-house AI products</span></li><li><b>MCP · RAG · Evals</b><span>Core practice areas</span></li></ul></div></div>
<section id="about" class="alt">
  <div class="wrap">
    {head("Who we are", "An AI and quality engineering company.", "Agentic QA Technologies LLP (LLPIN ACV-7177, registered in Puducherry, India) works where AI systems meet software quality: building, testing and evaluating AI-powered software, and helping people and teams do the same.")}
    {cards([("AI-native quality engineering", "Playwright and API automation with AI-assisted triage, CI/CD integration and test strategy for modern web products."),
            ("Custom AI agents", "Task-specific agents connected to company data and tools through APIs and MCP servers, with human checkpoints where they matter."),
            ("LLM &amp; agent evaluation", "Evaluation suites (DeepEval, Ragas, LangSmith) that measure accuracy, safety and regressions in LLM and RAG features."),
            ("Automation consulting", "Identify high-value automation opportunities, define API and MCP integration requirements, and create a delivery roadmap covering implementation, evaluation and CI/CD."),
            ("Skill programmes", "Structured, hands-on programmes in AI engineering, Playwright + AI and NEET preparation, each run on its own site."),
            ("In-house tooling", "Explore working AI applications built by our team, demonstrating RAG, structured LLM feedback, sentiment analysis and meeting summarisation.")])}
    <div class="grid g2 mv" style="margin-top:40px">
      <article class="mv-card reveal"><h3>Our aims</h3><p>Deliver reliable AI and QA outcomes for business clients, and make engineers job-ready for the AI era by working the way real teams practise: live, hands-on and project-driven.</p></article>
      <article class="mv-card reveal"><h3>Our goals</h3><p>Build durable in-house tooling and programmes; serve companies with consulting and custom agents; and support learners through clear pathways — AI engineering, Playwright + AI, and NEET preparation through CatalystAI.</p></article>
    </div>
    <div class="section-head" style="margin-top:48px"><span class="eyebrow">Achievements</span><h3>What we have built so far.</h3></div>
    <ul class="checklist">
      <li>Registered as Agentic QA Technologies LLP — LLPIN ACV-7177, Puducherry, India</li>
      <li>In-house applied AI projects: FeedbackPulse, MeetingMind, ResumeGenie and StudyMate</li>
      <li>Industry Internship Completion Certificates issued to programme graduates</li>
      <li>Four focused sites for business, engineering, exam-prep and automation work</li>
    </ul>
    <div class="section-head" style="margin-top:56px"><span class="eyebrow">In-house AI products</span><h3>Applied AI built and run by our own team.</h3></div>
    {proj_strip()}
  </div>
</section>
<section id="founder"><div class="wrap">
  {head("Leadership", "The founders.", "Turning emerging technology into real-world impact—our founders bring together AI engineering, intelligent automation, quality engineering and modern software development to build solutions and empower the next generation of tech talent.")}
  <div class="founders">
    <article class="founder-card reveal">
      <img class="f-photo" src="/assets/img/ganesh.webp" alt="Ganesan (Ganesh) Sivaraman" width="272" height="272" loading="lazy">
      <span class="eyebrow">Founder</span>
      <h2>Ganesan (Ganesh) Sivaraman</h2>
      <p class="f-role"><strong>AI QA Architect · MCP Servers · LLM &amp; Agent Evaluation · RAG · Playwright + AI</strong><br>Founder, Agentic QA Technologies · Bengaluru</p>
      <p>Ganesh architects AI-native QA: MCP servers, LLM and agent evaluation with DeepEval, Ragas and LangSmith, RAG systems, and Playwright + AI frameworks in TypeScript. His path runs from manual testing to Playwright automation, QA management and AI automation architecture.</p>
      <p>At Symphony Talent he led QA, built a Playwright framework that lifted automated coverage by 80%, set up CI/CD for testing and worked on SkillCheck. At Agentic QA Technologies he leads consulting and delivery and teaches the programmes personally.</p>
      <p class="muted">Works with organisations on AI quality engineering, MCP integrations, AI evaluation and corporate training.</p>
      <ul class="timeline career" aria-label="Career path">
        <li><b>AI Automation Architect</b> — Agentic QA Technologies<span>May 2025–present</span></li>
        <li><b>QA Manager</b> — Symphony Talent<span>2018–2025</span></li>
        <li><b>QA Manager</b> — Harman Connected Services<span>2015–2018</span></li>
        <li><b>Test Lead</b> — First Advantage<span>2006–2015</span></li>
      </ul>
      <p class="muted f-edu">MCA, Bharathidasan University · B.Sc. Mathematics, University of Madras</p>
      <div class="cta-row f-cta"><a class="btn btn-primary btn-sm" href="mailto:ganesh@agenticqa.io?subject=Hello%20Ganesh">✉ ganesh@agenticqa.io</a><a class="btn btn-ghost btn-sm" href="https://www.linkedin.com/in/ganesan-sivaraman/" rel="noopener">LinkedIn profile</a><a class="btn btn-ghost btn-sm" href="https://www.youtube.com/@AgenticQA" rel="noopener">▶ YouTube @AgenticQA</a></div>
    </article>
    <article class="founder-card reveal" id="cofounder">
      <img class="f-photo" src="/assets/img/moksha.webp" alt="Moksha Meera" width="272" height="272" loading="lazy">
      <span class="eyebrow">Co-founder, Director &amp; Tech Lead</span>
      <h2>Moksha Meera</h2>
      <p class="f-role"><strong>Co-founder &amp; Director · Tech Lead · LLM Engineer · AI &amp; Automation Engineering</strong><br>Agentic QA Technologies · Bengaluru</p>
      <p>Moksha leads technical delivery for the company's in-house AI projects and automation tooling, combining hands-on development with practical training alongside Ganesh.</p>
      <ul class="timeline career" aria-label="Career path">
        <li><b>Co-founder, Director &amp; Tech Lead</b> — Agentic QA Technologies<span>Jan 2026–present</span></li>
        <li><b>Automation Engineer</b> — ePy-Tallent Tech solution<span>May 2024–Dec 2025</span></li>
      </ul>
      <p class="muted f-edu">M.Sc. Computer Science, Pondicherry University · B.Sc. Computer Science, Pondicherry University</p>
    </article>
  </div>
</div></section>
<section id="certificates" class="alt"><div class="wrap">
  {head("Certificates", "Industry Internship Completion Certificate.", "Graduates of our programmes receive an Industry Internship Completion Certificate from Agentic QA Technologies. It records that the learner completed the programme's hands-on work and capstone project under our team's guidance. It is issued by the company itself, not by an external accreditation body.")}
  <div class="cert-layout">
    <div class="cert-copy">
      <article class="card cert-grad reveal">
        <span class="eyebrow">Named graduate</span>
        <div class="grad-row"><img src="/assets/img/certificate-handover.webp" alt="Sivanesan P receiving his Industry Internship Completion Certificate from Ganesan Sivaraman" width="140" height="180" loading="lazy"><div><h3>Sivanesan P</h3><p class="muted">Programme graduate, receiving his certificate from Ganesan Sivaraman. Names on certificates match programme completion records.</p></div></div>
      </article>
      <div class="cert-facts">
        <article class="card reveal"><h3>What it means</h3><p class="muted">Proof of internship-style delivery work with the company: projects, reviews and a defined scope — not a government or university diploma.</p></article>
        <article class="card reveal"><h3>Issued by</h3><p class="muted">Agentic QA Technologies LLP (LLPIN ACV-7177), Puducherry — the same team that runs the work.</p></article>
      </div>
    </div>
    <figure class="cert-sample reveal">
      <img src="/assets/img/certificate-sample.svg" alt="Sample Industry Internship Completion Certificate layout from Agentic QA Technologies" width="840" height="594" loading="lazy">
      <figcaption class="muted">Sample certificate layout — placeholder name only; issued certificates carry the graduate's real name.</figcaption>
    </figure>
  </div>
</div></section>
<section id="activities">
  <div class="wrap">
    {head("Activities", "Four lines of work, one company.", "Each activity has its own site with full details.")}
    {cardhtml}
  </div>
</section>
''' + contact("Contact", "Talk to Agentic QA Technologies.", "Tell us what you are looking for — a project, a partnership or a question — and we will reply or set up a quick call.", "Agentic QA enquiry",
  ["AI for Business (agents / consulting)", "AI evaluation / MCP work", "AI Engineering", "NEET Prep", "Playwright + AI", "Partnership / other"],
  ["Company / team", "Working professional", "Student", "Parent", "Other"], "Send enquiry", "enquiry")
hub_nav = [("#about", "Company"), ("#founder", "Founders"), ("#certificates", "Certificates"), ("#activities", "Activities"), ("#contact", "Contact")]
write("hub/index.html", page("Agentic QA Technologies LLP — AI-native quality engineering & AI agents", "Agentic QA Technologies LLP: AI-native quality engineering, custom AI agents, LLM evaluation and consulting — with dedicated sites for AI engineering, NEET prep and Playwright + AI.", HUB + "/", hub_nav, "Contact", hub_body))

priv = open(os.path.join(ROOT, "archive/v7/privacy.html")).read()
pmain = priv.split('<main id="main">')[1].split("</main>")[0]
pmain = pmain.replace("across agenticqa.io", "across agenticqa.io and its subdomains (ai., aiengineering., neetjee., playwrightai.)")
write("hub/privacy.html", page("Privacy Policy | Agentic QA Technologies", "Privacy policy for agenticqa.io and its subdomains.", HUB + "/privacy.html", [("./", "Home"), ("./#activities", "Activities")], "Contact", pmain, cta_href=HUB + "/#contact"))

# ---------------- AI (business) ----------------
ai_body = f'''<section class="hero"><div class="wrap hero-grid"><div class="hero-copy">
  <span class="pill"><span class="dot" aria-hidden="true"></span>AI for Business · ai.agenticqa.io</span>
  <h1>Custom AI agents that <span class="grad">do real work for your team.</span></h1>
  <p class="lede">We design, build and hand over AI agents and automations that fit your existing tools — from support triage to QA pipelines — with evaluation and guardrails built in from day one.</p>
  <div class="cta-row"><a class="btn btn-primary" href="#contact">Book a discovery call</a><a class="btn btn-ghost" href="#services">See services</a></div>
</div>
  {hero_art("ai")}
</div></section>
<div class="trust-band"><div class="wrap"><ul><li><b>APIs + MCP</b><span>Agents wired to your tools</span></li><li><b>Evals first</b><span>DeepEval · Ragas · LangSmith</span></li><li><b>Human-in-the-loop</b><span>Checkpoints where it matters</span></li><li><b>Handover</b><span>Docs and enablement included</span></li></ul></div></div>
<section id="services" class="alt"><div class="wrap">
  {head("Services", "What we build for companies.")}
  {cards([("Custom AI agents", "Task-specific agents connected to your data and tools via APIs and MCP servers — with human-in-the-loop checkpoints where it matters."),
          ("Automation consulting", "We map your manual workflows, find the high-value automation candidates and give you a practical roadmap."),
          ("AI-native QA", "Playwright and API test automation with AI-assisted triage, self-healing locators and CI/CD integration."),
          ("LLM & agent evaluation", "Build evaluation suites using DeepEval, Ragas and LangSmith to assess response quality, retrieval performance and regressions in LLM and RAG applications."),
          ("RAG over your documents", "Retrieval-augmented assistants that answer from your own knowledge base, with sources shown."),
          ("Team enablement", "Train your engineers to maintain delivered agents, configure MCP integrations, run evaluations and extend Playwright and API test suites.")], icons=["agent","flow","bug","gauge","doc","people"])}
</div></section>
<section id="process"><div class="wrap">
  {head("How we work", "From first call to production.")}
  <ol class="journey steps-line reveal">
    <li><span>Step 1</span><h3>Discovery call</h3><p>We understand your goals, systems and constraints.</p></li>
    <li><span>Step 2</span><h3>Scoping</h3><p>A written proposal with deliverables, timeline and success measures.</p></li>
    <li><span>Step 3</span><h3>Build &amp; evaluate</h3><p>Iterative delivery with demos and an evaluation suite.</p></li>
    <li class="cap"><span>Step 4</span><h3>Handover</h3><p>Documentation, enablement and optional ongoing support.</p></li>
  </ol>
</div></section>
<section id="builds" class="alt"><div class="wrap">
  {head("Reference builds", "Applied AI we run in-house.", "The same patterns we deliver for clients — retrieval, summarisation, structured LLM feedback and sentiment analysis — running in our own products.")}
  {proj_strip()}
</div></section>
<section id="pricing"><div class="wrap">
  {head("Engagement models", "Three ways to work with us.", "We do not publish fixed packages. Fees depend on scope and are discussed on a call after we understand your needs.")}
  {cards([("Discovery sprint", "A short, scoped review of your workflows and data that ends in a written automation roadmap and a recommended first agent."),
          ("Build &amp; handover", "We design, build and evaluate an agent or automation end to end, then hand it over with documentation and enablement."),
          ("Ongoing support", "Optional monitoring, evaluation runs and iteration after go-live, so quality holds as your data and tools change.")], icons=["spark","rocket","chart"])}
  <div class="fee-strip reveal"><span>Fees are scoped per engagement and shared on a call.</span><a class="btn btn-primary btn-sm" href="#contact">Request a pricing call</a></div>
</div></section>
''' + contact("Enquiries", "Tell us what you want to automate.", "Share a short description of your workflow and we will set up a call. Fees are discussed on the call.", "AI for Business enquiry",
  ["Custom AI agent", "Automation consulting", "AI-native QA", "LLM evaluation", "Pricing call", "Other"], ["Founder / leadership", "Engineering lead", "Product / operations", "Other"], "Request a call", "enquiry")
write("sites/ai/index.html", page("AI for Business — Custom AI agents & automation consulting | Agentic QA", "Custom AI agents, automation consulting and AI-native QA for companies. Fees discussed on a call.", SITES['ai'][0] + "/", [("#services", "Services"), ("#process", "Process"), ("#builds", "Builds"), ("#pricing", "Pricing"), (HUB + "/", "Agentic QA home")], "Book a call", ai_body, "Business", "signal"))

# ---------------- AI Engineering ----------------
ae_body = f'''<section class="hero"><div class="wrap hero-grid"><div class="hero-copy">
  <span class="pill"><span class="dot" aria-hidden="true"></span>AI Engineering · aiengineering.agenticqa.io</span>
  <h1>Build real systems with <span class="grad">LLMs, RAG and vector databases.</span></h1>
  <p class="lede">The technical builder track for developers and SDETs who want production-style LLM systems — retrieval pipelines, agents over MCP, evaluation harnesses and parameter-efficient fine-tuning — not a Playwright testing syllabus.</p>
  <div class="cta-row"><a class="btn btn-primary" href="#contact">Join the waitlist</a><a class="btn btn-ghost" href="#curriculum">See the curriculum</a></div>
</div>
  {hero_art("ae")}
</div></section>
<section id="curriculum" class="alt"><div class="wrap">
  {head("Curriculum", "Technical depth across the LLM stack.", "Eight focus areas. Each ends with a working notebook or repo you can keep.")}
  {cards([("LLM API craft", "Chat and completion APIs, system prompts, structured JSON output, tool calling, streaming and token budgeting."),
          ("Prompt systems", "Few-shot patterns, chain-of-thought where it helps, guardrails, and failure modes when prompts drift."),
          ("Embeddings &amp; chunking", "Embedding models, chunk strategies, overlap, metadata filters and hybrid lexical + vector search."),
          ("RAG pipelines", "Ingest → index → retrieve → rerank → generate with citations; hallucination checks before answers ship."),
          ("Vector databases", "ChromaDB and comparable stores: collections, indexing choices, freshness and cost at modest scale."),
          ("Agents &amp; MCP", "Multi-step agents, MCP server design, tool allowlists and human checkpoints for risky actions."),
          ("Evaluation harnesses", "DeepEval, Ragas and LangSmith-style suites: golden sets, regression gates and red-team probes."),
          ("Fine-tuning choices", "When to fine-tune vs prompt vs RAG; dataset prep and LoRA / PEFT trade-offs.")], "g2", icons=["code","spark","layers","flow","db","agent","gauge","chart"])}
</div></section>
<section id="stack"><div class="wrap">
  {head("Stack we practise", "Tools you will touch on the builder track.")}
  <ul class="chips">{"".join(f'<li>{t}</li>' for t in ["Python","TypeScript","LLM APIs","ChromaDB","Embeddings","MCP servers","DeepEval","Ragas","LangSmith","LoRA / PEFT","GitHub Actions"])}</ul>
  <ul class="checklist">
    <li>Python + TypeScript clients for major LLM APIs</li>
    <li>ChromaDB (and comparable vector stores) for retrieval labs</li>
    <li>MCP servers as the bridge between agents and real tools</li>
    <li>DeepEval / Ragas-style metrics wired into a small CI gate</li>
    <li>In-house apps (ResumeGenie, StudyMate, FeedbackPulse, MeetingMind) as reference implementations</li>
  </ul>
</div></section>
<section id="projects" class="alt"><div class="wrap">
  {head("Projects", "Real AI projects, not toy demos.", "Builders work through in-house projects like these.")}
  <div class="grid g2">
    <article class="card project reveal"><img src="/assets/img/ResumeGenieAI.webp" alt="ResumeGenie AI dashboard" width="1200" height="657" loading="lazy"><div class="body"><span class="tag">RAG · LLM</span><h3>ResumeGenie AI</h3><p>Resume analysis and improvement suggestions powered by LLM feedback with structured critique outputs.</p></div></article>
    <article class="card project reveal"><img src="/assets/img/StudyMateAI.webp" alt="StudyMate AI interface" width="1200" height="653" loading="lazy"><div class="body"><span class="tag">RAG · ChromaDB</span><h3>StudyMate AI</h3><p>Ask questions over large PDFs with a retrieval-augmented study assistant and source citations.</p></div></article>
    <article class="card project reveal"><img src="/assets/img/FeedBack_Pulse.webp" alt="FeedbackPulse sentiment dashboard" width="1200" height="664" loading="lazy"><div class="body"><span class="tag">NLP · Sentiment</span><h3>FeedbackPulse AI</h3><p>Batch sentiment analysis of customer reviews for product teams, with theme clustering.</p></div></article>
    <article class="card project reveal"><img src="/assets/img/MeetingMind_AI_.webp" alt="MeetingMind AI screen" width="1200" height="657" loading="lazy"><div class="body"><span class="tag">LLM · Summaries</span><h3>MeetingMind AI</h3><p>Meeting assistant that summarises discussions and extracts action items with owners.</p></div></article>
  </div>
</div></section>
<section id="format"><div class="wrap">
  {head("Format", "Live, hands-on, project-driven.")}
  {cards([("Live sessions", "Guided labs in every class, not pre-recorded video."), ("Taught by the builders", "Ganesh and Moksha teach from the systems they ship."), ("Portfolio on GitHub", "Each focus area ends in a repo you keep."), ("Fees on a call", "Fees and batch dates are shared on a quick call.")], "g4 feat", icons=["pc","people","code","clock"])}
</div></section>
''' + contact("Next batch", "Join the AI Engineering waitlist.", "We will email batch dates and an invite to a demo session. Fees are shared on a call.", "AI Engineering waitlist",
  ["Join the waitlist", "Free demo session", "Team / company cohort", "Other"], ["Developer", "Tester / SDET", "Student / fresher", "Company / team"], "Join the waitlist")
write("sites/aiengineering/index.html", page("AI Engineering — LLMs, RAG, vector databases & fine-tuning | Agentic QA", "Hands-on AI engineering builder track: LLMs, RAG, vector databases, agents, MCP, evaluation and fine-tuning.", SITES['aiengineering'][0] + "/", [("#curriculum", "Curriculum"), ("#stack", "Stack"), ("#projects", "Projects"), ("#format", "Format"), (HUB + "/", "Agentic QA home")], "Join waitlist", ae_body, "Engineering", "mint"))

# ---------------- NEET ----------------
nj_body = f'''<section class="hero"><div class="wrap hero-grid"><div class="hero-copy">
  <span class="pill"><span class="dot" aria-hidden="true"></span>CatalystAI · neetjee.agenticqa.io</span>
  <ul class="stat-chips"><li>NCERT-aligned</li><li>Chapter tests &amp; full mocks</li><li>Personalised study plans</li></ul>
  <h1>NEET preparation with <span class="grad">a plan that adapts to you.</span></h1>
  <p class="lede">CatalystAI on <strong>neetjee</strong>.agenticqa.io combines AI-powered study plans, visual explanations and doubt-solving for NEET aspirants — NCERT-aligned, weak-area focused, with a growing JEE practice track.</p>
  <div class="cta-row"><a class="btn btn-primary" href="#contact">Join the waitlist</a><a class="btn btn-ghost" href="#syllabus">See the syllabus</a></div>
</div>
  {hero_art("neet")}
</div></section>
<section id="syllabus" class="alt"><div class="wrap">
  {head("NEET syllabus", "NCERT-aligned coverage of all three subjects.")}
  {cards([("Biology", "Diversity of living organisms, cell biology, plant and human physiology, genetics and evolution, ecology."),
          ("Chemistry", "Physical, organic and inorganic chemistry with concept maps and reaction practice."),
          ("Physics", "Mechanics, thermodynamics, electrostatics, optics and modern physics with step-by-step problem solving.")], "g3 subj", icons=["leaf","flask","atom"])}
</div></section>
<section id="jee"><div class="wrap">
  {head("JEE practice track", "Same CatalystAI approach for JEE aspirants.", "Physics, Chemistry and Mathematics practice sets with timed mocks — alongside the core NEET path.")}
  {cards([("Physics &amp; Chemistry depth", "JEE-style numericals and multi-concept problems layered on the same NCERT foundation."),
          ("Mathematics", "Algebra, calculus, coordinate geometry and trigonometry drills with step solutions."),
          ("Timed JEE mocks", "Full-length practice under exam timing, with weak-topic follow-ups.")])}
</div></section>
<section id="mocks" class="alt"><div class="wrap">
  {head("Mock tests", "Practise under exam conditions.")}
  {cards([("Chapter tests", "Short tests after each chapter to lock in concepts."), ("Full-length mocks", "Timed mocks in the NEET pattern with detailed solutions."), ("Weak-area analysis", "AI highlights topics to revisit based on your answers.")], icons=["book","clock","chart"])}
</div></section>
<section id="plans"><div class="wrap">
  {head("Study plans", "Small steps every day.")}
  {ticks(["Personalised daily and weekly study plans","Smart flashcards and spaced revision","Doubt-solving and follow-ups from our student support team","Progress check-ins you can share with parents"])}
  <blockquote class="quote-banner">&ldquo;Small steps every day add up to big results on exam day.&rdquo;</blockquote>
</div></section>
<section id="team" class="alt"><div class="wrap">
  {head("Team", "The people behind CatalystAI.")}
  <div class="grid g3 team"><article class="card team-card reveal"><img src="/assets/img/pradhidhan.webp" alt="Pradhidhan R G" width="160" height="160" loading="lazy"><span class="eyebrow">CatalystAI team</span><h3>Pradhidhan R G</h3><p class="muted">Pradhidhan R G works with the CatalystAI team on content and learner experience for NEET and JEE practice.</p></article><article class="card team-card reveal"><img src="/assets/img/tanushka-grey.webp" alt="Thanushka Mira" width="160" height="160" loading="lazy"><span class="eyebrow">Student support</span><h3>Thanushka Mira</h3><p class="muted">Thanushka Mira looks after student support for CatalystAI, helping NEET learners with study planning, practice sets and day-to-day doubt follow-ups.</p></article><article class="card team-card reveal"><img src="/assets/img/heri.webp" alt="Hari Krishna G" width="160" height="160" loading="lazy"><span class="eyebrow">Campus ambassador</span><h3>Hari Krishna G</h3><p class="muted">Hari Krishna G supports the CatalystAI community as campus ambassador, sharing study resources and helping with event sign-ups.</p></article></div>
</div></section>
''' + contact("CatalystAI", "Join the NEET Prep waitlist.", "We will share programme details and next steps. Fees are shared on a call.", "CatalystAI NEET enquiry",
  ["Join the waitlist", "NEET mocks", "JEE practice", "Study plan", "Other"], ["Student", "Parent", "School / coaching centre"], "Join the waitlist")
write("sites/neetjee/index.html", page("NEET Prep — CatalystAI on neetjee | Agentic QA", "CatalystAI NEET and JEE preparation on neetjee.agenticqa.io: NCERT-aligned syllabus, mock tests and AI-powered study plans.", SITES['neetjee'][0] + "/", [("#syllabus", "Syllabus"), ("#jee", "JEE"), ("#mocks", "Mock tests"), ("#plans", "Study plans"), ("#team", "Team"), (HUB + "/", "Agentic QA home")], "Join waitlist", nj_body, "NEET", "amber"))

# ---------------- Playwright AI ----------------
pw_body = f'''<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <span class="pill"><span class="dot" aria-hidden="true"></span>Live Playwright course · next batch starts 15 Nov 2026</span>
      <h1>Become a confident <span class="grad">AI-ready Playwright automation tester.</span></h1>
      <p class="lede">A beginner-friendly, live course that takes you from your first test to a real Page Object Model framework — with AI-assisted testing and the SDET skills teams hire for.</p>
      <div class="cta-row"><a class="btn btn-primary" href="#contact">Join the waitlist</a><a class="btn btn-ghost" href="#contact">Book a free 30-minute demo class</a></div>
      <ul class="trust"><li>No prior coding needed</li><li>Live, not pre-recorded</li><li>Hands-on in every class</li></ul>
    </div>
    <dl class="facts" aria-label="Course at a glance">
      <div class="fact"><dt>Class length</dt><dd>90<small> min</small></dd></div>
      <div class="fact"><dt>Live class days</dt><dd>30</dd></div>
      <div class="fact"><dt>Capstone days</dt><dd>5</dd></div>
      <div class="fact"><dt>Next batch</dt><dd>15<small> Nov 2026</small></dd></div>
    </dl>
  </div>
  <div class="wrap"><div class="fee-strip reveal"><span>Fees are shared on a quick call — no hidden packages.</span><a class="btn btn-primary btn-sm" href="#contact">Request a call</a></div></div>
</section>
<section id="course" class="alt"><div class="wrap">
  {head("How the course works", "Short theory, lots of practice, every single class.", "Each live class is 90 minutes: 60 minutes of teaching followed by 30 minutes of guided hands-on work.")}
  <div class="format reveal" aria-label="90-minute class format"><div class="teach"><b>60 min</b>Live teaching &amp; demos</div><div class="hands"><b>30 min</b>Hands-on practice</div></div>
  <ol class="journey reveal" style="margin-top:28px">
    <li><span>Stage 1</span><h3>Foundations</h3><p>Testing basics, setup from scratch, the JavaScript / TypeScript you actually need.</p></li>
    <li><span>Stage 2</span><h3>Playwright core</h3><p>Locators, auto-waiting, assertions, fixtures, traces and debugging.</p></li>
    <li><span>Stage 3</span><h3>Framework, SDET &amp; AI</h3><p>Page Object Model, BDD, reports, CI/CD, flaky-test handling and AI-assisted testing.</p></li>
    <li class="cap"><span>+5 days</span><h3>Capstone</h3><p>Build a complete framework from an empty folder and present it.</p></li>
  </ol>
</div></section>
<section id="tutorials"><div class="wrap">
  {head("Tutorials", "Syllabus: from zero to a working framework.", "Every topic ends with common mistakes to avoid, an exercise and a short quiz.")}
  <div class="grid g3 syllabus">
    <div class="card"><h3>Foundations</h3><ol><li><b>Automation testing basics</b> — manual vs automated, setup</li><li><b>AI for testers</b> — prompting AI tools for test cases and data</li><li><b>What is Playwright</b> — browsers, locators, auto-waiting</li><li><b>JS + TS essentials</b> — just what the framework uses</li><li><b>BDD with Gherkin</b> — Given / When / Then, tags</li></ol></div>
    <div class="card"><h3>Framework craft</h3><ol><li><b>Page Object Model</b> — BasePage, fixtures</li><li><b>Framework tour</b> — every folder, end to end</li><li><b>Hard topics</b> — iframes, shadow DOM, sessions, Allure</li><li><b>AI-assisted framework coding</b> — generate and refactor with AI, review the output</li><li><b>Capstone</b> — empty folder to green suite</li></ol></div>
    <div class="card"><h3>Professional edge</h3><ol><li><b>CI &amp; debugging</b> — sharding, traces, pipelines</li><li><b>Playwright MCP &amp; AI agents</b> — an introduction</li><li><b>AI in CI/CD</b> — AI failure triage and self-healing locators</li><li><b>Interview preparation</b> — Q&amp;A practice, mock interview</li><li><b>Test strategy</b> — metrics, flaky-test policy</li></ol></div>
  </div>
</div></section>
<section id="labs" class="alt"><div class="wrap">
  {head("Hands-on labs", "Skills employers look for in an SDET.")}
  {cards([("Write reliable tests", "Resilient locators, auto-waiting and web-first assertions that do not flake."),
          ("Design with Page Objects", "A maintainable framework with the Page Object Model, fixtures and clean test data."),
          ("Debug like an SDET", "Read traces, screenshots and videos to find root causes quickly."),
          ("Run in CI/CD", "Parallel runs on GitHub Actions with HTML / Allure reports."),
          ("Test with AI", "Use AI assistants to generate test ideas, data and code — and review the output critically."),
          ("Playwright MCP", "Drive the browser from AI agents through the Playwright MCP server.")], icons=["check","layers","bug","rocket","spark","agent"])}
  <figure class="success-fig" style="margin-top:32px"><img src="/assets/img/certificate-handover.webp" alt="Internship certificate handover at Agentic QA" loading="lazy"><figcaption class="muted">Every graduate earns an industry internship certificate.</figcaption></figure>
</div></section>
<section id="instructor"><div class="wrap"><div class="instructor instructor-card reveal">
  <div class="photo-wrap"><img class="avatar" src="/assets/img/ganesh.webp" alt="Ganesan (Ganesh) Sivaraman" width="272" height="272" loading="lazy"></div>
  <div><span class="eyebrow">Your instructor</span><h2>Ganesan (Ganesh) Sivaraman</h2><p>Ganesh architects AI-native QA automation with Playwright, TypeScript, Python, RAG and MCP servers, and teaches every live class personally, with Moksha Meera teaching alongside in hands-on sessions.</p><a class="btn btn-ghost btn-sm" href="{HUB}/#about">About the team →</a></div>
</div></div></section>
<section id="faq"><div class="wrap faq" style="max-width:820px">
  <div class="section-head center"><span class="eyebrow">FAQ</span><h2>Common questions.</h2></div>
  <details><summary>Do I need coding experience?</summary><p>No. The course starts from zero and teaches the JavaScript / TypeScript you need as you go.</p></details>
  <details><summary>How long is the course?</summary><p>30 days of live classes plus 5 capstone days. Each class is 90 minutes — 60 minutes teaching and 30 minutes hands-on.</p></details>
  <details><summary>Are classes live or recorded?</summary><p>Classes are taught live by Ganesh, with hands-on practice in every session.</p></details>
  <details><summary>What laptop do I need?</summary><p>Any ordinary laptop that can run a modern browser and Node.js. No GPU required.</p></details>
  <details><summary>Will this guarantee me a job?</summary><p>No course can promise that. You will leave with a framework you built, a capstone you can demo and interview practice.</p></details>
</div></section>
''' + contact("Next batch · limited seats", "Join the waitlist for the next batch.", "Next batch starts <strong>15 Nov 2026</strong>. Fees are shared on a quick call.", "Playwright AI waitlist",
  ["Free demo class (30 min)", "Join waitlist / next batch", "A call about fees", "Other question"], ["Student / fresher", "Manual tester moving to automation", "Automation engineer / SDET", "QA lead or manager", "Company / team training"], "Join the waitlist")
write("sites/playwrightai/index.html", page("Playwright + AI — Live Playwright testing course with AI | Agentic QA", "Live, beginner-friendly Playwright test automation with AI: tutorials, hands-on labs and a capstone framework.", SITES['playwrightai'][0] + "/", [("#course", "Course"), ("#tutorials", "Tutorials"), ("#labs", "Labs"), ("#faq", "FAQ"), ("#instructor", "Instructor"), (HUB + "/", "Agentic QA home")], "Join waitlist", pw_body, "Playwright", "violet"))
print("built")
