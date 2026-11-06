import {
  ALLOWED,
  validateContactPayload,
  formatEnquiryEmail,
  resolveInterestLabel,
} from '../api/lib/contact-validate.js';

let fail = 0;
function chk(name, cond) {
  console.log((cond ? 'PASS' : 'FAIL') + '  ' + name);
  if (!cond) fail++;
}

const samples = [
  ['Agentic QA enquiry', 'NEET Prep', 'Website enquiry — NEET Prep', 'Agentic QA (main)'],
  ['AI for Business enquiry', 'Custom AI agent', 'Website enquiry — Custom AI agent', 'AI for Business'],
  ['AI Engineering waitlist', 'Join the waitlist', 'Website enquiry — Join the waitlist', 'AI Engineering'],
  ['CatalystAI NEET enquiry', 'NEET mocks', 'Website enquiry — NEET mocks', 'CatalystAI NEET & JEE'],
  ['Playwright AI waitlist', 'Free demo class (30 min)', 'Website enquiry — Free demo class (30 min)', 'Playwright AI'],
];

for (const [routing, interest, wantSub, wantSite] of samples) {
  const v = validateContactPayload({
    _subject: routing,
    name: 'Pradhidhan',
    email: 'student@example.com',
    interest,
    profile: 'Student',
    message: 'Hello',
    _honey: '',
  });
  chk(`${routing} ok`, v.ok === true);
  chk(`${routing} mailSubject`, v.data?.mailSubject === wantSub);
  chk(`${routing} website label`, v.data?.websiteLabel === wantSite);
  chk(`${routing} body Website line`, v.data?.text?.startsWith(`Website: ${wantSite}`) === true);
  chk(`${routing} body labels`, /Name: Pradhidhan/.test(v.data?.text) && /Interested in: /.test(v.data?.text) && /Message:\nHello/.test(v.data?.text));
  chk(`${routing} keeps routing subject`, v.data?.subject === routing);
}

chk('empty interest → General', validateContactPayload({
  _subject: 'Agentic QA enquiry', name: 'A', email: 'a@b.co', interest: '', profile: '', message: '', _honey: '',
}).data?.mailSubject === 'Website enquiry — General');

chk('CRLF in interest rejected', validateContactPayload({
  _subject: 'Agentic QA enquiry', name: 'A', email: 'a@b.co', interest: 'NEET\r\nBcc: x@y.z', _honey: '',
}).ok === false);

chk('CRLF in name rejected', validateContactPayload({
  _subject: 'Agentic QA enquiry', name: 'A\r\nX', email: 'a@b.co', interest: 'NEET Prep',
}).ok === false);

const meta = ALLOWED['CatalystAI NEET enquiry'];
chk('resolve allowlisted interest', resolveInterestLabel(meta, 'NEET Prep') === 'NEET Prep' || resolveInterestLabel(meta, 'NEET mocks') === 'NEET mocks');
chk('resolve unknown sanitized', resolveInterestLabel(meta, 'Something custom') === 'Something custom');

const fmt = formatEnquiryEmail({
  websiteLabel: 'CatalystAI NEET & JEE',
  name: 'A',
  email: 'a@b.co',
  interestLabel: 'NEET Prep',
  profile: 'Student',
  message: 'hi',
});
chk('sample subject NEET Prep', fmt.mailSubject === 'Website enquiry — NEET Prep');
chk('sample body shape', fmt.text === [
  'Website: CatalystAI NEET & JEE',
  'Name: A',
  'Email: a@b.co',
  'Interested in: NEET Prep',
  'Profile: Student',
  '',
  'Message:',
  'hi',
].join('\n'));

// Reply-To still visitor email in data
chk('visitor email preserved for Reply-To', validateContactPayload({
  _subject: 'Agentic QA enquiry', name: 'A', email: 'Visitor@Example.COM', interest: 'NEET Prep', _honey: '',
}).data?.email === 'visitor@example.com');

process.exit(fail ? 1 : 0);
