# Architecture Decision Records (ADRs)

## How to write ADRs
- Keep them short and specific.
- Use the template in `docs/adr/0000-template.md`.
- Capture context, decision, consequences, and rollout/rollback plans.

## Naming rules
- Use `ADR-XXXX-short-title.md` with a zero-padded number.
- Increment numbers sequentially.

## When ADRs are required
- Auth/session handling
- Payments/billing
- DB schema changes impacting production data
- Public API breaking changes
- Security middleware/routing core
- Secrets/keys/encryption logic
- Cross-scope changes affecting contracts or compatibility
