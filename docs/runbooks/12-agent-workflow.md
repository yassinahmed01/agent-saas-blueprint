# 12-Agent Workflow Runbook

Purpose: run a multi-agent epic safely with clear scope boundaries, small PRs, and reliable checks.

## Create the Epic and 12 agent-task issues

### GitHub UI
1) Create an Epic issue that describes outcomes, scope, risks, and cross-scope boundaries.
2) Create 12 agent-task issues, one per role. Use clear, scoped titles like:
   - `docs: add 12-agent workflow runbook`
   - `api: add billing retry guardrails`
3) Link each task issue to the Epic (tracked by or referenced in the Epic body).
4) Ensure each issue lists:
   - Scope folder(s)
   - Constraints
   - Tests expected
   - Definition of done

### GitHub CLI (gh)
1) Create the Epic:
   ```bash
   gh issue create --title "epic: <short name>" --body "Summary, scope, risks, checklist"
   ```
2) Create 12 task issues (repeat per agent role):
   ```bash
   gh issue create --title "docs: <task>" --body "Scope: docs/**\nConstraints: ...\nTests: ...\nDoD: ..."
   ```
3) Link tasks to the Epic by editing the Epic body to reference each task:
   ```bash
   gh issue edit <EPIC_NUMBER> --add-assignee @me --body "<epic body>\n- Closes #123\n- Closes #124"
   ```

## Branch naming

Format: `agent/<role>/<issue>-<slug>`

Examples:
- `agent/docs/006-runbook`
- `agent/api/214-rate-limit`
- `agent/web/331-onboarding-copy`

## How agents use AGENTS.md and prompts

1) Read the root `AGENTS.md` before coding.
2) Read the subsystem `AGENTS.md` for the folder you touch.
3) Read the role prompt: `prompts/roles/<role>.md`.
4) Obey scope boundaries:
   - Only edit files in your ownership scope.
   - Cross-scope changes require separate, scoped PRs.
   - Keep backward compatibility across scopes.

## PR workflow

1) Create a small PR focused on one issue.
2) Include `Closes #X` in the PR description.
3) Ensure required checks are green before review.
4) No direct pushes to `main`.
5) Keep PRs boring and minimal: no extra refactors or drive-by edits.

## Cross-scope changes

When a change touches multiple scopes:
1) Split the work into multiple PRs, one per scope.
2) Maintain backward compatibility between PRs.
3) Use ADRs when a change touches any forbidden areas in `AGENTS.md` or needs an architectural decision.

## Run an Epic checklist (start → merge → verify)

1) Define Epic scope, risks, and success criteria.
2) Create 12 scoped issues, one per agent role.
3) Assign owners and confirm scope boundaries.
4) Each agent creates a branch using the standard format.
5) Each agent produces a small PR with `Closes #X`.
6) Required checks pass; reviewers approve.
7) Merge PRs in a safe order, maintaining compatibility.
8) Verify the Epic outcomes (tests, smoke checks, docs).
9) Close the Epic and capture follow-ups or ADRs.
