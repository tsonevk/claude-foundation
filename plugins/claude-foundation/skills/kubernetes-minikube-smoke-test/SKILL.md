---
name: kubernetes-minikube-smoke-test
description: Deploy and smoke-test a containerized workload on a local Minikube cluster, from image loading to rollout, connectivity checks, restart and NetworkPolicy tests, and cleanup, read-first with approval for every mutation.
disable-model-invocation: true
---

# Kubernetes Minikube Smoke Test

## Purpose
- Prove that a Docker or Compose workload runs on Kubernetes (Minikube) before it goes anywhere real.
- Produce pass/fail evidence per check, not a verbal "it works".

## When to use
- Moving a Docker/Compose stack to Kubernetes and a local Minikube is the test target.
- You need a repeatable load-image, apply, rollout, check, cleanup sequence.
- You want to test restart, persistence, or NetworkPolicy behaviour on a throwaway cluster.

## When not to use
- The cluster is shared or production; use `kubernetes-cluster-operations-review` with read-only evidence instead.
- You only need manifest or policy review; use `kubernetes-manifest-review` or `kubernetes-policy-and-access-review`.
- Chart-based releases; use `helm-chart-review`.

## Read first
- Project `AGENTS.md` / `CLAUDE.md` and any current-task or decision-log files.
- The manifests or kustomize overlay in scope, and any host/platform design doc (driver, runtime, pinned versions).

## Operating rules
- Project guardrails win over this skill. If the project forbids applying manifests or touching a host, stop.
- Mutating steps need explicit approval each time: `minikube start/stop/delete`, `image load`, `kubectl apply/delete`, `rollout restart`, deleting pods.
- Read-only steps (version, status, get, describe, logs, dry-run, render) need no approval.
- Never print or record secret values. Secrets are created out-of-band; record names only.
- Reference environment: Linux shell commands only, no hardcoded Windows paths.
- Separate evidence (command output) from inference. Mark gaps `UNKNOWN`.

## Required inputs
- Target cluster context (confirm it is Minikube: `kubectl config current-context`).
- Driver/runtime in use (for example rootless podman + containerd) and pinned minikube/kubernetes versions.
- Image names and where they come from (registry, auth needs, HTTP vs HTTPS).
- Overlay path, namespace(s), service ports, and the request path to probe.

## Workflow
1. **Preconditions (read-only):** `minikube version`, `kubectl version --client`, `minikube status`, `kubectl get nodes -o wide`, disk and memory headroom. Confirm env such as `MINIKUBE_HOME` and, for rootless drivers, cgroup delegation.
2. **Cluster start (approval):** `minikube start --driver=<d> --container-runtime=<r> --kubernetes-version=<v> --cpus=<n> --memory=<MiB>`. Set resources explicitly. Add `--cni=calico` only if NetworkPolicy enforcement is needed and the default CNI does not enforce it (test first).
3. **Images (approval):** check registry reachability read-only first. Then either pull with the host runtime and `minikube image load <image>` (verify with `minikube image ls`), or let the cluster pull with an `imagePullSecret` (and an insecure-registry setting for HTTP registries). Use `imagePullPolicy: IfNotPresent`/`Never` for loaded images. Record digests, never credentials.
4. **Deploy (approval):** render and review (`kubectl kustomize <overlay>`), `kubectl apply --dry-run=server -k <overlay>`, then `kubectl apply -k <overlay>` and `kubectl -n <ns> rollout status deploy/<name> --timeout=180s`.
5. **Smoke tests (read-only):** all pods Ready with no restarts; request through the front service via `kubectl port-forward` (rootless drivers cannot bind ports below 1024); logs reach stdout; dependent services answer (for example `redis-cli ping`); internal DNS names resolve from inside a pod; containers run as the intended non-root UID/GID (`id`); no `OOMKilled` in `describe`; limits applied.
6. **Behaviour tests (approval each):**
   - Restart/persistence: write a harmless marker, delete the pod, check survival against the intended storage choice (emptyDir vs PVC).
   - NetworkPolicy: from a throwaway pod, confirm blocked pods cannot connect and allowed ones can. If everything connects, the CNI does not enforce policies.
   - Read-only root filesystem: watch for write errors to learn the real write set.
   - Multi-stack isolation: deploy a second stack in its own namespace.
7. **Cleanup (approval):** `kubectl delete -k <overlay>` (keeps cluster), `minikube stop` (keeps state), `minikube delete` (destroys cluster and PVs; ask first). Remove throwaway pods and background port-forwards; re-check disk usage.

## Expected output
- A pass/fail table: check, command, date, result.
- Evidence file paths (sanitized, no secrets).
- Items still `UNKNOWN` and the decision each test informs.

## Output contract
- State what ran, what was only planned, and what was skipped.
- Distinguish verified results from assumptions.
- Do not commit or push unless asked.

## Validation guidance
- Prefer `kubectl --dry-run=server` and rendered-output review before any apply.
- Prefer the project's scanners (for example kubesec, trivy) before deploy when installed.

## Rollback guidance
- `kubectl delete -k <overlay>` returns the namespace to empty; the cluster itself is disposable.
- If the cluster is unhealthy, `minikube stop` then inspect before `minikube delete`.

## Verification
- Every claim in the report maps to a command output or an explicit `UNKNOWN`.
- No secret values appear in files or output.

## Safety boundaries
- No mutation without explicit approval; never against a non-Minikube context.
- No production hosts, registries pushes, or credential handling beyond referencing Secret names.
