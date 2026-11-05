// Vercel Routing Middleware — host-based rewrites for the Agentic QA hub + subdomain sites.
// Shared files under /assets/ are served as-is for every host (pages reference /assets/... absolute paths).
import { rewrite, next } from '@vercel/functions';

export const HOST_MAP = {
  'agenticqa.io': '/hub',
  'www.agenticqa.io': '/hub',
  'ai.agenticqa.io': '/sites/ai',
  'aiengineering.agenticqa.io': '/sites/aiengineering',
  'neetjee.agenticqa.io': '/sites/neetjee',
  'playwrightai.agenticqa.io': '/sites/playwrightai',
};
// ?site= values for localhost / preview testing
export const SITE_PARAM = { hub: '/hub', ai: '/sites/ai', aiengineering: '/sites/aiengineering', neetjee: '/sites/neetjee', playwrightai: '/sites/playwrightai' };

export const config = { matcher: ['/((?!assets/|_vercel|favicon\\.ico).*)'] };

export function resolvePrefix(host, siteParam) {
  const h = (host || '').toLowerCase().split(':')[0];
  if (HOST_MAP[h]) return HOST_MAP[h];
  // localhost, *.vercel.app previews, anything else → hub (optionally overridden by ?site=)
  if (siteParam && SITE_PARAM[siteParam]) return SITE_PARAM[siteParam];
  return '/hub';
}

export default function middleware(request) {
  const url = new URL(request.url);
  const p = url.pathname;
  if (p.startsWith('/assets/') || p.startsWith('/hub/') || p.startsWith('/sites/') || p === '/robots.txt' || p === '/sitemap.xml') return next();
  const prefix = resolvePrefix(request.headers.get('host'), url.searchParams.get('site'));
  url.pathname = prefix + (p.endsWith('/') ? p + 'index.html' : p);
  return rewrite(url);
}
