// Next-batch date: 15th and 30th of each month (Feb: 15th + last day of Feb).
// "Today" = Asia/Kolkata; optional ?today=YYYY-MM-DD override for preview testing.
// ESM — imported by tests and loaded as <script type="module"> on pages.

const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

export function parseYmd(ymd) {
  const p = String(ymd).split('-').map(Number);
  return { y: p[0], m: p[1], d: p[2] };
}

export function ymdToUtcMs(ymd) {
  const { y, m, d } = parseYmd(ymd);
  return Date.UTC(y, m - 1, d);
}

export function utcMsToYmd(ms) {
  const dt = new Date(ms);
  const y = dt.getUTCFullYear();
  const m = dt.getUTCMonth() + 1;
  const d = dt.getUTCDate();
  return y + '-' + String(m).padStart(2, '0') + '-' + String(d).padStart(2, '0');
}

function pad2(n) {
  return String(n).padStart(2, '0');
}

function toYmd(y, m, d) {
  return y + '-' + pad2(m) + '-' + pad2(d);
}

/** Last calendar day of month m (1–12) in year y. */
export function lastDayOfMonth(y, m) {
  // Day 0 of next month = last day of this month (UTC)
  return new Date(Date.UTC(y, m, 0)).getUTCDate();
}

/**
 * Batch days in month m (1–12) of year y: always the 15th, plus
 * the 30th — or in February, the last day (28 or 29).
 * Months with fewer than 30 days only apply to February here.
 */
export function batchDaysInMonth(y, m) {
  if (m === 2) return [15, lastDayOfMonth(y, 2)];
  return [15, 30];
}

/** Format as "D Mon YYYY" (e.g. 30 Nov 2026). */
export function formatBatchDate(ymd) {
  const { y, m, d } = parseYmd(ymd);
  return d + ' ' + MONTHS[m - 1] + ' ' + y;
}

/**
 * Next batch date strictly AFTER todayYmd (calendar 15th / 30th; Feb last day).
 * On a batch day itself, returns the following batch.
 */
export function nextBatchDate(todayYmd) {
  const { y, m, d } = parseYmd(todayYmd);
  let yy = y;
  let mm = m;
  // Search current month, then forward up to 14 months (safety).
  for (let i = 0; i < 14; i++) {
    const days = batchDaysInMonth(yy, mm);
    for (let j = 0; j < days.length; j++) {
      const bd = days[j];
      if (yy > y || (yy === y && mm > m) || (yy === y && mm === m && bd > d)) {
        return toYmd(yy, mm, bd);
      }
    }
    mm += 1;
    if (mm > 12) { mm = 1; yy += 1; }
  }
  throw new Error('nextBatchDate: no candidate found after ' + todayYmd);
}

/** Today's calendar date in Asia/Kolkata (IST), YYYY-MM-DD. */
export function todayInKolkata(now) {
  const dt = now instanceof Date ? now : new Date();
  return new Intl.DateTimeFormat('en-CA', {
    timeZone: 'Asia/Kolkata',
    year: 'numeric',
    month: '2-digit',
    day: '2-digit'
  }).format(dt);
}

/** Preview hook: ?today=YYYY-MM-DD overrides "today". */
export function todayFromSearch(search) {
  const q = search == null
    ? (typeof location !== 'undefined' ? location.search : '')
    : String(search);
  const m = /(?:^\?|&)today=(\d{4}-\d{2}-\d{2})(?:&|$)/.exec(q);
  return m ? m[1] : null;
}

function fillEl(el, ymd) {
  const label = formatBatchDate(ymd);
  const fmt = el.getAttribute('data-batch-format') || 'text';
  if (fmt === 'fact') {
    const parts = label.match(/^(\d{1,2}) (.+)$/);
    el.textContent = '';
    if (parts) {
      el.appendChild(document.createTextNode(parts[1]));
      const small = document.createElement('small');
      small.textContent = ' ' + parts[2];
      el.appendChild(small);
    } else {
      el.appendChild(document.createTextNode(label));
    }
  } else {
    el.textContent = label;
  }
}

export function applyBatchDates(opts) {
  if (typeof document === 'undefined') return null;
  const search = opts && opts.search != null ? opts.search : (typeof location !== 'undefined' ? location.search : '');
  const today = todayFromSearch(search) || todayInKolkata(opts && opts.now);
  const ymd = nextBatchDate(today);
  const nodes = document.querySelectorAll('[data-batch-date]');
  for (let i = 0; i < nodes.length; i++) fillEl(nodes[i], ymd);
  return { today, ymd, label: formatBatchDate(ymd) };
}

function boot() {
  applyBatchDates();
}

if (typeof document !== 'undefined') {
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
}
