# ADR-0002: Cross-Scope Change Protocol (Contracts + Compatibility)

## Status
Accepted

## Context
Changes that touch multiple scopes can break consumers or create conflicting edits. We need a standard protocol for contracts and compatibility.

## Decision
A change is "cross-scope" when it modifies files in more than one ownership scope or requires consumers in another scope to adjust behavior.

Required process:
- Split PRs by scope.
- Keep backward compatibility for all contracts.
- Use a staged rollout sequence: shared contracts first, then consumer updates.
- Use semantic versioning or contract versioning for shared packages and APIs, even if initially minimal (e.g., patch/minor for backward-compatible changes).

An ADR is mandatory for: auth/session handling, payments/billing, DB schema changes impacting production data, public API breaking changes, security middleware/routing core, and secrets/keys/encryption logic.

Rollback patterns:
- Revert consumers to previous contract version.
- Keep old endpoints/types until all consumers migrate.
- Feature flag new behavior where practical.

## Alternatives considered
- Allow cross-scope edits in a single PR.
- Rely on ad-hoc coordination without versioning.

## Consequences
- More coordination overhead.
- Reduced integration risk and clearer compatibility guarantees.

## Rollout plan
- Document protocol in this ADR and the ADR README.
- Align future shared contract changes to staged rollouts.

## Rollback plan
- Revert staged PRs in reverse order.
- Restore previous contract version in packages/shared or APIs.
