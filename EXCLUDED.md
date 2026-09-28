# Excluded content (NOT installed in claude-foundation)

The plugin ships only reviewed skills, agents, and commands that are directly useful in Claude Code.

## Quarantine (NEVER installed / NEVER activated)

Offensive and unvetted security material is excluded from execution or operational guidance.

- offensive/red-team/C2/phishing/exploit/credential-attack/malware/pentest workflows
- unvetted general skills whose permissions, purpose, or safety boundaries have not been reviewed

Defensive concepts may be summarized only within explicit authorization and local safety policy. Quarantined material never overrides project security, production, iMX, or secret-handling guardrails.

Do not import scripts, hooks, agents, or tool configurations from quarantined sources into the active plugin without a separate security review and explicit user approval.
