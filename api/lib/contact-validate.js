/** Pure contact-form validation + enquiry email formatting (no I/O). */
export const ALLOWED = Object.freeze({
  'Agentic QA enquiry': {
    flow: 'hub',
    formId: 'enquiry-form',
    websiteLabel: 'Agentic QA (main)',
    interests: Object.freeze([
      'AI for Business (agents / consulting)',
      'AI evaluation / MCP work',
      'AI Engineering',
      'NEET Prep',
      'Playwright + AI',
      'Partnership / other',
      'Free demo class (30 min)',
    ]),
  },
  'AI for Business enquiry': {
    flow: 'ai',
    formId: 'enquiry-form',
    websiteLabel: 'AI for Business',
    interests: Object.freeze([
      'Custom AI agent',
      'Automation consulting',
      'AI-native QA',
      'LLM evaluation',
      'Pricing call',
      'Other',
      'Free demo class (30 min)',
    ]),
  },
  'AI Engineering waitlist': {
    flow: 'aiengineering',
    formId: 'waitlist-form',
    websiteLabel: 'AI Engineering',
    interests: Object.freeze([
      'Join the waitlist',
      'Free demo session',
      'Team / company cohort',
      'Other',
      'Free demo class (30 min)',
    ]),
  },
  'CatalystAI NEET enquiry': {
    flow: 'neetjee',
    formId: 'waitlist-form',
    websiteLabel: 'CatalystAI NEET & JEE',
    interests: Object.freeze([
      'Join the waitlist',
      'NEET mocks',
      'JEE practice',
      'Study plan',
      'Other',
      'Free demo class (30 min)',
    ]),
  },
  'Playwright AI waitlist': {
    flow: 'playwrightai',
    formId: 'waitlist-form',
    websiteLabel: 'Playwright AI',
    interests: Object.freeze([
      'Free demo class (30 min)',
      'Join waitlist / next batch',
      'A call about fees',
      'Other question',
    ]),
  },
});

const LIMITS = { name: 120, email: 200, interest: 120, profile: 120, message: 4000, subject: 160 };

function stripCtrl(s) {
  return String(s ?? '').replace(/[\r\n\0]/g, ' ').trim();
}

/** Resolve interest for mail subject: allowlisted preferred, else sanitized text, else General. */
export function resolveInterestLabel(flowMeta, interestRaw) {
  const interest = stripCtrl(interestRaw);
  if (!interest) return 'General';
  if (flowMeta.interests.includes(interest)) return interest;
  // bounded sanitized fallback (already length-checked by validate)
  return interest.slice(0, LIMITS.interest);
}

export function formatEnquiryEmail({ websiteLabel, name, email, interestLabel, profile, message }) {
  const mailSubject = `Website enquiry — ${interestLabel}`.slice(0, 200);
  const text = [
    `Website: ${websiteLabel}`,
    `Name: ${name}`,
    `Email: ${email}`,
    `Interested in: ${interestLabel}`,
    `Profile: ${profile || '(not specified)'}`,
    '',
    'Message:',
    message || '(no message)',
  ].join('\n');
  return { mailSubject, text };
}

export function validateContactPayload(raw) {
  if (!raw || typeof raw !== 'object') return { ok: false, status: 400, message: 'Invalid request.' };
  if (stripCtrl(raw._honey || raw.honey || '')) return { ok: true, honeypot: true };

  const subject = stripCtrl(raw._subject || raw.subject);
  const meta = ALLOWED[subject];
  if (!meta) return { ok: false, status: 400, message: 'Unknown enquiry type.' };

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

  const interestLabel = resolveInterestLabel(meta, interest);
  const { mailSubject, text } = formatEnquiryEmail({
    websiteLabel: meta.websiteLabel,
    name,
    email,
    interestLabel,
    profile,
    message,
  });

  return {
    ok: true,
    honeypot: false,
    data: {
      subject, // routing allowlist key (unchanged)
      mailSubject,
      text,
      name,
      email,
      interest,
      interestLabel,
      profile,
      message,
      flow: meta.flow,
      websiteLabel: meta.websiteLabel,
    },
  };
}
