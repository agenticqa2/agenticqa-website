function classify(r) {
  return Promise.resolve(r)
    .then((res) => res.json().then((data) => ({ ok: res.ok, data: data || {} }), () => { throw new Error('bad-json'); }))
    .then((res) => (res.ok && String(res.data.success) === 'true' ? 'OK' : 'ERR'))
    .catch(() => 'ERR');
}
const mk = (ok, body, badJson = false) => ({
  ok,
  json: async () => { if (badJson) throw new SyntaxError('x'); return body; },
});
const cases = [
  ['success-true-bool', mk(true, { success: true }), 'OK'],
  ['success-true-str', mk(true, { success: 'true' }), 'OK'],
  ['success-false-bool', mk(true, { success: false, message: 'Activation' }), 'ERR'],
  ['success-false-str', mk(true, { success: 'false', message: 'This form needs Activation' }), 'ERR'],
  ['http-not-ok', mk(false, { success: 'true' }), 'ERR'],
  ['bad-json', mk(true, {}, true), 'ERR'],
];
let fail = 0;
for (const [n, r, exp] of cases) {
  const got = await classify(r);
  console.log((got === exp ? 'PASS' : 'FAIL') + '  ' + n + ' -> ' + got);
  if (got !== exp) fail++;
}
const net = await Promise.reject(new TypeError('Failed to fetch')).then(() => 'OK', () => 'ERR');
console.log((net === 'ERR' ? 'PASS' : 'FAIL') + '  network -> ' + net);
if (net !== 'ERR') fail++;
process.exit(fail ? 1 : 0);
