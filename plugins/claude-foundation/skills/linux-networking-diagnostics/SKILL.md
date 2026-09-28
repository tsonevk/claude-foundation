---
name: linux-networking-diagnostics
description: Diagnose Linux host IP, routes, DNS, ports, sockets, and connectivity safely.
disable-model-invocation: true
---

# Linux Networking Diagnostics

## Workflow
1. Confirm source host/environment, destination, protocol/port, and symptom.
2. Inspect address, route, DNS, socket/listener, and relevant firewall evidence read-only.
3. Separate DNS, routing, transport, listener, and application-layer evidence.
4. Trace the narrowest path needed.
5. Report proven facts, bounded hypotheses, and the next safe check.

## Safety boundaries
- No route/DNS/IP/firewall mutation without explicit approval.
- No secret/private payload exposure.
