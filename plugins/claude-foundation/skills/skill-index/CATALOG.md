# claude-foundation skill catalog

GENERATED FILE — do not edit by hand. Regenerate with `python3 scripts/generate_skill_index.py --write`.

168 skills. **R** = routing tier (Claude sees the description and may invoke it automatically). **C:AUTO** = catalog tier, CATALOG_AUTO: not resident (`disable-model-invocation: true`, so Claude Code itself will not natively auto-invoke it), but skill-bank-router/skill-index MAY load its SKILL.md and apply it as router-selected guidance for a matching prompt. **C:MANUAL** = catalog tier, MANUAL_ONLY: our router must NOT auto-apply it — tell the user the explicit action/invocation required instead (`tiers.manual_only` in skill-metadata.json).

To use a CATALOG_AUTO (`[C:AUTO]`) skill, do either of these:

- read `skills/<dir>/SKILL.md` under the plugin directory and follow it, or
- tell the user to run `/claude-foundation:<name>`.

For a MANUAL_ONLY (`[C:MANUAL]`) skill, do NOT read/apply its SKILL.md as an automatic action from a matched prompt — tell the user which explicit invocation or workflow gate is required.

## iMX / CMS

- **adv3-cms-proxy-route-repair** [C:AUTO] — Diagnose and repair ADV3 dashboard/API failures caused by CMS-managed proxy route drift. Use when an ADV3 host loads `/ad-dashboard/login` but `/ad-rest-api/v1/etl-info` or `/ad-rest-api/v1/publication-info` returns `404`, when `proxy_adv3.conf` may have changed on host, or when CMS templates for `${AD_CLT}/config/httpd/docker/conf` must be inspected, corrected, deployed, and revalidated.
- **cms-safe-mutation-boundary** [C:AUTO] — Use this skill when designing or implementing bounded CMS mutation flows, especially readonly inspect, dry-run plan, explicit approval, precondition checks, approved mutation, audit trail, and rollback notes.
- **imx-backup-cloud-upload-diagnostic** [C:AUTO] — Use this skill when diagnosing iMX backup and cloud upload behavior, including OCI Object Storage uploads, rclone comparison, not_uploaded directories, upload logs, retry staging, and restore/upload instructions.
- **imx-certificate-runtime-review** [C:AUTO] — Review iMX certificate runtime state, expiry, trust, and binding evidence safely.
- **imx-cms-config-review** [C:AUTO] — Review iMX CMS configuration, variables, templates, and deployment diffs safely.
- **imx-containerization-guardrails** [R] — Review iMX containerization with strict read-first guardrails and bounded change scope, including Dockerfile, compose, and container runtime config, privilege boundaries, volume mounts, network settings, and evidence-preserving operations for iMX/Oracle workloads.
- **imx-containerization-safety-review** [C:AUTO] — DEPRECATED compatibility shim (legacy triggers retained): review iMX containerization choices for safe runtime, privilege, and evidence-preserving operations. Route this request to imx-containerization-guardrails.
- **imx-deployment-release-review** [C:AUTO] — Review iMX deployment and release plans, rollback paths, and promotion safety without changing runtime state.
- **imx-dr-parity-review** [C:AUTO] — Review iMX disaster-recovery parity, sync state, and promotion readiness safely.
- **imx-enterprise-app-runtime-review** [R] — Review iMX enterprise application runtime evidence for Oracle DB, WebLogic, Tomcat, and HTTPD without changing state.
- **imx-log-evidence-collection** [C:AUTO] — Collect and summarize iMX log evidence with minimal, redaction-safe scope.
- **imx-ops-readonly-diagnostic** [R] — Use this skill when diagnosing iMX operational issues in a safe readonly manner, including host and application health checks, symptom and health reviews, status checks, sensors, reports, logs, WebLogic and application runtime behavior, disabled background jobs, mail modules, Oracle/iMX context, and operator handoff summaries.
- **imx-ops-readonly-diagnostics** [C:AUTO] — DEPRECATED compatibility shim (legacy triggers retained): review iMX host and application health, logs, and symptoms without changing runtime state. Route this request to imx-ops-readonly-diagnostic.
- **imx-ops-runbook** [R] — Use when the task involves iMX operational management, reports, sensors, CMS variables, scheduling, log locations, or start/stop flows across Intranet, AD, and Extranet layers. Do not use for generic Linux work unrelated to iMX.
- **imx-orchestration-tower-review** [C:AUTO] — Review iMX Orchestration Tower jobs, schedules, and execution evidence safely.
- **imx-runtime-log-triage** [R] — Triage iMX runtime logs to isolate incidents without mutating production state.
- **imx-security-evidence-review** [C:AUTO] — Review iMX security evidence while preserving logs, traces, and operator handoff details.
- **imx-sensor-authoring** [C:AUTO] — Use this skill when creating, reviewing, or improving iMX sysadm sensors, including ksh scripts, metadata blocks, enable hooks, schedules, recipients, exit codes, and runtime logs.
- **imx-sensor-enable-hook-audit** [C:AUTO] — Use when an iMX sensor is unexpectedly reported as DISABLED and you need to audit the enable/disable path, especially `.enabled` hooks, lock files, sensor-specific disable flags, and config-to-env gaps before proposing the smallest safe operational fix.
- **imx-sensors-framework-review** [C:AUTO] — Review iMX sensors, reports, and runtime enablement safely.
- **imx-start-stop-guardrails** [C:AUTO] — Review iMX start, stop, restart, and shutdown safety with explicit confirmation.

