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
      <div><h4>Sites</h4><ul><li><a href="{HUB}/">Agentic QA home</a></li><li><a href="{SITES['ai'][0]}/">AI for Business</a></li><li><a href="{SITES['aiengineering'][0]}/">AI Engineering</a></li><li><a href="{SITES['neetjee'][0]}/">NEET Prep</a></li><li><a href="{SITES['playwrightai'][0]}/">Playwright + AI</a></li></ul></div>
      <div><h4>Company</h4><ul><li><a href="{HUB}/#about">About</a></li><li><a href="{HUB}/privacy.html">Privacy</a></li></ul></div>
      <div><h4>Connect</h4><ul><li><a href="tel:+919663434422">+91 96634 34422</a></li><li><a href="https://wa.me/919663434422" rel="noopener">WhatsApp</a></li><li><a href="mailto:admin@agenticqa.io">admin@agenticqa.io</a></li><li><a href="https://www.youtube.com/@AgenticQA" rel="noopener">YouTube @AgenticQA</a></li><li><a href="https://www.linkedin.com/in/ganesan-sivaraman/" rel="noopener">LinkedIn</a></li></ul></div>
    </div>
    <p class="copy">© <span id="year">2026</span> Agentic QA Technologies LLP · LLPIN: <span style="white-space:nowrap">ACV-7177</span> · Registered in Puducherry, India</p>
  </div>
</footer>
<script src="/assets/js/site.js" defer></script>
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
    <form class="form" id="waitlist-form" action="https://formsubmit.co/ganesh@agenticqa.io" data-ajax="https://formsubmit.co/ajax/ganesh@agenticqa.io" method="POST" novalidate>
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

def cards(items, cls="g3"):
    return f'<div class="grid {cls}">' + "".join(f'<article class="card reveal"><h3>{h}</h3><p class="muted">{p}</p></article>' for h, p in items) + "</div>"

def head(eyebrow, h2, lede=""):
    l = f'<p class="lede">{lede}</p>' if lede else ""
    return f'<div class="section-head"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2>{l}</div>'

