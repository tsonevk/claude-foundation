---
name: gitlab-ci-trivy-daemonless
description: Use when GitLab CI jobs fail because of Trivy version drift, mutable CI image tags, or Docker-in-Docker requirements on unprivileged runners.
disable-model-invocation: true
---

Stabilize GitLab CI with the smallest safe change, favoring pinned tool versions and daemonless registry operations.

## When to use
- The pipeline fails while pulling `:latest` tool images.
- Trivy flags stop working after a version pin.
- `docker:dind` fails with service health checks, mount permission errors, or missing privileged mode.
- Packaging jobs only need image retrieval or export, not an actual Docker daemon.

## Preferred approach
1. Inspect the current `.gitlab-ci.yml` and the exact failing log lines first.
2. Pin the CI tool image to a known version before changing command syntax.
3. Match the Trivy CLI flags to the pinned Trivy version.
4. Prefer remote registry scans or daemonless image export over `docker:dind`.
5. Keep artifact names stable unless the user explicitly approves a packaging format change.
6. Validate the YAML locally after edits.

## Trivy notes
- For Trivy `0.69.x`, prefer:
  - `trivy image --cache-dir .trivycache --download-db-only`
  - `trivy image ...` for the actual scan
- If scanning directly from a registry, choose the image source flag supported by the pinned version and verify it against the observed CLI help when needed.

## Packaging notes
- If the runner cannot support `docker:dind`, prefer daemonless tools such as `skopeo` or equivalent registry-native image export flows.
- Keep auth and insecure-registry flags scoped only to the images that require them.

## Output checklist
- target files
- exact changes
- validation commands
- rollback approach
- open risks or assumptions