## OCI

- **oci-cli-evidence-collection** [C:AUTO] — DEPRECATED compatibility shim (legacy triggers retained): collect deterministic read-only OCI CLI inventory and JSON evidence for diagnostics and handoff. Route this request to oci-evidence-collector.
- **oci-evidence-collector** [R] — Use this skill when preparing readonly OCI CLI evidence collection commands or scripts for AI-assisted diagnostics and handoff, including deterministic inventory and state capture that can be shared, replayed, or attached to a report, especially IPSec, DRG, VCN, route table, security list, load balancer, and compartment/region troubleshooting.
- **oci-iam-policy-review** [C:AUTO] — Review OCI IAM policies, dynamic groups, and compartment scope for least-privilege and operational safety.
- **oci-ipsec-tunnel-diagnostics** [C:AUTO] — Diagnose OCI IPSec tunnel state, IKE/BGP/static routing drift, and evidence for read-only investigations.
- **oci-network-security-review** [C:AUTO] — Review OCI network controls, segmentation, and exposure for security issues.
- **oci-network-segmentation-review** [C:AUTO] — Use this skill when reviewing OCI VCN/subnet/security-list/route-table designs for PROD/NON-PROD segregation, including Terraform export analysis, CIDR split impact, security list reorganization, and colleague handoff instructions.
- **oci-network-troubleshoot** [C:AUTO] — Use when investigating OCI connectivity issues involving load balancers, NSGs, security lists, route tables, private/public endpoints, ACL whitelisting, ICMP tests, curl reachability, or cross-network connectivity. Do not use for purely application-layer bugs with already confirmed network reachability.
- **oci-networking-diagnostics** [R] — Diagnose OCI VCN, subnet, route table, security list, NSG, DRG, LPG, VPN, and hybrid networking issues with read-only evidence.
- **oci-operations-review** [R] — Review OCI resource layout, tenancy scope, compartments, and regions with a read-first operations lens.
- **oci-security-evidence-review** [R] — Review OCI evidence artifacts, control mappings, and operational logs for security assurance.
- **oci-vault-key-rotation-review** [C:AUTO] — Review OCI vault key rotation plans for safety, evidence, and operational impact.

## AWS

- **auditing-aws-s3-bucket-permissions** [C:AUTO] — Systematically audit AWS S3 bucket permissions to identify publicly accessible buckets, overly permissive ACLs,
- **aws-iam-policy-review** [C:AUTO] — Review AWS IAM roles, policies, users, and trust relationships for least privilege and safe scope.
- **aws-networking-review** [C:AUTO] — Review AWS VPC networking, subnets, route tables, security groups, NACLs, VPN, and Transit Gateway state.
- **aws-operations-review** [C:AUTO] — Review AWS account and resource layout with a read-first operations lens.
- **aws-s3-storage-review** [C:AUTO] — Review AWS S3 bucket policy, public access, encryption, lifecycle, replication, and logging settings.

## Linux / RHEL

