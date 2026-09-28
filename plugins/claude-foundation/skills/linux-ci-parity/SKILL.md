---
name: linux-ci-parity
description: Use this skill when Windows-local development must match Linux GitLab CI behavior, especially bash resolution, shell scripts, Python tests invoking sh or bash, path portability, and runner validation.
disable-model-invocation: true
---

# Linux CI Parity

## Workflow
1. Read repository CI/test contracts and identify the Linux runner behavior that is authoritative.
2. Inspect shell invocation, line endings, paths, executability, environment assumptions, and Python subprocess usage.
3. Avoid hardcoded Windows tool paths in committed code/tests.
4. Make the smallest portability change.
5. Validate with Linux-compatible syntax/tests; do not declare success from Windows-only behavior.
