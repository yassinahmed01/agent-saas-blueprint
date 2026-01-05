# ADR-0001: Repo Boundaries & Ownership

## Status
Accepted

## Context
We need clear, enforceable ownership boundaries so multiple agents can work in parallel without unintended cross-scope edits.

## Decision
Adopt a folder ownership model with explicit scopes:
- apps/web
- apps/mobile
- services/api
- packages/shared
- infra
- docs
- .github
- scripts

Agents may only modify files within their assigned scope. Cross-scope changes are not allowed in a single PR and must follow the cross-scope protocol.

CI enforces scope boundaries at a high level by validating file paths touched in a PR against the declared scope for that change.

## Alternatives considered
- No explicit scope ownership, relying on code review.
- Broad ownership for all agents.

## Consequences
- Slower cross-cutting changes due to split PRs.
- Safer parallelism and lower risk of accidental scope violations.

## Rollout plan
- Document scopes in this ADR and the ADR README.
- Communicate scope rules in agent instructions.

## Rollback plan
- Remove CI scope checks and revert to review-only enforcement.
