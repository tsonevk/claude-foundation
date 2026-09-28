---
name: project-guidelines-template
description: Use when a repository needs a project-specific onboarding or execution skill that captures architecture, file structure, validation paths, and operational guidance in one reusable template.
disable-model-invocation: true
---

Create a project-local guidelines template from a repository's real structure.

## Goals
- Turn repository knowledge into a reusable project-local guide.
- Capture architecture, source-of-truth files, validation paths, and workflow notes in one place.
- Reduce repeated onboarding and rediscovery work.

## When to use
- A repository has enough stable structure to justify a project-specific skill or guide.
- The same repo is likely to be worked on repeatedly.
- An intake scan already identified the key boundaries and conventions.

## Do not use when
- The repository is too small or unstable.
- The task is a one-off change that does not need reusable onboarding material.

## Template sections
- project purpose and scope
- architecture overview
- important directories and file structure
- source-of-truth files and generated files
- validation commands
- deployment or operational notes when relevant
- risks, unsafe areas, and must-not-touch files

## Output mode B: path-scoped rules bootstrap (.claude/rules/)

When the repo's conventions differ strongly by area (Terraform vs Ansible vs Kubernetes vs
GitLab CI vs iMX/ksh), propose per-topic rule files instead of one long guide:

    .claude/rules/terraform.md
    .claude/rules/ansible.md
    .claude/rules/kubernetes.md
    .claude/rules/gitlab-ci.md
    .claude/rules/imx-ksh.md

Each file starts with YAML frontmatter limiting when it loads, e.g.:

    ---
    paths: ["**/*.tf", "**/*.tfvars"]
    ---

Rules load only for matching files, keeping context cost near zero for unrelated work. This
mode is propose-only: inspect the project first, generate the drafts, and let the user commit
them into the project repo. Never write global user-level domain rules; domain rules are
project-local by design.

## Input expectations
Build the template from:
- repository structure
- `AGENTS.md` and README files
- canonical context files
- validation entrypoints
- operational or deployment docs when relevant

## Output format
Return:
- suggested target file or skill location
- template outline
- exact content draft
- what still needs repo-specific confirmation

## Quality bar
- Prefer repository-specific facts over generic boilerplate.
- Keep it short enough to stay usable during execution.
- Do not invent architecture details that were not observed.
