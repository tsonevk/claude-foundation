---
name: gitlab-ci-security-gates-review
description: Review GitLab CI gates for security checks, approval thresholds, and evidence capture.
---

# GitLab CI Security Gates Review

## Workflow
1. Read project CI authority and the relevant `.gitlab-ci.yml` / included templates.
2. Trace security jobs, artifacts, allow-failure behavior, branch/environment rules, and approval gates.
3. Separate advisory checks from actual release blockers.
4. Identify gaps that could silently bypass required security evidence.
5. Recommend the smallest pipeline-native correction and validate syntax/config where possible.

## Output contract
- CI files/gates reviewed
- Findings and bypass risk
- Evidence/artifact gaps
- Minimal change
- Validation and rollback

## Safety boundaries
- Do not widen runner/deploy permissions.
- Do not expose protected variables or secrets.
- No pipeline push/deploy unless explicitly requested.