- **linux-ci-container-parity** [C:AUTO] — Keep container-related GitLab CI changes compatible with Linux runners and shell behavior.
- **linux-ci-parity** [C:AUTO] — Use this skill when Windows-local development must match Linux GitLab CI behavior, especially bash resolution, shell scripts, Python tests invoking sh or bash, path portability, and runner validation.
- **linux-container-host-ops** [C:AUTO] — Review Linux host-side container operations, storage, networking, and service support.
- **linux-networking-diagnostics** [C:AUTO] — Diagnose Linux host IP, routes, DNS, ports, sockets, and connectivity safely.
- **linux-package-patching-review** [C:AUTO] — Review dnf, yum, rpm, repos, patch windows, and reboot risk safely.
- **linux-selinux-firewall-review** [C:AUTO] — Review SELinux modes, AVCs, firewalld, iptables, and nftables safely.
- **linux-service-systemd-review** [C:AUTO] — Review systemd units, failed services, journalctl evidence, and timer safety.
- **linux-storage-filesystem-review** [C:AUTO] — Review disks, LVM, filesystems, mounts, fstab, inode, and capacity risk.
- **linux-system-diagnostics-review** [C:AUTO] — Review Linux host health, load, memory, processes, logs, and incident-style diagnostics.
- **linux-user-access-review** [C:AUTO] — Review Linux users, groups, sudo, SSH, permissions, and least privilege safely.
- **nginx-apache-haproxy-log-triage** [C:AUTO] — Triage Nginx, Apache, and HAProxy logs for suspicious requests and incident indicators.
- **rhel-oracle-linux-ops-review** [R] — Review Red Hat Enterprise Linux and Oracle Linux lifecycle, repos, subscriptions, kernels, and patch conventions.

## Containers / Docker / Podman

- **container-image-hardening** [R] — Review container image layers, package sets, runtime identity, and provenance controls for hardening opportunities.
- **container-log-weekly-archive** [C:AUTO] — Use when a containerized service writes many small log or temp files to a bind-mounted host directory and inode pressure must be reduced with container-side cleanup, weekly period-bounded archives, and delete-after-success retention.
- **container-runtime-diagnostics** [R] — Diagnose container runtime behavior from logs, mounts, health checks, launch definitions, and host evidence.
- **container-secrets-hygiene** [C:AUTO] — Review container workflows for secret handling, exposure, and leakage risks.
- **container-supply-chain-security** [C:AUTO] — Review container provenance, SBOM, signing, and image trust controls.
- **container-vulnerability-scanning** [C:AUTO] — Coordinate safe container vulnerability scans and triage the resulting findings.
- **docker-compose-review** [C:AUTO] — Review Docker Compose files for service wiring, ports, volumes, and runtime safety.
- **docker-compose-security-review** [C:AUTO] — Review Docker Compose files for privilege, exposure, secret, and network boundary issues.
- **docker-patterns** [R] — Use safe, reviewable Dockerfile and container patterns for build, run, image-size, and runtime hygiene work.
- **docker-to-kubernetes-migration** [C:AUTO] — Review Docker or Compose workloads for a bounded migration path to Kubernetes.
- **dockerfile-review** [C:AUTO] — Review Dockerfiles for safe, minimal, portable, and auditable changes.
- **helm-chart-review** [C:AUTO] — Review Helm charts, values, templates, and rendered output for safe defaults and release risk.
- **podman-rootless-security-review** [C:AUTO] — Review rootless Podman usage for capability, volume, and network safety.
- **podman-rootless-service** [C:AUTO] — Review or configure rootless Podman service wiring, user units, and socket activation.

## Kubernetes

- **auditing-kubernetes-cluster-rbac** [C:AUTO] — Auditing Kubernetes cluster RBAC configurations to identify overly permissive roles, wildcard permissions, dangerous
- **kubernetes-cluster-operations-review** [C:AUTO] — Diagnose Kubernetes runtime and rollout issues with read-only cluster evidence, targeted logs, and safe operational review.
- **kubernetes-manifest-review** [C:AUTO] — Review Kubernetes manifests for safety, coherence, and deployment-readiness before apply.
- **kubernetes-policy-and-access-review** [C:AUTO] — Review Kubernetes RBAC, service accounts, pod security, and admission policy for least privilege and safety.
- **managed-kubernetes-operations-review** [C:AUTO] — Review OKE and EKS managed Kubernetes operations, upgrades, and provider integration with read-only evidence.

## Terraform / IaC

