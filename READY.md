# hub-split — ready for review

## Structure
```
/index.html            local fallback → /hub/ (production: middleware serves /hub for /)
/middleware.js         Host → folder rewrites (+ ?site= on localhost/previews)
/vercel.json, /package.json (@vercel/functions for rewrite/next)
/robots.txt, /sitemap.xml
/assets/brand/  css/styles.css  js/site.js  img/   ← shared by every host
/hub/index.html, /hub/privacy.html                  agenticqa.io, www.agenticqa.io
/sites/ai/index.html                                ai.agenticqa.io
/sites/aiengineering/index.html                     aiengineering.agenticqa.io
/sites/neetjee/index.html                           neetjee.agenticqa.io
/sites/playwrightai/index.html                      playwrightai.agenticqa.io
/tools/build.py        regenerates all 6 pages from shared header/footer templates
/tests/run-tests.sh    structural + middleware + link + content + smoke tests
/archive/              untouched v7 pages + their images (reference only)
```

## Asset path approach
All pages reference shared files with **root-absolute** paths (`/assets/...`). The middleware matcher
excludes `/assets/`, so every subdomain gets the same files. In-site links are relative (`./`, `#section`);
cross-site links are full `https://<sub>.agenticqa.io/` URLs.

## Preview
- Static: `cd /workspace/hub-split && python3 -m http.server 8000` → http://localhost:8000/hub/ , /sites/ai/ , ...
- With middleware: `npm i && vercel dev` → http://localhost:3000/?site=neetjee (hub by default)
- Edit content in `tools/build.py`, then `python3 tools/build.py && bash tests/run-tests.sh`.

## Before going live
Add all six domains to the Vercel project; create DNS for `ai`, `aiengineering`, `neetjee`, `playwrightai`
(CNAME cname.vercel-dns.com); remove any old A records for `playwright`/`playwrightai` pointing elsewhere.
