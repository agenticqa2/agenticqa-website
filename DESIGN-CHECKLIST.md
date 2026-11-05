# AgenticQA website rebuild — design checklist & prompt template

**Branch:** `hub-split`  
**Folder:** `Documents/AgenticQA/agenticqa-website-hub-split`  
**Status:** Planning document only. Do not treat this as live content approval.  
**Host spelling:** use `neetjee.agenticqa.io` (NEET + JEE). Do not use `neatjee`.

---

## 1. Purpose

Rebuild agenticqa.io as an **enterprise software / AI company hub**, not a teaching or course landing page. The hub introduces the company, founders, credentials, and activities. Four product/program sites live on subdomains and must work when opened directly as well as from hub links.

**Study, don’t copy:** use enterprise-level reference sites (serious B2B software / AI company homes) for structure, hierarchy, whitespace, and professionalism. Do **not** paste their copy or brand. Do **not** drop any content that already exists on the current Agentic QA site — relocate it (see §3a).

---

## 2. Shared brand base (all hosts)

Keep one family across hub + all subdomains.

| Token | Value | Use |
|--------|--------|-----|
| Ink | `#0E1525` | Page background / dark surfaces |
| Neural | `#5B4BFF` | Primary brand / default accent |
| Signal | `#06B6D4` | Secondary accent / links on dark |
| Mint | `#10B981` | Success / positive |
| Amber | `#F59E0B` | Attention / highlight |
| Type — headings | Space Grotesk | H1–H3, logo lockups |
| Type — body | Manrope | Body, UI, forms |
| Logo | `assets/brand/logo.svg` (+ dark variant) | Header + footer on every host |
| Icon / favicon | `assets/brand/icon.svg` and PNG set | Every host |
| Footer legal | `© {year} Agentic QA Technologies LLP · LLPIN: ACV-7177 · Registered in Puducherry, India` | Auto year via `site.js` |

### Accent shift (subdomains feel distinct, still one family)

Keep palette foundation, logo, and type scale identical. Change **only the primary accent** (buttons, pills, gradient stops, focus rings):

| Host | Accent role | Suggested accent |
|------|-------------|------------------|
| `agenticqa.io` / `www` (hub) | Brand default | Neural `#5B4BFF` |
| `ai.agenticqa.io` | Business / consulting | Signal `#06B6D4` |
| `aiengineering.agenticqa.io` | Technical / builders | Mint `#10B981` |
| `neetjee.agenticqa.io` | Exam prep | Amber `#F59E0B` |
| `playwrightai.agenticqa.io` | Automation learning | Neural `#5B4BFF` (or a violet sibling of Neural, not a new unrelated hue) |

Implementation note: one shared stylesheet; each site root sets a data attribute or CSS variable (e.g. `data-accent="signal"`) that remaps `--accent` only.

---

## 3. Hard content rules (every page)

- No fees, prices, or discount amounts on the site (fees on a call / email only).
- No “years of experience” claims.
- No fake testimonials.
- No YouTube embeds.
- Never show anyone’s grade or age.
- No PAN, TAN, or full street address.
- No invented student counts.
- Drafts need Ganesh’s approval before merge to `main` or any live deploy.

---

## 3a. Hub language ban (training stays off the hub hero)

The hub (`agenticqa.io` / `www`) must read as a **software / AI company** from the **first line** (title, H1, lede, hero pill, primary CTAs).

**Forbidden on the hub hero / above-the-fold / primary H1** (and do not recycle as the hub’s opening story anywhere in the first screen):

- Lines like “Become a confident AI-ready Playwright automation tester”
- “Beginner-friendly live course(s)” as the lead promise
- Batch-start countdown framed as the main offer
- Waitlist / “Enroll” / “Join the course” as the primary company CTA
- Any other training-division messaging that makes the company home feel like a Playwright class page

**Where that copy belongs:** `playwrightai.agenticqa.io` only (and short gateway cards in hub §4.5 Activities that point there — cards summarize, they do not paste the full course hero).

Company-level mentions of “training programs” as one of several business lines are fine **after** the company identity is clear — never as the opening hook.

---

## 3b. Preserve all existing content (relocate, don’t delete)

Nothing from the current live / v7 site is throwaway. Inventory and **move**:

| Current material | Destination |
|------------------|-------------|
| Playwright course hero, syllabus, labs, waitlist/demo, course facts | `playwrightai.agenticqa.io` |
| AI engineering curriculum / projects | `aiengineering.agenticqa.io` |
| CatalystAI / NEET (and JEE if present) | `neetjee.agenticqa.io` |
| Business consulting / agents / fees-on-a-call | `ai.agenticqa.io` |
| Company mission, founders (Ganesh, Moksha), certificate story, org schema-level facts, privacy, footer legal | Hub `agenticqa.io` |
| Shared brand assets, contact channels, LLPIN footer | Every host as appropriate |

