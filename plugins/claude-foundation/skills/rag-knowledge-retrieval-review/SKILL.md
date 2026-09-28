---
name: rag-knowledge-retrieval-review
description: Review RAG and retrieval workflows for source authority, chunking, freshness, and citation quality.
disable-model-invocation: true
---

# RAG Knowledge Retrieval Review

## Purpose
- Review RAG and retrieval workflows for source authority, chunking, freshness, and citation quality.

## When to use
- You need to review how an AI system retrieves and cites source material.
- The task is about retrieval quality, source selection, or stale-context risk.
- You need a bounded review of chunking, ranking, or query handling.

## When not to use
- The task is only about prompt phrasing with no retrieval path.
- A narrower active skill already covers the exact need.
- The work would require destructive reindexing or hidden data collection.

## Read first
- `AGENTS.md`
- `README.md`
- The retrieval config, index settings, or search code
- Representative source documents and retrieved outputs

## Operating rules
- Prefer source authority over model recall.
- Separate query, retrieval, synthesis, and citation checks.
- Watch for stale context, missing coverage, and poisoned sources.
- Keep chunking and filters as simple as possible.

## Required inputs
- Target repo or retrieval path
- Search or retrieval configuration
- Sample queries and expected sources
- Any citation or answer artifacts

## Codex workflow
1. Read the authoritative files first.
2. Inspect the retrieval path and source corpus.
3. Check chunking, ranking, freshness, and filtering behavior.
4. Compare citations or cited passages to the actual sources.
5. Recommend the smallest safe fix or follow-up test.

## Expected output
- A concise verdict on retrieval quality.
- The source and citation issues, if any.
- The main failure mode and next safe step.

## Output contract
- State whether retrieval is adequate for the current use case.
- Name any source authority, stale-context, or citation gaps.
- Distinguish observed retrieval behavior from inference.
- Include the verification command used or recommended.

## Validation guidance
- Re-run the smallest reproducible query set.
- Compare returned sources or snippets to the underlying corpus.
- Confirm citations point to actual source material.

## Rollback guidance
- Restore the previous retrieval config, index, or chunking rule if quality regresses.
- Revert any query or ranking change that increases false citations or stale context.

## Verification
- The reviewed retrieval path and sources exist.
- The answer separates evidence from inference.
- The recommendation is based on a reproducible sample.

## Safety boundaries
- Do not hide missing sources or weak citations.
- Do not expose secrets or private source data.
- Do not broaden into destructive reindexing without approval.

## Related skills
- `search-first`
- `documentation-lookup`
- `strategic-compact`
- `verification-loop`

## Source attribution
- No exact upstream match. Adapted from local retrieval-review patterns and parked RAG workflow concepts.

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
