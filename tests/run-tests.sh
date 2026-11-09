#!/usr/bin/env bash
# Structural, link, content and smoke tests for hub-split. Run from repo root: bash tests/run-tests.sh
cd "$(dirname "$0")/.."; PASS=0; FAIL=0
ok(){ echo "PASS  $1"; PASS=$((PASS+1)); }; bad(){ echo "FAIL  $1"; FAIL=$((FAIL+1)); }
chk(){ if eval "$2" >/dev/null 2>&1; then ok "$1"; else bad "$1"; fi; }
PAGES="hub/index.html hub/privacy.html sites/ai/index.html sites/aiengineering/index.html sites/neetjee/index.html sites/playwrightai/index.html"
echo "== 1. Structure"
for f in $PAGES index.html middleware.js vercel.json package.json VERSIONS.md assets/css/styles.css assets/js/site.js assets/img/ganesh.webp assets/img/moksha.webp assets/brand/logo.svg; do chk "exists $f" "[ -s $f ]"; done
chk "site indexes are distinct" "[ \$(md5sum hub/index.html sites/*/index.html | awk '{print \$1}' | sort -u | wc -l) -eq 5 ]"
# middleware host mapping via node with stubbed @vercel/functions
mkdir -p /tmp/mwtest/node_modules/@vercel/functions
echo '{"name":"@vercel/functions","type":"module","main":"i.js"}' > /tmp/mwtest/node_modules/@vercel/functions/package.json
echo 'export const rewrite=u=>({rewrite:String(u)});export const next=()=>({next:true});' > /tmp/mwtest/node_modules/@vercel/functions/i.js
cp middleware.js /tmp/mwtest/middleware.mjs
cat > /tmp/mwtest/t.mjs <<'JS'
import mw from './middleware.mjs';
const cases=[["agenticqa.io","/","/hub/index.html"],["www.agenticqa.io","/privacy.html","/hub/privacy.html"],["ai.agenticqa.io","/","/sites/ai/index.html"],
["aiengineering.agenticqa.io","/","/sites/aiengineering/index.html"],["neetjee.agenticqa.io","/","/sites/neetjee/index.html"],["playwrightai.agenticqa.io","/","/sites/playwrightai/index.html"],
["localhost:3000","/","/hub/index.html"],["localhost:3000","/?site=neetjee","/sites/neetjee/index.html"],["x-git-hub.vercel.app","/?site=ai","/sites/ai/index.html"],
["agenticqa.io","/?site=ai","/sites/ai/index.html"],["ai.agenticqa.io","/?site=playwrightai","/sites/playwrightai/index.html"],["preview.vercel.app","/","/hub/index.html"]];
let f=0;for(const[h,p,exp]of cases){const r=mw({url:"https://"+h+p,headers:new Map([["host",h]])});const got=r.rewrite&&new URL(r.rewrite).pathname;
console.log((got===exp?"PASS":"FAIL")+"  middleware "+h+p+" -> "+got);if(got!==exp)f++}
const a=mw({url:"https://ai.agenticqa.io/assets/css/styles.css",headers:new Map([["host","ai.agenticqa.io"]])});console.log((a.next?"PASS":"FAIL")+"  middleware passes /assets/ through");if(!a.next)f++;
const api=mw({url:"https://www.agenticqa.io/api/contact",headers:new Map([["host","www.agenticqa.io"]])});console.log((api.next?"PASS":"FAIL")+"  middleware passes /api/ through");if(!api.next)f++;
process.exit(f?1:0);
JS
if out=$(cd /tmp/mwtest && node t.mjs); then echo "$out"; n=$(printf '%s\n' "$out" | grep -c '^PASS' || true); PASS=$((PASS+n)); else echo "$out"; n=$(printf '%s\n' "$out" | grep -c '^PASS' || true); f=$(printf '%s\n' "$out" | grep -c '^FAIL' || true); PASS=$((PASS+n)); FAIL=$((FAIL+f)); fi
for s in ai aiengineering neetjee playwrightai; do
  chk "hub card preview link /?site=$s" "grep -q 'class=\"hub-card reveal\" href=\"/?site=$s\" data-prod-href=\"https://$s.agenticqa.io/\"' hub/index.html"
done
chk "hub nav Contact label is Talk to Us" "grep -q 'href=\"#contact\">Talk to Us</a>' hub/index.html && ! grep -q 'site-nav[^>]*>.*href=\"#contact\">Contact</a>' hub/index.html"
chk "hub header CTA still Contact" "grep -q 'hdr-cta\" href=\"#contact\">Contact</a>' hub/index.html"
chk "site.js has nav scroll-spy" "grep -q 'Nav scroll-spy' assets/js/site.js && grep -q 'aria-current' assets/js/site.js"
chk "css highlights aria-current nav" "grep -q 'site-nav a\[aria-current="true"\]' assets/css/styles.css"