Before calling a rebuild “done,” diff against the previous site (and/or `archive/` / last tagged release) and confirm every section, form, image, and policy page still exists somewhere intentional.

---

## 4. MAIN PAGE — `agenticqa.io` / `www.agenticqa.io`

**Tone:** enterprise software / AI company site from the first pixel. **Do not** open with Playwright teaching, beginner-course slogans, batch dates, or course CTAs (see §3a). Teaching-division messaging belongs only on `playwrightai.agenticqa.io`. Preserve existing company copy and relocate training copy — do not thin the site (§3b).

### Section order (exact)

#### 4.1 Company first

Elaborate, enterprise-level detail:

- Who we are: **Agentic QA Technologies LLP** (legal name on footer; student-facing brand Agentic QA Technologies).
- What we do: AI-native quality engineering, automation consulting, custom AI agents for companies, and structured training programs that feed industry-ready skill.
- Aims / mission: make engineers job-ready for the AI era; teach and deliver the way real teams practise — live, hands-on, project-driven where training applies; deliver reliable AI + QA outcomes for business clients.
- Goals: build durable in-house tooling and programs; serve companies with consulting and agents; support learners through clear pathways (AI engineering, Playwright + AI, NEET prep via CatalystAI).
- Achievements (only verifiable, no invented metrics): e.g. Industry Internship Completion Certificate for program graduates; named in-house projects (FeedbackPulse, MeetingMind, ResumeGenie, StudyMate) as proof of applied AI work; LLP registration (LLPIN ACV-7177, Puducherry). Prefer outcomes and artifacts over hype.
- Contact strip allowed (email, phone, LinkedIn, YouTube channel link as text — no embed).

#### 4.2 Then Ganesan (founder)

- Name: Ganesan (Ganesh) Sivaraman — founder / AI QA Architect framing as already used.
- Role in the company, teaching and consulting posture (no years-of-experience lines).
- Photo: `ganesh.webp`.
- Links: LinkedIn, YouTube @AgenticQA (text links only).

#### 4.3 Then Moksha Meera

- Co-founder and director; leads technical side; builds in-house projects/tooling; teaches alongside Ganesh.
- Photo: `moksha.webp`.
- No age, grade, or school year.

#### 4.4 Then certificate issuing for students

- Industry Internship Completion Certificate for graduates of the training program.
- Use existing certificate imagery (e.g. handover photo) with accurate captions.
- Explain what the certificate represents; do not invent accreditation bodies.

#### 4.5 Then activities (with four subdomain gateways)

Activities overview of the four lines of work. **In this section**, include four navigation cards/links so visitors can open each subdomain:

| Card | URL | One-line promise on the hub |
|------|-----|-----------------------------|
| AI for business | `https://ai.agenticqa.io/` | Custom agents, automation consulting, business-side AI QA |
| AI engineering | `https://aiengineering.agenticqa.io/` | LLMs, RAG, vector DBs, fine-tuning — builder track |
| NEET prep | `https://neetjee.agenticqa.io/` | Syllabus, mocks, study plans (CatalystAI) |
| Playwright + AI | `https://playwrightai.agenticqa.io/` | Playwright testing with AI — tutorials & labs |

Each card: title, 2–3 sentence summary, clear CTA (“Open site”). Cards must not dump full subdomain curricula onto the hub.

Optional after activities: single contact / enquiry form for company-level questions (not course-only waitlist language).

---

## 5. SUB PAGES — content ownership

Each subdomain is a **standalone site**: own hero, nav, sections, footer, SEO title/description. Hub summaries stay short; detail lives here.

### 5.1 `ai.agenticqa.io` — business side

- Custom AI agents for companies
- Automation / AI-native QA consulting
- LLM evaluation, RAG for business workflows (business framing, not deep curriculum)
- Engagement process (discover → pilot → harden → handoff)
- Pricing: “discussed on a call” only — no numbers
- Enquiry CTA

### 5.2 `neetjee.agenticqa.io` — NEET exam prep

- NCERT-aligned syllabus pathways (Biology, Chemistry, Physics as applicable)
- Mock tests (chapter / full-length) and weak-area guidance
- Study plans
- CatalystAI mentors/support as already featured (no ages/grades)
- Waitlist / ask CTA  
- Note: if JEE returns later, add explicitly; current rebuild brief is NEET-first unless Ganesh says otherwise.

### 5.3 `aiengineering.agenticqa.io` — technical / builder side

- Building with LLMs
- RAG and vector databases
- Agents / tooling (e.g. MCP where accurate)
- Evaluation and model fine-tuning
- In-house project showcases (screenshots OK)
- Class / cohort format if offered — still no fees on page
- Waitlist CTA

