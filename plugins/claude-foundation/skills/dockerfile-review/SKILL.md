---
name: dockerfile-review
description: Review Dockerfiles for safe, minimal, portable, and auditable changes.
disable-model-invocation: true
---

# Dockerfile Review

## Workflow
1. Read project authority, the Dockerfile, and the build/CI files that consume it.
2. Check base image, stages, package installation, cache ordering, user, entrypoint/cmd, copied files, and secret exposure.
3. Identify the smallest concrete issue; avoid style-only churn.
4. Propose or apply only the bounded change requested.
5. Validate parsing/build path using existing repository tooling.

## Output contract
- File(s) reviewed
- Concrete issue or acceptable-as-is verdict
- Exact fix when needed
- Validation command/result
- Risks/rollback

## Safety boundaries
- No baked secrets.
- No unnecessary privileges.
- No deployment automation expansion.
