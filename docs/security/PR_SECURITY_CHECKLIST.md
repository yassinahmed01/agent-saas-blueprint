# PR Security Checklist

- No secrets, tokens, or credentials added.
- Auth/session changes reviewed for cookie flags, CSRF, and MFA requirements.
- Access control enforced on new routes and APIs.
- Inputs validated and outputs encoded where needed.
- Logging avoids PII/secrets and includes redaction where relevant.
- Dependencies pinned and major upgrades approved.
- New security-sensitive behavior has tests or documented manual checks.
