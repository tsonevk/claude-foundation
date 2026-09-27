---
name: harness-driven-coding
description: Turn any coding or config task into a bounded, evidence-backed change with an explicit harness (success criteria, validation commands, rollback path, iteration cap) before the first edit.
disable-model-invocation: true
---

# Harness-Driven Coding

## Purpose
Prevent speculative edits, scope creep, and unverifiable changes by requiring an explicit harness — target, success criteria, validation commands, rollback path, and iteration cap — before touching any file.

## When to use
- Any non-trivial code or config change where failure is hard to detect at a glance.
- Changes to shell hooks, CI pipelines, IaC, Ansible playbooks, Kubernetes manifests, or Terraform.
- Multi-file or multi-step changes in unfamiliar repos.
- Tasks where the user says "be careful", "don't break anything", or "minimal change".
- When the task spec is ambiguous and scoping it first will save multiple round trips.

## When not to use
- Trivial single-file typo fixes or doc-only edits where the diff is self-verifying.
- Pure exploration with no intended write.
- When the user explicitly asks to skip the harness.

## Workflow

### 1 — Inspect authoritative context first (no edits yet)

Read in this order, stopping when the answer is obvious:

| Source | What to read |
|--------|--------------|
| Project authority | `CLAUDE.md`, `AGENTS.md`, `README.md` |
| Compact handoff | `docs/activeContext.md`, `docs/currentTask.md`, `docs/decision-log.md` |
| Tests & CI | test files, `.gitlab-ci.yml`, `.github/workflows/`, `Makefile`, `tox.ini`, `pytest.ini` |
| Configs & schemas | `docker-compose.yml`, `ansible.cfg`, `terraform.tfvars`, `*.schema.json` |
| Target file | the file(s) the task will touch |

State what you found and what remains unknown before moving to step 2.

### 2 — Define the harness before the first edit

Write out briefly:

- **Target:** which file(s) change, which lines or blocks
- **Success criteria:** the observable outcome that proves the change works
- **Expected files changed:** complete list; flag any surprises
- **Validation commands:** ordered cheapest-first (examples below)
- **Rollback path:** `git checkout -- <file>` or equivalent
- **Risks:** what could break, what is deliberately out of scope
- **Iteration cap:** max N attempts (default 3) before stopping and reporting

Do not touch any file until the harness is defined.

### 3 — Make the smallest useful change

Edit only the files in the expected-files list. One logical change per commit. Prefer config-level extension over code surgery.

### 4 — Validate using the narrowest meaningful check

Run validation in cost order:

| Domain | Commands (cheapest first) |
|--------|--------------------------|
| **Git** | `git status --short` · `git diff --check` |
| **Python** | `python3 -m py_compile <file>` · `python3 -m json.tool <file>` |
| **Shell** | `bash -n <script>` |
| **Docker Compose** | `docker compose config` |
| **Ansible** | `ansible-playbook --syntax-check` → `--check` only on a safe host |
| **Terraform** | `terraform fmt -check` → `terraform validate` → `terraform plan` (read-only) |
| **Kubernetes** | `kubectl apply --dry-run=server` · `kubectl diff` |
| **CI** | Inspect the pipeline file; propose the smallest job change; do not push |

Stop at the first clear failure. Report the failing check and its output, not a guess about root cause.

### 5 — Stop after the iteration cap or first unclear failure

If the iteration cap is reached or a validation step fails in a way that is not immediately diagnosable:
- Revert the change (`git checkout -- <file>`).
- Report: what was attempted, which check failed, exact error output.
- Propose the next safe action; do not invent a workaround without user approval.

### 6 — Report evidence and next safe action

Final response must include:
- Files changed (exact list)
- Validation commands run and their output or verdict
- What was not verified and why
- Risks or open questions
- Rollback command
- Next safe action

## Safety boundaries
- Protected secret and credential classes defined by the repository's deny policy must never be read, edited, printed, copied, or included in logs. Treat policy entries as patterns, not inspection targets.
- Production deploys, service restarts, and cloud applies require explicit per-action confirmation.
- IAM, policy, state, and credential changes require explicit confirmation.
- Broad refactors require an explicit user request.
- Work remains foreground, bounded, and reviewable; detached execution is outside scope.
- Success claims require an executed check that proves the result.

## Related skills
- `search-first` — evidence-first preflight before any edit
- `verification-loop` — post-change check sequence and readiness verdict
- `safe-change-implementation` — minimal-risk change mechanics
- `security-review` — security-specific validation pass
- `repo-intake-scan` — full repo orientation when the codebase is unfamiliar

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- Linux / GitLab-CI parity is the source of truth for shell and CI validation, even when editing on Windows.
- For iMX work, use iMX-native ksh and Oracle context; avoid generic `sudo` or `systemctl`; whole-instance stop requires explicit reconfirmation.
- For OCI diagnostics, default to read-only evidence collection and deterministic reporting.
- Commit and push only when explicitly asked. Commit only relevant files; never commit secrets or scratch noise.