def write(rel, html):
    p = os.path.join(ROOT, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write(html)

# ---------------- HUB ----------------
hub_cards = [
 ("ai", "AI for Business", "Custom AI agents, automation consulting and AI-native QA for companies. We scope your workflows, build agents that fit your stack, and evaluate them before they reach users."),
 ("aiengineering", "AI Engineering", "The builder track: LLMs, retrieval-augmented generation, vector databases, agents and MCP, evaluation and fine-tuning — with in-house projects as working examples."),
 ("neetjee", "NEET Prep (CatalystAI)", "CatalystAI-powered NEET preparation: NCERT-aligned subject maps, mock tests and personalised study plans with doubt-solving support."),
 ("playwrightai", "Playwright + AI", "Playwright test automation with AI-assisted testing — tutorials, hands-on labs and Playwright MCP, for testers and teams moving into AI-era automation."),
]
cardhtml = '<div class="hub-cards">' + "".join(
 f'<a class="hub-card reveal" href="{SITES[k][0]}/"><span class="host">{SITES[k][0][8:]}</span><h3>{t}</h3><p>{d}</p><span class="go">Open site →</span></a>' for k, t, d in hub_cards) + "</div>"
hub_body = f'''<section class="hero" id="company">
  <div class="wrap">
    <span class="pill"><span class="dot" aria-hidden="true"></span>Agentic QA Technologies LLP</span>
    <h1>AI-native quality engineering and <span class="grad">AI agents for real-world teams.</span></h1>
    <p class="lede">Agentic QA Technologies LLP is a Bengaluru-based AI and automation engineering company. We build AI-native quality engineering solutions, custom AI agents and evaluation pipelines for companies — and run structured programmes that develop industry-ready AI and automation skills.</p>
    <div class="cta-row"><a class="btn btn-primary" href="#about">About the company</a><a class="btn btn-ghost" href="#contact">Talk to us</a></div>
  </div>
</section>
<section id="about" class="alt">
  <div class="wrap">
    {head("Who we are", "An AI and quality engineering company.", "Agentic QA Technologies LLP (LLPIN ACV-7177, registered in Puducherry, India) works where AI systems meet software quality: building, testing and evaluating AI-powered software, and helping people and teams do the same.")}
    {cards([("AI-native quality engineering", "Playwright and API automation with AI-assisted triage, CI/CD integration and test strategy for modern web products."),
            ("Custom AI agents", "Task-specific agents connected to company data and tools through APIs and MCP servers, with human checkpoints where they matter."),
            ("LLM &amp; agent evaluation", "Evaluation suites (DeepEval, Ragas, LangSmith) that measure accuracy, safety and regressions in LLM and RAG features."),
            ("Automation consulting", "Mapping manual workflows, finding high-value automation candidates and delivering a practical roadmap."),
            ("Skill programmes", "Structured, hands-on programmes in AI engineering, Playwright + AI and NEET preparation, each run on its own site."),
            ("In-house tooling", "Applied AI products built and maintained by our own team, used as reference implementations.")])}
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
  </div>
</section>
<section id="founder"><div class="wrap instructor">
    <div class="photo-wrap"><img class="avatar" src="/assets/img/ganesh.webp" alt="Ganesan (Ganesh) Sivaraman" width="272" height="272" loading="lazy"></div>
    <div>
      <span class="eyebrow">Founder</span>
      <h2>Ganesan (Ganesh) Sivaraman</h2>
      <p class="muted"><strong>AI QA Architect · MCP Servers · LLM &amp; Agent Evaluation · RAG · Playwright + AI</strong><br>Founder, Agentic QA Technologies · Bengaluru</p>
      <p>Ganesh architects AI-native QA: MCP servers, LLM and agent evaluation with DeepEval, Ragas and LangSmith, RAG systems, and Playwright + AI frameworks in TypeScript. His path runs from manual testing to Playwright automation, QA management and AI automation architecture.</p>
      <p>At Symphony Talent he led QA, built a Playwright framework that lifted automated coverage by 80%, set up CI/CD for testing and worked on SkillCheck. At Agentic QA Technologies he leads consulting and delivery and teaches the programmes personally.</p>
      <p class="muted">Open to: AI QA Architect / SDET Lead roles, MCP and AI evaluation freelance work, consulting, and corporate training.</p>
      <p class="muted" style="font-size:.95rem">MCA, Bharathidasan University · B.Sc. Mathematics, University of Madras</p>
      <div class="cta-row" style="margin-top:16px"><a class="btn btn-primary btn-sm" href="mailto:ganesh@agenticqa.io?subject=Hello%20Ganesh">✉ ganesh@agenticqa.io</a><a class="btn btn-ghost btn-sm" href="https://www.linkedin.com/in/ganesan-sivaraman/" rel="noopener">LinkedIn profile</a><a class="btn btn-ghost btn-sm" href="https://www.youtube.com/@AgenticQA" rel="noopener">▶ YouTube @AgenticQA</a></div>
    </div>
</div></section>
<section id="cofounder" class="alt"><div class="wrap instructor">
    <div class="photo-wrap"><img class="avatar" src="/assets/img/moksha.webp" alt="Moksha Meera" width="272" height="272" loading="lazy"></div>
    <div>
      <span class="eyebrow">Co-founder, Director &amp; Tech Lead</span>
      <h2>Moksha Meera</h2>
      <p class="muted"><strong>Co-founder &amp; Director · Tech Lead · LLM Engineer · AI &amp; Automation Engineering</strong><br>Agentic QA Technologies · Bengaluru</p>
      <p>Moksha is a co-founder and director of Agentic QA Technologies alongside Ganesh, and works full-time in the company. She leads the technical side, building the in-house projects and tooling, and teaches alongside Ganesh in hands-on sessions.</p>
      <p class="muted" style="font-size:.95rem">M.Sc. Computer Science, Pondicherry University · B.Sc. Computer Science, Pondicherry University</p>
    </div>
</div></section>
<section id="certificates"><div class="wrap">
  {head("Certificates", "Industry Internship Completion Certificate.", "Graduates of our programmes receive an Industry Internship Completion Certificate from Agentic QA Technologies. It records that the learner completed the programme's hands-on work and capstone project under our team's guidance. It is issued by the company itself, not by an external accreditation body.")}
  <figure class="success-fig"><img src="/assets/img/certificate-handover.webp" alt="Sivanesan P receiving his Industry Internship Completion Certificate from Ganesan Sivaraman" loading="lazy"><figcaption class="muted">Sivanesan P receiving his Industry Internship Completion Certificate from Ganesan Sivaraman.</figcaption></figure>
</div></section>
<section id="activities" class="alt">
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
write("hub/privacy.html", page("Privacy Policy | Agentic QA Technologies", "Privacy policy for agenticqa.io and its subdomains.", HUB + "/privacy.html", [("./", "Home"), ("./#activities", "Activities")], "Contact", pmain + contact("Questions", "Privacy questions?", "Email us for any data request.", "Privacy request", ["Data request", "Other"], ["Individual", "Company"], "Send")))

# ---------------- AI (business) ----------------
ai_body = f'''<section class="hero"><div class="wrap">
  <span class="pill"><span class="dot" aria-hidden="true"></span>AI for Business · ai.agenticqa.io</span>
  <h1>Custom AI agents that <span class="grad">do real work for your team.</span></h1>
  <p class="lede">We design, build and hand over AI agents and automations that fit your existing tools — from support triage to QA pipelines — with evaluation and guardrails built in from day one.</p>
  <div class="cta-row"><a class="btn btn-primary" href="#contact">Book a discovery call</a><a class="btn btn-ghost" href="#services">See services</a></div>
</div></section>
<section id="services" class="alt"><div class="wrap">
  {head("Services", "What we build for companies.")}
  {cards([("Custom AI agents", "Task-specific agents connected to your data and tools via APIs and MCP servers — with human-in-the-loop checkpoints where it matters."),
          ("Automation consulting", "We map your manual workflows, find the high-value automation candidates and give you a practical roadmap."),
          ("AI-native QA", "Playwright and API test automation with AI-assisted triage, self-healing locators and CI/CD integration."),
          ("LLM & agent evaluation", "Test suites that measure accuracy, safety and regressions in your LLM features before they reach users."),
          ("RAG over your documents", "Retrieval-augmented assistants that answer from your own knowledge base, with sources shown."),
          ("Team enablement", "Hands-on workshops so your engineers can maintain and extend what we build.")])}
</div></section>
<section id="process"><div class="wrap">
  {head("How we work", "From first call to production.")}
  <ol class="journey reveal">
    <li><span>Step 1</span><h3>Discovery call</h3><p>We understand your goals, systems and constraints.</p></li>
    <li><span>Step 2</span><h3>Scoping</h3><p>A written proposal with deliverables, timeline and success measures.</p></li>
    <li><span>Step 3</span><h3>Build &amp; evaluate</h3><p>Iterative delivery with demos and an evaluation suite.</p></li>
    <li class="cap"><span>Step 4</span><h3>Handover</h3><p>Documentation, training and optional ongoing support.</p></li>
  </ol>
</div></section>
<section id="pricing" class="alt"><div class="wrap">
  {head("Pricing", "Every engagement is scoped to you.", "We do not publish fixed packages. Fees depend on scope and are discussed on a call after we understand your needs.")}
  <div class="cta-row"><a class="btn btn-primary" href="#contact">Request a pricing call</a></div>
</div></section>
''' + contact("Enquiries", "Tell us what you want to automate.", "Share a short description of your workflow and we will set up a call. Fees are discussed on the call.", "AI for Business enquiry",
  ["Custom AI agent", "Automation consulting", "AI-native QA", "LLM evaluation", "Pricing call", "Other"], ["Founder / leadership", "Engineering lead", "Product / operations", "Other"], "Request a call")
write("sites/ai/index.html", page("AI for Business — Custom AI agents & automation consulting | Agentic QA", "Custom AI agents, automation consulting and AI-native QA for companies. Fees discussed on a call.", SITES['ai'][0] + "/", [("#services", "Services"), ("#process", "Process"), ("#pricing", "Pricing"), (HUB + "/", "Agentic QA home")], "Book a call", ai_body, "Business", "signal"))

# ---------------- AI Engineering ----------------
ae_body = f'''<section class="hero"><div class="wrap">
  <span class="pill"><span class="dot" aria-hidden="true"></span>AI Engineering · aiengineering.agenticqa.io</span>
  <h1>Build real systems with <span class="grad">LLMs, RAG and vector databases.</span></h1>
  <p class="lede">A hands-on AI engineering track for developers and testers: from your first LLM call to evaluated, production-style RAG applications and fine-tuned models.</p>
  <div class="cta-row"><a class="btn btn-primary" href="#contact">Join the waitlist</a><a class="btn btn-ghost" href="#curriculum">See the curriculum</a></div>
</div></section>
<section id="curriculum" class="alt"><div class="wrap">
  {head("Curriculum", "What you will learn.")}
  {cards([("Building with LLMs", "Prompt design, structured output, tool calling and streaming with modern LLM APIs."),
          ("Retrieval-augmented generation", "Chunking, embeddings, retrieval strategies, reranking and citing sources."),
          ("Vector databases", "Index design and querying with ChromaDB and other vector stores; trade-offs at scale."),
          ("Agents & MCP", "Multi-step agents, MCP server development and safe tool use."),
          ("Evaluation", "LLM and agent evaluation: test sets, metrics, regression checks and red-teaming basics."),
          ("Fine-tuning", "When to fine-tune vs. prompt vs. RAG; dataset preparation and parameter-efficient fine-tuning.")])}
</div></section>
<section id="projects"><div class="wrap">
  {head("Projects", "Real AI projects, not toy demos.", "Learners work on in-house projects like these.")}
  <div class="grid g2">
    <article class="card project reveal"><img src="/assets/img/ResumeGenieAI.webp" alt="ResumeGenie AI dashboard" width="1200" height="657" loading="lazy"><div class="body"><span class="tag">RAG · LLM</span><h3>ResumeGenie AI</h3><p>Resume analysis and improvement suggestions powered by LLM feedback.</p></div></article>
    <article class="card project reveal"><img src="/assets/img/StudyMateAI.webp" alt="StudyMate AI interface" width="1200" height="653" loading="lazy"><div class="body"><span class="tag">RAG · ChromaDB</span><h3>StudyMate AI</h3><p>Ask questions over large PDFs with a retrieval-augmented study assistant.</p></div></article>
    <article class="card project reveal"><img src="/assets/img/FeedBack_Pulse.webp" alt="FeedbackPulse sentiment dashboard" width="1200" height="664" loading="lazy"><div class="body"><span class="tag">NLP · Sentiment</span><h3>FeedbackPulse AI</h3><p>Batch sentiment analysis of customer reviews for product teams.</p></div></article>
    <article class="card project reveal"><img src="/assets/img/MeetingMind_AI_.webp" alt="MeetingMind AI screen" width="1200" height="657" loading="lazy"><div class="body"><span class="tag">LLM · Summaries</span><h3>MeetingMind AI</h3><p>AI meeting assistant project.</p></div></article>
  </div>
</div></section>
<section id="format" class="alt"><div class="wrap">
  {head("Format", "Live, hands-on, project-driven.")}
  <ul class="checklist"><li>Live classes with guided hands-on practice in every session</li><li>Taught by Ganesh and Moksha</li><li>Portfolio-ready projects on GitHub</li><li>Fees and batch dates shared on a quick call</li></ul>
</div></section>
''' + contact("Next batch", "Join the AI Engineering waitlist.", "We will email batch dates and an invite to a demo session. Fees are shared on a call.", "AI Engineering waitlist",
  ["Join the waitlist", "Free demo session", "Team / corporate training", "Other"], ["Developer", "Tester / SDET", "Student / fresher", "Company / team"], "Join the waitlist")
write("sites/aiengineering/index.html", page("AI Engineering — LLMs, RAG, vector databases & fine-tuning | Agentic QA", "Hands-on AI engineering training: LLMs, RAG, vector databases, agents, evaluation and fine-tuning.", SITES['aiengineering'][0] + "/", [("#curriculum", "Curriculum"), ("#projects", "Projects"), ("#format", "Format"), (HUB + "/", "Agentic QA home")], "Join waitlist", ae_body, "Engineering", "mint"))

# ---------------- NEET ----------------
nj_body = f'''<section class="hero"><div class="wrap">
  <span class="pill"><span class="dot" aria-hidden="true"></span>CatalystAI · neetjee.agenticqa.io</span>
  <h1>NEET preparation with <span class="grad">a plan that adapts to you.</span></h1>
  <p class="lede">CatalystAI from Agentic QA Technologies combines AI-powered study plans, visual explanations and doubt-solving for NEET aspirants — NCERT-aligned and focused on your weak areas.</p>
  <div class="cta-row"><a class="btn btn-primary" href="#contact">Join the waitlist</a><a class="btn btn-ghost" href="#syllabus">See the syllabus</a></div>
</div></section>
<section id="syllabus" class="alt"><div class="wrap">
  {head("Syllabus", "NCERT-aligned coverage of all three subjects.")}
  {cards([("Biology", "Diversity of living organisms, cell biology, plant and human physiology, genetics and evolution, ecology."),
          ("Chemistry", "Physical, organic and inorganic chemistry with concept maps and reaction practice."),
          ("Physics", "Mechanics, thermodynamics, electrostatics, optics and modern physics with step-by-step problem solving.")])}
</div></section>
<section id="mocks"><div class="wrap">
  {head("Mock tests", "Practise under exam conditions.")}
  {cards([("Chapter tests", "Short tests after each chapter to lock in concepts."), ("Full-length mocks", "Timed mocks in the NEET pattern with detailed solutions."), ("Weak-area analysis", "AI highlights topics to revisit based on your answers.")])}
</div></section>
<section id="plans" class="alt"><div class="wrap">
  {head("Study plans", "Small steps every day.")}
  <ul class="checklist"><li>Personalised daily and weekly study plans</li><li>Smart flashcards and spaced revision</li><li>Doubt-solving and follow-ups from our student support team</li><li>Progress check-ins you can share with parents</li></ul>
  <blockquote class="quote-banner">&ldquo;Small steps every day add up to big results on exam day.&rdquo;</blockquote>
</div></section>
<section id="team"><div class="wrap">
  {head("Team", "The people behind CatalystAI.")}
  <div class="card" style="display:flex;gap:20px;align-items:center;flex-wrap:wrap">
    <img src="/assets/img/tanushka-grey.webp" alt="Thanushka Mira" width="96" height="96" loading="lazy" style="width:96px;height:96px;border-radius:50%;object-fit:cover">
    <div style="flex:1;min-width:240px"><span class="eyebrow">Student support</span><h3 style="margin:4px 0">Thanushka Mira</h3><p class="muted" style="margin:0">Thanushka Mira looks after student support for CatalystAI, helping NEET learners with study planning, practice sets and day-to-day doubt follow-ups.</p></div>
  </div>
  <div class="card" style="margin-top:24px;display:flex;gap:20px;align-items:center;flex-wrap:wrap">
    <img src="/assets/img/heri.webp" alt="Hari Krishna G" width="96" height="96" loading="lazy" style="width:96px;height:96px;border-radius:50%;object-fit:cover">
    <div style="flex:1;min-width:240px"><span class="eyebrow">Campus ambassador</span><h3 style="margin:4px 0">Hari Krishna G</h3><p class="muted" style="margin:0">Hari Krishna G supports the CatalystAI community as campus ambassador, sharing study resources and helping with event sign-ups.</p></div>
  </div>
</div></section>
''' + contact("CatalystAI", "Join the NEET Prep waitlist.", "We will share programme details and next steps. Fees are shared on a call.", "CatalystAI NEET enquiry",
  ["Join the waitlist", "Mock tests", "Study plan", "Other"], ["Student", "Parent", "School / coaching centre"], "Join the waitlist")
write("sites/neetjee/index.html", page("NEET Prep — CatalystAI syllabus, mock tests & study plans | Agentic QA", "CatalystAI NEET preparation: NCERT-aligned syllabus, mock tests and AI-powered study plans.", SITES['neetjee'][0] + "/", [("#syllabus", "Syllabus"), ("#mocks", "Mock tests"), ("#plans", "Study plans"), ("#team", "Team"), (HUB + "/", "Agentic QA home")], "Join waitlist", nj_body, "NEET", "amber"))

# ---------------- Playwright AI ----------------
pw_body = f'''<section class="hero">
  <div class="wrap hero-grid">
    <div>
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
      <p class="fee-note">Fees are shared on a quick call. <a href="#contact">Request a call →</a></p>
    </dl>
  </div>
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
          ("Playwright MCP", "Drive the browser from AI agents through the Playwright MCP server.")])}
  <figure class="success-fig" style="margin-top:32px"><img src="/assets/img/certificate-handover.webp" alt="Internship certificate handover at Agentic QA" loading="lazy"><figcaption class="muted">Every graduate earns an industry internship certificate.</figcaption></figure>
</div></section>
<section id="instructor"><div class="wrap instructor">
  <div class="photo-wrap"><img class="avatar" src="/assets/img/ganesh.webp" alt="Ganesan (Ganesh) Sivaraman" width="272" height="272" loading="lazy"></div>
  <div><span class="eyebrow">Your instructor</span><h2>Ganesan (Ganesh) Sivaraman</h2><p>Ganesh architects AI-native QA automation with Playwright, TypeScript, Python, RAG and MCP servers, and teaches every live class personally, with Moksha Meera teaching alongside in hands-on sessions.</p><a class="btn btn-ghost btn-sm" href="{HUB}/#about">About the team →</a></div>
</div></section>
<section id="faq"><div class="wrap" style="max-width:820px">
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
