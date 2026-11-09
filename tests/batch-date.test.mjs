import {
  nextBatchDate,
  formatBatchDate,
  batchDaysInMonth,
  lastDayOfMonth,
  todayFromSearch
} from '../assets/js/batch-date.js';

let fail = 0;
function chk(name, cond) {
  console.log((cond ? 'PASS' : 'FAIL') + '  ' + name);
  if (!cond) fail++;
}

function expect(today, shown) {
  const got = nextBatchDate(today);
  const label = formatBatchDate(got);
  const ok = got === shown;
  chk(`today ${today} -> ${formatBatchDate(shown)} (got ${label})`, ok);
}

// Brief examples
expect('2026-11-14', '2026-11-15');
expect('2026-11-15', '2026-11-30');
expect('2026-11-29', '2026-11-30');
expect('2026-11-30', '2026-12-15');
expect('2026-12-30', '2027-01-15');
expect('2026-12-31', '2027-01-15');
expect('2027-01-31', '2027-02-15');
expect('2027-02-15', '2027-02-28');
expect('2027-02-28', '2027-03-15');
expect('2028-02-15', '2028-02-29'); // leap year
expect('2026-03-30', '2026-04-15'); // 31-day month: 31st -> next 15th
expect('2026-03-31', '2026-04-15');

// Extra boundaries
expect('2026-11-09', '2026-11-15');
expect('2027-02-14', '2027-02-15');
expect('2027-02-27', '2027-02-28');
expect('2028-02-28', '2028-02-29');
expect('2028-02-29', '2028-03-15');
expect('2026-04-15', '2026-04-30');
expect('2026-04-30', '2026-05-15');

chk('Feb 2027 last day 28', lastDayOfMonth(2027, 2) === 28);
chk('Feb 2028 last day 29', lastDayOfMonth(2028, 2) === 29);
chk('batchDays Feb 2027', JSON.stringify(batchDaysInMonth(2027, 2)) === JSON.stringify([15, 28]));
chk('batchDays Feb 2028', JSON.stringify(batchDaysInMonth(2028, 2)) === JSON.stringify([15, 29]));
chk('batchDays Nov', JSON.stringify(batchDaysInMonth(2026, 11)) === JSON.stringify([15, 30]));

chk('format 30 Nov 2026', formatBatchDate('2026-11-30') === '30 Nov 2026');
chk('format 15 Jan 2027', formatBatchDate('2027-01-15') === '15 Jan 2027');
chk('format 28 Feb 2027', formatBatchDate('2027-02-28') === '28 Feb 2027');
chk('format 29 Feb 2028', formatBatchDate('2028-02-29') === '29 Feb 2028');

chk('todayFromSearch ?today=', todayFromSearch('?today=2026-11-15') === '2026-11-15');
chk('todayFromSearch with site=', todayFromSearch('?site=playwrightai&today=2026-11-30') === '2026-11-30');
chk('todayFromSearch none', todayFromSearch('?site=playwrightai') === null);
chk('todayFromSearch rejects junk', todayFromSearch('?today=15-11-2026') === null);

if (fail) {
  console.log('RESULT  ' + fail + ' failed');
  process.exit(1);
}
console.log('RESULT  all batch-date checks passed');
