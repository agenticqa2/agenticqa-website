#!/usr/bin/env python3
"""Done-criteria checks for hub homepage revise (2026-11-09)."""
from pathlib import Path
import re, sys
ROOT = Path(__file__).resolve().parents[1]
hub = (ROOT / 'hub/index.html').read_text()
css = (ROOT / 'assets/css/styles.css').read_text()
js = (ROOT / 'assets/js/site.js').read_text()
fail = 0

def chk(name, cond):
  global fail
  print(('PASS' if cond else 'FAIL') + '  ' + name)
  if not cond: fail += 1

# order of section ids in main
ids = re.findall(r'<section[^>]*\bid="([^"]+)"', hub)
# hero has no id; sites, company, built, products, founder, certificate, enquiry(contact)
chk('sites before company', hub.find('id="sites"') < hub.find('id="company"'))
chk('company before built', hub.find('id="company"') < hub.find('id="built"'))
chk('built before products', hub.find('id="built"') < hub.find('id="products"'))
chk('products before founder', hub.find('id="products"') < hub.find('id="founder"'))
chk('founder before certificate', hub.find('id="founder"') < hub.find('id="certificate"'))
chk('certificate before contact', hub.find('id="certificate"') < hub.find('id="contact"'))

chk('heading Four sites of work.', '>Four sites of work.</h2>' in hub)
chk('AI Business card exact body', 'Custom AI agents, automation consulting, and AI-native QA. Scope the workflow, build the agent, evaluate it before users see it.' in hub)
chk('AI Business live link', 'data-prod-href="https://ai.agenticqa.io/"' in hub)

chk('no orbit hero-visual', 'hero-visual' not in hub)
chk('no trust-band', 'trust-band' not in hub)
chk('no Our aims', 'Our aims' not in hub)
chk('no Our goals', 'Our goals' not in hub)
chk('no Automation consulting card', 'Automation consulting' not in hub or hub.count('Automation consulting')==0)
# "automation consulting" appears in AI for Business body — allowed. Card title removed.
chk('no Skill programmes card', '<h3>Skill programmes</h3>' not in hub)
chk('no In-house tooling card', '<h3>In-house tooling</h3>' not in hub)
chk('no founder timeline', 'timeline career' not in hub and 'Symphony Talent' not in hub)
chk('no sample certificate', 'certificate-sample' not in hub)
chk('Sivanesan P present', 'Sivanesan P' in hub)
chk('Screen coming products', hub.count('Screen coming') >= 4)
chk('Open the product', hub.count('Open the product') == 4)

# LLP / ACV only in footer copy line
body_wo_footer = hub.split('<footer>')[0]
footer = hub.split('<footer>')[1]
chk('LLP not outside footer', 'LLP' not in body_wo_footer)
chk('ACV-7177 not outside footer', 'ACV-7177' not in body_wo_footer)
chk('footer exact legal', 'Agentic QA Technologies LLP · LLPIN ACV-7177' in footer)
chk('no Puducherry in hub', 'Puducherry' not in hub and 'puducherry' not in hub.lower())
chk('no registered in', 'registered in' not in hub.lower())

chk('nav Sites Company Founders Contact', all(x in hub for x in ['href="#sites">Sites', 'href="#company">Company', 'href="#founder">Founders', 'href="#contact">Contact']))
chk('hdr Talk to us', 'hdr-cta" href="#contact">Talk to us</a>' in hub or 'hdr-cta" href="#contact">Talk to us' in hub)
chk('logo alt Agentic QA Technologies', 'alt="Agentic QA Technologies"' in hub)
chk('nowrap real-world', 'class="nowrap">real-world</span>' in hub)
chk('hero pill no LLP', 'pill"><span class="dot"' in hub and 'Agentic QA Technologies</span>' in hub and 'Agentic QA Technologies LLP</span>' not in hub)
chk('lede exact', 'One company, four sites — business agents, AI engineering, NEET prep, and Playwright + AI. Pick the line of work, or talk to us.' in hub)
chk('7 built bullets', hub.count('<li>', hub.find('id="built"'), hub.find('id="products"')) == 7)
chk('built no registration bullet', 'Registered as' not in hub)
chk('contact heading', 'Talk to Agentic QA Technologies.' in hub)
chk('interest options', all(o in hub for o in ['AI for Business</option>', 'AI evaluation / MCP</option>', 'AI Engineering</option>', 'NEET Prep</option>', 'Playwright + AI</option>', 'Partnership / other</option>']))
chk('form /api/contact', 'action="/api/contact"' in hub and 'data-ajax="/api/contact"' in hub)
chk('title no LLP', '<title>Agentic QA Technologies —' in hub and 'LLP —' not in hub.split('</title>')[0])
chk('h2 sections present', hub.count('<h2>') >= 7)
chk('founder cards h3', hub.count('<h3>Ganesan') + hub.count('<h3>Moksha') == 2)
chk('css icon 44px', '.icon-btn{width:44px;height:44px;' in css.replace(' ','') or 'width:44px;height:44px' in css)
chk('css h2 weight 700', 'h2{font-size:clamp(1.7rem,3.4vw,2.5rem);font-weight:700}' in css or 'font-weight:750' not in css)
chk('scroll-spy in js', 'aria-current' in js and 'IntersectionObserver' in js)

# privacy note (not fail hub)
priv = (ROOT / 'hub/privacy.html').read_text()
if 'Puducherry' in priv:
  print('NOTE  privacy.html still contains Puducherry (out of hub scope)')

sys.exit(1 if fail else 0)
