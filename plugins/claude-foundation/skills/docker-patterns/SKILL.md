---
name: docker-patterns
description: Use safe, reviewable Dockerfile and container patterns for build, run, image-size, and runtime hygiene work.
---

# Docker Patterns

## Workflow
1. Read project container policy and current Dockerfile/compose/build inputs.
2. Separate build-time and runtime concerns.
3. Prefer multi-stage builds, minimal runtime dependencies, stable base images, non-root runtime where compatible, and cache-aware ordering.
4. Keep secrets out of build context and layers.
5. Change only what the current goal requires.
6. Verify build/config/runtime behavior with repository-native commands.

## Output contract
- Recommended change
- Build/runtime assumptions
- Size/security tradeoffs
- Verification

## Safety boundaries
- No unnecessary privileges.
- No hidden host-state dependency.
- No deployment redesign unless explicitly requested.
