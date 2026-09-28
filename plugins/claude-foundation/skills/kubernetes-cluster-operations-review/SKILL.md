---
name: kubernetes-cluster-operations-review
description: Diagnose Kubernetes runtime and rollout issues with read-only cluster evidence, targeted logs, and safe operational review.
disable-model-invocation: true
---

# Kubernetes Cluster Operations Review

## Workflow
1. Confirm cluster context, namespace/workload/node scope, symptom, and time window.
2. Gather only targeted `get`, `describe`, `logs`, events, rollout, DNS, or storage evidence needed for the issue.
3. Separate pod, node, service/network, image, config, and storage failure domains.
4. Narrow to the smallest supported cause and state remaining unknowns.
5. Recommend the next read-only check or bounded remediation; stop before mutation unless approved.

## Safety boundaries
- No apply/patch/delete/scale/drain/cordon/rollback without explicit approval.
- No secret values.
- Keep cluster scope narrow.
