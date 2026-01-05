# Agent SaaS Blueprint (10+ Agent-Ready)

This repo is designed for **10+ specialized agents** working safely in parallel.

## Rules
- PR-only changes (no direct commits to main)
- Small PRs (one purpose)
- Tests + docs required for behavior changes
- Scope boundaries are enforced

## Folder ownership (hard boundaries)
- apps/web        → Web Frontend Agent
- apps/mobile     → Mobile Agent
- services/api    → API Agent
- packages/shared → Shared/Contracts Agent
- infra           → DevOps Agent
- docs            → Docs/ADR Agents
- .github         → CI/DevOps Agent
- scripts         → DevOps/Tooling Agent

## Start here
- AGENTS.md (constitution)
- Each subsystem has its own AGENTS.md inside the folder
- CI smoke PR to register required checks.