- **auditing-terraform-infrastructure-for-security** [C:AUTO] — Auditing Terraform infrastructure-as-code for security misconfigurations using Checkov, tfsec, Terrascan, and
- **iac-ci-pipeline-review** [C:AUTO] — Review GitLab or Jenkins IaC validation pipelines, artifacts, plan retention, approvals, and protected variables.
- **iac-secrets-hygiene** [C:AUTO] — Review IaC secrets leakage across Terraform, Ansible, vars, tfvars, state, logs, and CI artifacts.
- **terraform-cloud-change-review** [C:AUTO] — Review Terraform cloud changes for destructive actions, drift, and rollback safety before apply.
- **terraform-module-review** [C:AUTO] — Review Terraform module structure, variables, outputs, providers, locals, and reuse safely.
- **terraform-plan-safety-review** [R] — Review Terraform plan/apply safety, replacements, destroys, lifecycle, dependencies, drift, and rollback.
- **terraform-provider-versioning** [C:AUTO] — Review Terraform provider versions, lock file safety, upgrade safety, and OpenTofu compatibility.
- **terraform-state-backend-review** [R] — Review Terraform state backend, locking, workspaces, tfstate secrets, import, move, and state rm risk.

## Ansible

- **ansible-ci-validation** [C:AUTO] — Validate Ansible with ansible-lint, syntax-check, check mode, molecule, and CI gating safely.
- **ansible-idempotency-safety** [C:AUTO] — Review Ansible idempotency, changed_when, failed_when, check_mode, handlers, and repeatability.
- **ansible-idempotent-change-check** [C:AUTO] — Verify current Ansible state before editing or reinstalling. Use when working on roles, playbooks, inventories, group vars, handlers, or package/service tasks and you need to confirm whether the requested change is already present before making a diff.
- **ansible-inventory-review** [C:AUTO] — Review Ansible inventory, group_vars, host_vars, environment separation, and host targeting.
- **ansible-linux-ops-guardrails** [C:AUTO] — Review Ansible-driven Linux, RHEL, and Oracle Linux package, service, file, cron, user, SELinux, and system operations safely.
- **ansible-playbook-review** [R] — Review Ansible playbooks, tasks, handlers, vars, templates, and execution safety with a read-first operations lens.
- **ansible-role-review** [R] — Review Ansible role structure, defaults, vars, tasks, handlers, templates, files, and meta for safe reuse.
- **ansible-secrets-hygiene** [C:AUTO] — Review Ansible Vault, secret vars, no_log usage, logs, artifacts, and credential handling safely.

## GitLab / CI-CD

- **agentic-ci-cd-guardrails** [C:AUTO] — Review and design defensive guardrails for AI-assisted CI/CD workflows that handle untrusted inputs, secrets, and deployment authority.
- **building-devsecops-pipeline-with-gitlab-ci** [C:AUTO] — Design and implement a comprehensive DevSecOps pipeline in GitLab CI/CD integrating SAST, DAST, container scanning,
- **ci-cd-pipeline-builder** [R] — Design or update CI/CD pipelines with explicit stages, checks, and deployment gates.
- **gitlab-ci-security-gates-review** [R] — Review GitLab CI gates for security checks, approval thresholds, and evidence capture.
- **gitlab-ci-trivy-daemonless** [C:AUTO] — Use when GitLab CI jobs fail because of Trivy version drift, mutable CI image tags, or Docker-in-Docker requirements on unprivileged runners.
- **gitlab-container-pipeline** [C:AUTO] — Review or shape GitLab CI jobs that build, scan, or publish container images.
- **gitlab-eol-guardrails** [C:AUTO] — Use when a GitLab repository needs LF line-ending guardrails for scripts or config files, especially when Web UI edits or pasted content can introduce CRLF (^M), and when the repo uses a shared CI include for versioning or release jobs.
- **gitlab-mr-security-validation** [C:AUTO] — Validate GitLab merge requests for security controls, evidence, and release gate readiness.
- **gitlab-runner-security-review** [C:AUTO] — Review GitLab runner posture, isolation, and secret handling for security risks.

## Security / audit / forensics

