# Audit report — hub-split

Generated 2026-11-05 12:51 IST. **== RESULT: 84 pass, 0 fail**

```
== 1. Structure
PASS  exists hub/index.html
PASS  exists hub/privacy.html
PASS  exists sites/ai/index.html
PASS  exists sites/aiengineering/index.html
PASS  exists sites/neetjee/index.html
PASS  exists sites/playwrightai/index.html
PASS  exists index.html
PASS  exists middleware.js
PASS  exists vercel.json
PASS  exists package.json
PASS  exists VERSIONS.md
PASS  exists assets/css/styles.css
PASS  exists assets/js/site.js
PASS  exists assets/img/ganesh.webp
PASS  exists assets/img/moksha.webp
PASS  exists assets/brand/logo.svg
PASS  site indexes are distinct
PASS  middleware agenticqa.io/ -> /hub/index.html
PASS  middleware www.agenticqa.io/privacy.html -> /hub/privacy.html
PASS  middleware ai.agenticqa.io/ -> /sites/ai/index.html
PASS  middleware aiengineering.agenticqa.io/ -> /sites/aiengineering/index.html
PASS  middleware neetjee.agenticqa.io/ -> /sites/neetjee/index.html
PASS  middleware playwrightai.agenticqa.io/ -> /sites/playwrightai/index.html
PASS  middleware localhost:3000/ -> /hub/index.html
PASS  middleware localhost:3000/?site=neetjee -> /sites/neetjee/index.html
PASS  middleware x-git-hub.vercel.app/?site=ai -> /sites/ai/index.html
PASS  middleware agenticqa.io/?site=ai -> /sites/ai/index.html
PASS  middleware ai.agenticqa.io/?site=playwrightai -> /sites/playwrightai/index.html
PASS  middleware preview.vercel.app/ -> /hub/index.html
PASS  middleware passes /assets/ through
PASS  hub card preview link /?site=ai
PASS  hub card preview link /?site=aiengineering
PASS  hub card preview link /?site=neetjee
PASS  hub card preview link /?site=playwrightai
== 2. Link check (local href/src)
PASS  no broken local href/src
== 3. Content audit
PASS  no prices/fees amounts (₹, Rs, INR, $ amounts)
PASS  no age/grade/class-N mentions
PASS  no years-of-experience claims
PASS  no YouTube iframe/embed
PASS  no testimonials / student counts
PASS  no PAN/TAN/street address
PASS  no payment QR on new sites
PASS  LLPIN ACV-7177 + JS year in hub/index.html
PASS  LLPIN ACV-7177 + JS year in hub/privacy.html
PASS  LLPIN ACV-7177 + JS year in sites/ai/index.html
PASS  LLPIN ACV-7177 + JS year in sites/aiengineering/index.html
PASS  LLPIN ACV-7177 + JS year in sites/neetjee/index.html
PASS  LLPIN ACV-7177 + JS year in sites/playwrightai/index.html
PASS  a11y (skip link, theme toggle, all img alt) hub/index.html
PASS  a11y (skip link, theme toggle, all img alt) hub/privacy.html
PASS  a11y (skip link, theme toggle, all img alt) sites/ai/index.html
PASS  a11y (skip link, theme toggle, all img alt) sites/aiengineering/index.html
PASS  a11y (skip link, theme toggle, all img alt) sites/neetjee/index.html
PASS  a11y (skip link, theme toggle, all img alt) sites/playwrightai/index.html
PASS  email/phone/YouTube present on hub
PASS  admin@agenticqa.io in footer of every page
PASS  ganesh@ only in hub founder section
== 3a. Hub language ban + order
PASS  hub visible text has no course/syllabus/enrol/waitlist/batch/beginner/become a confident
PASS  hub section order company>founder>cofounder>certificates>activities
PASS  accent neural on hub/index.html
PASS  accent signal on sites/ai/index.html
PASS  accent mint on sites/aiengineering/index.html
PASS  accent amber on sites/neetjee/index.html
PASS  accent violet on sites/playwrightai/index.html
PASS  no neatjee misspelling
== 3b. Subdomain content boundaries
PASS  ai has no course/syllabus/enrol/waitlist/batch/beginner/become a confident
PASS  ai has no enquiry waitlist-form id
PASS  ai uses enquiry-form
PASS  ai h1 is business agents
PASS  playwrightai has become a confident
PASS  playwrightai exclusive vs ai
PASS  aiengineering has no become a confident
PASS  aiengineering h1 LLMs/RAG
PASS  neetjee has no become a confident
PASS  neetjee h1 NEET preparation
PASS  no neatjee misspelling anywhere
== 4. Local smoke (python3 -m http.server)
PASS  HTTP 200 / (200)
PASS  HTTP 200 /hub/ (200)
PASS  HTTP 200 /hub/privacy.html (200)
PASS  HTTP 200 /sites/ai/ (200)
PASS  HTTP 200 /sites/aiengineering/ (200)
PASS  HTTP 200 /sites/neetjee/ (200)
PASS  HTTP 200 /sites/playwrightai/ (200)
PASS  HTTP 200 /assets/css/styles.css (200)
PASS  HTTP 200 /assets/js/site.js (200)
PASS  HTTP 200 /assets/brand/logo.svg (200)
PASS  HTTP 200 /assets/img/ganesh.webp (200)
== RESULT: 84 pass, 0 fail
```
