---
name: repository-context
description: Package bounded, governance-aware repository context with Repomix for repo-wide orientation, architecture review, independent review, or handoff to another model; never use it by default for small/local changes.
disable-model-invocation: true
---

# Repository Context

## Purpose
Produce a safe bounded repository context pack only when repo-wide context is genuinely more efficient than targeted reads.

## When to use
- Repo-wide orientation in a large unfamiliar repository.
- Architecture review spanning many modules.
- A bounded external/independent review needs a portable context artifact.
- Cross-cutting work would otherwise require many iterative reads.
- The user explicitly requests Repomix/context packaging.

## When not to use
- Small/local changes or a known scoped feature.
- A few targeted `Read`/`Grep`/`Glob` calls are enough.
- The repository has no reviewed packaging/exclusion policy and a safe bounded include set is not yet known.
- Production/customer/runtime data sits outside version control near the target.

## Workflow
1. Read project `CLAUDE.md` / `AGENTS.md` and relevant current-task/context docs first.
2. Inspect `.repomixignore`, Repomix config, `.gitignore`, and documented sensitive/runtime paths.
3. Prefer explicit bounded include/exclude scope over whole-repo packaging.
4. Never package `.env*`, credentials, keys/certs, cloud/Kubernetes configs, Terraform state, vault material, databases, runtime storage, customer dumps, logs, session state, or prior context outputs.
5. Use the smallest useful mode and pinned `repomix@1.18.0`.
6. Keep output local-only unless explicitly requested otherwise.

## Output contract
- Question the pack answers
- Mode/scope
- Include/exclude rules
- Local output lifecycle
- Pinned version/security-check status

## Safety boundaries
- No automatic packaging for local tasks.
- No sensitive/runtime material.
- No auto-commit/upload.
