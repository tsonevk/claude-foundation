---
name: windows-devops-troubleshooter
description: Use this skill when troubleshooting Windows-based DevOps tooling, including VS Code, PowerShell, Git Bash, OCI CLI, Python launcher issues, PATH problems, Claude Code workspace paths, Git remotes, and local repo hygiene.
disable-model-invocation: true
---

# Windows DevOps Troubleshooter

## Purpose
Use this skill for Windows DevOps environment troubleshooting.

Use it for:
- OCI CLI on Windows
- VS Code terminal
- PowerShell / Git Bash paths and quoting
- Python launcher failures
- PATH cleanup
- Claude Code workspace/plugin paths
- Git remote/network access
- local repo hygiene
- Windows-specific command translation

## Environment assumptions
Common workspace root: `~/projects`.
Common shells: PowerShell, Git Bash, VS Code integrated terminal.
Common tools: Git, Python, OCI CLI, VS Code, Claude Code, Docker Desktop or remote Docker context when relevant.

## General rules
- Prefer non-destructive diagnostics first.
- Do not delete paths until evidence confirms they are stale.
- Provide PowerShell and Git Bash variants when useful.
- Be explicit about current directory and path semantics.
- Avoid Linux-only commands unless Git Bash/WSL is actually in use.

## OCI CLI launcher checks
For launcher failures, start with:

```powershell
where.exe oci
where.exe python
py -0p
$env:Path -split ';'
```

Then identify the executable actually used, verify its Python target, remove only confirmed stale launchers, reinstall cleanly when required, and validate with `oci --version` plus a safe read-only command.

## Git remote/network checks

```powershell
git status --short --branch
git remote -v
git ls-remote origin
nslookup gitlab.com
nslookup gitlab.codixfr.private
ipconfig /flushdns
```

If behavior differs between Claude Code and a normal terminal, investigate shell/environment/network-context differences first.

## Path styles
Windows: `<home>\\projects\\repo`
Git Bash: `~/projects/repo`
WSL: `/mnt/c/<Windows-user>/projects/repo`

## Output contract
Diagnosis; likely cause; commands to verify; safe fix; validation; rollback.

Use copy-paste-ready commands and do not assume admin rights unless required.
