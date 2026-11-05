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
process.exit(f?1:0);
JS
if out=$(cd /tmp/mwtest && node t.mjs); then echo "$out"; PASS=$((PASS+10)); else echo "$out"; FAIL=$((FAIL+1)); fi
for s in ai aiengineering neetjee playwrightai; do
  chk "hub card preview link /?site=$s" "grep -q 'class=\"hub-card reveal\" href=\"/?site=$s\" data-prod-href=\"https://$s.agenticqa.io/\"' hub/index.html"
done
echo "== 2. Link check (local href/src)"
broken=0
for f in $PAGES; do
  for u in $(grep -o '\(href\|src\)="[^"#]*' $f | sed 's/^[a-z]*="//' | grep -v '^https\?:\|^mailto:\|^tel:\|^$'); do
    # Middleware preview routes (/?site=ai) are not filesystem paths — skip them
    case $u in '/?site='*) continue;; esac
    case $u in /*) t=".${u}";; *) t="$(dirname $f)/$u";; esac
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

echo "== 4. Local smoke (python3 -m http.server)"
python3 -m http.server 8765 --bind 127.0.0.1 >/dev/null 2>&1 & SP=$!; sleep 2
for u in / /hub/ /hub/privacy.html /sites/ai/ /sites/aiengineering/ /sites/neetjee/ /sites/playwrightai/ /assets/css/styles.css /assets/js/site.js /assets/brand/logo.svg /assets/img/ganesh.webp; do
  c=$(curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:8765$u); chk "HTTP 200 $u ($c)" "[ $c = 200 ]"; done
kill $SP
echo "== RESULT: $PASS pass, $FAIL fail"; [ $FAIL -eq 0 ]
