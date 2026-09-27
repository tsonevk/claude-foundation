---
name: ai-output-evaluation-review
description: Review AI, LLM, and AgentOps outputs for rubric quality, regression risk, hallucination, and citation fidelity.
disable-model-invocation: true
---

# AI Output Evaluation Review

## Purpose
- Review AI, LLM, and AgentOps outputs for rubric quality, regression risk, hallucination, and citation fidelity.

## When to use
- You need a bounded review of model output quality, acceptance criteria, or regression risk.
- The task is about comparing outputs to a rubric, baseline, or golden set.
- You need to check hallucinations, missing citations, or repeated failure modes.

## When not to use
- The task is pure prompt drafting with no output to evaluate.
- A narrower active skill already covers the exact review need.
- The work would require hidden scoring, live mutation, or production impact.

## Read first
- `AGENTS.md`
- `README.md`
- The prompt, rubric, or acceptance criteria being used
- Representative outputs, traces, or test artifacts

## Operating rules
- Keep the review evidence-based and reproducible.
- Separate observed output from inference about quality.
- Prefer the smallest useful sample or golden set.
- Call out rubric gaps before recommending a broader change.

## Required inputs
- Target repo, artifact, or output set
- The rubric, test oracle, or acceptance criteria
- Any baseline or expected output examples

## Codex workflow
1. Read the authoritative files first.
2. Identify the rubric or derive one from the stated requirements.
3. Compare outputs against the rubric and baseline.
4. Note regressions, hallucinations, citation issues, or missing coverage.
5. Recommend the smallest safe next step.

## Expected output
- A concise verdict on output quality.
- The criteria that passed and failed.
- The evidence reviewed and the main regression risks.

## Output contract
- State whether the output meets the current rubric.
- List the specific failure modes or quality gaps.
- Distinguish facts from interpretation.
- Recommend the smallest safe follow-up.

## Validation guidance
- Compare against a golden set, fixture, or explicit rubric.
- Re-run the narrowest useful evaluation if a result is unclear.
- Confirm the evaluation is repeatable with the same inputs.

## Rollback guidance
- Restore the previous rubric, prompt, or evaluation gate if the new check is noisy or unstable.
- Revert any automation that blocks valid outputs until the rubric is fixed.

## Verification
- The reviewed artifacts exist and match the scope.
- The answer names the evaluation criteria used.
- The answer separates evidence from inference.

## Safety boundaries
- Do not hide uncertainty behind a numeric score without a rubric.
- Do not expose secrets, hidden prompts, or private data.
- Do not turn review into autonomous mutation or deployment.

## Related skills
- `prompt-governance`
- `verification-loop`
- `deep-orchestration-mode`
- `llm-cost-optimizer`

For skill/agent ROUTING evaluation fixtures, see repo-root `evals/`.

## Source attribution
- No exact upstream match. Adapted from local AI evaluation and workflow review patterns.

## Local policy overrides
- English only for code, docs, prompts, comments, and commit messages.
- Before large tasks, create or update `docs/activeContext.md`, `docs/currentTask.md`, and `docs/decision-log.md`.
- For repo work, obey `AGENTS.md` first.
- For iMX work, use iMX-native ksh and Oracle context; avoid generic `sudo` or `systemctl` guidance; whole-instance stop requires explicit reconfirmation.
- For OCI diagnostics, default to read-only evidence collection and deterministic reporting.
- For MCP repos, registry, config, policy files, and tests are authoritative; skills are only guidance.
- Do not promise hidden async work or detached execution.
- No open-ended shell access.
- No secrets handling beyond detection and redaction guidance.
- No self-remediation outside an explicit, scoped approval.