- **access-review-evidence-pack** [C:AUTO] — Prepare evidence packs for access reviews, recertifications, and least-privilege checks.
- **analyzing-cloud-storage-access-patterns** [C:AUTO] — Detect abnormal access patterns in AWS S3, GCS, and Azure Blob Storage by analyzing CloudTrail Data Events, GCS
- **analyzing-docker-container-forensics** [C:AUTO] — Investigate compromised Docker containers by analyzing images, layers, volumes, logs, and runtime artifacts to
- **analyzing-kubernetes-audit-logs** [C:AUTO] — Parses Kubernetes API server audit logs (JSON lines) to detect exec-into-pod, secret access, RBAC modifications,
- **analyzing-linux-audit-logs-for-intrusion** [C:AUTO] — Uses the Linux Audit framework (auditd) with ausearch and aureport utilities to detect intrusion attempts, unauthorized
- **analyzing-linux-system-artifacts** [C:AUTO] — Examine Linux system artifacts including auth logs, cron jobs, shell history, and system configuration to uncover
- **analyzing-network-traffic-for-incidents** [C:AUTO] — Analyzes network traffic captures and flow data to identify adversary activity during security incidents, including
- **analyzing-sbom-for-supply-chain-vulnerabilities** [C:AUTO] — Parses Software Bill of Materials (SBOM) in CycloneDX and SPDX JSON formats to identify supply chain vulnerabilities
- **analyzing-web-server-logs-for-intrusion** [C:AUTO] — Parse Apache and Nginx access logs to detect SQL injection attempts, local file inclusion, directory traversal,
- **audit-log-evidence-review** [C:AUTO] — Review audit log evidence for completeness, integrity, and incident relevance.
- **auditing-cloud-with-cis-benchmarks** [C:AUTO] — This skill details how to conduct cloud security audits using Center for Internet Security benchmarks for AWS,
- **detecting-ai-model-prompt-injection-attacks** [C:AUTO] — Detects prompt injection attacks targeting LLM-based applications using a multi-layered defense combining regex
- **detecting-typosquatting-packages-in-npm-pypi** [C:AUTO] — Detects typosquatting attacks in npm and PyPI package registries by analyzing package name similarity using
- **implementing-llm-guardrails-for-security** [C:AUTO] — Implements input and output validation guardrails for LLM-powered applications to prevent prompt injection,
- **mcp-security-review** [C:AUTO] — Review MCP server and connector exposure, permissions, and tool boundaries.
- **oracle-fmw-weblogic-security-review** [C:AUTO] — Review Oracle Fusion Middleware and WebLogic security posture, configuration, and evidence.
- **security-review** [R] — Review code, configs, prompts, or docs for security issues before commit or release.
- **security-scan** [R] — Do a narrow scan for secrets, risky settings, and exposed attack surface in repo files.
- **soc2-evidence-mapper** [C:AUTO] — Map system evidence to SOC 2 control expectations without inventing controls or evidence.

## Agents / prompts / AI

