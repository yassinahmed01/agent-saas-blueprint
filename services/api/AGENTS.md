# API Agent — Scope & Standards

## Allowed
- /services/api/**
- /packages/shared/** (only if necessary)

## Forbidden
- /apps/web/**, /apps/mobile/**, /infra/** (unless explicitly required by task)

## Must-do checklist
- Validate inputs (never trust client)
- Explicit error handling; no silent failures
- Add/adjust tests for behavior changes
- Update API docs/spec if endpoints change
- No schema changes without Data/DB agent + ADR
