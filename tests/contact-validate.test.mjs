import { validateContactPayload, ALLOWED } from '../api/lib/contact-validate.js';

let fail = 0;
function chk(name, cond) {
  console.log((cond ? 'PASS' : 'FAIL') + '  ' + name);
  if (!cond) fail++;
}

chk('allowlist has 5 subjects', Object.keys(ALLOWED).length === 5);
chk('honeypot short-circuits ok', validateContactPayload({ _honey: 'x', _subject: 'Agentic QA enquiry', name: 'A', email: 'a@b.co' }).honeypot === true);
chk('unknown subject rejected', validateContactPayload({ _subject: 'Hack', name: 'A', email: 'a@b.co' }).ok === false);
chk('valid hub payload', validateContactPayload({
  _subject: 'Agentic QA enquiry', name: 'QA Test', email: 'ganesh.ganesh.siva@gmail.com',
  interest: 'Partnership / other', profile: 'Other', message: 'hi', _honey: ''
}).ok === true);
chk('crlf in name rejected', validateContactPayload({
  _subject: 'Agentic QA enquiry', name: 'A\r\nBcc: x@y.z', email: 'a@b.co'
}).ok === false);
chk('bad email rejected', validateContactPayload({
  _subject: 'Agentic QA enquiry', name: 'A', email: 'not-an-email'
}).ok === false);
chk('empty name rejected', validateContactPayload({
  _subject: 'Agentic QA enquiry', name: '', email: 'a@b.co'
}).ok === false);

// Mock SMTP path: ensure handler returns 503 without env (dynamic import with stub)
process.env.SMTP_USER = '';
process.env.SMTP_PASS = '';
const { default: handler } = await import('../api/contact.js');
function mockReq(body) {
  return {
    method: 'POST',
    headers: { 'content-type': 'application/json', 'x-forwarded-for': '203.0.113.10' },
    body,
  };
}
function mockRes() {
  const r = { statusCode: 0, body: null };
  r.status = (c) => { r.statusCode = c; return r; };
  r.json = (b) => { r.body = b; return r; };
  r.setHeader = () => {};
  return r;
}
{
  const res = mockRes();
  await handler(mockReq({
    _subject: 'Agentic QA enquiry', name: 'QA', email: 'a@b.co', interest: 'x', profile: 'y', message: 'z', _honey: ''
  }), res);
  chk('no SMTP env → 503 success false', res.statusCode === 503 && res.body?.success === 'false');
}
{
  const res = mockRes();
  await handler(mockReq({
    _subject: 'Agentic QA enquiry', name: 'QA', email: 'a@b.co', _honey: 'bot'
  }), res);
  chk('honeypot → 200 fake success no send', res.statusCode === 200 && res.body?.success === 'true');
}

process.exit(fail ? 1 : 0);