- **agent-hook-guardrails** [R] — Decide whether a repeated rule belongs in project guidance, a Claude Code hook, a repo-local check, or CI.
- **agent-permission-boundary-review** [C:AUTO] — Review Claude agent permissions, tool scopes, and data boundaries before deployment or reuse.
- **agent-result-contract** [R] — Apply the shared structured result envelope when subagents, loops, or automation return findings, so the parent thread can aggregate, retry, or escalate without guessing. Use when designing agent output, merging fan-out results, or classifying automation errors.
- **agentic-qa-evidence-loop** [C:AUTO] — Run a budget-aware post-change QA evidence loop with compact default validation, scenario setup, artifact capture, and pass/fail reporting.
- **ai-agent-tool-safety-review** [R] — Review Claude/LLM agent runtimes, tool workflows, and MCP gateways for unsafe actions, overbroad permissions, weak execution isolation, missing evidence, and prompt-to-tool abuse.
- **ai-instruction-curator** [C:AUTO] — Convert raw internet advice, posts, or AI workflow notes into durable, reusable project guidance without bloat.
- **ai-output-evaluation-review** [C:AUTO] — Review AI, LLM, and AgentOps outputs for rubric quality, regression risk, hallucination, and citation fidelity.
- **ai-usage** [R] — Analyze local Claude Code token usage and cost estimates with ccusage; workstation-local developer observability only, not billing authority or production telemetry.
- **blueprint-first-product-delivery** [C:AUTO] — Deliver a new app, dashboard, API, DevOps tool, MCP or agent gateway, or another major feature slice using a compact blueprint-first model with checked-in blueprint and implementation-plan docs. Use when the job is product-shaped and needs a thin verified vertical slice instead of ad hoc implementation.
- **claude-ci-review-gate** [C:AUTO] — Design or review a Claude-based CI code-review gate with an artifact-first, precision-first output contract. Use when adding Claude review to GitLab CI, Jenkins, or GitHub Actions pipelines, or when a review job produces noise, duplicates, or unverifiable findings.
- **claude-code-settings-hardening** [R] — Harden Claude Code settings and deterministic PreToolUse guards. Use for permission allow/deny/ask review, secret-path blocking, hook parity, and safe validation without reading protected files.
- **claude-plugin-adoption** [R] — Evaluate, adapt, or pilot Claude Code plugins, marketplaces, agent packs, and skill packs before adoption. Use when a task mentions Claude plugins, plugin marketplaces, external skill packs, agent packs, or installing/adapting third-party Claude Code workflow tools.
- **claude-plugin-authoring** [R] — Author, structure, and maintain a local Claude Code plugin — marketplace registration, plugin.json, skills, agents, skills-preload binding, skill-vs-agent decision criteria, legacy commands migration, auto-discovery, namespace scoping, and idempotent install.sh bootstrap.
- **context-budget-audit** [R] — Use when Claude Code sessions feel bloated and you want to audit global/project instructions, routing skills, subagent use, and tool-output patterns for avoidable context overhead.
- **deep-orchestration-mode** [C:AUTO] — Use a bounded scout-plan-slice-verify workflow for genuinely large, ambiguous, high-risk, explicitly parallelizable, recurring, or goal-driven Claude Code tasks.
- **documentation-lookup** [R] — Find and summarize authoritative docs, schemas, or repository guidance for the current task.
- **eight-rule-architecture** [C:AUTO] — Apply the reusable 8-rule working architecture for non-trivial repo tasks, with caution, surgical edits, read-before-write, checkpoints, context discipline, and loud failure reporting.
- **harness-driven-coding** [C:AUTO] — Turn any coding or config task into a bounded, evidence-backed change with an explicit harness (success criteria, validation commands, rollback path, iteration cap) before the first edit.
- **interaction-intake-contract** [R] — Classify ambiguous, high-risk, production-impacting, cross-domain, or genuinely multi-step requests before acting; define the target, success criteria, approval boundary, and next safe mode without adding ceremony to clear scoped tasks.
- **llm-cost-optimizer** [C:AUTO] — Reduce Claude Code token and model costs with measured prompt, routing, context, and validation changes.
- **manual-compact-handoff** [C:AUTO] — Use when a long-running Claude Code repository task needs durable, compact state for a future session without rereading the whole repository.
- **mcp-server-patterns** [C:AUTO] — Use authoritative MCP config, registry, and transport patterns for server and client work.
- **prompt-governance** [R] — Review reusable Claude Code prompts, skills, and instruction files for clarity, safety, trigger quality, authority boundaries, and testability.
- **prompt-quality** [R] — Turn vague AI requests into reliable, testable work instructions with explicit job, relevant context, output contract, and verification.
- **rag-knowledge-retrieval-review** [C:AUTO] — Review RAG and retrieval workflows for source authority, chunking, freshness, and citation quality.
- **search-first** [R] — Check authoritative repo docs and source files before guessing or improvising; stop as soon as the task has enough grounded context.
- **session-skill-harvester** [C:AUTO] — Scan the current session for reusable patterns, workflows, and non-obvious knowledge that could become skills. Always ends with a yes/no recommendation on whether to create a new skill. Use after any substantive session, or when the user asks "anything to add as a skill?", "skill suggestions", "harvest skills".
- **skill-bank-router** [R] — Route ambiguous tasks to the installed Claude Foundation catalog when the visible routing skills do not clearly fit, without loading the full skill library into every session.
- **skill-comply** [C:AUTO] — Check a Claude Foundation skill or instruction file against local format, lifecycle, routing, and safety rules.
- **skill-creator** [C:AUTO] — Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.
- **skill-scanner** [C:AUTO] — Pre-adoption security review for third-party or newly imported agent skills, including prompt injection, scripts, permissions, secrets, structural attacks, and supply-chain risk.
- **skill-stocktake** [C:AUTO] — Audit the Claude Foundation skill catalog for overlap, drift, weak scope, stale assumptions, or missing gaps.
- **strategic-compact** [C:AUTO] — Compress a complex request into a small actionable Claude Code brief with scope, risks, authoritative context, and verification.
- **verification-loop** [R] — Run the smallest useful verification sequence after a change and report residual risk clearly.

## Repo / code / workflow

