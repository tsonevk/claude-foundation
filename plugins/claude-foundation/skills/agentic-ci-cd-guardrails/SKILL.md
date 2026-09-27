---
name: agentic-ci-cd-guardrails
description: Review and design defensive guardrails for AI-assisted CI/CD workflows that handle untrusted inputs, secrets, and deployment authority.
disable-model-invocation: true
---

# Agentic CI/CD Guardrails

## Purpose
- Review and design defensive guardrails for AI-assisted CI/CD workflows where agents, coding assistants, or LLM jobs interact with repositories, issues, merge requests, logs, artifacts, secrets, or deployment pipelines.
- Keep AI review useful while preventing the unsafe combination of untrusted input, sensitive credentials, and state-changing permissions.

## When to use
- The task involves AI or agent jobs in GitHub Actions, GitLab CI/CD, Jenkins, or similar automation.
- The workflow reads untrusted content such as issues, pull requests, merge requests, comments, commit messages, user-provided files, logs, or generated artifacts.
- The workflow may also have access to secrets, cloud credentials, SSH keys, CI_JOB_TOKEN, GITHUB_TOKEN, package publishing tokens, deployment permissions, or production environments.
- The user wants to add, review, or harden an AI-assisted CI/CD workflow.
- The task mentions agentic coding actions, Claude Code GitHub Action, Codex, GitHub Actions, GitLab CI, AI code review, automated PR/MR changes, or deployment agents.

## When not to use
- The task is only normal CI syntax troubleshooting without AI or agent involvement.
- The task is a general secrets-management review unrelated to CI/CD or agents.
- The task asks for unsafe access to credentials or instructions to weaken controls.
- The task requires production mutation before the trust boundaries and approvals are explicit.

## Read first
- `AGENTS.md`
- `README.md`
- `skills/USAGE.md`
- The workflow files in scope, for example `.github/workflows/*.yml`, `.gitlab-ci.yml`, `.gitlab/ci/*.yml`, `Jenkinsfile`, or pipeline templates
- Any repository docs describing environments, secrets, branch protection, deployment gates, runners, or release policy
- The relevant MR/PR, issue, or schedule context when provided

## Operating rules
- Treat issue text, PR/MR descriptions, comments, commit messages, user-provided files, logs, and artifacts as untrusted by default.
- Never combine untrusted input, secrets, and state-changing tools in the same AI job.
- Prefer read-only AI review jobs that produce review comments, patch artifacts, or draft changes.
- Keep deployment, cloud mutation, production rotation, publishing, and infrastructure changes deterministic and gated outside the AI job.
- Use least-privilege tokens and scoped credentials per environment, project, client, and workflow.
- Use protected branches, protected environments, manual approvals, and evidence gates for production.
- Redact secrets before AI review and avoid dumping environment variables, tokens, keys, certificates, wallets, kubeconfigs, or OCI config content.
- Prefer ephemeral runners or isolated jobs for untrusted review work.
- Treat broad token allowlists and shared global CI variables as high risk.

## Required inputs
- CI/CD platform and workflow path
- Which content is untrusted
- Which secrets or credentials are available to the job
- Whether the job can write to the repository, comment externally, publish artifacts, deploy, rotate keys, or mutate infrastructure
- Target environment and approval model, especially for production

## Codex workflow
1. Read the authoritative repo guidance and workflow files first.
2. Classify each relevant job as untrusted review, trusted validation, nonprod execution, or production execution.
3. Identify all trust-boundary crossings: untrusted content, secrets, write tokens, external communication, artifact publishing, and deployment authority.
4. Check whether AI jobs are read-only and secretless.
5. Check whether trusted execution jobs avoid untrusted prompt-controlled behavior.
6. Recommend the smallest safe change: split jobs, remove secrets from review jobs, downgrade token permissions, add protected environments, add manual gates, add artifact evidence, or move execution out of the AI job.
7. Provide validation and rollback guidance.

## Expected output
- A concise CI/CD trust-boundary review.
- A risk classification for each AI or agent-related job.
- Concrete guardrail changes with minimal blast radius.
- Clear distinction between review-only AI behavior and trusted execution.

## Output contract
- State whether the design is acceptable, constrained, risky, or blocked.
- List the exact workflow files and job names reviewed.
- List the untrusted inputs and sensitive capabilities found.
- Recommend one safe implementation path.
- Include validation and rollback steps.
- Separate evidence from inference.

## Validation guidance
- Confirm AI review jobs run without cloud credentials, SSH keys, package publishing tokens, or production secrets.
- Confirm AI review jobs cannot deploy, rotate keys, write production configs, or directly mutate infrastructure.
- Confirm production jobs use protected branches/environments and explicit approval or evidence gates.
- Confirm logs and artifacts are sanitized before AI processing.
- Confirm broad token allowlists, privileged runners, and unrestricted outbound actions are justified or removed.
- If files changed, run the repository's own validation/lint scripts plus any CI lint available in the target repo.

## Rollback guidance
- Revert the smallest workflow or template change first.
- Disable only the new AI review job if it causes noise or policy friction.
- Preserve existing trusted execution jobs unless they are demonstrably unsafe.
- Keep production execution disabled until guardrails are validated.

## Verification
- The review identifies all AI or agent CI jobs in scope.
- The review states whether each job has secrets, write authority, external communication, or deployment permissions.
- The proposed change prevents the unsafe combination of untrusted input plus secrets plus state-changing tools.
- The proposed change is additive and reversible.

## Safety boundaries
- No secret printing or disclosure.
- No production-impacting CI/CD mutation without explicit approval.
- No live cloud, Kubernetes, SSH, Vault, OCI, package publishing, or deployment action from an AI review job.
- No self-remediation outside an explicit, scoped approval.

## Related skills
- `detecting-ai-model-prompt-injection-attacks`
- `prompt-governance`
- `agentic-qa-evidence-loop`
- `gitlab-container-pipeline`
- `container-secrets-hygiene`
- `container-supply-chain-security`
- `claude-ci-review-gate`
- `deep-orchestration-mode`
- `security-review`

## Source attribution
- Adapted from defensive AI and agentic CI/CD guardrail patterns, including the Microsoft Security article on securing CI/CD in an agentic world and local GitLab/Codex/DevSecOps workflow requirements.

## Local policy overrides
- English only for code, docs, prompts, comments, commit messages, and technical artifacts.
- For repo work, obey `AGENTS.md` first.
- Prefer small, additive, reversible changes.
- Inspect before editing.
- Do not introduce new secrets or production authority.
- Keep AI jobs review-only unless the user explicitly approves a bounded non-production mutation.