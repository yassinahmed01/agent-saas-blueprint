# Role Prompts (12 agents)

These prompts are used to run a "10+ senior agent" workflow.

## Important
- Branch naming must be: agent/<role>/<ticket>-<slug>
- <role> must match one of:
  spec, architect, api, web, mobile, shared, devops, qa, security, observability, performance, docs

CI will fail PRs if the role edits out-of-scope files.

## Standard Output Requirements (every agent)
When you respond, include:
1) Plan (bullet steps)
2) Changes made (what files + why)
3) Commands run (with results)
4) Risks + mitigations
5) Rollback plan
6) Follow-ups (if any)

## Universal constraints
- Read root AGENTS.md and the folder AGENTS.md before work.
- Keep PRs small and scoped.
- Add/adjust tests for behavior changes.
- No new frameworks/deps without explicit justification.
