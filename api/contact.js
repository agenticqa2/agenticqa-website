import nodemailer from 'nodemailer';
import { validateContactPayload } from './lib/contact-validate.js';
import { parseContactBody } from './lib/parse-body.js';

export const config = { maxDuration: 30 };

/** Best-effort in-memory rate limit (per instance). */
const hits = new Map();
const WINDOW_MS = 15 * 60 * 1000;
const MAX_HITS = 8;

function clientIp(req) {
  const xf = req.headers['x-forwarded-for'];
  if (typeof xf === 'string' && xf.length) return xf.split(',')[0].trim();
  return req.socket?.remoteAddress || 'unknown';
}

function rateLimit(ip) {
  const now = Date.now();
  let row = hits.get(ip);
  if (!row || now > row.reset) {
    row = { count: 0, reset: now + WINDOW_MS };
    hits.set(ip, row);
  }
  row.count += 1;
  return row.count <= MAX_HITS;
}

export default async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') {
    res.status(405).json({ success: 'false', message: 'Method not allowed.' });
    return;
  }
  if (!rateLimit(clientIp(req))) {
    res.status(429).json({ success: 'false', message: 'Too many requests. Please try again later or email admin@agenticqa.io.' });
    return;
  }

  let body;
  try {
    body = await parseContactBody(req);
  } catch (e) {
    const status = e?.status || 400;
    const message =
      status === 413
        ? 'Payload too large.'
        : status === 415
          ? 'Unsupported content type.'
          : 'Could not read form data.';
    res.status(status).json({ success: 'false', message });
    return;
  }

  const v = validateContactPayload(body);
  if (!v.ok) {
    res.status(v.status || 400).json({ success: 'false', message: v.message });
    return;
  }
  if (v.honeypot) {
    res.status(200).json({ success: 'true', message: 'OK' });
    return;
  }

  const user = process.env.SMTP_USER;
  const pass = process.env.SMTP_PASS;
  const mailTo = process.env.MAIL_TO || 'admin@agenticqa.io';
  const mailFrom = process.env.MAIL_FROM || user;
  const host = process.env.SMTP_HOST || 'smtp.titan.email';
  const port = Number(process.env.SMTP_PORT || 465);
  const secure = String(process.env.SMTP_SECURE || 'true') !== 'false';

  if (!user || !pass || !mailFrom) {
    res.status(503).json({
      success: 'false',
      message: 'Mail service is not configured yet. Please email admin@agenticqa.io directly.',
    });
    return;
  }

  const { subject, name, email, interest, profile, message, flow } = v.data;
  const text = [
    `Flow: ${flow}`,
    `Name: ${name}`,
    `Email: ${email}`,
    `Interest: ${interest || '(none)'}`,
    `Profile: ${profile || '(none)'}`,
    '',
    message || '(no message)',
  ].join('\n');

  try {
    const transporter = nodemailer.createTransport({
      host,
      port,
      secure,
      auth: { user, pass },
    });
    await transporter.sendMail({
      from: mailFrom,
      to: mailTo,
      replyTo: email,
      subject,
      text,
    });
    res.status(200).json({ success: 'true', message: 'The form was submitted successfully.' });
  } catch {
    res.status(502).json({
      success: 'false',
      message: 'Could not deliver the enquiry right now. Please email admin@agenticqa.io or try again later.',
    });
  }
}
