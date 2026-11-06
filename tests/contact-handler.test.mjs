import { Readable } from 'node:stream';
import { validateContactPayload, ALLOWED } from '../api/lib/contact-validate.js';
import { parseContactBody, PARSE_LIMITS } from '../api/lib/parse-body.js';

let fail = 0;
function chk(name, cond) {
  console.log((cond ? 'PASS' : 'FAIL') + '  ' + name);
  if (!cond) fail++;
}

const SUBJECTS = Object.keys(ALLOWED);

function multipartBody(fields, boundary = '----TestBoundary7MA4YWxk') {
  const parts = [];
  for (const [k, v] of Object.entries(fields)) {
    parts.push(
      `--${boundary}\r\nContent-Disposition: form-data; name="${k}"\r\n\r\n${v}\r\n`
    );
  }
  parts.push(`--${boundary}--\r\n`);
  return Buffer.from(parts.join(''), 'utf8');
}

function streamReq({ method = 'POST', ct, buf, ip = '198.51.100.10' }) {
  const req = Readable.from([buf]);
  req.method = method;
  req.headers = { 'content-type': ct, 'x-forwarded-for': ip };
  req.socket = { remoteAddress: ip };
  return req;
}

function mockRes() {
  const r = { statusCode: 0, body: null };
  r.status = (c) => { r.statusCode = c; return r; };
  r.json = (b) => { r.body = b; return r; };
  r.setHeader = () => {};
  return r;
}

// --- parseContactBody unit ---
{
  const boundary = '----TestBoundary7MA4YWxk';
  const buf = multipartBody({
    _subject: 'Agentic QA enquiry',
    name: 'Pradhidhan',
    email: 'student@example.com',
    interest: 'NEET Prep',
    profile: 'Student',
    message: 'student',
    _honey: '',
    _template: 'table',
  }, boundary);
  const parsed = await parseContactBody(streamReq({
    ct: `multipart/form-data; boundary=${boundary}`,
    buf,
  }));
  chk('multipart parses _subject', parsed._subject === 'Agentic QA enquiry');
  chk('multipart parses name/email', parsed.name === 'Pradhidhan' && parsed.email === 'student@example.com');
  chk('multipart allowlist validates', validateContactPayload(parsed).ok === true);
}

for (const sub of SUBJECTS) {
  const boundary = '----B' + sub.length;
  const buf = multipartBody({
    _subject: sub, name: 'T', email: 't@ex.co', interest: 'i', profile: 'p', message: 'm', _honey: '',
  }, boundary);
  const parsed = await parseContactBody(streamReq({ ct: `multipart/form-data; boundary=${boundary}`, buf }));
  const v = validateContactPayload(parsed);
  chk(`multipart ok: ${sub}`, v.ok === true && v.data.subject === sub);
}

{
  const boundary = '----HoneyB';
  const buf = multipartBody({ _subject: 'Agentic QA enquiry', name: 'T', email: 't@ex.co', _honey: 'bot' }, boundary);
  const parsed = await parseContactBody(streamReq({ ct: `multipart/form-data; boundary=${boundary}`, buf }));
  chk('multipart honeypot', validateContactPayload(parsed).honeypot === true);
}

{
  const boundary = '----FileB';
  // file part should reject
  const raw = Buffer.from(
    `--${boundary}\r\nContent-Disposition: form-data; name="file"; filename="x.txt"\r\nContent-Type: text/plain\r\n\r\nhi\r\n--${boundary}--\r\n`
  );
  let threw = false;
  try {
    await parseContactBody(streamReq({ ct: `multipart/form-data; boundary=${boundary}`, buf: raw }));
  } catch (e) {
    threw = e.status === 400;
  }
  chk('multipart rejects files', threw);
}

{
  const big = 'x'.repeat(PARSE_LIMITS.MAX_BODY + 100);
  let threw = false;
  try {
    await parseContactBody(streamReq({
      ct: 'application/json',
      buf: Buffer.from(JSON.stringify({ _subject: 'Agentic QA enquiry', name: 'A', email: 'a@b.co', pad: big })),
    }));
  } catch (e) {
    threw = e.status === 413;
  }
  chk('oversized body → 413', threw);
}

{
  const parsed = await parseContactBody({
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: { _subject: 'Agentic QA enquiry', name: 'A', email: 'a@b.co', interest: '', profile: '', message: '', _honey: '' },
  });
  chk('already-parsed object body', parsed._subject === 'Agentic QA enquiry');
}

{
  const q = new URLSearchParams({
    _subject: 'AI for Business enquiry', name: 'A', email: 'a@b.co', interest: 'x', profile: 'y', message: 'z', _honey: '',
  }).toString();
  const parsed = await parseContactBody(streamReq({
    ct: 'application/x-www-form-urlencoded',
    buf: Buffer.from(q),
  }));
  chk('urlencoded parses', validateContactPayload(parsed).ok === true);
}

{
  const payload = {
    _subject: 'Playwright AI waitlist', name: 'A', email: 'a@b.co', interest: 'x', profile: 'y', message: 'z', _honey: '',
  };
  const parsed = await parseContactBody(streamReq({
    ct: 'application/json',
    buf: Buffer.from(JSON.stringify(payload)),
  }));
  chk('json parses', validateContactPayload(parsed).ok === true);
}

// --- handler integration (no SMTP) ---
process.env.SMTP_USER = '';
process.env.SMTP_PASS = '';
const { default: handler } = await import('../api/contact.js');

{
  const boundary = '----HubMP';
  const buf = multipartBody({
    _subject: 'Agentic QA enquiry', name: 'Pradhidhan', email: 'student@example.com',
    interest: 'NEET Prep', profile: 'Student', message: 'student', _honey: '', _template: 'table',
  }, boundary);
  const res = mockRes();
  await handler(streamReq({ ct: `multipart/form-data; boundary=${boundary}`, buf }), res);
  // SMTP unset → 503 after successful parse/validate (not Unknown enquiry type)
  chk('handler multipart → 503 not unknown-type', res.statusCode === 503 && res.body?.success === 'false' && !/unknown enquiry/i.test(res.body?.message || ''));
}

{
  const res = mockRes();
  await handler(streamReq({
    ct: 'application/json',
    buf: Buffer.from(JSON.stringify({
      _subject: 'Agentic QA enquiry', name: 'A', email: 'a@b.co', interest: '', profile: '', message: '', _honey: '',
    })),
  }), res);
  chk('handler JSON → 503 when SMTP unset', res.statusCode === 503);
}

{
  const res = mockRes();
  const req = { method: 'GET', headers: {}, socket: {} };
  await handler(req, res);
  chk('handler GET → 405', res.statusCode === 405);
}

process.exit(fail ? 1 : 0);
