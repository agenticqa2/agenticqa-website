#!/usr/bin/env python3
"""Extended static QA — forms, footer, a11y, CSS, routing, JS risk, approved copy."""
import re, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
PAGES = [
  'hub/index.html','hub/privacy.html',
  'sites/ai/index.html','sites/aiengineering/index.html',
  'sites/neetjee/index.html','sites/playwrightai/index.html'
]
FORM_PAGES = [p for p in PAGES if p != 'hub/privacy.html']
PASS = FAIL = 0

def ok(msg):
  global PASS; print(f'PASS  {msg}'); PASS += 1
def bad(msg):
  global FAIL; print(f'FAIL  {msg}'); FAIL += 1
def chk(msg, cond):
  (ok if cond else bad)(msg)

href_re = re.compile(r'(?<![\w-])href="([^"]*)"')
EXPECT = {
  'https://agenticqa.io/', '/?site=ai', '/?site=aiengineering', '/?site=neetjee',
  '/?site=playwrightai', 'https://agenticqa.io/#about', 'https://agenticqa.io/privacy.html',
  'tel:+919663434422', 'https://wa.me/919663434422', 'mailto:admin@agenticqa.io',
  'https://www.youtube.com/@AgenticQA', 'https://www.linkedin.com/in/ganesan-sivaraman/',
}

inventory_cells = 0
href_attrs = 0
for p in PAGES:
  foot = re.search(r'<footer\b[^>]*>(.*?)</footer>', (ROOT/p).read_text(), re.S|re.I).group(1)
  hrefs = href_re.findall(foot)
  chk(f'footer destinations exact set on {p}', set(hrefs) == EXPECT)
  # 12 unique destinations present on this page → 12 inventory cells
  inventory_cells += len(set(hrefs) & EXPECT)
  href_attrs += len(hrefs)
  chk(f'footer brand-foot on {p}', 'brand-foot' in foot)
  chk(f'footer 13 href attrs on {p} (brand + 12 dest)', len(hrefs) == 13)
chk('footer 72 inventory cells (12 dest × 6 pages)', inventory_cells == 72)
chk('footer 78 raw href attrs (brand duplicates home)', href_attrs == 78)

chk('privacy has zero forms', '<form' not in (ROOT/'hub/privacy.html').read_text())

for p in FORM_PAGES:
  f = re.search(r'<form\b[^>]*>.*?</form>', (ROOT/p).read_text(), re.S).group(0)
  ok_form = (
    'formsubmit.co/admin@agenticqa.io' in f and
    'formsubmit.co/ajax/admin@agenticqa.io' in f and
    'name="_honey"' in f and
    'form-status' in f and
    'novalidate' in f and
    bool(re.search(r'name="name"[^>]*\brequired\b|\brequired\b[^>]*name="name"', f)) and
    bool(re.search(r'type="email"[^>]*\brequired\b|\brequired\b[^>]*type="email"', f)) and
    all(f'for="{fid}"' in f and f'id="{fid}"' in f for fid in ['f-name','f-email','f-interest','f-profile','f-msg'])
  )
  chk(f'form semantics {p}', ok_form)

js = (ROOT/'assets/js/site.js').read_text()
chk('site.js checkValidity+reportValidity+ok/err', all(s in js for s in ['checkValidity','reportValidity','form-status ok','form-status err']))
chk('site.js mailto fallback admin@', 'mailto:admin@agenticqa.io?subject=' in js and 'mailto:ganesh@agenticqa.io?subject=' not in js)
chk('site.js no eval/innerHTML/document.write/console', not re.search(r'eval\(|\.innerHTML|document\.write|\bconsole\.', js))
chk('site.js prod-href preview skip', 'isPreview' in js and 'data-prod-href' in js)

cans = {
  'hub/index.html': 'https://agenticqa.io/',
  'hub/privacy.html': 'https://agenticqa.io/privacy.html',
  'sites/ai/index.html': 'https://ai.agenticqa.io/',
  'sites/aiengineering/index.html': 'https://aiengineering.agenticqa.io/',
  'sites/neetjee/index.html': 'https://neetjee.agenticqa.io/',
  'sites/playwrightai/index.html': 'https://playwrightai.agenticqa.io/',
}
for p, u in cans.items():
  h = (ROOT/p).read_text()
  chk(f'canonical {p}', f'rel="canonical" href="{u}"' in h)

mw = (ROOT/'middleware.js').read_text()
for s in ["'agenticqa.io': '/hub'","'www.agenticqa.io': '/hub'","'ai.agenticqa.io': '/sites/ai'",
          "'aiengineering.agenticqa.io': '/sites/aiengineering'","'neetjee.agenticqa.io': '/sites/neetjee'",
          "'playwrightai.agenticqa.io': '/sites/playwrightai'"]:
  chk(f'HOST_MAP {s}', s in mw)

sm = (ROOT/'sitemap.xml').read_text()
for u in ['https://agenticqa.io/</loc>','privacy.html','ai.agenticqa.io','aiengineering.agenticqa.io','neetjee.agenticqa.io','playwrightai.agenticqa.io']:
  chk(f'sitemap has {u}', u in sm)

for p in PAGES:
  h = (ROOT/p).read_text()
  chk(f'a11y semantic {p}',
      bool(re.search(r'<html[^>]+lang=', h)) and 'name="viewport"' in h and '<main' in h and h.count('<h1')==1
      and 'class="skip"' in h and 'nav-toggle' in h and 'aria-expanded' in h)

css = (ROOT/'assets/css/styles.css').read_text()
chk('CSS responsive+a11y hooks', all(s in css for s in [
  'max-width:980px','max-width:820px','max-width:600px',':focus-visible','prefers-reduced-motion','.hp{','form-status.ok']))

hub = (ROOT/'hub/index.html').read_text()
ai = (ROOT/'sites/ai/index.html').read_text()
chk('approved copy hub automation consulting', 'Identify high-value automation opportunities, define API and MCP integration requirements, and create a delivery roadmap covering implementation, evaluation and CI/CD.' in hub)
chk('approved copy hub in-house tooling', 'Explore working AI applications built by our team, demonstrating RAG, structured LLM feedback, sentiment analysis and meeting summarisation.' in hub)
chk('approved copy Moksha delivery bio', "Moksha leads technical delivery for the company's in-house AI projects and automation tooling" in hub)
chk('approved copy ai DeepEval evaluation', 'Build evaluation suites using DeepEval, Ragas and LangSmith to assess response quality, retrieval performance and regressions in LLM and RAG applications.' in ai)
chk('approved copy ai Team enablement', 'Train your engineers to maintain delivered agents, configure MCP integrations, run evaluations and extend Playwright and API test suites.' in ai)

print(f'== EXTENDED RESULT: {PASS} pass, {FAIL} fail')
sys.exit(0 if FAIL == 0 else 1)
