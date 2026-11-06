# Hub-split QA audit — 2026-11-05 (Asia/Calcutta)

Commit: `d3b0fc7` on `hub-split` (preview only). `origin/main` remains `a453389`. Production untouched.

## Triple review

### Pass 1 — banned training language (hub + ai)
- hub/ai visible body: no course / syllabus / enroll / waitlist / batch / beginner / bootcamp / workshop / training / “become a confident”
- Shared footer Sites link “NEET Prep” on all pages is navigation only (not body sell copy)
- playwrightai retains course language by design

### Pass 2 — unique purpose / brand / emails / titles
| Page | Accent | H1 purpose |
|------|--------|------------|
| hub | neural | Company-first AI-native QE + agents |
| ai | signal | Custom AI agents / consulting / pricing |
| aiengineering | mint | LLMs, RAG, vector DBs (8-topic builder track) |
| neetjee | amber | NEET prep on **neetjee** + JEE practice track |
| playwrightai | violet | Playwright training exclusively |

- Founder cards: Ganesh = Founder only; Moksha = Co-founder, Director & Tech Lead (unchanged)
- admin@ on footer + contact forms; ganesh@ on founder card only
- Certificates: names left (Sivanesan P only) + sample SVG right + handover photo kept

### Pass 3 — links / cross-contamination
- Hub activity cards: `/?site={ai|aiengineering|neetjee|playwrightai}` + `data-prod-href`
- Middleware prefers `?site=` over host map (preview-safe)
- No hub-card absolute prod hrefs
- No Playwright “become a confident” / batch CTAs on hub or ai

## Tests
`bash tests/run-tests.sh` → **84 pass, 0 fail**

## Preview
- Deployment URL: https://agenticqa-website-pebmq933x-ganeshs-projects-ef1c52b3.vercel.app
- Branch alias: https://agenticqa-website-git-hub-split-ganeshs-projects-ef1c52b3.vercel.app
- Params: `/?site=ai` · `/?site=aiengineering` · `/?site=neetjee` · `/?site=playwrightai`
- Note: Vercel Deployment Protection (SSO) — open while signed into Vercel

## Explicit
- Did **not** merge to main
- Did **not** push main
- Production (`origin/main` @ a453389) untouched
