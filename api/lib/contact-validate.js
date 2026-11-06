/** Pure contact-form validation (no I/O). Used by /api/contact and tests. */
export const ALLOWED = Object.freeze({
  'Agentic QA enquiry': { flow: 'hub', formId: 'enquiry-form' },
  'AI for Business enquiry': { flow: 'ai', formId: 'enquiry-form' },
  'AI Engineering waitlist': { flow: 'aiengineering', formId: 'waitlist-form' },
  'CatalystAI NEET enquiry': { flow: 'neetjee', formId: 'waitlist-form' },
  'Playwright AI waitlist': { flow: 'playwrightai', formId: 'waitlist-form' },
});

const LIMITS = { name: 120, email: 200, interest: 120, profile: 120, message: 4000, subject: 160 };

function stripCtrl(s) {
  return String(s ?? '').replace(/[\r\n\0]/g, ' ').trim();
}

export function validateContactPayload(raw) {
  if (!raw || typeof raw !== 'object') return { ok: false, status: 400, message: 'Invalid request.' };
  // Honeypot: any value → fake success (no send)
  if (stripCtrl(raw._honey || raw.honey || '')) return { ok: true, honeypot: true };

  const subject = stripCtrl(raw._subject || raw.subject);
  if (!ALLOWED[subject]) return { ok: false, status: 400, message: 'Unknown enquiry type.' };

  const name = stripCtrl(raw.name);
  const email = stripCtrl(raw.email).toLowerCase();
  const interest = stripCtrl(raw.interest);
  const profile = stripCtrl(raw.profile);
  const message = stripCtrl(raw.message);

  if (!name || name.length > LIMITS.name) return { ok: false, status: 400, message: 'Please enter a valid name.' };
  if (!email || email.length > LIMITS.email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    return { ok: false, status: 400, message: 'Please enter a valid email.' };
  }
  if (interest.length > LIMITS.interest || profile.length > LIMITS.profile || message.length > LIMITS.message) {
    return { ok: false, status: 400, message: 'One or more fields are too long.' };
  }
  for (const key of ['name', 'email', '_subject', 'subject', 'interest', 'profile']) {
    if (/[\r\n]/.test(String(raw[key] ?? ''))) {
      return { ok: false, status: 400, message: 'Invalid characters in fields.' };
    }
  }

  return {
    ok: true,
    honeypot: false,
    data: { subject, name, email, interest, profile, message, flow: ALLOWED[subject].flow },
  };
}
