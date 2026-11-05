# Site versions

Every design is preserved as an annotated git tag so it can be restored at any time.

| Tag | Commit | Date | Description |
|---|---|---|---|
| `v1-original` | `d434511` | 2026-01-31 | Initial import — original "AgenticQA Infotech" site |
| `v1-final` | `d379b43` | 2026-02-17 | Original design after Feb 2026 fixes (formsubmit.co contact form, EU services) |
| `v2-github-style` | `ebf747b` | 2026-03-02 | GitHub.com-inspired UI (`5f9d1c1`) + docs mobile fix |
| `v3-metamuse` | `79332d8` | 2026-11-03 | QA-first editorial design (Fraunces / IBM Plex) |
| `v4-modern` *(branch `redesign-v4`)* | — | 2026-11-03 | Modern redesign: Inter/Plus Jakarta, light/dark, course-focused homepage |

## Inspect an old version locally

```bash
git fetch --tags
git checkout v2-github-style      # detached HEAD, read-only look
python3 -m http.server 8000       # open http://localhost:8000
git checkout main                 # go back
```

## Roll production back

**Option A — Vercel (fastest, no git changes):** Vercel dashboard → project → *Deployments* →
find the deployment built from the wanted commit → `⋯` → **Promote to production**
(or **Instant Rollback**).

**Option B — git (permanent):**

```bash
# make main look exactly like an old tag, as a new commit (history kept)
git checkout main
git restore --source=v3-metamuse --worktree --staged -- .
git commit -m "Roll back to v3-metamuse"
git push origin main               # Vercel redeploys automatically
```

## Ship v4

```bash
git push origin redesign-v4 --tags  # Vercel builds a preview URL for the branch
# review the preview, then:
git checkout main && git merge --ff-only redesign-v4 && git push origin main
git tag -a v4-modern -m "v4 modern redesign" && git push origin v4-modern
```
