---
name: documentation-lookup
description: Find and summarize authoritative docs, schemas, or repository guidance for the current task.
---

# Documentation Lookup

## Workflow
1. Check whether project source/config already answers the question.
2. Identify the strongest authoritative document/schema/reference.
3. Read only the smallest relevant section.
4. Extract only details needed for the task.
5. Separate confirmed facts from inference and point back to the source.

## Output contract
- Grounded summary
- Source references
- Caveats/unknowns
- Next useful file or command

## Safety boundaries
- Runtime/source evidence wins over stale prose.
- Do not copy long passages.
- Do not create handoff/context files just for a lookup.
