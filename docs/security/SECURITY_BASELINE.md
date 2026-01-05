# Security Baseline

## Secrets policy
- Never commit secrets, tokens, private keys, or credentials to the repo.
- Use environment variables for all secrets; keep `.env` files out of git.
- Provide `.env.example` with placeholder values only.
- Rotate secrets on employee offboarding, breach suspicion, or vendor compromise.
- Scope secrets to the minimum required privileges and environments.

## Auth/session checklist
- Use secure, HTTP-only cookies for session identifiers.
- Set `Secure`, `HttpOnly`, and `SameSite=Lax` (or `Strict` where safe) on auth cookies.
- Store tokens in server-side sessions or secure cookies; avoid localStorage for auth.
- Enforce CSRF protection on state-changing routes when using cookies.
- Require MFA for admin and privileged access paths.
- Use short-lived access tokens with refresh rotation when applicable.

## Logging rules
- Do not log secrets, tokens, passwords, or full credentials.
- Do not log PII unless necessary; use redaction.
- Redaction examples:
  - Replace `Authorization: Bearer <token>` with `Authorization: Bearer [REDACTED]`.
  - Mask emails as `user@example.com` -> `u***@example.com`.
  - Truncate IDs to last 4 characters when possible.
- Log only what is needed for debugging and audits.

## Dependency policy
- Pin direct dependencies to exact versions where possible.
- Review and update dependencies on a fixed cadence (at least monthly).
- Security patches may be fast-tracked outside the cadence.
- Major upgrades require approval from the owning agent and a security review.
- Track licenses for new dependencies and ensure compatibility.

## Minimal incident response steps
- Revoke and rotate affected keys or tokens immediately.
- Identify blast radius: affected services, data, and users.
- Remove leaked secrets from all logs and artifacts if possible.
- Audit recent access for suspicious activity and preserve evidence.
- Notify stakeholders and update runbooks with lessons learned.
