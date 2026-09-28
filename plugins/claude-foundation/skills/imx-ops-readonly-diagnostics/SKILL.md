---
name: imx-ops-readonly-diagnostics
description: "DEPRECATED compatibility shim (legacy triggers retained): review iMX host and application health, logs, and symptoms without changing runtime state. Route this request to imx-ops-readonly-diagnostic."
disable-model-invocation: true
---

# Deprecated compatibility shim

This skill is retained for compatibility. The active replacement is `imx-ops-readonly-diagnostic`
(singular), which now covers this skill's triggers.

Invoke the replacement through the Skill tool using the exact namespaced identifier:

`claude-foundation:imx-ops-readonly-diagnostic`

Do not reproduce or approximate the replacement workflow from memory. If the replacement skill
cannot be loaded, return a failed/escalate result instead of continuing with an improvised workflow.

Continue the user's task using that skill's full workflow, safety boundaries, and output contract.
Also report once that `imx-ops-readonly-diagnostics` is deprecated and scheduled for removal in the
next breaking release.
