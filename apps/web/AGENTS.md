# Web Frontend Agent — Scope & Standards

## Allowed
- /apps/web/**
- /packages/shared/** (only if necessary for shared types/contracts)

## Forbidden
- /services/api/**, /apps/mobile/**, /infra/**, /.github/**

## Must-do checklist
- Keep UI accessible (keyboard + labels where relevant)
- No breaking API assumptions without an ADR + contract update
- Add/adjust UI tests if test framework exists
- Update docs for new user flows

## PR requirements
- Screenshots for UI changes (if applicable)
- How to test manually (steps)
