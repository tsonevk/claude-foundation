---
name: skillspector-audit
description: Run a bounded NVIDIA SkillSpector static audit across the Claude Foundation skill root, preserve raw evidence, and review exact triage fingerprints.
disable-model-invocation: true
---

# SkillSpector Audit

## Purpose
Run the repository's pinned per-skill SkillSpector workflow on explicit request and return reproducible security evidence while leaving skill source and triage decisions unchanged.

## When to use
- The user asks to scan one or more Claude Foundation skills with NVIDIA SkillSpector.
- A new or changed `SKILL.md` needs a pre-publish static audit.
- A SkillSpector CI report needs review, explanation, or comparison with the current exact-triage policy.
- The reviewed baseline may have drifted after a skill or scanner update.

## When not to use
- The task is a general repository security audit rather than a skill-package audit.
- The user only wants format and lifecycle validation; use `skill-comply` first.
- The request is routine skill execution with no audit intent.
- The available repository does not contain the local runner, triage policy, and Claude Foundation skill root.

## Required inputs
- An explicit repository root containing the SkillSpector workflow files.
- Audit scope: the full Claude Foundation skill root, or the skill paths to highlight in the full-root results.
- The repository's pinned SkillSpector revision from `.github/workflows/skillspector-audit.yml`.
- A writable evidence directory outside the active plugin source.
- An explicit choice for dependency setup when the pinned scanner is not already available.

## Codex workflow
1. Read the closest project authority and inspect these files before running commands:
   - `.github/workflows/skillspector-audit.yml`
   - `.github/scripts/run-skillspector-per-skill.py`
   - `.github/skillspector-triage-policy.json`
2. Resolve the foundation repository root from an explicit path. Confirm that the active root is `claude-foundation/plugins/claude-foundation/skills/` and that the runner and policy files exist.
3. Record the current commit and working-tree state so the evidence is tied to an identifiable source snapshot. An audit may inspect local changes, but the report must label the source as dirty when applicable.
4. Run the deterministic preflight checks:

   ```bash
   python3 .github/scripts/run-skillspector-per-skill.py --self-test
   python3 -m json.tool .github/skillspector-triage-policy.json >/dev/null
   skillspector --version
   ```

5. Use the existing scanner when it matches the repository contract. If the binary is missing, treat installation of the pinned revision as a separate bounded setup step and obtain explicit approval before changing the local Python environment.
6. Run the repository wrapper against the full active root, even when only one skill is requested. Exact triage fingerprints depend on paths relative to that root.

   ```bash
   python3 .github/scripts/run-skillspector-per-skill.py \
     --root claude-foundation/plugins/claude-foundation/skills \
     --output artifacts/skillspector \
     --triage-policy .github/skillspector-triage-policy.json \
     --workers 4 \
     --timeout-seconds 300
   ```

7. Read `summary.json` and `summary.md`, then inspect both the raw and triaged report for each requested skill. Keep the raw report unchanged.
8. Separate results into active findings, reviewed false positives, accepted residuals, and scanner or triage errors. An accepted residual remains visible evidence.
9. Rank active findings by severity and source reachability. Treat `CRITICAL` and `HIGH` as block candidates, `MEDIUM` as review-required, and `LOW` as an advisory note.
10. Propose minimal source changes separately from evidence. Apply source changes only when the user has requested an edit.
11. Propose a triage-policy change only after human review confirms the exact path, rule, finding, snippet hash, severity, and reason. Preserve the raw report that supports the decision.
12. Re-run the full-root audit after any approved source or policy change and compare the new summary with the previous evidence.

## Output contract
- Repository root, commit, and clean or dirty source state.
- Scanner version and repository pin.
- Skill count, scan count, and scanner error count.
- Raw finding counts by severity.
- Active findings by skill, rule, file, and severity.
- Reviewed false-positive and accepted-residual counts, with policy IDs.
- Evidence paths for `summary.json`, `summary.csv`, `summary.md`, raw reports, triaged reports, and logs.
- Minimal remediation proposals and a separate triage recommendation when relevant.
- Final verdict: `CLEAN`, `NOTE`, `REVIEW`, `BLOCK_CANDIDATE`, or `ERROR`.

## Verification
- The self-test and triage-policy JSON validation pass.
- Every discovered `SKILL.md` has either a report or an explicit scanner error.
- Raw reports and triaged reports are stored separately.
- The full active root is used, preserving relative-path fingerprint semantics.
- `summary.json`, `summary.csv`, and `summary.md` agree on scan and finding counts.
- No source file or triage entry changes during an audit-only run.
- A repeated run against the same source, scanner pin, and policy produces equivalent classification results.

## Safety boundaries
- Treat audit execution as evidence generation.
- Keep the repository pin authoritative; scanner upgrades are separate reviewed changes.
- Keep raw findings visible beside triaged findings.
- Keep triage entries exact and reviewable; broad rule suppression is outside this workflow.
- Stop and report dependency, policy, malformed-report, timeout, or scanner errors.
- Keep evidence free of exposed sensitive values and private runtime data.
- Apply remediation and triage edits only as separately scoped repository changes.

## Related skills
- `skill-comply`
- `skill-stocktake`
- `security-review`
- `verification-loop`

## Source attribution
- Based on NVIDIA SkillSpector as the upstream static skill scanner.
- Adapted to the repository's pinned static-only per-skill runner and exact reviewed-triage policy.
- Uses the existing CI evidence model rather than introducing a second scanner implementation.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- Project-specific guidance remains authoritative for repository commands and runtime behavior.
- Keep audit runs read-focused and evidence-first.
- Use fixed command arguments and repository-owned paths.
- Preserve rollback by keeping audit output outside active plugin source.
- No production, cloud, host, or external-system mutation belongs in this workflow.
- No triage-policy mutation is implied by a scanner finding.
