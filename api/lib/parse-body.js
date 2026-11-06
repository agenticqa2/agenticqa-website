import Busboy from 'busboy';

const MAX_BODY = 64 * 1024; // 64 KiB total
const MAX_FIELD = 8 * 1024;
const MAX_FIELDS = 20;

function contentType(req) {
  return String(req.headers?.['content-type'] || req.headers?.['Content-Type'] || '');
}

/** Collect raw body bytes from a stream or Buffer, with size cap. */
function collectRaw(req) {
  if (Buffer.isBuffer(req.body)) return Promise.resolve(req.body);
  if (typeof req.body === 'string') return Promise.resolve(Buffer.from(req.body));
  return new Promise((resolve, reject) => {
    const chunks = [];
    let size = 0;
    let done = false;
    const fail = (err) => {
      if (done) return;
      done = true;
      reject(err);
    };
    req.on('data', (c) => {
      size += c.length;
      if (size > MAX_BODY) return fail(Object.assign(new Error('payload too large'), { status: 413 }));
      chunks.push(c);
    });
    req.on('end', () => {
      if (done) return;
      done = true;
      resolve(Buffer.concat(chunks));
    });
    req.on('error', fail);
  });
}

function parseUrlencoded(buf) {
  const out = {};
  for (const [k, v] of new URLSearchParams(buf.toString('utf8'))) out[k] = v;
  return out;
}

function parseMultipart(buf, ct) {
  return new Promise((resolve, reject) => {
    const out = {};
    let fields = 0;
    let rejected = false;
    let bb;
    try {
      bb = Busboy({
        headers: { 'content-type': ct },
        limits: { fields: MAX_FIELDS, fieldSize: MAX_FIELD, files: 0, fileSize: 0 },
      });
    } catch (e) {
      return reject(Object.assign(new Error('malformed multipart'), { status: 400 }));
    }
    const rejectFiles = () => {
      if (rejected) return;
      rejected = true;
      reject(Object.assign(new Error('files not allowed'), { status: 400 }));
    };
    bb.on('file', (_n, stream) => {
      stream.resume();
      rejectFiles();
    });
    bb.on('filesLimit', rejectFiles);
    bb.on('field', (name, val) => {
      fields += 1;
      if (fields > MAX_FIELDS) {
        rejected = true;
        reject(Object.assign(new Error('too many fields'), { status: 400 }));
        return;
      }
      out[name] = val;
    });
    bb.on('error', (e) => {
      if (!rejected) reject(Object.assign(e || new Error('malformed multipart'), { status: 400 }));
    });
    bb.on('finish', () => {
      if (!rejected) resolve(out);
    });
    bb.end(buf);
  });
}

/**
 * Parse POST body for /api/contact.
 * Accepts: already-parsed object, JSON, urlencoded, multipart fields-only.
 */
export async function parseContactBody(req) {
  const ct = contentType(req);
  // Vercel / frameworks may already parse JSON/urlencoded into an object
  if (req.body && typeof req.body === 'object' && !Buffer.isBuffer(req.body) && !Array.isArray(req.body)) {
    return { ...req.body };
  }

  const buf = await collectRaw(req);
  if (!buf.length) return {};

  if (ct.includes('application/json')) {
    try {
      const parsed = JSON.parse(buf.toString('utf8'));
      if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) {
        const err = new Error('invalid json');
        err.status = 400;
        throw err;
      }
      return parsed;
    } catch (e) {
      if (e.status) throw e;
      const err = new Error('invalid json');
      err.status = 400;
      throw err;
    }
  }
  if (ct.includes('application/x-www-form-urlencoded')) return parseUrlencoded(buf);
  if (ct.includes('multipart/form-data')) return parseMultipart(buf, ct);

  const err = new Error('unsupported content type');
  err.status = 415;
  throw err;
}

export const PARSE_LIMITS = { MAX_BODY, MAX_FIELD, MAX_FIELDS };