echo "== 2. Link check (local href/src)"
broken=0
for f in $PAGES; do
  for u in $(grep -o '\(href\|src\)="[^"#]*' $f | sed 's/^[a-z]*="//' | grep -v '^https\?:\|^mailto:\|^tel:\|^$'); do
    # Middleware preview routes (/?site=ai) are not filesystem paths — skip them
    case $u in '/?site='*) continue;; esac
    # strip query/hash for filesystem check (e.g. site.js?v=…)
    ufile="${u%%\?*}"; ufile="${ufile%%#*}"
    case $ufile in /*) t=".${ufile}";; *) t="$(dirname $f)/$ufile";; esac
    [ -d "$t" ] && t="$t/index.html"
    [ -e "$t" ] || { echo "   broken: $f -> $u"; broken=1; }
  done
done
chk "no broken local href/src" "[ $broken -eq 0 ]"
echo "== 3. Content audit"
chk "no prices/fees amounts (₹, Rs, INR, \$ amounts)" "! grep -nE '₹|Rs\.? ?[0-9]|INR|\\\$[0-9]|[0-9],[0-9]{3} ?/-' $PAGES"
chk "no age/grade/class-N mentions" "! grep -niE '\\b(age[ds]?|years? old|grade|class (1[0-2]|[6-9])|std\\.? ?[0-9])\\b' $PAGES"
chk "no years-of-experience claims" "! grep -niE '[0-9]+\\+? years|years of experience' $PAGES"
chk "no YouTube iframe/embed" "! grep -niE '<iframe|youtube.com/embed' $PAGES"
chk "no testimonials / student counts" "! grep -niE 'testimonial|[0-9]+\\+? (students|learners)' $PAGES"
chk "no PAN/TAN/street address" "! grep -nE '\\bPAN\\b|\\bTAN\\b|[A-Z]{5}[0-9]{4}[A-Z]|Street|Road|Nagar' $PAGES"
chk "no payment QR on new sites" "! grep -n 'qr-payment' $PAGES"
for f in $PAGES; do chk "LLPIN ACV-7177 + JS year in $f" "grep -q 'LLPIN: <span[^>]*>ACV-7177' $f && grep -q 'id=\"year\"' $f && grep -q '/assets/js/site.js' $f"; done
for f in $PAGES; do chk "a11y (skip link, theme toggle, all img alt) $f" "grep -q 'class=\"skip\"' $f && grep -q theme-toggle $f && ! grep -o '<img[^>]*>' $f | grep -v 'alt='"; done
chk "ganesh open-to replaced with organisations line" "grep -q 'Works with organisations on AI quality engineering, MCP integrations, AI evaluation and corporate training.' hub/index.html && ! grep -q 'Open to:' hub/index.html"
chk "ganesh career timeline roles" "grep -q 'AI Automation Architect' hub/index.html && grep -q 'Symphony Talent' hub/index.html && grep -q 'Harman Connected Services' hub/index.html && grep -q 'First Advantage' hub/index.html"
chk "moksha career timeline roles" "grep -q 'ePy-Tallent Tech solution' hub/index.html && grep -q 'Automation Engineer' hub/index.html && grep -q 'Co-founder, Director' hub/index.html"
chk "founder career timelines present" "grep -c 'class=\"timeline career\"' hub/index.html | grep -q '^2$'"
chk "email/phone/YouTube present on hub" "grep -q ganesh@agenticqa.io hub/index.html && grep -q '+91 96634 34422' hub/index.html && grep -q '@AgenticQA' hub/index.html"
chk "admin@agenticqa.io in footer of every page" "for f in $PAGES; do grep -q 'mailto:admin@agenticqa.io\">admin@agenticqa.io' \$f || exit 1; done"
chk "ganesh@ only in hub founder section" "grep -q 'mailto:ganesh@agenticqa.io?subject=Hello' hub/index.html && [ \$(grep -l 'mailto:ganesh@' sites/*/index.html | wc -l) -eq 0 ]"
echo "== 3a. Hub language ban + order"
chk "hub visible text has no course/syllabus/enrol/waitlist/batch/beginner/become a confident" "! sed 's/<[^>]*>/ /g' hub/index.html | grep -niE 'course|syllabus|enrol|waitlist|batch|beginner|become a confident'"
chk "hub section order company>founder>cofounder>certificates>activities" "python3 -c \"import re,sys;s=open('hub/index.html').read();i=[s.index('id=\\\"'+k+'\\\"') for k in ['company','about','founder','cofounder','certificates','activities']];sys.exit(0 if i==sorted(i) else 1)\""
for a in "hub/index.html neural" "sites/ai/index.html signal" "sites/aiengineering/index.html mint" "sites/neetjee/index.html amber" "sites/playwrightai/index.html violet"; do set -- $a; chk "accent $2 on $1" "grep -q 'data-accent=\"$2\"' $1"; done
chk "no neatjee misspelling" "! grep -rni neatjee hub sites tools middleware.js"

