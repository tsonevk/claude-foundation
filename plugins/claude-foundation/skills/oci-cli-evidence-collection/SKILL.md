---
name: oci-cli-evidence-collection
description: "DEPRECATED compatibility shim (legacy triggers retained): collect deterministic read-only OCI CLI inventory and JSON evidence for diagnostics and handoff. Route this request to oci-evidence-collector."
disable-model-invocation: true
---

# Deprecated compatibility shim

This skill is retained for compatibility. The active replacement is `oci-evidence-collector`, which
now covers this skill's triggers.

Invoke the replacement through the Skill tool using the exact namespaced identifier:

`claude-foundation:oci-evidence-collector`

Do not reproduce or approximate the replacement workflow from memory. If the replacement skill
cannot be loaded, return a failed/escalate result instead of continuing with an improvised workflow.

Continue the user's task using that skill's full workflow, safety boundaries, and output contract.
Also report once that `oci-cli-evidence-collection` is deprecated and scheduled for removal in the
next breaking release.