### 5.4 `playwrightai.agenticqa.io` — Playwright testing with AI

- Tutorials and hands-on labs
- Live course structure (class length, days, capstone) when accurate
- POM, SDET skills, AI-assisted testing / Playwright MCP where accurate
- Certificate mention can cross-link the idea; primary certificate story stays on hub section 4.4
- Waitlist / demo CTA — not the company-first story

---

## 6. Technical checklist (hub-split)

- [ ] Host routing via `middleware.js` for hub + four subdomains (+ `www`)
- [ ] Shared `/assets/` (brand, css, js, img)
- [ ] Accent via CSS variable / `data-accent` per site
- [ ] Footer LLPIN line + auto year on every page
- [ ] Hub section order matches §4 exactly
- [ ] Hub does not lead with Playwright / beginner-course / “become a confident…” training language (§3a)
- [ ] Content preservation diff done — nothing from current site lost (§3b)
- [ ] Hub first screen reads as software/AI company, not a class page
- [ ] All four activity cards use correct `https://` hosts (`neetjee`, not `neatjee`)
- [ ] Each subdomain loads with meaningful content if typed directly
- [ ] Vercel project domains added for every host (including `playwrightai`) before calling it “live”
- [ ] DNS CNAMEs → `cname.vercel-dns.com` for each subdomain
- [ ] `tests/run-tests.sh` green before preview push
- [ ] No merge to `main` without explicit Ganesh approval

---

## 7. Ready-to-use prompt template

Copy-paste for any future build pass:

```text
You are updating the Agentic QA site in Documents/AgenticQA/agenticqa-website-hub-split on branch hub-split only. Do not merge to main or deploy to production without explicit approval.

Shared brand: Ink #0E1525, Neural #5B4BFF, Signal #06B6D4, Mint #10B981, Amber #F59E0B; headings Space Grotesk; body Manrope; logos from assets/brand. One shared stylesheet; each host may change only the primary accent (hub=Neural, ai=Signal, aiengineering=Mint, neetjee=Amber, playwrightai=Neural/violet sibling).

Hard rules: no fees/prices on site; no years of experience; no fake testimonials; no YouTube embeds; never show age or grade; no PAN/TAN/street address; no invented metrics.

HUB LANGUAGE BAN: agenticqa.io must read as a software/AI company from the first line. Do NOT open with training/course language such as “Become a confident AI-ready Playwright automation tester”, “beginner-friendly live course(s)”, batch-start-as-main-offer, or enroll/waitlist as the primary company CTA. That training-division messaging belongs ONLY on playwrightai.agenticqa.io. Short activity cards on the hub may link there; they must not paste the course hero.

PRESERVE ALL EXISTING CONTENT: do not delete current-site material. Relocate Playwright course/syllabus/labs/waitlist → playwrightai; AI engineering → aiengineering; CatalystAI/NEET → neetjee; business agents/consulting → ai; company/founders/certificate/privacy/legal → hub. Diff against the previous site before finishing.

REFERENCE BAR: study enterprise B2B software/AI company sites for structure and professionalism; do not copy their copy or brand.

MAIN PAGE (agenticqa.io / www) — company site, NOT a teaching page. Section order MUST be:
1) Company first — what Agentic QA Technologies LLP is, what we do, aims, goals, achievements (enterprise depth).
2) Ganesan (Ganesh) Sivaraman — founder.
3) Moksha Meera — co-founder/director (no age/grade).
4) Certificate issuing for students (Industry Internship Completion Certificate).
5) Activities — include four gateway cards to:
   https://ai.agenticqa.io/
   https://neetjee.agenticqa.io/
   https://aiengineering.agenticqa.io/
   https://playwrightai.agenticqa.io/
Each subdomain must also work standalone.

SUBDOMAIN CONTENT:
- ai: business — custom agents, consulting, pricing-on-call, enquiry.
- neetjee: NEET prep — syllabus, mocks, study plans, CatalystAI support.
- aiengineering: technical — LLMs, RAG, vector DBs, fine-tuning, builder projects.
- playwrightai: Playwright + AI — tutorials, labs, live course details (including any former hub course hero lines).

Keep middleware host routing; shared /assets; footer with LLPIN ACV-7177 and auto year. Run tests/run-tests.sh. Report files changed and any content needing Ganesh approval. Spelling: neetjee not neatjee.
```

---

## 8. Document history

| Date | Note |
|------|------|
| 2026-11-05 | Initial checklist + prompt template from voice planning session. Planning only; page code not changed in this step. |
| 2026-11-05 | Added §3a hub language ban (no “become a confident…” / beginner-course lead on hub); §3b preserve-and-relocate all existing content; enterprise reference bar; prompt template + tech checklist updated. |