echo "== 3b. Subdomain content boundaries"
# ai = business only (no course/waitlist/batch/beginner/become a confident)
chk "ai has no course/syllabus/enrol/waitlist/batch/beginner/become a confident" "! sed 's/<[^>]*>/ /g' sites/ai/index.html | grep -niE 'course|syllabus|enrol|waitlist|batch|beginner|become a confident'"
chk "hub privacy has no waitlist form/section" "! grep -qE 'id=\"waitlist\"|id=\"waitlist-form\"|waitlist-form' hub/privacy.html"
chk "hub privacy Contact CTA points to hub contact" "grep -q 'hdr-cta\" href=\"https://agenticqa.io/#contact\"' hub/privacy.html || grep -q 'hdr-cta\" href=\"/#contact\"' hub/privacy.html"
chk "ai has no enquiry waitlist-form id" "! grep -q 'id=\"waitlist' sites/ai/index.html"
chk "ai uses enquiry-form" "grep -q 'id=\"enquiry-form\"' sites/ai/index.html"
chk "ai h1 is business agents" "grep -q 'Custom AI agents that' sites/ai/index.html"
# playwrightai exclusive course home
chk "playwrightai has become a confident" "grep -q 'Become a confident' sites/playwrightai/index.html"
chk "playwrightai exclusive vs ai" "! cmp -s sites/ai/index.html sites/playwrightai/index.html"
# aiengineering not a copy of playwright course
chk "aiengineering has no become a confident" "! grep -qi 'become a confident' sites/aiengineering/index.html"
chk "aiengineering h1 LLMs/RAG" "grep -q 'LLMs, RAG' sites/aiengineering/index.html"
# neetjee own content + spelling
chk "neetjee has no become a confident" "! grep -qi 'become a confident' sites/neetjee/index.html"
chk "neetjee h1 NEET preparation" "grep -qi 'NEET preparation' sites/neetjee/index.html"
chk "no neatjee misspelling anywhere" "! grep -ri 'neatjee' hub sites middleware.js tools/build.py --include='*.html' --include='*.js' --include='*.py'"


echo "== 3c. Spell / typo regression (common mistakes only)"
chk "no classic English typos in pages" "! grep -nEi '\\b(teh|recieve|seperate|occured|accomodate|definately|lenght|untill|sucess|enviroment|perfomance|avaliable|managment|developement|intership|certifcate|completetion|automtion|qualilty|technolgies|playwirght|neatjee)\\b' $PAGES"
chk "Agentic QA Technologies naming consistent (no Technology singular on pages)" "! grep -nE 'Agentic QA Technology[^I]|AgenticQA Technologies' $PAGES"
chk "British programme/organisation spellings present where used on hub" "grep -q 'programmes\\|programme' hub/index.html && grep -q 'organisations' hub/index.html"

echo "== 4. Local smoke (python3 -m http.server)"
python3 -m http.server 8765 --bind 127.0.0.1 >/dev/null 2>&1 & SP=$!; sleep 2
for u in / /hub/ /hub/privacy.html /sites/ai/ /sites/aiengineering/ /sites/neetjee/ /sites/playwrightai/ /assets/css/styles.css /assets/js/site.js /assets/brand/logo.svg /assets/img/ganesh.webp; do
  c=$(curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:8765$u); chk "HTTP 200 $u ($c)" "[ $c = 200 ]"; done
kill $SP 2>/dev/null || true
echo "== 5a. FormSubmit handler mock"
if node tests/formsubmit-handler-mock.mjs; then PASS=$((PASS+7)); else FAIL=$((FAIL+1)); fi
if out=$(node tests/contact-validate.test.mjs); then echo "$out"; n=$(printf '%s\n' "$out" | grep -c '^PASS' || true); PASS=$((PASS+n)); else echo "$out"; n=$(printf '%s\n' "$out" | grep -c '^PASS' || true); f=$(printf '%s\n' "$out" | grep -c '^FAIL' || true); PASS=$((PASS+n)); FAIL=$((FAIL+f)); fi
if out=$(node tests/contact-handler.test.mjs); then echo "$out"; n=$(printf '%s\n' "$out" | grep -c '^PASS' || true); PASS=$((PASS+n)); else echo "$out"; n=$(printf '%s\n' "$out" | grep -c '^PASS' || true); f=$(printf '%s\n' "$out" | grep -c '^FAIL' || true); PASS=$((PASS+n)); FAIL=$((FAIL+f)); fi


if out=$(node tests/enquiry-email.test.mjs); then echo "$out"; n=$(printf '%s\n' "$out" | grep -c '^PASS' || true); PASS=$((PASS+n)); else echo "$out"; n=$(printf '%s\n' "$out" | grep -c '^PASS' || true); f=$(printf '%s\n' "$out" | grep -c '^FAIL' || true); PASS=$((PASS+n)); FAIL=$((FAIL+f)); fi

echo "== 5. Extended QA (forms / footer / a11y / CSS / routing / JS risk)"
if out=$(python3 tests/extended-qa.py); then
  echo "$out"
  # Count PASS lines from extended (exclude EXTENDED RESULT)
  n=$(printf '%s\n' "$out" | grep -c '^PASS  ' || true)
  PASS=$((PASS+n))
else
  echo "$out"
  n=$(printf '%s\n' "$out" | grep -c '^PASS  ' || true)
  f=$(printf '%s\n' "$out" | grep -c '^FAIL  ' || true)
  PASS=$((PASS+n)); FAIL=$((FAIL+f))
fi
echo "== RESULT: $PASS pass, $FAIL fail"; [ $FAIL -eq 0 ]