- **building-incident-response-playbook** [C:AUTO] — Designs and documents structured incident response playbooks that define step-by-step procedures for specific
- **code-simplifier** [C:AUTO] — Simplify recently changed or explicitly requested code while preserving behavior, APIs, schemas, deployment semantics, security boundaries, and repository conventions. Use after an implementation or when the user explicitly asks for simplification/refactoring; keep scope bounded and validate after changes.
- **code-tour** [C:AUTO] — Create a guided repository tour from minimal verified context and selected file lines.
- **codebase-onboarding** [R] — Guide a minimal first-pass repository onboarding and context scan without broad, unnecessary reading.
- **git-worktree-manager** [C:AUTO] — Use git worktrees for isolated parallel work without branch collisions or dirty-state confusion.
- **jira-ai-investigation-brief** [C:AUTO] — Use this skill when converting Jira/Atlassian tasks into structured AI investigation briefs, DevOps analysis plans, colleague handoff instructions, and evidence collection checklists.
- **lb-incident-analysis** [C:AUTO] — Analyze load balancer incidents using logs, headers, and edge behavior evidence.
- **project-guidelines-template** [C:AUTO] — Use when a repository needs a project-specific onboarding or execution skill that captures architecture, file structure, validation paths, and operational guidance in one reusable template.
- **repo-health** [C:AUTO] — Run a periodic, read-only, deterministic-first repository maintainability health check to find growth, churn, complexity hotspots, and development-speed risks without broad LLM scanning or automatic refactoring.
- **repo-intake-scan** [C:AUTO] — Use when taking over or first inspecting a repository and you need a practical map of boundaries, source-of-truth files, risky areas, validation entrypoints, and reusable ideas.
- **repo-review** [R] — Review a repository before changing it so you do not duplicate, overwrite, or fight existing structure.
- **safe-change-implementation** [C:AUTO] — Use when the user asks for a minimal-risk code or configuration change that should preserve existing behavior as much as possible. Do not use when a full redesign is explicitly requested.
- **windows-devops-troubleshooter** [C:AUTO] — Use this skill when troubleshooting Windows-based DevOps tooling, including VS Code, PowerShell, Git Bash, OCI CLI, Python launcher issues, PATH problems, Claude Code workspace paths, Git remotes, and local repo hygiene.

## Other

- **bootstrap-ai-native-project** [C:AUTO] — Bootstrap or audit a repository's AI-assisted development governance — initialize project conventions, review whether CLAUDE.md/AGENTS.md/rules/skills/hooks are structured correctly, and add an intent/spec/plan/review lifecycle where size and risk justify it. Use when setting up a new project's standard Claude workflow or auditing an existing one for governance drift; not for an ordinary code change in an already-governed repo.
- **cloud-cost-risk-review** [C:AUTO] — Review cloud cost risk from idle, oversized, unattached, or duplicated resources with a read-first lens.
- **earnings-watch-report** [C:AUTO] — Use this skill when creating weekly upcoming earnings reports for the user's watchlist, especially EUR/European-listed instruments, AI/tech/pharma/industrial focus, and Trading 212 Invest planning.
- **engineering-reasoning-boundary** [R] — Preserve human engineering judgment on high-consequence work by switching from AI-first execution to reasoning-first analysis before mutation.
- **nvo-4th-grade-teacher-bg** [C:AUTO] — Use this skill when solving, explaining, or grading Bulgarian 4th-grade math/language tasks, NVO practice tests, and parent-friendly assessment reports.
- **portfolio-bucket-rebalance** [C:AUTO] — Use this skill when reviewing or correcting portfolio buckets, Google Sheets formulas, dashboard weights, asset classifications, and rebalance suggestions for the user's EUR-focused portfolio.
- **repository-context** [C:AUTO] — Package bounded, governance-aware repository context with Repomix for repo-wide orientation, architecture review, independent review, or handoff to another model; never use it by default for small/local changes.
- **skillspector-audit** [C:AUTO] — Run a bounded NVIDIA SkillSpector static audit across the Claude Foundation skill root, preserve raw evidence, and review exact triage fingerprints.
- **weekly-eur-stock-analyst** [C:AUTO] — Use this skill when preparing Bulgarian weekly stock/ETP analysis for EUR or European-listed instruments, including portfolio actions, anti-FOMO checks, leverage risk, earnings windows, swing options, and explicit direction.
