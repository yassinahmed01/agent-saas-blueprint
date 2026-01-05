# AGENTS.md — Engineering Constitution

## Safety rails (never violate)
Forbidden without explicit approval (ADR + plan):
- Auth/session handling
- Payments/billing
- DB schema changes impacting production data
- Public API breaking changes
- Security middleware / routing core
- Secrets/keys/encryption logic

Never do:
- No repo-wide refactors “for style”
- No new frameworks/deps without justification
- No silent env/config format changes
- No deleting features unless asked

## Scope boundaries (hard rule)
You may only modify files within your ownership scope.
Cross-scope work must be split into scoped PRs and keep backward compatibility.

## Quality bar
- Clear, boring code > clever code
- Explicit input validation + error handling
- No logging secrets/PII
- Add tests for behavior changes
- Update docs for developer/user-facing changes

## PR standards
PR description must include:
- Summary (what/why)
- Scope (folders touched)
- Risk (what could break)
- Tests (what ran + what added)
- Rollback plan

Branch naming:
- agent/<role>/<ticket>-<slug>
