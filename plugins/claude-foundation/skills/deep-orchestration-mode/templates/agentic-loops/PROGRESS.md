# Loop Progress

## Current state

- Status: manual setup
- Main objective:
- Current focus:
- Last updated:

## Last run

- Date:
- Trigger:
- Summary:
- Files or systems reviewed:
- Output produced:
- Verification result:

## Facts (verbatim — never paraphrase, never approximate)

Rules:
- Preserve exact values, but never copy secrets, tokens, private keys, credentials, private log
  payloads, or sensitive personal data.
- Use a redacted value plus a source reference when evidence contains protected information.
- observed_at is mandatory for runtime state, current versions, live infrastructure, and other
  time-sensitive facts; it is optional for stable repository facts.
- Do not emit empty placeholder facts; record only facts that exist.

facts:
  - key: ""             # e.g. commit_sha, host, namespace, port, ocid, exit_code, version
    value: ""
    source_ref: ""
    observed_at: ""      # required only for runtime or time-sensitive facts
    revalidate_before: "" # optional
    sensitivity: public | internal | redacted

conflicts:
  - key: ""
    values:
      - value: ""
        source_ref: ""

unknowns: []

## Open items

-

## Blockers

-

## Needs human review

-

## Next run should

- Read `TASK.md`, `PROGRESS.md`, `LOOP_INSTRUCTIONS.md`, and `VERIFY.md`.
- Inspect only the allowed inputs.
- Produce or update only the approved output files.
- Update this file before stopping.
- Run the checker phase before reporting completion.

## Decisions made

- The first loop version is manual.
- The first loop version is read-heavy and write-light.
- Scheduling is not enabled until manual runs are stable.

## Do not repeat

- Do not retry the same blocker indefinitely.
- Do not modify source files unless approval is recorded.
- Do not create extra output files unless the loop instructions allow them.
- Do not expand permissions without human review.

## Audit notes

- <YYYY-MM-DD>: <short note about permission changes, failures, or review decisions>
