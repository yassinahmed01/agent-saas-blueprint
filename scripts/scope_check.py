import os
import subprocess
import sys

def sh(cmd: list[str]) -> str:
    return subprocess.check_output(cmd, text=True).strip()

role = os.getenv("AGENT_ROLE", "").strip().lower()
if not role:
    print("AGENT_ROLE not set; skipping scope check.")
    sys.exit(0)

ROLE_SCOPES = {
    # Implementation agents
    "web": ["apps/web/", "packages/shared/"],
    "mobile": ["apps/mobile/", "packages/shared/"],
    "api": ["services/api/", "packages/shared/"],
    "shared": ["packages/shared/"],
    "devops": ["infra/", ".github/", "scripts/"],
    "docs": ["docs/", "README.md", ".editorconfig", "AGENTS.md"],

    # Cross-cutting / review agents (typically read-only, but allow limited fixes)
    "qa": ["tests/", "playwright/", ".github/", "docs/", "README.md"],
    "security": ["services/", "apps/", "packages/", "infra/", ".github/", "scripts/", "docs/", "README.md"],
    "observability": ["services/", "infra/", "packages/shared/", "docs/"],
    "performance": ["services/", "apps/", "packages/", "docs/"],

    # Planning/architecture agents
    "spec": ["docs/", "README.md", "AGENTS.md"],
    "architect": ["docs/", "README.md", "AGENTS.md", "packages/shared/"],
}

allowed = ROLE_SCOPES.get(role)
if not allowed:
    print(f"Unknown AGENT_ROLE='{role}'. Allowed roles: {', '.join(sorted(ROLE_SCOPES))}")
    sys.exit(1)

# Determine merge base with main for PRs; fallback to HEAD~1 for local runs
try:
    base = sh(["git", "merge-base", "origin/main", "HEAD"])
except Exception:
    try:
        base = sh(["git", "rev-parse", "HEAD~1"])
    except Exception:
        base = sh(["git", "rev-parse", "HEAD"])

changed = sh(["git", "diff", "--name-only", f"{base}...HEAD"]).splitlines()
changed = [c for c in changed if c.strip()]

def in_scope(path: str) -> bool:
    for prefix in allowed:
        if prefix.endswith("/"):
            if path.startswith(prefix):
                return True
        else:
            if path == prefix:
                return True
    return False

out = [p for p in changed if not in_scope(p)]

if out:
    print(f"❌ Scope violation for role '{role}'. Out-of-scope files touched:")
    for p in out:
        print(" -", p)
    print("\nAllowed prefixes/files for this role:")
    for a in allowed:
        print(" -", a)
    sys.exit(2)

print(f"✅ Scope check passed for role '{role}'. Files changed: {len(changed)}")
