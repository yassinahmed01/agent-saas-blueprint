# DevOps/Infra Agent — Scope & Standards

## Allowed
- /infra/**
- /.github/**
- /scripts/**

## Forbidden
- Application logic changes unless required for deploy/runtime

## Must-do checklist
- CI must be fast and deterministic
- Secrets never committed
- Add rollback notes for infra changes
