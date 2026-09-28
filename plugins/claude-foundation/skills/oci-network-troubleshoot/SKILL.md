---
name: oci-network-troubleshoot
description: Use when investigating OCI connectivity issues involving load balancers, NSGs, security lists, route tables, private/public endpoints, ACL whitelisting, ICMP tests, curl reachability, or cross-network connectivity. Do not use for purely application-layer bugs with already confirmed network reachability.
disable-model-invocation: true
---

Investigate the network path systematically and avoid guessing.

## Goals
- Separate network-layer failure from application-layer failure.
- Request or run the smallest proving tests first.
- Produce an evidence-based conclusion.

## Workflow
1. Identify source, destination, port, protocol, and whether traffic is public or private.
2. Check DNS resolution and whether the resolved address is expected.
3. Review likely control points:
   - route tables
   - security lists
   - NSGs
   - subnet placement
   - LB listeners and backend reachability
4. Prefer proving commands first:
   - `ping` or ICMP tests when relevant
   - `curl -Iv`
   - route or traceroute equivalent when available
   - listener or port checks
5. Separate:
   - cannot reach endpoint
   - can reach endpoint but app fails
6. Produce the most likely failing layer and next corrective actions.

## Output format
Always provide:
- probable failing layer
- evidence already available
- missing evidence still needed
- exact commands to run
- likely fix candidates

## Quality bar
- Do not jump directly to firewall-only explanations without checking resolution and path.
- Prefer explicit evidence requests when data is incomplete.
- Keep the conclusion short, practical, and testable.

## Related skills
- `oci-networking-diagnostics` — read-only topology/config evidence review (VCN, subnet, route, DRG, LPG, VPN); this skill is active connectivity investigation (LB, NSG, ACL whitelisting, reachability tests).
