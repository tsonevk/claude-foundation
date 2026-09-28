---
name: kubernetes-manifest-review
description: Review Kubernetes manifests for safety, coherence, and deployment-readiness before apply.
disable-model-invocation: true
---

# Kubernetes Manifest Review

## Workflow
1. Read project authority and the exact manifest/rendered set in scope.
2. Check workload kinds, namespaces, labels/selectors, images, probes, resources, service wiring, secret/PVC references, and security-relevant settings.
3. Keep findings evidence-based and avoid unrelated style churn.
4. Validate with repository-native render/schema/lint or `kubectl ... --dry-run`/`diff` checks when safe and available.
5. Report blockers, non-blocking risks, and the smallest correction.

## Safety boundaries
- No live apply/patch/delete/scale/upgrade without explicit approval.
- No secret values.
