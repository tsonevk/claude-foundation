---
name: claude-ci-review-gate
description: Design or review a Claude-based CI code-review gate with an artifact-first, precision-first output contract. Use when adding Claude review to GitLab CI, Jenkins, or GitHub Actions pipelines, or when a review job produces noise, duplicates, or unverifiable findings.
disable-model-invocation: true
---

# Claude CI Review Gate

## Purpose
Design a precision-first Claude review gate for GitLab CI / Jenkins / GitHub Actions: a reviewer stage that only produces a validated artifact, and an optional, separately credentialed publisher stage — so a review job cannot mutate the target system or leak write authority.

## When to use
- Adding Claude review to a GitLab CI, Jenkins, or GitHub Actions pipeline.
- A review job produces noise, duplicates, style-only comments, or unverifiable findings.
- Deciding whether a Claude review signal is trustworthy enough to gate merges.

## When not to use
- Enforcing merge decisions before precision data exists on real MRs.
- Auto-remediation from the review job.
- Any design where the reviewer job would receive write-capable credentials of any class.

## Required inputs
- The pipeline platform and how secrets are supplied through its secret store.
- The diff/commit range to review and the source checkout path.
- The controlled rule/check catalog, if one exists, for `rule_id` values.

## Workflow

### Two-stage design

**Stage A — reviewer, first and default slice:**
- Uses only the minimum model-execution credential required to invoke Claude Code.
- The model credential comes from the CI secret store and stays out of logs, artifacts, reviewed commands, and untrusted repository content.
- Receives no SCM write token, cloud credential, deploy credential, package-publish credential, or external-system write identity.
- Uses a read-only checkout and performs no external write:
  - treat the source checkout as read-only;
  - write generated reports only to a separate CI artifact/output directory;
  - keep review output outside the checked-out repository tree.
- Runs headless with structured output.
- Writes only the validated JSON report and audit metadata as pipeline artifacts.
- Does not comment on the MR/PR, block merge, or modify code.

**Stage B — optional publisher, separate job:**
- Enable only after precision is measured on real MRs.
- Read the already validated JSON artifact only.
- Use a separate, narrowly scoped token whose sole permission is posting the summary comment or annotation.
- Provide no source-checkout, merge, push, deploy, or package-publish rights.
- Place the job behind an approval or policy gate.

### Canonical Stage A output schema

```yaml
# Human signal only; enforcement starts only after precision is measured.
decision: pass | warn | block_candidate

findings:
  - severity: critical | high | medium | low
    category: correctness | security | regression | test-gap
    file: ""
    line_start: null
    line_end: null
    symbol: ""
    evidence: ""
    confidence: high | medium | low
    rule_id: ""
    identity_basis:
      category: ""
      file: ""
      symbol: ""
      normalized_rule: ""

coverage:
  files_reviewed: []
  files_skipped: []
  checks_not_run: []

recommendation: ""
```

### Finding identity and deduplication
- Use `rule_id` from a controlled rule catalog whenever one exists. The pipeline identity digest is SHA-256 over `rule_id`, file, and symbol using a documented delimiter.
- For free-form findings, the pipeline computes a best-effort identity digest from category, file, symbol, and normalized rule text.
- Canonicalize case, whitespace, path separators, and empty/null symbols before hashing.
- On re-review after new commits, supply only the previous validated finding identifiers and ask for new or still-unresolved issues.
- The model supplies structured identity fields; the pipeline owns hashing and deduplication.

## Guardrails
- Exclude style-only comments.
- Require `file` plus either a line span or a `symbol`, together with evidence, for every finding.
- Use an independent reviewer pass; the generating session must not approve its own output.
- Treat malformed JSON as a pipeline parse failure.
- Store an audit artifact containing the command line, model/version, commit SHA, prompt/skill version, and validation evidence.
- Apply the trust boundaries from `agentic-ci-cd-guardrails`: isolated model authentication only, no target-system or publishing authority, and read-only handling of untrusted source content.

## Output contract
- One validated Stage A JSON report plus audit metadata.
- No MR/PR comment, merge decision, or code change from Stage A.

## Verification
- Validate emitted JSON against the Stage A schema.
- Confirm every finding has `file`, location or symbol, and evidence.
- Confirm the reviewer job carries no write-capable credential.
- Confirm the output directory is separate from the source checkout.

## Safety boundaries
- Keep the reviewer credential-minimal and read-only.
- Keep publishing in a separate optional job with narrow authority.
- Require measured precision before merge enforcement.
- Keep secrets out of prompts, logs, commands, and artifacts.
- Keep remediation outside the reviewer job.

## Related skills
- `agentic-ci-cd-guardrails`
- `agent-result-contract`
- `ai-output-evaluation-review`
- `verification-loop`

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- Obey project `CLAUDE.md` / `AGENTS.md`.
- Nonprod before prod.
- No secrets in prompts, logs, scripts, tickets, or repositories.
- No self-remediation outside explicit, scoped approval.
